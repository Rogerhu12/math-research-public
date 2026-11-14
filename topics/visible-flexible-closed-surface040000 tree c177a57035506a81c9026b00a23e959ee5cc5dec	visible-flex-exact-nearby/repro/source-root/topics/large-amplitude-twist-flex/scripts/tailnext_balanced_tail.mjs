// Actual C2 finite-prefix tail redesign. The sufficiently deep profile is unchanged.
// Every changed cell is recalibrated and every mode uses its changed true transfer.
import oldCells from './general_root_smooth_tail_cells.cjs';
import {createMomentumTailEngine} from './general_root_tail_momentum.mjs';
const {cellSegments,cellSmooth,cellSmoothDerivative}=oldCells;
const calibrations=new Map(),transfers=new Map();
export function balancedCellTransfer(options={}){
 const {delta=.08,R=64,alpha=1+1/R,A=2.75*Math.log(2),c=.05,mode=2,direction=1,steps=256,lengthScale=1}=options;
 const k=direction*(mode*mode-4)/Math.sqrt(12),nu=mode*mode*(mode*mode-1)/12;
 let state=Float64Array.from([1,0,0,1,0,0,0,0]);
 function rhs(y,seg,x){const s=seg.transition?cellSmooth(x):0,lp=seg.lo+(seg.hi-seg.lo)*s,ap=seg.alo+(seg.ahi-seg.alo)*s,p=Math.exp(lp),u=lengthScale*delta*delta/p*seg.lengthRatio,v=-lengthScale*nu*p*seg.lengthRatio,z=lengthScale*k*delta*seg.lengthRatio,du=-ap*u,dv=ap*v,o=new Float64Array(8);for(let j=0;j<2;j++){o[j]=z*y[j]+u*y[j+2];o[j+2]=v*y[j]-z*y[j+2];o[j+4]=z*y[j+4]+u*y[j+6]+du*y[j+2];o[j+6]=v*y[j+4]-z*y[j+6]+dv*y[j];}return o;}
 for(const seg of cellSegments(delta,R,alpha,A,c)){
  if(!seg.transition){const P=Math.exp(seg.lo)/delta,L=lengthScale*seg.lengthRatio*delta,rho=Math.sqrt(Math.max(0,nu-k*k)),cc=Math.cos(rho*L),ss=rho?Math.sin(rho*L)/rho:L,m=[cc+k*ss,ss/P,-nu*P*ss,cc-k*ss],dm=[0,-seg.alo*ss/P,seg.alo*(-nu*P*ss),0],y=new Float64Array(8);for(let j=0;j<2;j++){y[j]=m[0]*state[j]+m[1]*state[j+2];y[j+2]=m[2]*state[j]+m[3]*state[j+2];y[j+4]=m[0]*state[j+4]+m[1]*state[j+6]+dm[0]*state[j]+dm[1]*state[j+2];y[j+6]=m[2]*state[j+4]+m[3]*state[j+6]+dm[2]*state[j]+dm[3]*state[j+2];}state=y;}
  else for(let n=0;n<steps;n++){const h=1/steps,x=n*h,a=rhs(state,seg,x),tmp=new Float64Array(8);for(let j=0;j<8;j++)tmp[j]=state[j]+h*a[j]/2;const b=rhs(tmp,seg,x+h/2);for(let j=0;j<8;j++)tmp[j]=state[j]+h*b[j]/2;const cc=rhs(tmp,seg,x+h/2);for(let j=0;j<8;j++)tmp[j]=state[j]+h*cc[j];const d=rhs(tmp,seg,x+h);for(let j=0;j<8;j++)state[j]+=h*(a[j]+2*b[j]+2*cc[j]+d[j])/6;}
 }
 const matrix=Array.from(state.slice(0,4));return {matrix,alphaDerivative:Array.from(state.slice(4)),determinant:matrix[0]*matrix[3]-matrix[1]*matrix[2]};
}
export function calibrateBalancedCell(options={}){
 const key=JSON.stringify(options);if(calibrations.has(key))return calibrations.get(key);
 let alpha=options.initialAlpha??(1+1/(options.R??64)),last=null,iterations=0;
 for(;iterations<32;iterations++){
  last=balancedCellTransfer({...options,mode:2,direction:1,alpha});const f=last.matrix[2],df=last.alphaDerivative[2];if(Math.abs(f)<2e-12*Math.max(1,Math.abs(last.matrix[0])))break;
  if(!(Math.abs(df)>1e-20&&Number.isFinite(df)))throw Error('prefix alpha derivative singular');
  let step=-f/df,accepted=false;for(let back=0;back<24;back++){const candidate=alpha+step;if(candidate>0){const z=balancedCellTransfer({...options,mode:2,direction:1,alpha:candidate});if(Math.abs(z.matrix[2])<Math.abs(f)){alpha=candidate;last=z;accepted=true;break;}}step*=.5;}if(!accepted)throw Error('prefix alpha line search failed');
 }
 if(iterations>=32)throw Error('prefix alpha iteration limit');
 const out={...last,alpha,iterations,gain:-last.matrix[0],targetLowerEntry:last.matrix[2]};calibrations.set(key,out);return out;
}
export function createBalancedTail(options={}){
 const {modes=2,depth=4,delta0=.08,R=64,a=2.75,etaPower=1.5,etaRatioAtN0=.05,epsilonScale=.1,rCuff=1,steps=32,quadrature=64,farPadding=10,orientation=1,nodeIndex=0,calibrationSteps=512,prefixEnd=-1,prefixR=R,prefixEtaMultiplier=1,preserveCellLength=true,prefixRByCell=null,projectionFloor=.1}=options;
 const M=modes,K=2*M,A=a*Math.log(2),portRatio=2**a,eta0=etaRatioAtN0*delta0,far=Math.max(depth+farPadding,prefixEnd-nodeIndex+1+farPadding),cells=[],ts=[],graphs=[],gains=[];
 function shape(n){const delta=delta0*2**(-n),baseC=etaRatioAtN0*2**(-n*(etaPower-1)),changed=n<=prefixEnd,Rn=changed?(prefixRByCell?.[n]??prefixR):R,c=baseC*(changed?prefixEtaMultiplier:1),lengthScale=changed&&preserveCellLength?(3+6*baseC)/(3+6*c):1;return {delta,R:Rn,c,lengthScale,baseC,length:delta*(3+6*c)*lengthScale,baseLength:delta*(3+6*baseC)};}
 function after(n){let sum=3*delta0*2**(-n)+6*eta0*2**(-etaPower*(n+1))/(1-2**(-etaPower));if(!preserveCellLength)for(let k=n+1;k<=prefixEnd;k++){const z=shape(k);sum+=z.length-z.baseLength;}return sum;}
 function physicalCell(index){const p=shape(index),cal=calibrateBalancedCell({...p,A,steps:calibrationSteps}),mu=epsilonScale*p.delta**a,rOuter=rCuff*Math.exp(orientation*after(index)/Math.sqrt(12)),logBase=Math.log(mu);let offset=0;const profiles=cellSegments(p.delta,p.R,cal.alpha,A,p.c).map(seg=>{const len=seg.lengthRatio*p.delta*p.lengthScale,start=offset;offset+=len;return x=>{const s=seg.transition?cellSmooth(x):0,ds=seg.transition?cellSmoothDerivative(x):0,logRadius=Math.log(rOuter)+orientation*(start+len*x)/Math.sqrt(12),r=Math.exp(logRadius);return {r,drdx:orientation*len*r/Math.sqrt(12),logw:logBase+seg.lo+(seg.hi-seg.lo)*s-Math.log(p.delta)-7*logRadius,dlogwdx:(seg.hi-seg.lo)*ds-7*orientation*len/Math.sqrt(12)};};});return {n:index-nodeIndex,physicalIndex:index,...p,mu,rOuter,cal,profiles};}
 for(let n=0;n<far;n++){
  const cell=physicalCell(n+nodeIndex),row=[];
  for(let j=0;j<M;j++){const mode=2*(j+1),parameters={delta:cell.delta,R:cell.R,alpha:cell.cal.alpha,A,c:cell.c,lengthScale:cell.lengthScale,mode,direction:orientation,steps:calibrationSteps},key=JSON.stringify(parameters);let t=transfers.get(key);if(!t){t=balancedCellTransfer(parameters).matrix;transfers.set(key,t);}row.push([t[0],t[1],t[2]/portRatio,t[3]/portRatio]);}
  ts.push(row);if(n<depth){cell.engine=createMomentumTailEngine({modes:M,quadrature,mu:cell.mu,orientation,projectionFloor});cells.push(cell);}
 }
 const end=new Float64Array(M);for(let j=0;j<M;j++){const m=2*(j+1),nu=m*m*(m*m-1)/12,alpha=1+1/R,t00=1-alpha*nu*R,t10=(-nu*(1+R)+alpha*nu*nu*R)/portRatio,t11=(1-alpha*nu)/portRatio,trace=t00+t11,det=1/portRatio,lambda=.5*(trace-Math.sqrt(trace*trace-4*det));end[j]=j===0?0:t10/(lambda-t11);}
 graphs[far]=end;for(let n=far-1;n>=0;n--){const graph=new Float64Array(M),gain=new Float64Array(M);for(let j=0;j<M;j++){const t=ts[n][j],v=graphs[n+1][j];gain[j]=t[0]+t[1]*v;if(Math.abs(gain[j])<1e-14)throw Error('prefix linear Q chart vertical');graph[j]=(t[2]+t[3]*v)/gain[j];}graphs[n]=graph;gains[n]=gain;}
 function initial(target){const states=Array.from({length:depth+1},()=>new Float64Array(K));states[0].set(target);for(let j=0;j<M;j++)states[0][M+j]=graphs[0][j]*target[j];for(let n=0;n<depth;n++)for(let j=0;j<M;j++){states[n+1][j]=states[n][j]/gains[n][j];states[n+1][M+j]=graphs[n+1][j]*states[n+1][j];}return states;}
 return {cells,graphs,gains,initial,linearTransfers:ts,parameters:{modes:M,depth,delta0,R,a,etaPower,etaRatioAtN0,epsilonScale,rCuff,steps,quadrature,farPadding,orientation,nodeIndex,calibrationSteps,prefixEnd,prefixR,prefixEtaMultiplier,preserveCellLength,prefixRByCell,projectionFloor,linearFarIndex:far}};
}
