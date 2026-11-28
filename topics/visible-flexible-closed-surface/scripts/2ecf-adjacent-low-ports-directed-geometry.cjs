'use strict';
// Interval operations cover binary64 nearest rounding with a redundant relative/absolute margin.
const guard=2**-47;
function out(l,h){return [l-guard*(1+Math.abs(l)),h+guard*(1+Math.abs(h))]}
const point=x=>[x,x], plus=(a,b)=>out(a[0]+b[0],a[1]+b[1]), neg=a=>[-a[1],-a[0]], sub=(a,b)=>plus(a,neg(b));
function mul(a,b){const t=a[0]*b[0],v=a[1]*b[1],w=a[0]*b[1],z=a[1]*b[0];return out(Math.min(t,v,w,z),Math.max(t,v,w,z))}
function sq(a){const x=a[0]**2,y=a[1]**2;return out(a[0]<=0&&a[1]>=0?0:Math.min(x,y),Math.max(x,y))}
function div(a,b){if(b[0]<=0)throw Error('positive denominator required');return mul(a,out(1/b[1],1/b[0]))}
const one=point(1), zero=point(0);
function rootmin(x){if(x<0)throw Error('negative square sum');let y=Math.max(0,Math.sqrt(x)-1e-11);if(sq(point(y))[1]>x)throw Error('unverified lower sqrt');return y}
function tr(a){ // Taylor endpoint point on [-2,2], degree 26; both alternating remainders < 2^27/27! < 2e-20.
 const x=point(a), xx=neg(sq(x));let sn=x, cs=one, t=x, v=one;
 for(let i=1;i<=13;i++){t=div(mul(t,xx),point((2*i)*(2*i+1)));v=div(mul(v,xx),point((2*i-1)*2*i));sn=plus(sn,t);cs=plus(cs,v)}
 return [plus(sn,[-2e-19,2e-19]),plus(cs,[-2e-19,2e-19])]}
function localTrig(a){ // extended by endpoint Lipschitz 1 to avoid marginal overshoot of pi/2 from rational input
 let t=(a[0]+a[1])/2,p=tr(t),d=out(Math.max(t-a[0],a[1]-t),Math.max(t-a[0],a[1]-t))[1];return p.map(v=>plus(v,[-d,d]))}
// Machin's formula with atan alternating series gives 3.1415926535897932 < pi < 3.1415926535897933.

const pi=out(3.141592653589793,3.141592653589793), P=div(mul(point(2),pi),point(3));
function trig(a){
 const j=Math.round((a[0]+a[1])/Math.PI),x=sub(a,mul(point(j/2),pi));
 if(Math.max(Math.abs(x[0]),Math.abs(x[1]))>1.9)throw Error('period reduction');
 const [s,c]=localTrig(x);
 switch((j%4+4)%4){case 0:return [s,c];case 1:return [c,neg(s)];case 2:return [neg(s),neg(c)];default:return [neg(c),s]}
}
const dec=x=>out(x,x);
function root(a){const l=rootmin(a[0]),h=Math.sqrt(a[1])+1e-11;if(sq(point(h))[0]<a[1])throw Error('upper sqrt check');return [l,h]}
const val=x=>Math.max(-x[0],x[1]),half=x=>mul(point(.5),x),S3=t=>mul(sq(t),sub(point(3),mul(point(2),t)));

