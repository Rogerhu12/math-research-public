# R149 ASQ21. The normalized physical phase fibre is holomorphic

Use the complexification of the complete perturbation space in [ASQ8.1](R149-supplement-selected-physical-phase-fibre-summable-analytic-iteration.md), retaining the original linear symmetries and pieces. Write \(Z=\|z\|\) and \(R_z=2^{-33000}\). Let \(P=P(Q_*+z+kh^a,\nu_*+k)\) be the actual folded physical return. The normalized degree-one lift \(g\), the metric parameter \(k\), the inverse lift \(H\), and the physical phase \(a=2H(0)\) are holomorphic functions of \(z\) for \(Z<R_z\) on fixed positive strips as specified below. On the real ball their normalized phase solution is the ASQ8 solution. Its choice of gauge is
\[
 \langle g-g_0\rangle=0,\qquad P\circ g=g\circ R.             \tag{ASQ21.1}
\]
The first mean is the average of the periodic difference of lifts. The phase equation retains its physical constant coefficient and the actual metric variation \(h^a,1\).

## A convergent complex correction with real fixed rotation

Use \(M=2^{6000}\), \(r_0=2^{-2104}\), \(d_0=r_0/16\), \(A=2^{24}M\), \(C=2^{52}M^3\), and \(a_0=(2^{12}M)^{-1}\) from ASQ8. Its holomorphic flow, first and second complex derivative bounds for \(P-\mathrm{Id}\), and base conjugacy bounds apply throughout the complex tube
\[
 Z+|k|+\|g-g_0\|_r+\|g'-g'_0\|_r\le a_0.
\]
Indeed \(|\operatorname{Im}g|\le2r+a_0\) with \(r\le r_0\) and \(a_0\ll 2^{-2100}\), so the images stay in the same ASQ8 strip with a strict margin. In this tube \(J=g'\circ R\) satisfies \(\|J^{-1}\|,\|g'\|\le2\). The original \(B=(P_k\circ g)/J\) satisfies \(\|B\|\le2M\), \(|\langle B\rangle|>1/64\). The latter follows from the real base mean \(>1/32\) and the same complex absolute variation bound \(6Ma_0\) proved by expanding the numerator and both inverse denominator factors.

