# R561: restored scalar Robert cocycle and its ordinary Artin class

Status: proved recovery, with a new complete exact finite-field run.  The old
R561 file and the old scalar certificate were lost with the previous workspace.
This proof reconstructs the normalization from the published R168, R198, R201,
R207, R210, R219, R311 and R322.  The scalar input formerly called R380 was
actually recomputed from the original R198 q, P and Weil root; the result is
(9,0), with all 44 exact Norm identities and all markings checked.

The conclusion is a fully specified ordinary ideal class C and the exact
identity L=31-22iC.  The original ordinary b, lambda, n, C and L remain
numerically unknown.  In particular, the old bridge C=-34ib is not used here.

## 1. Fields, generators, and the character projector

Let p=43, K=Q(i), A:y^2=x^3-x, F=K(A[p])^{F_p^*}, and let
Delta=<sigma>, |Delta|=44.  The primary beta=-1+2i fixes P_2=(i,1-i).
We use the actual tame lift of beta, removing its full principal-unit
part at p^2.  Set omega=8+25i modulo p and
omegahat=352+197i modulo p^2.  With coefficients in the p-adic coefficient
ring O, write

    Pplus = sum_{j=0}^{43} omegahat^j sigma^j.

There is no division by 44.  Its image has sigma eigenvalue omegahat^{-1};
this is the field/divisor chi-minus component throughout this file.
All multiplicative groups below are written additively after tensoring
with O and projecting to that component.  Group-ring formulas therefore
mean genuine multiplicative equalities in the completed tensor, not
formal equations in a different module.

Let L=F L_q, Gamma=<gamma>, |Gamma|=p, where L_q is the actual q-ray
extension with the positive R311/R322 generator.  Let
B=K(A[p^2])^{mu_42}, S=<s=1+p>, and T=<t=1+21pi>.
Thus kappa_p(t)=1; F_s=B^T is the scalar-only p-extension, F_t=B^S is
the anti-p extension, and M=L F_s.  At the marked q-prime, the positive
K_q Frobenius in S is s^32, so its inverse is s^11 and s=Fr_{K_q}^{39}.
On mu_{p^2} at that point, s acts as 1+2p.

## 2. Recovering the norm target from R311, without changing its marking

R311 fixes the ordinary real product Y and the real group-ring operator
Pi=sum_j center_p(15 Re(omega^j)) sigma^j.  Its exact equations are

    pY = 7U + Pi D_bal c_q_raw,       N_Gamma Y=7U,
    U=Pi z,                        u_0=15i z on the chosen component,

where D_bal=sum_{j=-21}^{21} j gamma^j and z is the short Robert unit.
Let k=Pi(omegahat^{-1}) in O; k mod p=29.  Put

    a=15i/7,  u=Pplus u_0,  c_q=Pplus c_q_raw,
    y=(a/k) Pplus Y.

These definitions give, in the same component,

    N_Gamma y=u,
    py=u+a D_bal c_q,
    (gamma-1)y=a gamma^22 c_q.

The third equality uses (gamma-1)D_bal=p gamma^22-N_Gamma and
N_Gamma c_q=0.  In particular, y is the actual R311 norm preimage,
not an arbitrarily chosen p-th root of u.

The published R322 formula for the original L is

    L=19 sum_{j=1}^{21} Im(omega^j) ell(sigma^j Y)-3.

Since a/k mod p=31i and the real Y gives
ell(Pplus Y)=2i sum Im(omega^j) ell(sigma^j Y), this yields

    ell(y)=40-L.

Here ell is the original Weil-normalized power-residue logarithm.  For
a residue in mu_43, its direct exponent r in the original Weil root
satisfies ell=21 r, equivalently r=-2 ell, because
(q^2-1)/43=21 modulo 43.  Consequently

    r_y := direct mu_43 exponent of y = 2L+6.

The distinction between r and ell must be retained below.

## 3. Actual p^2 and p^2q Robert products

Use the exact Kato--Siegel/Robert function of R198,
F_E(Q)=Delta_E^10/psi_{11,E}(Q), whose odd-degree isogeny norm is exact.
Choose an actual p^2 point R with pR=P, compatible with the original
real branch; the tame lift of beta has principal-unit correction
22+11i.  Let u_B be its mu_42 norm and set u_s=N_T u_B, followed by
Pplus projection.  Then

    N_S u_s=u.

In the actual p^2q torsion field take the corresponding mixed Robert
product, norm over mu_42, T and the chosen q-torsion norm subgroup.
With the p^2 argument R, call it c_raw.  The exact distribution relations
give

    N_S c_raw=c_q,
    N_Gamma c_raw=(s^32-1)u_s.

