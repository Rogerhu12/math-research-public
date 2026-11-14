// R95: same Newton direction and residual, a nonlinear Q/L trial curve.
// No solver/physical configuration is changed by importing this module.
// The caller evaluates/accepts the returned states with its original F.

const trigCache=new Map();

function tables(M,N,spacing){
 const key=`${M}/${N}/${spacing}`;
 if(trigCache.has(key))return trigCache.get(key);
 const J=M+1,sq2=Math.sqrt(2),freq=Float64Array.from({length:M},(_,j)=>spacing*(j+1)),
  cs=Array.from({length:N},()=>new Float64Array(J)),sn=Array.from({length:N},()=>new Float64Array(M));
 for(let n=0;n<N;n++){
  const theta=2*Math.PI*n/N;cs[n][0]=1;
  for(let j=0;j<M;j++){cs[n][j+1]=sq2*Math.cos(freq[j]*theta);sn[n][j]=sq2*Math.sin(freq[j]*theta);}
 }
 const out={M,N,J,freq,cs,sn};trigCache.set(key,out);return out;
}

function solveSPD(B,b){
 const J=b.length,L=new Float64Array(J*J),tmp=new Float64Array(J),out=new Float64Array(J);
 for(let i=0;i<J;i++)for(let j=0;j<=i;j++){
  let value=B[i*J+j];for(let k=0;k<j;k++)value-=L[i*J+k]*L[j*J+k];
  if(i===j){if(!(value>0))throw Error('Geometric retraction Gram matrix is not SPD');L[i*J+j]=Math.sqrt(value);}
  else L[i*J+j]=value/L[j*J+j];
 }
 for(let i=0;i<J;i++){let value=b[i];for(let j=0;j<i;j++)value-=L[i*J+j]*tmp[j];tmp[i]=value/L[i*J+i];}
 for(let i=J-1;i>=0;i--){let value=tmp[i];for(let j=i+1;j<J;j++)value-=L[j*J+i]*out[j];out[i]=value/L[i*J+i];}
 return out;
}

export function prepareGeometricNodeRetraction({engine,profile,x,state,delta,spacing,portRatio=1,knownRoot=null}){
 const {M,N,mu,orientation}=engine,K=2*M,J=M+1,sq2=Math.sqrt(2),sq12=Math.sqrt(12);
 if(!(Number.isInteger(spacing)&&spacing>0&&portRatio>0&&Number.isFinite(portRatio)))throw Error('Invalid geometric node coordinates');
 if(state.length<K||delta.length!==state.length)throw Error('Geometric node state/direction dimensions differ');
 const base=Float64Array.from(state),direction=Float64Array.from(delta),
  y=new Float64Array(K+2),dy=new Float64Array(K+2);
 for(let j=0;j<M;j++){y[j]=base[j];y[M+j]=base[M+j]*portRatio;dy[j]=direction[j];dy[M+j]=direction[M+j]*portRatio;}
 for(let j=K;j<Math.min(K+2,base.length);j++){y[j]=base[j];dy[j]=direction[j];}
 const rt=knownRoot??engine.root(y,profile,x),g=rt.g,t=tables(M,N,spacing),
  targetFactor=g.momentumTargetFactor,
  pFactor=g.momentumPFactor,right=new Float64Array(J),dp=new Float64Array(M),dpt=new Float64Array(M);
 for(let j=0;j<M;j++){
  right[j+1]=targetFactor*dy[M+j];
  dp[j]=-t.freq[j]*pFactor*dy[j];dpt[j]=t.freq[j]*dp[j];
 }
 for(let n=0;n<N;n++){
  const v=rt.e.rows[n],wp=g.w*v.P,wk=g.w*v.K,wpt=g.w*v.Pt,
   omega=1+(g.deepScaled?g.w*(g.w*(v.L+v.quad)):g.w2*(v.L+v.quad)),invD32=1/(v.D*v.sd),
   FP=g.E*v.P*omega/v.D+(g.deepScaled?2*(1+v.K)*wpt*wp:2*g.w2*(1+v.K)*v.Pt*v.P)/(v.S*v.S*v.sd),
   FT=-(g.E*v.Pt+(g.deepScaled?(1+v.K)*(g.w*(g.w*wp*wp)+2*g.w*wk+wk*wk):g.w2*(1+v.K)*(g.w2*v.P*v.P+2*v.K+v.K*v.K))/v.S)*invD32;
  let P1=0,T1=0;for(let j=0;j<M;j++){P1+=dp[j]*t.sn[n][j];T1+=dpt[j]*t.cs[n][j+1];}
  const value=FP*P1+FT*T1;
  for(let i=0;i<J;i++)right[i]-=value*t.cs[n][i]/N;
 }
 const dL=solveSPD(rt.e.B,right),raw=engine.toRaw(y,profile,x,rt).raw,baseMeanL=rt.L[0],
  rawDirection=new Float64Array(K),rawFactor=sq2*g.w/(sq12*g.r**3);
 for(let j=0;j<M;j++){rawDirection[j]=dy[j];rawDirection[M+j]=rawFactor*dL[j+1];}
 const diagnostics={M,N,spacing,x,portRatio,minA:rt.e.minA,minD:rt.e.minD,minS:rt.e.minS,
  rootRelativeResidual:rt.err/rt.scale,meanLDirection:dL[0],
  maxNonmeanLDirection:Math.max(...Array.from(dL.slice(1),Math.abs)),
  scope:'One fixed physical-node differential; positive geometry of later trial roots is not asserted.'};
 function step(lambda,{detail=false}={}){
  if(!Number.isFinite(lambda))throw Error('Retraction step is not finite');
  if(lambda===0)return {state:Float64Array.from(base),diagnostics:{...diagnostics,lambda,exactZeroStep:true}};
  const trialRaw=Float64Array.from(raw,(value,j)=>value+lambda*rawDirection[j]),
   initialized=engine.initializeFromRaw(trialRaw,profile,x),out=Float64Array.from(base,(value,j)=>value+lambda*direction[j]);
  for(let j=0;j<M;j++){out[j]=initialized.state[j];out[M+j]=initialized.state[M+j]/portRatio;}
  const info={lambda,normalizedMeanResidual:initialized.normalizedMeanResidual};
  if(detail){
   const e=engine.evaluateL(initialized.L,initialized.state.slice(0,M),g,false);
   Object.assign(info,{minA:e.minA,minD:e.minD,minS:e.minS,
    meanL:initialized.L[0],meanLChange:initialized.L[0]-baseMeanL,
    meanLLinearPrediction:baseMeanL+lambda*dL[0],
    canonicalLinearDifference:Math.max(...Array.from(out,(value,j)=>Math.abs(value-base[j]-lambda*direction[j])))});
  }
  return {state:out,diagnostics:info};
 }
 return {step,diagnostics,raw:Float64Array.from(raw),rawDirection,meanLDirection:dL[0]};
}

