# Actual request39: fixed-support projection, global repair and one full trial

Request39's twelve-query lane produced a real decreased warm on its
first trial, alpha1, and the fresh complete affine Rphi FD passed. The
chosen direction came from the fixed-support projection followed by a
global radial factor `0.002645002409295411` and the original feasible
segment recomposition. It was not the original-ray backup branch.

This distinction matters: alpha1 applies to the already strongly
scaled direction. The actual merit decrease was
`0.0022286119614634003`; the unscaled local projection remained
linearly infeasible after200 sweeps. The run supplies a legitimate
small warm improvement with all original domains checked. It does
not establish a well-solved local projection, a full damped-model
optimum, a new nonlinear native tail, an accepted full BVP, or a closed
surface.

## 1. Actual run, complete package and preserved parent

| Item | Actual value |
|---|---|
| Public run | `43620111146` |
| Twelve-query job | `132523707261` |
| Source commit | `56e8912844b6d7fafa268a9da8f184d6d055756f` |
| Artifact | `14123527874`, `visible-mainline-twelvequery-43620111146-1` |
| Complete ZIP size | 226302799 bytes |
| Complete ZIP SHA256 | `214021572e32bdfef98293e25039b1ecd9af23c6a078ea98fc1906d6e1b312ed` |
| Warm elapsed time | `247.74261838` seconds |
| Fresh FD elapsed time | `20.685872421` seconds |

The actual warm, FD, artifact preservation and ordinary publisher
steps all completed successfully. The other native lane in the same
run is a separate calculation; its outcome is not a result of this
warm lane.

The exact incoming field was request37's newly saved eleven-query
warm, together with its actual paired status:

| Parent file | SHA256 |
|---|---|
| `eleven-query-warm/warm-001.json.gz` | `dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8` |
| `eleven-query-warm/driver-status.json` | `37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0` |

The complete parent producer subtree is preserved. The699-node mesh,
all453 augmented state rows per node, saved RHS values, original
complete scalar formula and original accepted96/prepared699/T112
input bindings remain present. The new exact-coordinate inlet
projection reports maximum difference0. The previous failure evidence
which motivated RMS470 was measured during request37's model from
its request35 parent; it was not an already executed failed trial on
the newly saved request37 field.

The frozen source and mathematical interface is
[the twelve-query fixed-support note](2026-11-14-twelve-query-fixed-support-RMS470-interface.md).
The new output schema is
`exact-constraint-twelve-query-fixed-support-feasible-projection-warm-v1`.

## 2. Actual complete B, fixed correction support and implementation checks

The run used nine complete left-RMS grids on intervals
470,471,472,473,475,477,479,480,481, followed by the three original
collocation-midpoint grids473,475,477. Every grid has all2048 original
physical-phi angles. The left fraction remains
`0.17267316464601146`; midpoint inputs are the original returned
`state.middle` and `problem.mid`, with their complete nodal RHS chains.

The measured complete B shape is24576-by236036. Its full local-column
union is24576-by4397, comprising thirteen physical nodes470–482 and
the original three global controls. The compiled row arrays occupy
133496832 bytes. The model identity is

`18a5ad26655ec12a2c19eb0887a1895ee2bfeadf84f6fac9695f83d2a9f7977b`.

Only the C-projection correction was restricted to4059 coordinates:
physical nodes471–482 and the three controls. In particular complete
B still contains the338 physical node470 columns. The outside raw
direction was included through the actual complete action

$$
d=B_{\rm out}(z_0)_{\rm out},\qquad c_{\rm eff}=c+d.
$$

No column was erased from the complete model or from the later full
B checks. The original complete A construction called its Jacobian88
times; B captured only original calls59 and61. The capture retained13
nodes and13 actual variants. The two original chunks' shared node480
J/P identities agree, and every interval's endpoint binding agrees
with the preserved endpoint pool. No second full Jacobian was built.

The actual B implementation checks report:

