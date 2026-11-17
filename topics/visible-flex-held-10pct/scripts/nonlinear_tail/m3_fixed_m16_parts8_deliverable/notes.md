# Same physical metric: accepted M16 full coupled prefix and tail

This is a finite numerical refinement result, not a closed-family existence
certificate or the 10% held-displacement target. The accepted M16 pair uses
the exact frozen profile, physical tail factory, chart and phase mechanism
of the accepted fixed M8 pair. Its complete physical-metric descriptor has
SHA-256 `11a9de4da186d04dd1e925678582b0f6861425b4e0e2217937ec53ba052db125`.

## What changed and what passed

The original M16 run with two shooting parts terminated in line-search
failure. The all-node sparse linear correction with eight shooting parts
then passed the original nonlinear residual and positivity tests. The
failed state was used only as a warm initial guess. The nonlinear
equations, guards, boundary conditions, line search and tolerance were
not relaxed. The previously frozen sparse-linear proof and cross-engine
comparison are the source of the equivalence claim.

The parts2/steps64 and parts8/steps16 trials both use 128 RK steps per raw
physical segment, with 512 linear steps. Their physical factory/profile
hashes coincide. Regenerated linear DN slopes differ by at most
6.316e-9 from floating-point regrouping; no slope was overwritten to hide
that difference. Compared with the accepted M8 pair, angular order and
total RK resolution both increased, so the tail improvement is not
attributed solely to angular order.

The full actual-DN outer check and the final audited tail passed. The
tail's sampled metric defect decreased from 3.1864e-10 at M8 to
1.5873e-11 at M16; its full physical Darboux defect decreased from
2.3454e-6 to 2.7354e-7. Minimum leading factor remains 0.440917 and
minimum radicand 0.999726. Formal sampled maximum curvature is 8.040692.

## Full Cartesian seam

The seam audit uses the same material angle and the same meridional
direction. Only one rotation about z and one translation are fitted.
At 512 angles, the Euclidean supremum differences for
`X, Xs, Xss, Xu, Xsu, Xuu` are respectively
`7.764e-15, 2.647e-13, 3.315e-9, 2.464e-14, 8.139e-14, 1.896e-13`.
The Xss value includes the finite-difference reconstruction error; the
numerical stage-coordinate difference step .0004 with parts8 has the same
physical radial step as .0001 with parts2. The complete root and metric
are evaluated, including the momentum factor `2**a` and all height means.
This is an actual use of the already established R12 seam structure,
not a new seam theorem or an exact common-jet gluing certificate.

## The radial error that remains

Both fixed M8 and M16 prefixes have 983 radial nodes at tolerance 3e-7.
Their saved C2 interpolants have metric defect about 4.97064e-9 and
physical tensor defect about 9.01498e-6. The worst tensor point is the
midpoint of the near-cut bridge cell of width .000485838. Knot tensor
defect at M16 is 2.960e-11. Replacing second jets by ODE values removes
the observed defect diagnostically, but those substituted jets do not
define the saved map and are never counted as a refined surface.

The angular refinement therefore leaves a clearly measured radial
interpolation floor. A subsequent true BVP solve on the old nodes plus
their midpoints, with unchanged physical g and tighter radial tolerance,
is the appropriate separate experiment. It is not part of this frozen
record. Two older long runs were still active when this package froze;
their then-current iterates are not labelled failures.

## Reproduction and scope

`replay.py` consumes regenerated warm inputs and the already published
m3-seed and sparse-linear source packages. `record.json` retains the exact
historical command, source hashes and input/output hashes. No port,
height vector, checkpoint, sampled field, or matrix array is included.
The replay entry is a concrete recipe; it has not been claimed to be a
new cold nonlinear reproduction from an empty directory. The 70-source
restore and original startup were independently verified earlier.

The available positive-radius collar route closes a finite Cartesian
perturbation with a shared two-jet zero layer onto the rotational
background and disk; it does not require treating depth8 as an infinite
nonlinear solution. Continuous finite-map bounds, the exact common-jet
lift, fixed-g convergence beyond these finite levels, and the complete
closed-family displacement and reach checks remain separate obligations.
