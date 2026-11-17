// Reproduce the literal worker warm initializer, then locate its first
// failing local momentum root. No equation, root guard or solver is changed.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,oldFile,newFile,outFile]=process.argv.slice(2);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const read=p=>JSON.parse(gunzipSync(fs.readFileSync(p)));
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const old=read(oldFile),trial=read(newFile),prior=old.response.checkpoint,cfg=trial.config;
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const {remeshCheckpoint}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-warm-remesh.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,'f6tail_fast_split_flux_engine.mjs')));
const {integrationGrid}=await import(pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,'f6tail_cusp_grid.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,height=trial.request.height,ratio=height[0]/prior.cutHeight[0];
let initial=remeshCheckpoint(prior,dn,createFastSplitFluxMomentumTailEngine);
const harmonic=cfg.harmonicAmplitudePredictor===true&&height.slice(1).every(x=>x===0);
initial=initial.map(row=>row.map((v,j)=>v*(harmonic?ratio**(j%M+1):ratio)));
const r=dn.cutJets(new Float64Array(K)).radius,r4=r**4;
const delta=Float64Array.from(height,(h,j)=>h/r4-initial[0][j]);
const add=dn.tail.initial(delta);
let correctionMaximum={relative:0},maxHeightRoundoff=0;
for(let j=0;j<M;j++)maxHeightRoundoff=Math.max(maxHeightRoundoff,Math.abs(r4*delta[j]));
for(let n=0;n<initial.length;n++){
 const base=Math.max(1e-300,...initial[n].map(Math.abs)),absolute=Math.max(...add[n].map(Math.abs));
 if(absolute/base>correctionMaximum.relative)correctionMaximum={relative:absolute/base,absolute,node:n,base};
}
if(cfg.correctInitialBoundary!==false)initial=initial.map((row,n)=>row.map((v,j)=>v+add[n][j]));
const output={scope:'Finite diagnostic of the exact worker initial guess. No accepted nonlinear tail, no capacity bound.',
 source_sha256:sha(process.argv[1]),old_sha256:sha(oldFile),new_sha256:sha(newFile),ratio,harmonic,
 correctInitialBoundary:cfg.correctInitialBoundary!==false,height_l1:height.reduce((s,x)=>s+Math.abs(x),0),
 max_boundary_correction_in_height:maxHeightRoundoff,maximum_relative_linear_boundary_correction:correctionMaximum,
 M,quadrature:cfg.quadrature,shootingParts:cfg.shootingParts,steps:cfg.steps,completed_stages:0};
const write=()=>fs.writeFileSync(outFile,JSON.stringify(output,null,2)+'\n');
let failedCell=null,failedStage=-1;
for(let n=0;n<dn.tail.cells.length;n++){
 const c=dn.tail.cells[n],state=new Float64Array(K+2);state.set(initial[n+1]);
 try{c.engine.flowStateWithJacobian(state,c.profiles,{stepsPerSegment:cfg.steps});output.completed_stages=n+1;}
 catch(error){failedCell=c;failedStage=n;output.first_failure={stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,
   rawLeft:c.rawLeft,rawRight:c.rawRight,error:String(error)};write();break;}
}
if(failedCell){
 const cell=failedCell,engine=cell.engine;let state=new Float64Array(K+2);state.set(initial[failedStage+1]);
 let failure=null;
 function field(y,p,x,substage,step){
  try{return engine.rhsWithJacobian(y,p,x).derivative;}
  catch(error){failure={y:Float64Array.from(y),profile:p,x,substage,step,error:String(error)};throw error;}
 }
 const increment=(y,dy,h)=>Float64Array.from(y,(v,j)=>v+h*dy[j]);
 try{
  for(const p of cell.profiles){
   const cuts=p.integrationBreakpoints??[],grid=cuts.length?integrationGrid(cfg.steps,cuts):null;
   const count=grid?grid.length-1:cfg.steps;
   for(let n=0;n<count;n++){
    const x=grid?grid[n]:n/cfg.steps,h=grid?grid[n+1]-grid[n]:1/cfg.steps;
    const a=field(state,p,x,'a',n),b=field(increment(state,a,h/2),p,x+h/2,'b',n),
          c=field(increment(state,b,h/2),p,x+h/2,'c',n),d=field(increment(state,c,h),p,x+h,'d',n);
    for(let j=0;j<state.length;j++)state[j]+=h*(a[j]+2*b[j]+2*c[j]+d[j])/6;
   }
  }
 }catch(error){if(!failure)throw error;}
 if(failure){
  const f=failure,g=engine.geometry(f.profile,f.x);
  output.local_failure={x:f.x,substage:f.substage,step:f.step,error:f.error,
   r:g.r,w:g.w,w_r:g.w*g.dlogwdx/g.drdx,E:g.E,
   q_linf:Math.max(...f.y.slice(0,M).map(Math.abs)),p_linf:Math.max(...f.y.slice(M,K).map(Math.abs))};
  const trials=[];let lambda=0,step=.1,L=new Float64Array(M+1),last=null;
  while(lambda<1&&trials.length<200){
   const next=Math.min(1,lambda+step),y=Float64Array.from(f.y,v=>next*v);
   try{
    const rt=engine.root(y,f.profile,f.x,L);
    trials.push({lambda:next,accepted:true,minA:rt.e.minA,minD:rt.e.minD,minS:rt.e.minS,
                 relative_residual:rt.err/rt.scale,iterations:rt.iterations});
    lambda=next;L=rt.L;last=rt;step=Math.min(.1,step*1.5);
   }catch(error){trials.push({lambda:next,accepted:false,error:String(error)});step/=2;if(step<1e-6)break;}
  }
  output.local_state_homotopy={scope:'Original root with an explicitly supplied previous root as initial guess; unchanged D/S/A guards. This addresses this one local state only.',
    reached_lambda:lambda,passed_full_state:lambda===1,last_minA:last?.e.minA??null,
    last_minD:last?.e.minD??null,trials};
 }
}
write();console.log(JSON.stringify({...output,local_state_homotopy:output.local_state_homotopy?{
 ...output.local_state_homotopy,trials_count:output.local_state_homotopy.trials.length,
 trials:output.local_state_homotopy.trials.slice(-4)}:undefined}));
