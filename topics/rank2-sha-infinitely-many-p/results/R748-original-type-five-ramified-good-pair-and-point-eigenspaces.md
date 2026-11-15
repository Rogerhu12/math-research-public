# R748. The two original type-five lines at every finite p-character: good pairs, algebraic point logarithms, and point-factor idempotents

**Status.** Proved for the two complete eigen-sources $D_{2,17}$ and $D_{4,17}$ identified in R735, with every finite character allowed in R746. The proof allows arbitrary finite conductor at the chosen ordinary prime. It does not assume analytic rank one or finiteness of a Tate--Shafarevich group. It does not identify an arbitrary section in the full degree-$34$ theta space with either of these two sources.

The conclusion is a membership statement in a space of logarithms of algebraic points, with its actual finite Galois eigensector. It is not a choice of compatible square roots as the character varies. In particular it does not give a linear universal point map with specified coefficients for the complete space in R745.

## 1. Fixed original data and the precise assertion

Use the notation and the absolute source and period normalization of R735 and R746. Thus

$$
K=\mathbf Q(\omega),\qquad
\delta=1+2\omega,\qquad
\theta=17^{1/6},\qquad
E_k:y^2=x^3+17^k,\quad k\in\{2,4\}.
\tag{1}
$$

The prime $p$ is an ordinary prime in the original ray; in particular $p>19$, $p\nmid 2\cdot3\cdot17$, and $p=\mathfrak p\bar{\mathfrak p}$ in $K$. Fix the original embedding at $\mathfrak p$, the original period $\Omega_p$, and the Hecke character $\psi_k$ of $E_k$. Let $\omega_k=dx/(2y)$. The isomorphism to the common curve $E_1:y^2=x^3+1$ is

$$
\phi_k(x,y)=(\theta^{-2k}x,\theta^{-3k}y),\qquad
\phi_k^*\omega_1=\theta^k\omega_k.
\tag{2}
$$

Here $E_1$ in (2) denotes the common $b=1$ curve, not the curve indexed by $k=1$ in a sextic family. The corresponding periods are

$$
\Omega_{p,0}=\theta\Omega_p,\qquad
\Omega_{p,E_k}=\theta^{-k}\Omega_{p,0}
             =\theta^{1-k}\Omega_p.
\tag{3}
$$

For a finite character $\chi:\mathbf Z_p^\times\to\overline{\mathbf Q}^{\,\times}$, put

$$
I_{k,\chi}
 =\int_{\mathbf Z_p^\times}x^{-1}\chi(x)\,d\mu_{D_{k,17}}(x).
\tag{4}
$$

R746 proves that (4) is zero if $\chi|_{\mu_6}\ne1$. For the remaining characters define the global character

$$
\Gamma_k=\widehat\psi_k/\widehat{\bar\psi}_k,\qquad
\rho_\chi=\chi\circ\Gamma_k,\qquad
H_\chi=K^{\ker\rho_\chi}.
\tag{5}
$$

All character values are embedded by the original algebraic embeddings. Geometric reciprocity gives

$$
\rho_{\chi,\mathfrak p}(u)=\chi(u)^{-1},\qquad
\rho_{\chi,\bar{\mathfrak p}}(u)=\chi(u)
\quad (u\in\mathbf Z_p^\times).
\tag{6}
$$

In particular $\chi\ne1$ if and only if $\rho_\chi\ne1$. R746 also proves that $H_\chi/K$ is unramified away from the two primes above $p$, including at $2,3,17$. Its conductor at the two ordinary primes is the actual conductor of $\chi$; it is not replaced by an arbitrary larger level.

**Theorem 1.** For every surviving $\chi$, there are

$$
P_{k,\chi}\in E_k(H_\chi)_{\mathbf Q}\otimes_K\overline{\mathbf Q},
\qquad
\epsilon_{k,\chi}\in\overline{\mathbf Q}^{\,\times}
\tag{7}
$$

such that

$$
(\sigma\otimes1)P_{k,\chi}
 =\rho_\chi(\sigma)P_{k,\chi}
\quad\text{for }\sigma\in\operatorname{Gal}(H_\chi/K),
\tag{8}
$$

and, in the original primitive Katz normalization,

$$
\mathcal K_{34\delta}
   \bigl(\widehat{\bar\psi}_k\rho_\chi\bigr)
 =
 \epsilon_{k,\chi}\,
 \Omega_{p,E_k}^{-1}
 \log_{\omega_k}(P_{k,\chi})^2.
