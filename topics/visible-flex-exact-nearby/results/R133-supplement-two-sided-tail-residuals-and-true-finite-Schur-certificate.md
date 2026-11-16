# R133 supplement: two-sided tail residuals and a true finite Schur certificate

2026-11-16, newton_source.

**New analytic certificate and a capped implementation contract; no numerical evaluation.** Once a true WPT/WPTV/WPTVR tail inverse has been certified, the actual finite Schur matrix can be certified without replacing it by the matrix of a centre or by a finite section of an unsigned bound. A primal tail trial and a dual tail trial give a product of their complete residuals. This product, together with a finite signed pairing, controls the entire inverse defect.

The construction retains all four original blocks and both right-side rows. The193-dimensional raw head contains its physical even mean. The97 root-complement coordinates and96 actual outer-chart coordinates are separate. The prescribed96 root-even data remain genuine physical data. Any additional Theta, nu, WFR/WCF, amplitude, mean, cokernel or independently supplied functional port keeps its original row, column and norm.

No passed tail gate is asserted here. The old WHVA N4096 comparison is false. WPTV run43854566735/1 passed its complete readonly admission, saved the completed collar parent0 and its five running maxima, and then failed at the finite-display parser before a body reference or body intersection was saved. That complete failed prefix is retained; it supplies no whole tail gate. The conditional inverse below requires a completed, correctly bound tail certificate for exactly the chosen mesh and coordinate maps.

## WDS1. The actual four blocks

Fix the selected member, the ordinary-r positive interval, and one admitted WPT mesh. Let S be its actual piecewise-constant head coordinate map, P=E E^* its normalized cell-constant projection, and Q=Id-P. The complete zero-IVP equations are WPT.29:
$$
 F_0a=\mathscr B y+f_0,\qquad
 \mathscr C a+\mathscr D y=g_0 .
 \tag{WDS.1}
$$
Write F=S F_0S^{-1}, B_0=S\mathscr B, C_0=\mathscr C S^{-1}, and f=S f_0. This notation does not commute S past a Volterra integral. Write Sa=Eu+z, z in QH.

For the prescribed-root96 positive problem alone, y=(d,b) has dimensions97+96; b is the original outer y_L in H^{-5/6}, not a raw endpoint vector. In its inherited Hilbert coordinates define
$$
 \begin{split}
 A&=\begin{pmatrix}E^*FE&-E^*B_0\\ C_0E&\mathscr D\end{pmatrix},
 &B&=\binom{E^*FQ}{C_0Q},\\
 C&=(QFE,\,-QB_0),&R&=QFQ .
 \end{split}
 \tag{WDS.2}
$$
Then the complete operator and right side are
$$
 \mathcal A=\begin{pmatrix}A&B\\C&R\end{pmatrix},
 \qquad
 \mathcal A\binom{x}{z}=\binom{f_f}{g_t},
 \quad x=(u,y),\quad f_f=(E^*f,g_0),\quad g_t=Qf .
 \tag{WDS.3}
$$
Thus X_f and Y_f have the same real dimension193N+193; the tail spaces X_t,Y_t are QH. The four-block Schur complement of (WDS.2) is exactly WPT.31, including its signs.

If a finite completion or ramp equation is used, include its coordinates in X_f,Y_f and all its cross terms in (WDS.2). If an independent unknown function remains in y, this is still an operator system: the finite-square theorem below applies only after that function is kept as a prescribed parameter or is separately retained in an operator block. Declaring its values to be finite coordinates does not close it.

Assume an actual admitted tail certificate proves a two-sided inverse
$$
 R^{-1}:Y_t\longrightarrow X_t,\qquad
 \|R^{-1}\|\le\kappa .
 \tag{WDS.4}
$$
The certificate must bind the same selected member, mesh, S, projection, complete high feedback and any ramp augmentation. In particular the inverse record for one inherited refinement cannot be used with the finite blocks of another refinement.

## WDS2. A product residual for the true Schur matrix

Let Q_f:Y_f to X_f be a genuinely bounded finite trial inverse. Let
Z:X_f to X_t and Y:X_f to Y_t be complete finite-rank tail trials. All adjoints below use the actual Hilbert norms: normalized real sine/cosine modes, cell lengths, the H^{-5/6} outer-coordinate weights, and mean weight1. They are not unweighted transposes of arrays in another basis.

