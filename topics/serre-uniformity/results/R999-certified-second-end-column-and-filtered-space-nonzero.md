# R999 — Certified second end column and a larger nonzero filtered family

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b.

**Status: complete exact public computation and proved family statement.** For every original allowed prime $p\ge41$, the actual second end column $Z_{p-13,7}$ is a nonzero modular form and its original Legendre factor is a unit. Consequently

$$
11\nmid p+1\quad\Longrightarrow\quad V_p\ne0.
\tag{999.1}
$$

Combining this with the different end column already proved in R996 gives

$$
\boxed{55\nmid p+1\quad\Longrightarrow\quad V_p\ne0.}
\tag{999.2}
$$

Here $V_p$ is exactly R992's original primitive/Legendre-filtered span of R968's critical columns. This is a statement about the nonzero global span. It does not say that its CM marked functional is nonzero or that it is stable under $\mathcal G$. Those are separate outstanding conditions. The remaining nonzero-space branch is $55\mid p+1$; the main Serre goal remains open.

## 1. Unchanged source, label and exact constants

Throughout,

$$
p=6N+5\ge41,\qquad p\bmod9\in\{2,5\}.
$$

Take the original indices

$$
i=N-2,\quad j=1,\quad
a=6i+4=p-13,\quad b=6j+1=7,\quad h=6i+7=p-10.
\tag{999.3}
$$

The unchanged complete R968 formula, with all its Gaussian and zeta terms, reduces at this column to

$$
Z_{a,7}=6T_{a,9}+6\beta_3T_{a,3},\qquad [q^0]\beta_3=\frac1{30240}.
\tag{999.4}
$$

The other single-zeta terms and the double-zeta term vanish by their actual unit-orbit character. They were included in the public evaluation before being found zero. In particular the original $a\equiv4\pmod6$ is kept separately from its residue $a=-13\pmod p$; the integer representative $-13$ cannot be used to redefine that character.

The actual public exact output is

$$
\boxed{(p-13)![q^0]Z_{p-13,7}
=\frac{319435001}{40320}\pmod p.}
\tag{999.5}
$$

It agrees between the complete R968 falling-factorial sum and the independent integer ODE of R998. For the latter,

$$
S_7(v)=e^v(1-v/2)^{-13},\qquad
(2-v)S_7'=(15-v)S_7,
$$
$$
K_l=2^ll![v^l]S_7,\qquad
K_{l+1}=(l+15)K_l-2lK_{l-1},
$$

and the two required coefficients returned were

$$
[v^3]S_7=\frac{1993}{24},\qquad
[v^9]S_7=\frac{13690043}{10368}.
$$

Their prescribed combination $6[v^9]S_7+[v^3]S_7/5040$ is exactly (999.5). No modular prime window or old $j=0$ computation was performed.

The original Legendre factor for precisely the same $h$ is

$$
\boxed{P_{h-1}(1/s)=P_{p-11}(1/s)=P_{10}(1/s)
=-\frac{8953}{243},\qquad s^2=-3.}
\tag{999.6}
$$

The complete degree-ten polynomial recurrence and an independent factorial finite sum agreed as exact rational numbers. The reflection uses the same original Legendre convention as R996; it is not a neighboring label.

## 2. Complete factorization and actual exception sets

All four fixed positive integers were completely factored in the public job. The results are

| Integer | Complete factorization |
|---|---|
| $319435001$ | $11863\cdot26927$ |
| $40320$ | $2^7\cdot3^2\cdot5\cdot7$ |
| $8953$ | $7\cdot1279$ |
| $243$ | $3^5$ |

Every distinct factor was independently prime-certified by complete trial division, after the factorization itself. There is no probable-prime or unexamined-cofactor assumption. For the only factors at least 41, the returned certificates and congruences are:

