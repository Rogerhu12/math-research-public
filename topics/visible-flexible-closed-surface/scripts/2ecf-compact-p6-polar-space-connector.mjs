#!/usr/bin/env node
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {compactMixedJets} from './2ecf-compact-p32-prufer-physical-annulus.mjs';
import {rayHermite} from './2ecf-compact-p2-two-port-rays.mjs';
import {twistComplete,observeTwist} from './2ecf-space-center-explicit-cauchy-kernel.mjs';
import {steeredReference} from './2ecf-compact-p6-steered-space-center.mjs';
const endZ=.54,dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],norm=a=>Math.sqrt(dot(a,a)),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
function portObservations(field,t,u){const Y=field.jet([],t,u),p=Y[0],x=Y[1],v=Y[2],R=Math.hypot(p[0],p[1]),cross=(a,b)=>a[0]*b[1]-a[1]*b[0],d=(a,b)=>a[0]*b[0]+a[1]*b[1],ph=(a)=>cross(p,a)/(R*R),px=ph(x),pu=ph(v),p2=(a,b,m)=>ph(m)+(cross(b,a)-2*d(p,b)*ph(a))/(R*R),ptt=p2(x,x,Y[3]),ptu=p2(x,v,Y[4]),puu=p2(v,v,Y[5]),ut=-px/pu,utt=-(ptt+2*ut*ptu+ut*ut*puu)/pu,V=x.map((q,k)=>q+ut*v[k]),A=Y[3].map((q,k)=>q+2*ut*Y[4][k]+ut**2*Y[5][k]+utt*v[k]);let phi=Math.atan2(p[1],p[0]);while(phi-u>Math.PI)phi-=2*Math.PI;while(phi-u< -Math.PI)phi+=2*Math.PI;return {r:[R,d(p,V)/R,d(p,A)/R],z:[p[2],V[2],A[2]],phi:[phi,px,ptt],pu,ut,u};}
function polarInterfaces(field,a=.2,b=.8,N=256){let arr=[];for(let t of [a,b]){let byU=Array.from({length:N},(_,j)=>portObservations(field,t,2*Math.PI*j/N)),byPhi=[];for(let j=0;j<N;j++){let phi=2*Math.PI*j/N,u=phi,q;for(let k=0;k<12;k++){q=portObservations(field,t,u);let d=q.phi[0]-phi;if(Math.abs(d)<2e-14)break;u-=d/q.pu;}if(Math.abs(q.phi[0]-phi)>1e-9||q.pu<.03)throw Error('polar inverse');byPhi.push(q);}arr.push({byU,byPhi,t});}return arr;}
function polarChart(ends,c=.28,opts={}){
 const [left,right]=ends,N=left.byU.length,a=left.t,b=right.t,L=b-a,pi=Math.PI,tw=2*pi,degree=opts.degree??16,rd=opts.radiusDegree??9,co=opts.coeffs??Array((rd-5)*5).fill(0);
 function avg(x,j){const v=[1];for(let i=1;i<=j;i++){v.push(0);for(let k=i;k>=0;k--)v[k]=(1-x)*v[k]+x*(v[k-1]||0);}return v;}
 function interpol(table,angle){let idx=angle*N/tw,p=Math.floor(idx),q=idx-p,lo=p-2,results=Array(table[0].length).fill(0);for(let i=0;i<6;i++){let c=1;for(let k=0;k<6;k++)if(k!==i)c*=(q+2-k)/(i-k);let row=table[((lo+i)%N+N)%N];for(let h=0;h<row.length;h++)results[h]+=row[h]*c;}return results;}
 const table=[left,right].map(o=>o.byPhi.map(p=>[...p.r,...p.z.map((x,i)=>x-c*p.r[i])])),angles=[left,right].map(o=>o.byU.map(p=>[p.phi[0]-p.u,p.phi[1],p.phi[2]]));
 const cache=new Map();function position(t,u){let W=cache.get(t),q=(t-a)/L;if(!W){let T=avg(q,degree+1),rt=avg(q,rd);W=[T,rt];if(cache.size<12000)cache.set(t,W);}let [T,rt]=W,A=interpol(angles[0],u),B=interpol(angles[1],u),angle=u+rayHermite(A,B,L,q,0),v=interpol(table[0],angle),w=interpol(table[1],angle),la=[v[3],v[4],v[5]],ra=[w[3],w[4],w[5]],d=degree,d0=la[1],d1=d0+L*la[2]/d,dn=ra[1],de=dn-L*ra[2]/d,mid=((d+1)*(ra[0]-la[0])/L-d0-d1-dn-de)/(d-3);let ww=la[0],delta=0;
 for(let i=0;i<=d+1;i++){if(i)delta+=L/(d+1)*(i===1?d0:i===2?d1:i===d?de:i===d+1?dn:mid);ww+=T[i]*delta;}
 let up=[v[0],v[0]+L*v[1]/rd,v[0]+2*L*v[1]/rd+L*L*v[2]/(rd*(rd-1))],down=[w[0],w[0]-L*w[1]/rd,w[0]-2*L*w[1]/rd+L*L*w[2]/(rd*(rd-1))],r=0;
 for(let i=0;i<=rd;i++){let g;if(i<3)g=up[i];else if(i>rd-3)g=down[rd-i];else{let x=i/rd,offset=0,k=i-3;for(let j=0;j<5;j++)offset+=co[k*5+j]*[1,Math.cos(angle),Math.sin(angle),Math.cos(2*angle),Math.sin(2*angle)][j];g=(1-x)*v[0]+x*w[0]+offset;}r+=rt[i]*g;}return [r*Math.cos(angle),r*Math.sin(angle),ww+c*r];}
 return {position,N,a,b,c};}
