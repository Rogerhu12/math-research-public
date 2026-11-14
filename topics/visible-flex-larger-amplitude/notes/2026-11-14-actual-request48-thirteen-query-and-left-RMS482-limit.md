# Actual48: complete thirteen-query direction, then left-RMS482 limits the real step

Date: 2026-11-14. Public repository Actions run `43629964624`, job `132554193810`, source `86acdf3b193efb6ad536545e22c46584fcc0bdd5`. The warm, fresh affine Rphi FD, artifact upload and ordinary publisher all succeeded. The actual accepted warm step was $1/256$, with fixed-weight merit reduction `0.0031563944705226277`. Full BVP acceptance is still false.

The remaining nearest limitation is now **the original left-RMS point of interval482**, not its collocation midpoint. At the five nearest rejected steps, all thirteen modeled angle grids, all699 nodes and all698 collocation midpoints were valid and merit decreased; the original full RMS guard still rejected left-RMS482. The two query kinds must not be identified merely because they share the interval number.

## 1. Source, parent and complete receipt

The unchanged problem inputs are the actual accepted96 source, prepared699 M112 field, true completed zero-H T112 J and original tail config. The actual parent is request45:

- Warm SHA256 `8ce98e5b325eae8188f8b4c707d1abfaa109e50a790c9abe5850ef1a52d08b75`.
- Original status SHA256 `70be19b675c9f558cddbfa9532777a119a7bbe0629f505368e1588842aade30d`.

The three actual new sources are precisely those frozen in [the thirteen-query interface](2026-11-14-thirteen-query-condensed-warm-interface.md): domain `d674a64e11cfac1f57f0c24166546a55045847633935dddb8ef53df4024d3cff`, warm `7785f4eb905da4c3e80ba988c79fa8a34b0a27017e6b8abc99764d8105eccc7c`, and response `2cbd850a3a810f4296920e13629e86a9ca11545d7dd002d1a0d569e9e6d2319a`. The previous twelve-query, original QP, QR and condensation sources were unchanged.

Artifact `14128176114`, `visible-followup-condensedqp-43629964624-1`, is348442586 bytes. Its complete ZIP SHA256 is `3d67eb96dab97143bdc932bd65b52d6abed2c0d214f146d66ab8a33927b9f5b7`. The coordinator downloaded this artifact once and verified that digest before the local readback. Public bounded output is under `notes/public-actions-43629964624-1-condensedqp/`; large root and condensed arrays remain in the original artifact.

The warm step ran from `19:03:58Z` to `19:09:55Z`; FD finished at `19:10:17Z`, artifact upload at `19:10:27Z`, publisher at `19:10:33Z`. The warm producer's recorded elapsed time is `355.213734966` seconds.

## 2. Same original model, explicit thirteen-query support

The retained query order was nine original left-RMS grids on470,471,472,473,475,477,479,480,481, followed by original collocation midpoints473,475,477,482. Every grid had2048 original physical angles. There was no added left-RMS482 block in this run.

The complete B model identity is

`a90001ac0cdf6019bf43eb6807e8cc577e968e0d5e8328e1b1ba2ea7cfd202cd`.

Its shape was26624 by236036; local shape26624 by4735; stored compiled row bytes144621568. The original complete linearization made88 Jacobian calls. Capture retained only calls59 and61, with14 nodes and14 stored endpoint variants. Node483 came from the same original call61. No additional complete Jacobian was constructed. The retained nine RMS grids were compiled through the read-only interval view; the full operator, midpoint compiler, independent complex check and export all used the complete14-node capture.

Original implementation checks passed:

| Existing check | Saved actual value |
|---|---:|
| B adjoint normwise maximum | `4.59450797828714e-18` |
| B local/full action maximum | `0.0` |
| Complete original typed-query complex-chain relative maximum | `1.0356685063030829e-12` |
| Original collocation complex check | `8.673617379884035e-19` |

The last check has its original narrow scope: only free inlet core and global controls are nonzero, with interior physical coordinates zero. It is not a claim that every interior physical direction was independently checked. B's actual supplied full LSMR direction and its separate seeded direction were checked through the original complete endpoint RHS.

The original raw LSMR reached200 iterations (`istop=7`). Its saved unpreconditioned regularized-gradient norm was `1031.1301381403855`; the actual preconditioned normal norm was `0.000211454945704245`. These are different quantities. The selected direction came from the subsequent complete-H candidate; this raw LSMR stopping record does not explain the final real-domain failure by itself.

## 3. C baseline and complete-H candidate

The fixed C correction still used only nodes471 through482 and the three global parameters, dimension4059. Complete B retained the outside contributions of470 and483 through the actual affine offset `c+B_out*z0_out`. Recorded reconstruction discrepancies were `5.684341886080802e-14` for the raw direction and `4.5574655160862676e-14` for the candidate. These are readouts, not new scientific gates. Before global repair, the outside raw coordinates were bitwise preserved by the C projection.

C completed200 Hildreth sweeps. Its global projected-candidate radial factor was `0.0023338144775536846`; its raw-ray factor was `0.00010112888735894439`. The original feasible-segment safeguard retained a C direction with actual full objective `44.251404941685465` and model decrease `0.0017973846143100722`.

