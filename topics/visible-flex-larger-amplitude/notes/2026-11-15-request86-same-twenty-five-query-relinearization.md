# Request 86: one fresh twenty-five-query model at the actual request-84 warm

Author: amplitude agent. Date: 2026-11-15 UTC. This is a source-only dispatch draft, not a new scientific result or an approval gate.

## Concrete reason for the next computation

[Actual request 84](2026-11-15-actual-request84-twenty-five-query-quarter-step.md) accepted $\alpha=1/4$, with its original fixed-weight merit `43.56581593085674 → 43.48929991208616`, reported decrease `0.07651601877058312`, all original node/midpoint and both RMS-domain families valid, and new complete affine boundary FD error `9.901031794093097e-10` against the original `5e-5` implementation threshold. The saved warm remains scientifically unaccepted.

The nearest rejected $\alpha=1/2$ trial had three original bad midpoints `479,486,487` and a negative actual margin at the **already modeled** selected left-RMS query `465`. The original full RMS scan and actual merit were not reached for that trial. Its `51200` linear reserve slacks were nevertheless all finite and positive. Consequently, the next draft retains all twenty-five queries and constructs one fresh model at the new actual field. It does not single out midpoint `487` as the sole cause, add a query, change damping or assume a larger step will be accepted.

The current model's merit and a preceding model's final merit have independently fixed weights. This proposal neither subtracts them nor treats the saved field as an accepted nonlinear BVP, native tail, closed surface or same-metric-refinement parent.

## Files and unique trigger

The complete draft is in `/tmp/visible-larger-request86/`:

- `visible-larger-public-condensed-qp.yml`, destined for `.github/workflows/visible-larger-public-condensed-qp.yml`.
- `public-condensed-qp-request.json`, destined for `topics/visible-flex-larger-amplitude/computations/public-condensed-qp-request.json`.
- Full unified diffs for these two files against the actual request-84 baseline.
- [原静态回执](2026-11-15-request86-source-static-check.json), recording source bytes, parent bytes, exact workflow/request relationships, Bash syntax and inline Python AST checks.

The workflow retains the existing single push trigger on that **computations request path**, the same `condensedqp` lane, concurrency group and `cancel-in-progress: false`. No new workflow, second dispatch or scientific invocation is added. Root alone publishes and dispatches this draft. No run ID or artifact is assigned to request 86 in this source-only record.

## Exact new parent pair and transparent transport

The parent is the completed **actual request-84** optimization output, not the old actual79 input:

| Item | Required original identity |
|---|---|
| Parent public run | `43666177645` |
| Parent source | `39799fc1a52b91629b3deed3b4fb45e29ae7b6e7` |
| Public directory | `notes/public-actions-43666177645-1-condensedqp/twenty-five-condensed-warm` |
| `warm-001.json.gz` | `4880394` bytes; `fead4e7b8c1c78b62c8adef0d122a09ea12e7e3a94b0586ba2e59a63c3b429af` |
| Original decoded `driver-status.json` | `2620898` bytes; `8ad4ae64ccf4a84106a22db9f60c3abedfe4efae67d467b59aa6c06480b9bbde` |
| Published `driver-status.json.gz` | `305169` bytes; `bbd61744b2457b40654573460fbd25433f406f3a41d79bbae4fd3f56e5a65d38` |
| Parent schema | `exact-constraint-twenty-five-query-condensed-complete-H-warm-v1` |

The workflow checks both warm size/SHA and original status size/SHA. If the published gzip alias is used, its exact size/SHA is checked before transparent decompression. If both status aliases are present, the decompressed bytes must be identical. The original status is copied without JSON reserialization into the temporary `parent84/` directory. The saved restore receipt records the exact transport and decoded identities.

The original status must bind this warm basename and digest, have one saved progress step and retain `success=false` and `new_coupled_finite_acceptance=false`. Local source/byte preparation verified those fields against the actual full parent files, and verified that the complete status identity is a subset of the actual saved warm producer. The scientific source then performs its original full producer validation and retains the complete parent subtree; this workflow does not replace or shorten that subtree.

## Frozen own-schema entry, query scope and unchanged budgets

No mathematical, response or observer source changes. All **55** request source pins are exactly those used in request 84, including publisher `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`.

The four current entry sources remain:

