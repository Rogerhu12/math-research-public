# R133 supplement: the same positive Airy cutoff in its actual output window

2026-11-16, visible-exact / newton_source.

**Proved new complete cutoff recipe; no numerical evaluation.**
This keeps the original PC genuine terminal-Ai column, root shear, physical two-row reconstruction, cutoff, positive boundary problem, finite-head source and both means. The new target is exactly the old cutoff source $\chi'h^G$, now estimated directly from $H^{-4/3}$ into its actual $H^{-2/3}$ pair-source window using all output frequencies.

Every numerical input below is already saved in the complete PC execution. The proposed new calculation uses finite positive combinations, rational powers and whole-bound choices. It needs no old native, profile solve, amplitude differentiation, row restoration, ray, graph, source integral or exponential-sum reevaluation.

## WPC1. Unchanged source and exact units

Use the same real repaired family, fixed intrinsic parameter, actual root piece2549 and both signs as PC. Real parameters are imposed before the real-phase estimates. Write
$$
 n=4|j|\ge N:=388,\qquad \Lambda_j=(1+16j^2)^{1/2},\qquad P=Id-\Pi.
 \tag{WPC.1}
$$
The original normalized terminal profile $Y_n=f_n/a_n$ satisfies
$$
 Y_{TT}=(n^2T-V_n)Y,\qquad
 (Y,Y_T)(0)=
 \big(\operatorname{Ai}(0)+\beta_n\operatorname{Bi}(0),
 n^{2/3}[\operatorname{Ai}'(0)+\beta_n\operatorname{Bi}'(0)]\big).
$$
Its terminal Ai condition remains at $L=1/2000$. The entire nonzero $\beta_n$ remains.

For $q=(a,b)^t$, set
$$
 {\sf T}_n(q)=n^{7/6}e^{i\epsilon nX}(aY_n+n^{-1}bY_{n,T}),\qquad
 w=w_0+n^{-1}w_1^V.
 \tag{WPC.2}
$$
The original physical rows are
$$
 h_2^G=P{\sf T}(w),\qquad h_1^G=J(D_0-B_{\rm op})h_2^G.
 \tag{WPC.3}
$$
Keep precisely PC.8's quintic cutoff on $2\,10^{-6}<s=r-r_*<3\,10^{-6}$:
$$
 \|\chi'\|_\infty\le1875000,\qquad \ell_{\rm cut}=10^{-6},\qquad
 {\cal L}(\chi h^G)=\chi{\cal L}h^G+\chi'h^G.
 \tag{WPC.4}
$$
The target is exactly
$$
 \chi'h^G:H^{-4/3}_{|j|\ge97}\longrightarrow
 L^2_{\rm cut}(H^{-2/3}\oplus H^{-2/3}).
 \tag{WPC.5}
$$
PW.3 admits this complete collar pair source. It is not restricted to the special zero-second-row negative source used in WUB. A mean-zero trial component does not remove the independent physical mean of its ordinary residual. The unchanged volume and finite-to-high sources keep their own admitted spaces.

## WPC2. Two derivatives for this weighted Schur estimate

First use $\xi=X(\phi)$, with the actual degree-one real lift. Suppose symbols $b_j(\xi)$ obey uniform bounds $D_0$ and $D_2$ for their value and second derivative. The weighted matrix
$$
 M_{mj}=\Lambda_m^{-2/3}\widehat b_j(m-j)\Lambda_j^{2/3}
 \tag{WPC.6}
$$
satisfies, for $l=m-j$,
$$
 \frac{\Lambda_j^{2/3}}{\Lambda_m^{2/3}}\le(1+4|l|)^{2/3},\qquad
 |\widehat b_j(l)|\le
 \begin{cases}D_0,&l=0,\\ D_2/(16l^2),&l\ne0.\end{cases}
$$
Both full Schur sums are consequently at most
$$
 D_0+\frac{D_2}{8}\sum_{l\ge1}\frac{(1+4l)^{2/3}}{l^2}
 \le D_0+\frac{5^{2/3}}2D_2
 <D_0+\frac32D_2.
 \tag{WPC.7}
