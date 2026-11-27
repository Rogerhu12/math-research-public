#!/usr/bin/env node
/**
 * Complete source/parameter-only actual09 M160 -> M320 plans.
 * All parent numerical arguments, outputs, cleanup rules and 333/317 scalar
 * selectors are copied before the explicit source/layout/input-mode changes.
 * No future report, final point or scientific value is supplied.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const PARENT = {name:'run09-public-reference-analytic-frame-v2-complete-ready.json',bytes:93108,
    sha256:'2ea114b413037b9c54508d4fbf21423abefee7dc73c69a54efc57259aecb1a9f'};
const RUNTIME = {
  "frequency_refined_public_reference_adjacent_matrices.py": {
    "bytes": 36761,
    "sha256": "610805744bdb5f4826d0c3a63bb769c9744639734db232ec31b3dbeaa0f89569"
  },
  "frequency_refined_public_reference_calibration.py": {
    "bytes": 12345,
    "sha256": "b72572b13f94bf5482ced96c06aa940b5097ace270c159ec1837495519d9387a"
  },
  "frequency_refined_public_reference_frame_c1.py": {
    "bytes": 35894,
    "sha256": "f272aaa95e63867d18015d9e92fa321f36785459377433a4433382794ae9c15a"
  },
  "frequency_refined_public_reference_history_transfer.py": {
    "bytes": 82084,
    "sha256": "fdc29a36ca562cec8327a2ca250ecdd3a505827415617255993b6fcab5389279"
  },
  "frequency_refined_public_reference_normal_frame.py": {
    "bytes": 33671,
    "sha256": "787825f17de647598099fe7b4cbfc3d82b6ad90eac9943de6b67f653f092520a"
  },
  "frequency_refined_public_reference_source_binding.py": {
    "bytes": 34116,
    "sha256": "a62e122d32b5a8faa7e1dee82e8f8855c40c1f2d8a1bceeb14a298a6512ba931"
  },
  "frequency_refined_public_reference_stage_jacobian.py": {
    "bytes": 24227,
    "sha256": "2655c90ce07233cb3eb55ed64fa5702442ae0daaf5cafed53571afe35f5fbfa2"
  },
  "frequency_refined_public_reference_stage_matrices.py": {
    "bytes": 47775,
    "sha256": "d7a6ebc317637667a18b8fb58ac8717aba8cbada981a349027bcaa60b448e4b7"
  },
  "frequency_refined_smooth_triangle_literal_zero_moment_input.py": {
    "bytes": 31068,
    "sha256": "bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971"
  },
  "fullclosed_frequency_refined_public_reference_so3_qp.py": {
    "bytes": 86793,
    "sha256": "0dc3bbb46df6168f3f3130bb9009ee4cd94845f455926ba036ba987a79c8cc41"
  },
  "immutable_frequency_refined_public_reference_root_packets.py": {
    "bytes": 69734,
    "sha256": "4b352626ed6f306bcdb1dc0126131c8f9fb4ab3d081376ae70739ec7c9d752f9"
  },
  "launch_frequency_refined_public_reference_so3_actions.py": {
    "bytes": 21902,
    "sha256": "55fbc4900dd0b049b11e4ecfa1aba642daf39a85241f0b1cb4283cf657506e03"
  },
  "read_frequency_refined_public_reference_so3_report.py": {
    "bytes": 97436,
    "sha256": "f56c4f81037fa9d54edcdc566552c8eefb79cb372920419ed7e81fcf1b5aaf2e"
  },
  "so3_frequency_refined_public_reference_envelope_geometry.py": {
    "bytes": 68931,
    "sha256": "be23caab6ba3b62bf02129f5da5043dffe6fe4d51b394590f16400a61dbf1de6"
  },
  "so3_frequency_refined_public_reference_normal_lift.py": {
    "bytes": 96556,
    "sha256": "014fd521d315db223590d45b9b4d4da4e09975036044e533f601dcab636731d9"
  },
  "so3_frequency_refined_smooth_triangle_meridian_operator.py": {
    "bytes": 42982,
    "sha256": "41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2"
  },
  "so3_frequency_refinement_layout.py": {
    "bytes": 13582,
    "sha256": "ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27"
  }
};
const CONSTRUCTION = {
  "public_reference_frequency_binding_additions.py": {
    "bytes": 13252,
    "sha256": "834bf1838c22ef9b16a2e9668b9656051fce347df7f928d0a4b1f25dc11fede0"
  },
  "public_reference_frequency_transfer_additions.py": {
    "bytes": 30194,
    "sha256": "efa48beb6672a6ad84e16de9c406cdc9e20b02aaed8a074af1a28f85870b1170"
  },
  "reproduce_public_reference_frequency_sources.mjs": {
    "bytes": 36620,
    "sha256": "1e9178bcf907f63ecaba249adc6d4ae226b12351fc97db4c30ce4a8800e1a4d8"
  }
};

function bytesRecord(bytes) {
    return {bytes:bytes.length,sha256:crypto.createHash('sha256').update(bytes).digest('hex')};
}
function checkedFile(filename,expected) {
    const bytes=fs.readFileSync(filename),actual=bytesRecord(bytes);
    if(actual.bytes!==expected.bytes||actual.sha256!==expected.sha256)throw new Error('Changed complete input '+filename);
    const text=bytes.toString('utf8');
    if(!Buffer.from(text,'utf8').equals(bytes))throw new Error('Whole input is not canonical UTF-8 '+filename);
    return text;
}
function buildFrequencyReady(original,runtime,pins,constructors,kind) {
    const clone=x=>JSON.parse(JSON.stringify(x));
    if(!["independent","terminal","final"].includes(kind))throw new Error("Invalid complete input mode");
    if(original.fixed_target.identity_sha256!=="7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a" ||
        original.fixed_target.whole_actual_binding_sha256!=="2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d")
        throw new Error("The entire actual09 target and whole input binding must be retained");
    const parentDriver="ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5";
    const parentReader="aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32";
    const parentName="run09-public-reference-analytic-frame-v2-complete-ready.json";
    const parentSource={path:"computations/"+parentName,bytes:93108,sha256:"2ea114b413037b9c54508d4fbf21423abefee7dc73c69a54efc57259aecb1a9f"};
    const olddir="run09-public-reference-analytic-frame-v2-first";
    const newdir={independent:"run09-frequency-M320-analytic-frame-v2-independent",
        terminal:"run09-frequency-M320-analytic-frame-v2-from-terminal-history",
        final:"run09-frequency-M320-analytic-frame-v2-from-complete-final"}[kind];
    const steps=clone(original.steps);
    const replace=s=>s.split(olddir).join(newdir);
    for(let i=0;i<steps.length;i++) {
        const step=steps[i];
        step.id=(i===0?"complete-":"actual-")+newdir+"-20261127";
        step.script="topics/visible-flex-larger-amplitude/scripts/resume_20261126/"+
            (i===0?"launch_frequency_refined_public_reference_so3_actions.py":"read_frequency_refined_public_reference_so3_report.py");
        step.args=step.args.map(replace);
        step.outputs=step.outputs.map(replace);
        step.summary=Object.fromEntries(Object.entries(step.summary).map(([k,v])=>[replace(k),v]));
        if(step.cleanup_generated_patterns)step.cleanup_generated_patterns=step.cleanup_generated_patterns.map(replace);
        step.scope=i===0
            ? "Complete current M320/free SO3 expansion of the entire actual09 fixed target. Frozen reference M160/N2048/J923, full scalar/chart/seed, eight radial Gauss nodes, all 32 normal stages, analytic frame/J3, all complete sixjets, original geometry/Phase I/typed rows and immutable root-packet hooks remain. Original three SO3 blocks are embedded separately; every new mode is free. All current field values and finite objective are reread."
            : "Pure complete-source/actual09-target/74-role/history/packet/M320 binding. Original reference parent keeps initial failures readable. No F/J/root/integral or packet upgrade.";
    }
    steps[0].args.push("--current-modes","320");
    const parentReport="{work}/"+olddir+"/report.json",parentFinal="{work}/"+olddir+"/final-new-field.npz";
    if(kind!=="independent") {
        const args=steps[0].args,kept=[];
        for(let i=0;i<args.length;i++) {
            if(args[i]==="--independent-envelope-branch")continue;
            if(args[i]==="--pending-parallel-envelope-run"||args[i]==="--pending-parallel-envelope-source"){i++;continue;}
            kept.push(args[i]);
        }
        steps[0].args=kept;
        steps[0].args.push("--material-envelope-parent-report",parentReport);
        if(kind==="final") {
            steps[0].args.push("--material-envelope-seed-report",parentReport,"--material-envelope-seed-checkpoint",parentFinal);
            steps[0].parent_bundle=olddir+"/final-new-field.npz";
        }
    } else {
        steps[0].args.push("--pending-parallel-envelope-run","45943410994/1","--pending-parallel-envelope-source","45943410994/1="+parentDriver);
    }
    if(steps[1].parent_bundle!=="axisymmetric-R690-reference-v2-first/reference.npz")throw new Error("The pure reader must not require an unreturned new final");
    const science=Object.values(steps[0].summary)[0];
    Object.assign(science,{
        reference_M:"reference_M",current_M:"current_M",
        same_full_fixed_reference_target:"full_fixed_reference_target_unchanged",
        radial_observation_refinement:"radial_observation_refinement_performed",
        angular_observation_refinement:"angular_observation_refinement_performed",
        old_parent_Phi_inherited:"saved_parent_Phi_used_as_current_baseline",
        frequency_layout_identity:"frequency_layout_identity_sha256",
        frequency_input_mode:"frequency_refinement.mode",
        frequency_initial_point:"frequency_refinement.current_full_point_sha256",
        original_frozen_point:"frequency_refinement.frozen_original_point_relation.original_full_point_sha256",
        current_frozen_point:"frequency_refinement.frozen_original_point_relation.current_full_point_sha256"
    });
    const pure=Object.values(steps[1].summary)[0];
    for(const[name,key]of Object.entries({
        reference_M:"reference_M",current_M:"current_M",frequency_input_mode:"mode",
        frequency_layout_identity:"layout_identity_sha256",frequency_initial_point:"actual_initial_full_point_sha256",
        frequency_old_values_or_certificates_inherited:"old_field_values_or_certificates_inherited"
    }))pure[name]="analytic_stage_jacobian.frequency_refinement."+key;
    if(Object.keys(runtime).length!==17||Object.keys(pins).length!==74)throw new Error("Use all 17 whole runtime sources and all 74 roles");
    const result=clone(original);
    Object.assign(result,{
        schema:"complete-actual-public09-analytic-frame-M320-parameter-plan-v2",
        executed:false,queued:false,complete_source_and_parameter_closure:true,
        scope:"M160 to M320 current free Fourier space of the entire actually frozen run09 target. Frozen reference M160, full 160-word material chart, scalar parameters and exact nodes, N2048/513 quarter observer, J923 mesh, eight radial Gauss nodes and common 32-stage normal chain are retained. New current norm is rebuilt; no old finite Phi, field values, roots or certificates are inherited.",
        source_sha256:Object.fromEntries(Object.entries(runtime).map(([n,r])=>[n,r.sha256])),
        runtime_source_roles:clone(pins),
        complete_source_constructors:clone(constructors),
        complete_parent_ready:parentSource,
        complete_source_reproducer:{name:"reproduce_public_reference_frequency_sources.mjs",...constructors["reproduce_public_reference_frequency_sources.mjs"],
            complete_output_source_count:17,complete_actual_source_roles:74},
        complete_numeric_parameter_provenance:{
            all_original_numeric_solver_and_observation_parameters_retained:true,
            numerical_argument_changes:[],new_explicit_layout_argument:{option:"--current-modes",value:"320"},
            reference_M:160,current_M:320,full_N:2048,J:923,
            directions:1,maxiter:16,restoration_directions:4,restoration_maxiter:64,
            normal_stages:32,outer_radial_Gauss_order:8,seed_radial_Gauss_order:8,
            parent_science_words:original.steps[0].args.length,current_science_words:steps[0].args.length,
            parent_pure_words:original.steps[1].args.length,current_pure_words:steps[1].args.length,
            original_all_science_summary_selectors_retained:true,original_all_pure_summary_selectors_retained:true,
            science_summary_count:Object.keys(science).length,pure_summary_count:Object.keys(pure).length},
        complete_scientific_suffix:{
            original_sha256:"d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376",
            entire_save_report_through_EOF_byte_identical:true,
            both_original_record_only_packet_hooks_retained:true,
            original_Phase_I_QP_all_rows_all_trial_screens_retained:true},
        independent_branch:{
            mode:kind,actual_parent_source:parentDriver,actual_parent_reader:parentReader,
            complete_M160_parent_terminal_required:kind!=="independent",
            complete_actual_final_required:kind==="final",
            complete_parent_report:kind!=="independent"?parentReport:null,
            complete_parent_final:kind==="final"?parentFinal:null,
            actual_parent_report_sha256:null,actual_parent_final_sha256:null,
            actual_parent_field_has_not_been_fabricated:true,
            all_old_literal_addresses_and_uncapped_typed_lineage_transferred:true,
            original_three_rotation_blocks_copied_separately_and_new_modes_zero_on_injection:true,
            frozen_reference_seed_not_reselected_from_parent_final:true,
            original_reference_initial_point_used:kind!=="final",
            all_current_initial_values_roots_geometry_and_finite_Phi_reread:true},
        source_only_checks:{
            all_74_whole_runtime_source_roles_verified_before_executor_loss:true,
            all_17_runtime_AST_compile_and_complete_reproduction_passed_before_executor_loss:true,
            actual_three_launcher_print_commands_and_reader_help_passed_before_executor_loss:true,
            all_17_runtime_cloud_text_reconstruction_equals_exact_pre_loss_SHA:true,
            complete_cloud_text_constructor_replay_performed:true,
            cloud_constructor_Node_CLI_AST_or_compile_not_claimed:true,
            selected_adjacent_guard_matches_actual_definition:true,
            current_geometry_C1_guard_matches_own_complete_helper:true,
            scientific_imports_or_F_J_root_or_fixtures_executed_locally:false},
        actual_future_definition_or_field_sha256:null,
        actual_parent_run_status_note:"Actual e3cb setup failed before report at an adjacent-policy getter: all_original was absent while the selected analytic-J3 source declares all_selected. The actual full child log is 6387 bytes, SHA256 33671079a8ece2456621239ad80e51b7b8e3ff91aa3116b016391780319671de. This family binds repaired ff544/aee22 sources; no future terminal or final is fabricated.",
        limitations:"No local science, accepted M320 field, root existence/uniqueness or inverse-error certificate, continuous geometry certificate, radial/N refinement, cross-run target equivalence, floating bitwise preservation after changing M, or measured performance improvement is claimed.",
        steps
    });
    result.actual_failure_and_exact_repair={
        complete_evidence_source:parentSource,complete_evidence_field:"actual_failure_and_exact_repair",
        actual_log_bytes:6387,actual_log_sha256:"33671079a8ece2456621239ad80e51b7b8e3ff91aa3116b016391780319671de",
        missing_key:"all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained",
        actual_key:"all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained",
        old_science_report_produced:false,old_pure_readout_produced:false,repaired_scientific_success_inferred:false};
    Object.assign(result.unreturned_peer_evidence["45909290354/1"],{
        actual_API_observation_time_UTC:"2026-11-27T05:02:15Z",actual_API_updated_at_UTC:"2026-11-27T05:00:28Z",
        scientific_child_termination_time_UTC:null,scientific_child_termination_cause:null,
        observation_time_is_not_scientific_child_end_time:true});
    if(kind==="independent")result.unreturned_peer_evidence["45943410994/1"]={
        driver_sha256:parentDriver,repaired_parent_terminal_report_consumed:false,
        complete_terminal_field_or_typed_state_read:false,prior_e3cb_attempt_report_absent:true,
        actual_unpaid_provenance_obligation_retained:true,unknown_is_not_empty:true};
    for(let i=0;i<2;i++)for(const[k,v]of Object.entries(Object.values(original.steps[i].summary)[0]))
        if(Object.values(steps[i].summary)[0][k]!==v)throw new Error("Original scalar selector removed or reinterpreted: "+k);
    if(Object.keys(science).length!==344||Object.keys(pure).length!==323)throw new Error("Retain all 333/317 original selectors plus exactly 11/6 actual new scalars");
    if(steps[0].args[steps[0].args.indexOf("--angles")+1]!=="2048")throw new Error("M-only expansion cannot change N");
    if(steps[0].args.length!=={independent:151,terminal:140,final:144}[kind]||steps[1].args.length!==7)
        throw new Error("The complete parameter lengths changed");
    return result;
}

function main(argv) {
    const opt={};
    for(let i=0;i<argv.length;i++) {
        const arg=argv[i];
        if(arg==='--help') {
            process.stdout.write('Usage: node make_public_reference_frequency_ready.mjs --parent-ready FILE --generated-directory DIR --output-directory DIR [--construction-directory DIR] [--verify-existing]\n');
            return;
        }
        if(arg==='--verify-existing'){if(opt.verify)throw new Error('Repeated option');opt.verify=true;continue;}
        const key={'--parent-ready':'parent','--generated-directory':'generated','--construction-directory':'construction','--output-directory':'output'}[arg];
        if(!key||opt[key]!==undefined||i+1===argv.length)throw new Error('Unknown, repeated or incomplete option '+arg);
        opt[key]=argv[++i];
    }
    if(!opt.parent||!opt.generated||!opt.output)throw new Error('Complete parent/generated/output paths are required');
    opt.parent=path.resolve(opt.parent);opt.generated=path.resolve(opt.generated);opt.output=path.resolve(opt.output);
    opt.construction=path.resolve(opt.construction||path.dirname(fileURLToPath(import.meta.url)));
    const original=JSON.parse(checkedFile(opt.parent,PARENT));
    const texts={};
    for(const[n,pin]of Object.entries(RUNTIME))texts[n]=checkedFile(path.join(opt.generated,n),pin);
    const constructors={};
    for(const[n,pin]of Object.entries(CONSTRUCTION)) {
        checkedFile(path.join(opt.construction,n),pin);
        constructors[n]={...pin};
    }
    const self=fileURLToPath(import.meta.url);
    const selfName='make_public_reference_frequency_ready.mjs';
    if(path.basename(self)!==selfName)throw new Error('Keep the complete constructor filename');
    constructors[selfName]=bytesRecord(fs.readFileSync(self));
    const driver=texts['fullclosed_frequency_refined_public_reference_so3_qp.py'];
    const start=driver.indexOf('SOURCE_PINS = '),end=driver.indexOf('\n\nROOT_SNAPSHOT_SCHEMA',start);
    if(start<0||end<0)throw new Error('The complete source-role table is absent');
    const pins={};
    for(const m of driver.slice(start,end).matchAll(/'([^']+)': \('([^']+)',\s*'([0-9a-f]{64})'\)/g)) {
        if(pins[m[1]])throw new Error('Repeated role');
        pins[m[1]]=[m[2],m[3]];
    }
    if(Object.keys(pins).length!==74)throw new Error('Retain all 74 declared complete source roles');
    const outputs={};
    if(!opt.verify)fs.mkdirSync(opt.output,{recursive:true});
    for(const kind of ['independent','terminal','final']) {
        const value=buildFrequencyReady(original,RUNTIME,pins,constructors,kind);
        const text=JSON.stringify(value)+'\n',bytes=Buffer.from(text,'utf8');
        if(bytes.length>=100000||Buffer.byteLength(JSON.stringify(value.steps),'utf8')>=95000)
            throw new Error('The complete plan/queue exceeds the published size limit');
        const name='public09-frequency-M320-analytic-frame-v2-'+kind+'-ready.json';
        if(opt.verify) {
            if(fs.readFileSync(path.join(opt.output,name),'utf8')!==text)throw new Error('Existing complete plan differs '+name);
        } else fs.writeFileSync(path.join(opt.output,name),bytes);
        outputs[name]={...bytesRecord(bytes),science_arguments:value.steps[0].args.length,
            pure_arguments:value.steps[1].args.length,science_scalar_selectors:344,pure_scalar_selectors:323,
            compact_two_step_queue_bytes:Buffer.byteLength(JSON.stringify(value.steps),'utf8')};
    }
    process.stdout.write(JSON.stringify({schema:'complete-public09-M320-ready-source-reconstruction-v2',
        outputs,source_and_parameter_only:true,scientific_execution:false,verification_only:Boolean(opt.verify)},null,2)+'\n');
}
main(process.argv.slice(2));
