#!/usr/bin/env node
// Complete source-only reproduction. No scientific imports or evaluation.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const PRIMITIVES = [
 {
  "name": "radial_bisection_layout.py",
  "bytes": 18923,
  "sha256": "cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744"
 },
 {
  "name": "exact_affine_supported_reference.py",
  "bytes": 23435,
  "sha256": "2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117"
 },
 {
  "name": "complete_dyadic_radial_observations.py",
  "bytes": 28167,
  "sha256": "2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74"
 },
 {
  "name": "radial_material_address_transfer.py",
  "bytes": 22097,
  "sha256": "6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716"
 }
];
const CONSTRUCTORS = [
 {
  "name": "derive_radial_public_reference_lower.mjs",
  "bytes": 29293,
  "sha256": "5fc01d13c64055222991eb10f84cb940e01ef0c0ba4c79ae6dd37391741f0d90"
 },
 {
  "name": "derive_radial_public_reference_memory_binding.mjs",
  "bytes": 67357,
  "sha256": "5b32bc01adedc3ecc72aa644f949ede1e9f4041f4380bb10bd35d5a11aabf992"
 },
 {
  "name": "derive_radial_public_reference_upper.mjs",
  "bytes": 66189,
  "sha256": "733ba499b0e5f4df80197c80d3cd14477585d68d90762fbb6cd039b988f7e9d9"
 }
];
const SOURCE_PINS = {
 "root_packets": [
  "scripts/resume_20261126/immutable_radial_refined_public_reference_root_packets.py",
  "8d2b93dd055cc600aac14183d060d101421a924590c1fe8300625931bc8c0403"
 ],
 "analytic_parent_stage_matrices": [
  "scripts/resume_20261126/detached_normal_stage_matrix_reuse.py",
  "375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59"
 ],
 "analytic_parent_adjacent_matrices": [
  "scripts/resume_20261126/adjacent_normal_frame_matrices.py",
  "955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3"
 ],
 "analytic_parent_driver": [
  "scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py",
  "95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9"
 ],
 "analytic_parent_reader": [
  "scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py",
  "f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470"
 ],
 "analytic_J3": [
  "scripts/resume_20261126/radial_refined_public_reference_stage_jacobian.py",
  "0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9"
 ],
 "analytic_J3_binding": [
  "scripts/resume_20261126/radial_refined_public_reference_source_binding.py",
  "5b50b02aea139b81e7e1ed3cbf37c4ad8870d182c63d48bf648fb197e1cf3734"
 ],
 "analytic_parent_frame_C1": [
  "scripts/resume_20261126/normal_frame_c1_reuse.py",
  "ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9"
 ],
 "seed_reference": [
  "scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py",
  "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b"
 ],
 "seed_mean": [
  "scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py",
  "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"
 ],
 "reference": [
  "scripts/resume_20261126/so3_axisymmetric_reference.py",
  "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"
 ],
 "warm_producer": [
  "notes/2026-11-17-parallel-model-fullclosed-hold-warm.py",
  "bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3"
 ],
 "observed": [
  "scripts/resume_20261120/gauss_observed_closed_gram.py",
  "26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d"
 ],
 "deep_scalar": [
  "scripts/resume_20261126/deep_valley_tail_input.py",
  "e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"
 ],
 "scalar": [
  "notes/2026-11-17-parallel-model-full-hold-oracle.py",
  "a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670"
 ],
 "integer": [
  "notes/2026-11-17-parallel-inward-integral-enclosure.py",
  "babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0"
 ],
 "hold": [
  "scripts/parallel_20261117_negative_hold_profile_ivp.py",
  "ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1"
 ],
 "meridian": [
  "scripts/resume_20261126/so3_radial_refined_public_reference_meridian_operator.py",
  "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0"
 ],
 "geometry": [
  "scripts/resume_20261126/so3_radial_refined_public_reference_envelope_geometry.py",
  "2fe41a0ecc48d1404973b55dcde4cb4591bc4029fb4158740bbf5369aa869877"
 ],
 "qp": [
  "scripts/resume_20261120/fullspace_feasible_active_cg_v3.py",
  "fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4"
 ],
 "spectral": [
  "scripts/resume_20261120/positive_spectral_gram_weights.py",
  "e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91"
 ],
 "hessian": [
  "scripts/resume_20261120/positive_spectral_gram_hessian.py",
  "29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4"
 ],
 "centered": [
  "scripts/resume_20261126/centered_spectral_statistics.py",
  "5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01"
 ],
 "history": [
  "scripts/resume_20261120/launch_refinement_from_full_report.py",
  "4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60"
 ],
 "pure_geometry": [
  "scripts/resume_20261120_curvature_qp.py",
  "a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854"
 ],
 "geometry_selector": [
  "scripts/resume_20261120/fullclosed_point_inequalities_v2.py",
  "e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8"
 ],
 "endpoint": [
  "scripts/resume_20261126/so3_radial_refined_public_reference_normal_lift.py",
  "8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5"
 ],
 "axisymmetric_seed_driver": [
  "scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py",
  "606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9"
 ],
 "frozen_moment_input": [
  "scripts/resume_20261126/frozen_zero_moment_input.py",
  "4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611"
 ],
 "moment_trace_source": [
  "scripts/resume_20261126/trace_zero_initial_endpoint_failure.py",
  "73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54"
 ],
 "moment_initial_binding": [
  "scripts/resume_20261126/diagnose_zero_initial_chord.py",
  "65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0"
 ],
 "moment_original_endpoint": [
  "scripts/resume_20261126/so3_zero_closure_endpoint_operator.py",
  "5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46"
 ],
 "moment_original_driver": [
  "scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py",
  "b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b"
 ],
 "new_moment_input": [
  "scripts/resume_20261126/radial_refined_public_reference_literal_zero_moment_input.py",
  "59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652"
 ],
 "reference_calibration": [
  "scripts/resume_20261126/radial_refined_public_reference_calibration.py",
  "c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178"
 ],
 "frame_C1": [
  "scripts/resume_20261126/radial_refined_public_reference_frame_c1.py",
  "bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e"
 ],
 "envelope_memory": [
  "scripts/resume_20261126/complete_material_envelope_memory.py",
  "c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152"
 ],
 "envelope_rows": [
  "scripts/resume_20261126/complete_material_envelope_rows.py",
  "729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7"
 ],
 "stage_matrices": [
  "scripts/resume_20261126/radial_refined_public_reference_stage_matrices.py",
  "fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387"
 ],
 "envelope_transfer": [
  "scripts/resume_20261126/radial_refined_public_reference_history_transfer.py",
  "2720bd9033391fc3f0a48afe33f50ea5843b2bf225a6596ee5a5b7077819e55c"
 ],
 "envelope_parent_reader": [
  "scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py",
  "104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7"
 ],
 "envelope_parent_driver": [
  "scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py",
  "cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5"
 ],
 "envelope_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py",
  "a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd"
 ],
 "envelope_parent_calibration": [
  "scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py",
  "3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991"
 ],
 "envelope_parent_geometry": [
  "scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py",
  "bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f"
 ],
 "adjacent_matrices": [
  "scripts/resume_20261126/radial_refined_public_reference_adjacent_matrices.py",
  "3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4"
 ],
 "independent_envelope_memory": [
  "scripts/resume_20261126/radial_refined_public_reference_memory.py",
  "6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a"
 ],
 "independent_input_projection_producer": [
  "scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py",
  "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18"
 ],
 "analytic_frame": [
  "scripts/resume_20261126/radial_refined_public_reference_normal_frame.py",
  "8fb0f326356d8e94337d51bfba85068c5872453df8f08e6619f241dfe7f715ce"
 ],
 "frame_parent_driver": [
  "scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py",
  "0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51"
 ],
 "frame_parent_reader": [
  "scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py",
  "c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e"
 ],
 "frame_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py",
  "04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e"
 ],
 "frame_parent_calibration": [
  "scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py",
  "4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d"
 ],
 "frame_parent_J3": [
  "scripts/resume_20261126/analytic_normal_stage_jacobian.py",
  "64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d"
 ],
 "frame_parent_C1": [
  "scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py",
  "8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8"
 ],
 "frame_parent_stage_matrices": [
  "scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py",
  "5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1"
 ],
 "frame_parent_adjacent_matrices": [
  "scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py",
  "8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787"
 ],
 "actual_public_input_binding": [
  "scripts/resume_20261126/actual_public_reference_input_binding.py",
  "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a"
 ],
 "radial_parent_meridian": [
  "scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py",
  "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"
 ],
 "radial_parent_new_moment_input": [
  "scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py",
  "307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7"
 ],
 "radial_parent_analytic_J3": [
  "scripts/resume_20261126/analytic_frame_local_stage_jacobian.py",
  "894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866"
 ],
 "radial_parent_analytic_frame": [
  "scripts/resume_20261126/analytic_normal_frame_jets.py",
  "4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8"
 ],
 "radial_parent_frame_C1": [
  "scripts/resume_20261126/analytic_frame_c1_reuse.py",
  "f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb"
 ],
 "radial_parent_stage_matrices": [
  "scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py",
  "fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255"
 ],
 "radial_parent_adjacent_matrices": [
  "scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py",
  "3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695"
 ],
 "radial_parent_reference_calibration": [
  "scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py",
  "fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0"
 ],
 "radial_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py",
  "3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc"
 ],
 "radial_parent_root_packets": [
  "scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py",
  "094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0"
 ],
 "radial_parent_envelope_transfer": [
  "scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py",
  "6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707"
 ],
 "radial_parent_analytic_J3_binding": [
  "scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py",
  "15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592"
 ],
 "radial_parent_geometry": [
  "scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py",
  "e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13"
 ],
 "radial_parent_driver": [
  "scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py",
  "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"
 ],
 "radial_parent_reader": [
  "scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py",
  "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32"
 ],
 "radial_layout": [
  "scripts/resume_20261126/radial_bisection_layout.py",
  "cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744"
 ],
 "radial_affine_reference": [
  "scripts/resume_20261126/exact_affine_supported_reference.py",
  "2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117"
 ],
 "radial_observations": [
  "scripts/resume_20261126/complete_dyadic_radial_observations.py",
  "2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74"
 ],
 "radial_address_transfer": [
  "scripts/resume_20261126/radial_material_address_transfer.py",
  "6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716"
 ],
 "radial_parent_memory": [
  "scripts/resume_20261126/complete_material_envelope_memory_public_reference.py",
  "2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb"
 ]
};
const COMMON_STATISTIC_INSERTIONS = [
 "        common=base.common_parent_unweight(native)\n        if common.shape!=(7377,q.N,3):\n            raise ValueError('Keep all original material rows and all three current physical Gram components')\n        common_spectrum=spectral.statistics(common,parent_stage_weights,q.multiplicity,parameters)\n        common_spectrum=centered.augment_statistics(common,parent_stage_weights,q.multiplicity,parameters,\n            common_spectrum,stage_block=args.stage_block)\n",
 "            common_parent_functional=dict(spectral=common_spectrum,max_relative_gram=maximum(common),\n                complete_original_rows=7377,full_N=2048,\n                current_full_point_sha256=meridian.array_sha(point),\n                actual_current_model_identity_sha256=q.identity,\n                measure=report['common_parent_radial_functional'],\n                same_current_physical_field_used=True,saved_parent_values_reused=False),\n"
];

