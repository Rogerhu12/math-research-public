# R881 — Integral theta lift, opposite-character tensor, and the original finite test vector

Date: 2026-11-16. Status: proved integral finite-torus lift and generic-fiber comparison with the original finite cuspidal representation. The remaining comparison with the original sigma coefficient functionals and with the actual modular-quotient source is stated in §8.

## 1. Original integral model and the lift to its theta group

Retain R878's original curve, differential, tame six-level marking, and residue field:

$$
E:y^2=x^3-1,\qquad \omega=\frac{dx}{2y},\qquad
k_0=\mathbf F_{p^2},\qquad p\ge41,\quad p\equiv5\pmod6.
\tag{881.1}
$$

Set $R=W(k_0)$, $K=\operatorname{Frac}(R)$, and use the same equation for the smooth elliptic scheme over $R$. The six-level marking lifts uniquely after its chosen residue embedding, since $6$ is invertible in $R$. The CM action of $\mathcal O=\mathbf Z[\zeta]$ is defined over $R$.

Put

$$
\mathcal H=H^0(E,O(6pO)),\qquad \operatorname{rank}_R\mathcal H=6p,
\qquad T=\ker\!\left(\mathbf F_{p^2}^{\times}
 \xrightarrow{\operatorname N}\mathbf F_p^\times\right).
\tag{881.2}
$$

Write $n=p+1$ and let $\widetilde\chi:T\to R^\times$ be the Teichmueller lift of the tangent character $\chi(q)=q$ of R878. The notation $\widetilde\chi(q)$ is a character value, not an assertion that the corresponding Teichmueller unit is a global automorphism of $E$.

The action of $\mathcal O$ on the finite flat group scheme $E[p]$ factors through $\mathcal O/p\mathcal O$. Consequently each $q\in T$ acts on $E[p]$ over $R$, and preserves its Weil pairing: the Rosati norm of an integral representative is $1$ modulo $p$. This only uses that the target pairing is $\mu_p$.

Let $\mathcal G=\mathcal G(O(6pO))$. Its $p$-primary and six-primary inverse images form the same commuting central product as in R878. The odd-$p$ symmetric section

$$
\tau(u)=g\iota(g)^{-1},\qquad g\text{ above }u/2,
\tag{881.3}
$$

is valid over $R$ as an fppf construction. The center-independent descent and multiplication formula of R878 use only that $2$ is invertible and that $E[p]$ is killed by $p$. Thus

$$
A_q(\lambda\tau(u))=\lambda\tau(qu)
\tag{881.4}
$$

defines an actual automorphism of the $p$-primary theta group over $R$. Extend it by the identity on the original six-primary theta group. In particular the same six-level marking is fixed pointwise.

The relative finite theta theorem identifies weight-one representations with modules over the base, using $\mathcal H$ as a generator. Hence the intertwiners

$$
\mathcal I_q=
\{M:M\rho(g)=\rho(A_qg)M\}
\tag{881.5}
$$

form an invertible $R$-module, commute with residue-field extension, and contain isomorphisms. Since $R$ is local, this line is free. This is the relative form of Shin, Propositions 2.12–2.13, not an inference from characteristic-zero uniqueness alone.

## 2. A unique integral linearization with the R878 reduction

Let $\overline M_q$ be the actual normalized residue-field action in R878, which is the identity on the six-dimensional $\ker D$. Choose a generator $q_0$ of $T$ and an intertwiner $L\in\mathcal I_{q_0}$ whose reduction is $\overline M_{q_0}$. Such a choice is possible by the base-change assertion in §1.

The $n$-th power of $L$ commutes with the entire theta group. Relative Schur's lemma gives

$$
L^n=c\,1,\qquad c\in R^\times,\qquad c\equiv1\pmod p.
\tag{881.6}
$$

As $p\nmid n$, Hensel's lemma gives a unique $u\in1+pR$ with $u^n=c^{-1}$. Define $M_{q_0}=uL$ and $M_{q_0^j}=M_{q_0}^j$. Then

$$
M_q\rho(g)M_q^{-1}=\rho(A_qg),\qquad
M_qM_{q'}=M_{qq'},\qquad M_q\bmod p=\overline M_q.
\tag{881.7}
$$

This representation is independent of the initial generator and lift. Indeed two such linearizations differ, by relative Schur's lemma, by a character $T\to R^\times$ that is trivial modulo $p$. A prime-to-$p$ root of unity congruent to $1$ is $1$, so the character is trivial.

The projectors

$$
\mathsf e_a=\frac1n\sum_{q\in T}
 \widetilde\chi(q)^{-a}M_q
\tag{881.8}
$$

