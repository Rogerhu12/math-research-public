# R908 — The original finite-flat CM quotient: two possible nontrivial gluing scales

Date: 2026-11-16. Status: **proved for the original objects and primes specified below**. This paper constructs the actual finite-flat quotient after recording the original Tate-image index, classifies its possible nontrivial coordinate scales, and bounds the resulting good-model Hodge content. It does not identify a unit normal coefficient on the contracted original CM component.

## 1. Original quotient and its retained Tate indices

Keep all the objects of [R906](R906-original-period-lattice-and-integral-CM-Tate-image.md):
$$
p\ge41,\quad p\equiv2,5\pmod9,\quad
n=p+1,\quad e=p^2-1,\quad
R=R_0[\varpi],\quad\varpi^e=p.
\tag{908.1}
$$
The actual positive primitive quotient is
$$
q:J_{X_p}\longrightarrow A=A_{\theta,1},
\tag{908.2}
$$
with the original $c_0:a=0$ rigidification and $c_1:a=1$ centering. Its Raynaud factorization is
$$
q_G:G\longrightarrow B\xrightarrow{q_B}A_L,
\tag{908.3}
$$
where $B$ denotes the good-reduction abelian part, as in R906. No different optimal quotient or rescaling of $q$ is selected.

Let
$$
\mathcal H=\{1\le h\le p:\ h\equiv1\pmod6,\ (h,n)=1\},
\qquad t_h=(p-1)h.
\tag{908.4}
$$
By R390 and R859, the original integral local projectors $e_h$ cut the complete good-model BT group of $A$ into height-two, dimension-one groups $\mathscr A_h$. Their positive CM coordinate character is $t_h$. This is an integral target decomposition, not an asserted integral projector on the source Jacobian.

R906 identifies the **actual** stable image
$$
M=q(T_pJ_{X_p})=q_B(T_pB)\subset T_pA.
\tag{908.5}
$$
The stable-lattice theorem R390(390.19–22), in the positive labeling of R859, gives unique integers $a_h\ge0$ such that
$$
e_hM=p^{a_h}T_p\mathscr A_h.
\tag{908.6}
$$
The inequalities $a_h\ge0$ use the containment in (908.5). The integers are not assumed to vanish.

Consider now the Tate-module homomorphism
$$
p^{-a_h}e_hq_B:T_pB\longrightarrow T_p\mathscr A_h.
\tag{908.7}
$$
It is integral and surjective by (908.6). The full faithfulness for **complete** BT groups used in R390 §4 gives a unique actual homomorphism
$$
f_h:\mathscr B=B[p^\infty]_R\longrightarrow\mathscr A_h
\tag{908.8}
$$
with this Tate map. Uniqueness preserves its original semilinear descent. In the category of complete BT groups one has the exact equality of homomorphisms
$$
\boxed{e_hq_B=[p^{a_h}]\circ f_h.}
\tag{908.9}
$$
This keeps the original $p$ index explicitly. We do not infer that $f_h$ is a flat quotient from its surjective Tate map.

## 2. A genuine finite-flat quotient, with the original quadratic action

The generic-fiber map
$$
(f_h[p])_L:B[p]_L\longrightarrow\mathscr A_h[p]_L
\tag{908.10}
$$
is surjective: over characteristic zero this is the reduction modulo $p$ of the surjection of Tate lattices. Let $H_{h,L}$ be its kernel and let $\mathscr H_h$ be its schematic closure in $B[p]_R$. A closure of a generic subgroup in a finite flat group over a DVR is a finite flat subgroup. Set
$$
\mathscr D_h=B[p]_R/\mathscr H_h,\qquad
\pi_h:B[p]_R\twoheadrightarrow\mathscr D_h.
\tag{908.11}
$$
Thus $\mathscr D_h$ is finite flat of order $p^2$, and formation of this quotient commutes with base change. Since $f_h[p]$ kills $\mathscr H_h$ by flatness and generic density, it induces an actual morphism
$$
\phi_h:\mathscr D_h\longrightarrow\mathscr A_h[p],
\qquad f_h[p]=\phi_h\pi_h,
\tag{908.12}
$$
whose generic fiber is an isomorphism.

