// Stable momentum-coordinate finite-tail DN, no large state arrays in output.
// This only computes a selected linear deep line; it is not nonlinear closure.
import fs from 'node:fs';
import crypto from 'node:crypto';
import {createRecalibrationFactory,idealModeGraph} from './closing_weighted_tail.mjs';
import {loadClosingTailSource} from './closing_tail_sources.mjs';
const {splitIntegrationInterval}=await loadClosingTailSource('f6tail_cusp_grid.mjs');
function physicalModeColumn(cell,mode,steps,initial){
 let y=initial.slice();const logMu=Math.log(cell.mu),nu=mode*mode*(mode*mode-1)/12,root12=Math.sqrt(12);
 function rhs(v,g){const lr=Math.log(g.r),a=root12*g.drdx*Math.exp(logMu-8*lr-g.logw),b=-nu*root12*g.drdx*Math.exp(6*lr+g.logw-logMu),d=(mode*mode-4)*g.drdx/g.r;return [d*v[0]+a*v[1],b*v[0]-d*v[1]];}
 for(const profile of cell.profiles)for(let k=0;k<steps;k++){
  const pieces=splitIntegrationInterval(k/steps,(k+1)/steps,profile.integrationBreakpoints??[]);
  for(let j=0;j<pieces.length-1;j++){
   const x=pieces[j],h=pieces[j+1]-x,g0=profile(x),gm=profile(x+h/2),g1=profile(x+h),a=rhs(y,g0),b=rhs([y[0]+h*a[0]/2,y[1]+h*a[1]/2],gm),c=rhs([y[0]+h*b[0]/2,y[1]+h*b[1]/2],gm),d=rhs([y[0]+h*c[0],y[1]+h*c[1]],g1);
   y=[y[0]+h*(a[0]+2*b[0]+2*c[0]+d[0])/6,y[1]+h*(a[1]+2*b[1]+2*c[1]+d[1])/6];
   if(!y.every(Number.isFinite))throw Error('nonfinite momentum mode '+mode);
  }
 }return {column:y};
}
const [configFile,outFile,modesArg='16',stepsArg='256',farArg='48']=process.argv.slice(2);
const config=JSON.parse(fs.readFileSync(configFile,'utf8'));
const modes=Number(modesArg),steps=Number(stepsArg),far=Number(farArg);
const start=Date.now(),tail=createRecalibrationFactory(config).assemble(),spacing=config.spacing??3;
const out={method:'cusp-split RK4 momentum',source_sha256:crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex'),scope:'Finite linear momentum transfer on frozen physical weighted metric; no nonlinear or infinite-tail assertion.',config,config_sha256:crypto.createHash('sha256').update(fs.readFileSync(configFile)).digest('hex'),stats:tail.stats,modes,spacing,steps,far,rows:[]};
const cut=tail.cells[0].profiles.at(-1)(1),r=cut.r,w=Math.exp(cut.logw);
out.cut={r,w,wr:w*cut.dlogwdx/cut.drdx,E:1+w*w,Ep:2*w*w*cut.dlogwdx/cut.drdx};
for(let j=1;j<=modes;j++){
 const mode=spacing*j;
 let y=[1,tail.parameters.orientation*idealModeGraph(mode,tail.parameters.R,tail.parameters.a)],ln=0,lastMu=tail.cells[far-1].mu;
 for(let n=far-1;n>=0;n--){
  const cell=tail.cells[n];y[1]*=lastMu/cell.mu;lastMu=cell.mu;
  const z=physicalModeColumn(cell,mode,steps,y),norm=Math.hypot(...z.column);
  y=z.column.map(v=>v/norm);ln+=Math.log(norm);
 }
 const slope=mode*mode/r+Math.sqrt(12)*tail.cells[0].mu*y[1]/(r**8*w*y[0]);
 out.rows.push({mode,slope,logHeightGain:ln+Math.log(Math.abs(y[0]))+4*Math.log(r)});
 out.seconds=(Date.now()-start)/1000;
 fs.writeFileSync(outFile,JSON.stringify(out,null,2)+'\n');
 console.log(JSON.stringify(out.rows.at(-1)));
}
