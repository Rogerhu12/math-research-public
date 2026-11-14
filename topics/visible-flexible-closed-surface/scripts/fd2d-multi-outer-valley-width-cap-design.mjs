// Recalibrate exactly the first N physical cells after assigning more free
// width to their valleys. The old inner free-warp scale and deeper input are
// retained; the outer radius is a solved design output, not an imposed .5.
// Finite actual equations only, with bounded point memoization.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import v8 from 'node:v8';
import {createRecalibrationFactory,solvePhysicalCell} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
const [input,portFile,out,activeArg='2',weightArg='12',stepsArg='256']=process.argv.slice(2);
if(!input||!portFile||!out)throw Error('base-config actual-port unused-output-prefix [activeCells] [valleyWeight] [steps]');
const N=Number(activeArg),W=Number(weightArg),steps=Number(stepsArg);
if(!Number.isInteger(N)||N<1||N>12||!(W>=1&&W<=10000))throw Error('finite design range');
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const cfg=JSON.parse(fs.readFileSync(input,'utf8')),port=JSON.parse(fs.readFileSync(portFile,'utf8'));
if(!port.completed||port.config_sha256!==hash(input)||port.far<cfg.protectCell)throw Error('actual full-depth base port required');
const checkpoint=out+'-checkpoint.json';if(fs.existsSync(checkpoint))throw Error('unused output prefix');
const started=Date.now(),memory=()=>({...process.memoryUsage(),heap_size_limit:v8.getHeapStatistics().heap_size_limit});
const write=(f,d)=>{fs.writeFileSync(f+'.tmp',JSON.stringify(d,null,2)+'\n');fs.renameSync(f+'.tmp',f);};
let base=createRecalibrationFactory(cfg);boundTailPointCaches(base,cfg,{pointsPerEntry:8});let old=base.assemble();
const targetLambda=old.stats.alpha,innerRadius=old.cells[N-1].rStart,cuff=old.stats.rCuff;
let rc=cfg.rCut,controls=cfg.valleyControls.slice();
let state={schema:'fd2d-multi-outer-valley-width-and-cap-design-v1',
 source_sha256:hash(new URL(import.meta.url)),base_config_file:path.basename(input),base_config_sha256:hash(input),
 base_port_file:path.basename(portFile),base_port_sha256:hash(portFile),active_cells:N,valley_weight:W,valley_cap_scale:W,steps,
 target_inner_lambda:targetLambda,unchanged_inner_radius:innerRadius,rows:[],completed:false,
 scope:'New physical g. First N beta controls, valley caps and free-warp weights are redesigned. Outer cut is selected to retain the previous inner lambda. Actual assemble and full-depth bounded-line/DN recomputation remain required. No exact finite T21, nonlinear or continuous reach claim.',
 memory:memory()};write(checkpoint,state);
old=null;base=null;if(typeof global.gc==='function')global.gc();
try{
 for(let outer=0;outer<8;outer++){
  const design={...cfg,rCut:rc,width:rc-cuff,
   valleyCaps:cfg.valleyCaps.map((v,n)=>n<N?W*v:v),
   warpWeightLevels:Array.from({length:cfg.protectCell},(_,n)=>n<N?[1,1,W,1,1]:[1,1,1,1,1])};
  let factory=createRecalibrationFactory(design);
  const originalGet=factory.getEntries,seen=new WeakSet();
  const touch=(n,b)=>{const row=originalGet(n,b);if(!seen.has(row)){
   boundTailPointCaches({getEntries:()=>row,parameters:factory.parameters},{protectCell:1,valleyControls:[b]},{pointsPerEntry:8});seen.add(row);}return row;};
  const originalPhysical=factory.physicalCell;
  factory.physicalCell=(n,b,r,l)=>{touch(n,b);return originalPhysical(n,b,r,l);};
  let radius=innerRadius,pass=[];
  for(let n=N-1;n>=0;n--){
   const guess=controls[n]+(outer===0?Math.log(W):0);
   const solved=solvePhysicalCell(factory,n,radius,targetLambda,{steps,tolerance:1e-8,initialBeta:guess,limit:72});
   controls[n]=solved.beta;
   const row={outer,cell:n,rStart:radius,rEnd:solved.cell.rEnd,beta:solved.beta,gain_Q:solved.gain,
    momentum_residual:solved.zeroResidual,root_trace:solved.trace};
   radius=solved.cell.rEnd;pass.push(row);state.rows.push(row);state.current={outer,next_cell:n-1,radius,controls};
   state.memory=memory();state.seconds=(Date.now()-started)/1000;write(checkpoint,state);
   console.log(JSON.stringify({event:'cell',...Object.fromEntries(Object.entries(row).filter(([k])=>k!=='root_trace')),evaluations:solved.trace.length,memory:state.memory}));
  }
  const residual=radius-rc;
  state.last_radius_residual=residual;
  console.log(JSON.stringify({event:'outer',outer,requested_cut:rc,actual_cut:radius,radius_residual:residual}));
  if(Math.abs(residual)<2e-10){
   design.valleyControls=controls.slice();
   design.historical_calibration_only=design.design_calibration;delete design.design_calibration;
   design.calibration_status='New finite physical weighted-valley design; actual N-cell roots and radius closure only. No nonlinear or interval claim.';
   design.outer_width_design={source_sha256:state.source_sha256,base_config_file:path.basename(input),base_config_sha256:hash(input),
    target_inner_lambda:targetLambda,root_report:path.basename(checkpoint),active_cells:N,valley_weight:W,valley_cap_scale:W,
    finite_radius_residual:residual,maximum_finite_momentum_residual:Math.max(...pass.map(x=>Math.abs(x.momentum_residual))),
    physical_cuff_definition:'rCuff=8/25; binary factory subtraction is its finite evaluation',deep_source_unchanged_from_cell:160};
   for(let n=0;n<cfg.protectCell;n++)touch(n,controls[n]);
   const tail=factory.assemble(controls);
   state.final_stats=tail.stats;state.final_cut=rc;state.final_controls=controls;
   write(out+'-config.json',design);state.final_config_file=path.basename(out+'-config.json');state.final_config_sha256=hash(out+'-config.json');
   state.completed=true;state.seconds=(Date.now()-started)/1000;state.memory=memory();write(checkpoint,state);
   console.log(JSON.stringify({event:'complete',rCut:rc,width:design.width,lambda:tail.stats.alpha,minimumWarpWidth:tail.stats.minimumWarpWidth,
     meridianLength:tail.stats.meridianLength,heightSpan:tail.stats.heightSpan,sha256:state.final_config_sha256,seconds:state.seconds,memory:state.memory}));break;
  }
  rc=radius;factory=null;if(typeof global.gc==='function')global.gc();
 }
 if(!state.completed){state.stop_reason='outer radius iteration limit';write(checkpoint,state);process.exitCode=2;}
}catch(e){state.failure=String(e);state.memory=memory();write(checkpoint,state);console.log(JSON.stringify({event:'failure',failure:state.failure,memory:state.memory}));process.exitCode=1;}
