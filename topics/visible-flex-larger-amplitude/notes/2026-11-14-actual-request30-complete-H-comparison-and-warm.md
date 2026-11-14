# Actual request30: C retained after the complete-H comparison

The public Actions run executed the bounded complete-H candidate and
compared it with the retained C-metric candidate in the same fixed
quadratic model. The original C candidate had the lower objective and
was selected. Its actual step `2^-8` passed the original complete domain
checks, decreased the fixed-weight merit, and produced a new warm with a
fresh complete affine Rphi derivative check. The nearest rejected step
`2^-7` had finite nodes and collocation midpoints but failed the original
left RMS query at interval471. This remains unaccepted warm progress;
no nonlinear native tail at the new height or complete BVP was solved.

## 1. Actual run and preserved input

| Identity | Actual value |
| --- | --- |
| Public run | `43614132961` |
| Job | `132505423542`, `Mainline fullhprojection` |
| Source commit | `8ed43e0b1119f009642eb983141ad3e86f28af78` |
| Artifact | `14121154981`, `visible-mainline-fullhprojection-43614132961-1` |
| Downloaded ZIP | 244,400,092 bytes |
| ZIP SHA256 | `4cadfd6133f1e3e29fbfb5f5df05862b14c567a74439ae1447493e3ba3a07e37` |
| Actual request29 parent warm SHA256 | `f2e999e7c61d28683dc09adf387e0867b2dd36d271ebe0433fafbec68466fbd9` |
| Actual parent status SHA256 | `a24ebbe3d39d64d7676754c67fc56589652bf6fcd31c93c7eca97e1641bebde4` |
| New warm | `full-H-warm/warm-001.json.gz`, 4,723,248 bytes |
| New warm SHA256 | `8a91f696168a5d4b49c6a10e08ba23333839476117e9f7755b46bf21340607fc` |
| Warm elapsed time | `616.183787271` seconds |
| Fresh response elapsed time | `22.180583147999982` seconds |

The entry consumed the actual request29 field described in
[the request29 note](2026-11-14-actual-request29-observed-seven-query-warm.md).
It retained all 699 nodes, all M112/N2048 field modes, the complete
controlled scalar formula, exact constant core and controls, and the
exact inlet coordinate relations. The initial coordinate projection
changed no coefficient: its maximum reported difference is zero. The
new status has `optimization_progress=true`, one saved warm step,
`success=false`, and `new_coupled_finite_acceptance=false`.

The new saved controls, without thresholding, are

```text
[-1.4848087956500275e-19,
  5.3644493066971466e-20,
 -1.165935961123015e-19]
```

The saved intent equals `driver-status.identity`; that identity is also
the unchanged subset of the new warm's producer metadata. The entire
parent producer subtree remains available in `resume_producer`.

## 2. The fixed model used for the comparison

Both candidates used the same original complete A, weighted residual b,
damping270, B, and reserve vector c. The complete scaled-coordinate
dimension is 236,036. B has 14,336 rows, comprising all 2048 physical
angles at each left RMS interval
`(472,473,475,477,479,480,481)`, fraction
`0.17267316464601146`. Its possible local support has 3,721 columns.
The reserve parameter remains one half of each base beta-squared value.
This is an algorithmic constraint model, not a continuous domain
certificate or a replacement for any original nonlinear check.

The compared objective is

$$
f(z)=\frac12\lVert Az+b\rVert^2+\frac{270^2}{2}\lVert z\rVert^2.
$$

The nonlinear merit omits the damping term and holds the current row
weights fixed throughout every trial. The weights are refreshed at the
start of this new model. Consequently the request29 ending merit and
this run's beginning merit must not be subtracted to claim a step
decrease. All reported reductions below belong to this one fixed model.

