# R106 supplement: the complete finite part along the actual root characteristic

## Statement and scope

For the actual affine step5 family

\[
 p_5=-\frac{7789843107295549}{4611686018427387904},
 \qquad |p-p_5|\le 10^{-9},
\]

let \(t(p)\) be the certified positive simple root and fix the original physical
cut

\[
 r_c=\frac{268136140016943}{1125899906842624},\qquad
 c(p)=\sqrt{t(p)-r_c}.
\]

In physical root-label coordinates \(\eta\), the complete R106 finite part
from the root to this cut is holomorphic on \(|\Im\eta|\le1/900\), and

\[
 \boxed{\ \sup_{p,\ |\Im\eta|\le1/900}|h_{\sigma}^{\rm root}(\eta,p)|
       <15148.\ }                                                   \tag{1}
\]

This holds for both inward signs and, by exact radial reflection, both physical
roots. Every physical angular mean, ground-state contribution, cut term and
root term is included. The characteristic is the actual characteristic over
the complete real root interval. This is a coefficient of the physical
root-label one-form \(d\eta\), with initial root-label Jacobian \(1\).
Pullback by the complete global root map, the strict-region contribution and
the complete return-frame map remain separate operations. In particular,
(1) does not by itself assert a complete return multiplier, effective R104
cutoff, strong propagator remainder or full PDE inverse.

## 1. Executed and bound inputs

The completed actual seven-field Fourier/Taylor report is

    data/R106/root_seven_native_degree64/report.json

SHA256:

    abf77633bb8340eaf11fe45d6f3fb943a80d265c9a5c0d2ce234c64d9ee36bab

Its common error domain is

\[
 |\rho|\le R=\frac7{25000},\qquad
 |\Im\theta|\le S_{\rm in}=\frac1{400}.
\]

All radial rows \(0,\ldots,64\), all retained modes \(-450,\ldots,450\),
all infinite radial and angular tails, aliasing, interval coefficient choice
and arithmetic errors are accounted for. The underlying true holomorphy
domain is the executed seven-field bidisk in
[the actual bidisk proof](R106-supplement-actual-seven-field-native-bidisk.md).
The actual original object has SHA256

    91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848

The original scalar germs and shared affine parameter are preserved.

The complete finite regularized source was actually produced by
[the regularized FFT producer](../scripts/fourfold_subprincipal_root_regularized_fft_v2.py);
its report is

    data/R106/root_regularized_native_degree64_plus/report.json

SHA256:

    0e1e511cc0a5c10b13a5e314ba354f1880dfccf4e5bce411b99c648ba037a06d

Finite products retain all output modes (up to absolute Fourier index \(1350\));
the FFT is a padded, rigorously enclosed algorithm for these complete finite
products. It is not a projection of the product to the input bandwidth.
The report and coefficient shards bind every source and input hash.

The consumer
[actual root phase bound](../scripts/fourfold_subprincipal_actual_root_phase_bound.py)
produced

    notes/2026-11-13-R106-actual-complete-root-phase-bound.json

SHA256:

    0abe610d230cfb4214e26b0b4a8368594fdd4448559907d423d6aa29b0cd0724

It checks all finite-source shards, their contiguous radial row coverage,
identities, producer/dependency hashes, the seven-field report hash, and the
common root/domain identity before using any bound.

## 2. Complete regularized one-form

Use the R106 original-height root fields
\(G,q,k_*,S_{\rm reg},L_\theta,U_0,U_1\), and write
\(G_0=G(0,\theta)\), \(G_1=\partial_\rho G(0,\theta)\) and
\(q_0=q(0,\theta)\). The exact transport counterterms are

\[
 B_{-3}=-G_0/3,\qquad
 B_{-1}=-G_1-\frac23\partial_\theta(q_0G_0).
\]

The completed regularization has

\[
 H_\sigma=R_\sigma+\partial_\theta S_{\rm reg},
 \qquad
 C_\sigma(s,\theta)
 =s^{-3}(B_{-3}-U_0/4)
   +s^{-1}(B_{-1}-U_1/4)-\sigma L_\theta/4,
 \qquad
 Z_\sigma=\sigma L_\theta(0,\theta)/4.
\]

