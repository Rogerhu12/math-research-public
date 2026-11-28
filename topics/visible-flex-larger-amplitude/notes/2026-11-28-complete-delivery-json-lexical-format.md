# Complete delivery metadata: lexical JSON formatting (RET87)

2026-11-28; Astra-larger-e4e2a2bf-20261126 (AI-assisted). This is a lossless text-format change to historical delivery metadata. It is not a mathematical result, a new parameter choice, a changed scientific input or an additional execution condition.

## Scope and actual size

The complete topic tree at public commit `2d6b45da12fe0deb1809bc0c8e0fc22435cc4390` was read without truncation. The selection is exactly current `computations/*-delivery.json` files with 5,000 < UTF-8 bytes < 100,000, excluding names matched by `r72[4-9]|R72[4-9]|halfwave|run2[5-9]|run3[0-9]|retention-(8[3-9]|9\\d)|lexical-format`. These are 111 complete files, 3,624,429 bytes. All were fetched as whole small UTF-8 text and checked against their actual Git blob and byte count. The full SHA-256 of every original was computed from that whole text.

Exactly 81 files change: 3,164,002 bytes become 2,702,015 bytes, a gross reduction of 461,987 bytes. Thirty already compact files are byte-for-byte unchanged and are not rewritten. The complete mapping records them separately. Net topic reduction includes this note, the complete transformation source and the complete mapping; its exact figure is in the map's accounting.

## Exact transformation

The scanner walks each original character in order. Inside a JSON string it copies every character, including each original escape and backslash, unchanged. Outside strings it removes only ASCII space, tab, carriage return and line feed. It appends one final line feed. No key, array member, object member, order, punctuation, number token or string byte is removed or rewritten. Numbers are not parsed and reserialized: large integers, exponents, decimal spelling and negative zero keep their original literal tokens. JSON parsing was used only to establish that the already complete original and transformed texts are well-formed, never as a source for output serialization. A second lexical pass returns the same complete transformed text.

There is no numerical data compression, chunked raw carrier, binary encoding, truncated JSON or replacement of original scientific arrays. All actual success/failure/unknown fields and every embedded parameter/source record remain present with their exact token sequence. Runtime source, binding, ready, queue, request, CLI input, proof, raw report and checkpoint paths are not selected. Active halfwave/R724–R729 and run25–39 named delivery families are explicitly excluded, as are the current RET83–99 and previous lexical-format maps.

## Old and current identity are different objects

Each complete_file_map entry gives the same current path plus the exact original and new bytes, SHA-256 and Git blob. The unchanged_file_records list gives complete whole identities for all thirty skipped files. All old originals are recoverable at `2d6b45da12fe0deb1809bc0c8e0fc22435cc4390`; a consumer that expects an old whole file must use that original commit/path or exact old blob. It must never substitute the compact current file and label it with the old hash.

Fields inside these delivery objects are not updated. An internal `manifest_bytes`, previous artifact SHA, old source path, original request, historical timestamp, old completion boundary or embedded historical self-description keeps its original meaning. Such fields describe the object/version they originally recorded, not a newly invented whole identity for this formatted file. Current whole identity is given only by the explicit old/current mapping. This preserves full history without silently altering values to make old hash-bound consumers accept new bytes.

No claim is made that the selected metadata has no readers. Links used for ordinary JSON inspection still see the same complete JSON content. Old readers that check exact whole text must restore the complete old body first. The associated mathematical source and every actual parameter/input remain in their existing declared scopes and are not regenerated or edited by this operation. Previously recorded remote events remain historical facts; no network event is claimed to be replayable.

## Complete optional source and recovery

The full source is `scripts/resume_20261126/reproduce_complete_delivery_json_lexical_format.mjs`, 3691 bytes, SHA-256 `4e6c2efe4d702e41216de2e2cb5e069a02f48ea011545f26f8bbae83cecf7116`, Git blob `8f7b7edb5326b12e5b7c6988ab507c570dbccba8`. It is derived from the whole existing retention formatter, 3694 bytes / `eb477e86dce79599041e2461abdbeee579e927a8b6ce945d5bb84f6b12df8b3d` / blob `360c09a86237840e913c5a45cc3ca1075d87f444`, by changing only its basename and metadata schema strings. The lexical scanner and complete original/current byte/hash checks are unchanged.

Complete optional invocation:

```text
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_complete_delivery_json_lexical_format.mjs --manifest COMPLETE_DELIVERY_MAP --source-directory COMPLETE_FIXED_OLD_CHECKOUT --output-directory NEW_OUTPUT_ROOT
```

The old checkout supplies each full original file, restored from the one fixed commit. The source checks that entire old text, formats it, checks the entire expected new text, and writes it under a separate output directory. It cannot overwrite a different existing output. It performs no mathematical call, no AST/fixture/benchmark, no request or queue mutation and no Git ref update. It is an optional archival tool, not a required scientific admission step.

## Publication contract

Only root publishes. Immediately before an ordinary commit, the current tree must still match the mapped original blob and byte count for every proposed changed path. If another writer has changed one, that path must be preserved and handled from its newer complete version; no appended evidence is dropped. All 81 complete new files, the full source, this note and the complete map are protected as unreferenced UTF-8 Git blobs first. All files are smaller than 100,000 bytes. No path is deleted. The other thirty selected files and every nonselected path remain untouched.

[Complete old/current mapping and accounting](../computations/complete-delivery-json-lexical-format-delivery.json).
