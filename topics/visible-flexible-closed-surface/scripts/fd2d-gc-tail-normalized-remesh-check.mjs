// Actual stored-node spectral prolongation check; no ODE or DN is solved.
import fs from 'node:fs';
import zlib from 'node:zlib';
import {createHash} from 'node:crypto';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {subdividePhysical} from './fd2d-gc-tail-stage-graphs.mjs';
import {createDeepSplitMomentumEngine} from './fd2d-gc-tail-deep-engine.mjs';
import {geometricWarmRemesh} from './fd2d-gc-tail-normalized-warm-remesh.mjs';

const [configFile,responseFile,outputPrefix]=process.argv.slice(2);
if(!configFile||!responseFile||!outputPrefix)throw Error('config, actual response and output prefix required');
const started=Date.now(),hash=b=>createHash('sha256').update(b).digest('hex'),
 cfgBytes=fs.readFileSync(configFile),responseBytes=fs.readFileSync(responseFile),
 cfg=JSON.parse(cfgBytes),response=JSON.parse(responseBytes),prior=response.checkpoint;
if(!response.converged||!prior||prior.parameters.modes!==4||prior.parameters.quadrature!==64)
 throw Error('This fixture requires a complete actual M4/N64 response');
const M=8,N=128,factory=createRecalibrationFactory(cfg),
 cache=boundTailPointCaches(factory,cfg,{pointsPerEntry:8}),physical=factory.assemble(),
 stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),engines=new Map(),
 cells=stages.cells.map(c=>{
  if(!engines.has(c.mu))engines.set(c.mu,createDeepSplitMomentumEngine({modes:M,spacing:cfg.spacing,
   quadrature:N,mu:c.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor}));
  return {...c,engine:engines.get(c.mu)};
 }),parameters={...prior.parameters,modes:M,quadrature:N},
 dn={tail:{cells,rawNode:stages.rawNode,parameters}},
 converted=geometricWarmRemesh(prior,dn,createDeepSplitMomentumEngine);
if(converted.diagnostics.maxQChange!==0)throw Error('Physical Q changed');
if(!converted.states.every(s=>s.length===2*M&&s.every(Number.isFinite)))throw Error('Nonfinite converted state');
const selected=[];
for(const node of [0,18,28,36,2640,2880]){
 const cell=cells[node===0?0:node-1],profile=node===0?cell.profiles.at(-1):cell.profiles[0],x=node===0?1:0,
  state=Float64Array.from([...converted.states[node],0,0]);
 if(node===0)for(let j=0;j<M;j++)state[M+j]*=cell.portRatio;
 const root=cell.engine.root(state,profile,x);
 selected.push({node,rawCell:cell.rawCell,rawSegment:cell.rawSegment,logw:root.g.logw,
  old_Q:prior.states[node].slice(0,4),new_Q:converted.states[node].slice(0,8),
  normalized_L:Array.from(root.L),rootRelativeResidual:root.err/root.scale,
  minimumLeading:root.e.minA,minimumD:root.e.minD});
}
const checkpoint={parameters,states:converted.states,rawNode:stages.rawNode,
 rawStates:stages.rawNode.map(n=>converted.states[n]),cutHeight:[...prior.cutHeight,0,0,0,0],
 scope:'Actual Q/L spectral prolongation of a stored M4/N64 solution. M8/N128 initial guess only; no new ODE, Newton residual, DN or geometry certificate.'},
 bytes=zlib.gzipSync(JSON.stringify({status:'spectrally-prolonged-initial-guess-only',checkpoint})+'\n');
if(bytes.length>=5_000_000)throw Error('Converted checkpoint exceeds file limit');
fs.writeFileSync(outputPrefix+'-initial.json.gz',bytes,{flag:'wx'});
const report={schema:'fd2d-actual-node-normalized-spectral-prolongation-check-v1',
 source:{path:import.meta.filename,sha256:hash(fs.readFileSync(import.meta.filename))},
 config:{path:configFile,sha256:hash(cfgBytes),bytes:cfgBytes.length},
 actual_source_response:{path:responseFile,sha256:hash(responseBytes),bytes:responseBytes.length,
  actualResidual:response.residual,actualHeight:prior.cutHeight},
 converted:{path:outputPrefix+'-initial.json.gz',sha256:hash(bytes),bytes:bytes.length},
 diagnostics:converted.diagnostics,selected,pointCache:cache,seconds:(Date.now()-started)/1000,
 scope:checkpoint.scope};
fs.writeFileSync(outputPrefix+'-report.json',JSON.stringify(report,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({report:outputPrefix+'-report.json',seconds:report.seconds,
 converted:report.converted,diagnostics:report.diagnostics}));