| Check | Original Actions value |
|---|---:|
| Maximum normwise adjoint error | `5.338229723239566e-18` |
| Maximum local/full action discrepancy | `0.0` |
| Actual complete raw-LSMR direction versus original complex chain, relative | `1.0737010004479039e-12` |
| Seeded local direction versus original complex chain, relative | `9.311810238217192e-13` |
| Original constrained collocation complex-direction relative error | `8.673617379884035e-19` |

The last row has its precise original scope: free inlet core and
global controls vary, while interior physical coordinates of that
independent test direction are zero. It does not claim to test every
interior collocation direction. The B complex check separately uses
the complete actual236036-component LSMR direction and all twelve
typed query chains. Both original implementation checks passed;
their thresholds and scientific scope were unchanged.

## 3. Original LSMR model and the actual restricted projection

All weights were refreshed at the actual request37 input, then fixed
for this one model. The current merit before the step was
`44.292419650985686`. The end merit of request37 was
`44.292172704126806`, under that previous model's weights. These two
numbers are not a cross-model increase or decrease and must not be
subtracted as if the weighting were identical.

The original lambda270 LSMR stopped at80 iterations with `istop=2`,
below its200-iteration cap. Its original `atol=btol=1e-7` and complete
regularized operator were retained. The actual readouts were:

| Raw LSMR quantity | Value |
|---|---:|
| LSMR `normr` | `9.354656637941503` |
| LSMR `normar` | `2.7173987141625236e-5` |
| Independently read preconditioned normal norm | `2.717398714179766e-5` |
| Original unpreconditioned regularized gradient norm | `313.12159761275774` |
| Actual raw merit derivative | `-1.0752384321814896` |
| Actual raw damped-model decrease | `0.5376192440943904` |
| LSMR elapsed time | `8.743305399999997` seconds |

The preconditioned stopping statistic and original gradient are
different norms. This run did not stop at the iteration cap. These
readouts alone do not identify the raw direction as an accurate model
minimizer or explain a nonlinear domain failure.

The complete outside contribution was material to the local
halfspaces. The actual effective local offset had54 negative entries,
minimum `-12.764404423654142`, maximum `0.500475815214576`, and no
nonfinite or zero entries. The helper correctly allowed negative
effective offsets. It used every original row and recorded the full
offset arrays.

The actual restricted C projection used all200 allowed Hildreth
sweeps and stopped by `maximum-sweeps`. It did not take a numerical
fallback. The final recorded values were:

| Restricted projection quantity | Value |
|---|---:|
| Normalized primal violation | `0.0674319533199593` |
| Largest final dual coordinate update | `0.048493511480076634` |
| C-projection objective | `0.10577423019885471` |
| Projection stationarity norm in x coordinates | `7.0161199501003385e-15` |
| Signed complementarity sum | `-1.304489781900462` |
| Maximum absolute complementary product | `0.46521517133777845` |
| Original full slack minimum before repair | `-22.56837039044266` |
| Negative original full slacks before repair | 272 |
| Computed zero local rows | 0 |

Small stationarity here is not sufficient for projection optimality:
the actual primal violations and complementary products remain large.
Nor does failure to reach feasibility in200 sweeps prove that the
restricted halfspace set is mathematically infeasible.

The actual raw complete-offset reconstruction discrepancy was
`4.263256414560601e-14`; the local candidate's corresponding
discrepancy was `3.552713678800501e-14`. These are original Actions
readouts comparing the complete B action with the retained outside
offset and local-block assembly. The local helper reports exact byte
preservation of the outside raw coordinates before global radial
repair. Its multipliers describe this local projection only; they
were not reused as multipliers for the complete damped model.

## 4. Which direction was actually selected

The original same-model selector retained both its raw-ray backup and
the corrected local candidate. Their complete repairs were:

| Candidate | Before-repair full slack minimum | Negative rows | Actual global radial factor |
|---|---:|---:|---:|
| Original raw-ray backup | `-86.17165488972205` | 1988 | `0.00010571139027051392` |
| Fixed-support local projection candidate | `-22.56837039044266` | 272 | `0.002645002409295411` |

