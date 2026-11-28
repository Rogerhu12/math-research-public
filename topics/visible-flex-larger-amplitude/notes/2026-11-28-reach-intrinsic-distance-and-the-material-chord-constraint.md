# A reach bound for material chords on a nearly isometric closed surface

Let \(F_0:M\to\mathbb R^3\) be the reference embedding, \(g_0=F_0^*e\), and let \(F\) be a \(C^2\) embedding of the same closed material surface. If \(F^*e\geq(1-\varepsilon)g_0\) and its image has reach at least \(r>0\), every material pair \(p,q\) satisfies
\[
 |F(p)-F(q)|\ \geq\ 2r\,\sin\!\left(\min\!\left\{\frac{\pi}{2},
 \frac{\sqrt{1-\varepsilon}\,|F_0(p)-F_0(q)|}{2r}\right\}\right).
 \tag{1}
\]
Here \(0\leq\varepsilon<1\). The reference chord and the same fixed radius apply at every phase. This is a necessary condition. Its finite evaluations do not establish reach, relative metric accuracy, or injectivity.

## A sharp upper bound for intrinsic distance

Write \(S=F(M)\). For \(A,B\in S\) with \(d=|A-B|<2r\), let \(m=(A+B)/2\) and \(P\) its nearest point on \(S\). It is unique since \(s=|m-P|\leq d/2<r\). For \(s>0\) let \(n=(m-P)/s\). The tangent ball of any radius \(r'<r\) in direction \(n\) is empty of \(S\) in its interior. Expanding this ball inequality at \(A,B\), letting \(r'\uparrow r\), and averaging gives
\[
 2rs\leq s^2+d^2/4,\qquad
 s\leq s_*(d):=r-\sqrt{r^2-d^2/4}.
\]
The last inequality also holds when \(s=0\).

Put \(d_1=|A-P|\), \(d_2=|P-B|\). The parallelogram identity gives \(d_1^2+d_2^2=d^2/2+2s^2\leq4rs_*(d)<4r^2\). For \(f(u)=\arcsin(\sqrt u/(2r))\), one has \(f'(u)=1/(2\sqrt{u(4r^2-u)})\). If \(0<u\leq v\) and \(u+v\leq4r^2\), then \(u(4r^2-u)\leq v(4r^2-v)\). Consequently at fixed sum \(u+v\) the maximum of \(f(u)+f(v)\) occurs at \(u=v\), including endpoints by continuity. Thus
\[
 \arcsin(d_1/(2r))+\arcsin(d_2/(2r))
 \leq2\arcsin\left(\frac{\sqrt{d^2/4+s_*(d)^2}}{2r}\right)
 =\arcsin(d/(2r)).
\]
The identity follows by setting \(d=2r\sin\alpha\), \(0\leq\alpha<\pi/2\).

Replace the segment \(AB\) with \(AP,PB\), and repeat this operation on every resulting segment. Each child of a parent of length \(b>0\) has length at most \(b/2+s_*(b)\). The ratio
\[
 \frac12+\frac{s_*(b)}b=\frac12+\frac{b}{4(r+\sqrt{r^2-b^2/4})}
\]
is increasing and is strictly below one at \(b=d<2r\). The largest segment length therefore tends to zero geometrically. The preceding angle inequality bounds the sum of the lengths of every polygonal path by \(2r\arcsin(d/(2r))\), since \(b\leq 2r\arcsin(b/(2r))\) on each edge. The paths with constant-speed parametrization on \([0,1]\) have a common Lipschitz bound. Take a uniformly convergent subsequence. Every point of each polygon lies within its largest edge length of \(S\), since all vertices lie on \(S\). The limiting path lies on closed \(S\), joins \(A,B\), and has length at most the stated common bound. This proves
\[
 d_S(A,B)\leq2r\arcsin(d/(2r)).
\]
A circular arc of radius \(r\) has the chord and intrinsic distance in this formula as equalities.

## The fixed initial metric and its sampled constraint

Because \(F\) is an embedding, paths on its image lift to material paths. Hence \(d_S(F(p),F(q))\geq\sqrt{1-\varepsilon}\,d_{g_0}(p,q)\geq\sqrt{1-\varepsilon}\,|F_0(p)-F_0(q)|\). Combining with the previous bound gives (1) when the current chord is shorter than \(2r\); in particular such a chord is impossible when the material lower bound reaches \(\pi r\). At current chord lengths at least \(2r\), (1) holds automatically.

For Run 51 take \(r=.03\,\operatorname{diam}F_0(M)\) and \(\varepsilon=10^{-6}\). For a sampled pair let \(C_{ij}\) denote the fixed right side of (1), \(P_i,P_j\) the current spatial positions, and \(E_{ij}=(C_{ij}^2-|P_i-P_j|^2)/(4r^2)\). Positive \(E_{ij}\) records a violation, with differential
\[
 dE_{ij}=-(P_i-P_j)\cdot(dP_i-dP_j)/(2r^2).
\]
The search can enumerate just the current pairs of distance at most \(2r\); all remaining pairs satisfy the necessary condition. The Run 51 source enumerates that neighborhood on the full current training point set, counts its positive violations and applies the largest 160 to the objective using their position derivatives. The continuous statement uses every pair on the surface. Its numerical implementation uses the actual fixed-metric reference and current sample positions, ordinary floating-point arithmetic and a finite grid.
