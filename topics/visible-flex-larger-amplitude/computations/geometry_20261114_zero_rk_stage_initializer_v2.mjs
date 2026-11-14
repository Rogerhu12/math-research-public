// Initial guesses only for the unchanged complete finite native tail.
// Uses the exact zero-state linearization of the original split-flux/Fourier
// RHS, the current stage profiles, and the ORIGINAL variational RK grid.
// The original graphs, gains, far Robin data, scales, evaluate/Newton/J/audit
// are never changed. All numerical use belongs to the public Actions.
import fs from 'node:fs';
import crypto from 'node:crypto';

// V2 changes only candidate construction diagnostics and a non-native
// determinant veto: a FINITE rounded zero determinant does not enter the
// chart formula. Nonfinite values, zero chart denominators and nonzero
// prediction underflow still fail. No invertibility/accuracy is asserted.
const SCHEMA='same-native-RK-zero-stage-initializer-v2';
const OWN_SHA=crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex');
const IO_KEYS=new Set(['traceFile','iterationCheckpointFile','trialDiagnosticFile',
  'trialStatePrefix','initialCheckpoint']);
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
const fail=message=>{throw Error('Zero-RK initializer: '+message);};
const isVector=value=>Array.isArray(value)||(ArrayBuffer.isView(value)&&!(value instanceof DataView));

function finiteVector(value,length,label){
  if(!isVector(value)||value.length!==length)fail(label+' has the wrong full dimension');
  for(let j=0;j<length;j++)if(typeof value[j]!=='number'||!Number.isFinite(value[j]))
    fail(label+' contains a nonfinite number at '+j);
}
function binary(values){
  const out=Buffer.allocUnsafe(values.length*8);
  for(let j=0;j<values.length;j++)out.writeDoubleLE(values[j],8*j);
  return out;
}
function identityTree(value){
  if(value===null)return ['null'];
  if(typeof value==='number'){
    if(!Number.isFinite(value))fail('nonfinite identity number');
    return ['f64le',binary([value]).toString('hex')];
  }
  if(typeof value==='string'||typeof value==='boolean')return [typeof value,value];
  if(isVector(value))return ['array',Array.from(value,identityTree)];
  if(value&&typeof value==='object'){
    const proto=Object.getPrototypeOf(value);
    if(proto!==Object.prototype&&proto!==null)fail('identity needs plain JSON data');
    return ['object',Object.keys(value).sort().filter(k=>value[k]!==undefined)
      .map(k=>[k,identityTree(value[k])])];
  }
  fail('unsupported identity value');
}
const identityHash=value=>sha(Buffer.from(JSON.stringify(identityTree(value))));

function sourceIdentityRecord(value){
  if(!value||typeof value!=='object'||!value.sourceSHA256||
     !Object.keys(value.sourceSHA256).length||!value.physicalIdentity||!value.backendIdentity)
    fail('supply the consumed source SHA map, physical identity and backend identity');
  for(const [name,digest] of Object.entries(value.sourceSHA256))
    if(!name||typeof digest!=='string'||!/^[a-f0-9]{64}$/.test(digest))
      fail('invalid supplied source digest: '+name);
  // These are caller-supplied identities, not a substitute for the caller's
  // existing pinned-source/physical-profile checks.
  return {sha256:identityHash(value),sourceSHA256:{...value.sourceSHA256},
    physicalIdentitySHA256:identityHash(value.physicalIdentity),
    backendIdentitySHA256:identityHash(value.backendIdentity),
    callerMustVerifyConsumedSourceAndPhysicalIdentities:true};
}

