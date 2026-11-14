# R150 appendix — zero effective cube coefficient with two reduced complementary points is empty

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Original section and conclusion

Assume the original complete critical equations, rank Cat(y)=2,
ess(T3)=W of dimension three, y in W, and ess(V)=4.
The already proved inside-support reduction leaves

    g=D+R, deg D=deg R=2, D and R disjoint, W=Cy+E_R.

In this note both D and R are reduced. Normalize the two mean
directions as x=a v(s), z=b v(t), with a,b nonzero, and put

    y=x+z, u=x-z.

Let X,Z be the two complementary physical values, at two other
distinct points. The exact tensors are

    H=rho(x^2+z^2)+hX^2+kZ^2,
    V=rho(x^3+z^3)+vX^3+wZ^3,

where rho,v,w are nonzero. Their ordinary third tensor is

    T3=kappa y^3-6y(hX^2+kZ^2)+4(vX^3+wZ^3),
    kappa=1-2rho.

**Theorem.** The entire kappa=0 section is empty.

The proof retains both mean-block contributions in H,V. It does
not import the earlier reduced-four-point Gram-rank theorem:
that theorem had additional outside-mean hypotheses not present
here.

## 2. Complete original low-gradient block identities

Use the basis (y,u,X,Z). The physical isotropy of x,z gives

    K|E = [[2F,0,l^T],[0,-2F,n^T],[l,n,G_R]],

    G_R=[[0,g],[g,0]],  H_R=diag(h,k),
    V_R=vX^3+wZ^3.

Here l=K(y,(X,Z)), n=K(u,(X,Z)), and F=K(x,z).
The exact mean blocks are

    H_D=(rho/2)(y^2+u^2),
    V_D=(rho/4)(y^3+3yu^2).

Let Gamma be the normalized original first gradient

    Gamma=(F^2-2b+2tau2)y-4FHp+8HKHp
             +4V(p,p,.)-8V:(KHK), p=Ky,

where b=p^T H p and tau2=tr((KH)^2).
Set b_R=l^T H_R l and tau_R=tr((G_R H_R)^2).
Direct contraction gives the exact blocks

    Gamma_y=kappa^2 F^2-2kappa b_R+2tau_R,
    Gamma_u=0,

    Gamma_R=-4kappa F H_R l+8H_R G_R H_R l
          +4(1-rho)V_R(l,l,.)-4rho V_R(n,n,.)
          -8V_R:(G_R H_R G_R).                    (2.1)

These identities hold before specializing kappa or any pairings.

The original second-gradient quadric is

    N=T3_p-F T2+4HKH, T2=y^2-2H.

Its exact block matrix is

    N_yy=(1-rho)kappa F,  N_yu=0,
    N_uu=rho kappa F,
    N_yR=-2(1-rho)(H_R l)^T,
    N_uR=2rho(H_R n)^T,
    N_RR=-2F H_R+4(V_R)_l+4H_R G_R H_R.            (2.2)

In particular, if lambda annihilates W and lambda(u)=1,

    lambda^T N lambda=rho kappa F,
    N lambda=rho kappa F u+2rho H_R n.             (2.3)

All entries of (2.1)-(2.2) are reconstructed by the accompanying
exact integer polynomial calculation from the complete original
gradient formulas. No contribution from D has been discarded.

## 3. The complementary second moment is invertible

From now on kappa=0, hence rho=1/2.

If h=k=0, T3 only involves X,Z and has essential dimension at
most two. If exactly one coefficient vanishes, for example h=0,
then

    T3=4v X^3+Z^2(4wZ-6k y).

The three displayed directions are independent and v,k are
nonzero. This is the original forbidden cusp with a physical
cubed factor and a physical, hence secant, repeated factor.
The original no-secant-cuspidal-companion theorem excludes its
highest identity. The other case is symmetric. Therefore

    hk is nonzero.                                 (3.1)

The y component in (2.1) now gives

    0=2tau_R=4hk g^2,

so g=0. The R component becomes

    V_R(l,l,.)=V_R(n,n,.).

Since v,w are both nonzero,

    l_1^2=n_1^2,  l_2^2=n_2^2.                     (3.2)

## 4. The actual quadric has a smooth projection center

Suppose n=0. Equation (3.2) gives l=0 as well. Along with g=0,
this says both complementary physical directions X,Z are
orthogonal to all E=span(y,u,X,Z).

Thus the four-dimensional physical projection from E has a
basepoint at each of the two distinct physical support points
corresponding to X and Z. This contradicts the universal theorem
that a length-four physical projection has at most one simple
basepoint. That theorem has no outside-mean or critical-point
hypothesis and is applicable here.

Consequently n is nonzero. By (3.1) and (2.3),

    lambda^T N lambda=0,  N lambda=H_R n != 0.      (4.1)

Hence lambda is a smooth point of the original quadric N=0.

The same universal length-four theorem says that the physical
curve C_E in P(E*) is nondegenerate, birationally parametrized,
and of degree four or five. The original second-gradient identity
puts it on N=0. Projection from the smooth quadric point lambda
is generically one-to-one on C_E: a generic line through lambda
has at most one other intersection with the quadric. C_E is
neither a ruling line nor contained in the tangent plane, because
it is nondegenerate. Therefore projection to W is birational.

## 5. The plane image forces a fourth common factor

In coordinates [Y:X:Z] on W*, the third polynomial is

    T3=-6Y(hX^2+kZ^2)+4(vX^3+wZ^3).

At P=[1:0:0] it has an ordinary node: its tangent cone is
-6(hX^2+kZ^2), which has two distinct linear factors because hk
is nonzero.

If the physical plane image is an irreducible cubic, it is this
nodal cubic. Birationality gives common divisor degree two for
the three original quintics. The node has two normalization
preimages, each a common zero of the residual X,Z coordinates.
Thus the two original physical value polars have a common factor
of degree at least 2+2=4.

If the physical image is an irreducible conic Q, then T3=LQ.
The point P must belong to Q. Otherwise P, being on T3, would
lie only on the line L and would be a smooth point of LQ,
contrary to the node just established. On the smooth conic,
X and Z have their common zero at P. Birationality now gives
a common divisor of degree three for all three quintics, and
the preimage of P gives one further common factor of X,Z.
Again their common factor has degree at least 3+1=4.

Both possibilities contradict the original theorem that distinct
physical value polars have no common fourth-degree factor.
No reducible image or line image remains, since the image is
irreducible and the three polars are independent.

This proves the theorem, including all source points at infinity.

## 6. Exact author record and remaining scope

- notes/2026-11-14-rank-two-reduced-inside-low-blocks-verify.js
- notes/2026-11-14-rank-two-reduced-inside-low-blocks-certificate.json

The calculation reconstructs all four first-gradient components
and all sixteen second-gradient entries with the original
normalizations. Its purpose is to record the exact algebra used
in section 2.

Together with the physical-double-block exclusions, this removes
every zero-kappa branch in the inside/full-four-jet section.
The remaining reduced complementary blocks have kappa nonzero;
double means also have effective coefficient one and remain
subject to their own complete low-gradient formulas. No global
Jacobian-power certificate, operator inverse, or ordinary ISP
conclusion is asserted here.
