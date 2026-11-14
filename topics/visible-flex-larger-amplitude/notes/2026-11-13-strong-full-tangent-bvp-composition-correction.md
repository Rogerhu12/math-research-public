# Full-flow BVP entry composition correction

The first actual q106 launch exposed a Python entry composition defect before
any Node worker or numerical solve. The storage transformation was installed
inside the complete-call cache builder and looked for the young-space guard
import that the outer resource builder had not yet inserted. The original
source-anchor check correctly rejected this construction.

The owned r1 resource record reports exit 1, 0.5137131939991377 seconds, and
17940 KiB peak RSS. This is not a nonlinear rejection of the q106 design.
The exact launch plan, resource, ownership, heartbeat and stdout records are
retained in `2026-11-13-strong-q106-full-tangent-v2-preparation-manifest.json`.

The earlier `strong-full-tangent-python-transform-check.json` checked a
constructed source transformation and imported the client; it explicitly
performed no actual BVP. The earlier q096 prepare-only check exercised the
accepted-storage audit entry. Neither establishes that the original actual
BVP entry composed its wrappers in the same order during `main()`.
The independently completed q098 same-H full audit, exact binary roundtrip,
and separate production-worker startup remain valid; those use the unchanged
storage client and worker, and did not call this defective actual entry.

The fresh `strong_full_tangent_actual_bvp_v2.py` adds one explicit hook to the
SHA-checked retained cache entry: the storage transformation is applied to the
completed resource builder. The original cache, fixed physical merit, disk QR,
actual BVP and secant construction remain in their original order. It keeps
all original full-H, full-Jacobian, positivity, RMS, physical boundary and audit
gates. No frozen MJS or physical parameter was changed.

Source SHA-256:
`44a0c4c06a6171ddb2219b58bbdbfb8336aacf3454f674bdfdba874b9bdf81d5`.
The v2 actual entry has now passed its real `--prepare-only` path with the
complete q098 inputs and exact q106 target. The new r2 launch then restored
all 576 stage flow Jacobians under the unchanged full snapshot identity and
actually called the original full-state predictor at the new 28-component H.
Its first complete nonlinear residual was 3.4346892659157238, with positive
minimum leading factor 0.8753963192805541 and D 0.9999346366928967. The original
Newton correction is running; this note asserts no accepted q106 solution.

The preparation manifest has SHA-256
`931e6a4aca067a117c123b085cacecee883f2b127673c772845b9824247f79b4`;
its 11 files total 90139 bytes. The r2 launch plan is separately frozen as
`2026-11-13-strong-q106-m28-sixctrl-actual-r2-launch-plan.json`, SHA-256
`85bdc1d299bb770f6a093f1ba2a9d19467a13e300100d54446c488fb05f820ae`.
