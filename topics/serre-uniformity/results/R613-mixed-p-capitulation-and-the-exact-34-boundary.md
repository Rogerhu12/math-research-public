# R613: ordinary capitulation in 42 mixed-p extensions and the exact 34 boundary

**Status: proved from the complete R561 recovery and the published R198
input. The original scalar class and the original Norm residue remain
unknown.**

For the full pure-p layer, let S be the scalar direction and T the
anti-p direction with the original generators.  For every
\(r\in\mathbf F_{43}\), put

\[
 H_r=\langle ts^r\rangle,\qquad F_r=B^{H_r},\qquad M_r=LF_r.
\]

The class constructed by the same actual Robert/Hilbert 90 procedure as
R561, now on \(M_r/L\), has the exact coefficient

\[
 \boxed{C_r=C+34r\quad\text{in }k=\mathbf F_{43}[i].}
\]

Here C is the original scalar coefficient of R561 and
\(C\in i\mathbf F_{43}\).  Consequently \(C_r\ne0\) for all
\(r\ne0\), and the entire ordinary character class group of L
capitulates in each of these **42 actual extensions** \(M_r/L\).
The scalar field is \(F_0=F_s\); this statement does not decide C at
\(r=0\), does not compute the old ordinary coefficient b, and does
not prove the old bridge \(C=-34ib\).

The family here mixes S and T in the **pure-p** layer. It is distinct
from any family mixing the q direction Gamma with T.

## 1. The ordinary class line and its exact coefficient convention

Use the original data

\[
 p=43,\quad K=\mathbf Q(i),\quad A:y^2=x^3-x,\quad
 F=K(A[p])^{\mathbf F_p^\times},\quad L=FL_q.
\]

Write \(\Delta=\langle\sigma\rangle=C_{44}\) and
\(\Gamma=\langle\gamma\rangle=C_{43}\).  The marked sigma is
the tame primary beta direction \(\beta=-1+2i\); its q component is
trivial.  Gamma is the original positive tame generator, characterized
by \(\gamma\theta/\theta\equiv\zeta\) at q in R207/R311.

Let \(\mathcal O=\mathbf Z_{43}[i]\),
\(k=\mathcal O/43=\mathbf F_{43}[i]\), and let
\(\widehat\omega\) be the Teichmuller root with

\[
 \omega=8+25i\pmod {43},\qquad
 \widehat\omega=352+197i\pmod {43^2}.
\]

We use the field/divisor character on which sigma has eigenvalue
\(\widehat\omega^{-1}\), denoted \(\chi^-\), and the
**unaveraged** operator

\[
 P_+=\sum_{a=0}^{43}\widehat\omega^a\sigma^a=44e_{\chi^-}.
\]

No factor \(1/44\) is inserted.  R210 proves

\[
 A_L:=\bigl(\operatorname{Cl}(L)\otimes\mathcal O\bigr)_{\chi^-}
       \simeq\mathcal O/43=k.
\]

This is the **ordinary** ideal class group, with full finite divisors.
It is not a ray class or an S-class quotient.  If \(Q_L\) is the
marked q-prime of L, then

\[
 e_q=[P_+Q_L]
\]

is a nonzero k-basis.  The coefficient of \(Q_L\) in the displayed
divisor is 1.  The R561 genus Artin calculation gives, with the same
transport on all 44 conjugate primes,

\[
 \operatorname{Artin}(P_+Q_L)=44\cdot32.
\]

That calculation is based on R168's strict-p primal class with finite
coefficient 16 and singular coefficient 1.  In its \(\chi^-\)
coordinate, \(F_0\mapsto1\), \(K_0\mapsto-i\); thus its
\(K_q\)-Frobenius value is 32.  This fixes the sign and the scale of
the coefficient C used below.

All multiplicative groups are written additively after tensoring with
\(\mathcal O\) and taking this character summand.  A displayed
Hilbert 90 equation or divisor equation refers to this actual completed
ordinary multiplicative group and its full divisor group.

## 2. A single ancestor unit for both already computed p directions

Put

\[
 T_2=K(A[p^2]),\qquad B=T_2^{\mu_{42}},\qquad
 S=\langle s=1+p\rangle,\qquad
 T=\langle t=1+21pi\rangle.
\]

