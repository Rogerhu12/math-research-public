# R133 supplement: exact drift cancellation in the complete normalized mean flux

2026-11-16, tail_connector.

**Proved here: an exact matrix identity and a finite positive recipe for a different complete strict mean-bound candidate. No new scalar has been evaluated.** The identity combines the normalized weight kernel, the full transport divergence and the full transport matrix before taking an absolute bound. Every explicit drift term in that matrix cancels. The scalar produced by the angular projection remains present.

The WSMF52 first execution has completed successfully; its contract and all 52 saved targets remain unchanged. The new candidate has 47 prospective scalar targets in three complete conclusions: 27 flux/terminal/source records, seven physical-mean/endpoint records, and thirteen negative-receiver/whole-operator records. The five new kernel targets of WSMF are not reevaluated or needed by this candidate. The same physical equation, two stored means, true root initial condition and all original receivers remain in force.

## WMC1. Scope and the exact starting identity

Use the same selected real member, physical period $\pi/2$, normalized angular measure, ordinary radial measure, physical frequencies $n=4|j|\ge N_0=388$, and original 3070 interfaces as WMT and WSMF. The strict interval is $0\le r\le r_c$, with
$$
 r_c=\frac{76285779072683}{320000000000000},
 \qquad c_{\rm PW}=\frac{2333968743003}{10^{13}}.
 \tag{WMC.1}
$$
The genuine physical mean $z_{\rm ph}$ still satisfies $z_{\rm ph}(r_*)=0$ at the true root. The root bracket endpoint $r_+$ is only an upper length bound. No strict reciprocal of $T$ is used at the root.

Write $t=-T>0$, $x=X_\phi$, $y=T_\phi$, $\epsilon=\operatorname{sgn}j$, $z=n^{-1}$ and
$$
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix},
 \qquad
 {\cal C}=d\,Id-i\epsilon QK_T,
 \qquad
 {\cal M}=xE_{12}+i\epsilon yE_{11},
 \quad Q=Q_f .
 \tag{WMC.2}
$$
The physical background variables $u,v,K,\beta,\eta$ are distinct from the fold variables and the matrix $K_T$. In particular $S=u^2+Kv^2$, $m=\Pi v$ and $b_m=\beta(1-\Pi S)$.

The real normalized angular weight is $p=a_J/D_J$. The complete earlier normalized-weight theorem gives
$$
 \Pi e=0,\qquad
 e=-\frac{2\beta m}{\eta}I(pu),\qquad
 e_\phi=-\frac{2\beta m}{\eta}pu,\qquad
 e_\kappa=-b_m e+2\beta mP\left[p\left(Kv-\frac{du}{\eta}\right)\right].
 \tag{WMC.3}
$$
Here $P=Id-\Pi$ and $\eta$ has its original positive same-domain lower. These are exact functions; $p$ and $e$ are not replaced by upper-bound functions. No division by $\beta$ or $m$ is used in this proof.

Retain the complete transport matrix
$$
 {\cal L}=-\frac{\mathfrak h}{2}Id+
 \frac Q4
 \begin{pmatrix}x/T&-i\epsilon y\\i\epsilon y/T&-x/T\end{pmatrix},
 \qquad
 \mathfrak h=q_r/q+4\beta\Pi S-4d_\phi .
 \tag{WMC.4}
$$
The original physical identities used below are
$$
 d_\phi=-\beta(S-\Pi S),\qquad
 Q_\phi=-\frac{Qy}{2T},\qquad
 (K_T)_\phi=yE_{12}.
 \tag{WMC.5}
$$
The second identity follows from the exact pure-angular factor $Q=Q^0(t/t_0)^{-1/2}$ and $t_\phi=-y$. The radial factors in $Q$ have zero angular derivatives. Formula (5) makes no claim that those factors have zero radial derivatives.

