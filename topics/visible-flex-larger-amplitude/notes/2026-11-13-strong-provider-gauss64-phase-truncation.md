# Ideal Gauss64 error on the frozen neck's phase pieces

**Status: proved analytic bound, with nine exact rational checks executed.**
This is not a certificate for the actual NumPy table or its floating evaluation,
and is not a surface, convergence, embedding, reach, or amplitude result.

The statement isolates the quadrature truncation error before any rounding.
It applies to the same fixed segment data on both sides of the comparison.
No physical parameter is varied.

## 1. The actual panel structure and hypotheses

The pinned provider uses the flat-turn primitive from
computations/alternative-neck-flatturn.py
(SHA256 c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd).
Its integral routine explicitly splits a turn at normalized coordinates
$0,\varepsilon,1-\varepsilon,1$. This split is essential: a single polynomial
extension of the entire piecewise turn is not used in the proof.

For a turn, including the optional angle boost, set
$$
 C=\frac{\Delta}{1-\varepsilon},\qquad
 R(z)=z^3-\frac{z^4}{2},\qquad \Delta=\phi_1-\phi_0.
$$
The phase on the three panels is
$$
 \phi(u)=
 \begin{cases}
  \phi_0+C\varepsilon R(u/\varepsilon),&0\le u\le\varepsilon,\\
  \phi_0+C(u-\varepsilon/2),&\varepsilon\le u\le1-\varepsilon,\\
  \phi_1-C\varepsilon R((1-u)/\varepsilon),&1-\varepsilon\le u\le1.
 \end{cases}
$$
computations/strong_angle_boost.py calls this same flat-turn construction;
it does not use the older cubic radial-speed boost for the accepted profile.
The brake has $\phi(u)=\phi_0+\gamma u^2$; a coast has constant phase.
The initial Hermite radial primitive is polynomial and needs no phase
quadrature.

Use the following exact, conservative conditions:
$$
 \frac{79}{1000}<\varepsilon<\frac{81}{1000},\quad
 |\phi_0|,|\phi_1|<\frac85,\quad
 0<\gamma<\frac9{1000},\quad
 L>\frac{27}{10000}.
$$
The sum of physical lengths $L$ of the nonconstant phase segments is below
$4$. The executed 33-guard note
notes/2026-11-13-strong-q096-analytic-profile-bounds-r2.md establishes the
endpoint-angle and segment-length budgets for the intended analytic q096
profile. Its frozen cut gives
$\gamma=f\arctan(w)<(101/1000)(81/1000)<9/1000$.
These are conditions on the intended analytic construction; they do not
supply the missing floating-constructor or actual-table certificate.

For each panel and each partial width $w\in[0,b-a]$, use exact 64-point
Gaussian nodes and positive weights on $[0,1]$, denoted by
$(x_i,\omega_i)$. Define
$$
 I_f(w)=\int_a^{a+w}f(u)\,du,\qquad
 Q_f(w)=w\sum_{i=1}^{64}\omega_i f(a+w x_i),
 \quad f=\sin\phi\ \hbox{or}\ \cos\phi .
$$

## 2. Gaussian exactness and a uniform remainder estimate

The 64-node Gaussian rule integrates every polynomial of degree at most
127 exactly, has $\omega_i>0$, and $\sum_i\omega_i=1$.
For completeness, divide such a polynomial by the shifted degree-64 Legendre
polynomial: $p=P_{64}q+r$, with $\deg q,\deg r\le63$.
Orthogonality eliminates the integral of $P_{64}q$; evaluation at all roots
also eliminates it. Interpolation of $r$ proves exactness. If $\ell_i$
is the degree-63 Lagrange basis, then $\ell_i^2-\ell_i$ is divisible by
$P_{64}$ with quotient degree at most62. Orthogonality therefore gives
$\omega_i=\int_0^1\ell_i^2>0$. Exactness on constants gives the mass.

If $F$ is analytic on a neighborhood of
$\{|z-\tfrac12|\le1\}$ and $|F|\le M$ there, Cauchy's coefficient
bound gives a degree-127 Taylor polynomial $p$ for which
$$
 \sup_{0\le x\le1}|F(x)-p(x)|
 \le M\sum_{j=128}^{\infty}2^{-j}
 =2M\,2^{-128}.
$$
Using the positive mass-one rule and exactness on $p$,
$$
 \left|\int_0^1F(x)\,dx-\sum_i\omega_iF(x_i)\right|
 \le4M\,2^{-128}. \tag{1}
$$
This is a bound for the exact rule, not an estimate from sampled residuals.

## 3. Complex bounds for every actual phase panel

On $|x-\tfrac12|\le1$, $|x|\le3/2$.
In a partial left ramp, $z=(w/\varepsilon)x$, so $|z|\le3/2$.
In a partial right ramp, $z=1-(w/\varepsilon)x$; because $w/\varepsilon$
is real in $[0,1]$,
$$
 |z|\le1-\frac{w}{2\varepsilon}+\frac{w}{\varepsilon}
 \le\frac32 .
