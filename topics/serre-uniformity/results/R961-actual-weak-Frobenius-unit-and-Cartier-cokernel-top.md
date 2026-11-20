# R961 — The actual weak weight-four Frobenius coefficient detects the Cartier-cokernel top

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / literature_frontier.

**Status: proved.** For the original $r=2$ row, this result identifies a concrete low-weight divided-Frobenius coefficient with the original Cartier-cokernel functional evaluated on a particular weak-form construction. The coefficient is a unit, with an explicit normalization. The construction detects the top of R955's possible Cartier chain, not its bottom $F$. Thus it gives an actual comparison and also specifies why the unit by itself does not prove the original high diagonal nonzero.

There is no new numerical computation. All modular forms, the full-six coordinate $Q$, the original determinant transport and the corrected signs of R939/R958 are retained.

## 1. An original weak companion and its integral low-weight realization

Assume
$$
p\ge41,\qquad p\equiv11\pmod{12},\qquad p=6N+5,
\qquad r=2,\quad k=p-1.
\tag{961.1}
$$
As before, impose $p\equiv2,5\pmod9$ for the original Serre application. Put
$$
v=V_4^\dagger,\qquad F=V_{p-1}^\dagger,\qquad
g=\frac{E_4^2}{v}.
\tag{961.2}
$$
The identities of R939 give, in the original family,
$$
v=12sD,\quad E_4=-144uD,\quad
u=\frac{E_4}{4sv},\quad t=u^3,\quad D=1-4t.
$$
Consequently
$$
\boxed{\quad
g=-48u^2v=-576s\,u^2D.
\quad}
\tag{961.3}
$$
This is a weight-four weak cusp form on the actual $H_6$ quotient. It has no interior poles. Indeed the only zeros of $v$ are the original cusp and the three order-three points, and at those elliptic points $E_4^2$ has at least the zero required to cancel the denominator. At the unique coarse cusp the original Fourier expansions give
$$
v(Q)=Q+O(Q^4),\qquad E_4(Q^6)=1+O(Q^6),
$$
so
$$
g(Q)=Q^{-1}+O(Q^2).
\tag{961.4}
$$
There is no constant term. Both forms have integral coefficients at every prime $p>3$. The actual geometric deck characters are
$$
\delta v=\zeta v,\qquad \delta g=\zeta^2g.
\tag{961.5}
$$
The second follows from the invariance of $E_4$ and the already fixed character of $v$; it is not assigned from a Fourier congruence class.

For clarity about the later crystalline statement, let $\mathcal O=W(\kappa)$, with $\kappa$ a perfect field containing the original marking. Work on the integral fine full-six curve and then take the actual tame invariants. The parabolic de Rham realization of weight four is free of rank two, with the exact Hodge sequence
$$
0\longrightarrow\mathcal O[v]\longrightarrow M
\longrightarrow\mathcal O[v]^\vee\longrightarrow0.
\tag{961.6}
$$
Here $M$ is the image of compactly supported logarithmic de Rham cohomology in logarithmic de Rham cohomology for $\operatorname{Sym}^2\mathscr H$. It is not R956's different Bol-cokernel module.

