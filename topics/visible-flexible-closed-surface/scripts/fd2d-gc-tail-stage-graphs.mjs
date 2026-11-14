// Same RK columns and graph formulas as 950f-tail-subdivision.mjs.
// Iterate stages before modes so each temporary point cache is discarded
// after one stage. No metric, far graph, node, or scalar column changes.
import {linearColumn} from './950f-tail-subdivision.mjs';
export {linearColumn,subdividePhysical,liftRawCheckpoint} from './950f-tail-subdivision.mjs';
let statistics={};
export function stageGraphStatistics(){return {...statistics};}

function temporaryProfiles(profiles){
  const maps=profiles.map(()=>new Map());
  const wrapped=profiles.map((profile,j)=>{
    const point=x=>{
      const cache=maps[j];
      if(cache.has(x)){statistics.point_cache_hits++;return cache.get(x);}
      const value=profile(x);cache.set(x,value);statistics.point_evaluations++;
      return value;
    };
    point.integrationBreakpoints=profile.integrationBreakpoints;
    return point;
  });
  return {profiles:wrapped,finish(){
    const retained=maps.reduce((s,m)=>s+m.size,0);
    statistics.maximum_temporary_point_values=Math.max(statistics.maximum_temporary_point_values,retained);
  }};
}

function ideal(mode,R,a){
  if(mode===2)return 0;
  const nu=mode*mode*(mode*mode-1)/12,rho=2**a,alpha=1+1/R,
    t00=1-alpha*nu*R,t10=(-nu*(1+R)+alpha*nu*nu*R)/rho,
    t11=(1-alpha*nu)/rho,tr=t00+t11,det=1/rho,
    lambda=.5*(tr-Math.sqrt(tr*tr-4*det));
  return t10/(lambda-t11);
}

export function buildStableStageGraphs(physical,stages,{modes,spacing,linearFar,linearSteps}){
  if(!(linearFar>stages.rawDepth))throw Error('linearFar must be beyond the finite nonlinear tail');
  if(physical.cells.length<linearFar)throw Error('Missing actual physical/source cells before linearFar');
  statistics={modes,raw_depth:stages.rawDepth,linear_far:linearFar,stages:stages.cells.length,
    point_cache_hits:0,point_evaluations:0,maximum_temporary_point_values:0,
    scope:'Storage and traversal only; each independent scalar RK column retains its original operations.'};
  const rho=2**physical.parameters.a,
    graphs=Array.from({length:stages.cells.length+1},()=>new Float64Array(modes)),
    gains=Array.from({length:stages.cells.length},()=>new Float64Array(modes)),
    y=Array.from({length:modes},(_,j)=>[1,ideal(spacing*(j+1),physical.parameters.R,physical.parameters.a)]);
  let lastMu=physical.cells[linearFar-1].mu;
  for(let n=linearFar-1;n>=stages.rawDepth;n--){
    const c=physical.cells[n],cache=temporaryProfiles(c.profiles);
    for(let j=0;j<modes;j++){
      y[j][1]*=lastMu/c.mu;
      y[j]=linearColumn(cache.profiles,c.mu,spacing*(j+1),linearSteps,y[j]);
      const norm=Math.hypot(...y[j]);y[j]=y[j].map(v=>v/norm);
    }
    lastMu=c.mu;cache.finish();
  }
  for(let j=0;j<modes;j++)graphs.at(-1)[j]=y[j][1]/(rho*y[j][0]);
  for(let n=stages.cells.length-1;n>=0;n--){
    const c=stages.cells[n],cache=temporaryProfiles(c.profiles);
    for(let j=0;j<modes;j++){
      const out=linearColumn(cache.profiles,c.mu,spacing*(j+1),
        Math.max(8,Math.ceil(linearSteps/stages.parts)),[1,graphs[n+1][j]]);
      gains[n][j]=out[0];graphs[n][j]=out[1]/(c.portRatio*out[0]);
      if(!(Number.isFinite(graphs[n][j])&&Number.isFinite(out[0])&&Math.abs(out[0])>1e-250))
        throw Error('Stage Dirichlet chart vertical at '+n+', mode '+spacing*(j+1));
    }
    cache.finish();
  }
  return {graphs,gains};
}
