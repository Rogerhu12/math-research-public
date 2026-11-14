# R133 supplement: exact leading-matrix normalization and root Taylor jets of the first Airy correction

2026-11-14, phase_inverse.

**Proved identities and an explicit derivative-budget refinement.**
The actual first correction has a nonzero second root value.
Bounding all its radial derivatives by Cauchy on the whole amplitude
can therefore be expensive. This theorem removes the complete leading
transport reaction exactly, gives a finite recurrence for the true
root coefficients, and bounds only the remaining Taylor tail by the
already paid analytic supremum.

The first correction, original forcing and physical family do not
change. Numerical root jets beyond the existing records still require
a public directed consumer. No full strong-return norm or cutoff is
claimed here.

## 1. The exact analytic leading matrix

Use the actual canonical convention of
[the first-amplitude construction](R133-supplement-old-root-product-and-separated-first-Airy-amplitude-budgets.md),
(G.14)--(G.19).
Write the leading amplitudes as $a_0,b_0$, and let
$\tau^2=T$, $\epsilon\in\{-1,1\}$.
The complete first forcing is $(F_b,F_a)=-\mathcal L_0w_0$,
with the full degree-zero operator, original mean and ordered
$H^{-1}H_D$ term retained.

The true leading branches and first correction branches are
$$
 v_{\pm,0}=a_0\pm\tau b_0,\qquad
 v_\pm=a_1\pm\tau b_1 .
 \tag{J.1}
$$
Both leading branches are nonzero on the paid rectangle.
Consequently
$$
 \Delta=a_0^2-Tb_0^2=v_{+,0}v_{-,0}\ne0,\qquad
 M_0=\begin{pmatrix}a_0&Tb_0\\b_0&a_0\end{pmatrix}
 \tag{J.2}
$$
has a genuine analytic inverse. This $M_0$ is a two-amplitude
matrix, not an old-angle projection or the nonlinear even mean.

Define
$$
 \binom{A}{B}=M_0^{-1}\binom{a_1}{b_1},\qquad
 \binom{f_b}{f_a}=M_0^{-1}\binom{F_b}{F_a}.
 \tag{J.3}
$$
Thus
$$
 f_b=\frac{a_0F_b-Tb_0F_a}{\Delta},\qquad
 f_a=\frac{a_0F_a-b_0F_b}{\Delta}.
 \tag{J.4}
$$
All products and quotients are of the actual analytic functions
at the same canonical point. The complete complex direction disk
and actual inverse-image domain are unchanged.

The exact leading division in (G.16) gives
$$
 (\partial_\tau\pm2i\epsilon\tau^2\partial_X)
   (v_\pm/v_{\pm,0})
   =(\tau F_a\pm F_b)/v_{\pm,0}.
 \tag{J.5}
$$
But the two sides of (J.3) imply
$$
 v_\pm/v_{\pm,0}=A\pm\tau B,\qquad
 (\tau F_a\pm F_b)/v_{\pm,0}=\tau f_a\pm f_b .
$$
Adding and subtracting (J.5), then using analytic continuation at
$\tau=0$, yields the nonsingular system
$$
 \boxed{\quad
 2A_T+2i\epsilon T B_X=f_a,\qquad
 2TB_T+B+2i\epsilon T A_X=f_b .
 \quad}
 \tag{J.6}
$$
The first root condition is $A(0,X)=0$.
The second equation fixes $B(0,X)=f_b(0,X)$.
The excluded homogeneous solution $T^{-1/2}$ does not belong to the
analytic germ. No extra free root datum is introduced.

Equation (J.6) removes the entire homogeneous leading reaction.
It does not set the original canonical coefficients $l,m$ to zero
in the full scalar operator or in the first forcing.

## 2. A finite triangular recurrence with all angular terms

