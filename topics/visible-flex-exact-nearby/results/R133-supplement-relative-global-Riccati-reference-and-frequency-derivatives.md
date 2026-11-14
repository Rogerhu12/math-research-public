# R133 supplement: relative global Riccati reference and frequency derivatives

2026-11-14, root. **Proved.** This supplies the reference-comparison
step needed to transfer the actual positive-body certificate from its
repaired M32 centre to the explicit M96 family. The statement is an
analytic comparison theorem. It does not assert that the actual
whole-body coefficient hypotheses below have already been certified.

The reference is exactly the one in
[the full positive reference](R133-supplement-global-positive-reference-and-current-collar.md):
its left value is $g_M(r_*)=M^{-1/3}$, its right value is the
frequency-independent scalar $p_*>0$, and its speed is the actual
radial optical speed when that speed has been certified. No actual
regular boundary line is substituted for this scalar datum.

## 1. A common physical interval and a relative form hypothesis

Let $K\ge0$ be the same bounded function on $[r_*,R]$.
For $\alpha=0,1$, let $a_\alpha$ be positive, bounded and
bounded away from zero on that interval. Piecewise measurable
coefficients and the original finite radial seams are allowed.
Let $p_{*,\alpha}>0$ be independent of $M>0$.
Assume, almost everywhere,
$
 \left|{a_1\over a_0}-1\right|\le\tau,\qquad
 \left|{a_1^{-1}\over a_0^{-1}}-1\right|\le\tau,\qquad
 \left|{p_{*,1}\over p_{*,0}}-1\right|\le\tau,\qquad
                         0\le\tau\le1/16.              \tag{R.1}
$
For example, a speed-relative error $\epsilon<1$ and terminal
relative error $\epsilon_*$ give (R.1) with
$\tau=\max\{\epsilon/(1-\epsilon),\epsilon_*\}$.
The inverse-speed term is essential.

In the physical coordinate the references solve
$
 g_{\alpha,r}=Ma_\alpha(K-g_\alpha^2),\quad
          g_\alpha(r_*)=M^{-1/3},
\qquad
 p_{\alpha,r}=Ma_\alpha(p_\alpha^2-K),\quad
          p_\alpha(R)=p_{*,\alpha}.                    \tag{R.2}
$
They are positive. All comparisons below hold at every physical
$r$, including either side of a coefficient seam by continuity.

## 2. Real variational comparison, with its actual minimizers

For the right reference, $E_\alpha=Mp_\alpha(r)$ is the minimum,
over $u(r)=1$, of
$
 B_\alpha(u,u)=
 \int_r^R\{a_\alpha^{-1}|u'|^2+
                  a_\alpha M^2K|u|^2\}\,dt
            +Mp_{*,\alpha}|u(R)|^2.                  \tag{R.3}
$
For the left reference, $E_\alpha=Mg_\alpha(r)$, use $[r_*,r]$,
$u(r)=1$, and the common initial term
$M^{2/3}|u(r_*)|^2$.
These forms are coercive on the appropriate zero-trace variation
space. Their unique minimizers give (R.2) through the
Euler equation and its Robin condition.

Writing $\|u\|_0=B_0(u,u)^{1/2}$, (R.1) gives the full bilinear
form estimate
$
 |(B_1-B_0)(u,v)|\le\tau\|u\|_0\|v\|_0,\qquad
             (1-\tau)B_0\le B_1\le(1+\tau)B_0.        \tag{R.4}
$
Comparison of the minima therefore proves
$
 1-\tau\le{p_1\over p_0},{g_1\over g_0}\le1+\tau.      \tag{R.5}
$
This is uniform in interval length and frequency; no large
radial exponential has been introduced.

Let $u_\alpha$ be the two minimizers and $w=u_1-u_0$.
Then $w$ has zero prescribed trace, and stationarity gives
$
 B_1(w,v)=-(B_1-B_0)(u_0,v)
$
for every such variation $v$. Taking $v=w$ yields
$
 \|w\|_0\le{\tau\over1-\tau}\sqrt{E_0},\qquad
 \|u_1\|_0\le{1\over1-\tau}\sqrt{E_0}.                 \tag{R.6}
$
Thus the minimizer changes by order $\tau$, rather than merely
order $\sqrt{\tau}$. The latter weaker estimate would lose
unnecessary precision in the frequency comparison.

