# Fixed-projection nested core spaces and completed small-lambda diagnostics

This is an extension of the first finite double-mode prefix source package,
whose manifest SHA256 is
`bee3472b1a9b2d98d6479b64324d8cc50cdbde88e27b703df664bcbe90dc9b6b`.
The exact required base-file hashes are listed in `base_source_reference.json`.
Put these new scripts beside those base scripts in a scratch directory.
The original source-recovery manifest, worker and physical mode-4 port are
unchanged. No generated numerical checkpoint or field array is included here.

## 1. Completed calculations and their limits

The independent M8 design uses q=.005, eta=.15, a=.147, target transition .08,
control transition .16, BVP tolerance 1e-6 and at most 2400 nodes.

| Lambda | Finite BVP outcome | Sampled metric l1 | Sampled Cartesian Darboux tensor l1 |
|---:|---|---:|---:|
| 0 | accepted, 509 nodes | 5.68000e-7 | .000324610 |
| .05 | accepted, 513 nodes | 2.11838e-5 | .0516402 |
| .1 | mesh limit reached | no accepted-map audit | no accepted-map audit |

These are design steps: delta and vd are allowed to change at each lambda.
They are not a fixed-metric convergence sequence. At lambda .1 the last
finite iterate has 1320 nodes; its proposed refinement exceeded 2400.
RMS residual is .00676732 and the scaled BC residual is 8.63375e-7. The
failure is a numerical outcome, not a nonexistence result.

For lambda .05, the original C2 map and a diagnostic directly projected ODE
jet at the same positions give essentially the same maximum metric error
and tensor error. The metric maximum is .0000211838 near s=.0711975. The
tensor maximum .0516402 is at the existing physical break s=.0551987. Thus
the large defect was not removed by discarding radial interpolation error.
The ODE shadow is only a diagnostic, not a replacement globally C2 map.

The first fixed-metric M12 comparison froze the actual lambda-.05 profile:
delta=.02840636891770959, vd=.2645235084352783, vu=.4, ramp=.45, ramp_eta=.05,
and the original K4/peak_fraction .2 ShortBridge. It changed the original
M-dependent homotopy core basis, so the initial core second-jet difference
was .0271116 despite matching its represented low support moments.

That calculation terminated after 487.21 seconds with solver success,
1349 nodes, RMS 7.35014e-7 and BC 8.51967e-9. However, the core amplitude
collapsed from .005 to **.000007197849748885256**. Its core radius of curvature
range is approximately [.9994067,1.0003641], close to the circular core.
The metric error is still **4.23231e-6**, above 1e-6, and the Cartesian tensor
error is .0114729. It is neither a refinement retaining the original amplitude
nor a valid completed same-metric construction. All these outcomes, actual
physical parameters and scratch output hashes are in `completed_runs.json`.

## 2. A genuinely nested parameter-space construction

Let V_M be the compact complementary support-control space already defined
by the base package. These spaces are nested as M increases: the raw
trigonometric polynomial space grows, while the mean/optional fundamental
constraints stay the same. Canonical moment preconditioning changes only
the coordinates in each space.

Fix J=8 once. Let P_J be the orthogonal Fourier projection onto the
reflection-even support modes n,2n,...,Jn, with n=4. For a fixed positive
lambda define the single linear operator

\[
T_\lambda=\lambda I+(1-\lambda)P_J.
\]

It has eigenvalue 1 on the projected space and lambda on its orthogonal
complement. Therefore it is injective for lambda>0, and

\[
T_\lambda V_8\subset T_\lambda V_{12}\subset\cdots
\]

with the original dimensions. This keeps the old mathematical core inside
every refined core family. It differs from using P_M separately at each M,
which was the source of the .0271 initial second-jet change above.

At lambda one this is exactly the original compact support-control space;
all controls and their primitives vanish on the protected circle. At
intermediate lambda values no exact circular arc is claimed. Mean zero,
the exact integral core definition, actual rho and rho derivatives, and the
original full rho positivity guard are retained. Low-mode terms omitted
from P_J are also removed from the conservative derivative bounds; compact
terms remain completely present in those bounds and in the actual geometry.

