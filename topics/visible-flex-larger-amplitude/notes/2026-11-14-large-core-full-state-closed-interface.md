# Complete large-core prefix to a finite closed readout

This interface is implemented in:

- `computations/geometry_20261114_large_core_saved_prefix.py`;
- `computations/geometry_20261114_large_core_closed_assembly.py`.

It is prepared for a **genuinely accepted complete physical-cut full-DN output**. At the time this interface was written no such output had been accepted. The interface creates neither a new nonlinear solution nor numerical evidence by itself. The existing open prefixes at 0.99, 0.996 and 0.9975 cannot be passed off as its required physical-cut input.

## 1. Input and source bindings

The prefix input must retain the complete state of size `3M+2`, all physical radial knots, saved frozen-control RHS values, the original law, all core coefficients, and the complete scalar-profile formula with every solved design control. It must report actual success, status zero, collocation RMS at most `1e-6`, audited BC residual at most `1e-11`, and physical frozen-control RMS at most `1e-6`. These are the original finite acceptance gates, not new relaxed gates.

The separately supplied native tail response must be the file named by the prefix's `actual_tail.final_response_sha256`. Its complete config must match `actual_tail.sources.input_config`. Its original nonlinear convergence, residual, full audit, and all `(3T+2)T` finite Jacobian entries are required. The radial Cartesian readout must bind those same config and response hashes. Thus a historical A tail, a zero-height calibration response, or an unrelated same-metric tail cannot be substituted for the new field's actual full H.

The source bundle must carry its verified public repository origin. The consumed original numerical modules and two frozen ready inputs are checked against the actual tail source ledger. The three original SHA-locked mode-capacity changes are loaded explicitly for the subsequent native readout. No private checkout is used.

The full finite material projection is recomputed using the actual augmented endpoint core and the original recorded angular grid. Its difference from all T actual saved H entries is reported. The small augmented endpoint-to-inlet core drift is retained as a separate number; it is not silently renamed zero. This check binds a finite operator. It does not certify the omitted continuous material-angle Fourier tail.

## 2. The physical field includes its complete mean

The new state order is

\[
(r_0,\ldots,r_M,t_1,\ldots,t_M,z_0,\ldots,z_M).
\]

Every entry is a physical coefficient. In the rotating normal-angle frame,

\[
F=(R,T,Z),\quad
F_\varphi=(R_\varphi-T,T_\varphi+R,Z_\varphi),
\]

\[
F_{\varphi\varphi}
=(R_{\varphi\varphi}-2T_\varphi-R,
  T_{\varphi\varphi}+2R_\varphi-T,Z_{\varphi\varphi}).
\]

The adapter rotates these Cartesian jets into world coordinates. The same angular operators are applied to the complete saved first and second physical radial jets. It uses the original physical quintic: saved binary64 y, saved RHS, and the original finite-ODE second derivative at each radial knot determine the unique degree-five polynomial on each physical interval. Saved-node queries return their original stored jets directly. No old small-field gauge or independently integrated old-A mean is added.

For the constant complete core c,

\[
\theta=\Phi_c(\varphi)
=\varphi+\sum_{m=1}^M\frac{(1-4m^2)c_m}{2m}\sin(2m\varphi),
\qquad \rho=\Phi_c'>0.
\]

The reader requires a positive complete-core rational R237 lower bound for rho relative to the independently reconstructed R236 reference. If this sufficient bound fails, it asks for a stronger density certificate rather than assuming global invertibility from a finite angle sample. The inverse is evaluated at the requested material angles, including shifted phases; it is not truncated to a second finite Fourier series.

Since this angle map is independent of s,

\[
F_\theta=F_\varphi/\rho,\qquad
F_{\theta\theta}=F_{\varphi\varphi}/\rho^2
                   -\rho_\varphi F_\varphi/\rho^3,
\qquad F_{s\theta}=F_{s\varphi}/\rho.
\]

`nine_jets(s,theta)` exposes all derivatives with radial order 0, 1, 2 and material-angle order 0, 1, 2. `material_jets` and the closed map's `prefix_jets` expose the six usual keys `pos,s1,s2,p1,p2,sp`. The vectorized `profile(s)` returns the entire frozen a, a', a'' formula. Its end and all breakpoints are retained. This is the interface for a future new-state geometry cover; a consumer must not index the new `3M+2` states using the old `3M+1` perturbation layout.

The material mean is read directly:

\[
\langle Z\rangle_\theta
=z_0+\tfrac12\sum_{m=1}^M z_m(1-4m^2)c_m.
\]

The same formula holds for the saved Z_s and Z_ss coefficients. These means are **information already contained in F**, not terms to add to F a second time.

## 3. One planar registration and one height offset

