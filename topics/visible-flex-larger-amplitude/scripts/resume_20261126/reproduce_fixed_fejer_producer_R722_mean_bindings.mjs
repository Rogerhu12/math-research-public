#!/usr/bin/env node
// Complete source-only derivation. It never imports or executes Python/scientific code.
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
const SPEC = {
  "parents": {
    "kernel": {
      "name": "fixed_fejer_meridian_batched_R722_posterior_mean_jets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_R722_posterior_mean_jets.py",
      "bytes": 45225,
      "sha256": "e10a0bb386d4c44d9d8dc5ed16c75a37de1ff830754e04d57967780241feacf9",
      "git_blob_sha": "64df5fd379ae83ee5282728fc8cd3d72b3ee9c10"
    },
    "radial": {
      "name": "fixed_fejer_meridian_batched_R722_accurate_reference_control_radial_boxes.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_R722_accurate_reference_control_radial_boxes.py",
      "bytes": 46486,
      "sha256": "9da25953aeb95b88d5a878935832dac05546b778818e00e588c79581ae664953",
      "git_blob_sha": "43408b0f0bc15ad3e2f25805f315023701c354fe"
    }
  },
  "current": {
    "input": {
      "name": "fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
      "bytes": 32969,
      "sha256": "d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7",
      "git_blob_sha": "6a724fcd48a0d1da27b4762c9ac4ef6ac734cae4"
    },
    "driver": {
      "name": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
      "bytes": 99313,
      "sha256": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      "git_blob_sha": "8bba3e30bb8e843fd725a2d19f8966b984acc4ae"
    },
    "reader": {
      "name": "read_fixed_fejer_meridian_batched_so3_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_meridian_batched_so3_report.py",
      "bytes": 99382,
      "sha256": "8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49",
      "git_blob_sha": "9cd36fd99113d285fc47f17bad929647c8fc6de3"
    },
    "normal": {
      "name": "fixed_fejer_detached_meridian_normal_lift.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py",
      "bytes": 96276,
      "sha256": "76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d",
      "git_blob_sha": "fc51c16b6dbd53abf04fe9175e5421f77e25c49c"
    },
    "packet": {
      "name": "fixed_fejer_meridian_root_packets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_root_packets.py",
      "bytes": 73723,
      "sha256": "c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4",
      "git_blob_sha": "2b294ce46cf51c24c90b6e71c26d0d9c4269d28f"
    },
    "helper": {
      "name": "fixed_fejer_detached_meridian_values.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_values.py",
      "bytes": 41126,
      "sha256": "eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de",
      "git_blob_sha": "2b547c08dcaeb55701f5c68ba56d405f595f5b9e"
    },
    "kernel_name": "fixed_fejer_meridian_batched_producer_R722_posterior_mean_jets.py",
    "radial_name": "fixed_fejer_meridian_batched_producer_R722_accurate_reference_control_radial_boxes.py",
    "script_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126"
  },
  "expected": {
    "kernel": {
      "name": "fixed_fejer_meridian_batched_producer_R722_posterior_mean_jets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_posterior_mean_jets.py",
      "bytes": 45225,
      "sha256": "4fc252f8977f4f4246d2cc13583efc0bccd4b28742df3a797d1c266cdd1eac7d",
      "git_blob_sha": "e3fa2b73f5ae0dddaa049133bd9a8d61c89d8908"
    },
    "radial": {
      "name": "fixed_fejer_meridian_batched_producer_R722_accurate_reference_control_radial_boxes.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_accurate_reference_control_radial_boxes.py",
      "bytes": 46495,
      "sha256": "7c66ed0f31323451156c1cd76ae7401eb497f37377393bb66503523ad2aaac54",
      "git_blob_sha": "091a84d4222e36b0ee690e0c4f742c726dc80b17"
    }
  },
  "exact_patches": {
    "kernel": [
      {
        "label": "ACTUAL_INPUT_SHA256",
        "before": "ACTUAL_INPUT_SHA256 = \"fd299d23fcf754021dd1a3048b5f6b4008bf8542ba8e04ec2298830348ef417f\"",
        "after": "ACTUAL_INPUT_SHA256 = \"d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7\"",
        "occurrences": 1
      },
      {
        "label": "ACTUAL_DRIVER_SHA256",
        "before": "ACTUAL_DRIVER_SHA256 = \"5b0dc3573b4baa86728b0c0628a1338d339a6c4cf5cf0afcead1f4e6febcc58f\"",
        "after": "ACTUAL_DRIVER_SHA256 = \"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f\"",
        "occurrences": 1
      },
      {
        "label": "ACTUAL_READER_SHA256",
        "before": "ACTUAL_READER_SHA256 = \"79375ead2b0a93a54200d079b691e0fb8e0f74da480e3867ea7c91542f4ab222\"",
        "after": "ACTUAL_READER_SHA256 = \"8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49\"",
        "occurrences": 1
      },
      {
        "label": "ACTUAL_NORMAL_SHA256",
        "before": "ACTUAL_NORMAL_SHA256 = \"33c269f3cd04c9435ccb5144984124c8a0b6ae348f95c8bd71ac92a334c51cf4\"",
        "after": "ACTUAL_NORMAL_SHA256 = \"76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d\"",
        "occurrences": 1
      },
      {
        "label": "ACTUAL_PACKET_SHA256",
        "before": "ACTUAL_PACKET_SHA256 = \"45dd618adaa5262002bfb9d1979b6f555fe5233a57ec0f75abcec2ab7633a5be\"",
        "after": "ACTUAL_PACKET_SHA256 = \"c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4\"",
        "occurrences": 1
      }
    ],
    "radial": [
      {
        "label": "INPUT_SHA",
        "before": "INPUT_SHA = \"fd299d23fcf754021dd1a3048b5f6b4008bf8542ba8e04ec2298830348ef417f\"",
        "after": "INPUT_SHA = \"d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7\"",
        "occurrences": 1
      },
      {
        "label": "POSTERIOR_MEAN_NAME",
        "before": "POSTERIOR_MEAN_NAME = \"fixed_fejer_meridian_batched_R722_posterior_mean_jets.py\"",
        "after": "POSTERIOR_MEAN_NAME = \"fixed_fejer_meridian_batched_producer_R722_posterior_mean_jets.py\"",
        "occurrences": 1
      },
      {
        "label": "POSTERIOR_MEAN_SHA",
        "before": "POSTERIOR_MEAN_SHA = \"e10a0bb386d4c44d9d8dc5ed16c75a37de1ff830754e04d57967780241feacf9\"",
        "after": "POSTERIOR_MEAN_SHA = \"4fc252f8977f4f4246d2cc13583efc0bccd4b28742df3a797d1c266cdd1eac7d\"",
        "occurrences": 1
      }
    ]
  },
  "complete_parent_package": {
    "name": "fixed-fejer-repaired-meridian-batched-R722-mean-source-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-repaired-meridian-batched-R722-mean-source-delivery.json",
    "bytes": 29412,
    "sha256": "8003f75c3163a8702a73f7b94d5d2b8147bb5a5ac7b1bb347f1344419cd57c95",
    "git_blob_sha": "3a5c1b70573761c8a33d35788919199bf74d13ed"
  },
  "current_complete_package": {
    "name": "fixed-fejer-meridian-producer-binding-repair-complete-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-producer-binding-repair-complete-delivery.json",
    "bytes": 52830,
    "sha256": "970b8f8bbb141fc7f1c4e5e42d6048497f0de58731e65918f3c4e4cf6aff008a",
    "git_blob_sha": "45f14a52f824ca947a59bacf73ad123f17fddab9"
  },
  "current_commit": "8c1251a01aa2a1893386b69d13ab1e0a5ae4aa38"
};
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');
const H = {utf8: value => Buffer.from(value,'utf8'),sha256};
function deriveCallableR722(parents, current, hash) {
 const replace=(body,before,after,label)=>{
  if(body.split(before).length-1!==1)throw Error("Changed complete source span "+label);
  return body.replace(before,after);
 };
 const constant=(body,key,value,patches)=>{
  const lines=body.split("\n").filter(line=>line.startsWith(key+" = "));
  if(lines.length!==1)throw Error("Missing original complete source constant "+key);
  const after=key+" = "+JSON.stringify(value);
  patches.push({label:key,before:lines[0],after,occurrences:1});
  return replace(body,lines[0],after,key);
 };
 const kp=[],rp=[];
 let kernel=parents.kernel;
 for(const[key,record]of Object.entries({
  ACTUAL_INPUT_SHA256:current.input,ACTUAL_DRIVER_SHA256:current.driver,
  ACTUAL_READER_SHA256:current.reader,ACTUAL_NORMAL_SHA256:current.normal,
  ACTUAL_PACKET_SHA256:current.packet
 }))kernel=constant(kernel,key,record.sha256,kp);
 const kernel_record={name:current.kernel_name,path:current.script_path+"/"+current.kernel_name,
  bytes:hash.utf8(kernel).length,sha256:hash.sha256(kernel)};
 let radial=parents.radial;
 radial=constant(radial,"INPUT_SHA",current.input.sha256,rp);
 radial=constant(radial,"POSTERIOR_MEAN_NAME",current.kernel_name,rp);
 radial=constant(radial,"POSTERIOR_MEAN_SHA",kernel_record.sha256,rp);
 const radial_record={name:current.radial_name,path:current.script_path+"/"+current.radial_name,
  bytes:hash.utf8(radial).length,sha256:hash.sha256(radial)};
 for(const[body,patches,parent]of [[kernel,kp,parents.kernel],[radial,rp,parents.radial]]){
  let restored=body;
  for(const p of [...patches].reverse())restored=replace(restored,p.after,p.before,"reverse "+p.label);
  if(restored!==parent)throw Error("The entire original posterior/radial source was not retained");
 }
 return{kernel,radial,kernel_record,radial_record,kernel_patches:kp,radial_patches:rp};
}
async function main(){
 const words=process.argv.slice(2),args={};
 for(let i=0;i<words.length;i+=2){
  if(!['--source-directory','--generated-directory'].includes(words[i])||i+1>=words.length||words[i] in args)throw Error('Specify source and fresh generated directories exactly once');
  args[words[i]]=words[i+1];
 }
 if(Object.keys(args).length!==2)throw Error('Required: --source-directory DIR --generated-directory DIR');
 const sourceDirectory=path.resolve(args['--source-directory']),out=path.resolve(args['--generated-directory']);
 if(out===sourceDirectory||sourceDirectory.startsWith(out+path.sep)||out.startsWith(sourceDirectory+path.sep))throw Error('Keep the complete original source directory separate from generated files');
 async function read(record){
  const filename=path.join(sourceDirectory,record.name),raw=await fs.readFile(filename);
  if(raw.length!==record.bytes||sha256(raw)!==record.sha256)throw Error('Whole source identity mismatch: '+record.name);
  const s=raw.toString('utf8');
  if(!Buffer.from(s,'utf8').equals(raw))throw Error('The complete source is not valid UTF-8');
  return s;
 }
 const parents={};
 for(const role of ['kernel','radial'])parents[role]=await read(SPEC.parents[role]);
 for(const role of ['input','driver','reader','normal','packet','helper'])await read(SPEC.current[role]);
 const generated=deriveCallableR722(parents,SPEC.current,H);
 for(const role of ['kernel','radial']){
  const record=SPEC.expected[role],raw=Buffer.from(generated[role],'utf8');
  if(raw.length!==record.bytes||sha256(raw)!==record.sha256)throw Error('Complete generated identity mismatch: '+record.name);
 }
 for(const role of ['kernel','radial']){
  let inverse=generated[role];
  for(const patch of [...SPEC.exact_patches[role]].reverse()){
   if(inverse.split(patch.after).length-1!==patch.occurrences)throw Error('Changed reverse source span '+patch.label);
   inverse=inverse.split(patch.after).join(patch.before);
  }
  if(inverse!==parents[role])throw Error('Whole original source not restored');
 }
 await fs.mkdir(out,{recursive:true});
 for(const role of ['kernel','radial']){
  const record=SPEC.expected[role],filename=path.join(out,record.name);
  try {
   const existing=await fs.readFile(filename);
   if(existing.length!==record.bytes||sha256(existing)!==record.sha256)throw Error('Refuse a different existing output: '+filename);
  }catch(error){
   if(error.code!=='ENOENT')throw error;
   await fs.writeFile(filename,generated[role],{encoding:'utf8',flag:'wx'});
  }
 }
 process.stdout.write(JSON.stringify({complete_source_derivation:true,scientific_execution:false,generated:SPEC.expected},null,2)+'\n');
}
main().catch(error=>{process.stderr.write(String(error.stack||error)+'\n');process.exitCode=1;});
