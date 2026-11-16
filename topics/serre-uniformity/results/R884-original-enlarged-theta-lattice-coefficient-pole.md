# R884 — Exact first-pole obstruction on the original enlarged theta lattice

Date: 2026-11-16. Status: proved. Each original critical sigma coefficient functional is nonintegral on the genuine lattice $H^0(E,O(6pO))$, even after restricting to its original $\mu_6$ character. This statement concerns the enlarged lattice; it does not imply nonintegrality on the original six-dimensional source or failure of the same-label criterion.

## 1. Original functional and explicit integral sections

Use exactly the equation, differential, and $c=0$ sigma normalization of R697/R702:
$$
E:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad
p=6N+5\ge41.
\tag{884.1}
$$
Let $R=W(\mathbf F_{p^2})$, and let $s_{6p}$ be the canonical section of $O(6pO)$ with divisor $6pO$. Thus
$$
\mathcal H=H^0(E_R,O(6pO))
=\{R_0s_{6p}:\operatorname{div}_\infty(R_0)\le6pO\}
$$
is the same integral theta lattice used in R878/R881. The letter $R_0$ denotes a rational function, and does not denote the coefficient ring.

For a nonnegative integer $n$, define a characteristic-zero linear functional by
$$
\lambda_n(R_0s_{6p})=[z^n]\bigl(R_0(z)\sigma(z)^6\bigr).
\tag{884.2}
$$
This is a finite coefficient extraction from a Laurent series. It is the actual functional obtained by dividing the enlarged section expression by $\sigma^{6p-6}$.

The original critical functionals are
$$
\lambda_{6i+4}(x s_{6p})=f_i,\qquad
\lambda_{6j+1}(-xy s_{6p})=g_j,
\qquad 0\le i,j\le N-1.
\tag{884.3}
$$
They use ordinary power-series coefficients as in R770, with no factorial inserted.

For $0\le i,j\le N-1$, set
$$
a_i=3(N-i)+4,\qquad a_j=3(N-j)+4,
$$
$$
v_i=x^{a_i}s_{6p},\qquad
w_j=-x^{a_j}y\,s_{6p}.
\tag{884.4}
$$
These are genuine integral global sections. Indeed
$$
7\le a_i,a_j\le3N+4,\qquad
2a_i\le p+3<6p,\qquad
2a_j+3\le p+6<6p.
\tag{884.5}
$$
All their coefficients in the original integral Weierstrass equation are integral.

Let $B$ be the original nonzero Hasse/Cartier scalar
$$
B=(-1)^{N+1}\binom{3N+2}{2N+1}\pmod p.
\tag{884.6}
$$
The exact assertion is
$$
\boxed{
p\lambda_{6i+4}(v_i)\equiv-6B,\qquad
p\lambda_{6j+1}(w_j)\equiv-6B\pmod p.
}
\tag{884.7}
$$
In particular both values in (884.7) have $p$-adic valuation exactly $-1$.

## 2. Finite first-pole extraction

Retain the original algebraic coordinate and rational series of R702:
$$
u=x^{-1/2},\qquad z=uZ(u^6),\qquad
\sigma^6=u^6T(u^6),\qquad
y=-u^{-3}\sqrt{1-u^6}.
\tag{884.8}
$$
The branch of $u$ has $u=z+O(z^7)$, and the square root has constant term one. R702 (702.5)--(702.12) proves, with $M=2N+2$,
$$
pT(w)\equiv-6B\,w^{N+1}Z(w)T_0(w)
\pmod{p,w^M},
\qquad Z(0)=T_0(0)=1.
\tag{884.9}
$$
The left side is integral in this finite truncation. The coordinate $u(z)$, its unit quotient $u(z)/z$, and the required inverse powers are integral through every degree used here. This is exactly the finite coordinate-integrality assertion in R702 §2; no infinite sigma series is reduced modulo $p$.

