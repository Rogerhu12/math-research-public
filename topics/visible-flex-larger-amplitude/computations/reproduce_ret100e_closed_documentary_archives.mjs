#!/usr/bin/env node
// Regenerate 18 entire old terminal documentary archives in a scratch directory.
// All original numerical programs and queues remain separate. Node 18+.
import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const topic = "topics/visible-flex-larger-amplitude";
const ledger = JSON.parse(readFileSync(join(here, "ret100e-closed-documentary-reproduction.json"), "utf8"));
if (!process.argv[2]) throw new Error("Pass a scratch output directory");
const outdir = resolve(process.argv[2]);
const sha = (name, bytes) => createHash(name).update(bytes).digest("hex");

function check(bytes, expected) {
  const tuple = [bytes.length, sha("sha256", bytes),
    sha("sha1", Buffer.concat([Buffer.from("blob "+bytes.length+"\0"), bytes]))];
  if (JSON.stringify(tuple) !== JSON.stringify(expected)) throw new Error("Whole identity differs: "+expected[1]);
  return bytes;
}

function compact(text) {
  let answer = "", quoted = false, escaped = false;
  for (const c of text) {
    if (quoted) {
      answer += c;
      if (escaped) escaped = false;
      else if (c === "\\") escaped = true;
      else if (c === '"') quoted = false;
    } else if (c === '"') {
      answer += c;
      quoted = true;
    } else if (!" \r\n\t".includes(c)) answer += c;
  }
  return answer;
}

const sources = new Map();
function original(i) {
  if (sources.has(i)) return sources.get(i);
  const [kind, path, commit, ...expected] = ledger.sources[i];
  const git = args => execFileSync("git", ["-C", here, ...args], { maxBuffer: 1024*1024 });
  try {
    git(["cat-file", "-e", commit+"^{commit}"]);
  } catch {
    git(["fetch", "--no-tags", "--depth=1", "--filter=blob:none", "origin", commit]);
  }
  const bytes = check(git(["show", commit+":"+topic+"/"+path]), expected);
  sources.set(i, bytes);
  return bytes;
}

const envelopes = new Map();
for (const row of ledger.rows) {
  if (!envelopes.has(row.run)) {
    const [path, ...expected] = ledger.groups[row.run];
    envelopes.set(row.run, check(readFileSync(join(here, "..", path)), expected));
  }
  const [offset, size, digest] = row.envelope_span;
  const bytes = envelopes.get(row.run).subarray(offset, offset+size);
  if (bytes.length !== size || sha("sha256", bytes) !== digest) throw new Error("Archive envelope differs");
  let text = bytes.toString("utf8");
  for (const [j, spec] of row.records.entries()) {
    const [address, sourceIndex, sourceAddress, begin, count, mode] = spec;
    const raw = original(sourceIndex).subarray(begin, begin+count);
    if (raw.length !== count) throw new Error("Source range differs at "+sourceAddress);
    const value = raw.toString("utf8");
    let insertion;
    if (mode === "raw") insertion = value;
    else if (mode === "compact") insertion = compact(value);
    else if (mode === "published-ECMAScript-transcription") insertion = JSON.stringify(JSON.parse(value));
    else throw new Error("Unknown recorded formatting");
    const needle = '{"$ret100e_record":'+j+'}';
    const p = text.indexOf(needle);
    if (p < 0 || text.lastIndexOf(needle) !== p) throw new Error("Missing documentary placeholder at "+address);
    text = text.slice(0, p)+insertion+text.slice(p+needle.length);
  }
  const complete = check(Buffer.from(text), row.original);
  const dest = join(outdir, row.path);
  mkdirSync(dirname(dest), {recursive:true});
  writeFileSync(dest, complete, {flag:"wx"});
}
