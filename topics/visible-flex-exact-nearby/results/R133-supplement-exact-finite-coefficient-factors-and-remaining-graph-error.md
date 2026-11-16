# R133 supplement: exact finite coefficient factors and the remaining graph error

2026-11-16, visible-exact / phase_inverse.

**Proved exact finite-factor reduction for the same selected physical primitive row.** The root finite map and both primitive-conjugation ranks in WCE can be kept as actual finite factors. The projection of the root two-primitive term contributes one further finite row with output column $h-1$. After that exact separation, the remaining coefficient operator has a direct positive two-term bound. WFR's independent finite root response can be retained in the same graph system.

This is an identity of operators before taking norms. It is not a difference of upper bounds. The successful WPC/WCE scalar records are frozen. No new numerical combination, high cutoff, finite entry or determinant is evaluated here. The auxiliary variables below do not supply the 96 missing physical input columns, eliminate a radial mean function, or close the independent mean, amplitude, head and metric equations.

## WCF1. The same source, target and complete coefficient error

Use the selected real member, density convention and reflected input of WCE:
$$
 e_j(x)=e^{i4jx},\qquad
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 P=Id-\Pi,\qquad I=\partial_x^{-1}P,
$$
$$
 \mathcal S=U_\psi,\qquad U_\psi f=\psi'(f\circ\psi),\qquad
 X_s^{\rm fr}=\mathcal S D_+\mathcal H_{\rm nat}^s,
 \qquad \mathcal H_{\rm nat}^s=P_{97}\operatorname{Fix}(R_*)\cap H^s .
 \tag{WCF.1}
$$
All spaces carry their inherited norms. The fixed phase $D_+$ preserves real Fourier conjugacy. In particular $\Pi x=0$ for $x\in X_s^{\rm fr}$ because $\Pi\mathcal S=\Pi$. This uses the full density map, not ordinary composition.

Retain the WCE operators
$$
 \begin{gathered}
 h=U_{\mathcal H^{-1}}1,\quad P_h=Id-h\Pi,\quad
 Q_a=P(Id+R_a)/2,\quad Y^0=P\operatorname{Fix}(R_a)\cap L^2,\\
 T_i=Id+M_{c_i}I,\quad c_i=\nu_i+v_i,\quad \Pi v_i=0,\quad
 \rho_i=\Pi T_i|_{X^{\rm fr}},\\
 \mathcal A_J=Id+\mathcal V_w,\qquad
 \Pi h=1,\quad R_a h=h,\quad \mathcal A_Jh=h .
 \end{gathered}
 \tag{WCF.2}
$$
Here $\nu_i=-\mu/2$ is the fixed incoming coefficient mean. It is not a varying metric parameter. The exact identities in (WCF.2) include the true second waist normalizer; they do not set $\mathbf Z(0)$ or $\mathbf S_r(0)$ to zero.

At the original root put
$$
 F=F_*=\frac{\beta_*u_*v_*}{\eta_*},\quad c=C_+(0)-F,\quad
 c_i=\mathcal S c,\quad J_F=1024,
$$
$$
 A_F=P_{J_F}M_FIP_{J_F},\qquad T_F=Id+A_F,\qquad
 F_J=M_FI-A_F .
 \tag{WCF.3}
$$
The polynomial $F$ has Fourier degree at most 192. Keep $T_F^{-1}$ in its original right position.

Write
$$
 R_S=c_i\otimes p_\psi-(c_ip_\psi)\otimes1,\qquad
 p_\psi=\psi-id-\langle\psi-id\rangle ,
$$
$$
 \mathcal F_{\rm fin}=\mathcal S F_JT_F^{-1}\mathcal S^{-1},
 \qquad
 \mathcal T_2=\mathcal S M_cIA_FT_F^{-1}\mathcal S^{-1}.
 \tag{WCF.4}
$$
For real functions, $(u\otimes v)x=u\langle vx\rangle$; complexification uses the corresponding dual pairing. WCE.14 is the complete identity
$$
 D_{\rm alg}
 =Q_a\mathcal V_wT_i-(h-1)\otimes\rho_i
   +Q_a\mathcal A_JP_h
           (R_S+\mathcal F_{\rm fin}-\mathcal T_2)
 :X_{-4/3}^{\rm fr}\longrightarrow Y^0 .
 \tag{WCF.5}
