// Optional exact periodic quadrature reuse; declared N and all original guards retained.
// A complete optional state/variational entry point for the exact same finite
// momentum equations. All called RHS values use the split linear flux.
// Published original factories remain unchanged.
import {createFastMomentumTailEngine} from './f6tail_fast_momentum.mjs';
import {createSplitFluxMomentumTailEngine} from './f6tail_momentum_split_flux.mjs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const periodicSourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!periodicSourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const {integrationGrid}=await import(pathToFileURL(path.join(periodicSourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));

export function createFastSplitFluxMomentumTailEngine(options={}){
  const linearization=createFastMomentumTailEngine(options),
    split=createSplitFluxMomentumTailEngine(options),
    {M,size}=split,Kdim=2*M;
  function rhsWithJacobian(state,profile,x){
    // The reviewed analytic Jacobian is the derivative of the unchanged
    // mathematical projected RHS. Only its floating state evaluation changes.
    const result=linearization.rhsWithJacobian(state,profile,x);
    return {...result,derivative:split.rhs(state,profile,x,false,result.root)};
  }
  function flowStateWithJacobian(initial,segments,opts={}){
    const steps=opts.stepsPerSegment??64;
    let state=Float64Array.from(initial),tangent=new Float64Array(size*Kdim),
      minA=Infinity,minD=Infinity,maxRootRelative=0;
    for(let j=0;j<Kdim;j++)tangent[j*Kdim+j]=1;
    function field(s,t,p,x){
      const f=rhsWithJacobian(s,p,x),dt=new Float64Array(size*Kdim);
      minA=Math.min(minA,f.root.e.minA);minD=Math.min(minD,f.root.e.minD);
      maxRootRelative=Math.max(maxRootRelative,f.root.err/f.root.scale);
      for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
        const z=f.jacobian[i*Kdim+j];for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*t[j*Kdim+k];
      }
      return {ds:f.derivative,dt};
    }
    function increment(s,t,f,h){return {s:Float64Array.from(s,(v,j)=>v+h*f.ds[j]),t:Float64Array.from(t,(v,j)=>v+h*f.dt[j])};}
    for(const p of segments){
      const cuts=p.integrationBreakpoints??[],grid=cuts.length?integrationGrid(steps,cuts):null,
        count=grid?grid.length-1:steps,ordinaryH=1/steps;
      for(let n=0;n<count;n++){
        const h=grid?grid[n+1]-grid[n]:ordinaryH,x=grid?grid[n]:n*ordinaryH,
          a=field(state,tangent,p,x),ab=increment(state,tangent,a,h/2),b=field(ab.s,ab.t,p,x+h/2),
          bc=increment(state,tangent,b,h/2),c=field(bc.s,bc.t,p,x+h/2),cd=increment(state,tangent,c,h),d=field(cd.s,cd.t,p,x+h);
        for(let j=0;j<size;j++)state[j]+=h*(a.ds[j]+2*b.ds[j]+2*c.ds[j]+d.ds[j])/6;
        for(let j=0;j<tangent.length;j++)tangent[j]+=h*(a.dt[j]+2*b.dt[j]+2*c.dt[j]+d.dt[j])/6;
      }
    }
    return {state,tangent,shapeDimension:Kdim,minA,minD,maxRootRelative};
  }
  const unavailable=()=>{throw Error('This optional split engine does not expose legacy flowRawCell; use its explicit rk4 or flowStateWithJacobian.');};
  return {...split,rhsWithJacobian,flowStateWithJacobian,flowRawCell:unavailable,
    rhsEvaluation:'split-linear-flux-v1'};
}
