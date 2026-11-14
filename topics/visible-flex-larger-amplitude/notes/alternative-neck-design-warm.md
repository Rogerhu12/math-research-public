# Explicit metric-design continuation of the finite neck

This is a numerical initial-guess construction. It does **not** solve the
new metric problem, and it is not fixed-metric refinement. The script is
`computations/alternative-neck-design-warm.py`.

## Coordinate construction

Let the old and proposed physical necks have the same ordered segment and
knot topology. With one common list of numerical knots, construct the
positive C² maps

\[
 S_o:[0,1]\longrightarrow[0,L_o],\qquad
 S_n:[0,1]\longrightarrow[0,L_n]
\]

through the respective old and new physical knot lists. The existing
`root_neck_chart.NeckChart` supplies these maps. It is applied separately
to the two physical knot lists; the old numerical collocation chart need
not have been the same implementation, since the saved old polynomial
already uses physical meridian coordinates.

Write the old and new reference angular charts as
`theta=Theta_o(s,eta)` and `theta=Theta_n(s,psi)`. They are increasing
periodic C² maps in the angular variable. Set

\[
 \eta(t,\psi)=\Theta_o(S_o(t),\cdot)^{-1}
                  \bigl(\Theta_n(S_n(t),\psi)\bigr),
 \qquad
 G(t,\psi)=F_o(S_o(t),\eta(t,\psi)).
\]

Before finite Fourier projection, `G` has exactly the old image: the radial
map is onto and each angular map is a circle diffeomorphism. The inverse
function theorem and positive angular derivative give C² regularity of
the inverse, so this intermediate composition is C² when the saved map
is C².

This image identity does not identify the metrics. In the common
coordinates the old and proposed metric tensors are respectively

\[
 S_o'(t)^2dt^2+a_o(S_o(t))^2d\Theta_n^2,
 \qquad
 S_n'(t)^2dt^2+a_n(S_n(t))^2d\Theta_n^2.
\]

They usually differ. The script records both complete physical profiles,
both physical lengths, both physical knot lists, and the radial-map
derivative range. Undeclared changes of uncontrolled profile fields are
rejected. Tail parameters and the physical cut must remain unchanged.

## Fourier state and the height mean

The intermediate Cartesian positions are compared with the new reference
geometry and projected into the new cylindrical Fourier basis. Its
angular-mean height is included when measuring the intermediate image
projection error. The basis itself has no constant vertical coefficient.
Consequently, the subsequent nonlinear BVP reconstructs its own mean
height by integrating its solved velocity. The record explicitly describes
this additional initial-guess change; a dropped mean is not represented
as a coordinate identity or a solved surface.

The prescribed primary and secondary core coefficients stay fixed during
this design step. Higher core coefficients are carried into the new
parameter normalization. The default `keep_offsets` forecast retains the
old nonlinear offsets from its base design while applying them to the
new base design. `keep_physical` instead initially retains the old actual
values of the two controlled fields. Both are initial guesses only.

## Identity check

At the actual `.04/M14` checkpoint, keeping all metric fields unchanged
and running the new conversion with `--check-only` gives:

- radial reparameterization derivative range exactly `[1,1]`;
- sampled image projection error `3.08293e−13`;
- angular-mean height correction at most `2.22045e−16`;
- inlet correction at most `1.88837e−13`;
- complex-step state-Jacobian relative discrepancy `1.89274e−15`.

The complete diagnostic is
`alternative-neck-design-warm-identity-check-summary.json`. It is an
initial-guess/Jacobian check, not a newly solved checkpoint.

## First changed metric: loop curvature 8 to 7.5

Keep `vd=.98` and both descending-turn curvature bounds at seven. Change
only `loop_curvature` to `7.5`; by the provider definition this also changes
the finite terminal connector's turn bound, while retaining its prescribed
physical cut jets. A single linear solve of `delta,boost_length` gives

```
delta = .09818024760824497
boost_length = .20687468418051796
```

Its two normalized directional residuals are below `4.1e−13`. The complete
background height is `1.8040734642`, an increase of `.0336124108` over the
loop-eight base design. The predicted mode-two cut height for primary
core amplitude `.38` is `1.15535692e−4`. These are linear/background
calculations, not strong-core or reach claims.

