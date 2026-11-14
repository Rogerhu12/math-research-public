# R133 supplement: all signed frequencies in the Riccati frame and a true infinite-tail neighbourhood

2026-11-14, visible-exact / root. **Proved; 21 exact rational gates actually passed.**

This removes the finite angular band assumption from the high-to-high
coefficient estimate in the current positive-root interval. It supplies
a quantitative neighbourhood for the actual derivative, including an
arbitrary infinite Fourier tail and one complete angular commutator.
The low/high, mean and global boundary equations remain separate
operators; no full BVP inverse or nonlinear contraction is inferred here.

The centre is the same full moving object
\(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\).
The centre alone has degree 32. The perturbed state never receives that
support assumption.

## 1. The exact reference and Fourier norms

Use the full positive reference of
[R133 global reference](R133-supplement-global-positive-reference-and-current-collar.md),
with physical frequencies \(k=4j\), high projection \(|j|\ge97\), and
\(M_0=388\). At each radial point let \(M>0\), \(W_M=p_M+g_M\), and
\[
 T_M=W_M^{-1/2}\begin{pmatrix}p_M&-g_M\\1&1\end{pmatrix},
 \qquad {\cal T}_M=M^{-1/6}T_M.
 \tag{I.1}
\]
The hypotheses used below are precisely
\[
 p_M,g_M>0,\quad
 |\partial_{\log M}\log p_M|,\ |\partial_{\log M}\log g_M|\le1,
 \quad W_M<4,\quad 0\le K/W_M<1 .
 \tag{I.2}
\]
All are already proved for the actual root reference. The frequency
derivatives concern its complete variational definition, not a
differentiation of discrete numerical values.

For \(\sigma=\operatorname{sgn}k\), set
\(S_\sigma=\operatorname{diag}(-i\sigma,1)\). The moving state is
\(h_k=S_\sigma^{-1}{\cal T}_{|k|}Z_k\).
The zero mode is always outside this frame and inside the full head.

Define
\[
 w(k)=(1+|k|/388)^{2/3},\qquad
 \|a\|_{A_w}=\sum_{k\in4\mathbb Z}w(k)|a_k|,\quad
 \|a\|_{A_{w,1}}=\sum_k(1+|k|)w(k)|a_k|.
 \tag{I.3}
\]
Both weights are submultiplicative. The unknown neighbourhood is
\[
 \|q\|_{A^3}:=\sum_k(1+|k|)^3
       (|q_{1,k}|+|q_{2,k}|)\le\rho\le10^{-6}.
 \tag{I.4}
\]
This is the real odd/even moving class, uniformly in the radial
interval. In particular
\[
 \|q_a\|_{A_w},\ \|\partial_\phi q_a\|_{A_w},\
 \|q_a\|_{A_{w,1}},\ \|\partial_\phi q_a\|_{A_{w,1}}
 \le\rho .
 \tag{I.5}
\]
The largest weight used in the last expression has order \(8/3<3\).
There is no analytic-strip conclusion in (I.4).

## 2. Arbitrary frequency ratios, including crossing of the two signs

Let \(M,N\ge388\) and \(R=\max(M,N)/\min(M,N)\).
From (I.2), \(R^{-1}\le W_M/W_N\le R\). For either
\(\epsilon=1\) or \(-1\), the exact identity is
\[
 T_M^{-1}\operatorname{diag}(\epsilon,1)T_N
 =
 \frac{\epsilon(1,-1)^t(p_N,-g_N)
              +(g_M,p_M)^t(1,1)}
      {\sqrt{W_MW_N}} .
 \tag{I.6}
\]
Its norm is at most
\(\sqrt2(\sqrt{W_N/W_M}+\sqrt{W_M/W_N})
 \le2\sqrt2\,R^{1/2}<3R^{1/2}\).
