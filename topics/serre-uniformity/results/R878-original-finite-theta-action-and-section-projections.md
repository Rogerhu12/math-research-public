# R878 — Actual non-etale theta action and two original section projections

Date: 2026-11-16. Status: proved finite-theta construction and two nonzero projections. This does **not** identify either projection with an original R770 Cartier factor, with the primitive/Legendre test vector, or with the normal coefficient of the original modular quotient.

## 1. Original curve, line bundles, and finite field

Let $p\ge41$ be prime, $p\equiv5\pmod6$, and retain the original curve and differential

$$
E_0:y^2=x^3-1,\qquad O=\infty,\qquad
\omega=\frac{dx}{2y},\qquad D=\frac d\omega.
\tag{878.1}
$$

Use the original tame six-level marking and its specified embedding. We work over $k_0=\mathbf F_{p^2}$, and may extend to $k=\overline{\mathbf F}_p$ for representation-theoretic proofs. This field contains the six-torsion and the original tame constants. Indeed $x\mapsto x^3$ permutes $\mathbf F_p$, so the quadratic-character sum giving the trace of Frobenius is zero. Frobenius satisfies $\operatorname{Fr}^2=[-p]$, and $-p\equiv1\pmod6$; hence it acts trivially on $E_0[6]$ after squaring.

Put $L_m=O_{E_0}(mO)$ and let $s_m$ be its canonical section with divisor $mO$, with the multiplication convention $s_a s_b=s_{a+b}$. Write

$$
H=H^0(E_0,L_{6p}),\qquad \dim_{k_0}H=6p.
\tag{878.2}
$$

Thus $f s_{6p}\in H$ means that the rational function $f$ has no poles away from $O$ and pole order at most $6p$ at $O$. The original six-dimensional theta space maps into $H$ by

$$
j:H^0(E_0,L_6)\longrightarrow H,\qquad
v\longmapsto v s_6^{p-1}.
\tag{878.3}
$$

In the original characteristic-zero analytic trivialization, $s_6$ is represented by $\sigma(z)^6$, with the same flat parameter and Gaussian as in R770. In particular the two actual sections transported by (878.3) are

$$
v_F=x s_{6p}=j(x s_6),\qquad
v_G=-xy s_{6p}=j(-xy s_6).
\tag{878.4}
$$

The notation in (878.4) is algebraic. It does not assume that the entire characteristic-zero sigma series has ordinary coefficientwise reduction modulo $p$.

Let $\mathcal O=\mathbf Z[\zeta]$ be the original Eisenstein CM order. Since $p$ is inert,

$$
\mathcal O/p\mathcal O=\mathbf F_{p^2}.
$$

Fix its identification by its action on $\operatorname{Lie}(E_0)$ in the differential (878.1). For

$$
T=\{q\in\mathbf F_{p^2}^{\times}:q^{p+1}=1\},
\qquad \chi(q)=q,
\tag{878.5}
$$

the original CM endomorphisms induce an actual automorphism $a_q$ of the finite group scheme $E_0[p]$. This assertion uses the action of $\mathcal O/p\mathcal O$ on $E_0[p]$, not an assertion that $q$ is an automorphism of the whole elliptic curve. The action on its tangent line is multiplication by $q$. Rosati conjugation on $\mathcal O$ is complex conjugation, so $a_q$ preserves the $p$-Weil pairing because $q\bar q=q^{p+1}=1$.

## 2. A canonical lift on the actual theta group

Let $\mathcal G=\mathcal G(L_{6p})$ be the theta group. Its center is $\mathbf G_m$, its quotient is $E_0[6p]$, and its natural representation on $H$ has central weight one. Let $\mathcal G_p$ and $\mathcal G_6$ be the inverse images of $E_0[p]$ and $E_0[6]$, respectively.

The commutator pairing of $\mathcal G_p$ is $e_p^6$. It is nondegenerate because $p\nmid6$. The two groups $\mathcal G_p$ and $\mathcal G_6$ commute: a cross-commutator is killed by both $p$ and $6$. Multiplication gives the central-product description

$$
\mathcal G=
(\mathcal G_6\times\mathcal G_p)/
\{(\lambda,\lambda^{-1}):\lambda\in\mathbf G_m\}.
\tag{878.6}
$$

