# Storage C: exact frozen text recovery index

Date: 2026-11-09. Author/session: db6f / coupled_prefix.

## Status and purpose

The executor became unavailable after the author completed the Storage C v4 pure check. This index preserves the exact text of the six frozen C source versions, three frozen textual transformation ledgers, and the final author checker. These are recovery copies under `notes/`, each smaller than 100 KB. No runtime script, old frozen source, mathematical data file, HANDOFF, LOG, or result was changed by this recovery. No executable producer, mathematical consumer, BVP, DN, RK, mesh export, or continuous certification was run during recovery.

All ten copied files were recreated from retained complete text, checked against the previously recorded SHA256 and byte count, saved only after the new path returned NOT_FOUND, and fetched back at the resulting immutable commit. Every fetched text was compared with the complete supplied text. The table below records those actual commits and Git blob identities. The total is 250129 UTF-8 bytes; the largest individual copy is 48711 bytes.

The six C sources and three transformation ledgers were recovered by applying the complete retained textual transformations to the exact frozen old textual sources. The v4 checker was recovered from its retained complete text. Matching the previously recorded full SHA256 is the identity test: these are not guessed substitutes or a new implementation.

## Scope of existing verification

The earlier A foundation and B consumer batches already had full independent review. Their original reports and source versions remain unchanged.

The original author's Storage C final check was `db6f-prefix-check-storage-gates-v4.py`, SHA256 `59c250c55cfe731753f0ee1639728dd4d8b67fca0134e480ebd9f7ca1e55426c`. The actual executor sequence was start receipt `e21d05`, session `68045`, then completion receipt `88ff38` with exit code 0. The recorded output report was `notes/2026-11-09-db6f-prefix-storage-gates-check-v4.json`, SHA256 `f1daab8418dd20e722bfabf4688b813dc358300eed323dd04189747f973f380c`. The report's full bytes have not been recovered here; its old hash and the actual author execution receipt are preserved as prior evidence, not replaced with a reconstructed report.

That author check covered the declared complete-source transformations, 34 bound inputs, 12 negative cases, the real frozen old M12 storage entry, and the eight-item storage ledger after relocation of its reported paths. Its fresh isolated Python child did not import NumPy or SciPy. It did not instantiate mathematical classes or run new mathematical computations. The preceding v3 checker stopped with exit code 1 at a textual inverse-count ambiguity before storage testing; v4 changed that source-comparison step to full forward textual replay. This historical failed check is not erased.

The independent reviewer had read the C core sources and the v2/v3 changes, and independently reproduced the v2 relocation rejection before the executor became unavailable. The reviewer had not then completed an independent execution of the final v4 checker. Saving these exact text copies does not discharge that independent replay. **Storage C is not declared fully closed or independently replayed by this index.** No new M14 geometry or metric/curvature certificate is claimed.

## Recovery files and immutable identities

All source paths in the `Original path` field are relative to the repository root. Every `Recovery path` is a new text-only file in this topic's `notes/` directory. A `.py.txt` suffix intentionally makes the copy a recovery artifact rather than an installed executable.

### 1. db6f-prefix-angular-metric-storage.py

- Original path: `topics/visible-flexible-closed-surface/scripts/db6f-prefix-angular-metric-storage.py`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-db6f-prefix-angular-metric-storage.py.txt`
- UTF-8 bytes: 24286
- SHA256: `2f24cdf9b9649a5ecd34bdbbdabaf294f1fb985288578b54217a6143c98e902c`
- Recovery commit: `d32e71935164e190fe7d1c63051468f244363263`
- Git blob: `7055624885340f1d8d38ff8933d96945a5fa440e`
- Immutable-commit full-text readback: exact.

### 2. db6f-prefix-export-closed-mesh-storage.py

- Original path: `topics/visible-flexible-closed-surface/scripts/db6f-prefix-export-closed-mesh-storage.py`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-db6f-prefix-export-closed-mesh-storage.py.txt`
- UTF-8 bytes: 25497
- SHA256: `d776e41ef75741be0d5d44a8156d2c71a70ad016ef3678605d718a32ba7684d1`
- Recovery commit: `31920c0c68ca98a180f9b67ec070bc6d046a6963`
- Git blob: `582eef9d4a1360b775927f853680179153cd8808`
- Immutable-commit full-text readback: exact.

### 3. db6f-prefix-review-closed-mesh-storage.py

- Original path: `topics/visible-flexible-closed-surface/scripts/db6f-prefix-review-closed-mesh-storage.py`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-db6f-prefix-review-closed-mesh-storage.py.txt`
- UTF-8 bytes: 11115
- SHA256: `698e8b0528ffa7b1bbe1bc84c574079f60261156f1d3a6ddae048af0f9c0c479`
- Recovery commit: `35ba1b0a59361e663709b39119bf68d2be5ad373`
- Git blob: `3fc6afac2ac13c34c7dbc12076a980dd101bb7db`
- Immutable-commit full-text readback: exact.

### 4. db6f-prefix-terminal-error-storage.py

- Original path: `topics/visible-flexible-closed-surface/scripts/db6f-prefix-terminal-error-storage.py`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-db6f-prefix-terminal-error-storage.py.txt`
- UTF-8 bytes: 45587
- SHA256: `809cc7ab61903f11847653fda018506f7c2bed38a7501007909200eb0bf69584`
- Recovery commit: `b678a0dcb1132b921bcd78d98f9ac222ce788378`
- Git blob: `20cfc781ce1c4a1251bac1aa9b4168ecfa484849`
- Immutable-commit full-text readback: exact.