are integral idempotents. Their images are free direct summands, and R878 determines their ranks:

$$
\operatorname{rank}_R\mathsf e_a\mathcal H=
\begin{cases}
0,&a\equiv1\pmod n,\\
6,&a\not\equiv1\pmod n.
\end{cases}
\tag{881.9}
$$

Thus the finite-torus action is defined on the actual original integral line-bundle sections. It is not obtained by assigning arbitrary lifts to a residue-field matrix.

No full $\mathrm{SL}_2(\mathbf F_p)$ action on this integral lattice has been inferred. The proof constructs exactly the displayed CM torus and the fixed tame theta action.

## 3. The actual opposite-character tensor and its ranks

On

$$
\mathcal B=\mathcal H\otimes_R\mathcal H
=H^0(E\times_R E,O(6pO)\boxtimes O(6pO))
\tag{881.10}
$$

use the action

$$
\mathcal M_q=M_q\otimes M_{q^{-1}}.
\tag{881.11}
$$

It comes from the actual finite flat automorphism $(u,v)\mapsto(qu,q^{-1}v)$ of $E[p]^2$, and fixes both original six-primary theta groups. Put

$$
\mathcal P_d=\frac1n\sum_{q\in T}
 \widetilde\chi(q)^{-d}\mathcal M_q.
\tag{881.12}
$$

Equation (881.9) gives, over $R$ and not only after tensoring with $K$,

$$
\boxed{
\operatorname{rank}_R\mathcal P_d\mathcal B=
\begin{cases}
36p,&d\equiv0\pmod n,\\
36(p-1),&d\not\equiv0\pmod n.
\end{cases}}
\tag{881.13}
$$

For $d\ne0$, there are $n-2=p-1$ pairs $(a,b)$ with $a-b=d$ and $a,b\ne1$; for $d=0$ there are $n-1=p$ such pairs. Each pair contributes rank $36$.

These are actual integral projector images. They do not imply that the projection of any specified section is nonzero.

## 4. The single-factor phase and its exact cancellation

Fix a tame theta structure compatible with the original six-level marking. The commuting six-primary factor has a free irreducible module $\mathcal U$ of rank six. Finite theta equivalence gives

$$
\mathcal H\simeq\mathcal U\otimes_R\mathcal V,\qquad
\operatorname{rank}_R\mathcal V=p.
\tag{881.14}
$$

The $M_q$ act as $1_{\mathcal U}\otimes N_q$. This factorization may be made after a finite unramified extension if needed for the chosen tame theta basis; it introduces no factor of $p$. Both tensor factors in (881.10) use the same choice.