Here \(R_\sigma\) is the analytic source in the proved R106 transport
regularization. Its cancellation uses the exact geometric root identity
\(k_*(0)G_0=-1/16\), before approximation. A finite coefficient choice is
not required to satisfy that identity exactly; its complete discrepancy
is included in the source-error formula.

For the actual nonsingular root ODE

\[
 \Theta_s=2s\,q(s^2,\Theta)-2\sigma s^2k_*(s^2,\Theta),
 \qquad \Theta(0,\eta)=\eta,\qquad J=\partial_\eta\Theta,
                                                               \tag{2}
\]

the exact finite part is

\[
 h_\sigma^{\rm root}(\eta)
 =J(c,\eta)C_\sigma(c,\Theta(c,\eta))
  +\int_0^c H_\sigma(s,\Theta(s,\eta))J(s,\eta)\,ds
  +Z_\sigma(\eta).                                             \tag{3}
\]

The sign \(\sigma\) only changes signs of the odd source and regular cut/root
fields in the finite representation, so all modulus bounds below hold for
both signs. Under \(F(-r)=S F(r)\), \(\det S=-1\), the quantities
\(F\cdot F\), area square, support, \(a_0,c_0\) are even and \(b_0\) is odd.
Changing to inward root distance gives (2) with the corresponding inward
sign. Consequently the same estimates hold at the negative root. This is
the exact branch conversion detailed in
[the complete reference adapter proof](R106-supplement-complete-root-reference-sampler.md),
not an assignment of an unsigned physical orientation.

## 3. Existence and bounds for the actual whole root flow

The saved root interval gives

\[
 0.0156250182396570<c(p)<0.0156250182483485,
 \qquad c_{\max}^2<R.
\]

On the complete input error bidisk the actual fields satisfy
\(M_q<1.459\) and \(M_k<28.675\), with the more precise rigorous endpoints
retained in the source report and used in the arithmetic below. Put

\[
 A=c_{\max}^2M_q+\frac23c_{\max}^3M_k,\qquad
 S_f=\frac{17}{10000}.
\]

The executed interval evaluation gives

\[
 A<0.000428961227064,\qquad
 \frac1{900}+A<0.001540072338175<S_f.
\]

On any existing solution of (2) up to its first exit from the flow strip,
integration of (2) gives \(|\Theta(s,\eta)-\eta|\le A\).
This strict interior estimate prevents a first exit. The fields are
holomorphic on a fixed neighborhood of the closed flow domain, their
derivatives are bounded there, and the periodic angle lift has bounded
velocity. Ordinary Picard continuation therefore gives the actual solution
for every \(0\le s\le c(p)\), uniformly on the entire initial strip.
Holomorphic dependence on \(\eta\) follows on the same domain.
No saved finite trajectory or sampled-time estimate is used.

Cauchy's estimate with gap \(S_{\rm in}-S_f\) gives

\[
 |q_\theta|\le\frac{M_q}{S_{\rm in}-S_f},\qquad
 |(k_*)_\theta|\le\frac{M_k}{S_{\rm in}-S_f}.
\]

The differentiated ODE and Gronwall imply

\[
 |J|\le
 \exp\!\left(\frac{A}{S_{\rm in}-S_f}\right)
 \le1.709501032081087<1.710.                                   \tag{4}
\]

These are whole-time estimates on the true characteristic. In particular,
no unresolved true-minus-reference fee occurs in (3).

## 4. Complete source errors on the enlarged source strip

The finite source was first made on physical strip \(1/800\). For this
consumer set \(S_h=1/550>S_f\), still strictly smaller than
\(S_{\rm in}\). Its true approximation error is recomputed on \(S_h\);
the old error is not silently extended. Let \(r=c_{\max}^2\) and split
the total angle margin into two losses

\[
 d_1=d_2=(S_{\rm in}-S_h)/2.
\]

For complete seven-field errors \(e_G,e_q,e_k\), true moduli
\(M_G,M_q,M_k\), and finite moduli \(Q_h,K_h\), define