\tag{9}
$$

A zero value on the left is included: one may then take $P_{k,\chi}=0$. No nonvanishing for all finite $\chi$ is asserted.

Consequently there is $a_{k,\chi}\in\overline{\mathbf Q}^{\,\times}$, with an arbitrary algebraic choice of its sign, for which

$$
\boxed{\quad
\Omega_p I_{k,\chi}
 =a_{k,\chi}
   \log_{\omega_1}\bigl(\phi_kP_{k,\chi}\bigr).
\quad}
\tag{10}
$$

More precisely, the nonzero scalar can be chosen to satisfy

$$
a_{k,\chi}^{\,2}
 =
 \frac{\epsilon_{k,\chi}\chi(34)}
      {34c_k}\,\theta^{-k-12},
\tag{11}
$$

where $c_k$ is the fixed algebraic scalar of R735/R746. Thus no $p$-adic Iwasawa unit has been absorbed into an alleged algebraic coefficient.

Throughout, $E_k(H)_{\mathbf Q}=E_k(H)\otimes_{\mathbf Z}\mathbf Q$; expressions involving a tensor product over $K$ use this rational point space first. The tensor product in (7) uses the original CM action of $K$. A point in this tensor product is a finite algebraic linear combination of actual algebraic points. Formula (9), and therefore (10), uses the extension of the logarithm by this scalar action.

## 2. The good pair is chosen for the actual p-ramified character

Set

$$
\nu=\psi_k\rho_\chi^{-1}.
\tag{12}
$$

This character has infinity type $(1,0)$, satisfies $\nu\nu^*=\mathbf N_K$, and has the same central restriction as $\psi_k$. The finite character $\rho_\chi$ is anticyclotomic and is trivial on rational ideles.

The conductor at $2,3,17$ in (12) is the original conductor of $\psi_k$. In particular the ramified discriminant ideal $(\delta)$ occurs exactly once. If $\chi$ has positive conductor $p^n$, the new conductor is at the two split ordinary primes, both of exponent $n$. These statements include the nontrivial tame characters; they are not statements only about characters of $p$-power order.

The sign in the functional equation of $\nu$ is $-1$. To check that the twist has not changed the original sign, consider the two split local factors at $p$. The normalized unramified parameters are inverse on the two factors and the finite characters are $\chi,\chi^{-1}$. The product of their Tate epsilon factors differs from the untwisted product by $\chi(-1)$. This is $1$, since $\chi|_{\mu_6}=1$. All other local factors are unchanged.

Choose a good pair $(\psi,\xi)$ with

$$
\psi\xi^{-1}=\nu,\qquad
\psi\text{ of type }(1,0),\qquad
\xi\text{ finite},\qquad
L(\psi^*\xi^{-1},1)\ne0.
\tag{13}
$$

The conductor $\mathfrak m$ of $\psi$ is cyclic and can be required to be prime to $2\cdot3\cdot17\cdot p$ and to the conductor of $\nu$. In particular $f=\theta_\psi$ is ordinary and unramified at the chosen $p$. Its classical level is $|D_K|\mathbf N\mathfrak m$, and the cyclic ideal $\delta\mathfrak m$ supplies the Heegner embedding.

Here the finite character $\xi$, unlike $\psi$, is allowed to have conductor at $p$. This distinction is essential.

The existence assertion follows from the construction in BDP [B2, Proposition 3.28], not from a nonvanishing assertion for the original curve. Start with a cyclic conductor outside the finite forbidden set and take $\xi=\psi/\nu$. Then vary $\psi,\xi$ together by characters of a one-sided auxiliary split-prime extension, at an auxiliary prime different from $p$. The companion in (13) varies by the associated anticyclotomic characters. Its sign is $+1$, and the Greenberg--Rohrlich statement used in [B2, Lemma 3.29] supplies a nonzero companion value. The auxiliary primes can avoid any prescribed finite set.

The classical construction makes sense when $\nu$ is ramified at the distinguished $p$. Equivalently one can first carry out [B2, Proposition 3.28] with another ordinary prime outside the conductor of $\nu$, also imposing avoidance of our $p$ in the initial cyclic conductor and in the auxiliary split primes. No theorem about reduction of $B_\nu$ at our $p$ is being inferred in this argument.

Write

