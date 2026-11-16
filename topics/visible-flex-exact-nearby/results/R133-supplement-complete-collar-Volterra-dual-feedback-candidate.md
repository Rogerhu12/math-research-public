# R133 supplement: a complete collar Volterra and dual-feedback candidate

2026-11-16, tail_connector.

**Proved here: a fixed complete operator candidate, its exact residuals, and its numerical target boundary. No new scientific number is evaluated.** The candidate replaces the uncorrected collar source in W2H by a two-term ordinary Volterra correction. It also corrects the dual collar residual. The whole signed-centre feedback is estimated again, with all family differences and the transition included.

The first candidate fixes the completed WVC low reference and the actual operator, input and output spaces, radial projections, and finite trial factors. It changes a complete decomposition of the same paired head operator. Existing complete tail, independent outer and endpoint observations of that same operator remain read-only. There is no unannounced switch to the WCTR reference, larger radial mesh, or repeated iteration.

The mathematical target list below is complete. One input distinction remains essential before any implementation can be admitted: the completed WVC owner uses a zero placeholder on its collar. The actual signed degree32 centre and the full-family differences on that collar have not thereby been supplied. Section W2C9 identifies the required original coefficient evidence without replacing it by that placeholder.

## W2C1. Fixed interval, operators and reference

Use the same actual selected positive realization and notation as W2H. In particular,
$$
 \mathscr X=L^2(I;E_L),\quad \dim E_L=193,\quad
 \mathscr F=L^2_rH^{-2/3}_{\phi,H},\quad
 \mathscr H=L^2_rH^{-1}_{\phi,H},\quad
 G_H:\mathscr F\longrightarrow\mathscr H .
 \tag{W2C.1}
$$
The angular measure is normalized, physical frequency is $4j$, and every radial integral uses ordinary $dr$. The actual high space has its original reflection/parity and $|j|\ge97$; it is not replaced by an unrelated complex-circle inverse.

Let $a=r_*$ be the true root, $R=25/8$, and take the original proved body cut
$$
 c=\frac{1192029371497}{5000000000000},\qquad
 I_c=[a,c],\quad I_b=(c,R],\quad h=c-a\le\frac9{10^6}.
 \tag{W2C.2}
$$
The original full-family root interval is
$$
 \left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}
 \right].
 \tag{W2C.3}
$$
This is the collar of the complete given-head positive inverse. It is not the different $3/10^6$ support length of the positive trial cutoff used elsewhere.

Fix the completed WVC low reference $D_f=D_a$, its complete receiver $G_f$, the same $S$, and the same actual radial refinement160. Define
$$
 \begin{split}
 L&=\partial_r-A_{HH},&
 B&=B_{HL}S^{-1},&
 C&=G_fB_{LH},\\
 \mathcal K&=CG_HB,&
 \Gamma_H&=(A_L-D_f)S^{-1}+B_{LH}G_HB .
 \end{split}
 \tag{W2C.4}
$$
All97 root-complement outputs,96 outer outputs with their true $H^{-5/6}$ weight, physical mean coordinate and body output belong to the complete range of $G_f$.

The symbol $A_c$ below means the entire centre high block $P_H\mathscr A_cP_H$, never the scalar collar source constant. With the actual radial principal retained in $\mathscr A_c$, set
$$
 \begin{split}
 L_c&=\partial_r-A_c,& B_c&=B_{HL,c}S^{-1},&
 C_c&=G_fB_{LH,c},\\
 \Delta A&=A_{HH}-A_c,&
 \Delta B&=B-B_c,&
 \Delta C&=C-C_c .
 \end{split}
 \tag{W2C.5}
$$
The continuous repaired-degree32 centre is a trial operator replacement, not a different physical background solution. The full-degree96 actual difference, all ordered primitives and the complete physical mean rank remain.

## W2C2. One fixed collar primitive and cutoff

Write $P_c,P_b$ for restriction followed by extension by zero on the two radial intervals in (2). For an ordinary radial field define
$$
 (\mathcal J_c f)(r)=\int_a^{\min(r,c)}f(s)\,ds,\qquad
 \partial_r\mathcal J_c f=P_cf .
 \tag{W2C.6}
$$
In a nested expression $\mathcal J_c A_c\mathcal J_c f$, the inner coefficient and inner primitive are integrated only over $[a,c]$. Beyond $c$, each displayed primitive is its constant terminal value. The map is not an evaluation on an arbitrary $L^2$ input.

