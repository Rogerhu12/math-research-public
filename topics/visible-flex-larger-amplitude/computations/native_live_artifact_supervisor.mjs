// Source-only integration draft. Never run as a replacement numerical solver.
import fs from 'node:fs';
import fsp from 'node:fs/promises';
import path from 'node:path';
import {spawn} from 'node:child_process';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
import {
  requireThat, equal, sha256, checkedReceipt, readObject, writeJSON,
  CLOSURE_SOURCE_PINS, discoverClosed, sealBatch, verifyDownloaded,
  evictVerifiedPayloads
} from './native_closed_iteration_bytes.mjs';

const ARTIFACT_RUNTIME_KEYS = ['ACTIONS_RUNTIME_TOKEN', 'ACTIONS_RUNTIME_URL',
  'ACTIONS_RESULTS_URL', 'ACTIONS_CACHE_URL'];
const delay = milliseconds => new Promise(resolve => setTimeout(resolve, milliseconds));
export function cleanError(error) {
  let message = String(error && error.message || error);
  for (const key of [...ARTIFACT_RUNTIME_KEYS, 'GITHUB_TOKEN', 'GH_TOKEN']) {
    const value = process.env[key]; if (value) message = message.split(value).join('<redacted>');
  }
  return {name: String(error && error.name || 'Error'), code: error && error.code || null,
    message: message.replace(/https?:\/\/\S+/g, '<transport-url>')};
}
export async function loadLockedSDK(spec) {
  requireThat(process.env.GITHUB_ACTIONS === 'true', 'This transport entry is Actions-only');
  // A future workflow must create a real complete lock with integrity and run
  // npm ci from that lock. No lock value is invented in this source draft.
  requireThat(spec.sdk && path.isAbsolute(spec.sdk.dependency_root), 'Explicit installed SDK root');
  await checkedReceipt(spec.sdk.dependency_root, spec.sdk.lock);
  const lock = await readObject(path.join(spec.sdk.dependency_root, spec.sdk.lock.file));
  const locked = lock.packages && lock.packages['node_modules/@actions/artifact'];
  requireThat(locked && locked.version === '2.3.2' && typeof locked.integrity === 'string',
    'Actual lock must include @actions/artifact 2.3.2 and its integrity');
  const require = createRequire(path.join(spec.sdk.dependency_root, 'package.json'));
  const packagePath = require.resolve('@actions/artifact/package.json');
  const pkg = JSON.parse(await fsp.readFile(packagePath, 'utf8'));
  equal(pkg.name, '@actions/artifact', 'Installed SDK name');
  equal(pkg.version, '2.3.2', 'Installed SDK fixed version');
  const module = require('@actions/artifact');
  requireThat(typeof module.DefaultArtifactClient === 'function', 'Actual SDK client constructor');
  return {client: new module.DefaultArtifactClient(), identity: {
    version: pkg.version, package_json_sha256: sha256(await fsp.readFile(packagePath)),
    dependency_lock: spec.sdk.lock,
    install_scope: 'Workflow npm-ci identity; this runtime check is not a full node_modules content audit'
  }};
}
function disjoint(a, b) {
  const x = path.resolve(a), y = path.resolve(b);
  return x !== y && !x.startsWith(y + path.sep) && !y.startsWith(x + path.sep);
}
function specChecks(spec) {
  equal(spec.schema, 'native-live-byte-artifact-supervisor-spec-v1', 'Supervisor specification');
  requireThat(Array.isArray(spec.command) && spec.command.length > 0 &&
    spec.command.every(x => typeof x === 'string' && !x.includes('\0')), 'Unmodified command argv array');
  for (const key of ['cwd', 'live_output', 'storage_directory'])
    requireThat(path.isAbsolute(spec[key]), 'Explicit absolute ' + key);
  requireThat(disjoint(spec.live_output, spec.storage_directory), 'Storage does not occupy the live client output');
  equal(spec.source_pins, CLOSURE_SOURCE_PINS, 'Published immutable closure sources');
  equal(spec.iterations_per_batch, 2, 'Two complete closed iterations per normal batch');
  requireThat(Number.isInteger(spec.max_batches) && spec.max_batches >= 304 && spec.max_batches < 500,
    'Explicit artifact budget with room for final workflow artifacts');
  requireThat(typeof spec.evict_verified_payloads === 'boolean', 'Eviction is an explicit storage policy');
  requireThat(/^[A-Za-z0-9_.-]{1,80}$/.test(spec.artifact_prefix), 'Safe artifact namespace');
  requireThat(Number.isInteger(spec.poll_milliseconds) && spec.poll_milliseconds >= 1000,
    'Explicit non-busy polling interval');
  requireThat(Number.isInteger(spec.compression_level) && spec.compression_level >= 0 &&
    spec.compression_level <= 9 && Number.isInteger(spec.retention_days) && spec.retention_days >= 1,
    'Explicit artifact compression and retention policy');
}

