"use strict";
/* R201 recovery v2, reconstructed after the fifth executor outage.
 * This is a new source identity, not the unpublished e75bf1... original.
 * Complete half-period phase, physical twojets and every parameter column.
 * Fixed Gauss-8 is finite evaluation, NOT a continuous integration certificate.
 */
function need(c,m){if(!c)throw Error(m);}
const powers=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]],fac=[1,1,1,2,1,2];
const pairs=Array.from({length:6},()=>[]);
for(let i=0;i<6;i++)for(let j=0;j<6;j++){
 const k=powers.findIndex(v=>v[0]===powers[i][0]+powers[j][0]&&v[1]===powers[i][1]+powers[j][1]);
 if(k>=0)pairs[k].push([i,j]);
}
const gx=[-.9602898564975363,-.7966664774136267,-.525532409916329,-.1834346424956498,
 .1834346424956498,.525532409916329,.7966664774136267,.9602898564975363];
const gw=[.1012285362903763,.2223810344533745,.3137066458778873,.362683783378362,
 .362683783378362,.3137066458778873,.2223810344533745,.1012285362903763];
function createR201HalfPeriodProvider(raw,options={}){
 const P=raw.parameterCount,panels=options.panels===undefined?16:options.panels;
 need(Number.isInteger(P)&&P>=0,"Explicit parameterCount");need(Number.isInteger(panels)&&panels>0,"Positive panels");
 const D=v=>{const a=new Float64Array(P+1);a[0]=v;return a;};
 const da=(a,b)=>Float64Array.from(a,(v,i)=>v+b[i]);
 const ds=(a,b)=>Float64Array.from(a,(v,i)=>v-b[i]);
 const dc=(a,c)=>Float64Array.from(a,v=>v*c);
 function dm(a,b){const z=D(a[0]*b[0]);for(let j=1;j<=P;j++)z[j]=a[j]*b[0]+a[0]*b[j];return z;}
 function df(a,f,fp){const z=D(f(a[0])),v=fp(a[0]);for(let j=1;j<=P;j++)z[j]=v*a[j];return z;}
 const dp=(a,p)=>df(a,x=>Math.pow(x,p),x=>p*Math.pow(x,p-1));
 const dz=()=>Array.from({length:6},()=>D(0));
 const jc=v=>{const x=dz();x[0]=D(v);return x;};
 const ja=(a,b)=>a.map((v,i)=>da(v,b[i]));
 const js=(a,b)=>a.map((v,i)=>ds(v,b[i]));
 const jscale=(a,v)=>a.map(x=>dc(x,v));
 function jm(a,b){return pairs.map(list=>{let z=D(0);for(const [i,j]of list)z=da(z,dm(a[i],b[j]));return z;});}
 function unary(a,f,f1,f2){
  const h=a.map(v=>v.slice());h[0]=D(0);const h2=jm(h,h),z=dz();
  z[0]=f(a[0]);
  for(let i=1;i<6;i++)z[i]=da(dm(f1(a[0]),h[i]),dc(dm(f2(a[0]),h2[i]),.5));
  return z;
 }
 const jpow=(a,p)=>unary(a,x=>dp(x,p),x=>dc(dp(x,p-1),p),x=>dc(dp(x,p-2),p*(p-1)));
 const jsin=a=>unary(a,x=>df(x,Math.sin,Math.cos),x=>df(x,Math.cos,y=>-Math.sin(y)),x=>dc(df(x,Math.sin,Math.cos),-1));
 const jcos=a=>unary(a,x=>df(x,Math.cos,y=>-Math.sin(y)),x=>dc(df(x,Math.sin,Math.cos),-1),x=>dc(df(x,Math.cos,y=>-Math.sin(y)),-1));
 function rawjet(a,columns,name){
  need(a&&a.length===6&&columns&&columns.length===P,name+" complete physical jets");
  const z=dz();for(let k=0;k<6;k++){need(Number.isFinite(a[k]),name+" finite");z[k][0]=a[k]/fac[k];
   for(let j=0;j<P;j++){need(columns[j]&&columns[j].length===6&&Number.isFinite(columns[j][k]),name+" complete parameter jets");z[k][j+1]=columns[j][k]/fac[k];}}
  return z;
 }
 const quad=(f,a,b)=>{if(a===b)return null;let sum=null;const N=Math.max(1,Math.ceil(panels*(b-a)/Math.PI));
  for(let k=0;k<N;k++){const l=a+(b-a)*k/N,r=a+(b-a)*(k+1)/N,h=(r-l)/2,c=(l+r)/2;
   for(let j=0;j<8;j++){const x=c+h*gx[j],v=f(x),w=h*gw[j];if(sum===null)sum=new Float64Array(v.length);for(let i=0;i<v.length;i++)sum[i]+=w*v[i];}}
  return sum;
 };
 function prepare(s,p){
  need(Number.isFinite(s)&&p&&p.length===P&&Array.from(p).every(Number.isFinite),"Physical s and complete p");
  const parameters=Array.from(p),cache=new Map();
  function rpoint(u){const q=raw.evaluate(s,u,parameters);return {theta:rawjet(q.theta,q.thetaParameters,"theta"),psi:rawjet(q.psi,q.psiParameters,"psi")};}
  const mean=quad(u=>{const q=rpoint(u),c=jcos(q.psi),ss=jsin(q.psi),out=new Float64Array(12*(P+1));let at=0;
   for(const a of [c,ss])for(const v of a)for(const x of v)out[at++]=x;return out;},0,Math.PI);
  let at=0;const C=dz(),S=dz();for(const a of[C,S])for(const v of a)for(let i=0;i<=P;i++)v[i]=mean[at++];
  for(const i of[2,4,5]){C[i].fill(0);S[i].fill(0);}
  const R2=ja(jm(C,C),jm(S,S));need(Number.isFinite(R2[0][0])&&R2[0][0]>0,"Mean phase R must be positive");
  const invR=jpow(R2,-.5);
  function packed(u){
   const key=String(u);if(cache.has(key))return cache.get(key);
   const q=rpoint(u),cp=jm(ja(jm(C,jcos(q.psi)),jm(S,jsin(q.psi))),invR),
    sp=jm(js(jm(C,jsin(q.psi)),jm(S,jcos(q.psi))),invR);
   const t=[jscale(jm(jsin(q.theta),cp),-1),jm(jcos(q.theta),cp),sp];
   if(cache.size<4*panels*8+32)cache.set(key,t);return t;
  }
  const names=["T","Ts","Tu","Tss","Tsu","Tuu"];
  function unpack(t){const jets={},pars={};for(let k=0;k<6;k++){jets[names[k]]=t.map(v=>fac[k]*v[k][0]);pars[names[k]]=t.map(v=>Array.from(v[k].slice(1),x=>fac[k]*x));}return {jets,parameters:pars};}
  function point(u){need(Number.isFinite(u),"u finite");return unpack(packed(u));}
  function rad(u){const t=packed(u),z=new Float64Array(9*(P+1));let j=0;
   for(const k of[0,1,3])for(let a=0;a<3;a++)for(let p=0;p<=P;p++)z[j++]=t[a][k][p]*fac[k];return z;
  }
  let total=null,moment=null;
  function init(){if(total)return;const z=quad(u=>{const a=rad(u),b=new Float64Array(2*a.length);b.set(a);for(let i=0;i<a.length;i++)b[a.length+i]=(Math.PI-u)*a[i];return b;},0,Math.PI);
   total=z.slice(0,z.length/2);moment=z.slice(z.length/2);
  }
  function primitive(u){
   need(Number.isFinite(u)&&u>=0&&u<=2*Math.PI,"primitive u in [0,2pi]");init();
   const second=u>Math.PI,v=second?u-Math.PI:u,left=quad(rad,0,v)||new Float64Array(total.length),q={jets:{},parameters:{}};
   let index=0;for(const name of["Y","Ys","Yss"]){q.jets[name]=[];q.parameters[name]=[];
    for(let a=0;a<3;a++){const sign=second&&a<2?-1:1,vec=[];for(let j=0;j<=P;j++){vec.push(sign*(left[index]-(a<2?total[index]/2:moment[index]/Math.PI)));index++;}
     q.jets[name][a]=vec[0];q.parameters[name][a]=vec.slice(1);}}
   const t=point(u);for(const [a,b]of[["Yu","T"],["Ysu","Ts"],["Yuu","Tu"]]){q.jets[a]=t.jets[b];q.parameters[a]=t.parameters[b];}
   return q;
  }
  const c=C[0],ss=S[0],cs=C[1],ss1=S[1],css=dc(C[3],2),sss=dc(S[3],2),den=da(dm(c,c),dm(ss,ss));
  const div=(x,y)=>dm(x,dp(y,-1));
  const num=ds(dm(c,ss1),dm(ss,cs)),bs=div(num,den);
  const bss=ds(div(ds(dm(c,sss),dm(ss,css)),den),dc(div(dm(da(dm(c,cs),dm(ss,ss1)),num),dm(den,den)),2));
  const beta=D(Math.atan2(ss[0],c[0]));for(let j=1;j<=P;j++)beta[j]=(c[0]*ss[j]-ss[0]*c[j])/den[0];
  const phase={C:c[0],S:ss[0],R:Math.sqrt(den[0]),beta:{value:beta[0],s:bs[0],ss:bss[0],parameters:Array.from(beta.slice(1)),sParameters:Array.from(bs.slice(1)),ssParameters:Array.from(bss.slice(1))},continuousCertificate:false};
  return {point,primitive,phase,definition:{schema:"fd2d-R201-half-period-phase-recovery-v2",raw:raw.definition||null,s,parameters,panels,quadrature:"complete half-period composite Gauss-8",physicalJetOrder:2,parameterColumns:P,continuousCertificate:false}};
 }
 return {prepare,definition:{schema:"fd2d-R201-half-period-phase-recovery-provider-v2",parameterCount:P,panels,raw:raw.definition||null,exactDefinition:"R201 equations (1), (8), (10), (11); finite Gauss evaluation with unpaid continuous remainder"}};
}
function createR201LocalFixture(){
 const P=7;
 function wd(s){return [64*(s*s*s-3*s*s*s*s+3*s*s*s*s*s-s*s*s*s*s*s),64*(3*s*s-12*s*s*s+15*s*s*s*s-6*s*s*s*s*s),64*(6*s-36*s*s+60*s*s*s-30*s*s*s*s)];}
 function ed(s){return [1-10*s*s*s+15*s*s*s*s-6*s*s*s*s*s,-30*s*s+60*s*s*s-30*s*s*s*s,-60*s+180*s*s-120*s*s*s];}
 const trig=(k,u,cos)=>k===0?[1,0,0]:cos?[Math.cos(k*u),-k*Math.sin(k*u),-k*k*Math.cos(k*u)]:[Math.sin(k*u),k*Math.cos(k*u),-k*k*Math.sin(k*u)];
 const product=(a,b)=>[a[0]*b[0],a[1]*b[0],a[0]*b[1],a[2]*b[0],a[1]*b[1],a[0]*b[2]];
 function evaluate(s,u,p){const w=wd(s),e=ed(s),theta=[u,0,1,0,0,0],psi=product(w,trig(2,u,false)).map(v=>.18*v),tp=Array.from({length:P},()=>Array(6).fill(0)),pp=Array.from({length:P},()=>Array(6).fill(0));
  const z=product(e,trig(2,u,false));for(let k=0;k<6;k++)theta[k]+=.12*z[k];
  for(const [j,angle,cos]of[[0,0,true],[1,2,true],[2,4,false]])tp[j]=product(w,trig(angle,u,cos));
  for(const [j,angle,cos]of[[3,2,false],[4,2,true],[5,4,true],[6,0,true]])pp[j]=product(w,trig(angle,u,cos));
  for(let j=0;j<P;j++)for(let k=0;k<6;k++){theta[k]+=p[j]*tp[j][k];psi[k]+=p[j]*pp[j][k];}
  return {theta,psi,thetaParameters:tp,psiParameters:pp};
 }
 return {parameterCount:P,evaluate,definition:{schema:"R201-seven-parameter-recovery-fixture-v2",formula:"theta=u+.12(1-S5(s))sin2u+w(p0+p1cos2u+p2sin4u); psi=w(.18sin2u+p3sin2u+p4cos2u+p5cos4u+p6); w=64s^3(1-s)^3"}};
}
module.exports={createR201HalfPeriodProvider,createR201LocalFixture};