Thus, for both frequency signs,
\[
 \|{\cal T}_M^{-1}S_\sigma S_\tau^{-1}{\cal T}_N\|
                 <3R^{2/3}.
 \tag{I.7}
\]
This bound permits arbitrarily distant frequencies. No interval of
indices and no persistence of an intermediate high mode is assumed.

The logarithmic derivative of \({\cal T}_M\) has norm at most \(5/3\),
as follows directly from (I.2) and the explicit derivative in G.9–G.11.
For equal signs and \(R\le2\),
\[
 N\|{\cal T}_M^{-1}{\cal T}_N-I\|
 \le(5/3)R^{5/3}|M-N|<6|M-N|.
 \tag{I.8}
\]
The last constant follows from the exact cubed inequality
\((5/3)^3 2^5<6^3\).
For \(R\ge2\), (I.7) and \(N/|M-N|\le2\) instead give
\[
 N\|{\cal T}_M^{-1}{\cal T}_N-I\|
                       \le8|M-N|R^{2/3}.
 \tag{I.9}
\]
At \(M=N\), the equal-sign difference is exactly zero.

For opposite signs, \(|k-n|=M+N\ge N\), so (I.7) gives
\[
 N\|{\cal T}_M^{-1}S_\sigma S_\tau^{-1}{\cal T}_N-I\|
                    \le4|k-n|R^{2/3}.
 \tag{I.10}
\]
Finally
\(R\le1+|k-n|/388\). These inequalities are full matrix-kernel
bounds, including the sign change missed by a nearby-frequency
band argument.

## 3. Complete scalar transport and structured local reaction

Conjugate the complete high scalar transport \(P_Hd\partial_\phi P_H\).
Retain the exact skew-adjoint operator
\[
 {\cal B}_d=P_H(d\partial_\phi+d_\phi/2)P_H
 \tag{I.11}
\]
on the real physical circle. Its remainder has kernel
\[
 in\,d_{k-n}
  ({\cal T}_{|k|}^{-1}S_\sigma S_\tau^{-1}{\cal T}_{|n|}-I)
                 -i(k-n)d_{k-n}I/2 .
\]
Equations (I.8)–(I.10), followed by the ordinary convolution
\(\ell^1\)-\(\ell^2\) inequality, prove
\[
 \|{\cal E}_d\|_{\ell^2\to\ell^2}
                  \le\frac{17}{2}\|d_\phi\|_{A_w}.
 \tag{I.12}
\]
Real \(A^3\) coefficients in (I.4) give the required circle
regularity. The skew realization can equivalently be constructed
by symmetric smooth Fourier approximation with the same energy
identity. The projections are the fixed complete high projections.

Consider a local reaction coefficient of the actual structured form
\[
 B(\phi)=\begin{pmatrix}a&Kb\\c&e\end{pmatrix}.
\]
For each input and output pair its four rank-one terms give
\[
 \|{\cal T}_M^{-1}S_\sigma B_\ell S_\tau^{-1}{\cal T}_N\|
 \le 2R^{2/3}(|a_\ell|+|e_\ell|+|b_\ell|+4|c_\ell|).
 \tag{I.13}
\]
To verify this directly, the diagonal terms have factors at most
\(\sqrt2R^{2/3}\); the upper-right term has factor at most
\(2K/\sqrt{W_MW_N}\,(M/N)^{1/6}\le2R^{2/3}\);
the lower-left factor is at most
\(\sqrt{W_MW_N}(M/N)^{1/6}\le4R^{2/3}\).
The larger last coefficient in (I.13) is therefore valid.
All phases in \(S_\sigma,S_\tau\) have modulus one.
Consequently
\[
 \|{\cal E}_B\|
 \le2(\|a\|_{A_w}+\|e\|_{A_w}
                    +\|b\|_{A_w}+4\|c\|_{A_w}).
 \tag{I.14}
\]
In particular an unknown infinite reaction tail has no implicit
band-dependent factor.

## 4. The entire primitive, including low intermediate modes

