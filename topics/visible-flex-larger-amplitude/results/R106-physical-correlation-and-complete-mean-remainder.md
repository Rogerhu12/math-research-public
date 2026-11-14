# R106: Physical Fourier correlation and the complete mean remainder

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

This proves a source and linear-readout tool for the same actual outer
equations. It retains the complete complex mean root and the pointwise
inverse. It does not claim that a new Green kernel, the remaining middle
window, cut consistency, or a full outer solution has been computed.

## 1. Fixed space and complete source

Use the true source coordinate $x$ and fixed real background
$$
s=r_x/r>0,\qquad \ell=w_x/w,\qquad
0<w\le1/2,\qquad E=1+w^2,\qquad c_{\rm bg}=s+|\ell|.
\tag{A1}
$$
All derivatives with subscript theta are angular derivatives; no extra
$r_x$ is inserted in the source equation. Let $P,\overline K$ have zero
angular mean and only even nonzero modes. They may be complex. A
nonnegative strip function $\tau(x)$ is fixed once and for all.

For a Fourier field $f$, define the radial-first Wiener norms
$$
\|f\|_{j,*}
 =\sum_{m\in2\mathbb Z}\sup_x
       (1+|m|)^j e^{\tau(x)|m|}|f_m(x)|,\qquad j=0,1.
\tag{A2}
$$
For a nonzero density $d(x)\ge0$, a source norm replaces $|f_m(x)|$
in (A2) by $|f_m(x)|/d(x)$. At a zero of $d$, this notation is used
only for a source already proved to vanish there. Equivalently one
may use the corresponding coefficientwise inequality without dividing.

Put
$$
R=\|P\|_{1,*}+\|\overline K\|_{1,*}\le1/64.
$$
The complex small-root theorem of R33, applied in this same radial
Wiener algebra, gives a unique complete mean $c$ and derivative
$$
\|c\|_{0,*}\le4R^2,\qquad
\|Dc[\delta P,\delta\overline K]\|_{0,*}\le16R\,\delta R,
\quad
\delta R=\|\delta P\|_{1,*}+\|\delta\overline K\|_{1,*}.
\tag{A3}
$$
The mean is not dropped or held fixed when differentiating.

Define the exact correlated fields
$$
T=P_\theta,\qquad C=\overline K+P_\theta,\qquad
U=\overline K_\theta-P,
$$
and the following full Laurent functions, including their zero modes:
$$
\begin{aligned}
Q&=EsU^2+\ell\left[E C^2-w^2(\overline K^2+P^2)\right],\\
A&=\ell\left[2c(\overline K+ET)+c^2\right],\\
l&=c+\overline K+ET.
\end{aligned}
\tag{A4}
$$
The complete nonmean source is
$$
\mathcal N(P,\overline K)
 =\Pi_\perp\frac{Q+A}{1+l}.
\tag{A5}
$$
This is the same source as R44/R89: expand $C^2$ and use $E-w^2=1$.
In particular
$$
E C^2-w^2(\overline K^2+P^2)
 =\overline K^2+2E\overline KT+ET^2-w^2P^2.
$$
Adding the mean to $\overline K$ then produces exactly $A$.
The mean term $c_x$ is an angular constant in the full second equation
and disappears under $\Pi_\perp$; it is not an additional nonmean
forcing. This does not remove the separate complete mean equation.

The projection in (A5) is applied only after multiplication by the
complete inverse. Neither the zero mode of $Q$ nor the $c^2$ term may
be discarded before that multiplication.

## 2. Why radial suprema do not lose the algebra

For each signed mode and component, take the fixed numbers
$$
p_m=(1+|m|)\sup_x e^{\tau(x)|m|}|P_m(x)|,\quad
k_m=(1+|m|)\sup_x e^{\tau(x)|m|}|\overline K_m(x)|.
\tag{A6}
$$
Their total is $R$. Since $\tau(x)\ge0$ and $|a+b|\le|a|+|b|$,
every product coefficient is bounded by a convolution of these fixed
numbers. The convolution bound is taken before the sum over output
modes. Thus (A2) is a Banach algebra and no estimate replaces
$\sum_m\sup_x$ by $\sup_x\sum_m$.

