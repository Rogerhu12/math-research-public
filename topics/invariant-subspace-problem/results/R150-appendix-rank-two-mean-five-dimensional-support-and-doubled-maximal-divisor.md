# R150 appendix — rank-two means have a five-dimensional support bound and a doubled-support maximal case

Author: Astra-ISP-1cf8c51d. Date: 2026-11-13 UTC.

## 1. Statement and remaining case

Use the original six-mode Hankel tensors y,H,V and

    T3=y^3-6yH+4V,   M=H-yy^T/4.

Products in this formula are the corresponding homogeneous polynomials.
Assume

    rank Cat(y)=2,
    ess(T3)=W, dim W=3,

where Cat(y)=(y_(i+j))_(0<=i<=3,0<=j<=2).
Thus y has one unique exact length-two physical divisor D.

If D=s+t consists of two different points, choose physical representatives
so that

    y=a v(s)+b v(t),   a b nonzero,
    u=a v(s)-b v(t).

If D=2s is a double point, write

    y=a v(s)+b v'(s),  b nonzero,   u=v(s).

All statements about u are invariant under its nonzero rescaling, and
the double-point formula uses a local coordinate at infinity when needed.

**Theorem.**

1. Without using criticality, y,H,V have a common supporting vector
   space of dimension at most five. In particular ess(V)<=5.
2. Suppose ess(V)=5 and impose the original highest critical identity
   T3(Kv(z))=0. Then u belongs to W.
3. In this maximal case the common space is the exact jet space of a
   unique length-five physical divisor g, and

       g >= 2D, hence g=2D+r for one point r.

   The point r is allowed to coincide with a point of D. The only
   remaining multiplicity partitions are 5, 4+1, 3+2, and 2+2+1.

The theorem begins the rank-two-mean stratum left open by the
nonsecant-mean classifications. It does not exclude those four maximal
cases, does not classify ess(V)<=4, and does not address a rank-one or
zero mean, ess(T3)>=4, global Jacobian powers, or an operator inverse.

## 2. The one-dimensional conormal defect

Let I2 be the space of quadrics vanishing on the rational normal quintic,
and put

    U_y=span{Qy : r^T Q r belongs to I2}.

A vector z annihilates U_y exactly when yz^T+zy^T is Hankel. For a
rank-two mean the exact annihilator is

    U_y^ann = C u.                                    (2.1)

Here is a direct check including both divisor types. The curve and
the space of Hankel tensors are covariant under a change of parameter
on P1, so one may check the linear-algebra assertion with the two
distinct points at 0 and infinity, or a double point at 0. This changes
coordinates for this assertion only; no substitute for the original
K is used in the critical argument below.

In the first chart y=a e0+b e5. The Hankel equalities on
yz^T+zy^T force z1=z2=z3=z4=0 and a z5+b z0=0, giving (2.1).
In the double chart y=a e0+b e1 with b nonzero. The same equalities
force z1=...=z5=0, giving z proportional to e0. These formulas
transport back to the stated u, and include all points at infinity.

For every original curve quadric the complete difference identity is

    (1/6) q(partial)T3 = -4 M Qy.

Since all second derivatives of T3 lie in W,

    M(U_y) subset W.                                 (2.2)

The following symmetric linear-algebra consequence is useful.

- If u is outside W, (2.2) implies M=M_W+c u^2 with
  M_W in Sym^2 W.
- If u belongs to W, it implies
  M=M_W+u z^T+z u^T for some z.

To verify this, choose a vector-space decomposition containing W and
the line C u. The condition says that all columns indexed by covectors
annihilating u have image in W. Symmetry eliminates the transposed
blocks as well. If u is outside W, only the W-by-W and u-by-u blocks
survive. If u is in W, every block outside W must have its other
index in C u, giving the second formula.

Finally the exact polynomial identity

    V=(1/4)T3+(1/8)y^3+(3/2)yM                       (2.3)

shows that y,H,V have common support in

    E=W+Cy+Cu                if u is outside W,
    E=W+Cy+Cz                if u is in W.

In both cases dim E<=5. This proves part 1.

## 3. The maximal common support is an exact length-five jet space

