# R150 appendix — the reduced four-point original Gram matrix has rank at least three

Author: Astra-ISP-1cf8c51d. Date: 2026-11-13 UTC.

## Statement

Consider an original complete critical point in the nonsecant-mean,
essential-dimension-three, outside-mean stratum. Suppose its unique
length-four support consists of four distinct physical curve points
s0,s1,s2,s3. The preceding outside-mean and basepoint exclusions give
rank H=4 and a basepoint-free four-dimensional physical projection.
Normalize the four physical representatives u_i by the same functional
lambda so that

    lambda(u_i)=1,  lambda|_W=0,  lambda(y)=1.

The physical space is E=span(u_0,u_1,u_2,u_3)=W+Cy. Define its original
Gram matrix

    B_ij=K(u_i,u_j).

Here B is the restriction of the original nondegenerate six-mode
bilinear form K. It is not the quadratic relation N supplied by the
second gradient.

**Theorem.** rank B is at least three.

This is a necessary condition on the actual physical support, independent
of the remaining weight parameters. In particular a solution of the
restricted moment-gradient equations whose Gram matrix has rank at most
two cannot lift to an original critical point in this stratum. The
theorem does not assert that the restricted gradient equations force
rank at most two; that algebraic step remains separate.

## 1. The already established original parametrizations

Write

    Phi(z)=[K(u_0,v(z)):K(u_1,v(z)):K(u_2,v(z)):K(u_3,v(z))]
          in P(E*),

where v(z) is a local homogeneous representative of the original
rational normal curve. This is a basepoint-free morphism on P1; all
statements are homogeneous and include z=infinity.

The original highest equation and the outside-mean reduction show that
projection from [lambda] to P(W*) becomes, after removing its common
quadratic factor, a birational parametrization

    psi:P1 -> C,

where C is an irreducible ordinary nodal plane cubic. The common factor
does not meet the original four-point support.

For completeness, the latter nonintersection also follows immediately
at the four points from the assumptions already stated. At z=s_i the
coordinate vector of Phi is the nonzero i-th column of B, since Phi is
basepoint free. It cannot be proportional to lambda=(1,1,1,1):
its evaluation on u_i is B_ii=K(u_i,u_i)=0, whereas lambda(u_i)=1.
Thus Phi(s_i) is not the projection center, and psi(s_i) is its actual
well-defined projective image.

A birational morphism from P1 to an ordinary nodal cubic identifies P1
with the normalization. Every smooth point of C has one preimage; the
unique node has exactly two distinct preimages. Consequently the union
of any two point fibers contains at most three parameter points.

These properties are established in the earlier R150 four-jet
smooth-center, nonreduced/reduced central-cubic, and four-point
basepoint-exclusion results. No assumption about smoothness of the
four-dimensional image Phi(P1) is needed.

## 2. A rank-two Gram matrix gives at most two image points

Suppose first rank B=2. Let R be the radical of K restricted to E.
The quotient E/R has dimension two and carries a nondegenerate symmetric
bilinear form. Over the complex numbers its isotropic cone is the
union of exactly two distinct one-dimensional subspaces.

Each physical u_i is isotropic because the original curve is K-isotropic.
Its class in E/R is nonzero: a zero class would make B's i-th column
zero and would give a basepoint Phi(s_i), which has been excluded.
Therefore the four nonzero quotient classes [u_i mod R] lie in the
union of those two isotropic lines.

The map

    E/R -> image(B) in E*,   [u] -> K(u, .)|_E,

is a linear isomorphism. Hence the four nonzero polar columns B e_i
lie in at most two projective points of P(E*). Equivalently,

    cardinality {Phi(s_0),Phi(s_1),Phi(s_2),Phi(s_3)} <= 2.

Projecting these points from lambda, which is none of them, cannot
increase their number. Thus the four distinct parameters s_i belong
to the union of at most two fibers of psi. Section 1 shows that such
a union has at most three points. This contradiction excludes rank two.

The argument covers both possible nontrivial partitions of four support
points between the two isotropic lines. Three on one line already exceed
one nodal fiber; two on each line would require two different double
fibers, whereas an ordinary nodal cubic has only one. If the two
four-dimensional points project to the same plane point, the contradiction
is stronger, since one fiber would then have four elements.

## 3. Lower ranks

A nonzero symmetric rank-one matrix over C has the form c aa^T with
c nonzero. Its zero diagonal would imply a_i^2=0 for every i, hence
a=0, a contradiction. Since every B_ii is zero, rank one is impossible.

Rank zero would make every polar column zero, contradicting the
basepoint-free values Phi(s_i). Equivalently it would make E a
four-dimensional totally isotropic subspace of a nondegenerate
six-dimensional bilinear space, which is also impossible.

Thus rank B cannot be 0, 1, or 2, proving rank B>=3.

## Dependencies and remaining interface

The original facts used here can be found in:

- R150-appendix-four-jet-smooth-quadric-center-and-birational-projection.md
- R150-appendix-reduced-four-point-basepoint-critical-section-is-empty.md
- R150-appendix-reduced-four-point-single-half-weight-exclusion.md

The last file records the current reduced four-point class, the unique
2+2 half-weight partition, and the exact normalization-fiber assumptions.
This proof applies to that class, including the equal block-pairing
case where the node fiber is tangent to the original quadric at the
projection center. It does not use transversality of that fiber, so
there is no omitted equal-pairing exception.

No finite-field enumeration, positive-definite argument, Jacobian-power
claim, or operator inverse estimate is involved. The continuing algebraic
task is to determine whether the remaining full moment-gradient system
can admit rank-three or rank-four physical Gram data.
