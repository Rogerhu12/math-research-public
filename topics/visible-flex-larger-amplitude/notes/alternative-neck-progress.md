# Strong entry, a finite smooth neck, and actual nonlinear prefix solves

All surface computations below are still **surfaces with boundary**. A
finite linear tail Dirichlet-to-Neumann port is not a solved nonlinear
tail. No row below is registered as the requested closed-family,
Hausdorff, reach, grip, or all-time fixed-metric certificate.

## 1. A strong entry that accelerates only after gaining height

Use the exact support reference

\[
 h(\phi)=1+.38\cos(2\phi)-\frac{.38}{10\sqrt2}\cos(4\phi).
\]

The controlled Hermite outward leg has `k0=.45`, terminal speed `.25`, and
length `.65`. It ends at
`(a,a′,a″)=(1.09709375,.25,0)`. The geometric agent's whole-prefix nearest
point checks retain the full `.76` major-core witness. This was the reason
to start the next acceleration there instead of imposing a large initial
acceleration.

Append a length `.2` smoothstep radial-speed transition from `.25` to
`.65`:

\[
\begin{aligned}
 a&=a_0+.2\{.25u+.40(u^3-u^4/2)\},\\
 a'&=.25+.40(3u^2-2u^3),\\
 a''&=12u(1-u),\qquad 0\le u\le1.
\end{aligned}
\]

It has zero acceleration at both endpoints and maximum acceleration three.
The target metric is C² across this join. The actual finite Frenet map was
integrated, rather than substituting a prescribed metric for the computed
derivatives.

| Continuation discretization | sampled metric maximum | sampled principal curvature maximum |
|---|---:|---:|
| M64, angular 1024 | 8.6314e−10 | 6.1474865 |
| M96, angular 1536 | 2.2146e−11 | 6.1474758 |

Both use the saved M64 incoming finite state, whose metric error is
`1.2343e−11`; thus the second row has reached approximately the incoming
state and integration tolerance. These are the same physical metric and
initial finite geometry, not retuned parameters. They are not a proof of
infinite-mode existence or an exact finite concatenation.

At `s=.85`, the M96 state has

- `a=1.18709375`, `a′=.65`, `a″=0`;
- Frenet-domain margin `.20692689`;
- latitude curve curvature in `[.61485361,2.51280859]`;
- maximum endpoint surface principal curvature `2.45242527`;
- maximum ball radius `1.63420375` over the added piece;
- minimum sampled distance from the added piece to the rotated major-core
  witness `.78950003`, larger than `.76`.

The old incoming prefix supplies the closer `.76` core point. These checks
therefore support a double-mirror prefix diameter of approximately
`3.2684075` and a witness ratio approximately `.2325`; they still require
the global continuation to remain outside the witness ball and inside the
final diameter budget. The two files
`alternative-late-boost-025to065-m64.json` and
`alternative-late-boost-025to065-m96.json` contain only the added interval
`.65≤s≤.85`. Their `input` field identifies the incoming prefix; a geometry
reader must recursively include it.

## 2. Exact metric definition of the finite neck

For a turn from meridian angle `ψ0` to `ψ1`, use a nonnegative angular-speed
shape `w(u)` with cubic smoothstep ramps on `[0,ε]` and `[1−ε,1]` and value
one in between. Let `I(u)=∫₀ᵘw(t)dt`; then `I(1)=1−ε`. Define

\[
 T=\frac{|\psi_1-\psi_0|}{K(1-\varepsilon)},\qquad
 \psi(u)=\psi_0+
    (\psi_1-\psi_0)\frac{I(u)}{1-\varepsilon},
\]

and

\[
 a(s)=a_0+T\int_0^{s/T}\sin\psi(u)\,du.
\]

Thus `a′=sin ψ`, `a″=cos ψ·ψs`, `|ψs|≤K`, and `a″=0` at both turn ends.
The functions `w,w′` match at the ramp boundaries. Constant-angle legs
therefore join these turns with continuous `a,a′,a″`. The code uses split
64-point Gauss quadrature to evaluate the defining integrals; the formulas
above specify the exact metric.

