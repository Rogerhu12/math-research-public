# Actual run10 fixed-target radial J1845 continuation: complete source and parameter package

This implementation keeps the complete independently frozen **actual run10** target and refines the current radial SO3 approximation from $J=923$ to $J=1845$. The original reference remains $M=160$, $N=2048$, $J=923$. The current angular observation rule remains $N=2048$ and all three rotation channels remain present. This is a radial shared-quintic refinement, not an angular or frequency refinement.

The package contains **17 new complete runtime bodies**, **5 unchanged complete shared runtime bodies**, **5 complete source/parameter constructors**, three complete parameter plans, one shared complete parameter/source record, this explanation, and the delivery manifest. Every supplied body is below 100,000 bytes. The new runtime bodies total **934,734 bytes**. The shared bodies already exist in the repository and are not copied again.

The actual run10 scientific parent has not been read as a returned terminal or final in this preparation. Every future parent-report and parent-final SHA in the plans is `null`. No plan has been queued by this agent; no new field or scientific result is asserted. A real terminal or final must be consumed by its actual complete reader in the modes that request it.

## 1. Exact current input identity

The current input is the full run10 public-input freeze, not an old run09 record with a new label:

| Object | Complete identity |
|---|---|
| Public Actions run | `45972294636/1` |
| Fixed target definition | `e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049` |
| Complete reference model | `081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5` |
| Complete reference bundle | `512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b` |
| All 160 fixed chart words | `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` |
| Complete actual public binding | `4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf`, 430,908 bytes |
| Current observation carrier | `71f0048e2c6c973625fd110c6980c24242d2cf67b7dd7da5dd9e889fde26a22d` |
| Exact scalar parameter definition | `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa` |
| Original historical observation carrier | `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`, 227,202 bytes |

These identities and the complete six-file provenance come from the published run10 input producer and its full parameter/source record. The producer actually returned complete, with source `fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a`; its pure binding source is `9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209`. This preparation did not read the large carrier or 430,908-byte binding through the integration. The runtime reads and hashes those actual files fully on Actions.

The current scalar table has **2218** recorded live leaves. The **2397** leaves belong to the separately reconstructed historical carrier. A leaf count is not a target identity and is not a proof that a requested accuracy was reached. The code retains the actual accuracy boolean and complete current scalar metadata. It never substitutes the old table for the current one.

The fixed target's recorded `same_mathematical_g_claimed=False` concerns an unproved cross-run identity; it is not a proof that two mathematical targets differ. Within this new run10 radial family the entire current target, reference model, fixed chart, seed, scalar definition and node definitions are checked equal. No run09 final, root, metric value or certificate is imported.

## 2. Components shared without duplication

The following five complete published files are used with exactly their existing whole-file identities. None contains a hard-coded run09 reference model or current scalar leaf count.

| Complete shared body | Bytes | SHA256 |
|---|---:|---|
| radial_bisection_layout.py | 18923 | `cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744` |
| exact_affine_supported_reference.py | 23435 | `2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117` |
| complete_dyadic_radial_observations.py | 28167 | `2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74` |
| so3_radial_refined_public_reference_meridian_operator.py | 45749 | `130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0` |
| radial_refined_public_reference_literal_zero_moment_input.py | 35736 | `59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652` |

Their contracts are parameterized by the actual complete reference model and actual input files:

- `radial_bisection_layout.py` defines all exact symbolic nodes, current/old address conversions and the full three-channel midpoint injection.
- `exact_affine_supported_reference.py` evaluates the frozen supported seed at exact affine queries without rounding a new query into an unrelated old binary local coordinate.
- `complete_dyadic_radial_observations.py` restores the actual current scalar table, computes every required scalar query, preserves every original 7377 target word and records integral/carrier errors.
- The radial meridian base separates reference $J=923$ from current $J=1845$ and has the complete fine free layout and norm interface.
- The radial literal-Q binder retains the same 18 literal words, both supports, gamma support, full fixed seed and actual current base identities.

