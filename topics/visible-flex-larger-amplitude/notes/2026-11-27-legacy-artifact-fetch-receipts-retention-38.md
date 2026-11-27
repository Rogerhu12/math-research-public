# Retention 38: eight original artifact-download and extraction receipts

Date: 2026-11-27 UTC. Author: construction. Scope: complete read-only provenance for the eight named administrative receipts. This note does not record a deletion or a scientific rerun. Root alone controls publication and the current tree.

The proposal removes only eight published download/extraction directory receipts from the current tree. Their stored total is **1,439,073 bytes**. Every original scientific source, complete request, input descriptor, result, existing recovery record and mathematical conclusion keeps its existing retention status. The original files remain exactly recoverable from the fixed Git objects listed below. No large receipt body, binary payload, ZIP or gzip body was downloaded or decoded during this review.

The complete machine-readable ledger is [legacy-artifact-fetch-receipts-retention-38-provenance.json](../computations/legacy-artifact-fetch-receipts-retention-38-provenance.json), 97272 bytes, SHA256 `da9d924186b0ff9d11210e8c967a271a47a09a8b94b360a0d19d8e482dc05824`. It embeds all fields of the seven original scientific requests and both later recovery requests, not a reduced set of preferred parameters. Its source table, run records, original identity-file records and exact eight delete entries are also complete. Each saved request identity remains at its original path; fields outside its embedded `request` object remain recoverable through that whole-file identity.

## 1. Exact current-tree scope and fixed recovery

The actual metadata snapshot was taken at commit

`5b35f0b800915e418bca93f3875389a5e37a156c`.

For every entry, the directory metadata at that fixed commit independently matched the specified path, byte count and Git blob. The stored file body was not fetched to calculate a new SHA256. Its SHA256 is therefore explicitly **null** in the ledger. This does not replace a missing hash with an artifact ZIP hash, an adjacent receipt's hash or a reserialized JSON hash.

All paths below are under `topics/visible-flex-larger-amplitude/notes/`. The complete repository-relative paths are present in the ledger and its `exact_delete_entries`.

| Entry | Published directory run | File | Stored bytes | Exact Git blob |
|---|---:|---|---:|---|
| 1 | 43650386882 | `original-artifact-fetch-receipt.json` | 108272 | `d8fc5a3eebd155eca9deea8a76287048c3bf4007` |
| 2 | 43650856568 | `original-artifact-fetch-receipt.json` | 108272 | `630d986684f76b473def68df8c141be78ddfc2fb` |
| 3 | 43655003971 | `actual61-selected-fetch-receipt.json` | 183835 | `8841216b560cec92f8b66d5f5cb2d334fe6b03ca` |
| 4 | 43656059206 | `_pinned_public_artifact_receipt.json` | 136180 | `a6245aa1e131795ab0764a5b404887ea4402cc79` |
| 5 | 43656397000 | `actual61-selected-fetch-receipt.json` | 183835 | `d1a77c9278d2a65e456d55db88cddc9f33242834` |
| 6 | 43657001633 | `_pinned_public_artifact_receipt.json.gz` | 277411 | `f9558f06a8c4db0b4e7433b248941f41a2a5665f` |
| 7 | 43657001633 | `actual61-selected-fetch-receipt.json` | 183835 | `f3e5e4551876d78365b3eb2581268ca84cbe1234` |
| 8 | 43668743706 | `actual73-selected-fetch-receipt.json` | 257433 | `9ed086d031170ac7a9b541302471410eab5d1336` |

The two actual73 entries are different records: the named `actual61-selected-fetch-receipt.json` belongs to the original actual73 input selection; the `_pinned_public_artifact_receipt.json.gz` belongs to a later full-artifact readback and recovery. They must not be conflated merely because both were published under the original run directory.

For entry 6, 277,411 is the stored gzip length. The uncompressed byte count and uncompressed SHA256 are left null because neither was supplied by the small records inspected here. The other seven entries are JSON files whose stored and uncompressed byte counts coincide. No receipt fields, timestamps or output paths have been guessed.

## 2. Actual source and complete original parameter preservation

