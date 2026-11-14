/* R201 + R205 fixed-amplitude full-half-period developed-tail adapter.
 * New explicit representation; frozen R201 flat source remains unchanged.
 * Frozen R196 rho/height/profile/basis and R191 Gram curvature formulas remain.
 * Mean-phase normalization and ALL parameter columns use complete angular Gauss-8.
 * Exact definition is R201; finite quadrature has no continuous remainder here.
 */
"use strict";
function createR201R205Provider(engine,metricProvider,reference,options={},algebra){
  if(!reference||typeof reference.angular!=="function"||typeof reference.heightCorrection!=="function"||typeof reference.angularSubintervals!=="function")throw Error("Explicit frozen R205 reference required");
  if(reference.definition?.schema!=="fd2d-R205-fixed-amplitude-bent-annulus-reference-v1")throw Error("Declared R205 fixed-amplitude definition required");
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
  const J=md.radialBasisCount,K=md.angularModes,N=md.fullEquivalentAngles,nq=N/2,A=Math.PI,du=A/nq;
  if(!designed)throw Error("R201 actual adapter explicitly requires the saved R190 designed-radius layout");
  const legacyDimension=metricProvider.dimension,extraWidth=2*K+1,extraStart=legacyDimension;
  const blocks=Array.from({length:J},(_,j)=>[
    ...Array.from({length:K},(_,k)=>j*K+k),
    ...Array.from({length:K},(_,k)=>J*K+j*K+k),
    2*J*K+j,2*J*K+J+1+j,
    ...Array.from({length:extraWidth},(_,k)=>extraStart+j*extraWidth+k)]);
  const layout={schema:"fd2d-R201-explicit-radial-blocks-v1",legacyDimension,
    appended:{start:extraStart,widthPerRadial:extraWidth,channelOrder:["theta constant","theta cosine 2..2K","psi cosine 2..2K"]},
    radialBlocks:blocks,globalBorder:2*J*K+J};
  const base=metricProvider.base,curve=metricProvider.curve,c=base.centralLength,S=base.end;
  const oldDimension=2*J*K+J+1,n=legacyDimension+J*extraWidth,cutIndex=oldDimension-1;
  if(legacyDimension!==oldDimension+J)throw Error("Wrong original/designed parameter layout");
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
  function record(u){
    const f=[],fu=[],fc=[],fcu=[];
    for(let k=1;k<=K;k++){f.push(Math.sin(2*k*u));fu.push(2*k*Math.cos(2*k*u));fc.push(Math.cos(2*k*u));fcu.push(-2*k*Math.sin(2*k*u));}
    return {u,g:curve.at(u),f,fu,fc,fcu,sn:Math.sin(u),cs:Math.cos(u)};
  }
  const angleNodes=Array.from({length:nq+1},(_,j)=>record(j*du));
  function splitRule(s,lo,hi){
    const cuts=reference.angularSubintervals(s,lo,hi),out=[];
    if(!Array.isArray(cuts)||cuts.length<2||cuts[0]!==lo||cuts[cuts.length-1]!==hi)throw Error("Exact supplied material subinterval endpoints required");
    for(let j=1;j<cuts.length;j++){
      const l=cuts[j-1],h=cuts[j]-l;if(h<0||!Number.isFinite(h))throw Error("Ordered angular partition required");
      if(h===0)continue;for(let k=0;k<G8.x.length;k++)out.push({...record(l+h*G8.x[k]),weight:h*G8.w[k]});
    }return out;
  }
  function radial(s,z){
    if(!Number.isFinite(s)||s<0||s>S||z.length!==n||Array.from(z).some(x=>!Number.isFinite(x)))throw Error("Invalid complete state or physical point");
    if(designed&&Math.max(...Array.from(z).slice(oldDimension,legacyDimension).map(Math.abs))>md.radiusCoefficientBound)throw Error("Outside original R190 radius domain");
    const p=base.at(s),w=engine.profileWeights(s,c,S),angles=[],heights=[],radii=[];
    const hc=reference.heightCorrection(s);
    let a=p.a,as=p.as,ass=p.ass,Z=p.z-hc.value,Zs=p.zs-hc.first,Zss=p.zss-hc.second;
    const radialJets=radialBasis.physicalJets(s,c,S);
    for(let rj=0;rj<radialJets.indices.length;rj++){
      const j=radialJets.indices[rj],b=radialJets.value[rj],bp=radialJets.first[rj],bpp=radialJets.second[rj];
      const hz=z[2*J*K+j];Z+=hz*b;Zs+=hz*bp;Zss+=hz*bpp;
      if(designed){const rr=z[oldDimension+j];a+=rr*b;as+=rr*bp;ass+=rr*bpp;}
      if(b===0&&bp===0&&bpp===0)continue;
      for(let k=0;k<K;k++){
        angles.push({index:j*K+k,kind:0,k,b,bp,bpp,trig:"sin"});
        angles.push({index:J*K+j*K+k,kind:1,k,b,bp,bpp,trig:"sin"});
        angles.push({index:extraStart+j*extraWidth+1+k,kind:0,k,b,bp,bpp,trig:"cos"});
        angles.push({index:extraStart+j*extraWidth+1+K+k,kind:1,k,b,bp,bpp,trig:"cos"});
      }
      angles.push({index:extraStart+j*extraWidth,kind:0,k:-1,b,bp,bpp,trig:"constant"});
      heights.push({index:2*J*K+j,b,bp,bpp});
      if(designed)radii.push({index:oldDimension+j,b,bp,bpp});
    }
    const sh=shape(s);Z+=z[cutIndex]*sh[0];Zs+=z[cutIndex]*sh[1];Zss+=z[cutIndex]*sh[2];
    if(sh.some(x=>x!==0))heights.push({index:cutIndex,b:sh[0],bp:sh[1],bpp:sh[2]});
    if(!(a>0))throw Error("Actual designed radius is not positive");
    return {s,p,w,a,as,ass,Z,Zs,Zss,angles,heights,radii};
  }
  function angular(col,q){return col.trig==="constant"?[1,0]:col.trig==="cos"?[q.fc[col.k],q.fcu[col.k]]:[q.f[col.k],q.fu[col.k]];}
  function rawAngles(rad,q,z){
    const {g,sn,cs}=q,w=rad.w,ex=-sn,ey=cs,dx=g.v[0]-ex,dy=g.v[1]-ey;
    const tx=ex+w.q*dx,ty=ey+w.q*dy,tz=w.r*g.h;
    const txs=w.qs*dx,tys=w.qs*dy,tzs=w.rs*g.h,txss=w.qss*dx,tyss=w.qss*dy,tzss=w.rss*g.h;
    const txu=-cs+w.q*(g.vu[0]+cs),tyu=-sn+w.q*(g.vu[1]+sn),tzu=w.r*g.hu;
    const cp2=tx*tx+ty*ty,cp=Math.sqrt(cp2);
    if(!(cp2>1e-15))throw Error("Saved reference seed angle chart is singular");
    const cr=tx*tys-ty*txs,hd=tx*txs+ty*tys;
    let th=q.u+Math.atan2(ex*ty-ey*tx,ex*tx+ey*ty),ph=Math.asin(Math.max(-1,Math.min(1,tz)));
    let ths=cr/cp2,phs=tzs/cp,thss=(tx*tyss-ty*txss)/cp2-2*hd*cr/(cp2*cp2),phss=tzss/cp-tzs*hd/(cp2*cp);
    let thu=(tx*tyu-ty*txu)/cp2,phu=tzu/cp;
    const bend=reference.angular(rad.s,q.u);
    th+=bend[0];ph+=bend[1];ths+=bend[2];phs+=bend[3];thss+=bend[4];phss+=bend[5];thu+=bend[6];phu+=bend[7];
    for(const col of rad.angles){
      const [f,fu]=angular(col,q),v=z[col.index]*f,vu=z[col.index]*fu;
      if(col.kind===0){th+=col.b*v;ths+=col.bp*v;thss+=col.bpp*v;thu+=col.b*vu;}
      else{ph+=col.b*v;phs+=col.bp*v;phss+=col.bpp*v;phu+=col.b*vu;}
    }
    return {th,ph,ths,phs,thss,phss,thu,phu};
  }
  const complexMul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];
  const complexDiv=(a,b)=>{const d=b[0]*b[0]+b[1]*b[1];return[(a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d];};
  function meanPhase(rad,z,derivatives){
    const m=derivatives?rad.angles.length:0,mean=new Float64Array(6),columns=new Float64Array(6*m);
    for(const cell of rad.angleQuads)for(const q of cell){
      const v=rawAngles(rad,q,z),c=Math.cos(v.ph),sn=Math.sin(v.ph),ps=v.phs,pss=v.phss,w=q.weight;
      const a=[c,sn,-sn*ps,c*ps,-c*ps*ps-sn*pss,-sn*ps*ps+c*pss];for(let k=0;k<6;k++)mean[k]+=w*a[k];
      if(derivatives)for(let j=0;j<m;j++){const col=rad.angles[j];if(col.kind!==1)continue;
        const f=angular(col,q)[0],p=col.b*f,sp=col.bp*f,ssp=col.bpp*f;
        const b=[-sn*p,c*p,-c*p*ps-sn*sp,-sn*p*ps+c*sp,
          sn*p*ps*ps-2*c*ps*sp-c*p*pss-sn*ssp,
          -c*p*ps*ps-2*sn*ps*sp-sn*p*pss+c*ssp];
        for(let k=0;k<6;k++)columns[6*j+k]+=w*b[k];
      }
    }
    const Z=[mean[0],mean[1]],Zs=[mean[2],mean[3]],Zss=[mean[4],mean[5]],R=Math.hypot(...Z);
    if(!(R>0&&Number.isFinite(R)))throw Error("R201 mean-phase chart R=0 or nonfinite");
    const r=complexDiv(Zs,Z),q=complexDiv(Zss,Z),rr=complexMul(r,r);
    const beta=Math.atan2(Z[1],Z[0]),bs=r[1],bss=q[1]-rr[1],B=new Float64Array(3*m);
    if(derivatives)for(let j=0;j<m;j++){
      const v=columns.subarray(6*j,6*j+6),t0=complexDiv([v[0],v[1]],Z),t1=complexDiv([v[2],v[3]],Z),t2=complexDiv([v[4],v[5]],Z),
        rt0=complexMul(r,t0),qt0=complexMul(q,t0),u=[t1[0]-rt0[0],t1[1]-rt0[1]],ru=complexMul(r,u);
      B[3*j]=t0[1];B[3*j+1]=u[1];B[3*j+2]=t2[1]-qt0[1]-2*ru[1];
    }
    return {C:Z[0],S:Z[1],R,beta,bs,bss,columns:B};
  }
  function fill(rad,q,z,derivatives){
    const raw=rawAngles(rad,q,z),phase=rad.phase;
    const th=raw.th,ph=raw.ph-phase.beta,ths=raw.ths,phs=raw.phs-phase.bs,thss=raw.thss,phss=raw.phss-phase.bss,thu=raw.thu,phu=raw.phu;
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
      const col=rad.angles[j],[f,fu]=angular(col,q),offset=col.kind===1?phase.columns.subarray(3*j,3*j+3):[0,0,0],
        v=col.b*f-offset[0],vs=col.bp*f-offset[1],vss=col.bpp*f-offset[2],vu=col.b*fu,off=12*(j+1);
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
    rad.angleQuads=Array.from({length:nq},(_,j)=>splitRule(s,j*du,(j+1)*du));
    rad.phase=meanPhase(rad,z,derivatives);
    const total=new Float64Array(channels),moment=new Float64Array(channels),prefix=Array.from({length:nq+1},()=>new Float64Array(channels));
    function addRecord(q,out,mo){
      const v=fill(rad,q,z,derivatives);
      for(let b=0;b<blocks;b++)for(let k=0;k<9;k++){
        const at=9*b+k,inc=q.weight*v[12*b+k];out[at]+=inc;if(mo)mo[at]+=(A-q.u)*inc;
      }
    }
    for(let j=0;j<nq;j++){prefix[j].set(total);for(const q of rad.angleQuads[j])addRecord(q,total,moment);}
    prefix[nq].set(total);
    function atHalf(u,nodeIndex){
      let sums,q;
      if(nodeIndex!==undefined){sums=prefix[nodeIndex];q=angleNodes[nodeIndex];}
      else{
        const i=Math.min(nq,Math.floor(u/du));sums=Float64Array.from(prefix[i]);q=record(u);
        if(i<nq)for(const q of splitRule(s,i*du,u))addRecord(q,sums,null);
      }
      const values=fill(rad,q,z,derivatives);
      const prim=(b,order)=>[0,1,2].map(k=>{
        const off=9*b+3*order+k;return sums[off]-(k<2?total[off]/2:moment[off]/A);
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
        const R=[-1,-1,1],rotate=j=>Object.fromEntries(Object.entries(j).map(([key,v])=>[key,v.map((x,k)=>R[k]*x)]));
        packet.jets=rotate(packet.jets);packet.variations=packet.variations.map(rotate);
      }
      const curv=algebra.curvature(packet.jets),hinge=algebra.hinge(curv.S,guide);
      const jacobian=derivatives?[new Float64Array(packet.indices.length),new Float64Array(packet.indices.length),new Float64Array(packet.indices.length)]:null;
      if(derivatives)for(let j=0;j<packet.indices.length;j++){
        const d=hinge.apply(algebra.variation(packet.jets,curv,packet.variations[j]));
        for(let k=0;k<3;k++)jacobian[k][j]=d[k];
      }
      const rE=curv.E-1,rF=curv.F/rad.a,rG=curv.G/(rad.a*rad.a)-1,h=(rE+rG)/2,rr=Math.hypot((rE-rG)/2,rF);
      return {s,u,a:rad.a,phase:{C:rad.phase.C,S:rad.phase.S,R:rad.phase.R},jets:packet.jets,indices:packet.indices,jacobian,residual:hinge.residual,penaltySquared:hinge.squared,
        curvature:curv.kappa,principalCurvatures:curv.eigenvalues,orthonormalII:curv.S,
        relativeMetric:Math.max(Math.abs(h+rr),Math.abs(h-rr)),immersion:curv.w2/(rad.a*rad.a),
        threshold:hinge.threshold,parameterJets:derivatives?packet.variations:undefined};
    }
    return {node:j=>finish(atHalf(j*du,j),j*du),point:u=>{
      const v=((u%(2*Math.PI))+2*Math.PI)%(2*Math.PI),half=v>=Math.PI?1:0,q=v-half*Math.PI;
      return finish(atHalf(Math.max(0,Math.min(A,q))),u,half);
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
      activePoints:active,thresholdPoints:thresholds,rowCount:rows,radialPoints:radialPoints.length,halfNodes:nq+1,guide,weight,nodeShare};
    if(H){out.H=H;out.g=g;}
    if(residuals)out.residuals=residuals;if(jvp)out.jvp=jvp;
    return out;
  }
  const metricPoints=[];
  for(let i=1;i<cuts.length;i++){const lo=cuts[i-1],h=cuts[i]-lo;for(let j=0;j<2;j++)metricPoints.push({s:lo+h*G2.x[j],weight:h*G2.w[j]/S});}
  function metric(z,config={}){
    const derivatives=!!config.jacobian||!!config.direction, H=config.jacobian?new Float64Array(n*n):null,g=config.jacobian?new Float64Array(n):null,
      rows=metricPoints.length*(nq+1)*2,res=config.residuals?new Float64Array(rows):null,jvp=config.direction?new Float64Array(rows):null;
    let squared=0,maxRelativeMetric=0,minImmersion=Infinity,worst=null,index=0,minMeanR=Infinity;
    for(const rp of metricPoints){
      const sl=slice(rp.s,z,derivatives);
      for(let j=0;j<=nq;j++){
        const p=sl.node(j),a=p.a,T=p.jets.Xu.map(v=>v/a),V=p.jets.Xs,rE=dot(V,V)-1,rF=dot(V,T),aw=(j===0||j===nq?.5:1)/nq,w=rp.weight*aw;
        squared+=w*(rE*rE+2*rF*rF);minImmersion=Math.min(minImmersion,p.immersion);minMeanR=Math.min(minMeanR,p.phase.R);
        if(p.relativeMetric>maxRelativeMetric){maxRelativeMetric=p.relativeMetric;worst={s:rp.s,u:j*du,rE,rF};}
        if(res){res[index]=Math.sqrt(w)*rE;res[index+1]=Math.sqrt(2*w)*rF;}
        if(derivatives){
          const e=new Float64Array(p.indices.length),f=new Float64Array(p.indices.length);
          for(let k=0;k<p.indices.length;k++){
            const v=p.parameterJets[k],col=p.indices[k],da=col>=oldDimension&&col<legacyDimension?dot(v.Xu,T):0;
            const dT=v.Xu.map((x,i)=>(x-da*T[i])/a);
            e[k]=2*dot(V,v.Xs);f[k]=dot(v.Xs,T)+dot(V,dT);
          }
          for(let k=0;k<p.indices.length;k++){
            const ik=p.indices[k];if(g)g[ik]+=w*(e[k]*rE+2*f[k]*rF);
            if(H)for(let l=0;l<=k;l++){const il=p.indices[l],v=w*(e[k]*e[l]+2*f[k]*f[l]);H[ik*n+il]+=v;if(ik!==il)H[il*n+ik]+=v;}
          }
          if(jvp){let de=0,df=0;for(let k=0;k<p.indices.length;k++){de+=e[k]*config.direction[p.indices[k]];df+=f[k]*config.direction[p.indices[k]];}
            jvp[index]=Math.sqrt(w)*de;jvp[index+1]=Math.sqrt(2*w)*df;}
        }
        index+=2;
      }
    }
    const out={squaredNorm:squared,norm:Math.sqrt(squared),maxRelativeMetric,minImmersion,minMeanR,worst,rowCount:rows,radialPoints:metricPoints.length,halfNodes:nq+1,fullEquivalentAngles:N,continuousCertificate:false};
    if(H){out.H=H;out.g=g;}if(res)out.residuals=res;if(jvp)out.jvp=jvp;return out;
  }
  function evaluate(z,config={}){
    const met=metric(z,config),curv=penalty(z,config),out={...met,metricSquaredNorm:met.squaredNorm,curvaturePenaltySquaredNorm:curv.squaredNorm};
    out.squaredNorm=met.squaredNorm+curv.squaredNorm;out.norm=Math.sqrt(out.squaredNorm);out.rowCount=met.rowCount+curv.rowCount;
    out.curvature={...curv};for(const k of["H","g","residuals","jvp"])delete out.curvature[k];
    if(config.jacobian){for(let i=0;i<n*n;i++)out.H[i]+=curv.H[i];for(let i=0;i<n;i++)out.g[i]+=curv.g[i];out.diagonal=Float64Array.from({length:n},(_,i)=>out.H[i*n+i]);}
    for(const key of["residuals","jvp"])if(met[key]&&curv[key]){const v=new Float64Array(met[key].length+curv[key].length);v.set(met[key]);v.set(curv[key],met[key].length);out[key]=v;}
    out.curvatureIsNumericalGuide=true;out.continuousCertificate=false;out.strongTargetComplete=false;return out;
  }
  function injectLegacy(z){if(z.length!==legacyDimension)throw Error("Legacy dimension mismatch");const p=new Float64Array(n);p.set(z);return p;}
  return {dimension:n,initialVector:()=>injectLegacy(metricProvider.initialVector()),injectLegacy,
    base,curve,radialBasis,radialCuts:metricProvider.radialCuts,metric,penalty,evaluate,value:z=>evaluate(z),normal:z=>evaluate(z,{jacobian:true}),
    point:(s,u,z,config={})=>slice(s,z,!!config.jacobian).point(u),slice,
    definition:{schema:"fd2d-R201-R205-full-half-developed-tail-curvature-provider-v1",parentMetric:md,
      dimension:n,legacyDimension,radialBasisCount:J,angularModes:K,fullEquivalentAngles:N,halfNodes:nq+1,
      radialBlockLayout:layout,radialBasisDefinition:md.radialBasisDefinition,stateLayout:{legacy:md.stateLayout,appended:layout.appended},
      meanPhase:"Complete half-period C+iS integral, algebraic rotation; derivatives include beta_p,beta_sp,beta_ssp",
      primitive:"R201 full half-period zero-full-mean kernels, Gauss8 split at every R205 frozen-base angular clip; no quarter reflection",
      developedTailReference:reference.definition,amplitudeMode:"Fixed external design parameter, not an omitted state column",
      cutHeightMeaning:"Inner flat-cuff Zc=original base.height+cut coefficient; outer mean subtracts complete R205 section mean",
      guide,weight,nodeShare,radiusCoefficientBound:md.radiusCoefficientBound,physicalMetricChangesWithRadius:true,
      exactLegacyInjection:"Copy R205 D2 coefficients and append zeros; exact same developed reference, odd phase S=0, C>0. Copying an old flat state instead is an explicitly new baseline.",
      cutAndCentral:"R205 complete raw angular and mean-height twojets, zero-twojet state corrections; R201 theorem applies at the developed outer cut",
      parameterJets:"All theta sin/cos/constant, psi sin/cos, height, cut height and rho; fixed physical s,u",
      radialLocality:"Mean phase couples angles at fixed s only; exact local radial block support preserved",
      finiteQuadratureRemainderPaid:false,continuousMetricOrReachCertificate:false,strongTargetComplete:false}
  };
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR201R205Provider};