Define
$$
 \begin{split}
 M&=A-BR^{-1}C,\\
 T&=C-RZ,\qquad
 D=B^*Q_f^*-R^*Y,\\
 E_0&=Id-Q_fA+Q_fBZ+Y^*T .
 \end{split}
 \tag{WDS.5}
$$
These are complete maps: T:X_f to Y_t, D:X_f to X_t, and E_0:X_f to X_f. In particular D is not just the interior differential residual of a high adjoint trial.

The exact identity is
$$
 \boxed{\quad Id-Q_fM=E_0+D^*R^{-1}T .\quad}
 \tag{WDS.6}
$$
Indeed D^*=Q_fB-Y^*R, so
$$
 D^*R^{-1}T
 =Q_fBR^{-1}C-Q_fBZ-Y^*C+Y^*RZ.
$$
Adding E_0 cancels the last three terms in their stated order. No coefficient, primitive, projection or boundary map is commuted.

There is also a useful signed-pairing form:
$$
 E_0=Id-\binom{Q_f^*}{-Y}^{\!*}
                 \mathcal A\binom{Id}{-Z}.
 \tag{WDS.7}
$$
It evaluates the small residual as a full Petrov pairing, before taking absolute values. It is not an instruction to subtract unrelated positive bounds.

Suppose complete outward records give
$$
 \|E_0\|\le e,\quad \|D\|\le d,\quad \|T\|\le t,\quad
 \|Q_f\|\le q,\qquad \delta=e+\kappa d t<1 .
 \tag{WDS.8}
$$
Then M has a true two-sided finite inverse and
$$
 \boxed{\quad \|M^{-1}\|\le q/(1-\delta).\quad}
 \tag{WDS.9}
$$
Neumann inversion gives an inverse of Q_fM on X_f. The finite spaces have the same dimension, so M is injective and onto; its inverse is (Q_fM)^{-1}Q_f. No prior value of the positive-head kernel dimension m_H is required. The actual cokernel is removed only by this strict complete gate, not by the existence of a trial Q_f.

Both residuals matter. Replacing d or t by zero because one trial solves only a principal equation is invalid. Conversely a good dual trial can reduce the cost of a moderate primal residual through the product in (WDS.8), rather than paying the entire norm of B times that primal residual.

## WDS3. Both right-side rows and actual reconstruction

Let z_g be any admissible trial for the actual tail right side g_t, and set r_g=g_t-Rz_g. Then
$$
 \begin{split}
 Q_f(f_f-BR^{-1}g_t)
 &=Q_f(f_f-Bz_g)-Y^*r_g-D^*R^{-1}r_g,\\
 h_{\rm app}&=Q_f(f_f-Bz_g)-Y^*r_g .
 \end{split}
 \tag{WDS.10}
$$
This uses Q_fB=D^*+Y^*R. The complete error in this right-side evaluation is at most d kappa ||r_g||. Under (WDS.8),
$$
 \begin{split}
 \|x\|&\le
 \frac{\|h_{\rm app}\|+d\kappa\|r_g\|}{1-\delta},\\
 \|x-h_{\rm app}\|&\le
 \frac{\delta\|h_{\rm app}\|+d\kappa\|r_g\|}{1-\delta},\\
 z&=z_g-Zx+R^{-1}(r_g-Tx).
 \end{split}
 \tag{WDS.11}
$$
Thus the last tail correction has norm at most kappa(||r_g||+t||x||). The formulas apply to an entire bounded family of right sides by replacing vector norms with the appropriate operator norms.

They retain the two original rows, not only the head equation. Prescribed root c contributes its genuine pair (B_{c,0}c,-E_cc) before the S/projection conversion. Rough high input, nu, affine exterior functions, low jumps, independent mean data and every other input use their full WOB.31/WPT.31 right sides. A source or jump cannot be moved from one row to the other without the exact corresponding transformation.

The recovered raw head is a=S^{-1}(Eu+z). Its actual high state is the original given-head graph with this a and the same b and independent data. The raw endpoint is recovered by the bounded zero-IVP endpoint row. No trace of an arbitrary intermediate L2 head is taken.