## 3. The relative frequency derivative is also small

A dot denotes $M\partial_M$ at fixed physical $r$.
Put $D_\alpha=\dot B_\alpha$, differentiating its coefficients
while holding the arguments fixed. The three positive terms
in (R.3) have powers $0,2,1$ of $M$; in the left form they
have powers $0,2,2/3$. Consequently
$
 0\le D_\alpha\le2B_\alpha,\qquad
 |(D_1-D_0)(u,v)|\le2\tau\|u\|_0\|v\|_0.             \tag{R.7}
$
The differentiability of the minimizer follows from the coercive
linear variational equation. Equivalently its difference quotients
solve that same equation with differentiable coefficients.
Stationarity then gives the envelope identity
$
                    \dot E_\alpha=D_\alpha(u_\alpha,u_\alpha).
                                                               \tag{R.8}
$
In particular $|\dot{\log p_\alpha}|,|\dot{\log g_\alpha}|\le1$,
as in the original reference proof.

Let $q=\tau/(1-\tau)$. Equations (R.6)--(R.8) give
$
 {|\dot E_1-\dot E_0|\over E_0}
 \le {2\tau\over(1-\tau)^2}+2q(2+q)
       ={\tau(6-2\tau)\over(1-\tau)^2}.                \tag{R.9}
$
Indeed split the difference into
$(D_1-D_0)(u_1,u_1)$ and
$D_0(w,u_1)+D_0(u_0,w)$; use (R.7) for each term.
Differentiating the quotient and using
$|E_1/E_0-1|\le\tau$, $\dot E_0/E_0\le2$, proves
$
 \left|\dot{\left({p_1\over p_0}\right)}\right|,
 \left|\dot{\left({g_1\over g_0}\right)}\right|
 \le\tau\left({6-2\tau\over(1-\tau)^2}+2\right)
                         <10\tau.                   \tag{R.10}
$
At $\tau=0$ these derivatives are exactly zero. The displayed
strict inequality is understood for $\tau>0$.
This real-form proof also covers the noninteger left Robin power
$M^{2/3}$; no unproved complex-frequency continuation is used.

## 4. Complete two-row frames and their relative derivatives

Use the actual determinant-one matrices
$
 W_\alpha=p_\alpha+g_\alpha,\quad
 T_\alpha=W_\alpha^{-1/2}
          \begin{pmatrix}p_\alpha&-g_\alpha\\1&1\end{pmatrix},
 \qquad F_\alpha=M^{-1/6}T_\alpha,\qquad
 C_M=F_0^{-1}F_1=T_0^{-1}T_1.                         \tag{R.11}
$
Both rows are retained. Define
$
 x=p_1/p_0-1,\quad y=g_1/g_0-1,\quad
 \theta=p_0/W_0,\quad z=\theta x+(1-\theta)y.
$
Then the exact relative matrix is
$
 C_M=(1+z)^{-1/2}(I+D),\quad
 D=\begin{pmatrix}\theta x&-(1-\theta)y\\
                   -\theta x&(1-\theta)y\end{pmatrix}.          \tag{R.12}
$
Here $|x|,|y|,|z|\le\tau$ and
$\|D\|\le\sqrt2\,\tau<3\tau/2$.
Using the derivative bounds for each original reference,
$
 |\dot\theta|\le2\theta(1-\theta)\le1/2,\quad
 |\dot z|\le11\tau,\quad \|\dot D\|<16\tau.             \tag{R.13}
$
For the last inequality, the two quotient derivatives cost
$10\sqrt2\,\tau$, and the derivative of $\theta$ costs
at most $\tau$.

The mean-value theorem applied to $(1+z)^{-1/2}$, with
$1+z\ge15/16$, now gives the explicit uniform bounds
$
 \|C_M-I\|\le3\tau,\quad \|C_M^{-1}-I\|\le4\tau,\quad
 \|C_M^{-1}\|\le5/4,                                  \tag{R.14}
$
$
             \|\dot C_M\|\le32\tau,\qquad
             \|\dot C_M^{-1}\|\le64\tau.               \tag{R.15}
$
For clarity,
$
 |((1+z)^{-1/2})^\cdot|<7\tau,\qquad
 (1+z)^{-1/2}<16/15
