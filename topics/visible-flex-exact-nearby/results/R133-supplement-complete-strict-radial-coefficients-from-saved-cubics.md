# R133 supplement: complete strict radial coefficient fees from the saved piecewise cubics

2026-11-15, visible-exact / phase_inverse.

**An exact analytic derivative and interface contract for the new SF scalar consumer.** The successful WX result supplies the true characteristic derivatives and the two leading-density windows. The successful FA result supplies the complete corrected cut input and its cut error. This note supplies the remaining ordinary radial coefficient bounds required by SF, using the saved body jets and the exact piecewise polynomial definitions of the repaired centre and response.

The old body target is evaluated at the original intrinsic parameter $\nu_0$. Its old affine parameter box concerns $\eta$; it is not a certificate for the whole new $\nu_0+\delta$ family. All changes of $\gamma,K$ and their radial derivatives on the compact control support are charged below. The scalar function in the physical background remains the fixed true $s_{\eta_0,\nu_0}$. It is not replaced by a new rotational reference $s_{\eta_0,\nu_0+\delta}$.

This contract proves finite formulas and their domains. It does not report new numerical derivative, integral or jump budgets. Its intended consumer performs only those new scalar operations. It does not rerun an old target, primitive, profile, ray, repaired polynomial, source calculation or successful flow.

## 1. Reference, norms and immutable inputs

Keep exactly the reference and strict cut of [SF](R133-supplement-complete-strict-first-symbol-propagation-defect.md):
$$
 Q_\delta=\bar Q+\delta Z_{\rm can},\qquad
 \nu=\nu_0+\delta,\quad \eta_{\rm intrinsic}=\eta_0,\quad
 |\delta|\le d:=10^{-8},\qquad
 0\le r\le r_c=\frac{76285779072683}{320000000000000}.
 \tag{SJ.1}
$$
Here
$$
 \nu_0=-\frac{2572625729470897}{72057594037927936},
 \qquad \eta_0=-\frac{7789843107295549}{4611686018427387904}.
 \tag{SJ.2}
$$
The radial transport coefficient $\eta(r)=-\gamma(r)\langle v(r)\rangle$ used later is distinct from the fixed intrinsic parameter $\eta_0$.

All angular derivatives are in the original moving angle $\phi$, of period $\pi/2$. Put
$$
 \|f\|_{A^0}=\sum_{j\in\mathbb Z}|\widehat f_j|,
 \qquad
 \|(f_1,f_2)\|_{A^0,\mathrm{pair}}
       =\|f_1\|_{A^0}+\|f_2\|_{A^0}.
 \tag{SJ.3}
$$
Matrix, row and column coefficient budgets below use the sum of the complete component $A^0$ norms. This sum includes both Fourier signs and every mean. Ordinary radial and angular derivatives are used; there is no factorial-jet convention hidden in the numerical inputs.

The repaired definitions are immutable:

| Object | Definition SHA256 |
|---|---|
| Exactly continuous centre $\bar Q$ | `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47` |
| Complete physical response $Z_{\rm can}$ | `6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04` |
| Original background index | `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413` |
| Original full physical response index | `ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6` |

The already proved full-body estimates used here are
$$
 \|\bar Q\|_{A^0,\mathrm{pair}}\le7,\quad
 \|\bar Q_\phi\|_{A^0,\mathrm{pair}}\le6,\quad
 \|Z_{\rm can}\|_{A^0,\mathrm{pair}}\le19,\quad
 \|(Z_{\rm can})_\phi\|_{A^0,\mathrm{pair}}\le83.
 \tag{SJ.4}
$$
They are the full-state estimates identified in Section 2 of the [D parameter-difference contract](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md), including both repairs. Using these four estimates at the radius $d$ in (SJ.1) does not extend the separate D finite-operator computation made at $10^{-10}$. The latter conclusion is not an input here.

## 2. What the old body rows actually certify

The frozen correlated producer is
`scripts/fourfold_codazzi_correlated_head_residual_rows.py`,
Git blob `3af195a36ccb30630dbfcab0caef3564738ab169`,
13,043 bytes, SHA256
`1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07`.

Its `row_budget` calls
`target.coefficients(left,right,c['nu'])` and saves
`intrinsic_whole_third_jets` with precisely
$$
 a_{\rm phys},\qquad
 \gamma_0^{(j)},\ \beta^{(j)},\ K_0^{(j)},\
 s_0^{(j)},\quad 0\le j\le3.
 \tag{SJ.5}
$$
Its `main` fixes `c['nu']` to the exact original $\nu_0$. The original halfwidth is exactly $10^{-9}$ and the original completion identifies it as the whole original $\eta$ box. Restriction to the fixed $\eta_0$ in (SJ.1) is legitimate. No change of that old box, and no identification of that box with the new $\delta$ radius, is made.

The saved $s_0$ is the genuine scalar target at $(\eta_0,\nu_0)$. In particular,
$$
 \begin{split}
 s_{0,r}&=\beta s_0(1-K_0s_0^2),\\
 s_{0,rr}&=\beta_r s_0(1-K_0s_0^2)
       +\beta s_{0,r}(1-3K_0s_0^2)-\beta K_{0,r}s_0^3 .
 \end{split}\tag{SJ.6}
$$
These identities explain the true nonpolynomial part of the background. The new consumer reads the already saved $s_0,s_{0,r},s_{0,rr}$ enclosures in (SJ.5); it does not solve this ODE again.