The structure needed for Raynaud's classification is present on this specific quotient. Let $\delta$ be the original deck transformation $a\mapsto\zeta a$. R575(575.21) identifies its action on the positive CM quotient with $[\zeta]$, simultaneously for the full Tate realization. Functoriality induces its action on $B$, and (908.7–8) are equivariant for it. The generic kernel in (908.10), and hence its closure, are $\delta$-stable. Therefore $\delta$ acts on $\mathscr D_h$.

On the generic fiber of $\mathscr D_h$ the endomorphism $\delta^2+\delta+1$ vanishes. It consequently vanishes on the finite flat group itself. Since $[p]=0$ on $\mathscr D_h$ and $\Phi_3$ is irreducible modulo $p$,
$$
\mathbf F_p[\delta]/(\delta^2+\delta+1)
=\mathbf F_{p^2}
\tag{908.13}
$$
acts on $\mathscr D_h$, compatibly with $\phi_h$. This argument does not assert that $\Phi_3(\delta)=0$ on the entire source $B$; its $\delta$-fixed part is allowed.

The generic fiber is one-dimensional over $\mathbf F_{p^2}$. Its augmentation algebra has every multiplicative character of $\mathbf F_{p^2}^{\times}$ once. Since $p^2-1$ is a unit and the coordinate algebra is finite free over $R$, the corresponding character summands are free of rank one over $R$. This verifies the rank-one character condition in Raynaud's classification on the actual $\mathscr D_h$.

## 3. The two-coordinate Raynaud comparison

Use the two fundamental characters of $\mathbf F_{p^2}^{\times}$ in the original positive CM order, denoted $\chi_0$ and $\chi_1=\chi_0^p$.

The reference complete CM BT group in R390 is defined over the unramified ring before applying its finite twist. For its $p$ kernel one may choose Raynaud coordinates $x_0,x_1$ with
$$
x_0^p=A_0x_1,\qquad x_1^p=A_1x_0,
\qquad v_\varpi(A_0)=0,\quad v_\varpi(A_1)=e.
\tag{908.14}
$$
One way to see the ordered valuations is to use its unramified cotangent module: it is $R_0/p$ in the positive CM embedding and zero in the other embedding. The differentials of the two Raynaud equations give these same two valuations. Transport by the complete-BT comparison preserves them. The positive order is therefore fixed; reversing the coordinates would change the statement.

By Raynaud, Corollary 1.5.1 and §3.3, choose coordinates $y_0,y_1$ on $\mathscr D_h$ with
$$
y_0^p=D_0y_1,\qquad y_1^p=D_1y_0,\qquad
0\le v_\varpi(D_i)\le e.
\tag{908.15}
$$
The associated dual parameters $\widetilde D_i$ satisfy
$D_i\widetilde D_i=w$, where $w$ is $p$ times a unit. The actual generically invertible morphism (908.12) has
$$
\phi_h^*x_0=c_0y_0,\qquad
\phi_h^*x_1=c_1y_1,\qquad
c_i\in R\setminus\{0\}.
\tag{908.16}
$$
Put $s_i=v_\varpi(c_i)\ge0$. Comparing the equations gives
$$
v_\varpi(D_0)=s_1-ps_0,\qquad
v_\varpi(D_1)=e+s_0-ps_1.
\tag{908.17}
$$
In particular
$$
s_1\ge ps_0,\qquad ps_1\le e+s_0.
\tag{908.18}
$$
Their combination gives $es_0\le e$, hence $s_0\le1$. If $s_0=1$, both inequalities force $s_1=p$. If $s_0=0$, they give $0\le s_1\le p-1$. Thus the complete list at this stage is
$$
(s_0,s_1)=(0,r),\quad0\le r\le p-1,
\qquad\text{or}\qquad (s_0,s_1)=(1,p).
\tag{908.19}
$$
These are valuations for the actual generic isomorphism $\phi_h$, not valuations chosen by replacing its source with an arbitrary finite-flat model.

## 4. The original special-fiber action excludes the last case

Let $\tau$ and $\sigma=\tau^{e/2}$ be as in R906:
$$
\tau(\varpi)=\xi\varpi,\qquad
\sigma(\varpi)=-\varpi,\qquad \xi\in\mu_e\ \text{primitive}.
\tag{908.20}
$$
R906 used the triviality of $\sigma$ on the period graph. Here we need the stronger abelian-part statement, which follows from the same actual model.

