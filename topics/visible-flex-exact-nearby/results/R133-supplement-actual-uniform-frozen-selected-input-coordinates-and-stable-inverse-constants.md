# R133 supplement: actual uniform frozen reflected input coordinates and stable inverse bounds

## NIFA1. Proved from the unique public run

The unique [public push run 43795909913, attempt 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43795909913) completed successfully. Its one scientific child returned zero and passed all **16** gates. The complete [scientific conclusion](../notes/frozen_common_input_uniform_inverse_constants_ci/run-43795909913-1/actual-scientific-conclusion.json), [execution receipt](../notes/frozen_common_input_uniform_inverse_constants_ci/run-43795909913-1/execution.json), and [actual report](../notes/frozen_common_input_uniform_inverse_constants_ci/run-43795909913-1/actual-result.md) retain 32 scientific fields, all 15 actual progress entries, all three new mathematical graphs, and all **23** new interval records.

This is the actual scalar consumer of the [final NIF contract](R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md). It proves seven new quantitative bounds: one forward terminal-Ai leading modulus, two directions of the common input coordinate map in each of two Sobolev windows, and two stable inverse bounds on the correctly reflected frozen input space. Sixteen elementary factors are saved separately. Every original bound, exponential, logarithm, R97 comparison and RNE inverse polynomial is read from its already completed result. None is reevaluated.

The trigger commit is `9948aec967519e5b39535443f55adfcfb7e9d8f3`. The actual scientific checkout after the genuine pull is **`bc20ed50d94fc4236f887d71696d353d3c945c3c`**. They are different and are retained separately. The complete current input hashes were verified at the actual checkout.

The family is exactly the original real reference family
$$
 Q_\delta=Q_0+\delta Z_{\rm can},\qquad
 \nu_\delta=\nu_0+\delta,\qquad
 |\delta|\le 10^{-8},\qquad \eta_0\ \text{fixed}.
 \tag{NIFA.1}
$$
The fixed intrinsic parameter, original root bracket and strict cut are
$$
 \eta_0=-\frac{7789843107295549}{4611686018427387904},\qquad
 r_*\in\left[
 \frac{1191984371497}{5000000000000},
 \frac{2383968743003}{10000000000000}\right],\qquad
 r_c=\frac{76285779072683}{320000000000000}.
 \tag{NIFA.2}
$$
The root remains in original piece 2549. The physical period is $\pi/2$, the angular measure is normalized, and physical frequency is $n=4|j|$. The natural high cutoff is $|j|\ge97$; the common-root normalizer keeps its distinct actual cutoff $J_F=1024$. No inverse frequency is applied to either independent physical mean.

## NIFA2. Seven complete new principal bounds

Every interval below is copied literally from the public science. The certified upper endpoint of each complete record is used for the indicated norm bound. The two natural inverse constants underneath these products are the already saved RNE bounds in the respective negative windows, not the old $L^2$ gap bound reused in a different norm.

| New bound | Complete saved interval record |
|---|---|
| $K_\Lambda^+$, complete forward terminal-Ai leading modulus | `[141.193338114685244512497543235565477903811740354802032645655700902537200683 +/- 6.84e-74]` |
| $A_0$, upper for $\|N_i^{\rm fr}:\mathcal X_0^{\rm fr}\to\mathcal H_{\rm nat}^{0}\|$ | `[58.4555218876859644080734125988791898352764800412066670928638795018857278065 +/- 2.88e-74]` |
| $B_0$, upper for $\|(N_i^{\rm fr})^{-1}:\mathcal H_{\rm nat}^{0}\to\mathcal X_0^{\rm fr}\|$ | `[776.638118829540202218817534551538271360482147648106777846810552570201825427 +/- 4.70e-73]` |
| $A_{-4/3}$, complete input coordinate norm upper | `[5820880.70108924034549622179082990441640584186735462238854309412204748833574 +/- 1.87e-69]` |
| $B_{-4/3}$, complete inverse input coordinate norm upper | `[53052786824.8448885951218403284570560599254112027527196723364956100751274357 +/- 4.70e-65]` |
| $\|(C_{0,\delta}^{\rm fr})^{-1}:\mathcal H_{\rm nat}^{-1/6}\to\mathcal X_0^{\rm fr}\|$ upper | `[15936238064517.4828057467372890968538119846801465565268662528492477586809519 +/- 4.51e-63]` |
| $\|(C_{-4/3,\delta}^{\rm fr})^{-1}:\mathcal H_{\rm nat}^{-3/2}\to\mathcal X_{-4/3}^{\rm fr}\|$ upper | `[22522836490233569635107454255538470713632.6498065587114788209249542737189971 +/- 3.47e-35]` |

The exact coordinate order is
$$
 N_{i,\delta}^{\rm fr}
   =\Lambda_{+,\delta}^{-1}T_{F,\delta}^{-1}\mathcal S_*^{-1},
 \qquad
 (N_{i,\delta}^{\rm fr})^{-1}
   =\mathcal S_*T_{F,\delta}\Lambda_{+,\delta}.
 \tag{NIFA.3}
$$
The actual bounds are the complete positive products
$$
 A_s=K_\Lambda^-K_{F,s}^-K_{\mathcal S^{-1},s},\qquad
 B_s=K_{\mathcal S,s}K_{F,s}^+K_\Lambda^+,\qquad
 s=0,-4/3.
 \tag{NIFA.4}
$$
Thus $A_s$ bounds $N_i^{\rm fr}:\mathcal X_s^{\rm fr}\to\mathcal H_{\rm nat}^s$, and $B_s$ bounds its inverse in the reverse direction.

The stable map and its inverse keep all original weights in their order:
$$
 \begin{aligned}
 C_{s,\delta}^{\rm fr}
  &=N_{\rm out}^{-1}S_{{\rm nat},\delta}
           N_{\rm in}^{7/6}N_{i,\delta}^{\rm fr}
    :\mathcal X_s^{\rm fr}\longrightarrow\mathcal H_{\rm nat}^{s-1/6},\\
 (C_{s,\delta}^{\rm fr})^{-1}
  &=(N_{i,\delta}^{\rm fr})^{-1}N_{\rm in}^{-7/6}
           S_{{\rm nat},\delta}^{-1}N_{\rm out}.
 \end{aligned}
 \tag{NIFA.5}
$$
The complete uniform inverse bounds are
$$
 \|(C_{s,\delta}^{\rm fr})^{-1}\|
 \le \Gamma_{97}B_s K_{{\rm nat},s-7/6},
 \qquad
 \Gamma_{97}=\frac{150545}{150544}.
 \tag{NIFA.6}