The complete-H candidate retained the original $g=A^Tb$, all pure-global rows, all free core and the full affine exterior response. It used4735 local coordinates,215 reverse fronts and one full recovery. The condensation identity was

`e0bee8c334186012558b453ab61026e64f77a1057360cb8ed7ae5dc530bf29e0`.

The library's `factor_input_identity` was null; its `74234e98...` SHA is the hash of null and is not a unique model identifier. The report separately retained nine original input identities and four factor identities. The full factor was memory-only and not exported as independently readable raw factor files.

Saved full recovery diagnostics were:

| Actual original readback | Value |
|---|---:|
| Local mismatch L2 | `2.4315874621066242e-17` |
| Local mismatch Linf | `7.755433665060374e-18` |
| Original H residual L2 | `7.476563936298033e-10` |
| Original H relative residual L2 | `7.774517611391619e-16` |
| Original exterior-gradient L2 | `7.476561047968881e-10` |
| Supplied versus frozen reference A action | `0.0` |
| Supplied versus frozen reference AT action on the same Ax | `0.0` |

The actual returned local coordinates were not overwritten. The reports do not substitute a rounded-root residual for the original A/AT residual. Factorization took `21.583131279999975` seconds; condensation `10.395491102999983`; local QP `43.112776010000005`; the full candidate helper `79.46440986599998`. The maximum reported RSS was3851884 KiB. These are original Actions readouts, not local recomputations.

## 4. Working rows, repairs and actual complete-model comparison

The local QP stopped at its declared256 working-row budget. It performed775 local-H actions and256 local inverse calls. The final newly added row was22441, query10, midpoint475, angle1961. The last dual sweep200 had coordinate update `5.772746650817805e-10` and normalized working slack minimum `-2.1297770491646162e-10`.

Before repair, the last local stage had510 negative original slacks, minimum `-2.1171822239818283e-8`, maximum relative violation `8.956944533774364e-8`. Its worst relative row was9151, left-RMS475, angle959. The local stationarity norm was `4.122739831439033e-11`. The local radial factor `0.9999999104305483` restored all26624 rows, with minimum `4.274358644806853e-15`.

After the unique full recovery, the original complete selector made one additional radial correction `0.9999999999991195`, then used segment parameter1. The actual final direction was therefore not exactly the unaltered conditional recovery. Its original complete-direction identity is

`d69b43e72b6be00b632cfb925ceac6a58be5867da2c33fec2ebaf1482625d85f`.

| Same fixed model in this run | Saved value |
|---|---:|
| Initial merit/model objective at zero | `44.253202326299764` |
| Original C objective | `44.251404941685465` |
| Selected full-H objective | `43.844546783272705` |
| Selected actual directional derivative | `-0.8086697931212347` |
| Selected damped model decrease | `0.40865554302708174` |
| Final complete linear slack minimum | `1.942890293094024e-15` |
| Final complete linear negative count | `0` |
| Actual original stationarity L2 | `0.00034893309016046156` |
| Actual complementarity sum | `8.763576837099334e-10` |
| Best raw floating R267 lower value | `43.84454678239551` |
| Final raw floating gap | `8.771934290052741e-10` |
| Final raw floating distance bound | `1.551311166310468e-7` |

The full-H candidate won the actual same-model comparison. The remaining real-domain restriction is not explained by severe radial contraction of this candidate. The tiny printed R267 gap is still ordinary floating arithmetic, not a validated certificate of the exact full QP. A new model has freshly frozen weights: its initial merit must not be subtracted from an earlier model's terminal merit as if the two objectives were identical.

## 5. Complete real trial record

All nine tried steps retained finite original nodes, the original positive uniform-phi rho guard and finite boundary evaluation. The original seventeenth-trial budget was not enlarged. The five nearest rejected steps and the accepted step had no failed original collocation midpoint.

| Alpha | Actual midpoint failures | Full RMS outcome, if reached | Decision |
|---:|---|---|---|
| 1 | 473,475,477,482,483 | Not reached | Reject |
| 1/2 | 473,475,477,481,483 | Not reached | Reject |
| 1/4 | 483 | Not reached | Reject |
| 1/8 | None | Left469 and left482 fail | Reject |
| 1/16 | None | Left482 fails | Reject |
| 1/32 | None | Left482 fails | Reject |
| 1/64 | None | Left482 fails | Reject |
| 1/128 | None | Left482 fails | Reject |
| 1/256 | None | Both full698-point RMS grids pass | Accept warm |

At $1/4$, every modeled grid was positive, while unmodeled midpoint483 had minimum `-0.08287213984348285` at angle0. At $1/8$, left469 had minimum `-0.27853571724180726` at phi0, in addition to left482. These are larger-step observations; they do not justify treating an arbitrary untested new point as the nearest limitation.

The saved left-RMS482 failures were:

| Alpha | Minimum beta squared | Original angle location |
|---:|---:|---|
| 1/8 | `-0.05954958880597161` | phi `0.06442719309119693` |
| 1/16 | `-0.009957543056214657` | phi `3.11091303783208` |
| 1/32 | `-0.05144047504659022` | phi `0.0337475773334841` |
| 1/64 | `-0.04555530362297966` | phi `0.0` |
| 1/128 | `-0.018448315937696913` | phi `0.0` |

No monotonicity of these discrete minima versus alpha is asserted. All thirteen modeled grids were positive at each of these five steps. Each also had an actual merit decrease with an actual-to-predicted ratio close to1; rejection came from the original complete RMS domain check, not from a failure to decrease merit or an altered acceptance test.

At the accepted $1/256$ step:

- Actual fixed-weight merit became `44.25004593182924`.
- Actual reduction was `0.0031563944705226277`.
- Predicted unregularized reduction was `0.003156262947048806`.
- Actual/predicted ratio was `1.0000416706326527`.
- Physical collocation maximum changed from `0.007110255988772191` to `0.007110250799470694`.
- Complete affine boundary maximum was `7.656256251336757e-8`.
- Rho minimum was `0.16604058243274977`; exact-left and constant-state residual maxima stayed0.

The physical collocation maximum remains much larger than the original eventual BVP tolerances. Its worst position/component was not saved by this scalar maximum field; no location is invented here.

## 6. Actual saved warm and new FD

The new pair is:

- Warm `warm-001.json.gz`: `df6543c9b88c21bd9ea3c046f05a7c292b7d977d09c6ef431e6771560fe14689`.
- Original `driver-status.json`: `00c9e73f260d0fa239a17c3973bcbd113d813c079c04451335244e923e85be9e`.

The publisher stored the large status as `driver-status.json.gz`. A future input must decompress without JSON reserialization and verify the original status SHA above. It must not compare the compressed transport SHA with the original status identity.

FD report SHA is `a17da0a01f40a6656d2dfbbbddd83f7b0be09aebaca5cf91e5d3a8e6bfd28d20`. The original complete new-warm affine Rphi check passed with fourth-order Richardson relative error `7.169252867462084e-10`, second-order error `9.883351152852959e-6` and the unchanged threshold `5e-5`.

The report explicitly says current H is not the zero-H anchor. The true completed zero-H T112 J is held affine; no ready linear graph replaces it, and no nonlinear native solve at the new H is claimed. There is one accepted optimizer warm step, `optimization_progress=true`, while `success=false` and `new_coupled_finite_acceptance=false` remain.

## 7. Byte audit and limitations

The separate [prefix byte audit](2026-11-14-actual48-prefix-byte-audit.json) is58547 bytes, SHA256 `8c42f2f773cfa4e773be05c3aeafa5d9b8c54eadf0ed9c1f00aa1205872b3d12`. It performs no scientific evaluation, matrix action, norm or extremum computation.

Its completed scope is:

- 120 domain NPZ files and766 NPY payloads: compressed-file identities, shapes/dtypes, raw byte identities, all13 complete B/Gamma/Pi reconstructions, complete beta reconstruction and full domain model hash.
- 58 condensed NPZ files and58 NPY payloads:42 references reassembled into38 unique complete arrays with exact identity checks.
- 16 original observer reports and11 NPZ/33 original arrays, including nonfinite RHS bytes; returned residual identities and finite flags were unchanged.
- 40 unique mathematical/FD source hashes; current status and FD producer identity agree with the warm.
- The artifact's complete original parent45 file, its entire producer subtree, and its mesh/states/RHS agree bytewise with the actual B base.

The raw `condensed-root` arrays are outside that NPZ audit's scope. The memory-only complete QR factor is not an exported raw factor file and has not received an independent raw-factor byte audit. The numeric recovery values above are read from original Actions reports. The full artifact is preserved for additional specifically needed inspection, not silently replaced by this note.

The coordinator subsequently verified all14 exported raw root/affine/recovery files, totaling190956688 bytes, against the original `condensed-root/status.json` descriptors. The4735-by4735 root alone is179361800 bytes, raw SHA256 `6a244de638736fa55c4be6d81c6b2621edfe972cff777754d510a9a03a69b620`. This was byte-only verification and did not rerun a factor, action, residual or norm. See [the separate raw-root audit](2026-11-14-actual48-root-byte-audit.json), SHA256 `189fd865f1d4f0335c8fc846507797fa74c44120da04d89718649574516bfe50`. The memory-only complete QR factor remains outside this exported-file audit.

## 8. Concrete next computation

The evidence supports retaining the original complete algorithm and adding **only left-RMS482**, all2048 angles, in a new fourteen-query entry from this actual48 warm/status pair. Midpoint482 remains a distinct existing block. Both endpoints are already captured, so the complete local support stays nodes470 through483 plus global p, dimension4735. No complete Jacobian expansion or change to the frozen condensation library is needed.

The original fixed-C affine outside term, full-H alternative, lambda270, budgets, original17 trials, complete node/mid/RMS guards and actual new-warm FD remain. The larger-step left469 and midpoint483 observations remain recorded; they are not automatically appended to this minimum next modification. This is a next computation with preserved original goals, not completion of the topic.
