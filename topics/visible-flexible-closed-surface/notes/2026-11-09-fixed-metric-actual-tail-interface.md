# Actual low-curvature tail interface test

Date: 2026-11-09. Author: Astra-visible-flex-4ffd372b numerical subagent. Status: diagnostic / candidate, not a completed construction.

## Question and fixed data

The preceding numerical ellipse prefix used a synthetic Robin coefficient: the old tail slope was rescaled and the cut slope was overwritten. It therefore did not describe the actual low-curvature tail that would be needed for closure. This test uses the recorded actual physical tail with `rCut=.6, wCut=.05, width=.25, curvatureBound=5, slopeCap=.075, prefixR=2, prefixReturnStart=8, prefixEnd=15, protectCell=80, calibrationSteps=1024, warpSteps=16`. The source profile continues into the exact R64 deep source. This source relation alone is not a proof of a nonlinear infinite extension.

The actual linear port is retained unchanged as `fixed_metric_w005_linear_port.json`. Its final row uses linear depth64 and2048 radial steps. The nonlinear diagnostic uses M4, depth8,64 radial steps and128 angular nodes. All results in this note preserve this actual physical tail. Frequency, radial, depth, and infinite-extension certification are separate questions.

## Nonlinear prefix with the actual linear port

The profile `(vu,vd,ramp,cycles)=(.35,.5,.4,1)` has a planar mode2 linear inlet root at delta=.19075359676112422. The same-perimeter ellipse core with aspect1.02 and M4 solves with design delta=.19075415171934706. The solver reports convergence with274 nodes. The reconstructed finite prefix has whole-angle metric l1 diagnostic3.46085e-9, sampled curvature3.64745, maxheight1.86721, and physical terminal noncircular height2.490467207818641e-4. This adjusts the metric during design; it is not fixed-metric convergence evidence. The intended flex parameter is phase rotation of the final single band, so amplitude need not itself parametrize a same-metric family.

## Actual nonlinear response fails at the proposed initial height

Replacing the linear port by the actual nonlinear finite-depth DN fails at its first trial, with `momentum Newton line search failed`. The independently selected split-linear-flux arithmetic gives the same initial failure, so the earlier cancellation repair by itself does not fix this candidate. The source equations, physical geometry, and finite truncation are otherwise unchanged.

A diagnostic integrated every cell from its projective linear shooting seed. At cut fundamental height1e-8 it found a finite nonlinear shooting solution with normalized residual7.82653e-14, min leading coefficient A=.84431795, and minD=.9999999906. Initial trials at1e-7,1e-6,1e-5,5e-5,1e-4,2.5e-4 all fail in the first valley transition, cell0 segment3. At1e-7 the failure occurs near r=.5718915, w=4.12535e-5; at2.5e-4 it occurs near r=.5713544,w=.00244222. The records preserve the exact loop position and state magnitudes. The successful finite response is about25,000 times smaller than the proposed ellipse terminal height.

This is an initialization/branch diagnostic, not a proof that the boundary-value problem has no solution. Warm nonlinear-state amplitude continuation is recorded in `fixed_metric_w005_tail_continue.json`: it succeeds through4e-8 with residual9.63093e-10 and minA=.3184903, then fails at6e-8. The final successful raw state is retained in `fixed_metric_w005_tail_continue_last.json.gz`. Thus the required prefix terminal height is still6226 times the largest successful tested height. It is also not evidence that every other low-curvature tail fails. In particular, the geometric minimum-width calculation for this tail cannot be promoted to a nonlinear feasible interface.

## Code and reproducibility

- `fixed_metric_actual_tail_bvp.py`: actual nonlinear boundary map, with optional split-flux worker and strict matching of physical tail configuration to the linear-port record.
- `fixed_metric_real_tail_line.py`: actual linear tail / planar core matching screen.
- `fixed_metric_tail_probe.mjs`: locate failure of initial cell integrations over a stated amplitude list.
- `fixed_metric_tail_continue.mjs`: warm actual-state continuation of one fixed physical metric.
- `fixed_metric_ellipse_bvp.py`: fixed profile wrapper; replaces the design delta unknown by the extrinsic core aspect. The first low-order synthetic-port attempt failed its mesh budget and is preserved separately.

The scripts import the identified large-amplitude source dependencies read-only. They write only this topic. Raw arrays are gzip compressed without coefficient rounding. No claim about C² round-collar closure, reach, a full closed surface, or the README completion criteria is made.


## New cut-preserving physical tail (root candidate, cap=.02)

