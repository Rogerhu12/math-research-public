# A complete C² metric cycle based on the strong-core Hermite prefix

This note specifies a metric provider and its interface to the existing
nonlinear Frenet BVP. It is not a proof of a nonlinear boundary-value
solution, a closed surface, or any of the requested global certificates.

## Parameters and exact radius balance

Choose an outward speed `V∈(0,1)`, inward speed `W∈(0,1)`, initial
acceleration `k0≥0`, outward excursion `δ>0`, an outward constant-speed
length `C≥0`, a turn length `T>0`, and a braking length `B>0`.

The Hermite outward length is determined by

\[
 \delta=\frac{VS}{2}+\frac{k_0S^2}{12},\qquad
 S=\frac{12\delta}{\sqrt{9V^2+12k_0\delta}+3V}.
\]

Assume `k0 S≤3V`. On `[0,S]`, use the controlled Hermite formula proved in
`alternative-curvature-controlled-turns.md`. The endpoint jets are
`(1+δ,V,0)`. Append a constant-speed interval of length `C`, and then the
same note's smoothstep turn from `V` to `−W` in length `T`.

The radius after the turn is

\[
 a_1=1+\delta+VC+T(V-W)/2.
\]

Take a constant inward-speed interval of length

\[
 L=\frac{\delta+VC+T(V-W)/2-WB/2}{W},\tag{1}
\]

which must be nonnegative. Finally, for normalized brake coordinate
`u∈[0,1]`, set

\[
\begin{aligned}
 a&=1+WB/2-WB(u-u^3+u^4/2),\\
 a'&=-W(1-3u^2+2u^3),\\
 a''&=6Wu(1-u)/B.
\end{aligned}
\]

Equation (1) makes the final jets exactly `(1,0,0)`. Every interior seam
matches `a,a′,a″`; hence the entire piecewise metric is C². The slope lies
in `[-W,V]`. The radius is at least one: it first increases, then decreases
after the unique turn point, and ends at one. In particular the formal
background surface of revolution has a real positive height derivative
`sqrt(1−a′²)` throughout. This latter fact does not imply that a strong
noncircular Frenet curve stays inside its stricter admissible domain.

The physical meaning of `δ` is the radius increase at the end of the
Hermite leg; the maximum radius is generally larger, since the next coast
and the beginning of the turn also move outward. At fixed `V,k0,C,T,B,W`,
changing `δ` changes `S`. Thus `δ` is an effective design parameter for the
existing BVP, rather than an ignored label.

At the core, the jets are `(1,0,k0)`, so R6 permits the reflected C² seam
when the immersion satisfies its hypotheses. At the other end, `(1,0,0)`
matches the original `DirectionalBridge` without a metric jet jump.

## Implementation and verified source interface

`computations/alternative-hermite-cycle.py` exports `HermiteTurnCycle`
and `install(PlanarSymmetryFlow)`. Set `ramp_law='hermite_turn'` and provide
`delta,vu,vd,start_acceleration,coast_outward,turn_length,brake_length`.
The original provider also requires `ramp∈(0,.5)`, `direction='outward'`,
and `cycles=1`; `ramp` is not used to define this new law.

Call `install()` after loading the source modules and flat-profile patch,
but before constructing a BVP. The patch changes only in-memory class
methods, replaces the physical prefix duration and breakpoints, and leaves
the original bridge object intact. It does not edit the frozen source
tree. It supports vectorized `profile(s)` as required by the BVP.

The following concrete provider was instantiated with the frozen source
snapshot `86943663` through `numerical-m2-prefix.py`:

```
delta = .12959375
vu = .35
vd = .6
start_acceleration = .45
coast_outward = .05
turn_length = .3
brake_length = .2
```

This gives `S=.65`, `L=.08265625`, prefix length `1.28265625`, and total
length with the existing bridge `1.9215044709066094`. Sampled background
prefix height is `1.2109999451` and maximum background principal curvature
is `4.8007959853`. The measured interface jets were

| Location | a | a′ | a″ |
|---|---:|---:|---:|
| Initial core | 1 | 0 | .45 |
| Prefix/bridge seam | 1 | 0 | 0 to floating precision |
| Original physical tail cut | .6 | −.8944271910 | 1.8666666667 |

The source's two backward linear directions at the core are approximately
`(.998742464,.050134729)` for mode two and
`(−.970574304,.240801827)` for mode four. This example is therefore a
well-defined provider, not a resonant or solved BVP.

## Existing strong-prefix evidence and the remaining bridge

For the exact intended support coefficients
`h=1+.38 cos(2φ)−.38/(10√2) cos(4φ)`, the outward Hermite leg with
`k0=.45,V=.35,S=.65` was integrated with fixed physical parameters:

| Fourier modes M | angular points | maximum sampled metric error |
|---:|---:|---:|
| 64 | 1024 | 2.3093e−9 |
| 96 | 1536 | 1.7126e−11 |

The maximum sampled principal curvature remains `5.15734361`. The
geometric agent's continuous local nearest-point check found the rotated
major-core witness distance `≈.7164372345` and the double-mirror diameter
`≈3.057336839`, giving a sampled ratio `≈.234334`. A further exact ruled
strip of widths `.05` and `.1` does not further obscure that witness in
those checks, though it increases the diameter. Those are still surfaces
with boundary. The numerical entry's radial second-jet defect must also be
addressed before treating a finite concatenation as exactly C².

The script searches two scalar linear matching conditions by varying
`W,T,C` and the fraction of inward area spent braking. Its port is the
existing finite linear tail DN, not the fully nonlinear tail. Any root is
only a starting profile for a fresh nonlinear BVP; the turn, actual tail,
closed cap, reach, grip, and all-time phase-family bounds remain separate
obligations.

Direct Cauchy integration of a fast prefix into a positive-curvature turn
has already shown high-mode growth. This is retained in
`alternative-turn-fast035-flat005-m96.json` as a failed finite IVP. A
mixed-type Cauchy instability is not a nonexistence proof, and a discarded
high-mode or filtered solution would not by itself be a fixed-metric
convergence certificate.
