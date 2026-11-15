# R133 supplement: finite factorial collar bounds and the complete high inner-trace gate

2026-11-15. Analytic theorem for real approximate moving states on a
genuine two-sided positive collar. The argument is finite: no complex
extension of the unknown state, infinite analytic norm, or prior high
norm smallness is assumed. The complete high ordinary residual is an
explicit input.

This note continues
[the residual-sensitive collar energy and first-angular trace](R133-supplement-positive-collar-energy-and-residual-sensitive-first-angular-cut-trace.md).
Its notation and actual moving source units are retained. In particular
the second residual mean occurs in the radial principal-speed bound.
No numerical target, old profile or existing source certificate is
recomputed here.

## 1. Actual states, coefficients and finite input window

On
$$
 I=[c-2\ell,c+2\ell],\qquad 0<\ell\le1,
 \tag{H.1}
$$
let $Q$ and $Q^0$ be real states for the same intrinsic coefficients
$(\beta,G,K)$, with $G,K>0$. They are continuous across every genuine
radial seam. The ordinary residuals are
$$
 f=Q_r-\mathcal F(Q),\qquad f^0=Q^0_r-\mathcal F(Q^0).
$$
Neither residual is assumed zero. As in (E.5)--(E.13) put
$$
 W=P Q,\quad W^0=P Q^0,\quad z=W-W^0,\quad
 F=P(f-f^0),\quad P=\operatorname{diag}(K^{-1/4},K^{1/4}),
$$
$$
 b=\beta\sqrt K,\quad \alpha=\beta+\frac{K_r}{4K},
 \quad g=GK^{1/4},\quad
 a=-G\langle v\rangle\sqrt K>0,\quad
 d=-bI_\phi(|W|^2),\quad d_0=-bI_\phi(|W^0|^2).
 \tag{H.2}
$$
Here $a$ is the principal speed, not the physical radial coordinate.
All angular integrals use normalized measure $(2/\pi)d\phi$ on the
$\pi/2$ circle; all radial integrals use $dr$.

Fix a finite integer $N\ge1$. Assume the actual difference $z$ belongs
to $H^1(I\times S^1)$ and is bounded, and that its equation holds with
the stated ordinary source. We first give the a priori calculation for
smooth angular states. Section 8 justifies the same result by finite
real angular differences using only this initial $H^1$ regularity.
Smooth angular Nash iterates are an intended application; a core
solution or an iteration limit is not assumed to exist.

Suppose genuine bounds on the same collar give
$$
 a\ge a_->0,\quad |d|,|d_0|\le d_+,\quad
 |a_r/a|\le L,\quad
 |\alpha|\le\alpha_+,\quad |b|\le b_+,\quad |g|\le g_+ .
 \tag{H.3}
$$
The exact near-solution identity is
$$
 \frac{a_r}{a}
 =\frac{G_r}{G}+\frac{K_r}{2K}
    +\beta(1-\langle u^2+Kv^2\rangle)
                         +\frac{\langle f_2\rangle}{\langle v\rangle}.
 \tag{H.4}
$$
Thus (H.3) needs this real residual-mean contribution, or a directly
verified bound for the same actual logarithmic derivative.
An ordinary $L^2$ residual alone is not an $L^\infty_r$ mean bound.

Assume $\eta=\|z\|_{L^\infty(I\times S^1)}$ is known. For a proposed
$0<\sigma\le1$, take complete reference bounds
$$
 \begin{split}
 M_\sigma&\ge
       \sum_{m\in4\mathbb Z}e^{\sigma|m|}
                          \sup_{r\in I}|W^0_m(r)|,\\
 M_{1,\sigma}&\ge
       \sum_{m\in4\mathbb Z}|m|e^{\sigma|m|}
                          \sup_{r\in I}|W^0_m(r)|,\\
 D_\sigma&\ge
       \sum_{m\in4\mathbb Z}|m|e^{\sigma|m|}
                          \sup_{r\in I}|(d_0)_m(r)|.
 \end{split}
 \tag{H.5}
$$
Euclidean vector coefficient norms are used. These are genuine joint
coefficient bounds, with sum outside radial supremum. For the explicit
selected family $Q_0+\delta Z$ the angular support is finite; (H.5) is
a bound on that known reference and does not truncate $z$.

