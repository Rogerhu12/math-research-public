# Actual request 27: seven-query step passes; nearest failure is a midpoint

## Actual run and saved field

Public run `43610469627`, job `132494273063` (`Mainline sevenprojection`),
used source `b92d4b20b9dc8c81ed94977c2b0807e5281a4b8b`. It was created
at 2026-11-14 15:29:45 UTC. The actual warm step, new complete affine Rphi
derivative check, artifact upload and ordinary publication all succeeded.
The warm producer reported 200.081209107 seconds and the new derivative
check 20.267288233 seconds.

Artifact `14119758437`, `visible-mainline-sevenprojection-43610469627-1`,
is 143,121,398 ZIP bytes, SHA256
`d610b3d9b9507a4d7a72e6a36659ef0d7d595847543a7d8b4b7018afa4fc334e`.
Its input is the actual request26 warm, SHA256
`4e2ee245a3c931210eed8a9a67a4202397eb709b3e5aacc7271418d76d4098c1`.

The new `seven-angle-warm/warm-001.json.gz` is 4,717,570 bytes, SHA256
`f73dfc81b6247363e449be16f142e552f857ec38846f8bff0954f0ca76b55422`.
It retains all699 nodes, M112/N2048, the complete original scalar formula
and all actual constant controls. Its flags remain `success=false`,
`new_coupled_finite_acceptance=false` and no closed-surface claim. This
run did not call a native tail.

## Full provenance and operator scope

The seven-query entry has SHA256
`f6598a5e4738f6c2c310eccc9fd791b68c3731ad3fc3adfd83414450d95c8394`;
the new response entry has SHA256
`d05df1fd00eab33774ad34ff15a0988250fc49c6aca474656add0cc716d48c6e`.
The request26 engine and captured domain operator remain unchanged.
The actual `driver-status.identity` equals the saved optimization intent.
The complete `resume_producer` subtree matches request26's original
optimization-warm object, including its old five-query identity.

The current query tuple is `(472,473,475,477,479,480,481)`, each at the
original left RMS fraction `0.17267316464601146` and all2048 original
physical-phi angles. The actual finite B has 14,336 rows, 236,036 global
columns and 3,721 local columns. Its compiled row arrays occupy
77,873,152 bytes. The model hash is
`4ac1f9e9f798e27f5defa50d1d226cb2ab4e00c165ee1fd7599868182d76f85f`.

The original A construction again makes 88 Jacobian calls. The selected
factors come from calls59 and61, with eleven actual nodes and eleven
stored variants. Node480's original two-chunk factors are byte-identical.
The maximum normwise adjoint error is `7.37099045789449e-18`, with zero
local/full forward and transpose discrepancies. The independent original
complex Hermite-chain check has relative error
`6.548694215417781e-13` for the complete actual LSMR direction and
`2.9046166400496875e-13` for its independent seeded direction.

Read-only byte checks verified all68 files listed in the domain manifest,
all421 NPY array identities, and each complete B/Gamma/Pi/beta block
reconstructed from the saved parts. The checked actual-direction hash is
the one from this run's original LSMR direction. No scientific matrix or
solver was recomputed during these source and byte checks.

## Projection and actual selected model direction

The original unconstrained LSMR again stopped at iteration80 with
`istop=2`, within its maximum200 budget. The independently evaluated
preconditioned normal is `2.593337736108191e-5`; the original full
regularized gradient norm is `346.2106570621937`. Its actual raw slope
is `-1.057963828363735`, and its damped-model decrease is
`0.5289819399949941`. The value of lambda remains270.

The C-weighted Hildreth projection performed its 200-sweep limit, not a
converged-to-tolerance solve. Its final normalized primal violation is
`8.646397539029539e-7` and largest dual-coordinate update is
`2.5463228987807757e-5`. Before radial repair, the original inequalities
have 100 negative slacks and two rounded zeros, with minimum
`-0.0007361237768173656`. The local projection objective is
`0.025477856232286863`; projection-coordinate stationarity is
`4.638173515426016e-15`. These remain diagnostics of the local projection,
not KKT data for the complete original quadratic.

The projected candidate is repaired by the actual factor
`0.8216634644079532`. All14,336 resulting slacks are nonnegative, with
minimum `1.700029006457271e-16`. The feasible-segment minimization again
chooses `tau=1`; no further composition repair is required. The original
ray backup would have required factor `8.098292582263865e-6` and supplied
only `8.567665931670008e-6` model decrease, so the selected direction is
the genuinely useful repaired projection.

For that selected direction, the actual slope is
`-0.8236822441205771`, squared weighted action is
`0.30238443132089443`, damping penalty is `0.3752769293415319`, scaled
direction norm is `0.002268883354914993`, and full damped-model decrease
is `0.48485156378936395`. Its complete model gradient norm is
`210708.03084308124`; the zero-dual bound at this same point is
`304512.1691479347`. No complete constrained-model optimality is claimed.
R267 explains how a different evidence point may provide a better
posterior, but this producer did not evaluate that new two-point ratio.