$$
\xi_0=\psi/\psi_k,\qquad \xi=\xi_0\rho_\chi.
\tag{14}
$$

Thus the original $p$-ramification resides in $\rho_\chi$, while the tame part of the auxiliary pair is fixed during its local weight-space comparison.

## 3. Exact normalization of the Rankin--Katz comparison

We record the normalization argument because an equality only up to an unspecified element of an Iwasawa algebra would be insufficient for (9).

All modular forms below are normalized by their algebraic $q$-expansions. All modular parametrizations and differentials are algebraic. The CM differential used to define the two Katz periods is the same one used in the toric period. Changing these choices multiplies the displayed comparisons by explicitly algebraic factors.

### 3.1 The crystalline calculation

For $f=\theta_\psi$, the classical Rankin factorization is

$$
L(f,\Xi^{-1},s)
 =L(\psi\Xi^{-1},s)L(\psi^*\Xi^{-1},s).
\tag{15}
$$

The exact comparison in [B2, Theorem 3.17, equation (3-15)] is used with this normalization. Its factor is

$$
w(f,\Xi)^{-1}\,
 \frac{w_K}{2c^{\,k+2j-1}}
 \prod_{\ell\mid c}
       \frac{\ell-\epsilon_K(\ell)}{\ell-1},
\tag{16}
$$

with $k=2$ here. In this crystalline comparison, $c$ denotes the fixed conductor away from $p$; the $p$-primary conductor is varied in the local character and is handled by (17), not inserted into $c$ in (16). The scalar $w(f,\Xi)$ is not an anonymous unit: [B1, equation (5.1.11), Lemma 5.3] expresses it using the algebraic Atkin--Lehner scalar, a finite character value on a fixed ideal, and algebraic powers of fixed elements. In particular its finite-character specializations are algebraic and nonzero.

In the positive-weight calculation the two gamma factors are
$\Gamma(j+1)\Gamma(j+2)$. These are precisely the product of the two Katz gamma factors. The powers of the common CM periods cancel in the product. At $p$, the Rankin Euler polynomial factors as the product of the two Hecke Euler factors; both sides square this same product. Thus none of these factors may be replaced by a free analytic unit.

The tame local correction factors consist of finite character values, rational local volumes and Euler polynomials at fixed primes. They are rational functions over $\overline{\mathbf Q}$ of the relevant character values. If an imprimitive normalization is used temporarily, its exact missing Euler factors are retained and restored to the primitive normalization before (9).

### 3.2 Extension at the chosen ordinary place

The objects used for this extension are the actual toric distributions of LZZ [L, Theorem 2.3.17 and Section 4.2]. In their Kirillov model an $n$-admissible stable vector has support on $1+p^n$; all its coefficients can be chosen in $\overline{\mathbf Q}$. Take $n$ at least the conductor exponent of $\xi_{\mathfrak p}$.

The plus and minus vectors are paired with algebraic invariant differentials on the modular abelian variety and its dual. Their product is divided by the actual local-period distribution of [L, Proposition 4.1.6 and Lemma 4.1.9]. At a finite character $\kappa=\xi^{-1}$, its $p$-part is

$$
Q_p(f_+,f_-;\kappa)
 =
 \frac{L(1/2,\pi_p\otimes\kappa_{\bar{\mathfrak p}})^2}
      {\varepsilon(1/2,\Psi_p,\pi_p\otimes
                              \kappa_{\bar{\mathfrak p}})}
 \,\alpha_{\kappa,p}(f_+,f_-).
\tag{17}
$$

Here $\Psi_p$ is the fixed additive character, not the auxiliary Hecke character $\psi$. The Haar measures and the matrix coefficient pairing are those of LZZ. Local multiplicity one and the nonvanishing assertion of [L, Lemma 4.1.9] allow the algebraic vectors to be chosen so that (17) and the complete local product are nonzero.

Every quantity in (17) is algebraic at a finite $\kappa$. For positive conductor the local $L$-factor is $1$, and the epsilon factor is a nonzero finite Gauss sum times the displayed algebraic uniformizer powers. For conductor zero the ordinary Euler factors are retained. They are nonzero in this weight-one CM setting: an equality forcing a Frobenius root to be a finite-order unit or the corresponding integral norm would contradict its complex absolute value. The normalization at conductor zero is therefore not obtained by inserting a ramified Gauss factor by convention.

