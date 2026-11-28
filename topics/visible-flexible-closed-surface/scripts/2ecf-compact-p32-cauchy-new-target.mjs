#!/usr/bin/env node
/** Reconstruct both Cauchy fields from original true angular and radial material data. */
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {configure,build,jets,gramTarget,lbfgs} from './2ecf-compact-p32-direct-field.mjs';
import {gauss01} from './2ecf-compact-p32-normal-meridian-design.mjs';
import {compactMixedJets,packetCompactCore,packetControlled} from './2ecf-compact-p32-prufer-physical-annulus.mjs';
const pi=Math.PI,endZ=.54,dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],norm=a=>Math.sqrt(dot(a,a)),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const centralA=compactMixedJets(Array(192).fill(0))(0,0)[0][0];
function ownGrid(isIndependent){
 const ns=isIndependent?60:95,degree=isIndependent?11:10,[g,w]=gauss01(degree);
 let arr=[];for(let i=0;i<ns;i++)for(let j=0;j<degree;j++)arr.push([(i+g[j])/(ns+1),w[j]/(ns+1)]);
 const [last,ww]=gauss01(8);for(let j=0;j<8;j++)arr.push([(ns+last[j])/(ns+1),ww[j]/(ns+1)]);
 arr.sort((a,b)=>a[0]-b[0]);return arr;}

