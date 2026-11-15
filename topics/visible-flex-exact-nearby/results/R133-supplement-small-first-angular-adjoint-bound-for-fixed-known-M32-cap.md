# R133 supplement: a small first-angular adjoint bound for the fixed known M32 cap

2026-11-15. Independent analytic consequence of the already paid complete
physical cap, its true exterior derivative, and its residual Hessian.
No target, residual, kernel, finite matrix, or numerical enclosure is recomputed.

The fixed object is the exactly continuous centre with definition SHA256
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47,
at the original exact $\eta_0,\delta=0$, on $[L_c,R]=[9/10,25/8]$.
The exterior background is the original **known** $f_B$ satisfying
$\|f_B\|_{\dot A^2_\sigma}\le2^{-60}$ for $\sigma\ge1/16$.
This is the background domain in
[the original regular exterior](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md)
(S.1), with the true $C_R$ inverse and its independent means.

The result is a bound for the adjoint rows of the **old known cap operator**.
It does not assert smallness of an unknown composition operator minus the
identity, and it does not transfer this angular commutator to arbitrary rough
$f_B$ backgrounds. The new exact cap may still be compared with this old cap
by its separately proved same-physical-angle comparison.

## 1. Exact operator, measures, and the output mean

Use normalized circle measure, physical frequencies $k\in4\mathbb Z$, and
$\Lambda=(1-\partial_\theta^2)^{1/2}$. The two-component cap module is
$$
 \|x\|_{\mathfrak M}
 =\left(\sum_k\sup_r|x_{B,k}(r)|^2\right)^{1/2}
  +\left(\sum_k\sup_r|x_{C,k}(r)|^2\right)^{1/2}.
 \tag{H.1}
$$
In particular evaluation at either actual endpoint maps this space to
$L^2_\theta\oplus_1L^2_\theta$ with norm at most one.

Let $\widetilde G$ be the complete residual-sensitive physical cap inverse in
[the full-frequency moving interface](R133-supplement-full-frequency-moving-cap-boundary-and-Poisson-interface.md)
(P.10)--(P.13). Its input under consideration is the actual nonmean physical
$C$ trace $c$ at $L_c$, and its other independent source and endpoint inputs
are zero. Write
$$
 \mathcal P c=\widetilde G[c_{\ne0}(L_c)=c],\qquad
 \mathcal Kc=\bigl((\mathcal Pc)_B(L_c),\,
                         \langle(\mathcal Pc)_C(L_c)\rangle_\theta\bigr)
             =:(K_Bc,K_C^0c).
 \tag{H.2}
$$
The scalar $K_C^0$ is the operator called $K_0$ in that original interface.
Thus $\mathcal K$ denotes the complete pair, not that scalar alone.

The output space and its dual are
$$
 \mathcal Y=L^2_\theta\oplus_1\mathbb C,\qquad
 \mathcal Y^*=L^2_\theta\oplus_\infty\mathbb C.
 \tag{H.3}
$$
The pairing is the actual physical $L^2$ pairing plus the scalar pairing.
The adjoint takes values in $L^2_{\theta,\perp}$; projection to that input
space occurs only after the complete pairing. Neither the $C$ mean output
nor its dependence on all input modes is removed.

At the real fixed centre, the relevant restriction has odd $B$ and even $C$.
To differentiate by angular translation we first construct an auxiliary
full-$4\mathbb Z$ operator on the same physical measures. The full mean
extension below agrees with (H.2) on this reflection sector by uniqueness.
It is not a claim that the original raw moving equation has an all-direction
inverse without its separate phase row.

## 2. The known-background shift uses the original small exterior sphere

Set
$$
                         h=\frac1{256}.
 \tag{H.4}
$$
Translate every **known coefficient and known exterior background** in the
physical angle by $z$, $|z|\le h$. The unknown physical input remains an
ordinary $L^2$ function in the fixed real variable. No complex value of that
unknown input is taken.