The source family instantiates the already published exact-affine/refinement contract in [R676](../results/R676-fixed-metric-refinement-and-complete-observation-transfer.md). It does not register another general refinement theorem.

## 3. Exact node addresses and their working carriers

Every original symbolic endpoint is an affine expression
$$
X_i=A_i S+B_i.
$$
The first coefficient multiplies $S$. The pair convention is the actual source convention; the last endpoint is $(1,0)$. The new symbolic nodes bisect these exact affine expressions, and each original node occurs at the even new index.

All original binary64 mesh words are copied to even positions. A new midpoint's binary carrier is not silently equated with the accurate midpoint, nor with the binary average of old carriers. The accurate query identity is retained independently.

For a fine cell $2i+j$, $j\in\{0,1\}$, and a literal binary64 local coordinate $u$, the exact original query is
$$
(i,(j+\operatorname{Fraction}(u))/2).
$$
The helper proves equality of the complete affine point on both descriptions. The original local coordinate is retained as a rational number. It is not rounded to a binary old-$u$ address before reference evaluation.

An original address $(i,u)$ is mapped to the appropriate child using $u\le 1/2$ or $u>1/2$. The resulting child local coordinate $2u-j$ is accepted only when its binary64 representation has exactly that rational value. The accurate affine equality is checked again. Thus an address's meaning is not inferred from similar floating-point coordinates or from an unchanged count.

## 4. Complete three-channel shared-quintic injection

The old/current physical frequency count is $M=160$, with $3M+2=482$ rotation channels. Their actual blocks are:

| Component | Half-open channel interval |
|---|---|
| x | $[0,M+1)$ |
| y | $[M+1,2(M+1))$ |
| z | $[2(M+1),3M+2)$ |

Every old node has value, first radial derivative and second radial derivative words in every channel. The full old tensor is reconstructed using its original free mask. All original node words are copied to even new nodes; core and height words are copied separately and checked byte for byte. The structural endpoint masks remain in force. All new midpoint jet slots remain free variables in the new optimization.

For an old cell of width $h$, let its endpoint jets be $(Y_0,U_0,A_0)$ and $(Y_1,U_1,A_1)$. The implemented ordinary working midpoint formulas are
$$
\begin{aligned}
Y_{1/2}&=(Y_0+Y_1)/2+(5h/32)(U_0-U_1)+(h^2/64)(A_0+A_1),\\
U_{1/2}&=(15/(8h))(Y_1-Y_0)-(7/16)(U_0+U_1)+(h/32)(A_1-A_0),\\
A_{1/2}&=(3/(2h))(U_1-U_0)-(A_0+A_1)/4.
\end{aligned}
$$
They are applied independently in all 482 channels. An exactly zero old polynomial channel is explicitly kept zero. This retains all **1,333,370** old free words and adds the full midpoint freedom, giving **2,666,582** current free variables. There is no radial subspace projection, channel deletion, mode truncation or reduced normal stage count.

With accurate coefficients and accurate widths, restriction of a degree-five Hermite polynomial to its two subintervals represents the same polynomial. The working computation uses binary width carriers and ordinary rounded operations. Its records explicitly set the accurate coefficient/error and whole working field equality claims to false. Equal original node words do not prove that the new interpolated working field, selected roots or finite objective are bitwise equal.

The fixed supported seed is evaluated from the original reference. It is not rebuilt from the new outer point or from a copied old final. Exact selected-field inclusion still requires the corresponding exact implicit branch. The new working field is always reread.

## 5. Scalar reconstruction, nonnested Gauss rules and the common-parent functional

The current complete observation plan has 3689 native legacy nodes and 14753 native total rows before the complete original aliases are adjoined. Every original 7377 complete radial row is retained in the actual plan. Old and fine Gauss nodes are not assumed to be nested; the exact material address union is formed explicitly.

The observation rule uses its original six Gauss nodes per cell. This is distinct from the retained **eight-node outer meridian integration order** and the retained eight-node seed radial quadrature. All these roles keep their own explicit source and positive weights.

