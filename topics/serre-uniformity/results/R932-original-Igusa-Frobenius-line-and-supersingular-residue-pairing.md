# R932 — The original Igusa Frobenius line and its complete supersingular residue pairing

Date: 2026-11-16. Status: **proved for the two original central primitive labels below**. The additive line defining R913's actual Cartier-cokernel functional is identified, through the injective de Rham Frobenius, with the named good-model differential of R918/R920. Its value on the other named companion is then expressed as a complete supersingular residue sum in the original full-six marking. The sum has not been proved nonzero. Neither its nonzero value nor its equality to the specified low normal coefficient is assumed.

## 1. The original labels and the two different companions

Retain the original positive quotient, $c_0$ rigidification, $c_1$ centering, coefficient place, and tame transport of R913–R925. In particular,
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad n=p+1,
\qquad \zeta=(-1+\sqrt{-3})/2.
\tag{932.1}
$$
The following two cases exhaust these allowed primes:
$$
\begin{array}{c|c|c|c|c}
p\bmod12&h&r=2h-n&k_+=r+2&k_-=p+1-r\\ \hline
11&(p+3)/2&2&4&p-1\\
5&(p+9)/2&8&10&p-7.
\end{array}
\tag{932.2}
$$
Both labels are the original primitive labels of R918/R920. Indeed $h$ is odd and $h\equiv1\pmod6$. In the first row $2h-n=2$, and in the second $2h-n=8$; any common divisor of $h$ and $n$ is therefore an odd divisor of $2$ or $8$, hence is one. All weights are strictly between two and $p$. In particular $r<p-1$ and $(r-1)!$ is a unit.

Let $C_{\mathrm I}$ denote the disjoint union of the actual normalized Igusa component curves whose Jacobians give the factor $B_{\mathrm I}$ in R911–R913. Use its canonical componentwise Picard–Serre pairing. In the second row there are two original parts, with their actual $C_4$ quotient and full norm extension; they are not merged by a scalar-character argument.

R913 supplies the nonzero actual functional
$$
\lambda_h\in
\left[
(\omega_{B_{\mathrm I}})_{\chi_-,\,\delta=\zeta}
\big/
\mathcal C(\omega_{B_{\mathrm I}})_{\chi_-,\,\delta=\zeta^2}
\right]^\vee ,
\qquad
\chi_\pm=\operatorname N^{\,\pm(1-h)}.
\tag{932.3}
$$
Thus $\chi_+=\operatorname N^{1-h}$ and $\chi_-=\operatorname N^{h-1}$. The source of the actual additive line and its original integer $a_h$ are unchanged.

For $k\equiv4\pmod6$, write
$$
F_k=f_{a^{k-1}\epsilon_3(a)},\qquad
V_k^\dagger(Q)=F_k(Q)-2^k\zeta^2F_k(Q^4).
\tag{932.4}
$$
These are exactly R913(913.26), (913.31). In particular the phase is $\zeta^2$, the oldform coefficient is $2^k$, and $q=Q^6$ at the fixed full-six cusp. Below all forms are reduced at the original coefficient place. Put
$$
F=\overline V_{k_-}^{\dagger},\qquad
V=\overline V_{k_+}^{\dagger}.
\tag{932.5}
$$

Let $\mathcal A$ be the Hasse invariant with Tate expansion one and let $\mathfrak a$ be Gross's canonical Igusa section:
$$
\mathfrak a^{p-1}=\mathcal A,\qquad
\mathfrak a(Q)=1.
\tag{932.6}
$$
On a fine Igusa cover the original differential convention is
$$
\Phi_k(H)=\frac16\operatorname{KS}
\left(H/\mathfrak a^{k-2}\right),
\qquad
\Phi_k(H)=H(Q)\,dQ/Q.
\tag{932.7}
$$
The original determinant correction and full norm extensions are those already fixed in R913 §§3, 6–7. Formula (932.7) is used after those transports.

## 2. Injective de Rham Frobenius identifies the actual line

