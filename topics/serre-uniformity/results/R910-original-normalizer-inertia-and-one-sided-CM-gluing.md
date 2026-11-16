# R910 — Original normalizer inertia and the remaining CM gluing branch

Date: 2026-11-16. Status: **proved for the original objects of R908**. The actual normalizer action removes the $r=p-1$ branch of R908 and restricts its remaining nontrivial branch to the upper half of the original primitive labels. The original Tate indices and the distinction between good-model Hodge content and the contracted component's normal coefficient remain in force.

## 1. Objects and statement

Use precisely [R908](R908-original-finite-flat-CM-quotient-and-two-gluing-scales.md), including its positive CM order, its original $c_0$ rigidification and $c_1$ centering, and
$$
n=p+1,\quad e=p^2-1,\quad
\mathcal H=\{1\le h\le p:\ h\equiv1\pmod6,\ (h,n)=1\},
\quad t_h=(p-1)h.
\tag{910.1}
$$
Thus $p\ge41$, $p\equiv2,5\pmod9$, and $n$ is divisible by $6$. The source Raynaud abelian part has
$$
B_k=B_{\mathrm I}\times B_{\mathrm D},
\tag{910.2}
$$
with the actual Igusa and Drinfeld contributions after the normalizer and tame level-$6$ quotients.

For each $h$, R908 constructs the genuine finite-flat quotient
$$
B[p]\twoheadrightarrow\mathscr D_h
\xrightarrow{\phi_h}\mathscr A_h[p]
\tag{910.3}
$$
and retains the original Tate-image index $a_h$ through
$$
e_hq_B=[p^{a_h}]\circ f_h.
\tag{910.4}
$$
In the original Raynaud coordinate order its comparison scales are
$(s_0,s_1)=(0,r_h)$. R908 proves
$$
r_h\in\{0,p-1,\rho_h\},\qquad
\rho_h=\text{the least positive residue of }2h\bmod n.
\tag{910.5}
$$

The sharper assertion is
$$
\boxed{
\begin{aligned}
h<n/2&\quad\Longrightarrow\quad r_h=0,\\
h>n/2&\quad\Longrightarrow\quad r_h\in\{0,\,2h-n\}.
\end{aligned}}
\tag{910.6}
$$
The case $h=n/2$ does not occur, by primitivity. If $r_h>0$, the two additive lines in the strict dual-Lie injection of R908 go respectively to the Drinfeld and Igusa factors; this is a mixed source constraint, not the assertion that the nontrivial branch actually occurs.

## 2. Full inertia on the fine Drinfeld component

We use the actual fine models and right level action of Edixhoven–Parent, §2.2.3–4 and the proofs of Theorems 3.1 and 3.3. On full level the tame inertia element represented by $u\in\mathbf F_{p^2}^{\times}$ changes the pairing index by $u^{-p-1}$. The geometric Cartan element corresponding to $u$ has determinant $u^{p+1}$, so composing with it restores that index.

Their diagonalized formal parameters have Cartan eigenvalues $u^p,u$. The blow-up denominator contributes $u^{-1}$ to each parameter under inertia. Consequently this composite, representing inertia on the Cartan quotient, acts as
$$
(\widetilde\alpha,\widetilde\beta)
\longmapsto (u^{p-1}\widetilde\alpha,\widetilde\beta).
\tag{910.7}
$$
Here the numerator's first-order transformation suffices because these are the special-fiber blow-up coordinates. The tame marking and its formal parameter are defined over an unramified ring; no new action on the level-$6$ marking is introduced.

Put $q_u=u^{p-1}$, so $q_u^n=1$. In the original quotient coordinates of Edixhoven–Parent (19)–(23),
$$
u_1=\widetilde\alpha^{p+1},\quad
V=\widetilde\alpha\widetilde\beta,\quad
U=u_1-aN/2,\qquad
U^2=V^{p+1}+A_{\rm ns}.
\tag{910.8}
$$
Equation (910.7) therefore fixes $U$ and sends $V$ to $q_uV$. The normalizer involution sends $(U,V)$ to $(-U,-V)$. Hence on its actual quotient
$$
X=V^2,\quad Y=UV,\qquad
D^+:\ Y^2=X\bigl(X^{(p+1)/2}+A_{\rm ns}\bigr)
\tag{910.9}
$$
the complete inertia action is
$$
\boxed{(X,Y)\longmapsto(q_u^2X,q_uY).}
\tag{910.10}
$$
In particular this is not an extension guessed from the norm-one subgroup. For $u\in\mu_{p+1}$ it gives $q_u=u^{-2}$, consistent with the original normalizer-component action already used in R376.

There exists an actual tame inertia element with $q_u=-1$. Indeed, if $\xi$ generates $\mathbf F_{p^2}^{\times}$, take the image
$$
u_{\mathrm D}=\xi^{n/2};
\qquad u_{\mathrm D}^{p-1}=\xi^{e/2}=-1.
\tag{910.11}
$$
Choose any lift to tame inertia. Only its action on this finite special fiber is used; no assertion about its order in the absolute Galois group is needed. Equation (910.10) becomes
$$
(X,Y)\longmapsto(X,-Y).
\tag{910.12}
$$

