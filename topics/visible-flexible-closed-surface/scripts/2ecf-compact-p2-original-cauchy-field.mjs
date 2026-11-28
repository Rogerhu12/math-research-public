#!/usr/bin/env node
/** Two-lobed compact curve joined to the actual infinite prufer shell. */
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {configure,build,jets,gramTarget,lbfgs,evaluate} from './2ecf-compact-p32-direct-field.mjs';
import {gauss01} from './2ecf-compact-p32-normal-meridian-design.mjs';
import {compactMixedJets,packetCompactCore,packetControlled} from './2ecf-compact-p32-prufer-physical-annulus.mjs';
import {p32SpectralCauchy} from './2ecf-compact-p32-cauchy-new-target.mjs';
const pi=Math.PI,endZ=.54,dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],norm=a=>Math.sqrt(dot(a,a)),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],evaluateP2=evaluate,stats=({grad,...r})=>r;
function ownGrid(isIndependent){
 const ns=isIndependent?60:95,degree=isIndependent?11:10,[g,w]=gauss01(degree);
 let arr=[];for(let i=0;i<ns;i++)for(let j=0;j<degree;j++)arr.push([(i+g[j])/(ns+1),w[j]/(ns+1)]);
 const [last,ww]=gauss01(8);for(let j=0;j<8;j++)arr.push([(ns+last[j])/(ns+1),ww[j]/(ns+1)]);
 arr.sort((a,b)=>a[0]-b[0]);return arr;}

function compactStadium(p,r){const pi=Math.PI,c=[];let a=1;for(let j=1;j<=p;j++){a*=(p-j+1)/(p+j);c[j]=2*(1-r)*(j%2?-1:1)*a;}
 return u=>{u=(u%(2*pi)+2*pi)%(2*pi);let l=0,h=2*pi;for(let i=0;i<54;i++){let x=(l+h)/2,v=x;for(let k=1;k<=p;k++)v+=c[k]*Math.sin(2*k*x)/(2*k);if(v>u)h=x;else l=x;}let t=(l+h)/2,H=1,D=0,rho=1;for(let j=1;j<=p;j++){let k=2*j,cc=Math.cos(k*t)*c[j];H+=cc/(1-k*k);D-=k*c[j]*Math.sin(k*t)/(1-k*k);rho+=cc;}let x=Math.cos(t),y=Math.sin(t);return [[H*x-D*y,H*y+D*x],[-y,x],[-x/rho,-y/rho]];};}
function centralDifference(finish){
 const old=compactStadium(32,.25),fresh=compactStadium(2,.2),cache=new Map(),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];
 return (t,u)=>{let d=cache.get(u);if(!d){let a=old(u),b=fresh(u);d=a.map((v,i)=>[b[i][0]-v[0],b[i][1]-v[1],0]);if(cache.size<12000)cache.set(u,d);}
 let x=Math.max(0,Math.min(1,t/finish)),H=[1-x**3*(10+x*(-15+6*x)),-30*(x*(1-x))**2/finish,-60*x*(1-x)*(1-2*x)/finish**2];return orders.map(([rd,ad])=>d[ad].map(v=>H[rd]*v));};}
