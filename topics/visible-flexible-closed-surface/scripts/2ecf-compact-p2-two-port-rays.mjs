#!/usr/bin/env node
/** Direction-constrained real meridian connecting two physical PVA ports. */
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {gauss01} from './2ecf-compact-p32-normal-meridian-design.mjs';
import {compactMixedJets,actualCircleMoment,packetCompactCore} from './2ecf-compact-p32-prufer-physical-annulus.mjs';
import {compactStadium,changedCenterCauchyFull,observeP2} from './2ecf-compact-p2-original-cauchy-field.mjs';
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
function p2PortData(z,ck){
 const raw=compactMixedJets(z),M=ck.M,coef=ck.controls.at(-1),stop=ck.stop,finish=.70,old=compactStadium(32,.25),fresh=compactStadium(2,.2),ids=[[0,2,5],[1,4,8],[3,7,10]],out=packetCompactCore(z,{left:.44,right:.8,mode:-.006,radialMix:1}),cache=new Map();
 const x=stop/finish,H=[1-x**3*(10+x*(-15+6*x)),-30*(x*(1-x))**2/finish,-60*x*(1-x)*(1-2*x)/finish**2];
 const moment=actualCircleMoment(raw,.8),g=out.ext.value(moment[0]),[r,d1,d2]=moment,RR=[[g.r,g.U,g.z,g.f],[d1,d1*g.Ur,d1*g.w,d1*g.fr],[d2,d1*d1*g.Urr+d2*g.Ur,d1*d1*g.wr+d2*g.w,d1*d1*g.frr+d2*g.fr]];
 return u=>{if(cache.has(u))return cache.get(u);let v=raw(stop,u),a=old(u),b=fresh(u),left=ids.map((row,i)=>row.map((idx,j)=>v[idx].map((q,c)=>q+(c===2?0:H[i]*(b[j][c]-a[j][c])))));
 for(let j=0;j<M;j++)for(let c=0;c<3;c++){let k=c===2?2*j:2*j+1,C=Math.cos(k*u),S=Math.sin(k*u),A=c===1?[S,k*C,-k*k*S]:[C,-k*S,-k*k*C];for(let i=0;i<3;i++)for(let h=0;h<3;h++)left[i][h][c]+=coef[i][c*M+j]*A[h];}
 const right=RR.map(V=>[0,1,2].map(ad=>{let trig=(m,s)=>m===0?(ad===0&&!s?1:0):(s?Math.sin(m*u+ad*Math.PI/2):Math.cos(m*u+ad*Math.PI/2))*m**ad;
 return [(V[0]*trig(1,0)+V[1]*(.75*trig(1,0)+.25*trig(3,0)))/1.06,(V[0]*trig(1,1)+V[1]*(-.75*trig(1,1)+.25*trig(3,1)))/1.06,(V[2]*trig(0,0)+V[3]*trig(2,0))/1.06];}));let h=[left,right];if(cache.size<7000)cache.set(u,h);return h;};}

