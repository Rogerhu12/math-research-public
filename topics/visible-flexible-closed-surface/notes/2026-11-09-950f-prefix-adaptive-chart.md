# A frozen varying angular chart for the Frenet prefix

2026-11-09, macro_prefix for Astra-visible-flex-950f9f73. Exact coordinate derivation with sampled numerical diagnostics. No complete annulus/collar, closed surface, reach bound, or nonlinear seam assertion.

## Coordinate choice and physical metric

The fixed angular chart is

$$\theta(s,\psi)=\psi-\frac{e(s)}3\sin(3\psi),\quad
\rho=\theta_\psi=1-e(s)\cos(3\psi),\quad v=\theta_s/\rho.$$

The stored chart profile is a clamped C2 cubic spline in $x=s/L$, derived once from the first-order normalized shape amplitude. It is multiplied by a quintic cutoff on $x>3/4$, so $e,e',e''$ all vanish at the final cut. The exact round background $a(s)e^{i\theta(s,\psi)}$ is retained analytically. The physical metric is still $ds^2+a(s)^2d\theta^2$; in computational coordinates it reads

$$g_{ss}=1+a^2\theta_s^2,\quad g_{s\psi}=a^2\theta_s\rho,\quad g_{\psi\psi}=a^2\rho^2.$$

For the geometric Frenet normal velocity $V$ from the preceding constant-chart note, the new computational velocity is

$$W=F_s|_\psi=V+vF_\psi.$$

The tangential term is essential. The code projects $W-\partial_s[a(s)e_r(\theta(s,\psi))]$, and integrates $\operatorname{mean}_\psi W_z$ as the omitted vertical mean. Both include the advective contribution.

The chart shape is stored in `2026-11-09-950f-prefix-adaptive-chart.json`. The multiplier is $8q_*$, where $q_*$ is explicitly recorded in each run. During amplitude design it may change with the desired core amplitude; it is a numerical coordinate parameter. For the eventual fixed-metric angular/radial refinement sequence it will be kept fixed. No coordinate choice modifies the physical metric or repairs a nonzero isometry residual.

## Full second-jet recovery

With $F_{s\psi}$ denoting the mixed derivative in the computational variables, the recovered physical derivatives are

$$F_s^{\rm phys}=F_s^{\rm chart}-vF_\psi,\qquad
F_\theta=F_\psi/\rho,$$
$$F_{\theta\theta}=F_{\psi\psi}/\rho^2-F_\psi\rho_\psi/\rho^3,$$
$$F_{s\theta}^{\rm phys}=
(F_{s\psi}-v_\psi F_\psi-vF_{\psi\psi})/\rho,$$
$$F_{ss}^{\rm phys}=F_{ss}^{\rm chart}-2vF_{s\psi}+v^2F_{\psi\psi}
 +(v v_\psi-v_s)F_\psi.$$

These are used before metric and Cartesian Darboux tensor evaluation. For the C2 interpolant, the derivative of $W$ is calculated as

$$\partial_s W=\partial_sV+v_sF_\psi+vF_{s\psi},$$

where $\partial_sV$ includes both the geometric Frenet JVP and the explicit dependence on $a,a'$. The spline is C2 and the cutoff has two vanishing derivatives; the chart does not create a second-jet jump at its internal knots or at the tail cut.

At the cut the chart, first derivative and second derivative equal those of $\theta=\psi$. Hence the true physical linear DN is again diagonal on the represented height modes. Unlike the constant chart, it creates no extra linear mean by Fourier conjugation. The nonlinear mean derivative, full nonlinear DN, actual Cartesian seam, and tail convergence remain unpaid obligations.

## Reproducible checks

Implementation: `scripts/950f-prefix-adaptive-chart-bvp.py`. The `--check-only` diagnostic at q=q*=.08, M8 gives JVP relative difference $4.11\times10^{-16}$, projected round-background flow $2.13\times10^{-14}$, and exact zero for the cut's $e,v,v_s,v_\psi$.

`950f-prefix-chart-twojet-check.py` independently inserts an exact rotational surface into the chart and recovers $F_s,F_\theta,F_{ss},F_{s\theta},F_{\theta\theta}$ to maximum errors $2.22\times10^{-16},2.22\times10^{-16},1.78\times10^{-15},1.39\times10^{-15},2.04\times10^{-15}$. Its nonlinear velocity_s central-difference error decreases from $3.65\times10^{-6}$ at h=1e−4 to $5.70\times10^{-8}$ at h=1.25e−5, with factor four reduction on each step halving. The full output is `2026-11-09-950f-prefix-chart-twojet-check.json`.

These are implementation checks. Finite sampled FFT l1 values are explicitly not certified continuous-angle bounds, because the exact background and the inverse powers of $\rho$ are not finite trigonometric polynomials. Error enclosures or sufficiently controlled angular refinement are still required.

## Initial numerical outcomes

A direct q=.08 M8 seed did not converge: the nonlinear iteration drove support corrections toward the convexity boundary and produced metric .40355 and sampled curvature959.14. Its checkpoint is retained (`2026-11-09-950f-prefix-adaptive-design-m8-q08`). It was never a valid candidate and no square-root clipping was used.

The small-amplitude design q=q*=.01 succeeds at delta .07252798565301503,376 nodes,15.23 seconds. Sampled diagnostics are metric5.24471e−9, flow9.03742e−9, full Cartesian Darboux3.05231e−5 at collocation tolerance2e−6. Inlet metric is1.94e−14; sampled curvature5.43361; physical first height mode at the cut .0001588835914. The mean and nonlinear tail are not matched. This is a finite-prefix numerical state only.

Amplitude continuation is implemented by `950f-prefix-continue.py`. When the chart reference changes, `BVP.restart` solves the old/new material-angle identity, evaluates the old Fourier polynomial at the inverse angle, and projects it into the new basis. It does not directly reuse coefficients attached to different coordinates. Every stage's checkpoint, command, failure status and sampled audits are retained. Delta remains a design variable in this stage, so the stages do not form a fixed-metric convergence sequence.