The raw LSMR stopped with `istop=2` at 84 of the allowed 200 iterations.
Its residual norm is `9.36181202217061`; its reported preconditioned
normal norm is `2.8023571296453096e-5`, independently read as
`2.8023571296444233e-5`. Its complete unpreconditioned regularized
gradient norm is `320.85918621725165`. The latter is not replaced by the
preconditioned residual. The raw direction has actual model derivative
`-1.1013207206594153` and damped-model decrease
`0.55066039017657`. The stopping reason was the original relative
tolerance, not the iteration bound.

## 3. The C candidate was retained for an actual objective reason

| Same-model quantity | Original C candidate | Complete-H candidate |
| --- | --- | --- |
| Actual full damped objective | `43.905058168501064` | `44.35849607633413` |
| Actual directional derivative | `-0.7397834189900147` | `-0.014019469795567244` |
| Actual damped-model decrease | `0.4673643909042686` | `0.013926483071170486` |
| Minimum over all 14,336 linear slacks | `1.942890293094024e-16` | `4.6629367034256575e-15` |
| Complete stationarity norm with the reported multipliers | `298457.19124813564` | `1093214.7807709817` |

The helper was both attempted and completed, and its candidate was
usable and feasible in the supplied finite linear model. There was no
helper exception, skipped computation, or silent substitution. The
selection `original-C-metric-feasible-direction` follows the two actual
objective values in the table. The selected direction, its full A and B
actions, original gradient, zero multipliers, and all slacks were
recomputed and preserved after this comparison.

The original C projection used all 200 Hildreth sweeps and reached its
sweep bound. Its local projection objective is `0.04078230848190557`,
local stationarity norm `9.967506570296539e-15`, and complementarity sum
`1.1365312081656265e-6`. Those values describe the local C projection,
not the full damped quadratic's KKT equations. Before radial repair,
146 original linear slacks were negative, with minimum
`-0.0010666268564686887`. The actual repair factor was
`0.7305634509131044`; all linear slacks then became positive. The
same-model segment minimization selected the repaired projected
endpoint, parameter1, with no further repair. The feasible raw-ray
backup had model decrease only `0.00012329432392568023` and was also
retained in the comparison record.

For the selected C direction, the actual squared weighted A-action is
`0.2573680916004568`, damping penalty is `0.2874699645710353`, and
scaled direction norm is `0.0019857861326840888`. These are the actual
full-dimensional diagnostics of the selected vector.

## 4. What the bounded H computation actually achieved

The helper used `303.33100533100003` seconds. It stopped discretionary
work at the hard total bound of 1200 H products, before its 600-second
wall-time allowance. Its recorded complete action counts are

```text
A=1299, AT=1240, B=101, BT=54, H=1200,
mandatory_H_after_deadline=0.
```

No additional complete Jacobian was constructed. The helper retained
all global coordinates and formed 18 basis vectors and a working set of
16 of the supplied inequality rows. It did not reduce the original
field modes or discard any global controls. The final working rows are

```text
[10240,11253,10262,3018,10283,6144,0,4096,
 3007,12288,7146,8192,11210,4118,11231,6198].
```

All 17 inner CG calls report `converged=false` against their original
unpreconditioned residual targets. The first 16 reached 64 iterations;
the last reached 27 iterations and stopped for the discretionary
H-action limit. For example, the unconstrained refinement's original
residual norm is `495.29279371282666`, against target
`0.011079172793244626`; the last row inverse has norm
`5.7307053616189165`, against target `0.0009626207612861467`.
Approximate inverse vectors were used only to generate a finite global
basis. The basis metric and subspace objective were evaluated with the
actual complete A and damping, without a ridge or eigenvalue clipping.
No complete inverse or full-QP convergence is claimed.

At the last subspace solve, the unrepaired candidate had objective
`43.84399897348401` but 906 negative original linear slacks, with minimum
`-22.89191701121758`. The full-row radial repair factor
`0.013269597641858352` produced the feasible H candidate with objective
`44.35849607633413`. Its finite working-set dual solve also reached its
200-sweep bound. Thus this bounded H attempt improved the very short
feasible raw ray but did not improve the already available C candidate.
The records distinguish accurate evaluation of the full objective from
convergence of either the inverse solves or the complete constrained
model.