The actual old row is always used on a subset of its original closed interval and original scalar germ. Restriction does not make its saved whole-interval derivative enclosure sharper. In particular the final body row containing the root can still supply $K_{0,r},K_{0,rr},K_{0,rrr}$ on the strict portion, but its unsigned zero-order curvature interval must not be used to invent a strict square-root denominator. The latter comes from the already successful RR/ST strict test, as specified in Section 6.

## 3. Recover a genuine polynomial interval from the old common partition

The original partition source is
`scripts/fourfold_codazzi_mean_completed_head_body_residual_v3.py`,
blob `f514bb81ec6c24e2035c3b08b96520b4c1e243d5`,
29,107 bytes, SHA256
`9674f5f6b9d4ad95d7d87fb22b2ec4c8fc3cad136b78afed677343c2510bb6df`.

Its `prepare` forms the exact common cuts from all original background, response and adjoint nodes, all original scalar cells, and both compact-control endpoints. Its `identity` checks, separately for every labelled background and trial piece,
$$
 r_j^{\rm piece}\le \ell_{\rm row}<r_{\rm row}
                    \le r_{j+1}^{\rm piece}.
 \tag{SJ.7}
$$
This is a genuine containment test, not a midpoint choice of a polynomial.

Read the immutable body rows in their original order and group consecutive rows which have the same ordered pair of labels
`pieces.background` and `pieces.response`. The exact union is a closed interval
$$
 I_\lambda=[a_\lambda,b_\lambda],\qquad
 h_\lambda=b_\lambda-a_\lambda>0.
 \tag{SJ.8}
$$
On this interval each of the two physical polynomial pieces is unchanged. Scalar-germ changes and adjoint-piece cuts may subdivide the group without changing this fact. The consumer verifies exact adjacency, row indices, the original piece labels and their original input identity. It retains the exact endpoints and the constituent old row indices in its temporary audit.

The group is only called a full original polynomial piece when its two endpoints are witnessed by the corresponding original label changes or original domain endpoints. Otherwise it is explicitly a qualified subinterval of the original piece. Markov's inequality below holds on either kind of interval. A final partial interval ending at $r_c$ is not extended through the root or through an unseen polynomial join.

For each group take the maximum of the already saved complete $|s_0^{(p)}|$ enclosures of its constituent rows, denoted $S_{\lambda,p}$. No polynomial coefficient, Fourier norm, repair offset or old scalar germ is reevaluated to obtain this maximum. The polynomial interval length is an exact rational number from (SJ.8), not a nominal mesh width.

## 4. Mixed derivatives from the exact cubic definitions

By the [centre repair](R133-supplement-exact-continuous-repair-of-final-centre.md), on every unchanged original background piece
$$
 \bar Q-s_0e_2
 =\alpha(U,V)+e_j
 \tag{SJ.9}
$$
is a Banach-valued polynomial of degree at most three, where the physical repair $e_j(\phi)$ is constant in $r$. By Q.1--3 of the [response definition](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md), $Z_{\rm can}$ is another degree-at-most-three polynomial plus its own exact radial constant. Its 193 physical coefficients receive no factor $\alpha$.

For a Banach-valued polynomial $P$ of degree at most three on an interval of length $h$,
$$
 \sup\|P_r\|\le\frac{18}{h}\sup\|P\|,\qquad
 \sup\|P_{rr}\|\le\frac{96}{h^2}\sup\|P\|.
 \tag{SJ.10}
$$
The constants follow from the scalar Markov bounds $9$ and $24$ on $[-1,1]$, followed by the affine change of interval. Apply the scalar inequality to every norm-one dual functional and use the dual characterization of the Banach norm. This proves (SJ.10) directly for the complete pair $A^0$ norm; there is no dimension or Fourier-grid factor.

Set
$$
 \begin{array}{lll}
 C_{\lambda,0}=7+S_{\lambda,0},&
 C_{\lambda,k}=6\,128^{\,k-1}&(k\ge1),\\
 Z_0=19,&Z_k=83\,384^{\,k-1}&(k\ge1),\\
 M_1(h)=18/h,&M_2(h)=96/h^2.&
 \end{array}\tag{SJ.11}
