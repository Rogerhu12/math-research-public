# Isolated parameter recovery after unavailable execution sessions

At 18:49 UTC, `write_stdin` returned `Unknown process id` for the earlier
sequential controller 37542 and followers 62475 and 86359. No process exit code
or cause is inferred. The saved center index contained 29 complete segments
(0–28), and the saved uniform index contained 28. The last center child log
contained its complete result and the cover's requested-prefix completion;
the outer scheduler record still showed that child as active. These distinct
observations are preserved without rewriting the old operational history.

`notes/2026-11-12-parameter-sessions-unavailable-recovery.json` records the exact
files and hashes copied into
`data/phase_ring_continuation/step5_parameter_session_unavailable_1849/`.
It includes the old indices, chronological reports and coefficients, scheduler
state and final logs. The old chronological snapshots are evidence of the
previous state; their stored original paths are not silently redirected.

Every one of the 29 center and 28 uniform leaves was rechecked through the
unchanged `validate_parameter_report`. Each report path and SHA, exact source
scope, parameter interval, strip contract, first-integral contract and selected
g0 report identity matched the new parent g0 index. The latter retains exactly
the old selected paths and SHA values for this prefix. The copied parameter
indices were byte-identical before the new controllers started their replay.

New center outputs are under
`step5_parameter_density_forward_resume1849`; uniform outputs are under
`step5_uniform_parameter_density_forward_h1e9_resume1849`; hybrid accumulation
is under `step5_hybrid_parameter_density_forward_resume1849`. The source index
is `step5_forward_density_complete_v9_resume1837/index.json`. New parameter
proofs, proof locks, precomputation records, logs and operational state also use
independent locations. Existing completed expanded-field proofs are only read
as immutable ancestors. If no compatible expanded proof is found, the original
R3 analytic budget remains the valid fallback.

`fourfold_parameter_sequential_cover_v2.py` adds only explicit directory
arguments to the already frozen sequential controller. It still launches the
unchanged cover v4 and mathematical pipeline v5, one parameter child at a time.
It does not change any mathematical tolerance, primitive grid, parameter box,
seed validator or finite integral formula. Center/hybrid followers remain the
previously checked v2/v3 implementations.

The recovery command, from the topic directory, is:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python -u scripts/fourfold_parameter_sequential_cover_v2.py \
  --g0-index data/phase_ring_continuation/step5_forward_density_complete_v9_resume1837/index.json \
  --center-directory data/phase_ring_continuation/step5_parameter_density_forward_resume1849 \
  --uniform-directory data/phase_ring_continuation/step5_uniform_parameter_density_forward_h1e9_resume1849 \
  --expanded-domain-directory data/phase_ring_continuation/step5_expanded_time_domain_full \
  --parameter-proof-directory data/phase_ring_continuation/step5_expanded_parameter_time_domain_resume1849 \
  --parameter-proof-lock-directory /tmp/visible-flex-parameter-domain-locks-resume1849 \
  --precomputation-directory data/phase_ring_continuation/step5_parameter_precomputations_resume1849 \
  --log-directory /workspace/scratch/f6a2c7886477/parameter-density-logs-resume1849 \
  --out data/phase_ring_continuation/step5_parameter_sequential_cover_resume1849.json.gz \
  --stop-file /workspace/scratch/f6a2c7886477/stop-parameter-sequential-resume1849
```

No earlier unknown process is assumed dead, and no new process writes its old
output namespace. New reports must independently pass all original gates.
