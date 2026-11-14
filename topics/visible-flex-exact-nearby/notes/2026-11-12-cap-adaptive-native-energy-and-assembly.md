# Adaptive native inner-cap energy and exact finite assembly

This note continues R88 for the **same exact symmetrized affine point**
\(\delta_5=-7789843107295549/4611686018427387904\).
The finite boundary inputs are the physical modes \(k=-4,\ldots,4\),
together with the regular mean value \(\xi\). The chosen interior trial has
physical modes \(k=-16,\ldots,16\) and radial degree two. These physical
indices are not the canonical shear indices in R83/R92.

The actual finite functions are the binary coefficients in
2026-11-12-cap-space-boundary4-interior16-P2.npz, bound to its JSON
description. Neither a floating solve nor the apparent small size of the
saved floating energy gap certifies their energy. The sources in this note
integrate those exact finite functions against the true infinite angular
geometry. A complete cap claim requires all body elements, the natural
graft, and the true infinite-tail form.

## 1. A paid native radial interval

fourfold_phase_cap_native_cover_v2.py uses the frozen
fourfold_phase_cap_energy_interval.py formulas with the exact scaled
body geometry and vectorized directed polynomial evaluation. Every accepted
interval \([c-h,c+h]\) belongs to one exact scalar common span and one finite
trial element. Close but unequal binary knots remain distinct.

For either the primal or complementary dual energy, let \(M\) bound the
operator norm of the finite angular-trapezoid matrix on a true complex
radial disk of radius \(R>h\). This is an analytic extension of the energy:
the conjugated trial polynomial has conjugated coefficients, while its
radial argument remains the same complex argument. It is not the
pointwise conjugate of an evaluation at complex radius.

An \(n\)-point Gauss rule integrates the radial Taylor polynomial through
degree \(2n-1\). The two full remainder bounds, for the integral and its
positive-weight Gauss rule, give

\[
 \varepsilon_{\rm radial}
 \le 4hM\,\frac{(h/R)^{2n}}{1-h/R}.
\]

The Gauss nodes and weights themselves have directed enclosures from the
exact Legendre polynomial. Their uncertainty, the true primitive error,
all finite arithmetic, and the selection of the saved Hermitian dyadic
matrix are included in the reported node-and-weight operator error.

The full angular alias fee is independent of this radial remainder. In
the normalized angular coordinate \(x=4\theta\), with \(N\) angular samples
and trial bandwidth \(M_{\rm tr}=16\), all matrix lags satisfy
\(|\ell|\le2M_{\rm tr}\). A true coefficient-strip modulus therefore uses

\[
 \frac{e^{-(N-2M_{\rm tr})s}+e^{-(N+2M_{\rm tr})s}}
      {1-e^{-Ns}}.
\]

The complete finite-column \(\ell^1\) norms convert this coefficient fee
to an operator error, and integration multiplies it by \(2h\). The
infinite tangent and primitive tails are already present in the strip
modulus and at the directed Gauss nodes. A small fitted Fourier tail is
never substituted for this infinite error.

The actual interval record contains the sum

\[
 \varepsilon_I=
 \varepsilon_{\rm nodes}+
 \varepsilon_{\rm radial}+
 \varepsilon_{\rm angular}.
\]

It is accepted only if both primal and dual errors are at most its length
times the requested error density. A failed domain or fee causes genuine
dyadic radial subdivision; it does not discard the failing term.

## 2. Adaptive order and the narrow-strip continuation

For each interval the source first tries a radial disk of radius
\(\max(4h,2^{-12})\), then \(\max(2h,2^{-12})\). It chooses the smallest
Gauss order from 2 through 32 that pays the entire radial remainder.
The fixed minimum radius lets a very short common span use its own
polynomial germ on a useful larger analytic disk. The disk is an
extension of that chosen germ; only the original real integration
interval is asserted to equal the actual piecewise geometry.

The current inner-body run uses primitive size 256, angular size 1024,
160-bit native ball arithmetic, and normalized angular strip \(1/32\).
The earlier 512-angle, \(1/16\)-strip run paid valid intervals, but its
whole-strip denominator boxes forced extra radial subdivisions. The
saved narrower-strip probe pays an entire actual common span with
angular-alias error densities below \(1.237\cdot10^{-9}\) for the primal
energy and \(1.758\cdot10^{-8}\) for the dual energy. This is a genuine
domain and alias comparison, not an extrapolation from point samples.

The separate correlated-curvature probe preserves the exact identity

