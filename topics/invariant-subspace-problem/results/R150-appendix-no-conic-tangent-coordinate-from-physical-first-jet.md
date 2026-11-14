# R150 appendix — no conic tangent coordinate from a physical value with its first jet

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Original-kernel statement

Let W be any three-dimensional space of directions whose original
physical projection z -> [W^T K v(z)] has a nondegenerate conic as
its image. Suppose W contains the genuine physical tangent block

    span(v(s),v'(s)).

The coordinate on the conic defined by its physical value v(s)
cannot be a tangent line to that conic.

No critical-point assumption or mean-rank assumption is used.
The assertion includes infinity and every local choice of a
genuine first jet.

## 2. Tangency as a square after removing the common divisor

Write d for the maximum common divisor of the three physical
quintics and delta=deg d. If the conic map has degree e, a general
line gives

    5-delta=2e.

Its only possibilities are (delta,e)=(3,1) or (1,2).
If the physical-value coordinate were tangent to the conic,
its pullback divisor on the normalization would be twice a point.
After further pullback along the degree-e map, every root of

    p_s/d

would consequently have even multiplicity. Over C this homogeneous
form must be a nonzero scalar times a square. Also d divides both
p_s and its genuine first-jet polar p'_s.

We exclude this in both possible degrees.

## 3. A birational conic

If delta=3, the original cubic-gcd theorem

R150-appendix-physical-tangent-cubic-gcd-only-zero-and-infinity.md

forces s=0 or s=infinity and determines d exactly.

At s=0, after removing z^3 the physical value polar is z(5-z).
Its two homogeneous roots are distinct. At infinity, after removing
a^3 the polar is -a(a+b), again with two distinct roots. Neither
is a square. Thus a birational conic is impossible under the
proposed tangency.

## 4. A conic covered twice

Now delta=1. A binary quintic becomes a square after division by
one linear factor only if it has exactly one odd-multiplicity root,
and that root must be the removed factor d.

Use the unchanged original kernel

    p_s(z)=-(z-s)^2 q(s,z),

    q(s,z)=(s+1)z^3+(-3s^2-3s-5)z^2
            +(s^3-3s^2+22s)z+s^3-5s^2.

The source contact and discriminant computations already proved
in the original-polar appendices cover every source.

For finite s outside 0,2,-6 and with E8(s) nonzero, q(s,z) has
three distinct projective roots, none equal to s. All three are
odd-multiplicity roots of p_s, so division by one factor cannot
produce a square. This includes s=-1, where the cubic has a
simple root at infinity and two distinct finite roots.

At s=2 or -6, the self root has order three and the other two
roots are distinct and simple. Again three roots have odd
multiplicity.

At s=0, p_s has divisor 4[0]+[5], so the only possible removed
factor would be [5]. But p'_0(5)=-4000 is nonzero. This factor
cannot divide the common divisor d. At infinity the corresponding
divisor is 4[infinity]+[-1], and the first-jet polar at -1 is 5.
That case fails for the same reason.

The only remaining possibility is a finite root of E8(s), where

    E8(s)=5s^8+50s^7+153s^6-936s^5-2888s^4
          +15936s^3-3392s^2-25472s+9600.

The square freeness of E8 and the nonzero special values imply
that q(s,z) has an exact double root u and a distinct simple
root t, both different from s. The divisor of p_s is therefore

    2[s]+2[u]+[t].

The required common linear factor is [t]. Its also dividing
p'_s forces

    q(s,t)=q_s(s,t)=0,  s!=t.                       (4.1)

Section 3 of

R150-appendix-no-physical-shifted-tangent-conic-companion.md

proved exactly that every such ramification pair has E8(s)
nonzero: symmetry makes s the double root of q(t,z); substituting
its rational double-root formula into E8 gives a polynomial
relatively prime to E8(t), with the complete degree-40
substitution and finite-field Bezout certificate recorded there.
This contradicts E8(s)=0.

Thus no conic covered twice can have the proposed tangent
coordinate either. This completes the theorem.

## 5. Application to an exact double complementary block

A direct useful consequence concerns independent directions
Y,X,Z, where X=v(s), Z is a genuine first jet at s, and the
third tensor is

    T3=kappa Y^3-6Y(h0 X^2+2h1 XZ)
          +4(v0 X^3+3v1 X^2Z),                    (5.1)

with kappa and v1 both nonzero. The original physical projection
of their span cannot have a nondegenerate conic as its image
while T3 vanishes on it.

Indeed such a conic Q would divide T3. The nonzero Y^3 term
allows its factorization to be normalized as

    T3=(Y-A)(kappa Y^2+kappa AY+kappa A^2-6H_R),

    4V_R=-kappa A^3+6AH_R.

The absence of a Z^3 coefficient in V_R forces A=aX.
The nonzero X^2Z coefficient then gives v1=a h1, so h1 is
nonzero. The conic factor is

    Q=kappa Y^2+kappa aXY
        +(kappa a^2-6h0)X^2-12h1XZ.

Its restriction to the line X=0 is kappa Y^2. Hence the
physical value coordinate X defines a tangent line to Q,
contrary to the theorem.

In the rank-two-mean inside/full-four-jet section, this excludes
every conic branch with a double complementary block R=2s
and nonzero effective mean-cube coefficient kappa. For a double
mean that coefficient is always one, so its entire conic branch
with a double complementary block is excluded. For a reduced
mean, the value kappa=1-2rho=0 remains outside this corollary.

This proof uses the previously published exact original-kernel
certificates and introduces no independent audit gate. It does
not exclude the remaining cubic-image branches, reduced
complementary blocks, or the zero-kappa conic branch.
