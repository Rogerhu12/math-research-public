# Actual request45: complete local Schur QP gives a large model decrease; original midpoint482 limits the nonlinear step

## Actual run and preserved input

[Public Actions run 43627827085](https://github.com/Rogerhu12/math-research-public/actions/runs/43627827085), job `132547603012`, used source `3689913753612b02021e439082eaf1c166091183` and the independent condensed-QP workflow. The warm computation, actual new-warm boundary derivative check, artifact upload, and publisher all completed successfully.

The complete artifact is `14126039433`, named `visible-followup-condensedqp-43627827085-1`, 319,064,633 bytes. Its ZIP SHA256 is `a08478e30648b6f08f2d2d8716a891d8d128913f15d6b616505e6c99d253f876`. The unique downloader verified that ZIP before the readback below; the local completion marker has the same digest.

The parent is the actual request42 saved warm, SHA256 `3dd623e90edb97ff113bebddd09445d64b916626a8fb1821fd35e69beabdc317`, paired with status SHA256 `26272c6ca8e1a5ba1db2bb96cc749dca74cddc025bcd1a5a9864f149d4a16d04`. This is a new fixed optimization model at that parent, with freshly constructed weights. It must not be identified with request42's earlier model at the request40 parent.

The experiment used the same complete 699-node field, 112 physical modes, 112 native height modes, all core and scalar columns, and the unchanged physical-angle boundary residual. Its scalar and chart conventions are those of the [frozen interface](2026-11-14-complete-condensed-QP-warm-interface.md). No nonlinear native tail or accepted BVP was computed by this warm experiment.

The four new frozen numerical sources are:

| Source | SHA256 |
| --- | --- |
| `geometry_20261114_condensed_projection_warm.py` | `5d398d3d702e0fd93af3777504fc1d4e918110c7e5f0683601eac5d21c49914a` |
| `geometry_20261114_condensed_local_inequality_qp.py` | `ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173` |
| `root_20261114_complete_local_qp_condensation.py` | `84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b` |
| `geometry_20261114_condensed_projection_response.py` | `461b0d48068dba6cfcb62974c1e8f16889b1bd8ca5bd4b86e1bf6a3e09ac83b8` |

## One complete model and the exact-algebra scope

The actual live binding records one original `CompleteLinearization`, with original A of shape 236036 by 236036 and damping270. The original 24,576 inequality rows are the complete 2048-angle grids of nine left-RMS queries and the original collocation midpoints473,475,477.

The B model SHA256 is `e89ac9573ea48e0731a2ea7a72b0561c1245f30c02db1a9867dbcc0aba98051b`. Its complete local support consists of physical nodes470–482 and all three scalar controls, hence 4397 coordinates. The retained C candidate still restricts its local correction to nodes471–482 plus the controls and includes the complete outside offset. That C support does not restrict the new complete-H candidate.

The condensation uses [R270](../results/R270-exact-local-support-damped-QP-condensation.md): it keeps the original linear term from A-transpose times b, all pure-global rows, the full affine column, and the conditional optimal response of the outside variables. It does not zero the outside physical variables or discard the 109 free core variables.

The saved condensation report is complete. It records 216 reverse fronts, local QR dimension4397, 256 local inverse actions, and one final complete-chain recovery. The condensation elapsed time is 9.433830195999974 seconds; the local QP elapsed time is 39.72685857099998 seconds; the full helper time including factorization, condensation, QP, and recovery is 74.931920273 seconds.

The saved rounded local-root diagonal absolute values range from 270.00009206666306 to 1072.1431619881662. These are readouts of the finite root, not a proof that the rounded root is exactly the original full H. The actual model identity is `c481fea04b9156c4fa3b0bf2031bc8e23dde600618079e4a1309cbacf4ce5510`. A separate `factor_input_identity` field is null; its serialized-value hash must not be advertised as a unique non-null model identity. The actual individual factor/input identities and original-operator readback remain the relevant evidence. The saved original affine-column reconstruction error has L2 norm2.305050247518968e-10, against saved original-g L2 norm992704.1285587724; a computed approximate center did not replace the original linear term. The single complete recovery has original H residual L2 norm5.833733171728455e-10 and relative residual5.876648878182257e-16. Its recovered-local mismatch L2 is2.4061275080745594e-17 and Linf7.474218726571946e-18; the outside-gradient L2 is5.833730236243862e-10. The same-vector supplied/reference A and AT differences are both recorded as0. These are original Actions readouts, not new local evaluations.

## Local QP and comparison with the retained C candidate

The local working-row loop stopped at its declared 256-row budget. It did not stop because of the 600-second discretionary budget. The last saved stage is255. The last added row19543 is the midpoint473 row at original physical angle index1111.

At this last working-row solve:

| Saved readout | Value |
| --- | ---: |
| Completed dual sweeps | 200 |
| Largest final coordinate update | 8.326672684688674e-16 |
| Minimum normalized working slack | -4.3021142204224816e-16 |
| Working Gram asymmetry Linf | 4.107825191113079e-15 |
| Local unrepaired stationarity L2 | 1.3734365449214752e-11 |
| Minimum original unrepaired slack | -7.582823258189819e-14 |
| Negative original slack entries | 216 of24576 |
| Maximum relative original violation | 1.026487695238561e-12 |

The remaining negative stored slacks are at floating-point scale. The local all-row radial repair factor is 0.9999999999989437. After this repair the saved all-row minimum is 8.743006318923108e-16, with no negative entries. The final local feasible-segment selection has parameter1; its subsequent local repair factor is1.

This differs materially from the substantial internal shrink in request42, established by the [request46 readback](2026-11-14-actual-request46-request42-working-row-and-radial-readback.md). It is not a comparison of objective values between different fixed models.

The actual full conditional recovery then required a very small original global feasibility repair, factor0.9999999999971445. That repair and the final rounded segment composition are still recorded as changes to the recovered full vector. Accordingly, the producer does not claim that the finally selected rounded vector is the exact conditional minimizer at its local coordinates.

The original complete operators were applied to the recovered and selected full vectors. Within this one request45 model, the comparison is:

| Quantity | Retained C candidate | Selected condensed-H candidate |
| --- | ---: | ---: |
| Original damped objective | 44.27688711321688 | 43.85821639765896 |
| Original directional derivative | -0.0019093173662909435 | -0.8324574348819488 |
| Original model decrease | 0.0019061657701548887 | 0.42057688132810617 |
| Minimum complete linear slack | 8.604228440844963e-16 | 8.326672684688674e-16 |

The selected full direction SHA256 is `f4f32905ef504b921c34dfac0a3ade1b1ef800109e92d2a4e30a83d330f2b448`. All 24,576 supplied linear slacks were recomputed and are nonnegative. The actual full A/AT/B/BT stationarity L2, with the saved nonnegative dual, is 2.835179534553232e-6. Its complementarity sum is 3.393474242905913e-14.

The best R267 raw floating lower-bound value is43.85821639765893 and the reported final cross-point gap is2.842170943040401e-14. These strong finite diagnostics do not constitute an outward-rounded lower bound, exact full-QP optimality proof, or a BVP acceptance. The original all-domain nonlinear line search is still essential.

## The actual nonlinear trials

The original model starts with fixed-weight merit44.278793278987024. The selected full direction is tested at the original dyadic trial factors. No line-search count or acceptance tolerance was changed.

| Alpha | Original bad midpoint indices | Outcome |
| ---: | --- | --- |
| 1 | 473,475,477,480,481,482,483 | Original midpoint domain rejects |
| 1/2 | 473,475,477,481 | Original midpoint domain rejects |
| 1/4 | 482 | Original midpoint domain rejects |
| 1/8 | 482 | Original midpoint domain rejects |
| 1/16 | 482 | Original midpoint domain rejects |
| 1/32 | none | Original full trial and both RMS checks accept the warm step |

All six trials have valid original nodal domains, positive original uniform-phi rho guard, and finite boundary readout. The first five fail at the original midpoint domain before a finite full merit is reported. They are not finite-merit Armijo rejections.

For each of the three nearest rejected trials, every one of the twelve currently constrained query grids is actually positive. The extra obstruction is the **unconstrained original collocation midpoint482**:

| Alpha | Original midpoint482 minimum beta-squared | Original worst angle index | Negative sampled angles |
| ---: | ---: | ---: | ---: |
| 1/4 | -0.03797483974847915 | 980 | 4 |
| 1/8 | -0.030651700636741497 | 1004 | 8 |
| 1/16 | -0.08309044083909534 | 1014 | 16 |

These beta-squared values, angle labels, and counts are copied from the unchanged original midpoint observer. The observer consumes the already returned original midpoint state and RHS; it did not call the whole flow or construct another Jacobian. The dependence is visibly not monotone across these three alpha values, so no monotonicity of nonlinear margin along the direction is inferred.

At alpha1 the currently constrained grids also have nonlinear violations, despite the direction satisfying all their linearized inequalities. This is further direct evidence that linear feasibility cannot replace the original nonlinear domain checks.

The accepted alpha1/32 trial has:

| Saved quantity | Value |
| --- | ---: |
| Fixed-weight merit after trial | 44.252846552483554 |
| Actual merit reduction | 0.025946726503470074 |
| Predicted unregularized reduction | 0.025840864357267547 |
| Actual/predicted ratio | 1.0040966952474542 |
| Raw physical collocation maximum before | 0.007110297531831894 |
| Raw physical collocation maximum after | 0.007110255988772191 |
| Complete boundary maximum after | 7.686280188372218e-8 |
| Original uniform-phi rho minimum | 0.16604058243274977 |
| Left and constant-coordinate residual maxima | 0 |

All699 original node and698 original midpoint queries pass. Both original RMS sets, each with698 query points, also pass. The weighted merit and raw maximum collocation residual are different readouts; the small change in the raw maximum must not be misreported as a similarly large reduction. Its worst component/location is not saved in these scalar summaries and is not guessed.

## Saved warm and actual new-warm FD

The complete unaccepted saved warm is:

- `warm-001.json.gz`, SHA256 `8ce98e5b325eae8188f8b4c707d1abfaa109e50a790c9abe5850ef1a52d08b75`;
- paired `driver-status.json`, SHA256 `70be19b675c9f558cddbfa9532777a119a7bbe0629f505368e1588842aade30d`;
- actual new-warm `physical-response/response-check.json`, SHA256 `488dc5cac648c6ebe5551e1900be32750cc0619d5afbf4cd35ffd1bb2d45bcaf`.

The actual FD report is bound to this new warm and the original true T112 zero-height Jacobian/configuration. Its Richardson relative error is7.091595199583649e-10; its second-order relative error is9.883361120354762e-6; the unchanged implementation threshold is5e-5. The original derivative check passed. No old FD pass was relabelled, and no ready linear graph replaced the actual zero-height Jacobian.

The driver records one accepted **optimization warm step**, `optimization_progress: true`, `success: false`, and `new_coupled_finite_acceptance: false`. The warm driver elapsed time is340.01251992699997 seconds. The new-height nonlinear native tail, final coupled BVP, whole closed surface, and held-amplitude criteria are still unproved and unaccepted.

## Independent byte readback completed here

The readback used JSON parsing, streaming SHA256, ZIP/NPY header parsing, and raw-byte concatenation only. It did not recompute a matrix action, norm, extremum, ODE, FD, or optimizer.

The detailed small audit is [actual45 prefix byte audit](2026-11-14-actual45-prefix-byte-audit.json), 45,550 bytes, SHA256 `25d93108f4cb99416f610cd53e0aa316b74457778f09237384046ff2c813ae74`. It establishes:

- all111 domain NPZ files and708 contained NPY arrays match their saved compressed-file and raw-array hashes, shapes, and dtypes;
- all twelve complete B/Gamma/Pi grids and the full beta vector match their hashes when the actual chunk bytes are reassembled in the saved order;
- all58 condensed NPZ files and58 contained arrays match their identities;42 complete-array references reconstruct38 unique complete arrays with the expected original hashes;
- eight observer reports and14 observer NPZ files,42 arrays in total, preserve the original state/RHS/beta bytes, including nonfinite RHS bit patterns;
- all recorded observer “returned flags unchanged” and “residual bytes unchanged” checks remain true, with no additional whole-flow or Jacobian evaluation;
-38 current source SHA bindings agree with the frozen repository files;
- the new status identity and FD producer agree with the saved warm's complete producer, and the actual saved warm hash agrees with both status and FD.

The original A construction reports88 Jacobian calls. Only its existing calls59 and61 supplied the captured domain endpoint blocks; the retained B data contains13 endpoint nodes and13 variants. No second complete Jacobian was constructed. The actual full-angle adjoint error is1.304514891263702e-17, local/full action difference0, and maximum original complex-chain relative error1.2358122648687521e-12. These last numerical values are read from the original Actions checks, not recomputed during byte readback.

The separate independent physical collocation complex check has relative error8.673617379884035e-19. Its explicitly saved direction scope is **free inlet core and global controls only, with interior physical direction zero**. It is not described as a check of all interior physical directions.

The full parent42 file was not reloaded in this byte-audit pass; its complete original hash binding and retained producer chain are recorded rather than falsely labelled as a second parent-file audit. Root separately verified all14 exported raw files in the condensed-root directory, totaling166,244,832 bytes, including the154,668,872-byte local root with raw SHA256 `9f1bd271e057f47558ff141d7bd5551560456abfbb2bf1c53474505cfc41fbe3`. Every saved size and raw SHA matched. The separate [root-array audit](2026-11-14-actual45-root-byte-audit.json) is4290 bytes with SHA256 `460c9521a5a8f1ef97ea96369fa8cd40c529174ddbfcb0fd9f346b947c9e2001`. This complements the58 NPZ audit above; the two scopes were not conflated. The factor's full raw arrays were not exported, so their recorded hashes are not a substitute for independent factor-byte inspection.

## Concrete continuation supported by these data

Continue from the actual request45 saved warm and paired status. Preserve the existing twelve complete query grids and add only the observed original collocation midpoint482, with all2048 original physical angles.

That makes thirteen query grids and26,624 inequality rows. Its full local support extends to node483, giving physical nodes470–483 plus the three scalar controls, hence4735 local coordinates. The new node's original J/P block is available in the same original A construction; it does not require a second complete Jacobian.

The existing R270 library is dynamic in this contiguous local support. The new entry must keep the entire original affine recovery, including the outside variables, and must explicitly distinguish its thirteen-query identity from the frozen twelve-query producer. If the baseline C support stays at nodes471–482, its new outside contribution from node483 must remain in the affine offset.

This continuation retains damping270, the256-row local work budget,200 dual sweeps, the original17-trial limit, all original domain/merit/RMS checks, the unchanged FD gate, and the complete parent/source chain. It does not add further query locations merely because they failed at much larger trial factors, and it does not imply that the next field will be accepted by the complete BVP.
