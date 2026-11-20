# R969: certified original filtered full-level span at three primes

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

**Status: completed finite public computation.** At each of \(p=113,131,227\), the actual R968 coefficient forms, after the complete original primitive and Legendre filters, span the entire full-level space \(M_{p-5}(\mathbf F_p)\). In particular their span contains the actual Hasse quotient \(A/E_4\). Exact combinations were checked on all Sturm coordinates and two additional Fourier coefficients.

This proves the stated spanning result at these three primes. It is not a uniform spanning theorem. The calculation uses a new full-level Fourier source; it does not recompute any sigma sequence, supersingular trace, old central values or prime window.

## 1. Exact objects and implication

Write \(p=6N+5\), \(i+j=N-1\), and use the unchanged R968 forms and weights
\[
Z_i=Z_{6i+4,\,6j+1}\in M_{p-5}(\mathbf F_p),\qquad
w_i=\mathbf1_{(6i+7,p+1)=1}P_{6i+6}(1/s),\qquad s^2=-3.
\]
The tested columns are exactly \(w_iZ_i\). Zero Legendre values and nonprimitive labels are discarded only because their actual weight \(w_i\) is zero. Neither original filter is enlarged.

At each of the three primes the result is
\[
\boxed{\operatorname{span}_{\mathbf F_p}\{w_iZ_i:0\le i<N\}
       =M_{p-5}(\mathbf F_p).}
\tag{969.1}
\]
Here \(A\) is the Tate-normalized Hasse invariant. Its weight is \(p-1\), its Fourier expansion is one, and its zero at the fine \(j=0\) point is simple. The form \(E_4\) has the same simple zero there. Thus \(A/E_4\) is a holomorphic weight-\(p-5\) form whose value at that point is nonzero. Its actual Fourier series is \(1/E_4\), the target used in the computation.

Equation (969.1) therefore gives an exact combination
\[
\sum_i c_iw_iZ_i=A/E_4.
\tag{969.2}
\]
By R968's calibrated marked-value identity,
\[
[Z_i/E_6^N]_{\rm mark}=-72(-864)^{-N}f_i g_j.
\]
Since the right side of (969.2) has a nonzero marked value, at least one of the fully filtered original same-label products is nonzero at each named prime. This finite corollary uses the whole coefficient space and does not require the central label to be nonzero. In particular it respects R945's central zero at \(p=227\).

The prime \(113\equiv5\pmod{12}\) belongs to the general same-label full-level range, with \(p\bmod9\in\{2,5\}\). It is not presented as an \(r=2\), \(p\equiv11\pmod{12}\) trace experiment.

## 2. Frozen public execution