Set \(E=P\circ g-g\circ R\), \(\epsilon=\|E\|_r\), \(F=-E/J\) and \(D_R u=u-u\circ R\). With \(\langle u\rangle=0\) take
\[
 t={\langle F\rangle\over\langle B\rangle},\qquad
 u=D_R^{-1}(F-Bt),\qquad h=g'u,\qquad
 (k_{\rm new},g_{\rm new})=(k+t,g+h).                       \tag{ASQ21.2}
\]
Each operation is holomorphic on its stated smaller strip. Only the fixed irrational rotation acts in \(D_R^{-1}\). The operand has zero mean as an identity of complex numbers. For \(4d<r\), ASQ8 gives \(\|D_R^{-1}P_0\|_{r\to r-d}\le16d^{-2}\). Thus
\[
 |t|\le128\epsilon,\quad \|u\|_{r-d}\le2^{13}M d^{-2}\epsilon,\quad
 \|h\|_{r-d}\le2^{14}M d^{-2}\epsilon,\quad
 |t|+\|h\|_{r-4d}+\|h'\|_{r-4d}\le A d^{-3}\epsilon .
\]
By direct differentiation,
\[
 D_{k,g} E(t,h)=JBt+J D_Ru+E'u=-E+E'u .
\]
This identity retains the full off-solution multiplier, including its constant-mode contribution in \(E'u\). ASQ6 still gives the exact real off-conjugacy inverse. Here the full unpaid part of the complex correction is explicitly quadratic. On the new strip its norm is at most \(2^{13}M d^{-3}\epsilon^2\). The complete Taylor remainder on the straight correction segment is at most \(M(|t|+\|h\|)^2\) as in ASQ8. Since \(d<1\) and \(M>1\), the sum is less than \(C d^{-4}\epsilon^2\). No bound on a complex small divisor depending on \(z\) or \(k\) is required.

Set \(d_j=2^{-j}d_0,\ r_{j+1}=r_j-4d_j,\ r_\infty=r_0/2\), and \(e_j=16C d_j^{-4}\epsilon_j\). The original complex flow estimate gives \(\epsilon_0\le M Z\), including the mean, so \(e_0<1/4\). As in ASQ8 the sum of the proposed changes through any index with \(e_j\le(1/4)^{2^j}\) is bounded by
\[
 b_0={A d_0\over8C}<2^{-14000}.
\]
This keeps every straight segment in its complex tube before the Taylor bound is used and gives \(e_{j+1}\le e_j^2\). Also \(\epsilon_{j+1}\le(e_j/16)\epsilon_j\le\epsilon_j/64\), whence \(\sum |t_j|\le256 M Z\). The limits \(g_{\rm raw}-g_0\), its first derivative and \(k\) converge uniformly over the complete open data ball in the fixed sup norms on \(S_{r_\infty}\). Uniform convergence of holomorphic Banach maps on this ball implies holomorphy there, for example by scalar Cauchy integrals on every complex line and local boundedness. The limit satisfies the full return equation.

Put \(\tau=-\langle g_{\rm raw}-g_0\rangle\). Translating the source chart by \(g(x)=g_{\rm raw}(x+\tau)\) preserves the return identity, and \(\langle g_{\rm raw}(\cdot+\tau)-g_0\rangle=\langle g_{\rm raw}-g_0\rangle+\tau\) by periodicity and analytic continuation. This gives (ASQ21.1). Since \(|\tau|\le b_0\ll r_\infty/4\) and \(\|g'_0\|\le2\), the normalized lift is holomorphic into \(S_{r_\infty/2}\) with \(\|g-g_0\|\le3b_0\). On the real circle its derivative stays positive by the base bounds and \(\|g_{\rm raw}'-g_0'\|\le b_0\).

## Identification with the real solution and its genuine phase

For real data both ASQ8 and the construction above have real parameters satisfying \(|k|\le1024 M Z\). For ASQ8 this follows from \(|\Delta k_j|\le512\epsilon_j\) and the same ratio \(\epsilon_{j+1}/\epsilon_j\le1/64\). We show two such solutions with the stated small lift bounds have the same \(k\). Fix one solution \((k_1,g_1)\) before final translation and write \(t=k_2-k_1\). Then \(|t|\le2048M R_z=2^{-26989}\). On \(S_{r_\infty}\) solve the fixed cohomological equation
\[
 u=D_R^{-1}(\langle B\rangle-B),\qquad h=g_1'u .
\]
With \(d=d_0=r_\infty/8\) this gives \(\|h\|_{r_\infty-d}\le128M d^{-2}=2^{10223}\). On the real line \(g_1+th\) is a degree-one orientation-preserving lift, since \(\|h'\|\le2^{10223}/d\) and \(g_1'>1/2\). The maps throughout the straight segment stay inside the complex flow domain by these same estimates. Its return discrepancy is
\[
 P_{k_1+t}\circ(g_1+t h)-(g_1+t h)\circ R
        =tJ\langle B\rangle+{\cal R},\qquad
 \|{\cal R}\|\le M(1+2^{10223})^2 t^2 .
\]
Here the subscript on \(P\) designates the parameter value, the unvaried \(z\) is fixed, and \(J\langle B\rangle>1/128\) on the real circle. Since \(M(1+2^{10223})^2|t|<1/256\), a nonzero \(t\) would make this discrepancy strictly of its sign everywhere. Conjugation by \(g_1+t h\) would then put the lift \(P_{k_1+t}\) uniformly above \(R+\delta\) or uniformly below \(R-\delta\) for some \(\delta>0\). Iteration of these pointwise translation bounds contradicts the same lifted rotation number of the second exact solution. Thus the parameters coincide. Their two lifts differ by a source translation, since the continuous periodic displacement of \(g_1^{-1}\circ g_2\) commutes with the fixed irrational rotation and is constant. The mean condition removes that translation. It agrees with centring the inverse lift in the original physical angle. Indeed writing \(H(y)=y+\ell(y)\) and substituting \(x=H(y)\) gives \(\langle g-\mathrm{Id}\rangle=-\langle\ell(1+\ell')\rangle=-\langle H-\mathrm{Id}\rangle\) on the real circle. This keeps the same scalar normalization as the seed for either lift.

Write \(H_0=g_0^{-1}\). On \(S_{4s}\), \(s=r_\infty/32\), its imaginary part satisfies \(|\operatorname{Im}H_0|\le 2|\operatorname{Im}x|\) by the original real lift and the derivative bound of W.3–5. Thus \(g\circ H_0=\mathrm{Id}+v\) there with \(\|v\|\le3b_0\). On \(S_{2s}\), \(\|v'\|\le3b_0/s<1/4\). For each \(y\in S_s\) iteration of \(w=y-v(w)\) on \(|w-y|\le3b_0\) is a uniform complex contraction. Its fixed point \(w\) yields \(H(y)=H_0(w)\), \(\|H-H_0\|_{S_s}\le6b_0\), and \(|a-a_*|\le12b_0\). This also establishes holomorphic dependence of the physical phase and inverse lift with the same parameter \(k\).

## Mixed jets on a common physical family

For \(Z\le R_z/2\), unit directions \(z_1,\ldots,z_m\) in the original data norm, and \(m\ge1\), every one of the \(m\) scalar Cauchy circles can have radius arbitrarily close to \(R_z/(2m)\). In particular, writing \(L_m=(2m/R_z)^m\),
\[
 |D^m k|\le256M R_z L_m,\quad
 \|D^m g\|_{S_{r_\infty/2}}\le3b_0L_m,\quad
 \|D^m H\|_{S_s}\le6b_0L_m,\quad |D^m a|\le12b_0 L_m.       \tag{ASQ21.3}
\]
An additional \(j\) angular derivatives on any smaller strip of margin \(s'\) cost \(j!(s')^{-j}\). Thus these are actual mixed Frechet derivatives of selected nonlinear solutions, including the complete first and second phase and parameter variations on one common state. The estimates retain every radial piece and allow arbitrary angular support. In real fixed coordinates the moving reflected model of [ASQ19](R149-supplement-fixed-rotation-geometric-coefficient-and-moving-real-model-jets.md) uses exactly this \(a\) and its derivatives with the translation sign established there. Its independent scalar \(\xi\) continues to require ASQ19's stronger radial trace norm. The regular physical PDE, its high response and its independent world and border equations still have their separate inverse and smallness requirements.
