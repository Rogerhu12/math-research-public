#!/usr/bin/env node
/** Both material coordinates can move. The physical p32 surface and target stay fixed. */
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {configure,build,jets,gramTarget} from './2ecf-compact-p32-direct-field.mjs';
const pi=Math.PI,endZ=.54,dot=(v,w)=>v[0]*w[0]+v[1]*w[1]+v[2]*w[2],norm=v=>Math.sqrt(dot(v,v)),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
function compactPhysical(z){
 const pi=Math.PI,nt=8,nm=8,K=15,c=[0],h=[0];let ratio=1;
 if(z.length!==192)throw Error('Expected the actual 192-space field');
 for(let j=1;j<=32;j++){ratio*= (33-j)/(32+j);c.push(1.5*(j%2?-1:1)*ratio);h.push(c[j]/(1-4*j*j));}
 function polar(th,want){const a=Math.cos(2*th),b=Math.sin(2*th);let co=1,si=0,U=th,r=1,H=1,Hp=0;for(let j=1;j<=32;j++){
   const nco=co*a-si*b;si=si*a+co*b;co=nco;U+=c[j]*si/(2*j);r+=c[j]*co;if(want){H+=h[j]*co;Hp-=2*j*h[j]*si;}}
   return [U,r,H,Hp];}
 function central(u){const tp=2*pi;u=(u%tp+tp)%tp;const q=Math.min(3,Math.floor(u/(pi/2))),sx=(q===1||q===2)?-1:1,sy=q>=2?-1:1;
  const ua=q===0?u:q===1?pi-u:q===2?u-pi:tp-u;
  let low=0,high=pi/2,x=Math.max(0,Math.min(pi/2,ua*3.4));for(let n=0;n<17;n++){let [U,r]=polar(x,false),err=U-ua;if(Math.abs(err)<4e-16)break;if(err>0)high=x;else low=x;let y=x-err/r;if(!(y>low&&y<high))y=(low+high)/2;if(Math.abs(y-x)<2e-16)break;x=y;}
  let [U,r,H,Hp]=polar(x,true);if(Math.abs(U-ua)>5e-13){for(let n=0;n<40;n++){x=(low+high)/2;[U,r,H,Hp]=polar(x,true);if(U>ua)high=x;else low=x;}}
  let co=Math.cos(x),si=Math.sin(x),sg=q%2?-1:1;
  return [[sx*(H*co-Hp*si),sy*(H*si+Hp*co)],[sx*sg*(-si),sy*sg*co],[-sx*co/r,-sy*si/r]];
 }
 function bern(t){let b=[[1]];for(let n=1;n<=5;n++){let a=b.at(-1),next=[];for(let i=0;i<=n;i++)next.push((1-t)*(a[i]||0)+t*(a[i-1]||0));b.push(next);}
  return [b[5],Array.from({length:6},(_,i)=>5*((b[4][i-1]||0)-(b[4][i]||0))),Array.from({length:6},(_,i)=>20*((b[3][i-2]||0)-2*(b[3][i-1]||0)+(b[3][i]||0)))];}
 const vleft=[1,1,1,0,0,0],vright=[0,0,0,.83,.59,.35],vz=[13/128,13/128+.24,13/128+.48,.54,.54,.54];
 const ip=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),ord=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];
 return function(t,u){
  const C=central(u),B=bern(t),left=B.map(x=>ip(x,vleft)),right=B.map(x=>ip(x,vright)),height=B.map(x=>ip(x,vz)),co=Math.cos(u),si=Math.sin(u),es=[[co,si],[-si,co],[-co,-si]],w=2*t-1,p=t*(1-t),q=1-2*t,a=64*p**3,ap=192*p*p*q,app=384*p*q*q-384*p*p;
  const T=[1,w],D=[0,2],DD=[0,0];for(let k=2;k<nt;k++){T.push(2*w*T[k-1]-T[k-2]);D.push(4*T[k-1]+2*w*D[k-1]-D[k-2]);DD.push(8*D[k-1]+2*w*DD[k-1]-DD[k-2]);}
  const R=[T.map(x=>a*x),T.map((x,i)=>ap*x+a*D[i]),T.map((x,i)=>app*x+2*ap*D[i]+a*DD[i])],cos=[1],sin=[0];for(let m=1;m<=K;m++){cos.push(cos[m-1]*co-sin[m-1]*si);sin.push(sin[m-1]*co+cos[m-1]*si);}
  const Y=Array.from({length:6},(_,i)=>{let [dr,du]=ord[i];return [0,1,2].map(k=>k===2?(du===0?height[dr]:0):left[dr]*C[du][k]+right[dr]*es[du][k]);});
  for(let k=0;k<3;k++)for(let j=0;j<nm;j++){let m=k===2?2*j:2*j+1,ss=k===1,co0=ss?sin[m]:cos[m],co1=m*(ss?cos[m]:-sin[m]),co2=-m*m*co0,b0=0,b1=0,b2=0;
   for(let i=0;i<nt;i++){let y=z[(i*3+k)*nm+j];b0+=R[0][i]*y;b1+=R[1][i]*y;b2+=R[2][i]*y;}
   Y[0][k]+=b0*co0;Y[1][k]+=b1*co0;Y[2][k]+=b0*co1;Y[3][k]+=b2*co0;Y[4][k]+=b1*co1;Y[5][k]+=b0*co2;}
  return Y;
 };
}
function compactClock(nr,nm,z){
 const field=compactPhysical(z),h=1/(nr+3),dim=2*nr*nm,pi=Math.PI,ip=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
 const comb=(a,x,b,y)=>[a[0]*x+b[0]*y,a[1]*x+b[1]*y,a[2]*x+b[2]*y];
 function b3(x){const t=Math.abs(x),s=Math.sign(x);if(t>=2)return [0,0,0];if(t>1)return [(2-t)**3/6,-s*(2-t)**2/2,2-t];return [2/3-t*t+t**3/2,s*(-2*t+1.5*t*t),-2+3*t];}
 function basis(t,u){const out=[];for(let j=Math.max(0,Math.floor(t/h)-3);j<Math.min(nr,Math.floor(t/h)+1);j++){
   let [b,db,dd]=b3(t/h-j-2);if(!b&&!db&&!dd)continue;db/=h;dd/=h*h;for(let axis=0;axis<2;axis++)for(let k=0;k<nm;k++){
   const m=2*(k+axis),c=Math.cos(m*u),s=Math.sin(m*u),a=axis?s:c,da=m*(axis?c:-s),dda=-m*m*a,
       ix=(j*2+axis)*nm+k,scale=axis?1/m:h;
   out.push([ix,axis,b*a*scale,db*a*scale,b*da*scale,dd*a*scale,db*da*scale,b*dda*scale]);}}
  return out;}
 function coord(t,u,b,p){let d=[[t,1,0,0,0,0],[u,0,1,0,0,0]];for(let v of b){let c=p[v[0]],a=d[v[1]];for(let k=0;k<6;k++)a[k]+=c*v[2+k];}return d;}
 function goal(t){let Q=0,S=0;for(let i=0;i<64;i++){let [P,v,w]=field(t,i*2*pi/64);Q+=ip(v,v)/64;S+=ip(w,w)/64;}return [Q,S];}
 function train(R,N,rt=0,ut=0){let pts=[];for(let j=0;j<R;j++){let t=(j+rt)/(R-1+2*rt),g=goal(t);for(let i=0;i<N;i++){const u=(i+ut)/(N-1+2*ut)*pi/2;pts.push({t,u,g,b:basis(t,u)});}}return pts;}
 function evalf(pts,p,sharp,want=true){
  let cost=0,metric=0,minDet=Infinity,grad=new Float64Array(dim),at=[],maxD=0;
  for(let {t,u,g,b} of pts){let [[T,Tt,Tu],[U,Ut,Uu]]=coord(t,u,b,p),det=Tt*Uu-Tu*Ut;
   minDet=Math.min(minDet,det);if(!Number.isFinite(T)||T< -1e-14||T>1+1e-14||det<.05)return {cost:Infinity,grad,metric:Infinity,minDet};
   const [P,v,w,A,B,C]=field(T,U),V=comb(v,Tt,w,Ut),W=comb(v,Tu,w,Uu),Q=g[0],S=g[1],qs=Math.sqrt(Q*S),e=ip(V,V)/Q-1,f=ip(V,W)/qs,y=ip(W,W)/S-1;
   let err=Math.abs(.5*(e+y))+Math.hypot(.5*(e-y),f),tr=e*e+2*f*f+y*y;cost+=tr*(1+sharp*tr);
   if(err>metric){metric=err;at=[t,u,e,f,y];}
   maxD=Math.max(maxD,Math.abs(T-t),Math.abs(U-u));if(!want)continue;
   let sc=2*(1+2*sharp*tr),dE=sc*e/Q,dF=2*sc*f/qs,dG=sc*y/S;
   const vv=comb(V,2*dE,W,dF),ww=comb(V,dF,W,2*dG),G0=[ip(vv,comb(A,Tt,B,Ut))+ip(ww,comb(A,Tu,B,Uu)),ip(vv,v),ip(ww,v)],
    G1=[ip(vv,comb(B,Tt,C,Ut))+ip(ww,comb(B,Tu,C,Uu)),ip(vv,w),ip(ww,w)];
   for(let v of b){let a=v[1]?G1:G0;grad[v[0]]+=a[0]*v[2]+a[1]*v[3]+a[2]*v[4];}
  }
  for(let j=0;j<dim;j++)grad[j]/=pts.length;
  return {cost:cost/pts.length,grad,metric,minDet,at,maxD};
 }
 const inner=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0);
 function fit(pts,p,sharp,steps){let x=Array.from(p),r=evalf(pts,x,sharp),mem=[],hist=[],acceptedSteps=0;for(let it=0;it<steps;it++){
  let d=Array.from(r.grad),aa=[];for(let j=mem.length-1;j>=0;j--){let [s,y,sy]=mem[j],h=inner(s,d)/sy;aa[j]=h;for(let k=0;k<dim;k++)d[k]-=h*y[k];}
  let fac=mem.length?mem.at(-1)[2]/inner(mem.at(-1)[1],mem.at(-1)[1]):.3;d=d.map(v=>v*fac);
  for(let j=0;j<mem.length;j++){let [s,y,sy]=mem[j],h=inner(y,d)/sy;for(let k=0;k<dim;k++)d[k]+=s[k]*(aa[j]-h);}
  let descent=inner(d,r.grad);if(descent<=0){d=Array.from(r.grad);descent=inner(d,d);mem=[];}
  let step=1,xn,rn,accepted=false;for(let k=0;k<20;k++){xn=x.map((s,j)=>s-step*d[j]);rn=evalf(pts,xn,sharp,false);if(rn.cost<r.cost-1e-4*step*descent){accepted=true;break;}step*=.5;}
  if(!accepted)break;rn=evalf(pts,xn,sharp);let s=xn.map((v,j)=>v-x[j]),y=Array.from(rn.grad,(v,j)=>v-r.grad[j]),sy=inner(s,y);if(sy>1e-19){mem.push([s,y,sy]);if(mem.length>12)mem.shift();}
  x=xn;r=rn;acceptedSteps++;if((it+1)%5===0)hist.push([it+1,r.cost,r.metric,r.minDet]);}
  return {x,hist,acceptedSteps,final:{metric:r.metric,minDet:r.minDet,worst:r.at,cost:r.cost,maxDisplacement:r.maxD}};}
 return {field,basis,coord,train,fit,evalf,goal,dim};
}
const centralA=compactPhysical(Array(192).fill(0))(0,0)[0][0];
function composeJet(cl,t,u,p){
 const [T,U]=cl.coord(t,u,cl.basis(t,u),p),[P,v,w,A,B,C]=cl.field(T[0],U[0]);
 const first=(i)=>v.map((x,k)=>x*T[i]+w[k]*U[i]),second=(i,j,d)=>v.map((x,k)=>x*T[d]+w[k]*U[d]+A[k]*T[i]*T[j]+B[k]*(T[i]*U[j]+T[j]*U[i])+C[k]*U[i]*U[j]);
 return [P,first(1),first(2),second(1,1,3),second(1,2,4),second(2,2,5)];
}
function clockDerivativeBounds(p,nr,nm){
 const h=1/(nr+3),x=(j,d,k)=>j>=0&&j<nr?p[(j*2+d)*nm+k]:0;let bound=[0,0,0,0];
 for(let j=0;j<=nr;j++){let row=[0,0,0,0];for(let k=0;k<nm;k++){
   row[0]+=Math.abs(x(j,0,k)-x(j-1,0,k));row[1]+=2*k*h*Math.abs(x(j,0,k));
   row[2]+=Math.abs(x(j,1,k)-x(j-1,1,k))/(2*(k+1)*h);row[3]+=Math.abs(x(j,1,k));}
   for(let i=0;i<4;i++)bound[i]=Math.max(bound[i],row[i]+1e-13);
 }
 return {displacementJacobian:bound,determinantLower:(1-bound[0])*(1-bound[3])-bound[1]*bound[2]-1e-13};
}

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

