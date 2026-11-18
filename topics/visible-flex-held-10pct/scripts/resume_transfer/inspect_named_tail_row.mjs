// Read only: two original local full-Jacobian rows and named components.
// Reuse the already completed full-state candidate replay as the identity.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,input,baseline,nodeText,componentText,output]=process.argv.slice(2);
if(!output||fs.existsSync(output))throw Error('Need explicit fresh output and named row/components');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const r=JSON.parse(gunzipSync(fs.readFileSync(input))),b=JSON.parse(fs.readFileSync(baseline));
if(!r.response.failed||b.input.sha256!==sha(input)||b.before.norm!==r.response.lastIteration.norm||
 b.original_solver_invoked!==false)throw Error('The completed original failed-state replay must be the same');
const cfg=r.config,cp=r.response.checkpoint,n=Number(nodeText),components=componentText.split(',').map(Number);
const sources={...b.source_sha256};
for(const [name,digest] of Object.entries(r.source_sha256))sources[path.resolve(topic,'scripts',name)]=digest;
for(const [p,digest] of Object.entries(sources))if(sha(p)!==digest)throw Error('Source changed: '+p);
sources[path.resolve(process.argv[1])]=sha(process.argv[1]);
const source=path.join(topic,'repro/source-root');process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,N=dn.tail.cells.length;
if(!Number.isInteger(n)||!(n>0&&n<N)||components.some(j=>!Number.isInteger(j)||j<0||j>=K))
 throw Error('Named internal row and finite component indices required');
const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
const target=cp.cutHeight.map(v=>v/radius**4),scales=new Float64Array(N+1);
scales[0]=Math.max(1e-250,...target.map(Math.abs));for(let k=0;k<N;k++)scales[k+1]=scales[k]/Math.abs(dn.tail.gains[k][0]);
const view=new DataView(new ArrayBuffer(8));
function neighbor(v,direction){
 if(v===0)return direction*Number.MIN_VALUE;
 view.setFloat64(0,v,false);const bits=view.getBigUint64(0,false);
 view.setBigUint64(0,(v>0)===(direction>0)?bits+1n:bits-1n,false);return view.getFloat64(0,false);
}
const rows=[];
for(const k of [n-1,n]){
 const cell=dn.tail.cells[k],x=new Float64Array(K+2);x.set(cp.states[k+1]);
 const f=cell.engine.flowStateWithJacobian(x,cell.profiles,{stepsPerSegment:cfg.steps});
 const values=Array.from(f.state.slice(0,K),(v,j)=>v/(j<M?1:cell.portRatio));
 const residual=values.map((v,j)=>v-cp.states[k][j]);
 const norm=Math.max(...residual.map(v=>Math.abs(v)/scales[k]));
 rows.push({stage:k,norm,normalizationScale:scales[k],minA:f.minA,minD:f.minD,
  named:components.map(j=>{
   const state=cp.states[k][j],flow=values[j],sign=Math.sign(residual[j]);
   let columnMax=0;
   for(let i=0;i<K;i++)columnMax=Math.max(columnMax,Math.abs(f.tangent[i*K+j]/(i<M?1:cell.portRatio)));
   return {component:j,physicalMode:(j%M+1)*cfg.spacing,state,flow,signedResidual:residual[j],
    normalizedResidual:Math.abs(residual[j])/scales[k],direction:sign,
    adjacentTowardFlow:sign?neighbor(state,sign):state,
    isExactlyOneDirectedNeighbor:sign!==0&&Object.is(neighbor(state,sign),flow),
    inputColumnMax:columnMax,diagonal:f.tangent[j*K+j]/(j<M?1:cell.portRatio)};
  })});
}
if(rows[1].norm!==b.before.norm)throw Error('Named row does not reproduce the recorded full maximum');
const result={scope:'Only named original local full-Jacobian row values and derivatives. No state change, full replay or solver is performed.',
 command:process.argv,input:{path:path.resolve(input),sha256:sha(input)},baseline:{path:path.resolve(baseline),sha256:sha(baseline)},
 source_sha256:sources,originalGate:cfg.solveTolerance,originalFullNorm:b.before.norm,
 row:n,components,rows,statesChanged:false,originalSolverInvoked:false};
fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({output_sha256:sha(output),rows:rows.map(row=>({stage:row.stage,norm:row.norm,named:row.named})),solver_invoked:false}));
