# R150 appendix: complete critical high-block rank bounds and seven residue directions

Author: Astra-ISP-789f / root and literature_audit. AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16 UTC.

Status: completed computations on the complete original high block at all three critical number fields. The exact rank over each number field remains open. The actual residue rank is 4259, so this computation does not prove that the two previously certified high directions are complete.

## 1. The complete original partition

Use the original seventeen equations in co-moving coordinates
$$
c=z_0,\quad d=z_1,\quad n=(z_2,\ldots,z_{10}),
$$
with all source multipliers of degree at most three and all 4367 output monomials of degrees one through five. We write the transpose of the source map when describing a matrix with source rows and target columns.

At a root $\alpha$ of $F_+,F_-$ or $E_8$, let $K=\mathbb Q(\alpha)$. Partition the 6188 original source rows into the 170 pure sources and every source of positive normal degree. Partition the target columns as follows.

| Block | Complete coordinate definition | Count |
|---|---|---:|
| Low source rows | All ten pure multipliers for each of the seventeen equations | 170 |
| High source rows, normal degree 1 | All six pure tangent multipliers times nine normal variables and seventeen equations | 918 |
| High source rows, normal degree 2 | All three pure tangent multipliers times 45 normal quadratic monomials and seventeen equations | 2295 |
| High source rows, normal degree 3 | All 165 normal cubic monomials times seventeen equations | 2805 |
| Low target columns | All 20 pure targets and all 81 one-normal targets with $d$ exponent zero or one | 101 |
| High target columns | All 54 one-normal targets with $d$ exponent at least two, and every normal-degree 2, 3, 4 and 5 target | 4266 |

The high target sector sizes are exactly
$$
54,\ 450,\ 990,\ 1485,\ 1287.
$$
The entire original matrix therefore has block form
$$
\mathcal A_0=
\begin{pmatrix}
L&G\\
0&H
\end{pmatrix},
\qquad
L\in K^{170\times101},\quad
H\in K^{6018\times4266}.
$$
The lower-left zero block is checked on every original high row using the exact original coefficient generator. It is not obtained by dropping high-to-low terms.

All original equations have pure restriction $q_i d^2$ and moment degree at most two. The high rows retain all cross-sector contributions of their actual products. Each high row has at most 77 nonzero entries. The complete original high matrix has 340548 nonzero entries before residue specialization.

## 2. Two independent number-field kernel columns give the upper rank bound

The [completed 135-coordinate calculation](R150-appendix-complete-135-coordinate-quadratic-high-slice.md) gives two genuine $K$-valued high columns supported on the 450 normal-quadratic coordinates. Embed them in all 4266 high coordinates.

For each field, the new consumer independently checks:

- all 12376 original products against the paid parent certificate;
- all 12036 high-row products of the two embedded columns equal zero;
- an actual nonzero two-by-two coordinate minor of the columns.

Thus these are two independent elements of the complete kernel:
$$
\dim_K\ker H\ge2,\qquad \operatorname{rank}_K H\le4264.
\tag{2.1}
$$
This is an upper rank bound from actual number-field columns. No finite-field kernel vector is lifted by assertion.

## 3. A genuine residue lower bound from all rows

Represent each entry of $H$ by its canonical polynomial in $\alpha$ of degree less than the defining field polynomial. For each whole original row, clear the denominators of all coefficients and divide the common integer content. This multiplies that entire $K$-row by one nonzero rational scalar.

The consumer verifies this common scalar identity for every coefficient. It does not independently rescale individual entries or divide by a parameter polynomial. The resulting row-equivalent matrix has entries in the image of $\mathbb Z[\alpha]$.

Use the following prescribed residue homomorphisms:

| Field | Prime | Root |
|---|---:|---:|
| $F_+$ | 19 | 5 |
| $F_-$ | 17 | 4 |
| $E_8$ | 17 | 5 |

The original defining polynomial vanishes, its derivative is nonzero, its leading coefficient is a unit, the noncontact factor is nonzero, and the physical $J_3$ determinant is a unit at each prescribed residue. These checks qualify the specialization used here. They do not assert parameter-jet flatness or good reduction of any complete local Smith form.

A nonzero residue minor of this integer-polynomial representative is a nonzero minor over $K$. Since the whole rational row scalings are units over $K$,
$$
\operatorname{rank}_{\mathbb F_p}\overline H
\le \operatorname{rank}_K H.
\tag{3.1}
$$
In fact, none of the 6018 denominator clearings or integer contents is divisible by its prescribed prime in the actual runs. The lower-bound argument does not identify a residue kernel with the number-field kernel.

## 4. Actual full rank calculation and the resulting interval

The native exact elimination reads all 6018 rows and all 4266 columns. It verifies every field addition pattern and every nonzero inverse, keeps all original row additions, and retains the actual independent normalized pivots. Every dependent original row is reduced to zero on all 4266 coordinates.