The implementation rejects lambda zero explicitly. In the target refinement
M=12,J=8, the 11-dimensional control space would be mapped into a space of
dimension at most 8 at lambda zero, so a zero-lambda full-rank BVP cannot be
silently inferred. The baseline root must be obtained separately before
using this positive-lambda refinement provider.

### Exact defining coefficient embedding

If the old compact combination is represented by a raw trigonometric
coefficient vector t, its new canonical coefficients are its exact support
moments: c_new = 2 G_new[2:,:] t. Canonical moment normalization then gives
the same compact function. Applying the same T_lambda preserves that
identity. `embed_compact_coefficients` evaluates this defining formula using
the recorded high-precision constants converted to floats. The mathematical
space identity is exact; the following reported small numbers measure the
runtime floating evaluation and are not interval error certificates.

For the actual M8/lambda-.05 core, M12 re-expression gives maximum errors:

| Quantity | Runtime difference |
|---|---:|
| Core position | 7.8e-16 |
| First material derivative | 6.7e-16 |
| Second material derivative | 5.6e-16 |
| Rho | 4.5e-16 |
| First material rho derivative | 2.1e-14 |
| Second material rho derivative | 2.1e-12 |

The new triangle derivative bound is more conservative despite the identical
curve. The original guard uses 1024 points and certifies a lower bound
.42049, versus the old bound .91936. It is not changed to a sampled pass.
The analytic fixed-material parameter jets have second-jet directional
difference errors 5.37e-8, 4.87e-9, 9.14e-10 at steps 1e-5,3e-6,1e-6,
against derivative scale 8.17. Smaller steps reach roundoff noise.

The complete fixed-metric BVP initialization also retains the old full
warm map in the same material-angle chart: its projection discrepancy is
4.44e-16 and the normalized inlet correction is 1.07e-15. Full Frenet
parameter-direction checks are recorded, including their roundoff plateau;
no claim of a formal Jacobian enclosure is made.

## 3. Reproduction

First regenerate the base source and physical port using the base package.
Then reproduce the small-lambda design (it stops after the recorded failure):

```bash
python -u run_dual_prefix.py --source-topic /scratch/source/bundle/topics/visible-flexible-closed-surface --port /scratch/mode4_port24.json --profile root03-profile.json --out /scratch/double-small-lambda --q .005 --modes 8 --bimodal-eta .15 --lambdas 0 .05 .1 --nodes 201 --max-nodes 2400 --tol 1e-6 --angular 512
python diagnose_dual_prefix.py --source-topic /scratch/source/bundle/topics/visible-flexible-closed-surface --checkpoint /scratch/double-small-lambda-lam0.05.json.gz --out /scratch/lambda005-diagnostic.json --angular 528
python -u refine_fixed_prefix_general.py --source-topic /scratch/source/bundle/topics/visible-flexible-closed-surface --checkpoint /scratch/double-small-lambda-lam0.05.json.gz --out /scratch/nonnested-M12 --modes 12 --tol 1e-6 --max-nodes 2400 --angular 768
python audit_nested_projection.py --source-topic /scratch/source/bundle/topics/visible-flexible-closed-surface --checkpoint /scratch/double-small-lambda-lam0.05.json.gz --modes 12 --out /scratch/nested-core-audit.json
python -u refine_nested_prefix.py --source-topic /scratch/source/bundle/topics/visible-flexible-closed-surface --checkpoint /scratch/double-small-lambda-lam0.05.json.gz --out /scratch/nested-M12-initialization --modes 12 --tol 1e-6 --max-nodes 2400 --angular 768 --check-only
```

The final command in this package records initialization only. Removing
`--check-only` starts the actual independent nested BVP experiment; no
terminal result of that experiment is asserted here.

All physical metric, root, core positivity and residual gates remain. The
M core parameters are actual q and M-1 core controls; both physical profile
parameters are frozen. A future drop in q must be reported as amplitude
collapse, even if the finite solver returns success. No nonlinear tail or
closed surface is solved by these scripts.