## 5. R267 used evidence from a different point of the same model

[R267](../results/R267-two-point-damped-model-posterior-bound.md) permits
an arbitrary evidence point x and nonnegative multipliers, while the
finally selected feasible vector z may be different. This run preserved
the complete original residuals and used that distinction explicitly.

The helper's best stored floating lower-bound expression is
`43.11565368239749`. Its actual evidence label is
`actual-raw-LSMR-zero-dual-evidence`: the original raw LSMR vector with
zero multipliers. It is not an improved bound produced by the later H
refinement. That raw point is infeasible, with minimum linear slack
`-48.446991821107964`, which R267 allows for an evidence point. Its
objective is `43.82176216922875`, and its complete stationarity norm is
`320.85918621725165`. The later H-refined unconstrained point gave the
weaker lower-bound expression `42.139217912110475`.

At the selected C vector, the single-point zero-dual expression is very
loose: E is `610951.268914446`. Using the better evidence point from the
same fixed model instead, the saved final cross-point objective-gap
expression is `0.789404486103571`, and its distance-bound expression is
`0.004653728349122139`. The feasible H candidate separately has gap
`1.242842393936634` and distance expression `0.005839279494838185`.

These are ordinary floating evaluations of the exact algebraic
expressions. The run supplies no directed-rounding enclosure for them,
and they are not certified lower bounds or a complete-QP optimality
certificate. They do not alter any BVP acceptance tolerance. All values
in this paragraph were saved by Actions; no new posterior quotient or
matrix computation was performed while reading the artifact.

## 6. Actual backtracking located a new nearest limitation

Every tested trial had finite original nodal RHS values. The original
collocation-midpoint outcomes were:

| Alpha | Actual nonfinite midpoint RHS indices | Further original outcome |
| --- | --- | --- |
| `1` | `471,472,475,477,478` | Rejected |
| `1/2` | `473,475,477` | Rejected |
| `1/4` | `473,477` | Seven selected left RMS grids positive; rejected at midpoints |
| `1/8` | `473,475,477` | Seven selected left RMS grids positive; rejected at midpoints |
| `1/16` | `473` | Seven selected left RMS grids positive; rejected at midpoint |
| `1/32` | `473` | Seven selected left RMS grids positive; rejected at midpoint |
| `1/64` | `473` | Seven selected left RMS grids positive; rejected at midpoint |
| `1/128` | None | Actual merit decreases, but the original complete left RMS check rejects interval471 |
| `1/256` | None | Original nodes, midpoints, both complete RMS grids and rho check pass; warm step accepted |

At `1/64`, midpoint473 is the original station
`1.2018391887397941`. Its original input is finite, but its original RHS
is nonfinite. All 2048 directly read beta-squared values are finite;
10 are negative, with minimum `-0.13697024968996807` at angle index11,
phi `0.0337475773334841`. At that same trial, the selected left RMS473
minimum is positive, `0.11014163103894614`. They are distinct queries.

The nearer rejection `1/128` has finite original nodes and all original
collocation midpoints. Its actual fixed-weight merit is
`44.36639158903134`, a decrease of `0.006030970373963385`, with
actual-to-predicted ratio `1.0449203003085934`. Nevertheless the original
complete left RMS check reports this failure:

| Original RMS quantity | Actual value |
| --- | --- |
| Interval | `471` |
| Fraction | `0.17267316464601146` |
| Station | `1.1902387410048825` |
| Minimum beta-squared | `-0.013795646025840158` |
| Reported phi | `0` |
| Scalar a, ap, app | `1.1913434951459982`, `-0.12394221883211583`, `-2.4807235920076978` |
| Curve curvature at the reported minimum | `0.10332539113360148` |