Let $w=w_0+z w_1^e$ be the same complete genuine first trial, with
$$
 w_1^e=w_1+{\cal B}_{\rm ext}K_Tw_0,\qquad
 \binom{F_b^e}{F_a^e}=\binom{F_b}{F_a}+V_{\rm ext}w_0,
 \qquad
 q_e=\frac Q2
 \binom{xF_a^e+i\epsilon yF_b^e}
       {i\epsilon yF_a^e+(x/T)F_b^e}.
 \tag{WMC.6}
$$
The free forcing contains the original complete $\vartheta$ term. The extension retains its nonzero negative tail. WMT's exact angular-flux identity is
$$
 F_{{\rm mean},n}
 =n^{7/6}\Pi{\cal U}_{n,\epsilon}^{\rm ext}
 \left[\left({\cal B}-z{\cal D}\right)w+z e q_e\right],
 \quad
 {\cal B}=e_\kappa Id-\partial_\phi(e{\cal C})+e{\cal L},
 \quad
 {\cal D}=eV_{\rm ext}Q{\cal M}.
 \tag{WMC.7}
$$
It is this complete $\mathcal B$ that will be rewritten. No term of the forcing or physical feedback is removed.

## WMC2. Exact cancellation and the surviving scalar

Define the genuine angular scalar
$$
 c(r)=2\beta m\Pi\left[p\left(Kv-\frac{du}{\eta}\right)\right].
 \tag{WMC.8}
$$
It is constant in $\phi$, but it is not asserted to vanish or to be constant in $r$.

First, the $d e_\phi$ contribution cancels the unprojected $pdu$ contribution:
$$
 e_\kappa-d e_\phi
 =-b_m e+2\beta m pKv-c.
 \tag{WMC.9}
$$
The remaining scalar coefficients of $e$ satisfy the exact equality
$$
 -b_m-d_\phi-\mathfrak h/2
 =-\frac{q_r}{2q}-\beta(1+\Pi S)+d_\phi
 =-\frac{q_r}{2q}-\beta(1+S).
 \tag{WMC.10}
$$
No upper bound has been subtracted in these two identities.

The angular derivative of the matrix part is retained completely:
$$
 i\epsilon eQ_\phi K_T+i\epsilon eQ(K_T)_\phi
 =\frac{eQ}{2}
 \begin{pmatrix}0&i\epsilon y\\-i\epsilon y/T&0\end{pmatrix}.
 \tag{WMC.11}
$$
Adding the traceless part of $e{\cal L}$ gives the matrix
$$
 {\cal W}=\begin{pmatrix}x/T&i\epsilon y\\-i\epsilon y/T&-x/T\end{pmatrix}.
 \tag{WMC.12}
$$
Both off-diagonal signs have therefore changed relative to the traceless part of (4). The remaining derivative $i\epsilon e_\phi QK_T$ is evaluated by (3), not discarded.

Combining (9)--(12) proves the complete exact identity
$$
 \boxed{
 {\cal B}
 =2\beta m p\left(Kv\,Id-i\epsilon\frac{Qu}{\eta}K_T\right)
  +e\left\{-\left[\frac{q_r}{2q}+\beta(1+S)\right]Id
                   +\frac Q4{\cal W}\right\}-c\,Id .
 }
 \tag{WMC.13}
$$
The identity is valid also when $\beta=0$ or $m=0$. It only uses the existing $\eta\ne0$ and strict $T<0$ qualifications.

The scalar $c$ has a useful complete alternative expression. Periodicity and $\Pi e=0$ give
$$
 \begin{split}
 -\frac{2\beta m}{\eta}\Pi(pdu)
    &=\Pi(d e_\phi)=-\Pi(d_\phi e)=\beta\Pi(S e),\\
 c&=2\beta mK\Pi(pv)+\beta\Pi(S e).
 \end{split}
 \tag{WMC.14}
$$
This is a signed identity for the same full scalar, not a formula obtained by differentiating an upper bound.

## WMC3. A projected form that pays the whole scalar

