# Warm v2/v3 continuous prefix metric entry

Date: 2026-11-26. Session: Astra-held10-06bbeb395471 / fixed_metric.

Status: a new input-bound entry, with actual syntax/help checks; no new
accepted lambda-one field has been fed to this entry and no new continuous
metric or curvature number is asserted. The original R62 field and its
numerical constants are not recomputed or transferred.

## 1. Exact reuse and the new differences

The new [driver](../scripts/resume_20261126/warm_certify_prefix_metric.py)
calls the unchanged `AngleTable` and `PrefixMetric` classes from
[the R62 algorithm](../scripts/resume_m3/certify_prefix_metric_interval_taylor.py).
Their Gram cancellation, interval automatic derivatives, radial Taylor
remainder, angular interpolation remainder, symmetric operator norm, and
optional curvature enclosure are not rewritten.

The deliberately new inputs are:

1. The explicitly versioned accepted warm-v2, warm-v3, or original warm
   actual-DN field. The source gate is
   `seam_certify_true_cut_height.source_model`, so a same-map reexpression
   retains its original solver provenance and an actual-DN source must
   pass the separate complete nonlinear acceptance gate. The default
   requires lambda one. An intermediate-lambda diagnostic is explicit.
2. The actual dimension `n=3*M+1` and all actual state frequencies
   `3,6,...,3M`. The exact shared C2 coefficient/chart construction is the
   independently reviewed [M3PrefixPieces](../scripts/resume_20261126/seam_m3_prefix_pieces.py).
   A core phase frequency `j*pi/(pi/3-S)` is never substituted for a state
   Fourier frequency.
3. Fresh true-core arrays from
   [the warm oracle/exporter](2026-11-26-warm-true-core-interval-extension.md).
   Full run, physical field, current M, complete core definition, provider
   sources, v3 zero-control anchor, and actual projection must agree.
4. Full radial coverage bookkeeping in exact rational endpoints. The
   accepted leaves and complete initial grid are saved outside git.
   An exhausted attempt/depth budget leaves an explicit unresolved box.

The driver binds the original R62 metric source SHA
`6b36ccd6bab54fa35c6fe62a433f417faf7a51b80c35b798b17567eb22714986`,
the original derivative-kernel SHA
`fe99f0afc6ed90dac1b9b3616c857421fa621901958dfbafdbb26191c5766bb2`,
and the reviewed interval wrapper and outward kernel. These are the source
identities recorded by the original R62 execution; none of that execution's
field-specific estimates enters the new calculation. The input helper and
generic exact pieces are also explicitly version-bound. A future new
actual-refinement model kind needs an explicit helper update and review;
the current entry does not guess its parameter semantics.

## 2. One explicit C2 map

The physical NPZ is not silently declared an exactly C2 floating query.
The mathematical object is the exact rational quintic correction selecting
each knot's literal right-side two-jet, with the final knot taken from the
last left polynomial. The angular spline uses the same common-two-jet
construction. The unchanged lift cutoff is used. The prefix amplitude
delta is fixed; its original exact velocity table is normalized once to
the same frozen literal physical prefix endpoint.

Thus the target in this component is precisely

\[
 g_*=ds^2+a_*(s)^2\,d\theta^2,\qquad 0\le s\le s_b.
\]

This is the same explicit endpoint-normalized convention used by the new
true-height driver. It is not a claim of equality to a different rounded
query or to an unspecified globally attached target metric. The once-frozen
delta, reference table and literal endpoint determine this convention;
changing angular/radial verification partitions does not choose a new
profile.

The complete reference lift subtracts the actual literal projection:

\[
 H(\psi)=\Gamma(\theta_0(\psi))-e^{i\theta_0(\psi)}
                   -q I\cdot B(\psi).
\]

The actual full vector `I` is checked byte-for-byte against the mean-core
certificate after reconstructing the field. The output's `H,H1,H2` are
not taken from a truncated or reprojected replacement core.

The mean is exactly the equal-weight average at the original 1168 literal
binary nodes. Its true radial primitive has anchor `Z(0)=0`. The metric
needs this primitive's first derivative and curvature needs its second
derivative; these are enclosed from the analytic integrand jets. This
entry does not claim to have evaluated the absolute height primitive.
That belongs to the separate new true-height certificate.

Shared Y/e two-jets, the C2 cutoff, the piecewise smooth profile, and a
strictly positive fixed-node Frenet domain make the mean integrand C1.
Its true primitive is therefore C2. This is the same exact map convention
as the generic prefix/height components. The source float map is not
identified with this exact C2 interpretation.

