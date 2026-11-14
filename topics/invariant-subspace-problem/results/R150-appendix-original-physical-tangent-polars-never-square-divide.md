# R150 appendix — original tangent polars never satisfy the square-divisibility condition

Author: Astra-ISP-1cf8c51d. Date: 2026-11-13 UTC.

## 1. Statement for the original form

Let v(s) be a local nonzero representative of the original rational
normal quintic and let K be the original six-mode form. For any
s in P1 define the binary quintic

    p0(z)=K(v(s),v(z)).

Let u1 be any first physical jet transverse to v(s), so in a local
parameter u1=alpha v'(s)+beta v(s), with alpha nonzero, and put
p1(z)=K(u1,v(z)).

**Theorem.** In the homogeneous binary polynomial ring,

    p0 does not divide p1^2.                          (1.1)

This holds at every finite s and at infinity. Consequently there is
no vector Z, and no scalars c0,c1, for which

    p0 K(Z,v(z))+p1^2+c1 p0 p1+c0 p0^2=0             (1.2)

identically in z. The vector Z is unrestricted. Thus (1.2) cannot be
rescued by shifting a second jet by a vector from another support.

Since adding a multiple of p0 to p1 and multiplying p1 by a nonzero
scalar do not change divisibility in (1.1), it suffices to use the
ordinary first derivative at a finite point and the reciprocal
coordinate derivative at infinity.

## 2. The original cubic kernel factor

For finite s,

    k(s,z)=p0(z)=-(z-s)^2 q(s,z),

where

    q(s,z)=(s+1)z^3+(-3s^2-3s-5)z^2
             +(s^3-3s^2+22s)z+s^3-5s^2.

Both variables are understood homogeneously when discussing infinity.
Its coefficient pairing matrix in degree-three monomials is

    Cq=[[0,0,-5,1],
        [0,22,-3,1],
        [-5,-3,-3,0],
        [1,1,0,0]],        det Cq=70.

It is invertible. Hence the projective map s -> [q(s,.)] is the
degree-three Veronese embedding followed by an invertible linear map.
Its derivative is nowhere proportional to its value. In a finite
source chart, q_s(s,.) is therefore not proportional to q(s,.).

Also

    q(s,s)=-s^2(s-2)(s+6).

We first treat s outside {0,2,-6,infinity}.

## 3. Simple and repeated roots away from the diagonal

Suppose q(s,.) has three distinct projective roots. None is s.
If p0 divided (partial_s p0)^2, then at every one of those roots
partial_s p0 would vanish. At such a root,

    partial_s p0=-(z-s)^2 q_s(s,z).

Thus q_s would vanish at all three roots of q. Both are binary cubics,
so q_s would be proportional to q, contradicting the immersion just
proved. This also covers a simple root at infinity.

Now suppose q(s,.) has a repeated root. Its exact discriminant is

    disc_z q(s,z)=s^2 E8(s),

where

    E8(s)=5s^8+50s^7+153s^6-936s^5-2888s^4
            +15936s^3-3392s^2-25472s+9600.            (3.1)

The polynomial E8 is square free over C. Here is a compact exact
certificate. Modulo 103, let U,V have ascending coefficients

    U=(5,63,7,16,40,56,73),
    V=(10,102,24,85,53,56,17,81).

Direct multiplication gives

    U E8+V E8'=1 mod 103.                            (3.2)

The degrees eight and seven of E8 and E8' are retained modulo 103,
since their leading coefficients are 5 and 40. Thus their integer
resultant is nonzero, proving the claimed square freeness over C.
The attached executable reconstructs (3.1) and checks every coefficient
of (3.2).

For the present s, s is nonzero, so a zero of the discriminant is
simple. A simple discriminant zero means that q has exactly one
double root u and one distinct simple root w, and q_s(s,u) is nonzero.
This last assertion can also be checked directly: at
q=A(z-u)^2(z-w), with A nonzero, the first variation of its
discriminant in the direction h(z) is

    -4 A^3 (u-w)^3 h(u).

A triple root would make all first variations vanish. Taking
h=q_s proves the assertion. The leading coefficient A=s+1 cannot
vanish in this repeated-root case: at s=-1 the homogeneous cubic
has one simple root at infinity, and its remaining quadratic is
-5z^2-26z-6 with discriminant 556; equivalently E8(-1)=13900.

The double root u differs from s, because q(s,s) is nonzero in
the current case. Therefore

    partial_s p0(u)=-(u-s)^2 q_s(s,u) is nonzero.

This is incompatible with p0 dividing (partial_s p0)^2. It excludes
all repeated-root cases away from the four diagonal exceptions.

## 4. The four exceptional physical points

At s=0,

    p0=z^4(5-z),
    p1=z^3(-32+5z-z^2).

The root z=5 of p0 is not a root of p1: p1(5)=-4000.

At s=2,

    q(2,z)=(z-2)(3z^2-17z+6),
    q_s(2,z)=z^3-15z^2+22z-8.

The residual quadratic has discriminant 217 and is square free.
Its remainder in q_s is

    q_s(2,z) mod (3z^2-17z+6)=(96-296z)/9,

which is not zero. Thus at least one residual root of q is not
a root of q_s. At that root p1 is nonzero and p0 is zero.

At s=-6,

    q(-6,z)=-(z+6)(5z^2+65z+66),
    q_s(-6,z)=z^3+33z^2+166z+168.

The residual quadratic has discriminant 2905. The exact remainder is

    q_s(-6,z) mod (5z^2+65z+66)=(-480-536z)/5,

again nonzero. The same argument applies. These residual roots are
different from the diagonal point in both cases.

Finally use v_infinity(x)=(x^5,x^4,x^3,x^2,x,1). At x=0 the
finite-z expressions of the two homogeneous quintics are

    p0=-1-z,   p1=5+5z+5z^2.

At the finite root z=-1 of p0, p1=5. The extra powers at target
infinity do not alter this failed divisibility.

All points of P1 have now been treated, proving (1.1). Equation
(1.2) would imply the forbidden divisibility, so it is impossible.

## 5. Scope and reproducible record

This is a statement about the fixed original K. It does not assert
the same property for an arbitrary quadric containing a rational
normal curve. It is particularly useful for a length-three jet
cubic with a nonzero top jet: after a possible shift of the second
jet, its irreducible conic factor would force exactly (1.2).

The original kernel and discriminant also occur in
R150-appendix-no-secant-cuspidal-companion-and-outer-mean-rank-drop-exclusion.md;
the present square-divisibility conclusion is a separate statement.

Exact author files:

- notes/2026-11-13-physical-tangent-polar-nondivisibility-verify.js
- notes/2026-11-13-physical-tangent-polar-nondivisibility-certificate.json

The certificate uses integer polynomial arithmetic for the original
discriminant, the two exceptional remainders, the special values,
and det Cq; the finite-field identity is used only to prove the
nonzero integer resultant giving square freeness, not as a substitute
for the complex geometric proof.
