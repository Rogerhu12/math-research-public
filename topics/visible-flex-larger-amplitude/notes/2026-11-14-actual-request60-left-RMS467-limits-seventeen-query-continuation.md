# Actual request60: a 1/64 step and a newly limiting left-RMS 467 query

- Classification: actual numerical evidence and original-byte provenance; not a full BVP, nonlinear native-tail or closed-surface acceptance.
- Authors: amplitude agent (original reports, prefix and observer byte audits), root agent (unique artifact retrieval, fourteen raw output arrays and publication).
- Date: 2026-11-14 UTC.

## 1. Actual execution and continuation pair

[Run 43640358327](https://github.com/Rogerhu12/math-research-public/actions/runs/43640358327) used source `da346d172715761d7da23da84c92d97a92b438de`. Its prefix job was `132586430139`. The original warm step ran from 21:00:13Z to 21:08:07Z; the new boundary derivative check completed at 21:08:25Z, artifact upload at 21:08:38Z and publication at 21:08:44Z. The job completed successfully at 21:08:47Z.

The warm status records `elapsed_seconds=472.19090206400006`, one accepted optimization step, `optimization_progress=true`, `success=false`, and `new_coupled_finite_acceptance=false`. The saved field is an improved, unaccepted warm field.

Root uniquely retrieved and verified artifact `14131812988`, `visible-followup-condensedqp-43640358327-1`, of 465825094 bytes. Its complete ZIP SHA256 is:

`92a30dc94db8d841338adae5f29aa12e4e4baa43c115e7b1994546151fa2da7e`.

Bounded originals are under [public-actions-43640358327-1-condensedqp](public-actions-43640358327-1-condensedqp/). Complete large arrays remain in that original Actions artifact.

| Original file | Bytes | SHA256 |
|---|---:|---|
| `seventeen-condensed-warm/warm-001.json.gz` | 4783279 | `bc7cadbc17f17832785ace32b011136fd43c04147d450d557730de0f05d40a23` |
| `seventeen-condensed-warm/driver-status.json` | 1577692 | `5b419af7340777328184d7699cf1a4de539cd608c889f6e4f81fe549b253a922` |
| `seventeen-condensed-warm/model-000.json` | 695351 | `c2466a2a9d1a049425128c324342a00dcae998ff5941f9e1a19354d384e608f1` |
| `seventeen-condensed-warm/condensed-QP-summary.json` | 95917 | `692a9a540d4799a2aa22b23ebbe9df9e09ec2cf6200d0e262f0d5b20edf581d0` |
| `seventeen-condensed-warm/condensed-versus-C-comparison.json` | 22500 | `3dc0a21d853eca5af1bedac2e2ad4555e11001bca2f8bb4dae931f7bc54fef8f` |
| `physical-response/response-check.json` | 877872 | `392a3d46563301de1d27ec8aca8072be051ed923bc5fb03797e737317253c53b` |

The published status is gzip-compressed. Continuation must restore the exact original JSON bytes and verify the **uncompressed status SHA** above; parsing and reserializing the JSON is not the same file. The original warm and status together are the actual60 continuation pair.

This run used the actual58 parent warm `3911b6425a15273e29eb610917aea806f25bd07009de86e416f8e85cc91e7864` and original parent status `64140c9f8c2a175456135dcfd18842c06091da6a93758b854627a22fd12a7763`. Their complete producer subtree, status binding, mesh, states and RHS were independently checked against the current B base. Request60 used the already frozen seventeen-query entry's own-schema continuation path and built a new model at the actual58 saved field.

## 2. Frozen equations, sources and complete model

The producer schema is `exact-constraint-seventeen-query-condensed-complete-H-warm-v1`. Its [frozen interface](2026-11-14-seventeen-query-condensed-col-observer-interface.md) and mathematical definitions did not change. The four executed source hashes were:

| Source suffix after `geometry_20261114_seventeen_query_` | SHA256 |
|---|---|
| `domain_operator.py` | `5bb4f214d4d2505185448a9162c0d995bdb6c37168e6d9542dfe6202e8f21a41` |
| `condensed_warm.py` | `f8131287af5d10653692f6e5b7c3cf8ee1d4f17757c3017007b20061598f317b` |
| `condensed_response.py` | `f85fefd928e5ff7945e10082419e197b1b8c5cf3c4d00c1cdcd270380470bbbb` |
| `collocation_observer_warm.py` | `4205f7322d67cac1c3e851fb5759612ea31288433a21b90fa55b8b8406916121` |

The twelve left-RMS queries remained `(468,469,470,471,472,473,475,477,479,480,481,482)`, at original fraction `0.17267316464601146`. The five original collocation midpoints remained `(473,475,477,481,482)`. Each query retained all 2048 physical-angle samples. The resulting B had 34816 rows and 236036 complete coordinate columns; its local support was physical nodes 468–483 plus all three global controls, or 5411 columns.

The fixed C baseline still corrected only nodes 471–482 plus controls, or 4059 columns. Its effective offset retained every outside raw contribution. This restricted C calculation was only the comparison candidate. The complete-H branch retained the full affine exterior response, all 109 free-core coordinates and pure-global rows under [R268](../results/R268-complete-regularized-chain-border-QR.md) and [R270](../results/R270-exact-local-support-damped-QP-condensation.md).

The original A construction made 88 Jacobian calls. The domain operator captured the needed original endpoint blocks from calls 59 and 61, with 16 endpoint nodes and 16 variants. Shared node 480 had identical original J/P bytes across the two original chunks. No second complete J was constructed. Original collocation midpoints came directly from `state.middle` and `problem.mid`, retaining their original endpoint J/P and direct scalar-control chains.

The original budgets remained damping 270, LSMR 200, C projection 200 sweeps, 512 working rows, 200 dual sweeps, 600 seconds for the complete-H candidate, 90 seconds original-trial reserve, 30 seconds complete-recovery reserve and 1200 seconds total. The seventeen original trial allowance, original node/midpoint/rho/boundary guards and both 698-query RMS rules were unchanged.

The current B model identity was:

`e66553c9c84d1a769abc7fb1dfd2ef96c273f74eec7601a1fc91e2a1fed1ef7a`.

Compiled B storage was 189120512 bytes. Recorded implementation checks were:

| Actual check | Saved result |
|---|---:|
| B/transpose maximum normwise error | `1.2736627414094321e-18` |
| Local/full action difference | `0` |
| Actual LSMR-direction original complex-chain relative error | `6.650370794300038e-13` |
| Seeded-direction original complex-chain relative error | `8.021762760044932e-13` |
| Independent original collocation complex-direction error | `8.673617379884035e-19` |

The last check covers free inlet core and global controls with all interior physical coordinate directions zero. It is not a check of every interior coordinate direction. All recorded implementation checks passed their original thresholds; no scientific gate was added.

## 3. Fresh weights and the actual complete-H direction

The fresh model merit was `43.92644933127726`, physical collocation maximum `0.00710961172228531`, boundary maximum `4.4918924725999154e-8`, and sampled rho minimum `0.16604058243274977`. Original left and constant-coordinate residuals were zero. The row weights were calculated once at this base and held fixed over this model's original trials.

This fresh weighted functional differs from request58's earlier fixed functional. Cross-round merit values must not be subtracted as if the weights were identical.

The unprojected LSMR run stopped with `istop=7` at 200 iterations, taking `31.096686235999982` seconds. Its saved actual preconditioned normal norm was `0.0016542140706583177`, whereas the original regularized-gradient norm was `6011.58001689758`. These are distinct quantities. The raw direction had actual derivative `-1.165715291928317` and damped model decrease `0.5835356101977087`; it was not the final nonlinear trial direction.

The C baseline completed its 200 sweeps with its complete outside offset. It reported 4096 computed zero local rows and 104 zero-row negative-offset cases. Those describe the assembled binary64 restricted C subproblem, not exact real infeasibility of the complete B problem. It retained whole-vector radial repair and the feasible backup. Its reported original full objective was `43.925735135817`.

The complete-H branch actually ran and was selected using the same original A, b, damping, B and c. Its full objective was `43.64931793122075`, below the C candidate's objective. Factorization took `19.05226279300001` seconds, with 1486451296 bytes of memory-only factor arrays. Condensation took `10.681447987000013` seconds, retained all affine terms, used 215 reverse fronts and eliminated all 109 free-core variables while retaining the three controls. The local dimension was 5411. The total helper time including factorization, condensation, QP and recovery was `186.38176777300004` seconds.

The QP used 512 working rows and reported literal stop reason `maximum-working-row-budget`. It took `151.83556997699998` seconds, with 1543 local-H actions, 512 local inverse calls, 2112 local B actions, 1029 local B-transpose actions and 512 row reads. The last added working row was row 25720: query index 12, original midpoint 473, angle index 1144.

At the last unrepaired local stage, all 34816 slacks were finite; 420 were negative, with minimum `-2.5263124925345437e-13`. The worst relative violation was `1.597741314689991e-11`, at original left-RMS 482, angle 0. The saved local stationarity norm was `1.4271103671450796e-10`. Local radial repair had factor `0.9999999999839644`, after which the saved all-row minimum was zero with two zero entries. These original reports do not support describing this round's optimization step as suffering a substantial working-row feasibility deficit merely because its literal stop names the budget.

Following the one complete affine recovery, the original full selector retained segment parameter 1 and a whole-vector radial factor `0.9999999999729515`. The selected direction's reported values were:

| Quantity | Actual saved value |
|---|---:|
| Original full directional derivative | `-0.5462399400799908` |
| Original damped model decrease | `0.27713140005653114` |
| Weighted J-direction squared | `0.1934421212974709` |
| Damping penalty | `0.3447749587494484` |
| Scaled direction L2 norm | `0.0021747237301463305` |
| Maximum coefficient direction | `0.00016523467572641986` |
| Minimum of all 34816 final linear slacks | `1.942890293094024e-16` |
| Negative/zero final linear slacks | `0 / 0` |
| Original full stationarity norm with actual multipliers | `1.5202754922228684e-5` |
| Complementarity sum | `2.310107535560017e-13` |
| R267 reported lower-bound diagnostic | `43.649317931220516` |
| R267 quadratic residual term | `1.5852109549063683e-15` |

The original raw-ray feasibility factor was `0.00007830645640295167`; it was not the selected complete-H direction. The comparison reports a raw floating-point cross-point gap `2.3447910280083306e-13`. These are ordinary floating-point model diagnostics, not validated enclosures, exact QP optimality, a new BVP gate or a substitute for the original nonlinear domain checks.

The selected complete direction has identity `ef93768be218c5217a39f1af70cd3864574a69691b06597d51cc0872c229eae1`; its actually saved complete A action has identity `f8d72bae60c43349cf5f2b64a9171594a6045c3691a8c15efd20640a71381405`.

## 4. Complete recovery and its actual scope

The R270 model identity was `b1c61afca53558c0040e5829f3c4ed559922dfd6d4d9cf269c8f4acdbaaa4ca6`. There was exactly one original full-H recovery solve. The requested local coordinates were not silently overwritten into its returned full vector. Original A and A-transpose were read back on that actual vector; the supplied and frozen-reference same-vector actions each differed by zero in their saved reports.

| Actual recovery readout | Saved result |
|---|---:|
| Original full-H residual L2 | `5.530570765031681e-10` |
| Original relative residual L2 | `9.840749163045246e-16` |
| Local mismatch L2 | `4.9906715761539823e-17` |
| Local mismatch Linf | `2.545842226267525e-17` |
| Exterior gradient L2 | `5.530565590383285e-10` |
| Exterior gradient Linf | `2.6193447411060333e-10` |
| Local RHS embedding error L2 | `9.477808598837042e-16` |
| Recorded maximum RSS | `4039840 KiB` |

The report keeps the nine original input-array identities and four factor-array identities, and records three factor byte rechecks. `factor.input_identity` is null; its canonical null SHA is not a unique numerical model identity. The full factor arrays were memory-only (`file=null`) and were not exported. Independent byte auditing here covers exported data, not nonexistent full-factor files. The local root and thirteen other raw output arrays were exported and separately checked by root.

Global radial repair changes the whole vector, including exterior variables, so exact conditional optimality after that selector change is not claimed. The complete full-vector merit, slack, A/AT/B/BT diagnostics and original nonlinear trials were evaluated on the actual selected vector.

## 5. Every original nonlinear trial

The original engine tried seven of its permitted seventeen step lengths. No trial had a node-domain failure. The larger steps failed at actual original collocation midpoints. Smaller trials recomputed the original complete RHS and both original RMS query sets. The following numbers are read directly from the original reports, not recomputed locally.

| Trial step | Original midpoint failures | Original RMS outcome | Actual merit / outcome |
|---:|---|---|---|
| `1` | 473,475,477,480,484 | Not requested after nonfinite midpoint RHS | Not defined; rejected |
| `1/2` | 473,480,484 | Not requested after nonfinite midpoint RHS | Not defined; rejected |
| `1/4` | 480 | Not requested after nonfinite midpoint RHS | Not defined; rejected |
| `1/8` | 480 | Not requested after nonfinite midpoint RHS | Not defined; rejected |
| `1/16` | None | Only left-RMS 467 invalid; right RMS all valid | `43.89263556484359`; rejected on domain |
| `1/32` | None | Only left-RMS 467 invalid; right RMS all valid | `43.90946269547916`; rejected on domain |
| `1/64` | None | Both 698-query RMS sets all valid | `43.91793532799495`; accepted warm |

At steps `1/4` and `1/8`, all seventeen modeled actual query grids were positive even though the unmodeled original midpoint 480 failed. At step `1/4`, that midpoint's saved minimum was `-0.04732777206468408`, at angle index 163; at step `1/8` it was `-0.011156295078476264`, at index 882. These larger-step failures are distinct from the nearest rejected trial.

At step `1/16`, all nodes, midpoints and seventeen modeled actual full-angle query grids were valid. The actual merit decreased by `0.033813766433674175`, against predicted decrease `0.0337621796118403`, with ratio `1.001527947023177`. The only original RMS failure was left-RMS 467, with beta squared `-0.4220345939277368` at phi 0.

### Nearest rejected step: 1/32

This trial had all nodes, all original midpoints and all seventeen modeled query grids valid. Its actual merit decrease was `0.016986635798105`, predicted decrease `0.01697554396670993`, and ratio `1.0006534006460601`. Its minimum selected linear beta squared was `0.0018434149674966043`. The right-RMS set had all 698 queries valid.

The only invalid original left-RMS query was:

| Original query field | Saved value |
|---|---:|
| Interval | `467` |
| Original left station | `1.169440253991355` |
| Original right station | `1.174424705491115` |
| Original RMS fraction | `0.17267316464601146` |
| Actual query station | `1.170300935005843` |
| Scalar radius | `1.1933206462226578` |
| Scalar first derivative | `-0.07434857717191798` |
| Scalar second derivative | `-2.493080786236819` |
| Original beta squared minimum | `-0.006303834965005084` |
| Physical angle of reported minimum | `0` |
| Curve curvature at reported minimum | `0.06210848607314795` |

This is an actual original-domain rejection despite a genuinely decreasing merit, not rejection for the direction slope or the near-zero linear slack of an already modeled query. It supplies a specific missing query for the next algorithmic model.

### Accepted step: 1/64

The actual decrease was `0.008514003282314775`, predicted decrease `0.008511385523552411`, and ratio `1.0003075596511426`. The minimum selected linear beta squared was `0.0018580452450164156`; all seventeen actual selected grids and both original RMS sets were valid.

The accepted saved field had physical collocation maximum `0.007109591304982551` and boundary maximum `4.4217061600063744e-8`, with exact left and constant-coordinate residuals zero. This passes the original warm-step domain and merit conditions. It does not meet or assert the final full BVP acceptance.

## 6. Read-only location observer: the largest physical residual remains at interval 461

The observer reports 17 original `evaluate` calls, one original weights call and zero observer errors. It adds no RHS, J, profile, boundary, model or trial calls. Its saved original flags and residual bytes are unchanged. The complete physical maximum is undefined for the four evaluations whose original midpoint RHS is nonfinite; the report distinguishes that from finite original physical arrays followed by a later RMS-domain rejection.

For every finite complete physical residual array, the reported largest-magnitude component remained interval 461, radial coefficient 1, component index 1, complete physical row 155819. It is outside the current B support, but remains in the full original objective, full A and complete-H exterior response.

| Original row quantity | Base evaluation | Accepted full-RMS evaluation |
|---|---:|---:|
| Signed collocation residual | `-0.00710961172228531` | `-0.007109591304982551` |
| Left state component | `0.21357039690557744` | `0.21357038944960816` |
| Right state component | `0.20642164418735295` | `0.20642164063059937` |
| Left original RHS component | `-0.00985808499672205` | `-0.009861581274436104` |
| Right original RHS component | `-0.005934639763494642` | `-0.005938442951506827` |
| Original midpoint RHS component | `-0.007830746523776595` | `-0.007833892541421177` |
| Original midpoint state component | `0.2099935760186556` | `0.20999357070351657` |

The original stations were left `1.139533544992796`, right `1.1445179964925558`, midpoint `1.1420257707426757`, with interval length `0.004984451499759901`. The row's actual frozen weight for this model was `199.06505212461812`, within the complete W identity:

`f7c12ff520001da71f62f2cc7e242b0b6e0d81dc2f8b3624ffbad68d76c01cdb`.

Thus the maximum row's slow change is not evidence of a zero weight or omission from the full problem. The current model's small stationarity diagnostic does not imply rapid improvement of this individual unweighted component. No unique damping-causality claim follows. The [actual58 stored-row note](2026-11-14-actual58-stored-final-direction-at-largest-collocation-row.md) separately records the previous model's actual saved b/Az components and their algebraic interpretation; those numbers must not be transferred to request60's different weights and direction.

## 7. New boundary derivative check, with the native scope unchanged

The original complete affine physical-angle boundary test was genuinely rerun at the new actual60 warm. The check binds its exact new warm SHA and entire producer. Its maximum fourth-order Richardson relative directional error was `7.009663695797188e-10`, below the unchanged `5e-5` implementation threshold. The maximum second-order error was `9.883394384635908e-6`, with the original truncation-contract flag true. Runtime was `16.61132149900004` seconds.

This used the complete actual zero-H T112 Jacobian held explicitly affine, from response SHA `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` and configuration SHA `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`. It did not use `ready.linearD`. The actual warm height is not the zero anchor. The report explicitly records `nonlinear_DN_evaluated=false`, `nonlinear_native_at_current_H_solved=false`, `full_BVP_solved=false` and `full_Cartesian_closed_surface=false`. No old FD pass or prior warm SHA was relabeled.

## 8. Independent original-byte audits

These checks only read saved JSON, ZIP/NPZ/NPY or raw bytes, verify metadata and hash identities, and compare original source/producer bytes. No local scientific evaluation, matrix action, dot product, norm, extrema search, FD, optimization or native solve was performed.

The [prefix byte audit](2026-11-14-actual60-prefix-byte-audit.json), 76863 bytes, SHA256 `295b2eca720c9eb7181692217a653a4b9b611759099ec47da5d3e1aa0ed2978c`, verifies:

- All 154 domain NPZ files and 994 NPY payloads, including reassembled B, Gamma, Pi and beta identities, endpoint bindings and original midpoint bases.
- All 88 condensed NPZ files and 88 NPY payloads; 42 complete array references resolve to 38 unique complete original arrays, each reassembled identity checked.
- Eleven saved midpoint-observer report entries, ten NPZ files and thirty NPY arrays, preserving original nonfinite bit patterns and unchanged-return assertions.
- Forty-eight source hashes, the new warm/status/FD producer equality, the exact actual58 parent pair, the full parent producer subtree and parent mesh/state/RHS binary64 byte correspondence with the current model base.

The [collocation observer byte audit](2026-11-14-actual60-collocation-observer-byte-audit.json), 73094 bytes, SHA256 `668847a985a9498e87ced85e7c5b851fb05f0615322abad47032248dc07a4d67`, verifies all seventeen original observer JSON reports and eleven embedded report bindings, the current weights identity, raw signed component bits and unchanged-original flags.

Root's separate [fourteen-raw-array audit](2026-11-14-actual60-root-byte-audit.json), 5802 bytes, SHA256 `bac1810d40399f4690e789c5168fd7e1aa6b88bffd7a52a18f3a6fdfbad4ec5b`, verifies all fourteen exported raw arrays totaling 245864112 bytes against original size, dtype/shape and raw SHA descriptors. It binds the original condensed-root status, 29223 bytes, SHA `caaf4a24572862cd410824b84fc7e655f10d6849d7dc08efeca4059bc90318aa`. These exported local-root, affine, gradient and recovery bytes are distinct from the unexported full chain factors.

The complete artifact ZIP was independently verified by root. The public bounded archive does not contain every large payload; the original Actions artifact is the authority for those complete bytes.

## 9. Consequence and the next concrete calculation

Request60 successfully continued the same frozen seventeen-query algorithm from the actual58 field, and the completed new field is the pair in Section 1. The nearest rejected step now isolates an omitted left-RMS 467 query while all modeled grids, original nodes/midpoints and the right-RMS rule pass. The complete-H candidate's last local feasibility repair is at rounding scale; this record does not justify increasing the working-row budget as the immediate response to this particular rejection.

The authorized next calculation is a separate eighteen-query entry adding only the actual original left-RMS 467 query with all 2048 angles. Existing twelve left-RMS queries and five midpoints remain. Complete B support must include nodes 467–483 plus all three controls, giving 5749 local columns and 36864 rows. The original C baseline remains 4059 columns and retains its full outside offsets, now explicitly including node 467 as well. The new entry must retain all original J/P and scalar dependencies, complete-H affine exterior recovery, original budgets, all original domain/merit checks, seventeen-trial allowance, read-only observer and actual new-warm FD.

The midpoint480 failures occurred only at larger rejected steps in this model and are not silently added as if they caused the nearest rejection. This planned eighteen-query calculation is not yet a result. No completed full BVP, actual nonzero-H native tail, same-g refinement, closed C2 family, final curvature/reach/held-amplitude certificate or topic completion is asserted here.
