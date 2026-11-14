# R771 — Certified original quotient bases in weights 2, 6 and 12

Date: 2026-11-14. Status: **proved and the specified public computation completed**.

The original level-82 quotient now has explicit characteristic-zero recipes for bases of dimensions \(146,694,1514\). This assertion is certified by actual nonzero coefficient minors of those same recipes at the fixed good reduction prime \(739\). The computation does not lift a reduced row combination as a characteristic-zero formula. It has not yet computed the original rational map, \(\beta\), a full characteristic-zero Fourier table, or any height.

## 1. Exact public execution and retained inputs

The successful public execution is [run 43628998192](https://github.com/Rogerhu12/math-research-public/actions/runs/43628998192), attempt 1, in Rogerhu12/math-research-public, from source commit

49abc04d7867c9f56911866494692c597cf642d7.

The mathematical core reports **301.12633604 seconds**. Its process exited with code zero, and its final receipt was written at 2026-11-14T18:57:33.660029+00:00. The workflow completed successfully, including the final step requiring all three actual ranks and nonzero minors.

The exact source and method hashes are:

| Input | SHA256 |
|---|---|
| Core R771_original_quotient_RR_bases.py | 9cda269687a01c95c9c20695be771706bbddd37b1b8fedc8b9258386c3965d46 |
| Public wrapper | a850a84197ce7f0fe5ef2162b796aed1c7ee983e53da4e84f7bc875120a2b2a6 |
| Original method note | 3ff0f1aa3da867d1898ff968911ec5837c34ae5d7e873b378645c8fa67a0e36d |
| Original request | a9615bfd01fba9dd93dac699dc19399bd627e61263fb725ae9cff7e71e59b14f |
| Dedicated workflow | cb559fe89babca7a7744322c6bd1a82ae7a715e16a1775dfd4b964b4bbe0f9db |
| R767 proof | 33fb32458eaf62e1499de092b6139672304ceefe096eef4a5253a2d7637a940d |

The source request consumed the existing R745 and R759 small certificates verbatim:

| Retained result | Original run | Certificate SHA256 |
|---|---:|---|
| Original Hodge input R745 | 43616027318 | 7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be |
| Full integer period lattice and degrees R759 | 43625474728 | 7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0 |

It did not recompute the original topology, periods, Hom kernel, integral lattice, map degrees, or the old Hodge minor. No large old artifact was required for this run.

The small outputs are committed under

[computations/R771-p41-original-quotient-RR-bases/43628998192-1](../computations/R771-p41-original-quotient-RR-bases/43628998192-1).

The final certificate has SHA256

9eb870af949167895daa4e180c16848860f8fea1c9efe1b105ab3cd3a667009f,

and the full output manifest has SHA256

024ed12029720cc1c5d7ec0612aa484b04cdde8f763fceb852a0fdeabc2c3d74.

These files contain the actual selected seed labels, every coefficient exponent in each minor, the exact retained-input hashes, and all stage hashes. They are numerical outputs of the successful run, not values copied from theoretical dimension predictions.

## 2. The original group and exact recipes

Retain the curve \(Y\), original reference coset, cusp parameter, and original CM marking of R762/R767. Thus

\[
g(Y)=127,\qquad q_Y=Q^3=\exp(2\pi i\tau/82).
\]

The subgroup \(H_{82}\) is the inverse image of the original order-three subgroup modulo 2 and the original Cartan normalizer of determinant one modulo 41. It has order \(252\); the effective even-weight trace has \(126\) terms.

The seed functions are the actual weight-one Eisenstein products

\[
B_{\lambda,\mu}
=\frac12\sum_{h\in H_{82}}E_{\lambda h}E_{\mu h}.
\tag{771.1}
\]

Here \(\lambda,\mu\in(\mathbf Z/82\mathbf Z)^2\), row-label action is on the right, and \(E_\lambda\) has the original Zywina normalization including its constant term and both signed divisor sums. In particular no Fourier-only trace discards the constants. Replacing both labels by their negatives leaves the product unchanged, accounting for the factor \(1/2\).

The formal recipes are defined in characteristic zero. Each recorded M2 seed is one whole expression (771.1), and each higher-weight recipe is a recorded product or an explicitly named elliptic correction of these original expressions. Gaussian elimination selects independent original candidate rows; it does not define a new characteristic-zero row by lifting coefficients of a reduced linear combination.

The finite computation used

\[
\ell=739,\qquad
\overline{\xi}_{41}=538,\qquad
\overline{\xi}_{82}=512,\qquad
\overline{\sqrt{-3}}=98.
\tag{771.2}
\]

Its coefficient tables run through \(q_Y^{1640}\). The label enumeration supplies all 40 first-label orbits and 3360 second labels modulo sign; its complete candidate family has 134400 members. Streaming stopped when an actual full minor had been obtained. The selected 146 seeds are given individually in the small certificate. Their candidate permutation indices run from 0 to 298; an unselected candidate is not silently counted as a basis element.

## 3. Actual nonzero minors and characteristic-zero bases

The successful execution produced:

| Space | Actual selected dimension | Coefficient exponents used by its square minor | Determinant modulo 739 |
|---|---:|---|---:|
| \(M_2(H_{82})\) | 146 | \(0,1,\ldots,145\) | 550 |
| \(M_6(H_{82})\) | 694 | \(0,1,\ldots,693\) | 206 |
| \(M_{12}(H_{82})\) | 1514 | \(0,\ldots,1494\), then \(1496,1498,\ldots,1532\) | 140 |

Every determinant is of the original recipe rows at the explicitly recorded exponents.

All constants and denominators in the recipes are integral at the chosen prime above 739. The relevant level and small scalar denominators are units, and the chosen root of unity retains its exact order. Therefore a vanishing characteristic-zero determinant would reduce to zero at that prime. The three displayed nonzero reductions prove characteristic-zero independence of the corresponding original recipes.

R767 gives the matching characteristic-zero dimensions. Consequently these independent families are bases of the claimed original spaces. No unproved lifting of numerical coefficients is needed for this implication.

For completeness, the exact normal-product dimensions obtained on the way are

\[
146,\quad418,\quad690,\quad962,\quad1234,\quad1506
\tag{771.3}
\]

for \(H^0(Y,r\mathcal L)\), \(1\le r\le6\), where

\[
\mathcal L=K_Y+D_{\rm cusp},\qquad \deg\mathcal L=272.
\]

The weight-six basis extends the 690-dimensional normal-product space by the two first elliptic principal parts from \(E_4H^0(\mathcal L)\) and the two remaining parts from \(E_6,\eta_{\rm Ded}^{12}\). The weight-twelve basis extends \(H^0(6\mathcal L)\) by four successive two-dimensional principal-part layers, as proved in R767. The actual layer files preserve all selected product indices and all coefficient rows.

These statements concern the original modular-form spaces over a coefficient field containing the displayed roots of unity. Producing a basis defined over the smaller arithmetic field \(K\) requires the semilinear determinant trace of R772. This further descent was not performed by R771.

## 4. The actual Riemann–Roch basis

Use the unchanged original divisor and section

\[
D=2(t)_0,\qquad \deg D=1640,
\]
\[
D_\star=t^2\Delta
=\left(\frac{\eta_{\rm Ded}^{12}}2-\frac{\sqrt{-3}\,E_6}{144}\right)^2.
\tag{771.4}
\]

R767 proves the exact section identity

\[
\operatorname{div}_{6\mathcal L+4(P_0+P_1)}(D_\star)=D.
\tag{771.5}
\]

Thus, if \(F_1,\ldots,F_{1514}\) are the actual selected weight-twelve recipes in the certificate and stage file, then

\[
\boxed{\quad F_1/D_\star,\ldots,F_{1514}/D_\star
\text{ is a basis of }L(D).\quad}
\tag{771.6}
\]

The denominator has the original nonzero reference-cusp constant \(-1/6912\); no zero-at-cusp division is being hidden. The correct field contains the original \(K\), even though the modular-form recipes themselves have coefficients in \(\mathbf Q(\xi_{82})\).

The original R759 selected map is still index 4 of degree \(1206\), and R764 still gives its zero base translation. R771 does not select a different differential or a smaller-degree map. R769 has separately ruled out nonzero vectors of degree at most 693 in the complete original lattice; that finite search is not repeated here.

For the map recovery, the unchanged R767 full bounds remain 2847 Laurent rows, exact basis series through \(q_Y^{2846}\), and the original differential coefficient prefix through \(Q^{8557}\). The true global kernel has dimension 308 and rank 2720. R772 permits ending earlier once that full rank has actually been certified using accurate original rows over the descended coefficient field.

The tables in this run are reduced coefficient tables through 1640. They are not the full required characteristic-zero series through 2846. Formula (771.6) is already exact because it specifies functions by characteristic-zero recipes and proves their independence; finding the desired numerator and denominator in their span remains a subsequent calculation.

## 5. Preserved stages and receipts

The complete artifact is

serre-global-R771-p41-original-quotient-RR-bases-43628998192-1,

GitHub artifact ID **14127715743**, size **28383469 bytes**, with ZIP digest

e158bff06405576ce235745db26b6a2e35145d2b1f2d6978127b42a79e1e7c1c.

Every complete coefficient table is gzip-compressed and kept in the artifact rather than committed as a large reproducible table. The manifest contains the hashes of all 82 Eisenstein row blocks and every intermediate basis layer. The principal reusable completed files are:

| File | Bytes | SHA256 |
|---|---:|---|
| R771-basis-M2.json.gz | 301150 | b0b5b3f38be3355fdecb03a91638713319da14e8bd7765a5b68df5c9914f742f |
| R771-basis-power-2.json.gz | 866466 | 6c4e58ec65f5cf1bb8bc4d5c30d7a3aac6b8961fc205f55aaa39997b4ec07700 |
| R771-basis-power-3.json.gz | 1433690 | affc37995a1d990180d6287019319a6cff434cc7ad74886d6602760d59f0fd86 |
| R771-basis-power-4.json.gz | 2000625 | 20830fd931e1bfaf1b9f38e17ba8fe12625ccc3f9e20d1ad25fc2f385be3ff1e |
| R771-basis-power-5.json.gz | 2567421 | 3516d46279eef75a5c6464a88e8e46d5b06c046907cc8052af693547b67d95fb |
| R771-basis-power-6.json.gz | 3134106 | 8fbde1f9cb95b4b34df475812a75c7a4d5d9ee82a46c9a04c8cd7f5eb90007a8 |
| R771-basis-M6-complete.json.gz | 1437408 | 3cc9022b6ff07f5bc1cb57a9ddd5190673e3ad527958ca2439b317f5517b981e |
| R771-basis-M12-complete.json.gz | 3145068 | 2fb6e1937b4475fd13b1ca3e9900d8b56d7e7cab61fa673d3778ba0297348fea |
| R771-original-E4-E6-eta12-and-RR-denominators.json.gz | 1232 | 64c2a08a4a198391cd29ba927611047286a8a1e392aaf1699ba96567c3b07165 |
| R771-original-level82-Eisenstein-label-group.json.gz | 9673 | 3f394ae69f2b7f40940cd76b9847502964402181c0003bef6f2967f86eb9d2fc |

The core receipt hash is

8764e1f46e92ff256d01b0601fe6997e2f12849f5af3d37f202e6abb72256d8e,

the run receipt hash is

c1a5e55cfe6ad8c6d65119e88fa5c205cd6d3226b9e6e84c15b6765ef5d2a1d5,

and the retained-input receipt hash is

7d4031f5416dc4ffbc35f0734f4addb751f6e9f1ded07ae898aff3d8f3153f08.

The public input receipt, hash

e46a4ef36c4a6576a7a4392fbe0aa0bf0c5ab2a5d6d8dc7efa14740cf5187bc6,

binds the source commit, run, exact core/method/request/workflow, both README hashes, unchanged publication helper, and both retained input certificates. The final certificate explicitly marks the rational map, \(\beta\), and height as not yet computed.

## 6. Immediate continuation

R774 can now consume the actual weight-six basis and its 694-dimensional nonzero minor while forming the exact original \(H^3\). It reuses the R748 newform coefficients already available through 4096 and only extends the needed six original Fourier combinations and their symmetric cubic products.

In parallel the determinant-semilinear construction of R772 will produce actual \(K\)-defined recipes, using these completed Eisenstein blocks and original seeds directly. After descent, the true \(L\)-linear recovery of the original \(y\), the unchanged differential reconstruction of \(x\), evaluations at \(c_0,c_1\), and the genuine height inputs remain required. Neither a successful basis computation nor an Abel non-return statement proves the all-prime rational-point exclusion.
