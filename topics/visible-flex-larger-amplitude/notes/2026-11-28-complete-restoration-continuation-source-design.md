# Restoration continuation from the paid linear model and returned geometry

Prepared from complete published source on 2026-11-28 UTC. This is an independently prepared outer-algorithm design and a complete standard-library implementation of its scalar policy. It does not modify a running job, launch a solver, claim a new field, or replace the separate run22 half-wave seed direction.

## 1. Concrete outcome and the actual counterexample

The proposed next algorithm retains the existing full Phase-I QP, all selected typed inequalities, the full H2 coordinate norm, every variable, every normal stage, all nonlinear trial checks and the entire declared budget. It adds one success-dependent rule for the **next restoration damping**. After an actually accepted full step, it compares the already computed full-step selected-row prediction with the already returned complete finite geometry. Only if the selected model starts at the same finite violation and the actual decrease agrees sufficiently with its prediction does it reduce the next damping by a factor of ten. Otherwise it leaves the original damping rule in force.

This addresses a concrete asymmetry: accepted metric directions can reduce metric damping, while accepted restoration directions never reduce restoration damping. Restoration damping changes only when all line trials fail, when it increases by four. Successful but small restoration steps can therefore retain exactly the same regularization even when the actual linear model is useful.

It does **not** establish that damping caused the observed small decreases. The public observations have not supplied the actual accepted alpha, complete selected gradient norms, complete QP termination residuals or selected linear prediction needed for that attribution.

The latest root-observed run20 fact refutes an unconditional nonlinear improvement claim. At fixed publication head `920546134cd72cab133165c2be7a5380204dabd9`, the first completed trial at initial restoration damping `.001` had true finite positive violation `0.9750099817855096`, exceeding the current `0.9684249942095058`, and its returned acceptance was false. A new trial at point `d34614ab98e8942a3dc9e8e0ff77d4bda999c436b1a765ea8fc741cfcb8d72ee` started at `2026-11-28T00:03:30.800085+00:00`; its alpha and returned statistics were not supplied with that observation. It is a new trial, not evidence of a second direction.

Run19's first accepted restoration is a different fact: true finite positive violation decreased from `0.9684249942095058` to `0.9679630392005261`, while Phi changed from `3825.0583894874153` to `3825.0583176123996` and the finite maximum Gram residual rose slightly. The subsequent trial's statistics, Phi `3824.6263877655356` and Gram `0.6461163467955962`, did not by themselves establish geometry or acceptance. These are root-provided actual observations, not new numerical evaluations made for this note.

A later fixed read at `0d5f25d1fc7e00e48eede73f5ddf02f734ce7710` returned the run19 second trial's true finite positive violation `0.9817636973298995` and rejection; the accepted current point remains `d761b5...` at `0.9679630392005261`. Its next `b90d...` trial has returned only statistics, Phi `3824.8419061258187` and Gram `0.6460565438436483` at `2026-11-28T00:10:54.391913+00:00`. Run20's `d34614...` trial has statistics Phi `3824.9207739761805` and Gram `0.6460517826414733` at `2026-11-28T00:11:35.553745+00:00`; its geometry is still unknown in that record. Neither statistical decrease is promoted to acceptance. These further observations reinforce the need for true geometry and do not supply the still unknown QP model or alpha.

The new policy retains the full original backtracking in the face of precisely the run20 behavior. Agreement at one accepted parent is a reason to try a different next regularization, not a promise that the next nonlinear candidate will succeed. Run22's new half-wave seed remains separate.

## 2. Complete source attribution

Every source below is a complete text body below 100,000 bytes. Code-derived claims refer to these exact whole bodies. The new module was written as text; neither it nor a solver was executed, parsed with Python AST, compiled, benchmarked or tested on a fixture.

