# Actual63: the nearest rejected trial is limited by midpoint480

- Author: ChatGPT (GPT-6 Astra Pro), amplitude subtask.
- Classification: actual public Actions numerical receipt and read-only provenance checks.
- Status: one improved, unaccepted warm was saved; original fresh boundary FD passed.
- Research completion and complete nonlinear BVP acceptance are not claimed.

## 1. Outcome

Request63 reused the frozen eighteen-query entry at the actual62 warm.
The selected complete-H direction passed the original nonlinear trial
checks at alpha1/128. Its fixed-weight merit decreased from
43.794243580548255 to 43.79041968996707, with saved actual decrease
0.0038238905811880386. The saved actual/predicted ratio is
1.010083304813205.

The nearest rejected trial was alpha1/64. Every existing eighteen-query
angle grid was positive at that trial and all original nodes were valid.
The only original collocation midpoint failure was interval480:
the saved minimum beta squared was -0.011295551381192093 at original
physical-angle index162, with four negative grid values. The original
midpoint RHS was nonfinite, so the full RMS scan was not executed at
this rejected trial. This is a directly observed missing midpoint query;
left-RMS480 is already present and is a different physical station.

The next implementation therefore adds only the original midpoint480
full2048-angle query, beginning from the new actual63 warm. This is a
future nineteenth-query configuration, not an achieved result of that
configuration. No farther failed point is added on the evidence of a
larger rejected trial.

The original numerical observations are preserved in
[the full small readout](2026-11-14-actual63-original-readout.json).
Its 35552 original readout bytes have SHA256
9236a1dc149e3afc976f2675fcfe92fb845c2818249efa21ee64b09f06c5c6ba.
It reads original reports and performs no mathematical reevaluation.

## 2. Actual execution and complete artifact

