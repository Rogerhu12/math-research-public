# Actual nonlinear prefix–tail coupling at support amplitude 0.02

This is a finite numerical coupling result, not a completed closed surface or a
reach certificate. It continues the genuine nonlinear `q_support=0.01` branch;
the meridian parameter is solved again, so the two amplitudes are **different
metric designs**, not a fixed-metric convergence test.

## Reproduction and fixed inputs

The sequential runner is `scripts/950f-prefix-coupled-continue.py`, using
`scripts/950f-prefix-nonlinear-coupling-v2.py` and the weighted tail client v2.
The precise command, configurations, source hashes, complete coefficient
checkpoint, and all 24 tail calls are retained in
`2026-11-09-950f-prefix-coupled-v2-m8-q0p02*` and in the master continuation
summary. The solver keeps 8 threefold modes, uses the 256-point computational
angle grid, and audits with 512 angular points. The prefix tolerance is
`2e-7`; the actual finite tail has physical depth 10 and two shooting parts
per profile. The adaptive chart reference is `q_reference=0.02`; the change
of reference from the previous stage uses an explicit material-angle map.

## Result

After 745.75 seconds and 24 nonlinear tail requests, the BVP solver reports
success at

\[
q_{\rm support}=0.02,\qquad
\delta=0.07253060255757607.
\]

The prefix diagnostics are:

| Quantity | Value |
|---|---:|
| Sampled Fourier metric diagnostic | `2.9991757668921935e-9` |
| Flow residual | `4.458020094892163e-9` |
| Darboux residual | `3.102560943043592e-5` |
| Sampled maximum principal curvature | `5.55754923386062` |

The final actual nonlinear tail call is
`2026-11-09-950f-prefix-coupled-v2-m8-q0p02_tail_0024.json.gz`.
Its first input height coefficient is `-0.0003177732845903674` and its second
is `-1.281284079438985e-6`; the full vector is stored in that record. Its
shooting residual is `2.391260918143806e-11`. The sampled finite-tail audit
reports metric error `1.7297319132584352e-10`, full Darboux residual
`3.351924158101781e-7`, minimum leading coefficient
`0.8034568255787167`, minimum Darboux quantity `0.996652196434162`, and formal
curvature `6.137388304948253`. The growing full-Darboux residual, compared
with the smaller-amplitude run, is a reason to refine angular resolution
before a final candidate can be accepted.

## Full height-jet seam diagnostics

The cut chart is the identity through second order. With the stored sign and
arclength conversions, the measured mean first-height-jet difference is
`-9.32653954066609e-12`; the mean second-height-jet difference is
`1.1679812672582557e-10`. The maximum nonconstant first-height-jet difference
is `1.6024561574691578e-17` and the corresponding second-height-jet difference
is `6.3649365248998e-13`. The sampled Fourier diagnostic for the cut C1 metric
error is `7.193721706705921e-11`.

These are numerical checks of both mean and nonconstant jets; they do not
replace the conditional cut-mean uniqueness lemma or an exact Cartesian C2
seam. They also do not establish infinite-tail convergence, embedding,
continuous-angle estimates, held displacement, or reach. The runner proceeds
to larger support amplitudes using this full nonlinear tail state as its warm
start.
