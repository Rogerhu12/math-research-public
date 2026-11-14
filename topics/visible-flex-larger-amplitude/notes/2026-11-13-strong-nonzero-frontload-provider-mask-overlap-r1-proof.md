# Complete internal provider mask-overlap bands

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Same actual warm and same comparison field

This certificate continues the completed unsolved release warm
`c782a9bda980b0a31443be14d24444b695b246f58390d8f3bf4932e26807d8fa`.
The original provider, angle hook, pulse hook, and corrected frontload hook
are loaded in their original order. Reconstructed prefix and bridge records
are checked exactly against all twelve stored segment records in background
certificate `01aa989aecc9959f10ce556052b90475d5e60c884b814c10811aef63fbadb5ac`.
The actual small-cut port and all source hashes are preserved.

The exact C² radius is the previously defined piecewise split-Gauss radius
with the explicit quintic endpoint corrections, definition SHA
`0425ff91db63a9151f6bf2a70b5c4c8af914a2b0b99e440811b6fb01a6c10578`.
It is a comparison field; neither the floating provider nor the target
metric is modified.

Owned execution formally exited zero in 4.027 seconds, at 73,788 KiB,
with 116 gates. The primary SHA is
`ea0922ae5acb791598b5348d379618c1de2fa8312670d179b2a4bc9f334ebba1`.
Only ten actual provider endpoint tuples were evaluated. The resulting
bounds cover complete intervals by the argument below; they are not maxima
of endpoint or interior samples.

## What the original selector actually does

For a segment with stored local start \(s_0\), the unmodified loop accepts
the condition

```
ss >= seg['s0'] - 1e-13
```

and later loop iterations overwrite earlier output values. Put
\(a=\operatorname{fl}(s_0-10^{-13})\), using the actual binary literal
and actual binary subtraction. Throughout the complete binary64-input band
\([a,s_0]\), the later segment is selected and no still later segment is
active. Positivity and separation of all actual segment lengths verify the
last assertion for each band.

For every argument in that band, \(s-s_0\le0\). Division by the positive
segment length preserves its sign, and clipping to \([0,1]\) therefore
produces **exactly zero**. The returned tuple is the same actual
`piece_jet(segment, 0)` tuple throughout the band. An actual endpoint call
records that constant tuple. There is no appeal to an unproved uniform
trigonometric error: each constant output is an observed binary number,
compared exactly with the certified endpoint enclosure.

There are eight such bands inside the prefix and two inside the bridge.
The provider's component boundary is not an internal segment mask and is
not counted as an eleventh band here.

## Physical alignment and propagation over the whole band

The reference uses the original stored **global** binary segment endpoints.
For a component shift \(s_*\), a local argument is compared at the exact
real coordinate \(s_*+s\). The difference between that sum and a rounded
stored global seam is not discarded. Each record stores the complete
translated band and

\[
 d=\max\{\lvert s_*+a-b\rvert,\lvert s_*+s_0-b\rvert\},
\]

where \(b\) is the exact comparison seam. Every translated band is checked
to lie in the union of the two adjacent smooth comparison pieces. At the
seam, the comparison radius and its first two derivatives agree with the
right piece's original left jet, because the right piece's quintic
correction has zero left jet. The previous piece's correction makes its
right jet equal to that same jet.

Let \(E_k\) be the rigorous difference between the actual constant
endpoint entry and this common comparison jet, for \(k=0,1,2\). Let
\(M_{k+1}\) bound the corresponding next derivative on both adjacent
pieces. The complete overlap-band error is

\[
 E_k+dM_{k+1}.
\]

For the third derivative, the comparison is piecewise smooth and globally
C². Integrating its bounded piecewise third derivative proves the same
Lipschitz estimate across the seam; a third-derivative match is unnecessary.

## Complete third-derivative bounds

The first stored Bernstein radius is differentiated three times in exact
rational arithmetic and its complete derivative-control hull is used.
For a later smooth phase piece with normalized phase polynomial \(p\),
the exact split-Gauss primitive is a positive sum of terms
\(t\sin p(g_jt)\). Hence

\[
 \left|\frac{d^3}{dt^3}\left(t\sum_jw_j\sin p(g_jt)\right)\right|
 \le \Bigl(\sum_jw_j\Bigr)(3F_2+F_3),
\]

where the exact polynomial derivative hulls \(d_1,d_2,d_3\) give
\(F_2=d_1^2+d_2\) and
\(F_3=d_1^3+3d_1d_2+d_3\). The original constructor length and actual
physical subpiece length are retained in the derivative scaling. No
constructor-length/global-length equality is assumed for later pieces.

For the explicit quintic endpoint repair, degree-two Bernstein hulls of
the third derivatives of the three Hermite bases are bounded by
\(120,60,18\). Thus the additional physical third-derivative cost is

\[
 120|g_0|/h^3+60|g_1|/h^2+9|g_2|/h.
\]

All ten bands keep their own positive costs. The maxima are

| Supplied entry versus explicit C² comparison | Uniform upper bound, approximately |
| --- | ---: |
| Radius | \(9.99460507292\times10^{-14}\) |
| First physical derivative | \(7.59470106220\times10^{-13}\) |
| Second physical derivative | \(3.61975503349\times10^{-8}\) |

The second-derivative maximum occurs in the bridge turn-to-coast band. It
uses a conservative complete third-derivative hull, not a sampled local
slope. Exact rational upper bounds for each band, its endpoint discrepancy,
its coordinate displacement, and its two adjacent derivative hulls are
retained in the certificate.

## Remaining boundaries

This pays all internal segment-mask overlap bands within the two provider
components. The prefix-to-bridge dispatcher, its argument subtraction, the
material-to-physical chart, and arbitrary interior libm evaluation remain
separate. It does not certify the complete angular mean, a Cartesian
surface, the PDE, closed diameter, reach, or a new accepted solution. It
also does not identify the discontinuous rounded implementation with a C²
function; it bounds its supplied jet values against an explicit C² field.
