# Retention 55: exact recovery of old launch and array-directory metadata

Date: 2026-11-28 UTC. Repository: `Rogerhu12/math-research-public`.
Scope: `topics/visible-flex-larger-amplitude`.

This is a repository-capacity record. It proposes removal of exactly nineteen old descriptive JSON files from the current tree, with their complete byte identities and exact Git recovery retained. It performs no numerical computation and changes no scientific source, input, parameter, result, proof, workflow, queue or active run.

The numerical checkpoint candidates considered at the beginning of this investigation are **excluded**. In particular, all eighteen M94/M96 cumulative checkpoints remain. Their propagated columns, forcing and endpoint state are actual `--resume` inputs. Calling such a file “generated” or retaining its Git history does not make it administrative metadata. The original preference for a net two-megabyte release does not override this boundary; this smaller batch deliberately does not reach that target.

## 1. Exact object set and fixed recovery snapshot

The fixed recovery commit is:

`d38bc6187b9a81fc54a2126f3985b131a51d36ed`.

All nineteen candidate bodies are UTF-8 JSON smaller than 100,000 bytes. Each was read whole as metadata and matched to its Git blob, exact byte count and SHA-256. No large numerical JSON, compressed raw object, NPZ, binary array or numerical checkpoint body was downloaded or decompressed for this retention.

The candidates total **719,337 bytes**: fourteen pre-request launch descriptions total 437,222 bytes; five H/QR array directories total 282,115 bytes. The final delivery manifest records the added bytes and exact net release after preserving these complete records.

| ID | Original run | Descriptive object kind | Bytes |
|---|---:|---|---:|
| N01 | 43603818345 | pre_request_probe_identity | 34883 |
| N02 | 43604874829 | pre_request_probe_identity | 35607 |
| N03 | 43605912092 | pre_request_probe_identity | 36719 |
| N04 | 43607404925 | pre_request_native_identity | 42808 |
| N05 | 43611175099 | pre_request_native_identity | 30254 |
| N06 | 43619564953 | pre_request_native_identity | 37544 |
| N07 | 43630351235 | pre_request_native_identity | 34668 |
| N08 | 43636504089 | pre_request_native_identity | 31523 |
| N09 | 43637356027 | pre_request_native_identity | 31524 |
| N10 | 43640772654 | pre_request_native_identity | 29582 |
| N11 | 43645948199 | pre_request_native_identity | 26382 |
| N12 | 43657001633 | pre_request_native_identity | 24657 |
| N13 | 43668743706 | pre_request_native_identity | 16495 |
| N14 | 43675377211 | pre_request_native_identity | 24576 |
| H01 | 43614132961 | complete_H_actual_array_directory | 38176 |
| H02 | 43621054216 | QR_actual_array_directory | 48724 |
| H03 | 43621054216 | complete_H_actual_array_directory | 46185 |
| H04 | 43623850723 | QR_actual_array_directory | 85076 |
| H05 | 43623850723 | complete_H_actual_array_directory | 63954 |

The [complete provenance ledger](../computations/legacy-launch-array-metadata-retention-55-provenance.json) supplies every full path, whole SHA-256, Git blob, byte count, exact original schema, write/read boundary and deletion entry. The table above is only navigation. No other sibling file is authorized for deletion.

## 2. Complete original parameters remain available

Two complete parameter ledgers accompany this note:

- [Native launch parameters](../computations/legacy-launch-array-metadata-retention-55-native-parameters.json), 87770 bytes, SHA-256 `eb5266ebcfa0fa930913f0b7d4a55267c51ae88749faa1a549c693e4236c699f`, Git blob `54d6c848946c3064da9835393834715c8f71c314`.
- [H/QR parameters](../computations/legacy-launch-array-metadata-retention-55-H-QR-parameters.json), 69589 bytes, SHA-256 `1294b90801a37d0cd7f3057898b3687e467b589683cef45b9bd855ef80d58765`, Git blob `0510384fd49de492a07e8eff683ddd155decb2ad`.

The native ledger retains all fourteen actual worker argument vectors. It preserves every original `current_sources` and `frozen_sources` name/SHA pair through an explicit ordered index into a 117-pair table: every actual current-source map still has all 91 entries. The indices are descriptive deduplication, not a source alias or a shortened source set.

The full 112-height request copied into ten launch descriptions is preserved once, including `jacobian=true` and `audit=true`. Equality to the complete original `fresh_request` in the unchanged actual25 `seeded-solve-spec.json` was checked by reading that small spec. Its original complete bytes remain in the current tree; the new parameter ledger does not replace or shorten it. None of these copied request words is a newly generated numerical state.

Every original spec, input configuration and runtime configuration stays in place. The exact current-tree metadata of those retained objects is recorded, including specs that are too large or compressed to read here. A declaration of the original uncompressed spec SHA is kept separate from the compressed storage object's whole SHA; an unknown newly computed whole SHA is left null.

The complete original requests, source commits, original workflow objects and input restoration chains already published in retentions 29, 40, 53 and 54 are referenced by their exact whole-file records and selection pointers. Their fields are not reduced to a parameter count or an informal summary. The new files avoid duplicating those entire published catalogs.

