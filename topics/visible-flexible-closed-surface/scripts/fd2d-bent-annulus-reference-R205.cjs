/* R205: exact-form bent developable annulus reference for direct position.
 * The fixed design amplitude is not the orbit time. All integrals are stated
 * mathematical primitives; this implementation evaluates them by finite GL.
 */
"use strict";
function createR205BentAnnulusReference(engine,base,options={}){
  const amplitude=options.amplitude===undefined?1:options.amplitude;
  const cuffRadius=8/25,flatRadius=17/50,cutRadius=4/5,width=cutRadius-flatRadius;
  const c=base.centralLength,S=base.end,N=options.angles||64,quarter=Math.PI/2,nq=N/4,du=quarter/nq;
  if(!(amplitude>=0&&amplitude<=6/5)||!Number.isFinite(amplitude))throw Error("R205 fixed amplitude requires 0<=A<=6/5");
  if(N%4||N<16)throw Error("R205 angular count must be a multiple of four");
  if(!(S>c&&c>0))throw Error("R205 needs the complete positive central cylinder and endpoint");
  const endpoint=base.at(S);
  if(Math.abs(endpoint.a-cutRadius)>2e-13||Math.abs(endpoint.as+1)>2e-12||Math.abs(endpoint.ass)>2e-11)
    throw Error("R205 requires the explicit B32 endpoint (4/5,-1,0)");
  const G8=engine.gauss(8),G64=engine.gauss(64);
  const angularCache=new Map(),heightCache=new Map();
  const cacheLimit=options.cacheLimit===undefined?120000:options.cacheLimit;
  if(!Number.isInteger(cacheLimit)||cacheLimit<0)throw Error("Nonnegative integer cacheLimit required");
  let cacheHits=0,cacheMisses=0;
  function memo(cache,key,fn,limit){
    if(cache.has(key)){cacheHits++;return cache.get(key);}
    cacheMisses++;const value=fn();
    if(limit){if(cache.size>=limit)cache.delete(cache.keys().next().value);cache.set(key,value);}
    return value;
  }
  function step(t){
    if(t<=0)return [0,0,0];
    if(t>=1)return [1,0,0];
    return [t**5*(126+t*(-420+t*(540+t*(-315+70*t)))),
      630*t**4*(1-t)**4,2520*t**3*(1-t)**3*(1-2*t)];
  }
  function blend(s){
    if(s<=c)return [0,0,0];
    if(s>=S)return [1,0,0];
    const L=S-c,t=(s-c)/L;
    return [t*t*t*(10+t*(-15+6*t)),30*t*t*(1-t)*(1-t)/L,
      60*t*(1-t)*(1-2*t)/(L*L)];
  }
  // First dual component is the true derivative with respect to the fixed
  // external amplitude, useful for an explicit outer design continuation.
  const D=(v,d=0)=>[v,d],add=(a,b)=>[a[0]+b[0],a[1]+b[1]],
    sub=(a,b)=>[a[0]-b[0],a[1]-b[1]],mul=(a,b)=>[a[0]*b[0],a[1]*b[0]+a[0]*b[1]],
    scale=(a,k)=>[a[0]*k,a[1]*k],div=(a,b)=>[a[0]/b[0],(a[1]*b[0]-a[0]*b[1])/(b[0]*b[0])],
    sin=a=>[Math.sin(a[0]),Math.cos(a[0])*a[1]],cos=a=>[Math.cos(a[0]),-Math.sin(a[0])*a[1]],
    sqrt=a=>{const v=Math.sqrt(a[0]);return[v,a[1]/(2*v)];},
    atan2=(y,x)=>[Math.atan2(y[0],x[0]),(x[0]*y[1]-y[0]*x[1])/(x[0]*x[0]+y[0]*y[0])];
  function local(s,u){
    const p=base.at(s),sn=Math.sin(u),cs=Math.cos(u),sign=Math.sign(sn),j=step((Math.abs(p.a*sn)-flatRadius)/width);
    const alpha=D(sign*amplitude*j[0],sign*j[0]),k=D(amplitude*j[1]/width,j[1]/width),
      ky=D(sign*amplitude*j[2]/(width*width),sign*j[2]/(width*width));
    const alphas=scale(k,p.as*sn),alphass=add(scale(ky,p.as*p.as*sn*sn),scale(k,p.ass*sn)),
      alphau=scale(k,p.a*cs),ca=cos(alpha),sa=sin(alpha);
    const tx=D(-sn),ty=scale(ca,cs),tz=scale(sa,-cs),
      tys=scale(mul(sa,alphas),-cs),tzs=scale(mul(ca,alphas),-cs),
      tyss=scale(add(mul(ca,mul(alphas,alphas)),mul(sa,alphass)),-cs),
      tzss=scale(sub(mul(sa,mul(alphas,alphas)),mul(ca,alphass)),cs),
      txu=D(-cs),tyu=sub(scale(ca,-sn),scale(mul(sa,alphau),cs)),
      tzu=sub(scale(sa,sn),scale(mul(ca,alphau),cs));
    const cp2=add(mul(tx,tx),mul(ty,ty)),cp=sqrt(cp2);
    if(!(cp2[0]>0))throw Error("R205 reference angle chart is singular");
    const cr=mul(tx,tys),hd=mul(ty,tys);
    const theta=atan2(sub(scale(ty,-sn),scale(tx,cs)),add(scale(tx,-sn),scale(ty,cs))),phi=atan2(tz,cp);
    const ths=div(cr,cp2),phs=div(tzs,cp),
      thss=sub(div(mul(tx,tyss),cp2),scale(div(mul(hd,cr),mul(cp2,cp2)),2)),
      phss=sub(div(tzss,cp),div(mul(tzs,hd),mul(cp2,cp))),
      thu=sub(div(sub(mul(tx,tyu),mul(ty,txu)),cp2),D(1)),
      phu=div(tzu,cp);
    return {p,angles:[theta,phi,ths,phs,thss,phss,thu,phu],tz,tzs,tzss};
  }
  function angular(s,u){
    if(!Number.isFinite(s)||s<0||s>S||!Number.isFinite(u))throw Error("R205 angular reference expects the physical prefix and a finite material angle");
    return memo(angularCache,s+"|"+u,()=>{
      const chi=blend(s),out=new Float64Array(16);
      if(chi.every(v=>v===0))return out;
      const q=local(s,u).angles;
      for(let d=0;d<2;d++){
        const at=d*8;
        out[at]=chi[0]*q[0][d];out[at+1]=chi[0]*q[1][d];
        out[at+2]=chi[1]*q[0][d]+chi[0]*q[2][d];
        out[at+3]=chi[1]*q[1][d]+chi[0]*q[3][d];
        out[at+4]=chi[2]*q[0][d]+2*chi[1]*q[2][d]+chi[0]*q[4][d];
        out[at+5]=chi[2]*q[1][d]+2*chi[1]*q[3][d]+chi[0]*q[5][d];
        out[at+6]=chi[0]*q[6][d];out[at+7]=chi[0]*q[7][d];
      }
      return out;
    },cacheLimit);
  }
  function angularSubintervals(s,lo,hi){
    if(!(lo>=0&&hi<=2*Math.PI&&hi>=lo))throw Error("Invalid material integration interval in [0,2pi]");
    const radius=base.at(s).a,cuts=[lo,hi];
    for(const y of [flatRadius,cutRadius])if(y<radius){
      const u=Math.asin(y/radius);
      for(const q of [u,Math.PI-u,Math.PI+u,2*Math.PI-u])if(q>lo&&q<hi)cuts.push(q);
    }
    cuts.sort((a,b)=>a-b);return cuts;
  }
  function heightCorrection(s){
    if(!Number.isFinite(s)||s<0||s>S)throw Error("R205 height reference outside prefix");
    return memo(heightCache,s,()=>{
      const chi=blend(s),out={value:0,first:0,second:0,amplitude:[0,0,0],rawMean:[0,0,0]};
      if(chi.every(v=>v===0))return out;
      const p=base.at(s),m=[D(0),D(0),D(0)];
      for(let j=0;j<nq;j++){
        const pieces=angularSubintervals(s,j*du,(j+1)*du);
        for(let h=1;h<pieces.length;h++)for(let k=0;k<8;k++){
          const width=pieces[h]-pieces[h-1],u=pieces[h-1]+width*G8.x[k],w=width*G8.w[k]*(quarter-u),q=local(s,u);
          m[0]=add(m[0],scale(q.tz,w));m[1]=add(m[1],scale(q.tzs,w));m[2]=add(m[2],scale(q.tzss,w));
        }
      }
      const mean=scale(m[0],-p.a/quarter),
        first=scale(add(scale(m[0],p.as),scale(m[1],p.a)),-1/quarter),
        second=scale(add(add(scale(m[0],p.ass),scale(m[1],2*p.as)),scale(m[2],p.a)),-1/quarter);
      const values=scale(mean,chi[0]),
        ds=add(scale(mean,chi[1]),scale(first,chi[0])),
        dss=add(add(scale(mean,chi[2]),scale(first,2*chi[1])),scale(second,chi[0]));
      return {value:values[0],first:ds[0],second:dss[0],amplitude:[values[1],ds[1],dss[1]],rawMean:[mean[0],first[0],second[0]]};
    },Math.max(1,Math.floor(cacheLimit/128)));
  }
  function curve(y){
    if(!Number.isFinite(y))throw Error("Finite tail generating coordinate required");
    const sign=Math.sign(y),abs=Math.abs(y),end=Math.min(Math.max(abs-flatRadius,0),width);
    let dx=0,H=0,dxA=0,HA=0;
    for(let j=0;j<G64.x.length;j++){
      const q=end*G64.x[j],st=step(q/width)[0],alpha=amplitude*st,w=end*G64.w[j];
      dx+=w*(-2*Math.sin(alpha/2)**2);H+=w*Math.sin(alpha);
      dxA-=w*Math.sin(alpha)*st;HA+=w*Math.cos(alpha)*st;
    }
    const beyond=Math.max(abs-cutRadius,0);
    dx+=beyond*(Math.cos(amplitude)-1);H+=beyond*Math.sin(amplitude);
    dxA-=beyond*Math.sin(amplitude);HA+=beyond*Math.cos(amplitude);
    const st=step((abs-flatRadius)/width),alpha=sign*amplitude*st[0],
      alphaA=sign*st[0],k=amplitude*st[1]/width,kA=st[1]/width;
    return {X:y+sign*dx,H,XA:sign*dxA,HA,alpha,alphaA,k,kA,ky:sign*amplitude*st[2]/(width*width)};
  }
  function tailPoint(r,u,Zc=0){
    if(!(r>=cuffRadius&&r<=cutRadius)||!Number.isFinite(u)||!Number.isFinite(Zc))throw Error("Actual annulus domain required");
    const sn=Math.sin(u),cs=Math.cos(u),q=curve(r*sn),ca=Math.cos(q.alpha),sa=Math.sin(q.alpha),
      T=[0,ca,-sa],Nt=[0,-sa,-ca],Ty=Nt.map(v=>q.k*v),TA=Nt.map(v=>q.alphaA*v),
      NA=T.map(v=>-q.alphaA*v),TyA=Nt.map((v,i)=>q.kA*v+q.k*NA[i]);
    const X=[r*cs,q.X,Zc-q.H],Xr=[cs,sn*ca,-sn*sa],Xu=[-r*sn,r*cs*ca,-r*cs*sa];
    const Xrr=Ty.map(v=>sn*sn*v),
      Xru=[-sn,0,0]; // Filled componentwise below; avoids singular polar inverses.
    for(let i=1;i<3;i++)Xru[i]=cs*T[i]+r*sn*cs*Ty[i];
    const Xuu=[-r*cs,0,0];
    for(let i=1;i<3;i++)Xuu[i]=-r*sn*T[i]+r*r*cs*cs*Ty[i];
    const dX=[0,q.XA,-q.HA],dXr=TA.map(v=>sn*v),dXu=TA.map(v=>r*cs*v),
      dXrr=TyA.map(v=>sn*sn*v),dXru=TA.map((v,i)=>cs*v+r*sn*cs*TyA[i]),
      dXuu=TA.map((v,i)=>-r*sn*v+r*r*cs*cs*TyA[i]);
    return {jets:{X,Xs:Xr.map(v=>-v),Xu,Xss:Xrr,Xsu:Xru.map(v=>-v),Xuu},
      amplitudeJets:{X:dX,Xs:dXr.map(v=>-v),Xu:dXu,Xss:dXrr,Xsu:dXru.map(v=>-v),Xuu:dXuu},
      n:q.k*cs*cs,m:-q.k*sn*cs,l:q.k*sn*sn,curvature:q.k,cuffPlaneHeight:Zc};
  }
  function completeReferenceAngles(s,u,curve){
    if(!curve||typeof curve.at!=="function")throw Error("Explicit same central curve required");
    const g=curve.at(u),w=engine.profileWeights(s,c,S),sn=Math.sin(u),cs=Math.cos(u),
      ex=-sn,ey=cs,dx=g.v[0]-ex,dy=g.v[1]-ey;
    const tx=ex+w.q*dx,ty=ey+w.q*dy,tz=w.r*g.h,
      txs=w.qs*dx,tys=w.qs*dy,tzs=w.rs*g.h,
      txss=w.qss*dx,tyss=w.qss*dy,tzss=w.rss*g.h,
      txu=-cs+w.q*(g.vu[0]+cs),tyu=-sn+w.q*(g.vu[1]+sn),tzu=w.r*g.hu;
    const cp2=tx*tx+ty*ty,cp=Math.sqrt(cp2),cr=tx*tys-ty*txs,hd=tx*txs+ty*tys;
    if(!(cp2>1e-15))throw Error("The original complete reference angle chart is singular");
    const old=[u+Math.atan2(ex*ty-ey*tx,ex*tx+ey*ty),Math.asin(Math.max(-1,Math.min(1,tz))),
      cr/cp2,tzs/cp,(tx*tyss-ty*txss)/cp2-2*hd*cr/(cp2*cp2),
      tzss/cp-tzs*hd/(cp2*cp),(tx*tyu-ty*txu)/cp2,tzu/cp],
      bend=angular(s,u),values=old.map((v,j)=>v+bend[j]);
    return {theta:values[0],phi:values[1],theta_s:values[2],phi_s:values[3],
      theta_ss:values[4],phi_ss:values[5],theta_u:values[6],phi_u:values[7],
      values,amplitude:Array.from(bend.slice(8))};
  }
  function tailTangentJets(r,u,radialFirst=-1,radialSecond=0){
    if(!(r>=cuffRadius&&r<=cutRadius)||![u,radialFirst,radialSecond].every(Number.isFinite))throw Error("Actual tail tangent domain required");
    const sn=Math.sin(u),cs=Math.cos(u),q=curve(r*sn),sa=Math.sin(q.alpha),ca=Math.cos(q.alpha),
      alphas=q.k*radialFirst*sn,alphass=q.ky*radialFirst*radialFirst*sn*sn+q.k*radialSecond*sn,
      alphau=q.k*r*cs;
    return {T:[-sn,ca*cs,-sa*cs],
      Ts:[0,-sa*alphas*cs,-ca*alphas*cs],
      Tss:[0,-(ca*alphas*alphas+sa*alphass)*cs,(sa*alphas*alphas-ca*alphass)*cs],
      Tu:[-cs,-ca*sn-sa*alphau*cs,sa*sn-ca*alphau*cs]};
  }
  function cutSectionMeanJets(Zc){
    if(!Number.isFinite(Zc))throw Error("Finite actual cuff plane height required");
    const q=heightCorrection(S);
    return {value:Zc-q.value,first:-q.first,second:-q.second,
      cuffHeightParameterJets:[1,0,0],amplitude:q.amplitude.map(v=>-v)};
  }
  return {amplitude,angular,angularSubintervals,heightCorrection,completeReferenceAngles,
    tailPoint,tailTangentJets,cutSectionMeanJets,curve,
    statistics:()=>({angularEntries:angularCache.size,heightEntries:heightCache.size,cacheHits,cacheMisses}),
    definition:{schema:"fd2d-R205-fixed-amplitude-bent-annulus-reference-v1",amplitude,
      cuffRadius,flatRadius,cutRadius,alpha:"sgn(y)*A*S9((abs(y)-17/50)/(23/50)), clipped",
      amplitudeRange:[0,6/5],referenceRadialDependency:"the frozen B32 base a(s), a_s(s), a_ss(s); excludes radius-design coefficients",
      blend:"S5((s-c)/(S-c)), with exact constant extensions and zero endpoint first two jets",
      angleAddition:"chi*(theta_tail(a_base(s),u)-u, phi_tail(a_base(s),u)); relative theta uses positive-dot atan2, so full periodic angles are explicit",
      centerHeightSubtraction:"chi*mean_u Z_A(a_base(s)*sin(u)); complete s0-s2 jets included",
      cuffPlaneHeight:"base.height + saved cutHeight coefficient; outer cut mean is this minus mean Z_A",
      primitive:"complete quarter-cell Gauss8 split additionally at a_base(s)*sin(u)=17/50 or 4/5; same exact integrals, boundaries independent of all finite parameters",
      fullEquivalentAngles:N,angularCacheLimit:cacheLimit,
      externalAmplitudeDerivative:"angular entries 8..15 and heightCorrection.amplitude are exact-form first amplitude derivatives; A is frozen in finite state",
      tailPositionIntegral:"Gauss64 in normalized y with exact saturated-ray extension",
      continuousCertificate:false,wholePrefixSolved:false}
  };
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR205BentAnnulusReference};
