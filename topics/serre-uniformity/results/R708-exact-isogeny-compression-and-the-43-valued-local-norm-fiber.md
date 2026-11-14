# R708: exact isogeny compression and the 43-valued local Norm fiber

Status: proved. The ordinary units and all original markings remain those of
R561, R613, R619, R657 and R701. This result does not compute C, b, m, J or L.

There are two conclusions. First, the original partial q-Robert product has
an exact compression by degree-q isogenies, but it still requires
(q+1)/43 different quotient curves; it does not become one small isogeny
Norm. Second, all recorded distribution Norms, even with the actual c_q,
c_t and pure-p ancestor fixed, admit 43 different p-local values of the
R701 scalar. This ambiguity can preserve the original Gamma and tau
markings and every q-local input. The missing constraint is the embedding
of the actual global ordinary unit, not the choice of a local Norm root.

## 1. Original notation and the local quotient

Keep p=43, K=Q(i), the original q and Weil root, and

    B=K(A[p^2])^mu_42, P=S x T,
    S=<s=1+p>, T=<t=1+21p*i>,
    L=F L_q, M'=L B, M_s=L F_s, F_s=B^T,
    Gamma=<gamma>, pi=gamma-1,
    a=15i/7, a mod p=-4i.

Here pi is the Gamma augmentation operator, not a local field uniformizer.
All unit groups below are written additively after the same O=Z_43[i]
completion and chi-minus projection. The unaveraged operator remains

    Pplus=sum_{j=0}^{43} omegahat^j sigma^j=44 e_chi-minus.

No factor 1/44 is inserted. Write

    Aalpha=Pplus[alpha_F], alpha_F=1+89460 y_F.

The element alpha_F is the original R171 q-principalization, with
(alpha_F)=q_0 and Norm_{F/K}(alpha_F)=-q. It is a unit at p.
The real original y_F and the semilinear projector give

    tau(Aalpha)=Aalpha.                                      (708.1)

Let U_V denote the p-completed semilocal principal-unit group of V in this
character. Removing the prime-to-p residue roots of unity does not change
the completed group. As in R701, put

    Q_s=U_{F_s}/(p U_{F_s}+E_{F_s}),
    xi_alpha=the image of Aalpha in Q_s.

R327 and R377, used in R701, prove that xi_alpha is nonzero. More precisely
Q_s is free of rank one over k[S], and xi_alpha spans its S-socle.
For the original global units, R701 gives

    V_sc=pi^41 D_S c_s-11a pi^40 c_q,
    [V_sc]=(C/a) xi_alpha, D_S=sum_{j=0}^{42} j s^j.          (708.2)

The bracket first descends the Gamma-invariant mod-p p-local vector to
F_s and then takes Q_s. Its scalar eta_p=C/a is in F_43, with

    C=-4i eta_p, L=31-2 eta_p,
    Omega_2=epsilon(2 eta_p-21).

These are relations between the still-unknown actual values; no value is
assigned to them here.

## 2. Surjective local Norms in the marked character

