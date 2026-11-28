#!/usr/bin/env node
/** Real compact p32 core, genuine phase-designed accumulating second-mode tail and nonlinear spatial continuation. */
import {readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {configure,build,jets,gramTarget,lbfgs} from './2ecf-compact-p32-direct-field.mjs';
import {compactCurvatureCover} from './2ecf-compact-p32-full-curvature.mjs';
import {observeNormal} from './2ecf-compact-p32-normal-meridian-design.mjs';
import {pruferPackets,pruferExtension} from './2ecf-compact-prufer-packet-tail.mjs';
function compactMixedJets(z){
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
 const ip=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),ord=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2],[3,0],[2,1],[1,2],[0,3],[2,2]];
 return function(t,u){
  const C=central(u),B=bern(t),left=B.map(x=>ip(x,vleft)),right=B.map(x=>ip(x,vright)),height=B.map(x=>ip(x,vz)),co=Math.cos(u),si=Math.sin(u),es=[[co,si],[-si,co],[-co,-si],[si,-co]],w=2*t-1,p=t*(1-t),q=1-2*t,a=64*p**3,ap=192*p*p*q,app=384*p*q*q-384*p*p;
  const T=[1,w],D=[0,2],DD=[0,0],DDD=[0,0];for(let k=2;k<nt;k++){T.push(2*w*T[k-1]-T[k-2]);D.push(4*T[k-1]+2*w*D[k-1]-D[k-2]);DD.push(8*D[k-1]+2*w*DD[k-1]-DD[k-2]);DDD.push(12*DD[k-1]+2*w*DDD[k-1]-DDD[k-2]);}
  const R=[T.map(x=>a*x),T.map((x,i)=>ap*x+a*D[i]),T.map((x,i)=>app*x+2*ap*D[i]+a*DD[i]),T.map((x,i)=>384*(q**3-6*p*q)*x+3*app*D[i]+3*ap*DD[i]+a*DDD[i])],cos=[1],sin=[0];for(let m=1;m<=K;m++){cos.push(cos[m-1]*co-sin[m-1]*si);sin.push(sin[m-1]*co+cos[m-1]*si);}
  const Y=Array.from({length:11},(_,i)=>{let [dr,du]=ord[i];return [0,1,2].map(k=>k===2?(du===0?height[dr]:0):left[dr]*C[du][k]+right[dr]*es[du][k]);});
  for(let k=0;k<3;k++)for(let j=0;j<nm;j++){let m=k===2?2*j:2*j+1,ss=k===1,co0=ss?sin[m]:cos[m],co1=m*(ss?cos[m]:-sin[m]),co2=-m*m*co0,b0=0,b1=0,b2=0,b3=0;
   for(let i=0;i<nt;i++){let y=z[(i*3+k)*nm+j];b0+=R[0][i]*y;b1+=R[1][i]*y;b2+=R[2][i]*y;b3+=R[3][i]*y;}
   Y[0][k]+=b0*co0;Y[1][k]+=b1*co0;Y[2][k]+=b0*co1;Y[3][k]+=b2*co0;Y[4][k]+=b1*co1;Y[5][k]+=b0*co2;Y[6][k]+=b3*co0;Y[7][k]+=b2*co1;Y[8][k]+=b1*co2;Y[9][k]-=b0*m*m*co1;Y[10][k]+=b2*co2;}
  return Y;
 };
}

function actualCircleMoment(raw,t){
 let S=0,Sp=0,Spp=0;const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
 for(let i=0;i<64;i++){const y=raw(t,i*Math.PI/32);S+=dot(y[2],y[2])/64;Sp+=2*dot(y[2],y[4])/64;Spp+=2*(dot(y[4],y[4])+dot(y[2],y[7]))/64;}
 const r=Math.sqrt(S);return [1.06*r,1.06*Sp/(2*r),1.06*(Spp/(2*r)-Sp**2/(4*r**3))];}
