# Expanded frontload range: unchanged finite design candidate

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Heuristic / numerical design conclusion.** The actual floating LP with
frontload increment in [-0.04,0.04] returns exactly the saved candidate from
the earlier [-0.02,0.02] run at q increment 0.008, size cap 1.035 and full-core
tail multiplier 4. All eight saved controls, complete core increments, profile
increments, three extrema and reported geometry are equal as saved Float64
values. Lambda is -0.0015957928829956744, strictly inside both ranges. This run
does not support the earlier suggestion that the positive lambda bound was
the principal restriction in this particular scenario.

The actual reader retained the same seventeen fields and all 306 complete
chunks. All 14,453,760 curvature/size rows were replayed. The fine M32 core
remained the accepted q122 core, with the coarse twenty-eight directional
entries padded by four zero increments, and all five original weighted tail
budgets were replayed. The original trust 256, k0 interval [-0.064,0] and
vd interval [-0.004,0.001] were unchanged. The producer preparation preserves
the original tail-solver AST. This is an old-point design model, not a current
or fine Jacobian, a nonlinear domain certificate, or a new accepted solution.

The predicted kappa-times-size is 33.53431528137435. The identical candidate
already has a complete actual M32 warm evaluation: 33.52518911003503, above
100/3. Its original floating-grid orientation rejection and the subsequent
explicit exact-chart-order bridge remain in their original archive. The
present diagnostic does not alter those outcomes and does not rerun the
identical warm field. The exact equality comparison does not establish exact
LP optimality or impossibility of another physical construction.

The stored model has active positive vd and zero k0 bounds and weighted tail
budgets at frequencies 32 and 48, within its original floating replay
tolerances. These observations explain the returned finite candidate only;
they are not a complete dual certificate or a proof of a mathematical
obstruction. The next local model will use the genuinely accepted new M32
point and add the existing physical descending_sync_curvature control.

## Reproduction and storage

The resource file contains the exact executed command, ownership and wait4
result. Run from the original geometry-work directory with single-threaded
BLAS/OMP/MKL settings. All actual field manifests and regenerable arrays stay
under their previous identities; no new ODE, Node worker, direction field or
large data copy was used. The compact archive includes the real result and
the source preparation, not just the displayed scalar summary.

Owned execution: exit 0; 76.063592106 seconds; peak 187584 KiB.
