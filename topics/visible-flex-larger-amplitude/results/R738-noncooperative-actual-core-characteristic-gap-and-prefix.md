# R738 — Noncooperative, angle-sensitive continuation of the actual fixed-metric Fejér core

2026-11-28. **Proved.** On the real R734 Gauss–Codazzi extension the adverse coupling is multiplied by the actual difference of the two characteristic fields. This difference starts at zero on the whole noncircular core. We derive its transport-free integral identity and a closed positive-rectangle comparison with a quadratic initial charge for noncooperativity. It gives a new unconditional rational width from the genuine first six coefficients and an outward step rule on the original piecewise-polynomial input. No whole-field output, cap connection or $.2D$ closed flex follows from a scalar prefix alone.

## 1. Difference identity on the actual circle

Use [R734](R734-hyperbolic-core-continuation-computable-width-and-normal-balls.md), equations (2)–(7), with its actual fixed material arclength angle $\theta$ and the R717 dyadic support core. On one physical cell let
$$
 K=a''/a>0,\quad k=\sqrt K,\quad c=a'/a\ge0,\quad
 A=k'/(2k)=K'/(4K),\quad A_-=\max(0,-A).
$$
The coefficient $a$ is positive. Use the original FullHold $C^2$ scalar at its knots, not a fit to the initial law between them. R734 obtains the periodic fields from
$$
 D_-U=f(U,V),\quad D_+V=f(V,U),\quad
 D_-=\partial_s-(k/a)V\partial_\theta,\quad D_+=\partial_s+(k/a)U\partial_\theta,
 \qquad f(u,v)=cv(1+Ku^2)+A(v-u).
$$
The initial data are $U(0,\theta)=V(0,\theta)=\rho(\theta)$. Write $B=U+V$, $W=U-V$, $G=BU_\theta$, $J=BV_\theta$. Subtract the equations at *the same material angle*. The advection terms combine into $(k/a)\partial_\theta(UV)$, and the source difference is $(-c+cKUV-2A)W$. Since $(ka)'/(ka)=2A+c$, we get the exact identity
$$
 \partial_s(kaW)-cKUV(kaW)=K\,\partial_\theta(UV),\qquad (kaW)(0,\theta)=0.    \tag{1}
$$
There is no angular derivative of $W$ on the left. This identity is valid within each open polynomial cell and integrates across each fixed knot using the continuous values of all its undifferentiated physical fields.

Fix a candidate $0<m_*<M_*$. While both fields lie in this rectangle,
$|\partial_\theta(UV)|\le\max(|G|,|J|)$, by writing the derivative as $(VG+UJ)/(U+V)$. R734's differentiated system for $G$ has diagonal coefficient $[f(U,V)+f(V,U)]/B+f_1(U,V)=c(1+3KUV)-A$ and off-diagonal coefficient $c(1+KU^2)+A$; exchange the fields for $J$. Along a characteristic the derivative of an absolute value is bounded by its signed diagonal times that same absolute value plus the absolute off-diagonal times the other. At a point attaining the maximal component magnitude the resulting row sum is bounded by
$$
 L_1=c(2+4M_*^2K)+2A_- .
$$
Indeed $-A+|d+A|\le d+2A_-$ for $d\ge0$. The standard max comparison here can be justified by transporting a strict outward barrier on the compact angular circle and passing its offset to zero. The signed diagonal matters; taking its absolute value first would pay large positive $A$ needlessly. Define $Y=\max_\theta\{|G|,|J|\}$, $T=\max_\theta|kaW|$. On a time interval starting at $s_0$,
$$
 \begin{split}
 Y(s)&\le Y(s_0)\exp\int_{s_0}^s L_1,\\
 T(s)&\le T(s_0)e^{\int_{s_0}^s L_2}+
       \int_{s_0}^s K(v)Y(v)e^{\int_v^s L_2}\,dv,\qquad L_2=cKM_*^2 .
 \end{split}                                                                  \tag{2}
