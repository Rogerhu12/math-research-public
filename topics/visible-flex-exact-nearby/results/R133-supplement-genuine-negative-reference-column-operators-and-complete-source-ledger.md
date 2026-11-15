# R133 supplement: genuine negative reference column operators and the complete source ledger

2026-11-15, phase_inverse.

**Proved analytic operator recipe on the negative side.** This supplies the
all-output norm required in G.15 of
[the ordered genuine-reference source identity](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md).
It uses both genuine columns, both signed Fourier inputs, the old output mean,
and the actual circle maps. It does not estimate a growing positive column by
an unweighted negative-side bound.

The reference columns and their relative frame are those of
[the genuine common-radial two-column construction](R133-supplement-genuine-common-radial-reference-columns-and-two-source-ports.md).
Their actual scalar verification is public run 43688459733/1. The new complete
amplitude inputs are the selected whole-function conclusions of public run
43698106023/1, at the unchanged physical output disk $3/40000$.
Neither calculation is repeated here. The recipe below still requires its own
public scalar consumption before any numerical complete source or return bound
is asserted.

## 1. The real negative circle and both exact columns

Let $J_0\ge97$, $N=4J_0$, $n=4|j|$, and
$\epsilon=\operatorname{sgn}j$. Use the original real allowed parameters.
The coefficient enclosures may have been proved on complex parameter boxes;
the circle maps used in this theorem are real maps on real parameter slices.

Write
$$
 \rho=r_*-r>0,\qquad T=-\rho A(\rho,\phi)^{2/3},\qquad
 h=-T,\qquad \omega=\frac23h^{3/2}.
 \tag{V.1}
$$
On the physical subinterval under consideration assume the actual bounds
$$
 0<A_-\le A\le A_+,\quad A_+/A_-\le2,\quad
 0<\rho\le R,\quad R A_+^{2/3}\le L=\frac1{2000}.
 \tag{V.2}
$$
All powers use the original positive real branch. Set
$$
 |\partial_\phi\log h|\le L_1,\qquad
 |\partial_\phi^2\log h|\le L_2 .
$$
These are bounds for the actual angular fold, not for the radial reference
alone. The functions $\Phi_0=X,\Phi_\pm=X\pm\omega$ must have their actual
orientation and three-derivative circle bounds.

For the same $V_j(T)=V(j^{-2},T)$, let the row vector
$$
 {\bf Y}_j=(\widehat f_n,g_n),\qquad
 ({\bf Y}_j)_{TT}=(n^2T-V_j){\bf Y}_j .
 \tag{V.3}
$$
Its two-state matrix is $\Psi_n$ in A.19. In particular its Wronskian,
root shear, normalization, and finite-frequency potential are unchanged.
Use the already proved inequalities
$$
 \|F_n^{-1}\Psi_n\|_2<6/5,\qquad
 |V_j|\le M,\quad |(V_j)_T|\le M_1
 \quad(-L\le T\le0).
 \tag{V.4}
$$
Here $M=276$ is valid by the original complete potential result; $M_1$
is the corresponding actually paid derivative bound. A fixed unitary change
to the two signed Airy columns preserves every row norm used below.

## 2. Exact oscillatory amplitudes of the genuine solutions

For $h>0$, put
$$
 t=\frac23 n h^{3/2},\qquad
 {\bf W}=n^{1/6}h^{1/4}{\bf Y}_j .
$$
Direct differentiation of (V.3), using $t_T=-n\sqrt h$, gives
$$
 {\bf W}_{tt}+(1+q){\bf W}=0,\qquad
 q=\frac5{36t^2}+\frac{V_j(-h)}{n^2h}.
 \tag{V.5}
$$
Define the two row vectors
$$
 {\bf b}_\sigma=\frac12({\bf W}-\sigma i{\bf W}_t)e^{-\sigma it},
 \qquad
 ({\bf b}_\sigma)_t
       =\frac{\sigma i}{2}q{\bf W}e^{-\sigma it},
 \qquad \sigma=\pm1 .
 \tag{V.6}
$$
Consequently the exact profiles are
$$
 \begin{split}
 n^{1/6}{\bf Y}_j
   &=h^{-1/4}\sum_\sigma{\bf b}_\sigma e^{\sigma it},\\
 n^{-5/6}({\bf Y}_j)_T
   &=h^{1/4}\sum_\sigma
       \left(-\sigma i+\frac1{6t}\right){\bf b}_\sigma e^{\sigma it}.
 \end{split}
 \tag{V.7}
