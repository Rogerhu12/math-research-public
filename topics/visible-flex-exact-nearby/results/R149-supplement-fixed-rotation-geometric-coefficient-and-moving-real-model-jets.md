# R149 ASQ19. A genuine scalar neighborhood and the moving real waist inverse

The fixed rotation on the [ASQ8 exact phase leaf](R149-supplement-selected-physical-phase-fibre-summable-analytic-iteration.md) allows a neighborhood of the actual first-coefficient mean, with all original frequency labels retained. The model inverse and all of its scalar derivatives lose only one angular derivative in the moving reflected basis. A change of phase in the fixed physical basis has the additional translation derivatives quantified below.

## The actual coefficient before conjugation

Use the original radial coordinate \(\rho=r_*-r\), fixed \(r_*\), the actual radial intrinsic fields \(k,b,\gamma\), and take a fixed \(h\in(0,r_*)\) inside the common root germ. To avoid any subtraction of singular input balls let \(A,B,C,D\) be the full fields of [CT.10](R133-supplement-regular-density-transport-for-complete-first-coefficient.md). Thus for \(q=\sqrt{\rho k}\) and full physical mean \(\eta=-\gamma\langle v\rangle\),
\[
 t={k_\rho\over4k}-b(1+u^2+\rho k v^2),\qquad
 (A,B,C)=\big((16\eta\sqrt k)^{-1},\ t/(2\eta\sqrt k),\ t^2/(\eta\sqrt k)\big),
\]
\[
 D=4b^2\sqrt k\,u^2v^2/\eta+2b\sqrt k\,(uv_\phi-vu_\phi).
\]
Here \(u,v\) are the physical fields. Denote the scalar model multiplier mean by \(\xi\). Write \(\langle\ \rangle\) for normalized angular measure, \(A_0=A(0),A_1=A_\rho(0)\), \(A_2(\rho)=\int_0^1(1-s)A_{\rho\rho}(s\rho)\,ds\) and \(B_1(\rho)=\int_0^1 B_\rho(s\rho)\,ds\). The original scalar finite part is the following bounded *linear functional in the displayed four fields*:
\[
 \begin{split}
 {\cal V}(A,B,C,D)={}&-{2 A_0\over3h^{3/2}}
      -{2(A_1+\langle B(0)\rangle)\over\sqrt h}\\
 &+\int_0^h\{\rho^{-1/2}\langle A_2+B_1+C\rangle
                      -\sqrt\rho\,\langle D\rangle\}\,d\rho\\
 &+\int_h^{r_*}\langle\rho^{-5/2}A+\rho^{-3/2}B
                  +\rho^{-1/2}C-\rho^{1/2}D\rangle\,d\rho .
 \end{split}                                                  \tag{ASQ19.1}
\]
Indeed [PF.25–29](R133-supplement-pointwise-root-finite-part-and-complete-true-ray-first-coefficient.md) gives exactly this finite part because the actual density changes preserve the complete scalar mean. The subprincipal mean is \(\xi=-{\cal V}/2\), by [B.9–13](R133-supplement-selected-family-root-finite-part-and-actual-first-phase.md) and WCS.2 in the original regular-root chart. At the selected member \(|\xi_*|<36.957\). The coefficient is distinct from the physical metric parameter and from both physical mean equations.

All nearby intrinsic inputs \(k,b,\gamma\) below remain radial, as on the original physical metric. In particular \(\eta=-\gamma\langle v\rangle\) and \(A,A_0,A_1\) are radial; \(u,v\) retain their full angular dependence and means. Formula (ASQ19.1) itself defines an analytic extension to these nearby real smooth fields with positive \(k,\eta\), with the same fixed interfaces and radial root. For completeness an explicit derivative budget follows. For each input \(u,v,k,b,\gamma,\rho\) take the sum of the piecewise sup norms of \(\partial_\rho^i\partial_\phi^j/(i!j!)\), \(0\le i\le2,0\le j\le1\), using one-sided derivatives on each radial piece. The maximum over pieces of these sums is a submultiplicative algebra norm; use its sum over perturbed fields. Include the true radial and angular means. A smaller output norm for \(t,B,C,D\) is allowed: \(B\) needs only one radial derivative on the root collar, \(C,D\) only zero. One can therefore evaluate their low bounds using ordinary Leibniz rules for these indicated derivatives. All positivity margins and base norms here are on the complete selected pieces. This strong space is used for the scalar symbol; the weaker radial \(L^2\) phase-input norm by itself bounds no radial trace.

