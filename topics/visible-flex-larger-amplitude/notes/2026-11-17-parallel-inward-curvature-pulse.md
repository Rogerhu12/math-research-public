# Compact curvature pulses after the true .995 cut

Finite new-scalar designs; not a refinement of the unpulsed metric or an accepted closed surface. The actual .995 parent is `d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f`; original scalar carrier is `11960350cb15cc43334d039e161184a8f7b7caa0650311c96ae8b33eac69e327`. Each case zero-lifts the same true endpoint/core to M320, retains its physical density, and uses all962 Frenet equations at N4096.

## Explicit scalar

For t=s−.995 and clamped quintic S(u)=10u³−15u⁴+6u⁵, add A[S(t/w)−S(t/w−1)] to the first curvature ramp. Its support is [0,2w], its exact total turn is Aw, and its 0/1/2 derivatives vanish at the support endpoints. Subtract Aw/1.5 from the later constant-curvature duration, preserving the ideal reference's final angle −π/2. The old cut a/a′/a″ agree exactly. Every amplitude defines a different fixed a; R636's old R/L enclosure does not automatically transfer. Exact integrals define the scalar; the evaluator uses Gauss32 split at the pulse knots.

## Two bounded batches, all outcomes

DOP853, rtol1e−13, atol1e−16, explicit max/first step .000015625, target1.0; RHS endpoint Gram uses independent8192 angles. No failed state is a new parent.

| w | A | last accepted s | reached1.0 | nodes / RHS | endpoint relative Gram |
|---|---:|---:|---|---:|---:|
| .001 | −.5 | .9977273981296616 | no | 185 /2328 | — |
| .001 | .5 | .9975190130657777 | no | 172 /2159 | — |
| .001 | 1 | .9974251746769252 | no | 164 /2027 | — |
| .005 | −1.5 | .9977884566824422 | no | 189 /2387 | — |
| .005 | −3 | 1.0 | yes | 322 /3853 | 2.4393092161721222e−6 |
| .005 | −5 | 1.0 | yes | 322 /3853 | 8.173149194819798e−7 |

All four failures are Q/W/H domain evaluations, not proofs of nonextendability. The −5 case has sampled endpoint Hmin .0002095000964062078; the −3 case has3.539112573027612e−6. New ideal reference R/L are .5352963422811989/1.2997166467351668 for −3 and .5376528172492877/1.3063833134018337 for −5. These floating reference values are not interval bounds. Reaching1.0 and an endpoint Gram below1e−6 do not certify the whole common-jet quintic, the old/new C² join, or any closed-tail condition. The −5 whole segment and explicit jet bridge are the next necessary read.

## Reproduction

Source [curvature-pulse.py](2026-11-17-parallel-inward-curvature-pulse.py), SHA256 `148dd6305df67c881ceb180249f4eaf34e3a996a6568c7378be467d41a92d157`; frozen short-IVP source `13f363bef6133f30795842055d4bea6367748a1e954f29bafb42e1653b4e979c`. S is this topic's scripts directory; commands run with PYTHONDONTWRITEBYTECODE=1 and BLAS/OMP threads1.

```sh
PYTHONPATH="$S" python "$S/../notes/2026-11-17-parallel-inward-curvature-pulse.py" --reference parallel-continue0995-m112.json.gz --metric parallel-inward0997-m112.json.gz --half-width .001 --amplitudes -.5 .5 1 --end 1.0 --out parallel-inward-curvature-pulse.json
PYTHONPATH="$S" python "$S/../notes/2026-11-17-parallel-inward-curvature-pulse.py" --reference parallel-continue0995-m112.json.gz --metric parallel-inward0997-m112.json.gz --half-width .005 --amplitudes -1.5 -3 -5 --end 1.0 --out parallel-inward-negative-curvature-pulse.json
```

Raw scratch reports SHA256: small pulse `b47298bef64f7664b4a742fed688a0024fcfa8c98cfd13cdb02e5a5d4532e244`; negative pulse `71922db5948f57e864089a7d6febcad9dabc657a6b55808bac04953df519c60f`.