At the end of the prefix the fixed jets are `(r0,−vloop,0)`. A separate,
strictly positive-length connector finishes at the physical small cut.
Its last angle is quadratic in normalized arclength, chosen to match the
cut's acceleration as well as radius and speed. This avoids a zero-length
bridge and is compatible with the existing BVP's split numerical chart.

For the loop seed `r0=.35`, radius ratio `2.2`, speeds `±.985`, `K=8`, and
`ε=.08`, both curved turns have length `.3797211972`, height
`.2518540318`, and radius excursion `.1183563820`. The complete loop has
height `.6508610027` and radius range
`[.2316436180,.8883563820]`. These are finite smooth turns, not slope jumps.

## 3. The smooth loop really changes the linear attenuation

For comparison, the R4 exact constant-slope matrix gives an
instantaneously joined, equal-speed radius excursion `r→Qr→r` the identity

\[
 \det T_m=1,\qquad
 \operatorname{tr}T_m=
 2-4m^2(m^2-1)\frac{(Q-1)^2}{Q}.
\]

The eigenvalue magnitudes of that discontinuous-slope screen are independent
of the common speed; the `v/√(1−v²)` entries alone must not be presented as
an independent spectral-gain mechanism. For `m=2,Q=2.2`, the small
eigenvalue has magnitude about `1/29.38`.

The *complete C² loop* was integrated separately. For the seed above it
has the following numerical linear transfers:

| Mode | trace | determinant | smaller eigenvalue magnitude |
|---:|---:|---:|---:|
| 2 | 255.59440345 | 1.0000000000015 | .003912508624 |
| 4 | 3517.95934879 | .99999998525 | .000284255719 |

The smooth turns therefore cannot be replaced by the instantaneous seed
matrix. This finite loop supplies strong attenuation *on its stable
direction*. Matching that direction to a planar core is an additional
condition. The initial `alternative-neck-symmetric-seed.json` does **not**
satisfy that condition: its core directional residuals are approximately
`.142` and `−.111`.

## 4. A shorter resonant provider

The working nonlinear BVP configuration is
`computations/alternative-neck-resonant-profile.json`:

```
ramp_law = hermite_boost_neck
delta = .09709375
vu = .25
vd = .96
start_acceleration = .45
boost_speed = .8689804963021789
boost_length = .23484080028265214
coast_outward = 0
loop_radius = .35
loop_ratio = 1.1
loop_speed = .985
loop_curvature = 8
descending_turn_curvature = 8
descending_sync_curvature = 8
terminal_peak_fraction = .1
```

Here `delta` remains the actual initial Hermite radius increase, and `vd`
is the actual speed of the inward leg preceding the transition to the
fixed loop speed. Both can therefore be used as the existing dual BVP's
physical design controls. The initial Hermite duration is solved exactly
from `δ=vu·S/2+k0·S²/12`.

For this profile, the two linear core directional residuals are below
`5.1e−10`. The total background height is `1.83080526`; the predicted
terminal mode-two height at core amplitude `.38` is `1.67615e−4`.
The report `alternative-neck-small-loop-roots.json` also includes the
near-unit radius-ratio case and ratios `1.3,1.5`. These are design roots,
not validations of a strong nonlinear prefix.

In particular, the `.869` boost is **not** the verified `.65` boost from
section 1. Starting it from the old fixed `.38` core by direct M96 IVP
exhausted the Frenet-domain margin at `s≈.804`; the last saved sample already
had principal curvature above 50. The failed run is retained as
`alternative-late-boost-resonant-m96.json`. It neither validates this
strong candidate nor rules out a BVP that adjusts the free higher core
modes and metric controls.

## 5. Actual nonlinear dual-core prefix solves

The reference fourth support coefficient in these runs is
`−q/(10√2)`. Higher core coefficients are solved, and `delta,vd` are design
unknowns. The nonlinear solves use the general support-core angular chart
and the frozen small source snapshot, not a live source worktree.

