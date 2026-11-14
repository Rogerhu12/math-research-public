// Projective physical-height integration for the newly capped actual metric.
// Linear diagnostics only; finite far condition, no nonlinear existence claim.
import fs from 'node:fs/promises';
import {createCutPreservingTail} from './root_cut_preserving_tail.mjs';
const input=process.argv[2],output=process.argv[3];
if(!input||!output)throw Error('Arguments: config.json output.json [modes] [steps] [far]');
const config=JSON.parse(await fs.readFile(input,'utf8')),
  count=+(process.argv[4]??4),steps=+(process.argv[5]??512),far=+(process.argv[6]??32),
  tail=createCutPreservingTail(config),rows=[];
function idealGraph(m,R,a){if(m===2)return 0;const nu=m*m*(m*m-1)/12,rho=2**a,
  alpha=1+1/R,a00=1-alpha*nu*R,a10=(-nu*(1+R)+alpha*nu*nu*R)/rho,
  a11=(1-alpha*nu)/rho,tr=a00+a11,det=1/rho,
  lambda=.5*(tr-Math.sqrt(tr*tr-4*det));return a10/(lambda-a11);}
for(let index=1;index<=count;index++){
 const mode=2*index,scale=mode*mode/config.rCut,cell=tail.cells[far-1],gfar=cell.profiles[0](0),
       wfar=Math.exp(gfar.logw),z=idealGraph(mode,tail.parameters.R,tail.parameters.a),
       initialSlope=mode*mode/gfar.r+tail.parameters.orientation*Math.sqrt(12)*cell.mu*z/(gfar.r**8*wfar);
 let y=[1,initialSlope/scale],ln=Math.log(Math.hypot(...y));y=y.map(v=>v/Math.exp(ln));
 const records=[];
 function keep(n,j,x,g){if(mode===2)records.push([n,j,x,g.r,g.logw,g.dlogwdx/g.drdx,y[0],y[1],ln]);}
 function rhs(v,g){return [g.drdx*scale*v[1],-g.dlogwdx*(v[1]-mode*mode*v[0]/(g.r*scale))];}
 for(let n=far-1;n>=0;n--)for(let j=0;j<tail.cells[n].profiles.length;j++){
  const profile=tail.cells[n].profiles[j];keep(n,j,0,profile(0));
  for(let k=0;k<steps;k++){
   const x=k/steps,h=1/steps,g0=profile(x),gm=profile(x+h/2),g1=profile(x+h),
    a=rhs(y,g0),b=rhs(y.map((v,l)=>v+h*a[l]/2),gm),
    c=rhs(y.map((v,l)=>v+h*b[l]/2),gm),d=rhs(y.map((v,l)=>v+h*c[l]),g1);
   y=y.map((v,l)=>v+h*(a[l]+2*b[l]+2*c[l]+d[l])/6);
   const norm=Math.hypot(...y);if(!(norm>0&&Number.isFinite(norm)))throw Error('nonfinite propagation');
   y=y.map(v=>v/norm);ln+=Math.log(norm);keep(n,j,x+h,g1);
  }
 }
 const outerLog=ln+Math.log(Math.abs(y[0])),outerSign=Math.sign(y[0]),
  row={mode,far,steps,cutSlope:scale*y[1]/y[0],unitDirection:y,logHeightGain:outerLog};
 if(mode===2){
  let threshold=Infinity,where=null,maxHeight=0,maxDerivative=0;
  for(const [n,j,x,r,lw,lwr,a,b,l] of records){
   const w=Math.exp(lw),E=1+w*w,f=a*outerSign*Math.exp(l-outerLog),fr=scale*b*outerSign*Math.exp(l-outerLog),
     base=r*w/E,linear=r*fr/E-mode*mode*f,crit=linear===0?Infinity:base/Math.abs(linear);
   if(crit<threshold){threshold=crit;where={cell:n,segment:j,x,r,w,f,fr,baseT:base,linearT:linear};}
   maxHeight=Math.max(maxHeight,Math.abs(f));maxDerivative=Math.max(maxDerivative,Math.abs(fr));
  }
  row.linearTPositivityAmplitudeThreshold=threshold;
  row.thresholdLocation=where;row.normalizedHeightMax=maxHeight;row.normalizedDerivativeMax=maxDerivative;
  row.thresholdScope='Sampled sufficient bound for positivity of linearized H_theta_theta. Not a nonlinear amplitude bound or theorem.';
 }
 rows.push(row);console.log(JSON.stringify(row));
 await fs.writeFile(output,JSON.stringify({scope:'True finite-profile linear diagnostics, not nonlinear DN. Fixed selected ideal far condition must be refined.',config,stats:tail.stats,rows},null,2)+'\n');
}
