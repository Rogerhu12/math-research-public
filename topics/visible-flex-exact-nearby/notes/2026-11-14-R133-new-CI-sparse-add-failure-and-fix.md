# New cut workflows: actual infrastructure failure and exact repair

Runs [43586317809](https://github.com/Rogerhu12/math-research-public/actions/runs/43586317809)
and [43586726292](https://github.com/Rogerhu12/math-research-public/actions/runs/43586726292)
stopped before any mathematical producer. Git rejected `sparse-checkout add --no-cone`
with exit129: the existing checkout was already in non-cone mode, and `add` does not
accept that flag. This is an invocation failure, not a failed interval or inverse gate.

The two workflows now use `sparse-checkout add` on that existing non-cone checkout.
Their artifact step runs only when its designated output path was actually set;
otherwise an empty path could expand to `/`. The original failed upload reached a
permission error under `/proc`; it is not recorded as a valid mathematical artifact.
No source, original native, scientific manifest or expected numerical hash changes.
The corrected pushes request the two calculations that never started.

The completed nine-consumer phase workflow is changed to explicit dispatch only,
so this artifact-path guard does not rerun its already successful mathematical graph.
Its actual successful run43586895661 and all original fresh outputs remain unchanged.
Future single-consumer work uses those complete outputs directly.

Only the YAML and these exact invocation changes are checked locally. The cut-to-waist
proposal and the complete cap-to-cut arithmetic run directly in the public repository.