The reviewed producer chain consists of the common complete pinned transport, two explicitly different actual63 adapters, the actual61 and actual73 selected extractors, two full completed-artifact readers, the actual73 packet route, the public source restorer, and four exact publication-source versions. Their full text was retrieved and whole-file hashed. Source review covered receipt creation, original source/PIN validation, selected/full extraction semantics, receipt consumption and publication. It was not a new review or execution of the scientific body of each diagnostic.

| Complete source version | Bytes | SHA256 |
|---|---:|---|
| pinned_fetch | 28006 | `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` |
| selected61 | 14501 | `4853becf379f5db5594b62b2ec6b4266fd6853694fb19b19f56f11330db9f208` |
| selected73 | 17288 | `51f865285ab348792842a3d1419135fd1c9ae8ece5c853d13776f252e43d4056` |
| actual63_v1 | 57165 | `10aeaa14b20651d87cecca67db6acb6bb3fd78663aa6dfe07897aa9c04ca1e6a` |
| actual63_v2 | 57166 | `5033b8866dcc1fd158a7affda7305e1af90ece588ab1eca7d56dba4612ecb742` |
| publisher_10454 | 10454 | `5cc3de2699c3585961c86a37d718011c1d5d0829047e9eb7eec620e65c6c86f1` |
| publisher_12620 | 12620 | `627393d1ba77b5e13dcf34da64204d0554a7c009770a2d80a1353c3f16b007fe` |
| publisher_14433 | 14433 | `5a0216d00c8ca732b03886904ca232bc9453bc12d47a697d9384e4871c594de9` |
| publisher_14455 | 14455 | `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca` |
| resume | 13907 | `11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5` |
| root_20261114_read_completed_twenty_one_lambda27_prefix_py | 49810 | `42fb5d0f97c2cee619e2ac1b7e6ee2b9249ee42a518a23cdc9d4c462e0d3c3fa` |
| exact_20261115_read_noj_primal_current576_artifact_py | 76963 | `c062117765addc2acf7b82ca1aa6ad87027ebab8d32c75673af382d24dd26f06` |
| exact_20261115_actual73_readback_packets_py | 11509 | `d97eb11b51ff621f10d31a4da5aa942bca405ec36a64dd298e551eddc1d0e9d7` |

The ledger gives each full path and its actual source commit. For old versions whose Git blob was not separately exposed by the small source record, the actual source commit, full path, exact length and SHA256 remain the complete recovery locator. A current publisher file is not substituted for an older one.

Each of the 13 source versions was also matched against the appropriate original request's complete `source_sha256` map. The original workflow source was retrieved at the actual triggering source commit, including both separate completed-readback workflow versions. The two original actual65 attempts share a workflow but use different adapter source identities. Their one-character scientific input-digest correction is not silently applied to the failed attempt.

The complete original request objects include the original input tuples, all source pins, memory limits, diagnostic budgets, scientific dimensions, stages, selectors, tolerances and scope flags. The actual70 request retains its full same-parent/damping/query/layout description. The actual73 recovery request retains its independently labelled R276 exact-integer diagnostic and all original alpha powers; it is not mislabelled as an entirely byte-only job.

The following two SHA columns have different meanings. The first is the SHA of the **original raw request file**, as recorded by its actual run. The second is the SHA of the **saved identity JSON** read in this review. Parsing and embedding the complete request does not reproduce the first file's original whitespace or hash.

