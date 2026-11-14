# R43 supplement: complete root Fourier data in the actual negative collar

2026-11-13, phase-inverse continuation.

**Actual completed conclusion.** The same negative characteristic chart of
[the actual negative-collar theorem](R43-supplement-actual-negative-characteristic-collar.md)
has a complete R43 estimate on
\(0\le\xi\le\delta=2^{-140}\), for every \(|s|\le8\), uniformly over the
same real parameter interval \(p_5\pm10^{-9}\). The full intermediate
window through \(|s|\le10\) is paid. In the actual canonical amplitude
frame, including the mean, both amplitude branches, and both frequency
cones, its exact propagation is

\[
 C(\delta,0)=I+B+R_{4/3},\qquad
 \|R_{4/3}:E_s\longrightarrow E_{s+4/3}\|
 <6.192042\,10^{41}.
 \tag{RF1}
\]

Here \(B\) is the full real-ray phase operator of R43, not its angular
average. The homogeneous forward and inverse norms are below \(1.106\).
The canonical ordinary source
\(L^1(d\xi;H^{s-1/3})\to E_s\) has gain below \(20.961937\).

The collar is longer than the previous \(2^{-224}\) collar and the strong
constant is smaller than its previous \(1.228295\,10^{61}\) bound. These
numbers remain too coarse to be advertised as a practical complete-return
cutoff. The physical source changes, the strict/root interface, the positive
Ai/contact network, and the complete returned remainder are separate
obligations.

## 1. Existing complete data, with its actual uncertainty retained

The inputs are the existing complete canonical Fourier reports

- `notes/2026-11-12-ci-canonical-v0-scaled-Wiener.json` and its coefficient NPZ;
- `notes/2026-11-12-ci-canonical-v1-scaled-Wiener.json` and its coefficient NPZ;
- `notes/2026-11-13-actual-negative-canonical-collar-R43-v2.json`.

Their construction is in R97--R99 and the negative-collar supplement. The
new consumer checks the producer and dependency hashes, saved coefficient
hashes, actual nominal/root-fit input hashes, parameter identity, and the
complete negative characteristic chart gates before use.

Write the root potential traces as

\[
 V(0,\phi)=v_0(\phi),\qquad V_\xi(0,\phi)=v_1(\phi).
\]

The saved real binary64 coefficients \(c^{(i)}_n\), \(0\le n\le4096\),
are exact dyadic coefficients of a reference. They are **not** defined to
be the geometry. For every actual parameter value, the complete reports
prove

\[
 \left(\sum_{|n|\le4096}|(v_i)_n-c^{(i)}_n|^2\right)^{1/2}
 \le E_i,
\]
\[
 E_0<1.872673\,10^{-5},\qquad E_1<0.012340301.
 \tag{RF2}
\]

All physical-to-canonical map error, finite interpolation error, original
infinite primitive error, DFT rounding, and aliases are already in (RF2).
The same reports also give the complete true coefficient tails

\[
 |(v_0)_n|\le467.112549\,e^{-4u_*|n|}\quad(n\ne0),
 \qquad |(v_1)_n|\le2380464.991\,e^{-4u_*|n|},
\]
\[
 u_*>0.0018609264148396234.
 \tag{RF3}
\]

The first tail uses the certified split \(v_0=5050+(v_0-5050)\). The
constant is retained in \(c^{(0)}_0\), and is not charged separately at
each nonzero frequency.

The canonical angle used by those reports has period \(\pi/2\) and
Fourier modes \(e^{4in\eta}\). For R43 set
\(x=4\eta=q_{\rm quarter}\phi\), so \(x\) has period \(2\pi\) and
the same coefficient index is exactly \(n\). The actual root fit gives

\[
 38.8838516058<q_{\rm quarter}<38.8838516231.
 \tag{RF4}
\]

Thus neither an unrecorded physical factor four nor the final R104 circle
label is substituted into this local computation.

## 2. Complete finite-window root moments

For each needed real \(p\ge0\) and each split \(L\le4096\),
Cauchy--Schwarz applied to the **whole** low coefficient error gives

\[
 \begin{split}
 \sum_n\langle n\rangle^p|(v_i)_n|
 \le{}&\sum_{|n|\le L}\langle n\rangle^p|c^{(i)}_n|\\
 &+E_i\left(\sum_{|n|\le L}\langle n\rangle^{2p}\right)^{1/2}
 +2M_i\sum_{n>L}\langle n\rangle^p e^{-4u_*n}.
 \end{split}
 \tag{RF5}
\]

For \(i=0\), use the residual modulus in (RF3) only in the last term;
there is no omitted mean there. The finite sum and its error retain both
signs of every nonzero coefficient. The canonical projection cutoff is
strictly below half the original canonical DFT size, so its last retained
mode is an ordinary two-sided mode, not a Nyquist half coefficient.

The middle term is a single correlated \(\ell^2\) fee. It is not replaced
by an error per coefficient without summing the corresponding weights.
For fixed parameter \(p_0\), (RF5) bounds the whole coefficient sum, and
its right-hand side is independent of \(p_0\); this gives the claimed
uniform parameter-family bound.

The complete analytic tail is evaluated with
\(\langle n\rangle^p\le(n+1)^{\lceil p\rceil}\), binomial expansion,
and the exact Stirling/geometric power-tail formula. Every \(n>L\),
including every mode above 4096, is present. Selecting the smallest among
finitely many fully paid choices of \(L\) preserves the bound.

The actual choices and outward bounds are:

