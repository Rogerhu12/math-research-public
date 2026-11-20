# All-mode polar targets and a banded physical correction

Date: 2026-11-20 UTC. Status: proved algebraic identities for the stated finite model; implemented and numerically exercised. This is a solver construction, not an existence, reach, or amplitude certificate. See the separate six-step result note.

## 1. The exact weighted local problem

At a native stage and angle let $V=F_s$, $d=F_\phi$, $a>0$ be the original fixed scalar and $\rho>0$ the fixed material density during this subproblem. For an orthonormal two-frame $Q=[q_1,q_2]$, consider
$$
\mathcal E(Q)=|V-q_1|^2+|d/a-\rho q_2|^2,\qquad Q^\top Q=I_2.
$$
Expansion gives
$$
\mathcal E(Q)=|V|^2+|d/a|^2+1+\rho^2
 -2\operatorname{tr}\!\left(Q^\top[V,\rho d/a]\right).
$$
The quadratic target term is constant because each column of $Q$ has unit norm. Therefore this particular weighted problem reduces exactly to an ordinary thin polar decomposition of
$$
T=[V,\rho d/a].
$$
This does not assert that a general anisotropically weighted matrix approximation reduces to polar decomposition.

For completeness, let $T=U\Sigma W^\top$ be a thin SVD. Extend the columns of $U$ to an orthogonal basis. Each diagonal entry of $U^\top QW$ is at most one, so
$$
\operatorname{tr}(Q^\top T)\le \sigma_1+\sigma_2,
$$
with equality for $Q=UW^\top$. This proves the minimization assertion, including rank-deficient $T$. The minimizing two-frame need not be unique in the rank-deficient case. The implementation uses thin SVD and never inverts a singular Gram matrix.

The physical derivative targets are
$$
V^*=q_1,\qquad d^*=a\rho q_2.
$$
They obey $|V^*|^2=1$, $V^*\cdot d^*=0$, and $|d^*|^2=a^2\rho^2$ pointwise. These derivative targets need not be integrable. The subsequent global step addresses integrability in the original field space.

## 2. Fixed core, every other original jet free

Write the original field as
$$
F=q+\chi(s)\big((R+S-s)e_r(\Theta(\phi))+H e_z\big).
$$
Fix all current core support coefficients for this local/global solve. Hence $\rho$, $\Theta$, and the horizontal lift remain unchanged. Allow every original interior residual three-jet, every allowed horizontal core acceleration, and $H$ to vary:
$$
\delta F_s=\operatorname{synth}(\delta U)+\chi'(s)\delta H e_z,\qquad
\delta F_\phi=\operatorname{angular}(\delta Y).
$$
Core position and velocity remain fixed, the vertical core acceleration remains zero, and every terminal residual three-jet remains zero. For $M=160,J=923$ this leaves $1,332,088$ local coordinates: all $1,332,245$ original coordinates except the $157$ currently frozen free core support coefficients.

Let $b_V=V^*-V$ and $b_d=d^*-d$. The data part of the global quadratic step is
$$
E_{\rm data}(\delta)=\sum_{\ell,k}m_k
 \left(|\delta F_s-b_V|^2+a_\ell^{-2}|\delta F_\phi-b_d|^2\right).
$$
The stage index is exactly the original node/midpoint list. Full-circle angles and the exact quarter-orbit weights $m_k$ are equivalent. The quarter weights are $2$ at the two endpoints and $4$ elsewhere. No original angular mode or residual row is removed.

## 3. An exact underintegration kernel of the original sampled Gram

This observation concerns the original finite node/midpoint operator itself.

Restrict a correction to the angularly constant vertical channel. Its free coordinates are the $3(J-2)$ interior $(Y,U,A)$ values and $\delta H$, so the space has dimension $3J-5$. Its angular derivative vanishes identically. At the two radial endpoints its meridional derivative correction is already zero because the endpoint residual velocities and $\chi'$ are zero there.

The only remaining conditions for this correction to leave every sampled first derivative unchanged are the $J-2$ interior-node and $J-1$ midpoint scalar equations
$$
\delta q_Z'(s_\ell)+\chi'(s_\ell)\delta H=0.
$$
There are $2J-3$ such equations. Rank-nullity therefore gives a kernel of dimension at least
$$
(3J-5)-(2J-3)=J-2.
$$
For $J=923$, this is at least $921$ dimensions. Fixing $H$ still leaves at least $J-3$ dimensions.

