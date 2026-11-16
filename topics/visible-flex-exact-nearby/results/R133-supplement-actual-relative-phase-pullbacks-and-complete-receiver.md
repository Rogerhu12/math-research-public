# R133 actual result: complete relative phase pullbacks and the same whole receiver

2026-11-16. WRPA; complete read-only account of the first WRP40 execution. This note copies successful recorded values and verifies their file and operator identities. It performs no scientific recomputation.

## 1. Actual conclusion and its scope

The first public WRP40 run, **43881690924, attempt 1**, completed successfully. It saved all three graphs, comprising **7 + 15 + 18 = 40 new scalar records**, with all **14 scientific gates** true and the complete **16-field progress record** present. All **44 original record objects** and **nine complete consumed qualification objects** remain verbatim. The worker reports exactly one new scientific child, zero old scientific calls or repeated old targets, zero history restoration, and no interrupted or lost new target.

Both independently typed whole-operator comparisons selected the new complete relative-phase candidate. The original whole candidate is retained for each comparison. The saved whole result is

$$
 C_* \le \operatorname{ub}\!\left(
 [1.90736423682251400641766771203225487061996663267347748430927102916501134114
 \,10^{323}\ \mathord{+/-}\ 1.25\,10^{248}]\right),
 \tag{WRPA.1}
$$

and the saved reduced-operator result has the same displayed midpoint and radius $1.26\,10^{248}$. These are complete scalar upper records from the directed runtime; Appendix A preserves their exact original text. Here $\operatorname{ub}(I)$ denotes the certified upper endpoint of the saved ball $I$. Its midpoint alone is not substituted for that upper endpoint.

The leading displayed order remains $10^{323}$. This execution improves the complete angular pullback and its retained-source reception. It does not change the physical mean source, its propagation, the local patch, any actual jump, any of the four waist terms, the root matrix, the positive correction, or the exact finite factors. The original mean contributions remain in the complete negative-source bound. No smallness condition, signed finite inverse, or physical-column normalization is concluded.

The result is restricted to the same selected real member, with intrinsic parameter

$$
 \eta_0=-7789843107295549/4611686018427387904.
$$

It acts on the same intermediate input $H^{-4/3}$ and the same normalized physical waist $L^2$ output as WRP. The complete ordered common right map and readout remain outside the source bound once, as in the original whole-operator identity.

## 2. Complete published result files

All three result files are under

`topics/visible-flex-exact-nearby/notes/relative_phase_pullback_receiver_ci/run-43881690924-1/`

and were fetched in full. No result file was inferred from a log excerpt.

| File | Complete Git blob | Bytes | SHA256 |
|---|---|---:|---|
| `actual-scientific-conclusion.json` | `146904d030cca0887fae921084396bf4008d0281` | 82508 | `4b66bd0ba1425c7a5a705cba3b32b07ea893643a7aa8cde1a720dcf450e852ee` |
| `execution.json` | `f6a3a109b851b22dea30138539f056d6db2e8c49` | 21783 | `3a5ec986c684067683192850f1e7e667d56c463982ff80219b552ec3e7043e2c` |
| `report.md` | `61dd1c43419b05cb9bdb6e3cf0096ccbe42ab92f` | 449 | `c4885200c44d623457331575ade12d6cabbb4607d0951f4a39e8d76714c46142` |

Their total is **104740 bytes**. Each individual file remains below100000 bytes. The scientific file has exactly32 top-level fields and is canonical UTF8 JSON with a final newline. The execution file was likewise independently canonicalized to the exact original bytes.

The proof used by the run is

`results/R133-supplement-relative-phase-pullbacks-and-complete-receiver-refinement.md`,

Git blob `9f55708ca3a0a6018279628342fb8715a48ab830`,16951 bytes, SHA256

`95be269fc011c756fff2f882a32828ad7293bbaa140c28f0cf6eb5474e674f36`.

The complete frozen manifest is

`notes/2026-11-16-R133-relative-phase-pullback-receiver-current-inputs.json`,

Git `f31bb4186d0898be547fa28eb06ff6e9e6a7faa8`,18830 bytes, SHA256

`d4a3bb1055a7027460a736a5fb04a7b034d50ab4f492a09029c98f1e982b70f6`.

The workflow is `.github/workflows/visible-exact-relative-phase-pullback-receiver.yml`, Git `506b1cd7e68a48d63747438bb1a3af077e633e98`,2979 bytes, SHA256 `b0e4ea3e47c17d15208c2609aa7e7016ae1376402369806b202d9352f1c28665`. These package identities are distinct from the result-file identities.

## 3. All current input identities and read-only admission

There are nine current pinned inputs: five complete original actual files, the published WRP theorem, the new science source, its dedicated bounded worker, and the reviewed rules. There is no historical input.

All paths below are relative to `topics/visible-flex-exact-nearby/`.

