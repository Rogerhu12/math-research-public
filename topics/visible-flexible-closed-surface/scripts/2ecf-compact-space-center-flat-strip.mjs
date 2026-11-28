#!/usr/bin/env node
/** Genuine space-curve center, rectifying flat strip, and fully angular upper Cauchy positions. */
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {gauss01} from './2ecf-compact-p32-normal-meridian-design.mjs';
import {compactMixedJets,packetControlled} from './2ecf-compact-p32-prufer-physical-annulus.mjs';
import {rayHermite} from './2ecf-compact-p2-two-port-rays.mjs';
import {configure,build,jets,gramTarget} from './2ecf-compact-p32-direct-field.mjs';
const pi=Math.PI,endZ=.54,dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],norm=a=>Math.sqrt(dot(a,a));
function rigorousSpaceTwist(panels=8192){const E=10n**22n,low=(x,d)=>x>=0n?x/d:-((-x+d-1n)/d),up=(x,d)=>-low(-x,d),q=(a,b=1)=>[low(BigInt(a)*E,BigInt(b)),up(BigInt(a)*E,BigInt(b))],add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[1],-a[0]],sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>{let v=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]],l=v.reduce((x,y)=>x<y?x:y),r=v.reduce((x,y)=>x>y?x:y);return [low(l,E),up(r,E)];},sqr=a=>{let b=mul(a,a);if(b[0]<0n)b[0]=0n;return b;},abs=a=>[a[0]>=0n?a[0]:a[1]<=0n?-a[1]:0n,-a[0]>a[1]?-a[0]:a[1]],div=(a,b)=>{if(b[0]<=0n)throw Error('nonpositive denominator');return mul(a,[low(E*E,b[1]),up(E*E,b[0])]);},isqrt=z=>{if(z===0n)return 0n;let r=1n<<BigInt(Math.ceil(z.toString(2).length/2));for(;;){let f=(r+z/r)/2n;if(f>=r)return r;r=f;}},sqrt=a=>{let l=isqrt(E*a[0]),r=isqrt(E*a[1]);return [l,r*r===E*a[1]?r:r+1n];};
 const h=q(9,100),w=q(13,128),lam=q(53,50),o=q(1),b16=mul(q(16),sqr(h)),four=mul(q(4),h);let J=E,K=0n,Amax=0n;
 for(let i=0;i<panels;i++){let x=[q(i,panels)[0],q(i+1,panels)[1]],d=sub(o,x),rho=add(q(1,5),mul(q(32,15),sqr(x))),H=add(o,mul(mul(b16,x),sqr(d))),Hp=mul(mul(b16,d),sub(o,mul(q(3),x))),P=sub(mul(add(q(3),H),x),o),Pp=add(add(q(3),H),mul(x,Hp)),B=sub(add(neg(mul(P,H)),mul(q(2),mul(d,mul(Pp,H)))),mul(q(3),mul(d,mul(P,Hp)))),D=add(mul(sqr(H),H),mul(b16,mul(d,sqr(P)))),v=mul(rho,mul(sqr(H),sqrt(H))),corr=mul(mul(four,w),mul(sqrt(x),abs(B))),jac=div(sub(v,corr),v),kap=div(D,mul(lam,sub(v,corr))),aa=div(mul(four,mul(sqrt(d),abs(P))),mul(H,sqrt(H)));if(jac[0]<J)J=jac[0];if(kap[1]>K)K=kap[1];if(aa[1]>Amax)Amax=aa[1];}
 if(J<=q(584,1000)[1]||K>=q(774,100)[0]||Amax>=q(361,1000)[0])throw Error('requested strict estimate fails');return {panels,scale:E.toString(),jacobianLower:J.toString(),physicalCurvatureUpper:K.toString(),absoluteTorsionRatioUpper:Amax.toString()};}
