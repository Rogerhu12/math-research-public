# R133 supplement: per-index strict flux and a complete physical-mean bound

2026-11-16, tail_connector.

**Proved here: a finite positive recipe for a new complete strict physical-mean bound. No new scientific value has been evaluated.** There are 52 new scalar targets in three natural conclusions. The recipe uses the same genuine trial and $n^{-23/6}$ mean-source unit as WMT. Successful weight kernels, angular bounds, local mean and receiver constants are read verbatim.

The new ingredient is a backwards demand calculation for the exact angular flux. Complete first forcing needs the leading amplitude only through total order seven and ordinary radial order two; no radial derivative of the first amplitude is needed. Each angular coefficient is bounded individually, without taking a maximum over unrelated radial derivatives. The physical equation is unchanged.

The successful WSM result remains a proved finite upper bound. Its nonmean remainder, jumps, positive/root terms, four-endpoint decomposition and both whole-operator candidates are preserved. This proof supplies no smallness inequality, signed finite inverse or final nonlinear conclusion.

## WSMF1. Same object and units

Use the selected original real member at fixed intrinsic parameter $\eta_0$, period $\pi/2$, ordinary radial measure and the original 3070 true interfaces. The strict interval is
$$
 0\le r\le r_c,\qquad r_c=\frac{76285779072683}{320000000000000}.
 \tag{WSMF.1}
$$
The original collar receiver retains its distinct cut $c_{\rm PW}=2333968743003/10^{13}$.

For $n=4|j|\ge N_0=388$, $\epsilon=\operatorname{sgn}j$ and $z_n=n^{-1}$, the same WUA trial is
$$
 f=P n^{7/6}{\cal U}_{n,\epsilon}^{\rm ext}(w),\qquad
 w=w_0+z_nw_1^{\rm ext}.
 \tag{WSMF.2}
$$
The physical mean $z_{\rm ph}$ has the original condition $z_{\rm ph}(r_*)=0$ at the true root. It is not $z_n$ and is not zero elsewhere. Both stored physical means and their density conversion remain present.

Let $t=-T>0$, $s=\sqrt t$, $x=X_\phi$, $y=T_\phi$ and
$$
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix},\qquad
 H=i\epsilon x\,Id+yK_T,\qquad D=\partial_r-d\partial_\phi .
 \tag{WSMF.3}
$$
The lower for $t$ is the saved cut lower with its proved strict-domain qualification. No strict reciprocal is extended to the root.

Use normalized angular measure and
$$
 [a]_{q,\infty}=\|\partial_\phi^q a\|_\infty/q!,\qquad
 [a]_{q,1}=\|\partial_\phi^q a\|_1/q!.
 \tag{WSMF.4}
$$
Vector and matrix norms are component and entry sums, so $Id$ has norm two. Physical Fourier-Wiener bounds remain distinct from geometric sup bounds. The primitive fee $1/4$ is applied only in an already qualified Fourier-Wiener or $L^2$ space.

## WSMF2. Complete flux and finite demand

The exact WMT identity fixes every term. Put
$$
 \begin{split}
 {\cal C}&=d\,Id-i\epsilon Q_fK_T,\\
 {\mathfrak h}&=q_r/q+4\beta\Pi S-4d_\phi,\qquad S=u^2+Kv^2,\\
 {\cal L}&=-{\mathfrak h}Id/2+
 \frac{Q_f}{4}\begin{pmatrix}x/T&-i\epsilon y\\i\epsilon y/T&-x/T\end{pmatrix},\\
 {\cal M}&=xE_{12}+i\epsilon yE_{11}.
 \end{split}
 \tag{WSMF.5}
$$
Here $u,v,K,\beta$ are physical background variables, not fold variables or $K_T$.

The full free forcing $(F_b,F_a)^t=-{\cal L}_0w_0$ includes the original $\vartheta H^{-1}H_D$ term. Retain
$$
 \binom{F_b^e}{F_a^e}=\binom{F_b}{F_a}+V_{\rm ext}w_0,\qquad
 q_e=\frac{Q_f}{2}
 \binom{xF_a^e+i\epsilon yF_b^e}
       {i\epsilon yF_a^e+(x/T)F_b^e}.
 \tag{WSMF.6}
$$
The extension $w_1^{\rm ext}=w_1+{\cal B}_{\rm ext}K_Tw_0$ includes its nonzero negative tail.

For the original real normalized weight $p_J=a_J/D_J$,
$$
 e=-\frac{2\beta m}{\eta}I(p_Ju),\qquad
 e_\kappa=-b_m e+
 2\beta mP\!\left[p_J\left(Kv-\frac{du}{\eta}\right)\right],
 \quad b_m=\beta(1-\Pi S),\quad m=\Pi v .
 \tag{WSMF.7}
$$
Both kernels have zero mean. The genuine derivative rules, $H{\cal C}=M_r$ and
$yE_{12}{\cal C}-T_rE_{12}=-Q_f{\cal M}$ imply
$$
 F_{\rm mean}=n^{7/6}\Pi{\cal U}^{\rm ext}
 \left[
 \{e_\kappa Id-\partial_\phi(e{\cal C})+e{\cal L}
             -z_neV_{\rm ext}Q_f{\cal M}\}w
             +z_ne q_e
 \right].
 \tag{WSMF.8}
$$
This is angular integration by parts on the entire product. It creates no radial endpoint or missing $e_r$ term and deletes no physical feedback.

