# Actual request32: the midpoint constraints work, while RMS471 limits the step

The public nine-query run completed one real warm step and a fresh
complete affine Rphi derivative check. Adding the complete angular grids
at original collocation midpoints473 and477 removed those midpoint
failures at the smaller trial steps. The accepted step nevertheless
remained `2^-8`, because the original complete left RMS check rejected
interval471 at every tested step from `2^-4` through `2^-7`. That
limitation was actually evaluated in this new direction; it is not
inferred from the parallel seven-query run.

This is an unaccepted warm with a measured decrease, not an accepted
full-DN field or closed surface. The true nonlinear native tail at its
new nonzero height was not evaluated.

## 1. Actual identity and same-parent comparison

| Identity | Actual value |
| --- | --- |
| Public run | `43614990381` |
| Job | `132508019098`, `Mainline mixedquery` |
| Source commit | `4dce418073cf3152a0c33337e103bb746f485c76` |
| Artifact | `14122645137`, `visible-mainline-mixedquery-43614990381-1` |
| ZIP | 175,987,792 bytes |
| ZIP SHA256 | `bfd165666b043107bda597d5e31f4cf6122716a16ac3d8a2a20cc3fe3a80c0e1` |
| Actual request29 parent warm SHA256 | `f2e999e7c61d28683dc09adf387e0867b2dd36d271ebe0433fafbec68466fbd9` |
| New warm | `mixed-query-warm/warm-001.json.gz`, 4,723,774 bytes |
| New warm SHA256 | `7f5e8d5f888b79c4ce0c0db91c9bc4e27bb9ef0c7554c0f578431ddbbecb578e` |
| Warm elapsed time | `314.95115921499996` seconds |
| Fresh FD elapsed time | `21.27543712199997` seconds |

This branch and
[request30](2026-11-14-actual-request30-complete-H-comparison-and-warm.md)
start from exactly the same actual request29 parent. A read-only byte
comparison found identical base mesh, all augmented states, all nodal
RHS values, coordinate scale, captured endpoint J/P factors, and all
seven original B/Gamma/Pi block identities. The complete raw LSMR
direction is identical in all 236,036 entries. The reported original
initial residuals and the fixed-weight starting merit also agree.
Thus these two branches can be compared within their common initial
model; unrelated successive models with refreshed weights cannot be
compared by subtracting their displayed merits.

The nine-query manifest explicitly retains the unchanged seven-query
component model identity
`8faeb2c84a44e593f126a8a3afccaf912aa207b1052cab3639a6d371cc15245a`,
which is the actual request30 domain model. The new combined model is
`ed7904ddcb92137dfe1ff1dd5b496090df8200da01047b3fa5439441cfdebc4e`.

The field retains 699 nodes, M112/N2048, 338 physical and 453 augmented
rows per node, the complete scalar formula, all constant core and
control rows, and exact inlet coordinate relations. The initial
coordinate projection has maximum difference zero. The new field still
declares `success=false`, `new_coupled_finite_acceptance=false`, and
`complete_closed_surface=false`.

## 2. What the nine actual queries represent

The first seven queries remain the original left RMS fraction
`0.17267316464601146` at intervals
`(472,473,475,477,479,480,481)`. The final two are original collocation
midpoints, fraction one half, at intervals473 and477. Each query uses
all 2048 original physical angles. The combined B therefore has 18,432
rows and 236,036 columns, with possible local support of 3,721 columns.

The midpoint bases are the original `state.middle[j]` and
`problem.mid[j]` values. Their reported reconstructions by the original
collocation midpoint formula have maximum difference exactly zero.
The original midpoint stations and base beta-squared minima are

| Interval | Actual midpoint station | Base minimum beta-squared |
| --- | --- | --- |
| `473` | `1.2018391887397941` | `0.3950944947261622` |
| `477` | `1.212238432246558` | `0.8971438792786968` |

The differentiated midpoint formula is

$$
\delta y_m=\frac{\delta y_L+\delta y_R}{2}-\frac{h}{8}(\delta f_R-\delta f_L).
$$

It includes the original nodal J/P and global control chains. The
complete source never substitutes the left RMS query or a plain nodal
average for a collocation midpoint. Query kind, fraction, interval and
station are explicit in verification, export, trial readout and saved
producer metadata.

