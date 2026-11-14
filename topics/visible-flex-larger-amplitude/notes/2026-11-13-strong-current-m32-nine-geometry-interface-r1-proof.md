# Accepted-point M32 geometry interface with a ninth synchronization control

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Source preparation and API/units conclusion.** The actual source-only run
passed 18 identity and interface checks, with owned exit 0 in 1.514215112 s and
peak RSS 63,344 KiB. It created no geometry field, future accepted package,
response column, BVP, ODE or Node worker. No value at the pending A endpoint is
asserted. The original q122 fields and historical negative warm outcomes remain
unchanged.

## The control is an existing physical parameter

The original `alternative-neck-provider.py` passes
`descending_sync_curvature` to
`turn(-asin(vd),-asin(loop_speed),Ksync)`. The original flat-turn provider uses

\[
 L_{\rm sync}=
 \frac{|\arcsin(v_{\rm loop})-\arcsin(v_d)|}{K_{\rm sync}(1-\epsilon)},
 \qquad \epsilon=0.08.
\]

The actual binary constants and original formula are retained. Ksync has units
of phase radians per physical meridian length. With both endpoint speeds fixed,
its direct length derivative is `-Lsync/Ksync`. This identity explains what the
parameter changes; it does not predict the coupled field's curvature or size.
The entire physical profile, chart, mean and field are reevaluated for every
finite candidate, including all compensation in the original three physical
controls.

The original fixed-J producer differentiates an external physical parameter at
`h=2e-6*max(.1,abs(current value))` and `h/2`. If the eventual actual Ksync is 2,
these are 4e-6 and 2e-6. The proposed geometry stencil of +/-0.002 is a separate
finite warm step. It does not replace either response forcing step or claim a
bound on a nonlinear remainder.

For the core-held Ksync direction, the original producer forms
`source + Z*du`, where `du` solves the same current 3x3 low-core exchange.
Consequently the physical Ksync derivative is one, delta/boost length/boost
speed compensate it, and the three prescribed core coefficients have zero
first derivative up to the actually reported numerical error. All 32 core
coordinates and the complete shooting-state derivative remain present. The
new response observations, including combined half-step differences, must come
from the actual new job; the previous partial recovery is not accepted as this
new full response.

## Source adapters and complete data path

The external response order is
`delta, boost_length, boost_speed, vu, descending_turn_curvature,
start_acceleration, initial_speed_frontload, vd, descending_sync_curvature`.
After the original exchange the design order is
`actual_q1, actual_q4, actual_c6` followed by the six neutral parameters in the
same order. The existing variable-control validators already permit these
nine directions, so no minimax or geometric formula was changed.

The fresh planner delegates to the frozen complete-mean planner and explicitly
selects the corrected anchor provider `583af82c…`. Its modifications are listed
and exactly reversible. It requires a genuinely processed M32 accepted package
and a quintic witness whose input SHA is that same fixed-view package. The
baseline-only plan can be created before the response finishes. The full plan
must reuse that baseline command and grid verbatim, and adds the eighteen
positive/negative cases only after the complete nine-column response exists.

The mean is the original M32 rule of 1,552 angles for height and its first two
radial derivatives. Geometry uses at least the complete 768-angle grid. Every
current raw node, physical chart anchor and current quintic witness is retained.
The planned cases use the owned foreground resource wrapper. The original
strict chart, physical domain, positivity and finite-field checks remain in
force. No identity bridge for a failed chart is preemptively granted.

The fresh reader verifies nineteen actual completed fields, their true outer
provider preparation and the inner complete-mean producer SHA separately.
It preserves exact historical source labels, checks all current input paths,
all 32 core coordinates, the common mean/grid, every chunk SHA and complete
radial coverage. It then calls the unchanged full-array reader. The original
finite minimax retains all five row families, namely four signed principal
curvature rows and one size row at every actual point. With R radial samples
and A angles, the row count is exactly `5*R*A`; it is not hard-coded to the old
q122 grid size.

The fresh combined-plan adapter keeps the original simultaneous-control warm
constructor and all model/response checks. Its only additional command edits
give the chosen combined case its own heartbeat, ownership and resource names.
The true production BVP, tail and accepted audit remain separate obligations.
No old M28 geometric slope, padded coarse derivative or stale accepted-point
increment is used by this current-point path.

## Execution contract

First wait for A's original owned acceptance, fixed-view conversion and the
full-mean quintic audit of that same view. Prepare the unique baseline with
`root_actual_geometry_anchor_current_plan.py --baseline-only`, explicit nine
positive stencil steps and the actual saved paths. Evaluate it once. When the
one current full-J/QR response completes, prepare the full plan with the same
prefix, grid, witness and steps, adding `--response-data` and omitting
`--baseline-only`. Execute only its eighteen new cases.

`root_geometry_anchor_current_reader.py` can verify the full actual dataset
and then pass the unchanged current-control LP arguments. A selected actual
finite prediction is converted to a new combined warm plan with
`root_geometry_anchor_current_combined_plan.py`. The output of this source
preparation is not a plan populated with guessed A values and not a scientific
result for the nineteen as-yet uncomputed fields.