function buildPolarResidual(original,chart,opt={}){const {a,b}=chart,P=opt.P??56,N=opt.N??256,M=opt.M??104,pi=Math.PI,K=2*M+1,grid=Array.from({length:P+1},(_,i)=>a+(b-a)*i/P),data=grid.map(()=>Array.from({length:3},()=>new Float64Array(3*K))),dh=1.2e-5,angles=Array.from({length:N},(_,j)=>{let u=2*pi*j/N;return Array.from({length:K},(_,k)=>k===0?1/N:(2/N)*(k%2?Math.cos(((k+1)>>1)*u):Math.sin((k>>1)*u)));});
 for(let i=1;i<P;i++){let t=grid[i],row=data[i];for(let j=0;j<N;j++){let u=2*pi*j/N,ref=original.jet([],t,u),q=chart.position(t,u),qm=chart.position(t-dh,u),qp=chart.position(t+dh,u),D=q.map((x,k)=>[x-ref[0][k],(qp[k]-qm[k])/(2*dh)-ref[1][k],(qp[k]+qm[k]-2*x)/(dh*dh)-ref[3][k]]);for(let c=0;c<3;c++)for(let k=0;k<K;k++)for(let v=0;v<3;v++)row[v][c*K+k]+=D[c][v]*angles[j][k];}}
 return {a,b,M,times:grid,controls:data.map(r=>r.map(v=>Array.from(v))),P,N};}
function polarComplete(original,f){const {a,b,M,times,controls,P}=f,K=2*M+1,cache=new Map(),ang=new Map(),ord=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];return {jet(_,t,u){let Y=original.jet([],t,u);if(t<=a||t>=b)return Y;let V=cache.get(t);if(!V){let j=Math.min(P-1,Math.max(0,Math.floor((t-a)*P/(b-a)))),h=times[j+1]-times[j],x=(t-times[j])/h;V=Array.from({length:3},(_,d)=>Array.from({length:3*K},(_,k)=>rayHermite(controls[j].map(q=>q[k]),controls[j+1].map(q=>q[k]),h,x,d)));if(cache.size<3500)cache.set(t,V);}
 let A=ang.get(u);if(!A){A=Array.from({length:K},(_,j)=>{if(!j)return [1,0,0];let m=(j+1)>>1,c=Math.cos(m*u),s=Math.sin(m*u);return j%2?[c,-m*s,-m*m*c]:[s,m*c,-m*m*s];});if(ang.size<5000)ang.set(u,A);}for(let i=0;i<6;i++)for(let c=0;c<3;c++){let y=0;for(let k=0;k<K;k++)y+=V[ord[i][0]][c*K+k]*A[k][ord[i][1]];Y[i][c]+=y;}return Y;}};}
function linearRow(row,z){let Y=Float64Array.from(row.base);for(let j=0;j<z.length;j++){let v=z[j];if(v===0)continue;let A=row.delta[j];for(let k=0;k<Y.length;k++)Y[k]+=v*A[k];}return Y;}
function polarDirections(chart,degree=9,modes=4){const K=2*modes+1,dim=2*(degree-5)*K;function dir(t,u){const P=chart.position(t,u),r=Math.hypot(P[0],P[1]),x=(t-chart.a)/(chart.b-chart.a),q=1-x,ax=[P[0]/r,P[1]/r,chart.c],w=[0,0,1],A=[1],V=[];for(let k=1;k<=modes;k++)A.push(Math.cos(k*u),Math.sin(k*u));let bin=1;for(let j=0;j<=degree;j++){if(j>=3&&j<=degree-3){let h=bin*x**j*q**(degree-j);for(let e of [ax,w])for(let v of A)V.push(e.map(c=>h*v*c));}if(j<degree)bin*= (degree-j)/(j+1);}return [P,...V];}
 function actual(z){return {...chart,position(t,u){let a=dir(t,u),p=a[0].slice();for(let j=0;j<z.length;j++)for(let k=0;k<3;k++)p[k]+=z[j]*a[j+1][k];return p;}};}
 return {dir,actual,dim};}
