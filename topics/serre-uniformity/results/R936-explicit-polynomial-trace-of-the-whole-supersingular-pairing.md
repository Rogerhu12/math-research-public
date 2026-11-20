# R936: Explicit polynomial trace for the whole R932 supersingular sum

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / handoff_audit.

**Status: paper proof of the trace formula and the finite computation contract below. No prime has been evaluated in this note.** This continues R932, without asserting its sum is nonzero and without identifying that sum with R925's $Q'_h(0)$. The original quotient, positive cubic transport, determinant correction, full norm characters, oldform phase, and the unknown nonzero source scalar of R932 remain unchanged.

## 1. Statement and conventions

Let $p\ge41$ be prime with $p\equiv5\pmod6$. The original Serre application additionally requires $p\equiv2,5\pmod9$; any numerical output outside those two classes must be labeled auxiliary. Put
$$
p=6N+5,\qquad k=\mathbf F_p(s),\quad s^2=-3,\qquad
\zeta=(-1+s)/2.
\tag{ET1}
$$
Here $-3$ is a nonsquare, so $k=\mathbf F_{p^2}$. The two original labels give
$$
\begin{array}{c|c|c|c}
p\bmod12&r&k_-=p+1-r&J=(k_--4)/6\\ \hline
11&2&p-1&N\\
5&8&p-7&N-1.
\end{array}
\tag{ET2}
$$
Here $J$ denotes the degree of the companion polynomial in (ET6). It also equals the degree $m_h$ of the calibrated polynomial in R924/R925 for these two labels; it is not a Jacobian.

Write $F=V_{k_-}^{\dagger}$ for precisely R913's marked companion
$$
V_{k_-}^{\dagger}(Q)=F_{k_-}(Q)-2^{k_-}\zeta^2F_{k_-}(Q^4).
\tag{ET3}
$$
Let $\mathcal A$ be the Tate-normalized Hasse invariant and
$\mathcal B=\partial_{p-1}\mathcal A$, as in R932. Let
$$
S=\sum_{P\in\mathrm{SS}(\widetilde C_1)}
\frac{g_P^{1+1/p}}{b_P^r}
\tag{ET4}
$$
be the *entire* fine full-six Igusa sum of R932(932.36–37a), with those same definitions of $g_P$ and $b_P$.

The following explicit data use one variable $t$. Set
$$
D(t)=1-4t,\quad m=3N+2,
$$
$$
H_N(t)=
\sum_{a=0}^{\lfloor N/2\rfloor}
\frac{m!\,3^{3a+1}}
{(2N+1-a)!(3a+1)!(N-2a)!}\,
t^aD(t)^a(1/2-4t)^{N-2a}.
\tag{ET5}
$$
Every denominator is a $p$-unit.

There is a uniquely determined monic polynomial $P_J(X)\in k[X]$ of degree $J$ such that
$$
F=V_4^\dagger\eta^{12J}P_J(E_6/\eta^{12}).
\tag{ET6}
$$
All forms on the right use the original full-six variable $\tau'$, hence $E_6=E_6(Q^6)$ and $\eta^{12}=Q^3\prod_{n\ge1}(1-Q^{6n})^{12}$. Section 5 below gives a finite, integral construction of $P_J$ from (ET3).