There is a less demanding finite alternative to (H.5). The proof only
requires the three bounds
$$
 \begin{split}
 \sum_{q=0}^N\frac{\sigma^q}{q!}
        \sup_I\|\partial_\phi^qW^0\|_\infty&\le M_\sigma,\\
 \sum_{q=0}^N\frac{\sigma^q}{q!}
        \sup_I\|\partial_\phi^{q+1}W^0\|_\infty&\le M_{1,\sigma},\\
 \sum_{q=0}^N\frac{\sigma^q}{q!}
        \sup_I\|\partial_\phi^{q+1}d_0\|_\infty&\le D_\sigma .
 \end{split}
 \tag{H.5a}
$$
The full joint bounds (H.5) imply these, but are not necessary.
If the same known reference has moving degree at most 96 and
$B_0,B_1,D_1$ bound its actual closed-row ordinary Wiener norms
$\|W^0\|_{A^0}$, $\|W^0_\phi\|_{A^0}$,
$\|(d_0)_\phi\|_{A^0}$ uniformly on $I$, then valid choices are
$$
 M_\sigma=e^{384\sigma}B_0,\qquad
 M_{1,\sigma}=e^{384\sigma}B_1,\qquad
 D_\sigma=e^{768\sigma}D_1 .
 \tag{H.5b}
$$
Here $d_0$ has degree at most 192. For each derivative separately,
finite support gives, for example,
$\sup_I\|\partial_\phi^qW^0\|_\infty\le384^qB_0$; then one sums the
factorial series. This argument does not exchange a Fourier sum with
a radial supremum and does not turn an arbitrary pointwise state
bound into a Wiener bound. It permits direct use of complete
already-certified closed-row $A^0$ bounds, after all same-reference
repair and selected-parameter fees have been paid.

Define the complete finite ordinary-source quantity
$$
 \mathfrak A_N=
 \sum_{q=0}^{N}\frac{\sigma^q}{q!}
       \|\partial_\phi^qF\|_{L^2(I\times S^1)}
                      +\ell^{-1}\|z\|_{L^2(I\times S^1)} .
 \tag{H.6}
$$
This definition includes the undifferentiated full source mean.
The theorem requires (H.6) at its stated order; it does not infer it
from a lower-order residual.

## 2. The exact linear part and complete nonlinear remainder

Use the actual radial speed but the known reference drift:
$$
 \mathcal L_0=\partial_r-d_0\partial_\phi+aJ_0\partial_\phi,\qquad
 J_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$
The exact same-coefficient difference equation is
$$
 \mathcal L_0z=\mathcal A z+\mathcal Q(z)+F,
 \tag{H.7}
$$
where
$$
 \mathcal A z=\alpha Dz
 -b\{|W^0|^2z+2W^0(W^0\cdot z)\}
 -2bW^0_\phi I_\phi(W^0\cdot z)
                   +g\langle z_2\rangle J_0W^0_\phi
 \tag{H.8}
$$
and
$$
 \begin{split}
 \mathcal Q(z)={}&
 -b\{2(W^0\cdot z)z+|z|^2W^0+|z|^2z\}\\
 &-bW^0_\phi I_\phi(|z|^2)
 -bI_\phi(2W^0\cdot z+|z|^2)\,z_\phi .
 \end{split}
 \tag{H.9}
$$
In particular the last term of (H.9) is retained. It is the drift
difference acting on the unknown derivative, not a bounded linear
zero-order remainder. The full principal mean variation is the last
term of (H.8).

The finite factorial derivative sum of the linear operator in (H.8)
has the ordinary $L^2$ bound
$$
 C_{\rm lin}=
 \alpha_++3b_+M_\sigma^2
                  +(b_+M_\sigma/2+g_+)M_{1,\sigma}.
 \tag{H.10}
$$
This uses $\|I_\phi\|_{L^2\to L^2}=1/4$. The mean in (H.8) commutes
with the angular derivatives exactly: positive derivatives of its
input have zero mean, and the differentiated output is supplied by
the complete known $W^0_\phi$. The zero-th input mean is kept.

## 3. A finite derivative norm with radial width

