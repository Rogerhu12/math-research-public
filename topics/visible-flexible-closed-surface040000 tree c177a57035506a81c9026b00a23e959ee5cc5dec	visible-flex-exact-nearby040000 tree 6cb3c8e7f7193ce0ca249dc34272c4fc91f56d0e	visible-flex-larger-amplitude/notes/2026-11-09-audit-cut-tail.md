# Independent audit: cut-preserving tail, linear DN, and unchanged deep source

Reviewer: Astra independent_audit, 2026-11-09. I did not construct or modify the candidate cap, warp, or main linear propagator. This audit concerns the original `slopeCap=.02,protectCell=80` configuration. Changing protectCell later changes the background metric and requires a separately frozen candidate.

Audited source hashes:

- `scripts/root_cut_preserving_tail.mjs`: `c76f81a14c71ca6ca360c774b0b6e65c4082ada29519620949eb6ef436f3c8e1`.
- `scripts/root_cut_tail_linear.mjs`: `29bc8232abd880516b5044325285d01cff05ef0c83140c3c8b2919439be0869d`.

## Main findings

1. The cut-restoration derivative, radial warp, physical-height linear ODE, and projective log-normalization formulas are correct. An independent Python reconstruction reproduces the finite background and its cut jets.
2. The small m2 linear positivity threshold is real for this finite-profile linear branch. Independent adaptive propagation gives approximately4.107730815e-6. It is not a sign mistake or a normalization artifact.
3. **The original complete background with protectCell80 does not have curvature bounded by6.** The finite screen covers warped cells0–79 only. The first transition of the next unchanged raw cell already contains a point with curvature above341. This is a large, directly evaluated violation, not an uncertified upper-bound estimate. It invalidates a full-tail reach budget based on this original rotational background, not every possible isometric embedding of its metric.
4. Direct physical coordinates (f,f_r) become poorly conditioned in very deep cells. The log bookkeeping itself is correct, but the deep total height gain needs a stable coordinate check and step refinement. The shallow normalized DN and positivity threshold agree across the independent formulations and far depths tested.

## Independent computation and scope

`scripts/audit_cut_tail_export.mjs` exports the raw analytic source coefficients and comparison points, without editing the candidate. The compressed frozen input is `notes/2026-11-09-audit-cut-tail-input.json.gz`. The reconstruction in `scripts/audit_cut_tail.py` independently implements the cap, restoration, cutoff factors, SciPy adaptive quadrature, and the physical-height ODE; it does not call the author's warp evaluator or RK propagator. `scripts/audit_cut_tail_momentum.py` independently derives and integrates an alternative nonsubtractive coordinate system. The raw source calibration coefficients are held fixed at the exported values, not recalibrated during the audit. Thus this is an independent check of that numerical metric, not an independent existence proof for the exact cell-calibration roots.

Results:

- `notes/2026-11-09-audit-cut-tail-numerics.json`.
- `notes/2026-11-09-audit-cut-tail-momentum.json`.
- `notes/2026-11-09-audit-cut-tail-momentum-refined.json`.
- `scripts/audit_cut_tail_deep.py` and `notes/2026-11-09-audit-cut-tail-deep-curvature.json`.

All extrema reported from optimization are numerical estimates, not interval enclosures. A single evaluated point with a wide violation margin is sufficient for the negative diagnoses below.

## Cap and radial-warp formula audit

Write raw log slope z(x), capped value c(z(x)), and eta=1-S(x) on the restoring transition. The new log slope is z+eta(c-z). Its derivative is exactly z'+eta(c'-z')+eta'(c-z), as implemented. The quintic S has zero first and second derivatives at both endpoints, so this transition joins the capped branch and raw final port with the required derivative matches.

Let rx=|dr_old/dx|, v=|w_x|/(1+w²)^(3/2), chi be the cutoff, and j0 its endpoint scale. The positive warp speed is

$$|r_x|=A+\alpha B,\quad A=rx\,j_0(1-\chi)+\chi v/K,\quad B=\chi rx/(1+w^2).$$

