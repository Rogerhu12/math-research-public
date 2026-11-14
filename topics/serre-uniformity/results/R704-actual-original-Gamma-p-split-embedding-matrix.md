# R704: actual p-split embeddings with all 43 original Gamma labels

Status: proved and computed from the existing R191 and R305 exact inputs.
The complete 43 by 43 embedding matrix of the original q-ray normal basis
has now been evaluated modulo 43^2. Its determinant is 687, namely
q^21 modulo 43^2. The original c_s and c_q Robert coordinates have not been
computed, so this does not evaluate the 86 by 44 R701 unit matrix or C.

The new calculation uses the existing small R305 multiplication certificate;
it does not reconstruct its CRT table or enumerate q-torsion.

## 1. Fixed field, fixed root, fixed direction

Keep the same p=43, q, Weil root, positive tame gamma, and original CM phase
as R191, R305, R311 and R561. In this section only, write upsilon for the
order-42 cyclotomic automorphism zeta -> zeta^3, to distinguish it from the
order-44 sigma acting on F in R561 and R701.

Put

    B_cyc=K(zeta), r=i(zeta-zeta^-1),
    h_j=upsilon^j(g(r)(2-r)^22),
    e_j=center_43(3^-j), E_j=e_j mod 43 in {1,...,42},
    a_q=product_j h_j^e_j,
    c_+=product_{j:e_j<0} h_j.

These are exactly the existing R191 and R207 inputs. The original real
Kummer roots satisfy

    alpha^43=a_q,
    alpha_+=c_+ alpha,
    alpha_+^43=product_j h_j^E_j.

R191 provides the explicit polynomial b0 in r with

    b0^43=a_q modulo 43^4.

The polynomial f(r) is Eisenstein of degree 42 and b0 is a unit. Hensel's
lemma therefore supplies a root b with

    b^43=a_q, b-b0 in 43^3 O_{B_cyc^+,43}.

Indeed v_r(b0^43-a_q)>=168 and the derivative has r-valuation 42; the
resulting error valuation is at least 126. The real local field
B_cyc^+ at 43 does not contain mu_43, so this root is unique there.
Consequently it satisfies the exact original descent equation
upsilon(b)=w_q b^3. The map alpha -> b is thus compatible with the
order-42 lift used to define L_q. It selects a particular embedding

    iota_0 : L_q -> K_43.

This selection is intrinsic to the given real root, rather than a new
ordering of 43 unlabelled roots. The remaining embeddings are fixed by

    iota_n=iota_0 composed with gamma^n, 0<=n<43.             (704.1)

The same exact polynomial identity as R191 is used throughout:

    zeta=(S_44(r)-i r)/2,
    S_0=2, S_1=r, S_{j+1}=r S_j-S_{j-1}.                  (704.2)

The script reevaluates (704.2) at the original r_Q and compares both
coordinates with the stored original Weil root. R311 already proves that
this Kummer gamma agrees with the positive original q-tame generator.
There is no inversion of gamma, replacement of i, or new q-phase.

## 2. Complete evaluation of the normal basis

For k=3^j modulo 43 define

    R_k=upsilon_tilde^j(alpha_+).

R305 gives the ordinary integral normal basis

    theta_n=sum_{k=1}^{42} zeta^(nk) R_k,
    u_n=(1+theta_n)/43,
    gamma(u_n)=u_(n+1).

At the selected p-adic embedding,

    iota_0(R_(3^j))=upsilon^j(c_+ b).

Every h_j and c_+ is a p-adic unit. Replacing b by b0 therefore gives every
R_k correctly modulo 43^3. The coefficient ring used for the actual
calculation is

    (Z/43^4 Z)[r]/(f(r)), with i adjoined independently.

All the calculations are polynomial arithmetic in dimension 42. The
program checks b0^43=a_q modulo 43^4, product_j h_j=-q modulo 43^4, the
order-42 orbit of r, and the 42 identities R_k R_-k=-q modulo 43^3.

