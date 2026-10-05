# User brief and comparison

## Intended user and painful task

Maintainers preparing a static site URL migration. A finite planned redirect map can form a loop, extra chain or destination not present in the deployment manifest before the site is reachable.

Current alternatives: Live lychee, broken-link-checker or LinkChecker crawling; manual map review.

Evidence and limits: The researched tools document live link checking. Offline pre-deployment map demand is inferred, and their absence of equivalent features is not established. No fabricated customers, requests, adoption, testimonials or growth promise.

## Smallest useful capability and acceptance criteria

Detect cycles, missing declared terminal pages, over-budget chains and duplicate sources; report complete path evidence without HTTP requests.

Runnable acceptance fixtures are `test_redirect_graph.py` and `demo.py`. Invalid inputs must return an explicit failure, and diagnostics must preserve source files where the contract is read-only. See README for supported subsets and bounds. Plausible discovery path: static-site and redirects topics; checked-in before/after map example.

## Live leader research on 5 October 2026

Queries `redirect checker`; `redirect in:name` were requested from live GitHub sorted by stars descending. Search receipts include exact query URLs, observation times and top-ten metadata in [research-evidence.json](research-evidence.json). Irrelevant broad matches were rejected: map fonts/geospatial tools are not JavaScript source-map comparables, browser redirect extensions are not site migration analysis, and unrelated notebook/diffusion matches are not notebook hygiene tools.

Highest-star relevant comparable found among the researched set: [lycheeverse/lychee](https://github.com/lycheeverse/lychee) with 3979 stars. Some established comparables were added outside the narrow search query. This is bounded search coverage, not an exhaustive global ranking. Stars are a discovery signal, not a performance/reliability result.

| Comparable | Stars | Last observed push UTC | License metadata | Workflow, install, docs and tradeoff |
| --- | ---: | --- | --- | --- |
| [lycheeverse/lychee](https://github.com/lycheeverse/lychee) | 3979 | 2026-09-28T16:58:58Z | Apache-2.0 | Rust live link checker, documented brew/cargo and standalone usage, redirects and JSON output. It verifies reachable URLs, while this MVP checks a supplied exact-path graph. |
| [stevenvachon/broken-link-checker](https://github.com/stevenvachon/broken-link-checker) | 2082 | 2026-09-07T12:39:18Z | MIT | Node library/CLI, documented npm installation and HTML links, redirects, compression and authentication. Issue 266 concerns dependencies; no current vulnerability conclusion drawn. |
| [linkchecker/linkchecker](https://github.com/linkchecker/linkchecker) | 1076 | 2026-09-22T04:13:11Z | GPL-2.0 | Recursive multithreaded website/link crawler with several report formats. README describes features and support links. Installation behavior not measured. |

Current READMEs and the returned recent issue/PR samples were inspected. Samples may be maintainer PRs, not genuine user requests. Support channels and examples are visible; support responsiveness, actual installation reliability and time to first useful result of comparables were not measured. License metadata marked unresolved/unavailable is not a permission to reuse. No competitor code or prose is incorporated.

## Distinctness and rejected directions

Compared with all 133 owned repository names, descriptions/READMEs for overlapping tools and yesterday's five launch briefs. The five new products handle saved notebook state, planned redirect graphs, exported LFS bytes, content-bound JSONL record references, and generated-code source positions respectively. They share packaging, not one subdivided product.

Existing json-differ/log-parser/traceweave analyze different JSON or agent-trace semantics; urlnorm normalizes URLs; syncplan plans filesystem synchronization; wheel-sentinel validates Python wheel archives; portable-tree audits names. This candidate's user contract is separate. Environment checking was rejected because envdiff/env-vault/dotenv-mini already cover it; another archive checker was rejected as overlapping Wheel Sentinel.

## Fairness and limitations

Exact local paths only, case sensitive and percent encodings unchanged. No pattern, query, fragment, external URLs or web reachability checks. 2 MB / 10,000 rules; graph traversal worst case quadratic. Terminals are user supplied, not verified deployments.

There is no measured competitor benchmark or superiority claim. Local examples establish our behavior only. No claim is made that a competitor lacks this capability. Broader established tools can be better choices when their workflow/dependencies fit. Evidence dates, installed behavior and untested limits remain separate.
