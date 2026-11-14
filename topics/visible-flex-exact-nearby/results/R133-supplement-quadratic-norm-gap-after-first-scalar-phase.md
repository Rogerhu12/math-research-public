# R133 supplement: the quadratic-norm gap after the first scalar phase

2026-11-14, visible-exact-astra-0df9.

**已证明：** the arithmetic theorem below controls all four root-of-unity
divisors after a real scalar phase $\beta/n$ has been included.
It uses the actual quadratic target, an integer norm at high frequency,
and a complete finite continued-fraction reduction at the remaining
frequencies. A numerical instantiation is a separate public Actions
calculation. Applying the theorem to the full return still requires
its actual root/positive first coefficient and strong remainder.

## 1. The actual quadratic form

Use the exact target already proved in
[the bounded15 theorem](R133-supplement-bounded-fifteen-target-and-paid-KAM-arithmetic-tradeoff.md):
$$
 \rho=\frac{A+\sqrt5}{B},\qquad
 A=5831714953207175,\quad B=21212218271020390,\quad a=B/2.
 \tag{Q.1}
$$
Its continued fraction is the finite prefix
$$
 [0;3,1,1,1,3,7,1,3,1,1,1,2,2,1,15,5,4,8]
$$
followed by the infinite tail $\overline1$.
The corresponding integer continued-fraction matrix is unimodular.
Substituting its inverse fractional-linear map in $\tau^2-\tau-1=0$
gives a primitive integer polynomial of discriminant $5$. In the
normalization (Q.1) it is
$$
 f(x)=ax^2-Ax+c,\qquad c=\frac{A^2-5}{2B}\in\mathbb Z,\qquad
 A^2-4ac=5,\qquad f'(\rho)=\sqrt5.
 \tag{Q.2}
$$
For completeness, if the final matrix columns are $(p,q)$ and $(r,s)$,
its determinant $d=ps-qr=\pm1$ gives
$$
 \rho=\frac{A_0+d\sqrt5}{B_0},\quad
 A_0=ps+rq+2rs-2pq,\quad B_0=2(s^2+sq-q^2).
$$
Thus checking $dA_0=A$, $dB_0=B$ and the exact integer discriminant
verifies the stated normalization without rounded rational fitting.

Let $\mathcal B$ be a real closed interval for the scalar coefficient,
write $\mathcal I=\mathcal B/(2\pi)$, and suppose
$$
 |b|\le M\quad(b\in\mathcal I),\qquad
 0<\mu\le\operatorname{dist}(16\sqrt5\,\mathcal I,\mathbb Z).
 \tag{Q.3}
$$
The multiplier to be bounded is
$$
 D_{n,\ell}(\beta)
 =e^{\,i(2\pi n\rho+\beta/n)}-e^{2\pi i\ell/4},
 \qquad n\ne0,\quad \ell=0,1,2,3.
 \tag{Q.4}
$$
Here $2\pi n\rho=4n\Omega_{15}$. This is exactly the physical
fourfold convention, with no missing factor $4$.

## 2. All sufficiently high integers, without a denominator scan

Define
$$
 d_\infty=\frac{\mu}{64\sqrt5},\qquad
 N_0^2\ge\frac{64a(M+d_\infty)^2}{\mu}.
 \tag{Q.5}
$$
Then for every $|n|\ge N_0$, every $\beta\in\mathcal B$ and every
fourth root,
$$
 \boxed{|D_{n,\ell}(\beta)|>\frac{4d_\infty}{|n|}
       =\frac{\mu}{16\sqrt5\,|n|}.}
 \tag{Q.6}
$$

It suffices to prove this for $n>0$, since the negative multiplier is
the conjugate of the corresponding positive one. If for an integer $p$
$$
 \left|n\rho+\frac b n-p-\frac\ell4\right|
       \le\frac{d_\infty}{n},
$$
put $P=4p+\ell$, $N=4n$ and
$u=n(P/4-n\rho)$. Then $|u-b|\le d_\infty$, $|u|\le M+d_\infty$.
The exact integer quadratic norm is
$$
 \begin{split}
 Q(P,N)&=aP^2-APN+cN^2\in\mathbb Z,\\
 Q(P,4n)&=16\sqrt5\,u+\frac{16au^2}{n^2}.
 \end{split}
 \tag{Q.7}
$$
Consequently (Q.3) and (Q.5) would imply
$$
 \mu\le|Q(P,4n)-16\sqrt5\,b|
 \le16\sqrt5\,d_\infty+
       \frac{16a(M+d_\infty)^2}{n^2}
 \le\mu/2,
$$
a contradiction. The distance to each $p+\ell/4$ therefore exceeds
$d_\infty/n$. Finally
$2|\sin(\pi t)|\ge4\operatorname{dist}(t,\mathbb Z)$ proves (Q.6).

