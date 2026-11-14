// Actual rerun after the old executor's unpushed files were lost.
// Same physical family and split-RK4 cell equation. Every accepted cell is
// saved; no beta is reconstructed from remembered terminal output.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import v8 from 'node:v8';
import {createRecalibrationFactory,sampleTailGeometry} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {loadClosingTailSource} from './closing_tail_sources.mjs';
const {splitIntegrationInterval}=await loadClosingTailSource('f6tail_cusp_grid.mjs');
const [input,out,stepsArg='128',maxArg='6',resumeArg='']=process.argv.slice(2);
if(!input||!out)throw Error('input.json output-prefix [steps] [maxOuter] [--resume]');
const steps=Number(stepsArg),maxOuter=Number(maxArg),resume=resumeArg==='--resume';
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const cfg=JSON.parse(fs.readFileSync(input,'utf8')),sourceSha=hash(new URL(import.meta.url)),inputSha=hash(input),N=cfg.protectCell;
const checkpoint=out+'-checkpoint.json',journal=out+'-cells.jsonl';
if(!resume&&(fs.existsSync(checkpoint)||fs.existsSync(journal)))throw Error('unused output prefix required');
const started=Date.now(),factory=createRecalibrationFactory(cfg),marked=new WeakSet();
const memory=()=>({...process.memoryUsage(),heap_size_limit:v8.getHeapStatistics().heap_size_limit});
const write=(f,x)=>{fs.writeFileSync(f+'.tmp',JSON.stringify(x,null,2)+'\n');fs.renameSync(f+'.tmp',f);};
function entry(n,beta){const row=factory.getEntries(n,beta);if(!marked.has(row)){
 boundTailPointCaches({getEntries:()=>row,parameters:factory.parameters},{protectCell:1,valleyControls:[beta]},{pointsPerEntry:8});marked.add(row);}return row;}