The scalar reconstruction uses the actual preparation's complete definition, input identities, tolerance, admission state, leaf count, exact heap ordering, interval endpoints and complete metadata. The stopping count replaces only the elapsed-time stopping event in replay. All other metadata except elapsed time must match the actual preparation. Every original 7377 scalar target word must be reproduced before the plan can be used. New native and retained queries each record the actual integral remainder/carrier accounting; no accurately enclosed value is silently converted to an error-free centre.

Every current residual row has a strictly positive weight in the declared legacy/Gauss mixture. The current row rule, its normalization and the fully dimensioned coordinate norm change explicitly. No old norm identity is copied as the new one.

In addition to its new native objective, the driver evaluates the **original complete positive functional on the current field** using the exact 7377-row parent stage map and original positive mixture weights. It computes the current common-parent spectral/centred statistics anew from that current residual. It does not subtract an old report's Phi or treat an old field statistic as a fine-grid baseline.

## 6. Actual run10 normal, caches and derivative chain

The complete J923 scientific parent is:

| Role | SHA256 |
|---|---|
| Driver | `c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1` |
| Pure reader | `2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e` |
| Complete normal operator | `6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4` |
| Immutable root packets | `31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805` |
| Current material memory | `f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba` |

The new normal's **all 52 class methods are byte-identical** to the actual run10 normal. Only complete source constants and the new endpoint schema differ. All top-level functions and class methods of the analytic J3, analytic six-column frame, C1 frame, detached matrix, adjacent matrix, detached closure-value and immutable packet helpers are unchanged from their actual run10 parents. The packet helper adds the exact new source family to its registry.

The separate calibration body comes from the complete radial calibration: it retains the frozen J923 seed/core/height while defining the J1845 reference-coordinate initial point and its exact-affine integration. Its own new whole source is explicitly pinned. No old calibration guard is broadened.

All 32 stages, selected roots, domains, residual checks, angle jets, active upstream graphs, parameter J/J* and final original closure rereads remain. Same-call value/matrix reuse does not remove an equation or supply a root certificate. Active transforms and derivative paths retain their existing bypass rules. No cache rate, speedup, cost reduction or rounding identity is inferred by this source adaptation.

## 7. Three complete permanent radial grids and typed history

The permanent material responsibility contains the union of:

1. the true historical old-carrier grid;
2. the actual run10 original-reference grid;
3. the fine current grid;

together with the entire known explicit P0, all parent manifests and actual typed separation memory.

Historical $J=923,N=2048$ tagged locations are first interpreted under their original layout and carrier, then mapped by the exact rational address conversion. They are not reinterpreted using $J=1845$ indices. Fine same-source histories require their full current layout/model identity. All phi words remain the original angular words; this is not an N refinement.

The new memory's target validator is the complete actual run10 validator with the explicit current schema/source bindings. Its full read-carrier/P0/three-grid behaviour is retained. The geometry body from `_set_x` through EOF is byte-identical to the already complete radial geometry body: 38,112 bytes, SHA256 `3c1d3691dbb027201bd6759977ad62856d82f0f3a76615aa6dc609dfce62d8e9`.

Known protected rows, actual typed family/branch/sign/partner, discovery order and source provenance remain append-only. The working near-active row cap does not cap actual separation memory. Every current field is actually evaluated at all required old and new points. An old value, old feasibility label or old row gradient is not transported as a new value.

## 8. Actual parent and complete variable transfer

A strict parent is first captured as whole bytes and read by its actual full `2efa` reader. The parent must belong to actual `c3dc`, the current input's whole reference/carrier/scalar identities, the J923 layout and the exact original memory family. The source checker validates the entire old operator and all declared working policies before model normalization.

Normalization removes only the explicitly declared source/policy/layout/observation/calibration identities. Every other field of the full base, fixed reference/seed, scalar profile, 160-word chart, Q, bubble supports, gamma, common 32-node partition and frequency space must compare equal. The old and new Q definitions retain their own coordinate-layout initial-point hashes; these are related by a separately checked complete initial-point inclusion, not by relabelling one hash.