A successful certificate for this prescribed-root problem supplies the true96 normalized positive columns by applying the full inverse to the genuine c inputs. It does not by itself pay their later waist pairings, the negative radial head, the metric Schur, or the full physical square.

## WDS4. Whole finite residual enclosures without a public matrix array

For a declared partition of an orthonormal basis of X_f, let I_alpha be the complete input-panel embeddings. If
$$
 \|E_0I_\alpha\|\le e_\alpha,\qquad
 \|DI_\alpha\|\le d_\alpha,\qquad
 \|TI_\alpha\|\le t_\alpha,
$$
then
$$
 e=\Big(\sum_\alpha e_\alpha^2\Big)^{1/2},\quad
 d=\Big(\sum_\alpha d_\alpha^2\Big)^{1/2},\quad
 t=\Big(\sum_\alpha t_\alpha^2\Big)^{1/2}
 \tag{WDS.12}
$$
are valid whole-operator bounds. For example, sum the panel outputs and apply Cauchy--Schwarz to the input norms. No orthogonality of the outputs is assumed. Every finite input coordinate, including the mean and b weights, appears once.

Within a finite pairing panel, form the complete signed interval sum for each required entry before taking its absolute upper endpoint. Its full Frobenius bound is sufficient; a complete row/column Schur bound is also legitimate if its entire sums are certified. A finite sampled collection of tail inputs is never a substitute for d or t.

An evaluator may enclose a whole panel as a signed approximate result plus a complete operator error:
$$
 \|E_0I_\alpha\|\le\|\widehat E_\alpha\|+\epsilon_\alpha .
 \tag{WDS.13}
$$
The error includes all high-solution, coefficient, integration, chart and rounding errors in that panel. Entrywise choices from different trial operators are forbidden. Any comparison between alternatives compares complete triples (e,d,t) for the same fully specified Q_f,Z,Y and actual R, or compares their final complete delta records.

The small public conclusion need retain only the complete residual norms, their finally saved interval records, full scope, exact candidate identities, a complete coverage digest, and the last fully completed input-prefix index. Running sums and the current incomplete panel prefix must be preserved on failure. Temporary signed matrices, coefficient arrays and trial-state arrays are not new public artifacts. Their definition is the frozen exact circuit and its immutable input data; no omitted array is asserted to be an already certified operator.

## WDS5. A signed forward application from the original seven-port theorem

The original high problem is unchanged. Its ordinary source is in L2(dr;H^{-2/3}), and its raw high state is in L2(dr;H^{-1}). The seven input slots are exactly
$$
       (s,F_c,F_b,B,J_c,J_s,J_u).
 \tag{WDS.14}
$$
Use the complete saved receiver rows c,y,u from NEG. A new high trial v_hat for a declared head/outer input supplies its actual ordinary residual, all true jumps, stable-root mismatch and complete regular-exterior mismatch in these original units. For their complete nonnegative norm vector alpha, the correction satisfies
$$
 \|v-v_{\rm hat}\|_{\mathscr V}\le {\bf c}\cdot\alpha,\quad
 \|y_R-y_{R,\rm hat}\|_{H^{-5/6}}\le4{\bf y}\cdot\alpha,\quad
 \|s_u-s_{u,\rm hat}\|\le{\bf u}\cdot\alpha .
 \tag{WDS.15}
$$
The ordinary residual uses the actual signed operator, not the centre equation. The impulse terms have no radial length factor. The independent exterior height and mean are included through the original complete B input; b is not counted again as an unrelated affine source.

The true coupling shell gives the complete head forcing error
$$
 \|B_{LH}(v-v_{\rm hat})\|_{\mathscr H}
                  \le1153L_*\,{\bf c}\cdot\alpha .
 \tag{WDS.16}
$$
The original factor1153 is applied only after the true97..288 shell restriction. It does not make the high trial or its correction bandlimited.

For example, a head equation evaluated with v_hat instead of v has high-solution error at most
$$
 \|S\|\,C_{V0}\,1153L_*\,{\bf c}\cdot\alpha .
 \tag{WDS.17}
