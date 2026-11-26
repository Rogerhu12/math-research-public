"use strict";
/*
 * Frozen actual Cauchy checkpoint reader, including its real R205 tail.
 * Existing factory, q.z, A/Z, primitive and quadrature remain unchanged.
 * Optional higher angular jets come from explicit first dual derivatives
 * of the same reference angles and the same R201 mean-phase formula.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const JETS=["X","Xs","Xss","Xu","Xsu","Xuu"];
const HIGH=["Xssu","Xsuu","Xssuu"];
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const hashText=s=>crypto.createHash("sha256").update(s).digest("hex");
const dot=(a,b)=>a.reduce((s,v,k)=>s+v*b[k],0);
const norm=a=>Math.hypot(...a);
const JD=x=>Array.isArray(x)?x:[x,0];
const add=(a,b)=>{a=JD(a);b=JD(b);return[a[0]+b[0],a[1]+b[1]];};
const neg=a=>{a=JD(a);return[-a[0],-a[1]];};
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>{a=JD(a);b=JD(b);return[a[0]*b[0],a[1]*b[0]+a[0]*b[1]];};
const div=(a,b)=>{a=JD(a);b=JD(b);return[a[0]/b[0],(a[1]*b[0]-a[0]*b[1])/(b[0]*b[0])];};
const sq=a=>mul(a,a);
const sin=a=>{a=JD(a);return[Math.sin(a[0]),Math.cos(a[0])*a[1]];};
const cos=a=>{a=JD(a);return[Math.cos(a[0]),-Math.sin(a[0])*a[1]];};
const sqrt=a=>{a=JD(a);const y=Math.sqrt(a[0]);return[y,a[1]/(2*y)];};
const atan2=(y,x)=>{x=JD(x);y=JD(y);return[Math.atan2(y[0],x[0]),(x[0]*y[1]-y[0]*x[1])/(x[0]*x[0]+y[0]*y[0])];};
const asin=a=>{a=JD(a);return[Math.asin(Math.max(-1,Math.min(1,a[0]))),a[1]/Math.sqrt(1-a[0]*a[0])];};

function createCauchySource(candidate,input,options={}) {
  const scripts=path.resolve(options.scriptsDirectory??__dirname);
  const branch=require(path.join(scripts,"6a65-cauchy-global-position.cjs"));
  if(![branch.INITIAL,branch.CHECKPOINT].includes(input?.schema)||
     input.baseModel!=="short-cauchy-v1"||!Array.isArray(input.z)||
     !input.z.every(Number.isFinite))
    throw Error("An actual complete short-Cauchy checkpoint is required");
  const q=branch.build(candidate,input),saved=Array.from(q.z);
  if(saved.length!==input.z.length||!saved.every((v,k)=>Object.is(v,input.z[k])))
    throw Error("Source constructor changed complete checkpoint coefficients");
  const c=q.base.centralLength,S=q.base.end,cuff=S+.48;
  const amplitude=saved[q.amplitudeIndex],Z=q.base.height+saved[q.cutHeightIndex];
  const reference=q.referenceFactory(amplitude),algebra=
    require(path.join(scripts,"fd2d-position-curvature-chain-R191.cjs")).createR191Algebra();
  const J=input.options.radialBasisCount,K=input.options.modes,N=input.options.angles;
  const legacy=q.metric.dimension,width=2*K+1,radiusStart=q.metric.definition.stateLayout.radius[0];
  const G8=q.engine.gauss(8);
  let lastS=null,last=null;
  function assertUnchanged() {
    if(!saved.every((v,k)=>Object.is(v,q.z[k])))throw Error("Frozen source coefficients were mutated");
  }
  function radius(s) {
    if(!Number.isFinite(s)||s<0||s>cuff)throw Error("Point outside actual half-core plus true tail");
    if(s===cuff)return {a:.32,as:-1,ass:0};
    if(s>S)return {a:.8-(s-S),as:-1,ass:0};
    const b=q.base.at(s),r=q.metric.radialBasis.physicalJets(s,c,S);
    let a=b.a,as=b.as,ass=b.ass;
    for(let j=0;j<r.indices.length;j++){
      const v=saved[radiusStart+r.indices[j]];
      a+=v*r.value[j];as+=v*r.first[j];ass+=v*r.second[j];
    }
    return {a,as,ass};
  }
  function blend(s) {
    if(s<=c)return [0,0,0];if(s>=S)return [1,0,0];
    const L=S-c,t=(s-c)/L;
    return [t*t*t*(10+t*(-15+6*t)),30*t*t*(1-t)*(1-t)/L,
      60*t*(1-t)*(1-2*t)/(L*L)];
  }
  function stepDual(t) {
    if(t[0]<=0)return [[0,0],[0,0],[0,0]];
    if(t[0]>=1)return [[1,0],[0,0],[0,0]];
    const x=t[0],h=t[1],one=1-x;
    const v=x**5*(126+x*(-420+x*(540+x*(-315+70*x))));
    const d=630*x**4*one**4,dd=2520*x**3*one**3*(1-2*x);
    const ddd=7560*x*x*one*one*(1-2*x)**2-5040*x**3*one**3;
    return [[v,d*h],[d,dd*h],[dd,ddd*h]];
  }
  function tailFrame(p,u) {
    const U=[u,1],sn=sin(U),cs=cos(U),sign=Math.sign(sn[0]);
    const absY=mul(sign*p.a,sn),st=stepDual(div(sub(absY,.34),.46));
    const alpha=mul(sign*amplitude,st[0]),k=mul(amplitude/.46,st[1]),
      ky=mul(sign*amplitude/(.46*.46),st[2]);
    const alphas=mul(k,mul(p.as,sn));
    const alphass=add(mul(ky,mul(p.as*p.as,sq(sn))),mul(k,mul(p.ass,sn)));
    const ca=cos(alpha),sa=sin(alpha);
    const T=[neg(sn),mul(ca,cs),neg(mul(sa,cs))];
    const Ts=[[0,0],neg(mul(mul(sa,alphas),cs)),neg(mul(mul(ca,alphas),cs))];
    const Tss=[[0,0],neg(mul(add(mul(ca,sq(alphas)),mul(sa,alphass)),cs)),
      mul(sub(mul(sa,sq(alphas)),mul(ca,alphass)),cs)];
    const cp2=add(sq(T[0]),sq(T[1])),cp=sqrt(cp2);
    if(!(cp2[0]>0))throw Error("Actual tail angle chart singular");
    const cr=mul(T[0],Ts[1]),hd=mul(T[1],Ts[1]);
    const th=atan2(sub(mul(neg(sn),T[1]),mul(cs,T[0])),
      add(mul(neg(sn),T[0]),mul(cs,T[1])));
    const ph=atan2(T[2],cp),ths=div(cr,cp2),phs=div(Ts[2],cp);
    const thss=sub(div(mul(T[0],Tss[1]),cp2),mul(2,div(mul(hd,cr),sq(cp2))));
    const phss=sub(div(Tss[2],cp),div(mul(Ts[2],hd),mul(cp2,cp)));
    return {T,Ts,Tss,angles:[th,ph,ths,phs,thss,phss]};
  }
  function rawAngles(context,u) {
    const U=[u,1],sn=sin(U),cs=cos(U),g=q.metric.curve.at(u),w=context.w;
    const ex=neg(sn),ey=cs,dx=sub([g.v[0],g.vu[0]],ex),
      dy=sub([g.v[1],g.vu[1]],ey),gh=[g.h,g.hu];
    const tx=add(ex,mul(w.q,dx)),ty=add(ey,mul(w.q,dy)),tz=mul(w.r,gh);
    const txs=mul(w.qs,dx),tys=mul(w.qs,dy),tzs=mul(w.rs,gh);
    const txss=mul(w.qss,dx),tyss=mul(w.qss,dy),tzss=mul(w.rss,gh);
    const cp2=add(sq(tx),sq(ty)),cp=sqrt(cp2),cr=sub(mul(tx,tys),mul(ty,txs)),
      hd=add(mul(tx,txs),mul(ty,tys));
    if(!(cp2[0]>1e-15))throw Error("Actual source reference angle chart singular");
    let out=[
      add(U,atan2(sub(mul(ex,ty),mul(ey,tx)),add(mul(ex,tx),mul(ey,ty)))),
      asin(tz),div(cr,cp2),div(tzs,cp),
      sub(div(sub(mul(tx,tyss),mul(ty,txss)),cp2),mul(2,div(mul(hd,cr),sq(cp2)))),
      sub(div(tzss,cp),div(mul(tzs,hd),mul(cp2,cp))),
    ];
    if(context.chi.some(v=>v!==0)){
      const b=tailFrame(context.p,u).angles,chi=context.chi;
      const bend=[
        mul(chi[0],b[0]),mul(chi[0],b[1]),
        add(mul(chi[1],b[0]),mul(chi[0],b[2])),
        add(mul(chi[1],b[1]),mul(chi[0],b[3])),
        add(add(mul(chi[2],b[0]),mul(2*chi[1],b[2])),mul(chi[0],b[4])),
        add(add(mul(chi[2],b[1]),mul(2*chi[1],b[3])),mul(chi[0],b[5])),
      ];
      out=out.map((v,j)=>add(v,bend[j]));
    }
    for(let a=0;a<context.basis.indices.length;a++){
      const j=context.basis.indices[a],weights=[context.basis.value[a],context.basis.first[a],context.basis.second[a]];
      for(let k=0;k<K;k++){
        const f=2*(k+1),snk=sin(mul(f,U)),csk=cos(mul(f,U));
        const th=add(mul(saved[j*K+k],snk),mul(saved[legacy+j*width+1+k],csk));
        const ph=add(mul(saved[J*K+j*K+k],snk),mul(saved[legacy+j*width+1+K+k],csk));
        for(let d=0;d<3;d++){
          out[2*d]=add(out[2*d],mul(weights[d],th));
          out[2*d+1]=add(out[2*d+1],mul(weights[d],ph));
        }
      }
      const v=saved[legacy+j*width];
      for(let d=0;d<3;d++)out[2*d]=add(out[2*d],weights[d]*v);
    }
    return out;
  }
  function phase(context) {
    const mean=Array(6).fill(0),nq=N/2,du=Math.PI/nq;
    for(let j=0;j<nq;j++){
      const cuts=reference.angularSubintervals(context.s,j*du,(j+1)*du);
      for(let h=1;h<cuts.length;h++)for(let k=0;k<G8.x.length;k++){
        const length=cuts[h]-cuts[h-1],u=cuts[h-1]+length*G8.x[k],weight=length*G8.w[k];
        const r=rawAngles(context,u),p=r[1][0],ps=r[3][0],pss=r[5][0],co=Math.cos(p),sn=Math.sin(p);
        const row=[co,sn,-sn*ps,co*ps,-co*ps*ps-sn*pss,-sn*ps*ps+co*pss];
        for(let z=0;z<6;z++)mean[z]+=weight*row[z];
      }
    }
    const [C,V,Cs,Vs,Css,Vss]=mean,den=C*C+V*V;
    if(!(den>0&&Number.isFinite(den)))throw Error("Actual source mean phase singular");
    const re=(Cs*C+Vs*V)/den,im=(Vs*C-Cs*V)/den;
    return {C,S:V,R:Math.sqrt(den),beta:Math.atan2(V,C),bs:im,bss:(Vss*C-Css*V)/den-2*re*im};
  }
  function tangent(context,u) {
    if(context.tail)return tailFrame({a:context.radius.a,as:-1,ass:0},u);
    const raw=rawAngles(context,u),ph=context.phase;
    const th=raw[0],psi=sub(raw[1],ph.beta),ths=raw[2],psis=sub(raw[3],ph.bs),
      thss=raw[4],psiss=sub(raw[5],ph.bss);
    const st=sin(th),ct=cos(th),sp=sin(psi),co=cos(psi);
    const T=[neg(mul(st,co)),mul(ct,co),sp];
    const Dt=[neg(mul(ct,co)),neg(mul(st,co)),[0,0]];
    const Dp=[mul(st,sp),neg(mul(ct,sp)),co];
    const Dtt=[mul(st,co),neg(mul(ct,co)),[0,0]];
    const Dtp=[mul(ct,sp),mul(st,sp),[0,0]];
    const Ts=T.map((_,k)=>add(mul(Dt[k],ths),mul(Dp[k],psis)));
    const Tss=T.map((_,k)=>add(add(mul(Dt[k],thss),mul(Dp[k],psiss)),
      add(add(mul(Dtt[k],sq(ths)),mul(2,mul(Dtp[k],mul(ths,psis)))),neg(mul(T[k],sq(psis))))));
    return {T,Ts,Tss};
  }
  function context(s,deep) {
    if(lastS===s&&last&&(!deep||last.deep))return last;
    const r=radius(s),ctx={s,radius:r,tail:s>S,deep:!!deep};
    if(!ctx.tail){
      ctx.slice=q.position.slice(s,q.z,false);
      if(deep){
        ctx.p=q.base.at(s);ctx.w=q.engine.profileWeights(s,c,S);ctx.chi=blend(s);
        ctx.basis=q.metric.radialBasis.physicalJets(s,c,S);ctx.phase=phase(ctx);
      }
    }
    lastS=s;last=ctx;return ctx;
  }
  function packet(s,u,deep=false) {
    if(!Number.isFinite(u))throw Error("Finite material angle required");
    const ctx=context(s,deep);let out;
    if(ctx.tail){
      const jets=reference.tailPoint(ctx.radius.a,u,Z).jets,cv=algebra.curvature(jets);
      const e=cv.E-1,f=cv.F/ctx.radius.a,g=cv.G/(ctx.radius.a**2)-1;
      out={s,u,a:ctx.radius.a,jets,relativeMetric:Math.abs((e+g)/2)+Math.hypot((e-g)/2,f),
        curvature:cv.kappa,immersion:cv.w2/(ctx.radius.a**2)};
    }else{
      const TWO=2*Math.PI,v=((u%TWO)+TWO)%TWO,half=v>=Math.PI?1:0,hu=v-half*Math.PI;
      const ratio=hu*N/TWO,j=Math.round(ratio);
      if(Math.abs(ratio-j)<1e-13){
        const p=ctx.slice.node(j);
        out=half?{...p,u,jets:Object.fromEntries(JETS.map(k=>[k,p.jets[k].map((x,z)=>z<2?-x:x)]))}:p;
      }else out=ctx.slice.point(u);
    }
    out={...out,jets:{...out.jets},radius:ctx.radius};
    if(deep){
      const tj=tangent(ctx,u),{a,as,ass}=ctx.radius;
      out.jets.Xssu=[0,1,2].map(k=>ass*tj.T[k][0]+2*as*tj.Ts[k][0]+a*tj.Tss[k][0]);
      out.jets.Xsuu=[0,1,2].map(k=>as*tj.T[k][1]+a*tj.Ts[k][1]);
      out.jets.Xssuu=[0,1,2].map(k=>ass*tj.T[k][1]+2*as*tj.Ts[k][1]+a*tj.Tss[k][1]);
      out.higherJetConsistency={
        Xu:norm(out.jets.Xu.map((x,k)=>x-a*tj.T[k][0])),
        Xsu:norm(out.jets.Xsu.map((x,k)=>x-as*tj.T[k][0]-a*tj.Ts[k][0])),
        Xuu:norm(out.jets.Xuu.map((x,k)=>x-a*tj.T[k][1])),
        meanPhase:ctx.tail?0:Math.max(Math.abs(ctx.phase.C-out.phase.C),Math.abs(ctx.phase.S-out.phase.S)),
      };
    }
    return out;
  }
  const metadata={
    schema:"6a65-frozen-actual-Cauchy-core-and-true-R205-tail-source-v1",
    sourceIdentityKind:input.interfaceProbeOnly===true?
      "explicit-new-zero-free-coefficient-interface-probe":"actual-Cauchy-checkpoint",
    interfaceProbeOnly:input.interfaceProbeOnly===true,
    sourceHasNoClaimedBaselineOrAcceptance:input.interfaceProbeOnly===true,
    sourceCheckpointSchema:input.schema,checkpointDeclaredAcceptedSteps:input.cauchyAcceptedSteps,
    completeParameterDimension:saved.length,parameterVectorSHA256:hashText(JSON.stringify(saved)),
    c,S,cuff,amplitude,Z,amplitudeIndex:q.amplitudeIndex,cutHeightIndex:q.cutHeightIndex,
    centralA:q.metric.definition.centralA,centralB:q.metric.definition.centralB,
    centralGap:q.metric.definition.centralGap,primitiveAngles:N,
    sourceOptions:input.options,sourceCauchyDesign:input.cauchyDesign,
    radialMetricDefinition:q.metric.definition,actualDesign:q.design,
    sourceFileSHA256:hash(__filename),
    providerEntrySHA256:hash(path.join(scripts,"6a65-cauchy-global-position.cjs")),
    positionSourceSHA256:hash(path.join(scripts,"fd2d-R201-R205-variable-amplitude-lazy-curvature.cjs")),
    baseSourceSHA256:hash(path.join(scripts,"6a65-geometry-short-cauchy-base.cjs")),
    tailSourceSHA256:hash(path.join(scripts,"fd2d-bent-annulus-reference-R205.cjs")),
    ...options.identities,
    completeCoefficientsFrozen:true,amplitudeAndCuffHeightUnchanged:true,
    sourceAngularPrimitiveUnchanged:true,sourceMetricUnchanged:true,
    FourierOrHermiteBackgroundProjection:false,continuumCertificate:false,
  };
  function sample(s,angles,deep=false) {
    if(!Array.isArray(angles)||angles.length===0||!angles.every(Number.isFinite))throw Error("Nonempty finite material angles required");
    const names=deep?[...JETS,...HIGH]:JETS,values=Object.fromEntries(names.map(k=>[k,[]]));
    let maxMetric=0,maxCurvature=0,minImmersion=Infinity,minHeld=Infinity;
    const consistency={Xu:0,Xsu:0,Xuu:0,meanPhase:0};
    for(const u of angles){
      const p=packet(s,u,deep);
      for(const key of names)values[key].push(p.jets[key]);
      maxMetric=Math.max(maxMetric,p.relativeMetric);maxCurvature=Math.max(maxCurvature,p.curvature);
      minImmersion=Math.min(minImmersion,p.immersion);
      const X=p.jets.X;minHeld=Math.min(minHeld,norm([X[0],X[1]-metadata.centralA,X[2]]),
        norm([X[0],X[1]+metadata.centralA,X[2]]));
      if(deep)for(const key of Object.keys(consistency))consistency[key]=Math.max(consistency[key],p.higherJetConsistency[key]);
    }
    assertUnchanged();
    return {s,u:angles,radius:radius(s),jets:values,
      diagnostics:{maxMetric,maxCurvature,minImmersion,minHeld},
      ...(deep?{higherJetConsistency:consistency}:{})};
  }
  return {q,metadata,radius,packet,sample,assertUnchanged,clear:()=>{lastS=null;last=null;q.position.clearSliceReuse?.();}};
}

function mesh(cuts,lo,hi,step) {
  const points=[lo,...cuts.filter(x=>x>lo&&x<hi),hi].sort((a,b)=>a-b),out=[lo];
  for(let j=1;j<points.length;j++){
    const n=Math.ceil((points[j]-points[j-1])/step);
    for(let k=1;k<=n;k++)out.push(points[j-1]+(points[j]-points[j-1])*k/n);
  }
  return out;
}
module.exports={createCauchySource,JETS,HIGH,mesh};

if(require.main===module){
  const [mode,scriptsDirectory,candidateFile,inputFile,prefix,countText="512"]=process.argv.slice(2);
  if(!["serve","probe","archive"].includes(mode)||!scriptsDirectory||!candidateFile||!inputFile)
    throw Error("serve|probe|archive scripts-dir candidate actual-checkpoint [fresh-prefix] [angles]");
  const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile));
  const source=createCauchySource(candidate,input,{scriptsDirectory,identities:{
    candidateSHA256:hash(candidateFile),sourceStateSHA256:hash(inputFile),
  }});
  if(mode==="serve"){
    const readline=require("node:readline"),lines=readline.createInterface({input:process.stdin,crlfDelay:Infinity});
    lines.on("line",line=>{
      let request;
      try{
        request=JSON.parse(line);let answer;
        if(request.method==="metadata")answer={metadata:source.metadata};
        else if(request.method==="sample"||request.method===undefined)
          answer=source.sample(request.s,request.u,!!request.deep);
        else if(request.method==="clear"){source.clear();if(global.gc)global.gc();answer={cleared:true};}
        else throw Error("Unknown source request method");
        process.stdout.write(JSON.stringify({id:request.id??null,ok:true,...answer})+"\n");
      }catch(error){
        process.stdout.write(JSON.stringify({id:request?.id??null,ok:false,error:String(error.stack||error)})+"\n");
      }
    });
  }else{
    const count=Number(countText);
    if(!prefix||!Number.isInteger(count)||count<64||count%2)throw Error("Fresh archive prefix and even angular count >=64 required");
    const root=path.resolve(scriptsDirectory,"../../.."),where=path.resolve(prefix);
    if(where===root||where.startsWith(root+path.sep))throw Error("Raw archives must remain outside Git");
    const reportFile=prefix+"-report.json",dataFile=prefix+"-data.f64";
    if(fs.existsSync(reportFile)||fs.existsSync(dataFile))throw Error("Fresh actual source archive required");
    fs.mkdirSync(path.dirname(prefix),{recursive:true});
    const b=source.q.base.cauchyWarmDesign.coastEnd;
    const nodes=mode==="probe"?[source.metadata.c,b,b+.05,b+.1,b+.2,source.metadata.S,source.metadata.cuff]:
      mesh([...source.q.position.radialCuts,b,b+.2,source.metadata.S],0,source.metadata.cuff,.01);
    const angles=Array.from({length:count},(_,j)=>2*Math.PI*j/count),names=[...JETS,...HIGH];
    const rows=[],start=Date.now(),fd=fs.openSync(dataFile,"wx");
    try{
      for(let i=0;i<nodes.length;i++){
        const answer=source.sample(nodes[i],angles,true),data=new Float64Array(count*names.length*3);
        for(let j=0;j<count;j++)for(let k=0;k<names.length;k++)data.set(answer.jets[names[k]][j],j*names.length*3+k*3);
        fs.writeSync(fd,Buffer.from(data.buffer));
        rows.push({s:nodes[i],...answer.radius,...answer.diagnostics,higherJetConsistency:answer.higherJetConsistency});
        source.clear();if(global.gc&&i%16===0)global.gc();
        if(i%20===0||i===nodes.length-1)process.stdout.write(JSON.stringify({event:"source_row",index:i,total:nodes.length,...rows.at(-1)})+"\n");
      }
    }finally{fs.closeSync(fd);}
    const report={schema:"6a65-actual-Cauchy-source-full-jets-archive-v1",mode,count,nodes,rows,
      source:source.metadata,jetOrder:names,dtype:"little-endian Float64",shape:[nodes.length,count,names.length,3],
      dataFile,dataSHA256:hash(dataFile),sourceFileSHA256:hash(__filename),
      actualSourceValueEvaluation:true,notAProjectionOfBackground:true,
      unchangedSourceCoefficients:true,seconds:(Date.now()-start)/1000,OSExitCode:null,externalExitReceiptRequired:true};
    fs.writeFileSync(reportFile,JSON.stringify(report,null,2)+"\n");
    process.stdout.write(JSON.stringify({event:"archive_complete",reportSHA256:hash(reportFile),
      sourceStateSHA256:source.metadata.sourceStateSHA256,rows:nodes.length,seconds:report.seconds})+"\n");
  }
}