The symmetric structure on $L_{6p}$ induces an involution $\iota$ of $\mathcal G_p$, trivial on the center and inducing $u\mapsto-u$ on $E_0[p]$. A scalar change of the symmetric line-bundle isomorphism does not change this involution.

Here is the needed canonical section, including its fppf meaning. For a test scheme and $u\in E_0[p]$, choose fppf locally a lift $g$ of $u/2$ to $\mathcal G_p$, and set

$$
\tau(u)=g\iota(g)^{-1}.
\tag{878.7}
$$

The expression is independent of the lift: replacing $g$ by $\lambda g$ multiplies both $g$ and $\iota(g)$ by the same central $\lambda$. It therefore descends from the fppf cover and defines a morphism of schemes. It covers $u$ and satisfies $\iota(\tau(u))=\tau(u)^{-1}$.

If $e$ denotes the commutator pairing of $\mathcal G_p$, commuting the two lifts in (878.7) gives

$$
\tau(u)\tau(v)=e(u,v)^{1/2}\tau(u+v).
\tag{878.8}
$$

Here $1/2$ means the inverse of $2$ modulo $p$ on $\mu_p$; no square-root choice is being made. To check the sign directly, take lifts $g,h$ of $u/2,v/2$. Moving $\iota(g)^{-1}$ first past $h$ and then past $\iota(h)^{-1}$ contributes $e(u/2,v/2)^2=e(u,v)^{1/2}$.

Every element of $\mathcal G_p$ is uniquely $\lambda\tau(u)$. Consequently

$$
A_q(\lambda\tau(u))=\lambda\tau(a_q u)
\tag{878.9}
$$

is a well-defined group automorphism, and $A_qA_{q'}=A_{qq'}$. This uses the actual pairing preservation proved in §1.

Extend (878.9) to $\mathcal G$ by the identity on $\mathcal G_6$, using (878.6). The extension is well-defined because the two definitions coincide on the center. In particular it fixes the actual six-primary theta group pointwise, not merely its abstract isomorphism class. Thus the fixed original six-level marking is preserved.

## 3. Intertwiners and their normalization

The finite theta representation $H$ is absolutely irreducible of central weight one. The uniqueness theorem for a nondegenerate theta group in arbitrary characteristic gives an intertwiner $M_q$ satisfying

$$
M_q\,\rho(g)\,M_q^{-1}=\rho(A_qg)
\qquad(g\in\mathcal G).
\tag{878.10}
$$

It is unique up to scalar. One may first apply the theorem over $k$. The Hom space of the two representations is the kernel of linear equations over $k_0$ and commutes with this field extension, so it is one-dimensional over $k_0$ as well. A nonzero $k_0$-intertwiner is an isomorphism after extension and hence over $k_0$.

We now remove the scalar ambiguity by an actual descent subspace. Let

$$
F:E_0\longrightarrow E_0^{(p)},\qquad A=\ker F\simeq\alpha_p.
$$

There is a canonical identification

$$
L_{6p}=F^*O_{E_0^{(p)}}(6O).
\tag{878.11}
$$

It gives an $A$-linearization, or equivalently a splitting $\widetilde A\subset\mathcal G_p$ above $A$. This splitting is unique over $k_0$: two splittings differ by a homomorphism $\alpha_p\to\mathbf G_m$, and this group is zero over a field. Equivalently, its Cartier-dual description is $\alpha_p(k_0)=0$.

The CM action preserves $A$, and hence $A_q$ preserves $\widetilde A$ by uniqueness. Therefore $M_q$ preserves

$$
H^{\widetilde A}
=F^*H^0(E_0^{(p)},O(6O)),
\qquad \dim H^{\widetilde A}=6.
\tag{878.12}
$$

This is the Frobenius-transported original six-level space. The action of $\mathcal G_6$ on it is absolutely irreducible: $F$ identifies the six-torsion on the two curves and transports its theta group to the degree-six line bundle in (878.12).

Since $A_q$ is the identity on $\mathcal G_6$, equation (878.10) implies that $M_q$ commutes with $\mathcal G_6$. Its restriction to (878.12) is therefore a nonzero scalar. Normalize it by

