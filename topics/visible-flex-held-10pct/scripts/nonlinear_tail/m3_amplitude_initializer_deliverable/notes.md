# Why the first q=.025 warm initialization stopped

**Finite numerical diagnostic, not a capacity bound.** The accepted
fixed-g q≈.020001546 M16/parts8 pair supplied the warm state for a design
continuation with gauge amplitude .025. The complete signed height vector
was sent to the actual nonlinear tail. Its first request stopped inside
the local momentum-root Newton solver before a complete shooting
evaluation. Therefore no global shooting residual or prefix solve exists
for that attempt.

The saved failure is exactly reproduced by the attached diagnostic using
the original worker's remeshing, common amplitude scaling and complete
linear boundary correction. No equation or guard is modified.

## What the reproduction identifies

The new height is the old height times 1.2499033683549081, up to projection
roundoff below 1.1e-20 in each coefficient. The worker's harmonic-amplitude
predictor is **not active for this full multimode vector**; its code only
uses that predictor when every higher input mode is exactly zero. The
explicit linear cut correction has maximum relative size 3.14e-12 among
all stored node states. Thus this particular failure is not explained by
a missing material-angle pullback or a newly introduced large high mode.

The first failing flow is stage38, physical cell0, segment4, raw segment
interval [.125,.25]. Its failure is at the RK b midpoint of step12, local
stage x=.78125, radius .2447882536 and slope .00116526602. The complete
first 38 stages were evaluated successfully.

At that one failing intermediate state, an explicit amplitude homotopy
uses the previous local root as the next root's initial guess, with the
original D/S/A guards and tolerances. It reaches lambda .9979912745 with
minimum A=.0500026714 and D=.9999970741. Further attempted steps meet the
original numerical A floor .05. The experiment never reaches the full
intermediate state. It does not establish A=0, a geometric singularity,
the capacity of the genuine nonlinear branch, or nonexistence at q=.025.
The intermediate RK state belongs to an inconsistent scaled warm guess,
not to an accepted tail.

The next trial uses the original accepted pair with the smaller target
q=.021. At the time of this frozen diagnostic it has entered global
Newton and its residual has decreased from 683 to 164 to 9.49 while
minimum A stays above .39. That run is active and has no terminal claim
in this package. No iteration limit or original acceptance condition was
changed in response to the q=.025 failure.

## Reproduction

Regenerate the accepted refined pair from the radial-refinement package,
then run the q=.025 command in `record.json` using the same sparse source
copy. The two compressed responses remain runtime data. Invoke:

```text
node audit_m3_warm_initializer.mjs SOURCE_TOPIC ACCEPTED_Q02_RESPONSE \
  FAILED_Q025_RESPONSE OUTPUT_JSON
```

The output includes the full scalar homotopy trace in scratch. This
package keeps its hash and compact diagnostic values only, together with
code and the exact trial command. It contains no Fourier vector,
checkpoint, DN array or sampled field.