Suppose ess(V)=5. The constructed E has dimension exactly five and is
the essential support of V. The Hankel flattening of V has rank five:

    rank(V_(i+n))_(0<=i<=5,0<=n<=10)=5.

The finite binary apolar argument used in the earlier length-four
reduction now gives a unique first relation of degree five. More
explicitly, for the degree-fifteen functional Lambda_V, let b_j be its
apolar Hilbert function. We have b_5=5, symmetry b_j=b_(15-j),
and monotonicity after the first nonzero relation. If a is the first
relation degree, b_(a-1)=a=b_(16-a); these inequalities force a=5.
The degree-five relation space is one-dimensional.

Division by its polynomial g and the finite local decomposition give
an exact length-five physical jet representation of V. Every top
local coefficient is nonzero. Its essential image is E, so

    E=E_g.

Both y and u belong to E and span E_D. Thus D divides g: in the
reduced case the two physical vectors separately belong to E_g;
in the double case its physical value and first jet both do.
Equivalently the annihilating quintic of the hyperplane E_g vanishes
on the full divisor D. This uses both y and u, not merely y in E_g.

The same g supports H. Indeed H has all columns in E_g, so the
coefficient vector of g annihilates H, giving all six degree-ten
relations Lambda_H(g z^j)=0. Finite division again gives the common
local representation.

Write

    A_g = direct_sum C[epsilon_i]/(epsilon_i^n_i).

Restriction of degree-five coordinates identifies E* with A_g.
The tensor V is represented by a Frobenius functional Lambda:
V(f1,f2,f3)=Lambda(f1 f2 f3). Its multiplication pairing is
nondegenerate because every top local coefficient is nonzero.
Consequently contraction V ell has matrix rank

    rank(V ell)=sum_i max(n_i-ord_i ell,0),            (3.1)

and its exact local physical support has those same lengths.
Also V ell=0 implies ell=0.

## 4. Excluding the transverse companion u outside W

Assume for contradiction u is outside W. The equality dim E=5
means the classes of y and u are independent modulo W. Hence there
are unique functionals ell0,ell1 in the two-dimensional annihilator
of W with

    ell0(y)=0, ell0(u)=1,
    ell1(y)=1, ell1(u)=0.

Write M=M_W+c u^2. For any ell annihilating W, contraction of T3=0
in that direction gives the exact tensor identity

    V ell=(ell(y)/2)H
          +(y(H ell)^T+(H ell)y^T)/2
          -(ell(y)/4)yy^T.                           (4.1)

Since H ell0=c u, this gives

    V ell0=(c/2)(yu^T+uy^T).                         (4.2)

The scalar c is nonzero; otherwise V ell0=0 would contradict the
essential dimension of V. The right side has rank two and exact
physical support D.

The values of ell0 are units at the support of D. For two distinct
points they are 1/(2a) and -1/(2b); for a double point its value at
the underlying point is 1. Formula (3.1) and (4.2) therefore show that
g has exactly the multiplicities of D at those points. Thus

    g=D+R, deg R=3, D and R disjoint.                 (4.3)

The second functional has H ell1=y/4. Equation (4.1) now simplifies to

    H=2V ell1,   y=8V ell1^2.                        (4.4)

A double-point D is impossible here. Indeed ell1(v(s))=0, so
ell1^2 vanishes on the length-two local algebra of D; (4.4) would
make the nonzero D part of y vanish.

Therefore D=s+t is reduced. The values of ell1 there are
1/(2a),1/(2b), and (4.4) fixes the complete D tensors:

    H_D=(a^2/2)v(s)^2+(b^2/2)v(t)^2,
    V_D=(a^3/2)v(s)^3+(b^3/2)v(t)^3.                 (4.5)

Their contribution y^3-6yH_D+4V_D is identically zero.

On R, (4.4) says ell1^2=0 and H_R=2V_R ell1. Define

    j:E_R -> E_R+Cy,  j(v)=v-ell1(v)y.

This map is injective since y is outside E_R. The exact third tensor is

    T3=4 j^tensor3(V_R),   W=j(E_R).                 (4.6)

Indeed expanding the right side gives 4V_R-12y V_R ell1; all higher
terms vanish because ell1^2=0, and this is exactly
4V_R-6yH_R.

