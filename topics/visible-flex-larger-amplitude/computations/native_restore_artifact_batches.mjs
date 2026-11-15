// Source-only restoration draft. It does not import a numerical reader/solver.
import fsp from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {
  requireThat, equal, sha256, readObject, writeJSON, verifyDownloaded, restoreVerifiedPayload
} from './native_closed_iteration_bytes.mjs';
import {loadLockedSDK, cleanError} from './native_live_artifact_supervisor.mjs';

export async function restore(specFile) {
  const spec = await readObject(specFile);
  equal(spec.schema, 'native-live-byte-artifact-restore-spec-v1', 'Explicit restore specification');
  const raw = await fsp.readFile(spec.catalog_file);
  equal(sha256(raw), spec.catalog_sha256, 'Pinned original catalog bytes');
  const catalog = JSON.parse(raw);
  equal(catalog.schema, 'native-live-verified-artifact-catalog-v1', 'Original byte catalog schema');
  for (const key of ['output_directory', 'work_directory'])
    requireThat(path.isAbsolute(spec[key]), 'Explicit new ' + key);
  const output = path.resolve(spec.output_directory), work = path.resolve(spec.work_directory);
  requireThat(output !== work && !output.startsWith(work + path.sep) && !work.startsWith(output + path.sep),
    'Disjoint restored output and download directories');
  const sdk = await loadLockedSDK(spec);
  await fsp.mkdir(spec.work_directory, {recursive: false});
  await fsp.mkdir(spec.output_directory, {recursive: false});
  const receipt = {schema: 'native-live-byte-artifact-restoration-v1', catalog_sha256: sha256(raw),
    batches: [], completed: false, original_names_and_bytes_restored: true,
    no_scientific_program_called: true, native_acceptance_not_determined: true};
  try {
    for (const batch of catalog.batches) {
      requireThat(batch.members_verified === true && batch.digest_mismatch === false && batch.artifact,
        'A remotely verified original batch is required; partial catalog is not silently skipped');
      const directory = path.join(spec.work_directory, 'batch-' + String(batch.batch).padStart(4, '0'));
      await fsp.mkdir(directory, {recursive: false});
      const options = {path: directory, expectedHash: 'sha256:' + batch.artifact.sha256};
      // Later runs use the SDK's public read API. The token stays in memory and
      // is never included in any receipt or original scientific specification.
      if (spec.find_by) options.findBy = {
        repositoryOwner: spec.find_by.repository_owner,
        repositoryName: spec.find_by.repository_name,
        workflowRunId: Number(catalog.run_id), token: process.env.GITHUB_TOKEN || process.env.GH_TOKEN
      };
      const downloaded = await sdk.client.downloadArtifact(batch.artifact.id, options);
      requireThat(downloaded.digestMismatch === false, 'Original artifact digest mismatch during restore');
      const manifest = await verifyDownloaded(directory, batch.manifest);
      const restored = await restoreVerifiedPayload(directory, spec.output_directory, manifest);
      receipt.batches.push({batch: batch.batch, artifact: batch.artifact, manifest: batch.manifest, ...restored});
      await writeJSON(path.join(spec.work_directory, 'restore-receipt.json'), receipt);
      await fsp.rm(directory, {recursive: true});
    }
    receipt.completed = true;
  } catch (error) { receipt.actual_storage_error = cleanError(error); throw error; }
  finally { await writeJSON(path.join(spec.work_directory, 'restore-receipt.json'), receipt); }
  return receipt;
}
if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  try {
    requireThat(process.argv.length === 4 && process.argv[2] === '--spec', 'Usage: restore --spec SPEC.json');
    await restore(path.resolve(process.argv[3]));
  } catch (error) { process.stderr.write(JSON.stringify({storage_restore_error: cleanError(error)}) + '\n'); process.exitCode = 86; }
}