The complete right RMS grid has no failure at that trial. All seven
selected left RMS angular grids are positive, including RMS473 with
minimum `0.05675874463452901`. Thus neither good model descent nor
feasibility at all selected linear rows replaced the actual full domain
checks. The newly observed RMS471 limitation belongs to this particular
C direction; it must not be transplanted to a different candidate
without its own actual evaluation.

The accepted `1/256` step has

| Fixed-model quantity | Actual value |
| --- | --- |
| Merit before | `44.3724225594053` |
| Merit after | `44.369488776621324` |
| Actual decrease | `0.002933782783976824` |
| Predicted undamped merit decrease | `0.0028878154177191698` |
| Actual-to-predicted ratio | `1.0159176954231928` |
| Physical collocation maximum after | `0.007110437270942378` |
| Complete affine boundary maximum after | `8.831813076391987e-8` |
| Original 4096-angle rho minimum | `0.16604058243274977` |

Both original RMS fractions checked all 698 intervals and reported zero
failures. All core rows and all control rows remain exactly constant;
the inlet and constant-state collocation residuals remain zero. The
seven selected left RMS minima, in the declared order, are
`0.20837608827248932`, `0.029162423551921002`,
`0.5731584320789811`, `0.5053558364584354`,
`0.5361122065389998`, `0.005772916232701819`, and
`0.09275518996966148`.

Independent real directional checks held the same weights fixed and
gave merit slopes `-0.739784623604578`, `-0.7397837942590968`, and
`-0.7397834495748157`. Their full weighted-vector relative errors are
`8.118318209618428e-5`, `1.0062141256300149e-4`, and
`2.1530305182990646e-4`. These diagnostics support the actual negative
slope but do not establish machine-level convergence of the entire
finite-difference vector.

## 7. Fresh boundary FD, operator checks and observer preservation

The fresh complete affine Rphi check binds the actual new warm SHA. Its
maximum fourth-order directional error is `9.143364336011781e-10`, below
the unchanged `5e-5` implementation threshold. The maximum second-order
error is `9.883390288558213e-6`, and the reported second-order
truncation contracts. The original directions, three centered steps and
Richardson comparison were actually rerun. An earlier pass or warm SHA
was not relabelled.

The current native-height list is genuinely nonzero; its first entry is
`2.3995927160419497e-14`. The check uses the completed genuine zero-H
T112 Jacobian explicitly as an affine map at this new warm. It does not
claim a nonlinear native solve at that height, and it does not use the
ready linear graph. No new native response, Jacobian, final audit or
full Cartesian closed surface was produced by request30.

The full-angle B verification reports maximum adjoint error
`9.88888586928303e-18`, zero local/full action difference, and actual raw
LSMR direction complex-chain error `8.888344076056027e-13`. The seeded
local direction error is `5.755189140889822e-13`. These checks use the
complete original nodal RHS and Hermite chain on the selected queries.
The separate original nonlinear collocation check has error
`8.673617379884035e-19`; its explicitly recorded scope is only free
inlet core and global controls, with interior physical coordinates
zero. It is not described as checking every interior direction.

The read-only observer produced 12 reports and 16 actual bad-midpoint
NPZ files. Every report says that the original returned finite flag and
residual bytes were unchanged. All 16 file hashes and all 48 contained
original array identities were independently checked against the actual
bytes, using the producer's exact tuple-shape/dtype/C-bytes hashing
definition. There were no observer errors. This audit only read and
hashed stored bytes; it did not repeat any scientific calculation.

## 8. Frozen sources and key original artifacts

The actual new entry, complete-H helper and response source hashes are

```text
geometry_20261114_full_metric_projection_warm.py
8fb6411e7b876713725a80c2dbe9e322cc277001b0692ccc59e0edd59ec4e8b0
geometry_20261114_full_metric_inequality_correction.py
d5e9432e979859ed7d5277452ac058eb93e99da1cae7f96f700f15d7359d919c
geometry_20261114_full_metric_projection_response.py
a24f2e528e35ff7944b56c8fc5a3a1c99ffc7bf2cb5a886cc82990aa85e02117
```

