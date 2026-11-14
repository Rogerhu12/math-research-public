# Actual request49: fourteen-query warm, with the next limit at left-RMS469

Status: numerical evidence. 2026-11-14, /root/amplitude and /root, GPT-6 Astra Pro, AI-assisted.

## 1. Actual result and its scope

The independent fourteen-query run completed one real warm step and its original complete physical-angle boundary derivative check. It accepted `alpha=0.0625` after the unchanged nonlinear domain and fixed-weight merit checks. The fixed-weight merit in this model decreased from `44.250102036498696` to `44.20038969249102`, a recorded decrease of `0.04971234400767344`. The saved field remains explicitly **unaccepted as a full BVP**.

The nearest rejected trial was `alpha=0.125`. Every node, collocation midpoint, and all fourteen modeled angular query grids were valid at that trial; the only remaining original domain failure was **left-RMS interval469**. Its actual minimum beta squared was `-0.2951240357733671` at `phi=0`. This is a concrete reason to add that original query to the next algorithmic model. It is not evidence that the original domain check should be changed.

The new source, parent field, and model differ from earlier runs. In particular, the merit weights are fixed anew in this model; the printed merit must not be subtracted from another model's printed merit as if the weights were unchanged. The successful step is also not a controlled same-base comparison with request48.

All numerical evaluations reported here were performed by this public repository's GitHub Actions. The subsequent local work only read saved scalars and checked source, archive, and raw array byte identities. It did not rerun an ODE, Jacobian, matrix action, norm, optimizer, finite difference, or native tail.

## 2. Run, sources, and exact parent

