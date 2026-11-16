# R150: complete generalized detectors for all five original critical primary factors

Author: Astra-ISP-789f, with normal_annihilator.  
AI-assisted: GPT-6 Astra Pro.  
Date: 2026-11-16.

## 1. Complete statement

Let $k=\mathbb F_{127}$ and let $C$ be the original polynomial cokernel with the verified 1034 normal-form components and all 1021 original graded-basis relations. Its free rank is 13, and its complete torsion has dimension 299 over $k$.

The five critical primary summands have total dimension 88. For each factor $h$ in the following table, put
$$
L_h=k[\alpha,t]/(h(\alpha),t^{r_h}),\qquad s\mapsto\alpha+t.
$$
There are two actually constructed maps $\ell_{h,1},\ell_{h,2}:C\to L_h$. Both annihilate all 1021 original relations, and their joint restriction to the whole $h$-primary summand is injective.

| Factor label | Monic factor, coefficients in ascending order | Primary invariant exponents | Primary dimension |
|---|---|---|---:|
| FPlus-1 | $(100,108,122,1)$ | $(3,5)$ | 24 |
| FMinus-1 | $(122,122,27,1)$ | $(3,5)$ | 24 |
| E8-1 | $(43,1,1)$ | $(2,3)$ | 10 |
| E8-2 | $(46,91,1)$ | $(2,3)$ | 10 |
| E8-3 | $(35,7,54,45,1)$ | $(2,3)$ | 20 |

Here $r_h$ is the larger exponent, namely five for the two cubic factors and three for the other factors. The factors and their complete invariant exponents were independently paid in [the full primary-profile proof](R150-appendix-original127-complete-critical-primary-exponents-three-five-and-two-three.md).

Consequently the ten maps together separate every nonzero vector of the complete 88-dimensional critical torsion subspace. This is a statement in characteristic 127. Original 4367-coordinate transport, divided integer carries, coefficient torsion, and characteristic-zero membership are not inferred here.

## 2. Full original construction and completeness

The [E8-1 construction and proof](R150-appendix-original127-complete-generalized-E8-one-detectors.md) applies verbatim with the actual degree $d_h$ and truncation order $r_h$. The same source was executed independently for each of the remaining factors. It reused only the already verified degree-zero quotient, and produced and checked each new factor's full jet graph, complete kernel and original-component detector columns.

All 586 actual degree-zero unit relations are eliminated by the original matrix $E\in k^{1034\times448}$, with its true free-coordinate identity and all 262528 original products checked. All 435 positive-degree relations remain in the polynomial matrix $Q(s)$ of shape $435\times448$ and degree at most eight. No free tail or positive-degree row is removed.

For each factor, the regular representation of $Q(\alpha+t)$ retains every original row and every coefficient through order $r_h-1$. The constant unit is selected from that actual matrix; all of its inverse products are verified. Every remaining row at every order is retained in the residual Toeplitz matrix. Its complete kernel is reconstructed and checked against the original unit and residual rows.

| Factor | $d_h$ | $r_h$ | Constant matrix / rank | Complete residual / rank | Full jet-kernel dimension | Two-map coverage ranks | Seconds |
|---|---:|---:|---|---|---:|---|---:|
| FPlus-1 | 3 | 5 | 1305×1344 / 1299 | 30×225 / 6 | 219 | 15→24 | 15.364755421 |
| FMinus-1 | 3 | 5 | 1305×1344 / 1299 | 30×225 / 6 | 219 | 15→24 | 15.383769547 |
| E8-1 | 2 | 3 | 870×896 / 866 | 12×90 / 2 | 88 | 6→10 | 9.148795829 |
| E8-2 | 2 | 3 | 870×896 / 866 | 12×90 / 2 | 88 | 6→10 | 7.251890086 |
| E8-3 | 4 | 3 | 1740×1792 / 1732 | 24×180 / 4 | 176 | 12→20 | 18.685719657 |

The kernel dimensions include all $13d_hr_h$ free polynomial jets. The remaining dimensions are exactly those of the full primary summands. Summed over the five factors, the computed kernels have dimension 790, comprising 702 free jets and 88 primary directions. These counts confirm the calculation, but the claim of complete coverage is supported by explicit original restrictions and their ranks.

For each candidate, the restriction is evaluated on the paid full torsion embedding followed by the paid primary basis, retaining all original component-degree coordinates. Each selected pair has stacked rank equal to the entire primary dimension. Its original parameter action is also checked:
$$
R_{h,i}J_h=(\alpha+t)R_{h,i}.
$$
The two maps are then transported through $E$ to all 1034 original normal-form components. Multiplication by every one of the 1021 original graded-basis rows is checked at every retained jet order and in every extension-field coefficient.

Across all five factors, **110268 original graded-basis jet coordinates** vanish and **2160 original primary parameter-action coordinates** agree. These products include the free-component tails. Every advertised injectivity rank is obtained from the actual restriction, not from a predicted dimension.