$$
M_q|_{H^{\widetilde A}}=1.
\tag{878.13}
$$

Now $M_qM_{q'}$ and $M_{qq'}$ satisfy both (878.10) and (878.13), so uniqueness proves the genuine group law

$$
M_qM_{q'}=M_{qq'},\qquad M_1=1.
\tag{878.14}
$$

Thus $T$ acts linearly on the actual $6p$-dimensional space $H$, rather than only projectively. Everything is defined over $k_0$. The construction also commutes with Frobenius: its action sends $q$ to $q^p=q^{-1}$ and transports the specified six-level marking in the usual way. No characteristic-zero lift of every $M_q$, and no action on an unspecified integral modular-quotient lattice, is asserted.

The representation-theoretic input here is the finite theta theorem, not a split Heisenberg-group model. For a supersingular elliptic curve $E_0[p]$ is a nonsplit extension of $\alpha_p$ by $\alpha_p$ and has no Lagrangian product decomposition.

## 4. Original invariant derivative and the complete weight list

Use the Cartier connection on the Frobenius pullback (878.11). In the rational frame $s_{6p}$ its derivative in the direction (878.1) is simply

$$
\mathscr D(f s_{6p})=(Df)s_{6p}.
\tag{878.15}
$$

This maps $H$ into $H$. At $O$, differentiation increases a pole of order below $6p$ by at most one; the leading derivative of a pole of order exactly $6p$ vanishes in characteristic $p$. There are no other poles.

The original R574 identities, in precisely the differential (878.1), are

$$
D^p=0,\qquad D^{p-1}x=-B,
$$
$$
B=(-1)^{N+1}\binom{3N+2}{2N+1}\in\mathbf F_p^\times,
\qquad p=6N+5.
\tag{878.16}
$$

Thus $\mathscr D^p=0$. Its kernel is exactly (878.12): the kernel of the nonzero derivation $D$ on $k_0(E_0)$ is the subfield of $p$-th powers, and the pole bound on a $p$-th root is $6$. In particular

$$
\ker\mathscr D=H^{\widetilde A},\qquad\dim\ker\mathscr D=6.
\tag{878.17}
$$

The infinitesimal action of $\widetilde A$ is $\mathscr D$, up to the harmless common sign convention for the natural action on sections. Since $a_q$ acts on $\operatorname{Lie}(A)$ by $q$, (878.10) gives

$$
M_q\mathscr D M_q^{-1}=q\mathscr D.
\tag{878.18}
$$

The Jordan blocks of $\mathscr D$ have length at most $p$. Their number is $\dim\ker\mathscr D=6$, and their total dimension is $6p$. Consequently all six blocks have length exactly $p$.

Because $p\nmid|T|$, decompose $H$ into character spaces. The kernel (878.17) has trivial character by (878.13), and $\mathscr D$ raises the character exponent by one. The kernel filtration, or a homogeneous choice of Jordan chains, therefore gives

$$
\boxed{
H=\bigoplus_{a\in\{0,2,3,\ldots,p\}}H_a,\qquad
M_q|_{H_a}=q^a,\qquad \dim H_a=6.
}
\tag{878.19}
$$

The character $\chi^1$ is absent. For example, on
$\ker\mathscr D^r/\ker\mathscr D^{r-1}$ the character is $\chi^{1-r}$, for $1\le r\le p$, and each quotient has dimension six. This proves the list without inferring a representation from its dimension alone.

Let

$$
\mathsf e_a=\frac1{p+1}\sum_{q\in T}q^{-a}M_q.
\tag{878.20}
$$

These are actual, canonically normalized projectors on $H$. In particular

$$
\mathscr D^{p-1}:H_2\xrightarrow{\;\sim\;}H_0,\qquad
\mathscr D^{p-4}:H_5\xrightarrow{\;\sim\;}H_0.
\tag{878.21}
$$

This stable space grows with $p$. It is not a nonexistent constant-rank scalar differential closure of the six original sigma sections.

## 5. Nonzero projections of the two original sections

The original rational identities $Dx=2y$, $Dy=3x^2$ give

