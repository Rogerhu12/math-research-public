"use strict";
/* Add actual quartic metric point rows to the entire unchanged finite
 * objective. The point set is frozen outside LM and reused by value/normal.
 * No original row, coefficient, metric component or geometry term is removed. */
function defaultPeakRows() {
  const radial=[.18,.20,.22,.2346108715251372,.25,.27,.30];
  const fractions=[0,1/64,1/32,31/32,63/64,1];
  return radial.flatMap(s=>fractions.map((f,j)=>({s,u:Math.PI*f,
    weight:.0005*(j===0||j===fractions.length-1?.5:1),anglePiFraction:f})));
}
function createFixedPeakMetricProvider(base,metricPosition,rows=defaultPeakRows()) {
  const n=base.dimension,S=base.base.end;
  if(metricPosition.dimension!==n||typeof metricPosition.metricPacketRows!=="function")
    throw Error("Same complete quartic metric packet provider required");
  const points=rows.map(p=>({...p}));
  if(!points.length||points.some(p=>![p.s,p.u,p.weight].every(Number.isFinite)||p.s<0||p.s>S||p.weight<=0))
    throw Error("Fixed finite physical points with positive weights required");
  function extra(z,config={}) {
    if(z.length!==n)throw Error("Complete parameter state required");
    const derivatives=!!config.jacobian||!!config.direction;
    if(config.direction&&config.direction.length!==n)throw Error("Complete parameter direction required");
    const H=config.jacobian?new Float64Array(n*n):null,g=config.jacobian?new Float64Array(n):null;
    const residuals=config.residuals?new Float64Array(2*points.length):null;
    const jvp=config.direction?new Float64Array(2*points.length):null;
    let squared=0,quadratic=0,maxRelativeMetric=0,worst=null,lastS=null,sl=null;
    for(let j=0;j<points.length;j++) {
      const pt=points[j];if(pt.s!==lastS){sl=metricPosition.slice(pt.s,z,derivatives);lastS=pt.s;}
      const packet=sl.point(pt.u),r=metricPosition.metricPacketRows(packet,derivatives),w=pt.weight,sw=Math.sqrt(w);
      squared+=w*r.squared;quadratic+=w*r.q;
      if(packet.relativeMetric>maxRelativeMetric){maxRelativeMetric=packet.relativeMetric;worst={s:pt.s,u:pt.u,rE:r.e,rF:r.f};}
      if(residuals){residuals[2*j]=sw*r.E;residuals[2*j+1]=Math.SQRT2*sw*r.F;}
      if(derivatives) {
        for(let a=0;a<packet.indices.length;a++) {
          const ia=packet.indices[a];if(g)g[ia]+=w*(r.de[a]*r.E+2*r.df[a]*r.F);
          if(H)for(let b=0;b<=a;b++){
            const ib=packet.indices[b],v=w*(r.de[a]*r.de[b]+2*r.df[a]*r.df[b]);
            H[ia*n+ib]+=v;if(ia!==ib)H[ib*n+ia]+=v;
          }
        }
        if(jvp){let E=0,F=0;for(let k=0;k<packet.indices.length;k++){
          E+=r.de[k]*config.direction[packet.indices[k]];F+=r.df[k]*config.direction[packet.indices[k]];
        }jvp[2*j]=sw*E;jvp[2*j+1]=Math.SQRT2*sw*F;}
      }
    }
    const out={squaredNorm:squared,norm:Math.sqrt(squared),quadraticSquaredNorm:quadratic,
      extraQuarticSquaredNorm:squared-quadratic,maxRelativeMetric,worst,rowCount:2*points.length,
      physicalPointCount:points.length,totalPointWeight:points.reduce((s,p)=>s+p.weight,0),
      allOriginalRowsAndColumnsRetained:true,continuousCertificate:false};
    if(H){out.H=H;out.g=g;}if(residuals)out.residuals=residuals;if(jvp)out.jvp=jvp;return out;
  }
  function evaluate(z,config={}) {
    const old=base.evaluate(z,config),added=extra(z,config),out={...old};
    out.originalObjectiveSquaredNorm=old.squaredNorm;
    out.originalMetricSquaredNorm=old.metricSquaredNorm;
    out.originalQuadratureMaxRelativeMetric=old.maxRelativeMetric;
    out.originalQuadratureWorst=old.worst;
    out.additionalPeakMetricSquaredNorm=added.squaredNorm;
    out.additionalPeakQuadraticSquaredNorm=added.quadraticSquaredNorm;
    out.additionalPeakMaximum=added.maxRelativeMetric;
    out.additionalPeakWorst=added.worst;
    out.metricSquaredNorm=old.metricSquaredNorm+added.squaredNorm;
    out.squaredNorm=old.squaredNorm+added.squaredNorm;out.norm=Math.sqrt(out.squaredNorm);
    out.rowCount=old.rowCount+added.rowCount;
    out.maxRelativeMetric=Math.max(old.maxRelativeMetric,added.maxRelativeMetric);
    if(added.maxRelativeMetric>old.maxRelativeMetric)out.worst=added.worst;
    if(config.jacobian){for(let i=0;i<n*n;i++)out.H[i]+=added.H[i];for(let i=0;i<n;i++)out.g[i]+=added.g[i];
      out.diagonal=Float64Array.from({length:n},(_,i)=>out.H[i*n+i]);}
    for(const key of ["residuals","jvp"])if(old[key]&&added[key]){
      const all=new Float64Array(old[key].length+added[key].length);all.set(old[key]);all.set(added[key],old[key].length);out[key]=all;
    }
    out.fixedPeakMetricRowsAreFiniteSearchGuides=true;out.continuousCertificate=false;return out;
  }
  return {...base,extraPeakMetric:extra,peakMetricRows:points,evaluate,
    value:z=>evaluate(z),normal:z=>evaluate(z,{jacobian:true}),
    definition:{...base.definition,fixedPeakMetric:{schema:"6a65-fixed-extra-quartic-metric-points-v1",
      points,originalAllRowsAndColumnsRetained:true,fullEAndFCoupledRows:true,
      fixedDuringAllTrialsAndRecordedContinuation:true,derivativeSource:"quartic wrapper metricPacketRows(packet,true)",
      newFiniteObjectiveRequiresNewFullNormalAndValue:true,continuousCertificate:false}}};
}
module.exports={defaultPeakRows,createFixedPeakMetricProvider};
