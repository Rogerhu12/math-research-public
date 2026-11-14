// Finite-cell physical recalibration of a genuinely curvature-redistributed tail.
// The source is immutable and Git-blob verified by closing_tail_sources.mjs.
// All conclusions from this module are finite numerical diagnostics only.
import {loadClosingTailSource} from './closing_tail_sources.mjs';
const {createBalancedTail}=await loadClosingTailSource('tailnext_balanced_tail.mjs');
const {createRejoinedBalancedTail,rejoinedTailLength}=await loadClosingTailSource('f6tail_r20_rejoin_source.mjs');
const {default:oldCells}=await loadClosingTailSource('general_root_smooth_tail_cells.cjs');
const {splitIntegrationInterval}=await loadClosingTailSource('f6tail_cusp_grid.mjs');
const smooth=oldCells.cellSmooth,dsmooth=oldCells.cellSmoothDerivative,SQRT12=Math.sqrt(12);

function gauss(n){const x=[],w=[];for(let i=0;i<n;i++){let z=Math.cos(Math.PI*(i+.75)/(n+.5)),pp=0;for(let it=0;it<40;it++){let p=1,q=0;for(let k=1;k<=n;k++){const a=q;q=p;p=((2*k-1)*z*q-(k-1)*a)/k;}pp=n*(z*p-q)/(z*z-1);const dz=p/pp;z-=dz;if(Math.abs(dz)<2e-15)break;}x.push(z);w.push(2/((1-z*z)*pp*pp));}return {x,w};}
const G8=gauss(8),G16=gauss(16);
function quadrature(f,a,b,G){const out=new Float64Array(6),h=(b-a)/2,m=(a+b)/2;for(let k=0;k<G.x.length;k++){const y=f(m+h*G.x[k]);for(let j=0;j<6;j++)out[j]+=h*G.w[k]*y[j];}return out;}
function integrate(f,a,b,tol,depth=0){const u=quadrature(f,a,b,G8),v=quadrature(f,a,b,G16);if(depth>=16||v.every((z,j)=>Math.abs(z-u[j])<=tol*Math.max(1e-200,Math.abs(z))))return v;const m=(a+b)/2,l=integrate(f,a,m,tol,depth+1),r=integrate(f,m,b,tol,depth+1);return l.map((z,j)=>z+r[j]);}
function cap(g,slopeCap,transition,capLogDerivative=0){if(!(slopeCap>0))return g;const c=Math.log(slopeCap),z=g.logw,L=transition;if(z<=c-L)return g;if(z>=c+L)return {...g,logw:c,dlogwdx:capLogDerivative};const t=(z-c+L)/(2*L),u=1-t,S=v=>v**4*(35-84*v+70*v*v-20*v**3),J=v=>v**5*(7-14*v+10*v*v-2.5*v**3),I=t<=.5?t-J(t):.5-J(u),d=t<=.5?1-S(t):S(u);return {...g,logw:c-L+2*L*I,dlogwdx:d*g.dlogwdx+(1-d)*capLogDerivative};}
function critical(profile){const out=[],N=128;let x0=0,f0=profile(0).dlogwdx;for(let k=1;k<=N;k++){const x1=k/N,f1=profile(x1).dlogwdx;if(f0*f1<0){let lo=x0,hi=x1,fl=f0;for(let i=0;i<52;i++){const m=(lo+hi)/2,fm=profile(m).dlogwdx;if(fl*fm<=0)hi=m;else{lo=m;fl=fm;}}out.push((lo+hi)/2);}if(f1===0&&f0!==0&&x1<1)out.push(x1);x0=x1;f0=f1;}return [...new Set(out)];}

