// Append the unchanged source after the LAST physically modified cell.
// The finite warp, its 160 beta values, and protectCell are not extended.
import {loadClosingTailSource} from './closing_tail_sources.mjs';
const {createBalancedTail}=await loadClosingTailSource('tailnext_balanced_tail.mjs');
const {rawLogSlopeCriticalPoints}=await loadClosingTailSource('f6tail_cusp_grid.mjs');

export function appendUnchangedDeepSource(physical,linearFar){
  const first=physical.parameters.protectCell;
  if(!Number.isInteger(linearFar)||linearFar<first)
    throw Error('The linear far boundary must include every physically modified cell');
  if(physical.cells.length!==first||physical.source.cells.length!==first)
    throw Error('Expected the original finite warp ending at protectCell');
  if(physical.parameters.rejoinR20At!==null&&physical.parameters.rejoinR20At!==undefined)
    throw Error('This entry is for the unchanged R64 source, not an R20 rejoin');
  if(linearFar===first)return {...physical,deepExtension:{first,count:0}};
  const source=createBalancedTail({...physical.source.parameters,depth:linearFar});
  for(let n=0;n<first;n++){
    const a=physical.source.cells[n],b=source.cells[n];
    for(const key of ['mu','delta','R','c','lengthScale'])
      if(a[key]!==b[key])throw Error('Raw source identity changed at '+n+'/'+key);
    if(a.cal.alpha!==b.cal.alpha)throw Error('Raw source calibration changed at '+n);
  }
  const cells=physical.cells.slice();
  for(let n=first;n<linearFar;n++){
    const cell=source.cells[n];
    for(const profile of cell.profiles)
      profile.integrationBreakpoints=rawLogSlopeCriticalPoints(profile);
    cells.push(cell);
  }
  const left=cells[first-1].profiles[0](0),right=cells[first].profiles.at(-1)(1);
  const jet=g=>({r:g.r,logw:g.logw,w:Math.exp(g.logw),
    logw_r:g.dlogwdx/g.drdx,w_r:Math.exp(g.logw)*g.dlogwdx/g.drdx});
  const a=jet(left),b=jet(right),difference={};
  for(const key of Object.keys(a)){
    if(!Number.isFinite(a[key])||!Number.isFinite(b[key]))throw Error('Nonfinite unchanged source join');
    difference[key]=a[key]-b[key];
  }
  return {...physical,cells,source,linearDeepParameters:source.parameters,
    parameters:{...physical.parameters,unchangedDeepSourceStart:first,
      assembledCellCount:linearFar},
    deepExtension:{first,count:linearFar-first,linearFar,left:a,right:b,difference,
      scope:'Only the existing unchanged source is appended. The far Robin condition is still finite; this is not an infinite-tail certificate.'}};
}