function liveSnapshot(tail){
  const parameters=Object.fromEntries(Object.entries(tail.parameters).filter(([k])=>!IO_KEYS.has(k)));
  return {parameters,rawNode:Array.from(tail.rawNode),
    stages:tail.cells.map((cell,index)=>({
      stage:index,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
      rawLeft:cell.rawLeft,rawRight:cell.rawRight,part:cell.part,parts:cell.parts,
      portRatio:cell.portRatio,mu:cell.mu,
      profileIntegrationBreakpoints:cell.profiles.map(p=>Array.from(p.integrationBreakpoints??[]))
    })),
    graphs:tail.graphs.map(row=>Array.from(row)),gains:tail.gains.map(row=>Array.from(row))};
}

// Literal zero-state specialization of 78718-tail-fourier-product-jacobian.
// Retain its product order instead of replacing it by log/exp linear-column
// expressions. The complete zero-state nonlinear moment corrections vanish.
// At a nonzero base this 2x2 specialization must NOT be used as its full J.
function zeroBlockCoefficients(g,mu,frequency){
  const sq2=Math.sqrt(2),sq12=Math.sqrt(12);
  if(!(g.r>0&&g.w>0&&g.w2>0&&g.drdx!==0)||
     ![g.r,g.w,g.w2,g.drdx,mu].every(Number.isFinite)||!(mu>0))
    fail('the original geometry left its zero-state point domain');
  const sigma=g.drdx/g.r,
    pref=sq2*g.r**3*g.drdx*g.w2/(sq12*mu),
    targetFac=sq12*mu/(sq2*g.r**4*g.w2),
    pFac=g.r**3/(sq2*g.w),
    f=frequency;
  const result=[
    sigma*(f*f-4),
    sigma*(sq2*g.w*targetFac/g.r**3),
    -pref*f*f*(f*f-1)*pFac,
    (4-f*f)*sigma
  ];
  finiteVector(result,4,'zero-state local block');
  return result;
}
function product(a,b){
  // Both are 2x2 row-major; the two nonzero terms occur in the same order
  // as their physical-Q then momentum columns in the original full product.
  return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
          a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]];
}
function increment(base,field,h){
  return base.map((v,j)=>v+h*field[j]);
}
function advanceBlock(t,a0,am,a1,h){
  const k1=product(a0,t),
    k2=product(am,increment(t,k1,h/2)),
    k3=product(am,increment(t,k2,h/2)),
    k4=product(a1,increment(t,k3,h));
  const out=t.map((v,j)=>v+h*(k1[j]+2*k2[j]+2*k3[j]+k4[j])/6);
  finiteVector(out,4,'zero-state RK stage block');
  return out;
}
function validGrid(grid,label){
  if(!isVector(grid)||grid.length<2||grid[0]!==0||grid.at(-1)!==1)
    fail(label+' must run from zero to one');
  finiteVector(grid,grid.length,label);
  for(let j=1;j<grid.length;j++)if(!(grid[j]>grid[j-1]))
    fail(label+' is not strictly increasing');
}

function observedNumber(x){
  if(Number.isFinite(x))return x;
  return {nonfinite:Number.isNaN(x)?'NaN':x>0?'positive-infinity':'negative-infinity'};
}
function blockObservation(t,stage,modeIndex,spacing){
  const ad=t[0]*t[3],bc=t[1]*t[2],det=ad-bc,
    allFinite=t.every(Number.isFinite),termsFinite=[ad,bc,det].every(Number.isFinite);
  let relative=null;
  if(termsFinite){
    const scale=Math.max(Math.abs(ad),Math.abs(bc));
    relative=scale===0?0:(Math.abs(det)/scale)/(Math.abs(ad)/scale+Math.abs(bc)/scale);
  }
  return {stage,zero_based_mode_index:modeIndex,mode:modeIndex+1,frequency:spacing*(modeIndex+1),
    T_row_major:t.map(observedNumber),ad:observedNumber(ad),bc:observedNumber(bc),
    determinant:observedNumber(det),all_entries_finite:allFinite,
    products_and_determinant_finite:termsFinite,
    finite_rounded_zero_determinant:termsFinite&&det===0,
    relative_cancellation_abs_det_over_abs_ad_plus_abs_bc:relative,
    both_determinant_products_zero:termsFinite&&ad===0&&bc===0,
    invertibility_and_linear_accuracy_not_claimed:true};
}