function physicalCell(n,beta,r,alpha){entry(n,beta);return factory.physicalCell(n,beta,r,alpha);}
function column(cell,ns){let y=[1,0];const lm=Math.log(cell.mu),s=Math.sqrt(12);
 const rhs=(u,g)=>{const lr=Math.log(g.r);return [s*g.drdx*Math.exp(lm-8*lr-g.logw)*u[1],-s*g.drdx*Math.exp(6*lr+g.logw-lm)*u[0]];};
 for(const profile of cell.profiles)for(let i=0;i<ns;i++){
  const xs=splitIntegrationInterval(i/ns,(i+1)/ns,profile.integrationBreakpoints??[]);
  for(let k=0;k<xs.length-1;k++){
   const x=xs[k],h=xs[k+1]-x,g0=profile(x),gm=profile(x+h/2),g1=profile(x+h),
    a=rhs(y,g0),b=rhs([y[0]+h*a[0]/2,y[1]+h*a[1]/2],gm),
    c=rhs([y[0]+h*b[0]/2,y[1]+h*b[1]/2],gm),d=rhs([y[0]+h*c[0],y[1]+h*c[1]],g1);
   y=[y[0]+h*(a[0]+2*b[0]+2*c[0]+d[0])/6,y[1]+h*(a[1]+2*b[1]+2*c[1]+d[1])/6];
   if(!y.every(Number.isFinite))throw Error('nonfinite cell column');
  }
 }
 return {column:y,gain:y[0],residual:y[1]/Math.max(1,Math.abs(y[0]))};
}
function solve(n,r,alpha,guess,ns){const trace=[],tol=2e-8;
 const evaluate=beta=>{const cell=physicalCell(n,beta,r,alpha),v=column(cell,ns);trace.push({beta,gain:v.gain,residual:v.residual});return {beta,cell,...v};};
 let best=evaluate(guess);if(Math.abs(best.residual)<=tol)return {...best,trace};
 let lo=best,hi=best,width=.1;
 for(let i=0;i<12&&lo.column[1]*hi.column[1]>=0;i++){
  lo=evaluate(guess-width);hi=evaluate(guess+width);width*=1.8;
  if(Math.abs(lo.residual)<Math.abs(best.residual))best=lo;if(Math.abs(hi.residual)<Math.abs(best.residual))best=hi;
  if(Math.abs(best.residual)<=tol)return {...best,trace};
 }
 if(lo.column[1]*hi.column[1]>=0)throw Object.assign(Error('no physical T21 bracket'),{trace,cell:n});
 let fl=lo.column[1],fh=hi.column[1],side=0;
 for(let i=0;i<72;i++){
  const span=hi.beta-lo.beta;let beta=(lo.beta*fh-hi.beta*fl)/(fh-fl);
  if(!(beta>lo.beta&&beta<hi.beta)||i%9===8)beta=(lo.beta+hi.beta)/2;
  const z=evaluate(beta);if(Math.abs(z.residual)<Math.abs(best.residual))best=z;
  if(Math.abs(best.residual)<=tol)return {...best,trace};
  if(span<2e-13)throw Object.assign(Error('root roundoff before tolerance'),{trace,cell:n});
  if(lo.column[1]*z.column[1]<=0){hi=z;fh=z.column[1];fl=side===-1?fl*.5:lo.column[1];side=-1;}
  else{lo=z;fl=z.column[1];fh=side===1?fh*.5:hi.column[1];side=1;}
 }
 throw Object.assign(Error('physical T21 iteration limit'),{trace,cell:n});
}
let state;
if(resume){state=JSON.parse(fs.readFileSync(checkpoint,'utf8'));if(state.source_sha256!==sourceSha||state.input_sha256!==inputSha||state.steps!==steps||state.completed)throw Error('invalid resume binding');}
else{
 for(let n=0;n<N;n++)entry(n,cfg.valleyControls?.[n]??0);
 let initial=factory.assemble();const baseline=initial.stats;initial=null;
 const raw=factory.source.cells[N-1].profiles[2](.5),cap=entry(N-1,0).entries[2].profileSource(.5),guess=2*Math.log(baseline.alpha)+cap.logw-raw.logw;
 state={schema:'fd2d-recovered-layered-physical-calibration-v1',source_sha256:sourceSha,input_file:path.basename(input),input_sha256:inputSha,
  scope:'New actual finite rerun after executor change. T21 is solved in each true physical warped cell. Root iteration tolerance and quadrature are finite, not interval-certified. No nonlinear solution or completed strong target is claimed.',
  base_constructor_sha256:hash(new URL('./closing_recalibrated_tail.mjs',import.meta.url)),weighted_constructor_sha256:hash(new URL('./closing_weighted_tail.mjs',import.meta.url)),
  bounded_cache_sha256:hash(new URL('./fd2d-bounded-tail-point-cache.mjs',import.meta.url)),
  steps,deep_steps:'n>=60: min(steps,32); n>=24: min(steps,64)',root_tolerance:2e-8,
  controls:Array.from({length:N},(_,n)=>cfg.valleyControls?.[n]??0),baseline,outer:0,alpha:baseline.alpha,
  next_cell:N-1,r:factory.deepSource.r,last_beta:guess,beta_predictor_shift:0,current_rows:[],history:[],completed:false,memory:memory()};write(checkpoint,state);
}
console.log(JSON.stringify({event:resume?'resume':'start',outer:state.outer,next_cell:state.next_cell,baseline:state.baseline,memory:memory()}));
try{
 while(state.outer<maxOuter){
  for(let n=state.next_cell;n>=0;n--){
   const ns=n>=60?Math.min(steps,32):n>=24?Math.min(steps,64):steps,
    guess=state.outer===0?state.last_beta:state.controls[n]+state.beta_predictor_shift,began=Date.now(),z=solve(n,state.r,state.alpha,guess,ns),
    row={outer:state.outer,cell:n,steps:ns,beta:z.beta,gain_Q:z.gain,gain_height:z.gain*(z.cell.rEnd/z.cell.rStart)**4,
     residual:z.residual,rStart:z.cell.rStart,rEnd:z.cell.rEnd,localWidth:z.cell.localWidth,meridianLength:z.cell.meridianLength,heightSpan:z.cell.heightSpan,
     evaluations:z.trace.length,seconds:(Date.now()-began)/1000};
   state.controls[n]=z.beta;state.r=z.cell.rEnd;state.last_beta=z.beta;state.next_cell=n-1;state.current_rows.push(row);state.memory=memory();
   fs.appendFileSync(journal,JSON.stringify({...row,trace:z.trace,memory:state.memory})+'\n');write(checkpoint,state);
   if(n%8===0||n===N-1)console.log(JSON.stringify({event:'cell',...row,memory:state.memory}));
   if(n%4===0&&typeof global.gc==='function')global.gc();
  }
  for(let n=0;n<N;n++)entry(n,state.controls[n]);
  let tail=factory.assemble(state.controls,state.alpha);const next=factory.assemble(state.controls),newAlpha=next.stats.alpha,
   h={outer:state.outer,alpha:state.alpha,next_alpha:newAlpha,stats:tail.stats,cells:state.current_rows.length,
    min_abs_gain:Math.min(...state.current_rows.map(r=>Math.abs(r.gain_Q))),max_abs_gain:Math.max(...state.current_rows.map(r=>Math.abs(r.gain_Q))),
    max_abs_root_residual:Math.max(...state.current_rows.map(r=>Math.abs(r.residual)))};
  state.history.push(h);console.log(JSON.stringify({event:'outer',...h,memory:memory()}));
  if(Math.abs(tail.stats.cutRadiusError)<2e-10){
   const final={...cfg,valleyControls:state.controls,calibration_status:'Recovered finite actual physical m2 calibration; new nonlinear DN and continuous checks required',
    design_calibration:{source_sha256:sourceSha,report:path.basename(checkpoint),steps,alpha_at_cell_roots:state.alpha,assembled_alpha:newAlpha,
     cut_radius_error:tail.stats.cutRadiusError,finite_root_residual:h.max_abs_root_residual}};
   write(out+'-config.json',final);state.completed=true;state.stats=tail.stats;state.geometry=sampleTailGeometry(tail,64);
   state.final_config_file=path.basename(out+'-config.json');state.final_config_sha256=hash(out+'-config.json');state.memory=memory();state.seconds=(Date.now()-started)/1000;
   write(checkpoint,state);console.log(JSON.stringify({event:'complete',stats:state.stats,geometry:state.geometry,sha256:state.final_config_sha256,memory:state.memory}));break;
  }
  // This is only a starting guess for the next actual root. It is not an
  // imposed physical identity: each cell still recomputes its true T21.
  state.beta_predictor_shift=2*Math.log(newAlpha/state.alpha);
  state.outer++;state.alpha=newAlpha;state.next_cell=N-1;state.r=factory.deepSource.r;state.current_rows=[];tail=null;write(checkpoint,state);
  if(typeof global.gc==='function')global.gc();
 }
 if(!state.completed){state.stop_reason='finite outer limit';write(checkpoint,state);console.log(JSON.stringify({event:'outer_limit',outer:state.outer}));}
}catch(error){state.failure={message:String(error),trace:error.trace??null,cell:error.cell??state.next_cell};state.memory=memory();write(checkpoint,state);console.log(JSON.stringify({event:'failure',...state.failure,memory:state.memory}));process.exitCode=1;}
