# R149 ASQ28. Ordered natural-frequency reception for a signed physical source

Fix the selected real model of [ASQ16](R149-supplement-actual-all-frequency-primitive-and-single-physical-gate.md). The input index below is an original target index. The natural terminal Ai index of the source is its **output** index after the right normalization. Let \(V\) be one actual terminal Ai physical map from the original two-sign natural \(H^{-4/3}\) input to the full physical waist. In particular the statement applies separately to the signed local source and to each genuine source component with this contract. Suppose \(b_j\) bounds \(\|VP_{\{j\}}\|\) for each natural two-sign pair. The following formulas receive those estimates without assigning orthogonality to any propagated waist outputs.

Use \(P=P_{\ge97}\), \(I=\partial_\phi^{-1}P_{\ne0}\), \(P^{(0)}=P_{\ne0}\), \(p=\psi^{-1}\), and \(S=U_\psi\). Let \(D_\pm\) denote the two sign projectors; write \(R_s=\sum_\pm D_\pm R D_\pm\). The primitive identities on the two true Hilbert spaces are
\[
 S_0=ISI^{-1}=P^{(0)}(f\mapsto f\circ\psi),\qquad
 R=S_0^{-1}=P^{(0)}(f\mapsto f\circ p),\qquad
 C_0=ICI^{-1},\quad Z=C_0^{-1}.
\]
Indeed the terms subtracted when taking a primitive are precisely the angular constants. An intermediate subtracted constant stays constant under composition and disappears under the last orthogonal projection. Set \(f=I\bar GP u\). The exact compensated density at every natural mode is
\[
 I C^{-1} A\bar G P u=Z B f,\qquad B=Id-I\mathcal T_\alpha .              \tag{ASQ28.1}
\]
On the original real unit line \(\|P_{\{k\}}f\|=g_k|u_k|\), \(g_k=|\gamma_k|/(4k)\). All of ASQ16's signs and true source phases are retained. Passing to the modulus only after (ASQ28.1) gives a rigorous upper for arbitrary signed physical inputs. In the following take \(g_* =32/25\), \(g_k<.573\) for \(97\le k\le2^{20}\). By [GSW](R149-supplement-first-genuine-source-through-the-physical-waist-and-common-input.md) the remaining true normalization is ordered as \(\Lambda_+^{-1}T_F^{-1}P C^{-1}A\bar G P\), with \(\|\Lambda_+^{-1}\|<10.611\); this root scalar commutes with the individual natural frequency projections. On auxiliary full-circle summands extend \(V\) by its orthogonal projection to the original natural reflected subspace. This projection acts separately on each two-sign pair and contracts in the declared Sobolev norm. On the true normalized input it is identity. The full normalization already cancelled the adjacent \(\mathcal S^{-1}\mathcal S\).

## Both wrong-sign factors and the full original input tail

Let \(D_0=S_0-C_0\). Resolvent multiplication gives \(Z=R+RD_0 Z\). Compress to a single sign on both sides. Since \(D_0\) interchanges the signs and \(Z\) preserves each one,
\[
 \|P(Z-R_s)\|\le\|P(R-R_s)\|\,\|D_0\|\,\|Z\|
 < .00059(.08)(1.11)<.000053 .                            \tag{ASQ28.2}
\]
The last two factors follow from [ASQ12.2](R149-supplement-all-positive-i-safe-modes-in-the-physical-waist-square.md) in the original homogeneous window. To justify the first, the opposite entry of \(R\) on output \(j\ge97\) and input \(\ell\ge1\) is the normalized integral of \(e^{-4i(jy+\ell p(y))}\), up to complex conjugation. ASQ12.3 and its preceding twice-integrated trial estimate therefore bound its modulus by
\[
 .059\,\ell/(j+\ell)^3+4\ell E_p e^{-(j+.899\ell)/64},
 \qquad E_p=2.211\,10^{-7}.
\]
The squared kernel sum for the first term before the factor \(.059^2\) is \(\le\sum_{j\ge97}(3j^3)^{-1}\le1/(6\cdot96^2)\). For the exponential term the two squared sums are \(\sum_{j\ge97}e^{-j/32}<32e^{-3}<1.6\) and \(\sum_{\ell\ge1}\ell^2e^{-.899\ell/32}<91200\) from ASQ12. Their Hilbert--Schmidt bounds add to less than \(.00059\). The two opposite sign maps form an orthogonal direct sum on the full angular circle.