function twistedStrip(h=.09){const pi=Math.PI,[g,w]=gauss01(16),TWO=2*pi,centerCache=new Map();
 function local(t){const s=Math.sin(t),c=Math.cos(t),x=s*s,d=c*c,H=1+16*h*h*x*d*d,P=-1+(3+H)*x,Hp=16*h*h*d*(1-3*x),Pp=3+H+Hp*x,b=-P*H+2*d*Pp*H-3*d*P*Hp,r=.2+32/15*x*x,k=-4*h*s*c,om=h*(1-2*x),o=Math.cos(om),v=Math.sin(om),a=4*h*c*P/H**1.5,ad=4*h*s*b/(r*H**2.5),U=t-8/15*Math.sin(2*t)+1/15*Math.sin(4*t),K=Math.sqrt(H)/r,V=[-s,c*o,c*v],B=[c*c*k,(s*c*k*o-v)/Math.sqrt(H),(s*c*k*v+o)/Math.sqrt(H)];B[0]/=Math.sqrt(H);const N=[-c/Math.sqrt(H),(-s*o-c*k*v)/Math.sqrt(H),(-s*v+c*k*o)/Math.sqrt(H)];return {r,U,a,ad,K,V,B,N};}
 function xy(t){let q=centerCache.get(t);if(q)return q;const c=Math.cos(t),s=Math.sin(t),H=1+16/45*Math.cos(2*t)-4/225*Math.cos(4*t),D=-32/45*Math.sin(2*t)+16/225*Math.sin(4*t);let P=[H*c-D*s,0,0],n=Math.max(1,Math.ceil(Math.abs(t)/(.25*pi)));for(let i=0;i<n;i++)for(let j=0;j<g.length;j++){let v=(i+g[j])*t/n,s=Math.sin(v),c=Math.cos(v),r=.2+32/15*s**4,om=h*Math.cos(2*v),b=w[j]*t/n*r*c;P[1]+=b*Math.cos(om);P[2]+=b*Math.sin(om);}if(centerCache.size<30000)centerCache.set(t,P);return P;}
 function ring(s,u){u=(u%TWO+TWO)%TWO;let l=-1,r=TWO+1,t=u;for(let i=0;i<42;i++){let q=local(t),f=q.U+s*q.a-u;if(Math.abs(f)<5e-15)break;if(f>0)r=t;else l=t;let v=t-f/(q.r*(1+s*q.ad));t=v>l&&v<r?v:(l+r)/2;}let q=local(t),J=1+s*q.ad,n=q.K/J,m=-q.a*n,ll=q.a*q.a*n,gamma=xy(t),P=gamma.map((v,k)=>v+s*(q.B[k]+q.a*q.V[k]));return {...q,t,J,n,m,ll,P,jet:[P,q.B,q.V,q.N.map(v=>v*ll),q.N.map(v=>v*m),q.N.map(v=>v*n)]};}
 return {local,xy,ring};}
function twistedCauchySource(z,N,nstep,stop,snap){const g=twistedStrip(),left=u=>g.ring(13/128,u);return orientedCauchy(z,N,nstep,stop,true,1,snap,left);}

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
}
function twistReference(z,p){const s0=13/128,flat=twistedStrip(),base=packetControlled(z,p),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]],cache=new Map();return (t,u)=>{if(t>=.6)return base.jet([],t,u);let chi=t/.6,c=chi**3*(10+chi*(-15+6*chi)),ct=30*(chi*(1-chi))**2/.6,ctt=60*chi*(1-chi)*(1-2*chi)/.36,th=Math.tanh(1.2*t/.036),s=s0+.036*th,st=1.2*(1-th*th),stt=-2*1.2**2*th*(1-th*th)/.036;
 const R=flat.ring(s,u).jet,X=[R[0],R[1].map(v=>v*st),R[2],R[3].map((v,k)=>v*st**2+R[1][k]*stt),R[4].map(v=>v*st),R[5]],Y=base.jet([],t,u),W=Y.map((v,i)=>v.map((q,k)=>q-X[i][k])),out=X.map((v,i)=>v.map((q,k)=>q+c*W[i][k]));for(let k=0;k<3;k++){out[1][k]+=ct*W[0][k];out[3][k]+=ctt*W[0][k]+2*ct*W[1][k];out[4][k]+=ct*W[2][k];}return out;};}