[The complete physical cap-tail theorem](R119-supplement-complete-physical-cap-tail-Sobolev-Schur-with-all-mean-charges.md)
(L.5) proves, on the larger strip $|\operatorname{Im}z|\le1/128$,
$$
 \|Z_z\|_{A^0}<10^{-12},\qquad
 \|(f_B)_z\|_{\dot A^2}<2^{-60}.
 \tag{H.5}
$$
Its repaired-centre transfer (L.28) and the following paragraph retain
these same bounds: the actual repaired endpoint correction is less than
$4.970\,10^{-19}$ in $A_{1/64}$, while the original shifted endpoint
estimate is less than $7.7\,10^{-13}$. The true mean is separately retained.

For the present purpose one can use (H.5) in the **first** original sphere
of
[the complete Hilbert exterior](R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md)
(L.6)--(L.11). There is no need to replace it by the larger convenient
sphere later used in the cap-tail theorem. With
$$
 r_Z=10^{-12},\quad r_B=2^{-60},\quad
 F=10(r_Z+r_B)+r_B,\quad
 J_f=\frac9{1-36\cdot2^{12}F},
 \tag{H.6}
$$
the same square-zero Hilbert module proves
$$
 \|D_Zd_z\|<5.898255\,10^{-6},\qquad
 |D_Z(c_0)_z|<7.372818\,10^{-7}.
 \tag{H.7}
$$
These are true derivatives of the full $C_R$ graph. Their proof includes
the complete holonomy small root, finite-length reflection, and all
ordinary physical mean functionals. The positive comparison fee
$\epsilon_{\rm old}+2^{-512}$ remains in the Robin column.

All background bounds needed for the physical body are joint Wiener
bounds on width $1/64$ in
[the continuous-centre physical theorem](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md),
its table after (C.5) and (C.8). Thus they remain unchanged after this
shift. In particular
$$
 \|Q_{B,z}\|_{\mathscr A_0}<.039196064,\qquad
 \|Q_{C,z}\|_{\mathscr A_0}<.051432066.
 \tag{H.8}
$$
The actual radial reference and all its complete ordinary, divergence,
jump and mean kernels are unchanged. Substituting (H.7)--(H.8) into
[the original all-mode Green theorem](R133-supplement-actual-final-all-mode-physical-cap-Green.md)
(C.18)--(C.28) therefore keeps its complete contraction below $.820523$,
its resolvent below $5.571744$, and its inner-$c$ pair gain below
$13.316116$.

The full signed auxiliary space must also keep the $B$ mean.
[The true $B$-mean theorem](R133-supplement-complete-fourfold-periodic-cap-long-graph-with-true-B-mean.md)
(B.17), whose $L^2$ square-zero proof is given immediately before (B.12),
gives
$$
                   \|D_Z(b_0)_z\|<2^{-49}.
 \tag{H.9}
$$
The original independent outer-$B_0$ gain is $5.571744$. Closing this
additional row consequently multiplies each previous source and port
gain by at most
$$
           \bigl(1-5.571744\cdot2^{-49}\bigr)^{-1}<65/64.
 \tag{H.10}
$$
This is an actual scalar feedback, not a parity deletion. The $C$ mean
was already included in (H.7). On the real reflection sector, the
complete $B$-mean response has its exact parity value and this auxiliary
construction reduces to the original operator.

## 3. Complete complex-shift Hessian, including the gauge mean

Let $R_{\rm mov}$ be the actual continuous-centre residual on each true
cell. Its exact moving Fourier support is $|j|\le96$, hence physical
angular frequency at most $384$. Its complete stored $A^0$ and
inhomogeneous $A^1$ envelopes include the repair. No coefficient of this
residual or of its first angular derivative is replaced by a truncated
physical Fourier series.

The already paid inverse-angle displacement is
$$
          \|\phi(\theta)-\theta\|_{\mathscr A_{1/64}}
                         <h_*:=.003774146.
 \tag{H.11}
