// Initial guesses only: put a saved state on a finer shooting grid and/or
// append deeper nodes along the selected finite linear graph. The unchanged
// full nonlinear shooting residual must subsequently be solved.
import {liftRawCheckpoint} from './950f-tail-subdivision.mjs';
import {loadClosingTailSource} from './closing_tail_sources.mjs';
const {splitIntegrationInterval}=await loadClosingTailSource('f6tail_cusp_grid.mjs');
export function remeshCheckpoint(prior,dn,engineFactory){
 const old=prior.parameters,oldDepth=old.physicalDepth??old.depth,newDepth=dn.tail.parameters.physicalDepth;
 const oldParts=old.shootingParts,newParts=dn.tail.parameters.shootingParts,M=dn.tail.parameters.modes,oldM=old.modes,K=2*M;
 if(oldDepth>newDepth)throw Error('This warm remesh only extends physical depth');
 if(old.spacing!==dn.tail.parameters.spacing)throw Error('Warm angular spacing mismatch');
 const rawNode=dn.tail.rawNode,states=Array.from({length:dn.tail.cells.length+1},()=>Array(K).fill(0));
 const copy=(v,to)=>{for(let j=0;j<Math.min(M,oldM);j++){to[j]=v[j];to[M+j]=v[oldM+j];}};
 if(!oldParts){
  const stop=rawNode[oldDepth],shallow={tail:{...dn.tail,cells:dn.tail.cells.slice(0,stop),rawNode:rawNode.slice(0,oldDepth+1),parameters:{...dn.tail.parameters,physicalDepth:oldDepth}}};
  const first=liftRawCheckpoint(prior,shallow,engineFactory);
  for(let i=0;i<first.length;i++)states[i]=first[i];
 }else{
  if(newParts%oldParts!==0)throw Error('Warm remesh requires a refinement by an integral factor');
  const oldRaw=prior.rawNode??Array.from({length:oldDepth+1},(_,n)=>n*dn.tail.physical.cells[0].profiles.length*oldParts);
  if(prior.states.length!==oldRaw.at(-1)+1)throw Error('Warm stage node count mismatch');
  for(let n=0;n<=oldDepth;n++)copy(prior.states[oldRaw[n]],states[rawNode[n]]);
  for(let n=0;n<oldDepth;n++){
   const cell=dn.tail.physical.cells[n],J=cell.profiles.length,engine=engineFactory({modes:oldM,spacing:old.spacing,quadrature:old.quadrature,mu:cell.mu,orientation:1,projectionFloor:old.projectionFloor??.05});
   for(let i=rawNode[n]+1;i<rawNode[n+1];i++){
    const stage=dn.tail.cells[i-1],j=stage.rawSegment,x=stage.rawLeft,z=x*oldParts,nearest=Math.round(z),baseIndex=oldRaw[n]+(J-1-j)*oldParts;
    if(Math.abs(z-nearest)<1e-12){copy(prior.states[baseIndex+oldParts-nearest],states[i]);continue;}
    const part=Math.floor(z),oldStage=baseIndex+oldParts-1-part,a=part/oldParts,h=x-a,base=cell.profiles[j];
    const profile=t=>{const g=base(a+h*t);return {...g,drdx:h*g.drdx,dlogwdx:h*g.dlogwdx};};
    profile.integrationBreakpoints=(base.integrationBreakpoints??[]).filter(v=>v>a&&v<x).map(v=>(v-a)/h);
    let y=new Float64Array(2*oldM+2);y.set(prior.states[oldStage+1]);
    const steps=Math.max(1,Math.ceil(old.steps*oldParts*h));
    for(let k=0;k<steps;k++){
     const xs=splitIntegrationInterval(k/steps,(k+1)/steps,profile.integrationBreakpoints);
     for(let l=0;l<xs.length-1;l++)y=engine.rk4(y,profile,xs[l],xs[l+1]-xs[l]);
    }
    copy(y,states[i]);
   }
  }
 }
 // All appended data are only a linear initial guess, not a nonlinear tail.
 for(let i=rawNode[oldDepth];i<dn.tail.cells.length;i++)for(let j=0;j<M;j++){
  states[i+1][j]=states[i][j]/dn.tail.gains[i][j];
  states[i+1][M+j]=dn.tail.graphs[i+1][j]*states[i+1][j];
 }
 return states;
}
