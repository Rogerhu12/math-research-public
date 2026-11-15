# Actual complete root-value subtraction for the first Airy correction

**Status: actual public computation succeeded. All nine mathematical gates passed. The three smallest radii admit the new path bounds; the three larger cases retain their original complete bounds with the failed new path gates explicitly recorded.**

This is the actual consumption of the [root-value subtraction](R133-supplement-exact-root-value-subtraction-and-real-radial-first-Airy-amplitude-bounds.md) and [complete divided-forcing and ordered-derivative contract](R133-supplement-complete-divided-forcing-and-root-subtracted-Airy-derivatives.md). It continues the [original exterior derivative computation](R133-supplement-actual-strict-exterior-first-Airy-derivatives-and-local-sources.md). All statements concern the same repaired explicit family at fixed original $\eta_0$ and real $|\delta|\le10^{-8}$.

The correction, physical seams, full old Fourier output and independent mean equation are unchanged. This result does not give the full negative-boundary inverse, unknown high-input feedback, the nonlinear PDE branch, or the required numerical strong-return cutoff.

## A.1. Actual execution and exact identity

The public run is [43663147595, attempt 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43663147595). Its workflow event commit is
cd3ecd55989ebb163bab44519460b6f7fdd73243.
The actual immutable scientific checkout is
01c2202dc9f004b2f3a0649b766ab425c376eb8c.
The mathematical child returned zero, all nine gates passed, and the mathematical process took 135.032589411 seconds. The workflow completed successfully on 2026-11-15 at 01:30:46 UTC.

The exact mathematical source is
`scripts/fourfold_codazzi_root_subtracted_first_Airy_sources.py`,
50,796 bytes, SHA256
3e3bd6b66a90c1244c9b97f0e07d6cd5e15845780f80c87aee8912a41008f139.
The input manifest is
`notes/2026-11-15-R133-root-subtracted-first-Airy-sources-CI-inputs.json`,
17,055 bytes, SHA256
5158bc631e1cbf3eddea6b6ad1a2e28ac2e782eea1f94da5970f1ac7c3e1c426.
It pins 25 repository inputs and nine original artifact files. The latter are the completed large-root native, the original Taylor index and all seven original normalized-forcing stage files.

All following paths are relative to
`notes/root_subtracted_first_Airy_sources_ci/run-43663147595-1/`.

| Actual file | Bytes | SHA256 |
|---|---:|---|
| `consumers/root-subtracted-first-Airy-sources.json.gz` | 13,655 | d61f42392f65463282585dfb59fae26ec25549b064bd8ef7d551c2a202d4637b |
| `consumers/process.json` | 37,657 | ef0e7f24b7de5e343865d837ac0832fdc0a768cb85749064253978b480ba8bcd |
| `worker-process.json` | 5,371 | ccbae595b287021ae728793944a4d33ef839cb294ad0934a28caa523f4fa9e1d |
| `consumers/root/complete-root-forcing-norms-and-tail.json.gz` | 4,200 | 729796ab696e8ee9d0d456be75d3aacb29fae00e2e5f5f7181223e3b8d46b2e3 |

The exact runtime is Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5, SciPy 1.17.0 and Arb precision 320 bits.

## A.2. Reused mathematics and new work

The exact accepted normalized forcing coefficients of degrees zero through six are read from the original run 43653825736. Their complete non-circular Laurent arrays are unchanged; no FFT or finite coefficient is rebuilt. The 1,328 original coefficient rows, 4,359 radius-specific exterior rows, complete local profiles and radial weights are also reused. The original 1,079 physical seams remain in force.

The new work comprises:

- Seven complete weighted Fourier norm rows for the already saved normalized forcing coefficients.
- One whole-product forcing tail and root-mean separation.
- Six new radius/path profiles.
- 653 new scalar normalizations of existing physical forcing-jump records. This count includes the same physical seam when it belongs to more than one nested radius case.
- 1,036 new outward divided-forcing, ordered-derivative and local-source rows.
- 3,323 original exterior rows explicitly retained as fallbacks because the new full path conditions for their radii did not pass.

No original target, FFT, intrinsic, Taylor coefficient, cubic, derivative, profile or seam stage was recomputed. Each new accepted root norm, seam normalization and outward cell has a saved natural prefix.

## A.3. The actual full root function, including its mean

