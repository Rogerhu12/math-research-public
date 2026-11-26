"use strict";
/* Recovered source after the 2026-11-26 executor outage.
 * Complete actual parent -> new short Cauchy, earlier .14 inlet, natural
 * perimeter, physical clock, full rho fit, and a genuine value baseline.
 * New source identity. No old lost source hash or local value is inherited.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto"),cp=require("node:child_process");
const branch=require("./6a65-cauchy-global-position.cjs");
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const read=p=>JSON.parse(fs.readFileSync(p));
const write=(p,x)=>fs.writeFileSync(p,JSON.stringify(x,null,2)+"\n");
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const need=(v,m)=>{if(!v)throw Error(m);};
function validateRecipe(r){
  need(r?.schema==="6a65-short-Cauchy-clock-perimeter-transition-recipe-v2","Explicit recovered clock recipe required");
  need(same(r.geometryInput,{oldStart:.14,rawRightLength:.75,releasePhysicalClock:true}),"Explicit earlier inlet and physical clock required");
  need(r.archiveAngles===512&&r.exportAngles===128&&r.normalizationQuadrature===1024,"Declared complete angular grids required");
  need(Number.isInteger(r.nodeHeapMB)&&r.nodeHeapMB>=128&&r.nodeHeapMB<=8192,"Explicit child heap required");
  need(same(r.pythonPackages,{numpy:"2.3.5",scipy:"1.17.0"}),"Known actual Python package versions required");
  const c=r.config,d=c?.cauchyDesign;
  need(c?.baseModel==="short-cauchy-v1"&&d&&d.centralLength===13/128&&d.rampLength===.06&&d.coastLength===.02&&
    d.rightLength===.7956739498716915&&d.v===.05&&d.amplitude===.8746432018013935&&d.cuffHeight===.51,
    "Explicit short prefix, physical clock and retargeted ports required");
  need(c.options?.angles===128&&c.options.gap===1&&c.options.modes===11&&c.options.radialBasisCount===38&&
    Array.isArray(c.options.radialKnots)&&c.options.radialKnots.length===42,"Complete J38 K11 N128 fit required");
  need(c.metricTau===.05&&c.curvatureModel==="6a65-explicit-tau-quartic-curvature-hinge-v1"&&c.curvatureTau===1e6&&
    c.curvatureOptions?.guide===9.5&&c.curvatureOptions.weight===.01&&c.geometryOptions?.weight===10,
    "The entire startup objective must be declared");
  need(c.z===undefined&&c.gapLengthDesign===undefined&&c.peakMetricRows===undefined,"No inherited coefficients, clock or fixed peak objective");
  need(r.physicalDerivativeWeight===.03,"Declared full first-jet fit weight required");
  return r;
}
function validateInputs(candidateFile,inputFile,observerFile,recipeFile){
  const input=read(inputFile),observer=read(observerFile),recipe=validateRecipe(read(recipeFile));
  need(input.schema==="6a65-R219-expanded-peaks-checkpoint-v1"&&input.lowWideCapDesign?.result==="R219"&&
    input.options?.gap===1&&input.gapLengthDesign?.centralSeed&&Array.isArray(input.z),"Actual R219 complete parent required");
  need(input.z.length===input.options.radialBasisCount*(4*input.options.modes+3)+2&&input.z.every(Number.isFinite),"Complete parent vector required");
  need(observer.schema==="6a65-gap-clock-same-field-refined-metric-observation-v1"&&
    observer.inputs?.inputSHA256===hash(inputFile)&&observer.inputs?.candidateSHA256===hash(candidateFile)&&
    observer.dimension===input.z.length&&observer.originalAngularRule===input.options.angles&&
    observer.fieldCoefficientsUnchanged&&observer.physicalMetricUnchanged&&observer.sourceAngularPrimitiveUnchanged,
    "Exact same-state parent observation required");
  return {input,recipe};
}
async function initialize(candidateFile,inputFile,observerFile,prefix,recipeFile){
  const {input,recipe}=validateInputs(candidateFile,inputFile,observerFile,recipeFile);
  const work=path.resolve(prefix+"-work"),output=prefix+"-initial.json",reportFile=prefix+"-report.json";
  const sourceRoot=path.resolve(__dirname,"../../..");
  need(!(work===sourceRoot||work.startsWith(sourceRoot+path.sep)),"Raw data must remain outside the repository");
  need(!fs.existsSync(work)&&!fs.existsSync(output)&&!fs.existsSync(reportFile),"Fresh transition prefix required");
  fs.mkdirSync(work,{recursive:true});
  const begin=Date.now(),startedUTC=new Date().toISOString(),receipts=[];
  const source={inputSHA256:hash(inputFile),observerSHA256:hash(observerFile),candidateSHA256:hash(candidateFile),
    recipeSHA256:hash(recipeFile),transitionEntrySHA256:hash(__filename)};
  const manifestFile=path.join(work,"process-receipts.json");
  const manifest={schema:"6a65-recovered-Cauchy-clock-process-receipts-v2",startedUTC,source,status:"running",receipts,
    actualAcceptedOptimizationSteps:0,continuousCertificate:false};
  const save=()=>write(manifestFile,{...manifest,updatedUTC:new Date().toISOString()});
  const env={...process.env,OPENBLAS_NUM_THREADS:"1",OMP_NUM_THREADS:"1",MKL_NUM_THREADS:"1",PYTHONDONTWRITEBYTECODE:"1"};
  for(const key of Object.keys(env))
    if(["GH_TOKEN","GITHUB_TOKEN","MR_TOKEN","VISIBLE_FLEX_TOKEN","M12_RECOVERY_TOKEN"].includes(key)||
       key.startsWith("GIT_CONFIG_")||key.startsWith("PIP_"))delete env[key];
  async function run(label,command,args,allowFailure=false){
    const start=Date.now(),stdoutFile=path.join(work,label+".stdout.log"),stderrFile=path.join(work,label+".stderr.log");
    const out=fs.openSync(stdoutFile,"wx"),err=fs.openSync(stderrFile,"wx");
    process.stdout.write(JSON.stringify({event:"actual-transition-process-start",label,utc:new Date().toISOString()})+"\n");
    const actual=await new Promise(resolve=>{
      let spawnError=null;
      const child=cp.spawn(command,args,{cwd:work,env,stdio:["ignore","pipe","pipe"]});
      child.stdout.on("data",b=>{fs.writeSync(out,b);process.stdout.write(b);});
      child.stderr.on("data",b=>{fs.writeSync(err,b);process.stderr.write(b);});
      child.on("error",e=>{spawnError=e.message;});
      child.on("close",(exitCode,signal)=>resolve({exitCode,signal,spawnError}));
    });
    fs.closeSync(out);fs.closeSync(err);
    const entry=args.find(a=>typeof a==="string"&&a.startsWith(__dirname));
    const receipt={label,...actual,seconds:(Date.now()-start)/1000,stdoutSHA256:hash(stdoutFile),stderrSHA256:hash(stderrFile),
      executable:path.basename(command),entry:entry?path.basename(entry):null,entrySHA256:entry&&fs.existsSync(entry)?hash(entry):null};
    receipts.push(receipt);save();
    process.stdout.write(JSON.stringify({event:"actual-transition-process-exit",...receipt})+"\n");
    if((actual.exitCode!==0||actual.signal||actual.spawnError)&&!allowFailure)
      throw Error(label+" exited "+actual.exitCode+" signal "+actual.signal+"; no later result is inferred");
    return receipt;
  }
  const entry=n=>path.join(__dirname,n),nodeArgs=["--expose-gc","--max-old-space-size="+recipe.nodeHeapMB,"--max-semi-space-size=4"];
  const node=(label,file,args)=>run(label,process.execPath,[...nodeArgs,entry(file),...args.map(String)]);
  let python=process.env.CAUCHY_PYTHON||"python3";
  save();
  try{
    const probe="import json,sys,numpy,scipy; print(json.dumps({'python':sys.version.split()[0],'numpy':numpy.__version__,'scipy':scipy.__version__})); assert numpy.__version__=='2.3.5' and scipy.__version__=='1.17.0'";
    const checked=await run("python-dependency-probe",python,["-c",probe],true);
    if(checked.exitCode!==0||checked.signal||checked.spawnError){
      need(recipe.bootstrapPythonWhenMissing===true,"Pinned dependencies unavailable and no bootstrap declared");
      const venv=path.join(work,"python-env");
      await run("python-venv-create",python,["-m","venv",venv]);python=path.join(venv,"bin","python");
      await run("python-pinned-dependencies",python,["-m","pip","--isolated","install","--disable-pip-version-check","--no-input",
        "--index-url","https://pypi.org/simple","numpy==2.3.5","scipy==1.17.0"]);
      await run("python-dependency-recheck",python,["-c",probe]);
    }
    const py=(label,file,args)=>run(label,python,[entry(file),...args.map(String)]);
    const archive=path.join(work,"actual-parent-archive");
    await node("actual-parent-archive-512","6a65-geometry-strong-transplant-source.cjs",[candidateFile,inputFile,archive,"archive",512]);
    const archived=read(archive+"-report.json");
    need(archived.sourceStateSHA256===source.inputSHA256&&archived.candidateSHA256===source.candidateSHA256&&
      archived.count===512&&archived.mode==="archive"&&archived.sourceChange.A===recipe.config.cauchyDesign.amplitude&&
      archived.sourceChange.Z===recipe.config.cauchyDesign.cuffHeight&&hash(archived.dataFile)===archived.dataSHA256,
      "Actual archived source or retargeting mismatch");
    const centralSeed=input.gapLengthDesign.centralSeed,seedFile=path.join(work,"actual-central-seed.json");
    need(Math.abs(centralSeed.actualCentralA-archived.actualCentralSupport)<1e-12&&
      Math.abs(centralSeed.actualCentralA-centralSeed.actualCentralB-1)<1e-12,"Actual central seed mismatch");
    write(seedFile,{schema:"6a65-actual-central-seed-for-short-Cauchy-v1",inheritedGapLengthDesign:{centralSeed},source});
    const ramp=path.join(work,"short-Cauchy"),short=path.join(work,"short-complete"),
      earlyArchive=path.join(work,"earlier-source"),early=path.join(work,"earlier-perimeter"),clock=path.join(work,"physical-clock");
    await py("short-real-Cauchy-collect","6a65-geometry-short-cauchy-transplant.py",["collect",seedFile,ramp]);
    await py("short-complete-export","6a65-geometry-short-cauchy-transplant.py",["export",ramp+"-ramp-master.npz",
      ramp+"-coast-master.npz",archive+"-report.json",short,"--angles",128,"--quadrature",1024]);
    await node("actual-earlier-source","6a65-geometry-transplant-early-source.cjs",[candidateFile,inputFile,archive+"-report.json",earlyArchive,.14]);
    const ar=read(earlyArchive+"-report.json");
    need(ar.sourceStateSHA256===source.inputSHA256&&ar.extension?.newLower===.14&&
      ar.extension.oldReportSHA256===hash(archive+"-report.json")&&hash(ar.dataFile)===ar.dataSHA256,"Earlier archive mismatch");
    await py("actual-earlier-natural-perimeter","6a65-geometry-transplant-earlier-inlet.py",[ramp+"-ramp-master.npz",
      ramp+"-coast-master.npz",earlyArchive+"-report.json",short+"-samples.npz",short+"-report.json",early,"--old-start",.14]);
    await py("actual-complete-physical-clock","6a65-geometry-transplant-physical-clock.py",[early+"-samples.npz",early+"-report.json",clock]);
    const clockReport=read(clock+"-report.json"),physical=clockReport.parameters,d=recipe.config.cauchyDesign;
    const expectedCut=d.centralLength+d.rampLength+d.coastLength+d.rightLength;
    need(clockReport.schema==="6a65-complete-earlier14-exact-physical-clock-new-g-v1"&&
      Math.abs(physical.rightLength-d.rightLength)<1e-13&&Math.abs(physical.physicalCut-expectedCut)<1e-13&&
      physical.A===d.amplitude&&physical.Z===d.cuffHeight&&hash(clock+"-samples.npz")===clockReport.outputSHA256,
      "Actual complete geometry differs from the declared finite interval or ports");
    const config=structuredClone(recipe.config);
    config.objectiveTransition={schema:"6a65-recovered-clock-complete-rho-fit-v2",parentStateSHA256:source.inputSHA256,
      parentObserverSHA256:source.observerSHA256,actualParentAcceptedCount:input.r219AcceptedSteps,
      actualGeometrySampleSHA256:clockReport.outputSHA256,physicalMetricChanged:true,completeRhoFirstJetFit:true,
      old84FixedPeakRowsNotPartOfNewObjective:true,noOldNormalReused:true,newOptimizationAcceptedSteps:0};
    const configFile=path.join(work,"actual-new-config.json"),gridFile=path.join(work,"actual-fit-grid.json"),
      referenceFile=path.join(work,"actual-fit-reference.json"),fitFile=path.join(work,"actual-full-fit.json"),
      valueFile=path.join(work,"actual-full-baseline.json");
    write(configFile,config);
    const gridCode=[
      "import sys,json,hashlib,numpy as np",
      "from pathlib import Path",
      "samples,report,config,output=sys.argv[1:]",
      "r=json.loads(Path(report).read_text()); c=json.loads(Path(config).read_text())",
      "assert r['schema']=='6a65-complete-earlier14-exact-physical-clock-new-g-v1'",
      "assert hashlib.sha256(Path(samples).read_bytes()).hexdigest()==r['outputSHA256']",
      "a=np.load(samples,allow_pickle=False); s=a['s']; u=a['u']; cut=r['parameters']['physicalCut']",
      "d=c['cauchyDesign']; expected=sum(d[k] for k in ('centralLength','rampLength','coastLength','rightLength'))",
      "assert abs(cut-expected)<1e-13 and len(u)==c['options']['angles']",
      "s=s[s<=cut+1e-13]; assert s[0]==0 and abs(s[-1]-cut)<1e-13 and np.all(np.diff(s)>0)",
      "assert all(k in a for k in ('f','fs','targetRho','targetRhoFirst'))",
      "assert not Path(output).exists()",
      "Path(output).write_text(json.dumps({'s':s.tolist(),'u':u.tolist()})+'\\n')",
      "print(json.dumps({'actualFitRows':len(s),'angles':len(u),'physicalCut':cut,'newAcceptedSteps':0}))"
    ].join("\n");
    await run("actual-complete-fit-grid",python,["-c",gridCode,clock+"-samples.npz",clock+"-report.json",configFile,gridFile]);
    await node("actual-complete-fit-reference","6a65-cauchy-global-position.cjs",["reference",candidateFile,configFile,referenceFile,gridFile]);
    await py("actual-all-column-rho-fit","6a65-cauchy-global-warm-fit.py",[clock+"-samples.npz",referenceFile,fitFile,
      "--derivative-weight",.03,"--fit-radius"]);
    const fit=read(fitFile);
    need(fit.schema===branch.INITIAL&&fit.cauchyAcceptedSteps===0&&fit.accepted===false&&
      fit.warmFit?.completeRadiusFirstJetFit&&fit.warmFit.zeroRadiusInitial===false&&fit.z.length===1788,"Incomplete actual new fit");
    await node("actual-complete-new-baseline","6a65-cauchy-global-position.cjs",["value",candidateFile,fitFile,valueFile]);
    const initial=read(valueFile);
    need(initial.schema===branch.INITIAL&&initial.cauchyAcceptedSteps===0&&initial.accepted===false&&
      initial.z.length===fit.z.length&&initial.z.every((v,i)=>Object.is(v,fit.z[i]))&&Number.isFinite(initial.baseline?.squaredNorm),
      "Actual baseline must retain every complete fitted coefficient");
    const physicsSource=initial.source;
    initial.source={...physicsSource,...source,calculationInputSHA256:physicsSource.inputSHA256,
      archiveReportSHA256:hash(archive+"-report.json"),earlierArchiveReportSHA256:hash(earlyArchive+"-report.json"),
      earlierPerimeterReportSHA256:hash(early+"-report.json"),actualClockReportSHA256:hash(clock+"-report.json"),
      actualCompleteFitSHA256:hash(fitFile)};
    need(initial.source.entrySHA256===hash(entry("6a65-cauchy-global-position.cjs")),"Actual physics source must remain identified");
    initial.cauchyInitialization={actualCentralSeed:centralSeed,explicitSourceRetargeting:archived.sourceChange,
      completePhysicalClockReleased:true,actualParentConsumed:true,actualAcceptedOptimizationSteps:0,
      noLostLocalArrayOrSourceIdentityReused:true};
    initial.execution={...initial.execution,transitionStartedUTC:startedUTC,transitionEndedUTC:new Date().toISOString(),
      transitionSeconds:(Date.now()-begin)/1000,actualNormalEvaluations:0,actualAcceptedSteps:0};
    write(output,initial);
    manifest.status="complete_actual_new_baseline_zero_LM_steps";manifest.initialSHA256=hash(output);save();
    const report={schema:"6a65-recovered-Cauchy-clock-new-baseline-receipt-v2",source,initialSHA256:hash(output),
      processReceiptsSHA256:hash(manifestFile),receipts,actualDesign:initial.actualDesign,warmFit:initial.warmFit,
      sourceArchiveReportSHA256:hash(archive+"-report.json"),actualClockReportSHA256:hash(clock+"-report.json"),
      completeFitSHA256:hash(fitFile),freshCompleteBaseline:initial.baseline,dimension:initial.z.length,
      seconds:(Date.now()-begin)/1000,acceptedOptimizationStep:false,physicalMetricChanged:true,
      continuousCertificate:false,strongTargetComplete:false};
    write(reportFile,report);
    process.stdout.write(JSON.stringify({event:"actual-Cauchy-clock-transition-complete",initialSHA256:hash(output),
      reportSHA256:hash(reportFile),dimension:initial.z.length,R2:initial.baseline.squaredNorm,
      metric:initial.baseline.maxRelativeMetric,curvature:initial.baseline.curvature.maxCurvature,
      accepted:false,seconds:report.seconds})+"\n");
    return {initial,report};
  }catch(error){manifest.status="actual_subprocess_or_identity_failure";manifest.failure=String(error.stack||error);save();throw error;}
}
module.exports={validateRecipe,validateInputs,initialize};
if(require.main===module){
  const args=process.argv.slice(2);
  need(args.length===5,"candidate actual-R219-state same-state-observer fresh-prefix recipe required");
  initialize(...args.map(p=>path.resolve(p))).catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