Choose a radial cutoff $\chi$, equal to one on
$I_1=[c-\ell,c+\ell]$, supported in $I$, with
$0\le\chi\le1$ and $|\chi'|\le1/\ell$. Choose a nonnegative Lipschitz
width function $\rho$ such that
$$
 \rho=0\ \hbox{outside }I_1,\qquad
 \rho=\sigma\ \hbox{on }I_2=[c-\ell/2,c+\ell/2],\qquad
 |\rho'|\le2\sigma/\ell .
 \tag{H.11}
$$
In particular $\chi=1$ wherever $\rho>0$, and $\rho=0$ wherever
$\chi'\ne0$. Piecewise linear choices and their justified smooth
approximations have exactly these properties.

For $0\le t\le1$ set $\rho_t=t\rho$ and define the finite family
$$
 u_q(t,r,\phi)=\chi(r)\frac{\rho_t(r)^q}{q!}
                                  \partial_\phi^qz(r,\phi),
 \qquad 0\le q\le N .
 \tag{H.12}
$$
The $q=0$ member is always $\chi z$. No values or derivatives of order
greater than $N$ are set to zero in the differential equation. We use
only the exact Leibniz identities through the finite order $N$.

For a compactly supported two-vector $u$ define
$$
 X(u)=\|u_r\|_2+\|u_\phi\|_2+\ell^{-1}\|u\|_2
                    +\ell^{-1/2}\sup_{r\in I}\|u(r)\|_{L^2_\phi},
 \qquad X_N(t)=\sum_{q=0}^N X(u_q(t)).
 \tag{H.13}
$$
The inequalities (E.10)--(E.11), together with the elementary
one-dimensional radial bounds
$$
 \|u\|_2\le4\ell\|u_r\|_2,\qquad
 \sup_r\|u(r)\|_2\le2\sqrt\ell\|u_r\|_2 ,
$$
give
$$
 X(u)\le C_E\{\|\mathcal L_0u\|_2+L\|u\|_2\},\qquad
 C_E=7(1+2d_+/a_-)+2/a_- .
 \tag{H.14}
$$
The same $C_E$ applies to the actual-drift operator because (H.3)
bounds both drifts.

The radial derivative of the weight in (H.12) has the exact form
$$
 \partial_r\left(\frac{\rho_t^q}{q!}\partial_\phi^qz\right)
 -\frac{\rho_t^q}{q!}\partial_\phi^qz_r
  =\rho_t'\partial_\phi\left(
                \frac{\rho_t^{q-1}}{(q-1)!}\partial_\phi^{q-1}z\right),
 \quad q\ge1 .
 \tag{H.15}
$$
After multiplying by $\chi$ this is $\rho_t'\partial_\phi u_{q-1}$.
There is no factor $q$ left. The only cutoff source is $\chi'z$ at
order zero, because the positive-order weights vanish on its support.

The known drift commutator also sums before an estimate is taken:
$$
 \begin{split}
 &\sum_{q=0}^N
 \left\|\chi\frac{\rho_t^q}{q!}
        [\partial_\phi^q,d_0]\partial_\phi z\right\|_2\\
 &\hspace{12mm}\le \sigma D_\sigma
                          \sum_{q=0}^N\|\partial_\phi u_q\|_2 .
 \end{split}
 \tag{H.16}
$$
Indeed the positive derivative order on $d_0$ has total coefficient
sum at most
$\sum_{k\ge1}\sigma^k\|\partial_\phi^kd_0\|_\infty/k!
\le\sigma D_\sigma$; the remaining finite sum is the one on the
right. This pays the complete commutator instead of repeating a
large order-dependent coefficient at each level.

## 4. The nonlinear product estimate has no dependence on N

We use two explicit low-dimensional facts. First, on this normalized
circle the zero-mean primitive satisfies
$$
 \|I_\phi h\|_{L^\infty_\phi}
     \le(\pi/4)\|h\|_{L^1_\phi}<\|h\|_{L^1_\phi}.
 \tag{H.17}
$$
It follows directly from the periodic sawtooth kernel of
$\partial_\phi^{-1}P_{\ne0}$; the full nonmean projection is part
of that kernel.

