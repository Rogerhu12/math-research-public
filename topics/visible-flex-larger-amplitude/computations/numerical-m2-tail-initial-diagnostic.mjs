// Locate failure of an actual nonlinear RK evaluation of a linear initial guess.
// This diagnoses a warm state only and does not assert a solved tail.
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const [sourceTopic,configFile,heightFile,outputFile,scaleArg='0.015625']=process.argv.slice(2);
const sourceRoot=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(sourceTopic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(sourceTopic,'scripts/db6f-prefix-tail-shared-split.mjs')));
const config=JSON.parse(fs.readFileSync(configFile,'utf8')),input=JSON.parse(fs.readFileSync(heightFile,'utf8'));
const M=config.modes,K=2*M,scale=Number(scaleArg),height=input.full_prefix_target_height??input.full_target_height;
const physical=createRecalibrationFactory(config).assemble(),dn=createSplitFluxCompactTailDN({...config,tail:physical});
const target=Float64Array.from({length:M},(_,j)=>(height[j]??0)*scale**(j+1)/config.rCut**4);
const states=dn.tail.initial(target),result={scope:'Actual nonlinear evaluation of the finite linear warm state only.',modes:M,scale,physicalDepth:config.depth,parts:config.shootingParts,steps:config.steps,quadrature:config.quadrature,stages:dn.tail.cells.length,passed:0,failure:null};
const maximum=a=>Math.max(...Array.from(a,Math.abs));
function pointDiagnostic(cell,state,profile,x){
 const g=cell.engine.geometry(profile,x),Q=state.slice(0,M),L=Float64Array.from({length:M+1},(_,j)=>j?cell.engine.orientation*Math.sqrt(6)*cell.engine.mu*state[M+j-1]/(g.r**4*g.w2):0);
 let pMax=0,ptMax=0,lMax=0,minD=Infinity,minS=Infinity,minA=Infinity;
 for(let k=0;k<config.quadrature;k++){
  const t=2*Math.PI*k/config.quadrature;let P=0,Pt=0,Lv=0;
  for(let j=0;j<M;j++){const m=2*(j+1),p=-m*g.r**3*Q[j]/g.w;P+=p*Math.sin(m*t);Pt+=m*p*Math.cos(m*t);Lv+=Math.sqrt(2)*L[j+1]*Math.cos(m*t);}
  const K=Lv-Pt,T=2*K+K*K+g.E*P*P;minD=Math.min(minD,1-g.w2*T);minS=Math.min(minS,1-g.w2*P*P);minA=Math.min(minA,1+Lv+g.w2*Pt);pMax=Math.max(pMax,Math.abs(P));ptMax=Math.max(ptMax,Math.abs(Pt));lMax=Math.max(lMax,Math.abs(Lv));
 }
 let directRoot;
 try{const r=cell.engine.root(state,profile,x);directRoot={success:true,relativeResidual:r.err/r.scale,iterations:r.iterations,minD:r.e.minD,minS:r.e.minS,minA:r.e.minA};}
 catch(error){directRoot={success:false,error:String(error)};}
 return {w:g.w,mu:cell.engine.mu,Qmax:maximum(Q),momentumMax:maximum(state.slice(M,K)),pMax,ptMax,initialLMax:lMax,initialMinD:minD,initialMinS:minS,initialMinA:minA,directRoot};
}
result.source_sha256=Object.fromEntries([configFile,heightFile,...['scripts/closing_weighted_tail.mjs','scripts/db6f-prefix-tail-shared-split.mjs','scripts/db6f-prefix-tail-shared-core.mjs','repro/source-root/topics/large-amplitude-twist-flex/scripts/general_root_tail_momentum.mjs','repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs'].map(n=>path.join(sourceTopic,n))].map(n=>[n,crypto.createHash('sha256').update(fs.readFileSync(n)).digest('hex')]));
const start=Date.now();
outer:for(let n=0;n<dn.tail.cells.length;n++){
 const cell=dn.tail.cells[n];let state=new Float64Array(K+2);state.set(states[n+1]);
 for(let j=0;j<cell.profiles.length;j++){
  const profile=cell.profiles[j];
  for(let k=0;k<config.steps;k++){
   try{state=cell.engine.rk4(state,profile,k/config.steps,1/config.steps);}
   catch(error){const g=profile(k/config.steps);result.failure={stage:n,rawCell:cell.rawCell??null,rawSegment:cell.rawSegment??null,subProfile:j,step:k,x:k/config.steps,r:g.r,logw:g.logw,state_max:maximum(state),start_state_max:maximum(states[n+1]),target_state_max:maximum(states[n]),error:String(error),point:pointDiagnostic(cell,state,profile,k/config.steps),failed_state:Array.from(state),initial_state:Array.from(states[n+1])};break outer;}
  }
 }
 result.passed++;
}
result.seconds=(Date.now()-start)/1000;fs.writeFileSync(outputFile,JSON.stringify(result,null,2)+'\n');
const failure=result.failure?Object.fromEntries(Object.entries(result.failure).filter(([k])=>!k.endsWith('_state'))):null;
const {source_sha256,...brief}=result;console.log(JSON.stringify({...brief,failure}));
