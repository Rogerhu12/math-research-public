// Owned whole-evaluate transport for the already compiled literal LD kernel.
// No factory, profile, root, flow, or subprocess is invoked by importing this
// module. One fixed DN caches only state-independent Number coefficients.
// Inputs keep the original column units. Only returned pi rows are divided
// by each original portRatio; original residual/norm/solver remain in core.
import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {gzipSync} from 'node:zlib';
import os from 'node:os';

const digest=b=>createHash('sha256').update(b).digest('hex');
const ref=p=>({path:path.resolve(p),sha256:digest(fs.readFileSync(p))});
const assert=(ok,message)=>{if(!ok)throw Error(message);};
function exactFile(item){
  assert(item && typeof item.path==='string' && /^[a-f0-9]{64}$/.test(item.sha256),'Invalid file binding');
  assert(ref(item.path).sha256===item.sha256,'Bound file changed: '+item.path);
}
function scalarBytes(values){
  const b=Buffer.alloc(values.length*8);
  for(let j=0;j<values.length;j++)b.writeDoubleLE(values[j],8*j);
  return b;
}
function sameNumbers(a,b){return scalarBytes(a).equals(scalarBytes(b));}
function saveJSON(p,x){
  fs.writeFileSync(p,JSON.stringify(x,null,2)+'\n',{flag:'wx'});
  return ref(p);
}
function ensureFinite(values,label){
  for(const value of values)assert(Number.isFinite(value),'Nonfinite '+label);
}
function errorRecord(e){return {name:e?.name??'Error',message:String(e?.message??e)};}

export function readNativeManifest(){
  const p=process.env.VISIBLE_FLEX_NATIVE_MANIFEST,expected=process.env.VISIBLE_FLEX_NATIVE_MANIFEST_SHA256;
  assert(p && /^[a-f0-9]{64}$/.test(expected??''),'A frozen native manifest and its external SHA are required');
  const binding=ref(p);assert(binding.sha256===expected,'Native manifest changed');
  const manifest=JSON.parse(fs.readFileSync(p,'utf8'));
  assert(manifest.schema==='n4-native-batch-adapter-v1','Unsupported native adapter manifest');
  assert(os.endianness()==='LE' && process.arch==='x64' && process.platform==='linux','Only reviewed little-endian x86_64 Linux is supported');
  assert(path.resolve(process.env.VISIBLE_FLEX_SOURCE_ROOT??'')===path.join(manifest.source_topic,'repro/source-root'),'Owned source root mismatch');
  assert(path.resolve(process.env.CLOSING_TAIL_CACHE??'')===path.join(manifest.source_topic,'repro/source-root/topics/large-amplitude-twist-flex/scripts'),'Owned geometry cache root mismatch');
  assert(!process.env.LD_PRELOAD && !process.env.LD_LIBRARY_PATH,'Unreviewed dynamic-loader overrides');
  for(const item of manifest.owned_sources)exactFile(item);
  for(const item of Object.values(manifest.native_files))exactFile(item);
  for(const item of manifest.runtime_libraries)exactFile(item);
  return {manifest,binding};
}

// The two original paths are built separately. In this declared RK16 scope,
// their literal x/h sequences must agree; no midpoint or grid is rounded anew.
function originalGrids(profile,steps,cuspAwareFlow,gridAPI){
  const cuts=profile.integrationBreakpoints??[];
  const grid=cuts.length?gridAPI.integrationGrid(steps,cuts):null;
  const count=grid?grid.length-1:steps,ordinaryH=1/steps,variational=[];
  for(let n=0;n<count;n++){
    const h=grid?grid[n+1]-grid[n]:ordinaryH,x=grid?grid[n]:n*ordinaryH;
    variational.push({x,h});
  }
  const stateOnly=[];
  for(let k=0;k<steps;k++){
    const x=k/steps,h=1/steps;
    const split=cuspAwareFlow?gridAPI.splitIntegrationInterval(x,x+h,profile.integrationBreakpoints):[x,x+h];
    if(split.length===2)stateOnly.push({x,h});
    else for(let j=0;j<split.length-1;j++)stateOnly.push({x:split[j],h:split[j+1]-split[j]});
  }
  assert(stateOnly.length===variational.length,'Original scalar/variational cusp step counts differ');
  for(let j=0;j<stateOnly.length;j++)
    assert(sameNumbers([stateOnly[j].x,stateOnly[j].h],[variational[j].x,variational[j].h]),'Original scalar/variational cusp abscissas differ at step '+j);
  return variational;
}

