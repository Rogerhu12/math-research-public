# DQ window matrices: source units and a common material majorant

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

This is a clarification of the already frozen five-file package
`2026-11-13-inner-CsLambda-DQ-two-material-windows-r1-manifest.json`,
SHA `bc1b0c75b2aa57aa1a397387b8bbce4b434b9d73c05555a690a9fe1962b9c6cc`.
Its primary remains SHA
`bb4c7036f45d23a33cfe7f8dbeb4ccb142ffab22c91b62b0162de9c628dc9772`.
No source, numerical entry, input, or previous file is changed.

## 1. Relative and physical source units

In R106 (A4)–(A5), the variables are the relative physical variables
`P=p/w` and `Kbar=kappa_perp/w`, and the source is `mathcal N` in the
relative second equation. For the normalized strong field
`(B p,kappa_perp)/Vprime`, the two corresponding relative materials are

\[
s(V'/w)^2,\qquad |\ell|(V'/w)^2.
\]

These are the two expressions displayed in section 1 of the frozen
DQ proof. The word “physical” there identifies the equation underlying
the coefficients; it must not be read as an instruction to inject those
expressions directly into the equation for `kappa_perp`.

The physical second-equation source is `w mathcal N`. Its materials in
the original `x` coordinate are therefore

\[
sV'^2/w,\qquad |\ell|V'^2/w.
\tag{1}
\]

Equivalently, in the original outward radius coordinate they are

\[
d_1(r)\,dr=\frac{V'^2}{w}\,d\log r,
\qquad
d_\lambda(r)\,dr=\frac{V'^2}{w}\,|d\log w|.
\tag{2}
\]

Thus `d1=Vprime**2/(r*w)` and
`d_lambda=abs(w_r/w)*Vprime**2/w`. These are exactly the physical
materials used by `tail_high_two_material_kernel.py` and the subsequent
true endpoint recurrence. In particular the saved panel injections are
`V * (V/w) * radial_log_increment` and
`V * (V/w) * log_w_variation`, followed by the explicitly paid change
from the original envelope to `Vprime`. They contain one division by
`w`, not two. The DQ matrices contain only dimensionless coefficients
and are unchanged by this clarification.

## 2. One coefficientwise majorant for both materials

For all the certified cells, the saved floor satisfies `B0>=120`.
For every center frequency `k>=2` and perturbation frequency `n>=2`,
the frozen coefficients are

\[
\beta_s(k,n)=\frac{5kn}{4(1+k)(1+n)},
\]

\[
\beta_\ell(k,n)=
\frac{\max\{1,5k/(4B_0),5n/(4B_0),(5kn+1)/(4B_0^2)\}}
{(1+k)(1+n)}.
\]

Every entry of the maximum in the numerator of `beta_ell` is at most
`5kn/4`. For the first three entries this follows respectively from
`kn>=4`, `B0*n>=1`, and `B0*k>=1`. For the fourth it is equivalent to

\[
1\le 5kn(B_0^2-1),
\]

which is strict on this domain. Consequently

\[
0\le\beta_\ell(k,n)\le\beta_s(k,n)
\tag{3}
\]

holds before summing center frequencies, before taking a radial
supremum, and before collecting an output window. The sum and
difference membership factors and their positive angular weights are
the same for both materials. Hence the entire positive `s`-material
convolution is one coefficientwise majorant for both physical source
components in (1).

This justifies consuming their common-source whole-cell Green bound
with that one majorant, and in particular a consumer may use the
larger of its two valid total DQ bounds when that larger bound is the
bound for this common majorant. The justification is (3); a maximum
of unrelated total material masses would not by itself establish a
common bound in the radial-supremum-first Fourier norm. A numerical
check of all saved `Gamma_s>=Gamma_ell` entries is useful for guarding
the serialization but is not a substitute for the coefficientwise
argument.

The complete unknown quadratic term, full mean and inverse remainder,
far field, infinite band, and true endpoint readout remain separate
parts of the same R100 field consumer. This note neither changes the
parameter domain nor makes a new contraction or cut-closure claim.
