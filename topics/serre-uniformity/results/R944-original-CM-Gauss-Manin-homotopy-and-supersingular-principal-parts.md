# R944 — The original CM Gauss–Manin homotopy and supersingular principal parts

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / literature_frontier. **Status: proved for both original R932 rows.** This identifies a meromorphic representative of the fixed-low-weight CM de Rham class, with an explicit homotopy from the original high-weight companion and its exact R932 supersingular leading coefficient. It does **not** identify R936's trace with a crystalline norm or prove its nonvanishing.

## 1. Base curve, bundle, and Tate normalization

Work on the actual fine full-six tame modular curve $X$ in characteristic $p$, before taking the original tame quotient or extending between the original Igusa parts. Use the original marking and coefficient field $\mathbf F_{p^2}$. Write $C$ for the cusp divisor, $\mathrm{SS}$ for the complete supersingular divisor, and
$$
\mathscr H=H^1_{\mathrm{dR}}(\mathscr E/X),\qquad
\omega\subset\mathscr H
\tag{944.1}
$$
for the universal rank-two de Rham bundle and its Hodge line, with their canonical logarithmic extensions at $C$. The Gauss–Manin connection is denoted $\nabla$. Its horizontal alternating pairing is normalized by
$$
\operatorname{KS}(\rho^2)=\langle\rho,\nabla\rho\rangle=:K_\rho
\tag{944.2}
$$
for a local nowhere-zero Hodge frame $\rho$. On the Tate curve, for its canonical differential $\rho_{\mathrm{Tate}}$,
$$
K_{\rho_{\mathrm{Tate}}}=dq/q=6\,dQ/Q,
\qquad q=Q^6.
\tag{944.3}
$$
Thus the pairing sign in (944.2) is fixed by the same positive Kodaira–Spencer convention as the corrected R936. Katz, *$p$-adic properties of modular schemes and modular forms* (1973), Appendix A1.3.17 and Corollary A1.3.18, gives precisely this normalization; Appendix A2.2 gives the Tate Frobenius calculation. No sign is changed to fit the later formula.

Throughout this proof
$$
(r,k)=\begin{cases}(2,p-1)&p\equiv11\pmod{12},\\(8,p-7)&p\equiv5\pmod{12},\end{cases}
\quad p\ge41,
$$
$$
F=V_k^\dagger,\qquad V=V_{r+2}^\dagger,
\qquad G_j=\mathcal T^jF,
\qquad w_j=k+j(p+1).
\tag{944.4}
$$
These are the actual original forms, including the oldform phase $\zeta^2$. R932 supplies the full identity
$$
G_r=\mathcal A^{r+1}V,
\qquad G_{r-1}=G,\qquad w_{r-1}=rp.
\tag{944.5}
$$
The original Serre application keeps the additional condition $p\equiv2,5\pmod9$. All forms in (944.4) are cusp forms in the original fine marking.

## 2. The conjugate line and what its local frame means

There is a canonical linearized relative-Frobenius inclusion
$$
\mathsf f:F_X^*(\omega^{-1})\hookrightarrow\mathscr H.
\tag{944.6}
$$
Its image is the rank-one conjugate line. Here the map is $\mathcal O_X$-linear after the displayed Frobenius pullback; before linearization it is $p$-semilinear. It is not the crystalline Frobenius endomorphism of the global coefficient cohomology considered later.

One can construct (944.6) directly. Represent a local section of $R^1\pi_*\mathcal O_{\mathscr E}$ by a relative Čech cocycle $(u_{ij})$. Send it to the relative de Rham cocycle $(u_{ij}^p,0)$. This is well defined on classes and is $p$-semilinear in base scalars. Its representatives are closed even for the absolute differential in characteristic $p$, which proves horizontality for the Gauss–Manin connection. On every geometric fiber it is injective by the same elementary argument as R932 §2: if $(u_{ij}^p,0)$ is a coboundary, its local primitives have zero differential, hence are locally $p$th powers, and $(u_{ij})$ was already a coboundary. Consequently its image is a line subbundle, including at supersingular points. At a cusp its logarithmic extension is given by the Tate calculation in (944.3).

