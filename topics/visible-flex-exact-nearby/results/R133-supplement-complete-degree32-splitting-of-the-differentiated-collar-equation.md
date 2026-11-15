# R133 supplement: complete degree32 splitting of the differentiated collar equation

## 1. Same state and the precise additional estimate

Use the exact state, parameters, projections, ordinary norms, and cutoff
geometry of [NC](R133-supplement-nested-collar-localization-and-direct-projected-first-angular-trace.md).
In particular $J=96$ or $288$, $|\delta|\le10^{-10}$, the actual
two-sided state is continuous and real on $[17/20,19/20]$, and its full
$C^0$ difference from $Q_\delta$ is bounded by the declared $\rho$.
The genuine LC speed/mean hypotheses and both NC energy gates remain
required.

This supplement retains the bandwidth of the **base differentiated
operator**. It moves its low-input column to the exact 64-mode shell,
while paying every selected-reference and actual-state difference.
It does not replace the actual high-input coefficient in the second
absorption gate by a mixing coefficient.

Write
$$
 U=PQ_0,\qquad V=PQ_\delta=U+e,\qquad W=PQ=V+z,
 \quad \Delta=2E_0+\eta ,
 \tag{BD.1}
$$
with the LC bounds
$$
 \begin{gathered}
 \|U\|_{L^\infty}\le M_0,\quad
 |\langle U\rangle|\le M_{\rm av},\quad
 \|U-\langle U\rangle\|_{L^\infty}\le N_0,\quad
 \|U_\phi\|_{L^\infty}\le M_1,\\
 \|U_{\phi\phi}\|_{L^\infty}\le M_2:=128M_1,\qquad
 \|e\|_{L^\infty}\le E_0,\quad \|e_\phi\|_{L^\infty}\le E_1,\quad
 \|e_{\phi\phi}\|_{L^\infty}\le E_2:=384E_1,\qquad
 \|z\|_{C^0}\le\eta .
 \end{gathered}
 \tag{BD.2}
$$
The base $U$ has full angular degree32, including its continuous
repair. The selected direction $e$ has degree96, including its full
canonical correction. Neither statement truncates the actual $z$.
The values $M_{\rm av},N_0$ refer to this same base $U$.
The vector norms displayed in (BD.2) are Euclidean pointwise sup
norms. LC supplies them from Euclidean combinations of the two
componentwise $A^0$ envelopes. The bounds $128M_1$ and $384E_1$
follow by differentiating the known component envelopes on their
degree32 and degree96 supports. No identification with the sum of
Euclidean Fourier coefficient lengths is used. The separate known
raw $A^0$ repair hypotheses in (BD.5) and (BD.9) are retained.

The positive collar is outside the compact $\nu$ perturbation.
Thus the compared $\beta,G,K,P,b,\alpha,g$ here are the same radial
coefficient functions. The actual principal speed still uses the
actual complete moving mean. This is not a comparison of two
independently selected metrics or boundary states.

## 2. Complete base operators and their bandwidth

Let $\mathcal A_1(W)$ and $\mathcal B_{10}(W,V)$ be the exact
NC.12--13 coefficients. The first also depends on the actual
$d_\phi$, as written there. Define
$$
 d_0=-bI_\phi|U|^2,\qquad
 A_{1,0}=(d_0)_\phi\operatorname{Id}+\alpha D-bDN(U),
 \quad DN(U)=|U|^2\operatorname{Id}+2UU^t,\qquad
 B_0=\mathcal B_{10}(U,U).
 \tag{BD.3}
$$
Both $A_{1,0}$ and $d_0$ have angular coefficient degree at most64.
Every term of $B_0$ is either a multiplication by a degree64
coefficient or a composition of multiplication by one degree32
coefficient, the diagonal Fourier operator $I_\phi$ or
$P_{\perp,\phi}$, and a second degree32 coefficient.
Its final independent-mean output has degree at most32.
Therefore, exactly,
$$
 H_JA_{1,0}\Pi_{J-64}=0,\qquad
 H_Jd_0\partial_\phi\Pi_{J-64}=0,\qquad
 H_JB_0\Pi_{J-64}=0.
 \tag{BD.4}
$$
The same holds with an additional input angular derivative, since that
derivative does not enlarge Fourier support. This is an identity of
complete operators, including the finite-rank terms of the primitive.

Let $D_{0,1}$ bound $\|(d_0)_\phi\|_\infty$.
One admissible bound using the saved original raw fields is
$$
 D_{0,1}=D_{\rm raw,1}
       +|\beta|_+k_K(2R_A e_Q+e_Q^2),\quad
 R_A=U_A+V_A,\quad k_K=\max(1,K_+),\quad
 e_Q=3.861\cdot10^{-18}.
 \tag{BD.5}
