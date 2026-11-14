// Only rotational background geometry of the new finite tail is screened.
// No nonlinear PDE solution, full closed surface or reach is claimed.
import fs from 'node:fs/promises';
import {createCutPreservingTail} from './root_cut_preserving_tail.mjs';
const out=process.argv[2];if(!out)throw Error('Specify output JSON');
const rows=[];
for(const slopeCap of [.02,.05,.1]){
  const config={rCut:.6,wCut:.5,width:.35,curvatureBound:6,orientation:1,
    prefixR:2,prefixEnd:15,prefixReturnStart:8,protectCell:80,
    slopeCap,capTransition:2,calibrationSteps:512,warpSteps:16,
    cuspAwareQuadrature:true,quadratureTolerance:2e-10};
  const start=Date.now();let row;
  try{
    const tail=createCutPreservingTail(config);
    const samples={curvatureMax:0,azimuthalCurvatureMax:0,slopeMax:0,minRadialDerivative:Infinity};
    for(const cell of tail.cells)for(const profile of cell.profiles)for(let k=0;k<=64;k++){
      const g=profile(k/64),w=Math.exp(g.logw),wr=w*g.dlogwdx/g.drdx,
            kr=Math.abs(wr)/(1+w*w)**1.5,kt=w/(g.r*Math.sqrt(1+w*w));
      samples.curvatureMax=Math.max(samples.curvatureMax,kr);
      samples.azimuthalCurvatureMax=Math.max(samples.azimuthalCurvatureMax,kt);
      samples.slopeMax=Math.max(samples.slopeMax,w);
      samples.minRadialDerivative=Math.min(samples.minRadialDerivative,g.drdx);
    }
    row={config,success:true,stats:tail.stats,samples,seconds:(Date.now()-start)/1000};
  }catch(e){row={config,success:false,error:String(e),seconds:(Date.now()-start)/1000};}
  rows.push(row);console.log(JSON.stringify(row));
  await fs.writeFile(out,JSON.stringify({scope:'Background geometry only. No true DN, nonlinear matching, C2 closed flex or global reach certificate.',rows},null,2)+'\n');
}
