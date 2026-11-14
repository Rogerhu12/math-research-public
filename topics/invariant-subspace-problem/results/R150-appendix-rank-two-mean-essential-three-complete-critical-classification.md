# R150 appendix — complete critical classification for rank-two means and essential cubic dimension three

Author: Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

## 1. Complete theorem

Use the fixed original six-mode matrix K and the original physical
Hankel tensors y,H,V. Let

    T3=y^3-6yH+4V.

Assume

    rank Cat(y)=2, ess(T3)=W, dim W=3.

Then the original complete critical equations hold if and only if

    y,H,V are supported on W_+ or W_-,
    Q_+ divides T3|W_+ or Q_- divides T3|W_-, respectively.       (1.1)

Here W_+,W_- are the already classified physical totally isotropic
three-spaces associated to the roots of

    P_+(z)=z^3-5z^2+(32/5)z-8/5,
    P_-(z)=z^3+27z^2+(864/5)z+864/5,

and Q_+,Q_- are the respective nondegenerate physical conic
equations. Divisibility is in the symmetric algebra of that space.

In particular all three original matched first Bell cubics vanish
on this entire rank-two-mean, essential-dimension-three class.

The last new step proved below is exclusion of the remaining
full-four-dimensional third-moment conic section. Together with
the completed low-third-moment classification, this closes the
whole stated class. No rank-one mean, higher essential cubic
dimension, natural Jacobian power, or operator inverse is being
included in this theorem.

## 2. The exact remaining four-dimensional section

The common-support bound and maximal-five-jet exclusion show
that every hypothetical critical point in this class has common
support dimension at most four. The outside-mean section has
already been excluded for all third-moment ranks.

When ess(V)<=3, the complete necessary and sufficient criterion
is already (1.1), by

R150-appendix-rank-two-mean-essential-V-at-most-three-complete-critical-classification.md.

It therefore remains only to exclude y in W and ess(V)=4.
The doubled-support theorem gives the exact disjoint decomposition

    E=E_(D+R), deg D=deg R=2, D and R disjoint,
    W=Cy+E_R,

where D is the exact mean divisor. The complete double-R,
zero-cube, and cubic-projection exclusions reduce the last case to

    R=r+t, r!=t, with physical values X,Z,
    T3=kappa y^3-6y(hX^2+kZ^2)+4(vX^3+wZ^3),
    kappa v w != 0,

and the projected image is a nondegenerate conic.

The actual mean blocks, which remain present in the low gradients,
are exactly the following.

For a reduced mean, set x=a v(s), z=b v(t), y=x+z, u=x-z:

    H_D=(rho/2)(y^2+u^2),
    V_D=(rho/4)(y^3+3yu^2),
    rho!=0, kappa=1-2rho!=0.

For a double mean y=a u0+b u1, b!=0, put u=u0:

    H_D=eta u^2,
    V_D=(3eta/2)y u^2,
    eta!=0, kappa=1.

The remaining parts are H_R=hX^2+kZ^2 and V_R=vX^3+wZ^3.

## 3. Original conic geometry forces the complementary pairings to vanish

The new pure original-kernel theorem

R150-appendix-two-physical-value-conic-companions-force-orthogonality.md

applies exactly to the last form in section 2. It gives

    g=K(X,Z)=0.

Its proof uses the complete conic factorization, the degree-two
physical covering forced by hypothetical nonorthogonality, and
two explicit degree-eight eliminants with an exact coprimality
certificate. It does not assume either low gradient.

Let

    l_i=K(y,R_i), n_i=K(u,R_i), (R_1,R_2)=(X,Z),
    F=K(y,y)/2.

At the physical source X, the highest identity now reads
kappa l_1^3=0. The source Z similarly gives kappa l_2^3=0.
Thus

    g=l_1=l_2=0.                                   (3.1)

## 4. Complete low gradients eliminate the remaining configuration

