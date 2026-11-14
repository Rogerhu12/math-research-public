// Required second fundamental form at one already diagnosed height jet.
// No flow or DN; finite floating samples are diagnostics, not continuous bounds.
import fs from 'node:fs';import path from 'node:path';import zlib from 'node:zlib';import crypto from 'node:crypto';import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
import {createFourierRootSplitFluxEngine} from './78718-tail-fourier-root-split-engine.mjs';
const {createMomentumPhysicalJetEvaluator}=await import(pathToFileURL(path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts/f6tail_momentum_physical_jets.mjs')));
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.config||!opt.accepted||!opt.trial||!opt.out||fs.existsSync(opt.out))throw Error('inputs and fresh output required');
const inputs=[];function read(p){const b=fs.readFileSync(p);inputs.push({path:path.resolve(p),sha256:crypto.createHash('sha256').update(b).digest('hex')});return JSON.parse(p.endsWith('.gz')?zlib.gunzipSync(b):b);}
const cfg=read(opt.config),accepted=read(opt.accepted),trial=read(opt.trial),M=cfg.modes,N=cfg.quadrature,
 physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),stage=trial.stage,cell=stages.cells[stage],profile=cell.profiles[0];
function compute(input,floor){
 const engine=createFourierRootSplitFluxEngine({modes:M,spacing:cfg.spacing,quadrature:N,mu:cell.mu,orientation:cfg.orientation,projectionFloor:floor}),
  y=new Float64Array(2*M+2);y.set(input);
 const root=engine.root(y,profile,0),g=root.g,Kg=g.w2*g.dlogwdx/(g.r*g.E*g.E*g.drdx),
  evaluator=createMomentumPhysicalJetEvaluator(engine,{spacing:cfg.spacing}),jet=evaluator(y,profile,0);
 let worst=null,minLeading=null;
 for(let n=0;n<N;n++){
  const row=root.e.rows[n],c=g.w*row.A/(g.r*Math.sqrt(g.E)*row.sd),b=g.w*row.U/(g.r*row.sd),
   a=(Kg+b*b)/c,shape=(Math.abs(a+c)+Math.hypot(a-c,2*b))/2,
   v={theta:2*Math.PI*n/N,A:row.A,a,b,c,Kg,numerator:Kg+b*b,requiredShapeNorm:shape};
  if(!worst||shape>worst.requiredShapeNorm)worst=v;if(!minLeading||row.A<minLeading.A)minLeading=v;
 }
 return {floor,r:g.r,w:g.w,logSlopePerR:g.dlogwdx/g.drdx,Kg,minA:root.e.minA,
  rootRelative:root.err/root.scale,atMinA:minLeading,maximumRequiredShapeAtSampledAngles:worst,
  actualProjectedODEFormalCurvature:jet.formalHeightCurvature,
  actualProjectedODEMaxDarboux:jet.maxDarboux};
}
const report={scope:'Gauss-forced shape of a hypothetical exact isometry with the same local height and radial-height jet; sampled floating diagnostics only. No pointwise/nonlinear isometry is inferred from the finite projected ODE.',
 inputs,stage,x:0,modes:M,quadrature:N,accepted:compute(accepted.checkpoint.states[stage+1],.05),
 trial:compute(trial.inputState,1e-10)};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,...report}));