$$
Its full raw endpoint row has corresponding error at most
$$
 C_{R0}\,1153L_*\,{\bf c}\cdot\alpha
       +K_{RH}\,4{\bf y}\cdot\alpha .
 \tag{WDS.18}
$$
Here C_V0,C_R0,L_* are already saved WHVA records and K_RH is the already completed WOBSA high-outer-row record. These formulas add the actual Volterra and boundary-observation errors once each. All additional direct terms are evaluated in the same full row; (WDS.17) is not the entire error of a panel unless those terms have also been enclosed.

A polynomial trial may be chosen continuous across every artificial subdivision and identically zero near r_* to make its stable-root defect exactly zero for a zero-stable column. That is a construction of the trial, not a property assigned to the true solution. The remaining collar source, actual outer residual and genuine jumps are still paid. If a nonzero root trial is used, its complete stable coordinate must be evaluated through the actual root chart.

Likewise a zero high endpoint can avoid guessing signed coefficients of an exterior graph, at the cost of the full resulting exterior residual. A sharper nonzero endpoint needs the actual signed chart or a reference chart with a complete norm enclosure of its difference. The old graph norm alone is not a signed chart value.

For a panel of input data, every statement in (WDS.15)--(WDS.18) is made in operator norm on that whole panel. This certifies T and the high-dependent part of the signed pairing (WDS.7). It is a new application of a frozen receiver to a new residual, not a repeated Green, Riccati or original-source calculation.

## WDS6. A full dual certificate using a Green identity, not a new adjoint inverse

The exact dual residual can be read directly from the complete operator:
$$
       D=\operatorname{pr}_{X_t}\mathcal A^*
                            \binom{Q_f^*}{-Y}.
 \tag{WDS.19}
$$
First expand this entire adjoint expression. Keep its identity, head, Volterra, finite endpoint, mean, ramp and chart terms. Only after that expansion may its high-state-dependent functional be treated by the following device.

Let v be a genuine high state and write its differential operator as
L_H v=v_r-A_HH v on each original ordinary-r piece. For a smooth finite-angular dual trial w, the exact piecewise Green identity is
$$
 \sum_i\int_{I_i}\langle w,L_Hv\rangle\,dr
 =\sum_i[\langle w,v\rangle]_{\partial I_i}
  -\sum_i\int_{I_i}\langle w_r+A_{HH}^*w,v\rangle\,dr .
 \tag{WDS.20}
$$
Every one-sided boundary term is included. The pairing is the distributional angular pairing. In particular L2 H^1 is the dual of the raw L2 H^{-1} state; L2 H^{2/3} pairs with the ordinary H^{-2/3} source. No unrecorded Riesz conversion identifies these with the same Hilbert-space adjoint.

For a complete high observation
ell(v)=integral <xi,v> plus its actual boundary/mean/trace functional, subtraction gives
$$
 \ell(v)-\sum_i\int_{I_i}\langle w,L_Hv\rangle\,dr
 =
 \sum_i\int_{I_i}\langle\xi+w_r+A_{HH}^*w,v\rangle\,dr
 +\ell_\partial(v)-\sum_i[\langle w,v\rangle]_{\partial I_i}.
 \tag{WDS.21}
$$
For v=P_a a, the ordinary equation is L_Hv=B_HL a. The second term on the left is therefore the explicit signed head functional obtained from B_HL^*w. It involves a finite-angular coefficient contraction and no high inverse.

The right side is bounded by the full body/trace receivers for P_a. Its body residual is measured in L2 H^1, and each boundary residual in the dual of its actual root/outer/jump output. WOBSA has already completed the outer and root columns; WHVA supplies C_P. This gives a bound for every head input a, not merely for a tested set of head functions.

For example, if the complete remaining functional has only a body term of norm r_v and an outer H^{-5/6} term of dual norm r_R, then its norm after P_a S^{-1} is at most
$$
             \|S^{-1}\|\{C_P r_v+Y_a r_R\}.
 \tag{WDS.22}
$$
If root or interface observations occur, add their full qualified terms. This two-term display does not authorize dropping them. The factor4 is already included in the saved Y_a, whereas the original raw y receiver in (WDS.15) still needs that factor.