$$
The repair is known in $A^0$, whose nonmean projection has norm one.
Set
$$
 B_{\rm base}=8b_+M_0M_1+\frac{b_+M_0}{2}M_2 .
 \tag{BD.6}
$$
This bounds $H_JB_0$ on $L^2$. Its $g\langle h_2\rangle J_0U_{\phi\phi}$
term is zero only after the displayed high output projection.

A sharper complete low-to-high matrix bound is
$$
 A_{\rm mix,1}=D_{0,1}
                 +b_+(6M_{\rm av}N_0+3N_0^2).
 \tag{BD.7}
$$
Indeed $\alpha D$ and $DN(\langle U\rangle)$ are constant angular
matrices, hence Fourier diagonal. They give zero in
$H_JA_{1,0}\Pi_J$.
Expanding $DN(U)-DN(\langle U\rangle)$ gives the remaining complete
bound $6M_{\rm av}N_0+3N_0^2$.
This cancellation is only for the specified low-to-high column.
The complete actual $A_1^+$ in NC.17 is unchanged.

## 3. Full drift and local-matrix differences

Write $d=d_0+(d-d_0)$. The existing LC bounds give
$$
 \|d-d_0\|_\infty\le
 \Delta d:=D_{\rm ref,\delta}+D_{\rm nl}.
 \tag{BD.8}
$$
The known $A^0$ primitive and unknown $C^0$ sawtooth bounds used in
these two terms retain their distinct $1/4$ and $\pi/8$ constants.
Their already evaluated LC bounds can be read directly.

For the differentiated drift, an admissible complete bound is
$$
 \begin{split}
 \Delta d_1={}&|\beta|_+k_K
       \{2(R_A+e_Q)(19d_\nu)+(19d_\nu)^2\}\\
 &+2|\beta|_+k_K\rho
       \{2(R_A+e_Q+19d_\nu)+\rho\},\qquad d_\nu=10^{-10}.
 \end{split}
 \tag{BD.9}
$$
Then $\|d_\phi-(d_0)_\phi\|_\infty\le\Delta d_1$.
The first line is the known canonical offset in $A^0$; the second is
the full unknown difference in $C^0$, for which the nonmean projection
has norm two. The centre repair in $D_{0,1}$ is not charged twice as
part of the selected offset.

Since $\|W-U\|_\infty\le E_0+\eta$, the exact cubic derivative obeys
$$
 \|DN(W)-DN(U)\|_\infty
       \le6M_0(E_0+\eta)+3(E_0+\eta)^2.
$$
Consequently
$$
 \Delta A_1:=\Delta d_1+
        b_+\{6M_0(E_0+\eta)+3(E_0+\eta)^2\}
 \quad\hbox{bounds}\quad
 \|A_1(W)-A_{1,0}\|_{L^2\to L^2}.
 \tag{BD.10}
$$
No angular derivative of the unknown $z$ occurs in this coefficient
bound. The high own-input energy still uses the full actual $A_1(W)$.

## 4. Complete lower-order differentiated difference

For the first three local terms of NC.13, use
$$
 \|W+V\|_\infty\le2M_0+\Delta,\qquad
 \|W+V-2U\|_\infty\le\Delta,\qquad
 \|V_\phi-U_\phi\|_\infty\le E_1.
$$
Subtracting their complete base values and summing gives
$$
 b_+\{6M_0E_1+3\Delta(M_1+E_1)\}.
 \tag{BD.11}
$$
For example the first term contributes
$b_+\{E_1(2M_0+\Delta)+M_1\Delta\}$.
The second and third together contribute
$2b_+\{\Delta(M_1+E_1)+2M_0E_1\}$.
Thus (BD.11) is a bound on the full three-term difference, rather
than the difference of two upper bounds.

The complete nonmean-projection term contributes at most
$$
 b_+\{2M_0E_1+\Delta(M_1+E_1)\},
 \tag{BD.12}
$$
using its $L^2$ norm one. The complete primitive term contributes
$$
 \frac{b_+}{4}\{E_2(2M_0+\Delta)+M_2\Delta\}.
 \tag{BD.13}
$$
The two mean-rank output terms in the difference have degrees at
most96, and hence vanish under the final $H_J$.
All mean inputs in the other terms are retained.

It follows that the full projected difference is bounded by
$$
 \boxed{\quad
 \Delta B_{10}
 =b_+\{8M_0E_1+4\Delta(M_1+E_1)\}
       +\frac{b_+}{4}\{E_2(2M_0+\Delta)+M_2\Delta\}.
 \quad}
 \tag{BD.14}
