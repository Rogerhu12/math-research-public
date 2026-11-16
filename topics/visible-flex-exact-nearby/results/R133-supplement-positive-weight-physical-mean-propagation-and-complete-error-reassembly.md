# R133 supplement: positive-weight physical-mean propagation and complete error reassembly

2026-11-16, phase_inverse.

**Proved here:** the common positive angular weight in the exact mean-feedback quotient can be cancelled before taking an upper bound. The original metric identity also fixes the sign of the metric coefficient on the actual negative-curvature interval. Together these give new complete backward-propagation recipes for the same physical mean, using already saved scalar inputs and no angular-inverse norm inside the propagation exponent. The negative source and the waist endpoint admit an explicit new assembly from the resulting mean bounds.

All formulas below concern the same real background, complete reflected angular inverse, genuine trial, physical mean, ordinary radial measure and physical waist observation as JI, N, WEJ, WUA and WUE. They are analytic formulas and input qualifications. No new exponential, ball product, radial solve or scientific consumer has been executed for this note. The complete old successes and the preserved first-attempt prefix remain unchanged.

## WMR1. The actual scalar mean and its two real patches

Write
$$
 \Pi f=\langle f\rangle,\quad P=Id-\Pi,\quad
 I=\partial_\phi^{-1}P,\quad
 m=\Pi v,\quad S=u^2+Kv^2,\quad
 d=-\beta IS,\quad \eta=-\gamma m.
 \tag{WMR.1}
$$
The angular measure is normalized and the physical frequency is $4j$.
The background is real, $u$ is odd and $v$ is even. It is the original
continuous repaired background; its nonlinear PDE residual is not set
to zero. The already admitted real characteristic coefficient satisfies
$\eta>0$. The sign of $m$ is retained by its original qualification; no
pointwise sign of $v$ is assumed in this proof.

Use the same exact strict cut and root enclosure:
$$
 r_c=\frac{76285779072683}{320000000000000},\qquad
 r_-=\frac{1191984371497}{5000000000000},\qquad
 r_+=\frac{2383968743003}{10000000000000}.
 \tag{WMR.2}
$$
The actual root is $r_*\in[r_-,r_+]$. The strict patch is
$[0,r_c]$ and the local patch is $[r_c,r_*]$, with its coefficient
bounds inherited from the already qualified local germ. A bound saved
on the slightly larger real local interval is only used on this
physical subinterval. No sign statement about $K$ is extended beyond
the actual root.

Let $A$ and $J=A^{-1}$ be the original angular pair
$$
 A:\ H^{s+1}_{\rm odd}\longrightarrow H^s_{\rm even,0},
 \qquad
 J:\ H^s_{\rm even,0}\longrightarrow H^{s+1}_{\rm odd}.
 \tag{WMR.3}
$$
All $P$'s, the original $I$, and the nonlocal terms of N.4--5 are
included. In particular, $J$ is not a full signed-circle inverse.

For the same genuine height $f$ used in WEJ, put
$$
 k=Jb_2,\qquad
 h_1=J(D_0-B)f-zk,\qquad h_2=f+z,\qquad
 z'=a_{\rm eff}z-F_{\rm mean},\quad z(r_*)=0.
 \tag{WMR.4}
$$
Here $z$ is the original even physical mean. The condition at the root
is the actual definition of this completed trial, not a declaration
that its root-to-waist mean is identically zero. Its ordinary forcing,
all two-row states and the original positive/root discrepancy remain
those of WUA and WUE.

## WMR2. Cancel the common weight in the exact feedback

Set
$$
 \alpha=\frac{2\beta}{\eta},\qquad
 a_J=\exp\{-\alpha I(uv)\},\qquad
 w=1-\alpha uIv,\qquad D_J=\Pi(a_Jw).
 \tag{WMR.5}
$$
The factor $a_J$ is the angular integrating factor, not the physical
metric radius. It is real and strictly positive. JI.10 and the full
N.5 expression for $b_2$ give the exact WEJ.17--18 identity
$$
 \begin{split}
 a_{\rm eff}
 &=\beta(1-\Pi S)+2\beta\,\frac{\mathcal H}{D_J},\\
 \mathcal H
 &=\Pi\!\left[a_J
       \left(u^2-mKv+\frac{m}{\eta}ud\right)\right].
 \end{split}
 \tag{WMR.6}
$$
This uses $-\gamma m=\eta$ in the complete expression
$u^2-mKv-ud/\gamma$. It does not divide by $\beta$ and remains valid
where $\beta=0$. The complete mean of $v$, the drift $d$, and the
original nonlocal angular inverse are retained.

