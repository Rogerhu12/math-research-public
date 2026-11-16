# R899 — Certified original K-fixed seven-trace Riemann–Roch basis

Date: 2026-11-16. Status: **the complete original 418-dimensional K-fixed function basis and its unchanged first P0 unit column are certified**. All new arithmetic was executed in this public repository's GitHub Actions. The main absolute-uniformity problem remains open.

## 1. Actual producer and scope

The successful [public run 43879192431](https://github.com/Rogerhu12/math-research-public/actions/runs/43879192431), compute job 133366133706, used source commit `34001929c3c44484a7beefe396352c22ed68c1b7`. The core completed 280 retained mathematical stages in 9.162237032 seconds, with process exit 0 and a complete final certificate. The original queue entry eventually ran; it was not dispatched again.

| Bound object | SHA256 |
|---|---|
| Core | 9901767869180e7ff6c20ab56a693024adeef7d77aeb5b1105af0476a36e0248 |
| Wrapper | 2a887562b40272bdb6ba477342f9bbe2190cbd9364b6ff1ce7e3f676ceaeb794 |
| Mathematical configuration | cd913c163caeec5655ef3a7f4ed6415dcad8034611d46105d89e2155a31efa71 |
| Complete certificate, 72971 bytes | ff97cb88486f52fc3f5a621cb59d121fdb38c8f9fe0f2dc2faa2a3ddf298b43d |
| Complete manifest, 38889 bytes / 291 files | cb951c29e170592dc9f2ca3659290fa2f082a36185ac5377219de26a2e288eaf |

The arithmetic prime is the unchanged auxiliary prime \(\ell=1000000753\), and the original branch is retained. This is not a declaration of an integral unit at 41.

The exact mathematical construction is [R899's fibre-coordinate theorem](R899-original-K-fixed-trace-RR-basis-from-fibre-coordinates.md). Its inputs are the actual [R894 seven-pole trace](R894-certified-original-seven-pole-trace-and-marked-descent.md), the original R827 whole Artin coordinates, the original R890 normal V3 fibre arrays, and the fixed [R883 t frame](R883-certified-original-t-first-order-frame.md). The 16 completed flips, six Galois replays, old Krylov inverses, old normal arrays, P0 jets, and t constant were not recomputed.

## 2. The actual complete fibre-coordinate isomorphism

Write \(W_N\) for the original complete 418-dimensional normal space of \(D_N\), \(B_N\) for its 690-by-418 V3 coefficient matrix, and \(Q_N\) for the unchanged marked principal function. The K-defined space is
\[
\mathcal S=H^0(2H-T_f^0)=Q_N W_N,
\]
of dimension 418 and divisor degree 544. The normal sections without \(Q_N\) are not themselves asserted K-fixed.

The run evaluated the original functions on the three **complete length-272 fibres** at nodes 0, 1 and 2, using their original K coordinate bases and retaining every factor, multiplicity and denominator. The resulting 816-by-418 coordinate matrix has actual rank 418. Its selected rows are node 0 coordinates 0 through 271 followed by node 1 coordinates 0 through 145, in that order. All 418 original columns remain in order.

The selected square matrix \(A\) has
\[
\det A\bmod\ell=157473788\ne0.
\]
Both inverse products were checked, and the same inverse was applied to **all 816 rows**, not just the selected square. The selected coordinates of all new columns are exactly the identity matrix. Thus the actual unit chart required in the fibre-coordinate theorem has been supplied, without replacing it by a dimension estimate.

Define the exact original functions by
\[
(S_0,\ldots,S_{417})=Q_N\,B_N A^{-1}.
\]
Here \(A^{-1}\) is the exact unit-solve expression bound to these precise source rows and columns; only its auxiliary-prime array is expanded. Because the coordinate map is K-linear and these selected coordinates are rational identity vectors, uniqueness shows that each \(S_i\) is fixed by the original \(\operatorname{Gal}(L/K)\). This is a basis of the complete original K-space, not a chosen smaller subspace.

The old basis descent matrix remains the exact expression \(A^{-1}\sigma(A)\), with the multiplier \(\sigma(Q_N)/Q_N\) retained. The new fixed-function basis has identity descent by uniqueness, and the original sevenfold cocycle telescopes exactly. No sixfold replay or numeric old descent matrix is needed for this conclusion.

| Actual output | Bytes | SHA256 |
|---|---:|---|
| R899-evaluation-profile-nodes-0-1-2.json.gz | 2504058 | 698e2fa4875dc466e86cfd93c4dd451c9a2a735951e5eac269b754f4377b7e76 |
| R899-K-fixed-normal418-basis.json.gz | 1284055 | e74b821c0905d7825d3cc9c9c3fcbed3e22c0d11edbb1e12428a3b350d45f122 |
| R899-original-source-audit.json.gz | 23678 | 75ff9bea2c7bbbf1c6df19dca6a033b962f7f311f9ad29eda6a0f7a9c5309cec |

The complete normalized regular V3 space fibre arrays at nodes 0,1,2 are also retained. Their byte sizes and SHA256 values are respectively:

- 773058 / 68519cf569f641f2fbb6795b8dcd8de28225908e4d63e8cf6d64d2c4a04c3b8e;
- 1163438 / 1983c1e94e2dd54f2ec970da328cdcbf31e38af1719be824f94d370234594184;
- 1163585 / 974552ca2f176e49f0f0a4259ad826bfa5249f438e3e62f191548f2fe213db9b.

These are the normalized **regular sections** with the \(Q_N\) factor separated, so the next consumer can cancel \(Q_N\) before testing its two pencils. It must not impose an unnecessary whole-fibre unit condition on \(Q_N\).

## 3. Unchanged first P0 unit column

The original P0 functional, original \(Q_N\) and original t frame were transported through the same basis change. The first actual unit column is **column 0**, with no rescaling. Its normal V3 P0 value and its function's two leading coefficients are
\[
w_0(P_0)=88897486,\qquad
\operatorname{LC}_{\rho}(S_0)=528708486,\qquad
\operatorname{LC}_{t}(S_0)=590477772
\pmod\ell.
\]
The function has original \(\rho\)- and t-order \(-8435\). The positive conversion factor is the already retained \(c^{8435}=427728351\), where \(t=c\rho+\cdots\). The original \(Q_N\) leading coefficients remain 305966999 and 397080916 in the respective frames. None of these quantities is normalized to 1.

This actual modular unit supplies the unchanged first column required by R900. The leading row is bound as R899-original-P0-leading-row.json.gz, 24097 bytes, SHA256 8f6bcf2845bc87cd8834453ecc1e7c1d8637d3b348e3b8789c6e2793b3dfa2da. Its certificate expressly distinguishes the exact nonzero row from the actual modular unit check.

## 4. Original source closure and direct continuation

The one-day artifact is serre-R899-K-fixed-seven-trace-RR-43879192431-1, artifact 14234003349, 45236413 bytes, SHA256 907c1ef83ae70b5ccff655efb1690d9675b359df9ff757089bd50db5dcdfd1a6, expiring 2026-11-17T14:33:02Z.

Its necessary original carrier contains 164 unchanged members from the ten original source groups. In particular, it retains the actual R894 producer metadata and marked \(Q_N\), with the original complete global function DAG and producer identity. R900 can take that small bound source group from this completed carrier instead of downloading the full R894 archive.

| Retained object | Bytes | SHA256 |
|---|---:|---|
| R899-retained-original-inputs.tar.gz | 27656178 | eabd06641b2a4e01c13801ae019ad1f3de187e992741271dc89ffb97c84d9205 |
| R899-original-source-inventory.json | 65880 | ecc5d614e1c728625a0a60553360ab2841955db2ca4b29b8ba5aa6c5af9f95bc |
| R899-stage-manifest-5b4abf6cd8d833cf724a1e61274e8c6f23705c8ab2683a3a44679ac1061fcd02.json.gz | 27332 | 0dbb5e7da261057d836e04f9352593ae8023ca83a78d6eb2e37202efdd08e9ee |

Raw arrays remain only in the current necessary one-day artifact. This result records their identities and mathematical meaning, not their bytes in Git.

The existing [R900 execution method](../notes/R900-original-K-defined-degree272-consumer-method.md) now receives the real R899/R894 sources. Its next new arithmetic is the complete 1234-rank first pencil with residual dimension 146, then the 962-rank second pencil and complete dimension 418, to construct \(D_K\) of degree 272 and
\[
T_f^0=(D_K-H)+\operatorname{div}(Q_Nw_0/v).
\]
These ranks and the effective representative are not asserted completed by R899.

## 5. Boundaries retained

No Q-fixed basis, characteristic-zero coefficient expansion, K-defined effective degree-272 representative, five \(L_j\), Hecke endpoint calibration, non-p connection, period normalization or height bound has been computed here. The exact basis and its auxiliary-prime unit certificates are the completed inputs for the next original consumer; the absolute Serre uniformity criterion remains open.
