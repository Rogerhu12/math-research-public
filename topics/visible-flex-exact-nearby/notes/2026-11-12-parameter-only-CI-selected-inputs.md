# Parameter-only CI blocks bound to selected zero-order inputs

Status: orchestration and exact input validation; no new returned-map claim.
The mathematical density kernel remains
`fourfold_parameter_density_pipeline_efficient_v5.py` (SHA
`bee932df5c1d63860a900898cf0b9f288c49462361d08fbf0545bd900ff340fb`).

## Selected input and actual validation

`step5_parameter_ci_seed_prefix0056/index.json` has SHA
`bd8633409108f0c7128820fe4dd801c51648be7881522e505379b1f20bb89bbb`.
It selects the original complete leaves 0–55 and their original first-integral
files. The live g0 index was already at 110 when copied; no truncated
chronological accumulator was manufactured. The full observed live index is
retained separately as provenance and is not a 56-segment sum.

The new worker's actual plan for segments 32–55 passed the original
`validate_saved` and exact field-cover/reference partition checks for all
24 leaves. The input plan report is
`data/phase_ring_continuation/step5_ci_forward_blocks/local_parameter_plan56/block_0032_0056/block-manifest.json`.
Its `complete` field is deliberately false: this run validated inputs and did
not compute the parameter densities.

The first plan attempt rejected an absolute source path stored in the snapshot
because the operational lookup expected a relative string. The source bytes
were unchanged. The initial worker and failed plan are retained; the corrected
lookup uses the source basename and exact SHA, while the original mathematical
validator still checks the real source bytes. No proof or arithmetic gate was
relaxed.

The input handoff is
`notes/2026-11-12-parameter-only-CI-selected-inputs.json`: 114 read-only repo
files, 4,584,680 bytes, plus four original reference cache shards identified
separately. Existing complete domain ancestors and arithmetic dependencies
remain part of the sparse topic checkout and are rechecked by the original
validators. This selected handoff does not replace those checks.

## Concrete worker invocation

From the topic directory, after the exact original forward U/L/Q cache has
been restored and verified:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python -u scripts/fourfold_ci_density_block_parameters_v1.py \
  --g0-index data/phase_ring_continuation/step5_parameter_ci_seed_prefix0056/index.json \
  --g0-index-sha256 bd8633409108f0c7128820fe4dd801c51648be7881522e505379b1f20bb89bbb \
  --start 32 --stop 37 --run-tag ci_PARAMETER_RUN
```

Suggested disjoint half-open blocks are [32,37), [37,42), [42,47),
[47,51), [51,55). Segment 55 already has the complete selected
`local_actual55` g0/center/uniform block and should be reused.
Current local completions may be preferred by the unchanged dynamic cover;
a CI result is reusable only if its referenced g0 SHA equals the current
selected g0 SHA.

For every leaf the worker runs the parameter-domain precomputation in a
separate process, then the unchanged density kernel. The center uses target
1e-9 and both g1/g2; the true real parameter box uses half-width 1e-9, target
1e-7, and g2 only. Point primitive Q384, root Q1024, independent enlarged-domain
proof Q512, and all original alias/rounding/continuous bounds are retained.
The proved selected g0 enlargement is read directly from its original path;
g0 and its first integral are never recomputed or rewritten.

## Artifact and continuation contract

Output lives under
`data/phase_ring_continuation/step5_ci_forward_blocks/<run-tag>/block_<start>_<stop>/`.
A final `files.json` names the complete block manifest SHA and all new output
bytes plus read-only external g0/first/enlargement inputs. The artifact may
contain only the new block files; intake must then verify external inventory
paths against the current canonical original path and exact SHA.

`artifact-paths.txt` lists the new relative output paths.
`artifact-all-paths.txt` additionally lists the external read-only inputs.
The two lists are packaging metadata and do not participate in a circular
self-hash. A workflow should also preserve
`ci-output/parameter-inputs-proof.json`, using the topic directory as the
common archive root so relative paths do not change.

A suitable workflow follows the already successful pinned Python 3.12.14 /
NumPy 2.3.5 / SciPy 1.17.0 runtime and restores the previously verified
forward cache from run 43270092696. It checks all manifest files before invoking
the worker and always uploads complete or failed output. The parent agent owns
the workflow and dispatch; this note does not assert that a new CI run exists.

The existing read-only dynamic seed helper recognizes this worker by its
`fourfold_ci_density_block*.py` source SHA and again applies all report,
inventory, descriptor, domain, source and current g0 identity checks.
Only afterward does the original parameter cover validator accept a leaf.
All chronological C/D terms, including cross-block g1*g1 and g0*g2 frequencies,
are still computed by the unchanged accumulators. A completed block is not the
550-segment half-return or the actual KAM certificate.

## Distinct local interruptions retained

Uniform segment 32 first failed with explicit ENOSPC while creating field_p2.
The exact captured report/index/traceback are in
`notes/2026-11-12-parameter-uniform32-enospc-evidence.json`.
After space recovered, a separate retry reached field node 0 and returned
native -9 / outer 1 without a Python traceback; its cause is unknown.
Its independent snapshot is
`data/phase_ring_continuation/step5_parameter_failures/uniform32_resume_sigkill/evidence.json`.
These are operational interruptions, not failed mathematical inequalities.
The center33/uniform32 complete prefixes remain unchanged.
