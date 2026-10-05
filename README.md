# redirect-graph

Offline exact-path redirect graph audit for loops, excess hops and missing destinations.

## Install and first useful result

```bash
git clone https://github.com/nripankadas07/redirect-graph
cd redirect-graph
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/python demo.py
.venv/bin/redirect-graph --help
```

Python 3.10 or newer. The example creates synthetic inputs; it needs no account, service, token or downloaded dataset. Runtime uses only the standard library. Building requires setuptools from the package registry. POSIX commands above; Windows/macOS installation has not been tested.

## Useful contract

Detect cycles, missing declared terminal pages, over-budget chains and duplicate sources; report complete path evidence without HTTP requests.

Import `redirect_graph` for the function used by `demo.py`, or use the installed CLI described by `--help`. JSON reports print to stdout. Exit 0 means the documented success condition, 1 means diagnostic findings or an unmapped source position where applicable, and 2 means invalid input or I/O failure. JSONL indexing uses 0/2 only; LFS returns 2 when no pointers were found.

## Limits

Exact local paths only, case sensitive and percent encodings unchanged. No pattern, query, fragment, external URLs or web reachability checks. 2 MB / 10,000 rules; graph traversal worst case quadratic. Terminals are user supplied, not verified deployments.

No performance or superiority claim. Demand is inferred. See [research and acceptance criteria](RESEARCH.md), [validation](VALIDATION.md) and [support and security](SUPPORT.md). MIT license; implementation and synthetic fixtures are original. Comparables inform scope; no competitor code or prose is incorporated.

## Development

```bash
python -m unittest -v
python -m compileall -q redirect_graph.py
python demo.py
```

## CLI input

Save `redirects.json` as `{"rules":[{"from":"/old","to":"/new"}],"terminals":["/new"]}` then run `redirect-graph redirects.json --max-hops 1`. An exact source path can appear once. Terminal paths come from your planned page inventory, not HTTP probing.