$$
Here $\sum l^{-4/3}\le4$ and $5^{2/3}<3$. Input-label dependence of $b_j$ does not change either sum. No label derivative or output orthogonality is needed; zero and the full finite output are retained. Two derivatives suffice for exponent $2/3$ here. The corresponding sum with exponent $5/3$ would diverge, so this is not an arbitrary-window claim.

Read $X_\phi\ge m>0$, $|X_{\phi\phi}|\le F_2$. Bounds $D_k$ in the original angle give
$$
 \widetilde D_2=D_2/m^2+F_2D_1/m^3
 \tag{WPC.8}
$$
after the inverse angle. PC saves the complete scalar-pullback bound $C_X$ on $H^{-5/3}$, obtained by duality from the actual adjoint density composition. The same pullback has $L^2$ bound $m^{-1/2}$. Interpolation gives
$$
 C_{X,2/3}=(m^{-1/2})^{3/5}C_X^{2/5}.
 \tag{WPC.9}
$$
This scalar composition is not interchanged with a full-density coordinate map.

## WPC3. Exact profile weight shift

Put $t=n^{2/3}T$ and retain the original PC profiles
$$
 P_a=n^{1/6}Y_n,\qquad P_b=n^{-5/6}Y_{n,T}.
$$
Then $\mathsf T_n(q)=n e^{i\epsilon nX}(aP_a+bP_b)$. In (WPC.6), use
$$
 b_j=\Lambda_j^{2/3}n(aP_a+bP_b)\circ X^{-1}.
 \tag{WPC.10}
$$
The input factor $\Lambda_j^{4/3}$ and output $\Lambda_m^{-2/3}$ leave exactly the ratio in (WPC.6). Hence
$$
 \Lambda_j^{2/3}n\le k_N n^{5/3},\qquad
 k_N=(1+N^{-2})^{1/3},\qquad
 n^{5/3}=T^{-5/2}t^{5/2}.
 \tag{WPC.11}
$$
The original profile contributes $T^{-1/4}$. The total radial factor is therefore $T^{-11/4}$, and each original moment $S_p$ changes to $S_{p+5/2}$. The physical input normalization remains $n^{7/6}$.

A complete rational-power upper for each new moment is
$$
 \widehat S_p=\left(\frac{3p}{8}\right)^{2p/3},\quad p>0,
 \qquad
 \sup_{t\ge0}t^p e^{-2t^{3/2}/3}=(p/e)^{2p/3}\le\widehat S_p.
 \tag{WPC.12}
$$
The inequality uses $e>1+1+1/2+1/6=8/3$, and requires no exponential evaluation. The seven new exponents are $\{11,13,15,17,19,23,25\}/4$.

Read the original complete $C_A,M_0,M_1,Z_0,Z_1,Y_0,Y_1$ in the precise PC.11--14 meanings. Define
$$
 \begin{aligned}
 A_0&=\widehat S_{11/4},\\
 A_1&=Z_0(\widehat S_{15/4}+\widehat S_{17/4}),\\
 A_2&=Z_0^2\widehat S_{23/4}
      +M_0Y_0^2\widehat S_{11/4}
      +Z_1(\widehat S_{15/4}+\widehat S_{17/4}),\\
 B_0&=N^{-1/3}(\widehat S_{11/4}+\widehat S_{13/4}),\\
 B_1&=N^{-1/3}Z_0\widehat S_{19/4}
              +M_0N^{-1}Y_0\widehat S_{11/4},\\
 B_2&=N^{-1/3}\big[
 Z_0^2(\widehat S_{19/4}+\widehat S_{23/4}+\widehat S_{25/4})
 +Z_1\widehat S_{19/4}
 +M_0Y_0^2(\widehat S_{11/4}+\widehat S_{13/4})\big]\\
 &\quad+N^{-1}(M_1Y_0^2+M_0Y_1)\widehat S_{11/4}.
 \end{aligned}
 \tag{WPC.13}
$$
These are obtained by multiplying every complete PC.14 derivative term by $t^{5/2}$ before taking its supremum. The underlying derivative calculation uses the actual genuine ODE with both $V_n$ and $V_{n,T}$. No interval upper is differentiated; the original inverse powers of $n$ are bounded by $N$ exactly as in PC.