Edixhoven–Parent prove in Theorem 3.1 that inertia $-1$ acts pointwise on the special fiber of the fine Cartan quotient. Passing to the normalizer and to the original tame $H_6$ quotient preserves that property on every positive-genus normalized component. Exceptional resolution components have genus zero. The abelian part of the generalized Jacobian is the product of the Jacobians of those normalizations. Consequently
$$
\sigma|B_k=1.
\tag{908.21}
$$
The actual quotient (908.11) is descent-equivariant, so the faithfully flat map
$B_k[p]\to\mathscr D_{h,k}$ implies
$$
\sigma|\mathscr D_{h,k}=1
\tag{908.22}
$$
as an action on the group scheme, not merely on its geometric points.

In the transported reference coordinates, $\tau$ acts with characters
$$
x_0:\ t_h,\qquad x_1:\ pt_h\pmod e.
\tag{908.23}
$$
Both are even, so $\sigma$ is trivial on these target character lines. For any nonzero $c\in R$, reduction of $\sigma(c)/c$ is
$(-1)^{v_\varpi(c)}$. Applying this to (908.16) shows that the two source character lines have $\sigma$ eigenvalues
$$
(-1)^{s_0},\qquad(-1)^{s_1}.
\tag{908.24}
$$
Equation (908.22) therefore forces both $s_i$ to be even. In particular
$$
\boxed{(s_0,s_1)=(0,r),\qquad
r\in\{0,2,\ldots,p-1\}.}
\tag{908.25}
$$
The $(1,p)$ case is excluded without asserting that the absolute Galois element $\sigma$ has order two.

## 5. The two actual inertia kernels on the source

The source supplies more than (908.21). Write the special-fiber abelian part as the product of its Igusa and Drinfeld contributions:
$$
B_k=B_{\mathrm I}\times B_{\mathrm D}.
\tag{908.26}
$$
The notation includes all the actual tame quotients and all normalized positive-genus components of each kind.

The original model has the following two pointwise inertia kernels:
$$
\mu_{p+1}\ \text{acts trivially on }B_{\mathrm I},\qquad
\mu_{p-1}\ \text{acts trivially on }B_{\mathrm D}.
\tag{908.27}
$$
For the first assertion, Edixhoven–Parent §2.2.4 states that the norm-one subgroup is trivial on every full-level Igusa part. This remains true after the geometric quotients.

For the second, take $u\in\mathbf F_p^\times\subset\mathbf F_{p^2}^\times$. On full level the inertia action changes the Weil-pairing component by $u^{-2}$. The geometric scalar $uI$ belongs to the non-split Cartan and changes that component by $u^2$. Compose these two actions to represent inertia on the Cartan quotient. In the actual blow-up parameters
$$
\alpha=\overline{T(P)/\varpi},\qquad
\beta=\overline{T(Q)/\varpi},
\tag{908.28}
$$
the denominator contributes $u^{-1}$ and the geometric scalar contributes $u$ to each coordinate. The composite is the identity. This calculation uses the scalar linear term
$T([u]P)\equiv uT(P)$ and the same fundamental character as (908.20). It proves pointwise identity on the dense affine part of every Drinfeld component, hence on its normalization. The geometric and Galois actions commute, so the normalizer and tame $H_6$ quotients preserve the conclusion.

The two kinds of components cannot be interchanged by these tame quotients: an Igusa component dominates the tame modular base, whereas a Drinfeld component lies over a supersingular point. Rational resolution chains contribute no abelian factor. This proves (908.26–27) for the actual source, rather than only for an unmarked coarse curve.

It follows equally for the dual abelian variety that every inertia character occurring in
$\operatorname{Lie}(B_k^\vee)$ is trivial on one of these two subgroups. In exponent notation its exponent is divisible by $p+1$ or by $p-1$.

## 6. Cartier duality gives the required strict map

Suppose $r>0$ in (908.25). Equation (908.17) becomes
$$
v_\varpi(D_0)=r,\qquad
v_\varpi(D_1)=e-pr.
\tag{908.29}
$$
All four parameters $D_0,D_1,\widetilde D_0,\widetilde D_1$ have positive valuation: for $1\le r\le p-1$,
$$
0<r<e,\qquad 0<e-pr<e.
\tag{908.30}
$$
Raynaud's comultiplication formula now reduces to addition. Indeed its denominators $w_\chi$ are units by his Proposition 1.3.1, and every nonlinear term contains at least one dual parameter. Thus
$$
\mathscr D_{h,k}\simeq\alpha_p^2,
\qquad
\omega_{\mathscr D_{h,k}}
=k\,dy_0\oplus k\,dy_1.
\tag{908.31}
$$
The two inertia characters are, by (908.16) and (908.23),
$$
t_h,\qquad pt_h-r\pmod e.
\tag{908.32}
$$