Second, zero extension of a compactly supported $u$ in the radial
variable gives
$$
 \|u\|_{L^4(\mathbb R\times S^1)}
                 \le2\|u\|_{H^1(\mathbb R\times S^1)},\qquad
 \|u\|_{L^6(\mathbb R\times S^1)}
                         \le2\|u\|_{H^1(\mathbb R\times S^1)} .
 \tag{H.18}
$$
For completeness the scalar constants follow from Fourier
Hausdorff--Young and Holder. With dual measure $d\xi/(2\pi)$ and
angular frequencies $m\in4\mathbb Z$, the relevant factors are
$$
 \sum_m\int(1+\xi^2+m^2)^{-2}\frac{d\xi}{2\pi}<1,\qquad
 \sum_m\int(1+\xi^2+m^2)^{-3/2}\frac{d\xi}{2\pi}<1 .
$$
The first sum is
$\frac14\sum_m(1+m^2)^{-3/2}$ and the second
$\pi^{-1}\sum_m(1+m^2)^{-1}$; bounding the latter angular sum by
$5/4$ proves both assertions. Two Euclidean components cost at
most $\sqrt2<2$. Since $\ell\le1$, the $H^1$ norm of $u$ is at
most $X(u)$.

Where $\rho>0$ one has $\chi=1$, so every derivative of (H.9)
with its factorial weight is a genuine finite convolution of
the $u_q$ and the corresponding known-reference derivatives.
The elementary bounds
$$
 \sum_q\|u_q\|_{L^4}\le2X_N,\quad
 \sum_q\|u_q\|_{L^6}\le2X_N,\quad
 \sum_q\sup_r\|u_q(r)\|_2\le\sqrt\ell X_N,\quad
 \sum_q\|u_q\|_2\le\ell X_N
 \tag{H.19}
$$
therefore give the following complete list of nonlinear costs:
$$
 \begin{array}{c|c}
 \text{term in (H.9)}&
       \text{sum of ordinary }L^2\text{ bounds}\\ \hline
 b\{2(W^0\cdot z)z+|z|^2W^0\}
       &12b_+M_\sigma X_N^2\\
 b|z|^2z&8b_+X_N^3\\
 bW^0_\phi I_\phi(|z|^2)
       &b_+M_{1,\sigma}\ell^{3/2}X_N^2\\
 2bI_\phi(W^0\cdot z)z_\phi
       &2b_+M_\sigma\sqrt\ell X_N^2\\
 bI_\phi(|z|^2)z_\phi&b_+\ell X_N^3 .
 \end{array}
 \tag{H.20}
$$
For example the fourth line uses (H.17) to bound the primitive
coefficient in $L^\infty_{r,\phi}$ by
$2b_+M_\sigma\sqrt\ell X_N$, and only then uses the complete
$L^2$ angular derivative sum. It does not require an unknown
joint Wiener bound.

Thus the part where the width is positive is bounded by
$$
 c_2X_N^2+c_3X_N^3,\qquad
 c_2=b_+(14M_\sigma+M_{1,\sigma}),\quad c_3=9b_+ .
 \tag{H.21}
$$
These bounds hold for every finite $N$ with the same constants.

Where $\chi<1$ the width is zero. Only the order-zero term occurs,
and the true pointwise bound $|z|\le\eta$ gives instead
$$
 \|\chi\mathcal Q(z)\|_2
       \le c_{\rm out,0}\|u_0\|_2
                       +c_{\rm out,1}\|(u_0)_\phi\|_2 ,
 \tag{H.22}
$$
on that region, where
$$
 \begin{split}
 c_{\rm out,0}
     &=b_+(3M_\sigma\eta+\eta^2+M_{1,\sigma}\eta/4),\\
 c_{\rm out,1}
     &=b_+(2M_\sigma\eta+\eta^2).
 \end{split}
 \tag{H.23}
$$
Here $\chi I_\phi(|z|^2)=I_\phi(z\cdot u_0)$, so the primitive
term uses its $L^2$ norm $1/4$ without dividing by $\chi$.
This separate estimate is necessary; writing $z=u_0/\chi$
would not give a uniform bound.

## 5. Explicit low and source gates, then a finite continuity argument

Let
$$
 C_{\rm act}=\alpha_++3b_+(M_\sigma+\eta)^2
                    +\{b_+(M_\sigma+\eta)/2+g_+\}M_{1,\sigma}.
