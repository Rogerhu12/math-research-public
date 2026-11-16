# R888 — Original two cyclic quotients, saturated Hadamard transport, and the sigma source

Date: 2026-11-16. Status: proved. The two-flag quotient and contraction of R886 are transported to actual cyclic-$p$ quotients of the original elliptic curve. The original enlarged $F\otimes G$ source is explicit after this transport. The full mixed character and the divisions by $p$ in R886 remain present.

## 1. Original CM point and the two cyclic subgroups

Keep the original curve, differential, sigma, and $p$-marking:
$$
E_0:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad
\sigma(z)=z+O(z^7),\qquad
p\ge41,\quad p\equiv5\pmod6.
\tag{888.1}
$$
Let $\mathbb E=\mathbf F_{p^2}$, fix the original
$s=\sqrt{-3}=1+2\zeta$, and denote the marked $p$-torsion point with CM coordinate $a\in\mathbb E$ by $P_a$. Enlarge the valuation ring $R'$ of R886 to contain the same full marking if necessary.

The two generic lines are
$$
C_+=\{P_a:a\in\mathbf F_p\},\qquad
C_-=\{P_{sa}:a\in\mathbf F_p\}.
\tag{888.2}
$$
The second line is exactly the trace-zero line in $\mathbb E$ because $\overline s=-s$. We use the same notation for their finite flat closures. Since $[s]$ has degree three, prime to $p$,
$$
[s]C_+=C_-
\tag{888.3}
$$
is an equality of actual finite flat subgroups.

Let
$$
\pi_\pm:E_0\longrightarrow E_\pm=E_0/C_\pm
\tag{888.4}
$$
be the actual cyclic-$p$ quotients, with the original origin and the transported tame marking. These are the cyclic quotients to which R874 applies at the fixed CM fiber. They are not two arbitrarily chosen elliptic curves with the same reduction.

Throughout this paper the relation (888.3) is used at this fixed CM fiber. The general deformation $y^2=x^3+tx-1$ does not have the endomorphism $[s]$, so no corresponding identity of the two complete deformation families is asserted.

## 2. The Hadamard isogeny and the actual quotient diagram

Define the actual degree-four isogeny
$$
H:E_0^2\longrightarrow E_0^2,\qquad
H(P,Q)=(P+Q,P-Q).
\tag{888.5}
$$
Its kernel is $\{(T,T):T\in E_0[2]\}$. Since $p$ is odd, its restriction to the $p$-torsion is an isomorphism.

Use R886's original coordinates $(a,b)$ on the target $p$-torsion. If the source coordinates are $(r,t)$, then
$$
a=r+t,\qquad b=r-t.
$$
The two flags of R886 satisfy
$$
a=-\overline b
\quad\Longleftrightarrow\quad
r+\overline r=0,\quad t-\overline t=0,
$$
$$
a=\overline b
\quad\Longleftrightarrow\quad
r-\overline r=0,\quad t+\overline t=0.
\tag{888.6}
$$
Here the rational and trace-zero lines have zero intersection, since $2$ is invertible. Therefore, on the $p$-primary subgroup,
$$
H^{-1}L=C_-\times C_+,\qquad
H^{-1}L'=C_+\times C_-.
\tag{888.7}
$$
The equalities extend to the finite flat closures by saturation. In (888.7), $H^{-1}$ means the inverse of its isomorphism on $E_0[p]^2$; the full scheme-theoretic inverse image also contains the degree-four kernel of $H$.

It follows that $H$ descends to
$$
\overline H:E_-\times E_+\longrightarrow\mathscr B_L
$$
and gives the exact commutative diagram
$$
\pi_L\circ H
=\overline H\circ(\pi_-\times\pi_+).
\tag{888.8}
$$
Both vertical quotient degrees are $p^2$, so $\deg\overline H=4$. This is an isogeny of abelian schemes over $R'$, finite etale because $4$ is invertible.

Its differential before quotienting is the actual matrix
$$
H^*\begin{pmatrix}dz_1\\dz_2\end{pmatrix}
=
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\begin{pmatrix}dz\\dt\end{pmatrix}.
\tag{888.9}
$$
The determinant is $-2$, a $p$-unit. This formula does not replace either individual cyclic-quotient differential factor by one.

## 3. Line bundles, fixed sigma sign, and $p$-saturated pullback

