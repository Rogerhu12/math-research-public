# R133 — actual immutable audit of two old evolution reports

This is a metadata conclusion. The unique natural push run [43777745624/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43777745624) completed successfully. Both immutable old report files state `complete=true`, `status="finished"` and `exception=null`. This audit performs no scientific computation and grants no new analytic or numerical estimate.

## OMA.1. Exact execution and small public receipt

The deployment and actual checkout were `c9f72b1a899e7cf316fa76f3d508bfd63678110e`. GitHub records event `push`, attempt 1, creation `2026-11-15T23:59:33Z` and terminal success `2026-11-16T00:00:08Z`. Job `133007803638` completed all nine reported steps successfully. No workflow dispatch, cancellation, rerun, producer invocation or scientific child was used.

The complete public receipt is [actual-report-metadata.json](../notes/old_evolution_report_metadata_ci/run-43777745624-1/actual-report-metadata.json):

| File identity | Value |
|---|---|
| Git blob | `42223148049d201f7c64bf97c6a056961efb7feb` |
| Complete UTF-8 bytes | `12428` |
| Complete SHA256 | `c112361798ede90556326b9f8c20f14a185f34ab1d6cba9fd501ed9b10f81168` |
| Kind | `actual_immutable_old_evolution_report_metadata_v1` |
| Actual metadata return code | `0` |
| Complete / failure | `true / null` |

The audit ran from `2026-11-15T23:59:57.483002+00:00` to `2026-11-16T00:00:01.704863+00:00`. The complete small receipt was read and its byte length and SHA256 independently checked after publication. No large report body or job log was retrieved through the chat connector.

## OMA.2. Complete immutable restoration identities

Both original report paths below are relative to `topics/visible-flex-exact-nearby/`. Their complete restoration commit is

`b9c7cde9c28a38d9d7db2ad03fcfd3835578ac6b`.

The runner read each file from that exact commit, verified the expected Git blob and byte length, verified the Git blob SHA1 against the complete bytes, and computed SHA256 before JSON metadata extraction.

| Original report | Git blob | Bytes | Complete SHA256 |
|---|---|---:|---|
| `notes/2026-11-13-codazzi-evolution-r0235-n512-floating.json` | `e7fe4210bae462d8360d967534f3425c9e1756e7` | 360313 | `a8db0f022e9aafab96bae1e14bfad2cf49a8f05cf01623a60e90c608b0e39f77` |
| `notes/2026-11-13-codazzi-evolution-r0235-n1024-floating.json` | `de04339caa70cc10e4c55aaf3e9ea18fdfc719b8` | 360182 | `13faea5738c4100942ff93031b473233c52c258441ef69d347c7c4d6b70acded` |

The combined original report size is `720495` bytes. Both `identity_verified` and `metadata_complete` fields are true; missing required fields are empty. These are complete-file hashes, not hashes of selected metadata or sampled rows.

## OMA.3. What the original reports actually say

Both original reports have kind `floating_dealiased_two_field_Codazzi_with_position_reconstruction`. Both retained the mean and the original target, removed the Nyquist mode, requested `[0,0.235]`, finished `[0,0.235]`, and saved 236 sampled rows with first radial coordinate 0 and last coordinate 0.235. Both original success flags are true under the explicitly tested complete/finished/no-exception criterion. The two grids were respectively 512 and 1024, with doubled nonlinear grids 1024 and 2048.

The original metadata also states `certified=false` and makes each of `whole_parameter_interval`, `whole_radial_domain` and `whole_real_angular_circle` false. The original limitations retain floating arithmetic, unvalidated interpolation and infinite Fourier tails, sampled projection diagnostics, the single exact parameter center, and the absence of cap/return/global closure conditions. The audit preserves these limitations.

The JSON nonfinite-token count is empty for both files. The deployed extractor would preserve an original NaN or signed Infinity as an explicit tagged original token, separately from numerical success, but no such token occurred here.

