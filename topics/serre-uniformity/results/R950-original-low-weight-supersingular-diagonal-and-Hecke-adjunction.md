# R950 — Nonvanishing of the original fixed-low-weight supersingular diagonal

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / literature_frontier. **Status: proved for both original rows.** The proof determines the Hecke action on R947's class directly from its complete supersingular principal parts. It does not infer the type of a Frobenius preimage from the type of its image.

For the original forms and markings, put
$$
(r,w,V)=
\begin{cases}
(2,4,V_4^\dagger),&p\equiv11\pmod{12},\\
(8,10,V_{10}^\dagger),&p\equiv5\pmod{12},
\end{cases}
\qquad p\ge41.
$$
On the same connected fine full-six curve $X$ used in R944–R947, with its full supersingular divisor $\Sigma$, the result is
$$
\boxed{\quad
\sum_{P\in\Sigma}
\frac{(V/\rho_P^w)(P)^{p+1}}
{(\mathcal B/\rho_P^{p+1})(P)^w}
\ne0.
\quad}
\tag{950.1}
$$
Each $\rho_P$ is any nonzero local Hodge frame. The expression is independent of those choices. Every fine supersingular point is included; no elliptic zero or special marked point is removed. The original Serre application still imposes $p\equiv2,5\pmod9$.

This is the **low-weight** sum of R947(947.19). The original R932/R936 functional uses the other weight $p+1-r$ and the other form $F=V_{p+1-r}^\dagger$. No equality between those two sums is asserted here.

## 1. The principal-part construction on the whole low-weight space

Let $\kappa$ be a perfect coefficient field over which the fine marking is defined. It can harmlessly be enlarged so that all the finitely many supersingular points in the argument are rational. Write
$$
\mathcal S_w=H^0(X,\omega^w(-C)),\qquad w=r+2,
$$
where $C$ is the full cusp divisor. The positive Kodaira–Spencer convention is that of R944:
$$
K_\rho=\operatorname{KS}(\rho^2),\qquad
A=\mathcal A/\rho^{p-1},\qquad
b_P=(\mathcal B/\rho^{p+1})(P),\qquad
dA(P)=b_PK_\rho(P).
\tag{950.2}
$$
Here $A$ is a parameter at each $P\in\Sigma$ and $b_P\ne0$.

For every $Y\in\mathcal S_w$, not just the named CM form, define a class
$$
\mathfrak z_r(Y)\in H^1(X,\omega^{-r})
\tag{950.3}
$$
by the principal parts
$$
\frac{\mu_P(Y)}A\rho^{-r},\qquad
\mu_P(Y)=
\left(-\frac{(Y/\rho^w)(P)b_P^{p-r-2}}{r+1}\right)^{1/p}.
\tag{950.4}
$$
The inverse $p$th-power map is unique in the perfect residue fields. This construction is additive and $p^{-1}$-semilinear in $Y$.

The change-of-frame proof in R947 §4 applies to every $Y$. Explicitly, for $\rho'=z\rho$, the expression inside the root in (950.4) changes by
$z_P^{p(-p+r+1)}$. The difference between the resulting two principal parts is
$$
\frac{\mu_P(Y)}A
\left((z/z_P)^{p-1-r}-1\right)\rho^{-r},
$$
which is regular. Thus (950.3) is a well-defined global class, not an assignment dependent on a set of chosen values of frames. It is also compatible with isomorphisms of the underlying elliptic curves with level structure, and with perfect field extension. No assertion about the de Rham Frobenius image of (950.3) for arbitrary $Y$ is needed.

Let $\langle\ ,\ \rangle_X$ be the Serre pairing in the KS convention of R947. Its principal-part formula gives, for $U\in\mathcal S_w$,
$$
\langle\mathfrak z_r(Y),U\rangle_X
=\sum_{P\in\Sigma}\frac{\mu_P(Y)(U/\rho^w)(P)}{b_P}.
\tag{950.5}
$$
Define the complete finite sum
$$
\mathcal H_w(Y,U)=
\sum_{P\in\Sigma}
\frac{(Y/\rho^w)(P)(U/\rho^w)(P)^p}{b_P^w}.
\tag{950.6}
$$
Changing $\rho$ to $z\rho$ multiplies the numerator and denominator in each term by the same factor $z_P^{-w(p+1)}$. Hence (950.6) is intrinsic. It is linear in $Y$ and $p$-semilinear in $U$. Equation (950.5) gives exactly
$$
\boxed{\quad
\langle\mathfrak z_r(Y),U\rangle_X^p
=-\frac1{r+1}\mathcal H_w(Y,U).
\quad}
\tag{950.7}
$$
No positivity property of a finite-field norm is used.

