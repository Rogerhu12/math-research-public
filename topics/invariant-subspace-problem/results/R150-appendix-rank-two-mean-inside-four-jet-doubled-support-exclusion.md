# R150 appendix — rank-two inside mean: doubled four-jet support is empty

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Statement and the two remaining support forms

Assume the original complete critical equations and

    rank Cat(y)=2, ess(T3)=W, dim W=3,
    y in W, ess(V)=4.

The already proved common-support bound gives a unique exact
length-four physical divisor g supporting y,H,V. Let D be the
unique exact length-two mean divisor, and let u be its companion:

    y=a v(s)+b v(t), u=a v(s)-b v(t)       if s!=t;
    y=a v(s)+b v'(s), u=v(s)              if D=2s.

The required coefficients a,b or b are nonzero. As before, D
divides g by independence of any at most six rational-normal-curve
jets.

**Theorem.** The companion u cannot belong to W. Equivalently the
doubled-support branch g=2D is empty. Every remaining point in the
stated section must instead have

    g=D+R, deg R=2, D and R disjoint,
    W=Cy+E_R,

with the exact tensor normal forms in section 6 below.

This is a necessary reduction, not an assertion that the disjoint
two-block forms contain an original critical point.

## 2. Annihilating direction and support dichotomy

Let lambda span ann(W) in E_g*. The rank-two-mean conormal identity
implies M lambda=c u, where M=H-yy^T/4. Since lambda(y)=0,

    H lambda=c u,
    V lambda=(c/2)(yu^T+uy^T).                       (2.1)

Here c is nonzero: otherwise V lambda=0, contradicting ess(V)=4.
The displayed quadratic has exact rank and physical support D,
both of length two.

If lambda(u) is nonzero, lambda is a unit at every point of D:
for a reduced mean its two values are both nonzero, and for a
double mean its physical value is nonzero. The Frobenius rank
formula for V lambda forces g to have exactly D's multiplicities
there; it also forces lambda to vanish on the complementary
length-two divisor. This is the disjoint D+R case.

If lambda(u)=0, then lambda annihilates all E_D=span(y,u).
Contracting (2.1) again gives V lambda^2=0, hence lambda^2=0 in
the exact g algebra. If a point of D has multiplicity m and g
has multiplicity n, the exact support of V lambda says
ord(lambda)=n-m. Its square being zero gives n>=2m.
Since deg g=4, we obtain g=2D.

Thus u in W is exactly the doubled-support case. We now exclude
both possibilities for D.

## 3. A doubled double mean: g=4s

Use a local physical parameter for which lambda=epsilon^2 on
the length-four algebra. This is possible because lambda has
exact order two; taking the square root of its nonzero unit
factor is a valid local parameter change, also at infinity.
Let v0,v1,v2,v3 be the resulting physical Taylor jets.

Write y=a v0+b v1, b nonzero. Equation (2.1), together with the
Hankel local forms, gives

    H=h0 v0^2+2h1 v0 v1+c(2v0 v2+v1^2),

    V=eta0 v0^3+3eta1 v0^2 v1
        +3ca(v0^2 v2+v0 v1^2)
        +(cb/2)(3v0^2 v3+6v0 v1 v2+v1^3).

The top coefficient cb/2 is nonzero. Direct expansion yields

    T3=6cb v0^2 v3
        +b(b^2-4c)v1^3
        +(3ab^2-12b h1+6ac)v0 v1^2
        +(3a^2b-6b h0-12a h1+12eta1)v0^2 v1
        +(a^3-6a h0+4eta0)v0^3.                     (3.1)

If b(b^2-4c) is nonzero, shift v1 by a multiple of v0 to remove
the v0 v1^2 term from its cube. Equation (3.1) then has form

    T3=k L^3+v0^2 Z, k nonzero,

where L is a genuine first jet plus a physical value, so
rank Cat(L)<=2, and Z has nonzero v3 coefficient. The three
directions are independent. This is the forbidden physical
repeated-factor / secant cubed-factor cusp.

If b(b^2-4c)=0, write the remaining v0 v1^2 coefficient as A.
For A nonzero, the highest identity forces the physical value
polar p0 to divide the square of its genuine first-jet polar p1,
contrary to the tangent-polar theorem. If A=0, then T3=v0^2 Z
has essential dimension at most two, contrary to the hypothesis.
Thus g=4s is impossible.

## 4. Two doubled mean points: g=2s+2t

Let u0,u1 and v0,v1 be physical Taylor jets at two different
points s,t. Choose their local parameters so that lambda has
values 0,1 on each double block. Write

    y=a u0+b v0, u=a u0-b v0, ab nonzero.

Equation (2.1) fixes the first-jet coefficients:

    H=h0 u0^2+2ca u0u1+k0 v0^2-2cb v0v1,
    V=eta0 u0^3+3ca^2 u0^2u1
        +theta0 v0^3-3cb^2 v0^2v1.

Let U,V,Z denote the linear directions u0,v0,v1-u1.
The complete third tensor is

    T3=gamma U V Z+A U^3+B U^2 V+C U V^2+D V^3,      (4.1)

where gamma=12cab is nonzero and

    A=a^3-6a h0+4eta0,
    B=3a^2b-6b h0,
    C=3ab^2-6a k0,
    D=b^3-6b k0+4theta0.