Set
$$
 \begin{split}
 {\cal B}&=e_\kappa Id-\partial_\phi(e{\cal C})+e{\cal L},
 &{\cal D}&=eV_{\rm ext}Q_f{\cal M},\\
 A_0&={\cal B}w_0,
 &A_1&={\cal B}w_1^{\rm ext}-{\cal D}w_0+e q_e,
 &A_2&=-{\cal D}w_1^{\rm ext}.
 \end{split}
 \tag{WSMF.9}
$$
The full forcing is $n^{7/6}\Pi{\cal U}^{\rm ext}(A_0+z_nA_1+z_n^2A_2)$.

This sufficient demand table retains all predecessors; it is not claimed optimal.

| Node | Required ordinary derivatives | Reason |
|---|---|---|
| Saved kernels | $p_J$: angular $0..5$; $e$: angular $0..6$ | (7) and $\partial_\phi(e{\cal C})$ |
| New $e_\kappa$ | Angular $1..5$; degree zero is copied | Complete projected kernel |
| Drift $d$ | $(r^0,\phi^{0..7})$, $(r^1,\phi^{0..6})$ | Phase recurrence and full second-order forcing |
| Physical $u,v$ | $(r^0,\phi^{0..6})$, $(r^1,\phi^{0..5})$ | $d_\phi=-\beta PS$ and radial coefficient derivatives |
| Radial scalars | $\beta,K,\eta$ through one; $q$ through two; $\ell_0=2\beta\Pi S$ through one | Phase coefficients, $G_{rr}$, complete first forcing |
| Relative phases and $t/t_0$ | Total $\le7$, radial $\le2$ | Leading block |
| $w_0$ | $(r^0,\phi^{0..7})$, $(r^1,\phi^{0..6})$, $(r^2,\phi^{0..5})$ | Every term of $D^2w_0$ and lower-order terms |
| Full $F_a,F_b$ | Radial zero, angular $0..5$ | Both characteristic kernels and (6) |
| ${\cal C}$ | Angular $0..6$ | Derivative of the whole product |
| ${\cal L},{\cal M},H^{-1},T^{-1}$ | Angular $0..5$ | Matrix products and five inverse steps |
| $Q_f,T$ | Pure angular through six where needed | ${\cal C}$ and $y=T_\phi$ |
| Free cut, kernel and free $w_1$ | Angular $0..5$ | Fixed ordinary-$dr$ integral and old flow through five |
| $V_{\rm ext}(T),{\cal B}_{\rm ext}(T),w_1^{\rm ext}$ | Angular $0..5$ | All genuine-potential terms |
| Three $A_k$ and five inverse steps | $A_k$: angular $0..5$; terminal degrees $0..7$ | Complete terminal below |

No $w_{1,r}^{\rm ext}$, forcing radial derivative, leading radial third derivative, $\eta_{rr}$, $\beta_{rr}$ or $\gamma$ enters this mean demand. They remain wherever the other physical equations require them. In particular the already complete $T_k$ fee below retains its true radial and same-$J$ terms.

## WSMF3. Pure drift and five new kernel bounds

Let $Q_{i,j}^{\rm old}$ be the ordinary physical-background joint Fourier-Wiener upper in WGS's complete copies, $i=0,1$, $j=0,1,2,3$. The physical angular bandwidth is 384. Required ordinary normalized bounds are
$$
 U_{i,q},V_{i,q}\le
 \begin{cases}
 Q_{i,q}^{\rm old}/(i!\,q!),&q\le3,\\
 384^{q-3}Q_{i,3}^{\rm old}/(i!\,q!),&q>3.
 \end{cases}
 \tag{WSMF.10}
$$
A common joint upper may bound either component; the functions are not identified.

All products mean finite normalized convolutions. From $d=-\beta I P S$,
$$
 d_{i,q}\le(\beta S)_{i,q-1}/q\quad(q\ge1),\qquad
 d_{1,0}\le(\beta S)_{1,0}/4 .
 \tag{WSMF.11}
$$
The value $d_{0,0}$ is copied from the successful complete strict coefficient record. Formula (11) acts on the true full Fourier-Wiener background, not a geometric sup primitive.

Read the following nineteen WMT records verbatim:
$$
 {\mathsf p}_{0..5}^{\rm old},\qquad
 {\mathsf e}_{0..6}^{\rm old},\qquad
 U_{0..5}^{\rm old}=V_{0..5}^{\rm old}.
 \tag{WSMF.12}
$$
The last equality refers only to the common upper array.

With the same complete old bounds $b^+,\beta^+,M,K^+,\eta_-$ for
$|b_m|,|\beta|,|m|,|K|$ and the positive lower for $\eta$, define for $1\le q\le5$
$$
 {\mathsf k}_q^{\rm new}
 =b^+{\mathsf e}_q^{\rm old}
 +2\beta^+M
 \left\{{\mathsf p}^{\rm old}*
       \left(K^+V^{\rm old}+\eta_-^{-1}d*U^{\rm old}\right)\right\}_q .
 \tag{WSMF.13}
$$
Radial scalars have zero positive angular derivatives. Every term bounds the complete same $e_\kappa$ derivative.

At degree zero the expression and all inputs equal the successful WMT target:
$$
 {\mathsf k}_0^{\rm new}:={\mathsf k}_0^{\rm old}
 \quad\text{by exact record copy, without reevaluation.}
 \tag{WSMF.14}
$$
That record already paid the norm two of $P:L^1\to L^1$. Positive derivatives annihilate its constant output, explaining $2\beta^+M$ in (13), without deleting an actual mean equation.