| Actual run | Original raw request SHA256 | Saved request-identity SHA256 |
|---|---|---|
| 43650386882 | `36596d2e9f1276b323f047f008f4d43e9932ad1ab25729aa1675808a4dd9243b` | `166a79a041d89c731cd17b3bde35440be3baf9e3fc2213db63f70b1366b68195` |
| 43650856568 | `8096ddefaf4e069d75d1d13d1459e244cf53067acce013b303382101cd465a8f` | `62b5d4a1602e3dd784b399a72df79c0d560bb0161c9874c07ef247b8daf72afe` |
| 43655003971 | `c0dcd04ec91df9ba8147a591602eb0f0b56707825f36fbcd6986276329ec280f` | `2bce448f09c37ddf1a6e771cd0ace95265c8e7dfd0bd7a60cd7106a366fc1145` |
| 43656059206 | `478a9bd116ed46504a9354424191f00fc9061655d9d7ebebc35abeef81cc1fd4` | `09342593c67b6104e771e9cd6e4c7b72bd24b15698b8d355a3088f3c36247727` |
| 43656397000 | `46150710b03b5286cca2469ab1d846eaa8f60e52953647911f9285cb6df07080` | `0946b082e6251cbbdbe13b1a24619b486d7764286aa793743e46a76ff28d5016` |
| 43657001633 | `1823b6908d875f7e30975704f2182d9f2b0a34af83c6026b0e813ffaca199acc` | `e7a93c179ab394b251fe6b214cea9350d48c6064e1ec827e40cd07e866c6be27` |
| 43668743706 | `90da387ca0e9fa57b22e89bce34a8692f1e4e1ffa993542d5b38be9f175c68b8` | `9427241f066d5595b51a1131cc5b8fe34abc8ed4fe35f120964502ba2834dbd1` |
| 43657876708 | `3b721367e23311f5901f2b97c9536cf9224be906c339def5bdaaa345cceaabf7` | `a682eb9d9af037a04df877c51439d8b21274174d0ee7809785dfefcf63fcb8e7` |
| 43664753410 | `60097d6734c8847436454b4248056a983ea668e98b9f3443f598a249cfc9284d` | `ec6feff74234062cdba1d241ec0ad466c263a59308269b4585aa71117049a9ff` |

The original request path and its actual source commit are retained in every run record. Restoring an original raw request requires those original bytes; hashing the ledger's JSON rendering does not satisfy that guard. The full saved identity files, including their complete verified-source/input records, remain retained as separate pinned files.

## 3. What generated each receipt

### 3.1 Two complete actual63 artifact fetches

Runs `43650386882` and `43650856568` call the exact actual63 adapter's `fetch_original`. It pins the original actual63 artifact and source, delegates to the complete pinned public-artifact transport, and writes the extraction-root `_pinned_public_artifact_receipt.json`. The workflow then copies that actual receipt to `$VISIBLE_OUT/original-artifact-fetch-receipt.json`.

The shared original input is run `43646179305`, artifact `14134662698`, name `visible-followup-condensedqp-43646179305-1`, 494,657,224 bytes, ZIP SHA256 `c90869cdcc317eef9b23a8a17755a7679ea5ce6dc41c2c143216524b481c6653`, source `db6d728f30ee2d0c9ea62c96c622d8d85d2354b2`. The two receipt blobs differ; this proposal does not declare them interchangeable.

The downstream actual63 analyzer reads the extraction-root receipt and validates success, the exact PIN and the full downloaded archive identity. That runtime use remains intact. This proposal concerns the separately published old copy; it does not remove or bypass the original reader's input guard.

### 3.2 Three selected actual61 input receipts

Runs `43655003971`, `43656397000` and `43657001633` call the exact selected actual61 extractor using their complete request input tuple. They copy the resulting receipt from `$RUNNER_TEMP/actual61-noJ-selected/` to the named published `actual61-selected-fetch-receipt.json`.

Their common original archive is run `43645948199`, artifact `14136633570`, name `visible-mainline-current576native-43645948199-1`, 2,335,870,174 bytes, SHA256 `7b17d1b0c11bfe14329a1d8715c8451498d0dedb6821859deb8485e5b1c1b469`, source `cf6b51193255dfc713610d2919598451ccdd49e2`.

The producer first verifies the full ZIP identity. It then selects descriptor-bound original root records and all nine complete no-J current-array streams. It checks selected member sizes, CRCs and SHA256 values and the complete original stream identities. It does not claim to inflate or CRC-check unselected payloads, and it does not extract the stage-J payload for this selected input route. Retiring the receipt copy does not retire any selected raw-array descriptor or alter the original no-J/J comparison.

### 3.3 Two later full-artifact recovery receipts

