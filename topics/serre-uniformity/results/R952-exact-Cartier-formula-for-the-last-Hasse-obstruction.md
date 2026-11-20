# R952: an exact Cartier formula for the last Hasse obstruction

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved symbolic identities for the entire source space.** This identifies the map $\mathscr O_r$ of R946 itself, not only its kernel or its named CM eigenvector. It does not prove that Cartier is zero on the whole generalized original CM packet. No finite mathematical computation is used.

## 1. The complete-space statement

Use the same connected fine full-six curve, perfect field, Hodge bundle, Hasse invariant $\mathcal A$, Hasse derivative $\mathcal B$, Katz operator $\mathcal T$, and reduced supersingular divisor $\Sigma$ as in [R946](R946-universal-Bol-divisibility-and-final-supersingular-obstruction.md). Set
$$
2\le r\le p-2,\qquad w=p+1-r,\qquad s=p-1-r,
\tag{952.1}
$$
so $3\le w\le p-1$ and $s\ge1$. For any $H\in S_w$ write its original full-six Fourier expansion as
$$
H(Q)=\sum_{n\ge1}a_nQ^n.
$$
There is a unique form $\mathscr U H\in S_w$ characterized by
$$
\boxed{\quad
(\mathscr U H)^p
=\mathcal A^{p+1-r}H-6^r\mathcal T^{s}(\mathscr D_rH),
\qquad
(\mathscr U H)(Q)=\sum_{n\ge1}a_{pn}^{1/p}Q^n.
\quad}
\tag{952.2}
$$
The operator $\mathscr U$ is additive and $p^{-1}$-semilinear over the perfect coefficient field. The inverse Frobenius on its coefficients is part of this definition. It is not discarded when discussing original characters or paired tame markings.

The exact pointwise identification is
$$
\boxed{\quad
\mathscr O_r(H)
=\left.r!\,\frac{(\mathscr U H)^p}{\mathcal B^{p-r}}\right|_\Sigma.
\quad}
\tag{952.3}
$$
Both sides have weight $r$. Since $\mathcal B$ is a unit at every point of $\Sigma$, the division is legitimate there. Formula (952.3) implies
$$
\boxed{\quad
\mathscr O_r(H)=0
\iff \mathscr U H=0
\iff a_{pn}=0\ \text{for every }n\ge1.
\quad}
\tag{952.4}
$$
Thus the full-packet saturation condition of R946 is exactly the vanishing of this actual Cartier operator on that full packet. It is not merely equivalent to the vanishing of its scalar eigenvalue.

All statements first hold on the complete fine-level space, for both parities. For a tame character $\chi$, $\mathscr U$ has the Frobenius-conjugate character $\chi^{1/p}$; it is not declared to be a linear endomorphism of one unchanged character summand. Original $H_6$ applications retain the compatible even central character and even $r$, as in R946. All actual full-norm extensions are retained below.

## 2. Construction of the actual root form

For every fine-level modular form the complete Fourier identity $\Theta_Q^p=\Theta_Q$ and the full-six expansion principle give
$$
\mathcal T^pH=\mathcal A^{p+1}\mathcal TH.
\tag{952.5}
$$
Indeed both sides have weight $w+p(p+1)$, and their Fourier expansions agree. No Frobenius is being applied to their coefficients in this identity: it is the equality $n^p=n$ in the coefficient field that acts on the exponent $n$.

Let
$$
K=\mathcal A^{p+1}H-\mathcal T^{p-1}H.
$$
R946(946.10), or its direct Katz product-rule proof, says that $\mathcal T$ commutes with multiplication by every nonnegative power of $\mathcal A$, when the actual input weights are used. Thus (952.5) implies $\mathcal TK=0$. R946's universal identity, valid for this arbitrary $H$, gives
$$
\begin{aligned}
K
&=\mathcal A^r L,\\
L
&=\mathcal A^{p+1-r}H-6^r\mathcal T^s(\mathscr D_rH),\\
\operatorname{wt}(L)&=p(p+1-r)=pw.
\end{aligned}
\tag{952.6}
$$
Here $L$ is globally regular and cuspidal. Commutation again gives $\mathcal TL=0$, since multiplication by $\mathcal A^r$ is injective.

Because the weight of $L$ is divisible by $p$, the second term of the Katz rule disappears:
$$
\mathcal TL=6\mathcal A\partial_{pw}L.
$$
It follows that $\partial_{pw}L=0$. In a regular local Hodge frame $\rho$, write $L=l\rho^{pw}$. The connection contribution to its scalar derivative is a multiple of $pw$, hence zero. The identity $\partial_{pw}L=0$ therefore says $dl=0$ in the local function field.

