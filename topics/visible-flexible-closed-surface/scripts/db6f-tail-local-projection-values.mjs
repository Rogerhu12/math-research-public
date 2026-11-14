// Standalone arithmetic comparison on frozen local (Q,L,g) inputs.
// No root, RHS, RK, flow or worker interface is exposed or called.
import fs from 'node:fs';
import path from 'node:path';
import {gzipSync,gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';
import {pathToFileURL,fileURLToPath} from 'node:url';
const {values:a}=parseArgs({options:{'source-root':{type:'string'},
  points:{type:'string',multiple:true},out:{type:'string'}}});
if(!a['source-root']||!a.points?.length||!a.out)throw Error('Missing arguments');
if(fs.existsSync(a.out))throw Error('Refusing to overwrite output');
const root=path.resolve(a['source-root']),source=path.join(root,'topics/large-amplitude-twist-flex/scripts/general_root_tail_momentum.mjs');
const {createMomentumTailEngine}=await import(pathToFileURL(source));
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const sq2=Math.sqrt(2),bases={},packets=a.points.map(read),points=[];
for(let i=0;i<packets.length;i++){
  const packet=packets[i];let list=packet.points??(packet.point?[packet.point]:null);
  if(!list&&packet.status==='ONE_ORIGINAL_ROOT_AT_PRESELECTED_COMPLETED_M14_ENDPOINT'){
    if(packet.singleOriginalRootCalls!==1||packet.flowCalls!==0||packet.wholeDNEvaluations!==0)
      throw Error('Unexpected M14 extraction scope');
    list=[{id:'m14-q512-success-control',origin:packet.origin,location:packet.location,
      options:packet.options,state:packet.state,Q:packet.Q,L:packet.L,geometry:packet.geometry,
      target:packet.target,rootDiagnostic:packet.root,
      precomputedCoefficients:{p:packet.p,pt:packet.pt,U:packet.U},
      sourceEvaluation:{...packet.originalEvaluation,
        minA:packet.root.minA,minD:packet.root.minD,minS:packet.root.minS,
        maxQuad:packet.root.maxQuad,residual:packet.root.error,scale:packet.root.scale}}];
  }
  if(!list)throw Error('Input must have explicit point or points');
  for(const p of list)points.push({...p,inputPacket:{file:path.resolve(a.points[i]),sha256:sha(a.points[i])}});
}
if(points.length>4||new Set(points.map(p=>p.id)).size!==points.length)throw Error('Expected at most four distinct inputs');
function eq(x,y){return x.length===y.length&&x.every((z,j)=>z===y[j]);}
function mirror(B,J){for(let i=0;i<J;i++)for(let j=0;j<i;j++)B[j*J+i]=B[i*J+j];return B;}
function cosProduct(a,b,M){
  const z=new Float64Array(2*M+1);z[0]=a[0]*b[0];
  for(let j=1;j<=M;j++)z[j]=a[0]*b[j]+a[j]*b[0];
  for(let i=1;i<=M;i++)for(let j=1;j<=M;j++){
    const q=a[i]*b[j];if(i===j)z[0]+=q;else z[Math.abs(i-j)]+=q/sq2;
    z[i+j]+=q/sq2;
  }return z;
}
function sineSquare(p,M){
  const z=new Float64Array(2*M+1);
  for(let i=1;i<=M;i++)for(let j=1;j<=M;j++){
    const q=p[i-1]*p[j-1];if(i===j)z[0]+=q;else z[Math.abs(i-j)]+=q/sq2;
    z[i+j]-=q/sq2;
  }return z;
}
function analyticBL(L,M){
  const J=M+1,B=new Float64Array(J*J),at=k=>k<=M?L[k]:0;
  B[0]=L[0];for(let i=1;i<J;i++)B[i*J]=B[i]=L[i];
  for(let i=1;i<J;i++)for(let j=1;j<=i;j++)
    B[i*J+j]=i===j?L[0]+at(2*i)/sq2:(at(i+j)+at(i-j))/sq2;
  return mirror(B,J);
}
function analyticUK(U,L,pt,M){
  const K=Float64Array.from(L,(z,j)=>z-pt[j]),z=new Float64Array(M);
  for(let j=0;j<M;j++)z[j]=K[0]*U[j];
  for(let k=1;k<=M;k++)for(let l=1;l<=M;l++){
    const q=U[k-1]*K[l]/sq2;
    if(k+l<=M)z[k+l-1]+=q;
    if(k!==l)z[Math.abs(k-l)-1]+=(k>l?1:-1)*q;
  }return z;
}
function compare(point){
  const {modes:M,quadrature:N,spacing}=point.options,J=M+1,L=Float64Array.from(point.L),
    Q=Float64Array.from(point.Q),g=point.geometry,key=`M${M}-N${N}-k${spacing}`;
  if(!(N>4*M*spacing&&M>=1&&L.length===J&&Q.length===M))throw Error('Invalid point dimensions or original angular guard');
  const freq=Float64Array.from({length:M},(_,j)=>spacing*(j+1));
  if(!bases[key]){
    const cs=[],sn=[];for(let n=0;n<N;n++){
      const theta=2*Math.PI*n/N,c=[1],s=[];
      for(let j=0;j<M;j++){c.push(sq2*Math.cos(freq[j]*theta));s.push(sq2*Math.sin(freq[j]*theta));}
      cs.push(c);sn.push(s);
    }bases[key]={modes:M,quadrature:N,spacing,sqrt2:sq2,cs,sn};
  }
  const {cs,sn}=bases[key],engine=createMomentumTailEngine(point.options),old=engine.evaluateL(L,Q,g,true);
  const prior=point.sourceEvaluation;
  if(prior&&(!eq(Array.from(old.moments),prior.moments)||!eq(Array.from(old.B),prior.B)))
    throw Error('Source evaluation changed at '+point.id);
  const p=new Float64Array(M),pt=new Float64Array(J),Ucoef=new Float64Array(M);
  for(let j=0;j<M;j++){
    p[j]=-freq[j]*g.r**3*Q[j]/(sq2*g.w);pt[j+1]=freq[j]*p[j];
    Ucoef[j]=-freq[j]*L[j+1]+(freq[j]*freq[j]-1)*p[j];
  }
  if(point.precomputedCoefficients){
    for(const [name,values]of Object.entries({p,pt,U:Ucoef}))
      if(!eq(Array.from(values),point.precomputedCoefficients[name]))throw Error('Changed supplied coefficient '+name);
  }
  const zero=()=>new Float64Array(J),mat=()=>new Float64Array(J*J),flux=()=>new Float64Array(M);
  const qold=zero(),qrewrite=zero(),q2old=zero(),q2rewrite=zero(),Rq=zero(),
    Bold=mat(),Brewrite=mat(),BLnumeric=mat(),RB=mat(),
    Fold=flux(),Frewrite=flux(),UKnumeric=flux(),RF=flux();
  for(let i=0;i<J;i++)Bold[i*J+i]=Brewrite[i*J+i]=1;
  let maxQ2=0,maxRq=0,maxUK=0,maxRF=0,maxBm=0,maxRB=0;
  for(let n=0;n<N;n++){
    let P=0,Pt=0,Lv=L[0],U=0;
    for(let j=0;j<M;j++){P+=p[j]*sn[n][j];Pt+=pt[j+1]*cs[n][j+1];
      Lv+=L[j+1]*cs[n][j+1];U+=Ucoef[j]*sn[n][j];}
    const row=old.rows[n];for(const [name,value]of Object.entries({P,Pt,L:Lv,U}))
      if(value!==row[name])throw Error('Source row reconstruction differs '+point.id+' '+name);
    const K=Lv-Pt,T=2*K+K*K+g.E*P*P,u=g.w2*T,D=1-u,S=1-g.w2*P*P,
      sd=Math.sqrt(D),fc=u*(2+sd)/(2*sd*(1+sd)*(1+sd)),
      gc=g.w2*(P*P+S*T/(1+sd))/(S*sd),
      lowOld=.5*(K*K+g.E*P*P)+K*Pt,
      low=.5*(Lv*Lv+g.E*P*P-Pt*Pt),rem=T*fc+(1+K)*Pt*gc,
      oldq=.5*(K*K+g.E*P*P)+K*Pt+T*fc+(1+K)*Pt*gc,newq=low+rem,
      am=Lv+g.w2*Pt,x=Math.expm1(-1.5*Math.log1p(-u)),bm=am+(1+am)*x,
      rb=g.w2*Pt+(1+am)*x,bnew=Lv+rb,
      factor=(K+u/(1+sd)+g.w2*P*P*sd)/(S*sd),fo=U*factor,
      uk=U*K,rf=U*(1+K)*gc,fn=uk+rf;
    if(oldq!==row.quad||D!==row.D||S!==row.S||sd!==row.sd)
      throw Error('Source pointwise formula differs at '+point.id);
    maxQ2=Math.max(maxQ2,Math.abs(low));maxRq=Math.max(maxRq,Math.abs(rem));
    maxUK=Math.max(maxUK,Math.abs(uk));maxRF=Math.max(maxRF,Math.abs(rf));
    maxBm=Math.max(maxBm,Math.abs(bm));maxRB=Math.max(maxRB,Math.abs(rb));
    for(let i=0;i<J;i++){
      qold[i]+=oldq*cs[n][i]/N;qrewrite[i]+=newq*cs[n][i]/N;
      q2old[i]+=lowOld*cs[n][i]/N;q2rewrite[i]+=low*cs[n][i]/N;Rq[i]+=rem*cs[n][i]/N;
      for(let j=0;j<=i;j++){
        const ij=i*J+j;
        Bold[ij]+=bm*cs[n][i]*cs[n][j]/N;Brewrite[ij]+=bnew*cs[n][i]*cs[n][j]/N;
        BLnumeric[ij]+=Lv*cs[n][i]*cs[n][j]/N;RB[ij]+=rb*cs[n][i]*cs[n][j]/N;
      }
    }
    for(let j=0;j<M;j++){Fold[j]+=fo*sn[n][j]/N;Frewrite[j]+=fn*sn[n][j]/N;
      UKnumeric[j]+=uk*sn[n][j]/N;RF[j]+=rf*sn[n][j]/N;}
  }
  for(const B of [Bold,Brewrite,BLnumeric,RB])mirror(B,J);
  if(!eq(Array.from(qold),Array.from(old.quad))||!eq(Array.from(Bold),Array.from(old.B)))
    throw Error('Original projected output reconstruction differs at '+point.id);
  const ll=cosProduct(L,L,M),pp=sineSquare(p,M),tt=cosProduct(pt,pt,M),
    q2full=Float64Array.from(ll,(v,j)=>.5*(v+g.E*pp[j]-tt[j])),
    qanalytic=Float64Array.from(Rq,(v,j)=>q2full[j]+v),BL=analyticBL(L,M),UK=analyticUK(Ucoef,L,pt,M),
    Banalytic=Float64Array.from(BL,(v,ij)=>(ij%J===Math.floor(ij/J)?1:0)+v+RB[ij]),
    Fanalytic=Float64Array.from(UK,(v,j)=>v+RF[j]),moments=q=>Array.from(q,(v,j)=>v+L[j]),
    pref=point.options.orientation*sq2*g.r**3*g.drdx*g.w2/(Math.sqrt(12)*point.options.mu);
  const project=(q,B,F)=>({quad:Array.from(q),moments:moments(q),B:Array.from(B),nonlinearFlux:Array.from(F),
    physicalNonlinearMomentumRHS:Array.from(F,(v,j)=>pref*freq[j]*v)});
  return {id:point.id,point,basisKey:key,
    inputDefinition:'Both references freeze binary E,w2,p,pt,L,U coefficients; no E=1+w2 or w2=w*w recomputation.',
    frozenCoefficients:{L:Array.from(L),p:Array.from(p),pt:Array.from(pt),U:Array.from(Ucoef)},
    originalRowReconstructionPassed:true,originalOutputReconstructionPassed:true,
    original:project(qold,Bold,Fold),algebraSameTable:project(qrewrite,Brewrite,Frewrite),
    analyticLowProjection:project(qanalytic,Banalytic,Fanalytic),
    isolatedPolynomials:{q2OriginalNumeric:Array.from(q2old),q2RewrittenNumeric:Array.from(q2rewrite),
      q2Analytic:Array.from(q2full.slice(0,J)),BLnumeric:Array.from(BLnumeric),BLanalytic:Array.from(BL),
      UKnumeric:Array.from(UKnumeric),UKanalytic:Array.from(UK)},
    pointwiseMagnitudes:{q2:maxQ2,Rq:maxRq,UK:maxUK,fluxRemainder:maxRF,bm:maxBm,RB:maxRB},
    guard:{floor:point.options.projectionFloor,minA:old.minA,minD:old.minD,minS:old.minS},
    originalMaxQuad:old.maxQuad,originalScale:point.sourceEvaluation?.scale??null,
    physicalFluxMultipliers:Array.from(freq,m=>pref*m)};
}
const values=points.map(compare),report={status:'FOUR-OR-FEWER-local-projection-arithmetic-diagnostics',
  scope:'Standalone algebra evaluation at fixed saved inputs; no root/RHS/RK/flow or candidate engine. References are computed separately.',
  sourceSHA256:{[source]:sha(source)},scriptSHA256:sha(fileURLToPath(import.meta.url)),
  inputPackets:a.points.map(f=>({file:path.resolve(f),sha256:sha(f)})),originalRootCalls:0,bases,values};
const bytes=gzipSync(JSON.stringify(report)+'\n');if(bytes.length>=5_000_000)throw Error('File too large');
fs.writeFileSync(a.out,bytes,{flag:'wx'});
console.log(JSON.stringify({finished:true,points:values.length,allOriginalRowsAndOutputsReconstructed:true,
  bytes:bytes.length,sha256:sha(a.out)}));
