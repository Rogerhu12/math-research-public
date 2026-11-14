# Actual binary q106/q122 backgrounds: an explicit continuous C2 comparison

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Result and object being bounded

For each of the two actually accepted q106 and q122 primary files, the frozen
provider reconstructs the original 12 binary physical segments. Its total
physical length agrees exactly with the accepted primary. The original
64 Gauss nodes and weights agree in all bits with the certified table
`4d99ffcc5f29791b15564c7bcef62c5d83cfffaedf16ebc6b0f01561de9e7af1`.
No BVP, Flow object, RHS, ODE or Node worker is invoked.

The binary segment constants define an exact-real piecewise radius, using
the original split Gauss64 partial primitives and the Hermite radius
polynomial. A specified local quintic correction produces a new C2
comparison radius on the entire accepted physical interval. This comparison
is not a modification of either saved candidate or its target metric.

The actual producer exited 0 in 15.473607618 s with peak RSS 79,044 KiB;
all 1,589 gates passed. The primary SHA is
`a3f57c4efdbd5170183cd97ffe4d2828c57c6a2c13c5f603fd1ed144f99db60f`.
An independent exact-Fraction saved-data consumer passed all 236 gates in
0.700707344 s, peak RSS 11,768 KiB, without rerunning a provider or quadrature.

| Actual primary | Uniform repair C0 | Uniform repair C1 | Uniform repair C2 |
|---|---:|---:|---:|
| q106, SHA 83c4c9fdb2b493a42ed4328c507b977c4d12fa5d5839a901bfa20f488621a293 | <4.142e-15 | <1.268e-13 | <4.743e-10 |
| q122, SHA 006eaa15e9b1416aa72140e616e1ecf75461033df8448ade0bbd812826d210a8 | <4.151e-15 | <1.268e-13 | <4.743e-10 |

For each complete comparison radius, the stored outward bounds imply

\[
 a(s)>0.2178357,\qquad |a'(s)|<0.997420117,\qquad
 |a''(s)|<7.500000001.
\]

The complete stored dyadics, not the displayed decimals, are authoritative.
These are continuous interval bounds for the explicitly defined comparison
radius. They are not curvature, metric-error or reach bounds for the full
surface.

## Exact definition from actual binary segments

All recorded binary scalars are interpreted as exact rationals. For a
segment with stored constructor length L and binary global endpoints
s0,s1, put h=s1-s0 and u=(s-s0)/h. The exact rational discrepancy h-L is
recorded; it is not silently declared zero. Binary global endpoints are
contiguous and cover precisely the accepted physical interval.

For an initial Hermite segment, set b=k0 L, c=3V-2b, d=b-2V and use

\[
 a_0+L\left(\frac b2u^2+\frac c3u^3+\frac d4u^4\right).
\]

For every phase segment, retain the original exact-real phase formulas
with the actual binary phase endpoints and ramp parameter. On a smooth
subpiece [l,r], write

\[
 Q(w)=w\sum_{i=1}^{64}\omega_i
          \sin\phi(l+w g_i),\qquad 0\leq w\leq r-l,
\]

where g_i and omega_i are the exact binary normalized nodes and weights.
The radius equals a0 plus L times the sum of all preceding complete
subpiece primitives and the current partial primitive. Every full-prefix
contribution uses this same segment anchor. Original segment anchors are
retained. The flat turns use the original three pieces, including both
ramp joins. Coast and brake formulas are retained. There are 24 complete
smooth pieces per accepted profile.

This definition makes all arithmetic and trigonometric functions exact
real operations. It is a mathematical comparison with the frozen binary
realization, not a claim that a machine's floating function is itself C2.

## Exact-real one-sided jets