The exact root value is
$$
 b_*(X)=f_{b,0}(X),
$$
with full Fourier support $-384\le j\le384$ in the multiplier convention $e^{4ijX}$. The weighted norm width is $23/1024$. Its stored complex-parameter mean enclosure is
$$
 \langle b_*\rangle
 \in[-243.61488\pm7.51\cdot10^{-6}]
   +i[-8.63\cdot10^{-7},8.63\cdot10^{-7}].
\tag{A.1}
$$
The precise full mean ball is retained in the native. Outward bounds are
$$
 |\langle b_*\rangle|<243.614888,\qquad
 \|b_*-\langle b_*\rangle\|_{A_{23/1024}}<1.036504,
$$
$$
 \|b_*\|_{A_{23/1024}}<244.651376.
\tag{A.2}
$$
For angular derivative orders one through four, respectively,
$$
 \|\partial_X^q b_*\|_{A_{23/1024}}
 <
 (4.756621,\ 24.717593,\ 155.965986,\ 1254.250362)_q.
\tag{A.3}
$$
The separation is used only when differentiating $b_*(X)$ and estimating its nonconstant part. The full mean still multiplies the true derivatives of $M_0$ during reconstruction. In particular A.1 is a correction-amplitude mean, and is not the return-phase coefficient $\beta$.

The original auxiliary product supplies the normalized forcing suprema
$$
 \|f_b\|<1449.591406,\qquad \|f_a\|<2.269413
\tag{A.4}
$$
on the declared auxiliary circle $|\rho|\le1/3000$, $|\operatorname{Im}\phi|\le3/128$. This auxiliary object is identified with the physical family only inside the original physical root piece.

On the complete inner cover of radius
$90000009/10^{13}$, including the full true-root bracket width, the new finite-prefix-plus-tail bounds give
$$
\begin{array}{c|rrrr}
 &f&f_\phi&f_\rho&f_{\rho\phi}\\ \hline
 f_b&245.548641&4.767735&99941.775968&1246.816829\\
 f_a&0.319555&2.686700&71.099766&437.247689
\end{array}
\tag{A.5}
$$
as strict upper bounds on the declared inner strip $23/1024$. The tail is complete after degree six. No numerical fit or missing higher coefficient is substituted for that tail.

## A.4. Actual path gates and genuine forcing jumps

The fixed-$X$ lift is checked independently of both ray families. The nested widths are
$$
 \frac1{64}<\frac5{256}<\frac{11}{512}<\frac{23}{1024}<\frac3{128}.
\tag{A.6}
$$
The negative-side imaginary-width improvement uses only real allowed $\delta$. Its drift derivative comes from the original complete complex $1/16$ strip. The positive side retains the complete original optical displacement.

| Radius $R$ | Fixed-$X$ lift | Root composition | Negative real-parameter ray | Positive full optical ray | New derivative rows | Original fallback rows |
|---|---|---|---|---|---:|---:|
| $1/1000$ | passed | passed | passed | passed | 141 | 0 |
| $1/500$ | passed | passed | passed | passed | 271 | 0 |
| $1/200$ | passed | passed | passed | passed | 624 | 0 |
| $1/100$ | failed | passed | passed | failed | 0 | 895 |
| $3/200$ | failed | passed | passed | failed | 0 | 1,103 |
| $1/50$ | failed | passed | passed | failed | 0 | 1,325 |

Thus the new estimate is actually valid on both sides through radius $1/200$. At the three larger radii the original completed result remains valid; the new method is not extended outside its paid path domain.

For the three new cases the negative/positive counts of included physical forcing jumps are, respectively,
$(24,23)$, $(87,59)$ and $(256,204)$.
Each outward cell starts with the paid inner contribution, adds the original cell-length forcing integral and every crossed original jump, then divides by the actual positive lower bound for $|T|$. The exact root bracket is used, not its midpoint. A shared endpoint jump is recorded once per outward traversal.

The source term $N(g_a,TL_b)$ is evaluated in its exact cancelled form before any absolute estimate. Its first derivatives retain both normalized forcing derivatives and the full $b_*'(X)$ and $b_*''(X)$ contributions. The ordered matrices are not commuted.

## A.5. Actual complete local-source bounds

The new amplitude and derivative tables retain both strip-supremum and Wiener bounds. The true first-row local source is
$$
 JP\,S\bigl(\mu L_0w_1\bigr).