A convenient sufficient numerical choice is
$$
 M=4,\quad \mu=1/8,\quad N_0=2^{34}.
 \tag{Q.8}
$$
Indeed $a<2^{54}$ and $d_\infty<1$, so
$64a(4+d_\infty)^2/\mu<12800\,2^{54}<2^{68}=N_0^2$.
Whether a particular coefficient interval satisfies (Q.3) with
$\mu=1/8$ must still be checked. In that case the high-frequency
complex gap is also greater than $1/(288|n|)$, since $\sqrt5<9/4$.
This conclusion has paid the first scalar phase; it does not require
$\beta$ to be smaller than the old principal $1/68$ margin.

## 3. A complete reduction of all remaining integers

The retained actual head is $|n|\le96$. For $97\le n<N_0$ and $M=4$,
the following finite search is exhaustive for every possible gap smaller
than $1/(4n)$; it is not a collection of sampled denominators.

Let $p_k/q_k$ be the consecutive convergents of the exact continued
fraction in Section 1. Generate them until the next denominator is at
least $4N_0$. For each $k$ form all integer pairs
$$
 -66\le v\le66,\qquad -66\le u_0\le a_{k+1}+67,
 \tag{Q.9}
$$
and set
$$
 (P,N)=u_0(p_k,q_k)+v(p_{k-1},q_{k-1}).
 \tag{Q.10}
$$
Retain only
$$
 388\le N<4N_0,\qquad N\equiv0\pmod4,\qquad
 q_k\le N<q_{k+1}.
 \tag{Q.11}
$$
For each retained pair put $n=N/4$ and compute the complete interval
distance
$$
 d(P,N)=\operatorname{dist}
   \left(\mathcal I,\ n(P/4-n\rho)\right).
 \tag{Q.12}
$$
All quantities in (Q.12) are evaluated with directed interval arithmetic.
If any interval contains zero, it is an actual unresolved coefficient
interval and is preserved as a failed separation; it is not replaced
by a midpoint sign.

Here is completeness. If for some $P,N=4n$ the quantity in (Q.12) is
less than $1/16$, choose $b\in\mathcal I$ realizing that distance.
Then $|u|<4+1/16=65/16$, so
$$
 |N\rho-P|<65/N.
$$
Choose the unique $k$ with $q_k\le N<q_{k+1}$ and express $(P,N)$
in its unimodular convergent basis. The coefficient $v$ satisfies
$$
 \begin{split}
 |v|&=|p_kN-q_kP|\\
 &\le q_k|N\rho-P|+N|q_k\rho-p_k|\\
 &<65q_k/N+N/q_{k+1}<66.
 \end{split}
$$
The standard exact convergent inequality used here follows from the
continued-fraction tail and its unimodular determinant.
From $N=u_0q_k+vq_{k-1}$ and
$q_{k+1}=a_{k+1}q_k+q_{k-1}$, the wider bounds (Q.9) follow.
Thus this pair is included. Every omitted integer pair has distance
at least $1/16$.

Let $d_{\rm fin}$ be a positive common directed lower bound for all
the finitely many intervals (Q.12). With the convention that an empty
set needs no finite minimum, set
$$
 d_*=\min(1/16,d_{\rm fin},d_\infty).
 \tag{Q.13}
$$
The finite completeness argument and Section 2 give the uniform result
$$
 \boxed{\min_{\ell=0,1,2,3}|D_{n,\ell}(\beta)|
          >\frac{4\varepsilon}{|n|}
 \quad\text{for all }|n|\ge97,\ \beta\in\mathcal B,}
 \tag{Q.14}
$$
for any explicit rational $0<\varepsilon<d_*$.
The associated scalar inverse has at most one angular derivative of
loss, with multiplier bound $|n|/(4\varepsilon)$.
The mean and the entire original 193-state head are not removed.

## 4. Current coefficient and remaining operator obligations

The already completed
[selected-parameter finite part](R133-supplement-actual-selected-parameter-first-symbol-finite-part.md)
gives a narrow interval for $-\mathfrak X(\delta_*)/4$.
A public consumer may instantiate (Q.3), (Q.9)--(Q.14) on that exact
native interval without rerunning any scalar germ, root Newton step,
phase transport or finite-part integral. It must preserve the complete
finite candidate list, every failed separation, the quadratic identity
and the actual directed minimum.

The actual return coefficient is still
$-(\mathfrak X+b_{\rm root}^{\rm fin})/4$ plus its retained declared
interfaces. Applying the resulting arithmetic certificate to that
return requires its full coefficient interval to lie in the certified
$\mathcal B$, or a new interval instantiation. The whole operator also
needs its strong remainder and complete head/high feedback. This
arithmetic theorem alone does not supply those missing estimates,
a true PDE branch, or the final closed isometric family.
