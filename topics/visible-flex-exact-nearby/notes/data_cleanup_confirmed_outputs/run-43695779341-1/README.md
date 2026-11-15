# Ordinary deletion of one confirmed computational output

Storage administration only: no mathematical target or certificate is evaluated, and no data are uploaded to a Release or Actions artifact.

- Public repository: Rogerhu12/math-research-public.
- Immutable original commit: 269ec92a4543276d0dea7b0f01ed130c8b684902.
- Actual run: 43695779341, attempt 1.
- Selected original files: 1; original bytes: 321489.
- Staged ordinary deletions: 1; bytes: 321489.
- Manifest: deletion-manifest.json; SHA-256 be1691e3bb0f15b7b82f29faf64339b556c6c70dc88e18f0676738814a225094.
- Worker: topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_confirmed_output_cleanup.py; SHA-256 a3eea7caa1374437b7f3071c604573da534f455e16f6a1c8d88dc09996bb07e1.

The exact one-path allowlist comes from the current metadata tree and the fully read original R80 section 6 and source certificate. No generic filename classification is reused. The previous 11834 deleted files are not rehashed; only the one reviewed output version is eligible. The manifest retains every exact path, Git blob, byte count, SHA-256, predeletion commit and original producer/parameter/run reference. All scripts, conclusions, parameter/identity records and unlisted paths remain. Concurrent newer versions are preserved.

## Restore an original input for a continuing calculation

Use the exact manifest entry in the public repository:

~~~sh
git show <predeletion_commit>:<original_path> > <temporary_scientific_file>
~~~

Verify the original byte count and SHA-256 before using the file with its unchanged scientific manifest. Restore only required files to an independent temporary science tree. This copies original bytes; it neither recomputes an accepted stage nor grants a new result. Do not recommit the data or upload it to a Release. Both old successes and failures remain identified by their original public commits and runs.