Use the exact derivative B.3–B.4 in
[the complete moving equation](R133-supplement-complete-moving-band-and-mean-parameter-Schur.md):
\[
 {\cal N}h=-2\beta Q_\phi I(uh_1+Kvh_2),\qquad
 I=\partial_\phi^{-1}P_{\ne0}.
 \tag{I.15}
\]
The only deleted intermediate coefficient is its exact zero mode.
Every nonzero intermediate frequency has \(\|I\|\le1/4\).
We deliberately use this complete bound, even when both outside
frequencies are high. It remains valid when two arbitrary
perturbation tails create a small nonzero intermediate frequency.

Write \(U=\|u\|_{A_w}\), \(V=\|v\|_{A_w}\), and
\(U_1=\|u_\phi\|_{A_w}\), \(V_1=\|v_\phi\|_{A_w}\).
Apply the rank-one proof of (I.13) separately to every pair of
coefficient frequencies, use
\(w(\ell_1+\ell_2)\le w(\ell_1)w(\ell_2)\), and sum the absolute
primitive kernel. The complete result is
\[
 \|{\cal E}_{\cal N}\|
 \le|\beta|(U_1U+|K|V_1V+U_1V+4V_1U).
 \tag{I.16}
\]
The factor is \(2|\beta|\times(1/4)\times2=|\beta|\).
This estimate covers both signs and all infinite outputs.

The remaining rank-one term
\(\gamma\langle h_2\rangle J(K)Q_\phi\) has exactly zero high-to-high
part because the *input* high mean vanishes. Its low-to-high output
need not vanish in the new neighbourhood. That entire column and
the new high-to-mean row must be kept in the head coupling theorem.

## 5. Actual centre consumption with an infinite perturbed state

The actual centre bounds P.8 are
\[
 |\beta|<9/5,\quad K<61/100000<1,\quad
 ( \|u_c\|_{A^0},\|v_c\|_{A^0},
   \|u_{c,\phi}\|_{A^0},\|v_{c,\phi}\|_{A^0})
 <(13,9/5,216,86).
\]
Its support alone has \(|k|\le128\).
The exact gate \((129/97)^2<2^3\) gives
\[
 (U_c,V_c,U_{1,c},V_{1,c})<(26,18/5,432,172).
 \tag{I.17}
\]
For the \(A_{w,1}\) versions, multiplying these four bounds by 129
is sufficient. These support conversions are not applied to \(q\).

Let \(Q=Q_c+q\). In comparing coefficient remainders, choose a
single frame obeying (I.2), and evaluate *both* \(Q\) and \(Q_c\)
coefficient kernels in that frame.
For the actual derivative its principal speed must be
\(-\gamma\langle v_c+q_2\rangle\).
The change \(\gamma\langle q_2\rangle J\partial_\phi\) is not treated
as a bounded remainder. The uniform root construction must instead
use this actual new speed; its coarse speed and root margins are
checked in the neighbourhood inverse theorem.

With \(d=-\beta I(u^2+Kv^2)\), projection is contractive in \(A_w\),
so
\[
 \|\Delta d_\phi\|_{A_w}
 \le(2664/25)\rho+(18/5)\rho^2 .
 \tag{I.18}
\]
For \(L_0\) the coefficients \(a,e,b=c\) are exactly
\[
 a=-\beta(1+3u^2+Kv^2),\quad
 e=\beta(1-u^2-3Kv^2),\quad b=c=-2\beta uv .
\]
Their polynomial differences and (I.14) give
\[
 \|\Delta{\cal E}_{L_0}\|
 \le(47952/25)\rho+(324/5)\rho^2 .
 \tag{I.19}
\]
The complete primitive difference from (I.16) is
\[
 \|\Delta{\cal E}_{\cal N}\|
 \le(83754/25)\rho+(63/5)\rho^2 .
 \tag{I.20}
\]
For example its linear coefficient before multiplying \(9/5\) is
\[
 (432+26)+(172+18/5)+(432+18/5)+4(172+26)=9306/5.
\]
Both mixed terms and the two-tail quadratic term occur.

