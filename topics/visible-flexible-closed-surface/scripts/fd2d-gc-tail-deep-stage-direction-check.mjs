// Read-only local diagnosis of an observed complete nonlinear iteration.
import fs from 'node:fs';
import zlib from 'node:zlib';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {subdividePhysical} from './fd2d-gc-tail-stage-graphs.mjs';
import {createDeepSplitMomentumEngine} from './fd2d-gc-tail-deep-engine.mjs';
const [configFile,checkpointFile,stageText,output]=process.argv.slice(2),cfg=JSON.parse(fs.readFileSync(configFile)),
 record=JSON.parse(zlib.gunzipSync(fs.readFileSync(checkpointFile))),prior=record.checkpoint,
 factory=createRecalibrationFactory(cfg),cache=boundTailPointCaches(factory,cfg,{pointsPerEntry:8}),
 physical=factory.assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),
 n=Number(stageText),cell=stages.cells[n],M=cfg.modes,K=2*M,
 engine=createDeepSplitMomentumEngine({modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,mu:cell.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor}),
 initial=new Float64Array(K+2);
initial.set(prior.states[n+1]);
const f=engine.flowStateWithJacobian(initial,cell.profiles,{stepsPerSegment:cfg.steps}),rows=[];
for(let i=0;i<K;i++){
 let product=0;for(let j=0;j<K;j++)product+=f.tangent[i*K+j]*initial[j];
 rows.push({component:i,initial:initial[i],actual_end:f.state[i],J_times_initial:product,
  difference:f.state[i]-product,relative:(f.state[i]-product)/Math.max(1e-300,...initial.slice(0,K).map(Math.abs)),
  rawResidual:f.state[i]/(i<M?1:cell.portRatio)-prior.states[n][i]});
}
const points=[];
for(let j=0;j<cell.profiles.length;j++)for(const x of [0,.25,.5,.75,1]){
 const g=engine.geometry(cell.profiles[j],x),r=engine.root(initial,cell.profiles[j],x),v=engine.rhsWithJacobian(initial,cell.profiles[j],x);
 const component=[];for(let i=0;i<K;i++){let p=0;for(let k=0;k<K;k++)p+=v.jacobian[i*K+k]*initial[k];component.push({i,rhs:v.derivative[i],J_times_initial:p,difference:v.derivative[i]-p});}
 points.push({j,x,g,L:Array.from(r.L),component});
}
const report={stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,mu:cell.mu,portRatio:cell.portRatio,checkpointFile,iteration:record.iteration,rows,points,scope:'One actual stored stage, no new whole-tail solve or accepted state.'};
fs.writeFileSync(output,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,mu:cell.mu,portRatio:cell.portRatio,rows,maximum_point_logw:Math.max(...points.map(p=>p.g.logw)),minimum_point_logw:Math.min(...points.map(p=>p.g.logw))}));
