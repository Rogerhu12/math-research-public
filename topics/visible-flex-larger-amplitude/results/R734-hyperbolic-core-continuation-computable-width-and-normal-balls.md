# R734 — Exact hyperbolic continuation from the Fejér core, a computable width, and internal normal balls

2026-11-28. **Proved.** On any fixed radial interval where $a>0$ and $a''>0$, we reduce the same-metric immersion from R733's genuine core to a real, diagonally transported pair. Multiplying angular gradients by the positive sum of the two fields cancels both gradient products. Consequently a bounded positive rectangle for the values suffices to continue a complete smooth angular solution: no independent gradient-smallness condition is needed. We give explicit scalar comparison envelopes, a positive first-cell width calculated from the exact first two knots, and two-sided radius-$.16$ inequalities for every pair in that entire computable two-sided strip. Longer continuation still depends on the actual fixed scalar and the field; no new run or whole closed-surface certificate is claimed.

## 1. Orthonormal shape coefficients and real transport

Use $\theta=\Theta(\varphi)$, $\gamma_\theta=t$, $t_\theta=-n/\rho$ as in R717 and R733. Let $a=a_{\rm deep}$ and, on one or more of its true quintic cells with $a>0,\ a''>0$, set
$$
 k=\sqrt{a''/a},\qquad c=a'/a,\qquad A=k'/(2k)
          =\tfrac14(a'''/a''-a'/a).
$$
At a knot $a,a',a''$ are continuous; $A$ can have unequal finite one-sided values. All equations using $A$ are read on each open cell, with continuous unknowns at their common ends. On the actual core $a=1,\ a'=0,\ k^2=k_0>0$.

In the oriented orthonormal material frame $(E,T)=(F_s,F_\theta/a)$, $N=T\times E$, write the second form as $\left(\begin{smallmatrix}L&M\\M&P\end{smallmatrix}\right)$. The Gauss equation is $LP-M^2=-k^2$. The Codazzi equations, using $\nabla_EE=\nabla_ET=0,\ \nabla_TE=cT,\ \nabla_TT=-cE$, are
$$
 P_s=M_\theta/a+c(L-P),\qquad M_s=L_\theta/a-2cM.
 \tag{1}
$$
The core has $P=-1/\rho,\ M=0,\ L=k_0\rho$. Set
$$
 (M+k)/P=-kU,\qquad (M-k)/P=kV .
$$
Initially $U=V=\rho$. Conversely, on $U,V>0$ put
$$
 P=-\frac2{U+V},\qquad M=\frac{k(U-V)}{U+V},\qquad
 L=\frac{2k^2UV}{U+V}.
 \tag{2}
$$
These satisfy Gauss identically. Define
$$
 D_-=\partial_s-(kV/a)\partial_\theta,\qquad
 D_+=\partial_s+(kU/a)\partial_\theta,\qquad
 f(u,v)=cv(1+k^2u^2)+A(v-u).
$$
Then (1) is equivalent to
$$
 D_-U=f(U,V),\qquad D_+V=f(V,U).
 \tag{3}
$$
For an algebra check let $w=(M+k)/P$, $z=(M-k)/P$, so $L=Pwz$. In the quotient equation for $w_s$, the angular term $(L_\theta-wM_\theta)/P$ equals $z w_\theta$. The remaining terms are $-cz(1+w^2)+k'/P$. The $z$ equation exchanges the variables and reverses the sign of $k'/P$. Substitute $w=-kU$, $z=kV$ and divide out $k$ to obtain (3). The substitutions are pointwise invertible in the stated rectangle.

## 2. A value rectangle continues the full angular solution

Put $B=U+V$, $G=B U_\theta$, $J=B V_\theta$. On a smooth cell differentiate (3) in $\theta$. The first differentiated equation contains $+(k/a)V_\theta U_\theta$, while
$$
 D_-B=f(U,V)+f(V,U)-(k/a) B V_\theta .
$$
The products cancel in the equation for $G$. In the second equation the derivative of its positive characteristic speed gives the opposite sign, cancelled by $+(k/a) B U_\theta$ in $D_+B$. Precisely, with $H=f(U,V)+f(V,U)$,
$$
 \begin{aligned}
 D_-G&=[f_1(U,V)+H/B]G+f_2(U,V)J,\\
 D_+J&=[f_1(V,U)+H/B]J+f_2(V,U)G .
 \end{aligned}
 \tag{4}
$$
Here suffixes $1,2$ denote ordinary derivatives in the corresponding field value; the displayed $s$-dependent scalar coefficients are fixed. Thus if $0<m\le U,V\le B_+<\infty$ and $a,k$ are bounded above and below away from zero on a finite interval of finitely many cells, the absolute row sums of (4) have a finite, piecewise bounded majorant $C(s)$. Along both characteristic families Grönwall gives
$$
 \max(\|G(s)\|_\infty,\|J(s)\|_\infty)
 \le\max(\|G(0)\|_\infty,\|J(0)\|_\infty)\exp\!\int_0^s C(r)\,dr .
$$
In particular the first angular derivatives are bounded because $B\ge2m$.

For clarity about continuation, start with the local classical solution of the diagonal first-order system, obtained by the method of characteristics (at the analytic actual core R733 also gives it directly). On each smooth time cell the usual construction iterates the scalar characteristic ODEs with frozen previous fields and integrates both source terms. Bounded spatial first derivatives make the characteristic maps locally bi-Lipschitz, with their derivatives given by the exponential of the integrated speed gradient. One may justify restart with smooth data directly: differentiating (3) $j$ times in angle for $j\ge2$ gives a linear transported system in the two derivatives of order $j$, with coefficients bounded by the first derivative bound and forcing bounded by the lower-order derivatives. The only term where $j$ derivatives hit a speed is its order-$j$ field derivative times the already bounded first derivative. Induction and Grönwall therefore bound every finite angular order on a compact radial subinterval where the rectangle holds. Equation (3) then bounds radial derivatives of each angular order from one side. At a putative first finite stopping point all spatial derivatives have smooth periodic limits and the ordinary local characteristic theorem restarts the solution. At a fixed scalar knot use the smooth right-hand polynomial coefficients for this restart. There is no spatial boundary on the circle and uniqueness gives periodicity. This proves continuation on every such compact rectangle interval; a bound containing zero, a zero of $k$, and an unbounded interval are not covered.

## 3. Reconstruct one global periodic isometric immersion, and its curvature

For each $\theta$ integrate in $s$ the actual frame and position
$$
 E_s=L N,\quad T_s=M N,\quad N_s=-L E-MT,\quad F_s=E,\qquad
 (E,T,N,F)(0)=(e_z,t,n,\gamma).
 \tag{5}
$$
The coefficient matrix is skew, hence the frame remains orthonormal with the prescribed orientation. To see that this yields the required angular derivative and no hidden closing period, the angular frame equations are
$$
 E_\theta=a'T+aMN,\qquad T_\theta=-a'E+aPN,\qquad
 N_\theta=-aME-aPT .
 \tag{6}
$$
They hold on the core. With the frame as a column matrix $O$ write (5),(6) as $O_s=OC_s$, $O_\theta=OC_\theta$, where subscripts on $C$ identify the coordinate's skew matrix. The zero-curvature identity
$$
 \partial_\theta C_s-\partial_s C_\theta+C_\theta C_s-C_s C_\theta=0
$$
is exactly (1) and $LP-M^2=-a''/a$ (for example the $E,T$ component is $a''+a(LP-M^2)$). Therefore the residual $O_\theta-OC_\theta$ satisfies the homogeneous radial equation with right multiplier $C_s$ and initial zero, proving (6). Now $(F_\theta-aT)_s=E_\theta-a'T-aMN=0$. The initial value is zero and all frame ODEs have periodic coefficients and periodic initial data. Hence $F_\theta=aT$ globally on the circle, $|F_s|=1$, $F_s\cdot F_\theta=0$ and $|F_\theta|=a$. No unknown translation or angular monodromy was discarded. At a finite $C^2$ knot, (2),(5),(6) and $a,a',a''$ have continuous traces, so $F$ is $C^2$ across it. The two-sided reflected strip uses the core jets of R733. Equations (2),(5) determine the same local core immersion by uniqueness in (3), or by analytic uniqueness at the first cell.

For $m\le U,V\le B_+$ the trace of (2) is $2(k^2UV-1)/(U+V)$, strictly increasing in both entries ($\partial_U$ gives $2(k^2V^2+1)/(U+V)^2$). The product of the eigenvalues is fixed at $-k^2$. At fixed product both signed eigenvalues are increasing functions of the trace. At the two scalar endpoints their pairs are $(k^2m,-1/m)$ and $(k^2 B_+,-1/B_+)$. Thus
$$
 \|{\rm II}\|_{\rm op}\le \max(k^2 B_+,1/m)
 \tag{7}
$$
in the actual metric. This statement controls curvature and immersion throughout a rectangle; embeddedness and mixed-sheet normal balls are separate assertions.

## 4. Scalar envelopes on the true fixed cells

The cross derivative is $f_2(u,v)=c(1+k^2u^2)+A$. In particular
$$
 a'\ge0,\qquad a a'''+3a'a''\ge0
 \tag{8}
$$
on a positive hyperbolic interval suffice for $f_2\ge0$. In this case compare with the two equal-state ordinary solutions $y'=c y(1+k^2 y^2)$ from scalar initial values $r_-,r_+$ bounding every angular $\rho$. Both components stay between those solutions. One proof uses barriers offset outward by $\epsilon e^{Cs}$ on a bounded rectangle; at first contact the transport derivative uses the cross monotonicity and the Lipschitz bound on self variation. Increase $C$ above the bounded row sums and let $\epsilon\downarrow0$. This argument applies piecewise at the fixed knots. A direct identity using $a^2k^2=aa''$ gives
$$
 (a^2/y^2)'=-2a'a'',\qquad
 y(s;r)=\frac{a(s)}{\sqrt{r^{-2}-a'(s)^2}}
 \tag{9}
$$
for data starting at the core ($a(0)=1$, $a'(0)=0$). Therefore any compact actual interval from the core obeying (8), $a>0$, $a''>0$, $r_+^2 a'^2<1$ has the explicit positive rectangle $y(s;r_-)\le U,V\le y(s;r_+)$. One can use $r_-=1/4-553\,2^{-53}$ and $r_+=25/4+553\,2^{-53}$. The formula for a later restart substitutes $a(s_0)^2/y(s_0)^2+a'(s_0)^2-a'(s)^2$ under the square root. It is an entire actual surface theorem on the certified interval, not an estimate derived from a single meridian.

Even when (8) fails it does not prove physical blowup. At proposed positive envelopes $m,B_+$ the exact outward rectangle conditions (almost everywhere in $s$) are
$$
 m'\le\min(f(m,m),f(m,B_+)),\qquad
 B_+'\ge\max(f(B_+,m),f(B_+,B_+)).
 \tag{10}
$$
They follow from affineness in the other field at each boundary. The same barrier proof and (4) then continue the isometry with (7). The two ordinary extreme equations with equality provide an alternative recipe while $m>0$ and $B_+$ is finite. No convexity or positive sign of $a'''$ is needed for (10). A zero of $a''$ does require a different chart or a separate continuation argument.

## 5. A strictly positive and computable unconditional first-cell width

Let $w>0$ be the first physical knot width and $c_0,\ldots,c_5$ the **six exact FullHold coefficients** in the variable $s/w$ after replacing the core jet by the actual dyadic initial law. For clarity, from endpoint jets $(a_i,v_i,k_i)$ put $c_0=a_0,\ c_1=w v_0,\ c_2=w^2k_0/2$; define $A_0=a_1-c_0-c_1-c_2$, $A_1=w v_1-c_1-2c_2$, $A_2=w^2k_1-2c_2$. The three remaining coefficients are $10A_0-4A_1+A_2/2$, $-15A_0+7A_1-A_2$, $6A_0-3A_1+A_2/2$. These are precisely the original first-cell construction, not the ideal initial-law polynomial between the saved knots. Define the following positive *rational* using these inputs only:
$$
 B_3=w^{-3}\sum_{j=3}^5 j(j-1)(j-2)|c_j|,\qquad
 T_*=\min\!\left(w,\frac1{200},\frac{k_0}{2(1+B_3)},
                  \frac1{25(4+7 B_3/(2k_0))}\right).
 \tag{11}
$$
This is a fixed recipe, in contrast to an unspecified existential analytic width. Its numerical evaluation on the complete prepared input has not been executed in this work.

On $0\le s\le T_*$, $|a'''|\le B_3$ and consequently $k_0/2\le a''\le3k_0/2<3/8$, $1\le a<1.001$, $0\le c<.02$, $k^2<3/8$. Also $|A|\le B_3/(2k_0)+.005$. On the fixed positive rectangle $[.2,7]^2$ both sources in (3) have absolute value at most
$$
 .02\cdot7(1+(3/8)49)+7[B_3/(2k_0)+.005]<4+7B_3/(2k_0).
$$
Initial $\rho$ lies in $(.249,6.251)$ by R717. Along any characteristic the drift before first exit is bounded by $1/25=.04$, strictly smaller than the two available margins. Thus it cannot exit that rectangle on (11), with no cooperativity assumption. Sections 2–3 give a full periodic exact isometric immersion there and $\|{\rm II}\|_{\rm op}\le5$. These formulas are directly computable on the public runner from the original first knot and its two endpoint jets; no angular Fourier truncation or normal-stage solve enters the width.

## 6. Embeddedness and quantitative two-sided normal balls on this actual strip

Reflect across the core and consider $|s|\le T_*$. Let $C(s,\theta)=(\gamma(\theta),s)$ be the unit coordinate cylinder. The meridian and circumferential unit tangents and the unit normal of $F$ differ from $e_z,t,n$ respectively by at most $5|s|$ because (5) and (7) bound each radial derivative by 5 (for the normal use the Euclidean norm of the first shape-matrix column). Thus
$$
 |F-C|\le(5/2)s^2,\qquad |N-n|\le.025,\qquad
 \|DF-DC\|_{\rm op}<.04 .
 \tag{12}
$$
For the last inequality the column errors are bounded by $.025$ and $.001+1.001(.025)$, using $F_\theta=aT$. These estimates extend to the reflected coordinates with matching orientation. A material straight segment in unwrapped angle has intrinsic length at most $1.001$ times its Euclidean parameter length.

Take an ordered pair with circular material angle separation $\Delta\theta\le.1$. Write $v$ for the signed parameter difference. On the interval of shorter material angles, core tangent turns by at most $4.01$ per unit angle and thus lies within $.2005$ of the tangent at the midpoint. The planar cylinder chord has component along that middle tangent at least $\cos(.2005)|\Delta\theta|>.97|\Delta\theta|$, with independent vertical component $\Delta s$. Hence its 3D length is at least $.97|v|$. Integration of the last inequality of (12) along the straight segment gives $|F(q)-F(p)|\ge .93|v|$. This also proves injectivity for such distinct parameters. For a unit-speed path in the surface of intrinsic length $\ell$, the normal changes by at most $5$ times the arclength elapsed. Its tangent is orthogonal to its **current** normal, so integrating against the initial normal bounds the absolute normal chord by $(5/2)\ell^2$. Apply this to the straight parameter segment, parametrized by intrinsic arclength. It gives
$$
 \frac{2|N_p\cdot(F(q)-F(p))|}{|F(q)-F(p)|^2}
 \le5(1.001/.93)^2<1/.16 .
$$

For a larger material separation the limiting cylinder chord $D_0$ has length at least $.07$. To check the planar bound, use the shorter *normal-angle* arc of size $\delta\in[0,\pi]$ between the two core points. Its material arclength is at least the shorter material arclength, here $>.1$. If $\delta\le\pi/2$, its projection on the middle tangent is at least $\cos(\pi/4)(.1)>.07$. Otherwise the same projection, integrating $\rho t\,d\varphi$, is at least $2\inf\rho\,\sin(\delta/2)>.07$. Vertical separation can only increase $D_0$. By (12) the full chord differs by at most $5T_*^2\le.000125$ and has length at least $.998D_0>0$. R733 §3 proved the two-sided radius-$.2$ inequalities on that complete cylinder. Its base normal differs from the actual base normal by at most $.025$. Using (12) once more,
$$
 \frac{2|N_p\cdot(F(q)-F(p))|}{|F(q)-F(p)|^2}
 \le\frac{5+.05/.07+.00025/.07^2}{.998^2}<1/.16 .
$$
This completes embeddedness and the two-sided radius-$.16$ inequalities for all ordered pairs in the entire computable strip, including pairs on different sides of the core. It does not assert the reach of a free-boundary patch or the distance to arbitrary added remote points. R733's separately proved whole-surface graft and mixed-pair conclusions use its own permitted cutoff widths; their width is not silently replaced by (11).

For a longer hyperbolic input interval satisfying §4, (3)–(9) continue the exact same material immersion; global embeddedness/remote pairs on that larger interval still need their own estimates. An actual scalar-only public readout can test (8) and $r_+^2a'^2<1$ by exact polynomial signs on all requested physical cells and return the genuine certified prefix along with the first unresolved interval. Neither a failed sufficient test nor a finite prefix demonstrates nonexistence. Passing through the later sign-changing and cap regions, solving the two-end same-metric problem, full-family reach and refinement remain outstanding.
