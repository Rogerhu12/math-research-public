# R133 supplement: the original angular primitive on the actual Airy amplitudes, with exact mean and residual identities

2026-11-14, phase_inverse. **Proved operator identities and analytic
transport construction.** The coordinate map is the genuine full-family
moving fold, not a replacement local physical equation. This result
keeps the full old angular mean, the old integration curves and exact
remainders. It provides ingredients for the root connection; it does
not yet claim that the actual finite reflection constant vanishes
or that the complete return has a paid strong $4/3$ remainder.

## 1. The actual coordinate input and its scope

[The actual moving principal fold](R133-supplement-actual-moving-analytic-principal-fold.md)
was evaluated in public run 43602612900: actual child return zero,
all 16 gates passed. Its native is
$\mathtt{9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd}$.
It applies at intrinsic $\eta_0$ to the whole explicit family
$Q^\delta=Q^0+\delta Z$, $|\delta|\le10^{-8}$, with all 193
direction coordinates and the true even mean.

Use its actual analytic map $(\rho,\phi)\mapsto(T,X)$, where
$\rho=r_*-r$, on the canonical product
$$
 |T|\le81/4000000,\qquad |\Im X|\le1/128.               \tag{I.1}
$$
The old angular derivative at fixed $\rho$ is
$$
 Y=\alpha\partial_X+\zeta\partial_T,\qquad
 \alpha=X_\phi,\quad\zeta=T_\phi,\quad
 {\cal D}=\alpha^2+T\zeta^2 .                         \tag{I.2}
$$
The actual bounds include
$|\alpha-1|<0.000032360621$,
$|\zeta|<4.403311\,10^{-9}$,
$|{\cal D}-1|<0.000064722289$ and
$\zeta=O(T^2)$ exactly. At the true root $T=0$, $X=\phi$.

Let $\Pi_\rho$ denote the normalized old mean in $d\phi$ on the
circle of period $\pi/2$, with $\rho$ fixed. Let $I_\rho$ be its
genuine mean-zero primitive. Thus
$$
 YI_\rho=I_\rho Y=1-\Pi_\rho,\quad
 \Pi_\rho I_\rho=0,\quad
 \|I_\rho\|_{L^2_\phi\to L^2_\phi}=1/4.               \tag{I.3}
$$
All operators in (I.3) are pulled back from the old circle.
In canonical coordinates that circle is usually a curved graph.
No equality with integration at fixed $T$ is asserted.

## 2. Exact two-amplitude algebra, for both signs and both Airy columns

Choose any entire solution $F$ of $F''(z)=zF(z)$ and set, for
$n=4|j|>0$ and $\epsilon=\operatorname{sgn}(j)$,
$$
 f_0(T)=F(n^{2/3}T),\quad f_1(T)=n^{-1/3}F'(n^{2/3}T),
 \quad f_0'=nf_1,\quad f_1'=nTf_0.                    \tag{I.4}
$$
Define the exact amplitude map
$$
 {\cal U}_{n,\epsilon}(v)
   =e^{i\epsilon nX}(v_1f_0+v_2f_1).
$$
Both independent Airy columns may be used; no derivative row is
discarded. Direct differentiation gives
$$
 Y{\cal U}_{n,\epsilon}(v)
 ={\cal U}_{n,\epsilon}\bigl[(nH_\epsilon+Y\,{\rm Id})v\bigr],
\quad
 H_\epsilon=
 \begin{pmatrix}i\epsilon\alpha&\zeta T\\
                 \zeta&i\epsilon\alpha\end{pmatrix},
\quad\det H_\epsilon=-{\cal D}.                       \tag{I.5}
$$
Here $Y$ differentiates the two amplitudes as well as their variable
coefficients in subsequent compositions. Dropping that operation
would change the exact operator.

The actual fold therefore gives a true analytic inverse
$H_\epsilon^{-1}$. In row-sum matrix norm it is bounded by
$$
 H_*=\frac{1+j+B_T}{1-\varepsilon_D}<1.000098,          \tag{I.6}
$$
using the actual native's $j,B_T,\varepsilon_D$ and $|T|<1$.
Its upper and lower off-diagonal entries vanish to orders at least
3 and 2, respectively. At the root
$H_\epsilon^{-1}=-i\epsilon\,{\rm Id}$.

## 3. A finite expansion with an exact full primitive remainder