The product used in the Hilbert 90 equation is the one with argument
[q]^{-1}R, namely c=s^11 c_raw.  Thus the correctly oriented equalities
are

    N_S c=c_q,
    N_Gamma c=(1-s^11)u_s.

The equality N_S c=c_q is unaffected by the shift.  All these Robert
values are ordinary units: their torsion conductors contain at least
two distinct primes.  Their exact finite q evaluations and the full
Norm relations, rather than a ray-module analogue, are the input here.

## 4. The actual Hilbert 90 class, with its sign fixed by the norm

Define

    v=u_s-y+a D_bal c.

The preceding exact identities give N_S v=u-py+a D_bal c_q=0.
Hilbert 90 supplies z in M^* tensor O in the same character component
such that

    (s-1)z=v.                                      (H90)

This sign is part of the definition.  In particular, replacing v by -v
reverses the class below and is not an innocuous choice of logarithm.

Since v is an ordinary unit, (s-1)div_M z=0.  The extension M/L is
ramified only over p.  Its p-prime divisor module has zero chi-minus
component.  Away from p the extension is unramified, so its invariant
divisor lattice is exactly the image of extension of divisors.  Hence
there is a full divisor D of L such that

    div_M z = j_{M/L} D.

This D contains every outside-support term of div z; none is discarded.
Changing z by an S-invariant element of M^* changes D by a principal
divisor of L.  It therefore defines a genuine ordinary ideal class
[D] in ker(Cl(L)_chi -> Cl(M)_chi).  Define C by

    [D] = C [Pplus Q_L],

where the coefficient of the chosen q-prime Q_L in Pplus Q_L is 1.
The assertion that this is a k-line, and the actual identification of
that line, must use the ordinary genus class field of R210.

Put D_S=sum_{j=0}^{42} j s^j.  Because the Gamma-norm of D_bal c is
zero and N_Gamma y=u,

    N_Gamma v=p u_s-u=(s-1)D_S u_s.

Taking N_Gamma of (H90) shows that

    h=N_Gamma z-D_S u_s

is S-invariant, hence belongs to F^* tensor O.  Taking divisors gives

    div_F h=N_Gamma D.                            (principal norm)

This is the actual principal norm to which the genus reciprocity
formula is applied.  It is not Norm(alpha_F), and no ordinary norm
unknown has been replaced by the known polynomial defining F.

## 5. The required finite input and the q-phase calculation

The new exact scalar-p finite run in the appendix gives:

    high p^2 power-residue projection of u_s = 9,

with exponent (q^86-1)/p^2 and the original Weil root.  This implies
that the direct mu_p exponent of u_s is 25, since the exponent reduces
to 21 modulo p on mu_p and 21^{-1}=-2.  The complementary projected
coordinate is 0.  The finite certificate also verifies all 44
exact S-norm relations, the beta correction -22S, and the p^2 closure;
the value 9 alone would not verify the marking.

At q, write z=varpi^d z_unit using the real R207 q-ray uniformizer.
It is S-fixed, and its Gamma-norm divided by q has no mu_p phase.
The D_bal c term has zero residue because Gamma acts as inertia and
D_bal has augmentation zero.  Therefore the residue of (s-1)z is
the phase 25-r_y.  If z_unit has mu_{p^2} part xi^e with xi^p=zeta,
then s=1+2p gives

    2e=25-r_y.

The Gamma norm multiplies the residue exponent by p; D_S u_s has
zero phase since sum j is a multiple of p.  Thus

    r(h)=(25-r_y)/2,
    ell(h)=21(25-r_y)/2=(r_y-25)/4.               (phase)

The last equality is modulo 43.  Omitting the conversion r=-2ell
would introduce a spurious factor of -2 in the final formula.

## 6. Genus reciprocity normalization from the published sources

R168 (168.17), (168.28), together with the exact R171 values
gamma_q=0 and lambda_q=16, give a unique strict-p primal class w
normalized to q-singular coefficient 1.  Its finite coefficient is 16.
Its restriction to G_F is a homomorphism because F trivializes W.
The nonzero tame value and irreducibility under Delta show that its
image is the full two-dimensional irreducible F_p representation.

For clarity about the character direction, write W as the maps
D_z:x -> z conjugate(x).  Conjugating by beta acts on z by omega;
F_0=D_1 and K_0=D_i.  On the conjugate coordinate, which has the same
chi-minus character as Pplus divisors, F_0 maps to 1, K_0 maps to -i,
and sigma acts on values by omega^{-1}.  The w restriction is therefore
written w_minus below.  R168 (168.6) gives

    w_minus(Fr_{K_q})=2*16=32,
    w_minus(gamma)=-i.