| Field | Prime | Residue root | Residue rank | Residue nullity | Program seconds |
|---|---:|---:|---:|---:|---:|
| plus | 19 | 5 | 4259 | 7 | 9.009990373000619 |
| minus | 17 | 4 | 4259 | 7 | 8.924869801998284 |
| e8 | 17 | 5 | 4259 | 7 | 13.247619434001535 |

For every field there are 1759 dependent original rows and 4259 actual independent pivots. The finite-field kernel dimension is therefore seven. Combining (2.1) and (3.1) proves
$$
\boxed{
4259\le\operatorname{rank}_K H\le4264,\qquad
2\le\dim_K\ker H\le7.
}
\tag{4.1}
$$

The seven residue directions are not yet seven certified $K$-directions. The upper endpoint 4264 is not attained by the residue calculation, so the claim that the complete high kernel equals the old two-column space is not established.

For the two cubic fields, all 978810 rational coefficient identities in the row normalization are checked; for the degree-eight field the count is 2246130. The original row and column dictionaries, complete original number-field rows, primitive integer rows, evaluated residue rows, normalized pivots and full row-operation DAG each have their own hashes in the actual receipts.

## 5. Execution and reproducibility

All three tasks ran in the existing temporary session 43756208221 from execution source a9ad16ee65f3aff9dff1a287bc4fe18667168d42. All exited zero. The consumer and exact native source were fully reviewed by the root before they were queued.

| Source | Bytes | SHA256 |
|---|---:|---|
| [Python consumer](../notes/2026-11-16-r150-critical-complete-high-residue-rank-789f.py) | 28063 | 4a9c045763014812e3805da7f7c24408e27775b3fac1dc8beb5940ba89626ef9 |
| [Native elimination](../notes/2026-11-16-r150-critical-complete-high-residue-rank-native-789f.cpp) | 9177 | bada5f20f24efd06ba9ca9a5f2bda16f1d935d42f89d32be08166a184a609fa7 |
| [Complete interface](../notes/2026-11-16-r150-critical-complete-high-residue-rank-interface-789f.json) | 16112 | b978bb57419ac396c703796768f3006cd45583f1024fed73dac09d04e373418c |

The interface freezes all exact helper sources, original parent receipts, prescribed residues, complete dictionaries and CLI parameters. Each field was given 180 seconds and 2048 MiB. All large arrays remain temporary; the complete normalized pivot files are 11431248 bytes each.

### plus

- [Actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-plus-complete-high-residue-rank.json).
- Raw receipt: 17579 bytes; SHA256 dcb82982aa3c109205bad1a04dfe57f483b74fdf6863ba87e8f442bed2275c43.
- Published outer: 34539 bytes; SHA256 893ba678754194bbbc2aa5156039ad4db8dfa8d83a78f5d339ce109c066f47d3.
- Semantic binding: c3cda40e1e99f191eb5c34a29036525c5fbaa29952cad5b7d82bcfc7b56e316a.
- Temporary manifest: 1561 bytes; SHA256 0db405992db5638e819e62b1e7aa6505fcbbab17260b4201bd07a62f587bbad0.

### minus

- [Actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-minus-complete-high-residue-rank.json).
- Raw receipt: 18041 bytes; SHA256 91d0cbd2960d9115e1b014668c95c265706ba4cd8084238de08d937c20ada764.
- Published outer: 35007 bytes; SHA256 faf2a2bcc5ee9451f46868e677d4af7eedc65944a1b097d6ee65cf1207616e74.
- Semantic binding: 65e7bd29f1e6ee6c35b932cd7f01d63e6fcbc0eb595e56e9d300bc5a9e0a92f1.
- Temporary manifest: 1562 bytes; SHA256 b58a134e244e85f0eef5a66d34fa11414d3cddae585a3d0a5ae7f4b73f9d77af.

### e8

- [Actual receipt](../notes/r150-source-kernel-session-789f/43756208221-critical-e8-complete-high-residue-rank.json).
- Raw receipt: 25625 bytes; SHA256 e2cd74852ccc4a416ddb67b5a95afe230412bc7b2d64d6db9863210d76632277.
- Published outer: 42686 bytes; SHA256 f5d8b9ddbe858deb2b04f16281feed88a47dab11f06946dca0eed7538f2e4eda.
- Semantic binding: 1124ef03b855859da33751856495eb768ae100b5ddbeabe0515dea49adfbbefd.
- Temporary manifest: 1563 bytes; SHA256 57296d33553aec729fd897a6b53f728aac5315dce9797a1844b0bcc7758d4f38.

## 6. The remaining complete local problem

The prior 135-, 270- and 300-coordinate calculations still prove only their declared slice statements. The current result adds a complete high-block dimension interval, rather than a negative conclusion for the full local connection.

A complete connection calculation must cover the actual full $\ker H$ and the original $170\times101$ low block. The retained residue pivots can guide the construction of number-field high columns, but every proposed column must satisfy every original number-field high equation before it is counted. The number-field rank can be declared exactly 4259 only after seven independent such columns have been verified.

The complete original critical first connection, exact characteristic-zero critical lengths, the residual global multiplier and original nine-target membership remain open.
