# R951: the Bol concomitant and supersingular obstruction symmetry

Date: 2026-11-20. Authoring agent: handoff_audit.

**Status: proved symbolic structure, not generalized-packet vanishing.** This continues [R946](R946-universal-Bol-divisibility-and-final-supersingular-obstruction.md). It identifies the symmetry of the composition of its actual obstruction map with its actual connecting map. It makes no new finite calculation and does not identify this pairing with the different original Cartier functional of R932, or with the higher normal coefficient of R925.

## 1. The precise pairing

Retain R946's connected fine tame full-six curve $X$ over a perfect residue field $k$, the Hodge bundle $\omega$, its reduced supersingular divisor $\Sigma$, and the original normalized forms
$$
\mathcal A\in M_{p-1},\qquad
\mathcal B=\partial\mathcal A\in M_{p+1},\qquad
\partial\mathcal B=-\mathcal A E_4/144.
\tag{951.1}
$$
Here $p\ge41$, $2\le r\le p-2$, $w=p+1-r$, and $\partial$ is the graded Serre derivation in the original full-six convention. Let $\mathscr D_r:S_w\to S_{p+r+1}$ be exactly R946's operator, so that $\mathcal T^r=6^r\mathcal A^r\mathscr D_r$. Put
$$
\mathscr O_r(H)=\left.\frac{\mathscr D_rH}{\mathcal B}\right|_\Sigma,
\qquad
J_r=\delta\circ\mathscr O_r:S_w\longrightarrow S_w^\vee,
\tag{951.2}
$$
where $\delta$ is the last arrow of the complete fine-level sequence R946(946.15).

