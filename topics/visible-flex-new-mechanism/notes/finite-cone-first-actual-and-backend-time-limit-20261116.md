# First finite-cone actual: 25 accepted steps and a final backend time-limit stop

## 1. Scope and observed result

This note consumes the already completed public Actions run [43792959676](https://github.com/Rogerhu12/math-research-public/actions/runs/43792959676), job **133055320913**, source **c0e7336c28b8d1b1f83306e3a0781069f57c0f48**. No science, development checks, geometry, Jacobian, directional oracle, or optimizer was rerun to write it.

The new finite Lorentz-cone method produced **25 newly accepted ordinary full steps**, from source accepted index 27 to index **52**. The maximum of the two actual metric values decreased from **0.26610226672562226** to **0.2660182947853381**, a reported decrease of **0.00008397194028414434**. Both final grids passed all 14 original gate booleans and the exact original physical coefficient box. The target **0.26 remains unmet**.

The run constructed **27 primary models**, started **31 scientific Clarabel calls**, and evaluated **26 actual full steps**. The only actual rejection was model 5. Model 27 stopped before geometry because its one new backend call returned **MaxTime**. The actual finite physical proposal vector from that call is preserved, but it was not passed through the eligible-status repair path or evaluated on either physical grid. This is a backend-status stop, not a proof of stationarity, infeasibility, or exhaustion of the 32-call allowance.

The actual cone method used **0 new HiGHS calls and 0 SOC calls**. The prior 64 HiGHS calls, including its one SOC, remain a closed ancestor ledger.

## 2. Receipt, source closure, and actual rule pulls

All hashes in this table refer to the named original bytes. The JSON rows explicitly include one trailing LF; the decoded log is hashed as received, including its leading BOM and timestamps.

| Original evidence | UTF8 bytes | SHA256 |
|---|---:|---|
| Decoded original job log | 7416045 | a4a20c9f481fc5d8f1fcce7f279c9c8361e5c84d2da7edd324bd9180b97024c0 |
| FINITE_CONE_REQUEST JSON + LF | 30464 | 071fa607bf2fb70a7300876a4b53c669ea520faeb8cfe0a0ad7f6532ec474899 |
| FINITE_CONE_DEVELOPMENT JSON + LF | 2464 | 3e3f8828d6340932c7661f2c35d6aa8da972b45609fcc80759db5e82a9292e75 |
| FINITE_CONE_PRIOR_WORK_REUSED JSON + LF | 2069 | 1cd1679d023e03a470570c4bf5f35b5d7514fd07db43a19a46048afefe48a271 |
| FINITE_CONE_COMPLETE JSON + LF | 3202149 | 8a67d74a139e06c50c6f19e6b265a0c7e5788bd7e6681259712fb8d70a3b189e |
| Model 27 JSON + LF | 84126 | 046520467133e26d2449bfcf1a7aedb7e85b16da3b00e480727706daa567cbb9 |

The submitted request file was **41315 bytes**, SHA256 **340d6f063831331cfa56f9da64785a05f74a60c7d76c9a858be6c63c5563df64**. Its 175 source bindings comprise 164 Python files, 10 workflows, and the one ancestor human cost note. All 164 Python bindings in COMPLETE match the corresponding request entries, with no mismatch. The paid predecessor receipt verifies all 168 old bindings, including 158 Python files, against current bytes.

The science restored the latest completed terminal source only: run 43789033043, job 133043031523, source a08ed9fb3bd44ece17befa23651b281e67f6bb1b. Its source log and MODEL/COMPLETE fingerprints remain in the paid receipt. It did not replay older failed attempts or the old optimizer trajectory. The two necessary source-state restoration evaluations were newly charged, as recorded in Section 10. The 24 necessary original input reports were read once, using the unchanged input argument array.

The actual public pull ran from **02:34:35.890760Z to 02:34:38.756708Z**, from c0e7336c28b8d1b1f83306e3a0781069f57c0f48 to **a6ca911815e8965c37e1a99d41d7a0b15cf078f0**. Both README diffs were empty, return code was 0, and the source was restored after the rule check. The root README blob remained 21bd547f56590b7f2dd279d0297efb289a9b2783; the topic README remained d0432faff569c8e9af7ed4809847e12880976c11. Public git-output bytes were 1161, SHA256 bf9fd7d967b347d7f14d36135361715653d54829852ed6a66bbc49b68126c019.

The actual private pull ran from **02:34:41.339012Z to 02:34:41.897552Z**. Its before/after commit was **d9c989360de427dc418a82695a10c95059675441**. The recorded root README was unchanged, the private topic README was absent as previously recorded, and the session QUEUE entry was unique and ongoing. Private contents were not published.

## 3. First public development checks and paid reuse

The three new groups executed **3 / 4 / 5 checks**, all true, for **12 new checks**:

| Group | Checks | Actual execution scope |
|---|---:|---|
| new_real_clarabel_API | 3 | One true tiny Clarabel solve, pinned version/settings/status/API and analytic scalar solution |
| original161_cone_and_repair_bridge | 4 | Labelled new array fixture, original 161-column assembly, half-cone units, full-rho repair, and finite-vector capture |
| independent_ledger_deadline_and_capture | 5 | New ledger ceilings, dual deadline, charged failures, and post-solve capture boundaries |

The tiny real development call returned Solved with x = 0.9999999999514939, backend solve time 0.000060462 seconds and measured call elapsed 0.00014231399995878746 seconds. Total new development time was **0.011741840000013326 seconds**. It is separate from scientific cone counts.

The development receipt reports one new tiny real call and four stub backend constructors. Scientific research solver calls, ordinary geometry, original parameter-J/JVP calls, and original developer suites were all zero in development. The old eleven release checks and nine geometry checks were consumed from paid receipts and were not executed again.

## 4. Physical and administrative identity

The new objective has an explicit new method identity:

- New objective SHA256: e101bd909dbdb5fb2c7f839b2d416b66e473bf7326dfb80e7af396f3f97a26b6.
- Source objective SHA256: 49c5f2e8a40c076b716c314bd9a3b41f4a0b8cd1ed40b51e0e83c87ce8266888.
- Unchanged configuration: 1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19.
- Unchanged ordinary direct-reference field: 8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1.
- Unchanged selected-J factorization: b6cc198b6b58ec0484438c910a1e05a1273bc0cec81715415b8f538d31661963.
- Unchanged coordinate definition: b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580.

The original g, b0, permanent reference, physical height constraints, 159-to-163 map, box, grids, quadrature order 8, target, gate tolerances, and derivative configuration were preserved. The fresh numerical gate was bound to the actual direct-reference field through the original constructor and assert-context path; its physical rows and height object were not replaced.

The source state was accepted index 27, physical SHA256 bff1348df63200e43bb720e98fa359b057e7370dfbc2090095ba2800803f173c. Its existing pools, versions 8/6, 512-entry bank, eight separate retained supplemental supports, committed learning state, B = 0.000125, and both zero streaks were restored without pool initialization or old event replay.

## 5. All actual model outcomes

The displayed η values are copied from the actual two-grid trial decisions. The rejected row is a measured candidate, not a new accepted point. Every evaluated candidate used α = 1; no SOC or backtracking call occurred.

| Model | Source accepted index | B | Cone calls | Actual α=1 result | Actual η, max of two grids | New rows C/F | Next B |
|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | 27 | 0.000125 | 1 | accepted 28 | 0.2660998088319386 | 1/5 | 0.000125 |
| 2 | 28 | 0.000125 | 1 | accepted 29 | 0.2660964789702438 | 0/0 | 0.000125 |
| 3 | 29 | 0.000125 | 1 | accepted 30 | 0.2660942423318288 | 0/0 | 0.00025 |
| 4 | 30 | 0.00025 | 1 | accepted 31 | 0.2660908623461863 | 0/1 | 0.00025 |
| 5 | 31 | 0.00025 | 1 | rejected; previous accepted retained | 0.2660910921139907 | 1/0 | 0.000125 |
| 6 | 31 | 0.000125 | 1 | accepted 32 | 0.2660892899581480 | 0/0 | 0.000125 |
| 7 | 32 | 0.000125 | 1 | accepted 33 | 0.2660853896043901 | 0/1 | 0.000125 |
| 8 | 33 | 0.000125 | 1 | accepted 34 | 0.2660832299879992 | 0/1 | 0.000125 |
| 9 | 34 | 0.000125 | 1 | accepted 35 | 0.2660809965663937 | 0/0 | 0.000125 |
| 10 | 35 | 0.000125 | 1 | accepted 36 | 0.2660785642159293 | 0/1 | 0.000125 |
| 11 | 36 | 0.000125 | 1 | accepted 37 | 0.2660763288805632 | 5/0 | 0.000125 |
| 12 | 37 | 0.000125 | 1 | accepted 38 | 0.2660741706178415 | 0/0 | 0.000125 |
| 13 | 38 | 0.000125 | 1 | accepted 39 | 0.2660719929222568 | 0/0 | 0.00025 |
| 14 | 39 | 0.00025 | 1 | accepted 40 | 0.2660687902456361 | 0/0 | 0.00025 |
| 15 | 40 | 0.00025 | 1 | accepted 41 | 0.2660645373075936 | 0/0 | 0.00025 |
| 16 | 41 | 0.00025 | 2 | accepted 42 | 0.2660603074225141 | 0/0 | 0.00025 |
| 17 | 42 | 0.00025 | 3 | accepted 43 | 0.2660564733042597 | 0/0 | 0.00025 |
| 18 | 43 | 0.00025 | 1 | accepted 44 | 0.2660515426097285 | 1/0 | 0.00025 |
| 19 | 44 | 0.00025 | 1 | accepted 45 | 0.2660484897706158 | 0/0 | 0.00025 |
| 20 | 45 | 0.00025 | 1 | accepted 46 | 0.2660426793788445 | 0/0 | 0.00025 |
| 21 | 46 | 0.00025 | 1 | accepted 47 | 0.2660398332586794 | 1/0 | 0.00025 |
| 22 | 47 | 0.00025 | 2 | accepted 48 | 0.2660364396758873 | 0/1 | 0.00025 |
| 23 | 48 | 0.00025 | 1 | accepted 49 | 0.2660323516184760 | 0/0 | 0.00025 |
| 24 | 49 | 0.00025 | 1 | accepted 50 | 0.2660282227736336 | 0/0 | 0.00025 |
| 25 | 50 | 0.00025 | 1 | accepted 51 | 0.2660236955506781 | 0/0 | 0.00025 |
| 26 | 51 | 0.00025 | 1 | accepted 52 | 0.2660182947853381 | 0/0 | 0.00025 |
| 27 | 52 | 0.00025 | 1 | no trial; MaxTime status | — | — | 0.00025 retained |

Model 5 had all 14 gate booleans true on both grids, but its fine η was 0.2660910921139907, above the accepted base value 0.2660908623461863. Its actual/predicted ratio was -0.03811849130163429. It learned one coarse soft row and no fine row, returned to the previous accepted point, and the original shrink rule changed B from 0.00025 to 0.000125. No SOC was authorized or attempted.

All 26 physical trials had zero omitted hard rows and all two-grid original gate booleans true. Acceptance still required the original true metric decrease, which correctly rejected model 5.

The returned candidates of models 1–26 met the original full-affine epigraph-gap return criterion and were not returned as inexact cone models. This floating-point return criterion is distinct from a proof of optimality of the backend solve.

## 6. The finite-cone and full-grid separation actually used

Clarabel version **0.11.1** was used with max_iter 200, max_threads 1, tol_gap_abs/tol_gap_rel/tol_feas all 1e-9, and requested time_limit 10 seconds for each scientific call. Other actual backend settings, including reduced-accuracy settings, are retained in every native event.

The 31 backend statuses were **30 AlmostSolved and one MaxTime**; there were no scientific Solved returns. AlmostSolved was an allowed candidate source under the published contract, not an automatic actual acceptance. Each eligible finite vector passed the original linear/bound checks, complete two-grid affine-rho repair, included-cone half-metric residual checks, and then the original actual physical acceptance rules.

All 30 eligible events reported maximum raw and repaired original linear-row and bound violations of 0. The maximum repaired included-cone metric violation was also 0. Signed residuals and direct-versus-half-cone differences remain in the native events; they were not rounded into an exact arithmetic claim.

The original full-grid oracle identified missing finite-cone constraints at four inner steps:

| Model / inner step | Scientific cone ordinal | Original full-affine gap | Evaluated model gain | Newly added exact original cone rows |
|---|---:|---:|---:|---|
| 16 / 0 | 16 | 0.00006174490099548034 | -0.00005594984139711823 | Fine group 1, flat row 206665 |
| 17 / 0 | 18 | 0.000013931809075447277 | -0.000008443653770229265 | Fine group 1, flat row 191151 |
| 17 / 1 | 19 | 0.000011030475810503391 | -0.000005411559178492009 | Fine group 1, flat row 181837 |
| 22 / 0 | 25 | 0.000035726721093116455 | -0.00003179125963048701 | Coarse group 0, row 37095; fine group 0, row 74190 |

The gap tolerance at each of these four failures was 1e-9. The same models then solved the expanded finite cone problem and returned positive repaired candidates. No rejected negative-gain inner vector was physically tried. All prior support rows remained in the current model, including different normals belonging to the same original row.

The final model contained 5760 Lorentz cones, 10167 linear-cone rows including finite bounds, 33207 total assembled rows, 161 variables, and 2302372 CSC nonzeros. Its retained bundle had all 512 bank supports plus all eight supplemental supports.

## 7. Exact stop classification and saved-vector boundary

Model 27 started new cone ordinal **31**, with base accepted index 52, B = 0.00025, and the final pool versions 13/12. Its backend returned MaxTime, while also returning a finite original 161-variable array.

The adapter saved the actual **159 physical step components** before applying the status filter. The event does **not** save the other two auxiliary variables on this failure path. Consequently, this receipt supports exact recovery of the paid physical proposal p, but not recovery of the complete 161-vector, the solver rho, or the solver norm auxiliary.

The event reports:

- Requested backend time limit: 10 seconds.
- Backend-reported solve time: **10.26987467 seconds**.
- Measured solve/metadata elapsed: **10.444304071999909 seconds**.
- Complete adapter-call elapsed: **10.45588942500001 seconds**.
- Backend status: MaxTime.
- Adapter status: backend-status-or-finite-vector-not-eligible.
- No original repair result, full-grid affine evaluation, physical trial, or cone expansion for this final vector.

The outer result was no-returnable-finite-cone-affine-step, and the stage was finite-cone-model-no-returnable-step-not-stationarity. There was still one unused cone-call allowance. The science/value limits were also not exhausted. The stop cannot be relabelled as a stationary point, an infeasible finite cone problem, or a physical rejection of the saved p.

Every scientific backend-reported solve time was between **10.234178444 and 10.424527409 seconds**, despite the configured time limit 10. Actual calls were not forcibly preempted at exactly ten seconds. All elapsed time is charged; this note does not claim wall time at most ten seconds per call.

## 8. Preserved actual vectors and a discovered inherited controller mismatch

The record-existence checks agree with the native data:

| Evidence | Count |
|---|---:|
| Started cone events | 31 |
| Actual finite-return records | 31 |
| Actual exact159 step lists, including MaxTime | 31 |
| Physical trial records | 26 |
| Trial exact159 plus physical163 coordinate lists | 26 |

The original solver-vector flag is supported by actual stored lists, not by a hard-coded success assumption. The final MaxTime proposal is in model 27 at finite_cone_primary.cone_calls[0].new_candidate_step_record.exact_binary64_independent_step. Every successful or filtered finite return remains in its own native MODEL record. Dense A/J arrays were not logged; the complete final checkpoint is emitted once.

An inherited interface mismatch also has an exact observed consequence. The covered-soft ordinary-growth checker in frame_metric_covered_soft_growth.py requires the legacy fields returned_LP_success = true and returned_LP_status = 0. The new conic report deliberately does not impersonate a HiGHS success. Therefore, even models whose other old growth conditions passed returned:

frozen repaired return or original-unit residual gate not passed

from that coverage checker. **All covered-soft qualifications were false**, and no radius change may be credited to that newer covered-growth rule.

The original fallback controller did execute. It doubled B after models 3 and 13; the following models used 0.00025. It consumed old pairs at the cap after models 15, 24, and 26, and it shrank B after model 5. Both terminal streaks are zero. A future conic-specific coverage interface would have to validate the actual backend eligibility and original residuals explicitly; filling fake legacy status fields would misdescribe this run.

## 9. Complete actual gates and final checkpoint

The final gate receipt is the actual accepted trial of model 26, accepted index 52, physical SHA256:

**0c03e09059cac846ec5ab6a246236c52b42d28394930aa35759953ea2ce1fc21**

It was not replaced by a newly executed independent final audit. No extra final geometry call was made.

| Final observed quantity | Coarse | Fine |
|---|---:|---:|
| η | 0.26601808038739305 | 0.2660182947853381 |
| Maximum absolute principal curvature | 57.997683374142156 | 57.999249547251196 |
| Normalized ball radius squared maximum | 0.9905298063857301 | 0.9905298064299818 |
| Inner strip absolute margin | 0.000001439579471518293 | 0.0000014395822110491174 |
| Direct mirror radius minimum | 0.09760999647422229 | 0.09760999647446612 |
| Minimum signed height | 0.02 | 0.02 |
| All 14 original gate booleans | true | true |
| Old metric budget 167/625 | passed | passed |
| New target 13/50 | false | false |

The exact original 163-dimensional physical box passed with no violating index. This is kept distinct from numerical height/ball/strip gate checks and their original tolerances. The reported height-margin minima were -2.7755575615628914e-17 (coarse) and -5.551115123125783e-17 (fine); the unchanged 1e-9 gate tolerance accepted these floating-point values. No exact nonnegative-height-margin claim is made.

Terminal state and reusable information:

- Accepted index 52; B = 0.00025; legacy and covered streaks 0/0.
- Coarse/fine pool sizes **4448 / 4543**, versions **13 / 12**.
- Bank entries **512**; state SHA256 **b240dfd9aad4ea6052eec24590b7147102d1f180be1e9c364f5ba996ed1a47cb**.
- Bank cumulative counters: insertions 4962, evictions 73, inward binary64 adjustments 2562. Insertions include updates and are not a count of distinct new rows.
- Eight supplemental supports remain separate from the bank.
- Learning events **62**, commits **61**, pending **0**.
- Final coefficients γC = **57.187653029922444**, γF = **67.42701956990882**.
- Learning state SHA256 **b076a3436d0b5c2ae4738013314e9b806f7cf90d74712b28fafd2b791ce1ca76**.

The source had 36 events / 35 commits. This run added 26 first-primary samples and 26 commits. The first new sample raised both maxima and was consumed only by the next model; later samples did not further raise those maxima. Models retained their own frozen coefficients and final two-factory binding. The final model modified four fine curvature proposal targets and no coarse target; the original actual gates were unchanged.

## 10. Costs and resource intersection

| Counter or observed time | Value |
|---|---:|
| New scientific cone calls | 31 / 32 |
| New HiGHS calls / new SOC calls | 0 / 0 |
| Closed source HiGHS calls | 64 = 63 primary + 1 SOC |
| New actual values | 54 / 96 |
| Source plus new actual values | 116 / 160 |
| New scientific time, including source/input prepare | 657.9451113929999 s |
| Source final scientific time | 356.129820261 s |
| Cumulative original scientific time | 1014.074931654 s |
| New scientific allowance / original global allowance | 1200 / 1800 s |
| Measured process time | 659.284056995 s |
| Peak RSS on Linux | 7108116 KiB |
| Separate new development time | 0.011741840000013326 s |

The new actual values were two necessary restoration evaluations plus 26 two-grid physical trials. Coarse and fine cumulative counters are each 58. New independent final values are zero.

Timing detail:

- Latest source log read and validation: 3.142032701000005 s.
- Necessary 24 original inputs and immutable prepare: 14.688890893000007 s.
- Total new scientific input/prepare: 17.830967085999987 s.
- New constructor: 0.14821949299999915 s.
- Restoration plus outer execution: 639.8477262680001 s.
- Backend-reported solve times summed over 31 calls: 320.280408173 s.
- Complete adapter-call times summed over 31 calls: 351.7544147459998 s.
- Cone assembly times: 9.638324924000244 s; backend constructor times: 14.08423122899984 s.
- Selected coarse J: 270 batches, 27 refreshes, 0 cache hits, 21.525836378000406 s.
- Selected fine J: 702 batches, 26 refreshes, 1 cache hit, 53.18823345900023 s.

These timing categories have their source-defined scopes and are not all disjoint. They must not be added into a fabricated process total.

The direct-reference adapter observed 54 completed geometry calls and zero failures, total adapter geometry time 141.8758705499999 s. Its first coarse call was 110.166350024 s, including a fixed-height primitive prefix miss of 101.66041931299998 s and reference height-jets miss of 8.328463224000018 s. The following fine call was 18.98784704100001 s, including a scalar-grid miss of 18.66358528699999 s. Later calls reused the same process objects and their original caches. These observed new subcall timings do not identify a causal decomposition of the old 205-second call.

The authoritative final science clocks are the top-level COMPLETE values above. The checkpoint's earlier cumulative value, 1014.070891278 s, and earlier stage/ledger snapshots are not used to reduce the next inherited cost. All previous failed attempts already included in source 356.129820261 s remain counted once. Still older closed m7 costs are preserved separately in the ancestor receipt and do not become available allowance.

## 11. What the result establishes and what comes next

This run establishes that the new finite-cone proposals, original full-grid affine repair, and physical gates produced the listed 25 actual accepted steps with their complete receipts. It does not establish a controlled speed comparison with HiGHS, backend high-accuracy optimality, continuous feasibility between grid points, achievement of η = 0.26, or convergence.

Two concrete issues are now supported by evidence. First, the covered-soft checker needs an explicit conic eligibility interface if it is to operate; its current fallback cannot be advertised as covered-growth success. Second, the final paid physical proposal was filtered solely by MaxTime and has never been physically tried. Its exact159 vector is available, but its rho/norm auxiliaries and an original repair certificate are not.

The next narrow task can therefore be a separately specified validation of that one already-paid physical proposal at the same accepted state, without another cone call or old trial replay. It must keep the MaxTime status and missing-auxiliary boundary explicit, use the original physical box, all original two-grid gates and true metric-decrease requirement, and inherit the actual science/value counters. It must not invent an affine-error prediction, a covered-growth qualification, or a curvature-learning sample requiring an unavailable matching model. The remaining nominal new science is 542.054888607 s; the new value allowance has 42 left, while the original global value allowance has 44 left. The unused cone allowance is not automatically spent. A precise validation contract is the next work, not an unmodified repetition of this 27-model stage.

All full scientific arrays and checkpoints remain in runner stdout or temporary files under the existing no-payload-publication rule. This note contains the human result and its provenance only.
