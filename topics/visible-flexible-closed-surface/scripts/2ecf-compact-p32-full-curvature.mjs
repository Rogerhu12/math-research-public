#!/usr/bin/env node
/** Outward full-image first/second jet enclosures for the compact p32 transition. */
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
function compactCurvatureCover(z,nr=8,nm=8,threshold=10.52,maxVisits=350000,rangeStart=0,rangeEnd=16,receiver=null){
 const S=1n<<92n,min=(a,b)=>a<b?a:b,max=(a,b)=>a>b?a:b,abs=a=>a<0n?-a:a;
 const down=(a,b)=>a>=0n?a/b:-((-a+b-1n)/b),up=(a,b)=>-down(-a,b);
 const R=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b;}return [down(a*S,b),up(a*S,b)];};
 const add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[1],-a[0]],sub=(a,b)=>add(a,neg(b));
 const mul=(a,b)=>{let p=a[0]*b[0],q=a[0]*b[1],r=a[1]*b[0],s=a[1]*b[1];return [down(min(min(p,q),min(r,s)),S),up(max(max(p,q),max(r,s)),S)];};
 const mulI=(a,n)=>{n=BigInt(n);return n>=0n?[a[0]*n,a[1]*n]:[a[1]*n,a[0]*n];},divI=(a,n)=>[down(a[0],BigInt(n)),up(a[1],BigInt(n))];
 const extent=a=>max(abs(a[0]),abs(a[1])),loAbs=a=>a[0]>0n?a[0]:a[1]<0n?-a[1]:0n;
 const widen=(a,b)=>[a[0]-b,a[1]+b];const one=R(1),zero=R(0);
 const asD=x=>Number(x)/Number(S),dyadic=x=>{if(!Number.isFinite(x))throw Error("Finite coefficients required");if(x===0)return zero;const dv=new DataView(new ArrayBuffer(8));dv.setFloat64(0,x);let bits=dv.getBigUint64(0),e=Number((bits>>52n)&2047n),n=bits% (1n<<52n);if(e)n+=1n<<52n;e=(e||1)-1023-52;if(bits>>63n)n=-n;return R(n*(e>0?1n<<BigInt(e):1n),e<0?1n<<BigInt(-e):1n);};
 const bin=(n,j)=>{let a=1n;for(let k=0;k<j;k++)a=a*BigInt(n-k)/BigInt(k+1);return a;};
 const power=(a,n)=>{let x=one;for(let i=0;i<n;i++)x=mul(x,a);return x;};
 const sincos=x=>{let b=neg(mul(x,x)),ts=x,tc=one,s=x,c=one;
  for(let i=1;i<=25;i++){ts=divI(mul(ts,b),(2*i)*(2*i+1));tc=divI(mul(tc,b),(2*i-1)*(2*i));s=add(s,ts);c=add(c,tc);}
  // |x|<=2. The sine/cosine Taylor remainders are each < 2^-92.
  if(extent(x)>2n*S)throw Error("Taylor argument");return [widen(c,1n),widen(s,1n)];
 };
 const harmonics=(x,upto)=>{const [c,s]=sincos(x),a=[[one,zero]];for(let k=1;k<=upto;k++){let [v,w]=a[k-1];a.push([sub(mul(v,c),mul(w,s)),add(mul(w,c),mul(v,s))]);}return a;};
 function arctanInverse(k){let ans=zero;for(let j=0;j<64;j++){const term=R(j%2?-1:1,BigInt(2*j+1)*BigInt(k)**BigInt(2*j+1));ans=add(ans,term);}const remainder=R(1,129n*BigInt(k)**129n);return [ans[0],ans[1]+remainder[1]];}
 const pi=sub(mulI(arctanInverse(5),16),mulI(arctanInverse(239),4)),lambda=R(53,50),rhoMax=add(R(1,4),R(3n*4n**32n,4n*bin(64,32)));
 if(rhoMax[1]>=9n*S)throw Error("Stadium speed bound");
 const cs=[zero],hs=[zero],numcs=[0];
 for(let j=1;j<=32;j++){const c=R(3n*(j%2?-1n:1n)*bin(64,32-j),2n*bin(64,32));cs.push(c);hs.push(mul(c,R(1,1-4*j*j)));numcs.push(asD(c[0]));}
 const centralA=hs.reduce((a,b)=>add(a,b),one);if(centralA[0]<R(7,5)[1]||centralA[1]>R(3,2)[0])throw Error("Actual cardinal bounds");const axis=mul(lambda,centralA);
 const co=z.map(dyadic),h0=R(13,128),h1=R(27,50),r1=R(7,20),L=R(6,5);
 if(z.length!==nr*nm*3)throw Error("Incorrect coefficient space");

 const eps=1e-15,lo=v=>v-(Math.abs(v)+1)*eps,hi=v=>v+(Math.abs(v)+1)*eps;
 const plus=(a,b)=>[lo(a[0]+b[0]),hi(a[1]+b[1])],minus=(a,b)=>[lo(a[0]-b[1]),hi(a[1]-b[0])],prod=(a,b)=>{
   const s=a[0]*b[0],t=a[0]*b[1],u=a[1]*b[0],v=a[1]*b[1];return [lo(Math.min(s,t,u,v)),hi(Math.max(s,t,u,v))];};
 const times=(a,v)=>v>=0?[lo(a[0]*v),hi(a[1]*v)]:[lo(a[1]*v),hi(a[0]*v)];
 const reciprocal=a=>{if(a[0]<=0)throw Error("positive reciprocal");return [lo(1/a[1]),hi(1/a[0])];};
 const sq=a=>{let b=Math.min(a[0]**2,a[1]**2);return [a[0]<=0&&a[1]>=0?0:lo(b),hi(Math.max(a[0]**2,a[1]**2))];};
 const real=a=>[lo(asD(a[0])),hi(asD(a[1]))],dd=p=>p.slice(1).map((v,i)=>times(minus(v,p[i]),p.length-1)),zz0=[0,0];
 const angCache=new Map(),panelCache=new Map();
 function node(j,d){while(d>0&&j%2===0){j/=2;d--;}const key=j+"/"+d;if(angCache.has(key))return angCache.get(key);
  const den=2**d,U=divI(mulI(pi,j),2*den),ud=asD(U[0]);let low=0,high=Math.PI/2;
  for(let it=0;it<53;it++){const m=(low+high)/2;let v=m;for(let n=1;n<=32;n++)v+=numcs[n]*Math.sin(2*n*m)/(2*n);if(v>ud)high=m;else low=m;}
  const th=dyadic((low+high)/2),H=harmonics(th,64),[co,si]=H[1],F=harmonics(U,2*nm);
  let ar=th,hh=one,hp=zero;for(let k=1;k<=32;k++){ar=add(ar,divI(mul(cs[k],H[2*k][1]),2*k));hh=add(hh,mul(hs[k],H[2*k][0]));hp=sub(hp,mulI(mul(hs[k],H[2*k][1]),2*k));}
  const er=extent(sub(ar,U)),c=widen(co,4n*er),s=widen(si,4n*er),P=[widen(sub(mul(hh,co),mul(hp,si)),36n*er),widen(add(mul(hh,si),mul(hp,co)),36n*er)];
  const rad=add(R(1,4),mul(R(3n*4n**32n,4n*bin(64,32)),power(s,64)));
  const val={P:P.map(real),c:real(c),s:real(s),r:real(rad),F:F.map(a=>a.map(real))};angCache.set(key,val);return val;
 }
 function angularPanel(j,d){const key=j+"/"+d;if(panelCache.has(key))return panelCache.get(key);
  const a=node(j,d),b=node(j+1,d),den=2**d;
  const unite=(l,r)=>[Math.min(l[0],r[0]),Math.max(l[1],r[1])];
  const C=unite(a.c,b.c),Sin=unite(a.s,b.s),ri=reciprocal(unite(a.r,b.r)),gamma=[[],[],[]];
  gamma[0]=[unite(a.P[0],b.P[0]),unite(a.P[1],b.P[1])];gamma[1]=[times(Sin,-1),C];gamma[2]=[times(prod(C,ri),-1),times(prod(Sin,ri),-1)];
  function wave(k,s,o){if(k===0)return o===0&&!s?[1,1]:zz0;let idx=(o+(s?3:0))%4,sgn=idx<2?1:-1,kind=idx%2;
   // cos(x+pi/2)=-sin(x); cos(x+3pi/2)=sin(x).
   if(kind)sgn=-sgn;
   let v=unite(a.F[k][kind],b.F[k][kind]);
   for(let n=Math.ceil(k*j/den);n<=Math.floor(k*(j+1)/den);n++){
    if(n%2!==kind)continue;let e=kind?(n%4===1?1:-1):(n%4===0?1:-1);v=[Math.min(v[0],e),Math.max(v[1],e)];}
   return times(v,sgn*k**o);}
  let f=[];for(let k=0;k<3;k++)for(let h=0;h<nm;h++)f.push([0,1,2].map(o=>wave(k===2?2*h:2*h+1,k===1,o)));
  const val={gamma,e:[0,1,2].map(o=>[wave(1,false,o),wave(1,true,o)]),f};panelCache.set(key,val);return val;
 }
 const conv=(p,q)=>{let a=Array.from({length:p.length+q.length-1},()=>zz0);for(let i=0;i<p.length;i++)for(let j=0;j<q.length;j++)a[i+j]=plus(a[i+j],prod(p[i],q[j]));return a;};
 const scal=(p,v)=>p.map(q=>prod(q,v)),che=[[[1,1]],[[-1,-1],[2,2]]],base=[0,0,0,64,-192,192,-64].map(a=>[a,a]);
 for(let k=2;k<nr;k++){let p=conv([[-2,-2],[4,4]],che[k-1]);for(let j=0;j<che[k-2].length;j++)p[j]=minus(p[j],che[k-2][j]);che.push(p);}
 const D=nr+5,functions=[[[1,1],[1,1],[1,1],zz0,zz0,zz0],[zz0,zz0,zz0,real(add(r1,mul(L,R(2,5)))),real(add(r1,mul(L,R(1,5)))),real(r1)],[real(h0),real(add(h0,mul(L,R(1,5)))),real(add(h0,mul(L,R(2,5)))),real(h1),real(h1),real(h1)]];
 for(let k=0;k<3;k++)for(let h=0;h<nm;h++){
  let p=Array.from({length:D+1},()=>zz0);for(let j=0;j<nr;j++){let a=scal(conv(base,che[j]),real(co[(j*3+k)*nm+h]));for(let i=0;i<a.length;i++)p[i]=plus(p[i],a[i]);}
  functions.push(p.map((_,i)=>p.slice(0,i+1).reduce((a,b,j)=>plus(a,prod(b,real(R(bin(i,j),bin(D,j))))),zz0)));
 }
 const original=functions.map(p=>[p,dd(p),dd(dd(p))]),rCache=new Map();
 function half(p,dir){let side=[dir?p.at(-1):p[0]],row=p;while(row.length>1){row=row.slice(1).map((v,i)=>times(plus(row[i],v),.5));side.push(dir?row.at(-1):row[0]);}return dir?side.reverse():side;}
 function radialNode(j,d){const key=j+"/"+d;if(rCache.has(key))return rCache.get(key);const ctrl=d?radialNode(j>>1,d-1).ctrl.map(a=>a.map(p=>half(p,j%2))):original;
  const b=ctrl.map(a=>a.map(p=>[Math.min(...p.map(v=>v[0])),Math.max(...p.map(v=>v[1]))]));const val={ctrl,b};rCache.set(key,val);return val;}
 const derivativeOrders=[[1,0],[0,1],[2,0],[1,1],[0,2]];
 function vector(E,T,orders=derivativeOrders){let out=[];
  for(let [r,u] of orders){let row=[];for(let k=0;k<3;k++){let val=k<2?plus(prod(E[0][r],T.gamma[u][k]),prod(E[1][r],T.e[u][k])):(u===0?E[2][r]:zz0);
   for(let h=0;h<nm;h++)val=plus(val,prod(E[3+k*nm+h][r],T.f[k*nm+h][u]));row.push(val);}out.push(row);}
  return out;
 }
 const dot=(a,b)=>plus(plus(prod(a[0],b[0]),prod(a[1],b[1])),prod(a[2],b[2])),norm=a=>plus(plus(sq(a[0]),sq(a[1])),sq(a[2]));
 const cross=(a,b)=>[0,1,2].map(i=>minus(prod(a[(i+1)%3],b[(i+2)%3]),prod(a[(i+2)%3],b[(i+1)%3])));
 if(receiver)return receiver({angularPanel,radialNode,vector,real,lambda,dot,norm,plus,times,prod});
 const rho=prod(real(lambda),real(dyadic(threshold))),safety=lo(rho[0]);
 let visited=0,closed=0,rejected=0,need=[],deep=[0,0],minArea=Infinity;
 function covered(j,d,k,l){
  const theta=angularPanel(k,l),R=radialNode(j,d),[v,u,A,B,C]=vector(R.b,theta),n=cross(v,u),na=norm(n)[0];if(na<=0)return false;
  const g=times([lo(Math.sqrt(na)),hi(Math.sqrt(na))],safety);
  let E=norm(v),F=dot(v,u),G=norm(u),L=dot(n,A),M=dot(n,B),N=dot(n,C);
  for(let sign of [-1,1]){let aa=plus(prod(g,E),times(L,sign)),bb=plus(prod(g,F),times(M,sign)),cc=plus(prod(g,G),times(N,sign));
   if(aa[0]<=0||cc[0]<=0||minus(prod(aa,cc),sq(bb))[0]<=0)return false;}
  minArea=Math.min(minArea,na);return true;
 }
 function visit(j,d,k,l){
  if(++visited>maxVisits)throw Error("Visit budget, incomplete "+JSON.stringify([visited,closed,rejected,need.slice(0,3)]));
  if(covered(j,d,k,l)){closed++;deep[0]=Math.max(deep[0],d);deep[1]=Math.max(deep[1],l);return;}
  if(d+l>=30){rejected++;if(need.length<8)need.push([j,d,k,l]);return;}
  if(d<=l+1){visit(2*j,d+1,k,l);visit(2*j+1,d+1,k,l);}
  else{visit(j,d,2*k,l+1);visit(j,d,2*k+1,l+1);}
 }
 for(let j=rangeStart;j<rangeEnd;j++)for(let k=0;k<16;k++)visit(j,4,k,4);
 return {range:[rangeStart,rangeEnd,16],threshold,visited,closed,rejected,need,deep,minSquaredAreaOnClosed:minArea,complete:rejected===0};
 }
export {compactCurvatureCover};
if(process.argv[1] && import.meta.url===pathToFileURL(process.argv[1]).href){
 const [file,K='10.305',R='8',M='8']=process.argv.slice(2);
 const z=JSON.parse(readFileSync(file));
 const results=Array.from({length:16},(_,i)=>compactCurvatureCover(z,Number(R),Number(M),Number(K),400000,i,i+1));
 console.log(JSON.stringify(results,null,2));
 if(results.some(r=>!r.complete))process.exitCode=1;
}
