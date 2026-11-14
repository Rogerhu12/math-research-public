# R150 appendix — the two physical values in a diagonal conic companion must be orthogonal

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Statement

Let Y,X,Z be independent directions, with X,Z two distinct
physical values of the original rational normal quintic.
Suppose

    T3=kappa Y^3-6Y(hX^2+kZ^2)+4(vX^3+wZ^3),       (1.1)

where kappa,v,w are all nonzero, vanishes on the original
physical projection of their span. Assume that image is a
nondegenerate conic.

**Theorem.** K(X,Z)=0.

This is a pure original-kernel statement. It does not assume
a catalecticant rank for Y, complete low-gradient criticality,
or any external fourth direction.

## 2. The exact conic factor

The conic divides (1.1). Normalize its complementary linear
factor to Y-A, with A=aX+bZ. Then

    Q=kappa Y^2+kappa AY+kappa A^2-6H_R,
    4V_R=-kappa A^3+6AH_R.

The nonzero v,w force a,b both nonzero. The missing two mixed
monomials of V_R give

    h=kappa a^2/2, k=kappa b^2/2,
    v=kappa a^3/2, w=kappa b^3/2.

Replace X,Z by the still physical nonzero multiples P=aX,
Q0=bZ. The conic equation, after division by kappa, is

    C=Y^2+(P+Q0)Y-2P^2+2P Q0-2Q0^2=0.              (2.1)

Both coordinate lines P=0 and Q0=0 meet this conic in two
distinct points: their binary equations are respectively

    (Y-Q0)(Y+2Q0)=0, (Y-P)(Y+2P)=0.                 (2.2)

## 3. Nonorthogonality would force ramification at both physical sources

Assume g=K(P,Q0) is nonzero, and let r,t be the distinct
physical sources of P,Q0.

At r the projected coordinates have P=0 and Q0=g!=0.
Thus there is no basepoint at r. The physical polar p_P
has a zero of order at least two at its own source.
By (2.2), its coordinate line has only simple intersection
with the conic. Therefore the map from the parameter P1 to
the conic must be ramified at r. The same applies at t.

If d is the common divisor of the three quintics, delta its
degree, and e the conic map degree, then

    delta+2e=5.

The birational option e=1 cannot have this ramification.
Hence e=2 and delta=1. The two distinct sources r,t are
the two ramification points of this degree-two map.

If either r or t were infinity, its physical polar would
have self-contact order four. The map degree is only two
and (2.2) is a simple intersection, so that order is impossible.
Thus r,t are finite.

Write s for the unique basepoint. It is distinct from r,t,
because their cross pairing g is nonzero. It is finite as
well: a finite physical value v(r) has polar value -(r+1)
at infinity; two distinct finite values cannot both have
that value zero.

The degree-two map has a coordinate expression equivalent to

    ((z-r)/(z-t))^2.

Consequently its conic coordinates, after removal of z-s,
belong to

    span((z-r)^4,(z-r)^2(z-t)^2,(z-t)^4).            (3.1)

The original polar of P is a nonzero scalar multiple of

    -(z-r)^2 q(r,z),

where the unchanged original cubic kernel is

    q(r,z)=(r+1)z^3+(-3r^2-3r-5)z^2
             +(r^3-3r^2+22r)z+r^3-5r^2.

Using its double self factor in (3.1) gives

    q(r,z)/(z-s) in span((z-r)^2,(z-t)^2).

Likewise,

    q(t,z)/(z-s) in span((z-r)^2,(z-t)^2).           (3.2)

We now show that these necessary conditions never hold for
the original q.

## 4. Four explicit equations in symmetric coordinates

Put x=r+t and y=rt. A quadratic alpha z^2+beta z+gamma
belongs to span((z-r)^2,(z-t)^2) exactly when

    2gamma+x beta+2y alpha=0.

Dividing q(r,z) by z-s and applying this condition gives

    J(r,t;s)=2C_r+(2s+x)B_r+(2s^2+sx+2y)A_r=0,

where

    A_r=r+1, B_r=-3r^2-3r-5, C_r=r^3-3r^2+22r.

The corresponding equation for t also holds. Reducing powers
of r using r^2=xr-y shows directly that

    J(r,t;s)
      =-r[x^2+(9+5s)x-2s^2+6s-44]
         +(x+8+6s)y+2s^2-10s+(s-5)x.

Since r!=t, both J equations imply

    x^2+(9+5s)x-2s^2+6s-44=0,                     (4.1)
    (x+8+6s)y+2s^2-10s+(s-5)x=0.                  (4.2)

Also q(r,s)=q(t,s)=0. By symmetry of q, r,t are roots of
q(s,z). Set

    a=s+1, b=-3s^2-3s-5,
    c=s^3-3s^2+22s, d=s^3-5s^2.

The quadratic z^2-xz+y divides q(s,z), so its linear
quotient has coefficient b+ax. Comparing coefficients gives

    c=a y-(b+ax)x,
    d=(b+ax)y.                                     (4.3)

These equations remain necessary when a=0; no division by
s+1 or leading coefficient has been used.

## 5. Two incompatible degree-eight eliminants

For compact notation put

    S=9+5s, R=44-6s+2s^2,
    P=44+60s-7s^2+3s^3,
    Q=14+17s+8s^2.

Equations (4.1) and (4.3) give

    a y=P-Qx.

Multiplying (4.2) by a, substituting this identity, and
reducing x^2 using (4.1) gives

    L(s)x+C0(s)=0.

Doing the same with the last equation in (4.3) gives

    M(s)x+N(s)=0,

where ascending coefficient lists are

    L  = [53,59,-15,-5],
    C0 = [-264,70,18,-2,2],
    M  = [-240,-580,-566,-268,-67],
    N  = [836,1712,1214,434,-9,25].

No division by L,M,a or any source difference enters these
necessary consequences.

Thus both of the following explicit integer polynomials vanish:

    E=L N-M C0,

    4T=C0^2-S C0 L-R L^2.

Their ascending coefficient lists are

    E=[-19052,3740,48306,43596,8939,-2244,1242,72,9],
    T=[18007,-29632,-19492,11840,-744,-336,124,8,1].

They are relatively prime over C. An exact certificate
modulo 103 is

    U=[73,46,75,98,37,70,33,32],
    V=[35,28,17,78,24,76,12,21],

    U E+V T=1 in F_103[s].

Both degrees eight are retained modulo 103, with leading
coefficients 9 and 1. Therefore a nonconstant characteristic-zero
common factor would retain positive degree modulo 103,
contradicting this identity.

This rules out every finite s, including s=-1. Together with
the infinity exclusions in section 3, all possible parameters
have been covered. The assumed g!=0 is impossible, proving
K(X,Z)=0.

## 6. Exact original reconstruction

- notes/2026-11-14-physical-two-point-conic-ramification-verify.js
- notes/2026-11-14-physical-two-point-conic-ramification-certificate.json

The BigInt calculation reconstructs the kernel from the original
K, checks the symmetric J identity, builds L,C0,M,N and both
eliminants, and verifies the displayed finite-field Bezout
certificate and retained degrees. The finite-field identity
proves nonzero characteristic-zero resultant; it is not a
finite-field zero search used in place of a complex proof.

The theorem leaves the orthogonal-pair case as a geometric
possibility. In the current four-jet critical section the full
low gradients must still be applied to it, with both mean
blocks retained.