For the v3 core, the phase is globally at least C4 and Gamma at least C5.
The angular metric remainder only needs Gamma through order three; the
export also carries Gamma4 for other geometry consumers. The lower
regularity than an old R53-only label therefore does not remove a
hypothesis of the R62 metric algorithm.

## 3. Complete true-angle coverage

Both mean and external certificates must bind the same new run,
physical file, full core definition, actual mode count, oracle metadata,
and positive-curvature core calculation. V3 also requires the full
`phase_basis` and both `basis_anchor_v2` fields to agree.

The external arrays contain true Gamma and its derivatives at each
literal external node, and on every complete closed angular box.
The new explicit check `finite(warp_e) and abs(warp_e)<1` justifies the
endpoint enclosure of

\[
 \theta_0(\psi)=\psi-e\sin(3\psi)/3,
 \qquad \theta_0'(\psi)=1-e\cos(3\psi)>0.
\]

It holds for the current frozen warp .06. It is now a checked precondition,
not an assumption extrapolated to an unrelated future chart.

The external grid begins at zero, is strictly increasing, and every box's
left endpoint is its node. Each nonfinal right endpoint is exactly the
next literal node. The final interval covers mathematical `2*pi`, and the
last node is strictly below that true endpoint. The true core has period
`2*pi`, as do the state Fourier basis and material chart. The mean term is
independent of angle. Therefore the final interpolation endpoint has
exactly the zero-node value; no rounded `2*np.pi` value is substituted.

The angular gap is the outward maximum of the actual literal box widths.
No symbolic uniform-spacing identity is assumed. Increasing this external
verification grid preserves the original mean1168 rule and the actual
field; it does not constitute a solver refinement or pay a C2 limit.

## 4. Complete radial coverage and the two result scopes

The initial exact grid is the union of all physical field knots, angular
spline knots, profile polynomial branch endpoints, lift cutoff endpoints,
zero, and the exact prefix endpoint. Each generic piece evaluator rejects
a cell crossing one of its defining knots. Every later split is an exact
rational midpoint split.

Each accepted closed radial cell receives the original R62 bound

\[
 \max_j\left(\|E(c,\psi_j)\|
       +h_s\|E_s(c,\psi_j)\|
       +\tfrac12h_s^2\sup_I\|E_{ss}(\cdot,\psi_j)\|\right)
       +\tfrac18h_\psi^2\sup_{I\times\text{all angles}}\|E_{\psi\psi}\|.
\]

The common C2 map may have one-sided third radial derivatives at a knot.
The cells already split at that knot, so the original piecewise Taylor
argument applies without asserting global C3 regularity. Background Gram,
complete lift and convection are all retained by the unchanged algorithm.

The default target remains `9.7e-7` and any requested target must be positive
and at most `1e-6`. A domain interval failure or an excessive metric bound
requires subdivision; no clipping, discarded angle, or weakened metric
criterion is used. Success additionally requires that the exact total
accepted radial length is the full prefix endpoint and no unresolved cell
remains.

Curvature is evaluated on the same metric-accepted cells with the original
second fundamental form formula. Its scope is reported separately. If even
one curvature cell is unresolved, the whole-prefix curvature flag is false
and the final global curvature field is null. A metric-success status does
not become a reach or embeddedness certificate.

The exact endpoint report is computed before releasing the large temporary
Fraction dictionaries. The interval polynomial coefficients, target data,
and exact partitions remain. This changes temporary object lifetime only.

## 5. Reproduction and recorded limits

After a real versioned field and its fresh true-core arrays are available:

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261126/warm_certify_prefix_metric.py \
  --repo "$HELD10_REPO" \
  --source-run "$HELD10_FIELD/run.json" \
  --physical "$HELD10_FIELD/physical.npz" \
  --core-mean-certificate "$HELD10_CORE/mean1168-core.json" \
  --core-mean-intervals "$HELD10_CORE/mean1168-core-intervals.npz" \
  --core-angle-certificate "$HELD10_CORE/external-core.json" \
  --core-angle-intervals "$HELD10_CORE/external-core-intervals.npz" \
  --target 9.7e-7 \
  --outdir "$HELD10_WORK/warm-continuous-prefix"
```

The summary binds the source gate, actual field and core inputs, all helper
sources, exact endpoint algebra, actual mean nodes and state frequencies,
complete radial grid and compressed accepted leaves. Its `complete=true`
can only mean the explicitly named continuous prefix metric component.

The new file's syntax and CLI help were actually checked after executor
recovery. It has not been run on an accepted field. The frozen original
R61 inlet correction, its bounds, the R60 bridge/tail reference correction,
all-time seams, closed-surface geometry, reach, and fixed-problem
convergence are not transferred by this entry. They need the final actual
candidate and their own compatible new certificates.