For the original $V$, R947 proves from its actual rational Gauss–Manin primitive that
$$
\mathfrak z_r(V)=z_V,\qquad
\mathsf F_r(z_V)=[\Omega_V]\ne0.
\tag{950.8}
$$
In particular $z_V\ne0$. The last implication uses only that a map sends zero to zero. The argument below does not require $\mathsf F_r$ to be injective.

## 2. The exact isogeny change of the supersingular denominator

Consider a prime-to-$p$ isogeny
$$
\phi:E\longrightarrow E',\qquad \deg\phi=\ell,
$$
in the fine Hecke correspondence, and choose local frames with
$$
\phi^*\rho'=\rho.
\tag{950.9}
$$
These are frames on an étale neighborhood in the correspondence. Since $\ell\ne p$, the scheme of cyclic subgroups of order $\ell$ is étale over the fine elliptic moduli problem.

The scalar Hasse invariants agree:
$$
A(E',\rho')=A(E,\rho).
\tag{950.10}
$$
This follows directly from naturality of relative Frobenius and Verschiebung under $\phi$. Equivalently, the induced map on the Hodge quotient in the dual frame is multiplication by $\ell$, and the pullback on the alternating de Rham pairing also multiplies by $\ell$; those two factors cancel in the scalar Hasse invariant.

