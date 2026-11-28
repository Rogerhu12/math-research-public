# Complete candidate: demanded rotation coefficients and same-branch second-angular frames

## 1. Status and exact purpose

This is a separate source candidate derived from the complete paired-halfwave curvature-cache family. It does not modify run 25, run 26, their parameters, the R725 cutoff, or any running job. No local scientific calculation, Python import, AST or fixture was performed. No numerical return, eligible-path frequency, equality measurement, speedup, accepted point, final checkpoint or continuous certificate is claimed.

There are two narrowly bounded changes. First, an original plain-detached caller that only consumes coefficient orders zero or zero-and-one no longer evaluates the unconsumed rotation-coefficient arrays. Second, when the original normal chain upgrades an actual complete order-one branch to order two, an optional path computes the six new second-angular frame columns and reuses each stage's own existing orders zero and one. The root chain already replaced those two newly computed lower rows with the old stage words. The new path preserves that replacement while also preserving the old finite-return boundary by the sufficient range proof in Sections 6–8.

The complete original analytic-frame and AD implementations remain present. Every ineligible, unknown or numerically unavailable second-only case goes through the original full frame and its original AD fallback. The range is an implementation eligibility condition, not a new admissible physical domain, root condition, solver acceptance rule, scientific preflight or reduced problem.

The current source family has 137 scientific roles and 19 current runtime files. Relative to the immediate run-25 source registry, 14 current role pairs change and 123 are identical. Seventeen runtime files are new; the complete reference calibration and the complete location observer are reused byte for byte. A runtime file count is not an argument count or a scientific role count.

## 2. Complete source provenance

The immediate complete parent is:

- computations/fixed-fejer-paired-halfwave-curvature-cache-current-runtime-binding.json: 51,709 bytes, SHA256 d449d0a54b69b23c598234a28fede12917473ce7058e9d8815ba8b524c6f869f, Git blob 38f781117d79710e72947cb8f8f0ecb258f0dabb.
- computations/fixed-fejer-paired-halfwave-curvature-cache-complete-entry-delivery.json: 30,196 bytes, SHA256 4679db9388bf966a353f07a3a95af138bc80542e1e10a3d8151909e8572c8e10, Git blob 421977ba260ad7b31215c268ecd17f0c8314fc80.

That whole parent records the paired-halfwave source family, complete original parameter files, history and external obligations. The older mathematical source family is computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json, 67,013 bytes, SHA256 6dd246a030ffaf9e58e750c135e26424b12668b182f0e6a59726c2af006c1638, blob 4f20af6e3663bdf69aca7193bc29624dc706411c, originally published at 7d34ebe278826c68a9e84c32179251220bf2fc3b.

The actual old normal is fixed_fejer_paired_halfwave_normal_lift.py, 96,271 bytes, SHA256 c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac, blob f285b87e4705b534935dab238d531be22af90740. Its complete base is b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6; its complete paired-halfwave seed is cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0. Neither mathematical source is changed here. In particular this is the R724 halfwave seed, not the distinct old full-wave or new R725 cutoff seed.

The new whole registry supplies exact complete records for every new runtime and all 137 source roles. A matching mathematical expression is never substituted for a whole-source identity. All original historical method/AST anchors continue to denote the actual historical files. The additional method-source overrides explicitly bind the two new normal wrappers; they do not relabel those wrappers as historical methods.

## 3. The original repeated work and what remains in its order

The complete original normal source selects roots by literal angle at one complete immutable free point. Its order-one-to-two upgrade takes the already selected order-one stage records. In each of the 32 stages it calls the frame producer for order two, then replaces frame angular orders zero and one with that stage's actual cached lower-frame words. It also anchors the old lower control words, retains the original selected eta/J3 state, computes the new second jet and verifies the anchored words.

Consequently, a newly computed complete order-two analytic frame normally contains 18 applications of the original total operator: six columns times three angular orders. On a legitimate upgrade, 12 of those totals contribute to lower frame rows that the original caller subsequently overwrites.

