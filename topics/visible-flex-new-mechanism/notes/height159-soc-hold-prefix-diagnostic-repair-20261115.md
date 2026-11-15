# Preserve the original frozen159 exception before handoff

Date: 2026-11-15. This is a diagnostic-only change after run43705209195, source9ca83546823ea077bd8b9e6ef2d10344788518e5. No new development or scientific calculation has executed this revision.

## Established failure and scope

The prior new development suite passed, output SHA25630d15185b9630afd752a518703f09809936950d1114e07f762c3c97c93b8f42f. Five scientific prefixes ran. The sixth original159 prefix preserved an admissible initial state, used zero LPs and zero optimization seconds, then returned a non-complete status. The new driver rejected it before calling the conditional-SOC-radius stage.

The original stage exception was not printed. The consumer's generic “completed current temporary159 result required” error and temporary cleanup hid that cause. Its type and message cannot now be recovered from the published metadata or completed log. No particular pool/Jacobian/geometry defect is asserted.

Only scripts/frame_metric_height159_soc_hold_audit.py changes. The new conditional-radius library, all six frozen scientific prefixes, their sources, parameters, budgets, row semantics, pools, geometry and acceptance gates remain unchanged.

## Changes

The new pure prefix_handoff_diagnostic function reads the returned sixth report. It selects its status/phase/source/run, original top-level and stage error, budget reason, existing LP/value/Jacobian counts, available preflight records, and last coarse/fine pool count/hash/capacity. It does not extract coefficients, grid arrays, row ID arrays or any new geometric values. Missing information stays unavailable. In particular, a proposed pool size cannot be inferred if a frozen setter raised before recording it.

Immediately before the original handoff call, run_pipeline prints this small diagnostic to stdout. If the existing handoff rejects the result, the same diagnostic is copied into the small pipeline failure report and its native summary before cleanup. The original unsuccessful-status check, its error text, and every later source/state/reference/pool/gate check are unchanged. This patch does not permit an errored prefix to continue.

The diagnostic is a read-only view of an already JSON-serialized returned report. It does not catch or reinterpret a scientific exception, alter the solver or restart any budget. An unavailable original cause remains unavailable rather than being replaced by a guess.

## Targeted public development

The new CLI branch is:

    python topics/visible-flex-new-mechanism/scripts/frame_metric_height159_soc_hold_audit.py \
      --check-prefix-diagnostic-only --out <temporary-development.json>

It runs only a new dictionary/file fixture for the previously missing branch. Six prefix calls are stubs; the real run_pipeline and the real unsuccessful-status check execute. The fixture checks that an explicit nested initialization error is printed and retained, the new stage is not called, the original prefix is unmodified, coefficients/row arrays are omitted, unavailable errors are not invented, temporary cleanup still occurs, and the native failure summary preserves the same diagnostic. Its CLI-dispatch check replaces the new fixture with a marker and forbids calling the already-completed old development function.

The old --check-only branch remains available and unchanged in purpose, but is not needed for this targeted repair. The production98 arguments remain identical. The root-owned workflow can use the new targeted flag and the unchanged actual98 arguments; it must bind the new driver SHA.

This fixture has been authored and statically read only. It is not labeled passed; first execution belongs to public Actions. No source import, geometry evaluation, solver or old development suite was run during preparation.

## Next decision

The next returned sixth-prefix failure will expose its original error and available initialization state. A successful returned prefix still faces exactly the old handoff validation. Any later repair must address the observed original error, not increase a capacity or relax a gate based on the present lack of information.

Necessary restoration in a new public job remains restoration under the metadata-only policy. It is not new scientific improvement and must not be repeated until a historical state hash is forced.