The weak form $g$ defines an integral class in $M$. Its sole coarse cusp pole has exponent $-1$, a unit for the weight-four weak-exact condition: its principal part has an integral third primitive. The class has a unit image in the last term of (961.6). To check this, use the original scalar operator $\Theta_{\tau'}=\Theta_Q/6$ and the weight-four BGG factor $1/2$. A formal primitive of the positive leading term $v(Q)=Q+\cdots$ has bottom coefficient $2\cdot6^3Q+\cdots$. Its pairing with the leading term $g(Q)=Q^{-1}+\cdots$, followed by $K=6\,dQ/Q$, has residue of absolute value $2\cdot6^4$, a unit. Its sign is the common chosen order of the two degree-one classes. On the fine cover all twelve cusp residues are present; division by the unit degree twelve gives the same assertion on $H_6$. No unknown source factor enters this test. Thus
$$
\boxed{\quad M=\mathcal O[v]\oplus\mathcal O[g].\quad}
\tag{961.7}
$$
One can equivalently obtain (961.6–7) from the actual integral BGG complex and its Laurent-series Čech model: solving the intermediate Hodge pieces uses only $2$, and the negative exponent $-1$ introduces no $p$ denominator.

A primary reference for this precise weak-exact realization is Matija Kazalicki and Anthony J. Scholl, *Modular forms, de Rham cohomology and congruences* (2013), §4, equations (4.2–4.3), and Theorem 5.3:
https://arxiv.org/pdf/1301.5876 .
Its integral input here is applied on the fine curve before the unit tame averaging, not directly to a coarse curve with elliptic stabilizers.

## 2. A normalized weak high-weight section and its Cartier output

Use the unchanged original data
$$
\mathcal A=uD^{N+1}H(t),\qquad
\mathcal B=-D^{N+1}\beta(t),\qquad
F(E_u,\rho)=-D^{N+1}C(t).
\tag{961.8}
$$
In this result $C(t)$ remains the original companion polynomial; it is not a cusp divisor or a concomitant.

R958's complete opposite-deck operator extends to weak forms regular in the interior:
$$
\mathscr D_2\bigl(u^2D^{N+1}K(t)\bigr)
=D^{N+2}\mathcal L_-K,
$$
$$
\mathcal L_-(t^j)
=(3j+1)(3j+2)t^j-(6j+7)^2t^{j+1}.
\tag{961.9}
$$
Allow $\deg K\le N$ instead of $\deg K\le N-1$. This allows one simple pole at the coarse cusp and no other pole. Let $H_N$ be the leading coefficient of $H$ and define the actual weak section $H_{\mathrm{wk}}^-$ by
$$
\boxed{\quad
H_{\mathrm{wk}}^-(E_u,\rho)
=u^2D^{N+1}\,(4sH_Nt^N).
\quad}
\tag{961.10}
$$
Since $6N+5=p$, reduction of (961.9) at $j=N$ gives
$$
\mathcal L_-(t^N)=\frac34t^N-4t^{N+1}.
\tag{961.11}
$$
Also (961.3) and (961.8) give
$$
\mathcal Ag=-576s\,tD^{N+2}H(t).
$$
It follows that the degree-$N+1$ terms cancel in
$$
Y_0:=\mathcal Ag-36\mathscr D_2H_{\mathrm{wk}}^-.
\tag{961.12}
$$
Explicitly,
$$
Y_0(E_u,\rho)=D^{N+2}R_0(t),
$$
$$
R_0(t)
=-576s\,t\bigl(H(t)-H_Nt^N\bigr)-108sH_Nt^N,
\qquad \deg R_0\le N.
\tag{961.13}
$$
Consequently $Y_0$ is cuspidal, of weight $p+3$, and has the original $\delta=\zeta^2$ character. There is no constant-term issue: a form with this nontrivial deck character has no cusp constant.

Equivalently, the simple cusp pole cancels because
$$
H_{\mathrm{wk}}^-(Q)=Q^{-1}+O(Q^2).
\tag{961.14}
$$
This normalization can be verified without extracting a long expansion. The leading coefficient of $\mathcal Ag$ is $1$. The Fourier action of $36\mathscr D_2$ is $\Theta_Q^2$, which acts as $1$ on $Q^{-1}$. The pole cancellation already proved in (961.11–13) therefore forces precisely (961.14).

Extend the actual R952 operator $\mathscr U$ to this weak section by its identical root formula. It is regular on the interior. Its Fourier rule removes the pole in (961.14), because $-1$ is not divisible by $p$, and introduces no cusp constant. Hence
$$
F_0:=\mathscr U H_{\mathrm{wk}}^-\in S_{p-1}(H_6),
\qquad \delta F_0=\zeta F_0.
\tag{961.15}
$$
This is an actual high-weight cusp form in the original space, not an abstract vector representing a quotient.

For completeness, R952's extension here is justified by the same argument as for holomorphic sources. Its polynomial formula is regular away from cusps, and its weight is divisible by $p$; the rational root is forced by the full Fourier identity. In the normal local rings, regularity of its $p$th power implies regularity of the root. The displayed Fourier series then supplies regularity at every cusp. The original coefficient roots and tame return are retained.

## 3. The exact relation with R956's interpolation

The whole-Hasse-divisor formula in R952, now for $H_{\mathrm{wk}}^-$, is
$$
(\mathscr D_2H_{\mathrm{wk}}^-)|_\Sigma
=
2\,\frac{F_0^p}{\mathcal B^{p-3}}\Big|_\Sigma.
\tag{961.16}
$$
Thus (961.12) gives
$$
Y_0|_\Sigma=-72\,\frac{F_0^p}{\mathcal B^{p-3}}\Big|_\Sigma.
$$
For any high source $T\in S_{p-1}^+$, let $Y_T$ be the unique actual negative-deck cuspidal interpolation
$$
Y_T|_\Sigma=
2\,\frac{T^p}{\mathcal B^{p-3}}\Big|_\Sigma.
\tag{961.17}
$$
Existence and uniqueness are exactly the proof of R956 §7: the full Hasse evaluation sequence is surjective, and its kernel $\mathcal AS_4$ has only the positive deck character. Therefore
$$
\boxed{\quad Y_0=-36Y_{F_0}.\quad}
\tag{961.18}
$$

R956's Cartier edge continues to apply to weak inputs; the input $\mathcal Ag$ has one simple cusp pole, whose exponent is removed by Cartier. Its Fourier rule gives
$$
\mathscr K_2(\mathcal Ag)=\mathscr U_{\mathrm{low}}g
=g_p^{1/p}v,\qquad g_p=[Q^p]g.
\tag{961.19}
$$
The image is a cusp form of weight four, hence a multiple of $v$. The coefficient of $Q$ fixes the displayed multiple. As before,
$\mathscr K_2\mathscr D_2H_{\mathrm{wk}}^-=0$: at all indices divisible by $p$, the Fourier multiplier $n^2/36$ is zero, including for weak expansions. Equations (961.12), (961.18), and (961.19) prove
$$
\boxed{\quad
\mathscr K_2Y_{F_0}
=-\frac{g_p^{1/p}}{36}\,v.
\quad}
\tag{961.20}
$$
This identifies exactly which original high source is detected by this low weak-form coefficient. It is $F_0$ from (961.15), not the named bottom vector $F$.

## 4. The complete residue normalization and a unit formula for $g_p$

The weak source makes the previously absent cusp term in R951's concomitant explicit. Set
$$
\mathscr C_2(H_{\mathrm{wk}}^-,F)
=(\partial H_{\mathrm{wk}}^-)F
-H_{\mathrm{wk}}^-\partial F.
$$
Both source weights are $p-1=-1$ in the residue field. At the original cusp, using (961.14), $F(Q)=Q+\cdots$, and
$\partial_{p-1}=\Theta_Q/6+E_2/12$, the constant term is
$$
\left(-\frac16+\frac1{12}\right)
-\left(\frac16+\frac1{12}\right)
=-\frac13.
\tag{961.21}
$$
Since $\mathcal A(Q)=1$ and $K=6\,dQ/Q$, the residue of
$\operatorname{KS}(\mathscr C_2/\mathcal A^2)$ is $-2$ at the coarse cusp.

The original full-six fine cover has twelve cusps above that width-six cusp, each with ramification index one. Thus the complete fine cusp-residue sum is $-24$. The proof of R951(951.14–15), without discarding this cusp term, gives
$$
\sum_{P\in\Sigma}
\frac{(\mathscr D_2H_{\mathrm{wk}}^-)_PF_P
-(H_{\mathrm{wk}}^-)_P(\mathscr D_2F)_P}{b_P^2}
=24.
$$
The second summand vanishes because $\mathscr D_2F=\mathcal Av/36$. Hence
$$
\boxed{\quad
\sum_{P\in\Sigma}
\frac{(\mathscr D_2H_{\mathrm{wk}}^-)_PF_P}{b_P^2}
=24,\qquad
\mathcal H_k(F,F_0)=12.
\quad}
\tag{961.22}
$$
The second equality follows from (961.16). All supersingular points are included; their fine elliptic zeros are treated exactly as in R958. The factor twelve here is the proved fine cusp-cover degree, not R932's different source degree $d_1$.

Now apply R956(956.33) to the actual cuspidal $Y_0$. By (961.12) its supersingular values are $-36\mathscr D_2H_{\mathrm{wk}}^-$. Therefore
$$
\langle z_v,\mathscr K_2Y_0\rangle_X^p
=36(-36)\cdot24=-31104.
$$
Use (961.19) and R950's exact low pairing:
$$
\langle z_v,v\rangle_X^p
=-\frac13\mathcal H_4(v,v).
$$
We obtain the calibrated identities
$$
\boxed{\quad
g_p\,\langle z_v,v\rangle_X^p=-31104,
\qquad
g_p\,\mathcal H_4(v,v)=93312=12\cdot6^5.
\quad}
\tag{961.23}
$$
Both constants are units for $p\ge41$. In particular
$$
\boxed{\quad [Q^p](E_4^2/V_4^\dagger)\ne0.\quad}
\tag{961.24}
$$
This unit statement is proved in the original objects by the residue calculation; it is not inferred from a finite scan or a finite-field positivity principle. It is compatible with R950 and in fact calibrates its nonzero low diagonal.

## 5. Which actual crystalline matrix entry this is

The weak coefficient also has a genuine low-weight crystalline interpretation. This paragraph concerns the rank-two module $M$ in (961.6), with the same fine tame descent, and not a putative height-two quotient of the original Igusa Jacobian.

Let $\varphi$ be crystalline Frobenius, semilinear for Witt Frobenius $\sigma$. This is the $\sigma$-semilinear realization of the original marked crystal: its tame Frobenius and the already fixed determinant return are the original ones, and are incorporated before the source and target are expressed in (961.7). It makes no identification of the two distinct markings exchanged by an ordinary $T_5$ arrow. Naturality makes this crystalline operator commute with the actual geometric deck action. Since $\sigma(\zeta)=\zeta^p=\zeta^2$, it interchanges the two lines (961.5). Integral filtered comparison in the range $3<p-1$ gives $\varphi[v]\in p^3M$. Thus there are integral coefficients $a_p,b_p$ with
$$
\varphi[v]=p^3a_p[g],\qquad
\varphi[g]=b_p[v].
\tag{961.25}
$$
Both coefficients are units. For example, the alternating cohomological pairing is unimodular in the basis (961.7), and Frobenius multiplies it by $p^3$ together with coefficient Frobenius. Its determinant then has valuation three. In (961.25) this forces $a_p,b_p$ to have valuation zero. Equivalently one may use strong divisibility of the rank-two filtered module. Neither argument applies to the different complete Igusa eigenspace merely because it has a one-dimensional Hodge summand.

The exact Fourier identification is stronger than a unit test. Kazalicki–Scholl §6, equation (6.1), gives at the original cusp
$$
\operatorname{loc}(\varphi f)
=p^3\sum_n\sigma(f_n)Q^{pn}
$$
in the local third-derivative quotient. Here their cusp parameter is precisely $Q$, since the full-six parameter satisfies $q=Q^6$; their correcting root $\gamma_z$ is $1$.

Their §6 states the local formula for the $\sigma$-linear operator over an unramified coefficient ring, not only the $\mathbf Z_p$-linear special case. The strengthened integral localization of §2 is constructed from the same integral weak-exact quotient and local derivative lattices. It therefore remains the identical diagram after this finite unramified base change. All the marked data here are defined over such a ring; further perfect residue-field extension preserves the equality. In the present range their exponent is $\langle3\rangle=\inf_{j\ge3}v_p(p^j/j!)=3$: the value at $j=3$ is $3$, and Legendre's bound on $v_p(j!)$ makes every other value at least $3$.

This strengthened localization, applied to $S_4+p^3M$, permits division of the relation
$\varphi[v]=p^3a_p[g]$ by $p^3$: the resulting local difference belongs to
$\Theta_{\tau'}^3\mathcal O((Q))$. Taking the coefficient of $Q^p$ gives
$$
\boxed{\quad
a_pg_p\equiv1\pmod{p^3}.
\quad}
\tag{961.26}
$$
Indeed $[Q]v=1$, while a third derivative multiplies the coefficient at $Q^p$ by $(p/6)^3$. This is the actual divided-Frobenius coefficient of the original weak basis, with the coefficient Frobenius and cusp width retained.

For the integral filtered comparison one may use J. Tilouine, *Companion forms and classicality in the GL2(Q)-case* (17 September 2009), §4.1, pp. 19–20:
https://www.math.ucla.edu/~hida/conference_10/vasudev_0908.pdf .
Only its integral comparison and divided-Frobenius assertion in the small-weight range are used; its subsequent ordinary hypothesis is not applied.

Combining (961.23) and the reduction of (961.26) identifies the mod-$p$ value of this genuine matrix entry as
$$
\overline a_p
=\frac{\mathcal H_4(v,v)}{93312}.
\tag{961.27}
$$
There is no assertion that $\overline a_p$ equals R956's different scalar $\alpha$.

## 6. The exact top-versus-bottom distinction

R953 gives the named original high class $v_{\mathrm{high}}$ and
$$
\langle v_{\mathrm{high}},T\rangle_X^p
=-6\,\mathcal H_k(F,T)
\qquad(T\in S_{p-1}).
$$
Consequently (961.22) gives
$$
\boxed{\quad
\langle v_{\mathrm{high}},F_0\rangle_X^p=-72\ne0.
\quad}
\tag{961.28}
$$
After the original nonzero descent factors, the original functional $\lambda_h$ therefore detects $F_0$. This is precisely the nonzero Cartier-cokernel direction. Since $\lambda_h$ annihilates Cartier images, $F_0$ cannot belong to that image. On the actual CM nilpotent primary part its image is a nonzero generator of the one-dimensional cokernel of R955's chain.

The named form $F$, however, generates the kernel of that chain. If the chain has length at least three, this bottom lies in the Cartier image whereas its top does not. Equations (961.20), (961.23), and (961.28) are fully compatible with that possibility. To deduce the original diagonal nonzero, one must still prove that the named bottom has a nonzero class in this same cokernel, equivalently that the chain has length one.

Thus the low crystalline unit does have an actual source-preserving comparison here, but it is a comparison with $F_0$. Replacing $F_0$ by $F$ would insert exactly the remaining assertion. R956's unique interpolation $Y_F$, R958's single moment, and R955's first opposite-deck Cartier preimage retain that unresolved content.

## Dependencies and scope

The proof uses the original integral divisors and marking in R918/R920; the corrected original family and full point counts in R936/R939; the complete concomitant and Cartier identities in R951/R952; the low class, high boundary, and same-source residue comparison in R947/R950/R953/R956; and R958's opposite-deck polynomial operator. Section 5 supplies the exact low-weight crystalline interpretation using the primary references stated there.

This result proves neither the nonvanishing of the original high diagonal nor a bound in Serre's uniformity problem. It does not substitute the Igusa quotient's integral Hodge lattice for the Scholl lattice, and changes no same-label normal-derivative conclusion.

