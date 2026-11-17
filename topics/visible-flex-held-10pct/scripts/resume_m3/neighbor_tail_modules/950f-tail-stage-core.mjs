// Own numerical shooting subdivision; original source is read-only.
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {pathToFileURL} from 'node:url';
import {subdividePhysical,buildStableStageGraphs} from './950f-tail-subdivision.mjs';
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const sourceURL=name=>pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',name));
// Derived from frozen root multiple-shooting blob 2f1544ca9c8c11fe4a387047f693aa44d2013bb4.
// Added actual radial orientation and absolute node index; parent source is unmodified.
// Author: nonlinear_tail_match (AI assisted), 2026-11-08.
// Finite-mode finite-depth tool only; not a C2 infinite-tail or closed solution certificate.
const {createMomentumTailEngine}=await import(sourceURL('general_root_tail_momentum.mjs'));
const {createFastMomentumTailEngine}=await import(sourceURL('f6tail_fast_momentum.mjs'));
const {createCompactControlledTail}=await import(sourceURL('f6tail_compact_controlled_tail.mjs'));
const {buildWarpTailGraphs}=await import(sourceURL('f6tail_warp_linear.mjs'));
const {buildProjectivePhysicalTailGraph}=await import(sourceURL('f6tail_height_line_transport.mjs'));
const {createMomentumPhysicalJetEvaluator}=await import(sourceURL('f6tail_momentum_physical_jets.mjs'));
const {actualMetricFromDarbouxJets}=await import(sourceURL('f6tail_actual_metric.mjs'));
const {installCompactCriticalPoints,withCuspAwareRK}=await import(sourceURL('f6tail_cusp_grid.mjs'));
function denseSolve(a,b,n){
 const A=Float64Array.from(a),x=Float64Array.from(b);
 for(let k=0;k<n;k++){
  let p=k;for(let i=k+1;i<n;i++)if(Math.abs(A[i*n+k])>Math.abs(A[p*n+k]))p=i;
  if(!(Math.abs(A[p*n+k])>1e-280))throw new Error("tail graph chart singular");
  if(p!==k){for(let j=k;j<n;j++){const t=A[k*n+j];A[k*n+j]=A[p*n+j];A[p*n+j]=t;}const t=x[k];x[k]=x[p];x[p]=t;}
  for(let i=k+1;i<n;i++){const f=A[i*n+k]/A[k*n+k];A[i*n+k]=0;for(let j=k+1;j<n;j++)A[i*n+j]-=f*A[k*n+j];x[i]-=f*x[k];}
 }
 for(let i=n-1;i>=0;i--){for(let j=i+1;j<n;j++)x[i]-=A[i*n+j]*x[j];x[i]/=A[i*n+i];}
 return x;
}
function matrixProduct(a,b,n){
 const c=new Float64Array(n*n);for(let i=0;i<n;i++)for(let j=0;j<n;j++)for(let k=0;k<n;k++)c[i*n+j]+=a[i*n+k]*b[k*n+j];return c;
}
function matrixVector(a,b,n){
 const c=new Float64Array(n);for(let i=0;i<n;i++)for(let j=0;j<n;j++)c[i]+=a[i*n+j]*b[j];return c;
}
function matrixInverse(a,n){
 const inv=new Float64Array(n*n);for(let j=0;j<n;j++){const b=new Float64Array(n);b[j]=1;const x=denseSolve(a,b,n);for(let i=0;i<n;i++)inv[i*n+j]=x[i];}return inv;
}
function infinityNorm(a,n){
 let v=0;for(let i=0;i<n;i++){let s=0;for(let j=0;j<n;j++)s+=Math.abs(a[i*n+j]);v=Math.max(v,s);}return v;
}
function sparseGlobalSolve(payload){
 const helper=process.env.VISIBLE_FLEX_SPARSE_LINEAR_HELPER;
 if(!helper)throw new Error('VISIBLE_FLEX_SPARSE_LINEAR_HELPER required');
 const r=spawnSync(process.env.VISIBLE_FLEX_SPARSE_PYTHON??'python3',[helper],{input:JSON.stringify(payload),encoding:'utf8',maxBuffer:128*1024*1024});
 if(r.status!==0)throw new Error('Sparse original linear system failed: '+(r.stderr??'').slice(-2000));
 const out=JSON.parse(r.stdout);
 if(!(out.normwise_backward_error<1e-11))throw new Error('Sparse linear backward-error verification failed '+out.normwise_backward_error);
 return out;
}
function oneUlpInteriorCandidate(states,ev,scales){
 let largest=0,stage=-1,component=-1;
 for(let n=0;n<ev.residuals.length;n++)for(let j=0;j<ev.residuals[n].length;j++){
  const value=Math.abs(ev.residuals[n][j])/scales[n];
  if(value>largest){largest=value;stage=n;component=j;}
 }
 if(stage<=0||stage>=states.length-1||largest!==ev.norm)return null;
 const before=states[stage][component],after=ev.flows[stage].out[component];
 if(!Number.isFinite(before)||!Number.isFinite(after)||before===after)return null;
 const bits=new DataView(new ArrayBuffer(16));
 bits.setFloat64(0,before,false);bits.setFloat64(8,after,false);
 const a=bits.getBigUint64(0,false),b=bits.getBigUint64(8,false);
 if((a>b?a-b:b-a)!==1n)return null;
 const trial=states.map(row=>Float64Array.from(row));trial[stage][component]=after;
 return {states:trial,metadata:{stage,component,before,after,absoluteChange:after-before,
   binary64NeighborDistance:1,previousNormalizedResidual:ev.norm}};
}