function buildOtherCenterData(z,sol,M,finish=.70){const src=compactMixedJets(z),diff=centralDifference(finish);return compactOtherCauchyPositions(z,sol,M,(t,u)=>{let q=src(t,u),d=diff(t,u);return q.map((v,i)=>i<6?v.map((x,k)=>x+d[i][k]):v);});}
function compactOtherCauchyPositions(z,sol,M,ref){
 const raw=compactMixedJets(z),pi=Math.PI,N=sol.N,times=sol.rec.map(x=>x.t),sample=sol.snapshot,controls=[],a0=3*M,ip=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
 if(sample.length!==times.length)throw Error('Cauchy computation ended before its fixed endpoint');
 const A=Array.from({length:N},(_,j)=>Array.from({length:a0},(_,i)=>{let c=Math.floor(i/M),k=i%M,m=c===2?2*k:2*k+1;return (c===1?Math.sin(m*2*pi*j/N):Math.cos(m*2*pi*j/N))*(m===0?1:2)/N;}));
 for(let I=0;I<times.length;I++){const t=times[I],data=sample[I],row=Array.from({length:3},()=>new Float64Array(a0));if(I===0){controls.push(row);continue;}
  let Q=0,Qd=0;for(let j=0;j<64;j++){const X=raw(t,2*pi*j/64);Q+=ip(X[1],X[1])/64;Qd+=2*ip(X[1],X[3])/64;}let e=Math.sqrt(Q),ed=Qd/(2*e),K=sol.rec[I].K;
  for(let j=0;j<N;j++){const x=ref(t,2*pi*j/N),ii=14*j,n=data[ii],m=data[ii+1],l=(K+m*m)/n;for(let c=0;c<3;c++){
   const d=[data[ii+11+c]-x[0][c],e*data[ii+2+c]-x[1][c],ed*data[ii+2+c]+Q*l*data[ii+8+c]-x[3][c]];
   for(let k=0;k<M;k++){let a=c*M+k,v=A[j][a];for(let h=0;h<3;h++)row[h][a]+=v*d[h];}}}
  controls.push(row);
 }
 return {times,controls:controls.map(row=>row.map(a=>Array.from(a))),M,stop:sol.stop,weight:1};
}
function changedCenterCauchyFull(z,oldCoeffs,ck,finish=.70){
 const {times,controls,M,stop}=ck,pi=Math.PI,n=times.length-1,step=stop/n,base=packetCompactCore(z,{left:.44,right:.8,mode:-.006,radialMix:1}),prior=packetControlled(z,oldCoeffs),a0=3*M,radCache=new Map(),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];
 const difference=centralDifference(finish);const zero=Array.from({length:3},()=>new Float64Array(a0));
 function bern(t){let b=[[1]];for(let n=1;n<=5;n++){let r=b.at(-1);b.push(Array.from({length:n+1},(_,i)=>(1-t)*(r[i]||0)+t*(r[i-1]||0)));}return [b[5],Array.from({length:6},(_,i)=>5*((b[4][i-1]||0)-(b[4][i]||0))),Array.from({length:6},(_,i)=>20*((b[3][i-2]||0)-2*(b[3][i-1]||0)+(b[3][i]||0)))];}
 function row(t){if(radCache.has(t))return radCache.get(t);let i=t>=stop?n:Math.max(0,Math.min(n-1,Math.floor(t/step))),a=controls[i],b=i===n?zero:controls[i+1],L=i===n?finish-stop:times[i+1]-times[i],x=(t-times[i])/L,B=bern(x),v=Array.from({length:3},()=>new Float64Array(a0));
  for(let k=0;k<a0;k++){let aa=[a[0][k],a[0][k]+L*a[1][k]/5,a[0][k]+2*L*a[1][k]/5+L*L*a[2][k]/20,b[0][k]-2*L*b[1][k]/5+L*L*b[2][k]/20,b[0][k]-L*b[1][k]/5,b[0][k]];for(let d=0;d<3;d++)for(let w=0;w<6;w++)v[d][k]+=B[d][w]*aa[w]/L**d;}
  if(radCache.size<12000)radCache.set(t,v);return v;}
 function jet(p,t,u){if(t>=finish)return prior.jet([],t,u);let original=base.one(t,u),D=difference(t,u),P=original.map((v,i)=>v.map((x,k)=>x+D[i][k])),co=row(t);if(t>stop){let q=(t-stop)/(finish-stop),s=q**3*(10+q*(-15+6*q)),d=30*(q*(1-q))**2/(finish-stop),dd=60*q*(1-q)*(1-2*q)/(finish-stop)**2,W=prior.jet([],t,u).map((v,i)=>v.map((x,k)=>x-original[i][k]));
   P=P.map((v,i)=>v.map((x,k)=>x+s*W[i][k]));for(let k=0;k<3;k++){P[1][k]+=d*W[0][k];P[3][k]+=dd*W[0][k]+2*d*W[1][k];P[4][k]+=d*W[2][k];}}
  const cs=[1],ss=[0],c=Math.cos(u),s=Math.sin(u);for(let k=1;k<2*M;k++){cs.push(cs[k-1]*c-ss[k-1]*s);ss.push(ss[k-1]*c+cs[k-1]*s);}for(let k=0;k<a0;k++){let c=Math.floor(k/M),j=k%M,m=c===2?2*j:2*j+1,v=c===1?ss[m]:cs[m],d=m*(c===1?cs[m]:-ss[m]);P[0][c]+=co[0][k]*v;P[1][c]+=co[1][k]*v;P[2][c]+=co[0][k]*d;P[3][c]+=co[2][k]*v;P[4][c]+=co[1][k]*d;P[5][c]-=co[0][k]*m*m*v;}return P;}
 return {jet,stop,finish};
}
function p2Design(z,prev,ck,opts={}){
 const nf=opts.nf??22,na=opts.na??11,R=opts.R??67,N=opts.N??80,start=.24,end=.8,h=(end-start)/(nf+3),rads=Array.from({length:R},(_,j)=>j/(R-1)),shape=changedCenterCauchyFull(z,prev,ck,.70);
 configure(8,8);const tar=build(R,64,rads),g=tar.rows.map(row=>gramTarget(jets(tar,row,z),64));
 configure(nf,na);const data=build(R,N,rads),nb=na*3;
 for(let row of data.rows){row.B=Array.from({length:nf},(_,j)=>{let x=(row.t-start)/h-j-2,k=Math.abs(x),s=Math.sign(x);if(k>=2)return [0,0,0];return k>1?[h*(2-k)**3/6,-s*(2-k)**2/2,(2-k)/h]:[h*(2/3-k*k+.5*k**3),s*(-2*k+1.5*k*k),(-2+3*k)/h];});
  for(let i=0;i<N;i++)row.base.set(shape.jet([],row.t,2*Math.PI*i/N).flat(),18*i);}
 const opt={centralMark:301/225,metricSharp:opts.sharp??95,kw:opts.kw??2.5,gw:opts.gw??1100,kgoal:10.20,wgoal:.841,hgoal:.617};return {data,g,dim:nf*na*3,opt,nf,na};}
