# R278 candidate: actual approximate p3 roots with a two-coordinate outer model

Date: 2026-11-15. Author: ChatGPT / amplitude.

**Status.** Independent source and interface prepared for one public Actions request. No new equation, Jacobian, inner root, direction, finite difference, interval enclosure or optimizer has been evaluated during this preparation. Original source files remain unchanged. This is a new candidate algorithm; it is not the frozen `ec9` resume algorithm under another label, a BVP acceptance gate, or a claimed nonzero parent.

## 1. Motivation and exact input identity

[Actual90](2026-11-15-actual-request90-smaller-damping-backtracking-and-third-defect-growth.md) completed eight accepted directions with explicit damping `0.01`, but needed 48 original trial records and 40 rejections. Its original third unit defect ended at `14843.921358477846`, and its complete three-equation candidate remained unsolved. The final saved original parameter Jacobian has `J33 = -72000128.47538549`. This is a finite nonzero partial at a point whose third defect is not zero. It neither supplies an inner root nor proves the hypotheses of [R278, §6](../results/R278-finite-resonance-projective-normalization-and-local-elimination.md).

The new source starts from that real final parameter triple:

```json
[0.04241436079648833, 0.02766947731512731, -0.10800335072481342]
```

The actual90 parent is the complete original `small-core-damped-resume/damped-resume-status.json`, 60,951 bytes, SHA-256:

```text
5a4d157aa0bcada3cdd1d319adb419f23b94f52bfc1c945a3c6afe1207cb2f5a
```

Its published path is `notes/public-actions-43670368504-1-smallcoreresonance/small-core-damped-resume/damped-resume-status.json`. The new entry reads all parent bytes, verifies their identity and copies them unchanged. Only `final.parameters` become the initial guess. It computes a fresh original model and description; it does not relabel the parent Jacobian, merit, field or finite-difference report as current output.

The first-parent schema must be the exact frozen `ec9` schema and the above decoded bytes. Transparent gzip is supported: the CLI SHA is the hash of the actual supplied bytes, and the uncompressed size/SHA is separately checked against actual90. Later invocations can consume this exact new producer's own completed schema, with its complete source closure, original four input identities and declared last-accepted-point semantics intact. This support does not authorize or execute an additional invocation.

## 2. Frozen entry, reused sources and dependencies

| File | Bytes | SHA-256 |
|---|---:|---|
| `geometry_20261115_small_core_p3_inner_root_search.py` | 43,598 | `3b48efd71eb696fef66acbe7fbd163bb8dc8ca63287bfa8c4e873a2600fbf9d9` |
| Original model/checks: `geometry_20261114_small_core_resonance.py` | 25,799 | `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` |
| Parent resume provenance: `geometry_20261115_small_core_damped_resume.py` | 15,452 | `ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a` |
| Parent direction provenance: `geometry_20261115_small_core_damped_search.py` | 13,733 | `1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728` |

The new entry imports the pinned original `3b9` model directly. It calls its original `CircleReference.evaluate`, `jacobian`, `description`, `scalar_spec`, `scalar_domain` and `complete_reference_check`. The old `ec9` and `1691` files are retained and checked as actual-parent provenance. Their three-coordinate direction loop is not executed or monkey-patched into the new two-coordinate algorithm.

The source itself pins the original eleven consumed mathematical/provenance files and records those eleven plus its own actual SHA. The Actions workflow retains all original 70 source pins, adds this one source, and keeps the original 78-file public-source restoration. Four original mathematical files are unchanged:

| Input | SHA-256 |
|---|---|
| Accepted96 source | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| Original prepared112 mesh/profile | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| Actual full T112 zero slope-J anchor | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| Actual T112 native configuration | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

Runtime is the existing Python `3.12.14`, NumPy `2.3.5`, SciPy `1.17.0`, python-flint `0.9.0`, with BLAS/OpenMP threads fixed to one. No mathematical package or source is imported by the new entry until its public repository Actions guard passes. The complete computations directory and the original public-source restoration are required; the latter does not replace the topic's independently pinned local scalar sources.

## 3. Inner scalar probes and honest failure

Write the original unit equations as $d(p)=(d_1,d_2,d_3)$ and their original full parameter Jacobian as $J$. The diagnostic still consumes all entries of the actual $112\times112$ zero slope Jacobian. It requires that matrix to be exactly diagonal as recorded and all three original targets to be nonzero before attempting this unit-equation algorithm. It does not round off-diagonal entries to zero, use a ready linear graph, or silently omit high-core coupling in a general case.

At fixed $p_1,p_2$, each inner call tries to obtain

$$|d_3(p)|\le 10^{-8}.$$

This is the original unit-equation scale, not a scaled, projective or relative residual threshold. At every current inner point needed for a Newton update or root validation, the source evaluates the complete original $3\times3$ Jacobian. If the full Jacobian is nonfinite or $J_{33}$ is zero or nonfinite, it records that failure. It does not substitute a denominator floor, pseudoinverse, previous derivative or alternative parameter coordinate.