$$
The sign and the $n$ power in the second row follow from the exact identity
$n^{-5/6}Y_T=h^{1/4}[-W_t+W/(6t)]$.
These formulas are used only when $t\ge1$, so no value of $1/t$ at the root
is assigned.

The elementary Airy estimates A.8 imply a convenient full two-column bound
$$
             \|{\bf W}\|_2,\ \|{\bf W}_t\|_2<9
             \qquad(t\ge1,\ -L\le T<0).
 \tag{V.8}
$$
Here is a proof independent of a large-argument asymptotic truncation.
For either free real column put $s=n^{2/3}h$.
At $t=1$, $1<s=(3/2)^{2/3}<3/2$, and A.8 gives
$$
 |s^{1/4}Y|<3,\qquad
 \left|\frac{Y}{4s^{5/4}}+s^{-1/4}Y_s\right|<3 .
$$
The free oscillator has $q=5/(36t^2)$. Its energy is therefore bounded by
$18\exp(5/36)<25$ for all $t\ge1$.
The two free row norms are at most $5\sqrt2$.
The change from the two-state free matrix to the genuine matrix is exactly
$F_n^{-1}\Psi_n$, so (V.4) gives $6\sqrt2<9$.
Both the height and derivative rows are included before estimating.

For later angular differentiation define the nonnegative constants
$$
 \begin{split}
 Q_1&=\frac5{36}+\frac{2M\sqrt L}{3N},\\
 Q_2&=\frac5{36}+\frac{4ML^2}{9},\\
 Q_d&=\frac5{18}+
             \frac4{9N}(M_1L^{3/2}+M\sqrt L),\\
 B_0&=9,\qquad B_1=\frac92Q_1,\qquad
 B_2=\frac92(Q_d+2Q_2).
 \end{split}
 \tag{V.9}
$$
The exact changes of variable in (V.5) give
$t|q|\le Q_1$, $t^2|q|\le Q_2$, and $t^2|q_t|\le Q_d$.
Equation (V.6) and its derivative then prove
$$
 \|{\bf b}_\sigma\|\le B_0,\quad
 \|t({\bf b}_\sigma)_t\|\le B_1,\quad
 \|t^2({\bf b}_\sigma)_{tt}\|\le B_2 .
 \tag{V.10}
$$
Thus no uncontrolled derivative of a frequency-dependent connection matrix
is hidden in the high-argument amplitude.

## 3. A circle-independent frequency partition

At each fixed $\rho>0$ split the input labels, including both signs, by
$$
 \begin{array}{ll}
 \text{central:}&n<3/(2\rho^{3/2}A_-),\\
 \text{high:}&n\ge3/(2\rho^{3/2}A_-).
 \end{array}
 \tag{V.11}
$$
This partition is independent of $\phi$. In the high set the actual $t$
is at least one everywhere on the old circle. In the central set,
$t<A_+/A_-\le2$, hence $s=n^{2/3}h<3$.
This is only a partition for a pointwise norm estimate. The trial, its radial
derivatives, and its physical transmission are defined before this partition;
no radial derivative of the artificial label cutoff is taken.

For the high set put
$$
 \begin{split}
 b_0&=B_0,\\
 b_1&=\tfrac32L_1B_1,\\
 b_2&=\tfrac94L_1^2B_2+
                   (\tfrac32L_2+\tfrac94L_1^2)B_1,\\
 e_1&=L_1/4,\qquad e_2=L_2/4+L_1^2/16,\\
 h_0&=7/6,\qquad h_1=L_1/4,\qquad
 h_2=L_2/4+3L_1^2/8,\\
 c_0&=h_0b_0,\quad c_1=h_0b_1+h_1b_0,\quad
 c_2=h_0b_2+2h_1b_1+h_2b_0 .
 \end{split}
 \tag{V.12}
$$
The numbers $b_k$ bound the first two old-angle derivatives of
${\bf b}_\sigma(t(\phi))$. The $h_k$ bound the corresponding derivatives of
$-\sigma i+1/(6t)$. For instance the second derivative of $1/t$ is estimated
as $t^{-1}[(\partial_\phi\log t)^2-\partial_\phi^2\log t]$, not by dropping
one term. The triples
$$
 \begin{split}
 {\bf p}^{\,H}
 &=A_-^{-1/6}(b_0,\ b_1+e_1b_0,\
                         b_2+2e_1b_1+e_2b_0),\\
 {\bf q}^{\,H}
 &=R^{1/2}A_+^{1/6}(c_0,\ c_1+e_1c_0,\
                         c_2+2e_1c_1+e_2c_0)
 \end{split}
 \tag{V.13}
