# Actual request 84: a quarter step with twenty-five queries, with several nonlinear limits remaining

Author: amplitude agent; original public Actions producer and publication controlled by the root agent. Date: 2026-11-15 UTC.

## Result and immediate decision

Request 84 saved one improved warm field after accepting the third actual trial, $\alpha=1/4$. With this model's original row weights held fixed, the recorded merit decreased from `43.56581593085674` to `43.48929991208616`. The producer recorded a decrease of `0.07651601877058312`, a predicted unregularized decrease of `0.07747277770595443`, and an actual/predicted ratio of `0.9876503855457118`. All original node, collocation-midpoint, uniform-angle material-map and both RMS-query domain checks passed at the accepted state. The separately rerun complete affine physical-angle boundary FD passed with maximum fourth-order error `9.901031794093097e-10` against the unchanged `5e-5` threshold.

This is optimization progress in an **unaccepted warm field**. The saved status and warm both retain `success=false` and `new_coupled_finite_acceptance=false`. The boundary FD uses the actual completed zero-height T112 Jacobian as an explicitly affine map at the new warm; it does not solve the nonlinear native tail at the new height. There is no accepted full BVP, closed Cartesian surface, same-metric refinement parent, or whole-image held-amplitude conclusion in this run.

The nearest rejected trial, $\alpha=1/2$, failed at **three** original collocation midpoints, `479`, `486`, and `487`. In addition, the separately saved selected-query readout at this same trial found a negative domain margin at the **already modeled** left-RMS query `465`. The original full RMS stage and actual merit were not evaluated for this trial because the original midpoint RHS was nonfinite. Thus this record does not identify one omitted midpoint as the sole remaining cause. The minimal next proposal is one fresh model from the actual new request-84 pair using the same twenty-five queries and all unchanged parameters and gates. Adding a twenty-sixth query or changing damping is not justified solely by this nearest rejection.

All numbers below are copied from the saved Actions reports. The local work for this note comprised JSON reading, file hashes, transparent gzip decoding, source-byte comparison and exact report/producer relationships. No RHS, Jacobian, matrix action, norm, optimization, domain value, native solve or other scientific quantity was recomputed locally. The companion [literal readout](2026-11-15-actual84-original-readout.json) retains the complete three-trial scalar record, including all twenty-five selected grids per trial. The [primary identity receipt](2026-11-15-actual84-primary-identity-readback.json) records the actual file, source and parent checks.

## Actual run and input identity

