# R978 — The original Robert coordinate and its pure Hurwitz mirror

Date: 2026-11-20. Session: `serre-public-astra-20261120-de0a3e3b`. Authoring agent: `handoff_audit`.

**Status: proved exact source identity and integrality.** The high Artin–Hasse coordinate of the fixed Robert unit in R976 is an explicit nonzero factor times one pure Eisenstein–Hurwitz coefficient of the original curve. The complementary low coefficient is already a unit by R972. This result does not prove that the high coefficient is a unit.

The proof takes the complete ray-to-ring-class norm in an integral Lubin–Tate coordinate before evaluating a logarithm. In particular it does not discard terms of the rational sigma series at a point of valuation $1/(p^2-1)$. No new mathematical calculation is executed locally or invoked here.

## 1. Original objects and the statement

Retain the two original rows of R972:
$$
\begin{array}{c|c|c|c}
p\bmod12&r&a=r+1&w=p+1-r\\ \hline
11&2&3&p-1\\
5&8&9&p-7
\end{array}
\qquad p\ge41,\quad p\equiv2,5\pmod9.
\tag{978.1}
$$
Put
$$
q=p^2,\qquad m=\frac{p+1}{3},\qquad b=\frac a3,
\qquad n=p+1-a=3(m-b),\qquad d_0=3(p-1).
\tag{978.2}
$$
Thus $p=3m-1$, $b\in\{1,3\}$, $1\le b<m$, and $d_0m=q-1$. Both rows have $p\equiv5\pmod6$.

Use the original CM model and differential of R977:
$$
K=\mathbb Q(s),\quad s^2=-3,\qquad
E:y^2=x^3+1,\qquad \omega=\frac{dx}{2y},\qquad
\Delta_E=-432.
\tag{978.3}
$$
Let $F=K_p$, $A=\mathcal O_F=W(\mathbb F_{p^2})$. The source differential in (978.3) is fixed throughout. Its Weierstrass invariants are $g_2=0,g_3=-4$.

Let $L=H(\mathbb Z+p\mathcal O_K)$, with its unique prime $\mathfrak P$ above $p$. Keep exactly the root, embeddings, character and arithmetic Artin convention of R972/R976:
$$
\pi^{p+1}=-p,\qquad \varpi=\pi^3,\qquad
\varpi^m=-p,\qquad L_{\mathfrak P}=F(\varpi),
\tag{978.4}
$$
$$
\sigma=\operatorname{Frob}_{(2+s)}^{\mathrm{arith}}\bigm|_L,
\qquad V_7=N_{H_{(p)}/L}\Psi(1;(p),7^{-1}(p)),
\qquad U_7=V_7^{\sigma-1}.
\tag{978.5}
$$
Here $U_7$ is the actual global unit of R976, not an independently chosen local unit. Define $\zeta\in\mu_m\subset A^\times$ by
$$
\sigma\varpi=\zeta\varpi.
\tag{978.6}
$$
R972's reciprocity calculation gives
$$
\widetilde\chi(\sigma)=\zeta^{-b}.
\tag{978.7}
$$
The reduction of $\widetilde\chi(\sigma)-1$ is a unit, by the fixed-ideal computation of R976.

Write the genuine local logarithm, after removing the Teichmüller residue, as
$$
\log\langle U_7\rangle
\equiv\sum_{j=1}^{m-1} B_j\varpi^j\pmod p,
\qquad B_j\in\mathbb F_{p^2}.
\tag{978.8}
$$
R976 fixes its exact two Artin–Hasse coordinates as
$$
\gamma_0=B_b^p,\qquad \gamma_1=B_{m-b}.
\tag{978.9}
$$
The exponent $p$ in the first formula is the original residue-embedding component. It is not dropped or absorbed into an unspecified basis constant.

Define the rational Eisenstein–Hurwitz numbers of the fixed pair $(E,\omega)$ by the formal Weierstrass sigma function:
$$
\log\frac{\sigma_E(z)}z
=-\sum_{N\ge4}\frac{\mathcal G_N}{N}z^N,
\qquad \sigma_E'(0)=1.
\tag{978.10}
$$
For the lattice of $(E,\omega)$, these are $\mathcal G_N=\sum_{\lambda\ne0}\lambda^{-N}$ when $N\ge4$ is even. The series definition fixes the normalization without a choice of notation for factorial-normalized Bernoulli–Hurwitz numbers. Since $g_2=0,g_3=-4$, one has $\mathcal G_N=0$ unless $6\mid N$, and $\mathcal G_N\in\mathbb Q$.