| Role | Path | Complete Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| `wjr_actual` | `notes/relative_flow_Jacobian_ci/run-43873739440-1/actual-scientific-conclusion.json` | `80499e42f643e607db47c973b54f2243629a05e8` | 69002 | `806fbeaaab33ddff424fcfe70e40f83f46d1f85e089f9f01f941ed38ee249660` |
| `wsm_index` | `notes/strict_scaled_mixed_complete_ci/run-43877268949-1/actual-scientific-conclusion.json` | `7caabc2c0ca0953a3fe8d4c6ae25116c2ee09220` | 30834 | `3cb8fa2a506df28e634564a97aa124cb10aeb474a4daf02d7c7d62ac422d5172` |
| `wsm_profile` | `notes/strict_scaled_mixed_complete_ci/run-43877268949-1/graphs/strict_complete_angular_profile.json` | `fd6cc26610532bcb0aae73ff4e0ba8c7ad69e655` | 10901 | `860c6eca208427ebf72503924445e277701f62b7640992b9dc0b1321572673ed` |
| `wsm_N6` | `notes/strict_scaled_mixed_complete_ci/run-43877268949-1/graphs/strict_complete_ordered_N6.json` | `26baf34bdfda9e5191fb55cc5893f2f8bd2a5d6c` | 22944 | `4de5f900e09d548e2325d2ed09d4e68f74c596342c97648477e67a502396c4b6` |
| `wsm_receiver` | `notes/strict_scaled_mixed_complete_ci/run-43877268949-1/graphs/strict_complete_whole_receiver.json` | `15eb048bf37a6bcc28aeaa6d745a026bdbdd5a62` | 14230 | `2413d02a10b9e465212970a5cdeef41ef9091854f496921fefa528cea6851983` |
| `proof_WRP` | `results/R133-supplement-relative-phase-pullbacks-and-complete-receiver-refinement.md` | `9f55708ca3a0a6018279628342fb8715a48ab830` | 16951 | `95be269fc011c756fff2f882a32828ad7293bbaa140c28f0cf6eb5474e674f36` |
| `science` | `scripts/fourfold_codazzi_relative_phase_pullback.py` | `e4f1ea70197856466a756e982ccf6dffc8d0fc29` | 74480 | `40841675c92525e912e41d6c652667297e1de65162ba8f44956f5334f4defc6b` |
| `worker` | `scripts/fourfold_codazzi_relative_phase_pullback_public_worker.py` | `c410f91faae59dac177b737faffe4dd11d3f2d46` | 26542 | `3770e29dbb2becd615227c1ceceaf7c9a34cf585a705deeed75465dc02594d8e` |
| `rules` | `notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json` | `5c5d020913d717bb5bc8ce891297e00eaa8944f7` | 2461 | `65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1` |

The original WJR result supplies the actual positive-phase relative ratios. The complete WSM index and all three bound node files supply the same selected profile, exact retained N6 amplitudes, complete inverse windows, and current whole candidates. Their complete byte identities, original fields, runtime/source/manifest identities, statuses and dependency references were checked before the new directed runtime was imported.

The WSM profile and N6 nodes possess their own independent relative-angular predecessor field. The receiver instead retains that qualification through its complete binding and both actual direct dependencies. The reader checks this actual schema; it does not fabricate an independent receiver field.

The original WJR15-gate/56-target result and WSM22-gate/152-target result remain complete. The earlier failed ancestors mentioned by their immutable input chains retain their original failure status. A successful descendant does not relabel a failed ancestor.

The exact original-copy checkpoints are:

| Retained complete object | Bytes in canonical JSON plus newline | SHA256 |
|---|---:|---|
|44 original scalar record objects|5452|`aa9086fce792a007eb09eb0a7a076364cb9dfe8f8506e97a68fc4b37bceed75b`|
|9 complete consumed qualification objects|43857|`9f3e9070c01ffd7682fb17841a962664cf8f28b2136c2525795367fa7a3898f2`|
|Complete accepted-old-input object|11239|`d1cf3cc5eea82af08e63064a982203a1fb35b0420ec7a9ea29924607e78ad38c`|

Each was independently reconstructed from the complete old files and compared with the actual WRP copy. No original ball was parsed for a new scientific evaluation during this audit. Appendix B preserves all44 original record objects.

The nine complete qualification objects are retained by the scientific file, with the following independent identities:

| Qualification alias | Bytes | SHA256 |
|---|---:|---|
| `complete_WJR_parameters` | 1684 | `3c5e0f395ddc454ab87e5682767e34bd0f9a1c055b20fd726f2224f7796624b0` |
| `complete_WJR_positive_phase_ratio_qualification` | 533 | `ec6b131c37c4f04517da8beb3ef324d3ec6cd252dd48014da2ff2e373e4e7cd0` |
| `complete_WJR_retained_scope` | 1939 | `1479231e0ee2cd93fb2d02afe2d2578ea2477baa7c89902a0f307b27b33020c1` |
| `complete_WSM_ordered_N6_qualification` | 11797 | `3075e8ac14c57b506f96b7ab8ff86a8e0226738484072a6c8a006d66bba580a7` |
| `complete_WSM_original_input_qualification_references` | 14185 | `18b1dd23fd9207b25c6c617cbc4d26eead7962dcd0998ddca233b4f6321ec0ce` |
| `complete_WSM_parameters` | 1492 | `d87bb538f18f15953b925148e019c36471efc4f681289eadc094e7e762f9e195` |
| `complete_WSM_profile_qualification` | 5214 | `3f8c651a49249cdbb1d1bcf618bacb1af1b2928e05c58a835151738e9a5f6851` |
| `complete_WSM_receiver_qualification` | 5614 | `65b82b05f13d97340397a408c035753196e721dcc2da46963cae3ac865ef3b43` |
| `complete_WSM_retained_scope` | 1065 | `01691a513c8660346a27e70afa05232b58b9ac5e48bd1157660efeb815d87808` |

The non-ball projection preserves recursive object structure, array positions, empty containers, all derivative normalization and domain fields, and the complete failed-ancestry references. Repeated operation metadata is retained by the full original byte identity and explicit JSON path; mathematical scope is not deleted.

## 4. What the three new graphs certify

### 4.1. Seven complete relative inverse-phase and pullback records

The first graph uses the original complete global inverse-first-derivative budget $U$, the complete old $L^2$ pullback budget $K_0$, and the three WJR ordinary relative derivatives of the same actual positive phase derivative. It never replaces a global lower bound by an unrelated cut lower bound.

The inverse-phase derivatives through order4 and the complete row and column sums are formed in the same normalized circle measure. The auxiliary comparison acts on the three $H^2$ seminorm coordinates

