# Request104: ordinary removal of regenerable notes payloads

Status: repository bookkeeping; no scientific computation or acceptance decision.

- Actions run: 43682924785, attempt 1.
- Script SHA-256: 2465b3dd0e50acfc63b026e7fd73cd15d0c58e401fb925b9d47974b2e31d014c.
- Exact selector source SHA-256: bb5108640323cbd61fefa933a463f05699709709bbfde2ab7407fd6ec491a669.
- Request/recipe SHA-256: 078a1297f8d4c1c259c0f89f1c55e6af419200ca4319951532d25708a94fba03.
- Pinned historical commit: 52704ecdfc84f1d67c8a3cf6233d910f46582844.
- Pinned notes tree: 3832eb52ca0b5414ab761a47fd6774497695b431.
- Planning HEAD: 2cf540ca1c273724596288484394bb9ca49042d1.
- Root README blob: 74c08a36f6c997d0bc1e64a7956b42276f5fa5d7.
- Topic README blob: bff8aea253a9e6a7a4fac28d810ac454c5499fec.

## Exact deletion scope

The selector preserves Markdown, code, named parameters, manifests/identity records
and every unclassified JSON. Only the pinned tree's exact path + mode + blob OID
matches are removed from the current index. A changed or newly introduced file
is not inferred to be deletable from its name.

| Scope at the planning HEAD | Files | Bytes |
|---|---:|---:|
| Complete topic before this deletion | 16254 | 2810721669 |
| Exact current matches selected for deletion | 8184 | 2641928364 |
| Projected topic before adding this small note | 8070 | 168793305 |

- Already absent candidates: 0.
- Changed candidates retained: 0.
- Pinned deletion ledger SHA-256: 7b725628c3fb394d2d22f0fe7cbac28b7238bfac0d13a06227b1481804f450f0.
- Current matching ledger SHA-256: 7b725628c3fb394d2d22f0fe7cbac28b7238bfac0d13a06227b1481804f450f0.
- Current matching NUL path list SHA-256: 289ac88afec320e42045f1928b4112a625e7dca70ff35bbf1c5fd7ede0371625.

The large metadata ledger and path list are generated only in runner temporary
storage. Neither is committed or uploaded. The committed selector, parameters,
historical tree and hashes regenerate the exact list. Sizes come from GitHub
Git Tree metadata; Git matching uses ls-tree -r -z, without -l or data reads.

## Input continuity and remaining scope

The already declared original-input bootstrap commit remains 8bd267107cc8710d371f3b62c02986655ac965b0.
Request101 and subsequent literal-recipe continuations can restore their original
accepted/prepared/zero-anchor bytes from that history and verify their old SHA-256.
T112-config.json and all computations/source-dependencies.json/public78 code remain.
No historical commit is rewritten and no Release is created.

This conservative pass retains unknown JSON and does not claim to have classified
every historical small file under Rule15. It does not create a scientific gate.
Any later source/parameter change is independent of this metadata-only deletion.

The planning counts above are tied to the stated HEAD; the run's final compact
stdout records the actual post-push topic size after any concurrent rebase.