Naturality of the Gauss–Manin connection and the polarization gives
$$
\begin{aligned}
K_\rho
&=\langle\rho,\nabla\rho\rangle_E\\
&=\langle\phi^*\rho',\phi^*\nabla\rho'\rangle_E
=\ell\,K_{\rho'}.
\end{aligned}
\tag{950.11}
$$
At a supersingular point of the correspondence, differentiate (950.10) and use (950.2). Since the Hasse invariant itself vanishes there, no connection correction contributes to that evaluation. Consequently
$$
\boxed{\quad b_{E',\rho'}=\ell\,b_{E,\rho}.\quad}
\tag{950.12}
$$
This is a pointwise identity on the actual full supersingular correspondence. It is not an assumption that $\mathcal B$ is unchanged by an isogeny.

For the dual isogeny $\widehat\phi:E'\to E$, the frame on its target which pulls back to $\rho'$ is $\rho/\ell$, because
$$
\widehat\phi^*\rho=\ell\rho'.
\tag{950.13}
$$
Accordingly a weight-$w$ form on that target evaluates as
$$
U(E,\rho/\ell)=\ell^w U(E,\rho).
\tag{950.14}
$$
Equations (950.12) and (950.14) are the two factors needed in the adjunction.

## 3. Hecke adjunction before any packet argument

Use the modular Hecke normalization of R942 and R932. In isogeny notation it is
$$
(T_\ell Y)(E,\rho)
=\frac1\ell\sum_{C_\ell\subset E[\ell]}
Y(E/C_\ell,\rho_{C_\ell}),
\qquad
\phi_{C_\ell}^*\rho_{C_\ell}=\rho.
\tag{950.15}
$$
It has the Fourier rule
$$
\sum a_nQ^n\longmapsto
\sum_{n\ge1}(a_{\ell n}+\ell^{w-1}a_{n/\ell})Q^n.
$$
Indeed the multiplicative Tate quotient has normalized differential $\rho'/\ell$ and contributes $\ell^{w-1}Y(Q^\ell)$; the other $\ell$ quotients give the averaging term. Thus (950.15) has precisely the $1/\ell$ normalization already fixed in R942(942.5–6), with no extra factor of six.

First keep the full pairing components and the actual transpose level correspondence. Reversing an oriented isogeny edge by its dual is a bijection on this complete supersingular correspondence. In a term indexed by $\phi:(E,\rho)\to(E',\rho')$, put $b=b_{E,\rho}$ and $b'=\ell b$. Its contribution to $\mathcal H_w(T_\ell Y,U)$ is
$$
\frac1\ell\frac{Y(E',\rho')U(E,\rho)^p}{b^w}.
$$
Using the target frame $\rho/\ell$ for the reversed edge, this is
$$
\begin{aligned}
\frac1\ell
\frac{Y(E',\rho')\,
\ell^{-wp}U(E,\rho/\ell)^p\,\ell^w}{(b')^w}
&=
\frac1\ell
\frac{Y(E',\rho')U(E,\rho/\ell)^p}{(b')^w},
\end{aligned}
\tag{950.16}
$$
since $\ell^p=\ell$ in the residue field. Summing reversed edges, and using $(1/\ell)^p=1/\ell$, proves
$$
\boxed{\quad
\mathcal H_w(T_\ell Y,U)
=\mathcal H_w(Y,T_\ell^{\mathrm{tr}}U).
\quad}
\tag{950.17}
$$
The superscript here means the actual reversed level correspondence in the same modular normalization. It is not an instruction to identify two different tame markings.

Together with the injectivity of $p$th power on the coefficient field and (950.7), this gives
$$
\langle\mathfrak z_r(T_\ell Y),U\rangle_X
=\langle\mathfrak z_r(Y),T_\ell^{\mathrm{tr}}U\rangle_X.
\tag{950.18}
$$
Thus the map $\mathfrak z_r$ itself is Hecke equivariant for the Serre-dual correspondence action, with its stated semilinearity. This is a proof on principal parts, so a kernel of $\mathsf F_r$ cannot add an unidentified Hecke component to $z_V$.

## 4. Tame invariants and the conjugate intermediate marking

On the fixed fine pairing component let $G$ be R942(942.3)'s geometric graph subgroup, and let $G'$ be its determinant-five conjugate. Its order is divisible only by two and three. Write
$$
\mathcal S=\mathcal S_w^G,\qquad
\overline{\mathcal S}=\mathcal S_w^{G'}.
\tag{950.19}
$$
For $w=10$, these are exactly R942's two complete four-dimensional marked spaces. The original $V_w^\dagger$ belongs to $\mathcal S$.

Every element of $G$ changes the tame level datum through an isomorphism of elliptic curves. Equations (950.2–4) are natural for these isomorphisms. Thus
$$
\mathfrak z_r(g^*Y)=g^*\mathfrak z_r(Y),
$$
in the corresponding pullback conventions, and in particular
$$
z_V\in H^1(X,\omega^{-r})^G.
\tag{950.20}
$$
This membership is derived directly from the original principal parts; it is not inferred from (950.8).

The Serre pairing restricted to these $G$ invariants is perfect. To see this without a dimension assumption, take the unit averaging idempotent
$e_G=|G|^{-1}\sum_{g\in G}g$. For an invariant $z$,
$$
\langle z,U\rangle_X=\langle z,e_GU\rangle_X.
\tag{950.21}
$$
If $z$ annihilates all invariant $U$, it annihilates the whole cusp space and hence is zero by fine-level Serre duality. The corresponding argument applies to the other factor. In particular the nonzero $z_V$ gives a nonzero functional on the **whole actual** $\mathcal S$.

For $\ell=5$, R942 proves the two modular arrows
$$
T:\mathcal S\longrightarrow\overline{\mathcal S},
\qquad
\bar T:\overline{\mathcal S}\longrightarrow\mathcal S.
\tag{950.22}
$$
They are each other's actual transpose in (950.17). In detail, the determinant-five representatives give the two graph markings $G,G'$; reversing the isogeny gives the opposite arrow. Composing an isogeny with its dual contributes the scalar-five tame level map. At level six this is $-I$, already in the original graph subgroup, and it acts trivially in the even weight $w$ and the even tensor power $r$. Hence the transpose has no omitted diamond or sign. This is the same level computation used in R942 §§2 and 5 and R913 §7.

Consequently the cross-marking adjunction is
$$
\mathcal H_w(TY,\bar U)
=\mathcal H_w(Y,\bar T\bar U).
\tag{950.23}
$$
Both sides are full fine supersingular sums in their specified markings. Applying this to the two arrows gives an adjunction for the genuine endomorphism
$$
\mathcal U=\bar T T=T_5^2|_{\mathcal S}:
\qquad
\mathcal H_w(\mathcal UY,U)
=\mathcal H_w(Y,\mathcal UU).
\tag{950.24}
$$
No ordinary $T_5$ endomorphism of $\mathcal S$ has been invented.

The original full-norm and pairing-component transports are the ones already fixed in R913. They are isomorphisms, and (950.18) commutes with their actual pullbacks and transpose traces. In the original raw Hecke normalization the two modular arrows can acquire the prescribed nonzero powers of five. Their squares still have the same zero-primary spaces. We therefore use (950.24) in the marked modular spaces where every scalar has just been calculated, and do not replace an original degree or unknown source factor by one.

## 5. The two diagonal nonvanishing arguments

### 5.1 Weight four

For $r=2$, R918 proves the complete integral and residual equality
$$
\mathcal S=S_4(H_6,\kappa)=\kappa V_4^\dagger.
\tag{950.25}
$$
Equations (950.8), (950.20), and (950.21) say that $z_V$ defines a nonzero functional on this whole one-dimensional space. Therefore
$$
\langle z_V,V_4^\dagger\rangle_X\ne0.
\tag{950.26}
$$
Equation (950.7) proves (950.1) in this row. This conclusion does not need any high-weight multiplicity-one assertion.

### 5.2 Weight ten

For $r=8$, the original CM form satisfies
$$
T V_{10}^\dagger=0
$$
in the conjugate marked target. This is the original inert-five CM relation, also explicit in R942(942.14). Hence (950.23), or directly (950.24), shows
$$
\langle z_V,\mathcal U U\rangle_X=0
\qquad(U\in\mathcal S).
\tag{950.27}
$$
R942 proves on the complete four-dimensional space that
$$
\mathcal S=\kappa V_{10}^\dagger\oplus\operatorname{im}\mathcal U,
\tag{950.28}
$$
and $\mathcal U$ is invertible on its image. Its two possible nonzero eigenvalues are
$147456=2^{14}3^2$ and $666^2$, which are units for every $p\ge41$. The generalized zero-primary part is exactly the one-dimensional first summand; coincidence of the two nonzero eigenvalues does not affect (950.28).

The functional induced by $z_V$ on $\mathcal S$ is nonzero by (950.8) and (950.20–21), and it vanishes on the second summand by (950.27). It must therefore be nonzero on $V_{10}^\dagger$:
$$
\langle z_V,V_{10}^\dagger\rangle_X\ne0.
\tag{950.29}
$$
This is a genuine conclusion on the complete dual packet, not on an unspecified Frobenius preimage. Applying (950.7) proves (950.1) in the second row.

## 6. The remaining comparison is still a separate mathematical assertion

What is now proved is
$$
\langle z_V,V\rangle_X\ne0,\qquad
\sum_{P\in\Sigma}V_P^{p+1}/b_P^{r+2}\ne0.
$$
The original high-weight source remains
$$
F=V_{p+1-r}^\dagger,\qquad
\sum_{P\in\Sigma}F_P^{p+1}/b_P^{p+1-r}.
$$
R947 §5 shows explicitly why its singular Igusa projection does not give an uncorrected cohomological adjunction: it kills the horizontal polar part of $W$ and can create the original scalar poles from the remaining regular vector-valued section. No equality between the two displayed diagonals follows from (950.17), which is an adjunction at a single fixed weight.

The actual low-to-high comparison, or the full high-weight theta saturation of R946, remains necessary to deduce nonvanishing of R936's sum by this route. No claim about the same-label $Q'_h(0)$ follows either; the exact central counterexamples in R945 remain in force. The original $d_1$, $m_{\mathrm I}$, $c_h^{\mathrm F}$ and full norm transports are not recomputed or discarded.

## Dependencies and computation scope

- R944: the positive KS and Hasse-derivative normalization, horizontal conjugate line, and original CM homotopy.
- R947 §§3–4 and 6: the complete principal parts, the proved nonzero original class $z_V$, and the exact low-weight Serre residue formula.
- R918 §3: the complete weight-four tame invariant space, including integral base change.
- R942 §§2, 4–5: the determinant-five conjugate marking, both actual modular Hecke arrows, and their complete simple zero-primary space.
- R913 §7: original norm, determinant, transpose and Hecke scale transports.

The new isogeny and adjunction argument is proved in §§2–4 above. No finite mathematical computation or additional numerical test was executed for this result.
