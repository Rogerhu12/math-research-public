# q105 actual continuation: interrupted first-tail solve and same-H recovery

**Status: execution interruption; no accepted new prefix or coupled surface.** The formal Python session 30348 exited 1. The retained worker-close record reports return code −9. The cause is unknown: neither RSS nor elapsed wall time identifies the cause.

The target actual low core remains `(0.105, −0.006655700963004517, −0.0004116733380408847)` with representation gauge `0.09`. M24/N768, original prefix tolerance `1e−7`, node budget 2400, original tail M24/depth8/steps12/parts8/N512/tolerance `2e−9`, and physical full-H boundary tolerance `1e−10` remain unchanged.

## Observed progress

The first complete 24-component Dirichlet request was produced from the full accepted-baseline tangent warm. The tail accepted Newton trials reduced the original residual through `2551.8980258548645`, `0.007626516184192864`, `3.5587182577587475e−9`, and `5.560497277748043e−11`. The last value was retained at `2026-11-12T10:25:12.554Z` as an **unaccepted recovery state**. Its final full variational check, endpoint Jacobian and audit were not returned. No prefix Newton iteration started. The stored recovery contains all 577 states of width 48, all nine shooting nodes/raw states, the complete physical parameters and every component of cutHeight. The complete cutHeight matches the last request bitwise; this is not the old q095 reference H.

The resource wrapper formally recorded exit code 1, no Python termination signal, wall time 774.3368191719055 seconds and wait4 peak RSS 403008 KiB. The child worker itself was reported as −9. These are distinct observations.

## Explicit recovery change

The fresh `...-r2` run changes only output filenames and its warm checkpoint. The new, default-disabled `--tail-warm-checkpoint` option leaves the accepted q095 reference and its true-tail identity intact. It requires equality of every physical/numerical checkpoint parameter apart from the four output/warm paths, checks the complete finite states and raw-state consistency, and requires bitwise equality of the first live complete H before starting the worker. It does not change equations, geometry, tolerances, maximum nodes, full-H rechecking, or final audit. The original loader still performs its own physical remesh and true solve. The saved last norm is not used to bypass any solver gate.

The original production entry was reconstructed exactly and saved as `2026-11-12-strong-actual-q105-r1-entry-source.py.gz`; decompressed SHA256 is `c275e304f9be7bef25b26d46b3ff41e0881eda6ae629957d48b99121ad913393`. The recovery option's precise diff is saved alongside this note. Its stdlib preparation exited 0, with no worker. The fresh run remains pending and will be reported separately.