$$
Assume the following three quantitative inequalities:
$$
 C_E\ell(L+C_{\rm act})\le\tfrac14,
 \tag{H.24}
$$
$$
 C_E\{\ell(L+C_{\rm lin}+c_{\rm out,0})
           +2\sigma/\ell+\sigma D_\sigma+c_{\rm out,1}\}
                                      \le\tfrac14,
 \tag{H.25}
$$
$$
 2C_E^2c_2\mathfrak A_N
                  +4C_E^3c_3\mathfrak A_N^2\le\tfrac18 .
 \tag{H.26}
$$
All coefficient and state quantities in these gates are low ones.
The high information is entirely the complete finite source quantity
$\mathfrak A_N$, not an assumed small high norm of the unknown state.
The quantity in (H.6) is taken at the fixed maximum width $\sigma$;
its nonnegative finite sum bounds the source for every $0\le t\le1$
by $0\le\rho_t\le\sigma$. Thus (H.26) is a common gate throughout
the continuity argument, not a separate pointwise gate at one width.

At $t=0$ the positive-order members of (H.12) vanish. Applying
the actual-drift difference estimate (E.13)--(E.15) to $\chi z$
and using (H.24) proves
$$
 X_N(0)\le\tfrac43C_E\mathfrak A_N .
 \tag{H.27}
$$
For every $t\in[0,1]$, sum (H.14), use (H.7)--(H.23), and retain
the full weighted ordinary source (H.6). The result is
$$
 X_N(t)\le C_E\mathfrak A_N+\tfrac14X_N(t)
                         +C_Ec_2X_N(t)^2+C_Ec_3X_N(t)^3 .
 \tag{H.28}
$$
The cutoff source is exactly the second term in (H.6).
No source mean has been removed.

For a fixed smooth iterate and finite $N$, $X_N(t)$ is continuous.
If it first reached $2C_E\mathfrak A_N$, (H.26) would make the right
side of (H.28) at most $7/8$ of that value. This contradicts (H.28).
If $\mathfrak A_N=0$, the state difference is already zero by
(H.6). Consequently
$$
 \boxed{\qquad X_N(1)\le2C_E\mathfrak A_N .\qquad}
 \tag{H.29}
$$
This is an a priori finite continuity argument starting from a
proved low energy bound. It does not assume the high estimate
that it proves, and does not invoke a complex value of the
unknown state.

## 6. The actual high cut trace and its units

On $I_2$ the cutoff is one and the width is $\sigma$.
Equations (H.13) and (H.29) give, for every $0\le q\le N$,
$$
 \sup_{r\in I_2}\|\partial_\phi^qz(r)\|_2
     \le q!\sigma^{-q}\,2C_E\sqrt\ell\,\mathfrak A_N .
 \tag{H.30}
$$
At the actual cut $c$ let
$$
 p_c=\max\{K(c)^{1/4},K(c)^{-1/4}\}.
$$
The complete inhomogeneous Bessel norm is therefore bounded by
$$
 \boxed{\quad
 \|(Q-Q^0)(c)\|_{H^N_\phi}
 \le 2^{N+1}N!\sigma^{-N}
                         p_c\,2C_E\sqrt\ell\,\mathfrak A_N .
 \quad}
 \tag{H.31}
$$
For example $(1+m^2)^{N/2}\le2^{N/2}\max(1,|m|^N)$ proves a
stronger elementary conversion; the displayed factor includes
the full mean and is convenient for a conservative budget.

Take $N=8193$. A sufficient explicit numerical gate for the
previous physical inner-data conversion is
$$
 \sigma\ge2^{-32},\qquad
 p_c\,2C_E\sqrt\ell\,\mathfrak A_{8193}\le2^{1024},
 \tag{H.32}
$$
in addition to (H.24)--(H.26) and the actual first-angular gate
(E.21)--(E.22). Since $8193!<2^{13\cdot8193}$, (H.31) gives
$$
 \|(Q-Q^0)(c)\|_{H^{8193}_\phi}
                 <2^{46\cdot8193+1025}
                  =2^{377903}<2^{393000}.
 \tag{H.33}