There is a specific root of unity $\eta\in A^\times$, determined in Section 2 by the original Robert point and the fixed root (978.4), with $\eta^m=-1$. For every $1\le j<m$, set $N_j=d_0j$. Then
$$
\mathcal G_{N_j}/N_j\in\mathbb Z_p
\tag{978.11}
$$
and the exact coordinate identity is
$$
\boxed{\quad
B_j=24\,\overline\eta^{-j}(\overline\zeta^j-1)
\,\overline{\frac{\mathcal G_{N_j}}{N_j}}
\quad\text{in }\mathbb F_{p^2}.
\quad}
\tag{978.12}
$$
In particular,
$$
\boxed{\quad
\gamma_1=
24\,\overline\eta^{-(m-b)}\bigl(\chi(\sigma)-1\bigr)
\,\overline{\frac{\mathcal G_{n(p-1)}}{n(p-1)}}.
\quad}
\tag{978.13}
$$
The low coordinate is
$$
\gamma_0=
\left(
24\,\overline\eta^{-b}(\overline\zeta^b-1)
\,\overline{\frac{\mathcal G_{a(p-1)}}{a(p-1)}}
\right)^p.
\tag{978.14}
$$
Consequently R972/R976 imply the two distinct assertions
$$
\frac{\mathcal G_{a(p-1)}}{a(p-1)}\in\mathbb Z_p^\times,
\tag{978.15}
$$
$$
S_{\mathrm{orig}}\ne0
\quad\Longleftrightarrow\quad
\frac{\mathcal G_{n(p-1)}}{n(p-1)}\in\mathbb Z_p^\times.
\tag{978.16}
$$
The first assertion is a theorem. The second is an exact criterion, not a proof of either side. The two indices satisfy
$$
a(p-1)+n(p-1)=p^2-1.
\tag{978.17}
$$

## 2. The strict Lubin–Tate coordinate and the original root

Take $t=-x/y$ as parameter on $\widehat E$, so $\omega=dt+O(t)dt$. For $p\equiv2\pmod3$, the map $x\mapsto x^3$ permutes $\mathbb F_p$. Thus the quadratic-character sum for $y^2=x^3+1$ is zero, and $a_p(E)=0$. The elliptic Frobenius relation gives
$$
\operatorname{Fr}_p^2=[-p]\quad\text{on }E_{\mathbb F_p}.
$$
In this parameter,
$$
[-p]_{\widehat E}(t)\equiv t^q\pmod p,
\qquad [-p]_{\widehat E}'(0)=-p.
\tag{978.18}
$$
Therefore the actual formal group is a Lubin–Tate group over $A$ for the uniformizer $-p$.

Let $F_{\mathrm{LT}}$ be the standard Lubin–Tate group associated with
$$
f(T)=-pT+T^q.
\tag{978.19}
$$
The integral uniqueness theorem for Lubin–Tate series gives a unique strict isomorphism
$$
g:F_{\mathrm{LT}}\xrightarrow{\sim}\widehat E,
\qquad g(T)\in T+T^2A[[T]],
\qquad [-p]_{\widehat E}\circ g=g\circ f.
\tag{978.20}
$$
This is Milne, *Class Field Theory*, I, Lemma 2.11, Propositions 2.12 and 2.14, and Corollary 2.16. Both defining series have coefficients in $A$ and belong to the same $\mathcal F_{-p}$, so the isomorphism has derivative exactly one over $A$ itself. No period or unramified extension is introduced.

For every $\xi\in\mu_{q-1}$ one has $f(\xi T)=\xi f(T)$. The uniqueness statement hence gives $[\xi]_{\mathrm{LT}}(T)=\xi T$. For $\xi\in\mu_6$, the actual CM automorphism
$$
(x,y)\longmapsto(\xi^{-2}x,\xi^{-3}y)
$$
acts on $t$ by $t\mapsto\xi t$, and pulls back $\omega$ to $\xi\omega$. It commutes with $[-p]$ and has derivative $\xi$. Uniqueness in (978.20) therefore proves
$$
g(\xi T)=\xi g(T),\qquad
g(T)/T\in1+T^6A[[T]].
\tag{978.21}
$$