Use Taylor coefficients divided by factorial:
$$
 A=\sum_{k\ge0}A_kT^k,\quad B=\sum_{k\ge0}B_kT^k,\qquad
 f_a=\sum_{k\ge0}f_{a,k}T^k,\quad
 f_b=\sum_{k\ge0}f_{b,k}T^k .
$$
Let $A_{-1}=B_{-1}=0$ and $A_0=0$. Coefficient extraction in
(J.6) gives the exact recurrence
$$
 \boxed{\quad
 A_{k+1}=\frac{f_{a,k}}{2(k+1)}
          -\frac{i\epsilon}{k+1}\partial_X B_{k-1},\qquad
 B_k=\frac{f_{b,k}}{2k+1}
          -\frac{2i\epsilon}{2k+1}\partial_X A_{k-1}.
 \quad}
 \tag{J.7}
$$
Every denominator is a positive integer. The recurrence is
triangular in the radial degree and preserves the complete angular
functions, including their mean. It neither truncates a Fourier
output nor replaces an old mean by a canonical one.

For example,
$$
 A_1=f_{a,0}/2,\qquad
 B_0=f_{b,0},\qquad B_1=f_{b,1}/3,
$$
$$
 A_2=f_{a,1}/4-\frac{i\epsilon}{2}\partial_X f_{b,0},
 \qquad
 B_2=f_{b,2}/5-\frac{i\epsilon}{5}\partial_X f_{a,0}.
 \tag{J.8}
$$
The complete first correction is then reconstructed by the finite
convolution of the Taylor coefficients in
$$
 a_1=a_0A+Tb_0B,\qquad b_1=b_0A+a_0B .
 \tag{J.9}
$$
The nonconstant leading factors in (J.9) are essential.

The same recurrence applies to angular derivatives of these functions.
For a directed norm recipe one uses the corresponding differentiated
forcing coefficients and the ordinary product rule. A coefficient
enclosed only as a scalar supremum can instead have its extra angular
derivatives paid by a strictly positive declared strip margin.

## 3. The first two true root derivatives in the original amplitudes

The closed leading formula gives, for every allowed complex $X$
and parameter,
$$
 a_0(0,X)=1,\qquad b_0(T,X)=O(T^2).
 \tag{J.10}
$$
Set $c(X)=(a_0)_T(0,X)$ and $d(X)=(a_0)_{TT}(0,X)$.
In the following formulas every forcing value or derivative is
evaluated at $T=0$; they are ordinary derivatives, not divided
Taylor coefficients.

Substituting (J.10) into (J.4), (J.7) and (J.9) gives
$$
 a_1(0)=0,\qquad b_1(0)=F_b,
$$
$$
 (a_1)_T=\tfrac12F_a,\qquad
 (b_1)_T=\tfrac13F_{b,T}+\tfrac23cF_b,
 \tag{J.11}
$$
and
$$
 (a_1)_{TT}
 =\tfrac12F_{a,T}+\tfrac12cF_a-i\epsilon F_{b,X},
$$
$$
 (b_1)_{TT}
 =\tfrac15F_{b,TT}
   +\tfrac4{15}cF_{b,T}
   +\left(\tfrac45d-\tfrac4{15}c^2\right)F_b
   -\tfrac{2i\epsilon}{5}F_{a,X}.
 \tag{J.12}
$$
The $c,d$ terms are the restored homogeneous leading reaction.
It would be incorrect to apply $1/(2k+1)$ directly to the
un-normalized $F_b$ coefficients beyond the root value and omit them.
The simpler diagonal factors apply inside the complete recurrence
(J.7), with its angular cross terms and the normalized forcing.

For a direct check, the original canonical transport equations are
$$
 2T(b_1)_T+b_1+2i\epsilon T(a_1)_X
      +lTb_1+i\epsilon T^2ma_1=F_b,
$$
$$
 2(a_1)_T+2i\epsilon T(b_1)_X
      +la_1+i\epsilon T^2mb_1=F_a .
 \tag{J.13}
