# R150 appendix — rank-one inside means cannot have an exact double mean block in a common four-space

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Section and conclusion

Assume the original complete critical equations,

    rank Cat(y)=1, ess(T3)=W, dim W=3, y in W,

and that the minimal common support E of y,H,V has dimension
four. Its physical divisor g has length four. Indeed if H or V
has essential dimension four, its exact apolar divisor gives E;
otherwise their two divisors have total length at most six,
and physical-jet independence in E forces their union to have
length at most four. Adding the single physical mean point
and using minimality gives the same conclusion.

Let s be the mean point. This note proves:

**Theorem.** The multiplicity of s in g cannot be one or two.
In particular the entire exact-double-mean-block section is empty.

The multiplicities three and four remain separate cases in
this note. No general rank-one conclusion is assumed.

## 2. Contraction and the exact double-block normal form

Let lambda span ann(W) in E*. Since lambda(y)=0, contraction
of T3 gives

    V lambda=y(H lambda).

For a rank-one physical mean, yz is Hankel precisely when
z lies in its physical tangent two-space. Thus

    H lambda in span(v(s),v'(s)).

It is nonzero: otherwise lambda would annihilate the essential
supports of all y,H,V, contrary to the minimality of E.

If s were simple in g, lambda would kill its mean block.
On every other physical block the two contractions have to
vanish, since their supports lie at s. The exact local
Frobenius representation then makes lambda vanish on all E,
a contradiction. Thus multiplicity one is impossible.

Now suppose g=2s+R, with R disjoint of length two.
The same blockwise argument makes lambda vanish on R and
have exact order one at s. Both H and V have exact length
two at s. Choose the value y as local physical representative
and a genuine first jet u with lambda(u)=1. Then

    W=Cy+E_R,
    H_D=a y^2+2beta yu,
    V_D=c0 y^3+3beta y^2u, beta!=0.                (2.1)

The equality of the two top coefficients follows directly
from Vlambda=yHlambda. Put

    kappa=1-6a+4c0.

The complete third tensor is

    T3=kappa y^3-6yH_R+4V_R.                       (2.2)

The nonzero beta terms in the actual H,V have canceled in
T3; they remain in both complete low gradients below.

A double complementary R is impossible by the original
double-block highest-identity results. For kappa=0 use the
zero-cube double-block theorem. For nonzero kappa a cubic
image is excluded by the tangent two-jet cubic theorem;
in a conic factorization the physical value coordinate is
a tangent line, which the physical first-jet conic theorem
forbids. The argument includes zero top V_R coefficient:
factorization makes it beta_A h_1, and h_1=0 would reduce
essential dimension to two.

Hence only R=r+t with r!=t remains. Write its physical
values as X,Z and put

    H_R=hX^2+kZ^2, V_R=vX^3+wZ^3.

Their union support is exactly R; individual coefficients
may be zero.

## 3. The complete original four-dimensional low blocks

Use the basis (y,u,X,Z). Physical value-tangent isotropy gives

    K_E=[[0,0,l1,l2],
         [0,g0,n1,n2],
         [l1,n1,0,g],
         [l2,n2,g,0]],

where g0=K(u,u), l_i=K(y,R_i), n_i=K(u,R_i), and g=K(X,Z).
The original F=K(y,y)/2 is zero. Set d=1-2a.

The exact normalized mean gradient components are

    Gamma_y=-2kappa(h l1^2+k l2^2)+4hk g^2,
    Gamma_u=0,

    Gamma_X=8hk g l2+4d v l1^2
                  -16beta v l1 n1-8v k g^2,
    Gamma_Z=8hk g l1+4d w l2^2
                  -16beta w l2 n2-8w h g^2.        (3.1)

The original second-gradient quadric N=T3_(Ky)+4HKH has entries

    N_yy=4beta^2 g0, N_yu=N_uu=0,
    N_yR=-2d(H_R l)^T+4beta(H_R n)^T,
    N_uR=4beta(H_R l)^T,
    N_RR=4(V_R)_l+4H_R G_R H_R,                    (3.2)

with G_R=[[0,g],[g,0]]. In particular,

    lambda^T N lambda=0,
    N lambda=4beta H_R l.                          (3.3)

The supplied BigInt reconstruction checks all twenty components
of these two original gradients and the coefficient-twenty
identity used in section 4. It retains (2.1) throughout.

A useful consequence used repeatedly is that if

    g=l1=l2=0,

then the complete second quadric factors exactly as

    N=4beta y(beta g0 y+2H_R n).                    (3.4)

Its vanishing on the original polars, which form an integral
domain and are nonzero for nonzero directions, forces

    g0=0, H_R n=0.                                 (3.5)

If in addition n=0, every entry of K_E vanishes. This would
be a four-dimensional totally isotropic subspace in a
nondegenerate six-dimensional bilinear space, which is impossible.

## 4. Zero or one residual third coefficient

If v=w=0, essential dimension and the highest identity force
kappa,h,k all nonzero, and the image lies on the conic

    kappa Y^2-6hX^2-6kZ^2=0.

Evaluation at the two complementary sources gives

    kappa l1^2=6k g^2, kappa l2^2=6h g^2.

Their combination with Gamma_y=0 is -20hk g^2=0.
Thus g=l1=l2=0. Since H_R is invertible, (3.5) gives n=0,
the contradiction just described.

Next take v!=0,w=0 after a possible interchange.
Exact union support forces k!=0.

If kappa=0 and h=0, (2.2) is the forbidden physical cube /
physical repeated-factor cusp. If kappa=0 and h!=0, it is
an irreducible cubic with an ordinary node at [1:0:0].
Its normalization has common divisor degree two, and both
residual physical coordinates X,Z vanish at both node
preimages. The original two physical polars would therefore
share at least four factors, contradicting their universal
degree-three gcd bound.

For kappa!=0 and h=0, the cubic
kappa Y^3-6kYZ^2+4vX^3 is smooth and cannot be rationally
parameterized. Thus only kappa hkv!=0 remains.

The cubic is irreducible: eliminating any prospective linear
factor involving Z leaves the nonzero X^3 coefficient;
a factor involving only Y,X leaves its nonzero YZ^2 term.
Therefore the physical map is the cubic normalization.

The Z component of (3.1) gives g l1=0.
If g=0, the highest identity at X gives l1=0, and Gamma_y
then gives l2=0. Equation (3.5), with H_R invertible, gives
n=0, impossible.

If g!=0, then l1=0. The mean-gradient and highest equations
at Z give respectively

    kappa l2^2=2h g^2,
    kappa l2^3-6h l2 g^2+4v g^3=0.

Hence

    l2=vg/h, kappa=2h^3/v^2.

The physical source Z maps without a basepoint to the
ordinary node [v/h:1:0]. The line Z=0 is transverse to both
branches: in the chart X=1 its tangent cone is

    (6h^2/v)(Y-v/h)^2-(6kv/h)Z^2.

The pullback of this line on either normalization branch
has order one. But the physical value polar of Z has
self order at least two, and the nonzero X coordinate g
prevents a basepoint cancellation. This contradiction
excludes the final one-coefficient case.

## 5. Two nonzero residual third coefficients and nonzero kappa

Suppose now v,w,kappa are all nonzero.
The pure original conic theorem forces g=0 if the image is
a conic. The pure cubic contact argument forces g=0 if
the image is an irreducible cubic. Both have exactly the
hypotheses (2.2) with two distinct physical values and
nonzero kappa,v,w; they do not assume a mean rank.

Evaluating the highest identity at X,Z gives l1=l2=0.
Equation (3.5) then gives g0=0 and H_R n=0.

If H_R is invertible, n=0 and the contradiction is immediate.
If H_R has rank one, say h!=0,k=0, then n1=0.
At the mean source s, the polar of y has order at least two,
and the polar of X also has order at least two because
l1=n1=0. If n2 were nonzero, the polar of Z would have
exact order one. The term 4w p_Z^3 would then be the
unique term of order three in the highest identity;
all other terms would have order at least six.
Thus n2=0 as well. The other rank-one case is symmetric.

Finally if H_R=0, the third tensor is the smooth Fermat-type
cubic kappa y^3+4vX^3+4wZ^3, impossible for a rational
physical image. Every rank possibility is excluded.

## 6. Two nonzero residual third coefficients and zero kappa

Let v,w!=0 and kappa=0.
If H_R has rank zero, essential dimension is at most two.
If it has rank one, (2.2) is the prohibited physical cusp.
Hence hk!=0.

The y component of (3.1) gives g=0.
If l=0, (3.5) and invertibility of H_R give n=0,
again impossible.

Suppose l!=0. By (3.3), lambda is a smooth point of the
original quadric N=0. The length-four physical projection
is a nondegenerate birational quartic or quintic, with at
most one simple basepoint. Projection of that curve from
the smooth quadric point lambda is generically one-to-one:
a line through lambda has at most one other quadric point.
The curve cannot lie in a ruling line or in the tangent
plane because it is nondegenerate.

Thus its projection to W is birational. The third polynomial

    -6Y(hX^2+kZ^2)+4(vX^3+wZ^3)

has an ordinary node at P=[1:0:0].
For an irreducible cubic image, the common divisor has
degree two and the two node preimages add two common
zeros of the X,Z coordinates. Their original polars
would share degree at least four.

For an irreducible conic image, write T3=LQ. The conic
must pass through P: otherwise the singular point P
would lie only on the line factor and would be smooth.
Birationality gives common divisor degree three, and
the conic preimage of P adds one common zero of X,Z.
Again their gcd would have degree at least four.

Both violate the universal original bound for two distinct
physical polars. Hence l!=0 is impossible too.

## 7. Completion, exact files, and remaining cases

Every complementary divisor and every zero/nonzero third
coefficient in the exact-double-mean-block form has been
treated. The complete critical section is empty.

- notes/2026-11-14-rank-one-inside-double-mean-block-verify.js
- notes/2026-11-14-rank-one-inside-double-mean-block-certificate.json

The certificate records twenty original low-gradient blocks
and one exact conic consequence in BigInt arithmetic.
All projection-center, normalization, and local-contact
arguments are written in the proof above.

This excludes mean multiplicities one and two in the
rank-one inside common-four-space section. The higher
mean multiplicities remain separate tasks; no natural
Jacobian power or operator conclusion is asserted here.
