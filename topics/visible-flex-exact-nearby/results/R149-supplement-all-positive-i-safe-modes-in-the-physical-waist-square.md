# R149 ASQ12. The ordinary physical waist block on all positive-$i$ safe modes

Use the complete transformed physical row [ASQ10.6](R149-supplement-practical-high-cut-with-paid-coordinate-errors.md) and the single orthogonal projection $P_s$ of [ASQ11.7](R149-supplement-positive-i-model-primitive-fees-on-all-original-indices.md). The exact set includes all frequencies beyond $2^{34}$ and all but at most 372 of the frequencies between the first 96 and that tail. Denote the physical factor of ASQ10.1 at ordinary cutoff $97$ by
$$
 H_{\rm phys}=\|P_{97}(E_\partial^{\rm fr}+\Delta_\partial):
                     X_{\rm fr}^{-4/3}\longrightarrow Y_a^0\|.
$$
The complete safe square has distance from identity bounded by
$$
              4/5+(11/50)H_{\rm phys}.                    \tag{ASQ12.1}
$$
Every coordinate cost in $4/5$ below is proved for the true selected density and the original two-sided coefficients. In particular $H_{\rm phys}\le3/4$ suffices for invertibility simultaneously on all safe modes. The homogeneous row omits the positive feedback $\Delta_\partial$. The true physical norm in this test and the remaining signed finite square need their own actual estimates.

## The complete density inverse on two nearby windows

Write $S=U_\psi$, $p=\psi^{-1}$, $C$ for its diagonal same-sign compression, $D=S-C$. For $j,n\ge1$ the opposite-sign kernel is the true integral of $e^{-4i(ny+jp(y))}$ against normalized measure, with a conjugate block for the other sign. The real-axis bounds $p'>.9749=:m$, $|p''|<1/6$, $|p'|<1.0251$ are [SDI.4](R149-supplement-actual-small-density-inverse-constants-and-Theta-errors.md). One periodic integration by parts gives
$$
 |D_{j,-n}|\le \frac{(1/6)j}{4m^2(n+j)^2}.
$$
For $L^2$ units the matrix is bounded by this kernel; for $\dot H^{-1}$ units multiply by $n/j$. These two bounds are transposes. Schur's test with weights $j^{-1/2}$ costs at most $\sqrt{(\pi/2)(\pi/2+1/3)}$ for the kernel $j/(n+j)^2$. In the row sum the decreasing summand $n^{-1/2}/(n+j)^2$ is bounded by its integral from zero. In the column sum rescale $\sqrt{x}/(1+x)^2$; its integral is $\pi/2$ and its maximum is less than $1/3$. For a nonnegative unimodal function the sum is at most its integral plus its maximum. Thus
$$
                  \|D\|_{0\to0},\ \|D\|_{\dot H^{-1}\to\dot H^{-1}}<.08.
$$
On zero-mean inputs the $L^2$ norm of $S^{-1}$ is at most $\max(m^{-1/2},\sqrt{1.0251})<1.013$. The same bound holds for its $\dot H^{-1}$ norm: take a periodic primitive before and after the pushforward, apply the ordinary composition change of variables, and remove its constant orthogonally. As $C=S-D$ is a Neumann perturbation on each complete window, its inverse there agrees with the density inverse on their common dense domain (and hence with SDI). In detail partial Neumann sums are the same on their intersection and converge in both norms. Therefore
$$
                 \|C^{-1}\|_{0\to0},\
                 \|C^{-1}\|_{\dot H^{-1}\to\dot H^{-1}}<1.11.
                                                             \tag{ASQ12.2}
$$

## Resolving the true analytic error of the original inverse lift

Let $\widehat p$ be the complete degree-one trial lift of [IL](R149-supplement-actual-original-inverse-density-lift.md). On the original strip $\sigma=1/256$, $\|p-\widehat p\|_\infty<E=2.211\,10^{-7}$. On the real axis IL and SDI give $\widehat p'>.975$, $|\widehat p''|<.133$, $|\widehat p'''|<.814$. The lower derivative follows from SDI.3 and $P_1<1.024974$. Define $\widehat D$ by the same opposite-sign kernel with $\widehat p$ in the phase. Two integrations by parts now give
$$
 |\widehat D_{j,-n}|\le b\,j/(n+j)^3,\quad
 b=\tfrac1{16}\big(.814/.975^3+3(.133)^2/.975^4\big)<.059 .
