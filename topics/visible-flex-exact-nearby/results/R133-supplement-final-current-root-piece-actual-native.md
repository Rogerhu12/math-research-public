# R133: the final moving centre's complete physical root-piece port

2026-11-14, visible-exact / phase_inverse. **Proved by the actual complete
15-gate run.** This instantiates the three-state physical strict-to-Airy
construction at the final M32 moving centre, not at the former M256
amplitude-3/4 centre. The exact candidate index SHA is
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`;
all five lossless polynomial shards were checked by the candidate loader.
The exact amplitude and metric parameter are

\[
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 \nu=-\frac{2572625729470897}{72057594037927936}.
\tag{A.1}
\]

The whole original affine parameter interval \(|\eta|\le10^{-9}\), the
primitive infinite remainder, all angular frequencies of the variation,
and both original mean states are included.

## 1. Actual statement and domains

Let

\[
 r_c=\frac{2147184947341121}{9007199254740992},\quad
 h=2^{-37},\quad \delta=2^{-36}.
\tag{A.2}
\]

For the original physical Jacobi variation, in the original angle
\(\theta\), use

\[
 E_0=\|(h_1,qh_2)\|_{L^2_\theta},\quad
 E_1=\|(\partial_\theta h_1,q\partial_\theta h_2)\|_{L^2_\theta},
 \quad Y_2=\|h_2\|_{L^2_\theta},\qquad q=\sqrt{-K}.
\tag{A.3}
\]

For any fixed \(r_0\) with
\(r_c\le r_0<r_*^--h\), the complete forward physical evolution from
\(r_0\) to \(r_*(\eta)-h\), followed by the proved true fixed-radius
graph to \(T=-\delta\), obeys

\[
\begin{split}
 \|U(-\delta)\|_{\mathcal E}
 <{}&5.264044E_0(r_0)+1.008631E_1(r_0)+2.269796Y_2(r_0)\\
 &+0.028915503\|f\|_{L^2_rH^1_\theta(\Omega_s)}
   +0.001826455\|f\|_{H^1(\Omega_g)} .
\end{split}
\tag{A.4}
\]

Here \(\Omega_s\) is the physical strip from \(r_0\) to the true
parameter-dependent radius \(r_*(\eta)-h\). The graph domain
\(\Omega_g\), its physical source convention, and the padded full Airy
norm \(\mathcal E\) are those of
`R133-supplement-current-moving-body-complete-Airy-collar.md` and its
actual restored native. The second source norm includes its radial
derivative; no anisotropic source is silently relabelled as another
one. The strict source may instead be paid in \(L^1_rH^1_\theta\), with
coefficient less than \(8.542470\).

In particular (A.4) applies at
\(r_0=r_a=0.2383878742994\), the end of the new complete strict
certificate. There is no overlap requirement on the forcing: start
the strict source integral at the chosen \(r_0\).

This is a genuine physical Jacobi port. A moving-coordinate Jacobi
solution still requires the published residual-sensitive variation
bridge before it may be used as the input in (A.3). The centre is an
exact polynomial reference, not an assumed solution of the nonlinear
equation. No reverse common-piece estimate, positive regular closure,
whole-body inverse, or nonlinear existence is claimed here.

## 2. Same actual germ and full physical coefficients

The complete scalar germ is

\[
 \left[\frac{8556839292003943}{36028797018963968},
       \frac{8636031980136455}{36028797018963968}\right].
\tag{A.5}
\]

The actual candidate piece is **2549**, with endpoints

\[
 \left[r_c,\frac{4295308144604611}{18014398509481984}\right].
\tag{A.6}
\]

The entire real interval from \(r_c\) through the complete root
enclosure is inside (A.5) and (A.6). No PPoly join lies in this block.
The right-side trace into piece 2549 is required at \(r_c\); a prior
block must retain its true interface source there. The compact metric
perturbation is identically zero because \(r_c>.18\).

The current producer evaluates all 65 actual dyadic cubic rows and
the original complete intrinsic primitive on the closed radial
envelope. It then applies the exact physical inverse-angle derivative
formulas to the moving Fourier fields. The moving Fourier variable
is not treated as the original physical angle. The true gates give

\[
 \begin{gathered}
 -v>0.4516410295,\qquad
 K'>60.03578844,\qquad |K'|<60.37288887,\\
 q^2<0.000691730442,\qquad q<0.026300769,\qquad
 q(r_*(\eta)-h)>2.09001878\,10^{-5},\\
 r_*^+-h-r_c<1.145762636\,10^{-5}.
 \end{gathered}
\tag{A.7}
\]

The terminal negative type follows from the exact root quotient

\[
 -K(r)=(r_*(\eta)-r)
       \int_0^1K'(r_*(\eta)+t(r-r_*(\eta)))\,dt.
\tag{A.8}
\]

It is not inferred by cropping an interval box that straddles the
root. The full physical angular derivative bounds used through order
two may safely be rounded to

\[
 (U_0,U_1,U_2)<(.627409,6.454948,168.398989),\qquad
 (V_0,V_1,V_2)<(1.787872,6.917565,181.671356).
\tag{A.9}
\]

The native also retains the complete higher jets used by the
inverse-angle formula. These are full sums with the proved primitive
tail, not samples on an angular grid.

## 3. Complete three-state energy

For \(y=\operatorname{diag}(-1,1)h\), the original physical system is

\[
 y_r=(dI+aJ(K))y_\theta+Ly+\operatorname{diag}(-1,1)f,
 \quad d=\gamma u,\quad a=-\gamma v>0,\quad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
\tag{A.10}
\]

Its exact local identity \(L_{12}=KL_{21}\) makes the off-diagonal
part of \(HL+L^*H\) vanish for \(H=\operatorname{diag}(1,-K)\).
In the forward energy identity the remaining derivative contribution
\(-K'/(-K)\) in the lower diagonal is nonpositive. Retaining this
sign before taking an upper bound is essential. Differentiating once
in \(\theta\) gives the full commutators \(A_\theta y_\theta\) and
\(L_\theta y\). The separate second equation gives an ordinary
\(L^2\) estimate for \(y_2\), including its mean. Consequently

\[
 \begin{pmatrix}E_0\\E_1\\Y_2\end{pmatrix}'
 \le M\begin{pmatrix}E_0\\E_1\\Y_2\end{pmatrix}
     +\|f\|_{H^1_\theta}\begin{pmatrix}1\\1\\1\end{pmatrix},
 \qquad
 M\le\begin{pmatrix}
 11.402360&0&0\\199.192101&18.833296&0\\
 8.217558&2.001777&11.135676
 \end{pmatrix}.
\tag{A.11}
\]

All entries follow from the complete physical coefficient formulas
in Sections 2–3 of
`R133-supplement-complete-common-root-piece-to-Airy-port.md`;
(A.9) and the new complete intrinsic boxes replace that theorem's
old centre values. No numerical constant of the old centre is used.

The complete positive exponential gives

\[
 P_s\le
 \begin{pmatrix}
 1.000130653&0&0\\.002282665&1.000215809&0\\
 .000094193&.000022940&1.000127597
 \end{pmatrix}+10^{-90}{\bf1}_{3\times3}.
\tag{A.12}
\]

The producer sums through degree 24 and pays the entire remaining
matrix series by \(s^{25}/[25!(1-s/26)]\),
\(s=\|M\|_\infty(r_*^+-h-r_c)\); the actual remainder is below
\(5.617\,10^{-91}\). Positivity makes the same matrix valid for
**every forward subinterval** and every source insertion time. This
proves the extension from \(r_c\) to arbitrary \(r_0\) in (A.4).
The ordinary characteristic/Volterra construction on this strict
interval, followed by the displayed uniform energy bounds and
density, supplies existence as well as the estimates.

## 4. Actual graph, two states, and the exact weight cancellation

The actual fold satisfies \(q_{\rm can}=bq_{\rm phys}\) and
\(F=\operatorname{diag}(b^{-1/2},b^{1/2})\). Hence

\[
 H_{\rm can}^{1/2}F^{-1}=\sqrt b\,H_{\rm phys}^{1/2}.
\tag{A.13}
\]

Apply this before estimating either ordinary component. Including
the true angular Jacobian and the derivative of the frame gives

\[
 W_g\le\begin{pmatrix}
 .568789128&0&0\\1.669897145&.568789128&0\\0&0&2.229183990
 \end{pmatrix}.
\tag{A.14}
\]

The complete current graph propagation, already proved in the
restored 27-gate fold certificate, is

\[
 P_g\le\begin{pmatrix}
 1.768214932&0&0\\2.265685498&1.768214932&0\\
 2.585159\,10^{-9}&5.471868\,10^{-11}&1.000002574
 \end{pmatrix}.
\tag{A.15}
\]

At \(T=-2^{-36}\), put \(q_-=2^{-18}\). The full Airy comparison
row is

\[
 (A_H,A_H,A_Y),\qquad
 A_H=1+q_-^{1/3}/6,\qquad
 A_Y=\sqrt{(\sqrt{17}/4)^{1/3}}+5q_-^{1/3}/6.
\tag{A.16}
\]

It follows from the two-state spectral inequality and
\(Y^{5/6}H^{1/6}\le5Y/6+H/6\), retaining the independent mean
states at frequency zero. The actual multiplication order is

\[
 (A_H,A_H,A_Y)P_gW_gP_s
 <(5.264044,1.008631,2.269796).
\tag{A.17}
\]

Summing the unrounded entries, then applying Cauchy–Schwarz on the
true strict radial interval, gives the first source coefficient in
(A.4). The independent graph source is
\(A_H(sE_0+sE_1)+A_YsY_2\), giving its second coefficient.
At no point is the terminal \(q^{-1}\) used to replace \(Y_2\).
All matrices act on the full two-state physical problem and preserve
both means. Equation (A.17) does not interchange the factors.

## 5. Native identity, reproduction, and saved startup failures

Source: `scripts/fourfold_codazzi_current_moving_root_piece_ports_v2.py`,
SHA256 `ba80f199f591f7fae3bad6d05f09b59e9c2b7b8fc2845e875820059a5f0ff5e0`.
The only change from the prepared current-centre producer is its
candidate-location check: the complete index must have the graph's
exact SHA and occur among the graph's recorded inputs. A restored
index may reside in a different directory. The unchanged complete
loader verifies the bytes, size, shape, and common endpoints of every
polynomial shard, and the exact coordinates, object, amplitude and
\(\nu\) are checked again. This is not a relaxed numerical identity.

Native: `notes/2026-11-14-R133-current-root-piece-v2-ac1-native.json.gz`,
SHA256 `aaf8e60f981010b00d98c847c31ef221dee705772329ede58fb93fda85d351ef`.
All 15 gates passed in an actual normal-exit run, about 2.39 seconds.

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/fourfold_codazzi_current_moving_root_piece_ports_v2.py --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json --graph notes/2026-11-14-R133-current-moving-fold-Airy-restored-native.json.gz --out notes/2026-11-14-R133-current-root-piece-v2-ac1-native.json.gz
```

Two earlier startup attempts reached only file input: the restored
fold native was temporarily absent while the repository's sparse
paths were being synchronized. Both exited with `FileNotFoundError`
before any mathematical gate. Neither wrote a native conclusion or
was counted as a failed inequality. After the identical fold file
was restored, the complete computation above ran from its beginning.
