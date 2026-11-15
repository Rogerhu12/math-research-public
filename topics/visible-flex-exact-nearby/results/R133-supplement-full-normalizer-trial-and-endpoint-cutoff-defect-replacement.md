# R133 supplement UT: the full strict normalizer trial and endpoint replacement of the cutoff defect

2026-11-15. Exact analytic identities and a new scalar-consumption contract. No new numerical evaluation is reported.

The finite normalizer in [SF](R133-supplement-complete-strict-first-symbol-propagation-defect.md) generates a large sufficient bound for its cutoff defect. This note constructs a different trial using the full ordered normalizer. Returning to the original trial requires both endpoint corrections, all interfaces and both physical means. Only after that return may the two complete bounds be compared.

The successful SJ calculation, its complete four-part source ledger and its original result remain unchanged. No upper bound is subtracted from another upper bound. No old ray, row enclosure, coefficient closure, radial integral, normalizer or scientific producer is evaluated again.

## 1. Fixed object and complete state

Use the exact repaired real family $Q_\delta=Q_0+\delta Z_{\rm can}$, $|\delta|\le10^{-8}$, fixed intrinsic $\eta_0$, and the original strict interval
$$
 0\le r\le r_c,\qquad r_c=\frac{76285779072683}{320000000000000}.
 \tag{UT.1}
$$
The angle is the moving circle of period $\pi/2$, with frequencies $4j$. The input is the original complete $\mathcal X^{-4/3}_{97}$, both Fourier signs and both characteristic waves of the same terminal-Ai reference. Independent second-reference, exterior, root-head and physical matching-mean inputs remain separate.

Let $\Pi$ be the mean, $P=1-\Pi$, $I=\partial_\phi^{-1}P$, and $\mathcal Y=L^2_{\ne0}(\mathbb T;\mathbb C^2)\oplus\mathbb C^2$. Keep the full unscaled system
$$
 (\partial_r-\mathcal G)\binom yz=\binom{F_y}{F_z},\qquad
 \mathcal G=\begin{pmatrix}G_y&G_z\\Z_y&Z_z\end{pmatrix}.
 \tag{UT.2}
$$
Its physical density is $\mathfrak D_rh=n_g(r)(y,z)$, where $n_g=a_{\rm phys}^2/m^2$. All four blocks and both independent mean coordinates remain. The exact SF.8 identities are
$$
 [P,G_y]=0,\qquad Z_y\Pi=0.
 \tag{UT.3}
$$
They do not remove the genuine nonconstant mean source $Z_y y$.

## 2. Full and compressed normalizers, in their actual order

Denote the second matrix coefficient called $Z$ in SF by $Z_2$, to distinguish it from the Maslov sign operator. Use
$$
 \begin{gathered}
 T_1=1+SI,\quad T_2=1+Z_2I^2,\quad T=T_1T_2,\\
 A_J=P_JSIP_J,\quad B_J=P_JZ_2I^2P_J,\quad
 T_J=(1+A_J)(1+B_J),\quad F_T=T-T_J,\\
 J=J_s=268435456 .
 \end{gathered}\tag{UT.4}
$$
The moving projection $P_J$ selects $|j|\ge J$. It is distinct from $P$ and the root input projection at 97. The genuine coefficient supports are $\deg S\le192$, $\deg Z_2\le384$. The successful WT inverse is $T_J(0)^{-1}$ at this same $J$. No inverse of full $T$, or whole-interval inverse of $T_J$, is assumed.

Retain the actual SF diagonal generator, transport and primitive ranks:
$$
 V=V_0(1+M_{\mathfrak c}I),\qquad V(r_c)=1,\qquad
 \mathcal D_V=(\partial_r-L_d)V,\qquad
 \mathfrak c(r)=\int_{r_c}^r\mathfrak b(s)\,ds .
 \tag{UT.5}