For an explicit analytic ball put \(M\ge2\) larger than the algebra norms of the five base fields \(u,v,k,b,\gamma\) and the base fields \(k^{-1},k^{1/2},\eta^{-1},\rho\). These are finite on the selected compact pieces: the original base has positive \(k,\eta\), smooth root germs and finite one-sided coefficients on each piece. Set \(d=(32M^3)^{-1}\). For complex perturbations of total norm \(<d\), each numerator base field has norm \(<2M\). Mean is contractive and \(\|\delta\eta\|\le 2Md+d^2<3Md\), hence \(\|\delta\eta/\eta_*\|,\|\delta k/k_*\|<1/4\). The reciprocal and binomial series bound \(k^{-1},\eta^{-1},\sqrt k,1/\sqrt k\) by \(4M^2\) on this ball, with their indicated derivatives. For \(1/\sqrt{k_*}\) use \(\sqrt{k_*}\,k_*^{-1}\). All four fields, their two needed \(A\)-derivatives and the one needed \(B\)-derivative are bounded in ordinary sup norm by \(L=(16M)^{24}\). For example the reduced algebra norm of \(k_\rho\) with at most one radial derivative is \(\le2\|k\|\), \(t\) is a sum of products with at most five undifferentiated factors, and the squared term \(t^2/(\eta\sqrt k)\) is the largest such product. The factorial weights cost at most two for the unweighted second derivative. These operations commute with the continued bounded integral (ASQ19.1). Thus \(|\xi|\le V\) throughout the complex ball, where one may take
\[
 V=L\!\left[
 {2\over3h^{3/2}}+{4\over\sqrt h}+6\sqrt h+{2h^{3/2}\over3}
 +\int_h^{r_*}(t^{-5/2}+t^{-3/2}+t^{-1/2}+t^{1/2})\,dt\right]+1 .
\]
The disk estimate at the base gives \(|\xi-\xi_*|\le (2V/d)\|\delta U\|\) for \(\|\delta U\|\le d/2\), where \(U=(u,v,k,b,\gamma)\). On \(\|\delta U\|\le d/4\) the mixed directional bounds are \(\|D\xi\|\le4V/d,\ \|D^2\xi\|\le64V/d^2\), using two complex scalar circles of radius \(d/8\) for the second one. Hence every input of norm at most \(d/(64V)\) above the base obeys \(|\xi-\xi_*|\le1/32\). These same estimates apply to composites with a varying intrinsic metric by the ordinary product and chain rules, with its actual derivatives in \(k,b,\gamma\). The scalar formula does not prove a strong-remainder or a moving-root parametrix for arbitrary rough backgrounds.

## Exact real-model reciprocal on that neighborhood

Fix the original \(\Omega\), \(a=2H(0)\), \(b_{\rm ph}=a+\Omega\) as phase slots, retaining the moving common translation below. For \(n\ge97,\ k_n=4n,\ \theta_n=2n\Omega+\pi/4\), [WCS.7–10](R133-supplement-certified-Cayley-gap-on-the-reflected-waist-model.md) gives the real normalized coefficient
\[
 s_n(\xi)=\cos\theta_n-\xi\sin\theta_n/k_n,\qquad
 \gamma_n(\xi)=1/s_n(\xi).
\]
On \(1\le n\le96\) the original reference inverse has \(\gamma_n=1\) identically. The [whole ASQ16](R149-supplement-actual-all-frequency-primitive-and-single-physical-gate.md) and [whole ASQ14](R149-supplement-original-WMA-head-on-the-true-signed-waist-inverse.md) give \(g_*:=\sup_{n\ge97}|\gamma_n(\xi_*)|/k_n<32/25\) and a bound .573 up to \(2^{20}\). Use the exact identity
\[
 \gamma_n(\xi)=\gamma_n(\xi_*)
 \sum_{j\ge0}\big[(\xi-\xi_*)\sin\theta_n\,\gamma_n(\xi_*)/k_n\big]^j .
                                                               \tag{ASQ19.2}
\]
On the entire complex disk \(|\xi-\xi_*|\le1/32\) it gives \(g(\xi)<4/3\), and \(g_n(\xi)<.584\) on \(97\le n\le2^{20}\). Every individual signed-multiplier fee in ASQ16 is enlarged by a factor at most \(25/24\), including those that contain an additional primitive or a fractional Bessel power: those scaled multipliers are individually linear in \(|\gamma_n|\). The cube used to store one old third power needs its cube root before this comparison.

In the original moving orthonormal coordinates the complete inverse satisfies, for every \(s\in\mathbb R\) and all \(m\ge0\),
\[
 \|\partial_\xi^m\bar G(\xi)\|_{H^s\to H^{s-1}}
       \le m!(4/3)^{m+1}.                                   \tag{ASQ19.3}
\]
Indeed \(\partial_\xi^m\gamma_n=m!\gamma_n^{m+1}(\sin\theta_n/k_n)^m\) on the high lines, and \(k_n/\sqrt{1+k_n^2}\le1\). The low scalar derivatives vanish for \(m>0\); for \(m=0\) the low reference costs at most \(1/4\) in this loss-one norm. Formula (ASQ19.2) converges in operator norm there. In particular no second divisor or further angular derivative is lost by differentiating the physical coefficient mean.

