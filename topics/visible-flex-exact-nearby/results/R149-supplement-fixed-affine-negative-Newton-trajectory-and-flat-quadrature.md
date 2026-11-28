# R149 ASQ27. A fixed-affine negative Newton trajectory with a certified ordinary body and waist

Let \(h_*=\mathcal V_*(-f_{\delta_*})\) be the same zero-root, zero-impulse physical negative summand as [ASQ26](R149-supplement-correlated-base-to-selected-negative-Newton-response.md). The following computation measures this summand in ordinary \(L^2_rL^2_\phi\) and at its physical waist. The independent roots, height, positive return and boundary data in the regular solution retain their original definitions.

The affine geometric parameter is the exact \(\eta_0=-7789843107295549/4611686018427387904\) of the original affine graph 91040c22…. The angular velocity \(-\gamma(r)\langle v(r)\rangle\) is still the varying physical coefficient of this graph. The two original affine arrays supply the complete frozen spline and its parameter direction. All original 184 current and 32 historical inputs and the WSS 7728-piece partition are admitted. For this new base forcing take \(Q_0=(u,s+w)\), \(\nu_0=-2572625729470897/72057594037927936\), and apply the true selected flow as below. On every original cubic, the complete repaired \(65\) unnormalized sine, mean and cosine amplitudes are \(\alpha\) times the four original dyadic PPoly coefficient vectors, plus the witnessed base repair on the constant term. Here \(\alpha=6890507429876859/9007199254740992\).

Write \(v=s+w,\ m=\langle v\rangle,\ S=u^2+Kv^2,\ d=-\beta I S\), with the original zero-mean angular primitive \(I\). The exact source is
\[
g=-f_0=\binom{d u_\phi+\gamma mK v_\phi-\beta u(1+S)-u_r}
 {d v_\phi-\gamma m u_\phi+
       \beta\{w-u^2v-Kw(v^2+vs+s^2)\}-w_r}.                    \tag{ASQ27.1}
\]
This is the original signed cubic source after subtracting the rotational equation for \(s_r\). All one-sided original cubic derivatives enter before angular transformation. The complete linearization \(A_0\) retains the terms \(-2\beta (u_\phi,v_\phi)I(ua+Kvb)\) and \(\gamma(Kv_\phi,-u_\phi)\langle b\rangle\) on a trial \((a,b)\), along with the full local transport and reaction in [TC](R149-supplement-two-signed-negative-waist-responses-and-common-Gram-remainder.md). The base forcing has angular labels \(|j|\le96\). The full \(A_0L\) on the trial below has \(|j|\le160\).