Entry 4 was generated by the later completed readback run `43657876708`, source `c337fbad640298d5cdffadb1451746fbdd773662`, using the full actual70 reader and publisher SHA `5a0216d00c8ca732b03886904ca232bc9453bc12d47a697d9384e4871c594de9`. Its public restoration commit is `71278605f92a76280f3f9405dbd07cfb331d5c80`. The original artifact is `14139045881`, 606,816,318 bytes, SHA256 `e45f32846bf48cb474c738c58675b30dada435229846ed3b27e319d8dcb63bd9`.

Entry 6 was generated by completed readback run `43664753410`, source `4a2824deaf68a6fd1a55ae464aa87737956a42f7`. The packet route performs one complete actual73 fetch, preserves original packets first, and then calls the unchanged complete byte reader. Its publisher SHA is `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`; its restoration commit is `2c13197c4770b27d01f196e4670dabf7e28fc23f`. The original artifact is `14141540502`, 1,752,742,419 bytes, SHA256 `3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9`.

In both workflows, the recovery step first reads the real extraction receipt and checks success, repository, complete artifact PIN, actual download size/SHA and original workflow source. Only then does it invoke the pinned publisher with `GITHUB_RUN_ID`, `GITHUB_RUN_ATTEMPT` and `GITHUB_SHA` set to the original run, attempt 1 and original source. This explains the original-directory location without pretending the later receipt was generated by the original scientific job.

The two recovery workflow records are successful; their original scientific conclusions remain separate. Actual73's separate R276 postprocessing uses exact integer arithmetic and is expressly labelled as such. Its success does not turn the failed native solve into a success. No R276 arithmetic was executed during this retention review.

### 3.4 Selected actual73 input for actual83

Run `43668743706` uses the exact selected actual73 extractor for the same original actual73 archive tuple. The producer selects the actual final snapshot and all ten complete current-array streams, including the saved stage-J payload, plus the complete original delta and the signed residual ledger needed by that route. The original native result, snapshot, full current state and direction identities are all pinned in the complete request and source.

The workflow copies the actual extraction receipt to `actual73-selected-fetch-receipt.json`. This record describes original bytes and download provenance. It is not itself the actual83 nonlinear trial or the later exact realized-step computation.

## 4. Publication and gzip do not change scientific provenance

The original publication source iterates the completed result directory, records each file's size/SHA, and copies eligible small files. For JSON, JSONL or log files above one million bytes it uses `gzip.compress(raw,mtime=0)`. This is the actual path responsible for the existing actual73 compressed receipt. The reviewed 14,455-byte publisher differs from the 14,433-byte recovery70 publisher only by its extra permitted publication lane; both complete versions remain separately identified.

Receipt generation includes timestamps, runtime run IDs, output paths and extraction inventories. Repeating a download may verify the same input archive without reproducing those old receipt bytes. Exact restoration therefore uses the fixed Git blob, not a fabricated regenerated receipt or a new timestamp.

No original receipt is replaced by an empty object, a guessed success flag, another run's receipt, or a digest of a reconstructed JSON value. A future historical consumer that really opens one of these paths must receive its exact original restored bytes. That is its existing input contract, not a new scientific preflight or rerun request.

## 5. Original scientific outcomes remain unchanged

The actual GitHub API records at review time were:

| Original run | Triggering source commit | Workflow conclusion |
|---|---|---|
| 43650386882 | `949d7056a8fbee4d5b6b3fd27b67a7f6cda7ec74` | failure |
| 43650856568 | `8f79c33c697e18525ac9fffd7fab592f20f10df8` | success |
| 43655003971 | `e849b7f103f7e96cd3c243b678ef001508be0ddb` | success |
| 43656059206 | `ab974f19df95e509346fa15d0cefc037780434fd` | failure |
| 43656397000 | `3df227cb306922ee7eed7bf61764c6dc7c5a3eb9` | success |
| 43657001633 | `9515d5aaf7c68f8efd366438d6bd81ce73c3486f` | failure |
| 43668743706 | `8d199eda5c1f1df162ded244e8dfd012e0c8d127` | success |

