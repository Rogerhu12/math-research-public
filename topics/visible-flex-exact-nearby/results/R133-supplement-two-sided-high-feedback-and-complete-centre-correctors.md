# R133 supplement: two-sided high-feedback residuals and complete centre correctors

2026-11-16, tail_connector.

**Proved analytic identities and complete candidate boundaries; no new numerical target has been evaluated.** The completed WVC candidate has a false sufficient finite comparison. This note identifies two obstructions in its particular positive budget, then gives a two-sided high-feedback identity that replaces its large whole receiver factor by a genuine dual residual. A centre-only version requires no signed full-degree96 correction array. A separate finite-band residual corrector is also given with its entire enlarged source support.

Neither construction is a numerical success claim. The two candidate constructions are not mixed by taking advantageous entries. Every new candidate must preserve the same actual operator, both original right-side rows, all independent ports, physical means, and a complete finite comparison.

## W2H1. The fixed actual spaces

Use the same selected positive realization as WPT and WVC, on
$$
 I_+=[r_*,25/8],\qquad
 E_L=\{h_1\ {\rm odd},h_2\ {\rm even};\ |j|\le96\},\qquad
 \dim_{\mathbb R}E_L=193 .
 \tag{W2H.1}
$$
The angular measure is normalized, the physical frequency is $4j$, and all radial integrals use ordinary $dr$. The transformed head space is $\mathscr X=L^2(I_+;E_L)$ with the original fixed piecewise $S$ conversion. Let
$$
 \mathscr H=L^2_rH^{-1}_{\phi,H},\qquad
 \mathscr F=L^2_rH^{-2/3}_{\phi,H},\qquad
 G_H:\mathscr F\longrightarrow\mathscr H .
 \tag{W2H.2}
$$
The subscript $H$ denotes the original reflected high space $|j|\ge97$, with its actual odd/even assignments. It does not authorize a different full-complex-circle realization of the physical high inverse.

Here $G_H$ is the original given-head high inverse with every independent stable-root, outer, impulse, affine and other high port set to zero. It is not the coupled physical inverse. On the admitted smooth core write
$$
 L=\partial_r-A_{HH},\qquad LG_H=Id .
 \tag{W2H.3}
$$
The complete collar/body source columns of the original inverse bound the full output:
$$
 \|G_H(r_{\rm col}+r_{\rm body})\|_{\mathscr H}
 \le C_{\rm col}\|r_{\rm col}\|_{\mathscr F}
        +C_{\rm body}\|r_{\rm body}\|_{\mathscr F}.
 \tag{W2H.4}
$$
Their original source intervals and joint two-component qualifications are retained. A body column alone is not a global replacement for (4).

Fix one complete low reference receiver $G_f$ in its actual coordinates. Its output space $\mathscr Z$ includes the transformed low body, all97 root-complement rows, all96 outer rows with their original $H^{-5/6}$ norm, and the complete mean coordinate. Define
$$
 B=B_{HL}S^{-1}:\mathscr X\to\mathscr F,\qquad
 C=G_fB_{LH}:\mathscr H\to\mathscr Z,\qquad
 \mathcal K=CG_HB .
 \tag{W2H.5}
$$
All root and outer atoms of $G_f$ are part of $C$. Its adjoint includes them before any high trial is applied. The actual scalar mean equation, both stored physical density means, $\Theta,\nu$, the prescribed96 physical inputs, radial head, cokernel and external function inputs retain their separate original equations.

If the low reference is changed, for example by WCTR, every occurrence of $G_f,C$, its adjoint, low remainder, reference norm and endpoint receiver below must change together. The actual $G_H$, physical $S$, head/tail projections and operator blocks remain fixed. Write $D_f$ for that current complete low reference: $D_f=D_a$ for WVC and $D_f=rId+D_a$ for WCTR.

## W2H2. Two obstructions in the already completed positive recipe

The following are quoted complete old records, not new evaluations. Their full original objects remain in the WVC actual JSON. The first old receiver object also contains its original lower/upper strings; this table displays its ball field without replacing that object.