No radial weight derivative, new exponential or new angular inverse is needed. The old six $e_\kappa$ bounds remain in the old WMT file. A fixed new branch is used below; only completed whole-operator candidates are compared.

## WSMF4. The finite per-index geometric packet

At each real base point freeze its actual $t_0=t(r_0,\phi_0)>0$. Define coefficients by
$$
 a_{i,q}^{[t_0]}=
 \frac{t_0^i}{i!\,q!}\partial_r^i\partial_\phi^q a(r_0,\phi_0).
 \tag{WSMF.15}
$$
The uniform bounds cover all bases in the strict interval. The factor $t_0$ is constant when differentiating. Products are finite bivariate convolutions. A radial derivative shifts $(i,q)$ to $(i+1,q)$ with factor $(i+1)/t_0$; an angular derivative shifts to $(i,q+1)$ with factor $q+1$. Bounding the former reciprocal by $t_-^{-1}$ is done after the exact shift. This is not repeated differentiation by $t\partial_r$.

Let $P_\sigma=\Phi_{\sigma,\phi}>0$ and $\omega=(\Phi_- -\Phi_+)/2$. For $1\le q\le7$ the successful WJR records supply
$$
 |\partial_\phi^qP_\sigma|/P_\sigma\le R_{P,q}^{\rm old},
 \qquad
 |\partial_\phi^q\omega|/\omega\le R_{\omega,q}^{\rm old}.
 \tag{WSMF.16}
$$
These are ordinary physical-angular ratios. Divide by $q!$ once. Their normalized zero coefficients are one because the denominator is the same actual positive base, not an interval upper subsequently differentiated.

The exact equations
$$
 \partial_rP_\sigma=\partial_\phi[(d+\sigma\eta q)P_\sigma],
 \qquad
 \partial_r\omega=d\omega_\phi-\eta q\,x,\qquad
 x=(P_++P_-)/2
 \tag{WSMF.17}
$$
determine the required radial coefficients triangularly. At radial degree two and angular degree five, the phase equation needs at most $d_{\phi^7}$ and $d_{r\phi^6}$, exactly covered by (10)--11.

For a common positive normalized phase majorant $\widehat P$, the explicit recurrence is
$$
 \widehat P_{i+1,q}
 =\frac{t_+(q+1)}{i+1}
 \sum_{a=0}^{i}\sum_{b=0}^{q+1}
 (|d|+|\eta q|)_{a,b}^{[t_0]}
       \widehat P_{i-a,q+1-b}.
 \tag{WSMF.18}
$$
The relative-gap recurrence uses the full drift convolution and the complete source in (17). Since
$t_0\eta_0q_0/\omega_0=3Q_f(r_0,\phi_0)/2$,
its source coefficient is bounded by
$3Q_f^0(\widehat\eta\,\widehat q\,x)/2$, divided by $i+1$.
This is the WSJ recurrence stopped at total seven and radial two, with every required $\eta_r,q_r,d_r$ term. The signed source is bounded only after the exact identity.

Put $\tau=t/t_0=(\omega/\omega_0)^{2/3}$. Finite binomial composition retains every coefficient. For exponent $a$, a complete positive rule for a relative series $1+v$ is
$1+\sum_{k=1}^{7}|\binom ak|v^k$, truncated only after the requested total degree. This is a finite Taylor identity at a positive real base, with no assumed complex nonvanishing or infinite-series convergence.

Here $\tau$ always means $t/t_0$, not $Q_fP_{-\sigma}$. The mean demand does not claim a second radial derivative of $Q_f$, which could require $\eta_{rr}$.

The exact two-phase inverse is
$$
 H^{-1}=
 \begin{pmatrix}-i\epsilon a&s b\\-s^{-1}b&-i\epsilon a\end{pmatrix},
 \qquad
 a=\frac{x}{P_+P_-},\quad b=\frac{\omega_\phi}{P_+P_-}.
 \tag{WSMF.19}
$$
Both $a,b$ are bounded by the complete two reciprocal-phase arrays. Its entry-sum majorant is $2p^{-1}+s p^{-1}+s^{-1}p^{-1}$, with every product derivative. The variable $s$ similarity is not a physical isometry.

For pure angular coefficients the exact factors reduce to
$$
 Q_f=Q_f^0\tau^{-1/2},\qquad
 \mu^{-1}=(\mu^0)^{-1}\tau
 (P_+/P_+^0)^{-1}(P_-/P_-^0)^{-1}.
 \tag{WSMF.20}
$$
The complete radial dependence of $\eta,q$ is retained in (17); their positive pure-angular derivatives are zero.

For the mixed leading packet use
$$
 G/G^0=\tau^{1/4}(q/q^0)^{-1/2}(E_G/E_G^0),
 \qquad E_{G,r}=-\ell_0E_G,\quad\ell_0=2\beta\Pi S .
 \tag{WSMF.21}
$$
The normalized radial coefficients of $E_G/E_G^0$ through two are bounded by
$1$, $t_+\ell_0^+$ and
$t_+^2((\ell_0^+)^2+\ell_{0,r}^+)/2$.
Only $q_{rr}$ and $\ell_{0,r}$ are needed. The exact identities
$a_0=G(P_+^2+P_-^2)/2$ and $b_0^{\rm amp}=-2i\epsilon Gxy$
supply both components through total seven and radial two. Half-sum and half-difference contributions are fully retained before positive bounds.

