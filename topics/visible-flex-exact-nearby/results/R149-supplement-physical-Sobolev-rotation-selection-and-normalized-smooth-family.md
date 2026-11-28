# R149 ASQ24. A real Sobolev entry for the fixed rotation, with a unique physical parameter

Fix the genuine R31 selected member \(Q_*=Q_0+\delta_* Z,\ \nu_*=\nu_0+\delta_*\) and its true target \(\omega=2\pi\rho_{15}\). In this proof the regular variable is exactly the physical difference from the original affine direction,
\[
       Q=Q_0+(\delta_*+k)Z+z,\qquad \nu=\nu_*+k .
\]
All piecewise radial data and both means are retained. Put \(E=\|z\|_{L^2([0,r_*];L^2_\phi\oplus_2L^2_\phi)}\), \(\xi=\sup_r\|z\|_{A^0,\rm pair}\) and assume \(\xi\le10^{-7},\ \sup_r\|z_\phi\|_{A^0,\rm pair}\le10^{-6}\). These strong real bounds admit the physical value equation and its flow. Lipschitz estimates with a vanishing input difference are equalities at zero. The smallness scale below is in the ordinary negative **state** norm \(E\).

* For every such angularly smooth \(z\) with \(E\le 5\,10^{-14}\), there is a unique \(|k|\le6\,10^{-12}\) giving the exact target rotation of the true two-ray return. It obeys \(|k|\le114 E\). The selection has Lipschitz constant 114 in the ordinary state norm on this set.
* On a genuine regular path \(z=z(k)\) throughout \(|k|\le6\,10^{-12}\), assume the same strong bounds, \(\|z(0)\|_{L^2_rL^2}\le2\,10^{-14}\) and \(\|z(k_2)-z(k_1)\|_{L^2_rL^2}\le .005 |k_2-k_1|\). There is exactly one \(k\) for the target, with \(|k|\le260\|z(0)\|_{L^2_rL^2}\). Along a differentiable physical regular path the slope in this hypothesis is precisely \(q_\nu-Z\). The parameter selected on each such path depends continuously on external data continuous in the path's ordinary state norm.
* When the regular paths are angularly smooth, the selected return has a smooth orientation-preserving conjugacy. Along a family whose selected return is continuous in \(C^5\), its normalized conjugacy is continuous in \(C^2\). Smooth dependence of the return and paths gives smooth dependence of the selected parameter and normalized conjugacy, as established below.

The two radii concern a corrected state at the original R31 centre. In particular SM.30 gives only a larger upper bound for the distance of the alternative mean-exact compact trial. Its value defect, or the full regular correction about the original member, must be certified separately when using that trial. On a path these hypotheses suffice to impose phase on actual regular solutions without solving another coupled PDE on the phase chart. They do not supply the regular paths.

## The signed derivative at the true conjugacy