- Run: [44736934491](https://github.com/Rogerhu12/math-research-public/actions/runs/44736934491), conclusion **success**.
- Job: [136290572303](https://github.com/Rogerhu12/math-research-public/actions/runs/44736934491/job/136290572303), all steps successful.
- Source commit: `48359d18d5ea7aa116e6be60cac425759a829cf0`.
- Consumer: [full_level_critical_hasse_span_three_prime_consumer.py](../scripts/full_level_critical_hasse_span_three_prime_consumer.py), SHA256 `5bb625faec68b4276677213e948456df188af75c94f1fab9121946088790445a`.
- Exact method: [R969 execution contract](../notes/R969-original-full-level-filtered-Hasse-span-execution-method.md), SHA256 `165ba7f55a1b8f763efe1c340f4449733fb37db4073ad791e6a5a9f661f6a890`.
- Requested mathematical runtime: Python standard library, 240-second internal budget, public repository Actions only.

All three primes completed in approximately **1.353600 seconds**, with no error or uncompleted tail. The workflow checked both README hashes and the frozen script hash before execution.

## 3. Source and exact finite results

The consumer enumerates each required primary CM generator \(\beta=a+b\zeta\equiv1\bmod2s\) once, with its exact norm cutoff. It checks the complete conjugation pairing and the original normalized norm-one coefficient. One batch supplies all pure Taylor boundaries, including the inverse finite-character family. The exact mixed heat equation of R968 fills the needed coefficients; the displayed zeta formula R968(968.9) then gives the actual \(Z_i\).

All arithmetic takes place over \(\mathbf F_p\), with rational Bernoulli coefficients reduced only after their denominators are checked to be units. The weighted series \(B_{2n}E_{2n}\) is retained as a whole. No Bernoulli numerator is inverted.

For \(B=\lfloor(p-5)/12\rfloor\), the full-level basis is
\[
E_6^{N-2r}\Delta^r,\qquad 0\le r\le B.
\]
Its leading coefficients at \(q^r\) are one. The calculation retains every row \(q^0,\ldots,q^B\), and reduces every original source column and the target against this basis through \(q^{B+2}\). Exact Gaussian elimination uses all Sturm rows and checks the successful combination again on both extra rows.

| \(p\) | \(N\) | weight \(p-5\) | space dimension | retained filtered columns | exact filtered rank | Sturm bound \(B\) | checked through |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 113 | 18 | 108 | 10 | 16 | 10 | 9 | \(q^{11}\) |
| 131 | 21 | 126 | 11 | 19 | 11 | 10 | \(q^{12}\) |
| 227 | 37 | 222 | 19 | 35 | 19 | 18 | \(q^{20}\) |

The target belongs to the filtered span in every row. The separately labelled unfiltered diagnostic also has full rank, but is not used in place of the filtered result. Sturm's theorem applies because R968 proves the actual source modularity and integrality, and \(A/E_4\) is the actual modular target.

At \(p=227\), the new Fourier source was independently tied to two previously registered R945 scalars:

| original \((i,j,h)\) | consumed \(f_i g_j\) | new \([Z_i/E_6^{37}]_{\rm mark}\) | original scale |
|---|---:|---:|---:|
| \((18,18,115)\) | 0 | 0 | 4 |
| \((24,12,151)\) | 16 | 64 | 4 |

The consumed values come from R945 run44720732478, output SHA256 `217d9ff8f89c3270b8af2d0226fabb70662bff5874c526302933feaa66e08aad`. Both agree with \(-72(-864)^{-37}\) in the original field. The old sigma calculation was not called.

## 4. Evidence integrity

The complete deterministic report has **21,986 bytes** and SHA256
`7c3e1e2569996a2d3389be06b02e66c7aa55503f97facdff581c024a42dcfc64`.
The root session read the actual job logs, reconstructed that report by pure JSON/text IO, and verified both its exact byte count and hash. No mathematical consumer was run locally.

| \(p\) | actual full source-row SHA256 | actual weighted-matrix SHA256 |
|---:|---|---|
| 113 | `1ce8f71bed2d6b7ea8804c47ee9a46d2b3875cd68b1b4aa5d0bcf32095062201` | `df12f948622cf0009a253467a53b7f5f3a89a0c265c0cc6068cfe6f33de9df8b` |
| 131 | `d61357e32926a720bf72026d5e78c4b64402300866fd8e29d62a1f2183569f55` | `8b615f77ef4ddb5f6b950cb477874071769b85d4ff390d1f7f9d4c4c41203120` |
| 227 | `aa4aa471dea6f67c7914bcf872167266de0cb8185f2d03af589989920c2bb5d0` | `8b9e8f7eaf4ffbb956bd045a36ce72b665f17e0de484db33aee640fdce522c66` |

The public output includes the complete masks, target coordinates and successful sparse combinations. Regenerable matrices, raw logs, reports and certificates are not committed or uploaded as artifacts. The frozen source and the actual run bind those witnesses without changing the repository's storage rule.

The new remaining question is whether suitable actual filtered minors, or a direct identity placing \(A/E_4\) in the filtered span, can be controlled for all required primes. The three full-rank results do not prove that assertion and do not close the original height or Serre-uniformity goal.
