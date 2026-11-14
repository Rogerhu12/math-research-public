# R133 supplement: actual complete analytic Airy old-circle source budgets

2026-11-14, phase_inverse.

**Actual public result.** Run
[43634456797, attempt 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43634456797)
completed with mathematical return code zero and all **10 gates passed**.
It reused all 1328 original moment rows and all 1328 complete directed
matrix rows without recalculation, evaluated six new complete analytic
amplitude bounds, and accepted all 4377 radius-specific source-integral
rows. The mathematical child took **20.664579579999995 seconds**.

The new analytic construction improves some of the large-window
negative source bounds. Its smallest-window bound is worse than the
previous independently proved directed-matrix bound. Both complete
results remain valid. Neither establishes a useful cutoff-97
strong-return inverse.

## 1. Immutable actual process

The event commit is
$86eb613ed6c1fae0c813b42f60103441a687ed41$ and the separately
recorded actual scientific checkout is
$1a0504e2c18bfb39640e2b288776376603202322$.

The complete new native is
[analytic-Airy-old-circle-sources.json.gz](../notes/analytic_Airy_old_circle_sources_ci/run-43634456797-1/consumers/analytic-Airy-old-circle-sources.json.gz),
3445399 bytes, SHA256

```text
e54f05c3eea0e2ed9a8f7511004059b730b448adb26c9e035cc1803325080db8
```

The entire small
[process record](../notes/analytic_Airy_old_circle_sources_ci/run-43634456797-1/consumers/process.json)
was read after its 51260-byte size was checked. Its SHA256 is

```text
e0fa6ba5f68e6520f0e2944052d344ff3ffe9e97dacc8e2a3022ff36e00f52ec
```

The actual
[worker record](../notes/analytic_Airy_old_circle_sources_ci/run-43634456797-1/worker-process.json)
has 2996 bytes and SHA256

```text
cc974d20629e8787e67379dc763d0e02598994fd233bf13ddda619c94e976283
```

The scientific producer is
[fourfold_codazzi_analytic_Airy_old_circle_sources.py](../scripts/fourfold_codazzi_analytic_Airy_old_circle_sources.py),
SHA256

```text
439a29e2f1a3273bf9901d6a6ddfae075fb88a308d9a9e2a665cf839fc3e0dc7
```

and the
[exact 25-file manifest](../notes/2026-11-14-R133-analytic-Airy-old-circle-sources-CI-inputs.json)
has SHA256

```text
ee066de1b0328b6ede8b2a928680548065f6a8d1ad7d678f3ca515febf834e37
```

All 20 pins of the prior directed-matrix input manifest remain
byte-for-byte unchanged. The new inputs are two proved analytic
contracts, the new producer/driver and the original actual
directed-matrix process.

The completed original directed native from run 43632464994 is
7873296 bytes, SHA256

```text
3c8c4f3c93108de5a1c17149518f3aa16500a7f8ad58343f7a8dac325cc48d4b
```

Its original complete artifact was restored and checked. The two
original large root/forcing artifacts and the two completed repository
natives were likewise checked by exact SHA and size. No binary input
was manufactured or split.

Both actual worker pulls have recorded empty root/topic README
diffs: the first leaves
$1a0504e2c18bfb39640e2b288776376603202322$ unchanged; the second
advances to $c06050debf6de9add5ecad03d273342d71c116cb$.

## 2. What was newly bounded

The proved inputs are
[complete exponential Fourier bounds for actual Airy columns](R133-supplement-analytic-Airy-columns-and-complete-exponential-Fourier-bound.md)
and
[direct angular matrix jets](R133-supplement-direct-angular-matrix-jets-for-analytic-Airy-sources.md).
The full ordered matrix words remain those of
[the already completed directed-matrix calculation](R133-supplement-actual-directed-matrix-old-circle-sources.md).

The actual real family remains $|\delta|\le10^{-8}$, intrinsic
$\eta_0$, the exact repaired centre and the same full 193-component
direction. The physical input frequency is $n=4|j|$, $|j|\ge97$.
Every old mean and every Fourier output, including output zero,
is retained.

Each radius now uses the original complete leading strip $3/64$,
its genuine inverse phase strip $(2-E)3/64$, the exact two-by-two
$H^{-1},H_D$ derivative matrices and both Airy components separately.
Only angular order two and the already paid mixed radial-angular
derivative are required; no angular Cauchy loss is charged.

The actual Fourier factor sums every nonzero lag below 97 and
an exact geometric majorant for the complete infinite tail from
lag 97. It does not discard the mean-output diagonal.