It then sums the 43 actual theta_n. Because theta_n is in K_43, all its
nonconstant r-coefficients vanish modulo 43^3; this is checked for each
n and both i-coordinates before any division. Both constant coefficients
of 1+theta_n are divisible by 43, also checked individually. Division by
43 gives

    v_n=iota_0(u_n) modulo 43^2 in (Z/43^2 Z)[i].            (704.3)

Thus the whole marked embedding matrix is

    M[n,j]=v_(n+j mod 43), 0<=n,j<43.                      (704.4)

The certificate stores all 43 pairs v_n, an unambiguous rule for (704.4),
and a hash of the expanded matrix. Some actual values are

    v_0  = 750,
    v_1  = 1840+1666 i,
    v_42 = 1840+183 i                 modulo 1849.

They satisfy sum_n v_n=1 and v_-n=conjugate(v_n). The latter verifies
the original semilinear tau convention simultaneously with the Gamma
ordering, since tau fixes b and r and conjugates i.

No approximation of a complex root and no polynomial factorization with
an arbitrary choice of a p-adic factor is used.

## 3. Independent multiplication and invertibility checks

Read the existing R305 exact table

    u_0 u_s=sum_t c[s,t] u_t, c[s,t] in Z[i].

For each of the 43 marked embeddings, the script checks all 43 rows:

    M[n,0] M[n,s]=sum_t c[s,t] M[n,t] modulo 43^2.          (704.5)

Thus there are 1849 independent product-row checks, using the existing
global integer table, not an internally reconstructed replacement.
Together with sum_j M[n,j]=1, these say that the calculated rows give
algebra homomorphisms of the actual R305 order modulo 43^2.

Gaussian elimination is performed in (Z/43^2 Z)[i], using only pivots
whose reductions modulo 43 are nonzero. It yields

    rank(M modulo 43)=43,
    det M=687=q^21 modulo 43^2.                            (704.6)

There is also a conceptual check of the determinant and its sign. The
trace Gram identity of R305 gives M^t M with determinant q^42. Modulo
43, the cyclic regular representation has the single eigenvalue given
by evaluation at 1, because T^43-1=(T-1)^43. The circulant with entries
v_(n-j) therefore has determinant (sum v_j)^43=1. Replacing -j by j
permutes 21 pairs of columns, so the matrix (704.4) has determinant -1
modulo 43. Since q=-1 modulo 43 and 21 is odd, the two square roots
of q^42 are distinguished: the exact p-adic determinant is q^21.

The program also solves M e0=(1,0,...,0)^t. Its 43 normal-basis
coefficients are stored in the certificate. Their evaluations are
verified in all 43 rows, and their sum is 1. By (704.5) and invertibility
of M, e0 is the primitive idempotent for iota_0, and its Gamma translates
give all primitive idempotents. Consequently this is the full algebra
isomorphism

    O_{L_q} tensor_{Z[i]} (Z/43^2 Z)[i]
      -> product_{n=0}^{42} (Z/43^2 Z)[i],                 (704.7)

with every target factor ordered by (704.1).

## 4. Why this precision suffices for the R701 scalar field

Let F_s be the actual scalar p-field of R561. At p it has absolute
ramification index

    e(F_s,43)=44*43=1892.

R701 proves that values modulo varpi_s^1938 suffice for its local Kummer
quotient: the logarithm and exponential are inverse on U^46 and
(U^46)^43=U^1938. Here varpi_s is a uniformizer in F_s, not the r of the
degree-42 cyclotomic field.

The field L_q is unramified, in fact split, at p. Its R305 relative
discriminant q^42 is a p-adic unit. Thus after base change to the local
integer ring of F_s, its normal basis remains a full integral basis
of the product algebra of the 43 completions of M_s=F_s L_q. In
particular, if an actual p-integral element is written

    x=sum_j a_j u_j, a_j in O_{F_s,43},

then its n-th completion is

    x_n=sum_j a_j v_(n+j).                                (704.8)

The error in any v_j in (704.3) is divisible by 43^2, hence has
varpi_s-valuation at least 3784. It remains at least 3784 after the
integral linear combination (704.8), and 3784>1938. Therefore the
computed matrix already has more precision than the R701 local
Kummer calculation needs.

