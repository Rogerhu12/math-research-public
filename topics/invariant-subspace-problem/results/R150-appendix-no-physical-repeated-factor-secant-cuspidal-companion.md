# R150 appendix — no physical repeated-factor / secant cubed-factor cusp companion

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. The original-kernel statement

Let v(s) be a physical point of the original rational normal quintic,
let K be the original six-mode form, and let L be a nonzero vector not
parallel to v(s), with

    rank Cat(L)<=2,
    Cat(L)=(L_(i+j))_(0<=i<=3,0<=j<=2).

**Theorem.** There do not exist a nonzero binary quadratic G and
independent binary linear forms a,b such that

    K(v(s),v(z)) is proportional to G a^3,
    K(L,v(z))    is proportional to G a^2 b.           (1.1)

This is the reverse placement of the physical point from the
previously proved no-secant cuspidal-companion lemma: here the
physical point supplies the repeated factor of the cusp, and the
secant direction supplies its cubed factor.

Consequently an essential three-dimensional tensor

    T3=c L^3+d v(s)^2 R,   c d nonzero,

with L of catalecticant rank at most two and L,R,v(s) independent,
cannot satisfy the original highest identity T3(Kv(z))=0.

Indeed its irreducible cuspidal cubic has a birational parametrization
by the three quintic polars with common factor of degree two.
Unique factorization of the cusp equation then gives precisely (1.1).
No hypothesis on the mean rank is required for this pure kernel lemma.

## 2. A physical polar can have a triple root only at four diagonal points

For finite s the original kernel is

    k(s,z)=-(z-s)^2 q(s,z),

    q(s,z)=(s+1)z^3+(-3s^2-3s-5)z^2
           +(s^3-3s^2+22s)z+s^3-5s^2.

The original tangent-polar nondivisibility appendix proves, with a
complete integer certificate,

    disc_z q=s^2 E8(s),

where E8 has degree eight and is square free over C.
At a finite point s outside {0,2,-6}, the diagonal root of k has
multiplicity exactly two. A root of multiplicity at least three
elsewhere would be a triple root of q. Such a root makes the
discriminant vanish to order at least two in every parameter
direction, contrary to square freeness of E8 when s is nonzero.
The source value s=-1 causes no exception: q(-1,z) has a simple
root at target infinity and two distinct finite roots.

At the remaining source points the exact polars are

    k(0,z)=z^4(5-z),
    k(2,z)=-(z-2)^3(3z^2-17z+6),
    k(-6,z)=(z+6)^3(5z^2+65z+66).

The residual quadratics have nonzero discriminants 217 and 2905.
At source infinity, in target homogeneous coordinates (xi,eta),

    k(infinity;xi,eta)=-xi^4(xi+eta).

Therefore a triple root of a physical polar occurs only for

    s in {0,2,-6,infinity},

and that root is the source point s itself. This includes roots at
target infinity and all multiplicities.

If (1.1) held, a would consequently be the linear form vanishing
at that source point.

## 3. The entire companion pencil has catalecticant rank three

For a finite exceptional s choose the complementary linear form
xi, which is 1 in the finite target chart. The independent b in
(1.1) has the form alpha(z-s)+beta, with beta nonzero. Hence,
after a nonzero rescaling, its polar is

    k(s,z)/(z-s)+t k(s,z),                            (3.1)

where t is arbitrary.

Use the original integer inverse matrix S=3200 K^(-1):

    S=[[25,-25,0,100,80,-2800],
       [-25,25,0,-100,-80,-400],
       [0,0,0,0,640,3200],
       [100,-100,0,0,0,0],
       [80,-80,640,0,-6912,-34560],
       [-2800,-400,3200,0,-34560,-172800]].

Let Y be S times the ascending coefficient vector of k(s,z)/(z-s),
padded to six entries. The physical vectors in (3.1) therefore
have the form Y+t' v(s), up to a common nonzero scalar.

For any such vector, take successive row differences
row_(i+1)-s row_i in its 4-by-3 catalecticant matrix. These differences
are independent of t'. They form the 3-by-3 Hankel matrix of

    Z_i=Y_(i+1)-s Y_i,  0<=i<=4.

The exact data are:

| s | Z_0,Z_1,Z_2,Z_3,Z_4 | determinant of (Z_(i+j))_(0<=i,j<=2) |
|---|---|---:|
| 0 | -420,-640,0,6912,34560 | 5910036480 |
| 2 | 720,-2400,-7760,-20384,-53952 | 21064110080 |
| -6 | -30000,39200,-56400,108000,-1425600 | -169705152000000 |

Each determinant is nonzero. Since the row-difference matrix is
obtained by a linear operation on Cat(Y+t'v(s)), that catalecticant
has rank at least three for every complex t'.

At source infinity the complementary linear form is eta.
The companion polar k(infinity) eta/xi has finite-z coefficients

    (0,-1,-1,0,0,0),

so its physical vector, in the same S scaling, is

    Y=(25,-25,0,100,-560,-2800).

The whole pencil is Y+t'e5. The first three rows of its catalecticant
are independent of t', and their determinant is exactly

    100000.

Thus every independent companion at infinity also has rank three.

All four possibilities contradict rank Cat(L)<=2. This proves (1.1).

## 4. Exact certificate and scope

The following files reconstruct the original K and S, check
S K=3200 I, divide the actual physical polars by their diagonal
linear factors, and compute all four displayed determinants using
BigInt arithmetic:

- notes/2026-11-14-reverse-cusp-secant-companion-verify.js
- notes/2026-11-14-reverse-cusp-secant-companion-certificate.json

The square-free discriminant and the absence of any other triple
physical-polar root use
R150-appendix-original-physical-tangent-polars-never-square-divide.md.
The previous complementary cusp placement is in
R150-appendix-no-secant-cuspidal-companion-and-outer-mean-rank-drop-exclusion.md.

The present statement is about the fixed original K and actual secant
or tangent vectors. It is not a classification of all plane cusps,
all low-rank means, or all original critical points.
