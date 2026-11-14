# R133 supplement: analytic Airy columns and a complete exponential Fourier bound

2026-11-14, phase_inverse.

**Proved analytic operator estimate.** This replaces the two-real-derivative
symbol estimate in A.1--A.4 of
[the complete real Airy theorem](R133-supplement-complete-real-Airy-seam-operator-in-negative-source-window.md)
when a genuine complex old-angle strip is available. It keeps the true
ray maps, all output modes and the old mean. Its only amplitude input
is a sup norm on a declared analytic strip.

This is an estimate for the same actual Airy columns. The frequency
separation below is used only to bound their norm; it does not modify
a trial, add a radial cutoff source or create an artificial seam.

## 1. A complete analytic Fourier bound with exact discrete ratios

Use $\Lambda_j=(1+16j^2)^{1/2}$ and an integer input cutoff $J\ge1$.
Suppose each $b_j$ is $\pi/2$-periodic and holomorphic on
$|\operatorname{Im}x|<\tau$, with
$\sup_j\|b_j\|_{\tau,\infty}\le B$ for $|j|\ge J$.
There is no differentiability assumption in the column index $j$.
For
$$
 Qe_j=b_j(x)e^{4ijx}
$$
the entire matrix coefficient at lag $\ell=m-j$ satisfies
$|\widehat b_j(\ell)|\le B e^{-4\tau|\ell|}$.
Expanding into weighted diagonal shifts gives

$$
 \boxed{\quad
 \|QP_{\ge J}\|_{H^{-4/3}\to H^{-5/3}}
 \le B\,\mathcal D_{J,\tau}.\quad}                    \tag{A.1}
$$

The explicit complete factor is

$$
\begin{split}
 \mathcal D_{J,\tau}={}&\Lambda_J^{-1/3}
 +2\sum_{\ell=1}^{J-1}e^{-4\tau\ell}
       {\Lambda_J^{4/3}\over\Lambda_{J-\ell}^{5/3}}\\
 &+2\sum_{\ell=J}^{\infty}e^{-4\tau\ell}\Lambda_\ell^{4/3}.
\end{split}                                           \tag{A.2}
$$

In particular the mean output has not been discarded: its exact
weight occurs in the last sum at $\ell=|j|$.

Here is a direct proof of the discrete ratio in (A.2). For
$0\le\ell<J$, the largest value of
$\Lambda_j^{4/3}/\Lambda_{j+\ell}^{5/3}$ over $|j|\ge J$
is $\Lambda_J^{4/3}/\Lambda_{J-\ell}^{5/3}$.
For the opposite-sign branch write $k=|j|$, $x=4k$ and
$y=4(k-\ell)\ge4$. The logarithmic derivative is negative,
because
$$
 {4x\over1+x^2}\le {4\over y}
                  <{5y\over1+y^2}.
$$
The same-sign branch is smaller.
For $\ell\ge J$ the elementary fourfold inequality
$$
 \Lambda_{a+b}\le\Lambda_a\Lambda_b,\qquad a,b\in\mathbb Z,
 \tag{A.3}
$$
gives the upper bound $\Lambda_\ell^{4/3}$, attained at $j=-\ell$,
$m=0$. To verify (A.3), its squared difference is
$256a^2b^2-32ab\ge0$ for integer $a,b$.

The triangle inequality for the diagonal-shift expansion proves
(A.1). Absolute convergence follows from the exponential tail.
For an integer $L\ge J$ such that
$q(1+1/L)^{4/3}<1$, $q=e^{-4\tau}$, a fully directed tail rule is

$$
 \sum_{\ell=L}^{\infty}q^\ell\Lambda_\ell^{4/3}
 \le {q^L\Lambda_L^{4/3}\over1-q(1+1/L)^{4/3}}.
 \tag{A.4}
$$

The finite sum before $L$ remains exact interval arithmetic.
No frequency grid, orthogonality assumption on distinct columns,
or finite output projection is used.

## 2. Genuine complex circle maps

Suppose $\Phi$ is a real orientation-preserving circle lift,
holomorphic on $|\operatorname{Im}\phi|<\sigma$, and