export function createRecalibrationFactory(input={}){
 const p={rCut:1.03,wCut:.05,width:.04,curvatureBound:210,delta0:.006,R:64,a:2.75,etaPower:1.5,etaRatioAtN0:.05,orientation:-1,prefixR:8,prefixEnd:15,prefixReturnStart:8,protectCell:80,calibrationSteps:1024,warpSteps:16,quadratureTolerance:2e-11,slopeCap:0,capTransition:2,capMode:'original',cuspAwareQuadrature:true,valleyControls:[],rejoinR20At:null,rejoinIndexOffset:4,...input};
 const {rCut,wCut,width,curvatureBound,delta0,R,a,etaPower,etaRatioAtN0,orientation,prefixR,prefixEnd,prefixReturnStart,protectCell,calibrationSteps,warpSteps,quadratureTolerance,slopeCap,capTransition,capMode,rejoinR20At,rejoinIndexOffset}=p;
 if(!(rCut>width&&wCut>0&&width>0&&curvatureBound>0&&protectCell>prefixEnd+2&&[1,-1].includes(orientation)))throw Error('invalid tail parameters');
 const rCuff=rCut-orientation*width,totalLog=rejoinR20At===null?6*delta0+6*etaRatioAtN0*delta0/(1-2**(-etaPower)):rejoinedTailLength({delta0,etaRatioAtN0,etaPower,rejoinR20At,rejoinIndexOffset}).total,oldCut=rCuff*Math.exp(orientation*totalLog/SQRT12),epsilonScale=wCut*oldCut**7/(2*delta0)**a;
 const prefixRByCell=Array.from({length:prefixEnd+1},(_,n)=>n<prefixReturnStart?prefixR:Math.exp(Math.log(prefixR)+(Math.log(R)-Math.log(prefixR))*(n-prefixReturnStart+1)/(prefixEnd-prefixReturnStart+1)));
 const source=(rejoinR20At===null?createBalancedTail:createRejoinedBalancedTail)({rejoinR20At,rejoinIndexOffset,modes:1,depth:protectCell,delta0,R,a,etaPower,etaRatioAtN0,epsilonScale,rCuff,orientation,prefixEnd,prefixRByCell,calibrationSteps,steps:1,quadrature:16});
 const deepSource=source.cells.at(-1).profiles[0](0),caches=source.cells.map(()=>new Map());
 function getEntries(n,beta=0){
  if(caches[n].has(beta))return caches[n].get(beta);
  const entries=source.cells[n].profiles.map((base,j)=>{
   const last=source.cells[n].profiles.length-1,entry={n,j,beta};
   entry.profileSource=x=>{
    const z=base(x),v=j===3?smooth(x):j===4?1:j===5?1-smooth(x):0,d=j===3?dsmooth(x):j===5?-dsmooth(x):0,
      raw={...z,logw:z.logw+beta*v,dlogwdx:z.dlogwdx+beta*d};
    let localCap=slopeCap,capLogDerivative=0;
    if(slopeCap>0&&(p.pulseCaps?.[n]||p.valleyCaps?.[n])){
     const levels=[slopeCap,p.pulseCaps?.[n]?.[0]??slopeCap,p.valleyCaps?.[n]??slopeCap,p.pulseCaps?.[n]?.[1]??slopeCap,slopeCap];
     if(j%2===0)localCap=levels[j/2];
     else{const k=(j-1)/2,lc=Math.log(levels[k+1]/levels[k]);localCap=levels[k]*Math.exp(lc*smooth(x));capLogDerivative=lc*dsmooth(x);}
    }
    let g=cap(raw,localCap,capTransition,capLogDerivative);
    if(Number.isInteger(p.flatOuterThroughCell)&&p.flatOuterThroughCell>=0&&p.flatSlope>0){
     const lastCell=p.flatOuterThroughCell,startSegment=p.flatOuterStartSegment??2,lc=Math.log(p.flatSlope);
     if(n<lastCell||(n===lastCell&&j>startSegment))g={...g,logw:lc,dlogwdx:0};
     else if(n===lastCell&&j===startSegment){const t=smooth(x),dt=dsmooth(x);g={...g,logw:g.logw+t*(lc-g.logw),dlogwdx:(1-t)*g.dlogwdx+dt*(lc-g.logw)};}
    }
    if(capMode==='cut-preserving'&&n===0&&j===last)g=raw;
    if(capMode==='cut-preserving'&&n===0&&j===last-1){const eta=1-smooth(x),deta=-dsmooth(x);g={...raw,logw:raw.logw+eta*(g.logw-raw.logw),dlogwdx:raw.dlogwdx+eta*(g.dlogwdx-raw.dlogwdx)+deta*(g.logw-raw.logw)};}
    let chi=1,j0=1;if(n===protectCell-1&&j===0)chi=smooth(x);if(n===0&&j===last){chi=1-smooth(x);j0=1+(rCut/oldCut-1)*smooth(x);}return {...g,chi,j0};
   };
   entry.integrand=x=>{const g=entry.profileSource(x),w=Math.exp(g.logw),E=1+w*w,root=Math.sqrt(E),rx=Math.abs(g.drdx),v=Math.abs(w*g.dlogwdx)/(E*root),A=rx*g.j0*(1-g.chi)+g.chi*v/curvatureBound,B=g.chi*rx/E;return [A,B,root*A,root*B,w*A,w*B];};
   entry.breakpoints=p.cuspAwareQuadrature?critical(entry.profileSource):[];
   entry.integrate=(lo,hi)=>{const xs=splitIntegrationInterval(lo,hi,entry.breakpoints),out=new Float64Array(6);for(let k=0;k<xs.length-1;k++){const z=integrate(entry.integrand,xs[k],xs[k+1],quadratureTolerance);for(let l=0;l<6;l++)out[l]+=z[l];}return out;};
   entry.total=new Float64Array(6);entry.cumA=new Float64Array(warpSteps+1);entry.cumB=new Float64Array(warpSteps+1);
   for(let k=0;k<warpSteps;k++){const z=entry.integrate(k/warpSteps,(k+1)/warpSteps);for(let l=0;l<6;l++)entry.total[l]+=z[l];entry.cumA[k+1]=entry.total[0];entry.cumB[k+1]=entry.total[1];}
   const cache=new Map();entry.point=x=>{
    if(cache.has(x))return cache.get(x);const g=entry.profileSource(x),d=entry.integrand(x),i=Math.min(warpSteps-1,Math.max(0,Math.floor(x*warpSteps)));let A,B;
    if(x<=0){A=B=0;}else if(x>=1){A=entry.total[0];B=entry.total[1];}else{A=entry.cumA[i];B=entry.cumB[i];if(x>i/warpSteps){const z=entry.integrate(i/warpSteps,x);A+=z[0];B+=z[1];}}
    const result={g,A,B,dA:d[0],dB:d[1]};cache.set(x,result);return result;
   };
   return entry;
  });
  const total=new Float64Array(6);for(const e of entries)for(let i=0;i<6;i++)total[i]+=e.total[i];
  const result={n,beta,entries,total};caches[n].set(beta,result);while(caches[n].size>(p.maxCachedBetas??4))caches[n].delete(caches[n].keys().next().value);return result;
 }
 function physicalCell(n,beta,rStart,alpha){
  const es=getEntries(n,beta);let offset=0;
  const profiles=es.entries.map(e=>{const start=rStart+orientation*offset;offset+=e.total[0]+alpha*e.total[1];return x=>{const z=e.point(x),g=z.g;return {r:start+orientation*(z.A+alpha*z.B),drdx:orientation*(z.dA+alpha*z.dB),logw:g.logw,dlogwdx:g.dlogwdx,oldR:g.r,oldDrdx:g.drdx,chi:g.chi};};});
  return {...source.cells[n],beta,profiles,rStart,rEnd:rStart+orientation*offset,localWidth:offset,meridianLength:es.total[2]+alpha*es.total[3],heightSpan:es.total[4]+alpha*es.total[5]};
 }
 function assemble(controls=p.valleyControls,overrideAlpha=null){
  const totals=new Float64Array(6);for(let n=0;n<protectCell;n++)for(let j=0;j<6;j++)totals[j]+=getEntries(n,controls[n]??0).total[j];
  const target=orientation*(rCut-deepSource.r),alpha=overrideAlpha??((target-totals[0])/totals[1]);if(!(alpha>0))throw Error('curvature redistribution exceeds width '+JSON.stringify({minimumWidth:totals[0],requested:target,alpha}));
  const cells=[];let r=deepSource.r;for(let n=protectCell-1;n>=0;n--){cells[n]=physicalCell(n,controls[n]??0,r,alpha);r=cells[n].rEnd;}
  const cut=cells[0].profiles.at(-1)(1),deep=cells.at(-1).profiles[0](0),stats={rCut,rCuff,oldCut,wCut,width,curvatureBound,alpha,actualWidth:orientation*(cut.r-deepSource.r),minimumWarpWidth:totals[0],meridianLength:totals[2]+alpha*totals[3],heightSpan:totals[4]+alpha*totals[5],cutRadiusError:cut.r-rCut,cutSlopeError:Math.exp(cut.logw)-wCut,cutSecondError:Math.exp(cut.logw)*cut.dlogwdx/cut.drdx+7*wCut/rCut,deepRadiusError:deep.r-deepSource.r,deepSlopeError:Math.exp(deep.logw)-Math.exp(deepSource.logw),deepSecondError:Math.exp(deep.logw)*deep.dlogwdx/deep.drdx-Math.exp(deepSource.logw)*deepSource.dlogwdx/deepSource.drdx};
  return {cells,source,stats,parameters:{...p,valleyControls:Array.from(controls),rCuff,oldCut,epsilonScale,prefixRByCell},linearDeepParameters:source.parameters,momentumNormalization:1};
 }
 return {source,deepSource,parameters:{...p,rCuff,oldCut,epsilonScale,prefixRByCell},getEntries,physicalCell,assemble};
}

