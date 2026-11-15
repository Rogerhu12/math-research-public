# R133 supplement: wide-collar half trace with an independent narrow high-order domain

2026-11-15, visible-exact / tail_connector.

**Analytic conclusion.** The projected-principal energy estimate may use the full positive collar while the high-order interpolation bound is supplied only at the same interior cut by a separately proved narrow-collar result. A triangular cutoff removes the need for an inner plateau in the single half-trace argument. On the actual interval $[17/20,19/20]$ its derivative bound is $20$.

This statement does not enlarge any old factorial-collar domain. It preserves the completed NR and MA data and introduces only a new, explicitly identified moving-mean restriction and positive recombination of their saved bounds. No unknown body norm, matching condition, or low curvature entry is inferred from a coefficient table.

## 1. One state on two different radial domains

Use the exact notation and units of the published E, LT, PE, MC, MA and NR supplements:

- [E: the real positive-collar equation and complete mean](R133-supplement-positive-collar-energy-and-residual-sensitive-first-angular-cut-trace.md).
- [LT: finite, middle and infinite trace bands](R133-supplement-finite193-middle-band-and-infinite-collar-trace.md).
- [PE: projected-principal energy](R133-supplement-projected-principal-collar-energy-and-sharper-three-band-trace.md).
- [MC: the raw-response mean identity](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md).
- [MA: the five restored narrow high-order domains](R133-supplement-actual-raw-mean-fee-and-restored-high-collar-domain.md).
- [NR: the completed two restrictions and all trace coefficients](R133-supplement-actual-saved-nonmean-restrictions-and-three-band-trace-budgets.md).

Fix $c=9/10$, a real selected parameter $|\delta|\le d=10^{-10}$, and the same continuous reference $Q^\delta$ as those results. On this collar the intrinsic bump is absent, so the radial coefficients are the same actual $(\beta,G,K)$ used in E. Put
$$
 I_{\rm w}=[c-\ell_-,c+\ell_+],\qquad
 z=P(Q-Q^\delta),\qquad
 P=\operatorname{diag}(K^{-1/4},K^{1/4}).
 \tag{WC.1}
$$
The wide hypothesis is one real, continuous, two-sided $H^1$ state $Q$ on $I_{\rm w}$, solving the full ordinary equation, and satisfying
$$
 \|Q-Q^\delta\|_{C^0(I_{\rm w}\times S^1)}\le\rho_{\rm w}.
 \tag{WC.2}
$$
Every norm is in the normalized original moving angle, and radial integration uses actual $dr$. For the new scalar tables one may take $I_{\rm w}=[17/20,19/20]$ and $\rho_{\rm w}=10^{-4}$ or any of the five smaller MA radii. These are conditional state hypotheses, not newly established bounds on a core correction.

Independently, choose one of MA's five radii $\rho_{\rm n}$ and assume that the restriction of this very same state to
$$
 I_{\rm n}=[589819/655360,589829/655360]
 \tag{WC.3}
$$
satisfies that restored MA hypothesis. Its conclusion is the cut bound
$$
 \|(Q-Q^\delta)(c)\|_{H^{8193}}\le 2^{377903}.
 \tag{WC.4}
$$
The wide and narrow radii need not be equal. Neither (WC.2) with a larger radius nor a mere one-sided cap state implies the narrow hypothesis. Conversely, the narrow hypothesis says nothing about the state outside $I_{\rm n}$.

The ordinary wide energy estimate below does not require a wide factorial barrier. The bound (WC.4) is used only for the same function at the same cut.

## 2. A single triangular cutoff

Let $\chi$ be the continuous function that is linear from $0$ to $1$ on $[c-\ell_-,c]$ and linear from $1$ to $0$ on $[c,c+\ell_+]$. Then
$$
 0\le\chi\le1,\quad \chi(c)=1,\quad
 \chi(c-\ell_-)=\chi(c+\ell_+)=0,\quad
 |\chi'|=\ell_-^{-1}\ \text{or}\ \ell_+^{-1}.
 \tag{WC.5}
