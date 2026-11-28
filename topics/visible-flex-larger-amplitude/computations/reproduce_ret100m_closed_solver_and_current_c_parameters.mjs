#!/usr/bin/env node
/** Rebuild the complete historical complete public solver and current-C parameters from the retained request sources. */
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const topic = dirname(here);
const registry = JSON.parse(readFileSync(join(here, 'ret100m-closed-solver-and-current-c-whole-parameter-recovery.json')));
const root = execFileSync('git', ['-C',topic,'rev-parse','--show-toplevel'], {encoding:'utf8'}).trim();
if (process.argv.length !== 3) throw Error('Supply an output directory for the complete restored JSON files');
const out = resolve(process.argv[2]);

function verify(bytes, row) {
    const digest = createHash('sha256').update(bytes).digest('hex');
    const git = createHash('sha1').update('blob ' + bytes.length + '\0').update(bytes).digest('hex');
    if (bytes.length !== row[1] || digest !== row[2] || git !== row[3]) {
        throw Error('Whole-file identity differs for ' + row[0]);
    }
}

const docs = [];
const order = registry.source_and_restored_document_order;
const present = new Map();
function enter(name, value) {
    if (name !== order[docs.length] || present.has(name)) throw Error('Unexpected document order ' + name);
    present.set(name, docs.length);
    docs.push(value);
}

function restore(source, edit) {
    if (edit === null) return source;
    const [kind, value, pathOrDrops, order] = edit;
    if (kind === 'set') return value;
    if (kind === 'take') {
        if (value < 0 || value >= docs.length) throw Error('Forward document reference');
        let current = docs[value];
        for (const member of pathOrDrops) {
            if (current == null || !Object.hasOwn(current,member)) throw Error('Missing complete referenced member');
            current = current[member];
        }
        return current;
    }
    if (kind === 'array') {
        const old = Array.isArray(source) ? source : [];
        const result = [];
        for (const [action, key, delta, offset, count] of value) {
            if (action === 'copy') result.push(...old.slice(key,key+delta));
            else if (action === 'span') {
                if (key < 0 || key >= docs.length) throw Error('Unknown prior semantic array document');
                let array = docs[key];
                for (const member of delta) {
                    if (array == null || !Object.hasOwn(array,member)) throw Error('Missing semantic array');
                    array = array[member];
                }
                if (!Array.isArray(array) || offset<0 || count<1 || offset+count>array.length) {
                    throw Error('Invalid complete semantic array element selection');
                }
                result.push(...array.slice(offset,offset+count));
            }
            else if (action === 'change') result.push(restore(old[key],delta));
            else if (action === 'new') result.push(restore(undefined,key));
            else if (action === 'value') result.push(key);
            else throw Error('Unsupported array operation ' + action);
        }
        return result;
    }
    if (kind !== 'object') throw Error('Unsupported structural operation ' + kind);
    const old = source !== null && typeof source === 'object' && !Array.isArray(source) ? source : {};
    const result = Object.assign(Object.create(null), old);
    for (const key of pathOrDrops) delete result[key];
    for (const [key, delta] of Object.entries(value)) {
        if (delta?.[0] === 'member') result[key] = restore(old[delta[1]],delta[2]);
        else result[key] = restore(old[key],delta);
    }
    if (order) return Object.fromEntries(order.map(key => [key,result[key]]));
    return result;
}

function originalRequestText(data, indent, name) {
    const compactPaths = registry.original_compact_members[name];
    const compact = new Set((compactPaths || []).map(path=>JSON.stringify(path)));
    function emit(node, path, prefix) {
        if (node === null || typeof node !== 'object' || !Object.keys(node).length ||
                compact.has(JSON.stringify(path))) return JSON.stringify(node);
        const array = Array.isArray(node);
        const childPrefix = prefix + ' '.repeat(indent);
        const lines = Object.entries(node).map(([key,value]) => childPrefix +
            (array ? '' : JSON.stringify(key)+': ') +
            emit(value,[...path,array ? Number(key) : key],childPrefix));
        return (array?'[':'{') + '\n' + lines.join(',\n') + '\n' + prefix + (array?']':'}');
    }
    const text = (compact.size ? emit(data,[],'') : JSON.stringify(data,null,indent)) + '\n';
    const operations = registry.original_number_spellings[name];
    if (!operations) return text;
    let token = 0, index = 0;
    const restored = text.replace(/"(?:\\.|[^"\\])*"|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?/g, word => {
        const current = token++;
        if (index >= operations.length || operations[index][0] !== current) return word;
        const [, canonical, original] = operations[index++];
        if (word !== canonical || +original !== +canonical) throw Error('Incorrect original number spelling in ' + name);
        return original;
    });
    if (index !== operations.length) throw Error('Missing original number spelling in ' + name);
    return restored;
}

for (const row of registry.independent_source_files) {
    const bytes = execFileSync('git',['-C',root,'show',registry.before_commit + ':' + registry.topic + '/' + row[0]],
                               {maxBuffer:100000});
    verify(bytes,row);
    enter(row[0],JSON.parse(bytes));
}
const expected = new Map(registry.restored_branch_files.map(row => [row[0],row]));
for (const group of registry.complete_edit_groups) {
    const bytes = readFileSync(join(topic,group[0]));
    verify(bytes,group);
    for (const [name,parent,edit] of JSON.parse(bytes).rows) {
        if (!present.has(parent)) throw Error('No reconstructed parent ' + parent);
        const data = restore(docs[present.get(parent)],edit);
        const path = name;
        const row = expected.get(path);
        if (!row) throw Error('Unexpected target ' + path);
        const indent = registry.original_json_indent[name] || undefined;
        const whole = Buffer.from(originalRequestText(data,indent,name),'utf8');
        verify(whole,row);
        enter(name,data);
        const target = join(out,path);
        mkdirSync(dirname(target),{recursive:true});
        if (existsSync(target)) verify(readFileSync(target),row);
        else writeFileSync(target,whole,{flag:'wx'});
        expected.delete(path);
        process.stdout.write(JSON.stringify({path,bytes:whole.length})+'\n');
    }
}
if (expected.size || docs.length !== order.length) throw Error('Incomplete whole-document registry');