Let Gamma denote the complete normalized mean gradient:

    Gamma=(F^2-2b+2tau2)y-4FHp+8HKHp
              +4V(p,p,.)-8V:(KHK),

    p=Ky, b=p^T H p, tau2=tr((KH)^2).

For a reduced mean the exact full block identity already
reconstructed in

R150-appendix-rank-two-inside-zero-cube-reduced-complement-is-empty.md

is

    Gamma_y=kappa^2F^2
          -2kappa l^T H_R l+2tr((G_R H_R)^2),

where G_R is the original K restriction to R. By (3.1),

    Gamma_y=kappa^2 F^2.

The coefficient kappa is nonzero, so complete criticality gives F=0.

For completeness, in the double-mean case the same needed
component can be computed directly after (3.1), retaining eta.
Here K(y,u)=K(u,u)=0 and H_D=eta u^2, so Hp=0 and b=0.
Put d=n^T H_R n. Then

    tau2=2eta d,
    [V:(KHK)]_y=(eta/2)d.

The other mean-gradient terms have zero y component.
Consequently

    Gamma_y=F^2+4eta d-4eta d=F^2,

so F=0 in this case as well. The cancellation explicitly
retains the mean-block contribution; it is not a replacement
by a three-dimensional second or third moment.

We have now shown

    F=g=l_1=l_2=0.                                 (4.1)

In the basis (y,u,X,Z), the only possibly nonzero entries of K|E
are n_1,n_2. The y row vanishes, and K(u,u)=0 in both mean types.

Let a_u be the nonzero u^2 coefficient of H_D: it is rho/2
or eta. Since p=Ky annihilates E, the terms involving Hp and
V(p,p,.) vanish. The first term of Gamma lies in Cy, and the
mean part of V has no complementary X or Z component.
The remaining exact restriction is

    (KHK)|span(X,Z)=a_u n n^T.

Thus the two complete mean-gradient components are

    Gamma_X=-8a_u v n_1^2,
    Gamma_Z=-8a_u w n_2^2.

Because a_u,v,w are nonzero, criticality forces n_1=n_2=0.
Therefore K|E is identically zero.

This is impossible for a four-dimensional subspace of a
nondegenerate six-dimensional bilinear space: E contained in
its orthogonal complement would require dim E<=6-dim E=2.
This excludes the final conic section, and hence every
inside/full-four-dimensional-V critical point.

## 5. Completion and sufficiency

The complete exhaustive division is now:

| Third-moment support | Mean position / remaining support | Result |
|---|---|---|
| At least five | Common-support and maximal-five-jet reduction | Empty |
| Four | Mean outside W | Empty |
| Four | Mean inside W, doubled mean support | Empty |
| Four | Mean inside W, double complementary block | Empty |
| Four | Reduced complementary block, zero effective cube | Empty |
| Four | Reduced complementary block, cubic image | Empty |
| Four | Reduced complementary block, nonzero-cube conic | Empty by sections 3–4 |
| At most three | All mean positions and common supports | Exactly (1.1) |

All entries refer to the rank-two-mean, essential-cubic-dimension-three
class stated in section 1. The table does not change those hypotheses.

Necessity of (1.1) follows from the exclusions and the complete
low-V theorem. Sufficiency is the already established full original
criterion on W_+,W_-: the ordinary-moment functional through
degree six is supported on that physical totally isotropic
three-space, and the original highest equation is exactly
Q_+|T3 or Q_-|T3. The original matched directions satisfy the
respective conic equations, so the three matched Bell cubics vanish.

This completes this scalar critical stratum. The preceding
nonsecant-mean theorem and the present rank-two theorem can now
both be used for essential cubic dimension three. The genuine
remaining mean rank in that dimension is one; the zero-mean
case has T3=4V and is excluded by the invertibility of the original
highest Hankel coefficient map.

This is not a global Jacobian-power certificate and does not
supply the still-open estimates needed for the actual operator
or complete the ordinary separable Hilbert invariant-subspace
problem. Work proceeds to those remaining open sections.
