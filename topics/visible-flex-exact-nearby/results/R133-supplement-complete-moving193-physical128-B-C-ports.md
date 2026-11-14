# R133 supplement: complete moving193 to physical128 B and C ports

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Actual complete computation at $r=9/10$, for the same continuous
repaired final centre and the whole original affine parameter interval.**
Together with the preceding complete $C$ matrix, the saved physical
$B$ matrix converts all 193 moving real amplitudes into all physical
curvature ports, with a complete infinite-output error

$$
 \boxed{\quad
 \|D(B,C)[h]-(\widehat B h,\widehat C h_2)\|_{L^2_\theta\oplus L^2_\theta}
 <1.496913\,10^{-11}\|h\|_{L^2_\phi\oplus L^2_\phi}.
 \quad}                                                     \tag{B.1}
$$

Here $h_1$ has sine indices $1,\ldots,96$ and $h_2$ has its mean and
cosine indices $1,\ldots,96$. Physical frequency is $4j$. Both saved
nonmean matrices retain physical indices $1,\ldots,128$; all outputs
above 128 are included in the error. The physical $C$ mean is an
independent saved row, and the physical $B$ mean is exactly zero in this
reflection class. All amplitudes are physical and unnormalized.

The conclusion supplies the complete coordinate ports needed to join a
moving head to the physical cap. It does not validate a finite radial
proposal, remove the actual exterior equations, or prove the global
negative/positive Schur inverse.

## 1. Same true cut and complete moments

