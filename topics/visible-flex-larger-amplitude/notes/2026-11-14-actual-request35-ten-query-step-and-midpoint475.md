# Actual request35: RMS471 protection permits a larger real step

**Status: numerical evidence from an actual public Actions execution.**
The ten-query run continued the actual request32 warm and accepted an
original complete-domain step of `1/16`. The previous nine-query run
accepted `1/256`. The newly protected left RMS471 remains positive at
the new nearest rejected step `1/8`; that rejection comes from the
unmodeled original collocation midpoint475. All ten selected angular
grids are positive at that rejected step.

The saved field is an unaccepted warm, with a real measured decrease and
a fresh complete affine Rphi derivative check. Its nonzero native
height has not been solved by the nonlinear tail, the complete BVP has
not been accepted, and no closed-surface or completion claim follows.

## 1. Actual execution and preserved parent

| Identity | Actual value |
| --- | --- |
| Public run | `43616658549` |
| Job | `132513122964`, `Mainline tenquery` |
| Source commit | `65fdfd019da295f42c4510a2f3081f3b4a2c59f4` |
| Artifact | `14122008066`, `visible-mainline-tenquery-43616658549-1` |
| ZIP size | 192,883,292 bytes |
| ZIP SHA256 | `8a21da7d488905bf1cb5afc35ad5f9bccc96e00f6ac7ff287ec4c0367d1b42af` |
| Actual request32 parent warm | `7f5e8d5f888b79c4ce0c0db91c9bc4e27bb9ef0c7554c0f578431ddbbecb578e` |
| Paired actual request32 status | `a6224f936f261168ef05a3b51fa3b1318b6d25eacf6653c412d2c33a8731d56e` |
| New warm | `ten-query-warm/warm-001.json.gz`, 4,728,499 bytes |
| New warm SHA256 | `24ca673e64fb60d1d5206ec742ce08c653b390bafd5ecd3ffbe54f0b1c1cd25a` |
| New paired status SHA256 | `214d4eed229c8b63af29bda765dca4506de1646a3addcbd02d0b626068ebf1ff` |
| Warm elapsed time | `154.74737166` seconds |
| Fresh boundary FD elapsed time | `16.635515505` seconds |

The parent is the actual output recorded in
[request32](2026-11-14-actual-request32-nine-query-warm-and-RMS471.md).
The complete parent producer subtree, mesh, physical representation,
complete scalar formula, global parameters and source ledger are
preserved. The exact-coordinate inlet projection has reported maximum
difference zero. The problem still has 699 nodes, M112/N2048, 338
physical and 453 augmented rows per node, and 236,036 exact-coordinate
unknowns. The original uniform-phi rho guard uses 4096 angles.

Both `success` and `new_coupled_finite_acceptance` are false in the new
warm and status; `complete_closed_surface` is false. The status records
one accepted *warm* step and actual optimization progress. Its complete
current `identity` equals the written optimization intent, including
the typed query order, and is the corresponding subset of the saved
warm producer. No old status or FD report has been relabeled.

## 2. The actual ten-query model

The eight original left RMS queries are at intervals
`(471,472,473,475,477,479,480,481)` with fraction
`0.17267316464601146`. Two additional queries are the original
collocation midpoints473 and477, with fraction one half. Each query
contains all 2048 original physical angles. A repeated interval with
different query kind remains two separate groups.

The compiled B has shape `20480 x 236036`, with local shape
`20480 x 4059`, and occupies 111,247,360 bytes. Its model identity is
`5ce5b6169334d9c07c4faccb387f42238a2004c5496649ea9d4f839235dde0eb`.
The original complete A construction made 88 Jacobian calls. B captured
only the original two needed chunks and retained twelve endpoint nodes
and twelve variants; it did not construct another complete Jacobian.
The original midpoint input is directly `state.middle[j]` at
`problem.mid[j]`, and its complete chain remains

$$
\delta y_m=\frac{\delta y_L+\delta y_R}{2}
-\frac{h}{8}(\delta f_R-\delta f_L).
$$

