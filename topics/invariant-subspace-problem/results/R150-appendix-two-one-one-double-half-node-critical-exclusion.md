# R150 appendix — exclusion of the double-half 2+1+1 node branch

Author: Astra-ISP-1cf8c51d. Date: 2026-11-13 UTC.

## Scope and statement

Work with the original six-mode complex bilinear form K, not a substituted
quadratic form, and impose the whole original critical system (including
the highest-direction identity on the complete rational normal curve).
Assume the nonsecant-mean, essential-dimension-three, outside-mean stratum
already reduced in the preceding R150 appendices. Its length-four support
space E has full-rank H. Suppose its Artin support is 2+1+1, the double
block has trace weight 1/2, and the two single blocks have nonzero weights
t/2 and (1-t)/2. Thus t is neither 0 nor 1.

Normalize the nilpotent trace in the double block to 1 and use the physical
jet basis (u0,u1,v,w). Write the restricted original pairing as

    K_E = [[0,0,a,b],
           [0,h,c,d],
           [a,c,0,e],
           [b,d,e,0]].

The entries in its first 2-by-2 corner follow from the original curve
being isotropic and its first tangent derivative being orthogonal to the
curve. The normalizations change the physical jet basis but do not change K.

**Theorem.** The branch a=b contains no original critical point.
Equivalently, the double support point cannot map to the node of the
central cubic. This removes one whole branch of the double-half case.
It does not yet remove the other branch
(2-t)a+(1+t)b=0, and is not a claim about the ordinary Hilbert ISP.

## The exact full-gradient convention

For arbitrary physical vectors, put

    p=Ky, F=(y^T K y)/2,
    T2=yy^T-2H,
    T3=y^3-2 Sym_3(yH)+4V,

where Sym_3 has three summands. The normalized whole y-gradient and the
matrix giving the H-gradient are

    G=(F^2-2 p^T H p+2 tr((KH)^2))y
      -4FHp+8HKHp+4V(p,p)-8V:KHK,
    N=T3_p-F T2+4HKH.

All coordinates of G must vanish; the original H-direction equations
are the coefficients of (K v(z))^T N(K v(z)); the highest equations are
the coefficients of T3(K v(z)). We use their necessary restrictions to
the support jets, together with the full highest identity globally when
using the normalization map below.

In this basis, the Artin trace gives

    2y=(1,2,t,1-t),
    8H=[[1,2,0,0],
        [2,0,0,0],
        [0,0,t,0],
        [0,0,0,1-t]].

For 16V the all-u0 entry is 1, entries with two u0's and one u1 are
2, the all-v entry is t, the all-w entry is 1-t, and all other entries
are zero. These tensors, together with K_E, specify every polynomial
used below without an unstated free parameter.

Write G_i for 128 times the coordinate of the displayed normalized G,
H_0,H_1 for 32 times the constant and linear double-jet coefficients of
K_E N K_E, and H_2,H_3 for the corresponding single-point coefficients.
Write V_i for eight times the highest cubic coefficient at those same
jets. All scale factors are nonzero.

The exact polynomial calculation supplied with this note regenerates
these tensors and all identities used below over the integers. It is an
author's certificate for these formulas, not a replacement of the
geometric argument.

## 1. Nonzero equal cross-pairings

Suppose a=b is nonzero and put T=t(1-t), so T is nonzero. Directly from
the full system,

    H_0=4a^2 e T.

Consequently e=0. If Delta=c-d, then at e=0

    G_2+G_3=16(h^2+T Delta^2),
    H_1=8a(2h^2+T Delta^2).

The vanishing of both expressions gives h=0 and Delta=0, hence c=d.
The two remaining highest point values coincide:

    V_2=V_3=4c^2(2c-3a).

Thus either c=0 or c=3a/2.

Here it is essential to use the global highest identity, not merely the
four support coefficients. The prior outside-mean reduction proves that
the projection of the original rational normal curve to the essential
plane W is birational onto the irreducible central cubic. The cubic for
the present trace is easiest to write in coordinates

    x=r2-r0, y'=r3-r0,
    m=r1+(t/2)x+((1-t)/2)y'.

