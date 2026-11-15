# R133 supplement: actual complete principal inverse logarithmic certificates

2026-11-15, visible-exact / phase_inverse.

**Proved from the actual public execution.** The unique natural push run [43770122351/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43770122351) completed with scientific child exit status $0$, twenty passed gates, and all sixty scientific fields retained. It computed the new PG first-derivative products, complete minima, two logarithmic inverse certificates and two optional strict tests. The successful CG, TF and WX calculations were read without repetition.

The complete real principal factors are
$$
 T_{c_i}=1+M_{c_i}I,\qquad T_{c_o}=1+M_{c_o}I.
 \tag{PGA.1}
$$
For the same selected true common input, the actual result certifies
$$
 \|T_{c_i}^{-1}\|_{L^2\to L^2},\
 \|T_{c_o}^{-1}\|_{L^2\to L^2}\le e^{L_0},
 \qquad
 \|T_{c_i}^{-1}\|_{H^{-4/3}\to H^{-4/3}},\
 \|T_{c_o}^{-1}\|_{H^{-4/3}\to H^{-4/3}}\le e^{L_-}.
 \tag{PGA.2}
$$
The exact outward records for $L_0,L_-$ appear below. They are logarithms of certified upper bounds, not inverse norms. No exponential was evaluated.

Both optional Neumann tests returned false, with their signed negative gaps and null optional inverse fields preserved. This does not contradict the complete ODE inverse from MI and PG. No singularity or operator lower bound follows from these unsuccessful sufficient tests.

## 1. Exact public run and input identities

The workflow event is commit a388ad2f738cc010cd04524a0bf2a0a2c2368c65. Its one job, 132983926062, started at 2026-11-15T22:35:18Z and completed successfully at 2026-11-15T22:36:08Z. The checked scientific checkout was c48b18654476bcfa7acff6c90d671357c28dc1d9, reached by the actual pull before the child.

The exact runtime was Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5, and SciPy 1.17.0, with 320 arithmetic bits. There was one scientific child; its reported mathematical time was 0.013763421000000164 seconds and the enclosing child time was 0.3646244199999984 seconds.

The [PG analytic contract](R133-supplement-complete-principal-inverse-from-first-derivative-budgets.md) and the four deployed files are immutable inputs to this conclusion.

| Object | Git blob | Bytes | SHA256 |
|---|---|---|---|
| [contract](../results/R133-supplement-complete-principal-inverse-from-first-derivative-budgets.md) | 58cae91cb563b4f11102ca671cda2929b8dc7ecd | 14909 | 0a5e4ad71d0d980a097e6c0f4afa8476780a46b4b3e82e5a583633f8bb66ad1a |
| [science](../scripts/fourfold_codazzi_principal_inverse_first_derivatives.py) | a5e7e2b781a390a67f4a8b7381e5e738e8ff8a97 | 30632 | 08b8d1d9ff222ba7c8cea14bed50c0e9cd320359aa0e5456bc14c2ecfcc5c9c7 |
| [worker](../scripts/fourfold_codazzi_principal_inverse_first_derivatives_public_worker.py) | 2fd0ee21a53fd37ac2b561acdf213e347e8adaa6 | 38538 | 1af8afc75cf4aad17f719af38e99c723af63e91357ddb0fbbbae125693e78882 |
| [manifest](../notes/2026-11-15-R133-principal-inverse-first-derivatives-CI-inputs.json) | c1910315f3d260097bbbed3fab73569507621f01 | 10780 | febb85783c624eed3bab22cd6e0873aad08c3257e4758615668654f82289e51c |
| [flow](../../../.github/workflows/visible-principal-inverse-first-derivatives.yml) | bd77f5b45611bb589803c1b6d0097bc2081ae664 | 4331 | fa7b2436bbb0540917633c78f4a11c4cfb9d0117802887fe635356a05bd5bf47 |

The completed public small files are:

| Object | Git blob | Bytes | SHA256 |
|---|---|---|---|
| [execution](../notes/principal_inverse_first_derivatives_ci/run-43770122351-1/execution.json) | c2f1168fed5efdcfa032afaae46955bed2e27745 | 26173 | 95a0fafb34cbb7fa4fd5c0379324b71a35053af5daa73718f95bda8afdc26d67 |
| [actual result](../notes/principal_inverse_first_derivatives_ci/run-43770122351-1/actual-result.md) | cf792c145ae3cde500570789e7c335de8bb10545 | 4561 | aa6830e04f3c047ecfd14961c7896a0c33660558df8a5f1d679099b295e58881 |

The execution record contains the entire scientific receipt. The source identity is checked separately from the wrapper and manifest. The actual child source uses the final PG contract hash after its display-only correction.

