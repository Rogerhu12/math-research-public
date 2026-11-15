# Actual request70: lambda27 accepts1/128; nearest rejection is left-RMS465

Classification: actual computational result and original-output provenance readback. This is an optimization warm, not an accepted coupled BVP, native-tail solve, closed surface, or existence certificate.

Author: amplitude, with the separate same-parent scientific-byte comparison by exact_refinement. Root retrieved the completed reader artifact and the original warm. All numerical values below were produced in public Actions. Local work only reads existing JSON, compares structures, and hashes original bytes.

## 1. Result and the limit of the damping comparison

Request70 accepted one optimization step at **1/128** and passed the original complete affine Rphi FD check. Its nearest rejected step, **1/64**, had finite original nodes and midpoints, passed all21 modeled angular queries, and decreased the actual fixed-weight merit. The complete original RMS check rejected exactly **left-RMS465**. Its right RMS family had no invalid queries.

The same-run merit was43.755265024906336 before the step and43.73282692338201 afterward. The original recorded decrease is0.022438101524329568, predicted unregularized decrease0.022461446499691326, and ratio0.9989606646498889. The physical collocation maximum became0.007108143274268264. `success` and `new_coupled_finite_acceptance` remain false.

Request70 was designed as a lambda27 experiment using the same actual66 parent, scientific source formulas, and21-query layout as request68 with lambda270. **The actual finite arrays are not all byte-identical.** The separate completed-byte comparison found differences in the stored B/Gamma arrays, b/g, and several original A input hashes. This is therefore a same-parent, same-formula parameter experiment, not a verified fixed-finite-A/B causal experiment in which only lambda changed. A hash difference neither measures the difference nor proves that it is confined to last bits.

The observed lambda27 step improved the worst physical residual more than request68 did, but its recorded total weighted-merit decrease was smaller. Its finite-budget QP candidate also has much poorer final stationarity and a substantial local radial repair. These results do not establish that lambda27 is uniformly better or that damping alone caused the different behavior.

The complete eight-trial field extraction is [actual70-original-readout](2026-11-14-actual70-original-readout.json). The [primary identity readback](2026-11-14-actual70-primary-identity-readback.json) records the actual parent, output, source, and transparent-compression checks. The original large reports remain intact in the scientific artifact and in the completed reader artifact; the extraction is not a replacement for them.

## 2. Execution, publication recovery, and immutable identities

