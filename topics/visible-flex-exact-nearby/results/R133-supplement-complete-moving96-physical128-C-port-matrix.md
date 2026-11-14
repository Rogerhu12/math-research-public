# R133 supplement: complete moving96 to physical128 C-port matrix

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Actual complete computation, for the continuous repaired final centre at
$r=9/10$ and the whole original affine parameter interval.** The full
physical $C$ derivative of the moving second-component head
$\operatorname{span}\{1,\cos4\phi,\ldots,\cos384\phi\}$ has a saved,
directed $128\times97$ nonmean matrix and its independent physical mean
row. Let $\widehat H$ denote the saved binary64 matrix, extended by zero
on physical output indices $|j|>128$, with the saved physical mean row.
Then

$$
 \boxed{\quad
 \|D C[h]-\widehat H h_2\|_{L^2_\theta}
 <6.518925\,10^{-12}\|h_2\|_{L^2_\phi}.
 \quad}                                                     \tag{C.1}
$$

The first moving component contributes exactly zero to this port. Both
circle measures are normalized. The inputs and outputs are physical,
unnormalized real cosine amplitudes; the mean has weight one and each
nonzero cosine has squared norm $1/2$. The estimate includes the true
parameter interval, the exact continuous repair, every finite conversion
entry, binary64 rounding, and every omitted physical output frequency.
It is an interface theorem, not a complete body inverse.

## 1. Same centre, same actual cut, complete scalar input