$$
bound each branch in (V.7), after factoring out the common
$\rho^{-1/4}$. They apply to both genuine columns as row-vector bounds.

For the central set define
$$
 d_*=\left(\frac3{2A_-}\right)^{2/3},\quad
 H_*=\left(\frac3{2A_-}\right)^{1/6},\quad
 u_1=d_*A_+^{2/3}L_1,\quad
 u_2=d_*A_+^{2/3}(L_2+L_1^2),
$$
$$
 B_*=3+MN^{-4/3},\qquad C_*=1+B_*+M_1N^{-2}.
 \tag{V.14}
$$
Since $s<3$, A.8 and (V.4) give both
$\|{\bf Y}_j\|<8$ and
$\|({\bf Y}_j)_T/n^{2/3}\|<8$.
Differentiate only in the actual old angle and use (V.3):
$$
 \|{\bf Y}_{TT}\|\le8n^{4/3}B_*,\qquad
 \|{\bf Y}_{TTT}\|\le8n^2C_* .
$$
The two central triples, again with the common $\rho^{-1/4}$ removed, are
$$
 \begin{split}
 {\bf p}^{\,C}
 &=8H_*(1,\ u_1,\ B_*u_1^2+u_2),\\
 {\bf q}^{\,C}
 &=8R^{1/4}N^{-1/6}(1,\ B_*u_1,\
                                   C_*u_1^2+B_*u_2).
 \end{split}
 \tag{V.15}
$$
This includes every low Airy argument. It does not extend the high-argument
formulas through $t=0$.

After multiplication by $e^{i\epsilon nX}$, (V.13) has phases
$X+\epsilon\sigma\omega$; the two labels are simply exchanged for negative
input frequencies. Formula (V.15) has phase $X$. Thus the complete operator
is the sum of one central and two high pieces with three genuine real circle
maps.

## 4. All-output operator norm, including the output mean

