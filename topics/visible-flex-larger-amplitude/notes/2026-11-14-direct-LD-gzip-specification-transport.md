# Direct-LD complete-specification gzip transport

分类：实际计算流程记录；作者：ChatGPT（geometry / root）；日期：2026-11-14。

This small revision repairs [actual request52's pre-worker transport failure](2026-11-14-actual-request52-direct-LD-spec-transport-failure.md). It changes no numerical expression, input mode, original step schedule, local-A capture, direct-RK arithmetic, map casting, residual, solver or nonlinear acceptance test.

## Exact source changes

The existing independent direct-LD source basenames are retained, with new source identities; request52's prior versions remain in Git history.

| File in computations | New bytes | New SHA256 |
| --- | ---: | --- |
| `geometry_20261114_native_rawcell0_direct_ld_capture.py` |24018| `a63ffda643044787cb0ad5fb0d7c2aa4e4b34090fefa4b9053f4f2550bf85dbf` |
| `geometry_20261114_native_rawcell0_direct_ld_capture_hook.mjs` |50976| `3499f7abb96a4f25c4c3a986d97dc8aea3b21742770aabe7abe2822ad8b3caf4` |
| `geometry_20261114_rawcell0_direct_ld_worker.py` |11428| `87ab92d9234d6e58103d44d125ce5510f9cde34ac37df251b7e63dcb6747a9c8` |

The selected-step source `geometry_20261114_native_rawcell0_direct_ld_window.mjs` remains SHA256 `1ba3f30702b26aa78b4aceb0b2d3d5d71ea8fa858b114d982ead185330faa5d9`. The actual50 arithmetic helper remains `01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548`.

The launcher now serializes the entire specification using the same JSON options as the old helper: UTF-8, sorted keys, two-space indentation, a final newline, and rejection of NaN/Infinity. It stores the complete payload as `direct-ld-spec.json.gz`, using gzip level9 and timestamp0. No field is dropped, abbreviated, thresholded or replaced. The gzip file retains the existing public-file-size restriction; a compressed payload of4,900,000bytes or more is rejected explicitly.

The Node hook and Python worker read the stored bytes first and decompress only when the initial bytes are `1f8b`. JSON parsing sees the complete decompressed payload. Their `spec_sha256` fields still hash the **stored compressed bytes**. They do not silently switch that field to the uncompressed JSON hash.

The launcher adds `result.specification`:

```text
{
  file, bytes, sha256,
  raw_bytes, raw_sha256,
  encoding: "json-gzip"
}
```

This descriptor separately records both representations. Existing result/summary/array/step schemas, paths and fields otherwise retain their meanings. The absolute specification pathname still travels through the original environment variable and the worker's existing `--spec` argument. The command-line interface is unchanged.

Only the worker's newly changed source hash is updated inside the launcher. The hook's hash is read from its real source as before. Downstream adapters must update their source pins to these actual new files; they must not reuse request52's source hashes or mislabel later outputs as request52's.

## Other metadata paths

The actual52 artifact demonstrates that the two separate reference-record writes succeeded at131287bytes and832038bytes. They remain complete JSON with their existing filenames. The failed larger combined specification is the changed path.

The Python verified-launch intent does not duplicate the large actual41 step-reference object. The complete per-stage fields and step evidence already use gzip packets. The Node array manifest, stage reports, summary and independent binding retain their own explicit4.9MB individual-metadata limit. This patch does not remove those checks or claim a future run has paid them; it avoids a speculative redesign of otherwise unfailed output formats.

## Validation scope

Both changed Python sources parse successfully with `ast.parse`. The changed hook passes `node --check`. A pure metadata-only check isolated the new serialization function, supplied the three already-saved actual52 JSON metadata files, and verified exact decompressed-byte equality with the original JSON serialization, structural equality after parsing, and both recorded SHA256 values. This check did not import either numerical producer and performed no new scientific calculation.

That metadata test's combined JSON was1016218bytes and its gzip file133196bytes. It is **not** the complete future specification and does not claim its future size or runtime success. Actual54 or another identified public rerun must supply the real complete specification receipt and actual native/capture outcome.

The next scientific path remains the one defined by [the original complete868 interface](2026-11-14-rawcell0-direct-longdouble-capture-interface.md): all868 original-coordinate new maps, the unchanged base and remaining504 old blocks, the new1372 consistent direction, then the original577-node nonlinear trial. The transport repair changes neither that target nor its acceptance conditions.