| Original object | Exact JSON path | Original ball |
|---|---|---|
| collar receiver C_col | `copied_original_records.C_c` | `[0.109319620282863738374956159433910930938529803492544432340397 +/- 5.55e-62]` |
| complete collar source A_col | `copied_original_records.A_c` | `[0.216176788979021022547123318815010633904539663839870444207842182068403381225 +/- 1.43e-76]` |
| complete high-state error E_H | `complete_new_graphs.complete_high_trial_source.new_records.complete_high_state_error_upper` | `[2.16057243295090215876680878782484962879116266106260649890359036079873829581 +/- 1.25e-75]` |
| complete paired receiver C_pair | `complete_new_graphs.complete_actual_paired_receivers.new_records.complete_actual_paired_LH_upper` | `[290.238585997986741844319700388757294251345202090821800942056407977450991486 +/- 4.06e-73]` |
| complete signed-centre source K_H | `complete_new_graphs.complete_local_signed_remainder.new_records.complete_signed_centre_paired_source_norm_upper` | `[171.249282481397321805656022568111168152751621960434260418175748534263162199 +/- 4.53e-73]` |
| complete finite sufficient comparison | `complete_new_graphs.complete_actual_E_D_T.new_records.complete_actual_finite_defect_upper` | `[11066.2974592482170277255953739045070721096905053507529455902664127679013367 +/- 3.72e-71]` |

The three old intervals give the elementary rational qualifications
$$
 C_{\rm col}>\frac1{10},\qquad
 A_{\rm col}>\frac15,\qquad C_{\rm pair}>256 .
 \tag{W2H.6}
$$
These are comparisons of the already printed intervals with rational constants. No new interval product is evaluated here.

The old nonnegative recipe contains
$$
 E_H=C_{\rm col}A_{\rm col}+C_{\rm body}\alpha_{\rm body},\qquad
 \varepsilon_H\ge C_{\rm pair}E_H .
 \tag{W2H.7}
$$
If that exact recipe and its collar source are retained, even assigning the new body source the best possible value zero leaves the **budget**
$$
 C_{\rm pair}C_{\rm col}A_{\rm col}>
       \frac{128}{25}>1 .
 \tag{W2H.8}
$$
This is a lower bound on that positive upper-bound recipe. It is not a lower bound on the true operator error and gives no evidence of singularity.

There is also an independent obstruction if the old $K_H$ record is simply copied. WVC.42 contains $(1+e_\rho)w_0(K_H+\varepsilon_H)$ inside its complete positive comparison, with $e_\rho\ge0$ and $w_0=6/5$. Its old $K_H>171$ by itself prevents that unchanged positive comparison from being less than1. Improving only the displayed high-state factor cannot be described as a successful whole finite gate.

These facts explain the need for a genuinely different complete feedback estimate and a complete signed-centre comparison. They do not mandate any particular numerical experiment.

## W2H3. A whole high-feedback identity

Let $\widehat V:\mathscr X\to\mathscr H$ be a bounded high trial in the actual homogeneous graph, and define its complete primal residual
$$
 r=L\widehat V-B:\mathscr X\to\mathscr F .
 \tag{W2H.9}
$$
Let $\widehat W:\mathscr Z\to\mathscr F^*$ be a dual trial in the true dual high graph, and set
$$
 d=L^*\widehat W-C^*:\mathscr Z\to\mathscr H^* .
 \tag{W2H.10}
$$
The stars in (10) use the original ordinary-$dr$, angular-$L^2$ distribution pairing:
$$
 \mathscr F^*=L^2_rH^{2/3}_{\phi,H},\qquad
 \mathscr H^*=L^2_rH^1_{\phi,H}.
 \tag{W2H.11}
$$
They are not same-Hilbert adjoints with Bessel Riesz factors omitted. On the complete source and state spaces, the exact identity is
$$
 \boxed{\mathcal K
      =C\widehat V-\widehat W^*r+d^*G_Hr.}
 \tag{W2H.12}
$$

