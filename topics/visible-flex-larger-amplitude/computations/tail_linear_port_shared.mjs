// Complete finite linear port on the original stored metric. Physical point
// coefficients are evaluated once per RK4 grid point for all independent modes.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {advanceLinearColumns} from './closure_linear_stage_graphs.mjs';
import {createStoredPhysical} from './tail_stored_geometry.mjs';

const [topic,configFile,outFile,modesText='64',stepsText='4096',farText='48']=process.argv.slice(2);
if(!topic||!configFile||!outFile)
  throw Error('Usage: node tail_linear_port_shared.mjs SOURCE_TOPIC CONFIG OUTPUT [MODES STEPS FAR]');
const sourceRoot=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const {idealModeGraph}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')).href);
const modes=Number(modesText),steps=Number(stepsText),far=Number(farText);
if(![modes,steps,far].every(x=>Number.isInteger(x)&&x>0))throw Error('Positive integer resolution required');
const started=Date.now(),config=JSON.parse(fs.readFileSync(configFile,'utf8'));
const geometry=await createStoredPhysical(config),tail=geometry.physical;
if(far>tail.cells.length)throw Error('Far cell exceeds the original finite constructor');
const spacing=config.spacing??3,cut=tail.cells[0].profiles.at(-1)(1),r=cut.r,w=Math.exp(cut.logw);
const modesData=Array.from({length:modes},(_,j)=>{
  const mode=spacing*(j+1);return {mode,nu:mode*mode*(mode*mode-1)/12};
});
const ys=modesData.map(z=>[1,tail.parameters.orientation*idealModeGraph(z.mode,tail.parameters.R,tail.parameters.a)]);
const logGains=new Float64Array(modes);
let lastMu=tail.cells[far-1].mu,maximumHeapUsed=0,maximumRSS=0;
for(let n=far-1;n>=0;n--){
  const cell=tail.cells[n],ratio=lastMu/cell.mu;lastMu=cell.mu;
  for(const y of ys)y[1]*=ratio;
  advanceLinearColumns(ys,cell.profiles,cell.mu,modesData,steps);
  for(let j=0;j<modes;j++){
    const norm=Math.hypot(...ys[j]);
    if(!(norm>0&&Number.isFinite(norm)))throw Error('Nonfinite linear norm at cell '+n);
    ys[j][0]/=norm;ys[j][1]/=norm;logGains[j]+=Math.log(norm);
  }
  const usage=process.memoryUsage();
  maximumHeapUsed=Math.max(maximumHeapUsed,usage.heapUsed);maximumRSS=Math.max(maximumRSS,usage.rss);
  if(n%8===0)console.log(JSON.stringify({event:'cell-complete',cell:n,modes,steps,
    seconds:(Date.now()-started)/1000,heapUsed:usage.heapUsed,rss:usage.rss}));
}
const rows=ys.map((y,j)=>({mode:modesData[j].mode,
  slope:modesData[j].mode*modesData[j].mode/r+
    Math.sqrt(12)*tail.cells[0].mu*y[1]/(r**8*w*y[0]),
  logHeightGain:logGains[j]+Math.log(Math.abs(y[0]))+4*Math.log(r)}));
const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const result={method:'cusp-split RK4 momentum; shared physical coefficient grid',
  scope:'Complete finite linear transfer on the unchanged original stored metric. The same per-mode arithmetic is interleaved. No high-mode extrapolation, nonlinear solve, infinite-tail assertion, or metric substitution.',
  source_sha256:sha256(fs.readFileSync(new URL(import.meta.url))),
  shared_graph_sha256:sha256(fs.readFileSync(new URL('./closure_linear_stage_graphs.mjs',import.meta.url))),
  reference_source:'950f-tail-linear-cusp.mjs',
  reference_source_sha256:sha256(fs.readFileSync(path.join(topic,'scripts/950f-tail-linear-cusp.mjs'))),
  source_revision:JSON.parse(fs.readFileSync(path.join(topic,'source-origin.json'),'utf8')).source_revision,
  configuration_note:'Original per-mode RK4 arithmetic and cusp splits with shared physical coefficients and bounded private point caches; physical constructor and frozen warp alpha unchanged.',
  config,config_sha256:sha256(fs.readFileSync(configFile)),stats:tail.stats,
  stored_metric_adapter:geometry.manifest,modes,spacing,steps,far,
  cut:{r,w,wr:w*cut.dlogwdx/cut.drdx,E:1+w*w,Ep:2*w*w*cut.dlogwdx/cut.drdx},
  rows,maximumHeapUsed,maximumRSS,peakRSSKiB:process.resourceUsage().maxRSS,
  seconds:(Date.now()-started)/1000};
fs.writeFileSync(outFile,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({event:'done',output:outFile,modes,steps,seconds:result.seconds,
  maximumHeapUsed,maximumRSS,peakRSSKiB:result.peakRSSKiB}));