At an ordinary-output adapter, a saved complete bound for the identical function, norm, index and domain may be a safe fallback:
$$
 a_{i,q}^{\rm use}
 =\min\{t_-^{-i}\widehat a_{i,q},\
                 a_{i,q}^{\rm old,normalized}\}.
 \tag{WSMF.22}
$$
The old grouped coefficient is decoded with its original total-degree group and radial shape, not recomputed. It is not first multiplied by $t_+$ and divided by $t_-$. This minimum bounds a specified whole function or component; it does not select signed entries from different operators.

## WSMF5. Full first forcing and free transport

The positive bound for the diagonal part of the actual first-forcing operator retains
$$
 \partial_r^2a,\quad 2d\,\partial_r\partial_\phi a,\quad
 (d^2+\eta^2|K|)\partial_\phi^2a,\quad
 (|d_r|+|d\,d_\phi|)\partial_\phi a,\quad
 T_0^+D^+a,\quad V_0^+a .
 \tag{WSMF.23}
$$
The complete WUA/WSJ coefficient recipes include
$$
 \begin{split}
 t_Q^+&=|\eta_r|/\eta_-+|d_\phi|+|e_{\rm loc}|,\\
 T_0^+&=|\eta_r|/\eta_-+4|\beta|\,|\Pi S|+5|d_\phi|,\\
 r_Q^+&=D^+|\ell|+\eta^+|\partial_\phi e_{\rm loc}|
       +2|\beta|\eta^+|\partial_\phi u|\,|u|
       +|\ell|(|\eta_r|/\eta_-+|d_\phi|),\\
 \vartheta^+&=r_Q^+/\eta_-+2|\beta K|\,|u|\,|\partial_\phi u|,\\
 V_0^+&=t_Q^+|b_{\rm loc}|+D^+|b_{\rm loc}|
       +|K|\{|\ell|^2+4|\beta|\eta^+|u|\,|\partial_\phi u|\}.
 \end{split}
 \tag{WSMF.24}
$$
Here $D^+$ denotes the sum of the actual radial and drift-angular derivative bounds. It is not differentiation of an upper. The full physical quadratic coefficients $e_{\rm loc},b_{\rm loc},\ell$ are kept, and $b_{\rm loc}$ is distinct from $b_m$.

Multiply the two complete diagonal expressions (23) by $\mu^{-1}$ and retain the ordered cross terms
$\mu^{-1}\vartheta Q_fT b_0^{\rm amp}$ and
$\mu^{-1}\vartheta Q_f a_0$.
Their origin is the exact identity $H^{-1}H_D=-i\epsilon Q_fK_T$; the $\vartheta$ term is not set to zero.

At angular degree five, (23) needs precisely the three leading rows
$(r^2,\phi^5)$, $(r^1,\phi^6)$ and $(r^0,\phi^7)$.
The coefficient derivatives in (24) require background
$(r^1,\phi^{0..5})$, $(r^0,\phi^{0..6})$,
$\beta_r,K_r,\eta_r$. This proves the demand claim without generating a forcing radial derivative.

The actual free cut is
$$
 R_\sigma(r_c)=G(r_c)^{-1}P_\sigma(r_c)^{-2}
 [a_1(r_c)+i\epsilon\sigma s(r_c)b_1(r_c)] .
 \tag{WSMF.25}
$$
Read the old individual free $a_1,b_1$ angular records through three; for four and five read the old complete two-component bound, which bounds either component, and divide by the factorial once. No free-amplitude degree above six is needed.

The cut inverse-$G$ derivatives use the saved full inverse bound on the original $3/128$ holomorphic strip. The finite real reciprocal of $P_\sigma^2$ uses cut phase derivatives through six and the true cut phase lower. The square-root chain uses cut $t$ derivatives through four and the successful WDG fifth derivative. No real lower is silently extended to a complex strip or exchanged for an unrelated lower.

The complete free characteristic kernel is
$$
 {\cal K}_\sigma=\frac{Q_fP_{-\sigma}}{2G P_\sigma^2}
              (F_a-i\epsilon\sigma F_b/s).
 \tag{WSMF.26}
$$
Bound it through angular five. Its ordinary-$dr$ representation retains the nonzero cut trace:
$$
 R_\sigma(r,\phi)=R_\sigma(r_c,\chi_{r_c\leftarrow r}(\phi))
 -\int_r^{r_c}{\cal K}_\sigma(a,\chi_{a\leftarrow r}(\phi))\,da .
 \tag{WSMF.27}
$$
Use successful WBF flow bounds through five for all shorter intervals, both branches and orientations. Every ordinary Bell-polynomial term is retained in each composition. The integral pays the complete composed-kernel bound times the true strict length. No new ray integration or moving-limit derivative is generated.

Recover both free components from $v_{1,\sigma}=G P_\sigma^2R_\sigma$ by the actual half-sum and half-difference, then add the complete ${\cal B}_{\rm ext}K_Tw_0$. Read the successful ordinary potential derivatives $0..5$ and apply the finite chain rule to the new angular $T$ coefficients. The C64 cutoff and nonzero $\mathcal B_{\rm ext}$ tail remain complete and are not reevaluated.

## WSMF6. The eighteen complete flux amplitudes

For normalized arrays write $(a*b)_q=\sum_{i=0}^qa_i b_{q-i}$. Let $R_q$ bound derivatives of $1/T$, using the saved positive $t_-$ and complete positive reciprocal recurrence. The complete scalar in (5) is bounded by
$$
 h_0=q_1^+/q_-+4\beta^++4b^++4d_1,\qquad
 h_q=4(q+1)d_{q+1}\quad(q\ge1),
 \tag{WSMF.28}
