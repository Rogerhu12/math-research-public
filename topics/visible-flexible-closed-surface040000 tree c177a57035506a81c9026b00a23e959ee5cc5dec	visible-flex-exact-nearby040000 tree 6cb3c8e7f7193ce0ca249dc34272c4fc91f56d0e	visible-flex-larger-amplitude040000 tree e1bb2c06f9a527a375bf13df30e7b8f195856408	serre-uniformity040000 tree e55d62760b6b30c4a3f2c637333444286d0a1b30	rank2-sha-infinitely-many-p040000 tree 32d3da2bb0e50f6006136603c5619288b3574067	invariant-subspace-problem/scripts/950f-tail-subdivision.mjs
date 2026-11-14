// Numerical multiple-shooting subdivision of one fixed physical tail.
// No geometry, Fourier equation, root, or far boundary is changed here.
import {loadClosingTailSource} from './closing_tail_sources.mjs';
const {splitIntegrationInterval}=await loadClosingTailSource('f6tail_cusp_grid.mjs');
export function linearColumn(profiles,mu,mode,steps,initial){
 let y=initial.slice();const logMu=Math.log(mu),nu=mode*mode*(mode*mode-1)/12,sq12=Math.sqrt(12);
 function rhs(v,g){const lr=Math.log(g.r),a=sq12*g.drdx*Math.exp(logMu-8*lr-g.logw),b=-nu*sq12*g.drdx*Math.exp(6*lr+g.logw-logMu),d=(mode*mode-4)*g.drdx/g.r;return [d*v[0]+a*v[1],b*v[0]-d*v[1]];}
 for(const profile of profiles)for(let k=0;k<steps;k++){
  const xs=splitIntegrationInterval(k/steps,(k+1)/steps,profile.integrationBreakpoints??[]);
  for(let l=0;l<xs.length-1;l++){
   const x=xs[l],h=xs[l+1]-x,a=rhs(y,profile(x)),b=rhs([y[0]+h*a[0]/2,y[1]+h*a[1]/2],profile(x+h/2)),c=rhs([y[0]+h*b[0]/2,y[1]+h*b[1]/2],profile(x+h/2)),d=rhs([y[0]+h*c[0],y[1]+h*c[1]],profile(x+h));
   y=[y[0]+h*(a[0]+2*b[0]+2*c[0]+d[0])/6,y[1]+h*(a[1]+2*b[1]+2*c[1]+d[1])/6];
   if(!y.every(Number.isFinite))throw Error('nonfinite stage linear flow');
  }
 }return y;
}
function ideal(mode,R,a){
 if(mode===2)return 0;
 const nu=mode*mode*(mode*mode-1)/12,rho=2**a,alpha=1+1/R,t00=1-alpha*nu*R,t10=(-nu*(1+R)+alpha*nu*nu*R)/rho,t11=(1-alpha*nu)/rho,tr=t00+t11,det=1/rho,lambda=.5*(tr-Math.sqrt(tr*tr-4*det));
 return t10/(lambda-t11);
}
export function subdividePhysical(physical,rawDepth,parts){
 if(physical.parameters.orientation!==1)throw Error('This numerical subdivision currently supports orientation +1 only');
 if(!(Number.isInteger(parts)&&parts>0))throw Error('Positive integral shootingParts required');
 const rho=2**physical.parameters.a,cells=[],rawNode=[];
 for(let n=0;n<rawDepth;n++){
  rawNode[n]=cells.length;const old=physical.cells[n];
  for(let j=old.profiles.length-1;j>=0;j--)for(let k=parts-1;k>=0;k--){
   const base=old.profiles[j],a=k/parts,b=(k+1)/parts,h=b-a;
   const profile=x=>{const g=base(a+h*x);return {...g,drdx:h*g.drdx,dlogwdx:h*g.dlogwdx};};
   profile.integrationBreakpoints=(base.integrationBreakpoints??[]).filter(x=>x>a&&x<b).map(x=>(x-a)/h);
   cells.push({...old,profiles:[profile],rawCell:n,rawSegment:j,rawLeft:a,rawRight:b,part:k,parts,portRatio:j===old.profiles.length-1&&k===parts-1?rho:1});
  }
 }
 rawNode[rawDepth]=cells.length;
 return {cells,rawNode,rawDepth,parts};
}
export function buildStableStageGraphs(physical,stages,{modes,spacing,linearFar,linearSteps}){
 const rho=2**physical.parameters.a,graphs=Array.from({length:stages.cells.length+1},()=>new Float64Array(modes)),gains=Array.from({length:stages.cells.length},()=>new Float64Array(modes));
 if(!(linearFar>stages.rawDepth))throw Error('linearFar must be beyond the finite nonlinear tail');
 for(let j=0;j<modes;j++){
  const mode=spacing*(j+1);let y=[1,ideal(mode,physical.parameters.R,physical.parameters.a)],lastMu=physical.cells[linearFar-1].mu;
  for(let n=linearFar-1;n>=stages.rawDepth;n--){
   const c=physical.cells[n];y[1]*=lastMu/c.mu;lastMu=c.mu;
   y=linearColumn(c.profiles,c.mu,mode,linearSteps,y);const norm=Math.hypot(...y);y=y.map(v=>v/norm);
  }
  let g=y[1]/(rho*y[0]);graphs.at(-1)[j]=g;
  for(let n=stages.cells.length-1;n>=0;n--){
   const c=stages.cells[n],out=linearColumn(c.profiles,c.mu,mode,Math.max(8,Math.ceil(linearSteps/stages.parts)),[1,g]);
   gains[n][j]=out[0];g=out[1]/(c.portRatio*out[0]);graphs[n][j]=g;
   if(!(Number.isFinite(g)&&Number.isFinite(out[0])&&Math.abs(out[0])>1e-250))throw Error('Stage Dirichlet chart vertical at '+n+', mode '+mode);
  }
 }
 return {graphs,gains};
}

