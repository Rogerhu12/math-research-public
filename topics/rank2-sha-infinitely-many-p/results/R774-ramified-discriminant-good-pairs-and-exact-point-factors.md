# R774 — Arbitrary three-adic conductor: actual CM good pairs and the point-factor formula

Date: 2026-11-15. **Status: proved for each complete self-dual Hecke character specified in Theorem 1.** No bound on its conductor at the ramified prime of \(K=\mathbf Q(\sqrt{-3})\) is imposed. Application to the entire degree-\(174\) source of R772 still requires its actual finite CM decomposition and the original theta–Katz identity for each component. Those additional identifications are not assumed here.

The new step is an explicit auxiliary-pair construction. At the ramified prime \(3\), its companion twist is identically one, even when the target character has higher conductor. The auxiliary automorphic representation is principal series at every finite place, and its actual toric local periods can be nonzero on the split quaternion algebra. This supplies the ramification step that cannot be obtained merely by quoting the hypotheses of BDP Proposition 3.28.

## 1. Characters, periods, and statement

Put
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
\omega^2+\omega+1=0,\qquad \mathfrak d_K=(\delta).
\tag{1}
$$
A star is precomposition with the nontrivial automorphism of \(K\):
\(\eta^*(\mathfrak a)=\eta(\bar{\mathfrak a})\).
It is never an operation on an arbitrary \(p\)-adic scalar.

Let \(\nu\) be a complete algebraic Hecke character satisfying
$$
\operatorname{type}(\nu)=(1,0),\qquad
\nu\nu^*=\mathbf N_K,\qquad
\nu|_{\mathbf A_{\mathbf Q}^{\times}}
 =\epsilon_K\,\mathbf N_{\mathbf Q},\qquad
w(\nu)=-1.
\tag{2}
$$
The norm and infinity-type conventions are those of BDP [B2, §3A]. Its conductor \(\mathfrak f_\nu\) is invariant under conjugation. The exponent of \(\delta\) in \(\mathfrak f_\nu\) is arbitrary. Finite conductor at a chosen split ordinary prime
\(p=\mathfrak p\bar{\mathfrak p}>3\) is also allowed.

Let \(\psi_0\) be the Hecke character of
$$
E_0:y^2=x^3+1,\qquad \omega_0=dx/(2y),
$$
with the original ordinary embedding and period \(\Omega_{p,0}\). Define the **actual finite character**
$$
\rho_\nu=\psi_0/\nu,\qquad H_\nu=K^{\ker\rho_\nu}.
\tag{3}
$$
The two infinity types agree, so (3) is finite. Its central restriction is trivial and \(\rho_\nu^*=\rho_\nu^{-1}\).

**Theorem 1.** There is a tensor of algebraic points
$$
P_\nu\in
 \bigl(E_0(H_\nu)\otimes_{\mathbf Z}\mathbf Q\bigr)
       \otimes_K\overline{\mathbf Q}
$$
and an algebraic \(a_\nu\ne0\) such that
$$
(\sigma\otimes1)P_\nu=\rho_\nu(\sigma)P_\nu,\qquad
\boxed{\quad
\Omega_{p,0}\,\mathcal K(\widehat{\nu^*})
 =a_\nu\log_{\omega_0}(P_\nu)^2.
\quad}
\tag{4}
$$
Here \(\mathcal K\) is the original primitive Katz function with its actual local interpolation factors. The scalar is defined using algebraic differentials, the original CM period, the complete local-period factors, and finite-twist Gauss sums. It is not an unspecified specialization of a \(p\)-adic analytic unit.

A zero Katz value is included by taking \(P_\nu=0\). There is no assertion that every such value is nonzero, no assumed rank-one statement, and no assumed finiteness of a Tate–Shafarevich group.

If \(\rho_\nu\) is unramified at \(17\), the **point coordinate field** \(H_\nu\) in (4) is unramified at \(17\). The coefficient \(a_\nu\), and an algebraic square root of it, need not be unramified there. Galois in (4) acts only on the point factor.