The directions U,V,Z are independent.

### 4.1 The two physical values are orthogonal

Put k=K(u0,v0). At z=s the highest identity gives D k^3=0,
and at z=t it gives A k^3=0. If k were nonzero, A=D=0 and
(4.1) would be the product U V(gamma Z+B U+C V).
All three original polars of these nonzero directions are nonzero
polynomials; their product cannot vanish identically. Therefore

    K(u0,v0)=0,   F=y^T K y/2=0.                    (4.2)

Define d_s=K(u1,v0), d_t=K(u0,v1). These cannot both vanish.
For finite distinct source points, simultaneous vanishing would
give q=q_s=q_t=0 for the original cubic kernel. Away from source
0,-1 this would make its discriminant have a multiple zero,
contrary to the square freeness of E8. Source -1 has three
distinct projective q roots; source 0 has no distinct common
root of q and q_s. At infinity the only orthogonal finite point
is -1 and one cross derivative is nonzero. Thus the same assertion
holds in every local chart. Rescaling a genuine jet or adding
its physical value changes neither this simultaneous-zero question
under (4.2).

### 4.2 The original second-gradient quadric has a smooth center

Use the actual second-gradient tensor

    N=T3_p-F T2+4HKH, p=Ky.

Since lambda annihilates T3 and lambda(y)=lambda(u)=0,
(2.1) and (4.2) give

    N lambda=4c H K u
      =-4c^2 ab(d_s u0+d_t v0).                     (4.3)

This is nonzero because d_s,d_t are not both zero and u0,v0
are independent. Also lambda^T N lambda=0.
Thus [lambda] is a smooth point of the original quadric N=0.

The four-dimensional physical projection from E_g has at most one
simple basepoint and is birational onto a nondegenerate curve of
degree four or five, by the universal length-four projection theorem.
The original second-gradient identity puts this curve on N=0.
In particular N has rank at least three; a quadric of rank at most
two is a union of planes and cannot contain this nondegenerate
irreducible curve.

Projection of a quadric from one of its smooth points is generically
one-to-one: a generic line through that point has only one other
quadric point. The physical curve cannot be a ruling line or lie
in the tangent-plane intersection. Therefore the physical projection
to W is birational as well.

### 4.3 Either plane image contradicts the two-polar gcd bound

The three physical quintics corresponding to U,V,Z have a
nondegenerate irreducible plane image contained in (4.1). Hence its
degree is two or three.

If the image is the irreducible cubic (4.1), its point [0:0:1]
is an ordinary node, with tangent cone gamma UV. Its two
normalization preimages contribute a common divisor of degree two
to the two residual coordinate polars U,V. Birationality makes
the total common factor of the three quintics have degree
5-3=2. Consequently the original two physical value polars
K(u0,v(z)), K(v0,v(z)) have a common factor of degree at least four.

If the image is an irreducible conic, it is the quadratic factor
of (4.1). Its complementary linear factor cannot involve Z,
because the coefficient of Z is gamma UV; otherwise the quadratic
factor would be proportional to UV and reducible. Thus the linear
factor is U or V. The conic contains [0:0:1] as a smooth point.
Its one normalization preimage contributes a common factor of
degree one to the residual U,V coordinates. Birationality now
gives a common factor of degree 5-2=3 for all three quintics,
again giving degree at least four for the two physical value polars.

Both conclusions contradict the original theorem that two different
physical polars have no common factor of degree four. This is
proved, including infinity, in
R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md.

Thus g=2s+2t is impossible. Sections 3 and 4 prove the theorem.

## 5. Exact author record

The following files reconstruct the complete local third tensor
in both doubled-support cases using BigInt polynomial arithmetic:

- notes/2026-11-14-rank-two-mean-inside-doubled-support-verify.js
- notes/2026-11-14-rank-two-mean-inside-doubled-support-certificate.json

The use of the original second gradient in (4.3), its smooth-center
projection, and the two-polar divisor contradiction are the written
geometric proof. The proof retains the original K throughout.

## 6. Exact residual normal forms

Only lambda(u) nonzero remains. In this case lambda vanishes on
R and has kernel Cy on E_D, so

    W=Cy+E_R,  g=D+R, D and R disjoint.

The D part is fixed by (2.1).

For a reduced mean, put x=a v(s), z=b v(t), so y=x+z.
There is a nonzero scalar rho with

    H_D=rho(x^2+z^2),
    V_D=rho(x^3+z^3).

Consequently the complete third tensor is

    T3=(1-2rho)y^3-6yH_R+4V_R.                      (6.1)

The value rho=1/2 is not excluded here.

For a double mean y=a v0+b v1, there is a nonzero h with

    H_D=h v0^2,
    V_D=(3h/2)y v0^2.

Then

    T3=y^3-6yH_R+4V_R.                              (6.2)

In both cases V_R has its nonzero top coefficient(s) on the
exact length-two R. The complete original H and V still include
their displayed D parts. Their low gradients must be computed
with those parts present; the resemblance of (6.1) or (6.2) to an
earlier three-dimensional third tensor does not remove those
terms.

The existence or exclusion of these disjoint two-block residual
forms remains open in this note, as do the ess(V)<=3 cases being
treated separately.