export function liftRawCheckpoint(prior,dn,engineFactory){
 const rawDepth=dn.tail.parameters.physicalDepth,parts=dn.tail.parameters.shootingParts,M=dn.tail.parameters.modes,oldM=prior.parameters.modes,K=2*M,oldK=2*oldM;
 if(prior.states.length!==rawDepth+1)throw Error('Raw checkpoint depth mismatch');
 if(prior.parameters.spacing!==dn.tail.parameters.spacing)throw Error('Raw checkpoint angular spacing mismatch');
 const states=Array.from({length:dn.tail.cells.length+1},()=>Array(K).fill(0)),rawNodes=dn.tail.rawNode,copy=(v,target)=>{const keep=Math.min(oldM,M);for(let j=0;j<keep;j++){target[j]=v[j];target[M+j]=v[oldM+j];}};
 for(let n=0;n<=rawDepth;n++)copy(prior.states[n],states[rawNodes[n]]);
 for(let n=0;n<rawDepth;n++){
  const c=dn.tail.physical.cells[n],engine=engineFactory({modes:oldM,spacing:prior.parameters.spacing,quadrature:prior.parameters.quadrature,mu:c.mu,orientation:1,projectionFloor:prior.parameters.projectionFloor??.05});
  let y=new Float64Array(oldK+2);y.set(prior.states[n+1]);
  for(let i=rawNodes[n+1]-1;i>=rawNodes[n];i--){
   const stage=dn.tail.cells[i],p=stage.profiles[0],steps=Math.max(1,Math.round(prior.parameters.steps/parts));
   for(let k=0;k<steps;k++){
    const xs=splitIntegrationInterval(k/steps,(k+1)/steps,p.integrationBreakpoints??[]);
    for(let l=0;l<xs.length-1;l++)y=engine.rk4(y,p,xs[l],xs[l+1]-xs[l]);
   }
   if(i!==rawNodes[n])copy(y,states[i]);
  }
 }
 return states;
}
