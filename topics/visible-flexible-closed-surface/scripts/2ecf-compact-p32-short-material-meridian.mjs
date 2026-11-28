#!/usr/bin/env node
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {compactCurvatureCover} from './2ecf-compact-p32-full-curvature.mjs';
function compactMeridianGap(z,dr=10,du=20){
 const n=2**dr,na=2**du;let lower=0,upper=0,count=0,eps=1e-13;const low=x=>x-eps*(1+Math.abs(x)),high=x=>x+eps*(1+Math.abs(x));
 for(let q=0;q<16;q++){let part=compactCurvatureCover(z,8,8,10.305,1,0,0,({angularPanel,radialNode,vector,norm})=>{
  let panels=Array.from({length:17},(_,i)=>angularPanel(Math.min(na-1,i*na/16),du)),lower=0,upper=0;
  for(let r=q*n/16;r<(q+1)*n/16;r++){let R=radialNode(r,dr),Q=0,E16=0;for(let i=0;i<17;i++){let [v]=vector(R.b,panels[i],[[1,0]]),e=norm(v);Q=low(Q+Math.max(0,e[0])*(i===0||i===16?2:4)/64);if(i===16)E16=e[1];}
  if(Q<=0)throw Error('Broad target derivative enclosure');lower=low(lower+low(Math.sqrt(Q))/n);upper=high(upper+high(Math.sqrt(E16))/n);}
  return [lower,upper];});lower=low(lower+part[0]);upper=high(upper+part[1]);count+=n/16;}
 return {radialCells:count,fullTargetAngles:64,exactRayAngle:'pi/2',targetLower:lower,rayUpper:upper,operatorErrorLower:low(1-high(upper/lower)**2)};
}
export {compactMeridianGap};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [state,d='12',a='20']=process.argv.slice(2),rd=Number(d),ad=Number(a);if(!Number.isInteger(rd)||rd<4||rd>16||!Number.isInteger(ad)||ad<4||ad>26)throw Error('Unsupported dyadic depth');
 const result=compactMeridianGap(JSON.parse(readFileSync(state)),rd,ad);
 console.log(JSON.stringify(result,null,2));if(!(result.operatorErrorLower>0))process.exitCode=1;
}