$$
The leading homogeneous equations imply
$l(0)=-2c$ and $l_T(0)=-2d+2c^2$.
Evaluating (J.13) and its first two derivatives at zero reproduces
(J.11)--(J.12), including the factors and the sign of $i\epsilon$.
Terms involving $m$ vanish at these particular degrees because
$a_1(0)=0$ and $b_0=O(T^2)$; they remain in (J.7) at their true later
degrees through the complete normalized forcing and leading factors.

## 4. A root formula for the finite degree-zero forcing

The following optional identities reduce the first root values to
actual old-coordinate jets; they do not delete radial derivatives
that are still needed at higher degree.

At the true root,
$$
 T_\phi=0,\quad X_\phi=1,\quad K=0,\quad
 Q_*=a_*^{2/3},\quad \mu_*=Q_*^2,\quad
 T_r=Q_*,\quad X_r=d_{\rm drift}.
 \tag{J.14}
$$
Here $d_{\rm drift}$ denotes the old drift $d$ in
$D=\partial_r-d\partial_\phi$, rather than the leading second
derivative denoted $d(X)$ in Section 3.
The root values of $\eta,k,a_*,Q_*,\mu_*$ are radial scalars on
the full direction disk.

The exact leading expression and the old fold identities give
$$
 (b_0)_{rr}(r_*,\phi)
   =-\frac85 i\epsilon\,Q_*(d_{\rm drift})_{\phi\phi}.
 \tag{J.15}
$$
For proof, write $e=-d_{\rm drift}$ and $\rho=r_*-r$.
From
$X_\rho=eX_\phi+\frac23a\rho^2A_\phi$ and
$2\rho(A_\rho-eA_\phi)+3A=3aX_\phi$,
$$
 X_{\rho\phi}(0)=e_\phi,\qquad
 A_{\rho\phi}(0)=\tfrac35a_*e_{\phi\phi}.
$$
The exact formula $T=-\rho A^{2/3}$ then yields
$T_\phi=\frac25Q_*(d_{\rm drift})_{\phi\phi}\rho^2+O(\rho^3)$.
Insert this in $b_0=-2i\epsilon GX_\phi T_\phi$,
where $G(0)=X_\phi(0)=1$, to obtain (J.15).

Using the complete
[degree-zero operator](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md),
(L.4)--(L.6), and the exact
[fold matrix cancellation](R133-supplement-exact-fold-matrix-cancellation-and-leading-inverse-defect.md),
one therefore has
$$
 F_a(0,\phi)=
 \frac{i\epsilon}{Q_*}
       \left\{\frac85(d_{\rm drift})_{\phi\phi}-\vartheta\right\},
 \tag{J.16}
$$
$$
 F_b(0,\phi)=-\mu_*^{-1}
 \left\{(a_0)_{rr}
       -2d_{\rm drift}(a_0)_{r\phi}
       -T_0(a_0)_r+V_0\right\}_{r=r_*}.
 \tag{J.17}
$$
The terms omitted from these two point formulas vanish by
$a_0(0,\phi)=1$, $b_0=O(\rho^2)$ and $K(r_*)=0$.
The original $\vartheta,T_0,V_0$ remain complete; in particular
$\vartheta$ still includes $D\ell$, $\eta_r/\eta$, and the old mean.
Neither point formula identifies the degree-zero forcing with the
full old-$I/J$ residual.

All signs here use the fixed physical convention
$D=\partial_r-d_{\rm drift}\partial_\phi$.
Since $\partial_r^2=\partial_\rho^2$, (J.15) has no extra radial sign.

## 5. Only the genuine Taylor tail receives the full supremum

Let $w$ be either actual component $a_1$ or $b_1$,
holomorphic for $|T|<R_T$ and $|\operatorname{Im}X|\le\Sigma$.
Assume its already paid complete supremum is $M_w$.
Suppose the first $p+1$ exact root coefficients
$$
 w_k(X)=\frac1{k!}\partial_T^kw(0,X),\qquad 0\le k\le p,
