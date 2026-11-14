# Actual request46 readback: request42 stopped at 32 working rows and used a real internal radial repair

## Completed readback, with original computation unchanged

The request42-only reader in [run 43628475946](https://github.com/Rogerhu12/math-research-public/actions/runs/43628475946), job `132549570796`, completed using source `e19cc023cdf990ccf56c548f0d32f50faedea822`. It did not fetch or rerun the separate original stage41 computation. Its [v3 target summary](public-actions-43628475946-1-receipts/request42-receipt-summary-v3.json) reports `completed: true`, no missing mandatory target paths, and zero scientific evaluations.

The published summary is 34,482 bytes with SHA256 `350b9a95aea7853f63c26552b889f5e66fe561af7ff25d181b9e92e6e9c954d2`. These retrieved UTF-8 bytes were independently hashed and match the [publication ledger](public-actions-43628475946-1-receipts/publication.json), recorded at 2026-11-14 18:46:51.905428 UTC. The complete selected derived metadata was saved first in the Actions artifact as a 7,098-byte gzip, SHA256 `9b6218b319b737788a9f8ed352ecff95d542b993f0c7e41db31b2a8b83f9d32b`; it was deliberately not published as a second transport copy.

The reader source SHA256 is `f80608b3f8eec01a505b0698d0696905fb1191dd18e4a9707b55d6ac1b37e810`. Its original pin/helper source is the frozen v1 SHA256 `dd01f051731af09cbc4a2ee05fe36536303692e3add5a6ce87724620fd8dee74`. All seven original request42 file SHA checks passed. In particular, the original full helper report remains `0e57a7c02c2f1ceb85538ae5e0b33db532ac2139b17caf730ed90c1926a29884`.

This note fills the explicitly missing internal helper facts in the [actual request42 note](2026-11-14-actual-request42-complete-QR-32-row-warm.md). It does not assert an independent byte audit of the original request42 ZIP, large basis/slack arrays, or all 33 inverse vectors. The [actual request44 failure](2026-11-14-actual-request44-request42-summary-transport-failure.md) remains a failed earlier summary transport attempt.

## Actual stop and finite work

The saved original helper report gives:

| Original report field | Saved value |
| --- | --- |
| `active_stop_reason` | `maximum-32-or-requested-working-row-budget` |
| Maximum and actual working rows | 32 |
| Actual basis columns | 34 |
| Saved active stages | 33 |
| Helper elapsed seconds | 123.91190181600001 |
| Complete original H calls | 33 |
| Original A / AT / B / BT calls | 212 / 105 / 181 / 102 |
| Declared total H budget | 1200 |
| Full QP optimality claimed | false |

This is an observed working-row stop, not a deadline or H-action-budget stop. The full computation still used 236,036 coordinates and all 24,576 supplied inequality rows for the actual feasibility checks.

At stage32, the restricted stationarity norm in the saved reduced Gram is `2.584650659434717e-16`. The dual loop completed its declared 200 sweeps and reported `maximum-dual-sweeps`; its final H-normalized multiplier update is `2.298152069312693e-17`, minimum predicted working-row slack `-7.105427357601002e-15`, and maximum predicted relative working-row violation `1.3173082728724632e-12`.

The actual original A action differed from its basis combination by at most `2.220446049250313e-16`, and the actual B action by at most `4.218847493575595e-14`, as saved in the original report. These are finite diagnostics, not exact KKT or interval certificates.

## Last unrepaired point and the actual internal repair

The original stage32 evidence contains:

| Quantity | Unrepaired stage32 point |
| --- | ---: |
| Same damped-model objective | 43.73844101866751 |
| Model directional derivative | -1.0930539818129938 |
| Model decrease | 0.5467774931602041 |
| Complete original stationarity L2 with the saved dual | 1.1108597040659078e-8 |
| Complete original stationarity Linf | 5.0501827299248e-9 |
| Minimum original slack | -30.72964417841071 |
| Maximum relative primal violation | 125.72232273744466 |
| Negative original slack entries | 1668 of 24576 |

The negative-entry count is copied from the original radial-repair attempt's saved full-slack summary; it was not recomputed from an array here. The original full slack is identified by SHA256 `1380cd5020a645b29e0bba66198736e5bb3060879ae67eaf6898d8966f108c46`. This reader does not identify new worst-row labels or angles.

The true internal all-row radial factor is **0.007891269496944752**. The original attempt records its pre-headroom factor as `0.007891269496944867` and the same relative violation `125.72232273744466`. After that single repair, all 24,576 stored slacks are nonnegative, with minimum `3.3584246494910985e-15`.

The repaired objective is `44.27662694608533`, its original derivative is `-0.008625583545194881`, and its model decrease is `0.008591565742343087`. Its complete original stationarity L2 rises to `992702.5381993352`. That final large residual describes the repaired feasible direction with the radially scaled dual; it must not be substituted for the original QR inverse residual or the stationarity of the unrepaired working-row solution.

The subsequent original selector has projected-candidate repair factor1, segment parameter1, and composed-vector repair factor1. Those later unit factors do **not** mean that the helper avoided its earlier substantial internal shrink.

The close working-row and full stationarity diagnostics together with the large all-row violations support the specific remaining obstruction: the 32-row subproblem did not enforce the other supplied inequalities. This evidence does not prove that any larger fixed budget would solve the full QP, nor that the nonlinear boundary problem would then converge.

## Actual accepted warm step and scope

The selected H candidate had a smaller same-model objective than the retained C candidate, whose objective was `44.28320644526789`. The original nonlinear trial accepted alpha1 with actual fixed-weight merit `44.27560683679009`, reduction `0.009611675037582756`, and actual/predicted ratio `1.116352932052175`. All original node, midpoint, and both RMS-query checks passed. These are the original request42 values, copied without re-evaluation.

The actual saved warm remains SHA256 `3dd623e90edb97ff113bebddd09445d64b916626a8fb1821fd35e69beabdc317`. Its FD report still gives `7.171478513023801e-10` against the unchanged `5e-5` implementation-check threshold. The producer expressly records `success: false`, `new_coupled_finite_acceptance: false`, and no nonlinear native solve at that new height.

The R267 best raw floating lower-bound value is `43.73844101866751`; the final reported gap is `0.5381859274178211`. These remain floating diagnostics, not validated lower-bound enclosures.

The independently dispatched condensed-QP attempt continues from this actual request42 warm. Its model has refreshed weights and a different base field; none of the request42 objectives or matrices are silently treated as the same fixed model in that later experiment.
