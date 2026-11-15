# Complete strict physical Darboux receiver at the original P.22 cut

**Status.** This is a finite positive scalar contract for the second half of IN.15–27. The first all-segment Darboux consumer has actually succeeded in public run **43746008734/1**, with child return code zero and all 23 gates passed. Its complete scalar receivers are read unchanged. The new work below is the physical reconstruction at the same strict cut, together with the two explicit free-column terms. A numerical value for the resulting physical comparison is conditional on this contract's new cut-row and product gates.

The conclusion is a map from the full two-column, two-sign input $H^{-4/3}$ to the old-circle density pair with its two mean coordinates. It does not include the two strict normalizer inverses, the final circle change, an incoming inverse, or a complete return operator.

## 1. The object and the immutable first receiver

Use the same real parameter family $|\delta|\le 10^{-8}$, fixed intrinsic parameter $\eta_0$, physical input frequencies $n=4|j|$, and $|j|\ge97$. Let
$$
 r_c=\frac{76285779072683}{320000000000000},\qquad
 r_*\in\left[\frac{1191984371497}{5000000000000},
             \frac{2383968743003}{10000000000000}\right],
 \qquad \rho=r_*-r_c .
 \tag{DR.1}
$$
Thus $\rho$ lies in the exact positive interval already stored by the first receiver, whose lower endpoint is $1/262144$. No cut from the separate six-cut N consumer is substituted for $r_c$.

The primary proof is [IN, genuine Darboux comparison and complete incoming factorization](R133-supplement-genuine-Darboux-comparison-and-complete-incoming-factorization.md), immutable blob **f13509b4d0afc691cfc95d86c0f8e5562f919129**, SHA256 **d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75**. The actual first-receiver execution is [the complete execution](../notes/all_segment_Darboux_scalar_receivers_ci/run-43746008734-1/execution.json), immutable blob **64dab676807dbd3ee0913bdde1bb7cd732d8410a**, 35,387 bytes, SHA256 **816483884254f3e7ec06914b66afffc8434db11315dfab1712e71fbb7aae5ae1**.

Read its following complete fields, including their original balls and payload hashes:

- the exact cut and root bracket, complete same-family/segment qualifications, new three-phase gap and original nonzero root shear;
- the six complete zero-order functional coefficients, in the order $(a,a_\phi,a_{\phi\phi},b,b_\phi,b_{\phi\phi})$;
- the three density-zero raw $H^{-1}$ scalar bounds for $w_0,p_0,g_0$;
- the three density-one $L^2$ scalar bounds for $w_1^V,p_1,g_1$;
- the two complete differential inhomogeneous source bounds in $H^{-5/3}$;
- the original complete $n^{-2}$ strong-input multiplier upper bound.

The density-zero scalar bounds already include the extra term in the second identity IN.24. It is not added again. The two differential source bounds are separate and are added once below. The stored $p$ columns have not yet been divided by $\eta$.

All these fields retain both reference columns, both physical input signs, every output Fourier mode and the output mean. A source field called a “column” is not a projection onto a physical nonmean subspace.

## 2. Exact reconstruction and its typed numerical receiver

Write $D_0=\partial_r-d\partial_\phi$. Use the original complete operators $J,L,B_{\rm op}$, with their original finite-rank and mean terms. For the same scalar profile construction put $p=\eta h$ and $g=D_0w-p_\phi$. Write $\mathcal U_\perp(f)=P_\perp\mathcal U(f)$ for the original scalar nonmean projection. For an inhomogeneous profile, let $e_{D,\perp}=P_\perp e_D$, where $e_D$ is the extra first-row source in IN.24. The complete first reconstructed row is
$$
 \mathcal U_\perp(h)+J\{\mathcal U_\perp(g)-L\mathcal U_\perp(h)
                       -B_{\rm op}\mathcal U_\perp(w)+e_{D,\perp}\},
 \qquad \mathcal U_\perp(h)=\eta^{-1}\mathcal U_\perp(p).
 \tag{DR.2}
$$
This is IN.24–25 and the original G.11 identity
$JD_0P_\perp\mathcal U(w)=P_\perp\mathcal U(h)+J[P_\perp\mathcal U(g)-LP_\perp\mathcal U(h)]$,
followed by $-JB_{\rm op}P_\perp\mathcal U(w)$, in that order. Every displayed projection is contractive in its stated Sobolev window. The bounds below therefore use the already complete scalar bounds without changing any numerical fee. The complete rank/mean parts of $J,L,B_{\rm op}$ remain present; this scalar projection does not discard either final physical mean coordinate or change the complete primitive–mean map (DR.5). All signs matter for the identity; the positive bound below uses the sum of the four complete bounds.