Substitute (14) into (13). The result is
$$
 \boxed{
 \begin{split}
 {\cal B}={}&
 \left\{2\beta mK\,P(pv)
       -\left(\frac{q_r}{2q}+\beta\right)e
       -\beta\big[S e+\Pi(S e)\big]\right\}Id\\
 &-i\epsilon\frac{2\beta m}{\eta}pQu\,K_T
       +\frac{eQ}{4}{\cal W}.
 \end{split}}
 \tag{WMC.15}
$$
The two scalar terms in $c$ are both present: one is in $P(pv)$ and the other is the displayed additional $\Pi(S e)$. In particular, replacing $S e+\Pi(S e)$ by $P(S e)$ would give the wrong sign.

For an additional check, the mean of the coefficient of $Id$ in braces is
$$
 \Pi\{\cdots\}=-2\beta\Pi(S e).
 \tag{WMC.16}
$$
It need not vanish. The cancellation of the drift has not imposed a zero mean on this coefficient or on the physical solution.

At angular degree zero, both the projection $P(pv)$ and the sum $S e+\Pi(S e)$ require their full $L^1$ fee. At positive angular degree their constant parts have zero derivative, an exact property of the displayed functions. This distinction is used only for the kernel bound, never to delete an independent physical mean row.

## WMC4. Complete normalized derivative majorants

For $0\le j\le5$ use normalized derivatives
$$
 [a]_{j,1}=\|\partial_\phi^j a\|_1/j!,
 \qquad
 [a]_{j,\infty}=\|\partial_\phi^j a\|_\infty/j!.
 \tag{WMC.17}
$$
All $L^1$ norms use the normalized circle measure. Vectors use component sums and matrices entry sums. Thus $\|Id\|=2$ and $\|K_T\|=1+t$ in this recipe.

Read the complete successful WMT arrays
$\mathsf p_0,\ldots,\mathsf p_5$ and
$\mathsf e_0,\ldots,\mathsf e_5$ verbatim. Read its common physical-background upper array $U_j=V_j$ for $0\le j\le5$ with the original meaning that the same number bounds two different functions. No old weight or background target is reevaluated.

Write normalized convolution as
$(a*b)_j=\sum_{i=0}^j a_i b_{j-i}$.
Let $\beta^+,M,K^+,\eta_-,q_-,q_1^+$ be complete same-domain bounds for
$|\beta|,|m|,|K|,\eta,q,|q_r|$, where the two minus quantities are positive lowers. Define the private complete physical product array and the radial constant
$$
 {\cal S}_j=(U*U)_j+K^+(V*V)_j,\qquad
 h_*=\frac{q_1^+}{2q_-}+\beta^+,
 \qquad
 \delta_j=\begin{cases}1&j=0,\\0&j>0.\end{cases}
 \tag{WMC.18}
$$
These are finite predecessor arithmetic for this new candidate, not new versions of any published old physical graph.

Use complete sup arrays $Q,t,R,x,y$ for $Q,t,t^{-1},|x|,|y|$ in their actual derivative roles. In formulas below $1$ denotes the scalar array with degree-zero value one and all higher values zero; it does not denote a repeated derivative bound.

The complete positive bound furnished by (15) is
$$
 \begin{split}
 {\mathsf B}_j={}&
 4\beta^+M K^+(1+\delta_j)(\mathsf p*V)_j
 +2h_*\mathsf e_j
 +2\beta^+(1+\delta_j)(\mathsf e*{\cal S})_j\\
 &+\frac{2\beta^+M}{\eta_-}
       \{\mathsf p*Q*U*(1+t)\}_j\\
 &+\frac14\{\mathsf e*Q*[\,2x*R+y+y*R\,]\}_j .
 \end{split}
 \tag{WMC.19}
$$
Indeed, $\|P a\|_1\le2\|a\|_1$ for the normalized measure, whereas
$\partial_\phi^j Pa=\partial_\phi^j a$ for $j>0$. Also
$\|a+\Pi a\|_1\le2\|a\|_1$, and the derivative of its constant term vanishes for $j>0$. These give exactly the two factors $1+\delta_j$ in (19). The factor two from $Id$ is retained in both scalar contributions. The other two lines are the complete two off-diagonal entries of $K_T$ and all four entries of $\mathcal W$.

