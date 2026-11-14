# R150 appendix — rank-two mean, outside-mean, full four-jet critical section is empty

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Theorem

For the original six-mode system suppose

    rank Cat(y)=2,  ess(T3)=W, dim W=3,
    y not in W,    ess(V)=4.

Then there is no complete original critical point.

The proof uses the original highest identity together with the Hankel
and essential-support structure; it does not impose the extra condition
Ran(H-yy^T/4) subset W. In particular it includes the conormal-defect
cases that are absent in the nonsecant-mean argument.

The rank-two-mean five-jet exclusion already proves that y,H,V have
a common space of dimension at most four. Here ess(V)=4, so that
space is E=ess(V)=W+Cy. The finite Hankel flattening argument gives
a unique exact length-four divisor g with E=E_g; V has a nonzero
top coefficient in every local block, and H is supported on the
same g.

Let D be the unique exact length-two mean divisor. Then D divides g.
Indeed y has representations on D and g, whose union has length
at most six. All jets of a rational normal quintic on a divisor
of length at most six are linearly independent. Uniqueness on this
union forces the exact mean divisor to be contained in g.

## 2. The exact annihilating-direction equations

Define the mean companion u as follows:

    y=a v(s)+b v(t), u=a v(s)-b v(t)       for D=s+t, s!=t;
    y=a v(s)+b v'(s), u=v(s)              for D=2s.

Both mean coefficients needed for the indicated length are nonzero.
The conormal calculation gives U_y^ann=C u and
M(U_y) subset W, where M=H-yy^T/4. Let lambda be the unique
functional on E with

    lambda|_W=0,  lambda(y)=1.

By symmetry, M lambda=c u for some scalar c. Consequently

    H lambda=y/4+c u,                                (2.1)
    V lambda=H/2+(c/2)(yu^T+uy^T),                   (2.2)
    V lambda^2=(1/8+c lambda(u)/2)y+c u.              (2.3)

Equation (2.2) follows by contracting the original tensor
T3=y^3-2 Sym_3(yH)+4V in lambda. No central-trace simplification
has been assumed.

Work in the exact length-four local algebra of g. Because V is
Frobenius, contraction by a local function of order r has exact
remaining jet length n-r in a block of length n, when r<n.
In particular lambda^2 has exact remaining length n-2r.

If lambda is a unit at a mean point, (2.3) forces the multiplicity
of g there to equal its mean multiplicity: the right side is
supported on D, whereas multiplication by a unit preserves the full
local V length.

## 3. If g=D+R with disjoint R of length two

First suppose g has exactly the mean multiplicities at all points
of D. Then g=D+R with R disjoint from D and deg R=2.

On R, (2.1) and (2.2) give

    H_R=2V_R lambda_R,  V_R lambda_R^2=0.

Frobenius nondegeneracy means lambda_R^2=0 in the R algebra.
Thus the part

    C_R=4V_R-6yH_R

is the injective translation of a binary cubic:

    C_R=4 j^tensor3(V_R),   j(v)=v-lambda_R(v)y.

It has essential dimension at most two. It is also annihilated by
lambda. The remaining binary cubic

    C_D=y^3-6yH_D+4V_D

is therefore annihilated by the nonzero lambda_D. Hence

    C_D=k L^3

for some L in E_D, with rank Cat(L)<=2. Essential dimension three
forces k nonzero.

If R consists of two distinct simple points, lambda_R=0. Then T3
is a sum of three nonzero cubes in independent directions. Its plane
cubic is smooth. It cannot be the nonconstant image of P1 under
the three original polars; this is the same regular-differential
argument used in the earlier highest-moment projection classification.

If R is a double point with physical jets v0,v1, write

    V_R=eta0 v0^3+3eta1 v0^2 v1,   eta1 nonzero,
    lambda_R(v0)=0, lambda_R(v1)=rho.

Then

    T3=k L^3+4v0^2[eta0 v0+3eta1(v1-rho y)].

The three directions are independent. This is an irreducible cusp
whose repeated direction is a physical point and whose cubed
direction is a secant/tangent vector. It is excluded by
R150-appendix-no-physical-repeated-factor-secant-cuspidal-companion.md.

Therefore the disjoint D+R case is entirely empty.

## 4. A double-point mean can only leave one fourth-order jet

Suppose D=2s and g has higher multiplicity at s. If lambda(v(s))
were nonzero, section 2 would already put us in the excluded
disjoint case. Thus lambda(v(s))=0.

Since lambda(y)=1 and y has a nonzero first-jet coefficient,
lambda has exact order one at s. Here lambda(u)=0, so (2.3)
has exact mean jet length two. A block of length n gives
n-2=2, forcing n=4 and g=4s.

Use lambda itself as the local parameter. Denote the resulting
physical Taylor jets by v0,v1,v2,v3. Normalize

    lambda(v0)=0, lambda(v1)=1,
    lambda(v2)=lambda(v3)=0, y=a v0+v1.