$$
The second equation follows from (1) by a scalar integrating factor at fixed $\theta$. In particular the leading difference is charged using the angular derivative, even if $A<0$ at the first point.

At a maximum of either original field its partner has at most that value. Its positive-$A$ coupling points inward, while its negative-$A$ coupling is at most $A_-T/(ka)$. At a minimum the analogous lower source bound is $-A_-T/(ka)$ since $cv(1+Ku^2)\ge0$. Characteristics therefore give the following two numerical envelopes from valid starting bounds $m_i,M_i$:
$$
 m(s)\ge m_i-\int_{s_0}^s A_-T/(ka),\quad
 M(s)\le M_i+\int_{s_0}^s [cM_*(1+KM_*^2)+A_-T/(ka)].                        \tag{3}
$$
Here $m,M$ denote the actual extrema over both fields and the complete circle. More explicitly, apply a strict common upper or lower scalar barrier to both components. At first contact the respective component has zero angular derivative, its partner is on the inward side, and the above source bound applies; take the strict offset down to zero. Equations (1)–(3) hold up to a hypothetical first exit. Strict preservation of the rectangle in these estimates excludes the exit. R734's weighted gradient and higher differentiation argument then continues the classical periodic solution, with one-sided coefficient derivatives at the fixed knots.

For the actual [R717](R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) core one may start at
$$
 m_0=1/4-553\,2^{-53},\qquad M_0=25/4+553\,2^{-53},\qquad Y_0=64,\qquad T_0=0 .
$$
In fact $d\theta/d\varphi=\rho$, so the initial absolute weighted gradient is $2|\partial_\varphi\rho|$. For the ideal $\rho=1/4+(3/4)K_7(2\varphi-\pi)$, $|K_7'|\le2\sum_{j=1}^7j(1-j/8)=21$. This gives $2|\rho_\varphi|\le63$. The seven dyadic support coefficients differ by at most $2^{-53}$ each. In $2\rho_\varphi$ the resulting total error is at most $2\sum_{j=1}^7(2j)((2j)^2-1)\,2^{-53}<1$. This proves the initial value without a sample or an angle-grid derivative.

## 2. Outward rational continuation on any checked prefix

For the actual geometry use $m_*=1/5,M_*=7$. Suppose on an entire closed physical leaf of width $h$ we have upper bounds $C\ge c,\ H\ge K,\ E\ge A_-$ and $d>0$ below $ka=\sqrt{aa''}$, with $a,K>0,\ c\ge0$ certified throughout. Distinct one-sided polynomial derivatives are used if a leaf endpoint is an original knot. Given upper bounds $Y_i,T_i$ and extrema bounds $m_i,M_i$ from the last accepted leaf, put
$$
 \begin{split}
 e_1&=C(2+4M_*^2H)+2E,\quad e_2=CHM_*^2,\\
 Y_{i+1}&=Y_i/(1-he_1),\qquad T_{i+1}=(T_i+hH Y_{i+1})/(1-he_2),\\
 V_i&=hE\,T_{i+1}/d,\\
 m_{i+1}&=m_i-V_i,\qquad
 M_{i+1}=M_i+h C M_*(1+H M_*^2)+V_i .
 \end{split}                                                                 \tag{4}
