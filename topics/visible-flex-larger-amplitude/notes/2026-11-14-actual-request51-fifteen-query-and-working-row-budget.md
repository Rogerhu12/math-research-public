# Actual request51: fifteen-query warm and the remaining working-row budget

**分类**：启发式/数值证据。**作者**：ChatGPT（amplitude；root 完成下载、raw数组审计与发布）。日期：2026-11-14。

## 1. Preserved result and the distinction needed for continuation

Request51 completed one real fifteen-query warm step, accepting `alpha=0.125`, and passed the original complete affine physical-angle boundary FD at the saved new field. Its fixed-weight merit decreased from `44.20135024608698` to `44.115161170653145`, a recorded decrease of `0.08618907543383614`. The result remains an explicitly unaccepted warm: it is not a full native-tail solve, a full BVP solution, or a completed closed family.

Two separate limitations are visible in the actual data:

1. The closest rejected nonlinear trial, `alpha=0.25`, failed at original midpoints481 and482. Midpoint481 is outside the fifteen-query model; midpoint482 is already fully modeled. Every predicted linear beta value at that trial was positive, yet the actual midpoint482 minimum was negative. Adding midpoint481 alone would therefore not identify or resolve the whole observed limit.
2. The fixed quadratic subproblem reached its 256-working-row budget with a substantial violation at an original row that was not in the working set. Its subsequent local radial factor was `0.9133739508941273`. The final full stationarity and R267 diagnostics are correspondingly much looser than the pre-repair local stationarity. This is an actual bounded-optimization issue, not evidence of an inaccurate complete-H inverse.

The selected next configuration is a bounded continuation from this run's accepted warm using the same frozen fifteen-query entry and changing only `--condensed-max-working 256` to 512. The original dual-sweep, candidate-time, total-time, trial, FD, and scientific gates are retained. That next configuration was **not** executed by request51; its result must be read independently. No sixteenth query is added by this conclusion.

All scientific numbers below are saved results from this public repository's Actions. Later local processing only read original reports and checked file and array bytes; it did not evaluate a matrix action, norm, optimizer, ODE, derivative, or native response.

## 2. Actual run and immutable input identities

