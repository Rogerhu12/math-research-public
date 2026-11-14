import fs from 'node:fs/promises';
import {createRecalibrationFactory,physicalM2Column} from './closing_recalibrated_tail.mjs';
const input=process.argv[2],output=process.argv[3],steps=+(process.argv[4]??128),pulse=+(process.argv[5]??0);
if(!input||!output)throw Error('Usage: config.json output.json [steps] [pulse]');
const config=JSON.parse(await fs.readFile(input,'utf8')),rows=[];
for(const peak of [.02,.04,.08,.16,.24,.32,.4,.5,.65,.8,1.1,1.6]){
 const c={...config,protectCell:160,capMode:'cut-preserving',pulseCaps:[[pulse===0?peak:config.slopeCap,pulse===1?peak:config.slopeCap]]};
 let row;
 try{
  const factory=createRecalibrationFactory(c),controls=Array.from({length:160},(_,n)=>c.valleyControls?.[n]??2*Math.log(72.04)),samples=[];
  const evaluate=beta=>{controls[0]=beta;const tail=factory.assemble(controls),z=physicalM2Column(tail.cells[0],steps);return {beta,...z,stats:tail.stats};};
  let lo=evaluate(-10),hi=evaluate(16);samples.push(lo,hi);
  if(lo.column[1]*hi.column[1]>=0){row={peak,error:'No sign bracket [-10,16]',samples};}
  else{
   let best=lo;
   for(let it=0;it<42;it++){const beta=(lo.beta+hi.beta)/2,z=evaluate(beta);samples.push(z);best=z;if(Math.abs(z.zeroResidual)<1e-8)break;if(lo.column[1]*z.column[1]<=0)hi=z;else lo=z;}
   row={peak,calibrated:Math.abs(best.zeroResidual)<1e-7,beta:best.beta,gain:best.gain,residual:best.zeroResidual,stats:best.stats,sampleCount:samples.length,config:{...c,valleyControls:Array.from(controls)}};
  }
 }catch(e){row={peak,error:e.message};}
 rows.push(row);console.log(JSON.stringify({...row,config:undefined,samples:row.samples?.map(z=>({beta:z.beta,gain:z.gain,residual:z.zeroResidual}))}));
 await fs.writeFile(output,JSON.stringify({scope:'Changed finite metric: asymmetric first/second shallow pulse cap. Single-cell physical calibration with actual total width. No nonlinear claim.',input,steps,pulse,rows},null,2)+'\n');
}
