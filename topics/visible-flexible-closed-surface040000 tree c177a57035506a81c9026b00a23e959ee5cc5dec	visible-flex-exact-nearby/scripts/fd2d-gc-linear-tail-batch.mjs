// Actual finite linear momentum graph on one frozen physical tail.
// Used only to initialize a nonlinear GC BVP. This is not a nonlinear DN.
// Geometry is evaluated once per RK point, shared by independent modes.
import fs from 'node:fs';
import crypto from 'node:crypto';
import {createRecalibrationFactory,idealModeGraph} from './closing_weighted_tail.mjs';
import {loadClosingTailSource} from './closing_tail_sources.mjs';
const {splitIntegrationInterval}=await loadClosingTailSource('f6tail_cusp_grid.mjs');
const [configFile,outFile,modesArg='95',stepsArg='256',farArg='48']=process.argv.slice(2);
if(!configFile||!outFile)throw Error('config, output, [mode count], [steps], [far] required');
if(fs.existsSync(outFile))throw Error('Use an unused linear report filename');
const config=JSON.parse(fs.readFileSync(configFile,'utf8'));
const modes=Number(modesArg),steps=Number(stepsArg),far=Number(farArg),spacing=config.spacing??2;
const start=Date.now(),tail=createRecalibrationFactory(config).assemble();
const root12=Math.sqrt(12),frequency=Float64Array.from({length:modes},(_,j)=>spacing*(j+1));
const nu=Float64Array.from(frequency,m=>m*m*(m*m-1)/12);
let q=new Float64Array(modes).fill(1),p=Float64Array.from(frequency,m=>tail.parameters.orientation*idealModeGraph(m,tail.parameters.R,tail.parameters.a));
const logs=new Float64Array(modes),cut=tail.cells[0].profiles.at(-1)(1),r=cut.r,w=Math.exp(cut.logw);
const report={schema:'fd2d-finite-linear-tail-batch-v1',
 scope:'Selected finite-depth linear graph for an initializer. No nonlinear boundary response or infinite-tail assertion.',
 source_sha256:crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex'),
 config,config_sha256:crypto.createHash('sha256').update(fs.readFileSync(configFile)).digest('hex'),
 modes,spacing,steps,far,stats:tail.stats,cut:{r,w,wr:w*cut.dlogwdx/cut.drdx,E:1+w*w},
 completed:false,completed_cells:[],rows:[]};
let lastMu=tail.cells[far-1].mu,points=0;
function normalize(j){const norm=Math.hypot(q[j],p[j]);if(!(norm>0&&Number.isFinite(norm)))throw Error('nonfinite linear mode '+frequency[j]);q[j]/=norm;p[j]/=norm;logs[j]+=Math.log(norm);}
for(let j=0;j<modes;j++)normalize(j);
function scalarGeometry(g,logMu){const lr=Math.log(g.r);return [root12*g.drdx*Math.exp(logMu-8*lr-g.logw),-root12*g.drdx*Math.exp(6*lr+g.logw-logMu),g.drdx/g.r];}
function advance(h,g0,gm,g1){
 for(let j=0;j<modes;j++){
  const v=q[j],z=p[j],d=frequency[j]*frequency[j]-4,b=nu[j];
  const a0=d*g0[2]*v+g0[0]*z,a1=b*g0[1]*v-d*g0[2]*z;
  const v1=v+h*a0/2,z1=z+h*a1/2;
  const b0=d*gm[2]*v1+gm[0]*z1,b1=b*gm[1]*v1-d*gm[2]*z1;
  const v2=v+h*b0/2,z2=z+h*b1/2;
  const c0=d*gm[2]*v2+gm[0]*z2,c1=b*gm[1]*v2-d*gm[2]*z2;
  const v3=v+h*c0,z3=z+h*c1;
  const d0=d*g1[2]*v3+g1[0]*z3,d1=b*g1[1]*v3-d*g1[2]*z3;
  q[j]=v+h*(a0+2*b0+2*c0+d0)/6;p[j]=z+h*(a1+2*b1+2*c1+d1)/6;normalize(j);
 }
}
try{
 for(let n=far-1;n>=0;n--){
  const cell=tail.cells[n],logMu=Math.log(cell.mu);
  for(let j=0;j<modes;j++){p[j]*=lastMu/cell.mu;normalize(j);}lastMu=cell.mu;
  for(const profile of cell.profiles)for(let k=0;k<steps;k++){
   const pieces=splitIntegrationInterval(k/steps,(k+1)/steps,profile.integrationBreakpoints??[]);
   for(let j=0;j<pieces.length-1;j++){
    const x=pieces[j],h=pieces[j+1]-x;
    advance(h,scalarGeometry(profile(x),logMu),scalarGeometry(profile(x+h/2),logMu),scalarGeometry(profile(x+h),logMu));points+=3;
   }
  }
  report.completed_cells.push(n);report.seconds=(Date.now()-start)/1000;
  report.recovery={next_cell:n-1,q:Array.from(q),p:Array.from(p),logs:Array.from(logs),last_mu:lastMu};
  fs.writeFileSync(outFile,JSON.stringify(report,null,2)+'\n');
  if(n%8===0||n===far-1)console.log(JSON.stringify({event:'linear_cell',cell:n,seconds:report.seconds,points,modes}));
 }
 for(let j=0;j<modes;j++)report.rows.push({mode:frequency[j],slope:frequency[j]**2/r+root12*tail.cells[0].mu*p[j]/(r**8*w*q[j]),logHeightGain:logs[j]+Math.log(Math.abs(q[j]))+4*Math.log(r)});
 report.completed=true;
}catch(error){report.failure=String(error);process.exitCode=2;}
report.seconds=(Date.now()-start)/1000;report.geometry_evaluations=points;
fs.writeFileSync(outFile,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({event:'complete',completed:report.completed,rows:report.rows.length,seconds:report.seconds,failure:report.failure,first:report.rows[0],last:report.rows.at(-1)}));