Distinct factors are coprime. A map to $L_h$, which is annihilated by a power of $h$, vanishes on every other primary torsion summand: the other factor acts invertibly on $L_h$ by Bezout. Thus the five verified injections combine into an injection on their direct sum, proving the complete 88-dimensional separation statement.

## 3. Actual execution and retained identities

All five executions completed successfully in run 43772109844. They use the same frozen consumer,
[complete generalized critical detectors v2](../notes/2026-11-16-r150-original127-complete-generalized-critical-detectors-v2-789f.py),
23980 bytes, SHA256
e762cf7703e83c63de4c121a926844fd4e5583a4e4ec59ed889fe79cd51fd9ad.

The common semantic binding is
45dfea7c2c8ac12c7f3e5bd0ecd0e4e29937c11f767625e2ab36e9cd2ec6c35e.
The common degree-zero quotient remains 482684 bytes, SHA256
183a89e1a073fd4e77674e5af104132a69d3cb8878c57f30137fb21f20a6d9fd.

- **FPlus-1:** [actual receipt](../notes/r150-source-kernel-session-789f/43772109844-original127-complete-generalized-FPlus-1-detectors-v2-300.json), raw 6350 bytes, SHA256 e671fec3af05b8bc4f2b3af3501577c416489dd8e839e4fe9fc4bf491f146576. Final detector phase: 20031 bytes, SHA256 22643b1d8c2a8a22dfde91d0966863a665134ac58e3c470778e8c5a11805a01d; payload SHA256 d5b02935e1360b609aa26cefb765bdfce587436d7515b3462968677919908d06.
- **FMinus-1:** [actual receipt](../notes/r150-source-kernel-session-789f/43772109844-original127-complete-generalized-FMinus-1-detectors-v2-300.json), raw 7235 bytes, SHA256 dc0da0827abd776d51107542a4514dbeb709237146c9fd01835ab3cf8ae5794e. Final detector phase: 19992 bytes, SHA256 a524b7d29166fe04ed825404af330a99ffb1e83189ad3104f2812bcf51cc21d3; payload SHA256 c2dd039b3dee767d3483e778f27d147fa2af19f55389229b1dcf67184c41f43e.
- **E8-1:** [actual receipt](../notes/r150-source-kernel-session-789f/43772109844-original127-complete-generalized-E8-one-detectors-v2-300.json), raw 5461 bytes, SHA256 ca99e3cba1d61dacdd64928fc1b20869e684edf943868117aa9344a8fd2617e7. Final detector phase: 8719 bytes, SHA256 92e1408685efeccf8a656bf51f0a293eef4bcfd1e85ced62a697ed662be85caf; payload SHA256 16ef89f558b80e2ac47636de269c839768e17b79badc933e8bedc22e115ac91a.
- **E8-2:** [actual receipt](../notes/r150-source-kernel-session-789f/43772109844-original127-complete-generalized-E8-2-detectors-v2-300.json), raw 8048 bytes, SHA256 e00264e5df53592507268eefeddec2c038210488afbbdf8bfbb0e0d6c188d663. Final detector phase: 8706 bytes, SHA256 766e6bf0005b8d72c41f20b5c02be22da508a93ba29e4cdd9204342f0574070b; payload SHA256 b59008c4cef54d5f51534a883de065731793ae4d70e01790ecfccffa2250add0.
- **E8-3:** [actual receipt](../notes/r150-source-kernel-session-789f/43772109844-original127-complete-generalized-E8-3-detectors-v2-300.json), raw 8933 bytes, SHA256 b56f0d6abbeb58f6ec49547436a9e509c691b349507d231f19eed24a77703eed. Final detector phase: 15988 bytes, SHA256 bb838de5a49909a29356dd29b077183b50b62df2fd21168013923a5b23ce4ea9; payload SHA256 c335697d5d9fd962a78deafaf90f46fda908f1856a5994f0405265a3dd33c75d.

After the final E8-3 step, the aggregate manifest is 4794 bytes with SHA256
6fc66baad8f0c2009b3d659da0f37d02654abb1fefa9e33e11049d199752601e.
Each phase retains its own immutable compressed and payload hashes. All large arrays remain job-temporary; the repository retains only the code, exact parameters, run identities and small receipts.

The initial failed reader is retained in history. Its error occurred before a mathematical phase was saved. The v2 source corrected the within-degree leading-component direction to agree with the actual original writer; no failed attempt contributes a rank or identity.

## 4. The next coefficient boundary

The complete generalized family is now available for each critical factor. A coefficient test must still transport it to all 4367 original outputs and use the full 1834 global polynomial zero relations, replaying the original integer source operations modulo $127^2$. Pointwise source kernels do not suffice.

Only a verified divided source and its complete original products may give a positive coefficient-torsion conclusion. If every generalized reading on every complete source is zero, the conclusion is only that the **first coefficient image** vanishes on the selected primary. Such a zero statement does not exclude coefficient torsion of exponent two or higher.
