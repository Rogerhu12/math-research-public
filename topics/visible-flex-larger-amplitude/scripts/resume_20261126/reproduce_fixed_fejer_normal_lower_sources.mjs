#!/usr/bin/env node
/**
 * Complete source-only reconstruction of the fixed Fejer normal lower family.
 * Reads nine immutable complete M160 parent sources plus four complete new
 * reference/seed/base/Q sources. It writes all nine independent full outputs.
 * No Python import, field, root, quadrature, Jacobian or numerical test occurs.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const PARENTS = {
  "closure_values": {
    "role": "closure_values",
    "name": "immutable_point_detached_closure_values.py",
    "bytes": 59041,
    "sha256": "2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb",
    "git_blob_sha": "dc6e486e6aea06736558716b2590d3ff641b6ea7"
  },
  "analytic_J3": {
    "role": "analytic_J3",
    "name": "analytic_local_stage_jacobian_immutable_point.py",
    "bytes": 25732,
    "sha256": "21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024",
    "git_blob_sha": "218d7c7b6bfeaa8d6f9daffc204ad5df6660b840"
  },
  "analytic_frame": {
    "role": "analytic_frame",
    "name": "analytic_normal_frame_jets_immutable_point.py",
    "bytes": 47279,
    "sha256": "4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa",
    "git_blob_sha": "84616e0ab0e89d7a0fe96ef6836dcfc3560fdc61"
  },
  "frame_C1": {
    "role": "frame_C1",
    "name": "normal_frame_c1_immutable_point.py",
    "bytes": 37361,
    "sha256": "53b5bc456cb3f62c6a25d329de54920253d9193168ef3fb761198ff61fa0822d",
    "git_blob_sha": "087a41b9fc5e261363fd43d330dd8f0598e39b32"
  },
  "stage_matrices": {
    "role": "stage_matrices",
    "name": "detached_stage_matrices_immutable_point.py",
    "bytes": 47791,
    "sha256": "a41872f7563683b28d34cb9da35d7fc3bd0879fb5a8d1d183230a518f6b8f052",
    "git_blob_sha": "f835c6da819e07205a930c57518e892a27758ca8"
  },
  "adjacent_matrices": {
    "role": "adjacent_matrices",
    "name": "adjacent_normal_matrices_immutable_point.py",
    "bytes": 36766,
    "sha256": "ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59",
    "git_blob_sha": "44bc4531364aaaf7063c20ecda6516ab1480d0fb"
  },
  "reference_calibration": {
    "role": "reference_calibration",
    "name": "reference_centred_immutable_point_calibration.py",
    "bytes": 11905,
    "sha256": "794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238",
    "git_blob_sha": "f0db2b91deb565c49e2769f72e2277d39b220e5f"
  },
  "endpoint": {
    "role": "endpoint",
    "name": "so3_reference_centred_immutable_point_normal_lift_operator.py",
    "bytes": 98473,
    "sha256": "9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6",
    "git_blob_sha": "e72366421d50d3b3f1c99a95f764a99da0a4678e"
  },
  "root_packets": {
    "role": "root_packets",
    "name": "immutable_point_normal_root_packets.py",
    "bytes": 71680,
    "sha256": "b4c41b2dc8754607441c30cdb3a34199d7e40f8b52fc5e4a8f5d653ea524eac8",
    "git_blob_sha": "69984205fdad420c133b89a0ebe5bbb19d391ab1"
  }
};
const INPUTS = {
  "reference": {
    "role": "reference",
    "name": "fixed_fejer_axisymmetric_reference.py",
    "bytes": 60335,
    "sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
    "git_blob_sha": "8ad0794ebf0daab9a278c5ea1de784e93b64fd8c"
  },
  "seed_reference": {
    "role": "seed_reference",
    "name": "fixed_fejer_supported_meridian_reference.py",
    "bytes": 39771,
    "sha256": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
    "git_blob_sha": "ad7f2d9ea2e63df16d900cf12885d611fef5d823"
  },
  "meridian": {
    "role": "meridian",
    "name": "fixed_fejer_supported_so3_meridian_operator.py",
    "bytes": 40840,
    "sha256": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
    "git_blob_sha": "1d9e435bb68374b71c3d7361771c28f47838d59e"
  },
  "new_moment_input": {
    "role": "new_moment_input",
    "name": "fixed_fejer_literal_zero_moment_input.py",
    "bytes": 31409,
    "sha256": "ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3",
    "git_blob_sha": "172d2b82eca6496058d2c73560de86bada50f12d"
  }
};
const OUTPUTS = {
  "closure_values": {
    "role": "closure_values",
    "name": "fixed_fejer_immutable_closure_values.py",
    "bytes": 59048,
    "sha256": "01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595"
  },
  "analytic_J3": {
    "role": "analytic_J3",
    "name": "fixed_fejer_analytic_stage_jacobian.py",
    "bytes": 25739,
    "sha256": "7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72"
  },
  "analytic_frame": {
    "role": "analytic_frame",
    "name": "fixed_fejer_analytic_normal_frame.py",
    "bytes": 47286,
    "sha256": "75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c"
  },
  "frame_C1": {
    "role": "frame_C1",
    "name": "fixed_fejer_normal_frame_c1.py",
    "bytes": 37361,
    "sha256": "1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca"
  },
  "stage_matrices": {
    "role": "stage_matrices",
    "name": "fixed_fejer_detached_stage_matrices.py",
    "bytes": 47791,
    "sha256": "7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7"
  },
  "adjacent_matrices": {
    "role": "adjacent_matrices",
    "name": "fixed_fejer_adjacent_normal_matrices.py",
    "bytes": 36766,
    "sha256": "257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0"
  },
  "reference_calibration": {
    "role": "reference_calibration",
    "name": "fixed_fejer_reference_calibration.py",
    "bytes": 11914,
    "sha256": "fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c"
  },
  "endpoint": {
    "role": "endpoint",
    "name": "fixed_fejer_normal_lift_operator.py",
    "bytes": 98490,
    "sha256": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778"
  },
  "root_packets": {
    "role": "root_packets",
    "name": "fixed_fejer_immutable_normal_root_packets.py",
    "bytes": 72375,
    "sha256": "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468"
  }
};

function buildFixedFejerLower(parents, inputs, sha256, bytes) {
  const schema="complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1";
  const baseSchema="complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1";
  const seedSchema="complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1";
  const inputSchema="fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1";
  const names={
    closure_values:"fixed_fejer_immutable_closure_values.py",
    analytic_J3:"fixed_fejer_analytic_stage_jacobian.py",
    analytic_frame:"fixed_fejer_analytic_normal_frame.py",
    frame_C1:"fixed_fejer_normal_frame_c1.py",
    stage_matrices:"fixed_fejer_detached_stage_matrices.py",
    adjacent_matrices:"fixed_fejer_adjacent_normal_matrices.py",
    reference_calibration:"fixed_fejer_reference_calibration.py",
    endpoint:"fixed_fejer_normal_lift_operator.py",
    root_packets:"fixed_fejer_immutable_normal_root_packets.py"
  };
  const sourceRoles=["reference","seed_reference","meridian","new_moment_input"];
  for(const role of sourceRoles){
    const item=inputs[role];
    if(!item||typeof item.source!=="string"||!item.record||
        sha256(item.source)!==item.record.sha256||bytes(item.source)!==item.record.bytes||
        item.record.bytes>=100000||!item.record.name.startsWith("fixed_fejer_"))
      throw Error("Complete fixed-Fejer input absent or mismatched: "+role);
  }
  if(!inputs.reference.source.includes("SCHEMA = 'R690-fixed-fejer-axisymmetric-SO3-reference-input-v1'") &&
     !inputs.reference.source.includes('SCHEMA = "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1"'))
    throw Error("The declared complete reference schema changed");
  const base=inputs.meridian.record.sha256, seed=inputs.seed_reference.record.sha256,
        binder=inputs.new_moment_input.record.sha256;
  const outputs={}, patches=[];
  function put(role,edit){
    const original=parents[role];
    if(!original||sha256(original.source)!==original.record.sha256||
       bytes(original.source)!==original.record.bytes)throw Error("Whole original lower source mismatch: "+role);
    let text=original.source;
    const steps=[];
    const change=(oldText,newText,label)=>{
      if(!oldText||oldText===newText)throw Error("Empty or vacuous complete replacement: "+role+"/"+label);
      if(text.split(oldText).length!==2)throw Error("Unique whole replacement failed: "+role+"/"+label);
      text=text.replace(oldText,newText);
      steps.push({label,old:oldText,new:newText,count:1});
    };
    const constant=(key,value)=>{
      const found=text.match(new RegExp("^"+key+" = ('[^'\\n]*'|\\\"[^\\\"\\n]*\\\")$","m"));
      if(!found)throw Error("Complete literal assignment absent: "+role+"/"+key);
      change(found[0],key+" = '"+value+"'",key);
    };
    edit(constant,change);
    let reversed=text;
    for(const step of [...steps].reverse()){
      if(reversed.split(step.new).length!==2)throw Error("Unique inverse replacement failed: "+role+"/"+step.label);
      reversed=reversed.replace(step.new,step.old);
    }
    if(reversed!==original.source)throw Error("Whole inverse does not recover parent "+role);
    if(bytes(text)>=100000)throw Error("Complete output exceeds source limit "+role);
    outputs[role]={source:text,record:{role,name:names[role],bytes:bytes(text),sha256:sha256(text)}};
    patches.push({role,parent:{...original.record},output:outputs[role].record,steps,
       whole_exact_forward_and_inverse_checked:true});
  }
  put("closure_values",(c)=>{
    c("ENDPOINT_SCHEMA",schema);c("BASE_SOURCE_SHA256",base);
  });
  const closure=outputs.closure_values.record.sha256;
  for(const role of ["analytic_J3","analytic_frame"])put(role,(c)=>{
    c("ENDPOINT_SCHEMA",schema);c("BASE_SOURCE_SHA256",base);c("CLOSURE_VALUE_SOURCE_SHA256",closure);
  });
  const j3=outputs.analytic_J3.record.sha256,frame=outputs.analytic_frame.record.sha256;
  put("frame_C1",(c)=>{
    c("ANALYTIC_STAGE_SOURCE_SHA256",j3);c("CLOSURE_VALUE_SOURCE_SHA256",closure);c("BASE_SOURCE",base);
  });
  const c1=outputs.frame_C1.record.sha256;
  put("stage_matrices",(c)=>{
    c("ANALYTIC_STAGE_SOURCE_SHA256",j3);c("FRAME_C1_SOURCE_SHA256",c1);c("BASE_SOURCE_SHA256",base);
  });
  const stage=outputs.stage_matrices.record.sha256;
  put("adjacent_matrices",(c)=>{
    c("ANALYTIC_STAGE_SOURCE_SHA256",j3);c("FRAME_C1_SOURCE_SHA256",c1);
    c("STAGE_MATRIX_SOURCE_SHA256",stage);c("BASE_SOURCE_SHA256",base);
  });
  const adjacent=outputs.adjacent_matrices.record.sha256;
  put("reference_calibration",(c)=>{
    c("ENDPOINT_SCHEMA",schema);c("BASE_SOURCE",base);c("BASE_SCHEMA",baseSchema);c("SEED_SOURCE",seed);
  });
  const calibration=outputs.reference_calibration.record.sha256;
  put("endpoint",(c,change)=>{
    c("SCHEMA",schema);c("ANALYTIC_STAGE_SOURCE_SHA256",j3);c("ANALYTIC_FRAME_SOURCE_SHA256",frame);
    c("DETACHED_CLOSURE_SOURCE_SHA256",closure);c("REFERENCE_CENTERING_SOURCE_SHA256",calibration);
    c("NEW_REFERENCE_INPUT_SCHEMA",inputSchema);c("NEW_REFERENCE_INPUT_BINDER_SHA256",binder);
    c("SUPPORTED_BASE_SCHEMA",baseSchema);c("SUPPORTED_BASE_SOURCE_SHA256",base);
    c("SUPPORTED_SEED_SOURCE_SHA256",seed);c("FRAME_C1_SOURCE_SHA256",c1);
    c("STAGE_MATRIX_SOURCE_SHA256",stage);c("ADJACENT_FRAME_SOURCE_SHA256",adjacent);
    change("or seed.get('schema') != 'complete-supported-smooth-triangle-meridian-seed-reference-v1'",
      "or seed.get('schema') != '"+seedSchema+"'","complete seed constructor schema");
  });
  const normal=outputs.endpoint.record.sha256;
  put("root_packets",(_c,change)=>{
    const entry="    '"+normal+"': dict(schema='"+schema+"',\n"+
      "        base='"+base+"',\n"+
      "        adjacent='"+adjacent+"',calibration='"+calibration+"',\n"+
      "        analytic='"+j3+"',analytic_frame='"+frame+"',\n"+
      "        closure_values='"+closure+"'),\n";
    change("NORMALS = {\n","NORMALS = {\n"+entry,"explicit complete fixed-Fejer registry entry");
  });
  const p=parents.endpoint.source,n=outputs.endpoint.source;
  const getMethods=s=>{
    const starts=[...s.matchAll(/^    def ([A-Za-z_][A-Za-z0-9_]*)\(/gm)];
    return starts.map((m,i)=>({name:m[1],text:s.slice(m.index,i+1<starts.length?starts[i+1].index:s.length)}));
  };
  const oldMethods=getMethods(p),newMethods=getMethods(n);
  if(oldMethods.length!==newMethods.length)throw Error("The complete normal method count changed");
  const changedMethods=[];
  for(let i=0;i<oldMethods.length;i++){
    if(oldMethods[i].name!==newMethods[i].name)throw Error("The complete normal method order changed");
    if(oldMethods[i].text!==newMethods[i].text)changedMethods.push(oldMethods[i].name);
  }
  if(changedMethods.length!==1||changedMethods[0]!=="__init__")
    throw Error("A mathematical normal method changed: "+JSON.stringify(changedMethods));
  return {schema,outputs,patches,normal_method_count:oldMethods.length,
    normal_methods_byte_identical_except_constructor:oldMethods.length-1,
    changed_normal_method_scope:"Only the complete seed schema literal in __init__; all equations, 32-stage paths, angular jets, physical sixjets, cache guards and J/J* bodies unchanged",
    complete_original_packet_registry_retained:true,
    actual_parent_results_or_new_reference_success_invented:false};
}

function sha256(s) { return crypto.createHash('sha256').update(s,'utf8').digest('hex'); }
function bytes(s) { return Buffer.byteLength(s,'utf8'); }
function argument(name) {
  const i=process.argv.indexOf(name);
  if(i<0 || i+1>=process.argv.length) throw Error('Required argument '+name);
  return path.resolve(process.argv[i+1]);
}
function readComplete(directory,record) {
  const file=path.join(directory,record.name);
  const st=fs.statSync(file);
  if(!st.isFile() || st.size!==record.bytes || st.size>=100000)
    throw Error('Complete source size/type mismatch: '+record.name);
  const source=fs.readFileSync(file,'utf8');
  if(bytes(source)!==record.bytes || sha256(source)!==record.sha256)
    throw Error('Complete source bytes mismatch: '+record.name);
  return {source,record};
}
const sourceDirectory=argument('--source-directory');
const generatedDirectory=argument('--generated-directory');
if(generatedDirectory===sourceDirectory ||
   generatedDirectory.startsWith(sourceDirectory+path.sep) ||
   fs.existsSync(generatedDirectory))
  throw Error('Use one fresh separate complete output directory');
const parents=Object.fromEntries(Object.entries(PARENTS).map(([r,v])=>[r,readComplete(sourceDirectory,v)]));
const inputs=Object.fromEntries(Object.entries(INPUTS).map(([r,v])=>[r,readComplete(sourceDirectory,v)]));
const result=buildFixedFejerLower(parents,inputs,sha256,bytes);
for(const [role,expected] of Object.entries(OUTPUTS)) {
  const actual=result.outputs[role];
  if(!actual || actual.record.name!==expected.name ||
      actual.record.bytes!==expected.bytes || actual.record.sha256!==expected.sha256)
    throw Error('Complete expected output mismatch: '+role);
}
fs.mkdirSync(generatedDirectory,{recursive:false});
for(const item of Object.values(result.outputs))
  fs.writeFileSync(path.join(generatedDirectory,item.record.name),item.source,{encoding:'utf8',flag:'wx'});
const check={
 schema:'complete-fixed-fejer-normal-lower-source-only-reconstruction-v1',
 complete:true, source_only:true, scientific_execution_performed:false,
 Python_AST_or_compile_performed:false,
 complete_parent_count:Object.keys(PARENTS).length,
 complete_new_input_count:Object.keys(INPUTS).length,
 complete_output_count:Object.keys(OUTPUTS).length,
 mathematical_method_byte_comparison:'All 52 non-constructor normal methods retain the complete original bytes',
 normal_method_count:result.normal_method_count,
 changed_constructor_scope:result.changed_normal_method_scope,
 old_packet_registry_entry_count:7, old_packet_registry_completely_retained:true,
 outputs:Object.values(OUTPUTS),
 patches:result.patches
};
fs.writeFileSync(path.join(generatedDirectory,'source-construction-record.json'),
 JSON.stringify(check,null,2)+'\n',{encoding:'utf8',flag:'wx'});
console.log(JSON.stringify({
 complete:true,source_only:true,scientific_execution_performed:false,
 complete_output_count:Object.keys(OUTPUTS).length,
 normal_methods_byte_identical_except_constructor:result.normal_methods_byte_identical_except_constructor
}));