On a single fixed original intrinsic germ, the original 512-point primitive with all Fourier aliases bounded gives \(a,\beta,H,E,\bar E,K_{\mathrm{old}}\). Take the full fixed controlled values, with \(W\) the original compact bump,
\[
 G=\bar E e^{\nu_0W},\quad R=H^2+E/a^2+\bar E(e^{\nu_0 W}-1)/a^2,\quad
 \gamma=\sqrt G,\quad s=-\sqrt{G/R},\quad
 K=e^{-\nu_0W}\!\left(K_{\mathrm{old}}+
              {\nu_0\beta W'\over2a^2\bar E}\right).
\]
The original square bounds for \(G,R,G/R\) certify the same positive real square-root branches. In a group of halfwidth \(b\) contained in one true spline and control germ, enclose all four scalar magnitudes by \(M_\ell\) on the complex square of halfwidth \(24b\). On this germ enclose the Taylor coefficients at the true centre through order 22, retaining the full analytic angular primitive tails in every coefficient. The real evaluation error for field \(\ell\) is at most \(M_\ell\,24^{-23}/(1-1/24)\). Failed chart enclosures split before a subcell is accepted. The complete original 3073 negative closed restriction cells, the two ends of the genuine unknown-root bracket and the strict/root interface are all retained. Every subcell of halfwidth \(h\) in such a group has its own complex radius-\(16h\) disk inside the certified group disk. The same local polynomial germ has a complex continuation across its real subdivision ends.

Choose an ordinary degree-eight polynomial \(L(t)\) in all 193 normalized reflected coordinates, \(t\in[-1,1]\),
\[
 L(t)={(1-t)L_l+(1+t)L_r\over2}+(1-t^2)\sum_{j=0}^{6}b_j t^j .
\]
The floating Picard evaluations only choose the finite dyadics \(L_l,L_r,b_j\). Neighbouring reverse cells share the identical \(L_r=L_{\mathrm{next},l}\), so every radial interface has zero jump. The trial is identically zero on the full original uncertain root bracket. At real evaluation points use the complete complex Laurent polynomials with \(\partial_\phi e^{4ij\phi}=4ij e^{4ij\phi}\). Positive and negative sine coefficients have opposite signs, even cosine coefficients agree, and only the even row has an independent mean. Form the signed residual
\[
 e=g+A_0 L-L_r\quad (L_r\text{ here denotes the ordinary radial derivative}).
\]
Let \(M\) bound \(\sum_{a,j}|e_{aj}(z)|\) on \(|t|\le16\). This complex cap uses both raw PPoly components, their ordinary radial derivatives, the complete angular derivatives, and the literal analytic polynomial \(L,L_r\). In particular, set \(u_b=\|u\|_{A^0}, w_b=\|w\|_{A^0}, v_b=w_b+|s|,\ p_b=\|u_\phi\|_{A^0}+\|w_\phi\|_{A^0},\ m_b=|s|+|w_0|,\ k=|K|,\ k_m=\max(1,k)\). For the pair sum \(A^0\), the linearized cap is
\[
 \|A_0 L\|\le \left[384\{ |\beta|(u_b^2+kv_b^2)/4+|\gamma|m_bk_m\}
 +|\beta|\{2+4(1+k)(u_b+v_b)^2\}
 +|\beta|p_b(u_b+kv_b)/2+|\gamma|k_m p_b\right]\|L\|.
\]
This follows termwise from the four local reaction entries, \(\|I\|\le1/4\) and the complete input derivative. The cap for \(g\) follows directly from (ASQ27.1). Retain the complex scalar errors while certifying the real residual; independent enclosure of the finite products using FLINT gives all finite Fourier coefficients directly.

For a strict cell set \(v_j=1\); in the genuine root region set \(v_j=(1+16j^2)^{1/3}\). The polarized function \(P(t)=\sum_{a,j}v_j e_{aj}(t)\overline{e_{aj}(\bar t)}\) is analytic on the closed radius-16 disk and bounded there by \(v_{160}M^2\). Its real values equal the actual squared norm. Use the flat-measure normalized Clenshaw–Curtis sum \(Q_{48}\) on the 49 nodes \(\cos(i\pi/48)\). For \(N=48\) and \(\theta=i\pi/N\) its weights are
\[
 \frac{c_i}{N}\left(1+2\sum_{m=1}^{N/2-1}
   \frac{\cos(2m\theta)}{1-4m^2}+\frac{\cos(N\theta)}{1-N^2}\right),\qquad
 c_0=c_N=\tfrac12,\quad c_i=1\ (0<i<N).
\]
Cosine orthogonality on the doubled grid and \(\frac12\int_{-1}^1 T_{2m}(t)\,dt=(1-4m^2)^{-1}\) prove degree-48 exactness. The owner verifies every directed weight is positive. Subtracting the Taylor polynomial through 48 from both the integral and positive quadrature gives
\[
 \int_{\rm cell}\|e\|^2\,dr
 \le 2h\left[Q_{48}(P)+
 \frac{2v_{160}M^2\,16^{-49}}{1-1/16}\right].                 \tag{ASQ27.2}
\]
The integrals \(\int\|L\|_2^2\,dr\) are exactly integrated by the same flat quadrature, as the integrand has degree at most 16. All quadrature evaluations are directed, including the trigonometric nodes and local radial polynomials.

Accumulate the full squared residuals \(E_i^2\) and squared ordinary trial masses \(T_i^2\) on the disjoint strict region \(i=S\), root region below the bracket \(i=R\), and uncertain bracket \(i=B\). The nonnegative integrands on the closed bracket cover its genuine part. The genuine selected linearization differs on the entire physical interval. On \(|j|\le96\), the complete original selected-core run 43713242980/1 gives \(\|(A_{\delta_*}-A_0)L\|_2<d\,\|L\|_2\), \(d=1.049107\,10^{-5}\). Its output has labels \(|j|\le 96+192=288\) from the two base/family coefficients of degree at most 96 and the input degree 96. No transformed angle acts on this estimate. Hence \(\epsilon_S=E_S+dT_S,\ \epsilon_R=E_R+10.484dT_R,\ \epsilon_B=E_B\); \(T_B=0\). For the physical zero-root response at the selected operator, let
\[
 c=2333968743003/10^{13},\quad R=1/200,\quad b=r_+-r_-,\quad U=8.22,\ C=6.531704,\ A=25.943 .
\]
The strict Volterra kernel and the original mixed/ordinary root kernel in [NRO](R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md) and [NHT](R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md) give, after the actual [ASQ26](R149-supplement-correlated-base-to-selected-negative-Newton-response.md) source transfer,
\[
 \begin{aligned}
 \|h_*-L\|_{L^2_rL^2_\phi}
 &\le (cU/\sqrt2)\epsilon_S+A(\sqrt R\,\epsilon_R+\sqrt b\,\epsilon_B)
       +1.019\,10^{-15},\\
 \|h_*(0)-L(0)\|_2
 &\le U\sqrt c\,\epsilon_S+UC(\sqrt R\,\epsilon_R+\sqrt b\,\epsilon_B)
       +2.12\,10^{-15}.                                      \tag{ASQ27.3}
 \end{aligned}
\]
The shorter factor \(\sqrt b\) uses the actual support length of the bracket residual in the same root Duhamel integral. The whole ordinary body is bounded by the first line plus \((\sum_iT_i^2)^{1/2}\). The complete ASQ22 physical receivers apply to the second line around the **signed** dyadic trial waist. The new job reports the actual values and the truth value of the \(2\,10^{-14}\) one-summand radius comparison, independently of the size attained. Neither this comparison nor a complete regular solution is a prerequisite for preserving the actual full-suffix evidence.
