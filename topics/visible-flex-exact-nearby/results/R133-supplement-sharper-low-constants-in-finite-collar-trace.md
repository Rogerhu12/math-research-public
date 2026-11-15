# R133 supplement: sharper low constants in the finite collar trace theorem

2026-11-15. This note sharpens the energy norm and the two polynomial
coefficients in
[the finite factorial collar theorem](R133-supplement-finite-factorial-collar-bounds-and-complete-high-inner-trace-gate.md).
The equation, actual ordinary source, complete means, genuine seams,
finite real differences and all state/reference identities are unchanged.
No actual numerical collar gate is asserted to have passed.

## 1. A norm that retains the same required controls

For a compactly supported two-vector on the same interval of length
$4\ell$, $0<\ell\le1$, define
$$
 \begin{split}
 Z&=\|u\|_2,\quad R=\|u_r\|_2,\quad V=\|u_\phi\|_2,\quad
 H=(Z^2+R^2+V^2)^{1/2},\\
 Y(u)&=\max\{H,\ell^{-1}Z,\ell^{-1/2}
                         \sup_r\|u(r)\|_{L^2_\phi}\}.
 \end{split}
 \tag{A.1}
$$
The angular measure remains normalized, and the radial measure remains
$dr$. This is a norm. It supplies every individual bound used in
(H.19), with $X_N$ replaced by
$Y_N=\sum_{q=0}^NY(u_q)$.

The Hilbert-valued Dirichlet Poincare and evaluation inequalities are
$$
 Z\le\frac{4\ell}{\pi}R,\qquad
                  \sup_r\|u(r)\|_2\le\sqrt\ell R .
 \tag{A.2}
$$
For the second assertion, at position $x$ in an interval of length
$4\ell$, express evaluation as the inner product of $u_r$ with
$\mathbf 1_{[0,x]}-x/(4\ell)$. Its squared norm is
$x(4\ell-x)/(4\ell)\le\ell$. Thus both true endpoints are used.

Put
$$
 c_r=1+2d_+/a_-,\qquad c_\phi=2/a_-,
$$
$$
 C_E^\sharp=
 \max\left\{
 \sqrt{\bigl(1+(4\ell/\pi)^2\bigr)c_r^2+c_\phi^2},
                      \frac4\pi c_r\right\}.
 \tag{A.3}
$$
The original complete energy gives
$$
 Y(u)\le C_E^\sharp
                \{\|\mathcal L_0u\|_2+L\|u\|_2\}.
 \tag{A.4}
$$
Indeed (E.11) gives $R\le c_r E$, $V\le c_\phi E$; (A.2) gives the
other two bounds, and the first term in (A.3) controls $H$.
No angular or radial source has been removed.

For illustration of the coefficient scale, the *conditional* inequalities
$$
 a_-\ge\tfrac12,\qquad d_+\le\tfrac18,\qquad \ell\le\tfrac1{16}
 \tag{A.5}
$$
imply $C_E^\sharp<5$. This follows from $c_r\le3/2$, $c_\phi\le4$,
$4\ell/\pi<1/12$ and
$(1+1/144)(9/4)+16<25$. These are not claimed as newly evaluated
bounds for the actual collar.

## 2. Two complete low-dimensional product inequalities

For a smooth compactly supported vector $u$ on the radial line times
the normalized $\pi/2$ circle,
$$
                \|u\|_4^2\le2ZH,\qquad
                \|u\|_6^3\le5ZH^2 .
 \tag{A.6}
$$
They pass to $H^1$ by the already justified extension and approximation.

Here is an explicit proof which keeps the circle mean. Let
$L_\phi=\pi/2$. The two radial endpoints give, pointwise in angle,
$$
 |u(r,\phi)|^2\le\int_{\mathbb R}|u||u_r|\,dr .
$$
On a whole circle,
$$
 |u(r,\phi)|^2\le
      \langle|u|^2\rangle_\phi
                 +2L_\phi\langle|u||u_\phi|\rangle_\phi .
$$
Multiply these inequalities and integrate in their respective variables:
$$
 \|u\|_4^4\le Z^2R(Z+\pi V)
                   \le4Z^2H^2 .
 \tag{A.7}
