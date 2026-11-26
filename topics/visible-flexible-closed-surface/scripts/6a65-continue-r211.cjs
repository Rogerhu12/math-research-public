"use strict";
/* Continue the existing R211 objective from its published input. Only the exact
 * slice cache capacities change; no samples, columns, weights or fields do.
 * Checkpoints are reproducible local outputs, not repository artifacts. */
const fs=require("node:fs"),path=require("node:path");
const {continueR211Branch}=require("./fd2d-run-full-half-quartic-R211.cjs");
const [candidatePath,inputPath,outputPrefix,countText="2",valueLimitText="8",derivativeLimitText="4"]=process.argv.slice(2);
if(!candidatePath||!inputPath||!outputPrefix)throw Error("candidate input output-prefix [count value-cache derivative-cache]");
const input=JSON.parse(fs.readFileSync(inputPath,"utf8"));
const limits={valueLimit:Number(valueLimitText),derivativeLimit:Number(derivativeLimitText)};
const priorCache=input.curvatureOptions?.sliceReuse;
input.curvatureOptions={...input.curvatureOptions,sliceReuse:limits};
input.cacheTransition={prior:priorCache,current:limits,finiteObjectiveChanged:false,mathematicalFieldChanged:false};
const write=(name,data)=>{fs.mkdirSync(path.dirname(name),{recursive:true});fs.writeFileSync(name,JSON.stringify(data)+"\n");};
const status=x=>process.stdout.write(JSON.stringify(x)+"\n");
status({event:"start",cacheLimits:limits,count:Number(countText),time:new Date().toISOString()});
continueR211Branch(JSON.parse(fs.readFileSync(candidatePath,"utf8")),input,Number(countText),{
 runtime:"Node CLI; OS exit is recorded by the supervising process",
 onNormal:r=>status({event:"normal",iteration:r.branchIteration,seconds:r.normalSeconds,R2:r.baseline.squaredNorm,metric:r.baseline.maxRelativeMetric,curvature:r.baseline.curvature?.maxCurvature,memory:process.memoryUsage()}),
 onStep:(s,r)=>{write(outputPrefix+"-"+r.branchIteration+".json",s);status({event:"step",iteration:r.branchIteration,accepted:r.accepted,R2:r.squaredNorm,alpha:r.alpha,metric:r.evaluation?.maxRelativeMetric,curvature:r.evaluation?.curvature?.maxCurvature,seconds:r.elapsedSeconds});}
}).then(s=>{write(outputPrefix+"-final.json",s);status({event:"complete",accepted:s.branchAcceptedSteps,time:new Date().toISOString()});})
.catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