The raw-ray model-minimizing prefactor was1. Both candidates then
passed every complete linear halfspace after their own radial
repair. These radial factors act on the entire scaled vector,
including the outside raw coordinates and physical node470.

For the same complete damped quadratic, the segment derivative at
the feasible raw backup was `-0.002114328728833378`, and its curvature
was `5.956169157584628e-6`. The computed segment parameter was1. The
actual selection label was `feasible-segment-minimum`, with no
raw-backup fallback and no additional repair of the rounded composed
vector. The reported model decreases were:

| Actual feasible direction | Damped-model decrease |
|---|---:|
| Original-ray backup | `0.00011365894169858557` |
| Final selected direction | `0.0022250095859531705` |

Thus this was the repaired projection endpoint of the segment, not
the original raw-ray branch. The implementation still forms the
floating expression `backup+tau*(repaired-backup)` and re-evaluates
the entire result. Even at tau1, the preserved B actions of that
rounded composition need not be byte-identical to those of the
separately repaired endpoint. The final candidate's stored B action
and slacks do agree byte-for-byte with the separately saved final
linear-margin file. No identity between different floating
evaluation orders is assumed.

The final original full-model quantities were:

| Quantity | Value |
|---|---:|
| Actual merit derivative | `-0.002228217210437996` |
| Squared weighted-J action | `2.655116310605183e-6` |
| Damping penalty | `3.760132659045008e-6` |
| Scaled direction norm | `7.181874627793336e-6` |
| Maximum coefficient-direction component | `4.7256058504475404e-7` |
| Original complete damped-model gradient norm | `1007609.8218067184` |
| Final full linear slack minimum | `8.604228440844963e-16` |
| Final negative or zero linear slack count | 0 |
| Stored zero-dual posterior E | `6963494.876552584` |

The large zero-dual posterior value is a loose fixed-model diagnostic,
not a model-optimality certificate. There is no claim that the
restricted C projection solved the complete R265 quadratic. The
reported alpha1 below describes a small, already repaired direction;
it cannot be compared with earlier trial alphas without also retaining
their actual directions and model scales.

## 5. The one actual trial and every original domain check

Only one trial was needed. The original limit remained17 trials, but
the first actual alpha1 trial passed its merit test and the complete
original domain checks:

| Actual trial quantity | Value |
|---|---:|
| Alpha | `1.0` |
| Fixed-weight merit before | `44.292419650985686` |
| Fixed-weight merit after | `44.29019103902422` |
| Actual merit reduction | `0.0022286119614634003` |
| Predicted unregularized merit reduction | `0.0022268896522826933` |
| Actual/predicted ratio | `1.0007734146947702` |
| Physical collocation maximum before | `0.007110320785400957` |
| Physical collocation maximum after | `0.007110317266439588` |
| Complete affine boundary maximum before | `8.074771843017406e-8` |
| Complete affine boundary maximum after | `8.053357926995966e-8` |
| Original4096-angle rho minimum | `0.16604058243274977` |

All699 nodes and all698 original collocation midpoints were finite.
Both original RMS tests, at fractions
`0.17267316464601146` and `0.8273268353539885`, checked all698
intervals and reported zero failures. The exact inlet and constant
core/control collocation residuals remained0. The complete trial RHS
was genuinely recomputed. The damping penalty is absent from the
actual nonlinear merit, as in the frozen original method.

The complete actual query minima at that same accepted trial were:

| Kind | Interval | Base beta squared minimum | Trial beta squared minimum | Trial minimum angle index |
|---|---:|---:|---:|---:|
| left RMS | 470 | `0.11970340390491518` | `0.05951122083952942` | 0 |
| left RMS | 471 | `0.021770130579212732` | `0.13522336911564592` | 0 |
| left RMS | 472 | `0.19983054908853914` | `0.22047727919075333` | 0 |
| left RMS | 473 | `0.6465538855873549` | `0.64553780327205` | 948 |
| left RMS | 475 | `0.5479303480082631` | `0.5472047841442659` | 0 |
| left RMS | 477 | `0.48326299488698077` | `0.48262359058745063` | 0 |
| left RMS | 479 | `0.5126277647018241` | `0.5119494754801938` | 0 |
| left RMS | 480 | `0.005420214419654346` | `0.005412760152846308` | 0 |
| left RMS | 481 | `0.08875107286486683` | `0.08863365460168782` | 0 |
| original midpoint | 473 | `0.3785689893800356` | `0.631786155613238` | 11 |
| original midpoint | 475 | `0.758522334525311` | `0.7575165049898797` | 0 |
| original midpoint | 477 | `0.8518954503614481` | `0.8507628406352064` | 0 |

