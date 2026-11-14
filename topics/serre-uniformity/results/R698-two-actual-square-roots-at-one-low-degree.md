# R698 — The two actual square roots at one common low degree

Date: 2026-11-14. Status: **proved reduction**. All-prime nonvanishing remains open.

## Statement

Let $p\ge41$ be prime with $p\equiv5\pmod6$, and put

$$
N=(p-5)/6,\qquad \ell_2=2^{(p-1)/2}\in\{\pm1\}\subset\mathbf F_p.
\tag{698.1}
$$

Define fixed rational power series

$$
\begin{aligned}
C(w)&=(1-w)^{-1/2}=\sum_{j\ge0}c_jw^j,
&c_j&=\binom{2j}{j}/4^j,\\
Z(w)&=\sum_{j\ge0}\frac{c_j}{6j+1}w^j,\\
H(w)&=\sum_{j\ge0}h_jw^j,
&h_0&=1,\quad h_j=\frac{6j-4}{6j-1}h_{j-1},\\
T(w)&=\exp\left(\sum_{j\ge1}\frac{h_j}{j}w^j\right).
\end{aligned}
\tag{698.2}
$$

For the actual arithmetic square roots $A_k$ of R697, one has

$$
\boxed{
A_p\equiv-\ell_2[w^N]\,T(w)C(w),\qquad
A_{p-3}\equiv\frac23\ell_2[w^N]\,T(w)Z(w)^3\pmod p.
}
\tag{698.3}
$$

Every coefficient on the right through degree $N$ is $p$-integral.
The two expressions are at the same index and use the same fixed series
$T$.  In particular R697 becomes

$$
\boxed{
C_p\equiv-3\bigl([w^N]TC\bigr)^2,\qquad
C_{p-3}\equiv-\frac43\bigl([w^N]TZ^3\bigr)^2\pmod p.
}
\tag{698.4}
$$

Thus the original remaining first-term question is precisely the
nonvanishing of both coefficients in (698.3), for
$p\equiv2,5\pmod9$.  This result does not prove that nonvanishing.

## 1. The original sigma function in the algebraic parameter

Work first over $\mathbf Q$.  Near $O$ on the original curve let

$$
u=x^{-1/2},\qquad w=u^6,
\qquad x=u^{-2},\quad y=-u^{-3}\sqrt{1-u^6}.
\tag{698.5}
$$

The branch is fixed by $u=z+O(z^7)$, so

$$
\frac{dz}{du}=C(u^6),\qquad z=uZ(u^6),\qquad
Z+6wZ'=C.
\tag{698.6}
$$

Let $E=D_z\log\sigma$ be the actual original Weierstrass zeta
function, with $D_zE=-x$ and pole $z^{-1}$ at the origin.  Integration
in $u$ gives

$$
E(u)=u^{-1}W(u^6),\qquad
W(w)=1-\sum_{j\ge1}\frac{c_j}{6j-1}w^j,
\qquad 6wW'=W-C.
\tag{698.7}
$$

There is no arbitrary constant: both the actual zeta function and the
displayed primitive are odd, and have the specified pole.  Therefore

$$
\frac{d}{du}\log\frac{\sigma(uZ(u^6))}{u}
=\frac{C(u^6)W(u^6)-1}{u}.
\tag{698.8}
$$

Put $H=CW$.  Using $2(1-w)C'=C$ and (698.7), one finds

$$
6w(1-w)H'=(1+2w)H-1.
\tag{698.9}
$$

Comparing coefficients gives exactly the recurrence for $h_j$ in
(698.2).  Integrating (698.8) and using $\sigma(z)/z\to1$ gives the
identity of formal series

$$
\boxed{\sigma(uZ(u^6))^6=u^6T(u^6).}
\tag{698.10}
$$

In particular the two original sections from R697 are

$$
x\sigma^6=u^4T(w),\qquad
-xy\sigma^6=uJ(w),\quad J(w)=T(w)\sqrt{1-w}.
\tag{698.11}
$$

This uses the original sigma function and ordinary formal coordinate;
no modified divided-power series is substituted for it.

## 2. The complete integrality range

For $0\le j\le N$ the denominators entering $C,Z,H,T$ are products of
powers of two and the integers

$$
j,\qquad 6j+1,\qquad 6j-1,
\tag{698.12}
$$

as relevant.  All nonzero ones are prime to $p$: indeed
$6N+1=p-4$, $6N-1=p-6$, and $N<p$.
The exponential defining $T$ can equivalently be calculated by

$$
T_0=1,\qquad nT_n=\sum_{j=1}^n h_jT_{n-j}.
\tag{698.13}
$$

Thus every division used through degree $N$ is a unit division.  Notice
the boundary: $h_{N+1}$ has a denominator $6(N+1)-1=p$ and its
numerator is a unit.  The proof does not reduce $H$ or $T$ as unrestricted
infinite power series.  All subsequent characteristic-$p$ manipulations
take place in $\mathbf F_p[w]/(w^{N+1})$.