$$
It is in $W^{1,\infty}$. Its first weak derivative has a jump, but contains no point mass. No second derivative of $\chi$ is used.

Write $H_J=P_{|j|>J}$ and $\Pi_J=I-H_J$. With the actual real drift and speed of E, set
$$
 {\cal L}_{H_J}=\partial_r-H_Jd_{\rm act}\partial_\phi
                         +aJ_0\partial_\phi,\qquad
 a\ge a_->0,\quad |a_r/a|\le L,\quad |d_{\rm act}|\le d_+ .
 \tag{WC.6}
$$
The projected principal pairing is exactly PE.2--PE.6. For $u=\chi H_Jz$, the two radial boundary values are zero; the two contributions at $c$ cancel because $u$ and $a$ are continuous. Thus no additional interface term arises from the corner of the triangular cutoff.

Let $Z_{H,\pm}$ be the $L^2$ norms of $H_Jz$ on the two half intervals. The cutoff source is bounded by the full two-sided expression
$$
 C_{\chi,J}
  =\left(\ell_-^{-2}Z_{H,-}^2+
                     \ell_+^{-2}Z_{H,+}^2\right)^{1/2}
  \le\kappa_\chi Z_H,\qquad
 \kappa_\chi=\max(\ell_-^{-1},\ell_+^{-1}).
 \tag{WC.7}
$$
In particular, on $I_{\rm w}=[17/20,19/20]$,
$$
                    \kappa_\chi=20 .
 \tag{WC.8}
$$
The old $262144$ was a derivative bound for a much narrower cutoff. The value $40$ on the full wide interval would retain an unnecessary plateau. Among cutoffs with these endpoint values, the triangular cutoff attains the minimum possible uniform derivative bound.

For any projected source bound $E_J$ that includes (WC.7), the PE energy gives
$$
 \|u_\phi\|_2\le c_p E_J,\qquad
 \|u_r\|_2\le c_r E_J,\qquad
 c_p=2/a_-,\quad c_r=1+2d_+/a_- .
 \tag{WC.9}
$$
The true radial recovery still contains $d_+$. The projected pairing does not remove it.

## 3. The same three bands on the wider interval

All body norms in this section are over the complete wide interval. Set
$$
 Z_L=\|\Pi_{96}z\|_2,\quad Z_M=\|(\Pi_{288}-\Pi_{96})z\|_2,\quad
 Z_F=\|H_{288}z\|_2,\quad Z_H=(Z_M^2+Z_F^2)^{1/2},\quad
 Z=(Z_L^2+Z_H^2)^{1/2}.
 \tag{WC.10}
$$
The low projection contains the complete even mean. Preserve the E and PE constants $A_0,A_*,a_\Delta,d_\Delta$. Then
$$
 E_{96}=F_{96}+A_0Z+384d_+Z_L+LZ_H+C_{\chi,96}.
 \tag{WC.11}
$$
The factor $384$ is the largest physical angular frequency in the low band. No high-to-low drift commutator is added: it is already inside the projected principal operator.

The exact finite support of $A_*$ and $d_0$, and the complete difference bounds from LT, give
$$
 \begin{split}
 E_{288}={}&F_{288}+A_*Z_H+a_\Delta Z
       +384d_\Delta Z_L+1152d_+Z_M+LZ_F+C_{\chi,288}.
 \end{split}
 \tag{WC.12}
$$
The middle-to-far drift term remains. In particular, a small nonlinear difference does not remove the actual reference operator acting on $Z_H$.

For a table using only $Z_L,Z_H$, the following positive coefficients are sufficient:
$$
 \begin{aligned}
 E_{96}&\le F_{96}+(A_0+384d_+)Z_L
                              +(A_0+L+\kappa_\chi)Z_H,\\
 E_{288}&\le F_{288}+(a_\Delta+384d_\Delta)Z_L\\
 &\qquad+\left[A_*+a_\Delta+
       \sqrt{(1152d_+)^2+(L+\kappa_\chi)^2}\right]Z_H .
 \end{aligned}
 \tag{WC.13}
$$
These are fresh positive recombinations. They are not obtained by subtracting independently rounded bounds from a successful old coefficient table.