## Original nonlinear trials and observed limitation

The unchanged original backtracking produced:

| Alpha | Node failures | Midpoint failures | Original seven-query angular readout | Outcome |
| --- | ---: | ---: | --- | --- |
| `1` | 0 | 6 | Several modeled queries also invalid | Rejected |
| `1/2` | 0 | 2 | Several modeled queries also invalid | Rejected |
| `1/4` | 0 | 3 | All original angles at all seven queries positive | Rejected at original midpoint domain |
| `1/8` | 0 | 1 | All original angles at all seven queries positive | Rejected at original midpoint domain |
| `1/16` | 0 | 0 | All seven query grids positive | Full original left/right RMS checks pass; accepted warm step |

The records preserve the actual midpoint **counts**, not the complete
bad-midpoint indices or angles. In particular, the nearest rejected
`1/8` trial has one actual bad midpoint, but this run does not identify
its location. The original RMS tests are not reported as having run on
those nonfinite trials. There is no newly observed left-RMS query here
that would justify adding an eighth such constraint by assumption.

At the accepted `1/16` step, both original RMS sets have zero failures.
The actual seven modeled minima are:

| Interval | Minimum actual beta squared | Angle index |
| --- | ---: | ---: |
| 472 | `0.20990492975603814` | 0 |
| 473 | `0.0028689551401551716` | 0 |
| 475 | `0.5774031471672008` | 0 |
| 477 | `0.5090915734341173` | 0 |
| 479 | `0.5400729789850396` | 0 |
| 480 | `0.005829670900736383` | 0 |
| 481 | `0.093433826211479` | 0 |

Within this one fixed-weight model the actual merit decreases from
`44.43133020235467` to `44.380293912301596`, a real decrease of
`0.05103629005307653`. Its predicted unregularized decrease is
`0.050889545665112446`, giving actual/predicted ratio
`1.0028835861284704`. This model's weights were refreshed at its own
base: its initial merit must not be directly compared by subtraction
with request26's final merit.

The three independent real directional merit slopes are
`-0.8236821619433954`, `-0.8236823622809197`, and
`-0.8236823803997595`. The corresponding vector finite-difference
relative discrepancies range from `7.084772903498182e-5` to
`1.7631075861094747e-4`; these are diagnostics and do not assert machine-
level full-vector convergence.

## Preserved unaccepted scope and fresh FD

The saved new warm has physical collocation maximum
`0.007110456794261092` and complete affine boundary maximum
`8.962976439976726e-8`. These remain above the original final BVP
requirements. The original uniform4096-angle rho guard is positive,
with minimum `0.16604058243274977`. The inlet/constant-state residuals
remain exactly zero in the reported coordinate representation, and the
input chart projection change was zero.

The actual scalar controls are
`[-1.3644975490234042e-19, 4.8098725091519526e-20,
-1.0960144482597582e-19]`. The stored native-height trace is nonzero; its
first component is `1.9911248007634974e-14`. It is neither thresholded to
zero nor accompanied by a completed native solution from this run.

The fresh physical response binds the actual new warm SHA and passes
the unchanged original Richardson check. Its maximum fourth-order
relative error is `7.819442926433809e-10`, below the original `5e-5`
implementation threshold. The second-order maximum is
`9.883399520608296e-6`, and the recorded contraction checks pass. The
response explicitly declares no nonlinear native solve at the current H.

## Principal artifacts and immediate continuation

| File relative to the artifact root | SHA256 |
| --- | --- |
| `seven-angle-warm/model-000.json` | `d2489e0499489da552ba10bbe7cb34b7284ea7e10a24c4496a32e9f8efc36442` |
| `seven-angle-warm/driver-status.json` | `e8ca7cfde2e1bc247b29b595ade3ab26c1599f62784aad223db65ba3d650a765` |
| `seven-angle-warm/optimization-intent.json` | `10a7662bbf50673ae938c49a40621d91c7b87651698d912bf7c5c272024e23a8` |
| `seven-angle-warm/direction-00.json.gz` | `6b87b272375e08f7cc597cf23f9ae60de11443dbb327766c8747ee0c5243550e` |
| `seven-angle-warm/all-angle-linear-margins.json.gz` | `e2ccee7768043b9ab11fd5fb53a152168473533835f726019ebdacde4e662507` |
| `seven-angle-warm/domain-operator/manifest.json` | `5a431c41bc6508a2556321682e3157bbff59dff6d85122c10285d12536d8ed0c` |
| `physical-response/response-check.json` | `cccf0e163ed0febeae7862c9668652746966bf108fcf1b3fa41d4990f947dd9c` |

The direct next step is continuation from this actual warm with the same
seven-query algorithm. A read-only observer of the original returned
`middle` and `fm` arrays can additionally record actual bad-midpoint
indices, stations, original full-angle beta-squared values and source
state identities. Such an observer must not reevaluate the whole flow or
Jacobian, change the returned finite flag, or turn a diagnostic exception
into a scientific gate. It would provide the missing actual location
evidence while the same original solver and all original gates continue
to determine progress.