\[
 C^2(L^2-L')+LCC'
 =Z'(a'Z''-a''Z')/a^5.
\]

At the tested cell its larger disk still failed, and the smaller-disk
modulus improved by only about two percent at extra cost. That source
and report are retained as a diagnosis and are **not** used by the
native cover producer.

## 3. Saved prefix and observed interruptions

The old native producer supplied 28 consecutive paid subintervals from
\(1/4\) through
\(9322451228656927/36028797018963968\). They are frozen in

data/cap_physical4_energy/native_prefix_before_narrow_strip.json.gz

with SHA256
e2e1ff8f440c744047e2b6b8dd8fea61e822869c2b1a1eaee8b73b7bd0a9c8c9.
The file is a partial finite-element report and does not claim completion
of that whole element.

The v2 producer checks the old source, dependency, object, exact-trial,
and seed identities. It reuses only the consecutive already paid rows
and resumes exactly at their right endpoint. Their original matrix
errors remain unchanged. Different valid sampling layouts can be
combined because each row encloses the same exact energy integral on
its own stated interval.

One earlier process exited with an observed ENOSPC while creating an
output directory; that attempted new interval was not saved. A subsequent
small create/write probe succeeded. No diagnosis beyond the observed
filesystem error is inferred. A later wide-strip process was stopped
voluntarily with exit 130 to switch to the separately tested narrower
strip; all its already paid rows above were preserved. These events are
not recorded as successful numerical intervals.

Run from the topic directory:

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cap_native_cover_v2.py \
  --start-element 0 --stop-element 20 \
  --reuse-partial data/cap_physical4_energy/native_prefix_before_narrow_strip.json.gz \
  --out-dir data/cap_physical4_energy/body_native_0250_0800_narrow \
  --stop-file /workspace/scratch/f6a2c7886477/cap_native_stop
~~~

Completed element reports are reusable after identity and hash checks.
An interrupted incomplete new element is recomputed by this entry; its
old partial file remains evidence, not a silently completed element.
Each accepted interval is saved immediately, and the live manifest is
updated at finite-element boundaries. Only one element's matrices are
kept in memory.

## 4. Whole-cap assembly and its precise scope

fourfold_phase_cap_energy_collect.py reads the exact saved matrices
and all their operator fees. It checks exact consecutive intervals,
complete element identities, dependency hashes, the full body cover,
the complete natural graft, and the actual infinite tail. If a required
element is absent, it emits only a missing-piece report.

For complete data, let \(\widehat E,\widehat D\) be the selected exact
Hermitian dyadic primal and dual matrices, with true errors
\(\epsilon_E,\epsilon_D\). Let \(T\) be the exact boundary pairing of
the divergence-free saved flux. The variational/complementary identity
in R88 gives, for the retained input vector including \(\xi\),

\[
 T+T^*-D_{\rm true}\ \le S_{\rm true}\ \le E_{\rm true}.
\]

Define

\[
 G=\widehat E-T-T^*+\widehat D,\qquad
 C=\tfrac12(\widehat E+T+T^*-\widehat D).
\]

Then

\[
 \|S_{\rm true}-C\|_2
 \le\tfrac12\|G\|_2+\max(\epsilon_E,\epsilon_D).
\]

The saved centers and the complete accumulated fees are summed in
directed arithmetic. The bound on \(\|G\|_2\) uses the exact Hermitian
matrix \(G\) and directed products \(G,G^2,G^4,G^8,G^{16}\):
the maximum absolute row sum of \(G^m\), to the power \(1/m\), bounds
the norm of \(G\). Taking the minimum of these independently valid
bounds is allowed. Floating eigenvalues are not used as proof.

## 5. Exact constant kernel in the final center

The true augmented cap form annihilates
\(v=e_{\rm left\,mean}+e_\xi\), because the admissible function
\(U\equiv1\) has zero gradient and zero nonmean Robin trace. Hence
\(S_{\rm true}=P S_{\rm true}P\), where
\(P=I-vv^*/2\) is an orthogonal projection. Consequently

\[
 \|S_{\rm true}-PCP\|_2
 \le \|S_{\rm true}-C\|_2.
\]

The collector selects its final Hermitian dyadic center from \(PCP\),
explicitly gives it opposite mean and \(\xi\) columns, and pays the
full Frobenius selection error. Thus the saved center has the exact
constant kernel. This uses the true variational kernel; it does not
assert that all rounded interior coefficients of the original two
saved trial columns sum exactly to one. That earlier distinction
remains as recorded in the native-energy note.

Even after complete assembly, the result encloses only the stated
physical finite input/output compression of the full cap, with its
regular mean port. It does not supply omitted boundary outputs,
canonical/physical basis conversion, the full core/cap Schur inverse,
or a nonlinear existence theorem.