Every term is an $L^1$ kernel bound multiplied only by qualified sup bounds. No geometric sup is treated as a Fourier-Wiener norm, and no $L^1$ primitive fee $1/4$ is used. Formula (19) contains neither a new $e_\kappa$ derivative nor the sixth derivative of $e$. The scalar $c$ is paid in the two zero-degree fees, rather than saved as an unnecessary separate target.

The identity does not remove drift from the entire physical calculation. The complete first forcing, phase recurrence, low-order radial geometry, $k_r$, $J_r$ and physical feedback still contain every original term.

## WMC5. Ordered finite demand and the same complete trial

For geometric and first-transport predecessors use the sufficient finite packet proved in WSMF, stopped at the exact demand of the mean functional.

| Object | Demand for this candidate | Status |
|---|---|---|
| $p,e$ | Pure angular $0..5$ | Successful WMT records copied |
| Physical $u,v$ in (19) | Pure angular $0..5$ | Successful common WMT upper array copied |
| $d$ for geometry and forcing | $(r^0,\phi^{0..7})$, $(r^1,\phi^{0..6})$ | Complete private background formula with all old inputs |
| Physical $u,v$ for that drift | $(r^0,\phi^{0..6})$, $(r^1,\phi^{0..5})$ | Existing old entries copied; missing demand constructed privately |
| Relative phases and $t/t_0$ | Total $\le7$, radial $\le2$ | Frozen actual $t_0$ recurrence of WSMF/WSJ |
| Leading $w_0$ | $(r^0,\phi^{0..7})$, $(r^1,\phi^{0..6})$, $(r^2,\phi^{0..5})$ | Complete per-index packet |
| Full free $F_a,F_b$ | Pure angular $0..5$ | Includes full $\vartheta$ and all second-order terms |
| $Q,t,t^{-1},x,y$ in (19) | Pure angular through five; $x,y$ include the needed sixth geometry derivative | Complete same-function bounds |
| $H^{-1}$, $V_{\rm ext}$, $V_{\rm ext}y$ | Pure angular $0..5$ | Exact inverse and complete genuine potential |
| Free cut and transport | Pure angular $0..5$ | True nonzero cut and full ordinary-$dr$ integral |
| $w_1^e$ | Pure angular $0..5$ | Full free transport plus complete ${\cal B}_{\rm ext}K_Tw_0$ |
| Physical mean derivative and affine source | Full original $A_s,k_0,I_k,T_k$ | Existing complete records copied |

The normalized phase recurrence keeps all $\eta_r,q_r,d_r$ contributions. The frozen radial scale is differentiated as a constant. The leading second radial derivative needs $q_{rr}$ and the full original lower-order radial data. No claim is made that a radial-two $Q_f$ packet is available without $\eta_{rr}$; this mean functional does not require that packet.

The actual first amplitude retains its nonzero free cut trace. The cut initialization uses the complete original component records and the same separate cut phase lower, not a strict lower substituted into a complex disk. The genuine extension is added only after the full free transport or with its corresponding full extended forcing. No root domain is enlarged.

When a same-function ordinary normalized coefficient has an old complete bound on the identical domain and norm, it may be read as a safe bound. A positive minimum may be taken only between complete bounds for that same coefficient. No minimum between different operator entries or differently normalized quantities is used.

The WSMF private finite arrays were not published as independently reusable science targets. This proof does not claim they can be recovered from its eighteen upper-bound amplitudes. A later consumer must form the necessary private predecessor arithmetic for the new expression (19), from the admitted saved inputs. It must not invoke the old complete WSMF/WSM producers or reevaluate any of their public scalar targets.

## WMC6. Eighteen new complete amplitudes

The exact three coefficient functions remain
$$
 A_0={\cal B}w_0,\qquad
 A_1={\cal B}w_1^e-{\cal D}w_0+e q_e,\qquad
 A_2=-{\cal D}w_1^e.
 \tag{WMC.20}
