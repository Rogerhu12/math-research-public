# R911 — Original Picard descent and the exact CM gluing dichotomy

Date: 2026-11-16. Status: **proved for the original objects of R908–R910**. The good-model finite-flat comparison has exactly one scale for each original primitive label. The proof distinguishes cotangent pullback from dual Lie descent; it does not identify either with a chosen component's normal jet.

## 1. Statement and retained indices

Keep the original positive primitive labels and models:
$$
p\ge41,\quad p\equiv2,5\pmod9,\quad
n=p+1,\quad e=p^2-1,\quad
\mathcal H=\{1\le h\le p:\ h\equiv1\pmod6,\ (h,n)=1\},
\quad t_h=(p-1)h.
\tag{911.1}
$$
The target order, rigidification at $c_0$, centering at $c_1$, and the original quotient $q$ are those of R906 and R908. In particular
$$
e_hq_B=[p^{a_h}]\circ f_h,\qquad a_h\ge0,
\tag{911.2}
$$
and $a_h$ is the actual Tate-image index, not a chosen normalization of the original map.

For the genuine quotient
$$
B[p]\twoheadrightarrow\mathscr D_h
\xrightarrow{\phi_h}\mathscr A_h[p]
\tag{911.3}
$$
constructed in R908, let $(s_0,s_1)=(0,r_h)$ be its original Raynaud comparison scales. Then
$$
\boxed{
r_h=
\begin{cases}
0,&h<n/2,\\
2h-n,&h>n/2.
\end{cases}}
\tag{911.4}
$$
Primitivity excludes equality. The first case is R910; the new assertion is that its upper-half alternative $r_h=0$ is impossible.

Let $I_h$ be the coefficient ideal of $f_h^*\omega_h$ in the good-model invariant differentials of $B$. Consequently
$$
I_h=R\quad(h<n/2),\qquad
I_h\subseteq\varpi^{p(2h-n)}R\quad(h>n/2).
\tag{911.5}
$$
The second containment is not asserted to be equality.

## 2. The two descent operations are different

Use the semilinear **coordinate-ring** convention of R390 §2. For an augmentation ideal $I_G$, the cotangent module
$$
\omega_G=I_G/I_G^2
\tag{911.6}
$$
inherits the coordinate-ring descent. The induced descent on its linear dual is
$$
(\sigma v)(\bar f)
=\sigma_R\bigl(v(\sigma^{-1}\bar f)\bigr),
\qquad
v\in\operatorname{Lie}(G)=\operatorname{Hom}_R(\omega_G,R).
\tag{911.7}
$$
On the special fiber tame inertia fixes $k$. Thus an eigenvalue $\chi(\sigma)$ on $\omega_G$ becomes $\chi(\sigma)^{-1}$ on $\operatorname{Lie}(G)$. This inverse is a linear-dual inverse; it is not a Frobenius twist.

For a smooth normalized component $C$ of the original semistable source, use its actual Picard descent. Abel–Jacobi pullback gives
$$
\omega_{J_C}\xrightarrow{\sim}H^0(C,\Omega_C^1).
\tag{911.8}
$$
This intertwines the coordinate-ring descent with the pullback on differentials used in the original component equations. Explicitly, if $a_P:C\to J_C$ is an Abel map, its Galois transform is $a_{\sigma P}$; changing $P$ changes $a_P$ by a translation. Translations act trivially on invariant differentials, so (911.8) is descent-compatible even if a componentwise auxiliary base point is not fixed. It does not replace the original global $c_0$.

The tangent description
$$
\operatorname{Lie}(J_C)\simeq H^1(C,\mathcal O_C)
\tag{911.9}
$$
is the natural Picard-functor construction from infinitesimal invertible sheaves. The Serre pairing
$$
H^1(C,\mathcal O_C)\times H^0(C,\Omega_C^1)\longrightarrow k
\tag{911.10}
$$
is descent-equivariant. Equations (911.7–10) give inverse characters on these two cohomology spaces.

The canonical principal polarization of $J_C$ is defined by the curve and is preserved by its descent data. Taking the product over the actual normalized components gives a descent-equivariant principal polarization of the special-fiber abelian part $B_k$. This also allows components to be permuted. Therefore
$$
\boxed{\operatorname{Lie}(B_k^\vee)\simeq
\operatorname{Lie}(B_k)\simeq\omega_{B_k}^{\,\vee}}
\tag{911.11}
$$
as representations with the original semilinear descent. In particular, it is not correct to identify the characters on $\operatorname{Lie}(B_k^\vee)$ with those on $\omega_{B_k}$.