For one of the two density orders, let $\Gamma_w,\Gamma_p,\Gamma_g$ be its complete scalar $H^{-1}$ bounds. For density one its saved $L^2$ bounds also give these $H^{-1}$ bounds by the contractive inclusion. Let $E_D$ be its saved complete inhomogeneous bound in $H^{-5/3}$. On one original whole row containing $r_c$, read
$$
 \eta_->0,\quad
 C_J=\|J:H^{-5/3}\to H^{-2/3}\|,\quad
 C_L=\|L:H^{-5/3}\to H^{-5/3}\|,\quad
 C_B=\|B_{\rm op}:H^{-5/3}\to H^{-5/3}\|.
 \tag{DR.3}
$$
The exact old field for $C_J$ is **C_J_scalar**, not **C_J_new**. In the original norm producer it is copied from the original strip-$1/64$ field **J_Hminus5over3_to_Hminus2over3**. The old complete $C_L,C_B$ include the rank/mean contributions.

Since $H^{-1}\hookrightarrow H^{-5/3}$ and $H^{-2/3}\hookrightarrow H^{-1}$ contractively, a complete raw-pair bound is
$$
 \begin{split}
 A_1&=\frac{\Gamma_p}{\eta_-}
       +C_J\left(\Gamma_g+C_L\frac{\Gamma_p}{\eta_-}
                              +C_B\Gamma_w+E_D\right),\\
 A_{\rm raw}&=(A_1^2+\Gamma_w^2)^{1/2}.
 \end{split}\tag{DR.4}
$$
There is no extra physical frequency factor in this formula. The first receiver already paid the respective $1/n$ and $1/n^2$ of the two inhomogeneous differential sources.

The full primitive–mean map satisfies
$$
 (I,\Pi):H^{-1}\longrightarrow L^2\oplus\mathbb C,\qquad
 C_I=\frac{\sqrt{17}}4 .
 \tag{DR.5}
$$
This is the complete multiplier norm on the physical fourfold circle: the nonzero multipliers are $\sqrt{1+(4j)^2}/(4|j|)$, and the mean multiplier is one. Both physical rows use (DR.5).

At the same original cut set
$$
 q=\sqrt{-K},\qquad n_g=\frac{a_{\rm phys}^2}{m^2},\qquad
 T(q)=\frac1{\sqrt{2q}}\begin{pmatrix}1&q\\1&-q\end{pmatrix}.
 \tag{DR.6}
$$
Here $m$ is the complete actual moving mean and $a_{\rm phys}$ is the physical intrinsic radius, not the fold coefficient $a_0$ or a radius from the positive collar. If $q_-\le q\le q_+$ and $|m|\ge m_->0$, then
$$
 W_c=\frac{a_+^2}{m_-^2}
             \max\{\sqrt{q_+},q_-^{-1/2}\},\qquad
 \mathcal R(\Gamma_w,\Gamma_p,\Gamma_g,E_D)
       = C_I W_c A_{\rm raw}
 \tag{DR.7}
$$
bounds the ordered old-circle density readout of (DR.2). The radial multipliers commute with the angular primitive–mean map. The norm of $T(q)$ is exactly the maximum appearing in (DR.7); no extra unproved frame alignment is used.

If $r_c$ belongs to more than one original closed row, retain all the corresponding one-sided row identities and apply (DR.7) to each complete row. The final bound is the maximum of those complete row bounds, not an entrywise selection of different cases. The two sides use the same globally defined trial. No seam impulse is invented at a merely artificial norm-partition boundary.

## 3. Read the actual cut coefficients without recomputing them

Restore only the exact old successful inputs needed for this readout:

1. The original complete old-circle norm native from run **43629465215/1**, SHA256 **7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c**, containing all 1,328 saved coefficient rows.
2. The original complete first-forcing native from run **43624260519/1**, SHA256 **54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47**.
3. The original intrinsic whole-row part **native/rows-03066-03322.json.gz**, SHA256 **ada966331fcabf90da9f17597cdd0c4e0a56cfaf6233787e69c2587b104a8a21**, with common-row indices $[3066,3322)$.

The third part is located by its actual interval
$$
 \left[
 \frac{4290616894992767}{18014398509481984},
 \frac{4405787072963543}{18014398509481984}
 \right].
 \tag{DR.8}