For a smooth curve over a perfect field the kernel of $d$ in its function field is its subfield of $p$th powers, as also used in R932's inverse de Rham Frobenius argument. Thus $l=g^p$ for a unique rational function $g$. It is regular wherever $l$ is regular, since its valuation is the valuation of $l$ divided by $p$. If two Hodge frames have transition $\rho'=z\rho$, the two coefficients of $L$ differ by $z^{-pw}$; their unique $p$th roots therefore differ by $z^{-w}$. The root sections $g\rho^w$ consequently glue to an actual global section $G$ of $\omega^w$. Since $L$ vanishes at each cusp and is a $p$th power, $G$ also vanishes there. Therefore $G\in S_w$ and $G^p=L$.

This proves existence and uniqueness of the root form in (952.2). In the Tate frame $\mathcal A(Q)=1$, so
$$
G(Q)^p
=H(Q)-\Theta_Q^{p-1}H(Q)
=\sum_{n\ge1}a_{pn}Q^{pn}.
\tag{952.7}
$$
The perfect-field root gives exactly the displayed Fourier expansion of $\mathscr U H=G$. In particular the root is fixed by the original coefficients and cusp. No independent phase or scalar normalization has been chosen.

The argument also explains the actual character change. If a tame automorphism acts on $H$ through $\chi$, it acts on $L$ through the same $\chi$, by naturality of the canonical operators. Its action on the unique root $G$ is then through $\chi^{1/p}$. Norm characters with values in $\mathbf F_p$ retain their value, whereas a character valued in $\mathbf F_{p^2}$ is conjugated when its value is not in $\mathbf F_p$. This is the usual Cartier character transport, not a substitute for it.

## 3. Evaluate the entire iterate at every Hasse zero

At a supersingular point, evaluating the Katz rule on any weight-$k$ form $U$ gives
$$
(\mathcal TU)|_\Sigma=6k\,\mathcal B\,U|_\Sigma.
\tag{952.8}
$$
In the $s=p-1-r$ iterations starting with $\mathscr D_rH$, whose weight is $p+r+1$, the successive weight residues are
$$
r+1,r+2,\ldots,p-1.
$$
Every one is nonzero. Wilson's identity gives their product as
$-1/r!$. Consequently
$$
(\mathcal T^s\mathscr D_rH)|_\Sigma
=-\frac{6^s}{r!}\mathcal B^s(\mathscr D_rH)|_\Sigma.
\tag{952.9}
$$
The first term of $L$ in (952.6) vanishes along $\Sigma$. Since $r+s=p-1$ and $6^{p-1}=1$, (952.2) and (952.9) give
$$
(\mathscr U H)^p|_\Sigma
=\frac1{r!}\mathcal B^s(\mathscr D_rH)|_\Sigma.
\tag{952.10}
$$
Dividing by $\mathcal B^{s+1}$ proves (952.3), with $s+1=p-r$.

The identity holds at every supersingular point. For example, in a local Hodge frame it reads
$$
(\mathscr O_rH)_P
=r!\frac{g_P^p}{b_P^{p-r}},
\qquad
g_P=(\mathscr U H/\rho_P^w)(P),\quad
b_P=(\mathcal B/\rho_P^{p+1})(P).
\tag{952.11}
$$
Its frame exponent is exactly $r$, as required. No elliptic branch, trace degree or Igusa-part multiplicity is removed in passing to this formula.

If $\mathscr O_r(H)=0$, equation (952.10) shows that $\mathscr U H$ vanishes at the reduced divisor $\Sigma$. Thus $\mathcal A$ divides $\mathscr U H$ as a modular section. The quotient would be a cusp form of weight
$$
w-(p-1)=2-r\le0.
$$
There are no such nonzero cusp forms: negative Hodge degree excludes the negative weights, and a global constant cannot vanish at the nonempty cusp divisor in weight zero. Hence $\mathscr U H=0$. The converse follows from (952.3), and the Fourier criterion follows from (952.2). This proves (952.4) without an eigenform decomposition or a generalized-eigenvector lifting argument.

## 4. Identification with Cartier on the actual Igusa curve

On the fine Igusa cover use precisely R932's canonical section $\mathfrak a^{p-1}=\mathcal A$ and normalization
$$
\Phi_w(H)=\frac16\operatorname{KS}\left(H/\mathfrak a^{w-2}\right),
\qquad \Phi_w(H)(Q)=H(Q)\,dQ/Q.
\tag{952.12}
$$
For $3\le w\le p-1$ this is holomorphic. At a supersingular point use $\mathcal A/\rho^{p-1}=z^{p-1}$ and $\mathfrak a=z\rho$. The order of its scalar differential is at least
$(p-2)-(w-2)=p-w\ge1$. At the cusps the Hasse root is a unit and $H$ is cuspidal. The same statements apply to $\mathscr U H$.