function fftRealDerivative(a){
 const n=a.length,re=Float64Array.from(a),im=new Float64Array(n);function fft(inv){
 for(let i=1,j=0;i<n;i++){let b=n>>1;for(;j&b;b>>=1)j^=b;j^=b;if(i<j){let x=re[i];re[i]=re[j];re[j]=x;x=im[i];im[i]=im[j];im[j]=x;}}
 for(let w=2;w<=n;w*=2){const arg=(inv?1:-1)*2*Math.PI/w,cr=Math.cos(arg),ci=Math.sin(arg);for(let i=0;i<n;i+=w){let x=1,y=0;for(let j=0;j<w/2;j++){const l=i+j,h=l+w/2,U=re[h]*x-im[h]*y,V=re[h]*y+im[h]*x;re[h]=re[l]-U;im[h]=im[l]-V;re[l]+=U;im[l]+=V;let nx=x*cr-y*ci;y=x*ci+y*cr;x=nx;}}}}
 fft(false);for(let i=0;i<n;i++){let k=i<n/2?i:i===n/2?0:i-n,a=re[i],b=im[i];re[i]=-k*b;im[i]=k*a;}fft(true);return re.map(x=>x/n);
}
function p32SpectralCauchy(z,N=512,nstep=800,stop=.08,keep=false,weight=1,snapshots=40,spectral=true){
 const raw=compactMixedJets(z),pi=Math.PI,ip=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],dh=2*pi/N,dt=stop/nstep,cache=new Map(),size=14*N,Y=new Float64Array(size);
 function target(j){if(cache.has(j))return cache.get(j);let t=j*dt/2,Q=0,S=0,Qt=0,St=0,Stt=0;for(let k=0;k<64;k++){let y=raw(t,2*pi*k/64);Q+=ip(y[1],y[1])/64;S+=ip(y[2],y[2])/64;Qt+=2*ip(y[1],y[3])/64;St+=2*ip(y[2],y[4])/64;Stt+=2*(ip(y[4],y[4])+ip(y[2],y[7]))/64;}let e=Math.sqrt(Q),f0=Math.sqrt(S),ft0=St/(2*f0),ftt0=Stt/(2*f0)-ft0*ft0/f0,f=1+weight*(f0-1),ft=weight*ft0,ftt=weight*ftt0,K=-(ftt-ft*Qt/(2*Q))/(Q*f);const v=[e,f,ft,K];cache.set(j,v);return v;}
 const der=(a,j)=>(a[(j+N-2)%N]-8*a[(j+N-1)%N]+8*a[(j+1)%N]-a[(j+2)%N])/(12*dh);
 for(let k=0;k<N;k++){let x=raw(0,2*pi*k/N),es=x[1].map(v=>v/1.2),u=x[2],n=cross(es,u),off=14*k;Y.set([ip(n,x[5]),0,...es,...u,...n,...x[0]],off);}
 function rhs(Y,j){const [e,f,ft,K]=target(j),l=new Float64Array(N),m=new Float64Array(N),R=new Float64Array(size);
  for(let i=0;i<N;i++){let h=14*i;m[i]=Y[h+1];l[i]=(K+m[i]*m[i])/Y[h];}
  const dm=spectral?fftRealDerivative(m):m.map((_,j)=>der(m,j)),dl=spectral?fftRealDerivative(l):l.map((_,j)=>der(l,j));for(let i=0;i<N;i++){let h=i*14,n=Y[h];R[h]=(e*dm[i]+ft*(l[i]-n))/f;R[h+1]=(e*dl[i]-2*ft*m[i])/f;
   for(let k=0;k<3;k++){R[h+2+k]=e*l[i]*Y[h+8+k];R[h+5+k]=e*m[i]*Y[h+8+k];R[h+8+k]=-e*(l[i]*Y[h+2+k]+m[i]*Y[h+5+k]);R[h+11+k]=e*Y[h+2+k];}}
  return R;
 }
 const add=(x,y,d)=>x.map((a,i)=>a+d*y[i]);let rec=[],maxSoFar=0,first=null,snapshot=[];
 function observe(j){let [e,f,ft,K]=target(j*2),max=0,loc=0,min=Infinity,frameError=0,angleError=0;
  for(let k=0;k<N;k++){let h=14*k,n=Y[h],m=Y[h+1],l=(K+m*m)/n,kap=(Math.abs(.5*(n+l))+Math.hypot(.5*(n-l),m))/1.06;min=Math.min(min,n);if(kap>max){max=kap;loc=k;}const s=Y.slice(h+2,h+5),v=Y.slice(h+5,h+8);frameError=Math.max(frameError,Math.abs(ip(s,s)-1),Math.abs(ip(v,v)-1),Math.abs(ip(s,v)));for(let c=0;c<3;c++){const at=d=>Y[14*((k+N+d)%N)+11+c],d=(at(-2)-8*at(-1)+8*at(1)-at(2))/(12*dh);angleError=Math.max(angleError,Math.abs(d-f*v[c]));}}
  maxSoFar=Math.max(maxSoFar,max);if(first===null&&max>1/(.03*3.03588))first=[j*dt,max,2*pi*loc/N];return {t:j*dt,K,minimumN:min,maximumPhysicalCurvature:max,curvatureAngle:2*pi*loc/N,frameError,angleCompatibility:angleError};}
 for(let j=0;j<nstep;j++){if(j%Math.max(1,Math.round(nstep/snapshots))===0){let a=observe(j);rec.push(a);if(keep)snapshot.push(Array.from(Y));if(!Number.isFinite(a.maximumPhysicalCurvature)||a.minimumN<.005||a.maximumPhysicalCurvature>200)break;}
  const d1=rhs(Y,2*j),d2=rhs(add(Y,d1,dt/2),2*j+1),d3=rhs(add(Y,d2,dt/2),2*j+1),d4=rhs(add(Y,d3,dt),2*j+2);for(let i=0;i<size;i++)Y[i]+=dt/6*(d1[i]+2*d2[i]+2*d3[i]+d4[i]);}
 if(rec.length===snapshots){rec.push(observe(nstep));if(keep)snapshot.push(Array.from(Y));}return {N,nstep,stop,maxSoFar,first,rec,snapshot};
}
function compactCauchyPositions(z,sol,M=48){
 const raw=compactMixedJets(z),pi=Math.PI,N=sol.N,times=sol.rec.map(x=>x.t),sample=sol.snapshot,controls=[],a0=3*M,ip=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
 if(sample.length!==times.length)throw Error('Cauchy computation ended before its fixed endpoint');
 const A=Array.from({length:N},(_,j)=>Array.from({length:a0},(_,i)=>{let c=Math.floor(i/M),k=i%M,m=c===2?2*k:2*k+1;return (c===1?Math.sin(m*2*pi*j/N):Math.cos(m*2*pi*j/N))*(m===0?1:2)/N;}));
 for(let I=0;I<times.length;I++){const t=times[I],data=sample[I],row=Array.from({length:3},()=>new Float64Array(a0));if(I===0){controls.push(row);continue;}
  let Q=0,Qd=0;for(let j=0;j<64;j++){const X=raw(t,2*pi*j/64);Q+=ip(X[1],X[1])/64;Qd+=2*ip(X[1],X[3])/64;}let e=Math.sqrt(Q),ed=Qd/(2*e),K=sol.rec[I].K;
  for(let j=0;j<N;j++){const x=raw(t,2*pi*j/N),ii=14*j,n=data[ii],m=data[ii+1],l=(K+m*m)/n;for(let c=0;c<3;c++){
   const d=[data[ii+11+c]-x[0][c],e*data[ii+2+c]-x[1][c],ed*data[ii+2+c]+Q*l*data[ii+8+c]-x[3][c]];
   for(let k=0;k<M;k++){let a=c*M+k,v=A[j][a];for(let h=0;h<3;h++)row[h][a]+=v*d[h];}}}
  controls.push(row);
 }
 return {times,controls:controls.map(row=>row.map(a=>Array.from(a))),M,stop:sol.stop,weight:.35};
}
function trueCauchyFull(z,oldCoeffs,ck,finish=.43){
 const {times,controls,M,stop}=ck,pi=Math.PI,n=times.length-1,step=stop/n,base=packetCompactCore(z,{left:.44,right:.8,mode:-.006,radialMix:1}),prior=packetControlled(z,oldCoeffs),a0=3*M,radCache=new Map(),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];
 const zero=Array.from({length:3},()=>new Float64Array(a0));
 function bern(t){let b=[[1]];for(let n=1;n<=5;n++){let r=b.at(-1);b.push(Array.from({length:n+1},(_,i)=>(1-t)*(r[i]||0)+t*(r[i-1]||0)));}return [b[5],Array.from({length:6},(_,i)=>5*((b[4][i-1]||0)-(b[4][i]||0))),Array.from({length:6},(_,i)=>20*((b[3][i-2]||0)-2*(b[3][i-1]||0)+(b[3][i]||0)))];}
 function row(t){if(radCache.has(t))return radCache.get(t);let i=t>=stop?n:Math.max(0,Math.min(n-1,Math.floor(t/step))),a=controls[i],b=i===n?zero:controls[i+1],L=i===n?finish-stop:times[i+1]-times[i],x=(t-times[i])/L,B=bern(x),v=Array.from({length:3},()=>new Float64Array(a0));
  for(let k=0;k<a0;k++){let aa=[a[0][k],a[0][k]+L*a[1][k]/5,a[0][k]+2*L*a[1][k]/5+L*L*a[2][k]/20,b[0][k]-2*L*b[1][k]/5+L*L*b[2][k]/20,b[0][k]-L*b[1][k]/5,b[0][k]];for(let d=0;d<3;d++)for(let w=0;w<6;w++)v[d][k]+=B[d][w]*aa[w]/L**d;}
  if(radCache.size<12000)radCache.set(t,v);return v;}
 function jet(p,t,u){if(t>=finish)return prior.jet([],t,u);let P=base.one(t,u),co=row(t);if(t>stop){let q=(t-stop)/(finish-stop),s=q**3*(10+q*(-15+6*q)),d=30*(q*(1-q))**2/(finish-stop),dd=60*q*(1-q)*(1-2*q)/(finish-stop)**2,W=prior.jet([],t,u).map((v,i)=>v.map((x,k)=>x-P[i][k]));
   P=P.map((v,i)=>v.map((x,k)=>x+s*W[i][k]));for(let k=0;k<3;k++){P[1][k]+=d*W[0][k];P[3][k]+=dd*W[0][k]+2*d*W[1][k];P[4][k]+=d*W[2][k];}}
  const cs=[1],ss=[0],c=Math.cos(u),s=Math.sin(u);for(let k=1;k<2*M;k++){cs.push(cs[k-1]*c-ss[k-1]*s);ss.push(ss[k-1]*c+cs[k-1]*s);}for(let k=0;k<a0;k++){let c=Math.floor(k/M),j=k%M,m=c===2?2*j:2*j+1,v=c===1?ss[m]:cs[m],d=m*(c===1?cs[m]:-ss[m]);P[0][c]+=co[0][k]*v;P[1][c]+=co[1][k]*v;P[2][c]+=co[0][k]*d;P[3][c]+=co[2][k]*v;P[4][c]+=co[1][k]*d;P[5][c]-=co[0][k]*m*m*v;}return P;}
 return {jet,stop,finish};
}
function cauchyGoal(t,S0){let x=Math.max(0,Math.min(1,(t-.14)/(.42-.14))),w=.35+.65*x**3*(10+x*(-15+6*x));return (1+w*(Math.sqrt(S0)-1))**2;}
function cauchyFitDesign(z,prev,ck,opts={}){
 const nf=opts.nf??22,na=opts.na??10,N=opts.N??72,R=opts.R??64,steps=opts.steps??240,end=.8,start=.14,f= trueCauchyFull(z,prev,ck,opts.finish??.70),radii=Array.from({length:R},(_,i)=>i/(R-1));
 configure(8,8);let goal=build(R,64,radii),g=goal.rows.map(row=>{let [q,s]=gramTarget(jets(goal,row,z),64);return [q,cauchyGoal(row.t,s)];});
 configure(nf,na);const data=build(R,N,radii),h=(end-start)/(nf+3);
 function basis(t,j){let x=(t-start)/h-j-2,k=Math.abs(x),s=Math.sign(x);if(k>=2)return [0,0,0];return k>1?[h*(2-k)**3/6,-s*(2-k)**2/2,(2-k)/h]:[h*(2/3-k*k+.5*k**3),s*(-2*k+1.5*k*k),(-2+3*k)/h];}
 for(let row of data.rows){row.B=Array.from({length:nf},(_,j)=>basis(row.t,j));for(let i=0;i<N;i++)row.base.set(f.jet([],row.t,2*Math.PI*i/N).flat(),18*i);}
 let x=opts.initial||Array(nf*na*3).fill(0),o={metricSharp:opts.sharp??48,kw:opts.kw??2.5,gw:opts.gw??600,kgoal:10.4,wgoal:.8425,hgoal:.612};return lbfgs(data,x,o,steps,opts.mem??null,g);
}
function cauchyControlled(z,prev,ck,params,nf=22,na=10,finish=.70){
 const actual=trueCauchyFull(z,prev,ck,finish),start=.14,end=.8,h=(end-start)/(nf+3),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];
 return {jet(p,t,u){let Y=actual.jet([],t,u);if(t<=start||t>=end)return Y;
 for(let j=Math.max(0,Math.floor((t-start)/h)-3);j<Math.min(nf,Math.floor((t-start)/h)+1);j++){let q=(t-start)/h-j-2,k=Math.abs(q),sg=Math.sign(q);if(k>=2)continue;let b=k>1?[h*(2-k)**3/6,-sg*(2-k)**2/2,(2-k)/h]:[h*(2/3-k*k+.5*k**3),sg*(-2*k+1.5*k*k),(-2+3*k)/h];
 for(let a=0;a<3;a++)for(let c=0;c<na;c++){let m=a===2?2*c:2*c+1,co=Math.cos(m*u),si=Math.sin(m*u),v=params[(j*3+a)*na+c],A=a===1?[si,m*co,-m*m*si]:[co,-m*si,-m*m*co];
 for(let i=0;i<6;i++)Y[i][a]+=v*b[orders[i][0]]*A[orders[i][1]];}}return Y;}};
}
function observeCauchy(cl,p,z,group,lam=1.06){const ntarget=64,targetZ=z;configure(8,8);
 const ind=group==='G11',N=ind?256:group==='G10a'?128:192,angled=ind?.417:0;
 const pts=ownGrid(ind),target=build(pts.length,ntarget,pts.map(v=>v[0]),0);
 let prefixPeak=0,prefixKap=0,prefixAt=[],components=[0,0,0],peak=0,kap=0,held=Infinity,wd=0,bound=0,zhi=0,zlo=Infinity,minArea=Infinity,L=0,lowerQ=Infinity,lowerS=Infinity,mg=Array(7).fill(0),vmax=[0,0,0,0],sqv=[0,0,0,0],mworst,kworst;
 for(let i=0;i<pts.length;i++){let [t,w]=pts[i];const [Q,S0]=gramTarget(jets(target,target.rows[i],targetZ),ntarget),S=cauchyGoal(t,S0),Y=new Float64Array(N*18);
  for(let n=0;n<N;n++)Y.set(cl.jet(p,t,2*pi*(n+angled)/N).flat(),18*n);
  L+=w*lam*Math.sqrt(Q);lowerQ=Math.min(lowerQ,Q);lowerS=Math.min(lowerS,S);
  for(let n=0;n<N;n++){const p=18*n,v=(j)=>[Y[p+j],Y[p+j+1],Y[p+j+2]],P=v(0).map(x=>x*lam),V=v(3),U=v(6),A=v(9),B=v(12),C=v(15),E=dot(V,V),F=dot(V,U),G=dot(U,U),base=cross(V,U),ds=norm(base),nor=base.map(a=>a/ds),ar=ds/Math.sqrt(Q*S),ln=dot(A,nor),mn=dot(B,nor),nn=dot(C,nor),H=(G*ln-2*F*mn+E*nn)/(2*ds*ds),K=(ln*nn-mn*mn)/(ds*ds),rd=Math.sqrt(Math.max(0,H*H-K));
   const ka=(H+rd)/lam,kb=(H-rd)/lam,absK=Math.max(Math.abs(ka),Math.abs(kb)),e=E/Q-1,f=F/Math.sqrt(Q*S),g=G/S-1,me=Math.abs((e+g)/2)+Math.hypot((e-g)/2,f),u=2*pi*(n+angled)/N;
   components=[Math.max(components[0],Math.abs(e)),Math.max(components[1],Math.abs(f)),Math.max(components[2],Math.abs(g))];
   if(t<=.14){if(me>prefixPeak){prefixPeak=me;prefixAt=[t,u];}prefixKap=Math.max(prefixKap,absK);}
   if(me>peak){peak=me;mworst=[t,u];}if(absK>kap){kap=absK;kworst=[t,u];}
   const r=norm(P),rp=Math.hypot(P[0],P[1]-lam*centralA,P[2]),rm=Math.hypot(P[0],P[1]+lam*centralA,P[2]),rc=Math.hypot(P[0],P[1]),q=Math.max(0,Math.min(1,(rc-.52)/.02)),a=.0195*q**3*(10+q*(-15+6*q));
   held=Math.min(held,rp,rm);bound=Math.max(bound,r);wd=Math.max(wd,Math.abs(P[1]));zhi=Math.max(zhi,P[2]);zlo=Math.min(zlo,P[2]);minArea=Math.min(minArea,ar);
   let geo=[r-1.59,P[1]-.885,-P[1]-.885,P[2]-lam*endZ-a,-P[2]-lam*endZ-a,.65-rp,.65-rm].map(x=>Math.max(0,x));for(let j=0;j<7;j++)mg[j]=Math.max(mg[j],geo[j]);
   let metric2=e*e+2*f*f+g*g,cv=[ka,kb].map(k=>Math.max(0,Math.abs(k)-9.5));let msum=metric2*(1+metric2/.12**2),kn=cv.reduce((v,c)=>v+c*c,0),ksum=kn*(1+kn/4),gsum=geo.reduce((v,a)=>v+a*a,0),aa=Math.max(0,(.5/ar)**2-1)**2;
   let wt=w*lam*Math.sqrt(Q)/N;for(let j=0;j<4;j++){let v=[msum,ksum,gsum,aa][j];sqv[j]+=wt*v;vmax[j]=Math.max(vmax[j],v);}
  }
 }
 return {prefixPeak,prefixKap,prefixAt,components,group,radial:pts.length,angles:N,trueRowCount:14*pts.length*N,metric:peak,curvature:kap,held,halfWidth:wd,ballRadius:bound,upperZ:[zlo,zhi],minimumAreaRatio:minArea,physicalTransitionLength:L,finiteMinTargetSquared:[lowerQ,lowerS],metricWitness:mworst,curvatureWitness:kworst,guideMax:mg,groupSquaredNorms:sqv,groupMaxSquared:vmax};
}