The complete Rankin--Katz comparison is obtained by the following exact operation. Compare [L, Proposition 4.3.4] with the calculation (15)--(16), in the common algebraic differential normalization, and retain (17) and its tame analogues. The variable gamma factors and period powers cancel as in Section 3.1. The remaining variable factors are character evaluations on fixed ideles, algebraic powers, and the displayed local distributions. The fixed factor is algebraic: the modular differential and its $q$-expansion differ by an algebraic scalar, and the Atkin--Lehner and polarization normalizations in [B1, Section 5.1] are algebraic. This is the same normalization calculation underlying the exact formula (3-15), rather than the weaker Iwasawa-ideal version of that formula.

One can make the comparison without choosing a transcendental Petersson scalar. Begin with algebraic parametrizations whose pulled-back differentials are the normalized $\theta_\psi$ form and its algebraic Fricke-dual form. The calculation of [B1, Section 5.1] identifies their classical toric product with the square used in [B2] up to the explicitly algebraic phase in (16). In [L, Proposition 4.3.4], the same pulled-back differentials define the two archimedean periods; its canonical composition pairing cancels the Petersson/adjoint factor. The remaining gamma factors are the two gamma factors already displayed above. This accounts for the fixed period normalization, as well as the variable local factors. If a different admissible local vector is required, division by its actual $Q$ factor in [L, Corollary 4.3.5] gives the same comparison.

This comparison is an identity of rigid analytic toric distributions. On each relevant tame component, positive algebraic weights have an interior accumulation point. Hence the crystalline calculation extends to the finite-character point on that component. In particular it extends to all its wild finite characters. No approximation of a wild root of unity by integer exponents is being asserted. This is the same distinction used in R746.

It follows, in particular, that at our finite $\kappa$ the product of the two actual toric logarithms is an algebraic nonzero multiple of

$$
\mathcal K(\nu^*)\,
\mathcal K(\psi^{*-1}\xi\mathbf N_K).
\tag{18}
$$

The second factor in (18) is in the interpolation range. Its underlying classical value is the nonzero companion from (13). Its ramified $p$-factor is a nonzero Gauss factor; the unramified case retains its Euler factors. CM algebraicity and the finite-twist period rule give

$$
\mathcal K(\psi^{*-1}\xi\mathbf N_K)
 \in\overline{\mathbf Q}^{\,\times}\,\Omega_p(\nu^*).
\tag{19}
$$

For the period assertion one may use [B2, Definition 2.13 and Lemma 2.14]. That finite-twist rule is algebraic and permits $p$-ramified finite characters: the differential changes by its nonzero generalized Gauss sum. It is not a claim that a ramified Artin character is crystalline.

Equations (17)--(19) prove that, for algebraic good local vectors, there is a scalar $e\in\overline{\mathbf Q}^{\,\times}$ with

$$
\Omega_p(\nu^*)\mathcal K(\nu^*)
 =e\,
  \log_{\omega_+}(P^+_\kappa(f_+))\,
  \log_{\omega_-}(P^-_\kappa(f_-)).
\tag{20}
$$

The algebraic scalar in (20) is defined by the stated normalizations and local factors, before deciding whether either side is zero. Thus (20) remains an identity when the target value is zero.

This argument deliberately does not use a factorization stated only as
$\mathscr L_{\rm Rankin}=u\,\mathscr L_1\mathscr L_2$ with
$u\in\Lambda^\times$. Such a statement by itself would not establish algebraicity of $u(\rho_\chi)$.

## 4. The periods are logarithms of actual finite sums of points

LZZ applies with $F=\mathbf Q$, $E=K=\mathbf Q(\sqrt{-3})$. Its ordinary-place hypothesis is that $p$ splits in $K$. There is no exclusion of discriminant $-3$, no restriction that $\xi$ be unramified at $p$, and no analytic-rank or Sha hypothesis in [L, Proposition 4.3.6].

With their Haar normalization, the CM quotient has total volume $2$. At a sufficiently small finite level, its toric period is a finite sum of the form

$$
P^+_\kappa(f_+)
 =\frac{2}{[C:U]}
   \sum_{t\in C/U} f_+(T_tP^+)\,\kappa(t),
\tag{21}
$$

and similarly for the dual period, with the inverse character. Here $C$ is the finite adelic torus quotient at that level and $U$ is a subgroup on which the integrand is invariant. This formula retains the unit stabilizers of the original CM order, including the units in $K$; one must not silently use a discriminant-less-than-$-3$ convention.