The proof has three separate parts: a good pair with the correct companion sign, exact all-local CM factorization, and finite-twist descent in the same coefficient embedding.

## 2. A cyclic auxiliary character outside every prescribed finite set

Fix a finite set of rational primes containing those below \(\mathfrak f_\nu\), together with \(2,3,p,17,29\). Choose a split prime \(\ell>3\) outside this set and one prime \(\mathfrak l\mid\ell\).

Since \(K\) has class number one, an algebraic character of type \((1,0)\) with conductor supported on \(\mathfrak l\) can be constructed directly. Choose a character of
\((\mathcal O_K/\mathfrak l)^\times\) whose restriction to \(\mu_6\) is the chosen algebraic embedding of \(\mu_6\), and put, for ideals prime to \(\mathfrak l\),
$$
\psi((a))=a\,\tau(a)^{-1}.
\tag{5}
$$
Changing a generator by a unit leaves (5) unchanged. One can replace \(\mathfrak l\) by a higher power if needed. The conductor is cyclic: only one prime in each split pair occurs. In particular \(\psi\) is unramified at every inert or ramified rational prime and at the chosen ordinary \(p\).

Set
$$
\xi=\psi/\nu,\qquad
\nu'=\psi^*\xi^{-1}
    =\frac{\psi^*}{\psi}\,\nu.
\tag{6}
$$
Then \(\xi\) is finite, \(\psi\xi^{-1}=\nu\), and
$$
\operatorname{type}(\nu')=(0,1),\qquad
\nu'(\nu')^*=\mathbf N_K.
\tag{7}
$$
The auxiliary character \(\xi\), unlike \(\psi\), retains all the old conductor of \(\nu\), including its full conductor at \(3\) and at \(p\).

