// Source-only draft. Pure byte I/O; no mathematical module is loaded.
import fs from 'node:fs';
import fsp from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';

export const CLOSURE_SOURCE_PINS = Object.freeze({
  client: '7aa2aba10e44f0a0fd0e6eee47e9239a2f2244bb9663b8ec5ede294edc71bb64',
  hook: '0e802785329c73d5a951ca69942414ca5dcc40a9284dae9d31c4ca6cb819daa1'
});
export function requireThat(value, label) { if (!value) throw Error(label); }
export function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === 'object') return Object.fromEntries(
    Object.keys(value).sort().map(k => [k, stable(value[k])]));
  return value;
}
export function equal(a, b, label) {
  requireThat(JSON.stringify(stable(a)) === JSON.stringify(stable(b)), label);
}
export const sha256 = raw => crypto.createHash('sha256').update(raw).digest('hex');
export function relativeName(name) {
  requireThat(typeof name === 'string' && name.length > 0 && !name.includes('\\') &&
    !name.includes('\0') && !path.posix.isAbsolute(name) &&
    name.split('/').every(p => p && p !== '.' && p !== '..'), 'Unsafe relative evidence path');
  return name;
}
export async function safePath(root, name, allowMissing = false) {
  relativeName(name);
  let current = path.resolve(root);
  const rootStat = await fsp.lstat(current);
  requireThat(rootStat.isDirectory() && !rootStat.isSymbolicLink(), 'Regular root directory required');
  const parts = name.split('/');
  for (let i = 0; i < parts.length; i++) {
    current = path.join(current, parts[i]);
    try {
      const st = await fsp.lstat(current);
      requireThat(!st.isSymbolicLink(), 'Symlink evidence path is not supported');
      if (i + 1 < parts.length) requireThat(st.isDirectory(), 'Non-directory evidence parent');
    } catch (error) {
      if (!(allowMissing && error.code === 'ENOENT')) throw error;
    }
  }
  return current;
}
export async function fileReceipt(root, name) {
  const file = await safePath(root, name), before = await fsp.stat(file);
  requireThat(before.isFile(), 'Only regular evidence files are archived');
  const hash = crypto.createHash('sha256'); let bytes = 0;
  for await (const chunk of fs.createReadStream(file)) { hash.update(chunk); bytes += chunk.length; }
  const after = await fsp.stat(file);
  requireThat(before.dev === after.dev && before.ino === after.ino &&
    before.size === after.size && bytes === after.size && before.mtimeMs === after.mtimeMs,
    'Evidence file changed while hashing');
  return {file: name, bytes, sha256: hash.digest('hex')};
}
export async function checkedReceipt(root, descriptor) {
  const actual = await fileReceipt(root, descriptor.file);
  equal(actual, {file: descriptor.file, bytes: descriptor.bytes, sha256: descriptor.sha256},
    'Evidence descriptor mismatch: ' + descriptor.file);
  return actual;
}
export async function readObject(file) {
  const raw = await fsp.readFile(file);
  const decoded = raw[0] === 31 && raw[1] === 139 ? zlib.gunzipSync(raw) : raw;
  return JSON.parse(decoded.toString('utf8'));
}
export async function checkedObject(root, descriptor) {
  await checkedReceipt(root, descriptor);
  return readObject(await safePath(root, descriptor.file));
}
export async function writeJSON(file, value) {
  await fsp.mkdir(path.dirname(file), {recursive: true});
  const temporary = file + '.new-' + crypto.randomBytes(6).toString('hex');
  const handle = await fsp.open(temporary, 'wx');
  try { await handle.writeFile(JSON.stringify(value) + '\n'); await handle.sync(); }
  finally { await handle.close(); }
  await fsp.rename(temporary, file);
  const directory = await fsp.open(path.dirname(file), 'r');
  try { await directory.sync(); } finally { await directory.close(); }
}
export async function regularFiles(root, prefix = '') {
  const directory = prefix ? await safePath(root, prefix) : root;
  const entries = await fsp.readdir(directory, {withFileTypes: true}), output = [];
  for (const entry of entries.sort((a, b) => a.name.localeCompare(b.name))) {
    const name = prefix ? prefix + '/' + entry.name : entry.name;
    relativeName(name);
    requireThat(!entry.isSymbolicLink(), 'Archive does not follow symlinks');
    if (entry.isDirectory()) output.push(...await regularFiles(root, name));
    else { requireThat(entry.isFile(), 'Unsupported evidence entry'); output.push(name); }
  }
  return output;
}