Let $\gamma_k=\max(A_k,B_k)$ and let $T_->0$ be the saved full-transition lower bound. For complete component-sum amplitude jets
$d_k\ge\sup(|\partial_\phi^ka|+|\partial_\phi^kb|)$, define
$$
 D_k(d)=k_NC_AT_-^{-11/4}
              \sum_{\ell=0}^k {k\choose\ell}\gamma_\ell d_{k-\ell},
$$
$$
 {\cal F}(d)=C_{X,2/3}\left[
 D_0(d)+\frac32\left(\frac{D_2(d)}{m^2}
                         +\frac{F_2D_1(d)}{m^3}\right)\right].
 \tag{WPC.14}
$$
Leibniz and (WPC.7)--(WPC.11) prove
$$
 \|P{\sf T}(q):H^{-4/3}\to H^{-2/3}\|\le{\cal F}(d).
 \tag{WPC.15}
$$
The same bound holds without $P$, so its proof has not discarded a mean.

## WPC4. New Cauchy jets from saved full moduli

No old amplitude derivatives are recomputed. PC's complete verified products give on $|\Im\phi|\le s_p=1/256$,
$$
 \|w\|_1\le W,\qquad \|Dw\|_1\le W_D,\qquad
 \|p\|_1\le P_0,\qquad
 p=(H_n^V)^{-1}H_{D,n}^Vw .
 \tag{WPC.16}
$$
These component-sum moduli are uniform over both signs, all input frequencies and the entire transition. The genuine inverse retains its original determinant gap. The strip $s_p$ lies strictly inside the old fold, potential, inverse and amplitude domains.

The immutable PC producer's cutoff_and_head function constructs $W,W_D$ on that strip from the full leading/genuine moduli and their radial and angular margins. It constructs $P_0$ from the full matrix-entry bound, the complex-shift $H_D$ bound and $W$. The saved shift value of $P_0$ is thus a bound on the larger $s_p$ strip before its derivative is estimated on the shifted circle. This is verified from the old source, not inferred from a real derivative bound.

Set
$$
 h^{\rm amp}=p/\eta,\qquad g^{\rm amp}=Dw-p_\phi.
 \tag{WPC.17}
$$
Read the saved complete shift reconstruction $H$ for the full-strip modulus of $h^{\rm amp}$. The real saved $G$ is a complete zero-order bound for $g^{\rm amp}$. The required lists are
$$
 \begin{array}{c|ccc}
 &d_0&d_1&d_2\\ \hline
 w&W&W/s_p&2W/s_p^2\\
 h^{\rm amp}&H&H/s_p&2H/s_p^2\\
 g^{\rm amp}&G&W_D/s_p+2P_0/s_p^2&
                 2W_D/s_p^2+6P_0/s_p^3 .
 \end{array}
 \tag{WPC.18}
$$
The angle-independent $\eta$ has the original positive gap throughout this real radial interval. Cauchy for a vector holomorphic function in the component-sum norm gives $k!s_p^{-k}$ without an extra component factor. The needed third derivative of $p$ is a new complete Cauchy product; it is not claimed as a saved RJ third jet. The real $G$ is used only for $d_0$.

## WPC5. The full matrix words in the output window

PC saves the complete exponential-lag matrix norms $z_J,z_B,z_L$ at width $\delta_0=1/64$, uniformly on every actual positive intersection. They are M.1 row/column Schur norms, not merely real-circle $L^2$ numbers. Keep the entire nonlocal words and their old mean convention.

For any such matrix $A$,
$$
 \|A\|_{H^{-2/3}\to H^{-2/3}}\le q_{2/3}z_A,\qquad
 q_{2/3}=\frac{64}{63}16^{2/3}.
 \tag{WPC.19}
$$
To prove this, use the weight ratio $(1+x)^{2/3}$, $x=4|m-k|$. The lag norm pays $e^{\delta_0x}$. The maximum of
$(1+x)^{2/3}e^{-\delta_0x}$ occurs at
$x=(2/3)/\delta_0-1>0$ and equals
$((2/3)/\delta_0)^{2/3}e^{\delta_0-2/3}$.
The bounds $e>8/3$ and $e^{1/64}\le(1-1/64)^{-1}$ give (WPC.19).

