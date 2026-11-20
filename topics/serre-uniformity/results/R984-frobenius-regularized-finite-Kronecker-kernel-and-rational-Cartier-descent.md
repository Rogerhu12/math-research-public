# R984 — A genuine Frobenius-regularized finite Kronecker kernel and rational Cartier descent

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b. Authoring agent: literature_frontier; independently reviewed by root.

**Status: proved finite integrality and an exact coefficient formula.** The original balanced coefficient can be extracted from a finite integral Kronecker kernel obtained using a genuine one-step Frobenius basis. Its reduction can, in turn, be computed using a rational Cartier primitive on the original elliptic curve. The integral remainder in the Frobenius decomposition is retained. No nonvanishing, Hecke eigenspace identification, or mixed-to-pure Hurwitz congruence is asserted.

The input is the published formal-group theorem of Guerzhoy (2025), together with the algebraic connection functions of Bannai–Kobayashi–Tsuji (2010). The integrality needed for the connection functions is proved below, rather than inferred just from rationality over the fraction field. All calculations are symbolic.

## 1. Original curve, coefficients, and the exact Frobenius basis

Keep the two rows of R974/R978:
$$
p\ge41,\quad p\equiv2,5\pmod9,\qquad
(r,n)=
\begin{cases}
(2,p-2),&p\equiv11\pmod{12},\\
(8,p-8),&p\equiv5\pmod{12}.
\end{cases}
\tag{984.1}
$$
Thus $n\equiv3\pmod6$ and $3\le n\le p-2$. Work on the fixed source
$$
E_+:\ y^2=x^3+1,\qquad
\omega=\frac{dx}{2y},\qquad
g_2=0,\quad g_3=-4,\qquad t=-x/y.
\tag{984.2}
$$
Let $A=W(\mathbb F_{p^2})$, $F=\operatorname{Frac}(A)$, and let $\varphi$ denote arithmetic Frobenius on coefficients. Write
$$
\omega=f(t)\,dt,\qquad
f=\frac{x^3+1}{x^3-2}\in F(E_+),\qquad
l_E(t)=\int_0^t\omega=t+\cdots.
\tag{984.3}
$$
The rational expression for $f$ follows by differentiating $t=-x/y$ and using $2y\,dy=3x^2dx$. Its power-series expansion at the origin is integral.

Let $\zeta(z)=\sigma'(z)/\sigma(z)$ for the same Weierstrass sigma function as R978. Its normalization is
$$
\zeta(z)=\frac1z-\sum_{k\ge4}\mathcal G_k z^{k-1}.
\tag{984.4}
$$
Guerzhoy, equation (4), Proposition 1, Corollary 1, and Theorem 1, gives unique coefficients $\lambda,\mu\in A$ such that
$$
\zeta(l_E(t))-\lambda l_E(t)
-\frac{\mu}{p}l_E^\varphi(t^p)
\in t^{-1}+A[[t]].
\tag{984.5}
$$
The two logarithms in this formula represent the actual integral crystalline basis, and $\lambda,\mu$ are unchanged by a strict integral isomorphism of formal groups. In the CM case his Theorem 1 identifies $\lambda$ with the algebraic complex weight-two value. At the source (984.2), the $\mu_6$ symmetry makes that value zero. Hence put
$$
R(t)=\zeta(l_E(t))-\frac{\mu}{p}l_E^\varphi(t^p)
\in t^{-1}+tA[[t]].
\tag{984.6}
$$
The zero constant coefficient follows also from oddness: $t$, $l_E(t)$, $\zeta(l_E(t))$, and $l_E^\varphi(t^p)$ are all odd. We do not set the regular part of $R$ equal to zero.

The coefficient $\mu$ has a fixed normalization. Let
$$
B_p=E_{p+1}(E_+,\omega),\qquad \beta=\overline B_p/12\in\mathbb F_p^\times
\tag{984.7}
$$
as in R980. In R978's strict integral Lubin–Tate coordinate $T$, put
$$
t=g(T),\qquad g'(0)=1,\qquad
l_{\rm LT}(T)=l_E(g(T))=T+O(T^{p^2}).
\tag{984.8}
$$
Apply strict invariance in (984.5) and compare the coefficient of $T^p$. The pole $1/l_{\rm LT}(T)$ first differs from $1/T$ in degree $p^2-2>p$. Thus
$$
-\mathcal G_{p+1}-\mu/p\in A.
$$
Robert's formula $pS_{p+1}\equiv E_{p+1}/12$, together with $S_k(E_+,\omega)=\mathcal G_k$ from R980, gives
$$
\boxed{\quad \overline\mu=-\beta.\quad}
\tag{984.9}
$$
This is the sign and scale of the one-step Frobenius term. The displayed correction in (984.6) contains $1/p$; it is not an ordinary integral two-variable theta measure.

