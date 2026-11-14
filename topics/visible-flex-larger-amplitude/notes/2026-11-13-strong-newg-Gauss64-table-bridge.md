# Actual Gauss64 table and split angular-profile quadrature

2026-11-13, geometry_audit, GPT-6 Astra Pro, AI-assisted.

## Actual execution and scope

`strong_newg_gauss64_table_bridge.py` completed with formal exit 0 in
9.206173181533813 seconds, peak RSS 75288 KiB. All 399 identity and exact
rational gates passed. It imported the pinned actual provider source to
obtain its current NumPy arrays `gx`, `gw`, and `gu`, then enclosed every
one of the 64 exact Legendre roots and normalized Gaussian weights. It did
not evaluate an ODE, Newton step, Node worker, or surface.

For either of the actual q098 and q106 ideal analytic profiles certified in
the accompanying profile-domain packet, the result is:

- The actual binary table, with exact real function evaluation, differs from
  the exact normalized Gauss64 rule by at most
  \(9.013397364\times10^{-15}\) on each normalized split phase piece.
- The exact Gauss64 integration error for those phase sine/cosine functions
  is less than \(2^{-234}\).
- Summing the physical nonconstant angular-program segments, whose total
  length is less than 4, gives a primitive-value error less than
  \(2^{-44}\) from these two causes together.

Every bound concerns the indicated mathematical rule using the actual
binary nodes and weights. Affine node arithmetic, phase arithmetic,
floating sine/cosine evaluation, dot products, clipping boundaries, segment
length/endpoint assembly, and seam repair are separate. The Hermite inlet's
height integral is also separate. No C1/C2 error bound between the floating
provider and the ideal profile follows merely from this value bound; no
complete surface mean, Cartesian field, curvature, or reach is certified.

## Actual table identity and root completeness

The source pins `alternative-neck-excursion.py`,
`alternative-neck-flatturn.py`, and the actual-profile checker. The first
module's import executes the original

```
gx, gw = np.polynomial.legendre.leggauss(64)
gu = (gx + 1) / 2
```

The certificate retains all 64 binary input triples, their concatenated
little-endian Float64 SHA256, the NumPy version, and every source/input SHA.
In particular it includes the actual rounded `gu`; it does not replace that
array by an exact arithmetic expression in `gx`.

Legendre polynomials are evaluated by the exact recurrence

\[
 P_0=1,\quad P_1=x,\quad
 (n+1)P_{n+1}=(2n+1)xP_n-nP_{n-1}.
\]

For each actual binary node, the checker starts with the rational interval
\([g_x-2^{-48},g_x+2^{-48}]\), verifies opposite strict signs of \(P_{64}\),
and performs 32 exact bisections. The resulting 64 intervals are disjoint,
strictly ordered, and lie inside \((-1,1)\). They therefore contain all
64 distinct roots of this degree-64 polynomial; none is inferred from a
floating root finder or a residual tolerance.

For a root box \([a,b]\), let \(c=(a+b)/2\). The exact value

\[
 D_c=P_{64}'(c)=64\frac{P_{63}(c)-cP_{64}(c)}{1-c^2}
\]

is computed rationally. The derivative identity

\[
 P_n'=\sum_{j=n-1,n-3,\ldots}(2j+1)P_j
\]

and \(|P_j(x)|\le1\) on \([-1,1]\) imply

\[
 \|P_n''\|_\infty
 \le\sum_{j=n-1,n-3,\ldots}(2j+1)\frac{j(j+1)}2
 =\frac{(n-1)n(n+1)(n+2)}8.
\]

The first identity follows by telescoping
\(P_{j+1}'-P_{j-1}'=(2j+1)P_j\). The bound \(|P_j|\le1\) also follows
directly from the Legendre integral representation

\[
 P_j(\cos\theta)=\frac1\pi\int_0^\pi
 (\cos\theta+i\sin\theta\cos\varphi)^j\,d\varphi,
\]

whose integrand has modulus at most 1; the representation satisfies the
same recurrence and initial values. Thus the root derivative is enclosed
by \(D_c\pm C(b-a)/2\), with the displayed exact \(C\). Every such box
excludes zero.

## Positive weights and the actual-table error