function fitRay(ports,u,L,options={}){
 const n=options.knots??8,N=options.N??96,m=2*(n-1),Z=[0,0,1],C=Math.cos(u),S=Math.sin(u),R=[C,S,0],U=[-S,C,0],dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],nm=a=>Math.sqrt(dot(a,a)),lam=1.06,A=lam*301/225;
 const bd=ports.map(q=>{let P=q[0][0].map(v=>v*lam),V=q[1][0].map(v=>v*lam),D=q[2][0].map(v=>v*lam),s=nm(V),T=V.map(x=>x/s),T1=D.map((v,k)=>(v-T[k]*dot(T,D))/s**2),w=dot(T,U),h=Math.sqrt(1-w*w),theta=Math.atan2(T[2],dot(T,R)),beta=Math.asin(w);
 return {P,V,D,s,T,T1,theta,beta,dt:L*(T1[2]*dot(T,R)-dot(T1,R)*T[2])/(h*h),db:L*dot(T1,U)/h};});
 let [a,b]=bd,theta0=a.theta,theta1=b.theta;while(theta1<theta0-Math.PI)theta1+=2*Math.PI;while(theta1>theta0+Math.PI)theta1-=2*Math.PI;theta1+=2*Math.PI*(options.turn??0);
 function build(ctrl){const ang=Array.from({length:n+1},(_,i)=>i===0?[theta0,a.beta]:i===n?[theta1,b.beta]:[ctrl[2*i-2],ctrl[2*i-1]]),tan=ang.map((v,i)=>i===0?[a.dt,a.db]:i===n?[b.dt,b.db]:v.map((q,k)=>(ang[i+1][k]-ang[i-1][k])*n/2));
 return x=>{let i=Math.min(n-1,Math.max(0,Math.floor(n*x))),p=x*n-i,q=1-p,base=[q*q*(1+2*p),p*q*q/n,p*p*(3-2*p),-p*p*q/n],der=[-6*n*q*p,q*(1-3*p),6*n*q*p,p*(3*p-2)],v=[],vr=[];
 for(let k=0;k<2;k++){let w=[ang[i][k],tan[i][k],ang[i+1][k],tan[i+1][k]];v[k]=w.reduce((s,z,j)=>s+z*base[j],0);vr[k]=w.reduce((s,z,j)=>s+z*der[j],0);}
 let [th,bt]=v,ct=Math.cos(th),st=Math.sin(th),cb=Math.cos(bt),sb=Math.sin(bt);return {T:[ct*cb*C-sb*S,ct*cb*S+sb*C,st*cb],K:Math.hypot(cb*vr[0],vr[1])/L,ang:v,der:vr};};}
 const axis=Math.abs(Math.sin(2*u))<1e-10,kw=options.kw??1,guide=options.guide??1,smooth=options.smooth??.012;
 function residual(z,detail=false){let start=a.P.slice(),pred=build(z),r=[],pe=0,maxK=0,mw=0,mh=0,minHeld=10,minZ=2,shape=[];for(let i=0;i<N;i++){
 let o=pred((i+.5)/N);for(let k=0;k<3;k++)start[k]+=L/N*o.T[k];let [x,y,v]=start,held=Math.min(Math.hypot(x,y-A,v),Math.hypot(x,y+A,v));mw=Math.max(mw,Math.abs(y));mh=Math.max(mh,v);minZ=Math.min(minZ,v);minHeld=Math.min(minHeld,held);maxK=Math.max(maxK,o.K);
 r.push(kw*Math.max(0,o.K-9.55)/Math.sqrt(N),guide*140*Math.max(0,Math.abs(y)-.894)/Math.sqrt(N),guide*130*Math.max(0,.647-held)/Math.sqrt(N),guide*100*Math.max(0,v-.625)/Math.sqrt(N),guide*100*Math.max(0,.08-v)/Math.sqrt(N),guide*90*Math.max(0,Math.hypot(x,y,v)-1.580)/Math.sqrt(N),smooth*o.K/Math.sqrt(N));if(detail)shape.push(start.slice());}
 for(let j=0;j<3;j++){r.push(200*(start[j]-b.P[j]));pe+=Math.pow(start[j]-b.P[j],2);}
 return detail?{r,pe:Math.sqrt(pe),maxK,mw,mh,minZ,minHeld,shape}:r;}
 function solve(A,b){let n=b.length;for(let k=0;k<n;k++){let p=k;for(let i=k+1;i<n;i++)if(Math.abs(A[i][k])>Math.abs(A[p][k]))p=i;[A[k],A[p]]=[A[p],A[k]];[b[k],b[p]]=[b[p],b[k]];if(Math.abs(A[k][k])<1e-15)continue;for(let i=k+1;i<n;i++){let f=A[i][k]/A[k][k];for(let j=k+1;j<n;j++)A[i][j]-=f*A[k][j];b[i]-=f*b[k];}}
 let z=Array(n).fill(0);for(let i=n-1;i>=0;i--){let v=b[i];for(let j=i+1;j<n;j++)v-=A[i][j]*z[j];z[i]=v/A[i][i];}return z;}
 function ip(a,b){let q=0;for(let i=0;i<a.length;i++)q+=a[i]*b[i];return q;}
 let z=options.seed?.slice()??Array.from({length:m},(_,i)=>{let k=i%2,j=(i>>1)+1,t=j/n;return k?(1-t)*a.beta+t*b.beta:(1-t)*theta0+t*theta1+(options.wave??0)*Math.sin(2*Math.PI*t)+(options.bump??0)*Math.sin(Math.PI*t);});
 const active=Array.from({length:m},(_,i)=>i).filter(i=>!axis||i%2===0),dim=active.length;let damping=.04;
 for(let iter=0;iter<(options.it??45);iter++){let r=residual(z),cost=ip(r,r),J=active.map(i=>{let w=z.slice();w[i]+=2e-5;let m=residual(w);return m.map((v,j)=>(v-r[j])/2e-5);}),H=J.map((a,i)=>J.map((b,j)=>ip(a,b)+(i===j?damping*(.1+ip(a,a)):0))),d=solve(H,J.map(v=>-ip(v,r))),ok=false;
 for(let a of [1,.5,.25,.125,.0625,.03125]){let w=z.slice();for(let h=0;h<dim;h++)w[active[h]]+=a*d[h];let s=residual(w);if(ip(s,s)<cost){z=w;damping=Math.max(.000005,damping*.55);ok=true;break;}}if(!ok){damping*=4;if(damping>1e5)break;}}
 let q=residual(z,true);return {z,score:ip(q.r,q.r),pe:q.pe,maxK:q.maxK,mw:q.mw,mh:q.mh,minZ:q.minZ,minHeld:q.minHeld,shape:q.shape,theta:[theta0,theta1],bd,axis,build};}

