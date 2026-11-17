# Finite double-mode prefix: first actual solve and one same-metric refinement

This package records a new finite Frenet calculation using the literal physical
mode-4 tail port. It does not provide an exact isometry, a nonlinear tail, a
closed surface, or a 10% held-motion example. The two finite solves have
homotopy parameter zero, so their cores have no exact circular plateau.

## Definition and parameter count

The base core radius of curvature is

\[
\rho(\phi)=1+q\{(1-\lambda)[-15((1+\eta)\cos4\phi-\eta\cos8\phi)]
 +\lambda\rho_{\rm target}(\phi)\}+\sum_j c_j(b_j+b_j'').
\]

Here `eta=.15`, the plateau half-width is `.147`, its transition is `.08`,
and complementary controls use transition `.16`. The target and exact
integral definition are inherited from `plateau_core.py`. The complementary
controls are C4, vanish together with their primitive on the plateau, and
have zero mean. Their prescribed support moments at modes 8,12,... form the
identity. No fundamental-moment constraint is imposed. At lambda zero the
controls are their identical represented low-moment trigonometric functions;
at lambda one they are the actual supported functions.

For eta in [0,1/3], the new uncorrected curvature-radius bounds are
`1-15q <= rho <= 1+15q(1+2eta)` and
`|rho_phi| <= 60q(1+3eta)`. The target/control contributions are added using
their original conservative bounds. Actual material derivatives use both
harmonics with their correct frequencies. No positivity or Frenet root gate
was weakened.

The design has M unknown parameters. The first changes the physical radial
excursion delta, and the second changes the physical return speed vd. The
core's c8 slot and every derivative of that slot are identically zero.
Remaining parameters control c12,c16,... . The initial guess sums two full
backward eigenlines of the actual physical profile and literal tail DN.

The fixed-metric calculation keeps both actual delta and vd fixed. It uses
log(q/q_seed), c8/q_seed, c12/q_seed,... as its M parameters. This explicitly
releases c8; it does not keep the core fixed during nonlinear refinement.
Before solving, the old lambda-zero core is preserved exactly by its low
support moments. Its position and first two material derivatives agree in
the numerical audit to below 2e-15. The change in the reference lift is also
included in the seed map.

## Radial numerical coordinates

Changing vd changes the relative lengths of physical segments. The design
therefore uses an explicit monotone C2 quintic coordinate map that fixes
every physical profile break. On each reference interval of length h,
with physical secant r and common node derivative d,

\[
s=s_i+dh u+(r-d)h(10u^3-15u^4+6u^5).
\]

The derivative is bounded below by `min(d,(15r-7d)/8)`. The common d is a
smooth negative-power mean of all secants; the actual lower bound is checked
on every trial. The second derivative vanishes at every shared knot. Both
physical-parameter Jacobian columns include this coordinate change by
centered differences. Core-control columns use the existing analytic
material-angle derivative. The original excursion/range gates remain.

An initial engineering diagnostic detected a stale vd flow cache. The fix
synchronizes the inherited one-parameter cache, the two-parameter cache, and
the lifted geometry after every physical-parameter change. Corrected full
directional differences decrease from 8.68e-7 to 7.89e-8 to 1.43e-8 as the
step goes 1e-4, 3e-5, 1e-5. The erroneous diagnostic is retained by hash;
it is not a mathematical failure result.

## Completed calculations

Both use q_seed=.005, eta=.15, lambda=0, angular size 512, BVP tolerance
1e-6, boundary tolerance 1e-8, and maximum 2400 nodes. The actual physical
profile after design is delta=.028406992702837357 and
vd=.2645035359076601, with vu=.4, ramp=.45, ramp_eta=.05 and the original
ShortBridge K4/peak_fraction .2.

| Quantity | M6 design | M8, the same physical metric |
|---|---:|---:|
| Solver success | true | true |
| Nodes | 509 | 481 |
| Actual q | .005 | .004959299287687804 |
| Maximum solver RMS | 9.8718e-7 | 9.8649e-7 |
| Maximum scaled BC | 4.1596e-15 | 1.4577e-14 |
| Sampled physical metric FFT l1 | 4.26231e-6 | 5.73335e-7 |
| Sampled Cartesian Darboux tensor FFT l1 | .00204203 | .000327145 |
| Unprojected flow defect | 2.94376e-5 | 4.12566e-6 |
| Sampled maximum principal curvature | 8.59696 | 8.59146 |
| Minimum sampled Frenet margin | .00399781 | .00399840 |

These two levels give finite improvement, not a convergence theorem. The
map audit uses the explicit shared two-jet quintic interpolation and the
actual Cartesian coordinate chain rule. Its FFT l1 quantities are sampled
diagnostics, not continuous-angle interval enclosures.

The M6 maximum metric defect is at an existing node s=.29027035110038546,
in G/a^2-1. It persists identically when the derivative is replaced, for
diagnosis only, by the directly projected ODE jet at that same position.
Node and midpoint Darboux errors also agree to their displayed precision.
The largest metric harmonics are the first omitted modes 28 and 32, of
sizes 1.74914e-6 and 1.49210e-6. This identifies an angular truncation issue
in this run, rather than a radial interpolation spike. The ODE shadow is
not a replacement C2 map.

The chosen circularization path fixes h8/q from -.0357142857 at lambda zero
to approximately +.0984703233 at lambda one. It therefore crosses zero at
approximately lambda=.26615784. Because the primary may force mode 8 at
quadratic order, this is a possible path compatibility issue. No failure
or nonexistence conclusion is inferred from that observation.

## Reproduction

Use an independent scratch destination. The recovery manifest contains 70
small original source files, including the previously easy-to-miss `.cjs`
dependency. It contains no generated checkpoints or numerical field arrays.
Each file is recovered by exact historical commit and checked by SHA256.

```bash
python recover_m3_source.py --repo /path/to/math-research-public --dest /scratch/double-source
python export_original_worker_port.py --source-topic /scratch/double-source/bundle/topics/visible-flexible-closed-surface --config mode4_physical_config24.json --out /scratch/mode4_port24.json
python run_dual_prefix.py --source-topic /scratch/double-source/bundle/topics/visible-flexible-closed-surface --port /scratch/mode4_port24.json --profile root03-profile.json --out /scratch/double-q005-m6 --q .005 --modes 6 --bimodal-eta .15 --lambdas 0 --nodes 201 --max-nodes 2400 --tol 1e-6 --angular 512
python diagnose_dual_prefix.py --source-topic /scratch/double-source/bundle/topics/visible-flexible-closed-surface --checkpoint /scratch/double-q005-m6-lam0.json.gz --out /scratch/double-diagnostic.json
python refine_fixed_prefix.py --source-topic /scratch/double-source/bundle/topics/visible-flexible-closed-surface --checkpoint /scratch/double-q005-m6-lam0.json.gz --out /scratch/double-q005-m8-fixed --modes 8 --tol 1e-6 --max-nodes 2400 --angular 512
```

The recovered port must hash to
`2a3412f96702f409b2e074ac23b3223d4e0f1d0fe1f1114e7ae34911a5bf9095`.
The exporter's inherited docstring says m3; the literal configuration and
exported modes here are 4,8,...,96. No mode labels or DN values are changed.

`completed_runs.json` contains compact scalar records and the hashes of
the full scratch outputs. Regenerated numerical checkpoints and coefficient
arrays belong outside the repository. The source contains a design-only
guard and a separate fixed-metric driver so that physical changes cannot be
silently called refinement.
