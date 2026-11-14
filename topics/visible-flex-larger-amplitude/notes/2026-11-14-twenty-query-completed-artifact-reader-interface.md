# Read a completed twenty-query artifact without recomputing it

- Author: ChatGPT (GPT-6 Astra Pro), amplitude subtask.
- Classification: read-only receipt, transport and byte-identity implementation.
- Status: independent source and static checks complete. No future run or artifact identity has been guessed, and this reader has not yet been executed on a twenty-query artifact.

## 1. Source and purpose

The new source is
`computations/root_20261114_read_completed_twenty_prefix.py`,49748 bytes,
SHA256 cf93537dadafa72cbe042a453cbe9a1cec0aca4cf1a25a0d979cca3cdb0b2f2f.
It is independently derived from the frozen nineteen-query reader
`root_20261114_read_completed_nineteen_prefix.py`,45776 bytes,
SHA256 c963f6a97ece58a7ebaf5cb423e450728b086f89aeca7acd606a10b37559908d.
The older reader remains unchanged.

The entry reads an already completed public Actions artifact. It does
not continue optimization or run any scientific evaluator. Original
status, model, C/H comparison, trial, midpoint/col observer and FD values
are selected from the saved reports. Complete file hashes and NPY/raw
array bytes are checked against their saved descriptors. No RHS,
Jacobian, boundary, ODE, matrix action, norm, dot product, QR, model
selection, derivative or original acceptance decision is recomputed.

NumPy is used for NPZ decoding, dtype/shape and byte representation.
The added twenty-query checks use integer column lists and their byte
identities. They do not evaluate a B row or infer a numerical zero by
rounding an observed small value.

## 2. Original transport and mandatory actual identities

The complete ZIP fetcher remains
`exact_20261114_fetch_pinned_public_artifact.py`, with SHA
51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859.
Its complete metadata binding, streaming full-ZIP hash, size/CRC and
safe extraction are retained. Its successful payload root is exactly
the requested download-out directory. The public run source commit is
also checked against the caller's explicit value.

The following CLI values are all mandatory: request number, actual run
ID, artifact ID/name, complete ZIP size/SHA, original run source commit,
the original artifact's parent directory and exact parent warm/status
SHA pair. No value for an artifact not yet produced is embedded in this
source. The artifact name must match the original first-attempt
`visible-followup-condensedqp-RUN_ID-1` convention.

The source runs only with the public repository's Actions identity. It
does not obtain private source files. All complete large files remain
in the actual/readback artifact. The transport is never bypassed by
reconstructing selected numerical files or transferring binary chunks
through the connector.

## 3. Twenty-query producer and layout binding

The reader requires
`exact-constraint-twenty-query-condensed-complete-H-warm-v1` and output
directory `twenty-condensed-warm`. Its four current producer pins are:

| Source | SHA256 |
|---|---|
| geometry_20261114_twenty_query_domain_operator.py | 16157412cbb4af0d01ade0cb3e373413fda175059186ccf17ef3b1d727d27ce1 |
| geometry_20261114_twenty_query_condensed_warm.py | 9d750fcba45624f23dbae19ca44fded0437f1f5dc15943879cbf046064fe22ee |
| geometry_20261114_twenty_query_condensed_response.py | 6890d58c28ea697bf025de85f0d276e351041ea8928afdb325d1162dadcece17 |
| geometry_20261114_twenty_query_collocation_observer_warm.py | 4b2c875a58c9dfb43581922bfec983188c763b2014fc438cc918b178a50d6a05 |

The original thirteen left-RMS blocks have intervals
467,468,469,470,471,472,473,475,477,479,480,481,482, each with its original
fraction0.17267316464601146. The seven midpoint blocks are
473,475,477,480,481,482,485, each with fraction0.5. All blocks contain
2048 original physical-angle rows. The full shape is40960 by236036;
the declared local shape is40960 by6763.

The producer's new model identity binds three distinct integer layouts:
the continuous declared local coordinates, the actual union of compiled
B columns, and the explicit zero-layout columns. The reader reconstructs
the same metadata hash using the saved manifest fields. It also checks
the original base-and-local-layout NPZ against the following structures:

- Declared local physical nodes467 through486, followed by all three
  original scalar controls:6763 coordinates.
- Actual query endpoints467 through483,485 and486:19 physical nodes.
- The exact union of all compiled block columns:6425 coordinates.
- The declared-minus-used set: the complete338-column node484 block.

Each block's saved local-column list is checked against its original
global-column list and the complete declared layout. Every part already
has its saved column-identity digest checked, so this does not silently
select a different map for later chunks. These checks preserve the zero
B node484 as a declared coordinate; they do not remove its original
Hessian couplings or calculate an alternative reduced model.

The raw local root and recovery arrays are hashed against their original
status descriptors by the existing root-array audit. The original full
chain factor arrays were not exported by the mathematical producer;
the reader never claims an independent file audit of those RAM factors.

## 4. Preserved readout and byte-audit scope

Original scalar status and all original trials are written before any
optional complete array audit. The original parent warm/status bytes,
full parent producer subtree, newly saved warm/status identity and FD
producer binding are then checked. Transparent gzip status aliases are
decoded for the original JSON-byte SHA, without reserialization.

The byte phase retains the previous reader's complete scopes: every
declared domain NPZ/NPY; all typed B/Gamma/Pi and beta chunks recombined
by saved byte order; condensed-array references with full shapes and no
truncation; all fourteen exported root/recovery raw files; midpoint
payload descriptors; col-observer unchanged-return flags; and the
available frozen source bytes. Unavailable noncurrent source files are
reported as producer claims, rather than described as independently
hashed files.

Compact reports omit repeated source-entry trees. They identify accepted
and nearest rejected trials and preserve the original distinctions among
node, midpoint, selected-grid, merit and full-RMS stages. A full report
exceeding the bounded text target remains artifact-only while the
targeted scalar/FD/trial views remain available; its observations are not
discarded because of size. An audit failure preserves already written
observations, exception type/repr and the complete traceback. It does
not retroactively relabel the original scientific run as failed.

## 5. CLI and deliverables

Use actual metadata after the completed artifact exists:

~~~bash
python -u computations/root_20261114_read_completed_twenty_prefix.py \
  --request-number "$ACTUAL_REQUEST" \
  --run-id "$ACTUAL_RUN_ID" --artifact-id "$ACTUAL_ARTIFACT_ID" \
  --artifact-name "$ACTUAL_ARTIFACT_NAME" \
  --expected-size "$ACTUAL_ZIP_BYTES" --expected-sha256 "$ACTUAL_ZIP_SHA" \
  --source-commit "$ACTUAL_RUN_SOURCE" \
  --parent-directory "$ORIGINAL_PARENT_DIRECTORY" \
  --parent-warm-sha256 "$ORIGINAL_PARENT_WARM_SHA" \
  --parent-status-sha256 "$ORIGINAL_PARENT_STATUS_SHA" \
  --download-out "$RUNNER_TEMP/pinned-complete-prefix" \
  --out "$RESULTS/completed-prefix-readback" \
  --repository-root "$GITHUB_WORKSPACE"
~~~

The existing scientific environment's NumPy suffices; the readback
entry itself needs no SciPy model import. The ordinary small outputs are
`completed-prefix-readback.json`, `completed-prefix-trial-table.json`,
`completed-prefix-QP-scalars.json`, `completed-prefix-FD.json` and the
initial provisional status. Complete audit details, original report
copies, complete derived status and any failure traceback remain under
`large-arrays/` in the readback artifact. This is a read-only receipt
operation, not a second scientific run or an additional BVP acceptance
condition.
