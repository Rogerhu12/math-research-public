# R106 supplement: even Taylor parity and complete cross-cone bounds

**Proved for the same actual maps.** Their previously proved complex
domains and moduli are retained. Real odd jets enter only through an
explicit even Taylor expansion with its complete analytic tail.

At the norm scale \(N_0=2^{20}\), the complete errors for each relevant
\(Q_H-Q_H^{-*}\), its adjoint, and all opposite-cone/mean components
now have the following common bounds in both windows \(0\to2\) and
\(-2\to0\).

| Actual map | Positive-real-part strip width | Lower bound for \(\operatorname{Re}H'\) | Complete cross/adjoint bound |
|---|---:|---:|---:|
| Every strict relative flow and inverse | \(4.56962195948\,10^{-6}\) | \(0.0333697009649\) | \(9.609882202544\,10^{17}\) |
| Final actual root-circle map | \(2.73138315457\,10^{-5}\) | \(0.0861170743531\) | \(402383810928\) |

The respective complete error bounds improve by factors greater than
\(9.9240246517\,10^{13}\) and \(43240664.51\).
The old true negative scattering error is not re-estimated here.

## 1. Real parity with a complete complex remainder

Let \(H\) be holomorphic on \(|\operatorname{Im}z|\le S\), real on
the real circle, and suppose
\[
 H'(x)\ge m>0,\qquad |H'(z)|\le M.
\]
Every Taylor coefficient of \(H'\) at a real center is real.
Consequently the odd terms of \(H'(x+iy)\) are purely imaginary.
Cauchy's coefficient bound on the unchanged strip gives
\[
 \operatorname{Re}H'(x+iy)
 \ge m-M\sum_{k\ge1}(|y|/S)^{2k}
 =m-{M(|y|/S)^2\over1-(|y|/S)^2}.                         \tag{EC.1}
\]
This is a quadratic loss near the real axis. It does not assume that
a real derivative bound also holds at complex arguments.

If real odd jets through order eleven are additionally known,
\(|H^{(2k+1)}(x)|\le h_{2k+1}\), then for \(t=|y|/S<1\),
\[
 \operatorname{Re}H'(x+iy)
 \ge m-\sum_{k=1}^5
       \min\!\left(M,{h_{2k+1}S^{2k}\over(2k)!}\right)t^{2k}
        -{Mt^{12}\over1-t^2}.                            \tag{EC.2}
\]
The last term pays every higher even Taylor coefficient.
All real odd derivatives are consumed on their proved real domain;
all unsupplied complex coefficients use the old analytic modulus.

The disk of radius \(S\) centered at any real point lies in the
original strip. If its boundary is interpreted as a limiting closed
domain, apply Cauchy at smaller radii and pass monotonically to \(S\).
Thus (EC.1)--(EC.2) apply uniformly at every real center.

## 2. Actual strict maps

The complete actual strict family has
\[
 C_r^{-1}\le H_{t,s}'\le C_r,\quad C_r<14.983653,\qquad
 |H_{t,s}'(z)|\le C_c<36.730914
\]
on the original normalized complex width
\(S=2.7952875\,10^{-5}\). These permissions cover every pair of strict
times and the inverse, with the original full parameter box retained.

Use \(m=C_r^{-1}\), \(M=C_c\) in (EC.2). The real jets are those
already proved in the original complete real-ray report, with the
accepted first same-label closed-cell bounds where available.
This consumer intentionally does not require the later stronger
true-gap-intersection values.

A directed dyadic bisection on \(0<t\le1/2\) chooses a complete
substrip for which the full right-hand loss in (EC.2) is strictly
less than \(m/2\). The resulting directed values are
\[
 s>4.56962195948\,10^{-6},\qquad
 c=\inf\operatorname{Re}H'>0.0333697009649.                 \tag{EC.3}
\]
The old complex strip and modulus are unchanged; (EC.3) is a newly
paid positive-real-part statement inside them.

## 3. Actual final-circle map

The full final label from the actual two-cone normal form has
\[
 S_C=1/4096,\quad m_C>0.172234148706,\quad
 M_C<6.794131324991 .
\]
This is the actual R101 final-circle map, with its original parameter
scope and original exact affine object. No new all-parameter arithmetic
inverse is claimed.

Here the universal complete formula (EC.1) suffices. Choose
\[
 t_C=(1-2^{-40})\sqrt{{m_C\over2M_C+m_C}},\qquad s_C=S_Ct_C.
\]
Then the full loss is strictly smaller than \(m_C/2\), giving
\[
 s_C>2.73138315457\,10^{-5},\qquad
 \operatorname{Re}H_C'>0.0861170743531.                    \tag{EC.4}
\]
No new real jet or complex domain of the inverse was assumed.

## 4. Full infinite opposite cones, adjoints and means

For a real degree-one map with the positive complex derivative bound
on width \(s\), put
\[
 a={s\min(1,c)\over2}.
\]
Shifting the periodic Fourier contour by \(s/2\) gives
\[
 |(C_H)_{kj}|\le e^{-a(|k|+|j|)}
\]
for opposite signs, including the relevant zero-output rows.
For the original \(\Lambda_n=\max(1,|n|)\),
\[
 |(Q_H)_{kj}|
 \le\sqrt{\Lambda_k/\Lambda_j}\,e^{-a(|k|+|j|)} .
\]
The same exact density identities and complete mean ledger used in
the original normal-form proof apply without alteration.

Define
\[
 Z_p(a)=\sum_{n\in\mathbb Z}(1+|n|/N_0)^p e^{-2a|n|},
 \qquad
 Z_{p,1}(a)=\sum_{n\in\mathbb Z}|n|(1+|n|/N_0)^p e^{-2a|n|}.
\]
The original full Hilbert--Schmidt estimate is
\[
 e_H=8(1+M)\sqrt{(Z_4+Z_{4,1})Z_4}.                       \tag{EC.5}
\]
It includes both infinite opposite-cone rectangles, every required
mean input and output row, and both strong windows. In particular,
the actual \(Q_H^{-*}\) mean input
\(\Lambda^{-1/2}H'\) is not replaced by the constant mean.

The exact identity
\[
 E_{H^{-1}}=-E_H^*,\qquad E_H=Q_H-Q_H^{-*},
\]
also pays the inverse companion error. This avoids asserting a new
analytic inverse strip where none has been computed.

The new decays are
\[
 a_{\rm strict}>7.624345915548\,10^{-8},\qquad
 a_C>1.176093631046\,10^{-6}.
\]
Complete geometric-moment evaluation of (EC.5) gives the table above.
No Fourier coefficient below or above a cutoff is discarded.

## 5. Reproduction and limits

~~~bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_actual_real_jet_positive_complex_strip.py \
  --out notes/2026-11-13-R106-even-Taylor-complete-cross-cone.json
~~~

Source: scripts/fourfold_actual_real_jet_positive_complex_strip.py.  
Native: notes/2026-11-13-R106-even-Taylor-complete-cross-cone.json.

The consumer verifies the complete original object, real-jet and
complex-flow input identities, pays the entire Taylor tails, and
checks positivity before evaluating the two full geometric sums.
No original native geometry is rerun.

This result improves only the complete cross/mean/adjoint fees for
the identical maps. It does not shrink the true scattering error,
recompute a full returned \(R_*\), remove a finite-head path, or
prove the full feedback inverse.

