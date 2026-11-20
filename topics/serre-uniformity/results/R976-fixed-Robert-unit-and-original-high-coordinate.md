# R976 — A fixed Robert unit and the original high coordinate

Date: 2026-11-20. Authoring agent: literature_frontier. Independently checked by root and handoff_audit against the primary sources.

**Status: proved fixed global generator and exact local coefficient criterion.** This note supplies a fixed, explicit elliptic unit generating the actual global unit character line, and identifies the remaining high-weight condition with a specified coefficient of its finite local logarithm. It does not prove that this last coefficient is nonzero. All derivations are symbolic; no numerical mathematics is executed locally.

## 1. The original fields and characters

Keep both original rows of R970 and put
$$
a=r+1\in\{3,9\},\qquad n=p+1-a,\qquad
m=\frac{p+1}{3},\qquad b=\frac a3\in\{1,3\}.
\tag{976.1}
$$
Thus $n/3=m-b$. In the original range $p\ge41$, $p\equiv2,5\pmod9$ and $p\equiv5\pmod6$. In particular $\gcd(a,p+1)=3$.

Let $K=\mathbb Q(s)$, $s^2=-3$, and let $\mathfrak p=(p)$ be its inert prime. Write
$$
R=H_{\mathfrak p},\qquad
L=H(\mathbb Z+p\mathcal O_K),\qquad
\Delta=\operatorname{Gal}(L/K).
\tag{976.2}
$$
Here $R$ is the ray class field modulo $\mathfrak p$, whereas $L$ is the ring class field of conductor $p$. The standard exact ray and ring class sequences, using $h_K=1$ and $\mathcal O_K^\times=\mu_6$, give
$$
\operatorname{Gal}(R/K)=\mathbb F_{p^2}^{\times}/\mu_6,
\qquad
\Delta=\mathbb F_{p^2}^{\times}/(\mathbb F_p^{\times}\mu_6),
\qquad
[L:K]=m,\quad[R:L]=\frac{p-1}{2}.
\tag{976.3}
$$
The prime $\mathfrak p$ is unique and totally ramified in $L$.

Use exactly R972's residual character and its Teichmüller lift, denoted by the same symbol when no ambiguity is possible:
$$
\chi=\bar\chi_a,\qquad
\chi(\operatorname{Frob}_{(\alpha)}^{\mathrm{arith}})
=\left(\frac{\alpha}{\bar\alpha}\right)^a\pmod p.
\tag{976.4}
$$
This character is faithful on $\Delta$ and has conductor $\mathfrak p$. A coefficient ring $\mathcal O$ unramified over $\mathbb Z_p$, with residue field containing $k=\mathbb F_{p^2}$, contains all its values. Set
$$
e_\chi=\frac1m\sum_{\sigma\in\Delta}\chi(\sigma)^{-1}\sigma.
\tag{976.5}
$$
Thus $\sigma e_\chi=\chi(\sigma)e_\chi$. This is the actual $\chi$-unit component, not the $\chi^{-1}$-component. The inverse character appearing in a complex $L$-value below results from the complex regulator convention, not from switching the arithmetic component.

The following inputs are supplied by R972 and are not reproved here:

1. The actual low Fontaine--Laffaille adjoint Selmer group vanishes, and $e_\chi(\mathcal O\otimes\operatorname{Cl}(L))[p^\infty]=0$.
2. The image of the global $\chi$-unit lattice in the two-dimensional local unit space modulo $p$ is a nonzero line.
3. In R972's precise Artin--Hasse basis this line has coordinates $(\gamma_0,\gamma_1)$ with $\gamma_0\ne0$, and the original high congruence ideal, hence the original complete trace by R970, is a unit/nonzero exactly when $\gamma_1\ne0$.

The purpose here is to replace this unspecified global unit line by a single fixed Robert construction.

## 2. A fixed auxiliary ideal and a fixed Artin difference