Use normalized angle of period \(2\pi\). Write \(F_a(x)=4G(P_{0,a}(G^{-1}(x/4)))\), where \(a=\delta_*+k\) and the zero denotes \(z=0\). Let \(h=\mathrm{id}+v\) be the genuine normalized R31 conjugacy at \(a=\delta_*\), and \(H(\phi)=h^{-1}(4G(\phi))/4\) its original physical coordinate map. Write
\[
 f_{z,k}=4H\circ P_{z,\delta_*+k}\circ (4H)^{-1},\qquad f_{0,0}=R_\omega.
\]
The [complete R31 family estimate](R133-supplement-complete-explicit-family-circle-KAM-inputs-and-gates.md) and its original public whole 3560-byte native from run 43586895661/1, SHA256 `d6e59dfa851fb7d385f6281389221408cc132f90be8c2b1577fdd2be9a348d61`, give
\[
 \|F_a{}_{,a}\|<2.208,\quad\|F_{a,xa}\|<2.432,\quad\|F_{a,aa}\|<55.92,
 \qquad \langle F_{0,a}\rangle>1/20 .                       \tag{ASQ24.1}
\]
In the last expression the initial parameter is \(a=0\), before selection. Here and below the comma denotes differentiation of the family. The real parameter window for (ASQ24.1) is \(|a|<10^{-8}\); its angular Wiener strip contains width .063 in normalized units. We only evaluate at \(|a|<10^{-10}\). The [actual wider conjugacy](R133-supplement-actual-physical-Wiener-conjugacy-strip.md) gives
\[
 |\delta_*|<9.369\,10^{-11},\quad
 \|v\|_{.0465}<8.85\,10^{-7},\quad \|v'\|_{.0465}<.000222 .
\]
Thus \(9.369\,10^{-11}+6\,10^{-12}<10^{-10}\). The complete original body obeys \(\|Z\|_{A^0}<19,\ \|Z_\phi\|_{A^0}<83\) by [SM.29](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md). Hence the entire parameter segment and all straight input segments used here belong to [RP.3](R144-supplement-full-off-constraint-principal-return-Hessian.md).

Let
\[
 B=\partial_k f_{0,0}=\frac{(\partial_aF_{\delta_*})\circ h}{h'\circ R_\omega},
 \qquad \mu=\langle B\rangle .
\]
Composition in the normalized Wiener algebra on .04 is legitimate by the displayed margin. It gives \(\|B\|_{.04}<2.21\). The change from the initial mean is bounded by
\[
 55.92|\delta_*|+2.432\|v\|+
 2.208\,\|v'\|/(1-\|v'\|)<.001.
\]
In particular \(\mu>.049\); this includes the original speed means and the true optical metric change. From \(\|v''\|_0\le.000222/(e\,.0465)\) one obtains
\[
 \|B'\|_{A^0}\le 2.432\frac{1+.000222}{1-.000222}
       +\frac{2.208\,.000222}{e\,.0465(1-.000222)^2}<2.45.
\]
Solve \(u\circ R_\omega-u=B-\mu\) with zero mean and both signs. The original *circle* divisor bound is \(1/|1-e^{ij\omega}|\le(17/4)|j|\); see W's final arithmetic statement. Thus
\[
 \|u\|_\infty\le(17/4)\|B'\|_{A^0}<11,\quad
 \|u'\|_\infty\le(17/4)\left(\frac{2}{e\,.04}\right)^2 2.21 <3300 .
 \tag{ASQ24.2}
\]
Fix \(\Psi_k=\mathrm{id}+ku\) and put \(G_{z,k}=\Psi_k^{-1} f_{z,k}\Psi_k\). This differs from the earlier fixed finite map denoted by plain \(G\) in \(F_a\). All maps have degree one with the physical lift chosen at the seed.

## True low-norm comparison on the whole folded body

Write \(X_z\) for any initial-to-interior folded trajectory and \(Y_z=\partial_k X_z\) at fixed \(z\), all in physical angle. The metric support is fixed below the true root. [RP.11,12,18](R144-supplement-full-off-constraint-principal-return-Hessian.md) bounds the integration factor on every shorter interval by 1.08 and the folded pure state value source by \(2(.610)E\). Apply the variational equation along a straight line of background inputs, to get
\[
 \sup|X_{z_2}-X_{z_1}|\le1.08(1.220)\|z_2-z_1\|_{L^2_rL^2}<1.318\|z_2-z_1\|_{L^2_rL^2}.                  \tag{ASQ24.3}
\]
This pays the full speed-mean derivative in RP.17. At \(z=0\) the entire folded integrals of \(\|V_{\phi\phi}\|,\|V_k\|,\|V_{k\phi}\|\) are below .629, .541 and 2.267, respectively. In the original R31 source and (C.9), the recorded positive bounds for `complete_return_second_angular`, `complete_return_first_parameter` and `complete_return_mixed_parameter` are \(J^2D_{20}^*,JV_1,JQ_1+J^2D_{20}^*V_1\) with \(J\ge1\). Each therefore bounds the corresponding whole field integral; \(|Y_0|<.541\) also follows from the second bound at every interior time.