Suppose, on one of the admitted real patches, that
$$
 w\ge\delta>0.
 \tag{WMR.7}
$$
Then $D_J>0$ and
$$
 d\mathfrak p(\phi)=\frac{a_J(\phi)w(\phi)}{D_J}\,d\phi
 \quad\hbox{with normalized angular measure}
 \tag{WMR.8}
$$
is a positive measure of total mass one. Consequently the exact
quotient is
$$
 \frac{\mathcal H}{D_J}
 =\int\frac{u^2-mKv+(m/\eta)ud}{w}\,d\mathfrak p.
 \tag{WMR.9}
$$
No norm of $a_J$, $a_J^{-1}$ or $J$ has been taken in this equality.

For any complete same-patch bounds
$$
 U\ge\|u\|_\infty,\quad V\ge\|v\|_\infty,\quad M\ge|m|,
 \quad Q_K\ge|K|,\quad D\ge\|d\|_\infty,\quad
 \eta_->0,\quad \eta\ge\eta_- ,
$$
define
$$
 X=M Q_K V+\frac{MUD}{\eta_-},\qquad
 Q=\frac{U^2+X}{\delta}.
 \tag{WMR.10}
$$
Then
$$
 \left|\frac{\mathcal H}{D_J}\right|\le Q,\qquad
 \frac{\mathcal H}{D_J}\ge-\frac{X}{\delta}.
 \tag{WMR.11}
$$
For the second inequality write the numerator in (WMR.9) as $u^2+g$.
The pointwise bound $g\ge-X$, $w\ge\delta$ gives
$g/w\ge-X/\delta$, while $u^2/w\ge0$. Integrating against the
probability measure proves the result. It is not a lower bound
deduced from a previously computed upper bound for $\mathcal H$.

The choice $M=V$ is always valid and uses no new signed-mean estimate.
A sharper already qualified complete $|m|$ bound may be used only on
its own domain. The formula does not require $v$ to have one sign.

This cancellation is specific to the shared positive weight in
(WMR.6). A general positive lower for $D_J$ would not by itself prove
the pointwise condition (WMR.7).

## WMR3. The required pointwise gaps are already analytically qualified

On the strict patch, JI.3--4 and JI.12--13 give
$$
 \|u\|_\infty<\frac74,\qquad
 \|Iv\|_\infty<\frac7{16},\qquad |\alpha|<\frac12,\qquad
 w>\frac{79}{128}.
 \tag{WMR.12}
$$
The two primitive factors in $\|Iv\|_\infty$ are Fourier-Wiener
bounds: $Iv=I^2v_\phi$. No $L^\infty$ operator bound $1/4$ for $I$
is asserted. The already saved strict physical coefficient
$I_v$ may be coarser; that does not invalidate the independently
proved JI pointwise inequality.

On the local patch the actual completed nodes give, as wide rational
comparisons of their saved complete records,
$$
 \|u\|_\infty<1,\qquad \|Iv\|_\infty<\frac12,\qquad
 |\alpha|<\frac12.
 \tag{WMR.13}
$$
The three precise read-only paths are:

| Quantity | Actual node and complete path |
|---|---|
| $u$ upper | physical_coefficients_local.conclusion.complete_A0_jets.U.group_upper[0].ball |
| $Iv$ upper | physical_coefficients_local.conclusion.complete_A0_jets.I_v.group_upper[0].ball |
| $|\alpha|$ upper | same_angular_J_local.conclusion.new_complete_records.alpha_absolute_upper.ball |

Their original balls are respectively
$$
\begin{split}
 &[0.714759101152224654002214835338748279578360455877136000000475922096224286019
       \mathbin{+/-}4.02{\rm e}{-77}],\\
 &[0.472112519960540950582313059649055330372548844020161500000435718771486827900
       \mathbin{+/-}6.30{\rm e}{-78}],\\
 &[0.336212989812340749144281562000615991041963447551673515755311493736483935254
       \mathbin{+/-}1.12{\rm e}{-76}].
\end{split}
$$
These records are original complete local-germ bounds. Only their
comparison with the displayed rational constants is used here.
They are not samples of the true coefficients. Thus
$$
 w>\frac34
 \quad\hbox{on the physical local patch}.
 \tag{WMR.14}
$$

The fixed analytic choices used by the new recipes are
$$
 (U_s,\delta_s)=\left(\frac74,\frac{79}{128}\right),
 \qquad
 (U_\ell,\delta_\ell)=\left(1,\frac34\right).
 \tag{WMR.15}
$$
The strict lower is not moved to the root by continuity: (WMR.14)
has its own pointwise proof on the original local coefficient domain.
A numerical consumer may verify the same old-record rational
comparisons as admission, but it must not recompute the old
coefficient, $J$, $\alpha$ or $D_J$ targets.

