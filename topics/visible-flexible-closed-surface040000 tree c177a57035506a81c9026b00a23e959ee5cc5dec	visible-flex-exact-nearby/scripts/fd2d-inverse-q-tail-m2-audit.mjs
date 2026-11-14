// Complete inverse-Q changed tail, fixed-g m2 port with direct canonical-momentum recovery.
// Fork of the immutable layered-tail audit; only factory/identity and Gamma summaries differ.
// Raw states are spooled per cell rather than retained in a large JS array.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import readline from 'node:readline';
import {once} from 'node:events';
import {pipeline} from 'node:stream/promises';
import v8 from 'node:v8';
import {createRecalibrationFactory} from './fd2d-inverse-q-tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {loadClosingTailSource} from './closing_tail_sources.mjs';
const {splitIntegrationInterval}=await loadClosingTailSource('f6tail_cusp_grid.mjs');
const [configFile,out,spoolFile,stepsArg='256',resumeArg='']=process.argv.slice(2);
if(!configFile||!out||!spoolFile)throw Error('config output-prefix scratch-spool [steps] [--resume]');
const steps=Number(stepsArg),resume=resumeArg==='--resume',root12=Math.sqrt(12),began=Date.now();
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const sourceSha=hash(new URL(import.meta.url)),configSha=hash(configFile),cfg=JSON.parse(fs.readFileSync(configFile,'utf8'));
const file=out+'-checkpoint.json',memory=()=>({...process.memoryUsage(),heap_size_limit:v8.getHeapStatistics().heap_size_limit});
const write=(p,x)=>{fs.writeFileSync(p+'.tmp',JSON.stringify(x,null,2)+'\n');fs.renameSync(p+'.tmp',p);};
if(!resume&&(fs.existsSync(file)||fs.existsSync(spoolFile)))throw Error('unused output and spool required');
let factory=createRecalibrationFactory(cfg);boundTailPointCaches(factory,cfg,{pointsPerEntry:8});let tail=factory.assemble();
const N=tail.cells.length,cut=tail.cells[0].profiles.at(-1)(1);let state;
if(resume){state=JSON.parse(fs.readFileSync(file,'utf8'));if(state.source_sha256!==sourceSha||state.config_sha256!==configSha||state.steps!==steps||state.completed)throw Error('resume binding mismatch');fs.truncateSync(spoolFile,state.spool_bytes);}
else{fs.mkdirSync(path.dirname(spoolFile),{recursive:true});fs.writeFileSync(spoolFile,'');state={
 schema:'fd2d-inverse-q-full-tail-m2-momentum-audit-v1',source_sha256:sourceSha,config_file:path.basename(configFile),config_sha256:configSha,
 scope:'Actual fixed-g finite split-RK4 on all changed cells. Exact source m2 bounded inlet pi=0 is used at the unchanged deep port. No interior momentum is reset. Maxima are samples; no interval enclosure, nonlinear solution or strong-target completion is asserted.',
 base_constructor_sha256:hash(new URL('./closing_recalibrated_tail.mjs',import.meta.url)),weighted_constructor_sha256:hash(new URL('./closing_weighted_tail.mjs',import.meta.url)),
 cache_sha256:hash(new URL('./fd2d-bounded-tail-point-cache.mjs',import.meta.url)),
 inverse_q_source_files:tail.parameters.inverseQDefinition.sources,physical_definition_sha256:tail.parameters.inverseQDefinitionSHA256,
 steps,far:N,stats:tail.stats,
 next_cell:N-1,y:[1,0],lognorm:0,last_mu:tail.cells[N-1].mu,spool_bytes:0,cells:[],completed:false};write(file,state);}