For an explicit old final, the code reads all 13 original NPZ members, reconstructs the complete old free vector, checks old report/checkpoint/model/free-point identities, applies the full three-channel shared-quintic injection, and checks the current vector and all copied original words. The original seed and base.initial remain frozen. The current metric, geometry, roots, norm and common-parent statistic are then read on the new point.

Every actual inbound history is followed recursively. Parent addresses are walked with the original layout before exact transfer. Typed rows are appended without a cap and retain the original discovery provenance. Same-source restart uses its full actual new model identity.

The historical run07/run08/run09 source registry remains literal and separate. Those families do not satisfy this run10 strict terminal/final qualification simply because their names or chart summaries resemble the current target. Unknown peer reports remain unpaid source-bound history obligations; a new branch name does not make that history empty.

## 9. The three parameter plans

All plans preserve the actual run10 scientific arguments, including $M160$, $N2048$, outer order 8, 32 stages, full integration, original root tolerances/backtracking/domain, full geometry/Phase I policy, budgets and solver parameters. The new explicit layout argument is `--current-radial-factor 2`.

| Mode | Meaning | Scientific/pure words | Future report/final SHA |
|---|---|---:|---|
| independent | Original fixed reference point embedded in the full fine layout; explicitly declares unread run10 and old peer obligations | 155 / 7 | null / null |
| terminal | Complete actual J923 terminal and its entire history; original frozen reference remains the variable seed | 140 / 7 | null / null |
| final | Same actual terminal/history plus the actual complete 13-member final used only for full variable injection | 144 / 7 | null / null |

The terminal and final input paths refer to `{work}/run10-detached-closure-values-first/report.json` and, only for final mode, its `final.npz`. These paths are parameter requirements, not claims that those files have returned. A failure before any report does not become a terminal report. The pure step uses the actual fixed reference as its existing controller parent, so it can report a real initial-field failure without requiring a nonexistent final.

Every plan retains all **373** run10 science selectors, all **357** run10 pure selectors and all **43** progress selectors. Radial fields add 24 science and 16 pure selectors: totals **397 / 373**, respectively. The nine former run09 summary labels are mapped to the actual run10 labels with identical selector paths; no field is removed.

The complete source/parameter metadata is in a separate 45,124-byte record solely to keep each complete ready below the file-size ceiling. Each ready still contains both whole steps, all arguments, outputs, summary mappings, progress mappings and row-only cleanup patterns. The shared record stores every remaining common field and all three mode-specific records. The supplied constructor verifies reconstruction of every field of each unsplit full plan. This is a lossless split, not a shortened parameter set.

The run07 API observation at 05:02:15 UTC recorded a cancelled workflow; it is not a known scientific child termination time. The source-bound missing step4 history remains unknown, not empty. The plans make no workflow-liveness assertion about other unread peers.

## 10. Pure report and failure interfaces

The new source binding reads actual analytic J3, analytic-frame and detached-closure diagnostics at each record's **own** point. Its return includes both the closure summary and the original `radial_refinement` summary. A draft merge initially omitted that radial return key; it was corrected before final delivery, with every dependent source pin rebuilt. The unused draft blobs remain preserved and are not final sources.

The pure reader retains 26 of its original 28 top-level functions byte for byte. Only the complete C1 policy extraction and `read_report` wiring change. It keeps all radial input, common-parent, target, Q, exact reference, geometry, Phase I, typed row and final-bundle guards. ROOT_SNAPSHOT_KEYS exactly agrees with the driver and includes the actual closure diagnostic.

The final scientific solver suffix differs from the already complete radial suffix only by six read-only progress observations around the initial residual/statistics/geometry calls. Removing those six lines restores the entire old 20,488-byte suffix exactly. All numerical calls, both packet hooks, all line-search candidates and checks remain.

Progress is a mutable scalar observation. It is not a terminal report, immutable packet or continuous certificate. A partial cache, initial read error, failed candidate or missing field remains explicitly partial. No missing field is filled with zero or copied from another point.

## 11. Complete new runtime inventory