For a nonmean field with minimum $|m|=2$,
$$
\|P\|_{0,*}+\|\overline K\|_{0,*}\le R/3,\qquad
\|U\|_{0,*}\le R,\qquad \|C\|_{0,*}\le R.
\tag{A7}
$$
For the density $c_{\rm bg}$, a slightly more careful coefficient
argument is useful. The normalized $s$-material bilinear coefficients
of $Q$ have absolute value at most $E$. The normalized $\ell$-material
coefficients have absolute value at most $E+w^2/9$; here each
undifferentiated nonzero input supplies a factor at most $1/3$.
Consequently each individual coefficient of the combined bilinear
form, after division by $c_{\rm bg}$, is at most
$$
\frac{Es+(E+w^2/9)|\ell|}{s+|\ell|}
\le \frac54+\frac1{36}=\frac{23}{18}.
$$
Applying this bound to the fixed component masses (A6) gives
$$
\|Q/c_{\rm bg}\|_{0,*}\le\frac{23}{18}R^2,\qquad
\|DQ[\delta]/c_{\rm bg}\|_{0,*}
 \le\frac{23}{9}R\,\delta R.
\tag{A8}
$$
This coefficient argument is essential: merely combining two unrelated
pointwise norms with the variable weights $s/c_{\rm bg}$ and
$|\ell|/c_{\rm bg}$ would not justify a sum-of-radial-suprema bound.

## 3. Complete cubic and derivative remainder, with exact constants

Let $d(R)=1-5R/4-4R^2$. Equations(A3),(A7) give
$$
\begin{aligned}
\|l\|_{0,*}&\le 5R/4+4R^2,&
\|Dl[\delta]\|_{0,*}&\le(5/4+16R)\delta R,\\
\|A/c_{\rm bg}\|_{0,*}&\le10R^3+16R^4,&
\|DA[\delta]/c_{\rm bg}\|_{0,*}
 &\le(50R^2+128R^3)\delta R.
\end{aligned}
\tag{A9}
$$
For example, differentiating $A$ gives
$2\ell[Dc(\overline K+ET+c)+c(\delta\overline K+E\delta T)]$.
The two contributions are bounded respectively by
$40R^2+128R^3$ and $10R^2$, preserving the full $Dc$.

On $0\le R\le1/64$, $d(R)\ge1003/1024>0$ and the full inverse
has norm at most $1/d(R)$. Set
$$
\mathcal R=\mathcal N-\Pi_\perp Q
 =\Pi_\perp\frac{A-Ql}{1+l}.
\tag{A10}
$$
The algebra estimates above imply
$$
\|\mathcal R/c_{\rm bg}\|_{0,*}
 \le R^3\frac{10+16R+(23/18)(5/4+4R)}{d(R)}.
\tag{A11}
$$
The coefficient on the right is increasing in $R$ and at $1/64$ is
exactly $36640/3009<13$. Hence
$$
\boxed{\|\mathcal R/c_{\rm bg}\|_{0,*}\le13R^3.}
\tag{A12}
$$

Differentiate (A10) as a quotient, keeping every term:
$$
D\mathcal R[\delta]
=\Pi_\perp\left[
 \frac{DA-DQ\,l-Q\,Dl}{1+l}
 -\frac{(A-Ql)Dl}{(1+l)^2}\right].
\tag{A13}
$$
Its norm divided by $c_{\rm bg}R^2\delta R$ is at most
$$
\begin{aligned}
J(R)={}&
\frac{50+128R+(23/9)(5/4+4R)+(23/18)(5/4+16R)}{d(R)}\\
&+\frac{R[10+16R+(23/18)(5/4+4R)](5/4+16R)}{d(R)^2}.
\end{aligned}
\tag{A14}
$$
Every displayed positive numerator is increasing and $d$ is decreasing,
so $J$ is increasing on this interval. At $R=1/64$ it is exactly
$177343168/3018027<60$. Therefore
$$
\boxed{\|D\mathcal R[\delta]/c_{\rm bg}\|_{0,*}
       \le60R^2\delta R.}
\tag{A15}
$$
The exact slacks are $2477/3009$ in (A12) and
$3738452/3018027$ in (A15). These are estimates for the complete
mean and inverse remainder, not a finite Neumann truncation.

For a common convex domain whose full strong radius is at most
$R_*$, integration of (A15) along the line segment gives
$\|\mathcal R(X)-\mathcal R(Y)\|_{c_{\rm bg},0,*}
\le60R_*^2\|X-Y\|_{1,*}$. The segment's entire domain must be paid;
one cannot use just the smaller endpoint norm.

## 4. The frequency-resolved quadratic derivative

Let $a+b=m$ be signed even modes. The exact two-material derivative
of the unprojected $Q$ is
$$
\begin{aligned}
(DQ)_m={}&2Es\sum_{a+b=m}U_a\,\delta U_b\\
&+2\ell\sum_{a+b=m}
 \left[E C_a\,\delta C_b
       -w^2(\overline K_a\,\delta\overline K_b
                    +P_a\,\delta P_b)\right].
