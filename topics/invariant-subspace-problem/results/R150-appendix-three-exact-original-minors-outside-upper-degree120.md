# R150: three exact original-row determinant certificates and an outside upper divisor of degree 120

Date: 2026-11-15 UTC. Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.

## 1. Result and its scope

Let $G(s)\in\mathbb Q[s]^{56\times22}$ be the actual original polynomial core in [the complete original projection reduction](R150-appendix-original-projection-away-from-critical-support-56-by-22-schur.md). Put
$$
\Sigma_0=s(s-2)(s+6)F_+F_-E_8,\qquad S=\mathbb Q[s,\Sigma_0^{-1}],
$$
and let $\Omega$ be the monic part, coprime to $\Sigma_0$, of the gcd of **all** $22\times22$ minors of $G$.

The new execution has computed three nonzero exact determinants from constant rational combinations of the original 56 rows. Removing only the already specified factors of $\Sigma_0$ and taking their exact gcd gives a nonzero polynomial $U$ with
$$
\boxed{\Omega\mid U,\qquad \deg U=120.}
\tag{1}
$$
The full coefficient vector of the primitive positive $U$ has SHA256
`150089b4e115b8d975d4e4eb13492779a692a6af258094f852af22b7f34e652d`.

This is an actual upper divisor certificate. It does **not** yet prove $\Omega=U$, $\Omega=1$, or new membership of the nine original targets. The next separate question is whether the full 56-row matrix supplies the matching local lower valuations.

## 2. Why these are valid original minor certificates

For each original row $G_i$, the program chose a nonzero **constant** rational scalar $a_i$ by clearing all coefficient denominators and then removing integer content. It obtained
$$
Z_i=a_iG_i\in\mathbb Z[s]^{22}.
$$
All $56\cdot22=1232$ original polynomial identities were checked exactly. Thus this row normalization is a unit change over $\mathbb Q[s]$ and over $S$.

The first two squares select 22 original normalized rows, in ascending and descending greedy profile orders. The third uses a fixed integer row transformation $T=UL$, where $U,L$ are respectively upper and lower triangular with diagonal entries 1 and frozen signed off-diagonal entries, and then selects 22 rows of $TZ$. The resulting integer $22\times56$ row-combination matrix $C$ is recorded. Every resulting square $B=CZ$ was independently multiplied from the **original rational** $G$, including the scalars $a_i$, and all 484 polynomial coordinates were checked.

For the first two squares, $\det B$ is an original maximal minor times a nonzero rational constant. For the third, Cauchy--Binet gives
$$
\det(CZ)=\sum_{|I|=22}\det(C_{:,I})\det(Z_{I,:}).
$$
Hence the gcd of all original maximal minors divides every computed determinant. Taking their gcd and then removing only factors supported on $\Sigma_0$ proves (1). A constant row combination need not itself select one original minor; the displayed identity is the reason it remains a valid upper certificate.

The fixed finite-field profile at $s=4$ over $\mathbb F_{65521}$ selected nonzero squares. Their profile determinants were respectively $22582,4250,49860$. These values justify selection and check signs; they do not assert the characteristic-zero gcd of all minors.

## 3. Exact determinant arithmetic and completed checks

Each integer polynomial square was evaluated by fraction-free Bareiss elimination with both row and column swaps recorded. Every complete pivot transaction checked that each division had zero polynomial remainder and that multiplying the quotient by the previous pivot recovered the dividend. Only a fully completed pivot replaced the checkpoint.

All three squares completed 21 pivots, with **3311 exact polynomial divisions per square**. The signed resulting polynomial determinants were also checked against independently computed integer determinants at $s=-1,3,4$, and against the fixed field profile. Known-factor removal used exact polynomial division. The final $U$ was checked to divide the outside part of every completed determinant and to be coprime to each of the six specified support factors.

The startup checks used an independent six-term $3\times3$ determinant expansion with nontrivial swaps and verified that an interrupted pending pivot leaves the prior matrix unchanged. No previous row-module reduction or its large intermediate coefficients were loaded.

## 4. Actual execution and immutable input identity

The actual [execution receipt](../notes/r150-source-kernel-session-789f/43756208221-original-three-minor-determinant-upper-180.json) records:

| Item | Actual value |
|---|---|
| Run / step | `43756208221 / original-three-minor-determinant-upper-180` |
| Execution commit | `7b770ffec7ad458f124ed0b7e459ec11bf7e02a2` |
| Status / exit | completed / 0 |
| Mathematical time | 113.5622418009998 seconds |
| Wall time | 113.66367042999991 seconds |
| Budget | 180 seconds, 2048 MiB; outer limit 240 seconds |
| Frozen program | `766c8e072b176435223f767a1616e392731a6b92` |
| Program SHA256 | `4ae559a6b1b5efdf3d88e1f59bc987895f0f6ab5ec8dd2d61d5a55db3ef9a1be` |
| Mathematical binding | `5fc42d162e51b638ce06bbd67c2afd5755539a95a3bf5a650c4155df0ed6c8ef` |
| Full temporary receipt | 8436 bytes; `a18b3c1dd68890455a2b256adf1dfd9a9d690b60f81c99155be6e60a507dd145` |

The exact paid core retains all 56 rows and 22 columns, 641 nonzero polynomials, maximum degree 126, and maximum normalized integer coefficient height 409 bits. Its parent semantic binding is
`ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba`;
its logical matrix SHA256 is
`752d21d7ca74ee5235c05ade9048ef48f120891c567abfb5132a4b2b33b745c8`.
The stored core phase is 1394807 bytes with SHA256
`8693870cd23a4693d840d2d27bc1e0676ff4b8253a2b9c85e7b3c267a8199a82`.

The current upper polynomial is retained only in the live job:
`current-outside-gcd-upper.json.gz`, 12999 bytes, SHA256
`b6c26ab0cfae6a08dbdb02ebac570ef2fffaec953a0de4d9aef422b74815c3ab`,
exact uncompressed payload SHA256
`e1722fa0f09424affa18c29e4275858619cf4c789a891937fc6c6d4355a867c1`.
Its polynomial coefficients, the three complete determinants, row combinations, and complete pivot checkpoints are reproducible from the committed program, parameters, and pinned original core; no large recomputable array is published.

## 5. Precise next certificate

A matching lower certificate must use all 56 original rows. For a squarefree factor $f$ occurring in $U$ to exponent $e$, exact unit Schur elimination over $\mathbb Q[s]/(f)$ determines a rank uniformly on every irreducible component on which its pivots are units. If the residual corank is at least $e$, every maximal minor has valuation at least $e$ there; (1) then gives equality. If a nonunit entry distinguishes components, its exact gcd with $f$ splits the branch. If the first corank is smaller than $e$, further exact calculations modulo powers of $f$ are needed.

This describes the pending full-row certification problem, not a result already obtained by the present three determinants.
