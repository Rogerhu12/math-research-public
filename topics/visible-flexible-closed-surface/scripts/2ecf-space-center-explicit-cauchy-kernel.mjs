#!/usr/bin/env node
/** Shared outward material frame and position encoder with an explicit strip reference. */
import {compactMixedJets,packetControlled} from './2ecf-compact-p32-prufer-physical-annulus.mjs';
import {rayHermite} from './2ecf-compact-p2-two-port-rays.mjs';
import {twistedStrip,observeTwist} from './2ecf-compact-space-center-flat-strip.mjs';
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
function fftRealDerivative(a){
 const n=a.length,re=Float64Array.from(a),im=new Float64Array(n);function fft(inv){
 for(let i=1,j=0;i<n;i++){let b=n>>1;for(;j&b;b>>=1)j^=b;j^=b;if(i<j){let x=re[i];re[i]=re[j];re[j]=x;x=im[i];im[i]=im[j];im[j]=x;}}
 for(let w=2;w<=n;w*=2){const arg=(inv?1:-1)*2*Math.PI/w,cr=Math.cos(arg),ci=Math.sin(arg);for(let i=0;i<n;i+=w){let x=1,y=0;for(let j=0;j<w/2;j++){const l=i+j,h=l+w/2,U=re[h]*x-im[h]*y,V=re[h]*y+im[h]*x;re[h]=re[l]-U;im[h]=im[l]-V;re[l]+=U;im[l]+=V;let nx=x*cr-y*ci;y=x*ci+y*cr;x=nx;}}}}
 fft(false);for(let i=0;i<n;i++){let k=i<n/2?i:i===n/2?0:i-n,a=re[i],b=im[i];re[i]=-k*b;im[i]=k*a;}fft(true);return re.map(x=>x/n);
}
function orientedCauchy(z,N=512,nstep=800,stop=.08,keep=false,weight=1,snapshots=40,curveMode=null){
 const raw=compactMixedJets(z),pi=Math.PI,ip=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],dh=2*pi/N,dt=stop/nstep,cache=new Map(),size=14*N,Y=new Float64Array(size);
 function target(j){if(cache.has(j))return cache.get(j);let t=j*dt/2,Q=0,S=0,Qt=0,St=0,Stt=0;for(let k=0;k<64;k++){let y=raw(t,2*pi*k/64);Q+=ip(y[1],y[1])/64;S+=ip(y[2],y[2])/64;Qt+=2*ip(y[1],y[3])/64;St+=2*ip(y[2],y[4])/64;Stt+=2*(ip(y[4],y[4])+ip(y[2],y[7]))/64;}let e=Math.sqrt(Q),f0=Math.sqrt(S),ft0=St/(2*f0),ftt0=Stt/(2*f0)-ft0*ft0/f0,f=1+weight*(f0-1),ft=weight*ft0,ftt=weight*ftt0,K=-(ftt-ft*Qt/(2*Q))/(Q*f);const v=[e,f,ft,K];cache.set(j,v);return v;}
 const der=(a,j)=>(a[(j+N-2)%N]-8*a[(j+N-1)%N]+8*a[(j+1)%N]-a[(j+2)%N])/(12*dh);
 for(let k=0;k<N;k++){const q=curveMode(2*pi*k/N);Y.set([q.n,q.m,...q.B,...q.V,...q.N,...q.P],14*k);}
 function rhs(Y,j){const [e,f,ft,K]=target(j),l=new Float64Array(N),m=new Float64Array(N),R=new Float64Array(size);
  for(let i=0;i<N;i++){let h=14*i;m[i]=Y[h+1];l[i]=(K+m[i]*m[i])/Y[h];}
  const dm=fftRealDerivative(m),dl=fftRealDerivative(l);for(let i=0;i<N;i++){let h=i*14,n=Y[h];R[h]=(e*dm[i]+ft*(l[i]-n))/f;R[h+1]=(e*dl[i]-2*ft*m[i])/f;
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
}function twistReference(z,p,flat=twistedStrip(),s0=13/128){const base=packetControlled(z,p),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]],cache=new Map();return (t,u)=>{if(t>=.6)return base.jet([],t,u);let chi=t/.6,c=chi**3*(10+chi*(-15+6*chi)),ct=30*(chi*(1-chi))**2/.6,ctt=60*chi*(1-chi)*(1-2*chi)/.36,th=Math.tanh(1.2*t/.036),s=s0+.036*th,st=1.2*(1-th*th),stt=-2*1.2**2*th*(1-th*th)/.036;
 const R=flat.ring(s,u).jet,X=[R[0],R[1].map(v=>v*st),R[2],R[3].map((v,k)=>v*st**2+R[1][k]*stt),R[4].map(v=>v*st),R[5]],Y=base.jet([],t,u),W=Y.map((v,i)=>v.map((q,k)=>q-X[i][k])),out=X.map((v,i)=>v.map((q,k)=>q+c*W[i][k]));for(let k=0;k<3;k++){out[1][k]+=ct*W[0][k];out[3][k]+=ctt*W[0][k]+2*ct*W[1][k];out[4][k]+=ct*W[2][k];}return out;};}
