// New read-only observations at only the first original point root of each of
// three frozen stages. Quad/RHS terms are captured now, not attributed to the
// previous traces (which did not store quad). No flow, new root algorithm, DN,
// state update, or production mutation is performed.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {gunzipSync,gzipSync} from 'node:zlib';

const [capsuleArg,floatArg,mpArg,prefixArg]=process.argv.slice(2);
if(!prefixArg)throw Error('Need original capsule summary, float summary, MP90 summary, new output prefix');
const load=p=>JSON.parse(p.endsWith('.gz')?gunzipSync(fs.readFileSync(p)):fs.readFileSync(p,'utf8'));
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const bytes=a=>{const out=Buffer.alloc(8*a.length);a.forEach((v,j)=>out.writeDoubleLE(v,8*j));return out;};
const hashNumbers=a=>createHash('sha256').update(bytes(a)).digest('hex');
const same=(a,b)=>bytes(a).equals(bytes(b));
const capsuleSummary=load(capsuleArg),plainSummary=load(floatArg),mpSummary=load(mpArg);
if(sha(capsuleArg)!==plainSummary.capsule_summary_sha256||sha(capsuleArg)!==mpSummary.capsule_summary_sha256||
    sha(floatArg)!==mpSummary.validated_baseline_sha256||mpSummary.precision!=='mp'||mpSummary.dps!==90)
  throw Error('The exact original fixture/float/MP90 provenance differs');
if(!plainSummary.all_three_outputs42_bitwise_identical||!plainSummary.all_original_operands_and_judgments_bitwise_identical)
  throw Error('Complete exact original float baseline required');
for(const key of ['source_sha256','additional_original_root_sources'])
  for(const [file,value]of Object.entries(capsuleSummary[key]))if(sha(file)!==value)throw Error('Source changed: '+file);
for(const entry of [capsuleSummary.coefficients,capsuleSummary.reference,capsuleSummary.fixture,mpSummary.raw])
  if(sha(entry.path)!==entry.sha256)throw Error('Bound previous record changed');
const capsule=load(capsuleSummary.coefficients.path),old=load(capsuleSummary.reference.path),
  frozen=load(capsuleSummary.fixture.path),mp=load(mpSummary.raw.path),cfg=frozen.config;
const rootSource=Object.keys(capsuleSummary.source_sha256).find(p=>p.endsWith('/periodic-quadrature/general_root_tail_momentum.mjs'));
const topic=path.resolve(path.dirname(rootSource),'../..');
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const {createSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(path.dirname(rootSource),'f6tail_momentum_split_flux.mjs')));
const prefix=path.resolve(prefixArg),rawPath=prefix+'-raw.json.gz',summaryPath=prefix+'-summary.json';
for(const p of [rawPath,summaryPath])if(fs.existsSync(p))throw Error('Frozen output exists');
fs.mkdirSync(path.dirname(prefix),{recursive:true});