| Complete source basename | Bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| fullclosed_fixed_fejer_meridian_batched_so3_qp.py | 99313 | `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f` | `8bba3e30bb8e843fd725a2d19f8966b984acc4ae` |
| fullspace_feasible_active_cg_v3.py | 26947 | `fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4` | `fabfcd7556a634d19e8dac788d5cb95d696b3d5d` |
| fixed_fejer_supported_so3_meridian_operator.py | 40840 | `552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3` | `1d9e435bb68374b71c3d7361771c28f47838d59e` |
| so3_fixed_fejer_batched_missing_angle_geometry.py | 88163 | `5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135` | `c5325d3da8329547ad81e74a5da479323bfccd21` |
| complete_material_envelope_rows.py | 13744 | `729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7` | `3021e07436bc7fc8a6b1e4dd60f694d5d45e61a0` |
| fixed_fejer_complete_geometry_trial_progress.py | 39500 | `321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5` | `8173d3576958dc5c476466dd4c5012c5ed81b0c1` |
| read_fixed_fejer_meridian_batched_so3_report.py | 99382 | `8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49` | `9cd36fd99113d285fc47f17bad929647c8fc6de3` |
| fixed_fejer_detached_meridian_normal_lift.py | 96276 | `76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d` | `fc51c16b6dbd53abf04fe9175e5421f77e25c49c` |

The paths are under `topics/visible-flex-larger-amplitude/scripts/resume_20261126/`, except `fullspace_feasible_active_cg_v3.py`, under `scripts/resume_20261120/`. Complete paths are retained in the companion integration design and delivery manifest.

The existing fixed-.001 explanation remains at `notes/2026-11-27-full-restoration-scale-and-mu001-branch.md`, 15,526 bytes, SHA256 `42ef2c9012b6c76439f09d0255392eabda6a27d240737e22e1bd74e3a914e313`, Git blob `2338fb6779d9f2e8331fa370503cbf2752738758`. Its regularization comparison is used with its exact hypotheses, not presented as a new geometric theorem. The existing width analysis and R721/R722 are not replaced or re-proved.

Locations in the exact driver: `CommonSlackRows` begins at line145; `statistics` at824; `scan` at850; `physical_violation` at855; the outer loop at907; full selected-row construction at925; restoration QP construction at957–967; saved predictions at989–1009; trial evaluation/acceptance at1021–1057; accepted damping at1072–1078; failure multiplication at1081–1085; final rereading at1101–1115. These locate the complete functions; excerpts do not replace the source bodies.

## 3. The actual Phase-I objective and units

Let \(z\) be the complete physical step in the existing H2 coordinates, \(d\) the common-slack increment, and
\[
 w=(z,d),\qquad \tau=\tau_0+d.
\]
For every selected typed row let \(g_i\) be its actual physical signed violation and \(a_i z=dg_i[Tz]\) the complete coordinate derivative. The source solves
\[
 \min_w\ \frac12\tau^2+
       \frac12\mu^2(\|z\|^2+d^2)
 \quad\text{subject to}\quad
 g_i+a_i z\le\tau\ \text{for every selected row},
 \qquad\tau\ge0.
\]
The actual initialization is
\[
 \tau_0=\max(0,\max_i g_i)
       +8\epsilon_{\rm mach}(1+\max_i|g_i|).
\]
This padding initializes slack. It is not a nonlinear acceptance tolerance or extra geometric margin.

`CommonSlackRows` retains the complete original selected prefix, amplitude rows and every appended permanent typed row. Its positive rescaling by \(\operatorname{hypot}(\|a_i\|,1)\) applies to both sides and preserves the finite feasible set. Complete gradients and row metadata remain in the original scratch cache/report. No variable or typed row is eliminated.

The restoration operator is just \(Aw=d\), with residual \(\tau_0\). QPv3 squares its damping argument: the coefficient is \(\mu^2\), not \(\mu\). Thus .01 and .001 correspond algebraically to coefficients \(10^{-4}\) and \(10^{-6}\); this does not identify the best nonlinear value.

The original `jet-sum` norm uses radial length .05 and angular transition24. It includes all free core coefficients, every rotation node jet and height, and explicitly is not the exact radial Sobolev integral. The endpoint root-control radius is not an outer trust-region radius. Row-gradient norms are computed after the complete `coordinates.transpose` mapping. The proposed policy changes none of these units.

A one-row symbolic specialization illustrates a possible scale effect without diagnosing the actual run. For one nonzero gradient \(a\), no other active restriction and the conceptual unpadded start \(\tau_0=g>0\), the active exact solution satisfies
\[
 \frac{g-\tau_\mu}{g}
 =\frac{\|a\|^2}{\|a\|^2+\mu^2(1+\|a\|^2)}.
\]
A small gradient in the chosen norm can therefore give a small regularized linear improvement. This is algebra only, not a reduced solver or numerical fixture and not a claim about the actual many-row active set. The actual algorithm retains its padding and every row. Its true gradient scales remain unknown until their records are read.

## 4. Restoration acceptance is independent of Phi descent

