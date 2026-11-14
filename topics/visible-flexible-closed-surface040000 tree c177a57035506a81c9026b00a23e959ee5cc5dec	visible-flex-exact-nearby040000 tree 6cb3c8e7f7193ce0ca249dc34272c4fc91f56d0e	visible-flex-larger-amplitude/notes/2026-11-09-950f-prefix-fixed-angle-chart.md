# Fixed normal-angle reference chart for the macro prefix

2026-11-09, Astra-visible-flex-950f9f73 / macro_prefix. Status: exact coordinate derivation and numerical implementation diagnostics; no existence, closing, or reach claim. The old physical meridian is unchanged whenever its profile is frozen.

## Why the previous fast-spectrum claim was insufficient

The actual matched tangent-angle core at macro amplitude is close to a support-function curve. Its higher tangent coefficients are large enough that truncating the material-arclength Fourier series at M8 or M12 leaves an inlet metric defect of order 0.002. The pure single-sine R7 spectrum does not bound this matched core. Radial mesh or boundary tolerance refinement cannot remove an angular inlet defect.

## A fixed chart, with an exact round background

Fix a reference support amplitude $q_*$ with $0\leq e=8q_*<1$. Define

$$\theta(\psi)=\psi-\frac e3\sin(3\psi),\qquad \rho(\psi)=\theta'(\psi)=1-e\cos(3\psi)>0.$$

This is a fixed analytic orientation-preserving circle coordinate change. For every numerical refinement it is held fixed. The metric is the same geometric metric, written

$$ds^2+a(s)^2\rho(\psi)^2d\psi^2.$$

Represent the surface by

$$F(s,\psi)=a(s)(\cos\theta(\psi),\sin\theta(\psi),0)
 +q\sum_{j=0}^{3M}y_j(s)B_j(\psi)+h(s)e_z.$$

Here $B_j$ are the ordinary cylindrical Fourier basis at angle $\psi$, with threefold modes. The displayed round term and its first two $\psi$ derivatives are evaluated analytically, without Fourier truncation. The vertical mean is integrated separately. This eliminates a fixed metric error from approximating the round reference curve in the new chart.

If $d=F_\psi$, $T=d/|d|$, and $\kappa,N,B$ are the usual curvature/Frenet objects of the coordinate curve, then

$$F_s=-\frac{a'}{a\kappa}N+
 \sqrt{1-\left(\frac{a'}{a\kappa}\right)^2}B=:V.$$

The formula is invariant under a fixed change of angular parameter: $N,B,\kappa$ are geometric and $\partial_s\log|F_\psi|=a'/a$ is still the required length law. The numerical ODE projects $V-a' e_r(\theta(\psi))$ onto the $B_j$. Its derivative is obtained by the existing geometric Frenet JVP, while subtracting the known background analytically.

## Exact inlet and its parameter derivatives

The core remains the exact support family, parametrized by unit arclength as in `fixed_metric_mode3_core.py`. It is evaluated at $\theta(\psi)$, then its difference from $e_r(\theta(\psi))$ is projected. For the pure support curve with amplitude $q=q_*$, the normal angle is exactly $\psi$; its Cartesian position has only the first cylindrical support mode. Higher support coefficients remain free BVP variables. Their derivatives are taken at fixed material $\theta$, as required; the reference coordinate change is not differentiated during the solve.

## The tail DN is conjugated, not reused diagonally

Let $D_k$ be the true physical linear DN for frequency $3k$ in the original material angle. For a represented height

$$z(\psi)=\sum_{j=1}^M z_j\cos(3j\psi),$$

its physical Fourier coefficient is

$$C_{kj}=\frac1\pi\int_0^{2\pi}
 \cos(3k\theta(\psi))\cos(3j\psi)\rho(\psi)\,d\psi.$$

Projecting the DN output back to the $\psi$ basis gives

$$N_{ij}=\sum_{k=1}^K D_k C_{kj}\frac1\pi
 \int_0^{2\pi}\cos(3i\psi)\cos(3k\theta(\psi))\,d\psi.$$

The finite-port BVP uses this dense matrix $N$. The physical-mode cutoff $K$ is an additional approximation parameter and must also be refined. In particular, $K=M$ is generally wrong. The $\theta$-mean and $\psi$-mean are different. Although constant height has DN zero, a nonconstant physical mode has nonzero $\psi$ mean: $\operatorname{mean}_\psi\cos(3k\theta(\psi))=J_k(ke)$. Therefore the linear DN output already has mean $\sum_{k,j}D_k C_{kj}J_k(ke)z_j$. The finite-port solver matches only its nonconstant projected modes. The integrated $\psi$-mean must be compared independently with this linear mean, and subsequently with the full nonlinear mean. The finite linear matrix does not pay either this mean obligation or Cartesian two-jet matching. This correction was identified by independent_audit.

## Whole-equation audit

For the computed C2 interpolant, recover material derivatives by

$$F_\theta=F_\psi/\rho,\qquad
 F_{\theta\theta}=F_{\psi\psi}/\rho^2-F_\psi\rho'/\rho^3.$$

The implementation then evaluates the same Cartesian metric and full Darboux tensor as the earlier code, using the physical $s$ coordinate. The exact infinite Fourier l1 norm in $\psi$ would bound the whole-angle sup norm. However the analytic background and division by $\rho$ make the audited quantities non-polynomial; the implementation only reports a finite sampled FFT l1 diagnostic. It is not a continuous-angle enclosure without tail bounds or further validated refinement. It also need not equal the old l1 norm in $\theta$.

## First reproducible checks

`2026-11-09-950f-prefix-warp-check-m8.json`, generated with $q=q_*=.08$, M8 and the old p160 physical K16 DN, reports:

- analytic JVP versus complex-step relative difference $1.07\times10^{-15}$;
- pure round-background projected flow error $2.13\times10^{-14}$;
- exact-core inlet metric l1 $1.51\times10^{-12}$;
- inlet position / first / second jet errors about $1.99\times10^{-14}$ / $2.71\times10^{-13}$ / $7.30\times10^{-12}$.

These are arithmetic diagnostics, not interval error certificates. The K8 to K16 conjugated DN matrix changes by 53.16 in max entry norm, so this K16 interface is insufficient for an M8 macro solve. A larger physical DN cutoff is being generated before claiming usable convergence. The implementation is `scripts/950f-prefix-warped-bvp.py`.


## Baselines and failed attempts retained

The old arclength/tangent-core M16 refinement, at exactly the old frozen delta .07248923501041592, finished in225.08 s without convergence (node limit). It moved q_eff to .09425820244 and retained metric .0055635688, flow .03074762, full Darboux15.9682, inlet metric .0028744180. This is a failed finite-prefix refinement, not an amplitude obstruction. Checkpoint and coefficients are under `2026-11-09-950f-prefix-frozen-m16_*`.

The new constant-warp M8 direct q_support=.08 design reached a negative Frenet square-root argument −.0003995041 during the post-Newton inter-node residual check. It is an invalid iterate, retained in the run log; no clipping was applied. The q_support=.01 continuation start solved its projected equations (delta .07252798071575,350 nodes,14.50 s), but its actual metric .0001512388, flow .0005739147 and Darboux .03964652 are unacceptable. Its inlet metric is only6.50e−8, so this exposes an interior angular representation defect. It does not certify a prefix. The run and checkpoint names begin `2026-11-09-950f-prefix-warp-design-m8-q01`.

A new frozen s-dependent coordinate chart follows the approximate shape amplitude and tends to the identity, with two zero derivatives, at the cut. This is being tested separately and keeps all failed constant-chart evidence.
