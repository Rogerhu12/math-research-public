# R133 supplement: waist normalizer coefficients from complete one-sided residuals

2026-11-15, visible-exact-astra-0df9 / tail_connector.

**Proved scalar-consumer contract; no new numerical conclusion.** At the true waist $r=0$, the completed background and response residual rows give complete right radial derivative bounds for the same selected reference used by SP, ST and TN. Combined with the completed SP waist mean and curvature factors, these give new waist values of the TN.7--TN.8 normalizer fees. The new computation uses only scalar combinations of saved enclosures.

The first consumer uses the wide state bounds already paid by D. It preserves the actual tests at both $J=97$ and $J=268435456$, and a separately selected sufficient dyadic cutoff. A failed sufficient test remains a failure of that test. A later sharper consumption of the original strict waist row must preserve this first result.

## 1. Same selected object and one-sided domain

Set
$$
 Q_\delta=Q_0+\delta Z,\qquad \nu_\delta=\nu_0+\delta,\qquad
 |\delta|\le d=10^{-8}.
 \tag{WT.1}
$$
The fixed intrinsic parameter and exact amplitude and centre parameter are
$$
 \eta_0=-\frac{7789843107295549}{4611686018427387904},\quad
 \alpha=\frac{6890507429876859}{9007199254740992},\quad
 \nu_0=-\frac{2572625729470897}{72057594037927936}.
 \tag{WT.2}
$$
The characteristic coefficient $\eta$ used later is distinct from $\eta_0$.

The raw background candidate has SHA256
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413.
The exact continuous definitions of $Q_0$ and $Z$ have SHA256
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
and
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
The original full response proposal is
ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6.
It contains 96 sine coefficients and 97 cosine coefficients, including its genuine even mean.

Use the original moving angle $\phi$, normalized period $\pi/2$, physical frequencies $4j$, and the full pair norm
$$
 \|Q\|_{A^0_\Sigma}=\|u\|_{A^0}+\|v\|_{A^0},\qquad
 I=\partial_\phi^{-1}P_{\ne0},\qquad \|I\|_{A^0\to A^0}\le1/4.
 \tag{WT.3}
$$
This dominates each component's uniform norm and the Euclidean pair $L^2$ norm. Both $v$ and $m=\langle v\rangle_\phi$ retain their genuine means.

Every radial derivative below is right one-sided at $0$. The first background residual row and the first body row need not share a right endpoint. Each must start at exactly zero, have positive length and lie in its own declared scalar germ; their common positive subinterval suffices. The body row must end at or before $1/20$.

The intrinsic bump is supported in $[1/20,9/50]$. Thus $\gamma,\beta,K$ and the full moving field are independent of $\nu$ near the waist. In particular the complete parameter source $\mathcal F_\nu$ vanishes there. This is an exact support statement.

D's successful raw-plus-repair state check supplies
$$
 \|Q_{\rm raw}\|_{A^0_\Sigma},\|Q_0\|_{A^0_\Sigma}\le7,\qquad
 \|(Q_{\rm raw})_\phi\|_{A^0_\Sigma},\|(Q_0)_\phi\|_{A^0_\Sigma}\le6,
$$
$$
 \|Z_{\rm raw}\|_{A^0_\Sigma},\|Z\|_{A^0_\Sigma}\le19,\qquad
 \|(Z_{\rm raw})_\phi\|_{A^0_\Sigma},\|Z_\phi\|_{A^0_\Sigma}\le83 .
 \tag{WT.4}
$$
The raw bounds are dominated by the same original nonnegative budgets before repairs are added. D's parameter-difference conclusion at radius $10^{-10}$ is not enlarged: only these four $\delta$-independent state bounds are reused. The triangle in (WT.1) is new, and the copied SP waist factors already have the $10^{-8}$ qualification.

## 2. Complete moving equations and the background amplitude

For $Q=(u,v)$ put
$$
 S_Q=u^2+Kv^2,\quad m=\langle v\rangle,\quad
 d_Q=-\beta I(S_Q),\quad J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
$$
The full moving field, as in R.2, is
$$
 \mathcal F(Q,\nu)=d_QQ_\phi+\gamma mJ(K)Q_\phi
                         +\beta(-u,v)-\beta S_QQ,
 \tag{WT.5}
$$
or componentwise
$$
 \mathcal F_u=d_Qu_\phi+\gamma mK v_\phi-\beta(1+S_Q)u,\qquad
 \mathcal F_v=d_Qv_\phi-\gamma m u_\phi+\beta(1-S_Q)v.
 \tag{WT.6}
