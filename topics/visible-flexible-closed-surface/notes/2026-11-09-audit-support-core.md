# Independent audit: support core and fixed-arclength parameter derivative

Reviewer: Astra independent_audit, 2026-11-09. I did not construct the core/BVP implementation.

Target: `notes/2026-11-09-fixed-metric-mode3-prefix.md`, SHA256 `c3f0395a5e15598f77b9978e9168778511c236f0f21bba46735ea05088bdc35a`, together with the formulas in `notes/fixed_metric_mode3_core.py`.

**Verdict: PASS for the exact support-core identities and the complete fixed-arclength parameter Jacobian.** They are valid throughout the strictly convex finite-support-coefficient domain, not merely as a small-amplitude expansion. I did not rerun the projection table or any BVP for this local mathematical review.

Write n=(cos(phi),sin(phi)), t=(-sin(phi),cos(phi)), h=1+sum c_m cos(m phi), and rho=h+h''. The frame derivatives n_phi=t and t_phi=-n cancel the normal contributions in gamma_phi and give gamma_phi=rho*t. Since dtheta/dphi=rho>0, gamma_theta=t and gamma_thetatheta=-n/rho. The integral of rho over one period is2pi. For h=1+q*cos(3phi), rho=1-8q*cos(3phi)>0 when0<=q<1/8, so the exact maximum curvature is1/(1-8q).

The strictly convex support curve encloses a convex body with support h. The sum h(phi)+h(phi+pi)=2 in the pure mode3 case, proving constant width2. Additional even Fourier frequencies contribute twice their cosine terms to this width and must be reported separately, as the code does. Constant width does not mean central symmetry: the pure nonzero mode3 core is not centrally symmetric. Consequently the earlier diameter equality D=2*maxnorm cannot automatically be applied to a closed assembly using this core; the general upper bound D<=2*maxnorm remains available.

For the parameter derivative, the arclength relation is

$$\theta=\phi+\sum_m\frac{1-m^2}{m}c_m\sin(m\phi).$$

The choice of zero angle is independent of the coefficients because every sine vanishes at phi=0. Differentiating at fixed theta therefore gives

$$\delta\phi=-\frac{1-m^2}{m\rho}\sin(m\phi).$$

At fixed phi, delta gamma=cos(m phi)*n-m*sin(m phi)*t. The change of phi contributes the entire gamma_phi*delta phi=rho*t*delta phi, including the moving normal and tangent. Adding the two contributions gives

$$\delta\gamma=\cos(m\phi)n-\frac{\sin(m\phi)}m t.$$

This is exactly the implementation in `parameter_derivatives`. At the circle, phi=theta, it gives the radial coefficient1 and tangential coefficient-1/m in the material cylindrical basis. The moving-frame contribution is essential to this factor.

Differentiating gamma_theta=t at fixed theta gives delta gamma_theta=-n*delta phi. Differentiating gamma_thetatheta=-n/rho then gives

$$\delta\gamma_{\theta\theta}=-t\delta\phi/\rho+n\delta\rho/\rho^2,$$

where delta rho=(1-m²)cos(m phi)+rho_phi*delta phi. Both additional jet variations in the note are correct. As a check, differentiating the closed expression for delta gamma with respect to theta yields the same first-jet variation directly.

The constructor's continuous convexity allowance also has the correct direction: with L=sum |m(1-m²)c_m|, every normal angle is within pi/N of a sampled angle, so min(rho)>=min_sample(rho)-L*pi/N. The corresponding upper allowance bounds max(rho), hence its reciprocal is a safe curvature lower bound in exact arithmetic. For an uncorrected single mode, the closed-form bounds used by the code are exact. Floating-point evaluation errors are not enclosed by this observation.

One implementation-label caution: `initial_speed_limit` currently reports `minimum_sampled_curvature`. For corrected multimode cores this sampled minimum is generally an upper estimate of the true curvature minimum; if it is used as a rigorous Frenet admissibility limit, the existing conservative `curvature_lower_bound` is the appropriate quantity. This does not affect the exact core formulas, and the projection outputs themselves explicitly retain their sampled labels.

Finite angular projection of the exact inlet can lose its exact unit-speed metric. The mathematical core identity does not remove that truncation error. The author correctly reports the projection error separately and does not call the projection table a solved same-metric prefix or a closed flex.

### Author correction checked

The author has changed `initial_speed_limit` to the conservative `curvature_lower_bound` and retained `initial_speed_limit_sample` separately. I checked those assignments. The expanded note, SHA256 `3a06d5a9d8d4431b208a3c9d48bd9cbdb644473011c40fdb4848e18d45cfeff3`, also reports new design calculations; the pure support identities remain unchanged and PASS. This addendum does not independently rerun or certify those newly appended BVP design rows.