For a chosen smooth periodic amplitude $v$, define
$$
 v_0=H_\epsilon^{-1}v,\qquad
 v_{k+1}=-H_\epsilon^{-1}Yv_k,\qquad
 W_N={\cal U}_{n,\epsilon}
          \left(\sum_{k=0}^{N-1}n^{-1-k}v_k\right).    \tag{I.7}
$$
Every product and derivative is evaluated in the actual coordinate
map. Telescoping (I.5) gives the exact equality
$$
 YW_N={\cal U}_{n,\epsilon}(v)
             +n^{-N}{\cal U}_{n,\epsilon}(Yv_{N-1}).
$$
Applying the true old primitive, not a formal symbol inverse, yields
$$
 \boxed{\ I_\rho{\cal U}_{n,\epsilon}(v)
   =W_N-\Pi_\rho W_N
       -n^{-N}I_\rho{\cal U}_{n,\epsilon}(Yv_{N-1}).\ } \tag{I.8}
$$
This holds even if the original source has nonzero mean.
The identity automatically retains the corresponding exact mean
compatibility: the old mean of the differentiated expression is
zero. No mean is set to zero by a Fourier-tail assumption.

For real old $\rho$ and real parameters, the actual last term obeys
$$
 \|\text{last term}\|_{L^2_\phi}
 \le \frac{n^{-N}}4
           \|{\cal U}_{n,\epsilon}(Yv_{N-1})\|_{L^2_\phi}.
                                                               \tag{I.9}
$$
The same $1/4$ primitive bound holds in the complete old-angle
Wiener and weighted Fourier Hilbert norms, when those functions
have the required genuine old-angle domains. Formula (I.9) does not
replace the Airy function on its right by a unit-sized surrogate.

## 4. Explicit analytic coefficient bounds and finite derivative losses

Let $\mathcal B_{\tau,\sigma}$ be the space of periodic two-component
amplitudes analytic on $|T|\le\tau$, $|\Im X|\le\sigma$, with maximum
component supremum norm. Choose
$$
 \tau_{\rm out}=81/4000000,\quad \tau_{\rm in}=19/10^6,
 \quad \sigma_{\rm out}=1/128,\quad\sigma_{\rm in}=1/256.
$$
For a fixed finite $N$, set
$$
 L_N=(N+1)\left(
  \frac{1+j}{\sigma_{\rm out}-\sigma_{\rm in}}
       +\frac{B_T}{\tau_{\rm out}-\tau_{\rm in}}\right).
                                                               \tag{I.10}
$$
Cauchy's inequality on $N+1$ equally spaced intermediate products
gives
$$
 \|v_k\|_{\rm in}\le H_*^{k+1}L_N^k\|v\|_{\rm out},
 \qquad
 \|Yv_{N-1}\|_{\rm in}\le(H_*L_N)^N\|v\|_{\rm out}.    \tag{I.11}
$$
The intermediate products, and therefore derivatives of
$H_\epsilon^{-1}$, are all included by this recursion.
In particular (I.8) is a finite identity with a rigorous remainder,
not an infinite series assumed to converge. There is no requirement
that $H_*L_N/n<1$ just to use this identity. Such an additional gate
would be needed for an infinite Neumann argument.

## 5. The entire old mean is exponentially small on each high Airy column

This statement is specific to these analytic columns, not an
operator claim that the independent mean equation disappears.