| Item | Actual identity |
|---|---|
| Public run | [43666177645](https://github.com/Rogerhu12/math-research-public/actions/runs/43666177645) |
| Source commit | `39799fc1a52b91629b3deed3b4fb45e29ae7b6e7` |
| Scientific job | `132665958586`, `Follow-up condensedqp`, success |
| Run creation / final update | `2026-11-15T02:06:19Z` / `2026-11-15T02:17:03Z` |
| Complete scientific artifact | `14142830941`, `visible-followup-condensedqp-43666177645-1` |
| Artifact size / digest | `670263923` bytes / `fb8d56c1ec3df6f9c0b622e97c861113117a43e99679b6b569edd4146fe526b4` |
| Immediate parent warm, actual 79 | `565e2487317ffbc85560dd01efa2cfb4e479447d51a17216deb4ef61f55b4504` |
| Immediate parent original decoded status | `e790e998ed6eebdc084546131e206dd4e5d723aebf7f92830b3153f82a25a8c0` |
| Warm producer schema | `exact-constraint-twenty-five-query-condensed-complete-H-warm-v1` |

The original publication is under `notes/public-actions-43666177645-1-condensedqp/`. Root fetched the five primary published files once, preserving their exact bytes and transparent gzip identities. This primary readback did **not** download the complete 670 MB scientific ZIP or claim a complete array audit. The pinned completed-reader request is an independent readback of existing artifacts, not a scientific rerun or an acceptance condition.

Request 84 adds only left-RMS `465` to the prior twenty-four-query design. The actual typed list is:

- Seventeen left-RMS queries: `465, 466, 467, 468, 469, 470, 471, 472, 473, 475, 477, 479, 480, 481, 482, 484, 485`, all at the original fraction `0.17267316464601146`.
- Eight original collocation-midpoint queries: `473, 475, 477, 480, 481, 482, 484, 485`, all using the actual `state.middle` and `problem.mid` definitions.

Each query contributes its complete original 2048-point physical-angle grid: `51200` inequality rows. The actual endpoint and declared local support are the same complete physical nodes `465…486` plus all three global controls, `7439` local coordinates; the zero-layout list is empty. The fixed-support C candidate still uses nodes `471…482` plus the three controls, `4059` coordinates. Its affine outside offset retains the actual contributions of nodes `465…470` and `483…486`. The complete-H candidate retains the conditional response of all exterior physical variables and the free core. No exterior variable is silently fixed because it is outside this local inequality support.

The unchanged algorithmic settings include damping `270`, `512` working rows, `200` dual sweeps, the original LSMR/Hildreth settings, the bounded local/total time budgets, and the original seventeen-trial backtracking limit. Only three trials were needed here. These are optimization settings; the scalar metric design, original full equations, node budget, native requirements and final scientific tolerances are not changed by this warm optimization.

## All actual trials and their evaluation stages

| Actual $\alpha$ | Original node failures | Original midpoint failures | Selected-query nonlinear failures | Full original RMS stage | Actual fixed-weight merit | Accepted |
|---:|---:|---|---|---|---:|---|
| `1` | `0` | `480, 482, 485, 486, 487` | Left `465…472`, left `484`, mid `480, 482, 485` | Not reached | Not evaluated | No |
| `1/2` | `0` | `479, 486, 487` | Left `465` | Not reached | Not evaluated | No |
| `1/4` | `0` | None | None of the 25 grids | Both 698-point families passed | `43.48929991208616` | Yes |

The selected-query rows are read-only evaluations of their original nonlinear angle-domain expression; they are not a substitute for the original all-query domain stage. In particular, left `465` at $\alpha=1/2$ was observed as invalid even though the original RMS family was not reached. No claim is made that it was the only invalid RMS station in that rejected trial.

### Nearest rejection, $\alpha=1/2$

All three bad original midpoint inputs were finite, but their original RHS outputs were nonfinite. Their saved angle readouts are:

| Kind / interval | Actual station | Minimum $\beta^2$ | Angle index / $\phi$ | Negative angles |
|---|---:|---:|---|---:|
| Original midpoint `479` | `1.217222883746318` | `-0.02975376921808004` | `131` / `0.401902966426038` | `4` |
| Original midpoint `486` | `1.2516837037373927` | `-0.011979899118687687` | `1005` / `3.083301383650139` | `8` |
| Original midpoint `487` | `1.2566681552371528` | `-0.04159807851745456` | `982` / `3.0127382674073995` | `4` |
| Selected left-RMS `465`, already modeled | `1.1603320320063233` | `-0.953396699525703` | `65` / `0.19941750242513334` | `12` |

The other twenty-four selected grids at this trial had positive saved minima. The original uniform-physical-angle material-map guard remained valid with sampled minimum `0.16604058243274977`; the boundary was finite, the left residual was zero, and all core/control rows remained constant. These facts do not override the failed original midpoint-domain checks.

The complete `51200`-row **linear** reserve-slack report at this same $\alpha=1/2$ had no negative rows and minimum `0.0002916796430858515`. The negative actual left-465 margin therefore cannot be described as a missing linear row: that row belongs to the model, while the original nonlinear query differs from its directional linearization at this finite step. This is direct evidence for retaining the original nonlinear backtracking and for constructing a fresh model at the newly accepted field.

The current record has several unmodeled midpoint failures as well, so it does not prove that the existing twenty-five queries will suffice indefinitely. It also does not justify erasing the already modeled failure and adding only midpoint `487` on the assumption that this alone will allow the half step.

### The farther unit trial

At $\alpha=1$, the original midpoint minima were respectively:

| Midpoint interval | Minimum $\beta^2$ | Negative angles |
|---:|---:|---:|
| `480` | `-0.07953309058522207` | `12` |
| `482` | `-0.014637969814921714` | `4` |
| `485` | `-0.024947339878796493` | `4` |
| `486` | `-0.001816409364487681` | `4` |
| `487` | `-0.01922887163545406` | `8` |

The selected left-grid minima for `465…472` were `-0.4428162823516917`, `-0.5123814296075935`, `-0.4889204281146491`, `-0.340562607388774`, `-0.3148221820733008`, `-0.10781536735971975`, `-0.14833093122886631`, and `-0.12011024822939564`; selected left `484` had `-0.0746256690899112`. The selected midpoint rows `480`, `482`, and `485` reproduce the corresponding original midpoint values above. Full original RMS and actual merit were again not evaluated. The saved linear reserve slack nevertheless had `51200` finite entries, zero negative entries and minimum `1.1102230246251565e-16`. Actual nonlinear domain behavior is not monotone in these sampled step lengths; no monotonicity assertion or unmeasured merit value is inserted.

### Accepted quarter step

At $\alpha=1/4$, all original nodes and midpoints were finite and both original RMS families passed:

| Original RMS fraction | Original query points | Invalid points |
|---:|---:|---:|
| `0.17267316464601146` | `698` | `0` |
| `0.8273268353539885` | `698` | `0` |

The accepted full domain report retained `left_residual_max=0`, `constant_collocation_max=0`, constant core/control states and the original valid uniform-angle guard. All twenty-five selected nonlinear grids were positive. For context, saved selected left `482` had minimum `0.0010161144662940158` at angle index `0`; selected left `480` had minimum `0.003068594385023382` at index `1013`. The saved linear reserve-slack minimum was `0.0004375194646287217`, with no negative rows.

The local merit comparison is strictly within this request's freshly fixed weights. The preceding request-79 final merit and request-84 initial merit cannot be subtracted to measure inter-model progress: each fresh model computes and then holds its own original weights. The actual byte-preserved parent and current warm establish field continuity; they do not make two independently fixed merit functions identical.

## Actual finite model, candidate selection and posterior scope

The reported original-A and B implementation checks passed. The complete-coordinate adjoint checks, original augmented-action comparisons and the independent original nonlinear collocation complex check are retained in the literal readout. The latter check has its exact stated scope: **free inlet core and global controls only, with interior physical coordinates zero**. It is not a test of every interior physical direction.

The B check reports model identity `6ac00e85c7b163823d38186d0fbb4bc4e6cb28c4e757c97de294de78b4c8a77c`, maximum normalized adjoint error `1.6688923864529174e-17`, local/full action difference `0`, and maximum original complex-chain relative error `1.7103007779859776e-12`. These are original Actions results, not local reruns or independently certified enclosures.

The bounded local QP reached `512` working rows and stopped with `maximum-working-row-budget`. Its final saved stage `511` used all `200` dual sweeps. That stage's unrepaired local slack minimum was `-1.3672396548258803e-13`, with `504` negative floating entries; its local stationarity norm was `1.8035631842905684e-10`. The local repair factor was `0.9999999999807971`, after which the reported slack was nonnegative. These stored quantities matter: the budget stop alone does not establish that a large unresolved linear-model violation or an inadequate inverse solve caused the later nonlinear-domain rejection.

The original fixed-support C direction and the R270 direction were evaluated with the same current full model. The recorded objectives were:

| Candidate | Original full damped-model objective |
|---|---:|
| Retained C candidate | `43.56566044162508` |
| Selected R270 complete-H candidate | `43.39875157374576` |

The C candidate's projected-direction global radial factor was `0.001252705669534556`. For the recovered complete-H candidate, the global radial factor was `0.9999999998641956`; its preceding actual full slack minimum was `-5.601630270746227e-13`. The original feasible-segment selector chose the complete-H endpoint with segment parameter `1`, and its final composed repair factor was `1`. This actual chosen direction is not the heavily shortened raw-ray backup. Its recorded full directional derivative was `-0.32132161271424986`, its full damped-model decrease was `0.1670643571109729`, and its coefficient-direction maximum was `0.00013219113513087243`.

After all recovery, repair and selection, the original full A/AT/B/BT readback reported `51200` finite nonnegative slack entries, minimum `1.1102230246251565e-16`, stationarity norm `2.9829357063888715e-5`, nonnegative multipliers and complementarity sum `1.7740685018364765e-12`. The stored R267 cross-point gap was `1.7621459846850485e-12` and the stored distance bound was `6.952999145023744e-9`. They are ordinary floating posterior diagnostics, explicitly **not validated enclosures** or a new original-BVP gate. No claim of exact full-QP optimality follows.

The report explicitly sets `global_selector_changed_conditional_recovery=true`; after that final global change it does not claim the exterior variables remain at an exact conditional optimum. The actual full-vector checks and original nonlinear trials remain decisive.

## Condensation and original-H recovery

The stored R270 condensation completed `212` reverse fronts, retained `7439` local coordinates, performed `512` local-H solves and one complete recovery. The original affine construction kept the full original gradient rather than discarding it using an approximate center. Its original linear-term error was `1.3399078427607655e-10` in L2; the saved original gradient L2 was `219637.99645704497`.

The one original-H recovery reported:

| Original report field | Saved value |
|---|---:|
| Local recovery mismatch L2 | `6.801276121003694e-17` |
| Local recovery mismatch Linf | `2.759548638859785e-17` |
| Original-H residual L2 | `2.261480713585885e-10` |
| Relative original-H residual L2 | `1.030943538644219e-15` |
| Exterior gradient L2 | `2.2614600706370688e-10` |
| Supplied/frozen same-vector A difference | `0` |
| Supplied/frozen same-vector AT difference | `0` |

The condensation model identity is `f92fbb366e2b0bf6f2e8b4e28e51136f0e8c847695e6d5f47b5c70f18fd7c0ab`. The field `original_factor_input_identity_sha256=74234e98…` is the SHA of a JSON `null` identity, as the original recovery report shows; it is not presented as a unique physical-model identity. The original factor's separate input-array and factor-array identities remain in the report. The complete chain-QR factor arrays were not exported as raw files, and this primary note does not claim to audit their bytes. The completed artifact reader can audit actually exported B, local-root, candidate and observer bytes within its stated scope.

The warm producer elapsed time was `565.243268793` seconds. The factor/condensation/local-QP/recovery helper reported `272.56239218100006` seconds, including local-QP `231.78261019499996` seconds; condensation reported maximum RSS `4828992` KiB. No extra computation was performed to produce this note.

## The physical collocation maximum and new FD

The read-only collocation observer located the complete physical maximum at the same actual original row at the base and accepted states:

| Field | Base / accepted original value |
|---|---|
| Interval / physical component | `461`, radial mode `1`, component index `1`, angular frequency `2` |
| Complete residual row | `155819` |
| Interval endpoints | `1.139533544992796`, `1.1445179964925558` |
| Existing midpoint station | `1.1420257707426757` |
| Signed physical residual, base | `-0.007108516833554497` |
| Signed physical residual, accepted | `-0.007108203814352419` |
| Original fixed weight at this row | `199.03226329104072` |
| Original weight-array SHA | `724bcff672575ecadb0c1b2dded79fc590188ff92dceb2156d576ee9080c23b9` |

The observer copied the original returned arrays and original model weight, made no extra RHS/Jacobian/model call, and preserved the original finite flags and residual/collocation bytes. Row `155819` lies outside the local B support; it still belongs to the complete A and full-H response and is not a zero-weight or omitted equation. The stored maximum improves only modestly despite the recorded total merit decrease. Neither this observation nor the small floating model posterior establishes that damping is its unique cause or guarantees rapid reduction of that maximum.

The accepted complete-boundary maximum was `1.3149281045422406e-8`, compared with the original base `1.7532371533528647e-8`. This warm boundary uses the explicitly affine tail map, not a newly solved true nonlinear current-height tail.

The actual new-warm FD reran the original complete physical-angle boundary directions and Richardson levels. It reported fourth-order maximum `9.901031794093097e-10`, second-order maximum `9.883430085086724e-6`, contracting second-order errors and `implementation_check_passed=true`. It retained the true zero-anchor SHA `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` and config SHA `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`. It explicitly records `current_H_equals_affine_anchor=false`, `nonlinear_native_at_current_H_solved=false`, `full_BVP_solved=false`, and no relabeling of an old FD pass.

## Original bytes, producer chain and reusable new pair

The five original reports and their transparently decoded identities are:

| Original file | Bytes | SHA-256 |
|---|---:|---|
| `model-000.json` | `613814` | `53b62f1ec963c917f4587ba655fab170568360a8eb719eb06e2303d36b298ae6` |
| `driver-status.json.gz` | `305169` | `bbd61744b2457b40654573460fbd25433f406f3a41d79bbae4fd3f56e5a65d38` |
| Exact decoded `driver-status.json` | `2620898` | `8ad4ae64ccf4a84106a22db9f60c3abedfe4efae67d467b59aa6c06480b9bbde` |
| `condensed-QP-summary.json` | `108904` | `3e7a211063f97f5f89db77324eef86b53174e19dd79f0f5e14e475cc3fe474f2` |
| `response-check.json.gz` | `245761` | `f7cdab912797cc296cb066a6eb0ffc0aeec5dd111215312c7f7bbf4e5bf2f878` |
| Exact decoded `response-check.json` | `2020594` | `b147015d29b347185d77172b443f9b738aa089b9d7abbc6db5a8a0788c3cb7e5` |
| `warm-001.json.gz` | `4880394` | `fead4e7b8c1c78b62c8adef0d122a09ea12e7e3a94b0586ba2e59a63c3b429af` |

The primary receipt passed all seventeen saved identity relationships: parent warm/status hashes; parent status to parent producer; parent status to the resume SHA; complete preservation of the parent producer subtree; exact new warm/status/FD binding; status iteration to original model; unchanged original mesh; transparent status/FD gzip decoding; current schema agreement; explicit unaccepted flags; accepted original trial identity; and the complete root fetch-manifest file identities. It also matched all `64` distinct recorded producer/FD source digests to local source bytes, with no unresolved source.

The four new twenty-five-query sources remain the frozen domain `55fe72b1bad9cf3ee26b1d29a1a6cefb7f0f62f2570d7703bb8f3dfcd01b2260`, mathematical warm `5dbd5948f815a1fcf4eaf2a08f7d130407ce52c96b25240738d26c6476b48b0c`, response `8d55ce7f29520318db39de5dcdb0790cdce43452dc29085ec26cbfe042dfa75d` and observer `be6815071387c34fb25b4f064508af2ab65691bba4ff512d1fa999236a1f4d55`.

For a subsequent same-schema single-model call, the exact input pair is the new compressed warm SHA `fead4e7b8c1c78b62c8adef0d122a09ea12e7e3a94b0586ba2e59a63c3b429af` and original decoded status SHA `8ad4ae64ccf4a84106a22db9f60c3abedfe4efae67d467b59aa6c06480b9bbde`. If the status is transported as the published gzip, its digest is also pinned above and decompression must recover the exact original status bytes. No reserialization is used to invent a new parent identity.

The proposed next request keeps these twenty-five queries and all frozen sources, damping, budgets and original gates, and rebuilds one actual model from this pair. It is a new computation to be reported separately; this note does not claim that it has run or will accept a larger step. The complete byte reader is an evidence-preservation follow-up, not an additional mathematical approval gate.
