# R133 supplement: the same physical coefficient error from complete terminal and normalizer bounds

2026-11-16, visible-exact / phase_inverse.

**Proved exact identities and a complete new positive scalar recipe at the original selected real member. No new numerical evaluation is asserted.** The coefficient-only physical error in WUE.27 can be bounded directly from the completed individual incoming coefficient, the completed common-root normalizer factors, the actual selected density map, and the completed waist normalizer. This gives two complete candidates for the same operator and the same leading row. It does not alter the global genuine trial, rerun its source calculation, or identify a physical inverse.

The original two primitive-conjugation ranks, the full root finite map, the ordered two-primitive term, the physical density-mean row, the actual waist second normalizer, and the original transported input complement are retained. One candidate uses both full conjugation ranks throughout. The second uses the exact zero-mean property of the actual density-transported input only after the complete operator has been written.

## WCE1. The unchanged source, target and physical operator

Work at the same selected real member as WPL, WUE, SEI and WX. The circle has period $\pi/2$, normalized measure, physical Fourier frequencies $4j$, and Bessel weights $\Lambda_j=(1+16j^2)^{1/2}$. Put
$$
 \Pi f=\langle f\rangle,\qquad P=Id-\Pi,\qquad
 I=\partial_\phi^{-1}P,\qquad
 U_\psi f=\psi'(f\circ\psi).
 \tag{WCE.1}
$$
Every $U$ in this note is the full density map. It is not ordinary composition and is not an identity extension on the scalar mean.

Retain the actual selected map and natural input space:
$$
 \mathcal S=U_{\mathcal H^{-1}}U_{X_-}=U_\psi,\qquad
 \psi=X_-\circ\mathcal H^{-1},\qquad
 X_s^{\rm fr}=\mathcal S D_+\mathcal H_{\rm nat}^s,
 \quad
 D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_- .
 \tag{WCE.2}
$$
Here $\mathcal H_{\rm nat}^s=P_{97}\operatorname{Fix}(R_*)\cap H^s$ is the original reflected root space, with its real Fourier conjugacy retained. Its complexification may be used for the estimates. The norm on $X_s^{\rm fr}$ is the inherited ambient $H^s$ norm. Neither its reflected projector nor its carrier projector is replaced by an ordinary Fourier projector in the selected angle.

A full degree-one density map preserves the normalized integral:
$$
 \Pi U_\psi f=\Pi f .
 \tag{WCE.3}
$$
This follows by the exact change of variable $y=\psi(x)$, and extends to the distributional Sobolev spaces by duality and density. Consequently
$$
 \Pi x=0\quad\text{for every }x\in X_s^{\rm fr}.
 \tag{WCE.4}
$$
Indeed $D_+$ preserves the nonzero root frequencies and $\mathcal H_{\rm nat}^s$ has no zero frequency. This argument would not hold for an ordinary pullback $f\circ\psi$.

Use the unchanged WPL notation
$$
 \begin{gathered}
 h=U_{\mathcal H^{-1}}1,\qquad P_h=Id-h\Pi,\qquad
 Q_a=P\Pi_a^+,\qquad \Pi_a^+=(Id+R_a)/2,\\
 T_i=Id+M_{c_i}I,\qquad c_i=\nu_i+v_i,\qquad
 \Pi v_i=0,\quad \nu_i=-\mu/2,\qquad
 \rho_i=\Pi T_i|_{X^{\rm fr}},\\
 \mathcal A_J=Id+\mathcal V_w .
 \end{gathered}
 \tag{WCE.5}
$$
The identities $\Pi h=1$, $R_a h=h$, $\mathcal V_wh=0$ and $\Pi\mathcal V_w=0$ are the exact WPL waist identities. In particular $Q_ah=h-1$. The prescribed target is
$Y^0=P\operatorname{Fix}(R_a)\cap L^2$.

The operator to be bounded is exactly
$$
 D_{\rm alg}
 =\mathcal L_\partial Y_{W,J}N_i-Q_aT_i
 :X_{-4/3}^{\rm fr}\longrightarrow Y^0 ,
 \tag{WCE.6}
