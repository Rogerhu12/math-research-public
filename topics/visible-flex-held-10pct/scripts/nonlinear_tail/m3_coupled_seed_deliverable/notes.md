# Original m3 small-cut actual nonlinear seed

## Status and physical identity

This records a genuine finite nonlinear tail and prefix coupling at actual
core support amplitude q=0.02, with the original 950f m3 worker, its complete
nonlinear means and its original guards. It is not a closed-family result.
The physical tail starts at r=.3, w=.08 and uses the original m3 six valley
controls, spacing 3, physical depth 8 and 144 subdivided stages. The exact
finite physical parameters and numerical cutoffs are in tail-config.json.
The resolved positive-root guard remains projectionFloor=.05 and the tail
shooting tolerance remains 2e-9. No guard was relaxed.

The prefix uses vu=.45, vd=.50, flat ramp .4, eta=.05 and the explicit
ShortBridge K=4, peak_fraction=.2. Its design parameter after true coupling is
Delta=.06105607686781097. The numerical angle chart is regenerated from the
recorded reference profile; it is not part of the physical metric.

For an upper prefix the material angle at the cut is the intrinsic identity
angle, not the spatial polar angle. The orientation+1 worker receives the
complete represented vector -H at frequencies 3,6,... . The entire worker z,
including its nonlinear mean, is reflected before gluing. The cut change of
coordinates is r_s=-1/sqrt(E), r_ss=-w*w_r/E^2.

## Actual computations

The recorded warm path first used the fast55 complete q=.02 upper height at
signed multipliers -.001,-.003,-.01,-.03,-.1,-.3. All six were accepted. A
single further step to -1 failed the original Newton line search. This is a
finite numerical failure, not an upper bound on geometry or amplitude. The
accepted -.3 state was then used to warm the fast45 complete height through
-.4,-.5,-.6,-.7,-.8,-.9,-1, all accepted. At full fast45 input the nonlinear DN
differs from the original linear-prefix radial slope by l1=2.78708e-6.

The actual coupled solve then recomputed both the prefix and the full tail,
including the higher harmonics. For example the final worker first three
height modes are approximately -5.43962e-5,+6.65433e-7,+3.99877e-8; this is
not a scalar rescaling of the original linear endpoint. Generated H arrays
and checkpoints remain outside the repository, and their hashes are recorded.

| Finite diagnostic | q=.02 design M8 | Same physical g, fixed M8 |
|---|---:|---:|
| Actual support amplitude | .02 | .020001225073149356 |
| Prefix nodes | 743 | 983 |
| Prefix solver tolerance | 1e-6 | 3e-7 |
| Prefix metric FFT l1 | 2.7467254e-8 | 4.9706313e-9 |
| Prefix full Cartesian Darboux tensor FFT l1 | 2.9745911e-4 | 9.0149823e-6 |
| Tail fullD | 2.3438393e-6 | 2.3453588e-6 |
| Tail actual metric | 3.1843594e-10 | 3.1863756e-10 |
| Tail minimum A | .442031289 | .441994328 |
| Tail formal maximum curvature | 8.04068687 | 8.04069205 |
| Height two-jet seam, maximum of four reported components | 4.01644e-9 | 6.16551e-12 |

The fixed M8 comparison preserves the full physical profile, tail and angle
chart. Its support amplitude is an output of the fixed-metric problem, so the
small change in q is explicitly recorded. Its original fixed-metric source
also inserts all angular spline knots into the radial collocation mesh.
This and the tighter radial tolerance are simultaneous numerical changes;
the 33-fold full-tensor reduction must not be attributed exclusively to one.

## Full Cartesian seam and finite geometry

The q=.02 design seed was reconstructed on 512 identical material angles.
Only one global rotation about z and one translation were fitted. The
Euclidean maxima for X, X_s, X_u, X_ss, X_su, X_uu were respectively
4.113e-12, 3.556e-10, 7.704e-12, 8.601e-9, 3.453e-9, 2.667e-11. The planar
radial second derivative in the tail uses the source fourth-order difference
with step 1e-4. These are numerical comparisons, not rigorous interval bounds.
The proof governing height/metric-to-Cartesian seams is the existing R12;
this calculation is an actual physical check of its hypotheses and defects,
not another seam theorem.

