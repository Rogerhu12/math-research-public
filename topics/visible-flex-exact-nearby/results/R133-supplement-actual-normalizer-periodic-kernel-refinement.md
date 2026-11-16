# Proved actual periodic weighted-kernel refinement of the complete normalizer inverse

Proved from the unique public Actions run [43778474673/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43778474673), with scientific exit status 0 and all 18 gates passed. This is the first completed NPK evaluation. It reads the completed NW conclusion and evaluates only the new periodic-kernel square and positive products, one new adjoint candidate, two comparisons of whole norm records, and the four complete conditional affine coefficients.

The new complete $L^2$ and $H^{-4/3}$ bounds both improve the original NW candidates. The old successful mathematical work was not repeated: in particular the low-order exponential, all logarithms, the two optional Neumann verdicts, the Fourier bounds, and every earlier transport or angle calculation are read without reevaluation. Both weighted mean corrections and the two independent physical means remain part of the same inverse.

## 1. Exact evidence and public execution

| Item | Exact path or identity |
|---|---|
| Analytic NPK contract | [Complete normalizer inverse from the periodic weighted kernel](R133-supplement-complete-normalizer-inverse-from-periodic-weighted-kernel.md) |
| Scientific source | [fourfold_codazzi_normalizer_periodic_kernel_refinement.py](../scripts/fourfold_codazzi_normalizer_periodic_kernel_refinement.py) |
| Public worker | [fourfold_codazzi_normalizer_periodic_kernel_refinement_public_worker.py](../scripts/fourfold_codazzi_normalizer_periodic_kernel_refinement_public_worker.py) |
| Frozen inputs | [NPK CI inputs](../notes/2026-11-15-R133-normalizer-periodic-kernel-refinement-CI-inputs.json) |
| Workflow | [visible-normalizer-periodic-kernel-refinement.yml](../../../.github/workflows/visible-normalizer-periodic-kernel-refinement.yml) |
| Complete actual execution | [execution.json](../notes/normalizer_periodic_kernel_refinement_ci/run-43778474673-1/execution.json) |
| Original small result | [actual-result.md](../notes/normalizer_periodic_kernel_refinement_ci/run-43778474673-1/actual-result.md) |
| Original complete NW success | [NW actual proof](R133-supplement-actual-cohomological-normalizer-windows-and-global-sign-correction.md) and [NW execution](../notes/cohomological_normalizer_windows_sign_ci/run-43775614821-1/execution.json) |

| Object | Git blob | Bytes | SHA256 |
|---|---|---|---|
| NPK contract | `0cfdef792fbaf5eff1b6e3d49d404aab9bb0c135` | 11251 | `1ab985bcc97d40c63ab7ea0163746256cf9edc3d79233d990ca0189fa39b57b9` |
| NPK scientific source | `e1c79dbebc478182281c48aaba223651203766a5` | 30655 | `67d54e08d0c72583f198285ef555bb5dc55b2984d4708f9d65044c925a6c3a08` |
| NPK worker | `a2a5ad54f490effba6ee039a97b8c601ed11b7f5` | 39812 | `7dc92fb08c27ab9ff56678a0b6a3176a9127ca1d68597771b69124ce9ee495a1` |
| NPK manifest | `3e131dca6a9a709e00472c242e9e4291cf6d76dc` | 6098 | `950be9b64d5f25bba6b53ba8a979ce01b389f1987468824e902d71fbcce3bb6e` |
| NPK workflow | `2e39229a6a06d93ae862dd0019d05cff562e8000` | 4273 | `d4559887a643403f88764b60dd05a90b86c0069dcfe1794e44dcbc66e4c4dafa` |
| NPK execution | `f9d25679cf6f3749b20916cc07d7b4d424fe3cc2` | 36028 | `c76e9bee0541c2e042abcc9b2da83530c00c6b3ddf6e6b525531ca56d7ce609f` |
| NPK original result | `9078ae915c1fb3b51adc4e529a4585f6bfe6561d` | 2271 | `48e73b8933313384f49aa00a098bf222dd9adea281ed34a2c25051262ca8ad63` |
| NW execution read | `1215ffc9eb7b4171b661483fea474e2b65ca2f28` | 35204 | `1e327e83dafb5d09ec98acc6ba887ae28962a7f242be7e82692a864c2f93cb0b` |