$$
because $\beta\Pi S=\beta-b_m$ and the other two terms are radial.

With the complete arrays of WSMF4--5, use
$$
 \begin{split}
 C_q&=2d_q+\{Q*(t+1)\}_q,\\
 L_q&=h_q+\tfrac14\{Q*(2x*R+y+y*R)\}_q,\qquad M_q=x_q+y_q,\\
 q_q^e&=\tfrac12\{Q*[(x+y)*F_a^e+(y+x*R)*F_b^e]\}_q,\\
 B_q&=2{\mathsf k}_q+(q+1)({\mathsf e}*C)_{q+1}
                  +({\mathsf e}*L)_q,\\
 D_q&=({\mathsf e}*V*Q*M)_q,\qquad Q_q^e=({\mathsf e}*q^e)_q .
 \end{split}
 \tag{WSMF.29}
$$
Here $1$ means the scalar coefficient array with only degree zero equal to one. All arrays on the right are complete sup or $L^1$ arrays in their declared positions, not bare point values. The entry-sum factor two for each identity matrix is included. The potential additions in (6) enter both $F_a^e$ and $F_b^e$.

Put $W_0=|a_0|+|b_0^{\rm amp}|$, $W_1=|a_1^{\rm ext}|+|b_1^{\rm ext}|$ at the array level. For every $0\le q\le5$ retain
$$
 {\cal A}_{q,0}=(B*W_0)_q,\qquad
 {\cal A}_{q,1}=(B*W_1)_q+(D*W_0)_q+Q_q^e,\qquad
 {\cal A}_{q,2}=(D*W_1)_q .
 \tag{WSMF.30}
$$
These eighteen records bound the complete three amplitudes of (9), including the full angular derivative, both potential terms and the original projection contribution.

## WSMF7. Five exact mean steps and every terminal degree

Let $z=z_n$ and $c=V_{\rm ext}y$. The genuine angular rule uses
${\cal A}_n=\partial_\phi-zcE_{12}$. Set
$$
 v_0=H^{-1}A,\qquad v_{\ell+1}=-H^{-1}{\cal A}_n v_\ell
       \quad(0\le\ell\le3),\qquad A=A_0+zA_1+z^2A_2 .
 \tag{WSMF.31}
$$
Periodicity in the genuine derivative identity gives the complete fifth terminal:
$$
 \Pi{\cal U}^{\rm ext}(A)=
    -n^{-5}\Pi{\cal U}^{\rm ext}({\cal A}_n v_4).
 \tag{WSMF.32}
$$
The sign is immaterial only when taking the final absolute bound; no intermediate term is removed.

A complete finite positive implementation is
$$
 \begin{split}
 V^{(0)}_{q,k}
   &=\sum_{i=0}^q H_i{\cal A}_{q-i,k},
       &&0\le q\le5,\quad0\le k\le2,\\
 D^{(\ell)}_{q,k}
   &=(q+1)V^{(\ell)}_{q+1,k}
        +\sum_{i=0}^q c_iV^{(\ell)}_{q-i,k-1},\\
 V^{(\ell+1)}_{q,k}
   &=\sum_{i=0}^q H_iD^{(\ell)}_{q-i,k},
       &&0\le\ell\le3,\quad
         0\le q\le4-\ell,\quad0\le k\le3+\ell .
 \end{split}
 \tag{WSMF.33}
$$
Missing negative polynomial degrees are exact zero; no retained degree is omitted. The complete terminal bounds are
$$
 {\cal T}_k=V^{(4)}_{1,k}+c_0V^{(4)}_{0,k-1},
       \qquad 0\le k\le7.
 \tag{WSMF.34}
$$
This retains the full dependence on $z$, not only its first few terms.

Read the old single-reference pointwise profile upper $P_*$. Both original input signs are paid exactly as in WMT:
$$
 C_F^{\rm new}=2P_*\sum_{k=0}^7 N_0^{-k}{\cal T}_k,
 \qquad
 |F_{{\rm mean},n}|\le C_F^{\rm new}n^{-23/6}.
 \tag{WSMF.35}
$$
The exponent is $7/6-5=-23/6$. The old complete profile and both genuine reference roles are unchanged. No full signed operator estimate is inferred from a single-reference norm without the displayed assembly factor.

All finite inverse levels in (33) are computed completely as private intermediates in the same child. The public conclusion saves the eighteen full amplitudes, all eight terminal coefficients and their whole sum. Private mixed arrays are not exported as new certificates, but a successful public target is never recomputed.

## WSMF8. Same physical mean, both patches and four endpoints

All bounds in this section keep the unit $n^{-23/6}$. Read the old complete local mean $Z_l$, local raw mean-source bound $M_l$, strict backward factor $G_s$, absolute strict mean coefficient $A_s$, and $k_0,I_k,T_k$ fees from the successful WMT receipt. They refer to the same true root initial condition and complete physical feedback.

The new strict bounds are
$$
 \begin{split}
 Z_s&=G_s(r_c C_F^{\rm new}+Z_l),\\
 Z_s'&=A_s Z_s+C_F^{\rm new},\\
 M_s&=k_0Z_s'+T_kZ_s,\\
 \widetilde M_s&=I_kZ_s'+\tfrac14T_kZ_s,\qquad
 M_c=\max(M_l,M_s).
 \end{split}
 \tag{WSMF.36}