\tag{A.7}
$$
The numerator is unnormalized. No extra factor $1/n$ is inserted, and no division by $\mu$ is used in place of the true source. The local numerator is paid on the same old-angle width $1/128$ as its accepted phase/profile consumer. All Fourier outputs, including output mean, are included.

The following are strict outward upper bounds for its complete exterior ordinary radial $L^2H^{-2/3}$ source norm:

| Radius $R$ | Negative local source | Positive local source | Negative local component after the previously paid Cauchy/primitive gain |
|---|---:|---:|---:|
| $1/1000$ | $4.337713\cdot10^{20}$ | $1.150755\cdot10^{22}$ | $6.574738\cdot10^{19}$ |
| $1/500$ | $5.654995\cdot10^{20}$ | $1.416320\cdot10^{22}$ | $1.445234\cdot10^{20}$ |
| $1/200$ | $7.954848\cdot10^{20}$ | $1.952455\cdot10^{22}$ | $6.340808\cdot10^{20}$ |
| $1/100$ | $1.425015\cdot10^{22}$ | $3.121238\cdot10^{22}$ | $7.462789\cdot10^{22}$ |
| $3/200$ | $2.515435\cdot10^{22}$ | $5.350317\cdot10^{22}$ | $9.068217\cdot10^{23}$ |
| $1/50$ | $4.000637\cdot10^{22}$ | $8.318498\cdot10^{22}$ | $8.835020\cdot10^{24}$ |

The last three rows reproduce the accepted original source bounds after the labelled path fallback. They are not new successful path certificates. The first three negative local bounds improve their former bounds, but remain far too coarse to close the required numerical strong-return estimate. Large upper bounds do not prove large actual errors.

The last column is only the linear local-source component with other sources zero. It is not a bound for the whole corrected trial, its seams, its positive affine ports, or an unknown full high-frequency solution.

The already proved old-circle nonlocal and independent-mean bounds for this same correction remain available. This run does not yet consume the new smaller derivative tables through those complete words. Such a subsequent consumer must preserve their full projections, output means and separate source windows.

## A.6. Original natural files and publication

The six complete case files are under `consumers/cases/`.

| File | Bytes | SHA256 |
|---|---:|---|
| `radius-1-1000.json.gz` | 328,968 | 32db8dce1222884b050b8e3a183dc7167b2c062832772cb38ec6bddfd632468a |
| `radius-1-500.json.gz` | 650,459 | f37d0aceabf3e5a4497bb13445f30ee4560e10204c856ad26958de28dbed68c5 |
| `radius-1-200.json.gz` | 1,524,368 | 1db02267999091cd73dd9aaca6a1224b952718c0eb58667bcc6ee96fe1ddde56 |
| `radius-1-100.json.gz` | 651,034 | 27e11008fa0150ecf4168cfd8b9cfe3aaab146e9435f3c041c7aab73682ec150 |
| `radius-3-200.json.gz` | 799,763 | 16d40ccde898d35683da079323abb97015ea40a63ebdcd1268e3bee224ec262a |
| `radius-1-50.json.gz` | 956,923 | 8a307a536a1eb8cf98a13e395dc0eeb6949ec70f5d587f44032a54250d82010d |

The complete unabridged process is 100,236 bytes, SHA256
c89ba87ca47a7e86b6e0a6b145c614bba93f8bc66d66b88e6497eeeb376816cf,
at `consumers/complete-process-before-summary-size-limit.json`. It remains in the public result and original artifact. It was not read through the small-text connector. The 37,657-byte readable process removes repeated input pins and derivative tables only; the actual gates, root norms, all radius outcomes and natural-file receipts remain.

The worker records true pulls at:

- 01:27:43.204722 UTC, to 01c2202dc9f004b2f3a0649b766ab425c376eb8c.
- 01:30:37.116572 UTC, to bf3daff6b23c9b4d184606cbb4c1977cd00d2b22.
- 01:30:38.733296 UTC, to c71bad67c9ddc24642f3f5446d5a0ddbb67d7a73 during the concurrent-publication retry.

Both README diffs are empty in each recorded pull. Publication succeeded after the retained non-fast-forward retry. The original artifact is
`visible-exact-root-subtracted-first-Airy-sources-43663147595-1`.
No saved mathematical file was truncated or artificially split.