Use the fixed complex division parameter in R977 to select the actual point $P\in E[p]\setminus\{0\}$ under the already chosen $p$-adic embedding. Every such point reduces to the identity because the special fiber is supersingular. Define
$$
\tau=g^{-1}(t(P)).
$$
Since $[-p]_{\mathrm{LT}}(\tau)=0$ and $\tau\ne0$, equation (978.19) gives the exact equation
$$
\tau^{q-1}=p.
\tag{978.22}
$$
The sign in (978.22) is positive: the Lubin–Tate uniformizer is $-p$. Define
$$
X=\tau^{d_0},\qquad X^m=p.
\tag{978.23}
$$
The full local division field is $F(\tau)$, with tame group $\mu_{q-1}$. The subgroup generated by scalar $\mathbb F_p^\times$ and CM $\mu_6$ has order $d_0=3(p-1)$. Its fixed field is $F(X)$. This is precisely the ring-class completion of R972, not an auxiliary extension.

Keep the fixed root $\varpi$ of (978.4), and define
$$
\eta=\varpi/X.
\tag{978.24}
$$
Then $\eta^m=-1$. All roots of $Z^m+1$ are in $A$ because $2m\mid q-1$; thus $\eta$ is a Teichmüller root of unity in $F$, fixed by $\sigma$. Equivalently, $\epsilon=\pi/\tau^{p-1}$ satisfies $\epsilon^{p+1}=-1$ and $\eta=\epsilon^3$. This specifies the phase from the original roots, rather than making a replacement of them. Equations (978.6) and (978.24) now give
$$
\sigma X=\zeta X.
\tag{978.25}
$$

## 3. An integral Robert series with its actual CM invariance

Use the function of (977.6):
$$
F_7(E,t)=\frac{\Delta_E^4}{\psi_7(t)}.
\tag{978.26}
$$
The odd division polynomial has leading term $7x^{24}$, while $x=t^{-2}+\cdots$ has an integral expansion for the smooth model (978.3). Since $7$ is a $p$-adic unit,
$$
F_7(E,t)=\frac{\Delta_E^4}{7}\,t^{48}h_7(t),
\qquad h_7(t)\in1+tA[[t]].
\tag{978.27}
$$
The source $\mu_6$ fixes $F_7$: its division-polynomial weight is $48$, and $6\mid48$. As $t^{48}$ is likewise invariant, $h_7(\xi t)=h_7(t)$ for $\xi\in\mu_6$. Comparing coefficients over $A$ gives
$$
h_7(t)\in1+t^6A[[t]].
\tag{978.28}
$$
Define the actual integral series
$$
H(T)=\left(\frac{g(T)}T\right)^{48}h_7(g(T)).
\tag{978.29}
$$
By (978.21) and (978.28),
$$
\boxed{\quad H(T)\in1+T^6A[[T]],\qquad
F_7(E,g(T))=\frac{\Delta_E^4}{7}T^{48}H(T).\quad}
\tag{978.30}
$$
In particular $H$ is even. The possible twelfth root in the Robert normalization is retained in the norm formula below; it is not hidden in $g$ or $H$.

## 4. The whole half-kernel norm is an integral series in $X$

Put $D=(p-1)/2$, and choose representatives for $\mu_{p-1}/\{\pm1\}$. Since $H$ is even, the following product is independent of representatives:
$$
\mathcal P(T)=\prod_{u\in\mu_{p-1}/\{\pm1\}}H(uT).
\tag{978.31}
$$
It is invariant under $\mu_{p-1}$ by permutation of the factors, and under $\mu_6$ by (978.30). These two groups generate the cyclic group of order
$$
\operatorname{lcm}(p-1,6)=3(p-1)=d_0.
$$
For a coefficient of degree not divisible by $d_0$, choose a group element whose corresponding power differs from one; this difference is a unit of $A$, since its order is prime to $p$. Coefficient comparison forces that coefficient to vanish. It follows that there is an integral series
$$
\boxed{\quad \mathcal P(T)=G(T^{d_0}),\qquad
G(X)\in1+XA[[X]].\quad}
\tag{978.32}
$$

For an integer $u$ prime to $p$, its Teichmüller lift and $u$ have the same action on the $p$-torsion of the formal group: their difference is in $pA$, which annihilates that torsion. Thus the factors $g(u\tau)$ in (978.31) represent exactly the nonzero points of the actual cyclic kernel modulo $\{\pm1\}$. By the original multiplicity (977.11),
$$
V_7=\xi C_0 X^8G(X),\qquad \xi^{12}=1,
\tag{978.33}
$$
where
$$
C_0=\left(\frac{\Delta_E^4}{7}\right)^D
\prod_{u\in\mu_{p-1}/\{\pm1\}}u^{48}\in A^\times.
$$
Indeed $48D=24(p-1)=8d_0$. This also recovers the valuation $v_\varpi(V_7)=8$ of R977 with the full multiplicity intact.