Let f=sin(phi), f1=cos(phi) phi',
f2=cos(phi) phi''-sin(phi)(phi')^2, with derivatives in the original u
coordinate. Exact differentiation of the partial rule gives

\[
 Q'(w)=\sum_i\omega_i[f(l+w g_i)+w g_i f_1(l+w g_i)],
\]

\[
 Q''(w)=\sum_i\omega_i[2g_i f_1(l+w g_i)+w g_i^2f_2(l+w g_i)].
\]

The physical derivatives are L Q'/h and L Q''/h^2. Each left and right
one-sided jet is enclosed directly using 256-bit outward Arb arithmetic.
The report includes every actual join gap. In particular, finite binary
Gauss derivative jumps and constructor anchor discrepancies are measured,
not assumed to vanish. The stored K versus the exact binary phase-rate
discrepancy is also recorded separately.

## Whole-piece derivative and radius bounds

Each actual phase polynomial is first expressed on a fixed normalized
subpiece t in [0,1]. It is then shifted to t=1/2+z. The exact rational
coefficient bound on |z|<=2 is checked, with Arb outward exponentiation,
to give |sin(phi)|,|cos(phi)|<2^20 throughout that complex disk.
The Cauchy coefficient tail beyond degree 127 supplies complete remainder
bounds R0,R1,R2 on [0,1]. The polynomial is fixed for the whole subpiece;
it is not reselected as the partial endpoint varies.

Let E_w be the certified L1 error in the actual normalized weights and
E_g the maximum certified node error. For actual real derivative bounds
M0,M1,M2,M3 of f, the table perturbation through order two is bounded by

\[
 T_0=E_wM_0+E_gM_1,
\]

\[
 T_1=E_w(M_0+M_1)+E_g(2M_1+M_2),
\]

\[
 T_2=E_w(2M_1+M_2)+E_g(2M_1+4M_2+M_3).
\]

Exact Gauss64 integration of the fixed degree-127 polynomial leaves the
additional partial-primitive errors 2R0, 2R0+R1, and 3R1+R2. All M_j are
obtained from the actual rational polynomial coefficients on the full
normalized subpiece. The physical scales L/h and L/(h^2(r-l)) are retained.
These bounds pay the derivative differences between the finite quadrature
primitive and its exact integral. For Hermite segments, the actual
polynomial and its Bernstein acceleration bounds are used directly.

Radius bounds use 32 complete interval subpieces on every smooth phase
piece. The entire finite Gauss expression is evaluated on each interval,
with all 64 terms and all preceding complete integrals. Interval enclosure,
not a sampled extremum or a center-value interpolation, supplies each
radius lower and upper bound. The exact parameter intervals cover the
complete segment without gaps.

## Explicit repair and its uniform cost

On a smooth piece of physical length h, let the next piece's left jet
minus this piece's right jet be (e0,e1,e2). Put u0=e0, v0=h e1,
w0=h^2 e2/2, and t=(s-s_left)/h. Add

\[
 R(t)=u_0(10t^3-15t^4+6t^5)
     +v_0(-4t^3+7t^4-3t^5)
     +w_0(t^3-2t^4+t^5).
\]

Its first three left jets are zero. Its right value, first physical
derivative and second physical derivative are exactly e0,e1,e2. The last
piece receives zero correction. Therefore every original left jet is
retained, consecutive repaired jets match exactly, and the original first
left and last right jets are preserved. This proves the C2 property of
the explicitly defined new comparison radius at all internal joins.

The exact Bernstein bounds of the three basis functions are respectively
(1,2/5,1/10) in order zero, (5,2,1/2) in order one and (20,12,4) in order
two. If E_j bounds |e_j|, the complete piece corrections satisfy

\[
 \|R\|_\infty\leq E_0+\tfrac25hE_1+\tfrac1{20}h^2E_2,
\]

\[
 \|R_s\|_\infty\leq 5E_0/h+2E_1+\tfrac14hE_2,
\qquad
 \|R_{ss}\|_\infty\leq20E_0/h^2+12E_1/h+2E_2.
\]

The independent saved consumer verifies the endpoint identities and all
three sets of Bernstein coefficients exactly, then consumes all saved
gap intervals and compares all piece/global/domain inequalities with
exact Fractions. It also checks the exact piece cover and frozen explicit
definition hashes. The first-derivative bound remains strictly below one
after the repair, and the complete radius lower bound remains positive.

## Costs that this certificate does not pay

The accepted target g and both candidate files remain unchanged. The
original floating asin/atan/sqrt initialization and floating affine-node,
trigonometric, dot-product and accumulation evaluations are not covered
by interpreting their resulting binary constants exactly. The comparison
uses exact binary global segment endpoints; the cost of this physical
endpoint alignment relative to the original provider remains separate.

The final radius/first/second jet discrepancy from the original tail-port
target is explicitly saved and is not asserted to vanish. A comparison
radius does not by itself repair the complete surface's PDE, metric,
Cartesian jets, height mean, tail/cap seams or same-g refinement. The
surface mean and its angular/radial quadratures, the state-quintic repair,
the complete Cartesian transfer, and full-family reach/amplitude remain
distinct subsequent obligations. No old-g certificate is transferred to
q106 or q122, and neither accepted candidate is declared to meet the topic
completion standard here.