The native upper closing tail has vertical reflection sign sigma = -1. The existing native background remains separate from its small perturbation. Let m be the complete prefix material cut mean and m_tail the actual small tail cut mean. The sole absolute height offset is

\[
b=m-\sigma m_{\mathrm{tail}}.
\]

The upper tail uses

\[
Z=b-\sigma\int_r^{r_{\rm cut}}w(u)\,du+\sigma V_z,
\quad Z_r=\sigma(w+V_{z,r}),
\quad Z_{rr}=\sigma(w_r+V_{z,rr}).
\]

The adapter fits one proper SE(2) to corresponding complete cut positions. It applies the inverse registration to the **whole prefix**, including every derivative. The native tail, fixed caps and phase-rotation axis remain at their original common planar origin. There is no independent registration for different points, angles, derivative orders or radial stations. The rotation is defined by its recorded angle; its printed matrix is a floating evaluation. The unpatched six-jet differences remain in the result.

The prefix's core center and witness coordinates can move relative to the native cap axis under this normalization. The report therefore preserves the single registration, original and normalized core points, transformed core center, the native cap axis, and an actual phase-pi/2 core candidate. It explicitly does **not** reuse the old centered support gap as a proved held Hausdorff distance. The complete new surface, caps, phase axis, diameter and witness distance must be checked in this actual common frame.

## 4. A full angular finite C2 seam, with explicit metric cost

At the physical cut the prefix radial jets are

\[
F_r=F_s/a',\qquad
F_{rr}=F_{ss}/(a')^2-a''F_s/(a')^3.
\]

The adapter forms complete functions Delta_0(theta), Delta_1(theta), Delta_2(theta) by subtracting the actual native Cartesian tail cut jets from these normalized prefix jets. All their first and second angular derivatives are evaluated using the same complete inverse and saved field. No DFT of the prefix is used to replace these functions by a finite material-angle polynomial.

On a declared width W just inside the cut, with t from 0 to 1, the explicit correction is

\[
q_0(t)\Delta_0(\theta)+Wq_1(t)\Delta_1(\theta)
+W^2q_2(t)\Delta_2(\theta),
\]

\[
q_0=10t^3-15t^4+6t^5,\quad
q_1=-4t^3+7t^4-3t^5,\quad
q_2=\tfrac12t^3-t^4+\tfrac12t^5.
\]

The correction has zero radial 0/1/2 jets at its inner edge and the supplied Delta_0/Delta_1/Delta_2 at the cut. This defines a finite C2 glue for the represented continuous angular functions. Floating endpoint residuals and unpatched nine-jet norms on two angular grids are reported. The map differs from the original tail in this collar, and its metric error is measured. **This is not an exact isometric extension, an infinite nonlinear tail, or payment of the common-g convergence obligation.**

The original finite inner collar reaches the flat cuff with zero perturbation two-jet; the fixed cap and weak marker formulas are unchanged. This keeps the common theta chart at the cap. No nonlinear radial extension of the old phi-to-theta chart through a pole is attempted.

## 5. Executable Actions sequence

After an actual full-DN acceptance, use the already restored public source bundle and this accepted output's real final tail config/response:

```bash
python -u topics/visible-flex-larger-amplitude/computations/geometry_20261114_large_core_closed_assembly.py all \
  --checkpoint /path/to/full-dn/actual.json.gz \
  --tail-response /path/to/full-dn/actual-tail-final-audit.json.gz \
  --config /path/to/the-exact-input-T96-config.json \
  --port /path/to/the-original-port.json \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --out-prefix "$VISIBLE_OUT/refined-A-closed"
```

The compatibility basename does not mean A data are used; the new schema, all input hashes, complete H, and full-state reader identify the new field explicitly. The `all` action runs the existing actual-state radial readout at levels 1,2,4, then the original source-background primitive, then the finite closed-map consumer. An already completed same-response readout can be supplied with `--complete` to avoid repeating it. `plan` and `render` can be run separately with `--plan` and `--heights` for the latter. Original subprocess logs and explicit capacity manifests are retained.

Outputs preserve the existing consumer's `upper_rings`, `phase_angles`, `inputs`, `mean_gauge.upper_cap_height`, fixed-cap markers and piece labels. The held Hausdorff position-cover consumer can therefore consume a future full surface cover of this new map. The old finite Cartesian mesh, topology, phase point-cloud distances and finite normal-chord pair diagnostics are only preliminary numerical readouts. Their sampling limitations are retained.

## 6. Verification status and next actual gate

Only source/argument/schema inspection and Python AST parsing were performed for these new adapters locally. No complete-DN solution, new native-tail readout, closed mesh, C2 seam value, metric error, diameter, reach, or amplitude value is fabricated here. The first true full-DN result must pass through this actual-data pipeline in public Actions. Continuous coverage and fixed-metric discretization convergence remain subsequent mathematical work, regardless of whether the finite renderer succeeds.