Exponential-lag norms are submultiplicative in the actual order. Therefore
$$
 \|JL_A\|_{H^{-2/3}\to H^{-2/3}}\le q_{2/3}z_Jz_L,\qquad
 \|JB_{\rm op}\|_{H^{-2/3}\to H^{-2/3}}\le q_{2/3}z_Jz_B.
 \tag{WPC.20}
$$
Each complete word has only one window conversion. No factors commute or disappear. The old inverse has exactly the zero mean row/column extension used by the paid directed-matrix theorem; its physical parity restriction is unchanged.

## WPC6. Full two-row cutoff and same received positive correction

The exact PC.26a reconstruction is
$$
 h_1^G=P{\sf T}(h^{\rm amp})
   +J\{P{\sf T}(g^{\rm amp})
              -L_AP{\sf T}(h^{\rm amp})
              -B_{\rm op}P{\sf T}(w)\},\qquad
 h_2^G=P{\sf T}(w).
 \tag{WPC.21}
$$
Apply (WPC.14) to the three lists in (WPC.18), calling the results $F_w,F_h,F_g$. Then
$$
 \begin{aligned}
 C_1&=(1+q_{2/3}z_Jz_L)F_h
           +q_{2/3}z_JF_g+q_{2/3}z_Jz_BF_w,\\
 C_2&=F_w,\\
 C_{\rm cut}^{\,{\rm new}}
       &=1875000\sqrt{10^{-6}}\sqrt{C_1^2+C_2^2}.
 \end{aligned}
 \tag{WPC.22}
$$
This is a complete bound for (WPC.5). The radial factor is the original physical transition length. The pair norm is Euclidean. The full signed Schur matrix already includes both signs; restriction to the original orthonormal reflected input is contractive. Amplitude component-sum conversions remain in the actual moduli.

Read, without recomputing, the old PC volume $C_{\rm vol}$, finite-to-high source $C_{\rm FH}$, already composed positive collar-to-waist gain $K_{\rm pos}$, finite root received bound $C_F^{\,w}$, and old received positive bound $C_+^{\,w}$. Then
$$
 C_+^{\,w,{\rm new}}
       =K_{\rm pos}
           (C_{\rm vol}+C_{\rm cut}^{\,{\rm new}}+C_{\rm FH})
 \tag{WPC.23}
$$
bounds the same complete received positive correction.

The old $K_{\rm pos}$ already includes the seven-port positive graph, mixed root factor9 and negative receiver. None is multiplied again. The root finite output $C_F^{\,w}$ is distinct from (WPC.23).

The whole minimum of (WPC.23) and the saved $C_+^{\,w}$ is valid for exactly $\mathcal R_+$ in WUE.7. It may replace that one term in WUE.22/34. All negative sources and jumps, the full WES endpoint, coefficient algebra, mean ranks, true right $N_i$ and independent ports stay in place. No upper bound is subtracted.

This changes the proof of a bound, not the trial or physical source. Improvement has not yet been evaluated. No useful cutoff or finite inverse follows merely from the new formula.

## WPC7. Exact read-only input schema

The single scientific input is the successful PC execution at
notes/genuine_positive_Ai_cutoff_strong_correction_ci/run-43740173506-1/execution.json.
All paths below are under actual_scientific_receipt; original records are copied verbatim before typed reads.