$$
Its archive is the original **visible-exact-body-rows-3066-4000-43583838026-1**, 4,343,481 bytes, SHA256 **24e1b751f511106e19786e61f3d77abac8f932a25b1424511e5b4abcd3f97e07**, original artifact id **14109917818**. Both the complete archive and the complete extracted member are checked on the runner. This part number is an original common-row index; it is not a candidate-piece index.

Match every saved norm row to its original forcing row and every selected forcing row to its original whole intrinsic row using the exact intervals, common-row identifiers and **actual_scalar_germ**. Select every closed row containing the exact rational $r_c$. Read the original fields
$$
 \begin{array}{c|c}
 \text{quantity}&\text{original field}\\ \hline
 \eta_-,C_J,C_L,C_B,d^{(0..3)}
   &\text{norm row bounds: eta_lower, C_J_scalar, C_L, C_B, D}\\
 K&\text{forcing: complete_intrinsic_ordinary_jets.K[0]}\\
 m&\text{forcing: full_actual_mean_derivatives[0]}\\
 a_{\rm phys}&\text{intrinsic: intrinsic_whole_third_jets.a}.
 \end{array}
 \tag{DR.9}
$$
The signed interval for $K$ must be strictly negative and the full signed mean interval must retain its original nonzero sign. New square roots and the radial scalar (DR.7) are permitted new arithmetic. The original coefficient producer, mean solve, intrinsic jets, original profiles and old row integrations are not called.

## 4. The two explicit free-column amplitudes

Use the same regular Fuchsian function $\mathcal B$ and the same actual canonical coordinate $T$. IN.8 gives
$$
 \begin{split}
 R_2&=\mathcal B K w_1^V+\mathcal B' E_{22}w_0,
       &R_{2,a}&=\mathcal B T b_1^V,
       &R_{2,b}&=\mathcal B a_1^V+\mathcal B'b_0,\\
 R_3&=\mathcal B' E_{22}w_1^V,
       &R_{3,a}&=0,
       &R_{3,b}&=\mathcal B'b_1^V ,
 \end{split}\tag{DR.10}
$$
where $K=\left(\begin{smallmatrix}0&T\\1&0\end{smallmatrix}\right)$.
The negative signs with which these occur in the exact trial difference are kept in that identity. Triangle inequality will bound their two complete reconstructed maps.

For their product domain read the already successful B consumer, run **43711480764/1**:
$$
 R_S=1/8000,\qquad S_S=3/512,
 \qquad |\rho|<R_S,\quad |\operatorname{Im}\phi|<S_S.
 \tag{DR.11}
$$
Its **complete_new_amplitude_modulus** gives the complete moduli $A_1,B_1$ of the same $a_1^V,b_1^V$, and **complete_old_product_T_image_upper** gives $T_S$. Read the original whole-product leading $b_0$ and $Q$ moduli from the immutable 4,501-byte original fold-majorant stage. These are whole $R_G\times S_G$ quantities, with $R_G=3/8000$ and $S_G=3/128$; their restriction to (DR.11) requires no new old closure. Read $\mathcal B_0,\mathcal B_1$ from the successful whole-piece W receipt.

The product qualifies only after checking the exact B domain identities and the strict inclusion $T_S$ in the same paid potential/Fuchsian image disk, with the original parameter squares and actual $T$. In particular no real-angle derivative is used as a positive-strip modulus.

New complete product moduli are
$$
 \begin{array}{ll}
 M_{2,a}=\mathcal B_0T_SB_1,&
 M_{2,b}=\mathcal B_0A_1+\mathcal B_1\,b_{0,+},\\
 M_{3,a}=0,&M_{3,b}=\mathcal B_1B_1.
 \end{array}\tag{DR.12}
$$
Here $A_1,B_1$ denote amplitude moduli only; they are unrelated to the raw-row constant $A_1$ in (DR.4). Every product in (DR.12) is new. No successful amplitude jet or Taylor tail is recomputed.

Let $\rho_+$ be the exact upper endpoint in (DR.1), and put $d_R=R_S-\rho_+>0$. At the real strict cut, the complete Cauchy bounds for these new products are
$$
 \begin{split}
 |\partial_\phi^k R_{m,c}|&\le k!M_{m,c}S_S^{-k},
                       &&0\le k\le4,\\
 |\partial_r\partial_\phi^kR_{m,c}|
        &\le k!M_{m,c}d_R^{-1}S_S^{-k},
                       &&0\le k\le3 .
 \end{split}\tag{DR.13}