| Certified prime | Floor square root | Divisors checked | Total checks | Mod 6 | Mod 9 |
|---|---:|---|---:|---:|---:|
| 1279 | 35 | 2 and every odd integer 3 through 35 | 18 | 1 | 1 |
| 11863 | 108 | 2 and every odd integer 3 through 107 | 54 | 1 | 1 |
| 26927 | 164 | 2 and every odd integer 3 through 163 | 82 | 5 | 8 |

All tested remainders were nonzero. The exact square-root certificates were $1225\le1279<1296$, $11664\le11863<11881$, and $26896\le26927<27225$. The small factors 2, 3, 5 and 7 were also separately certified by the same full-bound routine.

Thus neither prime divisor of the cusp numerator is an original allowed prime: 11863 fails $p\equiv5\pmod6$, while 26927 fails $p\bmod9\in\{2,5\}$. The only Legendre numerator factor above the original lower bound, 1279, also fails the mod-six condition. All denominator factors are below 41. Therefore both (999.5) and (999.6) are units for **every** original allowed prime $p\ge41$.

The consumer printed, and the receipt retained, four actual empty bad-factor lists:

- allowed original prime divisors of the cusp numerator;
- such divisors in the requested $5\mid p+1$, $11\nmid p+1$ branch;
- allowed denominator primes;
- allowed Legendre numerator primes.

Emptiness was an outcome of the complete fixed factorization; it was not imposed as an input assumption. In fact the output proves the wider assertion (999.1), without requiring $5\mid p+1$.

For reproducibility without retaining the remainder arrays, the full ordered `divisor:remainder` streams, with one LF after each pair, have these SHA256 values:

| Prime | Full trial-stream SHA256 |
|---|---|
| 1279 | `b17e19f5b014d3abec3be3bef7443e6f1803e3cb5cb25a0b7360212c8174f1f5` |
| 11863 | `f69d541dd99ef379ed5baa2324f852882c1fa4abe2494ac7cc9de790e80c59cb` |
| 26927 | `984eaa1da7c4f9e64ca9c1d204dd811e28225294343b83bd36491c22b0c952b8` |

The frozen consumer and the stated full divisor ranges determine those streams. No raw stream is committed.

## 3. Deduction for the original filtered space

Because $a=p-13<p$, its factorial is a $p$-unit. Equation (999.5) therefore gives a nonzero cusp coefficient of the actual form $Z_{p-13,7}$, so that form is nonzero in $M_{p-5}(\mathbf F_p)$.

For the same original label, the primitive condition is exactly

$$
\gcd(h,p+1)=\gcd(p-10,p+1)=\gcd(11,p+1)=1
\quad\Longleftrightarrow\quad11\nmid p+1.
\tag{999.7}
$$

The other mask factor is the unit (999.6). Thus whenever $11\nmid p+1$, the retained span contains this nonzero actual column with a nonzero mask multiplier. This proves (999.1). When $11\mid p+1$, this particular column is deleted by the primitive mask; its nonzero cusp value cannot restore it.

R996 independently proved $V_p\ne0$ for $5\nmid p+1$, using the different column $Z_{p-7,1}$ and the original label $h=p-4$. The union of these two proved sufficient conditions is exactly $55\nmid p+1$, giving (999.2). No assumption has been made about the number of other surviving labels, full span, or the value of either column at the CM point.

This also identifies precisely what is left in the R992 criterion. In the family (999.2), its nonzero-space hypothesis is now proved. Its $\mathcal G(V_p)\subseteq V_p$ hypothesis is not proved. For $55\mid p+1$, the nonzero-space hypothesis still needs a different argument as well. The statement $V_p\ne0$ alone does not imply that the original same-label CM product $P_{h-1}(1/s)f_i g_j$ is nonzero.

## 4. Public execution and complete acceptance receipt

The only mathematical execution was the public GitHub Actions task:

- Repository: `Rogerhu12/math-research-public`.
- [Run 44764524952](https://github.com/Rogerhu12/math-research-public/actions/runs/44764524952).
- Job `136385485790`, `exact_research`; every job step succeeded.
- Source commit: `84a8cad4b15bff20f8e86ee49a5f8e2816e9eae6`.
- Run created: `2026-11-20T15:33:52Z`; successful final update: `2026-11-20T15:34:09Z`.
- Invocation: `python topics/serre-uniformity/scripts/original_second_end_column_cusp_consumer.py --seconds 30 --output /tmp/serre-second-end-column-cusp.json`.
- Wrapper record: `END_COMPUTATION` for `original-second-end-column-cusp`, exit code zero.
- Consumer elapsed time: `0.013812899999997796` seconds; final `within_total_budget=true`.

The deterministic, compact, sorted-key ASCII JSON payload including its final newline is **10156 bytes**, SHA256

```text
6d208b8d83cc8e2efc612e43f4d8f21084a45916384106636dcb1a77a557b7aa
```

The fetched job-log UTF-8 bytes are **29770 bytes**, SHA256

```text
bc57f1854f78320ace416df4054294c768644394854badf233ef2dbc0009ef8e
```

The root receipt check was local file I/O, schema comparison and hashing only. It reconstructed the payload from the actual log and checked:

- the run source commit, exact submitted request, wrapper exit zero, and successful job;
- equality of the standalone contract and the payload contract;
- equality of every pinned source hash with the actual source file bytes;
- equality of the complete R968, reduced two-term and independent ODE rational values;
- agreement of both Legendre routes with the reported exact result;
- complete factor-reconstruction flags, exact coverage of distinct factors by the primality certificates, and all full-trial flags;
- exact coverage of the same factors by the residue classifications and all four actual empty bad lists;
- the payload byte count and canonical SHA256, plus the final successful timing receipt.

No mathematical coefficient, factorization or primality test was rerun locally. The complete report and fetched log are disposable scratch; no raw array, certificate stream, artifact or Release was added to the repository. This request is complete and must not be retriggered merely to recover these already registered conclusions.

## 5. Frozen execution inputs

| Input | SHA256 |
|---|---|
| R998 method | `ec9edd293d1a44fd35f4f70a89bfce6d62fcc0e02e639d4ecb839ff8f2eb67ca` |
| Second end-column consumer | `b4a76a3dd37088c7dab1f8083723b0d51f123f566b3d485226070a82a524062b` |
| R968 complete source | `186efc0cb109befcce458f931779802027d30193cfec687131f8fda5e10ccaaa` |
| R996 finite cusp source | `ee4e728d30dd08f9a40c3de54fc8660574c9ee8d04c4383f77a420d7076b7c1d` |
| Submitted request JSON | `2e5b3f7f1ad5235e396f1df8373dff0e30b9fe98e8c950eb5e483a421d40bd17` |
| Public workflow | `8394c469b41e4b79b78b1a6c49a15bb742e4c28f9e45e5c2aa13aa7f9b105094` |

R998's complete method and code had independent root/audit review before submission. The inference from the returned constants to (999.1)–(999.2), including the original indices, factorial normalization, Legendre reflection and primitive mask, was independently checked on paper by root and legendre_shift. The executed factorization supplies the new exact arithmetic input, rather than an unverified local numerical assertion.

## Dependencies

- [R968](R968-full-level-mixed-CM-jet-and-critical-factor.md): actual original columns and the complete source formula.
- [R992](R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md): the original filtered space and the separate sufficient stability criterion.
- [R996](R996-original-end-column-cusp-unit-and-filtered-space-nonzero.md): the complete finite cusp reduction and the previously proved $5\nmid p+1$ family, consumed without recomputation.
- [R998 method](../notes/R998-original-second-end-column-execution-method.md) and [frozen consumer](../scripts/original_second_end_column_cusp_consumer.py): both exact channels, full factorization and acceptance contract.

The actual same-label marked nonvanishing, original filtered stability, the complete high trace in every allowed prime, and the global Serre uniformity conclusion remain open.
