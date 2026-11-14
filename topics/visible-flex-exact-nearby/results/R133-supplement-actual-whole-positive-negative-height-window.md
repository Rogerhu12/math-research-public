# R133: the complete positive high inverse in the negative height window

2026-11-14, visible-exact / phase_inverse. **Proved and actually run.**
The same complete final ac1 centre, all 4,650 positive-body boxes,
the whole original \(|\eta|\le10^{-9}\) interval and the same global
Riccati reference admit the negative window needed by the genuine
vector-height contact. The selected cutoff remains **\(N=97\)**.
The complete interior Volterra operator plus the already proved
actual negative-order exterior graph satisfies

\[
                 \boxed{\chi_-<0.711062297<1.}
\tag{H.1}
\]

Thus the entire unbounded high block is invertible in this window,
with all head, mean and affine columns retained. This is not a
claim that the negative return or the remaining 193-state/global
Schur problem has been inverted.

## 1. Exact window and unchanged actual reference

The interval is \([r_b,R]\),
\(r_b=0.2384058742994\), \(R=25/8\), at candidate
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.
Let \(Z_k\) be the exact canonical state (P.7) of
`R133-supplement-actual-whole-positive-N97-inverse.md`. In particular
the global reference \(p_M,g_M\) is unchanged from the root through
the actual exterior, and \(M=|k|=4|j|\).

For all \(|j|\ge97\), define

\[
 t=5/3,\qquad w_k=(388/M)^t,\qquad Y_k=w_kZ_k.
\tag{H.2}
\]

The compatible vector-height state is exactly

\[
 \widetilde Z_k(r)=n(r)M^{-5/3}Z_k(r)
                  =n(r)388^{-5/3}Y_k(r),
 \qquad n(r)=a(r)^2/m(r)^2.
\tag{H.3}
\]

