# Retention 61, part 2: twelve reproducible historical reports

Prepared 2026-11-28. This package records a proposed ordinary-tree retirement; only the root publisher may apply it. It changes no scientific source, current input, configuration, proof, solver budget or conclusion.

## 1. Exact scope

The twelve full files total **587,710 bytes**. Each is a generated historical report: five flat-strip/curvature comparisons, one failed turning IVP, and six exact or symbolic budget/transfer outputs. The complete files were individually read as text, each below 100,000 bytes. No gzip, NPZ, binary, or larger raw input body was retrieved.

The fixed output recovery snapshot is `17ed6ccae50001659c1bb8cf549075a538778f65`. It is the snapshot checked for these path/blob/size identities, not a claimed original execution commit. Complete older input files are separately bound to `60321451c058c6a51da58c37ae5ec6f2d1145f74`, their original paths, bytes, Git blobs and published whole SHA-256 values.

The exact deletion list is in [the complete provenance](../computations/legacy-generated-results-retention-61-part2-provenance.json). The publisher must compare that list with its fresh tree before the ordinary commit. There is no authorization here to retire a similarly named file or a different version.

| Historical generated output, under `notes/` | Bytes | Preserved interpretation |
| --- | ---: | --- |
| `alternative-flat-fast035-m64-width02.json` | 30,147 | Finite flat-strip comparison |
| `alternative-flat-fast035-m64-width03.json` | 29,132 | Negative orientation/support and very large curvature remain failures |
| `alternative-flat-hermite045-040-065-m96-width01.json` | 36,861 | Finite Hermite-parent flat-strip comparison |
| `alternative-turn-fast035-flat005-m96.json` | 88,998 | Actual domain failure during turning IVP |
| `2026-11-12-strong-initial-speed-pulse-budget-r1.json` | 57,131 | Exact pulse-polynomial budget, not a solved closed field |
| `2026-11-12-tail-r33-strong-m16-cut-strip.json` | 64,956 | One-cut analytic-strip budget |
| `2026-11-12-closure-rational-linear.json` | 44,873 | Rational linear/depth calculation, not nonlinear closure |
| `2026-11-13-strong-q096-convection-mean-exact.json` | 56,147 | Exact convection contribution, not the complete actual mean |
| `2026-11-13-strong-A32-nonmean-Cartesian-C2-transfer-r1.json` | 81,249 | Nonmean synthesis transfer only |
| `2026-11-13-strong-q106-nonmean-Cartesian-repair-transfer-r1.json` | 71,915 | Nonmean synthesis transfer only |
| `alternative-flat-fast035-m96-turn-budget.json` | 11,002 | Complete per-row turn budget retained |
| `alternative-flat-slow128-turn-budget.json` | 15,299 | Complete per-row turn budget retained |

All twelve whole SHA-256 and Git identities, exact restore commands, original parameters, known reader boundaries, input aliases and source records are recorded in the provenance. The separate [complete results record](../computations/legacy-generated-results-retention-61-part2-complete-results.json) keeps the original configuration, scalar results, failed and unpaid statuses, exact critical brackets and specified complete result tables. It also identifies the generated arrays/rows that remain recoverable as the exact old whole file. It must not be supplied to an unchanged numerical consumer as if it were that original file.

## 2. Three distinct flat producers

The original flat bodies are not interchangeable. The existing 6,340-byte `retention50-fast-original/alternative-flat-continuation.py` has whole SHA-256 `f66950b336524e97d91a2cea447d515ddc3f5137dbbfad074effe2f913141131`. The later current 7,300-byte body has whole SHA-256 `6be192d7116d3770bd7a7e5ade0020f31cc71d4b852b9ec7288f79a4a135ecad`. They remain unchanged.

Both original turn-budget outputs identify a third complete producer, SHA-256 `4a6cd34b62b1f71a173a84e4f478c80318da28b9644bbbf36cd4f241e90b7885`. Removing exactly the later controlled-Hermite dispatch from the 7,300-byte body recovers that whole identity, with 7,006 bytes and Git blob `9a9d4f828914f07b3f66ba60a0f32bd144e5fb3e`. The full recovered source is added at [retention61-original/alternative-flat-continuation.py](../computations/retention61-original/alternative-flat-continuation.py).

