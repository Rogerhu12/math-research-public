# R150 appendix — rank-one means with a common three-dimensional support

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Complete common-space criterion

Let y,H,V be the original physical Hankel tensors, let

    T3=y^3-6yH+4V,

and assume

    rank Cat(y)=1, ess(T3)=W, dim W=3,
    y,H,V are all supported on W.

Then

    original complete criticality
      if and only if
    W=W_+ or W_-, and Q_+|T3 or Q_-|T3, respectively.            (1.1)

All three original matched first Bell cubics therefore vanish.

This theorem covers all zero coefficients of H,V, every physical
jet multiplicity, and infinity. It concerns an actual common
three-space; a common four-space is not assumed away.

## 2. The common space is necessarily physical

The rank-one mean is a nonzero multiple of one physical value.
The exact binary apolar representation gives unique physical
divisors for H and V, of lengths at most three because their
essential supports are in W. Their union has length at most six,
and all its jets lie in W. Independence of physical jets of total
length at most six forces that union to have length at most three.

If its length is three, it already spans W. The physical mean
point must belong to that divisor: otherwise it would provide
a fourth independent physical jet in W.

If its length is two, essential dimension three forces the mean
point outside that two-space. Adding that physical point gives
an exact physical divisor of length three spanning W.

Smaller unions cannot give essential dimension three.
Thus W=E_C for an exact physical divisor C of length three,
containing the mean point. We treat its three possible
multiplicity types.

## 3. Three distinct physical points: exact full low blocks

Scale the physical representative at the mean point so that y=X.
Let Y,Z be the other two physical values and write

    H=h0 X^2+hY^2+kZ^2,
    V=v0 X^3+vY^3+wZ^3.

Put

    c=1-6h0+4v0, d=1-2h0.

The complete third tensor is

    T3=cX^3-6X(hY^2+kZ^2)+4(vY^3+wZ^3).            (3.1)

Let l1=K(X,Y), l2=K(X,Z), g=K(Y,Z).
All three diagonal pairings are zero because the directions
are physical values. In particular the original F=K(y,y)/2
is zero.

For the complete original normalized mean gradient Gamma,
direct contraction gives

    Gamma_X=-2c(h l1^2+k l2^2)+4hk g^2,
    Gamma_Y=8hk g l2+4d v l1^2-8v k g^2,
    Gamma_Z=8hk g l1+4d w l2^2-8w h g^2.             (3.2)

The original second-gradient quadric is

    N=T3_(Ky)-F(y^2-2H)+4HKH.

In the basis (X,Y,Z) its entries are exactly

    N_XX=0,
    N_XY=-2d h l1, N_XZ=-2d k l2,
    N_YY=4v l1, N_ZZ=4w l2, N_YZ=4hk g.             (3.3)

The physical highest and second-gradient identities say that
T3 and N vanish on the physical projection.
The accompanying BigInt calculation reconstructs all three
components of (3.2), all nine entries of (3.3), and the
coefficient-twenty identity used below.

We prove that l1=l2=g=0 in every possible coefficient case.

### 3.1 Both residual third coefficients are nonzero

First suppose v,w,c are all nonzero. The image is a conic or an
irreducible cubic. For a conic, the pure original-kernel theorem

R150-appendix-two-physical-value-conic-companions-force-orthogonality.md

applied to the physical pair Y,Z gives g=0.

For a cubic, the pure contact argument in section 2 of

R150-appendix-rank-two-inside-four-jet-cubic-projection-is-empty.md

has exactly the hypotheses (3.1) with c,v,w nonzero; it uses
neither a fourth support direction nor a mean-rank assumption.
For clarity, if g!=0 the source of Y maps without a basepoint
to Y=0. The restriction cX^3-6kXZ^2+4wZ^3 has either a simple
root, giving a transverse smooth intersection, or a double root,
giving an ordinary node transverse to Y=0 when h!=0.
Both give normalization order one, contrary to the physical
self order at least two. If h=0, the source of Z instead has
the squarefree restriction cX^3+4vY^3 and gives the same
contradiction. Thus g=0 in the cubic case as well.

