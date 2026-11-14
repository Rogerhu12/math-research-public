# Angular quadrature as a fixed-metric cost reduction

Status: **component numerical evidence only**, 2026-11-09. The active
M12 and M16 nonlinear solves have not been interrupted or changed.

The optional outer true-DN/inner affine-prefix algorithm already reduced
the completed M8/128 coupling to four actual tail calls. The next obvious
cost is the angular quadrature in each variational RHS. This quadrature
belongs to the numerical representation and does not recalibrate the
frozen physical metric.

`db6f-prefix-tail-quadrature-check.mjs` reconstructs the same physical
tail and evaluates the *same saved state* with the unchanged engine at
256 and 512 angular nodes. It compares the complete nonlinear root,
split-flux RHS, and analytic Jacobian. The sampled locations include both
ends of every stage in raw cell zero and both ends of the first/last
stage in every represented raw cell. No numerical data arrays are printed.

| Input state | Stage endpoints | RHS relative difference | Jacobian relative difference | Root relative difference | Measured N256/N512 time |
|---|---:|---:|---:|---:|---:|
| M12 actual response, call14 | 116 | 3.56e-14 | 8.99e-16 | 1.60e-15 | 181 / 362 ms |
| M16 raw-preserving warm lift | 188 | 5.72e-14 | 1.03e-15 | 2.11e-15 | 326 / 631 ms |

Each relative difference is the maximum coordinate difference divided by
the largest absolute reference coordinate in that tested vector. The
Jacobian absolute maxima are respectively $9.69\times10^{-8}$ and
$1.79\times10^{-7}$ because some background-scaled Jacobian entries are
large; the reports retain both absolute and relative measures. The
timings measure these component calls, not a complete nonlinear solve,
and are indicative rather than a controlled speed benchmark.

For M12, the sampled minimum leading coefficient is .199341 at N256
versus .199277 at N512. This difference is expected because the minimum
is itself sampled on a different angular grid; it is not evidence of
different root coefficients. For the M16 warm state, both sampled minima
are .191679188. No result here certifies the leading coefficient between
sampled angles or at future Newton iterates.

These observations support a practical continuation path: use N256 to
obtain the next high-mode warm solution, then re-solve the **actual**
nonlinear DN at N512 and perform the final original boundary and seam
checks there. They do not justify replacing the final true response by
a lower-quadrature surrogate. The M16 input is explicitly an unsolved
raw-preserving lift, so its component agreement is not an M16 solution.

The engine requires $N>4M\,\mathrm{spacing}$. With spacing three, N128
is invalid for both mode counts. An exploratory first invocation included
128 and was rejected before any diagnostic was accepted. The checker now
validates this requirement and defaults to the admissible pair 256/512.
No engine guard was modified.

Reports:

- `2026-11-09-db6f-prefix-tail-quadrature-m12.json`;
- `2026-11-09-db6f-prefix-tail-quadrature-m16-raw-warm.json`.

Reproduction example (M12):

```bash
node topics/visible-flexible-closed-surface/scripts/db6f-prefix-tail-quadrature-check.mjs \
  --source-root /workspace/scratch/1dce210849f9/math-research \
  --config topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64-tail-config.json \
  --checkpoint topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64_tail_0014.json.gz \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-tail-quadrature-m12.json
```

For M16, use the matching `fixed-m16-d12-p8-s64-outer-tail-config.json`
and `fixed-m16-d12-p8-s64-outer-raw-lift-warm.json.gz` inputs recorded in
the second report. The source dependency snapshot is retained in
`2026-11-09-db6f-prefix-source-dependencies-v2.json`.