Every vector in this kernel leaves $F_s$ and $F_\phi$ at every original stage and angle unchanged. Consequently it leaves the complete original sampled Gram residual **exactly unchanged for every real multiple of the vector**, not merely to first order. It can nevertheless change the field and its derivatives between stages.

This proves a sampling deficiency; it is not an obstruction to a genuine closed surface. It explains why decreasing the original sampled objective alone cannot certify continuous metric or curvature. A finite stage list with five distinct derivative samples in each polynomial piece, split at the $\chi$ breakpoint, detects an angularly constant vertical derivative polynomial of degree at most four. A future actual operator must also use the unchanged scalar oracle at its added stages.

## 4. Positive continuous regularization without dropping jets

To select a global correction, the implemented quadratic problem adds
$$
E_{\rm reg}(\delta)=\eta\sum_i h_i^{-1}
 \int_{s_i}^{s_{i+1}}\int_{\rm angles}
 |\delta F_s|^2\,d\mu_{\rm discrete}(\phi)\,ds,\qquad \eta>0.
$$
The default is $\eta=10^{-6}$. This regularizer is applied to the **increment**, not added to the reported nonlinear Gram objective.

Its quadratic form is strictly positive on every nonzero allowed correction with frozen core. Indeed, zero integral forces $\delta F_s=0$ everywhere by continuity. Thus $\delta F(s,\phi)$ is independent of $s$. The fixed core gives $\delta F(0,\phi)=0$, hence $\delta F=0$ everywhere. At the terminal circle this forces $\delta H=0$, and then the residual polynomial and all its jets vanish.

The integral is computed separately on each side of $S-\text{width}$. On each piece, $\delta q'$ and $\chi'\delta H$ have degree at most four. Their products have degree at most eight; five-point Gauss--Legendre quadrature integrates them exactly in exact arithmetic. Binary64 evaluations are numerical, not interval enclosures.

This first-derivative regularizer removes the sampled kernel from the quadratic solve. It does not bound second derivatives or reach. A large coordinate norm is not itself a curvature measurement; the actual candidate must be read geometrically. A second-derivative regularizer can be added as a distinct, recorded algorithmic version if needed.

## 5. Exact angular separation

For $\nu=2m>0$, a rotating-frame horizontal channel has coefficients $R(s)\cos(\nu\phi)$ and $T(s)\sin(\nu\phi)$. Its angular derivative is
$$
\big(-(\nu R+T)\sin(\nu\phi),\ (R+\nu T)\cos(\nu\phi)\big).
$$
The full angular sum is
$$
\frac N2\big((\nu R+T)^2+(R+\nu T)^2\big).
$$
Set $q_+=(R+T)/\sqrt2$ and $q_-=(R-T)/\sqrt2$. The angular quadratic terms become
$$
\frac N2\left((\nu+1)^2q_+^2+(\nu-1)^2q_-^2\right).
$$
The velocity term becomes $\frac N2((q_+')^2+(q_-')^2)$. A vertical nonconstant cosine channel has angular eigenvalue $\nu^2$. The constant rotating radial channel has eigenvalue $1$, while the constant vertical channel has eigenvalue $0$.

The angular norms are $N$ for the two constant channels and $N/2$ for all nonconstant channels. The RHS uses the original batched trigonometric adjoints with orbit weights, then divides by exactly these norms. The target may contain frequencies beyond $M$; its orthogonal projection is the exact RHS for minimizing the stated quadratic over the full original $M$-mode field space.

## 6. Banded radial matrices and the single height border

Each stage value and derivative uses six adjacent endpoint coordinates, in the order
$$
(Y_i,U_i,A_i,Y_{i+1},U_{i+1},A_{i+1}).
$$
Therefore every radial normal matrix has lower bandwidth five. For angular eigenvalue $\lambda$, its scalar quadratic matrix is
$$
K_\lambda=K_U+\lambda K_Y+\eta K_{\rm cont},
$$
where $K_U$ contains the original sampled velocity squares, $K_Y$ contains sampled position squares weighted by $a_\ell^{-2}$, and $K_{\rm cont}$ contains the cell integrals of squared velocity.