The background is the distinct continuous repair with definition
SHA256
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`
of the exact final candidate
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.
The producer verifies both identities and every candidate shard. It
evaluates all 65 candidate components at the exact rational cut $9/10$
by exact rational Horner evaluation. It then forms the actual cumulative
repair, component by component, through piece 5484 by the same exact
interface recurrence that defines the repaired object.

The intrinsic scalar provider is the already proved full rotational cap
provider. It is evaluated at this exact point on its true scalar germ

$$
 \left[
 \frac{1010495166391255}{1125899906842624},
 \frac{8106479329266893}{9007199254740992}
 \right].                                                   \tag{C.2}
$$

It retains the complete unit primitive and all infinite remainders, and
uses the original affine half width $10^{-9}$ before the positive branch
and reciprocal are taken. The compact $\nu$ control is exactly zero at
this cut. No pointwise floating target is substituted for this interval.

Write the resulting repaired state as

$$
 v=m+\sum_{j=1}^{32}v_j\cos4j\phi,\qquad
 \psi=\sum_{j=1}^{32}\frac{v_j}{4jm}\sin4j\phi,
 \qquad \theta=\phi+\psi.                                  \tag{C.3}
$$

The native gives $m\in[-3.2072027190\pm4.13\,10^{-11}]$ as a
short display enclosure and proves
$\theta_\phi>0.9866657171057276$ on the entire real circle. The saved
interval fields, not these shortened decimal displays, are used in all
subsequent calculations. The exact repair is applied before forming
$m$, $1/m$, or any phase coefficient.

## 2. Exact matrix entries, including the mean

Use $z=e^{i4\phi}$ and write the real antisymmetric Laurent polynomial

$$
 A=i\psi
   =\sum_{j=1}^{32}\frac{\psi_j}{2}(z^j-z^{-j}),
 \qquad E_l=\exp(-4lA),\quad l\ge1.                         \tag{C.4}
$$

For a Laurent series $E$, denote its coefficient at $z^k$ by $E[k]$.
The complete physical curvature moments and their derivative are

$$
 C_{4l}=m^{-1}\langle e^{-i4l(\phi+\psi)}\rangle,
 \qquad \delta\psi=\frac{Ih_2-z_0\psi}{m},
 \qquad z_0=\langle h_2\rangle.                            \tag{C.5}
$$

Differentiation of the actual moments gives

$$
 \delta C_{4l}=-\frac{z_0}{m^2}E_l[l]
 -\frac{i4l}{m^2}\langle e^{-i4l\theta}Ih_2\rangle
 +\frac{i4lz_0}{m^2}\langle e^{-i4l\theta}\psi\rangle.
                                                               \tag{C.6}
$$

The real physical cosine amplitude is $2\delta C_{4l}$. Therefore the
exact matrix entries, with column zero the moving mean, are

$$
 \boxed{\begin{aligned}
 H_{l0}&=\frac{2}{m^2}\big[-E_l[l]+4l(AE_l)[l]\big],\\
 H_{lj}&=-\frac{l}{jm^2}\big[E_l[l-j]-E_l[l+j]\big],
                      &&1\le j\le96,\ 1\le l\le128.
 \end{aligned}}                                             \tag{C.7}
$$

The independent physical mean is exactly

$$
 \delta C_0=-z_0/m^2;                                      \tag{C.8}
$$

all its nonmean-input columns vanish. All $h_1$ columns vanish. These are
identities at the approximate centre: neither Codazzi satisfaction nor
vanishing centre residual is assumed. In particular the moving-angle
variation in (C.6) is essential; replacing it by a bare fixed-angle
reciprocal derivative would produce a different matrix.

## 3. Complete Fourier exponential with an explicit infinite remainder

For each $l$, split $-4lA=P(z)+Q(z^{-1})$, where both $P$ and $Q$ are
finite ordinary polynomials with zero constant coefficient. The producer
uses Arb formal power series to compute exactly enclosed coefficients
through degree $n$ of $\exp P$ and $\exp Q$. This is formal-series
coefficient arithmetic, not periodic sampling.

For any positive real $\sigma$, define

$$
 M_{P,\sigma}=\sum_{j=1}^{32}|P_j|e^{j\sigma},\qquad
 M_{Q,\sigma}=\sum_{j=1}^{32}|Q_j|e^{j\sigma}.
$$

The whole omitted one-sided Fourier tails have $A_0$ bounds
$e^{M_{P,\sigma}-\sigma(n+1)}$ and
$e^{M_{Q,\sigma}-\sigma(n+1)}$. Since truncating a one-sided series
cannot increase its $A_0$ norm, the product of the two retained
polynomials approximates the full two-sided $E_l$ with remainder

$$
 \epsilon_l\le e^{-\sigma(n+1)}
 \big[e^{M_{P,\sigma}+M_{Q,0}}
      +e^{M_{Q,\sigma}+M_{P,0}}\big].                        \tag{C.9}
$$

The actual producer selects a certified width and integer cutoff with
$\epsilon_l<2^{-180}$. The selected cutoffs range from 101 through
104. The whole product polynomial is retained; there is no aliasing,
hard-head projection, or assumption that its other coefficients vanish.

For (C.7), the nonmean entry remainder is at most
$2l\epsilon_l/(j|m|^2)$ and the mean entry remainder is at most
$2(1+4l\|A\|_{A_0})\epsilon_l/|m|^2$. The multiplication $AE_l$ uses
all 65 actual phase coefficients. These errors are added as Arb balls
before producing output intervals. All interval dependence of $m$ and
$A$ is retained by directed arithmetic; no independence or statistical
interpretation of parameter intervals is used.

## 4. Exact directed intervals, dyadic proposals, and Gram normalization

Each interval entry is exported as integers $L_{lj},U_{lj}$ divided by
$S=2^{256}$, by outward rounding of the exact Arb endpoints. Its chosen
dyadic midpoint is

$$
 \widetilde H_{lj}=(L_{lj}+U_{lj})/(2S),\qquad
 r_{lj}=(U_{lj}-L_{lj})/(2S).                               \tag{C.10}
$$

The same operation is applied to the separate physical mean entry.
For the raw moving amplitude coordinates, the input Gram is
$W_{\rm in}=\operatorname{diag}(1,1/2,\ldots,1/2)$; the nonmean
physical output Gram is $W_{\rm out}=(1/2)I$. Consequently a rigorous
operator-error bound is

$$
 \left[r_{00}^2+
   \sum_{l=1}^{128}\left(\frac12r_{l0}^2+
                              \sum_{j=1}^{96}r_{lj}^2\right)
 \right]^{1/2}.                                            \tag{C.11}
$$

This is the Frobenius bound of
$W_{\rm out}^{1/2}(H-\widetilde H)W_{\rm in}^{-1/2}$,
with the physical mean as a separate weight-one output. Its actual
complete value is less than $6.518858\,10^{-12}$.

For each entry the code converts the exact rational midpoint directly to
binary64 and converts that result back to an exact rational. It checks
the individual difference is at most $2^{-52}$ and sums the *actual*
differences with the same Gram weights. The complete binary64 rounding
error is less than $4.394021\,10^{-17}$. Exact hexadecimal binary64
strings are saved, so the proposal is reproducible without dividing two
separately rounded large integers.

The previously proved whole physical-output tail above 128 has gain
less than $1.757236\,10^{-14}$. It has output support orthogonal to the
retained matrix and the mean row. Thus the complete matrix-and-tail
error is bounded by

$$
 \sqrt{(E_{\rm directed}+E_{\rm binary64})^2+E_{>128}^2}
 <6.518925\,10^{-12},                                     \tag{C.12}
$$

which proves (C.1). In particular there is no factor $\sqrt{97}$ or
$\sqrt{128}$ silently omitted: every entry already occurs in (C.11).

## 5. Actual output and interface use

All twelve actual gates passed in 39.71 seconds. The first few midpoint
entries, displayed only for orientation, are

| Physical cosine index | Moving mean | Moving cosine 1 | Moving cosine 2 | Moving cosine 3 |
| --- | ---: | ---: | ---: | ---: |
| 1 | $-.002558258768$ | $-.097216043954$ | $.000319763728$ | $-.000002115838$ |
| 2 | $-.000016534542$ | $-.002558185311$ | $-.097201281703$ | $.000852585724$ |
| 3 | $.000000006892$ | $-.000018601167$ | $-.002877793644$ | $-.097180247161$ |

The independent physical mean midpoint is $-.09721811075511112$ times
the moving mean. The full exact integer intervals, rather than this
display table, are the deliverable.

An actual physical cap proposal can be precomposed with the nonmean
matrix (C.7). The separate mean row (C.8) remains in the coupled scalar
equation. For normalized moving orthonormal columns, the nonmean input
columns must be multiplied by $\sqrt2$; a numerical approximation to
this factor requires its own explicit rounding fee. Precomposition
does not discard the tail (C.12): it is a genuine omitted physical
input to be paid with the installed complete cap Green. Neither the
finite cap proposal nor this coordinate matrix alone proves the
negative/positive global Schur inverse.

This report is for the stated repaired centre and whole original
parameter interval. It does not extend these finite coefficient
identities to an unknown infinite correction without its own change
of-background estimate.

## 6. Files and reproduction

Source: `scripts/fourfold_codazzi_final_moving96_physical128_C_matrix.py`.
Native: `notes/2026-11-14-R133-repaired-moving96-physical128-C-matrix-native.json.gz`.

The native schema has one common `exact_interval_denominator` $2^{256}$
and one common `dyadic_midpoint_denominator` $2^{257}$. Each of the 128
`rows` stores all 97 pairs `exact_interval_numerators`, all 97
`dyadic_midpoint_numerators`, and all 97
`exact_binary64_proposal_hex` values. `physical_mean_row` stores the
independent weight-one row; all of its other columns are exactly zero.
It also stores the exact cut coefficients and offsets, actual intrinsic
germ and scalar intervals, all exponential tails, and every input and
source SHA.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 \
  scripts/fourfold_codazzi_final_moving96_physical128_C_matrix.py \
  --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --out notes/2026-11-14-R133-repaired-moving96-physical128-C-matrix-native.json.gz
```

The exact final candidate is restored by the published six-stage replay
manifest; this computation does not duplicate its large intermediate
arrays. An existing output is never overwritten.