| q | modes | nodes | sampled metric ℓ¹ | max sampled κ | height max | terminal height max |
|---:|---:|---:|---:|---:|---:|---:|
| .001 | 6 | 565 | 3.91934e−9 | 8.0195032 | 1.8324178 | 4.40150e−7 |
| .003 | 8 | 748 | 2.57844e−9 | 8.0587165 | 1.8355905 | 1.31481e−6 |
| .008 | 10 | 823 | 6.52141e−9 | 8.1562155 | 1.8432294 | 3.46918e−6 |
| .020 | 12 | 1221 | 4.01854e−8 | 8.4086772 | 1.8600290 | 8.45862e−6 |

Their frozen physical parameters are, respectively,

```
q=.001: delta=.09744644563591624, vd=.9601476759853184
q=.003: delta=.09814436039628893, vd=.9604419783903627
q=.008: delta=.09984719083351601, vd=.9611713558413112
q=.020: delta=.10371128609890298, vd=.9628817017888675
```

The physical finite-linear-port boundary residuals are below `8.1e−19`
in these samples. The checkpoints are
`alternative-neck-q001-m6.json.gz` and
`alternative-neck-q003-m8.json.gz`, `alternative-neck-q008-m10.json.gz`,
and `alternative-neck-q020-m12.json.gz`, each accompanied by its
`_coeff_00.npy.gz` coefficient chunk. The metadata records the chunk's
filename and SHA256; both files are needed for restoration. Their schemas retain
`general-support-core-blend-v1`, the complete `frozen_profile`, the tagged
physical cut, physical meridian length, free core coefficients, and the
source hashes for the adapter chain.

This table is amplitude continuation with changing metric controls. It is
**not** a fixed-metric refinement table. Neither the local curvature values
nor a small linear-port residual proves reach or matching to the actual
nonlinear tail.

All four rows used the inherited `legacy` numerical meridian chart.
Changing the two physical controls moves the neck's internal physical
breakpoints nonuniformly. The subsequent `all-knots` chart fixes every
current physical breakpoint at its reference numerical knot. This is a
change of numerical coordinates, not a change of the physical metric.
The exact choice is now an explicit command-line argument and output field.

### 5.1 Where the curvature growth occurs

`computations/alternative-neck-curvature-map.py` reconstructs the saved
Cartesian first and second jets, including the actual height mean, then
computes principal curvatures. It first samples the complete physical
meridian and angles, then locally refines a maximum within each segment.
It does not replace the actual second fundamental form by that of the
rotational background.

For the `.008` checkpoint, the report
`alternative-neck-q008-curvature-map.json` gives:

| Segment | locally refined maximum κ |
|---|---:|
| First descending turn | 8.15657908 |
| Descending speed synchronization | 8.15473257 |
| Outward loop turn | 8.08433746 |
| Inward loop turn | 8.02930040 |
| Terminal connector turn | 8.00184433 |

The global sampled/refined maximum is on the first descending turn, at
`s=.9260615902`, angular coordinate approximately `π/2`. There the actual
orthonormal second fundamental form has
`L=8.15657908`, `N=.45429017`, and `M` within `3e−9` of zero. The
rotational background has meridian curvature exactly eight on this
plateau. Lowering only the first turn would leave the synchronization
segment with nearly the same curvature cost.

### 5.2 A compact K=7 redesign to test nonlinearly

The next design changes only the first descending turn and its speed
synchronization to curvature bound seven; the loop and terminal connector
remain at eight. At the old `.008` frozen controls this adds background
height `.0328327373`. That is a comparison of metric definitions, not an
actual surface continuation.

Solving the two linear core matching conditions with controls `delta,vd`
on the branch below the loop speed did not find a root: the best bounded
trial at `vd=.9849` retained residuals approximately `−.01147,.00105`.
The physical branch *above* the loop speed does have a linear root:

```
delta = .0942255680664908
vd = .9991452309123945
descending_turn_curvature = 7
descending_sync_curvature = 7
```

