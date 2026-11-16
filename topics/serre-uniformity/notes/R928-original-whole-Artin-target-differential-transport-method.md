# R928 execution method: eight numerator derivatives and the original whole-Artin differential transport

## 1. Scope and bound proofs

This is the execution contract for the independent leaf in R922, Sections 9–10. Its mathematical proof is the final file
`results/R922-original-bounded-connection-numerators-and-whole-Hecke-evaluation.md`,
SHA-256 `75e0e04e986203598b556403b4ea8eec3706da838e934ae11810c5abda569731`.
The original correspondence and whole-Artin conventions remain those of R873, R882 and R885; the completed derivative source is R919 and its differential-trace convention is R915.

This execution does not require the new R922 polynomial multiplier or the R926 seven numerator outputs. It creates the eight missing derivatives of the original numerator $K$, the complete quotient derivative of $V$, the actual target values of $g,h$, and the original differential-frame ratio $J$ at the existing full source fibre $z_s=0$. It does not evaluate any of the seven connections or produce a height.

All new arithmetic runs only in the public repository Actions. The standard-library wrapper does byte, source, schema and shape checks only. It neither imports the mathematical core nor executes FLINT arithmetic.

## 2. The actual completed source

The direct producer is R919:

| Item | Actual identity |
|---|---|
| Run | `43904104159` |
| Source commit | `1e0ecf187b6e282226833c6c45c5e94661a0a9b1` |
| Mathematical core SHA | `379083fd253ec82af43d185ddd6aed6f33ca6985d70e9864bab8f0a5ce1ef7ee` |
| Artifact | `14245060474`, 19,073,395 bytes |
| ZIP SHA | `863b68d79df7398937d2e56832dc772ee29c4420999448c5e12a2bb57017fa82` |
| Configuration SHA | `cb2e457199bc9856e16fbebcfc1cfecbb0a94388bbee274e65047499ea0e3ede` |
| Complete certificate | 17,249 bytes, `c5b5a3a4f2a7b221d1b10bfbbc4a8f092690cbdeb30f83cc36135d23c91608ca` |
| Full output manifest | 11,229 bytes, `3caecf7914afb5763ada21ae04300456bf99f483e3755e03cca6f3f956140ed3` |
| Existing input carrier | 14,612,930 bytes, `fb4af55fd04a6eef10029ef913953e07c3bd9d40c798a31c58774a7886620813` |

The source is already complete. A null `sources.R919.files` in the public request means deterministic expansion of the selected file specifications from that pinned manifest; it is not a pending mathematical source. The wrapper writes the expanded configuration before starting the core.

R919 owns the 33 completed blocks of derivatives of the original 2058 coefficient-basis functions, the nine $\delta P_i$, the complete $\dot U$, and its exact expression DAG. Its retained input carrier contains the already bound R885 whole correspondence and all 272 target normal coordinates, the R882 2058-by-17 coordinates, the original R827 $g,h$ vectors and place, and the R873 exact correspondence DAG. The new carrier preserves those selected files under their original producer groups and configurations. Their bytes and tags are not rewritten.

The full existing 73-member R919 carrier is hashed while read. Only the required original R885/R827/R882/R873 subset is retained in the new carrier. The old R807 leaves and the original 17 Gamma blocks need not be carried forward: their completed derivative consequences are already present in the source-bound R919 stages. No old large producer archive is downloaded for this execution.

The original auxiliary place is
$
\ell=1000000753,\qquad \zeta=549966761,\qquad s=99932770,
\qquad B=3197390.
$
It is not the prime-41 completion.

## 3. The eight new coefficient derivatives

Write the frozen original correspondence exactly as
$
P(U)=\sum_{i=0}^8P_iU^i,\qquad
K(U)=\sum_{i=0}^7K_iU^i,\qquad
V=\frac{K(U)}{P_U(U)}.
$
The last eight R882 coordinate columns, numbered 9 through 16, are coefficients of the numerator $K$; they are not coordinates of $V$.

For each completed R919 derivative block, the new core multiplies its transpose by the corresponding eight columns of the old R882 matrix. The 33 new contributions are immutable atomic stages. Their sum yields $\delta K_0,\ldots,\delta K_7$ in the full 272-dimensional source algebra. No original monomial derivative, Gamma block, normal conversion, original coefficient solve, or one of the nine $\delta P_i$ is recomputed.

All coefficient derivatives are the reductions of the derivation on the original function field, applied before specialization. No derivation on the quotient source algebra is invented.

## 4. The complete quotient rule

Let
$
A_0=\mathbf F_\ell[X]/(\chi_0),\qquad
E=A_0[U]/(P/a_8),\qquad
\mathscr D=P_U(U).
$
The dimensions remain 272 and $8\cdot272=2176$, with every factor and its full nilpotent multiplicity.

