// Finite changes to the original nine-segment cells and both original pulses.
// Only caps, valley controls, positive warp weights and the finite-block alpha change.
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!topic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC required');
const base=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const S=x=>x*x*x*(10+x*(-15+6*x));
const marked=Symbol('finite block port warp installed');
export function createRecalibrationFactory(config={}){
 const {outerCellDesign:design,...baseConfig}=config;
 if(!design||!Number.isInteger(design.count)||!(design.curvatureBound>=baseConfig.curvatureBound))throw Error('Finite pulse block count and curvature budget required');
 const count=design.count,originalFactory=base.createRecalibrationFactory(baseConfig);
 const old=originalFactory.assemble();
 const defaultPulseCaps=Array.from({length:count},(_,n)=>design.pulseCaps[n]??baseConfig.pulseCaps?.[n]);
 const valleyCaps=Array.from({length:count},(_,n)=>design.valleyCaps?.[n]??baseConfig.valleyCaps?.[n]??baseConfig.slopeCap);
 const defaultWeights=Array.from({length:count},(_,n)=>design.warpWeights?.[n]??baseConfig.warpWeightLevels?.[n]??[1,1,1,1,1]);
 let pulseCaps=defaultPulseCaps,weights=defaultWeights,fresh=base.createRecalibrationFactory({...baseConfig,curvatureBound:design.curvatureBound,pulseCaps,valleyCaps,warpWeightLevels:weights});
 const oldRows=Array.from({length:count},(_,n)=>originalFactory.getEntries(n,baseConfig.valleyControls?.[n]??0));
 const oldJet=(n,j,x)=>{const e=oldRows[n].entries[j],g=e.profileSource(x),v=e.integrand(x);return{logw:g.logw,dlogwdx:g.dlogwdx,drdx:baseConfig.orientation*(v[0]+old.stats.alpha*v[1])};};
 function rowFor(n,beta){
  const row=fresh.getEntries(n,beta);
  if(row[marked])return row;
  const steps=fresh.parameters.warpSteps,last=row.entries.length-1;
  row.total.fill(0);
  for(const e of row.entries){
   const j=e.j,sourceIntegrand=e.integrand;
   if((n===count-1&&j===0)||(n===0&&j===last)){
    e.integrand=x=>{
     const v=sourceIntegrand(x),g=e.profileSource(x),w=Math.exp(g.logw),root=Math.hypot(1,w),z=oldJet(n,j,x);
     // The port source height is unchanged. Convex blending of two admissible
     // radial speeds preserves the larger curvature budget and matches old jets.
     if(Math.max(Math.abs(g.logw-z.logw),Math.abs(g.dlogwdx-z.dlogwdx))>1e-10)throw Error('Finite block control alters protected port height profile');
     const b=n===count-1&&j===0?S(x):S(1-x),A=(1-b)*Math.abs(z.drdx)+b*v[0],B=b*v[1];
     return new Float64Array([A,B,root*A,root*B,w*A,w*B]);
    };
    e.total.fill(0);e.cumA.fill(0);e.cumB.fill(0);
    for(let k=0;k<steps;k++){const v=e.integrate(k/steps,(k+1)/steps);for(let q=0;q<6;q++)e.total[q]+=v[q];e.cumA[k+1]=e.total[0];e.cumB[k+1]=e.total[1];}
   }
   for(let q=0;q<6;q++)row.total[q]+=e.total[q];
  }
  row[marked]=true;return row;
 }
 function assemble(overrideControls=null,overrideCaps=null,overrideWeights=null){
  if((overrideCaps&&JSON.stringify(overrideCaps)!==JSON.stringify(pulseCaps))||(overrideWeights&&JSON.stringify(overrideWeights)!==JSON.stringify(weights))){if(overrideCaps)pulseCaps=overrideCaps.map(p=>Array.from(p));if(overrideWeights)weights=overrideWeights.map(p=>Array.from(p));fresh=base.createRecalibrationFactory({...baseConfig,curvatureBound:design.curvatureBound,pulseCaps,valleyCaps,warpWeightLevels:weights});}

  const controls=overrideControls??design.valleyControls;
  if(controls.length!==count)throw Error('One control per modified cell required');
  const total=new Float64Array(6);
  for(let n=0;n<count;n++){const row=rowFor(n,controls[n]);for(let q=0;q<6;q++)total[q]+=row.total[q];}
  const inner=old.cells[count-1].rStart,outer=old.cells[0].rEnd,width=baseConfig.orientation*(outer-inner),alpha=(width-total[0])/total[1];
  if(!(alpha>0))throw Error('Modified pulse block exceeds fixed width '+JSON.stringify({minimumWidth:total[0],width,alpha}));
  const cells=old.cells.slice();let r=inner;
  for(let n=count-1;n>=0;n--){cells[n]=fresh.physicalCell(n,controls[n],r,alpha);r=cells[n].rEnd;}
  const ports=[[count-1,0,0],[0,8,1]].map(([n,j,x])=>{const a=old.cells[n].profiles[j](x),b=cells[n].profiles[j](x);return{r:b.r-a.r,w:Math.exp(b.logw)-Math.exp(a.logw),wr:Math.exp(b.logw)*b.dlogwdx/b.drdx-Math.exp(a.logw)*a.dlogwdx/a.drdx};});
  const joins=Array.from({length:count-1},(_,n)=>{const a=cells[n].profiles[0](0),b=cells[n+1].profiles[8](1);return{r:a.r-b.r,w:Math.exp(a.logw)-Math.exp(b.logw),wr:Math.exp(a.logw)*a.dlogwdx/a.drdx-Math.exp(b.logw)*b.dlogwdx/b.drdx};});
  if([...ports,...joins].some(p=>Math.max(...Object.values(p).map(Math.abs))>2e-10))throw Error('Physical block join mismatch');
  const oldHeight=old.cells.slice(0,count).reduce((a,c)=>a+c.heightSpan,0),oldLength=old.cells.slice(0,count).reduce((a,c)=>a+c.meridianLength,0);
  return {...old,cells,parameters:{...old.parameters,constructor:'finite_preserved_pulses_v1',outerCellDesign:{...design,pulseCaps:pulseCaps.map(p=>Array.from(p)),warpWeights:weights.map(p=>Array.from(p)),valleyControls:Array.from(controls)}},stats:{...old.stats,heightSpan:old.stats.heightSpan-oldHeight+total[4]+alpha*total[5],meridianLength:old.stats.meridianLength-oldLength+total[2]+alpha*total[3],blockCount:count,blockAlpha:alpha,blockCurvatureBound:design.curvatureBound,blockMinimumWidth:total[0],blockWidth:width,blockPortDifferences:ports,blockInternalJoinDifferences:joins,unchangedPhysicalCellsFrom:count},sourceDefinition:'Original nine segments and both pulse/valley functions retained; finite caps/valley controls/positive warp changes with original deep source and protected ports.'};
 }
 return {assemble};
}