Here \(\mu_{42}\) is the rational Teichmuller subgroup.
Then \(\operatorname{Gal}(B/F)=S\times T\), each factor of order
p, and \(\kappa_p(t)=1\).  The two old fields are
\(F_s=B^T\) and \(F_t=B^S\).

Choose the original real p-torsion point P and a real R with pR=P.
Use the exact R198 function

\[
 v(Q)=\frac{64^{10}}{\psi_{11,A}(Q)},\qquad P_2=(i,1-i).
\]

Let

\[
 U_B=N_{T_2/B}v(P_2+R),\qquad u_B=P_+[U_B].
\]

This is one specified global ancestor, rather than separate choices
of Norm preimages on the two quotient fields.  Its two norms are

\[
 u_t=N_Su_B,\qquad u_s=N_Tu_B,
\]

and the exact odd-isogeny distribution gives

\[
 N_{S\times T}u_B=u:=P_+[u_0].                       \tag{613.1}
\]

Indeed, the full principal-p subgroup traverses \(R+A[p]\).
The multiplication-p distribution gives \(v([p]P_2+P)\);
\([p]P_2=-P_2\), and evenness together with the scalar norm gives
exactly the original \(u_0\).  The torsion conductors contain both
2 and p, so these are ordinary Robert units; even the weaker
\(\{2,p\}\)-unit statement would suffice after this character
projection because those divisor modules have zero \(\chi^-\)
component.

The anti-p quotient in R198 uses \(A/\langle P\rangle\), with
the actual t step 21 and beta correction -11 times its kernel point.
The scalar quotient in the new R561 computation uses
\(A/\langle iP\rangle\), with scalar step 1 and beta correction
-22 times its kernel point.  Both are the norms of the U_B above,
using the same function, P, R, primary tame lift and Weil root.

At q the anti-p quotient has the unique branch fixed by the original
tau.  The scalar quotient has 43 S-conjugate choices; its projected
\(\mu_p\) phase is S-invariant.  Thus the R198 branch and any
one of the R561 scalar choices extend to a common q-prime of B, and
no incompatible pair of unrelated Norm witnesses has been combined.

## 3. The two exact finite inputs and the coefficient 34

For the original Weil root zeta, let

\[
 \ell(x)=\log_\zeta\bigl(\overline x^{(q^2-1)/43}\bigr).
\]

On a \(\mu_{43}\) residue, write r_mu for the direct exponent
in zeta.  Since \((q^2-1)/43\equiv21\pmod{43}\),

\[
 r_\mu=-2\ell.                                      \tag{613.2}
\]

R198 (198.14), in the original t marking, gives

\[
 \ell(D_Tu_t)=13i,\qquad D_T=\sum_{j=0}^{42}jt^j.
                                                               \tag{613.3}
\]

The complete scalar computation in R561 gives the two high Teichmuller
power projections \((9,0)\), with exponent
\((q^{86}-1)/43^2\).  That full exponent also reduces to 21 modulo
43, so

\[
 r_\mu(u_s)=25.                                     \tag{613.4}
\]

The full scalar run checked all 44 exact Norm ratios, the original
Weil pairing, the two p-isogenies, the tame correction and the
p-squared closure.  In particular, (613.4) is an actual restored
finite input, not an old numerical summary assumed to be correct.

At the common q-prime of B the residue field is
\(\mathbf F_{q^{86}}\), whose p-primary multiplicative group is
\(\mu_{p^2}\).  Choose \(\xi\) with \(\xi^p=\zeta\).
Let \(e_j\in\mathcal O/p^2\) be the exponent of the p-primary
residue of \(t^ju_B\) in xi.  The arithmetic q data are

\[
 \operatorname{Fr}_{K_q}=s^{32},\qquad
 s=\operatorname{Fr}_{K_q}^{39},\qquad
 s|_{\mu_{p^2}}=1+2p.
\]

Consequently the S norm acts on exponents as multiplication by p,
because
\(\sum_{a=0}^{p-1}(1+2p)^a\equiv p\pmod{p^2}\).
Since \(N_St^ju_B=t^ju_t\), this proves

\[
 e_j\pmod p=r_\mu(t^ju_t),\qquad
 \sum_jje_j\equiv-2\cdot13i=17i\pmod p.            \tag{613.5}
\]

Also \(N_Tu_B=u_s\), so (613.4) says