The inner Newton direction changes only the third parameter:

$$\Delta p_3=-d_3/J_{33}.$$

For an inner trial $\alpha=1,2^{-1},\ldots,2^{-19}$, it calls the original real model at $p_3+\alpha\Delta p_3$. An inner update requires the actual absolute third defect to decrease strictly. The other two parameters are preserved. Every original real-domain exception and every rejected trial remains in its inner report. No trial is called a valid root merely because its linear prediction is small.

There are at most 12 inner Newton updates and 20 backtracks per update. A reached residual tolerance is checked separately from a usable Schur point: the source still obtains the actual full Jacobian and a finite nonzero $J_{33}$ at the returned point. An update-budget failure, line-search failure, nonfinite or zero partial, exactly zero Newton step before convergence, or original domain/cell failure returns an explicit unusable result. The last inner probe and its actual three residuals are saved, but are not adopted by the outer algorithm.

Inner points are **trial root-finding trajectories only**. Inner `accepted` terminology is qualified as `inner_step_accepted`; it does not signify an original outer merit acceptance, BVP solution or native solve. The actual third defect is never overwritten by zero.

## 4. The initial p3 projection is separately accountable

The fresh actual90 starting point is the initial accepted candidate state for bookkeeping. The first inner call fixes its first two coordinates and tries a p3 root. All intermediate points are probes.

If the final near-root differs from the starting point, let its complete actual parameter displacement be $v=p_{\mathrm{root}}-p_{90}$, with the first two components zero. Using the full original Jacobian computed by the **fresh initial** `description`, the source records

$$F(p)=\tfrac12 d(p)^Td(p),\qquad s=d(p_{90})^T J(p_{90})v.$$

It adopts the root as the new baseline only if $s$ is finite and strictly negative and

$$F(p_{\mathrm{root}})\le F(p_{90})+0.2s.$$

This is an explicit step of size one in the actual total p3 displacement. Both full merits, the complete Jacobian, actual displacement, slope and bound are saved. A worse projection cannot silently replace actual90. If this test or the inner solve fails, outer iterations are skipped, the fresh actual90 point is retained, and the original final FD/Arb/circle diagnostics still run there.

If the fresh parent already meets the actual inner tolerance and the point does not change, the report marks a no-op baseline. It does not invent a negative slope or call that unchanged point a newly accepted step. This initial projection is an algorithmic initialization distinct from the eight permitted outer directions.

## 5. Two-coordinate positive-damped outer model

Only at an actually computed usable near-root does the source form

$$t=-J_{3,1:2}/J_{33},\qquad K=J_{1:2,1:2}+J_{1:2,3}t.$$

The third actual residual is retained. At a true smooth inner root this is the Schur derivative from R278. Here it is explicitly an **algorithmic local model at an approximate root**, not an assertion of an exact implicit function or of the derivative of an arbitrary stopped root finder.

Let $D_j=\|K_{:,j}\|_2$, using `hypot.reduce`; an exactly zero column receives scale one and is retained. With $A=KD^{-1}$, the new source solves the explicit $4\times2$ least-squares model

$$\min_z\ \tfrac12\|Az+d_{1:2}\|_2^2+\tfrac12\eta^2\|z\|_2^2,\qquad \eta=0.1,$$

using `lstsq([A; eta I_2], [-d_1;-d_2;0;0], rcond=None)`. It does not form normal equations. The recovered full original-parameter direction is

$$v_{1:2}=D^{-1}z,\qquad v_3=t v_{1:2}.$$

The source then computes the actual full action $Jv$ and the original complete merit slope $s=d^T(Jv)$, saving all three components. In exact algebra the tangent construction annihilates the third row of $Jv$; the actual computed third component is saved, not forced to zero. A nonfinite or nonnegative actual full slope stops the outer candidate search honestly.

The same-point two-dimensional spectrum is also saved: SVD of $A$, both singular-vector matrices, $\xi=U^Td_{1:2}$, and the actual damping removal/retention fractions

$$\frac{\sigma_i^2}{\sigma_i^2+\eta^2},\qquad
\frac{\eta^2}{\sigma_i^2+\eta^2}.$$

These explain this already formed local model. They do not create another direction, evaluate another damping candidate, predict an accepted nonlinear step or add an acceptance gate. A failure of this optional spectrum readout is recorded while retaining the original direction and subsequent original merit tests. Actual88's saved85 spectrum is not an input or prerequisite.

## 6. Every outer trial resolves p3 and tests the original full merit

For each of at most eight outer directions, the source tries the original 20 values $\alpha=1,\ldots,2^{-19}$. The seed is $p+\alpha v$, including the Schur-predicted p3 component. A fresh inner call then holds the seed's first two coordinates fixed and solves p3 again with the stated inner budgets.

