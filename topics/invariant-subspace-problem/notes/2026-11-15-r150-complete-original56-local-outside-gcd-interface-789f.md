# R150: full original56-row local certification of the determinant upper divisor

Date: 2026-11-15 UTC. Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.

This is an execution interface. The three exact original-row determinants have actually completed and give $\Omega\mid U$, $\deg U=120$. The present new full-row arithmetic has not yet run. No assertion that $U$ is squarefree, a square, or the true $\Omega$ is made before the new receipt.

## 1. Frozen source and inputs

Program:
`notes/2026-11-15-r150-complete-original56-local-outside-gcd-789f.py`,
blob `6aa70edef4444856feb034a425c7b0e51d2f4da0`,
29457 bytes, SHA256
`0e111c2334bf62e4b4404d84c8af5e9f62ee99a6b64f766bad541c126b1e7fa4`.

The accompanying inputs JSON pins the two frozen decoder/upper-certificate sources, actual upper receipt, exact paid core phase, and the complete temporary $U$ file. The original core's mutable manifest is checked by semantic binding and its **immutable polynomial-core descriptor**; later old row-state additions do not change this input identity and are not read.

The source imports only the already pinned upper-program's exact core reader and constant row normalization. It does not call its determinant routine, load a Bareiss matrix, or reuse a Hermite state. Every original row remains present.

The actual parent execution is run `43756208221`, step `original-three-minor-determinant-upper-180`, execution commit `7b770ffec7ad458f124ed0b7e459ec11bf7e02a2`. Its mathematical binding is
`5fc42d162e51b638ce06bbd67c2afd5755539a95a3bf5a650c4155df0ed6c8ef`.
The complete parent raw receipt, 8436 bytes, has SHA256
`a18b3c1dd68890455a2b256adf1dfd9a9d690b60f81c99155be6e60a507dd145`.

## 2. Exact algebra and the fast lower certificate

Let $G$ be the entire $56\times22$ core, with all constant rational row scalings recorded. These scalings are units in $\mathbb Q[s]$. All maximal minors of $G$ have the outside gcd $\Omega$, and the completed parent certificate proves $\Omega\mid U$.

The new source first computes a complete squarefree decomposition
$$
U_{\mathrm{monic}}=\prod_i f_i^{e_i},
$$
with monic squarefree, pairwise coprime $f_i$. It verifies the product exactly. This needs no irreducible factorization.

For each $f_i$, start with **all 56 rows** modulo $f_i$. A retained entry $a$ is a unit exactly when $\gcd(a,f_i)=1$. The extended gcd gives an inverse, and its product is checked modulo the current power of $f_i$. After swapping that entry to position $(0,0)$, the residual is
$$
C_{ij}=B_{ij}-B_{i0}B_{00}^{-1}B_{0j}.
$$
Every retained coordinate is checked by
$$
B_{00}C_{ij}=B_{00}B_{ij}-B_{i0}B_{0j}
$$
in the full current finite ring. No nonpivot row is discarded.

If, after unit pivots modulo $f_i$, the remaining block is zero and has $k$ columns, every original maximal minor is divisible by $f_i^k$. The same rank deficiency holds at every irreducible component of the squarefree $f_i$. Consequently $k=e_i$ already proves that the true exponent is exactly $e_i$, using $\Omega\mid U$. A larger $k$ is an explicit consistency failure, not a stronger reported result.

In particular, if the *actual* new decomposition is $U=f^2$ with $\deg f=60$, and the exact complete residual modulo $f$ has corank 2, the full lower certificate closes there. No calculation modulo $f^2$ is needed.

## 3. Reducible support and genuinely unresolved precision

A reducible $f$ is not assumed to define a field. If no entry is a unit but some entry has a proper nonconstant gcd $g$ with $f$, the source splits
$$
f=g h,\qquad (g,h)=1.
$$
Both child branches retain the whole current matrix reduced modulo the appropriate child power, all earlier paid valuation, and their exact original operations. Their product coverage is checked. A unit selected on the parent remains a unit on either child.

If the first residual corank $k$ is positive but smaller than the upper exponent $e$, the source constructs the original matrix at the genuinely new precision $f^e$. It replays the saved **row and column positions** of the first profile, recomputing and verifying their inverses and Schur products at this higher precision; it does not rerun a field-profile search or old determinant.

