// One ORIGINAL state-only flow of an explicitly selected harmonic warm guess.
// No Newton step, no DN derivative, no tail acceptance. This optional comparison
// is never an automatic prerequisite for the active full-H continuation.
// Required flags: --source-topic --config --checkpoint --target-height
//                 --max-scale --report. The native manifest/run environment is
// supplied exactly as for the original worker, with a fresh owned run directory.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
const flags={};
for(let i=2;i<process.argv.length;i+=2){
 if(!process.argv[i]?.startsWith('--')||process.argv[i+1]===undefined)throw Error('Expected flag/value pairs');
 flags[process.argv[i].slice(2)]=process.argv[i+1];
}
for(const key of ['source-topic','config','checkpoint','target-height','max-scale','report'])
 if(flags[key]===undefined)throw Error('Missing --'+key);
const start=Date.now(),source=path.resolve(flags['source-topic']);
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const cfg=JSON.parse(fs.readFileSync(flags.config,'utf8'));
if(cfg.correctInitialBoundary===false)throw Error('Retain the original linear boundary correction');
const raw=fs.readFileSync(flags.checkpoint);
const record=JSON.parse((flags.checkpoint.endsWith('.gz')?zlib.gunzipSync(raw):raw).toString());
if(record.response?.converged!==true||record.response?.failed||
   !Number.isFinite(record.response.residual)||record.response.residual>(cfg.solveTolerance??2e-10))
 throw Error('This probe requires a complete accepted original shooting response');
const prior=record.response.checkpoint;
if(!prior?.parameters||!prior?.states||!prior?.cutHeight)throw Error('Missing complete checkpoint');
const targetRecord=JSON.parse(fs.readFileSync(flags['target-height'],'utf8'));
const H=Array.isArray(targetRecord)?targetRecord:targetRecord.height;
if(!Array.isArray(H)||H.length!==cfg.modes||H.some(v=>!Number.isFinite(v)))throw Error('Invalid physical target H');
const load=name=>import(pathToFileURL(path.join(source,'scripts',name)));
const {fullHarmonicEligibility}=await load('full_harmonic_warm_predictor.mjs');
const ratio=H[0]/prior.cutHeight[0],maxScale=Number(flags['max-scale']);
const eligibility=fullHarmonicEligibility(prior.cutHeight,H,ratio,maxScale);
const report={scope:'One original state-only residual evaluation of an optional initial guess; no Newton, no accepted tail, no DN derivative.',
 source_topic:source,source_sha256:sha(new URL(import.meta.url)),checkpoint:flags.checkpoint,
 checkpoint_sha256:sha(flags.checkpoint),config_sha256:sha(flags.config),
 target_height_sha256:sha(flags['target-height']),eligibility,
 accepted_tail:false,DN_derivative_computed:false,newton_steps:0,state_only_evaluations_attempted:0,state_only_evaluations:0,
 native_manifest_sha256:process.env.VISIBLE_FLEX_NATIVE_MANIFEST_SHA256,
 native_run_directory:process.env.VISIBLE_FLEX_NATIVE_RUN_DIR};
function save(){
 report.seconds=(Date.now()-start)/1000;
 fs.mkdirSync(path.dirname(path.resolve(flags.report)),{recursive:true});
 fs.writeFileSync(flags.report,JSON.stringify(report,null,2)+'\n');
}
if(!eligibility.eligible){report.status='predictor_ineligible_no_flow';save();console.log(JSON.stringify(report));process.exit(0);}
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(source,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
try{
 const {createRecalibrationFactory}=await load('closing_weighted_tail.mjs');
 const {createNativeCompactTailDN}=await load('native_batch_factory.mjs');
 const {remeshCheckpoint}=await load('950f-tail-warm-remesh.mjs');
 const {createFastSplitFluxMomentumTailEngine}=await load('periodic-quadrature/f6tail_fast_split_flux_engine.mjs');
 const physical=createRecalibrationFactory(cfg).assemble();
 const dn=createNativeCompactTailDN({...cfg,tail:physical}),M=cfg.modes;
 const old=prior.parameters,now=dn.tail.parameters;
 for(const key of ['pulseCaps','valleyCaps','flatOuterThroughCell','flatOuterStartSegment','flatSlope','capMode','rCut','wCut','width','curvatureBound','slopeCap','capTransition','calibrationSteps','warpSteps','quadratureTolerance','cuspAwareQuadrature','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','warpWeightLevels','constructor','valleyControls','delta0','R','a','etaPower','etaRatioAtN0','rejoinR20At','rejoinIndexOffset','spacing'])
  if(JSON.stringify(old[key]??null)!==JSON.stringify(now[key]??null))throw Error('Original warm geometry mismatch: '+key);
 for(const key of ['modes','physicalDepth','shootingParts','quadrature','steps'])
  if(old[key]!==now[key])throw Error('This comparison keeps the finite tail unchanged: '+key);
 const states=remeshCheckpoint(prior,dn,createFastSplitFluxMomentumTailEngine);
 let initial=states.map(row=>row.map((v,j)=>v*ratio**(j%M+1)));
 if(initial.some(row=>row.some(v=>!Number.isFinite(v))))throw Error('Nonfinite harmonic initial guess');
 const zero=dn.cutJets(new Float64Array(2*M)),r4=zero.radius**4;
 const delta=Float64Array.from(H,(v,j)=>v/r4-initial[0][j]);
 const add=dn.tail.initial(delta);
 initial=initial.map((row,n)=>row.map((v,j)=>v+add[n][j]));
 const target=Float64Array.from(H,v=>v/r4),scales=new Float64Array(initial.length);
 scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
 for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
 report.state_only_evaluations_attempted=1;
 const ev=dn.tail.evaluate(initial,target,false,scales);
 report.state_only_evaluations=1;
 report.status='original_state_only_residual_returned';
 report.normalized_residual=ev.norm;
 report.original_shooting_threshold=cfg.solveTolerance??2e-10;
 report.state_residual_below_threshold=ev.norm<report.original_shooting_threshold;
 report.minimum_flow_A=Math.min(...ev.flows.map(f=>f.minA));
 report.minimum_flow_D=Math.min(...ev.flows.map(f=>f.minD));
 report.linear_boundary_correction_preserved=true;
 report.complete_stage_count=ev.flows.length;
}catch(error){report.status='probe_error_no_tail_acceptance';report.error=String(error);save();console.log(JSON.stringify(report));process.exitCode=1;}
save();console.log(JSON.stringify(report));