On this window \(\|\beta D_K\|<6,\ \|Q_a\|_{A^0}<7,\ |\beta K_\nu|<4,\ |c_\nu|<47\), by RP.4,6,13 and TH.11. The uniform norm after removing the mean costs at most two. Consequently the integral difference of the coefficients \(V_\phi\) on the two trajectories is
\[
 \Delta L\le 2(.239)\,2(6)(14+1)\xi + .629(1.318)E
               <132\xi+2E .
\]
This pays both factors of \(Q\) in the differentiated primitive. The log of each angular Jacobian is the integral of this coefficient. The exponential between its two real values is at most 1.08. Thus \(|\Delta X_\phi|<143\xi+3E\).

At fixed angle the full change in \(V_k\) is the signed sum of \(2\beta I(Z^tD_K z)\), \(\beta K_\nu I(2v z_2+z_2^2)\), and the direct mean \(-\sigma c_\nu\langle z_2\rangle\), with the original two ray signs. The \(\langle Z_2\rangle\) term cancels only in this difference. RP.21's normalized primitive maps \(L^1\) to \(L^\infty\) with norm below one. The folded cost of these three terms is bounded by \(2\sqrt{.239}[2(6)19+4(14+1)+47]E<430E\), using \(|z_2|\le\xi\le1\). Comparing the two parameter-variation ODEs adds the displacement fee \(2.267(1.318)E\) and variation of the integration coefficient along the known \(Y_0\). Therefore
\[
 |Y_z-Y_0|\le1.08[.541(132\xi+2E)+430E+2.267(1.318)E]
                  <78\xi+470E.                              \tag{ASQ24.4}
\]
These estimates refer to the same time and initial angle; all are uniform.

The exact physical \(H\) satisfies \(.983<H'<1.017\) and \(\|H''\|_\infty<.8\), since the Wiener norm of \(H'-1\) on physical width \(1/128\) is below .016385. Applying this one coordinate map to (ASQ24.3–4), including the correct factor four in the parameter value, yields
\[
\begin{split}
 \|f_{z_2,k}-f_{z_1,k}\|_\infty&<5.37\|z_2-z_1\|_{L^2_rL^2},\\
 \|f'_{z,k}-f'_{0,k}\|_\infty&<155\xi+6E,\\
 \|\partial_k f_{z,k}-\partial_k f_{0,k}\|_\infty&<318\xi+1920E .
\end{split}                                                   \tag{ASQ24.5}
\]
For example the second line divides \(1.017(143\xi+3E)+.8(1.318)(1.08)E\) by .983. The last line uses \(4[1.017(78\xi+470E)+.8(1.318)(.541)E]\).

## Pointwise twist, scalar selection and simultaneous regular matching

