# R149 ASQ25. Direct signed residual for the true inverse density and its recovered coordinates

Use the exact selected objects of [ASQ17](R149-supplement-fast-true-Theta-series-and-complete-original-high-row-tail.md),
\[
 \Theta=E_{96}^*D_+^{-1}C^{-1}A\bar G,\qquad T=\Theta E_{96}^a .
\]
For a supplied real finite target column \(b\) of extent 512 (or any finite linear combination of such columns), form \(z=\bar G b\) from the full original model multipliers and true source phase. Both signs and every mean in the underlying physical problem use the original definition. This theorem works on the nonmean target space after actual physical half-sum extraction. Let \(v=A z\) and \(\widehat v=(Id-\mathcal T_{\widehat\alpha}I)z\), with \(\widehat\alpha\) the entire original degree-2048 real coefficient and \(\mathcal T\) the [two same-sign multiplications](R149-supplement-original-same-sign-source-Toeplitz-and-Theta-row-action.md). Thus \(\widehat v\) has support at most 2560. Let \(u\) be an arbitrary exact real trigonometric trial of extent at most 1024, including conjugate signs and with zero mean. No claim that a projected inverse or an approximate Neumann term equals the true inverse is needed. Define
\[
 \begin{aligned}
 e_\alpha(z)&=\min\left\{.348\|Iz\|_2,\quad
   \sqrt2(.06524)\sum_{n>0}|z_n|/(4n)\right\},\\
 e_p(u)&=E_p(275\|u\|_2+1.07\|u'\|_2),\qquad E_p=2.211\,10^{-7}.
 \end{aligned}                                                    \tag{ASQ25.1}
\]
Both candidates in \(e_\alpha\) are *whole* bounds for the same signed source error, using the original ASQ18.3 coefficient errors, orthogonality of the two signs and the true physical primitive. The factor \(\sqrt2\) combines the two conjugate one-sided infinity norms in the second bound.

Write \(p=\psi^{-1}\); the physical density is \(U_\psi u=\psi'(u\circ\psi)\), and \(C\) consists of its two diagonal sign blocks. Let \(\hat p\) be the original degree-64 terminal-side lift composed with its full 48-mode postmap, and \(\hat\psi=\hat p^{-1}\). (The terminal carrier has 129 complex entries including the mean, namely modes \(-64,\ldots,64\).) SDI.2–4 and [ASQ12](R149-supplement-all-positive-i-safe-modes-in-the-physical-waist-square.md) give
\[
 m=.9749<p',\hat p'<M=1.0251,\quad |p''|<1/6,
 \quad |p-\hat p|<E_p,\quad |p'-\hat p'|<256E_p .
\]
Thus \(\|\psi-\hat\psi\|_\infty\le E_p/m\) and \(\|\psi'-\hat\psi'\|_\infty\le m^{-2}(256+1/(6m))E_p\), by evaluating the true derivative first at the two inverse points. Every \((1-t)\psi+t\hat\psi\) has derivative at least \(1/M\). Change of variables in the difference of the two *density* pushforwards now gives
\[
 \|(C-C_{\hat p})u\|_2\le E_p\frac{\sqrt M}{m^2}
     [(256+1/(6m))\|u\|_2+\|u'\|_2] < e_p(u).              \tag{ASQ25.2}
\]
Here \(C_{\hat p}\) denotes same-sign compression of \(U_{\hat\psi}\). Projection and direct sum over signs preserve the bound.

## A whole signed inverse residual from the original 8192-point lift

Put \(K=4096, N=8192, \sigma=1/256\). DCP's original complete first record gives \(\eta=\|\hat p'-1\|_{S_\sigma}<1\), including every coefficient of the compound and its actual mean. Let \(W=\sum_{1\le n\le1024}|u_n|e^{4n\sigma}\). For each \(1\le k\le K\), transform a positive-sign input by the original exact action
\[
 (C_{\hat p}u)_k=
 \int u_+(y)e^{-4ik\hat p(y)}\,d\bar y .
 \tag{ASQ25.3}
\]
Normalized angular measure is used. The Jacobian cancels under the indicated change of variables; inserting one in (ASQ25.3) would compute a different operator. The opposite-sign output for real data is the conjugate, and all same-sign source inputs participate. Evaluate its normalized \(N\)-point trapezoid using the *complete original* 8192-grid of \(\hat p\). A uniform bound for each coefficient's two alias rays is
\[
 a_k=\frac{2W\exp\{-4N\sigma+4k(1+\eta)\sigma\}}{1-e^{-4N\sigma}}.
\]
Indeed \(|\operatorname{Im}\hat p(y\pm i\sigma)|\le(1+\eta)\sigma\); real translation causes no loss. On the lower boundary \(\operatorname{Im}\hat p(y-i\sigma)\le-(1-\eta)\sigma\). With \(q=e^{-4(1-\eta)\sigma}\), the infinite ordinary norm beyond \(K\) of \(C_{\hat p}u\) is bounded by
\[
 b_K=\sqrt2\,W q^{K+1}/\sqrt{1-q^2}.
\]
The original finite signed \(\widehat v\) vanishes there. Let \(d_k\) be the complete interval sum in (ASQ25.3) on all nodes minus the full same-sign coefficient \(\hat v_k\), extended by zero for \(k>2560\). Then
\[
 e(u,z)= 1.11\left[
 \sqrt{ 2\sum_{1\le k\le K}(|d_k|_{\rm up}+a_k)^2+b_K^2}
       +e_p(u)+e_\alpha(z)\right]                             \tag{ASQ25.4}
\]
bounds \(\|u-C^{-1}A\bar G b\|_2\), since ASQ12 gives \(\|C^{-1}\|_2<1.11\). Only the accumulated *signed* low residual enters before its norm. An implementation may choose \(u\) by finite least squares or by the ASQ17 iteration on the saved phase. The full certificate is (ASQ25.1–4), including the defect of that choice. The recovered 96-vector has exact real centres \(\operatorname{Re}u_n-\operatorname{Im}u_n\) with joint radius \(e(u,z)\), because the original normalized selector is an orthogonal contraction. The negative sign on the imaginary part follows from \(D_+^{-1}\) and the two conjugate coefficients of the real cosine basis.

## A signed residual for the finite coordinate solve

Let true \(x\) have a complete finite trial \(\hat x\), with full ordinary forward error \(d_x\). Write \(b_L=E_{96}^{a*}\hat x\) and \(b_H=P_{\ge97}\hat x\). For any exact real 96-vector \(s\), apply the preceding **single** signed action to the finite input \(b=b_H-E_{96}^a s\). In particular its row multiplies the same true source and normalizer before summing. The identity
\[
 T^{-1}\Theta\hat x-(b_L+s)=T^{-1}\Theta(b_H-E_{96}^a s)
\]
holds on the original model space. If \(t\) denotes the above signed 96 centres for that input, then
\[
 \|T^{-1}\Theta x-(b_L+s)\|_2
 \le 2.694(\|t\|_2+e(u,\bar G b))
         +\sqrt{1+(2.694\cdot3.04)^2}\,d_x.                  \tag{ASQ25.5}
\]
Here the ordinary full-error coefficient follows by the exact low-coordinate identity and [ASQ22](R149-supplement-small-true-Theta-reception-of-the-negative-parameter-defect.md) on the complementary high input, using orthogonal input squares. A separate prior physical raw error \(R\) incurred *before* the finite forward calculation costs only \(.457R\) in (ASQ25.5), or \(.456R\) in the unrecovered \(\Theta x\) norm, by ASQ22. Its high and low pieces need not be charged by the coarser \(d_x\) coefficient. The original two signed characteristic means are carried separately, with errors \(.681R\) for each. For a pair of raw columns \(R\) may be the full common \(D(t)\) of [ASQ23](R149-supplement-two-signed-negative-waist-responses-and-common-Gram-remainder.md).

A choice such as the UACT whole inverse applied to a proposed signed high row only selects \(s\). The true error in that choice is certified by the combined residual in (ASQ25.5); no bound proportional to the norm of a large independent particular is added in place of this residual. These formulas retain all 96 physical coordinates and both signs without altering root, physical height, Robin or other independent rows. Numerical radii and signed columns require the respective first genuine public solution and actions on its whole original input.