This is not a claim that all 32 stages incur a miss. The existing C1 cache may already reuse an identical complete previous-control input. The candidate only avoids the redundant lower work for actual eligible misses of the corresponding second-angular path. Existing full-frame cache hits remain full-frame hits. No factor-of-32 speedup follows.

All of the following stay in the complete original control flow and order:

- Every normal stage and its original equation, root selection, line search, domain test, residual and trace.
- The full previous-control and frame chain and the complete first-parameter J and J-transpose.
- Original forced residual rereads at each stage and at the final endpoint.
- The full point/domain checks, exact normal partition, literal angles and all grid/material queries.
- Statistics before geometry, every trial/acceptance decision, all solver budgets and the complete save/report sequence.
- Existing complete selected-row curvature pullbacks and their exact input cache semantics.

The complete driver suffix from the indented save_report definition to EOF is unchanged: 21,481 bytes, SHA256 d3396f3294750a1b607f8314545a44467a244c09e6a888a2d9f9c32db4599531. No geometry-first ordering change or adaptive restoration policy is introduced.

## 4. Demanded coefficient evaluation

Write q=|w|². The original base evaluates six functions A,B,Az,Bz,Azz,Bzz. It uses the same strict small branch q<1/4, the same clamped large-branch argument max(q,1/4), and the same degree-12 Horner expressions. The candidate helper repeats the exact consumed expression and arithmetic grouping.

The large-branch functions are:

\[
 A=\sin t/t,\quad B=(1-\cos t)/q_{\rm safe},\quad t=\sqrt{q_{\rm safe}},
\]
\[
 A_z=(t\cos t-\sin t)/(2t^3),\qquad
 B_z=(t\sin t-2(1-\cos t))/(2t^4),
\]
\[
 A_{zz}=(-t^2\sin t-3t\cos t+3\sin t)/(4t^5),
\]
\[
 B_{zz}=(t^2\cos t-5t\sin t+8(1-\cos t))/(4t^6).
\]

For derivative d and offset o=1,2, the original loop runs power k from 12 down through d and applies

\[
 h\leftarrow hq+
 \frac{(-1)^k\,k!/(k-d)!}{(2k+o)!}.
\]

No coefficient is rederived using a differently rounded series. This candidate does not replace the analytic frame's existing true polynomial derivatives. It only stops the original coefficient loop after the highest order its caller actually consumes.

The two changed normal call sites are exact:

1. _rotate consumes only A and B, so it requests maximum derivative zero.
2. _corrected_jets requests max(order, 1 if need_s else 0). Thus a radial derivative still requests Az/Bz even when the requested angular order is zero.

The six-slot interface is preserved. An uncomputed trailing slot is None. It is never a numerical zero, never a computed two-angle jet and never a substitute for a requested derivative. Order two always invokes the complete original six-array function.

The dispatcher checks the complete bound coefficient function object and uses the existing strict plain-detached environment checks. Reverse-mode activity, inference mode, forward dual/functorch/functional tracking, compilation/JIT, dispatch/function modes, autocast and unknown probe states use the original full path. The radial tensor must be a plain detached CPU float64 tensor with the original no-dual/known-version checks. Merely entering no_grad is insufficient. There is no coefficient-value cache and no retained graph.

The successfully completed Horner update counts per array-valued function invocation are exactly 26 for order zero, 50 for order one and 72 for the original full order-two call. These are recurrence updates on complete arrays, not scalar floating-operation counts. Failure accounting and partial calls are retained separately. No wall-time ratio follows from these counts.

## 5. Same-branch frame reuse, complete keys and original scope

The new C1 path is entered only by the already existing detached value scope. It does not fetch or upgrade roots. It reads the actual selected root-cache items and requires:

- A current order-two batch explicitly marked as a same-branch upgrade, with completed stage count zero at scope entry.
- The identical current full point, exact ordered literal phi hex words and normal stage count.
- Actual order-one entries for every angle, all 32 stage records, an original final endpoint check, and the full exact normal-node list.
- The same cache item objects still present at each stage.
- Read-only float64 stage arrays of the complete original shapes.
- Complete equality of the previous zero/first control words with that stage's actual old predecessor, or the exact initial zero words for stage zero.
- All original C1 data identity, point/model/source/method and stage-order checks.

