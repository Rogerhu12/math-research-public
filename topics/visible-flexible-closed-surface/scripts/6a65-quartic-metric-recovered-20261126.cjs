"use strict";
/* Recovered from the executed 2026-11-26 source text after executor loss.
 * Same R201/R205 position family; new metric merit q+q^2/tau^2.
 * This source has a new identity; old execution hashes are not inherited. */
function createQuarticMetricProvider(position,engine,tau){
  if(!(Number.isFinite(tau)&&tau>0))throw Error("Explicit positive metric tau required");
  const p=position,n=p.dimension,md=p.definition.parentMetric,N=md.fullEquivalentAngles,nq=N/2,S=p.base.end;
  const radiusRange=md.stateLayout.radius;
  if(!Array.isArray(radiusRange)||radiusRange.length!==2)throw Error("Explicit designed-radius layout required");
  const G2=engine.gauss(2),cuts=Array.from(p.radialCuts),points=[];
  for(let i=1;i<cuts.length;i++){
    const lo=cuts[i-1],length=cuts[i]-lo;
    for(let j=0;j<2;j++)points.push({s:lo+length*G2.x[j],weight:length*G2.w[j]/S});
  }
  const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],tau2=tau*tau;
  function packetRows(packet,derivatives=false){
    const a=packet.a,T=packet.jets.Xu.map(v=>v/a),V=packet.jets.Xs,e=dot(V,V)-1,f=dot(V,T);
    const q=e*e+2*f*f,h=Math.sqrt(1+q/tau2),E=h*e,F=h*f,m=packet.indices.length;
    const de=derivatives?new Float64Array(m):null,df=derivatives?new Float64Array(m):null;
    if(derivatives)for(let k=0;k<m;k++){
      const v=packet.parameterJets[k],col=packet.indices[k],da=col>=radiusRange[0]&&col<radiusRange[1]?dot(v.Xu,T):0;
      const dT=v.Xu.map((x,i)=>(x-da*T[i])/a),aE=2*dot(V,v.Xs),aF=dot(v.Xs,T)+dot(V,dT),dh=(e*aE+2*f*aF)/(tau2*h);
      de[k]=h*aE+e*dh;df[k]=h*aF+f*dh;
    }
    return {e,f,q,h,E,F,de,df,squared:q+q*q/tau2};
  }
  function metric(z,config={}){
    const derivatives=!!config.jacobian||!!config.direction;
    const H=config.jacobian?new Float64Array(n*n):null,g=config.jacobian?new Float64Array(n):null;
    const rows=points.length*(nq+1)*2,res=config.residuals?new Float64Array(rows):null,jvp=config.direction?new Float64Array(rows):null;
    if(config.direction&&config.direction.length!==n)throw Error("Complete direction required");
    let squared=0,original=0,maxRelativeMetric=0,minImmersion=Infinity,minMeanR=Infinity,worst=null,index=0;
    for(const rp of points){
      const sl=p.slice(rp.s,z,derivatives);
      for(let j=0;j<=nq;j++){
        const packet=sl.node(j),r=packetRows(packet,derivatives),aw=(j===0||j===nq?.5:1)/nq,w=rp.weight*aw,sw=Math.sqrt(w);
        squared+=w*r.squared;original+=w*r.q;minImmersion=Math.min(minImmersion,packet.immersion);minMeanR=Math.min(minMeanR,packet.phase.R);
        if(packet.relativeMetric>maxRelativeMetric){maxRelativeMetric=packet.relativeMetric;worst={s:rp.s,u:j*Math.PI/nq,rE:r.e,rF:r.f};}
        if(res){res[index]=sw*r.E;res[index+1]=Math.sqrt(2)*sw*r.F;}
        if(derivatives){
          for(let k=0;k<packet.indices.length;k++){
            const ik=packet.indices[k];if(g)g[ik]+=w*(r.de[k]*r.E+2*r.df[k]*r.F);
            if(H)for(let l=0;l<=k;l++){
              const il=packet.indices[l],v=w*(r.de[k]*r.de[l]+2*r.df[k]*r.df[l]);
              H[ik*n+il]+=v;if(ik!==il)H[il*n+ik]+=v;
            }
          }
          if(jvp){let E=0,F=0;for(let k=0;k<packet.indices.length;k++){E+=r.de[k]*config.direction[packet.indices[k]];F+=r.df[k]*config.direction[packet.indices[k]];}jvp[index]=sw*E;jvp[index+1]=Math.sqrt(2)*sw*F;}
        }
        index+=2;
      }
    }
    const out={squaredNorm:squared,norm:Math.sqrt(squared),quadraticMetricSquaredNorm:original,quarticMetricSquaredNorm:squared-original,maxRelativeMetric,minImmersion,minMeanR,worst,rowCount:rows,radialPoints:points.length,halfNodes:nq+1,fullEquivalentAngles:N,metricLoss:{q:"e*e+2*f*f",loss:"q+q*q/tau^2",tau},continuousCertificate:false};
    if(H){out.H=H;out.g=g;}if(res)out.residuals=res;if(jvp)out.jvp=jvp;return out;
  }
  function evaluate(z,config={}){
    const met=metric(z,config),curv=p.penalty(z,config),out={...met,metricSquaredNorm:met.squaredNorm,curvaturePenaltySquaredNorm:curv.squaredNorm};
    out.squaredNorm=met.squaredNorm+curv.squaredNorm;out.norm=Math.sqrt(out.squaredNorm);out.rowCount=met.rowCount+curv.rowCount;
    out.curvature={...curv};for(const key of ["H","g","residuals","jvp"])delete out.curvature[key];
    if(config.jacobian){for(let i=0;i<n*n;i++)out.H[i]+=curv.H[i];for(let i=0;i<n;i++)out.g[i]+=curv.g[i];out.diagonal=Float64Array.from({length:n},(_,i)=>out.H[i*n+i]);}
    for(const key of ["residuals","jvp"])if(met[key]&&curv[key]){const r=new Float64Array(met[key].length+curv[key].length);r.set(met[key]);r.set(curv[key],met[key].length);out[key]=r;}
    out.curvatureIsNumericalGuide=true;out.continuousCertificate=false;out.strongTargetComplete=false;return out;
  }
  return {...p,metric,metricPacketRows:packetRows,evaluate,value:z=>evaluate(z),normal:z=>evaluate(z,{jacobian:true}),definition:{...p.definition,metricLoss:{schema:"6a65-quartic-metric-recovered-20261126-v1",q:"e*e+2*f*f",loss:"q+q*q/tau^2",tau,derivative:"h*dr+r*(r.dot(dr)/(tau^2*h))",zeroSetUnchanged:true,finiteObjectiveChanged:true,allColumnsRetained:true,continuousCertificate:false}}};
}
module.exports={createQuarticMetricProvider};