Use the positive-principal-part convention for the connecting map, consistent with R932(932.30–33). Its Serre pairing is
$$
\mathscr B_r(H,H'):=J_r(H)(H')
=\sum_{P\in\Sigma}\operatorname{Res}_P
\operatorname{KS}\!\left(
\frac{(\mathscr D_rH)H'}{\mathcal A\mathcal B}
\right).
\tag{951.3}
$$
The fraction has weight two. It is used locally near $\Sigma$, where $\mathcal B$ is a unit; poles at other points have no role in the definition of the connecting map. A simultaneous opposite connecting/Serre convention changes the entire pairing by one common sign and changes none of the identities below.

More explicitly, choose any local unit Hodge frame $\rho$ at $P$ and write
$$
T=\mathcal A/\rho^{p-1},\quad
b=\mathcal B/\rho^{p+1},\quad
d=(\mathscr D_rH)/\rho^{p+r+1},\quad
h'=H'/\rho^w.
$$
By the simple Hasse zero and the same Kodaira–Spencer calculation as R932(932.22–25),
$\operatorname{KS}(\rho^2)=\kappa(T)dT$ with $\kappa(0)=1/b(0)$. Thus
$$
\boxed{\quad
\mathscr B_r(H,H')
=\sum_{P\in\Sigma}\frac{d(P)h'(P)}{b(P)^2}.
\quad}
\tag{951.4}
$$
Every geometric supersingular point of the fine curve occurs once. Over a field not containing every point, this means the residue-field trace sum. Each summand is independent of $\rho$, since both its numerator and denominator have weight $2p+2$. This is precisely the suggested $\sum_P(\mathscr D_rH)_P H'_P/\mathcal B_P^2$, with all point and frame factors retained.

The new conclusion is
$$
\boxed{\quad
\mathscr B_r(H,H')=(-1)^r\mathscr B_r(H',H).
\quad}
\tag{951.5}
$$
In particular it is symmetric for the original $r=2,8$ cases. It is alternating for odd $r$, on a fine-level space where the required odd central character is present. An incompatible odd-character space is not being used to draw any conclusion.

## 2. A global Bol concomitant

This section proves the formal-adjoint assertion directly in the same differential algebra as R946. No claim that $\mathcal A\mathcal B$ is horizontal will be made.

On the ordinary locus set $t=\mathcal B/\mathcal A$. R946 constructs $\mathscr D_r$ from
$$
(\partial+(w+2r-2)t)\cdots(\partial+(w+2)t)(\partial+wt).
\tag{951.6}
$$
As an operator, the rightmost factor acts first. The proof of R946(946.9) shows that all coefficients of (951.6), after expansion in the successive $\partial^jH$, are independent of $t$. Therefore
$$
\mathscr D_r=\sum_{j=0}^r a_j\partial^j,
\qquad a_j\in M_{2(r-j)},\quad a_r=1,
\tag{951.7}
$$
where the $a_j$ are the same polynomials in $E_4,E_6$ as in R946. Coefficients which vanish are permitted. Only denominators prime to $p$ occur.

In the differential-operator algebra with coefficient derivation $\partial$, let formal adjunction fix multiplication operators and send $\partial$ to $-\partial$, reversing products. Since $w=1-r$ in $k$, the constants in the successive factors of (951.6) are
$$
1-r,\ 3-r,\ \ldots,\ r-3,\ r-1.
$$
Reversing their order and changing every sign recovers the same list. Consequently
$$
\boxed{\quad \mathscr D_r^*=(-1)^r\mathscr D_r.\quad}
\tag{951.8}
$$
This identity first holds in the differential algebra containing $t$, and then in the regular coefficient algebra by (951.7). It is an identity of operators on the actual graded modular sections; it does not assume a new analytic coordinate or a new Hodge trivialization.

Define explicitly
$$
\mathscr C_r(H,H')
=\sum_{j=1}^r\sum_{i=0}^{j-1}
(-1)^i\bigl(\partial^{j-1-i}H\bigr)
\partial^i(a_jH').
\tag{951.9}
$$
The product rule gives a telescoping sum:
$$
\begin{aligned}
\partial\mathscr C_r(H,H')
&=(\mathscr D_rH)H'-H\mathscr D_r^*H'\\
&=(\mathscr D_rH)H'-(-1)^rH(\mathscr D_rH').
\end{aligned}
\tag{951.10}
$$
Every term of (951.9) has weight
$2w+2r-2=2p$. It is globally regular. Both factors in every summand vanish at the cusps because $H,H'$ are cuspidal and the Serre derivative preserves cuspidality. In particular
$$
\mathscr C_r(H,H')\in H^0(X,\omega^{2p}(-2\,\mathrm{cusps})).
\tag{951.11}
$$
For the original $r=2$ case this is simply
$$
\mathscr C_2(H,H')=(\partial H)H'-H\partial H',
\qquad
\partial\mathscr C_2=(\mathscr D_2H)H'-H\mathscr D_2H'.
\tag{951.12}
$$
The zeroth-order $E_4/144$ terms cancel exactly.

## 3. The residue identity that removes the apparent denominator problem

Write $C=\mathscr C_r(H,H')$. Its weight is $2p$, the same as $\mathcal A\mathcal B$, so $C/(\mathcal A\mathcal B)$ is an actual global rational function on the fine curve. The product rule and (951.1) give
$$
\partial(\mathcal A\mathcal B)
=\mathcal B^2-\mathcal A^2E_4/144.
\tag{951.13}
$$
On weight-zero functions, Kodaira–Spencer applied to $\partial$ is the usual differential. It follows that the following equality is an equality of global meromorphic differentials:
$$
\operatorname{KS}\!\left(\frac{\partial C}{\mathcal A\mathcal B}\right)
=d\!\left(\frac{C}{\mathcal A\mathcal B}\right)
+\operatorname{KS}\!\left(\frac{C}{\mathcal A^2}\right)
-\operatorname{KS}\!\left(\frac{CE_4}{144\mathcal B^2}\right).
\tag{951.14}
$$
At a supersingular point, the last term is regular because $\mathcal B$ is nonzero there. The exact differential in (951.14) has zero residue at every point, in arbitrary characteristic: the derivative of a Laurent monomial can never contribute a nonzero coefficient to $z^{-1}dz$. Hence
$$
\sum_{P\in\Sigma}\operatorname{Res}_P
\operatorname{KS}\!\left(\frac{\partial C}{\mathcal A\mathcal B}\right)
=\sum_{P\in\Sigma}\operatorname{Res}_P
\operatorname{KS}\!\left(\frac{C}{\mathcal A^2}\right)=0.
\tag{951.15}
$$
For the last equality, $C/\mathcal A^2$ has weight two and has no poles in the interior outside $\Sigma$. At a cusp, $\mathcal A$ is a unit and $C$ vanishes to order at least two by (951.11), whereas Kodaira–Spencer has at most the logarithmic pole. Thus the corresponding differential is regular at every cusp. Its only possible poles are therefore in $\Sigma$, and the residue theorem proves that their complete sum is zero.

Combining (951.10), (951.15), and (951.3) proves (951.5).

The middle differential in (951.14) is essential. Merely integrating (951.10) after dividing by $\mathcal A\mathcal B$ would be invalid because (951.13) is not zero. Likewise, the first differential in (951.3) may have poles at ordinary zeros of $\mathcal B$, so its supersingular sum alone is not automatically zero by the residue theorem. The proof above accounts for both issues and proves symmetry, not universal vanishing.

## 4. Hecke action, tame descent, and the exact remaining boundary

The map $J_r$ is Hecke equivariant in precisely the transported sense of R946(946.16–17). Indeed both $\mathscr O_r$ and the dual target in (946.15) have the factor $\ell^{r-1}$. These factors cancel on composing the maps. Thus $J_r$ intertwines the original source Hecke action with its actual Serre-dual transpose action. Equivalently, after the fixed R913 Fricke/transpose transport, the two arguments in $\mathscr B_r$ satisfy the usual adjoint correspondence identity. No new determinant factor or self-adjoint identification of two different markings is inserted.

On a tame $\chi$ summand the other argument lies in the $\chi^{-1}$ summand. Formula (951.5) interchanges these two actual summands; it does not identify them because they have the same dimension. When a prime-to-$p$ correspondence exchanges markings, the adjoint identity retains those source and target markings. The original full norm extensions are also retained. Descent of the residue pairing uses the actual pullback/trace degree, as in R932(932.37); every such factor appears on both sides of (951.5), so symmetry descends without replacing a degree or omitting a supersingular branch.

For the named original companions $F$ at $r=2,8$, R946(946.14) gives $\mathscr O_r(F)=0$. Equations (951.2) and (951.5) therefore imply
$$
\mathscr B_r(F,H')=0,\qquad
\mathscr B_r(H,F)=0
\tag{951.16}
$$
for every correctly paired $H,H'$. This is a structural constraint on the composed image. It is not $\mathscr O_r(M_{\rm CM})=0$. The exact sequence has kernel $M_r$, so even the stronger assertion $J_r(M_{\rm CM})=0$ would in general show only
$$
\mathscr O_r(M_{\rm CM})\subset M_r|_\Sigma.
\tag{951.17}
$$
One would still have to remove that actual localized kernel, or prove vanishing of the image directly. Conversely the symmetry in the original even-$r$ cases by itself does not imply $J_r(M_{\rm CM})=0$; a symmetric Hecke-compatible form can have a proper radical. No residual reducedness, generalized-packet saturation, or absence of Hecke congruences has been inferred.

Finally, $J_r$ here is the concrete composition of R946's Bol obstruction and Hasse connecting map. The nonzero actual Cartier-cokernel functional of R932 is a different specified object. No equality of the two has been proved here. R945's central $Q'_h(0)$ zeros and R948's scalar-root separation are unaffected by this result.

### Dependencies

- R946(946.2–10): the original operators, regular Bol polynomial and universal divisibility.
- R946(946.11–17): the obstruction, complete Hasse sequence, dual character and Hecke normalization.
- R932(932.22–25), (932.37–39): local Hasse/KS frame calculation and actual fine-cover trace convention.
- The formal-adjoint, concomitant, and residue arguments are proved in full above. No new mathematical computation, finite-prime scan, or unregistered numerical output is used.
