# Actual request37: midpoint475 resolves and the nearest RMS limit moves to470

**Status: numerical evidence from an actual public Actions execution.**
The eleven-query run continued the actual request35 warm and saved a
real descending step at alpha `1/16`. Adding the complete original
midpoint475 grid resolved that midpoint at the nearer tested steps.
At alpha `1/8` and `1/4`, all original nodes and collocation midpoints
were valid, all eleven selected angular grids were positive, and the
actual fixed-weight merit decreased. The original complete left RMS
check nevertheless rejected interval470 in both cases.

The saved result remains an unaccepted warm. The real nonlinear native
tail at its new nonzero height has not been solved. A fresh complete
affine Rphi derivative check passed, but neither a complete BVP nor a
closed surface is accepted by this execution.

## 1. Execution, parent and saved output identities

| Identity | Actual value |
| --- | --- |
| Public run | `43618014985` |
| Job | `132517259808`, `Mainline elevenquery` |
| Source commit | `6e9af38927c58e173c7922052ab58ca594af4bc7` |
| Artifact | `14122829001`, `visible-mainline-elevenquery-43618014985-1` |
| ZIP size | 209,109,318 bytes |
| ZIP SHA256 | `606a69a8d4b417e51b763a29a222fbdcc2b3a97f61965fc462e4bc3b518d3301` |
| Actual35 parent warm SHA256 | `24ca673e64fb60d1d5206ec742ce08c653b390bafd5ecd3ffbe54f0b1c1cd25a` |
| Paired actual35 status SHA256 | `214d4eed229c8b63af29bda765dca4506de1646a3addcbd02d0b626068ebf1ff` |
| New warm | `eleven-query-warm/warm-001.json.gz`, 4,732,645 bytes |
| New warm SHA256 | `dd83748341c8d6172096fc644361018be7b29d856de621a0b333104d20aafdb8` |
| New paired status SHA256 | `37e70ad5a3c9ef828d93bcbf371b3a107e3890026731d7944d98e370987d29e0` |
| Warm elapsed time | `158.098622954` seconds |
| Fresh complete boundary FD time | `16.201004794` seconds |

The parent is the actual saved field described in
[request35](2026-11-14-actual-request35-ten-query-step-and-midpoint475.md).
Its entire producer subtree and source ledger are preserved. The
current intent equals the current status identity, and every identity
value matches the saved warm producer. The field retains all 699
nodes, M112/N2048, 338 physical and 453 augmented rows per node, the
complete scalar formula and three global design parameters, exact
inlet relations, and exactly constant core/control rows.

The status records one real progressed warm step. Both `success` and
`new_coupled_finite_acceptance` remain false; the saved field also keeps
`complete_closed_surface=false`. The original true T112 zero-H
response/J and its configuration are unchanged. They remain an
explicitly affine boundary model at the new height, not a newly solved
nonlinear native response.

## 2. Actual eleven-query operator and verification

The selected query set is eight left RMS intervals
`(471,472,473,475,477,479,480,481)` at fraction
`0.17267316464601146`, followed by original collocation midpoints
`(473,475,477)` at fraction one half. Each query contains all 2048
original physical angles.

The actual B shape is `22528 x 236036`, local shape `22528 x 4059`;
compiled rows occupy 122,372,096 bytes. All three midpoint endpoint
pairs were already in the original twelve-node capture. The original
A construction made 88 Jacobian calls; B captured only original
calls59 and61, retained twelve nodes and twelve variants, and reused
their original J/P factors. The shared node480 factors from the two
chunks have identical recorded raw identities. No second complete
Jacobian was constructed.

The complete new domain-model identity is
`fbc14ec80a1d33274e2afa7dab3327a87ead8d61b715adf820c4d849fdf16b17`.
Its eight-query left-component model on this actual base is
`b55573b458cd5790f32d7aaa4d3f8a3d866d4e48200c05298c29a8476ba4f595`.
Neither is relabeled as a model from a previous round.

All three midpoint inputs are the original returned `state.middle`
rows at `problem.mid`. Their reported reconstruction differences from
the original midpoint formula are zero. Their base minima are:

| Original midpoint | Station | Base minimum beta-squared |
| --- | --- | --- |
| `473` | `1.2018391887397941` | `0.3864762681003041` |
| `475` | `1.2072539807467981` | `0.7761387099092815` |
| `477` | `1.212238432246558` | `0.8729004506058384` |