The profile and linear report are
`computations/alternative-neck-loop75-v098-resonant-profile.json` and
`alternative-neck-loop75-v098-linear-root.json`. The first actual test
uses the successful `.07/M18`, loop-eight checkpoint as a changed-metric
warm input, with `--design-fields loop_curvature`, the same `.07`
amplitude, the same physical tail, and fresh nonlinear solving. Its
output prefix is `alternative-neck-loop75-v098-q070-m18`.

That first image-preserving intermediate guess was not inside the new
Frenet square-root domain: the solve stopped before a completed Newton
iteration with margin `−.000572066`. This is a failure of that initial
guess, not a solution/nonexistence result for the proposed metric. The
failure summary is retained separately.

## Explicit radius-scaled latitude guess

The optional `--design-latitude-map scale_radius` keeps the preceding
radial/angle matching but then deliberately changes each latitude. Let
`lambda(t)=a_n(S_n(t))/a_o(S_o(t))`, and let `H_o(S_o(t))` be the saved
old angular-mean height. Replace the intermediate Cartesian latitude by

\[
 \widetilde G=
 \left(\lambda G_x,\lambda G_y,
 H_o+\lambda(G_z-H_o)\right).
\]

The radius ratio and the center height are angularly constant. Hence
`d_psi G_tilde=lambda d_psi G`. If the old latitude has its target metric,
the new one has the proposed target angular metric exactly:

\[
 |\partial_\psi\widetilde G|^2
 =\lambda^2 a_o(S_o)^2(\partial_\psi\Theta_n)^2
 =a_n(S_n)^2(\partial_\psi\Theta_n)^2.
\]

The same statement transfers the old finite angular metric error. The
meridian and mixed metric components are not asserted to match. This
rescaling changes the image and is explicitly labeled as a design
deformation before the new nonlinear solve. It is C² when the profiles,
coordinate maps, center height, and saved map are C².

The script reports its radius-ratio range, angular metric discrepancy,
Fourier projection error, and the projected initial Frenet margin. The
normal solver retains its domain guards. The original `preserve_image`
option remains the default for reproduction; the scaled retry uses the
distinct output prefix `alternative-neck-loop75-v098-q070-m18-scaled`.

That scaled retry succeeded as a new nonlinear finite-linear-port prefix
at the same `.07/M18` amplitude. It has sampled metric error
`6.39611e−9`, maximum sampled principal curvature `8.32121570`, height
`1.91951864`, cut-height coefficient maximum `1.95093e−5`, and minimum
Frenet margin `.00513852`. The old loop-eight values were respectively
`1.36712e−8`, `8.72921419`, `1.88600746`, `2.24808e−5`, and `.00513634`.
The actual new controls are `delta=.11998304888963393` and
`boost_length=.1990855144190508`.

The scaled initial guess's radius ratio was in
`[.96594091,1.01567454]`; its angular metric error before projection was
`5.31706e−9`, position projection error `5.89874e−11`, and projected
Frenet margin `.00513634`. The subsequent nonlinear solve used 963 nodes
and five collocation iterations. Its optional refresh fallback counters
were both zero, so this success is not evidence that the fallback itself
was needed.

## Isolating the short speed synchronization

The original loop-eight `.085/M20` solution shifted the curvature maximum
to the short synchronization from speed `.98` to `.985`. A local Cartesian
jet refinement finds curvature `9.2637070` there (background bound seven),
compared with `8.8859572` on the outward loop turn and `8.6271171` on the
first descending turn. The report is
`alternative-neck-k7-v098-q085-curvature-map.json`.

The next single design change therefore keeps first-turn bound seven and
loop bound 7.5, but lowers only `descending_sync_curvature` to two. The
longer synchronization replaces a portion of the nearby almost equal-speed
coast. The actual linear re-match gives

```
delta = .098180643250016
boost_length = .20687148120124016
```

with directional residuals below `4.7e−11` and background height
`1.8039294592`. Thus its background height is actually `.0001440050`
lower than the sync-seven design. Its predicted mode-two cut height at
primary amplitude `.38` is `1.14648133e−4`. These are background and
linear values; the new full nonlinear design test starts at `.07/M18`
from the successful loop-7.5 checkpoint, using the explicit radius-scaled
warm mechanism and declaring only `descending_sync_curvature` changed.