$$
Here $\mathcal B$ is the exact same function, now bounded by (19). No old upper for it or for $A_k$ is subtracted.

Let $W_0,W_1$ be complete component-sum sup arrays for $w_0,w_1^e$. With complete $F_a^e,F_b^e$ arrays, define
$$
 \begin{split}
 D_j&=\{\mathsf e*V_{\rm ext}*Q*(x+y)\}_j,\\
 q^e_j&=\tfrac12\{Q*[(x+y)*F_a^e+(y+x*R)*F_b^e]\}_j,\qquad
 E_j=(\mathsf e*q^e)_j,\\
 {\cal A}_{j,0}&=({\mathsf B}*W_0)_j,\\
 {\cal A}_{j,1}&=({\mathsf B}*W_1)_j+(D*W_0)_j+E_j,\\
 {\cal A}_{j,2}&=(D*W_1)_j,\qquad 0\le j\le5 .
 \end{split}
 \tag{WMC.21}
$$
The eighteen displayed amplitudes are complete new bound targets. The original potential additions occur in both forcing components. All three inverse-frequency degrees $0,1,2$ remain present.

The change of bound is defined at the exact function level by (13)--(15). It is not a numerical refinement by removing a fee from a previously printed subtotal. The new candidate is valid regardless of whether its final bound is smaller.

## WMC7. Five exact mean steps and all eight terminal coefficients

Let $c_V=V_{\rm ext}y$ and $\mathcal A_n=\partial_\phi-zc_VE_{12}$. Set
$$
 v_0=H^{-1}(A_0+zA_1+z^2A_2),\qquad
 v_{\ell+1}=-H^{-1}\mathcal A_n v_\ell,\quad0\le\ell\le3 .
 \tag{WMC.22}
$$
The genuine angular derivative identity and periodicity give
$$
 \Pi\mathcal U^{\rm ext}(A_0+zA_1+z^2A_2)
 =-n^{-5}\Pi\mathcal U^{\rm ext}(\mathcal A_n v_4).
 \tag{WMC.23}
$$
The complete finite positive recurrence is
$$
 \begin{split}
 V^{(0)}_{j,k}&=\sum_{i=0}^j H_i{\cal A}_{j-i,k},
       &&0\le j\le5,\quad0\le k\le2,\\
 D^{(\ell)}_{j,k}&=(j+1)V^{(\ell)}_{j+1,k}
                    +\sum_{i=0}^j(c_V)_iV^{(\ell)}_{j-i,k-1},\\
 V^{(\ell+1)}_{j,k}&=\sum_{i=0}^j H_iD^{(\ell)}_{j-i,k},
       &&0\le\ell\le3,\quad0\le j\le4-\ell,\quad0\le k\le3+\ell .
 \end{split}
 \tag{WMC.24}
$$
A negative polynomial index means exact zero. No nonnegative retained degree is truncated. In particular the full eight terminal records are
$$
 {\cal T}_k=V^{(4)}_{1,k}+(c_V)_0V^{(4)}_{0,k-1},
 \qquad 0\le k\le7 .
 \tag{WMC.25}
$$
Read the old single-reference pointwise profile upper $P_*$ and retain the original reflected assembly factor:
$$
 C_F^{\rm new}=2P_*\sum_{k=0}^7N_0^{-k}{\cal T}_k,
 \qquad |F_{{\rm mean},n}|\le C_F^{\rm new}n^{-23/6}.
 \tag{WMC.26}
$$
The exponent is still $7/6-5=-23/6$. This is not an N4 candidate and does not use the different N4 whole-input sum. The full potential and every terminal remain in (24)--(26).

The finite inverse levels are private intermediate arithmetic. Their terminal records are the new targets defined by (21), not the old WMT or WSMF terminal records, and no successful old terminal is recalculated.

## WMC8. The complete physical mean and all four endpoints

Read the original complete local mean $Z_l$, local raw mean-source upper $M_l$, strict backward propagator $G_s$, strict absolute coefficient $A_s$ and complete $k_0,I_k,T_k$ bounds. They keep their full original scopes, including the real two-patch propagation, true root condition and $J_r,k_r,R_0$ feedback.

