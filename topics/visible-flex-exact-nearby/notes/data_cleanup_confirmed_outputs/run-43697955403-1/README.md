# Ordinary deletion of two confirmed computational outputs

Storage administration only: no mathematical target or certificate is evaluated, and no data are uploaded to a Release or Actions artifact.

- Public repository: Rogerhu12/math-research-public.
- Immutable original commit: a39a3783181ae671015efca4c55120d4269ad1c5.
- Actual run: 43697955403, attempt 1.
- Selected original files: 2; original bytes: 1305312.
- Staged ordinary deletions: 2; bytes: 1305312.
- Manifest: deletion-manifest.json; SHA-256 052a94839d830423426e29f41f9452bfa40ba3f163bbc7dac171083bc20b9a62.
- Worker: topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_confirmed_output_cleanup.py; SHA-256 09f9d899988b5699169d57e12f0235c446b0d928571bf866fcc63a740ba7fa77.

The exact two-path allowlist comes from the current metadata tree, the fully read original R57 sections 2 and 5, R56 section 5, and both unchanged producers. No generic filename classification is reused. The previous 11834 deleted files and the later R80 deletion remain untouched and are not rehashed; only these two reviewed output versions are eligible. The manifest retains every exact path, Git blob, byte count, SHA-256, predeletion commit and original producer/parameter/run reference. All scripts, conclusions, parameter/identity records and unlisted paths remain. Concurrent newer versions are preserved.

## Restore an original input for a continuing calculation

Use the exact manifest entry in the public repository:

~~~sh
git show <predeletion_commit>:<original_path> > <temporary_scientific_file>
~~~

Verify the original byte count and SHA-256 before using the file with its unchanged scientific manifest. Restore only required files to an independent temporary science tree. This copies original bytes; it neither recomputes an accepted stage nor grants a new result. Do not recommit the data or upload it to a Release. Both old successes and failures remain identified by their original public commits and runs.
