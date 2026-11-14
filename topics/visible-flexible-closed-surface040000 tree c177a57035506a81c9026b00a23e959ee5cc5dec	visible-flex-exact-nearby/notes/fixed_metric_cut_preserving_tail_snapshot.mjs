// Derived for visible-flex on 2026-11-09 from source SHA256 c2a282deb622141cb05554a4a0910dd0a9a57cd7948ecab02917ae5c13d40bf5.
// Compact actual tail: R8 shallow cells, exact R64 deep source, and an
// integral-defined finite curvature redistribution. No infinite-tail claim.
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const sourceDir=process.env.VISIBLE_FLEX_SOURCE_ROOT
  ?path.resolve(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts')
  :fileURLToPath(new URL('../../large-amplitude-twist-flex/scripts/',import.meta.url));
const sourceImport=name=>import(pathToFileURL(path.join(sourceDir,name)));
const {createBalancedTail}=await sourceImport('tailnext_balanced_tail.mjs');
const {createRejoinedBalancedTail,rejoinedTailLength}=await sourceImport('f6tail_r20_rejoin_source.mjs');
const {default:cells}=await sourceImport('general_root_smooth_tail_cells.cjs');
const {rawLogSlopeCriticalPoints,splitIntegrationInterval}=await sourceImport('f6tail_cusp_grid.mjs');
// Derivation: the old cap is restored to the exact raw cut on the final
// transition. No old DN or finite-cell calibration is reused as a certificate.
function cutPreservingCap(g,slopeCap,transition,n,j,last,x){
  if(n!==0 || j<last-1)return cap(g,slopeCap,transition);
  if(j===last)return g;
  const c=cap(g,slopeCap,transition),eta=1-cells.cellSmooth(x),
        deta=-cells.cellSmoothDerivative(x);
  return {...g,logw:g.logw+eta*(c.logw-g.logw),
    dlogwdx:g.dlogwdx+eta*(c.dlogwdx-g.dlogwdx)+deta*(c.logw-g.logw)};
}
function generalCriticalPoints(profile){
  const roots=[],N=128;let a=0,fa=profile(0).dlogwdx;
  for(let k=1;k<=N;k++){
    let b=k/N,fb=profile(b).dlogwdx;
    if(fa*fb<0){let lo=a,hi=b,flo=fa;for(let it=0;it<52;it++){
      const mid=(lo+hi)/2,fm=profile(mid).dlogwdx;
      if(flo*fm<=0)hi=mid;else{lo=mid;flo=fm;}}
      roots.push((lo+hi)/2);}
    if(fb===0&&fa!==0&&b<1)roots.push(b);
    a=b;fa=fb;
  }
  return [...new Set(roots)];
}
const smooth=cells.cellSmooth;
function gauss(n){const x=[],w=[];for(let i=0;i<n;i++){let z=Math.cos(Math.PI*(i+.75)/(n+.5)),pp=0;for(let it=0;it<40;it++){let p=1,q=0;for(let k=1;k<=n;k++){const a=q;q=p;p=((2*k-1)*z*q-(k-1)*a)/k;}pp=n*(z*p-q)/(z*z-1);const dz=p/pp;z-=dz;if(Math.abs(dz)<2e-15)break;}x.push(z);w.push(2/((1-z*z)*pp*pp));}return {x,w};}
const G8=gauss(8),G16=gauss(16);
function quadrature(f,a,b,G){const out=new Float64Array(6),h=(b-a)/2,m=(a+b)/2;for(let k=0;k<G.x.length;k++){const y=f(m+h*G.x[k]);for(let j=0;j<6;j++)out[j]+=h*G.w[k]*y[j];}return out;}
function integrate(f,a,b,tol,depth=0){const x=quadrature(f,a,b,G8),y=quadrature(f,a,b,G16);if(depth>=16||y.every((v,j)=>Math.abs(v-x[j])<=tol*Math.max(1e-200,Math.abs(v))))return y;const m=(a+b)/2,l=integrate(f,a,m,tol,depth+1),r=integrate(f,m,b,tol,depth+1);return l.map((v,j)=>v+r[j]);}
function cap(g,slopeCap,transition){if(!(slopeCap>0))return g;const c=Math.log(slopeCap),z=g.logw,L=transition;if(z<=c-L)return g;if(z>=c+L)return {...g,logw:c,dlogwdx:0};const t=(z-c+L)/(2*L),u=1-t,S=v=>v**4*(35-84*v+70*v*v-20*v**3),J=v=>v**5*(7-14*v+10*v*v-2.5*v**3),I=t<=.5?t-J(t):.5-J(u),d=t<=.5?1-S(t):S(u);return {...g,logw:c-L+2*L*I,dlogwdx:d*g.dlogwdx};}
export function createCutPreservingTail(options={}){
 const cuspAwareQuadrature=options.cuspAwareQuadrature===true;
 const {rCut=1.03,wCut=.05,width=.04,curvatureBound=210,delta0=.006,R=64,a=2.75,etaPower=1.5,etaRatioAtN0=.05,orientation=-1,prefixR=8,prefixEnd=15,prefixReturnStart=8,protectCell=80,calibrationSteps=1024,warpSteps=16,quadratureTolerance=2e-11,slopeCap=0,capTransition=2,valleyControls=[],rejoinR20At=null,rejoinIndexOffset=4}=options;
 if(!(rCut>width&&wCut>0&&width>0&&curvatureBound>0&&protectCell>prefixEnd+2&&[1,-1].includes(orientation)))throw Error('invalid compact-tail parameters');
 const rCuff=rCut-orientation*width,totalLog=rejoinR20At===null?6*delta0+6*etaRatioAtN0*delta0/(1-2**(-etaPower)):rejoinedTailLength({delta0,etaRatioAtN0,etaPower,rejoinR20At,rejoinIndexOffset}).total,oldCut=rCuff*Math.exp(orientation*totalLog/Math.sqrt(12)),epsilonScale=wCut*oldCut**7/(2*delta0)**a;
 const prefixRByCell=Array.from({length:prefixEnd+1},(_,n)=>n<prefixReturnStart?prefixR:Math.exp(Math.log(prefixR)+(Math.log(R)-Math.log(prefixR))*(n-prefixReturnStart+1)/(prefixEnd-prefixReturnStart+1)));
 const source=(rejoinR20At===null?createBalancedTail:createRejoinedBalancedTail)({rejoinR20At,rejoinIndexOffset,modes:1,depth:protectCell,delta0,R,a,etaPower,etaRatioAtN0,epsilonScale,rCuff,orientation,prefixEnd,prefixRByCell,calibrationSteps,steps:1,quadrature:16});
 const cutRaw=source.cells[0].profiles.at(-1)(1),cutCap=cutPreservingCap(cutRaw,slopeCap,capTransition,0,source.cells[0].profiles.length-1,source.cells[0].profiles.length-1,1);if(Math.abs(cutCap.logw-cutRaw.logw)>2e-13)throw Error('cap would change prescribed cut slope');
 const entries=[],byCell=source.cells.map(()=>[]),sums=new Float64Array(6);let bufferMaxCurvature=0;
 for(let n=protectCell-1;n>=0;n--)for(let j=0;j<source.cells[n].profiles.length;j++){
  const base=source.cells[n].profiles[j],beta=valleyControls[n]??0,last=source.cells[n].profiles.length-1;
  const raw=x=>{const z=base(x),v=j===3?smooth(x):j===4?1:j===5?1-smooth(x):0,d=j===3?cells.cellSmoothDerivative(x):j===5?-cells.cellSmoothDerivative(x):0;return {...z,logw:z.logw+beta*v,dlogwdx:z.dlogwdx+beta*d};};
  const entry={n,j,raw,source:x=>{const g=cutPreservingCap(raw(x),slopeCap,capTransition,n,j,last,x);let chi=1,j0=1;if(n===protectCell-1&&j===0)chi=smooth(x);if(n===0&&j===last){chi=1-smooth(x);j0=1+(rCut/oldCut-1)*smooth(x);}return {...g,chi,j0};}};
  entry.integrand=x=>{const g=entry.source(x),w=Math.exp(g.logw),E=1+w*w,root=Math.sqrt(E),rx=Math.abs(g.drdx),v= Math.abs(w*g.dlogwdx)/(E*root),A=rx*g.j0*(1-g.chi)+g.chi*v/curvatureBound,B=g.chi*rx/E;if(g.chi<1)bufferMaxCurvature=Math.max(bufferMaxCurvature,v/(rx*g.j0));return [A,B,root*A,root*B,w*A,w*B];};
  entry.breakpoints=cuspAwareQuadrature?generalCriticalPoints(entry.source):[];
  entry.integrate=(a,b)=>{const grid=splitIntegrationInterval(a,b,entry.breakpoints);if(grid.length===2)return integrate(entry.integrand,a,b,quadratureTolerance);
    const out=new Float64Array(6);for(let k=0;k<grid.length-1;k++){const v=integrate(entry.integrand,grid[k],grid[k+1],quadratureTolerance);for(let j=0;j<6;j++)out[j]+=v[j];}return out;};
  entry.total=new Float64Array(6);entry.cumA=new Float64Array(warpSteps+1);entry.cumB=new Float64Array(warpSteps+1);for(let k=0;k<warpSteps;k++){const v=entry.integrate(k/warpSteps,(k+1)/warpSteps);for(let l=0;l<6;l++){entry.total[l]+=v[l];sums[l]+=v[l];}entry.cumA[k+1]=entry.total[0];entry.cumB[k+1]=entry.total[1];}
  entries.push(entry);byCell[n][j]=entry;
 }
 const deepSource=source.cells.at(-1).profiles[0](0),target=orientation*(rCut-deepSource.r),alpha=(target-sums[0])/sums[1];if(!(alpha>0))throw Error('curvature redistribution exceeds requested width: '+JSON.stringify({minimumWidth:sums[0],requested:target}));
 let accumulated=0;for(const entry of entries){const start=deepSource.r+orientation*accumulated,cache=new Map();entry.profile=x=>{if(cache.has(x))return cache.get(x);const g=entry.source(x),d=entry.integrand(x),i=Math.min(warpSteps-1,Math.max(0,Math.floor(x*warpSteps)));let A,B;if(x<=0){A=B=0;}else if(x>=1){A=entry.total[0];B=entry.total[1];}else{A=entry.cumA[i];B=entry.cumB[i];if(x>i/warpSteps){const q=entry.integrate(i/warpSteps,x);A+=q[0];B+=q[1];}}const ans={r:start+orientation*(A+alpha*B),drdx:orientation*(d[0]+alpha*d[1]),logw:g.logw,dlogwdx:g.dlogwdx,oldR:g.r,oldDrdx:g.drdx,chi:g.chi};cache.set(x,ans);return ans;};accumulated+=entry.total[0]+alpha*entry.total[1];}
 const warpedCells=source.cells.map((c,n)=>({...c,profiles:byCell[n].map(e=>e.profile)})),cut=warpedCells[0].profiles.at(-1)(1),deep=warpedCells.at(-1).profiles[0](0),stats={rCut,rCuff,oldCut,wCut,width,curvatureBound,alpha,meridianLength:sums[2]+alpha*sums[3],heightSpan:sums[4]+alpha*sums[5],minimumWarpWidth:sums[0],bufferMaxCurvature,cutRadiusError:cut.r-rCut,cutSlopeError:Math.exp(cut.logw)-wCut,cutSecondError:Math.exp(cut.logw)*cut.dlogwdx/cut.drdx+7*wCut/rCut,deepRadiusError:deep.r-deepSource.r,deepSlopeError:Math.exp(deep.logw)-Math.exp(deepSource.logw),deepSecondError:Math.exp(deep.logw)*deep.dlogwdx/deep.drdx-Math.exp(deepSource.logw)*deepSource.dlogwdx/deepSource.drdx,deepDerivativeRatio:deep.drdx/deepSource.drdx,scope:'New cut-preserving capped finite profile, exact unchanged deep source. Numerical geometry only; all physical DN and nonlinear matching must be recomputed.'};
 return {cells:warpedCells,source,stats,parameters:{...options,cutPreservingCap:true,rCut,wCut,width,curvatureBound,delta0,R,a,etaPower,etaRatioAtN0,orientation,prefixR,prefixEnd,prefixReturnStart,protectCell,calibrationSteps,warpSteps,quadratureTolerance,slopeCap,capTransition,valleyControls,rejoinR20At,rejoinIndexOffset,rCuff,oldCut,epsilonScale,prefixRByCell},linearDeepParameters:source.parameters,sourceDefinition:source.parameters.sourceDefinition??'Selected fixed delta0/eta R64 source; not literal R20 parameters.',momentumNormalization:1};
}