A separate tail cache stores only the complete six second-angular columns, shape (angle_count,3,6). It is keyed by every word of the complete previous control jets, including all three angular slots. This is distinct from the old full-frame cache. Each return obtains the current stage's actual old lower frame rows and concatenates those rows with the new or cached second-angular tail. It cannot reuse another stage's lower rows merely because the tail key agrees.

The actual low-order frame words are checked finite by the original complete word-reading helper. Source identity and shape failures remain errors. Allocation/capacity/clone or numerical-unavailability cases use the original complete frame behavior. The tail and its private scope certificate are cleared when that C1 value scope closes. No active graph or cross-point cache is introduced.

The original normal caller still performs its own lower-row replacement and word anchoring after this return. Its _run_chain, _get_roots, _implicit_jet_value, _total and full residual/field/J interfaces are unchanged. The active C1 scope is a different original class and retains its full construction.

## 6. Why an additional finite-range argument is necessary

Simply deleting the two overwritten lower rows would be incomplete. The original analytic producer formed all three angular rows, checked the entire resulting frame for finiteness and could fall back to original AD if a discarded lower row was nonfinite. The fact that its caller later overwrote that row does not authorize suppressing that original failure boundary.

The new path therefore has an internal sufficient finite-arithmetic range. It proves that those omitted lower rows would have passed their original finite-return check. The actual computed second row retains its original finite check. Outside this sufficient range the original full producer, including all discarded-row computations and its fallback, executes.

The eligibility certificate is private to one current C1 scope. It requires plain detached CPU float64 data and binds the exact data object, producer object, six tensor objects, tensor versions, shapes, strides, storage offsets, dtype/device, current immutable point object and its bytes owner, point SHA, model object/identity, S, J, integration order, mesh/weight object identities and their complete actual bytes. All original C1 data-identity checks remain. The selected CPU float64 and Torch 2.5.1 source contracts are inherited, not widened.

The certificate does not trust a point hash alone. It separately records and rechecks actual mesh and weight words. Every second-only producer miss rechecks the scope and the complete previous-control bound. Stage/cache identity controls remain outside the numerical range proof.

The sufficient numerical conditions are:

| Quantity | Required actual bound |
|---|---|
| Every component of W, Wp, Wpp, T, Tp, Tpp | absolute value at most 4096=2^12 |
| Every previous control word, all 3 by 6 slots | absolute value at most 2^12 |
| Every actual Gauss weight | absolute value at most 2^12 |
| Every actual width from np.diff(mesh) | absolute value at most 2^12 |
| S | 2^-12 ≤ S ≤ 2^12 |
| N=(J−1) times integration_order | N ≤ 2^20 |
| Each of the six original coefficient arrays and six actual coefficient-derivative arrays | absolute value at most 2^704 |

The complete actual baseline has J=923 and integration order 8, hence N=922×8=7,376 integration points per angle. The bound 2^20 is not a selected quadrature size. It merely permits a sufficient finite-return proof; the actual full 7,376 points remain present. No angle count factor enters this radial reduction because each angle and Cartesian component is reduced separately.

The coefficient bound is checked on every actual returned array after executing the complete original coefficient and derivative formulas in the second-angular producer. NaN, infinity or an over-range value fails the inequality and invokes the original full path. This proof therefore does not assume a global bound for a rounded trigonometric function or extrapolate a Taylor polynomial.

## 7. Complete finite bound for the omitted rows

All bounds below are componentwise. Let B=2^12. The exact source contraction has six summands, not three: apply(W,u) is the original einsum over the six control columns. Therefore the rounded working contractions satisfy the deliberately loose bounds

\[
 |w|<2^{27},\qquad |w_\phi|<2^{28},\qquad
 |w_{\phi\phi}|<2^{29}.
\]

For example, the first contraction is bounded by six products B²; the second has two such contractions; the third has coefficients 1,2,1. Their sums are bounded respectively by 6,12,24 times 2^24. The displayed powers have strict slack for the finite number of binary64 multiplications and additions. For all subsequent estimates it is safe to use 2^29 for both w and w_phi.