A useful legal trial choice makes w continuous across every original raw identity transmission and zero at both physical endpoints. Then its own Green boundary terms cancel. The boundary/mean observations contained in ell remain in (WDS.21) and are bounded in full; making w vanish does not make ell vanish. If w or the true homogeneous transmission jumps, the complete two-sided terms in (WDS.20) are retained instead.

The direct head terms in (WDS.19), the explicit B_HL^*w term, and the complete error from (WDS.21) together enclose the full column DI_alpha. Merely certifying the high functional is not a certificate of D. Applying (WDS.12) to all finite dual-input panels then proves its operator norm on the entire infinite tail. Thus no new adjoint-inverse bound is required, and no false homogeneous adjoint boundary condition is introduced.

## WDS7. What the signed centre can replace, and what it cannot

The true raw generator is WHR.4:
$$
 \mathcal A_{\rm raw}
 =M_d\partial\,Id+\eta\begin{pmatrix}0&-K\\1&0\end{pmatrix}\partial
 +\begin{pmatrix}M_{L11}&KM_\ell\\M_\ell&M_{L22}\end{pmatrix}
 -2\beta\binom{M_{u_\phi}}{M_{v_\phi}}I(M_u,KM_v)
 +\gamma\binom{Kv_\phi}{-u_\phi}\Pi_2 .
 \tag{WDS.23}
$$
The reference can use the original degree32 real cubic centre, its exact physical alpha, the exact rational nu definition, and the original scalar intrinsic enclosures. Every proposed reference value is separate from the actual coefficient. The complete65 old repair suprema and the full saved degree96 delta enclosures bound their difference. Rebuilding the6143 repair offsets, rerunning4650 row producers or recovering a lost signed matrix from unsigned norms is not part of this contract.

For the delta step at fixed intrinsic beta,K,gamma write a=(u_phi,v_phi)^t, b=(u,Kv), with centre versions a0,b0. The primitive difference is exactly
$$
        aIb-a_0Ib_0=(a-a_0)Ib+a_0I(b-b_0).
 \tag{WDS.24}
$$
All intermediate zero modes of I remain annihilated. Let e0,e1 bound the complete component changes in A0 and angular A0, and U,V,U1,V1 be the saved complete repaired-centre bounds. A valid whole primitive difference is
$$
 P_\Delta=\frac{|\beta|}{2}
 \left[e_1\{U+e_0+|K|(V+e_0)\}
       +(U_1+V_1)(1+|K|)e_0\right].
 \tag{WDS.25}
$$
The1/4 used here is the actual L2 primitive norm. It is not an L-infinity bound. The same completed expression is used for its L2 adjoint norm.

Let dDelta,dphiDelta and laDelta,leDelta,ellDelta be the complete saved delta fees. Let Em bound the saved independent mean variation. Since eta=-gamma Pi v,
$$
 \eta_\Delta\le|\gamma|E_m,\qquad
 M_\Delta\le|\gamma|(1+|K|)e_1 .
 \tag{WDS.26}
$$
For any finite-angular state z,
$$
 \|(\mathcal A_{\rm raw}-\mathcal A_{\rm raw,0})z\|_2
 \le [d_\Delta+\max(1,|K|)\eta_\Delta]\|\partial z\|_2
  +[la_\Delta+le_\Delta+(1+|K|)ell_\Delta+P_\Delta+M_\Delta]\|z\|_2 .
 \tag{WDS.27}
$$
This is a whole perturbation bound. The complete reference-to-centre error, including its signed intrinsic interval differences and all repair offsets, is added separately. An interval minus an exact rational reference is a valid signed difference; subtracting one positive upper bound from another is not.

For the adjoint drift, (M_d partial)^*=-M_d partial-M_dphi. Consequently an adjoint version of (WDS.27) includes dphiDelta in the zero-order bound. The principal eta,K are angle-independent. The primitive and physical mean rank are adjointed in their full stated order. This method does not need radial derivatives of the unknown coefficient perturbation.