Indeed $G_HB=\widehat V-G_Hr$ follows from (9), uniqueness and the actual homogeneous ports. The full Green identity in (10) gives
$CG_H=\widehat W^*-d^*G_H$. Substitution proves (12), including the plus sign in its last term.

Both identities are first proved on the common smooth core and extend only after the displayed complete operator bounds have been supplied. No derivative of a norm upper or radial derivative of the arbitrary head input is used.

The new signed comparison map is
$$
 \widehat{\mathcal K}=C\widehat V-\widehat W^*r .
 \tag{W2H.13}
$$
Its negative term is an actual operator in the trial definition. It cannot be implemented by subtracting a saved positive bound for $\widehat W^*r$ from a positive bound for $C\widehat V$.

If $\delta\ge\|d\|_{\mathscr Z\to\mathscr H^*}$ and $\rho_{\rm col},\rho_{\rm body}$ bound the two full residual-source pieces, then
$$
 \|\mathcal K-\widehat{\mathcal K}\|
 \le\delta(C_{\rm col}\rho_{\rm col}
                      +C_{\rm body}\rho_{\rm body}).
 \tag{W2H.14}
$$
For exactly the already completed WVC primal trial, its whole saved $E_H$ in (7) is available and the right side may instead be $\delta E_H$. That reuses its same complete error record; it does not rerun its source graph.

If the dual defect is estimated by a collar part and a body part, use their complete whole-domain sum, or a proved joint Hilbert bound. Formula (14) does not discard cross propagation from either source piece to either observation piece. A small body dual residual alone does not remove the collar.

## W2H4. Boundary, transmission and independent-port discipline

The equation $CG_H=\widehat W^*-d^*G_H$ requires the complete Green identity. It is not obtained from the interior adjoint differential equation alone.

A direct safe dual trial can be made compactly supported in the ordinary positive body: multiply the reference inverse on both sides by the original cutoff, which is zero in true neighbourhoods of both endpoints. Use the original raw identity transmission for its reference solution. Then its endpoint pairings vanish and its raw value matches across every original identity interface. Derivative jumps allowed by the piecewise coefficients do not create an omitted value-jump term.

The adjoint must be constructed in the physical pairing. Transformed coordinates involving different piecewise $S_i$ are not reset across interfaces. If a proposed implementation does not establish the required raw matching, its full Green jump rows must be added to (10) and received in the original dual port spaces.

Compact support of $\widehat W$ removes only its own test boundary terms. It does not remove:

- the root and outer atoms already contained in $C^*=B_{LH}^*G_f^*$;
- the actual high outer trace correction and its original receiver;
- the independent outer input $B_{LH}\mathcal P_b b$;
- any physical mean, metric, affine or impulse input.

All those terms remain in the same complete finite operator and right sides. The separate actual high-trace estimate is not inferred merely from the body state norm in (2).

## W2H5. A centre-only signed candidate

No full-degree96 signed array is needed to define a useful version of (12). Let the continuous degree32 repaired centre be exactly the one in WVC, with the full actual $\eta$ in its principal. Write
$$
 \begin{split}
 L_c&=\partial_r-A_{HH,c},&
 B_c&=B_{HL,c}S^{-1},&
 C_c&=G_fB_{LH,c},\\
 \Delta A&=A_{HH}-A_{HH,c},&
 \Delta B&=B-B_c,&
 \Delta C&=C-C_c .
 \end{split}
 \tag{W2H.15}
$$
Here the symbol $C_c$ is a centre operator and is different from the scalar collar receiver $C_{\rm col}$.

Choose a centre-defined primal trial $\widehat V$ and dual trial $\widehat W$. Put
$$
 r_c=L_c\widehat V-B_c,\qquad
 d_c=L_c^*\widehat W-C_c^* .
 \tag{W2H.16}
$$
Their actual residuals are exactly
$$
 r=r_c-\Delta A\,\widehat V-\Delta B,\qquad
 d=d_c-\Delta A^*\widehat W-\Delta C^* .
 \tag{W2H.17}
$$
Define the complete signed centre comparison
$$
 \widehat{\mathcal K}_c=C_c\widehat V-\widehat W^*r_c .
 \tag{W2H.18}