Only a usable actual near-root is an outer candidate. Its unchanged actual full three residuals are evaluated with the same unweighted merit as before. Acceptance requires

$$F(p_{\mathrm{candidate}})\le F(p)+0.2\alpha s.$$

The damping penalty is not added to the nonlinear merit. The two-coordinate residual is not substituted for the full merit. There is no weakened finite/physical/native/BVP tolerance, no automatic accept based on the inner tolerance, and no claim that linear feasibility or a small local model predicts actual nonlinear descent.

An inner solve can fail at one outer trial; that failure is preserved and the next original outer backtrack is attempted. If all 20 fail the inner requirement or original full Armijo check, the last accepted outer point remains the final candidate. Every actual root point, full merit, residual error, derivative, trial index, alpha and reason is retained.

## 7. Final original checks and mathematical scope

At the final adopted point, the entry invokes the unchanged original `description` with its complete112 right vector, unit defects, original3×3J and three real FD scales. It invokes the unchanged declared-real scalar `a/ap` Arb procedure at 160 bits/depth14 and the original complete zero-core circle FFT/node/mid/two-RMS check on the original 699-node mesh. The source does not use the finite-Gauss `app` as the exact derivative of the supplied radius.

The original two threshold statements remain distinct: an early search stop may report the maximum of the three unit equations at most `1e-8`; the final candidate flag tests the actual complete112 `full_right` vector against that same numerical threshold. Neither statement is an original nonlinear BVP acceptance. `success` and `full_nonlinear_nonzero_lambda_solution_computed` remain false. High109 nonresonance, interval transversality and a nonzero continuation are not inherited from a different parameter point.

## 8. CLI and output contract

The source is placed beside the frozen topic computations. The exact first invocation is:

```bash
python -u geometry_20261115_small_core_p3_inner_root_search.py \
  --accepted ACTUAL_ACCEPTED96.json.gz \
  --prepared ACTUAL_PREPARED112.json.gz \
  --tail-anchor ACTUAL_TRUE_T112_ZERO_ANCHOR.json.gz \
  --tail-config ACTUAL_T112_CONFIG.json \
  --parent-status ACTUAL90_damped-resume-status.json \
  --parent-status-sha256 5a4d157aa0bcada3cdd1d319adb419f23b94f52bfc1c945a3c6afe1207cb2f5a \
  --damping 0.1 --candidate-steps 8 --backtracks 20 \
  --inner-newton-steps 12 --inner-backtracks 20 \
  --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14 \
  --out FRESH_OUTPUT/small-core-p3-inner-root
```

The new schema is `R278-original-three-equation-approximate-p3-inner-root-LM-v1`. Primary status is `p3-inner-root-status.json`; the original final scalar/circle basenames are retained inside the new output directory. Parent bytes are `parent-status.json` or their unchanged `.gz` representation.

Each actual inner call has a complete `inner-solves/inner-NNNN.json.gz` with its seed, all steps, all original three residuals, full112 vectors, original3×3 derivatives, actual domain errors, final probe, exact stop reason, elapsed time and original call counts. The primary status holds its SHA/size descriptor and summary. Every outer trial links the actual corresponding inner report. This is bounded by one initial inner call plus at most eight times twenty outer-trial inner calls; an inner call has at most twelve Newton updates and twenty backtracks per update. Root validation may require a final additional fullJ at the reached point; that call is counted.

`large-arrays/original-model-evaluations.jsonl` streams all original real/complex evaluation and Jacobian events with context, parameters, original returns or exceptions, and measured costs. Real calls retain complete first-order right/height vectors and original query-domain readouts. Complex events are explicitly original complex-step probes, with real/imaginary parameters and equations; they are not claimed to have passed the original real-domain test. The trace does not call the model again and does not mutate its return. Nonfinite diagnostic values retain class and original binary64 bits. Observer failures are reported and cannot change an original evaluate return.

Full artifacts preserve these intermediate reports, logs and any partial failure. The existing publisher keeps `large-arrays` artifact-only; ordinary bounded JSON/gzip publication and source/input receipts remain in place. A completed unsuccessful root search returns an honest `diagnostic-completed` status with `success=false`; a programming/input/runtime exception remains an exception with traceback and partial files. This is not a newly imposed science gate.

## 9. Static preparation scope

`source-only-static-check.json` records 40 source/AST/original-JSON/byte checks: the exact actual90 status; all eleven frozen source bytes; the independent schema; Actions-before-import ordering; p3-only updates; the Schur/lift/column scaling expressions; full original merit responsibility at initialization and outer trials; direct original final checks; and preservation of the actual residuals.

The preparation imported no mathematical source and ran no numerical fixture, root solver, finite difference, SVD, Arb, native solver or scientific test. No repository/Git branch or workflow was edited or dispatched by this preparation. The paired request92 workflow/request draft supplies the one concrete Actions execution and complete source pins for the root's normal publication process.