The complete producer source ledger remains in the saved intent and
warm. Under the artifact root, the following actual bytes were read and
hashed:

| Relative path | SHA256 |
| --- | --- |
| `full-H-warm/full-H-versus-C-comparison.json` | `f4d7c53c235ced94100e4096006b31fac35653ae6c306dde376ebf5cde208255` |
| `full-H-warm/full-H-result.json.gz` | `aaff45531e1dce4cff15f80155a86c95f408c709b2c669e2a3a20dc0d8303fa7` |
| `full-H-warm/full-H-array-manifest.json` | `95e205c7ef90bbfba08817daf248f464a26a88d8ff4ea0f001a6f3909b84f852` |
| `full-H-warm/full-H-final-selected-evidence.json` | `7024a200e7c274ac50b4baf8e501337ae73ff9a2d483e4885aca2284f6c2aa8b` |
| `full-H-warm/model-000.json` | `4771b53ba505101a065b74650b7b369d3a4b12efc47254b46f251f4048461d46` |
| `full-H-warm/driver-status.json` | `52f4a8d7577cd80f78cd29b244a0c549a00f0cea2d4561bbc83362f20f2fcb19` |
| `full-H-warm/optimization-intent.json` | `709d673cfbd4c5f14ab3a2087ce29e32ba7e4f1f6f6c44c855b562652722d614` |
| `full-H-warm/direction-00.json.gz` | `7da7509d71b2a9e9c76148454116281ee42565872747142ca843da29ce80a532` |
| `full-H-warm/domain-operator/manifest.json` | `1a949ada2d51d44678beab947028047e742fff7587002b9ccd7c3685deebe716` |
| `full-H-response/response-check.json` | `d151d51a525583486b306a96c12ad276aa8e6b205e97652fcf36f76509cbbf0a` |

The full H arrays are preserved by their own manifest, including the
raw and refined evidence, basis, candidate directions, actual actions,
complete residuals and nonnegative multiplier lists. The actual domain
model identity is
`8faeb2c84a44e593f126a8a3afccaf912aa207b1052cab3639a6d371cc15245a`.

## 9. Consequence for continuation

This execution establishes a real successful C-versus-H selection and
another valid warm decrease. It does not establish that a larger H
budget would beat C, that the original complete QP was solved, or that
the new tiny native height may be replaced by zero. The actual helper
resource limit, unrepaired full-row violations and original-gradient
readouts are retained to support a subsequent algorithmic decision.

The independent nine-query branch starts from the same actual request29
parent and adds the two previously observed original collocation
midpoint grids. Its outcome must be read independently, including the
original complete RMS checks. In particular this run's interval471 RMS
failure is evidence about this direction, not an instruction to alter
that already frozen branch or relax its domain checks. Any later
accepted full-DN field still requires the original nonlinear native
response, final audit, complete BVP gates and geometric readouts.


## 10. Subsequent complete byte-identity audit

A subsequent read-only audit checked all 68 B NPZ files and 421 contained
arrays, including concatenation identities for the seven full
B/Gamma/Pi/beta blocks. It checked all 62 full-H NPZ files and reassembled
48 array references corresponding to 30 unique complete arrays. The
first column of the saved 236036-by-18 basis is byte-identical to the
actual raw LSMR direction, identity
`10579c066f064aa58716e53980e228c9d5a78f1ce6eb84948c4b09ae0925be7c`.
The 12 mathematical source identities, actual parent29 warm/status and
entire preserved producer chain, complete 699-node field/RHS data, and
selected final C direction/evidence matched all saved bindings. Only
stored bytes, shapes and hashes were compared; no scientific matrix
action was recomputed locally.