$$
Use $\dot H^{-1}$ input and $L^2$ output. After multiplication of columns by $4n$ the symmetric majorant is $4b j n/(n+j)^3$. With weights $j^{-1/2}$, each whole Schur sum is at most $4b(\pi/8+.26)$: rescale $\sqrt x/(1+x)^3$, whose integral is $\pi/8$ and whose maximum is less than $.26$. If $j\ge97$ in the output, the row correction drops to $.26/97$. For columns $n\ge97$ the same holds. For $n<97$ the column sum from $j=97$ is dominated by the integral from $96$ because its summand is decreasing there. Thus
$$
         \|P_{97}\widehat D\|_{\dot H^{-1}\to0}<.094,\qquad
         \|\widehat D\|_{\dot H^{-1}\to0}<.155 .
$$

For the actual analytic leg derivative, [DG.3–4](R149-supplement-complete-graph-remainder-through-same-sign-density-compression.md) bounds the integrated complex velocity derivative by $1/16$, so $\|(X_-^{-1})'-1\|_\infty\le e^{1/16}-1<1/15$ on this strip by its variational equation. On the needed image strip the original $H'$ has Wiener norm $<33/32$; its mean is exactly one, so $\|H'-1\|_\infty<1/32$. It follows from multiplication that $|p'-1|<(33/32)(16/15)-1=1/10$ throughout the strip. Under a downward shift of height $h<\sigma$, $\operatorname{Im}p(y-ih)\le-.9h$. The interpolated phase between the two lifts has imaginary part at most $-.9h+E$. Subtract the two exponential kernels **before** taking moduli and integrate along their affine interpolation. Taking $h$ up to $\sigma$ and using $E<.001\sigma$ yields
$$
 |(D-\widehat D)_{j,-n}|
       \le4jE\exp[-(n+.899j)/64].                          \tag{ASQ12.3}
$$
This estimate keeps the small original uniform lift error in front of the entire summation.

For clarity, after multiplication by $4n$, the separable Hilbert–Schmidt bound is $16E$ times the square root of the product of two sums. The input sum $\sum_{n\ge1}n^2e^{-n/32}<66100$ follows from the integral $2\cdot32^3$ and the maximum $4e^{-2}32^2$. Write $a=.899/32$. The full output sum $\sum_{j\ge1}j^2e^{-aj}<91200$ by the same integral-plus-maximum estimate. Its tail from $97$ is below
$$
 e^{-96a}(96^2/a+192/a^2+2/a^3)<45100
$$
by monotonicity past $2/a$; $1/a<35.60$ and $e^{-96a}<.068$ suffice. Consequently the full and high error bounds in (ASQ12.3) are $<.276$ and $<.194$, respectively. Altogether
$$
       \|P_{97}D\|_{\dot H^{-1}\to0}<.288,\qquad
       \|D\|_{\dot H^{-1}\to0}<.431.                        \tag{ASQ12.4}
$$
Each pair of opposite-sign blocks is an orthogonal direct sum. The two-sign norms incur no extra summand.

## Actual right factors and all coordinate terms

Use $v=v_i$, $w=v-\alpha$, $A=Id-\mathcal T_\alpha I$ and $B=Id+\mathcal T_w I$. The full [ASQ10.2–3](R149-supplement-practical-high-cut-with-paid-coordinate-errors.md) bounds give $|\nu|<37$, $\|v\|_{A^0}<1.08$, $\|\alpha\|_{A^0}<1.43$ and $\|w\|_{A^0}<2.51$. Apply the two separate windows of (ASQ12.2) in the actual order. On the smoother term $C^{-1}\mathcal T_\alpha I\bar G P_s$, take the full $L^2$ inverse first and then use the genuine $P_{97}$ output to pass to $\dot H^{-1}$. The other term uses the full $\dot H^{-1}$ inverse. This gives
$$
 \|P_{97}C^{-1}A\bar G P_s\|_{2\to\dot H^{-1}}
 <1.11(32/25)(1+1.43/388)<1.43 .                           \tag{ASQ12.5}