function observeClock(cl,p,z,group,lam=1.06){const ntarget=64,targetZ=z;configure(8,8);
 const ind=group==='G11',N=ind?256:group==='G10a'?128:192,angled=ind?.417:0;
 const pts=ownGrid(ind),target=build(pts.length,ntarget,pts.map(v=>v[0]),0);
 let peak=0,kap=0,held=Infinity,wd=0,bound=0,zhi=0,zlo=Infinity,minArea=Infinity,L=0,lowerQ=Infinity,lowerS=Infinity,mg=Array(7).fill(0),vmax=[0,0,0,0],sqv=[0,0,0,0],mworst,kworst;
 for(let i=0;i<pts.length;i++){let [t,w]=pts[i];const [Q,S]=gramTarget(jets(target,target.rows[i],targetZ),ntarget),Y=new Float64Array(N*18);
  for(let n=0;n<N;n++)Y.set(composeJet(cl,t,2*pi*(n+angled)/N,p).flat(),18*n);
  L+=w*lam*Math.sqrt(Q);lowerQ=Math.min(lowerQ,Q);lowerS=Math.min(lowerS,S);
  for(let n=0;n<N;n++){const p=18*n,v=(j)=>[Y[p+j],Y[p+j+1],Y[p+j+2]],P=v(0).map(x=>x*lam),V=v(3),U=v(6),A=v(9),B=v(12),C=v(15),E=dot(V,V),F=dot(V,U),G=dot(U,U),base=cross(V,U),ds=norm(base),nor=base.map(a=>a/ds),ar=ds/Math.sqrt(Q*S),ln=dot(A,nor),mn=dot(B,nor),nn=dot(C,nor),H=(G*ln-2*F*mn+E*nn)/(2*ds*ds),K=(ln*nn-mn*mn)/(ds*ds),rd=Math.sqrt(Math.max(0,H*H-K));
   const ka=(H+rd)/lam,kb=(H-rd)/lam,absK=Math.max(Math.abs(ka),Math.abs(kb)),e=E/Q-1,f=F/Math.sqrt(Q*S),g=G/S-1,me=Math.abs((e+g)/2)+Math.hypot((e-g)/2,f),u=2*pi*(n+angled)/N;
   if(me>peak){peak=me;mworst=[t,u];}if(absK>kap){kap=absK;kworst=[t,u];}
   const r=norm(P),rp=Math.hypot(P[0],P[1]-lam*centralA,P[2]),rm=Math.hypot(P[0],P[1]+lam*centralA,P[2]),rc=Math.hypot(P[0],P[1]),q=Math.max(0,Math.min(1,(rc-.52)/.02)),a=.0195*q**3*(10+q*(-15+6*q));
   held=Math.min(held,rp,rm);bound=Math.max(bound,r);wd=Math.max(wd,Math.abs(P[1]));zhi=Math.max(zhi,P[2]);zlo=Math.min(zlo,P[2]);minArea=Math.min(minArea,ar);
   let geo=[r-1.59,P[1]-.885,-P[1]-.885,P[2]-lam*endZ-a,-P[2]-lam*endZ-a,.65-rp,.65-rm].map(x=>Math.max(0,x));for(let j=0;j<7;j++)mg[j]=Math.max(mg[j],geo[j]);
   let metric2=e*e+2*f*f+g*g,cv=[ka,kb].map(k=>Math.max(0,Math.abs(k)-9.5));let msum=metric2*(1+metric2/.12**2),kn=cv.reduce((v,c)=>v+c*c,0),ksum=kn*(1+kn/4),gsum=geo.reduce((v,a)=>v+a*a,0),aa=Math.max(0,(.5/ar)**2-1)**2;
   let wt=w*lam*Math.sqrt(Q)/N;for(let j=0;j<4;j++){let v=[msum,ksum,gsum,aa][j];sqv[j]+=wt*v;vmax[j]=Math.max(vmax[j],v);}
  }
 }
 return {group,radial:pts.length,angles:N,trueRowCount:14*pts.length*N,metric:peak,curvature:kap,held,halfWidth:wd,ballRadius:bound,upperZ:[zlo,zhi],minimumAreaRatio:minArea,physicalTransitionLength:L,finiteMinTargetSquared:[lowerQ,lowerS],metricWitness:mworst,curvatureWitness:kworst,guideMax:mg,groupSquaredNorms:sqv,groupMaxSquared:vmax};
}

export {compactPhysical,compactClock,composeJet,clockDerivativeBounds,observeClock};
if(process.argv[1] && import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,output]=process.argv.slice(2),z=JSON.parse(readFileSync(state)),cl=compactClock(10,5,z);
 if(op==='fit'){const res=cl.fit(cl.train(37,21),Array(cl.dim).fill(0),95,115);writeFileSync(output,JSON.stringify(res.x)+'\n');console.log(JSON.stringify({accepted:res.acceptedSteps,finiteTraining:res.final}));}
 else if(op==='observe'){const p=JSON.parse(readFileSync(output));console.log(JSON.stringify({orientation:clockDerivativeBounds(p,10,5),full:['G10a','G10b','G11'].map(q=>observeClock(cl,p,z,q))},null,2));}
 else throw Error('fit STATE192 OUT | observe STATE192 CLOCK');
}