$$
No angular output projection is inserted.

The raw producer uses
$$
 Q_{\rm raw}=(\alpha U,s+\alpha V),\qquad
 s=C_{\rm ref,\nu_0}^{-1},\qquad s_r=\beta s(1-Ks^2).
 \tag{WT.7}
$$
The last identity is the exact radial reference identity at P.7--P.8 of
[the polynomial chart theorem](R133-supplement-polynomial-Codazzi-chart-and-complete-boundary.md).
Only that scalar identity is used from its physical-angle presentation; the complete equation here is (WT.5) in the moving angle.

The normalized right sides used by the saved residual helper are
$$
 \begin{split}
 f_U={}&d_QU_\phi+\gamma mK V_\phi-\beta U(1+S_Q),\\
 f_V={}&d_QV_\phi-\gamma mU_\phi\\
 &+\beta\{V-K(3s^2V+3\alpha sV^2+\alpha^2V^3)
                              -\alpha(s+\alpha V)U^2\}.
 \end{split}\tag{WT.8}
$$
It saves bounds for $R_U=U_r-f_U$ and $R_V=V_r-f_V$. Including the complete scalar $s_r$ from (WT.7) gives exactly
$$
 (Q_{\rm raw})_r-\mathcal F(Q_{\rm raw},\nu_0)
                                      =\alpha(R_U,R_V).
 \tag{WT.9}
$$
Thus `rows[0].complete_residual_A0.U` and
`rows[0].complete_residual_A0.V` acquire exactly one factor $|\alpha|$.
The different saved physical inverse-coordinate residual is not substituted for these fields.

Let their nonnegative upper bounds be $r_U,r_V$. From the complete body-row intrinsic jets put
$$
 b=|\beta|_+,\quad k=\max(1,|K|_+),\quad B=bk,\quad G=|\gamma|_+k.
 \tag{WT.10}
$$
For $M=7$, $P=6$, a complete bound for
$\|(Q_{\rm raw})_r(0+)\|_{A^0_\Sigma}$ is
$$
 \boxed{R_Q=bM+B(M^3+M^2P/4)+GMP+|\alpha|(r_U+r_V).}
 \tag{WT.11}
$$
The four field terms pay the linear reaction, cubic reaction, full primitive drift and mean-dependent principal coupling. The two complete residual components are then added. This uses the actual residual identity and does not assume that the saved background is a PDE solution.

## 3. Raw response, complete mean and canonical repairs

The body producer forms
$$
 R_Z=(\partial_r-A_{\rm raw})Z_{\rm raw}
                      -\mathcal F_\nu(Q_{\rm raw},\nu_0),\qquad
 A_{\rm raw}=D_Q\mathcal F(Q_{\rm raw},\nu_0).
 \tag{WT.12}
$$
Its exact source identity is
`R = operator_action(Q,h,hr,a) - parameter_source(Q,a,left,right)`.
The first helper is the full unnormalized moving operator, including both the primitive rank term and the derivative of $m$. The response proposal is not multiplied by $\alpha$.

Only the saved representation is split:
$$
 R_{\rm nm}=(R_{Z,1},P_{\ne0}R_{Z,2}),\qquad R_m=\langle R_{Z,2}\rangle .
 \tag{WT.13}
$$
Read precisely
`rows[0].uncorrected_response_nonmean.A0_sup`
and `rows[0].response_mean_residual`. The first field is the sum of the two full scalar Wiener bounds, according to the original `norms` helper. It is not an $L^2$ norm or a componentwise maximum. Set
$$
 R_*=(R_{\rm nm})_{A^0_\Sigma,+}+|R_m|_+ .
 \tag{WT.14}
$$
This bounds the whole raw response residual. No mean-completed surrogate or its summary is used.

Differentiating (WT.5) in this same norm gives
$$
 \|A_{\rm raw}h\|_{A^0_\Sigma}
       \le C_1\|h_\phi\|_{A^0_\Sigma}+C_0\|h\|_{A^0_\Sigma},
$$
$$
 C_1=BM^2/4+GM,\qquad
 C_0=b+3BM^2+BMP/2+GP.
 \tag{WT.15}
$$
The last term pays $\gamma\langle h_2\rangle J(K)Q_\phi$.
These are the same algebraic terms as R.12, proved here by Wiener multiplication and (WT.3), rather than by changing an $L^2$ norm label.

