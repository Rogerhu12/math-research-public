# R106 supplement: integrated parameter refinement and a boundary root bidisk

This note has two different execution statuses. Section 1 is an actually executed
exact-rational finite certificate using completed continuous reports. Sections
2–4 prove the interface implemented by the new native boundary program; that
program has not yet run. In particular, the requested physical angle width
$1/64$ is a proposed input, not a proved geometry domain.

## 1. Actual improvement of the whole-time ray tube

The immutable integrated-source report is
[step5-integrated-parameter-source-budget](../notes/2026-11-12-step5-integrated-parameter-source-budget.json),
SHA256
1157bc1b8ad6f70b9fbd65aeaee6152da842e066d22b216cd2ca87620e5f5a41.
Its complete 169 ordinary radial cells and the root interval bound the whole
forward physical time interval $[-\pi/2,\pi/2]$. The finite reference is the same
descriptor 097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052.
Its exact real parameter interval is $p_5\pm1/2000000$, so it contains the
requested $p_5\pm10^{-9}$.

After adding the printed ball radii outward, the two integrated bounds obey
$B_1<1077.689852253$ and $B_2<9646.363329155$. They are moduli of
$g_p=f_p(Y)/Y_x$ and $g_{pp}=f_{pp}(Y)/Y_x$ integrated in physical time.
Here $f$ is the physical angle velocity at fixed $\tau$,
$r=t(p)\sin\tau$, while $x$ is the normalized $2\pi$-periodic label.
There is no extra factor four. In the local normalized time of a reference
segment, the same integral is expressed with $h f_p/Y_x$.

Keep the same fixed reference $Y$ and let $X_p$ be its actual defect flow.
The earlier complete center report supplies
$A_0<4.092563989255516\,10^{-8}$ on label width $1/256$.
The integrated parameter source is paid on width $1/512$, with
$\operatorname{Re}Y_x>3/100$ and $|Y_x|<21/20$.
The fundamental theorem of calculus on the real parameter line gives

$$
 \int\|g^{\rm defect}(\,\cdot\,,p)\|_{1/512}
 \le A_0+10^{-9}B_1
 <1.118615492146\,10^{-6}<A_*:=7/6250000.
$$

Use the outer flow label strip $S_X=15/8192$ and the final strip $s=1/1024$.
Exactly the continuation and Cauchy argument of the original R106 all-time
tube applies: $2A_*<1/512-S_X$, and

$$
 |X_p-x|\le A_*,\qquad
 |X_{p,x}-1|\le {A_*\over S_X-s},\qquad
 |X_{p,xx}|\le {2A_*\over(S_X-s)^2}.
$$

For $\Theta_p=Y\circ X_p$, all times, and every real $p$ in the stated box, the
new actual finite certificate gives

$$
\begin{aligned}
 \operatorname{Re}\Theta_{p,x}&>0.028623744,\\
 |\Theta_{p,x}|&<1.051376256,\\
 |\Theta_p-Y|&<1.176\,10^{-6},\\
 |\Theta_{p,x}-Y_x|&<0.002581862687,\\
 |\operatorname{Im}\Theta_p|&<0.001026566625<1/900,\\
 |\Theta_{p,xx}|&<1082.479424583.
\end{aligned}
$$

These inequalities use the complete real-time reference, including all base and
$Q$ seams. They are not inferred from the endpoint conjugacy derivative.
The executable is
[fourfold_integrated_true_ray_budget_exact.mjs](../scripts/fourfold_integrated_true_ray_budget_exact.mjs).
The saved
[18-gate report](../notes/2026-11-13-R106-integrated-source-ray-refinement.json)
was computed with the identical BigInt implementation. It checks both original
input hashes, exact box containment, normalization, reference identity, and all
the displayed inequalities. This change does not produce signed parameter
forcing or a nonmean subprincipal phase.

## 2. Exact finite primitive on complex angular boundaries

Fix real $p$ in the actual affine box. Its root $t(p)$ is real and radial.
Thus $\rho=t(p)-r$ is independent of $\theta$; no nonradial complex root graph is
introduced. Let the actual root primitive and its finite approximation be
holomorphic on the previously paid input bidisk.