$$
The two cases use the same compatible distributional inverse, transported by the displayed weights and coordinates:

| Frozen input exponent $s$ | Original natural inverse exponent | Stable output exponent |
|---|---|---|
| $0$ | $-7/6$ | $-1/6$ |
| $-4/3$ | $-5/2$ | $-3/2$ |

No factor is commuted through the fixed chart. The positive high weight and the negative weight are charged as in NIF.23--26; the saved natural inverse constants are consumed once. The optional numerical forward bounds for $C_s^{\rm fr}$ were not evaluated. Their finite symbolic bound remains NIF.27.

## NIFA3. All sixteen complete elementary factors

The following table contains the remaining sixteen new records, so Sections NIFA2--3 give all 23 new scalar slots. The two $\pi$ records are complete interval evaluations. The square-root record is a positive lower-endpoint certificate; its lower endpoint is used before taking the inverse. Every other elementary record is an upper bound. This distinction is retained by the source and is not inferred from a printed midpoint.

| Exact scientific field | Complete saved interval record |
|---|---|
| `complete_forward_leading_conclusion.complete_pi_interval` | `[3.14159265358979323846264338327950288419716939937510582097494459230781640629 +/- 3.80e-75]` |
| `complete_forward_leading_conclusion.complete_two_pi_interval` | `[6.28318530717958647692528676655900576839433879875021164194988918461563281257 +/- 2.42e-75]` |
| `complete_forward_leading_conclusion.complete_sqrt_two_pi_lower` | `[2.50662827463100050241576528481104525300698674060993831662992357634229365461 +/- 2.16e-75]` |
| `complete_forward_leading_conclusion.complete_inverse_sqrt_two_pi_upper` | `[0.398942280401432677939946059934381868475858631164934657665925829670657925899 +/- 3.02e-76]` |
| `complete_forward_leading_conclusion.complete_root_k_over_eta_upper` | `[48.3599015229244254223917112077666712956869387989594595694200785324278682169 +/- 9.75e-75]` |
| `complete_forward_leading_conclusion.complete_root_ratio_sixth_upper` | `[1.90874348611766879364140035781151503968447703843762651752245405275313064789 +/- 4.73e-75]` |
| `complete_forward_leading_conclusion.complete_root_to_waist_radial_upper` | `[185.402718043213387658908372830560922767045790839204553360126666298975783592 +/- 4.94e-73]` |
| `complete_forward_leading_conclusion.complete_density_times_radial_upper` | `[185.419998067769074919127151467497455953723370285153267638572419383018301086 +/- 4.05e-73]` |
| `complete_forward_leading_conclusion.complete_forward_leading_prefactor_upper` | `[73.9718768611850356296915651957877930290214330935057535470376121622998240718 +/- 3.97e-74]` |
| `complete_coordinate_conclusion.windows.0.complete_Lambda_TF_inverse_product_upper` | `[11.1125892897547960442347381829974512711589705180450285547740638642240867456 +/- 4.46e-74]` |
| `complete_coordinate_conclusion.windows.0.complete_S_TF_forward_product_upper` | `[5.50052948106312660258015597869135855216693356569365362644950744712812042088 +/- 2.43e-76]` |
| `complete_coordinate_conclusion.windows.-4/3.complete_Lambda_TF_inverse_product_upper` | `[11.2495944636923546587930589387817242577288511501718553387477667883317994850 +/- 2.33e-74]` |
| `complete_coordinate_conclusion.windows.-4/3.complete_S_TF_forward_product_upper` | `[375745679.882944643062633059067841491018036867261657176088166959217953461617 +/- 3.33e-67]` |
| `complete_frozen_stable_inverse_conclusion.complete_gamma97_upper` | `[1.00000664257625677542778191093633754915506430013816558614092889786374747582 +/- 1.03e-75]` |
| `complete_frozen_stable_inverse_conclusion.windows.0.complete_coordinate_times_natural_inverse_upper` | `[15936132207544.0561394157017400099422781986893485881681925880563097717152029 +/- 1.95e-62]` |
| `complete_frozen_stable_inverse_conclusion.windows.-4/3.complete_coordinate_times_natural_inverse_upper` | `[22522686881568451341111405848389408715753.5197613907779127013007825977797515 +/- 3.09e-35]` |

The new forward leading scalar is exactly the positive combination
$$
 K_\Lambda^+
  =n_{g,0,+}\,P_{\rm rev}\,E_{\rm sh}\,
       (2\pi)^{-1/2}
       \left(\frac{k_{*,+}}{\eta_{*,-}}\right)^{1/6}.
 \tag{NIFA.7}
$$
Here $P_{\rm rev}$ is the original reverse radial bound, $E_{\rm sh}$ is the already saved exponential of the complete absolute short rate, and $\eta_{*,-}$ is the positive lower bound on the full original coefficient domain containing the root. It is not a bound transplanted from a cut-only row. The source performs one new $\pi$ evaluation, one new square root and one new positive sixth root, with the lower denominator qualifications retained. It does not reevaluate $E_{\rm sh}$ or an old geometric graph. The same modulus applies to all four original terminal-Ai sign/wave leading scalars; there is no additional sector sum or $\sqrt2$.

The forward leading bound and the inverse coordinate bounds are reparsed from their complete saved interval records before they enter the next positive product. No scalar is recovered by dividing an unrelated saved operator upper bound.

## NIFA4. The fixed reflected domain and the preserved ports

The natural root space is the original reflected high space $\mathcal H_{\rm nat}^s$, not the entire signed carrier space $\mathcal H_{\rm car}^s=P_{97}H^s$. With
$$
 D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_-,
 \qquad
 \Lambda_{+,\delta}=a_\delta D_+,\quad a_\delta>0,
 \qquad
 \mathcal S_*=U_{\mathcal H_*^{-1}}U_{X_{-,\delta_*}},
 \tag{NIFA.8}
$$
the fixed input space with its inherited physical Sobolev norm is
$$
 \boxed{\mathcal X_s^{\rm fr}
    =\mathcal S_*D_+\mathcal H_{\rm nat}^s
    =(N_{i,\delta_*})^{-1}\mathcal H_{\rm nat}^s.}
 \tag{NIFA.9}
$$
This is the corrected inverse-image domain. The fixed phase $D_+$ is essential: it preserves real Fourier conjugacy but does not preserve even reflection by itself.