The integrality condition in this precision statement matters. An
unconverted coordinate representation with p-denominators would lose
precision; it must first be replaced by integral normal-basis coordinates
or accompanied by the extra precision its denominators require.

For the O-completed chi component, apply (704.8) to the actual raw
algebraic units and their specified conjugates before taking the
unaveraged Pplus combination in the local unit group. This matrix is
linear on field elements; it is not an instruction to confuse additive
coordinates of field elements with multiplicative unit tensors.

## 5. Exact remaining input and the large-q boundary

This calculation supplies the original 43 p-adic branches and the
entire evaluation map needed to transfer known normal-basis coordinates
into them. It does not supply the coordinates of the original units.
To form the R701 vector

    V_sc=pi^41 D_S c_s -11 a pi^40 c_q,

one still needs p-integral coordinates, or independently certified
local values to depth varpi_s^1938, of the same actual c_s and c_q.
In particular c_s must retain the s^11 shift from R561 and all units
must retain the original unaveraged Pplus, q, Weil, and Gamma markings.

The existing R198/R561 large finite-field outputs evaluate the pure-p
ancestors at q. They are not these p-local mixed Robert coordinates.
R311 defines the raw q-Robert unit by a product with exactly
42(q^2-1)/43 factors and explicitly does not evaluate that product.
The normalized isogeny distribution gives its full Gamma norm and,
at the mixed scalar level, the Euler relation

    N_Gamma c_s=(1-s^11)u_s.

Those equations alone give no partial q-orbit product or p-local
Gamma-resolved coordinates. A fast norm identity replacing the huge
partial product must be proved for the same unit and same phase before
it can be used as an evaluator. No q-torsion enumeration is proposed
as a runnable computation.

Hence C, eta_p, the actual 86 by 44 R701 matrix, m, and L are all still
unknown. The new result is a completed original-label evaluation map,
with a precise remaining unit-coordinate input.

## 6. Public execution, reproduction and sealed artifacts

The formal finite computation ran in the public repository's own GitHub Actions:
[run 43588220740](https://github.com/Rogerhu12/math-research-public/actions/runs/43588220740),
source commit `35bf247162bba1619698404b9996a22cf0dc52a9`.
The job completed all 43 embeddings, all 1849 original multiplication rows,
the determinant and every primitive-idempotent evaluation. Its output is
byte-identical to the development certificate.

The complete original return is preserved under
`computations/R704-marked-p-split-embeddings/43588220740-1/`:

- [Full 43-pair certificate, expanded-matrix hash and idempotent](../computations/R704-marked-p-split-embeddings/43588220740-1/r704_marked_p_split_embeddings_certificate.json).
- [Public completion receipt](../computations/R704-marked-p-split-embeddings/43588220740-1/summary.json)
  and [all input/source bindings](../computations/R704-marked-p-split-embeddings/43588220740-1/public-actions-input.json).
- [Sealed file manifest](../computations/R704-marked-p-split-embeddings/43588220740-1/files-manifest.json),
  including the exact original R191 and R305 inputs, arithmetic source,
  workflow and rule snapshots. All 14 manifest hashes were checked on return.

The arithmetic source is
[scripts/build_r704_marked_p_split_embeddings.py](../scripts/build_r704_marked_p_split_embeddings.py),
SHA256 `1d5b97d6b46f74a79484f5bf5239a6a5e86f7f875ca6900b3466f65359034f14`.
The complete finite certificate has SHA256
`3c6f8982a06846a4e1fb0fe641627738add0dc153e430ea9e793723aff30895d`.
The public wrapper consumes already completed identical results and does not
repeat their arithmetic merely for packaging.

Sources are the already published R191 §§1–3, R207, R305 §§1–5,
R311 §1.1, R561 §§1–3, and R701 §§1 and 6. The result uses their
fixed arithmetic inputs; no new general theorem or external
classification is assumed. Neither the original Robert local coordinates
nor C, m or L are assigned a numerical value here.
