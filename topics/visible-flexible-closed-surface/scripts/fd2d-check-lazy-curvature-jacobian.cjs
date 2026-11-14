"use strict";
async function runLazyCurvatureCheck(req,candidate,onProgress=()=>{}){
 const lazy=req("fd2d-R201-R205-variable-amplitude-lazy-curvature.cjs"),instances=[];
 const alias=name=>name==="fd2d-R201-R205-variable-amplitude-slice-reuse.cjs"?
  {createR201R205AmplitudeProvider:(...args)=>{const p=lazy.createR201R205AmplitudeProvider(...args);instances.push(p);return p;}}:req(name);
 const report=await req("fd2d-check-R201-R205-slice-reuse.cjs").runSliceReuseCheck(alias,candidate,onProgress);
 report.extension="Lazy curvature Jacobian only when caller reads p.jacobian; all complete finite numerical outputs preserved";
 report.lazyJacobianStats=instances.map(p=>p.curvatureJacobianStats());return report;
}
module.exports={runLazyCurvatureCheck};
if(require.main===module){
 const fs=require("node:fs"),[candidatePath,reportPath]=process.argv.slice(2);
 if(!candidatePath||!reportPath||fs.existsSync(reportPath))throw Error("candidate and fresh report required");
 runLazyCurvatureCheck(name=>require("./"+name),JSON.parse(fs.readFileSync(candidatePath,"utf8")))
 .then(r=>{r.runtime="Actual Node invocation; process exit belongs to external receipt";fs.writeFileSync(reportPath,JSON.stringify(r,null,2)+"\n");process.stdout.write(JSON.stringify(r.lazyJacobianStats)+"\n");})
 .catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
