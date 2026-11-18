// Independent n3/M8 frozen-arithmetic baseline at the complete over-gate rows.
// Original source and state are read-only. The existing full-row outputs are
// reused for all16 physical outputs; only the missing original root/RK trace is
// evaluated here. No DN/Newton/prefix solve or new initial candidate is invoked.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {gunzipSync,gzipSync} from 'node:zlib';

const [topicArg,inputArg,rowsArg,prefixArg]=process.argv.slice(2);
if(!prefixArg)throw Error('SOURCE_TOPIC FAILURE COMPLETE_ROWS FRESH_PREFIX required');
const topic=path.resolve(topicArg),input=path.resolve(inputArg),rowsPath=path.resolve(rowsArg),prefix=path.resolve(prefixArg);
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const hash=b=>createHash('sha256').update(b).digest('hex');
const load=p=>JSON.parse(p.endsWith('.gz')?gunzipSync(fs.readFileSync(p)):fs.readFileSync(p,'utf8'));
function bytes(a){const b=Buffer.alloc(a.length*8);a.forEach((v,j)=>b.writeDoubleLE(v,8*j));return b;}
const ref=p=>({path:path.resolve(p),sha256:sha(p)});
function save(p,data){fs.writeFileSync(p,gzipSync(JSON.stringify(data)+'\n'),{flag:'wx'});return ref(p);}
const failed=load(input),old=load(rowsPath),cfg=failed.config,cp=failed.response.checkpoint;
if(sha(input)!=='753aa9ec4584f0bafa216acbfaffe98fab44a0369e914ca06c7c739d81b365c4'||
 old.input.sha256!==sha(input)||!failed.response.failed||old.statesChanged!==false||
 cfg.modes!==8||cfg.spacing!==3||cfg.quadrature!==128||cfg.steps!==16||cfg.shootingParts!==16||
 cfg.solveTolerance!==2e-9||(cfg.projectionFloor??.1)!==.1)
 throw Error('Only this actual n3/M8 near-converged failure and its full saved rows are supported');
const names=[...new Set(old.completeOverGateComponents.map(r=>r.stage))].sort((a,b)=>a-b);
if(names.join(',')!=='86,87,88')throw Error('The complete named failure rows changed');
const sources={...old.source_sha256,[path.resolve(process.argv[1])]:sha(process.argv[1])};
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Source changed: '+file);
const sourceRoot=path.join(topic,'repro/source-root'),cache=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;process.env.CLOSING_TAIL_CACHE=cache;
const source=path.join(cache,'general_root_tail_momentum.mjs'),split=path.join(cache,'f6tail_momentum_split_flux.mjs');
const files={root:prefix+'-traced-root.mjs',split:prefix+'-traced-split.mjs',coefficients:prefix+'-coefficients.json.gz',reference:prefix+'-reference.json.gz',summary:prefix+'-summary.json'};
for(const p of Object.values(files))if(fs.existsSync(p))throw Error('Use fresh output: '+p);
fs.mkdirSync(path.dirname(prefix),{recursive:true});
const originalRoot=fs.readFileSync(source,'utf8');let traced=originalRoot;const patches=[];
function once(from,to,label){if(traced.split(from).length!==2)throw Error('Original root block differs: '+label);traced=traced.replace(from,to);patches.push({label,original:from,replacement:to});}
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