Put $n=6i+4$. The definition of $a_i$ gives
$$
6-2a_i=n-p-1.
$$
Hence, through the coefficient of degree $n$,
$$
p\,x^{a_i}\sigma^6
=p\,u^{n-p-1}T(u^6)
\equiv-6B\,u^nZ(u^6)T_0(u^6)\pmod p.
\tag{884.10}
$$
The omitted $w^M$ terms have $u$-degree at least
$$
n-p-1+6M=n+p+1>n.
$$
Thus no omitted term can enter the coefficient being extracted, even though the prefactor has a negative exponent. The coefficient of $z^n$ on the right of (884.10) is $-6B$, since $u(z)=z+\cdots$ and both remaining factors have constant term one. This proves the first assertion of (884.7).

For $n=6j+1$ one has
$$
3-2a_j=n-p-1.
$$
The same finite calculation, now retaining the actual $y$ factor, gives
$$
\begin{aligned}
p(-x^{a_j}y)\sigma^6
&=p\,u^{n-p-1}\sqrt{1-u^6}\,T(u^6)\\
&\equiv-6B\,u^n\sqrt{1-u^6}\,
  Z(u^6)T_0(u^6)\pmod p.
\end{aligned}
\tag{884.11}
$$
Its omitted terms begin after degree $n$ by the identical bound. The square root has constant term one, so the extracted coefficient is again $-6B$. This proves (884.7), including integrality after multiplication by exactly one $p$.

Because $p\ge41$ and $B\ne0$, the residue $-6B$ is nonzero. Thus the failure of integrality is an equality of valuations, not merely an uncontrolled possible denominator.

## 3. The original tame characters are retained

For a sixth root of unity $\epsilon$, the original $c=0$ normalization has
$$
x(\epsilon z)=\epsilon^{-2}x(z),\qquad
y(\epsilon z)=\epsilon^{-3}y(z),\qquad
\sigma(\epsilon z)=\epsilon\sigma(z).
$$
Every exponent $a_i,a_j$ in (884.4) is $1$ modulo three. It follows that
$$
x^{a_i}\sigma^6\ \text{has character }\epsilon^4,\qquad
-x^{a_j}y\sigma^6\ \text{has character }\epsilon.
\tag{884.12}
$$
These are exactly the respective characters of the original $F=x\sigma^6$ and $G=-xy\sigma^6$. The counterexamples do not result from adding a section in an unrelated tame character.

This $\mu_6$ character statement is distinct from identifying a character of the full norm-one torus in R881. No primitive norm-one label is assigned to (884.4).

## 4. Consequence and precise boundary

The integral action and idempotents of R881 do not make $\lambda_{6i+4}$ or $\lambda_{6j+1}$ integral on the entire true theta-section lattice: (884.7) gives an explicit counterexample for every original critical index. Therefore integrality of a theta operator alone cannot justify applying one of these functionals modulo $p$ to an arbitrary enlarged-space image.

The restriction to the original source remains different. The six-dimensional subspace is obtained by multiplying $H^0(E,O(6O))$ by the canonical section of $O((6p-6)O)$, and R702/R770 already prove the needed first-block integrality on the original sections in (884.3). The sections (884.4) have poles exceeding six and are not members of that source subspace.

In particular this result proves neither that
$\lambda_n(\mathsf e_a(x s_{6p}))$ or
$\lambda_n(\mathsf e_a(-xy s_{6p}))$ is nonintegral for a specified $a$,
nor that its first-pole contribution survives the full original primitive projection. A cancellation on those specific projected source lattices is a separate question. The original same-$h$ product, the Legendre factor, and the modular-quotient normal coefficient remain open.

## Dependencies

- [R702](R702-first-pole-block-and-uniform-shifted-units.md), especially (702.5)--(702.15): the original finite first-pole identity and the precise coordinate-integrality range.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md): the original $f_i,g_j$ and critical indices.
- [R878](R878-original-finite-theta-action-and-section-projections.md) and [R881](R881-original-integral-theta-lift-and-cuspidal-test-vector.md): the actual enlarged theta lattice and its integral torus action.

This is a paper consequence of the existing all-prime first-pole identity. No new mathematical computation or prime scan was executed.