This is the hyperelliptic involution of the smooth projective normalization. It induces $[-1]$ on its Jacobian: if $P,Q$ are points, then
$P+\iota P$ and $Q+\iota Q$ are fibers of the same degree-two map, and thus
$[\iota P-\iota Q]=-[P-Q]$ in $\operatorname{Pic}^0$.

The same sign holds for the dual Jacobian and its Lie algebra. Cartier duality or passage to an inverse action does not change the sign of $[-1]$. As an optional coordinate check, the holomorphic basis is
$$
X^j\,dX/Y,\qquad
0\le j<\left\lfloor\frac{p+1}{4}\right\rfloor.
\tag{910.13}
$$
Its $q_u$ weights $2j+1$ are all odd. The genus here is $(p-1)/4$ for $p\equiv1\pmod4$ and $(p+1)/4$ for $p\equiv3\pmod4$; no common even-degree formula is being used.

Inertia fixes the underlying supersingular elliptic curve and the unramified tame marking. It therefore does not permute the fine Drinfeld components. Its action commutes with the tame level quotient. On a quotient component, pullback on the Jacobian followed by norm is multiplication by the quotient degree, a $p$-adic unit. Thus its action on the quotient's dual Lie space is still $-1$. Rational exceptional components contribute no abelian factor. We have proved for the actual source
$$
\boxed{u_{\mathrm D}\bigm|
\operatorname{Lie}(B_{\mathrm D}^{\vee})=-1.}
\tag{910.14}
$$

## 3. The extra Igusa inertia kernel after the normalizer

The normalizer also enlarges the kernel on the actual Igusa contribution:
$$
\boxed{\mu_{2(p+1)}\text{ acts pointwise on }B_{\mathrm I}.}
\tag{910.15}
$$
Here $\mu_{2(p+1)}$ is the inverse image of $\{1,-1\}$ under
$\operatorname{Norm}:\mathbf F_{p^2}^{\times}\to\mathbf F_p^{\times}$.
Its order divides $e$ because $p-1$ is even.

For norm $1$, pointwise triviality on the full-level Igusa part is Edixhoven–Parent §2.2.4 and is already used in R908. We give the missing norm $-1$ case using the original moduli interpretation.

An ordinary full-level point is a kernel line $\ell\subset\mathbf F_p^2$, together with the induced isomorphism
$\mathbf F_p^2/\ell\to E[p](k)$; see their §2.1. Inertia changes the pairing index but leaves this ordinary special-fiber datum and the tame marking unchanged. Choose the representative line used in their Theorem 3.3: it is spanned by $P_1+P_2$, and the actual normalizer element
$$
w_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\tag{910.16}
$$
in the $(P_1,P_2)$ basis has determinant $-1$. It fixes $\ell$ with eigenvalue $+1$ and acts by $-1$ on $\mathbf F_p^2/\ell$.

If $\operatorname{Norm}(u)=-1$, inertia sends the index $i$ to $-i$. Composing with $w_1$ restores $i$ and changes the Igusa generator only by $-1$. That change is already identified by the scalar $-I$ in the Cartan. This proves pointwise identity on the dense ordinary part of the normalizer Igusa quotient, hence on its normalization. Conjugating the chosen representative proves it on every Igusa orbit.

This argument covers both possibilities in Theorem 3.3: two Igusa parts of type $\mathrm{Ig}(p)/C_4$ when $p\equiv1\pmod4$, and one of type $\mathrm{Ig}(p)/\{\pm1\}$ when $p\equiv3\pmod4$. It does not assume that the unquotiented Igusa curves have the same number of components. The original tame level-$6$ quotient preserves this pointwise kernel. This proves (910.15).

Consequently every inertia exponent in the dual Lie of the Igusa contribution is divisible by $2n$:
$$
b\text{ occurs in }\operatorname{Lie}(B_{\mathrm I}^{\vee})
\quad\Longrightarrow\quad 2n\mid b.
\tag{910.17}
$$
The sign of a dual convention is immaterial to this divisibility.

## 4. Removing the $p-1$ branch

Suppose $r_h>0$. R908 proves that $\mathscr D_{h,k}\simeq\alpha_p^2$ and constructs the strict map
$$
\omega_{\mathscr D_{h,k}}
\simeq\operatorname{Lie}(\mathscr D_{h,k}^{\,D})
\hookrightarrow\operatorname{Lie}(B_k^\vee).
\tag{910.18}
$$
Its two characters, in the original coordinate convention, are
$$
t_h,\qquad b_h=pt_h-r_h\pmod e.
\tag{910.19}
$$
This is the Cartier-dual closed-immersion argument of R908, not an invalid cotangent-injectivity assertion for a finite-flat quotient.