$$
The full source identity is $g_{\rm mean}=-kz_{{\rm ph},r}-z_{\rm ph}{\mathscr T}_k$. Its norm bound uses both terms in (36). No $k_r$, $J_r$, background feedback or original $R_0$ contribution is declared zero. They are paid by the complete old $T_k$ and other original qualifications. The old exponential is read, not recomputed.

Only the mean part of the waist endpoint changes:
$$
 E_{\rm mean}=V_z^{\rm old}\,\Xi_{23/6}^{\rm old}\,Z_s,\qquad
 E_{\rm waist}=E_{\rm scatter}^{\rm old}
             +E_{\rm second}^{\rm old}
             +E_{\rm WT}^{\rm old}+E_{\rm mean}.
 \tag{WSMF.37}
$$
The full old $V_z$ norm includes both physical density means and its $q$ contribution. All normalizers occur in their original places, once. No positive root correction, input diagonal or second-reference term is omitted.

For orientation only, the saved nonmean scattering endpoint is about $5.01187\,10^{295}$ and the saved complete second-order endpoint about $1.21480\,10^{289}$. These are read values, not newly evaluated quantities. They remain fully charged in (37), even if the new mean becomes much smaller. Improving those independent endpoints would be a separate complete same-normalization target.

## WSMF9. Current nonmean provider and complete error reassembly

The nonmean provider is a complete successful receipt for the same trial, operator and domain. The successful WSM receiver is already available. If the complete WRP receiver has succeeded when the numerical manifest is frozen, its full improved nonmean bounds and unchanged complete terminal are used instead. This is a choice of a complete admitted predecessor, not a new mathematical gate or an incomplete candidate. The manifest must fix one actual immutable provider.

Read its complete collar retained bound $B_c$, strict primitive retained bound $B_t$, complete terminal dyadic contribution $N_t$, original complete jumps $J_c,J_s$, both dyadic sums and Bessel factor. Its terminal is unchanged by the present mean replacement, so it is copied without recomputation. Both all-signed output scope and the final same-parity angular inverse remain those of the provider.

With the original ordinary radial lengths, form
$$
 \begin{split}
 S_c={}&\sqrt2\,\ell_+^{1/4}B_c
       +\sqrt{\ell_+}\,M_c N_0^{-5/3},\\
 S_s={}&c_{\rm PW}
       [\ell_-^{-1/4}B_t+\widetilde M_sN_0^{-4/3}],\\
 R_c={}&C_O S_c+C_R J_c,\qquad
 R_s=C_1(S_s+J_s),\\
 N_c={}&R_c\,{\cal S}_{1/3},\qquad
 N_s=R_s\,{\cal S}_{2/3},\\
 C_{\rm neg}^{\rm new}
   ={}&C_{\rm Bes}(N_c+N_s+N_t^{\rm old}).
 \end{split}
 \tag{WSMF.38}
$$
Every displayed square root, power, dyadic sum and receiver constant already has a complete saved record and is read. This section does not reevaluate any of those old scalar targets. The new seven records are $S_c,S_s,R_c,R_s,N_c,N_s,C_{\rm neg}^{\rm new}$.

The collar source is received in the original ordinary-$L^2(dr)$ first-source $H^{-2/3}$ window. True jumps retain the original mixed $H^{-2/3}\oplus H^{-1}$ interface window and the exact second-row zero qualification. The strict primitive source uses the original $C_1$ window. All 3070 true interfaces and both-sided states remain in the old whole jump records. No length factor multiplies a jump.

Finally retain the original two distinct operator realizations:
$$
 \begin{split}
 S_{\rm nr}&=R_+^{\rm old}+C_{\rm neg}^{\rm new}+E_{\rm waist},\\
 S_{\rm all}&=S_{\rm nr}+R_F^{\rm old},\\
 R_{\rm whole}&=L_{\rm rec}^{\rm old}S_{\rm all},&
 C_{\rm whole}^{\rm new}&=C_{\rm alg}^{\rm old}+R_{\rm whole},\\
 R_{\rm reduced}&=L_{\rm rec}^{\rm old}S_{\rm nr},&
 C_{\rm reduced}^{\rm new}&=D_\infty^{\rm old}+R_{\rm reduced}.
 \end{split}
 \tag{WSMF.39}
$$
These are six complete new records. The root finite factor is not deleted from the whole realization. $D_\infty$ is not relabeled as $C_{\rm alg}$. The originally separated WCF/FJ and physical mean rows, $\Theta$, $\nu$, radial-head functions and all independent compatibility remain in their actual equations.

Compare a completed new whole bound only with the chosen provider's current complete whole bound, and separately compare the two complete reduced bounds. Store both candidates and their exact record paths. The old candidate wins equality. No saved upper is subtracted to estimate a missing term, and no part of one decomposition is combined with a different trial.

## WSMF10. Exact 52-target boundary

The three natural new conclusions are:

| Ordered conclusion | Complete new records | Count |
|---|---|---:|
| strict_per_index_flux_mean | Five full $e_\kappa$ angular bounds (13), eighteen full amplitudes (30), all eight terminal coefficients (34), whole $C_F$ (35) | 32 |
| complete_physical_mean_and_four_waist_endpoints | $Z_s,Z_s',M_s,\widetilde M_s,M_c,E_{\rm mean},E_{\rm waist}$ | 7 |
| complete_current_negative_and_whole_receiver | Seven records in (38), six in (39) | 13 |
| **Total** | **All complete new scalar targets** | **52** |