export function createZeroRKStageInitializer(dn,options={}){
  if(options.onConstructionEvent!==undefined&&typeof options.onConstructionEvent!=='function')
    fail('onConstructionEvent must be a diagnostic callback');
  let eventSequence=0;
  const emit=record=>options.onConstructionEvent?.({
    schema:'same-native-RK-v2-construction-evidence-v1',
    initializer_source_sha256:OWN_SHA,sequence:eventSequence++,...record});
  if(process.env.GITHUB_ACTIONS!=='true'||
     process.env.GITHUB_REPOSITORY!=='Rogerhu12/math-research-public')
    fail('run numerical construction only in this public repository Actions');
  const tail=dn?.tail,p=tail?.parameters;
  if(!p||!Array.isArray(tail.cells)||!Array.isArray(tail.graphs)||!Array.isArray(tail.gains))
    fail('supply the live complete original DN');
  const M=p.modes,K=2*M,depth=tail.cells.length,steps=p.steps,
    radius=options.radius,expectedSteps=options.expectedSteps??12;
  if(!Number.isSafeInteger(M)||M<1||!Number.isSafeInteger(depth)||depth<1||
     !Number.isSafeInteger(steps)||steps<1||steps!==expectedSteps||
     p.depth!==depth||p.orientation!==1||p.rhsEvaluation!=='split-linear-flux-v1'||
     !(p.projectionFloor>0&&p.projectionFloor<1)||
     !Number.isSafeInteger(p.spacing)||p.spacing<1)
    fail('the original mode/stage/step/orientation/zero-root identity differs');
  if(!(radius>0)||!Number.isFinite(radius)||typeof options.integrationGrid!=='function')
    fail('supply the original cut radius and pinned original integrationGrid function');
  if(tail.graphs.length!==depth+1||tail.gains.length!==depth)
    fail('original graph/gain dimensions differ');
  tail.graphs.forEach((row,n)=>finiteVector(row,M,'original graph '+n));
  tail.gains.forEach((row,n)=>finiteVector(row,M,'original gain '+n));
  const sourceIdentity=sourceIdentityRecord(options.sourceIdentity);
  if(options.sourceIdentity.backendIdentity.tailJacobian!=='fourier-root-and-product-moments-v1')
    fail('the original Fourier-root/product Jacobian backend must be explicit');
  const before=liveSnapshot(tail),frozenHash=identityHash(before),
    farGraph=Float64Array.from(tail.graphs.at(-1)),
    farHash=sha(binary(Array.from(farGraph))),r4=radius**4;
  if(!(r4>0)||!Number.isFinite(r4))fail('nonfinite physical-height conversion');
  const actualRadius=tail.cells[0].profiles.at(-1)(1).r;
  if(!Object.is(actualRadius,radius))fail('cut radius differs from the original physical cut');
  const blocks=[],geometryHash=crypto.createHash('sha256');
  let substeps=0,geometryEvaluations=0,minAbsDeterminant=Infinity,maxAbsBlockEntry=0,
    zeroDeterminantCount=0,firstZeroDeterminant=null,minRelativeCancellation=Infinity;
  for(let n=0;n<depth;n++){
    const cell=tail.cells[n];
    if(!Array.isArray(cell.profiles)||!cell.profiles.length||
       !(cell.portRatio>0)||!Number.isFinite(cell.portRatio)||
       typeof cell.engine?.geometry!=='function')
      fail('incomplete live stage '+n);
    let values=Array.from({length:M},()=>[1,0,0,1]);
    for(let profileIndex=0;profileIndex<cell.profiles.length;profileIndex++){
      const profile=cell.profiles[profileIndex],cuts=profile.integrationBreakpoints??[];
      finiteVector(cuts,cuts.length,'actual cusp points');
      for(const x of cuts)if(!(x>=0&&x<=1))fail('actual cusp lies outside the stage');
      // Exact branch and arithmetic expressions used by the original
      // Fourier-product flowStateWithJacobian, including its no-cusp branch.
      const grid=cuts.length?options.integrationGrid(steps,cuts):null;
      if(grid)validGrid(grid,'original integrationGrid result');
      const count=grid?grid.length-1:steps,ordinaryH=1/steps;
      for(let k=0;k<count;k++){
        const h=grid?grid[k+1]-grid[k]:ordinaryH,
          x=grid?grid[k]:k*ordinaryH;
        const g0=cell.engine.geometry(profile,x),
          gm=cell.engine.geometry(profile,x+h/2),
          g1=cell.engine.geometry(profile,x+h);
        for(const [where,g] of [[x,g0],[x+h/2,gm],[x+h,g1]]){
          geometryHash.update(binary([n,profileIndex,where,cell.mu,
            g.r,g.w,g.w2,g.drdx]));
          geometryEvaluations++;
        }
        for(let j=0;j<M;j++){
          const frequency=p.spacing*(j+1);
          const a0=zeroBlockCoefficients(g0,cell.mu,frequency),
            am=zeroBlockCoefficients(gm,cell.mu,frequency),
            a1=zeroBlockCoefficients(g1,cell.mu,frequency),previous=values[j];
          try{values[j]=advanceBlock(previous,a0,am,a1,h);}
          catch(error){
            emit({kind:'RK-block-rejected',stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
              profileIndex,substep:k,x,h,mode:j+1,zero_based_mode_index:j,
              input_T_row_major:previous.map(observedNumber),
              A0:a0.map(observedNumber),Am:am.map(observedNumber),A1:a1.map(observedNumber),
              error:String(error)});
            throw error;
          }
          // The actual v1 failure's single mode is traced across its original
          // RK substeps. This is arithmetic already needed by this candidate;
          // no extra physical flow or J is evaluated.
          if(n===12&&j===92)emit({kind:'actual21-failed-block-RK-trace',stage:n,
            rawCell:cell.rawCell,rawSegment:cell.rawSegment,profileIndex,substep:k,x,h,
            block_before_port_conversion:blockObservation(values[j],n,j,p.spacing)});
        }
        substeps++;
      }
    }
    const row=new Float64Array(4*M),observations=[];
    // Retain ALL this stage's blocks and determinant arithmetic BEFORE
    // deciding whether any mode must fail. Port arithmetic is unchanged.
    for(let j=0;j<M;j++){
      const t=values[j];
      t[2]/=cell.portRatio;t[3]/=cell.portRatio;
      observations.push(blockObservation(t,n,j,p.spacing));
    }
    emit({kind:'stage-blocks',stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
      portRatio:cell.portRatio,mu:cell.mu,blocks:observations});
    for(let j=0;j<M;j++){
      const t=values[j],record=observations[j],det=t[0]*t[3]-t[1]*t[2];
      finiteVector(t,4,'port-converted stage block '+n+' mode '+j);
      if(!record.products_and_determinant_finite){
        emit({kind:'nonfinite-determinant-arithmetic-rejected',stage:n,mode:j+1,
          zero_based_mode_index:j,block:record});
        fail('nonfinite determinant arithmetic in stage block '+n+' mode '+j);
      }
      // No inverse of T is used below. Only u=a+b*gamma_next is divided by.
      // A finite rounded det==0 is recorded and does not veto an initial guess.
      if(det===0){
        zeroDeterminantCount++;
        if(firstZeroDeterminant===null)firstZeroDeterminant=record;
      }
      minAbsDeterminant=Math.min(minAbsDeterminant,Math.abs(det));
      minRelativeCancellation=Math.min(minRelativeCancellation,
        record.relative_cancellation_abs_det_over_abs_ad_plus_abs_bc);
      for(const v of t)maxAbsBlockEntry=Math.max(maxAbsBlockEntry,Math.abs(v));
      row.set(t,4*j);
    }
    blocks.push(row);
  }
  // Only PRIVATE candidate charts/gains are formed. Never assign tail.graphs
  // or tail.gains: those also define the original far BC and residual scales.
  const candidateGraphs=Array.from({length:depth+1},()=>new Float64Array(M)),
    transferDenominators=Array.from({length:depth},()=>new Float64Array(M));
  candidateGraphs[depth].set(farGraph);
  let minAbsChartDenominator=Infinity,maxAbsCandidateGraph=0;
  emit({kind:'original-far-graph',node:depth,graph:Array.from(farGraph)});
  for(let n=depth-1;n>=0;n--){
    for(let j=0;j<M;j++){
      const t=blocks[n],i=4*j,next=candidateGraphs[n+1][j],
        denominator=t[i]+t[i+1]*next,
        numerator=t[i+2]+t[i+3]*next;
      if(!Number.isFinite(denominator)||denominator===0||!Number.isFinite(numerator)){
        emit({kind:'candidate-chart-rejected',stage:n,mode:j+1,zero_based_mode_index:j,
          T_row_major:Array.from(t.slice(i,i+4)),next_graph:observedNumber(next),
          numerator:observedNumber(numerator),denominator:observedNumber(denominator),
          completed_mode_graphs:Array.from(candidateGraphs[n].slice(0,j)),
          completed_mode_denominators:Array.from(transferDenominators[n].slice(0,j))});
        fail('nonfinite or singular candidate Dirichlet chart '+n+' mode '+j);
      }
      const g=numerator/denominator;
      if(!Number.isFinite(g)){
        emit({kind:'candidate-graph-rejected',stage:n,mode:j+1,zero_based_mode_index:j,
          T_row_major:Array.from(t.slice(i,i+4)),next_graph:observedNumber(next),
          numerator:observedNumber(numerator),denominator:observedNumber(denominator),
          graph:observedNumber(g)});
        fail('nonfinite candidate graph '+n+' mode '+j);
      }
      candidateGraphs[n][j]=g;transferDenominators[n][j]=denominator;
      minAbsChartDenominator=Math.min(minAbsChartDenominator,Math.abs(denominator));
      maxAbsCandidateGraph=Math.max(maxAbsCandidateGraph,Math.abs(g));
    }
    emit({kind:'candidate-graph-row',node:n,graph:Array.from(candidateGraphs[n]),
      denominators:Array.from(transferDenominators[n])});
  }
  function assertUnchanged(){
    if(identityHash(liveSnapshot(tail))!==frozenHash)
      fail('the original parameters/stages/graphs/gains changed after construction');
  }
  assertUnchanged();
  const blockHash=crypto.createHash('sha256');
  for(const row of blocks)blockHash.update(binary(Array.from(row)));
  const identity={schema:SCHEMA,sourceSHA256:OWN_SHA,sourceIdentity,
    originalDNIdentitySHA256:frozenHash,originalFarGraphSHA256:farHash,
    zeroStageBlocksSHA256:blockHash.digest('hex'),
    stageGeometryAndGridSHA256:geometryHash.digest('hex'),
    modes:M,shapeDimension:K,stages:depth,nodes:depth+1,
    stepsPerOriginalStageProfile:steps,shootingParts:p.shootingParts,
    physicalDepth:p.physicalDepth,quadrature:p.quadrature,spacing:p.spacing,
    radius,substeps,geometryEvaluations,minAbsDeterminant,
    maxAbsBlockEntry,minAbsChartDenominator,maxAbsCandidateGraph,
    zeroDeterminantCount,firstZeroDeterminant,minRelativeCancellation,
    finiteRoundedZeroDeterminantIsNotAVeto:true,
    nonfiniteDeterminantArithmeticStillRejected:true,
    stageBlockInvertibilityOrLinearAccuracyClaimed:false,
    allOriginalNonfiniteAndZeroChartAndPredictionUnderflowFailuresRetained:true,
    sourceDerivedZeroLinearization:true,
    zeroStateHasNoCrossModeShapeJacobian:true,
    originalFullJacobianBitwiseEqualityClaimed:false,
    appliesAsFullJacobianAtNonzeroBase:false,
    originalGraphsGainsFarBoundaryScalesUnchanged:true,
    originalNonlinearEvaluateNewtonJacobianAuditUnchanged:true,
    candidateOnly:true,nonlinearSolveCalled:false,nonlinearTargetAccepted:false};
  return {
    identity,
    stageBlock(stage,modeIndex){
      if(!Number.isSafeInteger(stage)||stage<0||stage>=depth||
         !Number.isSafeInteger(modeIndex)||modeIndex<0||modeIndex>=M)
        fail('stageBlock index out of range');
      return Array.from(blocks[stage].slice(4*modeIndex,4*modeIndex+4));
    },
    predict(height){
      finiteVector(height,M,'complete unchanged physical H');
      assertUnchanged();
      const copied=Array.from(height),inputHash=sha(binary(copied)),
        target=Float64Array.from(copied,h=>h/r4),
        states=Array.from({length:depth+1},()=>Array(K).fill(0));
      finiteVector(target,M,'original target H/r^4');
      for(let j=0;j<M;j++){
        if(copied[j]!==0&&target[j]===0)fail('nonzero H underflowed in the original height conversion');
        states[0][j]=target[j];
      }
      for(let n=0;n<=depth;n++){
        for(let j=0;j<M;j++){
          const q=states[n][j],g=candidateGraphs[n][j],momentum=g*q;
          if(!Number.isFinite(momentum)||(g!==0&&q!==0&&momentum===0)){
            emit({kind:'prediction-momentum-rejected',node:n,mode:j+1,zero_based_mode_index:j,
              Q:observedNumber(q),graph:observedNumber(g),momentum:observedNumber(momentum),
              nonzero_underflow:g!==0&&q!==0&&momentum===0,
              completed_mode_state:states[n].slice(0,j).concat(states[n].slice(M,M+j))});
            fail('nonfinite or underflowed candidate momentum '+n+' mode '+j);
          }
          states[n][M+j]=momentum;
          if(n<depth){
            const next=q/transferDenominators[n][j];
            if(!Number.isFinite(next)||(q!==0&&next===0)){
              emit({kind:'prediction-height-rejected',source_node:n,target_node:n+1,
                mode:j+1,zero_based_mode_index:j,Q:observedNumber(q),
                denominator:observedNumber(transferDenominators[n][j]),
                next_Q:observedNumber(next),nonzero_underflow:q!==0&&next===0});
              fail('nonfinite or underflowed candidate height '+n+' mode '+j);
            }
            states[n+1][j]=next;
          }
        }
        emit({kind:'completed-prediction-node',node:n,state:Array.from(states[n]),
          negative_zero_columns:states[n].flatMap((v,j)=>Object.is(v,-0)?[j]:[])});
      }
      // Keep the original requested Dirichlet conversion exactly; no clipping,
      // H threshold, low-mode restriction, or zero-response cache is used.
      for(let j=0;j<M;j++)states[0][j]=copied[j]/r4;
      if(sha(binary(Array.from(height)))!==inputHash)fail('caller H changed during prediction');
      assertUnchanged();
      const statesHash=crypto.createHash('sha256');
      for(const row of states)statesHash.update(binary(row));
      return {states,diagnostics:{...identity,
        physicalHeightFloat64LESHA256:inputHash,
        candidateStatesFloat64LESHA256:statesHash.digest('hex'),
        allPhysicalHeightModesPreserved:true,nonzeroHeightThresholding:false,
        originalDirichletConversionPreserved:true,
        completeZeroResponseOrTangentCacheClaimed:false,
        originalNonlinearAcceptanceStillRequired:true}};
    }
  };
}

export {SCHEMA};

