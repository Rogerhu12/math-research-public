# Ordinary deletion of reproducible data

Storage administration only: no mathematical target or certificate is evaluated, and no data are uploaded to a Release or Actions artifact.

- Public repository: Rogerhu12/math-research-public.
- Immutable original commit: 9c4d5366389693f3bebeb2be28974966317137ae.
- Actual run: 43679889657, attempt 1.
- Selected original files: 11834; original bytes: 1905188820.
- Staged ordinary deletions: 11834; bytes: 1905188820.
- Manifest: deletion-manifest.json.gz; SHA-256 bc3f23987ac4ab967b97d02df6ad260c4adccde45c34716031be057ab5da29e9.
- Worker: topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reproducible_data_cleanup.py; SHA-256 40c0f3df80a240f895c26023a62ac09a57dac05f639f22a2f11ff50257cbd868.

The manifest retains each path, Git blob, byte count, SHA-256, predeletion commit, and available original producer/parameter/run metadata. Scripts, conclusions, small parameter/identity records, and explicitly named parameter inputs are retained. Concurrent newer versions are preserved.

## Restore an original input for a continuing calculation

Use the exact manifest entry in the public repository:

~~~sh
git show <predeletion_commit>:<original_path> > <temporary_scientific_file>
~~~

Verify the original byte count and SHA-256 before using the file with its unchanged scientific manifest. Restore only required files to an independent temporary science tree. This copies original bytes; it neither recomputes an accepted stage nor grants a new result. Do not recommit the data or upload it to a Release. Both old successes and failures remain identified by their original public commits and runs.

2026-11-20 storage update: the large compressed deletion inventory itself is now kept only in normal Git history under root rule15. Its complete identity and byte-for-byte restoration commit are in `../../2026-11-20-reproducible-data-history-pointers.json`. The original process/publication receipts and hashes above remain unchanged; no accepted scientific target was rerun.
