// Explicit finite block replacement. Cells n>=count are literally retained.
// The original nonlinear root, momentum flow and matching conventions are unchanged.
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!topic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC required');
const base=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const S=x=>x*x*x*(10+x*(-15+6*x));
const DS=x=>30*x*x*(1-x)*(1-x);
function critical(profile){
 const out=[];let x0=0,f0=profile(0).dlogwdx;
 for(let k=1;k<=256;k++){
  const x1=k/256,f1=profile(x1).dlogwdx;
  if(f0*f1<0){let lo=x0,hi=x1,fl=f0;for(let q=0;q<52;q++){const mid=(lo+hi)/2,fm=profile(mid).dlogwdx;if(fl*fm<=0)hi=mid;else{lo=mid;fl=fm;}}out.push((lo+hi)/2);}
  if(f1===0&&f0!==0&&x1<1)out.push(x1);x0=x1;f0=f1;
 }
 return out;
}
export function createRecalibrationFactory(config={}){
 const {outerCellDesign:design,...baseConfig}=config;
 if(!design||!Number.isInteger(design.count)||design.count<1)throw Error('Finite block count required');
 const originalFactory=base.createRecalibrationFactory(baseConfig);
 function assemble(){
  const old=originalFactory.assemble(),count=design.count,K=design.curvatureBound;
  if(count>=old.cells.length||!(K>0))throw Error('Invalid finite block');
  if(design.levels.length!==count||design.levels.some(v=>v.length!==5||v.some(w=>!(w>0))))throw Error('Five positive levels per cell required');
  for(let n=0;n<count-1;n++)if(design.levels[n][0]!==design.levels[n+1][4])throw Error('Adjacent prescribed levels differ');
  const fresh=base.createRecalibrationFactory(baseConfig),steps=fresh.parameters.warpSteps,rows=[],total=new Float64Array(6);
  // Exact physical jet evaluation without unnecessary nested radial quadrature.
  const oldRows=Array.from({length:count},(_,n)=>originalFactory.getEntries(n,baseConfig.valleyControls?.[n]??0));
  const oldJet=(n,j,x)=>{const e=oldRows[n].entries[j],g=e.profileSource(x),v=e.integrand(x);return{logw:g.logw,dlogwdx:g.dlogwdx,drdx:baseConfig.orientation*(v[0]+old.stats.alpha*v[1])};};
  const speedFloor=design.speedFloor??1e-10;
  for(let n=0;n<count;n++){
   const row=fresh.getEntries(n,baseConfig.valleyControls?.[n]??0),last=row.entries.length-1;
   if(last!==8)throw Error('Expected nine original source segments');
   row.total.fill(0);
   for(const e of row.entries){
    const j=e.j,underlying=e.profileSource,levels=design.levels[n];
    e.profileSource=x=>{
     const g=underlying(x);let logw,dlogwdx;
     if(j%2===0){logw=Math.log(levels[j/2]);dlogwdx=0;}
     else {const k=(j-1)/2,lo=Math.log(levels[k]),delta=Math.log(levels[k+1]/levels[k]);logw=lo+S(x)*delta;dlogwdx=DS(x)*delta;}
     if(n===count-1&&j===0){const z=oldJet(n,j,x),b=S(x),db=DS(x);dlogwdx=(1-b)*z.dlogwdx+db*(logw-z.logw);logw=(1-b)*z.logw+b*logw;}
     if(n===0&&j===last){const z=oldJet(n,j,x),b=S(1-x),db=-DS(1-x);dlogwdx=(1-b)*z.dlogwdx+db*(logw-z.logw);logw=(1-b)*z.logw+b*logw;}
     return {...g,logw,dlogwdx};
    };
    e.breakpoints=critical(e.profileSource);
    const weight=design.weights?.[n]?.[j]??1;
    if(!(weight>0))throw Error('Positive free-warp weights required');
    e.integrand=x=>{
     const g=e.profileSource(x),w=Math.exp(g.logw),root=Math.hypot(1,w);
     const minSpeed=Math.hypot(w*g.dlogwdx,speedFloor)/(K*root**3);
     let A=minSpeed,B=weight;
     if(n===count-1&&j===0){const b=S(x),z=oldJet(n,j,x),zw=Math.exp(z.logw),oldMin=Math.hypot(zw*z.dlogwdx,speedFloor)/(K*Math.hypot(1,zw)**3);if(Math.abs(z.drdx)<oldMin-1e-15)throw Error('Old inner port exceeds requested curvature');A=minSpeed+(1-b)*(Math.abs(z.drdx)-oldMin);B=b*weight;}
     if(n===0&&j===last){const b=S(1-x),z=oldJet(n,j,x),zw=Math.exp(z.logw),oldMin=Math.hypot(zw*z.dlogwdx,speedFloor)/(K*Math.hypot(1,zw)**3);if(Math.abs(z.drdx)<oldMin-1e-15)throw Error('Old outer port exceeds requested curvature');A=minSpeed+(1-b)*(Math.abs(z.drdx)-oldMin);B=b*weight;}
     return new Float64Array([A,B,root*A,root*B,w*A,w*B]);
    };
    e.total.fill(0);e.cumA.fill(0);e.cumB.fill(0);
    for(let k=0;k<steps;k++){const z=e.integrate(k/steps,(k+1)/steps);for(let q=0;q<6;q++)e.total[q]+=z[q];e.cumA[k+1]=e.total[0];e.cumB[k+1]=e.total[1];}
    for(let q=0;q<6;q++)row.total[q]+=e.total[q];
   }
   for(let q=0;q<6;q++)total[q]+=row.total[q];rows.push(row);
  }
  const rInner=old.cells[count-1].rStart,rOuter=old.cells[0].rEnd,target=baseConfig.orientation*(rOuter-rInner),alpha=(target-total[0])/total[1];
  if(!(alpha>0))throw Error('Finite block exceeds fixed width '+JSON.stringify({minimum:total[0],available:target,alpha}));
  const cells=old.cells.slice();let r=rInner;
  for(let n=count-1;n>=0;n--){cells[n]=fresh.physicalCell(n,baseConfig.valleyControls?.[n]??0,r,alpha);r=cells[n].rEnd;}
  const check=(n,j,x)=>{const a=old.cells[n].profiles[j](x),b=cells[n].profiles[j](x);return{r:b.r-a.r,w:Math.exp(b.logw)-Math.exp(a.logw),wr:Math.exp(b.logw)*b.dlogwdx/b.drdx-Math.exp(a.logw)*a.dlogwdx/a.drdx};};
  const ports=[check(count-1,0,0),check(0,8,1)];
  if(ports.some(v=>Math.max(...Object.values(v).map(Math.abs))>2e-11))throw Error('Physical outer/inner port two-jet mismatch');
  const joins=[];
  for(let n=0;n<count-1;n++){const a=cells[n].profiles[0](0),b=cells[n+1].profiles[8](1);joins.push({r:a.r-b.r,w:Math.exp(a.logw)-Math.exp(b.logw),wr:Math.exp(a.logw)*a.dlogwdx/a.drdx-Math.exp(b.logw)*b.dlogwdx/b.drdx});}
  if(joins.some(v=>Math.max(...Object.values(v).map(Math.abs))>2e-11))throw Error('New internal physical two-jet mismatch');
  const oldHeight=old.cells.slice(0,count).reduce((a,c)=>a+c.heightSpan,0),oldLength=old.cells.slice(0,count).reduce((a,c)=>a+c.meridianLength,0);
  return {...old,cells,parameters:{...old.parameters,constructor:'finite_block_tail_v1',outerCellDesign:design},stats:{...old.stats,heightSpan:old.stats.heightSpan-oldHeight+total[4]+alpha*total[5],meridianLength:old.stats.meridianLength-oldLength+total[2]+alpha*total[3],blockCount:count,blockAlpha:alpha,blockHeight:total[4]+alpha*total[5],blockMinimumWidth:total[0],blockWidth:target,blockPortDifferences:ports,blockInternalJoinDifferences:joins,unchangedPhysicalCellsFrom:count},sourceDefinition:'Named finite first-cell block replacement; original n>=count cells, normalization and deep source retained.'};
 }
 return {assemble};
}
