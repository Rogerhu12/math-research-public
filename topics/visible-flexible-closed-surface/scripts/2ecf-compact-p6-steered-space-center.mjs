#!/usr/bin/env node
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {gauss01} from './2ecf-compact-p32-normal-meridian-design.mjs';
import {orientedCauchy,twistReference,buildTwistField,twistComplete,observeTwist} from './2ecf-space-center-explicit-cauchy-kernel.mjs';
function steerCore(p,amplitude,half=13/128){
 const M=[1];for(let k=1;k<=p+8;k++)M[k]=M[k-1]*(2*k-1)/(2*k); const mom=n=>.2*(M[n]-M[n+1])+32/15*(M[n+2]-M[n+3]),d=mom(p+1)/mom(p);
 let pol=[0,amplitude/(1-d)];for(let k=0;k<p;k++){let n=Array(pol.length+2).fill(0);for(let i=0;i<pol.length;i++){n[i]+=pol[i];n[i+2]-=pol[i];}pol=n;}let last=Array(pol.length+2).fill(0);for(let i=0;i<pol.length;i++){last[i]+=(1-d)*pol[i];last[i+2]-=pol[i];}let ps=[last];for(let j=0;j<3;j++)ps.push(ps.at(-1).slice(1).map((x,i)=>x*(i+1)));let hor=(a,t)=>a.reduceRight((v,x)=>v*t+x,0);
 function local(t){let s=Math.sin(t),c=Math.cos(t),x=s*s,r=.2+32/15*x*x,[F,y1,y2,y3]=ps.map(P=>hor(P,c)),v=Math.sqrt(1-F*F);if(!(v>.001))return {a:NaN};let g=-s*y1,gg=x*y2-c*y1,ggg=-s*(x*y3-3*c*y2-y1),k=g/v,kp=gg/v+F*g*g/v**3,kpp=ggg/v+(g**3+3*F*g*gg)/v**3+3*F*F*g**3/v**5,H=1+c*c*k*k,Hp=-2*s*c*k*k+2*c*c*k*kp,N0=c*kp-s*k*(1+H),Np=c*kpp-s*kp*(2+H)-c*k*(1+H)-s*k*Hp,a=N0/H**1.5,ad=(Np/H**1.5-1.5*N0*Hp/H**2.5)/r,K=Math.sqrt(H)/r,T=[-s,c*v,c*F],B=[c*c*k,(s*c*k*v-F),(s*c*k*F+v)].map(q=>q/Math.sqrt(H)),N=[-c,-s*v-c*k*F,-s*F+c*k*v].map(q=>q/Math.sqrt(H)),U=t-8/15*Math.sin(2*t)+1/15*Math.sin(4*t);return {F,v,r,U,a,ad,K,V:T,B,N};}
 return {d,local,ps};}
function steeringStrip(p,A,half){const f=steerCore(p,A,half),[G,W]=gauss01(16),pi=Math.PI,cache=new Map();
 function center(t){if(cache.has(t))return cache.get(t);const s=Math.sin(t),c=Math.cos(t),H=1+16/45*Math.cos(2*t)-4/225*Math.cos(4*t),D=-32/45*Math.sin(2*t)+16/225*Math.sin(4*t);let P=[H*c-D*s,0,0],count=Math.max(1,Math.ceil(Math.abs(t)/(.2*pi)));for(let i=0;i<count;i++)for(let j=0;j<G.length;j++){let v=(i+G[j])*t/count,q=f.local(v),ds=W[j]*t/count*q.r;P[1]+=ds*q.V[1];P[2]+=ds*q.V[2];}if(cache.size<5000)cache.set(t,P);return P;}
 function ring(s,u){u=(u%(2*pi)+2*pi)%(2*pi);let l=-2,r=2*pi+2,t=u;for(let it=0;it<80;it++){let q=f.local(t),e=q.U+s*q.a-u;if(Math.abs(e)<4e-15)break;if(e>0)r=t;else l=t;let w=t-e/(q.r*(1+s*q.ad));const gap=(r-l)*.12;t=w>l+gap&&w<r-gap?w:(l+r)/2;}const q=f.local(t);if(Math.abs(q.U+s*q.a-u)>7e-13)throw Error("material inverse did not converge");const J=1+s*q.ad,n=q.K/J,m=-q.a*n,ll=q.a*q.a*n,P=center(t).map((v,i)=>v+s*(q.B[i]+q.a*q.V[i]));return {...q,J,n,m,ll,t,P,jet:[P,q.B,q.V,q.N.map(v=>v*ll),q.N.map(v=>v*m),q.N.map(v=>v*n)]};}
 return {center,ring,local:f.local,half,A,p};}

function steeredReference(z,p,A=.30,half=13/128){const f=steeringStrip(6,A,half);return twistReference(z,p,f,half);}
export {steerCore,steeringStrip,steeredReference};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,p540,out,a0,h0,nn]=process.argv.slice(2),read=x=>JSON.parse(readFileSync(x)),N=Number(nn??512),A=Number(a0??.30),half=Number(h0??13/128);
 if(op==='ports'){const f=steeringStrip(6,A,half);console.log(JSON.stringify([0,Math.PI/2,Math.PI,3*Math.PI/2].map(u=>f.ring(half,u)),null,2));}
 else if(op==='make'||op==='trace'){const z=read(state),f=steeringStrip(6,A,half),s=orientedCauchy(z,N,N===512?1200:600,.20,true,1,40,u=>f.ring(half,u));if(op==='make'){if(!s.rec.every(q=>Number.isFinite(q.minimumN)&&q.minimumN>0)||s.rec.length!==41)throw Error('Cauchy source failed');const p=read(p540),d=buildTwistField(z,p,s,N===512?152:80,.70,steeredReference(z,p,A,half));writeFileSync(out,JSON.stringify(d)+'\n');}console.log(JSON.stringify(s.rec));}
 else if(op==='observe'){const z=read(state),p=read(p540),m=twistComplete(z,p,read(out),steeredReference(z,p,A,half));console.log(JSON.stringify(['G10a','G10b','G11'].map(g=>observeTwist(m,[],z,g)),null,2));}
 else throw Error('make/trace/observe STATE192 STATE540 FIELD A HALF N | ports - - - A HALF');
}
