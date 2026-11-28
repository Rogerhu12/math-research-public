#!/usr/bin/env node
/** A true normal graph on the certified-image material chart, with meridian length in the design. */
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {configure,build,jets,gramTarget} from './2ecf-compact-p32-direct-field.mjs';
import {compactClock} from './2ecf-compact-p32-two-material-clocks.mjs';
const pi=Math.PI,endZ=.54,dot=(v,w)=>v[0]*w[0]+v[1]*w[1]+v[2]*w[2],norm=v=>Math.sqrt(dot(v,v)),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
function compactPhysicalThird(z){
 const pi=Math.PI,nt=8,nm=8,K=15,c=[0],h=[0];let ratio=1;
 if(z.length!==192)throw Error('Expected the actual 192-space field');
 for(let j=1;j<=32;j++){ratio*= (33-j)/(32+j);c.push(1.5*(j%2?-1:1)*ratio);h.push(c[j]/(1-4*j*j));}
 function polar(th,want){const a=Math.cos(2*th),b=Math.sin(2*th);let co=1,si=0,U=th,r=1,H=1,Hp=0,rp=0;for(let j=1;j<=32;j++){
   const nco=co*a-si*b;si=si*a+co*b;co=nco;U+=c[j]*si/(2*j);r+=c[j]*co;if(want){H+=h[j]*co;Hp-=2*j*h[j]*si;rp-=2*j*c[j]*si;}}
   return [U,r,H,Hp,rp];}
 function central(u){const tp=2*pi;u=(u%tp+tp)%tp;const q=Math.min(3,Math.floor(u/(pi/2))),sx=(q===1||q===2)?-1:1,sy=q>=2?-1:1;
  const ua=q===0?u:q===1?pi-u:q===2?u-pi:tp-u;
  let low=0,high=pi/2,x=Math.max(0,Math.min(pi/2,ua*3.4));for(let n=0;n<17;n++){let [U,r]=polar(x,false),err=U-ua;if(Math.abs(err)<4e-16)break;if(err>0)high=x;else low=x;let y=x-err/r;if(!(y>low&&y<high))y=(low+high)/2;if(Math.abs(y-x)<2e-16)break;x=y;}
  let [U,r,H,Hp,rp]=polar(x,true);if(Math.abs(U-ua)>5e-13){for(let n=0;n<40;n++){x=(low+high)/2;[U,r,H,Hp,rp]=polar(x,true);if(U>ua)high=x;else low=x;}}
  let co=Math.cos(x),si=Math.sin(x),sg=q%2?-1:1;
  return [[sx*(H*co-Hp*si),sy*(H*si+Hp*co)],[sx*sg*(-si),sy*sg*co],[-sx*co/r,-sy*si/r],[sx*sg*(si/r**2+co*rp/r**3),sy*sg*(-co/r**2+si*rp/r**3)]];
 }
 function bern(t){let b=[[1]];for(let n=1;n<=5;n++){let a=b.at(-1),next=[];for(let i=0;i<=n;i++)next.push((1-t)*(a[i]||0)+t*(a[i-1]||0));b.push(next);}
  return [b[5],Array.from({length:6},(_,i)=>5*((b[4][i-1]||0)-(b[4][i]||0))),Array.from({length:6},(_,i)=>20*((b[3][i-2]||0)-2*(b[3][i-1]||0)+(b[3][i]||0))),Array.from({length:6},(_,i)=>60*((b[2][i-3]||0)-3*(b[2][i-2]||0)+3*(b[2][i-1]||0)-(b[2][i]||0)))];}
 const vleft=[1,1,1,0,0,0],vright=[0,0,0,.83,.59,.35],vz=[13/128,13/128+.24,13/128+.48,.54,.54,.54];
 const ip=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),ord=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2],[3,0],[2,1],[1,2],[0,3]];
 return function(t,u){
  const C=central(u),B=bern(t),left=B.map(x=>ip(x,vleft)),right=B.map(x=>ip(x,vright)),height=B.map(x=>ip(x,vz)),co=Math.cos(u),si=Math.sin(u),es=[[co,si],[-si,co],[-co,-si],[si,-co]],w=2*t-1,p=t*(1-t),q=1-2*t,a=64*p**3,ap=192*p*p*q,app=384*p*q*q-384*p*p;
  const T=[1,w],D=[0,2],DD=[0,0],DDD=[0,0];for(let k=2;k<nt;k++){T.push(2*w*T[k-1]-T[k-2]);D.push(4*T[k-1]+2*w*D[k-1]-D[k-2]);DD.push(8*D[k-1]+2*w*DD[k-1]-DD[k-2]);DDD.push(12*DD[k-1]+2*w*DDD[k-1]-DDD[k-2]);}
  const R=[T.map(x=>a*x),T.map((x,i)=>ap*x+a*D[i]),T.map((x,i)=>app*x+2*ap*D[i]+a*DD[i]),T.map((x,i)=>384*(q**3-6*p*q)*x+3*app*D[i]+3*ap*DD[i]+a*DDD[i])],cos=[1],sin=[0];for(let m=1;m<=K;m++){cos.push(cos[m-1]*co-sin[m-1]*si);sin.push(sin[m-1]*co+cos[m-1]*si);}
  const Y=Array.from({length:10},(_,i)=>{let [dr,du]=ord[i];return [0,1,2].map(k=>k===2?(du===0?height[dr]:0):left[dr]*C[du][k]+right[dr]*es[du][k]);});
  for(let k=0;k<3;k++)for(let j=0;j<nm;j++){let m=k===2?2*j:2*j+1,ss=k===1,co0=ss?sin[m]:cos[m],co1=m*(ss?cos[m]:-sin[m]),co2=-m*m*co0,b0=0,b1=0,b2=0,b3=0;
   for(let i=0;i<nt;i++){let y=z[(i*3+k)*nm+j];b0+=R[0][i]*y;b1+=R[1][i]*y;b2+=R[2][i]*y;b3+=R[3][i]*y;}
   Y[0][k]+=b0*co0;Y[1][k]+=b1*co0;Y[2][k]+=b0*co1;Y[3][k]+=b2*co0;Y[4][k]+=b1*co1;Y[5][k]+=b0*co2;Y[6][k]+=b3*co0;Y[7][k]+=b2*co1;Y[8][k]+=b1*co2;Y[9][k]-=b0*m*m*co1;}
  return Y;
 };
}