At the cut the stored shooting momentum is post-port normalized. The exporter
undoes it by multiplying its momentum components by 2**a exactly as the
original cutJets method does. Omitting this factor is an implementation
error; the provided exporter contains the correct normalization.

The prefix sample has max norm 1.145729193, minimum support .803179078 and
maximum curvature 8.050355002. The reflected centered sample therefore has
2*maxNorm=2.291458385 as a sampled enclosing diameter value. This is not a
continuous bound. The computed finite tail has height increase .0225432431,
max norm .841287496, minimum support .787232472, max sampled curvature
8.02930676 and max full Cartesian tensor 1.1354017e-6. Its maximum radius in
xy is .3000012745. These reports use the actual nonlinear mean throughout.
The core phase support difference is approximately .04, which would only be
about 1.75% after division by the sampled diameter; it is not a whole-surface
held-displacement witness.

## What the prefix tensor defect measures

After the exact angular chart chain rule, put
Hss=Xss, Hsu=(Xsu-(a_s/a)Xu)/a,
Huu=(Xuu+a*a_s*Xs)/a^2. The original full Cartesian defect is

T = sym(Hss tensor Huu) - Hsu tensor Hsu
    + (a_ss/a)*(I-Xs tensor Xs-(Xu/a) tensor (Xu/a)).

For an exact isometry these covariant Hessians are normal. Gauss gives
Hss_n*Huu_n-Hsu_n^2=-a_ss/a, so T vanishes with the displayed sign. The
implementation reconstructs the same physical derivatives directly; the
reported 2.97459e-4 exactly matches the original source audit. It is neither a
sign mistake nor a residual left in computational angle coordinates.

For the original M8 design, the maximum occurs at s=.1062754286, the midpoint
of a cell of width .0005668023. That cell crosses the angular spline knot
5L/64=.1062770425. The stored C2 quintic has a scalar Gauss defect 1.28853e-4
and tangential Hessian defect 8.50217e-5. In contrast, all collocation nodes
have tensor l1 at most 1.04354e-9. Substituting projected ODE jets at the same
positions also gives about 1.04354e-9, but those jets are only a diagnostic:
they do not replace the saved interpolant or prove it has small C2 error.

The fixed M8 run puts the angular knots into the mesh and removes that peak.
Its remaining maximum is at s=1.3430988984 in a near-cut bridge interval;
it does not cross an angular spline knot. It still has a scalar Gauss defect
7.34356e-6 and therefore still requires refinement. The source script reports
node and interior maxima separately and preserves the actual interpolant.

## Recovery, commands and provenance

Use a new scratch directory outside the git checkout:

```
python replay.py --repo /path/to/math-research-public --work /new/scratch/path
```

The command generates the source cache, literal original worker port,
reference chart, both open prefixes, the complete signed-height continuation,
actual coupled seed and same-g M8 comparison. `--through reference`, `prefix`,
`tail`, or `coupled` selects an earlier concrete endpoint. Every generated
array stays under the chosen scratch directory.

The 70-source manifest pins every source by immutable git revision, path,
SHA256 and byte length. An actual empty-directory restore plus original worker
startup reproduced canonical port8 byte for byte (SHA256
2b036a6f926503f46dddf41c8e141c215dc45340c556641d2fd2b6c192b62365).
Recomputed fast45 reference profile, chart values and cut metadata were also
exactly equal to the ones consumed by the successful run. This check did not
rerun the nonlinear solves.

The historical fast55 open prefix did not save its initial node budget or
whether it used a restart. Known settings are M8, angular384, audit768,
tol1e-6, bc_tol1e-7 and physical_bc_tol2e-9. The replay explicitly chooses a
cold 401-node initial mesh with max_nodes4000 there. This is a reconstructed
replay choice, not an invented historical command. The actual historical
checkpoint and H hashes remain in record.json. The fast45 open prefix and all
our true coupled runs retained their actual command records.

The ongoing M16 attempt is deliberately outside this frozen seed record.
No finite number of levels proves the required fixed-parameter limit.
Infinite nonlinear continuation, pole closure, all-family continuous
embedding/reach, a 10% held witness and a positive Euclidean quotient are all
still unpaid.
