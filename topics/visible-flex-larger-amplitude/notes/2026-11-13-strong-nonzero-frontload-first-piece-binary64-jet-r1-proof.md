# Actual first-piece binary64 evaluation and supplied-jet bridge

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Certified object

The input remains the completed **unsolved** warm with screen SHA
`c782a9bda980b0a31443be14d24444b695b246f58390d8f3bf4932e26807d8fa`.
The exact binary first length is `0.8597600240582437`. All 24 radius,
23 velocity, and 22 acceleration Bernstein controls are the actual stored
controls, checked against both the earlier first-piece certificate and the
complete background comparison. No accepted profile is substituted.

For every binary64 physical argument \(s\in[0,L]\), consider the original
first-piece coordinate computation followed by its `piece_jet` call.
The exact comparison coordinate is \(u=s/L\), and the actual one is the
clipped binary64 result of that normalization. The three entries returned
by `piece_jet` approximate a radius and its first two physical derivatives.
They are treated as **supplied jet values**, not derivatives of a rounded
function.

The exact-rational certificate formally exited zero, with 89 gates, in
1.045 seconds at 12,616 KiB. Its primary SHA is
`d56d778fb7cb627b66b20837463212d60ddb62d3fa3f4c797f9c3e0334e7de55`.
All infinitely many allowed binary64 arguments are covered by the analytic
recurrence below; a sampled maximum is not used.

## Basic-operation contract and complete recurrence

The frozen NumPy expression is

```
values[:count] = (1-u)*values[:count] + u*values[1:count+1]
```

The input and coefficient arrays are binary64. The certificate verifies
the frozen source hashes, the actual binary64 format, and the finite
coefficient hulls. Standard binary64 basic operations obey the conservative
contract

\[
 |\operatorname{fl}(z)-z|\le\epsilon |z|+\eta,
 \qquad \epsilon=2^{-52},\qquad \eta=16\,2^{-1022}.
\]

The relative constant allows any standard rounding direction. The absolute
constant is deliberately much larger than gradual-underflow rounding:
on the bounded operands here it also pays a subnormal input or result
being flushed. All arithmetic operands stay below 4 in absolute value;
the physical normalization denominator exceeds \(1/2\). Consequently
two possible subnormal input losses and the output loss fit inside the
displayed absolute fee. No overflow is possible. This contract concerns
basic arithmetic only: it imports no accuracy claim for sine, cosine,
square root, or any other libm routine.

Let \(A\) be the largest absolute Bernstein control, and let \(E\) bound
the discrepancy of the current computed row from the exact de Casteljau
row. The exact row stays inside \([-A,A]\). Writing
\(r=\operatorname{fl}(1-u)\), one has
\(|r-(1-u)|\le\epsilon+\eta\) and
\(|r|+u\le1+\epsilon+\eta\). Applying the basic-operation bound to the
two products and final sum gives the safe recurrence

\[
 E_{j+1}\le(1+\epsilon)^3E_j+
 \bigl((1+\epsilon)^3-1\bigr)A+
 16\eta(A+E_j+1),\qquad E_0=0.
\]

The factor three pays the complement's error together with the product
and addition errors. The last term retains the absolute-error cross terms.
Each step is computed in exact `Fraction` arithmetic and rounded **up** to
an absolute 160-bit dyadic. Every level verifies \(A+E_j<2\), which also
closes the bounded-operand premise of the arithmetic model. Degrees 23,
22, and 21 are handled separately.

## Physical-coordinate displacement and coherent derivatives

The first stored origin is exactly zero. For the exact \(u=s/L\in[0,1]\),
the original clipped division satisfies

\[
 |\widehat u-u|\le\epsilon+4\eta.
\]

Clipping is nonexpansive. The complete Bernstein hull of each polynomial's
normalized derivative therefore pays the argument displacement. These are
exact polynomial hulls on the entire interval.

Let \(R,V,A_2\) be the actual stored radius, velocity, and acceleration
polynomials. They need not satisfy \(R_s=V\) and \(R_{ss}=A_2\) exactly
after coefficient construction. The consumer differentiates the **stored
radius controls** in exact rational arithmetic, dividing by the actual
binary length at each physical derivative. It degree-elevates the two
polynomials to a common degree before bounding their difference by the
largest absolute difference control. Thus the independent supplied-jet
construction mismatch is paid explicitly.

The resulting uniform supplied-jet differences from the exact stored
radius's coherent jet are

| Entry | Certified upper bound, approximately |
| --- | ---: |
| Radius value | \(1.81443760574\times10^{-14}\) |
| Physical first derivative | \(9.48947091896\times10^{-15}\) |
| Physical second derivative | \(2.33608611560\times10^{-13}\) |

The already defined explicit first-piece quintic correction is then added
using its complete C⁰/C¹/C² bounds from background certificate
`01aa989aecc9959f10ce556052b90475d5e60c884b814c10811aef63fbadb5ac`.
The comparison definition SHA remains
`0425ff91db63a9151f6bf2a70b5c4c8af914a2b0b99e440811b6fb01a6c10578`.
This yields the actual supplied tuple versus that explicit C² radius jet:

\[
 (2.44951563149\times10^{-14},\quad
   4.64229179260\times10^{-14},\quad
   5.67354460703\times10^{-13}).
\]

The certificate stores exact rational upper bounds; the decimal values
above are only readable displays.

## Exact scope

This consumer covers the first `piece_jet` evaluation, including its
physical coordinate normalization, throughout the complete first piece.
The provider's global `Pieces.profile` loop permits neighboring masks to
overlap by a small tolerance and later masks overwrite earlier values.
Those branch-overlap bands are not silently identified with the exact
first-piece branch; they remain a separate cost. The material-chart
conversion to physical \(s\) also remains separate.

This does not claim that a floating-point function is C². The comparison
polynomial is explicitly C², and its distance from each supplied jet value
is what has been bounded. Partial-height sqrt/dot evaluation, full angular
mean, Cartesian surface derivatives, PDE residuals, closed diameter and
reach are not supplied by this small certificate. No source, original
candidate, target metric, or current BVP was changed.