Its two directional residuals are `−1.97e−9,1.23e−11`, background upper
height is `1.63925159`, and the linear prediction for the terminal
mode-two height at `q=.38` is `4.00783e−5`. The profile is saved as
`computations/alternative-neck-k7-resonant-profile.json`; the full
linear report is `alternative-neck-descending7-highspeed-linear-root.json`.

This branch remains inside the physical speed domain, with
`1−vd²≈.001709`, but that small background margin needs an actual
nonlinear solve. The source's old generic restriction `vd<.97` was an
artificial design guard. The dual solver now applies `vd<1` only to this
neck provider, leaving the underlying square-root and embedding guards
in place. A small-amplitude actual solve is needed before using this
linear root as an amplitude-continuation seed.

### 5.3 Actual K=7 continuation and the high-speed limitation

The high-speed K=7 root was then solved nonlinearly using the new
`all-knots` numerical chart. All uncontrolled metric fields were fixed;
`delta,vd` remained the two physical design controls.

| q | modes | final nodes | sampled metric ℓ¹ | max sampled κ | height max | terminal height max | minimum sampled Frenet margin |
|---:|---:|---:|---:|---:|---:|---:|---:|
| .001 | 6 | 672 | 2.35226e−10 | 8.0024836 | 1.6409167 | 1.04149e−7 | .00160394 |
| .003 | 8 | 776 | 6.28641e−10 | 8.0071561 | 1.6441857 | 3.04331e−7 | .00140429 |
| .008 | 10 | 1220 | 1.55380e−9 | 8.0168863 | 1.6520128 | 7.54022e−7 | .000963906 |
| .011 | 12 | 1188 | 3.70120e−9 | 8.0211016 | 1.6564817 | 9.85531e−7 | .000739767 |

The `.011` frozen controls are
`delta=.09815552472469687`, `vd=.9993972410351921`.
The checkpoints are `alternative-neck-k7-q001-m6.json.gz`,
`alternative-neck-k7-q003-m8.json.gz`,
`alternative-neck-k7-q008-m10.json.gz`, and
`alternative-neck-k7-q011-m12.json.gz`, with their coefficient chunks.
These are again changing-metric amplitude continuation, not a
fixed-metric refinement table.

The actual curvature and height improved over the K=8 branch, while the
Frenet square-root margin became the immediate numerical restriction.
For the `.008` map, `alternative-neck-domain-map.py` locates its sampled
minimum near the end of the first descending turn:
`s=1.2863096448`, `psi=π/2`, `a=1.1612638031`,
`a′=−.9993297572`. The actual margin is `.000963906`, compared with the
rotational background value `.001340036`. The loop still has margin
above `.0295`, and the terminal connector above `.00515`. This separates
the first-turn speed restriction from the later loop's geometric costs.

The direct `.008→.015` warm solve encountered an invalid Newton trial
with margin `−6.45e−7`. An intermediate `.011` solve succeeded, but the
subsequent `.011→.015` trial also encountered a negative margin,
`−2.05e−6`, before a completed collocation iteration. The two failure
summaries are retained separately as `alternative-neck-k7-q015-m12-summary.json`
and `alternative-neck-k7-q015-m12-warm011-summary.json`. They do not prove
that a `.015` solution or a different chart cannot exist.

### 5.4 Moving the K=7 design root to a safer fixed speed

A single targeted linear solve fixed `vd=.98` and varied only the initial
Hermite increase and the late-boost length. No curvature or profile grid
was scanned. Five least-squares evaluations gave

```
delta = .09815441405341828
boost_length = .2070595516254682
vd = .98
```

The residuals are `−3.50e−13,4.66e−14`. The complete background upper
height is `1.7704610534`; the predicted mode-two terminal height at
`q=.38` is `1.32220249e−4`. All loop and curvature settings are unchanged.
The new profile is
`computations/alternative-neck-k7-v098-resonant-profile.json`;
`alternative-neck-k7-v098-linear-root.json` records the solve and all
evaluations. The reproducible targeted solver is
`computations/alternative-neck-fixedspeed-root.py`.

