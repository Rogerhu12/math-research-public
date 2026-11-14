// Same finite linear graph as the verified shared-grid adapter, plus log gains
// from its far input to the *actual nonlinear endpoint*. No graph is changed.
import {advanceLinearColumns} from './closure_linear_stage_graphs.mjs';

let latest=null;
export const getDeepLinearBridge=()=>latest;
function ideal(mode,R,a){
  if(mode===2)return 0;
  const nu=mode*mode*(mode*mode-1)/12,rho=2**a,alpha=1+1/R;
  const t00=1-alpha*nu*R,t10=(-nu*(1+R)+alpha*nu*nu*R)/rho,t11=(1-alpha*nu)/rho;
  const tr=t00+t11,det=1/rho,lambda=.5*(tr-Math.sqrt(tr*tr-4*det));
  return t10/(lambda-t11);
}

export function buildScaledEndpointGraphs(physical,stages,{modes,spacing,linearFar,linearSteps}){
  if(!(linearFar>stages.rawDepth))throw Error('Far input must be deeper than the nonlinear endpoint');
  const rho=2**physical.parameters.a;
  const rows=Array.from({length:modes},(_,j)=>{const mode=spacing*(j+1);return {mode,nu:mode*mode*(mode*mode-1)/12};});
  const graphs=Array.from({length:stages.cells.length+1},()=>new Float64Array(modes));
  const gains=Array.from({length:stages.cells.length},()=>new Float64Array(modes));
  const ys=rows.map(z=>[1,ideal(z.mode,physical.parameters.R,physical.parameters.a)]);
  const logarithmicScale=new Float64Array(modes),selected=[];
  let lastMu=physical.cells[linearFar-1].mu;
  for(let n=linearFar-1;n>=stages.rawDepth;n--){
    const c=physical.cells[n],ratio=lastMu/c.mu;lastMu=c.mu;
    for(const y of ys)y[1]*=ratio;
    advanceLinearColumns(ys,c.profiles,c.mu,rows,linearSteps);
    for(let j=0;j<modes;j++){
      const y=ys[j],norm=Math.hypot(...y);
      if(!(norm>0))throw Error('Zero linear column');
      y[0]/=norm;y[1]/=norm;
      logarithmicScale[j]+=Math.log(norm);
    }
    if(n===stages.rawDepth||n%16===0||n===160||n===192||n===224)
      selected.push({physicalNode:n,mathematicalPort:n-1,
        rows:rows.map((z,j)=>({mode:z.mode,
          normalizedCanonicalColumn:Array.from(ys[j]),
          normalizedRawColumn:[ys[j][0],ys[j][1]/rho],
          logarithmicScale:logarithmicScale[j],
          logAbsoluteQGain:logarithmicScale[j]+Math.log(Math.abs(ys[j][0])),
          rawSlope:ys[j][1]/(rho*ys[j][0])}))});
  }
  for(let j=0;j<modes;j++)graphs.at(-1)[j]=ys[j][1]/(rho*ys[j][0]);
  latest={farPhysicalNode:linearFar,farMathematicalPort:linearFar-1,
    nonlinearPhysicalDepth:stages.rawDepth,nonlinearMathematicalPort:stages.rawDepth-1,
    modes,spacing,linearSteps,endpoint:selected.at(-1),selectedNodes:selected,
    farInitialRows:rows.map(z=>({mode:z.mode,Q:1,rawXi:ideal(z.mode,physical.parameters.R,physical.parameters.a)})),
    scope:'Finite numerical LINEAR transfer between the far input and the actual nonlinear endpoint. Log gain does not certify omitted nonlinear flow, angular tails or radial error.'};
  for(let n=stages.cells.length-1;n>=0;n--){
    const c=stages.cells[n],cols=rows.map((_,j)=>[1,graphs[n+1][j]]);
    advanceLinearColumns(cols,c.profiles,c.mu,rows,Math.max(8,Math.ceil(linearSteps/stages.parts)));
    for(let j=0;j<modes;j++){
      gains[n][j]=cols[j][0];graphs[n][j]=cols[j][1]/(c.portRatio*cols[j][0]);
      if(!Number.isFinite(graphs[n][j])||!Number.isFinite(gains[n][j])||Math.abs(gains[n][j])<=1e-250)
        throw Error('Stage Dirichlet chart vertical at '+n+', mode '+rows[j].mode);
    }
  }
  return {graphs,gains};
}