The theorem of the square gives
$$
H^*\bigl(O(6pO)\boxtimes O(6pO)\bigr)
\simeq O(12pO)\boxtimes O(12pO).
\tag{888.10}
$$
We fix this isomorphism by the actual original sigma addition identity
$$
\frac{\sigma(z+t)\sigma(z-t)}
     {\sigma(z)^2\sigma(t)^2}
=x(t)-x(z).
\tag{888.11}
$$
The sign is determined, for example, by $t\to0$: both sides have leading term $t^{-2}$. If $\delta=x(z)-x(t)$, raising (888.11) to the power $6p$ gives
$$
\sigma(z+t)^{6p}\sigma(z-t)^{6p}
=\delta^{6p}\sigma(z)^{12p}\sigma(t)^{12p}.
\tag{888.12}
$$
There is no remaining negative sign, since $6p$ is even.

This normalization is algebraic and integral. The divisor of $\delta$ is
$$
\operatorname{div}(\delta)
=\Delta_++\Delta_--2(O\times E_0)-2(E_0\times O),
$$
where $\Delta_\pm$ are $z=\pm t$. Thus multiplication by $\delta^{6p}$ gives the required isomorphism of line bundles. Its divisor has no vertical component, and (888.11) fixes its constant in the original local parameters. No independent Gaussian change or nonunit scalar is inserted.

Let $\mathscr M_\pm^{(6)}$ be the degree-six line bundle obtained by descending $O(6pO)$ through $\pi_\pm$, using the original odd symmetric theta lift on $C_\pm$. Put
$$
\mathscr M_\pm^{(12)}=
\bigl(\mathscr M_\pm^{(6)}\bigr)^{\otimes2}.
\tag{888.13}
$$
The symmetric theta construction is functorial under pullback and tensor product: its formula $g\iota(g)^{-1}$ is preserved by both operations. Consequently the descent data in (888.8)--(888.12) agree, giving an integral isomorphism
$$
\boxed{
\overline H^*\mathscr M_L
\simeq\mathscr M_-^{(12)}\boxtimes
       \mathscr M_+^{(12)}.
}
\tag{888.14}
$$
It is an isomorphism of the actual descended line bundles. It does not identify a degree-twelve theta space with a degree-six space.

