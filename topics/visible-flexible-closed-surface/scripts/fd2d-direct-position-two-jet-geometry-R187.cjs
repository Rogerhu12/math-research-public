/* Independent actual position 0--2 jets for the R187/R188 provider.
 * Complete angle functions and quarter Gauss8 primitives; no DFT.
 * Finite quadrature/samples are not continuous geometric certificates.
 */
"use strict";
function createR187Geometry(engine,provider){
  const def=provider.definition,base=provider.base,curve=provider.curve;
  if(def.schema!=="fd2d-R187-C2-direct-position-two-angle-finite-provider-v1")
    throw Error("Explicit R187 two-angle provider required");
  const J=def.radialBasisCount,K=def.angularModes,N=def.fullEquivalentAngles;
  const n=provider.dimension,nq=N/4,A=Math.PI/2,du=A/nq,c=base.centralLength,S=base.end,step=(S-c)/(J+3);
  if(n!==2*J*K+J+1||nq!==Math.floor(nq))throw Error("Wrong explicit parameter layout");
  const G8=engine.gauss(8);
  const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
  const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
  const add=(a,b)=>a.map((v,j)=>v+b[j]);
  function cubic(t){
    const a=Math.abs(t),sg=t<0?-1:1;
    if(a>=2)return [0,0,0];
    if(a<1)return [(4-6*a*a+3*a*a*a)/6,sg*(-12*a+9*a*a)/6,(-12+18*a)/6];
    return [(2-a)**3/6,-sg*(2-a)**2/2,2-a];
  }
  function centerShape(s){
    if(s<=c)return [0,0,0];
    if(s>=S)return [1,0,0];
    const t=(s-c)/(S-c),L=S-c;
    return [t*t*t*(10+t*(-15+6*t)),30*t*t*(1-t)*(1-t)/L,60*t*(1-t)*(1-2*t)/(L*L)];
  }
  function radial(s,z){
    if(!Number.isFinite(s)||s<0||s>S)throw Error("Outside the declared physical prefix");
    if(z.length!==n||Array.from(z).some(x=>!Number.isFinite(x)))throw Error("Wrong/nonfinite actual state");
    const p=base.at(s),w=engine.profileWeights(s,c,S),basis=[];
    let Z=p.z,Zs=p.zs,Zss=p.zss;
    for(let j=0;j<J;j++){
      const [b,bt,btt]=cubic((s-(c+(j+2)*step))/step),bp=bt/step,bpp=btt/(step*step);
      basis.push([b,bp,bpp]);
      // Position includes height B_j even where B'_j is zero. The metric
      // provider legitimately omits those columns from X_s at that point.
      const q=z[2*J*K+j];Z+=q*b;Zs+=q*bp;Zss+=q*bpp;
    }
    const sh=centerShape(s),height=z[n-1];
    Z+=height*sh[0];Zs+=height*sh[1];Zss+=height*sh[2];
    return {s,p,w,basis,Z,Zs,Zss};
  }
  function angles(rad,u,z){
    const g=curve.at(u),sn=Math.sin(u),cs=Math.cos(u),ex=-sn,ey=cs;
    const euux=-cs,euuy=-sn,dx=g.v[0]-ex,dy=g.v[1]-ey,w=rad.w;
    const tx=ex+w.q*dx,ty=ey+w.q*dy,tz=w.r*g.h;
    const txs=w.qs*dx,tys=w.qs*dy,tzs=w.rs*g.h;
    const txss=w.qss*dx,tyss=w.qss*dy,tzss=w.rss*g.h;
    const txu=euux+w.q*(g.vu[0]-euux),tyu=euuy+w.q*(g.vu[1]-euuy),tzu=w.r*g.hu;
    const cp2=tx*tx+ty*ty,cp=Math.sqrt(cp2);
    if(!(cp2>1e-15))throw Error("The declared reference angle chart is singular");
    const angularCross=tx*tys-ty*txs,horizontalDot=tx*txs+ty*tys;
    let th=u+Math.atan2(ex*ty-ey*tx,ex*tx+ey*ty),ph=Math.asin(Math.max(-1,Math.min(1,tz)));
    let ths=angularCross/cp2,phs=tzs/cp;
    let thss=(tx*tyss-ty*txss)/cp2-2*horizontalDot*angularCross/(cp2*cp2);
    let phss=tzss/cp-tzs*horizontalDot/(cp2*cp);
    let thu=(tx*tyu-ty*txu)/cp2,phu=tzu/cp;
    for(let j=0;j<J;j++){
      const [b,bp,bpp]=rad.basis[j];
      if(b===0&&bp===0&&bpp===0)continue;
      for(let k=1;k<=K;k++){
        const f=Math.sin(2*k*u),fu=2*k*Math.cos(2*k*u);
        const q=z[j*K+k-1],r=z[J*K+j*K+k-1];
        th+=b*q*f;ths+=bp*q*f;thss+=bpp*q*f;thu+=b*q*fu;
        ph+=b*r*f;phs+=bp*r*f;phss+=bpp*r*f;phu+=b*r*fu;
      }
    }
    const st=Math.sin(th),ct=Math.cos(th),sp=Math.sin(ph),co=Math.cos(ph);
    const T=[-st*co,ct*co,sp],Dt=[-ct*co,-st*co,0],Dp=[st*sp,-ct*sp,co];
    const Dtt=[st*co,-ct*co,0],Dtp=[ct*sp,st*sp,0];
    const Ts=T.map((v,k)=>Dt[k]*ths+Dp[k]*phs);
    const Tu=T.map((v,k)=>Dt[k]*thu+Dp[k]*phu);
    const Tss=T.map((v,k)=>Dt[k]*thss+Dp[k]*phss+Dtt[k]*ths*ths+2*Dtp[k]*ths*phs-v*phs*phs);
    return {T,Ts,Tss,Tu,theta:th,phi:ph,theta_s:ths,phi_s:phs,theta_ss:thss,phi_ss:phss,theta_u:thu,phi_u:phu};
  }
  function geometry(p,X,Xs,Xu,Xss,Xsu,Xuu){
    const E=dot(Xs,Xs),F=dot(Xs,Xu),G=dot(Xu,Xu),cr=cross(Xs,Xu),cross2=dot(cr,cr);
    const rE=E-1,rF=F/p.a,rG=G/(p.a*p.a)-1,mean=(rE+rG)/2,rad=Math.hypot((rE-rG)/2,rF);
    const result={E,F,G,rE,rF,rG,relativeMetric:Math.max(Math.abs(mean+rad),Math.abs(mean-rad)),
      immersion:cross2/(p.a*p.a),squaredRadius:dot(X,X),height:X[2],normal:null,principalCurvatures:null,curvature:null};
    if(!(E>0&&cross2>0))return result;
    const normal=cr.map(v=>v/Math.sqrt(cross2)),L=dot(normal,Xss),M=dot(normal,Xsu),NN=dot(normal,Xuu);
    const perpendicular=cross2/E,k=F/E,aa=L/E,bb=(M-k*L)/Math.sqrt(cross2),cc=(NN-2*k*M+k*k*L)/perpendicular;
    const h=(aa+cc)/2,r=Math.hypot((aa-cc)/2,bb),principal=[h+r,h-r];
    Object.assign(result,{normal,secondFundamental:[L,M,NN],orthonormalSecondFundamental:[aa,bb,cc],
      principalCurvatures:principal,curvature:Math.max(...principal.map(Math.abs)),inwardSupport:-dot(X,normal)});
    return result;
  }
  function slice(s,parameters){
    const z=Float64Array.from(parameters),rad=radial(s,z),channels=9;
    const prefix=Array.from({length:nq+1},()=>new Float64Array(channels));
    const total=new Float64Array(channels),moment=new Float64Array(channels);
    function accumulate(lo,hi,out,firstMoment){
      const width=hi-lo;if(width===0)return;
      for(let k=0;k<8;k++){
        const u=lo+width*G8.x[k],weight=width*G8.w[k],q=angles(rad,u,z),v=[...q.T,...q.Ts,...q.Tss];
        for(let j=0;j<channels;j++){const inc=weight*v[j];out[j]+=inc;if(firstMoment)firstMoment[j]+=(A-u)*inc;}
      }
    }
    for(let j=0;j<nq;j++){
      prefix[j].set(total);accumulate(j*du,(j+1)*du,total,moment);
    }
    prefix[nq].set(total);
    function quarter(u){
      const index=Math.min(nq,Math.floor(u/du)),integral=Float64Array.from(prefix[index]);
      if(index<nq)accumulate(index*du,u,integral,null);
      const primitives=[0,1,2].map(order=>[0,1,2].map(k=>{
        const off=3*order+k;
        return integral[off]-(k===0?total[off]:k===2?moment[off]/A:0);
      }));
      return {Y:primitives[0],Ys:primitives[1],Yss:primitives[2],...angles(rad,u,z)};
    }
    function point(u){
      if(!Number.isFinite(u))throw Error("Nonfinite material angle");
      let v=((u%(2*Math.PI))+2*Math.PI)%(2*Math.PI);
      if(v===2*Math.PI)v=0;
      const quadrant=Math.min(3,Math.floor(v/A)),q=quadrant%2?(quadrant+1)*A-v:v-quadrant*A;
      const matrices=[[1,1,1],[-1,1,1],[-1,-1,1],[1,-1,1]],R=matrices[quadrant],direction=quadrant%2?-1:1;
      const t=quarter(Math.max(0,Math.min(A,q))),rv=x=>x.map((a,k)=>R[k]*a),dv=x=>rv(x).map(a=>direction*a);
      const Y=rv(t.Y),Ys=rv(t.Ys),Yss=rv(t.Yss),T=dv(t.T),Ts=dv(t.Ts),Tss=dv(t.Tss),Tu=rv(t.Tu),p=rad.p;
      const X=Y.map((a,k)=>p.a*a+(k===2?rad.Z:0));
      const Xs=Y.map((a,k)=>p.as*a+p.a*Ys[k]+(k===2?rad.Zs:0));
      const Xu=T.map(a=>p.a*a);
      const Xss=Y.map((a,k)=>p.ass*a+2*p.as*Ys[k]+p.a*Yss[k]+(k===2?rad.Zss:0));
      const Xsu=T.map((a,k)=>p.as*a+p.a*Ts[k]),Xuu=Tu.map(a=>p.a*a);
      return {s,u,Y,Ys,Yss,T,Ts,Tss,Tu,X,Xs,Xu,Xss,Xsu,Xuu,Z:rad.Z,Zs:rad.Zs,Zss:rad.Zss,
        geometry:geometry(p,X,Xs,Xu,Xss,Xsu,Xuu),
        tangentIdentities:{unit:dot(T,T)-1,firstRadial:dot(T,Ts),secondRadial:dot(T,Tss)+dot(Ts,Ts),angular:dot(T,Tu)},
        quarterAngleJet:{u:q,theta:t.theta,phi:t.phi,theta_u:t.theta_u,phi_u:t.phi_u,theta_s:t.theta_s,phi_s:t.phi_s,theta_ss:t.theta_ss,phi_ss:t.phi_ss},
        finite_quadrature:true};
    }
    return {s,point,quarter,center:[rad.Z,rad.Zs,rad.Zss],quarterTotals:Array.from(total),quarterFirstMoments:Array.from(moment)};
  }
  function samples(z,config){
    if(!Array.isArray(config.s_values)||!Array.isArray(config.u_values))throw Error("Explicit finite point set required");
    const summary={count:0,maxRelativeMetric:0,minImmersion:Infinity,maxCurvature:0,minHeight:Infinity,maxHeight:-Infinity,maxSquaredRadius:0,
      maxAbsCoordinate:[0,0,0],minInwardSupport:Infinity,worstMetric:null,worstCurvature:null};
    const points=[];
    for(const s of config.s_values){
      const sl=slice(s,z);
      for(const u of config.u_values){
        const p=sl.point(u),g=p.geometry;summary.count++;
        if(g.relativeMetric>summary.maxRelativeMetric){summary.maxRelativeMetric=g.relativeMetric;summary.worstMetric={s,u};}
        summary.minImmersion=Math.min(summary.minImmersion,g.immersion);
        if(g.curvature===null)summary.nonimmersedSamples=(summary.nonimmersedSamples||0)+1;
        else if(g.curvature>summary.maxCurvature){summary.maxCurvature=g.curvature;summary.worstCurvature={s,u};}
        summary.minHeight=Math.min(summary.minHeight,g.height);summary.maxHeight=Math.max(summary.maxHeight,g.height);
        summary.maxSquaredRadius=Math.max(summary.maxSquaredRadius,g.squaredRadius);
        if(g.inwardSupport!==undefined)summary.minInwardSupport=Math.min(summary.minInwardSupport,g.inwardSupport);
        for(let k=0;k<3;k++)summary.maxAbsCoordinate[k]=Math.max(summary.maxAbsCoordinate[k],Math.abs(p.X[k]));
        if(config.include_points)points.push(p);
      }
    }
    return {schema:"fd2d-R187-actual-position-two-jet-finite-diagnostic-v1",definition:definition(),summary,
      sample_set:{s_values:config.s_values,u_values:config.u_values},points:config.include_points?points:undefined,
      continuous_metric_curvature_ball_or_reach_certificate:false,whole_surface_or_strong_goal_complete:false};
  }
  function definition(){
    return {schema:"fd2d-R187-quarter-primitive-actual-position-two-jet-consumer-v1",provider_schema:def.schema,
      parameter_layout:def.stateLayout,dimension:n,radialBasisCount:J,angularModes:K,fullEquivalentAngles:N,
      centralLength:c,end:S,radialSplineStep:step,centralGap:def.centralGap,
      primitive:"Same quarter Gauss8 cells/first moment for T,Ts,Tss; exact D2 symmetry extension",
      angular_derivatives:"Complete analytic theta_u and phi_u, no DFT or finite angular projection",
      physical_two_jet:"X=aY+Zez; Xss=assY+2asYs+aYss+Zssez; Xsu=asT+aTs; Xuu=aTu",
      center:"Full original background Z plus all C2 B-splines and the declared cut-height quintic",
      local_curvature:"Actual Gram matrix and orthonormalized second fundamental form of X",
      numerical_primitive_derivative_error_still_unbounded:true,continuous_certificate:false};
  }
  return {definition,dimension:n,slice,point:(s,u,z)=>slice(s,z).point(u),samples};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR187Geometry};
