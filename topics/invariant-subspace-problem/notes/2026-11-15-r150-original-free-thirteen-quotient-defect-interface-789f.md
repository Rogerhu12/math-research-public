# R150 original free-thirteen quotient-defect consumer interface

Author: AI (ChatGPT / literature_audit), 2026-11-15 UTC.

## Frozen source

Repository: Rogerhu12/math-research-public.

Path: topics/invariant-subspace-problem/notes/2026-11-15-r150-original-free-thirteen-quotient-defect-789f.py

Git blob: e7b77af3167e5c0e8df83b372a885e092ce43f2c

Bytes: 27836

SHA256: 7f092c2327864ed01d93095ae8f44af5bb42022f262fabbe5d5cd3801c2385b6

The source is a standalone Python 3 consumer requiring the already available python-flint 0.9.0. It imports no historical generator and invokes no network operation. Its only mathematical input is the previously verified original polynomial kernel phase. Local static parsing was attempted but the exec server was unavailable; no new mathematical calculation was run while freezing this source.

## Input identities

The small parent receipt may be either of the following exact files.

| Form | Bytes | SHA256 |
|---|---:|---|
| Published outer receipt | 11075 | 7db7d2437583105a9bb2474612cb5b4001989f7911ca79bd22992d025a056aa2 |
| Original raw mathematical receipt | 6068 | 354d34109b5b1a9593b038a69c7ad59e6eaa9ddd345474797408f05117c9639b |

Published path:

    topics/invariant-subspace-problem/notes/r150-source-kernel-session-789f/43756208221-original-global-projection-polynomial-core.json

Parent source SHA256:

    727175cf485a8ba5b5146a4cc6e749962e109c9e42265a2dd45f58cecdf933fb

Parent semantic binding:

    ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba

The checkpoint directory must contain this one exact temporary file:

    free-thirteen-kernel-70b27882aced10d9de363b30056d93491860db2b102d3750c949659a7ad11fc0.json.gz

It is 157898 bytes, SHA256:

    b4cd026450d301328d4273ca7256dd9d8ee645576fcc5a5118aecd99a4fc2c51

Uncompressed payload SHA256:

    70b27882aced10d9de363b30056d93491860db2b102d3750c949659a7ad11fc0

Canonical 155 by 13 polynomial-matrix SHA256:

    0094105c15f99860016767a662e27b7b60ddfb04b085f044f50bacfe694aabe6

No full polynomial core, Hermite candidate, normal-form data, high source chain, or large prior checkpoint is opened.

## Command and budget

A suggested first run is 120 seconds and 1024 MiB, with an outer timeout of 150 seconds:

    python SCRIPT \
      --core-receipt PARENT_RECEIPT \
      --checkpoint-dir WORK/original-global-projection-polynomial/checkpoints \
      --out WORK/original-free-thirteen-J \
      --remaining-seconds 120 \
      --memory-mib 1024

Only the path placeholder SCRIPT is the newly frozen source. The original checkpoint directory is read-only. All generated polynomial coefficients and resumable gcd states go under the new output directory.

The exact same source and output directory can be resumed with a larger remaining time budget. The semantic binding includes the source SHA256 and all original polynomial input identities, but does not include the budget. Completed gcd steps are restored; the paid original phase is rechecked. The source has no assertion about the desired value of the final defect dimension.

## Mathematics performed

The consumer verifies every entry of the original 155 by 13 matrix against the ten-axis and three-row support decomposition. In particular, all ten pure columns have zero entries off their own axes, and the remaining three columns vanish on those axes. Every original coefficient denominator must be a unit at 31.

The residual complete three-row presentation contains 30 original target columns. The exact complete maximal-minor gcd is evaluated through the 211-expression formula in the companion proof, separately over Q[s] and F31[s]. Neither field's axial gcd is substituted for the other. Every final gcd is checked to divide all 211 expressions.

The monic rational characteristic polynomial must have 31-integral coefficients and preserve its full degree after reduction. Exact division of the finite-field characteristic by that reduced rational characteristic gives the characteristic polynomial of J. All seven residue factors are checked to be irreducible and pairwise coprime. The identity E8 mod31 = 5(s-1)(s-2)E6 is checked, so all rational-to-residue collisions are retained.

The independent companion proof is:

    results/R150-appendix-coefficient-prime-quotient-defect-from-original-thirteen-free-kernels.md

Git blob 1c92d74d3c0267dfc0d480fa91e4a0d5a6b82825, 10843 bytes, SHA256 aaafb94b4fe17f99afce45af02a91b4ddc0bf8e7e5ea50b18091df3f47417f0a.

## Outputs and continuation

The small receipt is:

    WORK/original-free-thirteen-J/j-quotient-defect-receipt.json

It is also printed in full on stdout. Required content is under parameters, including the exact primary table, both complete gcd summaries, input identities, and the complete checkpoint inventory.

Status completed is the only status that reports the exact final J characteristic. A budget-checkpoint status exits with code 75, preserves the actual processed prefix, and is not a negative mathematical result. The session must not treat it as a completed prerequisite; resume the same binding before dependent work. A failed status reports errorType and errorMessage under parameters and makes no final J claim.

Temporary checkpoints are immutable JSON files named by their complete SHA256. The manifest is updated atomically only after the payload exists. Their matrix or polynomial coefficients are never an instruction to upload or commit recomputable data. Publication should retain only this source, its parameters, run identity, and the small mathematical receipt.

The completed calculation determines J and its primary lengths. It does not alone assert a new original target membership result or a complete coefficient-prime Smith spectrum. Those consequences require the separately proved original exact sequence and divided-source bounds.
