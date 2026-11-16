# R900 — Certified original K-defined bounded trace representative

Date: 2026-11-16. Status: **the original trace class has a certified K-defined effective degree-272 representative, its complete 418-dimensional Riemann–Roch space, and its unchanged marked principal function**. New arithmetic was performed only in this public repository's Actions. This result does not settle absolute Serre uniformity.

## 1. Successful original source

The [public run 43889194318](https://github.com/Rogerhu12/math-research-public/actions/runs/43889194318), compute job 133375658946, used source commit `1418d76e5a9e5dd0666fecdc224bbb620c1c6b4d`. It completed 65 mathematical stages, with process exit 0 and no scope stop. Core mathematical time was 34.063594246 seconds.

| Source | SHA256 |
|---|---|
| Core | 31d0911137f7521c994abb02c5c06684afe5ad025a126be195a99b0eb687e1af |
| Wrapper | 1ccf84b6d2dd09365c22801283832190d9c24a23285b642621ddd9ded3fe5db4 |
| Mathematical configuration | 045fe8572967fe28af433016735c6391f4537533d3c0d8c24bacf5603465bce0 |
| Complete certificate, 13725 bytes | 5d235ab51eb9fdd8776e66781dc86b09f3a59b406f6731ebd5d77d4744dd7683 |
| Complete output manifest, 12042 bytes / 76 files | 3791c7ee0c24fd9d358cf4c6b532244e96cece3f30ac9708255ea8dfc83ac9e0 |

The ground field is the **original** \(K=\mathbf Q(\zeta)\); the numerical matrices are evaluated at the original auxiliary prime \(\ell=1000000753\), original branch and original choices of \(s,\zeta,B\). The exact objects remain the fixed source-bound unit-solve expressions of [R900's theorem](R900-original-K-defined-bounded-trace-representative-and-marked-principal.md) and [execution method](../notes/R900-original-K-defined-degree272-consumer-method.md), rather than reconstructed characteristic-zero coefficient arrays.

The complete [R899 K-fixed basis](R899-certified-original-K-fixed-seven-trace-RR-basis.md) was consumed as actually produced. The original marked \(Q_N\) and its producer metadata were extracted from that completed source carrier, retaining R894's exact identity and full principal-function expression. Old flips, \(Q_N\), the K-fixed basis, W, Krylov inverses, old V3 fibre evaluations, P0 jets and the t constant were not recalculated.

## 2. First pencil: complete rank 1234 and the original degree-544 divisor

Keep \(T_0=T_f^0\) and R899's exact K-fixed basis
\[
S_i=Q_N w_i\in H^0(2H-T_0),\qquad 0\le i<418.
\]
The first anchor is the unchanged column \(S_0\), whose original P0 leading coefficient is a genuine unit at the auxiliary place. The first accepted second anchor is the integer trial 1:
\[
S_1^{\mathrm{trial}}=\sum_{i=0}^{417}S_i.
\]
No coefficients or leading units were rescaled.

The relation calculation cancels the shared nonzero \(Q_N\) **before** evaluation:
\[
S_0 r+S_1^{\mathrm{trial}}s
=Q_N(w_0r+w_1s).
\]
Thus it does not require \(Q_N\) to be a unit in each evaluation fibre. All seven original length-272 Artin fibres at nodes 0 through 6 are retained. Their total length 1904 exceeds \(\deg(6H)=1632\), so evaluation on these whole fibres is injective on the original V6 space.

The resulting 1904-by-1380 product matrix has actual rank **1234**, with selected minor
\[
634820587\pmod\ell.
\]
Both inverse products and all 1904 original relation rows were checked. Combined with the precise geometric upper bound in R900, this certifies that the first pencil has no additional common divisor.

Set
\[
D_0=\operatorname{div}(S_0)+2H-T_0.
\]
This is the original K-defined effective divisor of degree 544, avoiding P0. The canonical free-coordinate relation kernel and its second projection give the complete space
\[
H^0(3H-D_0),\qquad\dim=146.
\]
The projected 690-by-146 normal matrix has actual rank 146; its selected projection minor is 224157246. Its exact K-fixedness follows from the K-stable relation space and the retained free-coordinate identity, not from sampling Galois conjugates.

## 3. Second pencil: complete rank 962 and the K-defined degree-272 representative

In the complete canonical 146-space, the first unchanged column with unit original P0 value is column 0. Denote it by \(v\). Its actual value is
\[
v(P_0)=598945491\pmod\ell.
\]
This section is not divided by that value. The second pencil also succeeds at integer trial 1, with its second anchor the sum of all canonical 146 columns.

On the same seven whole fibres, the second 1904-by-1380 matrix has actual rank **962**, with selected minor
\[
803546737\pmod\ell.
\]
Its two inverse products and all 1904 relation rows are certified. The geometric rank bound and this unit certify the complete residual space and the effective divisor
\[
D_K=\operatorname{div}_{3H}(v)-D_0,\qquad
\deg D_K=272,\qquad P_0\notin D_K.
\]
Both \(D_K\) and its exact complete space
\[
H^0(3H-D_K),\qquad\dim=418,
\]
are defined over the original K. The second projection has actual rank 418, with projection minor 560974184. Again the canonical free-coordinate relation basis retains the original K structure and the original normal V3 convention.

| Exact completed object | Bytes | SHA256 |
|---|---:|---|
| R900-complete-K-defined-D0-146-certificate.json.gz | 6200 | 8a83f1b8487cc407a8cc483234100ba8d147fbe03a2b1f39875c75944ba58dce |
| R900-first-pencil-trial-000001-complete-K-fixed-normal146-space.json.gz | 411453 | 2f01eb48d4093a56e99807594dc25f25d59f4a495853426ab30e92d8afb112c1 |
| R900-complete-K-defined-DK-418-certificate.json.gz | 6169 | 152a225b14d91acaf88c67f695a2981c1e6aa10519b5484b5c1a5d7236d7ad9c |
| R900-second-pencil-trial-000001-complete-K-fixed-normal418-space.json.gz | 588416 | 2489facf81b48ceaedb775279e59af60f4eb7b26ae6833277e865b6c7af69a0f |
| R900-original-unscaled-v.json.gz | 8146 | 500e66fd8c5c0aee34359659735dd17843026fcbfad8994e81be87ce9d7e3405 |

The completeness statements concern the exact characteristic-zero spaces defined by these units and the geometric rank proof. They do not assert that arbitrary modular zeros are exact characteristic-zero identities.

## 4. The original principal identity and both marked leading coefficients

The actual marked principal is
\[
Q_K=\frac{S_0}{v}=\frac{Q_Nw_0}{v}.
\]
Both \(w_0\) and \(v\) already denote the original normal V3 functions divided by \(\tau^3\); their ratio has **no additional \(\tau\) power**. The original trace identity is exactly
\[
\boxed{\,T_0=(D_K-H)+\operatorname{div}(Q_K).\,}
\]
Indeed, substituting \(D_0=\operatorname{div}(S_0)+2H-T_0\) and
\(D_K=\operatorname{div}(v)+3H-D_0\) proves the identity with the displayed positive \(Q_N\) direction.

The unscaled source values are
\[
w_0(P_0)=88897486,\qquad
\operatorname{LC}_\rho(S_0)=528708486,\qquad
v(P_0)=598945491
\pmod\ell.
\]
The marked certificate gives
\[
\operatorname{ord}_\rho Q_K
=\operatorname{ord}_t Q_K=-8435,
\]
\[
\boxed{
\operatorname{LC}_\rho(Q_K)=515264909,\qquad
\operatorname{LC}_t(Q_K)=898623080
\pmod\ell.}
\]
The exact leading expression is the unchanged R894 leading coefficient times \(w_0(P_0)/v(P_0)\). The t conversion is positive multiplication by the retained \(c^{8435}=427728351\), where the original R883 coefficient is \(c=354813668\). Neither original \(Q_N\), \(S_0\), \(v\), nor either output leading coefficient is normalized to 1.

The marked file is R900-original-K-defined-DK-and-marked-principal-QK.json.gz, 5891 bytes, SHA256 c04fa64203155e11700d3da654799069894a18ba093291adf04eef8feb63e2a2. It preserves the full exact principal DAG and every original source reference, not merely the class of \(D_K-H\).

## 5. Current source closure and successor boundary

The one-day artifact is serre-global-R900-K-defined-degree272-43889194318-1, artifact 14236126620, 70095408 bytes, SHA256 bcbffdd5f301447507d77f1c3d908e060bfd8d488baedf61dff6d3f9c0b3698c, expiring 2026-11-17T14:47:25Z.

The necessary source carrier retains 48 unchanged selected members from R827/R883/R890/R894/R899. R900-retained-original-inputs.tar.gz has 25615974 bytes and SHA256 d6dc4747156cfd1e47a929d68632c042029e7567e6df8711d19e796c7655704c; its inventory has 40524 bytes and SHA256 8e8d4bda142a190fa82fe8fdaee694670822b55b285840c102d918f026aa67c1. All new numerical arrays and raw machine outputs remain in the necessary one-day artifact.

This supplies the real K-defined trace input for [R901's original shared 126-node construction](R901-original-five-Z-shared-bounded-flip-DAG-and-marked-principals.md). The separate R902 strict six-Galois input is still required. R901's immutable plan remains a definition with zero completion counters; only an actual execution request can consume completed inputs.

No Q-defined effective divisor, expanded characteristic-zero arrays, Picard principality, active Hecke support, five 128/144 spaces, connection calibration, non-p terms, period or height bound is inferred here. The original curve, embedding, t frame and absolute-uniformity target remain unchanged.