\end{aligned}
\tag{A16}
$$
Here $\delta U_b=ib\,\delta\overline K_b-\delta P_b$ and
$\delta C_b=\delta\overline K_b+ib\,\delta P_b$.
All coefficients are evaluated at the same radial point and same
background. If absolute Fourier caps are used, each convolution term
carries exactly
$e^{\tau(x)(|m|-|a|-|b|)}\le1$.
For a constant strip this is the usual fixed factor; for a varying
strip it must remain inside the appropriate actual position bound
until an outward bound has been taken.

One may separately bound $U,C,P,\overline K$ by certified radial
mode masses. In particular the $\ell$-material derivative costs
$2E|C_a||\delta C_b|$ rather than the generally larger bound obtained
by independently replacing $C$ by
$|\overline K|+|P_\theta|$.
The residual term with $w^2$ remains, even when the correlated $C$
is very small. The complete remainder is (A15), not zero.

For reflection-symmetric complex parameters, odd $P$ and even
$\overline K$ give equal absolute masses at opposite modes; this is
not an assertion of real conjugacy. If an input is a real sine or
cosine amplitude, convert it to its two complex half amplitudes
before using (A16), or explicitly retain the equivalent pair
formula. There is no unrecorded factor2.

If the centre has support $|a|\le92$, its pure quadratic source is
zero for $|m|\ge186$. This does not make the complete source zero,
and does not delete the remainder (A12). The derivative support
restriction $a+b=m$ is also exact; it can be retained when constructing
finite-band positive matrices.

## 5. Computing the correlated readout from existing true flows

For a positive real sine/cosine mode, write
$P=P_m^{\sin}\sin(m\theta)$ and
$\overline K=K_m^{\cos}\cos(m\theta)$. Then
$$
C_m^{\cos}=K_m^{\cos}+mP_m^{\sin},\qquad
U_m^{\sin}=-P_m^{\sin}-mK_m^{\cos}.
\tag{A17}
$$
The linear combinations are taken with their signs before the
absolute value. They are equally valid for complex reflected
amplitudes.

For a signed PHYSICAL solution column $(\phi_P,\phi_K)$, its
$C$ column is $m\phi_P+\phi_K$. If the saved column instead has
trace-zero coordinates $Y=F(P,\overline K)$, $F=\sqrt{rw^3}$,
the physical $C$ column is $(m\phi_{Y,1}+\phi_{Y,2})/F$.
This output conversion does not alter the source coefficient
$F(s)$, the Wronskian, or the source $x$ Jacobian.

Thus the true one-sided or two-point Green formula may be read by
this new output row before its absolute source integration. No new
ODE is mathematically necessary if complete signed columns at all
original target subpanels have been retained. Replacing this by
$m|\phi_P|+|\phi_K|$ is always legal but loses precisely the
correlation this tool is designed to keep.

The $C$ readout for the weak Wiener norm has no extra factor $1+m$;
the original strong $P,\overline K$ readouts retain that factor.
One must not turn the weak $C$ readout into a strong one for free.
Only the weak Wiener norm of $C$ is needed in (A16). The map
$(P,\overline K)\mapsto\overline K+P_\theta$ is bounded from the
original strong space to that weak space. Hence one can use a
Banach ball with additional $C$-norm inequalities without requesting
another free angular derivative. Such a ball is an intersection
inside the same original field space; $C$ is not an independent
new unknown.

In an actual nonlinear certificate, both quadratic materials and every required remainder density,
the actual $C$ readout, the complete mean domain, the inverse,
both physical initial data, and all remaining Fourier bands must
still be paid. This text provides the exact formulas and sufficient
universal remainder constants; it does not supply those new numerical
kernels.

## 6. Exact execution and unchanged data

The independent BigInt function
physicalCorrelationConstants() in
[closure_physical_correlation_constants.js](../computations/closure_physical_correlation_constants.js) was actually
executed in the current V8 tools environment. All six universal
comparison gates passed. The complete exact numerator/denominator
ledger is
[2026-11-13-closure-physical-correlation-constants.json](../notes/2026-11-13-closure-physical-correlation-constants.json).

No scientific input packet, Arb flow, source integral, original
candidate, or published result was changed. The original R104
linear kernels and their reported failed coarse comparison remain
valid and unchanged. No result about the full outer PDE or the
closed surface follows solely from this source lemma.

## References

- [R33: Complete complex mean and fixed radial Fourier masses](R33-full-head-forcing-on-a-variable-analytic-strip.md).
- [R44: Compatible height and complete source](R44-compatible-outer-height-and-continuous-defect.md).
- [R89: Complete weak source bound](R89-actual-outer-high-frequency-source-inverse.md).
- [R98: Mixed-density source and field norms](R98-mixed-density-low-middle-high-closure.md).
- [R104: Actual source-resolved physical kernels](R104-source-resolved-middle-physical-Green.md).