$$
D^3x=24xy,\qquad
v_G=-\frac1{24}\mathscr D^3v_F.
\tag{878.22}
$$

Combine (878.16), (878.18), and (878.20). Since $s_{6p}\in H_0$,

$$
\boxed{
\mathscr D^{p-1}(\mathsf e_2v_F)=-B s_{6p},
\qquad
\mathscr D^{p-4}(\mathsf e_5v_G)=\frac B{24}s_{6p}.
}
\tag{878.23}
$$

Both right-hand coefficients are units in the fixed residue field. Thus

$$
\mathsf e_2v_F\ne0,\qquad
\mathsf e_5v_G\ne0,\qquad
\mathsf e_5v_G=-\frac1{24}\mathscr D^3(\mathsf e_2v_F).
\tag{878.24}
$$

These equations identify the nonzero projections by their images under the specified isomorphisms (878.21); they are more precise than an assertion that the ambient representation contains those characters.

They are also compatible with the actual six-level theta action, because all the operators $M_q$ commute with $\mathcal G_6$. Neither a different Gaussian nor a different section has replaced $x\sigma^6$ or $-xy\sigma^6$ before the explicit multiplication (878.3).

## 6. Exact remaining comparison with the original critical jet

The result above does not yet identify (878.20) with the diagonal coefficient filters in R770.

First, (878.13) fixes the Frobenius-transported six-dimensional subspace. It does not assert that all $M_q$ preserve the different six-dimensional subspace $jH^0(L_6)$ in (878.3). Nor does it identify these intertwiners with automorphisms of $E_0$ fixing its marked origin. The construction only required actual automorphisms of the finite group scheme $E_0[p]$ and of its theta group.

Second, to recover the original analytic section from (878.3) one divides by $s_6^{p-1}$, represented in characteristic zero by $\sigma^{6p-6}$. On the two sections (878.4) this returns exactly

$$
F=x\sigma^6=z^4\sum_i f_i z^{6i},
\qquad
G=-xy\sigma^6=z\sum_j g_j z^{6j}.
\tag{878.25}
$$

On a general section $f s_{6p}\in H$ the same expression would be $f\sigma^6$, where $f$ may have a pole of order $6p$. Extracting a low coefficient can then require sigma coefficients through degree $6p+n$. The original first-$p$ integrality of the six sections does not supply ordinary coefficientwise reduction through that range. No integral extension of the original coefficient functionals to all of $H$, compatible with the $M_q$, has been proved here.

Finally, $\chi(q)=q$ was fixed by the original tangent action. The actual cuspidal label, its inverse-character convention, the original finite split/Cartan pairing, and its Legendre factor must still be transported together before any $\mathsf e_a$ can be identified with that test vector. The nonzero pair in (878.24) is not an assertion that the two R770 factors at one primitive label are units. In particular it neither removes $C_{p-3}$ from R875 nor contradicts the actual R706/R739 examples.

The new conclusion is an actual finite theta-group action preserving the specified tame marking, with the complete normalized derivative filtration and two explicit original-section projections. The next arithmetic step remains the integral comparison with the original filtered jet or with the actual ramified source of the modular quotient.

## Sources

- [R574](R574-completed-zeta-Cartier-input.md), (574R.3)–(574R.7), fixes the original $D$, the sign in $D^{p-1}x=-B$, and the nonzero $B$.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md), §§1–3, fixes the two sections and the actual same-label condition.
- [S. W. Shin, *Abelian varieties and Weil representations*](https://math.berkeley.edu/~swshin/AV-Weil.pdf), Propositions 2.12–2.13: uniqueness and existence of the finite nondegenerate theta representation in arbitrary characteristic. Sections 5.4 and 6.4 give the broader $p$-divisible construction; it is not needed in place of the explicit finite lift in §2 above.
- [B. Moonen, *The Theta group of a line bundle*, Chapter VIII](https://www.math.ru.nl/personal/bmoonen/BookAV/ThetaGr.pdf), §§1–2 and Theorem 8.32, for theta groups, descent linearizations, and the arbitrary-characteristic theorem. The paragraph preceding Lemma 8.24 explicitly distinguishes the supersingular $E[p]$ theta group from a split Heisenberg group.