function polarDesign(z,chart,opt={}){const {dir,actual,dim}=polarDirections(chart,opt.degree??9,opt.modes??4),R=opt.R??49,N=opt.N??64,ht=1.7e-5,hu=3.1e-5,raw=compactMixedJets(z),rows=[],g=[];
 for(let j=0;j<R;j++){let t=chart.a+(chart.b-chart.a)*j/(R-1),m=new Float64Array(18*N),delta=Array.from({length:dim},()=>new Float64Array(18*N)),Q=0,S=0;for(let i=0;i<64;i++){let p=raw(t,2*Math.PI*i/64);Q+=dot(p[1],p[1])/64;S+=dot(p[2],p[2])/64;}g.push([Q,S]);for(let i=0;i<N;i++){let u=2*Math.PI*i/N,a=dir(t,u),b=dir(t+ht,u),c=dir(t-ht,u),d=dir(t,u+hu),e=dir(t,u-hu),f=dir(t+ht,u+hu),h=dir(t+ht,u-hu),k=dir(t-ht,u+hu),l=dir(t-ht,u-hu);
 for(let v=0;v<=dim;v++){let row=v?delta[v-1]:m;for(let x=0;x<3;x++){let p=18*i+x;row[p]=a[v][x];row[p+3]=(b[v][x]-c[v][x])/(2*ht);row[p+6]=(d[v][x]-e[v][x])/(2*hu);row[p+9]=(b[v][x]+c[v][x]-2*a[v][x])/(ht*ht);row[p+12]=(f[v][x]-h[v][x]-k[v][x]+l[v][x])/(4*ht*hu);row[p+15]=(d[v][x]+e[v][x]-2*a[v][x])/(hu*hu);}}}rows.push({base:m,delta,t});}return {N,R,rows,g,dim,actual};}
