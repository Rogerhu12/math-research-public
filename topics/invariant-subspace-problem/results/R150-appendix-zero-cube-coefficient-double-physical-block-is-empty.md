# R150 appendix — the zero-cube coefficient cannot accompany a physical double block

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Statement

Let X=v(s), let Z be a genuine first physical jet at s, and let
Y,X,Z be independent directions. Consider the original ordinary
third tensor

    T3=-6Y(h0 X^2+2h1 XZ)+4(v0 X^3+3v1 X^2Z).      (1.1)

There is no tensor of this form having essential dimension three
and satisfying the original highest identity

    T3(Kv(z)) identically zero.                     (1.2)

This assertion does not require a catalecticant-rank restriction
on Y, a nonzero v1, or either low-gradient equation. It treats
precisely the zero effective mean-cube coefficient; the nonzero
coefficient is addressed separately.

## 2. The conic forced by the factorization

If h1=0, then (1.1) is X^2 times a single linear direction, so
its essential dimension is at most two. Hence h1 is nonzero.

The tensor is X Q, where

    Q=-6h0 YX-12h1 YZ+4v0 X^2+12v1 XZ.              (2.1)

The original physical polar of X is a nonzero polynomial, so
(1.2) forces Q to vanish on the physical projection of W=span(Y,X,Z).
The three physical polars are independent because K is invertible.
Their irreducible plane image is nondegenerate.

If Q were reducible, that irreducible image would lie in one of
its line factors, contradicting nondegeneracy. Therefore Q is a
nondegenerate conic. It contains

    P=[1:0:0] in coordinates [Y:X:Z].                (2.2)

Let d be the common divisor of the three original physical
quintics, delta its degree, and e the degree of their map to Q.
As usual,

    delta+2e=5,

so (delta,e) is either (3,1) or (1,2).

On the smooth conic, the two independent linear coordinates
X and Z have exactly one common zero, namely P, with common
multiplicity one. Pulling back along the degree-e map and then
restoring d gives the exact equality

    deg gcd(p_X,p_Z)=delta+e.                       (2.3)

## 3. Both degrees are impossible

For (delta,e)=(3,1), equality (2.3) gives a fourth-degree
common factor of a physical value polar and its genuine
first-jet polar. This contradicts the original length-four
projection theorem.

For (delta,e)=(1,2), equality (2.3) gives degree three.
The exact physical tangent gcd classification

R150-appendix-physical-tangent-cubic-gcd-only-zero-and-infinity.md

then forces s=0 or s=infinity. In both cases the common divisor
of p_X,p_Z is exactly the cube of the linear factor at s.
Their exact local orders there are

    ord_s p_X=4,   ord_s p_Z=3.                     (3.1)

Since d has degree one and divides their common divisor, it is
exactly the linear factor at s. After removing d the X and Z
coordinates both vanish at s. The three residual coordinates
have no common zero, by definition of d. Consequently

    ord_s p_Y=1.                                   (3.2)

But in the original identity (2.1), the term -12h1 p_Y p_Z
then has exact local order four. The other three terms have
orders at least five, eight, and seven, respectively. Its
nonzero leading coefficient cannot cancel. This is a contradiction.

The local order argument is unchanged by rescaling a genuine
first jet, adding its physical value, or using the infinity
chart. Thus every possibility is covered, proving the theorem.

## 4. Use in the current rank-two-mean section

For an inside rank-two mean with full four-dimensional third
moment, the remaining support has the exact disjoint form

    g=D+R, deg D=deg R=2, W=Cy+E_R.

When the mean divisor D is reduced, its exact tensors on D
give effective coefficient kappa=1-2rho. The present theorem
excludes the entire kappa=0 branch whenever R is a double point.
For a double mean the effective coefficient is one, so it is
handled by the nonzero-coefficient results instead.

The theorem uses the already published original K and its exact
physical-polar gcd certificates. No approximation, replacement
of the original matrix, independent audit gate, or low-gradient
omission is being used: the highest identity alone is already
impossible here.

Reduced complementary supports and other critical sections
remain separate tasks.
