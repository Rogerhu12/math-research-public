# R133 supplement DZF: first fourth-angle/sign run stopped at the legacy payload-hash convention

## 1. Actual result and unchanged mathematical scope

The first natural push run [43773126387/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43773126387), job 132993259075, finished with failure. It was triggered by commit b5ee6143e79210ab6db86666e2b40f78cda48370; the run started at 2026-11-15 23:08:04 UTC and its final Actions update was 23:08:48 UTC. The actual scientific checkout was 403a2fcf430f0ed98b5731256befe36bb833eadf.

One new scientific child was launched. It returned 1 after ten successful structural gates and the eleventh failed gate. Its preserved stage is “initial immutable input checks”. The failure is:

> ValueError: complete DZ gate failed: TC complete real phase triple is reused verbatim in the same WX propagation

This was an input-metadata failure. It did not evaluate the new fourth derivatives, density/sign difference, whole negative-window minimum, common-outgoing product or standard-outgoing subtotal. It does not establish failure of any analytic inequality, singularity of an operator, or the size of any unknown state.

The full partial scientific object, execution record and renderer output are preserved. No new completed target or scientific intermediate was lost. No old successful scientific calculation was repeated. The conditional analytic statements in [DX4](R133-supplement-complete-fourth-angle-derivatives-from-saved-cut-and-flow-bounds.md), [ZD](R133-supplement-strong-sign-density-conjugation-and-global-Cayley-return.md) and [MS](R133-supplement-exact-Maslov-sign-operator-and-common-input-outgoing-order.md) remain separate from this unsuccessful first numerical consumer.

## 2. Immutable deployed inputs and actual outputs

The deployed package used these exact files:

| File | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| Scientific source | 181e0aaa70149b7f92178cc686014d1cd77e4844 | 38593 | 245da4db1e6e105d5a753ab8917a3f2b0b1633214dba7e69fc81a36c7e52cd6b |
| Public worker | 7df9ce4274942020d9917a15417c3901584c4251 | 54906 | 8d0c64522b1a08664e5d8612c210e56952ab9e50a0fd2457b4286ab4557814ac |
| Input manifest | 436f3a2f7c197f6dbcab194743fce145fb81cab5 | 19314 | c9a45aa76c5228d440d36629a87e38ee24fcc8c61085cbfeef3cf4bfa41dfba9 |
| Workflow | ab784f843a6ce40c5c8d1f69bc2e66a2e7c6ffda | 4714 | 31bd63f993900206a687e83e3cdfe0d2dc3036e647bf1fa126bf5b269482fa5f |

The source and worker are scripts/fourfold_codazzi_fourth_angle_and_Maslov_sign_budgets.py and scripts/fourfold_codazzi_fourth_angle_and_Maslov_sign_public_worker.py. The manifest is [the original reviewed input list](../notes/2026-11-15-R133-fourth-angle-and-global-sign-CI-inputs.json); the workflow is .github/workflows/visible-exact-fourth-angle-global-sign.yml at repository root. The blob identities above preserve the first version even after a later correction.

The three actual files are in notes/fourth_angle_global_sign_budgets_ci/run-43773126387-1/:

| Actual file | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| [Complete partial scientific object](../notes/fourth_angle_global_sign_budgets_ci/run-43773126387-1/actual-scientific-conclusion.json) | 76127826bec9960467f29a579697f1691714f101 | 5079 | b12557172e497f66e40a6f74184d80875e543bb3abb57b45a567f71e52236b8c |
| [Execution record](../notes/fourth_angle_global_sign_budgets_ci/run-43773126387-1/execution.json) | a73d08c622306a16588bd893a4fba3201ad61388 | 13663 | a9f6e44f878a511ad94a627df3ad54619aeb2b33138b2c5e2c72a2e5387b89cb |
| [Original renderer output](../notes/fourth_angle_global_sign_budgets_ci/run-43773126387-1/actual-result.md) | 428a84e91f08a4d4a8b46753562ab9c8e4ad4a7e | 2839 | eacd19309d897563636e3ef03dab52a7f493651d0e8d877a573ebd8c1d5080c1 |

The execution record confirms all fourteen current small-text identities and all four immutable Python AST checks. Runtime was Python 3.12.14, python-flint 0.9.0, with 320-bit directed arithmetic. The two old Python sources were parsed as evidence and were neither imported nor executed. There were zero restored binaries, old artifacts, newly retained arrays, Releases or new data artifacts.

The complete science-plus-report payload printed before Git publication was 8213 bytes with SHA256 3b8847325f3a3bb482d519dbf53c1cf5c0e99e9fefceaf292ef9fc308a3f7c38. It is independently reproduced from the complete scientific object and the original report with only its final, later README-pull line removed. Re-serialization uses sorted keys, compact separators and one terminal LF. The scientific object alone reproduces its recorded 5079-byte SHA256 exactly.