- Scientific run: [43656059206](https://github.com/Rogerhu12/math-research-public/actions/runs/43656059206), job132634747064.
- Source commit: `ab974f19df95e509346fa15d0cefc037780434fd`.
- The warm, original FD, and artifact-preservation steps succeeded. The original publication step failed during rebase on a HANDOFF rule-line conflict. This publication failure did not undo the completed science.
- Scientific artifact14139045881, `visible-followup-condensedqp-43656059206-1`,606816318 bytes; ZIP SHA256 `e45f32846bf48cb474c738c58675b30dada435229846ed3b27e319d8dcb63bd9`.
- Completed readback and publication recovery: [43657876708](https://github.com/Rogerhu12/math-research-public/actions/runs/43657876708), source `c337fbad640298d5cdffadb1451746fbdd773662`, job132640383334, all steps successful. It read the existing artifact; it did not rerun the scientific calculation.
- Strict readback source: `42fb5d0f97c2cee619e2ac1b7e6ee2b9249ee42a518a23cdc9d4c462e0d3c3fa`.

The mathematical producer is `geometry_20261114_twenty_one_query_lambda27_condensed_warm.py`, SHA256 `a8dd293b4b10ab45a2e69dd1e3e37a2032e4af3eb4d5f21eefa556277cb0d64c`. The original FD wrapper has SHA256 `270797569ecff1e3b895d8bb5482c6c9f3c2a4e11d29ebc980c3cfd8bcd88bb0`; the read-only collocation observer wrapper has SHA256 `12437f6887b7fb6a7d5ea91214b95227056238054cd73e6db8c123f2aa49e881`. The current schema is `exact-constraint-twenty-one-query-lambda27-condensed-complete-H-warm-v1`.

The initial parent was the actual66 pair, not a warm produced by67 or68:

| Original input | Bytes | SHA256 |
|---|---:|---|
| Parent warm |4817773|`80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6`|
| Parent original decoded status |1955482|`04ace7953961b3905d2b72639976025dc9c4efd0bef7b932585cf21f8249bcd4`|

The new actual pair is:

| Output | Bytes | SHA256 |
|---|---:|---|
| `warm-001.json.gz` |4830647|`40c6ec6c4b9694fb00b02ef3af5a038e54ed89b28f407436cd0c96dadad509a8`|
| Original decoded `driver-status.json` |2736077|`3f8d217914b3c7fe737e9e06e4736d94ef7bd72f152a5623dd4ccc99221372b3`|

The entire parent producer is retained; the new status identity is a subset of the actual new warm producer, and the FD producer matches that new producer completely. The699-node mesh is unchanged. The public gzip status and FD decode to their original JSON bytes without reserialization. All17 recorded parent/report checks passed, and57 source-file SHA claims present in the primary reports matched local source bytes. The broader completed-artifact reader checked63 source files; these are different, explicitly stated scopes.

## 3. Complete actual trial sequence

Every one of the eight recorded trials had zero original nodal domain failures. The full RHS was recomputed in each original trial. All core rows and all scalar-control rows remained constant across nodes, and the exact left residual was zero. The three finite collocation trials reported zero constant-row residual; the earlier nonfinite trials left that maximum undefined. The original4096-point rho guard passed. A skipped RMS stage is not reported as a passing RMS stage.

| Step | Original bad midpoint intervals | Selected21-query result | Complete RMS stage | Outcome |
|---:|---|---|---|---|
|1|467,468,473,474,475,477,479,480,481,482,483,484,485,486,487,491,492,494|Several failures, including already modeled queries|Not executed|Reject|
|1/2|465,466,467,472,477,479,481,482,483,484,485,489,491,492|Several failures, including already modeled queries|Not executed|Reject|
|1/4|475,481,482,484,488,489|Several failures, including already modeled queries|Not executed|Reject|
|1/8|465,481,484,486|Left466, left467, and midpoint481 fail|Not executed|Reject|
|1/16|484|All21 selected queries pass|Not executed|Reject|
|1/32|None|All21 selected queries pass|Left464 and465 fail; right family passes|Reject|
|1/64|None|All21 selected queries pass|Only left465 fails; right family passes|Reject|
|1/128|None|All21 selected queries pass|Both698-query RMS families pass|Accept warm|

At1/32 the original merit was43.666083392245646, decrease0.08918163266069001, ratio0.996842109815866. Its left464 minimum beta squared was−0.21829951808444692, and left465 was−0.5720631783486281. The source did not accept this decrease because the original RMS domain gate failed.

At the nearest1/64 rejection, the original merit was43.71049325509106, decrease0.044771769815277196, predicted decrease0.04485928710355122, and ratio0.9980490709076137. Its physical collocation maximum was0.0071071569456406455 and boundary maximum2.9416326445021507e−8. Nevertheless, left465 at station1.1603320320063233 had minimum beta squared **−0.9357384204538486**, at phi3.040349921589341. This query lies outside the modeled support beginning at466. The selected linear beta-squared minimum was positive,0.0014824774871343704, but that is not a certificate for the unmodeled query or the complete nonlinear domain.

At the accepted1/128 step, the original boundary maximum was2.9649792414025513e−8. The full RMS re-evaluation had no invalid left or right queries. Its selected linear beta-squared minimum was0.001486593027475669. All21 actual selected grids had positive finite minima.

The farther failures are material: the data do not say that left465 is the only obstacle to a unit step. In particular,1/16 already fails at the original unmodeled midpoint484, and larger steps also fail at modeled queries. No midpoint484 or left465 was silently added to the completed calculation.

## 4. Actual C/H selection and finite-budget QP accuracy

The original C candidate was retained. Its damped objective was43.75499323264019. The recovered R270 candidate was selected with objective42.07281356158697, complete original directional derivative−2.879135929293701, and damped-model decrease1.6824514633192593. The saved squared weighted-J action was1.0421189973021074, damping penalty1.3512499346467757, scaled direction norm0.043053065394286216, and maximum coefficient direction0.006661320259912167. These are copied original readouts, not locally recomputed quantities.

The local QP stopped at its512 working-row budget. Its final saved stage was511; the200 dual sweeps were also exhausted. The newest row was31538, midpoint475, angle index818. At that unrepaired stage,1110 of43008 original linear slacks were negative, the minimum was−0.178110958713476, and the maximum relative violation was1.0590449894364138. The worst relative row was16438, left475, angle index54, with slack−0.05983047504350231 and original margin0.05649474350975586. The reported local stationarity norm was1.5328852972045167e−8; this small stationarity value did not establish full-row feasibility.

The local radial factor was **0.48566204484618775**, producing a minimum original linear slack4.496403249731884e−15 with no negative rows. The local repaired stationarity norm was4658.8335745395325. After full affine exterior recovery and the original selector, a separate final global radial factor0.9999999999994021 repaired four tiny negative linear slacks. The final full direction had minimum slack6.716849298982197e−15 and no negative rows. The global selector changed the conditional recovery, so the final selected direction is not labeled a conditional optimum.

The final original full-model stationarity norm was **2700.3404848009704**, complementarity sum0.002923712311614811. The best saved R267 raw-floating lower bound was−4959.191244468013, yielding final cross-point gap5001.2640580296 and distance diagnostic3.7041718437583566. These loose values do not certify a well-converged QP or a validated enclosure. They are not new BVP acceptance gates. Actual descent and the original complete nonlinear backtracking tests remain the operative warm acceptance conditions.

Helper time was261.07375310199996 seconds, including local-QP time204.55649346500013 seconds. Warm elapsed time was647.242005641 seconds. These timings describe this completed execution only.

## 5. Original row461 and the same-parent comparison

The complete physical maximum remained interval461, radial mode1, angular frequency2, original residual row155819. Its accepted signed value was−0.007108143274268264. The original frozen row weight was199.05060973500673, from the once-fixed base weight array with SHA256 `ae83aa163850620927fdb03a43c5c6f17c6fcc1b84e8f47621c74ca6d47b0766`. It was not recomputed from trial midpoint values. This row lies outside B support but remains in the complete A/H response; it is not omitted or assigned zero weight.

For comparison, the stored request68 result was:

| Actual saved observation | Request68, lambda270 | Request70, lambda27 |
|---|---:|---:|
| Initial newly frozen merit |43.75526502490638|43.755265024906336|
| Accepted step |1/8|1/128|
| Recorded actual merit decrease |0.050765805975864|0.022438101524329568|
| Accepted physical maximum |0.007108973872610448|0.007108143274268264|
| Nearest rejected original query |Left484 at1/4|Left465 at1/64|
| Final full stationarity norm |4.650449587614451e−6|2700.3404848009704|

This table only juxtaposes original observations. It does not subtract different objectives to create a new metric or assume identical finite operators. The [completed same-parent byte comparison](2026-11-15-actual68-70-same-parent-finite-array-comparison.md) by exact_refinement found that the same parent pair, query/layout data, raw base, Pi, beta, and890 of1226 domain arrays matched. All60 shared source hashes matched. The336 differing arrays were all21 Gamma and B-row arrays across their eight chunks. Original b and g differed, while constraint-margin c matched. Of the nine original A-input raw hashes, L/R/P/BY/BC differed; BP/inlet/S/Wr matched. Those nine A hashes are original Actions records, not independently exported complete A payloads. The unexported full QR factor is not claimed independently audited.

Thus the supported conclusion is limited and useful: this actual lambda27 trial gives better movement in the saved worst physical row, less total weighted-merit improvement, a much smaller accepted step, and a different nearest domain limit. Finite-model rounding differences and unequal QP accuracy remain part of the evidence. No unique damping explanation or universal preference follows.

## 6. Original linearization, condensation, and FD readouts

The original B implementation checks passed: maximum normwise adjoint error2.748954111858616e−18, full/local action difference0, and complete original complex-chain relative error1.3756514203153922e−12. The original independent A complex check was8.673617379884035e−19, but its direction contains only free inlet core and global scalar controls, with interior physical coordinates zero. It is not represented as a check of every interior physical column.

The condensation retained the complete affine term, pure-global root, and exterior response. It performed212 reverse fronts,512 local H solves, and one complete recovery; its local dimension was7101. The original affine reconstruction error was9.031098462606608e−11 at original g norm373996.5318415453. The actual recovery mismatch was5.8585791914949916e−15 in L2 and2.638433091797787e−15 in Linf. The original H residual was2.55919335797423e−9, relative6.844585845141335e−15; the exterior-gradient L2 was2.5591045179635296e−9. Same-vector supplied-versus-frozen A and AT actions were reported equal. Maximum RSS was4658776 KiB. The factor input identity field is null; its hash is not a unique model identity.

The original complete affine FD passed with maximum fourth-order relative directional error **7.114402626034738e−10**, below the unchanged5e−5 implementation threshold. The second-order readout was9.883365939138494e−6 and contracted. FD time was24.20810759999995 seconds. It binds the actual new warm bytes and full producer. It used the genuine completed T112 zero-H J as an explicitly affine map; current H was not that anchor. It did not run a nonlinear native solve at the new H, replace the actualJ with `ready.linearD`, or accept the full BVP.

## 7. Completed byte audit and remaining task

The successful independent readback verified the entire pinned scientific ZIP and safely read its original files. It verified190 domain NPZ files containing1226 NPY arrays,108 condensed NPZ files yielding38 complete arrays through42 references, and14 raw condensation/recovery files totaling415120992 bytes. All63 source-file hashes were present and matched; the typed midpoint files had their original descriptors. Current B has43008 rows,236036 global columns,7101 declared local columns,6763 actual compiled columns, and the explicit338-column zero-B node484. The original full H retains that node's variables. Full QR factor arrays were not exported, so no independent full-factor file audit is claimed.

The complete byte-audit report remains in the small completed-reader artifact. The primary readback additionally rechecked the actual original status, new warm, FD, parent subtree, source bytes, and transparent gzip relations locally. It did not repeat the science or recompute an array action, norm, beta, or optimizer result.

The next mainline decision must use actual request72's lambda270 result and its real nearest rejection. Request70 is retained as a completed, reproducible comparison and an additional warm, not promoted to a coupled solution or silently substituted as the mainline parent. The original nonlinear tail, whole closed geometry, same-g refinement, reach, and held-amplitude requirements remain unpaid.
