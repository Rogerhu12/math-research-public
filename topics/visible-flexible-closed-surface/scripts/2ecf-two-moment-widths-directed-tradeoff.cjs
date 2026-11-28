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
// All primitive moments in this routine enclose the full normal-angle parameter, with no node integration.
const cplus=(u,v)=>[plus(u[0],v[0]),plus(u[1],v[1])],ctimes=(u,v)=>[mul(u[0],v),mul(u[1],v)];
function signedDiv(a,b){if(b[1]<0)return div(neg(a),neg(b));return div(a,b)}
function expo(x){const [s,c]=trig(x);return [c,s]}
function primitive(n,a,b){
 if(n===0)return [sub(b,a),zero];
 const [sa,ca]=trig(mul(point(n),a)),[sb,cb]=trig(mul(point(n),b));
 return [mul(sub(sb,sa),div(one,point(Math.abs(n)))).map((x,i,z)=>n>0?x:-z[1-i]),mul(sub(ca,cb),div(one,point(Math.abs(n)))).map((x,i,z)=>n>0?x:-z[1-i])];
}
function pe(n,a,b,up){
 const h=sub(b,a);let acc=[zero,zero],z=expo(mul(point(n),a)),mag=one,nh=mul(point(n),h);
 const deg=32;
 for(let l=0;l<=deg;l++){
   const u=plus(sub(div(point(10),point(l+4)),div(point(15),point(l+5))),div(point(6),point(l+6)));
   acc=cplus(acc,ctimes(z,up?u:sub(div(one,point(l+1)),u)));
   const q=div(nh,point(l+1));z=[neg(mul(q,z[1])),mul(q,z[0])];
   mag=mul(mag,div(point(val(nh)),point(l+1)));
 }
 const remainder=mag[1];
 return ctimes(acc.map(t=>plus(t,[-remainder,remainder])),h);
}
function csMoment(gate,v1,frequencies,m){
 const U=half(P);let result=[zero,zero];
 if(!gate){
  const a=cplus(primitive(m,zero,V0),pe(m,V0,v1,false));
  return ctimes(a,div(one,kappa));
 }
 for(const [j,b] of frequencies){
   const n=m+j,weight=cplus(pe(n,V0,v1,true),primitive(n,v1,U));
   result=cplus(result,ctimes(weight,b));
 }
 return result;
}
const spectrum=[[0,one],...coef.flatMap((c,i)=>[[3*(i+1),half(c)],[-3*(i+1),half(c)]])];
function massProjection(gate,v1,co){
 const m0=csMoment(gate,v1,co,0),m1=csMoment(gate,v1,co,1),[sn,ct]=trig(half(P));
 return [m0[0],plus(m1[1],mul(div(ct,sn),m1[0])),div(m1[0],sn)];
}
function spectralCurve(width){
 const U=half(P),oldHi=dec(.548),newHi=plus(V0,dec(width));
 const oldLow=massProjection(false,oldHi,[]),oldHigh=massProjection(true,oldHi,spectrum);
 const lambda=div(sub(U,oldLow[0]),oldHigh[0]),Astar=plus(oldLow[1],mul(lambda,oldHigh[1]));
 const lo=massProjection(false,newHi,[]),hi=massProjection(true,newHi,spectrum),base=lo.map((x,i)=>plus(x,hi[i]));
 const w0=massProjection(true,newHi,[[0,one]]),w3=massProjection(true,newHi,[[3,point(.5)],[-3,point(.5)]]);
 const det=sub(mul(w0[0],w3[1]),mul(w3[0],w0[1]));
 const a1=sub(U,base[0]),a2=sub(Astar,base[1]);
 const a=signedDiv(sub(mul(a1,w3[1]),mul(w3[0],a2)),det);
 const b=signedDiv(sub(mul(w0[0],a2),mul(a1,w0[1])),det);
 const B=plus(base[2],plus(mul(a,w0[2]),mul(b,w3[2])));
 return {Astar,lambda,a,b,B,det,v1:newHi};
}
function radiusBounds(geom,n,only=null){
 const lowerBounds=Array(5).fill(0),upperBounds=Array(5).fill(0),witness=Array(5).fill(null);
 const U=half(P),ends=[zero,V0,geom.v1,U];let lower=100,upper=0,mR=0,mRR=0,vuu=0,hzuu=0;
 for(let p=0;p<3;p++){
   const l=ends[p],w=sub(ends[p+1],l);
   for(let i=0;i<n;i++){
    if(only&&!only.some(z=>z[0]===p&&z[1]===i))continue;
    const t=cell(i,n),v=plus(l,mul(t,w)),rb=baseRadius(v),[s3,c3]=trig(mul(point(3),v));
    let r0=plus(plus(rb,geom.a),mul(geom.b,c3));
    const g=p===0?zero:p===2?one:[S5(unit(i,n))[0],S5(unit(i+1,n))[1]];
    const gp=p===1?div(mul(point(30),mul(sq(t),sq(sub(one,t)))),w):zero,
    gpp=p===1?div(mul(point(60),mul(mul(t,sub(one,t)),sub(one,mul(point(2),t)))),sq(w)):zero;
    const cur=plus(div(oneMinus(g),kappa),mul(g,r0));
    lower=Math.min(lower,cur[0]);upper=Math.max(upper,cur[1]);
    let rp=neg(mul(point(3),mul(geom.b,s3))),rpp=neg(mul(point(9),mul(geom.b,c3)));
    for(let j=0;j<coef.length;j++){const k=3*(j+1),[sn,co]=trig(mul(point(k),v));
      rp=sub(rp,mul(point(k),mul(coef[j],sn)));rpp=sub(rpp,mul(point(k*k),mul(coef[j],co)));}
    const diff=sub(r0,div(one,kappa)),rv=plus(mul(gp,diff),mul(g,rp)),rvv=plus(plus(mul(gpp,diff),mul(point(2),mul(gp,rp))),mul(g,rpp));
    const k1=div(neg(rv),mul(sq(cur),cur));
    const k2=sub(div(mul(point(3),sq(rv)),mul(sq(sq(cur)),cur)),div(rvv,sq(sq(cur))));
    mR=Math.max(mR,val(k1));mRR=Math.max(mRR,val(k2));
    const ruu=sub(div(rvv,sq(cur)),div(sq(rv),mul(cur,sq(cur)))),mk=sub(ruu,div(one,cur)),kt=div(rv,sq(cur));
    const sd=plus(sq(mk),sq(kt)),norm=squareRootPositive(sd);
    const H2=div(mul(point(2),rvv),cur),k0=div(one,cur);
    const stats=[k0,k1,k2,norm,H2];
    for(let j=0;j<stats.length;j++){
      const a=stats[j],lower=Math.max(0,a[0],-a[1]),upper=val(a);
      if(lower>lowerBounds[j]){lowerBounds[j]=lower;witness[j]=[p,i]}
      upperBounds[j]=Math.max(upperBounds[j],upper);
    }
   }
 }
 return {cells:only?only.length:3*n,orderedQuantities:['k','abs_k_u','abs_k_uu','norm_(N/k)_uu','abs_(k^-2)_uu'],lowerBounds,upperBounds,witness};
}
function squareRootPositive(x){
 const l=Math.max(0,Math.sqrt(Math.max(0,x[0]))*(1-1e-8)-1e-8);
 const h=Math.sqrt(Math.max(0,x[1]))*(1+1e-8)+1e-8;
 if(l>0&&sq(point(l))[1]>x[0]||sq(point(h))[0]<x[1])throw Error('Unverified Euclidean norm bound');
 return [l,h];
}
function compute(){
 const original=spectralCurve(.04),reference=radiusBounds(original,768,[[1,661],[1,631]]);
 const widths=[.06,.08,.10,.12].map(width=>{const curve=spectralCurve(width);
  if(curve.Astar[0]<=.9027||curve.B[1]>=1.106)throw Error('Central size or moment enclosure');
  const bounds=radiusBounds(curve,2048);return {width,curve,bounds};});
 if(widths[0].bounds.upperBounds[3]>=reference.lowerBounds[3]||widths[0].bounds.upperBounds[4]>=reference.lowerBounds[4]||widths[3].bounds.lowerBounds[0]<=15)throw Error('Width comparison failed');
 return {cellsPerPiece:2048,referenceWidth:.04,referenceWitnessOnly:reference,widths};
}
if(typeof require==='function'&&require.main===module){
 const fs=require('node:fs'),arg=process.argv.slice(2),j=arg.indexOf('--out');
 if(j<0)throw Error('use --out PATH');
 fs.writeFileSync(arg[j+1],JSON.stringify({sourceSHA256:require('node:crypto').createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),result:compute()},null,2)+'\n',{flag:'wx'});
}
