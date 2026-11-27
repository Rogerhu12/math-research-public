# Full restoration scale and the independent mu = .001 branch

This note identifies the actual optimization phase and its numerical scale from the complete published source. It specifies one independent full-budget parameter branch. It does not change the running bhalf branch, identify an unobserved cause of its behavior, or claim a better field.

## 1. The small Phi change is not a metric-LM result

The earlier accepted finite-screen observation still has positive physical violation. In the actual driver, the phase is metric only when geometric_feasible is true: the complete screen has passed and max(0, maximum_physical_g) is zero. Every strictly positive finite-screen violation forces restoration. An undefined violation stops that attempt without inventing a linearization. This is a finite-screen rule, not a continuous certificate.

During restoration, Phi and all original metric rows are genuinely evaluated at every candidate, and positive relative E and determinant are required. But the QP and acceptance condition do not minimize Phi. Phi may even increase in an accepted restoration. A small incidental Phi decrease is therefore not evidence about metric-phase LM efficiency.

A small positive-g decrease is meaningful but does not distinguish a small computed direction, a backtracked direction, an inexact QP or a weak H2 direction. No unobserved accepted alpha, QP status, direction norm or row-gradient scale is supplied here.

## 2. Exact complete source attribution

These complete bounded text sources were read and bound by whole SHA256. Every file is below 100,000 bytes. The statements below refer to these bodies, not similarly named predecessors.

| Role | Complete source path | Bytes | SHA256 | Git blob |
| --- | --- | ---: | --- | --- |
| driver | `topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py` | 99313 | `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f` | `8bba3e30bb8e843fd725a2d19f8966b984acc4ae` |
| scalar_progress | `topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_trial_progress.py` | 39500 | `321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5` | `8173d3576958dc5c476466dd4c5012c5ed81b0c1` |
| geometry | `topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py` | 88163 | `5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135` | `c5325d3da8329547ad81e74a5da479323bfccd21` |
| qp | `topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullspace_feasible_active_cg_v3.py` | 26947 | `fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4` | `fabfcd7556a634d19e8dac788d5cb95d696b3d5d` |
| meridian | `topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py` | 40840 | `552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3` | `1d9e435bb68374b71c3d7361771c28f47838d59e` |
| endpoint | `topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py` | 96276 | `76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d` | `fc51c16b6dbd53abf04fe9175e5421f77e25c49c` |

The principal driver functions are CommonSlackRows.__init__, main and its physical_violation, geometric_feasible, statistics, scan and save_report closures. The linear-QP body is solve, including its final literal residual and KKT diagnostics. Coordinate scaling comes from the entire RotationH2Coordinates class. The normal-domain statement comes from EndpointPolicy and _inside_domain. The observation statement comes from Recorder.observe, _preserve_completed_trial, snapshot and report_snapshot.

No local scientific evaluation, Python import, AST/compile, benchmark or fixture was used. The work is source reading, algebra and complete metadata/parameter construction.

## 3. The exact restoration QP and its units

Write z for the full original whitened physical-coordinate step, d for the scalar common-slack increment, a_i = dg_i[T] for a full coordinate gradient, and g_i for its actual signed physical margin. The initialization is

\[
 \tau_0=\max(0,\max_i g_i)+\text{declared small positive slack padding}.
\]

The full augmented QP is

\[
 \min_{z,d}\ \frac12(\tau_0+d)^2+
       \frac{\mu_{\rm r}^2}{2}(\|z\|^2+d^2),
 \qquad
 g_i+a_i z\le\tau_0+d\quad\text{for every selected typed row},
 \qquad\tau_0+d\ge0.
\]

The objective is explicitly recorded by CommonSlackRows. The wrapper supplies the one-row operator A(z,d)=d and residual tau0 to the original QPv3. That solver forms mu2 = float(damping)**2. Thus .01 is a damping amplitude, and the regularization coefficient is 10^-4.

Row normalization does not erase this scale. The wrapper restores each old row's original positive scale, then divides the augmented row and its bound by sqrt(|a_i|^2+1). This preserves the physical inequality and the one common tau. Zero-gradient rows and the nonnegative-tau row remain.

The complete selected prefix, amplitude rows and typed-envelope rows remain in the QP. This is not a linearization of every continuous constraint. Nonlinear candidates still undergo the complete original finite grid and permanent-address screen. All full physical coordinates remain; the common slack is one additional variable.

## 4. The H2 coordinate scale is not a displacement radius

The current command selects jet-sum, radial length .05 and angular transition 24. The complete coordinate implementation uses Voronoi node masses w_j and angular factors