Every value in the table was read from the original Actions reports.
No new local evaluation of the field or its extrema was performed.
At RMS470, angle0, the saved base value is
`0.11970340390491518`, the selected Bz is
`-0.05985170195245673`, and the linearized beta squared is
`0.05985170195245845`. The actual value
`0.05951122083952942` remains positive but is not exactly the linear
reserve. This directly illustrates why the true nonlinear checks
remain necessary even after every linear row has passed.

The three retained read-only midpoint-observer reports correspond to
the original base evaluation, the trial and the full RMS recheck.
Each reports no bad midpoint, unchanged original finite flags, and
unchanged original residual bytes. No failed-midpoint NPZ is expected
when there is no bad midpoint to save. The observer did not recompute
the whole flow or change a gate.

The original independent real full-residual directional check reports
merit slopes
`-0.002228206774645969`, `-0.0022282301159748386`, and
`-0.0022283438738668337` at its three fixed step sizes. Its stored
relative full-vector discrepancies are respectively
`1.2422827863730263e-5`, `1.7909384064792777e-5`, and
`2.6554120852002115e-5`. This is a readout with the same weights and
actual RHS/boundary evaluations, not a new scientific acceptance gate.

There is no observed rejected trial in this request from which to
infer a thirteenth limiting query or a larger safe step. The original
collocation and affine boundary residuals also remain well above the
full BVP's unchanged final tolerances.

## 6. New warm, complete H and fresh boundary FD

The new warm is4,736,026 bytes with SHA256

`451e7ef1540d897602ea7e45170aafa1cd2684fa8936f2b4b442f97ce6090d4f`.

Its paired status is466,271 bytes with SHA256

`51122351db657b94ad36d327f865ed9b44a52fde8c84062ef6bbda7194620317`.

It records one progressed warm step and explicitly retains
`success=false`, `new_coupled_finite_acceptance=false` and no complete
closed-surface acceptance. The first eight entries of the complete112
native-height input preserved by the fresh FD are

```text
4.837914992953308e-14
3.1615803733932464e-14
1.940687962162465e-14
1.1074682895918654e-14
5.884038496413614e-15
2.975840416930587e-15
1.4770711959929693e-15
7.3351710430330375e-16
```

The original full list is retained; these nonzero values are not
thresholded into the zero anchor. The actual global control values
saved in the complete scalar specification are

```text
[-2.227596880008665e-19,
  8.779951572632976e-20,
 -1.6058663220191497e-19]
```

The fresh complete Rphi FD actually consumed the new warm and its
complete producer. It passed the original fourth-order Richardson
comparison with maximum relative error
`7.528714322173196e-10`, against the unchanged implementation threshold
`5e-5`. The recorded second-order maximum is
`9.883427677588788e-6`, and the original truncation-contract check is
true. This remains the full genuine zero-H T112 Jacobian held
explicitly affine at the new nonzero H. No ready linear graph was
substituted, no new nonlinear native solve occurred, and no full BVP
acceptance is asserted.

## 7. Complete read-only byte audit and reproducible records

After downloading the original package, the local inspection used
only decoding, hashing, shape/dtype checks, byte comparison and
reassembly of saved chunks. It did not run a new matrix action,
finite-difference derivative, ODE, native solve or optimization.

