# Request79: one same-24-query relinearization from the actual76 warm

**Classification:** verified source/input binding and a proposed numerical continuation. The numerical motivation is copied from actual76; this preparation did not execute a new model or mathematical calculation.

**Author:** amplitude branch of the visible-flex-larger-amplitude session, 2026-11-15 UTC.

## 1. Decision and actual evidence

Use the same frozen 24-query entry for one model at the actual76 new warm. Do not add a 25th query, change damping, increase a budget, or alter an original domain/merit/FD rule.

The [actual76 conclusion](2026-11-15-actual-request76-twenty-four-query-quarter-step.md) records an accepted $\alpha=1/4$, actual fixed-weight decrease `0.09093417026150519`, ratio `0.9927567534550313`, valid original node/midpoint/two RMS checks, and FD maximum `8.532100047207813e-10`. The nearest rejected half-step had original midpoint486 invalid and the already modeled selected left-RMS466 grid invalid. The full original RMS pass and actual merit were not evaluated for that half-step. Consequently, the next request does not assert that adding midpoint486 would remove its complete limitation.

The new base is a real saved optimization warm, while `success` and `new_coupled_finite_acceptance` remain false. Its fresh model will get its own original fixed weights; no cross-model subtraction of merit is used to predict success.

## 2. Exact parent pair and transparent status transport

The parent is run `43661532089`, source `1377826d89317b491f75036cafd63c3ea5bea5f1`, with published directory:

```text
notes/public-actions-43661532089-1-condensedqp/twenty-four-condensed-warm
```

| Parent object | Bytes | SHA-256 |
|---|---:|---|
| `warm-001.json.gz` | 4858829 | `bba24c1f882d14751c4272148ee0cd6271c584485c6d0d3efaafa1a081a2a97f` |
| Original `driver-status.json` | 2331066 | `a1a67b9a1e0e97aa23404a8fa6c5936805de34f763f0076516c4f736aedc4cb5` |
| Published `driver-status.json.gz` | 276520 | `d8e9133a002280ff7f116738a53203ff273681414ec8aae2405ced1ee5726c8d` |

The workflow accepts the original status or its existing transparent gzip alias. It checks the original JSON size/SHA in either case, and also checks the exact compressed size/SHA whenever the gzip alias is used. If both aliases exist they must decode to identical original bytes. It writes the recovered JSON bytes directly; it does not reserialize them. The compressed warm bytes are copied unchanged.

The parent schema is already `exact-constraint-twenty-four-query-condensed-complete-H-warm-v1`. The frozen entry's own-schema branch therefore applies, rather than its initial actual74/twenty-three-schema branch. The original paired-status and complete producer validation remain active. In the source, the initial actual74 constants and the left485 addition describe the introduction of the frozen 24-query representation; they are preserved as history, not misrepresented as the new current parent. The request separately records this history and makes `new_queries_added: false`, `added_query: null`, and the actual76 current pair explicit.

## 3. Unchanged sources and model

All 51 workflow source pins are byte-for-byte identical to actual76, including publisher `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`. The four current scientific sources remain:

| Source basename | SHA-256 |
|---|---|
| `geometry_20261114_twenty_four_query_domain_operator.py` | `06933e9341664d63b5a9eaeb00998daa1be7b1c1d143a60f1ae2ef05efa9db36` |
| `geometry_20261114_twenty_four_query_condensed_warm.py` | `b453b53d4ae759e0bc50d5d789beb04e53c18903adaf427c2a28c0382827d452` |
| `geometry_20261114_twenty_four_query_condensed_response.py` | `87261854684d5844c97d59b328db2aa070b015b565baf46dfb7e811808b3bb87` |
| `geometry_20261114_twenty_four_query_collocation_observer_warm.py` | `f6639751ea97bd857ad05ad0a36d38d11024dac25f6ecc0610fef2d9fe90cf35` |

The independent completed-artifact reader remains `root_20261114_read_completed_twenty_four_prefix.py`, SHA `1aa4da4e721aa12a9f4d6257e3a6b6a7b328059de217ba42268d73a018e9828c`; this request does not change or rerun it as an acceptance gate.

All 16 left RMS grids and eight collocation-midpoint grids remain in the same typed order, each with the complete original 2048-angle rule. B has 49,152 rows and actual/declared local dimension 7,101, containing nodes 466 through 486 and the three shared controls, with no zero-layout columns. Its 16 captured intervals and 21 actual endpoints remain unchanged. The original 4,059-dimensional C baseline retains all outside contributions. R270 still optimizes and recovers the full exterior response, all free core coordinates and the original affine term.

The runtime, source restoration, original M112 preparation, complete real T112 zero-H affine reference, original full physical-angle boundary equations, observer semantics and original FD computation remain identical. A new native nonlinear solve is not requested.

## 4. Budgets and invocation

| Existing setting | Request79 value |
|---|---:|
| Complete model calls | 1 |
| Damping | 270 |
| LSMR iterations / C projection sweeps | 200 / 200 |
| Original line-search trials | 17 |
| Overall budget | 1200 seconds |
| Condensed candidate budget | 600 seconds |
| Trial reserve / full recovery reserve | 90 / 30 seconds |
| Maximum working rows / dual sweeps | 512 / 200 |
| Material/boundary angle count / Jacobian workers | 4096 / 2 |

The scientific warm invocation is exactly the actual76 invocation after replacing only the parent path variable and its two expected hashes:

```text
--resume "$VISIBLE_PARENT76/warm-001.json.gz"
--expected-resume-sha bba24c1f882d14751c4272148ee0cd6271c584485c6d0d3efaafa1a081a2a97f
--parent-status "$VISIBLE_PARENT76/driver-status.json"
--expected-parent-status-sha a1a67b9a1e0e97aa23404a8fa6c5936805de34f763f0076516c4f736aedc4cb5
```

The output stays `twenty-four-condensed-warm/`. After one actual decreased warm is saved, the unchanged response step consumes its actual path and SHA and redoes the original complete boundary FD. No old FD result is relabeled. All trial failures, real midpoint/RMS/physical-row observations, producer history, root arrays and reports remain preserved by the existing workflow and publisher.

## 5. Minimal workflow diff and source-only checks

The exact actual76 workflow and request were read at source `1377826d89317b491f75036cafd63c3ea5bea5f1`; their byte hashes match the previously delivered actual76 drafts. The new files are `visible-larger-public-condensed-qp.yml` and `public-condensed-qp-request.json`, with full diffs against those exact baseline files.

Only parent sparse-checkout paths, transport length/hash checks, parent schema/current-source metadata, environment variable names, labels and the request's actual evidence change. The warm command comparison proves that all other command text is identical. The complete response step is byte-identical. All 51 source pins, the existing unique trigger, concurrency policy and runtime environment are unchanged.

The trigger remains the original repository path:

```text
topics/visible-flex-larger-amplitude/computations/public-condensed-qp-request.json
```

Preparation checked the real parent warm and both status identities, transparent decompression, the complete status-to-producer subset, source hashes and Python AST, eleven shell syntaxes and six inline Python AST blocks. These are original-byte and source checks only. No scientific module was imported, no RHS/Jacobian/matrix action was evaluated, and no repository or dispatch was changed by this preparation. The detailed receipt is `request79-static-check.json`.

Request79 remains a single experiment at a new base. Its result must be read from its actual complete trials and original merit/domain/FD outputs; neither a larger step nor eventual full BVP acceptance is assumed.
