# Adaptive finite pulse block: a genuinely coupled small-amplitude seed

**Classification: numerical evidence.** This package records a finite Fourier,
finite depth prefix/tail solution. It does not prove a closed isometric family,
an infinite nonlinear tail, or the held 10% requirement.

## Selected physical design

The cut is $r=.3$, $w=.08$ with $w_r=-7w/r$. The original first three cells keep
their nine segment topology, both pulse functions, and their valley functions.
The selected controls change finitely many pulse caps, valley controls and
positive radial warp weights; the physical cells from index 3 onwards are
unchanged. The two ends of the modified block preserve the original radial
location and $w,w_r$. Every candidate in the search is a distinct physical
metric. The selected metric is fully specified by `physical_config.json`.

The optimization varied three valley controls, three outer pulse caps, the
first inner pulse cap, and the first valley radial warp weight. It evaluated
331 actual physical geometries with complete first-mode propagation through
48 cells. A fitted prefix transfer was used only as a ranking surrogate;
the selected prefix was subsequently solved with its actual new canonical
linear port. The selected first-mode leading sensitivity per unit core
amplitude is about $26.74$, versus $57.23$ for the unmodified cut. This is a
first variation diagnostic, not an amplitude bound. In particular, the
second and third physical frequencies have large responses and require the
full nonlinear calculation.

The finite background height is $0.01892083229$. The sampled background
curvature is $9.96547$. The physical cap values are approximately
$(.402265,.00105144)$, $(.04,.000230961)$, $(.025,.000101267)$.
The exact values, the original protected source parameters and all controls
are retained in the configuration, not reconstructed from these rounded
numbers.

## Actual coupled computation

The true prefix/tail seed has design amplitude and actual primary amplitude
both equal to $q=.002$. It uses the complete 8 cosine modes of physical
frequencies $2,4,\ldots,16$, including all nonlinear means, and the original
nonlinear momentum root, flow, acceptance guards and boundary Jacobian.
The tail has 8 physical cells, 144 shooting stages, 32 flow steps per stage,
128 root quadrature angles, and a 48-cell homogeneous far boundary. Its
projection floor is $10^{-4}$ and nonlinear shooting tolerance is $10^{-8}$.
The resulting finite prefix profile has
$\delta=.1718183369254722$, $v_u=.55$, $v_d=.6$, ramp length $.4$,
flat ramp parameter $.05$, one cycle, and a ShortBridge with curvature 4
and peak fraction $.2$. The entire profile and numerical parameters appear
in `seed_record.json`.

The prefix's sampled metric defect is $1.21418\,10^{-9}$; the actual outer
nonlinear boundary residual is $1.05926\,10^{-10}$. The tail shooting
residual is $6.32420\,10^{-10}$, the tail's sampled actual metric defect is
$2.62016\,10^{-14}$, and its minimum chart factor is $.93700769$.
Its dense worker audit reports formal height curvature $9.96527672$.
This acceptance uses the actual nonlinear DN, not the finite linear port.

The upper prefix supplies its full signed physical height vector $H$ in the
intrinsic material angle. The orientation-$+1$ worker receives $-H$. Its
entire $z$ coordinate, including the nonlinear mean, is reflected before
alignment with the upper prefix. There is no replacement of material angle
by spatial polar angle.

The full mean and nonmean height two-jet discrepancies are at most
$1.065\,10^{-10}$. Actual Cartesian comparison then uses 512 identical
material angles and permits only one rotation about the $z$ axis and one
translation. It yields the following sampled Euclidean sup discrepancies:

| Jet | Discrepancy |
|---|---:|
| $X$ | $1.122\,10^{-13}$ |
| $X_s$ | $6.734\,10^{-12}$ |
| $X_u$ | $2.190\,10^{-13}$ |
| $X_{ss}$ | $1.816\,10^{-10}$ |
| $X_{su}$ | $1.769\,10^{-11}$ |
| $X_{uu}$ | $4.723\,10^{-13}$ |

