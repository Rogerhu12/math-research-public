"use strict";
/* Actual all-column directional check of the declared curvature objective
 * on the current new position input. No full normal is needed or reused. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const [candidateFile,stateFile,outFile]=process.argv.slice(2);
if(!outFile||fs.existsSync(outFile))throw Error("candidate actual-state fresh-report required");
const input=JSON.parse(fs.readFileSync(stateFile)),candidate=JSON.parse(fs.readFileSync(candidateFile));
const q=require("./6a65-cauchy-global-position.cjs").build(candidate,input),N=input.options.angles,nq=N/2;
const worst=input.evaluation.curvature.worst;
const sites=[{s:worst.s,j:Math.round(worst.u*nq/Math.PI)},{s:.4253125,j:24},{s:.6,j:17}];
const direction=Float64Array.from(q.z,(_,j)=>Math.cos(.73*(j+1))+.31*Math.sin(1.17*(j+1)));
const norm=Math.hypot(...direction);for(let i=0;i<direction.length;i++)direction[i]/=norm;
const rows=[],start=Date.now();
for(const site of sites){
  const packet=q.position.slice(site.s,q.z,true).node(site.j),J=packet.jacobian;
  const analytic=J.map(row=>packet.indices.reduce((v,col,k)=>v+row[k]*direction[col],0));
  q.position.clearSliceReuse?.();if(global.gc)global.gc();
  const estimates=[];
  for(const h of [1e-5,5e-6]){
    const plus=q.z.map((v,j)=>v+h*direction[j]),minus=q.z.map((v,j)=>v-h*direction[j]);
    const pp=q.position.slice(site.s,plus,false).node(site.j),pm=q.position.slice(site.s,minus,false).node(site.j);
    const finite=pp.residual.map((v,k)=>(v-pm.residual[k])/(2*h));
    const absolute=Math.hypot(...finite.map((v,k)=>v-analytic[k]));
    estimates.push({h,absolute,relative:absolute/Math.max(1,Math.hypot(...analytic)),plusCurvature:pp.curvature,minusCurvature:pm.curvature});
    q.position.clearSliceReuse?.();if(global.gc)global.gc();
  }
  rows.push({...site,u:site.j*Math.PI/nq,curvature:packet.curvature,activeColumns:packet.indices.length,
    allColumnDirectionNorm:norm>0?1:0,analyticNorm:Math.hypot(...analytic),estimates});
}
const result={schema:"6a65-actual-Cauchy-curvature-all-column-direction-check-v1",source:{candidateSHA256:hash(candidateFile),
  stateSHA256:hash(stateFile),entrySHA256:hash(__filename),positionSHA256:hash(path.join(__dirname,"6a65-cauchy-global-position.cjs")),
  hingeSHA256:hash(path.join(__dirname,"6a65-explicit-tau-curvature-hinge.cjs"))},curvatureModel:input.curvatureModel,
  tau:input.curvatureTau,rows,seconds:(Date.now()-start)/1000,finiteDirectionalCheckOnly:true,continuousCertificate:false};
fs.writeFileSync(outFile,JSON.stringify(result,null,2)+"\n");process.stdout.write(JSON.stringify(result)+"\n");
