# Macro prefix: amplitude continuation followed by fixed-metric refinement

2026-11-09, macro_prefix / Astra-visible-flex-950f9f73. Numerical finite-prefix result only. The tail interface is still the actual physical *linear* DN, not the nonlinear/infinite tail; no closed-surface claim.

## Physical source and parameter conventions

The physical tail is the weighted K6, width .45, p160 background. Its coefficients are recorded in `2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json`; the nonzero support core is

$$h(\phi)=1+\sum_{j=1}^M c_j\cos(3j\phi),\quad c_1=q_s.$$

Here q_s=.08 means the support-function coefficient, not the R7 tangent-angle coefficient b=.22. The pure core support difference under a phase rotation π/3 is .16. Higher matched c_j are retained and must enter the actual support and curvature bounds.

The meridian design keeps vu=.25,vd=.4,ramp=.4,cycles1,cut r=.6,w=.5, and varies its excursion delta. The angular reference chart is the fixed spline shape in `2026-11-09-950f-prefix-adaptive-chart.json`, multiplied during design by 8q_s. Chart changes are handled by an explicit material-angle pullback of the old Fourier map. The eventual fixed-metric refinement freezes both delta and the chart multiplier.

## Successful Mψ8 design continuation

| q_s | designed delta | sampled FFT metric l1 | sampled curvature max | first cut height |
|---:|---:|---:|---:|---:|
| .01 | .07252798565301503 | 5.24e−9 | 5.43361 | .0001588835914 |
| .02 | .07253060483953916 | 1.30e−8 | 5.55650 | .0003177598801 |
| .03 | .07253496830921587 | 1.07e−8 | 5.67977 | .0004766215738 |
| .04 | .07254107452124742 | 1.88e−8 | 5.80271 | .0006354614047 |
| .05 | .07254892084948035 | 1.01e−8 | 5.92685 | .0007942721354 |
| .06 | .072558503639651 | 3.15e−8 | 6.04794 | .0009530465853 |
| .07 | .07256981874197327 | 2.17e−8 | 6.17134 | .0011117776114 |
| .08 | .07258286079463004 | 3.95e−8 | 6.29304 | .0012704581569 |

Every row reports collocation success at tolerance2e−6. These are different designed meridian metrics; the table is **not** fixed-metric convergence. Directly starting the same M8 solver at q=.08 from a linear guess had failed, and that earlier failed state is retained. Continuation reached a different well-resolved branch with support corrections much smaller than those of the failed iterate.

## Freeze before refinement

Now freeze the exact floating-point profile delta=.07258286079463004 in `2026-11-09-950f-prefix-adaptive-frozen-profile.json`, and freeze the angular reference q*=.08 and the complete weighted tail parameters. In fixed mode q_s becomes an extrinsic unknown, while g is unchanged. Version2 of the adaptive solver adds the already-fixed chart spline knots to the radial mesh; no physical parameter is changed.

| discretization | q_s returned | metric FFT l1 | flow defect | full Cartesian Darboux FFT l1 | nodes |
|---|---:|---:|---:|---:|---:|
| M8 design state, tol2e−6 | .08 | 3.95256e−8 | 1.39848e−7 | 6.47250e−4 | 815 |
| M12, same g/chart, tol2e−9 | .0799999968950362 | 4.66272e−10 | 3.54737e−9 | 1.46305e−6 | 2953 |

The amplitude changes by only−3.105e−9, unlike the unstable old tangent-core M8→M12 refinement. M12 inlet metric FFT l1 is4.41735e−10; sampled curvature is6.293084577, and the Frenet square-root margin stays above .04473983542 at sampled points. The finite linear boundary residual is2.42e−18. These are positive numerical convergence diagnostics for this finite prefix, with the nonlinear interface explicitly absent.

## Actual M12 core and XYZ geometry

The M12 exact chosen support core has coefficients beginning

$$c_1=.0799999968950362,\quad c_2=.0002438597738737105,
\quad c_3=-.000024551029716570587.$$

All12 coefficients, their definition and the analytic support-core diagnostics are in the M12 summary. The explicit triangle-inequality phase support lower bound supplied by the core routine is .15995083776149438. Its conservative support curvature radius interval is [.3526663582,1.6302757178]. These values describe the chosen exact planar inlet, while the finite prefix retains the numerical errors above.

The C2 prefix is evaluated as actual Cartesian XYZ values by `950f-prefix-geometry-export.py`, with a central half-cylinder ell=.16. At M12,4247 radial points×1024 angular points give

$$\max_{\rm sampled}|F|=1.5111884761836525,\qquad2\max_{\rm sampled}|F|=3.022376952367305.$$

The maximum sample is at s=1.1134082392045062,ψ=0, approximately XYZ=(.89155761524,0,1.22017032797). M8 at1659×1024 gives the corresponding 2R value3.022376952132499. This agreement is useful evidence, but 2R_sample is **not** a proved upper bound on the continuous surface or the completed closed surface. The complete tail/caps, continuous coordinate bounds and all cross-piece reach inequalities remain required.

The M12 geometry JSON includes the complete physical cut height coefficients, first/second s derivatives, both mean jets, sign convention sigma=−1, and the actual input vector for the tail. Its first tail-input coefficient is approximately−.0012704581 and the second approximately−1.8201e−5. Therefore a pure one-mode tail experiment does not yet test the actual prefix interface.

## Next numerical step

`950f-prefix-nonlinear-coupling.py` is prepared to replace the finite linear DN by the weighted finite nonlinear solver. It records every response, includes sign inside the nonlinear height input, and audits both mean/nonmean first and second height jets plus the cut's sampled C1 metric defect. It has not yet produced a successful coupled macro state. A new design or a shifted extrinsic amplitude after coupling must be reported as such; the linear-port q=.08 cannot be carried into a nonlinear claim without solving that problem.