This theorem uses the frequency weight (H.2), which is constant
in the radial variable. Equation (H.3) is a pointwise norm
conversion. It does **not** move a variable \(n(r)\) through the
radial equation or omit \(n'/n\). Equivalently, the controlled
height norm is
\(\sup_r 388^{5/3}\|\widetilde Z(r)\|_2/n(r)\).
A plain unweighted \(L^\infty_r\) height norm or a different
height-source space requires the corresponding actual factors.

The mean is independent, as in the full exterior theorem. It is
not defined by taking a limit of (H.2) or (H.3) at \(k=0\).

## 2. Complete finite-band kernels before and after conjugation

The actual background has 32 modes; the complete coefficients of
its local and primitive terms have total outer frequency band 64.
The exact primitive intermediate still has its complete divisor
bound \(N-32\). No angular projection is inserted between its
two multipliers.

For high input and high output, a nonzero coefficient has
\(|j-l|\le64\). Hence the two frequency signs agree and

\[
 \max(M/L,L/M)\le R_0=161/97,
 \qquad w_M/w_L\le R_0^{5/3}<2.326788470.
\tag{H.4}
\]

The bounded remainder is first estimated by its **complete
absolute Fourier kernel**. In (C.14)–(C.15) of the whole-positive
producer theorem, replace the same-frequency supremum envelope
\(\mathcal B_\infty\) by the complete Wiener envelope
\(\mathcal B_A\). With the unchanged full quantities
\(\mathcal F_i\), \(d_\phi\), \(K/W\) and actual \(\beta\), set

\[
 E_{i,\rm abs}=\frac{13}{2}\|d_\phi\|_{A^0}
       +2\mathcal B_{A,i}
       +\frac{24\cdot32}{97}\mathcal B_{A,i}
       +\frac{4|\beta|}{97-32}\mathcal F_i.
\tag{H.5}
\]

The exact grounded upper-right factor \(K\), the two full
primitive convolutions, and both Fourier signs remain in this
bound. Multiplying every complete kernel by its scalar weight
ratio gives the valid conjugated bound
\(R_0^{5/3}E_{i,\rm abs}\). This does not rely on multiplying an
arbitrary \(L^2\) operator norm by a frequency ratio: the complete
absolute kernel is paid **before** that multiplication.

## 3. The shared unbounded skew transport has its own commutator

The principal diagonal model contains the actual shared skew
transport

\[
 \mathcal D=d\partial_\phi+\tfrac12d_\phi.
\tag{H.6}
\]

Its compression to the complete high space is still skew-adjoint.
Indeed the removed finite head has smooth finite coefficient
support, so the compression differs from the original skew
transport by a bounded skew finite-rank correction on the usual
domain. This supplies its full unitary propagation, not only a
formal skew matrix on finitely many test modes. The positive
diagonal damping is retained in each stable/unstable reference
evolution.

The new commutator is not covered by (H.5), because (H.6) is
unbounded. Its exact high Fourier entry is

\[
 \frac{i(k+l)}2\,\widehat d(k-l)
       \left[\left(\frac{|l|}{|k|}\right)^t-1\right].
\tag{H.7}
\]

For \(1\le x\le R_0\), convexity of \(x^t\), \(t=5/3\), makes
its secant slope increasing. If \(|l|\ge|k|\), divide (H.7)'s
scalar magnitude by \(|k-l|\) to obtain

\[
 \frac{x+1}{2}\frac{x^t-1}{x-1}
 \le C_t:=\frac{(R_0+1)(R_0^t-1)}{2(R_0-1)}.
\tag{H.8}
\]

If \(|k|\ge|l|\), the mean-value estimate for \(x^{-t}\) gives
the smaller bound \(t(R_0+1)/2\le C_t\). Thus the full
commutator obeys

\[
 \|w\mathcal D w^{-1}-\mathcal D\|_{L^2_H\to L^2_H}
 \le C_t\|d_\phi\|_{A^0},\qquad C_t<2.674308009.
\tag{H.9}
\]

The two high signs cannot couple directly through the band 64;
all couplings through the retained head stay in the source/Schur
columns. The original scalar half-density correction is already
included in (H.5), and (H.9) pays exactly the additional shared
transport conjugation. No bare pullback is declared close to the
identity in the same norm.

## 4. Actual complete Volterra computation

Use the same true all-frequency Riccati lower bounds and damping
\(k_i=388a_{-,i}w_i/2\) as the base whole-positive consumer.
The complete conjugated remainder is

\[
 E_{i,-}=R_0^{5/3}E_{i,\rm abs}+C_t\|d_\phi\|_{A^0}.
\tag{H.10}
\]

The actual closed-row native gives

\[
 \begin{gathered}
 \int E_{\rm abs}\,dr<574.218695,\qquad
 \int C_t\|d_\phi\|_{A^0}\,dr<.451459774,\\
 \int E_-\,dr<1336.536897.
 \end{gathered}
\tag{H.11}
\]

The two complete directed sweeps
\(A_s'=E_- -kA_s\) and \(-A_u'=E_- -kA_u\), each from zero
at its incoming endpoint, give

\[
 \tau_-\le\sup_r\sqrt{A_s(r)^2+A_u(r)^2}
           <.707058297.
\tag{H.12}
\]

Each row's maximum is taken over its entire closed interval,
not only at a chosen endpoint. The worst row is again 2943.
Its forward/backward majorants are below
\(.500010089\) and \(.499921340\), respectively.

The full same-object exterior theorem
`R133-supplement-final-regular-negative-window-and-height-ports.md`
has already paid its nonlinear derivative, mean and independent
outer-height column on \(H^{-3/2}\). Its complete high reflection
is below .004004. The common scalar factor relating (H.2) to
(H.3) cancels on this high-to-high boundary row. Hence

\[
 \chi_-<.707058297+.004004<.711062297<1,
 \qquad (1-\chi_-)^{-1}<3.460954.
\tag{H.13}
\]

This is a genuine complete Hilbert-space inverse for the positive
high problem, obtained by the full bounded Volterra-plus-boundary
operator. Existence for the weighted space follows by complete
Fourier approximation and the uniform conjugated estimates; the
background's finite band is not assigned to the unknown input.

## 5. All ordinary sources, endpoints, and actual jumps

Define the source norm precisely by

\[
 F_-^2=\int_{r_b}^{R}
    \|(388/|D|)^{5/3}f_H(r)\|_{H^{1/3}_\phi}^2\,dr.
\tag{H.14}
\]

This is the curvature-Jacobi ordinary source in its declared
frequency window. It is not silently changed to an unweighted
physical-height \(L^2\) source; the vector-height/weak-source
contact must supply its true conversion when that source is used.

Let \(G_-\) include the norm of the complete weighted stable
left input, the independent weighted right affine input, and

\[
 \sum_i C_i
       \|(388/|D|)^{5/3}[h_H]_{r_i}\|_{H^{1/3}_\phi}.
\tag{H.15}
\]

The stable/unstable source kernels use the unchanged diagonal
gap and the complete source frames. The actual source factor
before inversion is below .126139786. The complete bounds are

| Output | Coefficient of \(F_-\) | Coefficient of \(G_-\) |
|---|---:|---:|
| \(\|Y_H\|_{L^\infty_rL^2_\phi}\) | 0.436563951 | 3.460954 |
| \(\|(388/|D|)^{5/3}h_H\|_{L^2_rL^2_\phi}\) | 1.098812 | 8.711065 |
| Sum of both weighted raw endpoint norms | 4.324077 | 34.280040 |

The source has no extra radial derivative requirement. Each true
affine interface is retained with its signed backward unstable
column before taking the norm. Since \(0<w_k\le1\), the already
computed full actual \(A^1\) jump majorant is sufficient for
(H.15). Its complete native value is below
\(3.696950\,10^{-16}\); low and mean jumps remain separately
in the head equations.

## 6. Exact external affine row, mean, and head return

Let \(y_L\) denote the true low nonmean second-component chart
of the exterior theorem, with its same affine convention. Let
\(F_B=\|\langle D\rangle^{-3/2}|D|^2\delta f_B\|_2\), and let
\(r_B\in H^{-3/2}\), \(r_C\in\mathbb R\) be the independent
physical boundary residuals. Dividing that theorem's complete
height row by \(n_R388^{-5/3}\) gives exactly

\[
 \begin{split}
 \|Y_{u,H}(R)\|<{}&.004004\|Y_{s,H}(R)\|\\
 &+388^{5/3}\{
 .001502\|y_L\|_{H^{-3/2}}+.005732F_B\\
 &\hspace{29mm}+22.402\|r_B\|_{H^{-3/2}}+27.111|r_C|\}.
 \end{split}
\tag{H.16}
\]

The independent affine bracket is included in \(G_-\), not in
the small high reflection. The complete attached mean is

\[
 \begin{split}
 |z(R)|<{}&.001092453\,388^{-5/3}
       (\|Y_{s,H}(R)\|+\|Y_{u,H}(R)\|)\\
 &+.000364151\|y_L\|_{H^{-3/2}}
       +.001361613F_B+49.017844|r_C|.
 \end{split}
\tag{H.17}
\]

All appearances of \(n_R\) have canceled in these **boundary
identities** using the same true mean integrating factor; this
does not authorize omitting a radial \(n'/n\) elsewhere. The
overall height translation and original regular outer input
remain independent geometric ports.

Inside the positive body, a high input that feeds a head output
through the finite centre must have \(97\le|j|\le160\). Thus
undoing its frequency weight on that entire coupling shell costs

\[
 (160/97)^{5/3}<2.302751536.
\tag{H.18}
\]

The low-to-high source is first formed by the full actual
operator and then weighted; \(w\le1\) makes the original full
ordinary-source bound valid. Its output through index 160 still
pays its complete \(H^{1/3}\) weight. Equations (H.18) and (P.12)
of the base whole-positive theorem pay the entire interior
head/high pair without commuting the projection through a
multiplier or the primitive. The true exterior mean/high path
is not band-limited by this interior support fact; it is retained
explicitly in (H.17).

## 7. Actual files and scope

Source:
`scripts/fourfold_codazzi_current_positive_negative_window.py`,
SHA256 `3edf00132d9c8ac3724b5538f5a5f2013c0ff222ff7ad40c3c3e36b5541a3fd1`.

Native:
`notes/2026-11-14-R133-current-positive-negative-window-N97-native.json.gz`,
SHA256 `9a35cddd465e8c6c062d1a79fdc24c847e7d5b14684518a6c64b0f17e195ca96`.

The normal-exit actual run took about 11.32 seconds and consumed
all 4,650 rows of the original complete coefficient native,
SHA256 `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`.
It checks the current candidate, full interval, whole original
parameter, unchanged producer and every producer dependency.
The report records the exact rational band ratio, outward Arb
weight and secant, both full sweeps, complete source/reconstruction
bounds, and a digest of every derived weighted/coupling row.

After lossless restoration of the coefficient native, reproduce
with a new output:

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python3 scripts/fourfold_codazzi_current_positive_negative_window.py --coefficients /actual/scratch/current-positive-complete-ac1-native.json.gz --cutoff 97 --out /actual/scratch/new-positive-negative-window-N97.json.gz
```

The complete 193-state head, negative return, true parameter
condition and nonlinear body are still not inverted by (H.13).
The fixed background's band cannot be imposed on an unknown
Fourier correction. The root neighbourhood certificate also
does not automatically extend this full positive-body estimate
to a nonlinear neighbourhood. These distinctions are kept in
the native's explicit permissions.
