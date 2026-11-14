# R133 supplement: a genuine physical Wiener conjugacy on strip 1/128

2026-11-14, visible-exact-astra-0df / phase_inverse. **Proved by the
actual public Actions run 43588332723, attempt 1.**

The same explicit family

\[
 Q_\delta=\overline Q+\delta Z,\qquad
 \nu_\delta=\nu_0+\delta,\qquad \eta=\eta_0
 \tag{W.1}
\]

contains a parameter \(\delta_*\), with

\[
 |\delta_*|<9.368259853002\,10^{-11},
 \tag{W.2}
\]

whose true two-ray return has an exact real analytic conjugacy
\(\mathcal H\) satisfying

\[
 \mathcal H\circ P_{\delta_*}=\mathcal H+\Omega_{15},\qquad
 \Omega_{15}=\frac\pi2
       \frac{5831714953207175+\sqrt5}{21212218271020390}.
 \tag{W.3}
\]

Its periodic part belongs to the physical moving-label Wiener algebra
\(\mathcal A_{1/128}\), with physical Fourier frequencies \(4j\).
If \(G=K_{48}\circ H\) is the exact finite coordinate from the
completed full-Laurent certificate, the actual bounds are

\[
 \|\mathcal H-G\|_{\mathcal A_{1/128}}
                   <2.210026409642\,10^{-7},
 \tag{W.4}
\]

\[
 \|\mathcal H'-G'\|_{\mathcal A_{1/128}}
                   <0.0002246235683080,
 \quad
 \|\mathcal H'\|_{\mathcal A_{1/128}}<1.016384090833,
 \quad
 \|\mathcal H'\|_{C^0(\mathbb R)}<1.015747716790.
 \tag{W.5}
\]

The word physical fixes the angular scale \(\phi\), as opposed to
the normalized angle \(x=4\phi\). It does not replace the moving
angle by the separate implicit physical-angle chart \(\theta\).

This is an existence assertion in (W.1). It does not identify
\(\delta_*\) with a parameter selected using another bookkeeping
loss without an additional uniqueness argument. In particular it
does not assert a true PDE solution branch or the completed strong
return inverse.

## 1. Actual inputs and retained failed losses

The sole mathematical process consumed the completed original
public R31 certificate and the same-run K48 certificate:

| Input | SHA256 |
|---|---|
| R31 from run 43586895661 | `d6e59dfa851fb7d385f6281389221408cc132f90be8c2b1577fdd2be9a348d61` |
| K48 from that same run | `a44d6a6b2d0bad07d60e323142fd266b8dd91a645afa9d306fe22c8794a84f60` |
| Original root contract | `1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43` |

No original scalar germ, transported polynomial, complete residual,
Laurent exponential or R31 constant was recomputed. The complete
same-family inputs and their proof are those of
[the R31 input theorem](R133-supplement-complete-explicit-family-circle-KAM-inputs-and-gates.md).
The normalized initial error is
\(\epsilon<5.855162408126\,10^{-13}\), with
\(s_0=1/16\), \(S=63/1000\), and parameter radius \(10^{-8}\).

All eight exact loss trials are retained in the native output:

| Loss | R31 smallness gate | Physical \(\mathcal A_{1/128}\) inverse-composition gate |
|---|---|---|
| \(3/200\) | pass | fail |
| \(1/100\) | pass | fail |
| \(3/400\) | pass | fail |
| \(1/200\) | pass | fail |
| \(1/250\) | pass | pass |
| \(7/2000\) | fail | fail |
| \(3/1000\) | fail | fail |
| \(1/400\) | fail | fail |

The selected loss \(d_0=1/250\) gives

\[
 s_\infty=s_0-4d_0=93/2000,
 \qquad \epsilon<5.855162408126\,10^{-13}
       <6.512601262693\,10^{-13}
       <\hbox{the proved R31 threshold}.
 \tag{W.6}
\]

Both displayed decimal bounds are rounded in the safe direction.
The parameter-domain margin exceeds
\(9.906317401469\,10^{-9}\); the R31 angular-domain margin exceeds
\(0.0004991159894361\).

## 2. The inverse and composition cost is paid in the same algebra

R31 supplies a normalized lift \(h_\infty=\mathrm{id}+u\) with

\[
 F_{\delta_*}\circ h_\infty
       =h_\infty\circ R_{4\Omega_{15}},\qquad
 F_\delta(x)=4G(P_\delta(G^{-1}(x/4))).
 \tag{W.7}
\]

On the final normalized strip the actual estimates are

\[
 \|u\|<H_c:=8.840105638565\,10^{-7},\qquad
 \|u'\|<H_d:=0.000221002640965<1.
 \tag{W.8}
\]

At physical \(\sigma=1/128\), evaluation of **all** exact H and
K48 coefficients gives

\[
 G_0=\|G-\mathrm{id}\|_{\mathcal A_\sigma}
             <0.003469118991384,
 \qquad G_1=\|G'\|_{\mathcal A_\sigma}<1.016159467265.
 \tag{W.9}
\]

The genuine inverse-composition gate is

\[
 s_\infty-4\sigma-4G_0-H_c
                       >0.0013726400239022>0.
 \tag{W.10}
\]

To justify it directly, solve \(v=-u\circ(\mathrm{id}+v)\) in the
normalized Wiener algebra on width \(4\sigma+4G_0\), in the ball
\(\|v\|\le H_c\). The Banach algebra exponential estimate and
(W.10) make every composition legitimate; the full derivative bound
\(H_d<1\) makes this a contraction. Therefore
\(h_\infty^{-1}=\mathrm{id}+v\) exists there, and

\[
 \|v\|\le H_c,\qquad \|v'\|\le\frac{H_d}{1-H_d}.
 \tag{W.11}
\]

The first bound follows from the fixed-point equation. The second
follows by differentiating it and summing the same Wiener-algebra
geometric series. It does not convert a sup bound to a Fourier bound.
Now define

\[
 \mathcal H(\phi)=\frac14 h_\infty^{-1}(4G(\phi)).
 \tag{W.12}
\]

The image margin (W.10) pays this full composition. Equations
(W.7) and (W.12) prove (W.3) exactly, while
\(H_c/4\), \(G_1H_d/(1-H_d)\), and \(G_1/(1-H_d)\) give
(W.4)--(W.5). The separately evaluated real \(G'\) gives the last
bound in (W.5). The real maps are orientation preserving; the
conjugacy is a real degree-one lift.

## 3. Original evidence and exact scope

The mathematical source is
`scripts/fourfold_codazzi_phase_R31_strip_refinement.py`, SHA
`c1ca128ce18007ec118565beb013a97eaf7c0ccb11962caee474eec092a6c069`.
The actual original native is
`notes/phase_strip_refinement_ci/run-43588332723-1/consumers/R31-strip-refinement.json.gz`,
3356 bytes, SHA
`dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854`.
The sibling process and publication records preserve the actual
public run, source, checkout and return code.

The target's all-fourth-root **principal** gap remains \(1/(68|j|)\),
and the circle homological constant is \(17/4\). This wider positive
strip is now available to a subsequent actual nonmean first-symbol
normalization. The true \(\beta/j\), its root/positive-port matching,
the complete strong remainder, and the true PDE response are still
separate calculations; (W.3) does not pay them.
