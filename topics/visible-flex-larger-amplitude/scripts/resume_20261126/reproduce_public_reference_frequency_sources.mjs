#!/usr/bin/env node
/**
 * Complete source-only reconstruction of the actual public09 M160 -> M320
 * analytic-frame/J3/packet family. All 17 outputs are whole-source pinned.
 *
 * This revision was reconstructed in V8 after the executor became unavailable.
 * The complete pure text transformation was actually replayed for all 17 files,
 * each byte-identical to the previously AST/compile-checked runtime candidate.
 * This file does not claim that its Node CLI was run in the unavailable executor.
 *
 * Inputs include the already published N-only source bodies solely as immutable
 * construction material. Runtime output fixes N=2048 and changes only current M.
 * No scientific module, arrays, root, matrix or numerical fixture is evaluated.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const INPUTS = {
  "so3_frequency_refinement_layout.py": {
    "sha256": "ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27",
    "bytes": 13582
  },
  "so3_frequency_refined_smooth_triangle_meridian_operator.py": {
    "sha256": "41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2",
    "bytes": 42982
  },
  "frequency_refined_smooth_triangle_literal_zero_moment_input.py": {
    "sha256": "bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971",
    "bytes": 31068
  },
  "angular_refined_public_reference_stage_jacobian.py": {
    "sha256": "7257ff8cb625ada848a41b1ce0d37bf88a0e095196dfb7ab072f210c3da030c4",
    "bytes": 24225
  },
  "angular_refined_public_reference_normal_frame.py": {
    "sha256": "a3afa4762a0573a8eb3de026d56a0922977c6b5359b7567f322fa4c866f51aff",
    "bytes": 33669
  },
  "angular_refined_public_reference_frame_c1.py": {
    "sha256": "65b3c988178c766c3715cd08c8200b93816067e316cd260ee7da254b890fada4",
    "bytes": 35894
  },
  "angular_refined_public_reference_stage_matrices.py": {
    "sha256": "29c20d6831f15abac6b6701d4b471d75154b915c6739d9a0df84c79438c2928b",
    "bytes": 47775
  },
  "angular_refined_public_reference_adjacent_matrices.py": {
    "sha256": "5d8bc302e0bbbb48de1c47b7c7470a6904cc09c9dcda84a71c5f93455d8e9602",
    "bytes": 36761
  },
  "so3_angular_refined_public_reference_normal_lift.py": {
    "sha256": "ceaaab5f05c9faaddaff8174be9f97e9aa5b0936b9cf586990877433a9cce100",
    "bytes": 96515
  },
  "immutable_angular_refined_public_reference_root_packets.py": {
    "sha256": "ac34e4a1ded37726545fc743ca002706a8f40a1d5e3cf153472b9429559644cb",
    "bytes": 69730
  },
  "angular_refined_public_reference_source_binding.py": {
    "sha256": "0e00f37b2a504b05d5d7b5535e2bf06085f9715bd7f0992df2ad4589af85e140",
    "bytes": 28014
  },
  "reference_centred_frequency_refined_smooth_triangle_calibration.py": {
    "sha256": "688e111664eaca9f57803388f18f220c22d8bc6c4b9472589df2e06f3c8d9e47",
    "bytes": 12375
  },
  "transfer_run09_public_reference_analytic_frame_memory.py": {
    "sha256": "6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707",
    "bytes": 64221
  },
  "fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py": {
    "sha256": "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5",
    "bytes": 80726
  },
  "launch_run09_public_reference_analytic_frame_actions_v2.py": {
    "sha256": "c1888457b67c85185aebe6c91d2bd4942ccc2d2074407e17f7f54a2825927d23",
    "bytes": 21359
  },
  "read_run09_public_reference_analytic_frame_so3_report_v2.py": {
    "sha256": "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32",
    "bytes": 97351
  },
  "so3_run09_public_reference_analytic_frame_geometry_v2.py": {
    "sha256": "e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13",
    "bytes": 68903
  }
};
const TEMPLATES = {
  "public_reference_frequency_binding_additions.py": {
    "sha256": "834bf1838c22ef9b16a2e9668b9656051fce347df7f928d0a4b1f25dc11fede0",
    "bytes": 13252
  },
  "public_reference_frequency_transfer_additions.py": {
    "sha256": "efa48beb6672a6ad84e16de9c406cdc9e20b02aaed8a074af1a28f85870b1170",
    "bytes": 30194
  }
};
const OUTPUTS = {
  "frequency_refined_public_reference_adjacent_matrices.py": {
    "sha256": "610805744bdb5f4826d0c3a63bb769c9744639734db232ec31b3dbeaa0f89569",
    "bytes": 36761
  },
  "frequency_refined_public_reference_calibration.py": {
    "sha256": "b72572b13f94bf5482ced96c06aa940b5097ace270c159ec1837495519d9387a",
    "bytes": 12345
  },
  "frequency_refined_public_reference_frame_c1.py": {
    "sha256": "f272aaa95e63867d18015d9e92fa321f36785459377433a4433382794ae9c15a",
    "bytes": 35894
  },
  "frequency_refined_public_reference_history_transfer.py": {
    "sha256": "fdc29a36ca562cec8327a2ca250ecdd3a505827415617255993b6fcab5389279",
    "bytes": 82084
  },
  "frequency_refined_public_reference_normal_frame.py": {
    "sha256": "787825f17de647598099fe7b4cbfc3d82b6ad90eac9943de6b67f653f092520a",
    "bytes": 33671
  },
  "frequency_refined_public_reference_source_binding.py": {
    "sha256": "a62e122d32b5a8faa7e1dee82e8f8855c40c1f2d8a1bceeb14a298a6512ba931",
    "bytes": 34116
  },
  "frequency_refined_public_reference_stage_jacobian.py": {
    "sha256": "2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2",
    "bytes": 24227
  },
  "frequency_refined_public_reference_stage_matrices.py": {
    "sha256": "d7a6ebc317637667a18b8fb58ac8717aba8cbada981a349027bcaa60b448e4b7",
    "bytes": 47775
  },
  "frequency_refined_smooth_triangle_literal_zero_moment_input.py": {
    "sha256": "bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971",
    "bytes": 31068
  },
  "fullclosed_frequency_refined_public_reference_so3_qp.py": {
    "sha256": "0dc3bbb46df6168f3f3130bb9009ee4cd94845f455926ba036ba987a79c8cc41",
    "bytes": 86793
  },
  "immutable_frequency_refined_public_reference_root_packets.py": {
    "sha256": "4b352626ed6f306bcdb1dc0126131c8f9fb4ab3d081376ae70739ec7c9d752f9",
    "bytes": 69734
  },
  "launch_frequency_refined_public_reference_so3_actions.py": {
    "sha256": "55fbc4900dd0b049b11e4ecfa1aba642daf39a85241f0b1cb4283cf657506e03",
    "bytes": 21902
  },
  "read_frequency_refined_public_reference_so3_report.py": {
    "sha256": "f56c4f81037fa9d54edcdc566552c8eefb79cb372920419ed7e81fcf1b5aaf2e",
    "bytes": 97436
  },
  "so3_frequency_refined_public_reference_envelope_geometry.py": {
    "sha256": "be23caab6ba3b62bf02129f5da5043dffe6fe4d51b394590f16400a61dbf1de6",
    "bytes": 68931
  },
  "so3_frequency_refined_public_reference_normal_lift.py": {
    "sha256": "014fd521d315db223590d45b9b4d4da4e09975036044e533f601dcab636731d9",
    "bytes": 96556
  },
  "so3_frequency_refined_smooth_triangle_meridian_operator.py": {
    "sha256": "41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2",
    "bytes": 42982
  },
  "so3_frequency_refinement_layout.py": {
    "sha256": "ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27",
    "bytes": 13582
  }
};

function sha(source) {
    return crypto.createHash('sha256').update(source,'utf8').digest('hex');
}
function checkedText(filename,expected) {
    const bytes=fs.readFileSync(filename);
    if(bytes.length!==expected.bytes ||
            crypto.createHash('sha256').update(bytes).digest('hex')!==expected.sha256)
        throw new Error('Changed complete immutable source: '+filename);
    const text=bytes.toString('utf8');
    if(!Buffer.from(text,'utf8').equals(bytes))
        throw new Error('The complete source must round-trip as UTF-8: '+filename);
    return text;
}
const prettyPins = function(pins){return "{"+Object.keys(pins).sort().map((key,i)=>{const [path,sha]=pins[key];return(i?" ":"")+"'"+key+"': ('"+path+"',\n"+" ".repeat(key.length+6)+"'"+sha+"')"}).join(",\n")+"}";};

function deriveMTransfer(parent, funcs, bindingSHA){
const once=(s,a,b)=>{if(s.split(a).length!==2)throw new Error("Missing/ambiguous "+a.slice(0,80));return s.replace(a,b);};
const assign=(s,k,v)=>once(s,s.match(new RegExp("^"+k+" = .+$","m"))[0],k+" = '"+v+"'");
const body=(t,n)=>{const i=t.indexOf("def "+n+"(");if(i<0)throw n;const re=/\n(?=\S)/g;re.lastIndex=i+4;let m,j=t.length;while(m=re.exec(t)){if(t.slice(m.index+1).startsWith("def ")||t.slice(m.index+1).startsWith("if __name__")){j=m.index+1;break;}}return t.slice(i,j).trimEnd()+"\n";};
let s=assign(parent,"SCHEMA","strict-public09-M160-to-M320-complete-material-history-transfer-v1");
s=assign(s,"ANALYTIC_BINDING_SOURCE_SHA256",bindingSHA);
s=once(s,"HISTORY_SOURCE_SHA256 =","LAYOUT_SOURCE_SHA256 = 'ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27'\nHISTORY_SOURCE_SHA256 =");
const family="'ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'] = {'report_schema': 'complete-run09-public-reference-analytic-frame-material-envelope-SO3-QP-v1', 'reader_sha256': 'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32', 'reader_relative': 'scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py', 'operator_sha256': '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc', 'operator_schema': 'complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1', 'memory_sha256': '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'}";
s=once(s,"\n\ndef _parent_family(source, payload=None):","\n\nPARENT_FAMILIES["+family+"\n\ndef _parent_family(source, payload=None):");
s=once(s,"Path(__file__).with_name('run09_public_reference_analytic_frame_binding.py')","Path(__file__).with_name('frequency_refined_public_reference_source_binding.py')");
s=once(s,"def _compatible_models(old,new,current_pins):","def _compatible_models(old,new,current_pins,*,frozen_point_relation):");
s=once(s,"return module.compatible_legacy_model(old,new,current_pins,source_directory=path.parent)","return module.compatible_legacy_model(old,new,current_pins,source_directory=path.parent,\n        frozen_point_relation=frozen_point_relation)");
s=once(s,"        historical_parent_families_retained_for_source_bound_unknown_peer_obligations=True,","        historical_parent_families_retained_for_source_bound_unknown_peer_obligations=True,\n        actual_public09_M160_complete_terminal_transfer_supported=True,\n        frequency_layout_source_sha256=LAYOUT_SOURCE_SHA256,reference_M=160,current_M=320,J=923,full_N=2048,\n        complete_fixed_target_reference_seed_mesh_observer_Q_gamma_partition_retained=True,\n        three_unequal_rotation_blocks_copied_with_explicit_new_zero_modes=True,\n        full_actual_run09_input_and_target_validation_retained=True,");
s=once(s,"        changed_model_fields='strict terminal transfer only: complete source/schema, full explicitly bound C1/detached/adjacent/analytic-J3/complete-six-control-frame policies, and calibration source/endpoint source',","        changed_model_fields='complete declared M160-to-M320 free layout, exact dependent frozen-point identities, source/schema and fully bound unchanged matrix policies; fixed target and observer retained',");
s=once(s,"    actual_memory_sha=sha(memory.__file__)\n","    actual_memory_sha=sha(memory.__file__)\n    if (q.M!=320 or q.n!=962 or q.J!=923 or q.full_N!=2048 or q.N!=513\n            or q.base.reference_M!=160):\n        raise ValueError('Use the exact M320 current layout with the frozen M160/N2048 reference')\n");
s=once(s,"    current_carrier_sha = sha(args.carrier)\n","    frozen_relation=_frozen_initial_points(q,pins)\n    current_carrier_sha = sha(args.carrier)\n");
s=once(s,"                or payload.get('original_variables') != q.free_size","                or payload.get('M')!=160\n                or payload.get('original_variables') != q.base.frequency_layout_definition['original_free_size']");
s=once(s,"                or payload.get('fixed_scalar_metric',{}).get('identity_sha256') != q.context.scalar_identity\n                or payload.get('representation',{}).get('base_complete_model') != q.base.model):","                or payload.get('fixed_scalar_metric',{}).get('identity_sha256') != q.context.scalar_identity):");
s=once(s,"        terminal = _terminal(payload)\n        model_binding = _compatible_models(payload['representation'],q.model,pins)","        terminal = _terminal(payload)\n        _input_identity(payload,args,q)\n        model_binding = _compatible_models(payload['representation'],q.model,pins,frozen_point_relation=frozen_relation)");
s=once(s,"        if actual.get('definition') != expected_policy:\n            raise ValueError('Do not reset or change the complete envelope policy/near-active cap during transfer')","        _policy_inclusion(actual.get('definition'),expected_policy)\n        inbound=_complete_input_reports(payload,current_carrier_sha256=current_carrier_sha)\n        for item in inbound:\n            if item['kind']=='complete_preparation' and item['payload'].get('reference_definition')!=preparation['reference_definition']:\n                raise ValueError('Every complete inherited preparation must retain the same actual frozen target')");
s=once(s,"            model_binding=model_binding,family=family,","            model_binding=model_binding,family=family,inbound=inbound,");
s=once(s,"    for path in paths:\n        if path not in manifest:\n            manifest.append(path)","    for parent in parents:\n        for item in parent['inbound']:\n            path=Path(item['record']['path']).resolve()\n            if item['kind']!='complete_preparation' and path not in manifest:manifest.append(path)\n    for path in paths:\n        if path not in manifest:\n            manifest.append(path)");
s=once(s,`        if (old['implicit_grid'] != envelope.metadata()['implicit_grid']
                or old['historical_address_binding']['origin_carrier']['record']['sha256']
                    != envelope.metadata()['historical_address_binding']['origin_carrier']['record']['sha256']):
            raise ValueError('Keep the entire actual old/current material grid and angle-word union')
        locations = history.Locations(q.J,q.P,q.full_N)
        locations.walk(payload,path=('complete_source_bound_envelope_parent',))`,`        inclusion=_grid_inclusion(old,envelope.metadata())
        locations = history.Locations(q.J,q.P,q.full_N)
        for item in parent['inbound']:
            if item['kind']!='complete_preparation':
                locations.walk(item['payload'],path=('complete_original_input_history',item['record']['sha256']))
        locations.walk(payload,path=('complete_source_bound_envelope_parent',))`);
s=once(s,"            actual_complete_walker_role_fingerprints=fingerprints,","            actual_complete_walker_role_fingerprints=fingerprints,\n            complete_original_role_arrays=copy.deepcopy(old_arrays),\n            complete_original_typed_rows=copy.deepcopy(rows),\n            complete_grid_inclusion=inclusion,\n            complete_inbound_history_records=[dict(record=v['record'],kind=v['kind']) for v in parent['inbound']],\n            inherited_prior_transfer_metadata=copy.deepcopy(payload.get('material_envelope_transfer')),");
s=once(s,"                typed_core_sha256=key,actual_new_field_value_inherited=False)","                typed_core_sha256=key,actual_new_field_value_inherited=False,\n                complete_original_typed_row=copy.deepcopy(row))");
s=once(s,"        actual_current_driver_sha256=caller_record['sha256'],\n        actual_current_model_identity_sha256=q.identity,","        actual_current_driver_sha256=caller_record['sha256'],\n        actual_current_driver_source=copy.deepcopy(caller_record),\n        frozen_original_point_relation=copy.deepcopy(frozen_relation),\n        reference_M=160,current_M=320,\n        actual_current_model_identity_sha256=q.identity,");
for(const name of ["seed_from_complete_prior_final","validate_seed_metadata"])s=once(s,body(s,name),funcs[name]);
s=once(s,"    known_reports = {}\n","    _reread_transfer_parents(value,model,envelope,caller_source_sha256,carrier_sha256)\n    known_reports = {}\n");
const start=s.indexOf("        origin=parent.get('inherited_prior_independent_branch_origin')",s.indexOf("def validate_metadata(")),end=s.indexOf("        _digest(parent.get('actual_model_identity_sha256'))",start);
s=s.slice(0,start)+`        inherited=parent.get('inherited_prior_transfer_metadata')
        if not isinstance(inherited,dict):
            raise ValueError('Keep the complete prior lineage and all unresolved source-bound obligations')
        if parent.get('inherited_prior_independent_branch_origin')!=inherited.get('independent_branch_origin'):
            raise ValueError('Do not rewrite a prior independent origin for a larger current space')
`+s.slice(end);
s=once(s,"binding.get('full_base_reference_chart_profile_and_partition_equal')","binding.get('full_fixed_reference_chart_profile_seed_mesh_Q_gamma_partition_and_observer_equal')");
s=once(s,"binding.get('only_explicit_source_schema_and_matrix_working_policy_fields_changed')","binding.get('only_declared_current_frequency_layout_and_complete_source_policies_changed')");
s=once(s,"            _digest(origin.get('first_discovered_source_full_point_sha256'))","            old_row=source['complete_original_typed_rows'][origin['source_row_ordinal']]\n            if origin.get('complete_original_typed_row')!=old_row or _typed_key(old_row)!=_typed_key(row):\n                raise ValueError('Retain the entire original typed row and its complete discovery lineage')\n            _digest(origin.get('first_discovered_source_full_point_sha256'))");
s=once(s,"        continuous_certificate=False)\n","        reference_M=160,current_M=320,full_N=2048,J=923,\n        fixed_target_observer_and_original_free_variables_retained=True,continuous_certificate=False)\n");
const extra=Object.entries(funcs).filter(([k])=>!["seed_from_complete_prior_final","validate_seed_metadata"].includes(k)).map(([k,v])=>v.trimEnd());
return s+"\n\n"+extra.join("\n\n")+"\n";
}

function deriveFrequencyPackage(input, template, hash, deriveTransfer, prettyPins) {
    const once=(s,a,b)=>{if(s.split(a).length!==2)throw new Error("Missing or ambiguous complete-source fragment: "+a.slice(0,100));return s.replace(a,b);};
    const body=(s,n)=>{const at=s.indexOf("def "+n+"(");if(at<0)throw new Error("Missing function "+n);const tail=s.slice(at);const matches=[...tail.matchAll(/\n(?=def |if __name__)/g)];return (matches.length?tail.slice(0,matches[0].index):tail).trimEnd()+"\n";};
    const functionBodies=s=>[...s.matchAll(/^def ([A-Za-z_]\w*)\(/gm)].map(m=>[m[1],body(s,m[1])]);
    const assign=(s,k,v)=>{const match=s.match(new RegExp("^"+k+" = .+$","m"));if(!match)throw new Error("Missing assignment "+k);return once(s,match[0],k+" = '"+v+"'");};
    const replacement=(s,pairs)=>{for(const[a,b]of pairs)s=s.split(a).join(b);return s;};
    const normalSchema="complete-frequency-refined-public-reference-analytic-frame-normal-plane-SO3-v1";
    const baseSchema="complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1";
    const inputSchema="frequency-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1";
    const qSchema="frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1";
    const snapshot="actual-frequency-refined-public-reference-analytic-frame-snapshot-v1";
    const result={};
    for(const n of ["so3_frequency_refinement_layout.py","so3_frequency_refined_smooth_triangle_meridian_operator.py","frequency_refined_smooth_triangle_literal_zero_moment_input.py"])result[n]=input[n];
    const pairs=[
        ["1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529",hash(result["so3_frequency_refined_smooth_triangle_meridian_operator.py"])],
        ["a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d",hash(result["frequency_refined_smooth_triangle_literal_zero_moment_input.py"])],
        ["complete-angular-refined-supported-smooth-triangle-reference-so3-meridian-v1",baseSchema],
        ["complete-angular-refined-public-reference-analytic-frame-normal-plane-SO3-v1",normalSchema],
        ["angular-refined-supported-smooth-triangle-literal-Q-input-v1",inputSchema]
    ];
    for(const stem of ["stage_jacobian","normal_frame","frame_c1","stage_matrices","adjacent_matrices"]) {
        const oldName="angular_refined_public_reference_"+stem+".py";
        const newName="frequency_refined_public_reference_"+stem+".py";
        result[newName]=replacement(input[oldName],pairs);
        pairs.push([hash(input[oldName]),hash(result[newName])]);
    }
    result["frequency_refined_public_reference_calibration.py"]=assign(
        input["reference_centred_frequency_refined_smooth_triangle_calibration.py"],"ENDPOINT_SCHEMA",normalSchema);
    pairs.push(["dffb102d4daed36735a34f69e920c10fc41f5e8fb2aa606a0d86acda9cf6eeb9",hash(result["frequency_refined_public_reference_calibration.py"])]);
    let normal=replacement(input["so3_angular_refined_public_reference_normal_lift.py"],pairs);
    const chartAt=normal.indexOf("    def _chart("),chartEnd=normal.indexOf("\n    def ",chartAt+8);
    if(chartAt<0||chartEnd<0)throw new Error("Complete chart method missing");
    normal=normal.slice(0,chartAt)+normal.slice(chartAt,chartEnd).split("self.freq").join("self.reference_freq")+normal.slice(chartEnd);
    result["so3_frequency_refined_public_reference_normal_lift.py"]=normal;
    pairs.push(["ceaaab5f05c9faaddaff8174be9f97e9aa5b0936b9cf586990877433a9cce100",hash(normal)]);
    result["immutable_frequency_refined_public_reference_root_packets.py"]=replacement(input["immutable_angular_refined_public_reference_root_packets.py"],pairs)
        .split("immutable-angular-refined-public-reference-analytic-frame-root-packets-v1").join("immutable-frequency-refined-public-reference-analytic-frame-root-packets-v1");
    let binding=replacement(input["angular_refined_public_reference_source_binding.py"],pairs)
        .split("angular_refined_public_reference").join("frequency_refined_public_reference")
        .split("complete-public09-angular-refined-analytic-frame-source-model-binding-v1").join("complete-public09-frequency-refined-analytic-frame-source-model-binding-v1")
        .split("actual-angular-refined-public-reference-analytic-frame-snapshot-v1").join(snapshot);
    const start=binding.indexOf("def _bound_module("),end=binding.indexOf("def read_actual(",start);
    if(start<0||end<0)throw new Error("Complete binding construction interval absent");
    binding=binding.slice(0,start)+functionBodies(template["public_reference_frequency_binding_additions.py"]).map(x=>x[1].trimEnd()).join("\n\n")+"\n\n"+binding.slice(end);
    binding=once(binding,"    _observer(directory).validate_base_model(model['base_complete_model'])",
        "    _layout(directory).validate_base_model(model['base_complete_model'],expected_base_source_sha256=BASE_SOURCE_SHA256)");
    binding=once(binding,"angular_observation=angular_observation_binding","frequency_refinement=frequency_refinement_binding");
    result["frequency_refined_public_reference_source_binding.py"]=binding;
    const transferFunctions=Object.fromEntries(functionBodies(template["public_reference_frequency_transfer_additions.py"]));
    result["frequency_refined_public_reference_history_transfer.py"]=deriveTransfer(
        input["transfer_run09_public_reference_analytic_frame_memory.py"],transferFunctions,hash(binding));
    const names={meridian:"so3_frequency_refined_smooth_triangle_meridian_operator.py",
        new_moment_input:"frequency_refined_smooth_triangle_literal_zero_moment_input.py",
        frequency_layout:"so3_frequency_refinement_layout.py",
        analytic_J3:"frequency_refined_public_reference_stage_jacobian.py",
        analytic_frame:"frequency_refined_public_reference_normal_frame.py",
        frame_C1:"frequency_refined_public_reference_frame_c1.py",
        stage_matrices:"frequency_refined_public_reference_stage_matrices.py",
        adjacent_matrices:"frequency_refined_public_reference_adjacent_matrices.py",
        reference_calibration:"frequency_refined_public_reference_calibration.py",
        endpoint:"so3_frequency_refined_public_reference_normal_lift.py",
        root_packets:"immutable_frequency_refined_public_reference_root_packets.py",
        envelope_transfer:"frequency_refined_public_reference_history_transfer.py",
        analytic_J3_binding:"frequency_refined_public_reference_source_binding.py",
        geometry:"so3_frequency_refined_public_reference_envelope_geometry.py"};
    const parent=input["fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py"];
    const table=parent.slice(parent.indexOf("SOURCE_PINS = ")+14,parent.indexOf("\n\nROOT_SNAPSHOT_SCHEMA"));
    const originals=JSON.parse(table.replace(/\(/g,"[").replace(/\)/g,"]"));
    const upperPairs=[
        ["complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1",baseSchema],
        ["complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1",normalSchema],
        ["supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1",inputSchema],
        ["supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1",qSchema],
        ["actual-reference-centred-analytic-frame-normal-current-point-snapshot-v1",snapshot]];
    for(const[role,name]of Object.entries(names))if(role!=="geometry"&&originals[role])upperPairs.push(
        [originals[role][1],hash(result[name])],[originals[role][0].split("/").pop(),name]);
    const geoName=names.geometry;
    result[geoName]=assign(replacement(input["so3_run09_public_reference_analytic_frame_geometry_v2.py"],upperPairs),"SCHEMA",
        "complete-public09-frequency-refined-analytic-frame-envelope-world-geometry-v1");
    if(!result[geoName].includes("policy.get('source_sha256') != '"+hash(result[names.frame_C1])+"'")
            ||!result[geoName].includes("adjacent.definition.get('all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained')"))
        throw new Error("Current C1/selected-J3 complete literal guard is missing");
    const pins=JSON.parse(JSON.stringify(originals));
    for(const[role,name]of Object.entries(names)){
        if(originals[role])pins["frequency_parent_"+role]=originals[role];
        pins[role]=["scripts/resume_20261126/"+name,hash(result[name])];
    }
    pins.frequency_parent_driver=["scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py",hash(parent)];
    pins.frequency_parent_reader=["scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py",
        hash(input["read_run09_public_reference_analytic_frame_so3_report_v2.py"])];
    const schema="complete-public09-M320-analytic-frame-material-envelope-SO3-QP-v1";
    const driverName="fullclosed_frequency_refined_public_reference_so3_qp.py";
    const checks="    if (a.material_envelope_binding is None or a.normal_stages!=32 or a.integration_order!=8\n            or a.current_modes!=320 or a.angles!=2048):\n        raise ValueError('M-only inclusion retains the full actual target, all 32 stages, N2048 and eight radial Gauss nodes')\n";
    let driver=assign(replacement(parent,upperPairs),"SCHEMA",schema);
    const a=driver.indexOf("SOURCE_PINS = "),b=driver.indexOf("\n\nROOT_SNAPSHOT_SCHEMA",a);
    driver=driver.slice(0,a)+"SOURCE_PINS = "+prettyPins(pins)+driver.slice(b);
    driver=once(driver,"    p.add_argument('--angles', type=int, default=2048)",
        "    p.add_argument('--angles', type=int, default=2048)\n    p.add_argument('--current-modes', type=int, default=320)");
    driver=once(driver,"    a.manifest = [path.resolve() for path in a.manifest]",checks+"    a.manifest = [path.resolve() for path in a.manifest]");
    driver=once(driver,"    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])",
        "    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])\n    frequency_layout = load('_complete_actual_frequency_layout',paths['frequency_layout'])");
    driver=once(driver,"seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean)",
        "seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean,\n        current_modes=args.current_modes,frequency_layout_module=frequency_layout)");
    driver=once(driver,"    if prior_final_point is not None:\n        x = prior_final_point\n",
        "    if prior_final_point is not None:\n        x = prior_final_point\n    frequency_record=envelope_transfer.frequency_initial_record(args,q,x,\n        transfer_record=envelope_transfer_record,seed_record=prior_final_seed)\n");
    driver=once(driver,"        representation=q.model, coordinate_norm=coordinates.record,",
        "        representation=q.model, coordinate_norm=coordinates.record,\n        frequency_refinement=frequency_record,reference_M=160,current_M=320,\n        frequency_layout_definition=base.frequency_layout_definition,\n        frequency_layout_identity_sha256=base.model['frequency_layout_identity_sha256'],\n        frequency_layout_source=file_record(paths['frequency_layout']),\n        radial_observation_refinement_performed=False,angular_observation_refinement_performed=False,\n        full_fixed_reference_target_unchanged=True,saved_parent_Phi_used_as_current_baseline=False,");
    const scienceMarker="    def save_report():";
    if(driver.slice(driver.indexOf(scienceMarker))!==parent.slice(parent.indexOf(scienceMarker)))
        throw new Error("The complete scientific suffix must remain byte-identical");
    result[driverName]=driver;
    let launcher=assign(replacement(input["launch_run09_public_reference_analytic_frame_actions_v2.py"],upperPairs),"DRIVER_SHA",hash(driver));
    launcher=launcher.split("fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py").join(driverName);
    launcher=once(launcher,"    p.add_argument('--angles', type=int, default=2048)",
        "    p.add_argument('--angles', type=int, default=2048)\n    p.add_argument('--current-modes', type=int, default=320)");
    launcher=once(launcher,"    a.manifest = [path.resolve() for path in a.manifest]",checks+"    a.manifest = [path.resolve() for path in a.manifest]");
    launcher=once(launcher,"        fixed_supported_unit_seed=True,",
        "        fixed_supported_unit_seed=True,reference_M=160,current_M=args.current_modes,\n        every_original_free_word_retained_with_correct_three_block_zero_inclusion=True,\n        original_reference_M160_chart_and_N2048_radial_observer_retained=True,");
    result["launch_frequency_refined_public_reference_so3_actions.py"]=launcher;
    let reader=assign(replacement(input["read_run09_public_reference_analytic_frame_so3_report_v2.py"],upperPairs),"DRIVER_SHA",hash(driver));
    reader=assign(reader,"REPORT_SCHEMA",schema).split("fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py").join(driverName);
    reader=once(reader,"                    'all_original_outer_free_variables_and_norm_layout_unchanged'))",
        "                    'all_original_outer_free_variables_retained_and_new_modes_added',\n                    'frozen_reference_layout_unchanged','current_norm_layout_changed'))");
    result["read_frequency_refined_public_reference_so3_report.py"]=reader;
    return {sources:result,sourcePins:pins};
}

const STATIC_CHECK = String.raw`
import ast,json,pathlib,sys
directory=pathlib.Path(sys.argv[1])
names=json.loads(sys.argv[2])
checked=[]
for name in names:
    source=(directory/name).read_text()
    tree=ast.parse(source,filename=name)
    compile(source,name,'exec')
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            keys=[]
            for key in node.keys:
                if isinstance(key,ast.Constant) and isinstance(key.value,(str,int,float,bytes)):
                    if key.value in keys:raise ValueError('Duplicate literal dictionary key '+name+' '+repr(key.value))
                    keys.append(key.value)
        if isinstance(node,ast.Call):
            keys=[v.arg for v in node.keywords if v.arg is not None]
            if len(keys)!=len(set(keys)):raise ValueError('Duplicate keyword '+name)
    if any(line.rstrip()!=line for line in source.splitlines()):
        raise ValueError('Trailing whitespace '+name)
    checked.append(name)
print(json.dumps(dict(complete_sources=checked,scientific_imports=False,scientific_execution=False)))
`;

function main(argv) {
    const options={};
    for(let i=0;i<argv.length;i++) {
        const a=argv[i];
        if(a==='--help') {
            process.stdout.write('Usage: node reproduce_public_reference_frequency_sources.mjs --source-directory DIR --output-directory DIR [--template-directory DIR] [--verify-existing] [--python-executable python3]\n');
            return;
        }
        if(a==='--verify-existing') {if(options.verify)throw new Error('Repeated option');options.verify=true;continue;}
        const key={'--source-directory':'sources','--output-directory':'output','--template-directory':'templates','--python-executable':'python'}[a];
        if(!key||options[key]!==undefined||i+1===argv.length)throw new Error('Unknown, repeated or incomplete option '+a);
        options[key]=argv[++i];
    }
    if(!options.sources||!options.output)throw new Error('Both complete source and output directories are required');
    options.sources=path.resolve(options.sources);
    options.output=path.resolve(options.output);
    options.templates=path.resolve(options.templates||path.dirname(fileURLToPath(import.meta.url)));
    const input={},templates={};
    for(const[n,pin]of Object.entries(INPUTS))input[n]=checkedText(path.join(options.sources,n),pin);
    for(const[n,pin]of Object.entries(TEMPLATES))templates[n]=checkedText(path.join(options.templates,n),pin);
    const result=deriveFrequencyPackage(input,templates,sha,deriveMTransfer,prettyPins);
    if(JSON.stringify(Object.keys(result.sources).sort())!==JSON.stringify(Object.keys(OUTPUTS).sort()))
        throw new Error('The complete 17-file result set changed');
    for(const[n,s]of Object.entries(result.sources)) {
        if(Buffer.byteLength(s,'utf8')!==OUTPUTS[n].bytes||sha(s)!==OUTPUTS[n].sha256)
            throw new Error('Complete source reconstruction differs: '+n);
        if(Buffer.byteLength(s,'utf8')>=100000)throw new Error('Keep each whole source below 100 KB');
    }
    const roleChecks={};
    for(const[role,[relative,digest]]of Object.entries(result.sourcePins)) {
        const basename=path.basename(relative);
        const text=result.sources[basename]??fs.readFileSync(path.join(options.sources,basename),'utf8');
        if(sha(text)!==digest)throw new Error('The complete actual role differs: '+role);
        roleChecks[role]={relative_path:relative,sha256:digest,bytes:Buffer.byteLength(text,'utf8')};
    }
    if(Object.keys(roleChecks).length!==74)throw new Error('All 74 source roles are required');
    if(options.verify) {
        for(const[n,s]of Object.entries(result.sources)) {
            const actual=checkedText(path.join(options.output,n),OUTPUTS[n]);
            if(actual!==s)throw new Error('Existing complete source differs: '+n);
        }
    } else {
        fs.mkdirSync(options.output,{recursive:true});
        for(const[n,s]of Object.entries(result.sources))fs.writeFileSync(path.join(options.output,n),s,'utf8');
    }
    let staticCheck=null;
    if(options.python) {
        const child=spawnSync(options.python,['-c',STATIC_CHECK,options.output,JSON.stringify(Object.keys(OUTPUTS).sort())],{encoding:'utf8'});
        if(child.error)throw child.error;
        if(child.status!==0)throw new Error('Actual stdlib AST/compile failed: '+child.stderr);
        staticCheck=JSON.parse(child.stdout);
    }
    process.stdout.write(JSON.stringify({
        schema:'complete-public09-M320-source-only-reconstruction-v2',
        complete_sources:OUTPUTS,complete_source_roles:roleChecks,source_roles:Object.keys(roleChecks).length,
        every_runtime_byte_equals_pre_loss_locked_candidate:true,
        fixed_reference_M:160,current_M:320,full_N:2048,radial_nodes:923,integration_order:8,normal_stages:32,
        AST_compile_result:staticCheck,scientific_module_imports:false,scientific_execution:false,
        verification_only:Boolean(options.verify)
    },null,2)+'\n');
}
main(process.argv.slice(2));
