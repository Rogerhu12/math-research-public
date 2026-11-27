#!/usr/bin/env node
/**
 * Complete source-only reconstruction of the same actual-run10 M160 -> M320
 * immutable-point family: 15 independent complete bodies and 3 exact shared
 * original bodies. This program never imports or executes scientific Python.
 *
 * Every complete parent and output has an exact byte length and SHA256.
 * The full reference stays M160/N2048/J923; all current M320 slots are free.
 * The only supported different-source final is the real c3dc/2efa M160 family.
 * Its future report, checkpoint and point are never synthesized here.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const INPUTS = {
  "immutable_point_detached_closure_values.py": {
    "sha256": "2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb",
    "bytes": 59041,
    "git_blob_sha": "dc6e486e6aea06736558716b2590d3ff641b6ea7"
  },
  "analytic_local_stage_jacobian_immutable_point.py": {
    "sha256": "21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024",
    "bytes": 25732,
    "git_blob_sha": "218d7c7b6bfeaa8d6f9daffc204ad5df6660b840"
  },
  "analytic_normal_frame_jets_immutable_point.py": {
    "sha256": "4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa",
    "bytes": 47279,
    "git_blob_sha": "84616e0ab0e89d7a0fe96ef6836dcfc3560fdc61"
  },
  "normal_frame_c1_immutable_point.py": {
    "sha256": "53b5bc456cb3f62c6a25d329de54920253d9193168ef3fb761198ff61fa0822d",
    "bytes": 37361,
    "git_blob_sha": "087a41b9fc5e261363fd43d330dd8f0598e39b32"
  },
  "detached_stage_matrices_immutable_point.py": {
    "sha256": "a41872f7563683b28d34cb9da35d7fc3bd0879fb5a8d1d183230a518f6b8f052",
    "bytes": 47791,
    "git_blob_sha": "f835c6da819e07205a930c57518e892a27758ca8"
  },
  "adjacent_normal_matrices_immutable_point.py": {
    "sha256": "ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59",
    "bytes": 36766,
    "git_blob_sha": "44bc4531364aaaf7063c20ecda6516ab1480d0fb"
  },
  "reference_centred_immutable_point_calibration.py": {
    "sha256": "794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238",
    "bytes": 11905,
    "git_blob_sha": "f0db2b91deb565c49e2769f72e2277d39b220e5f"
  },
  "so3_reference_centred_immutable_point_normal_lift_operator.py": {
    "sha256": "9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6",
    "bytes": 98473,
    "git_blob_sha": "e72366421d50d3b3f1c99a95f764a99da0a4678e"
  },
  "immutable_point_normal_root_packets.py": {
    "sha256": "b4c41b2dc8754607441c30cdb3a34199d7e40f8b52fc5e4a8f5d653ea524eac8",
    "bytes": 71680,
    "git_blob_sha": "69984205fdad420c133b89a0ebe5bbb19d391ab1"
  },
  "run10_immutable_point_source_binding.py": {
    "sha256": "85f3007a6927968eb253eab168e9379f9a1f732caf5aa43b9f24776f39606d97",
    "bytes": 34790,
    "git_blob_sha": "2a27443be7d65a13c3e5acdeefd6a116dc82df1d"
  },
  "so3_run10_immutable_point_geometry.py": {
    "sha256": "dbbd4601f4bbc0798759f3c63cd3caae3cfc19f1a62ec9dbd02cc6fbceb896ce",
    "bytes": 70708,
    "git_blob_sha": "92f21c3cb98ff1970bbaaa3f624020ac701c7c75"
  },
  "transfer_run10_immutable_point_memory.py": {
    "sha256": "0007abf0b2814b09a3ecc30f621cbd8814a3d94528c753762aa7be5175d08486",
    "bytes": 66265,
    "git_blob_sha": "e69cd00d739753d624bfe3db3a45638f31830c07"
  },
  "fullclosed_run10_immutable_point_so3_qp.py": {
    "sha256": "a7031dfa247dd98053692b356999104d3bebe7624c635e219a55ee8133ea8a65",
    "bytes": 87787,
    "git_blob_sha": "1f767b819495e6a3d78367ed74716d1fd0197405"
  },
  "launch_run10_immutable_point_actions.py": {
    "sha256": "668bf9170657ad6c8d3bb12fe90b688becbc2ab8c010134d430f84dd2ed072aa",
    "bytes": 21785,
    "git_blob_sha": "3d614235b11c249c291722497ffc389bb7a40a04"
  },
  "read_run10_immutable_point_so3_report.py": {
    "sha256": "41a6e7c3149f493dcabea908574a8ca0ff031cf275e9aa471e4dcff7786c67f3",
    "bytes": 97696,
    "git_blob_sha": "4fe38d92b4c115c792db95115e389628ab99c658"
  },
  "frequency_refined_public_reference_calibration.py": {
    "sha256": "b72572b13f94bf5482ced96c06aa940b5097ace270c159ec1837495519d9387a",
    "bytes": 12345,
    "git_blob_sha": "98a0548e067a7102fd1c0810f755492f9474df52"
  },
  "public_reference_frequency_binding_additions.py": {
    "sha256": "834bf1838c22ef9b16a2e9668b9656051fce347df7f928d0a4b1f25dc11fede0",
    "bytes": 13252,
    "git_blob_sha": "00a849d787a3cc62b5ca9f31935f36b18eaa78d5"
  },
  "frequency_refined_public_reference_history_transfer.py": {
    "sha256": "fdc29a36ca562cec8327a2ca250ecdd3a505827415617255993b6fcab5389279",
    "bytes": 82084,
    "git_blob_sha": "99b78780fef8c4ed9143e7167e48bb94aabafdc5"
  },
  "so3_frequency_refined_smooth_triangle_meridian_operator.py": {
    "sha256": "41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2",
    "bytes": 42982,
    "git_blob_sha": "20b4707c1ea7628d7bd922d24ba0226da276c2d1"
  },
  "frequency_refined_smooth_triangle_literal_zero_moment_input.py": {
    "sha256": "bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971",
    "bytes": 31068,
    "git_blob_sha": "6a4d1e1465a115175738e1f023cc9d9f6aa2767e"
  },
  "so3_frequency_refinement_layout.py": {
    "sha256": "ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27",
    "bytes": 13582,
    "git_blob_sha": "8d459b9b1dc3defda44b58bc36c306fe586c484e"
  }
};
const OUTPUTS = {
  "run10_frequency_immutable_point_closure_values.py": {
    "sha256": "e87044f0b0a51c9552f3f4028617a433c661e73b6a4507a6edb5ddbab7a877fb",
    "bytes": 59808
  },
  "run10_frequency_immutable_point_stage_jacobian.py": {
    "sha256": "3f351c6b0aa80ff025e5714f8dcbf67cba870e5e9c45b9ad80b61198e5fa00ed",
    "bytes": 25743
  },
  "run10_frequency_immutable_point_normal_frame.py": {
    "sha256": "83f864898f1ed0ebd45f02aafa354b084978e9e623816d1b6c52777964b149c4",
    "bytes": 47290
  },
  "run10_frequency_immutable_point_frame_c1.py": {
    "sha256": "fbe2f08578c6ea21c1e481e8f37b9ff973838e841329e20d87fa53753def96aa",
    "bytes": 37361
  },
  "run10_frequency_immutable_point_stage_matrices.py": {
    "sha256": "93944b0a344e9d155477b874dc215cc104e616e74bcee536609484e1cddc8168",
    "bytes": 47791
  },
  "run10_frequency_immutable_point_adjacent_matrices.py": {
    "sha256": "2331d3a43188b39eeb3522094af1351ca8df46fe0820cf65597cb04b8d19c40c",
    "bytes": 36766
  },
  "run10_frequency_immutable_point_calibration.py": {
    "sha256": "61ad9a9e782c0fd67bf83887d8414968946e8543baac773dcc628419f0248992",
    "bytes": 12374
  },
  "so3_run10_frequency_immutable_point_normal_lift.py": {
    "sha256": "a53b2ad03c1c5ba81a0392c6fe7bd08076f6e8f3f11e64f7e997f8319bedc8aa",
    "bytes": 98516
  },
  "immutable_run10_frequency_root_packets.py": {
    "sha256": "bdc6e3c714f919deb27ac72400a2d3391cd288a3d089d5baaaaa6eac17759b2f",
    "bytes": 72379
  },
  "run10_frequency_immutable_point_source_binding.py": {
    "sha256": "1cf73abf9170964d194b1963c0fb54839c9326bb509510eee04303746f6fa1f8",
    "bytes": 38000
  },
  "transfer_run10_frequency_immutable_point_memory.py": {
    "sha256": "952790e603606e1efeff10c89580383567e7e645524a4601b68dde1bbe09207b",
    "bytes": 82837
  },
  "so3_run10_frequency_immutable_point_geometry.py": {
    "sha256": "eac5997e6bc27d4b510a2933e0d2c3c4bc73d37c9316a77bcf257df9f45e9aa5",
    "bytes": 70768
  },
  "fullclosed_run10_frequency_immutable_point_so3_qp.py": {
    "sha256": "1ea2b362cb714a37daa44d8eec9a67eba355b9cb555f07fb465c1cb056f794bb",
    "bytes": 91975
  },
  "launch_run10_frequency_immutable_point_actions.py": {
    "sha256": "6894d7d1b057d13daa8d38d82522bfb8e36626b0372d64c067290fdbfdb3b326",
    "bytes": 22348
  },
  "read_run10_frequency_immutable_point_so3_report.py": {
    "sha256": "24939deed9a2b24732608a182d039751f8259f16f4d7f20acac40115f218c08b",
    "bytes": 98133
  },
  "so3_frequency_refined_smooth_triangle_meridian_operator.py": {
    "sha256": "41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2",
    "bytes": 42982
  },
  "frequency_refined_smooth_triangle_literal_zero_moment_input.py": {
    "sha256": "bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971",
    "bytes": 31068
  },
  "so3_frequency_refinement_layout.py": {
    "sha256": "ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27",
    "bytes": 13582
  }
};
const IMMUTABLE_ROLE_NAMES = {
  "closure_values": "immutable_point_detached_closure_values.py",
  "analytic_J3": "analytic_local_stage_jacobian_immutable_point.py",
  "analytic_frame": "analytic_normal_frame_jets_immutable_point.py",
  "frame_C1": "normal_frame_c1_immutable_point.py",
  "stage_matrices": "detached_stage_matrices_immutable_point.py",
  "adjacent_matrices": "adjacent_normal_matrices_immutable_point.py",
  "reference_calibration": "reference_centred_immutable_point_calibration.py",
  "endpoint": "so3_reference_centred_immutable_point_normal_lift_operator.py",
  "root_packets": "immutable_point_normal_root_packets.py",
  "analytic_J3_binding": "run10_immutable_point_source_binding.py",
  "geometry": "so3_run10_immutable_point_geometry.py",
  "envelope_transfer": "transfer_run10_immutable_point_memory.py",
  "driver": "fullclosed_run10_immutable_point_so3_qp.py",
  "launcher": "launch_run10_immutable_point_actions.py",
  "reader": "read_run10_immutable_point_so3_report.py"
};
const sha256=s=>crypto.createHash('sha256').update(s,'utf8').digest('hex');
const utf8=s=>Buffer.from(s,'utf8');

function readComplete(directory,name) {
 const expected=INPUTS[name],raw=fs.readFileSync(path.join(directory,name));
 const source=raw.toString('utf8');
 if(!Buffer.from(source,'utf8').equals(raw)||raw.length!==expected.bytes||sha256(source)!==expected.sha256)
  throw new Error('Changed whole source '+name);
 return {source,record:{name,...expected}};
}
function literalSourceRoles(source) {
 const start=source.indexOf('SOURCE_PINS = '),end=source.indexOf('\n\nROOT_SNAPSHOT_SCHEMA',start);
 if(start<0||end<start)throw new Error('One complete literal parent source table is required');
 const raw=source.slice(start+'SOURCE_PINS = '.length,end);
 const value=JSON.parse(raw.replace(/\(/g,'[').replace(/\)/g,']'));
 if(Object.keys(value).length!==90)throw new Error('Retain the complete immutable parent 90-role table');
 return value;
}

function buildM10Lower(parents,m09,sha256,utf8) {
 const out={},ops={},inputs={}; const names={
 closure_values:"run10_frequency_immutable_point_closure_values.py",
 analytic_J3:"run10_frequency_immutable_point_stage_jacobian.py",
 analytic_frame:"run10_frequency_immutable_point_normal_frame.py",
 frame_C1:"run10_frequency_immutable_point_frame_c1.py",
 stage_matrices:"run10_frequency_immutable_point_stage_matrices.py",
 adjacent_matrices:"run10_frequency_immutable_point_adjacent_matrices.py",
 reference_calibration:"run10_frequency_immutable_point_calibration.py",
 endpoint:"so3_run10_frequency_immutable_point_normal_lift.py",
 root_packets:"immutable_run10_frequency_root_packets.py"
 };
 const schema="complete-R711-reference-centred-frequency-refined-immutable-point-closure-analytic-frame-J3-normal-layer-v1";
 const oldschema="complete-R711-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1";
 const oldbase="6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865";
 const base="41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2";
 const oldbaseschema="complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1";
 const baseschema="complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1";
 function one(role,s,a,b) {
   const n=s.split(a).length-1;if(n!==1)throw Error(role+" expected one occurrence "+a.slice(0,100)+" got "+n);
   (ops[role]??=[]).push({kind:"replace",old:a,new:b,count:1});
   return s.replace(a,b);
 }
 function all(role,s,a,b){
   const n=s.split(a).length-1;if(n<1)throw Error(role+" missing "+a);
   (ops[role]??=[]).push({kind:"replace",old:a,new:b,count:n});
   return s.split(a).join(b);
 }
 function begin(role,source,key=role){
   inputs[role]={key,sha256:sha256(source),bytes:utf8(source).length};ops[role]=[];return source;
 }
 function save(role,s){if(utf8(s).length>=100000)throw Error("oversize "+role);out[role]={name:names[role],source:s,sha256:sha256(s),bytes:utf8(s).length};}
 const chart0=parents.endpoint.source.match(/    def _chart\(self, phi\):\n[\s\S]*?(?=\n    def )/)[0];
 const chart=chart0.replace("tensor(self.freq)","tensor(self.reference_freq)");
 if(chart===chart0)throw Error("missing reference/current chart split");
 let s=begin("closure_values",parents.closure_values.source);
 s=all("closure_values",s,oldschema,schema);s=all("closure_values",s,oldbase,base);
 let line=s.split("\n").find(x=>x.startsWith("DERIVED_METHOD_SOURCES = json.loads("));
 const arg=line.slice("DERIVED_METHOD_SOURCES = json.loads(".length,-1);
 const methods=JSON.parse(JSON.parse(arg)); if(methods._chart)throw Error("unexpected old chart override");
 methods._chart=chart.trimEnd()+"\n";
 s=one("closure_values",s,line,"DERIVED_METHOD_SOURCES = json.loads("+JSON.stringify(JSON.stringify(methods))+")");
 s=one("closure_values",s,"        base_source_sha256=BASE_SOURCE_SHA256,torch_version=TORCH_VERSION,",
 "        base_source_sha256=BASE_SOURCE_SHA256,torch_version=TORCH_VERSION,\n        frozen_reference_M=160,current_M=320,\n        material_chart_uses_frozen_reference_frequencies=True,");
 save("closure_values",s);
 for(const role of ["analytic_J3","analytic_frame","frame_C1","stage_matrices","adjacent_matrices"]){
   s=begin(role,parents[role].source);
   if(s.includes(oldschema))s=all(role,s,oldschema,schema);
   s=all(role,s,oldbase,base);
   for(const dep of ["closure_values","analytic_J3","analytic_frame","frame_C1","stage_matrices"]){
     if(out[dep]&&s.includes(parents[dep].record.sha256))s=all(role,s,parents[dep].record.sha256,out[dep].sha256);
   }
   save(role,s);
 }
 s=begin("reference_calibration",m09.reference_calibration.source,"M09:frequency_refined_public_reference_calibration.py");
 s=one("reference_calibration",s,s.match(/^ENDPOINT_SCHEMA = .+$/m)[0],"ENDPOINT_SCHEMA = '"+schema+"'");
 save("reference_calibration",s);
 s=begin("endpoint",parents.endpoint.source);
 s=all("endpoint",s,oldschema,schema);s=all("endpoint",s,oldbase,base);
 s=all("endpoint",s,oldbaseschema,baseschema);
 s=all("endpoint",s,"307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7","bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971");
 for(const [a,b] of [
 ["supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1","frequency-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1"],
 ["supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1","frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1"]])
 {if(s.includes(a))s=all("endpoint",s,a,b);}
 for(const dep of ["closure_values","analytic_J3","analytic_frame","frame_C1","stage_matrices","adjacent_matrices","reference_calibration"]){
   s=all("endpoint",s,parents[dep].record.sha256,out[dep].sha256);
 }
 s=one("endpoint",s,chart0,chart);save("endpoint",s);
 s=begin("root_packets",parents.root_packets.source);
 const spec="    '"+out.endpoint.sha256+"': dict(schema='"+schema+"',\n"+
 "        base='"+base+"',\n"+
 "        adjacent='"+out.adjacent_matrices.sha256+"',calibration='"+out.reference_calibration.sha256+"',\n"+
 "        analytic='"+out.analytic_J3.sha256+"',analytic_frame='"+out.analytic_frame.sha256+"',\n"+
 "        closure_values='"+out.closure_values.sha256+"'),\n";
 s=one("root_packets",s,"NORMALS = {\n","NORMALS = {\n"+spec);save("root_packets",s);
 return {schema,base_schema:baseschema,outputs:out,patches:ops,inputs};
}


function buildM10Binding(parent,adds,lower,sha256,utf8) {
 const ops=[]; const one=(s,a,b)=>{let n=s.split(a).length-1;if(n!==1)throw Error("binding count "+n+" "+a.slice(0,80));ops.push({kind:"replace",old:a,new:b,count:n});return s.replace(a,b);};
 const all=(s,a,b)=>{let n=s.split(a).length-1;if(!n)throw Error("binding missing "+a);ops.push({kind:"replace",old:a,new:b,count:n});return s.split(a).join(b);};
 function body(s,n){const i=s.indexOf("def "+n+"(");if(i<0)throw Error(n);let j=s.slice(i+4).search(/\ndef /);return s.slice(i,j<0?s.length:i+4+j+1).trimEnd()+"\n";}
 let extra=adds.slice(adds.indexOf("def _bound_module"));
 extra=extra.split("public09").join("actual_run10").split("run09").join("run10");
 let validator=body(parent,"_compatible_immutable_point_parent");
 const start=validator.indexOf("    directory=Path(source_directory).resolve()");
 const end=validator.indexOf("    before,after=copy.deepcopy(old),copy.deepcopy(new)");
 let v="def _validate_original_parent_model(old,directory,current_pins):\n";
 v+="    if (old.get('source_sha256')!=IMMUTABLE_POINT_PARENT_NORMAL\n            or old.get('schema')!='complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1'):\n        raise ValueError('Use the complete actual c3dc run10 M160 source-bound field')\n";
 v+=validator.slice(start,end).replace("Path(source_directory).resolve()","Path(directory).resolve()");
 v+="    if sha(driver_path)!=IMMUTABLE_POINT_PARENT_DRIVER[1] or sha(binding_path)!=IMMUTABLE_POINT_PARENT_BINDING[1]:\n        raise ValueError('The entire actual parent source changed during validation')\n    return tuple(module.POLICY_KEYS.values())\n";
 extra=extra.replace(body(extra,"_validate_original_parent_model"),v+"\n\n");
 extra=extra.replace("old_policy_keys=_validate_original_parent_model(old,source_directory)","old_policy_keys=_validate_original_parent_model(old,source_directory,current_pins)");
 let s=parent;
 s=one(s,s.slice(s.indexOf("def _compatible_immutable_point_parent"),s.indexOf("def read_actual")),extra+"\n\n");
 s=one(s,s.match(/^SCHEMA = .+$/m)[0],"SCHEMA = 'complete-run10-frequency-refined-immutable-point-source-model-binding-v1'");
 s=one(s,s.match(/^OPERATOR_SCHEMA = .+$/m)[0],"OPERATOR_SCHEMA = '"+lower.schema+"'");
 s=one(s,s.match(/^ROOT_SNAPSHOT_SCHEMA = .+$/m)[0],"ROOT_SNAPSHOT_SCHEMA = 'actual-run10-frequency-refined-immutable-point-current-snapshot-v1'");
 s=one(s,s.match(/^BASE_SOURCE_SHA256 = .+$/m)[0],"BASE_SOURCE_SHA256 = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'");
 const roles=["analytic_J3","frame_C1","stage_matrices","adjacent_matrices","reference_calibration","endpoint","analytic_frame","closure_values"];
 const pins=Object.fromEntries(roles.map(r=>[r,[lower.outputs[r].name,lower.outputs[r].sha256]]));
 s=one(s,s.match(/^SOURCE_BINDINGS = .+$/m)[0],"SOURCE_BINDINGS = "+JSON.stringify(pins));
 s=one(s,"    policies=_policies(directory)\n","    _layout(directory).validate_base_model(model['base_complete_model'],expected_base_source_sha256=BASE_SOURCE_SHA256)\n    policies=_policies(directory)\n");
 s=one(s,"        analytic_normal_frame=frame,detached_closure_value_reuse=closure,\n","        analytic_normal_frame=frame,detached_closure_value_reuse=closure,\n        frequency_refinement=frequency_refinement_binding(report,roles=roles,source_directory=source_directory),\n");
 return {name:"run10_frequency_immutable_point_source_binding.py",source:s,sha256:sha256(s),bytes:utf8(s).length,patches:ops,parent_sha256:sha256(parent)};
}


function buildM10Transfer(parent,immutable,binding,sha256,utf8){
 const ops=[];const one=(s,a,b)=>{const n=s.split(a).length-1;if(n!==1)throw Error("transfer "+n+" "+a.slice(0,100));ops.push({kind:"replace",old:a,new:b,count:n});return s.replace(a,b);};
 const all=(s,a,b)=>{const n=s.split(a).length-1;if(n<1)throw Error("transfer missing "+a);ops.push({kind:"replace",old:a,new:b,count:n});return s.split(a).join(b);};
 let s=parent;
 s=one(s,"SCHEMA = 'strict-public09-M160-to-M320-complete-material-history-transfer-v1'","SCHEMA = 'strict-run10-M160-to-M320-immutable-point-complete-history-transfer-v1'");
 s=one(s,"ANALYTIC_BINDING_SOURCE_SHA256 = 'a62e122d32b5a8faa7e1dee82e8f8855c40c1f2d8a1bceeb14a298a6512ba931'","ANALYTIC_BINDING_SOURCE_SHA256 = '"+binding.sha256+"'");
 s=one(s,"CURRENT_MEMORY_SOURCE_SHA256 = '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'","CURRENT_MEMORY_SOURCE_SHA256 = 'f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba'");
 const start=immutable.indexOf("PARENT_FAMILIES = {\n")+"PARENT_FAMILIES = {\n".length;
 const stop=immutable.indexOf("    'ff5444",start);
 if(start<20||stop<start)throw Error("parent family source missing");
 const family=immutable.slice(start,stop);
 s=one(s,"PARENT_FAMILIES = {\n","PARENT_FAMILIES = {\n"+family);
 s=all(s,"frequency_refined_public_reference_source_binding.py",binding.name);
 s=one(s,"complete_material_envelope_memory_public_reference.py","complete_material_envelope_memory_public_run10.py");
 s=one(s,"legacy_actual_7c_final_is_not_the_run09_full_reference_target=True,","legacy_actual_7c_final_is_not_the_run10_full_reference_target=True,");
 s=one(s,"actual_public09_M160_complete_terminal_transfer_supported=True,",
 "actual_run10_c3dc_M160_complete_terminal_and_full13_final_transfer_supported=True,\n        actual_run09_ff544_complete_final_transfer_supported=False,\n        unknown_historical_run09_obligations_preserved=True,");
 s=one(s,"full_actual_run09_input_and_target_validation_retained=True,","full_actual_run10_input_and_target_validation_retained=True,");
 s=one(s,"9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18","fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a");
 s=one(s,"306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a","9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209");
 s=one(s,"actual_origin_run_id='45943410994'","actual_origin_run_id='45972294636'");
 s=one(s,"2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d","4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf");
 s=one(s,"actual-public09-M320-input-point-and-fixed-reference-v1","actual-run10-M320-input-point-and-fixed-reference-v1");
 return {name:"transfer_run10_frequency_immutable_point_memory.py",source:s,bytes:utf8(s).length,sha256:sha256(s),patches:ops,parent_sha256:sha256(parent)};
}


function buildM10Upper(parents,sourceRoles,lower,binding,transfer,shared,sha256,utf8) {
 const outputs={},ops={};
 const roles={...lower.outputs,analytic_J3_binding:binding,envelope_transfer:transfer,...shared};
 const baseSchema=lower.base_schema;
 const oldschema="complete-R711-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1";
 const snapshot="actual-run10-frequency-refined-immutable-point-current-snapshot-v1";
 const driverSchema="complete-run10-M320-immutable-point-material-envelope-SO3-QP-v1";
 function one(r,s,a,b){const n=s.split(a).length-1;if(n!==1)throw Error(r+" "+n+" "+a.slice(0,100));(ops[r]??=[]).push({kind:"replace",old:a,new:b,count:n});return s.replace(a,b);}
 function all(r,s,a,b){const n=s.split(a).length-1;if(n<1)throw Error(r+" missing "+a);(ops[r]??=[]).push({kind:"replace",old:a,new:b,count:n});return s.split(a).join(b);}
 function assign(r,s,k,v){const m=s.match(new RegExp("^"+k+" = .+$","m"));if(!m)throw Error(k);return one(r,s,m[0],k+" = '"+v+"'");}
 function save(role,name,source){if(utf8(source).length>=100000)throw Error("oversize "+role);outputs[role]={name,source,bytes:utf8(source).length,sha256:sha256(source)};}
 const common=[
 [oldschema,lower.schema],
 ["complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1",baseSchema],
 ["supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1","frequency-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1"],
 ["supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1","frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1"],
 ["actual-reference-centred-immutable-point-closure-value-current-point-snapshot-v1",snapshot]
 ];
 for(const[r,v]of Object.entries(roles)){
    if(sourceRoles[r])common.push([sourceRoles[r][1],v.sha256],[sourceRoles[r][0].split("/").pop(),v.name]);
 }
 function replaceKnown(role,s){for(const[a,b]of common)if(s.includes(a)&&a!==b)s=all(role,s,a,b);return s;}
 let geo=replaceKnown("geometry",parents.geometry.source);
 geo=assign("geometry",geo,"SCHEMA","complete-run10-M320-immutable-point-envelope-world-geometry-v1");
 save("geometry","so3_run10_frequency_immutable_point_geometry.py",geo);roles.geometry=outputs.geometry;
 common.push([sourceRoles.geometry[1],outputs.geometry.sha256],[sourceRoles.geometry[0].split("/").pop(),outputs.geometry.name]);
 const pins=JSON.parse(JSON.stringify(sourceRoles));
 for(const[r,v]of Object.entries(roles)){
   if(sourceRoles[r]){
     if(pins["frequency_parent_"+r])throw Error("alias collision "+r);
     pins["frequency_parent_"+r]=sourceRoles[r];
   }
   pins[r]=["scripts/resume_20261126/"+v.name,v.sha256];
 }
 pins.frequency_parent_driver=["scripts/resume_20261126/"+parents.driver.record.name,parents.driver.record.sha256];
 pins.frequency_parent_reader=["scripts/resume_20261126/"+parents.reader.record.name,parents.reader.record.sha256];
 const pretty=ps=>"{"+Object.entries(ps).map(([k,v])=>JSON.stringify(k)+": ("+JSON.stringify(v[0])+", "+JSON.stringify(v[1])+")").join(", ")+"}";
 let d=parents.driver.source;ops.driver=[];
 const tableStart=d.indexOf("SOURCE_PINS = "),tableEnd=d.indexOf("\n\nROOT_SNAPSHOT_SCHEMA",tableStart);
 if(tableStart<0||tableEnd<tableStart)throw Error("table boundary");
 // Preserve every old record before substituting current source roles.
 const placeholder="SOURCE_PINS = __COMPLETE_SOURCE_TABLE_PENDING__";
 d=one("driver",d,d.slice(tableStart,tableEnd),placeholder);
 d=replaceKnown("driver",d);
 d=one("driver",d,placeholder,"SOURCE_PINS = "+pretty(pins));
 d=assign("driver",d,"SCHEMA",driverSchema);
 const addArg="    p.add_argument('--angles', type=int, default=2048)";
 const newArg=addArg+"\n    p.add_argument('--current-modes', type=int, default=320)";
 const check="    if (a.material_envelope_binding is None or a.normal_stages!=32 or a.integration_order!=8\n            or a.current_modes!=320 or a.angles!=2048):\n        raise ValueError('M-only inclusion retains the complete actual target, all 32 stages, N2048 and eight radial Gauss nodes')\n";
 d=one("driver",d,addArg,newArg);
 d=one("driver",d,"    a.manifest = [path.resolve() for path in a.manifest]",check+"    a.manifest = [path.resolve() for path in a.manifest]");
 d=one("driver",d,"    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])",
 "    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])\n    frequency_layout = load('_complete_actual_frequency_layout',paths['frequency_layout'])");
 d=one("driver",d,"seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean)",
 "seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean,\n        current_modes=args.current_modes,frequency_layout_module=frequency_layout)");
 d=one("driver",d,"    if prior_final_point is not None:\n        x = prior_final_point\n",
 "    if prior_final_point is not None:\n        x = prior_final_point\n    frequency_record=envelope_transfer.frequency_initial_record(args,q,x,\n        transfer_record=envelope_transfer_record,seed_record=prior_final_seed)\n");
 d=one("driver",d,"        representation=q.model, coordinate_norm=coordinates.record,",
 "        representation=q.model, coordinate_norm=coordinates.record,\n        frequency_refinement=frequency_record,reference_M=160,current_M=320,\n        frequency_layout_definition=base.frequency_layout_definition,\n        frequency_layout_identity_sha256=base.model['frequency_layout_identity_sha256'],\n        frequency_layout_source=file_record(paths['frequency_layout']),\n        radial_observation_refinement_performed=False,angular_observation_refinement_performed=False,\n        full_fixed_reference_target_unchanged=True,saved_parent_Phi_used_as_current_baseline=False,");
 const marker="    def save_report():";
 if(d.slice(d.indexOf(marker))!==parents.driver.source.slice(parents.driver.source.indexOf(marker)))throw Error("changed scientific suffix");
 save("driver","fullclosed_run10_frequency_immutable_point_so3_qp.py",d);
 let l=replaceKnown("launcher",parents.launcher.source);
 l=assign("launcher",l,"DRIVER_SHA",outputs.driver.sha256);
 l=all("launcher",l,parents.driver.record.name,outputs.driver.name);
 l=one("launcher",l,addArg,newArg);
 l=one("launcher",l,"    a.manifest = [path.resolve() for path in a.manifest]",check+"    a.manifest = [path.resolve() for path in a.manifest]");
 l=one("launcher",l,"        fixed_supported_unit_seed=True,",
 "        fixed_supported_unit_seed=True,reference_M=160,current_M=args.current_modes,\n        every_original_free_word_retained_with_correct_three_block_zero_inclusion=True,\n        original_reference_M160_chart_and_N2048_radial_observer_retained=True,");
 save("launcher","launch_run10_frequency_immutable_point_actions.py",l);
 let r=replaceKnown("reader",parents.reader.source);
 r=assign("reader",r,"DRIVER_SHA",outputs.driver.sha256);
 r=assign("reader",r,"REPORT_SCHEMA",driverSchema);
 r=all("reader",r,parents.driver.record.name,outputs.driver.name);
 r=one("reader",r,"                    'all_original_outer_free_variables_and_norm_layout_unchanged'))",
 "                    'all_original_outer_free_variables_retained_and_new_modes_added',\n                    'frozen_reference_layout_unchanged','current_norm_layout_changed'))");
 r=one("reader",r,"schema='actual-run10-detached-closure-value-packet-envelope-SO3-readout-v1'",
 "schema='actual-run10-M320-immutable-point-envelope-SO3-readout-v1'");
 r=one("reader",r,"        material_envelope_transfer=transfer_binding,\n",
 "        material_envelope_transfer=transfer_binding,\n        frequency_refinement=report['frequency_refinement'],\n        frequency_refinement_binding=extra['analytic_J3_binding']['frequency_refinement'],\n        reference_M=report['reference_M'],current_M=report['current_M'],\n        frequency_layout_identity_sha256=report['frequency_layout_identity_sha256'],\n");
 save("reader","read_run10_frequency_immutable_point_so3_report.py",r);
 return {outputs,patches:ops,pins,driverSchema,snapshot,scientific_suffix_sha256:sha256(d.slice(d.indexOf(marker))),scientific_suffix_bytes:utf8(d.slice(d.indexOf(marker))).length};
}


function deriveAll(input) {
 const parents=Object.fromEntries(Object.entries(IMMUTABLE_ROLE_NAMES).map(([r,n])=>[r,input[n]]));
 const m09={reference_calibration:input['frequency_refined_public_reference_calibration.py']};
 const lower=buildM10Lower(parents,m09,sha256,utf8);
 const binding=buildM10Binding(parents.analytic_J3_binding.source,
  input['public_reference_frequency_binding_additions.py'].source,lower,sha256,utf8);
 const transfer=buildM10Transfer(input['frequency_refined_public_reference_history_transfer.py'].source,
  parents.envelope_transfer.source,binding,sha256,utf8);
 const shared=Object.fromEntries([
  ['meridian','so3_frequency_refined_smooth_triangle_meridian_operator.py'],
  ['new_moment_input','frequency_refined_smooth_triangle_literal_zero_moment_input.py'],
  ['frequency_layout','so3_frequency_refinement_layout.py']
 ].map(([r,n])=>[r,{name:n,source:input[n].source,bytes:utf8(input[n].source).length,sha256:sha256(input[n].source)}]));
 const upper=buildM10Upper(parents,literalSourceRoles(parents.driver.source),
  lower,binding,transfer,shared,sha256,utf8);
 const runtime={...lower.outputs,analytic_J3_binding:binding,envelope_transfer:transfer,...upper.outputs,...shared};
 for(const [role,item]of Object.entries(runtime)) {
  const expected=OUTPUTS[item.name];
  if(!expected||utf8(item.source).length!==expected.bytes||sha256(item.source)!==expected.sha256)
   throw new Error('The entire regenerated source differs: '+role);
 }
 if(Object.keys(runtime).length!==18||Object.keys(upper.pins).length!==107)
  throw new Error('The complete source/layout family is incomplete');
 const old=Object.values(literalSourceRoles(parents.driver.source)).map(v=>JSON.stringify(v));
 const current=new Set(Object.values(upper.pins).map(v=>JSON.stringify(v)));
 if(old.some(v=>!current.has(v)))throw new Error('An original complete source role was removed');
 return {runtime,source_roles:upper.pins,suffix_bytes:upper.scientific_suffix_bytes,
  suffix_sha256:upper.scientific_suffix_sha256};
}
function main(argv) {
 const opts={};
 for(let i=0;i<argv.length;i+=2) {
  if(!['--source-directory','--generated-directory'].includes(argv[i])||argv[i+1]===undefined||opts[argv[i]])
   throw new Error('Use both complete source and fresh generated directory arguments once');
  opts[argv[i]]=path.resolve(argv[i+1]);
 }
 const sourceDir=opts['--source-directory'],out=opts['--generated-directory'];
 if(!sourceDir||!out||out===sourceDir||out.startsWith(sourceDir+path.sep))
  throw new Error('Use a separate new output directory; preserve every complete input source');
 if(fs.existsSync(out))throw new Error('The complete source output directory must be fresh');
 const input=Object.fromEntries(Object.keys(INPUTS).map(n=>[n,readComplete(sourceDir,n)]));
 const result=deriveAll(input);
 fs.mkdirSync(out,{recursive:true});
 for(const item of Object.values(result.runtime))fs.writeFileSync(path.join(out,item.name),item.source,{encoding:'utf8',flag:'wx'});
 for(const n of Object.keys(INPUTS))readComplete(sourceDir,n);
 console.log(JSON.stringify({complete:true,whole_sources:18,independent_new_sources:15,unchanged_shared_sources:3,
  complete_source_roles:107,scientific_suffix_bytes:result.suffix_bytes,
  scientific_suffix_sha256:result.suffix_sha256,all_full_output_SHA256_verified:true,
  local_Python_AST_or_compile_performed:false,scientific_imports_or_execution:false}));
}
if(path.resolve(process.argv[1]||'')===fileURLToPath(import.meta.url))main(process.argv.slice(2));
