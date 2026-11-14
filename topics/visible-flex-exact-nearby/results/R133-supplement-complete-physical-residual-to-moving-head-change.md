# R133 supplement — complete physical residual to moving-head change of equations

## 1. Actual complete map at the cut

At the same repaired final centre and the exact cut $r=9/10$, let

$$
 \theta=\Theta(\phi)=\phi+\psi(\phi),\qquad
 \Theta_\phi=v/m>0,\qquad m=\langle v\rangle<0.              \tag{B.1}
$$

The exact candidate identity, all cumulative value repairs and the whole
original affine interval are those of the already proved complete
$C$-port matrix. Define the full change of a physical odd boundary
residual by

$$
 \boxed{\quad (\mathcal S R)(\phi)=v(\phi)R(\Theta(\phi)).\quad}
                                                               \tag{B.2}
$$

This is an exact bounded isomorphism of the complete physical and moving
odd $L^2$ spaces, with normalized circle measure on both sides. The
actual new native proves

$$
 \|\mathcal S\|<3.228515,\qquad
 \|\mathcal S^{-1}\|<0.313899.                             \tag{B.3}
$$

No restriction to a Fourier head is used in (B.2)–(B.3). These bounds
therefore apply to unknown infinite output tails and ordinary boundary
source errors as well as to finite proposals.

The complete finite block

$$
 K_{96,128}=\Pi_{\sin,96}^{\phi}\mathcal S\Pi_{\sin,128}^{\theta}
                                                               \tag{B.4}
$$

has actually been evaluated with directed entries on the whole original
affine interval. Its exact rational midpoint followed by the stored
binary64 rounding is within

$$
 \boxed{\quad\|K_{96,128}-K_{\rm num}\|_{L^2\to L^2}
          <1.385711\,10^{-10}.\quad}                       \tag{B.5}
$$

All ten gates passed in the actual 3.27-second computation. It only
consumed the already proved cut phase, mean and exact finite centre
coefficients. No target primitive was recomputed.

The block (B.4) is not the whole map (B.2). No physical input above 128,
moving output above 96, physical mean equation, or body/high feedback
equation is removed. This result supplies the same-coordinate output
projection needed by a genuine moving-head/high Schur decomposition;
it is not a proof of that whole Schur inverse.

## 2. Full norm and inverse, with the true density

Changing variables by (B.1) gives the exact identity

$$
 \|\mathcal S R\|_{L^2_\phi}^2
 =\int |R(\theta)|^2\,|m|\,
       |v(\Theta^{-1}(\theta))|\,\frac{d\theta}{\pi/2}.
                                                               \tag{B.6}
$$

Indeed the measure factor is $d\phi=d\theta/\Theta_\phi$, and
$v^2/\Theta_\phi=mv=|m||v|$. Hence

$$
 \|\mathcal S\|\le\sqrt{|m|\sup|v|},\qquad
 \|\mathcal S^{-1}\|\le\frac1{\sqrt{|m|\inf|v|}}.             \tag{B.7}
$$

The real lower bound for $|v|$ is obtained from the actual complete mean
and all 32 exact nonmean cosine coefficients. It is positive before
either inverse bound is taken. The candidate and affine bounds are not
replaced by their midpoints. The more precise computed upper endpoints
are $3.22851478314729$ and $0.313898015023217$.

The same estimate applies to arbitrary $L^2$ functions; in the actual
reflection class $v$ is even and $\Theta$ is odd, so (B.2) preserves the
odd subspace. It is a multiplier followed by a true coordinate change,
not an assertion that composition minus identity is small on $L^2$.

## 3. Exact entries without differentiating an approximate angle

Use raw physical inputs $\sin(4l\theta)$ and raw moving outputs
$\sin(4j\phi)$. Write

$$
 A=i\psi,\qquad E_l=\exp(-4lA).
$$

The coefficients of $A$ form the real antisymmetric Laurent vector
already used in the complete $C$-port certificate. From $v=m\Theta_\phi$,

$$
 v\sin(4l\Theta)
   =-\frac{m}{4l}\partial_\phi\cos(4l\Theta).               \tag{B.8}
$$

An integration by parts with the full periodic functions gives

$$
\boxed{\quad
 K_{j,l}=m\frac jl
     \left(\widehat E_l(l-j)+\widehat E_l(l+j)\right),
 \quad1\le j\le96,\quad1\le l\le128.
\quad}                                                       \tag{B.9}
$$

The factor two of the raw sine amplitude is included. As a check on the
normalization, if $\psi=0$, (B.9) is $m\delta_{jl}$, exactly the map
$R\mapsto mR$.

