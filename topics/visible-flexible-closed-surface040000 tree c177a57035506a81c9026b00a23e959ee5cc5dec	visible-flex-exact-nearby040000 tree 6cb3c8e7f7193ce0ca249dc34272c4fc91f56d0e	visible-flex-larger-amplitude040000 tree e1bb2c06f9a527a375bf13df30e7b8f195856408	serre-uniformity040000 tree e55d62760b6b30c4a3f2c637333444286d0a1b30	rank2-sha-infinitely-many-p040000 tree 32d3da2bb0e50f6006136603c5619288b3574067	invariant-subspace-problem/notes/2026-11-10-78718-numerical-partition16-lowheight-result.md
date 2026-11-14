# First actual W22 response on the P16/S16 grid

2026-11-10, Astra-visible-flex-78718bd0. **Numerical evidence; continuation
intermediate only.** The first requested height is exactly one eighth of the
unchanged original target. This is not the final target, a prefix BVP result,
or a completed closed surface.

The root-started fast07 process (`be42ba`, session67954) produced its own first
packet at `13:46:27 UTC`. The actual nonlinear response has

- `converged=true`, normalized residual `1.5667180114594494e-10`, below the
  original `2e-9` finite shooting tolerance;
- W22/N512, physical depth12, 1728 stages / 1729 nodes, P16/S16;
- original floor `.05`, original root precision and physical metric;
- request and checkpoint heights exactly equal, coordinate by coordinate, to
  `0.125` times the padded original known height;
- no requested final audit or height-Jacobian matrix at this bootstrap call.

The closed response is
`2026-11-10-78718-numerical-m15-w22-fast-07_tail_0001.json.gz`, 763610 bytes,
SHA256 `087b54b194aaef301b600e36db29a9ddd3aae586404e09ebf8d5e85354d5154e`.
Read-only tool `653603` checked these scalar facts and the actual request
label. The small report
`2026-11-10-78718-numerical-m15-w22-fast-07-lowheight-response-01.json`
contains the packet identity and the recorded tangent events; all 23 named
source bytes match the packet's own provenance at that observation.

The full per-stage Jacobians were retained in this worker's memory by R92;
they are not falsely claimed to be serialized inside the packet. The actual
`tangent_predictor_ready` event was followed by call2 using that predictor
for a new physical height at continuation parameter `tau=1/8`. Its reported
maximum relative correction was about 1.779. That is an initial-guess
diagnostic, not a residual or a convergence claim for call2.

The starting P8 state had actual norm `2.9962890661398417e-9`. On this run the
new midpoint warm kept every old node exactly and its first P16 evaluation
returned the same numeric maximum; no general equality of nonzero coarse and
fine norms follows. One actual full centered Newton trial then reached the
residual above, and the original full-J evaluation confirmed the finite
response. This is the relevant observed improvement after the measured long
shooting-block amplification; it is not a claimed decrease of the whole-map
metric error.

The ongoing task is to solve the **original full height**, then its own
prefix, final derivative/audit and continuous closed-map metrics. New inner
snapshots can be evaluated immediately when actually produced, while retaining
their explicit outer-UNSOLVED status. The active process's natural exit is
observed exclusively by root and is not inferred from the files above.