$$
It is the original physical coefficient error
$\mathcal L_\partial Y_{W,J}N_i-Q_aT_i$. No state error, old right normalization or leading scalar has been changed.

## WCF2. An actual finite factor for the root map

Let $K=1215=J_F+192-1$, and let $E_K:\mathbb R^{2431}\to L^2_{\rm real}$ be the isometric injection of the full real Fourier space $|j|\le K$, including its constant. Thus
$$
 Q_K=E_KE_K^*=Id-P_{1216}.
$$
The full matrix of $F_J$ in the complex Fourier basis is
$$
 (F_J)_{jk}=
 \begin{cases}
 \widehat F(j-k)\,[1-p_jp_k]/(i4k),&k\ne0,\\
 0,&k=0,
 \end{cases}
 \qquad p_j=\mathbf1_{\{|j|\ge1024\}} .
 \tag{WCF.6}
$$
If this entry is nonzero, $|j-k|\le192$ and at least one of $|j|,|k|$ is at most 1023. Both are therefore at most 1215. Consequently
$$
 F_J=Q_KF_JQ_K=F_JE_KE_K^* .
 \tag{WCF.7}
$$
The input constant happens to give a zero column, but the output mean of other columns is retained. No mean row is removed from (WCF.6).

Define the exact columns and rows
$$
 U_F=Q_a\mathcal A_JP_h\mathcal S F_JE_K,\qquad
 V_F=E_K^*T_F^{-1}\mathcal S^{-1}.
 \tag{WCF.8}
$$
Then
$$
 Q_a\mathcal A_JP_h\mathcal F_{\rm fin}=U_FV_F .
 \tag{WCF.9}
$$
Right multiplication by $T_F^{-1}\mathcal S^{-1}$ changes the dual rows. Thus $V_F$ is not declared to have finite Fourier input support. Likewise $\mathcal S,P_h,\mathcal A_J$ can give the columns $U_F$ high Fourier output. Neither $P_JU_F=0$ nor an ordinary-low formula for $V_F$ is inferred.

There is a smaller optional carrier on the actual reflected source. NIF.10--10a and 18a prove that $T_F^{-1}$ preserves $P_{97}$ and the root reflection and commutes with $D_+$. Therefore
$$
 T_F^{-1}\mathcal S^{-1}X_s^{\rm fr}
       \subset D_+\mathcal H_{\rm nat}^s .
 \tag{WCF.10}
$$
Let $E_{\rm ref}$ insert $D_+$ times the normalized real root-even modes $97,\ldots,1215$. It is an isometry with 1119 real coordinates. On this particular source,
$$
 F_JT_F^{-1}\mathcal S^{-1}
 =F_JE_{\rm ref}E_{\rm ref}^*T_F^{-1}\mathcal S^{-1}.
 \tag{WCF.11}
$$
One may replace $E_K$ by $E_{\rm ref}$ in (WCF.8). This does not discard either Fourier sign or the output mean. Its complexification has dimension 1119, not twice that number. It is a safe carrier dimension, not an assertion of the exact rank or a count of physical input columns. Outside this typed source, use (WCF.7)--(WCF.9).

## WCF3. Both primitive ranks and both physical-column rows

The two primitive ranks in (WCF.4) have the full factorization
$$
 \begin{split}
 U_S&=\bigl(Q_a\mathcal A_JP_hc_i,\
                   -Q_a\mathcal A_JP_h(c_ip_\psi)\bigr),\\
 V_Sx&=\bigl(\langle p_\psi x\rangle,\Pi x\bigr).
 \end{split}
 \tag{WCF.12}
$$
Hence $U_SV_S=Q_a\mathcal A_JP_hR_S$ as complete operators. On the actual source (WCF.1), the second row vanishes, and the first column may equivalently be written
$$
 Q_a\mathcal A_J\bigl(v_i-\nu_i(h-1)\bigr).
 \tag{WCF.13}
