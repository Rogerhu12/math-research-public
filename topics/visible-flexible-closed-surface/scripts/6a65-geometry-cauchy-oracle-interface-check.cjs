"use strict";
/* Explicit new zero-free-coefficient probe. It is not a CI checkpoint,
 * a complete value baseline, an optimization acceptance, or a good surface. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto"),cp=require("node:child_process");
const [scriptsDirectory,candidateFile,recipeFile,prefix]=process.argv.slice(2);
if(!prefix)throw Error("scripts-dir public-candidate public-recipe fresh-prefix required");
const scripts=path.resolve(scriptsDirectory),sourceFile=path.join(__dirname,"6a65-geometry-cauchy-tail-source.cjs");
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const inputFile=prefix+"-explicit-new-probe.json",reportFile=prefix+"-report.json";
if(fs.existsSync(inputFile)||fs.existsSync(reportFile))throw Error("Fresh interface probe outputs required");
fs.mkdirSync(path.dirname(prefix),{recursive:true});
const start=Date.now(),candidate=JSON.parse(fs.readFileSync(candidateFile)),recipe=JSON.parse(fs.readFileSync(recipeFile));
const branch=require(path.join(scripts,"6a65-cauchy-global-position.cjs"));
const config=JSON.parse(JSON.stringify(recipe.config)),initial=branch.build(candidate,config);
if(!initial.z.every((v,j)=>j===initial.cutHeightIndex||j===initial.amplitudeIndex||v===0))
  throw Error("Declared zero free coefficients were not zero");
const probe={...config,schema:branch.INITIAL,z:Array.from(initial.z),cauchyAcceptedSteps:0,accepted:false,
  interfaceProbeOnly:true,actualValueBaseline:false,actualAcceptedSteps:0,
  construction:"Entirely new zero theta/phi/height/rho coefficients; actual cut-height and tail-amplitude parameters from public recipe.",
  notCICheckpoint:true,noCIValueOrCurvatureInherited:true,
  source:{candidateSHA256:hash(candidateFile),recipeSHA256:hash(recipeFile),entrySHA256:hash(__filename)}};
fs.writeFileSync(inputFile,JSON.stringify(probe)+"\n");
const reader=require(sourceFile),source=reader.createCauchySource(candidate,probe,{scriptsDirectory:scripts,
  identities:{sourceStateSHA256:hash(inputFile),candidateSHA256:hash(candidateFile)}});
const {c,S,cuff,amplitude,Z}=source.metadata,b=c+config.cauchyDesign.rampLength+config.cauchyDesign.coastLength;
const angles=[0,.173,.947,Math.PI/2,2.197,Math.PI,3.641,5.897];
const rows=[0,c,b,b+.037,b+.1234567,S,cuff].map(s=>{
  const a=source.sample(s,angles,true);return {s,radius:a.radius,diagnostics:a.diagnostics,higherJetConsistency:a.higherJetConsistency};
});
const consistency={Xu:0,Xsu:0,Xuu:0,meanPhase:0};
for(const row of rows)for(const key of Object.keys(consistency))
  consistency[key]=Math.max(consistency[key],row.higherJetConsistency[key]);
const norm=x=>Math.hypot(...x),difference=(a,b)=>norm(a.map((x,j)=>x-b[j]));
const join={};for(const key of reader.JETS)join[key]=0;
const flat={};for(const key of reader.JETS)flat[key]=0;
const tail=initial.referenceFactory(amplitude);
for(const u of angles){
  const left=source.packet(S,u,false).jets,right=tail.tailPoint(.8,u,Z).jets;
  for(const key of reader.JETS)join[key]=Math.max(join[key],difference(left[key],right[key]));
  const sn=Math.sin(u),cs=Math.cos(u),at=source.packet(cuff,u,false).jets;
  const exact={X:[.32*cs,.32*sn,Z],Xs:[-cs,-sn,0],Xss:[0,0,0],
    Xu:[-.32*sn,.32*cs,0],Xsu:[sn,-cs,0],Xuu:[-.32*cs,-.32*sn,0]};
  for(const key of reader.JETS)flat[key]=Math.max(flat[key],difference(at[key],exact[key]));
}
const s=b+.1234567,u=.7131234,center=source.packet(s,u,true),FD=[];
for(const h of [2e-4,1e-4]){
  const p2=source.packet(s,u+2*h,true),p1=source.packet(s,u+h,true),
    m1=source.packet(s,u-h,true),m2=source.packet(s,u-2*h,true);
  const errors={};
  for(const [original,derived] of [["Xss","Xssu"],["Xsu","Xsuu"],["Xssu","Xssuu"]]){
    const d=[0,1,2].map(k=>(-p2.jets[original][k]+8*p1.jets[original][k]
      -8*m1.jets[original][k]+m2.jets[original][k])/(12*h));
    errors[derived]={absolute:difference(d,center.jets[derived]),
      relative:difference(d,center.jets[derived])/Math.max(1,norm(center.jets[derived]))};
  }
  FD.push({h,errors});
}
const requests=[{id:"meta",method:"metadata"},{id:"cuff",method:"sample",s:cuff,u:[.173,3.641],deep:false}];
const protocol=cp.spawnSync(process.execPath,["--expose-gc",sourceFile,"serve",scripts,candidateFile,inputFile],
  {input:requests.map(x=>JSON.stringify(x)).join("\n")+"\n",encoding:"utf8",maxBuffer:4*1024*1024});
const answers=protocol.stdout.trim().split("\n").filter(Boolean).map(x=>JSON.parse(x));
if(protocol.status!==0||answers.length!==2||answers.some(x=>!x.ok))throw Error("Actual stdin oracle protocol failed");
const protocolReceipt={actualOSExitCode:protocol.status,responses:answers.map(x=>({id:x.id,ok:x.ok})),
  metadataStateMatches:answers[0].metadata.sourceStateSHA256===hash(inputFile),
  actualCuffRadius:answers[1].radius.a,allSixJetsPresent:reader.JETS.every(k=>Array.isArray(answers[1].jets[k]))};
source.assertUnchanged();
const passed=Object.values(consistency).every(x=>x<2e-10)&&Object.values(join).every(x=>x<2e-9)&&
  Object.values(flat).every(x=>x<2e-12)&&FD.every(row=>Object.values(row.errors).every(e=>e.relative<2e-6))&&
  protocolReceipt.metadataStateMatches&&protocolReceipt.actualCuffRadius===.32&&protocolReceipt.allSixJetsPresent;
const report={schema:"6a65-explicit-new-zero-coefficient-Cauchy-oracle-interface-check-v1",
  interfaceProbeOnly:true,notCICheckpoint:true,actualValueBaselinesComputed:0,actualAcceptedSteps:0,
  source:source.metadata,rows,higherJetNativeConsistency:consistency,actualCutToR205TwoJetDifference:join,
  actualFlatCuffTwoJetDifference:flat,finiteDifferenceProbe:{s,u,rows:FD},protocol:protocolReceipt,
  allDeclaredChecksPassed:passed,inputFile,inputSHA256:hash(inputFile),recipeSHA256:hash(recipeFile),
  sourceFileSHA256:hash(sourceFile),entrySHA256:hash(__filename),seconds:(Date.now()-start)/1000,
  OSExitCode:null,externalExitReceiptRequired:true};
fs.writeFileSync(reportFile,JSON.stringify(report,null,2)+"\n");
process.stdout.write(JSON.stringify({reportFile,reportSHA256:hash(reportFile),passed,seconds:report.seconds,
  sourceFileSHA256:report.sourceFileSHA256,higherJetNativeConsistency:consistency,
  actualCutToR205TwoJetDifference:join,actualFlatCuffTwoJetDifference:flat,finiteDifferenceProbe:report.finiteDifferenceProbe,
  protocol:protocolReceipt})+"\n");
if(!passed)process.exitCode=1;