function buildTwistField(z,p,sol,M,finish=.70,ref=twistReference(z,p)){const raw=compactMixedJets(z),N=sol.N,times=sol.rec.map(q=>q.t),controls=[],K=2*M+1;
 if(!Number.isFinite(sol.rec.at(-1).minimumN)||times.at(-1)<sol.stop-1e-9)throw Error('incomplete source');
 const A=Array.from({length:N},(_,j)=>Array.from({length:K},(_,i)=>i===0?1/N:2*(i%2?Math.cos((i+1)/2*2*Math.PI*j/N):Math.sin(i/2*2*Math.PI*j/N))/N));
 for(let I=0;I<times.length;I++){let t=times[I],row=Array.from({length:3},()=>new Float64Array(3*K)),Q=0,Qd=0;for(let k=0;k<64;k++){let q=raw(t,Math.PI*k/32);Q+=dot(q[1],q[1])/64;Qd+=2*dot(q[1],q[3])/64;}if(I>0){let data=sol.snapshot[I],e=Math.sqrt(Q),ed=Qd/(2*e),gauss=sol.rec[I].K;for(let j=0;j<N;j++){let o=14*j,Y=ref(t,2*Math.PI*j/N),l=(gauss+data[o+1]**2)/data[o];for(let c=0;c<3;c++){let d0=data[o+11+c]-Y[0][c],d1=e*data[o+2+c]-Y[1][c],d2=ed*data[o+2+c]+Q*l*data[o+8+c]-Y[3][c];for(let k=0;k<K;k++){let v=A[j][k],i=c*K+k;row[0][i]+=v*d0;row[1][i]+=v*d1;row[2][i]+=v*d2;}}}}
 controls.push(row.map(v=>Array.from(v)));}times.push(finish);controls.push(Array.from({length:3},()=>Array(3*K).fill(0)));return {M,times,controls,stop:sol.stop,finish};}
function twistComplete(z,p,f,ref=twistReference(z,p)){const {times,controls,M,finish}=f,K=2*M+1,cache=new Map(),angles=new Map(),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];return {jet(_,t,u){const X=ref(t,u);if(t>=finish)return X;let V=cache.get(t);if(!V){let i=0;while(times[i+1]<t)i++;let a=controls[i],b=controls[i+1],L=times[i+1]-times[i],s=(t-times[i])/L;V=Array.from({length:3},(_,d)=>Array.from({length:3*K},(_,k)=>rayHermite(a.map(q=>q[k]),b.map(q=>q[k]),L,s,d)));if(cache.size<3000)cache.set(t,V);}let tr=angles.get(u);if(!tr){tr=Array.from({length:K},(_,j)=>{if(!j)return [1,0,0];let m=(j+1)>>1,c=Math.cos(m*u),s=Math.sin(m*u);return j%2?[c,-m*s,-m*m*c]:[s,m*c,-m*m*s];});if(angles.size<5000)angles.set(u,tr);}for(let i=0;i<6;i++)for(let c=0;c<3;c++){let q=0;for(let k=0;k<K;k++)q+=V[orders[i][0]][c*K+k]*tr[k][orders[i][1]];X[i][c]+=q;}return X;}};}

export {orientedCauchy,twistReference,buildTwistField,twistComplete,observeTwist};
