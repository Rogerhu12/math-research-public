# Actual request44: original request42 inputs verified, summary transport failed

## Actual receipt and scope

The read-only receipt job in [public Actions run 43627297724](https://github.com/Rogerhu12/math-research-public/actions/runs/43627297724) used source commit `d07eeb32ec7e72f8982b0c8f3c9352e4a0e34e1f`. Its job was `132545953652`. The run was created at 2026-11-14 18:33:52 UTC and completed at 18:34:28 UTC. This note concerns only the request42 metadata reader; the independent original stage43 field reader has a separate receipt.

The workflow and job report success, but the request42 reader's actual log says `return_code: 1`, `receipt_summary_completed: false`, and `failed_stage: "summary-transport-size"`. The workflow expressly uses `continue-on-error: true` on that reader step. Thus the Actions step conclusion does not establish that its intended summary was produced.

The numerical request42 computation was not rerun. This reader performed file hashing, JSON reading, and metadata copying only. It did not evaluate any model, matrix action, norm, extremum, native tail, or boundary problem.

## Preserved small evidence

The publisher actually preserved both of these original files:

| File | Bytes | SHA256 |
| --- | ---: | --- |
| [request42-reader.log](public-actions-43627297724-1-receipts/request42-reader.log) | 287 | `6cb896bc82cf705cee31d05aeee64dd21abea44a9201dfecbc8604872c9643c3` |
| [request42-receipt-summary-v2.json](public-actions-43627297724-1-receipts/request42-receipt-summary-v2.json) | 9528 | `e2581a010ed8792626d0949777d63af71c7be99315f15265995fea207433361d` |

These text bytes were independently hashed after retrieval and agree with the actual [publication ledger](public-actions-43627297724-1-receipts/publication.json). The ledger was recorded at 18:34:22.428368 UTC. This is a small-text identity check, not an independent audit of the original request42 ZIP or its large arrays.

The actual v2 failure receipt gives:

- `completed: false`;
- `scientific_evaluations: 0`;
- `failed_stage: "summary-transport-size"`;
- `bytes_before_transport_abbreviation: 206693`;
- `original_scientific_outputs_unmodified: true`.

All seven pinned original files existed and passed their full SHA256 checks in the public Actions reader:

| Original request42 file | Original bytes | SHA256 |
| --- | ---: | --- |
| `twelve-query-qr-warm/full-H-result.json.gz` | 1328308 | `0e57a7c02c2f1ceb85538ae5e0b33db532ac2139b17caf730ed90c1926a29884` |
| `twelve-query-qr-warm/full-H-versus-C-comparison.json` | 13430 | `5fc48cd7068d8b0b6f2f5e61bf673131ed6ed50195cac12cc7c957433db2a008` |
| `twelve-query-qr-warm/full-H-final-selected-evidence.json` | 13013 | `aa8f3da16825c34c3ae1492f6e890bad0bd593b427784e247c122dc7a427d79b` |
| `twelve-query-qr-warm/model-000.json` | 246935 | `fe7523e69982312d339d0bf0b99626cb266ff6cb5b1b7dae648a2c1afdb47f17` |
| `twelve-query-qr-warm/driver-status.json` | 528261 | `26272c6ca8e1a5ba1db2bb96cc749dca74cddc025bcd1a5a9864f149d4a16d04` |
| `twelve-query-qr-warm/warm-001.json.gz` | 4740550 | `3dd623e90edb97ff113bebddd09445d64b916626a8fb1821fd35e69beabdc317` |
| `physical-response/response-check.json` | 321173 | `346a4f6a193b682f747c96dfb4408c62c17d4c4db850e8700717475d10db22d4` |

## What failed and what remains unreported

The actual preserved structures show that `full-H-result.json.gz` has the expected top-level `report`, `active_history`, and `last_subspace` objects. The active history has 33 entries. The last subspace has `x`, `mu`, `coefficients`, and `report`. The helper report contains the intended stop, budget, work-count, internal repair, and posterior fields. There is no observed schema mismatch or input SHA failure.

The v2 implementation still copied the whole final active-history entry using the v1 recursive `slim` helper. That helper retains nested lists of up to 64 entries at each level, so it can retain complete small Gram matrices and other nested report trees. The v2 also retained an entire producer subtree. Its final size guard then replaced the oversized 206,693-byte summary with the 9528-byte failure receipt. Consequently, the discarded summary's numerical fields are not established by this receipt.

The source inspection identifies a concrete overinclusive serialization mechanism. It does not assign a measured byte contribution to an individual subtree, because no such per-section sizes were saved. Nor does this v2 result independently establish the exact cause of the missing v1 output in request43: no v1 exception log is available in this receipt. The earlier inference that a successful request43 step meant a successful summary is withdrawn.

In particular, this note does **not** fill the outstanding request42 helper details by guessing: the precise internal stop reason, last unrepaired all-row violations, and internal radial factor still need to be copied from the original saved report. The already published [actual request42 note](2026-11-14-actual-request42-complete-QR-32-row-warm.md) retains its stated limits.

## Concrete receipt-only correction

A separate v3 reader will use explicit scalar paths for the helper summary, the last active stage, the last subspace diagnostics, the actual radial repair, the original nonlinear trials, status, and FD. It will not recursively copy complete producer, Gram, basis, coordinate, or field trees into the public scalar summary.

The full derived metadata document will be preserved as an artifact before producing bounded public sections. If a public section needs splitting, its original selected scalars will be retained in separate small text parts; a size limit will not erase previously read numerical metadata. Input and producer SHA checks remain unchanged. This is only a readback correction and introduces no scientific computation or acceptance gate.

The independent condensed-QP experiment uses separately frozen numerical sources and is unaffected by this receipt transport failure.