function packetCompactCore(z,options={}){
 const a=options.left??.54,b=options.right??.77,lambda=1.06,cv=.371,speed=1.272,pi=Math.PI,v=options.adjust??0,initial=options.packetMode??4e-6;
 const raw=options.raw||compactMixedJets(z),pack=options.packet||pruferPackets({cuff:cv,Z:.5724,delta:options.delta??.011,prefix:2,slope:options.slope??8e-6,switch:1,levels:37});
 const mom=options.mom||new Map(),mix=options.radialMix??1;const r=t=>{const linear=[cv+speed*(1-t)+v*(1-t)**3,-speed-3*v*(1-t)**2,6*v*(1-t)];if(!mix)return linear;if(!mom.has(t))mom.set(t,actualCircleMoment(raw,t));const row=mom.get(t);return row.map((v,k)=>mix*v+(1-mix)*linear[k]);};
 const rOut=r(b)[0];const tailCache=new Map();if(rOut<=pack.rout)throw Error('Cut lies in the infinite packet stack');const ext=pruferExtension(pack,initial,rOut,options.mode??-.017,options.sign??1),rows=new Map();
 const orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]],ids=[[0,2,5],[1,4,8],[3,7,10]],depth=b-a;
 function tail(t,u,rd,ad){const [rr,d1,d2]=r(t);let g=tailCache.get(t);if(!g){g=ext.value(rr);if(tailCache.size<100000)tailCache.set(t,g);}let trig=(m,si)=>m===0?(ad===0&&!si?1:0):(si?Math.sin(m*u+ad*pi/2):Math.cos(m*u+ad*pi/2))*m**ad;
  const V=rd===0?[g.r,g.U,g.z,g.f]:rd===1?[d1,d1*g.Ur,d1*g.w,d1*g.fr]:[d2,d1*d1*g.Urr+d2*g.Ur,d1*d1*g.wr+d2*g.w,d1*d1*g.frr+d2*g.fr];
  return [(V[0]*trig(1,0)+V[1]*(.75*trig(1,0)+.25*trig(3,0)))/lambda,(V[0]*trig(1,1)+V[1]*(-.75*trig(1,1)+.25*trig(3,1)))/lambda,(V[2]*trig(0,0)+V[3]*trig(2,0))/lambda];}
 const hor=(p,t)=>p.reduceRight((s,v)=>s*t+v,0),polys=[[0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]],der=p=>p.slice(1).map((v,i)=>v*(i+1)),H=polys.map(p=>[p,der(p),der(der(p))]);
 function jet(t,u){if(t>=b)return orders.map(([rd,ad])=>tail(t,u,rd,ad));const Y=raw(t,u);if(t<=a)return Y.slice(0,6);
  let dif=rows.get(u);if(!dif){const Z=raw(b,u);dif=ids.map((a,rd)=>a.map((id,ad)=>tail(b,u,rd,ad).map((v,k)=>v-Z[id][k])));if(rows.size<3200)rows.set(u,dif);}
  let x=(t-a)/depth;return orders.map(([rd,ad],i)=>{let v=Array.from(Y[i]);for(let j=0;j<3;j++){let k=hor(H[j][rd],x)*depth**(j-rd);for(let axis=0;axis<3;axis++)v[axis]+=k*dif[j][ad][axis];}return v;});}
 return {jet:(p,t,u)=>jet(t,u),one:jet,pack,ext,cut:{a,b,rOut,adjust:v}};
}
function packetFitDesign(z,opts={}){
 const nf=opts.radial??20,na=opts.angle??9,N=opts.N??72,R=opts.R??53,steps=opts.steps??135,ff=packetCompactCore(z,{left:.44,right:.8,mode:-.006,radialMix:1}),end=ff.cut.b;
 const radii=Array.from({length:R},(_,i)=>i/(R-1));
 configure(8,8);const gd=build(R,64,radii,0),g=gd.rows.map(row=>gramTarget(jets(gd,row,z),64));
 configure(nf,na);const data=build(R,N,radii,0),h=end/(nf+3);
 function local(t,j){let x=t/h-j-2,k=Math.abs(x),s=Math.sign(x);if(k>=2)return [0,0,0];return k>1?[h*(2-k)**3/6,-s*(2-k)**2/2,(2-k)/h]:[h*(2/3-k*k+.5*k**3),s*(-2*k+1.5*k*k),(-2+3*k)/h];}
 for(let row of data.rows){row.B=Array.from({length:nf},(_,i)=>local(row.t,i));for(let n=0;n<N;n++)row.base.set(ff.one(row.t,2*Math.PI*n/N).flat(),18*n);}
 const seed=opts.seed??Array(nf*na*3).fill(0),opt={metricSharp:opts.sharp??280,kw:opts.kw??2.6,gw:opts.gw??2500,kgoal:10.24,wgoal:.8423,hgoal:.625};return lbfgs(data,seed,opt,steps,null,g);
}
function packetControlled(z,controls,nf=20,na=9){
 const f=packetCompactCore(z,{left:.44,right:.8,mode:-.006,radialMix:1}),h=f.cut.b/(nf+3),orders=[[0,0],[1,0],[0,1],[2,0],[1,1],[0,2]];
 return {jet(p,t,u){const Y=f.one(t,u);for(let j=Math.max(0,Math.floor(t/h)-3);j<Math.min(nf,Math.floor(t/h)+1);j++){
 let xx=t/h-j-2,k=Math.abs(xx),sg=Math.sign(xx);if(k>=2)continue;let b=k>1?[h*(2-k)**3/6,-sg*(2-k)**2/2,(2-k)/h]:[h*(2/3-k*k+.5*k**3),sg*(-2*k+1.5*k*k),(-2+3*k)/h];
 for(let a=0;a<3;a++)for(let c=0;c<na;c++){let m=a===2?2*c:2*c+1,co=Math.cos(m*u),si=Math.sin(m*u),x=controls[(j*3+a)*na+c],A=a===1?[si,m*co,-m*m*si]:[co,-m*si,-m*m*co];
 for(let i=0;i<6;i++)Y[i][a]+=x*b[orders[i][0]]*A[orders[i][1]];}}return Y;},...{pack:f.pack,ext:f.ext,cut:f.cut}};
}
function packetNative(model,z,nativeAngles=96){
 const raw=compactMixedJets(z),means=new Map(),lambda=1.06,b=model.cut.b,pi=Math.PI,sc=4e-6,ip=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
 function moment(t){if(means.has(t))return means.get(t);let S=0,Q=0,D=0;for(let j=0;j<64;j++){let y=raw(t,j*Math.PI/32);Q+=ip(y[1],y[1])/64;S+=ip(y[2],y[2])/64;D+=ip(y[2],y[4])/64;}let val=[lambda*Math.sqrt(S),lambda*D/Math.sqrt(S),lambda*lambda*Q];means.set(t,val);return val;}
 const K=512,T=Array.from({length:K+1},(_,j)=>b+(1-b)*j/K),rs=T.map(t=>moment(t)[0]);
 function inverse(r){let l=0,h=K;while(h-l>1){let j=(l+h)>>1;if(rs[j]>r)l=j;else h=j;}let t=T[l]+(T[h]-T[l])*(rs[l]-r)/(rs[l]-rs[h]);t=Math.max(b,Math.min(1,t));for(let it=0;it<2;it++){let [rr,dd]=moment(t);t=Math.max(b,Math.min(1,t-(rr-r)/dd));}let v=moment(t);return v[2]/(v[1]*v[1]);}
 const us=Array.from({length:nativeAngles},(_,j)=>(j+.317)*pi/(2*nativeAngles)).concat([0,pi/2]);let rowCount=0,levels=[],maxGuides=Array(7).fill(0),minArea=Infinity,maxBarrier=0;const mark=1.06*raw(0,0)[0][0];
 function check(g,n,peak){let rr=g.r,grr=inverse(rr),far=0;for(let u of us){let c=Math.cos(u),s=Math.sin(u),cc=Math.cos(2*u),ss=Math.sin(2*u),x=.75*c+.25*Math.cos(3*u),y=-.75*s+.25*Math.sin(3*u),xp=-.75*s-.75*Math.sin(3*u),yp=-.75*c+.75*Math.cos(3*u),xpp=-.75*c-2.25*Math.cos(3*u),ypp=.75*s-2.25*Math.sin(3*u);
 let v=[c+sc*g.Ur*x,s+sc*g.Ur*y,g.w+sc*g.fr*cc],w=[-rr*s+sc*g.U*xp,rr*c+sc*g.U*yp,-2*sc*g.f*ss],A=[sc*g.Urr*x,sc*g.Urr*y,g.wr+sc*g.frr*cc],B=[-s+sc*g.Ur*xp,c+sc*g.Ur*yp,-2*sc*g.fr*ss],C=[-rr*c+sc*g.U*xpp,-rr*s+sc*g.U*ypp,-4*sc*g.f*cc],E=ip(v,v),F=ip(v,w),G=ip(w,w),nv=cross(v,w),d=Math.sqrt(ip(nv,nv)),no=nv.map(v=>v/d),l=ip(A,no),m=ip(B,no),nn=ip(C,no),H=(G*l-2*F*m+E*nn)/(2*d*d),K=(l*nn-m*m)/(d*d),k=Math.abs(H)+Math.sqrt(Math.max(0,H*H-K)),e=E/grr-1,f=F/(rr*Math.sqrt(grr)),a=G/(rr*rr)-1,op=Math.abs((e+a)/2)+Math.hypot((e-a)/2,f);
 const P=[rr*c+sc*g.U*x,rr*s+sc*g.U*y,g.z+sc*g.f*cc],ball=Math.hypot(...P),rad=Math.hypot(P[0],P[1]),q=Math.max(0,Math.min(1,(rad-.52)/.02)),allow=.0195*q**3*(10+q*(-15+6*q)),ar=d/(rr*Math.sqrt(grr)),gp=Math.hypot(P[0],P[1]-mark,P[2]),gm=Math.hypot(P[0],P[1]+mark,P[2]);
 const geo=[ball-1.59,P[1]-.885,-P[1]-.885,P[2]-.5724-allow,-P[2]-.5724-allow,.65-gp,.65-gm];for(let i=0;i<7;i++)maxGuides[i]=Math.max(maxGuides[i],geo[i]);minArea=Math.min(minArea,ar);maxBarrier=Math.max(maxBarrier,Math.max(0,(.5/ar)**2-1));peak.metric=Math.max(peak.metric,op);peak.curvature=Math.max(peak.curvature,k);peak.angular=Math.max(peak.angular,Math.abs(a));peak.shear=Math.max(peak.shear,Math.abs(f));rowCount+=14;}}
 for(let cell of model.pack.cells){let peak={n:cell.n,radial:0,metric:0,curvature:0,angular:0,shear:0};
  for(let part of cell.parts)for(let row of part.table)for(let s of [0,.5,1]){let g=model.pack.layerPoint(cell,part,row,row.u+(row.v-row.u)*s);check(g,cell.n,peak);peak.radial++;}levels.push(peak);}
 return {physicalCells:levels.length,firstQuadrantAngularSamples:us.length,rawScalarObservations:rowCount,minimumAreaRatio:minArea,maximumAreaBarrier:maxBarrier,maximumOriginalGuides:maxGuides,globalMetric:Math.max(...levels.map(q=>q.metric)),globalCurvature:Math.max(...levels.map(q=>q.curvature)),first:levels.slice(0,9),last:levels.at(-1)};
}
function trueCuffCoordinate(z){
 const lo=x=>x-1e-13*(1+Math.abs(x)),hi=x=>x+1e-13*(1+Math.abs(x)),n=512,a=2**20;let largest=-Infinity,small=Infinity,cp=[];
 for(let block=12;block<16;block++)compactCurvatureCover(z,8,8,10.305,1,0,0,({radialNode,angularPanel,vector,dot,norm})=>{
  let panels=Array.from({length:17},(_,i)=>angularPanel(Math.min(a-1,i*a/16),20));for(let j=block*n/16;j<(block+1)*n/16;j++){let R=radialNode(j,9),du=0,dl=0,sl=0,sh=0;for(let i=0;i<17;i++){let [u,b]=vector(R.b,panels[i],[[0,1],[1,1]]),wt=(i===0||i===16?2:4)/64,v=dot(u,b),q=norm(u);du=hi(du+wt*v[1]);dl=lo(dl+wt*v[0]);sl=lo(sl+wt*q[0]);sh=hi(sh+wt*q[1]);}
  largest=Math.max(largest,du);small=Math.min(small,dl);if(j===Math.floor(.8*n))cp=[lo(1.06*Math.sqrt(sl)),hi(1.06*Math.sqrt(sh))];}
 });
 return {cover:[.75,1],radialBins:n/4,largestMeanUdotB:largest,minimumMeanUdotB:small,cutRadiusIncludingEntireCell:cp};
}
export {compactMixedJets,actualCircleMoment,packetCompactCore,packetFitDesign,packetControlled,packetNative};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [op,state,out]=process.argv.slice(2),z=JSON.parse(readFileSync(state)),options={left:.44,right:.8,mode:-.006,radialMix:1};
 if(op==='fit540'){const r=packetFitDesign(z);writeFileSync(out,JSON.stringify(r.z)+'\n');console.log(JSON.stringify({training:r.stats,updates:r.hist},null,2));}
 else if(op==='radius')console.log(JSON.stringify(trueCuffCoordinate(z),null,2));
 else if(op==='geometry'){const q=packetCompactCore(z,options);console.log(JSON.stringify({cut:q.cut,outer:q.ext.outer,infiniteApproximation:q.pack.stats()},null,2));}
 else if(op==='native'){console.log(JSON.stringify(packetNative(packetCompactCore(z,options),z),null,2));}
 else if(op==='observe'||op==='observe540'){const q=op==='observe'?packetCompactCore(z,options):packetControlled(z,JSON.parse(readFileSync(out)));console.log(JSON.stringify(['G10a','G10b','G11'].map(x=>observeNormal(q,[],z,x)),null,2));}
 else throw Error('fit540 STATE192 OUT540 | observe STATE192 | observe540 STATE192 STATE540 | native STATE192 | geometry STATE192');
}