The public execution is
[run43646179305](https://github.com/Rogerhu12/math-research-public/actions/runs/43646179305),
source commit db6d728f30ee2d0c9ea62c96c622d8d85d2354b2.
The prefix job was132604404966. The original warm, fresh FD, upload and
publisher steps all completed successfully.

The complete artifact is visible-followup-condensedqp-43646179305-1,
artifact14134662698. Its size is494657224 bytes and complete ZIP SHA256 is

c90869cdcc317eef9b23a8a17755a7679ea5ce6dc41c2c143216524b481c6653.

Root downloaded this artifact once and verified the complete size,
ZIP SHA and extraction CRCs before local readout. The observations below
come from those original files. The public report directory is
[the original request63 output](public-actions-43646179305-1-condensedqp/).

The original status elapsed time is618.53620896 seconds. The phase is
actual-full-angle-projection-merit-decreased-unaccepted-warm-saved.
optimization_progress is true and accepted_warm_steps is1. The original
success and new_coupled_finite_acceptance fields remain false. A passing
Actions job here records warm progress and its implementation checks;
it does not turn that warm into a solved nonlinear field.

## 3. Parent and restart pair

The old actual62 pair remains present under parent62 and is preserved
at original bytes. The restart pair from this run is:

| File | Original bytes | SHA256 |
|---|---:|---|
| New eighteen-condensed-warm/warm-001.json.gz | 4799943 | 6934054f06c42ab20bc0401133d91bffe9cf90ca4b8f42c14524091d15f82b0a |
| New eighteen-condensed-warm/driver-status.json | 1810333 | 8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46 |
| Original parent62/warm-001.json.gz | 4792420 | dffaa532026e07357d5115089d968c1be4472c44d9a5f5da25ebcb3e2291ac73 |
| Original parent62/driver-status.json | 1466059 | 4f8239522cef511aca6721ddc9c4541cc9d4e65db3e7260d277b090ad226c054 |

The new original status is larger than the public JSON threshold and
its public gzip alias has231286 bytes. A future consumer must restore
and hash the original1810333 JSON bytes. Parsing and reserializing JSON
is not an equivalent original-byte restoration.

The producer schema is
exact-constraint-eighteen-query-condensed-complete-H-warm-v1.

[The primary identity readback](2026-11-14-actual63-primary-identity-readback.json)
has1773 bytes and SHA256
265e8c76b7e7c6269bc60b9cc152fc4d6d7243e9ca1ba87c59bc5a97066ff953.
It verifies the two original parent byte hashes, the new warm/status
binding, the original FD's new-warm hash, complete canonical producer
equality for FD versus warm, complete parent-producer retention, status
producer subsets, and the original model/status iteration, before and
trial records.

Additional original report identities in that receipt are:

| Original report | Bytes | SHA256 |
|---|---:|---|
| model-000.json | 739340 | 68549fb677c2a255895a3dcef701c4f2e6b25586874e697f63527bb3c65646e0 |
| physical-response/response-check.json | 1060728 | db0bceb142cccac9c68d550917eaf26c93d3a5e98ed8bee76372d64715b762cc |

The primary receipt is a byte/report binding check. It does not claim
that the entire B/condensed/raw array audit has already completed.

## 4. The finite model and implementation were unchanged

This request used the same699 nodes,112 field modes,112 tail modes,
338 physical state entries,453 augmented state entries,236036 reduced
coordinates,109 free core entries and three scalar controls.

The eighteen modeled queries were thirteen original left RMS stations
at intervals467,468,469,470,471,472,473,475,477,479,480,481,482, and five
original collocation midpoints at473,475,477,481,482. Each has all2048
original physical-angle samples. The complete B has36864 rows and
5749 local coordinates: physical nodes467 through483 and all three
global controls.

The baseline C correction still acts only on nodes471 through482 plus
the three controls. The outside contribution of nodes467,468,469,470
and483 is retained in every original affine constraint offset.
The complete-H candidate retains the full outside conditional response;
it does not freeze outside coordinates.

The original damping270, LSMR200, projection200, working-row512,
dual-sweep200, candidate600-second, trial-reserve90-second,
recovery-reserve30-second, total1200-second and original17-trial budgets
were unchanged. The original full domain, fixed-weight merit, boundary,
RMS and fresh FD checks were unchanged.

The actual frozen source identities remain:

| Source | SHA256 |
|---|---|
| geometry_20261114_eighteen_query_domain_operator.py | ec43c049542f523e1c4f2b1956c07a9216497eb066a8f6f22ceddd8f11e2c051 |
| geometry_20261114_eighteen_query_condensed_warm.py | b9f7d9150c57cff485f5f891881870095fc91f7a58fd40f63544e6bb9c3ef335 |
| geometry_20261114_eighteen_query_condensed_response.py | 5885daeced8a8961f7f12d259ed5479683e7fd8dc2cccb8a2873ac9424918c9e |
| geometry_20261114_eighteen_query_collocation_observer_warm.py | 6ad75ce4b350aee4ae52afe2c6045f50d657931419ef7c4b46d0758db3acd1ca |

## 5. The computed quadratic direction

The original C/H comparison uses the same current A, b, damping, B and c.
Its C candidate objective was43.79357494676784. It selected the
R270-condensed complete-H candidate with objective43.54719205984342.

Saved original full-model values for the selected direction are:

| Quantity | Saved value |
|---|---:|
| Actual directional derivative | -0.48526811564111894 |
| Damped model decrease | 0.24705152070483538 |
| Weighted J-direction square | 0.17822912069780125 |
| Damping penalty | 0.29820406917476583 |
| Scaled direction L2 | 0.002022520901748054 |
| Maximum coefficient direction magnitude | 0.00015778990238230725 |
| Final complete linear slack minimum | 5.551115123125783e-17 |
| Final complete negative slack count | 0 |
| Final original stationarity L2 | 1.3101150794789128e-5 |
| Final complementarity sum | 2.893841978133817e-13 |
| R267 cross-point gap, raw floating point | 2.913225216616411e-13 |
| Factor/condensation/QP/recovery helper seconds | 242.84952017199998 |

The local QP reached the512 working-row budget. Its final saved
unrepaired slack minimum was -1.1518563880486e-13 with296 negative
entries and two zeros. The saved local stationarity L2 was
2.8225851567548194e-11. Its worst relative violation was a left-RMS482
row at angle0, with slack -1.4113710200547303e-14.

The local repair factor was0.9999999999816946, and the later complete
global repair factor was0.9999999999684314. The final segment parameter
was1. Thus the selected complete-H direction was not reduced to the
tiny original raw ray; that ray's feasibility factor was
0.00006515616005886902. The C candidate required factor
0.001671825859353917.

These are original floating point diagnostics, not validated R267
enclosures or a nonlinear optimality theorem. They do not provide
evidence that adding working-row budget is the remedy for this run:
the nearest actual failure occurs at an unmodeled original midpoint,
while the final complete modeled linear slacks are nonnegative.

The complete B model identity is
70d341ea175f20479b18ed0a775246f55462aa5fcf8547507314fac8acdf271e.
The condensation model identity is
0d94d3f5c96d082d421bed8c77e148d546e3c4bf922344e3498815dc5c72cd93.
These are this new model's identities; no previous round's fixed
weights or model identity is substituted.

## 6. All eight original trials

All eight trials had zero original node-domain failures and retained the
original uniform-phi density guard with minimum0.16604058243274977.
The failures below are the saved original midpoint readouts.

| Alpha | Original bad midpoints | Failed modeled query grids | Outcome |
|---:|---|---|---|
| 1 | 475,481,482,485,486 | All thirteen left RMS grids; mid475,481,482 | Rejected before finite merit/RMS acceptance |
| 1/2 | 480,481 | left467,left481,mid481 | Rejected before finite merit/RMS acceptance |
| 1/4 | 485 | None of the eighteen | Rejected at original midpoint RHS |
| 1/8 | 480 | None of the eighteen | Rejected at original midpoint RHS |
| 1/16 | 480 | None of the eighteen | Rejected at original midpoint RHS |
| 1/32 | 480,484 | None of the eighteen | Rejected at original midpoint RHS |
| 1/64 | 480 | None of the eighteen | Nearest rejected trial |
| 1/128 | None | None of the eighteen | Accepted after all original checks |

A nonfinite original midpoint RHS prevents claiming a finite actual
merit for the rejected trials. Their positive predicted model reductions
are predictions, not actual merit measurements. In particular, the
nearest rejected trial did not run the full original RMS scan.

For alpha1/64 the saved selected linear beta minimum was
0.0015534750239719333 and linear reserve-slack minimum was
0.0007706214685845028. All36864 modeled linear rows and all eighteen
actual selected grids were positive. Nevertheless the original,
unmodeled midpoint480 had minimum beta squared
-0.011295551381192093 at phi0.4970097752749477, angle index162, and
four negative grid values. Its finite original middle input produced
a nonfinite original RHS.

This nearest-trial evidence concerns midpoint480 at station
1.2217769947388337. It does not replace or identify that station with
the left RMS station in interval480.

For the accepted alpha1/128:

| Quantity | Saved value |
|---|---:|
| Predicted unregularized merit decrease | 0.0037857180323311963 |
| Actual fixed-weight merit | 43.79041968996707 |
| Actual merit decrease | 0.0038238905811880386 |
| Actual/predicted ratio | 1.010083304813205 |
| Complete boundary maximum | 3.2903722327075875e-8 |
| Physical collocation maximum | 0.0071092556155250685 |
| Left residual maximum | 0 |
| Constant-state collocation maximum | 0 |
| Selected linear beta minimum | 0.0015595910673733972 |
| Selected reserve-slack minimum | 0.0007767375119859666 |

The accepted trial had zero original midpoint failures and zero invalid
points in each complete698-point RMS scan, at fractions
0.17267316464601146 and0.8273268353539885. It preserved identical
core states and identical control states across all nodes.

The fixed weights were rebuilt for this model. The reported merit is
compared only with this model's43.794243580548255 baseline, not with
the numerical merit printed at the end of request62.

## 7. The largest original collocation entry remains identified

The original read-only observer still locates the largest physical
collocation entry at interval461, radial mode1, angular frequency2,
original residual row155819. Its signed value moved from
-0.007109265719764634 at this model's base to
-0.0071092556155250685 at the accepted warm.

The actual frozen row weight is199.05455376436257. Its weight-array
identity is
c202abb587c2422ce33466befb85377c3c03bfb705898e3c11b2deabf3104a0c.
It is the original base-state weight retained throughout the trials;
it was not recomputed from each trial's midpoint RHS.

The observer records16 original evaluate calls, one original weight
call and zero observer errors. It changes no original return array,
finite flag, merit or acceptance decision.

Interval461 lies outside the selected B support, but the complete
collocation residual and its row weight remain in the original A,
and the complete-H condensation retains the outside affine response.
The slow improvement of this single entry cannot be described as a
zero weight or an omitted equation. A small quadratic stationarity
diagnostic also does not by itself imply fast decrease of the largest
nonlinear collocation entry.

## 8. Fresh FD, and its precise finite scope

The original complete physical-angle boundary FD was rerun on the new
warm6934054f... and retained its entire actual producer identity.

Its maximum fourth-order Richardson relative error is
7.094809478749229e-10. Its maximum second-order relative error is
9.883371804776467e-6, with the original second-order contraction flag
true. The original5e-5 threshold passed. The original left/right
off-block Jacobian maximum remains0. The saved FD elapsed time is
21.569843381000055 seconds.

The reference is the completed real T112 zero-height Jacobian,
SHA e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51,
held explicitly affine with the original tail configuration,
SHA01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5.
The ready linear graph was not substituted. The new warm's H is not
the anchor H, and this FD is not a new nonlinear native tail solve.

No complete nonlinear BVP, same-metric refinement, closed Cartesian
surface, whole-image held amplitude, or final geometric certification
is inferred from this warm/FD receipt.

## 9. Audit scope at this publication

Completed work for this note is the original entire ZIP size/SHA/CRC
verification, original report readout, the exact parent and new-pair
byte hashes, and complete canonical producer/status/FD/model binding.
The two small readout JSON files linked above record this scope.

The generic read-only Actions byte reader is prepared separately. Its
later full-domain NPZ, condensed arrays, declared raw files, source-ledger
and midpoint-payload results must be recorded as their actual execution
results. This note does not predeclare those counts or claim their
success. A byte-readout step is not a second mathematical solve or an
extra nonlinear acceptance gate.

The original complete QR factor arrays were not exported; no independent
full-factor file audit is claimed.

## 10. Immediate continuation

The next source change is independent of the frozen eighteen-query
sources and adds exactly midpoint480 to the existing eighteen grids.
Both endpoints480 and481 are already in the original captured node
set, so the complete local support stays at nodes467 through483 plus
the three controls, dimension5749. The full row count becomes38912.

The original left-RMS480 grid remains present as a separate typed query.
The baseline C dimension4059, every outside affine offset, complete
original-H recovery, damping270,512 working rows,200 dual sweeps, all
budgets, all original trials and checks, and actual new-warm FD remain
unchanged. The new parent is the actual63 warm/status pair above.

This is the next executable design supported by the nearest original
failure. It is not evidence that the next full step will pass or that
the research completion criteria have been met.