Choosing alpha=(target-integral(A))/integral(B) gives the required total radial width. Since alpha>0, rx>0, j0>0, and0<=chi<=1, the warp speed is strictly positive on each finite segment. The absolute value in v can make the warp speed nonsmooth at critical slopes, but it remains continuous and positive; w(r) still has a continuous first derivative w_x/r_x, sufficient for the height graph to be C2 there.

At the cut, the final port is exactly raw, chi=0, j0=rCut/oldCut. Its raw slope obeys w_x=-7w*r_old_x/r_old, so

$$w_r\big|_{\rm cut}=-7w_{\rm cut}/r_{\rm cut}.$$

At the deep boundary, chi=0 and j0=1, while the cap is inactive at the tiny raw slope; hence the radius, w, and w_r match the selected raw source. This establishes the local C2 background interface, not a curvature bound for that source.

The independent reconstruction gives:

| Quantity | Independent value |
| --- | ---: |
| alpha | 71.92861702899884 |
| minimum warp width | .14866993535892076 |
| meridian length | .3529172290121697 |
| height span | .021628808248546225 |
| cut r | .6000000000000001 |
| cut w | .5000000000000004 |
| cut w_r | -5.833333333333338 |
| largest radius difference at324 comparison points | 7.8e-16 |
| largest finite-interface w_r jump | 3.4e-16 |
| optimized finite meridian curvature estimate | 5.9998777141 |

On chi=1 segments the inequality kappa_m<=K follows directly from the warp formula. Buffer segments need the separate inequality reviewed in `notes/2026-11-09-audit-radial-reach.md`; the stored raw `bufferMaxCurvature` above6 does not by itself contradict the actual redistributed curvature. None of these finite checks controls the infinite unchanged source.

## Linear equation and positivity diagnostic

For the rotational metric E(r)dr²+r²dtheta², E=1+w², linearize the height Darboux equation at h_r=w with a mode f(r)cos(m theta). The Hessian terms are

$$h_{;rr}=w_r/E,\qquad h_{;\theta\theta}=rw/E,$$

and the right-hand-side gradient variation cancels the extra E terms in the determinant variation. The result is

$$f_{rr}+\frac{w_r}{w}f_r-\frac{m^2w_r}{rw}f=0.$$

In the profile variable x this becomes (f_r)_x=-(log w)_x(f_r-m²f/r), which is exactly the author's RHS after its constant derivative scaling. No missing orientation or E factor was found.

For the literal linearized height h+A*f*cos(m theta), normalized by f(rCut)=1, the angular covariant Hessian is

$$H_{\theta\theta}=\frac{rw}{E}+A\left(\frac{rf_r}{E}-m^2f\right)\cos(m\theta).$$

At each r the permissible amplitude for positivity is base/|linear|. The global sufficient condition uses the infimum over the *continuous* profile. A minimum taken only over sample points is not a certified global sufficient bound; it is an estimate of that threshold. Conversely, an amplitude above the ratio at a specific evaluated point makes this exact linear ansatz negative at a suitable theta, regardless of unsampled locations.

Independent results at far32 with the exported background held fixed:

| Mode | Author RK512 cut DN | Independent momentum DOP853 cut DN |
| --- | ---: | ---: |
| 2 | 5.676917026273384 | 5.676917013597372 |
| 4 | 15.580778667050502 | 15.580778572422625 |
| 6 | 25.549515604462645 | 25.549515349754337 |
| 8 | 35.31157333323465 | 35.31157284624422 |

For m2, the independently optimized threshold is4.107730815247447e-6, near cell1, segment3, x=.99735004. At that point r≈.38333562274, w≈2.407823099e-5, f≈.00284938730, and f_r≈-5.831954117. Thus base≈9.230043666e-6 while the linear coefficient is approximately-2.246993311. The scale of the threshold comes from this very small background slope and a finite negative radial derivative of the normalized solution.

Using far24,32,48,80 on the same background gives the same shallow m2 DN and threshold to the displayed useful digits. Tightening the momentum solver tolerance from2e-12 to2e-13 changes the m2 DN by less than9e-13. The old gentle prefix's leading terminal height mode is about.003729, roughly908 times this linear threshold. Feeding that height into this particular linear lifting would make the angular Hessian negative. This does not prove a nonlinear amplitude impossibility: a large nonlinear correction or a different tail/background could change the conclusion. It does show that this small linear chart cannot justify the desired old-prefix input.