$$
with the same compressed SW trial $Y_{W,J}$, physical readout $\mathcal L_\partial$, and right input map
$N_i=\Lambda_+^{-1}T_F^{-1}\mathcal S^{-1}$ as WUE.26--28. There is no state error in $D_{\rm alg}$. The positive correction, global negative source, jumps and genuine endpoint comparison belong to the separate complete state term in WUE.34.

## WCE2. Exact common-root algebra with the full finite map

Let $C=C_+(0)$ be the single complete root coefficient in SW.27, including its scalar mean and the common finite function
$$
 F=F_*=\frac{\beta_*u_*v_*}{\eta_*},\qquad
 c=C-F,\qquad c_i=\mathcal S c .
 \tag{WCE.7}
$$
All quantities refer to the original root gauge. The full $v_*$ mean is included. The finite angular degree of $F$ is at most192.

Keep the successful root cutoff $J_F=1024$ and define
$$
 \begin{gathered}
 A_F=P_{J_F}M_FIP_{J_F},\qquad T_F=Id+A_F,\\
 F_J=M_FI-A_F,\qquad
 R_F=(F_J-M_cIA_F)T_F^{-1}.
 \end{gathered}
 \tag{WCE.8}
$$
The exact ordered identity IC.9, applied to the exact single-first-symbol map of SW, is
$$
 (Id+M_CI)T_F^{-1}=Id+M_cI+R_F .
 \tag{WCE.9}
$$
For verification,
$Id+M_CI=T_F+M_cI+F_J$ and
$M_cIT_F^{-1}=M_cI-M_cIA_FT_F^{-1}$.
No factor is commuted through $T_F^{-1}$.

Both input and output support of $F_J$ lie in $|j|\le J_F+191=1215$ before right multiplication by $T_F^{-1}$. Its mean output is included. The map $F_JT_F^{-1}$ remains finite rank, but its dual rows are not declared to retain that finite input support. Their complete strong fee has already been evaluated by TF.

The coefficient trial in (WCE.9) is exactly $Id+M_CI$. Thus the additional $E_\sigma$ in the general IC.8 statement is zero for this particular algebraic trial. This fact says nothing about the physical state error or the complete error of a genuine solution.

## WCE3. Both primitive ranks and the actual projection

Put
$$
 p_\psi=\psi-id-\langle\psi-id\rangle .
$$
IC.16 gives the exact full-circle identity
$$
 \mathcal S M_cI\mathcal S^{-1}=M_{c_i}I+R_S,\qquad
 R_S=c_i\otimes p_\psi-(c_ip_\psi)\otimes1 .
 \tag{WCE.10}
$$
Here $(u\otimes v)f=u\langle vf\rangle$, with the usual conjugation when expressed as a Hermitian dual row. Both terms are present, including the constant functional. Therefore
$$
 \begin{gathered}
 E_0=R_S+\mathcal S R_F\mathcal S^{-1},\\
 \mathcal S(Id+M_CI)T_F^{-1}\mathcal S^{-1}=T_i+E_0 .
 \end{gathered}
 \tag{WCE.11}
$$

The actual decoded plus component contains the original moving-circle projection. Since
$U_{\mathcal H^{-1}}P U_{X_-}=P_h\mathcal S$, WUE.26 becomes
$$
 T_i+E_{\rm coeff}=P_h(T_i+E_0).
 \tag{WCE.12}
$$
In particular
$$
 E_{\rm coeff}=P_hE_0-h\otimes\rho_i,\qquad
 P_hE_{\rm coeff}=P_hE_0
 \quad\text{on }X^{\rm fr}.
 \tag{WCE.13}
$$
Only the projected errors in the second identity are equal. It would be incorrect to identify the two full-circle errors $E_{\rm coeff}$ and $E_0$.

