# R149 ASQ6. The full off-conjugacy phase inverse and its physical source

**Proved.** At a nonzero raw conjugacy defect the phase equation of the
selected physical system can be solved exactly in its entire circle
variable and one scalar. The scalar stays positive on the explicit
neighbourhood below. This includes the parabolic divisor at mean
multiplier one. We give all coefficient derivatives through order two,
the physical source and the exact residual of this elimination.

## The equation in the original chart

Use the actual double-leg return $P$, the lift $g$, $R$ and $J=g'\circ R$
from [PD.1–10](R133-supplement-complete-phase-row-approximate-inverse-and-quadratic-defect.md).
In particular $R$ uses $\rho_{15}$, and $E=P\circ g-g\circ R$ is raw.
For actual state variation $h=z+k h^a$, use the complete NP candidate
$h^a$ and its specified passive lift from
[CP.4,18](R147-supplement-uniform-positive-phase-pivot-near-the-mean-exact-centre.md).
Define
$$
 m=\frac{(P'\circ g)g'}J=1+\frac{E'}J,\quad
 Lz=\frac{D_QP[z]\circ g}J,\quad
 B=\frac{DP[h^a,1]\circ g}J,\quad F=\frac bJ-Lz .
 \tag{ASQ6.1}
$$
Here $b$ is the entire raw phase right side, with its constant. $z$
includes every affine state particular as well as the remaining
unknowns. If prescribed independent exterior inputs enter the
phase directly, subtract their entire raw differential from $b$.
With $\delta g=g'a$, $\langle a\rangle=0$, the exact remaining row is
$$
                 ma-a\circ R+Bk=F.                   \tag{ASQ6.2}
$$
Both $P'$ and $g'$ are positive. The variable-multiplier term in
(ASQ6.2) therefore includes the complete $E'a$ of PD.9, also in
the mean.

## Conjugation, weighted compatibility and small divisors

Write $\ell=\log m$, $\lambda=e^{\langle\ell\rangle}$,
$D_R=I-R^*$ where $R^*u=u\circ R$, $P_0=I-\langle\cdot\rangle$.
With the unique zero-mean solution
$u=D_R^{-1}(-P_0\ell)$, put $w=e^u$, $\chi=e^{-u\circ R}$.
Then $mw=\lambda(w\circ R)$. For any $G$, set
$$
 U(G)=(\lambda I-R^*)^{-1}_{\ne0}P_0(\chi G),\quad
 d(G)=-\frac{\langle wU(G)\rangle}{\langle w\rangle},\quad
 \mathfrak l_m(G)=\langle\chi G\rangle-(\lambda-1)d(G).
 \tag{ASQ6.3}
$$
The inverse with subscript $\ne0$ outputs only nonzero modes.
For every $n\ne0$ put $\theta_n=2\pi n\rho_{15}$. Exactly
$$
 |\lambda-e^{i\theta_n}|^2=(\lambda-1)^2+
                         \lambda|1-e^{i\theta_n}|^2 .
$$
Real functions stay real. PD.13–15 therefore give the whole inverse
$H^{s+1}_0\to H^s_0$ with norm at most $17/\sqrt\lambda$ for every real
$s$. For the gauge-fixed $a=w v$, its constant $v_0=d(G)$ follows from
$\langle wv\rangle=0$. The remaining scalar equation is
$\mathfrak l_m(F-Bk)=0$. Hence exactly
$$
 k=\frac{\mathfrak l_m F}{\mathfrak l_m B},\qquad
 a=w[U(F-Bk)+d(F-Bk)].                                   \tag{ASQ6.4}
$$
Substitution gives the whole (ASQ6.2). Conversely the nonmean
multipliers, the gauge, then the scalar fix the solution uniquely if
the denominator is nonzero. In particular $\lambda=1$ requires
$\langle\chi(F-Bk)\rangle=0$ and the same gauge. There is no division
by $\lambda-1$. Positive $\langle w\rangle$ also keeps this construction
uniform across $\lambda=1$. At the true selected conjugacy $m=1$ by
CP.2, so (ASQ6.4) recovers ASQ3.

## An explicit neighbourhood of invertibility

On CP.13, $\langle B\rangle>1/60$ and
$\|B\|_\infty<2.16(132)(25/24)=297$, by CP.9,15–17 and RP.23.
Also require the actual $\|\ell\|_{H^2}\le\eta=2^{-19}$, a separate
condition on the raw return/lift. With $v=17\eta$, set $d_*=v/2$.
PD.15 gives $\|u\|_{H^1}\le v$; its zero mean and
$\sum_{n\ne0}(1+16n^2)^{-1}\le\pi^2/48<1/4$ give
$\|u\|_\infty\le d_*$. Moving the nonmean inverse in (ASQ6.3) to
$P_0w$ in the normalized $L^2$ inner product gives
$$
 \|[(\lambda I-R^*)^{-1}_{\ne0}]^*P_0w\|_2
 \le\frac{17}{\sqrt\lambda}\|P_0w\|_{H^1}
 \le\frac{18e^{d_*}v}{\sqrt\lambda}.
$$
The last step uses the lowest physical frequency four and
$\|w'\|_2\le e^{d_*}\|u'\|_2$. Consequently the compatibility
functional extends to all $L^2$, even when the nonmean solution
itself needs a stronger input. More precisely,
$$
 |\mathfrak l_m G-\langle G\rangle|
 \le \Big[e^{d_*}-1+18 e^{3d_*}v
             |\lambda-1|/\sqrt\lambda\Big]\|G\|_2 .
$$
Since $|\lambda-1|/\sqrt\lambda=2\sinh(|\langle\ell\rangle|/2)
\le\eta/(1-\eta/2)$, the bracket is at most
$$
 D=\frac{d_*}{1-d_*}
       +\frac{18v\eta}{(1-3d_*)(1-\eta/2)}
   =\frac{6230684722697}{384281879761649375}.
$$
Here $297D<1/120$ and $120(1+D)<121$. Thus
$$
                  \mathfrak l_m B>1/120,\qquad
                  |k|\le121\|F\|_2 .                      \tag{ASQ6.5}
$$
One sufficient way to check the logarithm condition uses $e=E'/J$
and $t_e=\|e\|_{A^0}<1$. The Fourier power inequality proved below
gives $\|\log(1+e)\|_{H^2}\le\|e\|_{H^2}/(1-t_e)^2$.
This test uses the complete raw residual. The true selected point
uses CP.2 and CP.10 directly, irrespective of whether it lies in the
smaller ball centered at $\widetilde Q_*$. A $C^1$ lift ball by itself
does not supply this $H^2$ logarithm test.

## Explicit tame inverse and two derivatives

Write $|h|_r=\|h\|_{H^r}$ and
$T_r(f,g)=C_r(|f|_r|g|_1+|f|_1|g|_r)$,
$C_r=(9/8)2^{r-1}$, for $r\ge1$ as in PD.17. The same notation
applies to nonnegative norm profiles. Set $t=(9/8)v$ and
$$
 W_r=1+17|\ell|_{r+1}\sum_{j\ge1}j^r t^{j-1}/j! .
$$
Indeed $|u^j|_r\le j^r|u|_r\|u\|_{A^0}^{j-1}$: distribute
$\Lambda_{k_1+\cdots+k_j}^r\le j^{r-1}\sum\Lambda_{k_i}^r$
and apply convolution Young. Thus both $w$ and $\chi$ have norm at
most $W_r$. For integer $r$, the series is $e^t$ times a polynomial
with nonnegative integer coefficients (differentiate $e^t$ by $t\partial_t$
$r$ times and divide by $t$). This supplies rational upper bounds
using $e^t\le1/(1-t)$ in the present ball; the value at $t=0$ is one.

For any entire RHS $Y$ with profile $y_r=|Y|_r$, define
$$
 b(y)=121y_0,\qquad G_r=y_r+|B|_rb(y),\qquad
 V_r=(17/\sqrt\lambda)T_{r+1}(W,G),\qquad
 Z_r=V_r+e^{2d_*}V_1,\qquad I_r(y)=T_r(W,Z).           \tag{ASQ6.6}
$$
Then (ASQ6.4) obeys $|k|\le b(y), |a|_r\le I_r(y)$:
$|U|_r\le V_r$ and $|d|\le e^{2d_*}|U|_0$.
The last low bound can alternatively use the adjoint estimate above.
At order $s$ the forcing and column cost $s+1$ derivatives, and
$\ell$ costs $s+2$. Each multiplication in (ASQ6.6) takes at most
one high factor. High-background factors multiplying $G_2$ are genuine
low-data terms. Constants involving the fixed low orders remain visible.

Denote the solution by $(a,k)$, and denote first and mixed coefficient
jets by subscripts. Write $\mathcal T(a,k)=ma-a\circ R+Bk$.
For two bases, with all quantities compared in the same angular and
raw-source chart,
$$
 \mathcal T_1(\Delta a,\Delta k)
       =\Delta F-\Delta m\,a_0-\Delta B\,k_0 .
$$
For the difference, apply $(I_s,b)$ at base 1 to the profile of the
right side. For input order $r\ge1$ this profile is at most
$|\Delta F|_r+T_r(\Delta m,a_0)+|\Delta B|_r|k_0|$; at order zero
use the order-one upper bound or $\|fg\|_2\le\|f\|_\infty\|g\|_2$.
There is no inverse of an operator difference. On a two-parameter
surface the exact recursive data are
$$
 \begin{aligned}
 Y_i&=F_i-m_i a-B_i k,\\
 Y_{ij}&=F_{ij}-m_{ij}a-B_{ij}k-m_i a_j-m_j a_i-B_i k_j-B_j k_i.
 \end{aligned}                                          \tag{ASQ6.7}
$$
Use the same inverse on $Y_i,Y_j,Y_{ij}$ in that order.
Explicitly majorize each coefficient-times-function by $T_r$ and
each scalar product by $|B_*|_r b(y_*)$; majorize $a_*$ by
$I_r(y_*)$. This nonnegative recursion, together with (ASQ6.6), is a
finite explicit bound for each derivative, including its scalar.
At most $F,B$ of order $s+3$ and $\ell$ of order $s+4$ are needed
for $D^2$ in order $s$, with successively lower orders for the
differentiated data. The first derivative uses $s+2,s+3$.
The product proof and (ASQ6.6) show that every term at each level
is a single high factor times low factors. The low levels may consume
the two extra derivative buffers. For genuinely differentiable
coefficient families at these windows, the difference identity first
gives continuity and then, after subtracting the first jet, the
first difference quotient. Repeating on the first-jet equations
gives the mixed quotient, using the same inverse on the remainder.
This proves differentiability with the displayed losses, including
at $\lambda=1$.

These are coefficient derivatives. More is required for physical
directions. Set $M=(P'\circ g)g'$ and $N_B=DP[h^a,1]\circ g$,
$N_F=b-D_QP[z]\circ g$ in the conventions of (ASQ6.1). For any
of $C=m,B,F$ with respective numerator $N=M,N_B,N_F$,
$$
 JC_i=N_i-J_iC,\qquad
 JC_{ij}=N_{ij}-J_{ij}C-J_iC_j-J_jC_i,
 \quad J_i=g_i'\circ R .
 \tag{ASQ6.8}
$$
Here $J_{ij}=g_{ij}'\circ R$ for moving directions. A base-dependent
$z$ or passive lift contributes all its derivatives to $N_i,N_{ij}$;
so does the full external RHS. For fixed $h^a$, $D^2 N_B$ contains
$D^3P[\cdot,\cdot,(h^a,1)]\circ g$ as well as angular and lift
terms. The two-jet bound in coefficient coordinates does not obtain
this third variation by renaming an already paid Hessian.

## Return to the full physical equations

In raw regular coordinates substitute (ASQ6.4) into PD.3. The exact row
is $Az+(Ah^a-N_\nu)\mathfrak l_m(b/J-Lz)/(\mathfrak l_m B)=f$.
If an approximate regular solve is used, its complete error is
$Az-f+(Ah^a-N_\nu)k$, and the raw phase error contributed by this
linear solve is **zero**. In particular the finite NP trial leaves
its body, jumps, Robin, waist, means and height defects wherever
present. A one-world placement $t$ is recovered once from the
complete absolute height row. The relative height or prescribed
nonmean forcing still enters its physical matching row.

Equivalently one may first make the existing regular block
eliminations of [ASQ4](R149-supplement-actualsquare-CFC-physical-cross-and-tail-budget.md).
Here is the weighted phase row on that actual square. At fixed root
and selected exterior write $D_w,D_c,D_k,D_f$ for the
**full normalized phase functions** $\delta P\circ g/J$ of the
reconstructed physical states per unit $w,c,k$ and the entire affine
forced state respectively, including the direct metric in $D_k$.
The subscript $w$ denotes the linear map on the waist $w$, unrelated
to the positive multiplication weight in (ASQ6.3).
For $p=H^{-1}(Pf-PKQq-PXc-Pg_{\rm met}k)$ the weighted phase
compatibility is exactly
$$
 \begin{aligned}
 &\mathfrak l_m[(D_wQ-D_wP H^{-1}PKQ)q
 +(D_c-D_wP H^{-1}PX)c\\
 &\hspace{28mm}+(D_k-D_wP H^{-1}Pg_{\rm met})k]\\
 &=\mathfrak l_m[b/J-D_f-D_wP H^{-1}Pf].
 \end{aligned}                                            \tag{ASQ6.9}
$$
The unprojected functions, with these same signs, are used in
$U+d$ of (ASQ6.3) to reconstruct $a$ after solving the square.
The low waist and $\Theta$ rows retain ASQ4.2–3, the original
$J_{\rm cut}-1$ modes with $J_{\rm cut}=2^{4608}$, and their
$KQ,X,g_{\rm met},f$ crosses. The height row uses its own full
$D_w^H,D_c^H,D_k^H,D_f^H$ with the identical signed $p$ and
one translation coefficient one. The CFC stored means retain
their source responses, and independent exterior inputs enter
$D_f,f,b$ at their actual ports. CP's lower bound concerns the
uneliminated candidate in (ASQ6.1); it is not a bound on the
coefficient of $k$ after the high response in (ASQ6.9).

For an actual state-dependent left normalizer $O$ and raw regular
residual $r$, the correction includes
$D(Or)[x]=O Dr[x]+DO[x]r$ and
$$
 D^2(Or)[x,y]=O D^2r[x,y]+DO[x]Dr[y]+DO[y]Dr[x]+D^2O[x,y]r .
$$
A moving input chart also contributes $Dr[D^2\Xi]$ inside the
composed Hessian and $D\Xi$ on both first directions. These
identities retain the full base residual even at $E=0$. If the
normalizer also depends on $g$, its first and second gauge terms
must likewise be substituted after (ASQ6.4); the independence of
the *raw* regular map from $a$ is used before such normalization.
For a smoothed Newton step with data $-S\mathcal F$ and its actual
regular residual $d_{\rm reg}$, the exact new residual is
$(I-S)\mathcal F+(d_{\rm reg},0)+\int_0^1(1-t)D^2\mathcal F[\Delta,\Delta]dt$.
In the moving raw phase units its $L^2$ integral is at most
$400\mathcal H(\Delta)\mathcal E(\Delta)$ on the domain of
[RP.26–29](R144-supplement-full-off-constraint-principal-return-Hessian.md).
The physical chart uses RP.28's entire secant.

The [full-function implementation](../scripts/fourfold_codazzi_actualsquare_weighted_phase.py)
performs (ASQ6.3–4,7), including both zero-mode conditions. Its
scalar check implements the displayed rational comparison. No new
finite inverse or physical trajectory has been evaluated. The raw
phase has an exact elimination at the stated bases. Applying it to
a full nonlinear core iteration also needs the true regular inverse,
its physical source windows, neighbourhood control, and a summable
error estimate for the complete system.