$$
This restriction is made after retaining both ranks. It does not make $\rho_i$ zero:
$$
 \rho_i(x)=\langle v_iIx\rangle
          =-\langle(Iv_i)x\rangle,\qquad x\in X^{\rm fr}.
 \tag{WCF.14}
$$

There is also an exact finite correction from the projection in front of $\mathcal T_2$. Define the complete row
$$
 \ell_2=\Pi\mathcal T_2
       =\Pi M_cIA_FT_F^{-1}\mathcal S^{-1}.
 \tag{WCF.15}
$$
The second equality is the density identity $\Pi\mathcal S=\Pi$. Since $\mathcal A_Jh=h$ and $Q_ah=h-1$,
$$
 -Q_a\mathcal A_JP_h\mathcal T_2
       =-Q_a\mathcal A_J\mathcal T_2+(h-1)\otimes\ell_2 .
 \tag{WCF.16}
$$
The sign of the added row is positive. The original physical density-mean term is still $-(h-1)\otimes\rho_i$.

Define
$$
 \boxed{\quad
 D_\infty=Q_a\mathcal V_wT_i-Q_a\mathcal A_J\mathcal T_2 .
 \quad}
 \tag{WCF.17}
$$
Then the complete same physical coefficient operator is
$$
 \boxed{\quad
 D_{\rm alg}
   =D_\infty+U_FV_F+U_SV_S
          -(h-1)\otimes\rho_i+(h-1)\otimes\ell_2 .
 \quad}
 \tag{WCF.18}
$$
Both terms of $D_\infty$ are the original ordered two-primitive operators. The complete $J_s=268435456$ compression and $\mathbf Z(0)$ stay in $\mathcal V_w$; the complete $A_F$ compression stays in $\mathcal T_2$.

For example use the explicit auxiliary space
$\mathbb F_{\rm alg}=\mathbb R^{2431}\oplus\mathbb R^2\oplus\mathbb R^2$ and set
$$
 \begin{split}
 \mathbf U_{\rm alg}
   &=\bigl(U_F,\ U_S,\ -(h-1),\ h-1\bigr),\\
 \mathbf V_{\rm alg}x
   &=\bigl(V_Fx,\ V_Sx,\ \rho_i(x),\ \ell_2(x)\bigr).
 \end{split}
 \tag{WCF.19}
$$
Thus $D_{\rm alg}=D_\infty+\mathbf U_{\rm alg}\mathbf V_{\rm alg}$. Redundant finite coordinates are harmless. On the actual source one can use (WCF.11), omit the zero second primitive row, and combine the last two rows into the exact row $\ell_2-\rho_i$, obtaining a carrier of at most 1121 real coordinates. Any bound for that combined row uses a complete direct estimate or the positive sum of its two row norms. It is never the difference of two upper bounds.

The mean functionals in (WCF.12), (WCF.14) and (WCF.15) are not the independent two stored physical mean entries or their matching equations. The column $h-1$ is nonconstant and mean-zero; the primitive target projection does not kill it.

## WCF4. Typed bounds for the exact finite columns and rows

Use the complete same-map constants of WCE, TF and WX. Write
$K_{F,-}$ for the saved full $T_F^{-1}$ norm on $H^{-4/3}$,
$K_{S,0}$ and $K_{S^{-1},-}$ for the selected density norms, and
$K_{\mathcal A,0}$ for the complete $\mathcal A_J$ forward norm.
Let $F^\#\ge\|F\|_\infty$. The complete primitive has norm $1/4$ on $L^2$, so
$$
 \|F_J\|_{2\to2}\le F^\#/2 .
$$
With normalized real Fourier injections, one valid joint pair of bounds is
$$
 \begin{split}
 \|U_F:\ell^2\to Y^0\|
  &\le K_{\mathcal A,0}K_{H^{-1},0}K_{S,0}F^\#/2,\\
 \|V_F:X_{-4/3}^{\rm fr}\to\ell^2\|
  &\le\Lambda_{1215}^{4/3}K_{F,-}K_{S^{-1},-}.
 \end{split}
 \tag{WCF.20}
$$
The row estimate is a joint finite Fourier embedding, with no extra square root of the number of modes. It is valid for either injection above. These are symbolic sufficient bounds; no old saved product is divided to infer a separate factor.

