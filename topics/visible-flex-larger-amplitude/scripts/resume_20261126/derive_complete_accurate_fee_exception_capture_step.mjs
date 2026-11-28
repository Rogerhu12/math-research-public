#!/usr/bin/env node
/** Build one complete captured fee step from a whole-byte-bound original ready.
 * Text/JSON construction only: does not import or execute any scientific source.
 * The original ready, original step, arguments, domain, budgets and history remain.
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const SCHEMA = "complete-original-accurate-fee-exception-capture-parameter-deriver-v1";
const WRAPPER = {
  "name": "capture_complete_accurate_fee_exception.py",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/capture_complete_accurate_fee_exception.py",
  "bytes": 14448,
  "sha256": "16c18a231f19718594dba5abb8cb72e67c7eda3f2974aa061d2bcf72cfc57f5e",
  "git_blob_sha": "2584e65a5306ca8aae5c6478e8a0c1551dac81b1",
  "role": "complete-original-fee-exception-capture-entry"
};
const MAX_FILE_BYTES = 100000;
const sha = bytes => crypto.createHash("sha256").update(bytes).digest("hex");
const gitBlob = bytes => crypto.createHash("sha1")
  .update(Buffer.from("blob " + bytes.length + "\0")).update(bytes).digest("hex");
const clone = value => JSON.parse(JSON.stringify(value));
function stable(value) {
  if (Array.isArray(value)) return "[" + value.map(stable).join(",") + "]";
  if (value !== null && typeof value === "object") return "{"
    + Object.keys(value).sort().map(key => JSON.stringify(key) + ":" + stable(value[key])).join(",") + "}";
  return JSON.stringify(value);
}
function same(a,b,label) {
  if(stable(a)!==stable(b)) throw new Error(label + " differs");
}
function fail(message) { throw new Error(message); }
function argumentsOf(argv) {
  const allowed = new Set(["--repository-root","--recipe","--output-directory"]);
  const out={};
  for(let i=0;i<argv.length;i+=2) {
    const key=argv[i],value=argv[i+1];
    if(!allowed.has(key)||typeof value!=="string"||out[key]!==undefined)
      fail("Supply each full required parameter exactly once");
    out[key]=value;
  }
  for(const key of allowed) if(out[key]===undefined) fail("Missing " + key);
  return out;
}
function inside(root,relative) {
  if(typeof relative!=="string"||relative.length===0||path.isAbsolute(relative))
    fail("An explicit repository-relative complete file path is required");
  const candidate=path.resolve(root,relative),rel=path.relative(root,candidate);
  if(rel===".."||rel.startsWith(".."+path.sep)||path.isAbsolute(rel))
    fail("The complete source/ready path escapes the declared repository");
  return candidate;
}
function readSmall(file) {
  const stat=fs.statSync(file);
  if(!stat.isFile()||stat.size>=MAX_FILE_BYTES) fail("Only a complete text artifact below 100000 bytes may be read");
  const bytes=fs.readFileSync(file);
  if(bytes.length!==stat.size) fail("The file changed during its full read");
  return bytes;
}
function verify(root,record,label) {
  if(!record||typeof record.path!=="string"||!Number.isInteger(record.bytes)
      ||!(/^[0-9a-f]{64}$/).test(record.sha256)) fail("Complete " + label + " identity is missing");
  const file=inside(root,record.path),bytes=readSmall(file);
  if(bytes.length!==record.bytes||sha(bytes)!==record.sha256)
    fail("Complete " + label + " byte count/SHA differs");
  if(record.git_blob_sha!==undefined&&gitBlob(bytes)!==record.git_blob_sha)
    fail("Complete " + label + " Git blob differs");
  return {file,bytes,text:bytes.toString("utf8")};
}
function pointer(value,word) {
  if(word==="") return value;
  if(typeof word!=="string"||!word.startsWith("/")) fail("Use a complete RFC6901 JSON pointer");
  let current=value;
  for(const part of word.slice(1).split("/")) {
    if(/~(?:[^01]|$)/.test(part)) fail("Invalid JSON pointer escape");
    const key=part.replace(/~1/g,"/").replace(/~0/g,"~");
    if(current===null||typeof current!=="object"||!Object.hasOwn(current,key))
      fail("The complete parent JSON pointer does not exist");
    current=current[key];
  }
  return current;
}
function canonicalRecord(file,bytes) {
  return {path:file,bytes:bytes.length,sha256:sha(bytes),git_blob_sha:gitBlob(bytes)};
}
function makeStep(original,source,recipe) {
  if(!original||typeof original!=="object"||Array.isArray(original)
      ||typeof original.id!=="string"||typeof original.script!=="string"
      ||!Array.isArray(original.args)||!original.args.every(v=>typeof v==="string")
      ||!Array.isArray(original.outputs)||!original.outputs.every(v=>typeof v==="string")
      ||!original.summary||typeof original.summary!=="object"||Array.isArray(original.summary))
    fail("The selected original whole step does not have the complete controller contract");
  if(original.script!==source.path) fail("The target source must be exactly the original step script");
  if(typeof recipe.new_step_id!=="string"||recipe.new_step_id.length===0
      ||recipe.new_step_id===original.id) fail("Use an explicit fresh actual step id");
  const relative=recipe.diagnostic_directory_relative_to_work;
  if(typeof relative!=="string"||relative.length===0||relative.startsWith("/")
      ||relative.split("/").some(p=>p===""||p==="."||p==="..")
      ||relative.includes("{")||relative.includes("}"))
    fail("Use a fresh explicit diagnostic directory relative to work");
  const diagnostic=relative+"/execution-diagnostic.json";
  if(original.outputs.includes(diagnostic)||Object.hasOwn(original.summary,diagnostic))
    fail("The diagnostic file must not replace an original declared output");
  const header=["--target-script","{repo}/"+source.path,
    "--target-sha256",source.sha256,"--target-bytes",String(source.bytes),
    "--diagnostic-directory","{work}/"+relative,"--"];
  const step=clone(original);
  step.id=recipe.new_step_id;
  step.script=WRAPPER.path;
  step.args=header.concat(original.args);
  step.outputs=original.outputs.concat([diagnostic]);
  step.summary=clone(original.summary);
  step.summary[diagnostic]={
    schema:"schema",actual_phase:"phase",
    original_entry_invoked:"original_entry_invoked",
    original_entry_completed_or_raised:"original_entry_completed_or_raised",
    actual_exception_type:"actual_python_exception_type",
    actual_exception_module:"actual_python_exception_module",
    actual_exception_preview:"actual_python_exception_message_preview",
    complete_trace_in_diagnostic:"complete_python_traceback_text_in_this_diagnostic",
    actual_full_trace:"full_python_traceback.sha256",
    actual_source:"original_target_source.sha256",
    requested_source:"expected_target_source.sha256",
    original_exit_code:"original_SystemExit_code",
    mathematical_success_inferred:"mathematical_success_inferred"
  };
  if(typeof original.scope==="string") step.scope=original.scope
    +" Complete original source and arguments execute once through the separate exception-capture entry; "
    +"execution diagnostics neither change scientific status nor supply an absent report, point, root or fee.";
  const inverse=clone(step);
  inverse.id=original.id;inverse.script=original.script;
  inverse.args=inverse.args.slice(header.length);
  inverse.outputs=inverse.outputs.slice(0,-1);
  delete inverse.summary[diagnostic];
  if(Object.hasOwn(original,"scope")) inverse.scope=original.scope;
  else delete inverse.scope;
  same(inverse,original,"The complete inverse original step");
  same(step.args.slice(header.length),original.args,"Every original numerical and path word");
  for(const [output,selectors] of Object.entries(original.summary))
    same(step.summary[output],selectors,"Every complete original selector object");
  for(const [key,value] of Object.entries(original))
    if(!["id","script","args","outputs","summary","scope"].includes(key))
      same(step[key],value,"Every other original step field "+key);
  return {step,diagnostic,header_words:header.length};
}
function writeNew(root,relative,value) {
  const file=inside(root,relative);
  const bytes=Buffer.from(JSON.stringify(value,null,2)+"\n","utf8");
  if(bytes.length>=MAX_FILE_BYTES) fail("Keep the complete output below 100000 bytes; share whole history rather than trim it");
  fs.mkdirSync(path.dirname(file),{recursive:true});
  fs.writeFileSync(file,bytes,{flag:"wx"});
  return canonicalRecord(relative,bytes);
}
function main() {
  const cli=argumentsOf(process.argv.slice(2));
  const root=path.resolve(cli["--repository-root"]);
  const out=path.resolve(cli["--output-directory"]);
  const recipeFile=path.resolve(cli["--recipe"]),recipeBytes=readSmall(recipeFile);
  const recipe=JSON.parse(recipeBytes.toString("utf8"));
  if(recipe.schema!=="complete-original-accurate-fee-exception-capture-recipe-v1")
    fail("Use the explicit whole-parent capture recipe schema");
  const parent=verify(root,recipe.parent_ready,"original parent ready");
  const source=verify(root,recipe.target_source,"original scientific target");
  verify(root,WRAPPER,"independent exception capture entry");
  const parentValue=JSON.parse(parent.text),original=pointer(parentValue,recipe.parent_step_pointer);
  const built=makeStep(original,recipe.target_source,recipe);
  const ready={
    schema:"complete-original-accurate-fee-exception-capture-ready-v1",
    executed:false,admitted:false,
    scientific_execution_only_in_public_Actions:true,
    complete_original_scientific_ready:recipe.parent_ready,
    complete_original_step_pointer:recipe.parent_step_pointer,
    complete_original_scientific_ready_metadata_reference:{
      file:recipe.parent_ready,json_pointer:""},
    complete_original_step:clone(original),
    original_target_source:recipe.target_source,
    complete_capture_entry_source:WRAPPER,
    complete_parameter_recipe:canonicalRecord(recipeFile,recipeBytes),
    steps:[built.step],
    complete_original_argv_word_count:original.args.length,
    capture_header_including_separator_word_count:built.header_words,
    original_argv_retained_in_order_and_byte_values:true,
    all_original_outputs_selectors_and_other_step_fields_retained:true,
    original_source_and_downstream_source_pins_unchanged:true,
    original_stdout_unchanged_by_capture_entry:true,
    original_scientific_output_directory_unchanged:true,
    original_repo_argument_unchanged:true,
    resume_repo_path_must_already_be_the_original_request_bound_absolute_path:true,
    diagnostic_directory_must_be_fresh_and_separate:true,
    controller_executes_capture_source_original_report_still_binds_original_source:true,
    original_pure_and_source_guards_execute_without_weakening:true,
    complete_original_domain_and_all_budgets_unchanged:true,
    actual_return_diagnostics_do_not_prove_completion_or_infeasibility:true,
    no_additional_F_J_root_or_scientific_probe:true,
    historical_statuses_and_unknown_responsibilities_replaced:false,
    actual_future_report_sha256:null,actual_future_point_sha256:null,
    actual_future_exception_or_trace:null,
    execution_has_not_been_requested_or_run_by_parameter_deriver:true
  };
  const output=writeNew(out,recipe.output_ready_path,ready);
  process.stdout.write(JSON.stringify({schema:SCHEMA,output,
    complete_original_argv_word_count:original.args.length,
    wrapped_argv_word_count:built.step.args.length,
    all_scientific_source_execution_performed:false},null,2)+"\n");
}
main();
