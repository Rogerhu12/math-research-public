// R95 mean-seeded version. All equations, floors and stopping thresholds
// are the original initializeFromRaw equations; only L0's initial guess
// is the base root plus its differential, instead of the unrelated zero.
import {prepareGeometricNodeRetraction as prepareDifferential} from './78718-tail-geometric-newton-retraction.mjs';

export function initializeFromRawWithMeanGuess(engine,raw,profile,x,meanGuess){
 const {M,orientation,mu}=engine,g=engine.geometry(profile,x),Q=Float64Array.from(raw.slice(0,M)),
  L=new Float64Array(M+1),sq2=Math.sqrt(2),sq12=Math.sqrt(12);
 if(!Number.isFinite(meanGuess))throw Error('Geometric mean predictor is not finite');
 L[0]=meanGuess;
 for(let j=0;j<M;j++)L[j+1]=sq12*g.r**3*raw[M+j]/(sq2*g.w);
 let e,iterations;
 for(let it=0;it<30;it++){
  iterations=it;
  e=engine.evaluateL(L,Q,g,true);
  const error=e.moments[0],scale=Math.max(1e-300,e.maxQuad,Math.abs(L[0]));
  if(Math.abs(error)<=8e-14*scale)break;
  const step=error/e.B[0];let accepted=false;
  for(let k=0;k<20;k++){
   const trial=Float64Array.from(L);trial[0]-=step*2**(-k);
   try{
    const candidate=engine.evaluateL(trial,Q,g,false);
    if(Math.abs(candidate.moments[0])<Math.abs(error)){L.set(trial);accepted=true;break;}
   }catch(_){}
  }
  if(!accepted)throw Error('Geometric seeded full mean root failed');
  if(it===29)throw Error('Geometric seeded mean iteration limit');
 }
 e=engine.evaluateL(L,Q,g,true);
 const state=new Float64Array(2*M+2),factor=orientation*sq2*g.r**4*g.w2/(sq12*mu);
 state.set(Q);for(let j=0;j<M;j++)state[M+j]=factor*e.moments[j+1];
 return {state,L,g,meanPhysical:g.w*L[0],normalizedMeanResidual:e.moments[0],
  meanIterations:iterations,minA:e.minA,minD:e.minD,minS:e.minS};
}

export function prepareGeometricNodeRetraction(options){
 const {engine,profile,x,spacing,portRatio=1}=options,{M}=engine,K=2*M,
  base=Float64Array.from(options.state),delta=Float64Array.from(options.delta),y=new Float64Array(K+2);
 for(let j=0;j<M;j++){y[j]=base[j];y[M+j]=base[M+j]*portRatio;}
 const root=options.knownRoot??engine.root(y,profile,x),mean0=root.L[0],
  differential=prepareDifferential({...options,knownRoot:root}),
  {raw,rawDirection,meanLDirection}=differential;
 const diagnostics={...differential.diagnostics,
  method:'same-direction-Q-L-Newton-retraction-mean-seeded-v2',
  meanInitialization:'base L0 plus lambda times exact directional dL0'};
 function step(lambda,{detail=false}={}){
  if(!Number.isFinite(lambda))throw Error('Retraction step is not finite');
  if(lambda===0)return {state:Float64Array.from(base),diagnostics:{...diagnostics,lambda,exactZeroStep:true}};
  const trialRaw=Float64Array.from(raw,(v,j)=>v+lambda*rawDirection[j]),
   predictedMean=mean0+lambda*meanLDirection,
   initialized=initializeFromRawWithMeanGuess(engine,trialRaw,profile,x,predictedMean),
   state=Float64Array.from(base,(v,j)=>v+lambda*delta[j]);
  for(let j=0;j<M;j++){state[j]=initialized.state[j];state[M+j]=initialized.state[M+j]/portRatio;}
  const info={lambda,normalizedMeanResidual:initialized.normalizedMeanResidual,meanIterations:initialized.meanIterations};
  if(detail)Object.assign(info,{minA:initialized.minA,minD:initialized.minD,minS:initialized.minS,
   meanL:initialized.L[0],meanLChange:initialized.L[0]-mean0,meanLLinearPrediction:predictedMean,
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
  diagnostics:{nodeCount:nodes.length,method:'same-direction-Q-L-Newton-retraction-mean-seeded-v2',
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