function buildTwistField(z,p,sol,M,finish=.70){const ref=twistReference(z,p),raw=compactMixedJets(z),N=sol.N,times=sol.rec.map(q=>q.t),controls=[],K=2*M+1;
 if(!Number.isFinite(sol.rec.at(-1).minimumN)||times.at(-1)<sol.stop-1e-9)throw Error('incomplete source');
 const A=Array.from({length:N},(_,j)=>Array.from({length:K},(_,i)=>i===0?1/N:2*(i%2?Math.cos((i+1)/2*2*Math.PI*j/N):Math.sin(i/2*2*Math.PI*j/N))/N));
 for(let I=0;I<times.length;I++){let t=times[I],row=Array.from({length:3},()=>new Float64Array(3*K)),Q=0,Qd=0;for(let k=0;k<64;k++){let q=raw(t,Math.PI*k/32);Q+=dot(q[1],q[1])/64;Qd+=2*dot(q[1],q[3])/64;}if(I>0){let data=sol.snapshot[I],e=Math.sqrt(Q),ed=Qd/(2*e),gauss=sol.rec[I].K;for(let j=0;j<N;j++){let o=14*j,Y=ref(t,2*Math.PI*j/N),l=(gauss+data[o+1]**2)/data[o];for(let c=0;c<3;c++){let d0=data[o+11+c]-Y[0][c],d1=e*data[o+2+c]-Y[1][c],d2=ed*data[o+2+c]+Q*l*data[o+8+c]-Y[3][c];for(let k=0;k<K;k++){let v=A[j][k],i=c*K+k;row[0][i]+=v*d0;row[1][i]+=v*d1;row[2][i]+=v*d2;}}}}
 controls.push(row.map(v=>Array.from(v)));}times.push(finish);controls.push(Array.from({length:3},()=>Array(3*K).fill(0)));return {M,times,controls,stop:sol.stop,finish};}
function twistComplete(z,p,f){const ref=twistReference(z,p),{times,controls,M,finish}=f,K=2*M+1,cache=new Map(),angles=new Map(),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];return {jet(_,t,u){const X=ref(t,u);if(t>=finish)return X;let V=cache.get(t);if(!V){let i=0;while(times[i+1]<t)i++;let a=controls[i],b=controls[i+1],L=times[i+1]-times[i],s=(t-times[i])/L;V=Array.from({length:3},(_,d)=>Array.from({length:3*K},(_,k)=>rayHermite(a.map(q=>q[k]),b.map(q=>q[k]),L,s,d)));if(cache.size<3000)cache.set(t,V);}let tr=angles.get(u);if(!tr){tr=Array.from({length:K},(_,j)=>{if(!j)return [1,0,0];let m=(j+1)>>1,c=Math.cos(m*u),s=Math.sin(m*u);return j%2?[c,-m*s,-m*m*c]:[s,m*c,-m*m*s];});if(angles.size<5000)angles.set(u,tr);}for(let i=0;i<6;i++)for(let c=0;c<3;c++){let q=0;for(let k=0;k<K;k++)q+=V[orders[i][0]][c*K+k]*tr[k][orders[i][1]];X[i][c]+=q;}return X;}};}

function ownGrid(isIndependent){
 const ns=isIndependent?60:95,degree=isIndependent?11:10,[g,w]=gauss01(degree);
 let arr=[];for(let i=0;i<ns;i++)for(let j=0;j<degree;j++)arr.push([(i+g[j])/(ns+1),w[j]/(ns+1)]);
 const [last,ww]=gauss01(8);for(let j=0;j<8;j++)arr.push([(ns+last[j])/(ns+1),ww[j]/(ns+1)]);
 arr.sort((a,b)=>a[0]-b[0]);return arr;}