For the two primitive columns and their rows, sufficient bounds are
$$
 \begin{array}{c|c}
 \text{column or row}&\text{complete bound}\\ \hline
 U_{S,1}&K_{\mathcal A,0}K_{H^{-1},0}C_i^\#\\
 U_{S,2}&K_{\mathcal A,0}K_{H^{-1},0}C_i^\#P_\infty\\
 V_{S,1}&P_{43}\\
 V_{S,2}&1\\
 h-1&H_{\rm dev}=1/31\\
 \rho_i&R_i^\#
 \end{array}
 \tag{WCF.21}
$$
Here $P_{43}$, $P_\infty$, $C_i^\#$ and $R_i^\#$ have exactly their WCE.18--25 meanings. In particular the last row uses the already saved complete $C_I B_{i,1/3}$ product. The projected column (WCF.13) can instead use its complete WCE bound
$K_{\mathcal A,0}(d_{i,0}+\nu^\#H_{\rm dev})$.

Let
$$
 C_{2I}^{\rm root}
   \ge\|M_cIA_FT_F^{-1}:H^{-4/3}\to L^2\|
 \tag{WCF.22}
$$
be the completed WPC/WCE root-two-primitive record. The right inverse is already included. Equation (WCF.15) gives
$$
 \|\ell_2\|_{(X_{-4/3}^{\rm fr})^*}
       \le C_{2I}^{\rm root}K_{S^{-1},-}.
 \tag{WCF.23}
$$
There is no $K_{S,0}$ in this particular row bound because $\Pi\mathcal S=\Pi$. The infinite operator in (WCF.17) does require its left density norm.

All columns in (WCF.19) are true $L^2$ vectors in $Y^0$, and all rows are bounded on the actual negative source. Thus their restriction to $L^2$ is bounded as well. They are real maps with the original Fourier conjugacy; complexification creates no second physical copy. No smoothness of the transformed columns is needed beyond these established types.

## WCF5. A direct new bound using only completed scalar inputs

Read the complete saved physical two-primitive row bound
$$
 C_{wI}\ge\|Q_a\mathcal V_wT_i\|_{X_{-4/3}^{\rm fr}\to L^2}.
$$
Equations (WCF.4), (WCF.17) and (WCF.22) prove the direct positive estimate
$$
 \boxed{\quad
 C_{D,\infty}
 :=C_{wI}
   +K_{\mathcal A,0}K_{S,0}
                  C_{2I}^{\rm root}K_{S^{-1},-}
 \ \ge\|D_\infty\|_{X_{-4/3}^{\rm fr}\to Y^0}.
 \quad}
 \tag{WCF.24}
$$
This estimate has no $P_h$ norm, finite-map norm, primitive-rank norm or physical density-row norm. Those operators remain in (WCF.19), rather than being omitted. The intermediate identity (WCF.5) supplies a second way to check (WCF.18); it does not authorize an entrywise minimum between bounds for different infinite remainders.

The already successful WPC/WCE science contains all five numerical inputs for (WCF.24), plus the inputs for (WCF.23):

| Symbol | Exact field inside the completed science |
|---|---|
| $C_{wI}$ | complete_wce_waist_conclusion.complete_physical_two_primitive_row_upper |
| $K_{\mathcal A,0}$ | complete_wce_waist_conclusion.complete_waist_forward_L2_upper |
| $C_{2I}^{\rm root}$ | complete_wce_root_coefficient_conclusion.complete_root_two_primitive_fee_upper |
| $K_{S,0}$ | copied_original_scalar_records.WCE.S_L2 |
| $K_{S^{-1},-}$ | copied_original_scalar_records.WCE.S_inverse_Hminus4_3 |

The last two records are copied verbatim from WX. Their immutable meanings are respectively
complete_selected_common_input_conclusion.complete_common_input_L2_upper and
complete_selected_common_input_conclusion.complete_common_input_inverse_Hminus4_3_upper.
The successful schema and each full record must be checked; neither map norm is reconstructed.

The completed science is
notes/positive_cutoff_and_reflected_coefficient_refinement_ci/run-43812987299-1/actual-scientific-conclusion.json,
blob 3d6fbe7cb3c345f5fd4631428e4189823d05684a, 55533 bytes,
SHA256 e2cb2aacc031532e3b4db92873b404e9550599da75427dbb3c6448b65120d88d.
It is the original complete 38-field, 22-gate success. Both whole $D_{\rm alg}$ candidates and their selected record remain unchanged. Formula (WCF.24) is a new scalar target for a different explicitly defined remainder, not a correction to either old whole bound.

No value of (WCF.23) or (WCF.24) is evaluated here. No old coefficient conversion, root inverse, chart, exponential, logarithm, propagator, source integral or successful scalar graph is run again.

## WCF6. The same physical row, combined with the finite root factor

Use WFR's complete root factor
$$
 U_*=-\mathcal B^{-1}L_\partial\mathcal R_*E_*,
 \qquad V_*^{\rm src}=V_*N_i\mathcal W^{-1}\mathcal A .
 \tag{WCF.25}
$$
Here $E_*$ is the chosen exact WFR root-trace injection, $V_*=E_*^*P_F\mathcal H_*$, and $\mathcal R_*$ is the full root receiver. Its physical sign, both curvature rows and both stored output means remain WFR's. Nothing in the coefficient factor (WCF.19) duplicates this independent root response.

Define the complete remaining physical strong operator
$$
 E_{\partial,\infty}
   =D_\infty
       +L_\partial(R_++T_{\rm neg}+E_{\rm end})N_i .
 \tag{WCF.26}
$$
The positive correction, the complete WUB volume and every genuine jump, and all four WES endpoint terms remain. The root shear and genuine reference correction inside those unchanged terms are not discarded. Only the separate finite root factor of WFR and the exact finite coefficient factor have been extracted.

Put $\mathcal R=\mathcal W^{-1}\mathcal A$ for the actual right source map; this symbol is distinct from WGB's coordinate isomorphism
$\mathcal U=\mathcal A^{-1}\mathcal W\mathcal S D_+$.
The exact same WBP physical row is
$$
 \widetilde{\mathcal B}_{\rm ss}
   =M_\nu+E_\infty^{\rm all}
             +\mathcal B^{-1}\mathbf U_{\rm alg}
                                  \mathbf V_{\rm alg}\mathcal R
             +U_*V_*^{\rm src},
$$
$$
 E_\infty^{\rm all}
  =\mathcal B^{-1}\bigl[
      Q_a\mathcal R_{\rm ss}
      +Q_aT_i(\mathcal W^{-1}-Id)\mathcal A
      +E_{\partial,\infty}\mathcal R\bigr].
 \tag{WCF.27}
$$
Every factor has its original side. In particular no second $N_i$ is applied to $D_\infty$ or to $\mathbf V_{\rm alg}$.

Use complete WFR/WUE symbols in their original units. A sufficient direct budget is
$$
 C_{\partial,\infty}
  =C_{D,\infty}
      +K_\partial K_{N,-}
                  (C_+^w+C_{{\rm neg},4/3}+C_{\rm end}),
$$
$$
 C_{\infty,r}^{\rm all}
  =K_{B,0}\left[
       C_r+K_{i,0}^{\rm fwd}C_{W^{-1}-Id}K_{A,-}
       +C_{\partial,\infty}K_{W^{-1},-}K_{A,-}
          \right],\qquad r\in\{\mathrm{unc},\mathrm{col}\}.
 \tag{WCF.28}
$$
The two $C_r$ are the complete WBP bounds for the same $\mathcal R_{\rm ss}$. Any refined WIR bound must be for the same $\mathcal W^{-1}$ or its same strong difference in the indicated window. The received $C_+^w$ is not multiplied by its receiver again. Quantitative negative-source and endpoint constants remain their own new complete targets.

Only complete candidates for this same $E_\infty^{\rm all}$ can be compared. Its root, finite-map, conjugation-rank and density-row factors are excluded from (WCF.28) precisely because they appear as exact factors in (WCF.27).

## WCF7. Exact graph transport and the reduced high block

Keep the WFI/WGB graph
$$
 \mathcal D=\{x\in X_b^{-1}:\overline Mx\in Y^0\},\qquad
 \overline G=\overline M^{-1},\qquad
 \mathcal D_{\rm true}=\widetilde P\mathcal D .
 \tag{WCF.29}
$$
The reference $\overline M=M_\nu P_{97}+L_{\rm low}Q_{97}$ is not a physical low-input map. WFI proves its bounded forward action on $L^2$ and its inverse $Y^0\to\mathcal D\hookrightarrow H^{-1}$.

The right map has the correct true domain:
$$
 \mathcal R\mathcal U=\mathcal S D_+,\qquad
 \mathcal R\widetilde X_s=X_s^{\rm fr}.
 \tag{WCF.30}
$$
Thus $\mathbf V_{\rm alg}\mathcal R\widetilde P\overline G$ is a bounded row vector on $Y^0$. The sequence is
$Y^0\to\mathcal D\to H^{-1}\hookrightarrow H^{-4/3}$,
then the actual projection and right map into $X_{-4/3}^{\rm fr}$.
No physical error is extended outside its qualified input by notation.

Define
$$
 \begin{split}
 \widehat U_{\rm alg}&=\mathcal B^{-1}\mathbf U_{\rm alg},&
 \widehat V_{\rm alg}&=\mathbf V_{\rm alg}
                            \mathcal R\widetilde P\overline G,\\
 \widehat V_*&=V_*^{\rm src}\widetilde P\overline G,&
 \mathbf U_{\rm tot}&=(\widehat U_{\rm alg},U_*),\qquad
 \mathbf V_{\rm tot}=(\widehat V_{\rm alg},\widehat V_*)^t .
 \end{split}
 \tag{WCF.31}
$$
The left inverse $\mathcal B^{-1}$ acts on $L^2$; $\mathcal R$ acts in the negative source window. Each transformed column still belongs to $Y^0$, and each transformed row is bounded on $Y^0$. Coordinate bounds may be multiplied in this order; no density map is commuted through a cutoff or graph inverse.

The reference extension of the same physical row is exactly
$$
 Id+K_\infty+\mathbf U_{\rm tot}\mathbf V_{\rm tot},
$$
$$
 K_\infty
  =\big[(M_\nu-\overline M)+E_\infty^{\rm all}\big]
                         \widetilde P\overline G .
 \tag{WCF.32}
$$
This follows from (WCF.27), not from a decomposition of saved norms. $K_\infty$ is compact by the same $H^{-1}\hookrightarrow H^{-4/3}$ graph embedding as WFI.

For $J\ge97$, the exact range of $M_\nu-\overline M$ lies in the ordinary low target. Hence
$$
 P_J(M_\nu-\overline M)=0,\qquad
 H_J^\infty
   =Id_{P_J}+P_JE_\infty^{\rm all}
                         \widetilde P\overline G P_J .
 \tag{WCF.33}
$$
The complete sufficient high test is
$$
 \chi_{J,r}^{\infty}
    :=2K_{\rm CYA}C_{\infty,r}^{\rm all}
                       K_{\widetilde P,-}\Lambda_J^{-1/3}<1,
 \qquad
 \|(H_J^\infty)^{-1}\|\le(1-\chi_{J,r}^{\infty})^{-1}.
 \tag{WCF.34}
$$
No smallness of
$P_J\mathbf U_{\rm tot}\mathbf V_{\rm tot}P_J$
is assumed. It stays in the auxiliary equations. In particular none of the transformed finite columns is declared to have low output. Formula (WCF.34) is conditional: no new cutoff or numerical verdict is given.

## WCF8. The complete finite equations and remaining data

For the original homogeneous high column, the same WGB constraint is
$$
 \Theta u=0,\qquad\Theta=V_Q\overline G .
$$
The exact reference-coordinate system is now
$$
 (Id+K_\infty)u+\mathbf U_{\rm tot}z=f,\qquad
 z=\mathbf V_{\rm tot}u,\qquad\Theta u=0 .
 \tag{WCF.35}
$$
The vector $z$ is determined by $u$. It is not a new freely prescribed physical input or the original radial mean function.

Under the complete test (WCF.34), use WFR.21--22 with
$K^\circ=K_\infty$, $U_*=\mathbf U_{\rm tot}$ and
$V=\mathbf V_{\rm tot}$. This retains all high-column responses and cross terms. The auxiliary row has right side
$+\mathbf V_{\rm tot}P_J(H_J^\infty)^{-1}P_Jf$,
whereas the 96 zero constraints have right side
$-\Theta P_J(H_J^\infty)^{-1}P_Jf$.
They are different equations.

If genuine 96 additional physical columns are supplied, append their exact WGB factor
$(H_{\rm phys}-\overline M C_Q)V_Q\overline G$.
In that physical augmented realization the finite coordinates are encoded once, and the resulting square uses the full WGB/RNS $(q,z,\varkappa)$ system. A reference column $\overline M C_Q$, a coefficient-factor column, or a root impulse response is not a substitute for an unknown physical Poisson column.

The scalar metric row, physical mean and amplitude matching, exterior conditions and their high feedback remain. If those equations are appended, their true action on every auxiliary factor must also be appended; no zero extension to the other output ports is inferred from this primitive-row calculation. Any unresolved radial head or mean function remains infinite-dimensional until a complete bounded elimination has been proved.

Actual finite entries still require new qualified data:

| Factor | Exact data required for finite pairings |
|---|---|
| $F_J$ | True root polynomial Fourier coefficients and (WCF.6), including its output mean |
| $U_F$ | The actual selected density, projected waist second normalizer and left target coordinate applied to each finite column |
| $V_F$ | The true ordered inverse $T_F^{-1}\mathcal S^{-1}$, or its complete adjoint rows |
| $U_S,V_S$ | The actual $c_i,p_\psi,h$ and both primitive pairings before typed restriction |
| $\rho_i,\ell_2$ | Their exact dual rows (WCF.14)--(WCF.15), including any later graph and source compositions |
| $U_*,\widehat V_*$ | The independent complete root responses and root trace rows of WFR |
| Physical border | Actual finite physical columns and all matching/parameter rows in the same output units |

A list of scalar norm uppers does not determine these entries. Bounds (WCF.20)--(WCF.23) qualify the factorization and its graph types; they do not certify a finite determinant. Redundant auxiliary variables can be retained without altering equivalence to the exact operator.

## WCF9. Immutable evidence and precise scope

| Source | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WCE: exact same physical coefficient error and original finite/mean terms | 7519a36a72fe5775de8dcacb7812f48a42e73d3b | 22798 | 3d77e17b15a2dd37c7c66d969d28c50edc5dcbaa7608d6686477ac322ebc0bcf |
| NIF: actual density-reflected source and root-normalizer parity | d606faa1ffd30c34d3487985a57dbc62a18890bc | 32942 | 8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640 |
| WBP: exact source/target normalizers and complete same-row error | 54f859b305861a1c4be4be7826c059e1e4ffc3e8 | 18114 | 19f0182fb19cb3842948ee427993f7478af0557f2ec790c7c2f8ce5849015a7e |
| WFI: qualified graph and transported finite complement | aec7503e379c3abcbb66b33ed0a7e68be39703fa | 23476 | 7abf7f41df8fc48872c82b420836947a0728698d5142ac939c4d2d5ff99c4309 |
| WGB: exact graph parameterization and full physical finite border | 30cd8f7858888c35f942094611614c9f74b3e2af | 25135 | e7d23c583205fcb538fd21260e2e9c5b4859ed73ab6129a453b8c5d1fb05bf7c |
| WFR: independent exact root finite factor | 66557b3eb76c002dedbb7189a197a5a066ec0201 | 16083 | cb72cb37e284e8e4b4c834896b1437ee6400d78a9f8fe5321e75e4b4dac0fcde |
| Complete WPC/WCE actual scalar success | 3d6fbe7cb3c345f5fd4631428e4189823d05684a | 55533 | e2cb2aacc031532e3b4db92873b404e9550599da75427dbb3c6448b65120d88d |

The conclusion is the exact decomposition (WCF.18), its typed finite factors, the new direct remainder formula (WCF.24), and their correctly ordered insertion into (WCF.27)--(WCF.35). It does not alter the selected parameter, change the genuine trial, prove an incoming inverse, close the physical finite system or establish a nonlinear solution.