$
when $\tau>0$; together with (R.13) these bound
$\dot C_M$ by
$[7(1+3/32)+256/15]\tau<32\tau$.
The inverse bounds follow from
$3\tau\le3/16$ and
$\dot C^{-1}=-C^{-1}\dot C C^{-1}$.
All estimates extend with equality at $\tau=0$.

Let $\mathcal A_\alpha=F_\alpha^{-1}\dot F_\alpha$.
The original variational argument gives
$\|\mathcal A_\alpha\|<5/3$.
The exact identity
$
 \mathcal A_1=C^{-1}\mathcal A_0C+C^{-1}\dot C
$
and (R.14)--(R.15) imply
$
               \|\mathcal A_1-\mathcal A_0\|<64\tau
                                                       \tag{R.16}
$
for positive $\tau$, and equality zero when $\tau=0$.

## 5. Neighbouring frequencies: the drift cancellation is retained

For fixed $r$, set
$
 R_\alpha(M,N)=F_\alpha(M)^{-1}F_\alpha(N),\qquad
 b=\max(M,N)/\min(M,N).
$
The logarithmic-frequency differential equation gives
$\|R_\alpha(M,N)\|\le b^{5/3}$.
Its exact variation formula and (R.16) give
$
 \|R_1(M,N)-R_0(M,N)\|
              \le64\tau\,b^{5/3}|\log(M/N)|.           \tag{R.17}
$
The two factors in the variation integral have product norm at
most $b^{5/3}$, independent of the intermediate frequency.

For $b\le3$, $b^{5/3}<7$ and
$N|\log(M/N)|\le3|M-N|$, hence
$
 N\|R_1(M,N)-R_0(M,N)\|
                    \le2048\tau\,|M-N|.              \tag{R.18}
$
It vanishes exactly on the diagonal. A bare uniform
$O(\tau)$ frame difference multiplied by $N$ would instead
be unbounded; it cannot replace (R.18).

For the full family, the high cutoff is $|j|\ge97$ and
the quadratic coefficient bandwidth is192. Thus coupled
high frequencies have the same sign and ratio below3.
Equation (R.18) applies to both signs after the fixed unitary
curvature-row sign change. In Fourier convolution it pays
the unchanged drift-frame difference by
$2048\tau\|\partial_\phi d_0\|_{A^0}$.
The new transport $d_1\partial_\phi$ itself must remain in
the actual energy equation. This result does not turn the
first-order difference
$(d_1-d_0)\partial_\phi$ into a bounded zeroth-order operator.

For an unchanged local or primitive block $B_{MN}$, its exact
new-frame expression is
$
 F_1(M)^{-1}B_{MN}F_1(N)
   =C_M^{-1}[F_0(M)^{-1}B_{MN}F_0(N)]C_N .
$
The change of this block has norm at most
$
 8\tau\,\|F_0(M)^{-1}B_{MN}F_0(N)\|.                  \tag{R.19}
$
Indeed its coefficient is bounded by
$4\tau(1+3\tau)+3\tau\le8\tau$.
This statement transfers an already paid block; new M96
coefficient terms and their true intermediate primitive index
must still be paid separately.

## 6. Positive radial rates and the remaining actual audit

The exact reference rate is
$\kappa_\alpha=Ma_\alpha W_\alpha/2$.
Equations (R.1) and (R.5) give
$
 (1-\tau)^2\kappa_0\le\kappa_1\le(1+\tau)^2\kappa_0,
 \qquad |\kappa_1/\kappa_0-1|\le3\tau.                \tag{R.20}
$
All body rows therefore keep an explicit positive lower
reference after the real coefficient audit. This does not
identify old and new Volterra kernels without updating their
rate bounds.

For the actual M96 family one must now certify (R.1) from its
complete full-interval mean direction, the unchanged intrinsic
positive target, and the true outer scalar $q_*/(-m_R)$.
The saved original 4650-row body contains whole-row reference
bounds and kernels, not sampled exact Riccati solutions.
Those records can be consumed without recomputing them:
(R.5), (R.18)--(R.20), the complete new coefficient differences,
the low/high crossing maps and the actual new outer graph
provide the transfer data.

No terminal scalar or actual mean is inferred from a negative
window norm. No new p/g numerical integration is required by
this theorem. The remaining complete coefficient/outer audit,
its all-radial contractions, all source columns and the true
low/high Schur problem remain explicit obligations.
