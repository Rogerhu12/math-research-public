#!/usr/bin/env node
import {readFileSync} from "node:fs";
import {pathToFileURL} from "node:url";
function continuousPositionCover(z,radial=448,angles=128,nr=8,nm=8){
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
 let mt=[0n,0n,0n],mu=[0n,0n,0n];
 for(let k=0;k<3;k++)for(let j=0;j<nr;j++)for(let h=0;h<nm;h++){
  const a=extent(co[(j*3+k)*nm+h]),m=k===2?2*h:2*h+1;
  mt[k]+=BigInt(120+48*j*j+4*j**4)*a;mu[k]+=BigInt(m*m)*a;
 }
 // Five Bernstein controls and their second differences: base |P_tt|<=160.
 // Gamma unit speed with |Gamma_uu|<=4, and radial coefficient <=.35+2*(6/5)/5<.84.
 mt=mt.map(v=>v+160n*S);mu=mu.map(v=>v+5n*S);
 const ht=R(1,radial),hu=divI(pi,2*angles);
 const err=mt.map((a,k)=>divI(add(mul([0n,a],mul(ht,ht)),mul([0n,mu[k]],mul(hu,hu))),8)[1]);
 const angle=[];
 function arcGuess(th){let u=th;for(let j=1;j<=32;j++)u+=numcs[j]*Math.sin(2*j*th)/(2*j);return u;}
 for(let h=0;h<=angles;h++){
  const u=divI(mulI(pi,h),2*angles),ud=asD(u[0]);let lo=0,hi=Math.PI/2;
  for(let iter=0;iter<56;iter++){const t=(lo+hi)/2;if(arcGuess(t)>ud)hi=t;else lo=t;}
  const th=dyadic((lo+hi)/2),T=harmonics(th,64),A=harmonics(u,2*nm),c=T[1][0],s=T[1][1];
  let ar=th,V=one,W=zero;for(let j=1;j<=32;j++){ar=add(ar,divI(mul(cs[j],T[2*j][1]),2*j));V=add(V,mul(hs[j],T[2*j][0]));W=sub(W,mulI(mul(hs[j],T[2*j][1]),2*j));}
  const residual=extent(sub(ar,u)),shift=36n*residual;
  // u'(theta)>=1/4; |P_theta|<=rhoMax<9. Thus 36 times residual covers each coordinate.
  const P=[widen(sub(mul(V,c),mul(W,s)),shift),widen(add(mul(V,s),mul(W,c)),shift),zero];
  angle.push({P,A});
 }
 let tw=0n,br=0n,heldSq=null,cylSq=null,zmax=-100n*S,zmin=100n*S,count=0,prev=null;
 for(let i=0;i<=radial;i++){const t=R(i,radial),v=sub(one,t),bl=[];
  for(let n=0;n<6;n++)bl.push(mulI(mul(power(t,n),power(v,5-n)),bin(5,n)));
  const left=add(add(bl[0],bl[1]),bl[2]),right=add(add(bl[3],bl[4]),bl[5]);
  const rr=add(mul(right,r1),divI(mul(L,add(mulI(bl[3],2),bl[4])),5));
  const zz=add(add(mul(left,h0),mul(right,h1)),divI(mul(L,add(bl[1],mulI(bl[2],2))),5));
  const t2=sub(mulI(t,2),one),che=[one,t2],b=mulI(power(mul(t,v),3),64);
  for(let j=2;j<nr;j++)che.push(sub(mulI(mul(t2,che[j-1]),2),che[j-2]));
  const amps=[];for(let k=0;k<3;k++){amps.push([]);for(let h=0;h<nm;h++){
    let f=zero;for(let j=0;j<nr;j++)f=add(f,mul(co[(j*3+k)*nm+h],che[j]));amps[k].push(mul(b,f));}}
  let current=angle.map(({P,A})=>{let out=[add(mul(P[0],left),mul(rr,A[1][0])),add(mul(P[1],left),mul(rr,A[1][1])),zz];
   for(let k=0;k<3;k++)for(let h=0;h<nm;h++){let m=k===2?2*h:2*h+1;out[k]=add(out[k],mul(amps[k][h],A[m][k===1?1:0]));}return out;});
  if(prev)for(let h=0;h<angles;h++){const pts=[prev[h],prev[h+1],current[h],current[h+1]],box=[0,1,2].map(k=>{
   let l=pts[0][k][0],u=pts[0][k][1];for(let j=1;j<4;j++){l=min(l,pts[j][k][0]);u=max(u,pts[j][k][1]);}return mul(lambda,widen([l,u],err[k]));});
   const rmin=loAbs(box[0])**2n+loAbs(box[1])**2n;cylSq=cylSq===null?rmin:min(cylSq,rmin);tw=max(tw,extent(box[1]));br=max(br,box.reduce((v,b)=>v+extent(b)**2n,0n));zmax=max(zmax,box[2][1]);zmin=min(zmin,box[2][0]);
   for(let sign of [1,-1]){const b=sub(box[1],mulI(axis,sign));const sq=loAbs(box[0])**2n+loAbs(b)**2n+loAbs(box[2])**2n;if(heldSq===null||sq<heldSq)heldSq=sq;}
   count++;
  }
  prev=current;
 }
 const Q=(x)=>x.toString()+"/"+S.toString(),Q2=x=>x.toString()+"/"+(S*S).toString();
 const checks={width:tw*1000n<897n*S,ball:br*10000n**2n<15822n**2n*S*S,
   held:heldSq*1000n**2n>650n**2n*S*S,cylinder:cylSq*100n**2n>35n**2n*S*S,height:zmax*1000n<635n*S,upperSide:zmin>0n};
 if(!Object.values(checks).every(v=>v))throw Error("Insufficient continuous bound: "+JSON.stringify([asD(tw),Math.sqrt(Number(br))/Number(S),Math.sqrt(Number(heldSq))/Number(S),asD(zmax),asD(zmin)]));
 return {radialCells:radial,quarterCells:angles,quarterRectangles:count,wholeRectangles:4*count,
    halfWidthUpperExact:Q(tw),ballSquaredUpperExact:Q2(br),heldSquaredLowerExact:Q2(heldSq),
    cylindricalRadiusSquaredLowerExact:Q2(cylSq),maxHeightExact:Q(zmax),positiveSideMinHeightExact:Q(zmin),
    readable:{width:asD(tw),ball:Math.sqrt(Number(br))/Number(S),held:Math.sqrt(Number(heldSq))/Number(S),radiusLower:Math.sqrt(Number(cylSq))/Number(S),height:asD(zmax),lower:asD(zmin)},
    checks,unscaledBilinearErrors:err.map(Q)};
}
export {continuousPositionCover};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){const [p,nr,nm,r,u]=process.argv.slice(2);console.log(JSON.stringify(continuousPositionCover(JSON.parse(readFileSync(p)),Number(r??448),Number(u??128),Number(nr??8),Number(nm??8)),null,2));}
