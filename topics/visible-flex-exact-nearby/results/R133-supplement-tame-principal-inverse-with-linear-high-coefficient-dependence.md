# R133 supplement: tame full-circle principal inverse bounds with linear high-coefficient dependence

2026-11-15. **Proved analytic estimates.** No new numerical calculation is made.

The complete principal inverse can be bounded in positive Sobolev spaces with linear dependence on the high Sobolev norm of its coefficient. The adjoint gives a corresponding negative-window operator bound with one fewer coefficient derivative. The constants may depend on a fixed low coefficient norm and the existing L2 inverse. A first coefficient derivative has a complete tame bound of the same kind.

This supplies one scalar component needed by a possible full tame construction. It does not assert that the physical incoming operator, a changing geometric background, or its true coordinate changes satisfy the hypotheses.

## PTB1. Full scalar spaces and already proved inverse

Use the normalized circle of period $\pi/2$, physical frequencies $4j$ and
$$
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 \|f\|_s^2=\sum_j\Lambda_j^{2s}|\widehat f_j|^2,\qquad
 I=\partial_\phi^{-1}(1-\Pi),\quad C_I=\frac{\sqrt{17}}4 .
 \tag{PTB.1}
$$
For every real $r$,
$$
 \|I:H^r\to H^r\|\le\frac14,\qquad
 \|I:H^r\to H^{r+1}\|\le C_I,\qquad I^*=-I.
 \tag{PTB.2}
$$
The scalar constant coordinate is included. The identities $I1=0$ and $\Pi I=0$ do not make $\Pi M_cI$ vanish.

Let $c$ be a smooth, possibly complex coefficient, and assume the actual full operator
$$
 T_c=1+M_cI:L^2\to L^2,\qquad A_c=T_c^{-1},\qquad
 \|A_c\|_{0\to0}\le K,\quad K\ge1
 \tag{PTB.3}
$$
has already been established. The derivative bootstrap, duality and common-core agreement in [PSB](R133-supplement-complete-principal-Sobolev-bootstrap-and-coefficient-perturbations.md) then supply the same inverse on every fixed Sobolev space. Smoothness here allows those identities to be used before estimating them; no regularity is inferred by assuming the desired bound.

For the actual IC factors the existing [SEIA](R133-supplement-actual-individual-principal-energy-gates-and-two-window-inverse-bounds.md) supplies the L2 inverse. Its unique successful run is 43773319871/1, execution blob e1532b816ea344ee65e52a503279376a0c449299, 46192 bytes, SHA256 b0088f831471f29d41624e487586fbb9f4801ef7837f9b4dd3c29a57e51b3d29. The complete shared norm record, rather than its midpoint or an old logarithm, is the permitted K input. No SEI scalar is reevaluated here.

Write
$$
 c_r=\|c\|_r,\qquad c_{\rm W}=\sum_{j\in\mathbb Z}|\widehat c_j|,
 \qquad q_r=2^{\max(r-1,0)}\quad(r\ge0).
 \tag{PTB.4}
$$
Every quantity in (PTB.4) includes the full scalar mean. Complete upper bounds may replace them. They cannot be supplied by a nonmean bound without separately adding the mean.

## PTB2. Elementary full-series product estimates

For all labels $j,k$,
$$
 \Lambda_j\le\Lambda_{j-k}+\Lambda_k,\qquad
 \Lambda_j^r\le q_r(\Lambda_{j-k}^r+\Lambda_k^r).
 \tag{PTB.5}
$$
The first inequality follows by the Euclidean triangle inequality, with one of the two constant coordinates set to zero and then enlarged. The second is the concavity inequality for $0\le r\le1$ and the elementary convexity inequality for $r\ge1$.

Convolution, absolute values and the $\ell^1*\ell^2\to\ell^2$ inequality therefore give
$$
 \|ab\|_r\le q_r\left(\|a\|_r\|b\|_{\rm W}
                         +\|a\|_{\rm W}\|b\|_r\right),\qquad r\ge0.
 \tag{PTB.6}
$$
This uses the complete two-sided Fourier sums. It is valid for complex functions and does not remove a mean.

The decreasing-integral estimate $\sum_{j\ge1}j^{-2}\le2$ gives
$$
 \sum_{j\ne0}(4j)^{-2}\le\frac14 .
 \tag{PTB.7}