## Log normalization and independent momentum coordinates

If a state is represented as exp(l)*y and each step divides y by its norm while adding the log norm to l, then the terminal outer log is l_out+log|y_out[0]|. Multiplying an intermediate first coordinate by sign(y_out[0])*exp(l-outerLog) correctly gives the height normalized to one at the cut. The author's sign and logarithm formulas are correct.

A separate conditioning issue remains: in very deep cells f_r and m²f/r nearly cancel. I independently used

$$V=f/r^4,\qquad \pi=\frac{\sigma r^4w}{\sqrt{12}\,\mu}\left(f_r-\frac{m^2f}{r}\right),$$

where sigma is the radial orientation and mu is constant within each cell. With P=r^7*w/mu and d tau/dx=sigma*sqrt(12)*r_x/r, the exact equations are

$$V_\tau=kV+\pi/P,\qquad \pi_\tau=-\nu PV-k\pi,$$

$$k=\sigma(m^2-4)/\sqrt{12},\qquad \nu=m^2(m^2-1)/12.$$

At a cell boundary pi rescales by mu_old/mu_new. This system computes the small momentum directly, avoiding cancellation of the two physical derivatives. The far32 m2 log height gain is365.41172681067 in the refined calculation, versus365.40871006734 in the author's RK512 data. A direct adaptive physical-coordinate calculation becomes much less reliable at greater far depths (for example it gave781.59 at far48, while the momentum calculation gives569.06123429). The normalization algebra does not cure a badly conditioned state representation. These errors did not change the tested shallow projective direction and its threshold, but total growth or deep amplitude claims should use the nonsubtractive formulation and their own convergence check.

## The unchanged deep source violates the original curvature budget

For an unchanged source cell n, let delta=delta0*2^(-n), eta=eta0*2^(-etaPower*n), and mu=epsilonScale*delta^a. On the first transition, after its initial port, the exact raw formulas are

$$\log r=\log r_c+\sigma[after(n)+\eta(1+x)]/\sqrt{12},$$
$$\log w=\log\mu+(\log R-\log\delta)S(x)-7\log r.$$

No calibrated alpha_n occurs in this transition. Therefore w_r follows directly by dividing the analytic x derivatives. At n80 and the fixed rational sample x=.9, the resulting curvature is341.3474778119. Its optimized value is about342.8467339. The very small slope (approximately3.3e-40) is divided by an even smaller radial transition width; a tiny slope is not a small curvature.

| Raw cell | Curvature at fixed x=.9, first transition |
| --- | ---: |
| 80 | 341.3474778119 |
| 96 | 22.7264257178 |
| 112 | 1.4807168447 |
| 120 | .3755430840 |
| 128 | .0949035276 |

The double-precision radii at these depths round to r_c=.25, but the defining analytic radial derivatives are nonzero. Taking finite differences of rounded radii would erase the very phenomenon being checked. The witness uses those defining derivatives directly and has a huge margin above6.

If one additionally has a uniform exact-source bracket alpha_n in[1/2,2], the conservative all-segment bound in the closing note gives3.32867656 at n128 and decreases thereafter for these parameters. This is a possible route to a valid deeper cutoff, conditional on that bracket; the first-transition table alone is not an upper bound for all deep segments. Moving protection from80 to a deeper fixed index is a change of geometry, even though its C0 displacement may be tiny. It must be frozen before claiming same-metric convergence under frequency or mesh refinement.

No nonlinear solution, full closed flex, or complete reach certificate is established by this audit.

### Native RK1024 rerun

I also reran the author's unchanged script with1024 radial steps and far32; the separate output is `notes/2026-11-09-audit-cut-tail-root-s1024.json`. It gives m2 DN5.676917011542046 and sampled threshold4.107731473642127e-6, confirming the independent values. Its log height gain365.41157995531 moves substantially toward the momentum result365.41172681067 from the RK512 value365.40871006734. Thus finite-step propagation error is present in the original gain as well as the deeper physical-coordinate conditioning concern; there is no evidence of an algebraic error in the log normalization itself.