$$
Consequently, for the translated known residual
$R_{\rm mov}(\phi(\theta+z))$,
$$
 384(h+h_*)<3,\qquad
 e^{384(h+h_*)}<21,\qquad e^{384h}=e^{3/2}<5.
 \tag{H.12}
$$
The first estimate bounds the physical $A^0$ and first-derivative
envelopes by $21$ times the corresponding original moving envelopes.
The physical derivative uses the same already paid $\phi_\theta$ bound.
For the joint divergence coefficient in the original Hessian certificate,
the factor $e^{4jh_*}$ was already included, so its additional shift
cost is at most $5$, also at most $21$.

Every nonresidual coefficient used here has an original $\mathscr A_{1/64}$
bound: $u,v,B,C,B_\theta,C_\theta$, their measure bound, and the inverse
differential coefficients. Such bounds also hold at $\theta+z$ with the
same numerical values. In particular no second angular derivative of
the residual and no derivative of the unknown is requested.

For clarity, the complete original local Hessian budgets in
[the local triangular certificate](R133-supplement-local-triangular-cap-Hessian-and-trial-source.md)
(L.7), (L.10)--(L.11) are positive sums of terms linear in the two
residual envelopes or their first angular derivative:
$$
 \begin{gathered}
 E_A=C_*R_{V,A}/4,\qquad
 E_\infty=\pi C_*r_{V,0}/8,\qquad E_1=2C_*r_{V,0},\\
 t_B=C_*r_{U,0}+B_*C_*r_{V,0},\quad
 t_C=C_*^2r_{V,0},\\
 b_*=C_*^2r_{V,0}/4+2C_*E_\infty,\\
 Z_{BB}=t_CV,\quad
 Z_{BC}=t_CH_C+
       (C_*t_B+B_*t_C+t_{B,1}C_*/4+B_1b_*)H_2,\\
 Z_{CC}=(2C_*t_C+t_{C,1}C_*/4+C_1b_*)H_2 .
 \tag{H.13}
 \end{gathered}
$$
The displayed $E_\infty$ uses the real-circle primitive kernel on a
complex-valued coefficient, which has the same absolute kernel bound.
It does not apply a real-variable positivity claim at a complex angle.

The arbitrary-direction angular gauge is
$$
 E_h=I_\theta(Ch_2)-m\langle C I_\theta(Ch_2)\rangle_\theta,\qquad
 \|E_h\|_2\le \frac{J_*C_*}{4}\|h_2\|_2,\qquad J_*<33/32,
 \tag{H.14}
$$
by
[the full normalized gauge](R133-supplement-complete-normalized-angle-gauge-and-residual-Hessian.md)
(G.23)--(G.26). Both mean pairings in its complete Hessian remain.
At the original real centre $C$ and $R_{{\rm mov},2}\circ\phi$ are even,
so the weighted constant in $E_R$ is exactly zero. The same identity
holds for their simultaneous known translation: the zero Fourier
coefficient of a translated complete product is unchanged. Thus one
may translate the original $e=I_\theta(CR_2)$ while keeping the full
directional expression (H.14).

The bound $J_*$ in (H.14) continues to the complex shift by the original
joint bound for $mC-1$; it is not interpreted as a complex change-of-measure
formula. The reconstruction and the triangular majorant remain precisely
those in (G.25). Since $21(33/32)<22$, the full translated Hessian source
majorant is at most $22$ times the original one, cell by cell.

Write $H_z$ for this actual residual Hessian and $G_z$ for the physical
inverse after the $B$-mean closure (H.10). The already paid
$\chi_H=.003840162$ is the response to the **complete** divergence and
ordinary sources, with all real cells and means. Multiplying each of
those inequalities gives
$$
       \|G_zH_z\|_{\mathfrak M\to\mathfrak M}
       \le(65/64)\,22\,\chi_H<.09 .
 \tag{H.15}
$$
In particular the divergence term is still
$\partial_\theta(-e x)$ with its original module unit, and the
remaining term $e_\theta x+Zx$ still has its original ordinary-source
unit and true radial integration. No source is changed into another
space.

