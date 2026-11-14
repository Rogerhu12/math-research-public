// Independent physical (height, radial-height-slope) projective recovery.
// This does not call buildStableStageGraphs or its momentum propagation.
import fs from 'node:fs';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {loadClosingTailSource} from './closing_tail_sources.mjs';
const {splitIntegrationInterval}=await loadClosingTailSource('f6tail_cusp_grid.mjs');
const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const request=JSON.parse(fs.readFileSync(process.argv[3],'utf8'));
const start=Date.now(),tail=createRecalibrationFactory(cfg).assemble();
const mode=2,scale=mode*mode/cfg.rCut,far=tail.cells[cfg.linearFar-1].profiles[0](0);
function compute(steps){
 let y=[1,mode*mode/(far.r*scale)],lognorm=0;const nodes=[];
 function normalize(){const norm=Math.hypot(...y);y=y.map(v=>v/norm);lognorm+=Math.log(norm);}
 function rhs(v,g){return [g.drdx*scale*v[1],-g.dlogwdx*(v[1]-mode*mode*v[0]/(g.r*scale))];}
 normalize();
 for(let n=cfg.linearFar-1;n>=0;n--){
  const cell=tail.cells[n];
  for(let j=0;j<cell.profiles.length;j++){
   const profile=cell.profiles[j];
   for(let k=0;k<steps;k++){
    const x0=k/steps;
    if(n<cfg.depth&&(k===0||k===steps/2)){
     const part=k===0?0:1,stage=n*cell.profiles.length*2+(cell.profiles.length-1-j)*2+(1-part),g=profile(x0);
     nodes.push({stage,rawCell:n,rawSegment:j,part,r:g.r,w:Math.exp(g.logw),mu:cell.mu,
      unit_height:y[0],unit_slope:scale*y[1],lognorm});
    }
    const xs=splitIntegrationInterval(x0,(k+1)/steps,profile.integrationBreakpoints??[]);
    for(let z=0;z<xs.length-1;z++){
     const x=xs[z],h=xs[z+1]-x,g0=profile(x),gm=profile(x+h/2),g1=profile(x+h),a=rhs(y,g0),
      b=rhs(y.map((v,j)=>v+h*a[j]/2),gm),c=rhs(y.map((v,j)=>v+h*b[j]/2),gm),d=rhs(y.map((v,j)=>v+h*c[j]),g1);
     y=y.map((v,j)=>v+h*(a[j]+2*b[j]+2*c[j]+d[j])/6);normalize();
    }
   }
  }
 }
 const cutoff=y[0],cutlog=lognorm;
 const rows=nodes.map(q=>{
  const factor=request.height[0]*Math.exp(q.lognorm-cutlog)/cutoff;
  const f=factor*q.unit_height,fr=factor*q.unit_slope,
   P=-mode*f/(q.r*q.w),Pt=mode*P,L=(fr-mode*mode*f/q.r)/q.w;
  return {stage:q.stage,rawCell:q.rawCell,rawSegment:q.rawSegment,part:q.part,r:q.r,w:q.w,
   height:f,slope:fr,Q:f/q.r**4,pi:cfg.orientation*q.r**4*q.w*(fr-mode*mode*f/q.r)/(Math.sqrt(12)*q.mu),
   P,Pt,L,physical_angular_gradient:mode*f/q.r,physical_slope_perturbation:fr-mode*mode*f/q.r};
 }).sort((a,b)=>a.stage-b.stage);
 function maximum(key){return rows.reduce((a,b)=>Math.abs(a[key])>Math.abs(b[key])?a:b);}
 return {steps,cutSlope:scale*y[1]/y[0],cutLogGain:lognorm+Math.log(Math.abs(y[0])),
  maxL:maximum('L'),maxP:maximum('P'),maxHeight:maximum('height'),maxSlope:maximum('slope'),rows};
}
const a=compute(256),b=compute(512);
const compare={L_absolute:Math.max(...a.rows.map((r,i)=>Math.abs(r.L-b.rows[i].L))),
 height_absolute:Math.max(...a.rows.map((r,i)=>Math.abs(r.height-b.rows[i].height))),
 slope_absolute:Math.max(...a.rows.map((r,i)=>Math.abs(r.slope-b.rows[i].slope)))};
const report={scope:'Two finite physical-line projective computations, independent of the momentum Riccati initializer; not a nonlinear branch or interval certificate.',
 height:request.height[0],mode,coarse:a,fine:b,compare,seconds:(Date.now()-start)/1000};
fs.writeFileSync(process.argv[4],JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({cutSlope:b.cutSlope,maxL:b.maxL.L,maxP:b.maxP.P,maxPhysicalHeight:b.maxHeight.height,
 maxPhysicalSlope:b.maxSlope.slope,compare,seconds:report.seconds}));
