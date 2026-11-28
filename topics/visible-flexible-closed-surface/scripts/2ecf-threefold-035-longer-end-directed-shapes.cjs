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
function trig(a){ // extended by endpoint Lipschitz 1 to avoid marginal overshoot of pi/2 from rational input
 let t=(a[0]+a[1])/2,p=tr(t),d=out(Math.max(t-a[0],a[1]-t),Math.max(t-a[0],a[1]-t))[1];return p.map(v=>plus(v,[-d,d]))}
// Machin's formula with atan alternating series gives 3.1415926535897932 < pi < 3.1415926535897933.

const pi=out(3.141592653589793,3.141592653589793), P=div(mul(point(2),pi),point(3));
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
function curve(k0,n=2048){
 const l0=dec(.915),l1=dec(1.09),tau=half(sub(sub(P,l0),l1)),a=half(l0),end=plus(a,tau),U=half(P);
 const k1=div(sub(P,mul(k0,plus(l0,tau))),plus(l1,tau));
 let sinInt=zero,cosInt=zero;
 for(let j=0;j<3;j++){
   const x0=[zero,a,end][j],wd=[a,tau,sub(U,end)][j],dx=div(wd,point(n));
   function angle(t){
     const s=plus(x0,mul(wd,t)),q=sub(k1,k0);
     if(j===0)return mul(k0,s);
     if(j===1)return plus(mul(k0,s),mul(mul(q,tau),betaIntegral(t)));
     return plus(mul(k0,s),mul(q,plus(sub(s,end),half(tau))));
   }
   let last=angle(zero);
   for(let i=0;i<n;i++){
     const next=angle(unit(i+1,n)),b=[last[0],next[1]];
     const [sn,co]=trig(b);sinInt=plus(sinInt,mul(dx,sn));cosInt=plus(cosInt,mul(dx,co));last=next;
   }
 }
 const [s,c]=trig(U);
 return {k:[k0,k1],ray:[plus(sinInt,mul(div(c,s),cosInt)),div(cosInt,s)]};
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
function frame2(cur,i,eta){
 const k=cur.k[i],f=flat(k,i?.31:.249),r=cur.ray[i],sgn=i?-1:1;
 const e=pol(eta,sgn),n=pol(plus(eta,mul(k,sub(dec(.205),eta))),sgn),t=perp(n);
 const orig=splus(sv(e,sub(r,div(one,k))),sv(n,div(one,k)));
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
function both(klo){
 const cur=curve(dec(klo)),sp=klo===.25?[[1.43,false,.73],[-1.39,true,1.11]]:[[1.37,true,.98],[-1.33,false,.46]];
 const limbs=sp.map(x=>limbRows(x)),fr0=[0,1].map(i=>frame2(cur,i,zero)),fr1=[0,1].map(i=>frame2(cur,i,dec(.41)));
 const exp=[0,1].map(i=>spatial(limbs[i].rows,fr0[i])),cmp=[0,1].map(i=>spatial(limbs[i].rows,fr1[i]));
 const li=klo===.25?12:23,hi=klo===.25?19:12,heldIdx=klo===.25?63:76;
 const p=pointInFrame(fr0[0],limbs[0].witness(li,-1)),q=pointInFrame(fr0[1],limbs[1].witness(hi,1));
 const w0=pointInFrame(fr1[0],limbs[0].witness(heldIdx,-1)),w=holdXY(w0,fr1[1],fr0[1]);
 // Unnormalized high-shoulder material coordinates near the separating support direction.
 const dir=klo===.25?[dec(-.19),dec(-.98)]:[dec(-.031),point(-1)];
 const E=splus(sv(fr0[1].n,dir[0]),sv(fr0[1].t,dir[1]));
 const mx=Math.max(...exp.map(v=>support(v,E,zero)[1]));
 const held=div(sub(dot(w,E),point(mx)),mag(dir))[0];
 // Cover the unit sphere in azimuth and elevation. z reflection gives both elevation signs.
 const na=96,ne=20,ranges=[0,0],planes=[];
 const all=[...cmp[0],...cmp[1]];let maxWidth=0,maxPlanar=0;
 for(let j=0;j<na;j++){
   const quadrant=Math.floor(4*j/na),angle=mul(half(pi),unit(j%(na/4),na/4)),e0=pol(angle);
   let eh=e0;for(let k=0;k<quadrant;k++)eh=perp(eh);
   const a=support(all,eh,zero);maxPlanar=Math.max(maxPlanar,a[1]);planes.push({eh,a});
 }
 for(let k=0;k<=ne;k++){
   const [s,c]=trig(mul(half(pi),unit(k,ne)));
   for(const {eh,a} of planes){
     const s0=k?support(all,sv(eh,c),s):a;
     maxWidth=Math.max(maxWidth,sub(point(s0[1]),point(s0[0]))[1]);
   }
 }
 const cosAng=trig(div(pi,point(na)))[1],cosEl=trig(plus(div(pi,point(na)),div(pi,point(4*ne))))[1];
 const planar=div(point(maxPlanar),cosAng)[1],diam=div(point(maxWidth),cosEl)[1];
 return {klo,centerRays:cur.ray,portOffsets:fr0.map(f=>f.offset),expandedPair:[p,q],expandedDiameterLower:mag(sminus(p,q))[0],
    compactWholeFingerDiameterUpper:diam,compactWholeFingerPlanarRadiusUpper:planar,
    compactWitnessInExpandedActualSpace:w,witnessPlanarRadiusLower:mag(w)[0],heldAwayFromAllExpandedFingers:held,
    witnesses:{expandedLowCapAngleUnitsPiOver160:li,expandedHighCapAngleUnitsPiOver160:hi,
               heldLowCapAngleUnitsPiOver160:heldIdx,meridianCosChi:[-1,1,-1]},
    directionCover:[na,ne],spineCells:768};
}

if(typeof require==='function'&&require.main===module){
 const fs=require('node:fs'),args=process.argv.slice(2),j=args.indexOf('--out');
 if(j<0)throw Error('use --out PATH');
 const r={sourceSHA256:require('node:crypto').createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),groups:[both(.35)]};
 fs.writeFileSync(args[j+1],JSON.stringify(r,null,2)+'\n',{flag:'wx'});
}
