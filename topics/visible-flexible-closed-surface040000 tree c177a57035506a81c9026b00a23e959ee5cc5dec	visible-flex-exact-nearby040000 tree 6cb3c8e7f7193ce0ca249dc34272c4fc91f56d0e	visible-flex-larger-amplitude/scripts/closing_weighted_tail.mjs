// Positive, C2-compatible reallocation of the free part of the radial warp.
// The frozen base constructor and every archived metric stay unchanged.
import * as base from './closing_recalibrated_tail.mjs';
export {physicalModeColumn,physicalM2Column,diagnosePhysicalMode,diagnosePhysicalM2,
  sampleTailGeometry,idealModeGraph,solvePhysicalCell} from './closing_recalibrated_tail.mjs';
const smooth=x=>x*x*x*(10+x*(-15+6*x));
const marked=Symbol('positive radial weights installed');

export function createRecalibrationFactory(config={}){
 const inner=base.createRecalibrationFactory(config),weights=config.warpWeightLevels??[];
 function getEntries(n,beta=0){
  const row=inner.getEntries(n,beta);if(row[marked])return row;
  const levels=weights[n]??[1,1,1,1,1];
  if(levels.length!==5||levels.some(v=>!(v>0&&Number.isFinite(v))))throw Error('Five positive warp weight levels required');
  // The two port levels are kept at 1: this preserves the cell joins even
  // when the uncapped source has nonzero w_r at those joins.
  if(levels[0]!==1||levels[4]!==1)throw Error('Warp weights at cell ports must equal 1');
  if(levels.every(v=>v===1)){row[marked]=true;return row;}
  row.total.fill(0);
  for(const entry of row.entries){
   const oldIntegrand=entry.integrand,j=entry.j;
   const weight=x=>j%2===0?levels[j/2]:levels[(j-1)/2]*Math.exp(Math.log(levels[(j+1)/2]/levels[(j-1)/2])*smooth(x));
   // No profile points have been evaluated before this wrapper installs the
   // new integrand. entry.integrate and entry.point dynamically read it.
   entry.integrand=x=>{const v=oldIntegrand(x),a=weight(x);v[1]*=a;v[3]*=a;v[5]*=a;return v;};
   entry.total.fill(0);entry.cumA.fill(0);entry.cumB.fill(0);
   const steps=inner.parameters.warpSteps;
   for(let k=0;k<steps;k++){
    const v=entry.integrate(k/steps,(k+1)/steps);for(let i=0;i<6;i++)entry.total[i]+=v[i];
    entry.cumA[k+1]=entry.total[0];entry.cumB[k+1]=entry.total[1];
   }
   for(let i=0;i<6;i++)row.total[i]+=entry.total[i];
  }
  row[marked]=true;return row;
 }
 function assemble(controls=config.valleyControls??[],overrideAlpha=null){
  for(let n=0;n<inner.parameters.protectCell;n++)getEntries(n,controls[n]??0);
  const tail=inner.assemble(controls,overrideAlpha);
  for(let n=0;n<tail.cells.length;n++)for(let j=0;j<tail.cells[n].profiles.length;j++)tail.cells[n].profiles[j].integrationBreakpoints=Array.from(getEntries(n,controls[n]??0).entries[j].breakpoints);
  return {...tail,parameters:{...tail.parameters,constructor:'closing_weighted_tail_v1',warpWeightLevels:weights},stats:{...tail.stats,positiveWarpWeights:weights},sourceDefinition:'Frozen exact deep source; finitely changed cap/valley and positive C2-compatible free-warp weights.'};
 }
 function physicalCell(n,beta,rStart,alpha){const es=getEntries(n,beta),cell=inner.physicalCell(n,beta,rStart,alpha);for(let j=0;j<cell.profiles.length;j++)cell.profiles[j].integrationBreakpoints=Array.from(es.entries[j].breakpoints);return cell;}
 return {...inner,getEntries,assemble,physicalCell};
}