$$
The bounds on the endpoints and epsilon imply
$$
 |C|<\frac{16/5}{919/1000}<4.
$$
Consequently, on either ramp,
$$
 |\phi-\phi_{\rm real\ endpoint}|
 \le4\frac{81}{1000}
 \left((3/2)^3+\tfrac12(3/2)^4\right)<2.
$$
On the middle panel, the imaginary phase has magnitude below4.
For the brake, the phase increment has magnitude at most
$(9/1000)(3/2)^2<2$.
Thus both $\sin\phi$ and $\cos\phi$ have complex modulus below
$e^4<64$ on every relevant disc. One elementary rational upper bound is
$$
 e < 1+1+\frac12+\frac16+\frac{1/24}{1-1/5}
 =\frac{87}{32};
 \qquad (87/32)^4<64.
$$

The phase derivatives in the original segment coordinate $u$ satisfy
$$
 |\phi'(u)|\le4(3(3/2)^2+2(3/2)^3)=54,
$$
$$
 |\phi''(u)|
 \le\frac4{79/1000}\bigl(6(3/2)+6(3/2)^2\bigr)
 =\frac{90}{79/1000}<1200. \tag{2}
$$
The linear middle phase, quadratic brake, and constant coast obey these
same conservative inequalities. The piecewise phases are extended by
their own polynomial on each panel; clipping operations are never extended
to complex arguments.

## 4. The primitive and its first two derivatives

Differentiate $w f(a+wx)$ at fixed $x$. Its first two width derivatives are
$$
 F_1(x,w)=f(a+wx)+wx f'(a+wx),
$$
$$
 F_2(x,w)=2x f'(a+wx)+wx^2 f''(a+wx).
$$
The zeroth, first and second integrands are entire in $x$ within each
panel. Since $0\le w\le1$, the preceding bounds give
$$
 M_0=64,\qquad
 M_1\le64(1+\tfrac32\,54)=5248<2^{13},
$$
$$
 M_2\le64\left(3\cdot54+\frac94(1200+54^2)\right)
 =603072<2^{20}.
$$
Differentiating the finite quadrature sum and the integral is legitimate.
Applying (1) to these three analytic integrands yields, for every partial
panel width $w$,
$$
 |Q_f(w)-I_f(w)|\le w\,2^{-120}, \tag{3}
$$
$$
 |Q_f'(w)-I_f'(w)|<2^{-113}, \tag{4}
$$
$$
 |Q_f''(w)-I_f''(w)|<2^{-106}. \tag{5}
$$
For (3), apply (1) to $f(a+wx)$, then multiply by $w$.
The non-strict form includes the exact zero-width case.
For (4)-(5), apply it directly to $F_1,F_2$.
There is no division by a partial width, so these bounds include $w=0$.

For a physical segment $s=s_0+Lu$, a radial primitive is
$a_0+L I_{\sin\phi}(u)$, assembled from its panel primitives.
Its exact-Gauss counterpart uses $LQ_{\sin\phi}$ with the same segment
data. Therefore:
$$
 |a_G-a|<2^{-118}
$$
after accumulating all nonconstant phase segments, since their total
physical length is below4. Within each open physical panel,
$$
 |(a_G-a)_s|<2^{-113},\qquad
 |(a_G-a)_{ss}|<\frac{2^{-106}}{L}<2^{-97}. \tag{6}
$$
Coasts contribute exactly zero truncation error and need no positive lower
length bound. The same per-piece estimates apply to the cosine phase primitive used for
the phase-segment background height.

This does not assert that the Gaussian primitive is exactly $C^2$ at
panel joins. Its value is assembled continuously in exact arithmetic, but
its derivatives can have nonzero quadrature-sized jumps. At a join of
$C^2$-compatible ideal pieces, the conservative jump bounds are twice
the corresponding bounds in (6). In particular, the provider's separate
analytic velocity/acceleration formulas should be compared with the ideal
primitive, rather than treating them as exact derivatives of the finite
Gaussian expression.

## 5. What this pays and what it does not

The source computations/strong_provider_gauss64_phase_truncation.js
has been executed using exact BigInt rational arithmetic. All nine
coefficient/exponential/error-budget inequalities passed; its result is
notes/2026-11-13-strong-provider-gauss64-phase-truncation.json.

This proves that, for fixed compatible segment data, ideal Gauss64
truncation on the actual split phase panels is extremely small even at
the second physical derivative level. It does not replace the following
still separate tasks:

- Read and certify the actual NumPy2.3.5 nodes and weights.
- Bound rounded trigonometric, polynomial, dot-product and summation operations.
- Bind the frozen segment lengths, initial radii, physical knots and complete
  piece selection; bound their floating construction and seam mismatches.
- Account for the initial Hermite background-height integral involving
  $\sqrt{1-v^2}$, to which the entire phase argument does not apply.
- Bound the independent nonlinear surface mean-height quadrature and the
  actual surface coefficient errors.

No finite-difference estimate, numerical surface acceptance, continuous
metric-error bound or reach certificate follows solely from this lemma.