function p2RayFamily(z,ck,opt={}){
 const J=opt.J??48,n=opt.knots??8,port=p2PortData(z,ck),L=opt.L??.85372,rays=[];let prior;
 for(let j=0;j<=J;j++){const u=j*Math.PI/(2*J),params={turn:0,knots:n,N:opt.N??80,it:opt.it??50,guide:1,kw:1};let v=fitRay(port(u),u,L,{...params,seed:prior});if(j===0)prior=v.z.slice();else if(j===J){const q=fitRay(port(u),u,L,{...params,seed:prior.map((q,i)=>i%2?0:q)});v=q;}
 prior=v.z.slice();rays.push({z:v.z,score:v.score,curvature:v.maxK,ep:v.pe,width:v.mw,held:v.minHeld});}return {J,n,L,rays};}

function rayHermite(a,b,h,x,der){let q=[a[0],h*a[1],.5*h*h*a[2]],d0=b[0]-q[0]-q[1]-q[2],d1=h*b[1]-q[1]-2*q[2],d2=h*h*b[2]-2*q[2];q.push(10*d0-4*d1+.5*d2,-15*d0+7*d1-d2,6*d0-3*d1+.5*d2);for(let i=0;i<der;i++)q=q.slice(1).map((v,j)=>v*(j+1));return q.reduceRight((s,v)=>s*x+v,0)/h**der;}
function rayBridgeAt(port,t,lo=.24,hi=.8){let h=hi-lo,x=(t-lo)/h;return [[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]].map(([rd,ad])=>[0,1,2].map(k=>rayHermite(port[0].map(q=>q[ad][k]),port[1].map(q=>q[ad][k]),h,x,rd)));}
function buildRayField(z,ck,fam,opts={}){const pi=Math.PI,a=.24,b=.8,span=b-a,P=opts.panels??56,M=opts.modes??40,{L,J,n}=fam,N=4*J,raw=compactMixedJets(z),get=p2PortData(z,ck),times=Array.from({length:P+1},(_,i)=>a+span*i/P),sq=t=>{let Q=0,Qd=0;for(let j=0;j<64;j++){let X=raw(t,pi*j/32);Q+=dot(X[1],X[1])/64;Qd+=2*dot(X[1],X[3])/64;}return [1.06*Math.sqrt(Q),1.06*Qd/(2*Math.sqrt(Q))];},[G,W]=gauss01(8),init=times.map(t=>sq(t)),int=[0];
 for(let i=0;i<P;i++){let s=0;for(let j=0;j<G.length;j++)s+=W[j]*sq(times[i]+(times[i+1]-times[i])*G[j])[0];int.push(int[i]+s*(times[i+1]-times[i]));}
 let data=times.map(()=>Array.from({length:3},()=>new Float64Array(3*M))),tmax=0;
 for(let j=0;j<=J;j++){let u=pi*j/(2*J),port=get(u),fit=fitRay(port,u,L,{knots:n,N:8,it:0,seed:fam.rays[j].z,turn:0}),T=fit.build(fit.z),sa=fit.bd[0].s,sb=fit.bd[1].s,da=dot(fit.bd[0].D,fit.bd[0].T),db=dot(fit.bd[1].D,fit.bd[1].T),I=int[P],A=[0,sa/L-init[0][0]/I,da/L-init[0][1]/I],B=[0,sb/L-init[P][0]/I,db/L-init[P][1]/I],xs=times.map((t,i)=>[int[i]/I+rayHermite(A,B,span,i/P,0),init[i][0]/I+rayHermite(A,B,span,i/P,1),init[i][1]/I+rayHermite(A,B,span,i/P,2)]);
 xs[0][0]=0;xs[P][0]=1;const path=[fit.bd[0].P.slice()];for(let i=0;i<P;i++){let x=xs[i][0],dx=xs[i+1][0]-x,v=path[i].slice();if(!(dx>0))throw Error('nonpositive physical length map');for(let k=0;k<G.length;k++){let U=T(x+dx*G[k]).T;for(let a=0;a<3;a++)v[a]+=L*dx*W[k]*U[a];}path.push(v);}
 let residue=fit.bd[1].P.map((v,k)=>v-path[P][k]);tmax=Math.max(tmax,Math.hypot(...residue));
 for(let i=1;i<P;i++){let [x,dx,ddx]=xs[i],o=T(x),[th,bt]=o.ang,[dt,db]=o.der,ct=Math.cos(th),st=Math.sin(th),cb=Math.cos(bt),ss=Math.sin(bt),co=Math.cos(u),si=Math.sin(u),ax=-st*cb*dt-ct*ss*db,ay=cb*db,az=ct*cb*dt-st*ss*db,dT=[co*ax-si*ay,si*ax+co*ay,az],H=x**3*(10+x*(-15+6*x)),H1=30*(x*(1-x))**2,H2=60*x*(1-x)*(1-2*x),base=rayBridgeAt(port,times[i]),D=[[],[],[]];for(let c=0;c<3;c++){let pp=L*o.T[c]+H1*residue[c],p2=L*dT[c]+H2*residue[c];D[0][c]=(path[i][c]+H*residue[c])/1.06-base[0][c];D[1][c]=dx*pp/1.06-base[1][c];D[2][c]=(ddx*pp+dx*dx*p2)/1.06-base[3][c];}
 for(let c=0;c<3;c++)for(let k=0;k<M;k++){let m=c===2?2*k:2*k+1,v=(c===1?Math.sin(m*u):Math.cos(m*u))*(m===0?1:2)*(j===0||j===J?.5:1)/J;
 for(let h=0;h<3;h++)data[i][h][c*M+k]+=v*D[h][c];}
 }}
 return {times,controls:data.map(r=>r.map(v=>Array.from(v))),M,a,b,J,P,L,maxEndpointRepair:tmax};}