export function createCompactTailShooting(options={}){
 const {modes=2,spacing=6,depth:physicalDepth=8,steps=64,quadrature=128,linearFar=48,linearSteps=512,projectionFloor=.05,linearMethod='matrix',fastJacobian=false}=options;
 const physical=options.tail??createCompactControlledTail(options),cuspAwareFlow=options.cuspAwareFlow===true;
 if(cuspAwareFlow&&!fastJacobian)throw Error('cuspAwareFlow requires the optional fastJacobian variational engine');
 // The weighted factory provides actual capped-profile critical points; keep them unchanged.
 const {delta0,R,a,etaPower,etaRatioAtN0,epsilonScale,rCuff,orientation,calibrationSteps}=physical.parameters;
 const nodeIndex=0,farPadding=linearFar-physicalDepth,M=modes,K=2*M,portRatio=2**a;
 const geometry={leftCells:physical.cells,rightCells:physical.cells,linearDeepParameters:physical.linearDeepParameters,momentumNormalization:1};
 const stages=subdividePhysical(physical,physicalDepth,options.shootingParts??1),depth=stages.cells.length;
 const wholeGraph=buildStableStageGraphs(physical,stages,{modes:M,spacing,linearFar,linearSteps});
 const engineFactory=fastJacobian?createFastMomentumTailEngine:createMomentumTailEngine;
 // Same-mu allocation cache is local to this one fixed-options DN.
 const engineCache=new Map();
 const graphs=wholeGraph.graphs,gains=wholeGraph.gains,cells=stages.cells.map(c=>{
  if(!engineCache.has(c.mu)){
   const e=engineFactory({modes:M,spacing,quadrature,mu:c.mu,orientation,projectionFloor});
   engineCache.set(c.mu,cuspAwareFlow?withCuspAwareRK(e):e);
  }
  return {...c,engine:engineCache.get(c.mu)};
 });
 const nodeR=Array.from({length:depth+1},(_,n)=>n===0?cells[0].profiles.at(-1)(1).r:cells[n-1].profiles[0](0).r);
 function initial(target){
  const states=Array.from({length:depth+1},()=>new Float64Array(K));
  states[0].set(target);for(let j=0;j<M;j++)states[0][M+j]=graphs[0][j]*target[j];
  for(let n=0;n<depth;n++)for(let j=0;j<M;j++){
   states[n+1][j]=states[n][j]/gains[n][j];states[n+1][M+j]=graphs[n+1][j]*states[n+1][j];
  }return states;
 }
 function cellFlow(n,input,withJac){
  const c=cells[n],s=new Float64Array(K+2);s.set(input);
  let f;
  if(withJac)f=c.engine.flowStateWithJacobian(s,c.profiles,{stepsPerSegment:steps});
  else{
   let state=s;
   for(const profile of c.profiles)for(let k=0;k<steps;k++)state=c.engine.rk4(state,profile,k/steps,1/steps);
   f={state};
  }
  const out=Float64Array.from(f.state.slice(0,K),(v,j)=>j<M?v:v/c.portRatio);
  let J=null;if(withJac){J=new Float64Array(K*K);for(let i=0;i<K;i++)for(let j=0;j<K;j++)J[i*K+j]=f.tangent[i*K+j]/(i<M?1:c.portRatio);}
  return {out,J,meanHeight:f.state[K]+f.state[K+1],minA:f.minA,minD:f.minD};
 }
 function scaleFor(target){
  const s=new Float64Array(depth+1);s[0]=Math.max(1e-250,...Array.from(target,Math.abs));
  for(let n=0;n<depth;n++)s[n+1]=s[n]/Math.abs(gains[n][0]);return s;
 }
 function evaluate(states,target,withJac,scales){
  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity;
  for(let n=0;n<depth;n++){
   const f=cellFlow(n,states[n+1],withJac),r=Float64Array.from(f.out,(v,j)=>v-states[n][j]);
   norm=Math.max(norm,...Array.from(r,v=>Math.abs(v)/scales[n]));flows.push(f);residuals.push(r);
   if(withJac){minA=Math.min(minA,f.minA);minD=Math.min(minD,f.minD);}
  }
  const end=new Float64Array(M);for(let j=0;j<M;j++){end[j]=states[depth][M+j]-graphs[depth][j]*states[depth][j];norm=Math.max(norm,Math.abs(end[j])/scales[depth]);}
  for(let j=0;j<M;j++)norm=Math.max(norm,Math.abs(states[0][j]-target[j])/scales[0]);
  return {flows,residuals,end,norm,minA,minD};
 }
 function correction(ev,states,target){
  const ans=sparseGlobalSolve({mode:'correction',M,depth,Js:ev.flows.map(f=>Array.from(f.J)),scales:Array.from(scaleFor(target)),deepGraph:Array.from(graphs[depth]),residuals:ev.residuals.map(v=>Array.from(v)),deepEnd:Array.from(ev.end),targetDelta:Array.from(target,(v,j)=>v-states[0][j])});
  return {delta:ans.delta.map(v=>Float64Array.from(v)),maxChartCondition:null,sparseLinear:ans};
 }
 function solve(target,opts={}){
  const scales=scaleFor(target);let states=opts.initial?opts.initial.map(x=>Float64Array.from(x)):initial(target);
  const history=[];let last;
  for(let it=0;it<(opts.maxIterations??8);it++){
   const ev=evaluate(states,target,true,scales);last=ev;history.push({iteration:it,norm:ev.norm,minA:ev.minA,minD:ev.minD});opts.progress?.(history.at(-1),states.map(v=>Array.from(v)));
   if(ev.norm<(opts.tolerance??1e-10))break;
   const cor=correction(ev,states,target);history.at(-1).chartCondition=cor.maxChartCondition;opts.progress?.({...history.at(-1),phase:'correction'});
   let accepted=false;
   for(let k=0;k<10;k++){
    const lambda=2**(-k),trial=states.map((s,n)=>Float64Array.from(s,(v,j)=>v+lambda*cor.delta[n][j]));
    try{const test=evaluate(trial,target,false,scales);if(test.norm<ev.norm){states=trial;history.at(-1).step=lambda;accepted=true;break;}}catch(_){}
   }
   if(!accepted&&options.oneUlpInitialRetry===true){
    const candidate=oneUlpInteriorCandidate(states,ev,scales);
    if(candidate){
     try{
      const check=evaluate(candidate.states,target,true,scales);
      opts.progress?.({...history.at(-1),phase:'one_ulp_initial_candidate',
        candidate:candidate.metadata,candidateNormalizedResidual:check.norm});
      if(check.norm<(opts.tolerance??1e-10)){
       states=candidate.states;last=check;
       history.push({iteration:it+1,norm:check.norm,minA:check.minA,minD:check.minD,
         oneUlpInitialCandidate:candidate.metadata});
       opts.progress?.(history.at(-1),states.map(v=>Array.from(v)));
       break;
      }
     }catch(error){opts.progress?.({...history.at(-1),phase:'one_ulp_initial_candidate_error',error:String(error)});}
    }
   }
   if(!accepted)throw new Error("multiple-shooting line search failed at "+ev.norm);
  }
  if(!last||last.norm>=(opts.tolerance??1e-10)){last=evaluate(states,target,true,scales);}
  const rawCut=cells[0].engine;const portProfile=cells[0].profiles.at(-1);
  // Node0 pi is normalized by mu_-1=2^a mu_0; convert back to the cell0 engine normalization.
  const state0=new Float64Array(K+2);state0.set(states[0]);for(let j=0;j<M;j++)state0[M+j]*=portRatio;
  const cut=rawCut.toRaw(state0,portProfile,1);
  return {parameters:{...physical.parameters,modes:M,spacing,depth,physicalDepth,shootingParts:stages.parts,steps,quadrature,linearFar,linearSteps,linearMethod:'stable-momentum-cusp-subdivision',projectionFloor,farPadding,nodeIndex},
   ...(opts.jacobian?{linearizedFlowJacobians:last.flows.map(f=>Array.from(f.J))}:{}),
   states:states.map(x=>Array.from(x)),cutRaw:Array.from(cut.raw),cutMeanPhysical:cut.meanPhysical,cutRadius:nodeR[0],
   history,normalizedResidual:last.norm,minA:last.minA,minD:last.minD,
   meanHeightToCut:last.flows.reduce((sum,f)=>sum+f.meanHeight,0),
   linearGraphAtCut:Array.from(graphs[0]),linearGraphAtDeep:Array.from(graphs[depth]),nodeRadius:nodeR,
   converged:last.norm<(opts.tolerance??1e-10),
   scope:"Finite-M, finite-depth nonlinear boundary response. Deep graph is nonzero linear flat data; depth/mode/radial convergence and true infinite-tail certification remain separate."};
 }
 return {solve,initial,evaluate,cells,graphs,gains,physical,rawNode:stages.rawNode,parameters:{...physical.parameters,modes:M,spacing,depth,physicalDepth,shootingParts:stages.parts,steps,quadrature,linearFar,linearSteps,linearMethod:'stable-momentum-cusp-subdivision',projectionFloor,farPadding,nodeIndex}};
}