let restored=traced;
for(const p of [...patches].reverse()){if(restored.split(p.replacement).length!==2)throw Error('Trace patch not reversible');restored=restored.replace(p.replacement,p.original);}
if(restored!==originalRoot)throw Error('Unexpected arithmetic change in traced original root');
const rootImport='"./general_exact_tail_cauchy_raw.mjs"';
if(traced.split(rootImport).length!==2)throw Error('Original raw diagnostic import differs');
traced=traced.replace(rootImport,JSON.stringify(pathToFileURL(path.join(cache,'general_exact_tail_cauchy_raw.mjs')).href));
fs.writeFileSync(files.root,traced,{flag:'wx'});
const originalSplit=fs.readFileSync(split,'utf8');
if(originalSplit.split("'./general_root_tail_momentum.mjs'").length!==2)throw Error('Original split import differs');
fs.writeFileSync(files.split,originalSplit.replace("'./general_root_tail_momentum.mjs'",JSON.stringify(pathToFileURL(files.root).href)),{flag:'wx'});
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const {createSplitFluxMomentumTailEngine}=await import(pathToFileURL(files.split));
const gridAPI=await import(pathToFileURL(path.join(cache,'f6tail_cusp_grid.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,size=K+2,sq2=Math.sqrt(2),sq12=Math.sqrt(12),freq=Array.from({length:M},(_,j)=>(j+1)*cfg.spacing);
if(dn.tail.cells.length!==1152||cp.states.length!==1153)throw Error('Original finite grid differs');
const state_cos=Array.from({length:cfg.quadrature},(_,n)=>{const theta=2*Math.PI*n/cfg.quadrature;return [1,...freq.map(m=>sq2*Math.cos(m*theta))];});
const state_sin=Array.from({length:cfg.quadrature},(_,n)=>{const theta=2*Math.PI*n/cfg.quadrature;return freq.map(m=>sq2*Math.sin(m*theta));});
function originalGrid(profile){
 const cuts=profile.integrationBreakpoints??[],g=cuts.length?gridAPI.integrationGrid(cfg.steps,cuts):null;
 const n=g?g.length-1:cfg.steps,h0=1/cfg.steps,variational=[];
 for(let i=0;i<n;i++)variational.push({x:g?g[i]:i*h0,h:g?g[i+1]-g[i]:h0});
 const scalar=[];
 for(let i=0;i<cfg.steps;i++){const x=i/cfg.steps,h=1/cfg.steps,s=gridAPI.splitIntegrationInterval(x,x+h,profile.integrationBreakpoints);
  if(s.length===2)scalar.push({x,h});else for(let j=0;j<s.length-1;j++)scalar.push({x:s[j],h:s[j+1]-s[j]});}
 if(scalar.length!==variational.length||scalar.some((s,i)=>!bytes([s.x,s.h]).equals(bytes([variational[i].x,variational[i].h]))))throw Error('Literal scalar/variational grids differ');
 return variational;
}
const fixtures=[],referenceRows=[],began=performance.now();
for(const stage of names){
 const cell=dn.tail.cells[stage],row=old.fullAffectedAndUpstreamRows.find(r=>r.stage===stage);
 if(!row||row.components.length!==K)throw Error('Saved complete physical row missing');
 const events=[],engine=createSplitFluxMomentumTailEngine({...cfg,mu:cell.mu,frozenProbeTrace:e=>events.push(e)});
 const grid=cell.profiles.map(originalGrid),points=[];
 for(let profile=0;profile<grid.length;profile++)for(const {x,h} of grid[profile])for(const xx of [x,x+h/2,x+h]){
  const g=engine.geometry(cell.profiles[profile],xx),r3=g.r**3,r4=g.r**4;
  points.push({profile,x:xx,geometry:g,coefficients:{r3,r4,sqrt2:sq2,sqrt12:sq12,E:g.E,w2:g.w2,
   pNumerator:freq.map(m=>-m*r3),pDenominator:sq2*g.w,targetFactor:cfg.orientation*sq12*cell.mu/(sq2*r4*g.w2),
   sigma:g.drdx/g.r,fluxPrefactor:cfg.orientation*sq2*r3*g.drdx*g.w2/(sq12*cell.mu),qLNumerator:sq2*g.w,meanFactor:g.drdx*g.w}});
 }
 const initial42=[...cp.states[stage+1],0,0];let state=Float64Array.from(initial42),minA=Infinity,minD=Infinity;
 const inc=(v,f,h)=>Float64Array.from(v,(x,j)=>x+h*f[j]);
 function field(v,profile,step,label,x){events.push({event:'rk_field',profile,step,label,x});const rt=engine.root(v,cell.profiles[profile],x),f=Float64Array.from(engine.rhs(v,cell.profiles[profile],x,false,rt));minA=Math.min(minA,rt.e.minA);minD=Math.min(minD,rt.e.minD);return f;}
 for(let p=0;p<grid.length;p++)for(let k=0;k<grid[p].length;k++){
  const {x,h}=grid[p][k],a=field(state,p,k,'a',x),b=field(inc(state,a,h/2),p,k,'b',x+h/2),c=field(inc(state,b,h/2),p,k,'c',x+h/2),d=field(inc(state,c,h),p,k,'d',x+h);
  for(let j=0;j<size;j++)state[j]+=h*(a[j]+2*b[j]+2*c[j]+d[j])/6;
 }
 const physicalState=Array.from(state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio),oldFlow=row.components.map(r=>r.flow);
 if(!bytes(physicalState).equals(bytes(oldFlow)))throw Error('Original traced scalar flow differs from the saved complete full-Jac row at '+stage);
 fixtures.push({stage,mu:cell.mu,portRatio:cell.portRatio,normalizationScale:row.components[0].normalizationScale,grid,points,initial42,targetNode40:cp.states[stage],scope:'Legacy ABI field suffixes42/40 contain actual18/16 values for n3/M8.'});
 referenceRows.push({stage,state:Array.from(state),state_sha256:hash(bytes(Array.from(state))),minA,minD,events,root_calls:events.filter(e=>e.event==='root_return').length,saved_fullJac_physical_output_equal:true});
 console.log(JSON.stringify({event:'m3_original_trace_complete',stage,outputs:size,root_calls:referenceRows.at(-1).root_calls,events:events.length,saved_fullJac_physical_output_equal:true}));
}
const context={scope:'Independent n3/M8 arithmetic baseline input. Original saved complete16 physical outputs are reused; only the previously missing original root/RK trace is evaluated. No DN/Newton/prefix solve, new initializer or production change.',command:process.argv,
 source_sha256:sources,input:ref(input),complete_rows:ref(rowsPath),traced_source:{root:ref(files.root),split:ref(files.split)},
 modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,independent_quadrature_nodes:cfg.quadrature,steps:cfg.steps,original_tail_gate:cfg.solveTolerance,
 root_rules:{floor:cfg.projectionFloor??.1,iterations:30,tolerance:8e-14,scale_floor:1e-300,halving_factors:Array.from({length:20},(_,j)=>2**(-j)),fallback_tolerance:5e-12},
 trace_arithmetic_restored_exactly:true,trace_patch_parent:'ca62c285779a8f1c60749bf208009f47ca887c3316015206fb1e68a1a3fe6205',named_stages:names};
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Bound source changed during capture: '+file);
const coefficients=save(files.coefficients,{...context,trig:{state_cos,state_sin},fixtures,trace_source_patches:patches});
const reference=save(files.reference,{...context,rows:referenceRows});
const summary={...context,coefficients,reference,named_results:referenceRows.map(r=>({stage:r.stage,state_sha256:r.state_sha256,outputs:size,root_calls:r.root_calls,trace_events:r.events.length,minA:r.minA,minD:r.minD,saved_fullJac_physical_output_equal:true})),seconds:(performance.now()-began)/1000};
fs.writeFileSync(files.summary,JSON.stringify(summary,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({event:'m3_capture_terminal',summary:ref(files.summary)}));