The input is the exact continuous repair with definition SHA256
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`
of candidate
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.
The preceding $C$ native already encloses the true scalar target at the
exact cut, verifies all candidate shards, retains the whole original
$\eta$ interval, and computes the exact cumulative repair through this
cut. The present consumer verifies that complete native by SHA and reads
its exact rational candidate coefficients and exact rational offsets.
It uses the same certified mean $m$ and phase $\psi$ with outward
interval parsing. It does not evaluate a different target or relabel an
old centre certificate.

As before,

$$
 \theta=\phi+\psi,\qquad
 \psi=I(v-m)/m,\qquad m=\langle v\rangle<0,
 \qquad B=u/v,\quad C=1/v.                                \tag{B.2}
$$

Since $d\theta=(v/m)d\phi$, all true physical Fourier moments are

$$
 B_k=\frac1m\langle u e^{-ik\theta}\rangle_\phi,
 \qquad C_k=\frac1m\langle e^{-ik\theta}\rangle_\phi.
                                                               \tag{B.3}
$$

For a complete moving variation $h=(h_1,h_2)$, put $z_0=\langle h_2\rangle$.
Direct differentiation gives the full identity

$$
 \boxed{\quad
 \delta B_k=
 \frac1m\langle h_1e^{-ik\theta}\rangle
 -\frac{z_0}{m^2}\langle ue^{-ik\theta}\rangle
 -\frac{ik}{m^2}\langle ue^{-ik\theta}Ih_2\rangle
 +\frac{ikz_0}{m^2}\langle ue^{-ik\theta}\psi\rangle.
 \quad}                                                      \tag{B.4}
$$

Both the measure and the variable physical angle have been
differentiated. There is no $1/v$ in (B.4). It is valid at the approximate
centre, with no zero-residual assumption.

## 2. All 193 exact matrix columns and the independent mean

Let $z=e^{i4\phi}$, write $u=iU$ and $A=i\psi$, and set
$E_l=e^{-4lA}$. Thus the real antisymmetric coefficients of $U$ satisfy
$U_j=-u_j/2$, $U_{-j}=u_j/2$, whereas
$A_j=\psi_j/2$, $A_{-j}=-\psi_j/2$. The physical sine amplitude of an
odd real function is $2i$ times its positive complex Fourier coefficient.
Consequently (B.4) gives

$$
 \boxed{\begin{aligned}
 B^{(1)}_{lj}&=\frac{E_l[l-j]-E_l[l+j]}m,
                     &&1\le j\le96,\\
 B^{(0)}_l&=\frac{2}{m^2}
                   \big[(UE_l)[l]-4l(AUE_l)[l]\big],\\
 B^{(2)}_{lj}&=\frac{l}{jm^2}
                   \big[(UE_l)[l-j]-(UE_l)[l+j]\big],
                     &&1\le j\le96,
 \qquad 1\le l\le128.
 \end{aligned}}                                             \tag{B.5}
$$

The saved order is the 96 $h_1$ sine columns, the $h_2$ mean column,
then the 96 $h_2$ cosine columns. The sign of the first row is readily
checked at $\psi=0$: $\delta B=h_1/m$ when $h_2=0$.

Since both $u$ and $h_1$ are odd, (B.3) gives $B_0=\delta B_0=0$
exactly in the reflection class. This does not delete the even mean:
the physical $C$ mean remains

$$ \delta C_0=-z_0/m^2,                                   \tag{B.6} $$

with its full directed row supplied by the $C$ native. This row is a
matching equation, not an additional freely prescribed Dirichlet input.

## 3. Entire Fourier exponential and all physical output tails

For each $l$ the same one-sided Arb formal-series algorithm used by the
$C$ matrix computes $E_l$, with a proved complete $A_0$ error
$\epsilon_l<2^{-180}$. Multiplication by the complete finite $U$ and
$A$ adds errors at most $\|U\|_{A_0}\epsilon_l$ and
$\|A\|_{A_0}\|U\|_{A_0}\epsilon_l$, respectively. Before exporting
entries, the producer therefore adds the full per-entry errors

$$
 \frac{2\epsilon_l}{|m|},\qquad
 \frac{2\|U\|_{A_0}(1+4l\|A\|_{A_0})\epsilon_l}{|m|^2},\qquad
 \frac{2l\|U\|_{A_0}\epsilon_l}{j|m|^2}.                   \tag{B.7}
$$

No convolution coefficient is sampled or aliased. All 32 actual sine
coefficients of the repaired $u$ are exact rational inputs.

For the full output tail, use any certified contour with
$p_\sigma\ge\|\psi\|_{S_\sigma}$ and
$a_\sigma=\sigma-p_\sigma>0$. Let $g$ be the complete repaired mean
gap and $U_\sigma\ge\|u\|_{S_\sigma}$. The existing complete physical
cap native contains all coefficients of $2u$; these are weighted before
summation and augmented by all exact repair coefficients to obtain
$U_\sigma$. No $A_{1/32}$ bound is extrapolated to a larger strip.

For the finite head define

$$
 C_N^2=2\sum_{j=1}^{96}e^{8j\sigma},\qquad
 B_N^2=2\sum_{j=1}^{96}\frac{e^{8j\sigma}}{(4j)^2}.
                                                               \tag{B.8}
$$

Then $\|h_1\|_{S_\sigma}\le C_N\|h_1\|_2$ and
$\|Ih_{2,\ne0}\|_{S_\sigma}\le B_N\|h_{2,\ne0}\|_2$.
Shifting the entire integrands in (B.4), with opposite shifts for
positive and negative output indices, gives coefficient bounds

$$
 \frac{C_N}{g}e^{-4|l|a_\sigma}\|h_1\|_2,\qquad
 \frac{4|l|U_\sigma B_N}{g^2}e^{-4|l|a_\sigma}\|h_{2,\ne0}\|_2,
 \qquad
 \frac{U_\sigma(1+4|l|p_\sigma)}{g^2}
                 e^{-4|l|a_\sigma}|z_0|.                  \tag{B.9}
$$

These are true complex Fourier coefficients. Set
$S_j=\sum_{l>128}l^je^{-8la_\sigma}$ and evaluate these infinite sums
by their exact geometric expressions, as in the preceding complete
$C$-tail proof. The three tail operator constants are

$$
 T_1=\frac{C_N}{g}\sqrt{2S_0},\quad
 T_2=\frac{4U_\sigma B_N}{g^2}\sqrt{2S_2},\quad
 T_0=\frac{U_\sigma}{g^2}
       \sqrt{2(S_0+8p_\sigma S_1+16p_\sigma^2 S_2)}.
                                                               \tag{B.10}
$$

The two signs are included in each factor two. The three input
subspaces are orthogonal, so the complete tail norm is at most
$\sqrt{T_1^2+T_2^2+T_0^2}$. The actual certified value is less than
$4.212762\,10^{-14}$. The tail argument needs only the entire moving
integrands, not an unproved inverse physical chart on that large complex
strip.

## 4. Directed intervals and the complete paired error

Every matrix entry is exported with outward integer endpoints divided
by $2^{256}$. Its exact dyadic midpoint has denominator $2^{257}$.
Binary64 proposals are formed from those exact rational midpoints and
saved as hexadecimal strings; every conversion error is checked
exactly against $2^{-52}$ and is also summed at its actual value.

The raw input Gram is

$$
 W=\operatorname{diag}
       (\underbrace{1/2,\ldots,1/2}_{96},1,
        \underbrace{1/2,\ldots,1/2}_{96}),                  \tag{B.11}
$$

and the physical sine-output Gram is $(1/2)I$. Thus the Frobenius
operator-error sum uses weight $1$ for all nonmean input columns and
weight $1/2$ for the mean column. Every one of the $128\times193$
entries is included. The actual bounds are

| Complete error | Bound |
| --- | ---: |
| Directed matrix to exact dyadic midpoint | $1.347488\,10^{-11}$ |
| Dyadic midpoint to saved binary64 matrix | $1.589263\,10^{-16}$ |
| All physical $B$ outputs above 128 | $4.212762\,10^{-14}$ |
| Complete physical $B$ operator error | $1.347510\,10^{-11}$ |
| Complete physical $C$ operator error, including its mean | $6.518925\,10^{-12}$ |
| Complete paired physical $(B,C)$ operator error | $1.496913\,10^{-11}$ |

For each component the infinite tail is output-orthogonal to the
retained matrix, giving
$E_B^2\le(E_{B,\rm directed}+E_{B,\rm round})^2+T_B^2$.
The two curvature components form an orthogonal direct sum, hence the
complete paired error is at most $\sqrt{E_B^2+E_C^2}$. This proves
(B.1), including the true mean and all physical frequencies.

## 5. Actual files, reproduction, and remaining global work

All eleven gates passed in 1.90 seconds. The consumer reuses the
already proved actual cut inputs and does not repeat the primitive
calculation.

- Source: `scripts/fourfold_codazzi_final_moving193_physical128_B_matrix.py`.
- Native: `notes/2026-11-14-R133-repaired-moving193-physical128-B-matrix-native.json.gz`.
- Same-centre complete $C$ input:
  `notes/2026-11-14-R133-repaired-moving96-physical128-C-matrix-native.json.gz`.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 \
  scripts/fourfold_codazzi_final_moving193_physical128_B_matrix.py \
  --out notes/2026-11-14-R133-repaired-moving193-physical128-B-matrix-native.json.gz
```

The native stores all exact interval pairs, dyadic midpoint numerators,
binary64 hex values, input/source identities, contour bounds, and both
separate and paired errors. Existing outputs are never overwritten.

The physical cap may now be precomposed with the true $C$ columns and
compared with the true $B$ columns in the same 193 moving variables.
Its complete exterior Robin and mean equations remain in place; the
finite cap proposal still needs its continuous residual certificate.
The entire negative-side head/high interaction and the final parameter
Schur also remain separate obligations. No coordinate conversion is
being used as a substitute for those inverses.
