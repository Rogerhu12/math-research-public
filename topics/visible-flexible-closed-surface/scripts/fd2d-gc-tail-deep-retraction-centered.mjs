// R95 numerical centering: the same exact Q/L retraction and original F.
// Subtract the same base conversion used at every trial, so a zero raw
// increment has no floating coordinate-roundtrip bias.  No floor or mean
// equation is changed.  This does not promise a smaller whole residual.
import {prepareGeometricNodeRetraction as prepareDifferential} from './fd2d-gc-tail-deep-retraction-differential.mjs';
import {initializeFromRawWithMeanGuess} from './fd2d-gc-tail-deep-retraction-mean.mjs';
export {initializeFromRawWithMeanGuess} from './fd2d-gc-tail-deep-retraction-mean.mjs';

export function prepareGeometricNodeRetraction(options){
 const {engine,profile,x,portRatio=1}=options,{M}=engine,K=2*M,
  base=Float64Array.from(options.state),delta=Float64Array.from(options.delta),y=new Float64Array(K+2);
 for(let j=0;j<M;j++){y[j]=base[j];y[M+j]=base[M+j]*portRatio;}
 const root=options.knownRoot??engine.root(y,profile,x),mean0=root.L[0],
  differential=prepareDifferential({...options,knownRoot:root}),
  {raw,rawDirection,meanLDirection}=differential,
  anchor=initializeFromRawWithMeanGuess(engine,raw,profile,x,mean0),
  anchorPi=Float64Array.from(anchor.state.slice(M,K)),
  anchorMeanL=anchor.L[0];
 const diagnostics={...differential.diagnostics,
  method:'same-direction-Q-L-Newton-retraction-centered-v3',
  meanInitialization:'base L0 plus lambda times exact directional dL0',
  coordinateCentering:'base pi plus [C(raw+lambda*deltaRaw)-C(raw)]pi, then divide the increment by portRatio',
  maxUncenteredAnchorBias:Math.max(...Array.from(anchorPi,(v,j)=>Math.abs(v/portRatio-base[M+j]))),
  anchorMeanResidual:anchor.normalizedMeanResidual};
 function step(lambda,{detail=false}={}){
  if(!Number.isFinite(lambda))throw Error('Retraction step is not finite');
  if(lambda===0)return {state:Float64Array.from(base),diagnostics:{...diagnostics,lambda,exactZeroStep:true}};
  const trialRaw=Float64Array.from(raw,(v,j)=>rawDirection[j]===0?v:v+lambda*rawDirection[j]),
   predictedMean=meanLDirection===0?mean0:mean0+lambda*meanLDirection,
   initialized=initializeFromRawWithMeanGuess(engine,trialRaw,profile,x,predictedMean),
   state=Float64Array.from(base,(v,j)=>delta[j]===0?v:v+lambda*delta[j]);
  for(let j=0;j<M;j++){
   const increment=(initialized.state[M+j]-anchorPi[j])/portRatio;
   // Keep even signed zero coordinates unchanged for a genuinely zero
   // converted increment.  The centering itself is evaluated above.
   state[M+j]=increment===0?base[M+j]:base[M+j]+increment;
  }
  const info={lambda,normalizedMeanResidual:initialized.normalizedMeanResidual,meanIterations:initialized.meanIterations};
  if(detail)Object.assign(info,{minA:initialized.minA,minD:initialized.minD,minS:initialized.minS,
   meanL:initialized.L[0],meanLChange:initialized.L[0]-mean0,meanLLinearPrediction:predictedMean,
   meanLChangeFromConvertedAnchor:initialized.L[0]-anchorMeanL,
   canonicalLinearDifference:Math.max(...Array.from(state,(v,j)=>Math.abs(v-base[j]-lambda*delta[j])))});
  return {state,diagnostics:info};
 }
 return {step,diagnostics,raw,rawDirection,meanLDirection};
}

export function prepareGeometricShootingRetraction(states,delta,cells,{spacing}={}){
 if(states.length!==cells.length+1||delta.length!==states.length)throw Error('Geometric shooting node counts differ');
 const nodes=[];
 for(let i=0;i<states.length;i++){
  const cell=cells[i===0?0:i-1],profile=i===0?cell.profiles.at(-1):cell.profiles[0],x=i===0?1:0,
   portRatio=i===0?cell.portRatio:1;
  try{nodes.push(prepareGeometricNodeRetraction({engine:cell.engine,profile,x,state:states[i],delta:delta[i],spacing,portRatio}));}
  catch(error){const failure=Error(`Geometric retraction preparation at node ${i}: ${String(error)}`);failure.node=i;failure.cause=error;throw failure;}
 }
 return {
  step(lambda){return nodes.map((node,i)=>{
   try{return Array.from(node.step(lambda).state);}
   catch(error){const failure=Error(`Geometric retraction trial at node ${i}: ${String(error)}`);failure.node=i;failure.cause=error;throw failure;}
  });},
  diagnostics:{nodeCount:nodes.length,method:'same-direction-Q-L-Newton-retraction-centered-v3',
   minPreparationA:Math.min(...nodes.map(v=>v.diagnostics.minA)),
   minPreparationD:Math.min(...nodes.map(v=>v.diagnostics.minD)),
   scope:'The original residual, correction, branch floor, mean equation and acceptance criterion remain unchanged.'}
 };
}

export function createGeometricTrialHook(cells,{spacing}={}){
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
