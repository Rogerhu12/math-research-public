# A genuinely coupled macro prefix at support amplitude 0.1

2026-11-09, db6f/coupled_prefix. Status: **completed finite numerical coupling**;
not a completed closed surface, a continuous geometric certificate, or an
infinite-dimensional existence proof. The frozen metric is now being refined.

## Physical design and retained state

The new flat-acceleration prefix has

    direction=outward, vu=.17, vd=.18, ramp=.4, ramp_eta=.05, cycles=1,
    delta=.07254443456654512, rCut=.6, wCut=.5.

The formula is specified in `2026-11-09-db6f-prefix-flat-law.md`. The physical
weighted K6 tail is unchanged from the prior work: width=.45, cuff radius=.15,
protectCell160, the same six valley controls, pulse/valley caps and warp weights.
The actual nonlinear DN, including its full mean root, is used throughout the
coupled BVP. Neither a pure first harmonic nor the linear tail DN is substituted.

Full prefix: `2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine.json.gz`
and its coefficient file. Final actual tail:
`2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine_tail_0017.json.gz`.
The matching summary/config/trace/log files retain the commands' inputs and all
17 tail responses. The design took570.61 seconds and ended with778 prefix nodes.

The first direct .8-to1 amplitude jump of the tail failed in its initial root
line search. The successful route uses .85,.9,.95,1 from the saved .8 state;
these are numerical warm-start steps on the same tail metric, not changes to
its geometry. All failed records are preserved.

## Finite numerical diagnostics

| Quantity | Value |
|---|---:|
| q_support | .1 |
| Prefix metric Fourier diagnostic | 1.11865856e-7 |
| Prefix sampled actual Cartesian curvature | 5.11256734 |
| Core support gap, finite exact coefficient candidate | .19995854611194433 |
| Tail normalized shooting residual | 1.35056538e-10 |
| Tail actual-metric diagnostic | 3.16461861e-7 |
| Tail full unprojected Darboux residual | 6.25149463e-4 |
| Tail minimum leading coefficient | .195089443664 |
| Tail minimum D | .991501521856 |
| Tail formal height curvature | 6.42859360 |
| Mean first-height-jet mismatch | -1.06796794e-11 |
| Mean second-height-jet mismatch | 1.33534073e-10 |
| Maximum nonmean first-height-jet mismatch | 1.60897340e-17 |
| Maximum nonmean second-height-jet mismatch | 2.45572556e-9 |
| Cut C1 metric Fourier diagnostic | 4.85804498e-7 |

The core gap and the low sampled metric error make this a viable macro
candidate. They do not by themselves pay the continuous-angle/radial, complete
C2 Cartesian seam, infinite-tail, reach, fixed-H, or noncongruence gates.
In particular the full-Darboux and cut-C1 residuals expose finite-M truncation;
they must decrease in the following same-metric refinement, not be ignored.

## Geometry budget and exact-metric refinement

The immediately preceding linear-port warm prefix has sampled D_ball3.785619358,
positive outward support at least.8178843, and a short-meridian support/height
held ratio.05282056. The true coupled geometry must be recomputed. Root has
constructed a separately shared-jet exact C2 mirror representation and is
working on continuous certificates and the complete tail/cap assembly.

`db6f-prefix-freeze-refine.py` has frozen the displayed physical metric, with
unchanged chart reference q=.1, and launched M12/depth12, angular512, tail
quadrature512, prefix tolerance2e-9, physical BC tolerance2e-11. The initial
same-metric baseline is the completed M8 coupled checkpoint above. All finite
parameters remain fixed except numerical approximation orders, radial nodes and
the finite approximation depth of the same infinite tail. Any change in actual
q in fixed mode is an output error of solving this same BVP, not a new metric
or a manually reduced amplitude.