### 5. db6f-prefix-terminal-error-storage-v2.py

- Original path: `topics/visible-flexible-closed-surface/scripts/db6f-prefix-terminal-error-storage-v2.py`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-db6f-prefix-terminal-error-storage-v2.py.txt`
- UTF-8 bytes: 48456
- SHA256: `a00f8210d561983e9d137a848cb7b582e33de8450c0b70497e3933080c297aa1`
- Recovery commit: `b6405487f0222a161ff6d51f03658767a934be50`
- Git blob: `9e2b7bcb3a93109c2beffe88e44f0b9fb3b1bbf9`
- Immutable-commit full-text readback: exact.

### 6. db6f-prefix-terminal-error-storage-v3.py

- Original path: `topics/visible-flexible-closed-surface/scripts/db6f-prefix-terminal-error-storage-v3.py`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-db6f-prefix-terminal-error-storage-v3.py.txt`
- UTF-8 bytes: 48711
- SHA256: `8db94c71a9035f2f977daea9c315b669bce4c20800f80e7886b77c66af6f7ed7`
- Recovery commit: `72ca9a7b743842f1aa4287e987efb66fdaea7dfd`
- Git blob: `430fee2a7109af8fa30f4ab519e856bba6fa25ba`
- Immutable-commit full-text readback: exact.

### 7. 2026-11-09-db6f-prefix-storage-gates-transformations.json

- Original path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-gates-transformations.json`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-transformations-1.json.txt`
- UTF-8 bytes: 24049
- SHA256: `0417ac80883dda492618f8535a06ce0eaab230decf0eec4751d2b8c41b25dd88`
- Recovery commit: `4d5a424ad7897accfccc6631bf265bfc481b003d`
- Git blob: `0c6832cddec03bfbe157350fa4735afde8afeafd`
- Immutable-commit full-text readback: exact.

### 8. 2026-11-09-db6f-prefix-storage-terminal-v2-transformations.json

- Original path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-terminal-v2-transformations.json`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-transformations-2.json.txt`
- UTF-8 bytes: 5307
- SHA256: `82bbb53a65803c1f2531a6d2544f82d86f820d458acfeb5494f07f3d7b7f3d69`
- Recovery commit: `def3ba1e1f174fae76bc8af7834aab151adee1c3`
- Git blob: `509d8c79a3c7970103277e622b6880d2c86f3e1c`
- Immutable-commit full-text readback: exact.

### 9. 2026-11-09-db6f-prefix-storage-terminal-v3-transformations.json

- Original path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-terminal-v3-transformations.json`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-transformations-3.json.txt`
- UTF-8 bytes: 3146
- SHA256: `4299872c6189de869d137682ace26eee965fdabc0af01a2c47a25342bab1e336`
- Recovery commit: `371a83946b2f4d06d693ba51749afa13ceebf9ac`
- Git blob: `62912eb0232f8dc855560a138ebe019063f1a901`
- Immutable-commit full-text readback: exact.

### 10. db6f-prefix-check-storage-gates-v4.py

- Original path: `topics/visible-flexible-closed-surface/scripts/db6f-prefix-check-storage-gates-v4.py`
- Recovery path: `topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-storage-c-recovered-db6f-prefix-check-storage-gates-v4.py.txt`
- UTF-8 bytes: 13975
- SHA256: `59c250c55cfe731753f0ee1639728dd4d8b67fca0134e480ebd9f7ca1e55426c`
- Recovery commit: `37395f9e0273251e37db86e886dd59e5d0363a6e`
- Git blob: `7f9b450539fd1e5e4e4ccca355f7e29782bad784`
- Immutable-commit full-text readback: exact.

## Mathematical and source-identity boundaries

The final terminal version is v3, SHA256 `8db94c71a9035f2f977daea9c315b669bce4c20800f80e7886b77c66af6f7ed7`; v1 and v2 are retained historical source identities. The v3 relocation repair first compares the reported basename/byte-count/SHA256 multiset with the actual verified storage closure, then resolves the matching actual local files. It does not widen the old tail source gates or the generic old file-resolution policy.

The new prefix source family and its storage closure are explicit. The original tail sources, exact-target transfer semantics, same-metric requirements, full-coverage requirements, scalar thresholds, and final source provenance remain distinct. The additional stored representation does not lower the Hermite mode count or change the mathematical map. Existing old-graph storage-equivalence checks do not certify any future new graph.

## Safe continuation

1. Obtain each recovery copy from its recorded immutable commit and recompute its SHA256 and UTF-8 byte count.
2. If the original intended source already exists, compare its full bytes with the frozen identity. Do not overwrite an existing frozen source on a mismatch.
3. If an intended source is absent and the research owner authorizes restoration, restore only the exactly matching bytes at the listed intended path. Keep this index and the historical versions.
4. Reconstruct the expected local dependency closure from the original frozen A/B/C bindings. A text backup alone does not supply any missing old mathematical data file.
5. Finish the independent final C source/checker review and its actual permitted pure-storage replay when an executor is available. Do not substitute the author's recorded exit code or the present readback for that review.
6. Only after those requirements and the future candidate's own actual identities are satisfied may the corresponding new producer/consumer entry be considered for an authorized run.

The separate recovery-status note is `notes/2026-11-09-db6f-prefix-storage-c-interruption-recovery.md`, SHA256 `47a48712349310d50108f47df8cda747db115b61b901f419e7c7332b4aaed58e`. It records the interruption boundary. Neither that note nor this index assigns a cause to the unavailable executor or fabricates a missing job exit code.