\[
 \sum_je_j=25p\pmod{p^2}.                           \tag{613.6}
\]

For each \(r\in\mathbf F_p\), define
\(u_r=N_{H_r}u_B\).  At this prime, the element
\((ts^r)^j\) gives the exponent
\((1+2prj)e_j\).  Therefore (613.5)--(613.6) give the actual identity

\[
 \begin{aligned}
 \text{the }\mu_{p^2}\text{ exponent of }u_r
 &=\sum_j(1+2prj)e_j\\
 &=p(25+34ir)\pmod{p^2},
 \end{aligned}
\]

or equivalently

\[
 \boxed{r_\mu(u_r)=25+34ir.}                        \tag{613.7}
\]

The computation does not depend on the chosen lift xi of zeta.
Replacing xi by \(\xi^{1+kp}\) multiplies the exponents by
\(1-kp\), which leaves both (613.5) and the divisible-by-p sum
(613.6) unchanged in the places where they are used.

This proves the coefficient 34 from the common actual ancestor:
it is \(2\cdot(-2)\cdot13=-52=34\pmod{43}\).
It does not use a ray-T action as an ordinary class action.

## 4. The exact global mixed-pq products on every field F_r

It remains essential to connect (613.7) to actual ordinary divisor
classes. A local residue formula alone would not prove capitulation.

In the actual p-squared-q torsion field, choose a nonzero real
q-torsion point \(Q_q\), and put
\(H_q=(\mathbf F_{q^2}^\times)^{43}\), as in R311.
Start with the same function v and take the actual product over
\(\mu_{42}\times H_q\) of
\(v(P_2+[k]R+[h]Q_q)\).  Apply P_+, and call the result
\(c_{B,\mathrm{raw}}\in BL\).  Define

\[
 c_B=s^{11}c_{B,\mathrm{raw}}.
\]

This is equivalently the q-inverse-p-point convention
\([q]^{-1}R\) used in R561.  The exact distributions give

\[
 N_{S\times T}c_B=c_q,
 \qquad N_\Gamma c_B=(1-s^{11})u_B.                 \tag{613.8}
\]

For the first identity, the full p-direction norm uses the
multiplication-p isogeny.  The replacement of \(Q_q\) by
\([p]Q_q\) is absorbed by \(H_q\), since
\(\mathbf F_q^\times\subset H_q\); the sign on P_2 is absorbed
by evenness and the scalar product, just as in (613.1).

For the second identity, the Gamma norm extends the H_q product to
all nonzero q-torsion points.  The exact multiplication-q distribution
then gives
\((s^{32}-1)u_B\) on \(c_{B,\mathrm{raw}}\): q is a scalar,
\(-q\equiv1+32p\pmod{p^2}\), and \(qP_2=-P_2\).
Applying \(s^{11}\) gives \((1-s^{11})u_B\), because
\(32+11=43\).  There is no anti-p correction in this q scalar.
All the products have conductor supported on at least the distinct
primes 2, p and q, and are ordinary units in the character summand.

Now set

\[
 c_r=N_{H_r}c_B\in M_r.
\]

S and H_r have trivial intersection and generate \(S\times T\).
All norm operators commute with Gamma, with the actual tame Delta,
and with the character projection.  Thus (613.1), (613.8) give, on
every r without a new choice of a norm witness,

\[
 \boxed{N_Su_r=u,\qquad N_Sc_r=c_q,
 N_\Gamma c_r=(1-s^{11})u_r.}                       \tag{613.9}
\]

The image of S generates \(\operatorname{Gal}(M_r/L)\).
At q, S intersects H_r trivially, so \(F_r/F\) is unramified of
degree p and its positive Frobenius remains \(s^{32}\).  The local
q field of F_r is the same degree-p unramified field used above.
The extension \(M_r/F_r\) is the original totally ramified Gamma
extension.  These statements retain the original gamma and s
orientations; they do not relabel them to fit (613.7).

## 5. Full Hilbert 90 divisor descent and the class C_r

Keep R561's fixed ordinary q-Norm unit y and coefficient a:

\[
 a=15i/7,\qquad N_\Gamma y=u,\qquad
 py=u+aD_\Gamma^{\rm bal}c_q,
\quad D_\Gamma^{\rm bal}=\sum_{j=-21}^{21}j\gamma^j.
\]

