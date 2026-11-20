# R941 — The original supersingular trace as a fixed-cusp constant term

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / literature_frontier. **Status: proved symbolic identity; no nonvanishing claim.** This continues the corrected R936 and R939 without a new finite-prime calculation. It keeps the actual original CM form, original full-six cusp, phase, both labels, and all supersingular weights.

## 1. Exact statement

Use R936/R939, with $p\ge41$, $p\equiv5\pmod6$, and the original Serre restriction $p\equiv2,5\pmod9$ whenever applying this to that question. Write
$$
p=6N+5,\quad s^2=-3,\quad t=u^3,\quad D=1-4t,\quad x=1-8t,
$$
$$
L=\mathbf F_{p^2}[t]/(tH),\quad e_0=H/H(0),\quad
\beta=-xH-3tDH',
$$
$$
R_{\mathrm{poly}}=D^{2N+2}C^{p+1}\beta^{r-2},\qquad
T=\operatorname{Tr}_{L/\mathbf F_{p^2}}((3-2e_0)R_{\mathrm{poly}}).
\tag{941.1}
$$
In particular $T=R_{\mathrm{poly}}(0)+3\sum_{H(a)=0}R_{\mathrm{poly}}(a)$, with each geometric $H$ root once. Put
$$
m=(p^2-1)/12,\qquad \chi=\left(\frac{-1}{p}\right),\qquad
F=V_{k_-}^{\dagger},\qquad \mathcal B=\partial_{p-1}\mathcal A=E_{p+1}/12.
\tag{941.2}
$$
Every form below is evaluated in the original full-six variable: $F=F(Q)$, while $\Delta=\Delta(Q^6)$ and $E_2=E_2(Q^6)$. The exact constant-term identity is
$$
\boxed{
T=6\chi\operatorname{CT}_Q
\left(\frac{F(Q)^{p+1}\mathcal B(Q)^{r-1}}{\Delta(Q^6)^m}\right).
}
\tag{941.3}
$$
For the $r=2$ row, $p\equiv11\pmod{12}$ and $\chi=-1$, this becomes
$$
\boxed{
T=\operatorname{CT}_Q
\left(\frac{F(Q)^p\Theta_QF(Q)}{\Delta(Q^6)^m}\right),\qquad
\Theta_Q=Q\frac d{dQ}.
}
\tag{941.4}
$$
The $p$th power in these expressions is the actual Frobenius power. In particular, if it is rewritten as a series in $Q^p$, its coefficients, including the oldform phase $\zeta^2$, must also be raised to $p$; it must not be replaced by $F(Q^p)$ with its coefficients unchanged.

Both rows admit the following stronger unified expression, proved in §5:
$$
\boxed{
T=-\frac{\chi}{6^{r-2}(r-1)!}
\operatorname{CT}_Q\left(
\frac{F(Q)^p\Theta_Q^{r-1}F(Q)}{\Delta(Q^6)^m}
\right).
}
\tag{941.4a}
$$
For $r=8$ its outside factor is $-1/(6^6\,7!)$. All these factors are units for the stipulated $p$.

## 2. A global extension of the finite-algebra function

The corrected evaluations of the original forms are
$$
F(E_u,\omega)=(-1)^J D^{J+1}C,\qquad
\mathcal B(E_u,\omega)=-D^{N+1}\beta,\qquad
\Delta(E_u,\omega)=-108D^2.
\tag{941.5}
$$
Both $p+1$ and $r-2$ are even. Therefore the signs disappear in $F^{p+1}\mathcal B^{r-2}$. Since
$$
J+1=(p+3-r)/6,\qquad N+1=(p+1)/6,
$$
its $D$ exponent before division by $\Delta^m$ is
$$
(J+1)(p+1)+(N+1)(r-2)=(p+1)^2/6.
$$
Subtracting $2m=(p^2-1)/6$ leaves $2N+2=(p+1)/3$. Consequently the literal polynomial in (941.1), now regarded on the whole coarse $\mathbf P^1_u$, equals the global modular function
$$
R_{\mathrm{poly}}
=(-108)^m\frac{F^{p+1}\mathcal B^{r-2}}{\Delta^m}
=-\chi\frac{F^{p+1}\mathcal B^{r-2}}{\Delta^m}.
\tag{941.6}
$$
The last constant is R939(939.16–17), evaluated at $t=0$: $-\chi(-108)^m=1$, equivalently $(-108)^m=-\chi$. The numerator and denominator in (941.6) have the same modular weight $p^2-1$. The equality in (941.6) holds globally as a rational function, not just modulo $tH$.