The driver rescans the current field and chooses metric mode only when finite geometry is complete, passed and has zero positive physical violation. Positive violation selects restoration; undefined geometry stops without inventing a valid linearization.

Every candidate still pays for the original complete residual/statistics and must have positive relative E and determinant. Restoration is then accepted by
\[
 G_{\rm trial}<G_0,\qquad
 G_{\rm trial}\le(1-10^{-4}\alpha)G_0,
 \qquad G=\max(0,\texttt{maximum\_physical\_g}),
\]
together with the original complete-geometry requirements.

Phi need not decrease in restoration. An incidental Phi decrease with an increased maximum Gram residual is compatible with this declared objective. Such observations do not assess a metric-LM direction which has not occurred, and do not distinguish a short full step from a backtracked or truncated step.

The new helper does not accept or reject a trial. It is called only **after the complete direction returns and the original success/failure damping block runs**. It reads the original returned acceptance and own-point records. Rejection keeps the original fourfold increase. The metric branch is outside this policy.

The complete current allowances remain one metric direction with up to16 advances, up to4 restoration directions with64 advances each, and up to15 line trials per direction. All32 normal stages and all original angular, radial, integration, permanent-memory and typed-row responsibilities remain. The budget is an allowance, not a requirement to run redundant work after the original stopping condition; the proposed policy shortens neither the allowance nor the domain.

## 5. A structural correction: conditioning does not imply 64 slow face solves

The Phase-I Hessian, with \(e\) the slack-coordinate unit vector, is
\[
 H=\mu^2I+ee^\top.
\]
On one fixed active face let \(P\) be its Euclidean orthogonal tangent projection and \(p=Pe\). The restricted Hessian is
\[
 H_T=\mu^2I_T+pp^\top.
\]
It has at most two eigenvalues, \(\mu^2\) and \(\mu^2+\|p\|^2\). Exact CG on an unchanged face therefore needs at most two unblocked advances.

The actual code also performs face additions/releases, floating-point projections, literal row tests and residual replacement. The complete QP need not finish in two advances. The result does rule out using the condition number alone as an explanation of all64 allowed advances.

For reference, an exact fixed-face Newton direction is available. Put \(u=Pw\), using the current \(\tau=\tau_0+e^\top w\). Then
\[
 d_N=-u-p\,\frac{\tau-p^\top u}{\mu^2+p^\top p}.
\]
Since \(P\nabla f=\mu^2u+\tau p\), direct substitution gives \(H_Td_N=-P\nabla f\). The denominator is positive even at \(p=0\), when \(d_N=-u\). All components remain in the complete tangent space. The expression avoids a subtractive inverse written with \(1/\mu^2\).

A separately declared QP implementation could replace two unblocked fixed-face advances by one such minimization while retaining every inactive-row blocking test. Its early-release path still needs the original sign logic: a Newton direction after releasing a row is not automatically inward before face stationarity. It must preserve true final residuals and not label a truncated result exact KKT.

No QP rewrite is included here. The potential saving is limited to that face operation. Restoration's A/A* are already trivial; full row projections remain. This algebra is not a justified explanation or cure for the time spent constructing nonlinear fields and scanning geometry.

## 6. Exact success-dependent policy

Before trials, the source already records every physical \(g_i\), every selected full-step value \(\ell_i=g_i+a_i z\), actual damping, QP status/residuals and current full finite geometry. After acceptance it has the true alpha and accepted geometry. The helper reads these records; it does not call C, C*, F, J, J*, root solving, integration or geometry.

Define working scalars
\[
 M_0=\max(0,\max_i g_i),\quad
 M_1=\max(0,\max_i\ell_i),\quad
 P_{\rm dec}=G_0-M_1,\quad
 A_{\rm dec}=G_0-G_1.
\]
A selected working set is not assumed to represent every continuous constraint or even the maximum of the whole finite scan. After verifying the actual own-point/model associations, the helper requires
\[
 |M_0-G_0|\le t_{\rm work},\qquad P_{\rm dec}>t_{\rm work},
\]
where
\[
 t_{\rm work}=64\epsilon_{\rm mach}
 (1+|G_0|+|G_1|+|M_0|+|M_1|).
\]
This is a declared algorithmic binary64 comparison. It is not an interval enclosure, proof of equality of exact quantities, new physical margin or admission gate.

Reduction occurs only if:

1. The original completed direction is restoration and was accepted.
2. The literal returned accepted alpha equals1.
3. Complete rows and starting geometry belong to the same actual point/model; accepted geometry has its own valid point and the same model.
4. Every selected value/prediction is finite and present, counts agree, and full original-row retention is recorded.
5. Both geometry values are complete finite returns, \(G_0>0\), \(G_1<G_0\), and the above working comparisons hold.
6. The ordinary finite ratio \(A_{\rm dec}/P_{\rm dec}\ge3/4\).

Then
\[
 \mu_{\rm next}=\min\{\mu,\max(10^{-8},\mu/10)\}.
\]
The outer minimum avoids raising an already smaller user-selected damping. Otherwise the actual original-rule next damping is preserved. Rejected directions retain their fourfold increase; accepted backtracked steps do not trigger the new decrease. Missing or unsuitable scientific observations disable this reduction rather than stop an otherwise valid original direction.

The factor10 is an explicit algorithm choice along the already selected .01-to-.001 path. The threshold3/4 and floor have the scale of the existing metric rule, but its objective ratio is not reused or confused with this geometric ratio. The inclusive threshold and every constant are in the complete source-bound policy definition, not claimed optimal.

QP status, advance count, projected-gradient norm, maximum linear violation and coordinate-step norm are retained when present. KKT convergence is not required as an extra execution condition. The original code permits a truncated direction to undergo the nonlinear test, and this design preserves that responsibility.

## 7. Exact-QP justification and its limits

For a fixed complete linear feasible set and exact global QP minimizers, lowering positive \(\mu\) cannot increase the optimal nonnegative \(\tau\). Add the optimality inequalities for
\[
 \frac12\tau^2+\frac12\mu^2\|w\|^2
\]
at the two damping values: the less regularized optimizer's norm cannot decrease, and its data term cannot increase. Nonnegative slack converts the squared statement to a statement about \(\tau\).

This is the previously recorded exact-QP comparison. It does not compare different working sets or current points, two incomplete64-advance answers, or true nonlinear geometries. It says nothing by itself about root-branch success, the complete raw lift, D, curvature or Phi.

The observed-agreement rule is therefore an explicit numerical continuation heuristic. Even after one agreeing accepted step, the next less regularized step can fail and must pass all original backtracking and geometry tests. The run20 refusal is evidence against a stronger claim, not a contradiction of the exact linear comparison.

If all accepted steps are backtracked, the selected start misses the full finite maximum, or prediction is poor, this policy makes no reduction. It does not force progress by suppressing those facts.

## 8. Complete module and minimum source changes

New module: `scripts/resume_20261126/fixed_fejer_restoration_damping_continuation.py`.

- Bytes: 18684.
- SHA256: `be523c77d488eaaaab9a18f6aa556283362f66bee0916f9d1489cd2b51c1b710`.
- Git blob: `05eb88969c5e83cf2f01fcb3f02e40f4cbea0775`.

APIs:

- `initialize_report(report)` attaches the full source-bound definition before first F.
- `decide(direction, *, model_identity_sha256, original_rule_next_damping, policy)` is nonmutating and reads scalar/list records.
- `after_original_update(direction, report, original_rule_next_damping)` appends the complete decision and returns next damping after the unchanged failure block.
- `validate_report(report, *, source_sha256)` purely reconstructs every reported completed decision and verifies the damping sequence.

The driver needs three exact insertions: one actual full-source role, report initialization, and a call after its unchanged original failure block. Against the whole99,313-byte parent they add451 bytes, giving99,764 bytes before explicit new basename/schema/source-identity updates. Textual inversion recovers the entire parent. No generated source was run or compiled.

The complete pure reader keeps every old check. Four short insertions append the stdlib validator dispatch, its result and the **full new decision in each original direction readout**. The projected whole size is99,751 bytes before new names/schema/driver pin; inversion recovers every original99,382 bytes. Existing geometry, domain, typed-row, root and13-member checkpoint checks remain.

The complete patch file is `computations/fixed-fejer-restoration-continuation-complete-integration-design.json`. It contains exact old/replacement strings, full parent identities, API contracts and remaining family-binding responsibilities. Root owns final new driver/launcher/reader generation, basenames, source registry and any public run. No final caller/source-family SHA, physical point or result is fabricated.

In an isolated branch, one policy role is added while preserving all137 old scientific roles and all18 old runtime responsibilities. Scientific lower bodies need not change. A downstream consumer that hard-pins an old driver must receive an explicit new family binding; old hashes are not relabeled.