The original successful inputs retained their own runtime schemas:

| Input | Successful run | Old gates | Exact completed object SHA256 |
|---|---|---|---|
| CG | 43768992861/1 | 21 | a68095bb38c38d62a4b1af256c84c96e7f1f7f1c2663d5fdb5ffc814b73e57fc |
| TF | 43766881076/1 | 14 | a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720 |
| WX | 43763424840/1 | 20 | e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12 |

CG and TF retain their original two-key runtime records. WX retains its original four-key runtime record. They were checked separately; no runtime field was invented to make an old success fit a newer schema.

## 2. Same selected reference and full means

The underlying complete real family has $|\delta|\le10^{-8}$ and fixed intrinsic parameter $\eta_0$. Its exact root interval and strict cut are
$$
 r_*\in
 \left[\frac{1191984371497}{5000000000000},
       \frac{2383968743003}{10000000000000}\right],
 \qquad
 r_c=\frac{76285779072683}{320000000000000}.
 \tag{PGA.3}
$$
The true common input is the same selected map
$$
 \mathcal S=U_{\mathcal H^{-1}}U_{X_-}
           =U_{X_-\circ\mathcal H^{-1}},
 \qquad
 \mathcal S^{-1}=U_{X_-^{-1}}U_{\mathcal H}.
 \tag{PGA.4}
$$
Its original selected parameter restriction remains 0.00000000009368259853002. The family bounds on coefficient inputs do not enlarge that conjugacy scope.

The original physical frequency is $n=4|j|$ and the normalized period is $\pi/2$. Both signs, both individual real principal coefficients, the complete scalar means in their inverse equations and two independent physical mean blocks remain. The actual root function $F_*$ keeps its complete mean and degree192. Scalar subtraction of $\langle c_\sigma\rangle$ in PG is not deletion of a physical mean coordinate.

The exact centre and response definition hashes retained by all same-object checks are:

- Centre: 440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47.
- Response: 6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.

## 3. Saved complete scalar inputs

These values are copied verbatim from CG, TF and WX. The third CG derivative entry remains in the saved array for identity; this new calculation uses only its first two entries.

| Saved complete input | Original outward record |
|---|---|
| CG h0 | `[7190870492193.90360909434825858876484500259132235195427566835 +/- 8.32e-49]` |
| CG h1 | `[2797767145453406646.36332143358468420624936230641359462284623 +/- 1.42e-42]` |
| CG h2, retained but not consumed by new mathematics | `[1663540036061490115828017.90982806587273865931743251640821272 +/- 2.34e-36]` |
| TF full root F_A0 | `[184.968226870198793095967741098936895577604521232951166970003267689081637 +/- 4.21e-70]` |
| WX selected density derivative upper M | `[27.69777482587445182392067441913413601982066844949280 +/- 4.77e-53]` |
| WX selected density second derivative upper F | `[11129879.44412865454748279730347245235799146501075376 +/- 2.47e-45]` |

Independent metadata comparison verified these four complete saved objects against their original successes, including the entire three-entry CG array. The exact saved-payload SHA256 is
7fced21b0beccf22ff382ab0d30a935f56867fe4271608a1ce68932cfc3594a5.
The three accepted-success identity objects and the selected common-input scope are likewise retained unchanged.

## 4. New selected first-derivative budgets

PG first pays the full root subtraction by positive budgets, then the true density chain rule:
$$
 t_0=h_0+F_{A0},\qquad t_1=h_1+768F_{A0},\qquad
 A_0=M t_0,\qquad A_1=F t_0+M^2t_1.
 \tag{PGA.5}
$$
These are new complete upper bounds. No difference of unsigned upper bounds is treated as a signed coefficient. No third coordinate derivative or second coefficient derivative is evaluated.

| New quantity | Complete outward record |
|---|---|
| t0 after full root subtraction | `[7190870492378.87183596454705168473258610152821792955879690130 +/- 2.00e-48]` |
| t1 after full root subtraction | `[2797767145453548701.96155774625778190947452628994939822311854 +/- 1.68e-42]` |
| A0, both ci and co on the same selected input | `[199171111699934.940517718423517963631695240757706460038984595 +/- 1.78e-46]` |
| A1, both first angular derivatives | `[2226387394810436209755.27284178536279418639782680197995456068 +/- 3.05e-39]` |

## 5. Complete nonmean and primitive bounds

For each actual coefficient $c$, let $b=c-\langle c\rangle$ and $p=Ib$. The exact complete Fourier estimates in PG give the new budgets
$$
 V_0=\min\{2A_0,A_1/2\},\qquad
 P_0=\min\{\pi V_0/8,A_1/8\},\qquad
 B_{1/3}=\frac{39}{32}A_1,\qquad
 P_{4/3}=\frac{243}{160}A_1 .
 \tag{PGA.6}