const clamp01=a=>[Math.max(0,Math.min(1,a[0])),Math.max(0,Math.min(1,a[1]))];
const union=(a,b)=>[Math.min(a[0],b[0]),Math.max(a[1],b[1])];
const splus=(a,v)=>a.map((b,i)=>plus(b,v[i]));
const sminus=(a,v)=>a.map((b,i)=>sub(b,v[i]));
const sv=(a,v)=>a.map(x=>mul(x,v));
const dot=(a,b)=>plus(mul(a[0],b[0]),mul(a[1],b[1]));
const perp=a=>[neg(a[1]),a[0]];
const pol=(angle,sgn=1)=>{let [s,c]=trig(angle);return sv([c,s],point(sgn));};
const mag=a=>root(plus(sq(a[0]),sq(a[1])));
const oneMinus=x=>sub(one,x);
const clipSq=a=>[Math.max(0,a[0]),Math.max(0,a[1])];
const posRoot=a=>{const u=clipSq(a);if(u[0]>1e-9)return root(u);const h=Math.sqrt(u[1])+1e-6;if(sq(point(h))[0]<u[1])throw Error("cap sqrt");return [0,h];};
const unit=(i,n)=>div(point(i),point(n));
const cell=(i,n)=>[unit(i,n)[0],unit(i+1,n)[1]];
function bez(a,coef) {
  let z=coef.map(x=>point(x));const b=oneMinus(a);
  while(z.length>1){const s=[];for(let j=0;j+1<z.length;j++)s.push(plus(mul(b,z[j]),mul(a,z[j+1])));z=s}
  return z[0];
}
const S5=t=>bez(t,[0,0,0,1,1,1]);
function betaIntegral(t){
  // Integral of the degree-15 Bernstein CDF with coefficients 0 (j<8), 1 otherwise.
  const z=Array.from({length:17},(_,i)=>Math.max(0,i-8)/16);
  return bez(t,z);
}
const coeffs=[0.09999976505231697,0.00017340635052370438,-0.000020726030862500148,2.732239542665825e-9,1.364904959536114e-9,-6.697024595314116e-10,2.5420195020236015e-11,2.7693941053364423e-11,2.279645039764186e-11,7.050341026639808e-10,5.749608505622311e-11,2.4233142751359304e-10];
const kappa=dec(.63),etaMax=dec(1.15),V0=dec(.536),V1=dec(.548),portWidth=dec(.27);
const coef=coeffs.map((x,j)=>mul(point((1-9*(j+1)**2)*((j+1)%2?-1:1)),point(x)));
const derivativeMax=coef.reduce((s,a,j)=>plus(s,mul(point(3*(j+1)),point(val(a)))),zero)[1];
function baseRadius(v){
 const m=(v[0]+v[1])/2,[,c]=trig(mul(point(3),point(m)));
 let cm=one,ck=c,res=one;
 for(const b of coef){res=plus(res,mul(b,ck));[cm,ck]=[ck,sub(mul(mul(point(2),c),ck),cm)]}
 const d=mul(point(derivativeMax),point(out(Math.max(m-v[0],v[1]-m),Math.max(m-v[0],v[1]-m))[1]))[1];
 return plus(res,[-d,d]);
}
function curve(n=4096){
 const U=half(P),ends=[zero,V0,V1,U];
 let constant=zero,part=zero;
 const panels=[];
 let baseMin=Infinity;
 for(let j=0;j<3;j++){
   const a=ends[j],wd=sub(ends[j+1],a),dv=div(wd,point(n));
   for(let i=0;i<n;i++){
     const t=cell(i,n),v=plus(a,mul(wd,t)),rb=baseRadius(v);
     baseMin=Math.min(baseMin,rb[0]);
     const g=j===0?zero:j===2?one:[S5(unit(i,n))[0],S5(unit(i+1,n))[1]];
     const A=div(oneMinus(g),kappa),B=mul(g,rb);
     constant=plus(constant,mul(dv,A));part=plus(part,mul(dv,B));
     panels.push([v,dv,A,B]);
   }
 }
 const scale=div(sub(U,constant),part);
 let si=zero,co=zero,min=Infinity,max=0;
 for(const [v,dv,a,b] of panels){
   const r=plus(a,mul(scale,b)),[s,c]=trig(v);
   min=Math.min(min,r[0]);max=Math.max(max,r[1]);
   si=plus(si,mul(dv,mul(r,s)));co=plus(co,mul(dv,mul(r,c)));
 }
 const [s,c]=trig(U),A=plus(si,mul(div(c,s),co)),B=div(co,s);
 if(scale[0]<=0 || min<=0)throw Error('curvature radius');
 return {A,B,scale,min,max,baseMin,k:kappa,rmax:div(one,point(min))[1],panels:panels.length};
}
function flat(k,width,n=128){
 const w=dec(width),f=dec(.234),L=sub(w,f),e=div(L,point(20)),lev=div(mul(k,sub(div(w,L),dec(.025))),dec(.95));
 const stops=[f,plus(f,e),sub(w,e),w];let integral=zero;
 for(let j=0;j<3;j++){
   const width=sub(stops[j+1],stops[j]),dx=div(width,point(n));
   for(let i=0;i<n;i++){
     const t=cell(i,n),it=mul(mul(sq(t),t),sub(one,half(t)));let v;
     if(j===0)v=mul(mul(lev,e),it);
     else if(j===1)v=mul(lev,plus(half(e),mul(width,t)));
     else v=plus(mul(lev,sub(L,mul(point(1.5),e))),mul(e,plus(mul(lev,t),mul(sub(k,lev),it))));
     integral=plus(integral,mul(dx,div(v,root(sub(one,sq(v))))));
   }
 }
 return plus(neg(div(mul(k,sq(w)),plus(one,root(sub(one,sq(mul(k,w))))))),integral);
}
function frame2(cur,i,eta,f){
 const k=kappa,ref=mul(point(i),P),e=pol(plus(ref,eta));
 const n=pol(plus(plus(ref,eta),mul(k,sub(half(etaMax),eta)))),t=perp(n);
 const orig=splus(sv(e,sub(cur.A,div(one,k))),sv(n,div(one,k)));
 return {o:splus(orig,sv(n,f)),n,t,orig,offset:f};
}
function turn(t,short,w){
 if(!short)return mul(w,S5(t));
 const e=dec(.05),cut=dec(.95),sqint=y=>mul(mul(sq(y),y),sub(one,half(y)));
 const pieces=[];
 if(t[0]<=e[1])pieces.push(div(mul(e,sqint(clamp01(div(t,e)))),cut));
 if(t[1]>=e[0]&&t[0]<=cut[1])pieces.push(div(sub(t,half(e)),cut));
 if(t[1]>=cut[0])pieces.push(div(sub(cut,mul(e,sqint(clamp01(div(oneMinus(t),e))))),cut));
 return mul(w,pieces.reduce(union));
}
const db=mul(dec(.115),plus(one,mul(dec(.004),half(pi)))),tube=sub(dec(.233),db),rr=dec(.115);
function cap(theta){
 const [s0,c0]=trig(theta),s=clamp01(s0),c=clamp01(c0),g=div(sub(tube,rr),[1,1.254]);
 // 1 <= J <= sqrt(pi/2) < 1.254 by Cauchy-Schwarz; the terminal integral lies between cos(theta) and pi/2-theta.
 const dist=plus(mul(rr,s),mul(mul(point(2),g),posRoot(s)));
 const rad=[mul(plus(rr,point(g[0])),c)[0],Math.min(sub(tube,mul(rr,sub(one,c)))[1],plus(mul(rr,c),mul(g,sub(half(pi),theta)))[1])];
 return [dist,rad];
}
function limbRows(spec,n=768){
 const [w0,short,Llast]=spec,w=dec(w0),last=dec(Llast),L=short?dec(.43):dec(.78);
 const start=plus(db,dec(.24)),rows=[{d:[0,start[1]],t:zero,rad:dec(.233),b:zero}];
 let d=start,t=zero,bprev=turn(zero,short,w);
 const add=(delta,co,si,r,b)=>({d:plus(d,mul(delta,co)),t:plus(t,mul(delta,si)),rad:r,b});
 for(let i=0;i<n;i++){
   const bn=turn(unit(i+1,n),short,w),b=union(bprev,bn),[si,co]=trig(b),ds=div(L,point(n));
   rows.push(add([0,ds[1]],co,si,tube,b));d=plus(d,mul(ds,co));t=plus(t,mul(ds,si));bprev=bn;
 }
 const [si,co]=trig(w);
 for(let j=0;j<32;j++)rows.push(add(mul(last,cell(j,32)),co,si,tube,w));
 d=plus(d,mul(last,co));t=plus(t,mul(last,si));
 for(let j=0;j<32;j++){
   const [dist,rad]=cap(mul(half(pi),cell(j,32)));rows.push(add(dist,co,si,rad,w));
 }
 function witness(index,side){
   const [dist,rad]=cap(mul(half(pi),unit(index,80)));
   return [sub(plus(d,mul(dist,co)),mul(point(side),mul(rad,si))),
           plus(plus(t,mul(dist,si)),mul(point(side),mul(rad,co)))];
 }
 return {rows,witness};
}
function pointInFrame(f,x){return splus(f.o,splus(sv(f.n,x[0]),sv(f.t,x[1])))}
function holdXY(p,from,to){const a=sminus(p,from.orig);return splus(to.orig,splus(sv(to.n,dot(a,from.n)),sv(to.t,dot(a,from.t))))}
function spatial(rows,f){
 return rows.map(q=>{const [si,co]=trig(q.b),c=pointInFrame(f,[q.d,q.t]);
  return {c,w:sminus(sv(f.t,co),sv(f.n,si)),r:q.rad};});
}
function support(rows,e,z){
 let hi=-Infinity,lo=Infinity;
 for(const q of rows){
  const c=dot(q.c,e),a=dot(q.w,e),rad=q.r[1]*Math.sqrt(Math.max(0,sq(a)[1]+sq(z)[1]));
  // Directed verification of the radius without assuming sqrt is correctly rounded.
  const dr=out(rad+1e-6,rad+1e-6)[1];
  if(q.r[1]>0 && sq(point(dr))[0]<mul(sq(point(q.r[1])),plus(sq(a),sq(z)))[1])throw Error('projected radius');
  hi=Math.max(hi,plus(c,point(dr))[1]);lo=Math.min(lo,sub(c,point(dr))[0]);
 }
 return [lo,hi];
}
function window(k,w,n=192,nt=192){
 const flat=dec(.234),L=sub(w,flat),e=div(L,point(20)),level=div(mul(k,sub(div(w,L),dec(.025))),dec(.95));
 const rad=[[zero,flat],[flat,plus(flat,e)],[plus(flat,e),sub(w,e)],[sub(w,e),w]],X=[];
 for(let j=0;j<4;j++){let lo=rad[j][0],hi=rad[j][1],span=sub(hi,lo),dx=div(span,point(n));
 for(let i=0;i<n;i++){
 const t=out(i/n,(i+1)/n),x=plus(lo,mul(span,t)),it=mul(mul(sq(t),t),sub(one,half(t)));let v,dd;
 if(j===0){v=zero;dd=zero}
 else if(j===1){v=mul(mul(level,e),it);dd=mul(level,S3(t))}
 else if(j===2){v=mul(level,plus(half(e),mul(span,t)));dd=level}
 else{v=plus(mul(level,sub(L,mul(point(1.5),e))),mul(e,plus(mul(level,t),mul(sub(k,level),it))));dd=plus(level,mul(sub(k,level),S3(t)))}
 const p=mul(k,x),r0=root(sub(one,sq(p))),r1=root(sub(one,sq(v)));
 X.push({l:neg(div(p,r0)),h:neg(div(v,r1)),ll:neg(div(k,mul(sq(r0),r0))),hh:neg(div(dd,mul(sq(r1),r1))),dx});
 }}
 let delta=zero,off=0;for(let i=X.length-1;i>=0;i--){let q=X[i],v=neg(mul(sub(q.h,q.l),q.dx));q.d=plus(delta,[Math.min(0,v[0]),Math.max(0,v[1])]);delta=plus(delta,v);off=Math.max(off,val(q.d))}
 let mindi=1e5,mindet=1e5,ax=0;
 for(let j=0;j<nt;j++){let t=out(j/nt,(j+1)/nt),S=z=>mul(mul(sq(z),z),plus(point(10),mul(z,plus(point(-15),mul(point(6),z))))),wa=[Math.max(0,S(point(t[0]))[0]),Math.min(1,S(point(t[1]))[1])],w0=sub(one,wa),
 wp=div(mul(point(30),mul(sq(t),sq(sub(one,t)))),dec(.30)),wpp=div(mul(point(60),mul(mul(t,sub(one,t)),sub(one,mul(point(2),t)))),dec(.09));
 for(const q of X){let hx=plus(mul(q.l,w0),mul(q.h,wa)),hs=mul(q.d,wp),xx=plus(mul(q.ll,w0),mul(q.hh,wa)),ss=mul(q.d,wpp),xs=mul(sub(q.h,q.l),wp);
 const A=plus(one,sq(hx)),D=plus(one,sq(hs)),B=mul(hx,hs),Q=plus(A,sq(hs));
 let base=point(mul(dec(8.65),root(Q))[0]);ax=Math.max(ax,val(hs));
 for(const sign of [-1,1]){let a=plus(mul(base,A),mul(point(sign),xx)),d=plus(mul(base,D),mul(point(sign),ss)),b=plus(mul(base,B),mul(point(sign),xs));mindi=Math.min(mindi,a[0],d[0]);mindet=Math.min(mindet,sub(mul(a,d),sq(b))[0])}}}
 if(mindi<=0||mindet<=0)throw Error('physical mother curvature bound failed '+JSON.stringify({mindi,mindet}));
 return {curvature:8.65,offset:off,axialSlope:ax,minDiagonal:mindi,minDet:mindet,boxes:4*n*nt};
}
const specs=[[1.45,true,1.15],[1.45,true,1.05]];
function prelim(n,m){
 const cur=curve(n),f=flat(kappa,.27),limbs=specs.map(x=>limbRows(x,m)),fr0=[0,1].map(i=>frame2(cur,i,zero,f)),fr1=[0,1].map(i=>frame2(cur,i,etaMax,f));
 const exp=[0,1].map(i=>spatial(limbs[i].rows,fr0[i])),cmp=[0,1].map(i=>spatial(limbs[i].rows,fr1[i]));
 return {cur,f,limbs,fr0,fr1,exp,cmp};
}
function whole(){
 const {cur,f,limbs,fr0,fr1,exp,cmp}=prelim(4096,768);
 const W=window(kappa,portWidth),r=dec(.115);
 const patch=div(trig(sub(V0,mul(kappa,half(etaMax))))[0],kappa)[0];
 const boundSourceNormals=mul(point(cur.rmax),half(plus(dec(.230),mul(point(2),point(W.offset)))))[1];
 if(patch<=portWidth[1] || trig(dec(1.15))[0][0]<=boundSourceNormals ||
    trig(dec(.18))[0][0]<=mul(kappa,portWidth)[1] || 2*(1.15+.18)>=pi[0])throw Error('central short normal angle');
 const minAxis=Math.min(cur.A[0],cur.B[0]),maxAxis=Math.max(cur.A[1],cur.B[1]);
 const co=trig(div(pi,point(6)))[1];
 const motherRho=plus(div(point(maxAxis),co),point(W.offset))[1];
 const motherSupport=div(sub(sub(mul(point(minAxis),co),point(W.offset)),mul(dec(.77),point(W.axialSlope))),root(plus(one,sq(point(W.axialSlope)))))[0];
 const radiusOfTurn=div(mul(dec(.43),dec(.95)),dec(1.45))[0];
 if(radiusOfTurn<=plus(r,tube)[1] || motherSupport<=r[1] || W.offset>=.066)throw Error('mother or tubular arm');
 const delta=mul(mul(mul(point(2),root(point(3))),sub(div(one,kappa),cur.A)),trig(mul(kappa,half(etaMax)))[0]);
 let sep=Infinity;
 for(let i=0;i<32;i++){
   const eta=mul(etaMax,cell(i,32)),parts=limbs.map((l,j)=>spatial(l.rows,frame2(cur,j,eta,f)));
   const a=support(parts[0],[one,zero],zero),b=support(parts[1],[one,zero],zero);
   sep=Math.min(sep,sub(point(a[0]),point(b[1]))[0]);
 }
 if(sep<=.23)throw Error('inter-arm contact');
 const p=pointInFrame(fr0[0],limbs[0].witness(19,-1)),q=pointInFrame(fr0[1],limbs[1].witness(72,-1));
 const low=pointInFrame(fr0[0],limbs[0].witness(59,-1)),w=holdXY(low,fr0[1],fr1[1]);
 const e=pol(mul(pi,div(point(42),point(72)))),mx=Math.max(...cmp.map(v=>support(v,e,zero)[1]));
 const held=div(sub(dot(w,e),point(mx)),mag(e))[0];
 const na=96,ne=20,all=cmp.flat(),planes=[];
 let maxWidth=0,maxPlanar=0;
 for(let j=0;j<na;j++){
   const eh=pol(mul(mul(pi,point(2)),unit(j,na))),a=support(all,eh,zero);
   maxPlanar=Math.max(maxPlanar,a[1]);planes.push({eh,a});
 }
 for(let k=0;k<=ne;k++){
   const [s,c]=trig(mul(half(pi),unit(k,ne)));
   for(const {eh,a} of planes){
     const h=k?support(all,sv(eh,c),s):a;
     maxWidth=Math.max(maxWidth,sub(point(h[1]),point(h[0]))[1]);
   }
 }
 const cosAng=trig(div(pi,point(na)))[1],cosEl=trig(plus(div(pi,point(na)),div(pi,point(4*ne))))[1];
 const planar=div(point(maxPlanar),cosAng)[1],diam=div(point(maxWidth),cosEl)[1];
 const H=mul(plus(plus(plus(plus(r,dec(.24)),dec(.43)),dec(1.05)),r),trig(half(dec(1.45)))[1])[0];
 return {k:cur.k,phase:etaMax,curve:cur,flatOffset:f,fullWindow:W,sourceShortNormalCap:boundSourceNormals,
   admissiblePortHalfWidth:patch,relativeTranslationMagnitude:delta,minimumSpineRadius:radiusOfTurn,
   motherPlanarRadiusUpper:motherRho,minimumMotherSupport:motherSupport,fullPhaseDistinctArmSeparation:sep,
   centralReach:.115,holdingPatchDiameterLower:H,expandedDiameterLower:mag(sminus(p,q))[0],
   compactWholeArmDiameterUpper:diam,compactWholeArmPlanarRadiusUpper:planar,
   expandedLowWitnessInCompactWorld:w,actualWitnessPlanarRadiusLower:mag(w)[0],heldFromAllCompactArmPoints:held,
   witnesses:{expanded:[19,-1,72,-1],heldExpanded:[59,-1],supportAngleInPiUnits:[42,72]},
   axisCells:768,phaseIntervals:32,angles:[na,ne]};
}
if(typeof require==='function' && require.main===module){
 const fs=require('node:fs'),args=process.argv.slice(2),i=args.indexOf('--out');
 if(i<0)throw Error('use --out PATH');
 fs.writeFileSync(args[i+1],JSON.stringify({sourceSHA256:require('node:crypto').createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),result:whole()},null,2)+'\n',{flag:'wx'});
}
