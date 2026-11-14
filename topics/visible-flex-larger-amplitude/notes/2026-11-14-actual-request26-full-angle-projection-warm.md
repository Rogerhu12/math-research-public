# Actual request 26: full-angle projection produces a larger verified warm step

## Run and actual saved field

Public request 26 ran on source
`2a251065ca5ebbccc0c5571227af737fa6b65961`, run `43608931469`, job
`132489481146` (`Mainline angleprojection`). The warm step, its fresh
complete affine Rphi derivative check, artifact upload and ordinary
publication all finished successfully. The warm producer reported
251.385146735 seconds and the derivative check 24.208709145 seconds.

Artifact `14119626920`, `visible-mainline-angleprojection-43608931469-1`,
contains 108,924,237 ZIP bytes, SHA256
`e0c1e49bb2d075bfcfbe7cfbf05a384aa74b152b1b2bb6e230f45b00c60f8a24`.
The actual input is request22's latest complete warm, SHA256
`03ca9477cbb759cdbf07117f2540aa51dbe07545985c957289d0f0a3079f4be8`.
The new `full-angle-warm/warm-001.json.gz` is 4,711,738 bytes, SHA256
`4e2ee245a3c931210eed8a9a67a4202397eb709b3e5aacc7271418d76d4098c1`.

This new field remains explicitly `success=false` and
`new_coupled_finite_acceptance=false`. It is a real improvement of the
complete unaccepted warm; it is not an accepted nonlinear DN solution or
a closed surface. No native tail was called by this run.

The unchanged source hashes are the ones in
`2026-11-14-full-angle-feasible-projection-warm-interface.md`: operator
`af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7`,
warm entry
`7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152`,
and response entry
`90e7addef0e03375b40968f54fb55ce85dc02c3f5cb123f895f100af663f2e92`.

## Complete actual operator checks

The captured domain model is
`8884784feeb1f49e942800eee259e5618a7462d30042de5075eef1dac5e56c67`.
The original complete A construction made 88 Jacobian calls; the B module
captured selected endpoint factors from original calls 59 and 61, each
with 17 nodes. There are nine selected nodes and nine actual stored
factor variants. Node480's two original chunk copies are byte-identical.

The complete B has 10,240 rows, 236,036 global columns and 3,045 possible
local columns. The actual compiled row blocks occupy 55,623,680 bytes.
No global dense B was constructed. All five original N2048 physical-angle
grids, both endpoint physical/control chains and direct query scalar
derivatives were retained.

The maximum normwise adjoint error is
`2.272315893518922e-18`; local/full forward and transpose comparisons have
zero reported differences. Against the independent original nonlinear
complex Hermite chain, the actual complete LSMR direction has relative
error `6.56268259860486e-13`, and the independent seeded direction has
relative error `1.08773571324249e-12`. These pass the original
implementation thresholds. The actual LSMR direction, not a substitute
or a global-only direction, is bound by its stored array hash.

A subsequent read-only identity check verified all 50 domain-operator
files, all 305 stored NPY array identities, and each full B/Gamma/Pi block
reconstructed from its actual stored byte parts. The complete base
state/RHS/mesh/scale, beta vector, model hash and source ledger agree.
No Jacobian or numerical solver was rerun for these byte checks.

## LSMR, finite projection and the actual selected direction

The single original unprojected model kept lambda270, the complete
original residual and the declared fixed weights. LSMR stopped at
iteration80 with `istop=2`, within its maximum200 budget. Its reported
normal residual is `2.6115438468187817e-5`; the independently evaluated
preconditioned normal is `2.6115438468088016e-5`. The unpreconditioned
original regularized gradient norm is `345.6423090505119`. These remain
different quantities. LSMR's actual raw direction has slope
`-1.0711274502321086` and damped-model decrease `0.5355637512713852`.

The local Hildreth projection used all `5 * 2048` halfspaces with the
fixed one-half base-margin reserve. It completed its 200-sweep limit,
**not** its `1e-10` stopping tolerance. The last normalized primal
violation is `1.0029902579184726e-6`; the largest dual-coordinate update is
`2.7532736746986586e-5`. The original unnormalized inequalities still
include 74 negative slacks, with minimum `-0.000849456142691607`, before
repair. The local projection objective is `0.024236694929915426`.

Projection-coordinate stationarity is `5.1899836458626795e-15` in L2.
Its complementarity sum is `1.9151344252164855e-6`, and maximum absolute
complementarity product is `2.0035813733719944e-7`. These multipliers and
stationarity concern the declared local C-weighted projection; they are
not KKT data of the complete R265 quadratic.

The actual radial repair and selection were:

| Candidate | Actual repair factor | Damped-model decrease / selection |
| --- | ---: | --- |
| Original-ray feasible backup | `6.499225294503624e-6` | `6.961475996012835e-6` |
| Locally projected candidate | `0.8606834326670906` | Selected by the feasible-segment minimization |
| Final segment combination | `1` | Segment parameter `tau=1`; decrease `0.4990204300440543` |

Thus this run actually selected the repaired projection, not the tiny
original-ray fallback. The final full 10,240-row slack minimum is
`1.3530843112619095e-16`, with zero negative rows. The actual selected
direction has slope `-0.8769409413632383`, squared weighted residual
action `0.33801519217533316`, damping penalty `0.4178258304630349`, and
scaled direction norm `0.00239405364879166`.

The selected direction's complete damped-model gradient norm is
`166834.19891868532`. The diagnostic zero-dual R265 bound is
`190902.9487574723`, so no near-optimality of the complete constrained
quadratic is established. The negative directional derivative, positive model decrease,
all-row feasibility, and the later real nonlinear decrease are the
claims actually used.

