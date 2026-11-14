# R133 supplement: the complete nonlinear Sobolev source and its actual derivative loss

2026-11-14, visible-exact / root. **Proved; all 9 new exact rational gates passed.**

The complete conservative remainder is now estimated in the ordinary
source spaces accepted by the true root inverse. This gives quantitative
nonlinear source and Jacobian bounds for an arbitrary infinite angular
tail, retains the even mean, and identifies the exact loss of derivatives.
It does not turn a local inverse into a same-space contraction.

The final centre remains
\(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\).
The actual root interval has length \(h_r=9\,10^{-6}\), uniformly for
the original \(|\eta|\le10^{-9}\).

## 1. Norms and the exact full remainder

Use normalized Fourier \(L^2\) on the fourfold circle, \(k\in4\mathbb Z\).
For a scalar field put
\[
 \|a\|_{A^t}=\sum_k(1+|k|)^t|a_k|,\qquad
 \|a\|_{X_t}=\left(\sum_k(1+|k|)^{2t}|a_k|^2\right)^{1/2}.
 \tag{S.1}
\]
For two-component fields use the sum of the two component norms.
Ordinary \(H^s\) below has Bessel weight \(\langle k\rangle^s\) and
the usual Euclidean component norm. In particular
\(\|a\|_{H^s}\le\|a\|_{X_s}\), without an unpaid equivalence constant.

For \(t\ge0\), submultiplicativity of \((1+|k|)^t\) gives exactly
\[
 \|ab\|_{X_t}\le\|a\|_{A^t}\|b\|_{X_t},\quad
 \|I a\|_{X_t}\le\tfrac14\|a\|_{X_t},\quad
 \|\partial_\phi a\|_{H^s}\le\|a\|_{X_{s+1}},
 \tag{S.2}
\]
where \(I=\partial_\phi^{-1}P_{\ne0}\). The mean has norm at most
one. All convolution sums are complete; \(I\) removes only the
actual intermediate zero coefficient.

Write \(Q=(u,v)\), \(m=\langle v\rangle\),
\(J=\left(\begin{smallmatrix}0&K\\-1&0\end{smallmatrix}\right)\),
\(S_h=h_1^2+Kh_2^2\), and \(B=uh_1+Kvh_2\).
The exact identity from
[the complete flux theorem](R133-supplement-complete-moving-nonlinear-flux-and-metric-remainder.md)
is
\[
 R(Q,h):=F(Q+h)-F(Q)-DF(Q)h
                   =\partial_\phi{\cal A}+{\cal B},
\]
\[
 {\cal A}=-\beta\{I S_h\,Q+2I B\,h+I S_h\,h\}
                         +\gamma\langle h_2\rangle Jh,
\]
\[
 {\cal B}=-\beta\{\langle S_h\rangle Q
                     +2\langle B\rangle h+\langle S_h\rangle h\}.
 \tag{S.3}
\]
No radial equation for the centre is used. This remains the exact
remainder at a nonzero-residual background and on both sides of
every real PPoly interface.

## 2. A full Sobolev remainder and a complete derivative bound

Fix \(s\ge0\), set \(t=s+1\), and let
\[
 \|Q\|_{A^t}\le B_t,\quad \|h\|_{A^t}\le\rho,\quad
 H_t=\|h\|_{X_t},\quad
 b=|\beta|,\quad g=|\gamma|,\quad \kappa=\max(1,|K|).
\]
The complete flux obeys
\[
 \|{\cal A}\|_{X_t}
 \le\kappa\{(3/4)bB_t\rho+(1/4)b\rho^2+g\rho\}H_t.
 \tag{S.4}
\]
For example the first primitive term is bounded by
\(\kappa B_t\rho H_t/4\), the second by
\(\kappa B_t\rho H_t/2\), and the cubic by
\(\kappa\rho^2H_t/4\).
The two mean-rank factors in the last term are retained.

The mean reaction is bounded by
\[
 \|{\cal B}\|_{X_s}
       \le b\kappa(3B_t\rho+\rho^2)H_t .
 \tag{S.5}
\]
For its first term use
\(|\langle S_h\rangle|\le\kappa\rho H_t\);
for its second use
\(|\langle B\rangle|\le\kappa B_t\rho\).
Thus neither estimate loses the nonzero even mean.

Together,
\[
 \boxed{\quad
 \|R(Q,h)\|_{H^s}
 \le C_s\rho\|h\|_{X_{s+1}},\qquad
 C_s=\kappa\{(15/4)bB_{s+1}+(5/4)b\rho+g\}.
 \quad}                                                        \tag{S.6}
\]
For radially varying states the same bound holds in \(L^2_rH^s_\phi\)
with the uniform coefficient and \(A^{s+1}\) bounds and with
\(\|h\|_{L^2_rX_{s+1}}\) on the right.