export async function supervise(specFile) {
  const specRaw = await fsp.readFile(specFile), spec = JSON.parse(specRaw);
  specChecks(spec);
  requireThat(process.env.ACTIONS_RUNTIME_TOKEN && process.env.ACTIONS_RESULTS_URL,
    'Run the supervisor as a JavaScript action with artifact runtime credentials');
  const sdk = await loadLockedSDK(spec);
  await fsp.mkdir(spec.storage_directory, {recursive: false});
  const catalogFile = path.join(spec.storage_directory, 'catalog.json');
  const catalog = {schema: 'native-live-verified-artifact-catalog-v1',
    specification_sha256: sha256(specRaw), source_pins: spec.source_pins, sdk: sdk.identity,
    run_id: process.env.GITHUB_RUN_ID, run_attempt: process.env.GITHUB_RUN_ATTEMPT,
    evict_verified_payloads: spec.evict_verified_payloads, batches: [],
    child_exit: null, storage_error: null, scientific_result_is_owned_by_original_driver: true};
  await fsp.writeFile(path.join(spec.storage_directory, 'supervisor-spec.json'), specRaw, {flag: 'wx'});
  await writeJSON(catalogFile, catalog);
  const childEnv = {...process.env};
  for (const key of ARTIFACT_RUNTIME_KEYS) delete childEnv[key];
  // Preserve the rules runner's existing GH_TOKEN/GITHUB_TOKEN environment.
  // No artifact token or signed URL is serialized into any output file.
  let childDone = false, childExit = null;
  const child = spawn(spec.command[0], spec.command.slice(1), {
    cwd: spec.cwd, env: childEnv, shell: false, stdio: 'inherit'
  });
  const childFinished = new Promise(resolve => {
    child.once('error', error => { childDone = true; childExit = {code: null, signal: null,
      launch_error: cleanError(error)}; resolve(); });
    child.once('close', (code, signal) => { childDone = true;
      if (!childExit) childExit = {code, signal, launch_error: null}; resolve(); });
  });
  const forward = signal => { catalog.supervisor_signal = signal; child.kill(signal); };
  const onTerm = () => forward('SIGTERM'), onInt = () => forward('SIGINT');
  process.on('SIGTERM', onTerm); process.on('SIGINT', onInt);
  const seen = new Set();
  try {
    while (true) {
      const pending = await discoverClosed(spec.live_output, seen, spec.source_pins);
      if (pending.length < 2 && !childDone) { await delay(spec.poll_milliseconds); continue; }
      if (!pending.length && childDone) break;
      const closed = pending.slice(0, 2), batch = catalog.batches.length;
      requireThat(batch < spec.max_batches, 'Storage artifact budget exhausted; raw files retained');
      const name = 'batch-' + String(batch).padStart(4, '0');
      const staging = path.join(spec.storage_directory, name + '-staging');
      const verification = path.join(spec.storage_directory, name + '-verification');
      const sealed = await sealBatch(spec.live_output, staging, closed, {
        run_id: catalog.run_id, run_attempt: catalog.run_attempt, batch,
        source_pins: spec.source_pins, supervisor_specification_sha256: sha256(specRaw)
      });
      const artifactName = spec.artifact_prefix + '-' + catalog.run_id + '-' + catalog.run_attempt + '-' +
        String(batch).padStart(4, '0') + '-' + sealed.receipt.sha256.slice(0, 12);
      const record = {batch, artifact_name: artifactName, keys: closed.map(x => x.key),
        manifest: sealed.receipt, artifact: null, members_verified: false,
        digest_mismatch: null, eviction: null};
      catalog.batches.push(record);
      await writeJSON(path.join(spec.storage_directory, name + '-manifest.json'), sealed.manifest);
      await writeJSON(catalogFile, catalog);
      const uploaded = await sdk.client.uploadArtifact(artifactName, sealed.files, staging, {
        compressionLevel: spec.compression_level, retentionDays: spec.retention_days
      });
      requireThat(Number.isSafeInteger(uploaded.id) && uploaded.id > 0 &&
        /^[0-9a-f]{64}$/.test(uploaded.digest), 'A real finalized artifact id and SHA256 are required');
      record.artifact = {id: uploaded.id, name: artifactName, size: uploaded.size, sha256: uploaded.digest};
      await writeJSON(catalogFile, catalog);
      await fsp.mkdir(verification, {recursive: false});
      const downloaded = await sdk.client.downloadArtifact(uploaded.id, {
        path: verification, expectedHash: 'sha256:' + uploaded.digest
      });
      requireThat(downloaded.digestMismatch === false, 'Downloaded artifact digest mismatch');
      const manifest = await verifyDownloaded(verification, sealed.receipt);
      record.digest_mismatch = false; record.members_verified = true;
      record.verified_member_count = manifest.members.length;
      record.verified_bytes = manifest.members.reduce((s, x) => s + x.bytes, 0);
      // The durable remote identity/catalog precedes every original unlink.
      await writeJSON(path.join(spec.storage_directory, name + '-verified.json'), record);
      await writeJSON(catalogFile, catalog);
      if (spec.evict_verified_payloads) {
        const journal = await fsp.open(path.join(spec.storage_directory, name + '-evictions.jsonl'), 'wx');
        try { record.eviction = await evictVerifiedPayloads(spec.live_output, manifest, record,
          item => journal.write(JSON.stringify(item) + '\n')); await journal.sync(); }
        finally { await journal.close(); }
      }
      for (const item of closed) seen.add(item.key);
      record.completed = true;
      await writeJSON(catalogFile, catalog);
      // Removing hardlink staging is necessary to actually reclaim inode data.
      // Only our freshly allocated work directories are removed here.
      await fsp.rm(staging, {recursive: true});
      await fsp.rm(verification, {recursive: true});
    }
  } catch (error) {
    catalog.storage_error = cleanError(error);
    // Do not kill, pause, restart or alter scientific parameters after a storage
    // failure. Retain every unverified original; the final ordinary artifact
    // remains responsible for active/failed/partial directories.
    await writeJSON(catalogFile, catalog);
  }
  await childFinished;
  process.removeListener('SIGTERM', onTerm); process.removeListener('SIGINT', onInt);
  catalog.child_exit = childExit;
  catalog.completed_at = new Date().toISOString();
  catalog.storage_completed = !catalog.storage_error;
  catalog.native_acceptance_not_determined = true;
  await writeJSON(catalogFile, catalog);
  return {child_exit: childExit, storage_error: catalog.storage_error,
    exit_code: Number.isInteger(childExit.code) && childExit.code !== 0 ? childExit.code :
      childExit.signal || childExit.launch_error ? 87 : catalog.storage_error ? 86 : 0};
}
if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  try {
    requireThat(process.argv.length === 4 && process.argv[2] === '--spec', 'Usage: supervisor --spec SPEC.json');
    const answer = await supervise(path.resolve(process.argv[3])); process.exitCode = answer.exit_code;
  } catch (error) { process.stderr.write(JSON.stringify({storage_startup_error: cleanError(error)}) + '\n'); process.exitCode = 86; }
}
