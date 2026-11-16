# R133 — exact two-file whitelist for old diagnostic report cleanup

2026-11-16 UTC. This whitelist is based on the completed immutable metadata audit [43777745624/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43777745624). It covers exactly the two report JSON files in Section 1. Preparing this whitelist did not delete a file, execute a producer or perform scientific arithmetic.

## 1. The complete deletion set and immutable restoration

Restore **each complete file at its identical path** from commit
`b9c7cde9c28a38d9d7db2ad03fcfd3835578ac6b`.

| Exact repository path | Git blob | Bytes | Complete SHA256 |
|---|---|---:|---|
| `topics/visible-flex-exact-nearby/notes/2026-11-13-codazzi-evolution-r0235-n512-floating.json` | `e7fe4210bae462d8360d967534f3425c9e1756e7` | 360313 | `a8db0f022e9aafab96bae1e14bfad2cf49a8f05cf01623a60e90c608b0e39f77` |
| `topics/visible-flex-exact-nearby/notes/2026-11-13-codazzi-evolution-r0235-n1024-floating.json` | `de04339caa70cc10e4c55aaf3e9ea18fdfc719b8` | 360182 | `13faea5738c4100942ff93031b473233c52c258441ef69d347c7c4d6b70acded` |

The exact total is **720495 bytes**. No directory, wildcard, similarly named waist report, endpoint, candidate, input array, source file or failure record belongs to this set. A fresh-tree identity check must still match the above exact blobs before any ordinary Git deletion; this whitelist authorizes no history rewrite or replacement of the original bytes.

## 2. Complete success and scope evidence retained in the small audit

The public [actual-report-metadata.json](old_evolution_report_metadata_ci/run-43777745624-1/actual-report-metadata.json) is Git blob
`42223148049d201f7c64bf97c6a056961efb7feb`, 12428 bytes, SHA256
`c112361798ede90556326b9f8c20f14a185f34ab1d6cba9fd501ed9b10f81168`.

The audit runner read both complete original files from the restoration commit, verified byte length and Git blob SHA1, computed complete SHA256 before decoding, and then retained the original status, exception, source/dependency/object identities, requested and finished intervals, endpoint file identities, diagnostic scope and limitations. This is not a hash of an excerpt.

For each report the actual original fields are:

- `complete=true`, `status="finished"` and `exception=null`;
- `original_success_flag_read_from_report=true` under precisely those three conditions;
- requested and finished radial interval `[0,0.235]`;
- 236 original sampled rows, first radius 0 and last radius 0.235;
- `mean_retained=true` and `original_target_fixed=true`;
- `certified=false` and all three whole-parameter, whole-radial and whole-angular flags false;
- no original NaN or signed Infinity tokens.

The 512 and 1024 angular runs used doubled nonlinear grids 1024 and 2048. Their original limitations explicitly preserve unvalidated floating arithmetic, interpolation and infinite Fourier tails, sampled projection defects, a single exact parameter center, and no cap/regular-mean-return/global closure. Their successful diagnostic completion is therefore not a certified solution.

This audit was itself successful: deployment and checkout `c9f72b1a899e7cf316fa76f3d508bfd63678110e`, natural push attempt 1, job `133007803638`, all nine reported steps successful, terminal update `2026-11-16T00:00:08Z`. It records metadata return code 0, complete true, failure null, and **zero scientific computations, producer calls, old mathematics recomputed, numerical enclosures, arrays, artifacts, Releases and deletions**. Its two true pull/README checks both have empty diffs.

The metadata receipt remains after cleanup, so original success and limitations can be read without retrieving the two large reports. Their complete bytes remain recoverable from Section 1.

## 3. Why these JSON files are report outputs, not endpoint definitions

The original producer is
`topics/visible-flex-exact-nearby/scripts/fourfold_phase_codazzi_evolution_probe.py`,
Git blob `0d3f34154e92282d3876f099585ec3c4438f92ca`,
11127 bytes, SHA256
`2d9e8a9dd185e13c1c506a628f36847fe6180390bca3b60014d7c1beb8a69c36`.

The complete small producer text was read. Its `--out` and `--state` arguments are separate. It writes the computed endpoint with `np.savez_compressed(args.state,...)`, then forms the diagnostic JSON containing that separate endpoint's path and SHA256, and finally writes `args.out`. Neither of the two JSON report files defines the state, original exact object, origin or direction. The audit never imports or executes this producer.

The following distinct endpoint files are explicitly **preserved**:

| Exact repository path | Complete original SHA256 retained by the report |
|---|---|
| `topics/visible-flex-exact-nearby/notes/2026-11-13-codazzi-evolution-r0235-n512-endpoint-floating.npz` | `e49a5141da41c7710cebe152419b34ba0c9ff8aa397bf5710c980148b2af0738` |
| `topics/visible-flex-exact-nearby/notes/2026-11-13-codazzi-evolution-r0235-n1024-endpoint-floating.npz` | `825e9eb6b4c587c41bd39ef36c76f28366993a81af754c120fea9dbcf1081552` |

All source dependencies and exact/native/candidate inputs are preserved. In particular the exact origin and direction arrays, with SHA256 `0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b` and `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`, are not cleanup candidates.

## 4. Small provenance and the separate failed attempt remain

Preserve
`topics/visible-flex-exact-nearby/notes/2026-11-13-R126-Codazzi-candidate-and-diagnostics.md`,
blob `adfe97699fa73cd9ae24d3db8837e4ec3fda7ffa`,
8714 bytes, SHA256
`68acb99affa62507776252d4b6b23d7199ab0442c72f4b8bb561adc50a741b30`.
Its Section 2 is the earlier small account of the same two diagnostic endpoints.

Also preserve the separate failed report
`topics/visible-flex-exact-nearby/notes/2026-11-13-waist-cauchy-evolution-r0235-n512-floating.json`,
blob `c36016198b823966517e3e65b2349e78c73d0231`, 1195 bytes.
That report records a different waist formulation and an incomplete attempt. It is not either of the two successful dealiased report files in Section 1. No status or failure history is relabelled or removed.

## 5. Exact dependency scope checked before proposing cleanup

The held complete SC, HS, WT, KL, WE, DZ/DZ2 and UT input manifests were searched for both exact report basenames: all searches returned zero occurrences. Independent peer checks of the complete current NW, NPK and SEI manifests likewise found neither current nor historical direct pin. The new CEB nine-current-input plan has no occurrence and no history/archive input.

These are checks of the specified actual input manifests, not a claim that no historical prose link exists anywhere. The completed OM manifest deliberately names the two paths at the immutable restoration commit; it remains reproducible after their removal from the current tree. Its preserved small audit source, manifest, workflow and actual receipt are not cleanup candidates.

Only the two exact JSON paths in Section 1 may be removed under this whitelist. Complete mathematical receipts, the exact background and response definitions, original arrays and endpoint states, source files, the small R126 account, all failed-attempt records, and the immutable restoration chain remain intact.
