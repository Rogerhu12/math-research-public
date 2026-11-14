"use strict";
async function runR210GuideCheck(req,candidate){
 const start=Date.now(),e=req("fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187();
 const spl=req("fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines();
 const options={radialBasisCount:3,radialKnots:spl.uniformKnots(3),modes:2,angles:32,gap:.8,radiusCoefficientBound:.4};
 const m=req("fd2d-nonuniform-metric-provider-R196.cjs").createR196MetricProvider(e,candidate,options,spl);
 const ref=A=>req("fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference(e,m.base,{amplitude:A,angles:32});
 const p=req("fd2d-R201-R205-variable-amplitude-lazy-curvature.cjs").createR201R205AmplitudeProvider(e,m,ref,{guide:9.5,weight:.01,nodeShare:.5},req("fd2d-position-curvature-chain-R191.cjs").createR191Algebra());
 const g=req("fd2d-R210-amplitude-height-allowance-geometric-guide.cjs").createR210AmplitudeGeometryProvider(p,{radius:1.59,width:.84,held:.65,weight:10,nodeShare:.5,cutWindow:[.41,.60]});
 const n=p.dimension,cut=m.definition.stateLayout.cutHeight,z=Array.from({length:n},(_,i)=>.0003*Math.sin((i+1)*.71));
 z[cut]=.56-m.base.height;z[p.amplitudeIndex]=.25;
 const direction=Float64Array.from({length:n},(_,i)=>.003*Math.cos((i+1)*.37));
 const normal=g.penalty(z,{jacobian:true,residuals:true,direction});
 const epsilon=1e-5,plus=z.map((v,i)=>v+epsilon*direction[i]),minus=z.map((v,i)=>v-epsilon*direction[i]);
 const vp=g.penalty(plus,{residuals:true}),vm=g.penalty(minus,{residuals:true});
 let diff2=0,scale2=0,maxDiff=0,rJ=0,j2=0,dg=0,dHd=0;
 for(let i=0;i<normal.jvp.length;i++){
  const fd=(vp.residuals[i]-vm.residuals[i])/(2*epsilon),d=fd-normal.jvp[i];
  diff2+=d*d;scale2+=normal.jvp[i]**2;maxDiff=Math.max(maxDiff,Math.abs(d));rJ+=normal.residuals[i]*normal.jvp[i];j2+=normal.jvp[i]**2;
 }
 for(let i=0;i<n;i++){dg+=direction[i]*normal.g[i];for(let j=0;j<n;j++)dHd+=direction[i]*normal.H[i*n+j]*direction[j];}
 const jvpRelative=Math.sqrt(diff2/scale2),gradientRelative=Math.abs(dg-rJ)/Math.max(1e-30,Math.abs(rJ)),normalRelative=Math.abs(dHd-j2)/Math.max(1e-30,j2);
 if(jvpRelative>1e-6||gradientRelative>1e-10||normalRelative>1e-10)throw Error("R210 complete actual chain mismatch "+JSON.stringify({jvpRelative,gradientRelative,normalRelative}));
 const synth=[];
 for(const r of [.50,.52,.53,.54,.56])for(const sign of [-1,1]){
  const Z=m.base.height+z[cut],allowance=g.heightAllowanceAtRadius(r),X=[r,0,sign*(Z+allowance.value+.007)],indices=[0,cut,p.amplitudeIndex];
  const variations=[[.7,-.4,.2],[.13,.02,.4],[-.2,.3,.1]],ds=[.01,-.02,.03],packet={jets:{X},indices,parameterJets:variations.map(X=>({X}))};
  const a=g.constraints(packet,z,true),dX=[0,1,2].map(k=>variations.reduce((v,row,j)=>v+row[k]*ds[j],0));
  const zz=s=>{const q=Array.from(z);for(let j=0;j<indices.length;j++)q[indices[j]]+=s*epsilon*ds[j];return q;};
  const p1=g.constraints({jets:{X:X.map((v,k)=>v+epsilon*dX[k])},indices:[]},zz(1),false);
  const p0=g.constraints({jets:{X:X.map((v,k)=>v-epsilon*dX[k])},indices:[]},zz(-1),false);
  let err=0;
  for(let row=0;row<7;row++){let d=0;for(let j=0;j<a.indices.length;j++){const at=indices.indexOf(a.indices[j]);if(at>=0)d+=a.jacobian[row][j]*ds[at];}err=Math.max(err,Math.abs((p1.residual[row]-p0.residual[row])/(2*epsilon)-d));}
  if(err>1e-8)throw Error("R210 cylindrical/height synthetic chain mismatch");
  synth.push({cylindricalRadius:r,sign,allowance:allowance.value,radialDerivative:allowance.first,maximumJVPError:err});
 }
 return {schema:"fd2d-R210-height-allowance-complete-chain-check-v1",runtime:"actual pure V8; no OS child or exit",
  options,geometryDefinition:g.definition.geometry,z,direction:Array.from(direction),dimension:n,
  actualGeometryRows:normal.rowCount,actualGeometrySquaredNorm:normal.squaredNorm,
  epsilon,jvpRelative,maxJVPAbsoluteError:maxDiff,gradientDirectionalRelativeError:gradientRelative,normalQuadraticRelativeError:normalRelative,
  syntheticBothSignsAndTransitionEndpoints:synth,fullCutAndAmplitudeColumnsIncluded:true,
  oldPhysicalFieldAndMetricUnchanged:true,newCompleteR210CapsRequired:true,
  actualLMOrLargeNormalRun:false,continuousCoreCertificate:false,strongTargetComplete:false,seconds:(Date.now()-start)/1000};
}
module.exports={runR210GuideCheck};
if(require.main===module){
 const fs=require("node:fs"),[candidatePath,reportPath]=process.argv.slice(2);
 if(!candidatePath||!reportPath||fs.existsSync(reportPath))throw Error("candidate and fresh report required");
 runR210GuideCheck(name=>require("./"+name),JSON.parse(fs.readFileSync(candidatePath,"utf8")))
 .then(r=>{r.runtime="Actual Node invocation; exit belongs to external receipt";fs.writeFileSync(reportPath,JSON.stringify(r,null,2)+"\n");process.stdout.write(JSON.stringify({jvp:r.jvpRelative,seconds:r.seconds})+"\n");})
 .catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