$$
Then (12) becomes
$$
 \boxed{
 \mathcal K-\widehat{\mathcal K}_c
  =\Delta C\,\widehat V
    +\widehat W^*(\Delta A\,\widehat V+\Delta B)
    +d^*G_Hr .}
 \tag{W2H.19}
$$
The signs are fixed by $L=L_c-\Delta A$. Every complete full-degree96 correction, ordered primitive and physical mean rank remains in (17)--(19).

The two family terms in (19) can be bounded by their complete positive operator compositions. They do not require recovering a signed full-degree96 coefficient from an upper bound. A centre-norm difference is not substituted for a true family difference.

The new complete paired head candidate uses the one signed operator
$$
 G_f(A_{L,c}-D_f)S^{-1}+\widehat{\mathcal K}_c
 \tag{W2H.20}
$$
and separately pays the full low-family error $G_f\Delta A_LS^{-1}$ and all of (19). Thus a smaller high-error budget is not combined with the old complete $K_H$ as if the trial had remained unchanged.

There is no assertion that (20) is small. Its full kernel or circuit norm must be bounded as the declared complete map. Any proposed numerical implementation must retain the negative operator in (18) before an admissible final norm comparison, or pay its entire triangle bound.

With the original low reference fixed, (19)--(20) are a different complete decomposition of the same actual paired map $G_f\Gamma$. They need not change its finite preconditioner or its actual trial factors. In that use, a bound for (20) plus its entire remainder bounds that unchanged actual map. If a later implementation also changes a finite trial or reference, its full block definitions and both right sides must instead be rederived together.

## W2H6. An explicit dual trial without coefficient radial derivatives

Let $P_M$ project onto the original reflected high modes97 through $M$, and let $G_{0,M}$ be the complete diagonal principal reference inverse on this finite angular band, with both Green triangles and its original homogeneous reference boundary conditions. All states remain ordinary radial functions.

For the first dual candidate take $M=160$ and set
$$
 \widehat V=\chi G_{0,160}\chi B_c,\qquad
 \widehat W=\chi G_{0,160}^*\chi C_c^* .
 \tag{W2H.21}
$$
The centre cross blocks have high support97 through160, so the projections in this definition are exact for their source inputs. The low receiver's body and atoms are all sent through $C_c^*$ before the dual reference kernel.

