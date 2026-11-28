# R768. Non-even velocity polarizations preserving the complete R767 endpoint map

Use exactly the closed R767 material sphere, fixed initial pullback, central moving curve and two rigidly translated exterior components. In its notation $p$ is even and $b(u)=\sin(2\pi P(u))$ is odd under $u\mapsto1-u$. The values $\beta=|b_h|$ and $\gamma>0$ are the two genuine bridge moment controls determined by the physical phase and label $s$. They do not depend on the new free fields. Let $J$ denote a positive quarter turn in the profile plane. The pointwise velocity always has the form
$$
 V(u)=R_{b_h}(p(u))[\cos(\gamma b(u))e_y+\sin(\gamma b(u))N(u)].
$$
The source integrates this actual unit vector. The aim is to allow different polarizations on the paired material levels, while preserving the genuine integrated endpoint vector through every label and phase.

Choose an even nonnegative $C^2$ envelope $\Omega$ supported in $[.02,.235]\cup[.765,.98]$, strictly positive on the interiors of these two intervals. The source rises/falls with the $S_7$ cutoff over width $.035$. Let $N_e(s,u,t)$ be any even unit horizontal direction. On $\{\Omega\ne0\}$ take $N_e=N_*(s,t)$ independent of $u$; it is still freely variable in the longitudinal material coordinate and phase. Away from this support it may also vary in $u$, with a smooth transition. At $t=0$ take $N_e=-n_0$. Put
$$
 \tau_0=1,\qquad \tau_1=p\,\operatorname{sinc}(\beta p),\qquad
 \tau_2=p^2\,\operatorname{cosc}(\beta p),\qquad
 \operatorname{sinc}x=\frac{\sin x}{x},\quad
 \operatorname{cosc}x=\frac{1-\cos x}{x^2}.
$$
Use their entire values at zero. In particular $\tau_1,\tau_2$ limit to $p,p^2/2$. Define the even weight $w=\Omega b^2\operatorname{sinc}(\gamma b)$. It is positive throughout either support interval except for possible isolated zeros of $b$; $\operatorname{sinc}(\gamma b)\ge2/\pi$. Form
$$
 G_{ij}=\int_0^1 w\tau_i\tau_j\,du,\qquad
 c=G^{-1}\int_0^1 w\tau f\,du ,
$$
where $f$ is an arbitrary smooth even scalar material control, vanishing at zero phase. The $3\times3$ matrix is strictly positive definite on the entire compact parameter set. Indeed $p$ varies over an interval on either support component. At $\beta=0$ the three independent polynomials $1,p,p^2/2$ are involved. At $\beta>0$ the span is that of $1,\sin(\beta p),\cos(\beta p)$, which is linearly independent on every nonempty interval of $p$. Positivity of the weight then proves the assertion. By compactness and continuity the least eigenvalue has a positive uniform lower bound. This conclusion requires no choice of a direction $b_h/|b_h|$ at a zero horizontal displacement.

Choose a positive smooth scalar denominator $S(s,t)$ making
$$
 z=\frac{.89\,\Omega b}{S}\,[f-c\cdot\tau]
$$
bounded in absolute value by $.89$. A concrete finite-dimensional choice is $f=\sum_{j=1}^m d_j T_j(2(2u-1)^2-1)$, $S=\sqrt{1+2m\sum_jd_j^2+6|c|^2}$. Indeed $|T_j|\le1$ here, and each $|\tau_i|\le1$. Thus $|f-c\cdot\tau|\le\sqrt{2m\sum d_j^2+6|c|^2}$. The denominator is the same for all transverse levels of a given meridian. The actual physical direction
$$
 N=\sqrt{1-z^2}\,N_e+z\,JN_e
$$
is a smooth horizontal unit vector, generally non-even. Its first summand cancels from the integrated odd term of $V$ just as in R767. For the second summand, $JN_e=JN_*$ on the support. Rotating this fixed vector by $R_{b_h}(p)$ gives components in the span of $1,\tau_1,\tau_2$ as functions of $u$, by Rodrigues' formula with the fixed vector $(b_{h,z},0,-b_{h,x})$. Consequently its total moment is a linear combination of the three integrals
$$
 \int_0^1\sin(\gamma b)\,z\,\tau_i\,du
 =\frac{.89\gamma}{S}\int_0^1 w\,[f-c\cdot\tau]\tau_i\,du=0 .
$$
This proves exact closure for every choice of the longitudinal and temporal coefficients: no target endpoint or cap is refitted. The new term vanishes in positive-width intervals at each endpoint so that the complete R767 seam jets, exact $g_{vv}$, central and exterior tensors, full original reach and positive-phase held/support witness carry over. The genuine three-dimensional thickness of the moving bridges, their two unresolved metric rows and the rigid quotient still have to be established.

