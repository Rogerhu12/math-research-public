# Parameterized completed eighteen-query prefix readback

- Author: ChatGPT (GPT-6 Astra Pro), amplitude subtask.
- Classification: transport and read-only artifact interface.
- Status: source and AST checks completed; this new entry has not executed an artifact audit.
- Scientific scope: no new mathematical evaluation and no change to a finite solver or acceptance criterion.

## Source and retained byte-audit implementation

The independent source is
[computations/root_20261114_read_completed_eighteen_prefix.py](../computations/root_20261114_read_completed_eighteen_prefix.py).

It has 43863 bytes and SHA256
e3810833e4635dfd76b31b1f3944074fa95848ff67b1884e2b7468182a8f931e.

It derives from the already executed actual62 reader,
[computations/root_20261114_read_actual62_receipts.py](../computations/root_20261114_read_actual62_receipts.py),
SHA256 03a7868435cba5c2f71bdf04faaf2ae85c11b33b44904b472499b8bad7b1c819.
The old source is unchanged. Twenty-five original utility and byte-audit
function ASTs were compared. They agree after normalizing one exception
message from the historical actual60 parent label to the current paired
parent label. The numerical array identity, NPZ member verification,
complete B/Gamma/Pi assembly, finite B metadata reconstruction, condensed
part assembly, raw-output verification, source ledger checks and observer
payload verification are retained.

The new differences concern explicit artifact arguments, the parent
directory, report selection and original report copying. This is still
specific to the frozen eighteen-query family: eighteen original grids,
36864 finite B rows, 236036 complete coordinates and 5749 local coordinates.
It does not silently accept another finite dimension or producer schema.

## Explicit actual identities

There is no built-in guessed future artifact. The command requires the
actual request number, run ID, artifact ID, artifact name, complete ZIP
size and SHA256, actual source commit, original parent directory, and
the original compressed warm and decoded status SHA256 values.

For the already dispatched request63, the known run is 43646179305,
the source is db6d728f30ee2d0c9ea62c96c622d8d85d2354b2, and the parent
directory is parent62. Its parent warm SHA is
dffaa532026e07357d5115089d968c1be4472c44d9a5f5da25ebcb3e2291ac73.
Its parent original status SHA is
4f8239522cef511aca6721ddc9c4541cc9d4e65db3e7260d277b090ad226c054.
These are completed actual62 outputs, not an assertion that request63
has completed or has produced a new accepted warm.

The artifact ID, complete size and ZIP digest for a later readback must be
obtained from the actual published run. A source draft must not invent them.

The CLI is:

~~~sh
python -u "$C/root_20261114_read_completed_eighteen_prefix.py" \
  --request-number "$ACTUAL_REQUEST_NUMBER" \
  --run-id "$ACTUAL_RUN_ID" \
  --artifact-id "$ACTUAL_ARTIFACT_ID" \
  --artifact-name "$ACTUAL_ARTIFACT_NAME" \
  --expected-size "$ACTUAL_ZIP_BYTES" \
  --expected-sha256 "$ACTUAL_ZIP_SHA256" \
  --source-commit "$ACTUAL_SOURCE_COMMIT" \
  --parent-directory "$ACTUAL_PARENT_DIRECTORY" \
  --parent-warm-sha256 "$ACTUAL_PARENT_WARM_SHA256" \
  --parent-status-sha256 "$ACTUAL_PARENT_DECODED_STATUS_SHA256" \
  --download-out "$RUNNER_TEMP/completed-prefix-original" \
  --out "$OUT/completed-prefix-readback" \
  --repository-root "$GITHUB_WORKSPACE"
~~~

The current artifact-name contract is the original first attempt:
visible-followup-condensedqp-RUN_ID-1. The parent directory is a single
basename of the form parent followed by digits. All hashes are required
explicit lowercase hexadecimal strings. The complete ZIP source and
artifact metadata are checked against the supplied actual tuple.

## Transport

The transport source remains
[computations/exact_20261114_fetch_pinned_public_artifact.py](../computations/exact_20261114_fetch_pinned_public_artifact.py),
SHA256 51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859,
schema pinned-public-actions-artifact-fetch-v3.

Only its in-memory explicit PIN, truthful adapter schema and metadata
wrapper change. The wrapper binds workflow_run.head_sha to the supplied
source commit. Original HTTPS, redirect authorization stripping,
complete streamed ZIP SHA/size checking, member path safety and
CRC/size verification stay in that transport. Successful payloads are
placed directly under download-out.

The entry requires GITHUB_ACTIONS=true and
GITHUB_REPOSITORY=Rogerhu12/math-research-public. Authentication is only
the workflow environment token used by the unchanged transport.
No credential is an argument or a generated file.

Dependencies are the Python standard library and NumPy for safe
allow_pickle=False NPY decoding and byte conversion. No finite-field,
Frenet, collocation, native tail, boundary or optimization module is
imported.

## Compact observations and full original reports

The published target reports are:

- completed-prefix-readback.json: exact input identities, new pair,
  accepted and nearest rejected original trials, actual FD/QP scalar
  observations, and completed byte-audit counts.
- completed-prefix-trial-table.json: all saved original trial flags and
  scalar observations, original failed-query readouts and midpoint indices.
- completed-prefix-QP-scalars.json: original C/H comparison, local stop,
  unrepaired slack, repair and recovery observations.
- completed-prefix-FD.json: original FD results and source claims.
- completed-prefix-status-provisional.json: the original saved status
  identity and scalar fields even before later validation succeeds.

The trial view is saved before requiring a new warm or its FD report.
The reader does not reconstruct either if the original calculation did
not produce one. Exceptions retain their type, repr and full traceback
under large-arrays; an audit error never reclassifies the original
scientific run.

Repeated source_entry trees are excluded from derived compact reports.
This changes only the readout. All original producer trees are still
read and compared in full for status/warm/FD/parent binding. Original
model, status, FD, condensed summary and C/H comparison files are copied
byte-for-byte into large-arrays/original-reports, with a copy manifest.
They are not reserialized, mechanically divided for connector transport,
or substituted by the compact reports.

All numerical values in the target reports are copied from original
JSON fields. Failed-query selection uses the already saved original
negative/zero/nonfinite counters. It does not calculate beta, a norm,
a minimum, a derivative, a model, an acceptance decision, or a new
linear prediction.

## Audit scope and limits

The original byte audit still verifies all declared domain parts, all
complete B/Gamma/Pi/beta identities, the full finite B model identity,
condensed array references, the fourteen declared raw output files,
the supplied producer source files, and declared midpoint payloads.
Counts and hashes are actual results of a future execution; this
interface does not predeclare them.

The same paired parent remains bound at original bytes and complete
producer structure. The new warm and its original FD report must bind
each other. Public status compression is decoded transparently to
the original JSON bytes and never through JSON reserialization.

Complete array audit records, transport metadata, original reports and
tracebacks remain artifact-only under large-arrays. The original full
factor arrays were not exported by the producer; the reader therefore
does not claim an independent full-factor file audit.

The main report explicitly separates original warm progress from
BVP acceptance and research completion. A successful readback proves
that the specified existing observations and bytes were recovered and
checked. It is not another scientific run and supplies no new
mathematical certificate.