function p2Controlled(z,prev,ck,controls,nf=22,na=11){const actual=changedCenterCauchyFull(z,prev,ck,.70),start=.24,end=.8,h=(end-start)/(nf+3),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];return {jet(p,t,u){const Y=actual.jet([],t,u);if(t<=start||t>=end)return Y;
 for(let j=Math.max(0,Math.floor((t-start)/h)-3);j<Math.min(nf,Math.floor((t-start)/h)+1);j++){let x=(t-start)/h-j-2,k=Math.abs(x),s=Math.sign(x);if(k>=2)continue;let b=k>1?[h*(2-k)**3/6,-s*(2-k)**2/2,(2-k)/h]:[h*(2/3-k*k+.5*k**3),s*(-2*k+1.5*k*k),(-2+3*k)/h];
 for(let a=0;a<3;a++)for(let m=0;m<na;m++){const k=a===2?2*m:2*m+1,c=Math.cos(k*u),s=Math.sin(k*u),v=controls[(3*j+a)*na+m],A=a===1?[s,k*c,-k*k*s]:[c,-k*s,-k*k*c];for(let l=0;l<6;l++)Y[l][a]+=v*b[orders[l][0]]*A[orders[l][1]];}}return Y;}};}
function fullGramNormal(d,x){
 const {data,g,nf,na,opt}=d,{N,R}=data,C=3*na,dim=nf*C,outer=[],diag=new Float64Array(dim),baseScale=1/(R*N),ord=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]],zero=()=>new Float64Array(18);
 const lin=(a,x,b,y)=>a.map((v,k)=>v*x+b[k]*y),put=(v,d,a)=>{for(let k=0;k<3;k++)v[3*d+k]+=a[k];};
 for(let j=0;j<R;j++){let row=data.rows[j],active=[];for(let k=0;k<nf;k++)if(row.B[k].some(v=>v!==0))active.push(k);if(!active.length)continue;const Y=jets(data,row,x),Q=g[j][0],S=g[j][1],qs=Math.sqrt(Q*S);
  for(let i=0;i<N;i++){let p=18*i,y=k=>Array.from(Y.slice(p+3*k,p+3*k+3)),P=y(0),V=y(1),U=y(2),A=y(3),B=y(4),Z=y(5),E=dot(V,V),F=dot(V,U),G=dot(U,U),n=cross(V,U),area=norm(n),nn=n.map(v=>v/area),l=dot(A,nn),m=dot(B,nn),c=dot(Z,nn),H=(G*l-2*F*m+E*c)/(2*area*area),K=(l*c-m*m)/(area*area),root=Math.sqrt(Math.max(0,H*H-K)),e=E/Q-1,f=F/qs,q=G/S-1,sm=e*e+2*f*f+q*q,rows=[];
   function project(bar,weight){if(!(weight>0))return;let out=new Float64Array(active.length*C),w=Math.sqrt(weight*baseScale),ptr=0;
    for(let k of active)for(let h=0;h<C;h++){const ax=Math.floor(h/na),a=(i*C+h)*3;let v=0;for(let z=0;z<6;z++)v+=bar[3*z+ax]*row.B[k][ord[z][0]]*data.A[a+ord[z][1]];v*=w;out[ptr++]=v;diag[k*C+h]+=v*v;}
    rows.push(out);}
   const mE=zero(),mF=zero(),mG=zero();put(mE,1,V.map(v=>2*v/Q));put(mF,1,U.map(v=>v/qs));put(mF,2,V.map(v=>v/qs));put(mG,2,U.map(v=>2*v/S));
   const ws=2+4*opt.metricSharp*sm;project(mE,ws);project(mF,2*ws);project(mG,ws);
   project(mE.map((v,k)=>e*v+2*f*mF[k]+q*mG[k]),8*opt.metricSharp);
   for(let kap of [H+root,H-root]){let vv=Math.abs(kap)/opt.kgoal-1;if(vv<=0)continue;let aa=m-kap*F,bb=kap*E-l,cc=c-kap*G,dd=kap*F-m;if(cc*cc+dd*dd>aa*aa+bb*bb){aa=cc;bb=dd;}
    let w=Math.sqrt(E*aa*aa+2*F*aa*bb+G*bb*bb);if(w<1e-14)continue;aa/=w;bb/=w;let a=aa*aa,b=2*aa*bb,zz=bb*bb,t=zero(),bn=A.map((v,k)=>a*v+b*B[k]+zz*Z[k]),pn=dot(bn,nn);bn=bn.map((v,k)=>(v-pn*nn[k])/area);
    put(t,1,lin(V,-2*kap*a,U,-kap*b));put(t,2,lin(V,-kap*b,U,-2*kap*zz));put(t,1,cross(U,bn));put(t,2,cross(bn,V));put(t,3,nn.map(v=>v*a));put(t,4,nn.map(v=>v*b));put(t,5,nn.map(v=>v*zz));project(t,2*opt.kw*(1+6*vv*vv)/(opt.kgoal*opt.kgoal));}
   const ar=area/qs;if(ar<.5){let b=zero();put(b,1,cross(U,nn).map(v=>v/qs));put(b,2,cross(nn,V).map(v=>v/qs));project(b,20);}
   const rr=norm(P),cx=301/225,rp=Math.hypot(P[0],P[1]-cx,P[2]),rm=Math.hypot(P[0],P[1]+cx,P[2]),rc=Math.hypot(P[0],P[1]),v=Math.max(0,Math.min(1,(rc-.52)/.02)),allow=.0195*v**3*(10+v*(-15+6*v)),da=.0195*30*(v*(1-v))**2/.02;
   const sg=[rr-1.59,P[1]-opt.wgoal,-P[1]-opt.wgoal,P[2]-.54-allow,-P[2]-.54-allow,opt.hgoal-rp,opt.hgoal-rm];
   for(let k=0;k<7;k++){if(sg[k]<=0)continue;const dg=k===0?P.map(v=>v/rr):k===1?[0,1,0]:k===2?[0,-1,0]:k===3||k===4?[-da*P[0]/rc,-da*P[1]/rc,k===3?1:-1]:[-P[0]/(k===5?rp:rm),-(P[1]+(k===5?-cx:cx))/(k===5?rp:rm),-P[2]/(k===5?rp:rm)];let b=zero();put(b,0,dg);project(b,2*opt.gw);}
   outer.push({off:active[0]*C,rows});
  }
 }
 return {diag,outer};
}
function normalSteps(d,seed,steps=12,iterations=36){const {data,g,opt,dim}=d;let x=Array.from(seed),hist=[],damping=.015;
 const ip=(a,b)=>{let z=0;for(let i=0;i<a.length;i++)z+=a[i]*b[i];return z;};
 for(let it=0;it<steps;it++){let f=evaluateP2(data,x,opt,g),{outer,diag}=fullGramNormal(d,x),sc=diag.map(v=>Math.max(1e-7,v)),rr=Float64Array.from(f.grad,v=>-v),u=rr.map((v,i)=>v/(sc[i]*(1+damping))),q=Float64Array.from(u),dx=new Float64Array(dim),ru=ip(rr,u),nIter=0;
  for(let j=0;j<iterations;j++){let y=q.map((v,i)=>damping*sc[i]*v);for(let block of outer)for(let row of block.rows){let a=0,start=block.off;for(let k=0;k<row.length;k++)a+=row[k]*q[start+k];for(let k=0;k<row.length;k++)y[start+k]+=a*row[k];}
   let den=ip(q,y);if(!(den>0))break;let step=ru/den;for(let i=0;i<dim;i++){dx[i]+=step*q[i];rr[i]-=step*y[i];}u=rr.map((v,i)=>v/(sc[i]*(1+damping)));let nu=ip(rr,u);nIter=j+1;if(nu<1e-9*ip(f.grad,f.grad))break;for(let i=0;i<dim;i++)q[i]=u[i]+q[i]*(nu/ru);ru=nu;}
  let rate=1,ok=false,rn,xn;for(let j=0;j<17;j++){xn=x.map((v,i)=>v+rate*dx[i]);rn=evaluateP2(data,xn,{...opt,deriv:false},g);if(rn.cost<f.cost){ok=true;break;}rate/=2;}
  if(!ok){damping*=8;if(damping>1e4)break;hist.push([it+1,false,damping,f.cost]);continue;}
  x=xn;damping=Math.max(.0002,Math.min(100,damping*(rate===1?.42:rate>=.25?1.2:3)));hist.push([it+1,true,damping,rate,nIter,rn.cost,rn.metric,rn.curvature,rn.held]);}
 let final=evaluateP2(data,x,{...opt,deriv:false},g);return {x,hist,stats:stats(final)};
}function observeP2(cl,p,z,group,lam=1.06){const ntarget=64,targetZ=z;configure(8,8);
 const ind=group==='G11',N=ind?256:group==='G10a'?128:192,angled=ind?.417:0;
 const pts=ownGrid(ind),target=build(pts.length,ntarget,pts.map(v=>v[0]),0);
 let prefixPeak=0,prefixKap=0,prefixAt=[],components=[0,0,0],peak=0,kap=0,held=Infinity,wd=0,bound=0,zhi=0,zlo=Infinity,minArea=Infinity,L=0,lowerQ=Infinity,lowerS=Infinity,mg=Array(7).fill(0),vmax=[0,0,0,0],sqv=[0,0,0,0],mworst,kworst;
 for(let i=0;i<pts.length;i++){let [t,w]=pts[i];const [Q,S0]=gramTarget(jets(target,target.rows[i],targetZ),ntarget),S=S0,Y=new Float64Array(N*18);
  for(let n=0;n<N;n++)Y.set(cl.jet(p,t,2*pi*(n+angled)/N).flat(),18*n);
  L+=w*lam*Math.sqrt(Q);lowerQ=Math.min(lowerQ,Q);lowerS=Math.min(lowerS,S);
  for(let n=0;n<N;n++){const p=18*n,v=(j)=>[Y[p+j],Y[p+j+1],Y[p+j+2]],P=v(0).map(x=>x*lam),V=v(3),U=v(6),A=v(9),B=v(12),C=v(15),E=dot(V,V),F=dot(V,U),G=dot(U,U),base=cross(V,U),ds=norm(base),nor=base.map(a=>a/ds),ar=ds/Math.sqrt(Q*S),ln=dot(A,nor),mn=dot(B,nor),nn=dot(C,nor),H=(G*ln-2*F*mn+E*nn)/(2*ds*ds),K=(ln*nn-mn*mn)/(ds*ds),rd=Math.sqrt(Math.max(0,H*H-K));
   const ka=(H+rd)/lam,kb=(H-rd)/lam,absK=Math.max(Math.abs(ka),Math.abs(kb)),e=E/Q-1,f=F/Math.sqrt(Q*S),g=G/S-1,me=Math.abs((e+g)/2)+Math.hypot((e-g)/2,f),u=2*pi*(n+angled)/N;
   components=[Math.max(components[0],Math.abs(e)),Math.max(components[1],Math.abs(f)),Math.max(components[2],Math.abs(g))];
   if(t<=.24){if(me>prefixPeak){prefixPeak=me;prefixAt=[t,u];}prefixKap=Math.max(prefixKap,absK);}
   if(me>peak){peak=me;mworst=[t,u];}if(absK>kap){kap=absK;kworst=[t,u];}
   const r=norm(P),rp=Math.hypot(P[0],P[1]-lam*(301/225),P[2]),rm=Math.hypot(P[0],P[1]+lam*(301/225),P[2]),rc=Math.hypot(P[0],P[1]),q=Math.max(0,Math.min(1,(rc-.52)/.02)),a=.0195*q**3*(10+q*(-15+6*q));
   held=Math.min(held,rp,rm);bound=Math.max(bound,r);wd=Math.max(wd,Math.abs(P[1]));zhi=Math.max(zhi,P[2]);zlo=Math.min(zlo,P[2]);minArea=Math.min(minArea,ar);
   let geo=[r-1.59,P[1]-.885,-P[1]-.885,P[2]-lam*endZ-a,-P[2]-lam*endZ-a,.65-rp,.65-rm].map(x=>Math.max(0,x));for(let j=0;j<7;j++)mg[j]=Math.max(mg[j],geo[j]);
   let metric2=e*e+2*f*f+g*g,cv=[ka,kb].map(k=>Math.max(0,Math.abs(k)-9.5));let msum=metric2*(1+metric2/.12**2),kn=cv.reduce((v,c)=>v+c*c,0),ksum=kn*(1+kn/4),gsum=geo.reduce((v,a)=>v+a*a,0),aa=Math.max(0,(.5/ar)**2-1)**2;
   let wt=w*lam*Math.sqrt(Q)/N;for(let j=0;j<4;j++){let v=[msum,ksum,gsum,aa][j];sqv[j]+=wt*v;vmax[j]=Math.max(vmax[j],v);}
  }
 }
 return {prefixPeak,prefixKap,prefixAt,components,group,radial:pts.length,angles:N,trueRowCount:14*pts.length*N,metric:peak,curvature:kap,held,halfWidth:wd,ballRadius:bound,upperZ:[zlo,zhi],minimumAreaRatio:minArea,physicalTransitionLength:L,finiteMinTargetSquared:[lowerQ,lowerS],metricWitness:mworst,curvatureWitness:kworst,guideMax:mg,groupSquaredNorms:sqv,groupMaxSquared:vmax};
}