The full shifted residual-sensitive inner solution therefore exists and
satisfies
$$
 \|\mathcal P_z\|_{L^2_\perp\to\mathfrak M}
 \le \frac{13.316116(65/64)}{1-.09}<16,\qquad
 \|\mathcal K_z\|_{L^2_\perp\to\mathcal Y}<16 .
 \tag{H.16}
$$
The complete pair norm is the sum in (H.1); no factor $\sqrt2$ is inserted
into the feedback estimate. All independent source columns used to
construct $G_z$ remain available, although (H.16) considers only the
inner nonmean-$C$ input.

## 4. The bounded commutator and the actual adjoint domain

The family in (H.16) is holomorphic as a family of bounded operators.
Indeed its coefficient and exterior maps are holomorphic in the known
translation, and the complete physical and Hessian Neumann series
converge uniformly on a slightly larger disk than $|z|\le h$.
All the strict margins above and the original larger coefficient strips
give that extra neighborhood.

For real $z$, let $U_z$ be angular translation and let
$U_z^{\mathcal Y}(b,a)=(U_zb,a)$. Uniqueness of the complete problem gives
$$
               \mathcal K_z=U_z^{\mathcal Y}\mathcal K U_{-z}.
 \tag{H.17}
$$
This real identity is enough. It can first be checked on finite Fourier
inputs and then completed in $L^2$. It is not the definition of an
unbounded complex translation acting on the unknown input.

Put
$$
 D=\partial_\theta,\qquad D_{\mathcal Y}(b,a)=(Db,0).
$$
Cauchy's estimate on (H.4) and (H.16) gives the bounded extension
$$
 \mathcal C:=D_{\mathcal Y}\mathcal K-\mathcal KD,\qquad
          \|\mathcal C\|_{L^2_\perp\to\mathcal Y}\le4096.
 \tag{H.18}
$$
Both derivatives have their usual distributional meaning. Taking the
actual Hilbert pairings on finite Fourier functions, then taking
closures, gives
$$
     D\mathcal K^*g=\mathcal K^*D_{\mathcal Y}g+\mathcal C^*g,
 \qquad g=(b,a),\ b\in H^1_\theta,\ a\in\mathbb C.
 \tag{H.19}
$$
The sign follows because each angular derivative is skew adjoint.
The scalar derivative is zero; its nonconstant adjoint response is
still controlled by the $\mathcal C^*g$ term. Thus the complete mean
column has not disappeared.

With the norm in (H.3),
$$
 \boxed{\quad
 \|\mathcal K^*g\|_{H^1_\theta}
 \le16\|D_{\mathcal Y}g\|_{\mathcal Y^*}
        +(4096+16)\|g\|_{\mathcal Y^*}.
 \quad}
 \tag{H.20}
$$
Here $\|u\|_{H^1}\le\|u\|_2+\|Du\|_2$ was used once.
At the real reflection centre, the full auxiliary operator intertwines
the appropriate reflection actions. Its adjoint applied to an odd
$B$ test and the scalar $C$-mean test has even nonmean output and agrees
with the adjoint of the original restricted operator (H.2).

## 5. The actual moving 97 tests, without a dimension factor

At the true inner cut retain the exact maps
$$
 \Theta_\phi=v/m,\qquad Vf=f\circ\phi,\qquad
 \mathcal Sg=v(g\circ\Theta),\qquad \mathcal S^*=mV .
 \tag{H.21}
$$
This adjoint includes the normalized change of measure. For example
$$
 \langle f,\mathcal Sg\rangle_\phi
                       =\langle mVf,g\rangle_\theta .
$$
The sign of $m$ is retained; the norm bounds use $|m|$.

Let
$$
 f(\phi)=\sum_{j=1}^{96}\lambda_j\sqrt2\sin(4j\phi),
 \qquad a=\lambda_{97},\qquad
 g=(mVf,a).
 \tag{H.22}