Combining (I.12), (I.18)–(I.20), with exact rational arithmetic,
\[
 \boxed{\ \|\Delta{\cal E}\|
       \le6174\rho+108\rho^2<6200\rho,\qquad
                   0<\rho\le10^{-6}.\ }
 \tag{I.21}
\]
At \(\rho=0\) the difference is zero.
This is a bound for the whole high coefficient remainder, not just
a truncation of its matrix.

## 6. One full angular commutator still lies in A cubed

The exact commutator kernel is
\[
 [\partial_\phi,{\cal E}]_{kn}=i(k-n){\cal E}_{kn}.
\]
In every proof above one may replace the coefficient norms by
\(A_{w,1}\), since \(1+|\ell_1+\ell_2|\le
(1+|\ell_1|)(1+|\ell_2|)\). The complete centre bounds increase
by at most 129 and every perturbation bound remains \(\rho\)
by (I.5). Hence
\[
 \boxed{\ \|[\partial_\phi,\Delta{\cal E}]\|
       \le796446\rho+108\rho^2<800000\rho.\ }
 \tag{I.22}
\]
This includes the derivative of the complete primitive with all
its intermediate modes. Replacing \(R^{2/3}\) by the coarser
logarithmic \(R^{5/3}\) estimate would have required an unpaid
additional derivative here.

When differentiating (I.11), the highest derivative has coefficient
\(d_\phi\), while the lower extra term is \(d_{\phi\phi}Z/2\).
In the same neighbourhood
\[
 \|\Delta d_\phi\|_\infty<110\rho,\qquad
 \|\Delta d_{\phi\phi}\|_{A_w}
       \le129(2664/25)\rho+(18/5)\rho^2.
\]
Adding half of the latter to (I.22) yields a complete increase below
\(810000\rho\) in the first triangular lower-order forcing constant.

For the current root reference, the old centre constants were
\[
 E_c=18262183/1261,\qquad C_1=4538112,\qquad h=9\,10^{-6}.
\]
The actually executed rational gates give
\[
 h(E_c+6200\rho)<2/15,\qquad
 h(E_c+6200\rho+5+110\rho)<2/15 .
 \tag{I.23}
\]
Thus, whenever the new actual speed satisfies the same paid coarse
reference hypotheses, the high base and once-differentiated
two-port equations retain resolvent \(15/13\).
The once-differentiated forcing has the explicit triangular term
\[
 (4538112+810000\rho)\|Z\|_{L^2}.
 \tag{I.24}
\]
It is a lower-order forcing term, not a new exponential growth rate.

This statement does not assign the old finite-band \(641^s\)
source factor to the new low-to-high column. Its complete infinite
output has to be bounded at its actual source order. Similarly,
a second angular commutator is not granted by \(A^3\) alone.

## 7. Executed budget and exact scope

The source is
[scripts/fourfold_codazzi_infinite_tail_Riccati_frame.mjs](../scripts/fourfold_codazzi_infinite_tail_Riccati_frame.mjs);
the complete executed report is
[notes/2026-11-14-R133-infinite-tail-Riccati-frame-rational.json](../notes/2026-11-14-R133-infinite-tail-Riccati-frame-rational.json).

The complete arithmetic function ran in the available V8 runtime;
all 21 normalized BigInt gates passed. The Node file is a direct
reproduction wrapper. These calculations consume previously proved
same-object text bounds and do not reconstruct any lost native
candidate arrays.

The new results are the arbitrary signed-frequency frame kernel,
the complete transport/reaction/primitive estimates, the actual
\(6200\rho\) high remainder budget and its \(A^3\) first-commutator
contract. The remaining head, mean, actual reference-speed margins,
negative return, positive body, physical outer rows and scalar
parameter Schur must remain in the complete problem. A high block
neighbourhood is not by itself an exact closed surface or a
same-space nonlinear contraction.
