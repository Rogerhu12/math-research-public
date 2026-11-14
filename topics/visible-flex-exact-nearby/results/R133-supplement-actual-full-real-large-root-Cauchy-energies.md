# R133 supplement: actual full real large-root Cauchy energies and seam-source windows

2026-11-14, visible-exact-astra-0df9 / root.

**Actual result.** Public run [43621934843](https://github.com/Rogerhu12/math-research-public/actions/runs/43621934843), attempt1, returned child0 and passed all eight scientific gates. The consumer evaluated 792 exact common radial cells from completed original data. It certifies the two full-frequency root-to-negative Cauchy estimates below on every listed real radius, for the same explicit family $Q_\delta=Q_0+\delta Z$, $\nu_\delta=\nu_0+\delta$, fixed physical $\eta_0$ and $|\delta|\le10^{-8}$.

The independent physical even mean, complete ordinary sources and genuine affine seam impulses remain. These are directed Cauchy estimates, not a coupled boundary inverse or a final strong-return norm.

## 1. Complete source and output spaces

Let $\rho=r_*-r$, $0\le\rho\le R$, and use the complete unprojected moving state $h=(h_1,h_2)$, physical Fourier frequencies $4j$, and the original primitive $I=\partial_\phi^{-1}(1-\Pi)$. Define
$$
 \begin{aligned}
 B_0&=\|(h_1(0),h_2(0))\|_{H^{1/3}\times L^2}
       +\sqrt R\,\|g\|_{L^2_\rho(H^{1/3}\times H^{1/3})}
       +\sum_a\|j_a\|_{H^{1/3}\times L^2},\\
 B_{-1}&=\|(h_1(0),h_2(0))\|_{H^{-2/3}\times H^{-1}}
       +\sqrt R\,\|g\|_{L^2_\rho(H^{-2/3}\times H^{-2/3})}
       +\sum_a\|j_a\|_{H^{-2/3}\times H^{-1}} .
 \end{aligned}
$$
Every $j_a$ is the actual prescribed two-row affine jump. Then the independently proved [E1–12 energy theorem](R133-supplement-full-real-large-root-Cauchy-two-source-windows.md), with its actually passed row budgets, gives
$$
 \sup_{0\le\rho\le R}\|h(\rho)\|_{L^2\times L^2}
 \le C_0(R)B_0,\qquad
 \sup_{0\le\rho\le R}\|h(\rho)\|_{H^{-1}\times H^{-1}}
 \le C_{-1}(R)B_{-1}.
$$
If the original primitive is applied afterwards, its exact norm
$C_I=\sqrt{17}/4$ gives
$$
 \sup_{0\le\rho\le R}\|Ih(\rho)\|_{L^2\times L^2}
 \le C_I C_{-1}(R)B_{-1}.
$$
This last statement concerns $Ih$. It does not replace the independent mean by zero in the original system.

All displayed decimals in the following table are outward upper bounds obtained by widening the actual directed endpoints.

| Exact radius $R$ | $C_0(R)$ | $C_{-1}(R)$ | $C_I C_{-1}(R)$ |
|---|---:|---:|---:|
| $1/1000$ | 4.287051 | 4.650003 | 4.793113 |
| $1/500$ | 4.665060 | 5.544040 | 5.714665 |
| $1/200$ | 6.531704 | 10.936120 | 11.272695 |
| $1/100$ | 13.915830 | 50.806275 | 52.369909 |
| $3/200$ | 32.143033 | 285.560911 | 294.349450 |
| $1/50$ | 73.578101 | 1514.952276 | 1561.577063 |

For $R=1/50$, the separate ordinary $L^2_\rho$ source gains, after absorbing $\sqrt R$, are respectively below
$10.405514783$, $214.246605493$, and $220.840346094$.
The initial and summed-affine-jump gains remain the corresponding table entries.

## 2. The actual nonmonotone weight fee

The true root lies in the exact original interval
$$
 \left[\frac{1191984371497}{5000000000000},
       \frac{2383968743003}{10000000000000}\right].
$$
Its width is retained. All integrals use the larger fixed interval
$[r_--R,r_+]$, so they bound every true root-to-point segment without identifying a fixed cut with the true $\rho=R$.

On the largest negative window the actual common-row root-ratio lower bound satisfies
$$
 k=-K/\rho>49.1638,
$$
while the recorded whole $K_r$ lower endpoint is approximately $-20.6187$.
Thus the former attempted global condition $K_r>1$ cannot be used. The corrected Fourier weight
$$
 w_j^2=-K+\Lambda_j^{-2/3}e^{-\rho\Lambda_j^{2/3}},
 \qquad \Lambda_j=\sqrt{1+16j^2},
$$
still has $w_j\ge\Lambda_j^{-1/3}$ because $k>1$.

For each row whose $K_r$ lower bound is below1, the consumer uses its strictly positive distance from $r_-$ to pay the positive part of $-w_\rho/w$ as E.3a. Near the root the actual positive derivative gate is checked instead. The complete extra integral is
$$
 \sum_i |I_i|S_i<0.034816267.
$$
The first five radii have zero such fee. On $R=1/50$, the complete two growth integrals, including every local, primitive, transport and mean term, satisfy
$$
 {\cal I}_0<2.553460545,\qquad
 {\cal I}_{-1}<5.578252325.
$$
The actual angular speed is below $1.253802<13/10$; the complete saved local $q^2$ upper bound is below $1.048659$. No sign assumption on a whole radial interval enclosure is silently restored.

## 3. Actual computation and preserved failures

The successful mathematical consumption took **1.9821087870000014 seconds**, with recorded child wall time **5.000481786999998 seconds**. All 792 common cells and every local growth decomposition remain in the complete native.

The consumer receives the original 1300-row radius-$1/50$ root native and the six original intrinsic third-jet parts from run43583838026. It verifies their exact SHA256 identities, original row identities, complete selected ranges and closed covers. It then intersects the true radial intervals. No original scalar target, candidate, response solve, Fourier coefficient, primitive or root computation ran again.

Two preceding actual failures are retained:

- Run43620358162 had three successful input gates and zero completed scalar rows. The reader incorrectly required a selected original part to carry the global 7721-cell completion flag. The original producer and finish reader show that these parts correctly have complete=False, selected_cells_complete=True and no failure.
- Run43621351216 passed five input gates and then failed the first actual global $K_r>1$ gate, again with zero completed scalar rows. The nonmonotone fee is an explicit mathematical repair. Neither failed execution is relabelled successful.

The successful run records four real pull/README checks with empty differences, last at commit
08e74aee5894fd1e6a791bc182344f7189095a35.
The separately reviewed rule commit remains
ee26c0a65a2e63c15f2ccfba6714181584416542.

## 4. Immutable evidence

Directory:
notes/large_root_Cauchy_ci/run-43621934843-1-full-real-large-root-Cauchy/.

| Evidence | SHA256 |
|---|---|
| Complete native, 665816 bytes | 3a214897f5dc47e1a1fed3db327f54fcc0302ad6fd273ea96ecdbfcc0ca4f1e0 |
| Small summary, 50621 bytes | 238a85156791fac2516a23c5f9a6ea1253e648c341bedae139d1c2c5c47cbee5 |
| Read repository process snapshot, 11652 bytes | 82bf0467ccaaece38dcb606e537552e5c59dedf6ac8cb9cd4375458fab951c1c |
| Mathematical source | 9acc1e8187663b91845347878034a384f5ff25b939e7faa0a1ab72f7f8738de9 |
| Reviewed worker | d491f1c6d1e6f1788f92ca8f47ddcf2b977ca5cf5dbffe879650cbbe7a8554db |
| Exact 16-file input manifest | cc907dc35cd1d71703910ee6cc8fda7bb90f677867f43b0752d0719d899d4846 |

The native is native/full-real-large-root-Cauchy-two-windows.json.gz;
the summary is evidence/full-real-large-root-Cauchy-summary.json.
The original native and all failed prefixes remain unchanged.

## 5. Use in the unfinished full inverse

The actual first-correction jump must still be reconstructed and measured in the declared source norm; this consumer does not evaluate it. The newly available radii allow an explicit choice between geometric reach and propagation cost. No old positive Green map receives a lower Sobolev source window automatically.

The full first Airy forcing, finite inverse and original mean remainders, numerical strong-return constants, sufficient Fourier cutoff, actual finite-head/high-tail feedback, physical parameter Schur complement and nonlinear branch remain separate obligations. This result supplies the complete real negative Cauchy leg needed for those obligations.
