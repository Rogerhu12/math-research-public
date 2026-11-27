#!/usr/bin/env node
// Optional whole-source reproduction only. This is not a scientific admission step.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const PLAN = {
  "schema": "complete-fixed-fejer-closed-source-text-derivation-v1",
  "parent": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_closed_phase_grip_evidence.py",
    "bytes": 70086,
    "sha256": "f7a10d7d6050cd57b5aea72d374c33662bf0c88e4175b6f7b738d6331d0976be"
  },
  "output": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_closed_phase_grip_evidence.py",
    "name": "fixed_fejer_complete_closed_phase_grip_evidence.py",
    "bytes": 71420,
    "sha256": "d606055d1b247d8354ac320bc28a0f40f4b00cbf1ff530a9b6bb2e80dec80bb9",
    "git_blob_sha": "33d9ee5b22c3e8bb5a92262ca7af7b89f20bb78b"
  },
  "proof": {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-fixed-fejer-closed-phase-grip-source-adapter.md",
    "name": "2026-11-27-fixed-fejer-closed-phase-grip-source-adapter.md",
    "bytes": 15093,
    "sha256": "16c15c597359b3017c9e050b5ddef94950d508e88a9c05fa726300cd129b726e",
    "git_blob_sha": "234e60bc7bbf7f286c77ed4e6f78cdf1d935c79c"
  },
  "complete_current_accurate_sources": [
    {
      "role": "input",
      "name": "fixed_fejer_normal_packet_accurate_field_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_normal_packet_accurate_field_input.py",
      "bytes": 32991,
      "sha256": "1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f",
      "git_blob_sha": "46ee6fd8157265253259a642844783ea4cd712bb"
    },
    {
      "role": "radial",
      "name": "fixed_fejer_accurate_reference_control_radial_boxes.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_accurate_reference_control_radial_boxes.py",
      "bytes": 45317,
      "sha256": "c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4",
      "git_blob_sha": "e572b4f4de1ebc3468d173989105f813675cab1b"
    },
    {
      "role": "normal",
      "name": "fixed_fejer_complete_normal_root_and_sixjet_fees.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_normal_root_and_sixjet_fees.py",
      "bytes": 40294,
      "sha256": "1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35",
      "git_blob_sha": "2aa3dc44a8ba8d61ec6ffa4de90c3dd61b2d85c2"
    },
    {
      "role": "leaf",
      "name": "fixed_fejer_complete_physical_leaf_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_physical_leaf_binding.py",
      "bytes": 47321,
      "sha256": "ee03b17d9c716ef24d76552cec1fc6031b7fa1eb037cf7cb55ddc9980b28721c",
      "git_blob_sha": "fbe38e6afce500e502ca9655dd784360f200f208"
    },
    {
      "role": "geometry",
      "name": "fixed_fejer_continuous_gram_curvature_support.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_continuous_gram_curvature_support.py",
      "bytes": 46689,
      "sha256": "fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b",
      "git_blob_sha": "368afa8be43c26eecdd13ef5466fe9de56b5afec"
    },
    {
      "role": "bridge",
      "name": "fixed_fejer_complete_geometry_support_beta_bridge.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_support_beta_bridge.py",
      "bytes": 20810,
      "sha256": "ff77dd925949bffaed4bffce8249554cfb0d56390da70bc3398cebe1f2202d15",
      "git_blob_sha": "3c6b9b259bb20231ca607192510f235315fb1f5e"
    }
  ],
  "changes": [
    {
      "label": "complete new field namespace",
      "old": "actual run10 whole leaves",
      "new": "actual fixed-Fejer whole leaves",
      "count": 1,
      "positions": [
        80
      ],
      "before_sha256": "f7a10d7d6050cd57b5aea72d374c33662bf0c88e4175b6f7b738d6331d0976be",
      "after_sha256": "c7d4b8fcc9d8a6dcad6553a940a6d4e4055044aa7dc8c664866a5f177e5f7e73"
    },
    {
      "label": "report schema",
      "old": "\"actual-run10-complete-closed-phase-grip-evidence-v1\"",
      "new": "\"actual-fixed-fejer-complete-closed-phase-grip-evidence-v1\"",
      "count": 1,
      "positions": [
        1305
      ],
      "before_sha256": "c7d4b8fcc9d8a6dcad6553a940a6d4e4055044aa7dc8c664866a5f177e5f7e73",
      "after_sha256": "373823dd1870646338cfc822d2fb9f42435d55c147685dbe2357f32ef121ef0f"
    },
    {
      "label": "bridge complete identity",
      "old": "BRIDGE = (\"run10_complete_geometry_support_beta_bridge.py\",\n    \"96d3467b15130c08948f52f701a80aeaf7a86337ebf3b9f1535b301e5677b8c9\")",
      "new": "BRIDGE = (\"fixed_fejer_complete_geometry_support_beta_bridge.py\",\n    \"ff77dd925949bffaed4bffce8249554cfb0d56390da70bc3398cebe1f2202d15\")",
      "count": 1,
      "positions": [
        1412
      ],
      "before_sha256": "373823dd1870646338cfc822d2fb9f42435d55c147685dbe2357f32ef121ef0f",
      "after_sha256": "ef0d5318c11dc09991780b974d935ef4084fdf97823b33b09d97806c8203d307"
    },
    {
      "label": "geometry complete identity",
      "old": "GEOMETRY = (\"run10_continuous_gram_curvature_support.py\",\n    \"e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7\")",
      "new": "GEOMETRY = (\"fixed_fejer_continuous_gram_curvature_support.py\",\n    \"fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b\")",
      "count": 1,
      "positions": [
        1550
      ],
      "before_sha256": "ef0d5318c11dc09991780b974d935ef4084fdf97823b33b09d97806c8203d307",
      "after_sha256": "a42b3bb07a91c41eec300bc32b5c2a69db28598f3bd1ca841c9d8e968bdd1f04"
    },
    {
      "label": "source adapter proof role",
      "old": "\"run10_current_source_adapter\"",
      "new": "\"fixed_fejer_current_source_adapter\"",
      "count": 3,
      "positions": [
        1825,
        33015,
        49411
      ],
      "before_sha256": "a42b3bb07a91c41eec300bc32b5c2a69db28598f3bd1ca841c9d8e968bdd1f04",
      "after_sha256": "66f5d863b74c4e0fd05a89182a93c1b3b5db783715d5e1b5a25ab766bdbd481a"
    },
    {
      "label": "source adapter proof filename",
      "old": "2026-11-27-run10-closed-phase-grip-source-adapter.md",
      "new": "2026-11-27-fixed-fejer-closed-phase-grip-source-adapter.md",
      "count": 1,
      "positions": [
        1887
      ],
      "before_sha256": "66f5d863b74c4e0fd05a89182a93c1b3b5db783715d5e1b5a25ab766bdbd481a",
      "after_sha256": "bece9553d4098b2223b034277840f167ad6eb4e996a01a419bb860f234489020"
    },
    {
      "label": "source adapter whole proof identity",
      "old": "b378593327e31a91385d4f5397c8fbb9294147febb843060941bfbaba92584e7",
      "new": "16c15c597359b3017c9e050b5ddef94950d508e88a9c05fa726300cd129b726e",
      "count": 2,
      "positions": [
        1957,
        43090
      ],
      "before_sha256": "bece9553d4098b2223b034277840f167ad6eb4e996a01a419bb860f234489020",
      "after_sha256": "b860205e10b72bcc5624c214ff07ad0944b6e675fd67c538306bb99173191a59"
    },
    {
      "label": "actual chart word record in point",
      "old": "base.get(\"fixed_chart_core_sha256\")!=r.ACTUAL_CHART",
      "new": "base.get(\"fixed_chart_core_sha256\")!=actual[\"fixed_chart_core_sha256\"]",
      "count": 1,
      "positions": [
        9362
      ],
      "before_sha256": "b860205e10b72bcc5624c214ff07ad0944b6e675fd67c538306bb99173191a59",
      "after_sha256": "f5a272935bdd17d555404dfdec97047a7689afba62268a3607f996f94cdf42d2"
    },
    {
      "label": "actual chart word record in field",
      "old": "fixed_material_chart_identity_sha256=r.ACTUAL_CHART",
      "new": "fixed_material_chart_identity_sha256=a[\"fixed_chart_core_sha256\"]",
      "count": 1,
      "positions": [
        42297
      ],
      "before_sha256": "f5a272935bdd17d555404dfdec97047a7689afba62268a3607f996f94cdf42d2",
      "after_sha256": "66ca6c1bafcd36ad7349c372b95b4b4b88670fac532dea6f5546206260168b8e"
    },
    {
      "label": "actual complete input source",
      "old": "run10_normal_packet_accurate_field_input.py",
      "new": "fixed_fejer_normal_packet_accurate_field_input.py",
      "count": 1,
      "positions": [
        41356
      ],
      "before_sha256": "66ca6c1bafcd36ad7349c372b95b4b4b88670fac532dea6f5546206260168b8e",
      "after_sha256": "8412c57b6d37c9086038ae72a8e0f97e57fe7aaf5704f480e60b674a1d3c286d"
    },
    {
      "label": "actual complete radial source",
      "old": "run10_accurate_reference_control_radial_boxes.py",
      "new": "fixed_fejer_accurate_reference_control_radial_boxes.py",
      "count": 1,
      "positions": [
        41417
      ],
      "before_sha256": "8412c57b6d37c9086038ae72a8e0f97e57fe7aaf5704f480e60b674a1d3c286d",
      "after_sha256": "657cf50ca80494d3fac69dca4d538cecf9af6c564de5c6983db378eb4ff635c4"
    },
    {
      "label": "field instance declaration",
      "old": "original_field_in_this_statement_is_the_actual_run10_field=True,",
      "new": "original_field_in_this_statement_is_the_actual_fixed_fejer_field=True,\n        mathematical_target_identity_sha256=a[\"mathematical_target_identity_sha256\"],\n        previous_target_field_or_certificate_inherited=False,\n        same_mathematical_g_as_run10_claimed=False,",
      "count": 1,
      "positions": [
        42899
      ],
      "before_sha256": "657cf50ca80494d3fac69dca4d538cecf9af6c564de5c6983db378eb4ff635c4",
      "after_sha256": "339db16d4002faf30f9b844e07048558df93f9e45ba951295533da7af670fd08"
    },
    {
      "label": "genuine geometry error scope",
      "old": "Use the exact whole actual run10 geometry producer",
      "new": "Use the exact whole actual fixed-Fejer geometry producer",
      "count": 1,
      "positions": [
        59080
      ],
      "before_sha256": "339db16d4002faf30f9b844e07048558df93f9e45ba951295533da7af670fd08",
      "after_sha256": "226b41497bb75f848942fe6eccd273e0e55621fa418e7cada6d555db1dc86ebc"
    },
    {
      "label": "complete original problem source materialization",
      "old": "        record=r.file_record(Path(repo).resolve()/name)\n",
      "new": "        source_path=Path(repo).resolve()/name\n        if role==\"original_problem\" and not source_path.exists():\n            # The controller checks out this topic sparsely. Materialize only\n            # this declared public proof from the same frozen source commit.\n            raw=subprocess.check_output([\"git\",\"show\",\"HEAD:\"+name],cwd=Path(repo).resolve())\n            if hashlib.sha256(raw).hexdigest()!=digest:\n                raise ValueError(\"The complete original problem source changed\")\n            source_path.parent.mkdir(parents=True,exist_ok=True)\n            with source_path.open(\"xb\") as handle:\n                handle.write(raw)\n        record=r.file_record(source_path)\n",
      "count": 1,
      "positions": [
        7154
      ],
      "before_sha256": "226b41497bb75f848942fe6eccd273e0e55621fa418e7cada6d555db1dc86ebc",
      "after_sha256": "c66e08178eec19c9f3ced5f5f4db0c87dd985d4e158ce503b3d6afb44d23c26e"
    },
    {
      "label": "source proof coverage",
      "old": "    \"source_specific_ports\": (\n",
      "new": "    \"R717_fixed_chart_design_only\": (\n        TOPIC+\"/results/R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md\",\n        \"9727ed8b7e48d9aa4a343c1d3dcd666a9fbc0d74f876df1ee80494df7b337378\"),\n    \"run10_algorithm_parent_adapter\": (\n        TOPIC+\"/notes/2026-11-27-run10-closed-phase-grip-source-adapter.md\",\n        \"b378593327e31a91385d4f5397c8fbb9294147febb843060941bfbaba92584e7\"),\n    \"source_specific_ports\": (\n",
      "count": 1,
      "positions": [
        2025
      ],
      "before_sha256": "c66e08178eec19c9f3ced5f5f4db0c87dd985d4e158ce503b3d6afb44d23c26e",
      "after_sha256": "d606055d1b247d8354ac320bc28a0f40f4b00cbf1ff530a9b6bb2e80dec80bb9"
    }
  ],
  "scientific_execution": false
};