For a circle lift $\Phi$ use its actual bounds
$$
 0<m_\Phi\le\Phi'\le M_\Phi,\quad
 |\Phi''|\le F_{2,\Phi},\quad |\Phi'''|\le F_{3,\Phi}.
$$
Set
$$
 P_2=F_{2,\Phi}/m_\Phi^3,\qquad
 P_3=F_{3,\Phi}/m_\Phi^4+3F_{2,\Phi}^2/m_\Phi^5,
$$
$$
 C_{0,\Phi}=m_\Phi^{-1/2},\quad
 C_{2,\Phi}=\sqrt{M_\Phi}
 \{m_\Phi^{-2}+2P_2^2+m_\Phi^{-4}+P_3^2+
               9P_2^2/(2m_\Phi^2)+m_\Phi^{-6}\}^{1/2},\quad
 C_\Phi=C_{0,\Phi}^{1/6}C_{2,\Phi}^{5/6}.
 \tag{V.16}
$$
These are exactly the full composition constants of A.3 in
[the real seam operator theorem](R133-supplement-complete-real-Airy-seam-operator-in-negative-source-window.md).
They bound composition on $H^{-5/3}$, not merely on $L^2$.

For any amplitude $w_j=(a_j,b_j)^t$, let
$a_k\ge\sup_j\|\partial_\phi^ka_j\|_\infty$ and similarly $b_k$,
$0\le k\le2$. For each of the three pieces take the appropriate profile
triples from (V.13) or (V.15), and form
$$
 D_k=\sum_{\ell=0}^k {k\choose\ell}
                   (p_\ell a_{k-\ell}+q_\ell b_{k-\ell}),\qquad k=0,1,2.
 \tag{V.17}
$$
Define $\Lambda_J=(1+16J^2)^{1/2}$ and
$$
 {\cal S}_{J}(B_0,B_2)=
 2^{5/3}\Lambda_J^{-1/3}(B_0+\pi^2B_2/48)
       +8B_2(J^{-4/3}+3J^{-1/3})^{1/2}.
$$
Then a valid explicit G.15 bound is
$$
 \boxed{\quad
 {\cal A}^{V}_\rho(w)=\rho^{-1/4}
   \sum_{\Phi\in\{X,X+\omega,X-\omega\}}
       C_\Phi\,{\cal S}_{J_0}
       \left(D_{0,\Phi},
         \frac{D_{2,\Phi}}{m_\Phi^2}
          +\frac{D_{1,\Phi}F_{2,\Phi}}{m_\Phi^3}\right).
 \quad}
 \tag{V.18}
$$
It bounds the full direct-sum two-column input
$H^{-4/3}(\mathbb C^2)_{|j|\ge J_0}$ to scalar $H^{-5/3}$.
A single specified column is a restriction of this result.

For completeness the matrix proof of A.2 remains valid for these row symbols.
Their Fourier coefficient row norms satisfy
$\min(B_0,B_2/(16\ell^2))$. The row and column Schur bounds use these norms.
On $|m|<|j|/2$, the row norm is its Hilbert--Schmidt norm from $\mathbb C^2$
to $\mathbb C$, so the identical squared tail bound applies. Output $m=0$
is included in that tail. The frequency restrictions (V.11) only delete input
columns; they do not increase either bound. Formula (V.18) uses the triangle
inequality between the three maps and makes no assumption of orthogonality
between their images or between the two genuine columns.

## 5. Finite derivative inputs; no hidden radial differentiation

The selected actual table of run 43698106023/1 bounds $w_1^V$ with radial
orders $0,1,2$ and angular orders $0,1,2,3$ on all three stated strips.
A joint Wiener bound bounds the corresponding pointwise derivative on every
real old circle. The amplitude mean columns of that table are not the
independent physical even-mean equation.

Products of two derivative triples are evaluated by the full binomial
Leibniz rule. For matrices the order of multiplication is retained:
$$
 (AB)^{(k)}=\sum_{\ell=0}^k{k\choose\ell}
                         A^{(\ell)}B^{(k-\ell)}.
 \tag{V.19}
$$
One may replace each ordered summand by the product of its appropriate
operator norms only after fixing this identity. In particular $B_jH_{D,j}^V$
is never interchanged with either matrix factor.

The old-circle inverse $B_j=(H_j^V)^{-1}$ has paid complex-strip bounds
through angular order two. Any needed third and fourth angular derivatives
are paid on a strictly narrower strip. If
$\sup_{|\Im\phi|\le\sigma_B}\|\partial_\phi^2 B_j\|\le B^{[2]}$, then on
$|\Im\phi|\le\sigma<\sigma_B$,
$$
 \|B_j^{(3)}\|\le B^{[2]}/(\sigma_B-\sigma),\qquad
 \|B_j^{(4)}\|\le2B^{[2]}/(\sigma_B-\sigma)^2.
 \tag{V.20}
$$
The same Banach-valued Cauchy rule applies to the actual $H_D^V$, coefficients
or leading amplitude when the needed complete bound and strip are known.
It is not a claim that the already published order-two table contained higher
orders.

In the local source, $D^2w_1^V$ differentiated twice in the old angle needs
$\partial_\phi^4w_1^V$. For a retained positive-width table, this missing
derivative can be bounded explicitly by
$$
 \sup_{\phi\ {\rm real}}|\partial_\phi^4w_1^V|
       \le \sigma^{-1}\|\partial_\phi^3w_1^V\|_{{\cal A}_\sigma},
       \qquad \sigma>0 .
 \tag{V.21}
$$
No fourth angular entry is silently read from the order-three table.
All other local derivatives of $w_1^V$ needed below are among
$w_{\rho\rho,\phi^2}$, $w_{\rho,\phi^3}$, and $w_{\phi^3}$.
At density zero, the leading-amplitude nonlocal terms require its genuine
angular order four and first radial derivative through angular order three;
their original holomorphic leading bounds supply them with the declared
positive Cauchy margins.

Use throughout
$$
 D=\partial_r-d\partial_\phi,\qquad
 D^2w=w_{rr}-2d w_{r\phi}+(dd_\phi-d_r)w_\phi+d^2w_{\phi\phi}.
 \tag{V.22}
$$
The tables use $\rho=r_*-r$, so $w_r=-w_\rho$;
absolute radial bounds are unchanged. No second radial derivative of the
potential or of the angular inverse is manufactured by this sign change.

There is also an exact reduction for the coefficient
$A_T=D^2T+\eta^2K T_{\phi\phi}-T_0DT$.
Since $[D,\partial_\phi]=d_\phi\partial_\phi$, the identities
$DT=Qx,\ DX=-QTy,\ x=X_\phi,\ y=T_\phi$ give
$$
 A_T=(DQ+Qd_\phi-T_0Q)x-QQ_\phi Ty-Q^2y^2 .
 \tag{V.23}
$$
The $T_{\phi\phi}$ terms cancel before taking bounds. Thus its angular
order two needs the actual first-radial mixed $Q$ derivatives, not a new
third-radial fold computation.

The correction term containing $V_T(T)$ does need two angular derivatives.
If $|T|\le T_{\max}<I_T$ and the original complete potential bounds
$|V_{TT}|\le M_2$ on $|T|\le I_T$, pay
$$
 |V_{TTT}(T)|\le M_2/(I_T-T_{\max}).
 \tag{V.24}
$$
Then
$(V_T\circ T)_{\phi\phi}=V_{TTT}T_\phi^2+V_{TT}T_{\phi\phi}$.
The nonzero image margin is a separate gate. It is not supplied merely by
the bound $T_{\max}\le L$ unless $I_T>L$ has also been certified.

## 6. The exact three local amplitudes and the complete old-circle rows

Define exactly as in G.4--G.6
$$
 \begin{split}
 {\cal C}_j(w)&=E_{12}
   \{2QV_j(xDw+QTyw_\phi)+(\mu(V_j)_T+A_TV_j)w\},\\
 {\cal R}_j(w)&=\vartheta QV_j B_je_1(i\epsilon y,x)w,\\
 {\cal L}_{j,\rm raw}(w)&=
       (D^2+\eta^2K\partial_\phi^2-T_0D+V_0-\mu V_j)w
                         +i\epsilon\vartheta Q{\cal K}w,\\
 L_1&={\cal L}_{j,\rm raw}(w_1^V)-{\cal C}_j(w_0),\\
 L_2&=-{\cal C}_j(w_1^V)+{\cal R}_j(w_0),\qquad
 L_3={\cal R}_j(w_1^V).
 \end{split}
 \tag{V.25}
$$
These are raw amplitudes, including the factor $\mu$ in the required
places. They are not divided by $\mu$ when inserted into G.21.
The matrix $E_{12}$ is on the left. The weights $n^{-1}$ and $n^{-2}$
are input-label operators after the ordered amplitudes.

For either $w=w_0$ or $w_1^V$, form the full amplitudes
$$
 h=\eta^{-1}B_jH_{D,j}^Vw,\quad
 y=B_j(vH_{D,j}^Vw),\quad
 g=Dw-\eta h_\phi,\quad q=vDw-y_\phi.
 \tag{V.26}
$$
Apply (V.18) separately to every amplitude needed in G.17--G.20.
The exact old-circle rows of G.13 remain in their original order.
Formula (V.28) below retains all four full operator terms and all five
old-mean contributions of G.19. No mean of a coefficient is discarded when
a full multiplication operator is bounded.

For clarity, the exact typed budget to be consumed is the following.
The input is always $H^{-4/3}_{|j|\ge J_0}$, with both genuine columns.
$$
 \begin{array}{c|c|c|c|c}
 i&X_i&Y_i&\Gamma_i(w)&M_i(w)\\ \hline
 0&H^{-8/3}&H^{-5/3}
 &{\cal A}^V(Bw)+{\cal A}^V(\partial_\phi(Bw))
 &{\cal A}^V(\partial_\phi(Bw))\\
 1&H^{-5/3}&H^{-2/3}&{\cal A}^V(w)&{\cal A}^V(w)
 \end{array}
 \tag{V.27}
$$
Here $\Gamma_0$ bounds the density $n^{7/6}$ into $X_0$;
$\Gamma_1$ bounds the density $n^{1/6}$ into $X_1$.
Let the original one-gain $J$, $L,B_{\rm op},S_Q,S_V,R_Q$ bounds in these
exact windows be $c_{J,i},c_{L,i},c_{B,i},c_{Q,i},c_{V,i},c_{R,i}$.
They must come from the same actual old coefficients and full projection
convention. Define
$$
 E_i(w)=\Gamma_i(g)+c_{L,i}\Gamma_i(h),\qquad C_I=\sqrt{17}/4 .
$$
With $m_q(f)=\sum_\ell(1+|4\ell|)^q|\widehat f_\ell|$, the complete
nonlocal first-row amplitude bound is
$$
 \begin{split}
 N_i(w)={}&c_{V,i}\Gamma_i(w)+c_{Q,i}\Gamma_i(h)
                   +c_{R,i}c_{J,i}E_i(w)
       +|c_B|m_3(v_\phi)C_I\Gamma_i(q)\\
 &+m_0(r_Q)M_i(h)+|c_B|m_0(v_\phi)M_i(y)\\
 &+\{|c_B|m_0(v_\phi)m_0(v)/4+m_0(T_0)\}M_i(g)
       +m_0(V_0)M_i(w).
 \end{split}
 \tag{V.28}
$$
All five full old-mean contributions are retained. The independent physical
even-mean equation is a further row:
$$
 M_i^{\rm phys}(w)=2|bm|
 \{M_i(uh)+m_3(u)c_{J,i}[E_i(w)+c_{B,i}\Gamma_i(w)]
                                      +|K|M_i((v-m)w)\}.
 \tag{V.29}
$$
This is not replaced by the amplitude-mean columns of the S result.

The first original source row of the corrected trial is bounded in
$H^{-2/3}$ by
$$
 C_{\rm first}(\rho)=c_{J,1}
 \{{\cal A}^V(L_1)+N^{-1}{\cal A}^V(L_2)
        +N^{-2}{\cal A}^V(L_3)+N_0(w_0)+N_1(w_1^V)\}.
 \tag{V.30}
$$
The second row is the actual constant
$$
 C_{\rm mean}(\rho)=M_0^{\rm phys}(w_0)+M_1^{\rm phys}(w_1^V).
 \tag{V.31}
$$
Both its $H^{-2/3}$ and $H^{-1}$ norms are its ordinary absolute constant
norm. Supplied independent mean sources are added as independent inputs.

## 7. Volume, true trace, and positive-interface ledgers

If uniform consumption of (V.16)--(V.31) gives
$C_{\rm first}(\rho)\le K_1\rho^{-1/4}$ and
$C_{\rm mean}(\rho)\le K_2\rho^{-1/4}$, the actual negative-side volume norm
on a segment of true-root length at most $R$ is at most
$$
 \|g\|_{L^2_r(H^{-2/3}\oplus\mathbb C)}
 \le \sqrt2\,R^{1/4}(K_1^2+K_2^2)^{1/2}.
 \tag{V.32}
$$
An uncertain-root interval is treated with its true one-sided parts. If two
sides or two bracket portions are used, their squared integrals are both
included; (V.32) is a one-sided formula.

The following are separate, typed rows of a later network consumer.

| Row | Actual input | Required independently paid map |
|---|---|---|
| Negative volume correction | Both source rows in (V.32) | The same-family complete negative Cauchy source map, in its stated angular window |
| Negative cut trace | The same ordinary sources, true root data and genuine physical jumps | The same Cauchy theorem's trace bound at that actual cut |
| Wave readout at a strict negative cut | The actual physical pair in that trace norm | The complete inverse physical frame and circle-map readout, including its frequency powers |
| Positive root graph | Its full collar/body sources, head, mean and outer affine ports | The actual two-ended positive graph, including every coefficient in its source-to-port matrix |
| Seam correction | Actual one-sided values and first radial derivatives | The physical two-trace jump formula G.22, with coefficient/reference changes included |
| Final high return | All preceding rows in the same input/output normalization | A complete feedback or Schur gate; it is not a consequence of any one scalar row |

In particular a known $H^{-1}$ physical output is not renamed $L^2$ wave
output without the third row. An unrestricted positive $g_n$ grows and
cannot use (V.18) on a fixed positive interval. The positive graph must first
control its coefficient or supply a complete weighted Green representation.

The source, root port and all physical traces also retain the exact
Liouville/Piola factors from A.25--A.27:
$$
 \widetilde g_j=
 \binom{g_{2,j}/(\kappa G)}
       {(i\epsilon n a\,g_{1,j}+c\,g_{2,j})/(\kappa^2G)},\qquad
 dT=\kappa\,dr.
 \tag{V.33}
$$
No derivative of $g_2$ is introduced. At the root use the original mixed
matrix in A.26, its nonzero finite-frequency $c$ column, and the root shear
of both reference columns. The independent $j=0$ physical equation is not
the analytic parameter value $z=0$.

Within the single original analytic physical piece, the same genuine columns
and their first derivatives have common traces. Across a real physical seam
or a reference matching curve, G.22--G.23 are still required. In particular the
old-circle distributional term
$-\sum_s[\mathsf S^V(Bw)]_{\phi_s}\delta_{\phi_s}$, and its negative primitive,
are not declared zero by this norm theorem.

The actual S result improved ten of 144 complete derivative bounds and none
of its 36 amplitude-mean bounds. This theorem provides a way to consume the
selected complete bounds without rerunning their accepted algebra. It does
not turn that limited improvement into a small ordinary-source norm, a
cutoff-97 inverse, or a completed whole positive/negative matching.