function frozenPoint(cell,profile,x,M,spacing,orientation,sq2,sq12){
  // geometry is the actual already subdivided/reparametrized original profile.
  // Its drdx already has the stage-coordinate factor; do not multiply it again.
  const g=cell.engine.geometry(profile,x),r3=g.r**3,r4=g.r**4;
  const pNumerator=Array.from({length:M},(_,j)=>-((j+1)*spacing)*r3);
  const values=[r3,r4,sq2,sq12,g.E,g.w2,sq2*g.w,
    orientation*sq12*cell.mu/(sq2*r4*g.w2),g.drdx/g.r,
    orientation*sq2*r3*g.drdx*g.w2/(sq12*cell.mu),sq2*g.w,g.drdx*g.w,...pNumerator];
  ensureFinite(values,'static original coefficient');
  return values;
}

class BatchReader{
  constructor(buffer){this.buffer=buffer;this.offset=0;}
  take(n){assert(Number.isSafeInteger(n)&&n>=0&&this.offset+n<=this.buffer.length,'Truncated native batch output');const b=this.buffer.subarray(this.offset,this.offset+n);this.offset+=n;return b;}
  int(){return this.take(4).readInt32LE(0);}
  uint(){return this.take(4).readUInt32LE(0);}
  count(){const x=this.take(8).readBigUInt64LE(0);assert(x<=BigInt(Number.MAX_SAFE_INTEGER),'Native counter overflow');return Number(x);}
  scalar(){return this.take(8).readDoubleLE(0);}
  array(n){const b=this.take(8*n),out=new Float64Array(n);for(let j=0;j<n;j++)out[j]=b.readDoubleLE(8*j);return out;}
  end(){assert(this.offset===this.buffer.length,'Unexpected trailing native batch output bytes');}
}

