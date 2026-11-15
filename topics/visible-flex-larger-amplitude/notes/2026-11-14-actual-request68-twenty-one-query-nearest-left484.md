# Actual request68: the21-query warm accepts1/8; the nearest rejection is left-RMS484

Classification: actual computational result and provenance readback, not a full BVP acceptance or an exact existence certificate.

Author: amplitude. Root retrieved the five published original files through the command line. This note reads those original results and checks their bytes and producer identities; it performs no new scientific computation.

## 1. Observed result

The actual21-query, lambda270 run accepted one decreased optimization warm at step1/8. The subsequent original complete affine Rphi derivative test passed. The next larger tried step,1/4, had finite original nodes and midpoints, passed every one of the21 modeled angular queries, and decreased the actual fixed-weight merit. Its complete original RMS check nevertheless rejected one unmodeled query: **left-RMS484**. The right RMS family had no failures.

This is an accepted optimization step only. Both saved `success` and `new_coupled_finite_acceptance` remain false. The run did not solve the nonlinear native tail at the new height, accept the full coupled BVP, or construct a closed Cartesian surface.

The same-model merit decreased from43.75526502490638 to43.704499218930515. The original report records actual reduction0.050765805975864, predicted unregularized reduction0.055037214881811854, and ratio0.9223905331125426. These values use this run's newly frozen row weights. They must not be subtracted from a prior round's differently weighted merit to claim a cross-round improvement.

The original primary records are preserved in [the compact actual readout](2026-11-14-actual68-original-readout.json) and [the parent/report/source byte identity readback](2026-11-14-actual68-primary-identity-readback.json). The latter records the local scope precisely; the complete artifact array audit is separate.

## 2. Actual execution and source