The planar radial second derivative is evaluated by the existing fourth order
one-sided difference. Halving its profile step from $10^{-4}$ to $5\,10^{-5}$
gives a Cartesian $X_{ss}$ discrepancy $2.427\,10^{-10}$; the two computed
$X_{ss}$ arrays differ by at most $3.183\,10^{-10}$. These are numerical
checks with visible roundoff sensitivity, not certified $C^2$ error bounds.

### Corrected exporter error

The first Cartesian exporter mistakenly inserted the stored cut momentum
directly into the local root. The original `createCompactTailDN.cutJets`
rescales its momentum coordinates by $2^a$ before root evaluation. Omitting
that normalization produced a false apparent $X_{ss}$ mismatch of about
$4.28\,10^{-4}$. The corrected exporter reproduces the source normalization
exactly. Both old output hashes and the corrected hashes are in
`seed_record.json`; the original scratch outputs were retained. This was an
implementation error in a new diagnostic, not a failed mathematical match.

## Sampled geometric envelope

The prefix envelope was sampled at 1,041 meridian locations and 256 angles.
The computed finite tail was sampled at five points in each shooting stage
and 128 angles, using actual Cartesian first and second derivatives.

| Quantity | Prefix | Computed finite tail |
|---|---:|---:|
| Maximum $|X|$ | $1.50074253$ | $1.32900575$ |
| Maximum cylindrical radius | $1.17268423$ | $.300000163$ |
| Minimum $X\cdot n$ | $.77065106$ | $1.27549464$ |
| Maximum sampled Cartesian curvature | $4.08744470$ | $9.96143986$ |

The finite tail increases the mean height by $0.01892077115$. Its sampled
full vector Darboux tensor norm is at most $6.34714\,10^{-11}$. The reflected
prefix envelope suggests a centered diameter bound around $3.00148505$;
the finite tail lies inside that sampled ball. These are sampled quantities.
Continuous enclosures, the remainder of the nonlinear tail, the cap, and
their joins remain to be supplied before applying any reach theorem.
Reach must be assessed from the actual product $K D$ and positive support;
$K=10$ is a convenient sufficient window, not a requirement of the problem.

## Separate direction experiment

Before the coupled solve, the full vector from the linear-port prefix at
$q=.002$ was sent through the true tail at factors $.5,1,2,4$.
All four were accepted, with minimum chart factors approximately
$.9711,.9384,.8637,.7098$. The factor-4 worker curvature was $11.6648$;
the attempted factor 8 failed the initial $D/S/A$ guard. This is a finite
continuation outcome on one chosen boundary direction. It is not a capacity
upper bound and not a coupled prefix at four or eight times the core
amplitude. It must not be substituted for the true coupled continuation.

The exact seam implication is already covered by this topic’s R12, `results/R12-height-metric-jets-determine-cartesian-seam.md`. This experiment adds the actual 512-angle Cartesian comparison and finite-tail geometry; the independent Gauss–Weingarten argument is a cross-check of R12, not a new theorem.

## Reproduction and remaining work

Only code, physical parameters, scalar records and artifact hashes are
included. Recomputable ports, vectors, meshes and checkpoints stay outside
the repository. Recover dependencies from a partial checkout and run:

```bash
python recover_sources.py --repo REPO --output RECOVERY
OPENBLAS_NUM_THREADS=1 python reproduce_seed.py \
  --repo REPO \
  --source-topic RECOVERY/bundle/topics/visible-flexible-closed-surface \
  --prefix-recovery RECOVERY \
  --output NEW_SCRATCH_RUN
```

The optional `--continue-amplitudes .004 .006 .008` follows each successful
pair of actual prefix and tail checkpoints. The design computation allows
the prefix profile parameter to vary with amplitude; fixed-parameter mode,
quadrature, radial and depth refinement is a separate requirement. The
worker physical metric is fixed throughout that continuation.

`manifest.json` identifies every bundled source; `sources_manifest.json`
identifies immutable upstream source blobs. `seed_record.json` gives exact
run parameters, amplitude conventions, numerical results and archived output
hashes. Regenerated worker/port metadata embeds paths, and gzip headers may
depend on creation time; relocated runs can therefore have different byte
hashes without changing the equations or numerical physical parameters.
No mandatory independent rerun is imposed before using these recorded
finite results. The complete held-10% problem remains open.