## 2. Connection functions on the integral model

Since the weight-two CM value is zero, the reduced theta function here is exactly $\sigma$. Define
$$
\Theta(z,W)=\frac{\sigma(z+W)}{\sigma(z)\sigma(W)},\qquad
\Xi(z,W)=e^{-\zeta(z)W}\Theta(z,W)
=\sum_{j\ge0}L_j(z)W^{j-1}.
\tag{984.10}
$$
These are the connection functions in Bannai–Kobayashi–Tsuji, Definitions 1.5–1.6. In particular $L_0=1$ and $L_1=0$.

We need the following integral refinement at small indices:
$$
\boxed{\quad
L_j\in A[x,y]\subset F(E_+),\qquad 0\le j\le p-2.
\quad}
\tag{984.11}
$$
Here the equality means the rational function on $E_+$; its only possible pole is at the origin. To prove it directly, Taylor-expand $\log\sigma(z+W)$ and use $\zeta'=-x$:
$$
\Xi(z,W)=W^{-1}\exp\left(
-\sum_{k\ge2}\frac{D^{k-2}x}{k!}W^k
+\sum_{k\ge4}\frac{\mathcal G_k}{k}W^k
\right),
\qquad D=\frac{d}{dz}.
\tag{984.12}
$$
In the coordinate $Y=2y$, the derivation satisfies
$$
Dx=Y,\qquad DY=6x^2-g_2/2.
\tag{984.13}
$$
Thus every $D^{k-2}x$ is a polynomial over $\mathbb Z[1/2,g_2,g_3]$ in $x,Y$.

For $4\le k\le p-2$, the coefficients $\mathcal G_k$ are $p$-integral. One can see this universally from Robert's formula
$S_k=2G_k^{\rm Rob}/(k-1)!$: its Fourier coefficients are $p$-integral, since $k!$ is a unit and the Bernoulli denominator has no $p$ in this range. The level-one integral $q$-expansion principle then places $S_k$ in $\mathbb Z_p[E_4,E_6]$. Evaluating at the fixed integral model and using R980 proves the claim. Odd weights contribute zero.

To compute $L_j$ for $j\le p-2$ from (984.12), only $k\le j$ occur. Every $k!$, $k$, and exponential factorial needed is therefore a unit. This proves (984.11) on the integral model itself. It also proves that $L_j$ has pole order at most $j$ at the origin. No assertion about an unrestricted integral series in all powers of $W$ is needed.

## 3. A finite integral kernel retaining every required original coefficient

Set $M=p-2$ and retain Laurent coefficients in $W$ through $W^{M-1}$. Define the actual-parameter kernel
$$
\mathcal K_\mu(t,W)
=e^{R(t)W}\Xi(l_E(t),W).
\tag{984.14}
$$
For each $0\le j\le M$, the coefficient of $W^{j-1}$ is
$$
\sum_{h=0}^j\frac{R(t)^{j-h}}{(j-h)!}L_h(t)\in A((t)).
\tag{984.15}
$$
The factorial bound $j<p$ is essential. Equations (984.6) and (984.11) establish the integrality in (984.15).

There is also an exact identity over $F$:
$$
\mathcal K_\mu(t,W)=
\exp\left(-\frac{\mu}{p}l_E^\varphi(t^p)W\right)
\Theta(l_E(t),W).
\tag{984.16}
$$
In particular, $\mathcal K_\mu$ is not identified with $\Theta$ as a full series. The exponential correction in (984.16) starts in $t^pW$.

The theta function has just the simple poles
$$
\Theta(z,W)-z^{-1}-W^{-1}\in F[[z,W]].
\tag{984.17}
$$
Using (984.16), multiplication by the correction cannot introduce another negative power of $t$. Consequently the integral Laurent coefficients already proved in (984.15) satisfy
$$
\boxed{\quad
\mathcal K_\mu(t,W)-t^{-1}-W^{-1}
\in A[[t,W]]\pmod{W^M}.
\quad}
\tag{984.18}
$$
This pole assertion is made for the product (984.14), not for its individual summands, which can have higher poles.

