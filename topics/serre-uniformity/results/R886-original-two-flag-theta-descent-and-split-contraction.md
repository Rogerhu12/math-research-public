# R886 — Actual two-flag theta descent and the original split coefficient

Date: 2026-11-16. Status: proved geometric descent and integral theta contractions. The exact formulas recover the original finite split vector and finite norm at the same label. They do not yet identify the contraction of the original sigma source with its R770 critical coefficient, and do not assert integrality after division by $p$.

## 1. The positive product polarization and the marked two flags

Retain R878/R881's original data
$$
E:y^2=x^3-1,\qquad \omega=\frac{dx}{2y},\qquad
R=W(\mathbf F_{p^2}),\qquad p\ge41,\quad p\equiv5\pmod6.
\tag{886.1}
$$
Write $n=p+1$, $\mathbb E=\mathbf F_{p^2}$, and
$$
\mathscr X=E_R\times_R E_R,\qquad
\mathscr L=O(6pO)\boxtimes O(6pO),\qquad
\mathcal B=H^0(\mathscr X,\mathscr L).
\tag{886.2}
$$
The polarization is the positive product polarization on the two factors, not its difference.

Pass to a finite extension $K'/\operatorname{Frac}(R)$ containing the chosen original $p$-torsion marking, character values, and $\mu_p$, and let $R'$ be its valuation ring. On the generic geometric $p$-torsion use exactly R881's marked coordinates:
$$
b(a,a')=\operatorname{Tr}_{\mathbb E/\mathbf F_p}
 (\gamma a\overline{a'}),\qquad
\overline\gamma=-\gamma,\quad \gamma\ne0,
$$
$$
u=a+\overline b,\qquad
v=-\frac{\gamma}{2}(a-\overline b).
\tag{886.3}
$$
The alternating form on the product is $b(a,a')+b(b,b')$. Direct expansion gives
$$
b(a,a')+b(b,b')
=\operatorname{Tr}(u\overline{v'}-v\overline{u'}).
\tag{886.4}
$$
In particular conjugation in the second original factor is anti-symplectic. This is the reason the two graphs below are isotropic for the positive product form.

Define generic subgroups of order $p^2$ by
$$
L_K=\{u=0\}=\{a=-\overline b\},\qquad
L'_K=\{v=0\}=\{a=\overline b\}.
\tag{886.5}
$$
They are complementary maximal isotropic subgroups of the $p$-primary kernel of $\mathscr L$. Inverting (886.3) gives
$$
a=\frac u2-\frac v\gamma,\qquad
b=\frac{\overline u}{2}-\frac{\overline v}{\gamma}.
\tag{886.6}
$$
Thus a point written $(u,0)$ below means the original marked pair
$(u/2,\overline u/2)$; a point $(0,v)$ means
$(-v/\gamma,-\overline v/\gamma)$. These are fixed coordinates, and the factor $\gamma$ is retained.

Let $L,L'$ be the scheme-theoretic closures of (886.5) in $\mathscr X[p]_{R'}$. They are finite flat subgroup schemes of rank $p^2$. Indeed their coordinate rings are the saturated quotients defining the generic subgroups inside a finite flat scheme over a DVR, so they are torsion-free and finite over $R'$. The group laws extend by the same saturation argument.

Their isotropy extends from the generic fiber: the two pairing morphisms agree on a schematically dense generic fiber of the finite flat product. The annihilator of either closure has the same rank; uniqueness of the finite flat closure then gives maximal isotropy.

No assertion is made that $L$ and $L'$ remain complementary on the special fiber. Nor is the conjugation in (886.3) asserted to extend to an automorphism of the original elliptic scheme.

## 2. Actual quotient and the tame multiplicity space

Use the original odd-$p$ symmetric theta section $\tau$ of R878/R881 for the $p$-primary theta group of $\mathscr L$. Its multiplication law is
$$
\tau(x)\tau(y)=e(x,y)^{1/2}\tau(x+y),
\tag{886.7}
$$
where the square root on $\mu_p$ is the unique group automorphism inverse to squaring. Thus $\tau|_L$ and $\tau|_{L'}$ are actual homomorphisms of finite flat group schemes, not choices of unrelated lifts of generic points.

The free translation action gives an fppf quotient
$$
\pi:\mathscr X_{R'}\longrightarrow\mathscr B_L=\mathscr X_{R'}/L.
\tag{886.8}
$$
Here the quotient theorem applies because the source is projective and each finite orbit is contained in an affine open. The quotient is flat over $R'$ by faithfully flat descent, is proper, and has geometric fibers equal to quotients of abelian varieties by finite subgroup schemes. Those fibers are abelian varieties, so the quotient is smooth and is an abelian scheme.

The homomorphism $\tau|_L$ is an $L$-linearization of $\mathscr L$. Faithfully flat descent therefore gives a specific line bundle $\mathscr M_L$, together with
$$
\pi^*\mathscr M_L\simeq\mathscr L.
\tag{886.9}
$$
This is descent of the actual line bundle with its original theta lifts. It is not the assertion that generic isotropy by itself supplies an unspecified integral descent.

The descended polarization has type $(6,6)$. The $p$-primary part has been removed by a maximal isotropic subgroup, while the original six-primary kernel and theta marking are transported unchanged by the prime-to-six isogeny $\pi$. Equivalently its kernel is the same marked six-primary group of exponent six and rank $6^4$.

Set
$$
\mathcal U_L=H^0(\mathscr B_L,\mathscr M_L).
$$
It is free of rank $36$, and pullback identifies
$$
\boxed{
\pi^*\mathcal U_L=\mathcal B_{R'}^{\,\tau(L)}.
}
\tag{886.10}
$$
One can compute the rank directly:
$\chi(\mathscr L)=(6p)^2$, $\deg\pi=p^2$, and hence
$\chi(\mathscr M_L)=36$. Ampleness, base change, and vanishing of higher cohomology give the asserted free module. This is the actual descended tame multiplicity space.

The descent theorem used here is the relative coherent-sheaf descent in Moonen et al., Proposition 7.2. The theta interpretation is their Theorem 8.10; its proof by the same fppf descent applies over $R'$. The quotient is covered by their Theorem 4.16 and Example 4.29, with the abelian-fiber assertion in Example 4.40.

## 3. A fixed generic Schrödinger identification

The chosen complementary generic flags, the original $\tau$, and the additive character $\psi$ determine a generic Heisenberg identification
$$
\mathcal B_{K'}\simeq
\mathcal U_{L,K'}\otimes_{K'}\operatorname{Fun}(\mathbb E,K')
\tag{886.11}
$$
with the following normalization:
$$
\pi^*s\longleftrightarrow s\otimes1
\qquad(s\in\mathcal U_{L,K'}).
\tag{886.12}
$$
Existence follows from the finite theta representation theorem; the $L$-invariant line in the function factor consists exactly of the constant functions. Its identification with (886.10) fixes the multiplicity-space scalar. Thus (886.11) is not left with an arbitrary change of tame basis.

The Heisenberg action is exactly the one in R881:
$$
\rho(\tau(u,v))\varphi(\xi)=
\psi\!\left(-\operatorname{Tr}(u\overline\xi)
-\tfrac12\operatorname{Tr}(u\overline v)\right)
\varphi(\xi+v).
\tag{886.13}
$$
The variable $\xi$ has the $v$-coordinate normalization of (886.3).

The opposite-character norm-one action of R881 acts by
$\varphi(\xi)\mapsto\varphi(q^{-1}\xi)$. Its two single-factor phases have already been proved to cancel. It consequently acts as the identity on (886.12), hence on the actual integral module $\mathcal U_L$, because the latter is torsion-free. Denote that actual integral action on $\mathcal B$ by $\mathcal M_q$.

All uses of the function model in this section are on the generic fiber. No claim that (886.11) identifies the integral theta lattice with the whole function-value lattice is made.

## 4. Exact Gauss constant, with the original character

For an original primitive label let
$$
7\le h\le p-4,\qquad h\equiv1\pmod6,\qquad (h,n)=1,
$$
$$
\theta_h(y)=[y]^{-h(p-1)},\qquad
\mu_h=\theta_h|_T=\widetilde\chi^{\,2h}.
\tag{886.14}
$$
In particular $\theta_h|_{\mathbf F_p^\times}=1$, and $\theta_h$ is nontrivial.

For either $\eta=\theta_h$ or $\theta_h^{-1}$, put
$$
G(\eta)=\sum_{u\in\mathbb E^\times}
 \eta(u)\psi(\operatorname{Tr}u).
$$
Choose $\delta\ne0$ of trace zero. Then
$\delta^{p-1}=-1$, so, because $h$ is odd,
$$
\eta(\delta)=-1.
\tag{886.15}
$$
The trace-zero nonzero fiber has character sum $-(p-1)$. Every nonzero trace fiber has the same character sum, since multiplication by an element of $\mathbf F_p^\times$ preserves $\eta$. The total character sum is zero; hence the common sum on a nonzero trace fiber is $1$. Finally
$\sum_{t\in\mathbf F_p^\times}\psi(t)=-1$, giving
$$
\boxed{G(\theta_h)=G(\theta_h^{-1})=-p.}
\tag{886.16}
$$
This proof retains the original character direction. It works for the specific original additive character, and in fact for every nontrivial additive character of $\mathbf F_p$.

For later use define the actual integral theta operators
$$
\mathcal G_\eta=
\sum_{u\in\mathbb E^\times}\eta(u)\rho(\tau(u,0)).
\tag{886.17}
$$
Every torsion point and character value in this sum is defined over $R'$, and every theta operator is integral. Thus (886.17) acts on $\mathcal B_{R'}$.

In the generic function model, substitution in the Gauss sum gives
$$
\mathcal G_{\theta_h^{-1}}\varphi(\xi)
=\begin{cases}
-p\,\theta_h(\xi)^{-1}\varphi(\xi),&\xi\ne0,\\
0,&\xi=0,
\end{cases}
$$
$$
\mathcal G_{\theta_h}\varphi(\xi)
=\begin{cases}
-p\,\theta_h(\xi)\varphi(\xi),&\xi\ne0,\\
0,&\xi=0.
\end{cases}
\tag{886.18}
$$
For example the first sum is
$G(\theta_h^{-1})\theta_h(-\overline\xi)$.
Since $\theta_h(-1)=1$ and
$\theta_h(\overline\xi)=\theta_h(\xi)^{-1}$, it is exactly the first formula in (886.18).

There is no silent removal of $\gamma$. If one replaced the configuration coordinate $\xi$ by the first original coordinate $a=-\xi/\gamma$ on $L$, then
$\theta_h(-\gamma)=-1$ would contribute the extra sign
$\theta_h(\xi)^{-1}=-\theta_h(a)^{-1}$.
We do not make that replacement. All formulas use (886.3), (886.6), and (886.13).

## 5. An integral source for the original split vector

For $s\in\mathcal U_L$, define
$$
\Gamma_h(s)=\mathcal G_{\theta_h^{-1}}\,\pi^*s.
\tag{886.19}
$$
This is an integral global section of $\mathscr L$. Equations (886.12) and (886.18) give the exact generic identity
$$
\boxed{
\Gamma_h(s)=-p\,s\otimes\Phi_{0,h},\qquad
\Phi_{0,h}(0)=0,\quad
\Phi_{0,h}(\xi)=\theta_h(\xi)^{-1}\quad(\xi\ne0).
}
\tag{886.20}
$$
The function $\Phi_{0,h}$ is precisely the image of the original $e_0$ in R881, not a newly chosen finite vector. In particular $\Gamma_h$ is injective, since it is injective on the generic fiber and its source is torsion-free.

The torus label is exact integrally. Using $\mathcal M_q\pi^*s=\pi^*s$ and
$\mathcal M_q\tau(u,0)\mathcal M_q^{-1}=\tau(qu,0)$ gives
$$
\mathcal M_q\Gamma_h(s)=\theta_h(q)\Gamma_h(s)
=\widetilde\chi(q)^{2h}\Gamma_h(s).
$$
Consequently
$$
\boxed{\Gamma_h(\mathcal U_L)\subseteq
 \mathcal P_{2h}\mathcal B_{R'}.}
\tag{886.21}
$$
The actual source in (886.19) and the original label in (886.14) are used throughout.

Formula (886.20) does not show that $\Gamma_h(s)/p$ is integral in $\mathcal B_{R'}$. The integrality asserted here is that of $\Gamma_h(s)$ itself.

## 6. The reverse integral contraction and the split coefficient

Define the unnormalized theta trace along the first flag:
$$
\mathcal T_L=
\sum_{v\in\mathbb E}\rho(\tau(0,v)).
\tag{886.22}
$$
It is integral. Its image is $\tau(L)$-invariant: this holds by reindexing on the generic fiber, and extends to the finite flat group scheme because the underlying modules are torsion-free. Thus it lands in the actual descended module (886.10). No division by the order $p^2$ is used.

The reverse contraction is the integral map
$$
\boxed{
\mathcal C_h=(\pi^*)^{-1}\mathcal T_L\mathcal G_{\theta_h}:
\mathcal B_{R'}\longrightarrow\mathcal U_L.
}
\tag{886.23}
$$
If $S$ has generic function-vector expression $\Psi_S(\xi)\in\mathcal U_{L,K'}$, equations (886.18) and (886.22) give
$$
\mathcal C_h(S)=-p\sum_{\xi\in\mathbb E^\times}
 \theta_h(\xi)\Psi_S(\xi).
\tag{886.24}
$$
In particular set
$$
\ell_h(S)=\frac1{p^2-1}
 \sum_{\xi\in\mathbb E^\times}
 \theta_h(\xi)\Psi_S(\xi).
\tag{886.25}
$$
Then
$$
\boxed{
\mathcal C_h=-p(p^2-1)\ell_h.
}
\tag{886.26}
$$
The denominator $p^2-1$ is a unit. The remaining displayed division by $p$ is genuine and has not been removed by (886.23).

On the function factor, (886.25) is exactly the original normalized split coefficient. Indeed the original Hermitian form is
$$
G(\varphi,\varphi')=\frac1n
 \sum_{\xi\in\mathbb E}\varphi(\xi)\overline{\varphi'(\xi)},
$$
and $\overline{\Phi_{0,h}(\xi)}=\theta_h(\xi)$, while
$G(\Phi_{0,h},\Phi_{0,h})=p-1$. Therefore
$$
\ell_h(\varphi)=
\frac{G(\varphi,\Phi_{0,h})}{p-1}.
\tag{886.27}
$$
For a vector with a tame multiplicity factor, the same formula is taken coefficientwise in that factor.

This contraction selects the same torus character. Since
$\mathcal M_q\mathcal G_{\theta_h}\mathcal M_q^{-1}
=\theta_h(q)^{-1}\mathcal G_{\theta_h}$ and
$\mathcal M_q$ is the identity on the output of $\mathcal T_L$, one has
$$
\mathcal C_h\mathcal M_q
=\widetilde\chi(q)^{2h}\mathcal C_h,
\qquad
\boxed{\mathcal C_h=\mathcal C_h\mathcal P_{2h}.}
\tag{886.28}
$$
Thus (886.23) is an actual integral contraction of the specified character component, not a rank count.

Combining the forward and reverse maps gives a completely specified scalar:
$$
\boxed{\mathcal C_h\Gamma_h
=p^2(p^2-1)\,1_{\mathcal U_L}.}
\tag{886.29}
$$

## 7. The original CM average and its exact norm

On the generic $W_{\mu_h}$ factor, use the full determinant extension and the actual torus of R727/R881:
$$
\mathsf T_\zeta=
\left\{\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}\right\}
/\mathbf F_p^\times,\qquad
\mathcal A_h=\frac1n\sum_{t\in\mathsf T_\zeta}\rho_h(t).
\tag{886.30}
$$
This is the original finite CM average in the resulting cuspidal representation. It is different from the character torus acting on $\mathscr X[p]$.

Extend $\mathcal A_h$ by the identity on $\mathcal U_{L,K'}$. Its action is being used only on the generic fiber; no integral action on the entire theta lattice is asserted. The original norm is
$$
N_h=G(\Phi_{0,h},\operatorname{Tr}_{\mathsf T_\zeta}\Phi_{0,h}).
$$
Since the torus average is self-adjoint and $N_h$ is real, (886.27) gives
$$
\ell_h(\mathcal A_h\Phi_{0,h})=\frac{N_h}{p^2-1}.
\tag{886.31}
$$
Equations (886.20), (886.26), and (886.31) therefore prove
$$
\boxed{
\mathcal C_h\mathcal A_h\Gamma_h
=p^2N_h\,1_{\mathcal U_L}.
}
\tag{886.32}
$$
In particular the original Legendre factor is retained:
$$
p^{-2}\mathcal C_h\mathcal A_h\Gamma_h\bmod p
=-P_{h-1}(1/\sqrt{-3})^2\,1_{\mathcal U_L},
\tag{886.33}
$$
where the reduction means the integral scalar identity (886.32), using R727's exact integrality of $N_h$. It is not a claim that the individual divided maps are integral.

Whenever both labels belong to the original permitted class, the construction continues to distinguish $h$ from $h+n/2$. The characters restricted to the first torus agree, but $\theta_{h+n/2}=\theta_h\,\varepsilon\circ\operatorname N$, so both (886.17) and (886.25) change by the actual norm-quadratic factor. The full determinant extension in (886.30) changes accordingly, exactly as in R881.

## 8. The original source that is still to be compared

The section
$$
S_{F,G}=(x s_{6p})\otimes(-xy s_{6p})\in\mathcal B_{R'}
\tag{886.34}
$$
is the actual enlarged image of the original sigma-six pair. Formula (886.23) gives a concrete integral vector
$\mathcal C_h(S_{F,G})$ in the descended type-$(6,6)$ source, and (886.28) proves that it depends only on the genuine $\mathcal P_{2h}$ component of that section.

What is not proved is an equality between
$\mathcal C_h(S_{F,G})/p$, or its required fifth-lift variant, and the R770 functional $f_i g_j$ at $h=6i+7$, $i+j=N-1$. Those original functionals divide by $\sigma^{6p-6}$ on each factor and take specified ordinary Taylor coefficients. R884 supplies exact nonintegrality examples on the enlarged theta lattice; it cannot be bypassed by (886.23).

Thus (886.19)--(886.33) give an actual two-flag source, a fixed tame multiplicity module, an integral reverse contraction, and the exact original finite norm. They do not prove that the contraction of (886.34) is a unit, that its divided value is integral, that its original critical Taylor comparison has no correction, or that the modular quotient has a unit normal coefficient.

## Sources

- [R881](R881-original-integral-theta-lift-and-cuspidal-test-vector.md): original positive product symplectic coordinates, phase cancellation, $\Phi_{r,h}$, exact Gram form, and full determinant extension.
- [R878](R878-original-finite-theta-action-and-section-projections.md): original odd symmetric theta section and finite flat theta action.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md): the actual $e_0$, $\theta_h$, CM torus, $N_h$, and its Legendre-square reduction.
- [R884](R884-original-enlarged-theta-lattice-coefficient-pole.md): exact denominator obstruction for the original sigma functionals.
- [Moonen et al., Chapter IV](https://www.math.ru.nl/~bmoonen/BookAV/Quotients.pdf), Theorem 4.16, Example 4.29 and Example 4.40: finite flat quotients and the abelian fibers.
- [Moonen et al., Chapter VII](https://www.math.ru.nl/personal/bmoonen/BookAV/DualAV2.pdf), Proposition 7.2: relative faithfully flat descent of locally free sheaves.
- [Moonen et al., Chapter VIII](https://www.math.ru.nl/personal/bmoonen/BookAV/ThetaGr.pdf), Theorem 8.10 and Proposition 8.15: theta linearization, descent, and the remaining theta group.
- [S. W. Shin, Abelian varieties and Weil representations](https://math.berkeley.edu/~swshin/AV-Weil.pdf), Propositions 2.12--2.13: relative finite theta representations and base change.

All scalar identities are proved above. No new mathematical computation or prime scan was executed.