Put $E_c=A_{HH,c}-D_H$. Applying
$L_0^*=-\partial_r-D_H^*$ to the entire source of $G_{0,160}^*$ gives
$$
 \begin{split}
 d_c={}&(\chi^2-1)C_c^*
       -[\chi'Id+\chi E_c^*]G_{0,160}^*\chi C_c^*,\\
 d={}&d_c-\chi\Delta A^*G_{0,160}^*\chi C_c^*
                     -\Delta C^* .
 \end{split}
 \tag{W2H.22}
$$
The sign of the cutoff derivative is negative in the first line because the formal adjoint radial derivative is $-\partial_r$. This is the full adjoint analogue of WVC.8.

No radial derivative of $B_{HL,c}$, $B_{LH,c}$, $C_c^*$ or the arbitrary receiver input is required. The inverse identity applies first to its complete source. The adjoints of the angular words retain both multiplier factors, the true intermediate projection in $I$, the identity $I^*=-I$, and every mean row.

For a receiver norm, the complete defect $d$ is measured in $L^2_rH^1_{\phi,H}$. The same finite angular operator has the corresponding full Bessel weight on each output coordinate. It is not measured merely in unweighted $L^2$ and then relabeled.

The centre part of (22) can reach mode224. The complete family term can reach mode352, while $\Delta C^*$ is supported through288. These are support statements for the explicitly constructed defect coefficients. They do not truncate $G_Hr$ or grant a finite-band realization of the unknown actual high state.

The complete forward and reverse kernel bounds may exploit the same exact real Fourier coordinates, actual radial measures and atomic weights as WVC. The reverse must be the transpose of the declared signed or positive comparison kernel; an unrelated envelope routine is not presumed self-adjoint.

## W2H7. A separate complete residual-corrector candidate

This section supplies another possible whole trial, not an entrywise combination with (21). Let
$$
 V_0=\chi G_{0,160}\chi B_c,\qquad
 R_0=L_cV_0-B_c .
 \tag{W2H.23}
$$
Its complete centre residual has output through224. A correction using only modes97 through160 cannot silently remove the161-through224 source.

Choose the larger internal reference $G_{0,224}$ and define
$$
 Q_{224}=\chi G_{0,224}\chi,\qquad
 V_1=V_0-Q_{224}R_0 .
 \tag{W2H.24}
$$
This is a new actual signed trial on the same head input and homogeneous high ports. It does not enlarge the actual angular head96 or the actual radial tail space.

Since $P_{224}R_0=R_0$, its complete centre residual is
$$
 \begin{split}
 R_1&=L_cV_1-B_c=(Id-L_cQ_{224})R_0\\
    &=(1-\chi^2)R_0-\chi'G_{0,224}\chi R_0
                   +\chi E_cG_{0,224}\chi R_0 .
 \end{split}
 \tag{W2H.25}
$$
Every cutoff commutator is retained. On the body where $\chi=1$ and $\chi'=0$, the exact residual is $E_cG_{0,224}R_0$. This is a specific new complete composite; it is not the product of two arbitrary old positive errors.

On a collar where $\chi=0$, $V_0=V_1=0$ and $R_1=R_0=-B_c$. More generally every iteration using a left cutoff zero on that collar has the same uncorrected collar source. This proves the structural warning in W2H2 without a numerical trial.

The full actual residual is
$$
 LV_1-B=R_1-\Delta A\,V_1-\Delta B .
 \tag{W2H.26}
$$
The new trial has angular output through224, its centre residual through288, and its full-family residual through416. The old352 support label is therefore not copied to (26). A complete whole-output family norm may be used if its actual scope covers (26); no projection of the family error is permitted.

Reference modes161 through224 and the whole new norms are genuine new prerequisites. The old successful public scalars, old five maxima, old reference identities and old56 graphs remain immutable inputs. The original radial refinement160 and its actual bound $\|R^{-1}\|\le3$ are unrelated to this auxiliary angular cutoff224.

This corrector has no guaranteed contraction factor in the present evidence. Before any further iteration, its whole signed trial, all source pieces and all affected receiver terms must be saved and checked as one distinct candidate. An unfavorable result does not authorize an automatic larger band or iteration.

## W2H8. Full receiver and finite-gate obligations

The observation $C=G_fB_{LH}$ is the paired head receiver. A separate tail-source observation uses the original $T_VB_{LH}$ with its own output norm. The same abstract identity may be applied to that observation, but it requires its own complete dual trial and source/defect norms. A paired-head bound is not relabeled as a tail-source bound.

Likewise a change of primal trial in (24) changes its raw norm, high-state error, high-trace error, family-LH response, signed-centre source and tail source. All those terms must be recomputed only as the new complete candidate, with every already completed unchanged object read verbatim. One may instead keep the old primal trial in (21), reuse its complete old $E_H$ and trace bounds, and change only the declared dual comparison and its affected family/centre terms.

The original independent outer input, its paired error, the odd/mean endpoint receivers, full outer chart and affine sources remain. The actual outer trace bound comes from its qualified trace receiver, never from a bare $L^2_r$ evaluation. Its old complete value may be reused only when both operator and reference observation are unchanged.

A complete future candidate must provide the same full quantities entering WVC.42:
$$
 \begin{split}
 e={}&e_\rho+(1+e_\rho)
       \sqrt{w_0^2(K_H+\varepsilon_H)^2+\varepsilon_b^2}
       +\sqrt{w_0^2o_H^2+o_b^2},\\
 d_f={}&(1+e_\rho)(K_H+\varepsilon_H)+o_H,\qquad
 t_f=\sqrt{w_0^2t_H^2+t_b^2}.
 \end{split}
 \tag{W2H.27}
$$
Here $K_H$ and $\varepsilon_H$ must be justified for the same complete signed comparison, such as (20), after its actual trial and coordinate factors. The scalar $d_f$ in (27) is distinct from the dual defect operator $d$ in (10).

Only a newly saved strict whole comparison
$$
                         e+3d_ft_f<1
 \tag{W2H.28}
$$
would activate the existing finite reconstruction theorem. The actual tail bound3 is unchanged because the actual operator, spaces and projections are unchanged; a new reference does not inherit an unproved reference contraction.

Equations (12), (19) and (25) by themselves do not prove (28), a prescribed signed96 inverse, the full physical inverse, a negative-side extension, strong $\nu$, or any nonlinear Nash gate. A false sufficient comparison remains a complete mathematical outcome, not a proof of singularity.

## W2H9. Minimal next work and immutable numerical boundary

The first dual candidate can be developed from:

1. The complete WVC actual file, with all56 completed records, all mode-prefix records, its false finite gate, full original scopes and exact saved reference definition.
2. The same admitted continuous repaired-degree32 packets, original source/native coverage and complete full-degree96 difference envelopes.
3. The exact complete low reference receiver and its reverse, including every physical body coordinate and root/outer atom.
4. The same high principal kernel and reverse on97 through160.
5. The complete new dual residual (22), measured in its true $H^1$ state-dual window, the family terms (19), and the complete signed map (20).

No norm upper supplies a signed coefficient. No current source definition or parameter selection is changed. Original native restoration identities, complete coverage and actual raw transmissions remain mandatory.

A first implementation should declare complete natural graphs for the dual trial/defect, the complete family correction, the entire signed-centre paired map, any separately changed tail receiver, and the full final comparison. Its exact record count and source/output models must be derived from that finished implementation. This note does not silently authorize a numerical child, a particular resource budget, a new coefficient array artifact or an automatic retry.

The optional corrector in W2H7 has additional new angular-band prerequisites and must have a separate complete candidate declaration. It is not justified by simply changing the number160 in an old successful source and rerunning its targets.

All formulas in this note were derived without evaluating new scientific numbers. The quoted current records are copied as strings. The rational argument (6)--(8) and the exact support arithmetic are proof statements, not a new interval evaluation.

## W2H10. Complete primary evidence

All paths below are relative to topics/visible-flex-exact-nearby. The actual source and receipt entries were read in full as small UTF8 text; no native binary, large log, old producer or scientific function was executed.

| Exact role | Path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| Actual dual window, both complete collar/body columns, original mean and seams | results/R133-supplement-cellwise-principal-inverses-and-dual-radial-head-tail.md | b37c59bc05a2131b27014f37c1a6555d6f7e2c58 | 22954 | 22fb6fac312540818390bea1bb3a3ed2c750f515ad91bbbb1b0790fcdfe1fd6e |
| Complete actual centre residual, trial, receiver and finite comparison | results/R133-supplement-continuous-repaired-centre-trials-and-clipped-tracefree-reference.md | e377cb2e0578fc66ba8a7bc32e339fadcb0a242c | 29128 | fade78e696506af0ef2c1e304e824ff7415c63df53b31f0ed299d8ff548845a8 |
| Completed WVC scientific result; full56 records, original copies and false gate | notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json | 746ec1e16befe8914c64521ad087c1f1dd23ab73 | 78627 | 85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88 |
| Exact whole high/source/paired/finite assembly used in that completed result | scripts/fourfold_codazzi_continuous_centre_candidate_math.py | 7236b07376a46e96a2664aa3d800896bc182ed89 | 12983 | 9ff4d6cac77591957632e68fe87d1b1356e66662d6e16c01e447d2500e29fd98 |
| Same real Fourier words, both reference Green triangles and full reverse kernels | scripts/fourfold_codazzi_continuous_centre_kernel_math.py | b6b08273eb17923a4b98cce439d4cd11988c6be8 | 32915 | 0b3cc24c80fd1f038c5f3b1d3df2ea7cf8ce19695f30bdedd7a3a37f86fd9584 |

The published WVC false finite comparison remains independent of these new analytic alternatives. The complete WEX endpoint computation, WSMF52 and all previous successful physical error bounds are unaffected.