The complete original nodal J/P, global scalar-control and exact-inlet
chains remain in every typed row. The actual B verification reports
maximum adjoint error `7.696145901579609e-19`, local/full action
discrepancy zero, actual-LSMR complex-chain relative discrepancy
`8.844764454960603e-13`, and seeded-direction discrepancy
`9.740381962639658e-13`. All original implementation checks passed.

The separate complete collocation check reports independent complex
error `8.673617379884035e-19`. As its scope field explicitly states,
that one independent collocation direction uses only free inlet core
and global controls, with interior physical directions zero. The full
B complex check uses the actual complete saved LSMR direction. Those
two verification scopes are not conflated.

## 3. Actual model direction and local C projection

The original raw LSMR solve returned `istop=2` at 81 of at most200
iterations, in `6.606533218999999` seconds. Its reported preconditioned
normal norm is `2.5418101708209383e-5`; its original regularized
gradient norm is `335.6716870276418`. The raw directional derivative is
`-1.1022412698285962`, with damped-model decrease
`0.5511206597720628`. The iteration limit did not stop this solve, and
the small preconditioned norm is not a small original KKT norm.

The unchanged Hildreth projection reached its 200-sweep limit. Its
final normalized primal violation is `1.0297545453870657e-6`, maximum
dual-coordinate update `1.301612183391733e-5`, local objective
`0.06057709654733838`, local stationarity norm
`5.438087922582134e-15`, and complementarity sum
`1.303428097260199e-6`. These are the local C-projection quantities.
They do not establish a complete-model optimum or a small complete
KKT residual.

Before radial repair, 220 slacks were negative and two were zero, with
minimum `-0.0012580906123994956`. The actual radial factor
`0.6897397025180634` made all 22,528 slacks positive; the minimum is
`5.551115123125783e-17`. The same-model feasible-segment minimization
selected the repaired endpoint at parameter1 with no further repair.

| Selected complete-model diagnostic | Actual value |
| --- | --- |
| Directional derivative | `-0.608596910318609` |
| Damped-model decrease | `0.3946333646992678` |
| Squared weighted A-action | `0.1902665941640983` |
| Damping penalty | `0.23766049707458403` |
| Scaled-direction norm | `0.0018055716887202648` |
| Original complete model gradient norm | `327510.3261738139` |
| Zero-dual posterior expression E | `735685.9653667898` |
| Original-ray backup model decrease | `0.00011980691371850548` |

The selected vector has a real negative complete-model derivative.
The loose zero-dual model expression is retained honestly and is not
used as an additional BVP acceptance threshold. The original residual
weights are fixed throughout the real trials, and the damping penalty
is excluded from their nonlinear merit.

## 4. All five actual trials

All five original nodal RHS evaluations were finite and retained
exact inlet and constant-variable relations. The outcomes are:

| Alpha | Original bad collocation midpoints | Complete RMS outcome |
| --- | --- | --- |
| `1` | `473,475,477` | Not reached after original midpoint rejection |
| `1/2` | `472,473,475,477,482` | Not reached after original midpoint rejection |
| `1/4` | None | Only left RMS470 invalid; complete right RMS valid |
| `1/8` | None | Only left RMS470 invalid; complete right RMS valid |
| `1/16` | None | Both complete original RMS grids valid; warm step accepted |

The first two midpoint failures are real nonlinear limitations even
on selected grids. All selected linear-beta minima remain positive:
`0.002796861383102922` at alpha1 and `0.004195292074654328` at alpha1/2.
Nevertheless at alpha1 the three selected midpoint minima are
`-0.07158032828044814`, `-0.09303193354840933`, and
`-0.012017873602808704`. At alpha1/2 they are
`-0.10503334867104175`, `-0.08404626325407549`, and
`-0.0766977689422017`. Thus the linear reserve is not a certificate of
nonlinear feasibility at a larger step. The original backtracking
retains and enforces these failures.

At the nearer alpha `1/4` and `1/8`, all eleven original selected grids
are positive and all original nodes and midpoints are valid. The newly
modeled midpoint475 has minima `0.43130076839049203` and
`0.7389613421392083`, respectively. At alpha1/8 the retained
midpoint473/477 minima are `0.3716759297799376` and
`0.8255809525005828`; left RMS471 is `0.02133513405370646`.

These two trials also decrease the actual fixed-weight merit:

| Alpha | Actual merit | Actual decrease | Actual/predicted ratio |
| --- | --- | --- | --- |
| `1/4` | `44.18566447711165` | `0.14420798226760212` | `0.9863517928309009` |
| `1/8` | `44.25508326048422` | `0.07478919889503288` | `1.0026953726011407` |

Both are correctly rejected by the complete original left RMS rule at
the previously unmodeled interval470:

| Quantity | Alpha `1/4` | Alpha `1/8` |
| --- | --- | --- |
| Actual station | `1.1852542895051228` | Same station |
| Interval endpoints | `1.1843936084906348`, `1.1893780599903945` | Same endpoints |
| Minimum beta-squared | `-0.24713929103386545` | `-0.2501880308616917` |
| Reported phi | `3.009670305831628` | `0` |
| Curvature at that angle | `0.08381673628270844` | `0.08371447510485115` |
| Scalar a | `1.1919304470480967` | Same |
| Returned ap | `-0.11156786967520294` | Same |
| Returned app | `-2.484392041395813` | Same |

Each complete RMS check evaluated 698 stations for each fraction. At
both rejected trials its left invalid count is one and its right
invalid count is zero. This is an actual original all-RMS result, not a
failure inferred by extending the selected B rows.

The stored full midpoint observer sees finite original midpoint inputs
at the two larger failed trials, with the original nonfinite physical
RHS rows. Its readout preserves the exact original finite flag and
residual bytes, calls no second whole flow or Jacobian, and does not
replace the original gate.

## 5. Accepted step, original residuals and fresh FD

This new model refreshes its weights at the actual35 parent, then holds
them fixed. Its starting merit is `44.32987245937925`, not the preceding
model's final `44.32940101648062`. Those two different-weight values
must not be subtracted to infer progress or deterioration.

| Accepted-step quantity | Actual value |
| --- | --- |
| Alpha | `0.0625` |
| Fixed-weight initial merit | `44.32987245937925` |
| Actual final merit | `44.292172704126806` |
| Actual decrease | `0.037699755252447176` |
| Predicted unregularized decrease | `0.03766569245318631` |
| Actual/predicted ratio | `1.0009043454943303` |
| Physical collocation maximum | `0.007110320785400957` |
| Complete affine boundary maximum | `8.074771843017406e-8` |
| Original rho minimum | `0.16604058243274977` |
| Exact inlet/constant-row residual maxima | `0 / 0` |
| Invalid original left/right RMS stations | `0 / 0`, 698 stations each |

The accepted selected-grid minima are:

| Kind | Interval | Minimum beta-squared | Angle index |
| --- | --- | --- | --- |
| Left RMS | `471` | `0.021770130579212732` | `0` |
| Left RMS | `472` | `0.19983054908853914` | `0` |
| Left RMS | `473` | `0.6465538855873549` | `76` |
| Left RMS | `475` | `0.5479303480082631` | `0` |
| Left RMS | `477` | `0.48326299488698077` | `0` |
| Left RMS | `479` | `0.5126277647018241` | `0` |
| Left RMS | `480` | `0.005420214419654346` | `0` |
| Left RMS | `481` | `0.08875107286486683` | `0` |
| Collocation midpoint | `473` | `0.3785689893800356` | `0` |
| Collocation midpoint | `475` | `0.758522334525311` | `0` |
| Collocation midpoint | `477` | `0.8518954503614481` | `0` |

Three independent real directional merit slopes are
`-0.6085968617242088`, `-0.60859707240013`, and
`-0.6085967686431104`, compared with model slope
`-0.608596910318609`. Their complete weighted-vector relative
discrepancies are `6.884560617769616e-5`, `9.52270143601207e-5`,
and `0.0001685676388857342`. The real directional check supports the
measured descent; it is not described as machine-precision vector
agreement.

The actual nonzero native height begins

```
[4.7701880967848475e-14,
 3.11746621045499e-14,
 1.913732585448752e-14,
 1.0921776925172766e-14, ...]
```

The complete 112-entry list is retained and bound to the fresh response.
The three actual global scalar parameters are

```
[-2.2056579842565033e-19,
  8.679453249647546e-20,
 -1.5924599700844841e-19]
```