The normalization of (21), ordinary stabilizations, and the chosen $p$-local finite Fourier projectors have algebraic coefficients. Proposition 4.3.6 identifies their universal toric periods with their formal-group logarithms. Thus the two factors in (20) are logarithms of algebraic points, not classes in a completed local tensor product supplied only by an Iwasawa main conjecture.

### 4.1 The two loci and the fixed coefficient embedding

The star on a Hecke character in this proof is precomposition with the nontrivial automorphism of $K$:
$\eta^*(\mathfrak a)=\eta(\bar{\mathfrak a})$.
It is not an operation on an arbitrary element of $\mathbf C_p$.
Fix the coefficient embedding used for $f=\theta_\psi$, and use LZZ's canonical identification
$M_{A^\vee}=M_A$ from their Section 3.1.
The holomorphic CM characters of the two abelian factors, in this **same** coefficient embedding, are
$$
\psi^+=\psi,\qquad
\psi^-=\frac{\mathbf N_K}{\psi^*}.
\tag{22a}
$$
Here is a way to verify the second formula without identifying the two embeddings by notation.
The dual Tate module is the contragredient Tate module tensored by the cyclotomic character.
Its two characters over $K$ are therefore $\mathbf N_K/\psi$ and
$\mathbf N_K/\psi^*$.
Of these, $\mathbf N_K/\psi^*$ is the character with the required holomorphic type $(1,0)$.
The duality of the coefficient field in LZZ is induced by transpose endomorphisms, as is also clear from their canonical composition pairing.
Thus using an algebraic polarization does not allow one to replace $\psi^-$ by $\psi$ before (22a).

For the CM loci, choose the abstract conjugation of LZZ (3.1) to be the restriction of complex conjugation after a fixed algebraic complex embedding.
It commutes with the finite Hecke correspondences.
Choose Artin notation so that, on the positive locus,
$$
\sigma_sP^+=T_sP^+.
$$
Complex conjugation satisfies
$\sigma_sc=c\sigma_{\bar s}$.
Consequently
$$
\sigma_sP^-=T_{\bar s}P^-,
\qquad P^-=cP^+.
\tag{22b}
$$
These are algebraic reciprocity identities on the two CM loci.
They agree with the opposite tangent characters in LZZ Definition 2.4.1 and the conjugate-equivariance of their two local CM embeddings.
Changing the initial CM point or the abstract conjugation by a finite Hecke translation only multiplies the corresponding finite period by an algebraic character value.

The following table now records every change. The toric character in LZZ is
$\kappa=\xi^{-1}$.

| Period | Holomorphic CM character | Character in the finite sum | Galois action on its CM locus | Point-factor character |
|---|---|---|---|---|
| $P^+_\kappa$ | $\psi$ | $\xi^{-1}(t)$ | $t\mapsto st$ | $\xi(s)$ |
| $P^-_\kappa$ | $\mathbf N_K/\psi^*$ | $\xi(t)$ | $t\mapsto\bar s\,t$ | $\xi(\bar s)^{-1}=(\xi^*)^{-1}(s)$ |

In the last column the scalar coefficients are kept fixed.
For example, in the second row the change of variable $u=\bar s\,t$ gives
$\xi(t)=\xi(u)\xi(\bar s)^{-1}$.
The same calculation in the first row gives $\xi(s)$.

For a CM variety with holomorphic character $\eta$, a tensor of points with point-factor character $\tau$ descends to its finite twist with character $\eta\tau^{-1}$; this is precisely [B2, (2-8)--(2-9)].
Applying that rule to both rows gives
$$
\begin{aligned}
\nu^+&=\psi\xi^{-1}=\nu,\\
\nu^-&=\frac{\mathbf N_K}{\psi^*}
               \bigl((\xi^*)^{-1}\bigr)^{-1}
       =\frac{\mathbf N_K}{\psi^*\xi^{*-1}}
       =\frac{\mathbf N_K}{\nu^*}
       =\nu.
\end{aligned}
\tag{22c}
$$
The last equality uses the actual self-duality $\nu\nu^*=\mathbf N_K$.
Thus both transferred point factors lie in the same $B_\nu(K)$ and in the same holomorphic coefficient component.
No equality between a $\rho_\chi$ point and a $\rho_\chi^{-1}$ point has been assumed.
Ignoring either (22a) or (22b) would not justify (22c).