Substituting (WCE.13) into the already proved WUE.27 yields the complete same-row formula
$$
 \boxed{\;
 D_{\rm alg}
 =Q_a\mathcal V_wT_i
       -(h-1)\otimes\rho_i
       +Q_a\mathcal A_JP_h
          \bigl(R_S+\mathcal S R_F\mathcal S^{-1}\bigr).
 \;}
 \tag{WCE.14}
$$
The physical mean rank in its middle term has not been removed by input mean zero. Its functional is generally nonzero.

There is a useful exact projection bound. Write any $f=a\,1+u_0$ with $\Pi u_0=0$ and $h=1+h_0$. Then
$P_hf=u_0-a h_0$. The norm of this row operator from
$\mathbb C\oplus L^2_0$ to $L^2_0$ is
$$
 \|P_h\|_{L^2\to L^2}
 =\sqrt{1+\|h_0\|_2^2}=\|h\|_2
 \le K_{H^{-1},0}.
 \tag{WCE.15}
$$
Here $K_{H^{-1},0}$ is the saved complete norm of $U_{\mathcal H^{-1}}$. This is an exact Hilbert-space calculation, not a subtraction of two upper bounds.

Now, and only now, restrict (WCE.10) to (WCE.4). The second input functional vanishes on that source and
$$
 P_hR_S|_{X^{\rm fr}}
  =\bigl(v_i-\nu_i(h-1)\bigr)\otimes p_\psi .
 \tag{WCE.16}
$$
This uses $P_hc_i=v_i-\nu_i(h-1)$. It neither removes an independently supplied physical mean input nor declares $\rho_i$ zero.

The original selected bound
$31/32\le\mathcal H'\le33/32$ gives
$$
 \|h-1\|_2\le\|h-1\|_\infty\le H_{\rm dev}:=\frac1{31}.
 \tag{WCE.17}
$$
The reason is $h=(\mathcal H^{-1})'=1/(\mathcal H'\circ\mathcal H^{-1})$. This uses the same true selected chart as the old WX receipt.

## WCE4. Completed terminal bounds and the two root costs

Read, without reconstructing their old arithmetic, complete bounds
$$
 \begin{gathered}
 C_i^\#\ge\|c_i\|_\infty,\qquad
 M_\mu\ge|\mu|,\qquad
 d_{i,0}\ge\|v_i\|_2,\qquad
 H_{i,2}\ge\|v_i\|_{H^2},\\
 R_i^\#\ge C_I W_{1/3}(v_i),\qquad C_I=\sqrt{17}/4 .
 \end{gathered}
 \tag{WCE.18}
$$
All five are already saved by SEI. In particular $C_i^\#$ is its full actual coefficient bound; it is not recomputed as $|\mu|/2+\|v_i\|_\infty$. The field for $H_{i,2}$ is the complete Bessel $H^2$ bound, not merely the zeroth derivative or a pointwise value. The field for $R_i^\#$ is the already evaluated complete product named complete_CI_B_upper, not a new multiplication of two old inputs.

