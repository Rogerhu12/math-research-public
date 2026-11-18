// Read-only reference/coefficients for three prescribed finite stage flows.
// "serve" exposes the original V8 scalar functions to a float port; it has no
// filesystem mutation or mathematical state. "export" adds trace callbacks to
// an owned copy of the original point-root source. Production sources stay intact.
import fs from 'node:fs';
import path from 'node:path';
import readline from 'node:readline';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {gunzipSync,gzipSync} from 'node:zlib';

const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const digest=b=>createHash('sha256').update(b).digest('hex');
function bytes(a){const b=Buffer.alloc(a.length*8);a.forEach((v,j)=>b.writeDoubleLE(v,8*j));return b;}
const numberHash=a=>digest(bytes(a));
const load=p=>JSON.parse(p.endsWith('.gz')?gunzipSync(fs.readFileSync(p)):fs.readFileSync(p,'utf8'));
function save(file,data){fs.writeFileSync(file,gzipSync(JSON.stringify(data)+'\n'));return {path:path.resolve(file),sha256:sha(file)};}

if(process.argv[2]==='serve'){
  const rl=readline.createInterface({input:process.stdin,crlfDelay:Infinity});
  for await(const line of rl){
    const request=JSON.parse(line);let out;
    if(request.operation==='root_rows'){
      out={sqrtD:request.D.map(v=>Math.sqrt(v)),
        bmNonlinear:request.needJac?request.u.map(v=>Math.expm1(-1.5*Math.log1p(-v))):null};
    }else if(request.operation==='sqrt')out={value:Math.sqrt(request.value)};
    else throw Error('Unrecognized arithmetic operation');
    process.stdout.write(JSON.stringify(out)+'\n');
  }
}else{
  const [mode,fixtureArg,oldOutputArg,prefixArg]=process.argv.slice(2);
  if(mode!=='export'||!prefixArg)throw Error('export FIXTURE OLD_ORIGINAL_OUTPUT NEW_PREFIX, or serve');
  const fixturePath=path.resolve(fixtureArg),oldOutputPath=path.resolve(oldOutputArg),prefix=path.resolve(prefixArg);
  const frozen=load(fixturePath),old=load(oldOutputPath),cfg=frozen.config;
  if(frozen.named_stages.join(',')!=='43,38,175'||cfg.modes!==20||cfg.spacing!==4||
      cfg.shootingParts!==32||cfg.steps!==16||cfg.solveTolerance!==2e-9)
    throw Error('Only the declared original three n4 fixtures are supported');
  if(old.input_sha256!==frozen.input_sha256||JSON.stringify(old.config)!==JSON.stringify(cfg))
    throw Error('The original flow and frozen fixture identities differ');
  for(const group of [frozen.source_sha256,frozen.additional_current_root_source_sha256])
    for(const [name,value] of Object.entries(group))if(sha(name)!==value)
      throw Error('An original source changed: '+name);
  if(sha(frozen.input)!==frozen.input_sha256)throw Error('The original failed state changed');
  const source=Object.keys(frozen.source_sha256).find(p=>p.endsWith('/periodic-quadrature/general_root_tail_momentum.mjs'));
  if(!source)throw Error('No bound original periodic momentum root');
  const split=path.join(path.dirname(source),'f6tail_momentum_split_flux.mjs');
  const topic=path.resolve(path.dirname(source),'../..');
  process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
  process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
  const files={root:prefix+'-traced-root.mjs',split:prefix+'-traced-split.mjs',
    coefficients:prefix+'-coefficients.json.gz',reference:prefix+'-reference.json.gz',summary:prefix+'-summary.json'};
  for(const p of Object.values(files))if(fs.existsSync(p))throw Error('Frozen output exists: '+p);
  fs.mkdirSync(path.dirname(prefix),{recursive:true});
  let traced=fs.readFileSync(source,'utf8');
  const patches=[];
  function once(from,to,label){
    const hits=traced.split(from).length-1;if(hits!==1)throw Error('Expected exactly one original operand block: '+label);
    traced=traced.replace(from,to);patches.push({label,original:from,replacement:to});
  }
  once('export function createMomentumTailEngine(options={}) {',
    'export function createMomentumTailEngine(options={}) {\n const __emit=(event,payload)=>options.frozenProbeTrace?.({event,...payload});', 'trace callback only');
  once(' function evaluateL(L,Q,g,needJac=true){',
    ' function evaluateL(L,Q,g,needJac=true){\n  __emit("evaluate_start",{L:Array.from(L),Q:Array.from(Q),needJac});','evaluation operands');
  once('   if(!(D>floor&&S>floor&&A>floor))throw new Error("momentum branch D/S/A rejected");',
    '   __emit("domain",{n,D,S,A,floor,D_pass:D>floor,S_compared:D>floor,S_pass:D>floor?S>floor:null,A_compared:D>floor&&S>floor,A_pass:D>floor&&S>floor?A>floor:null});\n   if(!(D>floor&&S>floor&&A>floor))throw new Error("momentum branch D/S/A rejected");','original left-to-right domain judgment');
  once('  return {moments:Float64Array.from(L,(v,j)=>v+quad[j]),quad,B,rows,minD,minS,minA,maxQuad};',
    '  __emit("evaluate_end",{moments:Array.from(L,(v,j)=>v+quad[j]),minD,minS,minA,maxQuad});\n  return {moments:Float64Array.from(L,(v,j)=>v+quad[j]),quad,B,rows,minD,minS,minA,maxQuad};','root moments');
  once('   if(i===j){if(!(v>0))throw new Error("momentum Newton matrix not SPD");L[i*J+j]=Math.sqrt(v);}',
    '   if(i===j){__emit("spd_positive",{i,value:v,positive:v>0});if(!(v>0))throw new Error("momentum Newton matrix not SPD");L[i*J+j]=Math.sqrt(v);}','original SPD judgment');
  once('  let L=guess?Float64Array.from(guess):Float64Array.from(target);\n  let last;',
    '  let L=guess?Float64Array.from(guess):Float64Array.from(target);\n  __emit("root_start",{state:Array.from(state),x,target:Array.from(target),L:Array.from(L)});\n  let last;','original target and root initial value');
  once('   if(err<=8e-14*scale)return last;',
    '   __emit("root_stop",{iteration:it,err,scale,tolerance:8e-14,threshold:8e-14*scale,accepted:err<=8e-14*scale});\n   if(err<=8e-14*scale){__emit("root_return",{iteration:it,err,scale,roundoffFallback:false});return last;}','original stopping operands');
  once('    const fac=2**(-k),trial=Float64Array.from(L,(v,j)=>v-fac*step[j]);',
    '    const fac=2**(-k),trial=Float64Array.from(L,(v,j)=>v-fac*step[j]);\n    __emit("trial_start",{k,fac,trial:Array.from(trial)});','original halving operands');
  once('     if(er<err||er<=8e-14*scale){L=trial;accepted=true;break;}}',
    '     __emit("trial_judgment",{k,er,err,scale,threshold:8e-14*scale,improves:er<err,tolerance_compared:!(er<err),within_tolerance:er<err?null:er<=8e-14*scale,accepted:er<err||er<=8e-14*scale});\n     if(er<err||er<=8e-14*scale){L=trial;accepted=true;break;}}','original halving judgment');
  once('    catch(_){}\n   }\n   if(!accepted){if(err<=5e-12*scale)return {...last,roundoffFallback:true};throw new Error("momentum Newton line search failed");}',
    '    catch(__error){__emit("trial_caught",{k,message:String(__error.message)});}\n   }\n   if(!accepted){__emit("fallback_judgment",{err,scale,tolerance:5e-12,threshold:5e-12*scale,accepted:err<=5e-12*scale});if(err<=5e-12*scale){__emit("root_return",{iteration:it,err,scale,roundoffFallback:true});return {...last,roundoffFallback:true};}throw new Error("momentum Newton line search failed");}','original fallback operands');
  fs.writeFileSync(files.root,traced);
  const splitOriginal=fs.readFileSync(split,'utf8');
  if(splitOriginal.split("'./general_root_tail_momentum.mjs'").length!==2)throw Error('Original split import differs');
  fs.writeFileSync(files.split,splitOriginal.replace("'./general_root_tail_momentum.mjs'",JSON.stringify('./'+path.basename(files.root))));
  const {createSplitFluxMomentumTailEngine}=await import(pathToFileURL(files.split));
  const sq2=Math.sqrt(2),sq12=Math.sqrt(12),M=cfg.modes,size=2*M+2;
  const freq=Array.from({length:M},(_,j)=>(j+1)*cfg.spacing),coefficientRows=[],referenceRows=[];
  const started=performance.now();
  for(const fixture of frozen.fixtures){
    const events=[],engine=createSplitFluxMomentumTailEngine({...cfg,mu:fixture.mu,frozenProbeTrace:e=>events.push(e)});
    const geometryByProfile=new Map();
    for(const row of fixture.geometry){
      if(!geometryByProfile.has(row.profile))geometryByProfile.set(row.profile,new Map());
      const table=geometryByProfile.get(row.profile),key=bytes([row.x]).toString('hex');
      if(table.has(key)&&JSON.stringify(table.get(key))!==JSON.stringify(row.values))throw Error('Inconsistent duplicate frozen geometry');
      table.set(key,row.values);
    }
    const profiles=Array.from({length:fixture.grid.length},(_,i)=>x=>{
      const value=geometryByProfile.get(i).get(bytes([x]).toString('hex'));
      if(!value)throw Error('A reference root requested unfrozen geometry');
      return {...value};
    });
    const coefficientPoints=fixture.geometry.map(row=>{
      const g=engine.geometry(profiles[row.profile],row.x);
      for(const name of Object.keys(row.values))if(!Object.is(g[name],row.values[name]))
        throw Error('Original geometry arithmetic no longer reproduces fixture: '+name);
      const r3=g.r**3,r4=g.r**4;
      return {profile:row.profile,x:row.x,geometry:g,
        coefficients:{r3,r4,sqrt2:sq2,sqrt12:sq12,E:g.E,w2:g.w2,
          pNumerator:freq.map(m=>-m*r3),pDenominator:sq2*g.w,
          targetFactor:cfg.orientation*sq12*fixture.mu/(sq2*r4*g.w2),
          sigma:g.drdx/g.r,
          fluxPrefactor:cfg.orientation*sq2*r3*g.drdx*g.w2/(sq12*fixture.mu),
          qLNumerator:sq2*g.w,meanFactor:g.drdx*g.w}};
    });
    let state=Float64Array.from(fixture.initial42),minA=Infinity,minD=Infinity;
    const increment=(v,f,h)=>Float64Array.from(v,(x,j)=>x+h*f[j]);
    function field(v,profile,step,label,x){
      events.push({event:'rk_field',profile,step,label,x});
      const rt=engine.root(v,profiles[profile],x),f=Float64Array.from(engine.rhs(v,profiles[profile],x,false,rt));
      minA=Math.min(minA,rt.e.minA);minD=Math.min(minD,rt.e.minD);return f;
    }
    for(let i=0;i<fixture.grid.length;i++)for(let k=0;k<fixture.grid[i].length;k++){
      const {x,h}=fixture.grid[i][k],a=field(state,i,k,'a',x),
        b=field(increment(state,a,h/2),i,k,'b',x+h/2),
        c=field(increment(state,b,h/2),i,k,'c',x+h/2),
        d=field(increment(state,c,h),i,k,'d',x+h);
      for(let j=0;j<size;j++)state[j]+=h*(a[j]+2*b[j]+2*c[j]+d[j])/6;
    }
    const prior=old.rows.find(row=>row.stage===fixture.stage);
    if(!prior||!bytes(state).equals(bytes(prior.reference42)))throw Error('Traced original state flow differs from all42 original full-Jacobian output');
    const rows={...fixture,points:coefficientPoints};delete rows.geometry;
    coefficientRows.push(rows);
    referenceRows.push({stage:fixture.stage,state:Array.from(state),state42_sha256:numberHash(Array.from(state)),
      minA,minD,events,root_calls:events.filter(e=>e.event==='root_return').length});
    console.log(JSON.stringify({event:'traced_original_stage_complete',stage:fixture.stage,all42_bitwise_identical:true,
      root_calls:referenceRows.at(-1).root_calls,trace_events:events.length}));
  }
  const context={fixture:{path:fixturePath,sha256:sha(fixturePath)},original_output:{path:oldOutputPath,sha256:sha(oldOutputPath)},
    input:{path:frozen.input,sha256:frozen.input_sha256},source_sha256:{...frozen.source_sha256,[path.resolve(process.argv[1])]:sha(process.argv[1])},
    additional_original_root_sources:frozen.additional_current_root_source_sha256,
    traced_source:{root:{path:files.root,sha256:sha(files.root)},split:{path:files.split,sha256:sha(files.split)}},
    scope:'Three-stage read-only reference. Original point-root source is copied with callbacks only. Static original Number coefficient subexpressions are frozen; no high-precision run or whole-tail evaluation is performed.',
    modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,independent_quadrature_nodes:frozen.independent_quadrature_nodes,
    steps:cfg.steps,original_tail_gate:cfg.solveTolerance,command:process.argv,
    root_rules:{floor:cfg.projectionFloor??.1,iterations:30,tolerance:8e-14,scale_floor:1e-300,
      halving_factors:Array.from({length:20},(_,j)=>2**(-j)),fallback_tolerance:5e-12,
      domain_sequence:'D > floor && S > floor && A > floor; left-to-right short-circuit',
      stopping:'err <= tolerance * scale',trial:'er < err || er <= tolerance * old_scale; short-circuit',
      fallback:'Only after no trial accepted: err <= fallback_tolerance * scale',
      scale:'max(scale_floor, e.maxQuad, abs of all target components)',
      initialization:'L = target; no supplied guess',spd:'Sequential lower-triangular Cholesky, each diagonal v > 0'},
    patch_identity:digest(JSON.stringify(patches))};
  const coefficients=save(files.coefficients,{...context,trig:frozen.trig,fixtures:coefficientRows,trace_source_patches:patches});
  const reference=save(files.reference,{...context,rows:referenceRows});
  const summary={...context,coefficients,reference,named_results:referenceRows.map(r=>({stage:r.stage,
    original_all42_bitwise_identical:true,state42_sha256:r.state42_sha256,root_calls:r.root_calls,
    trace_events:r.events.length,minA:r.minA,minD:r.minD})),seconds:(performance.now()-started)/1000};
  fs.writeFileSync(files.summary,JSON.stringify(summary,null,2)+'\n');
  console.log(JSON.stringify({event:'terminal',summary:files.summary,sha256:sha(files.summary)}));
}
