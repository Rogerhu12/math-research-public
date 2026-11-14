# R150 appendix — exclusion of the double-half 2+1+1 nonnode branch

Author: Astra-ISP-1cf8c51d. Date: 2026-11-13 UTC.

## Statement and exact scope

Retain the original six-mode bilinear form K and all original critical
equations. Work in the nonsecant-mean, essential-dimension-three,
outside-mean stratum in which H has rank four and the unique
length-four Artin support has type 2+1+1. Normalize its trace as

    tau(u0)=1/2, tau(u1)=1,
    tau(v)=t/2, tau(w)=(1-t)/2,   t not in {0,1}.

The notation means the usual double-block coordinate basis and two
single-point idempotents; the corresponding physical jet vectors are
also denoted (u0,u1,v,w). In that physical basis put

    K_E = [[0,0,a,b],
           [0,h,c,d],
           [a,c,0,e],
           [b,d,e,0]].

**Theorem.** The branch a-b nonzero and
(2-t)a+(1+t)b=0 contains no original critical point.

Together with
R150-appendix-two-one-one-double-half-node-critical-exclusion.md, this
removes the entire double-block-half class. Together with the previously
published conic and single-point-half exclusions, it removes every
2+1+1 support in this stratum. This result does not remove the reduced
four-point case or the other mean/essential-dimension strata, and does
not solve the ordinary Hilbert ISP.

## 1. Full-gradient conventions

Use exactly the conventions of the preceding node-branch appendix:

    p=Ky, F=y^T K y/2,
    T2=yy^T-2H,
    T3=y^3-2 Sym_3(yH)+4V,

    G=(F^2-2p^T H p+2tr((KH)^2))y
      -4FHp+8HKHp+4V(p,p)-8V:KHK,
    N=T3_p-F T2+4HKH.

Write G_i for 128 times the coordinates of G, H_i for 32 times
the support-jet coefficients of K_E N K_E, and V_i for eight times
the corresponding coefficients of T3(K_E r). The support order is
the double origin, its first derivative, then the two single points.

The actual trace tensors are

    2y=(1,2,t,1-t),
    8H=[[1,2,0,0],
        [2,0,0,0],
        [0,0,t,0],
        [0,0,0,1-t]],

and 16V has all-u0 entry 1, two-u0/one-u1 entries 2,
all-v entry t, all-w entry 1-t, and all other entries zero.

In particular the first highest equation factors exactly as

    V_0=t(1-t)(a-b)^2[(2-t)a+(1+t)b].

The a=b factor was removed in the preceding appendix. Because the
remaining equations are homogeneous in K_E, normalize a-b=3. This gives

    a=t+1, b=t-2.                                      (1)

The normalization divides all Gram entries by one common nonzero
scalar. No alternative physical form is introduced.

## 2. Two first-jet equations and the exceptional support weights

At (1), the next highest equation and the constant H equation are

    V_1=9t(t-1)[6h-(t+1)d+(t-2)c],

    H_0=2t(t-1)[18h-6(t+1)d+6(t-2)c
                         +(t-2)(t+1)e].

Since t is neither 0 nor 1, their vanishing gives

    6h=(t+1)d-(t-2)c,
    18h=(t-2)(t+1)e.                                  (2)

If t=-1, these force h=c=0, while a=0. The physical
length-three jet support span(u0,u1,v) is then totally isotropic.
If t=2, they force h=d=0, while b=0, so span(u0,u1,w)
is totally isotropic. Both cases contradict the original-form
classification in
R150-appendix-classification-of-isotropic-length-three-curve-jets.md:
the only isotropic length-three curve supports are the two reduced
three-point supports W_+ and W_-, with no 2+1 support, including at
infinity.

Henceforth t avoids -1,0,1,2. Equations (2) can be parametrized without
losing any case by

    c=(t+1)u,
    d=(t-2)(u+e/3),
    h=(t+1)(t-2)e/18.                                 (3)

For integer formulas replace K_E by 18K_E and denote the resulting
gradient polynomials by Ghat_i and Hhat_i. Thus its entries are

    a'=18(t+1), b'=18(t-2),
    c'=18(t+1)u, d'=18(t-2)u+6(t-2)e,
    h'=(t+1)(t-2)e, e'=18e.

Every equation is unchanged as a zero condition.

## 3. The cross-pairing e must vanish

The following direct identity uses just two coordinates of the whole
y-gradient:

    -(t+1)Ghat_2+(2-t)Ghat_3
      =-64(t+1)(t-2)(2t-1)(14t^2-14t-1)e^2.           (4)

Consequently, if e is nonzero, only these weights remain:

    t=1/2, or 14t^2-14t-1=0.                          (5)

There is no numerical or generic-rank inference in (4); it is an
integer polynomial identity.

At t=1/2, Hhat_1 is a nonzero constant multiple of -e, immediately
contradicting e nonzero.