One must not claim that the finite-flat quotient
$B_k[p]\to\mathscr D_{h,k}$ injects its cotangent space into that of $B_k$. Such a claim fails already for the Frobenius quotient of a supersingular elliptic $p$ kernel.

Instead take the actual Cartier dual of this quotient:
$$
\mathscr D_{h,k}^{\,D}\hookrightarrow B_k^\vee[p].
\tag{908.33}
$$
It is a closed immersion, hence gives an injection on Lie algebras. For an additive $\alpha_p^2$ the truncated exponential pairing
$$
\prod_{i=0}^1
\left(\sum_{j=0}^{p-1}\frac{(y_i z_i)^j}{j!}\right)
\tag{908.34}
$$
identifies the Lie representation of its Cartier dual with its original cotangent representation:
$$
\operatorname{Lie}(\mathscr D_{h,k}^{\,D})
\simeq\omega_{\mathscr D_{h,k}}.
\tag{908.35}
$$
This is equivariant for the semilinear descent convention of R390. In particular it introduces no Frobenius twist of (908.32): a coordinate scaling has the inverse scaling on the dual group, whose Lie representation is precisely the original cotangent representation.

Equations (908.33–35) give the strict injection that is actually needed:
$$
\omega_{\mathscr D_{h,k}}
\hookrightarrow\operatorname{Lie}(B_k^\vee).
\tag{908.36}
$$
Together with (908.27), the second character in (908.32) must satisfy
$$
p-1\mid pt_h-r
\qquad\text{or}\qquad
p+1\mid pt_h-r.
\tag{908.37}
$$
The first alternative gives $r=p-1$, since $0<r\le p-1$. The second gives
$$
r\equiv2h\pmod{p+1}.
\tag{908.38}
$$
Let $\rho_h$ be the least positive residue of $2h$ modulo $p+1$. Primitivity and $p+1\ge42$ give
$$
0<\rho_h\le p-1,\qquad \rho_h\ \text{even}.
\tag{908.39}
$$
Moreover $\rho_h\ne p-1$: equality would force
$h=p$ or $h=(p-1)/2$, neither of which is $1\pmod6$.

We have proved the actual finite-flat classification needed here:
$$
\boxed{r\in\{0,\ p-1,\ \rho_h\},\qquad
\rho_h\equiv2h\pmod{p+1}.}
\tag{908.40}
$$
This is an allowed-list theorem. It does not assert that either nonzero value occurs for the original quotient, or that it is absent.

## 7. Good-model differential content

Let $\omega_h$ be a unit invariant differential on the height-two, dimension-one group $\mathscr A_h$, in its original positive CM embedding. Let
$I_h\subset R$ be the ideal generated by the coefficients of
$f_h^*\omega_h$ in any basis of $\omega_B$. It is independent of a change of integral basis or a unit change of $\omega_h$.

If $r=0$, both $c_i$ in (908.16) are units, so $\phi_h$ is an isomorphism. Thus
$$
(f_h[p])_k:B_k[p]\twoheadrightarrow\mathscr A_{h,k}[p]
\tag{908.41}
$$
is a faithfully flat map between $p$ kernels of complete BT groups. This implies
$$
\boxed{I_h=R\qquad(r=0).}
\tag{908.42}
$$
For clarity, this implication is a BT strictness statement, not the false cotangent assertion avoided above. Contravariant Dieudonné theory sends (908.41) to an injection modulo $p$ of the full Dieudonné lattices. The lattice cokernel is therefore free and is stable under $F,V$. Because $V$ is injective on that free quotient, the injection is strict for the Hodge filtration. The induced cotangent map is consequently primitive. Equivalently the complete-BT kernel in the special fiber has the expected height and gives the exact Hodge sequence.

