# R963 — A complete new finite window for the original r=2 Cartier moment

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b. Authoring agent: literature_frontier.

**Status: finite computation certified by a successful public GitHub Actions run.** For every prime
\[
1000<p\le100000,\qquad p\equiv11\pmod{12},\qquad p\equiv2\text{ or }5\pmod9,
\tag{963.1}
\]
the original moment of R958 and the original complete supersingular trace are nonzero. All 1,582 candidate primes were completed, from 1,019 through 99,923. Every required identity check passed. There was no zero, failure, or uncompleted tail.

This is a finite assertion. It neither proves nonvanishing for all primes nor completes the Serre-uniformity problem. The earlier R936/R939 primes at most 1,000 were excluded by the consumer and were not rerun. The statement concerns the original \(r=2\) row, with its original phase and normalization; it does not assert anything new for the \(r=8\) row or for the independent same-label \(Q'\) obstruction of R945.

## 1. Public run, frozen source, and reproducibility

The successful run is

- [GitHub Actions run 44731335315](https://github.com/Rogerhu12/math-research-public/actions/runs/44731335315).
- [Job 136271559447](https://github.com/Rogerhu12/math-research-public/actions/runs/44731335315/job/136271559447).
- Source commit: `efdeebbe23cf971f0d66d39e53964e99a9ccc67c`.
- [Consumer at that source commit](https://github.com/Rogerhu12/math-research-public/blob/efdeebbe23cf971f0d66d39e53964e99a9ccc67c/topics/serre-uniformity/scripts/r2_original_moment_new_window.py).
- Consumer SHA256: `a3af15c40c8206dc62b266febe2710d941a877529df270ec1c663cce57d00aa5`.
- Pinned and reported runtime: `python-flint==0.9.0`.

The actual invocation was

```sh
python topics/serre-uniformity/scripts/r2_original_moment_new_window.py \
  --minimum 1001 --maximum 100000 --budget-seconds 620
```

The consumer reported elapsed time **539.210186 seconds**, below the requested 620-second budget. Its start and summary records both identify the same frozen script. The log's consumer records run from `2026-11-20T11:54:13.7155473Z` to `2026-11-20T12:03:12.9229762Z`.

All new mathematical execution occurred in that public Actions job. Local work consisted of source inspection, AST/hash checks before dispatch, and reading/parsing/hashing the returned output. The root agent independently checked the complete row stream and its three reported hashes by pure I/O operations. This file stores only the small receipt and method, not the reproducible polynomial arrays or the full row stream.

## 2. Exact original objects computed

Write
\[
p=6N+5,\qquad s^2=-3,\qquad s^p=-s,\qquad
t=u^3,\quad D=1-4t.
\tag{963.2}
\]
All the primes in (963.1) have odd \(N\). The original degree-\(N\) Hasse polynomial \(H\) retains its actual R936 constant term
\[
H(0)=\frac{3(3N+2)!}{(2N+1)!\,N!\,2^N}\in\mathbf F_p^\times.
\tag{963.3}
\]
In particular the program does **not** replace \(H\) by \(H/H(0)\) and then report the rescaled trace as the original one. Only the modulus used internally for polynomial reduction is made monic.

The original R939/R958 companion is written
\[
C=sC_0,\qquad C_0\in\mathbf F_p[t],\qquad
F(E_u,\rho)=-D^{N+1}C(t).
\tag{963.4}
\]
The sign is the corrected original sign of R958(958.6), not a new source convention. The program obtains \(H\) and \(C_0\) using the already proved recurrences
\[
h_{j+1}=\frac{(6j+5)^2}{3(j+1)(3j+4)}h_j,
\tag{963.5}
\]
\[
(C_0)_j=
\frac{(j+1)(3j+2)(C_0)_{j+1}+h_j/9}{3(2j+1)^2},
\qquad (C_0)_{N+1}=0.
\tag{963.6}
\]
All displayed denominators are units in the stated range. These are linear-length coefficient constructions; the higher powers and reductions are performed by FLINT's modular polynomial arithmetic.

Set
\[
\beta=-(1-8t)H-3tDH',\qquad
L=\mathbf F_p[t]/(tH),\qquad e_0=H/H(0)\in L.
\tag{963.7}
\]
The actual full-point weight is \(3-2e_0\): it is one at \(t=0\), and three at every root of \(H\). The elliptic points have the already proved zero contribution of R936/R939. No point is discarded on the basis of a numerical nonzero denominator, and no finite-field norm is treated as a positive real quantity.

Use R958's moment functional on the unique degree-at-most-\(N\) representative,
\[
\ell_N(t^j)=
\frac{(1/3)_j(2/3)_j}{4^j(7/6)_j^2},\qquad 0\le j\le N.
\tag{963.8}
\]
The reported quantity `moment_over_s` is exactly
\[
m_p=\frac{\ell_N(R_F)}s
=\ell_N\!\left(2D^{2N+1}\beta^2C_0^p\bmod tH\right).
\tag{963.9}
\]
Indeed the original polynomial is \(R_F=-2D^{2N+1}\beta^2C^p\), and \(C^p=-sC_0^p\). This explains the positive sign in (963.9) without changing the original companion.

The other reported scalars are
\[
c_p=\frac{c_{\rm mom}}s
=\operatorname{Tr}_{L/\mathbf F_p}
\left((3-2e_0)\frac{DC_0}{\beta^2}\right),
\tag{963.10}
\]
\[
T_p=3\operatorname{Tr}_{L/\mathbf F_p}
\left((3-2e_0)D^{2N+2}C_0^{p+1}\right),\qquad
S_p^{\,p}=432T_p.
\tag{963.11}
\]
Here \(T_p\) is the original R939 polynomial trace and \(S_p\) is the original complete supersingular pairing of R932/R936; the subscript indicates the prime and does not denote a Hecke operator. R958's exact scale becomes
\[
\boxed{\quad T_p=\frac32c_pm_p,\qquad
S_p^{\,p}=648c_pm_p.\quad}
\tag{963.12}
\]
The equality follows from \(c_{\rm mom}=sc_p\), \(\ell_N(R_F)=sm_p\), and \(s^2=-3\). It retains the original fine-cover and source normalizations already incorporated in R932/R936; no new cover degree or source scalar is introduced here.

## 3. Checks performed at every candidate prime

In addition to evaluating (963.9–11), the consumer checked all of the following before emitting a successful row:

1. \(H\) has degree \(N\) and the original nonzero constant term (963.3), and satisfies
   \[
   9tDH''+12(1-8t)H'-25H=0.
   \]
2. The companion obeys the **negative** original equation
   \[
   9tDC_0''+6(1-12t)C_0'-9C_0=-H/3.
   \]
3. \(\beta'=-H/3\), \(H(1/4)\ne0\), and \(tH\) is squarefree. Thus the finite algebra used for the trace is étale.
4. \(\beta^{p-1}=1\) in the whole algebra \(L\), checked by multiplying the computed \(\beta^{p-3}\) by \(\beta^2\). This verifies the inverse used in (963.10).
5. \(e_0^2=e_0\), retaining exactly the one-versus-three whole-point weights.
6. The computed \(c_p\) is nonzero, as predicted by the proved R958 criterion, and the independently evaluated trace agrees with the moment by both equalities of (963.12).

For a monic squarefree modulus \(M=(tH)/h_N\), the trace routine uses the standard Euler identity
\[
\operatorname{Tr}_{L/\mathbf F_p}(f)
=[t^{\deg M-1}]\bigl(fM'\bmod M\bigr).
\tag{963.13}
\]
Thus the trace is taken over the entire finite étale algebra, rather than just over its rational roots. This identity is valid after a splitting-field extension and then descends: at a root \(a\), the Lagrange basis polynomial has leading coefficient \(1/M'(a)\), so the displayed coefficient sums \(f(a)\) over all roots.

The program had a separate checked witness path if a zero occurred: it would solve the triangular opposite-deck system for \(K\), check \(\mathcal L_-K=R_F/s\) as a full polynomial identity, and output the actual Cartier-preimage certificate. That branch was not reached in this run. Its existence is not counted as a test of a zero instance.

## 4. Compact receipt

The returned summary has `status=completed`, `failure=null`, `first_zero=null`, and `uncompleted_count=0`.

| Item | Returned value |
|---|---:|
| Requested interval | \(1000<p\le100000\) |
| Candidate primes satisfying (963.1) | 1,582 |
| Completed candidate primes | 1,582 |
| First completed prime | 1,019 |
| Last completed prime | 99,923 |
| Zero moments | 0 |
| Uncompleted candidates | 0 |
| Reported elapsed seconds | 539.210186 |

Two endpoint rows, included only to make the receipt easy to compare with the public log, are:

| \(p\) | \(m_p\) | \(c_p\) | \(T_p\) | \(S_p^{\,p}\) |
|---:|---:|---:|---:|---:|
| 1,019 | 460 | 875 | 502 | 836 |
| 99,923 | 27,610 | 24,066 | 61,388 | 40,021 |

The log's canonical output hashes are:

- Arithmetic rows SHA256: `26009267ff3ae699f724fe79d98c0ccabdaf0a81b0dfe41abeb72636cb16cdd5`.
- All consumer stdout records before the summary, including newlines, SHA256: `2ff33749dc79218136abb5d2cc3bdbee6789c6d7fb822208af86d118ebc63049`.
- Summary payload before insertion of its own hash field, SHA256: `2f406127e48c88e9cfca3bd47a17c59c264627796f0112c42ddacf39dc64239a`.

The arithmetic-row hash excludes runtime timings and event wrappers; the prefix hash includes the actual emitted records. The script defines both canonicalizations explicitly. The root's independent I/O verification agreed with all three values.

## 5. Exact finite consequence and remaining boundary

By the proved equivalences in R955, R958, and R960, for each and every prime in (963.1):
\[
\ell_N(R_F)\ne0
\iff S_p\ne0
\iff L=1
\iff h=2.
\tag{963.14}
\]
Here \(L\) is the actual single odd Cartier-chain length, and \(h\) is the height of the one-dimensional formal connected part of the actual inverse-character Igusa factor in R960. These are the original geometric objects. The finite conclusion does not identify that factor with the different height-two CM target of R916.

No argument in this receipt controls the unbounded range \(p>100000\). In particular the complete successful window does not eliminate the possible longer chains \(L\ge3\) in that range. It also does not identify the low Scholl Frobenius unit of R961 with the named bottom class: R961's top-versus-bottom distinction remains necessary. The remaining task is an actual general nonvanishing or global comparison argument, together with the independent original endpoint and height bridges required by the topic README.