\[
 \sigma_m=\sqrt{1+(\nu_m/24)^2}.
\]

Its declared positive node-jet norm is

\[
 \sum_{j,m}w_j\sigma_m^2
  (\omega_{jm}^2+\ell^2\omega_{s,jm}^2+\ell^4\omega_{ss,jm}^2)
 +\sum_{\mathrm{free\ core}\ m}((1-\nu_m^2)dc_m)^2+dH^2,
 \qquad\ell=.05.
\]

The source explicitly distinguishes this from the integrated polynomial Sobolev norm. Lift and transpose retain every recorded diagonal/mode/core scale. The new branch keeps this same norm and every variable.

Consequently mu=.01 is not an unweighted coefficient limit or physical displacement radius. It must be interpreted relative to the actual full coordinate gradients and active face. The row metadata gradient_coordinate_norm records that scale; it has not been inferred from the public value of g.

The endpoint-control-radius argument 2 is not an outer trust radius for z. It is passed to EndpointPolicy, whose actual domain is |u_i|<2 for the six normal controls at every stage and accepted Newton trial. The policy explicitly imposes no normal-increment radius. The outer candidate remains x+alpha*Tz and must pass all original field/root/domain checks.

Metric-phase damping has a different data residual: main scales the complete positive-residual Hessian with sqrt(k/(scale^2*normalizer)). The same printed .01 has no automatic equal strength across that objective and the one-row restoration objective.

## 5. Original acceptance, damping updates and budgets

Outer trials start with alpha=1 and halve after rejection, for up to 15 complete trial evaluations. Every candidate pays the complete residual and statistics. During restoration, a nonsingular relative metric causes the complete geometry to be read even if Phi did not decrease.

The exact restoration acceptance requires the original domain checks, a defined complete true geometry, and

\[
 G_{\rm trial}<G_{\rm old},\qquad
 G_{\rm trial}\le(1-10^{-4}\alpha)G_{\rm old}.
\]

Here G is the nonnegative true finite-screen physical violation, not the linear common slack. This weak sufficient-decrease coefficient permits small improvements. It does not reveal alpha from an observed change.

After accepted restoration, restoration_damping stays unchanged. Only an entire direction with every allowed trial rejected multiplies it by four. The metric branch alone has its existing actual/full-prediction ratio and success-based damping halving. That metric rule is not invoked because a restoration happened to lower Phi.

The current budgets remain one metric direction, four restoration directions, 16 inner advances for metric, 64 for restoration, and 15 line trials. Both accepted and rejected restoration directions consume that outer restoration budget. A positive violation at budget exhaustion remains an honest finite-budget termination.

QPv3 is truncated. Its tolerance is atol + rtol*initial_gradient_norm, with actual selected atol=0 and rtol=1e-6. Its complete report records active-set/rank/feasibility/sign outcomes and pays a literal final linear residual and transpose. A return at 64 advances is not automatically an exact minimizer.

## 6. Precise comparison supporting the chosen direction

The new independent branch changes only initial restoration damping .01 to .001. The regularization coefficient changes from 10^-4 to 10^-6. Metric damping stays .01.

The comparison below assumes one fixed complete linear feasible set, the same tau0 and coordinate norm, and exact global QP minimizers. Define

\[
 F(z,d)=\tfrac12(\tau_0+d)^2,\qquad
 R(z,d)=\tfrac12(\|z\|^2+d^2).
\]

For 0<lambda_L<lambda_H, let p_L and p_H minimize F+lambda_L R and F+lambda_H R over that same feasible set. Minimality gives

\[
 F(p_L)+\lambda_LR(p_L)\le F(p_H)+\lambda_LR(p_H),
\]
\[
 F(p_H)+\lambda_HR(p_H)\le F(p_L)+\lambda_HR(p_L).
\]

Adding shows R(p_H)<=R(p_L). The first inequality then yields F(p_L)<=F(p_H). Because the augmented constraints require tau0+d>=0,

\[
 \tau(p_L)\le\tau(p_H).
\]

This is the supported direction: weaker regularization cannot increase the best exact nonnegative common slack of an unchanged QP. It puts less cost on moving the complete physical coordinate and slack.

It is not a comparison theorem for the actual 64-advance truncated algorithm, different points or working sets, floating-point conditioning, nonlinear full-grid g, root success, accepted alpha, Phi, wall time or final geometry. Larger steps may require more backtracking or fail original domain checks. All those checks remain.

For a purely algebraic illustration with one active row a of norm n>0, tau0=g>0, no padding and no other constraints, the exact active optimum is