| Power \(p\) | Split for \(v_0\) | Complete \(v_0\) moment | Split for \(v_1\) | Complete \(v_1\) moment |
|---|---:|---:|---:|---:|
| \(31/3\) | 3488 | \(2.391642\,10^{33}\) | 3776 | \(3.524590\,10^{36}\) |
| \(19/2\) | 3328 | \(1.577676\,10^{30}\) | 3616 | \(2.265330\,10^{33}\) |
| \(32/3\) | 3104 | \(1.091426\,10^{34}\) | 3392 | \(1.784593\,10^{37}\) |

These are bounds for the true root traces, not values of the reference
polynomials. Their size still reflects amplification of the already paid
coefficient error by high Sobolev weights.

## 3. Complete radial errors on the actual negative chart

The negative characteristic theorem has already proved the holomorphic
actual potential on a radial disk and an actual canonical angle strip:

\[
 R_V=5\,10^{-8},\qquad S_V>8.7512855\,10^{-6},\qquad
 \sup|V|<4.062836\,10^{14}=:M_V.
 \tag{RF6}
\]

The displayed decimals in (RF6) are explanatory outward bounds; the
consumer uses the directed stored endpoints. This is the exact negative
characteristic chart. No positive finite coordinate chart replaces it.

For \(z=\delta/R_V\), Cauchy's coefficient estimate on that full disk
gives on the whole smaller angle strip

\[
 |V-v_0-\xi v_1|\le M_V{z^2\over1-z}=:\varepsilon_0,
\]
\[
 |V_\xi-v_1|\le{M_V\over R_V}
                    {z(2-z)\over(1-z)^2}=:\varepsilon_1.
 \tag{RF7}
\]

Each corresponding normalized-angle Fourier coefficient has the additional
factor \(e^{-d|n|}\), where
\(d=q_{{\rm quarter},-}S_V\). In particular, for every \(p\ge0\),

\[
 \sum_n\langle n\rangle^p|e_n|
 \le\varepsilon\left\{
 {2\lceil p\rceil!\over(1-e^{-d})^{\lceil p\rceil+1}}-1\right\}
 =:\mathcal T_p(\varepsilon).
 \tag{RF8}
\]

This follows by \(\langle n\rangle^p\le(n+1)^{\lceil p\rceil}\) and
\((n+1)^m\le m!\binom{n+m}{m}\). The mean is included. The apparently
large derivative remainder in (RF7) is retained rather than discarded
because \(\delta\) is small.

Combine (RF5) and (RF8) as

\[
 \sum_n\langle n\rangle^p\sup_{0\le\xi\le\delta}|V_n(\xi)|
 \le L_{0,p}+\delta L_{1,p}+\mathcal T_p(\varepsilon_0),
\]
\[
 \sum_n\langle n\rangle^p\sup_{0\le\xi\le\delta}|(V_\xi)_n(\xi)|
 \le L_{1,p}+\mathcal T_p(\varepsilon_1).
 \tag{RF9}
\]

For each fixed actual parameter the root terms are common to all \(\xi\),
so the supremum over \(\xi\) in these inequalities does not destroy the
correlated root coefficient error used in (RF5).

## 4. Actual R43 consumption, including the ordinary source

For \(|s|\le8\), the three powers in the table pay all R43 quantities:

\[
 p_K=8+2+1/3=31/3,\quad
 p_B=8+1+1/2=19/2,\quad
 p_W=8+4/3+4/3=32/3.
\]

The extra two layers in \(p_K\) pay the complete intermediate Volterra
window. Since the true quarter frequency is larger than four, the maxima
with one in R43's \(q\)-factors equal one. The actual directed computation
gives

\[
 K_0<2.698781\,10^{37},\qquad
 \delta K_0<1.936281\,10^{-5}<1/10,
\]
\[
 B_1<1.333706\,10^{34},\qquad
 \mathcal W<6.501001\,10^{38},\qquad C_q<476.237535.
 \tag{RF10}
\]

R43 now gives precisely

\[
 2C_q\mathcal W+2e^{1/10}\delta B_1^2
 <6.192042\,10^{41},
\]

which proves (RF1). This uses the full operator form of the R43 theorem,
so it includes its actual mean propagation, cross-cone entries, and both
amplitude rows. No columnwise inference of an operator norm is made.

For the exact ordinary canonical source, R39's coefficient and the same
Volterra bound give

\[
 {5\sqrt2\pi\over c_A}e^{1/10}<20.961937,
 \qquad c_A=\sqrt{\operatorname{Ai}(0)/[-\operatorname{Ai}'(0)]}.
 \tag{RF11}
\]

The statement concerns this source in these canonical units. It does not
declare a physical weak divergence source or an unwired root contact to be
an ordinary source satisfying (RF11).

## 5. Reproduction and limits

The standalone consumer is
`scripts/fourfold_negative_collar_root_fourier_budget.py`. Its complete
native report is
`notes/2026-11-13-negative-collar-root-Fourier-window8-v2.json`.
From the topic directory the exact reproduction command is

```sh
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_negative_collar_root_fourier_budget.py \
  --collar-dyadic-power 140 --window 8 --bits 320 \
  --out /tmp/negative-collar-root-Fourier-window8.json
```

The saved report includes every selected split, finite coefficient term,
correlated low error, complete root analytic tail, radial remainder, and
all final constants. The earlier filename without `-v2` is a preliminary
run before removing an unnecessary import of the still-running strict
field producer; it is not the frozen conclusion report.

The current conclusion is the exact negative collar (RF1). It does not
bridge the remaining distance to the physical regular cut, identify the
complete returned R104 coefficient, supply positive Ai/contact bounds,
invert the complete finite Schur block, or prove the nonlinear closed
family required by the topic README.