Set $\nu^\#=M_\mu/2$. The complete signed $\mu$ record remains a provenance input for $\nu_i=-\mu/2$. Using the full nonzero signed spectrum in IC.29 gives
$$
 W_{4/3}(v_i)\le\frac{243}{160}H_{i,2},\qquad
 K_{i,-}:=1+\frac14
       \left(\nu^\#+\frac{243}{160}H_{i,2}\right)
       \ge\|T_i\|_{H^{-4/3}\to H^{-4/3}} .
 \tag{WCE.19}
$$
Only this displayed positive combination is new. The $1/4$ is the ordinary same-window norm of the complete primitive, not a gain assigned to the output of a coefficient.

On (WCE.4), integration by parts gives
$\rho_i(x)=\langle v_iIx\rangle=-\langle(Iv_i)x\rangle$.
Thus
$$
 \|\rho_i\|_{(X_{-4/3}^{\rm fr})^*}
 \le\|Iv_i\|_{H^{4/3}}
 \le C_IW_{1/3}(v_i)\le R_i^\# .
 \tag{WCE.20}
$$
This retains the full scalar mean functional of the physical decoded state.

Let $m_\psi>0$ be the saved true lower bound for $\inf\psi'$. Since $c_i=\psi'(c\circ\psi)$,
$$
 c_\infty^\#:=C_i^\#/m_\psi\ge\|c\|_\infty .
 \tag{WCE.21}
$$
A directed computation must use the positive lower endpoint of $m_\psi$. No inverse is inferred from an upper derivative bound.

TF has already saved two complete after-right-inverse factors:
$$
 \begin{split}
 B_{2I}&\ge
  \alpha_{J_F}m_{F,-1/3}K_{F,-4/3},\\
 B_{\rm fin}&\ge
  2C_I\|F\|_\infty\Lambda_{J_F+191}^{1/3}K_{F,-4/3},
 \qquad
 \alpha_{J_F}=\frac{\Lambda_{J_F}^{4/3}}{(4J_F)^2}.
 \end{split}
 \tag{WCE.22}
$$
The first pays $M_cIA_FT_F^{-1}$ per unit $\|c\|_\infty$, with
$H^{-4/3}\to H^{-1/3}\to H^{2/3}\to L^2$ in the original order. The second pays the entire $F_JT_F^{-1}$. Therefore
$$
 C_F^\#=c_\infty^\#B_{2I}+B_{\rm fin}
       \ge\|R_F\|_{H^{-4/3}\to L^2}.
 \tag{WCE.23}
$$
There is no further $T_F^{-1}$ factor in (WCE.23).

Use WX's saved $K_{S,0}$ and $K_{S^{-1},-}$ to define
$$
 C_S^\#=K_{S,0}C_F^\#K_{S^{-1},-}
       \ge\|\mathcal S R_F\mathcal S^{-1}\|_{H^{-4/3}\to L^2}.
 \tag{WCE.24}
$$
The actual left and right density maps are charged once in their respective windows.

Finally read WX's complete displacement bounds
$P_{43}\ge\|p_\psi\|_{H^{4/3}}$ and
$P_\infty\ge\|p_\psi\|_\infty$. The two complete rank candidates are
$$
 \begin{split}
 C_{\rm rank}^{\rm full}
    &=C_i^\#(P_{43}+P_\infty)
       \ge\|R_S\|_{H^{-4/3}\to L^2},\\
 C_{\rm rank}^{\rm projected}
    &=(d_{i,0}+\nu^\#H_{\rm dev})P_{43}
       \ge\|P_hR_S|_{X_{-4/3}^{\rm fr}}\|_{H^{-4/3}\to L^2}.
 \end{split}
 \tag{WCE.25}
$$
The first uses normalized $\|c_i\|_2\le\|c_i\|_\infty$ and retains both ranks. The second follows from the exact operator (WCE.16), not from subtracting any part of the first bound.

## WCE5. The actual waist second normalizer, with no new jets

Keep the original moving cutoff $J_s=268435456$. Write the same WT operators at the right waist trace as
$$
 A_1=P_{J_s}\mathbf S(0)IP_{J_s},\qquad
 A_2=P_{J_s}\mathbf Z(0)I^2P_{J_s},\qquad
 \mathscr T_{J_s}(0)=(Id+A_1)(Id+A_2).
 \tag{WCE.26}
$$
They are extended by the identity on the moving finite complement and the two adjoined physical means. The cutoff is neither 97 nor the root cutoff 1024.

WPL.32--37 proves the actual operator identity $\mathbf S(0)=0$: the original metric has exact radial parity and genuine differentiability at the waist, and the compact metric perturbation is supported away from it. Hence
$$
 A_1=0,\qquad
 \mathscr T_{J_s}(0)-Id=A_2 .
 \tag{WCE.27}
$$
The term $\mathbf Z(0)$, which includes $-\mathbf S_r(0)$, is not zeroed.

The successful WT fixed-$J_s$ row already contains
$$
 \begin{gathered}
 R_{w,2}\ge\|(Id+A_1)A_2\|_{H^{-4/3}\to L^2},
 \qquad
 \tau_{w,2}\ge\|A_2\|_{L^2\to L^2}.
 \end{gathered}
 \tag{WCE.28}
$$
Its first bound is precisely TN.20 with the complete new waist coefficients: the source computes
$(1+\tau_{1,0})\gamma_{J_s}^2\Lambda_{J_s}^{-2/3}m_{2,2/3}$.
Its saved name is forward_complete_strong_remainder. It is not the separate first_symbol_finite_strong_fee. By (WCE.27), the entire old $R_{w,2}$ is a valid bound for the actual $A_2$, even if the old upper bound for $\mathbf S(0)$ was positive. Nothing is subtracted from either old number.

Restrict the matrix operator to reflected pairs $E_Rv=(v,Rv)$. It preserves this subspace, and
$\|E_Rv\|_{H^s\oplus H^s}=\sqrt2\|v\|_{H^s}$ on both sides. Thus no extra component factor is needed for the scalar restriction
$B_w=P_{J_s}M_{\mathbf Z_{+,-}(0)}I^2P_{J_s}R$.
WPL.38 gives
$\mathcal V_w=U_{\mathcal H^{-1}}B_wU_{\mathcal H}$.
Read the saved complete density norms and form
$$
 \begin{split}
 \delta_w^\#
   &=K_{H^{-1},0}R_{w,2}K_{H,-4/3}
       \ge\|\mathcal V_w\|_{H^{-4/3}\to L^2},\\
 K_{\mathcal A,0}^\#
   &=1+K_{H^{-1},0}\tau_{w,2}K_{H,0}
       \ge\|Id+\mathcal V_w\|_{L^2\to L^2}.
 \end{split}
 \tag{WCE.29}
$$
The identity part in the second formula is exact. These are new positive products of already completed same-waist quantities. No cut constant is moved to the waist, no new radial derivative of $u,v$ is needed, and no old strong remainder is recomputed.

## WCE6. Two complete bounds for the same physical error

Define the complete physical-row contribution
$$
 C_{\rm row}^\#
       =\delta_w^\#K_{i,-}+H_{\rm dev}R_i^\# .
 \tag{WCE.30}
$$
Equations (WCE.14)--(WCE.29) prove both
$$
 \boxed{\;
 C_{\rm alg}^{\rm full}
   =C_{\rm row}^\#
       +K_{\mathcal A,0}^\#K_{H^{-1},0}
          (C_{\rm rank}^{\rm full}+C_S^\#)
       \ge\|D_{\rm alg}\|_{X_{-4/3}^{\rm fr}\to Y^0},
 \;}
 \tag{WCE.31}
$$
and
$$
 \boxed{\;
 C_{\rm alg}^{\rm projected}
   =C_{\rm row}^\#
       +K_{\mathcal A,0}^\#
          (C_{\rm rank}^{\rm projected}+K_{H^{-1},0}C_S^\#)
       \ge\|D_{\rm alg}\|_{X_{-4/3}^{\rm fr}\to Y^0}.
 \;}
 \tag{WCE.32}
$$
Their common row and root terms are already complete. The first candidate estimates the full auxiliary conjugation ranks before restricting to the physical source. The second uses exactly (WCE.4) and (WCE.16). Both preserve the same physical mean rank in (WCE.30).

After the complete final upper records have been saved, their whole minimum is another bound for this same operator. No entrywise mixing with an old coefficient/state budget is used. If the complete old WUE.29 candidate is also evaluated in exactly these coordinates, it may be compared as a whole; the scalar CG coefficient fee alone is not the same operator as $D_{\rm alg}$.

These estimates restrict to $X_{-\sigma}^{\rm fr}$ for $1<\sigma\le4/3$ by the ambient Bessel embedding, without a new source-space identification. They replace only $C_{\rm alg}$ in WUE.34. The complete positive/root products, WUB source blocks, every jump, WES endpoint terms and the original $N_i$ factor in the state contribution retain their own places. In particular the coefficient part does not receive a second $N_i$, $T_F^{-1}$, or nonunit leading scalar.

## WCE7. Exact completed inputs for a future scalar consumer

All paths below are relative to topics/visible-flex-exact-nearby/. The four objects are complete original successes; they are not prefix receipts or excerpts.

| Role and exact path | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| SEI execution: notes/individual_principal_energy_terminal_density_ci/run-43773319871-1/execution.json | e1532b816ea344ee65e52a503279376a0c449299 | 46192 | b0088f831471f29d41624e487586fbb9f4801ef7837f9b4dd3c29a57e51b3d29 |
| TF science: notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-scientific-conclusion.json | 3766aea85aba59230be3813b4b7634d318316e49 | 18206 | a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720 |
| WX execution: notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json | 5121a599896025d90e2861450756a256aaba659d | 43753 | e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12 |
| WT science: notes/waist_normalizer_coefficients_ci/run-43763134339-1/actual-scientific-conclusion.json | b742d3167f68c05ef197450a3112eb5b8edcacac | 27619 | 2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d |

For SEI and WX, use actual_scientific_receipt inside the execution. TF and WT are standalone mathematical objects. Their complete gate counts are respectively 20, 14, 20, 20, and their successful child return codes are zero. Retain their original source/manifest/runtime and parameter identities; do not impose another producer's schema on WX.

The following abbreviations refer to exact object paths, not recomputed intermediate quantities:

- SI = SEI.actual_scientific_receipt.
- SI.N = SI.complete_new_individual_nonmean_budget_conclusion.branches.incoming.
- SI.D = SI.complete_new_individual_density_derivative_conclusion.
- SI.E = SI.complete_new_signed_energy_conclusion.branches.incoming.
- WX.S = WX.actual_scientific_receipt.complete_selected_common_input_conclusion.
- WX.H = WX.actual_scientific_receipt.complete_selected_H_coordinate_conclusion.
- WX.P = WX.actual_scientific_receipt.complete_full_primitive_rank_conclusion.selected_common_input.
- TF.B = TF.complete_new_strong_scalar_factors.
- WT.J = the unique entry of WT.complete_fixed_cutoff_results with J equal to 268435456.

| New-recipe symbol | Exact saved field, followed by .ball unless stated otherwise |
|---|---|
| $C_i^\#$ | SI.N.complete_actual_coefficient_Linfty_upper |
| $M_\mu$ | SI.D.complete_absolute_mu_upper |
| $d_{i,0}$ | SI.D.branches.incoming.complete_actual_nonmean_derivative_L2_upper[0] |
| $H_{i,2}$ | SI.N.complete_Bessel_H0_H1_H2_H3_upper[2] |
| $R_i^\#$ | SI.E.complete_CI_B_upper |
| $B_{2I}$ | TF.B.complete_two_primitive_left_multiplier_fee_after_right_inverse |
| $B_{\rm fin}$ | TF.B.complete_finite_map_fee_after_right_inverse |
| $m_\psi$ | WX.S.common_input_derivative_lower |
| $K_{S,0}$ | WX.S.complete_common_input_L2_upper |
| $K_{S^{-1},-}$ | WX.S.complete_common_input_inverse_Hminus4_3_upper |
| $P_{43}$ | WX.P.complete_zero_mean_displacement_H2_and_H4_3_upper |
| $P_\infty$ | WX.P.complete_zero_mean_displacement_Linfty_upper |
| $K_{H,0}$ | WX.H.complete_density_L2_upper |
| $K_{H^{-1},0}$ | WX.H.complete_inverse_density_L2_upper |
| $K_{H,-4/3}$ | WX.H.complete_density_Hminus4_3_upper |
| $R_{w,2}$ | WT.J.forward_complete_strong_remainder |
| $\tau_{w,2}$ | WT.J.tau.tau2_L2 |

These are seventeen complete old bound records. Also preserve the complete signed record
SI.complete_SN_terminal_conclusion_read_verbatim.complete_scalar_mu_copied,
and WX.H.phase_derivative_lower and WX.H.phase_derivative_upper. They qualify the exact sign/mean and the bound 31/32--33/32; no other background is selected.

The only bound input used as a denominator is $m_\psi$, which must be read by its strictly positive lower endpoint. All other uses of old upper bounds in the displayed expressions use upward endpoints; counting the table itself, this means sixteen upper inputs and one lower input. The signed $\mu$ record is retained whole, while $\nu^\#$ uses the separate already saved absolute upper.

A future consumer verifies the full same-selected scope, true density convention, the original exact input 97, root 1024, moving 268435456, the true WT waist trace, and all four complete receipts before any new scalar product. It stores every original record verbatim and each complete new elementary factor and final candidate. It uses no old enclosure, no SN coordinate conversion, no old exponential or logarithm, no profile calculation, no source integral, and no finite-matrix inversion. No such consumer or numerical evaluation is executed in this note.

## WCE8. Immutable analytic evidence and retained scope

| Exact analytic source and use | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| IC.9--17,20,25,29: root two primitives, finite map, full density ranks and terminal coefficient | eeedd786977f2e324852e430bc1a3a82c175e78f | 18327 | a5717f1d2be8ba7e11b43b53a052f419c8bb25ef198a9c2bf1acda16ea5f7cea |
| TN.12--20: ordered compressed normalizer and full forward remainder | 401edaeaf8d64f32e51af6faef7c34cb0172f35a | 18847 | 0ffa3261e3bb3fdea2cd05afd489b2e71b5587a2bba9432410c492e2ee64f2aa |
| WT.26--31: the same formulas at the actual one-sided waist trace | 8c5ee6ec69250c5e51d4bc0179f245c6a24ae263 | 22752 | e4e317e896fade7dee1c93303ff8c9ed4c811d35b90cc6bc3ed3cecabdf30da5 |
| Frozen WT source, cutoff_row: exact meaning of the two saved waist fields | 7f0a7713998a96d10e8b28fbbc3a33f8783359d6 | 26205 | 7cde6f7f6d03bbfa107a93abdd4ee925b332f47ac7c4a2257d6557e00927a393 |
| SW.27--31: single complete root coefficient, original projection and unchanged old leading factors | d01094f9dd6b858dd80fe12da5d0790f0c210d1a | 24343 | 72bb6b3c9a7ae6ac660ded4d08ac67a986a43d58fcd3d1d7a95e3deb14d0ae6d |
| WRA.6--10: the actual decoded coefficient-only row | ffe98b2256041bdc4a49d85146ddc48afb301e2c | 26647 | 40fb2167aa27c9f9e07bfcaea89c6f5d20059cc724eb7ba4930e02b16dd27889 |
| WPL.32--43: exact waist first-normalizer zero, full second normalizer and physical mean rank | 582679b6e48a271153b90ecf1691deca2dc27c9c | 31021 | 052bd8ed9550ffebd9cb56744f7d4e56a9b6de5405c363d438813f9a100c8e24 |
| WUE.23--29,34: same reflected trial, same physical error and complete state decomposition | 9b5b13f0178c9a292ae8ba11264051c1fe438c14 | 32557 | e191f96acc39ab802adb93ace2d1e57691b017629ed762ddd39624d3bcb61ce1 |
| NIF.2--10a: full density convention and actual reflected input space | d606faa1ffd30c34d3487985a57dbc62a18890bc | 32942 | 8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640 |

The full scalar density mean is not either of the two original physical mean ports. If another realization uses $U_\psi P+\Pi$ instead, its difference $(\psi'-1)\Pi$ must be restored explicitly. Neither (WCE.4) nor the zero value of $\mathbf S(0)$ changes those physical equations.

The complete root finite operator through 1215, the moving finite complement through the original $J_s$, their transported dual rows, the real reflected source constraint, and the original low physical columns remain. A scalar norm for a finite-rank contribution is not a finite Schur inverse. No full-circle principal inverse is restricted to a same-space reflected endomorphism.

The conclusion is exactly the pair of new complete symbolic bounds (WCE.31)--(WCE.32) for (WCE.6). It supplies no new selected parameter, no whole-family KAM chart, no complete physical incoming inverse, no closed mean/head/parameter border, and no nonlinear background.