Let
$$
\mathcal U_\pm^{(12)}
=H^0(E_\pm,\mathscr M_\pm^{(12)}).
$$
The pullback
$$
\overline H^*:\mathcal U_L
\longrightarrow
\mathcal U_-^{(12)}\otimes_{R'}\mathcal U_+^{(12)}
\tag{888.15}
$$
is $p$-saturated. Indeed the trace map for the finite etale degree-four isogeny, together with the projection formula, satisfies
$\operatorname{Tr}_{\overline H}\overline H^*=4$.
Thus $\frac14\operatorname{Tr}_{\overline H}$ is an integral left inverse. For every integer $m\ge0$,
$$
\boxed{
s_0\in\varpi^m\mathcal U_L
\quad\Longleftrightarrow\quad
\overline H^*s_0\in
\varpi^m(\mathcal U_-^{(12)}\otimes\mathcal U_+^{(12)}).
}
\tag{888.16}
$$
This proves equality of the full coefficient-content ideals as well as of common $p$-content.

The isogeny $\overline H$ has a nontrivial two-primary kernel. Therefore (888.14) retains its actual degree-twelve theta transport; it does not declare the original two-primary level-six basis unchanged.

## 4. Full transport of the two-flag contraction

Let $\tau_{12p}$ denote the symmetric theta lift for
$O(12pO)\boxtimes O(12pO)$ on the source of $H$.
On the $p$-primary kernel, (888.10) doubles the alternating form, precisely as required by the degree $12p$ line bundles. Functoriality gives
$$
H^*\rho_{6p}(\tau(H(r,t)))
=\rho_{12p}(\tau_{12p}(r,t))H^*.
\tag{888.17}
$$
Thus no extra unchosen theta character occurs.

For the flag $L'$, R886's coordinates are $(u,0)$, corresponding to
$(a,b)=(u/2,\overline u/2)$. Its inverse under $H$ is
$$
r=\frac{u+\overline u}{4}\in\mathbf F_p,\qquad
t=\frac{u-\overline u}{4}\in s\mathbf F_p,\qquad
u=2(r+t).
\tag{888.18}
$$
Because $\theta_h(2)=1$, the transported Gauss weight is exactly
$\theta_h(r+t)$. Define the integral mixed operators
$$
\mathcal G_h^{\mathrm{mix},\pm}
=
\sum_{\substack{r\in\mathbf F_p,\ t\in s\mathbf F_p\\
(r,t)\ne(0,0)}}
\theta_h(r+t)^{\pm1}
\,\rho_{12p}(\tau_{12p}(r,t)).
\tag{888.19}
$$
Here $r+t\ne0$ whenever $(r,t)\ne(0,0)$. These are not products of two independently weighted one-dimensional sums.

Let $\mathcal T_-\otimes\mathcal T_+$ be the unnormalized theta trace along $C_-\times C_+$ on the source of $H$. Equations (888.7), (888.17), and (888.18) give
$$
H^*\mathcal T_L
=(\mathcal T_-\otimes\mathcal T_+)H^*,
$$
$$
H^*\mathcal G_{\theta_h^{\pm1}}
=\mathcal G_h^{\mathrm{mix},\pm}H^*.
\tag{888.20}
$$
In the first flag, the original coordinate is $v=-\gamma(r+t)$ for $r\in s\mathbf F_p$, $t\in\mathbf F_p$. The full unweighted trace is merely reindexed by this bijection. The additive character and the $\gamma$-scaled commutator remain the pullback in (888.17); no independent additive-character normalization has been made.

For every actual source section $S\in\mathcal B_{R'}$, the R886 contraction therefore satisfies the exact integral identity
$$
\boxed{
(\pi_-\times\pi_+)^*
\overline H^*\mathcal C_h(S)
=
(\mathcal T_-\otimes\mathcal T_+)
\mathcal G_h^{\mathrm{mix},+}\,H^*S.
}
\tag{888.21}
$$
This formula specifies the actual same-$h$ source on the two cyclic quotients. It keeps the original mixed finite character.

Likewise, the pullback of $\Gamma_h(s_0)$ is obtained from the negative-character mixed sum in (888.19), applied to
$(\pi_-\times\pi_+)^*\overline H^*s_0$.
The exact constants of R886 remain
$$
\Gamma_h=-p\,(\text{original split vector}),\qquad
\mathcal C_h=-p(p^2-1)\ell_h,
$$
$$
\mathcal C_h\mathcal A_h\Gamma_h=p^2N_h.
\tag{888.22}
$$
Neither the degree-four isogeny nor (888.21) removes either displayed factor of $p$.

## 5. The original $F\otimes G$ source as an explicit polynomial

Write
$$
A=x(z),\quad B_0=x(t),\quad U=y(z),\quad V=y(t),\quad
\delta=A-B_0,\quad U^2=A^3-1,\quad V^2=B_0^3-1.
$$
Use $B_0$ here to avoid confusing the second elliptic coordinate with the original Cartier scalar $B$.

Define
$$
K=A^2B_0^2+4(A+B_0),
$$
$$
Y_-=U(4-B_0^3-3AB_0^2)
     +V(4-A^3-3A^2B_0).
\tag{888.23}
$$
The ordinary elliptic addition formulas give
$$
x(z+t)x(z-t)=\frac K{\delta^2},\qquad
y(z-t)=\frac{Y_-}{\delta^3}.
\tag{888.24}
$$
To verify the first identity without an unspecified normalization, put
$K_0=AB_0(A+B_0)-2$. The two $x$ numerators are
$K_0-2UV$ and $K_0+2UV$. Their product is
$$
K_0^2-4U^2V^2
=(A-B_0)^2\bigl(A^2B_0^2+4(A+B_0)\bigr).
$$
For the second identity the chord slope for $P-Q$ is
$(U+V)/(A-B_0)$. Substituting
$y(P-Q)=-U+(U+V)(A-x(P-Q))/\delta$
and using the two curve equations gives exactly $Y_-$.

Let the original sections be $F=x\sigma^6$, $G=-xy\sigma^6$.
Equations (888.11) and (888.24) give the exact original identity
$$
\boxed{
F(z+t)G(z-t)
=-K\,Y_-\,\delta\,
  \sigma(z)^{12}\sigma(t)^{12}.
}
\tag{888.25}
$$
The remaining negative sign comes from $G=-xy\sigma^6$. The even power in (888.12) supplies no further sign.

The polynomial $-K Y_-\delta$ is an actual section coefficient of
$O(12O)\boxtimes O(12O)$. For instance each monomial containing $U$ has $A$-degree at most four and $B_0$-degree at most six, so the corresponding pole orders are at most $11$ and $12$; the $V$ terms satisfy the interchanged bounds. No pole remains on the diagonal.

For the enlarged original source
$$
S_{F,G}=(x s_{6p})\otimes(-xy s_{6p}),
$$
the identical line-bundle transport is
$$
\boxed{
H^*S_{F,G}
=-K\,Y_-\,\delta^{6p-5}\,
  (s_{12p}\boxtimes s_{12p}).
}
\tag{888.26}
$$
Equivalently it is (888.25) enlarged by the explicit additional factor
$\delta^{6p-6}$ together with the indicated change of theta degree.
It is not obtained by dropping that factor modulo $p$.

The largest possible pole order in either factor in (888.26) is at most $12p$, either by (888.10) or directly from the displayed polynomial degrees. Thus (888.26) is a true integral global section, not only a formal germ or rational comparison.

Substituting this explicit polynomial into (888.21) completely specifies the original source vector $\overline H^*\mathcal C_h(S_{F,G})$ on the two actual cyclic quotients. Its content is exactly the content of $\mathcal C_h(S_{F,G})$ by (888.16).

## 6. The actual degree-three relation and a single-quotient realization

At the fixed original CM point, (888.3) induces an actual degree-three isogeny
$$
\phi_s:E_+\longrightarrow E_-,\qquad
\pi_-\circ[s]=\phi_s\circ\pi_+.
\tag{888.27}
$$
It is finite etale over $R'$. Combining it with $\overline H$ gives
$$
J=\overline H\circ(\phi_s\times1):
E_+\times E_+\longrightarrow\mathscr B_L,\qquad \deg J=12.
\tag{888.28}
$$
The corresponding line bundle is
$$
J^*\mathscr M_L
\simeq \phi_s^*\mathscr M_-^{(12)}
       \boxtimes\mathscr M_+^{(12)},
\tag{888.29}
$$
of degrees $(36,12)$. The pullback is again saturated:
$\frac1{12}\operatorname{Tr}_J$ is an integral left inverse. Thus one may study the exact coefficient-content of the R886 source on the square of the one actual curve $E_+$, but in the actual degree-$(36,12)$ line bundle, not in a falsely unchanged degree-six space.

The source before quotienting is then obtained by replacing $z$ with $sz$ in (888.25)--(888.26). Its normalization is completely fixed by the original R782 identity
$$
\sigma(sz)=s\,x(z)\sigma(z)^3.
\tag{888.30}
$$
Differentiating this identity in the same flat coordinate gives
$$
x(sz)=\frac{4-x(z)^3}{3x(z)^2},\qquad
y(sz)=-\frac{y(z)(x(z)^3+8)}
                 {3s\,x(z)^3}.
\tag{888.31}
$$
Thus, if a polynomial coefficient is wanted, one substitutes (888.31) in (888.23)--(888.26) and multiplies by the exact factor
$s^{12p}x(z)^{12p}$ from $\sigma(sz)^{12p}$.
The resulting apparent denominators are canceled by this factor: the powers of $x(z)$ in their denominators are at most $(12p-10)+4+6=12p$, from $\delta^{6p-5}$, $K$, and $Y_-$, respectively. The remaining powers of $3$ and $s$ are units. The line bundle is exactly the degree $(36p,12p)$ pullback. No redefinition of sigma or period is involved.

Under this further pullback the first flag is $C_+\times C_+$ and the complementary flag is $C_-\times C_-$. In coordinates $v=sa$, $w=sb$, with $a,b\in\mathbf F_p$, the mixed character in (888.19) becomes
$$
\boxed{\theta_h(-3a+s b)^{\pm1}.}
\tag{888.32}
$$
Indeed the input of (888.19) is $r=sv=-3a$ and $t=w=sb$. Its norm is
$$
\operatorname N(-3a+s b)=9a^2+3b^2,
$$
and it is nonzero for $(a,b)\ne(0,0)$ because $-3$ is a nonsquare. Formula (888.32) remains a genuine two-variable character and is not replaced by separate masks on $a$ and $b$.

## 7. Exact relation with the original quotient frames

Choose the quotient equations and differentials exactly as in R874:
$$
E_\pm:y_\pm^2=x_\pm^3+t'_\pm x_\pm-1,\qquad
\omega_\pm=\frac{dx_\pm}{2y_\pm},\qquad
\pi_\pm^*\omega_\pm=a_\pm\omega.
\tag{888.33}
$$
The quotient reduction is the fixed Frobenius identification, not an independent rescaling. Let $\varpi^{p^2-1}=p$ as there, and use R874's actual original formal parameter $u=-x/y$. Define the residue-field elements
$$
\ell_+=\overline{u(P_1)/\varpi},\qquad
\ell_-=\overline{u([s]P_1)/\varpi}.
$$
All identities involving $\ell_\pm$ below are in that original residue field, not characteristic-zero equalities of the formal coordinates. At the CM point,
$$
\ell_-=s\ell_+,\qquad
\ell_+^{p^2-1}=1.
\tag{888.34}
$$
The second equality is R874 (874.20)--(874.21) at the actual CM value $\mathcal D=0$: the nonzero roots satisfy $Z^{p^2}-Z=0$. The separate identity $c^{p-1}=-1$ there concerns the Moore constant, not $\ell_+$. The chosen marking still determines the actual $\ell_+$; it is not changed here by a further normalization.

Since $s^{p-1}=-1$, R874 (874.10), (874.19) give
$$
\overline{\frac{a_\pm}{\varpi^{p-1}}}
=-\ell_\pm^{p-1},\qquad
\overline{\frac{t'_\pm}{\varpi^{p-1}}}
=-\frac6B\,\ell_\pm^{p-1},
$$
$$
\ell_-^{p-1}=-\ell_+^{p-1}.
\tag{888.35}
$$
All displayed quotients are the same nonzero units in the original residue field as in R874. If
$\phi_s^*\omega_-=c_s\omega_+$, equation (888.27) gives the exact relation
$$
\boxed{c_s=s\,a_-/a_+,\qquad \overline{c_s}=-s.}
\tag{888.36}
$$
This also checks the Frobenius orientation: $s^p=-s$.

These are statements at the specified CM fiber. They do not say that $t'_-$ and $t'_+$ are negatives as functions on the full deformation branch. Any use of derivatives along that branch must still use the actual R874 Kodaira--Spencer formula
$$
a_L^2 b(t)\,dt=p\,b(t'_L)\,dt'_L.
\tag{888.37}
$$
In particular neither the factor $a_L^2/p$ nor its distinct source and quotient scales is removed by (888.35).

## 8. What the source comparison now reduces to

The remaining arithmetic vector in R886 is no longer specified only by a generic representation. Its pullback is the concrete same-$h$ mixed theta contraction (888.21), applied to the explicit original polynomial section (888.26). The degree-four and degree-twelve pullbacks preserve its entire coefficient-content ideal. Both actual cyclic quotient coordinates and their differential scales are fixed in §7.

What is still not proved is the required comparison of this vector, after the $p$ divisions in (888.22) and the original fifth lift, with
$$
f_i g_{N-1-i},\qquad h=6i+7.
$$
The original Legendre norm remains the separate factor in (888.22), and the primitive character remains the same $\theta_h$ in every mixed sum. The high factor $\delta^{6p-6}$ and the original sigma coefficient functionals have not been discarded. R884's denominator boundary therefore remains operative.

In particular this result proves no new universal $p$-unit assertion for the critical coefficients or the actual modular-quotient normal map. It supplies a saturated, explicitly marked transport of the genuine source to actual cyclic-$p$ quotients, on which that specific comparison can be made.

## Dependencies

- [R886](R886-original-two-flag-theta-descent-and-split-contraction.md): actual flags, descended multiplicity space, $\Gamma_h$, $\mathcal C_h$, and the original finite norm.
- [R881](R881-original-integral-theta-lift-and-cuspidal-test-vector.md): original symplectic coordinates and character convention.
- [R874](R874-original-cyclic-p-quotient-scales-and-Kodaira-Spencer-leading-term.md), (874.3), (874.10), (874.19)--(874.25): actual quotient frames, CM torsion residues, and Kodaira--Spencer scale.
- [R782](R782-original-sigma-six-Hirota-square-addition-kernel.md), (782.1), (782.14), (782.21): original sigma and CM normalization; no new sixth-order recurrence is asserted here.
- [R884](R884-original-enlarged-theta-lattice-coefficient-pole.md): original coefficient functionals on the enlarged lattice.
- [Moonen et al., Duality](https://www.math.ru.nl/personal/bmoonen/BookAV/DualAV2.pdf), Proposition 7.2, and [Theta groups](https://www.math.ru.nl/personal/bmoonen/BookAV/ThetaGr.pdf), Theorem 8.10: compatibility of the actual descent data.

All calculations above are displayed paper identities. No new mathematical computation or prime scan was executed.