Now substitute the original strict integral coordinate $t=g(T)$ from (984.8). The same finite integrality and simple-pole assertion hold in $T$. For every $i\le p-2$, the coefficient of $T^i$ is unaffected by the exponential correction in (984.16): that correction starts in $T^pW$, while the theta factor has no power of $T$ below $-1$.

The correction after this substitution is still $l_E^\varphi(g(T)^p)$ in (984.16). It is not silently replaced by $l_{\rm LT}^\varphi(T^p)=l_E^\varphi(g^\varphi(T^p))$. Strict invariance of $\lambda,\mu$ preserves their classes modulo integral series; it does not identify these two integral remainders after division by $p$. The coefficient bound above is what makes the stated low rectangle unaffected.

Moreover replacing $l_{\rm LT}(T)$ by $T$ changes the simple pole only in degree at least $p^2-2$, and changes regular terms only in still higher degree. Therefore, if
$$
c_n^+=[z^nW^{n-1}]\Theta(z,W),
\tag{984.19}
$$
then
$$
\boxed{\quad
c_n^+=[T^nW^{n-1}]\mathcal K_\mu(g(T),W)\in A,
\qquad n=p-r.
\quad}
\tag{984.20}
$$
This is an equality in characteristic zero before reduction, not just a congruence or a unit criterion. It keeps the original differential and the original sigma phase. For comparison with the $g_3=+4$ convention of R974/R975, R979 gives $c_n^+=-c_n^-$ in the two rows; no such phase change is made inside (984.14).

## 4. A rational Cartier primitive for the reduction of the regularized zeta function

Write $k=\mathbb F_{p^2}$ and reduce the model and its rational functions modulo $p$. Differentiate (984.6). Since
$$
\frac{d}{dt}\left(\frac1p l_E^\varphi(t^p)\right)
=t^{p-1}f^\varphi(t^p),
$$
and $f^\varphi(t^p)\equiv f(t)^p\pmod p$, equations (984.3) and (984.9) give
$$
d\overline R=\nu,\qquad
\nu=-x\omega+\beta\,t^{p-1}f^p\,dt
\in\Omega^1_{k(E_+)/k}.
\tag{984.21}
$$
All terms of $\nu$ are genuine rational functions or differentials on the original curve. In particular the use of $f^p$ is a reduction of coefficient Frobenius and substitution, not a change of the original parameter.

The rational differential $\nu$ has Cartier operator zero. Indeed its Laurent expansion at the origin is the derivative of $\overline R$, whose Cartier operator vanishes. Laurent expansion is injective on rational differentials and is compatible with Cartier.

For completeness, existence of a rational primitive needs no degeneration or lifting assertion. The rational function $t$ is a separating parameter, so it is a $p$-basis of $k(E_+)$. Write uniquely
$$
\nu=\left(\sum_{i=0}^{p-1}u_i^p t^i\right)dt,
\qquad u_i\in k(E_+).
$$
The Cartier-zero condition is $u_{p-1}=0$, and hence
$$
J_0=\sum_{i=0}^{p-2}\frac{u_i^p}{i+1}t^{i+1}\in k(E_+)
\quad\text{satisfies}\quad dJ_0=\nu.
\tag{984.22}
$$
This also specifies a concrete rational operation producing a primitive.

Normalize a primitive $J$ at the origin as follows. The Laurent expansion of $\overline R-J_0$ has derivative zero. Thus every negative exponent in this difference is a multiple of $p$, except that the desired pole $t^{-1}$ of $\overline R$ must already be the same pole of $J_0$. Remove the finitely many extra negative terms of $J_0$ using rational $p$th powers $a\,t^{-mp}$, and then remove its constant term. These changes have zero derivative. They may introduce poles at other zeros of $t$, which are permitted. This yields
$$
J=t^{-1}+t\,k[[t]]\quad\text{at the origin},\qquad dJ=\nu.
\tag{984.23}
$$
The normalization and perfectness of $k$ imply an exact local identity
$$
\boxed{\quad
\overline R(t)-J(t)=h(t)^p,\qquad h(t)\in t\,k[[t]].
\quad}
\tag{984.24}
$$
The right side is retained and can be nonzero. The zero constant term in (984.23) matters: without it the difference need not start in degree $p$.

## 5. Exact rational formula for the original finite coefficient