The complete root normalizer preserves the original reflection because its coefficient $F_*=\beta uv/\eta$ is odd and both $M_{F_*}$ and $I$ change sign under reflection. Its sign commutation follows from the separate actual high cutoff and finite band argument. These two qualifications give, for the entire real family,
$$
 N_{i,\delta}^{\rm fr}(\mathcal S_*D_+f)
       =a_\delta^{-1}T_{F,\delta}^{-1}f,
 \qquad f\in\mathcal H_{\rm nat}^s.
 \tag{NIFA.10}
$$
The resulting reflected projector and the ambient high projector remain distinct:
$$
 Q_{\rm fr}
  =\mathcal S_*D_+Q_{\rm nat}D_+^{-1}\mathcal S_*^{-1},
 \qquad
 P_{\rm fr}=\mathcal S_*P_{97}\mathcal S_*^{-1}.
 \tag{NIFA.11}
$$
The other reflection component is not a finite low-frequency head. The old shorthand $\mathcal S_*\mathcal H_{\rm nat}^s$ is not used.

The high-coordinate maps extend to independently declared ports only as
$\operatorname{diag}(N_i^{\rm fr},1_{\rm rest})$ in the corresponding direction. Both physical means remain independent. The rest can include an infinite-dimensional radial head space, independent second-reference data, low columns and source ports; it is not replaced by a finite vector. A full density pullback preserves the mean functional and need not fix the constant function. Its exact mean-identity finite-rank corrections and inverse counterparts remain.

The selected map $\mathcal H_*$ and $\mathcal S_*$ are frozen at the original selected parameter. This result does not construct a varying selected KAM conjugacy. It proves the two bounded stable trace inverses on (NIFA.9). The original smooth regular given-head graph qualification is unchanged, and rough bulk extension remains governed by the existing SE/FC qualifications. No new complete physical incoming inverse, finite Schur inverse, nonlinear background or final surface is asserted. Restricting an old full-circle principal or Cayley inverse to this reflected subspace requires its own domain/range compatibility; it is not a consequence of these seven scalar products. Operator-norm continuity of the Riccati frame is not asserted.

## NIFA5. All sixteen complete original input records

These values are read from the four successful originals, preserving all original decimal digits and radii. Fourteen entries retain their complete one-key `{"ball":...}` records; the two RNE entries remain original strings. Only `eta_root_lower` is consumed at a strictly positive lower endpoint. The other fifteen are consumed at their upper endpoints. The separately computed square-root lower endpoint in NIFA3 is new, not an additional old record.

| Original record key | Original complete JSON value | Endpoint consumed |
|---|---|---|
| `KF_forward_0` | `{"ball":"[1.04515825851323212722069524929173264052187610381663846849853595402565470 +/- 3.37e-72]"}` | Upper |
| `KF_forward_minus4_3` | `{"ball":"[1.05678696737891142323114182414752655323262586904302827560163616263149079 +/- 7.23e-73]"}` | Upper |
| `KF_inverse_0` | `{"ball":"[1.04729397192346971466575604221266654789993881066352877954482111920497066 +/- 1.01e-72]"}` | Upper |
| `KF_inverse_minus4_3` | `{"ball":"[1.06020587652516472128960751979473279256202439177297140649109225489526729 +/- 1.78e-72]"}` | Upper |
| `KLambda_inverse_upper` | `{"ball":"[10.6107641098566743676210375177543475099037616546566595973215917592748734 +/- 1.61e-71]"}` | Upper |
| `KS_forward_0` | `{"ball":"[5.262867547817867306879019910803827331274181821819889 +/- 1.46e-52]"}` | Upper |
| `KS_forward_minus4_3` | `{"ball":"[355554800.9972958602734947243276105593307920284359492 +/- 1.30e-44]"}` | Upper |
| `KS_inverse_0` | `{"ball":"[5.260297160588737107942783119746478724580916512096002 +/- 6.75e-53]"}` | Upper |
| `KS_inverse_minus4_3` | `{"ball":"[517430.2700311477963576442309386038271752854535066086 +/- 7.40e-48]"}` | Upper |
| `Knat_minus5_2` | `"[424533530272927398350857968257.940198257953239915827785659374693502090360095 +/- 7.25e-47]"` | Upper |
| `Knat_minus7_6` | `"[20519379388.1263062243678969989681725018000120809824206229413687820751469767 +/- 3.20e-65]"` | Upper |
| `Kr_root_upper` | `{"ball":"[60.59473758383870414082750587300440600000000000000000 +/- 3e-55]"}` | Upper |
| `eta_root_lower` | `{"ball":"[1.25299547095054573079366467377879882466593863889 +/- 3.72e-48]"}` | Positive lower |
| `ng_waist_upper` | `{"ball":"[1.000093202649551554352039595968117361688278413511756016906361800 +/- 1.41e-64]"}` | Upper |
| `saved_absolute_short_exp_upper` | `{"ball":"[1.00176978631221295496404937528780548717650939825876936040065893371974849 +/- 2.27e-73]"}` | Upper |
| `saved_reverse_radial_upper` | `{"ball":"[185.0751745325951770396074382417460543669648347869247 +/- 3.96e-50]"}` | Upper |

The complete original scope path-values are preserved in Appendix A. These are explicitly selected, complete path-values from four original scopes, not a claim to have copied four entire scientific files. The new science retains their original role and path labels.

The three original collections were independently compared to the four complete saved sources without scientific arithmetic:

| Complete collection | Canonical bytes including final LF | SHA256 |
|---|---:|---|
| Sixteen original scalar records | 1751 | `57731cdef27a9fa90024339d9d4d4e58daef926f532f5d2290a1956516073b10` |
| Four original scope collections | 8523 | `3f12846bb79fc7cefd00649fecf6ac4ca3a7babe7fa584ff7cace9cf90f58c73` |
| Complete accepted-original provenance | 5148 | `269bbedf447b770ffc9cd27085fc932a26cca3c80df62ff37595d54ab24983fc` |

The TF/KL/WX/RNE complete scientific schemas have respectively 38/38/55/35 fields and 14/16/20/16 passed gates. WX remains an embedded `actual_scientific_receipt` in its original execution file. Its complete canonical science is 31088 bytes with SHA256 `536e5f33441570eec1b0b35091400f815c5333c4cfd3f0f731099f5dd48cb015`; the original four-key runtime, source, manifest and `consumers/process.json` identity are checked as originally recorded. The other three inputs are standalone complete scientific files. Appendix B retains the full accepted-original provenance, including distinct event and checkout commits where present.