The full physical source was snapshotted without changes from
`scripts/root_cut_preserving_tail.mjs` to
`fixed_metric_cut_preserving_tail_snapshot.mjs`. The actual DN factory is
`createSplitFluxCompactTailDN({...cfg,tail:createCutPreservingTail(cfg)})`;
the boundary coefficients have not been rescaled from another metric.
The four actual m=2,4,6,8 linear slopes were taken from the parent s1024/far40
record, with a faithful canonical wrapper in `fixed_metric_cut002_linear_port.json`.

With the gentle vu=.35, vd=.5, ramp=.4, one-cycle profile, recomputing the
linear planar inlet gives delta=.19165367318140422 and cut-height gain
.03541844431985608. Thus this real DN does **not** automatically suppress
the port amplitude by orders of magnitude. The nonlinear Frenet prefix
at axis ratio1.02 and M4 solves to delta=.19165424121675134, metric_l1
3.4613e-9, sampled curvature4.17761, and cut height
.00035068186391583355. This cut height is about85.4 times the parent's
sampled linearized T-positivity threshold4.10773e-6. The result is a finite
prefix with an actual *linear* physical-tail port, not a solved nonlinear
closed surface.

The custom actual nonlinear worker retains full finite shooting states for
every fresh successful response. The coupling now also reports the mean
first and second height jets by the same orientation convention as the
reviewed inward bridge: evaluate DN(sigma*H), then meanSlope/sqrt(E) and
sigma*(meanSecond/E+meanSlope*a_ss). These mean values are not zeroed.
A Cartesian planar two-jet comparison is still separate required work.

## Fixed-physical-metric nonlinear continuation and angular refinement

The cap=.02 custom nonlinear tail, with depth8 and the specified physical source frozen, succeeds at fundamental cut heights1e-8,3e-8,1e-7,3e-7,1e-6. The M4 residuals are respectively6.00e-14,1.32e-13,1.14e-13,3.62e-11,1.69e-13, while the minimum sampled leading coefficients A are .99756,.99269,.97553,.92584,.74430. The next warm attempt3e-6 fails a momentum Newton line search. This is branch exploration and does not prove a maximal amplitude.

At height1e-6, the M4 full normalized Darboux defect is5.5005856e-5 even though the shooting residual is nearly machine precision. The actual metric diagnostic is algebraically tiny and cannot substitute for this full equation check. The M8 calculation at the same physical tail and cut height, with64 radial steps, succeeds with residual1.2538846e-10, normalized full Darboux defect2.9694363e-8, minimum A=.74430557, and sampled curvature5.99879955. The complete record is `fixed_metric_cut002_tail_m8_a1e6.json`; all raw finite shooting states are retained beside the summaries. This small-amplitude finite branch does not meet the visibility or round-collar completion requirement.

The M8 run also repairs the numerical flow integration grid: the cut-restoration transformation introduces an actual zero of dlog(w)/dx in first-cell segment7 at x=.9598247894721866, absent from the inherited raw-source cusp grid. The physical warp quadrature already used the actual derivative roots; the added `actualCuspGrid` worker flag only adds roots for the flow integrator. A128-bracket sign-change search and48 bisections detected the added point; this is not a rigorous enumeration of all possible critical points. This repair plus angular refinement accounts for the M4-to-M8 improvement, so it cannot be attributed to M alone. The physical source snapshot is unchanged. A same-M8 radial step-doubling check is recorded separately.

For the complete Cartesian seam, `2026-11-09-fixed-metric-cut-two-jet-lemma.md` proves a conditional local fact: at a regular cut, equality of complete height two-jets including nonlinear means, together with the same metric and branch, determines the full Cartesian two-jet up to a single planar rigid motion. Current approximate checkpoints still require an actual quantitative seam audit; this lemma does not turn their residuals into an exact seam.

## Independent deep-background audit received
Parent independent audit found the N80-protected background has raw cell80 curvature about342.8467; values near n96,n112,n128 are22.735,1.495,.09768 respectively. Thus every prior sampled curvature≈6 in this note/table only concerns the inspected finite shallow tail. The N80 physical configuration is not a globally low-curvature construction. Parent proposes a new protectCell160 physical profile; it must get a new actual DN and must never be mixed with the N80 refinement table. The N80 calculations remain reproducible local/interface diagnostics only. No further high-M investment in this geometry is planned.

Same N80 physical metric, M8 radial64→128: normalized full Darboux defect 2.96943631906e-08→2.96943653e-08; fundamental slope absolute change 4.48904880146e-14 (relative 7.90755437504e-09); second-height-jet change 5.23722260221e-13. minA .74430557 stable. The finite shooting residual is 3.14481696353e-10. Data fixed_metric_cut002_finite_convergence.json; second raw state fixed_metric_cut002_tail_m8_s128_a1e6_tail_0001.json.gz. Radial audit finished; no numerical jobs remain in this subagent. The independent deep-background obstruction above remains decisive for final geometry.