$$
The signed radial direction, complete mean of $\mathfrak c$, both ordered primitives and both conjugation ranks remain. The cut map is exactly
$$
 \mathcal B_c=n_g(r_c)^{-1}B_{\rm free}^{[1]},\qquad
 K_c^-=\|\mathcal B_c:\mathcal X^{-4/3}_{97}\to H^{-4/3}\|.
 \tag{UT.6}
$$
This is the corrected FA first-order map, with the original root/cut/leading and two-sign normalization. No root input factor or common gauge is moved.

Initially on finite Fourier input sums, define
$$
 \mathbb Y_J=\binom{PT_JV\mathcal B_c}{0},\qquad
 \mathbb Y_T=\binom{PTV\mathcal B_c}{0},\qquad
 \mathbb E_T=\binom{PF_TV\mathcal B_c}{0}.
 \tag{UT.7}
$$
Thus $\mathbb Y_T=\mathbb Y_J+\mathbb E_T$. The zero in these trial states is not the mean of the exact solution.

## 3. Exact source difference and its endpoint identity

The complete defects satisfy
$$
 \mathcal Q=G_yT-T_r-TL_d,\quad
 \mathcal F_J=G_yF_T-(F_T)_r-F_TL_d,\quad
 \mathcal Q_J=\mathcal Q-\mathcal F_J .
 \tag{UT.8}
$$
Here $\mathcal Q$ is SF.18 in full, including $\mathcal F_0,\mathcal F_1,\mathcal F_2$, all two-primitive products and every mean. By (UT.3),
$$
 \mathbb F_T^{\rm app}
  =(\partial_r-\mathcal G)\mathbb Y_T
  =\binom{P(T\mathcal D_V-\mathcal QV)\mathcal B_c}
                  {-Z_yTV\mathcal B_c}.
 \tag{UT.9}
$$
The old SF source has $T_J,\mathcal Q_J$ in the same positions. Therefore
$$
 \begin{split}
 \mathbb F_T^{\rm app}-\mathbb F_J^{\rm app}
 &=\binom{P(F_T\mathcal D_V-\mathcal F_JV)\mathcal B_c}
                  {-Z_yF_TV\mathcal B_c}\\
 &=(\partial_r-\mathcal G)\mathbb E_T .
 \end{split}\tag{UT.10}
$$
The first row expands to $(F_T)_rV+F_TV_r-G_yF_TV$; the two $F_TL_dV$ terms cancel. The second row is essential. Removing $\mathcal F_J$ from the original source without changing the trial would not prove (UT.9).

Let $\mathcal U(r,s)$ be the same full unscaled propagation. Brackets at joins mean right trace minus left trace in increasing $r$. The exact backwards identity is
$$
 \begin{split}
 \mathbb E_T(0)={}&\mathcal U(0,r_c)\mathbb E_T(r_c)
 -\int_0^{r_c}\mathcal U(0,r)
       (\mathbb F_T^{\rm app}-\mathbb F_J^{\rm app})(r)\,dr\\
 &-\sum_\ell\mathcal U(0,r_\ell)
        \bigl([\mathbb Y_T]_\ell-[\mathbb Y_J]_\ell\bigr).
 \end{split}\tag{UT.11}
$$
All jumps of $\mathbb E_T$ are present. This is an endpoint identity, not a claim that a propagated radial integral of finite angular maps is finite rank. The distinction proved in BT remains.

## 4. Three independent saved source parts and the complete interface sum

Use the complete SF budgets $t_0,t_-,q_*,z_*,d_V,v_-,c_-$, with minus denoting $H^{-4/3}$. The factors $t_0,t_-$ bound full $T$, as well as its compressed realization. A complete ordinary source majorant for (UT.9) is
$$
 f_T^{\rm app}
   =K_c^-(t_0d_V+q_*v_-c_-+z_*t_-v_-c_-).
 \tag{UT.12}
$$
The nonmean pair and the two means are its output. In particular $Z_y$ is charged and all three finite maps remain inside $q_*$.

