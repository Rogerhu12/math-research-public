# Independent audit: gentle ellipse prefix / tail interface

Author: Astra independent_audit, 2026-11-09. This note concerns interface mathematics and independent verification; it does not construct the main candidate.

## Confirmed source-level fact: the old port is not a scaled tail at the gentle cut

The old exported port uses `(rCut,wCut)=(0.98,0.05)`, `slopeCap=0.5`, `capTransition=2`, width0.08. `repo_scan_gentle.scaled_port` replaces these by `(0.6,0.5)` while only multiplying all physical Robin slopes by `0.98/0.6`; its own docstring correctly labels this provisional. Euclidean uniform scaling preserves `w=h_r`, so multiplying w by10 cannot arise from that scaling. It requires a new metric profile and recomputation of the exact or numerical tail DN.

The existing compact-tail builder also rejects the naive parameter substitution. Its cap is exactly unchanged only for `log(w)<=log(slopeCap)-capTransition`. Thus preservation of the prescribed shallow derivative requires `slopeCap >= wCut*exp(capTransition)` (up to numerical endpoint tolerance). For wCut0.5 and transition2 this means slopeCap at least3.694528049..., whereas inheriting slopeCap0.5 fails before any solve. This is a concrete interface constraint, not a no-go theorem for other tails.

An available repair within the same builder is to choose a smaller positive capTransition and a slopeCap greater than wCut, satisfying `capTransition <= log(slopeCap/wCut)`. For example slopeCap0.6 and transition0.1 preserve the shallow slope. Whether its recomputed nonlinear tail matches the prefix, has small enough curvature, and converges remains to be independently checked.

## Exact phase/collar interface (conditional)

For a rotational material metric `g=ds^2+a(s)^2 dtheta^2` and a single exact embedding F, the phase operation `F_phi(s,theta)=R_phi F(s,theta-phi)` preserves g. On an open standard rotational collar, `F=(a(s)cos(theta),a(s)sin(theta),z(s))`, this operation is pointwise the identity. Hence fixed caps may be attached pointwise with C2 regularity if the actual band and standard collar have matching Cartesian jets of order at most2. A nonzero finite Robin trace is not such a collar.

The same statement for an approximate band preserves the size of its metric error, because the error tensor is pulled back by a material angular translation and an ambient rotation. This does not lower that error or establish an exact solution; it does reduce the all-phase local metric and curvature audit to one representative band once real rotational collars have been supplied.

## Remaining audit

Independently inspect the nonlinear DN and its mean/rigid-gauge matching, frozen-metric refinement, and the eventual actual C2 closure. No completion certificate is issued here.

## Independent nonlinear mean / orientation check

The independent evaluator `scripts/audit_port_trace.py` uses only saved PPoly coefficients, NumPy/SciPy, and its own Cartesian Fourier basis and Frenet calculation. It verifies the SHA256 of every compressed coefficient chunk and does not invoke the candidate BVP or tail solver. The result is `notes/2026-11-09-audit-port-trace.json` (Ntheta=1024 and2048).

On the accepted gentle M12/aspect1.2 prefix, at r=.6,w=.5, it finds

| Quantity | Independent value |
| --- | ---: |
| actual mean vertical s-derivative | .4473734283080657 |
| rotational value w/sqrt(1+w²) | .4472135954999579 |
| nonzero mean s-correction | .0001598328081078 |
| corresponding positive-background tail mean u_r | .5001786985119818 |
| mean from independent angular holonomy root | .5001786985124089 |
| root minus actual mean | 4.3e-13 |
| angular metric error | 2.7973e-8 |
| terminal nonmean height max | .0037353211268815 |

Both angular resolutions agree at the shown digits. These are floating-point sampled checks, not interval enclosures or an infinite-tail existence result.

Here is the exact geometric mechanism behind the mean check. For an exact metric E(r)dr²+r²dtheta² and height u, put S=r²-u_theta² and Delta=E*S-r²*u_r². Where the planar projection has positive Jacobian, the turning rate of its theta curve is

$$\omega=\frac{r^2(r+u_r u_{\theta\theta}-u_\theta^2/r)}{S\sqrt\Delta}.$$

This follows by differentiating the two planar inner-product equations and solving for the coefficient of X_r in X_thetatheta. A simple positively oriented closed projection requires mean(omega)=1. Fixing the nonmean u_r and solving this scalar equation supplies the mean branch. At the circular reference its derivative with respect to mean u_r is w>0, so this branch is locally unique. On the saved prefix the derivative is about .50050168594. Imposing zero nonlinear mean correction gives mean(omega)=.9999105890734004, which is not one. The nonlinear mean correction is therefore not optional: omitting it would already create a first-jet error about1.6e-4 in s at this cut. Correct nonmean trace alone is insufficient.

For an inward segment write sigma=sign(dr/ds)=-1, E=1+w². To retain the upward prefix orientation, its physical height is z=sigma*u(r,theta)+constant, with u a standard positive-background tail. Therefore

$$z_s=u_r/\sqrt E,\qquad z_{ss}=\sigma(u_{rr}/E+u_r a_{ss}),\qquad a_{ss}=-E_r/(2E^2).$$

The tail DN must be evaluated on input `sigma*H_prefix`; the first-jet condition is `H_prefix_s=DN(sigma*H_prefix)/sqrt(E)`. In a nonlinear DN the sign belongs inside the input. The existing large-topic `f6curve_inward_bridge_bvp.py` already uses exactly this convention, including the nonlinear mean and second jets. This is a requirement for any replacement coupling, not a newly found defect in that existing implementation. Using an unreflected positive tail would instead give an O(1) first-jet jump (.8945870 in the independent example).

When both sides are exact isometries with the same metric and the same height/Cauchy trace, a simple planar projection and the same holonomy branch determine their planar cross-section up to rigid planar motion. This explains how a matched nonlinear DN can provide a full seam after fixing the planar gauge. It does not validate replacing the DN by the provisional linear Robin port, and an actual Cartesian two-jet comparison remains necessary for the approximate computed maps.

## Continuity of the phase family

Once a compact C2 band with actual open rotational collars exists, a continuous scalar phase phi(t) produces a family continuous in the C2 topology: all derivatives of F of material order at most2 are uniformly continuous on the compact parameter band, so angular translation is continuous in their uniform norms; the ambient rotation is continuous as well. The fixed-cap extension is identical on a neighborhood of each seam. No C3 regularity is required for this continuity argument. Fixed asymmetric cap metrics do not obstruct it, since only the rotational band is reparametrized.