| Item | Actual identity |
| --- | --- |
| Run | [43631235905](https://github.com/Rogerhu12/math-research-public/actions/runs/43631235905) |
| Scientific job | `132558124307` |
| Source commit | `d5c99bef58700db0da1a3de2faba3e94d60b1dc1` |
| Artifact | `14128436509`, `visible-followup-condensedqp-43631235905-1` |
| ZIP bytes | `364751872` |
| ZIP SHA256 | `c6fb1a399527a741f9064fc50b3aa0090182f8939fe21b23fcad223db9af5b14` |
| Warm step | `19:17:48Z` to `19:23:55Z`, success |
| Original boundary FD | `19:23:55Z` to `19:24:14Z`, success |
| Artifact upload | completed `19:24:24Z`, success |
| Ordinary publication | completed `19:24:30Z`, success |
| Job completion | `19:24:33Z`, success |

The artifact was downloaded once by the root process and its complete ZIP SHA was checked before this readback. The public output is [public-actions-43631235905-1-condensedqp](public-actions-43631235905-1-condensedqp/), with the scientific output in `fourteen-condensed-warm/` and the FD output in `physical-response/`.

The three new source files were frozen before dispatch:

| Source | SHA256 |
| --- | --- |
| `geometry_20261114_fourteen_query_domain_operator.py` | `049ab10d130c94d5b1849a2af3b0e3f4848819bb9b7af68230488c25ba778464` |
| `geometry_20261114_fourteen_query_condensed_warm.py` | `331b59edadfa1fb7d5f8c64e6f0119c63a62f5e2a3df999549ef7effd932aac8` |
| `geometry_20261114_fourteen_query_condensed_response.py` | `a84a693172af678146eb36cd43b965b8206bf3d048dac32047fb7acc4c7e82a1` |

The complete original QR, R270 condensation, local QP, fixed-support C comparison, trial, and FD sources were retained. The interface is [fourteen-query-condensed-warm-interface](2026-11-14-fourteen-query-condensed-warm-interface.md).

The actual parent is request48, not the old prepared699 seed:

- Parent warm SHA: `df6543c9b88c21bd9ea3c046f05a7c292b7d977d09c6ef431e6771560fe14689`.
- Parent original status SHA: `00c9e73f260d0fa239a17c3973bcbd113d813c079c04451335244e923e85be9e`.
- The compressed published status was decompressed to its original bytes, without JSON reserialization, and checked against that original SHA.
- The entire original parent `optimization_warm` subtree is preserved in this run's `resume_producer`.

The parent mesh, states, and saved RHS also agree byte-for-byte with this model's actual B base. The canonical array identities are respectively `7cef3604718c2d21dc4f0c866d29a08dc05b1596b49e4ea81a415cf9a9dc68bb`, `ffa7c2cb076eb6df05c53808e7552c06717a0bac077615768b0a1042867fc65e`, and `d6abaa4d6393c05c1a878250209b9ebead246bd2f68b30fb6fa7cedbb266bb84`.

## 3. The complete fourteen-query model actually used

The ten left-RMS queries were intervals `470,471,472,473,475,477,479,480,481,482`, each at the original fraction `0.17267316464601146`. The four collocation-midpoint queries were intervals `473,475,477,482`, each taken directly from the original `state.middle` and `problem.mid`. All queries used the complete original 2048-point physical-angle grid.

Thus B had `28672` rows, all `236036` full coordinates, and a complete local support of `4735` coordinates: physical nodes 470 through 483 and all three global scalar controls. The local C correction retained its older support of nodes 471 through 482 and the controls, `4059` coordinates. The full B action of the exterior raw direction, including nodes 470 and 483, was retained in its affine offset. The complete-H alternative conditionally optimized the exterior variables; it did not freeze them to the C correction support.

The actual B model SHA was:

`15711b59c57f174c6583bd070c6050719b2269abf0240b8c4cefe4e54dd0c2d4`.

The unique original complete linearization made 88 Jacobian calls. B captured only the original calls 59 and 61, containing the required 14 endpoint nodes and 14 stored variants. Node 480 occurred in both source chunks; the identical captured values were retained as one actual variant. No second complete Jacobian was constructed. The compiled row storage was `155746304` bytes.

The original Actions implementation checks reported:

| Saved check | Value |
| --- | ---: |
| Maximum normwise adjoint error | `6.003120945327195e-18` |
| Maximum local/full action difference | `0.0` |
| Actual original complex-chain relative error | `1.3037791441624681e-12` |
| Independent original physical collocation complex check | `8.673617379884035e-19` |

The last check has the explicitly saved scope **only free inlet core and global controls, with interior physical coordinates zero**. It must not be described as an independent check of every interior physical direction. The complete B directional check used the actual saved LSMR direction. None of these diagnostics replaced any scientific acceptance condition.

## 4. Raw LSMR and the retained C candidate

The raw LSMR solve used the original `lambda=270`, at most 200 iterations, and the original column and row weights. It stopped at iteration 200 with `istop=7`. Its saved original regularized gradient norm was `1073.9623887754958`, whereas its actual preconditioned normal norm was `0.00021665682433341188`. These are different norms; they must not be conflated.

The raw direction's saved slope was `-1.2641934297737207` and damped model decrease was `0.6321064922209899`. The actual selected direction below came from the condensed complete-H calculation, so the eventual domain failure is not identified with raw LSMR truncation.

The unchanged fixed-support C comparison ran 200 sweeps and stopped at its sweep budget. It retained the complete affine outside offset, with raw/candidate reconstruction differences `4.263256414560601e-14` and `4.984901380566953e-14`. There were no computed-zero-row infeasibility cases. Outside raw coordinates were preserved before the later full-vector radial operations; the final direction is not claimed to preserve them.

The C projected candidate required radial factor `0.0023298750291752355`; the feasible raw ray required `0.00010079540054837413`. Its final selected objective was `44.24831412845383`, with model decrease `0.0017879080448843987`. This candidate was retained for the actual same-model comparison rather than discarded because its direction was smaller.

## 5. R270 condensation, QP budget, and complete recovery

The actual condensation model was:

`e530aa4596789a0fcc3e426733c3c41a5d7cdd3caabb63c4eeae54afc5b93192`.

The calculation retained physical nodes 470 through 483, conditionally eliminated 469 left physical nodes and 215 right physical nodes, retained the complete pure-global contributions, eliminated 109 free core coordinates, and kept all three scalar controls. Its local dimension was 4735. The original linear term was retained through the affine square-root construction of [R270](../results/R270-exact-local-support-damped-QP-condensation.md); a computed approximate center was not substituted for that linear term.

There was one complete factorization and one final complete-H recovery. The local QP made 256 inverse calls and 775 local H actions. The actual condensation took `10.253653303000021` seconds, the QP `52.23381275300005` seconds, and the complete helper including factorization, condensation, QP, and recovery `86.01499305300001` seconds. The maximum saved RSS was `3853100` KiB. These operations did not reconstruct the full Jacobian or call the native tail.

The working-row budget 256 was reached. Stage 255 added row 23649, query 11: midpoint475, angle index 1121. Its final dual sweep count was200. The unrepaired candidate still had 484 negative original slacks, minimum `-1.0636807709019092e-5`; the maximum relative violation was `4.4154135484661384e-5`, at row 9161, left-RMS475 angle 969. Its saved local stationarity norm before repair was `5.810713972078567e-12`.

The local radial factor `0.9999558478140025` removed those violations. The local feasible-segment parameter was1. After the full conditional recovery, the original full B readback required another factor `0.9999999999999242`; the final global segment parameter was again1. All 28672 final linear slacks were finite and nonnegative, with saved minimum `1.3322676295501878e-15`. These are rounded finite-model readouts, not a continuous-angle or interval certificate.

The original complete-H recovery readbacks were:

| Readback | Actual saved value |
| --- | ---: |
| Local mismatch L2 | `2.451351898370048e-17` |
| Local mismatch Linf | `7.90451146377713e-18` |
| Original H residual L2 | `7.049098712506211e-10` |
| Original H relative residual L2 | `7.358760985301333e-16` |
| Exterior gradient L2 | `7.049094269747331e-10` |
| Same-vector supplied/reference A difference | `0.0` |
| Same-vector supplied/reference AT difference | `0.0` |

The actual recovered local coordinates were not overwritten to make them equal to the requested values. The factor's `input_identity` is null; its hash `74234e98...` is therefore not a unique model identity. The report separately preserves all nine original input-array identities, the four factor-array identities, and three factor byte rechecks. The full factor arrays have `file=null`: they were held in memory and were not exported as independently readable raw factor files.

The same-model selector chose **R270-condensed-complete-H**:

| Selected full-model readback | Value |
| --- | ---: |
| Objective | `43.8430803236376` |
| Actual derivative | `-0.8053830612089119` |
| Damped model decrease | `0.40702171286111155` |
| Full stationarity norm after repairs | `0.17275813912882879` |
| Complementarity sum | `3.8674191236822516e-7` |
| Best R267 floating lower-bound diagnostic | `43.843079732194916` |
| Final floating gap diagnostic | `5.914426850495147e-7` |
| Floating distance-bound diagnostic | `4.028167916565426e-6` |

The posterior numbers use the original full A/AT/B/BT readbacks. They are not validated enclosures, a proof of full QP optimality, or a BVP acceptance gate. The repairs change stationarity, so the small pre-repair local stationarity norm must not be substituted for the final full-model norm.

## 6. Every actual nonlinear trial and the limiting query

The original seventeen-trial allowance was retained. This run executed the first five candidates and stopped after the successful fifth candidate. The table reports the actual original checks; a dash means the later RMS check was not reached after the earlier original domain failure.

| Alpha | Invalid original midpoints | Original left-RMS failures | Original right-RMS failures | Actual fixed-weight merit decrease | Result |
| ---: | --- | --- | --- | ---: | --- |
| `1` | `473,475,477,481,482,483` | — | — | — | original midpoint domain rejection |
| `1/2` | `473,475,477,481` | — | — | — | original midpoint domain rejection |
| `1/4` | none | `469` | none | `0.19187870836272936` | original RMS domain rejection |
| `1/8` | none | `469` | none | `0.09819846773537222` | original RMS domain rejection |
| `1/16` | none | none | none | `0.04971234400767344` | accepted warm step |

All node checks, the original 4096-point uniform-phi rho guard, and boundary finiteness passed at all five trials. At `1/4`, `1/8`, and `1/16`, every one of the fourteen modeled 2048-angle query grids was positive. The two rejected finite-field trials actually decreased merit: their actual/predicted decrease ratios were `1.0059370141943549` and `1.0017900401512758`. Thus they were rejected by the original RMS domain condition, not by an incorrect Armijo slope or failure to reduce the actual merit.

The limiting original left-RMS469 station was `s=1.180269838005363`, inside the original interval `[1.179409156990875, 1.1843936084906348]`. It used the original left-RMS fraction and scalar values `a=1.1924556756329512`, `ap=-0.09917619651381597`, `app=-2.4876747200511526`.

| Rejected trial | Actual beta squared minimum at left-RMS469 | Actual phi of saved minimum |
| ---: | ---: | ---: |
| `1/4` | `-0.2974443548830277` | `3.043417883165112` |
| `1/8` | `-0.2951240357733671` | `0.0` |

These are saved whole-field query evaluations, not values extrapolated from a linear B row. The larger rejected steps also exhibit genuine nonlinear midpoint failures despite the complete finite linear inequalities. This continues to require the original full nonlinear backtracking; one-step linear feasibility does not imply nonlinear feasibility at alpha1.

At the accepted `1/16` step, the actual merit was `44.20038969249102`, predicted decrease `0.049673971319009746`, and actual/predicted ratio `1.000772490856776`. Both original 698-query RMS levels had zero failures. The saved physical collocation maximum changed from `0.007110250799470694` to `0.0071101678278726824`; the boundary maximum was `7.177739211877821e-8`. The inlet and constant-row maxima remained0, and the rho minimum was `0.16604058243274977`. The report does not save the location of the physical collocation maximum, so no location is inferred here.

## 7. New warm and the genuinely recomputed FD

| Saved artifact | SHA256 |
| --- | --- |
| `fourteen-condensed-warm/warm-001.json.gz` | `c0d9c6d59e16ef1482f8ee60f9681d8db089b21d68e249adf1830df03be6612b` |
| Original `fourteen-condensed-warm/driver-status.json` | `e22fd03b8c24adbd0eeeaf0b084d18944d17e4cd1f4115075cb63d9e9a41aad7` |
| `physical-response/response-check.json` | `43245db767010a7f36ad266cd5993395e781ec22e2343946f9504b63aadc78b3` |

The status records one accepted warm step, elapsed `365.482310735` seconds, `optimization_progress=true`, `success=false`, and `new_coupled_finite_acceptance=false`.

The boundary FD was actually recomputed at that saved warm, with its new SHA and complete producer. Its fourth-order Richardson error was `7.070190461766486e-10`; its second-order error was `9.88334483709194e-6`. The original verification threshold stayed `5e-5`. The FD took `17.33883713800003` seconds and passed.

This check used the complete already-completed true zero-H T112 Jacobian held **explicitly affine**, with the original zero-anchor SHA `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` and config SHA `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`. The new warm's H is not equal to that affine anchor. No nonlinear native solution at the new H, new true nonlinear J, final native audit, closed surface, or full BVP acceptance is claimed. The old ready linear graph was not substituted for the actual completed zero J.

## 8. Byte audit and the next concrete calculation

The independent readback [actual49-prefix-byte-audit](2026-11-14-actual49-prefix-byte-audit.json) is 61157 bytes, SHA `3020ae943d5af8faa44d6740a6735402905e3c8d28e1a4606290848276c88eee`. It checked:

- All 128 domain NPZ files and 822 NPY members, including full B/Gamma/Pi reconstruction for all 14 blocks and full beta reconstruction, against the recorded compressed-file and canonical raw-array identities.
- All 58 condensed NPZ files and 58 arrays; 42 references reconstructed 38 distinct complete arrays, including local candidates, final full candidates, multipliers, and original model readbacks.
- Nine original-return observer reports, ten observer NPZ files and 30 arrays, preserving the original nonfinite payload bytes and the flags that the original returned finite/residual values were unchanged.
- All 42 distinct current mathematical/FD source hashes in the actual ledgers, the exact parent48 pair and whole producer subtree, and parent mesh/states/RHS against the current B base.
- The current status identity and FD's complete optimization producer against the saved new warm, including the actual new warm SHA.

The separate [actual49-root-byte-audit](2026-11-14-actual49-root-byte-audit.json), 5847 bytes with SHA `2fef0e2f0281b3d589efcdea814aacc8c4eaba677a3202ce0c95eac1c543041f`, checked all 14 exported raw files, totaling 190956688 bytes, against the recorded `output_arrays` sizes and raw SHA values. These include the local root, gradient, affine data, and recovery arrays. This is independent of the NPZ audit above. The complete factor still has no exported raw files, so neither audit is an independent full-factor file audit. No new scientific numbers were computed by either byte audit.

The next evidence-based model adds only the actual limiting **left-RMS469**, retaining all ten current left-RMS queries and all four current midpoint queries. This would produce 15 complete 2048-angle blocks, 30720 rows, and full local support nodes 469 through 483 plus the three controls, dimension 5073. The C comparison can keep its original 4059-coordinate correction support, provided the complete outside affine contribution is retained. The original QR/R270 library already supports this consecutive full physical support; no change to the BVP, fixed scalar formula, lambda, residual definitions, trial allowance, or final scientific gates is indicated.

That next calculation has not been performed by request49. Its input must be this run's new warm/status pair, not a relabeled parent or a rejected trial. The current result is a preserved numerical warm improvement and a measured domain limit, while the topic's complete same-metric large-amplitude closed-family criteria remain outstanding.