For a local frame $\rho$ of $\omega$, let $\rho^{-1}$ denote the dual Hodge-quotient frame in the Serre-dual identification. Define
$$
\sigma_\rho=\mathsf f(1\otimes\rho^{-1}),\qquad
A=\mathcal A/\rho^{p-1}.
\tag{944.7}
$$
This is a local nowhere-zero horizontal section, with
$$
\nabla\sigma_\rho=0,\qquad
\langle\rho,\sigma_\rho\rangle=A.
\tag{944.8}
$$
The second equality is precisely the definition of the Hasse invariant as Frobenius on $R^1\pi_*\mathcal O$: the projection of (944.6) onto the Hodge quotient is that Frobenius. The orientation is the Tate orientation in §1. In that frame $A(Q)=1$ and $\sigma_{\rho_{\mathrm{Tate}}}=\nabla_{q\partial_q}\rho_{\mathrm{Tate}}$, with pairing one. Thus this is also an independent normalization check.

The canonical object is the map (944.6) and its image line, **not** a global choice of $\sigma$. Under a frame change $\rho'=z\rho$ one has
$$
\sigma_{\rho'}=z^{-p}\sigma_\rho,\qquad
A'=z^{1-p}A,\qquad K_{\rho'}=z^2K_\rho.
\tag{944.9}
$$
In particular $\rho$ has frame weight $+1$, and $\sigma_\rho$ has frame weight $-p$. Horizontality is compatible with (944.9), since $d(z^{-p})=0$ in characteristic $p$.

At a supersingular point $P$, $A(P)=0$. Equation (944.8), the nondegeneracy of the rank-two alternating form, and the fact that $\sigma_\rho(P)\ne0$ show that the conjugate line coincides with the Hodge line at $P$. Its exact scalar there is proved in §6; it is not discarded or treated as an ordinary splitting at $P$.

## 3. The Igusa basis and the exact factor six

On the ordinary Igusa cover, write the original tautological Hasse root as $\mathfrak a=a\rho$, so
$$
a^{p-1}=A.
$$
Define
$$
e=a\rho,\qquad f=a^{-p}\sigma_\rho,\qquad
\eta=\operatorname{KS}(e^2)=a^2K_\rho.
\tag{944.10}
$$
These satisfy
$$
\langle e,f\rangle=1,\qquad
\nabla f=0,\qquad
\boxed{\nabla e=f\eta.}
\tag{944.11}
$$
Indeed $\langle e,f\rangle=a^{1-p}A=1$, and the first two equations imply that $\nabla e$ has no $e$ component. Its $f$ coefficient is $\langle e,\nabla e\rangle=\eta$, proving the last identity with its displayed sign.

Write $g_j=G_j/\rho^{w_j}$, and put
$$
h_j=g_j/a^{w_j},\qquad 0\le j\le r.
\tag{944.12}
$$
The normalized Katz operator of R932 is $\mathcal T_w=6(\mathcal A\partial_w+w\mathcal B)$. The Leibniz rule, $\partial_1a=-a\mathcal B/\mathcal A$ in scalar notation, and $a^{p-1}=A$ therefore give
$$
\boxed{dh_j=h_{j+1}\eta/6\qquad(0\le j<r).}
\tag{944.13}
$$
For clarity, division by $a^{w_j}$ first gives
$\partial_0h_j=g_{j+1}/(6a^{w_j+p-1})$; multiplying by $K_\rho$ and using $\eta=a^2K_\rho$ gives (944.13). It also follows at the original Tate cusp from $\mathcal T_w(Q)=\Theta_Q$ and (944.3), for any of the original constant choices of the Hasse root there. No new Igusa normalization has been imposed.

Let $v=V/\rho^{r+2}$. Equation (944.5) gives
$$
h_r=v/a^{r+2}.
\tag{944.14}
$$

## 4. The explicit homotopy and its descent

Define a section of $\operatorname{Sym}^r\mathscr H$ on the ordinary locus by
$$
Z=\sum_{j=0}^{r-1}
(-6)^j\frac{r!}{(r-j)!}\,
h_{r-1-j}e^{r-j}f^j.
\tag{944.15}
$$
This is ordinary symmetric multiplication, not a divided-power convention. Every factorial in (944.15) is a $p$-unit.

Using (944.11–13), differentiate the $j$th summand. Its two contributions, before its outside scalar, are
$$
\left(\frac16 h_{r-j}e^{r-j}f^j
 +(r-j)h_{r-1-j}e^{r-j-1}f^{j+1}\right)\eta.