The existing complete nodal physical/control J/P factors, direct query
scalar-control derivative, exact inlet chart, and variable scaling are
all retained. The eight-query left-component model on this new base
has identity
`2f40fdeb134ce8bce4a0db22d3bb6c6183764f8d6b8bea98eb8010938e91410d`;
it is not represented as the previous base's seven-query model.

The actual implementation checks report:

| Check | Actual result |
| --- | --- |
| Maximum normwise B/B-transpose adjoint error | `2.031011484241313e-18` |
| Maximum local/full action discrepancy | `0` |
| Original complex chain, actual complete LSMR direction | `5.608182293534991e-13` relative |
| Original complex chain, seeded direction | `1.1567989937781275e-12` relative |
| Original implementation thresholds | `5e-12` adjoint/local; `5e-5` complex chain |

The original complete collocation verifier also reports independent
complex directional error `8.673617379884035e-19`. Its precise scope is
free inlet core and global controls only, with all interior physical
coordinate directions zero. It does not assert independent testing of
every interior physical column. The separate full B check does use the
actual complete saved LSMR direction, including its local physical
components and original nonlinear midpoint chain.

## 3. The measured direction, projection and repair

The original damped LSMR solve stopped with `istop=2` after 84 of at most
200 iterations. Its actual preconditioned normal norm is
`2.7926670047964158e-5`, while the original unpreconditioned regularized
gradient norm is `323.36371806863497`. The raw directional derivative
is `-1.1005839959588257`, with damped-model decrease
`0.5502920274269889`. The two residual norms describe different
coordinates; stopping was not caused by the iteration limit. The
reported LSMR time is `6.972368441000015` seconds.

The local C-metric Hildreth projection used its unchanged 200-sweep
bound. At that bound its normalized primal violation was
`9.678286402437591e-7`, maximum dual-coordinate update
`2.0448318627738077e-5`, local projection objective
`0.054698217786970864`, local stationarity norm
`7.367953387913228e-15`, and complementarity sum
`1.3567264728901003e-6`. These are local projection diagnostics, not
the complete damped-model KKT quantities.

Before radial repair, 132 of the original 20,480 slacks were negative,
with minimum `-0.0011849360167310516`. The actual aggregate repair
factor was `0.7089606218412714`. A second rounding-level repair was
recorded after the first still left two tiny negative slacks; the final
all-row minimum is `1.1796119636642288e-16`. The same-model feasible
segment minimization selected parameter1 with no further repair.

| Selected direction quantity | Actual result |
| --- | --- |
| Actual complete-model directional derivative | `-0.652258821004469` |
| Damped-model decrease | `0.41493569167282296` |
| Squared weighted A-action | `0.2122222444366802` |
| Damping penalty | `0.2624240142266118` |
| Scaled-direction norm | `0.0018973088089223717` |
| Maximum coefficient direction | `0.0001407662622572` |
| Original full model gradient norm | `321472.92732217215` |
| Selected zero-dual posterior expression E | `708812.3662625964` |
| Original feasible-ray backup model decrease | `0.00012299847072337207` |

The selected direction is a verified descent candidate, not a
complete-QP optimum. The displayed zero-dual model bound is loose and
does not become a scientific BVP gate. The penalty does not enter the
actual nonlinear merit. Its weights remain fixed throughout this
model's real trials.

## 4. All actual trials and the nearest remaining limitation

Every trial had valid original nodal RHS values, valid boundary values,
the unchanged positive rho guard, exact inlet relations, and exactly
constant core and control states. The original midpoint outcomes are:

| Alpha | Original bad midpoint RHS intervals | Outcome |
| --- | --- | --- |
| `1` | `475,476,477,482` | Rejected |
| `1/2` | `475,477` | Rejected |
| `1/4` | `472,473` | Rejected |
| `1/8` | `475` | Rejected; all ten selected grids positive |
| `1/16` | None | All original nodes, midpoints, both RMS grids and rho checks pass |

The original observer records finite midpoint input arrays at all these
bad points and nonfinite original physical RHS rows. It evaluates the
original beta-squared expression on the saved original midpoint input,
without rerunning the whole flow or changing the original finite flag,
residual bytes or acceptance decision.

