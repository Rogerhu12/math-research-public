# R760 — The original R758 cap metric exceeds the intrinsic curvature budget

2026-11-28. This calculation uses the published original R758 time-zero field. It holds independently of any optimizer, grid, phase interpolation or change in the second fundamental form.

In the positive cap take the material right equator $s=P/2$ and $\rho=.84$. This lies strictly inside the homothetic-ellipse interval $.82<\rho<.87$. In a physical neighborhood about $z=0$, write $X=x-c_x$, $\lambda=\rho/.82$, $A=.494$, $B=.22$, $e=.49$ and $a=A-e=.004$. The positive root of
$$
 (X+e\lambda)^2/A^2+z^2/B^2=\lambda^2
$$
is the *physical* homothety parameter. At the right tip $X=a\lambda$, hence $\lambda_x=1/a$, $\lambda_{xx}=\lambda_z=\lambda_{xz}=0$ and $\lambda_{zz}=A/(a\lambda B^2)$. The material angular interpolation changes no graph values here: the outer height is constant throughout the open equatorial right-wall sector, and all the ellipses in this interval are complete physical plane ellipses. The total transverse ordinate, up to a constant, is exactly
$$
 H=b+S_7(t)(h-b),\qquad t=(\rho-.82)/.16,\quad
 b=.040[(X+e)^2+z^2],\quad
 h=\int_0^{.0075}\sin\beta(u)\,du,\quad 0\le h\le .0075(.014).
$$
At this point $t=1/8$, $t_x=1281.25$, $t_{zz}>12000$, $t_{xx}=t_z=t_{xz}=0$. Moreover $.0095<b-h<.010$, $0<b_x<.04$, $b_{xx}=b_{zz}=.08$, $b_z=b_{xz}=0$. Since $S_7'=140t^3(1-t)^3$ and $S_7''=420t^2(1-t)^2(1-2t)$, we have $.18<S'_7(1/8)<.19$, $S''_7(1/8)>3.7$. Differentiating the physical graph gives $H_z=H_{xz}=0$, $|H_x|<2.5$, and
$$
 H_{xx}=.08(1-S_7)-2b_x S'_7t_x+(h-b)S''_7t_x^2<-57000,\qquad
 H_{zz}=.08(1-S_7)+(h-b)S'_7t_{zz}<-20 .
$$
Therefore
$$
 K_{g_{758}}=\frac{H_{xx}H_{zz}}{(1+H_x^2)^2}>21000 .
$$
This is the intrinsic Gaussian curvature of the specified original metric at a regular physical point. Every $C^2$ isometric embedding has the same Gaussian curvature there by the Gauss equation. An embedded surface of reach at least $r$ has both absolute principal curvatures at most $1/r$, hence $|K|\le1/r^2$. The original R758 diameter is at least 1.40 from its fixed grip, so the requested $.03D$ would be at least .042. Its reciprocal square is below 567. This rules out the desired thickness on this particular metric even if both full ends and the entire original initial immersion are allowed to vary while retaining that diameter scale. The unchanged R758 four physical search jobs still measure their full original fields and return their original finite costs. The obstruction is a physical graph-Hessian value in the time-zero cap, rather than a conditioning statement about its polar labels.
