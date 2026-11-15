# R133 supplement: separate cut and propagated first-coefficient budgets

2026-11-15, newton_source.

**Analytic closure and new readout contract; numerical prerequisites are stated separately.** This note supplies complete multiplier and dual-row formulas for the distinct coefficients $C_{\sigma,c}$, $g_\sigma$ and $C_\sigma=C_{\sigma,c}+g_\sigma$ in WY.20--29. It uses the actual saved FA amplitude derivatives, the correlated KL root-short numerator and the complete SJ ordinary transport integrals. It never infers either summand by subtracting an upper bound for their sum.

The existing FA, ST, WX and KL numerical conclusions are frozen. The SJ transport integral and TF root inverse must be successful in their own right before a consumer uses their corresponding new values. No pending numerical conclusion is asserted by this text.

## CG1. The exact object and its two signs

Work on the same real family $Q_\delta=\bar Q+\delta Z$, $|\delta|\le10^{-8}$, at the original fixed intrinsic $\eta_0$, the P22 cut $r_c$, the original root, and the physical circle of length $\pi/2$. The Fourier label $j$ has physical frequency $4j$ and the primitive is
$$
 I=\partial_\phi^{-1}(1-\Pi),\qquad
 \Lambda_j=(1+16j^2)^{1/2}.
 \tag{CG.1}
$$
All scalar Fourier means below are retained unless a displayed primitive explicitly annihilates them. The two independent physical mean ports and the original finite/sign complement remain separate.

Use the physical branch label of PF and WY. FA's printed phase label $\tau$ is first relabelled by $\tau=-\sigma$. Set
$$
 \Phi=\Phi_\sigma(r_c),\quad
 \kappa=\partial_\phi\Phi>0,\quad
 H=\Phi^{-1},\quad z=\kappa^{-1}.
 \tag{CG.2}
$$
Derivatives of $z$ in this note are in the original cut angle $\phi$. Derivatives of a function composed with $H$ are in the root input angle.

WY.39--41, with the exact first normalizer of FA.28, identify
$$
 \begin{split}
 \alpha^{(0)}_{\sigma,\epsilon}
   &=L_{\sigma,\epsilon,c}\,\kappa,\\
 \alpha^{(1)}_{\sigma,\epsilon}
   &=\mathscr J_\sigma
      \left(A_{-\sigma,1}
          -\frac{S A_{-\sigma,0}}{i\epsilon\kappa}\right),\\
 d_{\sigma,\epsilon,c}
   &=\frac{i\epsilon\,\alpha^{(1)}_{\sigma,\epsilon}}
            {L_{\sigma,\epsilon,c}\kappa},\qquad
 C_{\sigma,\epsilon,c}=d_{\sigma,\epsilon,c}\circ H.
 \end{split}\tag{CG.3}
$$
Here $L_{\sigma,\epsilon,c}=\ell_{\sigma,\epsilon}^*E(r_c)$ is a radial scalar. The leading vector $A_{-\sigma,0}$ is on the own row. Since $S$ is off diagonal, its own-row contribution in the second line is exactly zero:
$$
 \alpha^{(1)}_{\sigma,\epsilon}=\mathscr J_\sigma A_{-\sigma,1}.
 \tag{CG.4}
$$
This equality follows from the original leading and first-frame identities; it is not a cancellation between unrelated norm estimates. The opposite-row first coefficient, all primitive means/tails and the complete FA remainder remain where FA.28--32 placed them.

The original input primitive gives $Ie_j=(i\epsilon n)^{-1}e_j$, so (CG.3) is an exact rewrite of the finite first-amplitude map:
$$
 e^{i\epsilon n\Phi}
       \{\alpha^{(0)}_{\sigma,\epsilon}
                         +n^{-1}\alpha^{(1)}_{\sigma,\epsilon}\}
 =L_{\sigma,\epsilon,c}U_\Phi(1+M_{C_{\sigma,\epsilon,c}}I)e_j.
 \tag{CG.5}
$$
No output primitive is expanded a second time in (CG.5).

