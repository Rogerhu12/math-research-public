/**
 * Reallocate the existing free radial width using a frozen actual linear load.
 * A is unchanged; B_new=B[1-kappa*T+kappa*c*T*load], where
 * c=integral(B*T)/integral(B*T*load) separately on each changed cell.
 * Thus every exact cell width and all old endpoint jets are preserved.
 * The new metric still requires its own actual linear/nonlinear response.
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import {createRecalibrationFactory as createBaseFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
const hash=x=>crypto.createHash('sha256').update(x).digest('hex');
const clone=x=>JSON.parse(JSON.stringify(x));
const S5=t=>t*t*t*(10+t*(-15+6*t));
const sourceFiles=['fd2d-load-balanced-tail.mjs','closing_weighted_tail.mjs',
  'closing_recalibrated_tail.mjs','fd2d-bounded-tail-point-cache.mjs'];
const sources=Object.fromEntries(sourceFiles.map(name=>[name,
  hash(fs.readFileSync(new URL('./'+name,import.meta.url)))]));
function interpolator(knots,values){
  return x=>{
    if(x<=knots[0])return values[0];
    if(x>=knots.at(-1))return values.at(-1);
    let lo=0,hi=knots.length-1;
    while(hi-lo>1){const m=(lo+hi)>>1;if(knots[m]<=x)lo=m;else hi=m;}
    const t=(x-knots[lo])/(knots[hi]-knots[lo]);
    return values[lo]+(values[hi]-values[lo])*S5(t);
  };
}
export function createRecalibrationFactory(config={}){
  if(config.schema!=='fd2d-load-balanced-tail-v1'||!config.baseConfig||!config.frozenLinearLoad)
    throw Error('A complete frozen load-balanced physical definition is required');
  const base=clone(config.baseConfig),reference=clone(config.frozenLinearLoad),
    kappa=config.loadBlend??.95,N=reference.changedCells;
  if(!(kappa>0&&kappa<1&&Number.isInteger(N)&&N>0&&N<base.protectCell))
    throw Error('Need a strict positive blend and a finite outer prefix');
  const inner=createBaseFactory(base);
  boundTailPointCaches(inner,base,{pointsPerEntry:config.pointCachePerEntry??8});
  const original=inner.assemble(),alpha=original.stats.alpha,records=[],compiled=[];
  for(let n=0;n<N;n++){
    const row=inner.getEntries(n,base.valleyControls[n]),pieces=row.entries.length,
      data=reference.cells[n];
    if(data.cell!==n||data.segments.length!==pieces)throw Error('Load partition mismatch');
    const totalBefore=Array.from(row.total),parts=[];
    for(let j=0;j<pieces;j++){
      const entry=row.entries[j],input=data.segments[j],old=entry.integrand,
        knots=input.x,loads=input.absoluteDeltaL.map((v,k)=>{
          const z=old(knots[k]);
          return z[1]>0?1+v*(z[0]+alpha*z[1])/(alpha*z[1]):1;
        });
      if(knots.length!==loads.length||knots[0]!==0||knots.at(-1)!==1||
         loads.some(v=>!Number.isFinite(v)||v<1))throw Error('Invalid finite positive load');
      parts.push({entry,old,knots,loads});
    }
    // Average the two evaluations at each artificial profile join; this is
    // part of the frozen weight definition, not a modification of the old H.
    for(let j=0;j<pieces-1;j++){
      const v=(parts[j].loads.at(-1)+parts[j+1].loads[0])/2;
      parts[j].loads[parts[j].loads.length-1]=v;parts[j+1].loads[0]=v;
    }
    let numerator=0,denominator=0;
    for(let j=0;j<pieces;j++){
      const p=parts[j],load=interpolator(p.knots,p.loads),
        taper=x=>{const t=(j+x)/pieces,d=Math.min(1,pieces*t,pieces*(1-t));return S5(Math.max(0,d));};
      p.load=load;p.taper=taper;
      p.entry.breakpoints=[...new Set([...p.entry.breakpoints,...p.knots.filter(x=>x>0&&x<1)])].sort((a,b)=>a-b);
      p.entry.integrand=x=>{const B=p.old(x)[1],T=taper(x);return [B*T,B*T*load(x),0,0,0,0];};
      const z=p.entry.integrate(0,1);numerator+=z[0];denominator+=z[1];
      p.entry.integrand=p.old;
    }
    const c=numerator/denominator;
    if(!(numerator>0&&denominator>0&&c>0))throw Error('Positive load normalization failed');
    row.total.fill(0);
    for(const p of parts){
      const e=p.entry;
      e.integrand=x=>{
        const z=p.old(x),T=p.taper(x),weight=1-kappa*T+kappa*c*T*p.load(x);
        if(!(weight>0&&Number.isFinite(weight)))throw Error('Lost positive free warp');
        z[1]*=weight;z[3]*=weight;z[5]*=weight;return z;
      };
      e.total.fill(0);e.cumA.fill(0);e.cumB.fill(0);
      for(let k=0;k<inner.parameters.warpSteps;k++){
        const z=e.integrate(k/inner.parameters.warpSteps,(k+1)/inner.parameters.warpSteps);
        for(let i=0;i<6;i++)e.total[i]+=z[i];
        e.cumA[k+1]=e.total[0];e.cumB[k+1]=e.total[1];
      }
      for(let i=0;i<6;i++)row.total[i]+=e.total[i];
    }
    records.push({cell:n,kappa,c,numerator,denominator,
      oldA:totalBefore[0],newA:row.total[0],oldB:totalBefore[1],newB:row.total[1],
      massDifference:row.total[1]-totalBefore[1],
      predictedWidthDifference:row.total[0]-totalBefore[0]+alpha*(row.total[1]-totalBefore[1])});
    compiled.push({cell:n,normalization:c,segments:parts.map((p,j)=>({segment:j,x:p.knots,positiveLoad:p.loads}))});
  }
  // Clear every old physical point memo after replacing the integrands.
  boundTailPointCaches(inner,base,{pointsPerEntry:config.pointCachePerEntry??8});
  const definition={schema:'fd2d-load-balanced-physical-definition-v1',baseConfig:base,
    frozenLinearLoad:reference,compiledPositiveLoad:compiled,kappa,sources,
    normalization:'c_n=integral(B T)/integral(B T load), exact integral definition',
    alpha:'The same radius-normalizing alpha as the original bound base factory',
    positiveWeight:'W=1-kappa*T+kappa*c_n*T*load >= 1-kappa > 0',
    taper:'S5 on the first and last ninth of a cell; one on its middle seven ninths',
    interpolation:'Positive C2 S5 blends between consecutive frozen load samples; shared endpoint values averaged',
    originalLinearSolutionUse:'Only a frozen design weight; it is never substituted for the new physical ODE solution'};
  const definitionSHA=hash(JSON.stringify(definition));
  let cached=null;
  function assemble(controls=base.valleyControls,overrideAlpha=null){
    if(overrideAlpha!==null||JSON.stringify(controls)!==JSON.stringify(base.valleyControls))
      throw Error('This frozen redistribution has no beta or alpha mutation interface');
    if(cached)return cached;
    const tail=inner.assemble(base.valleyControls,alpha);
    cached={...tail,parameters:{...tail.parameters,constructor:'fd2d_load_balanced_tail_v1',
      loadBalancedDefinition:definition,loadBalancedDefinitionSHA256:definitionSHA},
      stats:{...tail.stats,loadRedistribution:{definitionSHA,changedCells:N,kappa,records,
        originalStats:original.stats,
        scope:'Actual floating integrals; the exact normalized construction preserves each cell width and old deep metric'}},
      sourceDefinition:'Bound original source and unchanged deep cells; a positive normalized finite free-warp redistribution.'};
    return cached;
  }
  return {...inner,parameters:{...inner.parameters,loadBalancedDefinitionSHA256:definitionSHA},assemble,
    physicalCell(){throw Error('This frozen load-balanced factory does not recalibrate cells');}};
}