This is the same actual R311 positive-root construction, transported
through the R219 integral character normalization.  It is independent
of r.  Define

\[
 v_r=u_r-y+aD_\Gamma^{\rm bal}c_r.
\]

Equation (613.9) gives \(N_Sv_r=0\).  Hilbert 90, flatly tensored
with \(\mathcal O\) and projected to \(\chi^-\), supplies
an actual completed multiplicative element \(z_r\) with

\[
 (s-1)z_r=v_r.                                      \tag{613.10}
\]

Since \(v_r\) is an ordinary unit, \(\operatorname{div}z_r\)
is S-invariant.  The extension \(M_r/L\) ramifies only above p.
The entire Delta at p is inertial and fixes the p-prime, so that
prime's divisor module has zero \(\chi^-\) component; the Gamma
copies have the same property.  Everywhere else the extension is
unramified, so invariant divisors descend with ramification index 1.
There is consequently a full finite divisor D_r of L such that

\[
 \operatorname{div}_{M_r}z_r=j_{M_r/L}D_r.           \tag{613.11}
\]

No outside-support term is discarded.  Any two z_r solving (613.10)
differ by an S-invariant multiplicative element, so their D_r differ
by a principal divisor of L.  Thus

\[
 [D_r]\in\ker\bigl(A_L\longrightarrow
             (\operatorname{Cl}(M_r)\otimes\mathcal O)_{\chi^-}\bigr)
\]

is a genuine ordinary ideal class. Define its coefficient by

\[
 [D_r]=C_r e_q.                                     \tag{613.12}
\]

For later reciprocity put \(D_S=\sum_{j=0}^{42}js^j\).
The Gamma norm of \(v_r\) is \(pu_r-u=(s-1)D_Su_r\), so

\[
 h_r=N_\Gamma z_r-D_Su_r\in F^\times\otimes\mathcal O,
 \qquad \operatorname{div}_F h_r=N_\Gamma D_r.       \tag{613.13}
\]

This equality includes the entire outside divisor of (613.11).
It is the actual principal norm needed for the ordinary genus
Artin computation, rather than a substituted ray representative.

## 6. The q phase and the ordinary Artin coefficient

Let \(r_y=r_\mu(y)\). R561 proves, in the original complete
normalization,

\[
 r_y=2\mathcal L+6\in\mathbf F_{43},\qquad
 C=i(r_y-25),\qquad \mathcal L=31-22iC.              \tag{613.14}
\]

At q the Gamma derivative term in \(v_r\) has zero residue: Gamma
is inertia, and the balanced derivative has augmentation zero.
Use the real R207 q-ray uniformizer theta to remove the valuation
of z_r.  Its Gamma norm divided by q is a rational q-unit and hence
has no p-primary residue.  If the remaining unit part of z_r has
\(\mu_{p^2}\) exponent e, (613.10) and (613.7) give

\[
 2e=r_\mu(u_r)-r_y.
\]

Taking the Gamma norm gives the direct \(\mu_p\) exponent e;
the \(D_Su_r\) term has zero phase because
\(\sum_{j=0}^{42}j\) is divisible by p.  Consequently

\[
 r_\mu(h_r)=\frac{r_\mu(u_r)-r_y}{2},\qquad
 \ell(h_r)=\frac{21}{2}\bigl(r_\mu(u_r)-r_y\bigr).  \tag{613.15}
\]

These logarithms are taken after removing the q valuation.  The
formulas are \(\mathcal O\)-linear, and therefore remain valid
when \(r_\mu(u_r)\) has both real and imaginary coefficients.
No assertion that the mixed field is globally real or CM is used.

For completeness, the ordinary reciprocity step has the same
unchanged base L as R561.  Positive local reciprocity gives the
strict-p genus character value \(+i\ell(\text{unit})\); its
q-uniformizer value is 32.  Apply global reciprocity to the full
principal norm (613.13).  The q-exterior Artin sum is the negative
of the full q-local sum.  The q-valuation part of D_r adds back the
\(32v_q(h_r)\) terms, so only the residue part remains.  On the
44 Delta-conjugates the logarithm and transported character have
opposite weights; their product is constant. Thus

\[
 \operatorname{Artin}(D_r)=-44i\ell(h_r),\qquad
 C_r=-\frac{i}{32}\ell(h_r).
\]