$$
Each minimum compares two whole bounds for the same norm. The complete signed spectrum, including arbitrarily high modes, is retained.

| New quantity | Complete outward record |
|---|---|
| V0 candidate 2A0 | `[398342223399869.881035436847035927263390481515412920077969190 +/- 3.55e-46]` |
| V0 candidate A1/2 | `[1113193697405218104877.63642089268139709319891340098997728034 +/- 1.53e-39]` |
| V0 complete minimum | `[398342223399869.881035436847035927263390481515412920077969190 +/- 3.55e-46]` |
| P0 candidate pi V0/8 | `[156428625330956.931171541431393114296540947712708034989257674 +/- 1.40e-46]` |
| P0 candidate A1/8 | `[278298424351304526219.409105223170349273299728350247494320085 +/- 3.81e-40]` |
| P0 complete minimum | `[156428625330956.931171541431393114296540947712708034989257674 +/- 1.40e-46]` |
| B1/3 | `[2713409637425219130639.23877592591090541467235141491306962083 +/- 2.47e-39]` |
| P4/3 | `[3381325855868349993565.82062846151974367059169945550705598904 +/- 2.63e-39]` |
| CI = sqrt17/4 | `[1.03077640640441513745535246399351925628679980634340510859966 +/- 1.61e-60]` |

## 6. Actual complete logarithmic inverse certificates

The new scalar evaluation uses exactly
$$
 L_0=\log(1+V_0)+4P_0,\qquad
 L_-=\log(1+4C_I B_{1/3})+5P_{4/3}.
 \tag{PGA.7}
$$
The complete directed results are:

| Window | Complete logarithmic record |
|---|---|
| L2: L0 | `[625714501323861.343018775261247285693046068477242089880096787 +/- 3.15e-46]` |
| H^(-4/3): Lminus | `[16906629279341749967879.8722419453538981576557572281331116982 +/- 5.48e-39]` |

The full-circle ODE proof supplies one actual inverse on both windows, for every real scalar mean including zero. In the negative-window estimate the shifted primitive first gains one derivative to $H^{-1/3}$; the nonmean multiplier is charged there. There is no division by a possibly vanishing scalar mean and no artificial high compression.

These large upper certificates do not imply that the actual inverse is large. Their content is the complete certified bound (PGA.2). No exponential value or finite numerical inverse norm was produced.

## 7. Optional strict Neumann tests, preserved as failed

The actual tests used $V_0/4$ on $L^2$ and $C_I B_{1/3}$ on the negative window. Their signed gaps are the lower endpoints of one minus these complete perturbation budgets.

| Window | Perturbation upper | Signed gap lower record | Strict gate | Optional inverse |
|---|---|---|---|---|
| L2 | `[99585555849967.4702588592117589818158476203788532300194922974 +/- 1.15e-47]` | `[-99585555849966.4702588592117589818158476203788532300194922974 +/- 1.15e-47]` | false | null |
| H^(-4/3) | `[2796918635168274400734.75711422257364692876643263861573626735 +/- 4.10e-39]` | `[-2796918635168274400733.75711422257364692876643263861573626735 +/- 4.10e-39]` | false | null |

Both original optional records explicitly state that a failed test does not negate the complete ODE inverse and that the full scalar-mean factor is contractive. The twenty scientific gates passed because these optional outcomes were kept with their correct scope; the code did not force them to pass.

No actual strictly signed pointwise lower bound for either coefficient was checked. Neither the real mean nor an unsigned upper budget alone proves such a lower bound.

## 8. Complete public execution and byte audit

All seventeen input files were exact current small texts, with total pinned size 351865 bytes. They were copied and verified before the four complete Python AST checks, which preceded the one scientific child. The only Python files in that closure were PG and the immutable CG, TF and WX sources; the three old sources were identity evidence and were not imported.

The full input receipt list was independently reconstructed in the exact manifest order. Its digest is
f9144933a89b17e2371e77b26db026c3b54456e86dbd6458273da54bfe3cc75d.
The four-file AST inventory was independently reconstructed with digest
66a58453e050d922b8ed359ab313fb4510ffe9dfede40014957ccd00359c933b.
All seventeen original entries match the actual worker record.

The exact scientific JSON and recoverable prepublication payload were independently rebuilt from the published lexical JSON, preserving the original decimal number tokens. Both byte counts and hashes agree with the original worker records:

| Complete small object | Bytes | SHA256 |
|---|---|---|
| Scientific process.json, all 60 fields | 13227 | 17992b28128794369c611cab65aa09ea4ca7430d67c676a0873851130ff3043a |
| Full result plus execution envelope, printed before final pull/Git publication | 19693 | 2e8151614d7559b0845781190bf88d4c79e1cc93f6564d541b50197e7ef6cd4a |
| Temporary scalar native, recorded only by size/hash | 4986 | 0dcebcbc2e3114c233a4179c38a5d4c2743b89347421705a9f94d4c26db79898 |
| Scientific stdout log, empty | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

The temporary native was not fetched or regenerated for this report. Its size and hash above are the actual child record.

The actual README checks occurred at 22:35:56.584722 and 22:35:58.970184 UTC. Each real pull recorded an empty README diff and the same published/checked commit c48b18654476bcfa7acff6c90d671357c28dc1d9. The actual published topic contained 199227652 blob bytes before these two small results, below the capacity limit with the required 120000-byte reserve. The projected result total was 199258386 bytes. The owned local delta was empty; the capacity API read only complete published tree metadata, not blob bodies or an unpublished tree.

The job metadata response was 3291 bytes with SHA256
e165c2e736fdb0f6a05ad3cfc47f3c0f9eb92205f51fd6690c9cf6dc81ae03cb.
Every job step completed successfully. The unique event was a push of the deployed head, not a manual dispatch.

The actual operation counters are:

| Counter | Actual value |
|---|---|
| Original successful small receipts read | 3 |
| Saved coefficient arrays / full root coefficients / selected coordinate derivatives | 1 / 1 / 2 |
| New root-subtracted coefficient budgets / selected derivative bounds | 2 / 2 |
| New nonmean and primitive bounds / universal primitive constants | 4 / 1 |
| New logarithmic certificates / optional tests / optional inverse bounds | 2 / 2 / 0 |
| Direct exponential norm evaluations | 0 |
| Old enclosures, CG/TF/WX targets, profiles, phases, rays, sources or root gauges recomputed | 0 |
| Old scientific imports or calls | 0 |
| Binary or archive inputs restored / new angular or radial integrals evaluated | 0 / 0 |
| Selected coordinate third derivatives evaluated | 0 |

The exact passed gates, in original order, are:

1. public Actions uses the exact pinned runtime and320-bit directed arithmetic.
2. the new manifest exact parameters and complete current-only source closure are frozen.
3. all seventeen exact small texts are checked before any new scalar arithmetic.
4. all primary contracts and three old source-manifest identities are exact read-only evidence.
5. accepted CG run 43768992861/1 retains its exact complete source manifest runtime and gates.
6. accepted TF run 43766881076/1 retains its exact complete source manifest runtime and gates.
7. accepted WX run 43763424840/1 retains its exact complete source manifest runtime and gates.
8. all original complete references share the family cut root and physical frequency.
9. only the complete successful three-entry CG coefficient is consumed without rerunning its integrals.
10. the same complete TF root coefficient retains its degree192 and full mean.
11. the same selected WX density map keeps its first two derivatives and ordered input.
12. all complete saved coefficient and coordinate inputs are finite positive-budget records.
13. both complete selected coefficient bounds use the actual density chain rule after the full root subtraction.
14. the four complete nonmean and primitive bounds keep both Fourier signs and same-norm minima.
15. the two finite logarithmic records certify the same complete inverse on their actual windows.
16. each optional strict test is directed and a failed test keeps the complete logarithmic inverse.
17. all complete original input objects and their immutable bytes are retained unchanged.
18. all mean finite and selected-domain interfaces retain their exact principal-only scope.
19. only the declared new scalar products minima logarithms and strict tests were evaluated.
20. all twenty gates and complete principal log records are preserved.

## 9. Precisely completed and retained conclusions

The completed numerical conclusion consists of the two principal inverse logarithmic certificates in (PGA.7), the full first-derivative and nonmean budgets used to obtain them, and the complete outcomes of both optional strict tests. Both factors and both windows use the same selected reference, exact input order and full scalar-mean equations.

The independent physical means, full density-versus-mean-identity rank differences, actual incoming and outgoing errors, finite/high and high/finite rows, and finite matching block remain distinct. No complete physical incoming inverse, finite Schur inverse, full return remainder, nonlinear core solution or final surface is asserted.

The [adjoint-bootstrap lemma](R133-supplement-complete-principal-inverse-adjoint-bootstrap-from-L2.md) provides a separate analytic candidate that can consume five saved PG records. It has not been numerically evaluated in this run. Any later evaluation must read this complete success unchanged and retain the original $L_-$ certificate alongside the new whole-bound candidate.