The coefficient $C_0$ is fixed by $\sigma$. Roots of unity have zero $p$-adic logarithm; $\mu_{12}\subset F$ in the present range. Using (978.25), the actual unit $U_7$ therefore satisfies
$$
\boxed{\quad
\log\langle U_7\rangle=
\log G(\zeta X)-\log G(X).
\quad}
\tag{978.34}
$$
Both arguments on the right belong to $1+X\mathcal O_{L_{\mathfrak P}}$. This equality has been obtained from the complete integral norm before any logarithmic truncation.

## 5. Why no higher logarithmic terms return modulo $p$

The ramification index of $F(X)/F$ is
$$
e=m=(p+1)/3<p-1.
$$
Consequently log and exp give inverse integral maps between $1+X\mathcal O_{L_{\mathfrak P}}$ and $X\mathcal O_{L_{\mathfrak P}}$. We also give the coefficient bound needed for the exact truncation.

Write the formal characteristic-zero logarithm as
$$
\log G(X)=\sum_{j\ge1}g_jX^j.
$$
Since $G'/G\in A[[X]]$, one has $jg_j\in A$. Normalize $v_X(X)=1$, hence $v_X(p)=m$. Then
$$
v_X(g_jX^j)\ge j-mv_p(j).
\tag{978.35}
$$
For every $j\ge m$, this lower bound is at least $m$. If $p\nmid j$ this is immediate. If $v_p(j)=t\ge1$, then
$$
j-mt\ge p^t-mt\ge p-m=2m-1\ge m.
\tag{978.36}
$$
The middle inequality follows because $p^t-mt$ increases for $t\ge1$. Thus all terms with $j\ge m$ vanish modulo $p$, including those with $p$ in their denominators. For $1\le j<m$, $g_j\in A$.

Substituting $X=\eta^{-1}\varpi$ in the already convergent equality (978.34) now gives
$$
B_j=\overline\eta^{-j}(\overline\zeta^j-1)\overline{g_j},
\qquad 1\le j<m.
\tag{978.37}
$$
The argument applies to $G$ after the norm, whose variable has ramification $m$. It does not assert this truncation for $\log H(\tau)$, where the valuation denominator would be $q-1$.

## 6. Formal sigma coefficients below the first Lubin–Tate correction

Let $z=\log_E(t)$ be the formal elliptic logarithm with $dz=\omega$. The strict isomorphism (978.20) gives
$$
z(g(T))=\log_{\mathrm{LT}}(T).
\tag{978.38}
$$
The standard Lubin–Tate logarithm is equivariant for $[\xi](T)=\xi T$ with $\xi\in\mu_{q-1}$. Its nonzero degrees are therefore $1$ modulo $q-1$, and its linear coefficient is one. Consequently
$$
z(g(T))=T+O(T^q).
\tag{978.39}
$$
This is an equality of formal series over $F$. No evaluation of the right side at $\tau$ will be used.

For the formal sigma function of (978.10), the odd division-polynomial identity is
$$
\psi_7(z)=\frac{\sigma_E(7z)}{\sigma_E(z)^{49}}.
\tag{978.40}
$$
For completeness, the quotient on the right is elliptic: the quasi-period factors cancel between $7z$ and the $49$-th power. Its divisor is $[7]^*[O]-49[O]$ and its leading term is $7z^{-48}$. The ordinary division polynomial has the same divisor and leading term, so their ratio is one. The odd integer seven gives no additional sign. This proves (978.40) with the differential and leading coefficient of (978.3).

Combining (978.30), (978.38), and (978.40), with $z=z(g(T))$, yields the formal identity
$$
\log H(T)
=48\log\frac zT
+49\log\frac{\sigma_E(z)}z
-\log\frac{\sigma_E(7z)}{7z}.
\tag{978.41}
$$
For $N<q-1$, equation (978.39) shows that the first term contributes zero in degree $N$, and substitution of $z$ changes no coefficient of that degree in the remaining terms. If
$$
c_N=[T^N]\log H(T),
$$
then
$$
c_N=-(49-7^N)\frac{\mathcal G_N}{N},
\qquad N<q-1.
\tag{978.42}
$$
Only formal coefficients are compared here; in particular no convergence assertion for the rational sigma series at a torsion point enters the proof.

Taking the formal logarithm in (978.32) gives
$$
\log G(T^{d_0})
=\sum_{u\in\mu_{p-1}/\{\pm1\}}\log H(uT).
$$
For $N_j=d_0j$ every $u^{N_j}=1$, so coefficient comparison gives
$$
g_j=Dc_{N_j}
=-D(49-7^{N_j})\frac{\mathcal G_{N_j}}{N_j},
\qquad 1\le j<m.
\tag{978.43}
$$
Here $N_j<d_0m=q-1$, so (978.42) applies.