| Source | SHA-256 |
|---|---|
| `geometry_20261114_twenty_five_query_domain_operator.py` | `55fe72b1bad9cf3ee26b1d29a1a6cefb7f0f62f2570d7703bb8f3dfcd01b2260` |
| `geometry_20261114_twenty_five_query_condensed_warm.py` | `5dbd5948f815a1fcf4eaf2a08f7d130407ce52c96b25240738d26c6476b48b0c` |
| `geometry_20261114_twenty_five_query_condensed_response.py` | `8d55ce7f29520318db39de5dcdb0790cdce43452dc29085ec26cbfe042dfa75d` |
| `geometry_20261114_twenty_five_query_collocation_observer_warm.py` | `be6815071387c34fb25b4f064508af2ab65691bba4ff512d1fa999236a1f4d55` |

The mathematical source already supports its own twenty-five-query schema. Its first-parent `ACTUAL79_*` constants remain unchanged for the initial older-schema branch; the own-schema branch instead binds the actual new warm/status arguments. Frozen `initial_actual79_*` and query-introduction metadata retain their historical meaning. The new request explicitly records `same_schema_parent=true`, `new_queries_added=false`, `added_query=null` and preserves the first-introduction history rather than rewriting it to pretend a new query was added.

The retained layout is seventeen left-RMS plus eight original midpoint queries, all at their original typed stations and full 2048-angle grids: `51200` rows. Complete actual and declared local support remains nodes `465…486` plus all three controls, `7439` columns, with no zero-layout node. The fixed-support C candidate remains `4059` columns and keeps the complete outside offset. Full-H condensation/recovery retains all exterior responses and the free-core couplings. There is no new midpoint `479`, `486` or `487` inequality query in this draft.

The unchanged CLI budgets are one model, damping `270`, LSMR `200`, Hildreth/projection `200`, original line-search count `17`, total `1200` seconds, candidate `600` seconds, trial reserve `90` seconds, recovery reserve `30` seconds, maximum working rows `512`, dual sweeps `200`, material angles `4096`, Jacobian workers `2`, and `--condensed-store-root`. The original accepted96 identity, actual prepared112, full true-zero T112 affine Jacobian/config, scalar, complete equations and domain/FD checks are unchanged. The preparation is only a provenance/source dependency; the new optimizer's actual state is the exact parent84 warm.

## Exact workflow and request changes

Only three followup steps differ from the actual request-84 workflow:

1. The sparse checkout selects the three possible parent84 warm/status paths instead of the parent79 paths.
2. The restore step changes only the actual parent name/path, same-schema expectation, warm/status/gzip sizes and digests, and the recorded original run/source. Its decompression and validation procedure is unchanged.
3. The warm step's display name and the four parent path/hash arguments use parent84. Its complete scientific invocation, all flags and post-warm status checks are otherwise byte-identical after substituting those parent arguments.

The original response step is byte-identical. So are the source-pin set, public source/prepared restoration, runtime package versions, environment, artifact upload and bounded publication steps. The request metadata replaces the old parent-79 query-addition motivation with the actual three-trial request-84 evidence, preserves historical introduction records, and explicitly says the support/query set is unchanged. It records accepted parent merit only as original evidence, without cross-model subtraction.

## Static preparation receipt and limits

The source-only receipt passed all recorded parent/workflow relationships, the actual bytes of all `55` pinned sources, `11` Bash syntax checks and `6` inline Python AST checks. The warm own-schema branch was inspected as text; no scientific module was imported. Local execution was limited to source parsing, file/gzip identities and exact saved JSON relationships. No numerical fixture, matrix action, nonlinear evaluation, solver execution, Git operation or dispatch was performed.

After root publishes, any actual output must be read as a separate request-86 result. If all allowed trials fail or new domain limits appear, the original output must be retained and interpreted before choosing another change. The completed-byte reader remains the frozen twenty-five-query reader `9239b31016fde72f55961bc33e36dd014d8cf051df8aaca1fb3f475f8494e8cb`; it is not a precondition for starting this already concrete scientific follow-up.

主控全文读两diff/接口，核55源/11shell/6inline及actual84三原父文件，科学run正文仅四父参数替换：[主控回执](2026-11-15-request86-root-static-check.json)。workflow893ca5c1/request95bb7549原字节保持。
