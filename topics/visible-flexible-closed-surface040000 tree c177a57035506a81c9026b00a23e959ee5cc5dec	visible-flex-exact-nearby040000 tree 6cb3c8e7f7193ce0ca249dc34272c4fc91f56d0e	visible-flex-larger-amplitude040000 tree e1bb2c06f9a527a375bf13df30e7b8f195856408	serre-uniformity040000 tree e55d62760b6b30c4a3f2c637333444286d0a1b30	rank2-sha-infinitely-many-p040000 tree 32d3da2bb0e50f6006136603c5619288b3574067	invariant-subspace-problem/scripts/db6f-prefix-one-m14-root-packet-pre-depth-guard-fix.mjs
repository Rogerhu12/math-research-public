// One preselected endpoint from an already completed M14/N512 DN response.
// No RK flow, stage Jacobian, whole-tail solve, or endpoint scan is performed.
import fs from 'node:fs';
import path from 'node:path';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {parseArgs} from 'node:util';

const {values:v}=parseArgs({options:Object.fromEntries(
  ['source-root','config','checkpoint','out'].map(k=>[k,{type:'string'}]))});
for(const k of ['source-root','config','checkpoint','out'])if(!v[k])throw Error('Missing --'+k);
if(fs.existsSync(v.out)||fs.existsSync(v.out+'.tmp'))throw Error('Output already exists');
if(!v.out.endsWith('.json.gz'))throw Error('Output must end .json.gz');
const here=path.dirname(fileURLToPath(import.meta.url)),sourceRoot=path.resolve(v['source-root']);
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const source=name=>path.join(process.env.CLOSING_TAIL_CACHE,name);
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const {createMomentumTailEngine}=await import(pathToFileURL(source('general_root_tail_momentum.mjs')));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const config=read(v.config),record=read(v.checkpoint),cp=record.response?.checkpoint;
if(!record.response?.converged||!cp)throw Error('Input must be a completed converged response');
const p=cp.parameters,M=p.modes,N=p.quadrature,K=2*M,J=M+1;
if(M!==14||N!==512||p.spacing!==3||p.physicalDepth!==12||p.shootingParts!==8||p.steps!==32||p.projectionFloor!==.05)
  throw Error('Input is not the preselected original M14/N512 discretization');
if(!(record.response.residual>=0&&record.response.residual<config.solveTolerance))
  throw Error('Input DN residual does not meet its original tolerance');
for(const k of ['modes','quadrature','spacing','steps'])if(config[k]!==p[k])throw Error('Numerical config mismatch: '+k);
if(config.depth!==p.physicalDepth||config.shootingParts!==p.shootingParts)throw Error('Subdivision config mismatch');
const physical=createRecalibrationFactory(config).assemble();
for(const k of Object.keys(physical.parameters)){
  if(k in p&&JSON.stringify(p[k])!==JSON.stringify(physical.parameters[k]))
    throw Error('Physical parameter mismatch: '+k);
}
const staged=subdividePhysical(physical,p.physicalDepth,p.shootingParts),stage=37,x=0;
if(staged.cells.length+1!==cp.states.length)throw Error('State/stage dimensions differ');
const cell=staged.cells[stage],profile=cell.profiles[0];
if(cell.rawCell!==0||cell.rawSegment!==4||cell.rawLeft!==.25||cell.profiles.length!==1)
  throw Error('Preselected stage no longer identifies raw0/segment4/raw x=.25');
if(cp.states[stage+1].length!==K)throw Error('Wrong endpoint state dimension');
const state=new Float64Array(K+2);state.set(cp.states[stage+1]);
const options={modes:M,quadrature:N,spacing:p.spacing,mu:cell.mu,
  orientation:p.orientation,projectionFloor:p.projectionFloor};
const engine=createMomentumTailEngine(options);
const start=performance.now();
// This is the only root invocation. It uses the original default seed/guard.
const root=engine.root(state,profile,x),g=root.g,Q=state.slice(0,M),
  sq2=Math.sqrt(2),sq12=Math.sqrt(12),frequency=Float64Array.from({length:M},(_,j)=>p.spacing*(j+1)),
  target=new Float64Array(J),pcoef=new Float64Array(M),pt=new Float64Array(J),Ucoef=new Float64Array(M),
  factor=p.orientation*sq12*cell.mu/(sq2*g.r**4*g.w2);
