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
const pi=out(3.141592653589793,3.141592653589793), half=div(pi,point(2)), k0=div(one,point(5)), kh=div(sub(pi,point(.3)),sub(pi,point(1.5)));
const choose=(n,k)=>{let z=1;for(let i=0;i<k;i++)z=z*(n-i)/(i+1);return z};
function bern(x,n,c){let s=zero,p=[one],q=[one];for(let i=1;i<=n;i++){p.push(mul(p[i-1],x));q.push(mul(q[i-1],sub(one,x)))}for(let i=0;i<=n;i++){if(c(i))s=plus(s,mul(mul(p[i],q[n-i]),point(choose(n,i)*c(i))))}return s}
function baseval(v){const x=mul(point(2),sub(v,point(.5))),clamp=a=>Math.max(0,Math.min(1,a)),xi=[clamp(x[0]),clamp(x[1])],plusPart=[Math.max(0,v[0]-1),Math.max(0,v[1]-1)];let k=plus(k0,mul(sub(kh,k0),bern(xi,15,i=>i>=8?1:0)));let b=plus(mul(k0,v),mul(sub(kh,k0),plus(mul(point(.5),bern(xi,16,i=>Math.max(0,i-8)/16)),plusPart)));return [k,b]}
function angles(n){let step=div(half,point(n)),levels=[],kx=[],s=[],c=[],cum=[zero],rev=[];
 for(let i=0;i<=n;i++){let v=mul(step,point(i)),[k,b]=baseval(v),[sn,cs]=trig(b);levels.push(v);kx.push(k);s.push(sn);c.push(cs)}
 let box=(a,b)=>[Math.min(a[0],b[0]),Math.max(a[1],b[1])];
 for(let i=0;i<n;i++)cum.push(plus(cum[i],mul(step,box(c[i],c[i+1]))));
 rev[n]=zero;for(let i=n-1;i>=0;i--)rev[i]=plus(rev[i+1],mul(step,box(s[i],s[i+1])));
 let out=[];for(let i=0;i<n;i++){const [sn,cs]=trig(box(levels[i],levels[i+1]));
 out.push({g:[box(rev[i+1],rev[i]),box(cum[i],cum[i+1]),zero],T:[neg(box(s[i],s[i+1])),box(c[i],c[i+1]),zero],N:[box(c[i],c[i+1]),box(s[i],s[i+1]),zero],e:[cs,sn,zero],et:[neg(sn),cs,zero],k:box(kx[i],kx[i+1])})}return out}
const scale=(s,v)=>v.map(t=>mul(s,t)),addv=(v,w)=>v.map((t,i)=>plus(t,w[i])),subv=(v,w)=>v.map((t,i)=>sub(t,w[i]));
const dot=(v,w)=>plus(plus(mul(v[0],w[0]),mul(v[1],w[1])),mul(v[2],w[2]));
const norm2=v=>plus(plus(sq(v[0]),sq(v[1])),sq(v[2]));
const cross=(a,b)=>[sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0]))];
const R=out(.94,.94),L=out(.58,.58),gate=out(.10,.10),ez=[zero,zero,one];
function bases(v){let w=sub(one,v),v2=sq(v),w2=sq(w),w3=mul(w2,w);return [
 [mul(w3,plus(one,mul(v,plus(point(3),mul(point(6),v))))),mul(mul(v,w3),plus(one,mul(point(3),v))),mul(point(.5),mul(v2,w3))],
 [mul(point(-30),mul(v2,w2)),mul(w2,plus(one,mul(v,sub(point(2),mul(point(15),v))))),mul(mul(v,w2),sub(one,mul(point(2.5),v)))],
 [mul(point(-60),mul(mul(v,w),sub(one,mul(point(2),v)))),mul(point(-12),mul(mul(v,w),sub(point(3),mul(point(5),v)))),mul(w,plus(one,mul(v,sub(mul(point(10),v),point(8)))))]
 ]}