The finite-twist isogenies of [B2, Lemma 2.9] transfer both points and both algebraic differentials to this common component.
All differential scalars are algebraic.
In particular the auxiliary conductors used to construct $\psi$ disappear by this actual isogeny and twist descent, rather than by a claim about the modular level.

## 5. From the product to a square without assuming rank one

If $\mathcal K(\nu^*)=0$, take $P_\nu=0$. This gives the required zero case.

Suppose now that $\mathcal K(\nu^*)\ne0$. By (19)--(20), both actual toric logarithms in (20) are nonzero. In particular a corresponding Heegner point in $B_\nu(K)$ is non-torsion.

The general Gross--Zagier formula gives

$$
L'(\theta_\psi,\xi^{-1},1)
 =L'(\nu,1)L(\psi^*\xi^{-1},1),
\tag{23}
$$

and the non-torsion point forces this derivative to be nonzero. For this implication one may pair the point with its polarization conjugate and use positivity of the canonical height; it does not assume that an arbitrarily chosen bilinear pairing is positive. The companion in (13) is nonzero, so $L'(\nu,1)\ne0$.

The Gross--Zagier--Kolyvagin--Logachev consequence used in [B2, Lemma 3.25] now shows that $B_\nu(K)\otimes\mathbf Q$ is one-dimensional over its CM coefficient field. This consequence is classical and has no dependence on our chosen $p$: if desired, apply the cited argument with an auxiliary ordinary prime not dividing the conductor of $\nu$. Thus the conductor of $\nu$ at our $p$ does not obstruct this step.

Choose a generator $P_\nu$ of this line and an algebraic invariant differential in the specified CM component. By the two separate computations (22a)--(22c), both transferred logarithms in (20) use this same holomorphic $\nu$ component. They are therefore algebraic nonzero multiples of $\log_{\omega_\nu}(P_\nu)$. Rank one is used only after this component calculation; it would not identify logarithms in two different CM embeddings or finite eigensectors. We have therefore proved

$$
\mathcal K(\nu^*)
 =e_\nu\,
  \Omega_p(\nu^*)^{-1}
  \log_{\omega_\nu}(P_\nu)^2,
\qquad e_\nu\in\overline{\mathbf Q}^{\,\times}.
\tag{24}
$$

The rank-one conclusion in this paragraph was derived from nonzero (20); it was not an input to (24). There is likewise no assumed Sha finiteness. No statement that every finite twist has a nonzero value follows.

## 6. Descent to the exact field H_chi

For $\nu=\psi_k\rho_\chi^{-1}$, the CM twist construction gives, up to a $K$-isogeny,

$$
B_\nu
 \sim_K
 (E_k\otimes_K K(\rho_\chi))^{\rho_\chi^{-1}}.
\tag{25}
$$

Untwisting a $K$-rational point on (25) gives a tensor
$P_{k,\chi}\in E_k(H_\chi)_{\mathbf Q}\otimes_K\overline{\mathbf Q}$ satisfying (8). This is the explicit meaning of the finite-character descent in [B2, equations (2-8)--(2-9), Lemma 2.9, and Proposition 3.31]. It eliminates the auxiliary good-pair fields at the level of the point factor.

The differential and period comparison is algebraic. The generalized Gauss sum of the finite twist is nonzero and lies in an algebraic extension; by [B2, Lemmas 2.8 and 2.14] it accounts for both the twisted differential and the period. Consequently (24) becomes (9) with the fixed elliptic differential $\omega_k$ and period $\Omega_{p,E_k}$, for an algebraic $\epsilon_{k,\chi}\ne0$.

The coordinate field $H_\chi$ is unramified at $2,3,17$, as proved in R746. The field containing the scalar $\epsilon_{k,\chi}$, a Gauss sum, or a chosen algebraic square root may have additional ramification. That does not enlarge the coordinate field asserted in (7). These are distinct field assertions.

Also, $K(\theta)/K$ is totally ramified at $17$, whereas $H_\chi/K$ is unramified there. Their intersection is $K$. Hence the point-factor action of $\operatorname{Gal}(H_\chi/K)$ on $\phi_kP_{k,\chi}$ can be extended to the compositum by fixing $K(\theta)$. It still has the exact character $\rho_\chi$.