If $r>0$, (908.29) gives the integral cotangent module
$$
\omega_{\mathscr D_h}
=
R/(D_1)\,dy_0\ \oplus\ R/(D_0)\,dy_1.
\tag{908.43}
$$
The positive target generator pulls back to the unit multiple $c_0dy_0$. Since $D_1$ has valuation $e-pr$, its image under $\pi_h^*$ in
$$
\omega_{B[p]}=\omega_B/p\omega_B
\tag{908.44}
$$
is annihilated by $\varpi^{e-pr}$. This module is free over $R/p$, so that image lies in
$\varpi^{pr}\omega_B/p\omega_B$. Since $pr<e$, lifting back to the full differential gives
$$
\boxed{I_h\subset\varpi^{pr}R
\qquad(r>0).}
\tag{908.45}
$$
In particular the reduction of the differential of $f_h$ is zero.

There is also a direct check of this vanishing. For a BT$_1$ source, $\operatorname{im}V=\ker F$. Every morphism to $\alpha_p$ kills $\operatorname{im}V$, so factors through $F$ and has zero differential. Apply this to both coordinates of the actual quotient in (908.31).

Finally (908.9) gives the exact original scaling
$$
(e_hq_B)^*\omega_h=p^{a_h}f_h^*\omega_h.
\tag{908.46}
$$
Thus the coefficient ideal of the original good-model pullback is exactly $p^{a_h}I_h$. Its $\varpi$ valuation is
$$
\boxed{
\begin{cases}
e\,a_h,&r=0,\\
\ge e\,a_h+p\,r,&r\in\{p-1,\rho_h\}.
\end{cases}}
\tag{908.47}
$$
The second line is a lower bound, not an asserted equality. Neither $a_h$ nor the nonzero gluing case has been discarded.

## 8. What this establishes, and what remains distinct

The construction records three separate objects: the original Tate index $a_h$, the actual finite-flat quotient $\mathscr D_h$, and its coordinate defect $r$. Complete-BT full faithfulness constructs $f_h$ from its integral Tate map; it does not identify $\mathscr D_h$ with the $p$ kernel of a complete BT quotient. In fact Raynaud's criterion in Remark 1.5.4 shows precisely why the positive-$r$ model, whose four parameters are nonunits, is not such a $p$ kernel.

The new source geometry restricts a possible failure of good-model Hodge primitivity to the two original scales in (908.40). The two possibilities are detected through the actual Igusa/Drinfeld inertia kernels and the strict Cartier-dual Lie inclusion. No hypothesis of ordinary reduction of an Igusa Jacobian is used.

This still concerns the global good-model map out of the Raynaud abelian part. Restriction to the marked original disk on $D_1$ is another map. R376's contraction, the original parameter of R859/R861, and the first normal-content ideal must all be retained. Even (908.42) does not give a unit value at that specific point.

Likewise the integral 36-source maps of R897/R898 and their prescribed $h$ and Legendre phase cannot be substituted for this particular cotangent column without an actual source comparison. An ambient unit vector is not an upper bound for the column in (908.46). Consequently neither the same-$h$ critical product of R770 nor the original height nonvanishing is claimed here.

## Original and primary sources

- [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md), especially (575.21–25): actual deck action and positive CM convention.
- [R390](R390-cm-coordinate-inertia-weight-one-channel-and-cartier-unit.md), §§3–4, and [R859](R859-original-prime-to-p-CM-model-and-normal-content-transport.md), (859.5–9), (859.17–19): actual stable-lattice projectors, complete-BT comparison, and coordinate characters.
- [R906](R906-original-period-lattice-and-integral-CM-Tate-image.md): actual Raynaud factorization and equality of integral Tate images, with the fixed scale of $q$.
- Michel Raynaud, [*Schémas en groupes de type $(p,\ldots,p)$*](https://www.numdam.org/item/10.24033/bsmf.1779.pdf), Proposition 1.3.1, Theorem 1.4.1, Corollaries 1.5.1–2, Remarks 1.5.3–4, §2.1 and §3.3: structure constants, character-line equations, duality, schematic closure, and generic-isomorphism scaling. The inequalities and the original-source restrictions are derived in this paper.
- Bas Edixhoven and Pierre Parent, [*Semistable reduction of modular curves associated with maximal subgroups in prime level*](https://arxiv.org/pdf/1907.02418), §2.2.3, (8–10); §2.2.4, (11–13); Theorem 3.1 and its proof; Theorem 3.3. The scalar cancellation in (908.28) compares the two actions before quotienting; it does not conflate them.
- The full-BT extension theorem is the Tate theorem already used with its precise scope in R390 §4. No low-ramification BT$_1$ uniqueness theorem is applied over $R$.