The provenance preserves the entire old/new text patch, its one occurrence, both complete source records and the two original report fields that establish the old SHA. This was a text/hash recovery only. No import, AST, compilation or scientific run occurred. The recovered source has no invented historical commit. A historical recomputation must place it under its original basename next to the exact sibling providers in an isolated restored directory; it must not overwrite the current producer.

All five flat outputs have complete effective CLI parameters, the original full input identity, original provider/sibling records and the distinction between a reconstructed complete command and an unrecorded original shell invocation. The original trajectories are not newly retired by this package.

## 3. Finite comparisons and the real failed turn

The width-0.2 M64 report retains metric error `3.099492598135356e-7`, maximum absolute curvature `5.3798042458813935`, minimum signed area/Jacobian `0.263484426388337`, and minimum support `0.2403496833666729`. These are finite reported quantities, not an all-domain certificate.

The width-0.3 M64 report retains curvature `1223.97550351628`, minimum signed area/Jacobian `-0.072817106190542`, and minimum support `-0.2454755476298433`. The retention does not turn these negative quantities into an admissible surface.

The M96 Hermite-parent width-0.1 comparison retains metric error `9.944820744678395e-9`, maximum absolute curvature `4.029330214394809`, minimum signed area/Jacobian `0.59129765413585`, and support `0.08336551836454448`. Its parent and controlled-profile provider are separately recorded; no relation to the current Fejér field is asserted.

The failed M96 turn retains the actual exception:

```text
FloatingPointError('domain at s=0.532859076, margin=-0.0308097775729')
```

The original target was `s=0.9`, with M=96, N=1536, coast length 0.05, turn length 0.4, target radial speed -0.6, rtol 1e-11, max_step 0.00025, and 40 output steps. The full recorded configuration, reached location, initial/final reported rows, failure state and original coefficient/detail fingerprints are retained. The exact original output remains available through its whole Git identity. This failed finite IVP is not a nonexistence proof.

The two turn-budget reports retain all original radial rows—11 and 16 respectively—including every B8/B10 budget and normal/mixed component. They are complete comparisons at their stated samples; they do not pay a full turning solution or reach.

## 4. Exact pulse budget and its actual consumers

The pulse report retains all five exact choices `0, 1/5, 7/20, 1/2, 3/5`, their complete scalar/enclosure conclusions, root intervals, endpoint data and positive-leaf counts `1,1,1,2,3`. The original resource record is retained in full, including its exact argv, exit code 0, wall time `11.0383839607` seconds and peak RSS 13,556 KiB. Unknown workflow or runtime versions are not inferred.

Its accepted 42,588-byte gzip parent is bound by its published SHA and exact historical blob; its body was not read. This is an old independently specified pulse/profile calculation. It is not a new computation for the current fixed Fejér target, and its whole field, BVP, closure and reach obligations remain unpaid.

The downstream background-bounds source really reads the pulse certificate's accepted reference identity, unchanged core fields, the per-row curvature certificate, all closed intervals and positive leaves, and the radius/parallel-curvature bounds. The envelope source binds the whole pulse report and complete accepted reference. Both complete consumer sources and both complete original OS resource/argv records are preserved in the provenance. These readers require the original pulse file to be restored first; a summary or the present retention projection cannot replace it. The already retained downstream background result stays in the tree.

## 5. M16 analytic strip and rational linear outputs

The M16 strip source consumes the complete real response, complete real-source enclosure and complete radius enclosure. All three original whole input identities and their exact restoration paths are preserved. The whole finite H/P coefficients, precision 192 bits, all seven tau values `0,1/256,1/128,1/64,1/32,1/16,1`, two width targets and 64 bisection iterations remain in the complete recipe.

The results retain all seven cases and both exact critical-width brackets. At tau `1/64`, the reported norm display is about `0.0155699233512596` with positive margin about `5.507664874e-5`. At `1/32` the working-radius test is false even though the holomorphic-domain test remains true; at tau `1` both are false. These are one-cut facts. The full radial problem, real-source closure and nonlinear DN remain unpaid, as in R33.

The rational linear report has its complete self-contained rational model and all original parameters preserved. Its producer takes only the output argument and has no external scientific input. R15 publishes the producer and its command, but the original report did not record the execution source SHA, workflow or resource record. Those historical fields stay null; the retained current source identity is not relabelled as a recorded execution identity.