If z has finite angular support through J, every raw product in (WDS.23) has support through J+192; the primitive does not enlarge that total shift. On a high-projected source, its L2 error converts to H^{-2/3} using the true first high frequency388. On the finite output of a dual residual, an H^1 bound follows from the full J+192 frequency weight. These weights are applied to the whole reconstructed product, never to one factor before another multiplication.

The physical mean rank is retained in (WDS.27). Its zero in a particular high/cross block may be used only after that block's exact projections prove it. A centre mean input with zero high image does not imply that the full delta mean column is zero.

The existing WPTV19-input restoration closes the positive body coefficient data:13 original native parts,5 original cubic parts and1 original repair container. It does not supply a new signed outer graph or root chart. The latter may be handled by complete reference-chart errors from WOB or must be admitted separately if sharper signed actions are requested.

The first collar can use a zero signed reference and the already complete collar coefficient/source bounds; there is no need to divide by K at the root. Such a coarse reference may fail the final inverse test. Any improved collar signed model must use its true original germ definitions and enclosures; the body cache is not extended into the collar.

## WDS8. A concrete finite implementation with a resource stop

The following is one finite algorithm, not a numerical claim.

1. Admit the exact completed tail record and select its single mesh. For the current WPTV contract the parent/refinement caps are161/322. Do not create another scientific mesh after observing a failed gate. The base finite dimension is193N+193; at the maximum declared refinement it is62339, before any additional legitimate finite variables.
2. Use normalized physical real Fourier coordinates and the actual cell isometry. Build a small exact rational circuit for Q_f, rather than storing a dense62339-square array. One candidate is a mode-by-mode discrete Volterra principal system with one full two-dimensional root/outer boundary completion per nonzero low mode and the independent mean completion. Its reference cell lengths, normalizations, coefficients and p_R are exact rational trial values. Every difference from the actual finite blocks stays in E_0.
3. In unnormalized reference cell values this principal circuit has equations u_i-sum_{j<i} h_j D_j u_j-(h_i/2)D_i u_i-E_dd=r_i, with the full reference endpoint row. Each local2-by-2 pivot and the final2-by-2 boundary pivot is checked as an exact rational pivot. A zero pivot rejects this candidate; it proves nothing about the true operator. Exact diagonal coordinate conversions define its action in the actual finite Hilbert spaces. Their full norms and uncertainty are retained.
4. Applying the circuit and its transpose uses radial recurrences and small angular blocks. The trial may incorporate a declared finite angular correction if its full factorization, inverse action, transpose action and norm enclosure are supplied. No arbitrary sparse subset of the actual193 equations becomes the certificate.
5. Choose primal and dual tail trials in a predeclared finite polynomial space, with exact Q projections. A concrete first class has radial degree at most5 on the admitted cells and signed angular high trials through J=480. These are approximation caps, not truncations of the actual high inverse. Missing high modes are paid by the complete residual theorem. Rational approximations may be generated from the centre only, but their frozen circuit/recipe must define the same trials for every certification panel.
6. Process input panels of at most4 actual orthonormal finite coordinates. Evaluate the complete forward and weak-dual residuals, full finite pairing, all interval integration errors and all coefficient uncertainty on every old coefficient row intersecting a cell. Use complete polynomial/interval enclosures over each closed piece, not nodal samples. Adjacent raw identity transmissions do not erase independent affine jumps.
7. Accumulate the complete sums in (WDS.12) and a genuine q bound for the circuit. No scientific matrix or coefficient array is uploaded. Declare temporary memory and wall-clock caps before execution; reaching one is a retained resource failure, not permission to increase J, degree, N or panel count. The proposed circuit removes a dense-storage requirement; it does not prove the chosen caps will be computationally adequate.
8. Save the complete e,d,t,q records and the finally saved tail kappa, then compute and save the new whole delta. Compare their saved directed endpoints. Only a strict pass permits a new inverse norm record. Preserve a false sufficient gate as a complete result.

A circuit that approximates only the principal operator can be a poor Q_f. The certificate tests it against the full actual operator; it never asserts that the principal circuit is already a good approximation. More accurate trials are permitted only as separately frozen complete candidates with declared caps. Different tail refinements and different Q_f/Z/Y candidates do not share an entrywise minimum.

