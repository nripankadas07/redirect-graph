"""Audit a finite exact-path redirect map before deployment."""
import argparse,json,pathlib

def path(value):
    if not isinstance(value,str) or not value.startswith('/') or value.startswith('//') or any(ord(c)<33 for c in value):
        raise ValueError('paths must be local absolute paths without whitespace')
    if any(c in value for c in '*?#\\'):raise ValueError('wildcards, query, fragment and backslash are unsupported')
    if any(c in value for c in '{}'):raise ValueError('pattern rules are unsupported')
    if any(s in ('.','..')for s in value.split('/')):raise ValueError('dot segments are unsupported')
    return value

def analyze(rules,terminals,max_hops=1):
    if not isinstance(rules,list)or len(rules)>10000:raise ValueError('rules must be a list of at most 10000')
    if type(max_hops)is not int or max_hops<1:raise ValueError('max_hops must be positive')
    if not isinstance(terminals,list):raise ValueError('terminals must be a list')
    pages={path(x)for x in terminals};graph={}
    for rule in rules:
        if not isinstance(rule,dict)or set(rule)!={'from','to'}:raise ValueError('each rule needs exactly from and to')
        source,target=path(rule['from']),path(rule['to'])
        if source in graph:raise ValueError('duplicate source: '+source)
        graph[source]=target
    result=[]
    for start in sorted(graph):
        trail=[start];visited={start};cur=start;kind=None
        while cur in graph:
            cur=graph[cur];trail.append(cur)
            if cur in visited:kind='cycle';break
            visited.add(cur)
        if kind is None:
            if cur not in pages:kind='missing_terminal'
            elif len(trail)-1>max_hops:kind='long_chain'
        result.append({'source':start,'path':trail,'hops':len(trail)-1,'issue':kind,'terminal':None if kind=='cycle'else cur})
    return {'routes':result,'findings':sum(x['issue']is not None for x in result)}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('map');p.add_argument('--max-hops',type=int,default=1);a=p.parse_args()
    try:
        with pathlib.Path(a.map).open('rb')as f:raw=f.read(2_000_001)
        if len(raw)>2_000_000:raise ValueError('2 MB map limit exceeded')
        j=json.loads(raw)
        if not isinstance(j,dict)or set(j)!={'rules','terminals'}:raise ValueError('expected rules and terminals')
        r=analyze(j['rules'],j['terminals'],a.max_hops);print(json.dumps(r));return int(bool(r['findings']))
    except (OSError,ValueError,TypeError,RecursionError)as e:print(json.dumps({'error':str(e)}));return 2
if __name__=='__main__':raise SystemExit(main())