This candidate trades some of the high-speed height advantage for a
background speed margin `.0396`. Its natural next nonlinear controls are
`delta,boost_length`, with `vd` genuinely fixed at `.98`; allowing `vd`
to move again would not test that design choice.

### 5.5 Nonlinear continuation with vd exactly .98

The dual solver now supports `--second-control boost_length`. The first
two parameters are physical offsets of `delta,boost_length`; `vd` remains
exactly the value `.98` in the input profile. The same positive Frenet
root guards and complete physical Cartesian audits remain active.

| q | modes | final nodes | sampled metric ℓ¹ | max sampled κ | height max | terminal height max | minimum sampled Frenet margin |
|---:|---:|---:|---:|---:|---:|---:|---:|
| .001 | 6 | 693 | 7.27437e−10 | 8.0082372 | 1.7725786 | 3.47475e−7 | .00515285 |
| .003 | 8 | 803 | 5.92893e−10 | 8.0249625 | 1.7767590 | 1.03962e−6 | .00515233 |
| .008 | 10 | 868 | 1.52556e−9 | 8.0681940 | 1.7869046 | 2.75411e−6 | .00515103 |
| .020 | 12 | 900 | 3.85395e−9 | 8.1794764 | 1.8096390 | 6.78253e−6 | .00514800 |
| .040 | 14 | 928 | 3.76368e−9 | 8.3852322 | 1.8432729 | 1.32558e−5 | .00514317 |
| .055 | 16 | 970 | 7.46444e−9 | 8.5524391 | 1.8656467 | 1.79363e−5 | .00513969 |
| .070 | 18 | 977 | 1.36712e−8 | 8.7292142 | 1.8860075 | 2.24808e−5 | .00513634 |
| .085 | 20 | 1024 | 4.71830e−8 | 9.2636034 | 1.9046469 | 2.68950e−5 | .00513310 |

The `.008` frozen controls are
`delta=.10111855327625638`,
`boost_length=.20618084952939544`; the `.040` frozen controls are
`delta=.11162015607074556`, `boost_length=.20257909428553353`.
Checkpoints use the prefix
`alternative-neck-k7-v098-q001-m6`, `...-q003-m8`, and `...-q008-m10`.
The next two are `...-q020-m12` and `...-q040-m14`.
The `.055` checkpoint is `...-q055-m16`, with frozen
`delta=.11595398674098607`, `boost_length=.20087404640295486`.
The `.070` controls are `.11999323911576933,.19917059559728914`;
the `.085` controls are `.12378067503769839,.1974723533893321`.
The corresponding checkpoint suffixes are `q070-m18` and `q085-m20`.
Each has a compressed metadata file and its compressed coefficient chunk.
The all-knots numerical chart is recorded in the metadata. Fixing `vd`
alone does not fix the metric: the other two physical controls change in
this amplitude-continuation table.

The first run can be reproduced by:

```
python topics/visible-flex-larger-amplitude/computations/alternative-neck-bvp.py \
  --source-topic /workspace/scratch/83b864ada613/visible-flex-source/topics/visible-flexible-closed-surface \
  --port topics/visible-flex-larger-amplitude/computations/alternative-neck-provider-smallcut30-port.json \
  --profile topics/visible-flex-larger-amplitude/computations/alternative-neck-k7-v098-resonant-profile.json \
  --q .001 --modes 6 --angular 128 --nodes 401 --max-nodes 3000 --tol 2e-6 \
  --meridian-chart all-knots --second-control boost_length \
  --out-prefix topics/visible-flex-larger-amplitude/notes/alternative-neck-k7-v098-q001-m6
```

The `.003` and `.008` runs add `--restart` with the previous compressed
metadata file, raise the angular/mode resolutions to `192/8` and
`224/10`, and use tolerances `1e−6` and `8e−7`. The physical geometry is
reconstructed and converted before each new nonlinear solve; the old
trajectory is not relabeled as a new solution.