$$
Require $he_j<1$ before division. Since $e^x\le1/(1-x)$ for $0\le x<1$, (2)–(3) justify (4) simultaneously on the whole leaf. When $m_{i+1}>m_*$ and $M_{i+1}<M_*$ the step continues the whole exact solution. Shrinking the leaf or seeking tighter bounds is allowed after an inconclusive step; it is not an assertion of physical breakdown. Lower-bound updates round down and other positive costs round up. No particular subdivision schedule is part of this theorem. The signed root-free expression for $A$ is $(aa'''-a'a'')/(4aa'')$. Rational Bernstein bounds, positive-denominator interval divisions, and a rational $d$ with $d^2\le\inf aa''$ suffice.

At a $C^2$ knot $k,a,U,V$ and their angular derivatives have continuous values. The one-sided restarts in R734 give the matched immersion and frames in $C^2$ and pass the accumulated bounds, with no restarting $T$ at zero. The exact surface has $F_\theta=aT_{\rm frame}$ and $F_s$ unit and orthogonal; $T_{\rm frame}$ is the circumferential unit tangent, distinct from the scalar upper bound $T$. On each accepted leaf R734 gives $\|{\rm II}\|_{\rm op}\le\max(1/m_*,HM_*)$. The same signed-core reflection from R733–R734 continues the other half with matching complete two-jets. A long prefix needs its own embeddedness and global normal-chord estimates.

## 3. A stronger unconditional first-cell formula

Use the six exact FullHold coefficients $c_0,\ldots,c_5$ in $s/w$ and the true first knot width $w>0$ of R734 §5. Set $B_3=w^{-3}\sum_{j=3}^5 j(j-1)(j-2)|c_j|$ and retain the actual positive dyadic $k_0=a''(0)$ of that result. Define
$$
 T_\dagger=\min\left(w,\;1/1000,\; k_0/[2(1+B_3)]\right).                        \tag{5}
$$
We remove R734's linear-in-$|A|$ whole-rectangle charge on this width. Throughout $s\le T_\dagger$, the first three elementary bounds in R734 §5 apply by their own proof from $B_3s\le k_0/2$ and $s\le1/200$: $k_0/2\le a''\le3k_0/2<3/8$, $1\le a<1.001$, $0\le c<.02$, $K<3/8$ and $|A|\le E_*=B_3/(2k_0)+.005$. Also $ka=\sqrt{aa''}>.31$ since the actual $k_0$ is at least $1/5$. For $s\le T_\dagger$,
$$
 sE_*\le1/4+.005/1000<.251,\quad
 s\sup L_1<.51,\quad s\sup L_2<.001 .
$$
For the middle inequality use $.02(2+4\cdot49\cdot3/8)/1000+2(.250005)<.51$. On the rectangle, (2) gives $Y<64/(1-.51)<131$, and, since $T(0)=0$,
$$
 |W(s,\theta)|\le\frac{(3/8)\,131}{.31(1-.001)}\,s<160s .
$$
Thus the total adverse charge in (3) is at most $80 E_*s^2<.021$. The additional upper charge from $cM_*(1+KM_*^2)$ is below $.003$. Neither cost reaches the exit margins $m_0-.2>.049$ and $7-M_0>.749$. This proves (5) without cooperativity. Taking the larger of the two independently proved widths $T_*,T_\dagger$ preserves the full original conclusion. On both widths $s\le.005$, the rectangle, $K\le3/8$, $a$ and metric bounds used in R734 §6 hold, hence its entire two-sided strip is embedded, $\|{\rm II}\|_{\rm op}\le5$, and all its ordered point pairs obey both radius-$.16$ tangent-normal-ball tests. This last conclusion is inherited only on these justified widths or other intervals where the full geometric hypotheses have been verified.

The scale improvement is transparent without evaluating new scientific data. If $f_4=[25(4+7B_3/(2k_0))]^{-1}$ is the last entry of the old minimum, then
$$
 \frac{k_0/(2(1+B_3))}{f_4}
   =\frac{50k_0+(175/4)B_3}{1+B_3}\ge10 .
$$
As $T_*\le f_4$, it follows that $T_\dagger\ge\min(w,1/1000,10T_*)$. The first knot or the new absolute width can still cap the improvement; they must be checked on the actual input. Larger noncooperative prefixes may be certified by (4), with their own output, knots, failed intervals and reach scope. The global angle-dependent endpoint, passage through $K=0$, target caps, whole-family reach and fixed-parameter refinement are not proved by this local continuation.
