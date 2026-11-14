/* Reproduction entry for the already completed pure-V8 strong R197 chart.
 * The CLI is a new execution entry: each actual Node run writes its own
 * observations. It never adopts an earlier V8 elapsed time or process exit.
 * Run from the topic directory. No large arrays are printed to stdout.
 */
"use strict";
function parseArgs(argv){
  const out={};for(let i=0;i<argv.length;i++){
    const k=argv[i];if(!["--request","--out-prefix","--resume","--cell-limit","--expected-report"].includes(k))throw Error("Unknown argument "+k);
    if(i+1>=argv.length)throw Error("Missing argument value");out[k.slice(2)]=argv[++i];
  }
  if(!out.request||!out["out-prefix"])throw Error("--request and --out-prefix are required");
  if(out["cell-limit"]!==undefined&&(!/^[0-9]+$/.test(out["cell-limit"])||Number(out["cell-limit"])<1))throw Error("Positive cell limit required");
  return out;
}
function main(argv){
  const fs=require("node:fs"),path=require("node:path"),zlib=require("node:zlib"),crypto=require("node:crypto");
  const a=parseArgs(argv),sha=b=>crypto.createHash("sha256").update(b).digest("hex");
  const requestPath=path.resolve(a.request),requestBytes=fs.readFileSync(requestPath),request=JSON.parse(requestBytes.toString("utf8"));
  if(request.schema!=="fd2d-R197-strong-saved-ellipse-incremental-run-request-v1")throw Error("Wrong request schema");
  function requireBound(row){
    const p=path.resolve(row.path),b=fs.readFileSync(p);
    if(b.length!==row.bytes||sha(b)!==row.sha256)throw Error("Frozen source mismatch: "+row.path);
    return require(p);
  }
  const arithmeticModule=requireBound(request.arithmetic_source),chartModule=requireBound(request.source);
  requireBound(request.original_R197_source);
  const prefix=path.resolve(a["out-prefix"]),dir=path.dirname(prefix);fs.mkdirSync(dir,{recursive:true});
  const output={checkpoint:prefix+"-checkpoint.json.gz",portable:prefix+"-portable.json.gz",
    progress:prefix+"-progress.json",report:prefix+"-report.json",owner:prefix+"-owner.json"};
  let checkpoint;
  if(a.resume){
    const p=path.resolve(a.resume),b=fs.readFileSync(p);
    checkpoint=JSON.parse((p.endsWith(".gz")?zlib.gunzipSync(b):b).toString("utf8"));
  }
  const C=arithmeticModule.createR188ExactPrimitive(request.arithmetic_precision_bits);
  const chart=chartModule.createR197ResumableSavedEllipseChart({...request.chart_spec,checkpoint},C);
  const owner={schema:"fd2d-R197-node-replay-owner-v1",request_sha256:sha(requestBytes),
    binding_sha256:chart.progress().binding_sha256,source_sha256:request.source.sha256};
  if(fs.existsSync(output.owner)){
    if(!a.resume)throw Error("Existing output requires explicit --resume");
    const old=JSON.parse(fs.readFileSync(output.owner,"utf8"));
    if(JSON.stringify(old)!==JSON.stringify(owner))throw Error("Existing output owner/binding differs");
  }else{
    for(const p of Object.values(output))if(fs.existsSync(p))throw Error("Unowned existing output: "+p);
    fs.writeFileSync(output.owner,JSON.stringify(owner,null,2)+"\n",{flag:"wx"});
  }
  function atomicWrite(p,b){
    const temp=p+".tmp-"+process.pid;
    fs.writeFileSync(temp,b,{flag:"wx"});fs.renameSync(temp,p);
  }
  function saveJSON(p,obj,gzip){
    const raw=Buffer.from(JSON.stringify(obj),"utf8"),out=gzip?zlib.gzipSync(raw,{level:9}):raw;
    if(out.length>=5000000)throw Error("One output exceeds repository 5 MB limit");
    atomicWrite(p,out);return {path:p,uncompressed_bytes:raw.length,uncompressed_sha256:sha(raw),
      stored_bytes:out.length,stored_sha256:sha(out),compression:gzip?"gzip":"none",serialization:"JSON.stringify with no trailing newline"};
  }
  const start=chart.progress().completed_cells,startedUTC=new Date().toISOString(),started=process.hrtime.bigint();
  let observations=[];
  if(a.resume&&fs.existsSync(output.progress)){
    const old=JSON.parse(fs.readFileSync(output.progress,"utf8"));
    if(old.binding_sha256!==owner.binding_sha256||old.request_sha256!==owner.request_sha256)throw Error("Progress binding mismatch");
    observations=old.observations||[];
  }
  let checkpointIdentity;
  const maximum=a["cell-limit"]===undefined?request.chart_spec.cells:Number(a["cell-limit"]);
  for(let i=0;i<maximum&&!chart.progress().complete;i++){
    const t0=process.hrtime.bigint(),from=chart.progress().completed_cells;
    chart.advance(1);
    checkpointIdentity=saveJSON(output.checkpoint,chart.checkpointState(),true);
    const row={completed_utc:new Date().toISOString(),from_completed_cells:from,completed_cells:chart.progress().completed_cells,
      actual_node_seconds:Number(process.hrtime.bigint()-t0)/1e9,checkpoint:checkpointIdentity,
      last_row_sha256:chart.progress().last_row_sha256};
    observations.push(row);
    saveJSON(output.progress,{...owner,schema:"fd2d-R197-node-replay-progress-v1",observations},false);
    process.stdout.write(JSON.stringify({completed_cells:row.completed_cells,total_cells:request.chart_spec.cells,
      actual_node_seconds:row.actual_node_seconds,checkpoint_sha256:checkpointIdentity.uncompressed_sha256})+"\n");
  }
  if(!checkpointIdentity)checkpointIdentity=saveJSON(output.checkpoint,chart.checkpointState(),true);
  const complete=chart.progress().complete;
  const portableIdentity=complete?saveJSON(output.portable,chart.portablePackets(),true):null;
  let expectedComparison=null;
  if(complete&&a["expected-report"]){
    const expected=JSON.parse(fs.readFileSync(path.resolve(a["expected-report"]),"utf8"));
    expectedComparison={portable_sha256_matches:portableIdentity.uncompressed_sha256===expected.complete_portable.sha256,
      checkpoint_sha256_matches:checkpointIdentity.uncompressed_sha256===expected.complete_checkpoint.sha256};
    if(!Object.values(expectedComparison).every(Boolean))throw Error("Actual regenerated bytes differ from the declared V8 output; files are retained");
  }
  const report={schema:"fd2d-R197-node-reproduction-report-v1",completed:true,whole_chart_complete:complete,
    execution:{host:"Node",node_version:process.version,started_utc:startedUTC,completed_utc:new Date().toISOString(),
      observed_seconds:Number(process.hrtime.bigint()-started)/1e9,
      started_from_completed_cells:start,created_child_OS_process:false,
      checkpoint_OS_process_created_field_scope:"The pure constructor does not create a child process; this report records the actual existing Node host. External shell exit is not inferred."},
    request_sha256:owner.request_sha256,source:request.source,arithmetic_source:request.arithmetic_source,
    progress:chart.progress(),checkpoint:checkpointIdentity,portable:portableIdentity,expectedComparison,
    status:complete?"actual complete quarter generated":"requested finite partial batch saved",
    normalization_recomputed:false,old_small_gap_chart_recomputed:false,normal_or_BVP_recomputed:false};
  saveJSON(output.report,report,false);
  process.stdout.write(JSON.stringify({report:output.report,complete,portable_sha256:portableIdentity&&portableIdentity.uncompressed_sha256})+"\n");
  return report;
}
if(typeof module!=="undefined"&&module.exports)module.exports={main,parseArgs};
if(typeof require==="function"&&require.main===module){
  try{main(process.argv.slice(2));}catch(error){process.stderr.write(String(error.stack||error)+"\n");process.exitCode=1;}
}