Use the actual source abbreviations

\[
 C=w\times V,\quad D=w\times C,\quad
 C_\phi=w_\phi\times V+w\times V_\phi,\quad
 D_\phi=w_\phi\times C+w\times C_\phi,
\]

with V=T. For one control column let e=W[...,ell], e_phi=Wp[...,ell]. Denote its variation by d. A cross-product component has two products and one subtraction, while a dot product has three products. These exact operation counts and the foregoing bounds give:

| Actual intermediate | Sufficient absolute bound |
|---|---:|
| C | 2^42 |
| D | 2^72 |
| C_phi | 2^44 |
| D_phi | 2^75 |
| dq=2 w·e | 2^44 |
| d(q_phi)=2(e·w_phi+w·e_phi) | 2^45 |
| q_phi=2 w·w_phi | 2^62 |
| dC=e×V | 2^25 |
| dD=e×C+w×dC | 2^56 |
| dC_phi=e_phi×V+e×V_phi | 2^27 |
| dD_phi=e_phi×C+w_phi×dC+e×C_phi+w×dC_phi | 2^60 |

These are upper bounds for the original computation, not estimates of a physical derivative. In particular the bounds for C and D have unused slack from replacing the sharper w bound by 2^29.

By the checked coefficient bound:

\[
 |dA|,|dB|\le 2^{748},\qquad
 |A_\phi|,|B_\phi|\le2^{766},
\]
\[
 |dA_\phi|,|dB_\phi|\le2^{813}.
\]

The last line follows directly from the actual two terms
Azq*dq*q_phi + Az*d(q_phi), and its B analogue. Their exponents are at most 810 and 749; the stated 813 is deliberately larger and includes finite arithmetic slack.

The original order-zero frame integrand for each of the six columns is

\[
 dA\,C+A\,dC+dB\,D+B\,dD.
\]

Its four product bounds have exponents at most 790,729,820,760. The complete rounded sum is less than 2^825. The original order-one frame integrand is

\[
 dA_\phi C+A_\phi dC+dA C_\phi+A dC_\phi
 +dB_\phi D+B_\phi dD+dB D_\phi+B dD_\phi.
\]

Its eight product bounds have exponents at most 855,791,792,731,885,822,823,764. The complete rounded sum is less than 2^890. Every multiplication and intermediate addition in those two expressions is finite; no cancellation of infinities is used. We use the common, still looser bound 2^900 for either complete lower-order integrand.

For clarity about rounding: the inherited operation domain is finite CPU binary64 arithmetic. Taking the conservative relative rounding allowance u=2^-52, each fixed short dot/cross/product expression has fewer than a hundred elementary roundings. The strict slack between the exact term sums and the powers above exceeds their cumulative rounding allowance. Underflow can only contribute an absolute error at subnormal scale; that is also contained in these deliberately very large absolute bounds. This is a finite-arithmetic argument, not a certified enclosure for the field value or its derivative error.

The original _total is preserved verbatim:

~~~
block = value.reshape(J-1, integration_order, angle_count, 3)
widths = tensor(np.diff(mesh))
cell_total = (block*tensor(gauss_w)[None,:,None,None]).sum(1) \
             * widths[:,None,None]
return torch.cumsum(cell_total,0)[-1]
~~~

The frame column then divides that result by S. Thus, before rounding allowances, the absolute bound is

\[
 N\,2^{900}\,2^{12}\,2^{12}\,2^{12}\le 2^{956}.
\]

Here the factors are the true number N of radial summands, the integrand, the actual Gauss weight, the actual cell width, and 1/S. The two reductions do not multiply the number of terms to N². If a=J−1 and b=integration_order, the reduction paths have at most a+b fixed-addition depth, with a+b≤ab+1=N+1.

Even using the conservative bound of 2^20+1 dependent additions, the accumulated factor (1+u)^(2^20+1) is below 2. The finite number of outer products and the final division adds a factor below 2. Allowing a total factor 16 is therefore conservative, so every resulting lower-order column is bounded by 2^960. Every intermediate absolute partial sum is bounded by the same absolute-sum argument. This remains far below binary64 overflow near 2^1024.