Use the same already declared transition width $w=1/16$. Let
$$
 \psi(r)=
 \begin{cases}
 1,&a\le r\le c,\\
 1-3t^2+2t^3,\quad t=(r-c)/w,&c<r<c+w,\\
 0,&c+w\le r\le R.
 \end{cases}
 \tag{W2C.7}
$$
The admitted original geometry has $c<c+w<R-w<R$. Thus $\psi$ is a fixed $C^1$ multiplier, with both derivative joins included. It is the complement of the original upward cutoff on that transition. Its value and derivative are exact functions; no adjustable width or numerical sweep is proposed.

The norm of the zero-initial primitive on the collar satisfies
$$
 \|P_c\mathcal J_c\|_{L^2(I_c)\to L^2(I_c)}
                  \le\frac{2h}{\pi}.
 \tag{W2C.8}
$$
For example this is the Dirichlet-at-the-left, free-at-the-right Poincare inequality. It applies to each fixed Hilbert angular fiber and therefore to the complete Bessel-weighted finite bands. It does not remove the primitive's constant continuation or the entire transition cost in (7).

## W2C3. The exact two-term primal correction

Keep the old actual body trial
$$
 V_b=\chi G_{0,160}\chi B_c .
 \tag{W2C.9}
$$
Here $\chi$ and the high principal inverse are exactly the original WVC ones. The signed centre input on the collar is multiplied by $\chi=0$, so the new genuine collar packet does not change the operator in (9).

Define
$$
 U_0=\mathcal J_cB_c,\qquad
 U_1=\mathcal J_cA_c\mathcal J_cB_c,\qquad
 V_c=\psi(U_0+U_1),\qquad
 \widehat V=V_b+V_c .
 \tag{W2C.10}
$$
These are operators on the complete ordinary $L^2$ head. No radial derivative of a head input or of $B_c$ is taken. The centre residual is
$$
 R_c=L_c\widehat V-B_c .
 \tag{W2C.11}
$$
On the collar, the old trial and its derivative vanish, and direct differentiation gives
$$
 \boxed{P_cR_c=-P_cA_c\mathcal J_cA_c\mathcal J_cB_c.}
 \tag{W2C.12}
$$
Indeed $L_c(U_0+U_1)=B_c-A_cU_1$ there. Thus the old complete $-B_c$ source has cancelled as an exact operator, before any positive estimate.