After these unit eliminations, all residual entries are exactly divisible by $f$. Dividing the whole $m\times n$ residual by $f$ adds $n$ to the maximal-minor valuation. Further unit Schur pivots, coprime splits, and full $f$-divisions continue until either all columns exit or the cumulative lower valuation reaches $e$.

Precision $f^e$ suffices: after $l$ whole divisions, the available entry precision is $f^{e-l}$ and the already removed maximal-minor valuation is at least $l$. Thus omitted terms cannot change a total valuation below $e$. If the cumulative lower bound reaches $e$, the parent upper certificate gives equality even if some directions have not individually exited.

Each completed branch produces an exact common exponent on its squarefree support. The final source verifies
$$
\prod_{\text{closed }b} f_b^{e_b}=U_{\mathrm{monic}},
\qquad
\Omega_{\mathrm{actual}}=\prod_{\text{closed }b}f_b^{d_b},
\qquad
\Omega_{\mathrm{actual}}\mid U.
$$
All upper support must be covered, and every branch must be closed, before the complete-gcd gate is true.

## 4. Actual source correspondence and scope

The parent core reduction already contains the original source and projection identities. This consumer locks its exact bytes, payload, and logical matrix SHA256, then independently repeats the 1232 constant row-normalization identities. All further computations concern that full original core.

Unit Schur operations preserve the local maximal-minor ideal. Whole residual division accounts for its valuation by the current number of columns. These statements apply to rectangular matrices, so retaining 56 original rows at entry and every nonpivot row thereafter is essential. A single selected square's rank would not provide this lower certificate.

If completed, the output is the exact outside maximal-minor gcd of the original core. It can be nonconstant. This step does not by itself assert membership of the nine original targets or identify the full original matrix's gcd on the already inverted support.

## 5. CLI, budget, and exact continuation

~~~text
python3 {scripts}/2026-11-15-r150-complete-original56-local-outside-gcd-789f.py
  --upper-source {scripts}/2026-11-15-r150-original-three-minor-determinant-upper-789f.py
  --core-source {scripts}/2026-11-15-r150-original-global-projection-polynomial-core-789f.py
  --parent-checkpoints {work}/original-global-projection-polynomial/checkpoints
  --upper-out {work}/original-three-minor-determinant-upper
  --out {work}/complete-original56-local-outside-gcd
  --remaining-seconds 180
  --memory-mib 2048
~~~

Shared mathematical budget: 180 seconds / 2048 MiB. Outer deadline: 240 seconds. No compiler, installation, or extra Python dependency is required.

The two-slot checkpoint stores the complete active matrices, factor branches, valuation offsets, source-coordinate permutations, original profile positions, and exact operations. A pending pivot does not modify the previous matrix. A complete unit pivot, factor split, higher-precision preparation/replay, or whole-factor division is committed atomically. Bindings include both source programs and every immutable actual input; paths, time, and memory are excluded so the same code/out can continue under a later explicit budget.

The independent tiny test uses all three $2\times2$ minors of a $3\times2$ matrix with reducible support. It forces both a proper support split and a higher-precision division, comparing the result with the direct gcd of the three exact minors. A second check deliberately interrupts a pending pivot and confirms that its input matrix is unchanged. These checks are executed only in the real job; this source was generated and statically reviewed without local execution or AST parsing.

The first real Python parse is in the queued Actions job. The public python-flint 0.9.0 scalar APIs used here are documented at
https://python-flint.readthedocs.io/en/latest/fmpq_poly.html .
Extended-gcd output is not trusted by tuple position alone: the returned Bezout identity and the modular inverse are both verified.

## 6. Outputs and completion gates

Small receipt:
`{work}/complete-original56-local-outside-gcd/complete-original56-outside-gcd-receipt.json`.

Temporary complete coefficient/source certificate:
`{work}/complete-original56-local-outside-gcd/complete-original56-outside-gcd.json.gz`.

The completed status requires all of:

- `completeOriginalOutsideGcdComputed=true`;
- `allOriginal56RowsCertified=true`;
- `allSupportBranchesClosed=true`;
- exact final support coverage and divisibility identities.

The receipt separately reports whether the actual gcd equals $U$ and whether it is 1. A timeout is `budget-checkpoint` with exit 75 and the last whole transaction; a failed identity is `failed`. Neither is a completed gcd.

Only small source/parameter/run/hash records are published. All coefficient arrays and operation certificates remain temporary in this job. The receipt retains bounded event summaries and hashes of complete branch summaries to stay below the small-text publication limit without deleting the exact temporary state.