Write \(J=\{97,\dots,1023\}\), \(L=2240\), and \(P_J\) for the natural projection. For \(\ell>L\), \(j\in J\), the same-sign coefficient of \(R_s\) is \(\langle e^{4i(\ell p(y)-jy)}\rangle\). On the original strip of width \(1/256\) the real lift \(p\) has \(|p'-1|<.1\), so shifting upward gives
\[
 \|P_JR_sP_{>L}\|\le
 \frac{\exp[-(.9(2241)-1023)/64]}
 {\sqrt{(1-e^{-1/32})(1-e^{-.9/32})}}<.0000064 .           \tag{ASQ28.3}
\]
This is an estimate of the entire infinite kernel. It retains all unlisted model divisors via \(g_*\) on their own input.

## A finite signed matrix and its entire operator error

Let \(\widehat p,\widehat\alpha\) be the full original compound lift and degree-2048 real coefficient of [ASQ18](R149-supplement-actual-signed-Theta-trial-and-finite-inverse-by-primitive-residual.md). Put \(\widehat B=Id-I\mathcal T_{\widehat\alpha}\), \(\widehat R_s=\operatorname{diag}_\pm P^{(0)}(f\mapsto f\circ\widehat p)\). Define
\[
 M=P_J\widehat R_sP_{1\le |j|\le L}\widehat B .
\]
Only the positive input indices \(97\le k\le L+2048=4288\) occur in the positive sign block. The negative block is its exact conjugate. Explicitly, with \(K_{j\ell}=\langle e^{4i(\ell\widehat p(y)-jy)}\rangle\),
\[
 M_{jk}=\mathbf1_{k\le L}K_{jk}
       -\sum_{\ell=1}^{L}K_{j\ell}\frac{\widehat\alpha_{\ell-k}}{4i\ell},
       \qquad \widehat\alpha_0=0.                            \tag{ASQ28.4}
\]
All 2048 positive and negative coefficient shifts participate. The full 8192 stored \(\widehat p\) nodes of the original DCP actual give a certified trapezoid for each \(K_{j\ell}\). The complete two-ray alias radius is
\[
 \frac{2\exp\{[-8192+j+(1+\eta)\ell]/64\}}{1-e^{-8192/64}},\qquad
 \eta=\|\widehat p'-1\|_{S_{1/256}}<.026 .
\]
It follows by bounding the absolute analytic integrand on both boundary lines before summing all aliases. A directed computation may insert this fee per entry before taking the sum in (ASQ28.4). The terminal coefficient matrix then encloses the complete analytic \(M\).

Use \(G_L=\sup_{97\le k\le L}4k g_k\). It can be taken directly from the whole original signed OT2240 model or bounded above by \(4L(.573)\). For the exact operators,
\[
 \|P_J Z B I\bar GP-M I\bar GP\|\le d_J,                    \tag{ASQ28.5}
\]
where
\[
 d_J =
 .000053(1+1.43/4)g_*
 +\frac{1.013(.348)}{388}\,g_*
 +.0000064(1+.491/4)g_*
 +1.013 E_p(G_L+.491 g_*).
\]
For the first term apply (ASQ28.2) to \(Bf\). Replacing \(B\) by \(\widehat B\) costs the second term: the derivative of \((Ih)\circ p\) is \(p'(h\circ p)\), whose \(L^2\) cost is at most \(\sqrt{\sup p'}<1.013\). At outputs \(j\ge97\) integrate this derivative once, and apply \(\|\alpha-\widehat\alpha\|_\infty<.348\). For the third term first project the *intermediate* \(\widehat Bf\) to \(>2240\), then apply (ASQ28.3); \(\|\widehat\alpha\|_{A^0}<.491\). Finally the real path \(p_t=(1-t)p+t\widehat p\) has \(p_t'>.9749\). Change variables in the interpolation derivative \((\widehat p-p) h'\circ p_t\) to get \(1.013 E_p\|h'\|_2\). Here \(h=P_{\le L}\widehat Bf\): its first derivative is \(\partial_\phi P_{\le L}f-P_{\le L}\mathcal T_{\widehat\alpha}f\), at a cost \(G_L+.491g_*\) per unit original input. Thus (ASQ28.5) retains the true lift, true coefficient and all derivative orders in their original places. Using the coarse \(G_L\) above gives \(d_J<.00243\).

For each natural \(j\), set \(w_j=4j(1+16j^2)^{-2/3}\); \(w_j\le(4j)^{-1/3}\). Let \(B_J\) be any certified whole natural operator bound for \(VP_J\). The value \((\sum_{j\in J}b_j^2)^{1/2}\) is also a legal \(B_J\) by the triangle inequality and orthogonality of **inputs**. On \(J\), \(T_F^{-1}\) is exactly identity on both sides by [TFA.2](R133-supplement-actual-complete-common-root-normalizer-and-two-window-inverse.md). A genuine natural-low contribution to the full physical high action consequently has norm at most
\[
 10.611\left\{\left[
 \sum_{k=97}^{4288}g_k^2
  \left(\sum_{j=97}^{1023} b_j w_j |M_{jk}|_{\rm up}\right)^2
 \right]^{1/2}+ B_J\,388^{-1/3}\, d_J\right\}.              \tag{ASQ28.6}
\]
Indeed the two sign entries of the matrix on each angular index are conjugates, so the norm of their action on the two-dimensional sign pair is \(|M_{jk}|\). Apply the full single-label terminal operator, sum actual output norms by the triangle inequality, then apply Cauchy--Schwarz in the original input \(k\). Weighting by a natural \(g_j\) after propagation would change (ASQ28.6).

## Genuine higher natural-input bands

The full TFA actual gives \(\|F_*\|_{A^0}<185\), \(\deg F_*\le192\), \(A_F=P_{1024}M_{F_*}IP_{1024}\), \(T_F=Id+A_F\). In the \(\dot H^{-1}\) window \(I A_F I^{-1}=P_{1024}I M_{F_*}P_{1024}\) has norm at most \(185/4096\). The original \(L^2,H^{-4/3}\) Neumann series and this one agree on their common smooth inputs, giving the same \(T_F^{-1}\), with \(\|T_F^{-1}\|_{\dot H^{-1}}<1.048\) and \(\|T_F^{-1}\|_{H^{-4/3}}<1.061\). For any natural band \(D\subset[N,\infty)\), \(N\ge1024\), write \(B_D=\|V P_D\|\) or use a verified upper. Set
\[
 t_M=1.048(1.11)(.573)(1+1.43/388)(4N)^{-1/3},\quad
 t_H=\min\left\{1.048(1.11)(32/25)(1+1.43/388)(4N)^{-1/3},
       \ 1.061(5/2)(1.001)(32/25)(4\cdot2^{20})^{-1/3}\right\}.
\]
Then its true right action costs
\[
       10.611 B_D\sqrt{t_M^2+t_H^2}.                          \tag{ASQ28.7}
\]
This follows from ASQ15.3–4 in the two original input windows \(97\le k\le2^{20}\) and \(k>2^{20}\). In the homogeneous estimate project to natural \(D\) **after** the whole \(T_F^{-1}\), then gain \((4N)^{-1/3}\) on this genuine output. In the second candidate for \(t_H\), both projections contract in \(H^{-4/3}\). Formula (ASQ28.7) works without commuting \(P_D\) past \(T_F^{-1}\). It applies, for example, to \(1024\ldots4096\), \(4097\ldots2^{20}\), and every larger natural index. Contributions from such separate natural regions sum by the triangle inequality for a common waist output. Using a known joint \(V\) bound on their union is an additional valid direct application. The actual \(b_j,B_D\) values and the signed finite matrix in (ASQ28.6) must come from compatible complete genuine source and normalization receipts.
