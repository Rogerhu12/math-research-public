"use strict";
/* Recovered explicit composite: first preserve the actual original Cauchy
 * observer, then run a separately counted fixed-g Cartesian experiment.
 * One ordinary local scalar-note commit; parent owns pull/push/HANDOFF. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto"),cp=require("node:child_process");
const original=require("./6a65-cauchy-same-field-observer-recovered-v2.cjs");
const MARKER="6a65-independent-Cartesian-after-actual-Cauchy-observer-v1";
const TOPIC="topics/visible-flexible-closed-surface",ENTRY="6a65-cartesian-independent-experiment-v2.py";
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const emit=x=>process.stdout.write(JSON.stringify(x)+"\n");
const pause=ms=>Atomics.wait(new Int32Array(new SharedArrayBuffer(4)),0,0,ms);
function write(p,v){if(fs.existsSync(p))throw Error("Fresh output required: "+p);fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,JSON.stringify(v,null,2)+"\n");}
function noCredentials(){
  const env={...process.env};
  for(const k of Object.keys(env))if(["GH_TOKEN","GITHUB_TOKEN","MR_TOKEN","VISIBLE_FLEX_TOKEN","M12_RECOVERY_TOKEN","CART_COLD_TOKEN"].includes(k)||k.startsWith("GIT_CONFIG_")||k.startsWith("PIP_"))delete env[k];
  env.OPENBLAS_NUM_THREADS="1";env.OMP_NUM_THREADS="1";env.GIT_TERMINAL_PROMPT="0";return env;
}
function command(program,args,cwd,log,env){
  if(fs.existsSync(log))throw Error("Fresh subprocess log required");
  const start=Date.now(),fd=fs.openSync(log,"wx");let r;
  try{r=cp.spawnSync(program,args,{cwd,env,stdio:["ignore",fd,fd]});}finally{fs.closeSync(fd);}
  const receipt={command:program,arguments:args,OSExitCode:r.status,signal:r.signal??null,spawnError:r.error?String(r.error):null,
    seconds:(Date.now()-start)/1000,stdoutSHA256:hash(log)};
  emit({event:"independent-consumer-process-returned",...receipt});return receipt;
}
function requireExit(r,label){if(r.OSExitCode!==0||r.signal||r.spawnError)throw Error(label+" actual exit "+r.OSExitCode+" signal "+r.signal);}
function pythonFor(out,prefix,env,receipts){
  const candidates=["python3"],visit=(folder,depth)=>{
    if(depth<0)return;
    for(const e of fs.readdirSync(folder,{withFileTypes:true})){
      if(!e.isDirectory()||e.name.startsWith("source-")||e.name===".git")continue;
      const d=path.join(folder,e.name),p=path.join(d,"bin/python");
      if(e.name.includes("python-env")&&fs.existsSync(p))candidates.unshift(p);
      else if(depth>0&&e.name.endsWith("-work"))visit(d,depth-1);
    }
  };visit(out,2);
  for(let i=0;i<candidates.length;i++){
    const r=command(candidates[i],["-c","import numpy,scipy; assert numpy.__version__=='2.3.5' and scipy.__version__=='1.17.0'; print(numpy.__version__,scipy.__version__)"],out,prefix+".python-probe-"+i+".log",env);
    receipts.push(r);if(r.OSExitCode===0&&!r.signal&&!r.spawnError)return candidates[i];
  }
  const d=prefix+".python-env";if(fs.existsSync(d))throw Error("Fresh pinned Python environment required");
  let r=command("python3",["-m","venv",d],out,prefix+".venv.log",env);receipts.push(r);requireExit(r,"venv");
  const p=path.join(d,"bin/python");
  r=command(p,["-m","pip","--disable-pip-version-check","install","--no-input","numpy==2.3.5","scipy==1.17.0"],out,prefix+".pip.log",env);
  receipts.push(r);requireExit(r,"pinned numerical dependencies");return p;
}
function manifest(p){
  for(let i=0;i<10;i++){try{return JSON.parse(fs.readFileSync(p));}catch(e){if(i===9)throw e;pause(100);}}
}
function git(repo,env,args){
  const r=cp.spawnSync("git",args,{cwd:repo,env,encoding:"utf8",maxBuffer:1048576});
  if(r.status!==0)throw Error("Local git "+args[0]+" failed: "+String(r.stderr||r.error||r.status));return r.stdout;
}
function safeWindow(file,repo,env,runId,epoch){
  const start=Date.now();
  while(true){
    const m=manifest(file),last=m.pulls?.at(-1),age=Date.now()-Date.parse(last?.utc);
    if(String(m.run_id)!==runId||m.source_epochs?.at(-1)?.epoch!==epoch)throw Error("Parent run/source epoch changed");
    if(m.status==="unreviewed_readme_change"||m.failure?.includes("README changed"))throw Error("Unreviewed parent rule change");
    const dirty=git(repo,env,["status","--porcelain","--untracked-files=normal"]);
    if(Number.isFinite(age)&&age>=15000&&age<45*60000-90000&&!dirty.trim()){
      if(fs.existsSync(path.join(repo,".git/rebase-merge"))||fs.existsSync(path.join(repo,".git/rebase-apply")))throw Error("Parent rebase active");
      return {actualLastPullUTC:last.utc,actualLastPullCommit:last.to,ageMilliseconds:age};
    }
    if(Date.now()-start>12*60000)throw Error("No clean parent publication window became available");
    emit({event:"independent-awaiting-parent-clean-pull-window",utc:new Date().toISOString(),lastActualPullUTC:last?.utc??null,worktreeClean:!dirty.trim()});pause(1000);
  }
}
function rejectRaw(v){
  if(!v||typeof v!=="object")return;
  if(!Array.isArray(v))for(const k of ["z","coefficients","parameterVector","gridDefinition"])if(v[k]&&typeof v[k]==="object")throw Error("Raw array in scalar note: "+k);
  for(const x of Object.values(v))rejectRaw(x);
}
function noteFor(r){
  const lines=["# 原 Cauchy 观察之后的独立完整 Cartesian 实验","",
    "**可信度：实际有限数值实验；连续与 reach 未认证，课题未完成。**","",
    "这是同 runner 下游消费。原 Cauchy observer 的模型、状态和计数保留。Cartesian 有独立固定 g、全 13 行目标、系数及接受计数，不能加到 Cauchy 计数。","",
    "- 实际 run: "+r.runId+"；原 Cauchy 已接受数 "+r.originalCauchyAcceptedSteps+"。",
    "- 原状态 SHA-256: "+r.originalCauchyStateSHA256+"。",
    "- 实际原 observer SHA-256: "+r.originalCauchyObserverSHA256+"。",
    "- 冻结 source epoch: "+r.sourceEpoch+"。",
    "- 独立入口 SHA-256: "+r.entrySHA256+"。",
    "- 复合入口 SHA-256: "+r.compositeObserverSHA256+"。",
    "- 实际独立结果: "+r.status+"。",""];
  const q=r.independentScalarReport;
  if(q){
    lines.push("| 独立阶段 | 完整 R² | sample metric | sample κ | held |","|---|---:|---:|---:|---:|",
      ...[["新基线",q.baseline],["末态",q.evaluation],["同场密观察",q.refinedObservation]].map(([n,v])=>
        "| "+[n,v?.squaredNorm,v?.maxRelativeMetric,v?.maxCurvature,v?.minHeldDistance].join(" | ")+" |"),"",
      "独立实际接受数 "+q.ownAcceptedSteps+"；Cauchy 增量 0；完整 "+q.dimension+" 列、"+q.completeRows+" 行。","");
    for(const [n,k] of [["训练","targetGaussianCurvatureTraining"],["密观察","targetGaussianCurvatureRefined"]])
      if(q[k])lines.push(n+"固定 g 采样 max|K_g|="+q[k].maxAbsoluteTargetGaussianCurvature+"，s="+q[k].s+"，signed K_g="+q[k].signedTargetGaussianCurvature+"。");
    lines.push("K_g=-a_ss/a 只作采样必要条件诊断，不作连续界或 LM 验收门。","");
  }
  const fence=String.fromCharCode(96).repeat(3);
  lines.push("以下仅小标量、身份及真实进程回执；raw 和完整系数只在 runner 临时区。","",fence+"json",JSON.stringify(r,null,2),fence,"");
  const text=lines.join("\n");if(Buffer.byteLength(text)>=100000)throw Error("Scalar note exceeds 100KB; raw fallback forbidden");return text;
}
function observe(candidate,input,options={}){
  const d=input?.cartesianDownstream;
  if(d?.schema!==MARKER)return original.forStrongController(candidate,input,options);
  for(const k of ["candidateFile","inputFile","outputFile"])if(typeof options[k]!=="string")throw Error("Actual file path required: "+k);
  const stage=d.sourceStageLabel,name=path.basename(options.outputFile);
  if(![stage+"-current-field.json",stage+"-stalled-current-field.json"].includes(name))return original.forStrongController(candidate,input,options);
  const sourceHash=hash(options.inputFile),candidateHash=hash(options.candidateFile);
  if(!Number.isInteger(input.cauchyAcceptedSteps)||input.cauchyAcceptedSteps<0)throw Error("Actual Cauchy count required");
  const frozen=path.resolve(__dirname,"../../.."),out=path.dirname(frozen),epoch=path.basename(frozen),
    manifestFile=path.join(out,"scalar-run-manifest.json"),m=manifest(manifestFile),live=m.source_epochs?.at(-1),
    runId=String(m.run_id),attempt=String(m.attempt);
  if(m.schema!=="6a65-strong-branch-actions-scalar-manifest-v1"||live?.epoch!==epoch||!/^source-[0-9]{3}$/.test(epoch)||
     !/^[0-9a-f]{40}$/.test(live.commit)||process.env.GITHUB_REPOSITORY!=="Rogerhu12/math-research-public"||
     process.env.GITHUB_RUN_ID!==runId||process.env.GITHUB_RUN_ATTEMPT!==attempt||live.candidate_sha256!==candidateHash)
    throw Error("Actual parent run and frozen source epoch required");
  if(!m.steps?.some(r=>r.stage===stage&&r.output_sha256===sourceHash))throw Error("Parent actual Cauchy attempt receipt required");
  const rel=d.recipeRepoRelative;
  if(typeof rel!=="string"||!/^topics\/visible-flexible-closed-surface\/ci-requests\/6a65-[A-Za-z0-9_.-]+\.json$/.test(rel))throw Error("Frozen topic recipe required");
  const recipe=path.join(frozen,rel);if(hash(recipe)!==d.recipeSHA256)throw Error("Frozen recipe identity changed");
  const start=Date.now(),base=original.forStrongController(candidate,input,{...options,candidateSHA256:candidateHash});
  base.inputs={candidateFile:options.candidateFile,candidateSHA256:candidateHash,inputFile:options.inputFile,inputSHA256:sourceHash,
    scriptSHA256:hash(path.join(__dirname,"6a65-cauchy-same-field-observer-recovered-v2.cjs"))};
  base.elapsedSeconds=(Date.now()-start)/1000;
  const originalFile=options.outputFile+".original-Cauchy.json";write(originalFile,base);
  const prefix=path.join(out,stage+".independent-Cartesian"),entry=path.join(__dirname,ENTRY),env=noCredentials(),receipts=[];
  const receipt={schema:"6a65-independent-Cartesian-composite-consumer-receipt-v2",runId,attempt,
    sourceEpoch:live.commit,sourceEpochDirectory:epoch,originalCauchyStateSHA256:sourceHash,
    originalCauchyObserverSHA256:hash(originalFile),originalCauchyAcceptedSteps:input.cauchyAcceptedSteps,
    originalCauchyStateAndCounterUnchanged:true,acceptedCauchyStepsAddedByThisExperiment:0,
    entrySHA256:hash(entry),compositeObserverSHA256:hash(__filename),recipeSHA256:hash(recipe),
    originalMathematicalObservationSchema:base.mathematicalObservationSchema,
    independentModel:"complete-proper-half-turn-Cartesian-fixed-g",actualProcessReceipts:receipts,
    rawPublished:false,continuousCertificate:false,strongTargetComplete:false};
  try{
    const python=pythonFor(out,prefix,env,receipts);
    const r=command(python,[entry,"--scripts",__dirname,"--candidate",options.candidateFile,"--source",options.inputFile,
      "--observer",originalFile,"--prefix",prefix,"--recipe",recipe,"--source-epoch",live.commit,"--run-id",runId],
      out,prefix+".experiment.log",env);receipts.push(r);receipt.experimentProcess=r;requireExit(r,"Independent Cartesian experiment");
    const reportFile=prefix+"-report.json",q=JSON.parse(fs.readFileSync(reportFile));
    if(q.schema!=="6a65-independent-complete-Cartesian-experiment-scalar-report-v1"||q.originalCauchyStateSHA256!==sourceHash||
       q.originalCauchyObserverSHA256!==hash(originalFile)||q.originalCauchyAcceptedSteps!==input.cauchyAcceptedSteps||
       q.originalCauchyStateAndCounterUnchanged!==true||q.acceptedCauchyStepsAddedByThisExperiment!==0||
       q.entrySHA256!==hash(entry)||q.recipeSHA256!==hash(recipe)||q.sourceEpoch!==live.commit||String(q.runId)!==runId)
      throw Error("Independent actual report does not match unchanged parent identity");
    rejectRaw(q);receipt.independentScalarReport=q;receipt.independentReportSHA256=hash(reportFile);
    receipt.status=q.accepted?"independent_actual_complete_trial_accepted":"independent_actual_attempt_stalled";
  }catch(e){
    receipt.status="independent_experiment_actual_failure";receipt.error=String(e.stack||e);
    const p=prefix+"-failure.json";if(fs.existsSync(p))receipt.independentFailureSHA256=hash(p);
  }
  if(hash(options.inputFile)!==sourceHash||hash(options.candidateFile)!==candidateHash||hash(originalFile)!==receipt.originalCauchyObserverSHA256)
    throw Error("Independent consumer modified original source/observer bytes");
  const repo=path.resolve(process.env.GITHUB_WORKSPACE??"");
  if(!fs.existsSync(path.join(repo,".git"))||git(repo,env,["rev-parse","--show-toplevel"]).trim()!==repo)throw Error("Actual parent checkout required");
  receipt.publicationWindow=safeWindow(manifestFile,repo,env,runId,epoch);
  const note=path.join(repo,TOPIC,"notes","2026-11-26-6a65-independent-Cartesian-"+runId+"-"+attempt+"-"+epoch+".md");
  if(fs.existsSync(note))throw Error("One new independent scalar commit only");
  rejectRaw(receipt);fs.writeFileSync(note,noteFor(receipt));
  const relative=path.relative(repo,note);git(repo,env,["add","--",relative]);
  const staged=git(repo,env,["diff","--cached","--name-only"]).trim().split("\n");
  if(staged.length!==1||staged[0]!==relative)throw Error("Commit contains paths outside its own scalar note");
  git(repo,env,["commit","-m","visible-flex: independent Cartesian actual consumer "+runId+"/"+attempt+" "+epoch,"--",relative]);
  const commit=git(repo,env,["rev-parse","HEAD"]).trim();
  if(git(repo,env,["status","--porcelain","--untracked-files=normal"]).trim())throw Error("Independent scalar commit left dirty checkout");
  const compact={schema:receipt.schema,status:receipt.status,sourceEpoch:live.commit,
    originalCauchyStateSHA256:sourceHash,originalCauchyObserverSHA256:receipt.originalCauchyObserverSHA256,
    originalCauchyAcceptedSteps:input.cauchyAcceptedSteps,originalCauchyStateAndCounterUnchanged:true,
    acceptedCauchyStepsAddedByThisExperiment:0,independentReportSHA256:receipt.independentReportSHA256??null,
    independentOwnAcceptedSteps:receipt.independentScalarReport?.ownAcceptedSteps??null,
    actualExperimentExitCode:receipt.experimentProcess?.OSExitCode??null,scalarNoteRepoRelative:relative,
    scalarNoteSHA256:hash(note),localCommitAwaitingParentPullAndPush:commit,parentPublicationRequired:true,
    continuousCertificate:false,strongTargetComplete:false};
  emit({event:"independent-scalar-local-commit-awaits-parent-publish",...compact});
  return {...base,independentDownstreamExperiment:compact};
}
module.exports={observe,MARKER};
