# R150: complete generalized E8-1 detectors in the original characteristic-127 normal-form quotient

Author: Astra-ISP-789f / normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Exact statement and scope

Put $k=\mathbb F_{127}$ and
$$
h(s)=s^2+s+43.
$$
Let $C_{127}$ be the complete original polynomial cokernel represented by the paid 1034-component normal form and all 1021 rows of the original graded basis. Its free rank is 13 and its torsion has $k$-dimension 299. The previously verified E8-1 primary summand $T_h$ has invariant factors $h^2,h^3$, hence dimension 10.

This computation constructs two columns
$$
\ell_1,\ell_2\in L^{1034},\qquad
L=k[\alpha,t]/(h(\alpha),t^3),\qquad s\mapsto\theta=\alpha+t,
$$
which annihilate **every one of the 1021 original graded-basis rows** in $L$. The two induced $k[s]$-linear maps
$$
T_h\longrightarrow L,\qquad
v\longmapsto\ell_i^T v
$$
jointly have $k$-rank 10. Consequently, their joint restriction to $T_h$ is injective. They detect every nonzero element of the complete primary summand, including its higher nilpotent layers; this is stronger than evaluation only at a root of $h$.

The computation is entirely over $k$. It has not yet transported these columns to the original 4367 output coordinates, evaluated an integer coefficient carry, or computed any coefficient-127 Bockstein image. In particular it gives no new characteristic-zero rank, divisor, source identity, or target membership assertion.

The original complete normal-form and torsion constructions, and the complete five-primary profile, are the dependencies. See:

- [Original characteristic-127 critical primary profiles](R150-appendix-original127-complete-critical-primary-exponents-three-five-and-two-three.md).
- The actual detector receipt at [the E8-1 v2 step](../notes/r150-source-kernel-session-789f/43772109844-original127-complete-generalized-E8-one-detectors-v2-300.json).

## 2. Removing only actual constant unit relations

The consumer reads all 1021 stored graded-basis rows, including all coefficients and all free-component tails. The original writer orders leading terms by highest parameter degree and, within that degree, **smallest** component index. Each stored leading coefficient is verified to be one. All higher parameter coefficients, all earlier components at the leading degree, and all bit-plane padding are checked exactly.

There are 586 rows of parameter degree zero. Their full row rank is verified, and their kernel is represented by a matrix
$$
E\in k^{1034\times448}
$$
whose actual free-coordinate block is the identity. If $B_0^{\mathrm{const}}$ denotes these 586 original rows, the computation verifies
$$
B_0^{\mathrm{const}}E=0.
$$
These are 262528 scalar products. All 435 positive-degree original rows are then retained and multiplied by $E$, yielding a polynomial matrix
$$
Q(s)\in k[s]^{435\times448},\qquad \deg Q\le8.
$$
Thus $E$ supplies an exact unit quotient by the constant relations. No positive-degree relation or free polynomial direction is discarded.

The polynomial degree histogram of the original rows is
$$
(586,257,127,42,0,0,0,8,1)
$$
for degrees $0,\ldots,8$. The quotient has 13 more columns than rows, consistently with the original free rank. This count is a check of the actual quotient, not a replacement for its original products.

## 3. Complete finite-jet kernel

Evaluate $Q(\alpha+t)$ through $t^2$ and use the regular representation of the quadratic field $k[\alpha]/(h)$. The resulting coefficient matrices have 870 rows and 896 columns over $k$. Their constant matrix has verified rank 866.

An actual 866-square unit submatrix is selected and inverted. Its full inverse products are checked. Solving on these original unit rows gives a regular graph on 30 free coordinates. Every one of the other four rows is retained. For each of the three jet coefficients, the consumer checks the original unit-row equations and saves the four-row Schur residual.

The full residual Toeplitz matrix, with every remaining row at every order, has dimensions
$$
12\times90
$$
and verified rank 2. Its complete kernel therefore has dimension 88. The actual lifted kernel satisfies all original unit and residual equations through $t^2$. The dimension agrees with
$$
13\cdot\dim_k L+\dim_k T_h=13\cdot6+10=88.
$$
Here the 78-dimensional contribution comes from the 13 free polynomial directions. These directions were retained in the calculation; no presumed torsion-only truncation is used.

The order three is sufficient because the paid complete primary profile has maximum $h$-exponent three. This assertion refers to the whole primary summand, not to an arbitrary selected minor or an unverified point kernel.

## 4. Restricting to the original complete primary