The exact common original object and parameter identities are retained in the public receipt:

- object SHA256 `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`;
- origin SHA256 `0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`;
- direction SHA256 `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`;
- exact center `-7789843107295549 / 4611686018427387904`.

No original sampled row, diagnostic, ordinary integral or enclosure was recomputed.

## OMA.4. Preserved source and endpoint identities

The common original producer is `scripts/fourfold_phase_codazzi_evolution_probe.py`, Git blob `0d3f34154e92282d3876f099585ec3c4438f92ca`, 11127 bytes, SHA256 `2d9e8a9dd185e13c1c506a628f36847fe6180390bca3b60014d7c1beb8a69c36`. It was read as source text during preparation, never imported or executed by this audit. The receipt retains all four original dependency SHA256 values.

The two endpoint files are separate objects and are preserved:

| Endpoint path, relative to the topic | Complete original SHA256 |
|---|---|
| `notes/2026-11-13-codazzi-evolution-r0235-n512-endpoint-floating.npz` | `e49a5141da41c7710cebe152419b34ba0c9ff8aa397bf5710c980148b2af0738` |
| `notes/2026-11-13-codazzi-evolution-r0235-n1024-endpoint-floating.npz` | `825e9eb6b4c587c41bd39ef36c76f28366993a81af754c120fea9dbcf1081552` |

The earlier small provenance report [R126 candidate and diagnostics](../notes/2026-11-13-R126-Codazzi-candidate-and-diagnostics.md), blob `adfe97699fa73cd9ae24d3db8837e4ec3fda7ffa`, 8714 bytes, SHA256 `68acb99affa62507776252d4b6b23d7199ab0442c72f4b8bb561adc50a741b30`, separately records the same sampled endpoint scope.

The distinct failed waist-formulation report `notes/2026-11-13-waist-cauchy-evolution-r0235-n512-floating.json`, its failure history, the exact origin and direction arrays, all endpoint/native/candidate data, and all producer sources remain outside this two-report audit and outside its proposed report-only cleanup scope.

## OMA.5. Frozen audit code and publication checks

| Audit input | Git blob | Bytes | Complete SHA256 |
|---|---|---:|---|
| `scripts/fourfold_codazzi_old_evolution_report_metadata.py` | `4dd7a5d6635a5c72205d750b9819c9175eae08f6` | 21315 | `c22e023d4632ae3a9feb7e0f98ebbf5c734e5dcd08f2ca72c3428f595245f6f0` |
| `notes/2026-11-15-R133-old-evolution-report-metadata-inputs.json` | `826e1cc2b110d424e79a54ca87b55603c35f3da7` | 3949 | `32c695a896b8f71d6a20314178846878e93f01e8d9ad0ec2c9815c6e41182fa7` |
| `.github/workflows/visible-exact-old-evolution-report-metadata.yml`, repository root | `197868e51e67f45b61f126cb9c790ba1fd596bd9` | 3008 | `0483d22a063d506f05651d66d0e64cbbc4c8c29ddb4cbac838ea9a9dc5bb832c` |

Both real pull checkpoints had empty README diffs and the same two exact README SHA256 values: root `6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9` and topic `81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220`. Frozen source and manifest identities passed. The fresh metadata-only topic capacity inventory gave 199886862 bytes before the one owned receipt and projected 199899290 bytes after it. The inventory SHA256 is `e4670d131889e6f446481d85cfc255482405c65081750ce6429bcc5dfae2af1b`.

The receipt records zero scientific computations, zero producer calls, zero old mathematics recomputed, zero new numerical enclosures, zero arrays, zero artifacts, zero Releases and zero deleted files. Its `eligible_for_deletion_not_decided=true` deliberately leaves the subsequent cleanup decision to the separate reviewed whitelist. This conclusion establishes the original completion statuses and full restoration identities; it does not itself delete a file or alter any certified mathematical result.