The fresh complete affine Rphi FD reports Richardson relative error
`8.381607559065326e-10`, below the original `5e-5` threshold. Its
second-order discrepancy `9.883428525475155e-6` contracts. The exact
new warm hash and its complete producer are bound to that result.
The genuine completed T112 zero-H J is held affine, without a
`ready.linearD` substitution. A new nonlinear native H/J response and
final true-tail audit remain outstanding.

## 6. Full saved-byte audit

The 102 domain NPZ files and all 650 contained NPY arrays were checked
against their recorded file hashes, byte lengths, shapes, dtypes and
raw array hashes. Streaming the original angular chunks reconstructs
the full hashes of each of the eleven B/Gamma/Pi blocks and the full
22,528-entry beta array. The latter hash is
`9ad4c9f4a0cb18b39a89b4703917f2cf0f98634d43e7ef0f4b5fc43fe4e8441f`.
The frozen canonical metadata recipe reproduces the recorded complete
domain-model SHA. File counts and aggregate export byte lengths also
match the actual model's export record.

All eight original interval endpoint-pair identities match the audited
endpoint pool files; the repeated node480 pair from original calls59
and61 has matching bytes. The saved three original midpoint subset
arrays match their recorded identities. This audit does not recompute
the flow or the midpoint formula; the numerical reconstruction
diagnostics above are the ones produced in Actions.

Nine original midpoint observer reports, eight observer NPZ files and
24 raw arrays were checked. Their original NaN-containing RHS bytes
are preserved; all observed finite flags and residual byte identities
are unchanged. The actual parent35 warm/status hashes and entire
producer subtree match. The original base mesh/states/RHS in the B
export match the actual parent arrays byte for byte. All twenty-four
current producer sources and the twenty-eight distinct producer/FD
source files match their recorded frozen hashes.

The full saved LSMR direction array has identity
`6a3b3ea9b05e80e0f90148cb6cead947fb6f8e2eee70461953f99628ad1062f8`,
which is the actual direction supplied to the full complex B check.
Only file reading, byte comparisons, hashing and metadata reassembly
were done locally. No solver, matrix action or new scientific
diagnostic was executed locally.

| Artifact-relative file | SHA256 |
| --- | --- |
| `eleven-query-warm/model-000.json` | `2d0ea022f312756ab2278e230999c4b15504556ac2c42c5fe8129feaf76c1839` |
| `eleven-query-warm/optimization-intent.json` | `1f05052687012c70c0619f2e3a8294c51879d426d33c1408d90c4616aee2333c` |
| `eleven-query-warm/direction-00.json.gz` | `d233fc46d5714fcb1ff646f43c5a6b645bd0961595772d99a6fa0562ff6f5ffd` |
| `eleven-query-warm/full-angle-operator-check.json` | `c95c89d6f72cb7721a2a4b3cf1d5a26ec1529ce343a53358bb019f2de4c1679a` |
| `eleven-query-warm/domain-operator/manifest.json` | `13f62ebdf20b7a44b1a71ab01fe4dae934429fbfcbebaed4b0108e24b8ba330f` |
| `physical-response/response-check.json` | `e1a0db6ef08d583d8d5568563f7439464a8faad250a0bca61821e385554a0c66` |

## 7. Implication for continuation

The intended midpoint475 limitation is resolved at the nearer tested
steps. The new, actually measured nearest limitation is left RMS470,
adjacent to the left edge of the current twelve-node projection
support. It is therefore inappropriate to describe the current query
set as already covering every observed near-step failure and blindly
chain several identical models on that premise. The actual accepted
warm remains a valid continuation point.

Protecting the complete original RMS470 grid is a concrete next
optimizer experiment supported by this run. Its endpoint470 lies
outside the existing projection support, while endpoint471 lies
inside. Merely adding a query to the present generic compiler would
also enlarge the permitted local correction support. The observed
successive edge failures motivate distinguishing that algorithm choice
from the added inequality itself. This adjacency does not, by itself,
prove whether the raw direction, local projection correction or their
nonlinear interaction caused the RMS470 violation; those contributions
have not been independently separated in this execution.

A possible bounded-support variant would keep local corrections on the
existing twelve nodes, retain the complete contribution of the raw
direction outside that support in every new row, and check the full
original B action after each repair or combination. It would still
need the original nodal J/P factor at470, captured from the same actual
A construction, and the actual complete nonlinear gates. Such a
variant would be a new explicitly identified optimizer algorithm, not
a reinterpretation of this frozen run or a proof of convergence. No
numerical performance for it is claimed here.