function corrections(B,der,d,eps){let res=[zero,zero,zero];for(let j=0;j<3;j++){let fact=B[der][j];for(let t=0;t<j-der;t++)fact=mul(fact,gate);for(let t=0;t<der-j;t++)fact=div(fact,gate);res=res.map((r,i)=>plus(r,mul(fact,out(-eps[d][j][i],eps[d][j][i]))))}return res}
function closureBlock(a,b,isgate,angs,m,eps,K){let stats={area2:1e6,principalMinor:1e6,det:1e6,bad:0};const invL=div(one,L);
 for(let j=0;j<m;j++){const rad=plus(a,mul(sub(b,a),out(j/m,(j+1)/m))),t=div(rad,L),B=bases(t),q=B[0][0],qd=mul(B[1][0],invL),qdd=mul(mul(B[2][0],invL),invL);const uq=sub(one,q);
 const D=isgate?bases(div(rad,gate)):null;
 const corr=(i,d)=>D?corrections(D,i,d,eps):[zero,zero,zero],dv=corr(1,0),du=corr(0,1),dvv=corr(2,0),dvu=corr(1,1),duu=corr(0,2);
 for(const {g,T,N,e,et,k} of angs){const delta=subv(g,scale(R,e)),deltaU=subv(T,scale(R,et));
 const v=addv(addv(scale(qd,delta),ez),dv),u=addv(addv(scale(q,T),scale(mul(uq,R),et)),du),vv=addv(scale(qdd,delta),dvv),vu=addv(scale(qd,deltaU),dvu),uu=addv(subv(scale(neg(mul(q,k)),N),scale(mul(uq,R),e)),duu);
 const normal=cross(v,u), ar=norm2(normal)[0],scaleK=point(mul(point(K),point(rootmin(ar)))[0]), E=norm2(v),G=norm2(u),F=dot(v,u),e2=dot(normal,vv),f2=dot(normal,vu),g2=dot(normal,uu);
 stats.area2=Math.min(stats.area2,ar);for(let sig of [-1,1]){let A=plus(mul(scaleK,E),mul(point(sig),e2)),C=plus(mul(scaleK,G),mul(point(sig),g2)),B=plus(mul(scaleK,F),mul(point(sig),f2));let det=sub(mul(A,C),sq(B))[0];stats.principalMinor=Math.min(stats.principalMinor,A[0],C[0]);stats.det=Math.min(stats.det,det);if(det<=0||A[0]<=0||C[0]<=0)stats.bad++}}}
 return stats}