Since \(64\equiv21\pmod{43}\), (613.15) gives

\[
 C_r=i\bigl(r_y-r_\mu(u_r)\bigr)
    =i(r_y-25-34ir)=C+34r,                          \tag{613.16}
\]

which proves the claimed formula with its exact sign and scale.

## 7. Coefficient conjugation and actual capitulation

Because \(\mathcal L\in\mathbf F_{43}\), (613.14) proves
\(C\in i\mathbf F_{43}\), or equivalently
\(C=-\overline C\).  The involution on k here is coefficient
conjugation \(i\mapsto-i\); it is not an untracked change of a
Weil root. Since \(43\equiv3\pmod4\), i is not in
\(\mathbf F_{43}\), and real and imaginary parts are independent.

The global family has the matching conjugation behavior:
\(\tau s\tau=s\), \(\tau t\tau=t^{-1}\), so
\(\tau H_r\tau=H_{-r}\).  With coefficient conjugation included,
the original P_2 transformation makes \(\tau u_B=-u_B\) and
\(\tau c_B=-c_B\); the -i change of the R label is the tame
Delta order-two element after the rational norm.  Also
\(\tau y=-y\), \(\tau a=-a\), and
\(\tau D_\Gamma^{\rm bal}\tau=-D_\Gamma^{\rm bal}\).
Thus \(\tau v_r=-v_{-r}\).  Equation (613.10) gives
\([D_{-r}]=-[\tau D_r]\), while \(e_q\) is semilinearly
tau-fixed.  Hence

\[
 C_{-r}=-\overline{C_r},
\]

in agreement with (613.16).  This also explains the pure-imaginary
scalar coefficient at r=0 directly at the divisor level.

For \(r\in\mathbf F_{43}^\times\), equation (613.16) gives

\[
 \operatorname{Re}(C_r)=34r\ne0.
\]

Therefore \(C_r\ne0\) in the field k.  The class \([D_r]\)
lies in the ordinary capitulation kernel by (613.11).  Since
\(A_L=ke_q\) and C_r is invertible in k, this forces
\(j_{M_r/L}(e_q)=0\).  The entire character class group
capitulates.  The 42 nonzero r give 42 distinct subgroups H_r and
42 distinct actual degree-p extensions \(M_r/L\).

This is more than a local nonzero residue or an abstract kernel
criterion: the full Hilbert 90 divisor gives an element of the
ordinary principalization kernel, and its nonzero coefficient
forces that kernel to be the full known class line.

At r=0 the conclusion is only the original unknown C.  Neither
its zero/nonzero status nor its value has been obtained here.
The old b/lambda/n bridge and the original \(\mathcal L\) remain
open.

## 8. Actual small verification and data boundary

The standard-library verifier `verify_r613_mixed_p_boundary.py`
reads the published R198 certificate and the new complete scalar
certificate of R561; either may be supplied as deterministic gzip.
It recomputes the weighted 44-row derivative from the actual stored
rows, obtaining \(13i\), rather than copying its summary field.
It checks the common original q, the generator directions, the
scalar high outputs, the \(\mu_p\)-to-log conversion, and the
\(1+2p\) norm and mixed-power formulas.

It then verifies the coefficient 34 and the full formula
\(C_r=34r+i\nu\) for all 43 r and every symbolic possible
\(C=i\nu\), \(\nu\in\mathbf F_{43}\).  The 1806 cases with
\(r\ne0\) are all nonzero.  The variable nu is explicitly
symbolic: no row is selected as the actual original C.

The large R198 or R561 Robert evaluations are not rerun for this
small algebraic boundary check.  Their complete mathematical and
arithmetic provenance is retained by decompressed SHA256 values.

```sh
python scripts/verify_r613_mixed_p_boundary.py \
  notes/r198_p_squared_robert_certificate.json \
  notes/r380_scalar_recovery_certificate.json.gz \
  --output /tmp/r613-mixed-p-recheck.json \
  --check notes/r613_mixed_p_boundary_certificate.json
```

The proof of the global extension, full divisor descent and ordinary
principalization implication is in sections 4--7; the small program
does not purport to prove class field theory by finite enumeration.
Its explicit false flags retain the original scalar C, b, lambda, n
and \(\mathcal L\) as uncomputed.