Keeping the geometry factors at their actual selected bounds, simultaneous substitution of \(\xi\) in the high model, its reciprocal, and all occurrences of the coefficient mean in the coordinate identity [ASQ10.6](R149-supplement-practical-high-cut-with-paid-coordinate-errors.md) gives the full complement bound
\[
 \|P_{97}(\mathcal L-Id)P_{97}\|
 <{25\over24}\big(.441+.1 C_{\rm phys}(97)\big).            \tag{ASQ19.4}
\]
Indeed \(|\xi|\le36.957+1/32<37\), the existing ASQ15/16 bound for that scalar. The exact high reference correction still vanishes; the original two window estimates are sums of nonnegative terms either independent of \(\gamma_n\) or linear in its weighted modulus. This includes the orthogonal combination preceding the one physical output norm. The other coefficient, chart and physical norm restrictions are the ones actually used by ASQ10–16; (ASQ19.4) isolates the complete cost of this moving scalar. At \(C_{\rm phys}(97)\le5\) and those same remaining bounds the right side is \(<.981\). No uniform bound for a changed physical PDE remainder follows from varying this scalar alone.

## Motion of the two actual reflection lines

Use \({\cal T}_t f(x)=f(x-t)\), with generator \(D=-\partial_x\). Writing \(k=4n\), WCS.7–10 gives the target \(\widetilde v_n^a=\sqrt2\cos(kx-ka/2)\) and the input \(\widetilde u_n^{b_{\rm ph}}=\sqrt2\cos(kx-kb_{\rm ph}/2-\pi/4)\): the positive-frequency coefficients are respectively \(e^{-ika/2}/\sqrt2\) and \(e^{-i(kb_{\rm ph}/2+\pi/4)}/\sqrt2\). Applying \({\cal T}_{(a-a_*)/2}\) multiplies both positive coefficients by \(e^{-ik(a-a_*)/2}\) and both negative ones by its conjugate. Since \(b_{\rm ph}-b_{{\rm ph},*}=a-a_*\), this is exactly their common translate with the displayed positive translation parameter. Extend \(\bar G\) to zero on the orthogonal complement of each target line, also on the auxiliary scalar mean. Its exact ambient expression is \({\cal T}_{(a-a_*)/2}\bar G(\xi,a_*){\cal T}_{-(a-a_*)/2}\). For smooth data its jets are
\[
 \partial_a^\ell\partial_\xi^m\bar G
 =2^{-\ell}\sum_{k=0}^\ell(-1)^k{\ell\choose k}
       D^{\ell-k}(\partial_\xi^m\bar G) D^k,\qquad
 \|\partial_a^\ell\partial_\xi^m\bar G\|_{H^s\to H^{s-1-\ell}}
       \le m!(4/3)^{m+1}.                                   \tag{ASQ19.5}
\]
Both same-frequency signs rotate, and the range and the target projection have both been differentiated. The bounds pass to strong derivatives on each fixed input by smooth density. In operator norm an arbitrary positive extra derivative loss suffices: cut off a finite head and bound the uniform remaining tail by its inverse extra weight. This avoids assuming norm differentiability of translations at the limiting index.

For a physical path with two tangent directions \(h,l\), writing subscripts for actual scalar derivatives, the first jet is \(G_\xi\xi_h+G_a a_h\). The entire second jet is
\[
 G_{\xi\xi}\xi_h\xi_l+G_{\xi a}(\xi_h a_l+\xi_l a_h)
 +G_{aa}a_h a_l+G_\xi\xi_{hl}+G_a a_{hl}.
\]
The scalar jets of \(\xi\) are actual derivatives under (ASQ19.1); the phase is the original inverse-lift value \(a=2H(0)\). If \(H=g^{-1}\), at \(x_0=g^{-1}(0)\) they are
\[
 a_h=-2g_h(x_0)/g'(x_0),\quad
 a_{hl}=-2\,[g_{hl}+g'_h x_l+g'_l x_h+g''x_hx_l](x_0)/g'(x_0),
 \qquad x_h=a_h/2,\quad x_l=a_l/2 ,
\]
where \(x_h,x_l\) are scalars. The actual ASQ8 tube has \(1/g'\le2\). Evaluating these terms therefore costs the indicated low angular derivatives of the genuine phase solution. The physical source and target normalizers, independent physical means, negative-body phase equation and physical height are not encoded in this two-line Fourier model; they keep their respective jets and common reconstructed solution.
