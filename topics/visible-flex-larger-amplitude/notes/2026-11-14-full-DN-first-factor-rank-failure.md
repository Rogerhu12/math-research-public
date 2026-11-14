# First actual full-DN attempt: failed linear solve before any accepted step

Evidence: [public Actions run 43584222071](https://github.com/Rogerhu12/math-research-public/actions/runs/43584222071), source `a47c0f96b7a5843deb8d8ffea181beab6eb6696e`, coupling artifact `14109339087`. The job published all its actual outputs under `notes/public-actions-43584222071-1-coupling/`. This note reads those outputs and the original job log; no numerical solve was rerun locally.

## 1. What actually passed

The complete boundary implementation check passed its **unchanged** threshold `5e-5`. The two fourth-order Richardson levels gave maximum relative directional error `7.280355356577817e-9`. The original coarse centered-difference maximum `5.049653970341734e-5` remains in the record, and all significant second-order errors contracted as required. This is a glue/Jacobian implementation check using the explicitly labeled original linear-graph reference, not a nonlinear BVP acceptance.

The actual full-DN solve then imported exactly one completed true zero-H response and its finite variational DN Jacobian. The imported complete response was previously computed by the unmodified native nonlinear worker. The source, full config, cut, original physical parameters, all 96 zero heights, and the completed audit/J bundle were checked by the strict cache adapter. The current worker emitted its ready event but received no new nonzero-H solve request during this attempt. The failure below therefore did not occur in a new nonlinear tail solve.

The independent zero-H Jacobian audit also completed in this run. The true finite shooting Jacobian is distinct from `ready.linearD`; the latter was not substituted as the actual DN matrix in the coupled solve.

## 2. The failed finite solve

The state had 290 physical components, 96 constant core components and 3 constant scalar controls: total dimension 389. The separated system had 293 left rows and 96 right nonmean material DN rows. It used the saved 690-node warm field, preserving every old node exactly, and the original complete equations and acceptance gates.

At the first factorization:

| Quantity | Returned value |
| --- | ---: |
| Mesh nodes | 690 |
| Reduced terminal matrix size | 96 by 96 |
| Reduced condition estimate | 7.152884712357285e17 |
| Maximum linear RHS component | 0.00711059469197025 |
| Maximum actual linear residual | 0.004099778897826766 |
| Relative actual linear residual | 0.5765732790896527 |
| Maximum computed correction component | 7952.048727741045 |
| Initial nonmean boundary residual | 0.0019641614811819466 |

The initial factorization took about 89.1 seconds. Its first linear correction did not solve the finite linear system accurately. The original line search then rejected every trial at Newton iteration zero. **No Newton update was accepted.** The log's eventual generic “singular Jacobian” status must not conceal this more specific measured failure.

The outer SciPy controller next reported a NaN RMS on the unchanged field, inserted 188 nodes, and encountered an invalid current state on the next Newton call. It returned status 2 after two mesh rounds, with 878 nodes, no finite maximum RMS, and boundary residual `0.00196416148118607`. The driver correctly wrote phase `inner-newton-not-accepted` and `new_coupled_finite_acceptance=false` and exited 2. There is no accepted full-DN output or new closed field from this run.

## 3. Which state can be reused

The original `prepared.json.gz` and `outer-00-newton-checkpoint.json.gz` have **identical mesh, state and RHS arrays**. The latter checkpoint is the original 690-node initial field, not a later improvement.

The 878-node `outer-00-pending.json.gz` retains all 690 original mesh positions. Their state values differ by at most `1.734723475976807e-18`, from interpolation roundoff. All scalar controls remain exactly zero. The additional 188 rows are interpolated mesh refinement after the failed update, not a successful nonlinear continuation. The next new design should retain the verified original 690-node warm and the completed zero-H anchor; it should not call the 878-node file an improved accepted checkpoint.

The original prepared warm is a finite initial guess. Its passing nodes-and-midpoints preflight did not guarantee valid states at every point used later by the solver's RMS estimator. The latter evaluates each cubic interval also at fractions

\[
\tfrac12\pm\tfrac12\sqrt{3/7}.
\]

Those actual query points must be checked explicitly before another coupled solve. The new entry records their locations and the original point-domain quantity

\[
\beta^2=1-\left(\frac{a'}{a\kappa_{\rm curve}}\right)^2.
\]

It does not clip a negative value or change the original domain. Old saved nodes stay unchanged. For a zero-control warm, newly inserted points may sample the already defined original analytic taper/material-circle seed rather than an invalid point of its coarse Hermite interpolant. If that original seed itself is invalid there, the attempt retains the actual point and fails explicitly.

## 4. Why the old coast control is a plausible near-null direction

The dimension count alone is not a rank argument. The third old scalar control is supported entirely in the coast where this particular warm has already tapered to a material circle. In the exact axisymmetric limit, a compactly supported variation of a(s) that vanishes with its first two jets at both support endpoints changes the vertical mean accumulated along the circle family. At the final fixed physical cut it does not create a nonmean height or nonmean slope. The right boundary here contains only nonmean DN rows, so it cannot observe that control in this exact limit.

The finite projected material circle, earlier nonaxisymmetric portion and numerical transport can perturb that kernel. The actual condition estimate near `7e17` and failed linear residual are consistent with a serious rank/conditioning problem, but the old artifact did not save the full reduced SVD or its singular vectors. We do **not** infer an exact rank theorem for the actual 690-node matrix from this mechanism alone, nor assert that it is the only source of its ill-conditioning.

## 5. Separately named v2 design and actual diagnostics

The next executable entry is `geometry_20261114_full_dn_prefix_controls.py`. It uses the original complete driver, equations, 96 material modes, true tail client, QR factor, Newton, line search, RMS gate `1e-6` and BC gate `1e-11`. It changes only the explicitly named scalar design family: all three controls are now supported inside the actually nonaxisymmetric accepted prefix of length L, on

\[
(.05L,.30L),\quad(.35L,.60L),\quad(.65L,.90L).
\]

Each is the same width-squared normalized C2 bump, with normalized polynomial coefficients `[0,0,0,64,-192,192,-64]`, extended by zero. The full base scalar profile at p=0 remains identical. The original core and physical-cut scalar 0/1/2 jets remain fixed for all controls. This is a new metric-design family, not an accepted result or a promised rank improvement.

`geometry_20261114_prefix_controls_profile.py` serializes schema `complete-prefix-controls-scalar-profile-v2`, the exact binary64 support endpoints, polynomial convention, complete frozen p, and both the new profile and original base-profile source hashes. Its reconstruction uses these same supports. `geometry_20261114_prefix_controls_readout.py` and the new full-state closed reader use this v2 constructor. They cannot silently interpret a new p under the old prefix/turn/coast supports. A warm file from the old scheme is reused only when all its controls are zero.

The new actual run records:

- the original warm's RMS-query domain and each subsequent preflight round;
- each true 96-by-96 terminal reduced matrix and complete SVD;
- six smallest singular directions, their physical/core/control components, and the numerical drift of nominally constant rows during backward transport;
- the first original linear solve's residual by physical, constant-core, constant-control and boundary blocks.

These diagnostics leave the original QR solve and all original acceptance gates intact. The actual response rank, correction accuracy and nonlinear convergence must be measured. The new source was only statically inspected and AST-parsed locally; the numerical test belongs in public Actions.

## Original artifact hashes

- `full-DN/prepared.json.gz`: `136ae9e2b0c30700224ea773fe51aa980313ea00436978d41d556e2a5f152225`
- `full-DN/outer-00-newton-checkpoint.json.gz`: `fff08fd56cb6e41c6b16562730d30e1223b65f549e1fb79a3c1dc605a74935e5`
- `full-DN/outer-00-pending.json.gz`: `6064b03df181e425350b6923788ab10cf2d94588a8e97157849007d4cfb9f245`
- `full-DN/outer-00-anchor-tail.json.gz`: `3abed02dd338534a21b58537ca3294c479a696de075be8ea29f04bbc82b515c3`
- `full-DN/true-tail_imported-zero.json`: `a8310746d6b9b1542b7f3d45097dd1ba3de4756c89139d48ea4e4176f3f05cfb`
- `boundary-response/response-check.json`: `faf082d5a88704e00b33442a25394a39c5fefb30cced2aaa9ea752e4abc2d1f6`
- `zero-height-J-audit.json`: `6399790a1d1565102767e4a3b6b418915082e309f4c2e0195395b613f9cd6c35`