The first request for `.07/M18` was rejected in the BVP constructor
because the existing physical linear port supplies only sixteen modes.
No nonlinear solve started. This interface limit is recorded in
`alternative-neck-k7-v098-q070-m18-port-limit.json`; an M16 continuation
and an actual same-parameters higher-mode linear-port computation are
separate from that rejected call. Missing high-mode slopes must not be
filled by extrapolation.

The subsequent `.04→.07/M16` attempt did start but failed to converge:
after two collocation iterations its maximum residual was `.03815`,
the boundary residual was `6.59e−7`, and the next refinement would exceed
the 3500-node limit. Its domain audit records 56 rejected Newton trials
and a minimum damping fraction `1/128`. The checkpoint retains
`solver_success=false` and has no successful metric/curvature audit.
The smaller `.04→.055/M16` continuation in the table then succeeded.

For later modes, the numerical-tail work generated an actual 32-mode
linear port with the same physical parameters and cut. The first sixteen
slopes remain exactly the old values. The new slopes at frequencies
34 through 64 were recomputed with 2048 steps, with a 1024-step comparison
giving maximum relative difference `4.78e−9`, including the nearby
Dirichlet-pole slopes. The file
`computations/alternative-neck-provider-smallcut30-port32-r2048.json`
adds only the existing neck connector tag to that port and records its
parent hash; no slope is extrapolated. The comparison is in
`notes/numerical-m2-tail-smallcut-30-linear32-comparison.json`.

The `.055→.070/M18` continuation using that extended port succeeded. The
next `.085/M20` run also converged; it explicitly selected the optional
`refresh` Newton backend. No claim that a backend change caused success
is made without its fallback counters and a relevant comparison.

At `.085`, the sampled product `kappa_max*(2*height_max)` is already about
`35.29`. Since the double mirror has diameter at least twice that height,
this particular numerical design exceeds the necessary local-curvature
budget `1/.03` for the desired reach/diameter ratio. This is a reason to
redesign the turn curvature while continuing the amplitude project, not
an impossibility statement about other profiles. The explicit
changed-metric warm mechanism and first loop-eight to loop-7.5 design
are documented in `alternative-neck-design-warm.md`.

## 6. Reconstruction and continuation

The provider is `computations/alternative-neck-provider.py`. After loading
the source classes and any short-bridge patch, but before constructing a
flow or BVP, call `install()`. For this metric kind use
`port=tagged_port(port,frozen_profile)`. The cut tag is

```
_prefix_bridge = {
  kind: finite_neck_terminal_v1,
  radius: .35,
  speed: .985,
  curvature: 8,
  peak_fraction: .1
}
```

The tag values are derived from the frozen profile, not inferred from a
previous checkpoint. `root_dual_core_bvp.py` and the general checkpoint
pullback now have conditional hooks for `ramp_law=hermite_boost_neck`.
The standalone adapter `computations/alternative-neck-bvp.py` installs the
same provider and records its source dependencies in the output metadata.

For example, the `.003` run used the following arguments, with paths
relative to the repository root:

```
python topics/visible-flex-larger-amplitude/computations/alternative-neck-bvp.py \
  --source-topic /workspace/scratch/83b864ada613/visible-flex-source/topics/visible-flexible-closed-surface \
  --port topics/visible-flex-larger-amplitude/computations/alternative-neck-provider-smallcut30-port.json \
  --profile topics/visible-flex-larger-amplitude/computations/alternative-neck-resonant-profile.json \
  --q .003 --modes 8 --angular 192 --nodes 241 --max-nodes 2000 --tol 1e-6 \
  --meridian-chart legacy \
  --restart topics/visible-flex-larger-amplitude/notes/alternative-neck-q001-m6.json.gz \
  --out-prefix topics/visible-flex-larger-amplitude/notes/alternative-neck-q003-m8
```

The next substantive tasks are actual tail coupling, amplitude continuation
with curvature and physical diameter tracked, and fixed-metric refinement
of a selected solved profile. A mismatch, domain failure, or large
curvature on one finite Cauchy trial remains evidence about that trial; it
must not be relabeled as a general nonexistence theorem.
