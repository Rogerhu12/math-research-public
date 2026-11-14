// Stable momentum-coordinate finite-tail DN, no large state arrays in output.
// This only computes a selected linear deep line; it is not nonlinear closure.
import fs from 'node:fs';
import crypto from 'node:crypto';
import {createRecalibrationFactory,physicalModeColumn,idealModeGraph} from './closing_weighted_tail.mjs';
const [configFile,outFile,modesArg='16',stepsArg='256',farArg='48']=process.argv.slice(2);
const config=JSON.parse(fs.readFileSync(configFile,'utf8'));
const modes=Number(modesArg),steps=Number(stepsArg),far=Number(farArg);
const start=Date.now(),tail=createRecalibrationFactory(config).assemble(),spacing=config.spacing??3;
const out={scope:'Finite linear momentum transfer on frozen physical weighted metric; no nonlinear or infinite-tail assertion.',config,config_sha256:crypto.createHash('sha256').update(fs.readFileSync(configFile)).digest('hex'),stats:tail.stats,modes,spacing,steps,far,rows:[]};
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