At the nearest rejected step `1/8`, the only bad midpoint is:

| Quantity | Actual value |
| --- | --- |
| Interval and kind | `475`, original collocation midpoint |
| Station | `1.2072539807467981` |
| Endpoint stations | `1.2051920955041622`, `1.209315865989434` |
| Original beta-squared minimum | `-0.09677364082856954` |
| Reported angle | index0, phi0 |
| Negative sampled angles | 6 of 2048 |
| Scalar a/ap/app | `1.1888761711331595`, `-0.16602747765333536`, `-2.4653028169274553` |
| Curvature at reported minimum | `0.1333474899866362` |

At that same actual step the newly selected left RMS471 minimum is
`0.021807211900929158`; selected midpoint473 and477 minima are
`0.3800683240512349` and `0.8419239213610225`. All ten original angular
grids are strictly positive. Thus the nearest rejection is neither
RMS471 nor one of the two previously protected midpoint grids. There
is no completed original all-RMS evaluation of this rejected state,
because its original midpoint gate already failed; untested RMS
queries are not asserted valid there.

The larger-step records also retain real nonlinear limitations on
already selected queries. At `1/4`, selected midpoint473 has minimum
`-0.0752322784144226` at angle98 while the selected linear-beta minimum
is `0.005051301703614121`. At `1/2`, selected midpoint477 has minimum
`-0.08048621783258247`. At alpha1 several selected RMS grids also have
negative real margins. These observations prevent interpreting the
linear reserve as a nonlinear feasibility certificate at unit step.
They do not alter the nearer, measured midpoint475 limitation.

## 5. Accepted real step and new nonzero boundary height

For this model, after refreshing the fixed weights at its actual
request32 parent, the initial merit is `44.36981782700075`. This differs
from the preceding model's final merit because its weights were fixed
at an earlier base. The following decrease is measured within this
one model, not by subtracting merits from different rounds:

| Accepted-step quantity | Actual result |
| --- | --- |
| Alpha | `0.0625` |
| Initial fixed-weight merit | `44.36981782700075` |
| Actual final merit | `44.32940101648062` |
| Actual decrease | `0.040416810520135016` |
| Predicted unregularized decrease | `0.04035167974161392` |
| Actual-to-predicted ratio | `1.001614078495323` |
| Physical collocation maximum | `0.007110378190224274` |
| Complete affine boundary maximum | `8.439522038007604e-8` |
| Original uniform-phi rho minimum | `0.16604058243274977` |
| Inlet and constant-row residual maxima | `0`, `0` |
| Invalid original left/right RMS queries | `0 / 0`, with 698 stations each |

The selected original angular minima at this accepted step are:

| Kind | Interval | Minimum beta-squared | Angle index |
| --- | --- | --- | --- |
| Left RMS | `471` | `0.022234411943400034` | `0` |
| Left RMS | `472` | `0.20403469654241613` | `0` |
| Left RMS | `473` | `0.6078231588131409` | `948` |
| Left RMS | `475` | `0.5601938920887262` | `0` |
| Left RMS | `477` | `0.49402936496015015` | `0` |
| Left RMS | `479` | `0.5240666120793167` | `0` |
| Left RMS | `480` | `0.005593722766205733` | `0` |
| Left RMS | `481` | `0.09071687054788069` | `0` |
| Collocation midpoint | `473` | `0.3864762681003041` | `0` |
| Collocation midpoint | `477` | `0.8729004506058384` | `0` |

The three independent real directional merit slopes are
`-0.6522588358848225`, `-0.6522587545987335`, and
`-0.6522588411428387`, versus model slope `-0.652258821004469`.
The corresponding full weighted-vector relative discrepancies are
`6.02241796532824e-5`, `8.561280949869294e-5`, and
`0.00018337238421505856`; machine-precision vector agreement is not
claimed from this readout.

The new native height begins

```
[3.6219698038466e-14,
 2.3688482459881996e-14,
 1.4557399408649173e-14,
 8.319859117048702e-15,
 4.426797265869582e-15, ...]
```