This proves (9) and its actual field assertion.

## 7. Returning to the original theta moment

R746 supplies the exact original-source identity

$$
\mathcal K_{34\delta}
  (\widehat{\bar\psi}_k\rho_\chi)
 =34c_k\theta^{11}\Omega_p\,\chi(34)^{-1}I_{k,\chi}^2.
\tag{26}
$$

Combining (9), (26), and the period and logarithm scalings (2)--(3) gives

$$
(\Omega_p I_{k,\chi})^2
 =
 \frac{\epsilon_{k,\chi}\chi(34)}
      {34c_k}\theta^{-k-12}
 \log_{\omega_1}(\phi_kP_{k,\chi})^2.
\tag{27}
$$

All factors on the right other than the displayed logarithm are algebraic. Taking an algebraic square root proves (10)--(11). If the common value is zero, (26) gives $I_{k,\chi}=0$ and the zero point works. Thus no division by a zero period or logarithm was used.

For an algebraic-valued finite function $\Phi$ on $(\mathbf Z/p^\ell)^\times$, finite Fourier inversion in R746 yields

$$
\Omega_p\int_{\mathbf Z_p^\times}
              x^{-1}\Phi(x)\,d\mu_{D_{k,17}}(x)
 \in
 \sum_{\substack{\chi\bmod p^\ell\\\chi|_{\mu_6}=1}}
 \log_{\omega_1}
 \left(\phi_k
  (E_k(H_\chi)_{\mathbf Q}\otimes_K\overline{\mathbf Q})^{\rho_\chi}\right).
\tag{28}
$$

The coefficients in (28) are algebraic; the statement includes all tame and wild characters. Fourier inversion is linear before any square is taken. It does not delete cross terms in the square of the resulting sum.

## 8. The point-factor idempotents and the trivial character

Let $H/K$ be a finite extension containing the finitely many $H_\chi$ occurring in (28). Work in the algebraic tensor space of points and let Galois act **only on the point factor**:

$$
\sigma(P\otimes a)=(\sigma P)\otimes a.
\tag{29}
$$

In particular the coefficients $a\in\overline{\mathbf Q}$, including the Fourier coefficients, Gauss factors and square roots in (11), are fixed for this operation.

The trivial point-factor idempotent is

$$
e_{\mathrm{triv}}
 =\frac1{|\operatorname{Gal}(H/K)|}
       \sum_{\sigma\in\operatorname{Gal}(H/K)}(\sigma\otimes1).
\tag{30}
$$

By (8),

$$
e_{\mathrm{triv}}P_{k,\chi}=0
\quad\text{if }\chi\ne1.
\tag{31}
$$

For $\chi=1$, the original rank-one calculation in R735 gives

$$
\phi_k\left(E_k(K)_{\mathbf Q}\otimes_K\overline{\mathbf Q}\right)
 =\overline{\mathbf Q}\,Q_k,
\tag{32}
$$

with the original non-torsion point of that result. Thus the trivial point-factor part of the actual finite sum in (28) belongs to the original $Q_k$ line.

Equations (29)--(31) are statements in a tensor product of algebraic point spaces. They do not assert a Galois action on an arbitrary $p$-adic number, and do not move the chosen $p$-adic embedding. In particular one must not apply $\sigma$ simultaneously to the scalar coefficients and call that the idempotent in (30). R749 proves the logarithm map on the common algebraic point tensor space is injective. A logarithm relation in that space can therefore be transferred to its unique point-space relation, and (30) is then a legitimate algebraic operation on the complete relation.

### 8.1 Algebraic linear independence of the nonzero finite-character values

The point-factor hypothesis (H) in R749 is now proved for every surviving finite character on each of the two sources.
Its Theorem 3 therefore applies: in every finite collection of indices $(k,\chi)$, all the nonzero values
$$
\Omega_p I_{k,\chi}
$$
are linearly independent over $\overline{\mathbf Q}$.
Only linear independence is asserted here, not algebraic independence.

Indeed, after putting the finitely many $H_\chi$ in a common only-$p$-ramified field, the two cubic characters at $17$ separate $k=2$ and $k=4$, and the point-factor $p$-ray characters separate different $\chi$.
The logarithm map on the common algebraic point tensor space is injective by R749.
Its point-factor projectors keep every scalar from (11) fixed.