The checked ranges therefore prove that the original omitted lower-frame components and all their original total-reduction intermediates are finite. We do not merely observe that the final stored old lower frame is finite. Both facts are used: the proof preserves the old producer's discarded-row finite boundary, and the actual old-word checks preserve what the original caller ultimately returns.

## 8. The computed second row, hard errors and all fallback boundaries

The new _analytic_second is copied from the complete original _analytic body. It computes the same w,w_phi,w_phiphi; q,q_phi,q_phiphi; six original coefficient values; six actual coefficient derivatives; all C/D jets; and all variations needed for the second angular row. For each of six columns, the original full second-angular integrand and original _total/S grouping are retained. The six resulting columns are stacked in their original order.

Only the completed order-zero/order-one derivative arrays and their 12 total reductions are omitted. Intermediate first derivatives needed by the second row are still computed; this is not a truncated second derivative.

Original boundaries retained or accounted for are:

1. _arguments checks the complete six-column previous-control shape, full current model/methods/partition, all needed W and T jets, all core/cap/reference endpoints and all reference integration jets. Source/shape/complete-input failures remain errors.
2. The coefficient functions and their derivative functions execute normally. A nonfinite or over-range coefficient gives an unavailable optional path and the original complete producer.
3. Section 7 proves that the omitted lower-row finite check cannot fail inside the eligible range.
4. The actual six new second-angular columns retain the original complete finite check and shape check.
5. Each reused stage lower row is an actual finite complete word array, not a synthesized value.
6. The original normal caller still applies its original assembly, anchored-control checks, root/stage residual checks, trace and final endpoint reread.
7. Arithmetic, numerical unavailability or allocation failure in the second-only calculation returns to the original complete C1 value production, including the original analytic-to-AD fallback. No zero tail or partial frame is returned as a completed frame.
8. A full-frame cache hit still has its original semantics. A second-tail hit requires the original C1 same-data/same-model/same-point/same-stage checks and per-stage actual lower-row binding; it does not increment an original integral count.
9. The original full analytic and AD bodies are retained. Active/unknown computation does not use the demanded detached rotation path or this detached branch-upgrade cache.

The optional certificate and its finite range do not prove a continuous root branch, uniqueness outside the existing discrete chain, a quadrature error, a norm bound for the physical field, or an accepted trial. Memory allocation and exception timing can differ because some arrays are no longer allocated and additional bookkeeping is present; no promise of identical out-of-memory scheduling is made.

## 9. Active derivatives and unchanged source methods

The candidate does not detach an active upstream point, reference, previous frame or previous control. The original active frame scope and original first-parameter implicit construction stay intact. Requests with active or unknown tracking use all six original coefficient arrays. The original numerical root iteration is still not differentiated; all original implicit equations and upstream edges remain.

The normal implementation changes only the _rotate and _corrected_jets dispatch calls. Its other scientific methods, including the complete stage/root/implicit chain, remain byte for byte. The previous complete normal method registry is retained, with the two exact new method bodies explicitly added to the source-override maps where the original guards require them.

The original normal schema is retained because its data/constructor contract is unchanged. The actual whole normal source, policy definitions, method identities, and therefore working model identity are explicitly new. No old report or checkpoint is made current by sharing a schema name.

The packet registry adds an explicit new source entry and binds the four new second-angular producer methods for that entry. Every old registry entry remains. Packet capture still reads only actual existing roots/jet orders, never asks for an upgrade, and keeps original complete point/order/angle/provenance identities. No cached first-order placeholder is relabelled as a computed second jet.

## 10. Work removed, work added and what is not known

For one successful demanded coefficient call, order zero evaluates two arrays instead of six; order one evaluates four arrays instead of six. Both retain the original formulas. Degree two, active and unknown requests retain the original six. The counted 26/50/72 recurrence updates are complete-array loop operations. They are not hardware operation counts and do not establish a runtime ratio.