\[
\begin{aligned}
 B&=M_G/R+2M_qM_G/(3d_1),\\
 e_B&=e_G/R+2(e_qM_G+Q_he_G)/(3d_1),\\
 E_{G2}&=e_G/[R^2(1-r/R)],\\
 E_{qG}&=(e_qM_G+Q_he_G)/[R(1-r/R)],\\
 E_{kG}&=(e_kM_G+K_he_G)/[R(1-r/R)],\\
 E_{qB}&=e_qB+Q_he_B,\qquad E_{kB}=e_kB+K_he_B.
\end{aligned}
\]

Radial coefficient Cauchy estimates for the shifted analytic remainders
and the two angular Cauchy estimates give the complete true \(R_\sigma\)
error

\[
 E_{G2}+\frac{2(E_{qG}+c_{\max}E_{kG})}{3d_2}
       +\frac{2(E_{qB}+c_{\max}E_{kB})}{d_2}.
\]

Adding \(e_{S_{\rm reg}}/(S_{\rm in}-S_h)\) gives the error of \(H_\sigma\).
The cut and root errors are, respectively,

\[
 \frac{e_G}{3c_{\min}^3}+\frac{e_B}{c_{\min}}
 +\frac{e_{U_0}}{4c_{\min}^3}+\frac{e_{U_1}}{4c_{\min}}
 +\frac{e_{L_\theta}}4,\qquad \frac{e_{L_\theta}}4.
\]

All these are directed Arb computations. For a saved finite row with largest
index \(K_n\), its finite-arithmetic Wiener error is transferred from
\(S_o=1/800\) to \(S_h\) by multiplying by
\(\exp(4K_n(S_h-S_o))\), then by \((r/\mathrm{scale})^n\).
The full finite polynomials are independently evaluated by their complete
weighted coefficient sums on \(S_h\). This transfer uses their explicit
finite support; it does not extend the domain of an unknown true tail.

The resulting complete moduli are

| Actual quantity | Executed upper bound | Simple outward bound |
| --- | ---: | ---: |
| \(H_\sigma\) | \(3110.450375392364\) | \(3111\) |
| \(C_\sigma(c,\cdot)\) | \(8811.718077287586\) | \(8812\) |
| \(Z_\sigma\) | \(0.374652934652310\) | \(0.375\) |
| true source approximation error | \(2445.890943464654\) | \(2446\) |
| true cut approximation error | \(5.328307017522\) | \(5.329\) |

Combining these complete fields with (3) and (4), using the original
unrounded bounds, gives

\[
 |h_\sigma^{\rm root}|
 \le M_J(M_C+c_{\max}M_H)+M_Z
 \le15147.098993231531<15148.
\]

This proves (1).

## 5. Reproduction and retained data

Run from this topic directory, with a native Python installation containing
python-flint, NumPy and SciPy:

~~~bash
python3 scripts/fourfold_subprincipal_root_regularized_fft_v2.py \
  data/R106/root_seven_native_degree64/report.json \
  --sigma 1 --working-strip 1/800 \
  --out-dir data/R106/root_regularized_native_degree64_plus

python3 scripts/fourfold_subprincipal_actual_root_phase_bound.py \
  data/R106/root_regularized_native_degree64_plus/report.json \
  --out notes/2026-11-13-R106-actual-complete-root-phase-bound.json
~~~

Use new output paths if reproducing while the saved reports exist; the producers
intentionally refuse to overwrite evidence. In the present runtime the commands
were prefixed with
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps
and PYTHONDONTWRITEBYTECODE=1.
The regularized source took about \(64\) seconds and this consumer about
\(7.4\) seconds. The original seven-field coefficient shards are retained. The new regularized
source coefficient shards are reproducible in about 64 seconds by the first
command and are not duplicated in the repository; their exact hashes remain
in its saved report. Regenerate those shards before replaying the coarse
consumer. The sharp consumer uses the completed report directly. The large
seven-field node intermediates are likewise reproducible by the exact upstream
command recorded in the seven-field recovery note.
