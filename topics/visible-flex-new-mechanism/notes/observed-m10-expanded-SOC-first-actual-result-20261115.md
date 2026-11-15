# First completed expanded-pool SOC on the observed m10 failed trial

Date: 2026-11-15 UTC. This is a new, completed application of the frozen expanded-pool SOC to one previously observed failed trial. It does not rerun the old primary optimizer, advance the current best checkpoint, or establish convergence.

## 1. Actual result

Public [run43750302276, job132922557741](https://github.com/Rogerhu12/math-research-public/actions/runs/43750302276/job/132922557741), source **b2d9ce66118948254c9c8fa376092c41b807ec62**, completed successfully. The scientific status is:

    complete-historical-m10-expanded-SOC-accepted

The single newly solved SOC repaired the historical m10 curvature violation while preserving the failed trial's reported coarse/fine eta values. Its corrected point was accepted against the historical base \(x\), then independently re-evaluated on both complete grids.

| Quantity | Historical accepted \(x\) | Original failed \(y\) | Newly corrected \(z\) |
|---|---:|---:|---:|
| Maximum eta on both grids | 0.26636800393715654 | 0.2663651531755449 | 0.2663651531755449 |
| Coarse maximum absolute curvature | — | 58.00000333192753 | 57.99996262976777 |
| Fine maximum absolute curvature | — | 58.00002409366549 | 57.99998339149647 |
| New coarse/fine row counts on the trial | — | 1 / 1 | 0 / 0 |
| Accepted under the original recovery gates | Yes | No | Yes |

The true two-grid eta decrease relative to \(x\) is
**0.000002850761611661312**. The two complete-grid eta values at \(z\) are respectively
0.2663651531755449 and 0.2663651530478497, equal to their values at \(y\) in the emitted binary64 records.

Both independent final evaluations pass the original hard and previous metric recovery gates, and the original physical box is checked exactly without clipping. The new metric target is still false on both grids. The reported maximum curvature is **57.99998339149647**.

This is a result for the historical \(x\to y\to z\) branch. It is not claimed better than the later current global-best point and is not a certificate for continuous metric bounds, embedding, or whole-surface reach.

## 2. Evidence and source identity

| Original public object | Bytes | SHA256 |
|---|---:|---|
| Complete decoded job log | 4,071,522 | 8238f26dc3f436564da3afb7657f00c3d33160476b81b8602342a9f29ff127f6 |
| M10_SOC_CACHE_DEVELOPMENT JSON plus LF | 16,834 | 770095c5f0d7c3992c1ad698ab5439806f1be18d15120f91ecf6dff9a459f5cb |
| M10_SOC_COMPLETE JSON, no LF, as bound by REPORT_METADATA | 3,024,903 | 71ca64dae2831239eafb2ae1b011db3878f3d8764174b40c0f0bae0620d4a32b |
| Same COMPLETE JSON plus LF | 3,024,904 | 39b6a1f3c3deaf3f4ea87f00bf4c9ea500c015e879f4fd7b329aa12233fa1117 |
| Runner temporary audit.json | 5,204,571 | f5e0432624c4b658536045922fdcb102e075628bb4522c12e4fa36d9183f4330 |
| Runner temporary audit-summary.json | 1,027,564 | a45b8cdd2b0fb248f12e76bbb0470ec299844e117d84651ed260c8c4527232e5 |

The parsed original COMPLETE bytes agree with its emitted byte count and hash. The pretty temporary JSON and compact stdout JSON are distinct serializations; their hashes are not interchangeable.

The request binds **123 sources**, of which the scientific implementation report lists **120 Python sources**. The original 117 dependency files and the original seven-check file remain unchanged. The source configuration remains:

    b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6

The new driver is 67,762 bytes / SHA256
91d3112d1ce4cb132ac43353af9613940f8c5ddb5ae6cbf972053a85529914be.
The cache-development module is 11,564 bytes / SHA256
dc8335cb27794b872f39a2343f7c060b6c2dc35fbc199d2825edab007876fdbf.

Large payloads are not committed, uploaded as artifacts, or copied to a Release. This note records source, parameters, public execution identity, hashes and human conclusions.

## 3. Development execution and reuse

The positive cache-reinstallation/full_views/capture group ran once and passed. Its developer duration was **0.03975253800000189 s**.

The successful charged-miss group from the previous partial cache developer run was reused from its exact original record. Its source closure, including the production restore helper, was checked unchanged. It was not executed again. The old m10 seven groups and earlier expanded-pool ten groups were likewise reused with their original log/payload/source proofs, with zero executions.

Thus the new developer report combines one newly completed positive group with one already-paid negative group. It does not claim that two new groups ran, nor that the earlier partial report was wholly successful.

The previous failures remain recorded: the first scientific attempt stopped before capture on a cleared epigraph cache, and the subsequent positive fixture stopped on a coarse/fine tolerance shape mismatch. Neither failure is erased by this completed attempt.

## 4. Same physical historical trial and exact model rebind

Historical \(x\) and \(y\) were recovered in the same 159-coordinate space, with the same reference163 and physical163 map, g/b0, physical widths, source configuration and original two-grid definitions. The actual comparisons of eta and maximum curvature to both historical records were exactly zero on each grid; all fourteen original gate flags matched.

The initial direction bank matched **9 entries** and the original state SHA256:

    07a1f00af0acc950a7db91c698d824b3ce47324921272f45b2e2b1b1eca18f81

The two original learned row IDs were recovered: coarse **72480**, fine **144960**. Complete pools changed from \((4417,4091)\), versions \((4,7)\), to \((4418,4092)\), versions \((5,8)\). Every original row remained present.

The restored old layout contained 8,191 selected rows by 159 parameters. The rebound model at the same \(x\) contained 8,193 selected rows by 159 parameters, including both newly observed IDs.

After learning, the new helper called the original evaluate(vector(y)) and fine_decision(y) to reinstall the selected-layout cache. Actual ordinary counters remained \((2,2)\to(2,2)\): **zero additional ordinary evaluations**. The original strict full_views same-state contract passed. This restore took **0.03913401099998737 s**.

Rebinding at \(x\) also reused its saved accepted ordinary values with counter increment \((0,0)\); the accepted coarse/fine cache restore counters each increased by one. Its new selected J and complete model were rebuilt on the expanded layout. Reported rebind work was **1.884026346999974 s**.

The signatures retain their distinct domains:

| Domain | SHA256 |
|---|---|
| Replayed historical complete model | 71736cd03d0d682cd6cc66a9f78d0836e306ea965176a83057f4f887a9e7608c |
| Current-policy complete model before expansion | dc1b4ecfddc1f87839645fa22ca41df5badd72cd4c9e2f1b4c3c599024da52e9 |
| Expanded model after both factories | 23520e496b44d8d511a0bdeaa3deb64b052ea9d904d1a6d10f3222f36f0d88b9 |
| Expanded complete-observable binding | 2905effbb573fd4d0eac2fb4952caeca2ae3b782bbe5a927db013280f240edda |
| New expanded selected J | faae2d733cfe2c41c7fb501cc97ad26069544cff989a6cdf7896c1253da9ddbb |

The old whole signature is provenance, not an invented new-policy signature. The old scalar/J and physical observable fields were checked strictly; only the declared evaluation-metadata leaves changed. The new capture used the actual rounded \(d=y-x\), and the original subspace apply reconstructed the same \(y\) bitwise.

## 5. The only new SOC and its original RHS

The rebound budget was evaluated on the same actual \(d\):

| Rebound quantity | Emitted value |
|---|---:|
| Scalar and complete initial slack | 0.006368003937156641 |
| Minimum scalar slack at \(d\) | 0.006364189167921444 |
| Evaluated complete affine slack at \(d\) | 0.006364514876452287 |
| Scalar gain | 0.000003814769235196795 |
| Complete affine gain | 0.0000034890607043536193 |
| Original scalar SOC RHS, actually used | 0.006366096552539042 |
| Hypothetical complete-model RHS, not used | 0.006366259406804464 |

Both original positive-gain conditions held. The SOC used the original scalar RHS; it did not substitute the old primary LP auxiliary or the more permissive hypothetical complete-model RHS.

Exactly **one new correction LP** was charged before invoking the solver, at shared ordinal12 after the 11 historical primary calls. No old primary solve or nonlinear optimizer was executed.

The SOC had 8,845 rows and 322 variables, used the original ten-second time limit, returned HiGHS Optimal in **0.3343323189999978 s**, and passed original-unit row and bound residual checks, both reported as zero. The correction's maximum absolute independent-coordinate value was **2.296611138489122e-7**. Its only nonzero emitted coordinate was independent index72:

    -8676351571668901 / 37778931862957161709568

The subsequent physical acceptance used the actual rounded \(z\), not the LP residuals. Its canonical physical hash is:

    4d8213c9b9cad093ae40d8789b967e9cc3f78fb104baeeceb4571e2adbe7ff66

The complete rebound model's actual base-to-total-step diagnostic is available, with ratio **0.937958084659154** and predicted improvement **0.000003039327298615113**. This is a diagnostic on the expanded model and actual \(z-x\); it is not a same-layout SOC-hold witness.

## 6. Learning and controller boundary

The original \(y\) learning counts, one coarse and one fine row, remained in the trial record. The corrected \(z\) added no rows. No recursive SOC or second primary step was attempted.

The existing controller did **not** authorize holding the model radius. Its returned next body radius is **0.0000625**, from original **0.000125**, with next growth streak0. The old learning fact was not erased to manufacture a hold qualification.

The controller's detailed failed guard list is preserved in the report. In particular, its inherited same-layout linkage/sequence checks are not interchangeable with the explicitly bound expanded-layout diagnostic. The positive expanded-model ratio is not used to bypass those checks. No next primary model was run with the returned radius.

## 7. Actual cost and limits

| Observed cost or count | Value |
|---|---:|
| Read-only original-input preparation | 19.999946183999995 s |
| New run phase | 266.26478756200004 s |
| Process total | 286.264737843 s |
| Active optimization clock | 40.44415599299998 s |
| Historical \(x\) ordinary initialization | 225.55548790199998 s |
| Old-layout J and both factories | 34.518677706000005 s |
| \(y\) value recovery and original separation | 0.7900536700000202 s |
| Rebound work | 1.884026346999974 s |
| SOC solve | 0.3343323189999978 s |
| Independent final two-grid segment | 0.6445636400000012 s |
| Peak RSS | 1,072,604 KiB |
| New ordinary objective values | 6 |
| New independent final values | 2 |
| New total values | 8 |
| New primary LPs / new SOC LPs | 0 / 1 |
| Original optimizer executions | 0 |

Timing segments may be nested and are not advertised as a disjoint sum. The long ordinary initialization is explicitly outside the active clock; the report does not assign an unmeasured cause to it.

The original shared limits remained 12 LP calls, 40 physical values and 120 active seconds; the replay used its declared eight new values. The 11 inherited primary counts are historical accounting, not executions in this job.

## 8. Rules and conclusions that follow

The job performed actual public pull/read from 19:04:34.987203 to **19:04:36.553093 UTC**, after commit
66be1b6940e56fa5094c7ccd3ef4b970642fc04a. Root and topic README blobs remained
21bd547f56590b7f2dd279d0297efb289a9b2783 and
d0432faff569c8e9af7ed4809847e12880976c11, with empty diffs.

Actual private pull/read completed at **19:04:39.327329 UTC**, after
77808ef775999a50ae3b7b5b6a0943d22ed91146. Recorded rules remained unchanged and the session QUEUE was unique and ongoing. These are consumed job observations; no private contents are reproduced.

This single completed experiment shows that the fixed m10 trial's original new-row return could be followed by a correctly rebound, budgeted SOC which recovered the original physical gates and retained its eta decrease. It establishes neither a general improvement rate nor an advantage in elapsed time, and it does not automatically select this historical branch as the next global warm start. A subsequent method decision must use this completed evidence and the current mainline state explicitly.

Responsibility: tail_cost consumed the original completed log and wrote this result without new local scientific execution. Root owns publication, state selection and any subsequent Actions request.