$$
The second contribution for $j$ cancels the first for $j+1$, because their outside coefficients satisfy $c_{j+1}=-6(r-j)c_j$. The two surviving ends give, since $r$ is even,
$$
\nabla Z=\frac16 h_re^r\eta-6^{r-1}r!h_0f^r\eta.
\tag{944.16}
$$

This expression descends from Igusa to the actual fine tame base. In fact the total power of $a$ in every summand of (944.15) is
$$
-w_{r-1-j}+(r-j)-pj=-r(p-1).
$$
Thus the exact descended formula is
$$
\boxed{
Z=A^{-r}\sum_{j=0}^{r-1}
(-6)^j\frac{r!}{(r-j)!}\,
g_{r-1-j}\rho^{r-j}\sigma_\rho^j.
}
\tag{944.17}
$$
The frame-change rules (944.9), together with the stated $w_j$, verify term by term that (944.17) is independent of $\rho$.

Define the following vector-valued differentials on that same base:
$$
\Omega_V=v\rho^rK_\rho,
\qquad
\Psi_F=\frac{(F/\rho^k)\sigma_\rho^r}{A^{r+1}}K_\rho.
\tag{944.18}
$$
Again each expression is frame independent. Indeed the total frame exponent in the second is $-k-pr+(r+1)(p-1)+2=0$. Equations (944.14), (944.16) now prove
$$
\boxed{\Omega_V=6\nabla Z+6^r r!\,\Psi_F.}
\tag{944.19}
$$
This gives the fixed-low-weight form $V$ a representative involving **precisely** the original $F$. The remaining derivative after the $r-1$ terms in (944.15) becomes the $f^r$ coefficient in (944.16). This is why this explicit identity uses the original $\Theta_Q^rF=V$ without incorrectly replacing it by a scalar Bol operator of order $r+1$.

The identity is established on the original fine base, before any quotient or norm-character extension. Its passage from Igusa to that base only cancels the displayed $a$ exponents. It does not identify the two original Igusa parts, erase a determinant character, or replace the original fine degree by a small tame degree.

## 5. A precise global de Rham interpretation

The form $\Omega_V$ is the usual holomorphic, parabolic de Rham representative of the named weight-$r+2$ cusp form with coefficients in $\operatorname{Sym}^r\mathscr H$. All coefficients in the numerator of (944.17) are regular. Since the Hasse divisor on the fine tame base is reduced,
$$
\operatorname{pole}_{\mathrm{SS}}Z\le r,
\qquad \operatorname{pole}_{\mathrm{SS}}\Psi_F\le r+1<p.
\tag{944.20}
$$
At every cusp $A$ is a unit and all $G_j,F,V$ are cuspidal, so the displayed sections and differentials have the required regular or parabolic logarithmic behavior there. In particular the construction introduces no new cusp principal part.

There is no need to assume a general comparison theorem identifying arbitrary meromorphic forms with de Rham cohomology in characteristic $p$. The present regularization is explicit. Cover $X$ by $X\setminus\mathrm{SS}$ and neighborhoods of the supersingular points. On the first open set take $\Psi_F$, on a supersingular neighborhood take $\Omega_V/(6^r r!)$, and on each overlap use the correction $Z/(6^{r-1}r!)$. They satisfy
$$
\frac{\Omega_V}{6^r r!}-\Psi_F
=\nabla\left(\frac{Z}{6^{r-1}r!}\right).
\tag{944.21}
$$
This is a concrete Čech–de Rham cocycle, cohomologous to the global holomorphic representative $\Omega_V/(6^r r!)$. Hence the regularized class specified by (944.21) obeys
$$
\boxed{[\Omega_V]=6^r r!\,[\Psi_F]_{Z}.}
\tag{944.22}
$$
The subscript records this actual correction. It does not silently assign a cohomology class to an unspecified meromorphic differential.

## 6. Its leading principal part is the original R932 coefficient

Fix **any** supersingular point $P$ on the fine tame base, using the same local frame $\rho$ as R932. Put
$$
B=\mathcal B/\rho^{p+1},\qquad b_P=B(P),\qquad
F_P=(F/\rho^k)(P).
$$
At $P$ write $\sigma_\rho(P)=q_P\rho(P)$. Differentiating (944.8) and using $\nabla\sigma_\rho=0$ gives
$$
dA(P)=\langle\nabla\rho,\sigma_\rho\rangle(P)
=-q_PK_\rho(P).
$$
By the defining Serre derivative, $dA(P)=b_PK_\rho(P)$: its connection term is multiplied by $A(P)=0$. Thus
$$
\boxed{\sigma_\rho(P)=-b_P\rho(P).}
\tag{944.23}
$$
The minus sign follows from the alternating rank-two pairing and the fixed positive KS convention.

