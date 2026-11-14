# Waiting for exact completed block seeds after a fixed prefix

`scripts/fourfold_forward_density_cover_v9.py` extends the frozen v8 controller
with `--seed-only-from N`. At every new key whose segment is at least `N`, it
requires a validated completed block seed and cannot launch a local sampling
process. With `--follow` it saves the actual segment, exact normalized subspan,
domain path and domain SHA, then waits for a complete block. Without `--follow`
it returns an explicitly incomplete waiting index. An additional assertion
rejects any accidental entry into local sampling at or beyond the threshold.

The previously completed prefix has priority and keeps its exact report bytes.
Explicit static seeds and already complete local leaves retain the original
v8 validation paths. Thus a caller who wants all new segments to come from CI
should omit unrelated old standalone pilot seeds. For the current run, the
parent can resume directly from the saved v7 prefix using
`--seed-only-from 56 --follow`; the existing complete local block 55 is found
by the same dynamic block mechanism. Existing mathematical kernels and v8 are
unchanged.

Dynamic discovery still performs the complete manifest, worker/source, file
inventory, report and current-domain SHA checks in
`fourfold_completed_block_seeds.py`. The controller records this evidence before
calling the unchanged `validate_saved`, including its full finite first-integral
check. It then applies exactly the same ordered integration, local fees, time
seam checks and final 550-segment completeness gate. A missing block does not
create a zero-density leaf and does not advance the cumulative time endpoint.

The non-`main` function ASTs of v8 and v9 match exactly. A real probe on the
actual exact reference and field-domain cover used an empty block directory,
`--seed-only-from 0 --stop-segment 1`, and no `--follow`. It returned code 0 with
`missing_complete_block_seed`, no local process directory, zero completed
segments, and `complete=false`. The precise waiting key is forward segment 0,
normalized subspan `[0,1]`; its genuine field-domain SHA is in the saved index.
This verifies the operational refusal to sample, not a new mathematical leaf.

Probe replay (from the topic directory):

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python -u scripts/fourfold_forward_density_cover_v9.py \
  --seed-only-from 0 --stop-segment 1 \
  --block-directory data/phase_ring_continuation/seed_only_missing_block_probe/empty_blocks \
  --out-directory data/phase_ring_continuation/seed_only_missing_block_probe/g0 \
  --primitive-nodes 640 --bits 320
```
