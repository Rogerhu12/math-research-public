#!/usr/bin/env node
/** Restore the complete, original compact ready JSONs of two closed research runs. */
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { mkdirSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const directory = dirname(fileURLToPath(import.meta.url));
const topicRoot = dirname(directory);
const manifest = JSON.parse(readFileSync(join(directory, 'ret100h-closed-branch-parameter-recovery.json')));
const repo = execFileSync('git', ['-C', topicRoot, 'rev-parse', '--show-toplevel'], { encoding: 'utf8' }).trim();
if (process.argv.length !== 3) throw Error('Usage: node reproduce_ret100h_closed_branch_parameters.mjs OUTPUT_DIRECTORY');
const output = resolve(process.argv[2]);

function verify(bytes, row) {
    const [path, size, sha256, gitBlob] = row;
    const digest = createHash('sha256').update(bytes).digest('hex');
    const blob = createHash('sha1').update('blob ' + bytes.length + '\0').update(bytes).digest('hex');
    if (bytes.length !== size || digest !== sha256 || blob !== gitBlob) {
        throw Error('Wrong complete original file identity: ' + path);
    }
}

function reconstruct(source, edit) {
    if (edit === null) return source;
    const [kind, value] = edit;
    if (kind === 'set') return value;
    if (kind === 'array') {
        const result = [];
        for (const [action, original, countOrEdit] of value) {
            if (action === 'copy') result.push(...source.slice(original, original + countOrEdit));
            else if (action === 'change') result.push(reconstruct(source[original], countOrEdit));
            else if (action === 'value') result.push(original);
            else throw Error('Unknown array operation ' + action);
        }
        return result;
    }
    if (kind !== 'object') throw Error('Unknown object operation ' + kind);
    const [, members, dropped, order] = edit;
    let result = Object.assign(Object.create(null), source);
    for (const key of dropped) delete result[key];
    for (const [key, operation] of Object.entries(members)) {
        if (operation[0] === 'field') {
            result[key] = reconstruct(source[operation[1]], operation[2]);
        } else {
            result[key] = reconstruct(source[key], operation);
        }
    }
    if (order) result = Object.fromEntries(order.map(key => [key, result[key]]));
    return result;
}

const available = new Map();
for (const row of manifest.independent_source_files) {
    const path = row[0];
    const bytes = execFileSync('git', ['-C', repo, 'show', manifest.before_commit + ':' + manifest.topic + '/' + path],
        { maxBuffer: 256000 });
    verify(bytes, row);
    available.set(path, JSON.parse(bytes));
}
const expected = new Map(manifest.restored_branch_files.map(row => [row[0], row]));
let count = 0;
for (const group of manifest.complete_edit_groups) {
    const bytes = readFileSync(join(topicRoot, group[0]));
    verify(bytes, group);
    for (const [name, parentName, edit] of JSON.parse(bytes).rows) {
        const path = 'computations/' + name;
        const parent = 'computations/' + parentName;
        if (!available.has(parent) || !expected.has(path)) throw Error('Unresolved branch lineage: ' + path);
        const value = reconstruct(available.get(parent), edit);
        const whole = Buffer.from(JSON.stringify(value) + '\n', 'utf8');
        verify(whole, expected.get(path));
        const to = join(output, path);
        mkdirSync(dirname(to), { recursive: true });
        if (existsSync(to)) verify(readFileSync(to), expected.get(path));
        else writeFileSync(to, whole, { flag: 'wx' });
        available.set(path, value);
        expected.delete(path);
        ++count;
        process.stdout.write(JSON.stringify({ path, bytes: whole.length }) + '\n');
    }
}
if (expected.size !== 0) throw Error('Incomplete output registry');
process.stdout.write('Restored ' + count + ' complete original scientific parameter publications.\n');