function cap(m){let highMeridian=0,highParallel=0;let H=out(.32,.32);for(let i=0;i<m;i++){let t=out(i/m,(i+1)/m),t2=sq(t),t4=sq(t2),t6=mul(t4,t2),d=plus(mul(sq(H),sub(one,t4)),mul(point(4),mul(sq(R),t6)));let km2=div(sq(mul(mul(H,R),sub(mul(point(6),t2),mul(point(2),t6)))),mul(sq(d),d)),kp2=div(sq(H),mul(sq(R),d));highMeridian=Math.max(highMeridian,km2[1]);highParallel=Math.max(highParallel,kp2[1])}return {meridianSquared:highMeridian,parallelSquared:highParallel}}
function jetLimits() {
  // R303 section 2 supplies rows 0,1. In row 2 each generous threshold
  // is checked separately against its own exact terminal Fourier/ramp receipt.
  return [
    [[.0016,.0016,.000025],[.051,.051,.00085],[.15,.15,.0031]],
    [[.011,.011,.00014],[.26,.26,.0053],[3.3,3.3,.08]],
    [[2.4,2.4,.08],[32,32,1.6],[320,320,8]]
  ];
}
function compute() {
  const angular=192, gateCells=64, tailCells=100, capCells=1024;
  const dirs=angles(angular), eps=jetLimits(), bound=8.6875;
  const first=closureBlock(zero,gate,true,dirs,gateCells,eps,bound);
  const remainder=closureBlock(gate,L,false,dirs,tailCells,eps,bound);
  const capResult=cap(capCells);
  if(first.bad || remainder.bad || capResult.meridianSquared>=64 || capResult.parallelSquared>=1.14)
    throw Error('curvature positivity failed');
  return {schema:'C3-wide-closing-cap-directed-matrix-certificate-v3',
    angularQuarter:angular, gateCells, tailCells,capCells, allQuadrants:4,
    gate:first,remainder,cap:capResult,curvatureUpper:bound,
    terminalSecondEnvelope:eps[2],closedReachRadius:0.115};
}
function upperDyadic(s) {
  const [a,b]=String(s).split('/').map(BigInt), d=b===undefined?1n:b, den=1n<<40n;
  if(a<0 || d<=0) throw Error('nonnegative rational required');
  // Round upwards before conversion. All consumed quantities are below 2^12.
  const m=(a*den+d-1n)/d;
  if(m>1n<<52n) throw Error('rational out of range');
  return Number(m)/Number(den);
}
function withRamp(record,ramp) {
  if(ramp.schema!=='true-H65-continuous-ramp-second-jets-Bernstein-and-fourth-order-inlet-v1')
    throw Error('different ramp schema');
  if(!/^[a-f0-9]{64}$/.test(ramp.fieldSHA256))throw Error('ramp SHA-256 missing');
  const upperRow=row=>row.map(upperDyadic);
  function normBounds(row,xy,z) {
    const a=upperRow(row);
    if(plus(sq(point(a[0])),sq(point(a[1])))[1]>=sq(out(xy,xy))[0] || a[2]>=out(z,z)[0])
      throw Error('actual horizontal/vertical jet bound exceeds stated envelope: '+a+' vs '+xy+','+z);
    return a;
  }
  record.velocityFromVertical=normBounds(ramp.velocityFromVertical,.06,.001);
  record.angularFromCenter=normBounds(ramp.angularFromCenter,.012,.00015);
  record.terminalValue=ramp.terminalValue.map((q,j)=>normBounds(q,jetLimits()[0][j][0],jetLimits()[0][j][2]));
  // Replay the absolute spatial cushions actually embedded in the published
  // integer covers rather than transferring a field with a different file SHA.
  const normUpper=(x,y)=>{
    const a=plus(sq(point(x)),sq(point(y)))[1];
    const q=Math.sqrt(a)+1e-11;
    if(sq(point(q))[0]<a)throw Error('unverified upper sqrt');
    return q;
  };
  const dp=record.terminalValue;
  const norms=dp.map(x=>normUpper(x[0],x[1]));
  function gateError(w){
    return plus(plus(point(w[0]),mul(out(.04,.04),point(w[1]))),
      mul(out(.0005,.0005),point(w[2])))[1];
  }
  const dx=record.velocityFromVertical;
  record.shapeCoverEnvelope=[
    mul(out(.06,.06),point(normUpper(dx[0],dx[1])))[1],
    mul(out(.06,.06),point(dx[2]))[1],
    gateError(norms),gateError(dp.map(v=>v[2]))
  ];
  record.bindsPublishedShapeCover=record.shapeCoverEnvelope.every((x,i)=>x<[.0032,.00005,.0036,.00006][i]);
  record.terminalAngular=ramp.terminalAngular.map((q,j)=>normBounds(q,jetLimits()[1][j][0],jetLimits()[1][j][2]));
  const actual=ramp.terminalSecondAngular.map(row=>row.map(upperDyadic));
  for(let j=0;j<3;j++) for(let c=0;c<3;c++)
    if(!(actual[j][c]<record.terminalSecondEnvelope[j][c]))throw Error('second angular error exceeds envelope');
  record.fieldSHA256=ramp.fieldSHA256;
  record.terminalSecondAngularUpperDyadics=actual;
  record.rampPrincipalAbsoluteUpper=upperDyadic(ramp.globalPrincipalAbsoluteUpper);
  // The finger shoulders already have reach r. Strictly smaller candidate
  // balls have no diagonal limit on any regular piece if all |k| <= 1/r.
  record.allLocalPiecesCertified=record.rampPrincipalAbsoluteUpper<8.6956;
  if(!record.allLocalPiecesCertified)throw Error('ramp curvature still requires sharpening');
  return record;
}
if(typeof require==='function' && typeof module!=='undefined' && require.main===module) {
  const fs=require('node:fs'),sha=x=>require('node:crypto').createHash('sha256').update(x).digest('hex');
  const args=process.argv.slice(2),arg=k=>args.includes(k)?args[args.indexOf(k)+1]:null;
  const out=compute(),ramp=arg('--ramp');
  out.sourceSHA256=sha(fs.readFileSync(__filename));
  if(ramp){const raw=fs.readFileSync(ramp);withRamp(out,JSON.parse(raw));out.rampReceiptSHA256=sha(raw)}
  const target=arg('--out'),s=JSON.stringify(out,null,2)+'\n';
  if(target)fs.writeFileSync(target,s,{flag:'wx'});else process.stdout.write(s);
}