The native ledger's compact JSON serialization changes only the storage of this new bookkeeping document. It does not reserialize any original reader input or substitute the new document's SHA for an old file SHA.

## 3. What a verified launch description contains

The fourteen `verified-launch-intent.json` files are envelopes written by their complete original launchers after source/configuration/constructor/ready/capacity checks and before the requested native solve or diagnostic evaluation. They contain actual command arguments, source hashes, specification hashes, input file identities and initial call/cache flags. Some also repeat the original height request.

They do not contain the original full state array, a shooting checkpoint, a Jacobian, a direction, a returned trial result, a converged endpoint or a numerical audit. Those data remain separate objects, outside this deletion list. A pre-request flag such as `identity_verified_before_request` is not evidence that the subsequent solve succeeded.

All fourteen writer source files and all fourteen actual hook source files were fetched whole and checked against the exact source hashes declared by the corresponding launch descriptions. The complete source files remain untouched. The earlier whole source/input catalogs preserve the wider original worker graph and its previously recorded source-availability boundaries; no missing original file is silently replaced by a same-named current version.

This classification is based on the actual writer and consumer code, rather than on the word “intent” in a filename.

## 4. The old launch readers still require exact bytes

These files are not claimed to be globally unused. The original v1/v2/v3 `runCandidateProbe` hooks explicitly read their launch file, verify its whole SHA against `request.verified_launch_intent_sha256`, verify the spec and pre-stage identity flag, then use the declared current-ready hash. The old summaries record the same launch SHA.

The complete seeded-solve loader's `read_actual23` reads the v3 verified launch together with the full candidate checkpoint, spec, instrumentation and original live identity. The correction-capture loader's `validate_actual25` also binds the actual25 launch's exact whole SHA:

`19f886ed5baf101ed4cc3b053b9d7a67645578ca1434fe5acd50ef9f81ed6cd5`.

Later original launchers retain those historical checks. The realized-trial producer separately stores its actual launch record in the result.

Accordingly, any invocation of those old readers must first restore the original description bytes at the exact original path. The original guards remain unchanged. A fresh rerun, a new path-containing JSON serialization or a new SHA is not substituted for the old description. This is an exact restoration contract for historical metadata, not a new numerical admission test.

## 5. H/QR directories are separate from their numerical payloads

The complete `geometry_20261114_full_metric_projection_warm.py` defines `ArrayArchive.array` and `ArrayArchive.convert`. Actual NumPy arrays are written to separate NPZ members. The returned directory entries contain only:

`file, sha256, bytes, array, leading_slice, single_git_file_under_5MB`.

The nested array record contains:

`shape, dtype, sha256, bytes, definition`.

The full-H producer archives the selected direction, original A/B actions, multipliers, gradient, stationarity residual and all-row slack as separate payloads. It writes `full-H-final-selected-evidence.json` separately. Only after all final array writes does it write `full-H-array-manifest.json`, then bind that file's whole SHA in the comparison record. The directory itself is not the complete numerical evidence.

The QR producer's `CompleteInverse.preserve` likewise writes a directory for the actual returned RHS, candidate and residual arrays. The original inverse accounting and complete factor-export policy remain unchanged. In the actual40 run the large QR factors were memory-only; their original `files=null` boundary stays exactly that. This retention does not manufacture factor files or upgrade an accounting record to a factor-byte audit.

The five directories index 62, 68, 63, 132 and 94 file entries respectively. Their total 419 references are not 419 newly recovered arrays. None of those NPZ names occurs at its exact directory path in the fixed current topic tree. The original reports explicitly explain the artifact-only publication policy. The final-result and numerical array objects were already external or absent from that current Git tree before this batch; they are not being deleted here.

The directories themselves remain exactly recoverable by Git. Original artifact IDs, ZIP lengths and published ZIP hashes remain in the complete result notes and this provenance ledger. Current artifact-service availability was not retested and is not promised.

## 6. H/QR original workflows, resources and real input restoration

The H/QR parameter ledger retains complete original request objects and the complete preparation/warm/finite-difference lane blocks from the actual workflow at each source commit:

| Original run | Original source commit |
|---|---|
| 43614132961 / request30 | `8ed43e0b1119f009642eb983141ad3e86f28af78` |
| 43621054216 / request40 | `8a59ebd9d241bf424e9ba1c272e22b76264a034c` |
| 43623850723 / request42 | `34abbdf26804307a61fa4d18139c969c1cf9c445` |

The whole original workflow files are also identified, preserving checkout, environment, preparation, publication and unrelated lane context. The actual command bodies retain all arguments, timeouts and guards. For example, the original one warm iteration, 200 LSMR iterations, damping 270, 200 projection sweeps, 17 line-search steps, 1,200-second total budget, two Jacobian workers and 4,096-angle CLI remain exact. The source-entry physical-angle and row counts retain their own original meanings rather than being conflated with that CLI value.