The deployment head and actual scientific checkout are both `12ae0a1e822b953ce3a2b96287ee3c0af0243992`. The Actions API identifies one push run for that head, run number 1, attempt 1. The run was created and started on 2026-11-16 at 00:07:18 UTC, and its final status is `completed/success`. Job `133010076980` ran from 00:07:20 through 00:07:54 UTC; every one of its 12 returned steps completed successfully.

The scientific runtime is Python `3.12.14`, `python-flint 0.9.0`, at 320 arithmetic bits. The worker recorded one scientific child and no old scientific child. Its elapsed child time was `0.21412824799999441` seconds; the complete scalar evaluation recorded `0.0029676980000061803` seconds. Those timings are copied metadata, not additional numerical tests.

## 2. Same selected function, complete means, and unchanged original records

The object is the original full-circle normalizer
$$
 N=\operatorname{Id}+M_w I,\qquad
 w(x-\Omega)-w(x)=v(x),\qquad
 p=Iw,\qquad \langle w\rangle=\langle p\rangle=0 .
 \tag{NPKA.1}
$$
The physical period is $\ell=\pi/2$, the nonzero physical frequency is $4|j|$, and the angular $L^2$ measure is normalized. Ordinary integration in the Green kernel still uses $dt$ and therefore keeps the factor $\pi/2$.

The same selected common input remains
$$
 S=U_{H^{-1}}U_{X_-}
   =U_{X_-\circ H^{-1}},\qquad
 |\delta|\le 0.00000000009368259853002 .
 \tag{NPKA.2}
