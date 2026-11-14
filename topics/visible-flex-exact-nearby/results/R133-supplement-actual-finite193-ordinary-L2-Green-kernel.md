# R133 supplement: actual finite193 ordinary L2 Green kernel

## Actual public run and the precise scope

Public Actions [run43633074696](https://github.com/Rogerhu12/math-research-public/actions/runs/43633074696) completed the new kernel child with return code0 and all9 gates. The mathematical child took185.005036227 seconds. Its source is `scripts/fourfold_codazzi_finite193_L2_Green_kernel.py`, SHA256 `5b8f83906d36363266977441427add053a6ed05625525cfd000e05e03360b3db`.

This is an ordinary $L^2_r$ source inverse bound for the **complete finite193 compressed BVP** at the same continuously repaired M32 centre, fixed physical $\eta_0$ and original $\nu$. It retains all96 odd rows, all97 even rows including the independent even mean, the actual low97 cap boundary, and all96 waist constraints. The infinite high block and the true cap low/high cross blocks remain separate inputs.

The source did not re-evaluate the target, the large arrays, the cap, the body, the mean flow, the Riccati graph or the projectors. It consumed the original complete Green native from run43601964129, SHA256 `fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6`, and its exact artifact process SHA256 `297cb4c9b8f58bbaacbcf1d0be594f43ea385420f8ea58fbb14e83bf84a63a1c`.

## Proven operator bounds

The input is the ordinary pair $L^2$ norm on $[0,9/10]$ with normalized circular angular measure. The independent even mean has weight1. Let $G_L$ denote this finite BVP inverse with homogeneous waist and cap loads. The actual complete kernel bounds give:

| Output | Outward decimal upper bound |
| --- | ---: |
| $L^2([0,9/10])$ | $22386.327560863$ |
| $L^2([0,2383968743003/10^{13}])$ | $10488.564543774$ |
| $C^0([0,9/10])$ in the ordinary angular pair norm | $181981.908212897$ |
| $C^0$ on the same fixed negative window | $181981.908212897$ |

These are upper bounds on the indicated inverse operator, not lower bounds on an actual response. In particular, a large displayed constant does not prove a large actual error. The fixed negative endpoint belongs to the current physical background; changing $\delta$, $\nu$ or the nonlinear centre requires the separately identified transfer.

The original genuine boundary columns are preserved, with their original units:

| Input load | Full inner-body $L^2$ | Fixed negative-window $L^2$ | Full inner-body $C^0$ |
| --- | ---: | ---: | ---: |
| Unit waist load | $5367.466583150$ | $2515.284296031$ | $43632.849880657$ |
| Unit true low97 cap load | $7084.386904087$ | $3319.054557912$ | $57587.666669591$ |

Thus arbitrary ordinary body forcing and these boundary loads have a common, fully specified finite-dimensional solution space. This result does not substitute an $L^\infty$ unit-source bound for an $L^2$ source bound.

## What was integrated

The complete original event list contains6391 continuous intervals and5970 genuine secant/tangent interfaces, including the virtual waist interface at $0^-$. All of them passed the identity and complete-cover checks. The original positive graph retains a full-suffix no-pole margin above $.9193997829227$, a mixed-jump denominator above $.9999999999878$, and a final waist margin above $.4182689997615$.

Only the small signed kernel integral was new. For each constant comparison generator $A$, the source computed

$$
G(h)=\int_0^h e^{tA}e^{tA^\mathsf{T}}\,dt
$$

with a four-dimensional augmented matrix exponential. It kept the signed off-diagonal Gram entry through each complete quadratic form before rounding upward. Three independent public algebra gates checked the zero generator, a positive upper shear and a negative lower shear.

The backward sweep formed the squared norms of the future source kernels. The forward sweep retained the disjoint past/future source supports and the entire node Gram. Every original interface was consumed. Whole-cell bounds used the original positive graph and physical weight, one local Minkowski step, and the actual radial measure. All6391 kernel integrals and6391 whole-cell bounds were newly evaluated; none of the old6391 ports was recomputed. The proof and normalization are in `notes/2026-11-14-R133-finite193-ordinary-L2-Green-kernel-contract.md`.

## Exact evidence and rule checks

The published directory is

`notes/finite193_L2_Green_kernel_ci/run-43633074696-1-finite193-ordinary-L2-Green-kernel/`.

| Record | Bytes | SHA256 |
| --- | ---: | --- |
| `process.json` as read from the repository | 8121 | `7689ee4fb3a99cdaa47c7cdb5262b0419a16964a99a1dcf12cbc97df6a68a3c8` |
| `evidence/complete-finite193-ordinary-L2-Green-kernel-summary.json` | 20010 | `fd88f3dd72c3983ca011d1a66520f91db0c7108118611c3a5b99f97f195fe9be` |
| `native/complete-finite193-ordinary-L2-Green-kernel.json.gz` | 18075636 | `ac4441cb98afabbbc646697434caebf464a22f702e2d0fa7d8e5910efd7ef448` |

The full native is preserved as10 exact byte parts with its lossless manifest; no native binary was transferred through the connector. The process has4 actual pull/README checks, each with empty rule diff. Its last read commit is `feb5a20e5e99b58515667500f7d5ce4fb61a8b82`; the separately reviewed rule commit remains `ee26c0a65a2e63c15f2ccfba6714181584416542`. The worker and97-file manifest SHAs are respectively `368b9b0eb613fa7c508adcae6fb3fbd92193413ac879b1a7ab21d7721492f314` and `fb2336796edcd9ccc57a082015cdb6c51ee7c47a921ce03a3cbf3bbab6181ff6`.

## The remaining feedback problem

This supplies an actual $G_L$ in the ordinary $L^2$ space needed to combine with ordinary high-block sources. It supplies neither the negative-region high BVP inverse $G_H$ nor the inverse of the complete head/high Schur feedback. The actual cap cross blocks, both directions of the body feedback, independent mean, and the parameter/nonlinear-background transfers remain in that problem. The existing particular $\nu$-source bounds and this uniform finite inverse bound remain distinct certificates. No full PDE response error, true parameter Schur, or completed nonlinear existence claim is made here.