Put $M_F=\max(|F(0)|,|F'(0)|)$. The power-series recursion for
$F''=zF$ gives
$$
 F(z)=F(0)\sum_{k\ge0}\frac{z^{3k}}{9^k k!(2/3)_k}
     +F'(0)z\sum_{k\ge0}\frac{z^{3k}}{9^k k!(4/3)_k}.
$$
Since $(2/3)_k\ge(2/3)^k k!$, $(4/3)_k\ge k!$ and
$\sum x^{2k}/(k!)^2\le e^{2x}$ for $x\ge0$,
$$
 |F(z)|\le M_F(1+|z|)e^{|z|^{3/2}} .
$$
Unit-circle Cauchy, $(t+1)^{3/2}\le2t^{3/2}+2$ and $e<3$
then give the convenient complete bound
$$
 |f_0(T)|+|f_1(T)|
 \le20M_F(1+n^{2/3}|T|)\exp(2n|T|^{3/2}),\qquad n\ge1 .
                                                               \tag{I.12}
$$
This proof applies to both fundamental columns with their actual
initial normalizations; it uses no large-$n$ asymptotic remainder.

For $|\rho|\le4/10^6$, let
$T_c=(4/10^6)A_+^{2/3}$ and use the original angular contour
$\Im\phi=\epsilon h_\phi$, $h_\phi=3/1024$.
Require $T_c<\tau_{\rm in}$ and
$h_\phi+M_0<\sigma_{\rm in}$. The actual fold bounds imply on
this contour $|T|\le T_c$ and
$\epsilon\Im X\ge h_\phi-M_0$. Thus
$$
 \|\Pi_\rho{\cal U}_{n,\epsilon}(v)\|
 \le20M_F(1+n^{2/3}T_c)
       e^{-n c_\Pi}\|v\|_{\rm in},\qquad
 c_\Pi=h_\phi-M_0-2T_c^{3/2}.                          \tag{I.13}
$$
The old normalized mean is precisely the contour integral of the
full expression. No change of mean measure has been omitted.
The numerical consumer checks $c_\Pi>1/512$ from the actual fold
native. The same formula applied to (I.7), with its finite coefficient
sum, pays the complete $\Pi_\rho W_N$ in (I.8).
It remains an explicit finite-rank source term.

## 6. The actual nonlocal inverse J has a residual identity, not just a symbol

Write $P=1-\Pi_\rho$ and let $\mathcal A$ be the complete ordered
moving map from the nonmean first state to the nonmean second row:
$$
 \mathcal A=\eta\partial_\phi+L,\qquad
 L=P(-2buv)P-2bP v_\phi I_\rho uP .                   \tag{I.14}
$$
This is the original moving operator, with its projections and
primitive. The actual fold run newly proved on complete moving
$A_{1/128}$ and weighted Fourier $H^0_{1/128}$, as well as real
$L^2$,
$$
 \|J\|<0.825332620,\quad
 \|\partial_\phi J\|,\|J\partial_\phi\|<3.301330479,
 \qquad J=\mathcal A^{-1}.                            \tag{I.15}
$$
The radial Cauchy bound on the actual inverse image is
$\|\partial_rJ\|<253948.498330$.
These are full inverse bounds, not finite Fourier inverses.

For any proposed smooth trial $g$ and forcing $f$, define its
complete original nonmean residual
$E=\mathcal A Pg-Pf$. Then
$$
             JPf=Pg-JE,\qquad \|JPf-Pg\|\le\|J\|\|E\|. \tag{I.16}
$$
This exact identity can be applied to each finite two-amplitude
construction after all its old means are included.
The independent even mean equation of the full moving system is
not part of $J$ and remains an independent residual/source row.

Let $D_0=\partial_r-Pd\partial_\phi P$ on the nonmean sector.
Both orderings of $\partial_\phi J$ are bounded by (I.15).
Consequently
$$
 \|[D_0,J]\|
 \le \|\partial_rJ\|+
       J_1(2d_*+d'_* /4)=:C_{DJ},                    \tag{I.17}
$$
where $d_*,d'_*$ are genuine complete bounds for $d,d_\phi$ on
the same moving domain. The wider-strip bounds in the actual
fold native are sufficient. They are consumed with their real
domain instead of silently using the old half-disk radial fee.
The exact differentiated error is
$D_0(JPf-Pg)=-[D_0,J]E-JD_0E$.
Thus radial derivatives of a proposed inverse approximation can
be paid by actual source residuals and the full commutator,
without differentiating an unstructured error ball.

Equations (I.8) and (I.16) are also a direct construction route:
invert the point matrix $\eta H_\epsilon$, recursively cancel
the retained amplitude derivatives and local multiplier in (I.14),
and use (I.8) for every nested primitive. At any chosen finite
order, compute the exact residual $E$ including the true old mean,
then apply (I.16)--(I.17). A formal angular expansion alone grants
none of these full-error bounds.

## 7. Leading and forced Airy transport are genuinely analytic

The exact local part after the actual fold has the form
$$
 {\cal P}_{\rm loc}=\partial_T^2+T\partial_X^2+
          l(T,X)\partial_T+T^2m(T,X)\partial_X+v(T,X).
                                                               \tag{I.18}
$$
The complete nonlocal and independent mean operators remain
separate, as in the principal-fold theorem.

For $\mathcal U_{n,\epsilon}(a,b)$, direct differentiation gives
the exact decomposition
$$
 {\cal P}_{\rm loc}\mathcal U_{n,\epsilon}(a,b)
 =\mathcal U_{n,\epsilon}
       \left(n\,{\cal T}_\epsilon(a,b)
                      +{\cal L}(a,b)\right),          \tag{I.19}
$$
where $\mathcal L$ applies the displayed local differential
operator to each amplitude, and
$$
\begin{split}
 ({\cal T}_\epsilon)_0
 &=b+2Tb_T+2i\epsilon T a_X+lTb+i\epsilon T^2ma,\\
 ({\cal T}_\epsilon)_1
 &=2a_T+2i\epsilon T b_X+la+i\epsilon T^2mb .
\end{split}
$$
The term $b$ in the first line is the actual derivative of $T$
in $f_1'=nTf_0$; it must not be omitted.

For the forced transport system set these two components equal
to $F_b,F_a$, respectively. Put $\widetilde b=\sqrt T\,b$ and
$v_\pm=a\pm\widetilde b$. The two equations become exactly
$$
 \partial_Tv_\pm=-\frac l2v_\pm
   \mp i\epsilon\sqrt T(\partial_X+Tm/2)v_\pm
                  +F_a/2\pm F_b/(2\sqrt T).           \tag{I.20}
$$
Writing $t=\sqrt T$ removes the apparent singularity:
$$
 \partial_tv_\pm=-t\,l(t^2,X)v_\pm
 \mp2i\epsilon t^2\partial_Xv_\pm
 \mp i\epsilon t^4m(t^2,X)v_\pm
                  +tF_a(t^2,X)\pm F_b(t^2,X).         \tag{I.21}
$$
These are actual analytic scalar transport equations with
characteristic displacement at most $(2/3)|T|^{3/2}$. On a
strictly smaller analytic product with that angular margin,
standard characteristic integration is an explicit analytic
construction: compose the analytic coefficients with the true
linear-in-$X$ characteristic shifts, integrate in $t$, and multiply
by the exponential of the analytic scalar reaction integral.

For prescribed common analytic trace $v_+(0,X)=v_-(0,X)=a_*(X)$,
uniqueness gives $v_+(-t,X)=v_-(t,X)$. Therefore
$$
 a=(v_++v_-)/2,\qquad
 b=(v_+-v_-)/(2t)
$$
are analytic in $T$, including zero. The second expression has no
$C(X)/\sqrt T$ homogeneous term: such a term would assign different
initial traces to the two scalar transports.

For the leading homogeneous problem, $F_a=F_b=0$ and $a_*=1$,
one gets $b(0)=0$ and $b_T(0)=0$, hence $b=O(T^2)$.
For later finite orders the algebraic amplitude sources obtained
from (I.8) are analytic, so their transport solutions exist by
(I.21). The exact old-mean and primitive remainder terms stay
separate source residuals; they are not forced into this
two-amplitude class.
The analytic value of a later $a(0,X)$ is a freely specified
common amplitude normalization; the value of $b(0,X)$ is fixed
by $F_b(0,X)$.

This is more than an unproved power-series ansatz: each finite
transport amplitude is defined by a convergent analytic
characteristic integral. It is still not the actual reflected
solution of the full boundary problem until the complete
parametrix residual and both boundary rows are paid.

## 8. What remains between these identities and the actual root phase

An analytic common amplitude at the root cancels from a ratio of
the two oscillatory branches. An analytic next $b(0,X)$ multiplies
the derivative Airy branch, whose leading branch difference has
a factor $\sqrt{-T}$. These facts explain why a zero finite root
constant is a plausible outcome after the correct normalization.
They do not by themselves prove that outcome.

A valid completion must construct a two-row approximation using
both Airy columns and the genuine transports above; evaluate its
full original moving residual using (I.8), (I.14) and all projected
mean rows; correct that residual with the actual positive regular
graph and its same-reference interface inverse; and carry the
root error to the actual negative cut with a true full-input
Cauchy estimate. Every field, source, projection and endpoint
normalization must refer to the same repaired background or
the same explicitly paid parameter family.

Only after bounding that true correction in the required
frequency-weighted norms may one identify the actual finite
reflection constant and declare a strong $4/3$ remainder.
In particular the model Airy coefficient, the absence of a
formal $C/\sqrt T$, a finite Fourier experiment or the local
principal-fold Jacobian do not replace these remaining steps.