export function createNativeBatchEvaluator(context,loaded,gridAPI){
  const {cells,M,spacing,quadrature:N,steps,projectionFloor,orientation,cuspAwareFlow,physicalParameters}=context;
  const {manifest,binding}=loaded,K=2*M,size=K+2,depth=cells.length;
  const scope={M,spacing,quadrature:N,steps,projectionFloor,orientation,cuspAwareFlow,stageCount:depth};
  for(const [key,value] of Object.entries(manifest.fixed_scope))
    assert(Object.is(scope[key],value),'Native adapter scope mismatch: '+key);
  assert(typeof gridAPI.integrationGrid==='function'&&typeof gridAPI.splitIntegrationInterval==='function','Original cusp functions required');
  const runDir=path.resolve(process.env.VISIBLE_FLEX_NATIVE_RUN_DIR??'');
  assert(process.env.VISIBLE_FLEX_NATIVE_RUN_DIR && !fs.existsSync(runDir),'Fresh native run directory required');
  fs.mkdirSync(runDir,{recursive:false});
  const eventsPath=path.join(runDir,'events.jsonl');
  const event=row=>fs.appendFileSync(eventsPath,JSON.stringify({time:new Date().toISOString(),...row})+'\n');
  event({event:'static_prepare_start',manifest:binding,scope});
  const staticStart=performance.now();
  let ga=N,gb=spacing;while(gb!==0){const t=ga%gb;ga=gb;gb=t;}
  const nq=N/ga,sq2=Math.sqrt(2),sq12=Math.sqrt(12),cosine=[],sine=[];
  for(let n=0;n<nq;n++){
    cosine.push(1);const theta=2*Math.PI*n/N;
    for(let j=0;j<M;j++)cosine.push(sq2*Math.cos(((j+1)*spacing)*theta));
    for(let j=0;j<M;j++)sine.push(sq2*Math.sin(((j+1)*spacing)*theta));
  }
  const stages=[];
  for(let n=0;n<depth;n++){
    const cell=cells[n];
    assert(cell.engine.M===M&&cell.engine.N===N&&cell.engine.size===size&&cell.engine.mu===cell.mu,'Original cell-engine dimensions/mu differ');
    assert(cell.engine.orientation===orientation&&cell.engine.quadratureIndependentNodes===nq,'Original periodic engine metadata differ');
    assert(cell.engine.rhsEvaluation==='split-linear-flux-v1','Cache must be built after split-engine replacement');
    assert(Number.isFinite(cell.portRatio)&&cell.portRatio>0,'Invalid original port ratio');
    const points=[],pointLookup=new Map(),stageSteps=[],profileGrids=[];
    function point(profileIndex,x){
      const key=profileIndex+':'+scalarBytes([x]).toString('hex');
      if(pointLookup.has(key))return pointLookup.get(key);
      const values=frozenPoint(cell,cell.profiles[profileIndex],x,M,spacing,orientation,sq2,sq12);
      const index=points.length;points.push({profile:profileIndex,x,values});pointLookup.set(key,index);return index;
    }
    for(let profile=0;profile<cell.profiles.length;profile++){
      const grid=originalGrids(cell.profiles[profile],steps,cuspAwareFlow,gridAPI);profileGrids.push(grid);
      for(let step=0;step<grid.length;step++){
        const {x,h}=grid[step];
        stageSteps.push({profile,step,point_a:point(profile,x),point_mid:point(profile,x+h/2),point_end:point(profile,x+h),x,h});
      }
    }
    const coefficientValues=points.flatMap(p=>p.values),coefficients=scalarBytes(coefficientValues);
    const gridBytes=Buffer.alloc(stageSteps.length*36);
    stageSteps.forEach((p,j)=>{
      const base=36*j;
      [p.profile,p.step,p.point_a,p.point_mid,p.point_end].forEach((v,k)=>gridBytes.writeInt32LE(v,base+4*k));
      gridBytes.writeDoubleLE(p.x,base+20);gridBytes.writeDoubleLE(p.h,base+28);
    });
    stages.push({stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,rawLeft:cell.rawLeft,rawRight:cell.rawRight,
      mu:cell.mu,portRatio:cell.portRatio,profileGrids,points,steps:stageSteps,coefficients,gridBytes,
      nsteps:stageSteps.length,npoints:points.length,initialOffset:null,blockOffset:null,blockLength:null});
  }
  const headerBytes=140+20*8+cosine.length*8+sine.length*8;
  const totalBytes=headerBytes+stages.reduce((v,s)=>v+8+size*8+s.coefficients.length+s.gridBytes.length,0);
  const template=Buffer.alloc(totalBytes);let offset=0;
  function integer(v){template.writeInt32LE(v,offset);offset+=4;}
  function number(v){template.writeDoubleLE(v,offset);offset+=8;}
  template.write('VFN4LD01',offset,'ascii');offset+=8;
  [1,M,N,spacing,nq,30,20,depth,0].forEach(integer);
  const tokenOffset=offset;assert(tokenOffset===44,'ABI token offset changed');template.fill(48,offset,offset+64);offset+=64;
  [projectionFloor,8e-14,5e-12,1e-300].forEach(number);
  Array.from({length:20},(_,j)=>2**(-j)).forEach(number);cosine.forEach(number);sine.forEach(number);
  assert(offset===headerBytes,'Static header size mismatch');
  for(const s of stages){
    s.blockOffset=offset;integer(s.nsteps);integer(s.npoints);s.initialOffset=offset;offset+=size*8;
    s.coefficients.copy(template,offset);offset+=s.coefficients.length;
    s.gridBytes.copy(template,offset);offset+=s.gridBytes.length;s.blockLength=offset-s.blockOffset;
  }
  assert(offset===totalBytes,'Static wire size mismatch');
  const templatePath=path.join(runDir,'static-template.bin');fs.writeFileSync(templatePath,template,{flag:'wx'});
  const counts={stageCount:depth,totalSteps:stages.reduce((v,s)=>v+s.nsteps,0),
    totalUniquePoints:stages.reduce((v,s)=>v+s.npoints,0),stagesWithExtraCuspSteps:stages.filter(s=>s.nsteps!==steps*cells[s.stage].profiles.length).length,
    headerBytes,inputBytes:totalBytes,stateOnlyOutputBytes:88+depth*(8+size*8+64),
    fullJacOutputBytes:88+depth*(8+size*8+size*K*8+64)};
  const staticData={scope,independentQuadratureNodes:nq,manifest:binding,physicalParameters,
    cosine_sha256:digest(scalarBytes(cosine)),sine_sha256:digest(scalarBytes(sine)),template:ref(templatePath),counts,
    stages:stages.map(s=>({stage:s.stage,rawCell:s.rawCell,rawSegment:s.rawSegment,rawLeft:s.rawLeft,rawRight:s.rawRight,
      mu:s.mu,portRatio:s.portRatio,profileGrids:s.profileGrids,
      points:s.points.map(p=>({profile:p.profile,x:p.x})),nsteps:s.nsteps,npoints:s.npoints,
      coefficients_sha256:digest(s.coefficients),grid_sha256:digest(s.gridBytes),
      initialOffset:s.initialOffset,blockOffset:s.blockOffset,blockLength:s.blockLength})),
    original_scalar_and_variational_grid_bytes_equal:true,
    source_cache_scope:'One fixed DN only, after split replacement. Actual Number geometry/trig/grid; no state/root/RHS cache.',
    input_units:'Original states[n+1], no portRatio multiplication; two appended means start at zero.',
    output_units:'Only pi output/J rows divided by original c.portRatio. No input-column scaling.',
    runtime:{node:ref(process.execPath),versions:process.versions,execArgv:process.execArgv,platform:process.platform,arch:process.arch},
    staticPreparationSeconds:(performance.now()-staticStart)/1000};
  const staticPath=path.join(runDir,'static-metadata.json.gz');
  fs.writeFileSync(staticPath,gzipSync(JSON.stringify(staticData)+'\n'),{flag:'wx'});
  const staticRef=ref(staticPath);event({event:'static_prepare_complete',metadata:staticRef,counts,seconds:staticData.staticPreparationSeconds});
  let calls=0;
  function prepare(states,withJac){
    assert(typeof withJac==='boolean','Explicit withJac flag required');
    assert(states.length===depth+1&&states.every(row=>row.length===K),'Original finite-state dimensions required');
    const input=Buffer.from(template);
    input.writeInt32LE(withJac?1:0,40);
    for(let n=0;n<depth;n++){
      ensureFinite(states[n+1],'original input state');
      for(let j=0;j<K;j++)input.writeDoubleLE(states[n+1][j],stages[n].initialOffset+8*j);
      // The template's two mean zeros are never replaced by another stage.
    }
    const token=createHash('sha256').update(input.subarray(0,44)).update(input.subarray(108)).digest('hex');
    input.write(token,44,'ascii');
    return {input,token,withJac,owner:template};
  }
  function inspectStage(prepared,n){
    assert(prepared.owner===template&&Number.isInteger(n)&&n>=0&&n<depth,'Foreign prepared batch/stage');
    const s=stages[n];return {stage:n,mu:s.mu,portRatio:s.portRatio,profileGrids:s.profileGrids,
      points:s.points.map(p=>({profile:p.profile,x:p.x,values:p.values.slice()})),
      stepBytes:Buffer.from(s.gridBytes),coefficientBytes:Buffer.from(s.coefficients),
      initialBytes:Buffer.from(prepared.input.subarray(s.initialOffset,s.initialOffset+size*8)),
      cosineBytes:scalarBytes(cosine),sineBytes:scalarBytes(sine),
      blockBytes:Buffer.from(prepared.input.subarray(s.blockOffset,s.blockOffset+s.blockLength))};
  }
  function evaluate(states,withJac){
    const prepared=prepare(states,withJac);return execute(prepared);
  }
  function execute(prepared){
    assert(prepared.owner===template,'A foreign/mutated static batch is not accepted');
    const currentToken=createHash('sha256').update(prepared.input.subarray(0,44)).update(prepared.input.subarray(108)).digest('hex');
    assert(currentToken===prepared.token&&prepared.input.subarray(44,108).toString('ascii')===prepared.token,'Prepared input token changed');
    exactFile(manifest.native_files.executable);
    for(const item of manifest.runtime_libraries)exactFile(item);
    calls++;const label=String(calls).padStart(4,'0')+'-'+(prepared.withJac?'jac':'state');
    const prefix=path.join(runDir,label),inputPath=prefix+'-input.bin',outputPath=prefix+'-output.bin';
    fs.writeFileSync(inputPath,prepared.input,{flag:'wx'});
    const start=performance.now();event({event:'batch_start',call:calls,withJac:prepared.withJac,input:ref(inputPath),token:prepared.token});
    const child=spawnSync(manifest.native_files.executable.path,[inputPath,outputPath],
      {encoding:null,maxBuffer:16*1024*1024});
    const processSeconds=(performance.now()-start)/1000;
    const stdoutPath=prefix+'-stdout.txt',stderrPath=prefix+'-stderr.txt';
    fs.writeFileSync(stdoutPath,child.stdout??Buffer.alloc(0),{flag:'wx'});
    fs.writeFileSync(stderrPath,child.stderr??Buffer.alloc(0),{flag:'wx'});
    const outcome={call:calls,withJac:prepared.withJac,command:[manifest.native_files.executable.path,inputPath,outputPath],
      manifest:binding,static_metadata:staticRef,input:ref(inputPath),output:fs.existsSync(outputPath)?ref(outputPath):null,
      stdout:ref(stdoutPath),stderr:ref(stderrPath),returncode:child.status,signal:child.signal??null,
      spawn_error:child.error?errorRecord(child.error):null,process_wall_seconds:processSeconds,
      payload_token:prepared.token,token_scope:'Payload only; source/binary/runtime bindings checked independently.',
      full_output_preserved:true,original_equations_or_gates_changed:false};
    let parsed=null,failure=null;
    try{
      assert(!child.error&&child.signal===null,'Native process engineering interruption');
      assert(child.status===0||child.status===3,'Native protocol/engineering exit '+child.status);
      assert(outcome.output!==null,'No native output');
      const raw=fs.readFileSync(outputPath),r=new BatchReader(raw);
      assert(r.take(8).toString('ascii')==='VFN4OUT1','Native output magic mismatch');
      assert(r.int()===1&&r.int()===M&&r.int()===depth&&r.int()===(prepared.withJac?1:0),'Native output dimensions differ');
      assert(r.take(64).toString('ascii')===prepared.token,'Native output token differs');
      const flows=[],diagnostics=[];let kernelSeconds=0;
      for(let n=0;n<depth;n++){
        assert(r.int()===n,'Native stage order differs');const status=r.int();
        if(status!==0){
          assert(child.status===3,'Nonzero stage status without native failure exit');
          const message=r.take(r.uint()).toString('utf8');r.end();
          const e=Error('Native stage '+n+': '+message);e.name='NativeStageFailure';
          outcome.failed_stage=n;outcome.native_stage_message=message;
          outcome.successful_stages_before_failure=n;
          throw e;
        }
        const state=r.array(size),tangent=prepared.withJac?r.array(size*K):null;
        ensureFinite(state,'native boundary state');if(tangent)ensureFinite(tangent,'native boundary tangent');
        const d={stage:n,root_calls:r.count(),root_updates:r.count(),root_fallbacks:r.count(),
          minA:r.scalar(),minD:r.scalar(),max_root_relative_residual:r.scalar(),
          min_literal_Jacobian_pivot:r.scalar(),kernel_seconds:r.scalar()};
        ensureFinite([d.minA,d.minD,d.max_root_relative_residual,d.kernel_seconds],'native root diagnostics');
        if(prepared.withJac)assert(Number.isFinite(d.min_literal_Jacobian_pivot)&&d.min_literal_Jacobian_pivot>0,'Invalid native literal-Jacobian pivot');
        assert(d.root_calls===4*stages[n].nsteps,'Native root call count differs from actual cusp grid');
        const ratio=cells[n].portRatio,out=Float64Array.from(state.slice(0,K),(v,j)=>j<M?v:v/ratio);
        let J=null;if(prepared.withJac){
          J=new Float64Array(K*K);
          for(let i=0;i<K;i++)for(let j=0;j<K;j++)J[i*K+j]=tangent[i*K+j]/(i<M?1:ratio);
        }
        flows.push({out,J,meanHeight:state[K]+state[K+1],minA:d.minA,minD:d.minD});
        diagnostics.push(d);kernelSeconds+=d.kernel_seconds;
      }
      r.end();assert(child.status===0,'Native successful rows with nonzero process exit');
      outcome.diagnostics=diagnostics;outcome.kernel_seconds_sum=kernelSeconds;
      outcome.status='complete';outcome.returned_flow_count=flows.length;parsed=flows;
    }catch(e){
      failure=e;outcome.status=e.name==='NativeStageFailure'?'native_stage_failure':'engineering_failure';
      outcome.failure=errorRecord(e);
    }
    outcome.decode_and_validation_seconds=(performance.now()-start)/1000-processSeconds;
    const record=saveJSON(prefix+'-record.json',outcome);
    event({event:'batch_terminal',call:calls,status:outcome.status,record,
      returncode:child.status,signal:child.signal??null,processSeconds});
    // The original core retains its original trial catch/line-search logic.
    // Any process/protocol failure is separately recorded as engineering;
    // it must not later be described as an observed mathematical obstruction.
    if(failure)throw failure;
    return parsed;
  }
  return {evaluate,prepare,execute,inspectStage,staticMetadata:staticData,staticMetadataRef:staticRef,
    runDirectory:runDir,manifest:binding,get callCount(){return calls;}};
}