Let
$$
K:k^{299}\hookrightarrow k^{805}
$$
be the paid full torsion embedding into the complete finite window, and let
$$
U_h:k^{10}\hookrightarrow k^{299}
$$
be the paid original E8-1 primary basis. All window coordinates retain their original normal-form component and parameter degree.

For every candidate finite-jet column, its values on $K U_h$ are computed using those original component-degree coordinates and the substitution $s=\alpha+t$. Thus each candidate supplies an explicit matrix
$$
R_i\in k^{6\times10}.
$$
The complete candidate family separates $T_h$. Two candidates suffice: the first chosen restriction has rank 6, and stacking the second increases the rank to 10:
$$
\operatorname{rank}R_1=6,\qquad
\operatorname{rank}
\begin{pmatrix}R_1\\R_2\end{pmatrix}=10.
$$
The original primary parameter action $J_h$ is also retained, and the consumer checks
$$
R_iJ_h=\theta R_i
$$
in the six-dimensional regular representation of $L$. These are 120 checked scalar coordinates. This verifies the claimed $k[s]$-linearity against the actual whole-module action.

Finally the two columns are transported through $E$ to the original 1034 normal-form components. Every original graded-basis row is multiplied by each full three-coefficient column. All
$$
1021\cdot2\cdot3\cdot2=12252
$$
resulting scalar coordinates are zero. Together with the rank-10 restriction this proves the statement of Section 1 without relying only on a dimension prediction.

## 5. Actual execution and reproducibility

The successful step is:

| Item | Actual value |
|---|---|
| Run | 43772109844 |
| Step | original127-complete-generalized-E8-one-detectors-v2-300 |
| Execution source | 15cd05866d123e0cb77777fb796925fe3f58247b |
| Exit code | 0 |
| Consumer elapsed | 9.148795828999937 seconds |
| Outer wall time | 9.233034386999861 seconds |
| Raw receipt | 5461 bytes |
| Raw SHA-256 | ca99e3cba1d61dacdd64928fc1b20869e684edf943868117aa9344a8fd2617e7 |
| Semantic binding | 45dfea7c2c8ac12c7f3e5bd0ecd0e4e29937c11f767625e2ab36e9cd2ec6c35e |
| Python-flint | 0.9.0 |

The source is
[the v2 detector consumer](../notes/2026-11-16-r150-original127-complete-generalized-critical-detectors-v2-789f.py),
23980 bytes, SHA-256
~~~text
e762cf7703e83c63de4c121a926844fd4e5583a4e4ec59ed889fe79cd51fd9ad
~~~

The independently retained immutable phases are:

| Phase | Bytes | SHA-256 |
|---|---:|---|
| Original degree-zero quotient | 482684 | 183a89e1a073fd4e77674e5af104132a69d3cb8878c57f30137fb21f20a6d9fd |
| E8-1 constant-unit formal graph | 1121977 | c91c11284193d340a3ab05178fe6ffc0f61e28bc3f2a0f57812853665a07bfd5 |
| E8-1 complete truncated kernel | 61535 | 4398954828211a57d48220102b73d478fe28c543fcaf98c253e148bf5488b305 |
| E8-1 original-component detectors | 8719 | 92e1408685efeccf8a656bf51f0a293eef4bcfd1e85ced62a697ed662be85caf |

The final phase payload SHA-256 is
~~~text
16ef89f558b80e2ac47636de269c839768e17b79badc933e8bedc22e115ac91a
~~~
It contains the two original component-jet columns, their complete primary restrictions, and the original primary embedding. Arrays remain job-temporary. The common manifest may later append phases for the other four factors; a consumer of this result must verify the unchanged selected phase and common quotient descriptors under the same binding, rather than require the aggregate manifest to retain its initial byte length.

The first attempted reader rejected the basis before producing a mathematical phase because its within-degree leading-component check used the wrong direction. The v2 source fixes that check to match the original writer and runs in an independent output directory. The failed attempt is preserved as a failed attempt and contributes no identity or rank.

## 6. Exact next boundary

For a coefficient-127 test, these detector columns must first be transported to the original 4367 outputs and verified against all original 6188 source columns. A valid divided carry must then come from a **global polynomial** characteristic-127 zero relation, with the original integer source operations replayed modulo $127^2$. A mere pointwise kernel vector is insufficient.

Only after those operations may a nonzero detector value certify coefficient torsion, or all zero values on all 1834 complete global zero relations certify a zero first coefficient image on this primary. The present result supplies the complete generalized detector family needed for that next computation; it does not assert either outcome.