The two physical input signs give one real function, exactly as proved in WY.42--44. For each sign the complete PF/CT transport equation is
$\partial_\rho C_{\sigma,\epsilon}=-U_{H_\sigma}a_\sigma$, with a common real right side. The root expansion has the same two singular functions and the same individual finite function $F_*$ for both signs. Their difference, and the difference from the complex conjugate, are radial constants with zero root limit. Hence
$$
 C_{\sigma,+}=C_{\sigma,-}=:C_\sigma,\qquad
 C_\sigma\ \hbox{is real}.
 \tag{CG.6}
$$
This argument uses the complete pointwise root normalization, not equality of two norm bounds or only the scalar finite part. The Airy/Maslov sign factors remain in the original leading input diagonal.

## CG2. A cut leading inverse from the already computed KL numerator

The exact correlated leading identity KL.8--11 applies at the cut as well as the waist:
$$
 |L_{\sigma,\epsilon,c}|^{-1}
 =\frac{\sqrt{2\pi}}{n_g(r_c)}
       \left(\frac{\eta_*}{k_*}\right)^{1/6}
       k_{\rm root}(r_c)^{-1}.
 \tag{CG.7}
$$
The common root-short numerator is already a specified KL output:
`complete_new_leading_scalar_conclusion.complete_saved_root_short_common_numerator_upper`.
Write this complete upper bound as $N_{\rm KL}$. Its identity contains no endpoint density division and no strict cut-to-waist exponential.

Let $n_{c,-}>0$ be the original ST cut lower bound, copied verbatim in the successful FA field
`complete_new_first_frame_and_leading_conclusion.same_cut_ng_lower_read_verbatim`.
Define only the new scalar
$$
 L_c^\#=\frac{N_{\rm KL}}{n_{c,-}}.
 \tag{CG.8}
$$
Then $|L_{\sigma,\epsilon,c}|^{-1}\le L_c^\#$ for every sign and branch. The denominator is its positive lower endpoint. No WX forward radial factor, waist density, additional $n_g^{-1}$, or norm of $B_{\rm free}^{[1]}$ is used here.

The original KL numerator must be read as a completed new result, rather than recomputed after it has succeeded. The exact terminal-Ai reference restriction remains: (CG.7) does not normalize an unrelated second reference column.

## CG3. The cut coefficient from saved amplitude and phase derivatives

Read the three complete FA numbers
$$
 a_j\ge
 \|\partial_\phi^j A_{-\sigma,1}\|_{\infty,\mathrm{entry\ sum}},
 \qquad
 z_j\ge\|\partial_\phi^j\kappa^{-1}\|_\infty,
 \qquad j=0,1,2 .
 \tag{CG.9}
$$
Their field names are
`complete_common_each_sign_each_branch_A1_angular_jets`
and `complete_phase_reciprocal_angular_jets`, inside the successful FA first-frame conclusion. The original producer constructs complete derivative suprema before their later $H^2$ use; they are not derivatives recovered from an $L^2$ norm. The bounds are common to each branch and sign. They already bound either scalar own component; no factor for summing four sectors is inserted.

By (CG.3)--(CG.4), complete cut-angle derivative bounds for $d$ are
$$
 D_j=L_c^\#\sum_{\ell=0}^j{j\choose\ell}a_\ell z_{j-\ell},
 \qquad j=0,1,2 .
 \tag{CG.10}
$$
The radial $L_{\sigma,\epsilon,c}$ is differentiated zero times. The factor $i\epsilon$ has modulus one.