## 3. A differential whose residues have the full required weights

On $\mathbf P^1_u$ use the actual meromorphic differential
$$
\Omega=R_{\mathrm{poly}}\frac{\mathcal B}{\mathcal A}
\operatorname{KS}(\omega^2).
\tag{941.7}
$$
Here $\mathcal B/\mathcal A$ has weight two, so applying Kodaira–Spencer gives a well-defined differential independent of the chosen Hodge frame. The corrected signs are essential:
$$
\mathcal A=uD^{N+1}H,\qquad
\mathcal B=-D^{N+1}\beta,\qquad
\operatorname{KS}(\omega^2)=du/D.
$$
Using $dt=3u^2du$ gives
$$
\Omega
=-R_{\mathrm{poly}}\frac{\beta}{uDH}\,du
=R_{\mathrm{poly}}
\left(\frac{H'}H+\frac{x}{3tD}\right)dt.
\tag{941.8}
$$
This expression descends to $\mathbf P^1_t$. At a root of $H$, the residue on $\mathbf P^1_t$ is $R_{\mathrm{poly}}(a)$; the roots are simple and are neither $0$ nor $1/4$. At $t=0$ the residue is $R_{\mathrm{poly}}(0)/3$. At $t=1/4$ the second term has at most a simple pole, but $R_{\mathrm{poly}}$ contains $D^{2N+2}$, so the differential is regular there with residue zero. These statements account for every finite pole in (941.8).

Pullback along $t=u^3$ gives three points above each $H$ root, each with residue $R_{\mathrm{poly}}(a)$, and a ramified point above $t=0$ with residue $R_{\mathrm{poly}}(0)$. The elliptic $D=0$ points retain residue zero. Thus
$$
\sum_{u\ne\infty}\operatorname{Res}_u\Omega=T.
\tag{941.9}
$$
This proves the original weights directly. It does not replace weight one at $t=0$ by weight three and does not remove an elliptic branch from the point accounting.

The coarse curve has the single cusp $u=\infty$; $j=27648u^3(1-4u^3)$ has its only pole there of order six. The original $Q$ is its uniformizer since $u\sim(4s)^{-1}Q^{-1}$. In the Tate frame
$$
\mathcal A(Q)=1,\quad
\mathcal B(Q)=E_2(Q^6)/12,\quad
\operatorname{KS}=6\,dQ/Q.
$$
Therefore
$$
\operatorname{Res}_{Q=0}\Omega
=\frac12\operatorname{CT}_Q(R_{\mathrm{poly}}(Q)E_2(Q^6)).
$$
The residue theorem on $\mathbf P^1_u$ and (941.9) prove
$$
T=-\frac12\operatorname{CT}_Q(R_{\mathrm{poly}}(Q)E_2(Q^6)).
\tag{941.10}
$$
Substitution of (941.6) and $E_2(Q^6)=12\mathcal B(Q)$ proves (941.3).

## 4. Exact integration by parts for the original r=2 row

In characteristic $p$,
$$
\Theta_Q(\Delta(Q^6)^{-m})
=-6mE_2(Q^6)\Delta(Q^6)^{-m}
=6\mathcal B(Q)\Delta(Q^6)^{-m},
\tag{941.11}
$$
because $m\equiv-1/12\pmod p$. The constant term of the derivative of any Laurent series with a finite principal part is zero. Also
$$
\Theta_Q(F^{p+1})=F^p\Theta_QF
$$
in characteristic $p$. For $r=2$, equations (941.3) and (941.11) hence give
$$
T=\chi\operatorname{CT}_Q(F^{p+1}\Theta_Q\Delta^{-m})
=-\chi\operatorname{CT}_Q(F^p\Theta_QF\Delta^{-m}).
$$
Since $\chi=-1$, this is precisely (941.4). This calculation keeps $\Theta_Q=6\Theta_{\tau'}$ throughout.

## 5. The original Katz iterate removes every extra B factor

Let
$$
G=\mathcal T^{r-1}F,\qquad c_r=-6^{r-1}(r-1)!.
$$
R932 gives $\operatorname{wt}(G)=rp$ and $G(Q)=\Theta_Q^{r-1}F(Q)$. Work with the same original weight and character at every Katz step. Modulo the ideal generated by $\mathcal A$, applying the Katz operator to a weight-$w$ form multiplies it by $6w\mathcal B$. The successive weights of the $r-1$ steps are $1-r,2-r,\ldots,-1$ modulo $p$, so their product is exactly $c_r$. Consequently the globally holomorphic modular form
$$
G-c_r\mathcal B^{r-1}F
$$
is divisible by $\mathcal A$ as a modular section, not just after evaluating at some chosen supersingular point. Put
$$
U=\frac{G-c_r\mathcal B^{r-1}F}{\mathcal A},\qquad
\operatorname{wt}(U)=(r-1)p+1.
\tag{941.12}
$$
Then
$$
W=\frac{F^pU}{\Delta^m}
\tag{941.13}
$$
has weight exactly two. Its tame character is trivial: $U$ has the same original tame character as $F$, and the $(p+1)$st power of that character is trivial as in R936's descent. There are no poles in the interior, since $U$ is a holomorphic modular section and $\Delta$ vanishes only at the cusp. Thus Kodaira–Spencer turns (941.13) into a meromorphic differential on the original coarse $\mathbf P^1_u$ with a possible pole only at its single cusp. At elliptic points, the weight-two modular transformation rule is precisely the condition for this differential to descend regularly.

The residue theorem therefore gives $\operatorname{CT}_QW(Q)=0$: in the Tate frame the differential is $6W(Q)dQ/Q$, and six is a unit. Since $\mathcal A(Q)=1$, this proves
$$
\operatorname{CT}_Q\left(\frac{F^pG}{\Delta^m}\right)
=c_r\operatorname{CT}_Q\left(\frac{F^{p+1}\mathcal B^{r-1}}{\Delta^m}\right).
\tag{941.14}
$$
Combining (941.14) with (941.3), and using the exact full-six identity for $G(Q)$, proves (941.4a). This argument handles both rows and does not substitute a weight-$k_+$ form for the weight-$k_-$ source $F$.

## 6. Scope and concrete remaining gap

The identities above replace the finite supersingular trace by a single constant term of the same original CM source. They do not assert that this constant term is nonzero. Calling $F^{p+1}$ a norm supplies no positivity over the finite field. No reduction to an unrelated hypergeometric companion, a different oldform phase, or a subset of supersingular points has been made.

In either row, once $T$ is known, the original full fine sum and the original functional remain exactly
$$
S^p=12[-6^{r-1}(r-1)!]^2T,
$$
$$
\lambda_h(\Phi_{k_-}(F)_{\mathrm{full}})
=\frac{m_{\mathrm I}(c_h^{\mathrm F})^{1/p}}
{d_1\,6^r(r-1)!}S.
$$
In particular the actual $d_1$ and $c_h^{\mathrm F}$ are retained. R932's comparison with the original normal coefficient $Q'_h(0)$ is still missing. A usable next theorem would evaluate the specific constant term in (941.3) or (941.4a), or prove that this actual CM vector has nonzero value under the resulting functional; an abstract nonzero functional alone does not establish that assertion.

Dependencies: corrected R936, especially its original $C$, all-point accounting and phase; R939, especially the global scalar evaluations and the Baker constant fixed at $t=0$; R932(932.15–19) for the two original derivative normalizations. All calculations displayed here are symbolic paper algebra. No new finite-prime arithmetic has been executed.

## Related primary source

M. Kaneko and D. Zagier, *Supersingular j-invariants, hypergeometric series, and Atkin’s orthogonal polynomials*, AMS/IP Studies in Advanced Mathematics 7 (1998), 97–126, §5; [author PDF](https://www2.math.kyushu-u.ac.jp/~mkaneko/papers/17Atkin.pdf), [author bibliography](https://www2.math.kyushu-u.ac.jp/~mkaneko/papers-e.html). Their weighted constant-term description gives the classical Atkin-pairing context. The present original-source identity is proved directly above on the actual level-six curve; no equality to an abstract positive norm, or transfer of characteristic-zero positivity to the residue field, is assumed.