## 3. Lagrange inversion for the first root

For $m=6N+4=p-1$, Lagrange inversion applied to $z=uZ(u^6)$ gives

$$
[z^m](x\sigma^6)
=\frac1m[w^N](4T+6wT')Z^{-m}.
\tag{698.14}
$$

In the valid finite ring, $Z^p\equiv1\pmod{w^{N+1}}$, so
$Z^{-(p-1)}\equiv Z$.  If $[w^N]$ denotes the coefficient functional,

$$
\begin{aligned}
[w^N](4T+6wT')Z
&=(6N+4)[w^N]TZ-6[w^N]wTZ'\\
&\equiv-[w^N]T(Z+6wZ')\\
&=-[w^N]TC.
\end{aligned}
\tag{698.15}
$$

Now R697 uses $A_p=2^{-m/2}m![z^m](x\sigma^6)$.
Wilson's theorem gives $(m-1)!=(p-2)!\equiv1$, while
$2^{-m/2}=\ell_2$.  Multiplying (698.14)--(698.15) by the exact
factor in R697 proves the first formula in (698.3).

## 4. Lagrange inversion for the second root

For $m=6N+1=p-4$, the second expression in (698.11) gives

$$
[z^m](-xy\sigma^6)
=\frac1m[w^N](J+6wJ')Z^{-m}.
\tag{698.16}
$$

The same finite Frobenius calculation gives $Z^{-m}\equiv Z^4$.
Then

$$
\begin{aligned}
[w^N](J+6wJ')Z^4
&=(6N+1)[w^N]JZ^4-24[w^N]wJZ^3Z'\\
&\equiv-4[w^N]JZ^3(Z+6wZ')\\
&=-4[w^N]TZ^3,
\end{aligned}
\tag{698.17}
$$

because $JC=T$.  In R697 the prefactor is
$2^{-(m-1)/2}(m-1)!$.  Wilson's theorem gives

$$
(p-5)!\equiv-1/24,\qquad
2^{-(p-5)/2}=4\ell_2.
\tag{698.18}
$$

Combining (698.16)--(698.18) gives
$(-\ell_2/6)(-4)[w^N]TZ^3$, proving the second formula in (698.3).
Equation (698.4) now follows from R697(697.5).

## 5. Exact scalar implementation and remaining boundary

The recurrence (698.13), a truncated cubic product for $Z^3$, and two
finite convolutions compute the two target coefficients using
$O(N^2)$ scalar field operations and $O(N)$ storage.  No algebraic
extension, modulus-$p^2$ calculation, or division by $p$ is required.
All denominator units are proved in section 2.

The executable `R698_scalar_square_roots.py` records every coefficient
of $C,Z,H,T$ through $N$ and every summand in the two final convolutions.
The two small checks below agree with the independently computed ordinary
Bell derivatives of R697 and the original Cartier computations.  They
are normalization checks, not evidence promoted to a uniform theorem.

| $p$ | $N$ | $[w^N]TC$ | $[w^N]TZ^3$ | $A_p$ | $A_{p-3}$ | $C_p$ | $C_{p-3}$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 41 | 6 | 31 | 36 | 10 | 24 | 28 | 35 |
| 47 | 7 | 45 | 45 | 2 | 30 | 35 | 26 |

The complete certificates are `R698-prime41.json` and
`R698-prime47.json`; each contains its executable's SHA256 digest.

This reduction makes the unit problem elementary to state, but does not
remove it.  In particular positivity of the rational coefficients in
characteristic zero is not a nonvanishing argument modulo $p$, and
the integral truncation cannot be extended past the displayed
$h_{N+1}$ boundary by reducing a denominator $p$.

## Dependencies

- R697: actual arithmetic square roots, original sigma-six sections,
  and the exact factorial and power-of-two normalization.
- Formal Lagrange inversion and the original Weierstrass identity
  $D_z^2\log\sigma=-x$, applied with the complete integral cutoff.


## Fast exact window implementation

`R698_fast_scalar_window.py` computes the same finite series by polynomial Newton exponentiation. If $g$ equals $\exp(f)$ modulo $w^r$, then $g(1+f-\log g)$ equals it modulo $w^{2r}$; use $\log g=\int g'/g$ and truncate at $N+1<p$. Every integrated index and every recurrence denominator is therefore a unit. After exponentiation the program checks the complete coefficient identity $wT'=T(H-1)$ through degree $N$, with $T(0)=1$; these conditions uniquely determine the finite series. It then computes the two exact finite convolutions. Any zero retains all coefficients and all convolution summands.

The separate public Actions request is the disjoint interval $2001\le p\le200000$, $p\equiv2,5\pmod9$, in four shards. This request is not a completed numerical result. Each completed prime writes its own deterministic gzip certificate and checkpoint, including source and input SHA. The previous R689 interval is not repeated.