Evaluating the highest identity at the physical sources Y,Z
now gives c l1^3=c l2^3=0. Hence l1=l2=0.

It remains in this coefficient case to allow c=0.
If h=k=0, essential dimension is at most two.
If exactly one vanishes, (3.1) is the forbidden cusp consisting
of a physical cube plus the square of a different physical
value times an independent direction. This is covered by the
original no-secant cuspidal-companion theorem.
Consequently hk!=0.

Equation (3.2) then gives g=0. Its last two components reduce to

    d v l1^2=d w l2^2=0.

If d!=0 this gives l1=l2=0. If d=0, (3.3) reduces to

    N=4v l1 Y^2+4w l2 Z^2.

A nonzero binary quadratic factors into nonzero linear forms
over C, whose original physical polars are nonzero polynomials
because K is invertible. Their product cannot vanish identically.
Thus the second-gradient identity forces N=0 and again
l1=l2=0.

### 3.2 Exactly one residual third coefficient is nonzero

Interchange Y,Z if necessary and take v!=0,w=0.
Essential dimension three requires k!=0.

If c=0 and h=0, (3.1) is again the prohibited physical cusp.
If c=0 and h!=0, it is irreducible: as a polynomial linear in X
its coefficients hY^2+kZ^2 and Y^3 are coprime.
It has an ordinary node at [1:0:0].
The physical map to this cubic is its normalization, with
common divisor degree two. The two physical coordinates Y,Z
vanish at both node preimages, so their original polars have
a common divisor of degree at least four. This contradicts
the universal original two-physical-polar gcd bound.
Thus c cannot be zero here.

If h=0 with c!=0, the cubic cX^3-6kXZ^2+4vY^3 is smooth:
its Y derivative forces Y=0 at any singular point, and the
remaining two derivatives then force X=Z=0.
A smooth plane cubic cannot be rationally parametrized, so
this case is impossible. Therefore hkc!=0.

The cubic (3.1) is now irreducible. A prospective line with
nonzero Z coefficient can be eliminated by setting Z=aX+bY;
the coefficient 4v of Y^3 remains nonzero. A line involving
only X,Y would set X=tY, leaving the nonzero term -6ktYZ^2
unless t=0, which is excluded by 4vY^3. Coordinate lines are
also excluded directly.

An irreducible cubic has no nonzero quadratic relation, so
N=0. Equation (3.3) gives g=0 and l1=0. Equation (3.2) then
gives -2ck l2^2=0, hence l2=0.

### 3.3 Both residual third coefficients vanish

Now v=w=0. Essential dimension requires hk!=0.
If c=0, T3 is a product of three linear forms and cannot
vanish on a nondegenerate irreducible physical image.
Hence c!=0, and the image must be the nondegenerate conic

    cX^2-6hY^2-6kZ^2=0.

At the sources Y,Z respectively this gives

    c l1^2=6k g^2, c l2^2=6h g^2.

Substitution in Gamma_X=0 yields -20hk g^2=0.
Thus g=l1=l2=0.

Every reduced-support case has now been treated.
Its whole three-space is totally isotropic. The original
physical length-three isotropic classification identifies it
as W_+ or W_-.

## 4. A double point and a different simple point

Let X be the physical value at the double point s, Y its
genuine first jet, and Z the value at a different point t.
The physical tensors are

    H=h0X^2+2h1XY+h2Z^2,
    V=v0X^3+3v1X^2Y+v2Z^3.

The rank-one mean is at one of the two physical values.

### 4.1 Mean at the double point

Scale X and its jet so that y=X. Put

    c=1-6h0+4v0, e=12(v1-h1).

Then

    T3=cX^3+eX^2Y-6h2XZ^2+4v2Z^3.                 (4.1)

Write k0=K(X,Z), ell=K(Y,Z), g0=K(Y,Y).
The physical identities give K(X,X)=K(X,Y)=0.