For a root \(x_i\), the normalized Gauss weight on \([0,1]\) is

\[
 w_i=\frac1{(1-x_i^2)P_{64}'(x_i)^2}.
\]

This is the usual Legendre weight on \([-1,1]\) divided by two. Exact
positive lower and upper bounds follow from the root and derivative boxes.
The resulting rule is exact on all polynomials of degree at most 127:
divide such a polynomial by \(P_{64}\), use its orthogonality against
degree at most 63, and interpolate the degree-at-most-63 remainder at the
64 roots. Integrating the Lagrange cardinal functions gives the displayed
weights. Positivity is also apparent from the formula, and exactness on
the constant polynomial gives \(\sum_iw_i=1\).

The checker encloses

\[
 E_w=\sum_i|\widehat w_i-w_i|,\qquad
 E_u=\max_i|\widehat u_i-(1+x_i)/2|,
\]

where \(\widehat w_i\) and \(\widehat u_i\) are the actual binary table.
For a real split-phase sine or cosine \(f\), the preceding profile proof
gives \(|f|\le1\) and \(|f'|\le4\) in the normalized integration variable.
Consequently

\[
 \left|\sum_i\widehat w_i f(\widehat u_i)
              -\sum_iw_i f((1+x_i)/2)\right|
 \le E_w+4E_u.
\]

The program evaluates this exact positive sum and proves it is below
\(2^{-40}\); the saved sharper endpoint is approximately
\(9.013397363742184\times10^{-15}\). Intermediate rational endpoints
are serialized outwards. Both actual accepted profiles and every original
provider source are identified by their own SHA256 values.

## Exact quadrature error on the actual split-phase formulas

The pinned `flatturn.integral` splits at \(0,\epsilon,1-\epsilon,1\)
before applying the rule, where \(\epsilon\) is the actual binary .08
constant. Here the endpoints and phase formulas are interpreted in exact
real arithmetic. Therefore a partial ramp is integrated only through its
own degree-four phase polynomial, without analytically continuing across
the piece boundaries.

Let the normalized quadrature variable be \(t\). Consider the complex disk
\(|t-1/2|\le2\). In either ramp, the polynomial is an endpoint angle plus
or minus

\[
 \frac{\Delta\phi\,\epsilon}{1-\epsilon}
 (z^3-z^4/2),
\]

where for a partial piece \(z=at\) or \(z=1-at\), \(0\le a\le1\).
On this disk \(|z|\le5/2\). The actual-profile angle bounds give

\[
 |\phi|\le\frac85+
 \frac{(22/7)\epsilon}{1-\epsilon}
 \left[(5/2)^3+(5/2)^4/2\right]<12.
\]

On a plateau the phase is linear; its real center value is below \(8/5\)
and its complex displacement is at most 8, again below 12. On the brake,
the quadratic phase increment is \(f\arctan w<81/1000\), giving the bound
\(8/5+(81/1000)(5/2)^2<12\). The certificate checks all three inequalities
rationally.

Hence throughout that disk both sine and cosine have modulus less than
\(e^{12}<3^{12}<2^{20}\). The elementary \(e<3\) follows from the
factorial series. Cauchy's coefficient bounds about \(t=1/2\) give a
degree-127 Taylor remainder on \([0,1]\) at most

\[
 E_P=2^{20}\sum_{j=128}^\infty4^{-j}
     =\frac43\,2^{-236}.
\]

Both the integral and the positive Gaussian rule have norm one. Since the
rule integrates that Taylor polynomial exactly, the normalized Gaussian
error is at most

\[
 2E_P=\frac83\,2^{-236}<2^{-234}.
\]

Each split-piece contribution carries its actual exact normalized width.
The widths for a segment sum to at most one, and the total physical length
of the nonconstant angular-program segments is below four. Thus the sum of
table and quadrature errors is at most
\(4(E_w+4E_u+2E_P)<2^{-44}\), as checked in the saved certificate.

Constant phases retain the actual normalized weight sum in a separate field.
Neither its small defect nor any floating rounding operation is silently
identified with zero. The next realization bridge must account for those
operations and the Hermite inlet before a complete background/Cartesian
claim is made.
