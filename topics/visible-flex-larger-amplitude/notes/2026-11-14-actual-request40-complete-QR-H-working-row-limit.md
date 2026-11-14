# Actual request40: complete QR inverse, a better feasible direction, and the working-row limit

Request40 actually constructed the complete regularized block QR,
used it for the unconstrained center and sixteen original inequality
rows, and selected the resulting complete-H alternative over the
retained C-projection candidate. Its first original nonlinear trial,
alpha1, passed every original node, midpoint, both RMS grids and rho
guard. The fixed-weight merit decreased by
`0.012013409370396744`, and the fresh complete affine Rphi FD passed.

The remaining model limitation is concrete. The final sixteen-row
working problem had original full stationarity residual
`4.930496854039628e-9` and tiny working-row violations, but its full
24576-row slack still had1804 negative entries. The most negative
stored slack was on nonworking angles of original midpoint473. The
helper stopped at its sixteen-row budget, then applied a global
radial factor `0.00959007921159372`. Thus alpha1 applies to an already
repaired direction. Neither the inverse accuracy nor the successful
trial establishes full quadratic-program optimality, an accepted
full BVP, or a new nonlinear native tail.

## 1. Actual run, package, and exact parent

| Item | Actual value |
|---|---|
| Public run | [43621054216](https://github.com/Rogerhu12/math-research-public/actions/runs/43621054216) |
| Warm lane and job | `twelvequeryqr`, `132526640205` |
| Source commit | `8a59ebd9d241bf424e9ba1c272e22b76264a034c` |
| Artifact | `14123843853`, `visible-mainline-twelvequeryqr-43621054216-1` |
| Complete ZIP size | 389895464 bytes |
| Complete ZIP SHA256 | `8f83ed58585685a7833b55c59bd407076ee012d29dc732a5d08a0d4e5ac3a3f6` |
| Warm elapsed time | `322.436215515` seconds |
| Fresh FD elapsed time | `16.64749135200003` seconds |

The actual warm, FD, artifact and publisher steps completed
successfully. The result remains an unaccepted optimization warm.
The exact incoming field is the same actual request37 parent used
by request39, not request39's newly saved output:

| Parent file | SHA256 |
|---|---|
| `eleven-query-warm/warm-001.json.gz` | `dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8` |
| `eleven-query-warm/driver-status.json` | `37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0` |

All699 mesh nodes, the453 augmented state entries per node, original
saved RHS values, complete scalar formula, accepted96/prepared699
and true-zero-T112 bindings, and the complete parent producer
subtree were retained. The original exact-coordinate inlet
projection still reports zero difference. The new schema is
`exact-constraint-twelve-query-complete-QR-H-alternative-warm-v1`.

The frozen implementation is described in
[the complete QR warm interface](2026-11-14-twelve-query-complete-QR-warm-interface.md).
[R268](../results/R268-complete-regularized-chain-border-QR.md) proves
the exact chain-and-border energy identity. It does not replace
this run's original-operator residual measurements or certify the
floating factorization.

## 2. A controlled comparison with the original C candidate

The complete inequality model remained the twelve typed query grids:
nine left-RMS intervals470,471,472,473,475,477,479,480,481 and the
three original collocation midpoints473,475,477. Every grid contains
all2048 original physical-phi angles. The left fraction is
`0.17267316464601146`; midpoint inputs are the original returned
`state.middle` and `problem.mid` values.

The full B shape is24576-by236036. Its local-column union is
24576-by4397, with thirteen physical nodes470–482 and the original
three global controls. The compiled B rows occupy133496832 bytes.
The model identity is

`18a5ad26655ec12a2c19eb0887a1895ee2bfeadf84f6fac9695f83d2a9f7977b`.

All111 compressed domain NPZ files are byte-for-byte identical to
request39's corresponding files, including all708 preserved arrays,
the complete B/Gamma/Pi groups, base state/RHS, and original endpoint
J/P capture. This is a direct saved-byte comparison. The parent and
source formulas also agree. Within request40 the C and H choices
share the same actual A object, b, damping, B, c and fixed weights;
the complete-H extension constructed no second full Jacobian.

The original A construction made88 Jacobian calls. B captured only
the original calls59 and61, retaining13 endpoint variants. Shared
node480 has matching J/P bytes across those original chunks. The
actual original B checks remained:

| Check | Original Actions value |
|---|---:|
| Maximum normwise adjoint error | `5.338229723239566e-18` |
| Maximum local/full action discrepancy | `0.0` |
| Actual raw LSMR direction versus original complete complex query chain, relative | `1.0737010004479039e-12` |
| Seeded local direction versus original complete complex query chain, relative | `9.311810238217192e-13` |
| Original constrained collocation complex-direction relative error | `8.673617379884035e-19` |

The last check varies free inlet core and global controls with
interior physical test coordinates zero; it is not a claim to have
tested every interior collocation direction. The B test separately
uses the complete actual236036-component LSMR direction.

Only the baseline C-projection correction is restricted to4059
coordinates, physical nodes471–482 plus the three global controls.
Its offset retains the complete outside action

$$
c_{\rm eff}=c+B_{\rm out}(z_0)_{\rm out}.
$$

The complete-H candidate is free in all236036 original exact
coordinates, including node470, the free inlet core, and global p.
The local C support is not silently imposed on H. The C baseline,
its negative effective offsets,200 Hildreth sweeps, full-vector
radial repair, and same-model selection were all retained. Its
reported objective and direction agree with the repeated C result
from the same parent in request39. See
[the actual39 note](2026-11-14-actual-request39-fixed-support-projection-and-full-step.md)
for that baseline's incomplete local projection and strong repair.

## 3. What the complete QR actually executed

For the one fixed model, write

$$
f(z)=\tfrac12\|b+Az\|_2^2+\tfrac12\lambda^2\|z\|_2^2,
\qquad H=A^T A+\lambda^2 I,\qquad \lambda=270.
$$

The code factored the complete square-root chain with338 physical
coordinates per noninitial node and112 global border coordinates.
It retained every physical damping block, the global damping block,
all boundary rows and every pure-global QR remainder. No ridge,
clipping, physical mode deletion, or old PCG retry was used. The
optional QR column preconditioner was `none`, and the large factors
were not written as artifacts.

The actual factor report records all698 physical blocks completed
in `19.128500218` seconds, with1486451296 factor bytes. The outer
completion log records `19.128520082999955` seconds around that
operation; these are separate clocks. The factor-stage maximum
resident memory readout was3337860 KiB. Seventeen complete H-inverse calls
were made: one for the unconstrained center and sixteen for actual
original inequality rows. The first inverse's original H residual
norm was `6.355194653366658e-10`, with infinity norm
`3.4924596548080444e-10`, and relative residual
`6.290514339105675e-16`. The sixteen row-inverse residual norms
ranged from `8.856448815086289e-11` to
`3.5533993113497657e-10`; their relative residuals ranged from
`4.58100212305514e-16` to `7.141860016873343e-16`.
These are original A/AT readouts, not
factor-normal residuals or small reduced-Gram residuals.

The helper actually ran for `67.452024424` seconds, within its300
second helper budget and the original1200 second total budget,
with90 seconds reserved for original trials and preservation. Its
recorded helper action counts were A116, AT57, B101, BT54 and H17.
The separately counted frozen-source reference check added17 A and
17 AT actions, making133 A and74 AT actions in that combined scope.
Every actual same-vector supplied-versus-reference A/AT discrepancy
was0. The initial LSMR, baseline C projection, outer selector and
earlier implementation checks are outside that helper/reference
accounting scope; factor and triangular work are also explicitly
additional to its H-product cap. No
mandatory action was recorded after its deadline. The working-row
budget was16 and the final basis had18 columns. The stop reason was
`maximum-32-or-requested-working-row-budget`, not a timeout or an
inverse failure.

The raw LSMR direction was retained as the first full basis column.
It stopped after80 iterations with `istop=2`, below its200-iteration
cap. Its original complete gradient norm was
`313.12159761275774`, even though its preconditioned normal norm was
about `2.71739871418e-5`. The QR-refined unconstrained center had the
following separately saved full-model values:

| Quantity | Actual value |
|---|---:|
| Objective | `43.75480038530318` |
| Original full gradient/stationarity norm | `7.102228516064968e-10` |
| Minimum complete inequality slack | `-86.17193131547586` |
| Maximum relative primal violation | `9458.644526336902` |

Thus the accurate unconstrained center remained substantially
infeasible. An accurate inverse alone cannot supply the required
inequality-constrained direction.

## 4. The actual sixteen-row endpoint and the remaining rows

The working rows were added in this actual order:

`14336, 15349, 4096, 2048, 14358, 18432, 19434, 4118, 14379, 10240, 0, 16384, 8192, 12288, 10262, 15306`.

The final eighteen-column basis uses the actual A action in its full
H Gram. No approximate inverse Schur matrix replaced that Gram.
The final dual loop reached its allowed200 sweeps, with last maximum
H-normalized multiplier update `9.215704119060229e-18`, active
relative violation `9.689531898361632e-14`, and active predicted
minimum slack `-3.552713678800501e-15`. The original code does not
infer convergence merely from completing its sweep budget.

The final unrepaired working-subspace candidate had:

| Unrepaired quantity | Actual value |
|---|---:|
| Objective | `43.77648797207321` |
| Original merit derivative | `-1.0316450141188611` |
| Original damped-model decrease | `0.5159316789125015` |
| Original full gradient norm | `77.55960090773111` |
| Full stationarity norm with the actual nonnegative row multipliers | `4.930496854039628e-9` |
| Original complementarity sum | `7.629524153689826e-18` |
| Maximum absolute complementary product | `5.471441068190956e-18` |
| Complete24576-row slack minimum | `-33.72526277344046` |
| Negative complete slacks | 1804 |
| Maximum relative primal violation | `103.27442546992282` |

The stored minimum slack occurs at rows19413 and20437: query9,
original collocation midpoint473, physical angle indices981 and2005.
Neither row belongs to the sixteen-row working set. These locations
were obtained by locating the already recorded minimum in the
preserved original-slack array; no local B action, norm or model
solve was performed. The maximum relative violation is also an
original saved Actions value. Its separate argmax was not saved,
and this note does not identify the minimum-slack row as that
relative argmax.

This distinguishes the remaining issue from an inaccurate complete
inverse or an obviously unresolved working-row dual iteration.
The measured working-row stationarity/complementarity are small;
the omitted full inequality rows still fail. It does not prove that
thirty-two rows will suffice, or that the final nonlinear trial will
accept an unscaled working-set candidate.

## 5. Global repair, original C/H comparison and final model evidence

The last working-subspace candidate was globally scaled by
`0.00959007921159372`. The algebraic factor printed before the
implementation's floating safeguard was `0.009590079211593858`.
The complete repaired slack minimum was
`4.6629367034256575e-15`, with zero negative and zero zero entries.
All24576 rows were re-evaluated after repair.

This repair happened inside the complete-H helper. The later
original feasible-segment selector therefore recorded factor1 for
its incoming H candidate; that later factor1 must not hide the
earlier factor0.00959007921159372. The selector kept its repaired
raw-ray backup, whose factor was `0.00010571139027051392`, and used
the same complete quadratic to compare the two candidates. Its
segment derivative at the raw backup was
`-0.009778858608454143`, curvature
`9.278021121215138e-5`, and selected segment parameter1. The rounded
composition was checked again and needed no further repair.

The same-model C/H comparison reported:

| Actual feasible candidate | Complete damped objective |
|---|---:|
| Retained original C candidate | `44.29019464139972` |
| Complete-H alternative | `44.28257352354115` |

The selected label was
`bounded-complete-H-alternative-with-smaller-actual-model`. The
final direction bytes agree with the saved actual trial direction;
the C candidate was preserved rather than overwritten. The complete
H candidate's selected full-model readouts were:

| Selected quantity | Actual value |
|---|---:|
| Merit derivative | `-0.009893557403645597` |
| Squared weighted-J action | `3.996265646297161e-5` |
| Damping penalty | `5.489726173491213e-5` |
| Damped-model decrease | `0.009846127444546654` |
| Scaled direction norm | `2.744173569251269e-5` |
| Complete repaired slack minimum | `4.6629367034256575e-15` |
| Complete gradient norm | `1000593.511818494` |
| Complete stationarity norm with the saved repaired multipliers | `1000593.5117430527` |

The repaired multipliers are the same positive radial factor times
the nonnegative working-row multipliers. They are valid nonnegative
dual evidence, not a claim that repair preserved stationarity or
optimality. The small unrepaired residual and the large repaired
residual refer to different vectors and must not be conflated.

The [R267](../results/R267-two-point-damped-model-posterior-bound.md)
cross-point evidence retained the best raw-floating lower-bound
value `43.77648797207321`, attained by the unrepaired evidence
point. Against the selected feasible objective, the saved gap was
`0.5060855514679403`, with distance bound
`0.0037261746160578203`. The selected point's single-point E was
`6866854.428961571`; using that loose number alone would discard the
stronger independently retained evidence point. These are ordinary
floating diagnostic evaluations of the exact algebraic statements,
not validated lower bounds or floating enclosures. The complete
QP's optimality is not asserted.

## 6. The actual trial, every original domain, and the new physical field

The first original alpha1 trial was accepted as an optimization
warm. The original17-trial limit and actual domain checks were
unchanged; the remaining sixteen trials were unnecessary:

| Actual trial quantity | Value |
|---|---:|
| Fixed-weight merit before | `44.292419650985686` |
| Fixed-weight merit after | `44.28040624161529` |
| Actual merit decrease | `0.012013409370396744` |
| Predicted unregularized merit decrease | `0.009873576075414111` |
| Actual/predicted ratio | `1.216723229622038` |
| Original physical collocation maximum | `0.0071103080271700675` |
| Complete physical Rphi boundary maximum | `7.997334910447051e-8` |
| Original4096-point rho minimum | `0.16604058243274977` |
| Left/constant-row residual maxima | `0.0`, `0.0` |

All699 original nodes and698 original collocation midpoints were
finite. Both original698-point RMS grids, at fractions
`0.17267316464601146` and `0.8273268353539885`, had zero invalid
points. The boundary was finite, every trial RHS was actually
recomputed, and the core/control states were exactly constant across
nodes in the exact chart. The read-only midpoint observer recorded
no bad midpoints and confirmed unchanged original finite flags and
residual bytes in all three retained base/trial/RMS reports. No
observer gate was introduced.

The actual twelve full-angle minima after the accepted trial were:

| Query | Minimum original beta-squared | Angle index |
|---|---:|---:|
| Left-RMS470 | `0.11912933087532296` | 0 |
| Left-RMS471 | `0.021665384644629637` | 0 |
| Left-RMS472 | `0.14968931510937922` | 11 |
| Left-RMS473 | `0.28567213431874094` | 76 |
| Left-RMS475 | `0.14413367361447615` | 991 |
| Left-RMS477 | `0.177432589911644` | 54 |
| Left-RMS479 | `0.2555160925160963` | 1002 |
| Left-RMS480 | `0.005393898682581888` | 0 |
| Left-RMS481 | `0.08309555912750233` | 1013 |
| Original midpoint473 | `0.020554447707311296` | 54 |
| Original midpoint475 | `0.21574031299616914` | 22 |
| Original midpoint477 | `0.6563670928562213` | 54 |

Every row in each of these twelve actual2048-angle grids was
finite and positive. These saved-grid facts do not establish a
continuous angular domain bound or every unmodeled radial point.
The original full domain checks, rather than these twelve minima
alone, governed the trial.

The independent real directional diagnostic held the current
weights fixed and recomputed the complete nonlinear RHS/boundary.
For steps `1e-4`, `5e-5`, `2.5e-5`, its absolute/relative L2 errors
were `2.90750478205896e-5`, `5.9217868920590996e-5`,
`0.00011781495567941976`; independently evaluated merit slopes were
`-0.009893587673559523`, `-0.009893604797639455`,
`-0.009893542625150076`. These original diagnostic readouts were
preserved without turning them into new scientific acceptance gates.

This model's weights were refreshed at its actual request37 parent
and then fixed. The controlled C/H comparison is within this one
model; request39 used the same parent and its corresponding saved
B files. A future model from the new request40 warm will refresh
weights again. Its initial merit must not be subtracted from this
model's terminal merit as if those weights remained identical.

## 7. Fresh complete affine boundary FD, with its exact scope

The response entry consumed the actual new warm SHA and its complete
producer ledger. It recomputed every original direct/separated
boundary direction and both fourth-order Richardson levels. The
maximum fourth-order relative directional error was
`7.157355710541506e-10`, below the original implementation threshold
`5e-5`. The maximum second-order error was
`9.883432887906797e-6`, and the recorded second-order truncation
contractions passed.

The complete true-zero T112 response/J remained an explicitly
affine map for this implementation check. The ready linear graph
was not substituted for the actual shooting J. The new warm's
first eight native-height coefficients were

`4.867482223599667e-14, 3.181341071580249e-14, 1.958793643788373e-14, 1.1242098722858854e-14, 6.028013143492741e-15, 3.0884741999053453e-15, 1.556703848401029e-15, 7.833421268935398e-16`.

They differ from the zero anchor. No thresholding to zero or new
nonlinear native solve was performed. The three saved global
controls were

`-2.285200681334446e-19, 9.043893686927214e-20, -1.6410778191422653e-19`.

The FD report explicitly retains
`nonlinear_native_at_current_H_solved=False`,
`full_BVP_solved=False`, and `full_Cartesian_closed_surface=False`.
No old response pass was relabelled with the new warm SHA.

## 8. Complete saved-byte audit and preservation identities

Read-only audit of the actual artifacts checked:

- All111 domain NPZ file hashes/sizes and708 NPY array
  shape/dtype/byte identities; all twelve complete B/Gamma/Pi groups
  and the full beta array reconstructed from their original chunks.
- The canonical complete B model identity, all13 endpoint J/P
  bindings, original midpoint base bytes, full coordinate layout,
  fixed C support and outside-offset array identities.
- Exact byte equality of all111 domain NPZ files with request39,
  including the complete base state/RHS and original capture.
- Both actual37 parent SHA values, the complete unmodified parent
  producer subtree, and byte equality of the parent mesh/state/RHS
  with the model's saved base arrays.
- All31 current producer source hashes and all35 distinct current,
  FD and model-source hashes, plus exact current warm/status/FD
  producer binding.
- All63 full-H NPZ files and their63 actual arrays, all48 full-array
  references and30 unique reconstructed complete arrays. These
  include the236036-by18 basis and A-basis,24576-by18 B-basis,
  unconstrained center, original raw direction, unrepaired and
  repaired candidates, multipliers, stationarity/slack evidence,
  and final original A/B actions.
- The first full basis column is byte-for-byte the actual raw LSMR
  direction. The selected complete-H direction is byte-for-byte the
  actual saved trial direction; its final A action and evidence
  identities match the full helper result.
- The separate QR inverse audit checked all68 inverse NPZ files and
  their68 arrays, all17 saved inverse reports against the accounting
  record, the live-model/source bindings and the frozen numerical
  dependencies. The actual factor was memory-only: its hashes and
  report are saved, but the raw triangular factor bytes were not
  exported. No later independent refactorization or certified
  factor-rounding audit is claimed. See the separate
  [actual40 inverse byte audit](2026-11-14-actual40-complete-QR-inverse-byte-audit.md)
  for that exact division of saved and unexported data.
- All three retained observer reports preserve the original flags
  and residual bytes. There are no bad-midpoint arrays to audit for
  this run because no actual bad midpoint was observed.

This local work read or hashed already saved data. It did not
evaluate an ODE, build a matrix, apply A/B/H, recompute a norm, run
a solve or repeat a numerical experiment.

The principal preserved files, relative to the artifact root, are:

| File | Bytes | SHA256 |
|---|---:|---|
| `twelve-query-qr-warm/warm-001.json.gz` | 4738146 | `c62a7f12db331993698ed7e5d9086193d8e43d399dbd98adb2b869430e19aeda` |
| `twelve-query-qr-warm/driver-status.json` | 478290 | `30f19320351f37344c5e75c6dd8614707f26692c7888c2d0eafcdb532f24d359` |
| `twelve-query-qr-warm/optimization-intent.json` | 195828 | `8e18644f9746b33a7ea154349f23509f106d6f3e345a80ac8b831d15e1e58800` |
| `twelve-query-qr-warm/model-000.json` | 247118 | `1e4495c48e0d685e79cd1f906ad0ab06bddf72a392d13e54b10a5d5beb5a9c1d` |
| `twelve-query-qr-warm/domain-operator/manifest.json` | 337146 | `bf275ecdaf1288ff8b961264afd09f70dd121e8f457c29628c26ed29aba4bcb5` |
| `twelve-query-qr-warm/block-qr-live-model-binding.json` | 6906 | `90de5e4d8e369b436bb653ab7f72e0d41b4b0601f1507859212c6f00b9bbf6a6` |
| `twelve-query-qr-warm/block-qr-inverse-accounting.json` | 662851 | `a079d996b7d3c8ed19e712d7c21ee1798e3280941834f1549ce01b13be263b45` |
| `twelve-query-qr-warm/full-H-result.json.gz` | 870321 | `2526e12b80a25e5401652e1e30921991a3571a15dce940fe15dd45c03feb7b8d` |
| `twelve-query-qr-warm/full-H-versus-C-comparison.json` | 13427 | `ff0dca234e214e5b59f72c330992e0751eeb8c12eb96af2f3e8b6be744324b70` |
| `twelve-query-qr-warm/full-H-final-selected-evidence.json` | 13014 | `7e3ced330b4f89ab3208ab395c0ed407598e018ac457430853c21c2311e082f3` |
| `physical-response/response-check.json` | 271032 | `bbeba530a62cb4f4f226e130146be903524afa6b2caacb99e44e3ac5a925b3f9` |

The full-H array manifest SHA is
`b6c1906374304f391a8c762df7f499888616a53ed692abb26eb0c43069bf2d3d`.
The complete array chunks and ordinary scientific readouts remain
bound to the artifact above even where large artifact-only trees
are excluded from Git publication.

## 9. Evidence-based continuation through the already frozen entry

The current exact query set has no newly observed nonlinear failed
point in request40. There is therefore no basis here to add another
query or change the physical equations. The explicit remaining
limitation is the sixteen-row working budget in an otherwise
successful complete-H solve and full trial.

The frozen QR entry already accepts its own schema as a parent,
with the actual warm and paired-status SHA values above. Its
existing `--full-h-max-active` option permits32 rows. The wrapper
propagates its schema and complete source list into the unchanged
parent validator; the full scalar formula, current p values,
constant-state layout, source ledger and original inputs remain
checked, and the entire previous producer subtree is preserved.
No new wrapper or source mutation is needed to continue from this
actual saved warm.

A concrete next run can therefore use that own-schema parent,
`--full-h-max-active 32`, and the same300 second helper,1200 H-action
and1200 second total budgets,90 second original-trial reserve,
lambda270,200 original LSMR iterations,200 dual sweeps, original17
trials and fresh actual-warm FD. This enlarges the existing
algorithmic working set; it changes no final scientific equation or
tolerance. It is not a prediction that32 rows will suffice. Its new
weights, complete full-row slacks, chosen candidate and actual
nonlinear trial must be read from that next run.

The present saved output still has `success=False` and
`new_coupled_finite_acceptance=False`. The true nonzero native tail,
full BVP acceptance, full closed construction, same-metric
refinement, and the topic's geometric completion criteria remain
outstanding.