The frozen SJ function `complete_source_row` records the following independent positive parts:

| Saved field | Exact positive budget integrated with true $dr$ |
|---|---|
| `leading_two_primitive_and_rank` | $K_c^-t_0d_V$ |
| `complete_Q_including_F0_F1_F2` | $K_c^-q_*v_-c_-$ |
| `complete_finite_FT_FJ` | $K_c^-f_Jv_-c_-$ |
| `complete_independent_mean_row` | $K_c^-z_*t_-v_-c_-$ |

Its `complete_finite_and_two_primitive_fees` uses the full factors $t_{1,0}=1+|S|_0/4$, $t_{2,-}=1+m_{4/3}(Z_2)/16$ and their products. The ordinary loop accumulated each part independently over all 3071 true row intersections. Thus the three appropriate saved **whole integral** records give
$$
 F_T^\#=F_{\rm leading}^\#+F_{\mathcal Q}^\#+F_{\rm mean}^\#
   \ \ge\ \int_0^{r_c}f_T^{\rm app}(r)\,dr .
 \tag{UT.13}
$$
The fourth record stays in the audit and old result. No expression of the form total minus an upper bound is used. No row budget or radial integral is recalculated.

At every original qualified join, exact repaired definitions give the same $S$ on both sides and continuous $V$. Consequently
$$
 \begin{split}
 [\mathbb Y_T]_\ell
 &=\binom{P(1+SI)[Z_2]_\ell I^2V\mathcal B_c}{0},\\
 [\mathbb Y_J]_\ell
 &=\binom{P(1+A_J)P_J[Z_2]_\ell I^2P_JV\mathcal B_c}{0}.
 \end{split}\tag{UT.14}
$$
Each separately has the same complete SF.43 upper
$$
 j_\ell^\#=K_c^-t_{1,0}C_I^2|[Z_2]_\ell|_0v_-c_-,
 \qquad C_I=\frac{\sqrt{17}}4 .
 \tag{UT.15}
$$
The old projections were only contractions in that inequality. The actual `complete_interface` uses precisely this full $t_{1,0}$, complete two-branch jump and negative-window transport.

The literal `complete_all_interface_impulses_upper` therefore supplies $J_T^\#$ for the new full trial too. All 2549 genuine polynomial joins, all 521 conservatively charged artificial refinements, and their separately saved subtotals remain. There is no radial length factor for any jump. The original $q_{rr},\beta_r,\gamma_r$, physical radial-state and mean jumps remain inside these complete records. Endpoint-ball overlap is not continuity.

If the reference were changed so that $[S]\ne0$, an additional complete one-primitive jump would be required and this reuse would not apply. This note keeps the exact family whose continuity qualifications succeeded in SJ.

## 5. Endpoint strong bound for the complete finite map

Set
$$
 A_f=SI-P_JSIP_J,\qquad B_f=Z_2I^2-P_JZ_2I^2P_J,\qquad
 F_T=A_fT_2+(1+A_J)B_f .
 \tag{UT.16}
$$
Both supports of $A_f$ lie in $|j|\le J+191$, because
$A_f=(1-P_J)SI+P_JSI(1-P_J)$ and $\deg S\le192$.
Writing $\Lambda_L=(1+16L^2)^{1/2}$, one obtains
$$
 \begin{split}
 \|A_f\|_{H^{-4/3}\to L^2}
       &\le2C_I m_{1/3}(S)\Lambda_{J+191}^{1/3},\\
 \|B_f\|_{H^{-4/3}\to L^2}
       &\le2C_I^2|Z_2|_0 .
 \end{split}\tag{UT.17}