// This reads only complete append-only lines. A partially written last line is
// ignored. Neither a stable mtime nor a QR solve substage counts as closure.
export async function discoverClosed(liveRoot, seen, sourcePins) {
  equal(sourcePins, CLOSURE_SOURCE_PINS, 'This storage draft observes the published closure contract');
  try { await fsp.access(liveRoot); } catch (e) { if (e.code === 'ENOENT') return []; throw e; }
  const calls = (await fsp.readdir(liveRoot)).filter(x => /^call-\d{4}$/.test(x)).sort();
  const logs = [];
  for (const callName of calls) {
    const callRoot = await safePath(liveRoot, callName); let raw;
    try { raw = await fsp.readFile(await safePath(callRoot, 'current-corrections.jsonl', true)); }
    catch (e) { if (e.code === 'ENOENT') continue; throw e; }
    if (raw.lastIndexOf(10) >= 0) logs.push({callName, callRoot, raw});
  }
  // The constructor writes the live spec before a completed correction line.
  // Do not race its initial file creation by parsing the spec before that point.
  if (!logs.length) return [];
  const specPath = await safePath(liveRoot, 'live-client-spec.json.gz', true);
  try { await fsp.access(specPath); } catch (e) { if (e.code === 'ENOENT') return []; throw e; }
  const spec = await readObject(specPath);
  equal(spec.schema, 'noj-primal-live-current576-tail-client-spec-v1', 'Actual live specification schema');
  equal(spec.source_sha256, sourcePins.client, 'Actual frozen live client');
  equal(spec.hook_sha256, sourcePins.hook, 'Actual frozen live hook');
  const found = [];
  for (const {callName, raw} of logs) {
    const end = raw.lastIndexOf(10); if (end < 0) continue;
    const lines = raw.subarray(0, end + 1).toString('utf8').split('\n').slice(0, -1);
    for (const line of lines) {
      const record = JSON.parse(line);
      if (record.linear_direction_returned !== true) continue;
      const it = record.nonlinear_iteration, call = record.native_call;
      requireThat(Number.isInteger(it) && it >= 0 && it < 32 &&
        callName === 'call-' + String(call).padStart(4, '0') &&
        record.snapshot_sequence === it, 'Closed record call/iteration identity');
      const iteration = 'iteration-' + String(it).padStart(3, '0');
      equal(record.iteration_directory, iteration, 'Closed iteration path');
      const key = callName + '/' + iteration; if (seen.has(key)) continue;
      const dir = await safePath(liveRoot, key);
      const returned = await readObject(await safePath(dir, 'returned-correction.json'));
      const exit = await readObject(await safePath(dir, 'qr-exit.json'));
      equal(returned, record.direction, 'Returned correction agrees with completed append record');
      equal(exit, record.qr_exit, 'Original exited child agrees with completed append record');
      requireThat(record.snapshot_completed === true, 'Original completed snapshot flag');
      requireThat(exit.status === 0 && exit.signal === null && exit.error === null,
        'Only a closed successful child is eligible for background sealing');
      equal(returned.schema, 'noj-primal-live-current576-returned-correction-v1', 'Returned correction schema');
      const snapshot = await checkedObject(path.join(dir, 'snapshot'), returned.snapshot_result);
      const result = await checkedObject(path.join(dir, 'qr'), returned.result);
      for (const object of [returned, exit, snapshot, result]) {
        equal(object.native_call, call, 'Same actual closed request');
        equal(object.nonlinear_iteration, it, 'Same actual closed nonlinear iteration');
        equal(object.snapshot_sequence, it, 'Same actual closed snapshot sequence');
      }
      equal(snapshot.source_sha256, sourcePins.client, 'Snapshot original client identity');
      equal(snapshot.hook_sha256, sourcePins.hook, 'Snapshot original hook identity');
      equal(result.source_sha256, spec.bridge.source_sha256, 'Exited original child source');
      equal(result.system_source_sha256, spec.bridge.system_source_sha256, 'Exited original child binder');
      equal(snapshot.current_state_sha256, returned.current_state_sha256, 'Closed current state receipt');
      equal(result.current_state_sha256, returned.current_state_sha256, 'Closed direction state receipt');
      await checkedReceipt(path.join(dir, 'snapshot'), snapshot.manifest);
      await checkedReceipt(path.join(dir, 'snapshot'), snapshot.context);
      for (const key of ['input_binding', 'direction_checkpoint', 'array_manifest', 'native_delta'])
        await checkedReceipt(path.join(dir, 'qr'), returned[key]);
      found.push({key, call, iteration: it, record, original_complete_line_base64:
        Buffer.from(line + '\n').toString('base64')});
    }
  }
  return found;
}

