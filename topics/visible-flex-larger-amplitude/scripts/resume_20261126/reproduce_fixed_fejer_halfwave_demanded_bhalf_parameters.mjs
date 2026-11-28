#!/usr/bin/env node
/**
 * Complete run28 parameter-text derivation from the actual whole run25 parent.
 * No scientific import, source execution, AST inspection or numerical test.
 * Every parent is a whole immutable file; no source/parameter/body is shortened.
 * Exactly the declared namespace/script/scope metadata changes. The full
 * inverse in build() restores both complete original step objects.
 */
import {readFileSync,writeFileSync,mkdirSync} from "node:fs";
import {resolve} from "node:path";
import {createHash} from "node:crypto";
const DATA={
  "date": "2026-11-28",
  "session": "Astra-larger-e4e2a2bf-20261126",
  "repository": "Rogerhu12/math-research-public",
  "topic": "topics/visible-flex-larger-amplitude",
  "intended_runner_label": "28",
  "old_namespace": "fixed-fejer-paired-halfwave-dk-cache-bhalf-first",
  "namespace": "fixed-fejer-paired-halfwave-demanded-bhalf-first",
  "names": {
    "binding": "fixed-fejer-halfwave-demanded-bhalf-complete-parameter-binding.json",
    "science": "fixed-fejer-halfwave-demanded-bhalf-science-complete-ready.json",
    "pure": "fixed-fejer-halfwave-demanded-bhalf-pure-complete-ready.json",
    "reproducer": "reproduce_fixed_fejer_halfwave_demanded_bhalf_parameters.mjs",
    "manifest": "fixed-fejer-halfwave-demanded-bhalf-complete-parameter-delivery.json"
  },
  "parent_records": {
    "science": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-dk-cache-bhalf-science-complete-ready.json",
      "bytes": 72494,
      "sha256": "3b26dda806f4a70a28c31721c2b27e9a228e53579864b32754701d68fb7eedcd",
      "sha": "d125adb6de02b975d29d428886a9230e01731d59",
      "git_blob_sha": "d125adb6de02b975d29d428886a9230e01731d59",
      "fixed_publication_commit": "037dd5055bf7df6fd2cd6307c1a05a708b3b6e2a",
      "name": "fixed-fejer-paired-halfwave-dk-cache-bhalf-science-complete-ready.json"
    },
    "pure": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-dk-cache-bhalf-pure-complete-ready.json",
      "bytes": 58591,
      "sha256": "8a52cf078f41e5d9b6081fbd41ca601b207646cabb6e34b53b4865a59d6e1e62",
      "sha": "f4a8af980ed367180148407da7e878ec337a38bd",
      "git_blob_sha": "f4a8af980ed367180148407da7e878ec337a38bd",
      "fixed_publication_commit": "037dd5055bf7df6fd2cd6307c1a05a708b3b6e2a",
      "name": "fixed-fejer-paired-halfwave-dk-cache-bhalf-pure-complete-ready.json"
    },
    "binding": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-dk-cache-bhalf-complete-parameter-binding.json",
      "bytes": 36381,
      "sha256": "25a945db36d4073b3706da8d0fea90b9fbc3661126834fdaf2bdd694007a2a49",
      "sha": "608dd30ced3c17417d61de2af37c644689a3ac24",
      "git_blob_sha": "608dd30ced3c17417d61de2af37c644689a3ac24",
      "fixed_publication_commit": "037dd5055bf7df6fd2cd6307c1a05a708b3b6e2a",
      "name": "fixed-fejer-paired-halfwave-dk-cache-bhalf-complete-parameter-binding.json"
    },
    "delivery": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-dk-cache-bhalf-complete-parameter-delivery.json",
      "bytes": 13918,
      "sha256": "9aa9b2c5b0f28aa5d7ece59374dd1eadd5c551a21b96104cd697ef37a8f2ee27",
      "sha": "cf18d6e464448e2a555cd0f7063fba66c08d68a5",
      "git_blob_sha": "cf18d6e464448e2a555cd0f7063fba66c08d68a5",
      "fixed_publication_commit": "037dd5055bf7df6fd2cd6307c1a05a708b3b6e2a",
      "name": "fixed-fejer-paired-halfwave-dk-cache-bhalf-complete-parameter-delivery.json"
    },
    "source_binding": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-curvature-cache-current-runtime-binding.json",
      "bytes": 51709,
      "sha256": "d449d0a54b69b23c598234a28fede12917473ce7058e9d8815ba8b524c6f869f",
      "sha": "38f781117d79710e72947cb8f8f0ecb258f0dabb",
      "git_blob_sha": "38f781117d79710e72947cb8f8f0ecb258f0dabb",
      "fixed_publication_commit": "06c3cefad4f173dd53018d67175e70a228dfcf91",
      "name": "fixed-fejer-paired-halfwave-curvature-cache-current-runtime-binding.json"
    }
  },
  "current_source_binding": {
    "name": "fixed-fejer-halfwave-demanded-current-runtime-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-current-runtime-binding.json",
    "bytes": 65101,
    "sha256": "931425f12d5386c4880393337c9a34856e33044de6f5dd16f0a103aa3b164ebc",
    "git_blob_sha": "abde5bcfe45b29e1563233621e0c8feacdb9407f",
    "fixed_publication_commit": "3fa8f98f08649da12ee5b8b9ba5889276285bc84"
  },
  "current_source_delivery": {
    "name": "fixed-fejer-halfwave-demanded-complete-source-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-complete-source-delivery.json",
    "bytes": 56928,
    "sha256": "6c8880e6badc4f0e4ec02eafb224f6d45baaf3943354defa5c445f1e0063a4be",
    "git_blob_sha": "3989acf5902578635c3b7bcaa9c94b55f6a7dca0",
    "fixed_publication_commit": "3fa8f98f08649da12ee5b8b9ba5889276285bc84"
  },
  "complete_prior14_external_binding": {
    "name": "fixed-fejer-r725-bfiveeighths-complete-parameter-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bfiveeighths-complete-parameter-binding.json",
    "bytes": 37316,
    "sha256": "d66e3ed8a8c18908e5d28cecb556308e4bfa9da6ae5fd4687798be5cd45ddd99",
    "git_blob_sha": "959b7b0f7229adccd705163665b5b6220aa2a534",
    "role": "parameter-binding"
  },
  "official27": {
    "key": "official27",
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run27-complete-r725-five-eighths-launch-and-continuation.md",
    "bytes": 31932,
    "sha256": "0aba4962e2c3712d407678da4e64a8f7d38053664e7278bd55a4d68750336bb7",
    "git_blob_sha": "ed1a598ba18f06cd4f663265f52fef60510388ea",
    "fixed_publication_commit": "6b09abf79ef694c5a422b66d349d625eccd21ffa",
    "name": "2026-11-28-run27-complete-r725-five-eighths-launch-and-continuation.md"
  },
  "later_actual25": {
    "key": "latest25",
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run25-complete-halfwave-curvature-cache-launch-and-continuation.md",
    "bytes": 35724,
    "sha256": "c11ebbd3ed45192ea961e7b8a9fc560c8197dbc10cdb8abf9117533dc39b7962",
    "git_blob_sha": "159e09a0384bf0fde7d39f19a0f6fe28edd60416",
    "fixed_publication_commit": "cf7b894fc0a4ed559bbc8b848efa713873383f5a",
    "name": "2026-11-28-run25-complete-halfwave-curvature-cache-launch-and-continuation.md"
  },
  "later_actual26": {
    "key": "latest26",
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md",
    "bytes": 50868,
    "sha256": "aaf989f4c548a320ffdf858cd6a0c4fd7980512aada1c42893b7d57215b99c3b",
    "git_blob_sha": "ab60f4473d5de7d6c1b2027d4740ab3cf29e7966",
    "fixed_publication_commit": "612a979218991762127207b37df99d5fd8933428",
    "name": "2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md"
  },
  "official27_facts": {
    "run_id": "46105138690",
    "run_attempt": 1,
    "run_attempt_key": "46105138690/1",
    "workflow_id": "433391338",
    "job_id": "140856083740",
    "official_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46105138690",
    "official_started_at": "2026-11-28T03:55:38Z",
    "official_head_sha": "a773d67267750078be498284d1fcd3cabe4f3ab3",
    "official_status_at_indicated_record": "in_progress",
    "official_conclusion_at_indicated_record": null,
    "declared_driver_source_sha256": "e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd",
    "declared_driver_is_not_observed_child_source": true
  },
  "scientific_scope": "Complete paired-halfwave b/S=1/2, delta=1/32 independent science using the complete demanded original rotation expressions and same-branch order-one-to-two frame reuse with full original fallback. The physical S5-boundary R724 seed, fixed metric, all variables, 32 normal stages, all numerical words and budgets, original curvature cache, every formal selector and all 64 existing live scalars are retained from the complete run25 parameter parent. This is a distinct complete source/model-policy binding; no old field, point, roots, final, typed history, actual cache hit or speedup is inferred. R725 cutoff, R726 Slerp and the separate restoration-continuation policy are not used.",
  "pure_scope": "Complete current demanded-halfwave pure readout of the independently returned full report and genuine final bundle. All 445 original formal selectors and seven complete argument words are retained from the complete run25 parent. Actual current source/model/point and own-point diagnostics are re-read by the current complete reader; no prior field or metadata snapshot is backfilled."
};
const INPUTS={
  "parent_science": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-dk-cache-bhalf-science-complete-ready.json",
    "bytes": 72494,
    "sha256": "3b26dda806f4a70a28c31721c2b27e9a228e53579864b32754701d68fb7eedcd",
    "sha": "d125adb6de02b975d29d428886a9230e01731d59",
    "git_blob_sha": "d125adb6de02b975d29d428886a9230e01731d59",
    "fixed_publication_commit": "037dd5055bf7df6fd2cd6307c1a05a708b3b6e2a",
    "name": "fixed-fejer-paired-halfwave-dk-cache-bhalf-science-complete-ready.json"
  },
  "parent_pure": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-dk-cache-bhalf-pure-complete-ready.json",
    "bytes": 58591,
    "sha256": "8a52cf078f41e5d9b6081fbd41ca601b207646cabb6e34b53b4865a59d6e1e62",
    "sha": "f4a8af980ed367180148407da7e878ec337a38bd",
    "git_blob_sha": "f4a8af980ed367180148407da7e878ec337a38bd",
    "fixed_publication_commit": "037dd5055bf7df6fd2cd6307c1a05a708b3b6e2a",
    "name": "fixed-fejer-paired-halfwave-dk-cache-bhalf-pure-complete-ready.json"
  },
  "parent_binding": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-dk-cache-bhalf-complete-parameter-binding.json",
    "bytes": 36381,
    "sha256": "25a945db36d4073b3706da8d0fea90b9fbc3661126834fdaf2bdd694007a2a49",
    "sha": "608dd30ced3c17417d61de2af37c644689a3ac24",
    "git_blob_sha": "608dd30ced3c17417d61de2af37c644689a3ac24",
    "fixed_publication_commit": "037dd5055bf7df6fd2cd6307c1a05a708b3b6e2a",
    "name": "fixed-fejer-paired-halfwave-dk-cache-bhalf-complete-parameter-binding.json"
  },
  "parent_delivery": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-dk-cache-bhalf-complete-parameter-delivery.json",
    "bytes": 13918,
    "sha256": "9aa9b2c5b0f28aa5d7ece59374dd1eadd5c551a21b96104cd697ef37a8f2ee27",
    "sha": "cf18d6e464448e2a555cd0f7063fba66c08d68a5",
    "git_blob_sha": "cf18d6e464448e2a555cd0f7063fba66c08d68a5",
    "fixed_publication_commit": "037dd5055bf7df6fd2cd6307c1a05a708b3b6e2a",
    "name": "fixed-fejer-paired-halfwave-dk-cache-bhalf-complete-parameter-delivery.json"
  },
  "parent_source_binding": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-curvature-cache-current-runtime-binding.json",
    "bytes": 51709,
    "sha256": "d449d0a54b69b23c598234a28fede12917473ce7058e9d8815ba8b524c6f869f",
    "sha": "38f781117d79710e72947cb8f8f0ecb258f0dabb",
    "git_blob_sha": "38f781117d79710e72947cb8f8f0ecb258f0dabb",
    "fixed_publication_commit": "06c3cefad4f173dd53018d67175e70a228dfcf91",
    "name": "fixed-fejer-paired-halfwave-curvature-cache-current-runtime-binding.json"
  },
  "current_source_binding": {
    "name": "fixed-fejer-halfwave-demanded-current-runtime-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-current-runtime-binding.json",
    "bytes": 65101,
    "sha256": "931425f12d5386c4880393337c9a34856e33044de6f5dd16f0a103aa3b164ebc",
    "git_blob_sha": "abde5bcfe45b29e1563233621e0c8feacdb9407f",
    "fixed_publication_commit": "3fa8f98f08649da12ee5b8b9ba5889276285bc84"
  },
  "current_source_delivery": {
    "name": "fixed-fejer-halfwave-demanded-complete-source-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-complete-source-delivery.json",
    "bytes": 56928,
    "sha256": "6c8880e6badc4f0e4ec02eafb224f6d45baaf3943354defa5c445f1e0063a4be",
    "git_blob_sha": "3989acf5902578635c3b7bcaa9c94b55f6a7dca0",
    "fixed_publication_commit": "3fa8f98f08649da12ee5b8b9ba5889276285bc84"
  },
  "prior14_binding": {
    "name": "fixed-fejer-r725-bfiveeighths-complete-parameter-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bfiveeighths-complete-parameter-binding.json",
    "bytes": 37316,
    "sha256": "d66e3ed8a8c18908e5d28cecb556308e4bfa9da6ae5fd4687798be5cd45ddd99",
    "git_blob_sha": "959b7b0f7229adccd705163665b5b6220aa2a534",
    "role": "parameter-binding"
  },
  "official27": {
    "key": "official27",
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run27-complete-r725-five-eighths-launch-and-continuation.md",
    "bytes": 31932,
    "sha256": "0aba4962e2c3712d407678da4e64a8f7d38053664e7278bd55a4d68750336bb7",
    "git_blob_sha": "ed1a598ba18f06cd4f663265f52fef60510388ea",
    "fixed_publication_commit": "6b09abf79ef694c5a422b66d349d625eccd21ffa",
    "name": "2026-11-28-run27-complete-r725-five-eighths-launch-and-continuation.md"
  },
  "later_actual25": {
    "key": "latest25",
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run25-complete-halfwave-curvature-cache-launch-and-continuation.md",
    "bytes": 35724,
    "sha256": "c11ebbd3ed45192ea961e7b8a9fc560c8197dbc10cdb8abf9117533dc39b7962",
    "git_blob_sha": "159e09a0384bf0fde7d39f19a0f6fe28edd60416",
    "fixed_publication_commit": "cf7b894fc0a4ed559bbc8b848efa713873383f5a",
    "name": "2026-11-28-run25-complete-halfwave-curvature-cache-launch-and-continuation.md"
  },
  "later_actual26": {
    "key": "latest26",
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md",
    "bytes": 50868,
    "sha256": "aaf989f4c548a320ffdf858cd6a0c4fd7980512aada1c42893b7d57215b99c3b",
    "git_blob_sha": "ab60f4473d5de7d6c1b2027d4740ab3cf29e7966",
    "fixed_publication_commit": "612a979218991762127207b37df99d5fd8933428",
    "name": "2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md"
  }
};
const EXPECTED={
  "binding": {
    "name": "fixed-fejer-halfwave-demanded-bhalf-complete-parameter-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-bhalf-complete-parameter-binding.json",
    "bytes": 45365,
    "sha256": "27a9467deba43fb964f287ad2df0897260c14bf94ccf624aee62344f1643a0c5",
    "git_blob_sha": "b591d00267e144934bcf1ea7037f762d7f5ba449",
    "role": "parameter-binding"
  },
  "science": {
    "name": "fixed-fejer-halfwave-demanded-bhalf-science-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-bhalf-science-complete-ready.json",
    "bytes": 73514,
    "sha256": "2103f0942aa047757a0e7c04a8af10ae8ba205907f91a3621151f3b5885f984e",
    "git_blob_sha": "157b23f71517ebfa5794e9ff9a7ec98f46069e35",
    "role": "science-ready"
  },
  "pure": {
    "name": "fixed-fejer-halfwave-demanded-bhalf-pure-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-demanded-bhalf-pure-complete-ready.json",
    "bytes": 59324,
    "sha256": "8b16a2e79a358af068a68395dbef62130133e7b481ec1c2baf1fc34e21491eb6",
    "git_blob_sha": "cc6bacf16d723ab0df42efe4b93719f4ce03c0c5",
    "role": "pure-ready"
  }
};
const digest=(algorithm,data)=>createHash(algorithm).update(data).digest("hex");
const gitBlob=buf=>digest("sha1",Buffer.concat([Buffer.from("blob "+buf.length+"\0","utf8"),buf]));
function options(argv){
 const out={};
 for(let i=0;i<argv.length;i+=2){
  const k=argv[i],v=argv[i+1];
  if(!["--parent-directory","--generated-directory"].includes(k)||v===undefined||Object.hasOwn(out,k))throw Error("Use --parent-directory <whole-input-files> --generated-directory <fresh-output-directory>");
  out[k]=v;
 }
 if(Object.keys(out).length!==2)throw Error("Both complete input/output directory arguments are required.");
 return out;
}
function loadAll(directory){
 const out={};
 for(const [key,r]of Object.entries(INPUTS)){
  if(r.bytes>=100000)throw Error("Declared complete input exceeds this source artifact contract: "+key);
  const name=r.name||r.path.split("/").at(-1);
  const buf=readFileSync(resolve(directory,name));
  if(buf.length!==r.bytes||digest("sha256",buf)!==r.sha256||gitBlob(buf)!==r.git_blob_sha)throw Error("Complete input bytes/SHA/blob mismatch: "+name);
  const text=buf.toString("utf8");
  out[key]=name.endsWith(".json")?JSON.parse(text):text;
 }
 return out;
}
function record(name,role,text){
 const buf=Buffer.from(text,"utf8");
 if(buf.length>=100000)throw Error("Complete generated file must remain below 100000 bytes: "+name);
 return {name,path:DATA.topic+"/computations/"+name,bytes:buf.length,sha256:digest("sha256",buf),git_blob_sha:gitBlob(buf),role};
}
function build(data,inputs,makeRecord){

const clone=v=>JSON.parse(JSON.stringify(v));
const ref=(record,pointer="")=>({complete_file:clone(record),json_pointer:pointer,whole_parent_value_retained:true});
const map=(v,from,to)=>typeof v==="string"?v.split(from).join(to):Array.isArray(v)?v.map(x=>map(x,from,to)):v&&typeof v==="object"?Object.fromEntries(Object.entries(v).map(([k,x])=>[k.split(from).join(to),map(x,from,to)])):v;
const need=(ok,msg)=>{if(!ok)throw Error(msg);};
const old=inputs.parent_binding, parentScience=inputs.parent_science, parentPure=inputs.parent_pure;
const source=inputs.current_source_binding,sourceDelivery=inputs.current_source_delivery;
const oldSource=inputs.parent_source_binding;
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
need(old.namespace===data.old_namespace,"whole parent namespace");
need(parentScience.steps.length===1&&parentPure.steps.length===1,"complete parent steps");
const sourceKeys=Object.keys(source.complete_source_role_registry),oldKeys=Object.keys(oldSource.complete_source_role_registry);
need(sourceKeys.length===137&&oldKeys.length===137&&same(sourceKeys.slice().sort(),oldKeys.slice().sort()),"complete137 source roles");
const changed=sourceKeys.filter(k=>!same(source.complete_source_role_registry[k],oldSource.complete_source_role_registry[k]));
need(changed.length===14,"14 exact current role changes");
need(Object.keys(source.current_complete_runtime_sources).length===19,"19 complete runtime files");
need(source.new_complete_source_count===17,"17 new runtime bodies");
const science=map(parentScience.steps[0],data.old_namespace,data.namespace);
const pure=map(parentPure.steps[0],data.old_namespace,data.namespace);
science.script=source.current_complete_runtime_sources.launcher.path;
pure.script=source.current_complete_runtime_sources.reader.path;
science.scope=data.scientific_scope;pure.scope=data.pure_scope;
const counts=s=>({argv_words:s.args.length,formal_selectors:Object.values(s.summary??{}).reduce((a,v)=>a+Object.keys(v).length,0),live_selectors:Object.values(s.progress_summary??{}).reduce((a,v)=>a+Object.keys(v).length,0)});
need(same(counts(science),{argv_words:157,formal_selectors:458,live_selectors:64}),"all complete science counts");
need(same(counts(pure),{argv_words:7,formal_selectors:445,live_selectors:0}),"all complete pure counts");
for(const [step,parent]of[[science,parentScience.steps[0]],[pure,parentPure.steps[0]]]){
 const inverse=map(step,data.namespace,data.old_namespace);
 inverse.script=parent.script;inverse.scope=parent.scope;
 need(same(inverse,parent),"full entire step inverse");
}
const argValue=(args,key)=>{const k=args.indexOf(key);need(k>=0&&k+1<args.length,"original argument "+key);return args[k+1];};
for(const [key,value]of[["--seed-boundary-total-length","1/2"],["--seed-profile-delta","1/32"],["--damping",".01"],["--restoration-damping",".01"],["--normal-stages","32"]])need(argValue(science.args,key)===value,"unchanged numeric "+key);
const pending=args=>args.flatMap((v,k)=>v==="--pending-parallel-envelope-source"?[args[k+1]]:[]);
need(pending(science.args).length===5&&same(pending(science.args),pending(parentScience.steps[0].args)),"all five original CLI peer pairs");
const prior14=inputs.prior14_binding.complete_peer_responsibilities;
need(prior14.external_obligation_count===14&&prior14.complete_external_obligation_pairs.length===14,"complete prior14");
const old12=old.complete_peer_responsibilities.complete_external_obligation_pairs;
need(old12.length===12&&same(old12,prior14.complete_external_obligation_pairs.slice(0,12)),"original12 complete source pair order");
const peer27={...clone(data.official27_facts),
 complete_official_launch_and_source_note:clone(data.official27),
 actual_scientific_source_commit:null,actual_launcher_source_sha256:null,
 actual_current_input_file_records:null,actual_model_identity_sha256:null,
 actual_current_full_point_sha256:null,actual_complete_scientific_report_sha256:null,
 actual_final_checkpoint_sha256:null,actual_complete_thirteen_member_parent:null,
 actual_root_packet_sha256:null,actual_snapshot_identity_sha256:null,
 complete_typed_or_accepted_history_available:false,unknown_history_is_not_empty:true,
 only_external_documented_obligation:true,not_a_typed_transfer_or_restart_input:true,
 no_original_five_peer_CLI_pair_added_removed_or_relabelled:true,
 R725_five_eighths_physical_family_is_not_current_S5_halfwave_bhalf:true};
const pairs=[...clone(prior14.complete_external_obligation_pairs),[peer27.run_attempt_key,peer27.declared_driver_source_sha256]];
need(new Set(pairs.map(x=>x[0])).size===15,"15 distinct external runs");
const future=clone(old.actual_future);
for(const k of Object.keys(future))need(future[k]===null,"future parent not null");
const sourceRef=ref(data.current_source_binding,"/complete_source_role_registry");
const currentRuntime=ref(data.current_source_binding,"/current_complete_runtime_sources");
const binding={
 schema:"complete-fixed-fejer-halfwave-demanded-bhalf-parameter-binding-v1",
 prepared_date:data.date,session:data.session,status:"complete-parameters-prepared-no-science-executed",
 repository:data.repository,topic:data.topic,namespace:data.namespace,intended_independent_runner_label:data.intended_runner_label,
 complete_parent_documents:clone(data.parent_records),
 complete_document_sharing:{
  all_parent_bytes_preserved_by_complete_file_and_exact_JSON_pointer:true,
  original25_parameters_are_actual157_7_458_445_64_parent:true,
  older22_48_live_parameter_records_inside_the_source_delivery_are_historical_sources_only:true,
  entire25_binding:ref(data.parent_records.binding),
  entire25_science:ref(data.parent_records.science),
  entire25_pure:ref(data.parent_records.pure),
  entire25_delivery:ref(data.parent_records.delivery),
  original_ancestor_source_input_parameter_failure_and_unknown_history_preserved_in_full:true,
  no_runtime_source_or_step_object_replaced_by_a_stub:true
 },
 current_source_role_registry:{...sourceRef,complete_pairs:137,changed_pairs:14,unchanged_pairs:123},
 current_runtime_records:{...currentRuntime,complete_runtime_count:19,new_runtime_count:17},
 complete_current_source_delivery:clone(data.current_source_delivery),
 complete_location_transport_delivery:clone(old.complete_location_transport_delivery),
 current_scientific_source_change:{
  complete_current_source_binding:clone(data.current_source_binding),
  complete_current_source_publication:data.current_source_binding.fixed_publication_commit,
  complete_actual14_role_changes:clone(source.changed_current_scientific_roles),
  complete_source_change_definitions:clone(source.source_changes),
  complete_finite_range_and_source_proof:clone(source.complete_finite_range_and_source_proof),
  complete_source_reproduction:ref(data.current_source_delivery,"/complete_reproducers"),
  complete21481byte_scientific_suffix:clone(sourceDelivery.complete_scientific_suffix),
  physical_mathematical_target_seed_base_Q_and_variables_unchanged:true,
  old_S5_boundary_and_original_R724_paired_halfwaves_retained:true,
  no_R725_cutoff_epsilon_or_R726_Slerp_or_adaptive_restoration_policy_added:true,
  mathematical_equivalence_does_not_supply_actual_working_word_or_full_model_equality:true,
  source_guard_and_model_policy_identity_are_current_complete_sources:true,
  full_actual_source_registry_and_all_original_history_aliases_retained:true,
  numerical_cache_hits_or_speedup_not_claimed:true
 },
 explicit_parameter_recipe:{
  complete_parent_science_step:ref(data.parent_records.science,"/steps/0"),
  complete_parent_pure_step:ref(data.parent_records.pure,"/steps/0"),
  old_namespace:data.old_namespace,new_namespace:data.namespace,
  current_scripts:{science:science.script,pure:pure.script},
  complete_original_scopes:{science:parentScience.steps[0].scope,pure:parentPure.steps[0].scope},
  current_scopes:{science:science.scope,pure:pure.scope},
  all_numerical_argument_words_unchanged:true,numeric_changes:[],
  scientific_argv_words:157,pure_argv_words:7,
  original_step_objects_outputs_cleanup_and_formal_values_retained:true,
  only_metadata_path_script_scope_id_changes:true,
  no_live_fields_added_or_removed:true,
  original_seed_parameter_recipe:clone(old.explicit_parameter_recipe.original_seed_parameter_recipe)
 },
 original_complete_budgets:clone(old.original_complete_budgets),
 fixed_target_scope:{
  accurate_a_rho0_g_reference_chart_and_predeclared_recipe_unchanged:true,
  current_M160_J923_N2048_and_all_three_rotation_channels_unchanged:true,
  physical_S5_paired_halfwave_seed_base_Q_mean_calibration_sources_unchanged_from25:true,
  actual_current_model_point_roots_and_complete_field_are_not_inherited:true,
  complete_own_six_input_reference_binding_required_by_original_solver:true,
  no_old_runner_raw_reference_roots_or_checkpoint_transferred:true,
  all_future_actual_sources_and_models_come_from_the_new_runner:true
 },
 complete_peer_responsibilities:{
  complete_original12_objects_and_discovery_history:ref(data.parent_records.binding,"/complete_peer_responsibilities"),
  complete_prior14_external_objects_and_all_history:ref(data.complete_prior14_external_binding,"/complete_peer_responsibilities"),
  complete_external_obligation_pairs:pairs,external_obligation_count:15,
  original_twelve_retained_in_original_order:true,
  actual25_and_actual26_complete_external_records_retained_by_whole_prior14_binding:true,
  added_complete_actual27_external_peer_record:peer27,
  later_observations_separately_preserved_without_rewriting_any_earlier_object:{
   actual25:clone(data.later_actual25),actual26:clone(data.later_actual26),
   scope:"These complete newer observations are evidence only; they do not replace any earlier complete status, create a typed parent or supply a run28 field."
  },
  supported_original_five_CLI_pairs_exactly_preserved:true,supported_CLI_peer_count:5,
  exact_original_CLI_history:ref(data.parent_records.science,"/steps/0/args"),
  no_new_peer_CLI_pair_or_new_transfer_family_added:true,
  metadata_external_obligations_are_not_typed_or_restart_inputs:true,
  unknown_history_is_not_empty:true,old_source_aliases_not_relabelled_as_current:true
 },
 complete_display_correspondence:{
  complete_original25_display:ref(data.parent_records.binding,"/complete_display_correspondence"),
  complete_older_display_and_all_ancestors_retained_in_original_whole_binding:true,
  current_live_mapping:clone(science.progress_summary),
  live_counts:{normal:6,mathematical:58,total:64},
  formal_counts:{science:458,pure:445},
  all_original64_key_selector_pairs_unchanged_except_output_namespace:true,
  all_original903_formal_key_selector_pairs_unchanged_except_output_namespace:true,
  location_missing_null_or_original_error_status_retained:true,
  no_new_F_J_root_or_scientific_value_requested_by_observation:true,
  complete_existing_transport_contract:clone(old.complete_location_transport_delivery),
  compact_public_limit:16384,pretty_progress_limit:32768,queue_and_index_limit:95000
 },
 actual_future:future,
 accurate_descendant_scope:{
  all_existing_source_guards_remain_strict:true,
  old25_or_R725_26_27_accurate_consumer_not_automatically_authorized_by_physical_equivalence:true,
  necessary_followup_must_bind_current_d1c99_driver_8631_reader_fbb17_normal_and_complete137_roles:true,
  no_existing_mean_roots_geometry_or_closed_proof_reused_by_source_label:true,
  existing_R724_S5_complete_math_may_be_reused_only_under_explicit_current_source_model_point_snapshot_binding:true
 },
 scientific_scope:clone(old.scientific_scope),
 complete_steps_preservation:{
  science:{parent:clone(data.parent_records.science),parent_json_pointer:"/steps/0",...counts(science),numeric_changes:[],full_inverse_recovers_entire_original_step:true},
  pure:{parent:clone(data.parent_records.pure),parent_json_pointer:"/steps/0",...counts(pure),numeric_changes:[],full_inverse_recovers_entire_original_step:true}
 },
 root_is_only_ref_queue_request_controller_and_launch_writer:true,
 refs_queues_requests_or_workflows_modified:false,
 scientific_execution_or_AST_fixture_or_new_admission_gate_added:false
};
const out={};
const bindText=JSON.stringify(binding,null,2)+"\n";
const bindRecord=makeRecord(data.names.binding,"parameter-binding",bindText);
out.binding={value:binding,text:bindText,record:bindRecord};
for(const [kind,parent,step]of[["science",parentScience,science],["pure",parentPure,pure]]){
 const value={
  schema:"complete-fixed-fejer-halfwave-demanded-bhalf-"+kind+"-ready-v1",
  prepared_date:data.date,executed:false,queued:false,
  scientific_execution_permitted_only_in_public_Actions:true,
  intended_independent_runner_label:data.intended_runner_label,namespace:data.namespace,
  complete_parameter_binding:bindRecord,
  complete_parent_parameter_file:clone(data.parent_records[kind]),
  whole_parent_step:ref(data.parent_records[kind],"/steps/0"),
  all_parent_metadata_preserved_as_historical_full_document:ref(data.parent_records[kind]),
  complete_current_source_registry:clone(binding.current_source_role_registry),
  complete_current_runtime_records:clone(binding.current_runtime_records),
  complete_peer_responsibilities:ref(bindRecord,"/complete_peer_responsibilities"),
  complete_all64_live_correspondence:ref(bindRecord,"/complete_display_correspondence"),
  explicit_parameter_recipe:ref(bindRecord,"/explicit_parameter_recipe"),
  scientific_numeric_changes:[],
  all_original_numerical_words_budgets_and_original_fields_preserved:true,
  all64_existing_live_fields_preserved:true,
  complete_runtime_source_bytes_changed_only_as_declared_in_actual_whole_source_binding:true,
  no_current_physical_cutoff_or_seed_mechanism_change:true,
  new_AST_fixture_replay_scientific_gate_added:false,
  actual_future:clone(future),
  current_argv_word_count:counts(step).argv_words,
  current_formal_selector_count:counts(step).formal_selectors,
  current_live_selector_count:counts(step).live_selectors,
  steps:[step]
 };
 const text=JSON.stringify(value,null,2)+"\n";
 out[kind]={value,text,record:makeRecord(data.names[kind],kind+"-ready",text)};
}
return out;

}
const opts=options(process.argv.slice(2));
const generated=build(DATA,loadAll(opts["--parent-directory"]),record);
mkdirSync(opts["--generated-directory"],{recursive:true});
const results=[];
for(const [kind,item]of Object.entries(generated)){
 const expected=EXPECTED[kind];
 for(const key of ["name","path","bytes","sha256","git_blob_sha","role"])if(item.record[key]!==expected[key])throw Error("Whole generated "+key+" mismatch: "+kind);
 writeFileSync(resolve(opts["--generated-directory"],item.record.name),item.text,"utf8");
 results.push(item.record);
}
process.stdout.write(JSON.stringify({
 complete_parameter_text_reproduction:true,
 complete_original_steps_recovered_by_inverse:true,
 original_numeric_arguments_unchanged:true,
 science_argv:157,pure_argv:7,science_formal:458,pure_formal:445,live_scalars:64,
 original_CLI_peers:5,external_obligations:15,
 scientific_or_AST_fixture_execution:false,
 files:results
},null,2)+"\n");