Reduce the finite connection functions and the strict coordinate modulo $p$, denoting them by $\overline L_j$ and $\overline g$. Using finite exponentials with factorials below $p$, define
$$
\mathcal K_J(T,W)
=\exp\bigl(J(\overline g(T))W\bigr)
\sum_{j=0}^{M}\overline L_j(\overline g(T))W^{j-1}
\pmod{W^M}.
\tag{984.25}
$$
The notation $\overline L_j(\overline g(T))$ means evaluation of the rational function on the formal point of $E_+$ with parameter $t=\overline g(T)$.

From (984.24) and the already integral kernel,
$$
\mathcal K_J(T,W)
=\exp\bigl(-h(\overline g(T))^pW\bigr)
\overline{\mathcal K_\mu(g(T),W)}
\pmod{W^M}.
\tag{984.26}
$$
The first factor differs from one only in terms of $T$-degree at least $p$. The second factor has only a simple $T$-pole, by (984.18). Thus every coefficient of $T^i$ with $i\le p-2$ is unchanged. In particular
$$
\boxed{\quad
\overline{c_n^+}
=[T^n]\sum_{j=0}^{n}
\frac{J(\overline g(T))^{\,n-j}}{(n-j)!}
\overline L_j(\overline g(T)),
\qquad n=p-r.
\quad}
\tag{984.27}
$$
All factorials in (984.27) are units, and all functions $J,L_j$ are rational on the same original curve. The required $\overline g$ is the reduction of the strict integral isomorphism already fixed in R978. Formula (984.27) is independent of the choice of normalized rational primitive: changing $J$ changes it by a regular $p$th power with zero constant term, and the same argument proves that the coefficient is unchanged.

Equivalently, before substituting $\overline g$, the finite kernel descends from the true integral Frobenius decomposition to a rational Cartier primitive, modulo an explicitly controlled $p$th-power factor. This is the precise sense of descent used here.

## 6. Scope for the remaining comparison

The formula depends on the actual rational differential (984.21) and the genuine Poincare connection functions. It is therefore more specific than assigning a finite-field character to a mixed coefficient. It does not remove the rational primitive $J$, replace its regular part by zero, or identify the two different Robert mirror pairs of R980.

In particular, the following assertions remain unproved here:

- a global Hecke eigenvector completion of this finite kernel in Robert's lattice $M[E_{p-1}/p]$;
- an equality between (984.27) and a specified pure coefficient $\mathcal G_{k^*}$;
- nonvanishing of (984.27), of the original high trace, or of a same-label $Q'$.

The original $p$-Frobenius coefficient has been calibrated as $\overline\mu=-B_p/12$, while its integral remainder has been replaced only by a rational representative modulo regular $p$th powers. Any further Hecke or mixed-to-pure comparison must respect those two facts.

## Sources

1. P. Guerzhoy, *On the p-adic values of the weight two Eisenstein series for supersingular primes*, Research in the Mathematical Sciences **12**, article 64 (2025), published 5 September 2025, DOI [10.1007/s40687-025-00540-8](https://doi.org/10.1007/s40687-025-00540-8). Equation (4), Proposition 1, Corollary 1, equation (14), and Theorem 1. The [author manuscript, arXiv:2403.02592v2](https://arxiv.org/pdf/2403.02592), dated 20 July 2025, contains these statements on PDF pp. 3–4 and 9–12. The theorem requires good reduction and $p$ prime to the CM discriminant and conductor; these conditions hold for (984.2).
2. Kenichi Bannai, Shinichi Kobayashi, Takeshi Tsuji, *On the de Rham and p-adic realizations of the elliptic polylogarithm for CM elliptic curves*, Annales scientifiques de l'École Normale Supérieure **43** (2010), 185–234, Definitions 1.5–1.6, printed p. 191, for $\Xi$ and its rational connection functions. [Published primary PDF](https://www.numdam.org/item/10.24033/asens.2119.pdf). The integral small-index strengthening needed here is proved in Section 2.
3. Gilles Robert, *Congruences entre séries d'Eisenstein, dans le cas supersingulier*, Inventiones Mathematicae **61** (1980), 103–158: §1.3 integral $q$-expansion principle; §1.4(2) for $S_k$; §5.3, Proposition 8(ii), for $pS_{p+1}\equiv E_{p+1}/12$. [Public scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0061/LOG_0012.pdf).
4. R974/R975/R979 for the original balanced coefficient and its phase; R978 for the strict integral Lubin–Tate coordinate and the original source; R980 for the exact $S_k=\mathcal G_k$ convention and $B_p$.