$$
Consequently
$$
 \|If\|_{\rm W}\le\frac12\|f\|_0,\qquad
 \|g\|_{\rm W}\le\frac32\|g\|_1 .
 \tag{PTB.8}
$$
For the second inequality use
$\sum_j\Lambda_j^{-2}\le1+1/4<9/4$ and Cauchy--Schwarz. These are exact analytic upper bounds, not fresh interval evaluations.

For $s\ge1$, Hilbert-scale interpolation gives
$$
 \|f\|_{s-1}\le\|f\|_s^{1-1/s}\|f\|_0^{1/s}.
 \tag{PTB.9}
$$
At $s=1$ the right side is simply $\|f\|_0$.

We will use the elementary absorption implication
$$
 U\le A+b U^{1-1/s}F^{1/s}
 \quad\Longrightarrow\quad
 U\le2A+(2b)^sF,\qquad s\ge1 .
 \tag{PTB.10}
$$
If $U\le2A$ there is nothing to prove. Otherwise $U/2<bU^{1-1/s}F^{1/s}$ and division by the positive power of U proves the second alternative. Zero cases follow directly or by continuity.

## PTB3. Positive windows, linear in the high coefficient norm

Put $f=A_cg$ and $G_r=\|g\|_r$. The exact equation is
$$
 f=g-cIf,\qquad \|f\|_0\le K G_0 .
 \tag{PTB.11}
$$
For $s\ge1$, (PTB.2),(PTB.6),(PTB.8) give
$$
 \|f\|_s\le G_s+\frac{q_s}{2}c_s\|f\|_0
                    +q_s C_I c_{\rm W}\|f\|_{s-1}.
 \tag{PTB.12}
$$
Apply (PTB.9)--(PTB.10). With
$$
 B_s(c)=q_s c_s+(2q_s C_I c_{\rm W})^s,\qquad s\ge1,
 \tag{PTB.13}
$$
the complete result is
$$
 \boxed{\ \|A_cg\|_s\le2G_s+K B_s(c)G_0,\qquad s\ge1.\ }
 \tag{PTB.14}
$$
At each fixed s, the coefficient dependence in the high norm $c_s$ is linear. The possibly large other coefficient factor depends only on the fixed low norm $c_{\rm W}$. No smallness condition on $c_s$ or on a derivative matrix is needed.

For $0<r<1$, the same product estimate uses
$\|If\|_r\le C_I\|f\|_{r-1}\le C_I\|f\|_0$. It gives
$$
 \boxed{\ \|A_cg\|_r
 \le G_r+K q_r(c_r/2+C_I c_{\rm W})G_0,\qquad 0<r<1.\ }
 \tag{PTB.15}
$$
At $r=0$ use the original exact bound K. These estimates agree with the same inverse on every common domain. They are additional complete bounds, not replacements for the sharper saved SEIA windows.

Define the convenient complete right-hand side
$$
 \Phi_r(c;g)=
 \begin{cases}
 K G_0,&r=0,\\
 G_r+K q_r(c_r/2+C_I c_{\rm W})G_0,&0<r<1,\\
 2G_r+K B_r(c)G_0,&r\ge1.
 \end{cases}
 \tag{PTB.16}
$$
Then $\|A_cg\|_r\le\Phi_r(c;g)$ for every fixed $r\ge0$.

## PTB4. Adjoint estimates and the same negative-window inverse

Let
$$
 z=(T_c^*)^{-1}g,\qquad T_c^*=1-I M_{\overline c}.
 \tag{PTB.17}
$$
The L2 inverse bound remains K and the exact identity is
$$
 z=g+I(\overline c z),\qquad \|z\|_0\le K G_0 .
 \tag{PTB.18}
$$
For $g\in H^1$, (PTB.8) and $\|c\|_\infty\le c_{\rm W}$ give
$$
 \|z\|_{\rm W}\le\|g\|_{\rm W}
                   +\tfrac12\|\overline c z\|_0
 \le L(c)G_1,\qquad
 L(c)=\frac32+\frac12 c_{\rm W}K .
 \tag{PTB.19}
$$
No high norm of c occurs in this low bound.