$$
The physical derivative frequencies are $128=4\cdot32$ and $384=4\cdot96$. Thus the complete mixed derivatives required below have the bounds
$$
 \begin{split}
 Q_{\lambda,0,0}^{\#}&=7+19d,\\
 Q_{\lambda,0,k}^{\#}&=C_{\lambda,k}+dZ_k,\qquad k\ge1,\\
 Q_{\lambda,p,k}^{\#}&=
 M_p(h_\lambda)(C_{\lambda,k}+dZ_k)
                    +{\bf1}_{k=0}S_{\lambda,p},
       \qquad p=1,2,\quad 0\le k\le3 .
 \end{split}\tag{SJ.12}
$$
They bound $\|\partial_r^p\partial_\phi^kQ_\delta\|_{A^0,\mathrm{pair}}$ uniformly over the full real family (SJ.1). To prove the last line, apply Markov to the polynomial
$\partial_\phi^k(\bar Q-s_0e_2+\delta Z_{\rm can})$, then add the true derivative of $s_0e_2$ only when $k=0$.

The first line deliberately uses (SJ.4) directly. It does not add and subtract $s_0$ and lose a second zero-order scalar fee. At positive angular order the scalar mean of $s_0$ is exactly absent, while the genuine Fourier means of all other complete products remain.

These are one-sided ordinary derivative bounds on each closed polynomial piece. They do not assert continuity of $Q_r$ or $Q_{rr}$. In particular they do not identify the distributional second derivative with an ordinary function. The actual jump contributions are retained in Section 10.

## 5. New full-family intrinsic jets, including the compact region

Write $a_{\rm phys}=a_{\rm phys,\eta_0}$ and $\gamma_0,K_0,s_0$ for the old $\nu_0$ quantities. From the exact metric definition D.2,
$$
 \gamma_\delta=\gamma_0e^{\delta w/2},\qquad
 K_\delta=e^{-\delta w}(K_0+\delta T_0w_r),\qquad
 T_0=\frac{\beta}{2\gamma_0^2a_{\rm phys}^2}.
 \tag{SJ.13}
$$
The symbol $T_0$ in this section is a radial metric coefficient, not a canonical fold coordinate. The functions $a_{\rm phys},\beta$ are independent of $\nu$. The reference $s_0$ inside (SJ.9) remains fixed. No $s_{\nu_\delta}$ derivative or parameter response is inserted into $Q_\delta$.

On the compact interval $[1/20,9/50]$ put
$$
 t=\frac{r-1/20}{13/100},\quad u=t(1-t),\quad v=1-2t,\quad
 w=4096u^6 .
 \tag{SJ.14}
$$
The weight is zero off this interval. Its derivatives through order five match zero at both endpoints. In addition to the already used bounds
$$
 W_0=1,\qquad W_1=2400/13,\qquad W_2=5280000/169,
 \tag{SJ.15}
$$
a complete positive third/fourth derivative pair is
$$
 W_3=10560(100/13)^3,\qquad W_4=190080(100/13)^4.
 \tag{SJ.16}
$$
Indeed
$$
 w_{ttt}=4096(120u^3v^3-180u^4v),\quad
 w_{tttt}=4096(360u^2v^4-1440u^3v^2+360u^4).
 \tag{SJ.17}
$$
Use $0\le u\le1/4$ and $|v|\le1$, then apply the true radial scale once for each derivative. No numerical maximization or old bump integral is required by this analytic statement.

Here is a complete positive ordinary-derivative calculus. For two nonnegative derivative arrays define
$$
 (X\star Y)_j=\sum_{i=0}^j {j\choose i}X_iY_{j-i}.
 \tag{SJ.18}
$$
Every product of radial coefficients below uses this rule. If $g\ge g_->0$ and $G_j\ge|g^{(j)}|$, set
$$
 R_0=g_-^{-1},\qquad
 R_j=g_-^{-1}\sum_{i=1}^j{j\choose i}G_iR_{j-i}\quad(j\ge1).
 \tag{SJ.19}
$$
Then $R_j$ bounds $|(g^{-1})^{(j)}|$, by differentiating $g g^{-1}=1$.

On each original body row let $b_j,\Gamma_j,K_j^0$ be absolute upper bounds read from (SJ.5), with positive saved lower bounds for $a_{\rm phys}$ and $\gamma_0$. For $A=a_{\rm phys}^{-2}$ one may use
$$
 \begin{split}
 A_0&=a_-^{-2},\qquad A_1=2b_0A_0,\\
 A_2&=(2b_1+4b_0^2)A_0,\\
 A_3&=(2b_2+12b_0b_1+8b_0^3)A_0 .
 \end{split}\tag{SJ.20}
$$
These follow from $a_r=\beta a$. Apply (SJ.19) to $\gamma_0$ and square the resulting array using (SJ.18), obtaining an array $G^{[-2]}$ for $\gamma_0^{-2}$. The genuinely new positive budget
$$
 T_j^\#=\tfrac12\,(b\star G^{[-2]}\star A)_j,\quad0\le j\le3
 \tag{SJ.21}
$$
bounds every derivative of the same $T_0$ in (SJ.13). It is not a call to the old signed Taylor-jet producer `T_jets`.

For $z=d$ or $z=d/2$ define
$$
 \begin{split}
 E_0(z)&=e^{zW_0},&E_1(z)&=zW_1E_0(z),\\
 E_2(z)&=(zW_2+z^2W_1^2)E_0(z),&
 E_3(z)&=(zW_3+3z^2W_1W_2+z^3W_1^3)E_0(z).
 \end{split}\tag{SJ.22}
$$
These bound the absolute ordinary derivatives of either signed exponential needed in (SJ.13). Set
$$
 L_j^\#=K_j^0+d\sum_{i=0}^j{j\choose i}T_i^\#W_{j-i+1}.
 \tag{SJ.23}
$$
Then complete full-family upper arrays are
$$
 K_j^\#=(E(d)\star L^\#)_j,\qquad
 \gamma_j^\#=(\Gamma\star E(d/2))_j,\quad0\le j\le3 .
 \tag{SJ.24}
$$
A full-family lower bound is $\gamma_-=\gamma_{0,-}e^{-dW_0/2}>0$. Outside the compact support the changed coefficients and all their derivatives equal the original ones exactly; those rows are copied instead of charged a fictitious exponential change.

The third derivative of $K_\delta$ genuinely needs $W_4$ through $T_0w_r$. Its omission would be a loss of domain, not an innocuous choice of a looser constant. Equations (SJ.13)--(SJ.24) explicitly cover the whole bump region for every $|\delta|\le10^{-8}$.

## 6. Strict square roots and the full radial transport speed

The existing SP/ST/RR conclusions, in their original order and exact intervals, allow a new complete scalar readout
$$
 0<q_-\le q(r,\delta)=\sqrt{-K_\delta(r)}\le q_+,
                 \qquad0\le r\le r_c .
 \tag{SJ.25}
$$
No original strict row container is needed for this readout. Let $q_{c,-}$ be the literal RR/ST lower bound at $r_c$, and let $C_+^{\rm SP}$ be the literal SP field
`complete_strict_propagation_conclusion.new_complete_forward_log_upper`.
Its frozen source computes
`cplus=up(oldc+jq+(qright.upper()/qleft.lower()).log())`.
Equations SP.29--30 prove that this specific positive-log budget bounds
$$
 \int_0^{r_a}\max(0,q_r/q)\,dr\le C_+^{\rm SP},
 \qquad r_a=\frac{1191939371497}{5000000000000},
 \qquad |\delta|\le10^{-8}.
 \tag{SJ.25a}
$$
Although the original SP nonradial product ends at its earlier cut, this curvature budget covers the full original interval $[0,r_a]$. The accepted ST `complete_accepted_original_conclusion` also preserves this exact full-interval source identity. It is not inferred from a generic propagator norm.

For $r\le r_a$,
$\log q(r_a)-\log q(r)\le C_+^{\rm SP}$.
On $[r_a,r_c]$ the accepted same-germ signed $K_r>0$ gives $q_r<0$ and $q(r_a)\ge q(r_c)$. Therefore the new sufficient choice is
$$
 q_-:=q_{c,-}\exp(-C_+^{\rm SP}).
 \tag{SJ.25b}
$$
For $r\ge r_a$ the stronger $q(r)\ge q_{c,-}$ holds. To implement (SJ.25b), use the stored lower endpoint of $q_{c,-}$, the stored upper endpoint of $C_+^{\rm SP}$, and a directed lower endpoint of the resulting exponential product. This is a new elementary positive combination of successful scalar inputs; it reruns neither the old grouped integral nor the old matrix product.

For $q_+$ take the larger upper endpoint of the accepted SP full-prefix
`new_entire_q_upper` and the accepted ST
`complete_new_strict_propagation_conclusion.complete_new_tail_scalar_maxima.qplus`.
Those two complete intervals cover $[0,r_c]$. All fields retain the same real family in (SJ.1). The root-adjacent lower bound is not recomputed from an old unsigned $K$ ball, and no N.005 cut constant is moved to P.22.

With (SJ.25), each row of (SJ.24) gives
$$
 \begin{split}
 q_1^\#&=K_1^\#/(2q_-),\\
 q_2^\#&=K_2^\#/(2q_-)+(K_1^\#)^2/(4q_-^3),\\
 q_3^\#&=K_3^\#/(2q_-)+3K_1^\#K_2^\#/(4q_-^3)
                              +3(K_1^\#)^3/(8q_-^5).
 \end{split}\tag{SJ.26}
$$
All these are derivatives in the outward coordinate $r$, not derivatives of inward root distance.

The explicit repaired mean in Q.7 of the response proof satisfies
$$
 -m_0>1.068732695 .
$$
Thus the full real family in (SJ.1) has
$$
 -m_\delta\ge m_-:=1.068732695-19d>0 .
 \tag{SJ.27}
$$
The same theorem covers the entire strict interval, since its negative endpoint lies beyond $r_c$. All mean derivatives are bounded by the corresponding component of (SJ.12), without a true-solution equation for $m_\delta$.

For $\eta=-\gamma_\delta m_\delta$ use
$$
 \begin{split}
 \eta_-&=\gamma_-m_-,\\
 \eta_0^\#&=\gamma_0^\#M_0,\quad
 \eta_1^\#=\gamma_1^\#M_0+\gamma_0^\#M_1,\\
 \eta_2^\#&=\gamma_2^\#M_0+2\gamma_1^\#M_1+\gamma_0^\#M_2 ,
 \end{split}\tag{SJ.28}
$$
where $M_p$ is any complete bound for $|m_\delta^{(p)}|$ from (SJ.12). Put $h=\eta q$. Its positive lower bound is $h_-=\eta_-q_-$, and $h_0^\#,h_1^\#,h_2^\#$ follow by the ordinary product rule. The inverse-derivative array of $h$, through order two, can be taken as
$$
 j_0=h_-^{-1},\qquad
 j_1=h_1^\#/h_-^2,\qquad
 j_2=h_2^\#/h_-^2+2(h_1^\#)^2/h_-^3 .
 \tag{SJ.29}
$$
These are new complete scalar bounds. The symbols $\eta_0^\#,\gamma_0^\#$ here mean derivative order zero and are not changes of the fixed parameter $\eta_0$ in (SJ.2).

## 7. A complete finite coefficient closure for SF

All signed identities in this section are exact before taking absolute values. Their positive implementation uses (SJ.18), the angular counterpart of that binomial rule, and the component entry sum. In particular two off-diagonal entries are both retained.

Write $u,v$ for the selected state and set, as in SF,
$$
 \mathscr S=u^2+K_\delta v^2,\quad
 d_r^{\,\rm drift}:=\partial_r(-\beta I\mathscr S),\quad
 d=-\beta I\mathscr S,\quad
 r_\sigma=u+\sigma qv,\quad c_\sigma=d+\sigma h .
 \tag{SJ.30}
$$
The notation $d_r^{\,\rm drift}$ is only to distinguish this derivative from the fixed parameter radius $d$ in (SJ.1). In the following formulas a subscript $r$ on a coefficient always denotes its ordinary radial derivative.

The complete drift formulas needed are
$$
 \begin{split}
 d_r&=-\beta_r I\mathscr S-\beta I\mathscr S_r,\\
 d_{\phi^k}&=-\beta P\partial_\phi^{k-1}\mathscr S
                                      \quad(1\le k\le4),\\
 d_{r\phi}&=-\beta_r P\mathscr S-\beta P\mathscr S_r,\qquad
 \ell_0=-2\beta\Pi\mathscr S .
 \end{split}\tag{SJ.31}
$$
Here $P=1-\Pi$, and both $P$ and $\Pi$ are contractions on $A^0$. The primitive has $A^0$ norm at most $1/4$. Hence every term of (SJ.31) has a direct complete positive bound from (SJ.12), (SJ.24) and (SJ.26). The fourth angular derivative of the drift uses only the third angular derivative of $\mathscr S$, so angular order three in (SJ.12) suffices.

Suppress the fixed branch label in the next display and write $R=r_\sigma$. The full off-diagonal coefficient is
$$
 B=-\frac{q_r}{2q}-\beta(1+R^2).
 \tag{SJ.32}
$$
Its radial and mixed derivatives are
$$
 \begin{split}
 B_r={}&-\tfrac12(q_{rr}/q-q_r^2/q^2)
                  -\beta_r(1+R^2)-2\beta RR_r,\\
 B_{rr}={}&-\tfrac12(q_{rrr}/q-3q_rq_{rr}/q^2+2q_r^3/q^3)\\
          &-\beta_{rr}(1+R^2)-4\beta_r RR_r
                              -2\beta(R_r^2+RR_{rr}),\\
 B_\phi={}&-2\beta RR_\phi,\\
 B_{r\phi}={}&-2\beta_r RR_\phi
                     -2\beta(R_rR_\phi+RR_{r\phi}),\\
 B_{\phi\phi}={}&-2\beta(R_\phi^2+RR_{\phi\phi}),\\
 B_{\phi\phi\phi}={}&-2\beta(3R_\phi R_{\phi\phi}
                                      +RR_{\phi\phi\phi}).
 \end{split}\tag{SJ.33}
$$
No radial derivative of the genuine response has been replaced by zero.

The first normalizer is $S_\sigma=-\sigma B_\sigma/(2h)$. In particular
$$
 \begin{split}
 (S_\sigma)_r
  &=-\frac{\sigma}{2h}\left((B_\sigma)_r-\frac{h_r}{h}B_\sigma\right),\\
 (S_\sigma)_{rr}
  &=-\frac{\sigma}{2h}\left((B_\sigma)_{rr}
       -2\frac{h_r}{h}(B_\sigma)_r+
                \left[2(h_r/h)^2-h_{rr}/h\right]B_\sigma\right).
 \end{split}\tag{SJ.34}
$$
The angular derivatives and $S_{r\phi}$ follow by differentiating only $B$ in the angular variable. Equivalently, their complete positive bounds are one half of the ordinary product of the $B$ derivative array and (SJ.29).

The exact remaining off-diagonal coefficient from SF.15 is
$$
 O_\sigma=-(B_\sigma)_\phi-\beta(R_\sigma)_\phi R_\sigma
                +c_\sigma(S_\sigma)_\phi-(S_\sigma)_r+S_\sigma d_\phi .
 \tag{SJ.35}
$$
The diagonal product $BS$ does not enter this off-diagonal row. The derivatives required for the second normalizer are
$$
 \begin{split}
 (O_\sigma)_\phi={}&-(B_\sigma)_{\phi\phi}
       -\beta\{(R_\sigma)_{\phi\phi}R_\sigma+(R_\sigma)_\phi^2\}\\
       &+c_\sigma(S_\sigma)_{\phi\phi}
             +2d_\phi(S_\sigma)_\phi-(S_\sigma)_{r\phi}
             +S_\sigma d_{\phi\phi},\\
 (O_\sigma)_r={}&-(B_\sigma)_{r\phi}
       -\beta_r(R_\sigma)_\phi R_\sigma\\
       &-\beta\{(R_\sigma)_{r\phi}R_\sigma
                              +(R_\sigma)_\phi(R_\sigma)_r\}\\
       &+(c_\sigma)_r(S_\sigma)_\phi+c_\sigma(S_\sigma)_{r\phi}
          -(S_\sigma)_{rr}+(S_\sigma)_r d_\phi+S_\sigma d_{r\phi}.
 \end{split}\tag{SJ.36}
$$
Consequently
$$
 Z_\sigma=-\frac{\sigma O_\sigma}{2h},\qquad
 (Z_\sigma)_\phi=-\frac{\sigma(O_\sigma)_\phi}{2h},\qquad
 (Z_\sigma)_r=-\frac{\sigma}{2h}
                    \left((O_\sigma)_r-\frac{h_r}{h}O_\sigma\right).
 \tag{SJ.37}
$$
These are the complete $Z=S_2$ coefficients of the same ordered normalizer, not an alternative scalar cancellation.

For the diagonal first coefficient retain
$$
 a_\sigma=-d_{\phi\phi}
       -\beta(r_\sigma)_\phi r_{-\sigma}
       +\frac{\sigma B_+B_-}{2h}.
 \tag{SJ.38}
$$
Its angular derivatives of orders zero, one and two are formed with the complete binomial rule. The $h^{-1}$ factor is radial. Thus they require exactly the angular derivatives of the state through order three already present in (SJ.12).

Finally form the full SF matrices and row
$$
 \begin{gathered}
 C=\operatorname{diag}(c_+,c_-),\quad
 A=d_{\phi\phi}\operatorname{Id}+B_\phi,\quad
 \mathbf r=(r_+,r_-)^t,\quad \mathbf a=(r_-,r_+),\\
 D=A+\beta\mathbf r_\phi\mathbf a,\quad K_{-1}=-D,\quad
 H_Z=CZ_\phi+C_\phi Z-Z_r .
 \end{gathered}\tag{SJ.39}
$$
All entry sums, both branches and all means are taken before an operator norm is claimed.

## 8. Angular bands, finite rows and both Sobolev windows

The exact degrees in the original moving angle are bounded as follows:

| Coefficient | Degree bound |
|---|---:|
| $r_\sigma,\mathbf r,\mathbf a$ and their ordinary radial derivatives | 96 |
| $d,C,B,S,S_r,S_{rr},A,D,K_{-1}$ | 192 |
| $a,O,Z,Z_\phi,Z_r$ | 384 |
| $H_Z$ | 576 |

Radial scalar reciprocals do not enlarge angular support. The products in (SJ.35)--(SJ.38), rather than a truncation of a large Fourier array, prove these bounds.

For a complete coefficient entry-sum $A^0$ bound $F^\#$ of degree at most $B_F$, the weighted multiplier norm in SF.31 has
$$
 m_s(F)\le (1+4B_F)^{|s|}F^\# .
 \tag{SJ.40}
$$
This uses a genuine already bounded Fourier $A^0$ sum. It is not applied to an arbitrary old pointwise supremum. For a saved field having only a supremum bound, the additional full coefficient-sum factor of SF.32 remains necessary.

Let $F^\#$ also denote the resulting unweighted entry sum for an ordinary multiplier. Complete positive finite-row fees for SF.11 and SF.17 can be chosen as
$$
 \begin{split}
 f_0={}&m_{4/3}(B)+D^\#/4+m_{4/3}(D)/4
                         +|\beta|\,\mathbf r^\#m_{4/3}(\mathbf a),\\
 f_1={}&S^\#\{C^\#+m_{4/3}(C)\},\\
 f_2={}&\tfrac14Z^\#\{C^\#+m_{4/3}(C)\},\\
 z_*={}&m_{4/3}(D)
                +|\beta|m_{4/3}(\mathbf r)m_{4/3}(\mathbf a_\phi).
 \end{split}\tag{SJ.41}
$$
For example, the second and third terms in $f_0$ bound respectively $(ID)\Pi$ and $\Pi DI$; the last uses $I\mathbf r_\phi=P\mathbf r$. The finite functional $\Pi DI$ uses the dual row $-ID$, so the same Sobolev window is paid. The last line follows from the exact complete row SF.13, including its mean pairing.

A sufficient $L^2$ bound for the complete $\mathcal N\partial_\phi$ used in SF.35 is
$$
 N_y^\#=|\beta|\,\mathbf r_\phi^\#
                  \left(2\mathbf a^\#+\mathbf a_\phi^\#/4\right).
 \tag{SJ.42}
$$
This uses the three exact terms of SF.12. It does not remove the independent $\gamma$ mean rank from the full error system SF.7; the latter is already part of the ST receiver.

Substitute (SJ.40)--(SJ.42) and the complete arrays of Section 7 in SF.33--36. Keep its actual
$J_s=268435456$, the full $F_T,\mathcal F_J$ maps through $J_s+575$, and their dual-row derivative fees. No finite block is deleted because the input label is at least 97. The two primitives and all intermediate Sobolev exponents in SF.34 remain in their original order.

## 9. True characteristic coefficients and the ordinary source integral

Read the successful WX full-family bounds for every shorter interval and both orientations:
$$
 \|\chi_\phi\|_\infty\le M,\quad
 \|\chi_{\phi\phi}\|_\infty\le F,\quad
 \|\chi_{\phi\phi\phi}\|_\infty\le G .
 \tag{SJ.43}
$$
These are the actual WX balls, not a new ray integration. Read its separate ungauged leading norms $v_0,v_{-4/3}$ in the reverse cut-to-waist direction. The radial $n_g$ factors are not incorporated into these leading norms.

If $A_{\sigma,k}^\#$ is the new complete angular derivative bound for $a_\sigma$ from (SJ.38), the exact density rule $\mathfrak b_\sigma=U_{\chi_\sigma}a_\sigma$ gives
$$
 \begin{split}
 B_{\sigma,0}^\#&=M A_{\sigma,0}^\#,\\
 B_{\sigma,1}^\#&=F A_{\sigma,0}^\#+M^2A_{\sigma,1}^\#,\\
 B_{\sigma,2}^\#&=G A_{\sigma,0}^\#
                  +3MF A_{\sigma,1}^\#+M^3A_{\sigma,2}^\# .
 \end{split}\tag{SJ.44}
$$
Each is a pointwise derivative bound on the true transported, generally nonpolynomial coefficient. The distinction from (SJ.40) is essential.

Over the exact refined old-cell partition of $[0,r_c]$ form the new positive ordinary integrals
$$
 C_{\sigma,k}^\#=\sum_\lambda |I_\lambda^{\rm row}|
                \sup_{I_\lambda^{\rm row}}B_{\sigma,k}^\# .
 \tag{SJ.45}
$$
These bound the derivatives of $\mathfrak c_\sigma(r)=\int_{r_c}^r\mathfrak b_\sigma(s)\,ds$ on every shorter interval. The actual ordinary radial lengths occur once; no old profile-weighted integral is transferred.

Use SF.38a--e, including both primitive ranks, to bound
$m_s(\mathfrak b),m_s(\mathfrak c),f_\psi,\mathcal D_V$.
In particular the complete derivative-to-Wiener bound
$3\sum_\sigma(B_{\sigma,0}^\#+2B_{\sigma,1}^\#+B_{\sigma,2}^\#)$
is available for the required $|s|\le4/3$, and the same expression with $C_{\sigma,k}^\#$ handles $\mathfrak c$.

The successful FA conclusion is read at its exact final source and manifest identity. Its
`complete_SF26_Kc_minus_corrected_Bfree1_divided_by_ng_once`
is already the complete $K_c^-$ in SF.26; $n_g(r_c)^{-1}$ is not applied a second time. Its
`complete_same_TN_forward_L2_times_free_cut_upper`
already includes the forward TN factor in SF.30; that factor is not applied a second time either.

With these literal inputs, use the full formula SF.38 to form a rowwise bound $f_{\rm app}^\#$ for the complete source SF.28, including
$-Z_yT_JV\mathcal B_c$. Its new ordinary $L^1_r$ bound is
$$
 F_{\rm app}^\#=\sum_\lambda |I_\lambda^{\rm row}|
                        f_{{\rm app},\lambda}^\# .
 \tag{SJ.46}
$$
A global value of every $C_{\sigma,k}^\#$ from (SJ.45) may be used in each row of (SJ.46). This is a safe complete budget even though it is not the sharpest possible partial-integral implementation.

## 10. Every genuine coefficient interface remains a source

At a reference interface qualified by the original matching convention in SF Section 9, the repaired $u,v$ and their angular derivatives are continuous. The same actual intrinsic functions give continuous
$\eta,\beta,q,q_r$ and therefore continuous $h,B,S,C$. This is the exact lower-coefficient matching used in SF.42, rather than a comparison of rounded endpoint balls. Radial derivatives of the repaired finite functions need not match.

The following exact jump identities isolate the terms which can remain. A bracket denotes right value minus left value in the same outward coordinate. From (SJ.34)--(SJ.37),
$$
 [O_\sigma]=-[ (S_\sigma)_r],\qquad
 [Z_\sigma]=-\frac{1}{4h^2}
              \left([(B_\sigma)_r]-\frac{B_\sigma}{h}[h_r]\right).
 \tag{SJ.47}
$$
The sign is independent of $\sigma$. The complete radial jumps in this formula are
$$
 \begin{split}
 [h_r]&=q[\eta_r],\\
 [(B_\sigma)_r]
   &=-\frac{[q_{rr}]}{2q}
      -[\beta_r](1+r_\sigma^2)
      -2\beta r_\sigma\{[u_r]+\sigma q[v_r]\},\\
 [\eta_r]&=-m[\gamma_r]-\gamma[m_r].
 \end{split}\tag{SJ.48}
$$
They use only the stated continuity of the lower coefficients. In particular the $q_r^2/q^2$ term in $B_r$ is continuous and cancels; the $q_{rr}$ jump does not disappear merely because two scalar interval enclosures overlap.

For complete one-sided budgets $J_{q2},J_{\beta1},J_{\gamma1},J_{u1},J_{v1},J_{m1}$ of the displayed jumps, put
$$
 \begin{split}
 J_\eta&=M_0J_{\gamma1}+\gamma_0^\#J_{m1},\\
 J_{B,\sigma}&=\frac{J_{q2}}{2q_-}
        +J_{\beta1}(1+(r_\sigma^\#)^2)
        +2b_0r_\sigma^\#(J_{u1}+q_+J_{v1}),\\
 J_{Z,\sigma}
   &=\frac{J_{B,\sigma}+B_\sigma^\#J_\eta/\eta_-}
                       {4h_-^2}.
 \end{split}\tag{SJ.49}
$$
A sum of the two one-sided absolute derivative budgets is always an admissible bound for each jump. Their exact zero may be used only when the original coefficient definition proves matching at that particular interface. This applies separately to the intrinsic terms $[q_{rr}],[\beta_r],[\gamma_r]$ as well as the physical mean term. No common-germ assertion or smoothness of an unrelated reference silently removes them.

An artificial cell cut inside one unchanged smooth piece produces no new jump. For a conservative audit it may instead be assigned the sum of its one-sided derivative bounds; that only enlarges the total positive impulse bound. Either implementation must distinguish original physical joins from refinements, and must not infer global distributional second derivatives from (SJ.12).

The actual SF interface source is precisely its two-primitive impulse
$$
 [\mathbb Y_{\rm app}]_\lambda
 =\binom{P(1+A_J)P_{J_s}[Z]I^2P_{J_s}
                        V\mathcal B_c}{0}.
 \tag{SJ.50}
$$
Accordingly its norm is bounded by the SF.43 recipe using the complete sum of $J_{Z,\sigma}$ in (SJ.49). It is added as an impulse, with no radial length. The whole error system still retains the actual two mean coordinates. No identity in (SJ.47) sets the propagated mean source to zero.

If a proposed join fails the lower-coefficient continuity qualifications needed for (SJ.47), that join is not processed by this specialized two-primitive formula. The consumer must stop that conclusion or retain the more general complete SF interface operator. A failed qualification is not relabelled as a successful two-primitive impulse.

## 11. Complete new conclusion and minimal reader scope

After all exact-domain and positive-denominator gates, the genuinely new scalar conclusion is
$$
 C_{\rm SF}=
 G_{\rm cut}\,E_c^{\rm dens}
 +G_{\rm src}\left(F_{\rm app}^\#+\sum_\lambda j_\lambda^\#\right),
 \tag{SJ.51}
$$
where both receiver constants are the literal successful ST quantities and $j_\lambda^\#$ is the complete impulse fee from SF.43. This is a bound for the difference between the same exact homogeneous free continuation and its actual SF first-symbol trial, in the physical waist density space $L^2_{\ne0}\oplus\mathbb C^2$, for input $\mathcal X^{-4/3}_{97}$.

It does not turn an individual order-zero trial into a strong map. It does not replace the later true waist receiver, the common-root right gauge, the actual incoming inverse, or the finite border. The full AW/PC contribution, independent external means and boundary ports remain in their already specified places.

The smallest input plan consists of the following read-only objects.

| Input | Use in this new consumer |
|---|---|
| Exact original body parts through the body cell containing $r_c$ | Read saved $a,\gamma,\beta,K,s$ ordinary jets and exact piece/interval labels; do not evaluate an old target |
| Original body manifest and two small producer texts | Lock the full parameter, complete mean, row and piece-containment identities |
| Centre/response definition proofs and D full-state estimate | Qualify the repaired cubics and the complete $7,6,19,83$ bounds |
| Accepted SP/ST/RR small conclusions | Read the exact full-interval positive-log budget, root cut bound and two upper covers; form (SJ.25b), then read the fixed family, endpoint/mean data and source receiver |
| Accepted WX execution and source identity | Read actual shorter-flow $M,F,G$ and the separate leading-density windows |
| Accepted FA execution and full scientific conclusion | Read the corrected $K_c^-$ and the already forward-restored cut error |
| SF and this contract | Bind the complete algebra, Sobolev windows, finite maps, genuine interfaces and formula (SJ.51) |

The old body archive and member identities must be verified in full before their temporary restoration. If an old receipt did not retain a member byte length, the new manifest says so and verifies the original whole archive and complete member SHA256, then records the actual restored length. It does not invent an old size. No scientific arrays are published.

The new temporary audit retains every exact qualified polynomial interval, every old row restriction, every original whole-jet identity, the full selected intrinsic derivative arrays, all positive coefficient budgets, each genuine interface contribution, and each ordinary source contribution. The public small conclusion retains the complete aggregate bounds, exact scope, actual strict gates, all literal reused objects or their pinned full identity, and hashes of the temporary audit.

Only public Actions evaluates these new numerical expressions. A complete successful new stage is saved atomically and emitted before Git publication. A publication failure does not authorize recomputing that successful mathematics.

## 12. Primary evidence and current successful scalar inputs

| Primary text or complete receipt | Git blob | UTF-8 bytes | SHA256 |
|---|---|---:|---|
| SF exact defect contract | `0f93e925d354133675b84ffeaa959a0b58d339a0` | 35,289 | `add091118ef1af71bc8c4be275742d4124a076d6cf2ebaf00d35c66f8348f2b4` |
| Exact continuous centre proof | `7338254acdfdab61bd22124d964a4231791b9f7f` | 11,484 | `a39fcfa2b7ca6f83cd9fadcc1987afe86f3364830848de78d2401469d7ce9f44` |
| Complete physical response proof | `2bc958ab42db0c4936a717e54ff3b43f5001bdf5` | 8,753 | `2b7d6080dc7fdac0bd5c557b71f3e7ec1eb5436a14d45a5a762e1b548a9e20f1` |
| D exact parameter identities and full-state bounds | `c85b66866103ea021cebbc050ccead214d4cf9d9` | 15,214 | `92fd222bbcc4495cce091cedee2628f83d014be23a40328a7292d47616621635` |
| Body correlated row producer | `3af195a36ccb30630dbfcab0caef3564738ab169` | 13,043 | `1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07` |
| Original partition and containment producer | `f514bb81ec6c24e2035c3b08b96520b4c1e243d5` | 29,107 | `9674f5f6b9d4ad95d7d87fb22b2ec4c8fc3cad136b78afed677343c2510bb6df` |
| Original body input manifest | `b4a96180d2e1abca2ae90e7ba363e6a0c78149d9` | 31,806 | `c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784` |
| ST actual execution, 43757644616/1 | `94eb4c7d643edc33f696d101753e4d23a7936a26` | 47,282 | `b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637` |
| WX actual execution, 43763424840/1 | `5121a599896025d90e2861450756a256aaba659d` | 43,753 | `e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12` |
| WX actual proof | `3f8a48d73f92a9f819e580fe49dc4fabaf77c76c` | 26,199 | `f5554084bedb32a14f0bf52382a72a0987dff3019544d71af9c769d1c90e502f` |
| FA actual scientific conclusion, 43763658978/1 | `2001f4e2eeece1cda56b18b90dccab04b7f6d336` | 35,718 | `2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2` |
| FA actual execution | `bef7897d1b501751b8b29bbb82a46bdb05496d28` | 17,821 | `735c8053b56cc240e3fdfb050d95ef2cbb17c26a376aa4132530d50687474c0a` |

The last two science chains are successful and frozen. The new work in this note is the complete radial/mixed derivative closure, the full-family intrinsic derivative correction, and the resulting SF source and genuine-jump scalar sums. Their actual numerical verdict remains the task of the new, separately identified consumer.