$$
The physical derivative is $-\partial_\rho$ at fixed parameter, which has the same absolute bound. The original moving root depends on the parameter, not on $\phi$. Therefore no angular root derivative is suppressed in (DR.13).

## 5. Free $p,g$ and the free inverse, with the required fourth derivatives

For the free Airy profiles the exact scalar transport columns are
$$
 p_m^0=-i\epsilon Q K R_m,\qquad
 g_m^0=\partial_rR_m-d\partial_\phi R_m-\partial_\phi p_m^0 .
 \tag{DR.14}
$$
The old $d$ and its three angular derivative bounds are read from the selected original row in (DR.9). They are not replaced by a radial or mean drift.

The full product moduli of the two components of $p_m^0$ are
$$
 (P_{m,a},P_{m,b})=(Q_+T_SM_{m,b},\,Q_+M_{m,a}).
 \tag{DR.15}
$$
Apply the same angular Cauchy formula $k!P_{m,c}S_S^{-k}$ for $0\le k\le4$. This avoids asking for a missing fourth derivative of an old saved $Q$ jet. If $r_{c,k}$, $r_{r,c,k}$ and $p_{c,k}$ denote these new nonnegative bounds, then for $0\le k\le3$
$$
 g_{c,k}=r_{r,c,k}
    +\sum_{\ell=0}^k {k\choose\ell}D_\ell r_{c,k-\ell+1}
    +p_{c,k+1}.
 \tag{DR.16}
$$
Thus every requested third derivative of $g_m^0$ includes the fourth angular derivative in (DR.14). There is no truncation to the saved density-one $p$ array of length three.

The free matrix and its inverse are
$$
 H^0=\begin{pmatrix}i\epsilon x&Ty\\y&i\epsilon x\end{pmatrix},
 \qquad
 \mathfrak B_0=(H^0)^{-1}
 =\frac1{B_+}\begin{pmatrix}-i\epsilon x&Ty\\y&-i\epsilon x\end{pmatrix},
 \qquad B_+=x^2+Ty^2 .
 \tag{DR.17}
$$
Read the accepted SV full-strip zero-order bounds $x_+,y_+$ and the accepted RV whole-$h$ image bound $T_h$. For the free denominator read the original H execution, run **43688459733/1**, immutable blob **5e7669f1990e1c4e9e3769afe3641ef6d84b82a3**, 16,120 bytes, SHA256 **fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57**. Its complete **old_circle_inverse.complete_free_Bplus_modulus_lower** already supplies
$
 |B_+|\ge g_{\rm free}>0
 \quad (|\rho|<1/20000,\ |\operatorname{Im}\phi|<1/64).
 \tag{DR.18}
$
The consumer reads that saved lower ball and checks the strict restriction $h<1/20000$; it does not regenerate the original free or deformed determinant formula. In particular no implication comparing $|B_+|$ with $|B_+-n^{-2}Vy^2|$ is used. The original H producer, SHA256 **9596ebee08e95939cf1b8a9d46a9f32053bd4706cc77e2263a80d09ede99294c**, explicitly separates the two gaps at its inverse-budget lines 153–155 and stores the free one. The complete original parameter and old-angle domain remains fixed.

Consequently, throughout the same strip $S_B=1/64$,
$
 |\mathfrak B_0|\le
 g_{\rm free}^{-1}\begin{pmatrix}x_+&T_hy_+\\y_+&x_+\end{pmatrix}
       =:\mathcal B^0 .
 \tag{DR.19}
$
This is a new free-matrix modulus readout. Its angular derivatives at the real cut cost $k!\mathcal B^0/S_B^k$, $0\le k\le3$. Matrix products with $R_m,p_m^0,g_m^0$ use the full entrywise ordered product and the complete binomial rule. Both physical components and their means remain.

The SV $x_+,y_+$ entries of order zero are full $S_G$ moduli; their positive-order real jets are not used to claim (DR.19). The image, denominator and strip are checked separately from the larger amplitude product (DR.11).

## 6. Complete free scalar receivers in the same input space

Let $\mathcal Z_0$ denote the first successful consumer's six-coefficient zero-order functional. Its $\rho^{-1/4}$ weight at (DR.1), full central/high partition, both reference columns and both signs are already included. IN.17 proves the same positive envelope for the free profiles, including their positive tail.

For a pair of complete angular arrays $v$ through order three write
$$
 \mathcal Z_0^+(v)=\mathcal Z_0(v)+\mathcal Z_0(\partial_\phi v).
 \tag{DR.20}