Since $\mathcal F_\nu=0$ on this first body cell and $b\le B$,
$$
 \boxed{R_Z^\#=(169B+6G)\,19+(49B/4+7G)\,83+R_*}
 \tag{WT.16}
$$
bounds $\|(Z_{\rm raw})_r(0+)\|_{A^0_\Sigma}$.

Both exact canonical repairs are angular polynomials constant on each original radial piece:
$$
 Q_0=Q_{\rm raw}+e_Q,\qquad Z=Z_{\rm raw}+e_Z.
 \tag{WT.17}
$$
Their right radial derivatives at the waist are unchanged. The state and angular repair fees have already entered (WT.4); the right derivative of a piece constant is zero. Thus no new $384E_Z$ residual fee occurs in this derivative readout. All means and the full original angular supports remain.

Define
$$
 M_\delta=7+19d,\quad P_\delta=6+83d,\quad
 R_\delta=R_Q+dR_Z^\# .
 \tag{WT.18}
$$
Then the same selected state satisfies
$$
 \|Q_\delta(0)\|_{A^0_\Sigma}\le M_\delta,\quad
 \|(Q_\delta)_\phi(0)\|_{A^0_\Sigma}\le P_\delta,\quad
 \|(Q_\delta)_r(0+)\|_{A^0_\Sigma}\le R_\delta.
 \tag{WT.19}
$$
Each component is bounded by the displayed pair bound. This is a deliberately wide complete readout, not a fabricated small componentwise derivative certificate.

## 4. The actual waist mean, curvature and speed

Copy the entire SP object
`complete_endpoint_readout_conclusion.waist_complete_radial_factors`.
It contains `complete_absolute_mean_lower`, `complete_absolute_mean_upper`,
`q_lower`, `q_upper`, both density factors, both physical-radius bounds and
`mean_state_repair_and_full_response_fee`.
These are the true $r=0$ fields at the radius (WT.1), not the P.22 fields.
Write their complete qualification as
$$
 0<m_-\le|m_\delta(0)|\le m_+,\quad m_\delta(0)<0,\qquad
 0<q_-\le q(0)=\sqrt{-K(0)}\le q_+.
 \tag{WT.20}
$$
The sign is part of the same SP proof and source identity. Its complete repair fee is copied rather than charged again.

From the body's `intrinsic_whole_third_jets` read
`gamma`, `gamma1`, `beta`, `beta1`, `K`, `K1`, `K2`.
Their suffixes denote ordinary radial derivatives, not factorial-scaled Taylor coefficients. Require a positive directed $\gamma_-$ and use
$$
 \gamma_+\ge|\gamma|,\quad \gamma_1\ge|\gamma_r|,\quad
 b_1\ge|\beta_r|,\quad K_1\ge|K_r|,\quad K_2\ge|K_{rr}|.
$$
For $\eta=-\gamma m_\delta$ set
$$
 \eta_-=\gamma_-m_-,\qquad \eta_+=\gamma_+m_+,\qquad
 e_1=\gamma_1m_++\gamma_+R_\delta .
 \tag{WT.21}
$$
These give $0<\eta_-\le\eta\le\eta_+$ and $|\eta_r|\le e_1$.
In particular the $\gamma m_r$ term is present, since
$|m_r|\le\|(v_\delta)_r\|_{A^0}\le R_\delta$.

A complete admissible input to the TN formulas at the waist is
$$
 U_0=V_0=M_\delta,\quad U_1=V_1=P_\delta,\quad
 U_{r,0}=V_{r,0}=R_\delta,\quad
 D_0=BM_\delta^2/4,\quad D_1=BM_\delta^2.
 \tag{WT.22}
$$
The last bound uses
$(d_Q)_\phi=-\beta P_{\ne0}(u^2+Kv^2)$ and Fourier projection contractivity in $A^0$.
It is not a bare uniform-norm estimate with an omitted projection factor.

The old whole closed-row intrinsic bounds may be wider than point evaluation, but contain the same right trace. No old enclosure is regenerated at a new sample point.

## 5. New waist normalizer fees

Use the exact TN.4--TN.5 definitions at $0$:
$$
 r_\sigma=u+\sigma qv,\quad c_\sigma=d_Q+\sigma\eta q,\quad
 B_\sigma=-q_r/(2q)-\beta(1+r_\sigma^2),\quad
 S_{\sigma,-\sigma}=-\sigma B_\sigma/(2\eta q),
$$
$$
 E_\sigma=-(B_\sigma)_\phi-\beta(r_\sigma)_\phi r_\sigma
 +c_\sigma(S_{\sigma,-\sigma})_\phi
 -(S_{\sigma,-\sigma})_r+S_{\sigma,-\sigma}(d_Q)_\phi,\quad
 (S_2)_{\sigma,-\sigma}=-\sigma E_\sigma/(2\eta q).
 \tag{WT.23}
$$
Their diagonals vanish. Only the exact common-residual cancellation in these off-diagonal identities is used; the full residual and means stay in the evolution.

Form
$$
 \begin{gathered}
 q_1=K_1/(2q_-),\qquad q_2=K_2/(2q_-)+K_1^2/(4q_-^3),\\
 W_0=U_0+q_+V_0,\quad W_\phi=U_1+q_+V_1,\quad
 W_r=U_{r,0}+q_+V_{r,0}+q_1V_0,\\
 a_-=\eta_-q_-,\quad a_+=\eta_+q_+,\quad a_1=e_1q_++\eta_+q_1 .
 \end{gathered}\tag{WT.24}
$$
Then
$$
 \begin{split}
 B_*&=q_1/(2q_-)+b(1+W_0^2),&
 B_{\phi,*}&=2bW_0W_\phi,\\
 B_{r,*}&=q_2/(2q_-)+q_1^2/(2q_-^2)+b_1(1+W_0^2)+2bW_0W_r,\\
 S_*&=B_* /(2a_-),&
 S_{\phi,*}&=B_{\phi,*}/(2a_-),\\
 S_{r,*}&=B_{r,*}/(2a_-)+B_*a_1/(2a_-^2),\\
 E_*&=B_{\phi,*}+bW_\phi W_0+(D_0+a_+)S_{\phi,*}+S_{r,*}+S_*D_1,\\
 S_{2,*}&=E_* /(2a_-).
 \end{split}\tag{WT.25}
$$
These are newly computed waist fees. Existing P.22 fees are not assigned to $r=0$.

The selected state, its repairs and its right radial derivative have label degree at most 96. Thus $S$ has complete degree at most 192 and $S_2$ at most 384, including their constant coefficients. The Euclidean norm of an off-diagonal two-by-two matrix is the maximum magnitude of its two entries, so these matrix bounds require no additional component factor.

## 6. Two fixed tests and the same inverse on two windows

Let $P_J$ project onto $|j|\ge J$ and put
$$
 A_J=P_JSIP_J,\quad B_J=P_JS_2I^2P_J,\quad
 T_J=(1+A_J)(1+B_J),\quad
 \mathcal N_J=(1+B_J)^{-1}(1+A_J)^{-1}.
 \tag{WT.26}
$$
These are the ordered compressed operators of TN.12, extended by the identity on the finite complement and the two independent adjoined means. This is the $T_J(0)$ used in the actual-trial convention. The uncompressed two-factor operator remains separate, with its complete finite correction retained.

For $t=0,-4/3$ set
$$
 m_{S,0}=S_*,\quad m_{2,0}=S_{2,*},\qquad
 m_{S,t}=(1+192/J)^{|t|}\sqrt{385}\,S_*,\quad
 m_{2,t}=(1+384/J)^{|t|}\sqrt{769}\,S_{2,*}\quad(t\ne0),
$$
$$
 \tau_{1,t}=m_{S,t}/(4J),\qquad \tau_{2,t}=m_{2,t}/(4J)^2.
 \tag{WT.27}
$$
Report all four strict comparisons for each of
$$
 J=97,\qquad J=268435456.
 \tag{WT.28}
$$
Only passing tests permit the same inverse's bounds
$$
 K_t=[(1-\tau_{1,t})(1-\tau_{2,t})]^{-1}.
 \tag{WT.29}
$$
The common-inverse argument is exactly the distributional uniqueness proof of TN.12--TN.16. A failed fixed-$J$ test gives no inverse at that $J$.

Also record the first dyadic integer satisfying the complete directed comparisons
$$
 J\ge384,\quad J\ge97,\quad
 J\ge4\sqrt{385}\,S_*,\quad J^2\ge4\sqrt{769}\,S_{2,*}.
 \tag{WT.30}
$$
Its four tests are evaluated separately. It neither overwrites a failed fixed test nor extends the original finite193 inverse to the larger finite complement.

At every accepted $J$, TN.19--TN.20 give the complete inverse and forward strong-remainder fees using the new waist constants. If the first symbol is written without compression, retain
$$
 F_S=SI-P_JSIP_J
 \tag{WT.31}
$$
with all input/output modes through $J+191$ and its full mean output. The full two-factor difference retains its complete support through $J+575$, together with the radial/evolution finite terms used by the actual-trial theorem. These finite operators are not set to zero.

This is a single waist trace conclusion. It provides neither an interval normalizer inverse nor a finite Schur inverse. A true-phase conjugation still needs its own full input/output coordinate norms and transformed projector.

## 7. Exact fields and minimum restoration

| Object | Exact saved field | New use |
|---|---|---|
| D execution | `actual_scientific_receipt.verified_global_state_bounds` and the raw-plus-repair gate | Four fixed state bounds (WT.4) |
| SP execution | `actual_scientific_receipt.complete_endpoint_readout_conclusion.waist_complete_radial_factors` | Full true-waist mean, $q$, radius and density factors, copied unchanged |
| Body sole `rows[0]` | `common_row`, `interval`, `actual_original_scalar_germ`, `intrinsic_whole_third_jets` | First-row and ordinary intrinsic-jet qualification |
| Same body row | `uncorrected_response_nonmean.A0_sup`, `response_mean_residual` | Complete raw response residual |
| Raw container `rows[0]` | `index`, `interval`, `candidate_piece`, `actual_scalar_germ`, `exact_angular_support_index` | First background-row qualification |
| Same raw row | `complete_residual_A0.U`, `complete_residual_A0.V` | Normalized residuals; $\alpha$ once |

The sole body file is
`notes/2026-11-14-R133-correlated-body-row0000-native.json.gz`,
at commit 7c130fb94528de8f003a43e7049fb42768a64eec:
8201 bytes, SHA256
feb3bbf9294dc995b88f5dc7c1e2ba866d3bd8c22dc84834dda7591cc9f644f0.
Its selected range is exactly `[0,1]`; the same bytes and range appear in the successful SP receipt.
Check `selected_cells_complete`, not the false global-completion condition inappropriate to a one-row natural part.

The background container is restored from the three original byte parts in
`notes/2026-11-14-R133-final-complete-moving-residual-parts.json`.
The restored compressed container has 4592623 bytes and SHA256
6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1.
The complete gzip byte stream must be restored before reading row0; one byte part is not one mathematical row.

The consumer checks the original 7296-row identity, exact candidate, amplitude, $\nu_0$, parameter width and complete partition/interface qualification. Only the saved row0 residual values enter new arithmetic. It does not recompute any old whole integral, CR restriction, residual, coefficient, primitive or interface.

The initial consumer does not restore the five-part strict native. If a fixed-cutoff test fails, that different saved waist row is a possible later sharper input, with this first result retained.

## 8. Immutable primary identities

All paths in the following table are relative to `topics/visible-flex-exact-nearby/`. Every listed text has been read under the stated identity; binaries are restored only in the public runner.

| Role / path | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| d_execution: `notes/selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json` | ce7af74c8b2f8cf7715775f352d2c26afb03413a | 40659 | 6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071 |
| sp_execution: `notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json` | 9998526894560d41523454334a444f062fe371a4 | 35259 | a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12 |
| body_manifest: `notes/2026-11-14-R133-body-CI-pinned-inputs.json` | b4a96180d2e1abca2ae90e7ba363e6a0c78149d9 | 31806 | c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784 |
| sp_manifest: `notes/2026-11-15-R133-primitive-mean-strict-propagation-CI-inputs.json` | 92a5282f198dfa05ee8ce1e7b4aaec532485a324 | 21754 | c77e969bd02ef95d30f16b53ae0a0d3854f596412151e9242ffa0485bd142210 |
| raw_manifest: `notes/2026-11-14-R133-final-complete-moving-residual-parts.json` | 413240311cf39cb0eacbd3f473525b7b59a51928 | 1814 | 0705cb80101f25105d74181aafdf9daaf5a65baeece2d41e8a25b4589259cdad |
| D_source: `scripts/fourfold_codazzi_selected_parameter_core_scalar_fees.py` | 704b1e1d4aa74e97c866c725a2524c1b8624039e | 25571 | 827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320 |
| complete_residual_identity: `results/R133-supplement-selected-centre-complete-residual-and-collar-source-bounds.md` | 4cd540b5da2e5f2de3aff44a52fc003ab26d5ae5 | 14153 | 575bd371c09d0b82a975b0c80082f652b82468c90d56d0e730da5e98602d6861 |
| exact_centre_repair: `results/R133-supplement-exact-continuous-repair-of-final-centre.md` | 7338254acdfdab61bd22124d964a4231791b9f7f | 11484 | a39fcfa2b7ca6f83cd9fadcc1987afe86f3364830848de78d2401469d7ce9f44 |
| response_repair: `results/R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md` | 2bc958ab42db0c4936a717e54ff3b43f5001bdf5 | 8753 | 2b7d6080dc7fdac0bd5c557b71f3e7ec1eb5436a14d45a5a762e1b548a9e20f1 |
| body_producer: `scripts/fourfold_codazzi_correlated_head_residual_rows.py` | 3af195a36ccb30630dbfcab0caef3564738ab169 | 13043 | 1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07 |
| body_operator: `scripts/fourfold_codazzi_nu_full_adjoint_kernel.py` | 10d587dbfd548f6940607b3215c493e800badd84 | 13638 | 09807e405455b58c043a5ff26b7ff5e4e1569a96c81ecd860125552bfba95a3b |
| fourier_norms: `scripts/fourfold_codazzi_correlated_radial_Fourier.py` | fcad3e31360289406466cc58fa105bb9fed19e1f | 10940 | 18de4ef746eed069a9a92ba783d54e2f394887866d60cbb286502b9c55cb17c5 |
| raw_producer: `scripts/fourfold_codazzi_moving_residual_checkpointed.py` | ceb34c84cf885a8a2c1d10fb8e42125b45376019 | 12188 | 98eb7034038d76a341e112927cff4bcb7bfd425bc56698305803a689060ac31e |
| raw_helper: `scripts/fourfold_codazzi_moving_continuous_residual.py` | c4df5ed00ffa55bd2f94ecbc3c5752aad99bd5a0 | 5482 | b8e78adda5b029572597e0875ed871da5f03b51951e22e6860fb722b33e1bf51 |
| raw_merger: `scripts/fourfold_codazzi_merge_complete_moving_residual.py` | 10ad6291c67dd7c2c3e153038b454b8211f11ca8 | 11093 | 24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f |
| radial_identity: `results/R133-supplement-polynomial-Codazzi-chart-and-complete-boundary.md` | 1b73111e5cf90876f1e593274b27cb1074915b85 | 11606 | 43ee65f22d64aed7d4f156647d0043e7626f2669b31c784a16c72169e6af8e35 |
| TN: `results/R133-supplement-strict-cut-two-window-normalizers-and-complete-strong-remainders.md` | 401edaeaf8d64f32e51af6faef7c34cb0172f35a | 18847 | 0ffa3261e3bb3fdea2cd05afd489b2e71b5587a2bba9432410c492e2ee64f2aa |
| SP_source: `scripts/fourfold_codazzi_primitive_mean_strict_propagation.py` | f12d3a63f01d8b9bc20c329c67a6582b626eae1d | 44298 | 9d6ef721338e47e2cae8d179ce84976881df91762050d2a77d83b5399f6ba69a |

The original body identity additionally locks intrinsic object
91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848,
the complete raw proposal, all original dependency hashes and the original $10^{-9}$ enclosure half-width. Those original enclosures are restricted to the declared fixed $\eta_0$; no new target values are generated.

The raw helper forms the full drift before any output truncation and retains all residual modes through label 96. The response row retains its complete output through label 160 and the separate true mean. The new endpoint estimates use the full residual norms, without deleting any finite mode.

## 9. Public execution and failure semantics

The new scalar arithmetic runs only in public Actions at the pinned runtime. It records all restored byte identities, both exact first-row intervals and scalar germs, the copied full SP factors, the two background residuals and the complete response nonmean/mean species, all bounds (WT.10)--(WT.25), and the four tests at each candidate cutoff.

Structural completion and strict inverse tests are separate. A nonpassing fixed-cutoff test is a complete scientific result, with all its data retained. Only a directed positive denominator permits an inverse or strong-remainder division. An identity, row/germ, sign, finite-value or source-unit failure stops with the actual diagnostic and completed prefix preserved.

The source neither imports nor executes an old producer. No old Fourier enclosure, target primitive, scalar mean flow, response proposal, global integral, CR restriction, QR, Gram or Green computation is rerun. Restored binaries and new intermediate arrays remain temporary; new artifact and Release counts are zero. The complete small conclusion is saved and printed with its bytes and SHA256 before publication formatting. Topic capacity and the 120KB reserve remain hard gates.

The resulting waist coefficient bounds and same-operator inverse gates can be combined with separately completed waist coordinate costs. They do not establish an unknown state, an incoming inverse, a finite Schur inverse, a nonlinear domain-entry gate or geometric closure.