for(let j=0;j<M;j++){
  target[j+1]=factor*state[M+j];
  pcoef[j]=-frequency[j]*g.r**3*Q[j]/(sq2*g.w);
  pt[j+1]=frequency[j]*pcoef[j];
  Ucoef[j]=-frequency[j]*root.L[j+1]+(frequency[j]*frequency[j]-1)*pcoef[j];
}
const cs=[],sn=[];
for(let n=0;n<N;n++){
  const theta=2*Math.PI*n/N,c=new Float64Array(J),s=new Float64Array(M);c[0]=1;
  for(let j=0;j<M;j++){c[j+1]=sq2*Math.cos(frequency[j]*theta);s[j]=sq2*Math.sin(frequency[j]*theta);}
  cs.push(Array.from(c));sn.push(Array.from(s));
}
const rows=root.e.rows.map(row=>{
  const T=2*row.K+row.K*row.K+g.E*row.P*row.P,u=g.w2*T;
  return {...row,T,u};
});
const scalarGeometry={...g};
for(const [key,value]of Object.entries(scalarGeometry))
  if(typeof value==='number'&&!Number.isFinite(value))throw Error('Nonfinite geometry '+key);
const bindings=new Map();
function bind(file){const full=path.resolve(file);bindings.set(full,{path:full,sha256:sha(full),bytes:fs.statSync(full).size});}
function bindOwn(file){
  const full=path.resolve(file);if(bindings.has(full))return;bind(full);
  const text=fs.readFileSync(full,'utf8'),pattern=/(?:from\s*|import\s*\()\s*['"](\.[^'"]+)['"]/g;
  for(const match of text.matchAll(pattern)){
    const dep=path.resolve(path.dirname(full),match[1]);if(fs.existsSync(dep)&&fs.statSync(dep).isFile())bindOwn(dep);
  }
}
for(const file of [fileURLToPath(import.meta.url),v.config,v.checkpoint])bind(file);
bindOwn(path.join(here,'closing_weighted_tail.mjs'));bindOwn(path.join(here,'950f-tail-subdivision.mjs'));
function bindBundle(dir){
  for(const entry of fs.readdirSync(dir,{withFileTypes:true})){
    const full=path.join(dir,entry.name);
    if(entry.isDirectory())bindBundle(full);else if(/\.(?:mjs|js|py)$/.test(entry.name))bind(full);
  }
}
bindBundle(sourceRoot);
const packet={
  status:'ONE_ORIGINAL_ROOT_AT_PRESELECTED_COMPLETED_M14_ENDPOINT',
  scope:'Fourth input of a maximum-four-point projection diagnostic. This is a preselected control, not a global worst point. One original angular root call; no RK, full DN, global Jacobian, or new geometry certification.',
  command:[process.execPath,...process.argv.slice(1)],
  origin:{checkpoint:path.resolve(v.checkpoint),checkpointSHA256:sha(v.checkpoint),
    config:path.resolve(v.config),configSHA256:sha(v.config),completedDNResidual:record.response.residual},
  location:{stage,rawCell:cell.rawCell,rawSegment:cell.rawSegment,profile:0,x,rawX:cell.rawLeft,
    inputNode:stage+1,stateConvention:'cp.states[stage+1], unchanged normalized Q/momentum; append two zero means; no port rescaling at profile x=0'},
  options,state:Array.from(state),Q:Array.from(Q),L:Array.from(root.L),geometry:scalarGeometry,
  target:Array.from(target),frequency:Array.from(frequency),p:Array.from(pcoef),pt:Array.from(pt),U:Array.from(Ucoef),
  root:{error:root.err,scale:root.scale,relativeResidual:root.err/root.scale,iterations:root.iterations,
    minA:root.e.minA,minD:root.e.minD,minS:root.e.minS,roundoffFallback:!!root.roundoffFallback,maxQuad:root.e.maxQuad},
  originalEvaluation:{moments:Array.from(root.e.moments),quad:Array.from(root.e.quad),B:Array.from(root.e.B),rows},
  originalRoundedBasis:{cs,sn,sqrt2:sq2},
  sourceBindings:[...bindings.values()].sort((a,b)=>a.path.localeCompare(b.path)),
  sourceBindingScope:'Own factory/subdivision static imports and the complete frozen source-root code bundle are bound conservatively; not every bundled source is executed.',
  singleOriginalRootCalls:1,flowCalls:0,wholeDNEvaluations:0,seconds:performance.now()-start,
};
const bytes=gzipSync(JSON.stringify(packet)+'\n');
if(bytes.length>=5_000_000)throw Error('Packet exceeds file limit');
fs.writeFileSync(v.out+'.tmp',bytes,{flag:'wx'});fs.renameSync(v.out+'.tmp',v.out);
console.log(JSON.stringify({out:path.resolve(v.out),sha256:sha(v.out),bytes:bytes.length,
  stage,rawCell:cell.rawCell,rawSegment:cell.rawSegment,rawX:cell.rawLeft,
  rootRelative:root.err/root.scale,minA:root.e.minA,minD:root.e.minD,minS:root.e.minS,
  iterations:root.iterations,roundoffFallback:!!root.roundoffFallback,seconds:packet.seconds}));