The seven new targets are
$$
 \begin{split}
 Z_s&=G_s(r_c C_F^{\rm new}+Z_l),&
 Z_s'&=A_sZ_s+C_F^{\rm new},\\
 M_s&=k_0Z_s'+T_kZ_s,&
 \widetilde M_s&=I_kZ_s'+\tfrac14T_kZ_s,&
 M_c&=\max(M_l,M_s),\\
 E_{\rm mean}&=V_z^{\rm old}\Xi_{23/6}^{\rm old}Z_s,&
 E_{\rm waist}&=E_{\rm scatter}^{\rm old}+E_{\rm second}^{\rm old}
                         +E_{\rm WT}^{\rm old}+E_{\rm mean}.
 \end{split}
 \tag{WMC.27}
$$
The complete physical source is $-kz_{{\rm ph},r}-z_{\rm ph}\mathscr T_k$; both terms are paid. The same-$J$ radial contributions have not been replaced by the zero angular derivative of $c$.

The original $V_z$ norm includes both stored physical means and the $q$ density contribution. The scattering, second-order and waist-normalizer endpoints remain complete unchanged old terms in (27), unless a separately successful complete same-object endpoint provider is explicitly admitted. No current large endpoint is reduced by subtracting a mean upper. All original factors occur in their original order and exactly once.

The strict reciprocal formulas of this proof are never applied to the local root interval. The old complete local $Z_l,M_l$ remain intact. This theorem gives no new root continuation, positive graph or head inverse.

## WMC9. Complete negative reception and whole-operator candidates

Admit one immutable complete current nonmean provider for the same trial and operator. The already successful WRPA receipt supplies the full improved collar and strict retained bounds $B_c,B_t$, complete terminal contribution $N_t$, original jumps $J_c,J_s$, receiver constants and all existing dyadic factors. A later successful whole-operator candidate may be used as the comparison value without changing these complete same-object nonmean data.

Using the original ordinary measures, form the seven complete received records
$$
 \begin{split}
 S_c&=\sqrt2\,\ell_+^{1/4}B_c+\sqrt{\ell_+}M_cN_0^{-5/3},\\
 S_s&=c_{\rm PW}\,[\ell_-^{-1/4}B_t+\widetilde M_sN_0^{-4/3}],\\
 R_c&=C_OS_c+C_RJ_c,\qquad R_s=C_1(S_s+J_s),\\
 N_c&=R_c{\cal S}_{1/3},\qquad N_s=R_s{\cal S}_{2/3},\\
 C_{\rm neg}^{\rm new}&=C_{\rm Bes}(N_c+N_s+N_t^{\rm old}).
 \end{split}
 \tag{WMC.28}
$$
Every square root, fixed power, dyadic sum and Bessel factor in (28) is an already complete saved record and is copied, not reevaluated.

The collar source uses the original $L^2(dr;H^{-2/3})$ first-source receiver. The jumps use the original mixed $H^{-2/3}\oplus H^{-1}$ space and the exact second-row-zero qualification. The strict primitive is received by the original $C_1$ map. All 3070 true interfaces and both-sided forcing qualifications remain present; no radial length multiplies a jump. Both physical mean coordinates are included in (27)--(28).

Retain the two different complete operator realizations:
$$
 \begin{split}
 S_{\rm nr}&=R_+^{\rm old}+C_{\rm neg}^{\rm new}+E_{\rm waist},
 &S_{\rm all}&=S_{\rm nr}+R_F^{\rm old},\\
 R_{\rm whole}&=L_{\rm rec}^{\rm old}S_{\rm all},
 &C_{\rm whole}^{\rm new}&=C_{\rm alg}^{\rm old}+R_{\rm whole},\\
 R_{\rm reduced}&=L_{\rm rec}^{\rm old}S_{\rm nr},
 &C_{\rm reduced}^{\rm new}&=D_\infty^{\rm old}+R_{\rm reduced}.
 \end{split}
 \tag{WMC.29}
