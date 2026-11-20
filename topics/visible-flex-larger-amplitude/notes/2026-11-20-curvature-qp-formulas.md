# Principal-curvature derivatives and a physical coarse QP

Date: 2026-11-20 UTC. Status: proved pointwise differential identities and finite convex-QP identities; numerical implementation and first six-step application are reported separately. Every geometric screen below is a sampled necessary condition, not a reach certificate.

## Pointwise derivative

Fix a parameter point of a regular $C^2$ surface. In any orthonormal ambient frame, write
$$
V=F_s,\quad d=F_\phi,\quad
c=V\times d,\quad A=|c|,\quad n=c/A.
$$
The first and second fundamental matrices are
$$
I=\begin{pmatrix}V\cdot V&V\cdot d\\V\cdot d&d\cdot d\end{pmatrix},
\qquad
II=\begin{pmatrix}n\cdot F_{ss}&n\cdot F_{s\phi}\\
n\cdot F_{s\phi}&n\cdot F_{\phi\phi}\end{pmatrix}.
$$
Let $\kappa$ be a simple generalized eigenvalue, with $IIv=\kappa Iv$ and $v^\top Iv=1$. Set
$$
t=v_1V+v_2d,\qquad
w=v_1^2F_{ss}+2v_1v_2F_{s\phi}+v_2^2F_{\phi\phi}.
$$
Then $|t|=1$ and $n\cdot w=\kappa$. Differentiating the generalized eigenvalue equation, the terms containing $\delta v$ cancel, giving
$$
\delta\kappa=v^\top(\delta II-\kappa\delta I)v.
$$
Moreover
$$
\delta n=\frac{I_3-nn^\top}{A}
  (\delta V\times d+V\times\delta d).
$$
With
$$
a=\frac{w-\kappa n}{A},
$$
the scalar triple-product identities yield
$$
\boxed{\;
\delta\kappa
=n\cdot\delta w+
(d\times a-2\kappa v_1t)\cdot\delta V+
(a\times V-2\kappa v_2t)\cdot\delta d.
\;}
$$
Thus the cotangents of $(F,F_s,F_\phi,F_{ss},F_{s\phi},F_{\phi\phi})$ are respectively
$$
0,\quad d\times a-2\kappa v_1t,\quad a\times V-2\kappa v_2t,\quad
v_1^2n,\quad 2v_1v_2n,\quad v_2^2n.
$$
This includes both the moving normal and the changing first fundamental form. Omitting either would produce an incorrect curvature derivative.

At a repeated principal eigenvalue there is generally no unique scalar branch derivative. The implementation uses generalized orthonormal eigenvectors to obtain selected linear constraints and still checks the actual two principal curvatures in every nonlinear trial. It does not claim a differentiable maximum-curvature theorem at an umbilic.

## Physical coarse columns

Use the already defined complete coarse three-jet correction space. For one radial/angular pair $(b,c)$, the actual physical variations are
$$
\delta F=Y_bh_c,\quad \delta V=U_bh_c,\quad
\delta d=Y_bh'_c,\quad
\delta F_{ss}=A_bh_c,\quad
\delta F_{s\phi}=U_bh'_c,\quad
\delta F_{\phi\phi}=Y_bh''_c.
$$
$Y_b,U_b,A_b$ are the literal original shared-quintic stage values. For the height direction, they include the actual $\chi,\chi',\chi''$ lift contributions. No ideal smooth surrogate replaces the stored nodal field.

For frequency $\nu=2m$, the angular second derivatives in the rotating orthonormal frame are
$$
h''_R=(-(1+\nu^2)\cos\nu\phi,-2\nu\sin\nu\phi,0),
$$
$$
h''_T=(-2\nu\cos\nu\phi,-(1+\nu^2)\sin\nu\phi,0),
\qquad h''_Z=(0,0,-\nu^2\cos\nu\phi).
$$
The rotation of the frame is included. Contracting these six variations with the cotangent above gives one exact row in the physical coarse coordinates.

The complete Gram equations still contain every original $M=160$ mode and every original angular/stage row. The 1,280-coordinate correction space in the first run uses 11 coarse nodes, all three jets, modes $0$ through $12$ in the documented parity channels, the free horizontal core acceleration directions, and one joint height direction. Core support coefficients remain fixed during these coarse steps.

## Diameter lower bounds and necessary constraints