function firstRoot(events){
  let field,start,evaluation,end,stop;
  for(const event of events){
    if(event.event==='rk_field')field=event;
    if(event.event==='root_start')start=event;
    if(event.event==='evaluate_start')evaluation=event;
    if(event.event==='evaluate_end')end=event;
    if(event.event==='root_stop')stop=event;
    if(event.event==='root_return'){
      if(event.roundoffFallback||!stop.accepted||!evaluation.needJac)throw Error('Only the accepted ordinary first root is supported');
      return {field,start,evaluation,end,stop,returned:event};
    }
  }
  throw Error('No saved first root');
}
const rows=[],scalars=[],began=performance.now();
for(let index=0;index<capsule.fixtures.length;index++){
  const fixture=capsule.fixtures[index],reference=firstRoot(old.rows[index].events),mpReference=firstRoot(mp.rows[index].events);
  if(reference.field.profile!==0||reference.field.step!==0||reference.field.label!=='a'||reference.field.x!==0)
    throw Error('The first common original RK input changed');
  if(!same(reference.start.state,fixture.initial42))throw Error('Original first root input differs');
  if(!same(mpReference.start.state.map(Number),fixture.initial42))throw Error('MP first root input does not roundtrip to the original input');
  const point=fixture.points.find(v=>v.profile===0&&v.x===0),coeff=point.coefficients;
  const engine=createSplitFluxMomentumTailEngine({...cfg,mu:fixture.mu});
  const profile=x=>{if(x!==0)throw Error('Only the first frozen point may be evaluated');return {...point.geometry};};
  const initial=Float64Array.from(fixture.initial42),rt=engine.root(initial,profile,0);
  const target=[0,...Array.from(initial.slice(cfg.modes,2*cfg.modes),v=>coeff.targetFactor*v)];
  if(!same(rt.L,reference.evaluation.L)||!same(rt.e.moments,reference.end.moments)||
      !same(target,reference.start.target)||rt.err!==reference.stop.err||rt.scale!==reference.stop.scale||
      rt.iterations!==reference.stop.iteration)
    throw Error('New original point-root observation differs from the saved root/moments/stop identity');
  for(const [key,value]of Object.entries(point.geometry))if(!Object.is(value,rt.g[key]))throw Error('Original geometry differs');
  const derivative=Float64Array.from(engine.rhs(initial,profile,0,false,rt)),M=cfg.modes,
    nq=capsule.independent_quadrature_nodes,nonlinearFlux=new Float64Array(M),terms=[];
  for(let n=0;n<nq;n++){
    const v=rt.e.rows[n],g=rt.g,u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),
      factor=(v.K+u/(1+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd),f=v.U*factor;
    for(let j=0;j<M;j++)nonlinearFlux[j]+=f*capsule.trig.state_sin[n][j]/nq;
  }
  for(let j=0;j<M;j++){
    const m=(j+1)*cfg.spacing,L=rt.L[j+1],Q=initial[j],momentum=initial[M+j],
      pShape=coeff.pNumerator[j]*Q/coeff.pDenominator,
      qA=(m*m-4)*Q,qB=coeff.qLNumerator*L/coeff.r3,qInside=qA+qB,qRhs=coeff.sigma*qInside,
      fluxA=-m*L,fluxB=(m*m-1)*pShape,linearFlux=fluxA+fluxB,
      momentumA=4*coeff.sigma*momentum,momentumB=coeff.fluxPrefactor*m*(linearFlux+nonlinearFlux[j]),
      momentumRhs=momentumA+momentumB,
      derivedLinearMomentumB=coeff.fluxPrefactor*m*linearFlux;
    if(!Object.is(qRhs,derivative[j])||!Object.is(momentumRhs,derivative[M+j]))
      throw Error('The newly captured original RHS term operands do not reconstruct its derivative');
    terms.push({mode:m,Q,momentum,target:target[j+1],L,pShape,qA,qB,qInside,qRhs,fluxA,fluxB,linearFlux,
      nonlinearFlux:nonlinearFlux[j],momentumA,momentumB,momentumRhs,derivedLinearMomentumB,
      derivedLinearMomentumSum:momentumA+derivedLinearMomentumB});
  }
  const ell=Array.from(rt.L,(v,j)=>v-target[j]),originalResidual=Array.from(rt.e.moments,(v,j)=>v-target[j]),
    stableAtSameRepresentedL=ell.map((v,j)=>v+rt.e.quad[j]),reconstructed=ell.map((v,j)=>target[j]+v),
    originalNorm=Math.max(...originalResidual.map(Math.abs)),stableNorm=Math.max(...stableAtSameRepresentedL.map(Math.abs));
  if(originalNorm!==rt.err||!same(reconstructed,rt.L))throw Error('Original point-root residual or target+delta identity differs');
  rows.push({stage:fixture.stage,new_observation:true,initial42:Array.from(initial),target,L:Array.from(rt.L),
    quad:Array.from(rt.e.quad),moments:Array.from(rt.e.moments),originalResidual,representedEll:ell,
    stableResidualAtSameRepresentedL:stableAtSameRepresentedL,originalDerivative42:Array.from(derivative),
    coefficientPoint:point,terms,scale:rt.scale,iterations:rt.iterations,originalErr:rt.err,
    minA:rt.e.minA,minD:rt.e.minD,minS:rt.e.minS,
    savedOriginalFirstRoot:reference,savedMP90FirstRoot:mpReference,
    normalizationScale:fixture.normalizationScale,originalFirstStep:fixture.grid[0][0]});
  const summary={stage:fixture.stage,original_saved_root_identity:true,
    original_L_sha256:hashNumbers(Array.from(rt.L)),original_target_sha256:hashNumbers(target),
    newly_captured_quad_sha256:hashNumbers(Array.from(rt.e.quad)),newly_captured_derivative42_sha256:hashNumbers(Array.from(derivative)),
    original_relative_root_residual:rt.err/rt.scale,
    stable_residual_at_same_represented_L_relative:stableNorm/rt.scale,
    first_step_original_h:fixture.grid[0][0].h,iterations:rt.iterations,scale:rt.scale,minA:rt.e.minA,minD:rt.e.minD};
  scalars.push(summary);console.log(JSON.stringify({event:'new_original_first_root_captured',...summary}));
}
const context={scope:'New read-only observations at only the first same-input original point root of stages43/38/175. Quad and RHS operand terms are captured in this execution, not retroactively attributed to prior traces. Stable residual at the same represented L is a newly derived arithmetic diagnostic; no shifted-root algorithm is solved.',
  capsule_summary:{path:path.resolve(capsuleArg),sha256:sha(capsuleArg)},
  float_summary:{path:path.resolve(floatArg),sha256:sha(floatArg)},mp90_summary:{path:path.resolve(mpArg),sha256:sha(mpArg)},
  source_sha256:{...capsuleSummary.source_sha256,[path.resolve(process.argv[1])]:sha(process.argv[1])},
  additional_original_root_sources:capsuleSummary.additional_original_root_sources,
  command:process.argv,old_failed_state:capsuleSummary.input,
  point_roots_evaluated:3,new_flow_evaluations:0,nonlinear_tail_solver_invoked:false,
  production_source_changed:false,checkpoint_written:false};
fs.writeFileSync(rawPath,gzipSync(JSON.stringify({...context,rows})+'\n'));
const result={...context,named_results:scalars,raw:{path:rawPath,sha256:sha(rawPath)},seconds:(performance.now()-began)/1000};
fs.writeFileSync(summaryPath,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({event:'terminal',summary:summaryPath,sha256:sha(summaryPath)}));