export function createCompactTailDN(options={}){
 const tail=createCompactTailShooting(options),M=tail.parameters.modes,spacing=tail.parameters.spacing,K=2*M,N=tail.parameters.quadrature,rho=2**tail.parameters.a,engine=tail.cells[0].engine,profile=tail.cells[0].profiles.at(-1),jetsEvaluator=createMomentumPhysicalJetEvaluator(engine,{spacing});
 function cutJets(node){
  const y=new Float64Array(K+2);y.set(node);for(let j=0;j<M;j++)y[M+j]*=rho;
  const rt=engine.root(y,profile,1),jets=jetsEvaluator(y,profile,1),g=rt.g,field=engine.rhs(y,profile,1,false,rt),slope=new Float64Array(M),second=new Float64Array(M),sigma=g.drdx/g.r,k=g.dlogwdx;
  for(let j=0;j<M;j++){const m2=(spacing*(j+1))**2;slope[j]=m2*g.r**3*y[j]+Math.sqrt(2)*g.w*rt.L[j+1];second[j]=(m2*g.r**3*(field[j]+3*sigma*y[j])+Math.sqrt(2)*g.w*(jets.Ldot[j+1]+k*rt.L[j+1]))/g.drdx;}
  const meanSlopeCorrection=g.w*rt.L[0],meanSecondCorrection=g.w*(k*rt.L[0]+jets.Ldot[0])/g.drdx,backgroundSecond=g.w*k/g.drdx;
  return {radius:g.r,backgroundSlope:g.w,backgroundSecond,E:g.E,Ep:2*g.w2*k/g.drdx,height:Array.from(node.slice(0,M),v=>g.r**4*v),slope:Array.from(slope),second:Array.from(second),meanSlope:g.w+meanSlopeCorrection,meanSecond:backgroundSecond+meanSecondCorrection,meanSlopeCorrection,meanSecondCorrection,minLeading:jets.minA,minD:jets.minD,endpointFullD:jets.maxDarboux,endpointPhi:jets.physicalHolonomyResidual,formalCurvature:jets.formalHeightCurvature};
 }
 const graphCache=new WeakMap();
 function tangentGraphAtCut(sol){
  if(graphCache.has(sol))return graphCache.get(sol);
  if(sol.states.length!==tail.parameters.depth+1||sol.states[0].length!==K)throw Error('DN tangent checkpoint dimensions disagree');
  const states=sol.states.map(v=>Float64Array.from(v)),target=states[0].slice(0,M),scales=new Float64Array(states.length);
  scales[0]=Math.max(1e-250,...target.map(Math.abs));
  for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(tail.gains[n][0]);
  const Js=sol.linearizedFlowJacobians??tail.evaluate(states,target,true,scales).flows.map(f=>Array.from(f.J));
  const ans=sparseGlobalSolve({mode:'tangent',M,depth:Js.length,Js,scales:Array.from(scales),deepGraph:Array.from(tail.graphs[Js.length])});
  const G=Float64Array.from(ans.graph);graphCache.set(sol,G);return G;
 }
 function heightJetJacobian(sol,{differenceStep=1e-4}={}){
  const G=tangentGraphAtCut(sol),base=Float64Array.from(sol.states[0]),scale=Math.max(1e-250,...base.slice(0,M).map(Math.abs)),r=profile(1).r,J=new Float64Array((3*M+2)*M);
  for(let k=0;k<M;k++){const h=differenceStep*Math.max(Math.abs(base[k]),.1*scale),plus=Float64Array.from(base),minus=Float64Array.from(base);plus[k]+=h;minus[k]-=h;for(let j=0;j<M;j++){plus[M+j]+=h*G[j*M+k];minus[M+j]-=h*G[j*M+k];}const a=cutJets(plus),b=cutJets(minus),av=[...a.slope,...a.second,a.meanSlopeCorrection,a.meanSecondCorrection,...a.height],bv=[...b.slope,...b.second,b.meanSlopeCorrection,b.meanSecondCorrection,...b.height];for(let j=0;j<av.length;j++)J[j*M+k]=(av[j]-bv[j])/(2*h*r**4);}
  return {matrix:Array.from(J),graph:Array.from(G),rows:['slope[m]','second[m]','meanSlopeCorrection','meanSecondCorrection','height[m]'],columns:'physical cut height Fourier coefficients',differenceStep};
 }

 function audit(sol,steps=tail.parameters.steps){let fullD=0,normalizedFullDefect=0,minLeading=Infinity,minD=Infinity,formalCurvature=0,maxPhysicalPV=0,actualMetric=0,holonomy=0;for(let n=0;n<tail.cells.length;n++){const c=tail.cells[n],ev=createMomentumPhysicalJetEvaluator(c.engine,{spacing});let y=new Float64Array(K+2);y.set(sol.states[n+1]);for(const p of c.profiles)for(let k=0;k<=steps;k++){const x=k/steps,g=c.engine.geometry(p,x),j=ev(y,p,x),metric=actualMetricFromDarbouxJets(g,j.perAngle);fullD=Math.max(fullD,j.maxDarboux);minLeading=Math.min(minLeading,j.minA);minD=Math.min(minD,j.minD);formalCurvature=Math.max(formalCurvature,j.formalHeightCurvature);maxPhysicalPV=Math.max(maxPhysicalPV,j.peakValley);actualMetric=Math.max(actualMetric,metric.actualMetricRelativeOperatorError);holonomy=Math.max(holonomy,Math.abs(j.physicalHolonomyResidual));for(const t of j.perAngle)normalizedFullDefect=Math.max(normalizedFullDefect,Math.abs(t.darboux*g.E*g.E*g.r*g.drdx/g.w2));if(k<steps)y=c.engine.rk4(y,p,x,1/steps);}}return {fullD,normalizedFullDefect,minLeading,minD,formalCurvature,maxPhysicalPV,actualMetric,holonomy};}
 return {tail,cutJets,audit,tangentGraphAtCut,heightJetJacobian,solve(height,opts={}){const r=profile(1).r,target=Float64Array.from(height,v=>v/r**4),sol=tail.solve(target,opts),result={...sol,jets:cutJets(sol.states[0]),audit:opts.audit?audit(sol,opts.auditSteps??tail.parameters.steps):null};if(opts.jacobian){const j=heightJetJacobian(result);result.graphJacobian=j.graph;result.heightJetJacobian=j.matrix;result.heightJetJacobianRows=j.rows;}return result;}};
}
