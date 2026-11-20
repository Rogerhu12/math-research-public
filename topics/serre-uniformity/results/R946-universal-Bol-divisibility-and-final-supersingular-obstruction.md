# R946: universal Bol divisibility and the final supersingular obstruction

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved.** This result proves a uniform divisibility statement for every form in the actual high-weight space, stronger than divisibility for a single eigenform. It does **not** prove the additional Hasse divisibility needed in (HS6) of [the saturation note](../notes/R946-Hecke-localization-and-theta-saturation.md). It also explains why the last supersingular quotient cannot simply be removed by asserting that its CM localization is zero.

The normalization is precisely R932's original full-six normalization. All statements may first be made on the fine tame full-six curve. The prime-to-$p$ tame descent, determinant transports and full norm extensions are then the original ones. No new choice of $\zeta$ or replacement of the named oldform is made.

## 1. Operators and an identity valid before Hecke localization

Let $p\ge41$ be prime, let $k$ be a perfect residue field containing the full-six marking, let
$$
2\le r\le p-2,
$$
and put
$$
w=p+1-r.
\tag{946.1}
$$
The primary statement is on a connected fine tame full-six curve $X$ over $k$, with $M_a=H^0(X,\omega^a)$ and $S_a=H^0(X,\omega^a(-\mathrm{cusps}))$. It includes both parities on this fine curve. On descent through a tame group with the central element $-I$, one must use a character $\chi$ satisfying $\chi(-I)=(-1)^w=(-1)^r$; the operators below preserve that character. Thus for the original $H_6$ space with trivial central character, the asserted application is to **even** $r$. No conclusion is extracted from an odd-weight space with incompatible central character.

For an original admissible upper label $h$, set $r=2h-p-1$. Whenever $2\le r\le p-2$, this is even and $w=2p+2-2h$, $r+2=2h-p+1$ are exactly the original two weights. The labels of R932 give $r=2,8$; the operator statement is not restricted to those two values. The actual tame character, paired marking, and full norm condition must still be retained for any additional label.