$$
The finite test coefficients have their Euclidean norm
$\|\lambda\|_2^2=\|f\|_2^2+|a|^2$.
The complete original measure bounds are
$J_\phi<1.015211829$, $J_\theta<1.015446803<33/32$, and
$|m|<5.8639401366$. Consequently
$$
 \|mVf\|_2\le|m|\sqrt{J_\phi}\|f\|_2<6\|f\|_2,\qquad
 \|g\|_{\mathcal Y^*}<6\|\lambda\|_2.
 \tag{H.23}
$$
Using the same physical derivative and the actual finite test support,
$$
 \|\partial_\theta(mVf)\|_2
 \le6J_\theta\|f_\phi\|_2
 <\frac{25}{4}\,384\,\|f\|_2
 =2400\|f\|_2 .
 \tag{H.24}
$$
There is no finite-support assertion about $Vf$ or about the eventual
adjoint output. Only the moving test $f$ in (H.22) is finite.

Substitution into (H.20) proves the simultaneous 97-column estimate
$$
 \boxed{\quad
 \|\mathcal K^*(mVf,a)\|_{H^1_\theta}
 \le\bigl(16\cdot2400+4112\cdot6\bigr)\|\lambda\|_2
 =63072\|\lambda\|_2<2^{16}\|\lambda\|_2 .
 \quad}
 \tag{H.25}
$$
It is an operator bound for every linear combination of the columns.
No Hilbert--Schmidt replacement or extra $\sqrt{97}$ is needed.
The scalar $a$ is the independent physical $C$-mean output test.

For comparison, physical tests of frequency at most $384$ in the
$B$ component, together with the same mean test, obey the simpler
bound $16\cdot384+4112<2^{14}$. The actual moving tests require
(H.21)--(H.25); these two input conventions are not interchanged.

## 6. What this permits in the parameter bridge

If a known angular coordinate varies, the adjoint finite boundary rows
may now be differentiated using (H.25) and the **actual** angle variation,
density, multiplier, and primitive formulas. This can pay a finite-row
operator difference without asserting
$\|C_\Phi-I\|_{L^2\to L^2}\ll1$.

The theorem retains the exact input $c=P_{\ne0,\theta}C(L_c)$ and the
output $(B(L_c),C_0(L_c))$. If a later boundary operator includes
$H_B,H_C,\mathcal S$, their background variations must still be kept in
their true order. A scalar normalization such as $m^{-2}$ in the moving
mean row is also separate and must be differentiated with its actual
mean. It is not silently absorbed into (H.25).

The physical bound comparing the new exact cap and this old cap, the
small intrinsic parameter interval, the full core high block, and the
actual core $H^1/H^{8193}$ trace gates remain their own statements.
This small adjoint bound supplies the missing known-operator angular
regularity; it does not settle those other gates.

### Exact primary identities

The following are the small public text blobs used for this proof:

| Primary | Exact blob |
| --- | --- |
| Complete physical cap-tail and repaired transfer (L.5), (L.28) | de57e6ac2339e046051f25e71c9d559c3a0aa480 |
| Original full Hilbert exterior (L.6)--(L.11) | a7ff7d2ca24df41ccd242ff9799b21fdcab2aec0 |
| Original complete physical Green (C.18)--(C.28) | f6c55d479ad3959bd71b12c7555c0189d6c53065 |
| Repaired coefficients and complete residual identity | e0a324d74373ff680cb77296dc1c58458a27cf2d |
| Local triangular Hessian source majorant | 7b921ecb49f7977d18a47876cf1b2b5743d1ae94 |
| Full normalized gauge (G.23)--(G.26) | 2cc73e02e2a02496fe075405b14e9b59ff8de4b4 |
| Complete true $B$ mean (B.17), (B.28) | 89761027f936b36eb012adf2ec593b70be3ce90d |
| Actual moving boundary operator (P.10)--(P.14) | 72a11fc332edf8a95c3b58bc46b0c93a0499f73d |