Now pass to a characteristic-zero extension $K'$ containing the original $p$-torsion marking, $\mu_p$, and all character values. The finite theta representation $\mathcal V_{K'}$ is the ordinary $p$-dimensional Heisenberg representation. Its compatible canonical Weil representation $\rho_{\rm W}$ of the symplectic group of $E[p](K')$ is unique for $p\ge5$. The canonical tensor compatibility will be used below.

On the nonsplit CM torus $T$, the canonical Weil representation contains every character once except the unique quadratic character

$$
\varepsilon_T=\widetilde\chi^{\,n/2}.
\tag{881.15}
$$

This is the finite Weil multiplicity formula of Gurevich–Hadani, Theorem 8; their Theorem 7 gives its character formula. On the other hand (881.9), divided by the tame rank six, says that $N_q$ omits exactly $\widetilde\chi$.

The two $T$ actions implement the same theta-group automorphism, so they differ by a character. The omitted character fixes this character exactly:

$$
\boxed{
N_q=\widetilde\chi(q)^{\,1-n/2}\rho_{\rm W}(q).
}
\tag{881.16}
$$

This equation is understood after one fixed Heisenberg intertwiner; changing its scalar changes neither side as an operator. In particular

$$
N_q\otimes N_{q^{-1}}
=\rho_{\rm W}(q)\otimes\rho_{\rm W}(q^{-1}).
\tag{881.17}
$$

The two single-factor phases cancel. The opposite-character tensor in (881.11) is therefore the canonical finite Weil action of the displayed torus, without a residual character twist.

The tensor compatibility here also follows from uniqueness: the restriction of the four-dimensional symplectic Weil action and the tensor of the two two-dimensional actions intertwine the same Heisenberg action. Their ratio is a character of $\mathrm{SL}_2(\mathbf F_p)\times\mathrm{SL}_2(\mathbf F_p)$, which is trivial for $p\ge5$. Thus no additional tensor phase is implicit in (881.17).

For completeness, the multiplicity formula is consistent with the original tangent orientation. For $q\ne1$ the Weil trace is
$\left(\frac{-\det(q-1)}p\right)=-\varepsilon_T(q)$, while the trace of $N_q$ is $-\widetilde\chi(q)$. Here
$\det(q-1)=\operatorname N(q-1)$ and
$(q-1)^{p-1}=-q^{-1}$; these identities give the displayed sign directly.

## 5. A precise symplectic identification with the anisotropic norm model

This section is on the generic fiber. It does not extend a conjugate-Frobenius operator to the integral elliptic scheme.

Use the actual CM $p$-marking to identify the two-dimensional $\mathbf F_p$-space of geometric $p$-torsion with

$$
\mathbb E=\mathbf F_{p^2}.
$$

Fix the additive character $\psi$ determined by the chosen $p$-th root of unity. The commutator pairing of the $p$-primary theta group can then be written uniquely

$$
b(a,b')=\operatorname{Tr}_{\mathbb E/\mathbf F_p}
 (\gamma a\overline{b'}),\qquad
\overline\gamma=-\gamma,\quad \gamma\ne0.
\tag{881.18}
$$

The constant $\gamma$ retains the actual pairing scale, including the sixth power of the original Weil pairing. It is not replaced by an unchosen square root.

On $\mathbb E\oplus\mathbb E$ with the direct-sum alternating form, define

$$
u=a+\overline b,\qquad
v=-\frac{\gamma}{2}(a-\overline b).
\tag{881.19}
$$

This is an invertible $\mathbf F_p$-linear map. A direct expansion gives

$$
b(a,a')+b(b,b')
=\operatorname{Tr}(u\overline{v'}-v\overline{u'}).
\tag{881.20}
$$

Moreover $(a,b)\mapsto(qa,q^{-1}b)$ becomes

$$
(u,v)\longmapsto(qu,qv).
\tag{881.21}
$$

Thus the torus is exactly the special orthogonal group of the anisotropic quadratic space $(\mathbb E,\operatorname N)$ in its usual finite dual pair. The commuting $\mathrm{SL}_2(\mathbf F_p)$ acts on the two positions $u,v$. Its generic Weil representation is realized on functions $\varphi:\mathbb E\to K'$. In this model the torus acts by $\varphi(\xi)\mapsto\varphi(q^{-1}\xi)$.

For a nontrivial character $\mu:T\to K'^\times$ the corresponding space is

$$
W_\mu=\{\varphi:\mathbb E\to K':
 \varphi(q\xi)=\mu(q)^{-1}\varphi(\xi)\}.
\tag{881.22}
$$

Its dimension is $p-1$. In the common conventions of Liu–Zhang §2.3, equation (2.2), and R727, the generators act by

$$
\rho_\mu\!\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix}
 \varphi(\xi)=\varphi(a\xi),
$$
$$
\rho_\mu\!\begin{pmatrix}1&b\\0&1\end{pmatrix}
 \varphi(\xi)=\psi(b\operatorname N\xi)\varphi(\xi),
$$
$$
\rho_\mu(w)\varphi(\xi)
=-\frac1p\sum_{\eta\in\mathbb E}
 \psi(\operatorname{Tr}(\overline\eta\,\xi))\varphi(\eta),
\qquad w=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\tag{881.23}
$$

These conventions can be checked directly against (881.20). With the configuration variable corresponding to $v$, the Heisenberg operator is
$$
\pi(u,v)\varphi(\xi)=
 \psi\!\left(-\operatorname{Tr}(u\overline\xi)
       -\tfrac12\operatorname{Tr}(u\overline v)\right)
 \varphi(\xi+v).
$$
Its commutator is (881.20). Conjugation by the three operators in (881.23) gives the displayed upper-unipotent, diagonal, and Weyl actions on $(u,v)$; the torus gives $(u,v)\mapsto(qu,qv)$. This fixes simultaneously the inverse in (881.22), the sign in the Fourier exponent, and the orientation of the label in (881.25).

In particular the Fourier constant is the original negative $1/p$. When $\mu^2\ne1$, $W_\mu$ is the irreducible cuspidal representation of $\mathrm{SL}_2(\mathbf F_p)$.

Combining (881.14), (881.17), and (881.19), the generic fiber of $\mathcal P_d\mathcal B$ is the tame multiplicity space $\mathcal U_{K'}^{\otimes2}$ tensored with $W_{\widetilde\chi^d}$, for $d\ne0$. The comparison is a Heisenberg/Weil comparison on the generic fiber. Its matrix has not been proved integral in the original theta-section and function-value bases.

## 6. Exact recovery of the original label and split vector

Take a label satisfying the original R727/R770 conditions

$$
7\le h\le p-4,\qquad h\equiv1\pmod6,\qquad (h,n)=1,
$$
$$
\theta_h(y)=[y]^{-h(p-1)}.
\tag{881.24}
$$

Here $[y]$ denotes the same Teichmueller orientation as R727. Its restriction to $T$ is precisely

$$
\mu_h(q)=\theta_h(q)=\widetilde\chi(q)^{2h}.
\tag{881.25}
$$

This follows from $-(p-1)\equiv2\pmod n$, not from an arbitrary relabeling. The order of $\mu_h$ is $n/2>2$, so (881.22) is cuspidal. Thus $\mathcal P_{2h}$ is an actual integral projector whose generic fiber contains the restriction of the original cuspidal representation.

There is an explicit isomorphism with the original Mercuri–Schoof model, including its split vector. For $r\in\mathbf F_p$, set

$$
\Phi_{r,h}(0)=0,\qquad
\Phi_{r,h}(\xi)=\theta_h(\xi)^{-1}
 \psi(r\operatorname N\xi)\quad(\xi\ne0).
\tag{881.26}
$$

These functions belong to $W_{\mu_h}$. Their only relation over $K'$ is
$\sum_r\Phi_{r,h}=0$: after choosing one point of each nonzero norm, this is the usual additive Fourier basis restricted from $\mathbf F_p$ to $\mathbf F_p^\times$.

The map

$$
\boxed{e_r\longmapsto\Phi_{r,h}}
\tag{881.27}
$$

intertwines the original unipotent action $e_r\mapsto e_{r+b}$ and the determinant-one diagonal action $e_r\mapsto e_{a^2r}$. It also intertwines the full original Weyl action, not merely its trace. Indeed substitute $\eta=\xi z$ into the last formula of (881.23):

$$
\rho_{\mu_h}(w)\Phi_{r,h}(\xi)
=-\frac{\theta_h(\xi)^{-1}}p
 \sum_{z\in\mathbb E^\times}\theta_h(z)^{-1}
 \psi\!\left(\operatorname N\xi\,
  (r\operatorname N z+\operatorname{Tr}z)\right).
$$

Frobenius $z\mapsto z^p$ preserves each norm/trace fiber and changes
$\theta_h(z)^{-1}$ to $\theta_h(z)$. Therefore

$$
\boxed{
\rho_{\mu_h}(w)\Phi_{r,h}
=-\frac1p\sum_{z\in\mathbb E^\times}
 \theta_h(z)\Phi_{r\operatorname N z+\operatorname{Tr}z,h}.
}
\tag{881.28}
$$

This is exactly R727.14. In particular the actual split vector is

$$
e_0\longleftrightarrow\Phi_{0,h}(\xi)=\theta_h(\xi)^{-1}
\quad(\xi\ne0).
\tag{881.29}
$$

Its normalization has not been replaced by a radial delta function.

The original Hermitian form also matches exactly. Use complex conjugation on the finite character values, or its algebraic involution, and put

$$
\langle\varphi,\varphi'\rangle
=\frac1n\sum_{\xi\in\mathbb E}
 \varphi(\xi)\overline{\varphi'(\xi)}.
$$

Each nonzero norm has $n$ points, so

$$
\boxed{
\langle\Phi_{r,h},\Phi_{s,h}\rangle
=\sum_{a\in\mathbf F_p^\times}\psi((r-s)a)
=p\delta_{rs}-1.
}
\tag{881.30}
$$

This is the original $G$, with no scalar adjustment.

## 7. The full determinant extension and the separate CM torus

The preceding identification need not discard the determinant-nonsquare part of the original group. Given $a\in\mathbf F_p^\times$, choose any $b_a\in\mathbb E^\times$ with $\operatorname N b_a=a$, and define

$$
\mathcal D_a\varphi(\xi)=\theta_h(b_a)\varphi(b_a\xi).
\tag{881.31}
$$

Changing $b_a$ by $q\in T$ changes the scalar and the function by inverse factors, by (881.22) and (881.25). Hence the definition is independent of the choice. It gives

$$
\mathcal D_a\Phi_{r,h}=\Phi_{ar,h}.
\tag{881.32}
$$

Together with (881.28), these operators are exactly the original full affine Borel and Weyl operators, and therefore recover its $\mathrm{PGL}_2(\mathbf F_p)$ representation. This fixes the original determinant extension in the generic norm model.

In particular labels differing by $n/2$ have the same restricted character $\mu_h$, but must not be merged. If $\varepsilon$ is the quadratic character of $\mathbf F_p^\times$, then

$$
\theta_{h+n/2}(\xi)
=\theta_h(\xi)\varepsilon(\operatorname N\xi),
$$
$$
\Phi_{0,h+n/2}(\xi)
=\varepsilon(\operatorname N\xi)\Phi_{0,h}(\xi).
\tag{881.33}
$$

The associated full representations differ by the determinant-quadratic twist. Formula (881.31) exhibits that difference as the scalar $\varepsilon(a)$.

There are two different tori in this construction. The torus in (881.11) is the commuting theta-character torus that selects $W_{\mu_h}$. The original CM averaging torus of R727 is inside the resulting full cuspidal group:

$$
\mathsf T_\zeta=
\left\{\begin{pmatrix}a&-b\\b&a+b\end{pmatrix}:
 (a,b)\ne(0,0)\right\}/\mathbf F_p^\times.
\tag{881.34}
$$

It acts on $W_{\mu_h}$ through (881.23), (881.31), and Bruhat decomposition. Its actual averaged vector is still

$$
u_h=\frac1n\sum_{t\in\mathsf T_\zeta}t\,\Phi_{0,h}.
\tag{881.35}
$$

Equations (881.27)–(881.32) preserve the exact R727 finite norm, and hence its proved reduction

$$
G(e_0,\operatorname{Tr}_{\mathsf T_\zeta}e_0)
\equiv-P_{h-1}(1/\sqrt{-3})^2\pmod p.
\tag{881.36}
$$

No change to trace-zero coordinates has been made while leaving the split vector fixed. The first torus does not replace the second one.

## 8. What has and has not crossed the integral boundary

The new assertions are an actual integral torus action on the original theta line bundle, its canonical opposite-character tensor, and a generic finite-Weil realization in which the original label, split vector, Hermitian form, determinant extension, and CM average are explicit.

The generic-fiber comparison in §5 is not yet an integral identification of the theta lattice with the original cuspidal lattice or its all-cusp enlargement. For example the functions in (881.26) are all congruent modulo $\zeta_p-1$ in the function-value lattice. Their spanning assertion was over $K'$, with $p$ invertible. Their Gram matrix (881.30) is the old nonsaturated one. The actual higher-phase lattice analysis of R863 and the all-cusp lattice of R869 remain relevant; this paper does not replace them by the entire function-value lattice.

Nor has a tame multiplicity vector in $\mathcal U^{\otimes2}$ or a source theta section been identified with the original arithmetic evaluation of (881.35). In particular the integral projectors (881.12) do not show that the projection of
$j(x\sigma^6)\otimes j(-xy\sigma^6)$, or of its required horizontal fifth lift, is the specified original test vector.

Finally the sigma coefficient functionals in R770 still require division by the displayed $\sigma^{6p-6}$ on each factor. R878 §6 explains why a low original coefficient, when applied after the enlarged-space action, can involve high sigma denominators. The new integral intertwiners supply a definite integral object for that comparison; they do not remove the denominators or their source terms.

Consequently no claim is made that

$$
P_{h-1}(1/\sqrt{-3})\,f_i g_j\ne0,\qquad
h=6i+7,\quad i+j=N-1,
$$

for any universally chosen original label. The R706/R739 boundaries and the unknown normal coefficient of the actual modular quotient remain unchanged.

## Sources

- [R878](R878-original-finite-theta-action-and-section-projections.md), the original finite theta action, its normalization on $\ker D$, and its complete weight filtration.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md), especially (727.2), (727.14), (727.17), the fixed $\theta_h(y)=[y]^{-h(p-1)}$, and the actual Legendre norm.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md), the original same-label coefficient condition.
- [S. W. Shin, *Abelian varieties and Weil representations*](https://math.berkeley.edu/~swshin/AV-Weil.pdf), Propositions 2.12–2.13, for the relative finite theta representation and base-change-compatible equivalence.
- [S. Gurevich and R. Hadani, *Notes on the Self-Reducibility of the Weil Representation and Higher-Dimensional Quantum Chaos*](https://arxiv.org/pdf/0708.0755), Theorems 7–8, for the finite Weil character and nonsplit-torus multiplicity formulas.
- [B. Liu and Q. Zhang, *Uniqueness of certain Fourier-Jacobi models over finite fields*](https://arxiv.org/pdf/1810.11901), §2.3, equation (2.2), for the anisotropic norm model and its cuspidal irreducibility. The original-vector comparison (881.26)–(881.32) is proved directly here.
- [P. Mercuri and R. Schoof, *Modular forms invariant under non-split Cartan subgroups*](https://reneschoof.github.io/mcom3503.pdf), §4, for the same affine model and Weyl action used in R727.