| Item | Identity |
| --- | --- |
| Run | [43632815810](https://github.com/Rogerhu12/math-research-public/actions/runs/43632815810) |
| Scientific job | `132563011884` |
| Source commit | `bd3fc94a6092313313daf607328a9695e80c17f4` |
| Artifact | `14128803396`, `visible-followup-condensedqp-43632815810-1` |
| Complete ZIP size | `389396609` bytes |
| Complete ZIP SHA256 | `790703540d90dd71d1b8edc73ef4489b0ef9ee83a3e216a3b584512dfafc5f24` |
| Warm step | `19:35:03Z` to `19:40:55Z`, success |
| Original FD step | `19:40:55Z` to `19:41:14Z`, success |
| Artifact upload | completed `19:41:23Z`, success |
| Ordinary publication | completed `19:41:28Z`, success |

Root downloaded the complete artifact once, checked its ZIP SHA, and marked extraction complete before the readback. Published results are under [public-actions-43632815810-1-condensedqp](public-actions-43632815810-1-condensedqp/); the warm directory is `fifteen-condensed-warm/`.

The independent sources are those frozen in the [fifteen-query interface](2026-11-14-fifteen-query-condensed-warm-interface.md):

| Source | SHA256 |
| --- | --- |
| `geometry_20261114_fifteen_query_domain_operator.py` | `c6581f0b8fdef4c3bc48d364c6845cff9a4244b043a4d14c772ef6fd3b2503e8` |
| `geometry_20261114_fifteen_query_condensed_warm.py` | `f1310edc94fb3a9c9f95b5dad98e7073c1879997b9a9bdf06c5028e91f83351e` |
| `geometry_20261114_fifteen_query_condensed_response.py` | `3328eb649daab9b7e2da831e0fd6fa864f10f4dd6c98c51adff0ddfbe0424487` |

The actual parent pair was request49:

- Warm SHA `c0d9c6d59e16ef1482f8ee60f9681d8db089b21d68e249adf1830df03be6612b`.
- Original status SHA `e22fd03b8c24adbd0eeeaf0b084d18944d17e4cd1f4115075cb63d9e9a41aad7`.

The parent producer subtree, complete scalar/profile description, original accepted96 and prepared699 identities, true zero112 anchor, original112 config, modes, mesh, and source ledgers were retained. Parent mesh/states/RHS agree exactly with this B model's original binary64 base. Their canonical identities are respectively `7cef3604718c2d21dc4f0c866d29a08dc05b1596b49e4ea81a415cf9a9dc68bb`, `ca16832a85466107a0085c83dd1e40d13d7e11dcd3686604eaafb9a7f7933558`, and `81ec25e324fda600a6551502063decbc86ad4b2131b55a9850257fcc60954234`.

The parent is the actual49 saved field, not its rejected trial and not the old prepared699 initial guess. Each round fixes its own merit weights; the actual51 starting merit must not be compared by direct subtraction with the printed merit of another round.

## 3. Full B construction and independent implementation checks

The eleven original left-RMS intervals were `469,470,471,472,473,475,477,479,480,481,482`, each at fraction `0.17267316464601146`. The four original collocation midpoints were `473,475,477,482`, each taken directly from `state.middle` and `problem.mid`. Each block used all 2048 original physical-angle points.

B had 30720 rows and 236036 full coordinates. Its complete local support was 5073 coordinates: physical nodes469 through483, plus all three global scalar controls. The compiled row storage was `166871040` bytes. Its actual model SHA was:

`bdf80051c378b09a7583964f0d5883a14b4893437a4170e59f22c0f2ba8ab98d`.

The original complete linearization made 88 Jacobian calls; the domain operator only captured the relevant original calls 59 and 61. There were 15 unique endpoint nodes and 15 stored variants. The original returned factors were unchanged; no second complete Jacobian or native tail was constructed.

| Saved Actions implementation check | Result |
| --- | ---: |
| Maximum normwise adjoint error | `5.062864396402891e-18` |
| Maximum local/full action difference | `0.0` |
| Maximum original complex-chain relative error | `8.781637017252139e-13` |
| Independent physical collocation complex check | `8.673617379884035e-19` |

The final check has the saved scope **only free inlet core and global controls; interior physical coordinates zero**. It is not an independent directional check of every interior physical column. The full B complex-chain check includes the actual saved LSMR direction. These are implementation checks with the retained thresholds; they are not an exact continuous-domain certificate.

## 4. Raw direction, restricted C comparison, and complete-H recovery

The raw LSMR run retained `lambda=270`, the original weights, 200 iterations, and the original `atol=btol=1e-7`. It stopped with `istop=7` at its iteration budget. Its saved original regularized gradient norm was `1066.0787181769729`, and its actual preconditioned normal norm was `0.0003149507772046886`. They describe different residuals. The raw direction had slope `-1.2412655755210824` and damped model decrease `0.6206548220116828`.

The C correction still used only nodes471 through482 and all three controls, 4059 coordinates. The complete outside contribution of nodes469,470,483 was retained in the affine offset. At this actual base, 46 computed-zero local rows had negative effective offsets. This is a statement about the rounded restricted local C problem; it is not a proof about exact real coefficients or a reason to reject the original BVP.

The C algorithm continued to its 200-sweep budget and used the original global repair/fallback. Its projected-candidate radial factor was `0.002339257417370177`; its raw-ray radial factor was `9.792117321138833e-5`. Raw/candidate complete offset reconstruction differences were `6.394884621840902e-14` and `4.879430193227563e-14`. The final C objective was `44.19965648440193`, with damped model decrease `0.0016937616850526487`. Outside coordinates were unchanged only before the full-vector radial operations, as explicitly recorded.

The complete-H candidate retained all outside variables through the unchanged [R270 affine condensation](../results/R270-exact-local-support-damped-QP-condensation.md). It conditionally eliminated 468 left physical nodes, 215 right physical nodes, and 109 free-core variables, retaining nodes469 through483 and all three scalar controls. Its model SHA was:

`e8714fe8079979ab17f7fc64d07780630fda87dc27aa4d23471d8a7e98d50893`.

There was one factorization and one final full recovery, with 256 local inverse calls and 775 local H actions. Condensation took `7.605408702000034` seconds, the local QP `35.24296228600002` seconds, and the full helper `60.11665572800001` seconds. The saved maximum RSS was `3923808` KiB. The original linear term was retained; an approximate center was not substituted for it.

The full recovery had these actual readbacks:

| Readback | Value |
| --- | ---: |
| Local mismatch L2 | `2.1575534774155637e-17` |
| Local mismatch Linf | `8.228078049628273e-18` |
| Original H residual L2 | `8.485386777905189e-10` |
| Original H relative residual | `9.44868986978053e-16` |
| Exterior gradient L2 | `8.485381357589182e-10` |
| Same-vector supplied/reference A difference | `0.0` |
| Same-vector supplied/reference AT difference | `0.0` |

No actual local coordinates were overwritten after recovery. As before, `factor_input_identity` is null and its hash is not a unique model identity. The report preserves the nine actual input-array identities, four factor-array identities, and three factor byte rechecks. The full factor arrays remain memory-only with `file=null`; saved hashes do not amount to an independent full-factor file audit.

## 5. The actual working-row limit and repair

The QP stopped at its 256-working-row budget. The final added row was13192, query 6: left-RMS477, angle 904. The last local dual solve completed 200 sweeps and also stopped at its sweep budget. Its maximum coordinate update was `1.1735674166195656e-5`, normalized working slack minimum `-2.5126096784879037e-6`, and normalized complementarity `1.4300988394522919e-6`.

The unrepaired candidate had 436 negative original slacks, minimum `-0.02946515761551116`. Its worst relative violation was `0.09484182138220355` at row 10349: left-RMS475, angle 109. The saved slack there was `-0.027790851285636964`, against reserve `0.2930231714302751`. **Row10349 is absent from the final 256-row working list.** This membership fact was checked directly in the saved metadata, without evaluating B.

The pre-repair local stationarity norm was `2.3437884570528478e-11`. The local radial factor `0.9133739508941273` then made every original linear row feasible, and the feasible local segment selected parameter1. The subsequent full recovery and original full B readback needed only a final radial factor `0.9999999999999457`; the global segment parameter was1. The selected full vector's 30720 slacks were finite and nonnegative, with minimum `4.107825191113079e-15`.

The same complete-model comparison selected R270-H:

| Final original-model diagnostic | Value |
| --- | ---: |
| C objective | `44.19965648440193` |
| Selected complete-H objective | `43.818862483377366` |
| Actual selected derivative | `-0.7040293555962288` |
| Damped model decrease | `0.38248776270961804` |
| Final full stationarity norm | `363.2000886229586` |
| Complementarity sum | `0.0006578285800793663` |
| Best R267 floating lower-bound diagnostic | `42.91344262204301` |
| Final floating gap diagnostic | `0.9054198613343587` |
| Floating distance-bound diagnostic | `0.004983979440709453` |

The small pre-repair local stationarity must not be reported as the final full stationarity. The full R267 gap is not small, and all these posterior readouts remain ordinary floating diagnostics, not validated enclosures. The finite full direction still genuinely reduces the original damped model and passes the original all-row feasibility readback. Model optimality was never a new scientific acceptance gate.

The data support spending more of the already bounded work on the same constraint set. They do not prove that doubling the working-row limit will remove the nonlinear domain restriction. They also do not identify the full-H inverse as the source of that restriction.

## 6. Every actual nonlinear trial

The original seventeen-trial allowance was unchanged. This execution tried its first four candidates and accepted the fourth.

| Alpha | Invalid original midpoint indices | Actual modeled query failures | Original RMS reached? | Result |
| ---: | --- | --- | --- | --- |
| `1` | `473,475,477,481,482,483` | ten of eleven left-RMS grids and all four midpoints | no | midpoint domain rejection |
| `1/2` | `473,475,477,482` | left469 and all four modeled midpoints | no | midpoint domain rejection |
| `1/4` | `481,482` | midpoint482 | no | midpoint domain rejection |
| `1/8` | none | none | both complete levels passed | accepted warm |

All node checks, the original uniform-phi rho guard, and boundary finiteness passed throughout. The closest rejected midpoint inputs were finite. Their original RHS values were nonfinite, and the read-only observer measured:

| Original midpoint | Station | Actual minimum beta squared at alpha1/4 | Angle index | Phi |
| --- | ---: | ---: | ---: | ---: |
| 481 | `1.2267614462385934` | `-0.01321064927182114` | `86` | `0.2638446955163303` |
| 482 | `1.2317458977383535` | `-0.0032933581226197717` | `82` | `0.25157284921324513` |

Midpoint482 is already one of the complete modeled query blocks. The saved minimum across **all 30720 linear predicted beta values** at alpha1/4 was positive, `0.001616517352433412`. Thus the actual negative midpoint482 value is an observed nonlinear deviation from this feasible first-order model. No new per-angle arithmetic was needed to establish that sign distinction. At this failed step, the original RMS gate was not reached, so no unobserved RMS failures or successes are asserted.

At the accepted alpha1/8, the actual fixed-weight merit was `44.115161170653145`. Predicted decrease was `0.08591829172092105`, actual decrease `0.08618907543383614`, and their saved ratio `1.0031516421880762`. Both original 698-query RMS levels had zero failures; all 15 selected angular grids were also valid. The physical collocation maximum was `0.007110002311305403`, compared with `0.0071101678278726824` at this model's start. The boundary maximum was `6.280522697136224e-8`, while inlet and constant-row maxima remained0. The rho minimum was `0.16604058243274977`.

The location of the largest physical collocation component was not saved in these reports. Neither a location nor a cause for its small relative change is invented. The merit decrease is measured with this model's fixed weights and is not a proof that every residual component decreases by the same factor.

## 7. New saved pair and original affine FD

| File | Actual SHA256 |
| --- | --- |
| `fifteen-condensed-warm/warm-001.json.gz` | `b6620a0ce55be257fc58c29e88187cc602ad08b46c4424903ffddc003b5b1595` |
| Original `fifteen-condensed-warm/driver-status.json` | `267451f8eb91ca568ff187bfb39dbd32b22ca844788e1e88165910190ad6f685` |
| `physical-response/response-check.json` | `19829b68b911df76f12973d20e799aa4af8837360855ec78f4963b0f76528437` |

The original status is 1051960 bytes; the publisher therefore retains its gzip transport. A continuation must decompress that file to the original bytes and check the original status SHA above. It must not use the compressed-file SHA or reserialize the JSON as a replacement for the original status identity.

The status records one accepted warm step, elapsed `349.84839812` seconds, `optimization_progress=true`, `success=false`, and `new_coupled_finite_acceptance=false`. The complete actual15 source and parent producer descriptions remain in the saved warm and status.

The original full boundary FD was recomputed at this exact new warm. Its fourth-order Richardson error was `7.186294196742241e-10`; its second-order error was `9.883373664116045e-6`. It passed the unchanged `5e-5` threshold in `17.525590421000004` seconds. The entire FD producer matches the saved warm; the old response or old warm SHA was not relabeled.

The FD holds the actual completed true zero-H T112 J explicitly affine. The new warm H is not equal to that zero anchor. The exact anchor and config SHAs remain `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` and `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`. No new native nonlinear solve, nonlinear current-H J, native final audit, or full BVP acceptance was produced here. No ready linear graph was substituted for that completed J.

## 8. Byte audit and the configured next calculation

The complete readback [actual51-prefix-byte-audit](2026-11-14-actual51-prefix-byte-audit.json) is 65409 bytes, SHA `886d87010ea587649a03ee2d77fabb5ea6abcd7bdc54ed6534775523efd51912`. It checked:

- 137 domain NPZ files and 880 NPY members, including exact full B/Gamma/Pi reconstruction for all 15 blocks, full beta reconstruction, and the declared model SHA.
- 63 condensed NPZ files and 63 arrays; 42 stored references reconstruct 38 unique full arrays, with their complete original bytes and saved identities.
- Six original-return observer reports, 12 observer NPZ files and 36 arrays, including original nonfinite payloads and the unchanged returned-finite/residual flags.
- 44 distinct current mathematical/FD source hashes, the actual49 parent pair and its whole producer, and parent mesh/states/RHS against this B base.
- The actual saved new warm SHA, current status identity, and the FD's entire optimization producer.

The separate [actual51-root-byte-audit](2026-11-14-actual51-root-byte-audit.json), 5800 bytes with SHA `8da37bda243f852ff8d97fc483fa96a0305ada0b47e8de7ff6027af27ca3c0cb`, checked all 14 exported raw files, totaling `217496448` bytes, against the sizes and raw SHA values in the actual `status.output_arrays` descriptors. It is independent of the NPZ audit above. The full factor was not exported, so neither audit constitutes an independent full-factor file audit. No new scientific evaluations were performed during either byte audit.

The next configured prefix task resumes the actual51 pair under the same frozen15 schema and changes only the working-row maximum to 512. All fifteen query blocks remain; no midpoint481 block is silently inserted. The same `lambda=270`, LSMR200, C projection200, local dual200, candidate600 seconds, recovery reserve30 seconds, trial reserve90 seconds, total1200 seconds, and original 17 trial allowance remain in effect. The same original FD and all final scientific gates remain intact.

This is a targeted attempt to improve a documented truncated quadratic calculation. It does not promise a larger nonlinear step, and it does not remove the already observed nonlinear midpoint482 issue. Its actual raw slacks, repairs, full stationarity, original trial failures, and saved warm must be examined after it runs. The topic's complete large-amplitude same-metric closed-family criteria remain outstanding.