## 9. Existing returned fields and observation boundaries

| Quantity | Existing location in one complete original direction |
| --- | --- |
| Actual damping | `actual_damping` |
| Full H2 step norm | `coordinate_step_norm` |
| Every physical selected value/gradient norm | `complete_selected_inequalities.rows[*].physical_g` / `gradient_coordinate_norm` |
| Complete row point | `complete_selected_inequalities.current_full_point_sha256` |
| Row model | `complete_selected_inequalities.source_binding.actual_model_identity_sha256` |
| Every full-step selected prediction | `selected_linear_physical_g[*]` |
| Maximum selected prediction | `maximum_selected_linear_physical_g` |
| Common slack | `computed_common_slack` |
| True starting violation | `old_actual_maximum_positive_physical_g` and `starting_geometry` |
| Accepted alpha/field | `accepted_alpha` and `accepted_geometry` |
| Actual finite QP outcome | `qp.status`, `qp.advances`, `qp.final_face_projected_gradient_norm`, `qp.maximum_linear_violation` |

The current observer's immutable completed-trial JSONs preserve alpha, phase, serial, returned statistics and six geometry scalars at the true trial point. They are not scientific checkpoints. They do not presently preserve the whole selected linear prediction or QP row-scale diagnostics. Unpublished values are not reconstructed from another point's mutable progress.

The new report retains all decision evidence, reasons and definition identity. Both complete selected lists remain in their original location; the new evidence hashes the complete lists rather than replacing them with a truncated list. Pure readout retains the full decision and reconstructs it. Any later display extension can use these already returned scalars, keeping the original48-field mapping in provenance.

## 10. Actual ordering and the wall-clock problem

The exact original order is:

| Site | Scientific sequence |
| --- | --- |
| Initial, lines874–881 | Residual, statistics, then geometry |
| Current parent, line910 | Geometry before complete row construction; current statistics already retained |
| Metric trial, lines1027–1036 | Residual/statistics; domain or Phi/Armijo rejection can skip geometry |
| Restoration trial, same lines | Residual/statistics; every domain-valid candidate reaches geometry irrespective of Phi |
| Final, lines1103–1105 | Geometry, then residual/statistics |

The nested `statistics` function does not itself call `q.residual`. Swapping only statistics and geometry while leaving residual first cannot remove an order1-to-order2 upgrade. A real reordering concerns the complete residual/statistics pair.

Metric early rejection is an actual behavior. Forcing a scan can spend previously unspent work and discover permanent locations on a candidate formerly never geometrically read. Restoration also has domain/root failure prefixes. Any geometry-first change must explicitly handle ordering, failure-prefix records, observer events and permanent-memory effects. Current/final sites already use geometry-first behavior. This delivery makes no ordering change.

The driver timer `full_geometry_and_row_preparation_seconds` starts after the loop's outer current-geometry scan and measures the full `build_rows` call, including its own scan and row construction. It does not include every preceding current scan. Trial `actual_seconds` includes residual, statistics, conditional geometry and bookkeeping. Closure-only counters do not measure the entire F/J/geometry workload.

The continuation policy adds no field work. It may use the existing outer allowance more effectively if the actual model predicts well; it does not prove completion within the350-minute platform window. Complete nonlinear trial cost is a separate constraint. The fixed-face algebra is not presented as a cure for it.

## 11. Concrete future execution and scope

A clean future algorithm comparison can use the original bhalf seed, profile fraction1/32, metric damping.01, restoration damping.01 and all original scientific parameters. The full90,652-byte19 science parameter file remains the numerical parent; the current complete later-peer binding preserves subsequent actual/unknown responsibilities. The only new algorithmic choice would be the declared restoration continuation.

No runner number, final source-family SHA, report, point, mean,13-member checkpoint or accepted field is assigned here. Root may choose a later independent run after closing the complete outer source family. The half-wave run22 and a geometry-first performance variant are not combined with this policy.

Evidence comes from the ordinary real run: actual complete selected prediction, alpha, QP diagnostics, true geometry decrease, next damping and complete natural report or honest failure. No replay fixture, benchmark, reduced-angle field, preflight or review step is added as a front door.

Known historical/peer responsibilities remain. This module does not invent a past final point or turn mutable progress into a restart. It does not alter the fixed target or pay any continuous metric, reach, curvature, R716/R722 or closed-surface error. The full scientific run must still produce and validate its own actual field.