For the finite function in (28), R749 (25) gives the exact identity
$$
(e_{\mathrm{triv}}^{\mathrm{pt}})^{\log}
 \left(\Omega_p\int_{\mathbf Z_p^\times}
              x^{-1}\Phi(x)\,d\mu_{D_{k,17}}(x)\right)
 =\widehat\Phi(1)\,\Omega_p I_{k,1}.
\tag{33}
$$
In particular a nonzero trivial Fourier coefficient forces this one-source finite-gate value to be nonzero, since the original $I_{k,1}$ is nonzero by R735.
This conclusion retains the hypothesis that the complete source in (28) has already been identified.
It does not identify the other theta components of a mixed gate.

## 9. Scope for the finite gates of R742/R745

The conclusion is available once a finite source has actually been decomposed into the two complete global eigen-sources of R735 and their finite $p$-Schwartz operations.

R745 pays the finite Fourier expansion and the algebraicity of finite orthogonal companion jets. It does not, by itself, identify every resulting section with either $D_{2,17}$ or $D_{4,17}$. In particular:

- For another angular type $h$, a negative-one moment survives precisely when $\chi(\zeta)=\zeta^{h+1}$ on $\mu_6$. The type-$5$ vanishing test in R746 cannot be applied to another type.
- A quarter source and the rational transformation returning its core must be transported together. A bare quarter factor does not prove the presence of an independent quadratic twist.
- The rational $Y_\kappa$ observation, if denominator-cleared, carries its actual theta index and full local Schwartz tensor. It is not the bare degree-$34$ line merely because its rational norm was $34$.
- Auxiliary good-pair choices in this proof do not authorize replacing the actual finite gate by a convenient local test vector. They identify the scalar Katz value through a separate nonzero auxiliary period. The original Fourier coefficient and its bad-place source identity remain those of R746/R745.
- The present proof imposes no additional vanishing on a moving gate, an exterior integral, or a complementary domain.

Thus the new usable conclusion is (28) together with the exact point-factor character (8) and the actual unramified coordinate field. The remaining full-source spectral decomposition is a separate arithmetic task.

## References and normalization sources

- R735, *Two type-five Schwartz and rank-one negative moments*: original complete sources, characters, periods and the two rank-one point lines.
- R746, *Original type-five all-finite-p-character squares*: the exact finite-character identity (26), all tame branches, and the global character (5).
- R745, *Finite p-gates, algebraic theta sources and orthogonal jets*: finite-source algebraicity without a free spectral identification.
- [R749](R749-point-factor-projectors-and-finite-character-extraction.md), *Point-factor projectors and finite-character extraction*: injective logarithm space and the point-only projectors; its hypothesis (H) is paid here.
- [B1] M. Bertolini, H. Darmon, K. Prasanna, *Generalized Heegner cycles and p-adic Rankin L-series*, Duke Math. J. 162 (2013), 1033--1148, especially Section 5.1, equation (5.1.11), Lemma 5.3 and Theorem 5.4. [Author-hosted published paper](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP1.pdf).
- [B2] M. Bertolini, H. Darmon, K. Prasanna, *p-adic Rankin L-series and rational points on CM elliptic curves*, Pacific J. Math. 260 (2012), 261--303, especially Lemmas 2.8--2.9, Definition 2.13, Lemma 2.14, Theorem 3.17, Proposition 3.28, Lemma 3.25 and Proposition 3.31. [Author-hosted paper](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf). The prime-to-$p$ restriction in its original Section 3E is replaced here at the point-period step by [L], not ignored.
- [L] Y. Liu, S. Zhang, W. Zhang, *A p-adic Waldspurger formula*, Duke Math. J. 167 (2018), 743--833, DOI [10.1215/00127094-2017-0045](https://doi.org/10.1215/00127094-2017-0045), especially Theorem 2.3.17, Definition 3.3.1, Theorem 3.3.2, Lemma 4.1.9 and Propositions 4.3.4--4.3.6. [Author-hosted published paper](https://web.math.princeton.edu/~shouwu/publications/pWalds.pdf).
- For comparison only, the Iwasawa-unit factorization in A. Burungale, F. Castella, C. Skinner, Y. Tian, *p-infinity-Selmer groups and rational points on CM elliptic curves*, Ann. Math. Québec 46 (2022), Proposition 4.5, is not used as a substitute for the algebraic normalization above. [Published open-access paper](https://link.springer.com/article/10.1007/s40316-022-00203-y).
