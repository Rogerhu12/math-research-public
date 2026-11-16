# R922 — Certified original shared polynomial trace-dual multiplier

Date: 2026-11-16. Status: **completed at the original auxiliary place by the public repository Actions**. This is the actual shared-matrix leaf of [R922](R922-original-bounded-connection-numerators-and-whole-Hecke-evaluation.md). The seven connection numerators, their target denominator units, the differential transport and the original height calculation are separate leaves.

## 1. Actual result

Retain the original genus-127 curve \(Y\), level \(82\), its \(-3\) descent, the original normal basis \(\beta_0,\ldots,\beta_{271}\), the original differential \(\nu=dz/g\), and
\[
 \epsilon=(0,1^{144},2^{127}).
\]
At the already fixed auxiliary place
\[
 \ell=1000000753,\qquad \zeta=549966761,\qquad s=99932770,
\]
the full polynomial matrices
\[
 G_{ij}(z)=\operatorname{Tr}_{k(Y)/k(z)}(\beta_i\beta_j),
 \qquad R(z)=M_g(z)G(z)^{-1}
 \tag{922C.1}
\]
have been computed. The actual output verifies, entry by entry,
\[
 \deg G_{ij}\leq\epsilon_i+\epsilon_j,\qquad
 \deg R_{ij}\leq3-\epsilon_i-\epsilon_j,\qquad
 R^t=R,\qquad R(z)G(z)=M_g(z).
 \tag{922C.2}
\]
A negative degree bound means the entire polynomial entry is zero. In particular the complete \(127\times127\) block indexed by the weight-two basis elements is zero.

The output contains five coefficient matrices for \(G\) and four for \(R\). The old \(M_g\) has six coefficient matrices, because its entry bound is \(3+\epsilon_j-\epsilon_i\). All eight coefficients of the full product \(RG\), from \(z^0\) through \(z^7\), were checked against those six old matrices followed by two zero matrices. The checks cover every one of the \(272\times272\) entries; they are not a sample of rows or nodes.

The exact characteristic-zero object remains the original expression (922C.1), with the finite-relative-dual proof in R922. The new arrays are its reduction at this place. Expanded characteristic-zero coordinates have not been computed.

## 2. Actual execution and frozen definitions