function shaText(value){return crypto.createHash("sha256").update(value,"utf8").digest("hex");}

function exactText(file,record){
 const data=fs.readFileSync(file);
 if(data.length!==record.bytes||crypto.createHash("sha256").update(data).digest("hex")!==record.sha256)
  throw new Error("Changed complete source: "+file);
 const text=data.toString("utf8");
 if(!Buffer.from(text,"utf8").equals(data))throw new Error("Not exact UTF-8: "+file);
 return text;
}

function parseOptions(argv){
 const result={};
 for(let i=0;i<argv.length;i++){
  const key=argv[i];
  if(key==="--verify-existing")result.verifyExisting=true;
  else if(key==="--repo"||key==="--outdir"){
   if(result[key.slice(2)]!==undefined||!argv[i+1])throw new Error("Missing or duplicate "+key);
   result[key.slice(2)]=path.resolve(argv[++i]);
  }else throw new Error("Unknown source-only argument "+key);
 }
 if(!result.repo||(!result.outdir&&!result.verifyExisting))
  throw new Error("Usage: node reproduce_radial_public_reference_sources.mjs --repo REPO [--outdir EMPTY_SCRATCH] [--verify-existing]");
 return result;
}

function applyExact(source,specification){
 let text=source;
 for(let i=specification.patches.length-1;i>=0;i--){
  const[start,end,before,after]=specification.patches[i];
  if(!Number.isInteger(start)||!Number.isInteger(end)||start<0||end<start||text.slice(start,end)!==before)
   throw new Error("Exact patch parent span changed: "+specification.output.name);
  text=text.slice(0,start)+after+text.slice(end);
 }
 if(Buffer.byteLength(text,"utf8")!==specification.output.bytes||shaText(text)!==specification.output.sha256)
  throw new Error("Whole constructed output changed: "+specification.output.name);
 return text;
}