| New full body | Bytes | SHA256 |
|---|---:|---|
| run10_radial_detached_closure_values.py | 54138 | `61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb` |
| run10_radial_analytic_stage_jacobian.py | 25720 | `7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b` |
| run10_radial_analytic_normal_frame.py | 47267 | `945b66100801058d311f215c9453efa35a9cbb3edf031dc1b10da0140f9567f2` |
| run10_radial_normal_frame_c1.py | 37361 | `976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2` |
| run10_radial_detached_stage_matrices.py | 47791 | `404ecb970b37b37fd00863c52564ac1ec784c902d7f5123cc5317d77976336c9` |
| run10_radial_adjacent_normal_matrices.py | 36766 | `7477da02b225834cc1f0dae147d0bca53a3b40398ee04cdf0dfc7f0217483a37` |
| run10_radial_reference_calibration.py | 12769 | `cb440bfe32830f5a479e466fec8439e9bde88bfbb4160e534f899f999bac573b` |
| so3_run10_radial_refined_closure_normal_lift.py | 98434 | `ffbbddc9047b36cd308ed79df7ad4669185f61e71d85caef9a14f37b8292a40c` |
| immutable_run10_radial_normal_root_packets.py | 71652 | `fa9f50d318af9ec268ce391b6ba16d8eb971d88ad519ae79c8ba3c661806f528` |
| run10_radial_material_address_transfer.py | 22097 | `e27e2f333e2a24279af84d6e015835420355b2fb446dbd56b99e99e68d40374b` |
| run10_radial_refined_material_memory.py | 59245 | `043d451e34890c522de17be687306898f2f18ec8451d1814ab75730eea687071` |
| run10_radial_source_and_report_binding.py | 48958 | `7536c4b1fb9085fe03a00be5da4073065b7abb98a3b2ee7b3d14833c478af415` |
| transfer_run10_radial_refined_material_memory.py | 87074 | `8cd8a25830518bc29f80b22dc26e1f611e145566a7cd5fd0bf8e4f758304bb3b` |
| so3_run10_radial_refined_envelope_geometry.py | 71804 | `a55a42c8d577dd4589425680c4a37eeb8e17d80de09a02215b3f424245c7f8e9` |
| fullclosed_run10_radial_refined_so3_qp.py | 93101 | `2693abdb070cb62584abb3ffceeb525854c62d47379c9349d9047a0a365fe4e5` |
| launch_run10_radial_refined_actions.py | 22614 | `b71588c0323c96970abedbe1b495429295f4bd44de01b921486123b6cfbf861e` |
| read_run10_radial_refined_so3_report.py | 97943 | `64e92ed8b48f753e9988221c2c1f91513ed2e468e6fff3ce9cc83096c4bad8e4` |

The driver declares **96 complete source roles**. The registry retains the full current run10 dependency paths, the required original radial sources and the literal historical parent sources. Every new runtime path is paired with its actual whole new SHA. Current and historical identities are not silently renamed.

## 12. Complete reconstruction and parameters

| Complete constructor | Bytes | SHA256 |
|---|---:|---|
| derive_run10_radial_lower.mjs | 12518 | `0d0a6c1c8e0ed57946d0dbaa121e08043a7aca9e3f993c4964ebf6430bb7f832` |
| derive_run10_radial_memory_binding.mjs | 38150 | `38aec843677331a5c358ab770127b5d09a9278b3aceae22dd8b80c354c2f6f34` |
| derive_run10_radial_upper.mjs | 60273 | `9143c2e1c1375af87ca988e0ad05dc746a1b77820e9db9450fb9235412da3ccd` |
| reproduce_run10_radial_sources.mjs | 29106 | `44d47d29606563ec8489d6873e6b7a77a02b783878d5d9d29736303531205864` |
| make_run10_radial_ready.mjs | 44333 | `dd7d5d758eadbde4c9d2d8b15532add84cf34303eb9e8a371f5e4dff71f96e40` |

The three source modules carry the complete original-parent identity, every literal replacement and exact occurrence count, plus each complete output identity. They independently produce full source files; no wrapper substitutes a small patch for the scientific body.