$$
 \bigl(\|f\|_2,\sqrt2\,\|f'\|_2,\|f''\|_2\bigr).
 \tag{WRPA.2}
$$

This is an auxiliary three-coordinate norm comparison, not the three coordinates of a physical state. The exact density adjoint of the same pullback is differentiated before norms are taken. Its full zeroth output, mean, and low Fourier output remain included.

The new $H^{-2}$ pullback upper is the complete $K_0\sqrt{RC}$, and the $H^{-5/3}$ upper is obtained by the declared complete interpolation. The old $K_0$, the old pointwise $U$, and the old square-root-of-two record are read once in their original roles.

The actual saved records include

$$
 K_{-2}=
 [7396213032484.01734210910305731892993512306464328897669887748261973884171744
 \ \mathord{+/-}\ 3.38\,10^{-63}],
$$
$$
 K_{-5/3}=
 [69699424619.6399110485438709112816886511076333785658070003231560093274023476
 \ \mathord{+/-}\ 3.10\,10^{-65}].
 \tag{WRPA.3}
$$

No individual inverse operator is inferred from these bounds.

### 4.2. All fifteen full-output profile weights

The second graph saves all five angular weights for each of the three windows $d=0,5/3,2$. The zeroth complete profile record is independently copied from WSM. Its positive terms are not re-expanded and then asserted to lie below that already saved record.

For higher weights the ordinary derivatives are obtained from the complete normalized profile coefficients by multiplying by the single required factorial. The full fourth-order composition includes every Bell coefficient. The complete Fourier Schur sum retains zero output, low output and high output; all signed inputs are handled before the original isometric reflection restriction.

The same complete near profile and both far genuine phases remain in the input profile record. This graph neither recalculates WSM's profile nor alters the genuine normalization or extended potential.

### 4.3. Eighteen records for the same complete receiver

The retained amplitude is the complete original

$$
 r=v_1+n^{-1}v_2,\qquad n=4|j|\ge388,
 \tag{WRPA.4}
$$

read through all five ordinary angular coefficients. It is projected into the actual even-zero input before the same parity inverse. The original complete $J:H^{-5/3}\to H^{-2/3}$ and ordered $IJ:H^{-2}\to L^2$ windows are read unchanged.

The new strict retained bounds are joined to the whole old local bound, and the actual mixed-source collar and strict ordinary source are received in their original windows. The true root remains $r_*$. The fixed upper enclosure $r_+$ supplies only an ordinary length majorant.

Every original physical mean fee and each complete3070-interface jump fee is retained. No radial length is multiplied onto a jump. The entire E3 terminal dyadic contribution is read as one old complete object. It is not replaced by a difference of old upper bounds.

The source sum retains the original positive correction, root fee and all four waist terms. The old ordered readout $L_{\rm rec}$ is applied once. The whole and reduced operators have different complete definitions and are compared independently.

The actual selected negative-source record is

$$
 C_- \le \operatorname{ub}\!\left(
 [4.56106007409224152018032214160376163184075594590616953941602114703272102345
 \,10^{316}\ \mathord{+/-}\ 3.45\,10^{241}]\right).
 \tag{WRPA.5}
$$

The old physical means are unchanged. Thus the leading magnitude of the final whole bound can remain unchanged even while the retained-source and pullback bounds improve. That observation does not authorize removing the mean or any terminal term.

## 5. Exact same-operator selection

Both complete old candidates are copied into the actual result. Both complete new candidates are saved before selection. The old candidate wins an equal saved upper. No entrywise minimum is taken inside an operator bound.

The exact selection objects are:

```json
{
  "reduced": {
    "both_complete_candidates_retained": true,
    "complete_selected_upper": {
      "ball": "[1.90736423682251400641766771203225487061996663267347748430927102916501134114e+323 +/- 1.26e+248]"
    },
    "new_record_path": [
      "complete_new_graphs",
      "complete_new_same_whole_receiver_conclusion",
      "new_records",
      "complete_same_reduced_error_upper"
    ],
    "operator": "reduced_after_exact_finite_factor_separation",
    "prior_record_path": [
      "copied_original_scalar_records",
      "prior_reduced"
    ],
    "prior_source_record_path": [
      "conclusion",
      "new_records",
      "whole_and_reduced",
      "complete_same_reduced_error_upper"
    ],
    "prior_source_role": "wsm_receiver",
    "prior_wins_equal_saved_upper": true,
    "selected_label": "new_complete_relative_phase_pullback_candidate",
    "selected_record_path": [
      "complete_new_graphs",
      "complete_new_same_whole_receiver_conclusion",
      "new_records",
      "complete_same_reduced_error_upper"
    ]
  },
  "whole": {
    "both_complete_candidates_retained": true,
    "complete_selected_upper": {
      "ball": "[1.90736423682251400641766771203225487061996663267347748430927102916501134114e+323 +/- 1.25e+248]"
    },
    "new_record_path": [
      "complete_new_graphs",
      "complete_new_same_whole_receiver_conclusion",
      "new_records",
      "complete_same_whole_error_upper"
    ],
    "operator": "whole",
    "prior_record_path": [
      "copied_original_scalar_records",
      "prior_whole"
    ],
    "prior_source_record_path": [
      "conclusion",
      "new_records",
      "whole_and_reduced",
      "complete_same_whole_error_upper"
    ],
    "prior_source_role": "wsm_receiver",
    "prior_wins_equal_saved_upper": true,
    "selected_label": "new_complete_relative_phase_pullback_candidate",
    "selected_record_path": [
      "complete_new_graphs",
      "complete_new_same_whole_receiver_conclusion",
      "new_records",
      "complete_same_whole_error_upper"
    ]
  }
}
```


The actual selected paths equal the complete new record objects byte for byte. The prior paths equal the original WSM whole and reduced objects byte for byte. This is a check of saved records and their identities, not a rerun of the directed comparison.

The source and scope retain the actual96 physical columns and their still uncomputed signed normalization, both independent physical mean coordinates, all $\Theta/\nu$ and radial-head ports, and the exact finite root/coefficient factors. The reduced bound retains those finite terms in its auxiliary border rather than discarding them.

## 6. All scientific gates and progress

The complete14-gate record is:

| Order | Gate | Passed |
|---:|---|---|
| 1 | `directed_public_runtime` | true |
| 2 | `current_input_and_AST_identity` | true |
| 3 | `all_five_complete_original_files_byte_identical` | true |
| 4 | `complete_WJR_relative_phase_receipt` | true |
| 5 | `complete_WSM_profile_N6_receiver_same_binding` | true |
| 6 | `complete_original_scopes_and_failed_ancestry_retained` | true |
| 7 | `all_44_scalar_and_nine_qualification_copies_retained` | true |
| 8 | `same_measure_full_mean_original_phase_budgets_and_parity_window` | true |
| 9 | `complete_relative_inverse_phase_and_pullbacks` | true |
| 10 | `complete_fifteen_full_output_profile_weights` | true |
| 11 | `complete_same_whole_and_reduced_receiver` | true |
| 12 | `only_identical_whole_operator_candidates_compared` | true |
| 13 | `all_current_inputs_still_identical` | true |
| 14 | `complete_scientific_graph_and_prefix` | true |

The complete16-field actual progress object is:

| Field | Actual value |
|---|---:|
| `complete_original_files_admitted` | 5 |
| `new_exponentials_saved` | 0 |
| `new_fractional_powers` | 2 |
| `new_graphs_completed` | 3 |
| `new_logarithms` | 0 |
| `new_quadratures` | 0 |
| `new_records_saved` | 40 |
| `new_square_roots` | 1 |
| `new_whole_comparisons_completed` | 2 |
| `old_binary_parts_restored` | 0 |
| `old_exponentials_recomputed` | 0 |
| `old_scientific_calls` | 0 |
| `old_targets_recomputed` | 0 |
| `original_qualification_objects_copied` | 9 |
| `original_record_objects_copied` | 44 |
| `original_records_copied_in_graphs` | 0 |

There are two new positive fractional powers and one square root, all inside the new seven-record pullback graph. There are no new exponentials, logarithms, flows, quadratures or ODE integrations. The complete scientific state is `complete=true`, `proved=true`, `stage=complete`, `actual_returncode=0`, `failure=null`, `current_target=null`. The exact completed-target order and record counts are7,15,18.

All forty planned new record leaves occur in the complete graph shapes. The final progress record reports40 saved new records. Therefore this successful run has no missing new target and no lost scientific prefix. The forty new records are frozen; this note does not authorize rerunning them.

## 7. Actual runtime, pulls, and publication

The GitHub Actions metadata was independently read from the public run and jobs endpoints. Run number1 and attempt1 are complete and successful, with event `push` and workflow event commit

`12345cce183d8b1a3bcf066ffe16c6399f1ea2f2`.

The run was created at14:02:44 UTC and updated complete at14:03:18 UTC on2026-11-16. Job133348935162 ran from14:02:48 to14:03:17 UTC. All nine actual job steps were successful; their actual numbers are1,2,3,4,5,6,11,12,13. This count includes the post-setup and complete-job steps.

The exact consumed-target marker was published before the sole scientific child. Its commit, and the actual science checkout, are

`6ea61c9cb552537314d535fc98ae1fb88a9537aa`.

The event checkout and scientific checkout are intentionally different: the marker commit intervened. The science file and execution file agree on the actual checkout, run, attempt, manifest and source identity.

The directed runtime is Python3.12.14 with python-flint0.9.0 at320 bits. The actual mathematical wall time is0.18615244299999745 seconds, and child wall time is0.7541033299999995 seconds. These are copied operation measurements, not mathematical bounds.

The execution retains four complete real `git pull --rebase` receipts. Each compares both READMEs with the explicit reviewed rules and records empty actual and reviewed differences. Reconstructing the complete ordered chain gives

`e4adb0fefea1996e29dc087b0ebc696e22fb115dc3cda36a0eb8fb11fdc860f7`.

The last pull ran14:03:11.909281--14:03:12.218489 UTC and retained the actual science checkout. The worker made one successful publication attempt.

The pure read-only preflight returned0, imported no flint, and produced a complete12874-byte JSON stdout. Independent canonical reconstruction gives

`bd51993a441daf09823b44c5b05760bea38def71dfcba8797d7ce92e472fd79c`.

Its complete accepted-old-input object is identical to the actual science admission. Its stderr was empty.

The final operation metadata records199601879 topic bytes before the three result files. With the complete104740-byte publication, the exact projected total is199706619. The individual95KB science and59KB execution caps,2KB report cap, and156KB complete output cap were respected. This is a byte accounting statement, not a scientific estimate.

The dedicated bounded worker preserves complete operation exception text in the job log before applying JSON-escaped UTF8 bounds to its diagnostic copy. It does not truncate scientific records or scopes. No failure diagnostic branch was taken in this successful run.

## 8. Full pre-Git reconstruction and audit limits

The worker publishes the exact complete scientific file, execution file and report only after printing each full payload with its byte count and SHA256. In this run no later metadata is appended to the execution JSON after that print. The independently reconstructed canonical execution is exactly21783 bytes with the SHA256 in Section2. The report was independently reconstructed from the complete fixed report template and actual run/problem fields; it is exactly449 bytes with the SHA256 in Section2. The complete scientific canonical JSON also equals the82508-byte published body exactly.

The complete scientific child stdout is reported as3882834 bytes, SHA256

`94a194de48845010069d105328100f76125b3f980943a1a858fcb095cf2b3535`.

That large log body was **not fetched or independently rehashed in this audit**. Its size and hash above are the complete worker receipt. The independent checks concern the complete small published bodies, their pre-Git reconstruction, all actual graph records, and the actual operation metadata. No claim of independently reading the large log is made.

Twenty direct static comparisons were performed on the complete actual files: canonical science/execution bodies, top-level fieldset, parameters, retained scope, all16 progress values, all14 gates, all graph counts and shapes, completed order, allnine input receipts, pure-preflight admission, source/manifest/run/checkout binding, exact whole selection paths, complete pull chain, fixed report reconstruction, pure-preflight stdout reconstruction, complete-success status, and forty-record/no-loss accounting. Every comparison passed. The original44/scopes9/accepted identities were separately reconstructed as stated in Section3.

No Arb operation, scalar comparison, old producer, private mixed-jet recurrence, source solve, or scientific import was executed during this audit.

## Appendix A. All forty new saved record objects

The following is copied from the three complete actual `new_records` objects. It is not a decimal recomputation.

```json
{
  "complete_new_relative_phase_pullback_conclusion": {
    "complete_column_sum_upper": {
      "ball": "[1427831038159.15258386297101563881134412943331373072633852855257125314705119 +/- 9.62e-64]"
    },
    "complete_phase_pullback_Hminus2_upper": {
      "ball": "[7396213032484.01734210910305731892993512306464328897669887748261973884171744 +/- 3.38e-63]"
    },
    "complete_phase_pullback_Hminus5_3_upper": {
      "ball": "[69699424619.6399110485438709112816886511076333785658070003231560093274023476 +/- 3.10e-65]"
    },
    "complete_row_sum_upper": {
      "ball": "[1427860585941.15885549842879786161884683551303994938405589160642774896409297 +/- 1.85e-63]"
    },
    "inverse_phase_derivative_2_upper": {
      "ball": "[14283503.8097763383362200393762655180504304219758280350573069513256858082543 +/- 1.45e-68]"
    },
    "inverse_phase_derivative_3_upper": {
      "ball": "[38311820438067.5810929172970088447663571696277814452785893810217859050703078 +/- 8.48e-63]"
    },
    "inverse_phase_derivative_4_upper": {
      "ball": "[168462453631149588735.214949738621511467028127680471282830052998949535977065 +/- 2.98e-56]"
    }
  },
  "complete_new_full_output_profile_weights_conclusion": {
    "five_thirds": {
      "angle_0": {
        "ball": "[2.04388588837260108708139888127193578815296020678855008487557262244119299550e+111 +/- 9.65e+35]"
      },
      "angle_1": {
        "ball": "[1.14637921608185585453690358288298204153426216815250910660927920782262007666e+92 +/- 2.72e+17]"
      },
      "angle_2": {
        "ball": "[4581321144573481881417467060534000866977309268743277702817952742507.86734438 +/- 2.50e-9]"
      },
      "angle_3": {
        "ball": "[42826358133294236754142585916190396769553278639.6660338422065904919477341578 +/- 3.38e-29]"
      },
      "angle_4": {
        "ball": "[1004524582024646919587.72710419441723549129918049563808514540889256206096490 +/- 3.74e-54]"
      }
    },
    "two": {
      "angle_0": {
        "ball": "[2.43449299800491488407120284826340614583783900827408194475761808501977921086e+113 +/- 2.43e+38]"
      },
      "angle_1": {
        "ball": "[1.36546379153867326890926639587057090592085683346569627635542505565266342906e+94 +/- 4.79e+19]"
      },
      "angle_2": {
        "ball": "[545685760223947146528094041747218304312115445261425245231920624906991.278466 +/- 2.88e-7]"
      },
      "angle_3": {
        "ball": "[5101090506015027486637908911224232358876965357338.25764101956959995384250926 +/- 4.61e-27]"
      },
      "angle_4": {
        "ball": "[119649931298757505111488.784396279489363780123051217362065323677077190488699 +/- 3.20e-52]"
      }
    },
    "zero": {
      "angle_0": {
        "ball": "[8.52505563832447340435310475607124474804663180277508107280815631188655221417e+100 +/- 4.04e+25]"
      },
      "angle_1": {
        "ball": "[4.78155197181683541547584764750903074047341689328723900782416453536735211049e+81 +/- 2.27e+6]"
      },
      "angle_2": {
        "ball": "[191087075245765219992094423369692421361241429445335266908.363865564403788264 +/- 3.58e-19]"
      },
      "angle_3": {
        "ball": "[1786288989762748833219851108047365160.39334188882751053169990113845691843707 +/- 1.16e-39]"
      },
      "angle_4": {
        "ball": "[41898757658.3512226030420499368090864107087552723957436131150696779299828944 +/- 3.91e-65]"
      }
    }
  },
  "complete_new_same_whole_receiver_conclusion": {
    "complete_all_source_sum_upper": {
      "ball": "[4.56106007409224152018533409396555028513020791167381919463794922770257378533e+316 +/- 4.48e+241]"
    },
    "complete_collar_B_union_upper": {
      "ball": "[8.42103831668428386668619632568159540924835998188047041329819847298842972045e+235 +/- 1.63e+160]"
    },
    "complete_collar_dyadic_contribution_upper": {
      "ball": "[5.66725541387218247454342170183374317789200036613103609203127334358455286198e+315 +/- 8.3e+237]"
    },
    "complete_collar_retained_and_mean_ordinary_upper": {
      "ball": "[1.74448394150398505005504389612843825783007865900660003560911039987416450444e+314 +/- 4.89e+239]"
    },
    "complete_collar_retained_mean_and_jumps_received_upper": {
      "ball": "[2.51443679118195699787367758122768539117259366579939123524425859694202437944e+316 +/- 2.80e+241]"
    },
    "complete_nonroot_source_sum_upper": {
      "ball": "[4.56106007409224152018533409396555028513020791167381919463794922770257378533e+316 +/- 4.47e+241]"
    },
    "complete_reduced_received_source_upper": {
      "ball": "[1.90736423682251400641766771203225487061996663267347748430927102916501134114e+323 +/- 1.25e+248]"
    },
    "complete_retained_five_thirds_profile_upper": {
      "ball": "[3.65037914949006544002698047664631418007998333393869317039923998240367419281e+202 +/- 2.06e+127]"
    },
    "complete_retained_two_profile_upper": {
      "ball": "[4.34800324717376297972304227815162925018900601695393418289939811829170342259e+204 +/- 1.89e+129]"
    },
    "complete_same_negative_error_upper": {
      "ball": "[4.56106007409224152018032214160376163184075594590616953941602114703272102345e+316 +/- 3.45e+241]"
    },
    "complete_same_reduced_error_upper": {
      "ball": "[1.90736423682251400641766771203225487061996663267347748430927102916501134114e+323 +/- 1.26e+248]"
    },
    "complete_same_whole_error_upper": {
      "ball": "[1.90736423682251400641766771203225487061996663267347748430927102916501134114e+323 +/- 1.25e+248]"
    },
    "complete_strict_dyadic_contribution_upper": {
      "ball": "[4.87428600400247394812343307442908744131768664526933084283055677842961003054e+315 +/- 1.13e+240]"
    },
    "complete_strict_retained_and_mean_ordinary_upper": {
      "ball": "[1.04993140574524359549635755299286511958658680187711148746878778580948699543e+315 +/- 1.94e+240]"
    },
    "complete_strict_retained_mean_and_jumps_received_upper": {
      "ball": "[2.01377709469874454348229190196160813952867474430630709706416133852126655813e+317 +/- 3.50e+242]"
    },
    "complete_whole_received_source_upper": {
      "ball": "[1.90736423682251400641766771203225487061996663267347748430927102916501134114e+323 +/- 1.24e+248]"
    },
    "strict_B_c_upper": {
      "ball": "[8.42103831668428386668619632568159540924835998188047041329819847298842972045e+235 +/- 1.62e+160]"
    },
    "strict_B_t_upper": {
      "ball": "[9.10863193887094504525828961928644347593236785796418851203521546448110911151e+225 +/- 1.28e+150]"
    }
  }
}
```


## Appendix B. All forty-four original scalar record objects

These exact objects are the original copies carried by this execution. The source's full path specification and Section3 identities bind them to the five complete old input files.

```json
{
  "Bessel_prefactor": {
    "ball": "[4.32674871092222514696491493234032876517560776049805173263924858362506279049 +/- 8.2e-78]"
  },
  "C_1": {
    "ball": "[191.8008246709565927797721403602769765475928447442644431106228330 +/- 1.50e-62]"
  },
  "C_O": {
    "ball": "[144.1364251833792583628990099208150998341999763036812790334467110 +/- 4.93e-62]"
  },
  "C_R": {
    "ball": "[2038.396873263098707542075374849093828633432756529021035448899354 +/- 3.80e-61]"
  },
  "Calg": {
    "ball": "[21334995458.2617317922131025794903520236605002743919069185868910377932054395 +/- 3.53e-65]"
  },
  "D_infinity": {
    "ball": "[2332847789.36260990230642073488324617852043430230187795053228301114686712271 +/- 3.40e-66]"
  },
  "Lrec": {
    "ball": "[4181844.14552383297616163326915204219390193419381147548707743087111723866719 +/- 4.49e-70]"
  },
  "N_minus4_3_upper": {
    "ball": "[0.000353365678957199556061688669104195383226755979071028582227403507686167109710 +/- 4.74e-79]"
  },
  "N_minus5_3_upper": {
    "ball": "[4.84485135891744585521108222415284249996400645047740736779623648386625368160e-5 +/- 4.40e-80]"
  },
  "RF": {
    "ball": "[2915432922793357.156724578277014851221391740910554139 +/- 4.68e-37]"
  },
  "Rplus": {
    "ball": "[30660269163968914982109729435.4771319902267658817347810102235838415051898056 +/- 2.77e-47]"
  },
  "collar_raw_mean": {
    "ball": "[5.09215384879890697330762529286228791107568849537392964653115505005635409804e+319 +/- 2.91e+244]"
  },
  "complete_terminal_dyadic_contribution_upper": {
    "ball": "[8.00858488235437792087641489166750919537047231324830110312864496566935689806e+162 +/- 2.31e+86]"
  },
  "dyadic_one_third": {
    "ball": "[0.225388660941768411848937895200456938979079214787810126918936162803929778332 +/- 4.14e-77]"
  },
  "dyadic_two_thirds": {
    "ball": "[0.0242046948335741875508791270915959402605580106707967758571815970904235081019 +/- 3.78e-77]"
  },
  "ell_minus_negative_fourth_upper": {
    "ball": "[3.76060309325562070733253499824415267217296755265025139066147752251855572103 +/- 4.55e-75]"
  },
  "ell_plus_one_fourth_upper": {
    "ball": "[0.265914794847249430812512142890325807530086922385195453388784486346011606249 +/- 3.18e-76]"
  },
  "inverse_phase_derivative_1": {
    "ball": "[26.8321948564818956814975591092788530467362242945934112849325398661342471640 +/- 4.74e-74]"
  },
  "jump_collar": {
    "ball": "[7.75606007655515967558999012405048857946293876810010816092847637407788647064e+232 +/- 2.41e+157]"
  },
  "jump_strict": {
    "ball": "[4.64664255670958269813320581961296592311099446254379250546328736283910257886e+224 +/- 4.41e+149]"
  },
  "local_B_c_upper": {
    "ball": "[67836897194301246414643444642537637429252677661116802221294528009932170005.2 +/- 0.0382]"
  },
  "phase_pullback_L2": {
    "ball": "[5.17998019846426591352019839042076862357591977138525322106918823524708814738 +/- 1.74e-75]"
  },
  "prior_reduced": {
    "ball": "[1.90736423682251400641766771203225487061996663267347748430927102916501134125e+323 +/- 3.57e+248]"
  },
  "prior_whole": {
    "ball": "[1.90736423682251400641766771203225487061996663267347748430927102916501134125e+323 +/- 3.56e+248]"
  },
  "profile_normalized_0": {
    "ball": "[58746.1354586494726979333060462847121615091627277530923376618505318612465418 +/- 3.08e-71]"
  },
  "profile_normalized_1": {
    "ball": "[626137747427819624934591820570.758089157181749750847992357424161971620577097 +/- 4.83e-46]"
  },
  "profile_normalized_2": {
    "ball": "[22326889535166955063463910598359600816518155658560.7304134306769400103292609 +/- 4.24e-26]"
  },
  "profile_normalized_3": {
    "ball": "[2.79341715142453655832449358209318442847886467261775852514171922029184036059e+74 +/- 0.480]"
  },
  "profile_normalized_4": {
    "ball": "[4.98039899541140607213764991921090019691533437447992426353849983035471705048e+93 +/- 4.49e+18]"
  },
  "relative_positive_phase_1": {
    "ball": "[19839.1178235962011081929822784687995067113369836738843572345737926974288559 +/- 6.42e-73]"
  },
  "relative_positive_phase_2": {
    "ball": "[802417605.813681702987453791552294586586248154071370463622444720705588561248 +/- 2.87e-68]"
  },
  "relative_positive_phase_3": {
    "ball": "[48676304227073.8582038189778760828142461467197256694867279505650086558941143 +/- 4.34e-62]"
  },
  "retained_amplitude_angle_0": {
    "ball": "[1.78599948757989743532343657712730258576575973745228670403946793803028560380e+91 +/- 3.39e+16]"
  },
  "retained_amplitude_angle_1": {
    "ball": "[1.61217550257582473230941320226992604235092872868044710134111778410793953326e+100 +/- 2.52e+25]"
  },
  "retained_amplitude_angle_2": {
    "ball": "[6.41956708244232258313872524081401209900579281408247752650375512227267154018e+108 +/- 1.36e+33]"
  },
  "retained_amplitude_angle_3": {
    "ball": "[1.34152147477156078476947888771398692467517128336473125751431191265974744392e+117 +/- 1.58e+42]"
  },
  "retained_amplitude_angle_4": {
    "ball": "[2.36000587195006389403771681295666665209920986323699558353721199725070638624e+134 +/- 2.38e+59]"
  },
  "sqrt_ell_plus_upper": {
    "ball": "[0.0707106781186547524400844362104849039284835937688474036588339868995366239231 +/- 5.37e-78]"
  },
  "sqrt_two_upper": {
    "ball": "[1.41421356237309504880168872420969807856967187537694807317667973799073247846 +/- 2.11e-75]"
  },
  "strict_IJminus2": {
    "ball": "[1866343711593823687222.95578852919829407266073319335152034842500206697260902 +/- 2.37e-54]"
  },
  "strict_Jminus5_3": {
    "ball": "[2055209043913351107540053009634105.88217038334465777566527659943927668893231 +/- 2.69e-42]"
  },
  "strict_primitive_mean": {
    "ball": "[1.27303846219972674332690632321557197776892212384348241163278876251408852451e+319 +/- 7.24e+243]"
  },
  "two_one_sixth_upper": {
    "ball": "[1.12246204830937298143353304967917951623241111061398675344040954588290400557 +/- 4.14e-75]"
  },
  "waist_endpoint": {
    "ball": "[5.01195236178865328945196576764965522192808066985276188101744324398376477288e+295 +/- 3.99e+220]"
  }
}
```
