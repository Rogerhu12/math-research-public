# R862 — Certified original Rosati projector polynomial and integral correspondence

Date: 2026-11-16. Status: **completed by the public repository's GitHub Actions**.

The [whole-Jacobian argument](R862-original-Rosati-projector-from-certified-Hom-correspondences.md), SHA256 afa1e0d08d0a0bd65374fee1996f0d644588840dee35fec7d766cc2f4e5707d0, identifies the original operator
\[
D_A=q_R^\dagger q_R
\]
with the sum of seven original elliptic-map pull–push correspondences. The following exact polynomial and integer multiple have now been obtained from its already certified original Hom and polarization data.

## 1. The actual polynomial and positive integer

The field is the original real field with
\[
\Psi(S)=S^6-S^5-6S^4+6S^3+8S^2-8S+1.
\]
The original Chebyshev coordinates retain the constant \(3870\cdot1\):
\[
a_A=3870+711s_1-801s_2-360s_3+612s_4+864s_5.
\]
The completed arithmetic gives its power-basis expression
\[
a_A=6696+6111S-3249S^2-4680S^3+612S^4+864S^5
\]
and the exact norm polynomial
\[
\begin{aligned}
P_A(X)={}&X^6-25326X^5+246668814X^4\\
&-1172462391702X^3+2870294606314506X^2\\
&-3449069535780048033X+1596092727686814808731.
\end{aligned}
\]
Thus the actual positive integer is
\[
\boxed{d_A=1596092727686814808731.}
\]
No minimal-denominator claim is made.

The six integral Faddeev–LeVerrier divisions were exact. The certificate also contains and verifies the original-field Cayley–Hamilton identity and
\[
\begin{aligned}
d_A a_A^{-1}={}&292749581283070590
-597768876071527482S\\
&+311524250434046244S^2
+561137346503715870S^3\\
&-53640701367535485S^4
-121342921924210182S^5.
\end{aligned}
\]
Neither the original \(\kappa\) nor \(v^\dagger v\) has been replaced by one.

## 2. The actual integral correspondence

The completed program has 23 nodes. Its canonical integer output is
\[
\begin{aligned}
F_A={}&-D_A^6+25326D_A^5-246668814D_A^4\\
&+1172462391702D_A^3-2870294606314506D_A^2\\
&+3449069535780048033D_A.
\end{aligned}
\]
Consequently
\[
\boxed{E_A=d_A^{-1}F_A
=1-P_A(D_A)/d_A=q^\dagger\kappa^{-1}q.}
\]
The last equality on the **entire original Jacobian** uses the cited paper proof. The arithmetic has separately verified \(P_A(E)=0\) and \(F_A(E)=d_AI_{12}\) on the completed original 12-dimensional Hom matrix, and the polynomial idempotence identity modulo \(XP_A(X)\). It does not infer a whole-Jacobian equality merely from those twelve rows.

All seven finite pull–push recipes retain the original map, its Galois transports, basepoint, elliptic polarization and scheme multiplicities. The five original symmetric directions have the unchanged pairs
\[
(165,67),\ (93,67),\ (100,67),\ (168,67),\ (371,134).
\]
They are recorded as integer differences of the corresponding original pull–push expressions. Their fibre-product equations have not been expanded into another large equation list.

## 3. Two genuine runs, with no repeated arithmetic

The arithmetic producer was run **43812454495**, source
dd58327584065e20e6106ec112ddb1b0b50a67a9, mathematical core SHA256
4656250c7fcd86c9e6d36a4c94925979b27cc4ab54e0cb1299e6972319598a86.
It completed all four stages. Its final writer then failed because a loop variable had shadowed the intended program filename: the completed program was actually named
R862-original-projector-integral_h_5.json.gz.

The [completion-only repair](../notes/R862-completed-stages-finalization-only.md) was run **43813805093**, job **133121204720**, source
aa45ec93ff0530a2af545bfea1185b8c5a8ac6cd, and succeeded. Its execution core SHA256 is
dca646e36abc62bc4ffe0d8b8003d73f1e569e9ccbee288e80cd73211c0c225d; wrapper SHA256 is
ee9bcb645e6192fb5261a5b3314d371b8238ee4c0e6452433513b1cb1c02dbd5.
The completion core reports 0.0028908240000049545 seconds and explicitly reports **no new mathematical arithmetic**. The four stages, stage index, mathematical configuration and original source inventory remain the arithmetic producer's original bytes; the historically shadowed filename is retained.

| Exact object | Bytes | SHA256 |
|---|---:|---|
| Final certificate | 6311 | 41a582652d1301d2044be03b69463d6863a0eea197a738ec5d3abca355233124 |
| Original norm stage | 2374 | 0d0d4b6ffa3a367e1427242b43eacdc8778e4c8f78271d61b800fdaca3da5e37 |
| Original 12-dimensional action | 1817 | 4859b1ceffa05b5f24935fbb256bc209d9c687668fa79c9ef73e058b2881b5eb |
| Original 23-node program | 2828 | dc817307942163da9fe25f1aeb9789006af68342296988590cbaccf7d08036b0 |
| Original four-stage index | 1886 | 06ec96ddb8057ee268875d91eeccb936ad966393d76c4127630f1b6066f1f420 |
| Original source audit | 1698 | 348a9dcfd569f38163ce3d50786e8ff0357d07d40d29c7e8be30fe5056e38d4e |
| Completion run's full manifest | 2222 | 85ebbce2301ed30094ac73621b9e17daecf5d68afde5ced6ef009251d297bc21 |

The unchanged mathematical configuration fingerprint is
2bddd0283a540b61fe421414505af6ca9f4a7f1f9d0b91877ca97a9f36bc1b42.
The 17 direct retained source files comprise R852's nine and R791's eight actual files, preserving the underlying 270-leaf carrier and all original producer identities. Their 2662748-byte carrier has SHA256
00db03fbc930c5728dfbc7d021b3cf7f5205710fbc7a3b06b0c6e62fbab8a292.

The successful artifact is **14201721469**, named
serre-global-R862-original-Rosati-projector-43813805093-1,
2717249 bytes, SHA256
1e820eadb222223c7be293f498c940ed28048fe229788bfc416918ac16b408ae,
expiring 2026-11-17 06:00:18 UTC.
The main session actually rehashed its whole ZIP, manifest and all fourteen listed files by pure IO. No mathematical module was run locally, and no machine output has been added to Git or a Release.

## 4. Exact boundary of this result

The original identity \(E_A\phi^*=0\) remains in force. This completed projector does not identify the active projector \(e_\eta\) on the original \(Y\), its integer \(d\), or its torsion-clearing \(N\). The number \(d_A\) above is not a substitute for those quantities, and its prime divisors do not by themselves give the full non-\(p\) height support.

Rigidified section comparisons, principal correction functions, the actual \(Y\) Hecke action and complete non-\(p\) terms remain their separate tasks. Neither the full original height nor Serre uniformity has been completed. The next original-\(Y\) operator is the shared-basis \(T_7\) consumer R865; the old Hom/Gram/norm work is closed and is not to be repeated.

