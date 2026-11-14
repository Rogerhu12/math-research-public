# R133 supplement: actual full-family root-to-negative Cauchy certificate

2026-11-14. **Proved, with an actual public directed-arithmetic certificate.**
Public [run 43604498718](https://github.com/Rogerhu12/math-research-public/actions/runs/43604498718)
completed successfully; the mathematical child returned zero and all twelve
gates passed. The mathematical wall time was 0.264403992 seconds.

## 1. Exact object and the resulting estimate

This instantiates the complete proof in
[the full-family root-to-negative Cauchy energy](R133-supplement-full-family-root-to-negative-Cauchy-energy.md).
It applies to the same explicit family $Q^\delta$ at intrinsic $\eta_0$,
every real $|\delta|\le10^{-8}$, and $0\le\rho=r_*-r\le9\,10^{-6}$.
It retains the complete 96-mode background, the true quadratic band192,
every unknown Fourier mode, the old angular primitive, and the independent
even mean.

For the full physical two-state equation with ordinary forcing $g$,
the complete estimate is

$$
\sup_{0\le\rho\le9\,10^{-6}}\|h(\rho)\|_{L^2\times L^2}
\le\frac{41}{10}\left[
 \left(\|h_1(0)\|_{H^{1/3}}^2+\|h_2(0)\|_{L^2}^2\right)^{1/2}
 +\frac3{1000}\|g\|_{L^2_\rho(H^{1/3}\times H^{1/3})}
\right].
$$

Circle measure is normalized and the physical angular frequency is $4j$.
The norm includes the independent mean coordinate. Propagation is from
the true root to the negative cut. This statement does not claim the
reverse estimate, an arbitrary Sobolev-index version, a positive root
reflection graph, a complete return inverse, or a nonlinear solution.

## 2. Exact execution identities

The evidence directory is
`notes/current_negative_root_cauchy_ci/run-43604498718-1/consumers/`.

| Item | Exact SHA256 or commit |
| --- | --- |
| actual native `current-negative-root-cauchy.json.gz` | `8f165ccf9dee6e622060b4fc269908ef322f0b0fea15b82dc4b223a2fb4c122d` |
| published `process.json` snapshot | `f3688651110c9748b8a88b0c1da6cc88f78c50284474d9d6a12fffa7b99cd3da` |
| mathematical source | `9bcf3dd119950ebb4188017eedd1f75dae729c345aa131a884f8346627209c28` |
| wrapper | `d5fb812c20397de89bf34c2881978ebb6981486cbea70cdcff0b0d37e358bc41` |
| nine-file manifest | `9cd9a83cb15756a10c97f4ca3a6a680f759ae6bc8560d0d5de6b6faeb9c4325f` |
| workflow event commit | `af133b7fe8eeaeea82eff51364f6d601c81c03e7` |
| actual scientific checkout commit | `669252ad459f499c6422523945b5da7b048b1b5b` |

The native consumes the unchanged actual root germ
`397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864`
and unchanged completed root scalarization
`10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f`.
The old germ and scalarization were not recomputed. The event commit and
scientific checkout commit differ because the worker genuinely pulled
current main before taking its immutable scientific snapshot.

## 3. Actual strict bounds

The following outward decimal bounds follow directly from the recorded
directed enclosures.

| Complete quantity | Certified bound |
| --- | ---: |
| real $K_\rho$ | $59.743804372436<K_\rho<60.464393710307$ |
| $q^2$ on the whole interval | $<0.000544179544$ |
| regular $w$ | $<1.000272052766$ |
| $\theta^{-1}$ | $<3.525421487366$ |
| local reaction growth | $<9.512856929692$ |
| complete drift growth | $<0.881197651577$ |
| primitive $L^2\to H^{1/3}$ | $<0.400880405379$ |
| complete ordered primitive growth | $<6.837339829519$ |
| genuine even-mean rank growth | $<11.746630396643$ |
| total energy growth | $<28.978024807429<31$ |
| reconstruction times paid exponential | $<4.002204670412<41/10$ |

The proof uses the frequency-dependent regular weight
$w_j^2=q^2+\Lambda_j^{-2/3}e^{-\rho\Lambda_j^{2/3}}$,
$\Lambda_j=(1+16j^2)^{1/2}$, and
$\theta_j=\exp[-(63/50)(1-e^{-\rho\Lambda_j^{2/3}})]$.
The dissipative derivative of $\theta$ absorbs the exact remaining
degenerate principal term before taking a frequency supremum. The drift
commutators, local reaction, complete ordered primitive, and true mean
rank are then separately paid. Thus the proof never integrates a
divergent supremum over all frequencies.

At the root this weight gives exactly the displayed
$H^{1/3}\times L^2$ trace norm. The radial forcing coefficient follows
from the exact identity $(3/1000)^2=9/10^6$ and Cauchy--Schwarz.
No truncation of an unknown input or deletion of a mean/source row
is used in the twelve-gate conclusion.

## 4. Use in the continuing proof

The estimate transfers a controlled two-row root error and a complete
ordinary residual of an actual Airy construction to the negative cut.
The actual Airy amplitudes, their old-curve means, the positive graph
correction, and the resulting finite reflection constant remain separate
obligations. In particular this certificate alone supplies neither
$b_{\rm root}^{\rm fin}=0$ nor the complete phase return.
