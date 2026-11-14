/* New R205 implementation; parent frozen R196 curvature Git blob 4512b251cd28727b714015b88e68ca8e8411cf08.
 * Fixed-amplitude reference changes X and its full two-jet. Every old finite
 * parameter direction is still differentiated through complete primitives.
 */
/* R196 nonuniform curvature factory. Parent R191 Git blob
 * 9322c7d1cc804d6529ab397d030af0e6c23ca2c7. Full T/Ts/Tss/Tu, primitive,
 * Gram-normal and parameter derivatives retained; explicit metric basis shared.
 */
/* R191: complete true-curvature penalty on the R187/R190 position family.
 * All angular functions remain complete. All parameter columns are analytic:
 * theta, phi, height, cut height and (for R190) the actual radius coefficients.
 */
"use strict";
function createR205CurvatureProvider(engine,metricProvider,options={},algebra){
  if(!algebra){
    if(typeof require==="undefined")throw Error("Supply createR191Algebra() in a pure V8 call");
    algebra=require("./fd2d-position-curvature-chain-R191.cjs").createR191Algebra();
  }
  const md=metricProvider.definition,designed=md.schema==="fd2d-R190-C2-direct-position-designed-radius-finite-provider-v1";
  if(!designed&&md.schema!=="fd2d-R187-C2-direct-position-two-angle-finite-provider-v1")throw Error("Explicit complete position provider required");
  const radialBasis=metricProvider.radialBasis;
  if(!radialBasis||md.radialBasisDefinition?.schema!=="fd2d-R196-shared-simple-cubic-radial-basis-v1"||
    radialBasis.count!==md.radialBasisCount||JSON.stringify(radialBasis.knots)!==JSON.stringify(md.radialBasisDefinition.knots)||
    !Array.isArray(metricProvider.radialCuts))throw Error("Explicit same R196 basis/knots/cuts required");
  const J=md.radialBasisCount,K=md.angularModes,N=md.fullEquivalentAngles,nq=N/4,A=Math.PI/2,du=A/nq;
  const base=metricProvider.base,curve=metricProvider.curve,c=base.centralLength,S=base.end;
  const bentReference=metricProvider.bentReference;
  if(!bentReference||md.bentAnnulusReference?.schema!=="fd2d-R205-fixed-amplitude-bent-annulus-reference-v1")
    throw Error("R205 requires its explicit bent-annulus metric reference, not an old provider");
  const oldDimension=2*J*K+J+1,n=metricProvider.dimension,cutIndex=oldDimension-1;
  if(n!==oldDimension+(designed?J:0))throw Error("Wrong original/designed parameter layout");
  const guide=options.guide===undefined?9.5:options.guide,weight=options.weight===undefined?1e-4:options.weight;
  const nodeShare=options.nodeShare===undefined?.5:options.nodeShare;
  if(![guide,weight,nodeShare].every(Number.isFinite)||!(guide>0&&weight>0&&nodeShare>=0&&nodeShare<=1))throw Error("Explicit positive guide/weight and nodeShare in [0,1] required");
  const G8=engine.gauss(8),G2=engine.gauss(2);
  const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
  function shape(s){
    if(s<=c)return [0,0,0];
    if(s>=S)return [1,0,0];
    const t=(s-c)/(S-c),L=S-c;
    return [t*t*t*(10+t*(-15+6*t)),30*t*t*(1-t)*(1-t)/L,60*t*(1-t)*(1-2*t)/(L*L)];
  }
  const angleRecordCache=new Map();
  function record(u){
    if(angleRecordCache.has(u))return angleRecordCache.get(u);
    const f=[],fu=[];
    for(let k=1;k<=K;k++){f.push(Math.sin(2*k*u));fu.push(2*k*Math.cos(2*k*u));}
    const value={u,g:curve.at(u),f,fu,sn:Math.sin(u),cs:Math.cos(u)};
    if(angleRecordCache.size>=65536)angleRecordCache.delete(angleRecordCache.keys().next().value);
    angleRecordCache.set(u,value);return value;
  }
  const angleNodes=Array.from({length:nq+1},(_,j)=>record(j*du));
  const angleQuads=Array.from({length:nq},(_,j)=>G8.x.map((x,k)=>({...record((j+x)*du),weight:du*G8.w[k]})));
  function radial(s,z){
    if(!Number.isFinite(s)||s<0||s>S||z.length!==n||Array.from(z).some(x=>!Number.isFinite(x)))throw Error("Invalid complete state or physical point");
    if(designed&&Math.max(...Array.from(z).slice(oldDimension).map(Math.abs))>md.radiusCoefficientBound)throw Error("Outside original R190 radius domain");
    const p=base.at(s),w=engine.profileWeights(s,c,S),angles=[],heights=[],radii=[];
    const heightBend=bentReference.heightCorrection(s);
    let a=p.a,as=p.as,ass=p.ass,Z=p.z-heightBend.value,Zs=p.zs-heightBend.first,Zss=p.zss-heightBend.second;
    const radialJets=radialBasis.physicalJets(s,c,S);
    for(let rj=0;rj<radialJets.indices.length;rj++){
      const j=radialJets.indices[rj],b=radialJets.value[rj],bp=radialJets.first[rj],bpp=radialJets.second[rj];
      const hz=z[2*J*K+j];Z+=hz*b;Zs+=hz*bp;Zss+=hz*bpp;
      if(designed){const rr=z[oldDimension+j];a+=rr*b;as+=rr*bp;ass+=rr*bpp;}
      if(b===0&&bp===0&&bpp===0)continue;
      for(let k=0;k<K;k++){
        angles.push({index:j*K+k,kind:0,k,b,bp,bpp});
        angles.push({index:J*K+j*K+k,kind:1,k,b,bp,bpp});
      }
      heights.push({index:2*J*K+j,b,bp,bpp});
      if(designed)radii.push({index:oldDimension+j,b,bp,bpp});
    }
    const sh=shape(s);Z+=z[cutIndex]*sh[0];Zs+=z[cutIndex]*sh[1];Zss+=z[cutIndex]*sh[2];
    if(sh.some(x=>x!==0))heights.push({index:cutIndex,b:sh[0],bp:sh[1],bpp:sh[2]});
    if(!(a>0))throw Error("Actual designed radius is not positive");
    return {s,p,w,a,as,ass,Z,Zs,Zss,angles,heights,radii};
  }
  function fill(rad,q,z,derivatives){
    const {g,sn,cs}=q,w=rad.w,ex=-sn,ey=cs,dx=g.v[0]-ex,dy=g.v[1]-ey;
    const tx=ex+w.q*dx,ty=ey+w.q*dy,tz=w.r*g.h;
    const txs=w.qs*dx,tys=w.qs*dy,tzs=w.rs*g.h,txss=w.qss*dx,tyss=w.qss*dy,tzss=w.rss*g.h;
    const txu=-cs+w.q*(g.vu[0]+cs),tyu=-sn+w.q*(g.vu[1]+sn),tzu=w.r*g.hu;
    const cp2=tx*tx+ty*ty,cp=Math.sqrt(cp2);
    if(!(cp2>1e-15))throw Error("Original reference angle chart is singular");
    const cr=tx*tys-ty*txs,hd=tx*txs+ty*tys;
    let th=q.u+Math.atan2(ex*ty-ey*tx,ex*tx+ey*ty),ph=Math.asin(Math.max(-1,Math.min(1,tz)));
    let ths=cr/cp2,phs=tzs/cp,thss=(tx*tyss-ty*txss)/cp2-2*hd*cr/(cp2*cp2),phss=tzss/cp-tzs*hd/(cp2*cp);
    let thu=(tx*tyu-ty*txu)/cp2,phu=tzu/cp;
    const bend=bentReference.angular(rad.s,q.u);
    th+=bend[0];ph+=bend[1];ths+=bend[2];phs+=bend[3];
    thss+=bend[4];phss+=bend[5];thu+=bend[6];phu+=bend[7];
    for(const col of rad.angles){
      const v=z[col.index]*q.f[col.k],vu=z[col.index]*q.fu[col.k];
      if(col.kind===0){th+=col.b*v;ths+=col.bp*v;thss+=col.bpp*v;thu+=col.b*vu;}
      else{ph+=col.b*v;phs+=col.bp*v;phss+=col.bpp*v;phu+=col.b*vu;}
    }
    const st=Math.sin(th),ct=Math.cos(th),sp=Math.sin(ph),co=Math.cos(ph);
    const T=[-st*co,ct*co,sp],Dt=[-ct*co,-st*co,0],Dp=[st*sp,-ct*sp,co];
    const Dtt=[st*co,-ct*co,0],Dtp=[ct*sp,st*sp,0],Dttp=[-st*sp,ct*sp,0];
    const m=derivatives?rad.angles.length:0,out=new Float64Array(12*(m+1));
    for(let k=0;k<3;k++){
      out[k]=T[k];out[3+k]=Dt[k]*ths+Dp[k]*phs;
      out[6+k]=Dt[k]*thss+Dp[k]*phss+Dtt[k]*ths*ths+2*Dtp[k]*ths*phs-T[k]*phs*phs;
      out[9+k]=Dt[k]*thu+Dp[k]*phu;
    }
    if(!derivatives)return out;
    for(let j=0;j<m;j++){
      const col=rad.angles[j],v=col.b*q.f[col.k],vs=col.bp*q.f[col.k],vss=col.bpp*q.f[col.k],vu=col.b*q.fu[col.k],off=12*(j+1);
      for(let k=0;k<3;k++){
        let D,Ds,Dss,Du;
        if(col.kind===0){
          D=Dt[k];Ds=Dtt[k]*ths+Dtp[k]*phs;Du=Dtt[k]*thu+Dtp[k]*phu;
          Dss=Dtt[k]*thss+Dtp[k]*phss-Dt[k]*(ths*ths+phs*phs)+2*Dttp[k]*ths*phs;
        }else{
          D=Dp[k];Ds=Dtp[k]*ths-T[k]*phs;Du=Dtp[k]*thu-T[k]*phu;
          Dss=Dtp[k]*thss-T[k]*phss+Dttp[k]*ths*ths-2*Dt[k]*ths*phs-Dp[k]*phs*phs;
        }
        out[off+k]=D*v;out[off+3+k]=Ds*v+D*vs;
        out[off+6+k]=Dss*v+2*Ds*vs+D*vss;out[off+9+k]=Du*v+D*vu;
      }
    }
    return out;
  }
  function slice(s,parameters,derivatives=false){
    const z=Float64Array.from(parameters),rad=radial(s,z),m=derivatives?rad.angles.length:0,blocks=m+1,channels=9*blocks;
    const total=new Float64Array(channels),moment=new Float64Array(channels),prefix=Array.from({length:nq+1},()=>new Float64Array(channels));
    function addRecord(q,out,mo){
      const v=fill(rad,q,z,derivatives);
      for(let b=0;b<blocks;b++)for(let k=0;k<9;k++){
        const at=9*b+k,inc=q.weight*v[12*b+k];out[at]+=inc;if(mo)mo[at]+=(A-q.u)*inc;
      }
    }
    function integrateInterval(lo,hi,out,mo,wholeCellIndex){
      const cuts=bentReference.angularSubintervals(s,lo,hi);
      if(wholeCellIndex!==undefined&&cuts.length===2){for(const q of angleQuads[wholeCellIndex])addRecord(q,out,mo);return;}
      for(let h=1;h<cuts.length;h++){
        const width=cuts[h]-cuts[h-1];
        for(let k=0;k<8;k++)addRecord({...record(cuts[h-1]+width*G8.x[k]),weight:width*G8.w[k]},out,mo);
      }
    }
    for(let j=0;j<nq;j++){prefix[j].set(total);integrateInterval(j*du,(j+1)*du,total,moment,j);}
    prefix[nq].set(total);
    function atQuarter(u,nodeIndex){
      let sums,q;
      if(nodeIndex!==undefined){sums=prefix[nodeIndex];q=angleNodes[nodeIndex];}
      else{
        const i=Math.min(nq,Math.floor(u/du));sums=Float64Array.from(prefix[i]);q=record(u);
        if(i<nq)integrateInterval(i*du,u,sums,null);
      }
      const values=fill(rad,q,z,derivatives);
      const prim=(b,order)=>[0,1,2].map(k=>{
        const off=9*b+3*order+k;return sums[off]-(k===0?total[off]:k===2?moment[off]/A:0);
      });
      const p0={Y:prim(0,0),Ys:prim(0,1),Yss:prim(0,2),T:Array.from(values.slice(0,3)),Ts:Array.from(values.slice(3,6)),Tu:Array.from(values.slice(9,12))};
      function jets(a,as,ass,Y,Ys,Yss,T,Ts,Tu,Z,Zs,Zss){
        return {X:Y.map((v,k)=>a*v+(k===2?Z:0)),Xs:Y.map((v,k)=>as*v+a*Ys[k]+(k===2?Zs:0)),Xu:T.map(v=>a*v),
          Xss:Y.map((v,k)=>ass*v+2*as*Ys[k]+a*Yss[k]+(k===2?Zss:0)),Xsu:T.map((v,k)=>as*v+a*Ts[k]),Xuu:Tu.map(v=>a*v)};
      }
      const j=jets(rad.a,rad.as,rad.ass,p0.Y,p0.Ys,p0.Yss,p0.T,p0.Ts,p0.Tu,rad.Z,rad.Zs,rad.Zss);
      const variations=[],indices=[];
      if(derivatives){
        for(let b=1;b<blocks;b++){
          const off=12*b;
          variations.push(jets(rad.a,rad.as,rad.ass,prim(b,0),prim(b,1),prim(b,2),Array.from(values.slice(off,off+3)),Array.from(values.slice(off+3,off+6)),Array.from(values.slice(off+9,off+12)),0,0,0));
          indices.push(rad.angles[b-1].index);
        }
        for(const col of rad.heights){
          variations.push({X:[0,0,col.b],Xs:[0,0,col.bp],Xu:[0,0,0],Xss:[0,0,col.bpp],Xsu:[0,0,0],Xuu:[0,0,0]});indices.push(col.index);
        }
        for(const col of rad.radii){
          variations.push(jets(col.b,col.bp,col.bpp,p0.Y,p0.Ys,p0.Yss,p0.T,p0.Ts,p0.Tu,0,0,0));indices.push(col.index);
        }
      }
      return {jets:j,variations,indices,radial:rad};
    }
    function finish(packet,u,quadrant=0){
      if(quadrant){
        const R=[[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1]][quadrant],sign=quadrant%2?-1:1;
        const reflect=j=>Object.fromEntries(Object.entries(j).map(([key,v])=>[key,v.map((x,k)=>R[k]*x*((key==="Xu"||key==="Xsu")?sign:1))]));
        packet.jets=reflect(packet.jets);packet.variations=packet.variations.map(reflect);
      }
      const curv=algebra.curvature(packet.jets),hinge=algebra.hinge(curv.S,guide);
      const jacobian=derivatives?[new Float64Array(packet.indices.length),new Float64Array(packet.indices.length),new Float64Array(packet.indices.length)]:null;
      if(derivatives)for(let j=0;j<packet.indices.length;j++){
        const d=hinge.apply(algebra.variation(packet.jets,curv,packet.variations[j]));
        for(let k=0;k<3;k++)jacobian[k][j]=d[k];
      }
      const rE=curv.E-1,rF=curv.F/rad.a,rG=curv.G/(rad.a*rad.a)-1,h=(rE+rG)/2,rr=Math.hypot((rE-rG)/2,rF);
      return {s,u,jets:packet.jets,indices:packet.indices,jacobian,residual:hinge.residual,penaltySquared:hinge.squared,
        curvature:curv.kappa,principalCurvatures:curv.eigenvalues,orthonormalII:curv.S,
        relativeMetric:Math.max(Math.abs(h+rr),Math.abs(h-rr)),immersion:curv.w2/(rad.a*rad.a),
        threshold:hinge.threshold,parameterJets:derivatives?packet.variations:undefined};
    }
    return {node:j=>finish(atQuarter(j*du,j),j*du),point:u=>{
      const v=((u%(2*Math.PI))+2*Math.PI)%(2*Math.PI),quadrant=Math.min(3,Math.floor(v/A)),q=quadrant%2?(quadrant+1)*A-v:v-quadrant*A;
      return finish(atQuarter(Math.max(0,Math.min(A,q))),u,quadrant);
    }};
  }
  const cuts=Array.from(metricProvider.radialCuts);
  if(cuts[0]!==0||cuts[cuts.length-1]!==S||cuts.some((x,i)=>!Number.isFinite(x)||(i>0&&x<=cuts[i-1])))
    throw Error("Invalid shared physical radial quadrature cuts");
  const radialPoints=[];
  if(nodeShare>0)for(let i=0;i<cuts.length;i++){
    const h=(i?cuts[i]-cuts[i-1]:0)+(i+1<cuts.length?cuts[i+1]-cuts[i]:0);
    radialPoints.push({s:cuts[i],weight:nodeShare*h/(2*S),kind:"physical_knot"});
  }
  if(nodeShare<1)for(let i=1;i<cuts.length;i++){
    const lo=cuts[i-1],h=cuts[i]-lo;
    for(let j=0;j<2;j++)radialPoints.push({s:lo+h*G2.x[j],weight:(1-nodeShare)*h*G2.w[j]/S,kind:"cell_Gauss2"});
  }
  radialPoints.sort((a,b)=>a.s-b.s);
  function penalty(z,config={}){
    const need=!!config.jacobian||!!config.direction,rows=radialPoints.length*(nq+1)*3;
    const H=config.jacobian?new Float64Array(n*n):null,g=config.jacobian?new Float64Array(n):null;
    const residuals=config.residuals?new Float64Array(rows):null,jvp=config.direction?new Float64Array(rows):null;
    let squared=0,maxCurvature=0,minImmersion=Infinity,maxRelativeMetric=0,active=0,thresholds=0,worst=null;
    for(let ri=0;ri<radialPoints.length;ri++){
      const rp=radialPoints[ri],sl=slice(rp.s,z,false),activeNodes=[];
      for(let j=0;j<=nq;j++){
        const p=sl.node(j),aw=(j===0||j===nq?.5:1)/nq,w=weight*rp.weight*aw,off=(ri*(nq+1)+j)*3;
        squared+=w*p.penaltySquared;
        if(p.curvature>maxCurvature){maxCurvature=p.curvature;worst={s:rp.s,u:j*du,kind:rp.kind,principalCurvatures:p.principalCurvatures,relativeMetric:p.relativeMetric};}
        minImmersion=Math.min(minImmersion,p.immersion);maxRelativeMetric=Math.max(maxRelativeMetric,p.relativeMetric);
        if(p.threshold)thresholds++;
        if(residuals)for(let k=0;k<3;k++)residuals[off+k]=Math.sqrt(w)*p.residual[k];
        if(p.penaltySquared>0){active++;if(need)activeNodes.push({j,w,off});}
      }
      if(!activeNodes.length)continue;
      const sj=slice(rp.s,z,true);
      for(const {j,w,off}of activeNodes){
        const p=sj.node(j),m=p.indices.length;
        for(let a=0;a<m;a++){
          const ia=p.indices[a];let grad=0;
          for(let k=0;k<3;k++)grad+=p.jacobian[k][a]*p.residual[k];
          if(g)g[ia]+=w*grad;
          if(H)for(let b=0;b<=a;b++){
            const ib=p.indices[b];let value=0;
            for(let k=0;k<3;k++)value+=p.jacobian[k][a]*p.jacobian[k][b];
            H[ia*n+ib]+=w*value;if(ia!==ib)H[ib*n+ia]+=w*value;
          }
        }
        if(jvp)for(let k=0;k<3;k++){
          let v=0;for(let a=0;a<m;a++)v+=p.jacobian[k][a]*config.direction[p.indices[a]];
          jvp[off+k]=Math.sqrt(w)*v;
        }
      }
    }
    const out={squaredNorm:squared,norm:Math.sqrt(squared),maxCurvature,minImmersion,maxRelativeMetric,worst,
      activePoints:active,thresholdPoints:thresholds,rowCount:rows,radialPoints:radialPoints.length,quarterNodes:nq+1,guide,weight,nodeShare};
    if(H){out.H=H;out.g=g;}
    if(residuals)out.residuals=residuals;if(jvp)out.jvp=jvp;
    return out;
  }
  function evaluate(z,config={}){
    const old=metricProvider.evaluate(z,config),curv=penalty(z,config),out={...old};
    out.metricSquaredNorm=old.squaredNorm;out.curvaturePenaltySquaredNorm=curv.squaredNorm;
    out.squaredNorm=old.squaredNorm+curv.squaredNorm;out.norm=Math.sqrt(out.squaredNorm);
    out.rowCount=old.rowCount+curv.rowCount;out.curvature={...curv};delete out.curvature.H;delete out.curvature.g;delete out.curvature.residuals;delete out.curvature.jvp;
    if(config.jacobian){for(let i=0;i<n*n;i++)out.H[i]+=curv.H[i];for(let i=0;i<n;i++)out.g[i]+=curv.g[i];out.diagonal=Float64Array.from({length:n},(_,i)=>out.H[i*n+i]);}
    for(const key of ["residuals","jvp"])if(old[key]&&curv[key]){
      const v=new Float64Array(old[key].length+curv[key].length);v.set(old[key]);v.set(curv[key],old[key].length);out[key]=v;
    }
    out.curvatureIsNumericalGuide=true;out.continuousCertificate=false;out.strongTargetComplete=false;
    return out;
  }
  return {dimension:n,initialVector:()=>metricProvider.initialVector(),base,curve,bentReference,radialBasis,radialCuts:metricProvider.radialCuts,
    point:(s,u,z,config={})=>slice(s,z,!!config.jacobian).point(u),
    slice,penalty,evaluate,value:z=>evaluate(z),normal:z=>evaluate(z,{jacobian:true}),
    definition:{schema:"fd2d-R191-complete-true-curvature-hinge-finite-provider-v1",metricProvider:md,
      implementation:"R205 bent-annulus complete reference; unchanged R191 true-geometry and all original parameter jets",
      bentAnnulusReference:md.bentAnnulusReference,cutHeightSemantics:md.cutHeightSemantics,
      radialBasisDefinition:md.radialBasisDefinition,radialBlockLayout:md.radialBlockLayout,
      dimension:n,guide,weight,nodeShare,stateLayout:md.stateLayout,physicalMetricChangesWithRadius:designed,
      residual:"sqrt(weight*radialWeight*angularWeight)*(Q11,sqrt(2)Q12,Q22), Q=S-clip(S,[-guide,guide]); S is actual orthonormal II",
      radialSampling:"physical profile and B3 knots plus actual cell G2; shares declared and fixed",
      curvatureRadialPoints:radialPoints.length,quarterNodes:nq+1,
      derivatives:"All actual theta/phi/height/cut-height/radius columns via complete T/Ts/Tss/Tu and quarter primitives, actual Gram and normal; no DFT",
      angularThirdTensorsAreParameterDerivativesNotRadialC3Requirement:true,
      thresholdConvention:"inactive slope zero at exact guide; generalized derivative, not claimed smooth there",
      completeSquaredPenaltyEqualsSumPrincipalCurvatureHingesSquared:true,
      continuousMetricOrReachCertificate:false,strongTargetComplete:false}
  };
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR205CurvatureProvider};