On the body let $R_b=L_cV_b-B_c$. The entire residual is
$$
 \boxed{
 P_bR_c=P_b\{R_b+\psi'(U_0+U_1)-\psi A_c(U_0+U_1)\}.}
 \tag{W2C.13}
$$
All the transition terms in (13) must be included in the same new body source graph. The new candidate does not replace a source on the collar by a free homogeneous continuation.

The actual residual is exactly
$$
 \mathcal R=L\widehat V-B
          =R_c-\Delta A\,\widehat V-\Delta B .
 \tag{W2C.14}
$$
The complete $\Delta B$ on the collar is still present. It must be obtained from genuine same-family coefficient evidence, not inferred from the small length or removed by the centre cancellation.

## W2C4. Actual homogeneous graph qualification

The old reference condition of $G_{0,160}$ at the root is not identified with the actual stable-root chart. The new correction instead belongs to the closed original homogeneous graph.

For every fixed head input, $V_c$ has finite angular support, ordinary radial $H^1$, zero raw value in both components at $a$, and zero value at $R$. Its raw value is continuous at $c$, at both cutoff joins and at every original identity-transmission seam. Different piecewise $S_i$ are never reset. The only new derivative jumps occur inside an ordinary weak $L^2$ source.

A precise argument also avoids assuming that a stronger asymptotic port follows merely from a convenient trace name. Let $v=V_cx$. Approximate $v$ by same-parity finite-angular functions $v_n$ compactly supported in the open interval, with $v_n\to v$ in ordinary $H^1_r$. On the fixed bands used here, the complete actual coefficients give
$$
 Lv_n\longrightarrow Lv\quad\hbox{in }\mathscr F,\qquad
 v_n\longrightarrow v\quad\hbox{in }\mathscr H .
 \tag{W2C.15}
$$
The original core identity used in WPT.15 gives $G_HLv_n=v_n$, with every genuine root/stable, outer, independent mean, affine and impulse port zero. Boundedness of the original $G_H$ then gives
$$
                         G_HLv=v .
 \tag{W2C.16}
$$
Hence $v$ is in that same closed homogeneous realization. No new root boundary condition is substituted.

The required finite-band coefficient bound is on the entire actual interval, including the collar; body rows alone are not enough. If an implementation has an actual nonzero raw transmission, it must transport the correction accordingly or add its complete impulse residual. The present candidate uses only the original proved identity transmissions.

## W2C5. The complete dual correction

The adjoints use the original ordinary-$dr$ angular distribution pairing:
$$
 \mathscr F^*=L^2_rH^{2/3}_{\phi,H},\qquad
 \mathscr H^*=L^2_rH^1_{\phi,H}.
 \tag{W2C.17}
$$
For this candidate $C_c=G_fB_{LH,c}$ is a bounded map from the raw high body state to the complete low output. Its adjoint is the ordinary body field $B_{LH,c}^*G_f^*z$. Root and outer output coordinates first pass through the complete adjoint body kernel of $G_f$. They are not silently treated as point sources in $\mathcal J_c$.

Any independent actual high endpoint, jump or affine observation that has not passed through that bounded body adjoint remains in its original seven-port row. It is not an input to (6) by an unproved $L^2$ identification.

Set
$$
 \begin{split}
 W_b&=\chi G_{0,160}^*\chi C_c^*,\\
 Z_0&=\mathcal J_c C_c^*,\qquad
 Z_1=\mathcal J_cA_c^*\mathcal J_c C_c^*,\\
 W_c&=\psi(-Z_0+Z_1),\qquad
 \widehat W=W_b+W_c .
 \end{split}
 \tag{W2C.18}
$$
The formal high adjoint is $L_c^*=-\partial_r-A_c^*$. The full centre dual residual $D_c=L_c^*\widehat W-C_c^*$ is
$$
 \boxed{P_cD_c=-P_cA_c^*\mathcal J_cA_c^*\mathcal J_cC_c^*,}
 \tag{W2C.19}
$$
and, with $D_b=L_c^*W_b-C_c^*$,
$$
 \boxed{
 P_bD_c=P_b\{D_b-\psi'(-Z_0+Z_1)
                          -\psi A_c^*(-Z_0+Z_1)\}.}
 \tag{W2C.20}
$$
Both signs of the transition derivative are fixed by the formal $-\partial_r$. The complete actual dual residual is
$$
 \mathcal D=D_c-\Delta A^*\widehat W-\Delta C^*:
                       \mathscr Z\longrightarrow\mathscr H^* .
 \tag{W2C.21}
$$
Every angular adjoint includes its full ordered multipliers, the intermediate zero-mode projection of $I$, $I^*=-I$, derivative of a drift multiplier in its true angular adjoint, and the genuine mean terms.

The same compact-core limit as in (15), now applied to $W_c$ and the full Green identity, proves admissibility in the true dual graph. In particular, endpoint terms vanish because both raw components of the test correction have zero trace; no artificial adjoint boundary condition is imposed. The full bound is in $H^1$ as in (21), not in an unweighted space relabeled afterwards.

## W2C6. What the collar estimate proves

Let $b_c$ bound $B_c$ from the collar head to its complete source window. Let $a_c$ bound each required $A_c$ contraction between the successive finite angular bands in that source window. From (8), a valid collar centre residual bound is
$$
 \|P_cR_c\|
       \le a_c^2\left(\frac{2h}{\pi}\right)^2 b_c .
 \tag{W2C.22}
$$
For the dual use its own complete $H^1$ contractions $a_c^\dagger$ and the whole $g_c=\|P_cC_c^*\|_{\mathscr Z\to L^2H^1}$:
$$
 \|P_cD_c\|
       \le(a_c^\dagger)^2\left(\frac{2h}{\pi}\right)^2g_c .
 \tag{W2C.23}
$$
A full kernel norm of (12) or (19) may replace either product by a sharper complete bound. Every Bessel conversion belongs to the actual indicated bands. The old low-head number $62286/125$ is not automatically a same-space high224 or dual $H^1$ bound.

Equations (22)--(23) remove the fixed zero-order centre collar term responsible for W2H's old budget obstruction. They do not prove a small actual error: the full family terms (14),(21), all transition terms, and the signed-centre map below still need bounds. The old complete source constant is neither subtracted from a new upper bound nor reinterpreted as a signed coefficient.

The primitive acts on the complete source function in $L^2$. Formula (22) therefore does not assume that $B_cx$ is continuous in $r$, or that an arbitrary head input has a derivative.

## W2C7. One entire paired head comparison

The exact W2H identity applies to the new $\widehat V,\widehat W$:
$$
 \mathcal K=C\widehat V-\widehat W^*\mathcal R
                     +\mathcal D^*G_H\mathcal R .
 \tag{W2C.24}
$$
Define the complete signed centre map
$$
 \mathcal H_c=
 G_f(A_{L,c}-D_f)S^{-1}
          +C_c\widehat V-\widehat W^*R_c .
 \tag{W2C.25}
$$
Then the actual paired head operator is
$$
 \boxed{
 G_f\Gamma_H=\mathcal H_c+
 G_f\Delta A_LS^{-1}
 +\Delta C\,\widehat V
 +\widehat W^*(\Delta A\,\widehat V+\Delta B)
 +\mathcal D^*G_H\mathcal R .}
 \tag{W2C.26}
$$
The low-family difference includes the collar, and keeps the entire low physical mean. It is not copied from a previous decomposition whose centre was zero on that collar.

All signs in (25) are actual operator signs. A saved upper bound for $\widehat W^*R_c$ cannot be subtracted from a saved upper bound for the other terms. The complete signed kernel or an exact signed circuit must be formed first. A full triangle bound remains valid but is not presumed to improve the old171 bound.

Let $\rho_c,\rho_b$ be complete bounds for the two pieces of $\mathcal R$. The original whole-output source columns give
$$
 E_{\rm new}=C_{\rm col}\rho_c+C_{\rm body}\rho_b .
 \tag{W2C.27}
$$
Let $\delta_c,\delta_b$ bound the two disjoint output pieces of $\mathcal D$, from the same complete $\mathscr Z$ input. A valid whole bound is
$$
 \delta=(\delta_c^2+\delta_b^2)^{1/2},\qquad
 \|\mathcal D^*G_H\mathcal R\|\le\delta E_{\rm new}.
 \tag{W2C.28}
$$
This retains all collar/body cross propagation. It does not assert that either inverse or observation is block diagonal in the radial partition.

With the full norms of the other three remainder terms in (26), define
$$
 \varepsilon_{\rm new}=
   \|G_f\Delta A_LS^{-1}\|_{\rm ub}
  +\|\Delta C\,\widehat V\|_{\rm ub}
  +\|\widehat W^*(\Delta A\,\widehat V+\Delta B)\|_{\rm ub}
  +\delta E_{\rm new}.
 \tag{W2C.29}
$$
A complete bound $K_{\rm new}\ge\|\mathcal H_c\|$ plus (29) bounds the same actual paired operator. All complete family terms use the same centre, primal trial and dual trial. No favourable entries from another candidate are selected.

## W2C8. Supports and unchanged complete observations

The centre blocks start with high support97 through160. Each centre angular action can shift by64. Thus
$$
 \begin{array}{c|c}
 \text{actual constructed object}&\text{largest possible angular index}\\ \hline
 \mathcal J_cB_c,\ \mathcal J_cC_c^*&160\\
 \widehat V,\ \widehat W&224\\
 R_c,\ D_c&288\\
 \Delta A\,\widehat V,\ \Delta A^*\widehat W&416
 \end{array}
 \tag{W2C.30}
$$
The direct $\Delta B$ and $\Delta C^*$ terms have their full support through288. These are supports of explicitly constructed trial and residual coefficients. The unknown actual $G_H\mathcal R$ has every high mode and is not truncated to416.

The number224 here is an auxiliary angular trial band. It is not the actual radial refinement160, the actual193 radial fiber, or the prescribed96 physical root coordinates. Neither the actual projections nor the already proved actual tail inverse bound3 changes.

With $D_f,G_f$ and the actual finite trial factors fixed, the following are unchanged **complete operators**, even though their previous proofs used an older high trial:

| Existing whole object | Reason its entire old record may be read |
|---|---|
| reference inverse and normalizer defect, $q,e_\rho$ | the full low reference is fixed |
| complete actual independent-outer paired error $\varepsilon_b$ | $G_fB_{LH}\mathcal P_b$ is unchanged |
| complete actual high outer trace $Y_a$ | both the old and new trial have zero true outer trace, so the old full observation is still the actual one |
| complete $q_R,o_H,o_b$ | their reference, actual trace and independent outer rows are unchanged |
| complete actual head and outer tail source bounds $t_H,t_b$ | they bound the same $T_V\Gamma_H$ and actual outer source |
| complete $T$ | the previous full square-sum bound is for those same actual tail blocks |

In particular the old complete $T$ can be copied directly; its square root is not reevaluated. The old high-state *error relative to the old trial* cannot serve as $E_{\rm new}$ in (27).

The original endpoint atoms, two physical density means, independent scalar mean, stable root, impulse, affine, exterior, $\Theta,\nu$, cokernel and arbitrary external-function inputs all retain their original rows. A complete actual trace is not inferred from bare radial $L^2$. No all-s or nonlinear Nash conclusion follows from a single candidate comparison.

If a future version uses WCTR, its entire low-reference provider and every affected observation in this table must be changed consistently. That is a different declared candidate; none of its numerical success is assumed here.

## W2C9. The exact missing collar input

The already completed WVC owner does not contain a signed genuine collar centre. Its function new_complete_parent_work creates its first parent with zero_packet for both reference and actual placeholders, assigns difference_AL=old G_c and difference_LH=old L_c_raw, and sets family_AHH=0. This is valid there because the old high trial is identically zero on the collar and the full actual collar fee is paid independently.

It does not supply $B_c,A_c,C_c^*$ for (10),(18). In particular, neither that zero packet nor WGS's complete norm-majorant tables can be interpreted as signed first32 Fourier coefficients.

The existing original collar source and its complete process establish:

- the same candidate, physical repair and full193 direction identities;
- one actual candidate piece2549 containing the entire collar and the original complex root domain;
- root radius $1/100000$, the real-family direction radius $1/100000000$, and the same full degree96 family;
- the exact root interval and cut (2)--(3);
- complete bounded collar coefficient and source/port contracts, with19 actual successful gates.

They do not by themselves print every signed coefficient required by the new trial.

Before a numerical source is frozen, a data-only admission must locate the exact original signed intrinsic germ enclosure, the original degree32 cubic on that same piece, the complete physical repair enclosure, and the full-family direction/remaining difference on that collar. Every path, original blob, bytes, SHA256, domain and normalization must be fixed. Original archived objects may only be restored by their immutable identities; no old producer or coefficient certificate is rerun.

The centre is the actual selected degree32 repaired function, not a midpoint inferred from an upper bound. Its $\eta$ principal is the actual one. The complete $\Delta A_L,\Delta A,\Delta B,\Delta C$ must be formed on the true collar from those same definitions and complete error envelopes. Positive-body records starting at $c$ cannot be extrapolated inward.

The small original collar producer already pins its two originals by SHA256:
$$
 \begin{split}
 \text{root germ: }&
 397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864,\\
 \text{root budget: }&
 10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f .
 \end{split}
 \tag{W2C.31}
$$
The first original path is notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz; the second is notes/current_root_scalarization_ci/run-43594466882-1/consumers/complete-moving-root-scalarization.json.gz. The complete restoration tuples and exact coefficient fields still require admission. A checksum alone does not certify their unseen field shapes.

All collar scientific coefficients introduced solely for this new complete operator are private intermediate packets. A future complete source must distinguish them from unchanged original public bounds, which remain copies.

## W2C10. A complete five-graph target contract

The following is the fixed target list for this candidate, conditional on the complete original input admission in W2C9. It does not authorize a science run before the source, full schema and output model exist.

A “norm triple” means a whole-input row bound, its true whole-output transpose column bound, and their square-root norm bound, in the indicated actual weighted spaces. The underlying positive kernel must dominate the declared entire signed operator. It includes any diagonal multiplier as well as all continuous and atomic rows; it is never a sampled-column check.

| Ordered complete graph | New targets | Complete contents |
|---|---:|---|
| Primal trial and full residual | 18 | Five norm triples: raw whole $\widehat V$, centre collar residual (12), centre body residual (13), full-family collar term $P_c(\Delta A\widehat V+\Delta B)$, and its full body term. Then the two complete source sums $\rho_c,\rho_b$ and $E_{\rm new}$. |
| Complete dual residual | 15 | Four norm triples: centre collar (19), centre body (20), full-family collar part of $\Delta A^*\widehat W+\Delta C^*$, and its body part, all measured in the true state-dual $H^1$. Then $\delta_c,\delta_b$ and the full $\delta$ in (28). |
| Complete family and dual feedback | 11 | Three norm triples for the first three remainder operators in (26). Then $\delta E_{\rm new}$ and the complete $\varepsilon_{\rm new}$. |
| Complete signed centre | 3 | One norm triple for the entire map (25), with its signs retained before an admissible complete norm comparison. |
| Same actual finite comparison | 3 | The complete new $E_0,D$ and $E_0+3D T_{\rm old}$; $T_{\rm old}$ is a literal complete copy. |
| Conditional continuation of the last graph | 2 only if its strict gate passes | A true positive gap and the full finite inverse bound, saved only after that complete comparison. |

There are50 unconditional new scalar records, or52 only if the complete new gate passes. The complete set of copied original objects is separate. No old whole tail bound, high-source graph, normalizer, successful WVC target or false old comparison is recomputed.

For this fixed reference, the last graph uses
$$
 \begin{split}
 E_0={}&e_\rho+(1+e_\rho)
 \sqrt{w_0^2(K_{\rm new}+\varepsilon_{\rm new})^2+
                    \varepsilon_{b,\rm old}^2}
 +\sqrt{w_0^2o_{H,\rm old}^2+o_{b,\rm old}^2},\\
 D={}&(1+e_\rho)(K_{\rm new}+\varepsilon_{\rm new})+o_{H,\rm old},\\
 \mathfrak e={}&E_0+3D T_{\rm old},\qquad w_0=6/5 .
 \end{split}
 \tag{W2C.32}
$$
Only a saved strict $\mathfrak e<1$ gives a new inverse. Failure of this sufficient gate is a complete outcome, not a singularity certificate, a parameter-search instruction or permission to discard an unfavorable graph.

Every completed record must enter its one complete active graph before publication, be durably saved and printed, and be read back before downstream use. A failed graph retains its entire already completed record prefix and all prior complete graphs. Original full inputs and every semantic qualifier must remain bound by their complete immutable identities; no label replaces a missing domain or normalization.

The numerical source may use finite internal coefficient and kernel workspaces. They are not new public certificate arrays. Exact whole-output and worst-case escaped-JSON models must be constructed for the finished source; this note does not invent a byte cap or assume a particular private materialization is cheap.

## W2C11. Primary evidence and present conclusion

All paths are relative to topics/visible-flex-exact-nearby. The complete small texts below were read, without running a scientific function or retrieving a native binary.

| Exact primary role | Path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| Complete dual identity and all original ports | results/R133-supplement-two-sided-high-feedback-and-complete-centre-correctors.md | 7e1c46ddc9c1a771a06c6bb4bf87c8676fd8c898 | 24119 | 72bef388c4bf801bfe746f0b645d1439d1a066ae3d6b7d68ab75b374b2908d6b |
| Actual high source/state windows and compact-core identity | results/R133-supplement-cellwise-principal-inverses-and-dual-radial-head-tail.md | b37c59bc05a2131b27014f37c1a6555d6f7e2c58 | 22954 | 22fb6fac312540818390bea1bb3a3ed2c750f515ad91bbbb1b0790fcdfe1fd6e |
| Completed original WVC result and same-operator whole observations | notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json | 746ec1e16befe8914c64521ad087c1f1dd23ab73 | 78627 | 85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88 |
| Exact completed WVC owner, including the collar placeholder | scripts/fourfold_codazzi_continuous_centre_tracefree_candidate.py | d8d3f135abe8ad49b8b7b002e830bbc8ad678a5f | 59614 | 126af29d436c20c9e4fe2bb50f0d82d1f2a2c6996f3b6862cb9e1f51924b586f |
| Original complete full-family collar derivation | scripts/fourfold_codazzi_full_delta96_root_collar_budget.py | 602a8a3df10c4319446909a56d532ba88b0a6367 | 15041 | 8d3ab188d47a1aa81cbc304350655f2172333b435fdf0e09482b245f957917bf |
| Actual successful collar process, full19 gates and original contracts | notes/full_delta96_root_collar_ci/run-43606747196-1/consumers/process.json | d10f4681c84ab579b8121b16e6246604a608a715 | 11340 | f919ecd9da5d447cf8950d1b267c28c7c33c2c396b21318b64a45317646745ae |

The completed old finite comparison is still false. The new result is an exact, fixed two-sided collar-corrected candidate with no constant centre collar forcing, complete transition and full-family costs, and an explicit50-record finite test. The required signed collar input is an identified admission task; none of its new numerical targets is represented as already evaluated.
