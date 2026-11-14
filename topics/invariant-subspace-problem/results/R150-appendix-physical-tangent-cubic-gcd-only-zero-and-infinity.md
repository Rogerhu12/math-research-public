# R150 appendix — a physical value and its first jet share a cubic factor only at 0 and infinity

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Statement

For the original six-mode matrix K, let

    p_s(z)=v(s)^T K v(z),

and let p'_s be the polar of a genuine first physical jet at s.
All divisibility is for homogeneous binary quintics.

**Theorem.** The common divisor of p_s and p'_s has degree at least
three if and only if s=0 or s=infinity. At both exceptional points
its degree is exactly three. At every other point its degree is
at most two.

Rescaling the genuine first jet or adding a multiple of v(s) does
not change the common divisor. Thus the statement is independent
of the choice of local parameter, including the chart at infinity.

In particular, a three-dimensional physical projection containing
the complete tangent space span(v(s),v'(s)) can have a common
factor of degree three only at these two points. This is a
necessary condition for a birational conic projection, not a
classification of every conic or a claim that these two planes
are original critical supports.

## 2. Two original Bezout minors

For finite s, construct the 5 by 5 coefficient matrix B(s) from

    [p_s(z) p'_s(w)-p_s(w) p'_s(z)]/(z-w)
      = sum B_ij(s) z^i w^j, 0<=i,j<=4.

If the two homogeneous quintics have a common cubic factor,
their remaining homogeneous factors have degree two. The
displayed matrix therefore factors through the two-dimensional
Bezout matrix of those quadratic factors and has rank at most
two. This implication also holds if one of the common factors
is at infinity. Consequently every 3 by 3 minor must vanish.

Direct expansion from the unchanged original K gives

    det B[{2,3,4},{2,3,4}] = s^2 A(s),
    det B[{2,3,4},{1,2,3}] = s^5 C(s),

where coefficient lists below run from constant to leading term:

    A = [394752,-1752544,942832,1279992,-197868,-33712,
         55644,-19962,-1549,3228,575],

    C = [3023808,-2140640,-4659536,-1531992,551256,-266844,
         -91676,109854,14250,-1915,-476].

The two degree-ten factors are relatively prime. An explicit
certificate modulo 103 is

    U = [13,93,91,97,18,31,99,6,26,98],
    V = [75,55,24,47,57,47,54,84,59,79],

    U A + V C = 1 in F_103[s].

The degree-ten leading coefficients reduce to 60 and 39 and
are nonzero. Hence the integer polynomials A,C have no common
nonconstant factor over Q or C. Indeed a primitive common
integer factor would retain positive degree modulo 103, since
both complete degrees are retained, contradicting the displayed
identity.

For s nonzero, the two minors cannot both vanish. Thus every
finite point with a cubic common factor must be s=0.

## 3. Both exceptional points

At s=0, the original affine polars are

    p_0(z)=z^4(5-z),
    p'_0(z)=z^3(-32+5z-z^2).

Their greatest common divisor is exactly z^3: the remaining
factors have no common zero, including the projective point at
infinity.

At infinity use the local curve vector

    (h^5,h^4,h^3,h^2,h,1).

Its value and first-jet polars, in homogeneous target coordinates
(a,b), are

    -a^4(a+b),  5a^3(a^2+ab+b^2).

Their common divisor is exactly a^3. This proves the theorem
in all charts.

## 4. Exact reconstruction record and scope

The accompanying author calculation rebuilds both minors from
the original matrix, checks the full integer coefficient lists,
and multiplies the displayed finite-field Bezout identity:

- notes/2026-11-14-physical-tangent-cubic-gcd-verify.js
- notes/2026-11-14-physical-tangent-cubic-gcd-certificate.json

This is an additional original-kernel obstruction for the
remaining rank-two-mean inside-support problem. It does not
exclude degree-one common factors and double-cover conics,
does not assert criticality of either exceptional plane, and
does not close the full invariant-subspace problem.