The full replay command is source-only:
```bash
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_run10_radial_sources.mjs --repo REPOSITORY --out SCRATCH_OUTPUT
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/make_run10_radial_ready.mjs --repo REPOSITORY --out SCRATCH_PLANS
```
Both refuse repository output directories. The replay checks each whole construction parent, all generated outputs, all five shared bodies, all 96 runtime roles, the 52 unchanged normal methods, complete geometry suffix, complete scientific suffix after the six declared observations, and driver/launcher argument equality. `--verify-existing` compares complete existing scratch outputs. It imports no Python scientific module and does not call F, J, a root, quadrature or a numerical fixture.

| Complete parameter artifact | Bytes | SHA256 |
|---|---:|---|
| run10-radial-J1845-complete-parameter-and-source-provenance.json | 45124 | `cbd2e79f1a9acf79b30555239a2374ada58523255335c336e69c31e2796e4530` |
| run10-radial-J1845-closure-values-independent-ready.json | 91930 | `f66c82940a6447e6e38fd2607d650cfc6059435c305f2fb65b1992a75829b3f7` |
| run10-radial-J1845-closure-values-terminal-ready.json | 91328 | `b20b07de7d967e8b588d42dbf15bdbbdb0b9d0b5797d5a06cf94d0f13570bda2` |
| run10-radial-J1845-closure-values-final-ready.json | 91520 | `63da403d8ef2f8ca20c3645182256e96905bfd33b305db76d803634b2e26ab3d` |

The construction-stage actual checks were V8 string/JSON/hash operations: all 17 complete sources were replayed from their stored complete parents; the three generated derivation modules were themselves evaluated with the pure hash adapter and reproduced all bodies; the parameter constructor reconstructed the entire shared provenance and all three ready files byte for byte. The five JavaScript constructors passed V8 syntax construction after import/entry stripping. **No Node CLI, Python AST/compile, scientific import or mathematical computation was run in this preparation.** The runtime/reproducer validation described above is supplied code, not a claim that an unavailable executor ran it.

## 13. Scope and remaining scientific responsibility

This package is ready as complete source and parameters. It does not claim a successful fine-grid field. Its first actual setup must still restore the same scalar input, compute all native/retained queries and pass the original-word checks. Its first field must still solve all selected normal equations and read all actual Gram/geometry rows. A complete parent final is used only when it truly exists and passes the full parent reader and 13-member reconstruction.

The new source keeps every mathematical variable and required address. It does not pay accurate midpoint-coefficient rounding, root-branch uniqueness, the complete quadrature/AD error, continuous Gram/reach, convergence, speed or task-completion debts by changing the representation. The ordinary working injection and new quadrature/calibration are explicitly different numerical definitions whose errors remain reported as unproved.

No already published run09/run10 runtime, parameter, proof, queue or ref was edited by this agent. All new complete bodies and the full source/parameter construction records are protected as separate unreferenced Git blobs for root's review and ordinary publication.

## 14. Final-checkpoint path correction before execution

Root's source review identified that the original final-mode parameter draft named `final-new-field.npz`, while the complete actual parent driver `c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1` writes `final = args.outdir/'final.npz'` and passes that path to `q.save`. The corrected full plan therefore uses `{work}/run10-detached-closure-values-first/final.npz`. This correction does not claim that a parent checkpoint has returned; its actual report and final hashes remain null.

The parameter constructor changes exactly that filename literal. Its complete V8 construction was then evaluated against the same three complete original parameter inputs, producing all four complete parameter artifacts. The independent and terminal step objects are unchanged; their shared-provenance pointers change. The final step changes only science argument 143, following `--material-envelope-seed-checkpoint`, plus the matching final-path metadata and provenance pointer. All numerical arguments, scientific and pure summary selectors, budgets, outputs, cleanup instructions and remaining arguments are unchanged. All 17 new runtime bodies, five shared runtime bodies and the other four source constructors retain their prior whole-file identities. The earlier complete draft files remain recoverable by their original Git blobs in the delivery manifest; they are not treated as an executed numerical experiment.