$$
These are six new complete records. $R_F$ is retained in the whole realization, and $D_\infty$ is not called $C_{\rm alg}$. The finite factors, $\Theta$, strong $\nu$ term, radial-head functions and their compatibility conditions remain in the actual equations. This new mean estimate neither constructs nor inverts any of them.

Only after (29) is completely saved may each new candidate be compared with the current complete bound for that same operator. Store both whole candidates and both reduced candidates separately, with exact original record paths; the old candidate wins equality. No componentwise selection between incompatible decompositions is permitted.

## WMC10. New-target boundary and admission

The prospective public targets are fixed by their complete formulas:

| Natural conclusion | New targets | Count |
|---|---|---:|
| complete_drift_cancelled_strict_mean_source | Eighteen amplitudes (21), eight terminal coefficients (25), full $C_F$ (26) | 27 |
| complete_physical_mean_and_four_endpoints | All seven records in (27) | 7 |
| complete_current_negative_and_whole_receiver | All seven records in (28) and six in (29) | 13 |
| **Total** | **Complete new candidates only** | **47** |

There is no new $e_\kappa$ target, no new $e_6$ target and no separate numerical target for $c$. Formula (15) and the two degree-zero fees in (19) retain all of $c$ within the complete flux targets.

The original WMT p/e/background records, WDG80, WBF83, WJR56, WRT42, WSM152 and WRPA40 are frozen. WSMF52, including any saved failure prefix or completed first execution, remains frozen and is never replayed. The independent W4M N4 candidate remains a different complete unit and is not inserted into the N5 coefficient formulas.

The already saved lower, cutoff, radial, extension, local, same-$J$, propagator, pointwise-profile and receiver objects used by WSMF are the required existing inputs here. The common neutral finite algebra may be reimplemented as inert support code, but no complete old producer is imported or called. The new matrix expression (19), not a rerun of WSMF's old positive matrix expression, defines the eighteen new targets.

The successful WSMF52 receipt from run 43886938106/1 may supply its complete current whole/reduced choices as comparison records. It is not a source of missing private mixed arrays and does not authorize deriving them from a saved upper. If a separately complete newer nonmean or endpoint provider exists, its entire same-object qualification and exact field mapping must be admitted before use.

A future owner must verify complete raw identities, all consumed schema/type/domain qualifications and exact immutable source paths. A successful child graph from an earlier failed parent is usable only with that parent status preserved. Each newly produced public record is made durable in its complete natural conclusion before its directed endpoint is consumed. A failure retains the full current prefix; it does not authorize automatic repetition of completed targets.

No interval value, scientific Python, Arb routine, ray integration, eigenvalue, old bound or numerical test has been evaluated in this proof. Its record count is not a substitute for a complete serialized output budget.

## WMC11. Exact existing input chain

The proof applies to the full saved-input chain already fixed for WSMF. All paths below are under topics/visible-flex-exact-nearby.