const centralA=compactPhysicalThird(Array(192).fill(0))(0,0)[0][0];
function gauss01(n){
 const t=[],w=[];
 for(let j=0;j<n;j++){let z=Math.cos(pi*(j+.75)/(n+.5)),p,p1,dp;
  for(let k=0;k<15;k++){p1=1;p=z;for(let a=2;a<=n;a++){let q=((2*a-1)*z*p-(a-1)*p1)/a;p1=p;p=q;}
   dp=n*(z*p-p1)/(z*z-1);let dz=p/dp;z-=dz;if(Math.abs(dz)<3e-16)break;}
  t.push((1-z)/2);w.push(1/((1-z*z)*dp*dp));
 }return [t,w];}
function ownGrid(isIndependent){
 const ns=isIndependent?60:95,degree=isIndependent?11:10,[g,w]=gauss01(degree);
 let arr=[];for(let i=0;i<ns;i++)for(let j=0;j<degree;j++)arr.push([(i+g[j])/(ns+1),w[j]/(ns+1)]);
 const [last,ww]=gauss01(8);for(let j=0;j<8;j++)arr.push([(ns+last[j])/(ns+1),ww[j]/(ns+1)]);
 arr.sort((a,b)=>a[0]-b[0]);return arr;}

function compactNormalModel(z,clock,nr=12,nm=7){
 const ref=compactClock(10,5,z),field=compactPhysicalThird(z),pi=Math.PI,lambda=1.06,h=1/(nr+3),dim=nr*nm,centralA=field(0,0)[0][0];
 const dot=(x,y)=>x[0]*y[0]+x[1]*y[1]+x[2]*y[2],norm=x=>Math.sqrt(dot(x,x)),cross=(x,y)=>[x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]],vec=(w,a,x,b)=>w.map((s,k)=>s*a+x[k]*b),add3=(w,x,y)=>w.map((s,k)=>s+x[k]+y[k]);
 function base(t,u){
  const [T,U]=ref.coord(t,u,ref.basis(t,u),clock),Y=field(T[0],U[0]),[P,v,w,A,B,C,D,Et,F,G]=Y,n0=cross(v,w),r=norm(n0),N=n0.map(x=>x/r),
    Zt=vec(cross(A,w),1,cross(v,B),1),Zu=vec(cross(B,w),1,cross(v,C),1),Rt=dot(N,Zt),Ru=dot(N,Zu),Nt=vec(Zt,1/r,N,-Rt/r),Nu=vec(Zu,1/r,N,-Ru/r);
  function d2(z,a,b,na,nb,y){let d=dot(nb,y)+dot(N,z);return z.map((v,k)=>(v-a*nb[k]-b*na[k]-d*N[k])/r);}
  const Ntt=d2(add3(cross(D,w),vec(cross(A,B),2,N,0),cross(v,Et)),Rt,Rt,Nt,Nt,Zt),
   Ntu=d2(add3(cross(Et,w),cross(A,C),cross(v,F)),Rt,Ru,Nt,Nu,Zt),
   Nuu=d2(add3(cross(F,w),vec(cross(B,C),2,N,0),cross(v,G)),Ru,Ru,Nu,Nu,Zu);
  function pull(y){let [p,v,w,A,B,C]=y;const first=i=>vec(v,T[i],w,U[i]),second=(i,j,d)=>v.map((x,k)=>x*T[d]+w[k]*U[d]+A[k]*T[i]*T[j]+B[k]*(T[i]*U[j]+T[j]*U[i])+C[k]*U[i]*U[j]);return [p,first(1),first(2),second(1,1,3),second(1,2,4),second(2,2,5)];}
  return [pull(Y),pull([N,Nt,Nu,Ntt,Ntu,Nuu])];}
 function basis(t,u){const b=[];for(let j=Math.max(0,Math.floor(t/h)-3);j<Math.min(nr,Math.floor(t/h)+1);j++){let x=t/h-j-2,a=Math.abs(x),sg=Math.sign(x),p,d,dd;
  if(a>=2)continue;if(a>1){p=(2-a)**3/6;d=-sg*(2-a)**2/2;dd=2-a;}else{p=2/3-a*a+a**3/2;d=sg*(-2*a+1.5*a*a);dd=-2+3*a;}d/=h;dd/=h*h;
  for(let k=0;k<nm;k++){let m=2*k,c=Math.cos(m*u),s=-m*Math.sin(m*u);b.push([j*nm+k,p*c,d*c,p*s,dd*c,d*s,-m*m*p*c]);}}return b;}
 const gather=(b,p)=>{let q=[0,0,0,0,0,0];for(let a of b)for(let k=0;k<6;k++)q[k]+=a[k+1]*p[a[0]];return q;};
 const product=(q,n)=>[n[0].map(v=>q[0]*v),vec(n[1],q[0],n[0],q[1]),vec(n[2],q[0],n[0],q[2]),n[0].map((s,k)=>s*q[3]+2*n[1][k]*q[1]+n[3][k]*q[0]),n[0].map((s,k)=>s*q[4]+n[1][k]*q[2]+n[2][k]*q[1]+n[4][k]*q[0]),n[0].map((s,k)=>s*q[5]+2*n[2][k]*q[2]+n[5][k]*q[0])];
 function jet(p,t,u){let [Y,N]=base(t,u),q=gather(basis(t,u),p),v=product(q,N);return v.map((a,i)=>a.map((x,k)=>x+Y[i][k]));}
 function prepare(R,N){let pts=[],goals=[];for(let i=0;i<R;i++){let t=i/(R-1),g=ref.goal(t),wt=(i===0||i===R-1?.5:1)/(R-1);goals.push(wt*Math.sqrt(g[0]));
  for(let j=0;j<N;j++){let u=j*pi/(2*N-2);pts.push({t,u,j,wt,g,base:base(t,u),b:basis(t,u)});}}
  return {pts,R,N,L:goals.reduce((a,b)=>a+b,0)};}
 function evaluate(data,p,opts,want=true){const {pts,N,R,L}=data,grad=new Float64Array(dim),len=new Float64Array(N),jac=want?Array.from({length:N},()=>new Float64Array(dim)):[],sharp=opts.sharp??100,cw=opts.curv??2,gw=opts.guide??3500,mw=opts.meridian??20,k0=9.5;let cost=0,peak=0,kap=0,held=Infinity,wmax=0,maxH=0,minArea=Infinity;
  for(let pt of pts){const {g,wt,j,b}=pt,[Y,n]=pt.base,q=gather(b,p),v=product(q,n),X=v.map((a,i)=>a.map((x,k)=>x+Y[i][k])),[P,V,U,A,B,C]=X,normal=cross(V,U),d=norm(normal),E=dot(V,V),F=dot(V,U),G=dot(U,U),Q=g[0],S=g[1],qs=Math.sqrt(Q*S),e=E/Q-1,f=F/qs,y=G/S-1,ar=d/qs,scale=wt/N;maxH=Math.max(maxH,Math.abs(q[0]));let cur=0;
   if(d<1e-8)return {cost:Infinity,grad};peak=Math.max(peak,Math.abs((e+y)/2)+Math.hypot((e-y)/2,f));minArea=Math.min(minArea,ar);const nn=normal.map(x=>x/d),l=dot(A,nn),m=dot(B,nn),nc=dot(C,nn),H=(G*l-2*F*m+E*nc)/(2*d*d),K=(l*nc-m*m)/(d*d),rad=Math.sqrt(Math.max(0,H*H-K)),sm=e*e+2*f*f+y*y;
   cur+=sm*(1+sharp*sm);const ds=2*(1+2*sharp*sm);let dE=ds*e/Q,dF=2*ds*f/qs,dG=ds*y/S,bar=Array.from({length:6},()=>[0,0,0]);
   if(ar<.5){let v=.5-ar;cur+=10*v*v;let s=-10*v*ar;dE+=s*G/(d*d);dF-=2*s*F/(d*d);dG+=s*E/(d*d);}
   for(let k of [H+rad,H-rad]){let ak=Math.abs(k)/lambda;kap=Math.max(kap,ak);if(ak<=k0)continue;let v=ak/k0-1;cur+=cw*v*v*(1+v*v);if(!want)continue;
    let w=cw*2*v*(1+2*v*v)*Math.sign(k)/(lambda*k0),a=m-k*F,b=k*E-l,cc=nc-k*G,dd=k*F-m;if(cc*cc+dd*dd>a*a+b*b){a=cc;b=dd;}let size=Math.sqrt(E*a*a+2*F*a*b+G*b*b);if(size<1e-13)continue;a/=size;b/=size;
    const aa=w*a*a,ab=2*w*a*b,bb=w*b*b;dE-=k*aa;dF-=k*ab;dG-=k*bb;let bn=A.map((x,i)=>aa*x+ab*B[i]+bb*C[i]),proj=dot(bn,nn);bn=bn.map((s,i)=>(s-proj*nn[i])/d);const dv=cross(U,bn),du=cross(bn,V);
    for(let i=0;i<3;i++){bar[1][i]+=dv[i];bar[2][i]+=du[i];bar[3][i]+=aa*nn[i];bar[4][i]+=ab*nn[i];bar[5][i]+=bb*nn[i];}}
   if(want){for(let i=0;i<3;i++){bar[1][i]+=2*dE*V[i]+dF*U[i];bar[2][i]+=dF*V[i]+2*dG*U[i];}}
   const PP=P.map(x=>x*lambda),rr=norm(PP),rp=Math.hypot(PP[0],PP[1]-lambda*centralA,PP[2]),rm=Math.hypot(PP[0],PP[1]+lambda*centralA,PP[2]),rc=Math.hypot(PP[0],PP[1]),lb=Math.max(0,Math.min(1,(rc-.52)/.02)),allow=.0195*lb**3*(10+lb*(-15+6*lb)),dar=.0195*30*(lb*(1-lb))**2/.02;
   held=Math.min(held,rp,rm);wmax=Math.max(wmax,Math.abs(PP[1]));const geo=[rr-1.59,PP[1]-.885,-PP[1]-.885,PP[2]-lambda*.54-allow,-PP[2]-lambda*.54-allow,.65-rp,.65-rm];
   for(let j=0;j<7;j++){if(geo[j]<=0)continue;cur+=gw*geo[j]**2;if(!want)continue;const gg=j===0?PP.map(x=>x/rr):j===1?[0,1,0]:j===2?[0,-1,0]:j===3||j===4?[-dar*PP[0]/rc,-dar*PP[1]/rc,j===3?1:-1]:[-PP[0]/(j===5?rp:rm),-(PP[1]+(j===5?-1:1)*lambda*centralA)/(j===5?rp:rm),-PP[2]/(j===5?rp:rm)];for(let k=0;k<3;k++)bar[0][k]+=2*lambda*gw*geo[j]*gg[k];}
   cost+=scale*cur;const sp=Math.sqrt(E);len[j]+=wt*sp;if(!want)continue;
   let w=Array(6).fill(0);for(let k=0;k<6;k++)w[0]+=dot(bar[k],n[k]);w[1]=dot(bar[1],n[0])+2*dot(bar[3],n[1])+dot(bar[4],n[2]);w[2]=dot(bar[2],n[0])+dot(bar[4],n[1])+2*dot(bar[5],n[2]);w[3]=dot(bar[3],n[0]);w[4]=dot(bar[4],n[0]);w[5]=dot(bar[5],n[0]);const dl=dot(V,n[1])/sp,dl1=dot(V,n[0])/sp;
   for(let v of b){let s=0;for(let k=0;k<6;k++)s+=w[k]*v[k+1];grad[v[0]]+=scale*s;jac[j][v[0]]+=wt*(v[1]*dl+v[2]*dl1);}
  }
  let deficits=[];for(let j=0;j<N;j++){let e=len[j]/L-1;deficits.push(e);cost+=mw*e*e/N;if(want)for(let k=0;k<dim;k++)grad[k]+=2*mw*e*jac[j][k]/(L*N);}
  return {cost,grad,metric:peak,curvature:kap,held,width:wmax,maximumNormal:maxH,minArea,meridianDeficit:Math.min(...deficits),shortAxisRatio:len[N-1]/L};
 }
 return {dim,basis,base,jet,prepare,evaluate};
}
function fitNormal(model,data,x,opts,steps){
 const dot=(v,w)=>v.reduce((s,x,i)=>s+x*w[i],0),dim=model.dim,mem=[],hist=[];let r=model.evaluate(data,x,opts),accepted=0;
 for(let it=0;it<steps;it++){let d=Array.from(r.grad),a=[];for(let k=mem.length-1;k>=0;k--){const [s,y,h]=mem[k],v=dot(s,d)/h;a[k]=v;for(let j=0;j<dim;j++)d[j]-=v*y[j];}let w=mem.length?mem.at(-1)[2]/dot(mem.at(-1)[1],mem.at(-1)[1]):.004;d=d.map(v=>v*w);
  for(let k=0;k<mem.length;k++){const [s,y,h]=mem[k],v=dot(y,d)/h;for(let j=0;j<dim;j++)d[j]+=s[j]*(a[k]-v);}let des=dot(d,r.grad);if(des<=0){d=Array.from(r.grad);des=dot(d,d);mem.length=0;}let step=1,nx,nr,ok=false;
  for(let k=0;k<21;k++){nx=x.map((v,j)=>v-step*d[j]);nr=model.evaluate(data,nx,opts,false);if(nr.cost<r.cost-1e-4*step*des){ok=true;break;}step*=.5;}if(!ok)break;nr=model.evaluate(data,nx,opts);let s=nx.map((v,j)=>v-x[j]),y=Array.from(nr.grad,(v,j)=>v-r.grad[j]),sy=dot(s,y);if(sy>1e-18){mem.push([s,y,sy]);if(mem.length>12)mem.shift();}r=nr;x=nx;accepted++;
  if(accepted%10===0)hist.push([accepted,r.cost,r.metric,r.curvature,r.shortAxisRatio]);}
 const {grad,...final}=r;return {x,accepted,hist,final};
}
function observeNormal(cl,p,z,group,lam=1.06){const ntarget=64,targetZ=z;configure(8,8);
 const ind=group==='G11',N=ind?256:group==='G10a'?128:192,angled=ind?.417:0;
 const pts=ownGrid(ind),target=build(pts.length,ntarget,pts.map(v=>v[0]),0);
 let components=[0,0,0],peak=0,kap=0,held=Infinity,wd=0,bound=0,zhi=0,zlo=Infinity,minArea=Infinity,L=0,lowerQ=Infinity,lowerS=Infinity,mg=Array(7).fill(0),vmax=[0,0,0,0],sqv=[0,0,0,0],mworst,kworst;
 for(let i=0;i<pts.length;i++){let [t,w]=pts[i];const [Q,S]=gramTarget(jets(target,target.rows[i],targetZ),ntarget),Y=new Float64Array(N*18);
  for(let n=0;n<N;n++)Y.set(cl.jet(p,t,2*pi*(n+angled)/N).flat(),18*n);
  L+=w*lam*Math.sqrt(Q);lowerQ=Math.min(lowerQ,Q);lowerS=Math.min(lowerS,S);
  for(let n=0;n<N;n++){const p=18*n,v=(j)=>[Y[p+j],Y[p+j+1],Y[p+j+2]],P=v(0).map(x=>x*lam),V=v(3),U=v(6),A=v(9),B=v(12),C=v(15),E=dot(V,V),F=dot(V,U),G=dot(U,U),base=cross(V,U),ds=norm(base),nor=base.map(a=>a/ds),ar=ds/Math.sqrt(Q*S),ln=dot(A,nor),mn=dot(B,nor),nn=dot(C,nor),H=(G*ln-2*F*mn+E*nn)/(2*ds*ds),K=(ln*nn-mn*mn)/(ds*ds),rd=Math.sqrt(Math.max(0,H*H-K));
   const ka=(H+rd)/lam,kb=(H-rd)/lam,absK=Math.max(Math.abs(ka),Math.abs(kb)),e=E/Q-1,f=F/Math.sqrt(Q*S),g=G/S-1,me=Math.abs((e+g)/2)+Math.hypot((e-g)/2,f),u=2*pi*(n+angled)/N;
   components=[Math.max(components[0],Math.abs(e)),Math.max(components[1],Math.abs(f)),Math.max(components[2],Math.abs(g))];
   if(me>peak){peak=me;mworst=[t,u];}if(absK>kap){kap=absK;kworst=[t,u];}
   const r=norm(P),rp=Math.hypot(P[0],P[1]-lam*centralA,P[2]),rm=Math.hypot(P[0],P[1]+lam*centralA,P[2]),rc=Math.hypot(P[0],P[1]),q=Math.max(0,Math.min(1,(rc-.52)/.02)),a=.0195*q**3*(10+q*(-15+6*q));
   held=Math.min(held,rp,rm);bound=Math.max(bound,r);wd=Math.max(wd,Math.abs(P[1]));zhi=Math.max(zhi,P[2]);zlo=Math.min(zlo,P[2]);minArea=Math.min(minArea,ar);
   let geo=[r-1.59,P[1]-.885,-P[1]-.885,P[2]-lam*endZ-a,-P[2]-lam*endZ-a,.65-rp,.65-rm].map(x=>Math.max(0,x));for(let j=0;j<7;j++)mg[j]=Math.max(mg[j],geo[j]);
   let metric2=e*e+2*f*f+g*g,cv=[ka,kb].map(k=>Math.max(0,Math.abs(k)-9.5));let msum=metric2*(1+metric2/.12**2),kn=cv.reduce((v,c)=>v+c*c,0),ksum=kn*(1+kn/4),gsum=geo.reduce((v,a)=>v+a*a,0),aa=Math.max(0,(.5/ar)**2-1)**2;
   let wt=w*lam*Math.sqrt(Q)/N;for(let j=0;j<4;j++){let v=[msum,ksum,gsum,aa][j];sqv[j]+=wt*v;vmax[j]=Math.max(vmax[j],v);}
  }
 }
 return {components,group,radial:pts.length,angles:N,trueRowCount:14*pts.length*N,metric:peak,curvature:kap,held,halfWidth:wd,ballRadius:bound,upperZ:[zlo,zhi],minimumAreaRatio:minArea,physicalTransitionLength:L,finiteMinTargetSquared:[lowerQ,lowerS],metricWitness:mworst,curvatureWitness:kworst,guideMax:mg,groupSquaredNorms:sqv,groupMaxSquared:vmax};
}

export {compactPhysicalThird,compactNormalModel,fitNormal,observeNormal,gauss01};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,clock,out]=process.argv.slice(2),z=JSON.parse(readFileSync(state)),w=JSON.parse(readFileSync(clock)),obj=compactNormalModel(z,w,12,7);
 if(op==='fit'){const opts={sharp:175,curv:2.5,guide:650,meridian:85},data=obj.prepare(42,25),r=fitNormal(obj,data,Array(obj.dim).fill(0),opts,90);writeFileSync(out,JSON.stringify(r.x)+'\n');console.log(JSON.stringify({accepted:r.accepted,training:r.final}));}
 else if(op==='observe'){const p=JSON.parse(readFileSync(out));console.log(JSON.stringify(['G10a','G10b','G11'].map(q=>observeNormal(obj,p,z,q)),null,2));}
 else throw Error('fit STATE192 CLOCK100 OUT84 | observe STATE192 CLOCK100 STATE84');
}
