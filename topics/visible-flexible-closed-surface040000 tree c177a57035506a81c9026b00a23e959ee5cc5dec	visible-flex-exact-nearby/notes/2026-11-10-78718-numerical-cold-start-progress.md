# Actual cold H/8 first evaluation: positive samples and residual coordinates

2026-11-10, Astra-visible-flex-78718bd0. **Numerical observation only.**
This note records already completed progress from fast05, whose tool session
is owned by the parent. It does not report a natural process exit, a solved
DN, or any continuous geometric bound.

The first full evaluation, at `2026-11-10T12:40:37.086Z`, has

| Quantity | Actual value |
|---|---:|
| Original normalized shooting norm | 231.56829464834516 |
| Sampled minimum A | 0.9431560339705308 |
| Sampled minimum D | 0.9989638250217566 |
| Worst stage / raw cell / raw segment | 11 / 0 / 7 |
| Worst component | 23, namely momentum index 1 at W=22 |
| Corresponding physical angular frequency | 6 |
| Absolute residual in this coordinate | 0.16811080304582005 |
| Original height scale for this stage | 0.0007259664078845925 |

The existing norm divides **both** the Q and momentum blocks by the propagated
lowest-mode height scale. The new maximum-location observation therefore does
not identify a relative metric error. A read of the same iteration-zero
checkpoint gives the left momentum coordinate `2.243370476663767` and the
incoming coordinate `0.4504723880700926`. The recorded absolute residual is
about `0.07493671009517178` of the left coordinate, while that coordinate is
about `3090.1849621400083` times the height scale. This explains how a norm of
231 can coexist with a coordinate residual of about 7.5%; neither quantity
alone bounds the surface metric.

All values above come from existing records, with **no added root or ODE**.
Read-only observation `e2b04d` found the configured cold branch, no worker
`initialCheckpoint`, H multiplier `.125`, floor `.05`, and the actual selected
R95 mean-seeded-v2 / Fourier-root / tangent implementations. Its closed scalar
capture is
`2026-11-10-78718-numerical-m15-w22-fast-05-cold-first-evaluation.json`.
Read-only observation `afefe5` found the matching iteration-zero coordinate
values. The progress trace and iteration checkpoint themselves remain live
outputs and are not asserted to be immutable inputs.

The original norm and original `2e-9` success requirement are retained. The
positive sampled A and D are useful initialization evidence, not an all-domain
positivity certificate or a convergence guarantee. The maximum at frequency 6
also prevents interpreting this particular first residual maximum as an
observed highest-mode defect.
