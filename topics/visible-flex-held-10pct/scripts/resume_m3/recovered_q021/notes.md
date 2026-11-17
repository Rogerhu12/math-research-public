# Second genuine m3 coupled amplitude, q = .021

This package records an accepted **design-amplitude** continuation from the
actual fixed-g radial2 q02 prefix/tail pair. Both the complete nonlinear mean
and every represented nonzero mode are included in the original tail DN.
The prefix delta is solved again, so this is a new physical metric, not a
fixed-metric refinement. Its purpose is to provide a second genuinely coupled
field for subsequent continuation.

## Accepted result

The original M8 prefix BVP used 743 nodes and reached maximum collocation RMS
`9.937745973504893e-7` at its original `1e-6` tolerance. The actual amplitude is
exactly `.021` in this design formulation. The new delta is
`.061055934246436315`; the input delta was `.06105607686781097`.

The first actual nonlinear-DN outer check accepted at normalized boundary
residual `8.540069141918627e-10`, corresponding to physical nonmean derivative
mismatch `1.7080138283837253e-11`. Its actual tail shooting residual was
`9.949141046367904e-10`. The final independently requested audit response
remained below the same original `2e-9` gate at
`1.8654639461939814e-9`. No acceptance tolerance or projection floor was lowered.

| Quantity | Recorded value |
| --- | ---: |
| Prefix sampled metric FFT l1 | 2.893656053460158e-8 |
| Prefix sampled Cartesian Darboux tensor | 3.3567160251287467e-4 |
| Prefix sampled principal curvature magnitude | 8.083305748996843 |
| Prefix maximum radial coordinate | 1.0710325349947085 |
| Prefix maximum height | .7859389236766786 |
| Tail sampled actual metric | 6.500828764188805e-10 |
| Tail sampled full D defect | 4.756889928589278e-6 |
| Tail minimum A at the accepted state | .41029955547542823 |
| Tail minimum D at the accepted state | .9997117455260914 |
| Tail sampled formal curvature | 8.044950847823886 |
| Mean height first-jet mismatch | 1.749637518200231e-10 |
| Mean height second-jet mismatch | -4.0995102867924516e-9 |
| Nonmean height second-jet mismatch | 3.77783907659766e-10 |

The tensor is the actual saved C2 interpolant's tensor; it was not replaced
by the much smaller ODE-node residual. This deliberately coarse design result
has not yet received a new full Cartesian seam audit, literal closed C2 map,
continuous reach enclosure, fixed-metric convergence study, or marker. It is
not the completed 10 percent construction.

## Exact computation and reproducibility

The physical tail remains the original spacing-three smallcut tail with
`rCut=.3`, `wCut=.08`, width `.25`, curvature bound `8`, orientation `+1`, the
original six nonzero valley controls and 160 protected controls. All those
physical constants are in `tail-settings.json`; its finite zero extension is
made by the replay script. Numerical tail settings are M8, N128, depth8,
shootingParts8, 16 RK steps per substage, original solve tolerance `2e-9` and
36 original Newton iterations. The canonical first eight linear DN columns
were regenerated from this actual worker and agree exactly with the M16
startup's first eight columns. No DN data are stored in this package.

The original material-angle restart projected the accepted radial2 M16
prefix to the target M8 numerical representation. The original tail warm
remesher similarly used the accepted complete M16 state. The original prefix
and nonlinear tail residuals, means, Jacobians, local guards, and acceptance
checks then solved the new problem. The coupling uses actual upper prefix
height H with worker input -H and reflects the entire worker height, including
its nonlinear mean, back to the upper geometry.

Recover the 70 original m3 source files and apply the already published
sparse-v2 stage transformation and helper. Regenerate the accepted radial2
pair using the previous fixed-M16 and radial-refinement packages. Then run:

```sh
python replay.py --source-topic RECOVERED_TOPIC \
  --short-bridge RECOVERED_ROOT_SHORT_BRIDGE_PY \
  --sparse-helper SPARSE_SHOOTING_LINEAR_PY --chart CHART_JSON \
  --prefix-restart RADIAL2_PREFIX_JSON_GZ \
  --tail-restart RADIAL2_TAIL_0004_JSON_GZ --outdir NEW_OUTPUT_DIRECTORY
```

`replay.py` checks the recorded source and warm-input hashes, regenerates the
linear startup port through the original worker, adds only the explicit
ShortBridge metadata, and launches the original coupler. All original argv,
source hashes and output hashes are in `record.json`. Output file metadata may
depend on the replay paths; the physical parameters, equations and numerical
gates are explicit. Regenerable fields, DN vectors and checkpoint arrays are
omitted under root README rule 15.

## Relationship to unsuccessful initial guesses

The earlier q025 trials concerned one prescribed height vector obtained by
scaling an initial prefix guess. This accepted q021 state pays the actual
nonlinear DN and changes the full higher-harmonic height vector. It supplies
new information for a material-angle field secant. Neither the earlier
initialization failures nor this successful small step establish an upper
amplitude bound. The separate M16 q021 design attempt was still active,
without a terminal result, when this package was frozen.