$$
This is a genuine sufficient criterion. No assertion is made
that a present core iterate has already passed (H.24)--(H.26)
or its full source gate.

For the selected reference $Q^0=Q_0+\delta Z$, the [complete same-family bound](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)
gives $\|Z\|_{A^0,\mathrm{pair}}<19$ and moving degree at most 96. Hence, at this same cut, including
the complete mean,
$$
 \|\delta Z(c)\|_{H^{8193}_\phi}
 \le19\cdot385^{8193}<2^{73742},
 \qquad |\delta|\le10^{-10}<1 .
 \tag{H.33a}
$$
Indeed the largest Bessel frequency is
$\sqrt{1+384^2}<385$. Thus (H.33) also gives
$$
       \|(Q-Q_0)(c)\|_{H^{8193}_\phi}
                       <2^{377904}<2^{393000}.
 \tag{H.33b}
$$
No additional high-reference gate is needed in this selected-family
comparison. Its low contribution must still be paid at the actual
cut; the global bound 19 is not asserted to be a sufficiently
small low cut bound.

The ordinary moving trace in (H.31) is not itself a physical
Fourier projection. The signed mean of $v$, the normalized inverse
angle, and both actual curvature mean outputs remain part of
the subsequent physical conversion.
The low physical input gate can use [the complete shape and mean separation](R133-supplement-shape-and-mean-separated-physical-inner-curvature-trace.md):
$\|v-v_0\|_{H^1}\le15\,10^{-9}/128$ suffices, with the known selected-reference contribution included at the same cut. This relaxation does not replace any coefficient or source gate in (H.24)--(H.26).

## 7. Genuine seams, reference units and approximate iterates

The proof applies to approximate iterates, with full residuals,
before a core solution has been constructed. It requires one
continuous two-sided collar state. If the two traces at an
artificial cut are unrelated, or an actual seam jump is present,
the complete interface forms (E.23) remain. An arbitrary rough
cap input at a one-sided boundary is not an interior trace and
does not satisfy this hypothesis.

The scalar coefficient bounds in (H.3)--(H.5) can be supplied
from complete already computed positive rows restricted to the
chosen collar, with actual radial derivatives and means.
The existing cap-only interval $[9/10,25/8]$ does not by itself
supply the left half of a collar centred at $9/10$.
Neither a metadata interval nor a reference sign replaces the
actual mean and speed gates.

For a sequence of approximate core iterates, the theorem gives
a uniform high cut ball only if the displayed quantities,
especially $\mathfrak A_{8193}$, are uniformly bounded as required.
A merely finite high residual at each step is insufficient.
With such bounds and a separately proved actual trace limit,
weak lower semicontinuity preserves (H.31) at the limit.

For an exact state the source is $F=-Pf^0$ if the fixed reference
is approximate. The reference residual must still be paid;
it does not disappear when the unknown residual vanishes.
The exact-state specialization is useful after existence has
been proved, but is not used to justify (H.29) for the iterates.



## 8. Finite real differences remove a prior high-regularity assumption

For real $h\ne0$ let $T_hz(\phi)=z(\phi+h)$ and
$D_h=(T_h-I)/h$. On the actual periodic circle,
$$
 D_h(fg)=fD_hg+(D_hf)T_hg,\qquad
 D_h^q(fg)=\sum_{k=0}^q{q\choose k}
                     (D_h^kf)T_h^kD_h^{q-k}g .
 \tag{H.34}
$$
For more factors the same identity gives multinomial coefficients and
real angular translations of the remaining factors. The translations
preserve the actual normalized $L^p$ norms and commute with $I_\phi$,
the mean, $\partial_r$ and $\partial_\phi$.

Replace (H.12) by
$$
 u_q^h(t)=\chi\,\rho_t^qD_h^qz/q!,\qquad 0\le q\le N .
 \tag{H.35}
$$
For fixed $h$ all these functions are $H^1$ because $z$ is $H^1$.
No actual derivative of $z$ above first order is needed to start the
energy calculation. The order-zero member is still $\chi z$.