const args=process.argv.slice(2), options={};
for(let i=0;i<args.length;i+=2){if(!["--repo","--outdir"].includes(args[i])||!args[i+1])throw Error("Use --repo REPOSITORY --outdir DIRECTORY");options[args[i]]=args[i+1];}
if(!options["--outdir"])throw Error("--outdir is required");
const root=path.resolve(options["--repo"]||"."), outdir=path.resolve(options["--outdir"]);
const hash=s=>crypto.createHash("sha256").update(s).digest("hex");
function read(record){const bytes=fs.readFileSync(path.join(root,record.path));if(bytes.length!==record.bytes||hash(bytes)!==record.sha256)throw Error("Complete source differs: "+record.path);return bytes.toString("utf8");}
const parent=read(PLAN.parent);read(PLAN.proof);for(const source of PLAN.complete_current_accurate_sources)read(source);
let body=parent;
for(const patch of PLAN.changes){
 if(hash(body)!==patch.before_sha256)throw Error("Full preimage differs: "+patch.label);
 const positions=[];for(let i=0;(i=body.indexOf(patch.old,i))>=0;i+=patch.old.length)positions.push(i);
 if(JSON.stringify(positions)!==JSON.stringify(patch.positions)||positions.length!==patch.count)throw Error("Complete patch positions differ: "+patch.label);
 body=body.split(patch.old).join(patch.new);
 if(hash(body)!==patch.after_sha256)throw Error("Full postimage differs: "+patch.label);
}
if(Buffer.byteLength(body)!==PLAN.output.bytes||hash(body)!==PLAN.output.sha256)throw Error("Complete output differs");
let inverse=body;
for(const patch of [...PLAN.changes].reverse()){
 let offset=0;const positions=patch.positions.map(i=>{const j=i+offset;offset+=patch.new.length-patch.old.length;return j;});
 for(const i of positions.reverse()){if(inverse.slice(i,i+patch.new.length)!==patch.new)throw Error("Inverse span differs");inverse=inverse.slice(0,i)+patch.old+inverse.slice(i+patch.new.length);}
 if(hash(inverse)!==patch.before_sha256)throw Error("Complete inverse differs");
}
if(inverse!==parent)throw Error("Original whole parent not recovered");
fs.mkdirSync(outdir,{recursive:true});
fs.writeFileSync(path.join(outdir,PLAN.output.name),body,{flag:"wx"});
process.stdout.write(JSON.stringify({source:PLAN.output,all_source_text_complete:true,scientific_execution:false})+"\n");