Now suppose q(t)=14t^2-14t-1=0. Reducing Hhat_1 modulo q and dividing
by a nonzero numerical constant gives the necessary equation

    e[9+(10t-5)e]=0.

Because e is nonzero and (2t-1)^2=9/7, this fixes

    e=(7-14t)/5.                                      (6)

Substitute (6) into Ghat_0 and Ghat_1 and reduce modulo q. After
nonzero numerical rescalings, their necessary vanishing equations are

    P0=-37-460u-150u^2+182t+140tu=0,
    P1=-111+160u+150u^2-42t-140tu=0.

Their sum is

    -148-300u+140t=0,

so u=(35t-37)/75. But then, using t^2-t=1/14,

    P0=3894/25,

which is nonzero over the complex numbers. This contradicts P0=0.
Thus neither root of q is possible, and (5) has been exhausted. We
conclude

    e=0.                                             (7)

All reductions in this paragraph take place over the rational
coefficient field with denominators explicitly cleared in the supplied
certificate. In particular they cover both complex embeddings of the
quadratic weight, not merely a test field or a sample of parameters.

## 4. The remaining matrix would ramify over a smooth point

At e=0 the first whole-gradient coordinate simplifies to

    Ghat_0=46656t(1-t)u^2.

Thus u=0. Equations (3) now give c=d=h=0, leaving

    K_E = [[0,0,t+1,t-2],
           [0,0,0,0],
           [t+1,0,0,0],
           [t-2,0,0,0]].                             (8)

A merely restricted support calculation does not by itself exclude
(8). Use now the global highest equation on the original curve.

The central cubic in the essential plane W is irreducible with one
ordinary node. In coordinates

    x=r2-r0, y'=r3-r0,
    m=r1+(t/2)x+((1-t)/2)y',

its equation, up to a nonzero scalar, is

    2m^3-3m[(t/2)x^2+((1-t)/2)(y')^2]
      +(t/2)x^3+((1-t)/2)(y')^3=0.

Its unique node is [1:2:2]. The established outside-mean reduction
identifies the plane projection of the original rational normal curve,
after cancelling its common base divisor, as a birational
parametrization of this cubic.

The polar of the double origin, by (8), is

    (0,0,t+1,t-2),

and its plane image is

    [m:x:y']=[2t-1:t+1:t-2].                          (9)

This image is defined, and is not the node: its last two coordinates
differ by 3. Since the cubic has no other singular point, (9) is smooth.

On the other hand, the entire second column of (8) is zero, so

    K(u1,E)=0, and hence K(u1,W)=0.                    (10)

The physical first jet u1 is a nonzero tangent derivative of the
normalized original curve, possibly plus a multiple of u0. Concretely,
in a local parameter at the double point,

    u1=alpha v'(s)+beta v(s),   alpha nonzero,

with the same statement in the reciprocal parameter when s is infinity.
Equation (10) therefore says that the derivative of the projective
plane projection at s is zero. No cancelled base factor can change
this conclusion: the value at s is the nonzero point (9), so the
projection is already defined there.

A birational morphism from the smooth parameter line to an irreducible
cubic factors through its normalization. The resulting map between the
two smooth normalization curves has degree one and is an isomorphism.
Over the smooth locus of the cubic, the normalization itself is a local
isomorphism. Therefore this parametrization has nonzero differential
at every preimage of a smooth point. Its differential cannot vanish
at the point (9). This contradicts (10), excluding (8).

This finishes the nonnode branch.

## 5. Consequences and the continuing work boundary

The node branch a=b and the nonnode branch are now both empty. The
nonreduced central-cubic classification says that a critical 2+1+1
support must have either a single-point half weight or a double-block
half weight. The former, including its reducible conic intersection,
was already excluded in
R150-appendix-two-one-one-conic-and-single-half-weight-critical-exclusion.md.
Thus no 2+1+1 support remains in the stated stratum.

Combining this with the separately proved quadruple-jet, 3+1, and 2+2
exclusions removes all nonreduced length-four supports in this same
nonsecant-mean, essential-dimension-three, outside-mean, rank-four-H
problem. The reduced four-point analysis, lower mean rank, other
essential dimensions, original Jacobian natural powers, and the actual
inverse/source-norm interfaces retain their separate obligations.
No global completion statement is made.

## Reproducible author record

- notes/2026-11-13-two-one-one-double-half-nonnode-exclusion-verify.js
- notes/2026-11-13-two-one-one-double-half-nonnode-exclusion-certificate.json

The executable reconstructs the actual trace tensors and checks eleven
exact identities: the highest branch factor, the two equations (2),
the syzygy (4), the e=0 formula, the half-weight H equation, the
quadratic-weight H reduction, the two displayed P equations, their
linear sum, and the nonzero constant residual. Integer arithmetic is
checked for overflow; the quadratic reductions use rational BigInt
arithmetic. The original-form length-three classification and the
smooth-point immersion contradiction are the written geometric proof.