For one eligible second-only producer miss, the six original second-angular totals remain; 12 lower totals and their completed lower integrand arrays are not evaluated. There may be far fewer such misses than stages because the original C1 cache already reuses identical control words. A hit in the new tail cache avoids another complete tail calculation but still binds and assembles each stage's own lower rows.

New cost includes the private range certificate, six complete static-array bound scans per eligible scope, repeated actual mesh/weight bytes checks, all previous control words, actual coefficient bound scans, source/method/data checks, scalar bookkeeping, and tail clone/assembly. These are not free. The existing original C1, meridian and closure guards are not removed to compensate. Capacity and allocation fallbacks remain. No estimate of net acceleration is justified without an actual full public Actions execution.

This candidate affects repeated normal frame and coefficient evaluation, including real field evaluations. The already published curvature dk cache remains a separate optimization normally exercised during selected build_rows calls. Neither that dk cache nor the present source inspection establishes which component dominates a particular observed trial.

## 11. Actual counters, own-point metadata and pure consumption

No reused value is counted as an original integral. The meridian helper retains all its old counters and adds separate rotation request/order/original/demand/success/failure/array/recurrence counters. Its last_rotation_call records its own point and actual returned or failed state; uncomputed slots are explicit.

The analytic-frame helper retains its old complete-frame and AD counts and separately records second_* scope eligibility, attempts, actual six-column totals, partial failures and returned angle vectors. Its actual_counts and last_second_call are distinct from its old full-frame counts and last_call.

The C1 actual_counts and last_value_scope retain separate second-tail requests, producer returns, cache hits, numerical failures, binding bypasses and actual reused lower angle frames. Per-stage records contain the own point, complete previous-control word SHA, actual old lower-frame SHA, original lower orders and new order. A closed or partially failed scope is not a declaration that a full normal chain succeeded.

The new small complete source-binding module reads the full actual operator metadata at each record's own point. Its pure output appears under:

~~~
analytic_stage_jacobian.same_branch_second_angular_frame_reuse
    .complete_own_point_metadata_records
    .latest_actual_diagnostics
~~~

It does not fill any of the existing 38 root snapshots from the latest record. A snapshot that never contained C1 diagnostics does not acquire them. Full source and policy identities, counts and per-record point attribution are validated using standard-library extraction, without importing Torch or recomputing a field.

The complete reader adds the actual analytic-frame source constant to its C1 pure namespace and retains its previous checks and full output. Its current file is 99,827 bytes. No validator was removed to stay below the size limit.

## 12. Minimal complete source propagation

The 17 complete new runtime files are necessary because existing guards bind whole source bytes:

- Nine lower files: the meridian and frame/C1 implementations; the two small normal wrapper calls; exact full-method override propagation through closure/J3 and stage/adjacent sources; and the explicit packet registry.
- The complete curvature selector changes only its two actual normal/meridian whole pins. It is not broadened to accept arbitrary models.
- The complete source binding, geometry, pure geometry binding and history transfer preserve their original scientific and history bodies while binding the actual new sources and consuming new diagnostics.
- Driver, launcher and reader propagate exact current whole identities. The complete driver scientific suffix and original numerical order are unchanged.

The reference calibration, root-owned location observer, base, reference, seed, frozen Q, mathematical target, layouts, full free coordinates, complete angular/radial domains and all remaining registered dependencies are the actual unchanged original files. Current pairs are distinguished from historical aliases. No global replacement changes an old peer source into this new driver.

## 13. Whole source reconstruction and exact parent recovery

Two complete Node text reproducers are supplied:

1. reproduce_fixed_fejer_halfwave_demanded_lower.mjs: constructs nine complete lower files and the complete selector from their exact whole parents.
2. reproduce_fixed_fejer_halfwave_demanded_upper.mjs: constructs seven complete upper files from their exact whole parents.

Both take --source-directory and --generated-directory. The source directory may contain the exact basenames directly or the complete repository/topic paths. Every input is whole-size/SHA checked before use. Every output is the complete file, whole-size/SHA checked, below 100,000 bytes. Existing different output files are preserved by an explicit error. No generated Python source is imported or executed.

Example commands, to be used only as source reconstruction, are:

