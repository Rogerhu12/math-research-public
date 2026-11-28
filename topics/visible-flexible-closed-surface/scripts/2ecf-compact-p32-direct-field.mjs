#!/usr/bin/env node
/** Compact p32 central cylinder, direct polynomial annulus and true planar recut. */
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
const pi=Math.PI, leftZ=13/128, endZ=.54, endR=.35, nominal=1.2, centralP=32, centralR=.25;
let nr,nm,ch,dim;function configure(radial,angular){nr=radial;nm=angular;ch=[];for(let k=0;k<3;k++)for(let j=0;j<nm;j++)ch.push([k,k===2?2*j:2*j+1,k===1?1:0]);dim=nr*ch.length;}
configure(8,8);
const pairs=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];

const c=[];let rat=1;for(let j=1;j<=centralP;j++){rat*= (centralP-j+1)/(centralP+j);c[j]=2*(1-centralR)*(j%2?-1:1)*rat;}
function arc(th){let s=th;for(let j=1;j<=centralP;j++)s+=c[j]*Math.sin(2*j*th)/(2*j);return s;}
function curve(u){
 let a=0,b=2*pi;u=(u%(2*pi)+2*pi)%(2*pi);for(let i=0;i<53;i++){let m=(a+b)/2;if(arc(m)>u)b=m;else a=m;}
 let th=(a+b)/2,h=1,hp=0,rho=1;for(let j=1;j<=centralP;j++){let f=2*j,co=Math.cos(f*th)*c[j];h+=co/(1-f*f);rho+=co;hp-=f*Math.sin(f*th)*c[j]/(1-f*f);}
 let x=Math.cos(th),y=Math.sin(th);return [[h*x-hp*y,h*y+hp*x],[-y,x],[-x/rho,-y/rho]];
}
const centralA=curve(0)[0][0];
const choose=[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]];
function bpoly(t,n,i){return i<0||i>n?0:choose[n][i]*t**i*(1-t)**(n-i);}
function bern(t,d,j){if(d===0)return bpoly(t,5,j);if(d===1)return 5*(bpoly(t,4,j-1)-bpoly(t,4,j));return 20*(bpoly(t,3,j-2)-2*bpoly(t,3,j-1)+bpoly(t,3,j));}
function poly(t,j){
 if(j>=12){const spans=[[0,.11],[0,.19],[.03,.17],[.063,.23],[.13,.36],[.20,.57],[.43,.80],[.75,1]],v=spans[j-12],w=v[1]-v[0],y=(t-v[0])/w;if(y<=0||y>=1)return [0,0,0];const b=y*(1-y),q=1-2*y,c=.8*w*w;return [c*64*b**3,c*192*b*b*q/w,c*(384*b*q*q-384*b*b)/(w*w)];}

 let u=2*t-1,p=t*(1-t),q=1-2*t;
 let a=64*p**3,ap=192*p*p*q,app=384*p*q*q-384*p*p;
 if(nr===4){const T=[1,u,2*u*u-1,4*u**3-3*u],Tp=[0,2,8*u,24*u*u-6],Tpp=[0,0,16,96*u];return [a*T[j],ap*T[j]+a*Tp[j],app*T[j]+2*ap*Tp[j]+a*Tpp[j]];}
 let T=[1,u],Tp=[0,2],Tpp=[0,0];for(let k=2;k<=j;k++){T[k]=2*u*T[k-1]-T[k-2];Tp[k]=4*T[k-1]+2*u*Tp[k-1]-Tp[k-2];Tpp[k]=8*Tp[k-1]+2*u*Tpp[k-1]-Tpp[k-2];}
 return [a*T[j],ap*T[j]+a*Tp[j],app*T[j]+2*ap*Tp[j]+a*Tpp[j]];
}
function ang(u,k,s,d){return k===0?(d===0&&!s?1:0):(s?Math.sin(k*u+d*pi/2):Math.cos(k*u+d*pi/2))*k**d;}
function build(R,N,rshift=0,ushift=0){
 const us=Array.from({length:N},(_,k)=>2*pi*(k+ushift)/N),cent=us.map(curve),A=new Float64Array(N*ch.length*3);
 for(let n=0;n<N;n++)for(let h=0;h<ch.length;h++)for(let d=0;d<3;d++)A[(n*ch.length+h)*3+d]=ang(us[n],ch[h][1],ch[h][2],d);
 let rows=[];
 for(let i=0;i<R;i++){
  let t=Array.isArray(rshift)?rshift[i]:(i+rshift)/(R-1+2*rshift),B=Array.from({length:nr},(_,j)=>poly(t,j)),base=new Float64Array(N*18);
  for(let n=0;n<N;n++)for(let j=0;j<6;j++)for(let k=0;k<3;k++){
   let [x,u]=pairs[j],ev=k<2?ang(us[n],1,k===1,u):0,P=k<2?cent[n][u][k]:(u===0?leftZ:0),V=k===2&&u===0?nominal:0,Q=k<2?endR*ev:(u===0?endZ:0),W=-nominal*ev;
   let vals=[P,P+V/5,P+2*V/5,Q-2*W/5,Q-W/5,Q];let v=0;for(let m=0;m<6;m++)v+=bern(t,x,m)*vals[m];base[n*18+3*j+k]=v;
  }
  rows.push({t,B,base});
 }
 return {R,N,A,rows};
}
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],norm=a=>Math.sqrt(dot(a,a));
function jets(data,row,z){
 let Y=new Float64Array(row.base),amp=new Float64Array(3*ch.length);
 for(let h=0;h<ch.length;h++)for(let a=0;a<3;a++)for(let j=0;j<nr;j++)amp[3*h+a]+=z[ch.length*j+h]*row.B[j][a];
 for(let n=0;n<data.N;n++)for(let h=0;h<ch.length;h++)for(let j=0;j<6;j++)Y[18*n+3*j+ch[h][0]]+=amp[3*h+pairs[j][0]]*data.A[(n*ch.length+h)*3+pairs[j][1]];
 return Y;
}
function gramTarget(Y,N){let E=0,G=0;for(let n=0;n<N;n++){let p=18*n;for(let k=0;k<3;k++){E+=Y[p+3+k]**2;G+=Y[p+6+k]**2;}}return [E/N,G/N];}
function evaluate(data,z,o={},external=null){
 const heldAxis=o.centralMark??centralA;
 let grad=new Float64Array(dim),cost=0,metric=0,curvature=0,held=Infinity,diamHalf=0,width=0,height=0,area=Infinity,guide=Array(7).fill(0),bad=false;
 let metricSharp=o.metricSharp??9,kgoal=o.kgoal??9.5,kw=o.kw??.3,gw=o.gw??200,baseCost=0,metricAt=[],curvAt=[];
 const deriv=o.deriv!==false, N=data.N,R=data.R;
 for(let i=0;i<R;i++){const row=data.rows[i],Y=jets(data,row,z);
  let [Q,S]=external?external[i]:gramTarget(Y,N),Dg=Math.sqrt(Q*S),accQ=0,accS=0;let bar=new Float64Array(Y.length);
  for(let n=0;n<N;n++){const p=18*n, vec=k=>[Y[p+k],Y[p+k+1],Y[p+k+2]];let P=vec(0),V=vec(3),U=vec(6),A=vec(9),B=vec(12),C=vec(15);
   const E=dot(V,V),F=dot(V,U),G=dot(U,U),nn=cross(V,U),den=norm(nn),det=den*den,ar=den/Dg;
   if(!Number.isFinite(ar)||ar<1e-6){bad=true;continue;}
   area=Math.min(area,ar);
   const normal=nn.map(x=>x/den),L=dot(A,normal),M=dot(B,normal),Nc=dot(C,normal),H=(G*L-2*F*M+E*Nc)/(2*det),K=(L*Nc-M*M)/det,rad=Math.sqrt(Math.max(0,H*H-K));
   const e=E/Q-1,f=F/Dg,g=G/S-1,sm=e*e+2*f*f+g*g,peak=Math.abs((e+g)/2)+Math.hypot((e-g)/2,f);
   if(peak>metric){metric=peak;metricAt=[row.t,n];}
   const cm=sm*(1+metricSharp*sm);cost+=cm;baseCost+=sm;
   const ds=2*(1+2*metricSharp*sm);let dE=ds*e/Q,dF=2*ds*f/Dg,dG=ds*g/S;
   accQ-=ds*(e*(e+1)+f*f)/Q;accS-=ds*(g*(g+1)+f*f)/S;
   if(ar<.5){const v=.5-ar;cost+=10*v*v;const da=-20*v*ar/2;dE+=da*G/det;dF-=da*2*F/det;dG+=da*E/det;accQ-=da/Q;accS-=da/S;}
   for(const kap of [H+rad,H-rad]){
    const ak=Math.abs(kap);if(ak>curvature){curvature=ak;curvAt=[row.t,n];}
    if(ak<=kgoal)continue;
    const v=(ak/kgoal-1),vv=v*v;cost+=kw*vv*(1+vv);
    if(!deriv)continue;
    const w=kw*2*v*(1+2*vv)*Math.sign(kap)/kgoal;
    let a=M-kap*F,b=kap*E-L,c2=Nc-kap*G,d2=kap*F-M;if(c2*c2+d2*d2>a*a+b*b){a=c2;b=d2;}
    let size=Math.sqrt(E*a*a+2*F*a*b+G*b*b);if(size<1e-13)continue;a/=size;b/=size;
    const aa=w*a*a,ab=2*w*a*b,bb=w*b*b;
    dE-=kap*aa;dF-=kap*ab;dG-=kap*bb;
    let nb=[0,0,0];for(let k=0;k<3;k++){nb[k]=aa*A[k]+ab*B[k]+bb*C[k];bar[p+9+k]+=aa*normal[k];bar[p+12+k]+=ab*normal[k];bar[p+15+k]+=bb*normal[k];}
    const bn=dot(nb,normal);nb=nb.map((v,k)=>(v-bn*normal[k])/den);
    const dv=cross(U,nb),du=cross(nb,V);for(let k=0;k<3;k++){bar[p+3+k]+=dv[k];bar[p+6+k]+=du[k];}
   }
   if(deriv)for(let k=0;k<3;k++){bar[p+3+k]+=2*dE*V[k]+dF*U[k];bar[p+6+k]+=dF*V[k]+2*dG*U[k];}
   const rr=norm(P),rp=Math.hypot(P[0],P[1]-heldAxis,P[2]),rm=Math.hypot(P[0],P[1]+heldAxis,P[2]),cyl=Math.hypot(P[0],P[1]),l=Math.max(0,Math.min(1,(cyl-.52)/.02)),allow=.0195*l**3*(10+l*(-15+6*l)),allowR=.0195*30*(l*(1-l))**2/.02;
   held=Math.min(held,rp,rm);diamHalf=Math.max(diamHalf,rr);width=Math.max(width,Math.abs(P[1]));height=Math.max(height,Math.abs(P[2]));
   const signed=[rr-1.59,P[1]-(o.wgoal??.885),-P[1]-(o.wgoal??.885),P[2]-endZ-allow,-P[2]-endZ-allow,(o.hgoal??.65)-rp,(o.hgoal??.65)-rm];
   for(let j=0;j<7;j++){const v=signed[j];guide[j]=Math.max(guide[j],v);if(v<=0)continue;cost+=gw*v*v;
    if(deriv){const w=2*gw*v, gg=j===0?P.map(xx=>xx/rr):j===1?[0,1,0]:j===2?[0,-1,0]:j===3||j===4?[-allowR*P[0]/cyl,-allowR*P[1]/cyl,j===3?1:-1]:[-P[0]/(j===5?rp:rm),-(P[1]+(j===5?-heldAxis:heldAxis))/(j===5?rp:rm),-P[2]/(j===5?rp:rm)]; for(let k=0;k<3;k++)bar[p+k]+=w*gg[k];}
   }
  }
  if(!deriv)continue;
  if(!external)for(let n=0;n<N;n++)for(let k=0;k<3;k++){const p=n*18;bar[p+3+k]+=2*accQ/N*Y[p+3+k];bar[p+6+k]+=2*accS/N*Y[p+6+k];}
  const bb=new Float64Array(3*ch.length);
  for(let n=0;n<N;n++)for(let h=0;h<ch.length;h++)for(let j=0;j<6;j++)bb[3*h+pairs[j][0]]+=bar[18*n+3*j+ch[h][0]]*data.A[(n*ch.length+h)*3+pairs[j][1]];
  for(let j=0;j<nr;j++)for(let h=0;h<ch.length;h++)for(let a=0;a<3;a++)grad[j*ch.length+h]+=bb[3*h+a]*row.B[j][a];
 }
 const scale=1/(R*N);cost*=scale;for(let j=0;j<dim;j++)grad[j]*=scale;
 return {cost:bad?Infinity:cost,grad,metric,curvature,held,diamHalf,width,height,area,guide,metricAt,curvAt};
}
function stats(f){let {grad,...rest}=f;return rest;}
function inner(a,b){let v=0;for(let i=0;i<a.length;i++)v+=a[i]*b[i];return v;}
function lbfgs(data,z,options,iterations,mem=null,external=null){
 z=Float64Array.from(z);let r=evaluate(data,z,options,external),hist=[],stash=mem??[];for(let it=0;it<iterations;it++){
  let d=Float64Array.from(r.grad),alpha=[];
  for(let k=stash.length-1;k>=0;k--){let [s,y,sy]=stash[k],v=inner(s,d)/sy;alpha[k]=v;for(let j=0;j<dim;j++)d[j]-=v*y[j];}
  let init=stash.length?stash.at(-1)[2]/inner(stash.at(-1)[1],stash.at(-1)[1]):.015;
  for(let j=0;j<dim;j++)d[j]*=init;
  for(let k=0;k<stash.length;k++){let [s,y,sy]=stash[k],v=inner(y,d)/sy;for(let j=0;j<dim;j++)d[j]+=s[j]*(alpha[k]-v);}
  let descent=inner(d,r.grad);if(descent<=0){d=Float64Array.from(r.grad);descent=inner(d,r.grad);stash=[];}
  let step=1,next,newz,ok=false;
  for(let tr=0;tr<18;tr++){newz=z.map((v,j)=>v-step*d[j]);next=evaluate(data,newz,{...options,deriv:false},external);
   if(next.cost<r.cost-1e-4*step*descent){ok=true;break;}step/=2;}
  if(!ok){hist.push({stopped:true,step});break;}
  next=evaluate(data,newz,options,external);let s=Array.from(newz,(v,j)=>v-z[j]),y=Array.from(next.grad,(v,j)=>v-r.grad[j]),sy=inner(s,y);
  if(sy>1e-12*Math.sqrt(inner(s,s)*inner(y,y))){stash.push([s,y,sy]);if(stash.length>10)stash.shift();}
  z=newz;r=next;if((it+1)%10===0)hist.push([it+1,r.cost,r.metric,r.curvature,r.held]);
 }
 return {z:Array.from(z),stats:stats(r),hist,mem:stash};
}
function freezeObserver(z,R,N,rt,ut,trainingAngles){
 const target=build(R,trainingAngles,rt,0),ind=build(R,N,rt,ut);
 const g=target.rows.map(row=>gramTarget(jets(target,row,z),trainingAngles));
 return stats(evaluate(ind,z,{deriv:false},g));
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
function physicalObserve(z,group,lam=1.06,ntarget=64,targetZ=z){
 const ind=group==='G11',N=ind?256:group==='G10a'?128:192,angled=ind?.417:0;
 const pts=ownGrid(ind),target=build(pts.length,ntarget,pts.map(v=>v[0]),0),meas=build(pts.length,N,pts.map(v=>v[0]),angled);
 let peak=0,kap=0,held=Infinity,wd=0,bound=0,zhi=0,zlo=Infinity,minArea=Infinity,L=0,lowerQ=Infinity,lowerS=Infinity,mg=Array(7).fill(0),vmax=[0,0,0,0],sqv=[0,0,0,0],mworst,kworst;
 for(let i=0;i<pts.length;i++){let [t,w]=pts[i];const [Q,S]=gramTarget(jets(target,target.rows[i],targetZ),ntarget),Y=jets(meas,meas.rows[i],z);
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
function closedCloud(z,R,N,rs=0,ua=0,scale=1){
 let data=build(R,N,rs,ua),cx=[],cy=[],cz=[],nx=[],ny=[],nz=[],material=[],uu=[];
 function add(x,y,h,n0,n1,n2,q,u){
  cx.push(scale*x);cy.push(scale*y);cz.push(scale*h);nx.push(n0);ny.push(n1);nz.push(n2);material.push(q);uu.push(u);
 }
 function ringsym(P,n,q,u){add(...P,...n,q,u);if(q>0)add(P[0],P[1],-P[2],n[0],n[1],-n[2],-q,u);}
 let angles=Array.from({length:N},(_,k)=>2*pi*(k+ua)/N),centrals=angles.map(curve);
 for(let s=0;s<8;s++)for(let n=0;n<N;n++){let [P,T]=centrals[n],v=s*leftZ/8;ringsym([...P,v],[T[1],-T[0],0],v,angles[n]);}
 let grid=data.rows;if(rs!==0){let bound=build(2,N,0,ua);grid=[bound.rows[0],...grid,bound.rows[1]];}
 for(let row of grid){let Y=jets(data,row,z);for(let i=0;i<N;i++){
   let p=18*i,V=Array.from(Y.slice(p+3,p+6)),U=Array.from(Y.slice(p+6,p+9)),n=cross(V,U),d=norm(n);
   ringsym(Array.from(Y.slice(p,p+3)),n.map(x=>x/d),leftZ+nominal*row.t,angles[i]);}}
 for(let s=1;s<=20;s++)for(let j=0;j<(s===20?1:N);j++){let radius=endR*(20-s)/20,u=angles[j]+(s%2)*pi/N;
   ringsym([radius*Math.cos(u),radius*Math.sin(u),endZ],[0,0,1],leftZ+nominal+endR-radius,u);}
 const reach=.0971,h=2*reach+.004,box=new Map(),idx=(a,b,c)=>(a+32)*4096+(b+32)*64+c+32;
 for(let i=0;i<cx.length;i++){const k=idx(Math.floor(cx[i]/h),Math.floor(cy[i]/h),Math.floor(cz[i]/h));
  if(!box.has(k))box.set(k,[]);box.get(k).push(i);}
 let best=Infinity,far=Infinity,minChord=Infinity,worst=null,pairs=0;
 for(let i=0;i<cx.length;i++){let a=Math.floor(cx[i]/h),b=Math.floor(cy[i]/h),c=Math.floor(cz[i]/h);
  for(let da=-1;da<=1;da++)for(let db=-1;db<=1;db++)for(let dc=-1;dc<=1;dc++){
   let v=box.get(idx(a+da,b+db,c+dc));if(!v)continue;
   for(let j of v){if(j<=i)continue;let x=cx[j]-cx[i],y=cy[j]-cy[i],z0=cz[j]-cz[i],ss=x*x+y*y+z0*z0;
    if(ss>h*h)continue;pairs+=2;minChord=Math.min(minChord,Math.sqrt(ss));
    const d1=nx[i]*x+ny[i]*y+nz[i]*z0,d2=nx[j]*x+ny[j]*y+nz[j]*z0;
    let test=ss/(2*Math.max(Math.abs(d1),Math.abs(d2)));if(test<best){best=test;worst=[material[i],uu[i],material[j],uu[j],Math.sqrt(ss)];}
    if(Math.abs(material[i]-material[j])>.20)far=Math.min(far,test);
   }
  }
 }
 return {sampledMin:best,materialFarMin:Number.isFinite(far)?far:null,minimumSampleSpacing:minChord,worst,points:cx.length,orderedNearPairs:pairs};
}
function exactTargetWitness(z, shapeNR=8, shapeNM=8) {
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;};
 const F=(p,q=1n)=>{p=BigInt(p);q=BigInt(q);if(q<0n){p=-p;q=-q;}const d=gcd(p,q);return [p/d,q/d];};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
 const abs=a=>a[0]<0n?neg(a):a,lt=(a,b)=>a[0]*b[1]<b[0]*a[1],choose=(n,j)=>{let a=1n;for(let k=0;k<j;k++)a=a*BigInt(n-k)/BigInt(k+1);return a;};
 const zero=F(0),one=F(1),half=F(1,2);
 const dyadic=(x)=>{if(x===0)return zero;const v=new DataView(new ArrayBuffer(8));v.setFloat64(0,x);const b=v.getBigUint64(0),e=Number((b>>52n)&2047n),mant=((e>0?1n:0n)<<52n)|(b% (1n<<52n)),exp=(e||1)-1023-52;
  return F((b>>63n?-1n:1n)*mant*(exp>0?1n<<BigInt(exp):1n),exp<0?1n<<BigInt(-exp):1n);};
 const plus=(p,q)=>Array.from({length:Math.max(p.length,q.length)},(_,i)=>add(p[i]??zero,q[i]??zero));
 const times=(p,q)=>{const out=Array.from({length:p.length+q.length-1},()=>zero);for(let i=0;i<p.length;i++)for(let j=0;j<q.length;j++)out[i+j]=add(out[i+j],mul(p[i],q[j]));return out;};
 const scale=(p,c)=>p.map(s=>mul(s,c)),diff=p=>p.slice(1).map((s,j)=>mul(s,F(j+1)));
 const ba=(coeff)=>{let p=[zero];for(let j=0;j<6;j++){
   let a=Array(j).fill(zero).concat([one]);for(let k=0;k<5-j;k++)a=times(a,[one,F(-1)]);
   p=plus(p,scale(a,mul(F(choose(5,j)),coeff[j])));}return p;};
 const toBern=p=>p.map((_,i)=>p.slice(0,i+1).reduce((q,x,j)=>add(q,mul(x,F(choose(i,j),choose(p.length-1,j)))),zero));
 let A=one,B=one;for(let j=1;j<=32;j++){
  let c=F(3n*(j%2?-1n:1n)*choose(64,32-j),2n*choose(64,32)*BigInt(1-4*j*j));A=add(A,c);B=add(B,j%2?neg(c):c);}
 const angle=(harm,sine,quarter,derivative)=>{if(harm===0)return derivative===0&&!sine?1:0;let i=(harm*quarter+derivative)%4;return (sine?[0,1,0,-1]:[1,0,-1,0])[i]*harm**derivative;};
 const slope=F(6,5),endR=F(7,20);
 const shape=[zero,zero,zero,F(64),F(-192),F(192),F(-64)],cheb=[[one],[F(-1),F(2)]];
 for(let k=2;k<shapeNR;k++)cheb.push(plus(times([F(-2),F(4)],cheb[k-1]),scale(cheb[k-2],F(-1))));
 let sets=[[],[]];for(let step=0;step<2;step++)for(let ax=0;ax<2;ax++)for(let k=0;k<3;k++){
  let ud=step===1?1:0,ev=k<2?F(angle(1,k===1,ax,ud)):zero;
  let P=k===2?(ud?zero:F(13,128)):(ud?F(ax===0?(k===1?1:0):(k===0?-1:0)):(ax===0?(k===0?A:zero):(k===1?B:zero)));
  let V=k===2&&!ud?slope:zero,Q=k===2?(ud?zero:F(27,50)):mul(ev,endR),W=mul(neg(slope),ev);
  let p=ba([P,add(P,mul(V,F(1,5))),add(P,mul(V,F(2,5))),sub(Q,mul(W,F(2,5))),sub(Q,mul(W,F(1,5))),Q]);
  for(let j=0;j<shapeNR;j++)for(let h=0;h<shapeNM;h++){let m=k===2?2*h:2*h+1,sine=k===1;
    p=plus(p,scale(times(shape,cheb[j]),mul(dyadic(z[(j*3+k)*shapeNM+h]),F(angle(m,sine,ax,ud)))));}
  sets[step].push(toBern(step===0?diff(p):p));
 }
 const split=a=>{let left=[a[0]],right=[a.at(-1)],row=a;while(row.length>1){row=row.slice(1).map((v,i)=>mul(half,add(row[i],v)));left.push(row[0]);right.push(row.at(-1));}return [left,right.reverse()];};
 const threshold=F(1,8);let leaves=[0,0],maxDepth=[0,0];
 function cover(arr,level,which){
   if(arr.some(b=>b.every(v=>!lt(v,threshold))||b.every(v=>!lt(neg(v),threshold)))){leaves[which]++;maxDepth[which]=Math.max(maxDepth[which],level);return;}
   if(level>=24)throw Error("Unresolved true axis component in positivity proof");
   let halves=arr.map(split);cover(halves.map(q=>q[0]),level+1,which);cover(halves.map(q=>q[1]),level+1,which);
 }
 for(let i=0;i<sets.length;i++)cover(sets[i],0,i);
 return {perimeter:"2*pi",A:A.join("/"),B:B.join("/"),speedAndRadiusCertificate:"For every t at one of the two true sampled cardinal material angles one Cartesian component has abs >= 1/8; both mean-squared targets on 64 angles are >= 1/4096 before scaling.",coverageLeaves:leaves,maximumSubdivisionDepth:maxDepth};
}
function pad(z,r,m,R,M){let w=Array(3*R*M).fill(0);for(let i=0;i<r;i++)for(let k=0;k<3;k++)for(let j=0;j<m;j++)w[(i*3+k)*M+j]=z[(i*3+k)*m+j];return w;}
function reproduce192(){
 configure(4,4);let seed=Array(dim).fill(0);seed[4]=.24;seed[8]=-.1;seed[9]=.14;
 const first=lbfgs(build(29,40),seed,{metricSharp:12,kw:.55,gw:200},120);
 configure(8,8);return lbfgs(build(39,64),pad(first.z,4,4,8,8),{metricSharp:40,kw:1.2,gw:4000},145);
}
function fixed396(seed){
 configure(12,11);const z=pad(seed,8,8,12,11),d=build(57,88),target=build(57,64),g=target.rows.map(r=>gramTarget(jets(target,r,z),64));
 return lbfgs(d,z,{metricSharp:140,kw:1.1,gw:1800,kgoal:10.15,wgoal:.842,hgoal:.614},155,null,g);
}
function chartRecord(z,goal=z,R=8,M=8) {
 configure(R,M);
 const target=R===8&&M===8?goal:pad(goal,8,8,R,M);
 return {fullPhysical:["G10a","G10b","G11"].map(g=>physicalObserve(z,g,1.06,64,target)),
         finiteCloud:closedCloud(z,81,96,.24,.31,1.06),exactTarget:exactTargetWitness(goal)};
}
function fixed720(seed,previous){
 configure(20,12);
 const z=pad(previous,12,11,20,12),data=build(68,96),training=build(68,64),goal=pad(seed,8,8,20,12);
 const g=training.rows.map(row=>gramTarget(jets(training,row,goal),64));
 return lbfgs(data,z,{metricSharp:1150,kw:2.4,gw:3700,kgoal:10.1,wgoal:.8425,hgoal:.62},170,null,g);
}

export {configure,build,jets,gramTarget,evaluate,lbfgs,pad,reproduce192,fixed396,fixed720,chartRecord,physicalObserve,closedCloud,exactTargetWitness};
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href){
 const [op,p,q,r]=process.argv.slice(2);
 if(op==="fit192")writeFileSync(p,JSON.stringify(reproduce192().z)+"\n");
 else if(op==="fit396")writeFileSync(q,JSON.stringify(fixed396(JSON.parse(readFileSync(p))).z)+"\n");
 else if(op==="fit720")writeFileSync(r,JSON.stringify(fixed720(JSON.parse(readFileSync(p)),JSON.parse(readFileSync(q))).z)+"\n");
 else if(op==="observe720")console.log(JSON.stringify(chartRecord(JSON.parse(readFileSync(q)),JSON.parse(readFileSync(p)),20,12),null,2));
 else if(op==="observe192")console.log(JSON.stringify(chartRecord(JSON.parse(readFileSync(p))),null,2));
 else if(op==="observe396")console.log(JSON.stringify(chartRecord(JSON.parse(readFileSync(q)),JSON.parse(readFileSync(p)),12,11),null,2));
 else throw new Error("fit192 OUT | fit396 TARGET192 OUT | observe192 STATE192 | observe396 TARGET192 STATE396 | fit720 TARGET192 PRIOR396 OUT | observe720 TARGET192 STATE720");
}
