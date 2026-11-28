#!/usr/bin/env node
/** Rebuild all seventeen new whole source files from the unchanged scientific run33 parent. */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const cfgPath = "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-native-horner-complete-source-edits.json";
const cfgRow = {bytes:43276, sha256:"9634c68c89ed55d77410dd28e17d472b733a012f71dcf5d436db725c7a0ebb0f", git_blob_sha:"a9a66f55682e6b0301331047543c1fc82c4935fe"};
function digest(algo,data) { return crypto.createHash(algo).update(data).digest("hex"); }
function identity(raw,row,file) {
    const bytes=Buffer.isBuffer(raw)?raw:Buffer.from(raw,"utf8");
    if (bytes.length!==row.bytes || digest("sha256",bytes)!==row.sha256 ||
            digest("sha1",Buffer.concat([Buffer.from("blob "+bytes.length+"\0"),bytes]))!==row.git_blob_sha)
        throw Error("Whole-file identity differs: "+file);
    const value=bytes.toString("utf8");
    if (!Buffer.from(value,"utf8").equals(bytes)) throw Error("Invalid original UTF-8: "+file);
    return value;
}
function inside(root,file) {
    if (!file.startsWith("topics/visible-flex-larger-amplitude/") || file.includes("\\") ||
            file.split("/").some(v=>!v||v===".."||v===".")) throw Error("Invalid source path: "+file);
    return path.join(root,file);
}
function writeWhole(root,row,text) {
    const file=inside(root,row.path);
    identity(text,row,file);
    fs.mkdirSync(path.dirname(file),{recursive:true});
    if (fs.existsSync(file)) { identity(fs.readFileSync(file),row,file); return "existing-identical"; }
    const tmp=file+".new-"+process.pid;
    fs.writeFileSync(tmp,text,{encoding:"utf8",flag:"wx"});
    fs.renameSync(tmp,file);
    identity(fs.readFileSync(file),row,file);
    return "complete-source-written";
}
function materialize(data, parents) {
    const built = new Map();
    const operators = Object.fromEntries(data.literal_method_and_registry_edits.endpoint.map(change => {
        const match = change.to.match(/^    def (\w+)\(/);
        if (!match) throw Error("Incomplete full physical method replacement");
        return [match[1], change.to];
    }));
    for (const entry of data.entries) {
        const {role,parent,current} = entry;
        let source = parents.get(role);
        for (const patch of data.literal_method_and_registry_edits[role] || []) {
            const parts = source.split(patch.from);
            if (!patch.from || parts.length !== 2) throw Error("Nonunique full-source edit in " + role);
            source = parts[0] + patch.to + parts[1];
        }
        const policy = data.method_source_guard_updates[role];
        if (policy) {
            const lines = source.split("\n");
            const indexes = lines.flatMap((line,index) => line.startsWith(policy.assignment) ? [index] : []);
            if (indexes.length !== 1) throw Error("Missing original method guard declaration in " + role);
            const index = indexes[0], literal = lines[index].slice(policy.assignment.length);
            const nested = policy.format === "json_string";
            const table = nested ? JSON.parse(JSON.parse(literal.slice(0,-1))) : JSON.parse(literal);
            for (const method of policy.methods) table[method] = operators[method];
            const text = JSON.stringify(table);
            lines[index] = policy.assignment + (nested ? JSON.stringify(text) + ")" : text);
            source = lines.join("\n");
        }
        for (const other of data.entries) {
            source = source.replaceAll(other.parent.name,other.current.name);
            if (other.role !== role && source.includes(other.parent.sha256)) {
                if (!built.has(other.role)) throw Error("Incomplete earlier source binding in " + role);
                source = source.replaceAll(other.parent.sha256,other.current.sha256);
            }
        }
        built.set(role,source);
    }
    return built;
}
const args={};
for(let i=2;i<process.argv.length;i+=2) {
    const key=process.argv[i],value=process.argv[i+1];
    if (!["--source-repository","--output-repository","--record"].includes(key) ||
            !value||Object.hasOwn(args,key)) throw Error("Use source/output repository roots and a fresh record");
    args[key]=value;
}
if(Object.keys(args).length!==3)throw Error("Provide all three build arguments");
const root=fs.realpathSync(args["--source-repository"]);
const out=fs.realpathSync(args["--output-repository"]),record=path.resolve(args["--record"]);
if(record===out || record.startsWith(out+path.sep) || fs.existsSync(record))throw Error("Fresh runner-local build receipt required");
const configFile=inside(root,cfgPath);
const data=JSON.parse(identity(fs.readFileSync(configFile),cfgRow,configFile));
const parents = new Map();
for (const {role,parent} of data.entries) {
    const input=inside(root,parent.path);
    parents.set(role,identity(fs.readFileSync(input),parent,input));
}
const built=materialize(data,parents),native=[];
for(const file of data.native_sources) {
    const src=inside(root,file.path);
    const raw=identity(fs.readFileSync(src),file,src);
    native.push({...file,write_status:writeWhole(out,file,raw)});
}
const generated=data.entries.map(({role,parent,current}) => ({
    role,input:parent,output:current,status:writeWhole(out,current,built.get(role))
}));
const self=fs.readFileSync(new URL(import.meta.url));
const result={schema:"actual-complete-R729-native-horner-source-materialization-v1",complete:true,
 direction:"forward",generated,complete_source_file_count:generated.length,native_sources:native,
 source_repository:root,output_repository:out,node_version:process.version,
 recipe_source_bytes:self.length,recipe_source_sha256:digest("sha256",self),configuration:cfgRow,
 complete_source_output_bytes:generated.reduce((s,r)=>s+r.output.bytes,0),actual_argv:process.argv,
 Python_AST_compile_fixture_or_scientific_evaluation:false};
fs.mkdirSync(path.dirname(record),{recursive:true});fs.writeFileSync(record,JSON.stringify(result,null,2)+"\n",{flag:"wx"});
process.stdout.write(JSON.stringify({complete:true,complete_source_file_count:generated.length,record})+"\n");
