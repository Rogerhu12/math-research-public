# Actual76: quarter-step decrease; the nearest rejection also violates an existing query

**Classification:** numerical evidence from the original public Actions output, plus byte/provenance checks of its published primary files. No scientific calculation was performed locally. This is an optimization warm step, not an accepted complete BVP, nonlinear native tail, or closed surface.

**Author:** amplitude branch of the visible-flex-larger-amplitude session, 2026-11-15 UTC.

## 1. Actual result and identity

[Run 43661532089](https://github.com/Rogerhu12/math-research-public/actions/runs/43661532089), source `1377826d89317b491f75036cafd63c3ea5bea5f1`, job `132651746146`, completed successfully. The original warm, original complete boundary finite-difference check, artifact upload, and publisher steps all succeeded. The actual warm accepted $\alpha=1/4$ after two rejected trials.

The new model's fixed-weight merit changed from `43.67031770334245` to `43.57938353308094`. The original producer saved decrease `0.09093417026150519`, prediction `0.09159763451120578`, and actual/predicted ratio `0.9927567534550313`. All 24 selected query grids and the complete original node, midpoint, and both 698-point RMS query checks passed at the accepted trial. The new warm's original boundary FD saved maximum fourth-order relative error `8.532100047207813e-10`, under the unchanged `5e-5` implementation threshold.

The producer still saved `success: false`, `new_coupled_finite_acceptance: false`, and `optimization_progress: true`. No actual native solve at the new height was performed. The warm phase took `456.52919002199997` seconds; its FD took `16.08357167099996` seconds.

The complete science artifact metadata is:

```text
artifact: 14140726714
name: visible-followup-condensedqp-43661532089-1
ZIP bytes: 640977134
ZIP SHA256: b57824ec8cb6ef22525966725fd333c4dfb1a0111aa403ccf54117d02ab7289c
```

These ZIP values are the GitHub artifact metadata. This primary readback used the exact published files fetched by the root agent; it did not download or audit the complete science archive.

## 2. What this model contains

Actual76 starts from actual74 warm SHA `204b208393218923f8abf9a36b6f03d29306409155447f561b2c2f4c373001a3`, paired with its original decoded status SHA `09d944723fb6be152e90ba283fc44d33d455f1a52bc73787a329fcdc7d97ea73`. The complete previous producer subtree is retained. Its one new query is the original left RMS query in interval 485, the nearest actual74 limitation; it retains the separate existing midpoint485 query.

The 24 query grids are 16 left RMS grids at intervals

```text
466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485
```

and eight original collocation-midpoint grids at

```text
473,475,477,480,481,482,484,485.
```

Each grid contains all original 2048 physical-angle samples: 49,152 inequality rows in total. The actual and declared local column sets both contain all physical variables at nodes 466 through 486 and the three shared controls, for 7,101 columns; the zero-layout set is empty. The complete physical/core/control model still has 236,036 coordinates. The original C baseline retains its 4,059-column support and complete outside offsets. Complete-H recovery preserves the affine optimum of exterior variables and the 109 free core variables; it does not freeze them to the raw LSMR direction.

The model uses the original $\lambda=270$, 512 working-row budget, 200 dual sweeps, original trial sequence, original full domain/merit rules, and original response checks. The model weights are newly fixed at actual74's saved field. Therefore this model's merit is compared with its own `43.67031770334245` baseline; subtracting the prior round's differently weighted merit would be inappropriate.

## 3. Every actual trial and the nearest rejection

| Actual step | Original node failures | Original midpoint failures | Selected angular readout | Complete RMS queries | Actual merit |
|---|---:|---:|---|---|---:|
| $1$ | 0 | 7: 475,477,479,480,481,485,486 | Negative values on several existing grids | Not evaluated | Not defined |
| $1/2$ | 0 | 1: 486 | Existing left-RMS466 negative | Not evaluated | Not defined |
| $1/4$ | 0 | 0 | All 24 grids strictly positive | Both 698-point sets valid | `43.57938353308094` |

The nearest rejected trial, $\alpha=1/2$, has two distinct saved pieces of domain evidence:

- **Original midpoint486**, which is not in this 24-query B model: its original midpoint input is finite but its original RHS is nonfinite. The observer saved $\beta^2_{\min}=-0.02459725597153306$ at angle index 47, $\phi=0.14419419406125028$, with four negative angle samples. The station is `1.2516837037373927`.
- **Existing selected left-RMS466**, query index 0: its independent selected-angle readout saved $\beta^2_{\min}=-0.4800191170959498$ at angle index 959, $\phi=2.9421751511646597$, with eight negative samples. The station is `1.1653164835060832`.

The selected grid readout is not the complete original RMS pass. At this trial the midpoint failure prevented that complete pass, and no actual merit was saved. It is therefore incorrect to describe this nearest rejection as solely an omitted midpoint486 constraint, or to infer what the remaining original RMS points would have done.

The model's saved linearized beta-squared minimum at $\alpha=1/2$ is positive, `0.0010121426509067596`, across all 49,152 modeled angle rows. The existing left466 grid nevertheless fails in the actual nonlinear query. Thus finite feasibility of this one linearized model does not make its half-step nonlinearly feasible. This is direct evidence to preserve the real original backtracking and to reconsider the model at the new accepted warm, rather than asserting that one new row will fix the larger step.

For the farther unit step, the seven original bad midpoint beta-squared minima were respectively `-0.06540999283066884`, `-0.04526581177154054`, `-0.07278247746459399`, `-0.10947242993447226`, `-0.10020124732388291`, `-0.07461019985007522`, and `-0.044560585532574803`. The original readout preserves each station, angle, negative count, midpoint/RHS hash, and raw observer descriptor. No maximum over the complete physical collocation residual is defined for either nonfinite trial.

At the accepted quarter step, all core and control states remain identical across nodes, the left residual and constant collocation residual remain zero, and the original uniform-phi guard remains valid on 4096 angles with saved minimum `0.16604058243274977`. Both original RMS fractions, `0.17267316464601146` and `0.8273268353539885`, have zero invalid points. The complete boundary maximum is `1.8097932193318206e-8`.

## 4. Actual C/H selection, repairs, and remaining numerical scope

The saved comparison chooses `R270-condensed-complete-H` in the same original model. Its objective is `43.47353223943321`; the retained C candidate's objective is `43.67001151481282`. The complete selected direction has actual derivative `-0.38090637568030233` and damped-model decrease `0.19678546390921117`.

The local QP stopped at its 512-working-row budget, with 200 sweeps in the final dual stage. Its final unrepaired local stage saved minimum slack `-1.6371626276878715e-13`, 421 negative slacks and ten exact zeros; its local stationarity L2 was `1.3963395252962177e-10`. The original local radial repair used factor `0.9999999999985326`. After conditional full recovery, the full-vector repair used factor `0.9999999999882926`; its segment parameter was 1 and its final composed repair factor was 1. These saved values distinguish the selected H direction from the C baseline, whose projected candidate required factor `0.0014487174643631668`, and from the raw-ray backup factor `4.696468999434147e-5`.

The final freshly evaluated full model saved all 49,152 linear slacks finite and positive, minimum `4.579669976578771e-16`, no negative or zero entries, nonnegative multipliers, stationarity L2 `3.536766257230226e-6`, and complementarity sum `1.657038395759014e-13`. Its saved cross-evidence R267 gap is `1.5631940186722204e-13`. These are ordinary floating-point readouts, not validated enclosures or a proof of QP optimality. They do not establish that increasing the working-row budget is the necessary next change, and they do not certify nonlinear domain feasibility.

The global repair does change the recovered vector, so the report correctly declines to call the final selected vector an exact exterior conditional optimum. The original full A/AT/B/BT readback is retained after all repairs and combinations. No candidate direction or metric was recomputed locally for this note.

## 5. Complete-H recovery and original implementation checks

R270 retained 21 physical nodes, eliminated 465 left and 212 right exterior physical nodes and all 109 free core coordinates, and preserved the three controls and full affine term. It used 212 reverse fronts, 512 local H solves, and one final original full-chain recovery. The condensation report's peak RSS is `4699664` KiB. Helper time including factor, condensation, QP and recovery is `156.153254393` seconds.

The saved recovered local mismatch is L2 `7.353953627205007e-17`, Linf `3.373478119029702e-17`. The original full H residual is L2 `1.968232263121937e-10`, relative `6.519126891394274e-16`; the saved exterior gradient L2 is `1.968146508163384e-10`. Same-vector supplied-versus-frozen original A and AT differences are both recorded as zero. The original affine construction records L2 error `7.082043753252418e-11` against original g L2 `302081.6219463831`, and explicitly does not discard g using a computed center.

The actual factor `input_identity` remains null. Its hash beginning `74234e98` is the hash of that null value and is not presented as a unique model identity. The separate recorded condensation model identity is `a0f9df6c3bcfbf45abb309c740330535443ef3b25cf74e5c6457edea5636431c`, and the B model identity is `f74b464eb3fcfe233cc084195e1fed50ab70b52aac07472343c5a96d1d1714d1`.

The original Actions implementation checks report B adjoint error `3.0483285070092677e-18`, local/full action difference zero, and maximum original complex-chain relative discrepancy `1.4135311081361798e-12`; the actual supplied direction's discrepancy is `8.084166314988237e-13`. The independent original nonlinear-collocation complex check is `8.673617379884035e-19` on its stated scope: free inlet core and shared controls, with interior physical direction zero. It is not a check of every interior physical direction.

The producer also saved three finite real full-residual direction diagnostics, with relative discrepancies `5.978793112513178e-5`, `0.0001531661571257932`, and `0.00021376480728044496`; their saved merit slopes are `-0.38090641208299303`, `-0.38090642931365437`, and `-0.38090643855070994`. They remain readout diagnostics rather than added acceptance gates. The separate original complete boundary FD passed using its own unchanged Richardson estimator and threshold.

## 6. The observed physical residual and actual FD scope

The read-only observer locates the maximum physical collocation component at interval 461, radial mode 1, original residual row 155819, both before and after the accepted step. Its signed value changes from `-0.007108873959470118` to `-0.00710855617496271`. Both values use the same saved model weight `199.04282150515004`; the weight is read from the original base-state Wr and is not recomputed from trial midpoint RHS.

This location is outside the B support but remains in the full residual and full H optimization. Its persistence is not evidence of an omitted equation or zero weight. A large aggregate merit decrease or a small model KKT readout does not require this particular maximum component to decrease rapidly. This note performs no new row-action or norm calculation.

The FD uses the completed actual T112 zero-height Jacobian as an explicitly affine reference at the new warm. The report says `current_H_equals_affine_anchor: false`, `nonlinear_native_at_current_H_solved: false`, and `nonlinear_DN_evaluated: false`. Its original second-order error is `9.883465553372668e-6` with truncation contraction; both fourth-order maxima are `8.532100047207813e-10`, and separated off-blocks are zero. It actually rechecks this new warm and its complete producer; it does not relabel an earlier pass or solve a new nonlinear tail.

## 7. Original new pair and primary byte checks

The new warm is:

```text
warm-001.json.gz: 4858829 bytes
bba24c1f882d14751c4272148ee0cd6271c584485c6d0d3efaafa1a081a2a97f
```

Its paired original status is:

```text
driver-status.json: 2331066 bytes
a1a67b9a1e0e97aa23404a8fa6c5936805de34f763f0076516c4f736aedc4cb5

driver-status.json.gz: 276520 bytes
d8e9133a002280ff7f116738a53203ff273681414ec8aae2405ced1ee5726c8d
```

The original schema is `exact-constraint-twenty-four-query-condensed-complete-H-warm-v1`. Both decoded status bytes and compressed transport bytes have been retained and checked; no status JSON was reserialized for the parent identity.

The [primary identity readback](2026-11-15-actual76-primary-identity-readback.json) checks 17 parent/report/publication relations: original parent pair, full producer retention, new warm/status/FD binding, transparent original JSON compression, unchanged mesh, original unaccepted flags, and all five fetched original-file identities. All 62 distinct source hashes in the current status and FD ledgers match actual local source bytes. The [compact original readout](2026-11-15-actual76-original-readout.json) preserves every actual trial and the selected QP/recovery/FD/observer fields without recomputing scientific quantities.

The primary model is 597,528 bytes, SHA `2189ac0bbbb909a50f8607855511c50cccd99c29bad3df39ebe9b865eae42ed0`; the original QP summary is 106,499 bytes, SHA `e782165a9935ecc992b2f694c5e8e042a1e112801f7af1649fc18350bf6b3654`; the original decoded FD is 1,747,618 bytes, SHA `b7c01d852f4bb705296ba25f87e73b84030b92a40c12b2a962c999b5f86ac0ce`. These files were read locally from the root's exact CLI fetch. This primary scope does not include an independent byte audit of the large B/condensed/raw arrays. The full chain QR factor was not exported; it cannot be claimed as independently file-audited. A completed-artifact reader can record the available payload scope separately and is not a new scientific gate.

## 8. Evidence-based successor

Continue once from the actual76 new pair using the same frozen 24-query own-schema entry, $\lambda=270$, 512 working rows, 200 dual sweeps, and all original trial/FD/domain rules. This relinearizes at a genuinely new accepted optimization warm; it does not repeat the original actual74 model.

The nearest rejected half-step already violates modeled left466 as well as unmodeled midpoint486. Automatically adding only midpoint486 would not address all observed nonlinear failures. The quarter-step has paid a genuine fixed-weight decrease and all original query checks, so the minimal next experiment is the same 24-query model at its new base. It is not a guarantee of the next step or eventual BVP acceptance. No 25th query, damping change, new scientific gate, or relaxed tolerance is introduced by this decision.
