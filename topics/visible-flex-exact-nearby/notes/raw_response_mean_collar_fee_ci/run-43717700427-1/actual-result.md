# Actual raw-response mean fee and corrected retained collar cases

Public run: 43717700427/1.
Actual scientific child code: 0.
Complete scalar accounting: True.

Scientific SHA256: 7547ece2825854a18e59c27294b12e8dbdcb13671c8fb0d8fba6af218d86f7f2.
Manifest SHA256: 5157dfea0e7d44c7a6659ffd14505ac2a09248ea12ed7333a53a08b11103f7e9.

The old 91-case computation remains unchanged. Its scalar pass count alone did not include the raw mean fee.
Only the raw mean restriction and five retained complete cases are newly evaluated.
The old target, residual polynomials, scalar mean flow and Green kernels are not rerun.

## Complete raw mean source windows

### retained_complete_case_collar

Exact interval: ['589819/655360', '589829/655360'].
Actual radial measure: 1/65536.
Original closed rows: 2.

| Complete scalar | Directed bound |
|---|---|
| raw_mean_signed_lower | -2.540000010320397905161371454596519470214843750000000000000000000000000e-7 |
| raw_mean_signed_upper | 2.540000010320397905161371454596519470214843750000000000000000000000000e-7 |
| raw_mean_sup | 2.540000010320397905161371454596519470214843750000000000000000000000000e-7 |
| raw_mean_L2 | [7.016279235058380745179556526429862627274743611094503173656796640976404e-10 +/- 1.97e-81] |
| P_scaled_raw_mean_sup | [1.796948584936341134472298572033080897910324811144038446180811967409894e-7 +/- 4.95e-77] |
| P_scaled_raw_mean_L2 | [4.963676981606263903148937555029153463275617790933467638849230110276397e-10 +/- 2.01e-81] |
| complete_scaled_square_integral | [2.463808917772787072231074543327064399500791188498199617234476939822117e-19 +/- 2.96e-90] |

The squared P factor on this independent mean is sqrt(K). Positive angular derivatives are exactly zero.

### whole_available_positive_collar

Exact interval: ['17/20', '19/20'].
Actual radial measure: 1/10.
Original closed rows: 140.

| Complete scalar | Directed bound |
|---|---|
| raw_mean_signed_lower | -8.670000042343417590018361806869506835937500000000000000000000000000000e-6 |
| raw_mean_signed_upper | 8.670000042343417590018361806869506835937500000000000000000000000000000e-6 |
| raw_mean_sup | 8.670000042343417590018361806869506835937500000000000000000000000000000e-6 |
| raw_mean_L2 | [7.525983666997945458278804353927118598030598821187228725907130929209366e-7 +/- 2.35e-77] |
| P_scaled_raw_mean_sup | [5.991704974135495654862870502009791668858605343989706388036952449394303e-6 +/- 4.42e-76] |
| P_scaled_raw_mean_L2 | [5.163870552551439546320770182487529367062570059417988390726524807902824e-7 +/- 2.36e-77] |
| complete_scaled_square_integral | [2.666555908350790957321221575586049485532462274217326588606213545692766e-13 +/- 8.72e-84] |

The squared P factor on this independent mean is sqrt(K). Positive angular derivatives are exactly zero.

## All newly evaluated retained cases

| Raw C0 radius | New mean source | Corrected nonlinear gate | Corrected factorial prefactor | Pass |
|---|---|---|---|---|
| 1/1048576 | [4.963676981606263903148937555029153463275617790933467638849230110276397e-20 +/- 2.02e-91] | [0.06496185982052562539618523266749131605712047446788152934663798589701361 +/- 4.99e-72] | [0.0001803234407565868858237064195305493627194208870553729042102889074402479 +/- 4.65e-75] | True |
| 1/16777216 | [4.963676981606263903148937555029153463275617790933467638849230110276397e-20 +/- 2.02e-91] | [0.004059992335381222471373777514947498929980621455244085120210421036284451 +/- 3.44e-73] | [1.127018310807661351483167856580805950775110866223620867617821153302662e-5 +/- 1.89e-76] | True |
| 1/268435456 | [4.963676981606263903148937555029153463275617790933467638849230110276397e-20 +/- 2.02e-91] | [0.0002537511608541141530187159540308588355958006604320424254809161770250883 +/- 3.28e-74] | [7.043922152249416048760183412398607479255422577988600045286995423656779e-7 +/- 3.15e-77] | True |
| 1/4294967296 | [4.963676981606263903148937555029153463275617790933467638849230110276397e-20 +/- 2.02e-91] | [1.586157784530577767030993626830306403752661103448630157557267254323681e-5 +/- 1.80e-75] | [4.403043172705052732061324129305399684723344616629972484472770053078219e-8 +/- 1.51e-78] | True |
| 1/68719476736 | [4.963676981606263903148937555029153463275617790933467638849230110276397e-20 +/- 2.02e-91] | [9.934808228758148574909662068077406786109252529940135319450463250307386e-7 +/- 3.64e-77] | [2.757820833843800208043889709163809150994937578940687970378690711692691e-9 +/- 1.06e-79] | True |

Newly checked cases: 5.
Newly passing cases: 5.
Conditional high-trace domain exists: True.

The complete per-case source values, unchanged angular bounds, all gates and low diagnostics are in execution.json.
The other ten historically passing cases have not been reauthorized by this restricted computation.

## Actual identity gates

- the new directed precision and scalar parameters are fixed: True.
- the separate new manifest and scientific source are immutable: True.
- the original raw193 row identity and full independent mean are unchanged: True.
- the old positive nonmean budget is identified without calling it the raw full source: True.
- the independent successful old forty-part receipt binds the same complete rows: True.
- the old successful 91-case execution and its qualified conclusion remain exact: True.
- only the five retained complete cases share the stated true narrow collar: True.
- all original forty natural parts and every raw row are unchanged: True.
- the full raw signed mean fields retain the original zero-to-25/8 cover: True.
- the exact canonical row payload agrees with the already successful independent receipt: True.
- both new mean restrictions use exact intersections and full closed-row ranges: True.
- all five retained complete cases receive the mean fee with their original thresholds: True.

## Mathematical scope

- The source is the original physical raw response plus its exact continuity repair; the scalar mean-completed trial is a different object.
- The old nonnegative nonmean budget is used only as a monotone upper bound, with the independent raw mean explicitly restored.
- Ordinary source value and finite factorial sums include the new pure mean fee; ordinary angular derivatives are unchanged.
- Each passing high conclusion requires one real continuous two-sided H1 solution of the full PDE in the stated C0 ball.
- No unknown low H1 cut, core solution, true high inverse or boundary selfmap is asserted.
- Full signed means, genuine radial measures, exact K weights and all old interfaces remain included.
- All restored data and the new row audit are temporary; only genuine small conclusions and exact hashes persist.

Actual failure: null.
New scalar seconds: 2.7895493780000606.
