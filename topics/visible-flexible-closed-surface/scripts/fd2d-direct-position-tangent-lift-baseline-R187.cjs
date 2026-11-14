/* R187: complete angular-length preserving position lifting.
 * This is a numerical initial-field experiment, not a solved isometry.
 * Pure numerical core runs in V8; the optional CLI only reads/writes JSON.
 */
"use strict";
function createR187() {
  const PI=Math.PI, TWO=2*PI;
  function gauss(n){
    const x=[],w=[];
    for(let i=1;i<=n;i++){
      let z=Math.cos(PI*(i-.25)/(n+.5)),dp=0;
      for(let it=0;it<30;it++){
        let a=1,b=z;
        for(let k=2;k<=n;k++){const c=((2*k-1)*z*b-(k-1)*a)/k;a=b;b=c;}
        dp=n*(z*b-a)/(z*z-1);
        const dz=b/dp;z-=dz;if(Math.abs(dz)<3e-16)break;
      }
      let a=1,b=z;for(let k=2;k<=n;k++){const c=((2*k-1)*z*b-(k-1)*a)/k;a=b;b=c;}
      dp=n*(z*b-a)/(z*z-1);
      x.push((1+z)/2);w.push(1/((1-z*z)*dp*dp));
    }
    return {x,w};
  }
  const G8=gauss(8),G24=gauss(24),G32=gauss(32);
  function quad(f,lo,hi,g=G24){
    let sum=0,err=0;const d=hi-lo;
    for(let j=0;j<g.x.length;j++){
      const y=g.w[j]*f(lo+d*g.x[j])-err,t=sum+y;err=(t-sum)-y;sum=t;
    }
    return d*sum;
  }
  function horner(c,x){let v=0;for(let i=c.length-1;i>=0;i--)v=v*x+c[i];return v;}
  function deriv(c){return c.slice(1).map((v,i)=>v*(i+1));}
  function quintic(L,j0,j1){
    const a=j0[0],b=L*j0[1],c=L*L*j0[2]/2;
    const d=j1[0]-a-b-c,v=L*j1[1]-b-2*c,k=L*L*j1[2]-2*c;
    return [a,b,c,10*d-4*v+k/2,-15*d+7*v-k,6*d-3*v+k/2];
  }
  function ellipse(A,B){
    const speed=t=>Math.hypot(A*Math.sin(t),B*Math.cos(t));
    const n=64,dt=PI/(2*n),cumulative=[0];
    for(let j=0;j<n;j++)cumulative.push(cumulative[j]+quad(speed,j*dt,(j+1)*dt,G8));
    const quarter=cumulative[n],a0=2*quarter/PI;
    function theta(u){
      let v=((u%TWO)+TWO)%TWO;
      if(Math.abs(v-TWO)<1e-14)v=0;
      const quadrant=Math.min(3,Math.floor(v/(PI/2))),local=v-quadrant*PI/2;
      let target=a0*local;if(quadrant%2)target=quarter-target;
      let lo=0,hi=n;
      while(hi-lo>1){const mid=(lo+hi)>>1;if(cumulative[mid]<=target)lo=mid;else hi=mid;}
      let t=lo*dt+(target-cumulative[lo])/(cumulative[hi]-cumulative[lo])*dt;
      for(let k=0;k<7;k++){
        const residual=cumulative[lo]+quad(speed,lo*dt,t,G8)-target;
        const change=residual/speed(t);t-=change;
        t=Math.max(lo*dt,Math.min(hi*dt,t));
        if(Math.abs(change)<2e-15)break;
      }
      return quadrant%2?(quadrant+1)*PI/2-t:quadrant*PI/2+t;
    }
    function at(u){
      const t=theta(u),ct=Math.cos(t),st=Math.sin(t),ell=speed(t);
      const v=[-A*st/ell,B*ct/ell],eu=[-Math.sin(u),Math.cos(u)];
      const cos=v[0]*eu[0]+v[1]*eu[1],sin=eu[0]*v[1]-eu[1]*v[0];
      const delta=Math.atan2(sin,cos),betaU=a0*A*B/(ell*ell*ell);
      return {u,gamma:[A*ct/a0,B*st/a0],v,
        vu:[-betaU*v[1],betaU*v[0]],
        h:2*Math.sin(delta/2),hu:Math.cos(delta/2)*(betaU-1),
        delta};
    }
    return {A,B,a0,quarter,theta,at};
  }
  function phase(p,t){
    const d=p.p1-p.p0,L=p.L;
    if(p.kind==="turn"){
      let v,I;
      if(t<.08){const x=t/.08;v=3*x*x-2*x*x*x;I=.08*(x*x*x-x*x*x*x/2);}
      else if(t>.92){const x=(1-t)/.08;v=3*x*x-2*x*x*x;I=.92-.08*(x*x*x-x*x*x*x/2);}
      else{v=1;I=t-.04;}
      return [p.p0+d*I/.92,d*v/(.92*L)];
    }
    if(p.kind==="phase_bridge"){
      const q0=L*p.ps0,q1=L*p.ps1,c2=3*d-2*q0-q1,c3=-2*d+q0+q1;
      return [p.p0+t*(q0+t*(c2+t*c3)),(q0+t*(2*c2+3*t*c3))/L];
    }
    if(p.kind==="brake")return[p.p0+d*t*t,2*d*t/L];
    return [p.p0,0];
  }
  function phaseIntegral(p,t,cosine=false){
    const cuts=[0,...(p.kind==="turn"?[.08,.92].filter(x=>x<t):[]),t];
    let ans=0;
    for(let j=1;j<cuts.length;j++)ans+=quad(x=>{const f=phase(p,x)[0];return cosine?Math.cos(f):Math.sin(f);},cuts[j-1],cuts[j]);
    return p.L*ans;
  }
  function candidate(bundle){
    const a0=ellipse(bundle.ellipse.A,bundle.ellipse.B).a0,resolved=[];
    let pv=0,pa=0,pp=0;
    for(const raw of bundle.segments){
      const p=JSON.parse(JSON.stringify(raw));
      if(p.kind==="hermite"){
        p.c=quintic(p.L,p.jet0,p.jet1);p.d=deriv(p.c);p.dd=deriv(p.d);
        pv=p.jet1[1];pa=p.jet1[2];pp=null;
      }else{
        if(p.start_from_previous)p.p0=pp===null?Math.asin(pv):pp;
        if(p.end_phase_add!==undefined)p.p1=p.p0+p.end_phase_add;
        if(p.end_radial_speed!==undefined)p.p1=Math.asin(p.end_radial_speed);
        if(p.start_second_from_previous)p.ps0=pa/Math.cos(p.p0);
        if(p.kind==="coast"||p.kind==="coast_to")p.p1=p.p0;
        if(p.length_from_turn_rate)p.L=Math.abs(p.p1-p.p0)/(p.K*.92);
        if(p.exact_endpoint_phase==="-pi/2")p.p1=-PI/2;
        pp=p.p1;pv=Math.sin(pp);
        pa=p.kind==="phase_bridge"?Math.cos(pp)*p.ps1:p.kind==="brake"?Math.cos(pp)*2*(p.p1-p.p0)/p.L:0;
      }
      resolved.push(p);
    }
    let s=0,a=a0,z=0;
    function local(p,t){
      if(p.kind==="hermite"){
        let aa=a0+horner(p.c,t),v=horner(p.d,t)/p.L,acc=horner(p.dd,t)/(p.L*p.L);
        if(t===0){aa=a0+p.jet0[0];v=p.jet0[1];acc=p.jet0[2];}
        if(t===1){aa=a0+p.jet1[0];v=p.jet1[1];acc=p.jet1[2];}
        const zs=Math.sqrt(Math.max(0,1-v*v));
        const zz=p.z0+p.L*quad(x=>{const q=horner(p.d,x)/p.L;return Math.sqrt(Math.max(0,1-q*q));},0,t);
        return {a:aa,as:v,ass:acc,z:zz,zs,zss:-v*acc/zs};
      }
      const [f,fs]=phase(p,t),v=Math.sin(f),zz=Math.cos(f);
      return {a:p.a0+phaseIntegral(p,t),as:v,ass:zz*fs,
        z:p.z0+phaseIntegral(p,t,true),zs:zz,zss:-v*fs};
    }
    for(let i=0;i<resolved.length;i++){
      const p=resolved[i];p.s0=s;p.a0=a;p.z0=z;
      if(p.kind==="coast_to"){
        const target=p.radius_after_next-phaseIntegral(resolved[i+1],1);
        p.L=(target-a)/Math.sin(p.p0);if(!(p.L>0))throw Error("Nonpositive B32 coast");
      }
      p.s1=s+p.L;
      const end=local(p,1);a=end.a;z=end.z;s=p.s1;
    }
    function at(s){
      let i=resolved.findIndex(p=>s<p.s1);if(i<0)i=resolved.length-1;
      const p=resolved[i],t=Math.max(0,Math.min(1,(s-p.s0)/p.L));
      const out=local(p,t);
      if(s===0){out.a=a0;out.as=0;out.ass=0;out.z=0;out.zs=1;out.zss=0;}
      if(s===resolved[resolved.length-1].s1){out.a=4/5;out.as=-1;out.ass=0;out.zs=0;out.zss=0;}
      return {...out,s};
    }
    return {a0,end:s,height:z,segments:resolved,at,
      centralLength:resolved[0].L,deepCoast:resolved.find(p=>p.kind==="coast_to").L};
  }
  function profileWeights(s,c,S){
    if(s<=c)return {q:1,qs:0,qss:0,r:0,rs:0,rss:0};
    if(s>=S)return {q:0,qs:0,qss:0,r:0,rs:0,rss:0};
    const L=S-c,t=(s-c)/L,step=t*t*t*(10+t*(-15+6*t));
    const dp=30*t*t*(1-t)*(1-t)/L,ddp=60*t*(1-t)*(1-2*t)/(L*L);
    const b=PI*(1-step),bs=-PI*dp,bss=-PI*ddp,sn=Math.sin(b),cs=Math.cos(b);
    return {q:(1-cs)/2,qs:sn*bs/2,qss:(cs*bs*bs+sn*bss)/2,
      r:sn/2,rs:cs*bs/2,rss:(-sn*bs*bs+cs*bss)/2};
  }
  function angular(curve,N){
    const du=TWO/N,H=[0],rows=[];
    let moment=0;
    for(let j=0;j<N;j++){
      const lo=j*du,hi=(j+1)*du;
      H.push(H[j]+quad(u=>curve.at(u).h,lo,hi,G8));
      moment+=quad(u=>(TWO-u)*curve.at(u).h,lo,hi,G8);
    }
    const mean=moment/TWO;
    for(let j=0;j<N;j++)rows.push({...curve.at(j*du),H:H[j]-mean});
    return {rows,primitiveIntegralRoundoff:H[N],primitiveMean:mean};
  }
  const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
  const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
  function point(p,w,g){
    const e=[Math.cos(g.u),Math.sin(g.u)],eu=[-Math.sin(g.u),Math.cos(g.u)];
    const D=[g.gamma[0]-e[0],g.gamma[1]-e[1]];
    const Du=[g.v[0]-eu[0],g.v[1]-eu[1]];
    const Duu=[g.vu[0]+e[0],g.vu[1]+e[1]];
    const Y=[e[0]+w.q*D[0],e[1]+w.q*D[1],w.r*g.H];
    const Ys=[w.qs*D[0],w.qs*D[1],w.rs*g.H];
    const Yss=[w.qss*D[0],w.qss*D[1],w.rss*g.H];
    const T=[eu[0]+w.q*Du[0],eu[1]+w.q*Du[1],w.r*g.h];
    const Ts=[w.qs*Du[0],w.qs*Du[1],w.rs*g.h];
    const Tu=[-e[0]+w.q*Duu[0],-e[1]+w.q*Duu[1],w.r*g.hu];
    const X=Y.map((v,j)=>p.a*v+(j===2?p.z:0));
    const Xs=Y.map((v,j)=>p.as*v+p.a*Ys[j]+(j===2?p.zs:0));
    const Xu=T.map(v=>p.a*v);
    const Xss=Y.map((v,j)=>p.ass*v+2*p.as*Ys[j]+p.a*Yss[j]+(j===2?p.zss:0));
    const Xsu=T.map((v,j)=>p.as*v+p.a*Ts[j]),Xuu=Tu.map(v=>p.a*v);
    const E=dot(Xs,Xs),F=dot(Xs,Xu),G=dot(Xu,Xu),det=E*G-F*F;
    const e11=E-1,e12=F/p.a,e22=G/(p.a*p.a)-1;
    const mean=(e11+e22)/2,rad=Math.hypot((e11-e22)/2,e12);
    let curvature=null;
    if(det>0){
      const nv=cross(Xs,Xu).map(v=>v/Math.sqrt(det));
      const L=dot(nv,Xss),M=dot(nv,Xsu),NN=dot(nv,Xuu);
      const hm=(G*L-2*F*M+E*NN)/(2*det),kg=(L*NN-M*M)/det;
      const rr=Math.sqrt(Math.max(0,hm*hm-kg));curvature=Math.max(Math.abs(hm+rr),Math.abs(hm-rr));
    }
    return {X,E,F,G,relativeMetric:Math.max(Math.abs(mean+rad),Math.abs(mean-rad)),
      angularMetric:Math.abs(e22),immersion:det/(p.a*p.a),curvature};
  }
  function ellipseForGap(gap,a0){
    if(gap===0)return ellipse(1,1);
    let lo=.05,hi=2;
    for(let k=0;k<55;k++){
      const mid=(lo+hi)/2,c=ellipse(mid+gap,mid);
      if(c.a0>a0)hi=mid;else lo=mid;
    }
    const B=(lo+hi)/2;return ellipse(B+gap,B);
  }
  function evaluate(bundle,options={}){
    const N=options.angles||128,sub=options.radialSubdivisions||4;
    const base=candidate(bundle),grid=[];
    for(const p of base.segments)for(let j=0;j<sub;j++)grid.push(p.s0+p.L*j/sub);
    grid.push(base.end);
    const profiles=grid.map(s=>({...base.at(s),weights:profileWeights(s,base.centralLength,base.end)}));
    const cases=[];
    for(const requestedGap of options.gaps||[0,.05,.64,.9]){
      const curve=ellipseForGap(requestedGap,base.a0),angularData=angular(curve,N);
      let maxMetric=-1,maxG=-1,minImm=Infinity,maxCurv=-1,worstMetric,worstCurv,minZ=Infinity,maxZ=-Infinity;
      const boundary={central:0,cut:0};
      for(const p of profiles)for(const g of angularData.rows){
        const v=point(p,p.weights,g);
        if(v.relativeMetric>maxMetric){maxMetric=v.relativeMetric;worstMetric={s:p.s,u:g.u,E:v.E,F:v.F,G:v.G};}
        maxG=Math.max(maxG,v.angularMetric);minImm=Math.min(minImm,v.immersion);
        if(v.curvature!==null&&v.curvature>maxCurv){maxCurv=v.curvature;worstCurv={s:p.s,u:g.u};}
        minZ=Math.min(minZ,v.X[2]);maxZ=Math.max(maxZ,v.X[2]);
        if(p.s===0)boundary.central=Math.max(boundary.central,v.relativeMetric);
        if(p.s===base.end)boundary.cut=Math.max(boundary.cut,v.relativeMetric);
      }
      cases.push({requestedGap,actualCentralGap:base.a0*(curve.A-curve.B)/curve.a0,
        actualCentralA:base.a0*curve.A/curve.a0,actualCentralB:base.a0*curve.B/curve.a0,
        maximumSampledRelativeMetric:maxMetric,maximumSampledAngularMetric:maxG,
        minimumSampledNormalizedImmersion:minImm,maximumSampledPrincipalCurvature:maxCurv,
        sampledHeightRange:[minZ,maxZ],worstMetric,worstCurv,boundary,
        signedPrimitiveFullPeriodQuadratureRoundoff:angularData.primitiveIntegralRoundoff,
        nonlinearSolved:false,continuousGeometryCertified:false});
    }
    return {schema:"fd2d-R187-direct-position-angular-isometry-initial-field-v1",
      actualRuntime:"pure JavaScript/V8 numerical evaluation; no OS child process",
      candidateDefinition:"R181 B32; exact scalar semantics unchanged, all values below are finite floating evaluations",
      base:{a0:base.a0,end:base.end,height:base.height,centralLength:base.centralLength,
            finalDeepCoastLength:base.deepCoast,segments:base.segments.length},
      numericalRule:{phaseGauss:24,ellipseQuarterPanels:64,ellipsePanelGauss:8,
        angularPrimitivePanelGauss:8,angles:N,radialSubdivisions:sub,radialPoints:grid.length},
      exactDefinitionAngularMetricPreserved:true,
      exactDefinitionCentralAndFlatCutTwoJetsPreserved:true,
      finiteGridOnly:true,newNonlinearAcceptedState:false,strongTargetComplete:false,cases};
  }
  return {ellipse,candidate,profileWeights,angular,point,evaluate,gauss,quad};
}
if(typeof module!=="undefined"&&module.exports){
  module.exports={createR187};
  if(require.main===module){
    const fs=require("node:fs"),crypto=require("node:crypto"),path=require("node:path");
    const [input,output]=process.argv.slice(2);
    if(!input||!output)throw Error("Usage: node this.cjs candidate.json new-report.json");
    if(fs.existsSync(output))throw Error("Choose a new report path");
    const raw=fs.readFileSync(input),start=process.hrtime.bigint();
    const report=createR187().evaluate(JSON.parse(raw));
    report.seconds=Number(process.hrtime.bigint()-start)/1e9;
    report.source={path:__filename,sha256:crypto.createHash("sha256").update(fs.readFileSync(__filename)).digest("hex")};
    report.input={path:input,sha256:crypto.createHash("sha256").update(raw).digest("hex")};
    fs.mkdirSync(path.dirname(output),{recursive:true});
    fs.writeFileSync(output,JSON.stringify(report,null,2)+"\n");
    console.log(JSON.stringify({output,seconds:report.seconds,cases:report.cases.map(x=>[x.actualCentralGap,x.maximumSampledRelativeMetric])}));
  }
}