Let the V functional be eta_j on the j-th local power.
Equation (2.3) gives

    eta3=1/8, eta2=a/8+c.

Equation (2.2) determines the complete H. Direct substitution yields

    T3=v0^2[
         (a^3-12a eta1+12a^2 c+4eta0)v0
         +(-3a/2+12c)v2+(3/2)v3].                   (4.1)

Its essential dimension is at most two, contradicting dim W=3.
The supplied BigInt certificate checks (4.1) from the complete H,V,
including every c term. This eliminates every double-point mean.

## 5. A reduced mean with excess multiplicity at one point

Now D consists of two different points. Excess multiplicity is
possible only at a point where lambda vanishes. It cannot vanish
at both, since lambda(y)=1.

Write the higher-multiplicity point as v0 and normalize the other
physical representative w by lambda(w)=1. Then

    y=a v0+w,  u=a v0-w,  a nonzero,
    lambda(u)=-1.

The point w has multiplicity exactly one. Equations (2.1)-(2.3)
fix its H and V coefficients as

    H_w=(1/4-c)w^2,
    V_w=(1/8-3c/2)w^3.                              (5.1)

The local V coefficient is nonzero by exactness of g. There are
only two possible multiplicities at v0: two or three.

### 5.1 A double point and one additional simple point

Here g=2s+t+r with all three points distinct and w=v(t).
At the double block write

    lambda(v0)=0, lambda(v1)=rho,
    V_s=eta0 v0^3+3eta1 v0^2 v1, eta1 nonzero.

Since lambda_s^2=0, (2.3) forces c=-1/4. At the other simple
point z=v(r), lambda vanishes and H has no contribution; write
its nonzero V coefficient as kappa.

The exact third tensor is

    T3=v0^2[
         12eta1(v1-rho w)
         +(4eta0-2a^3-12a eta1 rho)v0]
         +4kappa z^3.                               (5.2)

This is an irreducible cusp with a physical cubed direction z and
a different physical repeated direction v0. The original
no-secant-cuspidal-companion lemma excludes it.

### 5.2 A triple point, lambda of order one

Here g=3s+t. Use lambda as the local parameter at s, so its values
on v0,v1,v2 are 0,1,0. Write

    V_s=eta0 v0^3+3eta1 v0^2 v1
            +3eta2(v0^2 v2+v0 v1^2), eta2 nonzero.

Equation (2.3) gives

    eta2=a(1+4c)/8.

A direct complete expansion gives

    T3=12eta2 v0[
          (w-v1)^2+v0 v2
          +(2a-eta1/eta2)v0(w-v1)
          +B v0^2],                                (5.3)

where

    B=[a^3(1+12c)-12a eta1+4eta0]/(12eta2).

The original physical polar of v0 is a nonzero polynomial.
The highest identity thus forces the displayed quadratic factor
to vanish on all original polars. That is the forbidden relation

    p0 p2+(p_w-p1)^2+A p0(p_w-p1)+B p0^2=0

from R150-appendix-no-physical-shifted-tangent-conic-companion.md.
The first jet v1 is genuine, w is a different physical point,
and the theorem includes all nonzero rescalings and infinity.

### 5.3 A triple point, lambda of order at least two

In a local parameter write lambda= rho epsilon^2, allowing rho=0.
Then lambda^2=0 and (2.3) again forces c=-1/4. With the same
notation for V_s, the complete expansion is

    T3=12eta2 v0[
          v1^2+v0(v2-rho w)
          +(eta1/eta2)v0 v1+B v0^2],                 (5.4)

where

    B=[4eta0-2a^3-12a eta2 rho]/(12eta2).

The highest identity would force p0 to divide p1^2, impossible by
R150-appendix-original-physical-tangent-polars-never-square-divide.md.

The two orders in sections 5.2 and 5.3 exhaust the triple block.
Together with section 5.1, all reduced-mean excess-multiplicity cases
are excluded.

## 6. Conclusion, exact certificate, and next scope

Every divisor configuration has been treated: exact disjoint
D+R, a double mean with a fourth-order jet, and a reduced mean with
a double or triple block. Therefore the stated rank-two-mean,
outside-mean, ess(V)=4 section is empty.

The four nontrivial local expansions (4.1), (5.2), (5.3), and (5.4)
are checked over an integer polynomial ring after multiplying by
eight:

- notes/2026-11-14-rank-two-mean-full-four-jet-outside-exclusion-verify.js
- notes/2026-11-14-rank-two-mean-full-four-jet-outside-exclusion-certificate.json

The proof depends on the common-support bound in
R150-appendix-rank-two-mean-maximal-five-jet-section-is-empty.md
and the three original conic/cusp kernel exclusions explicitly cited
above. No finite-field sampling is used to infer the classification.

The remaining rank-two-mean work includes the inside-mean
ess(V)=4 section and the ess(V)<=3 cases. This result does not
supply a global Jacobian natural-power certificate or complete the
ordinary Hilbert ISP.