Put
$$
 \kappa_J^{\rm ang}=\sqrt{1+[4(J+1)]^{-2}},\qquad
 V_J=p_c\sqrt{\kappa_J^{\rm ang}c_pc_r}\,E_J,\qquad
 p_c=\max(K(c)^{1/4},K(c)^{-1/4}).
 \tag{WC.14}
$$
The full two-endpoint fundamental theorem of calculus, applied to $u=\chi H_Jz$, proves
$$
 \|H_J(Q-Q^\delta)(c)\|_{H^{1/2}}\le V_J .
 \tag{WC.15}
$$
There is no extra factor of two, and no plateau is used in this step. The factor $p_c$ is radial and is paid exactly once.

## 4. Where the narrow high-order bound is consumed

Let
$$
 c_L=\|\Pi_{96}(Q-Q^\delta)(c)\|_2,\qquad
 \Lambda_{96}=\sqrt{1+384^2},\qquad
 \Lambda_{288}=\sqrt{1+1152^2},\qquad
 \theta=16384/16385 .
 \tag{WC.16}
$$
The middle band is finite and the far band uses (WC.4). Consequently
$$
 \|(Q-Q^\delta)(c)\|_{H^1}
 \le \Lambda_{96}c_L+\sqrt{\Lambda_{288}}\,V_{96}
                                      +2^{24}V_{288}^{\theta}.
 \tag{WC.17}
$$
Indeed the high interpolation exponent is $1/16385$, and
$377903/16385<24$. Its high factor belongs to the same raw moving cut function as (WC.15); there is no interpolation between different states or different angles.

The new wide table may therefore be combined with any genuinely applicable MA narrow case. If its right side is less than $63d/320$, the W sufficient low gate follows in its stated known-base domain. All three unknown inputs in (WC.17), including the finite mean, remain explicit. No source-only statement proves that inequality.

For approximate iterates, $F_J$ must include their full projected ordinary residual, and $L$ must include the actual ordinary mean source in $m'/m$. The MA bound (WC.4) is not available for an approximate iterate merely because its low residual is small.

The direct first-angular trace route using two energy estimates is separate. It still needs nested cutoffs and the complete differentiated equation with $d_\phi p$ in $A_1$. The one-hat observation does not remove its second cutoff fee.

## 5. The only missing coefficient datum and its exact original field

The intrinsic bounds on all of $[17/20,19/20]$ already come from the successful D receipt. The saved NR receipt supplies the complete nonmean restriction on this same wide interval. The MC receipt supplies its independent raw-mean restriction. None needs to be recalculated.

The remaining wide speed datum is the lower bound on the absolute value of the original full moving mean. Its exact old field is
$$
 \texttt{row.complete\_inverse\_coordinate\_and\_physical\_residual.mean\_absolute\_gap}.
 \tag{WC.18}
$$
It belongs to the complete original 7296 closed rows, whose native bytes have SHA256
6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1.
The original producer proves that the full moving mean is negative; the field is its directed positive gap. It is not the radial intrinsic field named $s$.

Let $m_{\rm raw,w}$ be the minimum of the directed lower endpoints of (WC.18) on all original closed rows intersecting the wide interval. The actual reference and state obey
$$
 m_{\rm ref,w}=m_{\rm raw,w}-5.842\,10^{-21}-19d,\qquad
 |m_Q|\ge m_{\rm ref,w}-\rho_{\rm w}=:m_{\rm w}>0.
 \tag{WC.19}
$$
The complete centre-mean repair, the continuous response mean, and the unknown state radius are separate terms. The response bound $19$ is the already paid complete pair bound and is used only as an upper bound for its mean.

Using the saved intrinsic bounds, one may then set
$$
 a_-=G_-\sqrt{K_-}\,m_{\rm w}.
 \tag{WC.20}
$$
For the true residual-zero state, E.7 gives
$$
 L\le (|G_r|/G)_++\tfrac12(|K_r|/K)_+
       +|\beta|_+\max(|1-S_-|,|1-S_+|),
 \tag{WC.21}
