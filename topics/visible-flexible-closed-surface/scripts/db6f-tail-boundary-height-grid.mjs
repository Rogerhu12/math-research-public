// Numerical grid-design experiment including endpoint curvature layers.
// Samples compare an explicit integrated-Fr interpolant with source height
// two-jets. This is neither an exact ODE nor a continuous C2 certificate.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';
const {positionals,values}=parseArgs({allowPositionals:true,options:{
 'source-root':{type:'string'},'radius':{type:'string',default:'0.5277881139390467'},
 'angular-nodes':{type:'string',default:'512'},'flow-steps':{type:'string',default:'256'},
 'ratios':{type:'string',default:'0.2,0.1,0.05'},'uniform-steps':{type:'string',default:'64,128'}
}});
if(positionals.length!==2||!values['source-root'])throw Error('checkpoint output.json --source-root ROOT required');
const [input,out]=positionals,here=path.dirname(fileURLToPath(import.meta.url)),sourceRoot=path.resolve(values['source-root']);
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const source=name=>pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,name));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(source('f6tail_fast_split_flux_engine.mjs'));
const {withCuspAwareRK}=await import(source('f6tail_cusp_grid.mjs'));
const {createMomentumPhysicalJetEvaluator}=await import(source('f6tail_momentum_physical_jets.mjs'));
const raw=fs.readFileSync(input),rec=JSON.parse((input.endsWith('.gz')?gunzipSync(raw):raw).toString()),response=rec.response??rec,cp=response.checkpoint??response;
const p=cp.parameters,M=p.modes,K=2*M,N=+values['angular-nodes'],flowSteps=+values['flow-steps'],radius=+values.radius;
const factory=createRecalibrationFactory(rec.config??p),physical=factory.assemble(),staged=subdividePhysical(physical,8,p.shootingParts??1);
const index=staged.cells.findIndex(c=>c.profiles[0](0).r<=radius&&radius<=c.profiles[0](1).r);
if(index<0)throw Error('probe radius outside represented stages');
const cell=staged.cells[index],profile=cell.profiles[0],entry=factory.getEntries(cell.rawCell,p.valleyControls[cell.rawCell]??0).entries[cell.rawSegment];
let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});
engine=withCuspAwareRK(engine);
const heightJet=createMomentumPhysicalJetEvaluator(engine,{spacing:p.spacing});
const breaks=profile.integrationBreakpoints??[];
function wx(x){const g=profile(x);return Math.exp(g.logw)*g.dlogwdx;}
const layers=breaks.map((x,k)=>{
 const h=Math.min(1e-5,(x-(breaks[k-1]??0))/8,((breaks[k+1]??1)-x)/8);
 if(!(h>1e-12))return null;
 const g=profile(x),w=Math.exp(g.logw),d2=(wx(x+h)-wx(x-h))/(2*h);
 if(!(Math.abs(d2)>1e-12))return null;
 const scale=6*(1+w*w)**1.5*Math.abs(g.drdx)/Math.abs(d2);
 if(!(scale>1e-12&&scale<1))return null;
 return {x,r:g.r,widthScale:scale,radialSpeed:g.drdx,sourceWxDerivative:d2};
}).filter(Boolean);
// A vanishing endpoint w_x can enter its curvature-limited regime on a
// short scale even without an interior source critical point. These are
// grid proposals only, found from the frozen background itself.
function absoluteMeridionalCurvature(x){
 const g=profile(x),w=Math.exp(g.logw);
 return Math.abs(w*g.dlogwdx/g.drdx)/(1+w*w)**1.5;
}
for(const endpoint of [0,1]){
 const direction=endpoint===0?1:-1,initialCurvature=absoluteMeridionalCurvature(endpoint);
 if(!(initialCurvature<0.5))continue;
 let high=2**-24,low=0;
 while(high<0.5&&absoluteMeridionalCurvature(endpoint+direction*high)<3){low=high;high*=2;}
 if(!(high<=0.5&&absoluteMeridionalCurvature(endpoint+direction*high)>=3))continue;
 for(let k=0;k<45;k++){
  const mid=(low+high)/2;
  if(absoluteMeridionalCurvature(endpoint+direction*mid)<3)low=mid;else high=mid;
 }
 const scale=(low+high)/2,g=profile(endpoint);
 if(scale>1e-10&&scale<0.25)layers.push({x:endpoint,r:g.r,widthScale:scale,
  endpointCurvatureLayer:true,initialCurvature,thresholdCurvature:3,radialSpeed:g.drdx});
}
function grid(S,ratio){
 const a=[0,1,...Array.from({length:S-1},(_,k)=>(k+1)/S),...breaks];
 if(ratio>0)for(const layer of layers){
  for(const direction of [-1,1])for(let k=1;k<10000;k++){
   const x=layer.x+direction*layer.widthScale*Math.expm1(k*ratio);
   if(!(x>0&&x<1))break;
   a.push(x);
  }
 }
 return [...new Set(a)].sort((a,b)=>a-b);
}
function flow(state,a,b){
 let y=Float64Array.from(state);const count=Math.max(1,Math.ceil((b-a)*flowSteps));
 for(let k=0;k<count;k++)y=engine.rk4(y,profile,a+(b-a)*k/count,(b-a)/count);
 return y;
}
function jet(state,x){
 const root=engine.root(state,profile,x),j=heightJet(state,profile,x),g=root.g;
 return {first:g.w*root.e.rows[0].K,second:j.perAngle[0].urr-g.w*g.dlogwdx/g.drdx};
}
function integral(a,b){
 const z=entry.integrate(cell.rawLeft+(cell.rawRight-cell.rawLeft)*a,cell.rawLeft+(cell.rawRight-cell.rawLeft)*b);
 return z[0]+physical.stats.alpha*z[1];
}
function fractionPoint(a,b,L,f){
 let lo=a,hi=b;
 for(let k=0;k<42;k++){const mid=(lo+hi)/2;if(integral(a,mid)<f*L)lo=mid;else hi=mid;}
 return (lo+hi)/2;
}
const sha=x=>createHash('sha256').update(fs.readFileSync(x)).digest('hex');
const report={status:'numerical-endpoint-layer-grid-design-not-a-certificate',input,inputSHA256:sha(input),scriptSHA256:sha(fileURLToPath(import.meta.url)),
 radius,stage:index,rawCell:cell.rawCell,rawSegment:cell.rawSegment,angularNodes:N,flowSteps,nativeCheckpointSteps:p.steps,
 physicalStats:physical.stats,layers,rows:[],scope:'One-stage theta=0 height two-jet interpolation diagnostic; endpoint layers are heuristic background half-curvature scales. The initial CP is fixed; altered local integration grids are not a re-shot boundary solve.'};
