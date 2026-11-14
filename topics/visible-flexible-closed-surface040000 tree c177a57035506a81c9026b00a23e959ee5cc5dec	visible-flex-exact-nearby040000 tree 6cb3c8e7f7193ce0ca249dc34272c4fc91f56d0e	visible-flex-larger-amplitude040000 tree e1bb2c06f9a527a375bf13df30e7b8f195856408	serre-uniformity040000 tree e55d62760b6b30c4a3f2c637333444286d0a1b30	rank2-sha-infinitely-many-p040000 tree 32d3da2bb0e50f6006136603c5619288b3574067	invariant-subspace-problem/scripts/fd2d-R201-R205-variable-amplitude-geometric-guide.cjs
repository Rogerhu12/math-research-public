"use strict";
/* R201 full-half adaptation of frozen R203: complete true-position geometric guide. This is a finite objective,
 * never a continuous geometry certificate or a reach test. All positions and
 * all parameter columns come from the actual R196 position two-jet provider.
 */
function createR201R205AmplitudeGeometryProvider(positionProvider,options={}){
  const p=positionProvider,n=p.dimension,def=p.definition,md=def.parentMetric;
  const N=md.fullEquivalentAngles,nq=N/2,S=p.base.end,cut=md.stateLayout.cutHeight;
  if((def.schema!=="fd2d-R206-appended-global-parameter-provider-v1"||def.positionFamilySchema!=="fd2d-R201-R205-variable-amplitude-position-family-v1")||!Number.isInteger(nq)||nq<1||!Array.isArray(p.radialCuts)||typeof p.slice!=="function")
    throw Error("Explicit R201 half-period position provider required");
  const radius=options.radius===undefined?1.59:options.radius;
  const width=options.width===undefined?.84:options.width;
  const held=options.held===undefined?.65:options.held;
  const weight=options.weight===undefined?10:options.weight;
  const nodeShare=options.nodeShare===undefined?.5:options.nodeShare;
  const A=md.centralA;
  const cutWindow=options.cutWindow===undefined?null:Array.from(options.cutWindow);
  if(cutWindow&&(cutWindow.length!==2||!cutWindow.every(Number.isFinite)||!(cutWindow[0]>0&&cutWindow[0]<cutWindow[1])))throw Error("Explicit positive cut-height window required");
  function domain(z){const Z=p.base.height+z[cut];if(cutWindow&&(Z<cutWindow[0]||Z>cutWindow[1]))throw Error("Outside declared actual finite cut-height window");}

  if(![radius,width,held,weight,nodeShare,A].every(Number.isFinite)||
     !(radius>0&&width>0&&held>0&&weight>0&&A>0&&nodeShare>=0&&nodeShare<=1))
    throw Error("Explicit positive guide parameters required");
  const cuts=Array.from(p.radialCuts),points=[],gx=[(1-1/Math.sqrt(3))/2,(1+1/Math.sqrt(3))/2];
  if(cuts[0]!==0||cuts.at(-1)!==S||cuts.some((x,i)=>!Number.isFinite(x)||(i&&x<=cuts[i-1])))
    throw Error("Fixed complete radial cuts required");
  if(nodeShare>0)for(let i=0;i<cuts.length;i++){
    const h=(i?cuts[i]-cuts[i-1]:0)+(i+1<cuts.length?cuts[i+1]-cuts[i]:0);
    points.push({s:cuts[i],weight:nodeShare*h/(2*S),kind:"physical_knot"});
  }
  if(nodeShare<1)for(let i=1;i<cuts.length;i++){
    const lo=cuts[i-1],h=cuts[i]-lo;
    for(const q of gx)points.push({s:lo+h*q,weight:(1-nodeShare)*h/(2*S),kind:"cell_Gauss2"});
  }
  points.sort((a,b)=>a.s-b.s);
  const names=["ball","width_plus","width_minus","height_plus","height_minus","held_plus","held_minus"];
  function constraints(packet,z,derivatives=false){
    const X=packet.jets.X,Z=p.base.height+z[cut],r=Math.hypot(...X);
    const dp=[X[0],X[1]-A,X[2]],dm=[X[0],X[1]+A,X[2]],rp=Math.hypot(...dp),rm=Math.hypot(...dm);
    if(!(r>0&&rp>0&&rm>0&&Z>0))throw Error("Geometric distance differential domain");
    const signed=[r-radius,X[1]-width,-X[1]-width,X[2]-Z,-X[2]-Z,held-rp,held-rm];
    const residual=signed.map(v=>Math.max(0,v)),indices=Array.from(packet.indices);
    if(!indices.includes(cut))indices.push(cut);
    const jacobian=derivatives?Array.from({length:7},()=>new Float64Array(indices.length)):null;
    if(derivatives){
      const slots=new Map(packet.indices.map((v,k)=>[v,k]));
      for(let k=0;k<indices.length;k++){
        const j=indices[k],slot=slots.get(j),dX=slot===undefined?[0,0,0]:packet.parameterJets[slot].X,dZ=j===cut?1:0;
        const g=[(X[0]*dX[0]+X[1]*dX[1]+X[2]*dX[2])/r,dX[1],-dX[1],dX[2]-dZ,-dX[2]-dZ,
          -(dp[0]*dX[0]+dp[1]*dX[1]+dp[2]*dX[2])/rp,-(dm[0]*dX[0]+dm[1]*dX[1]+dm[2]*dX[2])/rm];
        for(let q=0;q<7;q++)jacobian[q][k]=signed[q]>0?g[q]:0;
      }
    }
    return {signed,residual,indices,jacobian,squared:residual.reduce((v,x)=>v+x*x,0),
      radius:r,absoluteY:Math.abs(X[1]),heightExcess:Math.abs(X[2])-Z,heldDistance:Math.min(rp,rm),Z,A};
  }
  function penalty(z,config={}){
    if(z.length!==n)throw Error("Full parameter vector required");domain(z);
    const need=!!config.jacobian||!!config.direction,rows=points.length*(nq+1)*7;
    const H=config.jacobian?new Float64Array(n*n):null,g=config.jacobian?new Float64Array(n):null;
    const residuals=config.residuals?new Float64Array(rows):null,jvp=config.direction?new Float64Array(rows):null;
    if(config.direction&&config.direction.length!==n)throw Error("Full direction required");
    let squared=0,active=0,thresholds=0,maxRadius=0,maxAbsoluteY=0,maxHeightExcess=-Infinity,minHeldDistance=Infinity;
    const maxima=Array(7).fill(0),witnesses=Array(7).fill(null);
    for(let ri=0;ri<points.length;ri++){
      const q=points[ri],sl=p.slice(q.s,z,false),selected=[];
      for(let j=0;j<=nq;j++){
        const packet=sl.node(j),c=constraints(packet,z,false),aw=(j===0||j===nq?.5:1)/nq,w=weight*q.weight*aw,off=(ri*(nq+1)+j)*7;
        squared+=w*c.squared;maxRadius=Math.max(maxRadius,c.radius);maxAbsoluteY=Math.max(maxAbsoluteY,c.absoluteY);
        maxHeightExcess=Math.max(maxHeightExcess,c.heightExcess);minHeldDistance=Math.min(minHeldDistance,c.heldDistance);
        for(let k=0;k<7;k++){
          if(c.signed[k]===0)thresholds++;
          if(c.residual[k]>maxima[k]){maxima[k]=c.residual[k];witnesses[k]={s:q.s,u:packet.u,X:packet.jets.X};}
          if(residuals)residuals[off+k]=Math.sqrt(w)*c.residual[k];
        }
        if(c.squared>0){active++;if(need)selected.push({j,w,off});}
      }
      if(!selected.length)continue;
      const sd=p.slice(q.s,z,true);
      for(const {j,w,off}of selected){
        const c=constraints(sd.node(j),z,true),m=c.indices.length;
        for(let a=0;a<m;a++){
          const ia=c.indices[a];let dg=0;
          for(let k=0;k<7;k++)dg+=c.jacobian[k][a]*c.residual[k];
          if(g)g[ia]+=w*dg;
          if(H)for(let b=0;b<=a;b++){
            const ib=c.indices[b];let h=0;for(let k=0;k<7;k++)h+=c.jacobian[k][a]*c.jacobian[k][b];
            H[ia*n+ib]+=w*h;if(ia!==ib)H[ib*n+ia]+=w*h;
          }
        }
        if(jvp)for(let k=0;k<7;k++){
          let v=0;for(let a=0;a<m;a++)v+=c.jacobian[k][a]*config.direction[c.indices[a]];
          jvp[off+k]=Math.sqrt(w)*v;
        }
      }
    }
    const out={squaredNorm:squared,norm:Math.sqrt(squared),activePoints:active,thresholdRows:thresholds,rowCount:rows,
      radialPoints:points.length,halfNodes:nq+1,maxRadius,maxAbsoluteY,maxHeightExcess,minHeldDistance,
      maximumViolations:Object.fromEntries(names.map((v,i)=>[v,maxima[i]])),
      witnesses:Object.fromEntries(names.map((v,i)=>[v,witnesses[i]])),guide:{radius,width,held,weight,nodeShare},
      continuousCertificate:false,nonlocalReachChecked:false};
    if(H){out.H=H;out.g=g;}
    if(residuals)out.residuals=residuals;if(jvp)out.jvp=jvp;
    return out;
  }
  function evaluate(z,config={}){
    domain(z);
    const old=p.evaluate(z,config),geo=penalty(z,config),out={...old};
    out.preGeometrySquaredNorm=old.squaredNorm;out.geometryPenaltySquaredNorm=geo.squaredNorm;
    out.squaredNorm=old.squaredNorm+geo.squaredNorm;out.norm=Math.sqrt(out.squaredNorm);out.rowCount=old.rowCount+geo.rowCount;
    out.geometry={...geo};delete out.geometry.H;delete out.geometry.g;delete out.geometry.residuals;delete out.geometry.jvp;
    if(config.jacobian){
      for(let i=0;i<n*n;i++)out.H[i]+=geo.H[i];for(let i=0;i<n;i++)out.g[i]+=geo.g[i];
      out.diagonal=Float64Array.from({length:n},(_,i)=>out.H[i*n+i]);
    }
    for(const key of ["residuals","jvp"])if(old[key]&&geo[key]){
      const v=new Float64Array(old[key].length+geo[key].length);v.set(old[key]);v.set(geo[key],old[key].length);out[key]=v;
    }
    out.geometricConstraintsAreNumericalGuides=true;out.continuousCertificate=false;out.strongTargetComplete=false;
    return out;
  }
  return {dimension:n,base:p.base,curve:p.curve,radialBasis:p.radialBasis,radialCuts:p.radialCuts,
    slice:p.slice,point:p.point,constraints,penalty,evaluate,normal:z=>evaluate(z,{jacobian:true}),value:z=>evaluate(z),
    definition:{...def,schema:"fd2d-R206-appended-global-parameter-provider-v1",parentSchema:def.schema,
      positionFamilySchema:"fd2d-R201-R205-variable-amplitude-position-family-v1",geometryFamilySchema:"fd2d-R201-R205-variable-amplitude-complete-position-guide-v1",
      geometry:{radius,width,held,weight,nodeShare,centralA:A,cutWindow,names,
        heightMeaning:"Inner flat cuff Zc, not developed outer section mean",
        symmetry:"proper half-turn only; full half-period angles, both width and held targets; no quarter reflection",
        derivatives:"all actual X parameter columns, and full cut-height derivative in height rows; fixed central A",
        thresholdConvention:"zero generalized slope at exact hinge boundary",
        noProjection:true,fullNonlinearValueRequired:true,continuousCertificate:false,nonlocalReachChecked:false}}};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR201R205AmplitudeGeometryProvider};
