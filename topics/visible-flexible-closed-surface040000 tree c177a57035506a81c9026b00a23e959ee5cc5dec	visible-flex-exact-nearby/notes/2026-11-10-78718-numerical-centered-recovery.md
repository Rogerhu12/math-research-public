# Fast06: centered trials and unchanged-state recovery at the original precision

2026-11-10, Astra-visible-flex-78718bd0. **An actual new numerical attempt;
not a solved DN or closed surface.** The parent started it with `3afd01`,
session `27279`, and exclusively observes that process.

## 1. Why this branch was selected

Fast05 naturally exited 2 (`9fa811`) at the unchanged original `2e-9` target,
after the original ten trial steps did not reduce a norm of
`3.3366011642270125e-9`. The permitted one-stage experiment subsequently found
that original/tight roots and state flow with/without Jacobian gave identical
state values. The root thresholds therefore did not explain that stage's
failure. The optional tight-root entry remains available, but was not selected
for fast06.

The separate zero-direction retraction experiment found a concrete arithmetic
effect: the old v2 coordinate roundtrip changed high momentum components by
roughly `1e-18`. For this stage the momentum-to-momentum block has a maximum
entry about `1.97e6`; a real repeated flow raised the norm from `3.33660e-9` to
`3.99009e-9` despite a zero Newton direction. The normalized residual change
was about `1.08147e-9`. These are actual local observations, not a global error
bound. They support removing the constant coordinate-conversion bias.

The new helper
`78718-tail-geometric-newton-retraction-centered-v3.mjs` implements the same
real-arithmetic R95 retraction as

$$
\pi_{trial}=\pi_{base}+
\big(C(raw+\lambda\,\delta raw)-C(raw)\big)_\pi,
$$

with the correct node0 port conversion applied to the increment. Q retains
its original canonical linear direction. The base conversion is prepared once
per Newton direction. A truly zero direction returns the same coordinates in
floating arithmetic, including signed zero. The mean equation, its original
precision, the original root, F, J, branch floor, ten trial steps and residual
decrease criterion remain unchanged. R95 contains the full mathematical and
numerical scope; zero bias does not guarantee whole-solver convergence.

## 2. The same state and same H are actually reused

The new worker is `78718-prefix-tail-geometric-centered-worker.mjs`.
When M, N, shooting parts, steps, physical depth, raw-node map and dimensions
are unchanged, it copies the supplied canonical shooting state directly.
It does not perform a raw Q/L conversion merely to reload identical data.
If the actual next requested height is also equal to the stored cut height,
it directly reuses those copied states, without amplitude scaling or a zero
boundary correction. The original full residual is still reevaluated.

The recovery file is the actual fast05 iteration-3 snapshot, explicitly
`iteration-recovery-only` and UNCONVERGED. It contains 865 W22 nodes and is
385541 bytes, SHA256
`18996bebb3b93b2b092c31e7e16f956a3826071133d40c01ac20dfe931adf7d9`.
Read-only `f50e2b` established that its cut height is exactly the same array
as `.125` times the padded known seed height. Its initial amplitude ratio is
1, not another 1/8. The known successful W15 packet still determines physical
parameters and the original target H; it is not reclassified as a solved W22
packet.

## 3. Actual command

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  topics/visible-flexible-closed-surface/scripts/78718-run-prefix-mode.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier \
  --tail-jacobian fourier-root --tail-predictor tangent \
  --tail-trial geometric-centered --tail-root-precision original \
  --bootstrap-height-scale 0.125 \
  --max-nodes 8000 --data-gib 6 --node-heap 1536 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz \
  --tail-initial-checkpoint topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-05-iteration3-root-diagnostic-input.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-06
```

The shooting grid remains P8/S32. Original root/mean tolerance is `8e-14`
with the original `5e-12` root fallback. Floor is `.05`, finite shooting
tolerance `2e-9`, and the physical metric and final requested H are unchanged.
First H/8 success, if obtained, is only a real continuation starting point;
the run must still return original H and solve the prefix/true-tail coupling.

## 4. Actual initialization observation

Limited syntax/selection checks were `437671` and `2586ae`, both exit 0,
with no worker/solver execution. After the parent's actual startup, read-only
`84b708` observed these completed trace events:

- `13:17:42.826Z`: same-grid canonical copy, 865 nodes, W22/N512, max Q change
  0, max momentum change 0, zero root calls for the copy, original UNCONVERGED
  scope retained.
- `13:17:43.048Z`: actual height equality true; raw reprojection calls 0,
  amplitude scaling calls 0, boundary correction false and actual canonical
  boundary mismatch 0.

The actual ready labels were centered-v3, original root precision,
Fourier-root/product moments and full-shooting tangent. The 12 recorded
selected source bindings matched the observed source bytes. This was a
read-only provenance/initialization check, not a new acceptance gate. No tool
session was consumed by the observer and no natural exit was inferred from
the live file's status field.

Read-only `2970f7` subsequently found the first actual full evaluation at
`13:20:13.287Z`: norm `3.3366011642270125e-9`, with the same stage12/frequency63
maximum, A and D as fast05 iteration 3. Thus the resumed numerical F itself,
not only an initialization label, was reproduced. The newly exposed existing
RHS counters reported 110800 roots, zero roundoff fallbacks and an overall
maximum relative root residual `7.998222187192424e-14`. This overall maximum
does not identify the roots along stage12, which the separate one-stage test
had already measured much more accurately. There was still no completed
first response or tangent-ready event at that read-only observation.