// Physical m2 state: u=f/r^4; z=pi/mu, pi=r^8*w*u_r/sqrt(12).
// u_x=sqrt(12)*mu*r_x*z/(r^8*w); z_x=-sqrt(12)*r_x*r^6*w*u/mu.
export function physicalModeColumn(cell,mode=2,steps=128,initial=[1,0],record=null){
 let y=initial.slice();const logMu=Math.log(cell.mu),nu=mode*mode*(mode*mode-1)/12;
 function rhs(v,g){const lr=Math.log(g.r),a=SQRT12*g.drdx*Math.exp(logMu-8*lr-g.logw),b=-nu*SQRT12*g.drdx*Math.exp(6*lr+g.logw-logMu),d=(mode*mode-4)*g.drdx/g.r;return [d*v[0]+a*v[1],b*v[0]-d*v[1]];}
 for(let j=0;j<cell.profiles.length;j++){
  const profile=cell.profiles[j];if(record)record(j,0,profile(0),y);
  for(let k=0;k<steps;k++){const x=k/steps,h=1/steps,g0=profile(x),gm=profile(x+h/2),g1=profile(x+h),a=rhs(y,g0),b=rhs([y[0]+h*a[0]/2,y[1]+h*a[1]/2],gm),c=rhs([y[0]+h*b[0]/2,y[1]+h*b[1]/2],gm),d=rhs([y[0]+h*c[0],y[1]+h*c[1]],g1);y=[y[0]+h*(a[0]+2*b[0]+2*c[0]+d[0])/6,y[1]+h*(a[1]+2*b[1]+2*c[1]+d[1])/6];if(!y.every(Number.isFinite))throw Error('nonfinite physical m2 column');if(record)record(j,x+h,g1,y);}
 }
 return {column:y,momentumRatio:y[1]/y[0],zeroResidual:y[1]/Math.max(1,Math.abs(y[0])),gain:y[0]};
}
export const physicalM2Column=(cell,steps=128,initial=[1,0],record=null)=>physicalModeColumn(cell,2,steps,initial,record);

