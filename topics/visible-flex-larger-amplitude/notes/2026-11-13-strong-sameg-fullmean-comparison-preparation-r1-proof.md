# Same-g actual spectral comparison with complete independent means

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Prepared interface and scope

`strong_sameg_actual_comparison_complete_mean.py` is a fresh adapter over the
frozen `strong_sameg_actual_comparison.py` (SHA256
`7c152306f09faf7de890377af4f69406677c374ed707b2bc2e391208c8d57f57`).
The preparation run ended with owned `wait4` exit 0. It loaded zero fields,
started no ODE, Node worker or Newton solve, and created no accepted endpoint.
The future M32 endpoint does not yet exist in this preparation record.

The original gates remain in their original function: both endpoints must
be successful and fully audited actual fixed-metric solutions; the coarse
one must be the genuine unchanged fixed view; the fine one must record a
successful same-g spectral refinement. The complete physical profile, tail
parameters and cut, material chart and reference, gauge, physical length,
numerical meridian chart, and shared actual-tail source identities are checked
by the original program. Only the allowed spectrum and representation/IO
differences are admitted.

## The corrected mean convention

The original `compare_shape` used its geometry angular count for all three
mean terms. The fresh adapter supplies, independently for each field,

\[
 N_{\rm mean}(M)=\max\{512,16(3M+1)\}.
\]

Thus the M28 and M32 means use 1360 and 1552 angles. This same field-specific
rule is used for the spanwise Gauss6 antiderivative, the mean of the original
vertical velocity in the first jet, and the mean of its original radial
derivative in the second jet. The actual polynomial state and its first two
physical derivatives are unchanged. The geometry count defaults to 768, and
the independent radial batches are at most 8.

No material-jet formula is changed. In particular, conversion from the
computational chart to physical material derivatives retains the original
rho, chart-velocity and mixed-derivative terms. No angle-dependent or radial
height alignment is applied to remove a difference.

## Sampling and loader identity

The original union of both complete physical node sets, every interval's
midpoint and two second-jet lobe fractions, and the 201 uniform physical
points is retained. The comparisons remain finite samples. They do not by
themselves prove continuous convergence, same-g existence, metric accuracy
between samples, embedding, or reach.

The already frozen initial-laws saved-field loader is reused. It installs
the pulse hook followed by the frontload hook, verifies that each reloaded
physical profile is exactly the saved one, and preserves the original
arithmetic at zero weights. At actual execution, exactly two real fields
must be loaded, and the saved output mean counts must match their own M.

The source preparation checks all six frozen dependency SHA256 values,
requires each source edit to match a unique original site, checks exact
reverse reconstruction of the original function and entry, and parses the
complete transformed code. It does not relax an actual-solution gate.

## Actual use after a genuine fine acceptance

Run this fresh entry with `--coarse` equal to the accepted M28 fixed-view
primary and `--fine` equal to the genuinely accepted M32 same-g primary,
the original `--source-topic` and `--port`, `--angular 768 --batch 8`, and a
fresh `--out`. `--source-dir` may name an independently frozen directory
containing the six exact dependencies. This allows the adapter to remain
outside a mutable repository checkout. A failed fine endpoint must never be
substituted by an initial guess or metadata-only plan.