$$
have directed derivative bounds
$\|\partial_X^q w_k\|\le C_{k,q}$ on a smaller strip
$\Sigma'<\Sigma$. Put $r<R_T$, $x=r/R_T$ and
$\Delta_X=\Sigma-\Sigma'$.

For $u=0,1,2$ define
$$
 {\cal T}_{p,u}(x)=
       \left(\frac{d}{dx}\right)^u\frac{x^{p+1}}{1-x}.
$$
These are nonnegative on $0\le x<1$, with continuous endpoint
values when a displayed power happens to have exponent zero.
Then the full mixed derivative obeys
$$
 \boxed{\quad
 \|\partial_T^u\partial_X^q w\|
 \le\sum_{k=u}^{p}\frac{k!}{(k-u)!}C_{k,q}r^{k-u}
  +q!M_w\Delta_X^{-q}R_T^{-u}{\cal T}_{p,u}(x).
 \quad}
 \tag{J.18}
$$
Empty sums are zero.

Indeed Cauchy on the original function gives
$\|\partial_X^q w_k\|\le q!M_w\Delta_X^{-q}R_T^{-k}$
for every omitted coefficient $k>p$.
Summing the exact differentiated geometric tail proves (J.18).
One does not first subtract a polynomial and enlarge the boundary
supremum by the size of that polynomial.
In particular the complete root value does not reappear in a
radial derivative term.

For the useful case $p\ge2$, the three tail factors are
$$
 {\cal T}_{p,0}=\frac{x^{p+1}}{1-x},\qquad
 {\cal T}_{p,1}=\frac{(p+1)x^p}{1-x}
                       +\frac{x^{p+1}}{(1-x)^2},
$$
$$
 {\cal T}_{p,2}
 =\frac{p(p+1)x^{p-1}}{1-x}
  +\frac{2(p+1)x^p}{(1-x)^2}
  +\frac{2x^{p+1}}{(1-x)^3}.
 \tag{J.19}
$$
An implementation may take the minimum of (J.18) and the earlier
valid Cauchy bound, after each has been fully paid.

The physical inner cover uses its actual
$r=\sup|\rho|\,A_+^{2/3}$, including the original root uncertainty.
Its strict image and strip inclusions must still be checked.
After (J.18), all first and second old-coordinate chain terms are
retained, as in (D.23). This does not bound a physical derivative
by a canonical derivative with the coordinate factors removed.

## 6. Required data and the preserved global obligations

To compute (J.11)--(J.12) sharply one needs actual bounds for
$F_b,F_{b,T},F_{b,TT},F_a,F_{a,T}$, their required angular derivatives,
and the leading $c,d$, on the same true root and complete parameter
disk. The whole saved first-forcing supremum alone does not supply
sharp values of those derivatives.

Direct differentiation of the un-divided local operator at the root
can require intrinsic $K$ through order five and $\eta$ through order
four. The strict-piece identity involving $1/\rho$ does not extend
those derivatives freely to $\rho=0$. One may instead bound any
uncomputed derivative by a genuine positive complex Cauchy margin;
the resulting cost must remain explicit.

If additional root derivative orders are needed, they are new
mathematics on the same analytic scalar/cubic germ, not a reason to
recompute its already accepted domain and lower-order evidence.
Finite polynomial Taylor coefficients and complete analytic primitive
tails must be treated together. A finite polynomial derivative alone
is not the derivative of the complete intrinsic metric.

The exact leading matrix, recurrence and Taylor-tail split leave the
first correction itself unchanged. Its original 1079 real seam
sources, exterior one-sided jets, old inverse remainder, independent
mean equation and full parameter identity therefore remain.
A successful finite root-jet calculation would sharpen the local
source budget. It would not itself provide the complete global strong
return, finite-head feedback, cutoff-97 inverse or nonlinear branch.