The complete zero-degree $e_\kappa$ is an old copy, not a 53rd calculation. The thirteen old $p/e$ records, six common background records, all original local/propagator/same-$J$ fees, fixed potential derivatives, WBF83, WJR56, WDG80, WMT195, WRT42, WSM152 and any completed WRP40 target remain frozen.

The mixed and transport arrays are finite private arithmetic needed to define this new mean functional. No old complete producer is imported or called; no successful old public target is regenerated. Only the reduced demand in WSMF2 is formed, not the original large private WSM packet or its public profile/N6 graphs.

Each new public scalar is inserted into its complete natural conclusion, checkpointed with its ordered path, made durable and read back before a downstream computation uses its directed endpoint. A failure preserves every completed target and the full current prefix, original scopes and diagnostic identity. It never authorizes an automatic replay of completed targets. Temporary finite arrays stay inside the scientific child; they are not split into new certificate files to evade a size limit.

Bounds, domains and reference objects must be typed before numerical execution. All old scalar objects preserve their exact strings and types. Every consumed complete qualification object retains its non-ball leaves and array positions, with original file bytes/SHA and source/run/manifest bindings. The original failed parent attempts remain labeled failed even when completed child graphs are reused.

The single-child input and output schemas and escaped-diagnostic budget are to be sealed from the concrete source, not inferred from this proof's record count. This proof performs no scientific Python, Arb, interval arithmetic, old target evaluation, ray integration or numerical experiment.

## WSMF11. Concrete existing input paths

All paths below are under topics/visible-flex-exact-nearby. The following complete current objects supply the old inputs. The optional future current provider is not assigned a prospective pin or called successful here.

| Role | Complete path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| WGS main | notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |
| WGS original copies | notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json | d6d13860e322d82ce354c8c0d0eb0f279ca63b3c | 31632 | 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66 |
| WBF absolute flow | notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/actual-scientific-conclusion.json | df5ea6fff610d70ad98fbebc9dd004d24388ce86 | 59417 | 87621adee76080dbbc14abdd7f8e5dce5d3e2742ba299fc941d13ff40f4410c0 |
| WJR relative phases and gap | notes/relative_flow_Jacobian_ci/run-43873739440-1/actual-scientific-conclusion.json | 80499e42f643e607db47c973b54f2243629a05e8 | 69002 | 806fbeaaab33ddff424fcfe70e40f83f46d1f85e089f9f01f941ed38ee249660 |
| WDG cut fifth derivative | notes/positive_drift_relative_omega_ci/run-43865837250-1/actual-scientific-conclusion.json | 67c7070e6678223b5de63635d4b18f110500a742 | 47714 | 04b757433390715acd5e2bca3cd29afef0ccf3e3cea35d5855a96eb28bf89395 |
| Complete potential extension | notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/extension_scalars.json | c5d9166b914a17136c5058b3d213afc4dffad5c0 | 12958 | 5816db201af6f0da0f7412c1a1fe0f1521d5425debf37693ab652f152e7fec00 |
| WMT weight, mean, endpoint records | notes/strict_flux_mean_forcing_ci/run-43856579962-1/actual-scientific-conclusion.json | edd66cdbe7a438569524ba2614d3822f61de5c81 | 90421 | c6680025917247e7bec958851d5ee85fc3c3750b059372a87ec568cd9d8acbd4 |
| Current WSM index | notes/strict_scaled_mixed_complete_ci/run-43877268949-1/actual-scientific-conclusion.json | 7caabc2c0ca0953a3fe8d4c6ae25116c2ee09220 | 30834 | 3cb8fa2a506df28e634564a97aa124cb10aeb474a4daf02d7c7d62ac422d5172 |
| Current WSM complete receiver | notes/strict_scaled_mixed_complete_ci/run-43877268949-1/graphs/strict_complete_whole_receiver.json | 15eb048bf37a6bcc28aeaa6d745a026bdbdd5a62 | 14230 | 2413d02a10b9e465212970a5cdeef41ef9091854f496921fefa528cea6851983 |

The exact consumed mathematical ports are:

- WMT: complete_new_graphs.complete_normalized_weight_L1_kernels.new_records.p_L1_upper[0..5], e_L1_upper[0..6], e_kappa_L1_upper[0] and pure_angular_background_pair_upper[0..5].
- WMT: copied_original_scalar_records.strict_base, strict_beta, strict_V, strict_Kabs, strict_eta_lower, local_mean, local_raw_mean_source, strict_backward_factor, strict_absolute_coefficient, strict_k0, strict_Ik, strict_Tk, point_profile, endpoint_Vz, Xi23_6, endpoint_scattering, endpoint_second_order and endpoint_WT. The eta field is read as a lower. Other lower ports retain their own WGS/cut role.
- WGS original copies: complete original ordinary Q/radial records and copied_original_stage_records.free_components, fold.Gi and the saved cut normalization; the original component-versus-pair meaning is preserved.
- WGS main: complete_higher_flow_and_cut_conclusion.cut_phase_lower and cut_phase_orders_5_through_15, original strict lower/point records, and same-function grouped fallbacks in their exact shape and norm.
- WBF: copied_original_scalar_records.flow_1 and phase_1; complete_new_graphs.complete_new_sharp_flow_conclusion.new_records.ordinary_flow_orders_2_through_15 supplies only orders two through five here.
- WJR: complete_new_graphs.complete_new_positive_phase_average_ratio_conclusion.new_records.ordinary_common_positive_phase_and_average_ratios_1_through_14[0..6] and complete_new_graphs.complete_new_relative_omega_conclusion.new_records.complete_strict_relative_omega_angular_orders_1_through_14[0..6].
- WDG: complete_new_graphs.complete_new_cut_T_high_angular_conclusion.new_records.ordinary_cut_T_orders_5_through_14[0], copied as the complete ordinary fifth cut derivative.
- The complete potential node: conclusion.Vext_derivatives[0..5] and conclusion.complete_B_derivatives[0..5], with Bext_negative_tail_retained and the full original domain qualification.
- The WSM provider: conclusion.new_records.same_inverse_and_union.complete_collar_B_union_upper and strict_B_t_upper; conclusion.new_records.new_negative_receiver.complete_terminal_dyadic_contribution_upper; its complete copied receiver/jump records and its two whole_candidate_choices. A later successful provider must map these same typed complete objects explicitly, not identify them by a similar field name.