For clarity, the use of Cartier duality in R908 has a different two-step effect. If
$\mathscr D_{h,k}=\alpha_p^2$ has additive coordinates $y_i$ of cotangent character $\chi_i$, the pairing
$$
\prod_{i=0}^1\sum_{j=0}^{p-1}\frac{(y_i z_i)^j}{j!}
\tag{911.12}
$$
gives dual coordinate $z_i$ of character $\chi_i^{-1}$. Applying (911.7) to the dual group reverses the character once more. Hence
$$
\operatorname{Lie}(\mathscr D_{h,k}^{\,D})
\simeq\omega_{\mathscr D_{h,k}}
\tag{911.13}
$$
has characters $\chi_i$, just as in R908. This does not conflict with (911.11): there is no asserted descent-equivariant self-duality of this particular $\alpha_p^2$ identifying its original coordinate lines with their duals.

The two maps used below must therefore be kept in their actual forms:
$$
\begin{aligned}
f_h^*&:\omega_{\mathscr A_h}\longrightarrow\omega_B,\\
\text{R908 dual injection}&:
\omega_{\mathscr D_{h,k}}
\longrightarrow\operatorname{Lie}(B_k^\vee)
\simeq\omega_{B_k}^{\,\vee}.
\end{aligned}
\tag{911.14}
$$

## 3. Exact half of the fine Drinfeld cotangent characters

R910 derives the full inertia action on every fine normalizer Drinfeld component:
$$
D^+:\ Y^2=X(X^{n/2}+A_{\rm ns}),\qquad
(X,Y)\longmapsto(q_u^2X,q_uY),\qquad
q_u=u^{p-1},\quad u\in\mathbf F_{p^2}^{\times}.
\tag{911.15}
$$
These are pullback transformations in the original coordinate-ring convention, not just values of an action on geometric points. For $u\in\mu_n$ they recover R376(376.22); the full-$u$ calculation is necessary to distinguish the two halves of the labels.

The standard holomorphic basis of the smooth projective normalization is
$$
X^j\,dX/Y,\qquad
0\le j<g_D,\quad
g_D=\left\lfloor\frac n4\right\rfloor.
\tag{911.16}
$$
Its characters are
$$
u^{(p-1)(2j+1)}.
\tag{911.17}
$$
The integers $2j+1$ in (911.17) are precisely the odd integers strictly between $0$ and $n/2$. To check the endpoint, if $p=4m+1$ they are $1,3,\ldots,2m-1$ and $n/2=2m+1$; if $p=4m+3$ they are $1,3,\ldots,2m+1$ and $n/2=2m+2$.

The tame level-$6$ quotient may remove characters by taking invariant subspaces, but it cannot add a new one. Pullback of a differential from a quotient component is injective because the finite quotient has degree prime to $p$; the action commutes with the original inertia. Inertia fixes each fine supersingular marked point, so no permutation of fine Drinfeld components creates additional characters. Rational exceptional components do not contribute to $B_k$.

It follows, for the actual source, that
$$
(\omega_{B_{\mathrm D}})_{t_h}=0
\qquad(h\in\mathcal H,\ h>n/2).
\tag{911.18}
$$
By (911.11), the corresponding possible primitive characters in
$\operatorname{Lie}(B_{\mathrm D}^\vee)$ instead lie in the upper half:
$$
q_u^{-(2j+1)}=q_u^{\,n-(2j+1)}.
\tag{911.19}
$$
This explains why the first character $t_h$ of a nontrivial R908 quotient is compatible with the upper-half branch. Using the lower-half list (911.17) in the dual-Lie injection would be an incorrect sign replacement.

## 4. No Igusa contribution to the primitive cotangent character

R910 proves the actual pointwise kernel
$$
\mu_{2n}\bigm| B_{\mathrm I}=1.
\tag{911.20}
$$
It follows on $\omega_{B_{\mathrm I}}$ as well. In fact its weaker subgroup $\mu_n$ already suffices here.

If the character $u^{t_h}$ were trivial on $\mu_n$, then
$$
n\mid(p-1)h
\quad\Longrightarrow\quad n\mid2h.
\tag{911.21}
$$
This is impossible because $(h,n)=1$ and $n>2$. Thus
$$
(\omega_{B_{\mathrm I}})_{t_h}=0
\qquad(h\in\mathcal H).
\tag{911.22}
$$
Combining (911.18) and (911.22) gives the exact absence needed for the upper half:
$$
\boxed{(\omega_{B_k})_{t_h}=0\qquad(h\in\mathcal H,\ h>n/2).}
\tag{911.23}
$$
No assertion about the ordinarity of an Igusa Jacobian has been made.

## 5. The upper-half branch is forced

Let $h>n/2$. R910 gives
$$
r_h\in\{0,2h-n\}.
\tag{911.24}
$$
Suppose $r_h=0$. R908's complete-BT argument in this branch gives
$I_h=R$. Equivalently, the reduction of
$$
f_h^*:\omega_{\mathscr A_h}\longrightarrow\omega_B
\tag{911.25}
$$
is nonzero. This equivalence uses that $\omega_B$ is free and $I_h$ is the ideal generated by the coordinates of the image of a generator of the rank-one source.