For a smooth proper connected curve $C$ over a perfect residue field, let
$$
F_{\mathrm{dR}}:H^1(C,\mathcal O_C)\longrightarrow H^1_{\mathrm{dR}}(C)
\tag{932.8}
$$
be the $p$-linear map sending a Čech cocycle $(u_{ij})$ to the de Rham class of $(u_{ij}^p,0)$. It is injective. Indeed, if $(u_{ij}^p,0)$ is a de Rham coboundary $(b_i-b_j,db_i)$, then $db_i=0$. On a smooth curve over a perfect field the local kernel of $d$ consists of $p$th powers. After refining the cover write $b_i=c_i^p$. Then $u_{ij}=c_i-c_j$, and the original class is zero. This is Oda, Definition 5.3.

The projection of (932.8) to $H^1(C,\mathcal O_C)$ is the ordinary $p$-linear Frobenius $F_{\mathcal O}$. If $F_{\mathcal O}v=0$, its injective image is therefore a nonzero holomorphic differential:
$$
v\ne0,\quad F_{\mathcal O}v=0
\quad\Longrightarrow\quad
0\ne F_{\mathrm{dR}}v\in H^0(C,\Omega^1_C).
\tag{932.9}
$$
Moreover $\mathcal C(F_{\mathrm{dR}}v)=0$, by Oda's Cartier description and Proposition 5.7. Equivalently, the exact sequence
$$
0\longrightarrow\mathcal O_C
\xrightarrow{\,b\mapsto b^p\,}F_*\mathcal O_C
\xrightarrow{\,d\,}\mathcal B^1_C\longrightarrow0
\tag{932.10}
$$
identifies the exact holomorphic differentials with $\ker F_{\mathcal O}$ after the required $p^{-1}$ scalar transport. The two directions of this transport must not be confused: (932.8) is $p$-linear, while recovering the class from an exact differential is $p^{-1}$-linear.

Apply this componentwise to $C_{\mathrm I}$. Let $v_h$ be the Serre-dual class of the actual functional $\lambda_h$. This means precisely the class specified by R913(913.8–12), using that same pairing. It is nonzero. Since $\lambda_h$ kills the Cartier image, the residue duality identity
$$
\langle F_{\mathcal O}v_h,\omega\rangle
=\langle v_h,\mathcal C\omega\rangle^p
\tag{932.11}
$$
gives $F_{\mathcal O}v_h=0$. Thus
$$
\eta_h=F_{\mathrm{dR}}v_h
\tag{932.12}
$$
is a nonzero exact holomorphic differential.

This construction fixes the character, rather than identifying two spaces because their dimensions agree. The class $v_h$ has full inertia character $\chi_+$ and geometric deck character $\zeta^2$, by the actual pairing in R913. Therefore
$$
\eta_h:\quad
\chi_+^p=\chi_+,\qquad
(\zeta^2)^p=\zeta.
\tag{932.13}
$$
The first equality uses that the full norm character has values in $\mathbf F_p^\times$; the second uses $p\equiv-1\pmod3$. This is the weight-$k_+$ space, not the weight-$k_-$ space paired with $\lambda_h$.

Only the original $T_5$ zero equation is needed for the Hecke step. R913 §7 gives $\lambda_h\circ T_5^{\rm orig}=0$ on the appropriate full source, retaining the other deck-character summand. By Serre duality the same class $v_h$ is killed by the transpose correspondence. The map (932.8) is natural for pullback and prime-to-$p$ trace; for trace one can use $\operatorname{Tr}(b^p)=\operatorname{Tr}(b)^p$ in the separable function-field extensions. Hence $\eta_h$ is killed by that same transpose correspondence. R913's actual transpose identification and full norm/diamond transport turn this into the weight-$k_+$ $T_5$ zero equation used in R920. Every inserted scalar is a power of $5$ or an original diamond/norm value and is invertible. Thus the zero equation is unchanged. This does not identify the nonzero Gross Hecke eigenvalues in the two different weights: the theta companion relation includes the factor $\ell^r$.