The original WGS scalar predecessors are copied_original_scalar_records.Q_0_0 through Q_0_3 and Q_1_0 through Q_1_3; beta_0, beta_1, K_0, K_1, q_0, q_1, q_2, eta_lower, q_lower, t_cut_lower, t_cut_upper, cut_t_1 through cut_t_4, cut_phase_1 through cut_phase_4, and free_old_0_4/free_old_0_5. The pure radial eta value and derivative are read from main.complete_strict_coefficient_conclusion.new_jets.eta.group_upper[0..1] under its saved pure-radial qualification. Main.complete_strict_leading_conclusion.complete_G_upper and complete_G_lower, complete_strict_geometry_conclusion.complete_jets.Q.group_upper[0] and mu_inverse.group_upper[0], and complete_higher_flow_and_cut_conclusion.strict_phase_lower supply their original same-domain roles. The complete original stage gives free_components.a1/b1["0"][0..3] and fold.Gi. Every field is validated against its full immutable source before use. No missing quantity may be manufactured by subtracting a saved upper.

## WSMF12. Primary proof chain and limits

The exact flux and complete mean identity are WMT, blob c8049ef93eca8f84f135ab4338d6485081fb8424, 31256 bytes, SHA256 51eb08d0b110b8a5b171538c3be023efb94df587fdab880ebddac518665f73ce. Its prior normalized-weight identities are WMF, blob 2c4a1789195a1ea400ef7c547b319ea3f4f7329f, 15111 bytes, SHA256 14900631ba2d793977336fd5f7e8870e4313cbda50a8a8c3e02fa11b53054356.

The scaled derivative and exact fold inverse proof is [WSJ](R133-supplement-scaled-strict-mixed-jets-and-exact-fold-inverses.md), blob 10c6e4220377b772692095347f096e5d897afc5e, 31568 bytes, SHA256 217cdff81516dd827122987ba6abe9a2cdacb6597d01fe9b4ee58a47faa8960d. The complete nonzero cut construction is [WCPR](R133-supplement-complete-cut-initialization-and-positive-profile-budget-reuse.md), blob da15190045b2cb05cffdfd410ab91fc9e5673286, 23905 bytes, SHA256 642e6fd207af3c632ee616eadbfe9ed15797e2df5baf8f6aff050984ac84a1ad.

The same full two-patch propagation is WMR, blob a7b23dea9a96dfab74475d382ca2d1df8edd5b8e, 31643 bytes, SHA256 550866c05d9a07d3e4b037e5840a4f75b66a7f3a9304c5cd0d52e4f2b7e729a6. The independent unexecuted local candidate remains [WML](R133-supplement-local-normalized-weight-and-complete-six-step-mean-source.md), blob 04827463ed6c8f81bcd54f278c004bcae668f7d5, 31888 bytes, SHA256 a67961a5cbf7bf6ec759a238c11f54f98fd131d0d6e0b8cf4fe682052b6469a6. This strict recipe neither executes nor replaces that local target.

The current successful finite bound is [WSMA](R133-supplement-actual-strict-scaled-mixed-profile-and-complete-waist-bound.md), final blob d686817cb87067788b658ace16218f7ada1d68cc, 36418 bytes, SHA256 dc566db379d0ad9bcc01e4f4f1ecc6395c907c0944281169e9761cc42cfce31c.

The complete per-index source was read as text only: scripts/fourfold_codazzi_strict_scaled_mixed_profile_math.py, blob c19a56d9ff82125a8899a9f0bc384aa262e474cb, 77499 bytes, SHA256 7ce81b0bc71cd39a1bec6a114965ce0e08e14f171adfc6d75bd113545377a7ec. Its exact formulas, rather than its completed producer calls, identify the finite private predecessor arithmetic used here.

Newton independently checked the full forcing demand $(r^0,\phi^7),(r^1,\phi^6),(r^2,\phi^5)$, the phase recurrence's $d_{\phi^7}$ and $d_{r\phi^6}$ predecessors, and the distinction between $t/t_0$ and an unneeded radial-two $Q_f$ packet. Phase independently checked the pure-angular $e_\kappa$ formula, old thirteen kernel records, degree-zero copy and the need for $e_6$ in the full flux. These are symbolic checks, not evaluations of the new 52 targets.

The next independent bottlenecks include the complete scattering and second-order waist endpoint constants, and any signed finite/head inverse still required by the original problem. They cannot be reduced by subtracting a mean fee from an old upper. The present theorem changes only a fully specified complete mean-bound candidate and its complete received whole bound.
