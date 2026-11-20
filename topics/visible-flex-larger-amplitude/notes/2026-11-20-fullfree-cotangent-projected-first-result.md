# Complete six-jet cotangent and first full-space geometric tangent direction

Date: 2026-11-20. Actual work by /root/fullclosed_solver. The executed direction in this note uses the original1845 node/midpoint stages. Later six-Gauss evidence is explicitly separated below.

## Exact complete-free point transpose

For one angle let B0, B1, B2 be the physical rotating-frame Fourier basis and its first and second angular derivatives, including the frame connection. For cotangents xi, alpha, beta, gamma, delta, epsilon of F, Fs, Fphi, Fss, Fsphi, Fphiphi, the nodal-stage cotangents are

Y*: B0^T xi+B1^T beta+B2^T epsilon;
U*: B0^T alpha+B1^T delta;
A*: B0^T gamma.

At a common-quintic midpoint these three rows are scattered to the two endpoint triples by the transpose of the literal3-by-6 Hermite weight matrix. At a node the corresponding triple is used directly. The constrained core position contributes gY_R,j-nu_j*gY_T,j to each free core coefficient; only the declared core A_XY and interior triples are free.

The analytic lift has radial scalar f and vertical scalar chi, with er, et depending on the core angle delta_theta. Write rho for the material circle speed and rho_phi for its derivative. Direct differentiation gives the additional scalar cotangents

- gtheta = f xi.et + f' alpha.et + f'' gamma.et - f rho beta.er - f' rho delta.er - f epsilon.(rho_phi er+rho^2 et);
- grho = f beta.et + f' delta.et -2 f rho epsilon.er;
- grho_phi = f epsilon.et;
- gH = chi xi_z+chi' alpha_z+chi'' gamma_z.

For core mode nu, qfreq=1-nu^2. Its extra derivative is gtheta*(qfreq/nu)*sin(nu phi)+grho*qfreq*cos(nu phi)-grho_phi*nu*qfreq*sin(nu phi). Adding this to the constrained-jet transpose accounts for every free core coefficient and the global height. Each formula is the ordinary chain rule and transpose of a displayed linear interpolation; consequently the complete point pullback is the exact derivative transpose of the documented finite six-jet model. No physical field or boundary term is omitted.

Executed helper `scripts/resume_20261120/fullclosed_point_cotangent.py` has SHA256 `de5b520b73282f00121c9f50e981097a24f322d82bbe09ef77c58e9981c34726`.
One necessary check of this new complete transpose uses RNG seed2026112002 and complex step1e-30: arbitrary six-jet contraction at the first cell midpoint gives relative difference5.464495846674897e-15, at the last cell midpoint9.946477282023175e-16, and the actual selected principal-curvature derivative3.367548960653923e-15. The principal-curvature six-jet cotangent itself is reused from the independently developed physical QP source, not rederived or replaced here.

A preceding setup attempt indexed a single row of the FFT trig proxy, which supports only its documented operator slices. It exited before any LSMR iteration or nonlinear trial. The fix evaluates the same sin/cos row at the actual angle. The failed setup identity is retained in scratch; this is an interface correction, not a failed numerical direction or a repeated scientific budget.

## Selected compatible tangent slice

The genuine parent is physical QP bundle SHA256 `0c53537771085266634794d82a0f133e2d1f149d1af7e0248e136d9ceee6812d`. On the original stage grid it has SSE371.14518899335843, max Gram .1801261226964055, K7.982277645632981, diameter point lower bound4.082530716916818, and necessary product .9776368103776534.

Retain the complete H2-type DoubleIntegrated coordinates plus1280 physical columns whitened in the same norm. From the physical QP scan take the top16 separated curvature locations and top2 separated radius locations, together with the analytic diameter lower bounds2 and2|H|. Select at most16 product rows with r=.03*D*|kappa|>=.98-.025, ordered by decreasing r. The actual parent supplies six rows. Their coordinate gradients are pulled back through the complete right map T and normalized.

