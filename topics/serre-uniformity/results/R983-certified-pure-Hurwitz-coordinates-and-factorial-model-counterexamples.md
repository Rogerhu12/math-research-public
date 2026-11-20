# R983 — Certified original pure Hurwitz coordinates and counterexamples to the factorial comparison model

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

**Status: completed public exact computation, independently audited source and output.** The four original pure Hurwitz coordinates are now computed at $p=41,47,227,857$. Every proved source identity passes. The explicitly unproved common-scalar comparison with the proposed index factorial fails already at both small calibration primes. This is a counterexample to that precise comparison model, not to Serre uniformity or to the original nonvanishing goal.

## 1. Public source and execution

- Source commit: `0c4cef11e3825245b8e3edf13f38a6f5fe1749f0`.
- Public [run 44748379140](https://github.com/Rogerhu12/math-research-public/actions/runs/44748379140), job `136329516699`, status **success**.
- Workflow: `.github/workflows/serre-current-exact-research.yml`; public repository only, no uploaded artifacts.
- Consumer: [original_pure_hurwitz_four_prime_consumer.py](../scripts/original_pure_hurwitz_four_prime_consumer.py), 17985 bytes, SHA256 `cb311d2d8544512f96999b63665b411d1ed9ebb0b8bc70435026422fc6fc6bc7`.
- Proved method: [R981](R981-original-pure-Hurwitz-residue-compression.md), 16198 bytes, SHA256 `bec9763d31321b217f6afaeb46349edcd061f3a87dbc462b44f35cd1867d013f`.
- Request SHA256: `7ec76c822f36633273c1e035d536582a3646cb0cb31d144b7bffd54d4936014f`; arguments `--budget-seconds 620`; Python with `python-flint==0.9.0`.
- Actual elapsed worker time: **3.5528688570000213 seconds**. Requested and completed primes are exactly `[41,47,227,857]`; the uncompleted list is empty.

The workflow checked the root and topic README hashes and the consumer hash before execution. Root read the full method and script, checked the independent formulas, corrected the sparse-checkout method-file path before publication, and later read the completed job output. Local work was limited to paper reasoning, file I/O, syntax parsing, and byte/hash verification. No mathematical part was executed locally.

## 2. Source normalization and observed coordinates

The curve, invariant differential, and Hurwitz convention are fixed throughout:
$$
E_+:y^2=x^3+1,\qquad \omega=dx/(2y),\qquad(g_2,g_3)=(0,-4),
$$
$$
\log(\sigma_+(z)/z)=-\sum_{N\ge4}\frac{\mathcal G_N}{N}z^N.
\tag{983.1}
$$
There is no factorial hidden in $\mathcal G_N$. Let $r=2$ or $8$ according to the original branch, $a=r+1$, $n=p-r$, and
$$
N_0=a(p-1),\quad N_0^*=N_0+p+1,
\quad N_1=n(p-1),\quad N_1^*=N_1+p+1.
\tag{983.2}
$$
The observed residues are:

| $p$ | $r$ | $\mathcal G_{N_0}$ | $\mathcal G_{N_0^*}$ | $\mathcal G_{N_1}$ | $\mathcal G_{N_1^*}$ | $\mathscr B_p$ |
|---:|---:|---:|---:|---:|---:|---:|
| 41 | 8 | 9 | 30 | 15 | 36 | 32 |
| 47 | 2 | 18 | 13 | 40 | 35 | 26 |
| 227 | 2 | 132 | 158 | 191 | 44 | 105 |
| 857 | 8 | 625 | 36 | 708 | 855 | 131 |

Here $\mathscr B_p=E_{p+1}(E_+,\omega)$, in the exact Robert convention of [R980](R980-original-level-one-Hurwitz-reflection-and-distinct-mirror-pairs.md). All sixteen displayed pure residues are nonzero. Their exact indices are:

| $p$ | $N_0$ | $N_0^*$ | $N_1$ | $N_1^*$ |
|---:|---:|---:|---:|---:|
| 41 | 360 | 402 | 1320 | 1362 |
| 47 | 138 | 186 | 2070 | 2118 |
| 227 | 678 | 906 | 50850 | 51078 |
| 857 | 7704 | 8562 | 726744 | 727602 |

The new pure values are not assigned from the known original trace or from balanced coefficients. The already registered [R973](R973-certified-balanced-Kronecker-coefficients-at-four-primes.md) constants are consumed only for the source scale and the comparison probe:
$$
\mathscr B_p=12(-1)^{(p+1)/6}B_{\rm old},
\qquad c_n(E_+)=-c_n(E_-).
\tag{983.3}
$$
Neither the old balanced values nor any old supersingular trace or same-label sigma product is recomputed.

## 3. Independent checks that actually ran

Every required coefficient of the canonical elliptic logarithm was constructed twice: first from the R981 two-digit Lucas/Wilson formula with its unique denominator-$p$ resonance, and then from an independent recurrence tracking the exact $p$-valuation and unit part of $\binom{-1/2}{j}$. The two complete required input segments agree, including every resonant coefficient. The differential equation $6Xf'+f=C$ also holds coefficient by coefficient.

Each new pure value was then computed through the bounded-exponent residue contraction and independently through the positive exponent $q+1-N$. A further Lagrange-inversion computation agrees whenever $N-2$ is a unit. At the singular $r=2$ high index, that check records the forced zero numerator and does not divide it by $p$ or use it to assign $\mathcal G_N$.

At $41,47$, all required pure values, including the two added probes below, also agree with an independent exact rational Laurent recurrence for $\wp_+$. Their rational valuations are zero. The rational prefix ends at $j=353$; no large-prime rational prefix is constructed. The same small-prime rational source independently checks (983.3).

Finally, both sides of the exact Robert reflections
$$
\mathcal G_{t(p-1)+p+1}
=\frac{\mathscr B_p}{12t}\mathcal G_{t(p-1)}\pmod p,
\qquad t=a,n,
\tag{983.4}
$$
are computed separately, and both reflection checks pass at all four primes. The previously proved low-coordinate nonvanishing is also respected. No conjectural equality was included in the success condition.

## 4. The precise factorial model is false

For clarity, the proposed correction was
$$
C_u=\frac{u!(p-u)!}{(p-1)!}\equiv(-1)^{u+1}u\pmod p,
\qquad 1\le u\le p-1,
\quad\beta=\mathscr B_p/12.
\tag{983.5}
$$
Its adjacent ratios fit the theta symmetry and Robert constants considered in [R982](R982-theta-symmetry-obstruction-to-a-common-Frobenius-scalar.md), so those symmetries alone did not exclude it. The candidate would require one scalar $\xi$, independent of $j$, in
$$
H_{j-1,j+1}=\xi\beta^{j-1}C_{j-1}\mathcal G_{K_j},
\qquad
K_j=(p+1-j)(p-1)+p+1,
\tag{983.6}
$$
where $H_{j-1,j+1}=-(j-1)!c_j(E_+)$ is the exact original mixed coefficient. Equivalently, when the denominator is nonzero,
$$
\xi_j=\frac{(-1)^{j+1}(j-2)!c_j(E_+)\beta^{1-j}}
{\mathcal G_{K_j}}
\tag{983.7}
$$
would have to be independent of $j$.

The old universal recurrence gives $c_3(E_+)=1/6$ and $c_6(E_+)=-1/900$. Only the new pure indices $K_3,K_6$ are added at $41,47$, and they receive the same independent rational calibration. The observations are:

| $p$ | $K_3$ | $\mathcal G_{K_3}$ | $K_6$ | $\mathcal G_{K_6}$ | $\xi_3$ | $\xi_6$ | $\xi_n$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 41 | 1602 | 35 | 1482 | 4 | 4 | 1 | 22 |
| 47 | 2118 | 35 | 1980 | 16 | 26 | 43 | 25 |

At $47$, $K_3=N_1^*$ is a duplicate index and is computed only once. At $j=n$, $K_n=N_0^*$ at every prime, so that probe uses the new low-star pure value and the signed old balanced datum, without additional coefficient computation. At $227,857$, only this $j=n$ probe is present, yielding $\xi_n=93,693$; no cross-index conclusion is drawn at those two primes.

A denominator-free necessary equality for $\xi_3=\xi_6$ is
$$
25\beta^3\mathcal G_{K_6}=4\mathcal G_{K_3}\pmod p.
\tag{983.8}
$$
The executed diagnostic records:

| $p$ | Left side | Right side | Left minus right |
|---:|---:|---:|---:|
| 41 | 27 | 17 | 10 |
| 47 | 30 | 46 | 31 |

Both differences are nonzero. Thus (983.6) with a common scalar and precisely the correction (983.5) is false at both primes. A change from the convention $\beta$ to the natural Frobenius sign $-\beta$, together with the corresponding $(-1)^uC_u$, leaves the product and this diagnostic unchanged.

This refutes that exact model only. It does not rule out a true comparison involving the integral Frobenius remainder, a different index-dependent correction, a nontrivial coordinate transformation, or a statement about one isolated near-$p$ coefficient. In particular the equality of weights and compatibility with theta symmetry are insufficient to identify the mixed and pure values.

## 5. Reproducibility and output hashes

Canonical JSON is UTF-8 with sorted keys and separators `(',', ':')`. Root parsed the public stdout and independently reserialized and hashed it, without executing any mathematics:

| Object | Bytes | SHA256 |
|---|---:|---|
| Four full result rows | 14804 | `08698e1b211288b59702264d91fbe5feed1942ad854610a09b0d588960d5756e` |
| Exact-prefix metadata record | 229 | `1028f332df7643e922e5482486616ca7d996fce23c37e388ec071ce3a5f45040` |
| Final deterministic summary | 667 | `acc2d0c662223cbeadc5b15236bcf49e1c09e720487100d63f46732a86fa00b3` |

The actual rational-prefix array has SHA256 `1c39dafbbad82ec4cd531a1a0d2939117eca6039f670cd4bf46f45645b4c96f2`; the metadata-record hash is a different object and must not be substituted for it. Individual row hashes are:

| $p$ | Row bytes | SHA256 |
|---:|---:|---|
| 41 | 4682 | `730ca7ca658d0abbe5a11e15c2de35f49532986db802af6709880ddc7a87626e` |
| 47 | 4690 | `4aefd74fbba349d6a4b6a96db9b2e82b08b31112d5265243fb15b7d366eaa880` |
| 227 | 2702 | `ec1452e42092252b15a3a03379ded7809ce628ef92f1513861f7a2df157753fe` |
| 857 | 2725 | `e01cbbd2c1d2dfc267d8ca263a6c91ec0d058845795906718afccce74f63637f` |

All detailed rational-value and input-segment hashes remain in the public job output. No coefficient array, full rational prefix, or regenerable certificate is committed or attached to a Release.

## 6. Consequence for the active problem

The direct pure-coordinate formula of [R978](R978-original-Robert-coordinate-and-pure-Hurwitz-mirror.md) and the Robert reflection of R980 now have independent finite calibration at these four primes. The already known finite original nonvanishing consequences are not registered again as new trace calculations.

The next actual comparison must retain the Frobenius integral remainder and the original coordinate transport. The general high pure unit, the original same-label condition, the required global height statements, and the README completion criterion remain open. This request is complete and must not be rerun merely because the surrounding session or context changes.
