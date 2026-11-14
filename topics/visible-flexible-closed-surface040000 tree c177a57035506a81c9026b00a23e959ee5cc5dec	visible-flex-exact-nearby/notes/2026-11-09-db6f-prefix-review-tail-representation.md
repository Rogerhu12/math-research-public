# Addendum: exact tail representation and background partition

Reviewer `coupled_prefix`, 2026-11-09. This is a read-only component review
of `ExactIntegratedTail.fields/expand`, `value_range`, and `load_packet`
in `db6f-audit-tail-metric-curvature.py`, frozen SHA256
`ed175aacdb2ba3e84d7c397d121e90c2a6a1492d05f5efdb646690481d302670`.
The source was not changed by the reviewer. **PASS for the stated
representation and partition logic, conditional on the supplier's
analytic background enclosures.** This does not certify a physical packet.

## Exact represented map

The class reads the saved derivative coefficients and reconstructs the
same integrated-quartic derivative model. On a span of exact length $L$,
write endpoint derivatives $u_0,u_1$, scaled second derivatives
$v_0=LV_{rr}(0),v_1=LV_{rr}(1)$, and midpoint derivative $m$.
The bubble coefficient is
$$
b=16m-8(u_0+u_1)-2(v_0-v_1).
$$
Adding $bt^2(1-t)^2$ to the cubic Hermite interpolant gives the prescribed
midpoint while keeping its endpoint values and derivatives. Its integral
over the span is exactly
$$
L\left[\frac7{30}(u_0+u_1)+\frac8{15}m+
\frac1{60}(v_0-v_1)\right].
$$
This is the implemented increment, so its accumulated value enclosures
contain the exact polynomial primitive. Differentiating the primitive
recovers the represented first and second jets. The R6 collar's three
quintic coefficients satisfy the prescribed outer two-jet and vanish to
second order at its inner endpoint.

With increment metadata, the radial lengths are exact products of saved
binary lengths and the declared rational scale. The constructor checks
that their exact sum reaches the declared outer anchor and that every
length is positive. Displayed absolute radii are not used to form these
lengths. The collar uses the exact difference between the represented
inner anchor and the declared cuff.

## Restriction and signed complex modes

Each order stored in `fields` is already a derivative with respect to
physical $r$. Restriction to $[a,b]$ therefore substitutes
$t=a+(b-a)u$ in those polynomials without multiplying their values by
$(b-a)$; multiplying would be a derivative-coordinate error. The method
correctly performs only this substitution. `interval_radius` uses the
same exact rational subinterval.

For a signed planar mode $m=1+3k$,
$$
e^{-i\theta}c_m e^{im\theta}=c_m e^{3ik\theta},
$$
so the radial and tangential coefficients are respectively
$c_m\cos(3k\theta)$ and $c_m\sin(3k\theta)$. `expand` handles positive,
negative, and zero $k$ with these signs. Taking the real part of a Laurent
polynomial combines opposite modes by their sum in cosine phase and by
$c_{-k}-c_k$ in the imaginary/sine phase. This is `real_coefficients`.
The apparent imaginary constant in sine phase contributes zero real
part, as implemented.

After exact-coefficient restriction, `value_range` transforms radial
power coefficients to outward Bernstein coefficients and bounds each
radial coefficient on all of $[0,1]$. It then combines those ranges with
the certified trigonometric ranges for each arc. This allows independent
coefficient extremes and is conservative. The trigonometric variable is
$3\theta$; one covered period therefore covers the full threefold map
for the scalar and rotating-frame geometric quantities at issue.

The independent script `db6f-prefix-review-tail-representation.py` compares
these operations with the original complex Cartesian Fourier sum followed
by rotation by $e^{-i\theta}$. It includes modes $-5,-2,1,4,7$, height
modes $0,3,6$, both regular and collar branches, three nested subintervals,
and all three radial jet orders. The 15,552 comparisons have largest
floating discrepancy $8.33\times10^{-17}$ and no sampled interval
violation. These numerical diagnostics support the algebra above; their
explicit floating tolerance is not an analytic background certificate.

## Partition checks and their scope

`load_packet` checks the manifest and data hashes, required coefficient
arrays, finite ordered coefficient endpoints, and nonnegative finite
remainders. It requires the ordered partition to start at span $-1$, local
coordinate zero, finish at the final finite span and local coordinate
one, and move between spans only after finishing the preceding span.
Within each span, the next left endpoint must equal the preceding right
endpoint. Strict interval length rules exclude duplicate zero-length
pieces. These checks reject gaps, overlaps, omitted spans, and out-of-order
rows using the exact binary local coordinates actually used by the audit.

For a row $[u_a,u_b]$ split again at local $[a,b]$, the geometry restriction
uses $u_a+(u_b-u_a)[a,b]$, while the supplier polynomial is restricted at
$[a,b]$ in its own row coordinate. Thus the two functions are evaluated
over the same physical interval.

Hash consistency and partition completeness cannot prove that a supplied
polynomial encloses the intended analytic $w,w_r$. The backend explicitly
leaves this assumption to a separate supplier proof. Nor does a restricted
pilot run establish full coverage: the output flags keep that distinction.

Reproduction:

```bash
python topics/visible-flexible-closed-surface/scripts/db6f-prefix-review-tail-representation.py \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-review-tail-representation.json
```
