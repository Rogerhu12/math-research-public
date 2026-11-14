// One finite physical design: redistribute outer-valley width while retaining
// the old inner warp scale. The final cut radius and beta0 are actual roots.
// All quantities here are finite diagnostics; unchanged deep source is explicit.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import v8 from 'node:v8';
import {createRecalibrationFactory,solvePhysicalCell} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
const [input,portFile,out,weightArg='12',stepsArg='256']=process.argv.slice(2);
if(!input||!portFile||!out)throw Error('base-config actual-port unused-output-prefix [valley-weight] [steps]');
const W=Number(weightArg),steps=Number(stepsArg),hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
if(!(W>=1&&W<=10000))throw Error('positive finite valley weight');
const cfg=JSON.parse(fs.readFileSync(input,'utf8')),port=JSON.parse(fs.readFileSync(portFile,'utf8'));
if(!port.completed||port.config_sha256!==hash(input)||port.far<cfg.protectCell)throw Error('actual full-depth base port required');
const checkpoint=out+'-checkpoint.json';if(fs.existsSync(checkpoint))throw Error('unused output prefix');
const started=Date.now(),memory=()=>({...process.memoryUsage(),heap_size_limit:v8.getHeapStatistics().heap_size_limit});
const write=(f,d)=>{fs.writeFileSync(f+'.tmp',JSON.stringify(d,null,2)+'\n');fs.renameSync(f+'.tmp',f);};
let base=createRecalibrationFactory(cfg);boundTailPointCaches(base,cfg,{pointsPerEntry:8});let old=base.assemble();
const targetLambda=old.stats.alpha,rStart=old.cells[0].rStart,cuff=old.stats.rCuff;
let rc=cfg.rCut,beta=cfg.valleyControls[0],state={schema:'fd2d-outer-valley-width-retarget-v1',
 source_sha256:hash(new URL(import.meta.url)),base_config_file:path.basename(input),base_config_sha256:hash(input),
 base_port_file:path.basename(portFile),base_port_sha256:hash(portFile),valley_weight:W,steps,
 target_inner_lambda:targetLambda,inner_cell0_radius:rStart,rows:[],completed:false,
 scope:'New physical g; only outer log-slope beta0 and outer free-warp weights are redesigned. Cut radius is chosen to retain the old free radial scale; actual assembled g and all linear/nonlinear ports need reevaluation. No exact finite T21 or nonlinear certificate.',
 memory:memory()};write(checkpoint,state);
old=null;base=null;if(typeof global.gc==='function')global.gc();
try{
 for(let outer=0;outer<8;outer++){
  const design={...cfg,rCut:rc,width:rc-cuff,
   warpWeightLevels:Array.from({length:cfg.protectCell},(_,n)=>n===0?[1,1,W,1,1]:[1,1,1,1,1])};
  let factory=createRecalibrationFactory(design);
  const originalGet=factory.getEntries,seen=new WeakSet();
  const touch=(n,b)=>{const row=originalGet(n,b);if(!seen.has(row)){
   boundTailPointCaches({getEntries:()=>row,parameters:factory.parameters},{protectCell:1,valleyControls:[b]},{pointsPerEntry:8});seen.add(row);}return row;};
  const originalPhysical=factory.physicalCell;
  factory.physicalCell=(n,b,r,l)=>{touch(n,b);return originalPhysical(n,b,r,l);};
  const guess=outer===0?beta+Math.log(W):beta;
  const solved=solvePhysicalCell(factory,0,rStart,targetLambda,{steps,tolerance:1e-8,initialBeta:guess,limit:72});
  beta=solved.beta;const nextRadius=solved.cell.rEnd;
  const row={outer,cut_radius_requested:rc,cut_radius_actual:nextRadius,radius_residual:nextRadius-rc,
    beta,gain_Q:solved.gain,momentum_residual:solved.zeroResidual,root_trace:solved.trace,memory:memory()};
  state.rows.push(row);state.current={rCut:nextRadius,beta};state.seconds=(Date.now()-started)/1000;write(checkpoint,state);
  console.log(JSON.stringify({event:'outer',...row}));
  if(Math.abs(nextRadius-rc)<2e-10){
   design.valleyControls=cfg.valleyControls.slice();design.valleyControls[0]=beta;
   design.historical_calibration_only=design.design_calibration;delete design.design_calibration;
   design.calibration_status='New one-cell weighted-width design. Actual finite beta0 root and radius closure only; no nonlinear or interval claim.';
   design.outer_width_design={source_sha256:state.source_sha256,base_config_file:path.basename(input),base_config_sha256:hash(input),
    target_inner_lambda:targetLambda,root_report:path.basename(checkpoint),valley_weight:W,
    finite_radius_residual:row.radius_residual,finite_momentum_residual:row.momentum_residual,
    physical_cuff_definition:'rCuff=8/25; binary factory subtraction is its finite evaluation',
    deep_source_unchanged_from_cell:160};
   for(let n=0;n<cfg.protectCell;n++)touch(n,design.valleyControls[n]);
   const tail=factory.assemble(design.valleyControls);
   state.final_stats=tail.stats;state.final_beta=beta;state.final_cut=rc;
   write(out+'-config.json',design);state.final_config_file=path.basename(out+'-config.json');state.final_config_sha256=hash(out+'-config.json');
   state.completed=true;state.seconds=(Date.now()-started)/1000;state.memory=memory();write(checkpoint,state);
   console.log(JSON.stringify({event:'complete',stats:state.final_stats,sha256:state.final_config_sha256,seconds:state.seconds,memory:state.memory}));break;
  }
  rc=nextRadius;factory=null;if(typeof global.gc==='function')global.gc();
 }
 if(!state.completed){state.stop_reason='outer radius iteration limit';write(checkpoint,state);process.exitCode=2;}
}catch(e){state.failure=String(e);state.memory=memory();write(checkpoint,state);console.log(JSON.stringify({event:'failure',failure:state.failure,memory:state.memory}));process.exitCode=1;}