The full differentiated remainder in any direction \(k\) satisfies
\[
 \boxed{\quad
 \|(DF(Q+h)-DF(Q))k\|_{H^s}
 \le D_s\rho\|k\|_{X_{s+1}},\qquad
 D_s=\kappa\{(15/2)bB_{s+1}+(15/4)b\rho+2g\}.
 \quad}                                                        \tag{S.7}
\]
To see every coefficient, differentiating the flux in (S.3) gives
quadratic coefficients \(3bB_t/2\), cubic coefficient \(3b\rho/4\),
and both mean-rank contributions \(2g\).
Differentiating the mean reaction gives coefficients \(6bB_t\)
and \(3b\rho\). Their sums are precisely (S.7).
The proof uses \(k\) only in \(X_{s+1}\), not a hypothetical
finite Fourier support or a stronger Wiener norm.
Smooth directions first justify the polynomial identity, and
the displayed bounded operators extend it by density.

The same estimate bounds the Lipschitz difference of remainders
along a segment lying in the stated \(A^{s+1}\) ball. It still
has the explicitly displayed derivative in its direction norm.

## 3. Consume the actual A-cubed root neighbourhood

The same real moving neighbourhood used in
[the complete nearby root inverse](R133-supplement-current-root-nearby-complete-infinite-tail-inverse.md)
has
\[
 \sup_r\|h(r)\|_{A^3}\le\rho\le10^{-6}.
 \tag{S.8}
\]
This pays both \(A^{4/3}\) and \(A^{7/3}\), for all the unknown
infinite tail. Only the *centre* has \(|k|\le128\), and its complete
bounds give
\[
 b,g<9/5,\qquad \kappa=1,\qquad
 \|Q_c\|_{A^0}<74/5 .
\]
The actual integer gate \(129^4<652^3\) implies
\[
 B_{4/3}<\frac{48248}{5}=9649.6,\qquad
 B_{7/3}<\frac{6223992}{5}=1244798.4 .
 \tag{S.9}
\]
The second inequality multiplies the first support factor by 129.
Neither support estimate is applied to \(h\).

Substituting into (S.6)–(S.7), the executed rational bounds are
\[
\begin{array}{c|c|c}
 \text{ordinary source norm}&
       \|R\|\text{ bound}&
       \|(DF(Q_c+h)-DF(Q_c))k\|\text{ bound}\\ \hline
 H^{1/3}&66000\,\rho\|h\|_{X_{4/3}}&
                    132000\,\rho\|k\|_{X_{4/3}}\\
 H^{4/3}&8500000\,\rho\|h\|_{X_{7/3}}&
                    17000000\,\rho\|k\|_{X_{7/3}}
\end{array}                                                     \tag{S.10}
\]
These are complete source estimates on the same neighbourhood,
not bounds on sampled Fourier values.

The even mean itself has the exact expression
\[
 \langle R_2\rangle
 =-\beta\{\langle S_h\rangle m
                +2\langle B\rangle\langle h_2\rangle
                +\langle S_h\rangle\langle h_2\rangle\}.
\]
Using \(|m_c|<28/25\), the complete root bounds prove
\[
 |\langle R_2\rangle|<56\rho^2,\qquad
 |D_h\langle R_2\rangle[k]|<112\rho\|k\|_{L^2,\mathrm{sum}}.
 \tag{S.11}
\]
The first mean is zero only in the actual odd/even reflection class.
Equation (S.11) does not set the independent even mean source to zero.

## 4. One actual root response and the exact remaining loss

The complete root inverse takes an ordinary source
\(L^2_rH^{1/3}_\phi\) into raw \(L^2_rL^2_\phi\) with norm below
\(1/8000\), and into both raw endpoint states with norm below \(1/25\).
For the first line of (S.10) and (S.8),
\[
 \|R\|_{L^2_rH^{1/3}_\phi}
 <66000\sqrt{h_r}\rho^2=198\rho^2 .
\]
Consequently the solution of the *linear* complete root problem
with this source and zero stated linear incoming ports has
\[
 \boxed{\quad
 \|z\|_{L^2_rL^2_\phi}<\rho^2/40,\qquad
 \|\operatorname{Tr}_{r_*,r_*+h_r}z\|<8\rho^2 .
 \quad}                                                        \tag{S.12}
\]
The precise unrounded factors are \(99/4000\) and \(198/25\).
The full mean and every head/high feedback path occur in this
inverse. Its ports are those of the specified background reference;
they have not been identified with some other nonlinear boundary
chart.

For the first angular bootstrap, the second line of (S.10)
is exactly an ordinary \(H^{4/3}\) source.
The already paid triangular estimate therefore applies with the
complete head forcing \(5560000\|z_L\|\) and lower-order
coefficient \(4538113\). No finite output cutoff is needed.