$$
For $m=2,3$ put
$$
 s_m=\sup_{n=4|j|\ge388}\frac{(1+n^2)^{2/3}}{n^m}
       \le 2\,388^{4/3-m}.
 \tag{DR.21}
$$
Read the already saved upper for $s_2=2\,388^{-2/3}$. Its quotient by 388 is a valid new upper for $s_3$. The factor two is used once in each input multiplier, before the variable-coefficient convolution.

The exact free primitive identity is the homogeneous version of IN.24, so the complete raw $H^{-1}$ bounds are
$$
 \begin{split}
 \Gamma_{w,m}^0&=s_m\mathcal Z_0^+(\mathfrak B_0R_m),\\
 \Gamma_{p,m}^0&=s_m\mathcal Z_0^+(\mathfrak B_0p_m^0),\\
 \Gamma_{g,m}^0&=s_m\mathcal Z_0^+(\mathfrak B_0g_m^0).
 \end{split}\tag{DR.22}
$$
Here the input density is the original $n^{7/6}$, and the displayed term already contains its explicit $n^{-m}$. The primitive identity removes the one additional $n$ relative to the zero-order profile. Thus (DR.21) is precisely the remaining $H^{-4/3}$ input fee; no second $n^{-m}$ is applied after (DR.22). There is no inhomogeneous source for the free profile, so its $E_D$ is exactly zero.

Use (DR.7) separately for the complete triples in (DR.22), dividing $p_m^0$ by the original $\eta_-$ only at (DR.4). All these statements include the physical output mean. An amplitude with mean zero is not used to delete a transported physical mean.

## 7. The four complete pieces and the exact scope

The exact Darboux trial difference is the sum of the two inhomogeneous error-profile density orders and the two signed free-amplitude terms of (DR.10). Hence at this strict cut
$$
 C_{\rm Dar}^{\rm old}
  =C_{\mathcal E,0}+C_{\mathcal E,1}
                         +C_{R_2}^0+C_{R_3}^0
 \tag{DR.23}
$$
is a complete bound
$$
 H^{-4/3}_{\text{two columns, both signs},\,|j|\ge97}
 \longrightarrow
 (L^2(\mathbb C^2)\oplus\mathbb C^2)_{\text{old-circle density}}.
 \tag{DR.24}
$$
Each summand is the maximum of its complete row instances at the same $r_c$. Alternatively one may maximize their complete rowwise sum; the consumer must identify which complete positive rule it uses. It does not minimize entries across different one-sided rows.

The root shear $\beta_n$, full root matrix, all-$\tau$ integral and three-phase gap remain in the immutable first-receiver fields. The free terms retain all means, $Q$, the actual $T$, $d$, the old angular inverse, and the physical $\eta^{-1}$.

The first and second strict normalizers, the subsequent genuine circle map and every finite cross block must still be composed in their original order. This contract neither grants their cutoff-97 inverses nor chooses a sufficiently large cutoff for IN.32. It also does not identify the unchanged nonzero stable trial trace with the zero stable boundary condition of the PC correction. The exact common stable-factor cancellation and full finite equations remain IN.28–38.

In particular (DR.23) is a strict-cut comparison constant, not the complete corrected-trial $C_E$ at the waist and not the full return remainder $R_0$. To pass to those objects one must include the already separated PC correction, true transport/source readouts and the ordered normalizer/circle costs in their exact windows.

## 8. Required new execution and persistent evidence

The new public consumer must:

- verify the immutable successful first execution, all 23 original gates, exact cut/family, complete six-coefficient functional and eight scalar source records;
- verify the old forcing/norm successes and archive/member hashes, then locate every actual closed cut row by exact rational comparisons and match its complete original germ;
- retain the original signed $K,m,a_{\rm phys}$ and positive $\eta$ gates, compute only the new physical cut scalars and the new products (DR.12)–(DR.22);
- read the original B/W/SV/RV/H/fold moduli and qualification payloads without importing or calling their successful producers;
- save all four complete physical contributions, their sum, the exact cut-row identities, product gaps, both mean channels, and the still-unpaid normalizer/incoming/return scope;
- atomically save the complete small science receipt before rendering and emit recoverable small science before any Git publication;
- leave original arrays and archives temporary, and publish only small conclusions and identities.

Failure of any actual gate is retained as a failure. The original successful first receiver, old amplitudes, profiles, scalar intrinsic solves, positive calibration, integrals, source columns, PC and PW are not rerun.