~~~
node scripts/resume_20261126/reproduce_fixed_fejer_halfwave_demanded_lower.mjs \
  --source-directory /path/to/complete/checkout --generated-directory /path/to/new/sources
node scripts/resume_20261126/reproduce_fixed_fejer_halfwave_demanded_upper.mjs \
  --source-directory /path/to/complete/checkout --generated-directory /path/to/new/sources
~~~

The lower reproducer contains all literal new bodies and exact insertion rules, not a compressed substitute for the full published runtime. It explicitly reconstructs complete method-override maps from original maps plus the two full new wrapper bodies. Packet history is preserved by adding one actual entry. The upper reproducer includes all exact old/new patches and verifies the whole inverse text equals every original parent.

During construction, pure JavaScript string replay reproduced all ten lower/selector texts exactly. All seven upper texts reproduced exactly forward and inverse. Primary lower body patches were also checked with their complete original text and exact scope. This is evidence about source reconstruction only; no AST, fixture, module import, physical evaluation or numerical equivalence experiment was run. The complete original Git blob identities also recover each parent byte for byte independently of source replay.

## 14. Parameters, history, scope and subsequent execution

The intended isolated namespace is fixed-fejer-paired-halfwave-demanded-bhalf-first. No new run is assigned in this delivery. The parameter parent remains the complete halfwave b/S=1/2, profile delta=1/32, metric damping .01, restoration damping .01 configuration, all 157 science argument words, seven pure words, original formal projections and original full budgets. Root owns any later queue, controller and parameter adaptation. No numerical argument is silently supplied by this note.

The inherited runtime budgets include M160, J923, N2048, all32 normal stages, normal angle block8, integration8, stageblock64, metric directions1/maxiter16, restoration directions4/maxiter64, line trials15, all192 active rows and32 near-active rows. All other words remain in the exact complete parameter files; this list is explanatory rather than a substitute for those files.

Existing five pending-peer CLI pairs, complete external obligations, all historical files and typed provenance remain in the whole parameter parent. Unknown accepted/final/typed histories are not replaced by empty lists. A same-source restart still requires this actual new driver's complete own report and complete 13-member final checkpoint; mutable progress, an initial file, another model's packet or a similar mathematical target is insufficient.

Accurate downstream fees, mesh and closed-surface consumers must continue to bind their actual current source family. This source candidate does not silently expand an old fee reader's hard pins. No numerical fee result is fabricated from unchanged mathematics. If root later adopts this candidate, source compatibility for such consumers remains an explicit separate source adaptation using actual whole reports and immutable points.

All candidate actual execution fields are null: run/input/model/point/report/final hashes, accepted/typed history, eligibility/hit counts, finite geometry values and timing. Actual observations from run25 do not become observations of this new source family.

## 15. Complete new runtime records

All paths except the selector are under scripts/resume_20261126; the selector is under scripts/resume_20261120. The delivery manifest and current-runtime binding give full repository paths. Every row below denotes a complete text blob, not an extract or patch.