The finite one-sided exponential coefficients are computed by the
already proved formal exponential routine. Its independently bounded
complete omitted $A^0$ tail is $\epsilon_l<2^{-180}$. Consequently the
missing contribution to (B.9) is at most

$$ 2|m|(j/l)\epsilon_l.                                   \tag{B.10} $$

This fee is added before extracting any exact directed entry interval.
All original affine uncertainty in $m$ and $\psi$ remains present. No
quadrature and no sampling of the angular map is used.

## 4. Actual matrix and Gram conventions

The native has 96 rows, ordered by moving index $j=1,\ldots,96$, and
128 columns, ordered by physical index $l=1,\ldots,128$. Both input and
output are raw sine amplitudes. Their normalized $L^2$ Gram matrices
are both $(1/2)I$, so the two factors cancel in the Hilbert–Schmidt
matrix-error bound.

Each entry is stored as two exact integer endpoints over $2^{256}$.
Its exact midpoint has denominator $2^{257}$. The binary64 proposal is
computed by converting that exact rational midpoint once; its exact
binary representation is saved as a hexadecimal string. The actual
complete directed and rounding bounds are

$$
\begin{split}
 \epsilon_{\rm directed}&<1.385697212\,10^{-10},\\
 \epsilon_{\rm binary64}&<1.350197257\,10^{-15}.
\end{split}                                                   \tag{B.11}
$$

Their sum gives (B.5). The entrywise float check allows $2^{-50}$,
since the diagonal entries have magnitude about $3.2$; it does not
reuse a smaller magnitude assumption from the different $C$ matrix.
The full recorded sum of exact rounding differences is used in (B.11).

If a complete physical residual has a finite proposal $r_{128}$ and
known error $\|R-r_{128}\|_{L^2_\theta}\le\epsilon$, then

$$
 \|\Pi_{96}^{\phi}\mathcal S R-K_{\rm num}r_{128}\|_2
 \le3.228515\epsilon+
           1.385711\,10^{-10}\|r_{128}\|_2.                \tag{B.12}
$$

This is a complete source/error contract. For the complementary moving
output one must retain

$$
 \Pi_{>96}^{\phi}\mathcal S r_{128}
 \quad\text{and an error at most }3.228515\epsilon.         \tag{B.13}
$$

In particular (B.12) does not declare (B.13) zero or small. Equally, an
unknown physical tail cannot be deleted merely because the displayed
matrix has 128 columns; it is paid through the full map norm in (B.3).

## 5. The exact identity block and the independent mean equation

At fixed physical angle, the derivative of $B=u/v$ with respect to the
moving first component $h_1$ is $h_1/v$ composed with $\Theta^{-1}$.
The angle depends only on the second component. The physical curvature
variation $\delta C$ also depends only on $h_2$. Therefore, for the
complete physical cap graph $\delta B=G_{\rm cap}\delta C$ and its full
boundary source, the transformed residual has the exact form

$$
 \mathcal S(\delta B-G_{\rm cap}\delta C)
     =h_1+\mathcal L_{\rm cap}h_2.                          \tag{B.14}
$$

Every nonlocal angle term and all cap source columns are part of
$\mathcal L_{\rm cap}$ or the transformed source. The complete $h_1$
block in (B.14) is an **exact identity**, including its zero output on
moving indices above 96 when the input $h_1$ lies in that head. It should
not be replaced by the approximate product of two truncated physical
matrices and then called an exact identity.

The true physical $C$ mean is independent. At the cut its first variation
is $-z/m^2$, where $z=\langle h_2\rangle$. Thus its regular graph equation
remains

$$
 -z/m^2-G_{{\rm cap},0}\delta C_{\ne0}=g_0.                \tag{B.15}
$$

One may multiply this row by $-m^2$, provided its source, adjoint and
all mean couplings are multiplied by the same factor. Equation (B.15)
is not removed by the odd $B$ transformation. The complete high/low
body coupling and the independent final compact parameter equation
remain to be assembled.

## 6. Files and reproduction

- `scripts/fourfold_codazzi_final_physical128_moving96_residual_matrix.py`
- `notes/2026-11-14-R133-repaired-physical128-moving96-residual-matrix-native.json.gz`

The only scientific native input is the actual same-cut complete
$C$-port certificate with SHA
`119dedb2e62f23553b81dea9eb787d8298c1224eebc2cc38790ec50274df0ca7`.
It contains the true whole-affine mean, complete finite phase, exact
cut candidate coefficients, exact cumulative repair, and their original
target identity. The source verifies that identity before consumption.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python -u \
  scripts/fourfold_codazzi_final_physical128_moving96_residual_matrix.py \
  --out /path/to/new-physical-moving-residual-matrix-native.json.gz
```

No mathematical process or scientific input used by the running complete
phase transport was changed to obtain this independent boundary block.