## NIFA6. Exact source, inputs and output identities

All eight input files are complete current small texts. Their total is 297952 bytes. The two Python files are parsed in full before the unique scientific child. There is no historical input, binary restore, artifact download, old source import, new array or Release.

| Current role | Immutable Git blob | Bytes | Complete SHA256 |
|---|---|---:|---|
| source | [`09e19b9612d1cbfde84dbf95e2ff4e5a5160fbd4`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/09e19b9612d1cbfde84dbf95e2ff4e5a5160fbd4) | 57861 | `d75ad8a2c76ad1f450cb5a96977c3ec5b8fb6fda69a1185590ba68eeec5e85a2` |
| worker | [`e7a841117c4c082e0e869a193963866be12b6c06`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/e7a841117c4c082e0e869a193963866be12b6c06) | 65113 | `5b5a9b7571372eae4ba2a0231902db6f30fcbdd7df16ed9272f2e82b32eb2b51` |
| rules | [`5c5d020913d717bb5bc8ce891297e00eaa8944f7`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/5c5d020913d717bb5bc8ce891297e00eaa8944f7) | 2461 | `65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1` |
| contract | [`d606faa1ffd30c34d3487985a57dbc62a18890bc`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/d606faa1ffd30c34d3487985a57dbc62a18890bc) | 32942 | `8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640` |
| tf_science | [`3766aea85aba59230be3813b4b7634d318316e49`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/3766aea85aba59230be3813b4b7634d318316e49) | 18206 | `a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720` |
| kl_science | [`d24a1ecdd9b4397184a3ab932a503e8eb79d0c24`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/d24a1ecdd9b4397184a3ab932a503e8eb79d0c24) | 20537 | `1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee` |
| wx_execution | [`5121a599896025d90e2861450756a256aaba659d`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/5121a599896025d90e2861450756a256aaba659d) | 43753 | `e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12` |
| rne_science | [`6f4ddebe683c0a22cb726d8ff7f8e7269146e46d`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/6f4ddebe683c0a22cb726d8ff7f8e7269146e46d) | 57079 | `579b09aa7164ec4800187436248fdafca85691066afa419ed6fa8b6ab1de3086` |

The source is [fourfold_codazzi_frozen_common_input_uniform_inverse_constants.py](../scripts/fourfold_codazzi_frozen_common_input_uniform_inverse_constants.py); the exact worker and all paths are fixed by the [manifest](../notes/2026-11-16-R133-frozen-common-input-uniform-inverse-constants-CI-inputs.json). The manifest is separately pinned by the workflow and is not self-pinned as its own input. The workflow is not reverse-pinned from the manifest. The independent static budget is a metadata reference, not a ninth input.

| Record | Immutable Git blob | Bytes | Complete SHA256 |
|---|---|---:|---|
| Complete scientific conclusion | [`7142de95e64d5b3c6df7af705c8b0bf08a5c5c5e`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/7142de95e64d5b3c6df7af705c8b0bf08a5c5c5e) | 29829 | `43294b0cd0fdcffea58a805ecfb3cf06d60136d5ffbb3c8269b3040ce5ea9883` |
| Execution receipt | [`42548fb36cc0d3947d00b76d13878d695a237b24`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/42548fb36cc0d3947d00b76d13878d695a237b24) | 11713 | `8a897235272b4eae3673ff61c9d571d74d20d718372b99a9f2107b245a3c88cd` |
| Final actual report | [`8a6e7daa484088c40fef8ac9a85f1b7508022e9a`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/8a6e7daa484088c40fef8ac9a85f1b7508022e9a) | 5752 | `bbe0fd2bbea1e8d360d53130d2b1eac2ff490044186fcbf24ed046c2faf62a79` |
| Frozen manifest | [`f6f282cb8acccbeb1b93a87515a1877b9eada204`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/f6f282cb8acccbeb1b93a87515a1877b9eada204) | 25201 | `138fe8d9d0298126bd4c81691975496db94c2c1d69df31970af4d5b9917fd819` |
| Workflow | [`396cfc886d1d22afc85b53baac4e671703a438ec`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/396cfc886d1d22afc85b53baac4e671703a438ec) | 4958 | `63a9e46806acba961481fda27b215a0cec368b49aed4602c1461853939d30969` |
| Independent static publication model | [`922948594e751a218fa07e991a55d2a1581410fb`](https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/922948594e751a218fa07e991a55d2a1581410fb) | 13767 | `303d90c3764ae89d9ceade615dfae9ab5f69da73a356d957930573625634cf32` |

Every actual source/manifest/runtime/parameter/input identity agrees with the frozen package. The source uses 320-bit directed Arb arithmetic in Python 3.12.14 with python-flint 0.9.0. The original WX runtime retains its distinct original four-key schema; it is not rewritten as the new two-key runtime.

The complete current-input receipt list is independently reconstructed from the eight manifest entries in their actual order: 2226 canonical bytes, SHA256 `168ee7e5e720447e762caaac1291d9366c4e93f43a2ff90cac7bee6b2255cdf5`. The complete two-file Python AST inventory is independently reconstructed in that same source/worker order and has SHA256 `602a50fccdde25e2253694bdfd856f5e3b1c315324880900d97a5697a63c4d05`. These are the exact two digests stored in the actual execution.

The three complete new graphs have the following canonical identities. All 23 scalar strings are present and distinct; the longest is 92 bytes.

| Complete graph | Scalar slots | Canonical bytes | SHA256 |
|---|---:|---:|---|
| `complete_forward_leading_conclusion` | 10 | 1802 | `05f5b742965700940158a8d8b26f0d78d6fcb4849a9affb5a9a6178d9abe0a77` |
| `complete_coordinate_conclusion` | 8 | 1549 | `cc017d50e4ed81cad2519a50b75a6e7b54995f71d24013fac602a111256b11b5` |
| `complete_frozen_stable_inverse_conclusion` | 5 | 1322 | `fda373f25260c956880bc5884d52e5ac5be672b2ac8d81efbc2a78be69a4de5d` |

## NIFA7. All actual gates and progress

The actual gate list is preserved verbatim, in its original order.