export {p32SpectralCauchy,compactCauchyPositions,trueCauchyFull,cauchyGoal,cauchyFitDesign,cauchyControlled,observeCauchy};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,p540,field,out]=process.argv.slice(2),read=x=>JSON.parse(readFileSync(x)),z=read(state);
 if(op==='original'){let a=p32SpectralCauchy(z,512,600,.12,false,1,40,false);console.log(JSON.stringify({first:a.first,maximum:a.maxSoFar,record:a.rec},null,2));}
 else if(op==='make256'||op==='make512'||op==='make1024'){const N=Number(op.slice(4)),[steps,snap,M]=N===256?[560,35,40]:N===512?[1120,70,80]:[1600,80,192];
 const s=p32SpectralCauchy(z,N,steps,.14,true,.35,snap),d=compactCauchyPositions(z,s,M);writeFileSync(field,JSON.stringify(d)+'\n');console.log(JSON.stringify({rows:s.rec.length,curvature:s.maxSoFar}));}
 else if(op==='observe'){const m=trueCauchyFull(z,read(p540),read(field));console.log(JSON.stringify(['G10a','G10b','G11'].map(g=>observeCauchy(m,[],z,g)),null,2));}
 else if(op==='fit660'){let r=cauchyFitDesign(z,read(p540),read(field));writeFileSync(out,JSON.stringify(r.z)+'\n');console.log(JSON.stringify({state:r.stats,steps:r.hist},null,2));}
 else if(op==='observe660'){const m=cauchyControlled(z,read(p540),read(field),read(out));console.log(JSON.stringify(['G10a','G10b','G11'].map(g=>observeCauchy(m,[],z,g)),null,2));}
 else throw Error('original STATE192 | make256/make512/make1024/observe STATE192 STATE540 FIELD | fit660/observe660 STATE192 STATE540 FIELD NEW660');
}