function observeTwist(cl,p,z,group,lam=1.06){const ntarget=64,targetZ=z;configure(8,8);
 const ind=group==='G11',N=ind?256:group==='G10a'?128:192,angled=ind?.417:0;
 const pts=ownGrid(ind),target=build(pts.length,ntarget,pts.map(v=>v[0]),0);
 let prefixPeak=0,prefixKap=0,prefixAt=[],components=[0,0,0],peak=0,kap=0,held=Infinity,wd=0,bound=0,zhi=0,zlo=Infinity,minArea=Infinity,L=0,lowerQ=Infinity,lowerS=Infinity,mg=Array(7).fill(0),vmax=[0,0,0,0],sqv=[0,0,0,0],mworst,kworst;
 for(let i=0;i<pts.length;i++){let [t,w]=pts[i];const [Q,S0]=gramTarget(jets(target,target.rows[i],targetZ),ntarget),S=S0,Y=new Float64Array(N*18);
  for(let n=0;n<N;n++)Y.set(cl.jet(p,t,2*pi*(n+angled)/N).flat(),18*n);
  L+=w*lam*Math.sqrt(Q);lowerQ=Math.min(lowerQ,Q);lowerS=Math.min(lowerS,S);
  for(let n=0;n<N;n++){const p=18*n,v=(j)=>[Y[p+j],Y[p+j+1],Y[p+j+2]],P=v(0).map(x=>x*lam),V=v(3),U=v(6),A=v(9),B=v(12),C=v(15),E=dot(V,V),F=dot(V,U),G=dot(U,U),base=cross(V,U),ds=norm(base),nor=base.map(a=>a/ds),ar=ds/Math.sqrt(Q*S),ln=dot(A,nor),mn=dot(B,nor),nn=dot(C,nor),H=(G*ln-2*F*mn+E*nn)/(2*ds*ds),K=(ln*nn-mn*mn)/(ds*ds),rd=Math.sqrt(Math.max(0,H*H-K));
   const ka=(H+rd)/lam,kb=(H-rd)/lam,absK=Math.max(Math.abs(ka),Math.abs(kb)),e=E/Q-1,f=F/Math.sqrt(Q*S),g=G/S-1,me=Math.abs((e+g)/2)+Math.hypot((e-g)/2,f),u=2*pi*(n+angled)/N;
   components=[Math.max(components[0],Math.abs(e)),Math.max(components[1],Math.abs(f)),Math.max(components[2],Math.abs(g))];
   if(t<=.20){if(me>prefixPeak){prefixPeak=me;prefixAt=[t,u];}prefixKap=Math.max(prefixKap,absK);}
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

export {twistedStrip,twistedCauchySource,rigorousSpaceTwist,buildTwistField,twistComplete,observeTwist};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,p540,output]=process.argv.slice(2),read=x=>JSON.parse(readFileSync(x));
 if(op==='strict')console.log(JSON.stringify(rigorousSpaceTwist(),null,2));
 else if(op==='ports'){let f=twistedStrip();console.log(JSON.stringify([0,Math.PI/2,Math.PI,3*Math.PI/2].map(u=>f.ring(13/128,u)),null,2));}
 else if(op==='make256'||op==='make512'){const N=Number(op.slice(4)),z=read(state),p=read(p540),s=twistedCauchySource(z,N,N===256?600:1200,.20,40),d=buildTwistField(z,p,s,N===256?80:152,.70);writeFileSync(output,JSON.stringify(d)+'\n');console.log(JSON.stringify(s.rec));}
 else if(op==='observe'){let z=read(state),p=read(p540),m=twistComplete(z,p,read(output));console.log(JSON.stringify(['G10a','G10b','G11'].map(g=>observeTwist(m,[],z,g)),null,2));}
 else throw Error('strict | ports | make256/make512/observe STATE192 STATE540 TWISTFIELD');
}