The execution record additionally identifies the child stdout as 6513 bytes, SHA256 7e10f5e36c177ceee6d85c49ec031bdb27d1cfcf6f0fc91dc1563c226fb17658, and its original prepublication execution payload as 11083 bytes, SHA256 251228018369cbab4fd2199bf8ff65c2a4efb17e33acc09af1193e9fe1f8d364. These latter two identities are quoted from the execution record; this audit does not claim to have downloaded the complete job log or independently reconstructed that earlier execution state.

## 3. Exact cause: one legacy object hash excludes the terminal LF

Let td be the complete original TC complete_density_coordinate_conclusion. The WX receipt contains the identical object under accepted_original_complete_conclusions.TC_complete_density_coordinate_read_verbatim. Their full object equality holds, including both phase branches, the complete scalar mean, the two independent physical mean coordinates and the common cut.

WX computed its separate legacy object hash from sorted compact JSON **without** a terminal LF:

| Encoding of this same complete object | Bytes | SHA256 |
|---|---:|---|
| Sorted compact JSON, no LF | 4396 | 2d050a0e34db04a3b7e53daa51ff91e4410c65ee84f7948f288ebe51a78ad4c7 |
| The same JSON followed by LF | 4397 | b30ac7c9dcc3cb9bdff6d79781cc0d956d13f053f52d7f4747fafae0727455ae |

The saved WX field is the first hash. The new DZ helper canonical deliberately appends LF for its own complete scientific files. The first DZ source mistakenly checked the legacy WX field against digest(canonical(td)), the second hash. Thus the failed conjunction does not exhibit a disagreement in the mathematical TC object.

The narrowly specified correction is:

~~~python
wa["TC_complete_density_coordinate_payload_sha256"] == digest(canonical(td)[:-1])
~~~

Only this one legacy-payload comparison changes. The global canonical serializer, the complete new scientific-file format, every pinned old scientific input, the mathematical parameters, all arithmetic formulas, all actual scope flags and the 24-gate design remain unchanged. Object equality is still checked in full before this hash. This is not permission to accept a missing hash or bypass the TC/WX identity.

## 4. Actual gate order, new work and lost-work accounting

The full eleven-gate list remains in the scientific object. The first three gates validate the runtime, all eleven mathematical text identities and the AST-only treatment of old sources. Gates 4–8 validate the five completed FA, TC, WX, PG and WE scientific records, including their original runs, source/manifest identities, runtimes and gates. Gate 9 validates the common real family, strict cut, selected parameter and physical Fourier units. Gate 10 validates the full original FA holomorphic strip. Gate 11 fails at the legacy hash comparison in Section 3.

In the frozen source, run calls checked_inputs before fourth_derivatives, sign_bounds or commonout_bounds. Gate 11 raises inside checked_inputs; therefore none of these three numerical routines was entered. All fifteen planned higher-derivative combinations and all new sign/commonout/standardout counters remain zero. The prospective gates 12–24 were not reached and are not recorded as passed.

The field original_completed_scientific_receipts_read remains at its initialized zero because it is assigned 5 only after the *entire* input audit returns. It must not be interpreted as saying that no old scientific file was read: gates 4–8 and the fourteen actual input receipts show precisely which successful records were validated. The zero is an incomplete-audit counter, not an absence-of-input claim.

| Category | Actual first-run status |
|---|---|
| New scientific children | 1, exit 1 |
| Recorded structural gates | 10 passed, 1 failed; later gates unexecuted |
| New higher-derivative and sign/subtotal targets | 0 completed; their numerical routines not entered |
| Old scientific producers or successful targets recomputed | 0 |
| New target results lost | 0 |
| Full partial science and failure identity | Saved, printed before formatting/publication and published |
| Complete new standardout bound or full incoming inverse | Not proved |

The nonzero elapsed process time records actual input validation and failure handling. It is not described as zero execution time or zero scientific child activity.

## 5. Correction to generic prose in the preserved renderer output

The first renderer correctly says that the mathematical receipt is incomplete. However, two later generic passages are inappropriate on this failure branch: the claim that the complete WE retained register has been copied and the scope sentence saying that the infinite sign difference is bounded.

Neither is an actual result of this run. The stopped scientific object contains no copied WE register and no new sign bound. Its false proof flags and zero new counters govern the interpretation. The original renderer file is preserved unchanged as historical evidence; a later worker may condition these sentences on the corresponding completed fields. Such a renderer change is operational metadata and does not alter the scientific formulas.

In particular the retained register has not been made zero, finite rank or paid. Both physical matching means, transported low input, complete old finite columns, second-reference and opposite-sign terms, the complete incoming error/inverse and the actual finite Schur problem remain subject to their existing exact obligations.

## 6. Permitted continuation

After this failure is recorded, the corrected consumer may perform the previously unentered DZ scalar combinations in one new natural public Actions run. It must consume the same already successful small FA/TC/WX/PG/WE records, preserve their full identities, and re-check the complete remaining input audit. This report grants no new numerical upper bound in advance.

No successful old ray, flow, KAM, residual, normalizer, coordinate or coefficient calculation is to be repeated. The failed first record remains immutable. A future successful result must be identified by its own source, manifest, run and complete scientific hash; it must continue to distinguish a known paid subtotal from the full operator error and the actual incoming inverse.