| Input | Complete path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| WGS main | notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |
| WGS copies | notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json | d6d13860e322d82ce354c8c0d0eb0f279ca63b3c | 31632 | 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66 |
| WBF | notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/actual-scientific-conclusion.json | df5ea6fff610d70ad98fbebc9dd004d24388ce86 | 59417 | 87621adee76080dbbc14abdd7f8e5dce5d3e2742ba299fc941d13ff40f4410c0 |
| WJR | notes/relative_flow_Jacobian_ci/run-43873739440-1/actual-scientific-conclusion.json | 80499e42f643e607db47c973b54f2243629a05e8 | 69002 | 806fbeaaab33ddff424fcfe70e40f83f46d1f85e089f9f01f941ed38ee249660 |
| WDG | notes/positive_drift_relative_omega_ci/run-43865837250-1/actual-scientific-conclusion.json | 67c7070e6678223b5de63635d4b18f110500a742 | 47714 | 04b757433390715acd5e2bca3cd29afef0ccf3e3cea35d5855a96eb28bf89395 |
| Complete extension | notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/extension_scalars.json | c5d9166b914a17136c5058b3d213afc4dffad5c0 | 12958 | 5816db201af6f0da0f7412c1a1fe0f1521d5425debf37693ab652f152e7fec00 |
| WMTA | notes/strict_flux_mean_forcing_ci/run-43856579962-1/actual-scientific-conclusion.json | edd66cdbe7a438569524ba2614d3822f61de5c81 | 90421 | c6680025917247e7bec958851d5ee85fc3c3750b059372a87ec568cd9d8acbd4 |
| WRPA | notes/relative_phase_pullback_receiver_ci/run-43881690924-1/actual-scientific-conclusion.json | 146904d030cca0887fae921084396bf4008d0281 | 82508 | 4b66bd0ba1425c7a5a705cba3b32b07ea893643a7aa8cde1a720dcf450e852ee |
| WSMF52 current complete comparison | notes/per_index_strict_flux_complete_mean_ci/run-43886938106-1/actual-scientific-conclusion.json | c20713f51366ef6c838147232994424bf3e633de | 61398 | 3243348d6dddc11c8baf1f6eb559d929a37c509a464165b7042d1ce47bb2e290 |

The WMT input arrays are
complete_new_graphs.complete_normalized_weight_L1_kernels.new_records.p_L1_upper[0..5],
e_L1_upper[0..5], and pure_angular_background_pair_upper[0..5].
Its exact copied scalar paths for strict_beta, strict_V, strict_Kabs, strict_eta_lower, local_mean, local_raw_mean_source, strict_backward_factor, strict_absolute_coefficient, strict_k0, strict_Ik, strict_Tk, point_profile, endpoint_Vz, Xi23_6, endpoint_scattering, endpoint_second_order and endpoint_WT retain their original roles. The eta field is a lower, not an upper to be inverted.

The required $q_1^+,q_-$ are WGS copies copied_original_scalar_records.q_1 and q_lower. The per-index geometric inputs, true cut component records, WDG fifth cut derivative, original flow/phase ratios and complete extension derivatives are exactly those listed in WSMF11, with their complete lower/sup/Fourier-Wiener distinctions. No unrecorded angular derivative is inferred from a total-degree label without its original certificate.

The published WSMF proof is [Per-index strict flux](R133-supplement-per-index-strict-flux-and-complete-physical-mean-bound.md), blob f808c0b5966bcb9728603dd808dad904873123e8, 36418 bytes, SHA256 5845b88028b384356f53535353559bdfa15691a1bf7e019fe39d42538643a803. It supplies the complete finite demand and ordered propagation used here, but its public 52 targets are not this new recipe.

The exact normalized-weight identity is WMF, blob 2c4a1789195a1ea400ef7c547b319ea3f4f7329f, 15111 bytes, SHA256 14900631ba2d793977336fd5f7e8870e4313cbda50a8a8c3e02fa11b53054356. The complete strict flux is WMT, blob c8049ef93eca8f84f135ab4338d6485081fb8424, 31256 bytes, SHA256 51eb08d0b110b8a5b171538c3be023efb94df587fdab880ebddac518665f73ce. The full two-patch physical-mean propagation is WMR, blob a7b23dea9a96dfab74475d382ca2d1df8edd5b8e, 31643 bytes, SHA256 550866c05d9a07d3e4b037e5840a4f75b66a7f3a9304c5cd0d52e4f2b7e729a6.

The exact strict mixed derivative and inverse scopes remain [WSJ](R133-supplement-scaled-strict-mixed-jets-and-exact-fold-inverses.md), blob 10c6e4220377b772692095347f096e5d897afc5e, and [WCPR](R133-supplement-complete-cut-initialization-and-positive-profile-budget-reuse.md), blob da15190045b2cb05cffdfd410ab91fc9e5673286. The exact drift cancellation above does not change either domain or remove any positive-lower requirement.

This proves a complete finite bound recipe. It does not prove smallness, a signed finite inverse, solvability of the negative head, or completion of the original nonlinear problem.