Let $\Psi(z;\Lambda,\Lambda')$ denote Robert's elliptic function with the normalization used by Oukhaba--Viguié §4. The ideal used inside this function will always be the **rational** ideal $(7)$, of norm $49$. Define
$$
V_7=N_{R/L}\Psi(1;\mathfrak p,7^{-1}\mathfrak p).
\tag{976.6}
$$
Since $7$ is prime to $6p$, the ray-class algebraicity theorem gives $\Psi(1;\mathfrak p,7^{-1}\mathfrak p)\in R^\times$. It is a $\mathfrak p$-unit, so $V_7$ is an $L$-unit away from its unique prime over $p$.

Put
$$
\alpha=2+s,\qquad \mathfrak h=(\alpha),\qquad
N\mathfrak h=7,\qquad
\sigma=\operatorname{Frob}_{\mathfrak h}^{\mathrm{arith}}|_L,
\qquad
U_7=V_7^{\sigma-1}=\frac{V_7^\sigma}{V_7}.
\tag{976.7}
$$
The unique prime over $p$ is fixed by $\sigma$, so its valuation cancels in (976.7). All other finite valuations of $V_7$ already vanish. Therefore
$$
U_7\in\mathcal O_L^\times.
\tag{976.8}
$$
This is a single fixed construction for all original primes and both rows. No search for a primitive residue class, no prime-dependent auxiliary ideal, and no omitted exceptional original prime are needed.

The factor $\chi(\sigma)-1$ is always a $p$-unit in this range. Indeed,
$$
\alpha^3=-10+9s,\qquad \alpha^9=6290+513s,
\tag{976.9}
$$
and hence
$$
\alpha^3-\bar\alpha^3=18s,\qquad
\alpha^9-\bar\alpha^9=1026s=54\cdot19s.
\tag{976.10}
$$
The denominators in $(\alpha/\bar\alpha)^a-1$ are powers of $\bar\alpha$, whose norm is seven. All possible prime divisors of the displayed numerators lie over $2,3,19$. Since $p\ge41$, (976.4) and (976.10) prove the assertion.

Also, the Artin symbol of the rational ideal $(7)$ is trivial in $\Delta$, by (976.3). Its Robert regularizer is therefore the constant
$$
N(7)-\chi((7))=49-1=48\in\mathcal O^\times.
\tag{976.11}
$$
The distinction between the rational ideal $(7)$ in (976.6) and the prime ideal $\mathfrak h$ in (976.7) is essential.

## 3. Exact generation of the elliptic-unit character lattice

We record the primary formulas and their conventions. Oukhaba--Viguié use arithmetic ideal Frobenius, denoted by $(\mathfrak g,H_{\mathfrak m}/K)$, and prove/recall in §4, printed p. 155,
$$
\Psi(1;\mathfrak m,\mathfrak g^{-1}\mathfrak m)^{w_{H_{\mathfrak m}}}
=\epsilon_{\mathfrak m}^{\,N\mathfrak g-\operatorname{Frob}_{\mathfrak g}^{\mathrm{arith}}}
\tag{976.12}
$$
when the unit kernel at $\mathfrak m$ is trivial. It is trivial at $\mathfrak m=\mathfrak p$, since $p>3$. Here $\epsilon_{\mathfrak m}$ is their Stark element and $w_{H_{\mathfrak m}}$ the number of roots of unity in the ray class field.

For $x\in L^\times$ define their complex equivariant regulator
$$
\ell_L(x)=\sum_{\tau\in\Delta}-\log|x^\tau|\,\tau^{-1},
\qquad |z|=z\bar z.
\tag{976.13}
$$
Their equation (2.1) and norm compatibility give
$$
\ell_L(N_{R/L}\epsilon_{\mathfrak p})e_\chi
=w_R L'_{\mathfrak p}(0,\chi^{-1})e_\chi.
\tag{976.14}
$$
In (976.14), $L_{\mathfrak p}$ is an ordinary complex Hecke $L$-function, with the Euler factor at $\mathfrak p$ omitted; for our conductor-$\mathfrak p$ character it is already the primitive one. It is not a $p$-adic $L$-function. To verify the inverse in (976.14), apply (976.13) to the norm and sum over all lifts $\tau\in\operatorname{Gal}(R/K)$: the scalar in the $e_\chi$ component is the sum with coefficients $\chi(\tau)^{-1}$, exactly the inverse-character sum in (2.1).

Apply (976.12) with $\mathfrak g=(7)$, take the norm to $L$, apply $\ell_L$, and use (976.11) and (976.14). This yields
$$
\ell_L(V_7)e_\chi=48L'_{\mathfrak p}(0,\chi^{-1})e_\chi,
\qquad
\ell_L(U_7)e_\chi
=48(\chi(\sigma)-1)L'_{\mathfrak p}(0,\chi^{-1})e_\chi.
\tag{976.15}
$$
There is **no unaccounted ray-field root-of-unity denominator** here. The ray field can contain $p$-th roots of unity, so $w_R$ must not be declared a $p$-unit. The same $w_R$ occurs on both sides of the regulator calculation and cancels exactly by (976.14), as an equality over characteristic zero. We do not divide an integral $p$-adic lattice by $w_R$.

Let $C_L$ be Rubin's group of elliptic units and let $E_L$ be Oukhaba--Viguié's group. Their Remark 4.3 says
$$
\mathbb Z[1/m]\otimes C_L=\mathbb Z[1/m]\otimes E_L.
\tag{976.16}
$$
Their Lemma 3.1 gives the complete character lattice
$$
\mathcal O_{(p)}\ell_L(E_L)e_\chi
=\mathcal O_{(p)}F_L L'_{\mathfrak p}(0,\chi^{-1})e_\chi,
\tag{976.17}
$$
where $F_L$ is the group-ring annihilator of $\mu_L$. In our field $\mu_L=\mu_6$: the extension is unramified outside $p$, while adjoining any additional root of unity would either ramify elsewhere or contain $\mu_p$, whose degree $p-1$ exceeds $m$. In particular $6\in F_L$ and six is a unit at $p$. Thus the right side of (976.17) is simply
$\mathcal O_{(p)}L'_{\mathfrak p}(0,\chi^{-1})e_\chi$.

The constants in (976.15) are units by (976.10)--(976.11). The complex regulator is injective on global units modulo roots of unity, and $p\nmid|\mu_L|$. Equal regulator lattices therefore imply equal unit lattices after localization and completion. Using (976.16), we obtain the exact generation statement
$$
\boxed{\quad
e_\chi(\mathcal O\otimes C_L)=\mathcal O\cdot e_\chi U_7.
\quad}
\tag{976.18}
$$
Here a multiplicative abelian group tensored with $\mathcal O$ is written additively in the module notation. Formula (976.18) is stronger than saying that $U_7$ has a nonzero rational regulator.

## 4. From elliptic units to the actual global units: the same character

Rubin's finite Gras theorem applies because $K$ has class number one, $L/K$ is abelian, and
$$
p\nmid w_K[L:K]=6m.
\tag{976.19}
$$
It identifies the $p$-primary character index of elliptic units in all units with the class-group order in the **same character**. Equivalently, after coefficient extension,
$$
\operatorname{length}_{\mathcal O}
e_\chi\bigl(\mathcal O\otimes(\mathcal O_L^\times/C_L)\bigr)
=\operatorname{length}_{\mathcal O}
e_\chi\bigl(\mathcal O\otimes\operatorname{Cl}(L)[p^\infty]\bigr).
\tag{976.20}
$$
One can use Rubin, *The main conjectures of Iwasawa theory for imaginary quadratic fields* (1991), Theorem 3.3. The same finite theorem is explained in his *Euler Systems*, Chapter III §3, Theorem 3.1 and Remark 3.3: the Euler-system divisibility becomes equality by the analytic class number formula. The hypothesis there that a prime above $p$ not split trivially in the character holds because our character is ramified at the unique prime above $p$. No split-prime or ordinary hypothesis is imposed here.

The theorem is sometimes stated for irreducible $\mathbb Z_p$-characters. That formulation suffices: $\chi$ and $\chi^p=\chi^{-1}$ form the same unramified coefficient orbit. Vanishing of the class component in R972 is stable under this coefficient automorphism; applying the stated index theorem and then the faithfully flat unramified extension gives (976.20) for the chosen component. No replacement of $\chi$ by its inverse in the local condition is made.

R972 makes the right side of (976.20) zero. Combining it with (976.18) proves
$$
\boxed{\quad
e_\chi(\mathcal O\otimes\mathcal O_L^\times)
=\mathcal O\cdot e_\chi U_7.
\quad}
\tag{976.21}
$$
This establishes the precise integral global source needed for the local coefficient calculation.

## 5. The actual local logarithm is integral

Fix the local parameter and reciprocity convention from R972. Thus
$$
M=K_{\mathfrak p}(\pi),\quad \pi^{p+1}=-p,
\qquad L_{\mathfrak P}=K_{\mathfrak p}(\rho),\quad
\rho=\pi^3,\quad \rho^m=-p.
\tag{976.22}
$$
The absolute ramification degree of $L_{\mathfrak P}$ is $m=(p+1)/3<p-1$. Consequently the ordinary $p$-adic logarithm is an integral isomorphism
$$
\log:1+\rho\mathcal O_{L_{\mathfrak P}}
\longrightarrow \rho\mathcal O_{L_{\mathfrak P}},
\tag{976.23}
$$
with inverse the ordinary exponential. It is important that (976.23) is asserted in $L_{\mathfrak P}$, not on all principal units of $M$, whose ramification degree is $p+1$.

Remove the Teichmüller lift of the residue of $U_7$, writing $\langle U_7\rangle\in1+\rho\mathcal O_{L_{\mathfrak P}}$. In
$$
\mathcal O_{L_{\mathfrak P}}/p
=\mathbb F_{p^2}[\rho]/(\rho^m),
$$
define the coefficients $B_j\in\mathbb F_{p^2}$ by
$$
\log\langle U_7\rangle
\equiv\sum_{j=1}^{m-1}B_j\rho^j\pmod p.
\tag{976.24}
$$
This is a finite, specified polynomial. If
$X=\langle U_7\rangle-1\bmod p$, it is exactly
$$
\sum_{j=1}^{m-1}B_j\rho^j
=\sum_{t=1}^{m-1}\frac{(-1)^{t+1}}{t}X^t
\quad\text{in }\mathbb F_{p^2}[\rho]/(\rho^m).
\tag{976.25}
$$
For $t<m$, the denominator is a unit because $m<p$. Terms with $m\le t<p$ vanish modulo $\rho^m$. If $v_p(t)=d\ge1$, their valuation is at least $t-md\ge p^d-md\ge p-m=2m-1\ge m$. This proves that all omitted logarithm terms vanish modulo $p$; no informal truncation of a nonintegral logarithm is used.

## 6. Exact comparison with the two Artin--Hasse coordinates

Let $\tau_0:\mathbb F_{p^2}\to k$ be the fixed identity embedding and $\tau_1=\tau_0\circ\operatorname{Frob}_p$. Under
$$
\mathbb F_{p^2}\otimes_{\mathbb F_p}k\simeq k\oplus k,
\qquad x\otimes y\longmapsto(\tau_0(x)y,\tau_1(x)y),
\tag{976.26}
$$
use the two canonical idempotent generators $\lambda_{\tau_0}$ and $\lambda_{\tau_1}$. These are the normalized generators in R972's Artin--Hasse basis
$$
u_0=\epsilon_{\pi^a}(\lambda_{\tau_1}),\qquad
u_1=\epsilon_{\pi^n}(\lambda_{\tau_0}).
\tag{976.27}
$$
The local geometric reciprocity normalization is the one fixed there; globally (976.4) uses arithmetic ideal Frobenius. They are not silently identified.

To compare (976.24) with (976.27), note that
$$
\pi^a=\rho^b,\qquad \pi^n=\rho^{m-b}.
\tag{976.28}
$$
For every $1\le d<m$, the Artin--Hasse series satisfies
$$
\log E_{\rm AH}(c\rho^d)
=\sum_{t\ge0}\frac{c^{p^t}\rho^{dp^t}}{p^t}
\equiv c\rho^d\pmod p.
\tag{976.29}
$$
Indeed all terms with $t\ge1$ have $\rho$-valuation at least $p-m=2m-1\ge m$. Thus there is no normalization scalar between the coefficient in (976.24) and its Artin--Hasse coordinate in the canonical idempotent basis.

The $\chi$-projector selects exactly the $\tau_1$ coefficient of degree $b$ and the $\tau_0$ coefficient of degree $m-b$. Explicitly, if $g\pi=\zeta\pi$, then $\chi(g)=\zeta^{-a}$. On the $\tau_0$ factor a monomial $\rho^j$ has eigenvalue $\zeta^{3j}$; on the $\tau_1$ factor it has eigenvalue $\zeta^{3jp}=\zeta^{-3j}$. In the range $1\le j<m$, the required exponents are uniquely $j=m-b$ and $j=b$, respectively. Orthogonality in (976.5) gives scalar one on these monomials, so there is no surviving $1/m$ factor.

It follows that the image of the actual generator $e_\chi U_7$ has coordinates
$$
\boxed{\quad
\gamma_0=\tau_1(B_b),\qquad
\gamma_1=\tau_0(B_{m-b}).
\quad}
\tag{976.30}
$$
Since $\tau_0$ is the chosen identity and $\tau_1$ Frobenius, these can also be written $\gamma_0=B_b^p$, $\gamma_1=B_{m-b}$ in $k$.

Using (976.21) and the precise R972 global annihilator line, we therefore obtain
$$
\boxed{\quad B_b\ne0,\qquad
\text{the original complete trace is nonzero}
\iff B_{m-b}\ne0.\quad}
\tag{976.31}
$$
In the two rows the unknown coefficient is respectively $B_{m-1}$ and $B_{m-3}$, while the already controlled coefficient is respectively $B_1$ and $B_3$.

## 7. Scope and next mathematical input

Equations (976.6)--(976.7) specify the global source by one fixed Robert function, a genuine ray-to-ring-class norm, and a fixed arithmetic Artin difference. Equation (976.25) specifies the remaining local scalar by a finite polynomial operation on this actual unit. The class-group and character identifications are part of the proof, rather than an arbitrary choice of a locally nonzero unit.

No step proves $B_{m-b}\ne0$. An ordinary Euler-system interpolation statement, a fixed low-weight Scholl unit, or a formal Frobenius congruence of individual infinite lattice summands would not supply that conclusion. The new concrete question is to evaluate the indicated finite logarithm coefficient of (976.7), or compare it with the balanced coefficient of R974 by an actual integral reciprocity formula. The source in (976.7) is fixed independently of $p$, though its evaluation, norm field, and target coefficient vary with $p$.

Changing the local Kummer root $\rho$ rescales individual coefficients by units and preserves their zero/nonzero status. For the exact coordinate equalities in (976.30), retain the fixed root and embeddings of R972. Likewise, changing arithmetic to geometric ideal Artin without changing (976.4)--(976.5) would invert the character and is not permitted.

## 8. Primary sources

1. Hassan Oukhaba and Stéphane Viguié, *On the Gras Conjecture for Imaginary Quadratic Fields*, Canadian Mathematical Bulletin **56** (2013), 148--160, DOI 10.4153/CMB-2011-173-1. The formulas used are (2.1), Lemma 3.1, the Robert function identity in §4 (printed p. 155), and Remark 4.3. Their introduction states the earlier Rubin theorem for $p\nmid w_K[L:K]$, which is exactly our range. [Publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf).
2. Karl Rubin, *The “main conjectures” of Iwasawa theory for imaginary quadratic fields*, Inventiones Mathematicae **103** (1991), 25--68, Theorem 3.3; DOI 10.1007/BF01239508. We use its finite Gras assertion, not an ordinary main conjecture.
3. Karl Rubin, *Euler Systems*, Annals of Mathematics Studies **147** (2000), Chapter III §3, Theorem 3.1 and Remark 3.3, printed pp. 39--40. [Author lecture-book PDF](https://swc-math.github.io/aws/1999/99RubinES.pdf).