If k0!=0, evaluation at s first gives v2=0.
After division by the nonzero physical polynomial p_X,
the highest identity becomes

    c p_X^2+e p_X p_Y-6h2 p_Z^2=0.

Its value at s gives h2=0. The third tensor then has at most
two essential directions, a contradiction. Thus k0=0.

If ell!=0, the polar p_Z has exact order one at s.
Let m>=2 be the self order of p_X; the genuine first-jet
polar p_Y has order m-1.
In (4.1) the term 4v2 p_Z^3 is the unique possible term
of order three, so v2=0.
In the divided quadratic identity, p_Z^2 has exact order
two while the other terms have orders at least three.
Therefore h2=0, again reducing the essential dimension.
Hence ell=0.

Now p=Ky annihilates the whole common space and F=0.
The original second gradient is exactly

    N=4HKH=4g0 h1^2 X^2.

If g0!=0 it forces h1=0. Essential dimension three in (4.1)
then requires e=12v1!=0. But g0!=0 gives the exact self
orders ord p_X=2 and ord p_Y=1, while ell=k0=0 gives
ord p_Z>=2. The term e p_X^2 p_Y has unique order five;
all other terms have order at least six. This is impossible.

Thus g0=0. The common 2+1 jet space would be totally
isotropic, contrary to the original isotropic length-three
classification. No mean at the double point remains.

### 4.2 Mean at the simple point

Scale Z so that y=Z. The third tensor is

    T3=cZ^3-6Z(h0X^2+2h1XY)+4(v0X^3+3v1X^2Y).

For c=0 the zero-cube physical-double-block theorem applies
without any assumption on v1 and excludes it.

For c!=0 an irreducible cubic image is excluded by the
physical tangent two-jet cubic-companion theorem.
In the conic alternative, write its linear complementary
factor as Z-A. The missing Y^3 coefficient forces A=aX.
The X^2Y coefficient then gives v1=a h1.

If h1=0, also v1=0 and the essential dimension is at most two.
Otherwise the conic factor is

    cZ^2+caXZ+(ca^2-6h0)X^2-12h1XY.

Its physical value coordinate X=0 is a tangent line.
The common space contains the complete genuine tangent
block X,Y, so the original no-conic-tangent-coordinate
theorem excludes it.

Thus the entire 2+1 support type is empty.

## 5. One triple point

Let X,Y,Z be the value, first jet, and Taylor second jet
at the same source. The mean is a nonzero physical value;
scale it to y=X. The physical forms are

    H=h0X^2+2h1XY+h2(2XZ+Y^2),
    V=v0X^3+3v1X^2Y+3v2(X^2Z+XY^2).

Their third tensor has the exact shape

    T3=X(cX^2+dXY+eXZ+fY^2).

Essential dimension three forces e and f nonzero:
if e=0 the variable Z is absent; if f=0 the tensor is
X^2 times one linear direction.

The highest identity therefore forces the nondegenerate conic

    cX^2+dXY+eXZ+fY^2=0

on the physical image. Its coordinate X=0 is a tangent line.
The physical first-jet block X,Y is in the space, so the same
universal tangent-coordinate prohibition applies.
This excludes every triple point, including infinity.

## 6. Sufficiency and author record

All effective physical divisors of length three have now
been covered. Only W_+,W_- remain. The already established
isotropic-plane moment criterion applies to the full ordinary
moment functional through degree six, supported on this
space; it has no restriction requiring a nonsecant mean.
It gives both sufficiency and the exact divisibility condition
in (1.1), and the vanishing of the three matched Bell cubics.

Exact author files:

- notes/2026-11-14-rank-one-three-space-low-blocks-verify.js
- notes/2026-11-14-rank-one-three-space-low-blocks-certificate.json

The BigInt calculation checks the complete reduced three-point
gradient blocks and the conic coefficient-twenty identity.
The nonreduced arguments above are written original tensor
and local-contact calculations, not numerical experiments.

The remaining rank-one common four-space and the higher
essential-cubic dimensions continue separately. This common
three-space classification does not assert a global Jacobian
power or an operator inverse.