The new program
[fourfold_subprincipal_root_bidisk_boundary.py](../scripts/fourfold_subprincipal_root_bidisk_boundary.py)
evaluates the entire finite primitive on
$\theta_j+iS$, $\theta_j=\pi j/(2N)$.
In the rotating cylindrical frame, its coefficient indexed by $k$ is multiplied
by $\exp(-4kS)$ before an inverse DFT. All complex coefficients are retained.
Calling the old real-angle evaluator would discard the imaginary part and is
therefore deliberately avoided.

For a finite radial coefficient polynomial $c_k(\rho)$ and a real angular cell
$|\theta-\theta_j|\le\pi/(4N)$, the exact inequality

$$
 \left|e^{i4k(\theta-\theta_j)}-1\right|
 \le |k|\pi/N
$$

implies the complete finite-cell fee

$$
 \sum_k
 \sup_{|\rho|\le R}|c_k(\rho)|
 e^{4|k|S}|k|\pi/N.
$$

The finite primitive's physical angular derivatives include the rotating-frame
connection, exactly as in the frozen geometry producer. Its radial derivatives
are obtained by differentiating the normalized polynomial with physical scale
$-\mathrm{scale}$.

The true infinite angular correction is evaluated on normalized width $4S$,
not on $4S+\pi/N$: changing the real part inside a cell does not enlarge the
imaginary strip. The complete radial Taylor tail and the radial derivatives of
the infinite correction are paid independently by the frozen Cauchy formulas.
The resulting six fields are true enclosures on the entire complex $\rho$ disk
and every closed real-angle cell of the upper boundary.

## 3. Interior denominators and the seven fields

All scalar input functions are real analytic on the actual root germ, uniformly
for the real parameter box. Schwarz conjugation sends the upper angular boundary
and the entire complex radial disk to the lower boundary and the same disk.
Consequently the upper-boundary certificate also supplies the lower one.

Write $C=F_\theta\times F_r$, $G_{\rm area}=C\cdot C$,
$R_F=F\cdot F$, and $H=C\cdot F$.
The boundary code first requires positive real part of
$G_{\rm area},R_F,H,F_z$ on all cells and all $|\rho|\le R$.
These are entire periodic angular functions. For each fixed complex $\rho$,
the harmonic minimum principle on the periodic strip proves the same positive
lower bounds inside. Their reciprocals are therefore analytic there.

Next $a_0=-n/G_{\rm area}$ is analytic, and its positive real boundary value
gives the same interior gate by the same argument. The true target factor
$Q=-K_0(t-\rho)/\rho$ is independent of $\theta$. Its entire radial-disk gate is
proved separately using

$$
 Q(\rho)=\int_0^1 K_{0,r}(t-z\rho)\,dz,\qquad
 Q_\rho(\rho)=-\int_0^1 zK_{0,rr}(t-z\rho)\,dz.
$$

The positive-real branch $\kappa=\sqrt Q$ is now fixed on the whole domain.
Thus all seven original-height fields
$G,q,k_*,S_{\rm reg},L_\theta,U_0,U_1$ from the preceding R106 supplement
are analytic throughout the common bidisk. The program computes their actual
boundary moduli before any angular mean, using the same complete six-jet
geometry. Applying the maximum modulus principle in the periodic angular strip
extends these moduli to every interior angle. No unproved wider true-field
domain is substituted.

The actual regularized density is bounded as
$|G|\le |A|+R|B|+R^2|C_2|$ from its exact expression
$G=A+\rho B+\rho^2C_2$.
This preserves the dominant constant and does not use a numerically inferred
identity to replace any coefficient. The identity $k_*(0)G(0)=-1/16$ remains
a consequence of the actual formulas.

## 4. Output identity and limits

The new report preserves the same domain schema, adds its explicit source file,
and binds the actual object, root certificate, common scalar germs, parameter
box and every producer dependency. Every closed angular cell is recorded.
A complete report is written only after all cells, true infinite tails and
denominator gates pass.

The unexecuted Fourier producer has been extended to admit either the original
whole-cell domain source or this complex-boundary source, and it checks the
actual chosen source hash. Historical reports are not rebound to new source
bytes. Finite Fourier node errors, aliases, omitted angular modes and omitted
radial modes remain separately charged. No phase integral, useful R104 cutoff,
or full PDE inverse follows from storing these programs. The next required
native result is the actual common bidisk and the complete seven signed-field
coefficient report.