For $s\ge1$, apply the primitive gain followed by (PTB.6) at order $s-1$:
$$
 \|z\|_s\le G_s+
 C_I q_{s-1}\{c_{s-1}L(c)G_1+c_{\rm W}\|z\|_{s-1}\}.
 \tag{PTB.20}
$$
Interpolation and the same absorption step prove
$$
 \boxed{
 \|z\|_s\le
 2G_s+2C_I q_{s-1}c_{s-1}L(c)G_1
              +K(2C_I q_{s-1}c_{\rm W})^sG_0 .
 }
 \tag{PTB.21}
$$
Since $G_0,G_1\le G_s$ for $s\ge1$, duality gives the same distributional inverse with
$$
 \boxed{
 \|A_c:H^{-s}\to H^{-s}\|
 \le 2+2C_I q_{s-1}c_{s-1}L(c)
                +K(2C_I q_{s-1}c_{\rm W})^s,\qquad s\ge1 .
 }
 \tag{PTB.22}
$$
The high coefficient norm in this operator estimate is $c_{s-1}$, and it occurs linearly. The two-sided inverse identities and common-core agreement are those already proved in PSB, rather than a new formal inverse.

For $0\le r\le1$ there is also the simpler direct adjoint estimate
$$
 \|z\|_r\le G_r+C_I\|\overline c z\|_{r-1}
          \le(1+C_I c_{\rm W}K)G_r .
 \tag{PTB.23}
$$
It yields the valid complete negative-window bound
$1+C_I c_{\rm W}K$. At zero the original K is another whole candidate. No logarithmic quantity is used in any product.

## PTB5. Exact first coefficient derivative, with a full tame bound

Use the exact PSB ordered identity
$$
 D A_c[h]g=-A_cM_hIA_cg .
 \tag{PTB.24}
$$
Let $h$ be a smooth coefficient perturbation, including its mean, and set
$$
 h_{\rm W}=\sum_j|\widehat h_j|,\qquad h_s=\|h\|_s.
 \tag{PTB.25}
$$
Write $f=A_cg$, $b=hIf$. The complete low bound is
$$
 \|b\|_0\le h_{\rm W}K G_0/4 .
 \tag{PTB.26}
$$
At $s\ge1$, the full product estimate gives
$$
 \|b\|_s\le q_s\{h_s K G_0/2
                         +h_{\rm W}C_I\Phi_{s-1}(c;g)\}.
 \tag{PTB.27}
$$
Apply (PTB.14) to $A_cb$. It follows that
$$
 \boxed{
 \begin{aligned}
 \|D A_c[h]g\|_s\le{}&
 q_s K h_s G_0
 +2q_s C_I h_{\rm W}\Phi_{s-1}(c;g)\\
 &+\frac{K^2}{4}B_s(c)h_{\rm W}G_0 .
 \end{aligned}
 }
 \tag{PTB.28}
$$
Thus the high norm of h enters linearly, and the high norms of c enter linearly with the low norm of h. The data g only require the indicated $H^{s-1}$ and L2 norms. The gain here comes from the exact intervening primitive, not a discarded mean or a changed derivative convention.

Equation (PTB.24) differentiates the true operator coefficient on the fixed circle. It does not differentiate a numerical norm upper bound. Changing the geometric chart, the physical input space, a physical mean receiver or a background solution creates additional actual derivatives and is not covered by renaming them h.

## PTB6. Uniform use and the actual remaining hypotheses

On any set where the actual full L2 inverse K and $c_{\rm W}$ are uniformly bounded, (PTB.14),(PTB.21),(PTB.22),(PTB.28) have uniform low constants at each fixed order and linear high-coefficient dependence. PSB's real signed coefficient neighborhood is one sufficient way to obtain a uniform L2 inverse; a bound on that neighborhood's Wiener norm is still needed.

The current successful SEI supplies one selected principal inverse and finite-order true-density data. It does not by itself supply every high coefficient norm, a uniform true geometric neighborhood or derivatives of a moving coordinate. Any new numerical evaluation of these bounds must use complete actual coefficient inputs in this public repository's Actions.

Both independent physical mean coordinates remain outside this scalar estimate and must retain their actual coupled equations. The full incoming error, given-head graph, independent ports, transported sign, finite columns and dual rows, nonlinear core, and tame bounds for the complete physical operator remain separate. These scalar tame estimates do not assert the final Nash hypotheses or the existence of the required exact surface family.