export {compactStadium,buildOtherCenterData,changedCenterCauchyFull,p2Design,p2Controlled,fullGramNormal,normalSteps,observeP2};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,p540,field,coeff,out]=process.argv.slice(2),read=x=>JSON.parse(readFileSync(x)),write=(x,z)=>writeFileSync(x,JSON.stringify(z)+'\n'),z=read(state),p=read(p540);
 if(op==='make256'||op==='make512'){const N=Number(op.slice(4)),s=p32SpectralCauchy(z,N,N===256?768:1536,.24,true,1,48,true,compactStadium(2,.2)),ck=buildOtherCenterData(z,s,N===256?48:96,.70);write(field,ck);}
 else if(op==='fit726'){const d=p2Design(z,p,read(field)),r=lbfgs(d.data,Array(d.dim).fill(0),d.opt,220,null,d.g);write(coeff,r.z);console.log(JSON.stringify(r.stats));}
 else if(op==='gn726'){const d=p2Design(z,p,read(field)),r=normalSteps(d,read(coeff),12,35);write(out,r.x);console.log(JSON.stringify(r.hist));}
 else if(op==='observe'){const ck=read(field),m=coeff?p2Controlled(z,p,ck,read(coeff)):changedCenterCauchyFull(z,p,ck,.70);console.log(JSON.stringify(['G10a','G10b','G11'].map(g=>observeP2(m,[],z,g)),null,2));}
 else throw Error('make256/make512/observe STATE192 STATE540 FIELD [FREE726] | fit726 STATE192 STATE540 FIELD FREE726 | gn726 STATE192 STATE540 FIELD FREE726 NEW726');
}