The known-drift term with $k=0$ in (H.34) is exactly
$d_0\partial_\phi u_q^h$ and remains in $\mathcal L_0$.
All the terms with $k\ge1$ obey (H.16): the reference difference
quotients satisfy
$\|D_h^kf\|_{L^\infty}\le\|\partial_\phi^kf\|_{L^\infty}$,
and translating $u_{q-k}^h$ changes none of its norms.
The same argument proves (H.10) and every product estimate
(H.20) without a new constant.

The radial width source is now exactly
$$
                         \rho_t'D_hu_{q-1}^h .
 \tag{H.36}
$$
Its norm is bounded by
$|\rho_t'|\|\partial_\phi u_{q-1}^h\|_2$, since
$D_hu=\int_0^1T_{sh}\partial_\phi u\,ds$ in $H^1$.
The cutoff cancellation is unchanged. Likewise
$\|D_h^qF\|_2\le\|\partial_\phi^qF\|_2$ uses precisely the complete
finite source input in (H.6).

It follows that (H.27)--(H.29) hold uniformly in $h$ for
$X_N^h(t)=\sum_qX(u_q^h(t))$. On $I_2$ this bounds
$D_h^qz$ in the genuine $H^1_{r,\phi}$ space, for every $q\le N$.
As $h\to0$, these difference quotients converge distributionally to
$\partial_\phi^qz$. Weak compactness identifies the limit and proves
its $H^1$ regularity. The radial Hilbert trace map is continuous on
$H^1_r(L^2_\phi)$, so the same limit gives the actual cut trace.
Weak lower semicontinuity proves (H.30)--(H.31).

This establishes the finite theorem from the initial $H^1$ state and
the complete finite high source assumption. There is no unproved
density of uniformly analytic unknown states and no exchange of
radial supremum with an infinite Fourier sum. The real differences
may leave the reflection subspace, which is harmless: the local
equation, the energy identity, and all mean formulas above hold on
the full $4\mathbb Z$ circle.

## 9. What is needed for a true residual-zero specialization

The exact selected reference $Q^0=Q_0+\delta Z$ has moving angular
degree at most 96. Its full ordinary residual is a polynomial in the
state with degree at most three, with radial scalar coefficients and
the complete angular primitive. Therefore
$$
             \operatorname{supp}_\phi f^0\subset\{|m|\le1152\},
                   \qquad 1152=4\cdot288 .
 \tag{H.37}
$$
The derivative $Q^0_r$ does not increase its angular degree.
The true radial seams and all residual means remain in $f^0$.
Multiplication by the radial matrix $P$ preserves this support.

Consequently the complete finite source sum of this reference obeys
$$
 \sum_{q=0}^N\frac{\sigma^q}{q!}
                \|\partial_\phi^q(Pf^0)\|_2
                      \le e^{1152\sigma}\|Pf^0\|_2 .
 \tag{H.38}
$$
For $\sigma\le2^{-12}$ the exponential is less than two.
This is a full Fourier support statement about the fixed reference
residual, not a truncation of the unknown state or its residual.

For an arbitrary approximate iterate the exact bound is
$$
 \mathfrak A_N\le
 \sum_{q=0}^N\frac{\sigma^q}{q!}
                    \|P\partial_\phi^q f\|_2
 +e^{1152\sigma}\|Pf^0\|_2+\ell^{-1}\|z\|_2 .
 \tag{H.39}
$$
Its first term must still be paid at every stated order.
A sequence of growing finite angular cutoffs does not make that term
uniform solely because each cutoff is finite.

If a separate construction has already given a genuine $H^1$ solution
of the original core equation on this same two-sided collar, then
$f=0$, (H.4) has no residual-mean term, and
$$
 \mathfrak A_N\le
      e^{1152\sigma}\|Pf^0\|_2+\ell^{-1}\|z\|_2 .
 \tag{H.40}
$$
This bound is independent of $N$. Section 8 then proves the high trace
directly for that solution whenever the actual coefficient, low-state
and source gates hold. One need not assume a uniform high residual
bound for the particular sequence previously used to construct the
solution. Its actual weak equation and initial $H^1$ regularity must
nevertheless have been proved.

Thus the new theorem has two precise uses: (H.39) for approximate
iterates with complete residuals, and (H.40) for an independently
constructed exact state. Both retain the same genuine collar,
reference residual, normalization, means and trace direction.
Neither use supplies the missing full core inverse, nonlinear core
self-map, or global matching.