| Role | Complete basename | Bytes | SHA256 | Git blob |
|---|---|---:|---|---|
| closure_values | fixed_fejer_paired_halfwave_demanded_closure_values.py | 61790 | 2440622a82f1da79ccba468fbcf9e3e2dbc36762df63550e8de4bfb85a1d10b6 | dde6812a1a05594d95b1e7ecf99694c86b2be10d |
| analytic_J3 | fixed_fejer_paired_halfwave_demanded_stage_jacobian.py | 27993 | 7909d5781488131fd94c6389c85b24a235665484c2d5734e2df2db0584619b2d | d3ab5c40142fd15af8f1a4ec66a5ce5e9732f09f |
| analytic_frame | fixed_fejer_paired_halfwave_demanded_angular_frame.py | 68761 | 477a501d3eb8a367687e6b40e8a58136ec2f9d11a28325e38b01a4455b85b285 | e9987f8c303ad38287cf97efea4f5b140bf5793c |
| frame_C1 | fixed_fejer_paired_halfwave_demanded_frame_c1.py | 55173 | b185062a817df8e99602fa8aaab0ddd67a50d9938dc044b436ebbd94d7bfa6b1 | 3cdda2bc48a54337761b9322c218ffcb688d833d |
| stage_matrices | fixed_fejer_paired_halfwave_demanded_stage_matrices.py | 61280 | e69a10e54239b02317cbc3b813ee90af91c2d3ddb9144ab3f1ea81dc9c08c83d | 70d3f4e8f41edf35eaa87270ab9f0df52fad4031 |
| adjacent_matrices | fixed_fejer_paired_halfwave_demanded_adjacent_matrices.py | 36766 | 6c466f2c4dccd158b3eca16eb7f020b935ee22824327f94e15e01a66647d5166 | 130a240ed1d44a3624fa0715b2a7409eccbbfc4a |
| detached_meridian_values | fixed_fejer_paired_halfwave_demanded_meridian_values.py | 52317 | 26fa4aa15bb9fd2a9aa95e0e0e6f3a300628da77c189340a9e5ce4f23d04df55 | c20c8fa717c30e3f516f091a50f6b4294ae57c67 |
| endpoint | fixed_fejer_paired_halfwave_demanded_normal_lift.py | 96366 | fbb17bbce55d6d100eeaa14cf29438ec00538b216d9a2aecb314d2376b44aee0 | f1c014aaa4a3c44f8c8f84b41742ef4d44bdc35a |
| root_packets | fixed_fejer_paired_halfwave_demanded_root_packets.py | 75271 | fe555d2149c5cb1e919f51709da68098df3ad5960fabd87569802c1eb477e83f | ccdb56a3e117f616748f8c94ce725eb81962763b |
| geometry_selector | fullclosed_point_inequalities_v2_halfwave_demanded_curvature_cache.py | 35982 | b7293b63eb21af56bb15770e7afd12fa86988bf0c14719959155a3341c085497 | df0ad3f36a1850bb16f87d7d45f3e55efb5491d2 |
| analytic_J3_binding | fixed_fejer_halfwave_demanded_source_binding.py | 43489 | 2cbb44badea88db3d4d36422b12da70fb7d5f028626e268d06a87bdbe06a2c30 | bfb96cbb9d6d67a1e7adf5a3a56e85bce7ba1781 |
| geometry | so3_fixed_fejer_halfwave_demanded_geometry.py | 88482 | 8cde4d7c8c3699b870de0395386eaf4327572eb44bb9f5dfe3ea143c21425ace | 68eb933352259f594793da2ee827d8c121b316c1 |
| batched_geometry_binding | fixed_fejer_halfwave_demanded_geometry_binding.py | 20550 | 3d5f761fee10105bd0bc6d1a4056891e80b8b4b640aa13536f926c05b7bfc1d0 | 07d3b873206f224fd897b0dd1d4d925e9ae1cce8 |
| envelope_transfer | fixed_fejer_halfwave_demanded_memory_transfer.py | 78922 | cfa6b64463fdf5ad450c31651f97101fd16944f507b5c8c1b9e922065521d0d9 | 8202375d58ef2a501bf88258a9d4c00f68fa5ea4 |
| driver | fullclosed_fixed_fejer_halfwave_demanded_qp.py | 99473 | d1c99f555e480a0b37fcefee98e1261033bed0b4bb6a7f681f8da345e5ae46ab | aa926d084b5cf081e740b543789db18925578bcf |
| launcher | launch_fixed_fejer_halfwave_demanded_actions.py | 22125 | 2a94d33f37356be25fbed93b79b85b4664490b464d7d5fb5acb3edb13db3e22b | 1c8c151a26c551a8657021145b0cd35d7a2608dd |
| reader | read_fixed_fejer_halfwave_demanded_report.py | 99827 | 8631ae6ba1b20480465b96d2c4b71c419253a736e24ecba9cae967d01cb955d2 | 128b22b3cd2673b8aa9babb8c55e1a7f36927b96 |

The complete unchanged source registry and parent history are available through the exact whole parent records in Section 2 and the new complete runtime binding. Source construction, ordinary publication and actual scientific execution remain different states.