The second equality uses R311 section 1.1: gamma theta/theta has
residue zeta, the original R168 tame convention.  With positive local
reciprocity, kappa_q(rec unit)=-ell(unit).  This sign also follows from
R168's positive invariant of the unramified-unit class cup the
uniformizer class and the antisymmetry of the reversed cup.  Hence

    w_minus(rec unit)=+i ell(unit).               (local unit)

Let H/F be the actual class field cut out by w|G_F; before extending
coefficients its Galois group has order p^2, not p.  Its two conjugate
O-character components are k-lines.  Because w is strict at p and
the 2-local representation has zero cohomology, H/F is unramified
away from q and split at p.  Its q-ramification is tame of exponent p.
The intersection H cap L is F: any nontrivial common quotient would
be the Delta-trivial group Gal(L/F), whereas the two-dimensional
Delta-type of Gal(H/F) has no trivial quotient.

Locally at every q-prime, HL/F is an abelian tame extension of exponent
p.  Tame inertia is cyclic, so its order is at most p; L/F already has
inertia of order p.  Thus HL/L is unramified at q.  It is unramified
everywhere else as well.  This is the actual genus class field in R210
section 2.2.  R210 section 2.1 gives Cl(L)_chi=k, so the nonzero map
defined by this extension is the full ordinary character class map.

R207 (207.5)--(207.8) supplies a real q-ray uniformizer theta.  Its
Gamma norm is rational and has q-adic valuation 1.  Consequently
N_Gamma(theta)/q has residue in F_q^*, on which ell is zero since
p does not divide q-1.  Norm compatibility of positive local Artin
therefore gives the value 32 on the marked prime Q_L.  No additional
unramified-quadratic factor is to be inserted: the factor 2 was
already included in w_minus(Fr_{K_q})=32.

Now take the complete equality div_F h=N_Gamma D of section 4.
At primes away from q, w is unramified (and zero at p and 2), so
Norm compatibility identifies their contribution to Artin(D) with
the valuation contribution of h.  Global reciprocity for the
principal element h makes that sum the negative of the full q-local
sum.  At a q-prime lambda the local expression is

    32 v_lambda(h) + i ell_lambda(h/q^{v_lambda(h)}),

with the corresponding Delta transport of w_minus.  The q-prime
contribution of D itself is +32 v_lambda(h), since L/F is totally
ramified there and its residue degree is 1.  These valuation terms
cancel.  This argument includes every outside-support prime of D;
there is no assumption that z or D is supported at q.

To account for the projector explicitly, label lambda_j=sigma^j
lambda_0.  A chi-minus h has sigma h=omegahat^{-1}h, so its local
logarithm at lambda_j is omega^j times the one at lambda_0.  Meanwhile
the transported w_minus has factor omega^{-j}.  Every product in
the global sum is therefore the same.  Similarly the coefficient
of sigma^j Q_L in Pplus Q_L is omegahat^j and its Artin transport is
omega^{-j}.  We obtain the two actual, consistently normalized values

    Artin(D)=-44i ell(h),
    Artin(Pplus Q_L)=44*32.

In particular the q-class is nonzero.  Dividing the two values gives

    C=-(i/32) ell(h).

Together with (phase), 128=-1 modulo 43 gives

    C=i(r_y-25),
    L=31-22i C.

The source-to-Artin argument is written out here independently of the
lost R561 draft.  QC has separately checked its signs and the cancellation
under these explicitly stated published field/class-group hypotheses.
The scalar finite input has now been restored by the actual complete run
described below.  This reconstruction assigns no numerical C or L.

## 7. Interface to the old R573 statement and to R599

The old recovered summary states A'=R/pi^43, s=1+i pi+..., t=1+b pi+...,
lambda=-i b and C=34 lambda=-34i b, hence L=31-17b.  That ordinary
class-module bridge is a separate proof to reconstruct; a scalar ray
action cannot be substituted for the ordinary coefficient b.

R599 seeks an actual ordinary Norm/reciprocity value.  The existence
of the present class and its relation to L do not determine that value.
No conclusion n=1 or n>=2 is entered without a calculation of b or C.

## 8. The recovered scalar finite model and its actual complete evaluation

### 8.1 Original inputs and the opposite p-isogeny kernel

The only external numerical input is the published
`r198_p_squared_robert_certificate.json`.  Its SHA256 is

```
e1666e118c7f10d991cf4aa0107ebbe8b68683cd7c9b3e08a587aab390e86d00
```

