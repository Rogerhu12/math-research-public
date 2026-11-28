#!/usr/bin/env node
// Restore complete historical GENERATED DESCRIPTIONS from unchanged canonical
// files plus exact byte splices. This imports only Node standard libraries.
// It never imports, constructs or evaluates a numerical model or old producer.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const SCHEMA = 'legacy-generated-adapter-exact-ascii-byte-deltas-v1';
const VOLUMES = [
  {
    "path": "topics/visible-flex-larger-amplitude/computations/legacy-preparation-descriptions-retention-67-complete-byte-deltas.json",
    "bytes": 56738,
    "sha256": "a6fdd94ddc83c80de07dfcdf4f6d42d0f615e30cd068849a3d47f069cf1bde47",
    "git_blob_sha": "9dac4caf59d5555a15e55806fa60c2218d7d580e"
  }
];
const digest = b => crypto.createHash('sha256').update(b).digest('hex');
const gitBlob = b => crypto.createHash('sha1').update(Buffer.concat([
  Buffer.from('blob ' + b.length + '\0', 'ascii'), b])).digest('hex');
function recordCheck(b, r, label) {
  if (b.length !== r.bytes || digest(b) !== r.sha256 ||
      gitBlob(b) !== r.git_blob_sha) {
    throw Error('Complete byte identity differs: ' + label);
  }
}
function safePath(root, relative) {
  if (typeof relative !== 'string' || path.isAbsolute(relative) ||
      relative.split('/').some(x => x === '..' || x === '')) {
    throw Error('Invalid relative record path');
  }
  const full = path.resolve(root, relative);
  if (!full.startsWith(path.resolve(root) + path.sep)) throw Error('Path escapes root');
  return full;
}
function main(argv) {
  let repo = null, outputRoot = null;
  const requested = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--repo') repo = argv[++i];
    else if (a === '--output-root') outputRoot = argv[++i];
    else if (a === '--only') requested.push(argv[++i]);
    else if (a === '--help') {
      process.stdout.write('node restore_legacy_preparation_descriptions_retention67.mjs --repo REPOSITORY --output-root DESTINATION [--only FULL_REPOSITORY_RELATIVE_PATH]\n');
      return;
    } else throw Error('Unknown argument: ' + a);
  }
  if (!repo || !outputRoot || requested.some(x => !x)) {
    throw Error('Explicit --repo and --output-root are required');
  }
  repo = path.resolve(repo); outputRoot = path.resolve(outputRoot);
  const members = [], names = new Set();
  for (const v of VOLUMES) {
    const bytes = fs.readFileSync(safePath(repo, v.path));
    recordCheck(bytes, v, v.path);
    const table = JSON.parse(bytes.toString('utf8'));
    if (table.schema !== SCHEMA || table.retention_batch !== 67 ||
        table.all_original_and_canonical_bodies_are_ascii !== true ||
        !Array.isArray(table.members)) throw Error('Wrong complete delta table');
    for (const m of table.members) {
      if (names.has(m.record.path)) throw Error('Duplicate historical member');
      names.add(m.record.path); members.push(m);
    }
  }
  for (const p of requested) if (!names.has(p)) throw Error('Unknown requested member: ' + p);
  const selected = requested.length ? members.filter(m => requested.includes(m.record.path)) : members;
  const canonical = new Map(), restored = [];
  for (const m of selected) {
    let base = canonical.get(m.canonical.path);
    if (!base) {
      base = fs.readFileSync(safePath(repo, m.canonical.path));
      recordCheck(base, m.canonical, m.canonical.path);
      if (!base.every(x => x < 128)) throw Error('The recorded ASCII canonical changed');
      canonical.set(m.canonical.path, base);
    } else recordCheck(base, m.canonical, m.canonical.path);
    if (!Array.isArray(m.edits)) throw Error('Missing complete splice list');
    let end = 0;
    for (const e of m.edits) {
      if (!Array.isArray(e) || e.length !== 3 ||
          !Number.isSafeInteger(e[0]) || !Number.isSafeInteger(e[1]) ||
          e[0] < end || e[1] < 0 || e[0] + e[1] > base.length ||
          typeof e[2] !== 'string' || /[^\x00-\x7f]/.test(e[2])) {
        throw Error('Invalid or overlapping exact byte splice');
      }
      end = e[0] + e[1];
    }
    let bytes = Buffer.from(base);
    for (let i = m.edits.length - 1; i >= 0; i--) {
      const [offset, remove, insert] = m.edits[i];
      bytes = Buffer.concat([bytes.subarray(0, offset),
        Buffer.from(insert, 'ascii'), bytes.subarray(offset + remove)]);
    }
    recordCheck(bytes, m.record, m.record.path);
    const destination = safePath(outputRoot, m.record.path);
    fs.mkdirSync(path.dirname(destination), {recursive: true});
    if (fs.existsSync(destination)) {
      const existing = fs.readFileSync(destination);
      if (!existing.equals(bytes)) throw Error('Refusing to overwrite different existing bytes: ' + destination);
    } else fs.writeFileSync(destination, bytes, {flag: 'wx'});
    restored.push({path: m.record.path, bytes: bytes.length, sha256: digest(bytes),
      git_blob_sha: gitBlob(bytes), output_path: destination});
  }
  process.stdout.write(JSON.stringify({
    schema: 'complete-legacy-generated-adapter-byte-restoration-v1',
    restored_count: restored.length, restored,
    numerical_producer_called: false,
    numerical_state_or_certificate_recomputed: false,
    parameter_and_source_strings_preserved_verbatim: true
  }) + '\n');
}
main(process.argv.slice(2));
