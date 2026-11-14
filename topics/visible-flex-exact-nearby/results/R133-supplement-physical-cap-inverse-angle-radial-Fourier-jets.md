# R133 supplement: actual physical cap coefficients with radial and Fourier remainders

2026-11-14. **Proved:** the complete coefficient construction below, with
two actual directed closed-cell computations at the inner cap endpoint.
The cells are specified in the native reports. This is not yet a full
cap-matrix residual calculation or a whole-body inverse.

## 1. The exact object and the coefficient algebra

Use the full final centre `ac1d5b98…` and its exact continuous value
repair with definition SHA256

```
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
```

On each original radial cubic the physical moving fields are

$$
 u=\alpha U+e_u,\qquad v=s+\delta v,
 \qquad \delta v=\alpha V+e_v,\qquad
 m=s+\langle\delta v\rangle,
 \qquad \theta=\phi+\psi,\quad
 \psi=m^{-1}I(\delta v-\langle\delta v\rangle).
 \tag{J.1}
$$

All 65 exact dyadic offsets are reconstructed from all 6143 original
interfaces and checked against the published offset-sequence hash.
Neither the complete mean nor the original intrinsic primitive tail is
removed. The actual physical multiplication columns are

$$
 Q_B=(2u)\circ\phi(\theta),\qquad
 Q_C=[-u^2-K(2s\delta v+\delta v^2)]\circ\phi(\theta).
 \tag{J.2}
$$

This uses the cancelled exact algebra from the full physical-cap Green
theorem. In particular it does not subtract two large approximate
values of $\ell$ and $Kv^2$.

Fix one closed radial cell $I$ contained in one actual candidate cubic
and one actual intrinsic scalar germ, and the whole original affine
parameter interval $\eta=\eta_0+\delta\eta$, $|\delta\eta|\le10^{-9}$, where
$\eta_0=-7789843107295549/4611686018427387904$ is the actual original
affine centre. In the formulas below the interval coordinate denotes
$\delta\eta$. Every norm in this proof
is the joint coefficient-supremum norm

$$
 \|f\|_{\mathcal A_\sigma(I)}
 =\sum_{k\in\mathbb Z}e^{4\sigma|k|}
       \sup_{(r,\eta)\in I\times[-10^{-9},10^{-9}]}|f_k(r,\eta)|.
 \tag{J.3}
$$

It is a Banach algebra of coefficient functions. The sum and supremum
in (J.3) are not interchanged. All products, inverse scalar series and
implicit-angle series below are interpreted in this algebra.

## 2. The full inverse angle and its radial jets

Suppose the actual directed finite Fourier bounds establish

$$
 \|\psi\|_{\mathcal A_{2\sigma}(I)}<\sigma,
 \qquad p=\|\psi_\phi\|_{\mathcal A_{2\sigma}(I)}<1.
 \tag{J.4}
$$

The map $h\mapsto-\psi({\rm id}+h)$ is a contraction on the closed
$\mathcal A_\sigma(I)$ ball of radius $\sigma$. Indeed expand each
$e^{4ik h}$ in its complete exponential series and use the algebra
inequality; the image norm is bounded by the first quantity in (J.4),
and the Lipschitz constant by the second. Its solution gives the
genuine inverse $\phi=\theta+h$. This proves existence simultaneously
over the full real cell and affine parameter interval, and retains the
exact reflection symmetry.

Write all radial jets as Taylor coefficients: $f_n=\partial_r^n f/n!$.
For the inverse-angle jets write $x_1=\phi_r$,
$x_2=\phi_{rr}/2$, $x_3=\phi_{rrr}/6$, and evaluate every term on the
right at the same genuine inverse angle. Differentiating (J.1) gives

$$
\begin{aligned}
 Jx_1&=-\psi_1,\\
 Jx_2&=-\psi_2-\psi_{1,\phi}x_1
                      -\tfrac12\psi_{0,\phi\phi}x_1^2,\\
 Jx_3&=-\psi_3-\psi_{2,\phi}x_1-\psi_{1,\phi}x_2
          -\tfrac12\psi_{1,\phi\phi}x_1^2
          -\psi_{0,\phi\phi}x_1x_2
          -\tfrac16\psi_{0,\phi\phi\phi}x_1^3,
 \qquad J=1+\psi_{0,\phi}.
\end{aligned}
 \tag{J.5}
$$

The inverse norm of $J$ is at most $(1-p)^{-1}$. A finite moving
coefficient $f$ has composed jets

$$
\begin{aligned}
 (f\circ\phi)_0&=f_0,\\
 (f\circ\phi)_1&=f_1+f_{0,\phi}x_1,\\
 (f\circ\phi)_2&=f_2+f_{1,\phi}x_1+f_{0,\phi}x_2
                                  +\tfrac12 f_{0,\phi\phi}x_1^2,\\
 (f\circ\phi)_3&=f_3+f_{2,\phi}x_1+f_{1,\phi}x_2
       +\tfrac12 f_{1,\phi\phi}x_1^2+f_{0,\phi}x_3
       +f_{0,\phi\phi}x_1x_2
       +\tfrac16 f_{0,\phi\phi\phi}x_1^3.
\end{aligned}
 \tag{J.6}
$$

