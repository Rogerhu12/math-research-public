# R866 — Certified original semilinear action and complete Q-holomorphic basis

Date: 2026-11-16. Status: **the complete original 127-dimensional holomorphic descent has been computed**.

The public repository's successful run **43815338283**, job **133126104764**, source
6373b025e7a4ea02a2beb3bb36a01447176903c9, completed all **52 stages** in
**3.399841967000043 seconds**. It gives the actual action of the original \(c_Y\), an exact selected \(127\times127\) inverse, and a full \(\mathbb Q\)-fixed basis of \(H^0(Y_K,\Omega^1)\). The [method](../notes/R866-original-holomorphic-semilinear-action-and-Q-fixed-basis.md), SHA256 0ecc37602135f9605e52e667a9e180215213772192f09897dce33026030a96f9, proves that these complete Fourier equalities identify the original global differential action.

## 1. The actual shared matrix and exact inverse

Let \(B\) be R864's already completed \(146\times127\) matrix in the original \(V_1\) basis. The new computation formed
\[
H=AB\in M_{560,127}(\mathbb Q),
\]
using all forty cyclotomic coordinates for each of the original orders \(q_Y^0,\ldots,q_Y^{13}\).
All forty constant rows are exactly zero. The actual rank is 127.

From within the old R837 set of 146 independent rows it selected a genuine 127-row set \(J\). For \(Q=H_J\), the exact determinant is nonzero and the saved inverse \(U=Q^{-1}\) satisfies **both** exact inverse products. The full selected row numbers and determinant are retained in the certificate; no full 146- or 272-dimensional conjugation matrix was recomputed.

The original sections are already \(e_i=82^2T_{(1,i)}\). Thus \(H\) is the Fourier matrix of
\[
F_j=\sum_i e_iB_{ij},\qquad \omega_j=82F_j\,dq_Y/q_Y.
\]
The differential coefficients are \(82H\); the recorded section scale 6724 does not prescribe a second multiplication or division.

## 2. The actual original semilinear matrix

Let \(S\) multiply the row at order \(n\) by \((-1)^n\). The computation obtained
\[
C=U S_J Q
\]
and verified
\[
\boxed{HC=SH,\qquad C^2=I_{127}.}
\]
The first equality was checked on **all \(560\times127\) original coordinates**, not just the selected rows.

The genuine action on coefficient columns is
\[
x\longmapsto C\bar x,\qquad \bar s=-s,\quad s^2=-3.
\]
The coefficient involution fixes \(\xi_{41}\); the geometric twist changes \(q_Y\) to \(-q_Y\). Both parts are retained.

The actual selected parity counts are **54 even and 73 odd**. Hence the rational linear matrix \(C\) has corresponding \(+1\) and \(-1\) eigenspace dimensions 54 and 73. These linear eigenspaces do not by themselves constitute the full fixed space of the semilinear action.

## 3. All 127 genuine Q-fixed differentials

Put
\[
d_j=\begin{cases}1,&J_j\text{ has even }q_Y\text{-order},\\
1/s=-s/3,&J_j\text{ has odd }q_Y\text{-order},\end{cases}
\qquad P=U\operatorname{diag}(d_j).
\]
The completed column stages contain the original coefficients of all the differential combinations
\[
\widetilde\omega_j=\sum_i\omega_iP_{ij}.
\]
They verify
\[
C\bar P=P,\qquad S\overline{HP}=HP
\]
on every relevant original row. Since \(U\) is invertible and every \(d_j\) is nonzero, these 127 vectors are independent over \(K\); the descent argument in the method gives the full 127-dimensional \(\mathbb Q\)-fixed space.

The \(V_1\)-to-normal transport retains the negative \(e_{73}\) correction exactly once. R864's conversion was already applied when its original \(V_1\) coordinates were recorded, so no second positive conversion was made here. The original \(\tau,\nu\) and the differential factor 82 are unchanged.

## 4. Actual source and output identities

| Completed object | Bytes | SHA256 |
|---|---:|---|
| Final certificate | 6120 | 00398c7c534c58d45106819b0731c16c6c72866a7299e581f36119608d1ac203 |
| Original Fourier matrix \(H\) | 468416 | 3c9ce8d3258d9a829c5588429523df640b3e6cb7a5d2fac050181ba34b6e50fc |
| Selected exact inverse | 599746 | e93951a05190af9e63ac9163797036ad88f1aaa5a360048d85e57d8c69d15e54 |
| Actual row selection | 2872 | 2e4310372b67a5a87300975a6ed689c38efec1c738e63ddeb7645953b7937cd1 |
| Actual semilinear matrix | 130421 | 70af52dd7252cc3e64bce98df4bf51c5e926b01b273a11a54e1be271be0b9b98 |
| Complete Q-basis index | 3412 | c956060107347f601ff08815124fbd66aac24518f2e82a2c066a6845abefe3a4 |
| Complete 52-stage index | 4910 | 84d752618604a4652691c527d340b86890ee1c50b302a7c5607390af847f0451 |
| Full output manifest | 10896 | 13e2f67fd009fa5c66d581c394e1a1e9893e09301aa594b2a4eb88e2ecc0d78b |

The mathematical configuration fingerprint is
7e6a55e273e2fd6570ed192d8b0a1b1b0a9deb543b4e5305fe277900914b5bc7.
The core is 2b8aa7c10efcca6899df4de84abb3eb0b81e414aae931de9cca578dfffcc9fce;
the wrapper is 7074905457e9299219fd8822b0272a034941cdb21fe07c94110fe5275b1b787c.

Artifact **14202411654** is named
serre-R866-original-holomorphic-semilinear-descent-43815338283-1,
5722522 bytes, SHA256
007b72c88ee1d72643978d67c7463b05ad14b086029386bfda39312c45403b22,
expiring 2026-11-17 06:14:40 UTC.
The main session rehashed the complete ZIP and all 65 manifest-listed outputs by pure IO.

The 178 original source files are R786's 152, R837's eight, R853's nine and R864's nine. The retained carrier is 2289659 bytes, SHA256
b865217a9836eea13fac3a9c67b92b131c4eb1c1feb1c1d62a6d3c74ab40f81c.
Its inventory is 33581 bytes / 53dae172883043dcb6e092cf3e8cf556dec53107cce9d88762904c4908791c97,
and its receipt is 6134 bytes / 90c13e916517626bee8fe8d27faf5b9c1cf0f79d69fa421de032ff3dceb80513.
All original producer identities are preserved. The old Fourier coefficients, cusp kernel and three generator conjugates were not recomputed.

The initial attempted run 43814823286 had no jobs because of a YAML colon in the pip command. The [activation record](../notes/R866-original-holomorphic-descent-activation.md) records the sole workflow syntax repair. It changed no mathematical core or input, and no mathematical stage existed in that failed attempt.

## 5. Direct next consumer and remaining scope

R865 now reads this same \(H,J,U\) and the fixed-basis interface for the original \(T_7\) correspondence. It must not repeat the shared prefix construction, row selection or inversion. Its full Fourier multiplier equations are new mathematics and remain to be computed separately.

This result completes the holomorphic descent. It does not compute the 128- or 634-dimensional meromorphic Riemann–Roch spaces in YP, a connection, a period row, the active \(e_\eta\), its torsion-clearing integer, any complete non-\(p\) height terms, or the full original height. Serre uniformity remains open.