$$
For the last bound use
$R(Z+\pi V)\le\sqrt{1+\pi^2}\,H^2/2<4H^2$.
This proof includes the angular constant mode.

Apply the same argument to $|u|^3$. The radial coefficient is now $3/2$,
and the angular coefficient is $3L_\phi$. Holder gives
$$
 \|u\|_6^6
 \le\frac32\|u\|_4^4R(Z+3L_\phi V).
$$
Since $L_\phi<2$ and
$R(Z+6V)\le\sqrt{37}\,H^2/2<7H^2/2$, (A.7) yields
$$
                  \|u\|_6^6\le21Z^2H^4<25Z^2H^4 .
 \tag{A.8}
$$
The Euclidean vector derivative satisfies
$|\partial|u|^p|\le p|u|^{p-1}|\partial u|$, so no extra component
factor is needed.

## 3. The improved nonlinear coefficients and the same bootstrap

The exact five nonlinear terms remain those in (H.9).
For the finite factorial sequence, (A.6) and
$\sum_qZ(u_q)\le\ell Y_N$, $\sum_qH(u_q)\le Y_N$
give
$$
 \sum_q\|u_q\|_4\le
       \sqrt{\,2\Bigl(\sum_qZ(u_q)\Bigr)
                         \Bigl(\sum_qH(u_q)\Bigr)}
                       \le\sqrt{2\ell}\,Y_N ,
$$
$$
 \sum_q\|u_q\|_6\le
       5^{1/3}\Bigl(\sum_qZ(u_q)\Bigr)^{1/3}
                 \Bigl(\sum_qH(u_q)\Bigr)^{2/3}
                       \le(5\ell)^{1/3}Y_N .
 \tag{A.9}
$$
These are ordinary Cauchy--Schwarz and Holder for the finite index sum,
not an exchange of a Fourier sum with a radial supremum.

Consequently the five bounds in (H.20) become, in the same order,
$$
 6b_+M_\sigma\ell Y_N^2,\quad
 5b_+\ell Y_N^3,\quad
 b_+M_{1,\sigma}\ell^{3/2}Y_N^2,\quad
 2b_+M_\sigma\sqrt\ell Y_N^2,\quad
 b_+\ell Y_N^3 .
 \tag{A.10}
$$
The primitive bounds and the actual $z_\phi$ terms have not changed.
Thus use
$$
 c_2^\sharp=b_+\{6M_\sigma\ell+
                    2M_\sigma\sqrt\ell+M_{1,\sigma}\ell^{3/2}\},
 \qquad c_3^\sharp=6b_+\ell .
 \tag{A.11}
$$

Every other estimate in (H.24)--(H.29) uses only the individual
controls supplied by $Y$. Therefore the following three *actual*
gates suffice:
$$
 C_E^\sharp\ell(L+C_{\rm act})\le\tfrac14,
$$
$$
 C_E^\sharp\{\ell(L+C_{\rm lin}+c_{\rm out,0})
       +2\sigma/\ell+\sigma D_\sigma+c_{\rm out,1}\}\le\tfrac14,
$$
$$
 2(C_E^\sharp)^2c_2^\sharp\mathfrak A_N
       +4(C_E^\sharp)^3c_3^\sharp\mathfrak A_N^2\le\tfrac18 .
 \tag{A.12}
$$
The cutoff region with $\chi<1$ is still treated by the distinct
true $C^0$ bound (H.22)--(H.23); it is not divided by $\chi$.

For all finite $N$ these gates prove
$$
                         Y_N(1)\le2C_E^\sharp\mathfrak A_N .
 \tag{A.13}
$$
The same proof works for $u_q^h$ and real shifted Leibniz products:
translation preserves $Z,R,V,H,Y$ and all circle means.
The low starting estimate and the uniform barrier are therefore
unchanged in logic. The high cut conclusions (H.30)--(H.33b)
hold with $C_E$ replaced by $C_E^\sharp$.

This sharpens a sufficient gate for actual coefficient consumption.
It does not relax the high ordinary residual requirement for
approximate iterates, the mean term in $a_r/a$, the two-sided
continuous-state hypothesis, or the separate low physical
inner-curvature radius.