Every moving derivative in (J.5)–(J.6) is bounded in
$\mathcal A_{2\sigma}(I)$ before composition. The actual scalar
$K,s$ jets through order three come from the full body/graft provider,
on their true one-sided scalar germ. Applying (J.6) to $u,\delta v$
and then the complete product rule in (J.2) gives numbers

$$
 \|(Q_\bullet)_j\|_{\mathcal A_\sigma(I)}\le M_{\bullet,j},
 \qquad 0\le j\le3,\quad \bullet\in\{B,C\}.
 \tag{J.7}
$$

These are joint norms as in (J.3), including the zero mode. Therefore
Taylor's integral remainder on $r=r_0+h t$, $|t|\le1$, has joint
$\mathcal A_0$ norm at most $h^3M_{\bullet,3}$. No extra frequency cutoff or
unproved interchange of radial supremum and Fourier sum occurs here.

## 3. Directed physical Fourier coefficients and the infinite remainder

At $r_0$, use $N$ equally spaced exact physical angles. The floating
inverse angle is only a bracket centre. Directed evaluations prove the
opposite signs of $x+\psi(\theta+x)$ at both bracket endpoints and
strictly positive derivative. Four interval Newton intersections then
preserve the actual zero for every affine parameter. Formulas (J.5)–(J.6)
give directed samples of the physical Taylor coefficients of orders
zero, one and two. All roots of unity, trigonometric evaluations and FFT
operations use the existing outward-rounded kernels.

For a cutoff $K_f<N/2$, let $P_j$ be the chosen exact dyadic, reflected
Fourier polynomial from the directed DFT, and let $e_j$ be the complete
retained-coefficient interval error. The DFT identity is
$\widehat Q^{\rm DFT}_k=\sum_{l\in\mathbb Z}Q_{k+lN}$.
Every alias entering $|k|\le K_f$ has index at least $N-K_f$ in
absolute value, and every such original coefficient enters at most
one retained slot. Thus the aggregate alias and omitted-tail bounds are

$$
 \sum_{|k|\le K_f}|\widehat Q^{\rm DFT}_k-Q_k|
 \le M_j e^{-4\sigma(N-K_f)},
 \qquad
 \sum_{|k|>K_f}|Q_k|
 \le M_j e^{-4\sigma(K_f+1)}.
 \tag{J.8}
$$

The same inequalities hold in the coefficient-supremum algebra over
$\eta$. They require no extraneous factor $2K_f+1$.
Exact reflection gives the sine parity of $Q_B$ and cosine parity of
$Q_C$; the directed positive and negative DFT intervals are intersected
before selecting their shared dyadic coefficients.

For the selected radial polynomial
$P(t)=\sum_{j=0}^2 h^jP_jt^j$, include the directed rounding cost of
each exact rational scaling $h^j$. Then the full error is bounded by

$$
\boxed{
 \|Q-P\|_{\mathcal A_0(I)}\le
 \sum_{j=0}^2h^j\left[e_j+
 M_j e^{-4\sigma(N-K_f)}+M_j e^{-4\sigma(K_f+1)}\right]
 +e_{\rm scale}+h^3M_3.}
 \tag{J.9}
$$

This contains every physical Fourier mode. In a matrix residual,
the unknown coefficient error in the first Codazzi equation may be
kept as the divergence source
$\partial_\theta[\gamma((Q_B-P_B)b+(Q_C-P_C)c)]$ and consumed by the
already proved divergence Green column. Its angle derivative does not
have to be bounded as an ordinary source. The second equation uses the
ordinary source $\beta((Q_B-P_B)b+(Q_C-P_C)c)$, with the full mean.

## 4. Actual completed cells and remaining work

The source is
[`fourfold_codazzi_physical_cap_coefficient_jets.py`](../scripts/fourfold_codazzi_physical_cap_coefficient_jets.py).
It uses $\sigma=1/16$, $N=512$, $K_f=128$, 192-bit Arb scalar
arithmetic and the existing directed binary64 vector kernels. Both
actual cells retain the whole affine interval and all intrinsic tails.

The first cell is only the tiny interval from the rational $9/10$ to
its first greater binary64 knot. It is recorded without presenting it
as a substantial radial enclosure. The second is the genuine closed
interval

$$
 \left[\frac{8106479329266893}{9007199254740992},
       \frac{2028496332161461}{2251799813685248}\right].
 \tag{J.10}
$$

On this second cell the complete physical errors in (J.9) are

$$
 \|Q_B-P_B\|_{\mathcal A_0}<2.165586\,10^{-10},\qquad
 \|Q_C-P_C\|_{\mathcal A_0}<3.658844\,10^{-9}.
 \tag{J.11}
$$

The full radial Taylor remainders themselves are less than
$2.163998\,10^{-10}$ and $3.524640\,10^{-9}$ respectively. The reports
separately retain the interval, alias, infinite-tail and radial costs.
No conclusion is made for another cell until that cell has actually
passed the same analytic inverse and directed arithmetic gates.

The next consumer must use the entire 96-column exact Hermite matrix,
all its physical output modes and all true outer rows. These completed
coefficient cells alone do not supply that matrix residual, a body
complement inverse or a nonzero nonlinear amplitude Schur.