This `.07/M18` design test succeeded in five collocation iterations at 958
nodes. Its metric error is `1.85313e−8`, maximum sampled curvature
`8.32119773`, height `1.91937709`, cut-height maximum `1.93642e−5`, and
minimum Frenet margin `.00513863`. The height decreased by `.000141557`
from the actual sync-seven map. The almost unchanged global curvature
maximum means that a different segment now supplies that maximum at this
amplitude; it does not negate the removal of the synchronization's own
curvature cost. The checkpoint is
`alternative-neck-loop75-sync2-v098-q070-m18.json.gz` and its coefficient
chunk. Amplitude continuation of this new profile to `.085/M20` follows.

Both successful same-amplitude reshapes in this note change the physical
metric: loop-eight to loop-7.5, and then synchronization-seven to
synchronization-two. They are new nonlinear design solutions, not
fixed-metric refinement. Their saved `frozen_profile` records the actual
new controls and all remaining physical profile parameters. A subsequent
amplitude step also re-solves the design controls and is not fixed-metric
refinement.

The direct `.07/M18` to `.085/M20` amplitude step on the loop-7.5,
synchronization-two profile failed after 244.6 seconds with an adaptive
Frenet-domain margin of `−1.02064e−9`. No successful terminal map or
curvature localization is inferred from that iteration. The failure
summary is `alternative-neck-loop75-sync2-v098-q085-m20-summary.json`.
The next test halves the amplitude increment to `.0775/M20`, starting
again from the successful `.07` checkpoint; this is a smaller continuation
step, not a relaxation of the domain or residual gates.

The smaller `.0775/M20` step succeeded in five collocation iterations at
992 nodes. Its metric error is `3.19629e−8`, sampled maximum curvature
`8.47338675`, height `1.92889848`, cut-height maximum `2.12508e−5`, and
minimum Frenet margin `.00513722`. The actual new controls are
`delta=.12190328479931874` and `boost_length=.1982492277029178`.
The saved prefix is `alternative-neck-loop75-sync2-v098-q0775-m20.json.gz`
with its coefficient chunk. This success after a smaller amplitude step
does not identify the cause of the failed larger step.

Actual Cartesian jet localization on the `.07` map puts the peak on the
first descending turn: `8.321784685` at `s=1.006667701`, `psi=pi/2`.
The outward and inward loop-turn peaks are `8.03150156` and `7.72360026`,
respectively. These sampled and locally optimized values are recorded in
`alternative-neck-loop75-sync2-v098-q070-curvature-map.json`; they are
not continuous curvature bounds.

The exact background identity is now proved in
`../results/R13-slower-speed-sync-height.md`. At the actual frozen
loop-7.5 `.07` controls, the admissible range has
`Kmin=.0343239152`; the exact formula predicts background height change
`−.000143442744` for synchronization curvature seven to two. Direct
evaluation of the same background profile agrees within `2e−16`; these
values are recorded in `alternative-sync-height-identity-check.json`.

## First descending turn: seven to 6.75

The `.0775/M20` Cartesian localization confirms that the first descending
turn still supplies the maximum: `8.473435937` at `s=1.016188902`,
`psi=pi/2`. The outward loop peak is `8.098549828`, while the inward loop
and terminal peaks are `7.75137560` and `7.51055873`. The diagnostic is
`alternative-neck-loop75-sync2-v098-q0775-curvature-map.json`.

The next design therefore changes only `descending_turn_curvature` from
seven to `6.75`; loop curvature `7.5`, synchronization curvature two,
and inward speed `.98` remain fixed. This change has a positive background
height cost. At the successful `.07` map's actual frozen inputs, the turn
plus following coast has height coefficient `1.86161671366` multiplying
`1/K`. Hence the fixed-input background height increase is
`.009849823882` and the length increase is `.01227614144`. This is a
background scaling calculation, not a prediction of the new actual
noncircular map.

Re-solving the linear two-mode matching equations gives

```
delta = .09924103685702657
boost_length = .1935415543336927
```

with maximum normalized directional residual `2.10e−9`, background height
`1.8080071221`, and predicted mode-two cut height `1.13132359e−4` at core
amplitude `.38`. The linear re-match's background height increase over
the preceding resonant base is only `.0040776629`, because the controls
also change. These two different comparisons must not be conflated.

The fresh nonlinear test uses the successful `.0775/M20` map, the explicit
radius-scaled latitude guess, and `--design-fields descending_turn_curvature`.
It is a new physical metric and not fixed-metric refinement. The output
prefix is `alternative-neck-first675-loop75-sync2-v098-q0775-m20`.