| Gate | Actual result | Exact name |
|---:|---|---|
| 1 | true | actual public Actions runtime and the frozen new source are exact |
| 2 | true | eight current small texts and the complete new parameter closure are frozen |
| 3 | true | all five mathematical primaries retain their original bytes SHA and Git identity |
| 4 | true | the TF complete fourteen gate success retains its full family and same two window inverse |
| 5 | true | the KL complete sixteen gate success retains the full correlated mean and absolute short rate |
| 6 | true | the WX complete twenty gate success retains its original embedded schema runtime and selected scope |
| 7 | true | the RNE complete sixteen gate success retains both original natural negative inverse records |
| 8 | true | the common family and frozen reflected phase domain retain every original endpoint and mean |
| 9 | true | sixteen complete old scalar records and all required original scope fields are preserved |
| 10 | true | the new complete forward leading bound uses the true reverse factor and a positive denominator |
| 11 | true | both coordinate windows retain complete forward and inverse products in their exact order |
| 12 | true | both frozen stable inverse windows retain the natural weights and the exact rational gamma |
| 13 | true | all original inputs and records remain unchanged with zero old scientific evaluation |
| 14 | true | all twenty three new scalar records and the complete operator identities are retained |
| 15 | true | actual progress and every declared new scalar count match the complete target |
| 16 | true | the complete thirty two field schema preserves the frozen reflected domain and every independent port |

All fifteen actual progress entries are also retained. These are completed-operation counters, not a declaration that planned work ran.

| Exact progress key | Actual value |
|---|---:|
| `accepted_original_successes` | 4 |
| `historical_inputs_restored` | 0 |
| `new_common_input_window_bounds_completed` | 4 |
| `new_elementary_factor_records_completed` | 16 |
| `new_fixed_square_roots_completed` | 1 |
| `new_forward_leading_scalar_completed` | 1 |
| `new_frozen_stable_inverse_windows_completed` | 2 |
| `new_pi_constants_completed` | 1 |
| `new_positive_sixth_roots_completed` | 1 |
| `old_R97_RNE_graphs_or_comparisons_recomputed` | 0 |
| `old_exponentials_reevaluated` | 0 |
| `old_logarithms_reevaluated` | 0 |
| `old_scientific_targets_recomputed` | 0 |
| `saved_original_scalar_records` | 16 |
| `saved_original_scope_collections` | 4 |

The scientific document reports `complete=true`, `proved=true`, `actual_returncode=0`, `stage="complete"`, and `failure=null`. Its actual mathematical wall time is 0.015665515999998547 seconds; the wrapper's complete child wall time is 0.37639018899999854 seconds. The wrapper records exactly one new scientific process. All old source, integral, flow, mean, root, Airy, coordinate-leading, exponential/logarithm, numerical-enclosure and R97/RNE graph or comparison counters remain zero.