The same original complete Jacobian construction made 88 Jacobian
calls; the domain operator captured only the two required original
chunks and retained 11 endpoint nodes and 11 variants. Both added
midpoint endpoint pairs were already present. The old and added unit
jet bytes match. The combined compiled B occupies 100,122,624 bytes.
No second complete Jacobian was constructed and no original field
mode, control, scientific tolerance or nonlinear domain gate changed.

## 3. Actual direction and comparison with seven-query C

The raw LSMR result is the same as request30: `istop=2`, 84 of 200
iterations, actual preconditioned normal norm
`2.8023571296444233e-5`, original regularized gradient norm
`320.85918621725165`, actual directional derivative
`-1.1013207206594153`, and damped-model decrease `0.55066039017657`.
The preconditioned residual is not the complete KKT residual, and the
iteration limit did not stop this solve.

The nine-query local C projection reached its 200-sweep bound, with
normalized violation `8.710786001033616e-7` and maximum multiplier
update `1.982708211336129e-5`. Its local objective is
`0.05434888369318498`, local stationarity norm
`6.10500121423252e-15`, and complementarity sum
`1.3443515810479148e-6`. These quantities belong to the local
projection problem only. Before radial repair, 126 original linear
slacks were negative and two were zero, with minimum
`-0.0010666268564686887`. The actual radial factor
`0.7305634509131044` made all 18,432 slacks positive; their minimum is
`1.942890293094024e-16`.

The same-model segment minimization selected the repaired projected
endpoint, with parameter1 and no further repair. Its selected
diagnostics, alongside the actually selected seven-query C direction,
are:

| Quantity on the common initial model | Request30 seven-query C | Request32 nine-query C |
| --- | --- | --- |
| Actual model derivative | `-0.7397834189900147` | `-0.6739924145916285` |
| Damped model decrease | `0.4673643909042686` | `0.4211797011629792` |
| Squared weighted A-action | `0.2573680916004568` | `0.2261859872894287` |
| Actual damping penalty | `0.2874699645710353` | `0.27943943956786993` |
| Selected scaled-direction norm | `0.0019857861326840888` | `0.001957853026005411` |
| Original full gradient norm | `298457.19124813564` | `298457.692084326` |
| Actual accepted alpha | `0.00390625` | `0.00390625` |
| Actual fixed-weight decrease | `0.002933782783976824` | `0.002631130390312819` |

The nine-query direction sacrifices some model descent and protects the
two additional midpoint grids. It did not increase the accepted alpha
or the actual merit decrease in this execution. Its selected zero-dual
posterior expression E is `610953.3193710725`, which is loose. No
complete-QP optimum or small full-model KKT residual is claimed.

## 4. Actual trials distinguish the resolved and remaining limitations

All nine trial states had finite original nodal RHS values. The
original midpoint and complete RMS outcomes were:

| Alpha | Original bad midpoint RHS indices | Later original check |
| --- | --- | --- |
| `1` | `475,476,477` | Rejected |
| `1/2` | `471,472,475,477` | Rejected |
| `1/4` | `472,473` | Rejected |
| `1/8` | `475` | All nine selected grids positive, but the unselected original midpoint475 rejects |
| `1/16` | None | All nine grids positive; complete left RMS471 rejects |
| `1/32` | None | All nine grids positive; complete left RMS471 rejects |
| `1/64` | None | All nine grids positive; complete left RMS471 rejects |
| `1/128` | None | All nine grids positive; complete left RMS471 rejects |
| `1/256` | None | All original nodes, midpoints, both RMS grids and rho checks pass |

There is a direct same-parent comparison at alpha `1/64`: request30's
selected C direction had midpoint473 beta-squared minimum
`-0.13697024968996807`, whereas the nine-query direction has midpoint473
minimum `0.3928818338924338` and midpoint477 minimum
`0.891832409231689`. This is an actual improvement at the intended
queries, not just satisfaction of their linear inequalities.

At `1/8`, the two selected midpoint minima are respectively
`0.38030274299217903` and `0.8406159543142014`. The remaining actual bad
midpoint is interval475, station `1.2072539807467981`, with minimum
`-0.09429437336940105` at phi0 and six negative sampled angles. That
larger-step failure remains in the original record; it is not used to
claim the nearer limitation is a midpoint failure.