$$
where $S_-=K_-m_{\rm w}^2$ and any complete established upper bound on
$u^2+Kv^2$ gives $S_+$. This retains the actual moving mean identity.
The rest of $d_+,A_0,A_*,a_\Delta,d_\Delta$ is the same explicit low-state algebra as PE, with the wide radius $\rho_{\rm w}$.

The new scalar consumer is allowed to read (WC.18), verify the complete original byte identity and coverage, and combine these positive formulas. It does not re-evaluate any intrinsic target, Fourier product, residual row, repair, scalar mean flow, Green operator or old high-order collar gate.

## 6. The complete known high source on the wide interval

Let $N_{\rm w}$ and $N_{\phi,\rm w}$ be the two already completed NR bounds on the $P$-scaled uncorrected nonmean response over the wide interval. Let $e_{\rm rep}$ be the saved complete operator-repair source supremum, $e_{\rm cont}$ the saved canonical continuity-offset source supremum, and $p_+$ the saved radial $P$ bound. Define
$$
 \begin{aligned}
 S_{\rm w}&=N_{\rm w}+p_+\sqrt{|I_{\rm w}|}\,(e_{\rm rep}+e_{\rm cont}),\\
 S_{\phi,\rm w}&=\min\!\left\{
 N_{\phi,\rm w}+640p_+\sqrt{|I_{\rm w}|}\,(e_{\rm rep}+e_{\rm cont}),
                                      \ 640S_{\rm w}\right\}.
 \end{aligned}
 \tag{WC.22}
$$
Both complete bounds in the minimum describe the same high projection. The repair and offset retain their actual degree at most160; $P$ is radial.

Let $t_2,t_3$ be the original saved full pointwise polynomial upper bounds, not the old narrow $L^2$ values. Then
$$
 T_{2,\rm w}=p_+\sqrt{|I_{\rm w}|}\,t_2,\qquad
 T_{3,\rm w}=p_+\sqrt{|I_{\rm w}|}\,t_3,
 \tag{WC.23}
$$
and the complete known selected-reference contributions are
$$
 \begin{aligned}
 F_{96}^{\rm known}
   &\le dS_{\rm w}+d^2T_{2,\rm w}+d^3T_{3,\rm w},\\
 F_{96,\phi}^{\rm known}
   &\le dS_{\phi,\rm w}+896d^2T_{2,\rm w}+1152d^3T_{3,\rm w},\\
 F_{288}^{\rm known}&=F_{288,\phi}^{\rm known}=0 .
 \end{aligned}
 \tag{WC.24}
$$
The zero statement is exact finite support: the base degree32 residual has degree96, and the three remaining complete species have degrees160,224,288. It is not a claim that the selected reference itself solves the PDE.

MC's raw-mean term is retained in the full ordinary source and copied unchanged from the completed wide MC restriction. It vanishes only after the indicated high projection. The old mean-completed nonmean budget is not relabelled as the full canonical response residual.

## 7. Domain bookkeeping and the two body halves

The original 91-case conclusion stores full scalar tables only for the five selected narrow cases. Its other old verdicts do not authorize new high-order domains after the MC correction. This supplement uses none of those discarded tables and changes none of those verdicts.

In particular, a new wide ordinary-energy table is not a claim that an old wide factorial case passed. Its high-order input remains exactly (WC.3)--(WC.4).

If independent rigorous sources provide raw moving body bounds $B_-$ and $B_+$ for the two halves of the same state, then
$$
 Z\le p_+\sqrt{B_-^2+B_+^2}.
 \tag{WC.25}
$$
The original finite Green output only covers the left side of $c$. Its ordinary source, special low-high column and true cut columns retain their different units. A right-cap derivative bound can supply $B_+$ only after fixing its actual physical base point, its input species, the complete mean, and the conversion to this same moving state. A small physical $\gamma$ alone is not a bound on $Q-Q^\delta$.

Thus the widened energy window changes a concrete cutoff cost and a concrete source restriction. It does not remove the unknown right body, the actual cut matching, the narrow high-domain hypothesis, or the full finite mean.