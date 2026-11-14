# Parameter index replay and the segment 24 storage interruption

## 1. The observed storage failure

The uniform parameter cover's first process for forward segment 24 returned
code 1. Its traceback explicitly reports `OSError: [Errno 28] No space left on
device` while creating the finite `field_p2` output directory. It had already
reached actual field node 8. This is an output-storage failure, not a failed
analytic estimate. No inference about the cause of earlier signal-9 exits is
made from this later, different event.

The original partial report, process log, command and return code are preserved
under `data/phase_ring_continuation/step5_parameter_density_interruptions/` as
`forward0024_uniform_v5_no_space.json.gz`, the matching `.log`, and
`forward0024_uniform_v5_no_space_note.json`. Afterward `df` observed 5.5 GB free.
No completed certificate or reference shard was deleted. The same frozen
mathematical pipeline was resumed with the same parameter interval, strips and
primitive-node count. A later successful report, if obtained, must be its own
actual recomputation; the interrupted report is not promoted to a certificate.

The next attempt on segment 24 separately returned child code -9, with no
Python traceback and the log only through field node 0. Its log and last-saved
report are preserved as `forward0024_uniform_v5_second_process_signal9*`.
The signal's cause is unknown. This event is not identified with the earlier
explicit storage exception. Center segment 27 subsequently finished normally,
and its controller paused at the next leaf boundary. The independent
`fourfold_parameter_sequential_cover.py` now calls the same frozen cover v4 and
pipeline v5 one parameter child at a time. It changes no arithmetic, source,
domain, node, cap or validation gate. Any abnormal child exit is saved and stops
this operational controller instead of being silently retried.

## 2. A controller replay is not changed mathematical evidence

The existing cover controllers revalidate old leaves from the beginning after
a restart. During that replay their published index can temporarily be shorter
than the preceding index. Both old chronological followers rejected this
shorter prefix, even when every overlapping entry was identical. Their existing
finite integral results remain valid for their explicitly recorded prefixes;
the stop did not demonstrate a source inconsistency.

The independent helper `fourfold_monotone_source_prefix.py` now distinguishes
two cases. Every overlapping entry must remain exactly equal, including its
report path and SHA, g0 path and SHA, segment and exact normalized endpoints.
Any difference still raises an error. If all overlapping entries are equal but
the new index is shorter, a follower waits. It neither integrates a source nor
publishes a new result while waiting. A shortened index claiming completion is
always rejected. A caller that stops during this wait retains only its already
published, explicitly incomplete result.

This is sufficient because the ordered-integral state is a deterministic
function of the already checked ordered list. Reobserving a shorter unchanged
prefix does not change that list. Once the index catches up, its entire old
prefix is compared before any additional leaf is accepted. A permanently
missing suffix therefore cannot produce a completed certificate. The final
gate still requires all 550 segments, unchanged source scope, exact adjacent
time endpoints, and the endpoint `+pi/2`.

The new runners are `fourfold_parameter_density_accumulate_v2.py` and
`fourfold_parameter_hybrid_accumulate_v3.py`. All source checking, directed
arithmetic, retained Fourier products, MVT transfers and error formulas are
unchanged. These runners do not loosen mathematical equality to ignore a
changed `reused` marker or other metadata: the current controllers preserve
their leaf-entry metadata during replay. Any future separation of operational
metadata from scientific identity would require its own explicit implementation.

`notes/2026-11-12-parameter-prefix-replay-validation.json` records actual checks
using the saved 20-leaf index. Equal, shorter, and empty replay prefixes are
classified as intended; a changed overlapping SHA and a shortened index claiming
completion are rejected. Separate replays of the saved 20-leaf center and
hybrid computations compare the full finite `C` and `D` coefficient bytes with
the previously frozen versions; those comparison results are stored separately.

## 3. Neighboring-germ grid diagnostic

The independent `fourfold_parameter_mixed_primitive_caps.py` probe keeps the
actual sampled main germ at Q384 and tests a smaller primitive grid only for
the unsampled neighboring germ's analytic cap majorants. On actual segment 24,
Q128 fails the true refined-root/simple-root gate; Q384 passes the complete
center and uniform cap calculation. The report intentionally has overall
`complete=false`, since one requested diagnostic case failed. This probe does
not produce a density certificate and does not change the frozen mathematical
pipeline or remove the failed case.