The completed run is [43913992769](https://github.com/Rogerhu12/math-research-public/actions/runs/43913992769), compute job 133463350249. Its source commit is fec176005094b37d86b143de7e460b4ab60471ea. The workflow and compute job both report success; the actual core receipt has complete=true, exit code zero, null error, and elapsed core time 2.48746259 seconds.

There are 26 complete mathematical stages and one separate incomplete current file. These counts come from the completed output, not a planned schedule. The new mathematical configuration SHA-256 is:

~~~
94a0009b06ff3ca92b2eacafdc2bbf526c1facec2b9ef5d5c3dec4ab9fb576cd
~~~

| Definition | SHA-256 |
|---|---|
| Mathematical core | a03394a509a14bd6f29df404f7f66c2877185c932e206ba32adecfa3192d90db |
| Standard-library wrapper | 6465d4c7e1f2474bd4745a5b2c5b4fa16d4e8ac134897f32f13476465e5e972c |
| Execution method | 5e293257730be33228a01dd8091e8f9e818027cfc30978aed497e4ed56661d25 |
| Actual active request | 0b0993547f9859195a3714fabdaca03b806657a3890a45d6a713e1605a4efc39 |
| Workflow | 65d311ab2f8d6b38bf440e7e2468490f2d2130f06c68eb97990c6f4b206c8fbd |
| Original R922 proof used by the computation | 75e0e04e986203598b556403b4ea8eec3706da838e934ae11810c5abda569731 |

The [execution method](../notes/R922-original-shared-low-weight-trace-dual-method.md), [request](../notes/R922-shared-low-weight-trace-dual-public-request.json), [core](../scripts/R922_original_shared_low_weight_trace_dual.py), and [wrapper](../scripts/R922_public_original_shared_low_weight_trace_dual.py) give the complete reproducible definitions. New mathematical execution occurred only in the authorized public repository Actions.

The rules job 133463123462 performed an actual git pull --rebase to fec176005094b37d86b143de7e460b4ab60471ea at 2026-11-16T17:02:17.820964+00:00. Root and topic README hashes were respectively 6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9 and 35f82f3d96f1e07d1b7c3f0320398fdc0cd68d0c0e55ac17881c9f976299646d, with no changed rules.

## 3. Exact reuse of the original sources

The source receipt binds 30 selected R827 files and six selected POLY files. Their mathematical identities were preserved.

| Original group | Run | Source commit | Original manifest SHA-256 |
|---|---|---|---|
| R827 | 43734420663 | 400edecfeab313d1858cdb72bf18f8452ab9566a | 2609de217bf1da048f7987ae7de09df38ac24fb63e82d45add1e7c6b9cdbea7e |
| POLY | 43842694142 | 0210f90f1ac7d2c89e948cae0cdc5f64f775dc07 | 51dff64343665bf629603f42e43cc21ecc10aaf17912df5cc6f20bb7b8973154 |

R827 ended later with exit 124. Its original selected \(W\), place, \(M_g\), operator-identity and five Krylov stages are complete. The consumer retained the historical incomplete overall receipt and the original stage configuration, including its original schema. It did not relabel the old stages as a new successful producer.

The POLY characteristic polynomial and its degree bounds were already complete. Its original \(273\)-node calculation was not repeated. The selected R827 files came through the previously completed, byte-bound intake carrier; the carrier remained transport rather than a new mathematical source.

In particular the original \(W\), \(M_g\), \(K_a\), \(K_a^{-1}\), characteristic relation and all original source identities were reused. No original matrix inverse was rerun.

## 4. The new whole-fibre arithmetic actually completed

At each of the five old nodes \(a=0,1,2,3,4\), the already completed characteristic polynomial supplied all Newton trace moments from exponent zero through 542. If \(H_a\) is the corresponding power-basis trace Gram matrix, the old Krylov inverse gives
\[
 G(a)=K_a^{-t}H_aK_a^{-1}.
 \tag{922C.3}
\]
These are traces on the complete degree-272 algebra, including all multiplicities. Construction of \(G(a)\) does not assume separability.

The actual four accepted nodes for \(R\) were \(0,1,2,3\). Each passed the full polynomial Bezout identity for \(\chi_a'\) and \(\chi_a\). No factor or nilpotent quotient was discarded, and cyclicity of \(K_a\) was not substituted for separability.

Writing
\[
 \chi_a(T)=T^{272}+c_1T^{271}+\cdots+c_{272},
 \qquad
 q_j(T)=\sum_{r=0}^{271-j}c_rT^{271-j-r},
\]
the power-dual columns are \(q_j/\chi_a'\). Multiplication by the Bezout inverse of \(\chi_a'\) gives the complete matrix \(H_a^{-1}\) without a new dense inverse. Both full inverse products were checked, followed by
\[
 R(a)=M_g(a)K_aH_a^{-1}K_a^t,\qquad R(a)G(a)=M_g(a).
 \tag{922C.4}
\]
The complete symmetry identities were also checked.

Scalar interpolation at the five actual \(G\) nodes and four actual \(R\) nodes then gave the polynomial matrices. Every weighted zero, every full node value, and every coefficient of (922C.2) passed the specified original identities. Thus the original shared low-weight multiplier is now available to the later connection consumer.

## 5. Completed output identities

All hashes below are the actual manifest-bound output identities reported by the completed standard-library output reader.

| Output | Bytes | SHA-256 |
|---|---:|---|
| p41-original-shared-low-weight-trace-dual-multiplier-certificate.json | 11271 | 921c5992dfe0658e8febfb21cb4a435f5bb72eb34baa6af79ada8514e7bebce9 |
| full-outputs-manifest.json | 5655 | 575390c170edd61f71b18de13a3b559edeee9990d492ec75c6d4a35013961080 |
| R922-trace-dual-complete-polynomial-low-weight-R.json.gz | 412278 | e4ecf5602c332a06bb75360913deb8119c3ba3e70a2a788b461a05e8d57a80d3 |
| R922-trace-dual-complete-polynomial-Gram.json.gz | 1462268 | 29f284d716e2a39f4adc28d06b110253be462611b53ce72da10b0b869df20300 |
| R922-trace-dual-complete-original-RG-equals-Mg.json.gz | 4387 | 885c75092420de257f047e3f2036c1cbc684929e94dc5652aa3aa8ccce999c36 |
| R922-trace-dual-exact-original-trace-dual-expression.json.gz | 5946 | beec5e5d966515bde23a3d5294714222402cf4fdd2c161c91c8369ca96792274 |
| R922-original-source-inventory.json | 19436 | cfc085f85070b0264e4daed9873eb23cb4728793ff6f20cb70724e519b7a7f56 |
| R922-retained-original-inputs.tar.gz | 11914872 | 3d34cb7d65af60b1715552de4d93aa5ce1f42b9ea92bb0222f0570b434db4dd2 |

The active one-day platform artifact is 14249830182, named serre-global-R922-shared-low-weight-trace-dual-43913992769-1. The platform reports 17061851 ZIP bytes and SHA-256 62a3420c5feb43be8fe9d9d15f58fe876ed0e49072ff86dc42c231445a0b2059, with expiry 2026-11-17T17:02:43Z. This archive identity is the platform digest; the mathematical member identities above are independently present in the run's output manifest and receipt. No claim is made here to have downloaded and rehashed the entire ZIP outside Actions.

The numeric matrices and retained raw source members stay in the necessary active one-day artifact. This document records the result and reproducible identities, not those raw arrays.

## 6. Interface to the still-open original height calculation

For the original source connections,
\[
 \alpha_D=\frac{1}{d_D}\sum_i y_{D,i}\beta_i^*\,dz,
\]
the now completed \(R\) supplies
\[
 B_D=\frac{\beta(U,V)R(U)y_D(U)}{d_D(U)}.
 \tag{922C.5}
\]
This formula is the original R922 formula, with \(V=K(U)/P_U(U)\). The last eight correspondence columns are the numerator \(K\), not \(V\). The whole target algebra and its nilpotents must still be retained.

No claim is made here that the seven \(y_D,d_D\) have already been computed, that every \(d_D(U)\) is a unit, or that the separate target differential transport has been completed. Those computations continue from their genuine original sources. The original Gal-seven average, norm correction, two endpoint frames, canonical Hecke projection, non-\(p\) contribution, Poincare data and height remain outside this certificate.

This closes the shared polynomial trace-dual leaf. The absolute Serre-uniformity objective remains open.