export function prepareGeometricShootingRetraction(states,delta,cells,{spacing}={}){
 if(states.length!==cells.length+1||delta.length!==states.length)throw Error('Geometric shooting node counts differ');
 const nodes=[];
 for(let i=0;i<states.length;i++){
  const cell=cells[i===0?0:i-1],profile=i===0?cell.profiles.at(-1):cell.profiles[0],
   x=i===0?1:0,ratio=i===0?cell.portRatio:1;
  try{nodes.push(prepareGeometricNodeRetraction({engine:cell.engine,profile,x,state:states[i],delta:delta[i],spacing,portRatio:ratio}));}
  catch(error){const failure=Error(`Geometric retraction preparation at node ${i}: ${String(error)}`);failure.node=i;failure.cause=error;throw failure;}
 }
 return {
  step(lambda){
   return nodes.map((node,i)=>{
    try{return Array.from(node.step(lambda).state);}
    catch(error){const failure=Error(`Geometric retraction trial at node ${i}: ${String(error)}`);failure.node=i;failure.cause=error;throw failure;}
   });
  },
  diagnostics:{nodeCount:nodes.length,method:'same-direction-Q-L-Newton-retraction-v1',
   minPreparationA:Math.min(...nodes.map(v=>v.diagnostics.minA)),
   minPreparationD:Math.min(...nodes.map(v=>v.diagnostics.minD)),
   scope:'Trial construction only; no residual, Jacobian, Newton correction, floor or acceptance criterion is changed.'}
 };
}

export function createGeometricTrialHook(cells,{spacing}={}){
 // Invoke this hook inside the original trial try/catch. A preparation
 // rejection is a trial-construction failure, not a claim that F was invalid.
 let previousStates=null,previousDelta=null,prepared=null;
 const statistics={preparations:0,trialCalls:0,lastPreparation:null};
 function retractTrial(states,delta,lambda){
  statistics.trialCalls++;
  if(states!==previousStates||delta!==previousDelta||!prepared){
   prepared=null;
   const next=prepareGeometricShootingRetraction(states,delta,cells,{spacing});
   prepared=next;previousStates=states;previousDelta=delta;
   statistics.preparations++;statistics.lastPreparation=next.diagnostics;
  }
  return prepared.step(lambda);
 }
 return {retractTrial,statistics};
}
