// Static text-only budget construction for WAD. This is not a scientific consumer.
function wadStaticModel(workerText,oldModel) {
 // Metadata-only model. This does not import or execute either scientific source.
 const literal=name=>{
   const re=new RegExp("^"+name+"=json\\.loads\\((\"(?:\\\\.|[^\"\\\\])*\")\\)$","m");
   const m=workerText.match(re);
   if(!m)throw Error("missing literal metadata constant "+name);
   return JSON.parse(JSON.parse(m[1]));
 };
 const copy=x=>JSON.parse(JSON.stringify(x));
 const fields=literal("SCIENCE_FIELDS"),pins=literal("SCIENCE_PIN_SHA256"),sizes=literal("SCIENCE_PIN_BYTES");
 const shapes=literal("SCIENTIFIC_GRAPH_SHAPES"),placeholder="B".repeat(128);
 const materialize=x=>x==="__FINITE_SCALAR__"?placeholder:
   Array.isArray(x)?x.map(materialize):
   x&&typeof x==="object"?Object.fromEntries(Object.entries(x).map(([k,v])=>[k,materialize(v)])):x;
 const graphs=materialize(shapes);
 const candidates=[
   {label:"saved_old_complete_Cstar",upper:copy(oldModel.original_scalar_records.Cold)},
   {label:"new_complete_first_row_candidate",upper:copy(graphs.complete_new_whole_row_candidate_conclusion.complete_first_row_candidate_upper)}
 ];
 const doc={
   kind:"actual_complete_physical_waist_first_row_receiver_v1",complete:true,proved:true,stage:"complete",failure:null,
   source_sha256:"437b69ea0d6790d2880b381e6747f2ced0da86a35ded73767886ded1657a1684",
   input_manifest_sha256:"f".repeat(64),
   input_sha256:{...pins,manifest:"f".repeat(64)},
   verified_original_inputs:Object.fromEntries(Object.entries(pins).map(([role,sha256])=>[role,{bytes:sizes[role],sha256}])),
   parameters:literal("SCIENCE_PARAMETERS"),runtime:{Python:"3.12.14",python_flint:"0.9.0"},arithmetic_bits:320,
   public_repository:"Rogerhu12/math-research-public",run_id:"999999999999",run_attempt:"99",
   workflow_event_commit:"f".repeat(40),actual_scientific_checkout_commit:"f".repeat(40),actual_returncode:0,
   gates:literal("SCIENCE_GATE_NAMES").map(name=>({name,passed:true})),
   actual_progress:literal("SUCCESS_ACTUAL_PROGRESS"),accepted_old_receipts:literal("ACCEPTED_OLD_RECEIPTS"),
   copied_original_scalar_records:copy(oldModel.original_scalar_records),
   copied_complete_original_scopes:copy(oldModel.complete_original_scope_objects),
   complete_new_first_row_gain_conclusion:graphs.complete_new_first_row_gain_conclusion,
   complete_new_whole_row_candidate_conclusion:graphs.complete_new_whole_row_candidate_conclusion,
   complete_whole_row_selection:{
     comparison:"whole saved old Cstar and complete new first-row candidate",
     complete_candidates:candidates,selected_index:1,selected_label:candidates[1].label,
     complete_selected_row_upper:copy(candidates[1].upper),new_candidate_upper_strictly_smaller:true,
     old_candidate_wins_ties:true,entrywise_minimum_used:false,different_trial_or_different_output_unit_minimum_used:false
   },
   original_scalar14_canonical_sha256:"070b718bed4a386dea25f0570c17a8573e8d1f33befea4edb81db9ebf0d4dc66",
   original_scope9_canonical_sha256:"fa01be532e31dc611aaf858b505115afb2596120f54de30de59ddb4b537ddec7",
   scope:literal("SCIENCE_SCOPE"),actual_mathematical_wall_seconds:12345.123456789,
   old_successful_targets_recomputed:0,new_reproducible_arrays_persisted:false
 };
 if(fields.length!==32||Object.keys(doc).length!==32||fields.some(k=>!Object.hasOwn(doc,k)))throw Error("32-field static model mismatch");
 return doc;
}
function wadStaticCanonical(x) {
 if(x===null)return "null";
 if(Array.isArray(x))return "["+x.map(wadStaticCanonical).join(",")+"]";
 if(typeof x==="object")return "{"+Object.keys(x).sort().map(k=>JSON.stringify(k)+":"+wadStaticCanonical(x[k])).join(",")+"}";
 return JSON.stringify(x);
}
function wadStaticState(doc) {
 return {run_id:doc.run_id,run_attempt:doc.run_attempt,workflow_commit:doc.workflow_event_commit,
 actual_scientific_checkout_commit:doc.actual_scientific_checkout_commit,source_sha256:doc.source_sha256,
 input_manifest_sha256:doc.input_manifest_sha256,complete_mathematical_receipt_available:true,
 actual_returncode:0,actual_new_scientific_processes:1,actual_failure:null};
}
function wadStaticPrepublication(state,doc,report) {
 return {marker:"PHYSICAL_WAIST_FIRST_ROW_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
 source_sha256:state.source_sha256,manifest_sha256:state.input_manifest_sha256,
 run_id:state.run_id,run_attempt:state.run_attempt,actual_returncode:state.actual_returncode,
 scientific_result:doc,report_text:report};
}
function wadRender(state,science) {
 const s=science||{};
 const pystr=v=>v===null||v===undefined?"None":v===true?"True":v===false?"False":String(v);
 const cell=v=>pystr(v).replace(/\|/g,"\\|").replace(/\n/g," ");
 const ball=v=>{
   if(v&&typeof v==="object"&&!Array.isArray(v)){
     if(typeof v.ball==="string")return v.ball;
     if("upper" in v)return pystr(v.upper);
     return JSON.stringify(v);
   }
   return pystr(v);
 };
 const get=(o,k,defaultValue=null)=>Object.prototype.hasOwnProperty.call(o,k)?o[k]:defaultValue;
 const sortedJson=v=>{
   if(v===null)return "null";
   if(Array.isArray(v))return "["+v.map(sortedJson).join(", ")+"]";
   if(typeof v==="object")return "{"+Object.keys(v).sort().map(k=>JSON.stringify(k)+": "+sortedJson(v[k])).join(", ")+"}";
   return JSON.stringify(v);
 };
 const failed=get(state,"actual_failure")!==null||get(s,"failure")!==null;
 const lines=[
 "# Actual complete physical waist first-row receiver",
 "",
 "This is the complete new scalar readout for WAD.32--36. The old ST and SW successes are immutable inputs.",
 "It retains the original natural-root H^(-4/3) input and raw moving-angle even meanzero L2 primitive output.",
 "",
 "## Actual execution",
 "",
 "| Item | Recorded value |",
 "|---|---|",
 "| Public run / attempt | "+cell(state.run_id)+"/"+cell(state.run_attempt)+" |",
 "| Workflow event commit | "+cell(state.workflow_commit)+" |",
 "| Actual scientific checkout | "+cell(get(state,"actual_scientific_checkout_commit","not launched"))+" |",
 "| Scientific source SHA256 | "+cell(state.source_sha256)+" |",
 "| Manifest SHA256 | "+cell(state.input_manifest_sha256)+" |",
 "| Complete scientific receipt | "+cell(get(state,"complete_mathematical_receipt_available",false))+" |",
 "| Actual return code | "+cell(get(state,"actual_returncode"))+" |",
 "| New scientific child processes | "+cell(state.actual_new_scientific_processes)+" |",
 "| Original ST / SW successes | 43757644616/1 and 43781399696/1 |",
 "| Gates passed / recorded | "+String((s.gates||[]).filter(g=>g.passed===true).length)+"/"+String((s.gates||[]).length)+" |",
 "",
 "## Complete new scalar records",
 "",
 "| Whole scalar | Outward record |",
 "|---|---|"
 ];
 if(failed){
   lines.push("","Every completed scalar and candidate is retained in actual-scientific-conclusion.json when that file exists. The full diagnostic appears below; execution.json records whether a scientific child and result existed.");
 }else for(const key of ["complete_new_first_row_gain_conclusion","complete_new_whole_row_candidate_conclusion"]){
   const graph=s[key]||{};
   for(const [name,value] of Object.entries(graph)){
     if(value&&typeof value==="object"&&!Array.isArray(value)&&Object.keys(value).length===1&&Object.hasOwn(value,"ball"))
       lines.push("| "+cell(name)+" | "+cell(value.ball)+" |");
   }
 }
 const selected=s.complete_whole_row_selection||{};
 lines.push("","## Whole-row selection","","| Candidate | Complete outward record |","|---|---|");
 if(!failed)for(const row of selected.complete_candidates||[])
   lines.push("| "+cell(row.label)+" | "+cell(ball(row.upper))+" |");
 lines.push("",
 "Selected complete record: "+cell(get(selected,"selected_label","no complete selection"))+".",
 "",
 "## Retained scope",
 "",
 "All PC, ST4, original cut, ordinary leading and full Q sources, independent mean, all 3070 interfaces, and the saved waist FT correction are retained exactly once. Interface terms have no radial length factor.",
 "The scientific schema covers fourteen original scalar records, nine complete original scopes, three new graphs and sixteen gates. Every stage actually completed is retained without truncation; the actual progress and complete/proved flags determine success.",
 "The first matrix row comes from the saved complete positive reverse algorithm. No old matrix product, source integral, exponential, trial, native enclosure or numerical graph is rerun.",
 "The comparison selects one entire final serialized upper record, with the old candidate retained on a tie. It does not splice favorable contributions.",
 "This readout has the original raw primitive-row units. It does not on its own prove a signed adjoint cancellation, WPL's differently normalized error, a usable high-frequency gate, a finite/mean/nu inverse, a nonlinear background or the final surface.",
 "",
 "Available scientific hashes are in execution.json. Available scientific output and this report are printed before Git publication, with an independent execution prepublication receipt.",
 "Current-tree capacity and both README reviews are recorded after real git pull --rebase operations. No new reproducible array, artifact or Release is published.",
 "");
 if(get(state,"actual_failure")!==null||get(s,"failure")!==null){
   const wf=get(state,"actual_failure"),sf=get(s,"failure");
   lines.push("## Actual incomplete outcome","");
   if(sortedJson(wf)===sortedJson(sf))
     lines.push("Same complete worker/science failure: "+cell(sortedJson(sf)));
   else
     lines.push("Worker: "+cell(sortedJson(wf)),"Science: "+cell(sortedJson(sf)));
   lines.push("Every completed scientific stage remains in the full science record. An incomplete run is not permission to recompute completed stages.","");
 }
 return lines.join("\n");
}
function wadStaticBudget(workerText,oldModel,manifestDraft,executionTemplate,hash) {
 // All values below are text/JSON-size models. No scientific arithmetic is evaluated.
 const can=x=>wadStaticCanonical(x)+"\n",copy=x=>JSON.parse(wadStaticCanonical(x));
 const doc=wadStaticModel(workerText,oldModel),baseState=wadStaticState(doc);
 const finalWorker=hash(workerText),F40="f".repeat(40),F64="f".repeat(64);
 const placeholders=x=>{
   if(Array.isArray(x))return x.map(placeholders);
   if(x&&typeof x==="object")return Object.fromEntries(Object.entries(x).map(([k,v])=>[k,placeholders(v)]));
   if(typeof x==="string"){
     if(/^[a-f0-9]{40}$/.test(x))return F40;
     if(/^[a-f0-9]{64}$/.test(x))return F64;
     if(/^\d{4}-\d\d-\d\dT/.test(x))return "2026-11-16T00:00:00.999999+00:00";
   }
   return x;
 };
 const e=placeholders(copy(executionTemplate));
 Object.assign(e,{
   kind:"actual_public_physical_waist_first_row_receiver_execution_v1",
   run_id:doc.run_id,run_attempt:doc.run_attempt,source_sha256:doc.source_sha256,
   worker_source_sha256:finalWorker.sha256,
   mathematical_input_sha256:Object.fromEntries(Object.entries(doc.input_sha256).filter(([k])=>k!=="manifest")),
   actual_verified_Git_input_count:7,complete_immutable_Python_AST_file_count:3,
   actual_scientific_runtime:{Python:"3.12.14",python_flint:"0.9.0"},
   new_scientific_child_wall_seconds:899.123456789
 });
 e.actual_original_Git_input_receipts=manifestDraft.files.map(x=>({
   role:x.role,path:x.path,bytes:x.role==="worker"?finalWorker.bytes:x.bytes,
   sha256:x.role==="worker"?finalWorker.sha256:x.sha256,origin:"exact_current_small_text"
 }));
 e.actual_verified_Git_input_receipts_sha256=hash(can(e.actual_original_Git_input_receipts)).sha256;
 e.complete_immutable_Python_AST_inventory_sha256=hash(can(e.actual_original_Git_input_receipts.filter(x=>x.path.endsWith(".py")).map(x=>({path:x.path,sha256:x.sha256})))).sha256;
 e.output_hashes=[{file:"actual-scientific-conclusion.json",...hash(can(doc))},
   {file:"new-scientific-child.stdout.log",bytes:9999999999,sha256:F64}];
 e.scientific_conclusion={file:"actual-scientific-conclusion.json",...hash(can(doc)),
   complete:true,actual_returncode:0,actual_gate_count:16,actual_passed_gate_count:16,
   original_result_printed_before_any_format_gate:true};
 for(const k of ["current_topic_blob_bytes","publication_base_topic_blob_bytes","projected_topic_blob_bytes"])e[k]=199999999;
 for(const k of ["current_published_topic_capacity_metadata","publication_capacity_metadata"]){
   e[k].blob_bytes=199999999;e[k].blob_count=99999;e[k].nested_tree_count=99999;
   for(const row of e[k].metadata_responses)row.bytes=16000000;
 }
 for(const k of ["current_topic_capacity_metadata","publication_owned_HEAD_delta"]){
   e[k].blob_bytes=199999999;e[k].blob_count=99999;
 }
 e.current_topic_blob_count=99999;
 const results=[];
 for(const mode of ["success","same_failure2000","different_failure1200","different_failure2000"]){
   const d=copy(doc),state=copy(baseState),ex=copy(e);
   if(mode!=="success"){
     Object.assign(d,{complete:false,proved:false,actual_returncode:1,
       stage:"complete_final_readonly_and_schema_checks",
       failure:{error_type:"ValueError",message:"X".repeat(2000),actual_progress:copy(d.actual_progress),
       complete_new_graphs_preserved:["complete_new_first_row_gain_conclusion","complete_new_whole_row_candidate_conclusion","complete_whole_row_selection"]}});
     Object.assign(state,{actual_returncode:1,complete_mathematical_receipt_available:false,actual_failure:copy(d.failure)});
     if(mode.startsWith("different"))state.actual_failure={type:"RuntimeError",message:"W".repeat(mode.endsWith("1200")?1200:2000)};
   }
   // Canonical source file is read back by the worker before rendering.
   const readDoc=JSON.parse(wadStaticCanonical(d)),report=wadRender(state,readDoc);
   const payload=wadStaticPrepublication(state,readDoc,report);
   const si=hash(can(readDoc)),ri=hash(report),pi=hash(can(payload));
   Object.assign(ex,{actual_failure:state.actual_failure,actual_returncode:state.actual_returncode,
     complete:state.complete_mathematical_receipt_available,complete_mathematical_receipt_available:state.complete_mathematical_receipt_available});
   Object.assign(ex.scientific_conclusion,{...si,complete:d.complete,actual_returncode:d.actual_returncode});
   Object.assign(ex.output_hashes[0],si);
   const prior=copy(ex);
   for(const k of ["recoverable_prepublication_stdout","publication_capacity_metadata","publication_owned_HEAD_delta",
      "publication_base_topic_blob_bytes","publication_capacity_metadata_commit","projected_topic_blob_bytes",
      "metadata_publication_retry_pending"])delete prior[k];
   prior.readme_checks=prior.readme_checks.slice(0,1);
   const process=hash(can({marker:"PHYSICAL_WAIST_FIRST_ROW_EXECUTION_PREPUBLICATION_V1",execution:prior}));
   ex.recoverable_prepublication_stdout={bytes:pi.bytes,sha256:pi.sha256,process_bytes:process.bytes,process_sha256:process.sha256,
     complete_science_and_report_preserved:true,before_any_git_publication:true};
   const ei=hash(can(ex));
   results.push({mode,science:si,report:ri,prepublication:pi,execution:ei,execution_prepublication:process,
     published_three_file_bytes:si.bytes+ri.bytes+ei.bytes});
 }
 return results;
}