function polarObjective(data,z,o={},external=null){ const dim=data.dim;
 let grad=new Float64Array(dim),cost=0,metric=0,curvature=0,held=Infinity,diamHalf=0,width=0,height=0,area=Infinity,guide=Array(7).fill(0),bad=false;
 let metricSharp=o.metricSharp??9,kgoal=o.kgoal??9.5,kw=o.kw??.3,gw=o.gw??200,baseCost=0,metricAt=[],curvAt=[];
 const deriv=o.deriv!==false, N=data.N,R=data.R;
 for(let i=0;i<R;i++){const row=data.rows[i],Y=linearRow(row,z);
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
   const rr=norm(P),rp=Math.hypot(P[0],P[1]-(301/225),P[2]),rm=Math.hypot(P[0],P[1]+(301/225),P[2]),cyl=Math.hypot(P[0],P[1]),l=Math.max(0,Math.min(1,(cyl-.52)/.02)),allow=.0195*l**3*(10+l*(-15+6*l)),allowR=.0195*30*(l*(1-l))**2/.02;
   held=Math.min(held,rp,rm);diamHalf=Math.max(diamHalf,rr);width=Math.max(width,Math.abs(P[1]));height=Math.max(height,Math.abs(P[2]));
   const signed=[rr-1.59,P[1]-(o.wgoal??.885),-P[1]-(o.wgoal??.885),P[2]-endZ-allow,-P[2]-endZ-allow,(o.hgoal??.65)-rp,(o.hgoal??.65)-rm];
   for(let j=0;j<7;j++){const v=signed[j];guide[j]=Math.max(guide[j],v);if(v<=0)continue;cost+=gw*v*v;
    if(deriv){const w=2*gw*v, gg=j===0?P.map(xx=>xx/rr):j===1?[0,1,0]:j===2?[0,-1,0]:j===3||j===4?[-allowR*P[0]/cyl,-allowR*P[1]/cyl,j===3?1:-1]:[-P[0]/(j===5?rp:rm),-(P[1]+(j===5?-(301/225):(301/225)))/(j===5?rp:rm),-P[2]/(j===5?rp:rm)]; for(let k=0;k<3;k++)bar[p+k]+=w*gg[k];}
   }
  }
  if(!deriv)continue;
  if(!external)for(let n=0;n<N;n++)for(let k=0;k<3;k++){const p=n*18;bar[p+3+k]+=2*accQ/N*Y[p+3+k];bar[p+6+k]+=2*accS/N*Y[p+6+k];}
  for(let j=0;j<dim;j++){const A=row.delta[j];let v=0;for(let k=0;k<A.length;k++)v+=bar[k]*A[k];grad[j]+=v;}
 }
 const scale=1/(R*N);cost*=scale;for(let j=0;j<dim;j++)grad[j]*=scale;
 return {cost:bad?Infinity:cost,grad,metric,curvature,held,diamHalf,width,height,area,guide,metricAt,curvAt};
}
function fitStats(f){let {grad,...rest}=f;return rest;}
function fitInner(a,b){let v=0;for(let i=0;i<a.length;i++)v+=a[i]*b[i];return v;}
function polarFitSteps(data,z,options,iterations,mem=null,external=null){const dim=data.dim;
 z=Float64Array.from(z);let r=polarObjective(data,z,options,external),hist=[],stash=mem??[];for(let it=0;it<iterations;it++){
  let d=Float64Array.from(r.grad),alpha=[];
  for(let k=stash.length-1;k>=0;k--){let [s,y,sy]=stash[k],v=fitInner(s,d)/sy;alpha[k]=v;for(let j=0;j<dim;j++)d[j]-=v*y[j];}
  let init=stash.length?stash.at(-1)[2]/fitInner(stash.at(-1)[1],stash.at(-1)[1]):.015;
  for(let j=0;j<dim;j++)d[j]*=init;
  for(let k=0;k<stash.length;k++){let [s,y,sy]=stash[k],v=fitInner(y,d)/sy;for(let j=0;j<dim;j++)d[j]+=s[j]*(alpha[k]-v);}
  let descent=fitInner(d,r.grad);if(descent<=0){d=Float64Array.from(r.grad);descent=fitInner(d,r.grad);stash=[];}
  let step=1,next,newz,ok=false;
  for(let tr=0;tr<18;tr++){newz=z.map((v,j)=>v-step*d[j]);next=polarObjective(data,newz,{...options,deriv:false},external);
   if(next.cost<r.cost-1e-4*step*descent){ok=true;break;}step/=2;}
  if(!ok){hist.push({stopped:true,step});break;}
  next=polarObjective(data,newz,options,external);let s=Array.from(newz,(v,j)=>v-z[j]),y=Array.from(next.grad,(v,j)=>v-r.grad[j]),sy=fitInner(s,y);
  if(sy>1e-12*Math.sqrt(fitInner(s,s)*fitInner(y,y))){stash.push([s,y,sy]);if(stash.length>10)stash.shift();}
  z=newz;r=next;if((it+1)%10===0)hist.push([it+1,r.cost,r.metric,r.curvature,r.held]);
 }
 return {z:Array.from(z),stats:fitStats(r),hist,mem:stash};
}

export {polarInterfaces,polarChart,polarDirections,polarDesign,polarFitSteps,polarComplete,buildPolarResidual};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,p540,field,coeff,out,ampl]=process.argv.slice(2),read=x=>JSON.parse(readFileSync(x)),z=read(state),p=read(p540),d=read(field),A=Number(ampl??.18),m=twistComplete(z,p,d,steeredReference(z,p,A,13/128));
 if(op==='observe'){let f=polarComplete(m,read(coeff));console.log(JSON.stringify(['G10a','G10b','G11'].map(g=>observeTwist(f,[],z,g)),null,2));}
 else {const ends=polarInterfaces(m,.2,.8,256),chart=polarChart(ends,.28);
 if(op==='fit'){const d=polarDesign(z,chart,{R:49,N:64,modes:4}),opt={metricSharp:60,kw:3,gw:1600,kgoal:10,wgoal:.839,hgoal:.615},r=polarFitSteps(d,Array(d.dim).fill(0),opt,115,null,d.g);writeFileSync(coeff,JSON.stringify(r.z)+'\n');console.log(JSON.stringify({hist:r.hist,stats:r.stats}));}
 else if(op==='field'){const actual=coeff==='zero'?chart:polarDirections(chart).actual(read(coeff)),f=buildPolarResidual(m,actual,{P:56,N:256,M:104});writeFileSync(out,JSON.stringify(f)+'\n');}
 else throw Error('fit STATE192 STATE540 P6FIELD COEFF | field STATE192 STATE540 P6FIELD COEFF/zero POLARFIELD | observe STATE192 STATE540 P6FIELD POLARFIELD');}}
