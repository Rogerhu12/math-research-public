// Saved-node numerical diagnostic: default angular-root guess versus its root.
// No new shooting solve, no trial-rejection attribution, no continuous bound.
import fs from 'node:fs';
import path from 'node:path';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {parseArgs} from 'node:util';
const {values:v}=parseArgs({options:{'source-root':{type:'string'},checkpoint:{type:'string'},
  config:{type:'string'},out:{type:'string'}}});
for(const k of ['source-root','checkpoint','config','out'])if(!v[k])throw Error('Missing '+k);
if(fs.existsSync(v.out))throw Error('Refusing to overwrite output');
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.resolve(v['source-root']);
const here=path.dirname(fileURLToPath(import.meta.url));
const source=name=>pathToFileURL(path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,
  'topics/large-amplitude-twist-flex/scripts',name));
const {createMomentumTailEngine}=await import(source('general_root_tail_momentum.mjs'));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>JSON.parse((p.endsWith('.gz')?gunzipSync(fs.readFileSync(p)):fs.readFileSync(p)).toString());
const rec=read(v.checkpoint),cp=rec.response?.checkpoint??rec.checkpoint??rec;
const p=cp.parameters,M=p.modes,K=2*M,N=p.quadrature,sq2=Math.sqrt(2),sq12=Math.sqrt(12);
const physical=createRecalibrationFactory(read(v.config)).assemble();
const staged=subdividePhysical(physical,p.physicalDepth,p.shootingParts??1);
if(staged.cells.length+1!==cp.states.length)throw Error('Stage dimension mismatch');
const engines=new Map();
const getEngine=c=>{
  if(!engines.has(c.mu))engines.set(c.mu,createMomentumTailEngine({modes:M,spacing:p.spacing,
    quadrature:N,mu:c.mu,orientation:p.orientation,projectionFloor:p.projectionFloor}));
  return engines.get(c.mu);
};
const frequencies=Array.from({length:M},(_,j)=>(j+1)*p.spacing);
const cos=Array.from({length:N},(_,n)=>frequencies.map(m=>sq2*Math.cos(2*Math.PI*n/N*m)));
const sin=Array.from({length:N},(_,n)=>frequencies.map(m=>sq2*Math.sin(2*Math.PI*n/N*m)));
function initialMargin(state,g,mu){
  const factor=p.orientation*sq12*mu/(sq2*g.r**4*g.w2);
  const target=frequencies.map((m,j)=>factor*state[M+j]);
  const Pcoef=frequencies.map((m,j)=>-m*g.r**3*state[j]/(sq2*g.w));
  let minA=Infinity,minD=Infinity,minS=Infinity,atA=null;
  for(let n=0;n<N;n++){
    let L=0,P=0,Pt=0;
    for(let j=0;j<M;j++){
      L+=target[j]*cos[n][j];P+=Pcoef[j]*sin[n][j];Pt+=frequencies[j]*Pcoef[j]*cos[n][j];
    }
    const k=L-Pt,T=2*k+k*k+g.E*P*P,D=1-g.w2*T,S=1-g.w2*P*P,A=1+L+g.w2*Pt;
    if(A<minA){minA=A;atA=2*Math.PI*n/N;}
    minD=Math.min(minD,D);minS=Math.min(minS,S);
  }
  return {minA,minD,minS,thetaAtMinA:atA,passesOriginalGuard:
    minA>p.projectionFloor&&minD>p.projectionFloor&&minS>p.projectionFloor};
}
const rows=[];
for(let n=0;n<staged.cells.length;n++){
  const c=staged.cells[n];
  if(!(c.rawCell===0||n===cp.rawNode[c.rawCell]||n+1===cp.rawNode[c.rawCell+1]))continue;
  for(const x of [0,1]){
    const e=getEngine(c),state=new Float64Array(K+2);state.set(cp.states[n+(x===0?1:0)]);
    if(x===1)for(let j=M;j<K;j++)state[j]*=c.portRatio;
    const row={stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,x,
      rawX:c.rawLeft+(c.rawRight-c.rawLeft)*x};
    try{
      const g=e.geometry(c.profiles[0],x);row.radius=g.r;row.defaultGuess=initialMargin(state,g,c.mu);
      const r=e.root(state,c.profiles[0],x);
      row.root={minA:r.e.minA,minD:r.e.minD,minS:r.e.minS,iterations:r.iterations,
        residual:r.err,scale:r.scale};
    }catch(error){row.failure=String(error);}
    rows.push(row);
  }
}
const successful=rows.filter(r=>r.root),guesses=rows.filter(r=>r.defaultGuess);
const ordered=guesses.toSorted((a,b)=>a.defaultGuess.minA-b.defaultGuess.minA);
const report={status:'saved-node-root-initialization-diagnostic-not-a-certificate',
  scope:'Compare the default L=target initialization with the original solved angular root at saved stage endpoints. These are an UNCONVERGED shooting iterate when the input is a recovery file. No rejected trial or unsaved RK interior point is reconstructed.',
  checkpoint:path.resolve(v.checkpoint),checkpointSHA256:sha(v.checkpoint),inputIteration:rec.iteration??null,
  config:path.resolve(v.config),configSHA256:sha(v.config),scriptSHA256:sha(fileURLToPath(import.meta.url)),
  rootSourceSHA256:sha(fileURLToPath(source('general_root_tail_momentum.mjs'))),
  modes:M,quadrature:N,projectionFloor:p.projectionFloor,evaluations:rows.length,
  failedEvaluations:rows.length-successful.length,
  minimumDefaultGuessA:Math.min(...guesses.map(r=>r.defaultGuess.minA)),
  minimumSolvedRootA:Math.min(...successful.map(r=>r.root.minA)),rows};
fs.writeFileSync(v.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({evaluations:report.evaluations,failed:report.failedEvaluations,
  minimumDefaultGuessA:report.minimumDefaultGuessA,minimumSolvedRootA:report.minimumSolvedRootA,
  lowestDefaultGuessNodes:ordered.slice(0,3).map(r=>({stage:r.stage,rawCell:r.rawCell,
    rawSegment:r.rawSegment,rawX:r.rawX,guessA:r.defaultGuess.minA,rootA:r.root?.minA,
    iterations:r.root?.iterations,failure:r.failure}))}));
