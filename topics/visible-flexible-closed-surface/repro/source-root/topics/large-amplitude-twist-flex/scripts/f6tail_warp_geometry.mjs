// Smooth finite-prefix slope cap followed by actual radial redistribution, evaluated by adaptive quadrature.
// R is an integral, and dR/dx is its same defining integrand; no inconsistent
// radius/derivative interpolation is used. Deep source profiles are unchanged.
import fs from 'node:fs/promises';import {gunzipSync} from 'node:zlib';
import cells from './general_root_smooth_tail_cells.cjs';
import {createBalancedTail} from './tailnext_balanced_tail.mjs';
const {cellSegments,cellSmooth,cellSmoothDerivative}=cells;
function gauss(n){const x=new Float64Array(n),w=new Float64Array(n);for(let i=0;i<Math.ceil(n/2);i++){let z=Math.cos(Math.PI*(i+.75)/(n+.5)),pp=0;for(let it=0;it<32;it++){let p1=1,p2=0;for(let k=1;k<=n;k++){const p3=p2;p2=p1;p1=((2*k-1)*z*p2-(k-1)*p3)/k;}pp=n*(z*p1-p2)/(z*z-1);const dz=p1/pp;z-=dz;if(Math.abs(dz)<2e-15)break;}const weight=2/((1-z*z)*pp*pp);x[i]=-z;x[n-1-i]=z;w[i]=w[n-1-i]=weight;}return {x,w};}
const G8=gauss(8),G16=gauss(16);
function quad(f,a,b,g){const z=new Float64Array(7),mid=(a+b)/2,h=(b-a)/2;for(let k=0;k<g.x.length;k++){const v=f(mid+h*g.x[k]),weight=h*g.w[k];for(let j=0;j<7;j++)z[j]+=weight*v[j];}return z;}
function integrate(f,a,b,tol=1e-11,depth=0){const lo=quad(f,a,b,G8),hi=quad(f,a,b,G16);let bad=false;for(let j=0;j<7;j++)if(Math.abs(hi[j]-lo[j])>tol*Math.max(Math.abs(hi[j]),1e-280))bad=true;if(!bad||depth>=14)return hi;const mid=(a+b)/2,left=integrate(f,a,mid,tol,depth+1),right=integrate(f,mid,b,tol,depth+1);return Float64Array.from(left,(v,j)=>v+right[j]);}
function kahanAdd(state,value){const y=value-state.c,t=state.s+y;state.c=(t-state.s)-y;state.s=t;}
function poly(c,t,o=0){let z=0;for(let j=c.length-1;j>=o;j--){let a=c[j];for(let k=0;k<o;k++)a*=j-k;z=z*t+a;}return z;}
export function buildWarpGeometryFromSeed(obj,options={}){
 const {seed,scale=1000,curvatureBudget=80,protectCell=224,warpSteps=64,quadratureTolerance=2e-11,calibrationSteps=512,designBeta=0,designControl='left',slopeCap=1.5,capTransition=2,momentumNormalization=1}=options;
 const meta=obj.metadata,epsilon=meta.parameters.epsilon*scale,tailEpsilon=epsilon/(2*meta.parameters.tail.delta0)**meta.parameters.tail.a,W=meta.W,core=obj.profileSegments.filter(s=>s.kind==='core'),oldL=core[0].r0,oldR=core.at(-1).r1,oldMid=core.find(s=>s.cell===1).r0,b=W/curvatureBudget;
 function pieceAt(r){let l=0,h=obj.pieces.length-1;while(l<h){const m=(l+h)>>1;if(obj.pieces[m].r1<r)l=m+1;else h=m;}const p=obj.pieces[l];return {p,t:Math.max(0,Math.min(1,(r-p.r0)/p.L))};}
 function bump(r){const u=(r-oldL)/(oldMid-oldL);return !(u>0&&u<1)?{value:0,radialDerivative:0}:{value:256*u**4*(1-u)**4,radialDerivative:1024*u**3*(1-u)**3*(1-2*u)/(oldMid-oldL)};}
 function controlB(r,rx,control){const L=bump(r),u=(r-oldMid)/(oldR-oldMid),R=!(u>0&&u<1)?{value:0,radialDerivative:0}:{value:256*u**4*(1-u)**4,radialDerivative:1024*u**3*(1-u)**3*(1-2*u)/(oldR-oldMid)};let value,radialDerivative;if(control==='left'){value=L.value;radialDerivative=L.radialDerivative;}else if(control==='right'){value=R.value;radialDerivative=R.radialDerivative;}else if(control==='opposite'){value=L.value-R.value;radialDerivative=L.radialDerivative-R.radialDerivative;}else if(control==='both'){value=L.value+R.value;radialDerivative=L.radialDerivative+R.radialDerivative;}else throw Error('unknown core control');return {value,dx:radialDerivative*rx};}
 const left=createBalancedTail({modes:1,depth:protectCell,steps:1,quadrature:16,epsilonScale:tailEpsilon,rCuff:meta.rInner,orientation:1,calibrationSteps}),right=createBalancedTail({modes:1,depth:protectCell,steps:1,quadrature:16,epsilonScale:tailEpsilon,rCuff:meta.rOuter,orientation:-1,calibrationSteps});
 function capProfile(g){
  if(!(slopeCap>0))return g;
  const c=Math.log(slopeCap),L=capTransition,z=g.logw;
  if(z<=c-L)return g;
  if(z>=c+L)return {...g,uncappedLogw:z,logw:c,dlogwdx:0};
  const t=(z-c+L)/(2*L),u=1-t,S=v=>v**4*(35-84*v+70*v*v-20*v**3),J=v=>v**5*(7-14*v+10*v*v-2.5*v**3),I=t<=.5?t-J(t):.5-J(u),derivative=t<=.5?1-S(t):S(u);
  return {...g,uncappedLogw:z,logw:c-L+2*L*I,dlogwdx:derivative*g.dlogwdx};
 }
 const sourceCore=core.map((s,i)=>({side:'core',cell:null,segment:i,mu:epsilon,source:x=>{const r=s.r0+(s.r1-s.r0)*x,drdx=s.r1-s.r0,{p,t}=pieceAt(r),raw=poly(p.w,t),B=controlB(r,drdx,designControl);return capProfile({r,drdx,logw:Math.log(epsilon*raw)+designBeta*B.value,dlogwdx:poly(p.w,t,1)/p.L/raw*drdx+designBeta*B.dx,chi:1,bump:B.value,bumpDx:B.dx,designB:B.value,designBx:B.dx});}}));
 function tailSources(tail,side){return tail.cells.map(c=>{let offset=0;const segs=cellSegments(c.delta,c.R,c.cal.alpha,tail.parameters.a*Math.log(2),c.c),total=(3+6*c.c)*c.delta;return c.profiles.map((p,j)=>{const len=segs[j].lengthRatio*c.delta,start=offset;offset+=len;return {side,cell:c.n,segment:j,mu:c.mu,source:x=>{const g=p(x),chi=c.n<protectCell-1?1:cellSmooth((start+len*x)/total);return capProfile({...g,chi,bump:0,bumpDx:0});}};});});}
 const sourceLeft=tailSources(left,'left'),sourceRight=tailSources(right,'right'),forward=[];
 for(let n=protectCell-1;n>=0;n--)for(const e of sourceLeft[n])forward.push({...e,original:e,flip:false});
 for(const e of sourceCore)forward.push({...e,original:e,flip:false});
 for(let n=0;n<protectCell;n++)for(let j=sourceRight[n].length-1;j>=0;j--){const e=sourceRight[n][j];forward.push({...e,original:e,flip:true,source:x=>{const g=e.source(1-x);return {...g,drdx:-g.drdx,dlogwdx:-g.dlogwdx,bumpDx:-g.bumpDx};}});}
 let maximumUnwarpedBufferCurvatureTimesW=0;
 const totals=Array.from({length:7},()=>({s:0,c:0})),N=warpSteps;
 for(const e of forward){
  e.integrand=x=>{const g=e.source(x),w=Math.exp(g.logw),wx=w*g.dlogwdx,E=1+w*w,root=Math.sqrt(E),vp=Math.abs(wx/g.drdx)/(E*root),A=g.drdx*(1-g.chi+b*g.chi*vp),B=g.drdx*g.chi/E;if(g.chi<1)maximumUnwarpedBufferCurvatureTimesW=Math.max(maximumUnwarpedBufferCurvatureTimesW,W*vp);return Float64Array.from([A,B,w*A,w*B,root*A,root*B,g.drdx*(1-g.chi)]);};
  e.cumulativeA=new Float64Array(N+1);e.cumulativeB=new Float64Array(N+1);e.total=new Float64Array(7);
  const aSum={s:0,c:0},bSum={s:0,c:0};
  for(let i=0;i<N;i++){const z=integrate(e.integrand,i/N,(i+1)/N,quadratureTolerance);kahanAdd(aSum,z[0]);kahanAdd(bSum,z[1]);e.cumulativeA[i+1]=aSum.s;e.cumulativeB[i+1]=bSum.s;for(let j=0;j<7;j++){e.total[j]+=z[j];kahanAdd(totals[j],z[j]);}}
 }
 const sums=totals.map(z=>z.s),a=(W-sums[0])/sums[1];if(!(a>0))throw Error('Total curvature redistribution consumes the full radial width');
 const cumulative={s:0,c:0},byKey=new Map();
 for(const e of forward){e.newStart=meta.rInner+cumulative.s;e.relativeWidth=e.total[0]+a*e.total[1];const cache=new Map();
  const evaluate=x=>{if(cache.has(x))return cache.get(x);const g=e.source(x),v=e.integrand(x),i=Math.min(N-1,Math.max(0,Math.floor(x*N)));let A,B;if(x<=0){A=0;B=0;}else if(x>=1){A=e.total[0];B=e.total[1];}else{A=e.cumulativeA[i];B=e.cumulativeB[i];if(x>i/N){const z=integrate(e.integrand,i/N,x,quadratureTolerance);A+=z[0];B+=z[1];}}const out={r:e.newStart+A+a*B,drdx:v[0]+a*v[1],logw:g.logw,dlogwdx:g.dlogwdx,oldR:g.r,oldDrdx:g.drdx,chi:g.chi,bump:g.bump,bumpDx:g.bumpDx,designB:g.designB??0,designBx:g.designBx??0};cache.set(x,out);return out;};
  const originalProfile=e.flip?(x=>{const g=evaluate(1-x);return {...g,drdx:-g.drdx,dlogwdx:-g.dlogwdx,oldDrdx:-g.oldDrdx,bumpDx:-g.bumpDx};}):evaluate;
  byKey.set(e.side+':'+e.cell+':'+e.segment,originalProfile);kahanAdd(cumulative,e.relativeWidth);
 }
 const leftCells=left.cells.map(c=>({...c,profiles:c.profiles.map((p,j)=>byKey.get('left:'+c.n+':'+j))})),rightCells=right.cells.map(c=>({...c,profiles:c.profiles.map((p,j)=>byKey.get('right:'+c.n+':'+j))}));
 const baseCore=sourceCore.map(e=>byKey.get('core:null:'+e.segment));
 const coreProfiles=(beta,control=designControl)=>baseCore.map(p=>x=>{const g=p(x),B=controlB(g.oldR,g.oldDrdx,control),correction=beta*B.value-designBeta*g.designB,correctionDx=beta*B.dx-designBeta*g.designBx;return {...g,logw:g.logw+correction,dlogwdx:g.dlogwdx+correctionDx,bump:B.value,bumpDx:B.dx};});
 const rL=baseCore[0](0).r,rR=baseCore.at(-1)(1).r;
 const stats={W,rInner:meta.rInner,rOuter:meta.rOuter,rL,rR,oldL,oldR,epsilon,tailEpsilon,scale,curvatureBudget,protectCell,warpSteps,quadratureTolerance,calibrationSteps,designBeta,designControl,a,Tchi:(sums[0]-sums[6])/b,maximumUnwarpedBufferCurvatureTimesW,heightSpanOverRadialWidth:(sums[2]+a*sums[3])/W,meridianLengthOverRadialWidth:(sums[4]+a*sums[5])/W,radialClosure:meta.rInner+cumulative.s-meta.rOuter,activeSegments:forward.length,definition:'Fixed radial map from designBeta background; later beta changes only the core slope on this same R map.',scope:'Actual fixed background profile evaluation; no nonlinear solution or infinite-tail certification.'};stats.annulusBoundingBoxDiameterOverRadialWidth=Math.hypot(2*meta.rOuter/W,stats.heightSpanOverRadialWidth);stats.slopeCap=slopeCap;stats.capTransition=capTransition;stats.deepCutJetErrors=[];for(const [side,newCells,oldCells] of [['left',leftCells,left.cells],['right',rightCells,right.cells]]){const p=newCells.at(-1).profiles[0](0),q=oldCells.at(-1).profiles[0](0),wp=Math.exp(p.logw),wq=Math.exp(q.logw);stats.deepCutJetErrors.push({side,radius:p.r-q.r,backgroundSlope:wp-wq,backgroundSecond:wp*p.dlogwdx/p.drdx-wq*q.dlogwdx/q.drdx,radialMapDerivative:p.drdx/q.drdx,chi:p.chi});} 
 if(!(momentumNormalization>0))throw Error('positive momentumNormalization required');
 for(const c of [...leftCells,...rightCells])c.mu/=momentumNormalization;
 return {parameters:{...options,...stats,momentumNormalization},stats,leftCells,rightCells,coreProfiles,baseCore,bump,sourceCore,meta,epsilon:epsilon/momentumNormalization,tailEpsilon:tailEpsilon/momentumNormalization,momentumNormalization,linearDeepParameters:left.parameters};
}
export async function createWarpGeometry(options={}){return buildWarpGeometryFromSeed(JSON.parse(gunzipSync(await fs.readFile(options.seed))),options);}
if(process.argv[1]?.endsWith('f6tail_warp_geometry.mjs')){const args=process.argv.slice(2),arg=k=>{const i=args.indexOf(k);return i<0?null:args[i+1]},cfg=JSON.parse(await fs.readFile(arg('--input'),'utf8')),start=Date.now(),g=await createWarpGeometry(cfg);await fs.writeFile(arg('--out'),JSON.stringify({scope:g.stats.scope,parameters:g.parameters,seconds:(Date.now()-start)/1000},null,2)+'\n');console.log(JSON.stringify({...g.stats,seconds:(Date.now()-start)/1000}));}
