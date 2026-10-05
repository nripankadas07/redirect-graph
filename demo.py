from redirect_graph import analyze
import json
r=analyze([{'from':'/old','to':'/middle'},{'from':'/middle','to':'/new'}],['/new']);assert r['findings']==1;print(json.dumps(r))