console.log(JSON.stringify({event:resume?'resume':'start',next_cell:state.next_cell,stats:state.stats,memory:memory()}));
const fd=fs.openSync(spoolFile,'a');
try{
 for(let n=state.next_cell;n>=0;n--){
  const c=tail.cells[n],lm=Math.log(c.mu),ns=n>=60?Math.min(steps,32):n>=24?Math.min(steps,128):steps;
  let y=state.y.slice(),ln=state.lognorm,count=0;y[1]*=state.last_mu/c.mu;
  const normalize=()=>{const norm=Math.hypot(...y);if(!(norm>0&&Number.isFinite(norm)))throw Error('nonfinite momentum');y=y.map(v=>v/norm);ln+=Math.log(norm);};normalize();
  const rhs=(u,g)=>{const lr=Math.log(g.r);return [root12*g.drdx*Math.exp(lm-8*lr-g.logw)*u[1],-root12*g.drdx*Math.exp(6*lr+g.logw-lm)*u[0]];};
  const record=(j,x,g)=>{fs.writeSync(fd,JSON.stringify({cell:n,segment:j,x,r:g.r,logw:g.logw,wr:Math.exp(g.logw)*g.dlogwdx/g.drdx,logmu:lm,Q:y[0],Z:y[1],lognorm:ln})+'\n');count++;};
  for(let j=0;j<c.profiles.length;j++){
   const profile=c.profiles[j],stride=Math.max(1,Math.floor(ns/(n<12?32:16)));
   for(let k=0;k<ns;k++){
    const x=k/ns;if(k%stride===0)record(j,x,profile(x));
    const xs=splitIntegrationInterval(x,(k+1)/ns,profile.integrationBreakpoints??[]);
    for(let j=0;j<xs.length-1;j++){
     const a=xs[j],h=xs[j+1]-a,g0=profile(a),gm=profile(a+h/2),g1=profile(a+h),k0=rhs(y,g0),
      k1=rhs([y[0]+h*k0[0]/2,y[1]+h*k0[1]/2],gm),k2=rhs([y[0]+h*k1[0]/2,y[1]+h*k1[1]/2],gm),k3=rhs([y[0]+h*k2[0],y[1]+h*k2[1]],g1);
     y=[y[0]+h*(k0[0]+2*k1[0]+2*k2[0]+k3[0])/6,y[1]+h*(k0[1]+2*k1[1]+2*k2[1]+k3[1])/6];normalize();
    }
   }
   record(j,1,profile(1));
  }
  state.y=y;state.lognorm=ln;state.last_mu=c.mu;state.next_cell=n-1;state.spool_bytes=fs.fstatSync(fd).size;
  state.cells.push({cell:n,steps:ns,beta:c.beta,samples:count,exit_momentum_ratio:y[1]/y[0],log_abs_Q:ln+Math.log(Math.abs(y[0]))});state.memory=memory();write(file,state);
  if(n%16===0||n===N-1)console.log(JSON.stringify({event:'cell',cell:n,lognorm:ln,memory:state.memory}));
  if(n%4===0&&typeof global.gc==='function')global.gc();
 }
 fs.closeSync(fd);
 const [Q,Z]=state.y,cutLog=state.lognorm+Math.log(Math.abs(Q))+4*Math.log(cut.r),cutSign=Math.sign(Q),
  D=4/cut.r+root12*tail.cells[0].mu*Z/(cut.r**8*Math.exp(cut.logw)*Q);
 state.cut={r:cut.r,w:Math.exp(cut.logw),wr:Math.exp(cut.logw)*cut.dlogwdx/cut.drdx};state.linear_slopes={'2':D};state.cut_log_height_gain=cutLog;write(file,state);
 tail=null;factory=null;if(typeof global.gc==='function')global.gc();
 const signed=(v,l)=>v===0?0:Math.sign(v)*Math.exp(l+Math.log(Math.abs(v))),maxima={},cellMaxima={},
  keys=['H','Hr','P','L','eta','zeta','delta_n','delta_m','delta_l','Gamma','linear_shape_operator_row_bound'],
  trajectory=out+'-trajectory.jsonl.gz',raw=out+'-raw-momentum.jsonl.gz',gz=zlib.createGzip(),done=pipeline(gz,fs.createWriteStream(trajectory));
 let samples=0,minimumW=Infinity,maxCurvature=0;
 for await(const line of readline.createInterface({input:fs.createReadStream(spoolFile),crlfDelay:Infinity})){
  const q=JSON.parse(line),w=Math.exp(q.logw),lr=Math.log(q.r),lc=q.lognorm-cutLog,E=1+w*w,
   H=cutSign*signed(q.Q,lc+4*lr),J=cutSign*signed(q.Z,lc+Math.log(root12)+q.logmu-4*lr-q.logw),Hr=4*H/q.r+J,
   P=-cutSign*signed(q.Q,lc+Math.log(2)+3*lr-q.logw),L=cutSign*signed(q.Z,lc+Math.log(root12)+q.logmu-4*lr-2*q.logw),
   n0=w/(q.r*Math.sqrt(E)),l0=q.wr/E**1.5,eta=-E*L,zeta=Math.sqrt(E)*(3*P-2*L),dn=n0*eta,dm=n0*zeta,dl=-l0*eta,
   row={cell:q.cell,segment:q.segment,x:q.x,r:q.r,w,wr:q.wr,H,Hr,P,L,eta,zeta,delta_n:dn,delta_m:dm,delta_l:dl,
    Gamma:L-4*H*w/q.r,slope_remainder:J,reference_n:n0,reference_l:l0,linear_shape_operator_row_bound:Math.max(Math.abs(dl)+Math.abs(dm),Math.abs(dn)+Math.abs(dm))};
  if(Object.values(row).some(v=>!Number.isFinite(v)))throw Error('nonfinite recovered physical value');
  for(const k of keys)if(!maxima[k]||Math.abs(row[k])>Math.abs(maxima[k][k]))maxima[k]=row;
  const cm=cellMaxima[q.cell]??={cell:q.cell,II:0,Gamma:0,L:0,H:0,Hr:0};
  for(const [k,v] of [['II',row.linear_shape_operator_row_bound],['Gamma',row.Gamma],['L',L],['H',H],['Hr',Hr]])if(Math.abs(v)>cm[k]){cm[k]=Math.abs(v);if(k==='II'||k==='Gamma')cm[k+'Where']={segment:q.segment,x:q.x,r:q.r,w,H,Hr};}
  minimumW=Math.min(minimumW,w);maxCurvature=Math.max(maxCurvature,Math.abs(n0),Math.abs(l0));samples++;
  if(!gz.write(JSON.stringify(row)+'\n'))await once(gz,'drain');
 }
 gz.end();await done;await pipeline(fs.createReadStream(spoolFile),zlib.createGzip(),fs.createWriteStream(raw));
 const report={...state,completed:true,unit_cut_height:'real cosine Hcut=1 in H(r)cos(2u)',samples,maxima,cell_maxima:Object.values(cellMaxima),minimum_sampled_w:minimumW,
  maximum_sampled_background_curvature:maxCurvature,maximum_sampled_relative_II:Math.max(Math.abs(maxima.eta.eta),Math.abs(maxima.zeta.zeta)),
  trajectory:{file:path.basename(trajectory),bytes:fs.statSync(trajectory).size,sha256:hash(trajectory)},
  raw_momentum:{file:path.basename(raw),bytes:fs.statSync(raw).size,sha256:hash(raw)},seconds:(Date.now()-began)/1000,memory:memory(),nonlinear_solution:false};
 write(out+'-report.json',report);state.completed=true;state.report=path.basename(out+'-report.json');write(file,state);
 console.log(JSON.stringify({event:'complete',D2:D,maximum_relative_II:report.maximum_sampled_relative_II,maxH:maxima.H.H,maxHr:maxima.Hr.Hr,maxL:maxima.L.L,trajectory:report.trajectory,memory:report.memory}));
}catch(error){try{fs.closeSync(fd);}catch{}state.failure=String(error);state.memory=memory();write(file,state);console.log(JSON.stringify({event:'failure',message:String(error),memory:state.memory}));process.exitCode=1;}