export function sampleTailGeometry(tail,steps=128){
 let maxMeridian=0,maxAngular=0,maxSlope=0,meridianWhere=null;
 for(let n=0;n<tail.cells.length;n++)for(let j=0;j<tail.cells[n].profiles.length;j++)for(let k=0;k<=steps;k++){
  const g=tail.cells[n].profiles[j](k/steps),w=Math.exp(g.logw),E=1+w*w,meridian=Math.abs(w*g.dlogwdx/g.drdx)/E**1.5,angular=Math.abs(w)/(g.r*Math.sqrt(E));
  if(meridian>maxMeridian){maxMeridian=meridian;meridianWhere={cell:n,segment:j,x:k/steps,r:g.r,w};}maxAngular=Math.max(maxAngular,angular);maxSlope=Math.max(maxSlope,w);
 }
 return {steps,maxMeridian,maxAngular,maxSlope,meridianWhere,scope:'Samples only; not a continuous curvature certificate.'};
}

export function solvePhysicalCell(factory,n,rStart,alpha,options={}){
 const steps=options.steps??128,tolerance=options.tolerance??1e-9,initialBeta=options.initialBeta??2*Math.log(alpha),limit=options.limit??40,trace=[];
 const evaluate=beta=>{const cell=factory.physicalCell(n,beta,rStart,alpha),z=physicalM2Column(cell,steps),result={beta,cell,...z};trace.push({beta,residual:z.zeroResidual,gain:z.gain});return result;};
 let center=evaluate(initialBeta);if(Math.abs(center.zeroResidual)<tolerance)return {...center,iterations:0,evaluations:trace.length,trace};
 let lo=center,hi=center,width=1;
 for(let i=0;i<8&&lo.column[1]*hi.column[1]>=0;i++){
  lo=evaluate(initialBeta-width);hi=evaluate(initialBeta+width);width*=1.8;
 }
 if(lo.column[1]*hi.column[1]>=0)throw Error('physical calibration lacks sign bracket '+JSON.stringify({n,alpha,rStart,trace}));
 let best=Math.abs(lo.zeroResidual)<Math.abs(hi.zeroResidual)?lo:hi,fl=lo.column[1],fh=hi.column[1],lastSide=0;
 for(let it=0;it<limit;it++){
  let beta=(lo.beta*fh-hi.beta*fl)/(fh-fl),span=hi.beta-lo.beta;
  if(!(beta>lo.beta+.02*span&&beta<hi.beta-.02*span)||it%6===5)beta=(lo.beta+hi.beta)/2;
  const z=evaluate(beta);if(Math.abs(z.zeroResidual)<Math.abs(best.zeroResidual))best=z;
  if(Math.abs(z.zeroResidual)<tolerance||span<2e-13)return {...best,iterations:it+1,evaluations:trace.length,trace};
  if(lo.column[1]*z.column[1]<=0){hi=z;fh=z.column[1];if(lastSide===-1)fl*=.5;else fl=lo.column[1];lastSide=-1;}
  else{lo=z;fl=z.column[1];if(lastSide===1)fh*=.5;else fh=hi.column[1];lastSide=1;}
 }
 throw Error('physical calibration iteration limit '+JSON.stringify({n,alpha,rStart,best:trace.reduce((a,b)=>Math.abs(a.residual)<Math.abs(b.residual)?a:b),trace}));
}