Write $\mathcal A$ for the Hasse invariant, $\mathcal B=\partial_{p-1}\mathcal A$, and
$$
\partial_k=\Theta_{\tau'}-\frac{k}{12}E_2,
\qquad
\mathcal T_k(H)=6(\mathcal A\partial_kH+k\mathcal B H).
\tag{946.2}
$$
Thus $\mathcal T$ has Fourier effect $\Theta_Q=Q\,d/dQ$, as in R932(932.15–16). All reductions in this note are modulo $p$.

There is a globally regular, cuspidality-preserving differential operator
$$
\mathscr D_r:S_w\longrightarrow S_{p+r+1}
\tag{946.3}
$$
such that, for **every** $H\in S_w$,
$$
\boxed{\quad
\mathcal T^rH=6^r\mathcal A^r\mathscr D_rH.
\quad}
\tag{946.4}
$$
The operator $\mathscr D_r$ is polynomial in successive Serre derivatives, $E_4$ and $E_6$, with denominators prime to $p$. For example,
$$
\mathscr D_2H
=\partial_{w+2}\partial_wH+\frac{E_4}{144}H.
\tag{946.5}
$$
In particular the high target weight $(r+1)p+1$ in (HS7) can be reduced, for the entire source space, to $p+r+1$. What remains to be proved on the actual generalized CM packet is exactly **one further** Hasse factor.

### Proof of (946.4)

Use $\partial$ for the graded Serre derivation. First,
$$
\partial\mathcal B=-\frac{\mathcal A E_4}{144}.
\tag{946.6}
$$
Both sides have weight $p+3$. Since $\mathcal A(Q)=1$ and $\mathcal B(Q)=E_2(Q)/12$, their equality follows from the Ramanujan identity
$\Theta_{\tau'}E_2=(E_2^2-E_4)/12$ and the full-level $q$-expansion principle:
$$
\partial_{p+1}\mathcal B(Q)
=\frac{E_2^2-E_4}{144}-\frac{E_2^2}{144}
=-\frac{E_4}{144}.
$$

On the ordinary locus put $t=\mathcal B/\mathcal A$. This is a rational section of weight two. The quotient rule and (946.6) give
$$
\partial t=-t^2-\frac{E_4}{144}.
\tag{946.7}
$$
We now carry out a formal polynomial argument, not a specialization or numerical experiment. Take variables $H_i$ of weight $w+2i$, with $\partial H_i=H_{i+1}$, and extend the derivation to the polynomial ring in $E_4,E_6,t,H_0,H_1,\ldots$ by
$$
\partial E_4=-E_6/3,\qquad
\partial E_6=-E_4^2/2,\qquad
\partial t=-t^2-E_4/144.
$$
Define polynomials, linear in the variables $H_i$, by
$$
P_0=H_0,\qquad
P_{j+1}=\bigl(\partial+(w+2j)t\bigr)P_j.
\tag{946.8}
$$
Their degree in $t$ is at most $j$. If $D_t$ is formal differentiation with respect to $t$, then
$$
[D_t,\partial]=-2tD_t.
$$
Consequently
$$
D_tP_j=j(w+j-1)P_{j-1}.
\tag{946.9}
$$
For completeness, the $j=1$ case is $D_tP_1=wH_0$. If (946.9) holds at $j$, differentiation of (946.8) gives
$$
\begin{aligned}
D_tP_{j+1}
&=\bigl(\partial+(w+2j-2)t\bigr)D_tP_j+(w+2j)P_j\\
&=\bigl(j(w+j-1)+w+2j\bigr)P_j\\
&=(j+1)(w+j)P_j.
\end{aligned}
$$
At $j=r$ the coefficient in (946.9) vanishes because $w+r-1=p$. Since $\deg_tP_r\le r<p$, a polynomial with zero $t$-derivative must be independent of $t$. Define $\mathscr D_rH$ by substituting $H_i=\partial^iH$ in this $t$-independent polynomial $P_r$.

This definition proves global regularity: only globally regular modular forms and their Serre derivatives occur. Every term has weight $w+2r=p+r+1$. It also proves cuspidality because the Serre derivative preserves vanishing of the constant term at each cusp.

To identify the operator, the product rule in (946.2) gives, for every integer $j\ge0$ and every rational modular section $U$ of weight $k$,
$$
\mathcal T_{k+j(p-1)}(\mathcal A^jU)=\mathcal A^j\mathcal T_k(U).
\tag{946.10}
$$
Indeed the coefficient of $\mathcal B\mathcal A^jU$ is $j+k+j(p-1)=k$ in characteristic $p$. Applying (946.10) and (946.8) successively gives
$\mathcal T^jH=6^j\mathcal A^jP_j$ on the ordinary locus. At $j=r$ this is (946.4), and both sides are globally regular, so the identity holds everywhere. Formula (946.5) follows at once from (946.7) with $w=-1$ in the residue field. This completes the proof.

## 2. A single, concrete supersingular obstruction

Let $X$ be a connected fine tame curve and let $\Sigma$ be its reduced supersingular divisor. The Hasse invariant has this divisor, and $\mathcal B$ is nonzero at each point of $\Sigma$. Define
$$
\mathscr O_r(H)
=\left.\frac{\mathscr D_rH}{\mathcal B}\right|_\Sigma
\in H^0(\Sigma,\omega^r).
\tag{946.11}
$$
The division is only along $\Sigma$, where it is legitimate. Its use does not drop any point, local frame factor, or fine-cover multiplicity.

For any subspace $M\subset S_w$, the following conditions are equivalent:
$$
\mathcal T^rM\subset\mathcal A^{r+1}S_{r+2},
\qquad
\mathscr D_rM\subset\mathcal A S_{r+2},
\qquad
\mathscr O_r(M)=0.
\tag{946.12}
$$
The first equivalence follows from (946.4), since $6^r$ is a unit and multiplication by $\mathcal A^r$ is injective. The second follows from the fact that the Hasse divisor is reduced. The quotient by $\mathcal A$ is regular everywhere if it is regular along $\Sigma$; at the cusps the Hasse invariant is a unit, so the quotient is still cuspidal.

One may also use the following exact sequence of complete spaces, rather than eigenvector spaces:
$$
0\longrightarrow S_{r+2}
\xrightarrow{\ \mathcal A\ }
S_{p+r+1}
\longrightarrow H^0(\Sigma,\omega^{p+r+1})
\longrightarrow0.
\tag{946.13}
$$
The sheaf sequence comes from the Hasse divisor. The obstruction to surjectivity of global sections is
$H^1(X,\omega^{r+2}(-\mathrm{cusps}))$, whose Serre dual is $H^0(X,\omega^{-r})=0$. Here the Kodaira–Spencer identification is $\Omega_X^1=\omega^2(-\mathrm{cusps})$, and $\deg\omega>0$ on the fine tame curve. Thus (946.13) is exact.

For the original named companions with $r=2,8$, R932 gives
$$
\mathscr D_rF=6^{-r}\mathcal A V_{r+2}^\dagger,
\qquad \mathscr O_r(F)=0.
\tag{946.14}
$$
This is still only the named-vector assertion. The open statement is $\mathscr O_r(M_{\rm CM})=0$ for the whole actual generalized packet.

## 3. The last supersingular module contains the dual high-weight module

There is an exact sequence
$$
0\longrightarrow M_r
\longrightarrow H^0(\Sigma,\omega^r)
\longrightarrow S_w^\vee
\longrightarrow0,
\qquad w=p+1-r.
\tag{946.15}
$$
Here $M_r=H^0(X,\omega^r)$ includes Eisenstein forms, and $S_w^\vee$ is the linear dual with the Serre-dual correspondence action specified below. This is the complete fine-level sequence, not an assertion that the last arrow is an isomorphism before localization. If one subsequently takes a tame $\chi$-isotypic component, its last term is the dual of the $\chi^{-1}$ component of $S_w$; one must retain that paired character or the actual transpose transport. In particular the two character labels must not be identified merely because their dimensions agree.

To prove (946.15), start with
$$
0\longrightarrow\omega^{r-p+1}
\xrightarrow{\ \mathcal A\ }\omega^r
\longrightarrow\omega^r|_\Sigma\longrightarrow0.
$$
Since $r<p-1$, the first sheaf has no global sections. Since $r\ge2$,
$$
H^1(X,\omega^r)^\vee
=H^0(X,\omega^{2-r}(-\mathrm{cusps}))=0.
$$
Finally,
$$
H^1(X,\omega^{r-p+1})^\vee
=H^0(X,\omega^{p+1-r}(-\mathrm{cusps}))=S_w.
$$
The long exact sequence is therefore exactly (946.15).

All these maps are natural for prime-to-$p$ Hecke correspondences. In Gross's modular normalization, multiplication by $\mathcal B|_\Sigma$ multiplies a Hecke eigenvalue by $\ell$, while $\mathscr D_r$ multiplies it by $\ell^r$. Hence
$$
T_\ell\mathscr O_r=\ell^{r-1}\mathscr O_rT_\ell.
\tag{946.16}
$$
For the last arrow in (946.15), Serre duality gives the same factor $\ell^{r-1}$ and the transpose correspondence on $S_w$. After the Fricke/transpose transport this is the dual of the original $T_\ell$ action, multiplied by $\ell^{r-1}$. These normalizations are precisely Edixhoven, *The weight in Serre's conjectures on modular forms* (1992), Propositions 7.2–7.3. His proof is the sheaf trace and Kodaira–Spencer calculation; it applies to the complete modules. On the original marked spaces the transpose and norm transports must be those already fixed in R913, and the two markings are retained whenever the correspondence exchanges them.

In particular, on the complete fine-level module, if the high-weight module contains the original CM eigensystem $\kappa$, then the target of the last arrow in (946.15) contains its dual packet with the transformed system
$$
\kappa'_\ell=\ell^{r-1}\kappa_\ell.
\tag{946.17}
$$
Localization is exact. Therefore $H^0(\Sigma,\omega^r)_{\kappa'}$ is nonzero: it surjects onto a nonzero dual high-weight packet. This is the transformed Hecke support permitted by (946.16). For an individual tame-character summand, the assertion uses the corresponding paired high-weight summand and the actual R913 transpose identification; it is not a declaration that every summand of the full supersingular space has that support.

This observation excludes the proposed shortcut of killing the **entire** last Hasse quotient by a Serre-weight support argument. It does not exclude the possibility that the particular differential-operator image (946.11) vanishes in that nonzero quotient. Proving that image vanishes is the remaining concrete task.

The fine-level statements descend through the original tame invariants because their orders are prime to $p$. The Serre pairing descends by the actual trace; the paired character is the dual tame character, as in R913. No fine-cover degree is replaced by an arbitrary scale, and no unidentified primitive-source constant is removed.

## 4. What the Ash–Stevens sequence supplies

The complete localized coefficient exact sequence is a useful input, but supplies a different map. For a prime-to-$p$ tame level and a non-Eisenstein maximal ideal, put $g=w-2=p-1-r$. Ash–Stevens's coefficient sequence, followed by compactly supported cohomology and localization, gives a short exact sequence whose coefficient representations are
$$
0\longrightarrow\operatorname{Sym}^{p-1-r}
\longrightarrow I_{p-1-r}
\longrightarrow\det^{p-1-r}\operatorname{Sym}^{r}
\longrightarrow0.
\tag{946.18}
$$
Thus the two modular weights are indeed $w$ and $r+2$. This is a complete-module statement and does not have the nonliftable-quotient-eigenvector problem. However, exactness alone supplies neither an isomorphism of its two ends nor their equality of lengths, and it does not identify its maps with (946.11).

A directly accessible primary account is John Bergdall and Robert Pollack, *Slopes of modular forms and the ghost conjecture, II*, Trans. Amer. Math. Soc. 372 (2019), 357–388, §6.1, Theorem 6.4, manuscript pp. 22–24:
https://arxiv.org/pdf/1710.01572 . Their Lemma 6.2 removes the localized $H_c^2$ terms and Theorem 6.4 gives the complete short exact sequences, explicitly citing Avner Ash and Glenn Stevens, *Modular forms in characteristic $\ell$ and special values of their $L$-functions*, Duke Math. J. 53 (1986), 849–868, Theorem 3.4 and Lemma 3.2.

For comparison, Emerton–Gee–Herzig, *Weight cycling and Serre-type conjectures for unitary groups*, §2.3, Proposition 2.3.1 and Corollary 2.3.3, use a factorization of a $p$-Hecke operator through an induced representation to force the occurrence of another weight when the operator has a kernel. Those statements by themselves do not assert equality of full localized lengths or the vanishing of (946.11). Primary manuscript:
https://math.uchicago.edu/~emerton/pdffiles/egh.pdf .

Edixhoven's primary author manuscript used above is
https://websites.math.leidenuniv.nl/edixhoven/public_html_rennes/publications/weight.ps.gz , §§3 and 7, especially manuscript pp. 23–25.

No new finite mathematical computation was executed for this result. The new proved content is (946.4), the reduction to the single map (946.11), and the exact support obstruction (946.15–17). The actual generalized-packet vanishing remains open. No identification of this supersingular obstruction, or of the full R932/R936 trace, with the higher original $Q'_h(0)$ is asserted. In particular this result cannot turn a nonzero supersingular trace into a nonzero central derivative.