$$
This projection really is present before $D$ and $S$ in ASQ10.6; no projection has been commuted through a composition. On its range the $H^{-4/3}$ cost is at most $388^{-1/3}$ times the $\dot H^{-1}$ cost. ASQ10.5 bounds the subsequent $S$ on $H^{-4/3}$ by $1.1$. The last term in ASQ10.6 therefore costs less than $(11/50)H_{\rm phys}$, using $P_s=P_sP_{97}$ on output.

From $\|v'''\|_2<12044$ and the two-sign Cauchy–Schwarz sum,
$$
 \|P_{\ge L}v\|_{A^0}\le12044
      \sqrt{2/(5\cdot4^6(L-1)^5)} .
$$
It is below $.008$ at $L=49$ and below $.00024$ at $L=194$. The true $T_i=Id+(\nu+v)I$ satisfies, by splitting its output before multiplication by $v$ at frequency $48$,
$$
 \|P_{97}Q_aT_iD\|_{\dot H^{-1}\to0}
 <(1+37/388)(.288)+(1.08/192)(.431)+.008(.08)<.32 .
$$
Here the low part uses $\|ID\|_{\dot H^{-1}\to0}=\|D\|_{\dot H^{-1}\to\dot H^{-1}}<.08$, and the high output of the $\nu$ term uses (ASQ12.4). Both reflections in $Q_a$ preserve frequency moduli. By (ASQ12.5) this whole term costs $<.32(1.43)$.

The finite reference correction $(M_\nu-\bar M)\bar G P_s$ vanishes on its genuine high input. The $B-Id$ cost is $<2.51/388$. For the sign commutator in WDH.15 the two opposite signs force a separation of at least 194; its one-half commutator factor absorbs the two signs in the symbol difference. Its cost is $<.00024(32/25)$. The remaining three terms are bounded directly in their original order
$$
 -M_v I\mathcal T_\alpha I\bar G,\qquad
 -\nu I\mathcal T_\alpha I\bar G,\qquad
 -\nu\mathcal T_w I^2\bar G .
$$
Use $P_s$ on both sides. The respective upper bounds are
$$
 \left({1.08\over192}+{.008\over4}\right)1.43\,{32\over25},\qquad
 {37\over388}1.43\,{32\over25},\qquad
 37(2.51){.573\over388}.
$$
The first splits the primitive immediately before $M_v$ at $48$ and keeps its low-to-high crossing. The last pays the **whole** original $I^2\bar G P_s$ from ASQ11.7. All these estimates include both ordinary physical Fourier signs.

The sum of the displayed nonphysical costs, including $.32(1.43)$, is strictly below $4/5$. This proves (ASQ12.1) without an assumed finite Galerkin inverse.

## The finite physical square

Write $Q_s=Id-P_s$ and let $L$ denote the full transformed waist operator in ASQ10.6, $b=Bf+Us$ its complete affine waist datum, and $X_*=BX$, $m_*=Bg_{\rm met}$. Under (ASQ12.1)'s physical norm test set $H=(P_s L|_{P_sY})^{-1}$. Then
$$
 p=H P_s(b-Lq-X_*c-m_*k),\qquad q=Q_s w_0,\qquad w_0=q+p .
$$
The actual finite waist row uses $Q_s(L(q+p)+X_*c+m_*k)=Q_s b$. The unaltered $\Theta$, both original means, the full weighted raw phase and same-world height rows use this same $q+p$, $c$, $k$ and complete exterior particular. The trial tail fees are those for the real $P_s X_*$; its first retained frequency may be 97, so no cutoff-65536 tail estimate has been substituted. The inversions and cancellations above concern the genuine simultaneous $P_s$ block only. The smaller finite complement and its physical border still require their own signed entries and inverse.