The choice will be varied below to obtain
$$
L(\nu',1)\ne0.
\tag{8}
$$
Neither (5) nor the proof of (8) changes the target \(\nu\).

## 3. The companion sign, including every old three-adic conductor

Write \(\theta=\psi^*/\psi\). It is anticyclotomic. We compute the quotient of the root numbers of \(\nu'=\theta\nu\) and \(\nu\), using the same global additive character and its induced local characters.

### 3.1 Old nonsplit places

At an inert place, an unramified character of \(K_v^\times\) is invariant under conjugation: it is trivial on units and its valuation is unchanged. Hence \(\theta_v=1\).

At the ramified place \(v=(\delta)\), the same conclusion holds. In particular
\(\bar\delta=-\delta\), and \(-1\) is a unit, so
$$
\psi_v(\bar\delta)=\psi_v(\delta),\qquad
\boxed{\theta_v=1.}
\tag{9}
$$
Thus the epsilon factor of \(\nu_v\) is unchanged for **every** conductor exponent. No assumption
\(\mathfrak d_K\Vert\mathfrak f_\nu\) occurs in (9).

The conductor of the additive character at \(3\) is also irrelevant to this comparison: the two multiplicative characters being compared there are exactly equal.

### 3.2 Old split places

Let \(v,\bar v\) be a split pair outside the auxiliary conductor. The character \(\theta\) is unramified at both places and
\(\theta_v(\varpi)\theta_{\bar v}(\varpi)=1\).
Self-duality gives the same conductor exponent for \(\nu_v\) and \(\nu_{\bar v}\). The formula for twisting a Tate epsilon factor by an unramified character therefore gives two inverse powers. Their product is one. This also handles the chosen ordinary primes when \(\nu\) is \(p\)-ramified.

### 3.3 New one-sided split conductor

At a new auxiliary split pair, \(\nu\) is unramified and the two ramified unit characters in \(\theta\nu\) are inverse. After unitary normalization the two remaining unramified parameters are inverse as well. The product of the two local Gauss sums is therefore precisely the parity factor
$$
\psi_{\mathfrak l}(-1).
\tag{10}
$$
The same calculation applies at every auxiliary split pair after the variation below. No extra factor depending on the conductor exponent survives.

At the complex place the normalized types are \(z/|z|\) and its inverse. Their Tate epsilon factors are equal: with the standard additive character both are \(i\). Thus changing \((1,0)\) into \((0,1)\) contributes no quotient sign.

Finally the principal idele \(-1\) gives
$$
\prod_{\mathfrak l\mid\mathfrak f_\psi}
     \psi_{\mathfrak l}(-1)=-1,
\tag{11}
$$
because the infinity component has value \(-1\), while every other finite component of \(\psi\) is unramified. Combining (9)–(11),
$$
\boxed{w(\nu')=-w(\nu)=+1.}
\tag{12}
$$

This is a direct local calculation. It replaces the use of BDP Remark 3.20 at the ramified discriminant and does not enlarge the hypotheses of that remark by notation.

## 4. A nonzero companion and its correct Katz argument

Choose another auxiliary split prime, outside the preceding finite set. Vary \(\psi\) by finite characters \(\alpha\) of the one-sided split-prime \(\mathbf Z_\ell\)-extension, and vary \(\xi\) by the same \(\alpha\). Then
$$
\psi\alpha\,(\xi\alpha)^{-1}=\nu,\qquad
\nu'_\alpha=\nu'\,\alpha^*/\alpha.
\tag{13}
$$
For \(\ell>3\), class number one and the split local units show that
\(\alpha^*/\alpha\) runs through the anticyclotomic \(\ell\)-power characters. Equivalently one can use the one-sided ray-class construction in [B2, proof of Proposition 3.28, Step 2]. The unit group contributes no \(\ell\)-torsion.

The character \((\nu')^*\) has type \((1,0)\) and sign \(+1\). The Greenberg–Rohrlich nonvanishing statement recorded in [B2, Lemma 3.29] therefore supplies a variation for which (8) holds. After this choice, the cyclic conductor of \(\psi\) still avoids all prescribed old primes. The complete pair \((\psi,\xi)\) is now fixed.

The Katz factor paired with the target is **not** \(\mathcal K(\nu')\). It is
$$
\boxed{
\vartheta=\psi^{*-1}\xi\mathbf N_K
 =\mathbf N_K/\nu'=(\nu')^*,
\qquad \operatorname{type}(\vartheta)=(1,0).
}
\tag{14}
$$
It lies in the genuine interpolation region. Its interpolated classical value is
$$
L(\vartheta^{-1},0)=L(\nu',1)\ne0.
\tag{15}
$$

For conductor zero at \(p\), the actual Katz factor in the conventions of [B2, (3-1)] is
$$
E_p(\vartheta)
 =\bigl(1-\vartheta(\mathfrak p)/p\bigr)
  \bigl(1-\vartheta(\bar{\mathfrak p})^{-1}\bigr)
 =\bigl(1-\vartheta(\bar{\mathfrak p})^{-1}\bigr)^2.
\tag{16}
$$
It is nonzero, since the complex absolute value of a weight-one Frobenius root is \(p^{1/2}\). At positive conductor the interpolation formula uses its actual nonzero local Gauss factor and uniformizer power; the corresponding ramified local \(L\)-factor is one. A ramified Gauss factor is not inserted into (16) by a limiting convention.

The same statement holds for the finite Euler factors restored in passing from an imprimitive to the primitive Katz function. Here their possible nontrivial eigenvalues have absolute value \(q^{\pm1/2}\), so the restored factors do not vanish.

The finite-twist period formula then gives
$$
\boxed{
\mathcal K(\widehat\vartheta)
 \in \overline{\mathbf Q}^{\,\times}\,\Omega_p(\nu^*).
}
\tag{17}
$$
Indeed \(\vartheta^*=\nu^*\xi^*/\xi\), and \(\xi^*/\xi\) is finite. Its differential and CM period change by a nonzero algebraic generalized Gauss sum [B2, Lemmas 2.8 and 2.14]. This includes finite ramification at the chosen \(p\).

## 5. The finite quaternion and actual local toric vectors

Let \(\pi_\psi\) be the unitary automorphic induction of \(\psi\). It is cuspidal because the two infinity types of \(\psi\) and \(\psi^*\) differ.

At a split finite place, \(\pi_{\psi,v}\) is a principal series. At a nonsplit place, \(\psi_v\) is unramified and invariant under the local conjugation. It extends to a character of \(F_v^\times\), and its induced Weil parameter is the sum of this extension and its product with the quadratic character of \(K_v/F_v\). Thus here too \(\pi_{\psi,v}\) is a principal series. This applies at the ramified prime \(3\), although one of the two characters on \(F_3^\times\) may be ramified.

Consequently the global quaternion algebra used below is
$$
B=M_2(\mathbf Q).
\tag{18}
$$
We do not transfer a principal series to a division algebra, where it has no Jacquet–Langlands transfer.

For completeness, the required local distinction can be checked without a conductor shortcut. If \(T=K_v^\times\) is nonsplit, it acts transitively on
\(\mathbf P^1(F_v)\), and the stabilizer is \(F_v^\times\). Restricting a principal series with central character \(\omega_\pi\) to \(T\) gives the smooth induced representation from this central character. Hence every character of \(T\) compatible with the center occurs, and the toric Hom is nonzero. The assertion is independent of its conductor.

At a split place, the open orbit in the Kirillov model gives the nonzero Mellin functional. Our normalized characters are unitary; the nonunitary boundary characters of the two closed orbits do not create an exceptional obstruction. In the LZZ normalization the compatibility is
$$
\omega_{\pi_\psi}\,
       \xi^{-1}|_{\mathbf A_{\mathbf Q}^{\times}}=1,
\tag{19}
$$
which follows directly from (2) and \(\xi=\psi/\nu\).

All finite characters and inducing parameters are algebraic. The vectors can therefore be chosen in the algebraic model. For a nonsplit place the torus quotient is compact, and the finite character projector is a finite sum on a sufficiently small open subgroup. At a split place one can choose compact support in the actual Kirillov coordinate. Choosing the paired dual vector makes the complete normalized local toric period nonzero.

At \(p\), choose LZZ \(n\)-admissible stable vectors, with \(n\) at least the actual conductor exponent. Their factor is
$$
Q_p(f_+,f_-;\xi^{-1})
 =
 \frac{L(1/2,\pi_{\psi,p}\otimes
                    \xi^{-1}_{\bar{\mathfrak p}})^2}
      {\varepsilon(1/2,\Psi_{p,\mathrm{add}},
                    \pi_{\psi,p}\otimes
                    \xi^{-1}_{\bar{\mathfrak p}})}
 \,\alpha_{\xi^{-1},p}(f_+,f_-).
\tag{20}
$$
The additive character, Haar measures and bilinear pairing are exactly those in LZZ. At every other finite place one retains the analogous normalized local matrix-coefficient factor \(Q_v\), including the full factor at \(3\). They are algebraic and may be made nonzero. They are not replaced by \(1\) when the target character is ramified.

The relevant assertions about these distributions are [L, Lemmas 4.1.8–4.1.9 and Proposition 4.1.6]. The preceding principal-series calculation verifies their nonzero-local-Hom hypothesis for the pair actually constructed here.

## 6. Exact CM factorization with the ramified local factors retained

We give the normalization argument explicitly. It is needed because an equality up to an arbitrary Iwasawa unit would not suffice for an algebraic point-factor coefficient.

Normalize \(\theta_\psi\) by its algebraic \(q\)-expansion, choose algebraic parametrizations and differentials on its modular abelian variety and dual, and use the same CM differential for the Katz periods. The classical factorization is the identity of local Euler factors
$$
L(\theta_\psi,\Xi^{-1},s)
 =L(\psi\Xi^{-1},s)\,
  L(\psi^*\Xi^{-1},s).
\tag{21}
$$
At the finite point the two Katz arguments are exactly
$$
\psi^{-1}\xi\mathbf N_K=\nu^*,\qquad
\psi^{*-1}\xi\mathbf N_K=\vartheta.
\tag{22}
$$

Compare the positive-weight interpolation formula in [L, Proposition 4.3.4] with the two Katz interpolation formulas, retaining all \(Q_v\) and (20). The varying archimedean gamma factors are
\(\Gamma(j+1)\Gamma(j+2)\), the product of the two Katz gamma factors. Their CM period powers likewise cancel in the product. At split \(p\), the two local Euler polynomials and the ramified Gauss factors factor according to (21); no new analytic factor is introduced by this operation.

There is a useful precise way to calibrate the fixed constant, including the Petersson/adjoint term in LZZ. Keep this same \(\psi\), its algebraic differential and its algebraic Fricke-dual differential. Choose a reference self-dual target with discriminant exponent one, for example the original \(E_{17^2}\) character. Our auxiliary conductor avoids its bad primes. On this reference component [B2, Theorem 3.17, (3-15)] is the exact CM comparison. Its constant is the algebraic Atkin–Lehner/ideal-evaluation factor times
$$
\frac{w_K}{2c^{\,k+2j-1}}
  \prod_{\ell\mid c}\frac{\ell-\epsilon_K(\ell)}{\ell-1}.
\tag{23}
$$
The differential-composition pairing in LZZ is the same pairing; its Petersson and adjoint term is fixed by \(\pi_\psi\) and these differentials, not by the finite toric character.

Now change the finite character from that reference to the actual \(\xi\). The fixed representation, differentials, pairing and gamma calculation are unchanged. The changes in the interpolation formulas are exactly:

| Place or normalization | Actual change |
|---|---|
| Ramified finite primes, including \(3\) | the \(Q_v\) matrix-coefficient integral, finite Gauss factors, rational Haar volumes and local Euler polynomials |
| Chosen ordinary \(p\) | (20), with the actual conductor, and the two Katz local interpolation factors |
| CM differentials of finite twists | nonzero algebraic generalized Gauss sums |
| Ideal representatives and Fricke normalization | finite character evaluations and algebraic powers |
| Infinity | the same two gamma factors and the same CM period powers |

These entries are the explicit local operations in (21) and LZZ's interpolation formula. Their finite-character specializations are algebraic. The fixed constant calibrated by (23) is unchanged. In particular the fact that the new character has \(\delta^a\)-conductor does not introduce an uncalibrated period.

On each finite tame component, positive algebraic weights with its prescribed congruence class accumulate in the corresponding rigid weight disc. The above *explicit* comparison therefore extends to the finite-character point. This uses LZZ's actual toric distributions and local \(Q\)'s, not just equality of two principal ideals in an Iwasawa algebra. A finite wild character is a point on that disc; no approximation of its root of unity by integer powers is being asserted.

It follows that, for the algebraic good vectors of §5,
$$
\log_{\omega_+}P^+_{\xi^{-1}}(f_+)\,
\log_{\omega_-}P^-_{\xi^{-1}}(f_-)
 =
 b_{\psi,\xi}\,
 \mathcal K(\widehat{\nu^*})\,
 \mathcal K(\widehat\vartheta),
\qquad b_{\psi,\xi}\in\overline{\mathbf Q}^{\,\times}.
\tag{24}
$$
The coefficient includes the complete factors of the table. It is defined before deciding whether the target is zero. Combining with (17),
$$
\Omega_p(\nu^*)\,\mathcal K(\widehat{\nu^*})
 =
 e_{\psi,\xi}\,
 \log_{\omega_+}P^+_{\xi^{-1}}(f_+)\,
 \log_{\omega_-}P^-_{\xi^{-1}}(f_-),
\qquad e_{\psi,\xi}\in\overline{\mathbf Q}^{\,\times}.
\tag{25}
$$
The equality (25) also holds if its target value is zero.

## 7. Actual points and the two coefficient embeddings

LZZ [Theorem 3.3.2 and Proposition 4.3.6] identifies the periods in (24) with logarithms of finite sums of algebraic CM points. Its tame level may include all of the actual conductor at \(3\). Its torus measure has total volume \(2\), so finite sums retain the \(\mu_6\) stabilizers of \(K\).

The identification of the two factors is as important as their product. In the same coefficient embedding, the holomorphic characters of the modular abelian factor and its dual are
$$
\psi^+=\psi,\qquad \psi^-=\mathbf N_K/\psi^*.
\tag{26}
$$
Choose the positive CM locus with reciprocity \(t\mapsto st\); on the conjugate negative locus the action is \(t\mapsto\bar s\,t\). For the toric character \(\xi^{-1}\) this gives:

| Factor | Holomorphic character | Coefficient in the finite sum | Point-only character |
|---|---|---|---|
| Positive | \(\psi\) | \(\xi^{-1}(t)\) | \(\xi\) |
| Negative | \(\mathbf N_K/\psi^*\) | \(\xi(t)\) | \((\xi^*)^{-1}\) |

Finite-twist descent takes a CM character \(\eta\) and point-only character \(\tau\) to \(\eta\tau^{-1}\). Hence the two descended characters are
$$
\psi\xi^{-1}=\nu,\qquad
\frac{\mathbf N_K}{\psi^*}\,\xi^*
  =\frac{\mathbf N_K}{\nu^*}=\nu.
\tag{27}
$$
Both point factors therefore land in the same holomorphic \(\nu\)-component. Neither complex conjugation of a \(p\)-adic number nor an equality of \(\rho\) and \(\rho^{-1}\) eigenspaces was used.

The finite-twist isogenies and differential comparisons in [B2, §2B, Lemmas 2.8–2.9] are algebraic and have no discriminant-exponent-one assumption. Thus all auxiliary split conductors disappear from the **descended point object**, not from a guess based on the modular level.

If the target in (25) is nonzero, both logarithms are nonzero, so a corresponding Heegner point is nontorsion. The general Gross–Zagier formula, with the nonzero local factors already verified in §5, gives
$$
L'(\theta_\psi,\xi^{-1},1)
 =L'(\nu,1)\,L(\nu',1)\ne0.
\tag{28}
$$
For the implication from a nonzero point, pair it with its polarization conjugate; the canonical height is positive on a nontorsion point. One does not assume positivity of an arbitrary bilinear test-vector pairing.

Since the companion is nonzero, \(L'(\nu,1)\ne0\). The Gross–Zagier–Kolyvagin–Logachev rank-one consequence for this CM component now applies, exactly as in the point-descent argument of [B2, Lemma 3.25]. The input is the actual generalized Heegner point; the general Gross–Zagier formula allows the ramification under consideration. An auxiliary ordinary prime outside \(\mathfrak f_\nu\) may be used for that classical rank argument. It is not a claim that the finite twist is crystalline at our chosen \(p\).

Therefore the two descended points in (27) are algebraic multiples of a generator of the same CM point line. Equation (25) becomes
$$
\Omega_p(\nu^*)\,\mathcal K(\widehat{\nu^*})
 =e_\nu\,\log_{\omega_\nu}(Q_\nu)^2,
\qquad e_\nu\in\overline{\mathbf Q}^{\,\times}.
\tag{29}
$$
If the target is zero, take \(Q_\nu=0\). Thus rank one was derived in the nonzero case rather than imposed as a hypothesis.

## 8. Exact descent to the base elliptic curve and the field at 17

By (3), \(\nu=\psi_0\rho_\nu^{-1}\). The finite-twist isogeny identifies its CM point component with
$$
\left(
 E_0(H_\nu)\otimes_{\mathbf Z}\mathbf Q
       \otimes_K\overline{\mathbf Q}
\right)^{\rho_\nu},
\tag{30}
$$
where superscript denotes action on the point factor only. The differential and period comparisons are nonzero algebraic multiples, including their actual finite Gauss sums. Replacing the differential and period in (29) by \(\omega_0,\Omega_{p,0}\) proves (4).

In particular, if \(\nu/\psi_0\) is trivial on the local units at \(17\), (30) is defined over a field unramified at \(17\). This assertion remains true even if its expression uses coefficients ramified at \(17\).

For a complete original eigen-source \(F\), suppose its **already verified** theta–Katz identity at a finite physical character is
$$
\mathcal K(\widehat{\nu^*})
  =c_{F,\chi}\,\Omega_{p,0}\,
       I_{F,\chi}^{\,2},
\qquad c_{F,\chi}\in\overline{\mathbf Q}^{\,\times}.
\tag{31}
$$
Then (4) gives
$$
\Omega_{p,0}I_{F,\chi}
 \in\overline{\mathbf Q}\,
       \log_{\omega_0}
       \left(E_0(H_\nu)_{\mathbf Q}
                  \otimes_K\overline{\mathbf Q}\right)^{\rho_\nu}.
\tag{32}
$$
The choice of sign of an algebraic square root is immaterial for this membership statement. It does not specify a simultaneous linear map as \((F,\chi)\) varies.

Finite sums with algebraic coefficients may be combined in a common finite point field. There is no passage here to arbitrary infinite \(p\)-adic sums, moving gate limits, or the full logarithm expansion. The limitation of R753 remains in force.

## 9. Exact scope for the P58 source

R772 has already paid the degree-\(174\) source, its complete finite \(p\)-gate expansion, its positive orthogonal companion jets, and its unramified \(17\)-local lattice after the explicit \(b=17\) period scaling.

The present theorem removes one separate obstruction: a component satisfying (2) is no longer excluded merely because its actual three-adic conductor is larger than \((\delta)\).

It does **not** do the following additional work by assumption:

- replace the entire degree-\(174\) source by the \(58\)-dimensional pullback subspace;
- identify its three-dimensional local factor by a conductor guess;
- identify every finite CM eigensection and its actual metaplectic splitting;
- assign sign \(-1\) to a target before computing its complete finite character;
- replace the actual theta identity (31) by the existence of a favorable auxiliary vector;
- discard the mixed P gates or the complement in R772 (30);
- infer a conditional P-negative-one zero from the two original central zeros.

The ideal underlying the three-primary Heisenberg factor of the standard index \(174\) is \((3)=\delta^2\), and its norm-one unit group has order \(6\). Its absolute Weil action and its splitting still have to be used to identify the characters. The preceding proof does not need an answer to that finite enumeration, and does not label it \(\delta^3\) without calculation.

Thus the good-pair and point-factor theorem is complete now; its use for every term of R772 remains tied to the actual finite source identity (31).

## References and proof dependencies

- [R748](R748-original-type-five-ramified-good-pair-and-point-eigenspaces.md): the original finite-\(p\) two-line formula, exact period convention, and the two CM-locus descent table. The new proof above replaces its discriminant-exponent-one auxiliary-pair input.
- [R772](R772-original-p58-orthogonal-weight-and-full-finite-schwartz-source.md): the actual P58/degree174 source and the complete finite-domain statement.
- [R749](R749-point-factor-projectors-and-finite-character-extraction.md): point-only projectors after a genuine algebraic point-space identity.
- R753: the finite-carrier restriction on limits.
- [B2] M. Bertolini, H. Darmon, K. Prasanna, *p-adic Rankin L-series and rational points on CM elliptic curves*, Pacific J. Math. 260 (2012), 261–303. [Author PDF](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf). Used here: the general finite-twist constructions in §2B–2C; the exact factorization at a reference component in Theorem 3.17; Greenberg–Rohrlich as Lemma 3.29; and the Gross–Zagier/point-descent argument of Lemma 3.25 and Remark 3.26. Its original conductor restriction is not silently removed.
- [L] Y. Liu, S. Zhang, W. Zhang, *A p-adic Waldspurger formula*, Duke Math. J. 167 (2018), 743–833. [Author-hosted published PDF](https://web.math.princeton.edu/~shouwu/publications/pWalds.pdf). Used here: Theorem 3.3.2, Lemmas 4.1.8–4.1.9, Proposition 4.3.4, Corollary 4.3.5, and Proposition 4.3.6, with their full local period.
- Tate's local epsilon identities used in §3 are the unramified-twist formula and the product formula for a finite character and its inverse. The old ramified-place calculation is the exact identity (9), so no omitted high-conductor Gauss calculation is hidden there.

This is a proof from the displayed local identities and the cited primary theorems. No numerical scan, auxiliary finite-field rank test, or new computational certificate is used.