A workflow conclusion is not used as a numerical convergence certificate. The retained original notes distinguish the actual outcomes:

- The first actual65 attempt stopped on a missing-character input SHA before the new diagnostic; its successful fetch is not a scientific success.
- The corrected actual65 diagnostic completed on the fixed actual63 model. It attributed the selected row's small predicted response to the full damped centre, while retaining all original B constraints. It did not produce a new accepted nonlinear trial.
- Actual69 completed one full no-J evaluation at the saved actual61 state and recorded its actual difference from the saved with-J path. Native acceptance remained false.
- Actual70 completed its QP/trial and original FD steps. Its workflow failure occurred during later publication; the full readback restored original files rather than rerunning the science.
- Actual71 recorded matching complete primal words and new full tangents for stages 11 and 12. It did not claim a full 576-stage native solve or a global derivative-accuracy certificate.
- Actual73 retains its genuine native no-descent failure after two accepted steps. Later complete readback, publication recovery and R276 analysis leave this failure intact.
- Actual83 completed the prescribed original no-J trial, but strict norm decrease was false. It did not generate a new direction or obtain native acceptance.

The ledger pins the complete corresponding small conclusion notes, including the actual65 typo/retry note, actual70 publication-recovery note and actual73 shared-readback/R276 note. Existing previous retention decisions for large scientific outputs are not changed by this administrative receipt proposal.

## 6. Current warm and other consumers

The current warm dependency statement reuses the already published complete retention34 source investigation at its exact whole identity: `legacy-condensed-intents-retention-34-provenance.json`, 93,023 bytes, SHA256 `f19e26a0cfde7ca23c8a63962c6ac0fac4e286ea84a78019baa7079d106012b2`, Git blob `b962986e53a86a228660db0ecb6d6b7cf9860aaa`.

That record identifies the actual `reproduce_and_solve`, `rebuild_fullclosed`, `rebuild_closed_warm`, current axisymmetric recipe and Hold-warm source versions. Its declared chain constructs the current prefix/assembly/Hold/mode inputs from the fixed original raw seed and complete source closure. The eight old extraction-directory receipt paths are not declared inputs of this reviewed current entry chain. This is a limited direct dependency statement; it is not a claim that every historical diagnostic or future arbitrary script never reads a receipt.

The complete retention29 ledger remains retained: 55,022 bytes, SHA256 `3c30ec4e8d3ad145c04767c7f1d42c11aea25fa25dcf45a9351702d3d1b2181f`, Git blob `6b2b5593030151c184d692047f9837fd2e716601`. It preserves original requests 95, 73 and 61, original current576 specifications, full source identities and source-version differences. The present ledger additionally embeds the complete original requests directly involved in the eight receipts and both actual recovery requests.

No global repository consumer scan, new Actions job or scientific test is proposed. The argument is specific to the exact reviewed producers, original source/workflow/input identities, current warm chain and unchanged restoration contract.

## 7. Exact restoration and authorized implementation

For any one selected repository-relative path, exact restoration is:

```bash
git show 5b35f0b800915e418bca93f3875389a5e37a156c:REPOSITORY_RELATIVE_PATH > DESTINATION
```

The recorded Git blob can also be read directly with `git cat-file blob`. Match the fixed object and stored length; do not invent a missing receipt SHA256. For the gzip receipt, restore the original compressed bytes unchanged and decompress only if the actual consuming interface requests JSON. Do not parse and reserialize a record whose original consumer checks its file hash.

Original scientific requests are restored from their own actual source commits and exact original request paths, rather than assuming all historical request versions coexist at the retention snapshot. The ledger preserves each original raw request SHA separately from its saved identity-file SHA.

Root may implement only the ledger's eight `exact_delete_entries`, together with this complete provenance record and note. The construction agent has not deleted files, changed refs, changed a queue, run science, rerun an artifact fetch or altered any source/parameter/result. The proposed gross removal is 1,439,073 bytes; net capacity must subtract the actual new ledger and note sizes. The separate group of eight actual41 gzip files belongs to retention37 and is outside this proposal.
