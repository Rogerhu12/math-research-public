# First conditional-SOC-radius run: recovery stopped before the new stage

Date: 2026-11-15. This is a human analysis of the completed public job and its fixed source, with no new geometry evaluation.

## 1. Outcome and provenance

The first public attempt at the conditional-SOC-radius experiment did **not invoke the new experiment**. Its new development suite completed successfully. Five necessary scientific input-restoration stages ran. The sixth, the frozen original five-null-height159 stage, returned an unsuccessful controller result before its first LP. The new driver then rejected that handoff. This is an implementation/recovery failure, not a positive or negative result about keeping the radius after an accepted SOC correction.

The authoritative run is [43705209195](https://github.com/Rogerhu12/math-research-public/actions/runs/43705209195), job [132784732079](https://github.com/Rogerhu12/math-research-public/actions/runs/43705209195/job/132784732079), at source [9ca83546823ea077bd8b9e6ef2d10344788518e5](https://github.com/Rogerhu12/math-research-public/tree/9ca83546823ea077bd8b9e6ef2d10344788518e5). The lane is metric_height159_soc_hold.

The new development output has SHA256 **30d15185b9630afd752a518703f09809936950d1114e07f762c3c97c93b8f42f**. The final failure report was 151,682 bytes, with raw SHA256 **48d2e493bbc71ea9a8fff5a70b2f753146849e2c7ae43ad23670e99210929366**. Its status was height159-SOC-hold-pipeline-failed-last-written-checkpoint-preserved; its phase was height159-qualified-state-full-pools-reference-and-controller-handoff. These are metadata for the temporary report, not a claim that its machine payload was retained.

The main research step failed; the later read-only scientific printer and metadata publisher succeeded. Publication success does not change the scientific execution status.

## 2. What actually ran

All five completed prefixes were necessary restoration of transient inputs under the repository data policy. Their output states can differ from historical states because their original wall budgets remain active. They are not additional applications of the proposed SOC-hold method.

| Temporary restoration | Final physical SHA256 prefix | Accepted records, including initial | LP calls | Shared full-value calls | Optimization seconds | Run-audit seconds |
|---|---|---:|---:|---:|---:|---:|
| Frozen growth | 643875e4f9d46763b | 8 | 12 | 39 | 116.727091278 | 499.600788075 |
| Frozen strip reserve | 267c41ff9cfe565c | 10 | 11 | 26 | 120.147445617 | 132.688600606 |
| Frozen scaled SOC | ec76df0b4d8c4752 | 11 | 12 | 26 | 106.706391897 | 119.237585536 |
| Frozen body103 | bfbd7465044bd742 | 2 | 1 | 4 | 1.560359665 | 14.216008012 |
| Frozen tail154 | 1e624252d6181f6a | 10 | 11 | 24 | 120.282632010 | 133.008606129 |
| Frozen height159 | 1e624252d6181f6a | 1 | 0 | 2 | 0 | 2.991470533 |

The sixth stage also performed two independent final value evaluations, so it used four full-value calls altogether. Its model, trial and correction tables were empty. Its one accepted record is the unchanged admissible initial state, not a new accepted step. The conditional-SOC-radius stage had zero invocations.

The pipeline elapsed time reported on failure was 919.703433642 seconds. The sixth stage printed a process high-water RSS of 3,108,928 KiB. This includes earlier prefixes; it is not an isolated memory measurement for the new method.

## 3. The sixth-stage input remained admissible

The final tail154 state, and unchanged sixth-stage state, was **1e624252d6181f6ad2bc6937adc37302b9bf77352f7c50a1aa02bf92fdb552c3**.

The sixth stage inherited the actual restored body radius 0.0000625, recorded exactly as 1152921504606847/18446744073709551616, with success streak zero. Tail radius was body radius divided by 8; new height radius was body radius multiplied by 4. No radius reset is reported.

Its exact height-coordinate map had SHA256 **4f708c9806a16853a561fa33d6ee656acd0ec0ce889294d888bdbe3feed73d16**. All five new height coordinates were zero. The nine exact physical height coefficients equalled their reference values, and the exact total height-integral change was zero.

Both original grids passed every printed actual gate at initialization and at the independent final re-evaluation:

| Quantity | Original 384-angle grid | Original 768-angle grid |
|---|---:|---:|
| Maximum actual metric error | 0.26648783764683898 | 0.26648836627858957 |
| Maximum absolute principal curvature | 57.999966106730888 | 57.999987818344678 |
| Inner-strip absolute margin | 2.4479143279e-7 | 4.0857549399e-8 |

On the fine grid, maximum absolute y was 0.3899899591424506, minimum signed z was 0.02, and the sampled direct mirror-pair radius minimum was approximately 0.10057759339275428. The reconstructed cap height was 0.14270420084310476, with reported margin zero against its declared target. The affine and reconstructed cap heights differed by 2.7755575615628914e-17, within the unchanged numerical consistency rule. The exact original coefficient-box check passed.

The fine metric maximum was in the body at t = 33/80 and theta/pi = 127/128. The current-height diagnostic reported b(0.09) = 1.0432470144212365 and maximum b squared minus one = 0.08836433309882352. In this five-height representation b is variable, so that diagnostic is not a fixed-family obstruction.

The independent final comparison recorded zero frozen-metric and exterior six-jet changes from the sixth-stage reference. Original 384-to-768 evaluation differences were approximately 8.19e-9 for X, 6.69e-6 for Xs and 0.00601708 for Xss. These are same-parameter numerical comparisons, not continuous error enclosures. The stage made no parameter change and paid none of the requested new metric improvement.

## 4. Failure known from source and logs

The top-level error printed was:

> ValueError: completed current temporary159 result required

The [fixed new driver](https://github.com/Rogerhu12/math-research-public/blob/9ca83546823ea077bd8b9e6ef2d10344788518e5/topics/visible-flex-new-mechanism/scripts/frame_metric_height159_soc_hold_audit.py) raises this in handoff_restored_height159, before constructing the new SOC-hold objective. The handoff requires the frozen sixth-prefix status complete-two-grid-entry-tail-height159-audit; it rejects other statuses before examining the nested controller error.

The new driver calls the [frozen original159 driver](https://github.com/Rogerhu12/math-research-public/blob/9ca83546823ea077bd8b9e6ef2d10344788518e5/topics/visible-flex-new-mechanism/scripts/frame_metric_entry_tail_height159_audit.py) directly. Static inspection found no replacement of old module globals, methods or configuration by the imported new SOC-hold module.

The original159 driver can finish independent diagnostics around a saved admissible state when its controller returned an error. Its top-level status then remains entry-tail-height159-controller-error-last-qualified-preserved, rather than the successful status required for handoff.

The sixth-stage log proves that its initial point was accepted and its reference installed, but its optimization clock was never started and no LP was called. The [frozen original159 controller](https://github.com/Rogerhu12/math-research-public/blob/9ca83546823ea077bd8b9e6ef2d10344788518e5/topics/visible-flex-new-mechanism/scripts/frame_metric_entry_tail_height159.py) performs coarse-pool expansion, fine-pool initialization, preflight and a first selected-row Jacobian before starting that clock. The observed failure is confined to this initialization interval.

**The original nested exception's type and message were not printed.** The new pipeline preserved the generic handoff error and temporary-file hashes, then cleaned the temporary directory. The evidence does not distinguish a pool-capacity boundary, a known-location check, a first-Jacobian failure or another error within that interval. Selecting one of those possibilities as the established cause would be unjustified.

The frozen fine-pool initializer does have a specific capacity boundary: it unions all inherited rows with fresh per-radial metric and curvature minima, then calls its strict setter. Exceeding capacity there raises an ordinary ValueError. This is a concrete diagnostic branch to expose, **not a demonstrated cause of this run**, and not a reason to increase capacity.

## 5. Minimal next action

The certain defect is loss of the original sixth-prefix failure diagnostic. The minimum defensible change is to the new consumer's reporting and handoff handling:

1. Before rejecting a returned prefix, print and retain its top-level status, nested stage status, original error type/message, budget reason, and existing initialization/Jacobian counters.
2. Record inherited and proposed fine-pool counts and unchanged capacity when available, without changing the pool, its IDs or any gate.
3. Preserve the diagnostic in pipeline failure metadata before temporary cleanup. Keep the successful-status requirement and all source, state, parameter and full-grid validation.
4. Once the original exception is known, repair that specific interface. Do not substitute a speculative Jacobian change, a relaxed gate, a larger pool or a fresh scientific budget for missing evidence.

The new development suite has already completed; it need not be repeated merely for assurance. An added failure-reporting branch needs only its own targeted development fixture. The completed five recovery prefixes are not new scientific progress. If another public job must restore their transient outputs because they no longer exist, it must identify and charge that work as necessary input restoration, without extending budgets or retrying until a historical hash appears.

This run gives no evidence about the proposed conditional radius hold itself. The sixth-stage baseline is a numerical state observed during recovery, not a continuously certified isometric embedding or proof of reach.