$$
 |\Phi_\phi-1|\le j<1,\qquad
 \Phi(\phi+\pi/2)=\Phi(\phi)+\pi/2 .
 \tag{A.5}
$$

It is injective on the strip: integrating its derivative along
the straight segment between two points gives
$|\Phi(z_1)-\Phi(z_2)-(z_1-z_2)|\le j|z_1-z_2|$.
Its image contains the strip of width $(1-j)\sigma$.
Indeed the upper/lower boundary images have imaginary part
at least $(1-j)\sigma$ in absolute value and the correct sign.
On a narrower closed strip, an expanding rectangle and the
argument principle give every point of the intervening strip
one inverse; periodicity bounds the horizontal displacement.
Letting the narrower strip increase gives the assertion.

Thus $\psi=\Phi^{-1}$ is holomorphic on any
$\tau\le(1-j)\sigma$ with the usual strict boundary convention.
If an actual column is
$b_j(\phi)e^{4ij\Phi(\phi)}$ and
$\|b_j\|_{\sigma,\infty}\le B$, factor it as
$C_\Phi Q$ with symbol $b_j\circ\psi$.
The full estimate is

$$
 \|C_\Phi QP_{\ge J}\|_{H^{-4/3}\to H^{-5/3}}
 \le C_\Phi\,B\,\mathcal D_{J,\tau},
 \tag{A.6}
$$

where $C_\Phi$ is the already proved real
$H^{-5/3}$ composition constant in A.3 of the linked theorem.
It uses the actual real bounds for $\Phi',\Phi'',\Phi'''$.
No complex map is substituted for a real composition operator.

For the present family, the true negative-side phases
$X\pm(2/3)(-T)^{3/2}$ and the real map $X$ satisfy (A.5)
on every paid leading strip with $j=e^{D_1R}-1$.
On the positive side only $X$ is used as a real circle map;
the two nonreal rays are not used for real Sobolev composition.

## 3. Uniform analytic Airy amplitudes on a right half-plane

Put $a=5/36$. With $t=2z^{3/2}/3$, the transformed equation for
$u(z)=\operatorname{Ai}(-z)$ is
$w_{tt}+(1+a/t^2)w=0$, $w=z^{1/4}u$.
For $\operatorname{Re}t>0$ define the two normalized solutions
by the actual horizontal Volterra equations

$$
 p_\epsilon(t)=1-
 \int_0^\infty\sin u\,e^{i\epsilon u}
       {a\over(t+u)^2}p_\epsilon(t+u)\,du,\qquad\epsilon=\pm1.
 \tag{A.7}
$$

The Volterra iterates converge normally on right half-planes.
Their ordered-integral bound gives

$$
 |p_\epsilon(t)|\le e^{a/\operatorname{Re}t},\qquad
 |p_\epsilon'(t)|
 \le {a\over\operatorname{Re}t}e^{a/\operatorname{Re}t}.
 \tag{A.8}
$$

For the derivative, deform the horizontal path within the
right half-plane and differentiate its lower endpoint. The
zero-endpoint sine kernel cancels the boundary term and gives
$$
 p_\epsilon'(t)=\int_0^\infty e^{2i\epsilon u}
       {a\over(t+u)^2}p_\epsilon(t+u)\,du.
$$
This verifies
$p_\epsilon''+2i\epsilon p_\epsilon'+a t^{-2}p_\epsilon=0$.
The integral bound uses
$\int_0^\infty|t+u|^{-2}du\le1/\operatorname{Re}t$.

The exact outgoing identity is

$$
 \operatorname{Ai}(-z)=
 {z^{-1/4}\over2\sqrt\pi}
 \sum_{\epsilon=\pm1}
       e^{i\epsilon(t-\pi/4)}p_\epsilon(t),
 \tag{A.9}
$$

