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
function window(k,w,h,n=192,nt=192){
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
 const ee=dec(.025),A=div(point(4),sub(one,mul(point(2),ee))),segments=[zero,ee,sub(point(.5),ee),point(.5)];
 for(let j=0;j<6*nt;j++){
   const part=Math.floor(j/nt), reflected=part>=3,p=reflected?5-part:part;
   const lo=segments[p],hi=segments[p+1],del=mul(sub(hi,lo),out((j%nt)/nt,(j%nt+1)/nt)),t=plus(lo,del);
   const tri=(u)=>div(mul(sq(u),u),point(6));
   let wa,vv,aa;
   if(p===0){aa=div(mul(A,t),ee);vv=div(mul(A,sq(t)),mul(point(2),ee));wa=div(mul(A,tri(t)),ee)}
   if(p===1){aa=A;vv=mul(A,plus(half(ee),del));wa=mul(A,plus(plus(div(sq(ee),point(6)),half(mul(ee,del))),half(sq(del))))}
   if(p===2){
     const b=sub(point(.5),mul(point(2),ee)),v0=mul(A,plus(half(ee),b)),w0=mul(A,plus(plus(div(sq(ee),point(6)),half(mul(ee,b))),half(sq(b))));
     aa=mul(A,sub(one,div(del,ee)));
     vv=plus(v0,mul(A,sub(del,div(half(sq(del)),ee))));
     wa=plus(plus(w0,mul(v0,del)),mul(A,sub(half(sq(del)),div(tri(del),ee))));
   }
   if(reflected){wa=sub(one,wa);aa=neg(aa)}
   const w0=sub(one,wa),wp=div(vv,dec(h)),wpp=div(aa,sq(dec(h)));
 for(const q of X){let hx=plus(mul(q.l,w0),mul(q.h,wa)),hs=mul(q.d,wp),xx=plus(mul(q.ll,w0),mul(q.hh,wa)),ss=mul(q.d,wpp),xs=mul(sub(q.h,q.l),wp);
 const A=plus(one,sq(hx)),D=plus(one,sq(hs)),B=mul(hx,hs),Q=plus(A,sq(hs));
 let base=point(mul(dec(8.65),root(Q))[0]);ax=Math.max(ax,val(hs));
 for(const sign of [-1,1]){let a=plus(mul(base,A),mul(point(sign),xx)),d=plus(mul(base,D),mul(point(sign),ss)),b=plus(mul(base,B),mul(point(sign),xs));mindi=Math.min(mindi,a[0],d[0]);mindet=Math.min(mindet,sub(mul(a,d),sq(b))[0])}}}
 if(mindi<=0||mindet<=0)throw Error('physical mother curvature bound failed '+JSON.stringify({mindi,mindet}));
 return {curvature:8.65,offset:off,axialSlope:ax,minDiagonal:mindi,minDet:mindet,boxes:24*n*nt};
}

function whole350(){
 const k=dec(.63),width=dec(.27),h=dec(.100),r=dec(.115),e=dec(.025),A=div(point(4),sub(one,mul(point(2),e)));
 const bound=window(k,width,.1,192,48);
 const parabolic=mul(mul(point(bound.offset),A),r);
 if(parabolic[1]>=sq(h)[0])throw Error('true shoulder bound');
 const [s,co]=trig(div(pi,point(6))),oldMin=dec(.90270993);
 const support=div(sub(sub(mul(oldMin,co),point(bound.offset)),mul(dec(.335),point(bound.axialSlope))),root(plus(one,sq(point(bound.axialSlope)))))[0];
 if(support<=r[1])throw Error('three-dimensional support');
 return {window:bound,easePeakAcceleration:A,parabolicLeft:parabolic,parabolicRight:sq(h),support,
   realCentralHalfHeight:.350,flatHalfHeight:.235,transitionEnds:[.235,.335],trueCylinderCollar:.015,
   inheritedArms:'R317, k=.63, eta=0 through 1.15, both bends +1.45; terminal straights 1.15,1.05',
   completeCentralReach:.115,armBallVerticalBound:.348};
}
if(typeof require==='function'&&require.main===module){
 const fs=require('node:fs'),args=process.argv.slice(2),i=args.indexOf('--out');
 if(i<0)throw Error('use --out PATH');
 const out={sourceSHA256:require('node:crypto').createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),result:whole350()};
 fs.writeFileSync(args[i+1],JSON.stringify(out,null,2)+'\n',{flag:'wx'});
}