If ell1|_R=0, then T3=4V_R is a nonzero Hankel cubic. This contradicts
the original highest identity: its coefficient map is the invertible
original J3 of
R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md.
Thus ell1|_R is a nonzero square-zero element. A reduced three-point
R has no such element. There are only two cases left.

### 4.1 R is a double point plus a distinct simple point

Let the physical jets be v0,v1 at the double point and w at the
simple point. The square-zero element has values 0,rho,0 with rho
nonzero. The exact V_R polynomial has form

    eta0 v0^3+3 eta1 v0^2 v1+eta2 w^3,
    eta1 eta2 nonzero.

By (4.6),

    T3=4 eta2 w^3
       +12 eta1 v0^2
          (v1-rho y+(eta0/(3eta1))v0).

The three displayed directions are independent. This is an
irreducible cuspidal cubic of the form a physical point cubed plus
a repeated physical point direction squared times an independent
linear direction.

The original highest identity would give a birational cuspidal
parametrization by three quintic polars with an exact common quadratic
factor. Its physical cubed direction w and repeated direction v0
satisfy precisely the pure original-kernel lemma in
R150-appendix-no-secant-cuspidal-companion-and-outer-mean-rank-drop-exclusion.md:
the repeated direction has mean catalecticant rank at most two
(in fact one) and is not parallel to w. That lemma excludes this
configuration, including infinity. Its kernel statement does not
assume a nonsecant mean, so its use here is within its proved scope.

### 4.2 R is one triple point

Use the Taylor physical jets v0,v1,v2 at that point. A nonzero
square-zero element has values 0,0,rho, with rho nonzero. With
eta2 nonzero the exact tensor polynomial is

    V_R=eta0 v0^3+3eta1 v0^2 v1
          +3eta2(v0^2 v2+v0 v1^2).

Equations (4.6) and j(v2)=v2-rho y give

    T3=12eta2 v0[
          v0(v2-rho y)+v1^2
          +(eta1/eta2)v0 v1+(eta0/(3eta2))v0^2].

The nonzero physical polar of v0 is not the zero polynomial.
The highest identity therefore forces its displayed quadratic
factor to vanish on all original physical polars. This is exactly

    p0 pZ+p1^2+c1 p0 p1+c0 p0^2=0,

where p0 is the original value polar, p1 its genuine first-jet
polar, and Z=v2-rho y. It is impossible by
R150-appendix-original-physical-tangent-polars-never-square-divide.md.

All possibilities in (4.3) have been exhausted. The assumption
u outside W is false. This proves part 2.

## 5. The surviving maximal case has g at least 2D

Now u belongs to W. Write

    M=M_W+u z^T+z u^T.

Since ess(V)=5, the classes of y,z are independent modulo W.
Choose ell in ann(W) with ell(y)=0 and ell(z)=1. Then

    H ell=u,
    V ell=(yu^T+uy^T)/2.                             (5.1)

Again this quadratic tensor has rank two and exact physical support D.
Since ell(u)=ell(y)=0, contraction once more gives V ell^2=0.
The Frobenius representation therefore yields

    ell^2=0 in A_g.                                  (5.2)

At a point where D has multiplicity m and g has multiplicity n,
formula (3.1) and the exact support in (5.1) give
ord(ell)=n-m. Equation (5.2) gives 2(n-m)>=n, hence n>=2m.
At points outside D no further lower bound is needed. Therefore

    g>=2D.

Because deg g=5 and deg D=2, g=2D+r with r a single point,
possibly overlapping D. If D is reduced this gives 2+2+1 or 3+2;
if D is double this gives 4+1 or 5. This proves part 3.

## 6. What is and is not closed

The argument proves the common five-dimensional bound and removes
the entire maximal branch with the companion u transverse to W.
It leaves a specific maximal branch with u in W and g=2D+r. Its
four listed multiplicity types require their own complete critical
analysis. The common-space cases with ess(V)<=4, as well as lower
mean rank and higher essential dimension of T3, remain separate.

No numerical sampling is used in this reduction. The only original-form
finite computations invoked are the already published nondegeneracy of
J3, the original no-secant cuspidal-companion lemma, and the tangent
polar nondivisibility lemma. Every use retains their original K and
their full projective, including infinite-point, scope.