For $0\le n\le r-1$, evaluating the actual Katz iterates at $P$ gives
$$
g_n(P)=6^n(-1)^n\frac{(r-1)!}{(r-1-n)!}\,b_P^nF_P.
\tag{944.24}
$$
Substitute (944.23–24) into (944.17). The coefficient of $b_P^{r-1}F_P\rho(P)^r$ is
$$
6^{r-1}(r-1)!
\sum_{j=0}^{r-1}(-1)^{r-1-j}\binom rj
=6^{r-1}(r-1)!,
$$
because the sum including $j=r$ is zero and its last summand is $-1$. Therefore
$$
\boxed{
(A^rZ)(P)=6^{r-1}(r-1)!b_P^{r-1}F_P\rho(P)^r
=-g_P\rho(P)^r,
}
\tag{944.25}
$$
where
$$
g_P=-6^{r-1}(r-1)!b_P^{r-1}F_P
$$
is exactly R932(932.31), with its original sign. In the local parameter $A$ the top polar term of $Z$ is consequently $-g_P\rho(P)^r/A^r$. Every lower term remains specified by (944.17); none has been dropped.

This applies at every fine supersingular point. At the already proved elliptic marked zeros, $F_P=0$ and the displayed highest coefficient is zero. The statement does not remove those points from the construction or infer that a zero leading coefficient eliminates every lower local term.

## 7. Symmetric-power pairing, factorials, and Frobenius limits

For future cup products, fix the normalized pairing on $\operatorname{Sym}^r\mathscr H$ by
$$
\langle x_1\cdots x_r,y_1\cdots y_r\rangle_r
=\frac1{r!}\sum_{\pi\in S_r}\prod_{i=1}^r\langle x_i,y_{\pi(i)}\rangle.
\tag{944.26}
$$
Thus $\langle\rho^r,\sigma_\rho^r\rangle_r=A^r$. In the ordinary basis $e,f$,
$$
\langle e^{r-j}f^j,e^jf^{r-j}\rangle_r
=\frac{(-1)^j}{\binom rj},
$$
and all other pairings of complementary monomials vanish unless the indices sum to $r$. Since $r$ is even, this bundle pairing is symmetric and the induced degree-one cohomology cup pairing is alternating. Omitting $1/r!$ would multiply that pairing by $r!$; the factor $6^r r!$ in (944.19) instead comes from the explicit connection calculation and is not a pairing convention.

Only the relative, $p$-semilinear conjugate-line map (944.6) has been used. No equality has been asserted between that map and a divided crystalline Frobenius on the fixed CM summand of global parabolic cohomology. In particular this proof does not prove that
$T=\operatorname{Tr}_{L/\mathbf F_{p^2}}((3-2e_0)R_{\mathrm{poly}})$
is a nonzero cup product. An actual bridge still has to transport the original R932 inverse-Frobenius scalar class and its Serre pairing to the fixed coefficient cohomology, specify the integral CM lattice, compute any divided Frobenius power and all factors, and verify that its local residue formula is the complete original $g_P^{1+1/p}/b_P^r$ sum. Equations (944.17), (944.23), and (944.25) now supply exact source and principal-part data for that calculation.

## Sources

- R932(932.15–19), (932.23–25), (932.31): original Katz normalization, both CM companions, local Hasse parameter, and the original $g_P$.
- Corrected R936 and R939: original full-six phase and positive Tate/KS normalization; no change to the fine Igusa degree or unknown original source scalar.
- N. M. Katz, *$p$-adic properties of modular schemes and modular forms*, in *Modular Functions of One Variable III*, Lecture Notes in Mathematics 350 (1973), 69–190, §2.0, Appendix A1.3.17–18, and Appendix A2.2; [author PDF](https://web.math.princeton.edu/~nmk/old/padicpropMFMS.pdf). The relative Čech construction, homotopy, frame checks, and all principal-part coefficients needed here have been proved above.

All new calculations are displayed paper algebra. No new mathematical arithmetic was executed locally or elsewhere in proving this result.
