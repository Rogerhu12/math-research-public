# R150 appendix — the rank-two inside four-jet section has no cubic projection

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. The remaining exact section

Assume the original complete critical equations,

    rank Cat(y)=2, ess(T3)=W, dim W=3,
    y in W, ess(V)=4.

The previous support and double-block exclusions leave

    g=D+R, deg D=deg R=2, D and R disjoint,
    R=r+t with r!=t, W=Cy+span(X,Z),

where X,Z are the two complementary physical values.
The exact ordinary third tensor has form

    T3=kappa Y^3-6Y(hX^2+kZ^2)+4(vX^3+wZ^3),       (1.1)

with Y=y and v,w nonzero. The zero-kappa reduced-mean branch
has already been excluded, so kappa is nonzero.

**Theorem.** The physical projection of W cannot have an
irreducible cubic as its image. Thus this section leaves only
the nondegenerate conic projection.

Both reduced and double mean divisors D are included.

## 2. A pure physical obstruction when the two complementary values pair nontrivially

We first prove a statement requiring only (1.1), the highest
identity, and a cubic image.

Let g_R=K(X,Z). Suppose g_R is nonzero. At the physical source
r of X, the three projected coordinates are

    [p_Y(r):p_X(r):p_Z(r)]=[l_1:0:g_R].

This point has no projection basepoint. The physical value polar
p_X has a zero of order at least two at r: both its value and
its first source derivative vanish because the original curve
is K-isotropic.

A cubic image is birationally parametrized: after removing the
common divisor of the three quintics, its degree times the map
degree is at most five, so its map degree is one. The source
P1 is therefore the normalization of that irreducible cubic.

Write the displayed image point as P=[t:0:1]. Restriction of
(1.1) to X=0 is

    f(t)=kappa t^3-6kt+4w.                          (2.1)

If t is a simple root, P is a smooth point of the cubic and
the line X=0 meets it transversely. The pullback of X then has
order one at r, contradicting the physical double zero.

If t is a repeated root, kappa and w being nonzero give

    t!=0, kappa t^2=2k, w=kt.

It is an exact double root, since f''(t)=6kappa t is nonzero.
The cubic itself is singular at P, because its X derivative
also vanishes there. In local variables eta=Y-t, xi=X, Z=1,
its tangent cone is

    3t(kappa eta^2-2h xi^2).                        (2.2)

If h is nonzero this is an ordinary node, and the line X=0
is transverse to both branches. Its pullback on each branch
again has order one, contradicting the physical double zero.

It remains to allow h=0. Now use the physical source t of Z
instead. It has nonzero X coordinate g_R, and the restriction
of the cubic to Z=0 is

    kappa Y^3+4vX^3.

This binary cubic has three distinct roots because kappa,v
are nonzero. Thus the same smooth transverse-intersection
contradiction applies at the source of Z.

Every possibility is excluded. We have proved the pure
highest-identity consequence

    K(X,Z)=0.                                      (2.3)

Evaluating (1.1) at the two physical sources now gives

    K(y,X)=K(y,Z)=0,                                (2.4)

because the remaining term at each source is kappa times
the cube of the corresponding y polar.

These arguments are projective and include physical sources
at infinity without change.

## 3. The original second gradient forces F=0

Let E=E_g be the exact four-dimensional physical support, and
let lambda span ann(W) in E*. The universal length-four
projection theorem gives common divisor degree delta_E<=1.
For the cubic W projection, birationality gives delta_W=2.

Therefore at least one source maps, after removal of the E
common divisor, to the projection center [lambda]. In particular
lambda belongs to the actual four-dimensional physical curve C_E.

The original second-gradient quadric

    N=T3_p-F T2+4HKH,
    p=Ky, F=K(y,y)/2, T2=y^2-2H,

vanishes on C_E. Hence

    lambda^T N lambda=0.                           (3.1)

The exact two mean blocks determine this value.

For a reduced mean, use x=a v(s), z=b v(t), y=x+z, u=x-z,
and lambda(u)=1. The already established normal form is

    H_D=(rho/2)(y^2+u^2),
    V_D=(rho/4)(y^3+3yu^2),
    kappa=1-2rho, rho!=0.

Physical isotropy gives K(y,u)=0 and K(u,u)=-2F. Since lambda
annihilates T3 and y,

    lambda^T N lambda
      =2F H(lambda,lambda)+4K(Hlambda,Hlambda)
      =rho(1-2rho)F=rho kappa F.                    (3.2)

For a double mean y=a u0+b u1, b!=0, let u=u0 and again
lambda(u)=1. Its exact block is

    H_D=eta u^2,
    V_D=(3eta/2)y u^2, eta!=0, kappa=1.

Here K(u,u)=K(y,u)=0, so the same direct calculation gives

    lambda^T N lambda=2eta F.                       (3.3)

All coefficients multiplying F in (3.2)-(3.3) are nonzero.
Thus (3.1) proves

    F=0.                                           (3.4)

No assumption that the quadric is nonzero or has a smooth
center is needed for this step.

## 4. The complete first gradient excludes the remaining orthogonal configuration

Use the basis (y,u,X,Z). Equations (2.3)-(2.4) and (3.4)
show that the only potentially nonzero entries of K|E are

    n_1=K(u,X), n_2=K(u,Z).

In particular the y row is zero, and K(u,u)=0 in both mean
types. Write a_u for the nonzero u^2 coefficient of H_D:
it is rho/2 for a reduced mean and eta for a double mean.

The exact original normalized first gradient is

    Gamma=(F^2-2b+2tau2)y-4FHp+8HKHp
              +4V(p,p,.)-8V:(KHK).

Because p=Ky annihilates all E, the terms involving Hp and
V(p,p,.) vanish. The first displayed term lies in Cy.
The mean part of V contributes no X or Z component.
Finally,

    (KHK)|span(X,Z)=a_u n n^T.

Therefore the two complementary components of the complete
first-gradient equation are exactly

    -8a_u v n_1^2=0,
    -8a_u w n_2^2=0.                                (4.1)

The three coefficients a_u,v,w are nonzero, so n_1=n_2=0.
It follows that K|E is identically zero.

This would make the four-dimensional E totally isotropic
for a nondegenerate form on a six-dimensional space. It is
impossible: E contained in E-perpendicular would require
4<=6-4=2. Equivalently its two complementary physical points
would both be basepoints of the length-four projection,
already contradicting its universal one-basepoint bound.

The theorem is proved.

## 5. Exact scope

The proof keeps the original D blocks in both low gradients.
Section 2 is a separate physical contact argument for the
two reduced complementary values; it uses their nonzero
third-moment coefficients and the nonzero effective cube
coefficient, not a stronger unproved assertion about every
plane cubic.

The preceding zero-kappa and double-complementary-block
theorems together with this result leave only the conic
projection for the inside/full-four-jet rank-two-mean section.
That conic still has to satisfy the complete original
low-gradient equations; this note does not claim it exists.

The low-third-moment cases are being classified separately.
No global Jacobian power or ordinary invariant-subspace
conclusion follows from this sectional exclusion.
