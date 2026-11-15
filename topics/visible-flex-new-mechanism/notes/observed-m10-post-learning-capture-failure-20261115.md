# Observed m10: exact historical recovery succeeded, then capture failed after pool expansion

Date: 2026-11-15 UTC. This is a report of the completed public attempt, not a successful SOC result. The source repair described below has not yet run.

## 1. Actual identity and outcome

The public job [132915623212](https://github.com/Rogerhu12/math-research-public/actions/runs/43748050775/job/132915623212), run **43748050775**, used source commit **1f794c7701191a3a5516fbc15b1a72035075f7b4** and ended in failure.

Its scientific report says `historical-m10-error-last-valid-point-preserved`. The exact historical accepted point \(x\), failed full trial \(y\), old selected model, the two complete model signatures, and the nine-entry norm bank were recovered. The failure occurred while capturing \(y\) after its two original new rows had been learned. No expanded-layout Jacobian, SOC LP, corrected point \(z\), or independent final check was reached.

An earlier attempt, run 43747845778 / job 132914985984, failed before development or scientific execution because the workflow sparse checkout omitted an older workflow file whose SHA was still required. The present attempt followed the workflow-only sparse correction. It is the first attempt that reached the new m10 scientific path.

| Already-produced public object | UTF-8 bytes | SHA256 |
|---|---:|---|
| Complete decoded job log | 3,021,131 | `92b9f7884560ba6368dea30c9cad34723b4db288621aca14f215702546acccf3` |
| Unique `M10_SOC_DEVELOPMENT` JSON plus LF | 13,482 | `03f49325b19eeab6394b76941c003ec90d8a79364ae8af92e8df80aa2472f1dd` |
| Unique `M10_SOC_COMPLETE` JSON plus LF | 2,451,381 | `038ae737572f8c685978e68efb3022a11430ea430218b664bafda9dd86213570` |

The large scientific payload remains runner-temporary/job-stdout evidence; this note records its identity and the human conclusions.

## 2. Development checks already paid

The ten expanded-pool interface checks from run 43744903357 were reused through their original completed report, log identity, and the exact 117 frozen dependency hashes. Their execution count in this attempt was zero.

All seven new m10 interface checks passed in **0.0037305280000055063 s**:

1. The unique m10 accepted \(x\), failed \(y\), and complete before/after pool lists can be selected without mutating the source.
2. Duplicated model numbers and an already-accepted source trial are rejected.
3. A mismatching accepted point or a missing historical SOC budget slot is rejected.
4. Missing unique peak evidence and a wrong final row ID are rejected.
5. Only the two explicitly permitted evaluation-metadata leaves may differ; e/f, de/df and original IDs remain bound.
6. The old selected and complete factory signatures can be replayed from the same scalar/J binding without misusing the old whole signature as a new-policy capture binding.
7. An altered scalar/J or complete-grid physical binding is rejected.

The seven-check source, `frame_metric_observed_m10_soc_development.py`, is 12,600 bytes with SHA256 `918702d5f6a6a25014fe2f0bc8235a60fafa38bc8c87d8c1bb8dbb3d6fdea5ca`. The driver tested by this attempt is 54,699 bytes with SHA256 `5a69407ea22297c0af8558643f45aa8a50588670697143d5ed23c2b63126685e`.

These seven checks are successful evidence even though the later scientific phase failed. The continuation should reuse this exact development record, not rerun the seven groups or the earlier ten.

## 3. Historical identities recovered exactly

The source configuration remained SHA256
`b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6`.

The current 159-coordinate state, its original reference163 and physical163 map, original width array, g/b0 definitions, and selected original row order were retained. The historical physical state hashes were:

- \(x\): `10b0a3b208ccb13919227d2b459995bffbe86dd528f0f1f136098d7b75adba1d`;
- \(y\): `627c9474c4f3d2cb9c28c248f1ae06251274e1c1d50a2097280fc93e57d4d290`.

On both grids, both the direct maximum eta and maximum absolute principal curvature differed from the recorded historical \(x\) and \(y\) values by **exactly 0 in the emitted binary64 comparisons**. All fourteen original gate flags matched on each comparison. This does not make \(y\) admissible: the historical trial was rejected and remained rejected.

The old selected layout had 8,191 rows and 159 columns, with coarse/fine versions \((4,7)\). The rebuilt signatures were:

| Signature domain | SHA256 |
|---|---|
| Current scalar/J model | `274bcb6ee9b9e6453e0afff1fc04dae1a83b980ccd524c4835bae9c65b79287f` |
| Replayed historical selected model | `6ef45e56f4292f5c1d8dffeff202ee84a96a40b52258beafce8eefb8000f6852` |
| Replayed historical complete model | `71736cd03d0d682cd6cc66a9f78d0836e306ea965176a83057f4f887a9e7608c` |
| Current complete model after both factories | `dc1b4ecfddc1f87839645fa22ca41df5badd72cd4c9e2f1b4c3c599024da52e9` |

The two deliberate metadata differences were the coarse/fine `external_current_cache_binding.*.evaluation_sha256` leaves. The original physical, array, ID, coordinate, scalar/J, and e/f/de/df comparisons were not waived. The historical signature remained provenance; capture was to use the new complete signature.

The initial bank was recovered exactly: **9 entries**, SHA256
`07a1f00af0acc950a7db91c698d824b3ce47324921272f45b2e2b1b1eca18f81`.
This gate ran before any new LP.

At \(y\), the actual separators recovered the original unique new IDs **72480** on the coarse grid and **144960** on the fine grid. Complete pools changed from sizes \((4417,4091)\), versions \((4,7)\), to sizes \((4418,4092)\), versions \((5,8)\). The original learning counts and rejection fact were retained.

## 4. The concrete cache failure

The exception was:

```text
TypeError: 'NoneType' object is not subscriptable
run_case -> core.capture_failed_trial -> objective.full_views(y)
frame_metric_entry_tail154.py:
    self.epigraph_cache['vector'][:-1]
```

The new driver evaluated \(y\), learned its newly violated rows, and immediately asked the frozen capture helper for complete views. The original pool setter clears the selected epigraph cache. The complete ordinary coarse geometry cache and fine geometry cache still describe \(y\), but `full_views` intentionally also requires the selected epigraph cache for that same state. The missing cache reinstallation is therefore a new orchestration defect.

This error is not evidence that the physical state changed, that a gate was relaxed, or that SOC failed mathematically. Capture itself had not finished, and the rebound registry was empty.

The narrow repair is to invoke the original `evaluate(vector(y))` and `fine_decision(y)` once after learning and before capture, thereby rebuilding the current-layout cache. It must record the actual ordinary evaluation counters before and after and require zero additional ordinary geometry calls. It must also preserve the same \(y\), pool IDs, pool versions and source trial. A cache miss is to be reported and rejected under the existing eight-value plan; it must not be silently labelled zero or paid by an enlarged budget.

The frozen 117 dependencies, SOC mathematics, full-grid gates, original scalar RHS, model factory order, norm bank, configuration and physical domain require no change. A new small synthetic check will target only this cache-reinstallation/capture interface and its charged-miss rejection.

## 5. Exact execution boundary and costs

| Observed quantity | Value |
|---|---:|
| Original-input preparation | 17.450677684 s |
| New run phase elapsed | 262.63810537300003 s |
| Process total | 280.088787387 s |
| Active optimization clock | 35.49693738799999 s |
| \(x\) ordinary initialization segment | 226.895550283 s |
| Old-layout J and two-factory recovery segment | 34.754261670000005 s |
| Peak RSS | 835,748 KiB |
| New ordinary objective geometry values | 4 |
| New independent final values | 0 |
| New primary LP calls | 0 |
| New SOC LP calls | 0 |
| Nonlinear optimizer calls | 0 |
| Rebound contexts completed | 0 |

The reported 11 primary LP calls are inherited historical budget accounting, not executions in this job. The original shared limits remained 12 total LP calls, 40 total values and 120 active seconds; the new replay's predeclared ordinary/final bound remained eight. This attempt consumed four new ordinary values, two at \(x\) and two at \(y\).

The long ordinary initialization was outside the new active optimization clock, as the report explicitly separates it. No unmeasured portion is assigned a causal explanation here.

## 6. What remains unpaid

The attempt has paid the new extraction/signature interfaces and exact historical recovery. It has not yet tested expanded-layout \(J(x)\), rebound scalar/complete gain eligibility, one SOC solve, any corrected \(z\), learning after \(z\), hold eligibility, or independent final two-grid acceptance.

The requested continuation is still the first completed application of expanded SOC to this single already-observed failed m10 trial. No old primary solve, optimizer, extra model, repeated backtracking or budget extension is authorized by this failure.

Public/private rule synchronization for this attempt was reported by the root agent as: public pull/read at 18:40:41 UTC, `1689b65d76f69a6892038d73aef669b8159a85af`; private pull/read at 18:40:43 UTC, `ba3378af0eeefc95fbb7d3701ea54824ae2d5ad2`. Both rule sets were unchanged and the session QUEUE remained ongoing. Those are actual root-consumed synchronization observations, not substitutes for a repository pull by this report author.

Responsibility: tail_cost consumed the already-produced public records and diagnosed the new driver boundary; root owns publication and any next public execution.