$$
The inverse order is $S^{-1}=U_{X_-^{-1}}U_H$. These factors were not exchanged. The continuous-centre and response identities remain respectively
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47` and `6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`.

The accepted NW execution is run `43775614821/1`, with its original source `c8352847b0bd8df141c4aeb97d4dab372b807d7d18546d2b93659f95011cd75f`, manifest `d66bc4a1fb2251f421a3feebef727352f92b252bf810892e732f008ebe5bad40`, and scientific checkout `a7ca18a0bff4a48ccdde5abd44f6d0f01ee17c78`. Its complete scientific JSON is 24234 bytes with SHA256 `55019238a3b762aaeace163a81da85b3c63c3034679ca23521d3c41b28b9e7aa`. NPK verifies that full canonical object and both original process/summary output identities before reading any new scalar target.

Eight whole objects are retained verbatim: `Fourier`, `windows`, `global_sign_and_affine`, `absolute_mu_and_CI`, `original_signed_mu`, `whole_path_scope`, `selected_common_input_scope`, and `original_scope`. The complete whole-object payload has SHA256 `539b86f06d7cb855b3d708eaf5cf0aa3162f27a700dd1b608f7ccd4374713021`. Independent comparison against the original NW execution verifies every one of those eight objects exactly.

The 13 actual scalar records used by the new consumer are reproduced below without changing their ball strings:

| Original complete record | Role | Exact original outward ball |
|---|---|---|
| $W_0$ | Complete Wiener bound for the true $w$ | `[418.595260838987995505643223856493412253619158936018083523968 +/- 4.82e-58]` |
| $B=W_{1/3}(w)$ | Complete intermediate-window multiplier bound | `[1713.22719641220703551430416736734738861014996889919326573260 +/- 4.95e-57]` |
| $P_0$ | Complete bound for the true $p=Iw$ | `[41.0860793880272764445248493459369956571120785389987091311822 +/- 4.05e-59]` |
| $E_0$ | Previously evaluated upper bound for $e^{P_0}$ | `[697360848278474303.937246497506776353989984705221526645631508 +/- 5.82e-44]` |
| $C_I$ | Original primitive constant | `[1.03077640640441513745535246399351925628679980634340510859966 +/- 1.61e-60]` |
| $C_I B$ | Original complete adjoint product, read directly | `[1765.95417287208587472463965323662545520773434929158700817209 +/- 2.16e-57]` |
| $K_{0,\mathrm{old}}$ | Original complete $L^2$ inverse bound | `[2.47493935061110791087365845925163148549123796035772184065025e+73 +/- 4.52e+13]` |
| $K_{-,\mathrm{old}}$ | Original complete $H^{-4/3}$ inverse bound | `[1.88583098292151044882195623702957671230939653905963901485692e+79 +/- 1.64e+19]` |
| $F_-$ | Original complete forward $N$ bound on $H^{-4/3}$ | `[156574.254929763192759730331343553446308945711968624965494928 +/- 3.66e-57]` |
| $C_{wZ}$ | Original full-sign commutator bound | `[3640.60779237593995046789635565561320079656868391078568968179 +/- 4.49e-57]` |
| $Q_*$ | Original complete two-primitive majorant | `[80855.3629399347925923003167331569284445784417557758700251122 +/- 3.24e-57]` |
| $A_{-,\mathrm{factor}}$ | Original complete factor in the conditional $A$ bound | `[31.9757595779885647046113030260614148387103007769720210991831 +/- 1.98e-59]` |
| $\mu^2/4$ fee | Original linear-model scalar fee, not removed | `[1365.79601183901162185423859228267945285056002368651115880249 +/- 2.37e-57]` |

The complete 13-record payload has SHA256 `e4364eba0aba2e965d7193fc3169a5a5f9bc43ce009ebe8a88d5cc021ca4d2a0`; independent comparison with the same original NW fields verifies every scalar record. The full signed original $\mu$ record, including its separate lower and upper endpoints, remains in the copied whole object. NPK neither replaces it by an independently rounded number nor computes another $\mu$ fee.

The copied transport scope remains complete: 3146 original intervals, 12584 complete subcells, 1256 completed prefix subcells read and 11328 new suffix subcells from that earlier success, with exact radial cursor `0`. No prefix is substituted for the complete terminal conclusion. All old log-only records and the failed optional Neumann tests remain unchanged; their failure never asserted noninvertibility.

## 3. Newly evaluated periodic-kernel bound

The NPK contract proves the exact same inverse using $a=e^p$, the original two weighted means, and a kernel bracket of absolute value at most 1. Consequently
$$
 \|z\|_2\le \frac{\pi}{2}E_0^2\|f\|_2,\qquad
 \|N^{-1}\|_{L^2\to L^2}
 \le K_{0,\mathrm{kernel}}
 :=1+W_0\frac{\pi}{2}E_0^2 .
 \tag{NPKA.3}
$$
Both mean corrections are retained in that exact kernel; no pointwise inversion of $1+wI$ is used. This run reads $E_0$ and evaluates its square. It does not reevaluate an exponential.

| New complete record | Exact outward ball |
|---|---|
| Physical ordinary circumference $\ell=\pi/2$ | `[1.57079632679489661923132169163975144209858469968755291048747 +/- 2.30e-60]` |
| Saved exponential squared $E_0^2$ | `[486312152711673257557323850526044828.072820398077831952774731 +/- 3.55e-25]` |
| Kernel primitive bound $(\pi/2)E_0^2$ | `[763897343155215176365111342893750705.104301143858976051781872 +/- 2.50e-25]` |
| Complete kernel inverse bound $K_{0,\mathrm{kernel}}$ | `[319763807612267217812380107408107915391.756084395514054702024 +/- 1.14e-22]` |

The two entire retained $L^2$ candidate records are:

| Candidate | Exact outward ball | Selected |
|---|---|---|
| `complete_periodic_weighted_kernel` | `[319763807612267217812380107408107915391.756084395514054702024 +/- 1.14e-22]` | yes |
| `original_NW_complete_L2_norm` | `[2.47493935061110791087365845925163148549123796035772184065025e+73 +/- 4.52e+13]` | no |

Selection compares the upper endpoints of the final retained outward records. It preserves the original NW candidate on a tie, as specified by the source's ordered candidate list. Both candidates bound the same complete inverse on the same window; the result is a whole-record choice, not an entrywise combination. The new kernel record is selected.

## 4. Newly evaluated adjoint bootstrap and complete negative-window choice

The previously proved adjoint bootstrap applies to the selected complete $L^2$ inverse first, and only then gives the same inverse on $H^{-4/3}$:
$$
 K_{-,\mathrm{new}}
 =1+(C_I B)+C_I(C_I B)\,W_0\,K_0 .
 \tag{NPKA.4}
$$
Here the parenthesized $C_I B$ is the original complete scalar record. The old adjoint calculation is not repeated. The second mean and both physical mean coordinates remain present through the bootstrap and duality.

| New complete adjoint record | Exact outward ball |
|---|---|
| Selected complete $K_0$ input, read verbatim | `[319763807612267217812380107408107915391.756084395514054702024 +/- 1.14e-22]` |
| Original $C_I B$ input, read verbatim | `[1765.95417287208587472463965323662545520773434929158700817209 +/- 2.16e-57]` |
| New product $C_I(C_I B)W_0K_0$ | `[243650615302257743804058281540446752851929437.348978515319525 +/- 2.12e-16]` |
| Complete new $H^{-4/3}$ inverse | `[243650615302257743804058281540446752851931204.303151387405400 +/- 6.34e-17]` |

The two complete negative-window candidate records are:

| Candidate | Exact outward ball | Selected |
|---|---|---|
| `complete_adjoint_from_kernel_selected_L2` | `[243650615302257743804058281540446752851931204.303151387405400 +/- 6.34e-17]` | yes |
| `original_NW_complete_negative_norm` | `[1.88583098292151044882195623702957671230939653905963901485692e+79 +/- 1.64e+19]` | no |

The new adjoint record is selected. These are actual evaluated norm certificates; the old logarithmic certificates have not been exponentiated or substituted into products. The chosen two bounds apply to the same complete $N^{-1}$, and to its rotated $N_-^{-1}$ in the original order.

## 5. Four complete conditional affine coefficients

With the chosen whole $K_0$ and $K_-$, the original exact global-sign formula gives
$$
 \begin{aligned}
 B_Z&=K_0 C_{wZ}K_-F_-,&
 A_Z&=B_Z A_{-,\mathrm{factor}},\\
 A_{\mathrm{Cay}}&=K_0Q_*+A_Z,&
 B_{\mathrm{Cay}}&=K_0F_-+B_Z .
 \end{aligned}
 \tag{NPKA.5}
$$
The operator order is left inverse on $L^2$, full sign commutator, right inverse on $H^{-4/3}$, then forward $N$ on $H^{-4/3}$. The second sign commutator and its mean row are included. No global sign has been replaced by a scalar sector.

| Complete conditional coefficient | Exact outward ball |
|---|---|
| $A_Z$ | `[1.42007714241732765623777032956907211562876568821795842337732e+93 +/- 4.05e+31]` |
| $B_Z$ | `[4.44110526586170190068923025491753692350251084622018478853401e+91 +/- 3.90e+31]` |
| $A_{\mathrm{Cay}}$ | `[1.42007714241732765623777032956907211562876568821798427799604e+93 +/- 4.15e+32]` |
| $B_{\mathrm{Cay}}$ | `[4.44110526586170190068923025491753692350251084622519146652705e+91 +/- 3.39e+31]` |

Thus the new coefficients may be consumed in their original conditional forms
$$
 A_Z+B_Z C_E,\qquad
 A_{\mathrm{Cay}}+B_{\mathrm{Cay}}C_E .
 \tag{NPKA.6}
$$
All four coefficients form one complete candidate. Their entries are not independently mixed with entries of the old NW affine candidate. The corresponding complete old affine object remains copied verbatim.

The complete strong error $C_E$ is still symbolic and unpaid. In particular no paid subtotal from WE or another partial receiver has been inserted in its place. The old linear-to-exponential $\mu^2/4$ fee is copied and retained; this calculation does not remove that fee from the linear model or rename an old linear remainder as a Cayley remainder.

## 6. Actual gates, counts, and exact input closure

| Gate | Actual complete condition | Passed |
|---|---|---|
| 1 | only the new kernel scalar arithmetic runs in public Actions at the frozen runtime | true |
| 2 | seven current small inputs and all new parameters are frozen before evaluation | true |
| 3 | every complete immutable size SHA and small text type is checked | true |
| 4 | the same two-mean inverse adjoint bootstrap and complete conditional global-sign proof are retained | true |
| 5 | the original NW run is a complete same-identity actual success | true |
| 6 | the complete original NW science has its exact canonical bytes hash and both original small outputs | true |
| 7 | the original true w p full-circle means and the selected common-input order are preserved | true |
| 8 | thirteen saved scalar records are complete positive same-operator budgets | true |
| 9 | the complete periodic kernel bound uses ordinary pi/2 length and both weighted means | true |
| 10 | the L2 comparison selects one whole retained outward record for the same inverse | true |
| 11 | the negative candidate uses the chosen complete L2 inverse in the proved adjoint order | true |
| 12 | the negative comparison also selects one whole retained outward record | true |
| 13 | four complete new affine coefficients keep the actual left and right inverse windows | true |
| 14 | the complete global sign and physical mean scope does not grant the unpaid C_E | true |
| 15 | all eight original complete objects and thirteen scalar records stay verbatim | true |
| 16 | only the one new square kernel product two whole choices and four affine products are evaluated | true |
| 17 | all complete retained ball records are finite and every scope condition is retained | true |
| 18 | the complete small result including all old and new candidates fits its reserved envelope | true |

| Actual count | Recorded value |
|---|---|
| `original_successful_small_receipts_read` | 1 |
| `original_complete_objects_read_verbatim` | 8 |
| `saved_scalar_records_read` | 13 |
| `new_physical_length_constants` | 1 |
| `new_saved_exponential_squares` | 1 |
| `new_complete_L2_kernel_candidates` | 1 |
| `new_complete_adjoint_negative_candidates` | 1 |
| `new_complete_norm_whole_choices` | 2 |
| `new_complete_conditional_affine_coefficients` | 4 |
| `new_exponential_evaluations` | 0 |
| `new_logarithm_evaluations` | 0 |
| `new_optional_Neumann_tests_evaluated` | 0 |
| `new_Fourier_or_target_budgets_evaluated` | 0 |
| `old_numerical_enclosures_recomputed` | 0 |
| `old_NW_or_PIB_budgets_recomputed` | 0 |
| `old_scientific_producer_imports` | 0 |
| `old_scientific_producer_calls` | 0 |
| `old_binary_or_archive_inputs_restored` | 0 |
| `new_angular_or_radial_integrals_evaluated` | 0 |
| `original_input_bytes_modified` | 0 |

The successful scientific object has exactly 60 retained top-level fields. The two additional failure-only whitelist fields are absent in this success. Every scope flag is true, while `complete_C_E_supplied`, `full_physical_incoming_inverse_claimed`, `finite_Schur_inverse_claimed`, `full_return_R0_claimed`, and `actual_nonlinear_background_claimed` all remain false.

Before the scientific child, the worker copied and verified seven complete current small text inputs, covering all 160477 pinned bytes. Their complete receipt digest is `bad3e682e5edc5f48f03487e98a0a2d4dddc8b9edd3450a61753907f6406edd3`. The original NW source is parsed as text/AST evidence; it is neither imported nor executed as a producer.

| Complete frozen input | Bytes | SHA256 |
|---|---|---|
| `notes/cohomological_normalizer_windows_sign_ci/run-43775614821-1/execution.json` | 35204 | `1e327e83dafb5d09ec98acc6ba887ae28962a7f242be7e82692a864c2f93cb0b` |
| `results/R133-supplement-complete-cohomological-normalizer-windows-and-global-sign-correction.md` | 19754 | `1469fdd05417284743e7857aabe0324ee67ccb1b7dbaa003461364d8c9447938` |
| `results/R133-supplement-complete-normalizer-inverse-from-periodic-weighted-kernel.md` | 11251 | `1ab985bcc97d40c63ab7ea0163746256cf9edc3d79233d990ca0189fa39b57b9` |
| `results/R133-supplement-complete-principal-inverse-adjoint-bootstrap-from-L2.md` | 11316 | `2d74b71c0584cb5ec1af849b6fb5756e48da58bf313d72be62d582d557d23acb` |
| `results/R133-supplement-exact-full-circle-subprincipal-normalizer-and-strong-remainder-budget.md` | 15615 | `427387a2f3836d95b5f79546f0c6d41e8d6307abbb76611073d2801364fda9db` |
| `scripts/fourfold_codazzi_cohomological_normalizer_windows_sign.py` | 36682 | `c8352847b0bd8df141c4aeb97d4dab372b807d7d18546d2b93659f95011cd75f` |
| `scripts/fourfold_codazzi_normalizer_periodic_kernel_refinement.py` | 30655 | `67d54e08d0c72583f198285ef555bb5dc55b2984d4708f9d65044c925a6c3a08` |

The full Python AST closure contains exactly the NPK and NW sources. Its digest is `568db898806e29cc7d89e612c702e8a9d7af96c9d1085f24b3dba413b2e989fa`. Independently reconstructing the complete seven input receipts in manifest order and the two AST entries reproduces both recorded digests exactly. The separately pinned manifest and reviewed rules are additionally checked; they are not counted a second time as scientific input files.

## 7. Complete small results, recoverability, and publication evidence

| Complete object | Bytes | SHA256 |
|---|---|---|
| Canonical scientific process/summary JSON | 25650 | `bbeb12f723b5bb65326d399132e1be08b39383b68989879c52630d68df52391d` |
| Complete pre-publication result and execution payload | 29917 | `972f36ade45a85e1126844b2f17814de4dc4b8686a131f08775399b68ad46fa4` |
| Temporary native gzip, not published | 7053 | `93627d5c9fc59ef6035493c67b8d2aaec6b761dade6fa1946a86e6190e56bed3` |
| Original scientific stdout log | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| Retrieved complete run metadata | 13314 | `aea9ad234fc65c7d59146f31548482aa333109943e537aee8b8431493b7c221b` |
| Retrieved complete jobs metadata | 3238 | `21b71c384c1b6e66bf9d649de8f09bae2063231a387a5b32ca4e52ba6ef92d18` |

The complete process and summary JSON identities are identical. A lexical JSON reconstruction preserves every original numeric token, sorts the original keys as the producer did, and adds the original final LF; it reproduces the full 25650-byte scientific hash above. The same method rebuilds the complete pre-publication payload from the retained result text and exact execution fields, reproducing all 29917 bytes and its hash. This checks complete objects, not a selection of visible ball strings.

The worker printed that complete small payload before any publication operation. It remains below its 59000-byte envelope. The temporary native name is `temporary-normalizer-periodic-kernel-refinement.json.gz`; only its complete identity is retained publicly. No native array, old archive, Release, or reproducible data artifact is uploaded.

Two actual terminal pulls and README comparisons were recorded at `2026-11-16T00:07:47.281616+00:00` and `2026-11-16T00:07:48.835350+00:00`. Both had before/after head `12ae0a1e822b953ce3a2b96287ee3c0af0243992` and an empty README diff. The reviewed rules identity is `65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1`.

The actual metadata-only published topic inventory recorded 199274929 bytes and 14529 blobs before this result. The scientific reserve check therefore passed with the full 120000-byte reserve. The final two-file projection was 199313228 bytes, below 200000000. The exact owned HEAD delta was empty at the base; publication was confined to this run's two small result files. No unpinned file was deleted or substituted by this worker.

## 8. Exact usable conclusion and remaining interfaces

For the same selected real $w$ and $p$, the actual run proves complete bounds for
$$
 N^{-1}:L^2\longrightarrow L^2,\qquad
 N^{-1}:H^{-4/3}\longrightarrow H^{-4/3},
 \tag{NPKA.7}
$$
with the two whole selected records in Sections 3 and 4, the same inverse on their common dense domain, and the corresponding rotated inverse. Full scalar means and the two independent physical means are retained. The four new complete conditional coefficients in Section 5 are available in the stated order.

The coefficient $w$ is the true cohomological solution from the difference of the individual principal coefficients. These new bounds concern $N$; they do not replace or recompute the separately certified individual incoming/outgoing principal inverses. They do not supply a physical incoming inverse, a finite Schur inverse, an actual nonlinear background, or a complete return remainder. Complete $C_E$, the remaining true incoming/outgoing errors, the finite rows and positive stable interface remain separate obligations.

No successful mathematical target is rerun to obtain this report. All numbers in the tables are copied from the immutable completed execution, and all independent checking here is text, schema, metadata, or exact JSON/hash reconstruction.
