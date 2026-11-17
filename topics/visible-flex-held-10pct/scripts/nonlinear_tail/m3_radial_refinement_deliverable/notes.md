# True radial BVP refinement of the accepted fixed-metric m3 pair

**Numerical evidence.** The physical metric, complete physical tail,
angular chart, gauge, phase range, Fourier order and tail discretization
are identical to the accepted M16/parts8 result. Only the radial initial
mesh and the prefix collocation tolerance change. This is a new nonlinear
solve, not resampling an old interpolant.

## Initialization and original acceptance

The original saved-mesh initializer first checks the frozen profile,
physical tail parameters and cut, complete chart, angular-chart kind, and
warp reference. The wrapper then retains its 983 checked nodes and adds
every interval midpoint, producing 1965 initial nodes. It evaluates the
old represented field only to supply the initial guess. The unchanged
nonlinear BVP adapts to 2462 nodes and achieves maximum RMS residual
9.96865e-9 at tolerance 1e-8. All old physical nodes remain in the final
mesh to at most 2.221e-16 coordinate roundoff.

The actual nonlinear tail is recomputed for the full new signed height
vector, including every mode and the nonlinear height means. Its true
outer boundary residual is 3.024e-14 and final shooting residual is
1.16071e-9, passing the unchanged original 2e-9 gate. No positive-root,
radicand, line-search or acceptance condition has been relaxed.

The gauge input remains .02; the primary support amplitude is an unknown
of the fixed-metric solve and changes from .020001225708876868 to
.020001546225852943. It is reported separately rather than silently
rounded to the gauge. The fixed physical delta remains
.06105607686781097. The complete physical-metric descriptor SHA remains
`11a9de4da186d04dd1e925678582b0f6861425b4e0e2217937ec53ba052db125`.

## Actual saved C2 map, with the same audit definition

| Quantity | Coarse M16 | Refined M16 |
|---|---:|---:|
| Radial nodes | 983 | 2462 |
| Prefix tolerance | 3e-7 | 1e-8 |
| Prefix metric FFT l1 | 4.97063945e-9 | 5.84547643e-11 |
| Full Cartesian Darboux tensor FFT l1 | 9.01498183e-6 | 1.94700116e-6 |
| Tensor at saved knots | 2.95947e-11 | 2.38220e-11 |
| Tail actual metric | 1.58728586e-11 | 1.58737468e-11 |
| Tail fullD | 2.73543602e-7 | 2.73591482e-7 |

The prefix metric drops by about 85.0 times and its full tensor defect by
about 4.63 times. The tail uses the same discretization and its errors
remain at that level; this experiment makes no claim of an additional
tail-resolution improvement. The worst prefix tensor remains inside the
near-cut bridge, now in an interval of width .000242919. Its second jet
comes from the saved quintic representation. ODE-jet replacement is only
a separately labelled localization diagnostic, never the accepted map.

The same material-point comparison of both saved maps includes their
nonlinear mean heights, uses no fitted rigid motion or reparametrization,
and compares all six Cartesian jets. At 5479 radial positions and 784
angles, their supremum differences are recorded in
`prefix-two-map-jets.json`; position differs by 3.221e-7 and Xss by
4.179e-5. Two levels and these finite samples do not prove C2 convergence.

## Complete cut seam and geometry

At 512 material angles, a single global z rotation and translation align
the actual prefix and tail cuts. The position, first and mixed/tangential
second jet differences are at most 1.139e-13; Xss, reconstructed with the
same physical finite-difference step as before, differs by 1.105e-9.
The full mean second-height mismatch is 3.493e-13. This uses the R12
structure and is a finite numerical seam audit. The independent common-jet
Hermite lift makes literal C2 matching and pays its metric cost separately.

Sampled prefix curvature is 8.050636. The tail retains minimum leading
factor .4409074, minimum radicand .99972594 and formal sampled curvature
8.040694. These figures are not substituted for continuous closed-family
reach bounds. The finite Cartesian-tail/collar/disk closure route remains
available; an infinite nonlinear tail is not imposed as a prerequisite.

## Source and reproduction record

The original source closure and sparse-linear correction package are
unchanged. `couple_m3_radial_refine.py` changes only the initial mesh. Its
first attempted invocation failed in the wrapper's argument parser before
any mathematical work: argparse treated `--restart` as an abbreviation
of `--restart-bisections`. `allow_abbrev=False` fixed that wrapper-only
problem. The original failure and before/after hashes are retained.

`replay.py` consumes the earlier source and M16 packages plus regenerated
warm states and reconstructs all arrays in scratch. `record.json` retains
the exact actual command, source/input/output hashes and scalar results.
No DN port, checkpoint, Fourier field, mesh or sampled jet array is stored
in this appendix. The current 10% displacement task is not completed by
this small-amplitude refinement; the next amplitude points must again
solve the complete nonlinear prefix/tail coupling.