For \(z=0\), \(f_{0,k}=h^{-1}F_a h\). On the real line \(\|(h^{-1})''\|<.002\) from the bounds on \(v'',v'\) above. Also \(\|F_a'\|<2\) from the physical \(G\) and its inverse in K.11 and the physical angular Jacobian in RP.12 (the inverse bound follows from \(\|G'-1\|<.017213\) in K.6). Thus (ASQ24.1) gives \(\|f_{0,k,xk}\|<3,\ \|f_{0,k,kk}\|<57\) on the whole stated interval. With (ASQ24.2,5),
\[
 \|G_{z,k}-R_\omega\|_\infty<25|k|+5.4E ,
 \qquad \|G_{z_2,k}-G_{z_1,k}\|_\infty<5.38\|z_2-z_1\|_{L^2_rL^2}.
 \tag{ASQ24.6}
\]
Indeed \(\|(\Psi_k^{-1})'\|\le(1-3300|k|)^{-1}\) and \(\|f_{0,k}-R_\omega\|\le 2.21|k|\) by the whole parameter derivative bound for \(h^{-1}F_a h\).

The numerator for the true fixed-input derivative \(\partial_k G_{z,k}\) is
\[
 (\partial_k f_{z,k})(\Psi_k)+f_{z,k}'(\Psi_k)u-u(G_{z,k}),
\]
and its denominator is \(1+ku'(G_{z,k})\). At \(k=z=0\) the numerator is exactly \(B+u-u\circ R_\omega=\mu\) pointwise. Its difference from \(\mu\) is at most
\[
 (318\xi+1920E)+57|k|+3(11)|k|
  +(155\xi+6E+3|k|)11+3300(25|k|+5.4E).
\]
The third term pays shifting the known \(B\) by \(ku\). For \(\xi\le10^{-7},\ E\le10^{-12},\ |k|\le6\,10^{-12}\), substitution gives the pointwise strict lower
\[
                         \partial_k G_{z,k}>.048 .          \tag{ASQ24.7}
\]
The larger cap on \(E\) in this comparison covers every interpolation needed on a regular path, where \(E\le 2\,10^{-14}+.005(6\,10^{-12})\).

For fixed \(z\), at the two parameters \(\pm114 E\) the maps are strictly on opposite sides of \(R_\omega\), by (ASQ24.6–7) and \(.048(114)>5.38\). When \(E=0\) the exact seed solves the equation. Both parameters belong to the paid window. A continuous ordered lift between two translations has translation number between their increments, by iterating the inequalities. The translation number is continuous in the uniform lift topology (equivalently, approximate it by the extremal \(n\)-step displacements divided by \(n\), whose gap is at most one period divided by \(n\)). This gives a root for the exact lifted increment \(\omega\). If there were two, the larger parameter produces a strictly larger map at every angle. Conjugating by the first root's true increasing conjugacy gives a map pointwise strictly above the rigid rotation, hence with strictly larger translation number. Smoothness of that conjugacy is proved below; an increasing homeomorphic conjugacy suffices here. The same order comparison with the second estimate of (ASQ24.6) gives \(|k(z_1)-k(z_2)|\le114\|z_1-z_2\|_{L^2_rL^2}\).

For variable \(z(k)\), subtract the fixed-input comparison across its two parameter values and then subtract the change of the physical input. The resulting pointwise increase per unit change in \(k\) is at least \(.048-5.38(.005)>.021\). Since \(.021(260)>5.38\), the signed barriers now lie at \(\pm260 E(0)\), still inside the paid window. The same argument gives uniqueness. For two paths satisfying these hypotheses the change in their roots is at most \(260\sup_k\|z_1(k)-z_2(k)\|_{L^2_rL^2}\). This procedure retains the genuine solution along each path at every parameter. It applies to a regular curve already constructed in the \(Z\) chart and does not require any change to the finite trial \(h^a\).

## Smooth regularity, normalized continuity and derivatives along data families

Rescale the circle by its period. The bound \(|1-e^{2\pi i j\rho_{15}}|^{-1}\le(17/4)|j|\), together with \(|1-e^{2\pi i x}|\le2\pi\operatorname{dist}(x,\mathbb Z)\), gives \(|\rho_{15}-p/q|\ge 2/(17\pi q^2)\). The time-dependent folded field is smooth in angle as soon as the regular body is smooth there, for instance piecewise \(L^2_rH^m_\phi\) for every \(m\); products of two such input derivatives are radially integrable. Its integral equation and variational equations on each original piece give a \(C^\infty\) orientation-preserving return, including at the true root by integration in radius. It has degree one and positive derivative by RP.12. The corollary on p.335 of J.-C. Yoccoz, *Ann. sci. ENS* 17 (1984), now supplies a genuine smooth conjugacy for the selected lift with this rotation number. [Original article, pp.334–335](https://www.numdam.org/item/10.24033/asens.1475.pdf)

For parameter continuity use Mostapha Benhenda, *Bull. Soc. Math. France* 142 (2014), Theorem 1.6 (5), p.677. For constant-type \(\rho_{15}\), \(k_{\rm reg}=5\), \(\eta=1/2\), its bound controls the conjugacy derivative in \(C^{2,1/2}\) by the Diophantine constant, \(\|Df\|_\infty\), the variation of \(\log Df\) and \(\|Sf\|_{C^2}\), with \(Sf\) the Schwarzian. These data are locally uniformly bounded for a family continuous in \(C^5\) with positive derivative. Fix the additive or input rotation of the conjugacies, for instance by fixing the preimage or value of a point. Arzelà–Ascoli gives precompactness in \(C^2\). Any subsequential limit is a degree-one, nondecreasing solution of the same conjugacy equation at the limiting parameter. Composing with the smooth conjugacy known at that parameter gives a continuous map commuting with an irrational rotation. Its periodic displacement is constant by density of irrational orbits, which implies it is a rotation. The point normalization forces the same limit for every subsequence. The limit is a diffeomorphism, so the inverse conjugacy also converges in \(C^2\). Larger \(k_{\rm reg}\) proves continuity in every smooth seminorm for a \(C^\infty\)-continuous family. [Original article, Theorem 1.6](https://www.numdam.org/item/10.24033/bsmf.2676.pdf)

Here is the derivative argument for smooth data or smooth regular paths, beyond pointwise conjugacy. Denote the conjugated pointwise monotone maps by \(F(s,k)\), with \(s\) any finite-dimensional external parameters; the place of \(z\) is explicit in (ASQ24.5–7). On a true smooth regular path the preceding difference comparison gives \(F_k\ge.021\); on a fixed-input family it gives \(F_k\ge.048\). The corresponding root \(k(s)\) is locally Lipschitz by the already proved comparison. At a fixed \(s\), write \(g\) for the conjugacy from the rotation to the return, in a common point gauge. At \(s+v\) set \(g_v=g\psi_v\) with \(\psi_v=\mathrm{id}+a_v\). The common gauge ensures \(a_v(0)=0\). With \(\Delta k=k(s+v)-k(s)\), the exact equation is
\[
 a_v\circ R_\omega-a_v
  = [g^{-1}F(s+v,k+\Delta k)g-R_\omega]\circ\psi_v .
 \tag{ASQ24.8}
\]
Its mean is zero. The bracket has first variation \(L_s v+L_k\Delta k\), with \(L_i=(F_i\circ g)/(g'\circ R_\omega)\). Smooth continuity already proved gives \(\psi_v\to\mathrm{id}\) in every smooth seminorm. Composition and Taylor's theorem give the remainder \(o(|v|)\) in each fixed seminorm since \(\Delta k=O(|v|)\). Moreover \(\langle L_k\rangle\ge.021\langle1/g'\rangle\ge.021\) by Jensen and degree one. Thus the complete parameter derivative is \(-\langle L_s v\rangle/\langle L_k\rangle\). The normalized solution of (ASQ24.8) divided by the external increment follows by the exact circle Fourier inverse, losing at most one Sobolev order, and by evaluating its additive constant at zero. This proves the first derivative without assuming differentiability of either root or conjugacy. The derivative formula depends smoothly, with finite loss in any prescribed seminorm, on \(F,g,k\) and their already available jets: inversion of \(g'\), composition, the fixed Fourier inverse and the scalar denominator above. Induction differentiating this explicit formula proves all mixed finite-dimensional derivatives, continuously in every smooth seminorm. The physical mean-normalized lift is obtained by the unique input rotation subtracting \(\langle g-\mathrm{id}\rangle\) after restoration of all known changes of angle. No change to the prescribed rotation or to either physical density mean is involved.
