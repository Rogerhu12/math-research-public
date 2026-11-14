# R150 appendix — no physical shifted-tangent conic companion

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. The original-kernel theorem

Let s,t be different points of the original rational normal quintic.
Let p_s(z)=K(v(s),v(z)) and p_t(z)=K(v(t),v(z)), with any local
nonzero physical representatives. Let p_s'(z) denote the polar of a
genuine first jet at s.

**Theorem.** For every complex c,

    p_s does not divide (p_s'-c p_t)^2               (1.1)

in the homogeneous binary polynomial ring.

The first jet may be rescaled by a nonzero constant and changed by
a multiple of v(s); these changes do not affect the assertion, after
rescaling c and noting that divisibility is unchanged by adding a
multiple of p_s inside the square.

In particular no vector Z and constants alpha,beta can give an identity

    p_s p_Z+(p_s'-c p_t)^2
        +alpha p_s(p_s'-c p_t)+beta p_s^2=0.          (1.2)

The statement concerns the fixed original K. It is useful when a
three-jet conic factor has its first jet shifted by a different
physical point. The unshifted case c=0 is already covered by
R150-appendix-original-physical-tangent-polars-never-square-divide.md.

## 2. Two necessary physical incidences

Take c nonzero and use the standard first derivative in a finite
source chart. Since p_s(s)=p_s'(s)=0, (1.1) would force p_t(s)=0.
Symmetry then gives p_s(t)=0. Evaluating the squared expression at
t, where p_t(t)=0, next forces p_s'(t)=0.

For distinct finite points these conditions are exactly

    q(s,t)=0,   q_s(s,t)=0,                           (2.1)

where

    k(s,z)=-(z-s)^2 q(s,z),

    q(s,z)=(s+1)z^3+(-3s^2-3s-5)z^2
            +(s^3-3s^2+22s)z+s^3-5s^2.

The infinite cases are already impossible at these incidence
conditions. If s=infinity, its polar is -1-z in the finite target
chart and its first-jet polar is 5+5z+5z^2. The only other orthogonal
point is t=-1, where the first-jet value is 5. If t=infinity, the
only finite orthogonal s is -1, and the first-jet value at infinity
is -1.

For finite s=0,2,-6, the following exact polynomial gcds apply:

    gcd_z(q(0,z),q_s(0,z))=z,
    gcd_z(q(2,z),q_s(2,z))=1,
    gcd_z(q(-6,z),q_s(-6,z))=1.

The first gcd permits only t=s=0, which is excluded. Hence from now
on s,t are finite, s is outside {0,2,-6}, and (2.1) holds.

## 3. The two projections of the ramification pair cannot both ramify

By symmetry, (2.1) says s is a repeated root of q(t,z).
The original discriminant is

    disc_z q(t,z)=t^2 E8(t),

    E8(t)=5t^8+50t^7+153t^6-936t^5-2888t^4
            +15936t^3-3392t^2-25472t+9600.

The already proved square freeness of E8 shows that this is an exact
double root with a distinct third root. The case t=0 would force
s=0; t=-1 has three distinct projective roots. Consequently

    E8(t)=0,   s=N(t)/(2D(t)),                        (3.1)

where

    D(t)=6t^4+24t^3-18t^2-36t+25,
    N(t)=3t^5+3t^4+26t^3+6t^2+110t.

The denominator D(t) is nonzero at an exact double root of a cubic
with a distinct third root. Formula (3.1) follows by eliminating
the square term between q and its derivative, equivalently the
standard identity (9AD-BC)/(2(B^2-3AC)) in cubic coefficients.

We need the following precise additional fact:

    E8(t)=0 implies E8(N(t)/(2D(t))) != 0.            (3.2)

Define the integer polynomial

    P(t)=(2D(t))^8 E8(N(t)/(2D(t))).

It has degree 40 and leading coefficient 32805. Modulo 103 its
remainder on division by E8 has ascending coefficients

    R=(64,14,24,6,66,94,97,13).

If U,V have ascending coefficients

    U=(72,75,96,47,40,7,57),
    V=(81,36,44,28,15,25,41,89),

direct multiplication gives

    U E8+V R=1 mod 103.                              (3.3)

The degrees of E8 and P remain eight and forty modulo 103, with
leading coefficients 5 and 51. Thus their integer resultant is
nonzero. This proves (3.2) over C. All integer coefficients of P
and the exact modular check are in the accompanying author record.

It follows that q(s,z) has three distinct projective roots.
Also q(s,s)=-s^2(s-2)(s+6) is nonzero by section 2.

## 4. Divisibility would put a fixed corrected tangent in the secant variety

Write

    q(t,z)=(z-s)^2 L_t(z),

where L_t is a nonzero binary linear form, absorbing its scalar
coefficient. Differentiating the original kernel gives

    p_s'=2(z-s)q(s,z)-(z-s)^2 q_s(s,z),

while

    p_t=-(z-t)^2(z-s)^2 L_t(z).

Because q(s,.) is square free, divisibility in (1.1) would imply

    q(s,.) divides p_s'-c p_t.

Modulo q(s,.), this is

    q(s,.) divides (z-s)^2[-q_s(s,.)+c(z-t)^2 L_t].

The factor z-s is invertible modulo q(s,.). The remaining forms
are binary cubics, so there would be a scalar alpha with

    q_s(s,z)=c(z-t)^2 L_t(z)+alpha q(s,z).             (4.1)

Multiplying by (z-s)^2 and applying the original K inverse, (4.1)
puts the vector

    Z_s=K^(-1)[coefficient vector of (z-s)^2 q_s(s,z)]

in span{v(s),v(t)}. In particular rank Cat(Z_s)<=2.

We now exclude this for every finite s by an exact calculation on
the original K.

## 5. The corrected tangent always has catalecticant rank three

Use S=3200K^(-1), as in the previous original-polar appendices.
Multiplying the coefficients of (z-s)^2 q_s by S gives the vector
Y(s)=3200 Z_s with coordinates

    Y0=-840-640s+550s^2+50s^3,
    Y1=-2360+640s-550s^2-50s^3,
    Y2=1280-5120s,
    Y3=-4200s^2+200s^3,
    Y4=-13824+20736s+4320s^2-7520s^3,
    Y5=-69120+103680s+21600s^2-5600s^3-9600s^4.

Form the 4-by-3 matrix Cat(Y)=(Y_(i+j)). Let P0 and P1 be the
primitive integer polynomials obtained by deleting, respectively,
row zero and row one and taking the determinant. Primitive means
division only by the positive gcd of all integer coefficients.
Both have degree ten, with leading coefficients 18750 and 9375.

For complete specification, the accompanying executable constructs
these determinants directly from the six displayed coordinates;
the certificate also lists all their integer coefficients.

Modulo 103, let A,B have ascending coefficients

    A=(70,36,85,91,37,88,29,66,5,75),
    B=(0,3,29,102,96,90,29,22,91,56).

Then

    A P0+B P1=1 mod 103.                             (5.1)

Both degrees ten are retained, since their leading coefficients
reduce to 4 and 2. Thus P0 and P1 are coprime over C. They cannot
simultaneously vanish at any finite s, so Cat(Y(s)), and hence
Cat(Z_s), has rank three.

This contradicts the secant consequence of (4.1). The supposed
divisibility is impossible. Together with sections 1 and 2, all
complex coefficients and all finite/infinite point configurations
have been covered.

## 6. Exact record and use boundary

- notes/2026-11-14-shifted-tangent-conic-companion-verify.js
- notes/2026-11-14-shifted-tangent-conic-companion-certificate.json

The executable builds the integer corrected-tangent vector,
its two catalecticant determinants, the full degree-forty composition,
and the exceptional source gcds. It checks the two displayed modular
Bezout identities and retained degrees. The finite-field calculations
prove nonzero integer resultants; no finite-field lack of points is
used as a surrogate for a complex conclusion.

The theorem rules out the specific original conic relation (1.2).
It does not exclude every three-dimensional conic projection or
complete the remaining rank-two-mean critical classification.