The nearer four rejected steps have valid nodes, valid original
collocation midpoints, positive margins on all nine selected grids and
actual decreasing merit. All four fail the actual original left RMS
query at interval471:

| Alpha | Actual merit decrease | Actual-to-predicted ratio | RMS471 minimum beta-squared | Reported phi |
| --- | --- | --- | --- | --- |
| `1/16` | `0.041747337491436554` | `1.0015493477747992` | `-0.20291673070373073` | `3.074097498922825` |
| `1/32` | `0.02096084071710891` | `1.0004305180875575` | `-0.199633162385783` | `0` |
| `1/64` | `0.01050512132824366` | `1.0001523721825` | `-0.09908776024422572` | `0` |
| `1/128` | `0.005258990407391195` | `1.0000622433737154` | `-0.020315754519159013` | `0` |

RMS471 is fraction `0.17267316464601146`, station
`1.1902387410048825`, between nodes `1.1893780599903945` and
`1.1943625114901544`. At the nearest rejection its original scalar
values are a `1.1913434951459982`, ap `-0.12394221883211583`, and app
`-2.4807235920076978`; the curve curvature at the reported minimum is
`0.10299472267036024`. The original right RMS fraction has no invalid
point on these four trials. No original failure was waived because of
good merit, good selected-query margins or a good finite model.

## 5. The accepted new warm and its fresh FD

The accepted alpha is `0.00390625`. The merit changes from
`44.3724225594053` to `44.36979142901499`, an actual decrease of
`0.002631130390312819`. Its predicted undamped merit decrease is
`0.0026310572073640773`, giving ratio `1.0000278150351642`.
Both original RMS fractions evaluate all 698 intervals and report zero
failures. The original 4096-angle rho minimum remains
`0.16604058243274977`; inlet and constant-state residuals remain zero.
The physical collocation maximum is `0.007110437270942378`, and the
complete affine boundary maximum is `8.831813076391987e-8`.

At the accepted field the seven left RMS minima, in declared order,
are `0.208376977831217`, `0.09703783246910924`,
`0.5731584320789811`, `0.5053568558928037`,
`0.5361122065389998`, `0.005772916232701819`, and
`0.09275518996966148`. The two original midpoint minima are
`0.3945333192882614` and `0.8958520601404756`. All nine reported minima
occur at angle index0.

The actual new scalar parameters are

```text
[-1.4848087956500275e-19,
  5.3644493066971466e-20,
 -1.165935961123015e-19]
```

The independent real directional check, with fixed weights, reads
merit slopes `-0.673992384534472`, `-0.6739924792498186`, and
`-0.6739923676946091`. Its full weighted-vector errors are
`8.095851771499839e-5`, `1.0061009621827894e-4`, and
`2.1530272166476124e-4`; these do not claim machine-level convergence of
the full vector difference.

The fresh complete affine Rphi FD binds the new warm SHA and reports
maximum fourth-order error `9.143364336011781e-10`, below the original
`5e-5` implementation threshold. Its second-order maximum is
`9.883390288558213e-6`, with contraction reported. It actually reran the
original directions, steps and Richardson estimates.

The current native height remains nonzero, with first entry
`2.3995927160419497e-14`. The whole new height list and the three
controls equal request30's saved values, while the interior field is
different. The genuine completed zero-H T112 Jacobian is held explicitly
affine for this FD. No current-height nonlinear native solution or
Jacobian is asserted, and no tiny coefficient is rounded away. Equal
endpoint FD diagnostics across these two actual fields are not used to
claim their interior geometries are identical.

## 6. New operator verification and complete byte preservation

The mixed operator's maximum adjoint error is
`1.4750457132038207e-17`; local/full forward and transpose differences
are zero. Its original full complex-chain check on the actual raw LSMR
direction has normalized maximum error `1.3463827828930567e-12`.
The seeded local direction has error `1.7762679341198368e-12`. The
worst row in both reports is the newly added original midpoint473,
angle0. The per-query normalization gives respectively
`1.8532225898198966e-12` and `1.892677980524638e-12` on that query; these
normalizations are recorded separately. The original `5e-5` complex
implementation threshold and `5e-12` adjoint/local threshold both pass.