Every selected index $N_j=3(p-1)j$ is prime to $p$, since $j<m<p$. Integrality of $H$ also gives $Nc_N\in A$ by its logarithmic derivative. Thus $c_{N_j}\in A$. Moreover
$$
49-7^{N_j}\equiv48\pmod p
$$
is a unit. Formula (978.42) proves (978.11), including its rationality over $\mathbb Z_p$. No integrality statement for unselected sigma indices is needed.

Finally, reducing (978.43) gives
$$
\overline{g_j}
=24\,\overline{\frac{\mathcal G_{N_j}}{N_j}},
\tag{978.44}
$$
because $D=(p-1)/2\equiv-1/2$ and $49-7^{N_j}\equiv48$. Combining this with (978.37) proves the positive constant $24$ in (978.12).

## 7. The two original coordinates and the remaining question

For $j=m-b$, equations (978.2) and (978.7) give
$$
N_j=n(p-1)=p^2-1-a(p-1),\qquad
\zeta^j-1=\widetilde\chi(\sigma)-1.
$$
Equations (978.9) and (978.12) therefore prove (978.13). Taking $j=b$ and the original $\tau_1$ embedding proves (978.14). All outside factors in these two equations are units: $p\ge41$, $\eta$ is a root of unity, and $\chi(\sigma)-1\ne0$ by R976. Also $\zeta^b-1\ne0$ because it is the inverse-character version of the same factor.

R972 proves $\gamma_0\ne0$, giving (978.15). R972/R976 identify $\gamma_1\ne0$ with the nonvanishing of the original whole supersingular pairing, giving (978.16). For $r=2$, the latter is additionally equivalent to the actual Igusa secondary Hasse coefficient $\kappa\ne0$ by R965. The height-two formal group used in Sections 2–6 is that of the fixed source CM elliptic curve; it is not a proof that the distinct Igusa factor has height two.

This result does not identify the two rational coefficients in (978.17), even modulo $p$. Their complementary exponents and the residual Frobenius symmetry do not imply an equality of integral sigma coefficients. A supersingular Kummer or reciprocity theorem used to finish the argument would have to establish the nonvanishing of the high coefficient in the exact normalization (978.10). Merely transferring the already known low coordinate, discarding factorials, or using an unspecified CM period would leave that step unproved.

The relation to R977 is exact at the source: its $\delta_p=D_C/\varpi^4$ has $\log U_7=2(\sigma-1)\log\langle\delta_p\rangle$. Equations (978.12)–(978.14) calculate the same unit's coefficients by its integral division-function norm. They do not replace $\omega_C$ by a minimal differential or suppress the $p^{12}$ factor in (977.5).

## Sources and dependencies

1. J. S. Milne, *Class Field Theory*, version 4.03 (2020), Chapter I, Definition 2.9, Lemma 2.11, Propositions 2.12 and 2.14, Corollaries 2.16 and 2.17, printed pp. 32–35. [Author PDF](https://www.jmilne.org/math/CourseNotes/CFT.pdf). These give the integral strict isomorphism for the two specified Lubin–Tate series and the Teichmüller action.
2. NIST, *Digital Library of Mathematical Functions*, §§23.2 and 23.9, especially (23.2.6), (23.2.8), and (23.9.1)–(23.9.4). [Sigma definition](https://dlmf.nist.gov/23.2), [Laurent coefficients](https://dlmf.nist.gov/23.9). These fix the ordinary Weierstrass sigma and lattice-sum normalization; the division-polynomial identity needed here is proved in Section 6.
3. [R972](R972-original-two-Artin-Hasse-lines-and-ring-class-regulator.md): the original ring class field, root, character, canonical two embedding components, global-unit primitivity, and exact low/high zero criterion.
4. [R976](R976-fixed-Robert-unit-and-original-high-coordinate.md): the actual fixed Robert unit $U_7$, its unit $\chi(\sigma)-1$, and $\gamma_0=B_b^p$, $\gamma_1=B_{m-b}$.
5. [R977](R977-original-Robert-norm-and-normalized-isogeny-discriminant.md), equations (977.6), (977.11), (977.14), (977.19), and (977.23): the original division function, exact half-kernel multiplicity, discriminant source, and retained root-of-unity convention.
6. [R965](R965-exact-original-trace-calibration-of-the-Igusa-height-coefficient.md): the separate exact calibration with the original $r=2$ Igusa coefficient.