The source generator has character $t_h$ by the original positive CM comparison R390/R859. The actual morphism $f_h$ preserves semilinear descent; this was retained when it was extended from the original Tate map in R908. Thus (911.25) gives a nonzero vector of character $t_h$ in $\omega_{B_k}$, contrary to (911.23). Therefore
$$
r_h=2h-n>0.
\tag{911.26}
$$
Together with the lower-half conclusion of R910 this proves (911.4). Applying the already proved R908 content bounds gives (911.5) for the same maps.

## 6. Actual additive subgroups in the upper branch

This forced branch also gives a concrete source consequence. For $h>n/2$, the actual quotient has
$$
\mathscr D_{h,k}\simeq\alpha_p^2,\qquad
t_h,\quad
b_h=pt_h-(2h-n)
=n\bigl((p-2)h+1\bigr)
\tag{911.27}
$$
as the two cotangent characters. Its Cartier dual is a closed subgroup of
$B_k^\vee[p]$ by R908. By R910 the two Lie lines map respectively into
$\operatorname{Lie}(B_{\mathrm D}^\vee)$ and
$\operatorname{Lie}(B_{\mathrm I}^\vee)$.

In fact they give actual subgroup inclusions
$$
\alpha_{p,0,h}\hookrightarrow B_{\mathrm D}^\vee[p],
\qquad
\alpha_{p,1,h}\hookrightarrow B_{\mathrm I}^\vee[p].
\tag{911.28}
$$
To justify this strengthening, use the additive coordinates in (911.12) to split
$\mathscr D_{h,k}^{\,D}$ into its two inertia eigensubgroups. For either subgroup, its composite with the wrong product projection has zero Lie map by the character exclusion of R910. Any nonzero homomorphism from $\alpha_p$ to a finite group scheme over the perfect field $k$ is a closed immersion: its kernel is either $0$ or $\alpha_p$, since $\alpha_p$ has order $p$. A closed immersion has injective Lie map. Thus a zero Lie map forces the composite to be zero. The correct projection consequently remains a closed immersion. This proves (911.28), with Lie characters $t_h$ and $b_h$, respectively.

One may record a modest numerical consequence without any finite calculation. Distinct upper-half labels have distinct $b_h\bmod e$: dividing by $n$ reduces this to
$$
(p-2)(h-h')\equiv0\pmod{p-1}
\quad\Longrightarrow\quad h\equiv h'\pmod{p-1},
\tag{911.29}
$$
and two distinct numbers in the upper half cannot differ by $p-1$. Their nonzero Lie images are therefore independent. With
$a(A)=\dim_k\operatorname{Hom}(\alpha_p,A)$, this gives
$$
a(B_{\mathrm I}^\vee)
\ge
\#\{h\in\mathcal H:\ h>n/2\}.
\tag{911.30}
$$
This lower bound is a consequence of the original quotients and their retained finite-flat comparison. It is not a claim that the displayed lines exhaust the Igusa $a$-space, nor an assumption that it is ordinary.

## 7. Original-map and normal-coefficient boundary

Multiplication by the retained factor in (911.2) gives
$$
\operatorname{content}_\varpi\bigl((e_hq_B)^*\omega_h\bigr)
=
ea_h\quad(h<n/2),
\tag{911.31}
$$
and
$$
\operatorname{content}_\varpi\bigl((e_hq_B)^*\omega_h\bigr)
\ge ea_h+p(2h-n)\quad(h>n/2).
\tag{911.32}
$$
The exact scale dichotomy does not determine the indices $a_h$. The second lower bound is not an exact value.

The vector in (911.31) is a primitive vector in the full good-model differential module after its recorded index is removed. It is not a primitive restriction at the original CM point or on the contracted component $D_1$. R376's actual contraction remains applicable. The further comparison with the specified integral source column in R897–R898 and its critical same-$h$ coefficient is still required. Neither the subgroup inclusions (911.28) nor the global content statements imply the desired original three-factor unit or the height conclusion.

## Sources

- [R908](R908-original-finite-flat-CM-quotient-and-two-gluing-scales.md), original finite-flat quotient, strict dual-Lie map, retained index, and content statements.
- [R910](R910-original-normalizer-inertia-and-one-sided-CM-gluing.md), original full inertia action, normalizer kernels, and the initial one-sided alternative.
- [R390](R390-cm-coordinate-inertia-weight-one-channel-and-cartier-unit.md), §§2–4, coordinate-ring descent and its inverse Tate convention; the positive original realization is retained as in R859.
- Milne, [*Jacobian Varieties*](https://jmilne.org/math/xnotes/JVs.pdf), Propositions 1.9, 2.1–2.2 and Theorem 6.6 / Summary 6.11: actual Picard descent, tangent/cotangent identifications, and canonical principal polarization. Formula (911.7) and the explicit two inverses in (911.12–13) fix the conventions used here.
- Edixhoven–Parent, [*Semistable reduction of modular curves associated with maximal subgroups in prime level*](https://arxiv.org/pdf/1907.02418), §2.2.3–4 and Theorems 3.1, 3.3, as transported to the original level in R910.