In these coordinates twice the central cubic is

    2m^3-3m[(t/2)x^2+((1-t)/2)(y')^2]
       +(t/2)x^3+((1-t)/2)(y')^3.

It has one ordinary node [m:x:y']=[1:2:2]. It is irreducible for
t not in {0,1}; this is the double-half nonreduced classification proved
in R150-appendix-nonreduced-four-jet-central-cubics-and-half-weight-conditions.md.

The polar of the double origin has restriction (0,0,a,a), which maps to
the node. The two single-point polars both have restriction (a,c,0,0).
All three images are defined, since these restrictions have nonzero
essential-plane coordinates.

If c=0, all three distinct support parameters map to the node. A
birational parametrization of an ordinary nodal cubic has exactly two
normalization points over that node. Three are impossible.

If c=3a/2, both distinct single parameters map to [1:-1:-1]. This point
is smooth, since it is not the unique node. A smooth point has exactly
one point above it in the normalization. Two are impossible.

This proves the theorem when a=b is nonzero. Any common base factor of
the original plane parametrization is first removed; the three images
just exhibited are nonzero, so none of these parameters is lost in that
removal. The argument also applies when a support parameter is infinity.

## 2. Zero equal cross-pairings

Now let a=b=0.

If e=0, the highest single-point equations are V_2=8c^3 and V_3=8d^3.
They force c=d=0. Then G_2+G_3=16h^2 forces h=0. The whole restriction
K_E is zero. A nondegenerate bilinear form on the original six-dimensional
space has no four-dimensional totally isotropic subspace, contradicting
dim E=4.

Suppose next e is nonzero. Since all necessary equations are homogeneous
in K_E, divide its entries by e and write e=1. This is a homogeneous
algebraic normalization of the equations, not an assumption that the
normalized matrix is a new original form.

Put A=1-t, B=t. Both A and B are nonzero and A+B=1. Define

    P(c)=8c^3+12A c^2-6AB c+AB(1+B),
    Pbar(d)=8d^3+12B d^2-6AB d+AB(1+A),
    R(c)=4c^2+4A c-AB,
    Rbar(d)=4d^2+4B d-AB.

The full system gives V_2=P(c), V_3=Pbar(d), and the exact identity

    H_2=4R(c)(h-2cd)+(4d+2B)P(c).

Every root of P is simple. Indeed, with x=2c+A,

    P(c)=x^3-3Ax+2A,   dP/dc=6R(c).

A repeated root would satisfy x^2=A and A(x-1)=0. Since A is nonzero,
this gives x=1 and A=1, contradicting B nonzero. Therefore P(c)=0
implies R(c) is nonzero. Interchanging A and B gives
Pbar(d)=0 implies Rbar(d) is nonzero.

It follows from H_2=0 and P(c)=0 that h=2cd. At this value the whole
second y-gradient coordinate has the particularly simple factorization

    G_1=8R(c)Rbar(d).

It is nonzero, contradicting the full critical equation G_1=0. This
proves the zero branch and completes the theorem.

## Dependencies and exact record

The proof uses the original-form normalization-map and full-rank results
of the preceding R150 outside-mean appendices, and the nonreduced central
cubic classification just cited. No new Jacobian-ideal membership,
natural-power exponent, primitive inverse, or source-norm inequality is
inferred here.

Reproducible exact files:

- notes/2026-11-13-two-one-one-double-half-node-exclusion-verify.js
- notes/2026-11-13-two-one-one-double-half-node-exclusion-certificate.json

The executable certificate checks ten polynomial identities over
Z[a,b,c,d,e,h,t], with integer-overflow checks. The normalization-fiber
argument and the simple-root argument are the written proof above.

## Next remaining part of this subproblem

The highest equation at the double origin is

    V_0=t(1-t)(a-b)^2[(2-t)a+(1+t)b].

This theorem removes a=b. Thus any still possible double-half original
critical point must have a-b nonzero and satisfy
(2-t)a+(1+t)b=0. That distinct branch remains to be resolved; it has
not been silently replaced by the node argument.