| Radius | Inverse phase strip, strict lower bound | Complete Fourier factor, strict upper bound | Composition factor, strict upper bound |
|---|---:|---:|---:|
| $1/1000$ | $0.04687028246911$ | $1.626181843730$ | $1.580897189717$ |
| $1/500$ | $0.04686156846759$ | $1.626520087867$ | $1.581666296412$ |
| $1/200$ | $0.04680504678570$ | $1.628717639105$ | $1.587909231823$ |
| $1/100$ | $0.04663563636234$ | $1.635341868066$ | $1.617706641928$ |
| $3/200$ | $0.04647811720842$ | $1.641552273305$ | $1.661811069098$ |
| $1/50$ | $0.04634507760236$ | $1.646836457223$ | $1.715834155225$ |

Every full amplitude tensor is saved before its first source
integration row. A later identical-input continuation can decode
that completed tensor and continue its integral prefix without
repeating the accepted amplitude calculation.

## 3. Complete actual source norms

The source map is
$$
 H^{-4/3}\longrightarrow
 L^2_r(H^{-2/3}\times H^{-2/3}).
$$
Its second row is purely the independent even mean, for which
the $H^{-2/3}$ and $H^{-1}$ norms coincide. The true root interval,
six complete radial covers and positive collar/body cut are
identical to the previous calculation.

All displayed source numbers are outward-rounded upper bounds.
The old and new negative columns are complete alternative
estimates on the same respective domain, so the smaller of
those two proved bounds is available. This does not change any
native record or any previous result.

| Radius | Actual integral rows | Previous directed negative source | New analytic negative source | New positive collar source | New positive body source |
|---|---:|---:|---:|---:|---:|
| $1/1000$ | 144 | $4.564909\,10^9$ | $3.385779\,10^{10}$ | $1.009055\,10^{10}$ | $3.153275\,10^{10}$ |
| $1/500$ | 274 | $1.577147\,10^{10}$ | $4.353811\,10^{10}$ | $1.038492\,10^{10}$ | $3.971666\,10^{10}$ |
| $1/200$ | 627 | $1.251183\,10^{11}$ | $7.598446\,10^{10}$ | $1.213894\,10^{10}$ | $6.044417\,10^{10}$ |
| $1/100$ | 898 | $7.517754\,10^{11}$ | $1.800352\,10^{11}$ | $1.909334\,10^{10}$ | $1.152247\,10^{11}$ |
| $3/200$ | 1106 | $1.900161\,10^{12}$ | $3.999022\,10^{11}$ | $3.415563\,10^{10}$ | $2.316172\,10^{11}$ |
| $1/50$ | 1328 | $3.453706\,10^{12}$ | $7.109141\,10^{11}$ | $5.456540\,10^{10}$ | $4.038805\,10^{11}$ |

Applying the unchanged actual complete negative source-to-primitive
map to the new negative sources gives:

| Radius | New negative component after the actual primitive/Cauchy map |
|---|---:|
| $1/1000$ | $5.131877\,10^9$ |
| $1/500$ | $1.112693\,10^{10}$ |
| $1/200$ | $6.056720\,10^{10}$ |
| $1/100$ | $9.428426\,10^{11}$ |
| $3/200$ | $1.441660\,10^{13}$ |
| $1/50$ | $1.569986\,10^{14}$ |

The positive columns are raw sources before the positive-to-root
map. The given-head positive high graph alone does not invert
the independent even-mean equation.

## 4. Dominant source and the next mathematical distinction

At the smallest radius the complete $R_QJ T(g_d)$ contribution
has negative ordinary-source bound
$3.000215007\,10^{10}$. The complete $S_V$ term is bounded by
$2.827759064\,10^9$.
The original raw-$D$ mean is separately bounded by $463828$.
No term disappeared because it was inconveniently large.

The complete infinite Fourier-tail factor at that radius is
less than $0.000448747753567$; this is a component of the
factor $1.626181843730$, not a dropped error.
The central Airy entire-function estimate also retains the
whole complex phase range. Its dependence on the radial
upper/lower ratio can be conservative even when the actual
angular variation is small. Improving that estimate requires
a new proved profile bound and an actual consumer; it cannot
be inferred merely from the successful ten-gate execution.

The native truthfully records zero new target, coefficient,
ray, original moment, directed-matrix or amplitude-equation
solves. Its six new calculations are analytic amplitude norm
bounds, followed by the true source integrals. All 1079 original
seams and every already completed source remain unchanged.

The local $\mathcal L_0w_1$ budget, old inverse remainder on
$w_1$, complete propagated correction, finite head and actual
strong-return smallness are still separate obligations.
The flags for a complete numerical strong-return norm,
cutoff-97 inverse and true PDE branch remain false.