function rayComplete(z,p,ck,field){const native=changedCenterCauchyFull(z,p,ck,.70),port=p2PortData(z,ck),{a,b,P,M,controls}=field,cache=new Map(),ord=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];
 return {jet(_,t,u){if(t<=a||t>=b)return native.jet([],t,u);let B=rayBridgeAt(port(u),t,a,b),v=cache.get(t);if(!v){let h=(b-a)/P,i=Math.min(P-1,Math.max(0,Math.floor((t-a)/h))),xi=(t-field.times[i])/h,v0=controls[i],v1=controls[i+1];v=Array.from({length:3},(_,d)=>Array.from({length:3*M},(_,k)=>rayHermite(v0.map(q=>q[k]),v1.map(q=>q[k]),h,xi,d)));if(cache.size<10000)cache.set(t,v);}
 let co=[1],si=[0],C=Math.cos(u),S=Math.sin(u);for(let j=1;j<=2*M;j++){co[j]=co[j-1]*C-si[j-1]*S;si[j]=si[j-1]*C+co[j-1]*S;}for(let c=0;c<3;c++)for(let k=0;k<M;k++){let m=c===2?2*k:2*k+1,arr=c===1?[si[m],m*co[m],-m*m*si[m]]:[co[m],-m*si[m],-m*m*co[m]];for(let d=0;d<6;d++)B[d][c]+=arr[ord[d][1]]*v[ord[d][0]][c*M+k];}return B;}};}

export {p2PortData,fitRay,p2RayFamily,rayHermite,rayBridgeAt,buildRayField,rayComplete};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,p540,field,out]=process.argv.slice(2),read=x=>JSON.parse(readFileSync(x)),z=read(state),p=read(p540),ck=read(field);
 if(op==='make'){const fam=p2RayFamily(z,ck),f=buildRayField(z,ck,fam);writeFileSync(out,JSON.stringify(f)+'\n');console.log(JSON.stringify({maxEndpointRepair:f.maxEndpointRepair,rays:fam.rays.map(({z,...v})=>v)}));}
 else if(op==='observe'){const m=rayComplete(z,p,ck,read(out));console.log(JSON.stringify(['G10a','G10b','G11'].map(g=>observeP2(m,[],z,g)),null,2));}
 else throw Error('make/observe STATE192 STATE540 P2F512 RAYFIELD');
}