There is a W in U_{M'} with

    N_Gamma N_S N_T W=Aalpha.                               (708.3)

To prove this without an ordinary-unit assumption, first consider the
unique p-adic completions B_p/F_p. The extension is abelian with group
P=S x T. Local reciprocity identifies the full local multiplicative Norm
quotient with P. The action of Delta on this quotient is trivial, since
the pure-p extension B/K is abelian. Its nontrivial chi-minus component
therefore vanishes. After p-completion and the indicated character
projection, the Norm onto F_p is surjective.

The same statement holds on the principal units in this character. A
local valuation and the prime-to-p residue roots have zero chi-minus
completed component: there is only one p-prime, Delta acts trivially on
its valuation, and the residue multiplicative group has order prime to p.
Thus N_P:U_B -> U_F is onto.

The original q-ray extension L_q/K is completely split at p by R191.
Consequently U_{M'} is a direct sum of 43 copies of U_B with Gamma
permuting the components. Its Gamma norm is the sum map onto U_B,
which is onto. Composing these two surjections proves (708.3).

This argument deliberately takes place in local unit groups. It does not
assert that Aalpha, u, y, or any other target has an ordinary global
unit Norm preimage.

## 3. A common-ancestor deformation preserving every displayed Norm

The original common ancestors satisfy the exact identities

    c_s=N_T c_B, c_t=N_S c_B, c_q=N_S N_T c_B,
    N_Gamma c_B=(1-s^11)u_B,
    u_s=N_T u_B, u_t=N_S u_B.                              (708.4)

Fix all the actual pure-p units, c_q, c_t and their markings. For
lambda in Z_43 define the following local units:

    c_B(lambda)=c_B+lambda pi(s-1)W,
    c_s(lambda)=N_T c_B(lambda),
    c_t(lambda)=c_t, c_q(lambda)=c_q.                       (708.5)

These satisfy every identity in (708.4), exactly in the completed
semilocal group. Indeed,

    N_S(s-1)=0, N_Gamma pi=0.

Hence N_S c_B(lambda)=c_t and N_Gamma c_B(lambda) retains the same
Euler factor (1-s^11)u_B. Taking N_T and further norms shows that
the unchanged c_q is still the common norm. There is no change of
the scalar shift s^11, q-Frobenius s^32, or the positive Gamma generator.

Now form the same expression as (708.2) from these local candidates.
Because D_S(s-1)=p-N_S, its difference from the actual expression is

    V_sc(lambda)-V_sc
       =lambda pi^42 (p-N_S)N_T W.                        (708.6)

Modulo p in O[Gamma],

    pi^42=N_Gamma.

This follows directly from (X-1)^42=sum_{j=0}^{42}X^j in characteristic
43; it does not use division by pi or an endpoint hypothesis on m.
Reducing (708.6) modulo p and using (708.3) therefore gives

    V_sc(lambda)-V_sc=-lambda Aalpha modulo p U_{M_s}.

Both sides are Gamma-invariant modulo p, so descent and projection to
Q_s yield the exact ambiguity formula

    [V_sc(lambda)]=[V_sc]-lambda xi_alpha.                 (708.7)

Since xi_alpha is nonzero, the 43 choices lambda modulo 43 produce
43 different scalar values eta_p-lambda. This is the full F_43 set of
values allowed by the real-coefficient condition in R701.

Thus solving the exact displayed Norm equations in the known local field,
even with the true c_q and c_t fixed, cannot by itself identify eta_p.
The R704 embedding matrix correctly evaluates elements once their global
coordinates are supplied; it cannot choose one member of (708.5).

## 4. The ambiguity preserves the original semilinear real marking

The p-local W in (708.3) can be chosen so that the deformation has the
same tau behavior as the original Robert units. Recall

    tau gamma tau^-1=gamma^-1,
    tau s tau^-1=s, tau t tau^-1=t^-1,
    tau pi=-gamma^-1 pi tau.

The original real p^2 and q points, P_2=(i,1-i), and the even CM-invariant
function v give tau(c_B)=sigma^22(c_B) before the chi projection. The
q-norm subgroup contains -i, and -i in the tame p^2 group has the class
sigma^22 modulo mu_42. In the indicated character sigma^22=-1, so

    tau(c_B)=-c_B.                                       (708.8)

The s^11 shift is rational scalar and commutes with tau, so (708.8)
also holds for the correctly oriented mixed ancestor used in (708.4).

Starting with any W from (708.3), replace it by

    W^+=(W+gamma^-1 tau(W))/2.                            (708.9)

This is integral because p is odd. All three norm operators commute with
tau, up to their harmless permutation of factors, and Aalpha is tau-fixed.
Thus (708.3) still holds. Formula (708.9) gives

    tau(W^+)=gamma W^+.

It follows at once that

    tau(pi(s-1)W^+)=-pi(s-1)W^+.

For lambda in Z_43, (708.5) therefore preserves (708.8), including the
semilinear conjugation of O coefficients. The 43-fold ambiguity is not
created by dropping the original real marking or reversing Gamma.

One may regard this deformation as supported at p in the full finite
idele unit group, taking it to be zero in additive notation at every
other finite place. All q-residue tables and every marked q-local phase
then remain unchanged. These are idele units, not asserted principal
ideles or global ordinary units.

The distinction is essential. For genuine ordinary global units satisfying
the same identities, the R561 genus calculation still fixes the scalar
Hilbert-90 class by u_s and the original y. Its q-phase computation has
no contribution from D_Gamma c_s, since Gamma is inertia at q and the
balanced derivative has augmentation zero. Consequently the R701 identity
has the same actual C. Nonzero lambda modulo p in (708.7) is incompatible
with that global ordinary condition. This is precisely the information
missing from a purely local or field-Norm reconstruction.

## 5. What the exact isogeny distribution does compress

There is an explicit geometric compression of the huge q-product, but
its size must be stated correctly.

Let E=A, choose the original real q-torsion point Q, and put

    H_q=(F_(q^2)^*)^43,
    m_q=(q^2-1)/43, d_q=(q+1)/43.

Since 43 does not divide q-1, H_q contains F_q^*. Under the original
CM identification E[q] with O_K/(q)=F_(q^2), the set H_q Q is a
disjoint union of the nonzero points on d_q distinct cyclic subgroups
C of order q. Let this set of subgroups be D_q. The members of D_q
are the cosets H_q/F_q^*, with their original labels.

For each C choose the quotient isogeny phi_C:E -> E/C with the invariant
differential normalization of the Robert function

    v_E(R)=Delta_E^10/psi_(11,E)(R).

For each original point R=P_2+R_(p^2), with the prescribed tame and
scalar shifts of its p^2 part, the exact odd-degree isogeny distribution
of R198 (198.4) gives

    product_{S in C} v_E(R+S)=v_(E/C)(phi_C R).

All evaluations avoid the 11-torsion divisor. Removing the S=0 factor
and multiplying over D_q proves

    product_{h in H_q} v_E(R+[h]Q)
      =v_E(R)^(-d_q) product_{C in D_q} v_(E/C)(phi_C R).   (708.10)

There is no root-of-unity or sign ambiguity: the degree q is odd and
prime to 11, and the normalization is exactly the one already proved
in R198. Taking the existing mu_42 and T norms, and the original s^11
shift, is compatible with (708.10). This does not introduce a different
Robert unit.

Formula (708.10) is a genuine product compression from m_q nonzero points
to d_q quotient curves. However d_q=(q+1)/43 for the same 776-bit q is
still enormous. It is not a list of 43 quotient curves, and it is not
an executable small-degree substitute for the unknown c_s or c_q.

The distinction from the pure-p R198/R561 computation is concrete. There,
an additive subgroup of order 43 is a kernel of a degree-43 isogeny;
the norm reduces to a single function value on that quotient. Here
H_q Q is a multiplicative CM orbit. It is not a coset of a nontrivial
additive subgroup of E[q], since its size m_q is prime to q. Even after
adjoining the zero point its size is

    1+d_q(q-1),

strictly between q and q^2. Additive subgroups of the two-dimensional
F_q-space E[q] have sizes 1, q and q^2. Therefore H_q Q union {0}
is not an isogeny kernel either.

Taking all 43 Gamma conjugates fills every nonzero point of E[q]. The
single multiplication-q distribution then becomes available:

    product_{S in E[q], S!=0} v_E(R+S)
      =v_E([q]R)/v_E(R).                                (708.11)

After the outer norms, (708.11) is exactly the familiar full Gamma Euler
relation in (708.4). It loses the partial-orbit information measured by
(708.7). The result does not rule out a different fast global algorithm;
it proves that the quoted complete-kernel distribution cannot simply be
applied to this partial orbit as though it were one small kernel.

## 6. Remaining computational task and sources

The outstanding input is still one of the following genuinely global
pieces of arithmetic: the actual mixed Robert units in the marked normal
basis; an ordinary global Norm witness for the original y or u; or the
original q-principalization X_t in F_t with its prescribed norm and
first moment. An additional exact global identity for the original
partial q-orbit could also supply it, but (708.4), local Norm solving,
and the isogeny identities (708.10)-(708.11) alone do not.

No large product, new numerical window, or long computation is claimed
or proposed in this proof.

Arithmetic inputs: R171, R191, R198, R311, R327, R377, R561, R613,
R619 and R701. The local Norm argument is the standard local reciprocity
identification for an abelian extension, as in J. S. Milne, *Class Field
Theory*, version 4.03, Chapter III, Theorems 3.1 and 3.4 (printed
pp.107-108), together with the naturality of local reciprocity,
<https://www.jmilne.org/math/CourseNotes/CFT.pdf>.

For the exact normalized isogeny distribution, see A. J. Scholl,
*An introduction to Kato's Euler systems* (1998), Theorem 1.2.1(iii),
Remark (iv) and proof, printed pp.384-386,
<https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf>;
the normalization and odd-degree sign are already checked explicitly
for the present function in R198 §1.1.
