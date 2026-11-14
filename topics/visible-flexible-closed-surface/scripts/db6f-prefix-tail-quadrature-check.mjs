// Compare the same saved physical tail state with numerical angular quadratures.
// This is a component cost/aliasing diagnostic, not a solved lower-quadrature DN.
import fs from 'node:fs';
import path from 'node:path';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {parseArgs} from 'node:util';
const {values:v}=parseArgs({options:{'source-root':{type:'string'},checkpoint:{type:'string'},
  config:{type:'string'},out:{type:'string'},quadratures:{type:'string',default:'256,512'}}});
for(const k of ['source-root','checkpoint','config','out'])if(!v[k])throw Error('Missing '+k);
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.resolve(v['source-root']);
const here=path.dirname(fileURLToPath(import.meta.url));
const source=name=>pathToFileURL(path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts',name));
const {createFastSplitFluxMomentumTailEngine}=await import(source('f6tail_fast_split_flux_engine.mjs'));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const sha=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const read=f=>JSON.parse((f.endsWith('.gz')?gunzipSync(fs.readFileSync(f)):fs.readFileSync(f)).toString());
const rec=read(v.checkpoint),cp=rec.response?.checkpoint??rec.checkpoint??rec;
const cfg=read(v.config),p=cp.parameters,M=p.modes,K=2*M;
const physical=createRecalibrationFactory(cfg).assemble();
const stages=subdividePhysical(physical,p.physicalDepth,p.shootingParts??1);
if(stages.cells.length+1!==cp.states.length)throw Error('Stage checkpoint mismatch');
const quadratures=v.quadratures.split(',').map(Number).sort((a,b)=>a-b);
if(!quadratures.includes(p.quadrature))throw Error('Include the saved quadrature');
if(quadratures.some(q=>!(Number.isInteger(q)&&q>4*M*p.spacing)))throw Error('Quadrature must satisfy the engine requirement N>4*M*spacing');
const selected=[];
for(let n=0;n<stages.cells.length;n++){
  const c=stages.cells[n];
  if(c.rawCell===0||n===cp.rawNode[c.rawCell]||n+1===cp.rawNode[c.rawCell+1])selected.push(n);
}
const caches=new Map(quadratures.map(q=>[q,new Map()]));
const engine=(q,c)=>{
  const cache=caches.get(q);
  if(!cache.has(c.mu))cache.set(c.mu,createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,
    quadrature:q,mu:c.mu,orientation:p.orientation,projectionFloor:p.projectionFloor}));
  return cache.get(c.mu);
};
function difference(a,b){
  let absolute=0,scale=0;
  for(let j=0;j<a.length;j++){absolute=Math.max(absolute,Math.abs(a[j]-b[j]));scale=Math.max(scale,Math.abs(b[j]));}
  return {absolute,relative:scale===0?absolute:absolute/scale};
}
const rows=[],timing=Object.fromEntries(quadratures.map(q=>[q,0]));
for(const n of selected)for(const x of [0,1]){
  const c=stages.cells[n],state=new Float64Array(K+2);
  state.set(cp.states[n+(x===0?1:0)]);
  if(x===1)for(let j=M;j<K;j++)state[j]*=c.portRatio;
  const values=new Map();
  for(const q of quadratures){
    const start=performance.now();
    const result=engine(q,c).rhsWithJacobian(state,c.profiles[0],x);
    timing[q]+=performance.now()-start;
    values.set(q,result);
  }
  const reference=values.get(p.quadrature),row={stage:n,rawCell:c.rawCell,x,
    minLeadingReference:reference.root.e.minA,comparisons:[]};
  for(const q of quadratures){
    const a=values.get(q);
    row.comparisons.push({quadrature:q,rhs:difference(a.derivative,reference.derivative),
      jacobian:difference(a.jacobian,reference.jacobian),
      root:difference(a.root.L,reference.root.L),minLeading:a.root.e.minA});
  }
  rows.push(row);
}
const maxima=quadratures.map(q=>{
  const a=rows.map(r=>r.comparisons.find(c=>c.quadrature===q));
  return {quadrature:q,evaluations:a.length,milliseconds:timing[q],
    rhsAbsolute:Math.max(...a.map(z=>z.rhs.absolute)),rhsRelative:Math.max(...a.map(z=>z.rhs.relative)),
    jacobianAbsolute:Math.max(...a.map(z=>z.jacobian.absolute)),jacobianRelative:Math.max(...a.map(z=>z.jacobian.relative)),
    rootAbsolute:Math.max(...a.map(z=>z.root.absolute)),rootRelative:Math.max(...a.map(z=>z.root.relative)),
    minimumLeading:Math.min(...a.map(z=>z.minLeading))};
});
const report={scope:'Same fixed physical metric and saved state. Actual RHS/Jacobian/root at saved stage endpoints; no new DN solve, no all-state aliasing proof.',
  checkpoint:path.resolve(v.checkpoint),checkpointSHA256:sha(v.checkpoint),config:path.resolve(v.config),
  configSHA256:sha(v.config),scriptSHA256:sha(fileURLToPath(import.meta.url)),modes:M,
  referenceQuadrature:p.quadrature,selectedStages:selected.length,maxima,rows};
fs.writeFileSync(v.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({modes:M,selectedStages:selected.length,maxima}));