It contains the exact 776-bit q, the original real p-torsion point P,
the primary beta-kernel 5-torsion point, and the original Weil root.
The new code checks the curve equations, the orders, beta(P_2)=P_2,
the beta-kernel condition, and the same Weil pairing by Miller's
algorithm.  It does not take the old scalar logarithm as an input.

For the scalar extension the correct quotient is

\[
 E=A/\langle iP\rangle,\qquad
 \phi:A\longrightarrow E,\qquad S=\phi(P),\qquad Q=\phi(R).
\]

This differs from the kernel \(\langle P\rangle\) in the published
anti-p calculation R198.  Here

\[
 \widehat\phi(Q)=P,\qquad [43]Q=S,
\]

and Q has exact order \(43^2\).  The scalar generator acts as
\(sQ=Q+S\).  The curve and S are defined over \(\mathbf F_q\).

Compute the normalized dual Velu isogeny \(\psi\) with kernel S.
Its target has coefficients \((-43^4,0)\); dividing the target x and y
coordinates by \(43^2\) and \(43^3\) gives \(\widehat\phi\).
If \(x_\psi(X)=N(X)/D(X)\), the monic polynomial

\[
 f(X)=N(X)-43^2x(P)D(X)
\]

has degree 43, and

\[
 x_Q=X\bmod f,\qquad
 y_Q=\frac{43^3y(P)}{x_\psi'(x_Q)}.
\]

The program verifies both coordinates of the dual equation and
\([43]Q=S\).  The full 44 coefficients of f are in the certificate.
An independent, subsequent Rabin irreducibility check of f also passes.

### 8.2 The full residue field and its original i

Write \(f(W-i)=A(W)-iB(W)\).  The code uses the degree-86 model

\[
 g(W)=A(W)^2+B(W)^2=f(W-i)f(W+i),\qquad
 i=\frac{A(W)}{B(W)},\qquad x_Q=W-i.
\]

Thus the embedding of the original Gaussian coordinate is explicit.
The model is squarefree.  Direct checks give

\[
 \operatorname{Frob}_q(Q)=Q+16S,\qquad i^q=-i.
\]

These checks also prove the field claim independently of an arbitrary
finite-field generator label.  The point Q has exact order \(43^2\),
so its Frobenius orbit and that of x_Q have length 43.  For the latter,
an equality of opposite points would give \(2Q\in\langle S\rangle\),
which is impossible after multiplying by 43.  Adjoining i has degree
2.  The element \(W=x_Q+i\) has degree 86: it is not fixed by the
43rd Frobenius, and if it were fixed by the second Frobenius, then x_Q
would be in \(\mathbf F_q\).  The full field is therefore
\(\mathbf F_{q^{86}}\), with \(\mathbf F_{q^2}\) embedded by the
recorded algebraic i and the original Weil root.

There are 43 possible Q's, differing by S.  Unlike the anti-p case,
realness alone does not distinguish them.  This causes no ambiguity
in the present invariant: the exact Norm of the projected u_s is u,
whose p-primary residue is trivial.  Since the S norm acts on
\(\mu_{p^2}\) as multiplication by p, the p-primary residue of u_s
already lies in \(\mu_p\), on which S acts trivially.  Consistently
changing the global R also replaces v and z by their S-conjugates;
the descended divisor D, and hence C, do not change.

### 8.3 Actual Teichmuller weights and the 44 tame branches

On branch j set \(P_j=\beta^jP\),
\(E_j=A/\langle iP_j\rangle\), and \(S_j=\phi_j(P_j)\).
The exact isogeny norm of the anti-p direction gives

\[
 u_{s,j}=
 \prod_{k=1}^{42}
 \mathcal F_{E_j}\left(\phi_j(P_2)+[k^{43}\bmod1849]Q_j\right).
\]

The exponent \(k^{43}\bmod1849\) is the actual rational
Teichmuller lift; replacing it by k would change this p-squared layer.

For the tame CM step, construct the degree-5 isogeny from the actual
kernel \(\phi_j(A[\beta])\), then divide its target coordinates by
\(\beta^2,\beta^3\).  This gives
\(\beta_j:E_j\to E_{j+1}\).  The exact correction is

\[
 Q_{j+1}=\beta_j(Q_j)-22S_{j+1}.
\]

The imaginary principal-unit correction 11i is killed by the quotient
kernel \(\langle iP_j\rangle\); the scalar correction 22 remains.
Each step checks the curve equation, the S label, and \([43]Q_j=S_j\).
The final exact closures are

\[
 P_{44}=[5]P_0,\qquad S_{44}=[5]S_0,\qquad
 Q_{44}=[5^{43}\bmod1849]Q_0=[1639]Q_0,
\]

and the quotient curve returns to its starting model.  These are
checks in the actual degree-86 field, not only in its p-Kummer quotient.

### 8.4 All exact norms and both high projections

The source evaluates \(\psi_{11}\) by the division-polynomial
recurrence printed in the source.  It computes all 44 upper values
and all 44 original lower Robert values, using 1848 evaluations on
each level.  For every j it checks the actual equality

\[
 N_{\mathbf F_{q^{86}}/\mathbf F_{q^2}}(u_{s,j})=u_{0,j}.
\]

For efficiency, the norm is an exact degree-43 resultant: substitute
\(W=X+i\), reduce modulo f(X), and take the resultant over
\(\mathbf F_q[i]\).  The Euclidean resultant routine retains each
leading-coefficient factor and sign.  Its constant, i, and x_Q norms
are independently checked before the 44 Robert norms.  The stored
ratio is 1 in every row; this is stronger than equality of power
residue logarithms.

Write \(\widehat\omega^j=A_j+iB_j\bmod1849\), with integer
representatives, and form

\[
 W_A=\prod_j u_{s,j}^{A_j},\qquad
 W_B=\prod_j u_{s,j}^{B_j}.
\]

Raising these to \((q^{86}-1)/43^2\) gives, in the original Weil root,

\[
 \boxed{\left(W_A^{(q^{86}-1)/43^2},
              W_B^{(q^{86}-1)/43^2}\right)=(\zeta^9,1).}
\]

The computation uses the identical exponent in factored form:
\(q^{43}\) fixes x_Q and sends i to -i, so the first factor is
\(\overline W/W\), followed by exponent \((q^{43}+1)/43^2\).
The code checks divisibility before forming that integer exponent.
The full exponent \((q^{86}-1)/43^2\) reduces to 21 modulo 43
(the shortened exponent \((q^{43}+1)/43^2\) reduces to 11).
Hence the direct \(\mu_{43}\)
exponent of the projected u_s is \(-2\cdot9=25\), exactly the input
used in section 5.

### 8.5 Recoverable files, independent check, and precise scope

The complete run took 712.597 seconds.  Its output was

```json
{"status":"PASS","all_44_norm_ratios":"1",
 "high_projection_logs":[9,0],"closure_Q_multiplier":1639,
 "actual_C_computed":false,"actual_L_computed":false}
```

The full finite certificate stores f, g, the embedding of i, initial
and final Q, all 44 upper values and exact norms, both projected
products, and the two final powers.  The original executed source is
preserved.  A portable verifier adds only input/output options and
optional certificate comparison; the arithmetic functions have
identical parsed syntax trees.  That audit is saved separately, and
the large calculation was not rerun merely for the I/O wrapper.

The independent small normalization checker additionally verifies
the degree-43 polynomial's irreducibility, the original Weil embedding,
the stored high outputs, the exact k=29 and a/k=31i coefficients,
the two power-log conversion factors, the scalar Frobenius direction,
and all 43 instances of the final scalar identities.  It explicitly
records that it does not repeat the large Robert products or the
long high powers.

Files supplied for publication:

- `verify_r561_scalar_robert.py`: portable complete verifier;
- `r380_scalar_recovery_certificate.json.gz`: losslessly compressed complete new arithmetic data; the decompressed SHA256 is `a6fd98bd55145e3ce91f4f79d2b9790d65cd740ece7229f07b288272c9783890`;
- `verify_r561_normalization.py`: independent small checker;
- `r561_normalization_certificate.json`: its complete output;
- `r561_portability_patch_audit.json`: the exact source-wrapper audit;
- `rebuild_r380_scalar_robert.py`: original source used for this recovery run.

For a fresh full run, assuming python-flint 0.9.0 is available:

```sh
mkdir -p /tmp/r561-recheck
gzip -dc notes/r380_scalar_recovery_certificate.json.gz > /tmp/r561-recheck/reference.json
python scripts/verify_r561_scalar_robert.py \
  --input notes/r198_p_squared_robert_certificate.json \
  --outdir /tmp/r561-recheck \
  --check /tmp/r561-recheck/reference.json

python scripts/verify_r561_normalization.py \
  /tmp/r561-recheck/reference.json \
  notes/r198_p_squared_robert_certificate.json \
  --output /tmp/r561-normalization-recheck.json
```

The use of a new output directory prevents overwriting the frozen
published data.  The q-Robert product c, the coordinates of y and z,
the ordinary class C, and the original L have not been evaluated.
The formal class definition and the identity relating C to L have
been proved; the finite scalar input required by that identity has
been actually recomputed.