Horizontal free indices start with the core acceleration and continue through every interior jet. Vertical free indices start with the first interior position. All terminal jets are excluded because their correction is constrained to zero. This is exact elimination of the original affine boundary conditions.

The horizontal eigenvalues are the odd squares from $1$ to $(2M+1)^2$, requiring $M+1$ distinct radial factors. Vertical eigenvalues are the even squares from $0$ to $(2M)^2$, requiring another $M+1$ factors. Thus $M=160$ uses $322$ small banded factors.

Only the constant vertical channel couples to $H$. Its normalized matrix is
$$
\begin{pmatrix}K_0&k\\k^\top&h\end{pmatrix}.
$$
The entries include both the sampled $\chi'$ terms and their continuous regularization terms. Set $u=K_0^{-1}k$ and $\sigma=h-k^\top u>0$. The solution for RHS $(b,c)$ is
$$
\delta H=\frac{c-k^\top K_0^{-1}b}{\sigma},\qquad
\delta q=K_0^{-1}b-u\,\delta H.
$$
No independent height-only spike is imposed; the entire vertical mean field adjusts jointly with the cap height.

## 7. Full-space right factor and its transpose

Each radial factor is equilibrated as $K=D L L^\top D$, with $L$ lower triangular. The right map is $B=D^{-1}L^{-\top}$ and its transpose is $B^\top=L^{-1}D^{-1}$, so $BB^\top=K^{-1}$.

For the bordered vertical mean block, before its common $N^{-1/2}$ angular normalization, the right map is
$$
(z_q,z_H)\longmapsto
\left(Bz_q-u\,z_H/\sqrt{\sigma},\ z_H/\sqrt{\sigma}\right).
$$
Its exact transpose sends
$$
(v_q,v_H)\longmapsto
\left(B^\top v_q,\ (v_H-u^\top v_q)/\sqrt{\sigma}\right).
$$
The $R/T$ changes of basis are orthogonal. All nonconstant factors include the normalization $(N/2)^{-1/2}$, and both constant factors include $N^{-1/2}$.

The public methods `right_factor` and `right_factor_transpose` act on the original complete packed vector. They apply a positive explicit scalar to the free core-support block, and the radial factors to every remaining coordinate. Thus a complete Gram solver using these maps still retains **all** original free variables. The factor is the inverse square root of the stated fixed-core energy block, not of the nonlinear Gram Hessian including varying-core couplings.

## 8. Acceptance, fallback, and future stage interface

A polar/global candidate is accepted only if the actual original Gram SSE decreases and the actual sampled metric determinant remains positive. The acceptance objective remains
$$
\sum_{\ell,k}m_k(r_{ss}^2+2r_{s\phi}^2+r_{\phi\phi}^2).
$$
The nonlinear trial uses the original analytic lift, every original angular mode, and every original stage.

If every polar trial fails, the implementation forms the original weighted Gram gradient, freezes only its core-support block, solves against the same positive energy, and computes a linearized least-squares step length using the original $Jv$. It then applies the same true nonlinear line search. This fallback is an original-objective descent direction in exact arithmetic whenever the projected gradient is nonzero. It has not been needed in the first six-step run.

`FrozenCoreEnergy(..., observations=...)` accepts supplied $(\text{cell},u,a,\text{weight})$ observations. This supports building the same banded energy with future additional radial stages without modifying the field space. The current CLI deliberately uses only the current original operator. Adding actual nonlinear Gram rows requires a matching field evaluator and values from the unchanged scalar oracle; no surrogate scalar values are silently inserted.

## Implementation and API references

- `scripts/resume_20261120_polar_banded.py`: complete solver and reusable factor.
- `scripts/resume_20261120_check_polar_banded.py`: one small independent physical-energy and transpose check.
- Original dense operator SHA256: `e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d`.
- Batched/quarter operator SHA256: `02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a`.

SciPy's documented lower-band layout is used for `cholesky_banded` and its solution routines: [SciPy cholesky_banded documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky_banded.html), [SciPy solve_banded documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_banded.html), accessed 2026-11-20. The mathematical identities above are derived here and do not rely on an external rigidity or existence theorem.
