#!/usr/bin/env node
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {p2PortData,fitRay,p2RayFamily,buildRayField,rayComplete} from './2ecf-compact-p2-two-port-rays.mjs';
import {compactMixedJets} from './2ecf-compact-p32-prufer-physical-annulus.mjs';
import {observeP2} from './2ecf-compact-p2-original-cauchy-field.mjs';
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],norm=a=>Math.sqrt(dot(a,a));
function jointRaySetup(z,ck,old,opt={}){
 const J=opt.J??10,n=opt.n??8,nt=opt.nt??24,N=4*J,L=old.L,dim=(n-1)*5,ports=p2PortData(z,ck),axis=Array.from({length:J+1},(_,j)=>Math.PI*j/(2*J)),rays=axis.map(u=>{const p=ports(u),s=fitRay(p,u,L,{knots:n,N:4,it:0});return {p,s};}),raw=compactMixedJets(z);
 const ss=[],ts=[],radius=400;let l=0;for(let j=0;j<=radius;j++){let t=.24+.56*j/radius,Q=0,S=0;for(let i=0;i<64;i++){let X=raw(t,2*Math.PI*i/64);Q+=dot(X[1],X[1])/64;S+=dot(X[2],X[2])/64;}let v=1.06*Math.sqrt(Q);if(j)l+=(.56/radius)*(v+ts[j-1][1])/2;ss.push(l);ts.push([t,v,1.06**2*S]);}const tar=Array.from({length:nt+1},(_,i)=>{let s=l*i/nt,j=0;while(j+1<radius&&ss[j+1]<s)j++;let w=(s-ss[j])/(ss[j+1]-ss[j]);return (1-w)*ts[j][2]+w*ts[j+1][2];});
 function parameters(c,u){let Q=Math.cos(2*u),v=[1,Q,Math.cos(4*u),Math.sin(2*u),Math.sin(4*u)],x=[];for(let i=0;i<n-1;i++)x.push(c[5*i]*v[0]+c[5*i+1]*Q+c[5*i+2]*v[2],c[5*i+3]*v[3]+c[5*i+4]*v[4]);return x;}
 const z0=Array(dim).fill(0);for(let j=0;j<=old.J;j++){let xi=j*Math.PI/(2*old.J),w=(j===0||j===old.J?.5:1)/old.J,p=old.rays[j].z;for(let k=0;k<n-1;k++){for(let m=0;m<3;m++)z0[k*5+m]+=p[2*k]*w*(m?2:1)*Math.cos(2*m*xi);for(let m=1;m<=2;m++)z0[k*5+2+m]+=p[2*k+1]*2*w*Math.sin(2*m*xi);}}
 const tw=Array.from({length:nt+1},(_,i)=>i/nt),delta=2*Math.PI/N;function residual(c,details=false){let pts=Array.from({length:nt+1},()=>[]),vel=pts.map(()=>[]),acc=pts.map(()=>[]),R=[],pe=0;for(let j=0;j<=J;j++){
 let u=axis[j],{s}=rays[j],f=s.build(parameters(c,u)),P=[s.bd[0].P.slice()],T=tw.map(t=>f(t)),dir=[];
 for(let i=0;i<nt;i++){let mid=f((i+.5)/nt).T;P.push(P[i].map((v,k)=>v+L*(T[i].T[k]+4*mid[k]+T[i+1].T[k])/(6*nt)));}
 let d=s.bd[1].P.map((v,k)=>v-P[nt][k]);for(let a of d)R.push(3*a);pe=Math.max(pe,Math.hypot(...d));for(let i=0;i<=nt;i++){let t=tw[i],h=t**3*(10+t*(-15+6*t)),hp=30*(t*(1-t))**2,hpp=60*t*(1-t)*(1-2*t),[th,bt]=T[i].ang,[dth,db]=T[i].der,c1=Math.cos(th),s1=Math.sin(th),c2=Math.cos(bt),s2=Math.sin(bt),ax=-s1*c2*dth-c1*s2*db,ay=c2*db,az=c1*c2*dth-s1*s2*db,dt=[Math.cos(u)*ax-Math.sin(u)*ay,Math.sin(u)*ax+Math.cos(u)*ay,az];pts[i][j]=P[i].map((v,k)=>v+h*d[k]);vel[i][j]=T[i].T.map((v,k)=>L*v+hp*d[k]);acc[i][j]=dt.map((v,k)=>L*v+hpp*d[k]);}}
 function ext(row,k){let idx=(k%N+N)%N,q=Math.floor(idx/J),h=idx%J,v=row[q%2?J-h:h];return [(q===1||q===2?-1:1)*v[0],(q>=2?-1:1)*v[1],v[2]];}
 let maxG=0,maxK=0,maxW=0,minH=9,minA=9;for(let i=1;i<nt;i++)for(let j=0;j<=J;j++){let P=pts[i][j],V=vel[i][j],A=acc[i][j],evalD=(row,o)=>{let x=ext(row,j-2),y=ext(row,j-1),z=ext(row,j),v=ext(row,j+1),w=ext(row,j+2);return x.map((a,k)=>o===1?(a-8*y[k]+8*v[k]-w[k])/(12*delta):(-a+16*y[k]-30*z[k]+16*v[k]-w[k])/(12*delta*delta));},U=evalD(pts[i],1),B=evalD(vel[i],1),C=evalD(pts[i],2),S=tar[i],E=dot(V,V),F=dot(U,V),G=dot(U,U),e=E/L**2-1,f=F/(L*Math.sqrt(S)),g=G/S-1,no=cross(V,U),area=norm(no),nn=no.map(v=>v/Math.max(area,1e-7)),l=dot(A,nn),m=dot(B,nn),h=dot(C,nn),ar=Math.max(area*area,1e-7),H=(l*G-2*m*F+h*E)/(2*ar),K=(l*h-m*m)/ar,k1=Math.abs(H)+Math.sqrt(Math.max(0,H*H-K)),rr=norm(P),w=Math.abs(P[1]),held=Math.min(Math.hypot(P[0],P[1]-1.06*301/225,P[2]),Math.hypot(P[0],P[1]+1.06*301/225,P[2])),arR=area/(L*Math.sqrt(S));
 maxG=Math.max(maxG,Math.abs((e+g)/2)+Math.hypot((e-g)/2,f));maxK=Math.max(maxK,k1);maxW=Math.max(maxW,w);minH=Math.min(minH,held);minA=Math.min(minA,arR);
 R.push(e,1.41421356237*f,g,.10*Math.max(0,Math.min(200,k1)-10),14*Math.max(0,w-.893),14*Math.max(0,.647-held),10*Math.max(0,P[2]-.625),10*Math.max(0,.08-P[2]),10*Math.max(0,rr-1.578),3*Math.max(0,.6-arR));}
 return details?{maxG,maxK,maxW,minH,minA,pe}:R;}
 function solve(c0,steps=30){let c=c0.slice(),hist=[],damp=.005;const ip=(a,b)=>{let s=0;for(let i=0;i<a.length;i++)s+=a[i]*b[i];return s;};for(let it=0;it<steps;it++){let r=residual(c),cost=ip(r,r),J=Array.from({length:dim},(_,j)=>{let v=c.slice();v[j]+=1e-5;let F=residual(v);return F.map((q,i)=>(q-r[i])/1e-5);}),A=J.map((v,i)=>J.map((w,j)=>ip(v,w)+(i===j?damp*(.01+ip(v,v)):0))),B=J.map(v=>-ip(v,r));
 for(let j=0;j<dim;j++){let p=j;for(let i=j+1;i<dim;i++)if(Math.abs(A[i][j])>Math.abs(A[p][j]))p=i;[A[j],A[p]]=[A[p],A[j]];[B[j],B[p]]=[B[p],B[j]];for(let i=j+1;i<dim;i++){let q=A[i][j]/A[j][j];for(let k=j+1;k<dim;k++)A[i][k]-=q*A[j][k];B[i]-=q*B[j];}}
 let dx=B.slice();for(let j=dim-1;j>=0;j--){for(let i=j+1;i<dim;i++)dx[j]-=A[j][i]*dx[i];dx[j]/=A[j][j];}let ok=false;for(let rate of [1,.5,.25,.125,.0625,.03125]){let v=c.map((q,k)=>q+rate*dx[k]),rr=residual(v),cc=ip(rr,rr);if(cc<cost){c=v;hist.push([it+1,cc,rate]);damp=Math.max(.00005,damp*(rate>=.5?.65:1.3));ok=true;break;}}if(!ok)damp*=6;}return {c,hist,stats:residual(c,true)};}
 function family(c,J=48){return {J,n,L,rays:Array.from({length:J+1},(_,j)=>({z:parameters(c,j*Math.PI/(2*J))}))};}return {z0,solve,residual,family};}

export {jointRaySetup};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,p540,field,out]=process.argv.slice(2),read=x=>JSON.parse(readFileSync(x)),z=read(state),p=read(p540),ck=read(field);
 if(op==='make'){const previous=p2RayFamily(z,ck),d=jointRaySetup(z,ck,previous),x=d.solve(d.z0,55),re=buildRayField(z,ck,d.family(x.c));writeFileSync(out,JSON.stringify(re)+'\n');console.log(JSON.stringify({steps:x.hist,stats:x.stats}));}
 else if(op==='observe'){const m=rayComplete(z,p,ck,read(out));console.log(JSON.stringify(['G10a','G10b','G11'].map(g=>observeP2(m,[],z,g)),null,2));}
 else throw Error('make/observe STATE192 STATE540 P2F512 JOINTFIELD');
}