All nine exact checks, all six tested depths, constants and first/last block conclusions remain. N=128 and 160 fail the linear condition; 176 and 192 satisfy the linear condition but not the low-height condition; 224 and 256 satisfy both stated tests. The 109 generated blocks remain in the original exactly recoverable file. This rational-deep metric is independently specified; these tests are not nonlinear existence, a certified closed surface, or permission to change the current metric.

## 6. Convection and nonmean Cartesian transfer

The convection report's original execution was exact BigInt work through `functions.exec`, with the original record explicitly saying the published Node CLI had not been executed. Its elapsed time `67.503` seconds and completion `2026-11-13T00:01:27Z` are retained as historical facts. The published Node command is a complete regeneration route for the mathematical data; it must not be described as the original shell command.

The whole exact-rational helper/source identities, K=32, M=28, cap precision 96 bits, all input coefficients, and all 28 original mode-weight rows are preserved. Named-column storage is lossless for those rows. The complete normal-velocity mean, actual finite field, full height mean and actual-prefix C2 certificate remain false/unpaid. The alias source and mathematical notes stay unchanged.

The A32 and q106 transfers share the complete synthesis producer but bind different complete saved repair certificates and original resource records. Their old local aliases resolve to the full 560,993- and 484,663-byte gzip inputs, not just the small manifests. Only metadata of those larger gzip inputs was used here.

The output record retains all six exact unrounded derivative sums and their dyadic upper caps, gauge, full scope flags and original input/source identities. The A32 case had 109 gates and 97 states; q106 had 97 gates and 85 states. Their original whole parameter/state bounds and generated rows remain exactly recoverable. The producer's all-physical/all-angle enclosure is explicitly a **nonmean synthesis** statement. The complete mean, background, PDE, metric and reach are not thereby paid. The unchanged comparison manifests and both interpretation notes remain in the tree.

## 7. Full restoration before historical readers

For each retired file, the provenance gives an exact `git show COMMIT:FULL_PATH` argv and whole blob identity. Restore into scratch or a separate historical checkout, compare bytes and recorded SHA, and supply those original bytes to any old consumer that pins the original whole hash. Gzip inputs stay compressed until their original unchanged consumer reads them.

Exact source layout matters. In particular the f669, 4a6 and 6be flat versions remain distinct, the old input aliases retain their exact full files, and the two original resource wrappers retain their own recorded identities. The ordinary `strong_resource_run.py` identity contains the full `...c1c1e110...` segment; the foreground wrapper is the exact e683fbb body, not a similarly named later observed wrapper.

The provenance includes complete read sets and actual resource commands where available. An indexed literal search was used only as evidence for identified references; it is not proof that no dynamic/future consumer exists. One rate-limited query is expressly not treated as a negative result. For an additional historical reader, the same exact-whole-file restoration rule applies without rewriting its checks.

A new scientific regeneration can have new path strings, timing/RSS or platform-dependent numerical serialization. It does not replace the fixed old byte identity. Unrecorded old shell syntax, Actions run, runtime version, OS exit status and resources remain unknown.

## 8. Preserved boundaries and publication

All original source, proofs, parameters, resource records, manifests, active Fejér/half-wave inputs and pending histories stay in place. Canonical/parent91, unresolved ports/Nelder, the q096/q098 screens with the unresolved external-client version, and the five earlier outward reports lacking max_step are excluded. Prior retention59/60 and retention61 part1 paths are not repeated.

The complete provenance refers to five existing full retention ledgers, eighteen existing complete sources, eleven proof/interpretation files and six source/input/result manifests by exact whole identity instead of reproducing their bodies again. The original 4a6 source is the only new source file, recovered exactly as explained above. Each new complete artifact is below 100,000 bytes.

This work executed only text retrieval, serialization and ordinary content hashing. It ran no scientific command, import, AST, compilation, CAS, fixture, numerical test, benchmark or replay. No ref, queue or deletion was written by this agent. Publication and the fresh identity comparison belong to the root publisher. No independent re-execution is added as a gate.

The final delivery manifest gives exact additions, exact twelve deletions, gross bytes, added bytes including the manifest, and net freed bytes. Complete failures and unpaid obligations remain visible in the retained results and notes. This is capacity maintenance for continuing the authorized research, not a newly computed mathematical result.
