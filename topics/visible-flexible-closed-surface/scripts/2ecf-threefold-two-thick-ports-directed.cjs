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
function cert(klo){const low=dec(klo),l0=dec(.915),l1=dec(1.09),tau=half(sub(sub(P,l0),l1)),high=div(sub(P,mul(low,plus(l0,tau))),plus(l1,tau));
 return {low:window(low,dec(.249)),high:window(high,dec(.31)),kHigh:high,phase:.41};}

function whole(k0) {
  const row=cert(k0);
  const kl=dec(k0),kh=row.kHigh, du=dec(.205);
  const half0=half(sub(dec(.915),dec(.41))), half1=half(sub(dec(1.09),dec(.41)));
  const patch=(l,k)=>sub(l,div(mul(sq(k),mul(sq(l),l)),point(6)));
  if(patch(half0,kl)[0]<=.249 || patch(half1,kh)[0]<=.31) throw Error('circle interval too short');
  if(row.low.offset>=.011 || row.high.offset>=.065 || kh[1]>=1.635)throw Error('mother offset');
  const twoR=dec(.23), root=dec(.115), diameter=dec(.233), largestTube=dec(.118);
  const lowTurn=k0<.30?1.43:1.37,highTurn=k0<.30?1.39:1.33;
  const lowRadius=k0<.30?div(dec(.78),mul(dec(1.875),dec(lowTurn))):div(mul(dec(.43),dec(.95)),dec(lowTurn));
  const highRadius=k0<.30?div(mul(dec(.43),dec(.95)),dec(highTurn)):div(dec(.78),mul(dec(1.875),dec(highTurn)));
  if(Math.min(lowRadius[0],highRadius[0])<=plus(root,largestTube)[1])throw Error('spine');
  const sinlo=x=>sub(x,div(mul(sq(x),x),point(6)))[0];
  if(sinlo(dec(.33))<=mul(dec(1.635),half(plus(twoR,dec(.13))))[1] ||
     sinlo(dec(.54))<=mul(dec(1.635),dec(.31))[1]) throw Error('short normals');
  // On 0<=beta<=pi/3, A >= U*cot(U), B >= U*cot(U), U=pi/3.
  const U=div(pi,point(3)),radiusLower=div(U,rootPositive3())[0];
  if(radiusLower<=.604 || plus(mul(kl,du),dec(lowTurn))[1]>=half(pi)[0])throw Error('arm orientation');
  const highNegative=Math.max(0,sub(plus(mul(kh,du),dec(highTurn)),half(pi))[1]);
  const axLen=k0<.30?2.017:1.537;
  const lowX=sub(sub(sub(point(radiusLower),dec(.011)),half(mul(kl,sq(du)))),diameter)[0];
  const highX=plus(plus(plus(plus(point(-radiusLower),dec(.065)),half(mul(kh,sq(du)))),
                       mul(out(highNegative,highNegative),dec(axLen))),diameter)[1];
  if(lowX-highX<=.30)throw Error('separation');
  const arc=k0<.30?.43:.78,last=k0<.30?1.11:.28,tilt=half(dec(highTurn));
  const h=mul(sub(one,half(sq(tilt))),plus(plus(plus(plus(root,dec(.24)),dec(arc)),dec(last)),root))[0];
  if(h<=1.19)throw Error('holding set');
  return {...row,minimumOriginalSymmetryAxisRadius:radiusLower,
    permittedMaterialHalfWidths:[patch(half0,kl)[0],patch(half1,kh)[0]],
    axisCurvatureRadiusLower:[lowRadius[0],highRadius[0]],
    distinctArmSeparation:out(lowX-highX,lowX-highX)[0],fullLimbDiameterLower:h,centralReach:.115};
}
function rootPositive3(){const v=1.732050807569;if(sq(point(v))[0]<=3)throw Error('sqrt3');return [1.7,v]}
if(typeof require==='function' && require.main===module){
  const fs=require('node:fs'),args=process.argv.slice(2),i=args.indexOf('--out');
  if(i<0)throw Error('use --out PATH');
  fs.writeFileSync(args[i+1],JSON.stringify({sourceSHA256:require('node:crypto').createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),inputs:[whole(.25),whole(.35)]},null,2)+'\n',{flag:'wx'});
}