export function idealModeGraph(mode,R,a){
 if(mode===2)return 0;const nu=mode*mode*(mode*mode-1)/12,rho=2**a,al=1+1/R,a00=1-al*nu*R,a10=(-nu*(1+R)+al*nu*nu*R)/rho,a11=(1-al*nu)/rho,tr=a00+a11,det=1/rho,lambda=.5*(tr-Math.sqrt(tr*tr-4*det));return a10/(lambda-a11);
}
export function diagnosePhysicalMode(tail,mode=2,steps=256,far=tail.cells.length,testAmplitude=0,angularSamples=32){
 const records=[],cellRows=[];let y=[1,tail.parameters.orientation*idealModeGraph(mode,tail.parameters.R,tail.parameters.a)],ln=0,lastMu=tail.cells[far-1].mu;
 for(let n=far-1;n>=0;n--){
  const cell=tail.cells[n];y[1]*=lastMu/cell.mu;lastMu=cell.mu;
  const z=physicalModeColumn(cell,mode,steps,y,(j,x,g,v)=>records.push([n,j,x,g.r,g.logw,v[0],v[1],ln,g.dlogwdx/g.drdx]));
  const norm=Math.hypot(...z.column);y=z.column.map(v=>v/norm);ln+=Math.log(norm);
  cellRows.push({cell:n,beta:cell.beta,exitMomentumRatio:y[1]/y[0],logU:ln+Math.log(Math.abs(y[0]))});
 }
 const rCut=tail.cells[0].profiles.at(-1)(1).r,wCut=Math.exp(tail.cells[0].profiles.at(-1)(1).logw),logOuter=ln+Math.log(Math.abs(y[0]))+4*Math.log(rCut),signOuter=Math.sign(y[0]);
 let threshold=Infinity,where=null,maxHeight=0,maxDerivative=0,gradientThreshold=Infinity,gradientWhere=null,smallPThreshold=Infinity,smallPWhere=null;
 const formal={amplitude:testAmplitude,angularSamples,maxAbsCurvature:0,minProjectionD:Infinity,minProjectionS:Infinity,where:null,scope:'Second form inferred from the linear height lift with the fixed metric. It violates nonlinear Gauss at order amplitude squared and is only a diagnostic, not an embedded-surface curvature certificate.'};
 const angles=Array.from({length:angularSamples},(_,i)=>[Math.cos(2*Math.PI*i/angularSamples),Math.sin(2*Math.PI*i/angularSamples)]);
 const cellThresholds=Array.from({length:far},()=>({threshold:Infinity,where:null}));
 for(const [n,j,x,r,lw,u,z,l,lwr] of records){
  const w=Math.exp(lw),E=1+w*w,scale=signOuter*Math.exp(l-logOuter),U=u*scale,Z=z*scale,mu=tail.cells[n].mu,
   f=r**4*U,fr=mode*mode*r**3*U+SQRT12*mu*Z/(r**4*w),base=r*w/E,linear=(SQRT12*mu*Z/(r**3*w)-mode*mode*r**4*U*w*w)/E,
   crit=linear===0?Infinity:base/Math.abs(linear),location={cell:n,segment:j,x,r,w,f,fr,baseT:base,linearT:linear};
  if(crit<threshold){threshold=crit;where=location;}if(crit<cellThresholds[n].threshold)cellThresholds[n]={threshold:crit,where:location};const grad=f===0?Infinity:r/(mode*Math.abs(f));if(grad<gradientThreshold){gradientThreshold=grad;gradientWhere=location;}const smallP=grad*w;if(smallP<smallPThreshold){smallPThreshold=smallP;smallPWhere=location;}maxHeight=Math.max(maxHeight,Math.abs(f));maxDerivative=Math.max(maxDerivative,Math.abs(fr));
  if(testAmplitude>0){
   const a=testAmplitude,wr=w*lwr,frr=-lwr*(fr-mode*mode*f/r);
   for(const [ct,st] of angles){
    const D=1-2*a*w*fr*ct-a*a*fr*fr*ct*ct-a*a*E*mode*mode*f*f*st*st/(r*r),S=1-a*a*mode*mode*f*f*st*st/(r*r);formal.minProjectionD=Math.min(formal.minProjectionD,D);formal.minProjectionS=Math.min(formal.minProjectionS,S);
    if(D<=0){formal.maxAbsCurvature=Infinity;continue;}
    const nz=Math.sqrt(D/E),hr=w+a*fr*ct,Hrr=wr+a*frr*ct-w*wr/E*hr,Htt=-a*mode*mode*f*ct+r/E*hr,Hrt=-a*mode*(fr-f/r)*st,
     A=Hrr/(E*nz),B=Htt/(r*r*nz),C=Hrt/(r*Math.sqrt(E)*nz),rad=Math.hypot((A-B)/2,C),v=Math.max(Math.abs((A+B)/2+rad),Math.abs((A+B)/2-rad));
    if(v>formal.maxAbsCurvature){formal.maxAbsCurvature=v;formal.where={...location,cosModeAngle:ct,sinModeAngle:st,baseMeridianCurvature:wr/E**1.5,baseAngularCurvature:w/(r*Math.sqrt(E)),frr};}
   }
  }
 }
 return {mode,far,steps,cutSlope:mode*mode/rCut+SQRT12*tail.cells[0].mu*y[1]/(rCut**8*wCut*y[0]),logHeightGain:logOuter,linearTPositivityAmplitudeThreshold:threshold,thresholdLocation:where,gradientAmplitudeThreshold:gradientThreshold,gradientThresholdLocation:gradientWhere,rescaledAngularSmallnessThreshold:smallPThreshold,rescaledAngularSmallnessLocation:smallPWhere,gradientThresholdDefinition:'r/(m*abs(f)); angular projection S=1-(h_theta/r)^2. The separate r*w/(m*abs(f)) threshold only controls normalized |P|<1 and is NOT a necessary embedding or graph condition.',normalizedHeightMax:maxHeight,normalizedDerivativeMax:maxDerivative,cellRows,cellThresholds,formalLinearHeightGeometry:testAmplitude>0?{...formal,linearAngularBranchMinimum:1-testAmplitude/threshold}:undefined,scope:'Sampled linearized H_theta_theta positivity and angular projection diagnostic only; not a nonlinear amplitude or existence theorem.'};
}
export const diagnosePhysicalM2=(tail,steps=256,far=tail.cells.length)=>diagnosePhysicalMode(tail,2,steps,far);