| Symbol | Original complete field |
|---|---|
| $C_A$ | complete_positive_domain_conclusion.CA.ball |
| $T_-$ | complete_positive_domain_conclusion.Tmin.ball |
| $m$ | complete_positive_domain_conclusion.m.ball |
| $F_2,C_X$ | complete_positive_domain_conclusion.F2.ball, CX.ball |
| $M_0,M_1$ | complete_positive_domain_conclusion.V.ball, VT.ball |
| $Z_0,Z_1,Y_0,Y_1$ | complete_positive_domain_conclusion.Z0.ball, Z1.ball, Y0.ball, Y1.ball |
| $W,W_D$ | complete_cutoff_and_head_conclusion.complete_pair_amplitude_holomorphic_upper.ball, complete_D_amplitude_holomorphic_upper.ball |
| $P_0,H$ | complete_cutoff_and_head_conclusion.complete_shift_reconstruction_coefficients.P.ball, H.ball |
| $G$ | complete_cutoff_and_head_conclusion.complete_real_reconstruction_coefficients.G.ball |
| $z_J,z_B,z_L$ | complete_positive_volume_conclusion.same_shift_L2_word_maxima.J.ball, B.ball, L.ball |
| $C_{\rm vol}$ | complete_strong_correction_conclusion.complete_positive_ordinary_volume_upper.ball |
| $C_{\rm FH}$ | complete_strong_correction_conclusion.complete_finite_head_commutator_source_upper.ball |
| $K_{\rm pos}$ | complete_strong_correction_conclusion.accepted_positive_collar_to_waist_gain_read_verbatim |
| Old $C_{\rm cut}$ | complete_strong_correction_conclusion.complete_positive_cutoff_source_upper.ball |
| Old $C_+^{\,w}$ | complete_strong_correction_conclusion.new_positive_correction_to_waist_upper.ball |
| $C_F^{\,w}$ | complete_strong_correction_conclusion.new_root_finite_head_to_waist_upper.ball |

Only $T_-$ and $m$ have lower-endpoint roles. All moduli, norms and fees use the retained upper endpoints. The exact widths, cutoff derivative, transition length and frequency cutoff must match the original parameter and domain records. Preserve the complete real family, potential/terminal normalization, both signs, means and same-shift matrix qualifications of the successful thirty-gate receipt. A new consumer verifies its complete source/manifest chain; it does not claim to reverify the old large inputs.

The new mathematical targets are the shifted profile, finite Cauchy lists, actual-window Schur/word fees, full cutoff candidate, received candidate and whole choice. The unchanged old quantities are only read. No consumer is implemented or executed here.

## WPC8. Immutable evidence and remaining scope

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| PC proof: exact profile, cutoff, reconstruction and head | 35f3ddaec691c2d7c636ec43da3f52605ed6b329 | 37079 | 5368abae4c66f73800c16d5f2b906ddaa0f1d62d07e9bd9a3ca539061bdf5d68 |
| PC complete successful execution | c32b8e3f3aca08d338784504c2cce5054d203bc6 | 46253 | 75f780f60446bd2a47fe286e72ca24fad929e3486c12d9ecbea42f42b9b1a817 |
| PC source: exact full-strip and matrix-word identities | 8e9f008291af88054d21919c18b882873096684e | 56118 | da6864cd790162759d5a78d40a67d0f3b4aa91b60614d947cca1a92371d6940b |
| Directed analytic matrix theorem | a0006605b4f942fe31f8f3b2c80e7d00ac7d37de | 11462 | 394068a9b18a47d5c1b9330f162c39b9b02a0d65db4b46ba5773c995adc6a52e |
| PW: full positive pair port and received units | d22fc84975785bfdf0e0ba91b100d53c9d4c32a3 | 16459 | 246c81ac387392c75a3267faaa934a7f0a4b978fdad8b8ac7cbbd4bd5c413562 |

PC is results/R133-supplement-genuine-positive-Airy-cutoff-and-complete-strong-correction-columns.md; its source is scripts/fourfold_codazzi_genuine_positive_Ai_cutoff_strong_correction.py. The matrix proof is results/R133-supplement-directed-analytic-matrix-old-circle-remainders.md. All paths are within topics/visible-flex-exact-nearby.

The independently derived height-cut plus exact mean-completion trial remains an alternative with its full mean cutoff source and outer condition. It is not needed for (WPC.22)--(WPC.23), and none of its changed sources enter this proof.

Other large positive volume, head, coefficient and physical border terms require their own complete estimate or retained exact factorization. The true supplied radial head, both physical mean/amplitude equations, metric parameter and genuinely independent second input remain. This theorem supplies neither physical incoming onto nor a nonlinear solution.