For the declared doubled body, the angular $\pi$ symmetry combined with reflection across $z=0$ supplies the antipodal point $-F$ for every body point $F$. Thus each sampled point gives
$$
D\ge D_j=2|F_j|.
$$
Its differential is
$$
\delta D_j=2\frac{F_j}{|F_j|}\cdot\delta F_j.
$$
The fixed core and two caps also give the lower bounds $2$ and $2|H|$, included explicitly by the implementation.

For a true $C^2$ surface, the reach cannot exceed a local principal-curvature radius. Consequently reach $\ge0.03D$ requires $0.03D_j|\kappa_i|\le1$ for every point pair. The computation uses $0.98$ as an interior numerical screening threshold. Its sampled values are not interval enclosures, and passing this necessary test proves neither reach nor embedding.

For selected curvature point $i$ and radius point $j$, at a nonzero simple principal branch, the linearized inequality is
$$
0.03\left(D_j\,\operatorname{sign}(\kappa_i)\,\delta\kappa_i+
|\kappa_i|\,\delta D_j\right)
\le 0.98-0.03D_j|\kappa_i|.
$$
The same formula applies to the constant core bound, whose derivative is zero, and to the cap-height bound with derivative $2\operatorname{sign}(H)\delta H$.

Both principal curvatures are actually read at every sampled point. The initial implementation selects 32 spatially separated large absolute principal-curvature branches and four large-radius points, plus the two explicit diameter bounds. This gives 192 selected inequalities. Selection is an optimization device, not a replacement for the complete trial screen.

## Finite quadratic problem and its dual

Let $r$ be the complete original Gram residual with the exact quarter multiplicities and Frobenius factors. Let $A$ be the physical coarse Gauss--Newton normal matrix plus the declared positive scaled damping, and let $g=J^\top r$. The step problem is
$$
\min_p\ \tfrac12p^\top Ap+g^\top p
\quad\text{subject to}\quad Qp\le b.
$$
All original Gram rows enter $A$ and $g$, through the previously established separated angular kernels. The curvature rows only constrain the step; they do not replace any metric equation.

Since $A$ is positive definite, write $p_0=-A^{-1}g$. Minimizing the Lagrangian in $p$ gives
$$
p=p_0-A^{-1}Q^\top\lambda,\qquad \lambda\ge0.
$$
The dual minimization is
$$
\min_{\lambda\ge0}\ 
\tfrac12\lambda^\top QA^{-1}Q^\top\lambda+
(b-Qp_0)^\top\lambda.
$$
This is the stated convex quadratic dual. The implementation scales coordinates and constraint rows, factors $A$, and uses L-BFGS-B on the small dual.

A numerical optimizer's termination flag is not treated as exact feasibility. Any positive linear row violation is reported and repaired by an explicit contraction toward the feasible zero direction. Because the current point passes the necessary screen, all current bounds are nonnegative. For $Q_ip>b_i\ge0$, imposing $\gamma\le b_i/(Q_ip)$ makes $Q_i(\gamma p)\le b_i$; nonviolating rows remain feasible for $0\le\gamma\le1$. The implementation records the contraction and the final maximum primal violation. It does not claim that the contracted direction remains the exact QP minimizer.

## Actual nonlinear acceptance

Every trial is read using the original complete operator. It must satisfy all of the following:

- The original full Gram SSE decreases strictly.
- The sampled metric determinant is positive.
- The actual maximum absolute principal curvature over every original node/midpoint and quarter angle, combined with the actual complete-body sampled diameter lower bound, satisfies $0.03D_{\rm lb}K_{\rm max}\le0.98$.

No statement about unsampled radial points, unsampled angles, all phases, embedding, or reach is inferred. In particular, the original node/midpoint metric operator has the already identified underintegration issue; adding more actual radial rows remains necessary.

The first run shows that new curvature peaks can appear away from the selected current points. Their detection by the complete trial screen is essential. The next version retains locations of rejected-trial peaks in a bounded active memory and differentiates them again at the next actual parent; stale curvature values or derivatives are never reused.

## Source interface

`scripts/resume_20261120_curvature_qp.py` exposes:

- `curvature_cotangent(z, branch)` for the six-jet cotangent, with principal branches ordered by the generalized symmetric eigensolver.
- `analytic_kappa(z, branch)` for a bilinear analytic branch, used in the actual complex-step probe.
- `CoarseGeometry.row(stage, angle, cotangent)` for the exact coarse transpose.
- `scan_geometry` for the complete current native-stage point screen.

The first source version's actual SHA256 is `a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854`. The original and coarse dependency hashes, the actual invocation, the derivative check, and all accepted numerical results are recorded in the companion result note.