In the finite algebra
$$
L=k[t]/(tH_N(t))
\tag{ET7}
$$
define
$$
\begin{aligned}
C(t)&=12s(6s)^JP_J(24s(1-8t)),\\
b(t)&=-D(t)\bigl(H_N(t)+3tH'_N(t)\bigr),\\
e_0(t)&=H_N(t)/H_N(0),\\
R(t)&=D(t)^{2N+2}\,C(t)^{p+1}\,b(t)^{-k_-}.
\end{aligned}
\tag{ET8}
$$
The algebra $L$ is étale of dimension $N+1$, and $b$ is a unit in it. In particular every operation displayed here is defined. The exact formula is
$$
\boxed{
S^p=
12\,[ -6^{r-1}(r-1)!]^2\,
\operatorname{Tr}_{L/k}\bigl((3-2e_0)R\bigr).
}
\tag{ET9}
$$
The factor twelve is the actual degree of the geometric full-six tame cover, with its ramification accounted for below. No supersingular branch or stabilizer weight is omitted.

For the actual functional of R932, this retains
$$
\lambda_h(\Phi_{k_-}(F)_{\rm full})
=
\frac{m_{\rm I}(c_h^{\rm F})^{1/p}}
{d_1\,6^r(r-1)!}\,S.
\tag{ET10}
$$
The factors $d_1,m_{\rm I},c_h^{\rm F}$ are exactly those of R932. In particular $d_1$ is *not* replaced by twelve: it is the degree of the full fine Igusa cover to the actual component and may include further quotient data. All factors outside the trace in (ET9–10) are nonzero, so the trace detects the original functional's zero or nonzero value without computing the unknown source scale.

## 2. Removing the $p$th roots without changing frames

R932(932.31) gives
$$
g_P=c_r b_P^{r-1}F_P,\qquad
c_r=-6^{r-1}(r-1)!\in\mathbf F_p^\times.
\tag{ET11}
$$
In characteristic $p$, raising the full finite sum to $p$ gives
$$
\begin{aligned}
S^p
&=\sum_P\frac{g_P^{p+1}}{b_P^{rp}}\\
&=c_r^2\sum_P
\frac{F_P^{p+1}}{b_P^{p+1-r}}
=c_r^2\sum_P\mathfrak R(P),
\end{aligned}
\tag{ET12}
$$
where
$$
\mathfrak R=\frac{F^{p+1}}{\mathcal B^{k_-}}.
\tag{ET13}
$$
The weights agree:
$k_-(p+1)=k_-(p+1)$. Thus (ET13) is a rational modular function, regular at every supersingular point because $\mathcal B$ is nonzero there in a good Hodge frame. This also proves directly that (ET12) is independent of every local Hodge frame. The passage uses Frobenius additivity, not a positivity statement about finite-field norms.

The function (ET13) is invariant under the whole actual tame group $H_6$. It descends to its coarse curve $X'(6)$. It is also invariant under the order-three deck action: $F^{p+1}$ has trivial deck character because $3\mid p+1$.

## 3. The actual genus-zero model and its Hodge frame

Use the already fixed model from R918/R920:
$$
X'(6)=\mathbf P^1_u,\qquad
j=27648u^3(1-4u^3),\qquad t=u^3.
\tag{ET14}
$$
The positive original model is $a=\sqrt[3]4\,u$, so $D=1-a^3$. This is the same unit cubic transport as R575 and R913.

On $D\ne0$ a generic elliptic curve representing this modular point is
$$
E_u:\quad
y^2=x^3+3uD\,x+D(1/2-4u^3),\qquad
\omega=dx/(2y).
\tag{ET15}
$$
Its directly computed invariants are
$$
c_4=-144uD,\qquad
c_6=-432D(1-8u^3),\qquad
\Delta=-108D^2.
\tag{ET16}
$$
Indeed $c_4^3-c_6^2=-186624D^2=1728(-108D^2)$, and $c_4^3/\Delta$ is (ET14). These equations fix the normalization used here directly from the Weierstrass equation; no discriminant constant from an external transcription is imported.

With algebraic modular forms normalized on the Tate curve, $E_4(E_u,\omega)=c_4$ and $E_6(E_u,\omega)=c_6$. The original marked cusp fixes the evaluations
$$
V_4^\dagger(E_u,\omega)=12sD,\qquad
\eta^{12}(E_u,\omega)=6sD,
$$
$$
(E_6/\eta^{12})(E_u,\omega)=24s(1-8u^3).
\tag{ET17}
$$
Here is a check of the constants and their marking. The valence divisor of $V_4^\dagger$ in R918 gives
$u=C\,E_4/V_4^\dagger$ for a constant $C$. At the original cusp
$$
V_4^\dagger=Q+8sQ^4+O(Q^7),\quad
E_4=1+O(Q^6),\quad j=Q^{-6}+744+O(Q^6).
$$
Comparing $Q^{-6}$ and $Q^{-3}$ in (ET14) gives
$C^6=-1/110592$ and $C^3=s/576$. Choose the branch
$C=1/(4s)$, which changes only the coordinate by a deck cube root if a different $u$ representative was originally used. The weight-zero function (ET13), as well as $t=u^3$, is unchanged by that choice. Then $V_4^\dagger=c_4/(4su)=12sD$.

The identity $\eta^{24}=\Delta$ gives $\eta^{12}=\pm6sD$. The positive sign is fixed by the same cusp: $u\sim(4s)^{-1}Q^{-1}$, so the weight-six Hodge-frame factor satisfies $c_6/E_6(Q^6)\sim Q^{-6}/8$. Therefore the evaluation of $\eta^{12}\sim Q^3$ is $Q^{-3}/8$, exactly the leading term of $6sD$. This proves (ET17) in the specified phase, rather than choosing an untracked square root.

The Kodaira–Spencer form in this frame is
$$
\operatorname{KS}(\omega^2)=-\frac{du}{D}.
\tag{ET18}
$$
To see it without choosing a Gauss–Manin connection matrix, use the algebraic modular identity
$d j/j=-(E_6/E_4)\operatorname{KS}(\omega^2)$ on the locus where the displayed quotients are defined. Substitution of (ET14) and (ET16) gives (ET18); both sides then extend across the removable $j=0,1728$ expressions on $D\ne0$.

## 4. The Hasse polynomial and all supersingular points

In the frame of (ET15), the Hasse invariant is
$$
\mathcal A(E_u,\omega)
=[x^{p-1}]
\bigl(x^3+3uDx+D(1/2-4u^3)\bigr)^{(p-1)/2}.
\tag{ET19}
$$
This is the usual direct Cartier calculation on $dx/(2y)$: rewrite the differential with $y^p$ in the denominator and select exponent $p-1$; the factor two is unchanged because $2^{p-1}=1$.

Let the exponents of $x^3$, $3uDx$, and $D(1/2-4u^3)$ in a contributing multinomial term be $i,j,\ell$. They satisfy
$i+j+\ell=m$ and $3i+j=2m$. Thus $i=j+2\ell$, and with $m=3N+2$ necessarily
$$
j=3a+1,\qquad
\ell=N-2a,\qquad
i=2N+1-a.
$$
Substitution gives exactly
$$
\boxed{\mathcal A(E_u,\omega)=uD^{N+1}H_N(u^3).}
\tag{ET20}
$$

The polynomial $H_N$ has degree $N$, and
$$
H_N(0)=
\frac{(3N+2)!\,3\,2^{-N}}{(2N+1)!\,N!}\ne0,
$$
$$
H_N(1/4)=
\frac{(3N+2)!\,3\,(-2)^{-N}}{(2N+1)!\,N!}\ne0.
\tag{ET21}
$$
For the degree assertion, (ET19) has degree at most $p-1$ in $u$. At the cusp its Hodge-frame factor has pole order $p-1$, while the Hasse invariant in the Tate frame has constant term one. Its degree is consequently exactly $p-1$. Dividing by $uD^{N+1}$ gives degree $N$ in $u^3$.

Outside $D=0$, the geometric full-six cover is unramified over $X'(6)$, since the only elliptic stabilizers on this latter curve are the three order-three points $D=0$. The Hasse divisor on the fine tame curve is reduced. Therefore the zeros of $uH_N(u^3)$ are all simple. In particular $H_N$ is squarefree, and by (ET21) none of its roots is $0$ or $1/4$. This proves that (ET7) is étale.

We now account for every point of the fine supersingular set. The effective index of $\Gamma(6)$ is $72$, whereas that of the original $H_6$ is $6$. Thus the geometric fine tame cover
$$
X(6)\longrightarrow X'(6)
$$
has degree $12$. At each point with $D\ne0$ it has twelve geometric points above it. At each of the three elliptic points $D=0$ it has four points, each with ramification index three. The Igusa cover over $X(6)$ has one point above each supersingular point, totally ramified of degree $p-1$. Thus no additional factor $p-1$ multiplies the supersingular point sum.

All three $D=0$ points are supersingular, since their $j$-invariant is zero and $p\equiv2\pmod3$. Their contributions to (ET12) are zero. Indeed a form of weight $k_-\equiv4\pmod6$ has fine order at least one at every order-three elliptic point, whereas $\mathcal B$ is a unit in the good Hodge frame. Therefore $\mathfrak R=F^{p+1}/\mathcal B^{k_-}$ vanishes there. This establishes their zero contribution; it does not discard those branches. It says nothing similar about the nonelliptic point $u=0$ over $j=0$.

The count is complete:
$$
12(3N+1)+3\cdot4=36N+24=6(p-1),
$$
the degree of the Hasse divisor on the fine full-six curve, whose Hodge line has degree six. There are no supersingular cusps.

## 5. Computing the original companion polynomial

R918 proves that $V_4^\dagger$ has exactly the mandatory cusp zero and fine order-one zeros at the three order-three elliptic points, and no others. Since $k_-=6J+4$, division by $V_4^\dagger$ identifies its cusp space with $M_{6J}(H_6)$. Division by $\eta^{12J}$ then gives a rational function on $\mathbf P^1_u$ with no finite poles and a pole of order at most $3J$ at infinity.

The quotient has trivial deck character: $F$ and $V_4^\dagger$ have the same original character, and $\eta^{12}$ is deck invariant by R920. It is therefore a polynomial in $u^3$ of degree at most $J$. R920's exact relation
$$
E_6/\eta^{12}=24s(1-8u^3)
$$
in the fixed cusp phase proves (ET6).

An integral basis for this character space is
$$
B_j=V_4^\dagger E_6^{J-j}\eta^{12j},
\qquad 0\le j\le J.
\tag{ET22}
$$
Its leading terms at the original cusp are $Q^{1+3j}$, with coefficient one. The matrix of the coefficients at $Q,Q^4,\ldots,Q^{1+3J}$ is triangular with diagonal one. As in R918/R920, cohomology and base change on the fine genus-one curve and averaging through the actual prime-to-$p$ group preserve the full integral character space. The triangular determinant proves that (ET22) is its full integral basis, not a sublattice of unspecified index.

Consequently subtracting successive $B_j$ multiples at their first nonzero coefficients recovers
$$
F=\sum_{j=0}^J c_jB_j,\qquad
P_J(X)=\sum_{j=0}^Jc_jX^{J-j}.
\tag{ET23}
$$
Only coefficients through $Q^{1+3J}$ are needed. The coefficient $c_0=1$, so $P_J$ is monic. This is an equality of the actual original modular forms, established from membership in the proved character space and its full triangular basis, not a conjecture from a finite Fourier match.

For a direct finite construction of the theta series, for $1\le n\le1+3J$ use
$$
[Q^n]F_{k_-}=
\frac16
\sum_{\substack{a,b\in\mathbf Z\\a^2-ab+b^2=n}}
(a+b\zeta)^{k_--1}\epsilon_3(a+b\zeta),
\tag{ET24}
$$
with the sum zero when $3\mid n$. Here
$\epsilon_3(a+b\zeta)=1$ or $-1$ according as $a+b\equiv1$ or $-1\pmod3$. Each principal ideal has six generators, and their terms agree because $k_--1$ is odd and divisible by three. The class number of $\mathbf Q(\sqrt{-3})$ is one, so (ET24) is precisely R913's theta series. The bounds $|a|,|b|\le\sqrt{2n}$ are sufficient because $a^2-ab+b^2\ge(a^2+b^2)/2$.

The remaining series in (ET22) have the exact finite product formulas
$$
\begin{aligned}
F_4(Q)&=Q\prod_{n\ge1}(1-Q^{3n})^8,\\
V_4^\dagger(Q)&=F_4(Q)-16\zeta^2F_4(Q^4),\\
E_6(Q^6)&=1-504\sum_{n\ge1}\sigma_5(n)Q^{6n},\\
\eta^{12}(Q^6)&=Q^3\prod_{n\ge1}(1-Q^{6n})^{12}.
\end{aligned}
\tag{ET25}
$$
Truncate only after the proved cutoff. This construction neither scans the original sigma series nor repeats any old prime certificate.

## 6. The denominator and the algebra trace

At a supersingular point with $D\ne0$, the connection term in $\partial_{p-1}\mathcal A$ is multiplied by $\mathcal A$ and vanishes. Thus (ET18) implies
$$
\mathcal B(E_u,\omega)
\equiv-D\,\frac{d}{du}\mathcal A(E_u,\omega)
\pmod{\mathcal A}.
\tag{ET26}
$$
Using (ET20) and then reducing modulo $uH_N(u^3)$ gives
$$
\frac{\mathcal B(E_u,\omega)}{D^{N+1}}
\equiv
-D\bigl(H_N(t)+3tH'_N(t)\bigr)=b(t).
\tag{ET27}
$$
This equality is asserted on the supersingular finite algebra, exactly where it is used; it is not an identity of arbitrary connection-dependent extensions away from that algebra.

At $t=0$, $b(0)=-H_N(0)\ne0$. At a root $\alpha$ of $H_N$,
$$
b(\alpha)=-3\alpha D(\alpha)H'_N(\alpha)\ne0
$$
by squarefreeness and (ET21). Hence $b$ is a unit in $L$.

Evaluation of (ET6) with (ET17) gives
$$
F(E_u,\omega)=D^{J+1}C(t).
\tag{ET28}
$$
Because $k_-=6J+4$ and $p+1=6(N+1)$,
$$
(J+1)(p+1)-(N+1)k_-=2N+2.
\tag{ET29}
$$
Substitution of (ET27–29) in (ET13) proves that its value on every $D\ne0$ supersingular branch is exactly $R(t)$ in (ET8).

The point $t=0$ has one $u$ preimage. Every nonzero root of $H_N(t)$ has three distinct $u$ preimages. Thus
$$
\sum_{\substack{u\in\overline k\\uH_N(u^3)=0}}
\mathfrak R(u)
=R(0)+3\sum_{H_N(\alpha)=0}R(\alpha).
\tag{ET30}
$$
The element $e_0=H_N/H_N(0)$ of $L$ is the idempotent which is one at $t=0$ and zero at every root of $H_N$. Therefore the right side of (ET30) is
$\operatorname{Tr}_{L/k}((3-2e_0)R)$, including residue-field degrees when a root is not rational over $k$. Multiplying by the twelve fine points over each such $u$, and adding the proved zero elliptic contributions, proves (ET9) from (ET12).

No factorization or root enumeration is required. If $M(t)$ is the monic polynomial proportional to $tH_N(t)$, of degree $d=N+1$, then
$$
\operatorname{Tr}_{L/k}(Z)
=[t^{d-1}]\bigl(Z(t)M'(t)\bmod M(t)\bigr).
\tag{ET31}
$$
For a proof, use Lagrange interpolation at the distinct roots of $M$: the coefficient of $t^{d-1}$ in the polynomial representing $ZM'$ is the sum of its values divided by $M'(\alpha)$, namely $\sum Z(\alpha)$. This is also the trace of multiplication by $Z$.

## 7. Exact scope, including $p=41$

The method computes the same entire R932 sum, not one local contribution and not an unsigned or rescaled substitute. The unknown original source constant is retained in (ET10). All prime-to-$p$ fine-cover, Igusa-component, and norm factors remain where R932 put them.

The nonzero or zero value of (ET9) is not presently identified with $Q'_h(0)$. R925 still requires that coefficient and the independent original Legendre factor for the specified fifth jet. In particular the newly reported $p=41,h=25$ Legendre zero does not force the trace in (ET9) to be zero: no Legendre multiplier occurs in (ET9). Conversely a nonzero trace at $41$ would not repair that fifth-jet zero.

An exact finite run of the accompanying script can produce proved values for the requested primes. Such values are finite conclusions only. They do not prove all-prime nonvanishing, an upper bound for the original height obstruction, or Serre uniformity.

## Sources and retained dependencies

- R932, equations (932.31), (932.36–37a): the full original principal parts, residue formula, and source scalar.
- R913, §§5–7: actual CM theta series, oldform coefficient, fixed $\zeta^2$ phase, and full inertia/Hecke transports.
- R918, §§2–4: the original $H_6$, its index-six coarse curve, three elliptic points, fine genus-one curve, and divisor of $V_4^\dagger$.
- R920, §§2–3: $u\mapsto\zeta u$, the complete weight-six module, $\eta^{12}$ and $E_6$, and exact cusp coefficients.
- J. Brau and N. Jones, *Elliptic curves with 2-torsion contained in the 3-torsion field*, Theorem 1.4 and its proof: https://homepages.math.uic.edu/~ncjones/2tin3t.pdf . The invariants of the displayed family are calculated directly in (ET16).
- B. H. Gross, *A tameness criterion for Galois representations associated to modular forms (mod p)*, §1, Proposition 1.9; §2, Proposition 2.3; §5, Propositions 5.2 and 5.7–5.9: https://www.math.purdue.edu/~tongliu/seminar/Mlift/Gross.pdf .

All derivations above are paper algebra. No new arithmetic has been executed locally.

## Executable consumer

The exact consumer is `scripts/R936_whole_supersingular_trace.py`, run through the public `serre-current-exact-research.yml` workflow. Script, exact parameters, source commit, run ID and deterministic output SHA are retained; raw polynomial arrays and matrices are temporary and are not committed. No computed value is asserted by this formula proof.