## WMR4. The metric fixes the sign needed for backward propagation

The physical metric is
$$
 g=E_\nu(r)\,dr^2+a_{\rm phys}(r)^2\,d\phi^2,\qquad
 \beta=\frac{a_{\rm phys}'}{a_{\rm phys}},\qquad
 \gamma=\frac{\sqrt{E_\nu}}{a_{\rm phys}} .
 \tag{WMR.16}
$$
P.1 identifies these exact coefficients. R77.1 establishes that the
physical radius is even; its equation (4) is the exact radial
curvature identity
$$
 \left(\frac{a_{\rm phys}'}{\sqrt{E_\nu}}\right)'
       =-K\,a_{\rm phys}\sqrt{E_\nu}.
 \tag{WMR.17}
$$
R77 uses some similarly named phase variables elsewhere; none of
those phase variables is identified with the metric $\beta$ here.

On the already admitted negative-curvature interval
$0\le r\le r_*$, $a_{\rm phys}>0$, $E_\nu>0$ and $K\le0$.
The waist condition $a_{\rm phys}'(0)=0$ therefore gives
$$
 \frac{a_{\rm phys}'(r)}{\sqrt{E_\nu(r)}}
 =\int_0^r -K(t)a_{\rm phys}(t)\sqrt{E_\nu(t)}\,dt
 \ge0,\qquad \beta(r)\ge0.
 \tag{WMR.18}
$$
The derivatives and the integral have their original one-sided
piecewise meanings; the actual metric is sufficiently continuous
at the real joins. The original compact parameter change
$E_\nu=Ee^{\nu h}$ leaves $a_{\rm phys}$ unchanged and is positive
on the real domain. The same argument uses the actual $K_\nu$ on
its actual negative interval. It does not assert $\beta\mathcal H\ge0$,
nor does it extend a negative-curvature conclusion to the positive
side of the root.

Let $b\ge\beta$ be a complete same-patch saved bound, and let
$\mathcal B_0$ be the unchanged complete_mean_base_upper record,
which already bounds $|\beta(1-\Pi S)|$. Its old construction
$b(1+S_0)$ is not recomputed. Define two different new quantities:
$$
 \begin{split}
 A^{\rm abs}&=\mathcal B_0+\frac{2b(U^2+X)}{\delta},\\
 A^\leftarrow&=
 b\left((U^2-1)_++\frac{2X}{\delta}\right).
 \end{split}
 \tag{WMR.19}
$$
They satisfy
$$
 |a_{\rm eff}|\le A^{\rm abs},\qquad
 (-a_{\rm eff})_+\le A^\leftarrow .
 \tag{WMR.20}
$$
The second estimate keeps the two angular averages distinct:
$$
 \Pi S=\Pi u^2+K\Pi v^2\le\Pi u^2\le U^2,\qquad
 \frac{\mathcal H}{D_J}\ge-\frac{X}{\delta}.
$$
Hence $a_{\rm eff}\ge\beta(1-U^2-2X/\delta)$, and
$$
 (-a_{\rm eff})_+
 \le b\max(0,U^2-1+2X/\delta)
 \le b\bigl((U^2-1)_++2X/\delta\bigr).
$$
No comparison between the original $\Pi u^2$ and the weighted
$\int u^2\,d\mathfrak p$ is used. For (WMR.15), the two exact
constants $(U^2-1)_+$ are $33/16$ and $0$.

Both quantities in (WMR.19) are complete direct expressions.
The absolute coefficient is still required for $z'$ and the full
source. The one-sided coefficient is used only in the backward
propagator. Neither is obtained by subtracting an old upper bound.

## WMR5. A complete two-patch backward estimate

For $0\le r\le s\le r_*$ the actual scalar fundamental solution is
$$
 \mathcal E_z(r,s)=
 \exp\left(-\int_r^s a_{\rm eff}(t)\,dt\right)>0.
 \tag{WMR.21}
$$
The sign in this formula is essential. Equations (WMR.20)--(WMR.21)
bound it by the integral of the negative part of $a_{\rm eff}$.

Let
$$
 L_s=r_c,\qquad L_\ell=r_+-r_c,\qquad
 G_p=\exp(L_p A_p^\leftarrow),\quad p\in\{s,\ell\}.
 \tag{WMR.22}
$$
Let $C_{F,p}$ be the unchanged original record
mean_N6_p.conclusion.new_complete_records.complete_reflected_mean_source_upper.
It includes the original reflected assembly and the complete six-step
mean source, with
$$
 |F_{{\rm mean},n}(r)|\le C_{F,p}n^{-23/6}.
 \tag{WMR.23}
$$
All its old angular jets, $e_\kappa$, $J_r$ qualifications and full
terminal are retained. The original mean source does not depend on
a norm upper for $a_{\rm eff}$; changing the latter's proof does not
change this forcing.

Define the new complete bounds in backward order:
$$
 \begin{split}
 Z_\ell&=L_\ell G_\ell C_{F,\ell},\\
 Z_s&=G_s\bigl(L_s C_{F,s}+Z_\ell\bigr),\\
 Z_{r,p}&=A_p^{\rm abs}Z_p+C_{F,p}.
 \end{split}
 \tag{WMR.24}
$$
Then, on each physical patch,
$$
 |z_n(r)|\le Z_p n^{-23/6},\qquad
 |z_n'(r)|\le Z_{r,p}n^{-23/6}.
 \tag{WMR.25}
$$
To prove this, integrate (WMR.4) from the root backwards:
$z_n(r)=\int_r^{r_*}\mathcal E_z(r,s)F_{{\rm mean},n}(s)\,ds$.
The local part gives $Z_\ell$. For a strict point, split the integral
at $r_c$ and use the exact propagator composition at that point.
The result is bounded by the second line of (WMR.24). All lengths are
ordinary physical radial lengths, each used once. Since $G_s\ge1$,
$Z_s\ge Z_\ell$ also bounds the complete union. The third line follows
from the original differential equation and uses $A^{\rm abs}$,
not $A^\leftarrow$.

This estimate keeps the actual root initial value, both physical mean
coordinates, the full feedback, and all ordinary source terms. In the
alternative normal form $\widetilde z=z+\ell_f f$, the root term,
the waist term and the complete radial integral are still present.
There is no subtraction of their norm uppers.

A second exact option follows directly from the metric factor.
Writing $A^\leftarrow=\beta\,C^\leftarrow$ at the pointwise-inequality
level, a constant same-patch $C^\leftarrow$ gives
$$
 \mathcal E_z(r,s)\le
 \left(\frac{a_{\rm phys}(s)}{a_{\rm phys}(r)}\right)^{C^\leftarrow}.
 \tag{WMR.26}
$$
Across the cut the two actual ratios occur in their true order.
This is an optional new complete target if suitable old same-domain
radius-ratio records are separately admitted. Such records are not
silently inferred from the norm inputs listed below. The scalar
recipes (WMR.22)--(WMR.24) already close without this optional route.

## WMR6. Exact affine dependence of the physical first source

Put
$$
 T_k=(D_0-E)k+b_1,\qquad k=Jb_2.
 \tag{WMR.27}
$$
The complete first ordinary source can be written in either exact
form
$$
 \begin{split}
 g_1&=J\mathscr Q f-z'k-zT_k\\
    &=J\mathscr Q f+F_{\rm mean}k
                    -z(T_k+a_{\rm eff}k),\qquad g_2=0 .
 \end{split}
 \tag{WMR.28}
$$
These are the same original scalarization and mean equation. They
do not change the trial, introduce an independent column, or discard
a mean port.

For each patch read the old complete bounds $k_0,k_{\phi,0},k_{r,0}$
and $E_0$ from mean_kernel_p. Define the new direct coefficient
$$
 \mathfrak r_p
 =k_{r,0}+D_p k_{\phi,0}+E_0 k_0+(b_1)_0.
 \tag{WMR.29}
$$
Here $(b_1)_0$ is the saved complete physical $A_0$ bound. This is a
bound for $T_k$, not for the old $R_m=T_k+a_{\rm eff}k$. In particular,
it is constructed from its four positive terms and is not the
difference of the old $R_m$ upper and an $a_{\rm eff}k$ upper.

The old record $(Ik)_0$ bounds the complete primitive of $k$.
Since $T_k$ is odd and $I$ has its actual $L^2$ norm $1/4$, the new
complete mean-source bounds are
$$
 \begin{split}
 M_{c,p}^{\rm new}
     &=k_0 Z_{r,p}+\mathfrak r_p Z_p,\\
 M_{t,p}^{\rm new}
     &=(Ik)_0 Z_{r,p}+\tfrac14\mathfrak r_p Z_p .
 \end{split}
 \tag{WMR.30}
$$
The first measures the raw first source, and the second its physical
primitive. Their coefficient decay remains $n^{-23/6}$ with the
original reflected input normalization. The $k_r$ term contains the
full original inverse derivative and all one-sided coefficient
derivatives. No statement that $\beta_r$, $J_r$, $e_\kappa$ or the
background residual vanishes is used.

One may instead evaluate the second line of (WMR.28), using
$\mathfrak r_p+A_p^{\rm abs}k_0$ and the complete old $C_{F,p}$.
That is another whole bound for this same mean-source contribution.
Only complete candidates may be compared. The first line is useful
because its dependence on the complete $Z_p,Z_{r,p}$ is explicitly
linear.

The actual $z$ is continuous across the original interfaces, and
the current trial has the already proved continuous $k$ and height.
Thus the old true-jump graph is the same complete graph. It is read
unchanged, with all 3070 actual interface entries retained by the
original disjoint-subset interpretation. No artificial jump is
introduced at the estimation split $r_c$.

## WMR7. Reassemble the same complete negative receiver

The already successful negative_reception graph separates its
saved patch records into $B_{c,p},B_{t,p},T_{c,p},T_{t,p},M_{c,p},M_{t,p}$.
Only the last two depended on the old propagated-mean upper.
The four complete nonmean records in each patch are copied, as are
the old collar unions $B_c^\cup,T_c^\cup$, all power/radial factors,
the dyadic input factors, the three original receivers and both
complete true-jump sums.

For clarity put
$$
 M_c^{\cup,\rm new}=\max(M_{c,s}^{\rm new},M_{c,\ell}^{\rm new}),
 \quad N=388,\quad c_{\rm PW}=\frac{2333968743003}{10^{13}},
 \quad \ell_+=\frac1{200},\quad \ell_-=r_--c_{\rm PW}.
 \tag{WMR.31}
$$
Every non-rational power below denotes the unchanged saved record
of that complete factor. The new ordinary-source targets are
$$
 \begin{split}
 O_c^{\rm new}
 &=\sqrt2\,\ell_+^{1/4}
       (B_c^\cup+T_c^\cup N^{-5/6})
       +\sqrt{\ell_+}\,M_c^{\cup,\rm new}N^{-5/3},\\
 O_t^{\rm new}
 &=c_{\rm PW}\left[
       \ell_-^{-1/4}(B_{t,s}+T_{t,s}N^{-1/2})
                     +M_{t,s}^{\rm new}N^{-4/3}\right].
 \end{split}
 \tag{WMR.32}
$$
They are new complete expressions for the same ordinary-source
maps. The original PW cut has not moved to the strict/local
coefficient split.

Write $J_c,J_t$ for the unchanged two complete true-jump sums and
$\mathcal S_{1/3},\mathcal S_{2/3}$ for the unchanged input dyadic
square-sum records. The new complete received negative bound is
$$
 C_-^{\rm new}
 =3^{4/3}\left[
    (C_O O_c^{\rm new}+C_R J_c)\mathcal S_{1/3}
       +C_1(O_t^{\rm new}+J_t)\mathcal S_{2/3}\right].
 \tag{WMR.33}
$$
The prefactor $3^{4/3}$ is also read from its saved record.
All complete low-output leakage, physical frequencies, both evolving
mean coordinates, ordinary $dr$, the impulse units and the original
two source windows remain unchanged.

Formula (WMR.33) is evaluated directly from its complete terms.
The previous $C_-$ upper is retained as an old whole candidate and
is never used as a minuend. No N6 operator word, profile bound, jump,
source receiver, dyadic series or primitive target is recomputed.

## WMR8. The waist endpoint and the final two complete norms

The unchanged completed endpoint graph contains the first three
complete endpoint contributions:
$$
 C_{\rm sc},\qquad C_2,\qquad C_{\rm WT}.
$$
It also contains the original complete physical mean-column norm
$V_z$ and the free-map graph contains $\Xi_{23/6}$. Copy these
already computed scalar records. The exact physical mean column is
$$
 v_z=\mathfrak D_0(-u_w/m_w,1),\qquad
 \|v_z\|^2=n_g(0)^2
       \left(q_0+\frac{\|I(u_w/m_w)\|_2^2}{q_0}\right).
 \tag{WMR.34}
$$
Its $q_0$ term includes both stored physical mean coordinates.
The exact identity $J_wb_{2,w}=u_w/m_w$ is only a waist identity.
It does not eliminate the full radial $k$, $k_r$ or mean-source
process.

The new complete same-trial endpoint is
$$
 C_{\rm end}^{\rm new}
 =C_{\rm sc}+C_2+C_{\rm WT}+V_z Z_s\Xi_{23/6}.
 \tag{WMR.35}
$$
The original genuine root matrix, full $\beta_n$, first-cancellation
remainder, complete second waist normalizer, true finite complement
and actual gauge factors in the first three records are unchanged.
The saved $n_g(0)$ has already been included exactly once where
required; no new receiver factor is inserted here.

Let $L_{\rm rec}$ be the already saved complete ordered product
$(K_{H^{-1},L^2}/\sqrt2)K_{N_i,H^{-4/3}}$. Read it directly from
the successful final whole graph. With the same old complete
$C_{\rm alg},D_\infty,R_+,R_F$, define
$$
 \begin{split}
 C_*^{\rm new}
 &=C_{\rm alg}+L_{\rm rec}
          (R_++R_F+C_-^{\rm new}+C_{\rm end}^{\rm new}),\\
 C_{\infty,*}^{\rm new}
 &=D_\infty+L_{\rm rec}
          (R_++C_-^{\rm new}+C_{\rm end}^{\rm new}).
 \end{split}
 \tag{WMR.36}
$$
The second expression retains the exact WFR root factor and all
WCF finite factors in their original auxiliary border. It is not a
whole $C_{\rm alg}$ replacement. Both norms still concern the same
$X_{\rm fr}\to P\operatorname{Fix}R_a$ physical map with input
$H^{-4/3}$ and output normalized physical $L^2$.

Only final complete bounds for the identical operator and coordinate
realization may be compared with the previous successful complete
ones: the whole bound competes only with the old whole bound, and
the reduced bound only with the old reduced bound. These two different
operators are never compared to one another. A whole comparison must record the selected original candidate
and keep all candidates. No combination of entrywise minima from
different decompositions is authorized.

## WMR9. What a finite separation does and does not accomplish

The map from the full forcing to the one endpoint value $z(0)$ is
one scalar functional. Multiplication by the fixed vector $v_z$
therefore gives a genuine rank-one endpoint term. Its norm may be
paid by (WMR.35), or the exact endpoint functional and column can be
retained as a finite auxiliary factor in a separately qualified
border.

The full radial map
$$
 F\longmapsto z(r)
   =\int_r^{r_*}\mathcal E_z(r,s)F(s)\,ds
 \tag{WMR.37}
$$
is a Volterra operator on radial functions. Conjugating it by its
nonzero scalar integrating factor gives ordinary backward integration,
which has infinite rank on the full scalar $L^2$ interval.
The body source in (WMR.28) uses this whole radial function and its
derivative, not only $z(0)$. Thus the endpoint rank-one fact does not
make the entire mean completion finite.

The alternative exact identities
$$
 \begin{split}
 \mathcal E_z(r,s)
 &=\frac{a_{\rm phys}(r)}{a_{\rm phys}(s)}
       \sqrt{\frac{E_G(r)}{E_G(s)}}
       \exp\!\left(\int_s^r2\beta\mathcal H/D_J\right),\\
 &=\frac{m(r)}{m(s)}
       \exp\!\left(\int_s^r
            (2\beta\mathcal H/D_J-R_0/m)\right),\\
 R_0&=m'-\beta m(1-\Pi S)
 \end{split}
 \tag{WMR.38}
$$
remain valid. They do not prove $R_0=0$, $\mathcal H\ge0$ or a
contractive propagator. A future signed correlation or integrated
coercivity certificate may strengthen (WMR.19), but it must be a new
complete same-domain target. Existing unsigned norm records alone
do not supply those stronger conclusions.

All genuine physical mean matching equations, the parameter $\nu$,
the true 96 physical columns, their omitted-output constraints,
the infinite radial head and the remaining physical ports are retained.
No finite Schur inverse, incoming inverse, nonlinear background or
final surface is proved by these new norm recipes.

## WMR10. Typed read-only inputs and numerical obligations

For each patch $p$, the five complete scalar norms
$\beta_p,K_p,V_p,d_p,(b_1)_p$ and the angular qualification
are read from physical_coefficients_p.conclusion.complete_A0_jets.
For a named jet, group_upper[0] is its saved order-zero complete
$A_0$ upper. It dominates the required real supremum. The positive
$\eta_{p,-}$ is read from
same_angular_J_p.conclusion.new_complete_records.same_eta_positive_lower
using its lower endpoint. No geometric pointwise jet is relabelled
as a Wiener bound.

The sufficient primary new-coefficient recipe takes
$$
 M_p=V_p,\quad (U_p,\delta_p)\text{ from (WMR.15)},
$$
and then uses (WMR.10), (WMR.19), (WMR.22) and (WMR.24).
It needs neither a new $D_J$ computation nor a new value of $a_J$.
The old $J_0$ remains in its genuine source and derivative places;
it is only absent from this different, exactly derived feedback
estimate.

The rest of the typed read-only map is:

| Purpose | Complete saved field |
|---|---|
| $C_{F,p}$ | mean_N6_p.conclusion.new_complete_records.complete_reflected_mean_source_upper |
| $k_0,k_{\phi,0},k_{r,0}$ | mean_kernel_p.conclusion.new_complete_records.complete_k_L2_upper, complete_k_phi_L2_upper, complete_k_r_L2_upper |
| $E_0,(Ik)_0,\mathcal B_0$ | same object: complete_E_L2_upper, complete_I_k_L2_upper, complete_mean_base_upper |
| Unchanged nonmean $B,T$ | negative_reception.conclusion.complete_patch_B_T_M_records.p, only the four B_c/B_t/T_c/T_t entries |
| Unchanged collar $B,T$ | negative_reception.conclusion.complete_collar_patch_union_records, only complete_collar_B_union_upper and complete_collar_T_union_upper |
| Complete receiver factors | negative_reception.conclusion.copied_complete_original_receiver_records |
| Complete radial/power factors | negative_reception.conclusion.complete_power_and_radial_measure_records |
| Complete input factors | negative_reception.conclusion.complete_input_Bessel_prefactor_upper and complete_input_dyadic_square_sum_records |
| Complete jump sums | true_jumps.conclusion.new_complete_records.complete_collar_jump_sum_upper and complete_strict_jump_sum_upper |
| Three nonmean endpoints | complete_four_waist_endpoint_contributions.conclusion.complete_four_endpoint_records, the scattering, second_order and old_waist_normalizer entries |
| Mean endpoint vector | same endpoint conclusion: complete_new_constants.complete_physical_mean_endpoint_vector_upper |
| Mean input tail | complete_free_waist_Airy_and_Schur_map.conclusion.complete_tail_weights.new_complete_records.complete_Xi23_6_upper |
| Ordered final readout | complete_same_physical_whole_and_reduced_error.conclusion.complete_new_records.complete_left_readout_times_right_input_upper |
| Original complete final inputs | same whole conclusion: complete_original_records |

The new directed consumer must copy all consumed old record objects
unchanged, retain their full original run/input/scope qualifications,
and bind each new complete graph to those immutable inputs.
It must take the true lower endpoint for $\eta_-$ and upper endpoints
for every norm majorant. All new products, the two new scalar
exponentials, both complete patch means and all final sums must be
saved completely before a subsequent format gate. No old graph,
native archive, producer, scalar exponential or existing recorded
product is called again.

The required new targets are the two complete quotient/coefficient
graphs, the two-patch propagation graph, the affine mean-source
and complete negative assembly, the new endpoint sum, and the two
complete final bounds. Their exact serialization counts and byte
budgets belong to a later separately reviewed consumer contract.
No numerical improvement factor, smallness gate or high-cutoff
admission is claimed before that new execution.

## WMR11. Immutable evidence

The primary algebra was read in full in the following objects.
The original R77 phase symbols are kept distinct from the metric
coefficients used in P and N.

| Complete primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| R77 exact metric parity and curvature, equation (4) | ba843df645c734a714ef29a4d341fb0679832900 | 9207 | 0a7276239ea25ceb87ca386e48e7c9901a7503edf52baad1d3ba753b51ae1243 |
| P actual metric and polynomial system | 1b73111e5cf90876f1e593274b27cb1074915b85 | 11606 | 43ee65f22d64aed7d4f156647d0043e7626f2669b31c784a16c72169e6af8e35 |
| N same complete moving scalarization | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| JI exact scalar denominator and strict pointwise gap | 839fa641fe9ce3758ee69cfe3cb4299f59a3a239 | 11769 | 01e4a33be5d895ccbfc949310a86bf561c8dccdfe1c1eff973fa1298fcc91cf1 |
| WEJ complete physical mean, feedback and source recipes | da9d8461ca406a1c6f4b829a91147a860133567f | 59644 | 6b7644a978915550b5835b3492eda3bffde872b8e92f16c2db6c4538e405be8f |
| Complete support source, read as text only | d4f887d637a709331977ef24cd48d930ea396b40 | 73459 | c42b14e13c7357bb3aa60447ee8679592e0948fffe11f7ecdd846fc554bafdf4 |
| Complete negative-receiver source, read as text only | 3288b02946fc2c53d70505cfcbabd6a5c1f841eb | 53183 | b8332d68174c8ae524874cc293cc8e65793f570bf733726d80d2f4d60f9bcdb4 |

The primary paths are results/R133-supplement-polynomial-Codazzi-chart-and-complete-boundary.md,
results/R133-supplement-complete-moving-root-scalarization.md and
results/R133-supplement-complete-real-interval-angular-inverse-and-physical-mean.md
for P, N and JI. All paths in this note are relative to the existing topic.
The fixed blobs above also identify the complete objects without relying
on a mutable title.

The relevant first-attempt actual nodes are under
notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/.
Their completed mathematics remains valid although that attempt later
stopped at a missing phase-derivative metadata key. No failed status is
relabeled successful.

| Complete saved node | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| physical_coefficients_strict | 43482134ed758ba90c331cc598d8e04377009a24 | 15788 | 58d527567281fc3fcdefc4b70884f46e2e64a6cbc58b13fa9431bc4e03bdc6dc |
| physical_coefficients_local | 8e04fca88d61b2f38152302cac8527ab8326d5df | 15904 | ee16b343c4dff938c0d56ce29f906b55a4fff250ff68c98c49e47d138b4c614a |
| same_angular_J_strict | f6faddfa43ccb00617327e3740f922bc59ce382b | 5471 | a904a3df4e4d750327618c126362424c8bb8bda42a8fd09344c7742a5631d127 |
| same_angular_J_local | 37864cba216c25f951f4b98cf16192fd4100cc4b | 5048 | 484350c39e3dd0591dfb62412f044f90d957065d7a7cb2e3c51dc2a240e954c1 |
| mean_kernel_strict | 4bff00acace27f4d649354fcb88e8b292fbd24db | 8083 | f62aa75b1069004b67c1195ede586b4cad25f8198687c43ee33626e26735658f |
| mean_kernel_local | ff77ae845a0a31a66cb7d3634c6db0c343cbde29 | 8081 | 5d0651e87d62fbe14bd351b648ddacba3f590ed7506c68b90d0e7f2f324be3a3 |
| mean_N6_strict | 7ba8a5f33624148475fae9752ac28f121f00d718 | 28403 | 82302654a5a87c15e6d0155e368ebd25c12605819b716fcaf1348e599a31bdfc |
| mean_N6_local | 16f608b4331774ca51b75c2a98a360d869344092 | 27359 | ac5222bb6d2a9a2e25a01e9cd8bd7f3b2535a9f8773ca6c1f688110bb58d672b |
| mean_union | dece62e9a834852a36eac95cff83594974fea251 | 3560 | c7799f1c4eeea8ecdf5dd97f6d4a0257b41b376b2485e85c3b3938834f45fd44 |
| true_jumps | d7a106f0d3372ea5d2b02b84ca60cbe549ddedc3 | 5897 | 1e2272cb7d1071f87a9ed6f7153ed994153351c15cdd81f6859ac9ba1fb61bbd |
| negative_reception | 584cf91584915adc481ab2766d4b1be884bed9da | 8811 | 5d8284aa02ca278dbcb492bfdc1a7825fe7c56518ddac9de989128d8cdc8def1 |

The unique remaining-only continuation 43831678361/1 subsequently
completed the three missing graphs without reevaluating the old
23 graphs or any of the 39 saved partial records. Its completed
nodes are under
notes/global_genuine_waist_error_completion_ci/run-43831678361-1/graphs/.

| Complete continuation node | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| complete_free_waist_Airy_and_Schur_map | d2aa61e0dc1502181a9e86549e81311e8fdacdaf | 14394 | 5f48bdc934047c86ed2fd2d79cb94c593c619cffefb3ac52510fd3c4bfe4b413 |
| complete_four_waist_endpoint_contributions | 13b5b9809e2ba649511613eb5e58ef78f51908dd | 7974 | 7fbee7f580c01944e585f5a763ce5a87717db8c8f59ea789b48f850fe6a75df3 |
| complete_same_physical_whole_and_reduced_error | 2f46123a6c4d54676b2c82ac205ca1060b6df97e | 9098 | 6e9267dccb21d9d1421608a5f0f2e7c0ee77630660eac272ee3923ef2b8319d0 |

Those three complete bodies and SHA256 identities were independently
read and compared with their frozen schemas for this note. They have
52/8/15 saved records, comprising 30 new records, the original 39
partial records and six copied original final-input records.
Their nine gates, new source binding, complete dependency receipts,
selected-domain flags and retained physical obligations remain intact.

The actual old mean_union record still contains the whole bound
$[3.98964231158840781026607678090888767530227450256100662036635695527599910418
{\rm e}{+341224409}\mathbin{+/-}2.38{\rm e}{+341224333}]$.
Its large propagation factor was formed from the old complete
absolute coefficient; this note does not alter that successful
record. The saved strict mean forcing remains of order
$10^{393}$, and the saved complete nonmean N6/profile coefficients
also remain large. The new recipes therefore do not by themselves
assert a small final norm or a useful finite cutoff. They remove a
specific unnecessary angular-inverse norm from the mean propagation
estimate while retaining every other already completed contribution.