\[
 d=-\frac{g n^2}{\mu^2+(1+\mu^2)n^2},\qquad
 z=-\frac{g a^\top}{\mu^2+(1+\mu^2)n^2}.
\]

This exposes the relative scale n versus mu. Strong regularization is a possible explanation when n is much smaller than mu, but not an assertion about the actual unobserved n. This formula is not a numerical fixture and was not used to invent a direction or field result.

## 7. Actual diagnostics already available in the source

For each completed direction, the original driver records phase, actual_damping, augmented coordinate_step_norm, every selected row and its gradient_coordinate_norm, and the complete QP report. It also records computed_common_slack, all selected_linear_physical_g values, their maximum, every actual trial alpha/statistics/geometry/error, and accepted_alpha with the genuine checkpoint if accepted.

Useful actual QP fields are status, advances, gradient_tolerance, final_face_projected_gradient_norm, maximum_linear_violation, multipliers, active face, inner history and transitions. The restoration coordinate_step_norm includes the slack increment; it is not silently the physical-z norm alone.

The unchanged observer preserves each returned decision in last_completed_trial and a bounded scalar file, with its own point, phase, serial, index, alpha, statistics, geometry and time. A new trial start does not erase that completed record. No extra F/J/root call is needed.

The current live projection contains six normal and 42 mathematical fields. Alpha, QP status and row-gradient norms are not among those live fields. The formal summary includes actual_mathematical_observation.last_completed_trial.alpha; the entire returned trial scalar contains more than the live projection. Missing values cannot be inferred from another point.

The full direction is appended to the report after its trial loop and original bookkeeping. A trial-start or trial-statistics live event alone therefore does not prove the whole direction record has already been serialized. This branch changes neither observation order nor scientific work.

## 8. Full independent run20 parameters

Namespace: fixed-fejer-meridian-batched-bhalf-mu001-first. Run19's source and queue stay unchanged. The two complete published run19 parameter files and its complete display correspondence are the direct parents.

Only scientific argv positions 37 and 71 change:

| Zero-based position | Parent | New |
| --- | --- | --- |
| 37, after --restoration-damping | .01 | .001 |
| 71, after --outdir | {work}/fixed-fejer-meridian-batched-bhalf-first | {work}/fixed-fejer-meridian-batched-bhalf-mu001-first |

All 157 science argv words and seven pure argv words remain. The pure report/output paths follow the new namespace. All 458 science formal selectors, 445 pure formal selectors and 48 live selectors are retained. The full preceding display history, failed-entry provenance, five original supported pending-peer CLI pairs and all external unknown histories remain. Actual run19 is added as external unknown whole history; it is not imported as typed rows, field values or a final seed.

The runtime remains complete 10fa/8027/f600 with 137 roles and 18 runtime files. No runtime source or formula is changed. The new runner constructs its own two necessary reference inputs and starts independently; it does not require a different solver's final report.

| Role | Complete file | Bytes | SHA256 | Git blob |
| --- | --- | ---: | --- | --- |
| science | `computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json` | 97019 | `89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca` | `598b4cdf62021a66b54c22b71171722027f1c0b5` |
| pure | `computations/fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json` | 86221 | `f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64` | `53655fce8344040770e02295898a1c4ae9a06ebf` |
| display | `computations/fixed-fejer-meridian-bhalf-mu001-complete-display-correspondence.json` | 32429 | `1fef7603002bdfbac58623b1d7c8b1cd0492d050f42c22acfd1ce11c3597278e` | `c89b5f4796e3c98a692f2704da6679df29aa39df` |
| reproducer | `scripts/resume_20261126/reproduce_fixed_fejer_bhalf_mu001_complete_parameters.mjs` | 15064 | `acd5d19439d9a6b00216bb6bfee2fab46087356a3580b97b946961fb6e83daa9` | `bdfb26059231d5f2b242d24d503c0ba36612d694` |

The ready files use complete compact JSON solely to keep each file below 100,000 bytes. No field, parameter or selector is removed. Their two complete step objects together occupy 103,956 compact bytes, so they must not be silently placed in a controller queue below that size. Root may queue science first, then archive its whole returned object and append the complete pure step. That schedules existing work; it does not introduce a mathematical gate.

The complete text constructor reads the three full hashed parents and emits both entire ready files and display. Every changed current metadata field is preserved separately as original parent history. No refs, queues, jobs, scientific array or current running parameter are changed by this package.

All new-run input/model/point/checkpoint/fee identities remain null until actual output. The comparison theorem is a reason for the selected parameter direction, not its measured outcome. The actual bhalf run19 continues at its original .01 restoration damping.