In the first row of (932.2), R918 identifies the whole actual weight-four character space with the line generated by $\Phi_4(V_4^\dagger)$. Hence (932.13) identifies $\eta_h$ with that line. In the second row, R920 identifies the whole actual weight-ten space on one part and proves that its original inert-$5$ Hecke-zero kernel is exactly the line generated by $\Phi_{10}(V_{10}^\dagger)$. The actual class $v_h$, and hence $\eta_h$, is killed by this correspondence. This applies R920's full Hecke-zero equation, including its other deck-character target; it does not treat $T_5$ as an endomorphism of one deck summand.

The nonsquare-norm interchange of the two Igusa parts commutes with Frobenius. Its full character is still $\chi_+$ by (932.13); restriction and extension are therefore exactly R920's original ones. We conclude in both cases that
$$
\boxed{\quad
\eta_h=c_h^{\mathrm F}\,\Phi_{k_+}(V),
\qquad c_h^{\mathrm F}\in k^\times.
\quad}
\tag{932.14}
$$
Here and below this differential is extended to all actual parts with its stated full norm character. In particular (932.14) also identifies the line with the nonzero primitive good-model layer of R916/R918/R920. It does not assign the same value to their scalar normalizations.

This is a comparison through the full de Rham map (932.8). It is not the direct identification of an additive Lie vector with a weight-$k_-$ holomorphic vector that R913 deliberately did not make.

## 3. A rational primitive in the actual six-level convention

