// Finite first-cell metric design. Every physical cell n>=1 is literally retained.
// A positive radial-warp blend preserves the old two-jet at both ports of cell 0.
import path from 'node:path';import{pathToFileURL}from'node:url';
const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;if(!topic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC required');
const base=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const S=x=>x*x*x*(10+x*(-15+6*x));
export function createRecalibrationFactory(config={}){
 const {outerCellDesign:design,...baseConfig}=config;if(!design)throw Error('outerCellDesign is required');
 const originalFactory=base.createRecalibrationFactory(baseConfig);
 function assemble(){
  const old=originalFactory.assemble(),oc=old.cells[0],beta=design.beta??baseConfig.valleyControls?.[0]??0;
  const changed={...baseConfig,curvatureBound:design.curvatureBound,pulseCaps:[design.pulseCaps],valleyCaps:[design.valleyCap],warpWeightLevels:[design.warpWeights]};
  const fresh=base.createRecalibrationFactory(changed),row=fresh.getEntries(0,beta),steps=fresh.parameters.warpSteps,last=row.entries.length-1;
  row.total.fill(0);
  for(const e of row.entries){
   const originalIntegrand=e.integrand,j=e.j;
   e.integrand=x=>{const v=originalIntegrand(x),b=j===0?S(x):j===last?S(1-x):1,g=e.profileSource(x),w=Math.exp(g.logw),E=Math.hypot(1,w),A=(1-b)*Math.abs(oc.profiles[j](x).drdx)+b*v[0],B=b*v[1];return new Float64Array([A,B,E*A,E*B,w*A,w*B]);};
   e.total.fill(0);e.cumA.fill(0);e.cumB.fill(0);
   for(let k=0;k<steps;k++){const v=e.integrate(k/steps,(k+1)/steps);for(let j=0;j<6;j++)e.total[j]+=v[j];e.cumA[k+1]=e.total[0];e.cumB[k+1]=e.total[1];}
   for(let j=0;j<6;j++)row.total[j]+=e.total[j];
  }
  const alpha=(oc.localWidth-row.total[0])/row.total[1];if(!(alpha>0))throw Error('new outer cell exceeds fixed original width');
  const cell=fresh.physicalCell(0,beta,oc.rStart,alpha),cells=[cell,...old.cells.slice(1)];
  const ports=[{j:0,x:0},{j:last,x:1}].map(({j,x})=>{const a=oc.profiles[j](x),b=cell.profiles[j](x);return{r:b.r-a.r,w:Math.exp(b.logw)-Math.exp(a.logw),wr:Math.exp(b.logw)*b.dlogwdx/b.drdx-Math.exp(a.logw)*a.dlogwdx/a.drdx};});
  if(ports.some(p=>Math.max(Math.abs(p.r),Math.abs(p.w),Math.abs(p.wr))>2e-11))throw Error('hybrid physical two-jet port mismatch');
  return {...old,cells,parameters:{...old.parameters,constructor:'hybrid_outer_cell_v1',outerCellDesign:design},stats:{...old.stats,meridianLength:old.stats.meridianLength-oc.meridianLength+cell.meridianLength,heightSpan:old.stats.heightSpan-oc.heightSpan+cell.heightSpan,outerCellAlpha:alpha,outerCellHeight:cell.heightSpan,outerCellMinimumWidth:row.total[0],outerCellPortDifferences:ports,unchangedPhysicalCellsFrom:1},sourceDefinition:'Original actual deep source and all cells n>=1 retained; only finite outer cell changed with exact port two-jets.'};
 }
 return {assemble};
}