$$
The first line uses $I:H^{-4/3}\to H^{-1/3}$, the full multiplier on $H^{-1/3}$, and the finite output embedding into $L^2$. The second uses $I^2:H^{-4/3}\to H^{2/3}\hookrightarrow L^2$ followed by $Z_2$ on $L^2$. Each of the two exact summands is bounded before addition. Hence the actual order in (UT.16) gives
$$
 \mathcal E_T(r)
 =2C_I m_{1/3}(S)\Lambda_{J+191}^{1/3}t_{2,-}
       +2C_I^2t_{1,0}|Z_2|_0
 \ \ge\ \|F_T(r)\|_{H^{-4/3}\to L^2}.
 \tag{UT.18}
$$
There is no derivative of $F_T$ and no full-$T$ inverse. The former $J^{7/3}$ body-source factor has been replaced by this endpoint estimate.

For a common endpoint bound, read the successful closed-interval SJ maxima $S^\#,Z^\#,t_{1,0}^\#,t_{2,-}^\#$. The first two are complete angular Wiener $A^0$ entry sums, as qualified by SJ.40, rather than bare pointwise Euclidean norms. Thus
$$
 m_{1/3}(S)\le(1+4\cdot192)^{1/3}S^\#,\qquad |Z_2|_0\le Z^\# .
 \tag{UT.19}
$$
Substitution into (UT.18) defines one positive $\mathcal E_T^\#$ valid at both closed endpoints. It is a new outward scalar combination of existing maxima. No endpoint jet or old coefficient closure is generated.

## 6. Both physical endpoint corrections

Let $\mathsf H^{0,c}$ be the same exact homogeneous free continuation as in SF. The old and new physical-density cut errors satisfy
$$
 \begin{gathered}
 E_{c,J}^{\rm dens}
 =\mathfrak D_{r_c}{\sf H}^{0,c}-n_g(r_c)\mathbb Y_J(r_c),\\
 E_{c,T}^{\rm dens}=E_{c,J}^{\rm dens}-n_g(r_c)\mathbb E_T(r_c).
 \end{gathered}\tag{UT.20}
$$
The already paid FA/SJ upper $E_{c,J}^\#$ includes the original forward TN factor and both mean rows. Since $V(r_c)=1$ and $n_g(r_c)\mathcal B_c=B_{\rm free}^{[1]}$,
$$
 \begin{gathered}
 n_g(r_c)\mathbb E_T(r_c)=\binom{PF_T(r_c)B_{\rm free}^{[1]}}0,\\
 \|E_{c,T}^{\rm dens}\|\le E_{c,J}^\#+\mathcal E_T^\#K_{\rm free,c}^- .
 \end{gathered}\tag{UT.21}
$$
Here $K_{\rm free,c}^-$ is the existing FA bound for the corrected $B_{\rm free}^{[1]}$ in the negative window. It is different from the normalized $K_c^-$. The radial cancellation is exact: no cut $n_g^{-1}$ is paid twice, and no upper norm is inverted. The original root/cut normalization stays fixed.

At the waist,
$$
 \mathfrak D_0{\sf H}^{0,c}-n_g(0)\mathbb Y_J(0)
 =\bigl(\mathfrak D_0{\sf H}^{0,c}-n_g(0)\mathbb Y_T(0)\bigr)
                                      +n_g(0)\mathbb E_T(0).
 \tag{UT.22}