All 112 entries are retained in the actual warm and fresh response.
The three global scalar parameters are

```
[-1.8494475003754575e-19,
  7.043481502525152e-20,
 -1.3793380005938907e-19]
```

The new height is not equal to the real completed zero-H anchor and is
not rounded to zero. The fresh complete Rphi boundary finite-difference
check uses that genuine complete T112 zero-H Jacobian as an explicitly
affine model. It reports fourth-order Richardson relative error
`9.255484210257807e-10`, below the unchanged `5e-5` threshold;
second-order error `9.883403864216294e-6` contracts. It uses no
`ready.linearD` replacement. A true nonlinear native solve at the new
height, a new native Jacobian, and final true-tail audit remain unpaid.

## 6. Original-byte and source verification

Read-only byte verification checked all 94 domain NPZ files and their
594 NPY arrays, including file hashes, shapes, dtypes and raw array
hashes. All ten B/Gamma/Pi groups and the complete beta array reassemble
to their recorded whole-array hashes. The frozen metadata recipe
reconstructs the recorded model SHA. Original endpoint J/P factors are
bound to their exact original A chunks; the two saved midpoint subsets
match the original middle-array bytes.

Seven original observer reports, nine observer NPZ files and 27 raw
arrays match their recorded hashes, including original NaN-containing
RHS bytes. Every observed finite flag and residual byte-identity check
is unchanged. The actual parent32 warm/status, complete producer
subtree, mesh, states and RHS match the B base exactly. All 22 current
producer source hashes and the union of 26 producer/FD source hashes
match their frozen files. The saved full LSMR direction is the same
actual direction passed to the full complex B check. No solver,
matrix product or new scientific diagnostic was run locally for this
verification.

The principal artifact-relative records are:

| File | SHA256 |
| --- | --- |
| `ten-query-warm/model-000.json` | `ac08cdc980c2b8d6b3c0f1bfb48c59ae93d0841179b6b5264fca236ba5997b6d` |
| `ten-query-warm/optimization-intent.json` | `080f8d2de61e4bc66b67649e7bdb3b9d89cb7eaf7501e3797c86e0b54656ec0e` |
| `ten-query-warm/direction-00.json.gz` | `247fbf8bd3c44c34244df3daf2f8790421e4573eb898fcf17483a9e2c5432223` |
| `ten-query-warm/full-angle-operator-check.json` | `f96ba5c43ae2bedc8b3cce8aa51a29e78ff551a8282bcf334d94ad68620a4594` |
| `ten-query-warm/domain-operator/manifest.json` | `54d90b2521bc538bf12f65234cc9cf4074db776532ed217c0ac3857e61af686a` |
| `physical-response/response-check.json` | `39f7731b244603932600fa61b838cd8977b2fb72d915e015136eb839d84fde7b` |

## 7. Concrete continuation from the actual saved field

The next independent optimizer variant can add only the full original
midpoint475 angular grid to the existing eight RMS and two midpoint
grids, continuing this new warm and paired status. Both endpoint nodes
of midpoint475 are already in the twelve-node capture, so this addition
needs neither a larger local node set nor another complete Jacobian.
It must use the original saved midpoint base and the complete nodal
J/P chain, with typed query identity and source provenance distinct from
the frozen ten-query implementation.

The actual evidence supports testing that one addition. It does not
support adding unobserved queries, changing lambda, increasing LSMR or
projection limits, removing the original nonlinear backtracking, or
claiming the larger-step selected-query nonlinear failures have been
resolved. The original complete trial, both RMS rules, rho guard,
boundary equations and fresh FD remain necessary.

The frozen original warm engine explicitly requires `iterations=1`
and saves `warm-001.json.gz`; it is not an existing multi-model loop.
If a later accepted warm supports several consecutive models with the
same query set, the unchanged entry can be run sequentially in separate
directories, binding each preceding actual warm/status and preserving
each producer subtree. Each model must refresh and then hold its own
weights fixed, retain every original gate, and save its actual result.
Passing a larger `iterations` value to the frozen engine would fail its
declared interface and is not a continuation mechanism.