All111 domain NPZ files and their708 NPY arrays match the recorded
compressed-file SHA, byte size, shape, dtype and raw-array identity.
For every one of the twelve typed groups, the actual chunks reassemble
to the recorded complete B, Gamma and Pi hashes. The concatenated
beta array matches
`8b2e63413ab85e1d85d71836dc9b6d63b1c13581c014e55f11b7a7c92d388f54`.
The canonical recorded model metadata reproduces the complete model
SHA quoted above.

The thirteen saved endpoint J/P pairs and every original interval
binding agree. The three saved original midpoint input arrays match
their recorded subset identities. The original mesh, complete state
and saved RHS arrays are byte-identical to the actual request37 parent
at the B base point. The4059 fixed-support indices match exactly
nodes471–482 and the three global controls, while the full B layout
retains all4397 local columns including node470.

The full outside-action, original-c and effective-offset arrays match
their recorded identities. The actual raw LSMR vector's identity is
`e8a33ba195d601b5f0d03d820def2bf7174a60ed6320ad75af4090ff16377ae7`,
exactly the direction used in the original B complex check. Current
producer source hashes cover27 files; the union with the fresh FD
contains31 distinct source files, all matching their frozen bytes.

The parent warm/status hashes and the entire previous producer match.
The current status identity equals the original current intent, the
new warm contains that complete identity, and the fresh FD's producer
equals the new warm's full producer. Final selected Bz/slack arrays
match the separate saved final linear margins. There is no relabeled
old FD input or flattened parent chain.

The following files are original request39 records under
`notes/public-actions-43620111146-1-twelvequery/`:

| File below that prefix | SHA256 |
|---|---|
| `twelve-query-warm/model-000.json` | `cad2a68334d026226975b1aac262811183895657bd2806ee2f765542afebaa74` |
| `twelve-query-warm/optimization-intent.json` | `b4f83a44925cea8e4141eedf56048c2124b4a144e3b0a2abc9f4ed623f0855c2` |
| `twelve-query-warm/domain-operator/manifest.json` | `c2eff3284fed6d294434d4b8be82fcaf8e25394e33caa21d32854ea139b16094` |
| `twelve-query-warm/full-angle-operator-check.json` | `64cc0c04d8aa68578d8d0a2619b3bc1d2b30461bb4f7bf36c960b8ed09f40cf6` |
| `twelve-query-warm/model-000-operator-check.json` | `008e8020dfb97ffe0f3955ff1a9ddb9382251212a6c741643aba7ab49880ab25` |
| `twelve-query-warm/local-projection-arrays.json.gz` | `fe40627babc4b2019a84a653c256152edceb3a1e5bbf492f2f04389dd8c40d86` |
| `twelve-query-warm/all-angle-selection-candidates.json.gz` | `33547760e584a6db8593758bd4b498e262fe3d23056cb24c187cc53bc72789b3` |
| `twelve-query-warm/all-angle-linear-margins.json.gz` | `59a6379a91e82abbfd3bf8070c7dcce240d8e144e7c89f67d97f0de46294e59f` |
| `twelve-query-warm/direction-00.json.gz` | `7afb0118794d01ba9a75c87c00ca10f2ca0f3ade48b304666eeb1431978ae368` |
| `twelve-query-warm/lsmr-direction-00.json.gz` | `573a459ded1c438049ead6bc0c1214ce70b5985a8aca121000ef07471595f698` |
| `twelve-query-warm/trial-00-all-selected-angles.json.gz` | `82a20c9d87cb3968f53d4e8ec771598127770a376a470a7517ea58238fd8c118` |
| `physical-response/response-check.json` | `23967f376990257da060d203f20609d9dab23948065974058b3312cecbc9da12` |

The full NPZ/J/P and typed-gradient bytes remain in the complete
artifact identified in section1; the published bounded records retain
their manifest and original identities. The accepted warm and paired
status hashes are in section6.

The concrete next comparison is the separately frozen full-H QR
alternative from the same actual37 parent, with the same twelve
complete queries and unchanged original trials. It must be judged
by its actual same-model C/H comparison, original H residuals and
real trial outcome. This request alone supplies no reason to add a
new query or to infer that additional local sweeps would produce a
substantially better feasible direction.