$$
 \operatorname{Ai}'(-z)=
 -{z^{1/4}\over2\sqrt\pi}
 \sum_{\epsilon=\pm1}e^{i\epsilon(t-\pi/4)}
 \left[
   \left(i\epsilon-{1\over6t}\right)p_\epsilon(t)
                         +p_\epsilon'(t)\right].
 \tag{A.10}
$$

To identify the normalization, use the standard leading
Ai/Ai-prime limits
[DLMF 9.7.5--9.7.6](https://dlmf.nist.gov/9.7#E5)
on the rotated arguments $ze^{\mp i\pi/3}$ and the exact
[Airy connection formulas](https://dlmf.nist.gov/9.2#v).
These rotated solutions solve the same equation; their
normalized horizontal limits are 1. The Volterra uniqueness
then identifies them with (A.7). Differentiating (A.9) gives
(A.10), including its sign and the $1/(6t)$ term.
The error bounds (A.8) are the direct Volterra bounds just
proved, rather than an unquantified asymptotic substitution.

For $\operatorname{Ai}(z)$ in the same right-$t$ half-plane,
the decaying normalization $p_0$ instead satisfies

$$
 p_0(t)=1-\frac12\int_0^\infty(1-e^{-2u})
                   {a\over(t+u)^2}p_0(t+u)\,du.
 \tag{A.11}
$$

It is holomorphic, with
$|p_0|\le e^{a/(2\operatorname{Re}t)}$ and
$|p_0'|\le a e^{a/(2\operatorname{Re}t)}/\operatorname{Re}t$.
The exact decaying profile is
$\operatorname{Ai}(z)=z^{-1/4}e^{-t}p_0(t)/(2\sqrt\pi)$;
its derivative has normalized bracket
$(-1-1/(6t))p_0+p_0'$.

## 4. Entire central columns and genuine branch columns

Fix a real radial point with $x=|\rho|>0$ and a paid old-angle
strip of width $\sigma$. Assume on it

$$
 \operatorname{Re}A\ge A_->0,\qquad |A|\le A_+,\qquad
 T=-\rho A^{2/3},\qquad n=4|j|\ge N=4J.
 \tag{A.12}
$$

All powers use the branch fixed by the positive real value.
For the negative side let $z=n^{2/3}xA^{2/3}$; for the positive
side use the same positive-$x$ expression.
In either case $t=(2/3)nx^{3/2}A$.

Separate input indices using the scalar condition
$(2/3)nx^{3/2}A_-\ge1$.
On these high columns, $\operatorname{Re}t\ge1$, so (A.8)
gives each negative branch the analytic bounds

$$
 \begin{array}{ll}
 n^{1/6}\operatorname{Ai}\hbox{ branch}:&
 c_-\,x^{-1/4}A_-^{-1/6},\\
 n^{-1/6}\operatorname{Ai}'\hbox{ branch}:&
 d_-\,x^{1/4}A_+^{1/6},
 \end{array}\quad
 c_-={e^{5/36}\over2\sqrt\pi},\quad d_-={47\over36}c_- .
 \tag{A.13}
$$

Their phases are precisely the two genuine
$X\pm(2/3)(-T)^{3/2}$. Negative Fourier columns interchange
the branch labels, with identical bounds.
On the positive side the sole real phase is $X$; the factor
$e^{-t}$ stays in its analytic amplitude and has modulus at
most 1. Replace $c_-,d_-$ by

$$
 c_+={e^{5/72}\over2\sqrt\pi},\qquad d_+={47\over36}c_+ .
 \tag{A.14}
$$

For the complementary central input indices define

$$
 Z=\left({3A_+\over2A_-}\right)^{2/3},\qquad
 E_Z=\exp(Z+Z^2/2).
$$

Their complex Airy argument satisfies $|z|\le Z$.
The entire initial-value equation $u''=zu$, the already
proved $|\operatorname{Ai}(0)|+|\operatorname{Ai}'(0)|<1$,
and the straight radial path in the complex $z$ plane give
$$
 |\operatorname{Ai}(z)|+|\operatorname{Ai}'(z)|\le E_Z .
$$
Indeed the first-order vector norm has growth at most $1+|z|$
along that path. The same bound holds at $-z$.
After multiplication by the density factors, the central
columns, with the sole phase $X$, have bounds

$$
 n^{1/6}|\operatorname{Ai}(\pm z)|
 \le x^{-1/4} E_Z
                 \left({3\over2A_-}\right)^{1/6},\qquad
 n^{-1/6}|\operatorname{Ai}'(\pm z)|
 \le E_Z N^{-1/6}.
 \tag{A.15}
$$

The high/central separation is independent of $\phi$.
Each column therefore remains analytic on the whole same
strip. The estimates differentiate neither that index
selector nor a new radial cutoff. The actual trial remains
the original entire Airy expression across every radial point.

## 5. Full column bound on the actual root window

Suppose the pair $w=(w_a,w_b)$ has analytic sup bounds
$W_a,W_b$ on the same strip, uniformly in the two input signs.
For $0<x\le R$ define

$$
 B_c=E_Z\left[
       \left({3\over2A_-}\right)^{1/6}W_a
             +R^{1/4}N^{-1/6}W_b\right],
$$

$$
 B_- =c_-A_-^{-1/6}W_a+d_-R^{1/2}A_+^{1/6}W_b,\qquad
 B_+ =c_+A_-^{-1/6}W_a+d_+R^{1/2}A_+^{1/6}W_b .
 \tag{A.16}
$$

Let $C_\Phi$ be a common valid composition constant for $X$
and both real negative-side ray maps, and take
$\tau=(1-j)\sigma>0$. Then the complete operators

$$
 \mathsf S_\rho(w)c=\sum_{|j|\ge J}n^{1/6}
 e^{i\operatorname{sgn}(j)nX}
 \{w_a\operatorname{Ai}(n^{2/3}T)
       +w_b n^{-1/3}\operatorname{Ai}'(n^{2/3}T)\}c_j
$$

satisfy

$$
 \|\mathsf S_\rho(w)\|_{H^{-4/3}\to H^{-5/3}}
 \le x^{-1/4}C_\Phi\mathcal D_{J,\tau}
                 (B_c^2+4B_-^2)^{1/2}
 \quad\hbox{on the negative side},                    \tag{A.17}
$$

$$
 \|\mathsf S_\rho(w)\|_{H^{-4/3}\to H^{-5/3}}
 \le x^{-1/4}C_X\mathcal D_{J,\tau}\max(B_c,B_+)
 \quad\hbox{on the positive side}.                    \tag{A.18}
$$

For (A.17), the central and high input projections are
orthogonal in $H^{-4/3}$, and the two high branches have
total bound $2B_-$. Cauchy--Schwarz in these two input
pieces gives the displayed square root. For (A.18) all
columns have the same real phase $X$, and a uniform
analytic amplitude bound is the maximum. Any empty
central set may instead be assigned zero in that pointwise
estimate.

## 6. Exact old derivative and mean identities remain unchanged

Use (A.17)--(A.18) for $\mathscr A_\rho$ in U.20--U.23.
The exact identities
$$
 \mathsf T(w)=\partial_\phi\mathsf S(H^{-1}w)
                  -\mathsf S(\partial_\phi(H^{-1}w))
$$
and their two complete old-mean consequences are unchanged.
Since the new $\mathscr A_\rho$ only uses a complex sup
norm, the first identity requires one amplitude derivative,
and the twice-iterated mean identity requires two.
There is no longer a further two-derivative Airy-symbol fee.

Every such derivative still needs its actual analytic
width. For example old leading bounds on $3/64$ can pay
derivatives on $1/32$ with loss $1/64$, and the inverse
phase strip is then $(1-j)/32$.
The actual constant radial parts of $H^{-1}$ and $H_D$
may be subtracted before this Cauchy step, exactly as in
the already proved radial-matrix lemma. Radial dependence
itself is not subtracted.

The coefficient operator products can be estimated with
[the complete directed matrix algebra](R133-supplement-directed-analytic-matrix-old-circle-remainders.md);
the old means and all their rank maps stay present.
The same $|\rho|^{-1/4}$ squared envelope is integrated
on both sides of the certified root interval.

This theorem grants neither the complete numerical source
norm nor its smallness. A new public consumer must use
the actual widths, composition constants, matrix costs
and directed tail in (A.4). Local next-amplitude residuals,
positive full low/mean propagation, the complete strong
return norm and the cutoff inverse remain separately
payable.
