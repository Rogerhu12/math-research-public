# R133 supplement: the complete moving first symbol and its root subtractions

2026-11-14, visible-exact-astra-0df / phase_inverse.

This gives the first strict-core symbol of the **complete current
moving Jacobi operator**, including its nonlocal primitive. It also
identifies the two exact subtractions needed to integrate its signed
mean to the current simple turning root. The operator is the one
linearized at the continuous centre with definition SHA
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`,
obtained from the full M32 candidate
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.

The principal ray return has now been normalized in an explicit
parameter family. Its rotation alone does not include the symbol
calculated here. In particular the cross-wave term contributes at the
same order as the diagonal nonlocal primitive. Omitting either gives
the wrong first coefficient.

The result below is a proved strict-core operator identity and a
convergent finite-part **definition**. No numerical value of that
finite part, or identification with the complete root/positive-cap
return, is asserted here. Those next steps must use the current
root frame and all actual ports. The exact symbolic consumer is
provided for public Actions execution; an execution record is a
separate artifact and is not invented by this text.

## 1. Fixed complete system

Use the notation of
[the complete quadratic-density theorem](R133-supplement-negative-quadratic-density-and-full-frequency-transport.md).
To distinguish it from the scalar phase coefficient, write
\(b=\beta_{\rm metric}=a_{\rm phys}'/a_{\rm phys}\). On a closed
strict negative interval let

\[
 q=\sqrt{-K},\quad \eta=-\gamma m>0,\quad
 r_\sigma=u+\sigma qv,\quad
 d=-b I(u^2+Kv^2),\quad c_\sigma=d+\sigma\eta q,
 \qquad I=\partial_\phi^{-1}P_{\ne0}.
 \tag{S.1}
\]

The complete wave equation, after the already proved radial scalar
gauge, is

\[
 w_r=(C\partial_\phi+2d_\phi+\ell)w+B w+\mathcal N w+f_w,
 \quad C=\operatorname{diag}(c_+,c_-),\quad
 \ell=-2R_0/m,
 \tag{S.2}
\]

\[
 B=\begin{pmatrix}0&B_+\\B_-&0\end{pmatrix},\qquad
 B_\sigma=-\frac{q_r}{2q}-b(1+r_\sigma^2),
 \tag{S.3}
\]

\[
 (\mathcal Nw)_\sigma
 =-b(r_\sigma)_\phi I(r_-w_++r_+w_-)
 -\frac{\sigma\gamma}{2}(r_\sigma)_\phi
                                  \langle w_+-w_-\rangle.
 \tag{S.4}
\]

The true residual \(R_0\), the second term of (S.4), and the ordinary
source \(f_w=nTf\) remain. Neither a true solution nor a vanishing
mean is assumed.

## 2. One primitive converts the quadratic density to a density

Retain the two independent means \(z=\langle w\rangle\) and put
\(y=Iw\), so \(w=\partial_\phi y+z\), \(\langle y\rangle=0\).
This is a bijection between the complete state and \((y,z)\), with
the declared one-order change of Sobolev index. It is not a bounded
identity in the original curvature L2 norm.

The exact principal identity is

\[
 I\{c_\sigma y_{\sigma,\phi\phi}
                         +2d_\phi y_{\sigma,\phi}\}
 =c_\sigma y_{\sigma,\phi}+d_\phi y_\sigma
                           -I(d_{\phi\phi}y_\sigma).
 \tag{S.5}
\]

Indeed the derivative of the first two terms on the right is the
braced expression plus \(d_{\phi\phi}y_\sigma\); their total mean
is zero because their sum is \(\partial_\phi(c_\sigma y_\sigma)\).
For every smooth periodic multiplier \(f\), the full primitive
commutator is

\[
 \boxed{\ I M_f=M_f I-I M_{f_\phi}I
               +(If)\langle\cdot\rangle-\langle fI(\cdot)\rangle.\ }
 \tag{S.6}
\]

Differentiating both sides and comparing their means proves (S.6)
without projecting a pullback. Both finite-rank terms are necessary.
They are retained in the complete mean/low equations, not set to
zero. On every fixed finite Sobolev window these smooth finite-rank
maps are smoothing, with constants depending on the corresponding
actual coefficient derivatives.

Using (S.5)--(S.6), the nonmean generator has expansion

\[
 C\partial_\phi+A_0+A_{-1}I+\mathcal R_{-2},
 \quad A_0=(d_\phi+\ell)\mathrm{Id}+B,
 \tag{S.7}
\]

where every diagonal entry is exactly

\[
 (A_{-1})_{\sigma\sigma}
                  =-d_{\phi\phi}-b(r_\sigma)_\phi r_{-\sigma}.
 \tag{S.8}
\]

The off-diagonal order-minus-one entries additionally contain
\(-\partial_\phi B_\sigma\). They are kept below. Formula (S.8)
comes from the full nested primitive in (S.4); replacing (S.4) by
zero would miss its second term.

Here \(\mathcal R_{-2}:H^s\to H^{s+2}\) is the exact remainder
obtained by (S.6), plus its explicitly retained mean maps. Existence
of a finite bound follows by two uses of the bounded primitive and
the full multiplier estimates on a strict interval. No small
numerical bound is asserted.

## 3. Cross-wave elimination and the two signed first coefficients

Use the off-diagonal order-minus-one normalizer with leading matrix

\[
 S=\begin{pmatrix}
 0&-B_+/(2\eta q)\\
 B_-/(2\eta q)&0
 \end{pmatrix},\qquad y_{\rm new}\longmapsto (\mathrm{Id}+SI)y_{\rm new}.
 \tag{S.9}
\]

In a fully invertible realization choose a finite \(N\) for which
\(\|P_{\ge N}SI P_{\ge N}\|_{H^s\to H^s}<1/2\), use that
operator on the high block and the identity on its complement.
The complete high-low and low-high terms remain in the equation.
The existence of such an \(N\) on a strict compact interval follows
from its finite multiplier bounds and the \(1/(4N)\) primitive.
This is not a quantitative cutoff-97 claim.

To check the diagonal coefficient without a symbolic convention
ambiguity, write \(T=\mathrm{Id}+S\partial_\phi^{-1}\) to order
minus one and solve
\(AT-T_r=TA^{\rm new}\). The zeroth order equation gives

\[
 A_0^{\rm new}=A_0+[C,S]=(d_\phi+\ell)\mathrm{Id}.
 \tag{S.10}
\]

At order minus one,

\[
 A_{-1}^{\rm new}
 =A_{-1}+CS_\phi-S_r+A_0S-SA_0^{\rm new}+SC_\phi.
 \tag{S.11}
\]

All terms involving \(S_r,S_\phi,C_\phi\) are off diagonal;
the common radial \(\ell\) commutes with \(SI\) exactly. The
diagonal contribution of \(A_0S-SA_0^{\rm new}\) is \(BS\).
Thus the two complete first coefficients are

\[
 \boxed{\ a_\sigma=-d_{\phi\phi}
       -b(r_\sigma)_\phi r_{-\sigma}
       +\frac{\sigma B_+B_-}{2\eta q}.\ }
 \tag{S.12}
\]

The remaining off-diagonal order-minus-one term is removed by an
off-diagonal order-minus-two normalizer using the same nonzero gap
\(2\eta q\). Its commutator with \(C\partial_\phi\) is
off diagonal at order minus one and therefore does not change
(S.12). The new remainder has two full angular gains on this
strict interval. All transformations act on the ordinary source;
their inverses and any interface matrices must be included in a
subsequent quantitative propagator.

The continuous-centre definition is useful here: (S.9) depends on
centre values and the intrinsic \(q,q_r,b,\eta\), so its two
traces agree at a join at which those data agree. A radial derivative
jump still enters the piecewise remainder. If an unrepaired centre
is used instead, the exact interface is \(T_+^{-1}J_{\rm old}T_-\);
it may not be replaced by the identity.

Subtracting the two rows gives the concrete signed density

\[
 \boxed{\ \Xi=a_+-a_-
       =\frac{B_+B_-}{\eta q}
                 -2bq(u v_\phi-v u_\phi).\ }
 \tag{S.13}
\]

All quadratic and quartic terms remain, since

\[
 B_+B_-=
 \left[\frac{q_r}{2q}+b(1+u^2+q^2v^2)\right]^2
                                      -4b^2q^2u^2v^2.
 \tag{S.14}
\]

The coefficient is independent of an assumption \(R_0=0\).
This does not make residual-dependent physical-coordinate bridge
errors vanish. It identifies the operator (S.2), exactly as stated.

## 4. Exact current-root finite part

Use the actual simple root \(r_*\), with inward coordinate
\(\rho=r_*-r>0\), and write

\[
 q^2=\rho k(\rho),\quad k>0,\qquad
 a_0=\frac{k_\rho}{4k}-b(1+u^2+\rho kv^2).
 \tag{S.15}
\]

The current joint complex germ proves analyticity of these
coefficients on a common candidate/scalar piece and a nonzero
\(\eta\). That is sufficient for the following finite part to
exist; the old reciprocal M256 centre is not used.
Since \(q_r/(2q)=-1/(4\rho)-k_\rho/(4k)\), (S.13) is exactly

\[
 \begin{split}
 \Xi={}&\frac{\rho^{-5/2}}{16\eta\sqrt k}
   +\frac{a_0\rho^{-3/2}}{2\eta\sqrt k}
   +\frac{a_0^2\rho^{-1/2}}{\eta\sqrt k}\\
 &-\left\{\frac{4b^2\sqrt k\,u^2v^2}{\eta}
              +2b\sqrt k(u v_\phi-v u_\phi)\right\}\sqrt\rho.
 \end{split}
 \tag{S.16}
\]

All means here are moving-label angular means, with normalized
period \(\pi/2\). The two coefficients of the nonintegrable terms
in \(\langle\Xi\rangle\) are

\[
 \boxed{\ g_0=\left.\frac1{16\eta\sqrt k}\right|_{\rho=0},\qquad
 g_1=\left.
 \frac{-\eta_\rho/\eta+(3/2)k_\rho/k
                    -8b(1+\langle u^2\rangle)}{16\eta\sqrt k}
                           \right|_{\rho=0}.\ }
 \tag{S.17}
\]

In particular the full \(\langle u^2\rangle\) must be retained;
radial replacement \(u=0\) is not legitimate for the present
centre. Define the current moving first-symbol finite part by

\[
 \mathfrak X=\lim_{\epsilon\downarrow0}
 \left\{\int_0^{r_*-\epsilon}\langle\Xi(r)\rangle\,dr
                  -\frac{2g_0}{3\epsilon^{3/2}}
                  -\frac{2g_1}{\sqrt\epsilon}\right\}.
 \tag{S.18}
\]

On a root collar \(0<\rho<h\), (S.18) is computed by the ordinary
convergent integral of
\(\langle\Xi\rangle-g_0\rho^{-5/2}-g_1\rho^{-3/2}\),
minus \(2g_0/(3h^{3/2})+2g_1/\sqrt h\). On substituting
\(\rho=s^2\), the remaining integrand extends continuously
through \(s=0\). Taylor integral remainders for
\(A=(16\eta\sqrt k)^{-1}\),
\(B=\langle a_0\rangle/(2\eta\sqrt k)\) evaluate it without
subtracting nearby divergent floating values:

\[
 2\frac{A(s^2)-A(0)-s^2A_\rho(0)}{s^4}
 +2\frac{B(s^2)-B(0)}{s^2}
 +\frac{2\langle a_0^2\rangle}{\eta\sqrt k}
 -2s^2\left\langle
       \frac{4b^2\sqrt k\,u^2v^2}{\eta}
             +2b\sqrt k(u v_\phi-v u_\phi)\right\rangle.
 \tag{S.19}
\]

The first quotient equals
\(2\int_0^1(1-t)A_{\rho\rho}(ts^2)dt\), and the second
equals \(2\int_0^1B_\rho(ts^2)dt\). These identities include
the exact \(s=0\) values. They also specify the genuine local
derivatives a validated root consumer has to supply.

## 5. What remains for the actual scalar phase and strong return

For a physical Fourier mode \(e^{4ij\phi}\), the coefficient
\(a_\sigma I\) contributes \(-ia_\sigma/(4j)\). That fixes
the unit conversion. It does not alone identify the first coefficient
of the full returned boundary equation. The latter still needs:

1. The complete nonmean first coefficient transported by the actual
   two rays and the paid final KAM coordinates.
2. The two-line current-root matching of (S.9), its finite part,
   amplitude and Maslov convention, including the exact endpoint
   matrices. A scalar height asymptotic is insufficient.
3. The actual positive regular graph, all mean/head paths, and the
   residual-sensitive bridge if the physical local operator is used.
4. A quantified full-frequency remainder in the chosen Sobolev
   window, and the scalar's interval over the eventual true PDE
   background.

Only after that matching may a multiple of (S.18) be called the
complete \(\beta/j\) phase. This result exposes an exact computable
ingredient and its necessary root subtraction, rather than granting
that uncompleted identification.

The public exact-identity producer is
`scripts/fourfold_codazzi_strict_subprincipal_identity.py`.
It checks the two signed matrix rows, the cross elimination, every
term of (S.16), the mean subtraction (S.17), and the physical
factor four. It does not accept a numerical finite Fourier matrix
as evidence for the whole operator.