The six-row Gram eigenvalues are approximately -2.68e-15,4.25e-15,1.0663447575841277e-5,1.9604968592293937,1.9999931247536948,2.0394993525694995. Relative cutoff1e-10 retains rank4; a Householder QR reorthogonalizes that row space. Its orthogonality error is1.0103029524088925e-14. Use P=I-Q^T Q with homogeneous restoration z0=0, and solve

||W(R+J T Pz)||^2+mu^2||z||^2.

Only this update lies in the selected current geometric tangent slice. The original nonlinear field, all original free variables and every original Gram row remain; no field mode is permanently frozen. The necessary pointwise nonlinear geometry screen remains the final acceptance criterion.

## Actual256-iteration direction and line search

The complete executed driver is `scripts/resume_20261120/fullclosed_integrated_h2_projected_lm.py`, SHA256 `2a3e29101ad0fbbb1c8be50895a7bf6f4bfa62d8dab532bb22a57e5489764cac`. One BLAS thread, max256 LSMR iterations, mu=.0025, atol=btol=1e-6; the original equal-stage Frobenius objective and exact weighted quarter orbits. The inner solve reaches stop7.

| Trial alpha | Complete SSE | Max relative Gram | K point maximum | Necessary point product | Result |
|---:|---:|---:|---:|---:|---|
| 1 | 179.36742214919116 | .12323092459237595 | 8.637650983034316 | 1.0589709852801035 | rejected by geometry |
| 1/2 | 241.1378176057063 | .15149588667312863 | 8.094320335213641 | .9918591469606762 | rejected by geometry |
| 1/4 | 297.50544441172883 | .1657653454419341 | 7.980230345145044 | .9776324439475 | accepted on original grid |

All three are actual nonlinear residual and full original point-geometry evaluations. The two rejected trials create new curvature maxima in the cap transition at stages1799 and1803, phi=pi/2, rather than the parent's principal active point. They are not accepted or silently discarded. The quarter-step maximum returns to stage1675, s=1.187503891218339, phi=.1349903093339364.

The final diameter point lower bound is4.0835598375188304, H=1.9252174517978016, minimum relative determinant .91743603319995, and minimum relative E .9164567731494168. The normalized objective falls from .00009822397659250043 to .00007873513836269077; linear full-step prediction is .000047069808942622014.

The complete linear step's max nodal delta Y/U/A are .0034893596750356594, .01917393254054916, .16564084559027856; delta H=-.00047908788127353565. These are full-step values; the accepted physical correction is one quarter of them. The projected endpoint residual is5.497667344154036e-18. All six normalized active linear residuals have magnitude at most5.090232926517718e-16; reapplying P changes the solved coordinate vector by5.533408147847118e-14.

LSMR normr=.006911992973120589, normar=.00003411849315733008, normA=40.019308672093665, condA=24.38163480125003, normx=.3360566423149925. Direction and actual line search take97.5501825020001 seconds.

Accepted/final NPZ SHA256: `30e5549c471c0bf7b0d351412003b369801e75a8c900ab65943bba7666eed807`.
Saved direction SHA256: `f4fbfe50fb3c1114245fb1a7f042ea8750b01610fa74c0e880ba0c57a59b1d9f`.
All raw arrays remain outside Git.

## New radial-sampling evidence changes the next parent

While this first direction was completing, the independent same-metric six-Gauss readout found that its parent0c535... has a larger curvature between the old node/midpoint stages and is excluded by the stronger necessary test. The accepted child in this note has not been granted a six-Gauss pass. Its original-grid result is retained exactly as observed, with that finite scope; it is not a reach or continuous curvature claim.

The next complete-space solve therefore switches to all7377 original-plus-Gauss stages, the same scalar-metric carrier, a stage-general three-jet transpose, and a genuinely Gauss-screened parent. It also uses the newly declared positive mixed radial quadrature objective; such weighted objectives must not be subtracted from the old equal-stage SSE as if unchanged. The original and added rows remain explicit, and original-grid raw readouts are retained separately.

No sampled target, closed isometry, continuous metric, reach, held/E3, all-t family, or fixed-g refinement completion is claimed.
