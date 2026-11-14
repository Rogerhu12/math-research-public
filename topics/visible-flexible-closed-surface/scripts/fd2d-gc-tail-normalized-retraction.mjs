// Same centered R95 Q/L curve, evaluated without a physical w*L intermediary.
// In exact arithmetic raw_j=(w/(sqrt(6)*r^3))*L_j at a fixed node, so taking
// the straight line in L is exactly the original straight line in raw slopes.
// The original residual/Jacobian/correction/floor/acceptance are unchanged.
import {prepareGeometricNodeRetraction as prepareDifferential} from './fd2d-gc-tail-deep-retraction-differential-v2.mjs';

function fromNormalized(engine,Q,nonmeanL,profile,x,meanGuess){
 const {M}=engine,g=engine.geometry(profile,x),L=Float64Array.from(nonmeanL);
 if(!Number.isFinite(meanGuess))throw Error('Normalized mean predictor is not finite');
 L[0]=meanGuess;let e,iterations;
 for(let it=0;it<30;it++){
  iterations=it;e=engine.evaluateL(L,Q,g,true);
  const error=e.moments[0],scale=Math.max(1e-300,e.maxQuad,Math.abs(L[0]));
  if(Math.abs(error)<=8e-14*scale)break;
  const correction=error/e.B[0];let accepted=false;
  for(let k=0;k<20;k++){
   const trial=Float64Array.from(L);trial[0]-=correction*2**(-k);
   try{const v=engine.evaluateL(trial,Q,g,false);if(Math.abs(v.moments[0])<Math.abs(error)){L.set(trial);accepted=true;break;}}catch(_){}
  }
  if(!accepted)throw Error('Normalized seeded full mean root failed');
  if(it===29)throw Error('Normalized seeded mean iteration limit');
 }
 e=engine.evaluateL(L,Q,g,true);
 const pi=Float64Array.from(e.moments.slice(1),v=>g.momentumInverseFactor*v);
 if(!pi.every(Number.isFinite))throw Error('Normalized momentum conversion outside binary64 range');
 return {pi,L,normalizedMeanResidual:e.moments[0],meanIterations:iterations,minA:e.minA,minD:e.minD,minS:e.minS};
}

export function prepareGeometricNodeRetraction(options){
 const {engine,profile,x,spacing,portRatio=1}=options,{M}=engine,K=2*M,
  base=Float64Array.from(options.state),direction=Float64Array.from(options.delta),y=new Float64Array(K+2);
 for(let j=0;j<M;j++){y[j]=base[j];y[M+j]=base[M+j]*portRatio;}
 const root=options.knownRoot??engine.root(y,profile,x),
  differential=prepareDifferential({...options,knownRoot:root}),
  L=Float64Array.from(differential.normalizedL),dL=Float64Array.from(differential.normalizedDirection),
  Q=Float64Array.from(base.slice(0,M)),anchor=fromNormalized(engine,Q,L,profile,x,L[0]),
  diagnostics={...differential.diagnostics,method:'same-direction-Q-L-centered-normalized-arithmetic-v1',
   physicalSlopeIntermediateUsed:false,anchorMeanIterations:anchor.meanIterations};
 function step(lambda,{detail=false}={}){
  if(!Number.isFinite(lambda))throw Error('Retraction step is not finite');
  if(lambda===0)return {state:Float64Array.from(base),diagnostics:{...diagnostics,lambda,exactZeroStep:true}};
  const nextQ=Float64Array.from(Q,(v,j)=>direction[j]===0?v:v+lambda*direction[j]),
   nextL=Float64Array.from(L,(v,j)=>dL[j]===0?v:v+lambda*dL[j]),
   initialized=fromNormalized(engine,nextQ,nextL,profile,x,nextL[0]),
   state=Float64Array.from(base,(v,j)=>direction[j]===0?v:v+lambda*direction[j]);
  for(let j=0;j<M;j++){
   const increment=(initialized.pi[j]-anchor.pi[j])/portRatio;
   state[M+j]=increment===0?base[M+j]:base[M+j]+increment;
  }
  const info={lambda,normalizedMeanResidual:initialized.normalizedMeanResidual,meanIterations:initialized.meanIterations};
  if(detail)Object.assign(info,{minA:initialized.minA,minD:initialized.minD,minS:initialized.minS,
   meanL:initialized.L[0],meanLChange:initialized.L[0]-L[0],meanLLinearPrediction:nextL[0],
   canonicalLinearDifference:Math.max(...state.map((v,j)=>Math.abs(v-base[j]-lambda*direction[j])))});
  return {state,diagnostics:info};
 }
 return {step,diagnostics,normalizedL:L,normalizedDirection:dL};
}

export function prepareGeometricShootingRetraction(states,delta,cells,{spacing}={}){
 if(states.length!==cells.length+1||delta.length!==states.length)throw Error('Geometric shooting node counts differ');
 const nodes=[];
 for(let i=0;i<states.length;i++){
  const cell=cells[i===0?0:i-1],profile=i===0?cell.profiles.at(-1):cell.profiles[0],x=i===0?1:0,portRatio=i===0?cell.portRatio:1;
  try{nodes.push(prepareGeometricNodeRetraction({engine:cell.engine,profile,x,state:states[i],delta:delta[i],spacing,portRatio}));}
  catch(error){const e=Error(`Normalized geometric preparation at node ${i}: ${String(error)}`);e.node=i;e.cause=error;throw e;}
 }
 return {step(lambda){return nodes.map((node,i)=>{try{return Array.from(node.step(lambda).state);}catch(error){const e=Error(`Normalized geometric trial at node ${i}: ${String(error)}`);e.node=i;e.cause=error;throw e;}});},
  diagnostics:{nodeCount:nodes.length,method:'same-direction-Q-L-centered-normalized-arithmetic-v1',
   minPreparationA:Math.min(...nodes.map(n=>n.diagnostics.minA)),minPreparationD:Math.min(...nodes.map(n=>n.diagnostics.minD)),
   scope:'Exactly the centered Q/L trial curve in real arithmetic. Physical raw conversion omitted; original F and acceptance retained.'}};
}

export function createGeometricTrialHook(cells,{spacing}={}){
 let previousStates=null,previousDelta=null,prepared=null;
 const statistics={preparations:0,trialCalls:0,lastPreparation:null};
 function retractTrial(states,delta,lambda){
  statistics.trialCalls++;
  if(states!==previousStates||delta!==previousDelta||!prepared){
   prepared=null;const next=prepareGeometricShootingRetraction(states,delta,cells,{spacing});
   prepared=next;previousStates=states;previousDelta=delta;statistics.preparations++;statistics.lastPreparation=next.diagnostics;
  }
  return prepared.step(lambda);
 }
 return {retractTrial,statistics};
}