export function reclaimable(name) {
  return /^call-\d{4}\/iteration-\d{3}\/(snapshot|qr)\/large-arrays\/.+/.test(name);
}
export async function sealBatch(liveRoot, stagingRoot, closed, identity) {
  await fsp.mkdir(stagingRoot, {recursive: false});
  const names = new Set(['live-client-spec.json.gz', 'live-client-intent.json', 'verified-launch-intent.json']);
  for (const item of closed) {
    names.add(item.key.split('/')[0] + '/request.json');
    for (const name of await regularFiles(liveRoot, item.key)) names.add(name);
  }
  const members = [];
  for (const name of [...names].sort()) {
    const receipt = await fileReceipt(liveRoot, name), source = await safePath(liveRoot, name);
    const destination = path.join(stagingRoot, 'payload', name);
    await fsp.mkdir(path.dirname(destination), {recursive: true});
    // No bulk copy and no chmod on the linked inode. EXDEV is a storage failure.
    await fsp.link(source, destination);
    members.push(receipt);
  }
  const manifest = {schema: 'native-live-closed-iteration-byte-batch-v1', identity,
    scope: 'Original files and complete returned records; no numerical recomputation',
    closed_records: closed.map(x => ({key: x.key, call: x.call, iteration: x.iteration,
      original_complete_line_base64: x.original_complete_line_base64})), members,
    payload_candidates: members.filter(x => reclaimable(x.file)).map(x => x.file),
    metadata_and_raw_bytes_unchanged: true, native_acceptance_not_determined: true};
  await writeJSON(path.join(stagingRoot, 'batch-manifest.json'), manifest);
  const receipt = await fileReceipt(stagingRoot, 'batch-manifest.json');
  return {manifest, receipt, files: (await regularFiles(stagingRoot)).map(x => path.join(stagingRoot, x))};
}
export async function verifyDownloaded(directory, expectedManifest) {
  await checkedReceipt(directory, expectedManifest);
  const manifest = await readObject(await safePath(directory, expectedManifest.file));
  equal(manifest.schema, 'native-live-closed-iteration-byte-batch-v1', 'Remote batch manifest schema');
  const names = manifest.members.map(x => 'payload/' + relativeName(x.file));
  requireThat(new Set(names).size === names.length, 'No duplicate batch members');
  equal((await regularFiles(directory)).sort(), ['batch-manifest.json', ...names].sort(),
    'Remote batch has exactly the original file set');
  for (const member of manifest.members)
    await checkedReceipt(path.join(directory, 'payload'), member);
  equal(manifest.payload_candidates, manifest.members.filter(x => reclaimable(x.file)).map(x => x.file),
    'Only explicit original large-array paths can be reclaimed');
  return manifest;
}
export async function evictVerifiedPayloads(liveRoot, manifest, remoteReceipt, onEach) {
  requireThat(remoteReceipt.members_verified === true && remoteReceipt.digest_mismatch === false &&
    Number.isSafeInteger(remoteReceipt.artifact.id), 'Durable remotely verified receipt required before eviction');
  let bytes = 0, files = 0;
  for (const member of manifest.members) {
    if (!reclaimable(member.file)) continue;
    await checkedReceipt(liveRoot, member);
    await fsp.unlink(await safePath(liveRoot, member.file));
    bytes += member.bytes; files++;
    if (onEach) await onEach({file: member.file, bytes: member.bytes, total_bytes: bytes, total_files: files});
  }
  return {bytes, files};
}
export async function restoreVerifiedPayload(verifiedRoot, outputRoot, manifest) {
  await fsp.mkdir(outputRoot, {recursive: true});
  let restored = 0, alreadyPresent = 0;
  for (const member of manifest.members) {
    const target = await safePath(outputRoot, member.file, true);
    try { await fsp.lstat(target); await checkedReceipt(outputRoot, member); alreadyPresent++; continue; }
    catch (e) { if (e.code !== 'ENOENT') throw e; }
    await fsp.mkdir(path.dirname(target), {recursive: true});
    await fsp.copyFile(await safePath(path.join(verifiedRoot, 'payload'), member.file), target, fs.constants.COPYFILE_EXCL);
    await checkedReceipt(outputRoot, member); restored++;
  }
  return {restored_files: restored, identical_existing_files: alreadyPresent,
    complete_payloads_restored_with_original_names: true};
}