The actual original midpoint formula is used in the complex chain,
including both nodal RHS derivatives and all control contributions. The
11 actual endpoints are reused. The separate original nonlinear
collocation implementation check retains its narrower stated scope:
free inlet core and global controls, with interior physical directions
zero. Neither check replaces the real nonlinear backtracking.

A read-only audit verified all 85 domain-operator files and all 536
contained NPY array identities against their actual bytes. It then
streamed the saved chunks to reconstruct the whole hashes of all nine
B/Gamma/Pi blocks and the complete beta-squared array. The two original
midpoint input rows and stations are preserved separately as actual
bytes. All 20 producer-source hashes match their frozen files.

The read-only midpoint observer produced 15 reports, 10 bad-midpoint
NPZ files and 30 original arrays. Every report preserves the original
returned finite flag and residual byte identity. Every original file
and array hash was checked. This audit did not run any new scientific
matrix, derivative or solver calculation.

There is one explicit metadata alias difference: the saved
`optimization-intent` additionally contains `query_interval_order`,
equal to its already declared typed query order. All other identity
fields equal `driver-status.identity`, and that entire status identity
equals the corresponding fields of the saved warm producer. This
extra read-only alias does not alter numerical data, the original
producer subtree or an acceptance result; the original files remain
unchanged.

## 7. Original source and artifact identities

The three new frozen numerical sources are

```text
geometry_20261114_mixed_query_domain_operator.py
34115f81cf5a09c3d07a6b79f408459fb014ca580ad0a992f8a639ff937ba854
geometry_20261114_mixed_query_projection_warm.py
d74d7a1c86cb131d262025cffa079a1a01a1ed7e5128ea339744c61cf4cfeac6
geometry_20261114_mixed_query_projection_response.py
5c871d96966a681e4fce607c0491db337c319854b568c5a038e46a560a0fa87c
```

Under the artifact root, key actual files are:

| Relative path | SHA256 |
| --- | --- |
| `mixed-query-warm/driver-status.json` | `a6224f936f261168ef05a3b51fa3b1318b6d25eacf6653c412d2c33a8731d56e` |
| `mixed-query-warm/optimization-intent.json` | `53ea9a59bf2a5206d540281654164e63dbcdb850c0a8e0077d80ffcb68ef5621` |
| `mixed-query-warm/model-000.json` | `96f1ba51b894724d4f82c7b0815a56b0fbfd8cba4866b2e5596323de9d3ff7a6` |
| `mixed-query-warm/direction-00.json.gz` | `dcd2bed9e40cf5eced3959acfa41dfc4e0a5539fe825f8eedcb46145559f019b` |
| `mixed-query-warm/full-angle-operator-check.json` | `82371baf173813207971ef0e779f8a6abc27e048a3e324540031aa272493440a` |
| `mixed-query-warm/domain-operator/manifest.json` | `e3eae53de48e197f4bd4169c30d6b6da85210fd12147e2c54aceeb2c40df2300` |
| `mixed-query-warm/domain-operator/original-collocation-midpoint-inputs.npz` | `e5555e569a1c9bdf774960754aca1eaeba4a611aaaa4d50346c5ef0dc7e63614` |
| `physical-response/response-check.json` | `2a297e00b5d74523f19fcf61f9822d676cbea6d17d9301677b5e29b28a142563` |

## 8. Concrete continuation consequence

The actual record supports adding the complete left RMS471 angular
grid to the current nine-query algorithmic model. The two original
midpoint grids should remain: their actual effects are measured above.
The next field must start from this saved request32 warm, preserve its
entire producer/source chain and all original equations and final
gates, and distinguish eight left RMS grids from two original
collocation-midpoint grids in every output. It must still rerun all
original nodes, midpoints, both complete RMS grids, rho and merit checks
on each proposed step; the ten selected linear grids cannot certify
all of those nonlinear conditions.

This continuation decision does not require changing the damping,
inner iteration allowance, projection sweeps, original backtracking
range or scientific tolerances. Larger-step midpoint475 and other
failures remain preserved evidence, not automatically added constraints
or presumed failures of the next direction. Any subsequent full-DN
acceptance still requires the genuine new-height native solve, final
audit and original full-field acceptance procedure.