[Job 133064556560](https://github.com/Rogerhu12/math-research-public/actions/runs/43795909913/job/133064556560) ran from 03:04:22Z to 03:05:03Z on 2026-11-16. All twelve recorded steps succeeded:

| Step number | Complete original step name | Conclusion |
|---:|---|---|
| 1 | Set up job | success |
| 2 | Initialize containers | success |
| 3 | Install terminal Git | success |
| 4 | Partially check out only scripts parameters and reviewed READMEs | success |
| 5 | Verify the separately pinned worker | success |
| 6 | Hydrate only small source proof and provenance texts | success |
| 7 | Parse the entire frozen Python closure before any new arithmetic | success |
| 8 | Install the pinned directed arithmetic runtime | success |
| 9 | Read four successful small receipts and evaluate only new frozen-coordinate constants | success |
| 17 | Post Partially check out only scripts parameters and reviewed READMEs | success |
| 18 | Stop containers | success |
| 19 | Complete job | success |

The independently read complete jobs API response is 3228 bytes with SHA256 `b18b6eb269c65aca48649d94787e94734bbd00787f22c7c335034f2c9bd6e015`. The complete run API response is 13335 bytes with SHA256 `3fab705d35400fd6da2395fb36845f96d290111fb3f7c41c0e668f1ad06f03b8`. It records one push run, attempt 1, head `9948aec967519e5b39535443f55adfcfb7e9d8f3`, created 03:04:20Z and completed successfully. No manual dispatch, restart, repetition of completed mathematics or second new child occurred.

## NIFA8. Full save-before-publication evidence

The scientific JSON was atomically saved and printed before size checks and publication. The complete child stdout is independently reconstructed as the exact two frozen markers surrounding the original scientific bytes: 29955 bytes, SHA256 `801b3fabc44817a9d860c040d08ad3fe9388ed3a5a27a9522364bece4a0d0f37`, exactly matching the saved child-log record.

Both complete prepublication payloads are independently reconstructed at the lexical JSON level, retaining the original numerical token spellings. This is a byte comparison, not a recomputation of scientific numbers.

| Complete prepublication object | Bytes | SHA256 |
|---|---:|---|
| Complete science plus initial report | 35933 | `e17b7933a27d6c181a5e7989b5644dd208fa63727ad339ebe1f5971fc773f6eb` |
| Complete execution state and its marker | 9154 | `df921f849e71a288b1a69c047f0ac8a209bc2f60c817c8121a010fe89ce04d7d` |
| Initial complete report inside the first payload | 5644 | `959fc7a5ced25ddb7f8487ddf7160aa66ff6bead70fb13401e29a6315d1b4718` |

The first report contains the first genuine pull check. The final report additionally contains the final publication pull check, giving 5752 bytes. The full execution retains both checks at 03:04:50.781149+00:00 and 03:04:55.477901+00:00, each with empty README diff. The prepublication execution reconstruction removes only the seven metadata fields added later by the worker's actual publication path and retains the first original README check; its byte count and digest match the original saved prepublication record exactly.

The actual science, report, execution and complete science/report prepublication payload are respectively 29829, 5752, 11713 and 35933 bytes. They fit the frozen 75000/8000/59000/90000-byte hard limits and the 35000/50000-byte success targets for science/prepublication. The worker verifies the same 150000-byte reserve before new mathematics. Its metadata-only capacity check records 199747711 topic bytes before publication and a projected 199795005 bytes after the three exact owned output files. No large body was read for that capacity check.

The reviewed rule record remains `65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1`; the separately read review commit is `2f72b274f8647dbf6ce236ff2185cbe22153f8e1`. Both READMEs remain unchanged. The complete original input/science and all completed new factors are retained before publication; no new artifact, Release or numerical array is uploaded.

## NIFA9. Scope of the no-duplicate-target check

Before deployment, the held WE/UT/SW/NW/NPK sources and the complete WE actual object were checked specifically for the independent products $A_s$ in (NIFA.4). WE saves
$A_{\rm port}=B_{H,0}K_{W,0}K_\Lambda^-$ and then
$A_{\rm state}=A_{\rm port}K_{F,-4/3}^-K_{\mathcal S^{-1},-4/3}$.
UT and SW inherit that complete state product. None of those checked objects saves the separate coordinate product $K_\Lambda^-K_{F,s}^-K_{\mathcal S^{-1},s}$. NW and NPK concern the different full-circle operator $N=1+M_wI$.

This is a bounded, source-specific check, not a claim that a repository-wide search proved absence. No coordinate bound is obtained by dividing $A_{\rm state}$ or any other saved norm upper bound. The complete actual manifest records the checked identities. The original successful computations remain frozen.

## Appendix A. Complete required original scope path-values

The following exact path-value collections are copied from the actual scientific conclusion. Their canonical identity is the 8523-byte scope object in NIFA5. They retain all selected-map, full-family, root-domain, mean and rough-space qualifications used by the new products.

```json
{
  "kl_science": {
    "complete_new_leading_scalar_conclusion.original_order": "E_star Lambda_sigma_inverse T_F_inverse S_inverse",
    "complete_new_leading_scalar_conclusion.physical_means_and_transported_finite_blocks_independent": true,
    "complete_new_leading_scalar_conclusion.root_mean_residual_retained_in_exact_log_derivative": true,
    "complete_new_leading_scalar_conclusion.same_input_multiplier_in_every_window": true,
    "complete_new_leading_scalar_conclusion.second_Bi_or_other_genuine_root_column_covered": false,
    "complete_new_root_short_conclusion.complete_mean_state_used": true,
    "complete_new_root_short_conclusion.old_WL_products_used_only_at_delta_zero_off_the_metric_support": true,
    "complete_new_root_short_conclusion.original_cut_eta_upper_not_reused_at_root": true,
    "complete_new_root_short_conclusion.root_point_not_replaced_by_bracket_midpoint": true,
    "copied_complete_input_objects.FA_complete_root_mean_value_q_bounds.exact_root_distance": [
      "1/262144",
      "1220703413/320000000000000"
    ],
    "copied_complete_input_objects.FA_complete_root_mean_value_q_bounds.whole_segment_in_one_original_germ": true,
    "copied_complete_input_objects.WX_complete_ungauged_leading_flow_conclusion.exact_evolution": "V0(b,a) = exp(integral_a^b ell0 dr) U_(chi_b_to_a)",
    "copied_complete_input_objects.WX_complete_ungauged_leading_flow_conclusion.exact_scalar_radial_rate": "ell0 = -2 beta mean(u^2+K*v^2)",
    "copied_complete_input_objects.WX_complete_ungauged_leading_flow_conclusion.reverse_orientation": "b<=a",
    "copied_complete_input_objects.WX_complete_ungauged_leading_flow_conclusion.true_radial_interval": [
      "0",
      "76285779072683/320000000000000"
    ],
    "parameters.all_four_moduli_equal_for_this_reference_column": true,
    "parameters.continuous_centre_definition_sha256": "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "parameters.continuous_response_definition_sha256": "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "parameters.exact_real_delta_radius": "1/100000000",
    "parameters.exact_root_interval": [
      "1191984371497/5000000000000",
      "2383968743003/10000000000000"
    ],
    "parameters.exact_short_interval_upper_length": "1220703413/320000000000000",
    "parameters.exact_strict_cut": "76285779072683/320000000000000",
    "parameters.fixed_intrinsic_parameter": "eta_0",
    "parameters.independent_physical_means": 2,
    "parameters.reference_column": "same terminal Ai free P8 first column",
    "parameters.root_mean_residual_set_to_zero": false
  },
  "rne_science": {
    "complete_natural_inverse_conclusion.exact_order": "(Id+D_g^-1 E)^-1 D_g^-1 M^-1",
    "complete_natural_inverse_conclusion.independent_physical_means_retained": true,
    "complete_natural_inverse_conclusion.selected_common_input_inverse_left_factor_remains_separate": true,
    "complete_natural_inverse_conclusion.true_Riccati_operator_norm_continuity_claimed": false,
    "complete_natural_inverse_conclusion.two_natural_negative_windows_certified": true,
    "complete_natural_inverse_conclusion.uniform_real_delta_family_only": true,
    "parameters.exact_intrinsic_parameter": "-7789843107295549/4611686018427387904",
    "parameters.exact_real_delta_radius": "1/100000000",
    "parameters.exact_root_interval": [
      "1191984371497/5000000000000",
      "2383968743003/10000000000000"
    ],
    "parameters.fixed_intrinsic_parameter": "eta_0",
    "parameters.input_cutoff_abs_j": 97,
    "parameters.natural_negative_windows": [
      "-7/6",
      "-5/2"
    ],
    "parameters.normalized_angular_measure": true,
    "parameters.physical_frequency": "n=4|j|",
    "parameters.physical_period": "pi/2",
    "parameters.physical_root_piece": 2549,
    "retained_scope": {
      "J_negative_windows_use_same_direction_finite_bootstrap": true,
      "L_and_J_not_assigned_new_finite_bandwidth": true,
      "Riccati_operator_norm_continuity_claimed": false,
      "complete_incoming_inverse_claimed": false,
      "complete_positive_R0_mean_rank_retained": true,
      "finite_Schur_inverse_claimed": false,
      "full_low_intermediate_primitive_one_quarter_retained": true,
      "independent_physical_mean_coordinates": 2,
      "input_frequency_diagonals_kept_in_original_order": true,
      "nonlinear_background_or_final_surface_claimed": false,
      "old_R97_graphs_and_comparison_not_recomputed": true,
      "old_scalar_upper_bounds_used_only_with_exact_positive_kernel_qualification": true,
      "original_J1_is_left_angular_derivative": true,
      "original_low_complement_radial_head_sources_and_all_other_finite_ports_retained": true,
      "original_reflection_and_two_carrier_signs_retained": true,
      "physical_bulk_Poisson_extension_claimed": false,
      "physical_fourier_factor_four_and_normalized_measure_retained": true,
      "same_distributional_inverse_in_both_natural_windows": true,
      "same_real_delta_family_and_fixed_intrinsic_eta0": true,
      "saved_positive_strict_margin_read_only": true,
      "scientific_target": "explicit uniform natural negative-window inverse constants for the actual original root97 stable operator",
      "true_Riccati_frame_used_only_through_uniform_bounds_and_strong_realization": true,
      "uniform_selected_chart_family_claimed": false
    }
  },
  "tf_science": {
    "complete_new_root_coefficient_conclusion.angular_degree": 192,
    "complete_new_root_coefficient_conclusion.cut_only_row790_eta_not_used": true,
    "complete_new_root_coefficient_conclusion.original_full_complex_eta_domain_includes_root": true,
    "complete_new_root_coefficient_conclusion.root_mean_and_both_Fourier_signs_retained": true,
    "complete_new_root_normalizer_conclusion.actual_J_F": 1024,
    "complete_new_root_normalizer_conclusion.below_J_F_and_independent_mean_ports_are_identity": true,
    "complete_new_root_normalizer_conclusion.right_transformed_finite_rows_keep_actual_dual_norms": true,
    "complete_new_root_normalizer_conclusion.root_cutoff_is_not_moving_Js_or_principal_angle_cutoff": true,
    "complete_new_root_normalizer_conclusion.same_inverse_on_both_windows": true,
    "parameters.continuous_centre_definition_sha256": "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "parameters.continuous_response_definition_sha256": "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "parameters.eta_lower_scope": "original full complex coefficient domain c[em], including the root",
    "parameters.exact_real_delta_radius": "1/100000000",
    "parameters.exact_root_interval": [
      "1191984371497/5000000000000",
      "2383968743003/10000000000000"
    ],
    "parameters.exact_strict_cut": "76285779072683/320000000000000",
    "parameters.fixed_intrinsic_parameter": "eta_0",
    "parameters.independent_physical_means": 2,
    "parameters.original_input_order": "L_sigma T_F_inverse; no factor commutation",
    "parameters.physical_frequency": "n=4|j|"
  },
  "wx_execution": {
    "complete_selected_common_input_conclusion.exact_order": "S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)",
    "complete_selected_common_input_conclusion.independent_mean_block_retained": true,
    "complete_selected_common_input_conclusion.inverse_order": "S_inverse = U_X_minus_inverse U_H",
    "complete_selected_common_input_conclusion.no_projection_commuted_through_coordinate": true,
    "complete_selected_common_input_conclusion.only_same_selected_actual_conjugacy": true,
    "mathematical_parameters.complete_mean_coordinates": 2,
    "mathematical_parameters.exact_real_delta_radius": "1/100000000",
    "mathematical_parameters.exact_root_interval": [
      "1191984371497/5000000000000",
      "2383968743003/10000000000000"
    ],
    "mathematical_parameters.exact_strict_cut": "76285779072683/320000000000000",
    "mathematical_parameters.fixed_intrinsic_parameter": "eta_0",
    "mathematical_parameters.selected_common_input_order": "S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)",
    "mathematical_parameters.selected_conjugacy_derivative_lower": "31/32",
    "mathematical_parameters.selected_conjugacy_derivative_upper": "33/32",
    "mathematical_parameters.selected_conjugacy_parameter_absolute_upper": "0.00000000009368259853002",
    "mathematical_parameters.selected_conjugacy_second_derivative_upper": "4",
    "scope": {
      "actual_H_and_common_input_only_at_original_selected_delta": true,
      "every_shorter_directed_subinterval_in_true_dr": true,
      "exact_root_labels_and_ordered_common_input_retained": true,
      "full_independent_mean_identity_blocks_retained": true,
      "full_primitive_two_rank_and_mean_adjustment_terms_retained": true,
      "full_ungauged_leading_flow_not_the_complete_Cauchy_flow": true,
      "no_finite_Schur_inverse_or_whole_return_R0_claimed": true,
      "no_first_symbol_coefficient_or_complete_incoming_outgoing_error_paid": true,
      "no_interior_ng_or_source_integral_paid": true,
      "no_waist_normalizer_inverse_paid": true,
      "original_projection_not_relabelled_as_phase_Fourier": true,
      "physical_ng_endpoint_ratios_remain_separate": true,
      "same_P22_cut_and_fixed_eta0_reference": true,
      "same_inverse_on_L2_and_Hminus4_3": true,
      "scalar_diagonal_recovery_uses_specific_positive_algorithm": true,
      "waist_and_shorter_flow_bounds_on_whole_original_real_family": true
    }
  }
}
```

## Appendix B. Complete accepted-original provenance

This exact object retains all four original successful receipts and the two original-copy hashes. Its compact sorted-key JSON plus final LF has 5148 bytes and SHA256 `269bbedf447b770ffc9cd27085fc932a26cca3c80df62ff37595d54ab24983fc`.

```json
{
  "four_original_science_objects_not_recomputed": true,
  "original_scalar_records_sha256": "57731cdef27a9fa90024339d9d4d4e58daef926f532f5d2290a1956516073b10",
  "original_scope_fields_sha256": "3f12846bb79fc7cefd00649fecf6ac4ca3a7babe7fa584ff7cace9cf90f58c73",
  "original_scope_fragments_are_exact_path_values_not_full_objects": true,
  "original_successes": {
    "kl_science": {
      "actual_returncode": 0,
      "actual_scientific_checkout_commit": "4af263bb810f74ab57be1088bbcb9560b06e2c7f",
      "arithmetic_bits": 320,
      "complete": true,
      "complete_original_gates_sha256": "45a617db8d31e61d46c0f0a8f2d4f8dd9bb614feb3d3d38704147ff163182a1f",
      "file_bytes": 20537,
      "file_git_blob": "d24a1ecdd9b4397184a3ab932a503e8eb79d0c24",
      "file_path": "topics/visible-flex-exact-nearby/notes/correlated_terminal_Ai_leading_scalar_ci/run-43766439345-1/actual-scientific-conclusion.json",
      "file_sha256": "1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee",
      "gate_count": 16,
      "input_manifest_sha256": "810a13c2e1e0d3fb85f00129ca3e826e00e264d78269e25b78408bc1f67b99c7",
      "kind": "actual_correlated_terminal_Ai_leading_scalar_v1",
      "passed_gate_count": 16,
      "proved": true,
      "run_attempt": "1",
      "run_id": "43766439345",
      "runtime": {
        "Python": "3.12.14",
        "python_flint": "0.9.0"
      },
      "science_canonical_bytes": 20537,
      "science_canonical_sha256": "1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee",
      "science_location": "complete standalone scientific object",
      "source_sha256": "1f9dd122c7de8a990f5c60d0f405b2e3b3e51420b807ded9be58e8715fd480d6",
      "workflow_event_commit": "8dcbbfefe6fa27bbbeb2f61da76e05083fbfb988"
    },
    "rne_science": {
      "actual_returncode": 0,
      "actual_scientific_checkout_commit": "58e9eaf49412f25a62af80920a33f21ec0c11491",
      "arithmetic_bits": 320,
      "complete": true,
      "complete_original_gates_sha256": "00ba13dcff64d117e0c63ba3607617c72eeb7db44eb38d1d75f581fdd5515028",
      "file_bytes": 57079,
      "file_git_blob": "6f4ddebe683c0a22cb726d8ff7f8e7269146e46d",
      "file_path": "topics/visible-flex-exact-nearby/notes/root_natural_negative_window_explicit_constants_ci/run-43792291190-1/actual-scientific-conclusion.json",
      "file_sha256": "579b09aa7164ec4800187436248fdafca85691066afa419ed6fa8b6ab1de3086",
      "gate_count": 16,
      "input_manifest_sha256": "e311c5119accc5ba90585e49a3bb24bbe672eb601977ebc29720e24979a9128b",
      "kind": "complete_root_natural_negative_window_explicit_constants_v1",
      "passed_gate_count": 16,
      "proved": true,
      "run_attempt": "1",
      "run_id": "43792291190",
      "runtime": {
        "Python": "3.12.14",
        "python_flint": "0.9.0"
      },
      "science_canonical_bytes": 57079,
      "science_canonical_sha256": "579b09aa7164ec4800187436248fdafca85691066afa419ed6fa8b6ab1de3086",
      "science_location": "complete standalone scientific object",
      "source_sha256": "fc7b4ceee05768c1aa5267b01c04dd721e286225d873d48ded954c9d4789f3d5",
      "workflow_event_commit": "58e9eaf49412f25a62af80920a33f21ec0c11491"
    },
    "tf_science": {
      "actual_returncode": 0,
      "actual_scientific_checkout_commit": "8839cad6bdb5bdd7b5f09959cbc3a20c55c680c6",
      "arithmetic_bits": 320,
      "complete": true,
      "complete_original_gates_sha256": "d8cf1f82f556ed32ea44309e407f8fe264e769275311ca7787d5913291466cb7",
      "file_bytes": 18206,
      "file_git_blob": "3766aea85aba59230be3813b4b7634d318316e49",
      "file_path": "topics/visible-flex-exact-nearby/notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-scientific-conclusion.json",
      "file_sha256": "a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720",
      "gate_count": 14,
      "input_manifest_sha256": "027a4462a2cc0424abf00bb03456b63b0811700e98e5ddd28ba1d4d793aefacf",
      "kind": "actual_common_root_normalizer_two_window_v1",
      "passed_gate_count": 14,
      "proved": true,
      "run_attempt": "1",
      "run_id": "43766881076",
      "runtime": {
        "Python": "3.12.14",
        "python_flint": "0.9.0"
      },
      "science_canonical_bytes": 18206,
      "science_canonical_sha256": "a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720",
      "science_location": "complete standalone scientific object",
      "source_sha256": "bf71639da0bc9e41ab86f9530fe02b34399c18e63e9041fa0c3abd0852ccdc4b",
      "workflow_event_commit": "0107666b538ced3a0fbc91f6a7f2cfa894f8ef6f"
    },
    "wx_execution": {
      "actual_returncode": 0,
      "actual_scientific_checkout_commit": "cd14574e6b1bd74973214d57979305e5e3dfe41f",
      "arithmetic_bits": 320,
      "complete": true,
      "complete_original_gates_sha256": "4c8f214fc05eaf3c8c3a9970a41921037356bf0f9021ef1b1ec942c485b90d47",
      "file_bytes": 43753,
      "file_git_blob": "5121a599896025d90e2861450756a256aaba659d",
      "file_path": "topics/visible-flex-exact-nearby/notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json",
      "file_sha256": "e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12",
      "gate_count": 20,
      "input_manifest_sha256": "aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26",
      "kind": "actual_true_waist_coordinates_from_saved_positive_products_v1",
      "passed_gate_count": 20,
      "proved": true,
      "run_attempt": "1",
      "run_id": "43763424840",
      "runtime": {
        "numpy": "2.3.5",
        "python": "3.12.14",
        "python_flint": "0.9.0",
        "scipy": "1.17.0"
      },
      "science_canonical_bytes": 31088,
      "science_canonical_sha256": "536e5f33441570eec1b0b35091400f815c5333c4cfd3f0f731099f5dd48cb015",
      "science_location": "embedded actual_scientific_receipt",
      "source_sha256": "63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424",
      "workflow_event_commit": "cd14574e6b1bd74973214d57979305e5e3dfe41f"
    }
  }
}
```

## Appendix C. Exact new operator identity record

The original scientific identity record is retained verbatim in content, including the corrected inverse-image domain and every unproved extension flag.

```json
{
  "Dplus": "exp(-i*pi/4) Pi_plus + exp(i*pi/4) Pi_minus",
  "Lambda_plus_on_high_nonmean": "Lambda_plus_delta = a_delta D_plus with a_delta > 0",
  "TF_reflection_identity": "R M_Fstar R = -M_Fstar and R I R = -I; R commutes with P1024",
  "TF_same_inverse_preserves_original_natural_reflection": true,
  "ambient_high_projector": "P_fr = S_star P97 S_star^-1",
  "exact_Ni_restriction": "Ni_delta_fr(S_star D_plus f) = a_delta^-1 T_F_delta^-1 f",
  "fixed_input_identity_across_delta": "identity on X_s_fr",
  "frozen_input_space": "X_s_fr = S_star D_plus H_nat^s = (Ni_delta_star)^-1 H_nat^s",
  "frozen_norm": "inherited physical H^s norm",
  "full_circle_principal_Cayley_restriction_needs_separate_domain_range": true,
  "full_circle_scalar_mean_not_scaled_by_a_delta": true,
  "full_signed_carrier_space": "H_car^s = P97 H^s",
  "independent_rest_extension": "diag(Ni_delta_fr, Id_rest); rest may include infinite radial ports",
  "natural_and_ambient_projectors_not_identified": true,
  "natural_projector": "Q_fr = S_star D_plus Q_nat D_plus^-1 S_star^-1",
  "natural_space": "H_nat^s is the original SE reflected high space",
  "new_full_incoming_or_finite_Schur_inverse_proved": false,
  "old_SE8_literal_domain_corrected": true,
  "physical_mean_coordinates": 2,
  "selected_KAM_conjugacy_only_at_original_delta_star": true
}
```