$$
Read $v_-^\#$ from the saved whole-interval reverse leading bound and $m_c^\#$ from the saved complete two-branch multiplier for $\mathfrak c$. Then
$$
 e_{0,T}^\#
 =n_{g,0}^+\mathcal E_T^\#v_-^\#
       \left(1+\frac{m_c^\#}{4}\right)K_c^-
 \ \ge\ \|n_g(0)\mathbb E_T(0)\|.
 \tag{UT.23}
$$
The upper $n_{g,0}^+$ is the actual waist value in WT's copied SP factors, not a cut value. Although $\mathbb E_T$ has zero trial mean by definition, the complete difference in (UT.22), the cut discrepancy and all propagated mean source rows still retain the two physical means.

The actual waist inverse remains $T_J(0)^{-1}$ at the same $J$:
$$
 T_J(0)^{-1}PT(0)V(0)\mathcal B_c
 =PV(0)\mathcal B_c+
      T_J(0)^{-1}PF_T(0)V(0)\mathcal B_c .
 \tag{UT.24}
$$
The commutation with $P$ follows from the double high compressions in (UT.4). The second term is the complete waist correction. It can be paid by (UT.23) and the actual WT $L^2$ inverse or retained in its exact finite factor at this endpoint. It cannot be deleted. This finite endpoint does not make the earlier radial integral finite rank.

If the correction is retained rather than paid, the trial and its finite ledger change. The original CG/WE assembly can be reused without a new operator audit only after (UT.22) is restored, or after that exact term has explicitly been included in the assembly. This contract takes the norm-paid return to the old trial.

## 7. New whole bound for the old trial

Use exactly the successful ST $G_{\rm cut}$ and $G_{\rm src}$ already copied into SJ. The first consumes physical density at the cut. SF.39--41 proves that the second consumes the present ordinary $L^1(dr;\mathcal Y)$ source and its unscaled state impulses. Its output factor already includes waist $n_g(0)$; that factor is not applied a second time.

The full-trial comparison has the complete sufficient bound
$$
 C_{{\rm SF},T}^\#
 =G_{\rm cut}\bigl(E_{c,J}^\#+\mathcal E_T^\#K_{\rm free,c}^-\bigr)
       +G_{\rm src}(F_T^\#+J_T^\#).
 \tag{UT.25}
$$
Returning to the original trial gives
$$
 C_{{\rm SF},J;{\rm UT}}^\#=C_{{\rm SF},T}^\#+e_{0,T}^\#.
 \tag{UT.26}
$$
Both actual radial endpoints are present. The root-to-cut data, corrected cut map, first-omitted terms and cut ranks remain in their FA/WY roles. Nothing new is asserted between the strict cut and the root.

Let $C_{{\rm SF},J;{\rm old}}^\#$ be the literal successful SJ whole bound. The two candidates now bound the same operator, so
$$
 C_{\rm SF,new}^\#
 =\min\left(C_{{\rm SF},J;{\rm old}}^\#,
            C_{{\rm SF},J;{\rm UT}}^\#\right).
 \tag{UT.27}
$$
The implementation compares upper endpoints of its final retained outward records, selects one whole candidate, and preserves both records and their provenance. It does not minimize separate entries. The old bound remains available if the new sufficient bound is larger.

The identities first hold on finite Fourier input sums. The strong endpoint maps in (UT.17) and the complete SF/SJ body and jump majorants extend the differences to all of $\mathcal X^{-4/3}_{97}$ by density. No individual order-zero trial is asserted to map that negative input space to $L^2$.

## 8. Optional downstream reuse in the ordered waist assembly

After the norm-paid return (UT.26), all other WE operators remain unchanged. New positive scalar combinations may form
$$
 \begin{gathered}
 C_{*,{\rm new}}=C_{\rm PC}+C_{{\rm ST},4}+C_{\rm SF,new}^\#,\\
 C_{{\rm paid,new}}
       =A_{\rm state}C_{*,{\rm new}}+C_{\rm CG,whole}.
 \end{gathered}\tag{UT.28}
$$
The four quantities $C_{\rm PC},C_{{\rm ST},4},A_{\rm state},C_{\rm CG,whole}$ and the old paid bound are read literally from successful WE. The same
$A_{\rm state}=B_{H^{-1},0}K_{WT,0}K_\Lambda K_{F,-}K_{S^{-1},-}$
has its original windows and order. The left coordinate cancellation applies only to the state term. The whole CG coefficient fee is added once, without the state factor or another right $K_F$.

The original input order $P_{97}\Lambda_\sigma^{-1}T_F^{-1}S^{-1}$ remains. Both physical input signs already belong to each complete wave operator. The exact global outgoing Maslov factor in MS/ZD remains separate from these individually normalized branches.

Every retained WE/BT row, independent physical matching mean, transported original low input, actual incoming and finite cross row, and conditional same-graph second-reference requirement remains. The new paid subtotal is not a complete $E_i/E_o$, incoming inverse, finite Schur inverse, returned-remainder, nonlinear-solution or final-surface certificate.

## 9. Current small inputs and the only new numerical target

All paths are relative to `topics/visible-flex-exact-nearby`.

| Input | Complete fields and use |
|---|---|
| SJ successful execution | All 26 gates; same family, interval and cutoffs; four independent source parts; full interface sum, subclasses and counts; $S,Z_2,t_{1,0},t_{2,-}$ maxima; reverse leading negative window; complete $\mathfrak c$ multiplier; normalized $K_c^-$; old cut error; both ST receivers; old whole SF bound |
| FA successful science | Same corrected reference/cut/input; `complete_corrected_Bfree1_Hminus4_3_upper`; normalized $K_c^-$ and forward-restored cut error cross-checked against SJ |
| WT successful science | Same full family and actual waist; fixed $J=268435456$ inverse in both windows; `copied_complete_SP_waist_factors.density_radial_factor_upper` |
| Optional WE successful science | Original order and retained register; four literal components for (UT.28); its old SJ whole record checked for exact equality |
| SF/SJ contracts and frozen SJ source | Read or AST-check only: independent source sums, full jump factor, complete supports and means, endpoint scope |

The minimal new target forms (UT.18)--(UT.19), adds three saved positive whole integrals, and forms (UT.21)--(UT.28). It restores no binary or native array. It reruns no old integral, target coefficient, normalizer, ray or scientific producer.

The complete new receipt retains the old fourth part, every interface count and subclass, both endpoint fees, the full-trial and returned-old-trial bounds, both whole candidates and their selection, and all unchanged restrictions. Only public Actions evaluates the new scalar arithmetic. This note reports no candidate numerical value or actual gate result.

## 10. Immutable primary identities

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| SF exact defect contract | `0f93e925d354133675b84ffeaa959a0b58d339a0` | 35289 | `add091118ef1af71bc8c4be275742d4124a076d6cf2ebaf00d35c66f8348f2b4` |
| SJ coefficient/interface contract | `32f770ec471af361dc3668bbe2ef37a0fddcd738` | 36867 | `ccaaa1b17fd68ce64d79a7bdc40dae9c0843b610da11149c178e92079d495f31` |
| Frozen SJ scientific source | `3d90ee2ed239c9e02344940eca4d4ca74696141e` | 58343 | `dfcf40ab948ea71ea80d733cd851602dcf5c78fdd83993e25f06664fc62b39d0` |
| SJ execution, 43768006977/1 | `7dac244799016d9cae317a61f6c5dbe47ca0a013` | 46318 | `2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88` |
| FA science, 43763658978/1 | `2001f4e2eeece1cda56b18b90dccab04b7f6d336` | 35718 | `2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2` |
| WT science, 43763134339/1 | `b742d3167f68c05ef197450a3112eb5b8edcacac` | 27619 | `2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d` |

The frozen source is `scripts/fourfold_codazzi_strict_radial_first_symbol_defect.py`. Its `complete_source_row`, `complete_finite_and_two_primitive_fees`, `complete_interface`, and independent ordinary accumulation loop are the exact source evidence. The execution is `notes/strict_radial_first_symbol_defect_ci/run-43768006977-1/execution.json`.

FA and WT are respectively `notes/free_Airy_first_omitted_cut_scalars_ci/run-43763658978-1/actual-scientific-conclusion.json` and `notes/waist_normalizer_coefficients_ci/run-43763134339-1/actual-scientific-conclusion.json`. A later manifest pins the optional WE receipt and this final published contract. No missing mathematical input is inferred from an unretained temporary array.
