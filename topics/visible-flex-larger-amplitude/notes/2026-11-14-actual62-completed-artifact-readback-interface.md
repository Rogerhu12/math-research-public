# Actual62 completed-artifact readback and byte audit

Date: 2026-11-14  
Author: ChatGPT, amplitude workstream  
Classification: read-only transport and receipt interface; no new scientific result.

## Entry and pinned input

The public actual62 prefix job completed while the local executor became
unavailable. This independent reader moves the already authorized
readback to public GitHub Actions. It does not rerun the prefix solver,
tail, optimization, model actions, or finite differences.

Entry:
[computations/root_20261114_read_actual62_receipts.py](../computations/root_20261114_read_actual62_receipts.py),
36,728 bytes; SHA-256
03a7868435cba5c2f71bdf04faaf2ae85c11b33b44904b472499b8bad7b1c819;
Git blob 0804383e39551aca868cf2204dfbf35c66a4b32d.

The fixed original metadata, independently read from GitHub's Actions
artifact endpoint, is:

| Field | Original value |
|---|---|
| Repository | Rogerhu12/math-research-public |
| Run | 43642866864 |
| Source | cc813fa7521098fdeba86b8bf8c0fe7d8c96bba0 |
| Artifact | 14132473712 |
| Name | visible-followup-condensedqp-43642866864-1 |
| ZIP bytes | 492837872 |
| ZIP SHA-256 | 220ad8c51a147942b663cd9196f009ecc976d1ff270b0348e494e08cf5e90730 |

The unchanged transport source is
[exact_20261114_fetch_pinned_public_artifact.py](../computations/exact_20261114_fetch_pinned_public_artifact.py),
SHA-256
51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859.

The adapter changes only its in-memory pin, receipt schema, source-commit
check, and truthful adapter metadata. It retains the original complete
extraction function, HTTPS handling, Authorization stripping, complete
ZIP SHA, all-member path/type checks, every file CRC/size/SHA, exclusive
publication, receipt-last move and read-only sealing. The verified
payload is published directly at --download-out, without an additional
files or artifact directory.

## Execution

Use Python 3.12 and numpy==2.3.5. SciPy and Node are not dependencies.
The reader and unchanged transport must be together in the topic's
computations directory. Keep the computations checkout for source-SHA
checks. The four current eighteen-query source files are mandatory and
independently pinned.

With C naming that computations directory and OUT an independent output
directory:

~~~bash
python -u "$C/root_20261114_read_actual62_receipts.py" \
  --download-out "$RUNNER_TEMP/actual62-original-verified" \
  --out "$OUT/request62-readback" \
  --repository-root "$GITHUB_WORKSPACE"
~~~

Both final directories must be fresh. The download destination's parent
must already exist under RUNNER_TEMP. Supply GITHUB_TOKEN only through
the step environment. The reader has no credential CLI argument.

The source received a complete manual interface check. The unavailable
executor prevented a local AST check; the ordinary Actions compile step
can precede this readback. This is an implementation fact, not a new
scientific acceptance condition.

## Small reports precede byte auditing

The entry first saves provisional original status scalars, then reads the
actual saved model/status/warm and FD. It checks the actual60 parent warm
SHA bc7cadbc17f17832785ace32b011136fd43c04147d450d557730de0f05d40a23
and decoded original parent-status SHA
5b419af7340777328184d7699cf1a4de539cd608c889f6e4f81fe549b253a922.
The complete parent producer subtree must survive. The new status and FD
must bind the actual new warm and its complete producer.

It writes:

- actual62-original-status-provisional.json: original status scalars and
  exact decoded SHA, explicitly before full identity validation.
- actual62-readback.json: actual new warm compressed SHA, original status
  decoded SHA, original accepted trial and its immediately preceding
  rejection, original FD and QP scalars, audit status and scope.
- actual62-original-trials.json: all original trial/domain/RMS/selected
  query summaries.
- actual62-original-FD.json: original response diagnostics and actual
  warm/source bindings; no FD execution.
- actual62-original-QP-scalars.json: original same-model comparison,
  last working-set observations, radial repairs and recovery scalars.

These are semantic reports for distinct questions. They do not transmit
a large original JSON tree in mechanical chunks. Full producer ancestry
is checked in the original files and represented by a canonical identity.

All derived detailed audits go under large-arrays and are artifact-only.
The complete original download directory also remains an artifact input,
not material to copy into Git.

## Byte-audit scope

NumPy is used only for NPZ decoding, dtype/shape metadata, byte conversion
and hashing. The entry imports no mathematical module and performs no
norm, dot product, RHS, Jacobian, ODE, boundary, QR or QP action.

It checks every declared domain NPZ and NPY identity, assembles the
original bytes of all eighteen B/Gamma/Pi groups and the complete margin
vector, reconstructs the producer's model-metadata SHA, and compares the
parent mesh/states/RHS bytes to the saved base.

It checks every condensed NPZ part and every complete array reference
in the original full result. Complete arrays are traversed by their
original parts; there is no small-member limit that could truncate a
basis. It separately hashes all fourteen exported condensed-root and
recovery raw files with their declared dtype/shape/size.

The observer scope records original return-preservation flags and the
midpoint payload descriptors. Any midpoint payload not matched to an
original declared descriptor remains explicitly unmatched. A source
absent from the receipt checkout is recorded as unavailable, not counted
as independently verified; current four entry pins are required.

Full receipts are:

- large-arrays/complete-transport-receipt.json.
- large-arrays/complete-original-byte-audit.json.
- large-arrays/complete-readback-status.json.

The original complete chain factor was kept in memory and not exported
as factor files. Its reported identity does not become an independent
factor-file byte audit.

## Failure and interpretation

Any failure preserves the already-written original observations. The
small status records the phase, error type and local exception repr;
large-arrays/failure-traceback.txt retains the complete traceback with a
file SHA. Network errors remain protected by the original transport's
credential-safe error handling.

If a derived main report exceeds the bounded-text limit, its complete
version stays in the artifact and the small status points to the
separate trial/FD reports. A size issue never clears earlier numeric
observations.

Reader success means the stated existing observations and byte checks
completed. It does not change the original solver flags or establish a
complete BVP, nonlinear native tail, closed surface or topic completion.
A reader failure is a readback failure, not a reclassification of the
already completed original scientific run.