const cases=[...values['uniform-steps'].split(',').map(s=>({steps:+s,ratio:0})),...values.ratios.split(',').map(s=>({steps:128,ratio:+s}))];
for(const test of cases){
 const xs=grid(test.steps,test.ratio),start=new Float64Array(K+2);start.set(cp.states[index+1]);
 const states=[start],jets=[jet(start,0)];
 for(let k=1;k<xs.length;k++){states.push(flow(states.at(-1),xs[k-1],xs[k]));jets.push(jet(states.at(-1),xs[k]));}
 let maxFirst=0,maxSecond=0,worst=null;
 for(let k=0;k<xs.length-1;k++){
  const a=xs[k],b=xs[k+1],L=integral(a,b),left=jets[k],right=jets[k+1];
  const xm=fractionPoint(a,b,L,.5),middle=jet(flow(states[k],a,xm),xm).first;
  const u0=left.first,u1=right.first,v0=L*left.second,v1=L*right.second;
  const A=16*middle-8*(u0+u1)-2*(v0-v1),z2=-3*u0+3*u1-2*v0-v1+A,z3=2*u0-2*u1+v0+v1-2*A;
  for(const t of [.25,.5,.75]){
   const x=t===.5?xm:fractionPoint(a,b,L,t),actual=jet(flow(states[k],a,x),x);
   const first=u0+t*(v0+t*(z2+t*(z3+t*A))),second=(v0+t*(2*z2+t*(3*z3+4*t*A)))/L;
   maxFirst=Math.max(maxFirst,Math.abs(first-actual.first));
   const error=Math.abs(second-actual.second);
   if(error>maxSecond){maxSecond=error;worst={x,r:profile(x).r,sourceSecond:actual.second,interpolatedSecond:second,span:[a,b],radialSpan:L};}
  }
 }
 const target=Float64Array.from(states.at(-1));
 for(let j=0;j<K;j++)target[j]=cp.states[index][j]*(j<M?1:cell.portRatio);
 const endpointFirstDefect=Math.abs(jets.at(-1).first-jet(target,1).first);
 const row={...test,nodes:xs.length,maxFirstSampleError:maxFirst,maxSecondSampleError:maxSecond,worst,stageEndpointFirstDefect:endpointFirstDefect};
 report.rows.push(row);fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(row));
}
report.finished=true;fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