At general output order \(a\), this structure uses
\[
 h\in X_{a+4/3}\ \longmapsto\
 R\in H^{a+1/3}\ \longmapsto\ z\in H^a .
 \tag{S.13}
\]
The total loss is \(4/3\) angular derivatives. Here the actually
proved output levels are \(a=0,1\), together with their
interpolated intermediate levels.
Neither (S.12) nor a small value of \(132000\rho\) removes that loss.
In particular the output is not controlled in the original
\(A^3\) neighbourhood by this assertion. A compatible smoothing
iteration and a complete global inverse remain necessary.

## 5. Full metric-parameter and normalized-reference remainder

The exact intrinsic identities N.15–N.18 in the flux theorem stay
unchanged:
\[
 K_{\nu+d\nu}=e^{-d\nu w}(K+d\nu\,Tw'),\quad
 \gamma_{\nu+d\nu}=\gamma e^{d\nu w/2},\quad
 (\gamma K)_{\nu+d\nu}
     =e^{-d\nu w/2}(\gamma K+d\nu\,\gamma Tw'),
\]
where \(T=\beta/(2E_\nu)\).
In coefficient coordinates \(K,\gamma,p=\gamma K\), the full
right-side difference is
\[
 \Delta F(Q)=
 \partial_\phi\{-\beta\Delta K I(v^2)Q
                   +m(\Delta p\,v,-\Delta\gamma\,u)\}
                    -\beta\Delta K\langle v^2\rangle Q .
 \tag{S.14}
\]
Its complete mean is still explicit.

Put \(a_1=|\Delta K|\), \(d_1=|\Delta p|+|\Delta\gamma|\).
With the same \(t=s+1\), \(B_t\) and \(\rho\), (S.2) gives
\[
\begin{split}
 \|\Delta F(Q+h)-\Delta F(Q)\|_{H^s}
 \le\{&(5/4)b a_1(3B_t^2+3B_t\rho+\rho^2)\\
      &+d_1(2B_t+\rho)\}\|h\|_{X_t}.
\end{split}                                                     \tag{S.15}
\]
Every mixed state/parameter term is present.
If the true coefficient Taylor remainders are bounded by
\((d\nu)^2K_2,(d\nu)^2G_2,(d\nu)^2P_2\), as in N.18, then
\[
 \|R_{\rm parameter}(Q,d\nu)\|_{H^s}
 \le |d\nu|^2\{(5/4)bK_2B_t^3+(P_2+G_2)B_t^2\}.
 \tag{S.16}
\]
The sum of (S.6), (S.15) and (S.16) is the complete joint
physical-state remainder.
On the current root germ the actual compact \(w,w'\) vanish,
so these parameter terms are exactly zero there.
On its real body support the complete true \(K,T,B_t\) envelopes
and the radial source norms still have to be supplied.

For normalized unknowns at fixed amplitude,
\(h=\alpha k+(0,s(\nu+d\nu)-s(\nu))\) and
\(h_{\rm lin}=\alpha k+(0,s_\nu d\nu)\).
The residual \(Q_r-F\) has the exact normalized remainder
\[
 R_{\rm norm}
 =\alpha^{-1}\{{\cal D}(h-h_{\rm lin})
                         -R_{\rm joint}(h,d\nu)\},
 \qquad {\cal D}=\partial_r-DF(Q,\nu).
 \tag{S.17}
\]
Thus the true \(s_{\nu\nu}\) and its radial jet are still required;
switching to Sobolev norms does not remove that term.
All true raw moving jumps remain data, and their raw state
Taylor remainder is zero because the raw jump equation is
linear. Actual nonlinear physical-angle, mean-chart, exterior
Robin and far-label rows require their own full remainders.

## 6. Source, actual execution and limits

Source:
[scripts/fourfold_codazzi_moving_Sobolev_flux_budget.mjs](../scripts/fourfold_codazzi_moving_Sobolev_flux_budget.mjs).

Complete actual report:
[notes/2026-11-14-R133-moving-Sobolev-flux-rational.json](../notes/2026-11-14-R133-moving-Sobolev-flux-rational.json).

The complete arithmetic function ran in the available V8 runtime.
All 9 exact rational gates passed. The Node wrapper reproduces the
same arithmetic and refuses to overwrite an existing report.
No lost native arrays, approximate Bessel library or numerical
angle samples are inputs.

The new contract is the exact ordinary Sobolev source estimate
(S.10), its nonzero mean row (S.11), and its one-step consumption
by the complete local inverse (S.12), with the real \(4/3\)
loss (S.13) stated explicitly. The uncomputed whole-body inverse,
true scalar parameter Schur, compatible smoothing iteration and
same-family geometric conditions remain necessary for the
requested visible-flex completion.