## Original backtracking and the next actual domain limitation

The direction was tested with the unchanged original nonlinear
backtracking and all original gates. At alpha1, 1/2, 1/4 and 1/8, all
nodes are valid but the numbers of invalid midpoints are respectively
8, 5, 3 and 1. Those records contain counts, not the complete midpoint
locations; no particular midpoint is inferred from them.

The next three trials show the relevant remaining limitation:

| Alpha | Node / midpoint failures | Actual fixed-weight merit | Actual / predicted ratio | Original two-RMS result |
| --- | --- | ---: | ---: | --- |
| `2^-4` | 0 / 0 | `44.39021619489074` | `0.9995801037337599` | Left RMS intervals472 and481 invalid; right RMS valid |
| `2^-5` | 0 / 0 | `44.41714278968988` | `0.9985290905945535` | Left RMS interval481 invalid; right RMS valid |
| `2^-6` | 0 / 0 | `44.43069444899323` | `0.9990257930877813` | Both original RMS sets valid; accepted warm step |

At `2^-4`, the two actually reported left RMS minima are:

| Interval | Physical phi | Actual beta squared |
| --- | ---: | ---: |
| 472 | `0` | `-0.17651823084561058` |
| 481 | `3.107845076256309` | `-0.08892785650304247` |

At `2^-5`, interval481 alone fails, at phi0 with beta squared
`-0.008204128545981293`. At these two rejected steps **every angle in all
five modeled queries is actually positive**. The remaining RMS failures
are neighboring intervals outside the five-query set, rather than an
omitted angle within that set.

At the accepted `2^-6` step, the five modeled actual minima are:

| Interval | Minimum actual beta squared | Original angle index |
| --- | ---: | ---: |
| 473 | `0.0005257483169005539` | 0 |
| 475 | `0.5930339726704557` | 0 |
| 477 | `0.522823660008334` | 0 |
| 479 | `0.5545465562835165` | 0 |
| 480 | `0.00598628254080491` | 1013 |

The model's merit decreases from `44.44434208099914` to
`44.43069444899323`, a genuine decrease of `0.013647632005913124` under
the **same fixed weights**. Its prediction is `0.013660940588662008`.
This model's initial merit differs from request22's final merit because
the weights are refreshed at the new model base; values from the two
models must not be directly subtracted.

The three independent real directional merit slopes are
`-0.8769408920272781`, `-0.8769410046483017` and
`-0.8769411786602177`, agreeing with the sign and size of the actual
model slope. Their vector finite-difference relative discrepancies range
from `6.472395851720259e-5` to `1.645125885167201e-4`; they are recorded
diagnostics, not a claim of machine-level full-vector convergence.

## New warm and genuinely rerun boundary check

The saved new field retains all699 nodes, M112/N2048, exact constant
core/controls and exact inlet identities. The input chart projection
change was zero. The accepted warm has physical collocation maximum
`0.007110525392946708` and complete affine boundary maximum
`9.449358469183357e-8`. These do not satisfy the original final BVP gates.
The uniform4096-angle rho guard remains positive, with minimum
`0.16604058243275`.

Its actual scalar controls are
`[-9.448605769266043e-20, 2.866721349892266e-20,
-8.587720312516577e-20]`. Its stored material height is nonzero; its first
component is `4.891640492688009e-15`. It is not thresholded into the
completed zero anchor and has no newly accepted native solution.

The new physical response file binds the actual new warm SHA and actually
passes the unchanged Richardson full-boundary check: maximum fourth-order
relative error `8.658996438962446e-10`, original threshold `5e-5`;
second-order maximum `9.883411689970644e-6`, with the recorded contraction
conditions satisfied. It explicitly says no nonlinear native solve at
the current H occurred.

## Principal output identities and immediate continuation

| File relative to the artifact root | SHA256 |
| --- | --- |
| `full-angle-warm/model-000.json` | `25cc92bf220aa8645ef6a1b8983da19ef9ae422eb16d029d4e5482c2c02f62eb` |
| `full-angle-warm/driver-status.json` | `b607c17d5a8a3c9f6ef96899a90dad1d6b59b7a550b78a539f42ac5c659ae64d` |
| `full-angle-warm/direction-00.json.gz` | `01b02e8b403f5c22618b4ce12630c0025d10b0877cdaf059b3f58800dac5e18e` |
| `full-angle-warm/all-angle-selection-candidates.json.gz` | `c504e1b7a9341edb02f0c19881b4ec67e0121251b160704cc11fc20a4a4c05c1` |
| `full-angle-warm/all-angle-linear-margins.json.gz` | `8a620bb2ff143be7327ccdaa5f9ec1db390012bae335ea30b19c6530ff1b5f67` |
| `full-angle-warm/full-angle-operator-check.json` | `6fcc057cdd93544f80adda93627771631e5f829c7d9deb401c26a1fc61a803c9` |
| `full-angle-warm/domain-operator/manifest.json` | `b06b88f5d426c84a6e7697d561caa7cc68e523d6414d2d6d647cc08e9acdac11` |
| `physical-response/response-check.json` | `340f51dcadf735efddb5ad6ed733f77b9dd4b2701a16641fc68d0c84f43f7d5c` |

The next bounded experiment can start from this actual new warm and add
the two actually observed neighboring left-RMS queries, intervals472 and
481, retaining **all** original angles at each. This adds finite
algorithmic inequalities, not new BVP equations or relaxed scientific
gates. The original complete nonlinear backtracking must remain, since
finite linear feasibility still does not certify other queries or a
unit nonlinear step. No midpoint location or unmeasured continuous-angle
conclusion is supplied by this record.