Request30's H budget/reserve is 600/180 seconds. The QR runs preserve 300/90 seconds, 1,200 H products, 64 inner iterations, relative tolerance 1e-8, 200 dual sweeps and column preconditioner `none`; the working-row cap is 16 for actual40 and 32 for actual42. Default values belonging to an original command are supported by the whole original source, not invented from a later run.

The actual parent inputs are distinct:

- Request30 consumes request29's `f2e999…` warm and `a24ebb…` status.
- Request40 consumes actual37's `dd8374…` warm and `37e70a…` status.
- Request42 consumes actual40's `c62a7f…` warm and `30f193…` status.

The full hashes, exact paths, byte counts and original Git objects are in the parameter ledger. These original input objects were located by metadata in each **actual source commit**, not assumed to exist in the later retirement snapshot. The common accepted state, full M112 preparation, boundary-response record, tail configuration and anchor are likewise recorded. Large input bodies were not read. Their continuation roles and scientific contents remain unchanged.

## 7. Actual outcomes are preserved without promotion

The complete original result notes remain in the current tree and are identified in the provenance ledger.

For the native chain, the records continue to distinguish the actual21 combined guard stop, actual22 identified rounded-zero/underflow failure, actual23 complete candidate with a residual above the original tolerance, actual25 rejected trials, and actual28's intentionally captured first Newton model. Later entries preserve the actual55 rejected attempts, actual57 no-decrease returns, and actual59's single accepted decrease without calling it a completed native solve. Actual83's one no-J trial had no strict decrease. Complete current576 requests and their failed or unaccepted-parent boundaries remain in the original ret29 catalog.

For the H/QR runs:

- [Actual30](2026-11-14-actual-request30-complete-H-comparison-and-warm.md) selected C rather than H in the complete objective comparison. It produced one accepted optimization-warm step and a finite-difference check. It did not establish native BVP convergence, complete-QP optimality or continuous geometry.
- [Actual40](2026-11-14-actual-request40-complete-QR-H-working-row-limit.md) selected QR-H and accepted one warm step. The small working-row stationarity was not a proof for all 24,576 rows; 1,804 full rows had negative slack. The [historical byte audit](2026-11-14-actual40-complete-QR-inverse-byte-audit.md) covered the specified returned arrays and 17 inverse records. It did not audit the memory-only QR factor bytes.
- [Actual42](2026-11-14-actual-request42-complete-QR-32-row-warm.md) continued the actual40 field with 32 working rows. The original note limits its independent inspection to the small original reports and first/last inverse reports; no new full large-array audit is inferred. The same run's separate rawcell0band failure remains separately recorded and is not overwritten by the prefix warm's result.

The provenance ledger preserves the exact archive identities reported by those notes. Nothing in this retention replaces an old failure, partial read or unavailable payload with success, zero, an empty array or a new certificate.

## 8. Exact recovery and the old readers

The candidate recovery method is exact Git-object restoration. Obtain the fixed commit or the declared individual blob, restore its bytes at the full path given in the ledger, and retain the old byte-count/SHA checks in the original reader.

For a declared candidate path `P`, the historical command form is:

```sh
git fetch --filter=blob:none origin d38bc6187b9a81fc54a2126f3985b131a51d36ed
git show d38bc6187b9a81fc54a2126f3985b131a51d36ed:P > P
```

Here `P` is the complete listed path including the topic prefix; it is not a shell variable or an instruction to rewrite an arbitrary file. The ledger supplies all nineteen precise targets. The restored original whole SHA, byte count and Git object must match the declared original record.

This restoration requires no new numerical run. Recomputing the warm, redoing a solve or regenerating path/time-containing metadata would create a different historical object and is not the chosen recovery method.

Restoring a small directory does not by itself restore a separately required NPZ/archive or solve any pre-existing input availability problem. Those are distinct contracts, recorded with their honest original boundaries.

## 9. Explicit exclusions

The complete ledger lists the eighteen M94/M96 checkpoints with their current metadata and the reason each is retained. Their aggregate 740,159 bytes are not counted in this batch's gross release.

Other numerical sample/result tables, including the considered R167 records, are also excluded. The canonical mathematical identities, parent91, ports, Nelder records with an unresolved original-source boundary, every original spec/config/request/ready, scientific sources, proofs, parameter packages and all active inputs/results remain outside this deletion list.

Prior retention deletions are not counted again. No unrelated raw file is selected merely because it is large or because the old producer could, in principle, be rerun.

## 10. Publication responsibility and nonclaims

Only root may implement the change. Root's fresh current-tree path/blob/size comparison must match the exact nineteen original entries; a differing object is retained rather than silently included. Publication is an ordinary successor containing the complete records and the precise deletion set, with no force update and no scientific source or queue edit.

This check is repository mutation bookkeeping. No independent rerun, AST test, benchmark, fixture, full-array scan or new mathematical gate is introduced. The work is limited to source reading, small descriptive metadata, original workflow/request records, Git metadata and text hashes.

The original numerical problem, every parameter and every recorded outcome retain their prior meanings. The smaller safe space release is the result of that boundary.