The original R885 inverse of $\mathscr D$ and the original R919
$\dot U=-\delta P(U)\mathscr D^{-1}$ are read unchanged. The new core forms only the formal $U$-derivatives
$
K_U,\qquad \delta P_U=(\delta P)_U,\qquad P_{UU},
$
and the expressions
$
\Delta_K=\delta K(U)-V\delta P_U(U),\qquad
\mathcal H_K=K_U(U)-VP_{UU}(U),
$
$
\dot V=\mathscr D^{-1}\bigl(\Delta_K+\mathcal H_K\dot U\bigr).
$
The complete acceptance equation is
$
\mathscr D\dot V+
V\bigl(\delta P_U+P_{UU}\dot U\bigr)
=\delta K+K_U\dot U.
$
The core compares every one of the 2176 coordinates. It saves both sides, $\Delta_K,\mathcal H_K,\dot V$, the new derivative references and all original inverse references.

This step does not rename $K/P_U$ to $K$, differentiate only the numerator, or compute a new $P_U^{-1}$.

## 5. Actual target $g,h$ and the frame

The original R827 vectors have four coefficient rows each:
$
g=\sum_{k=0}^3z^k\sum_{i=0}^{271}g_{ki}\beta_i,\qquad
h=\sum_{k=0}^3z^k\sum_{i=0}^{271}h_{ki}\beta_i.
$
The core reads the completed R885 values of every
$\beta_i(U,V)\in E$. It contracts each original block of 16 target coordinates with those exact reduced coefficient rows and then substitutes the actual $U$ by Horner evaluation. This produces $g_t,h_t\in E$. The source-specialized values at $z_s=0$ cannot replace these target evaluations.

The fixed trial sequence is $t=0,1,\ldots,2176$. The first request asks for its first eight terms; the same mathematical tag permits a larger prefix. For each tried value the core retains the full norm/Bézout witness for
$
\ell_t=g_t+t h_t.
$
The frozen R885 algebra helper computes the rank-eight characteristic polynomial without division, proves the characteristic identity, tests the full norm against the original $\chi_0$, and multiplies any inverse back in all of $E$. A nonunit trial retains its whole-algebra witness. No factor, residue point or nilpotent layer is removed.

At the first unit trial set
$
J=(\dot U+t\dot V)\ell_t^{-1}.
$
Completion requires both equations
$
Jg_t=\dot U,\qquad Jh_t=\dot V
$
in all 2176 coordinates. By the bound R922 proof, this is the original frame ratio
$
J=\pi_t^*\nu/\pi_s^*\nu.
$
The core does not invert $J$ and does not claim that $J$ is a unit. Its unit status is unnecessary for the subsequent differential trace.

A failed finite prefix is an honest incomplete endpoint. It does not prove failure of the exact correspondence or of the original differential. Existing contraction blocks and failed trials are reused if the prefix or time budget is increased.

## 6. Output identity, stages and continuation

The mathematical tag binds the new core SHA, the unchanged algebra-helper SHA, this method, the original proof hashes, all selected source identities and byte specifications, all mathematical input references, and the fixed strategy. Time budget and the requested number of frame trials do not enter the tag.

All new mathematical stages are `R928-*.json.gz`. The current checkpoint is explicitly incomplete. The immutable stage manifest is named from its actual content. It lists only complete stages; it is not itself a recursive member. The final certificate refers to the actual stage manifest and current checkpoint.

The main outputs are:

- `eight-original-delta-K-coefficients`: eight full source-algebra values and the 33 new contraction references.
- `whole-quotient-derivative`: full quotient-rule data and both equal 2176-coordinate sides.
- `whole-target-g-h`: actual full target values, with all 17 source blocks.
- `complete-target-differential-transport`: the selected integer, complete unit witness, $J$, and both multiplied-back products.
- `original-characteristic-zero-target-transport-DAG`: the exact source-bound function-field expression, separately from its finite-place values.

The complete endpoint is
`p41-original-whole-Artin-target-differential-transport-certificate.json`,
with result `R928-original-whole-Artin-target-differential-transport`.

Restoration requires the same core, helper and mathematical tag. It preserves all completed source and output bytes. A historical incomplete final certificate does not overwrite a newer current checkpoint. If the outer timeout leaves no core receipt, the wrapper accepts only the explicit incomplete exit-124 outer-timeout case and does not manufacture a receipt.

## 7. Frames and remaining boundaries

The exact expression DAG retains the actual R873 source/target orientation, the canonical dual-7 transport of both determinant frames, scalar 7, the diamond action, the original minus-3 descent, and the original $\kappa,\nu$ constants. Nothing is identified merely by self-adjointness, and no endpoint calibration scalar is evaluated here.

The actual arrays are at the one specified auxiliary place. They are not characteristic-zero expansions or prime-41 balls. The exact characteristic-zero output is the original source-bound expression. Seven connection numerator evaluations, the five Picard combinations, endpoint normalization, non-$p$ contributions, Poincare periods and heights all remain explicitly false. Their later consumption is a separate task.