The statement about rational coordinate conversions in step3 means that the circuit itself is completely specified finite data; all actual cell-length and H^{-5/6} weights still occur in the norm and action verification. It is not a replacement of those true weights by their rational approximations.

## WDS9. Exact readonly inputs and new targets

The body restore inventory is already immutable. An executable child must verify its whole containers, all4650 rows and original interface/mean/affine qualifiers before using any coefficient. In particular original intrinsic records have exactly five fields ball/lower/upper/mid_float/radius_upper_float; the last two are finite display metadata. The original repaired/delta/fee records have three fields. The display numbers are never numerical bounds.

The minimal old mathematical data are as follows. Prefix WOBSA refers to the complete receipt in the evidence table; G means its complete_new_graphs.

| Use | Original typed source/path |
|---|---|
| Whole7-port correction oracle | NEG.response_rows.entire_positive_raw_L2r_Hminus1, NEG.response_rows.body_Y_sup and NEG.response_rows.full_root_outgoing_unstable_Y_port, all seven entries of each complete row |
| Same positive body and source norms | WHVA.copied_original_records and its complete retained scope; original collar/body split and ordinary dr are unchanged |
| Body/head baseline | WHVA.new_records.C_P, C_K, C_V0, C_R0, L_star, A_infty; read completed records, never reevaluate their original recipes |
| Actual head outer and root observations | WOBSA.G.complete_positive_head_and_outer_columns.complete_new_records.complete_head_outer_trace_upper and complete_head_root_unstable_upper |
| Actual b columns | The same graph's complete_outer_b_raw_state_upper, complete_outer_b_outer_trace_upper, complete_outer_b_root_unstable_upper and complete_outer_b_to_head_source_upper |
| Complete high outer row | WOBSA.G.complete_outer_low_and_affine_rows.complete_new_records.complete_high_outer_row_upper |
| Actual low/affine outer rows | That graph's complete_low_outer_row_upper and all complete_affine_* records, with the exact WOB.3/WOB.7 chart identities |
| Whole zero-IVP observations | WOBSA.G.complete_zero_IVP_rows, all five saved records, and their complete no-inverse scope |
| Body signed reference | WPTV inventory's exact original cubic index/five parts, physical alpha/nu, complete intrinsic intervals, exact repair definition and65 suprema |
| Full coefficient difference | Original native inflated_rows[*].complete_delta_bounds, complete_delta_fees and full_delta_A0/full_delta_angular_A0/independent_mean_variation_bound, plus original_complete_repaired_bounds |
| Actual tail inverse | A future completed tail receipt with strict comparison, full inverse record, exact selected mesh/S/refinement identities and preserved false alternatives; no such receipt is manufactured here |
| New trial definitions | One small immutable rational circuit/recipe for Q_f,Z,Y and any right-side trial; fixed basis, projection, physical weights, angular/radial caps and temporary resource caps |

The notation WOBSA.G in the table means WOBSA.complete_new_graphs, not a head inverse named G. The complete WOBSA receipt has18 successful gates and six completed graphs; all37 old targets are frozen. The new finite stage does not calculate them again.

The actual outer identities, including p_R and its full remainder/mean row, are mandatory mathematical inputs. If only their old norm enclosures are used, the signed reference must be explicitly chosen and the whole uncertainty must remain. A missing signed coefficient cannot be inferred from an unsigned bound.

The new scientific targets are: one complete norm of each frozen trial circuit; complete forward-panel residual totals; complete dual-panel residual totals; complete signed finite-pairing error totals; their whole e,d,t values; delta and its comparison; and, conditionally, the true finite inverse norm and the full requested right-side/reconstruction bounds. A current panel is a prefix of these whole targets, not a reason to hide completed work.

Before execution the manifest fixes every input path/hash, full target order, basis coverage, all candidate circuits, caps, output schemas and partial-save rules. No trial matrix, inverse or new quantity is evaluated in this note. All new arithmetic belongs to a separately authorized own-Actions child. Existing successful computations and failed-prefix qualifications remain read-only.

## WDS10. Consequences and remaining obligations

The certificate is useful even with a moderately large kappa because its unresolved tail error is the product d t. It can also fail, for example because the coefficient uncertainty, the chosen principal circuit or the entire boundary observation error is too large. Failure is a complete sufficient-test outcome and does not show singularity.