The Fourier rule for Cartier now gives the exact identity of holomorphic differentials
$$
\boxed{\quad
\mathcal C\bigl(\Phi_w(H)\bigr)=\Phi_w(\mathscr U H).
\quad}
\tag{952.13}
$$
For clarity, its local rule on the logarithmic Fourier differential is
$\mathcal C(\sum a_nQ^n dQ/Q)=\sum a_{pn}^{1/p}Q^n dQ/Q$. Equality at the fixed cusp gives equality of the rational, and hence holomorphic, differentials. The scalar $1/6$ in (952.12) is fixed by inverse Frobenius, so no new factor of six occurs.

This is a semilinear map on the actual fine Igusa curve, with the character transport proved after (952.7). On original quotient components the map is transported by the same prime-to-$p$ pullbacks and traces as in R913/R932. The full norm character and any paired geometric deck character remain present. In particular one must not replace (952.13) by an assertion that the coefficient-extraction operator without inverse Frobenius is an endomorphism of one unchanged marked modular space.

Combining (952.4) and (952.13), for any actual source subspace $M\subset S_w$ one obtains
$$
\boxed{\quad
\mathcal T^rM\subset\mathcal A^{r+1}S_{r+2}
\iff\mathscr O_r(M)=0
\iff\mathcal C\bigl(\Phi_w(M)\bigr)=0.
\quad}
\tag{952.14}
$$
This is a complete-space equivalence. Applied to the actual generalized CM packet, its last condition is an assertion that the whole packet is in the Cartier kernel. A zero eigenvalue or a nilpotent Cartier primary part does not imply that assertion.

## 5. The composed pairing is a high-weight supersingular pairing with Cartier inserted

The same pointwise calculation identifies R951's bilinear form. For correctly paired $H,H'\in S_w$, substitute (952.10) in its full residue expression:
$$
\begin{aligned}
\mathscr B_r(H,H')
&=\sum_{P\in\Sigma}\frac{(\mathscr D_rH)_P H'_P}{b_P^2}\\
&=r!\sum_{P\in\Sigma}\frac{(\mathscr U H)_P^p H'_P}{b_P^w}.
\end{aligned}
\tag{952.15}
$$
Define at this same weight $w$ the intrinsic finite pairing
$$
\mathcal H_w(Y,U)=\sum_{P\in\Sigma}\frac{Y_PU_P^p}{b_P^w},
\tag{952.16}
$$
with the full fine-point or residue-field trace sum. This is exactly the type of finite pairing constructed in R950(950.6), now at the high weight and with its own two arguments. Equation (952.15) is
$$
\boxed{\quad
\mathscr B_r(H,H')=r!\,\mathcal H_w(H',\mathscr U H).
\quad}
\tag{952.17}
$$
It implies from R951 the precise identity
$$
\mathcal H_w(H',\mathscr U H)
=(-1)^r\mathcal H_w(H,\mathscr U H').
\tag{952.18}
$$
All quantities in (952.15–18) use the same original Hodge frames and actual characters; no low-weight/high-weight pairing identification is used.

For the named original companions, R947 proves that the coefficients of $F=V_{p+1-r}^\dagger$ at indices divisible by $p$ vanish. Thus
$$
\mathscr U F=0.
\tag{952.19}
$$
This recovers its vanishing under $\mathscr O_r$ and explains its place in both radicals of R951's composed pairing. It does **not** show
$\mathcal H_w(F,F)=0$ or nonzero: (952.17) has $\mathscr U F$, not $F$, in its second argument. The high-weight diagonal of R932/R936 remains a different scalar. Likewise R950's nonzero low-weight diagonal remains at weight $r+2$; no equality with it follows from (952.17).

## Dependencies and scope

- R946: the actual Katz product rule, universal $\mathcal A^r$ divisibility, and the definition of $\mathscr O_r$.
- R932(932.6–7), (932.22–25), and §§2, 5–6: canonical Igusa normalization, local Hasse orders, inverse-Frobenius roots and actual tame traces.
- R947 §1: the original named CM form has zero coefficients at indices divisible by $p$.
- R951: the exact obstruction/connecting-map residue pairing and its $(-1)^r$ symmetry.
- R950(950.6): notation for the intrinsic supersingular finite pairing; its low-weight nonvanishing is not substituted for high-weight nonvanishing.

Every new identity and kernel equivalence above is proved on the entire indicated fine-level source space. The remaining generalized-packet Cartier vanishing, the high-weight diagonal, and the original rational-point exclusion are not asserted. No new local or remote numerical arithmetic was performed.