- Public run: [43653811809](https://github.com/Rogerhu12/math-research-public/actions/runs/43653811809).
- Scientific job:132627870737. Warm, original FD, artifact preservation, and ordinary publication all completed successfully.
- Source commit: `9ad4c5d56a85ba952d6e9a538c49fbd3aae4fa14`.
- Artifact:14137921466, `visible-followup-condensedqp-43653811809-1`,590574983 bytes.
- Artifact API digest: `0fe545ea42c48bb2d5551afddb86190af3c7ff1a14509b9f1ed5a6e5d0e53784`.
- Artifact uploaded2026-11-14 at23:47:18 UTC.
- Public result directory: `notes/public-actions-43653811809-1-condensedqp/`.
- Warm algorithm elapsed737.791910502 seconds. The original response check took24.641922154999975 seconds.

The digest above is the recorded complete artifact identity. This first result readback did not independently download or hash that590MB ZIP. Root instead fetched the actual original model, status, QP summary, FD, and new warm. The status and FD were transparently decompressed into their original JSON bytes, without JSON reserialization.

The original trial model is636538 bytes, SHA256 `46a2d12e0589590935cdd41e355402e7dd47c98bfbcfd9ec8794af61fe4eda18`. The original QP summary is103148 bytes, SHA256 `67a63d37831e1f473c94fc5f0b03dad8651f1b2969aee5988efccc6f6ceeab36`. Both were read locally from the command-line retrieval, not by transferring a large report through the text connector.

## 3. What this run changed

The parent is the actual66 decreased twenty-query warm, SHA256 `80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6`, paired with original status SHA256 `04ace7953961b3905d2b72639976025dc9c4efd0bef7b932585cf21f8249bcd4`. The whole parent producer subtree is retained. The699-node mesh and all M112/T112 modes remain unchanged.

Request68 added only the full2048-angle **left-RMS466** query identified by request66's nearest failed trial. Its typed model has14 left-RMS queries and7 original collocation-midpoint queries:

- Left RMS:466,467,468,469,470,471,472,473,475,477,479,480,481,482, at the original fraction0.17267316464601146.
- Original midpoint:473,475,477,480,481,482,485, using the original saved midpoint state and station, not a separately interpolated RMS point.

Thus B has43008 rows and236036 complete coordinates. Its declared contiguous local coordinates are nodes466 through486 plus all3 global controls, dimension7101. Its actual block-column union is6763: node484 is an explicit zero-B layout block in this run. That node remains a full-H unknown with its complete couplings. No query or extra Jacobian capture was added for it merely to satisfy the contiguous condensation layout.

The original baseline C correction still uses only nodes471 through482 plus the3 controls, dimension4059, with the full outside affine offset retained. This restricted baseline support does not restrict the complete-H candidate or freeze its exterior variables. The global radial operation and complete selector act on the complete recovered vector.

The damping270,512 local working-row budget,200 dual sweeps,200 original LSMR iterations,200 baseline projection sweeps, original17 nonlinear trial levels,1200-second total budget,600-second candidate budget,90-second trial reserve,30-second recovery reserve, and all original numerical gates were retained.

## 4. Every original trial and the nearest failure

| Tried step | Original node failures | Original midpoint failures | Modeled angular-query result | Complete original RMS result | Actual merit result |
| --- | ---: | --- | --- | --- | --- |
|1 |0 |475,477,481,484,485,486 |All14 left queries and midpoints475,477,481,485 fail |Not reached |No finite full merit recorded |
|1/2 |0 |482,484,486 |Left466, left480, midpoint482 fail |Not reached |No finite full merit recorded |
|1/4 |0 |None |All21 pass |Exactly left484 fails; right family0 failures |43.6627283325061; decrease0.09253669240028017, rejected by original RMS domain |
|1/8 |0 |None |All21 pass |Both698-point RMS families pass |43.704499218930515; accepted decreased warm |

All original trials retained a valid4096-point uniform-phi core-density guard, with reported minimum0.16604058243274977. Their boundary residuals were finite. The original core rows and control rows remained exactly constant across nodes, and the exact-coordinate inlet residual was0. No midpoint/RMS failure was hidden by a selected-query pass.

At the nearest rejected1/4 step, the original complete RMS report records:

| Original field | Stored value |
| --- | ---: |
| Failed family and interval |left-RMS484 |
| Left endpoint |1.2392225749879933 |
| Right endpoint |1.2442070264877532 |
| Query station |1.2400832560024813 |
| Minimum beta squared |−0.04104689346427315 |
| Phi at the minimum |0 |
| Scalar radius |1.182103968045735 |
| Returned scalar first derivative |−0.24631188347455873 |
| Returned scalar second derivative |−2.422976547631053 |
| Curve curvature at the minimum |0.20421824691590268 |

The actual1/4 merit reduction was0.09253669240028017 versus the original prediction0.10763823458416243, ratio0.8597009488103937. It was an actual descent direction at that step, but it failed the original full domain test. Its physical collocation maximum was0.0071088137089857315 and its boundary maximum2.241243989718959e−8; neither replaces the failed RMS condition.

The farther1/2 trial also fails already-modeled left466, left480, and midpoint482. Its unmodeled midpoint484 is therefore not evidence that midpoint484 alone causes all rejected steps. In particular, this run does not justify adding that farther midpoint together with the distinct nearest left-RMS484 query. The compact readout retains every selected query's stored minimum, angle index, and negative/nonfinite counts, as well as every bad original midpoint and its raw-array identity reference.

## 5. Original physical residual and fixed row weights

The existing read-only observer locates the full physical collocation maximum at the same original row before and after the accepted step:

- Interval461, endpoints1.139533544992796 and1.1445179964925558.
- Original midpoint station1.1420257707426757.
- Radial component1, mode1, cosine frequency2.
- Complete physical residual row155819.
- Original signed value before:−0.007109134582008451.
- Original signed value after the accepted1/8 step:−0.007108973872610448.
- This model's original frozen row weight:199.05060973500673.
- Full weight-array identity: `ae83aa163850620927fdb03a43c5c6f17c6fcc1b84e8f47621c74ca6d47b0766`.

The weight is the original returned value of `1/(h_j*(1+abs(base_fm_jk)))`, fixed from the current base evaluation. It was not rebuilt from each trial's midpoint RHS. This row lies outside the local B support, but remains in the complete original A, full gradient, and full-H conditional response. Its slow change is not evidence of a zero weight or omitted equation; it also cannot be attributed uniquely to damping from this result alone.

The accepted step has complete boundary maximum2.614784483226259e−8 and constant-row collocation maximum0. The original after-selection directional diagnostic also ran its three saved real perturbation levels with the same weights. It reported finite evaluations and merit slopes−0.45004248313773587,−0.4500424567766004, and−0.4500424128650593. Its reported relative weighted-vector differences are0.00010648386650573337,0.00025883438759533766, and0.00023016479352469532. These are existing read-only diagnostics, not a new acceptance threshold and not a claim that every nonlinear Jacobian column was independently verified.

## 6. Complete-H candidate, repairs, and bounded local QP

The original same-model comparison retained both the baseline C candidate and the R270 condensed candidate. Their recorded objectives are:

| Candidate | Original complete damped-model objective |
| --- | ---: |
| Baseline C |43.75482112347814 |
| Selected R270 complete-H candidate |43.524676836119276 |

The complete-H candidate's actual original directional derivative is−0.45004249977234; its reported damped-model decrease is0.23058818878710202. The original weighted action squared is0.15591649148552264 and damping penalty0.28299213048495336. The scaled direction norm is0.001970259431870466; the actual coefficient-direction maximum is0.00014514922579697757.

The candidate's final whole-vector radial factor is0.9999999999875665, followed by segment parameter1 and no further composed repair. All43008 actual final linear slacks are finite and nonnegative; the reported minimum is9.159339953157541e−16. This was not the severely shrunken baseline C direction: that baseline's projected-candidate radial factor was0.001600539213204215. The recovered complete-H vector is rechecked against the original A, AT, B, and BT after the selector.

The local solver stopped at the unchanged512 working-row budget. The final unrepaired local stage had448 negative slacks, minimum−1.7608137170554983e−13, and4 exact stored zeros. Its maximum relative violation was2.271523957271902e−12. The worst relative row was26624, typed left-RMS482 at angle0, whose stored slack was−1.6930901125533637e−15. The local stationarity norm was3.351590591931631e−11. The report does not claim a certified exact local optimum.

After the original complete recovery and selector, the stored original full stationarity norm is4.650449587614451e−6 and complementarity sum1.5376846733718216e−13. The R267 floating-point lower-bound readout is43.52467683611912, with cross-point gap1.5631940186722204e−13 and distance readout2.070893075653107e−9. These are ordinary floating-point posterior diagnostics, not validated enclosures or additional BVP acceptance gates.

The complete-H helper took344.174572018 seconds, including factorization, condensation, QP, and recovery; the local QP report records286.252800305 seconds. No local numerical action was performed to reproduce any of these quantities.

## 7. Actual original model and recovery checks

The reported B model identity is `7e5512fa872b45e87fd88e5a2a0c4857ab8881fef8a2e47b3d78b77075486bcc`. The existing Actions implementation checks report:

- Normwise adjoint error3.1699487119213972e−18.
- Local-versus-complete action error0.
- Maximum original complex-chain relative error1.0763976181157966e−12, including the actual supplied LSMR direction.
- All original implementation thresholds passed unchanged.

The separately stored original-A nonlinear collocation complex check has relative error8.673617379884035e−19. Its actual scope is all free inlet-core and global-control directions with interior physical coordinates zero. It must not be described as an independent nonlinear check of every interior physical direction.

The condensation identity is `2285d1fbb40525691b29f09963894ef726b995f94d5c8c7d373ebe7f457c99b4`. It retained the complete original gradient and affine column, performed212 reverse fronts, made512 local-H solves, and requested one complete-chain recovery. Its local dimension is7101 and reported maximum RSS4660816 KiB.

The original gradient norm is373996.5318415453 and affine readback error1.2588406049489384e−10. The original gradient was not replaced by a presumed exact computed center. Recovery reported local mismatch L2=6.13803517486775e−17, Linf=1.7629296731203753e−17, and exterior-gradient L2=2.6559812358816e−10. The original-H residual is2.656166990667633e−10, relative7.103800644290338e−16. Saved same-vector supplied-versus-frozen original A and AT differences are both0.

The full-factor `input_identity` is null; its hash beginning74234e98 is the hash of that null field, not a unique model identity. The separate original-input and factor-array identities remain in the original report. The full QR factors were not independently exported as raw payloads. Reading these existing scalar reports does not constitute a full-factor byte audit.

## 8. Original FD and new parent pair

The complete original affine Rphi FD was recomputed on the actual new warm. Its fourth-order Richardson maximum is9.83834122423049e−10, below the unchanged5e−5 threshold. The second-order maximum is9.883426404089236e−6 and the second-order contraction checks passed. The separated boundary offblock maximum is0.

The response explicitly uses the complete previously solved real T112 zero-height Jacobian as an affine map. It reports `current_H_equals_affine_anchor:false`, `nonlinear_native_at_current_H_solved:false`, and `full_BVP_solved:false`. No ready linear graph substitutes for the actual zero-H response, and no prior response is relabeled as a new check.

The new pair is:

| Original file | Bytes | SHA256 |
| --- | ---: | --- |
| `twenty-one-condensed-warm/warm-001.json.gz` |4827392 |`3f45b939752cbe338ab5037a481ee2639b40783950ca4664d23c8ff168f4d535` |
| Decoded original `twenty-one-condensed-warm/driver-status.json` |2007513 |`f4de267f1630201fb077b9d6245016760868f9a20a5b4624db08e780ce2f90e9` |
| Published status gzip |242383 |`4ce10967f799b887540049617bfa16b59d171dd0019396906d6dde628450365c` |
| Decoded original `physical-response/response-check.json` |1376936 |`2dabe4a9402c3ee299420c30f46b3a148c3a2828fce286c1000cd17a95f6e85e` |

The schema is `exact-constraint-twenty-one-query-condensed-complete-H-warm-v1`, with `accepted_warm_steps:1` and `optimization_progress:true`. The status binds the actual warm bytes; the FD binds the same warm and its entire producer object. The whole parent producer is retained and the original699-node mesh is identical. All14 recorded report/parent identity checks pass. All56 distinct current mathematical/FD consumed-source hashes match actual local source bytes. These are byte and structural comparisons only.

At this note's first publication, the original domain/condensed/root payload audit is assigned to the independent public Actions21 reader and is not claimed complete here. The current identity readback covers only the explicitly listed original files, producer relationships, and source bytes. No fresh numerical solve or extra acceptance gate is required to publish the actual trial outcome.

## 9. Smallest next step supported by this result

The nearest rejected1/4 step isolates **left-RMS484** after all existing21 modeled queries, nodes, and midpoints pass. A minimal next model can add that one complete2048-angle left-RMS query at the original fraction, starting from this actual68 new warm and paired status. Its15 left queries plus7 original midpoints would give22 typed queries and45056 B rows.

This addition would use the already declared node484 coordinates. The declared continuous466-through486 plus-controls layout would stay7101, while the actual B block-column union would fill the previously zero node484 and become7101. The complete-H unknown for that node already exists; its newly nonzero B derivatives must be captured with the same original Jacobian construction, including all controls and outside-C offset terms. The baseline C support can remain4059 with the full offset.

This is a next-step design, not an executed request or a guarantee that1/4 will be accepted. The farther trial failures at already-modeled points remain real. The original nonlinear backtracking and complete RMS checks must continue to decide the actual result. The separate lambda27 comparison must use its declared same-parent model and cannot borrow this run's differently weighted later merit as if it were the same objective.