The method provides a concrete way to certify genuine finite signed actions from the repaired degree32 centre and full existing delta enclosures without recovering signed degree96 shards. It does not promise that those enclosures are narrow enough. If they are not, a sharper signed source is a new declared input/target; it cannot be obtained by subtracting upper bounds.

Every successful positive normalization still leaves the true negative head, independent functional data, full physical means, amplitude/metric rows, Theta constraints, all auxiliary finite factors and their cross pairings in the remaining physical system. Their separate solvability is neither assumed nor concluded by (WDS.9).

## Immutable primary evidence

Paths are relative to topics/visible-flex-exact-nearby/. Every text below was read in full or its indicated complete equations and records were rechecked in full in the current chain; no binary or large report body was fetched.

| Source | Path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| N, complete raw operator | results/R133-supplement-complete-moving-root-scalarization.md | 8a57ec851fc9029e4319650b87360b9867d22a97 |15539|0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af|
| WHR, true head and ports | results/R133-supplement-exact-positive-radial-head-Fredholm-reduction-and-trace-safe-finite-factors.md |0cb48560534119452e71ec1bc6e23df7af245943|28267|289935c35a77f706ce4f9c151ae40c85b67e14743899eaed293747e5704dbad4|
| WPT, all four blocks | results/R133-supplement-cellwise-principal-inverses-and-dual-radial-head-tail.md |b37c59bc05a2131b27014f37c1a6555d6f7e2c58|22954|22fb6fac312540818390bea1bb3a3ed2c750f515ad91bbbb1b0790fcdfe1fd6e|
| WPTV, full value difference | results/R133-supplement-frozen-cross-block-value-enclosures-for-the-positive-head.md |ddccd14e855ba95048fe92cbd21edfb82ebd8e6f|21178|dda500b8f5e2d02a39fbef4efcc5c2ad10dac93eef194f6e8d5b9b5a816cd0e9|
| WPTVR, same inherited tail | results/R133-supplement-five-whole-maxima-and-inherited-positive-head-refinements.md |49cb657d9aefd809857aeac0229124738978a05d|11659|62adc53eedc1ea339e02f6e2a8fa654e38c92fe04784343557e23c84ddd696c2|
| WOB, actual outer/square | results/R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md |8a55c94d8decc25f33876665119b327eb1d1fd29|41683|f13024a72e09d9b388fc51eac39d675b656d4d75ee72cdafe449a1c325e92979|
| WOBSA, whole frozen receivers | notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/actual-scientific-conclusion.json |b21c6d0717bccd6827eff4792bb12b8b1cd40d05|60416|ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79|
| WHVA, false old mesh gate | notes/zero_volterra_positive_head_ci/run-43838214094-1/actual-scientific-conclusion.json |ebe7ae42c2482ce9b20e7af1d41e02f89b920010|12011|ff5d6e5231e6be66107217d670133b18727dd5b24b81e7566fa884973b29df72|
| NEG, complete original graph | notes/full_delta_negative_one_positive_ci/run-43627228225-1-full-real-delta-negative-one-positive-graph/evidence/full-real-delta-negative-one-positive-graph-summary.json |3abd0f6b7291e0f9318dc035a58a4b6e8dfb851c|41797|0a3fb8e1be19b9ad82655099da8d5446ac49d92f073e7f6626d08a0626ec4fef|
| WPTV, completed collar and interrupted body | notes/frozen_cross_block_value_tail_ci/run-43854566735-1/actual-scientific-conclusion.json |e5721a0ecea7c3131401a8caa94839ad10e2e315|15309|b8812b6b940b17532c7643555d3393da71c2190606082862ccf651fbff762274|
| Exact19-input restore closure | notes/2026-11-16-R133-frozen-cross-block-readonly-input-inventory.json |18ec6014b06315aaf24cf9068e6fa31e05e6025a|38086|f7dd2ed019b30c076aa70ad1536601813095ef59bb504049d976eb0cd93b1547|

The evidence table identifies the previously proved ingredients. It does not assert that the future finite signed target or its tail prerequisite has succeeded.