The freedom affects a physically constrained quantity that all even polarizations leave fixed. For any even choice the chord from level $u$ to $1-u$ on the same meridian equals the integral of the drift term alone, because the odd term cancels over that symmetric subinterval. For the new family its difference has derivative proportional to $R_{b_h}(p)JN_*\sin(\gamma b)z$ wherever this quantity is nonzero (the endpoint contributions add). The derivative of the symmetric chord uses $-V(u)-V(1-u)$, so a nonzero value changes some actual chord. A nontrivial such $z$ exists: the weighted span removed has dimension three whereas arbitrary even polynomials on the open support have unbounded dimension. Already any collection of four linearly independent restrictions has a nonzero residual for at least one member. At positive phase this can be used on either side independently; compact smooth longitudinal controls may localize it in that label. The uniform matrix inverse and the entire formulas at $\beta=0$ permit differentiation through both material variables before integration. These arguments pertain to the exact integral definitions; the supplied working source treats their numerical quadrature, actual phase residuals and material continuity independently.

## Endpoint mixed row of the two symmetric-edge classes

Write $b_h$ horizontally in world coordinates, with $R_{b_h}(p)e_y=e_y+p b_h+O(p^2)$. Near zero the derivative defining $P$ gives $P(u)=C u^4+O(u^5)$ with $C=5/[2(.94)(.06)^3]>0$. Thus $p(u)=P(4u)=256C u^4+O(u^5)$ and $b(u)=2\pi C u^4+O(u^5)$. At $1-u$ the first has the same sign and the second the opposite. On the right head, $q_t=q_0$, $T_t=T_0=T$, and the two original edge tangents $F_s$ are both $T$. Inwards from either edge they are $T+O(u^5)$, since the endpoint displacement is the integral of $V$ and $\partial_s V=O(u^4)$ (the smooth material data are fixed). Reflections in the axial coordinate do not affect the mixed metric. On the positive side the coefficient of $u^4$ in the two expansions of $F_s\cdot V$ is
$$
 C T\cdot(256 b_h+2\pi\gamma N_*)\quad\hbox{and}\quad
 C T\cdot(256 b_h-2\pi\gamma N_*).
$$
Here $N_*=N_e(s,0,t)=N_e(s,1,t)$, because the odd part vanishes on both actual edge neighborhoods. The prescribed initial mixed coefficient is zero at every level. Adding the two equalities necessary for exact isometry gives $T\cdot b_h=0$. Throughout the right head $h=-\Delta J/2$ and $b_h$ is one constant multiple of $h$ with a strictly positive factor, by the R767 horizontal mean. At the last phase $\Delta J_z>.55$. The head tangent sweeps a genuine angular interval of length $>\pi$ and so cannot be everywhere orthogonal to this one nonzero vector. This excludes an exact final metric in both velocity classes. This boundary argument alone gives no universal discretized residual size as controls increase.

## A full fixed-boundary diagonal obstruction, independent of velocity parametrization

A stronger necessary condition fails already for an explicit material point pair in a single positive bridge at the last phase. Use the R767 right head with radius $r=.23$. Its true tangent angle decreases from $.88$ to $-\pi-.08$. Each speed ramp uses an angle at most $.001/.23$, so the two stations $s_1<s_2$ with tangent angles $-\pi/2+.85$ and $-\pi/2-.85$ are in the same exact constant-curvature arc. Their arclength difference is $a=2r(.85)=.391$ and their true profile chord is $(0,-2r\sin(.85))$ in the world profile $(x,z)$ plane, by integrating the circular tangent over the symmetric interval. Take the material points $(s_1,0),(s_2,L)$, $L=.66$. In the fixed $g_0$ the diagonal $s=s_1+(s_2-s_1)v/L$, $0\le v\le L$, has length at most
$$
 d_* = \sqrt{L^2+a^2}<.768.
$$
Indeed its metric is $dv^2+(1-d_0(v)/r)^2ds^2$, and $0\le d_0\le L\sin(.02)<r$. Nonnegativity follows because the initial $\sin(.02 b)$ is nonnegative on the first half and changes sign under reflection, with zero full integral. This estimates the length of an actual material path; it does not require finding a shortest geodesic.

At the last phase the first point is fixed. The second point belongs to the rigid exterior with horizontal translation $-\Delta J/2$ and axial distance $P_0-.18$ from the first. R767 gives $\Delta J_z>.55$, and $P_0\ge .66\cos(.02)>.65986$. Dropping the squared world $x$ component leaves
$$
 |F_{\pi/2}(s_2,L)-F_{\pi/2}(s_1,0)|^2
 \ge [2r\sin(.85)+\Delta J_z/2]^2+(P_0-.18)^2
 >(.345+.275)^2+.47986^2>.784^2.
$$
For the elementary sine bound one may use the alternating expansion through $-.85^7/7!$. It follows that every map with these two endpoint positions and $F^*e\preceq(1+\varepsilon)g_0$ must have $\varepsilon>(.784/.768)^2-1>.042$. In particular this applies to unrestricted interiors and changes of material gauge fixing the two labels. Any modified endpoint positions within $d$ of their specified values at each end still require $.784-2d\le\sqrt{1+\varepsilon}\,.768$. One must change the actual boundary motion (or change the initial metric) to continue toward the target tolerance. The original pulse, non-even moment result, certified initial reach, fixed grip and held witness retain their stated scope.