If $r_h=p-1$, then
$$
b_h=(p-1)(ph-1).
\tag{910.20}
$$
It cannot come from the Igusa contribution even using the weaker kernel $\mu_n$ of R908. Indeed, $n\mid b_h$ would give $2h\equiv-2\pmod n$. For $1\le h\le n-1$, this means
$h=(p-1)/2$ or $h=p$. Neither is $1\bmod6$: the first is $2\bmod3$ and the second is $5\bmod6$.

It must therefore come from the Drinfeld contribution. But on its line the element (910.11) has value
$$
u_{\mathrm D}^{b_h}
=(-1)^{ph-1}=+1,
\tag{910.21}
$$
because both $p$ and $h$ are odd. This contradicts (910.14). Thus
$$
r_h\ne p-1.
\tag{910.22}
$$

## 5. The remaining branch lies in the upper half

If $r_h>0$, equations (910.5) and (910.22) force $r_h=\rho_h$.
Set
$$
\epsilon_h=
\begin{cases}
0,&2h<n,\\
1,&2h>n.
\end{cases}
\qquad
\rho_h=2h-\epsilon_h n.
\tag{910.23}
$$
The inequalities are strict by primitivity. Also $\rho_h\ne p-1$, by the same two impossible labels used in §4.

The second character becomes
$$
b_h=p(p-1)h-\rho_h
=n\bigl((p-2)h+\epsilon_h\bigr).
\tag{910.24}
$$
It is not divisible by $p-1$, since $0<\rho_h<p-1$. By R908's actual kernel $\mu_{p-1}$ on the Drinfeld contribution, this line cannot map into $\operatorname{Lie}(B_{\mathrm D}^{\vee})$. The direct product (910.2) and tame semisimplicity therefore put its nonzero image entirely in the Igusa contribution.

Equation (910.17) now gives
$$
(p-2)h+\epsilon_h\equiv0\pmod2.
\tag{910.25}
$$
Since $(p-2)h$ is odd, $\epsilon_h=1$. This proves (910.6).

For completeness the first character in (910.19) cannot belong to the Igusa contribution: $n\mid(p-1)h$ would imply $n\mid2h$, contradicting $(h,n)=1$ and $n>2$. Hence in the nontrivial branch the two character lines of (910.18) necessarily have the distinct destinations
$$
k\,dy_0\hookrightarrow\operatorname{Lie}(B_{\mathrm D}^{\vee}),
\qquad
k\,dy_1\hookrightarrow\operatorname{Lie}(B_{\mathrm I}^{\vee}).
\tag{910.26}
$$
No ordinary-reduction property of an Igusa Jacobian is assumed.

## 6. Content for the same original map

Let $I_h$ be the ideal of the coefficients of $f_h^*\omega_h$ in the good-model invariant differentials of $B$, as in R908. That result proves
$$
r_h=0\Longrightarrow I_h=R,\qquad
r_h>0\Longrightarrow I_h\subseteq\varpi^{pr_h}R.
\tag{910.27}
$$
Therefore the lower-half labels satisfy
$$
\boxed{h<n/2\Longrightarrow I_h=R,\qquad
\operatorname{content}_\varpi\bigl((e_hq_B)^*\omega_h\bigr)=ea_h.}
\tag{910.28}
$$
For an upper-half nontrivial branch the original content bound is
$$
r_h=2h-n>0
\Longrightarrow
\operatorname{content}_\varpi\bigl((e_hq_B)^*\omega_h\bigr)
\ge ea_h+p(2h-n).
\tag{910.29}
$$
These are statements about the actual $q_B$ and its recorded index. They neither set $a_h=0$ nor replace the given quotient by an optimal one.

They also do not identify the first normal coefficient on the contracted $D_1$ of R376. The comparison from this global good-model column to the specified integral $36$-source column and then to the same-$h$ jet of R897–R898 remains necessary. In particular (910.28) is not a substitute for
$P_{h-1}(1/s)f_i g_{N-1-i}\ne0$ or for the height conclusion.

## Sources

- Edixhoven–Parent, [*Semistable reduction of modular curves associated with maximal subgroups in prime level*](https://arxiv.org/pdf/1907.02418), §2.1 (ordinary Igusa data), §2.2.3–4 ((8)–(13), level and inertia conventions), Theorem 3.1 ((16)–(21), Cartan coordinates), and Theorem 3.3 ((22)–(23), the genuine normalizer quotient). The complete $u$ action and enlarged Igusa kernel above are derived from these actual models.
- [R376](R376-actual-cm-drinfeld-point-and-component-contraction.md), original normalizer component and its contraction.
- [R906](R906-original-period-lattice-and-integral-CM-Tate-image.md), actual $q$, period/source decomposition, and retained Tate image.
- [R908](R908-original-finite-flat-CM-quotient-and-two-gluing-scales.md), the genuine finite-flat quotient, strict dual-Lie injection, and original Hodge-content bounds.