The inverse-map identities are
$$
 \begin{split}
 H'&=z\circ H,\\
 H''&=(zz')\circ H,\\
 H'''&=(z(z')^2+z^2z'')\circ H .
 \end{split}\tag{CG.11}
$$
Therefore the following three scalars bound the complete root-angle derivatives of $C_{\sigma,c}$:
$$
 \boxed{\quad
 c_0=D_0,\qquad
 c_1=D_1z_0,\qquad
 c_2=D_2z_0^2+D_1z_0z_1 .
 \quad}
 \tag{CG.12}
$$
All estimates in this section are suprema. Composition does not require an additional measure factor at this stage. Their use as normalized-circle $L^2$ bounds is the inequality $\|f\|_2\le\|f\|_\infty$, rather than an uncharged $L^2$ change of variables.

In particular (CG.12) is not obtained by dividing the upper norm of the complete corrected map by another norm upper, or by treating the uncorrected $L_-$ as the corrected coefficient. The actual coefficient and the actual leading denominator have been identified first.

## CG4. The propagated coefficient from the complete SJ integrals

The exact strict first transport is
$$
 \mathfrak c_\sigma(0)
    =\int_{r_c}^{0}U_{\chi_\sigma(r)}a_\sigma(r)\,dr ,
 \qquad
 g_\sigma=U_H\mathfrak c_\sigma(0)
          =H'\{\mathfrak c_\sigma(0)\circ H\}.
 \tag{CG.13}
$$
The orientation and density are those of SF and WY.45--46. In particular $C_\sigma(0)=C_{\sigma,c}+g_\sigma$ exactly.

SJ.44--45 defines complete ordinary-$dr$ bounds
$$
 C_j^\#\ge\|\partial_\phi^j\mathfrak c_\sigma(0)\|_\infty,
 \qquad j=0,1,2 ,
 \tag{CG.14}
$$
and the SJ consumer retains them as
`complete_new_transported_coefficient_conclusion.common_both_branch_complete_c_0_2_integrals`.
They include the full transported coefficient, its mean and every original radial subinterval. This is a separate completed output required by CG; an incomplete SJ prefix is not an input.

Using (CG.11), the full density composition gives
$$
 \boxed{\begin{split}
 g_0&=z_0C_0^\#,\\
 g_1&=z_0z_1C_0^\#+z_0^2C_1^\#,\\
 g_2&=(z_0z_1^2+z_0^2z_2)C_0^\#
               +3z_0^2z_1C_1^\#+z_0^3C_2^\# .
 \end{split}}
 \tag{CG.15}
$$
These bound $g_\sigma$ and its first two ordinary angular derivatives. No new ray integration, old profile integral or repeat of the SJ source calculation is involved. A positive integral bound is not subtracted from a total upper bound to infer another coefficient.

For later use set
$$
 h_j=c_j+g_j\quad(j=0,1,2).
 \tag{CG.16}
$$
They bound the full $C_\sigma(0)$ derivative columns, without using an unproved cancellation between its two summands. If a separately completed computation bounds the same whole function more sharply, whole-function bounds may be compared; neither individual summand is recovered by reverse subtraction.

## CG5. Three separate multiplier windows with the complete mean

For a scalar coefficient $f$ let
$$
 W_s(f)=\sum_{j\in\mathbb Z}(1+|4j|)^s|\widehat f_j|.
$$
A complete multiplier bound on $H^t$ is $W_{|t|}(f)$. Suppose $\|f\|_\infty\le f_0$ and
$\|\partial_\phi^j f\|_2\le f_j$ for $j=1,2$. In particular $\|f\|_2\le f_0$.
The following bounds retain the zero mode:
$$
 \begin{split}
 m_0(f)&\le f_0,\\
 m_{-1/3}(f)&\le f_0+\frac{39}{32}f_1,\\
 m_{-4/3}(f)&\le f_0+\frac{243}{160}f_2.
 \end{split}\tag{CG.17}
$$
The first is the complete sup bound when $f_0$ has that meaning, as all three arrays in CG do. For the other two lines the mean is bounded by $|\Pi f|\le f_0$.

For the full nonzero signed sum,
$$
 \left(\sum_{j\ne0}|4j|^{-4/3}\right)^{1/2}<\frac98 .
$$
Use $(1+n)^{1/3}\le(13/12)n^{1/3}$ and
$(1+n)^{4/3}\le(27/20)n^{4/3}$ for $n\ge4$, followed by Cauchy--Schwarz against the first and second derivative, respectively. This proves the exact constants in (CG.17). There is no finite-head truncation of this sum.

Apply (CG.17) independently to $(c_0,c_1,c_2)$ and $(g_0,g_1,g_2)$. Write the first pair of nonzero-window bounds as $m_{c,-1/3}$ and $m_{c,-4/3}$. The generally nonzero mean of $C_{\sigma,c}$ is not replaced by that of $g_\sigma$ or $C_\sigma$.

The original complete scalar inequality
$W_{4/3}(f)\le3(f_0+\sqrt2f_1+f_2)$
is another admissible whole bound. For a vector or matrix, the right side is summed componentwise; it is not silently changed into a Euclidean vector norm. The present branch coefficients are scalars.

## CG6. The inverse-displacement and projection dual rows

Put
$$
 p_H=H-\mathrm{id}-\langle H-\mathrm{id}\rangle,\qquad
 R_1=z_0z_1,\qquad
 C_{I^2}=\frac{17^{2/3}}{16}<\frac12 .
 \tag{CG.18}
$$
The mean-zero function $p_H$ satisfies $p_H''=H''$ and hence $p_H=I^2H''$. On the physical $4\mathbb Z$ nonzero spectrum,
$$
 \|I^2\|_{L^2\to H^{4/3}}
 =\sup_{n=4,8,\ldots}\frac{(1+n^2)^{2/3}}{n^2}
 =C_{I^2}.
 \tag{CG.19}
$$
The ratio is decreasing in $n>0$; $C_{I^2}<1/2$ follows from $17^2<8^3$. Thus
$$
 P_H:=C_{I^2}R_1\ge\|p_H\|_{H^{4/3}}.
 \tag{CG.20}
$$
No $H^3$ ball has been divided to infer a lower-order component.

Two complete supremum bounds are available:
$$
 P_\infty=
 \min\left\{\frac{\pi}{8}(z_0+1),\,\frac18 R_1\right\}
 \ge\|p_H\|_\infty .
 \tag{CG.21}
$$
For the first, $p_H=I(H'-1)$ and the period-$\pi/2$ mean-zero primitive kernel has $L^1$ norm $\pi/8$.
For the second, the full two-sign Cauchy--Schwarz estimate gives
$\sum|\widehat p_j|\le(\sum_{j\ne0}|4j|^{-4})^{1/2}\|H''\|_2$,
and the square-root sum is strictly less than $1/8$. Both are whole bounds for the same displacement.

An optional sharper complete candidate uses two already saved FA holomorphic moduli:
$$
 e_\kappa=
  \texttt{x\_deviation}
   +\sqrt{\texttt{T\_upper}}\ \texttt{y\_upper}.
$$
The exact $\Phi_\phi=X_\phi\pm\sqrt{-T}\,T_\phi$ gives
$|\kappa-1|\le e_\kappa$. Only if the new directed test $e_\kappa<1$ passes may the further bound
$$
 \|p_H\|_\infty\le
       \frac{\pi e_\kappa}{8(1-e_\kappa)}
 \tag{CG.22}
$$
be used in the whole minimum. This candidate uses the same real cut and original full holomorphic bounds; it never upgrades real jets to holomorphic suprema.

There is an equally direct dual bound for the independent waist projection row:
$$
 IC_\sigma=I^2\partial_\phi C_\sigma,\qquad
 P_C:=C_{I^2}h_1\ge\|IC_\sigma\|_{H^{4/3}}.
 \tag{CG.23}
$$
The scalar mean disappears here by the displayed original primitive identity, not by a hypothesis that $C_\sigma$ has mean zero. Its full mean is still present in (CG.17), the full branch operator and all physical mean rows.

## CG7. Complete WY algebra and waist projection fees

The exact original full-circle conjugation is
$$
 U_\Phi^{-1}(1+M_{\mathfrak c_\sigma}I)U_\Phi
 =1+M_{g_\sigma}I+
       g_\sigma\otimes p_H-(g_\sigma p_H)\otimes1 .
 \tag{CG.24}
$$
It contains both rank terms. Its multiplication by the original cut factor yields WY.23. Consequently
$$
 \boxed{\quad
 R_{\rm alg}^\#
 =C_I^2g_0\,m_{c,-1/3}
      +g_0(P_H+P_\infty)(1+m_{c,-4/3}/4),
 \qquad C_I=\frac{\sqrt{17}}4,
 \quad}
 \tag{CG.25}
$$
is a complete bound from $H^{-4/3}$ to $L^2$. The first term uses the intermediate $H^{-1/3}$ multiplier window between the two genuine primitives. The second includes the constant row, whose dual norm is one, and the same-window original cut factor on its right.

Let $B_{X^{-1},0}$ be the successful WX complete inverse-density $L^2$ bound for the actual root-labelled waist map. Then the independent projection rank of WY.25--29 has the complete contribution
$$
 \boxed{\quad
 C_{\rm proj}^\#
 =(1+B_{X^{-1},0})R_{\rm alg}^\#
               +B_{X^{-1},0}P_C .
 \quad}
 \tag{CG.26}
$$
This is distinct from the cut primitive rank already paid in FA and from the interval primitive rank already paid in SJ. The exact transported output $U_X^{-1}1$ remains. For low/mean input the additional original row $\Pi a$ remains in the finite border; (CG.23) does not remove it.

Each displayed bound applies to either original physical branch, with its original sign normalization. If a later map requires a sum of scalar component norms, that sum is made explicitly there. No extra factor from summing the two equal input-sign coefficient functions is introduced here.

## CG8. Common-root and selected-angle coefficient costs stay ordered

Suppose the TF scalar has separately completed and read
$F_A$, $J_F$, $K_{F,-4/3}$ and the declared compressed multiplier
$\overline m_{F,-1/3}(J_F)$. A complete scalar bound for
$\widetilde C_\sigma=C_\sigma-F_*$ is
$$
 \widetilde h_0=h_0+F_A .
 \tag{CG.27}
$$
No whole upper is subtracted to obtain it. The two additional root terms retain their original form
$$
 \alpha_J\widetilde h_0\overline m_{F,-1/3}(J_F),
 \qquad
 F_J^\#=2C_I F_A\Lambda_{J_F+191}^{1/3},
 \quad
 \alpha_J=\frac{\Lambda_{J_F}^{4/3}}{(4J_F)^2}.
 \tag{CG.28}
$$
If these scalar factors were already evaluated and saved in TF, they are read unchanged. Otherwise they are only new scalar products in the CG consumer. Their exact finite maps and the full root $F_J$ are not deleted.

For the same selected parameter, WX supplies
$S_0\ge\|\mathcal S\|_{L^2\to L^2}$,
$S_-^{\rm inv}\ge\|\mathcal S^{-1}\|_{H^{-4/3}\to H^{-4/3}}$,
and complete bounds $P_{S,H},P_{S,\infty}$ for the zero-mean displacement of its actual common input map. WY.50 gives
$c_i=\mathcal S\widetilde C_+$ and
$c_o=\mathcal S\widetilde C_-$.
The two additional IC full-density primitive ranks therefore have the safe complete fee
$$
 R_{\rm principal}^\#
 = S_0\widetilde h_0(P_{S,H}+P_{S,\infty}).
 \tag{CG.29}
$$
Indeed $\|c_\sigma\|_2\le S_0\widetilde h_0$, and
$\|c_\sigma p_{\mathcal S}\|_2\le
\|c_\sigma\|_2P_{S,\infty}$. Both ranks and the actual mean are present. These selected-coordinate inputs are not used to assert a family of principal conjugacies throughout $|\delta|\le10^{-8}$.

Thus one complete coefficient-only part of WY.36 is
$$
 \boxed{\quad
 C_{\rm coeff}^\#
 =S_0K_{F,-4/3}S_-^{\rm inv}
       \{C_{\rm proj}^\#
          +\alpha_J\widetilde h_0\overline m_{F,-1/3}
          +F_J^\#\}
       +R_{\rm principal}^\# .
 \quad}
 \tag{CG.30}
$$
This formula does not include the distinct actual state-error term, any original finite/mean-realization/other-sign row not already included, or a finite Schur inverse. The exact right order remains
$E_*\Lambda_\sigma^{-1}T_F^{-1}\mathcal S^{-1}$.
In particular the exact left angular cancellation available for the state term of WY.35 is not applied to (CG.30).

## CG9. Small readout schema and completion boundaries

A single later current-only consumer can evaluate these formulas after all required numerical inputs are complete:

| Role | Exact already defined object/field | Use |
|---|---|---|
| FA2 small science, successful run43763658978/1 | `complete_new_first_frame_and_leading_conclusion.complete_common_each_sign_each_branch_A1_angular_jets` and `complete_phase_reciprocal_angular_jets` | Complete $a_0,a_1,a_2,z_0,z_1,z_2$; per-branch sup/entry-sum provenance |
| Same FA2 object | `same_cut_ng_lower_read_verbatim` within that conclusion | Positive ST $n_g(r_c)$ lower, exactly once |
| KL completed small science, successful run43766439345/1 | `complete_new_leading_scalar_conclusion.complete_saved_root_short_common_numerator_upper` | $N_{\rm KL}$ without waist forward factor or endpoint density |
| SJ completed small science, required when available | `complete_new_transported_coefficient_conclusion.common_both_branch_complete_c_0_2_integrals` | All three complete ordinary-$dr$ transport bounds; no reintegration |
| WX execution, successful run43763424840/1 | `complete_waist_density_coordinate_conclusion.complete_inverse_density_L2_upper` | The actual inverse waist density factor in (CG.26) |
| Same WX object, only same selected parameter | `complete_selected_common_input_conclusion.complete_common_input_L2_upper`, `complete_common_input_inverse_Hminus4_3_upper` | The original $\mathcal S$ order and the correct two windows |
| Same WX object, only same selected parameter | `complete_full_primitive_rank_conclusion.selected_common_input.complete_zero_mean_displacement_H2_and_H4_3_upper` and `complete_zero_mean_displacement_Linfty_upper` | The actual dual displacement bounds in (CG.29), without recomputing a flow |
| TF completed small science, required when available | Full $F_A,J_F,K_{F,-4/3}$ and any already saved strong/finite factors | The same root-coordinate inverse and its complete complement |

Execution-record scientific fields are read under `actual_scientific_receipt`. The FA and WX exact source/manifest/gate identities, all new KL/SJ/TF identities, the same repaired family, fixed cut, actual physical frequencies, both means and the terminal-Ai reference are mandatory gates. A partial prefix, a wrapper status label, or the norm of only $C_o-C_i$ is insufficient.

The optional (CG.22) candidates use the FA fields
`complete_x_deviation_holomorphic`,
`complete_T_holomorphic_upper_read_from_original_full_Ap` and
`complete_y_holomorphic`
inside `complete_new_cut_domain_conclusion`.
No old full-complex fold is run again.

The new receipt should retain the complete three-column arrays $(D_j),(c_j),(g_j),(h_j)$, the separate three multiplier windows, $P_H,P_\infty,P_C$, the two WY fees, and any coefficient-only principal fee. This preserves the individual functions' complete positive bounds for later use. It does not replace them by a total upper that would later require an unjustified subtraction.

All new arithmetic is restricted to public Actions. Old source/profile/ray/normalizer/mean calculations are read only. A successful new small scalar is saved before any formatting or publication gate. No new Fourier arrays or radial references are needed for this consumer.

## CG10. Immutable primary identities

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WY complete object identification and four receivers | 847a7dd335158482811561c2ed5e1aa7175e8797 | 30764 | ebf8713508a11ef96decc5691056ea6eaa15d967d08b3a8af4b20c4284f6d1b3 |
| FA final analytic proof | acfb0cfd9a2598c00a6b29c2db05041d0340cba9 | 27814 | 24216c6d78f1261e16b9d53030fb2b899a94e9e9d8900e7fea79746ef32d96af |
| FA2 final scientific source | 9e0a75461e0b8302a82e0444828a2c86379c3443 | 48827 | a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954 |
| FA2 complete small science | 2001f4e2eeece1cda56b18b90dccab04b7f6d336 | 35718 | 2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2 |
| WX successful execution | 5121a599896025d90e2861450756a256aaba659d | 43753 | e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12 |
| KL analytic leading-scalar contract | cf3e435f21bbce03ad051a19676428504d490dcd | 13896 | dc48bdb46fde624f5e6f3820a7f37e326cb3b84274f34d46e1538f6166285b9a |
| KL complete small science | d24a1ecdd9b4397184a3ab932a503e8eb79d0c24 | 20537 | 1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee |
| SJ radial/transport/interface contract | 32f770ec471af361dc3668bbe2ef37a0fddcd738 | 36867 | ccaaa1b17fd68ce64d79a7bdc40dae9c0843b610da11149c178e92079d495f31 |
| TF common-root analytic contract | 1052d454e98c613177919b7b19e472da1364a828 | 14951 | 652a9a2c2a9e0ccce1b07adae8848837ba579bec63d6ba5da21989a24b1bf5a3 |

KL's small science has completed; its root-short numerator is read rather than recomputed. SJ and TF are cited as analytic contracts here, without asserting completion of their numerical consumers. The present new result is the fully typed scalar recipe. The complete incoming/outgoing strong remainder, the true finite blocks and final incoming inverse remain separate until their actual full inputs are supplied.