$$
Specifically,
$\|H_J(\mathcal B_{10}(W,V)-B_0)h\|_2
 \le\Delta B_{10}\|h\|_2$ for every full input $h$.
This assertion retains all its independent mean coordinates.

## 5. The three complete body columns

Use $z_L,z_S,z_H$ from NC.2 and $p=z_\phi$.
Splitting every term of the exact NC.18 equation by (BD.3)--(BD.14)
gives the three nonnegative constants
$$
 \begin{aligned}
 D_S&=B_{\rm base}+4J A_{\rm mix,1}+(4J)^2d_0^+,\\
 D_L&=\Delta B_{10}+4J\Delta A_1+(4J)^2\Delta d,\\
 D_H&=B_{\rm base}+\Delta B_{10}.
 \end{aligned}
 \tag{BD.15}
$$
Here $d_0^+$ is the complete LC bound, including the centre repair.
The base terms in the low-input column land only on $z_S$ by (BD.4).
The differences act on all $z_L$, with no band or mean deletion.
The lower-order base and difference both act on $z_H$.
The full high derivative coefficient $H_JA_1(W)p_H$ remains on the
left via its own already stated $t_1$ absorption.

With the two NC cutoffs and their actual derivatives, denote the full
cutoff source by
$$
 \mathcal E_\chi=F_0+C_SZ_S+C_LZ_L+\kappa_0Z_H.
$$
This notation distinguishes it from the known reference size $E_0$
in (BD.2). The complete derivative source bound is
$$
 G_{\rm BD}=F_1+D_SZ_S+D_LZ_L+D_HZ_H+\kappa_1 b_p\mathcal E_\chi,
 \qquad
 \|H_J(Q-Q_\delta)(c)\|_{H^1_\phi}\le\mathcal T_JG_{\rm BD}.
 \tag{BD.16}
$$
Every norm in (BD.16) uses the same surviving inner interval as NC.20.
The weak-state justification and final physical factor are exactly
those already proved in NC.21--23.

## 6. The complete nested five-column row

For the fixed geometry NC.24 and any positive integer $N$, retain
$$
 r_N=40Nk,\qquad
 \eta_N=r_N^N,\qquad
 \sigma_N=k\sum_{j=0}^{N-1}r_N^j,\qquad
 \Gamma_H=D_H+6400b_p,\qquad
 \Theta_N=80b_p+\Gamma_H\sigma_N.
 \tag{BD.17}
$$
Here $\kappa_0=\kappa_1=80$, so the full cutoff source in
(BD.16) is $\mathcal E_\chi=F_0+C_SZ_S+C_LZ_L+80Z_H$.
Both actual cutoff derivative costs occur in $\Gamma_H$.

Substitution of NC.10 and restriction of the outer norms proves
$$
 \boxed{\quad
 \begin{split}
 \|H_J(Q-Q_\delta)(c)\|_{H^1_\phi}
 \le\mathcal T_J\{&
 F_1^o+\Theta_NF_0^o
       +(D_S+\Theta_NC_S)Z_S^o\\
 &+(D_L+\Theta_NC_L)Z_L^o
                 +\Gamma_H\eta_NB_0^o\}.
 \end{split}
 \quad}
 \tag{BD.18}
$$
The high outer norm is denoted $B_0^o=\|z_H\|_{2,I_0}$ here to
distinguish it from the base operator $B_0$ in (BD.3).
This is one complete five-column row for each $(\rho,J,N)$.
The scalar coefficient of the high outer norm can be minimized over
a finite, declared set of $N$ values by selecting that **entire** row.
Such a selection is not asserted to minimize the unknown total
error, and it cannot combine entrywise minima from incompatible
rows or domains.

For a true solution, the source specialization is exactly NC.27:
$F_1^o\le1152F_0^o$ for $J=96$, and both vanish for $J=288$.
The existing full same-window source bound may be read without
a new radial integration. Approximate states retain both genuine
residual columns and the additional mean-residual speed cost.

All base/selected/current scalar bounds must be formed as complete
upper bounds before any maximum is taken.
The six declared $\rho$ domains stay distinct. A subsequent scalar
consumer may evaluate the two NC and BD full rows for all
$6\cdot2\cdot64$ declared cases, keeping its complete audit temporary
and publishing only its complete selected rows, selection rule,
gate counts, parameters and hashes. This note supplies no new
actual $t_1$, unknown shell/body/cut value, low trace, full core
existence, or high tail domain.