Let $\partial_k$ be the usual Serre derivative in the original full-six variable $\tau'$:
$$
\partial_k=\Theta_{\tau'}-\frac{k}{12}E_2,
\qquad
\mathcal B=\partial_{p-1}\mathcal A.
\tag{932.15}
$$
This $\mathcal B$ is a modular form; it is not a replacement for the scalar Cartier unit denoted by $B$ in the sigma results.

The Katz operator normalized to $\Theta_Q=Q\,d/dQ=6\Theta_{\tau'}$ is
$$
\mathcal T_k(H)=6\left(\mathcal A\,\partial_kH+
k\mathcal B H\right),
\qquad
\operatorname{wt}(\mathcal T_kH)=k+p+1.
\tag{932.16}
$$
For the sign, $\mathcal A(Q)=1$ gives
$\mathcal B(Q)=E_2(Q)/12$ in characteristic $p$; the $E_2$ terms in (932.16) cancel to $6\Theta_{\tau'}H$. In particular, for $k=p-1$ the sign of the second term is minus. Each iteration below uses the new weight, not the original weight again.

Define the actual modular form
$$
G=\mathcal T^{\,r-1}F,\qquad \operatorname{wt}(G)=rp.
\tag{932.17}
$$
R913(913.29), with the unchanged oldform factor checked there, gives the complete Fourier identity $\Theta_Q^r F=V$. The two modular weights differ by $(r+1)(p-1)$, so the full-level $q$-expansion principle gives
$$
\mathcal T G=\mathcal A^{r+1}V.
\tag{932.18}
$$
Since $rp=0$ in the residue field, (932.16) now implies
$$
\boxed{\quad
\partial_{rp}G=\frac{\mathcal A^rV}{6}.
\quad}
\tag{932.19}
$$
This is an equality of sections of weight $rp+2$.

On a fine Igusa cover of one chosen original Igusa part set
$$
f=\frac{G}{\mathfrak a^{rp}}.
\tag{932.20}
$$
It is an actual rational function: numerator and denominator have the same weight. It is regular away from supersingular points, and at the cusps the Hasse root is a unit and $G$ is cuspidal. Its differential satisfies
$$
\boxed{\quad df=\Phi_{k_+}(V).\quad}
\tag{932.21}
$$
Indeed both sides have expansion $V(Q)\,dQ/Q$ at the fixed cusp, by (932.18) and (932.7); their equality follows for rational differentials. This is also Gross Proposition 5.8 in the chosen $Q$ normalization. No indefinite complex integral or extra integration constant has been introduced.

## 4. Every supersingular principal part

Work first on one fine full-six Igusa component. Let $P$ be any supersingular point, and choose a local unit section $\rho$ of the Hodge bundle on its tame base. Put
$$
T=\mathcal A/\rho^{p-1},\qquad
z=\mathfrak a/\rho,\qquad
T=z^{p-1},
\tag{932.22}
$$
and
$$
g=G/\rho^{rp},\qquad
v=V/\rho^{r+2},\qquad
b=\mathcal B/\rho^{p+1}.
\tag{932.23}
$$
The Hasse invariant has a simple zero on the fine tame base, so $T$ is a uniformizer there, $z$ is a uniformizer on the fine Igusa curve, and
$$
b_P=b(P)\ne0.
\tag{932.24}
$$
The sections and values here are in the actually transported tame frame; no scaling of the original CM differential has been dropped.

Write $\operatorname{KS}(\rho^2)=\kappa(T)\,dT$. At $T=0$,
$$
\kappa(0)=b_P^{-1}.
\tag{932.25}
$$
Indeed the scalar derivation dual to $\operatorname{KS}(\rho^2)$ sends $T$ at zero to $\mathcal B/\rho^{p+1}$; the connection term from the chosen $\rho$ is multiplied by $T$ and vanishes there.

The exponent $rp$ of $\rho$ is zero in characteristic $p$. Hence (932.19), expressed in the frame $\rho$, implies
$$
\frac{dg}{dT}
=\frac{\kappa(T)}6\,T^r v(T).
\tag{932.26}
$$
Because $1,\ldots,r$ are nonzero in the residue field,
$$
g(T)=g_P+O(T^{r+1}).
\tag{932.27}
$$
Terms with positive exponent divisible by $p$ cause no omitted negative power: $r<p-1$, and every exponent beyond $r$ contributes nonnegative order below. More precisely,
$$
(r+1)(p-1)-rp=p-r-1>0.
\tag{932.28}
$$
Using (932.20) and (932.22), we therefore obtain the complete principal part
$$
\boxed{\quad
f=g_P z^{-rp}+\text{a regular function at }P.
\quad}
\tag{932.29}
$$
There are no further supersingular negative powers. This conclusion is at every supersingular point, not only at the marked $j=0$ point.

Let
$$
u_P=g_P^{\,1/p}z^{-r}.
\tag{932.30}
$$
The $p$th root is unambiguous in the perfect residue field. Then $f-u_P^p$ is a regular local primitive for the holomorphic differential (932.21).

The leading value $g_P$ can also be obtained without a local integration. Evaluating (932.16) at $\mathcal A=0$ multiplies the value of a weight-$w$ form by $6w\mathcal B$. In the $r-1$ steps of (932.17), these weights are
$1-r,2-r,\ldots,-1$ modulo $p$. Since $r$ is even,
$$
\boxed{\quad
g_P=-6^{r-1}(r-1)!\,b_P^{r-1}F_P,
\qquad F_P=(F/\rho^{k_-})(P).
\quad}
\tag{932.31}
$$
All factorials in this formula are units. The minus sign is retained.

## 5. The canonical functional and the residue sum

The principal parts (932.30) define a class in $H^1(\mathcal O)$ by the usual principal-parts connecting map. Its image under (932.8) is (932.21). For an explicit sign convention, take the Čech coboundary $b_i-b_j$, use primitive $f$ away from the supersingular set and primitive $f-u_P^p$ near $P$, and represent the connecting class by the principal parts $u_P$. Then its de Rham Frobenius is $df$. The associated Serre functional is
$$
\mathcal R_V(\omega)=
\sum_{P\in\mathrm{SS}}\operatorname{Res}_P(u_P\omega).
\tag{932.32}
$$
Changing both Čech and Serre sign conventions multiplies this one functional by a common sign and changes none of the comparison statements.

Equation (932.8) is injective, so the class in (932.32) is the unique $p^{-1}$-linear inverse image of $\Phi_{k_+}(V)$. In particular it is nonzero. This does not imply that its value on any specified differential is nonzero.

The actual comparison (932.14) now gives
$$
\lambda_h=(c_h^{\mathrm F})^{1/p}\mathcal R_V
\tag{932.33}
$$
on the original component union, with the same pairing convention. Thus the multiplier is nonzero in the original marked residue field. It was not defined by dividing by the value at $\Phi_{k_-}(F)$.

To evaluate that specified value on a fine cover, use (932.7) and (932.22):
$$
\begin{aligned}
\Phi_{k_-}(F)
&=\frac16 (F/\rho^{k_-})z^{-(k_--2)}
                 \kappa(T)\,dT\\
&=-\frac16 (F/\rho^{k_-})\kappa(T)
                 z^{r-1}\,dz.
\end{aligned}
\tag{932.34}
$$
Here $dT=(p-1)z^{p-2}dz=-z^{p-2}dz$ and $k_-=p+1-r$. Consequently (932.30–31) give
$$
\begin{aligned}
\operatorname{Res}_P(u_P\Phi_{k_-}(F))
&=-\frac{g_P^{1/p}F_P}{6b_P}\\
&=\frac{g_P^{1+1/p}}
{6^r(r-1)!\,b_P^r}.
\end{aligned}
\tag{932.35}
$$
Thus, on the fine cover,
$$
\boxed{\quad
\mathcal R_V(\Phi_{k_-}(F))
=\frac1{6^r(r-1)!}
\sum_{P\in\mathrm{SS}}
\frac{g_P^{\,1+1/p}}{b_P^r}.
\quad}
\tag{932.36}
$$

To descend this equation, choose one original Igusa part $C_1$ and the actual finite tame cover $\pi:\widetilde C_1\to C_1$ with the transported full-six marking. Write $d_1=\deg(\pi)$; this integer is prime to $p$. Pullback and trace give
$$
\langle \pi^*v,\pi^*\omega\rangle
=d_1\langle v,\omega\rangle.
\tag{932.37}
$$
The chosen fine sum is over **all** supersingular points of $\widetilde C_1$. No supersingular point is removed. Its contribution on $C_1$ is divided by the actual degree $d_1$. No product of stabilizer orders is substituted for that degree when those stabilizers share $-1$.

There is one part in the first row of (932.2), and two in the second. In the latter case let the actual nonsquare-norm element transport $C_1$ to the other part. The two differential extensions have characters $\chi_+$ and $\chi_-$. The inverse de Rham Frobenius changes the first scalar to $\chi_+^{1/p}=\chi_+$, since its values lie in $\mathbf F_p$. Thus the two factors in the transported Serre pairing cancel, and the contribution on the other part is equal to the contribution on $C_1$. This uses both actual norm extensions; it does not require the two modular forms to have the same extension. In particular the rational primitive need only be constructed on the chosen part and then transported with its own $\chi_+$ character.

Let $m_{\mathrm I}=1$ or $2$ be this number of parts. The actual evaluation is therefore
$$
\boxed{\quad
\lambda_h\!\left(\Phi_{k_-}(F)_{\rm full}\right)
=
\frac{m_{\mathrm I}(c_h^{\mathrm F})^{1/p}}
     {d_1\,6^r(r-1)!}
\sum_{P\in\operatorname{SS}(\widetilde C_1)}
\frac{g_P^{\,1+1/p}}{b_P^r}.
\quad}
\tag{932.37a}
$$
Here the subscript indicates the full original $\chi_-$ extension, and $c_h^{\mathrm F}$ is exactly the comparison scalar in (932.14) using the same Serre convention. Every factor outside the sum is nonzero. This is the promised original-functional identity. Its vanishing is exactly the vanishing of this complete and correctly transported supersingular sum. No individual summand is selected as a substitute.

## 6. Independence of local frames and the marked zero

For completeness, replace $\rho$ by $\rho'=a(T)\rho$, with $a(0)\ne0$. The values change by
$$
g'_P=a(0)^{-rp}g_P,\qquad
b'_P=a(0)^{-(p+1)}b_P.
\tag{932.38}
$$
Therefore
$$
\frac{(g'_P)^{1+1/p}}{(b'_P)^r}
=\frac{g_P^{1+1/p}}{b_P^r}.
\tag{932.39}
$$
The use of a $p$th root in this formula is exact: $(a^{-rp})^{1/p}=a^{-r}$. Thus each term in (932.36) is independent of the unit Hodge frame. The residue expression is also independent of a change of local parameter or of a regular addition to a local primitive.

At the actual marked $j=0$ point, the other companion itself has value zero:
$$
F(P^\dagger)=0.
\tag{932.40}
$$
This follows from R875(875.11–15), applied to $k=k_-$: its actual vector is fixed by $ST^{-1}$, the automorphy factor at $\tau^\dagger$ is $\zeta$, and $k_-\equiv1\pmod3$. The integral characteristic-zero identity reduces at the prescribed good tame place. The coefficient in (932.4) is exactly the one used there.

Equations (932.31), (932.35) show that the corresponding summand is zero. The statement does not claim vanishing at every marking over $j=0$, nor does it discard the other supersingular points. In particular the marked unit of $V_4^\dagger/E_4$ or $V_{10}^\dagger/E_4$ in R918/R920 cannot be inserted as a nonzero value for (932.36).

## 7. The remaining original nonvanishing questions

This result identifies the actual functional, not merely an abstract functional with the same eigenvalues. Its line is obtained from the original additive subgroup by the injective map (932.8), the full original characters, and the exact named-vector identifications R918/R920. Its evaluation is the complete residue expression (932.36), with the actual quotient degrees and a nonzero common scalar as in (932.33).

Neither the nonzero class in (932.32) nor the nonzero good-model layer proves that (932.36) is nonzero. A Cartier-kernel vector can still lie in the Cartier image when the zero-primary Cartier part has a longer chain. No residual Hecke semisimplicity, absence of congruences, or automatic pairing nondegeneracy on this one vector has been used.

The original integer $a_h$, original quotient, and target differential remain unchanged. There is still no equality here between the value in (932.36) and $Q'_h(0)$ in R924/R925. In particular the established relation
$$
\mathscr J_h\ne0
\quad\Longleftrightarrow\quad
P_{h-1}(1/\sqrt{-3})\ne0
\ \text{and}\ Q'_h(0)\ne0
\tag{932.41}
$$
retains both conditions. R929 proves an unshifted auxiliary Hasse value is a unit in the $p\equiv5\pmod{12}$ row; it does not prove the shifted Legendre condition in (932.41). No primitive label, determinant extension, or specified $J_{3,2}$ coefficient has been changed.

## Sources

- [R913](R913-original-Igusa-Cartier-functional-and-two-CM-companions.md), (913.8–12), §§3 and 5–7: the actual functional, two weights, full norm extensions, complete Fourier identities, original oldform phase, and Hecke transpose convention.
- [R916](R916-original-finite-flat-quotient-and-exact-Hodge-content.md), §6; [R918](R918-original-central-primitive-Igusa-layer-and-marked-weight-four-vector.md), §§4–5; [R920](R920-original-upper-primitive-Igusa-layer-and-inert-Hecke-row.md), §§4–6: the nonzero original good-model layer and its complete named-vector identification.
- [R875](R875-original-tame-CM-constant-and-first-Cartier-factor.md), (875.11–15): the integral full-six vector and its actual marked vanishing.
- [R925](R925-original-low-normal-coefficients-and-same-label-critical-jet.md): the original low coefficient and same-label critical-jet equivalence, which is not replaced by the residue pairing.
- Oda, *The first de Rham cohomology group and Dieudonné modules*, [original PDF](https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf), printed pp. 110 and 120–123, Definition 5.3, Definition 5.5, and Proposition 5.7: the restricted Lie/Cartier duality and injective $p$-linear de Rham Frobenius. The Čech and residue constructions needed here are proved above.
- Gross, *A tameness criterion for Galois representations associated to modular forms (mod p)*, [original PDF](https://www.math.purdue.edu/~tongliu/seminar/Mlift/Gross.pdf), printed pp. 461–464, Propositions 5.2 and 5.7–5.9: canonical Igusa Hasse root, fine local orders, rational functions and exact differentials, and Hecke compatibility.

All calculations in this proof are symbolic paper derivations. No new mathematical computation or finite-prime scan has been executed.