function parseSourcePins(driver){
 const a=driver.indexOf("SOURCE_PINS = "),b=driver.indexOf("\nROOT_SNAPSHOT_SCHEMA",a);
 if(a<0||b<0)throw new Error("The complete literal source registry is absent");
 const result={};
 for(const m of driver.slice(a,b).matchAll(/'([A-Za-z_][A-Za-z_0-9]*)'\s*:\s*\(\s*'([^']+)'\s*,\s*'([a-f0-9]{64})'\s*\)/g)){
  if(Object.hasOwn(result,m[1]))throw new Error("Duplicate source role "+m[1]);
  result[m[1]]=[m[2],m[3]];
 }
 if(JSON.stringify(Object.entries(result).sort())!==JSON.stringify(Object.entries(SOURCE_PINS).sort()))
  throw new Error("Do not truncate or relabel the complete 78-role runtime closure");
 return result;
}

async function main(){
 const options=parseOptions(process.argv.slice(2));
 const topic=path.join(options.repo,"topics/visible-flex-larger-amplitude");
 const scriptDirectory=path.join(topic,"scripts/resume_20261126");
 const outputs={},proofs={};
 for(const item of PRIMITIVES){
  const text=exactText(path.join(scriptDirectory,item.name),item);
  outputs[item.name]=text;
 }
 for(const item of CONSTRUCTORS){
  const location=path.join(scriptDirectory,item.name);
  exactText(location,item);
  const module=await import(pathToFileURL(location).href);
  for(const [key,spec]of Object.entries(module.specifications)){
   if(Object.hasOwn(outputs,spec.output.name))throw new Error("Duplicate output "+key);
   const source=exactText(path.join(topic,spec.parent.path),spec.parent);
   outputs[spec.output.name]=applyExact(source,spec);
   proofs[key]={parent:spec.parent,output:spec.output,complete_patches:spec.patches.length};
  }
 }
 if(Object.keys(outputs).length!==21||Object.keys(proofs).length!==17)
  throw new Error("Four original complete primitives and all seventeen complete transformations are required");
 const actualDriver=outputs["fullclosed_radial_refined_public_reference_so3_qp.py"];
 const pins=parseSourcePins(actualDriver);
 for(const[role,[relative,wanted]]of Object.entries(pins)){
  const base=path.basename(relative);
  const text=Object.hasOwn(outputs,base)?outputs[base]:fs.readFileSync(path.join(topic,relative),"utf8");
  if(shaText(text)!==wanted)throw new Error("Changed whole runtime role "+role);
 }
 const originalNormal=fs.readFileSync(path.join(topic,SOURCE_PINS.radial_parent_endpoint[0]),"utf8");
 const currentNormal=outputs["so3_radial_refined_public_reference_normal_lift.py"];
 const classMarker="class ZeroClosureOperator";
 if(originalNormal.indexOf(classMarker)<0||currentNormal.indexOf(classMarker)<0||
   originalNormal.slice(originalNormal.indexOf(classMarker))!==currentNormal.slice(currentNormal.indexOf(classMarker)))
  throw new Error("The complete original normal class and every stage/implicit/field method must be retained");
 const geoProof=proofs.geometry;
 const originalGeometry=exactText(path.join(topic,geoProof.parent.path),geoProof.parent);
 const geometry=outputs[geoProof.output.name],geoMarker="    def _set_x(";
 if(originalGeometry.indexOf(geoMarker)<0||geometry.indexOf(geoMarker)<0||
    originalGeometry.slice(originalGeometry.indexOf(geoMarker))!==geometry.slice(geometry.indexOf(geoMarker)))
  throw new Error("The complete original physical scan/rows/permanent-memory suffix changed");
 const originalDriver=exactText(path.join(topic,proofs.driver.parent.path),proofs.driver.parent);
 const suffixMarker="    def save_report():";
 let projected=actualDriver.slice(actualDriver.indexOf(suffixMarker));
 if(actualDriver.indexOf(suffixMarker)<0)throw new Error("Missing full scientific suffix");
 for(const text of COMMON_STATISTIC_INSERTIONS){
  if(projected.split(text).length!==2)throw new Error("Keep exactly the declared complete common-parent statistic insertion");
  projected=projected.replace(text,"");
 }
 if(projected!==originalDriver.slice(originalDriver.indexOf(suffixMarker)))
  throw new Error("The actual complete scientific suffix differs beyond the two declared common-parent statistic insertions");
 if(options.verifyExisting)for(const[name,text]of Object.entries(outputs))
  if(fs.readFileSync(path.join(scriptDirectory,name),"utf8")!==text)throw new Error("Existing full output differs: "+name);
 if(options.outdir){
  const rel=path.relative(options.repo,options.outdir);
  if(rel===""||(!rel.startsWith(".."+path.sep)&&rel!==".."&&!path.isAbsolute(rel)))
   throw new Error("Construct only in scratch outside the repository");
  if(fs.existsSync(options.outdir)&&fs.readdirSync(options.outdir).length)throw new Error("Use an empty scratch output directory");
  fs.mkdirSync(options.outdir,{recursive:true});
  for(const[name,text]of Object.entries(outputs))fs.writeFileSync(path.join(options.outdir,name),text,{encoding:"utf8",flag:"wx"});
 }
 process.stdout.write(JSON.stringify({schema:"complete-public09-radial-source-reconstruction-v1",
  complete_source_count:21,original_complete_primitives:4,derived_complete_bodies:17,runtime_role_count:78,
  all_whole_outputs_equal:true,complete_original_normal_class_equal:true,complete_original_geometry_physical_suffix_equal:true,
  complete_scientific_suffix_equal_after_only_two_declared_common_parent_statistics_insertions:true,
  science_imported_or_executed:false,Python_AST_or_compile_executed:false,outputs:Object.fromEntries(Object.entries(outputs).map(([name,text])=>[name,{bytes:Buffer.byteLength(text,"utf8"),sha256:shaText(text)}]))},null,2)+"\n");
}

await main();
