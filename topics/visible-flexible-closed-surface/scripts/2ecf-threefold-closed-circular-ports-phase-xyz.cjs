const P=2*Math.PI/3,U=P/2,etaMax=.41,loLen=.915,hiLen=1.09,tau=(P-loLen-hiLen)/2,kl=.35,kh=(P-kl*(loLen+tau))/(hiLen+tau),a0=loLen/2,a1=a0+tau;
const C=Math.cos,S=Math.sin,H=Math.hypot;
function bc(n,k){let y=1;for(let j=0;j<k;j++)y*= (n-j)/(j+1);return y}
function B(n,x,c){let v=0;for(let i=0;i<=n;i++)v+=bc(n,i)*x**i*(1-x)**(n-i)*c(i);return v}
function kin(u){if(u<=a0)return [kl,kl*u];if(u>=a1)return [kh,kl*u+(kh-kl)*(u-a1+tau/2)];let x=(u-a0)/tau;return [kl+(kh-kl)*B(15,x,i=>i>=8?1:0),kl*u+(kh-kl)*tau*B(16,x,i=>Math.max(0,i-8)/16)]}
function rotate(p,a){return [C(a)*p[0]-S(a)*p[1],S(a)*p[0]+C(a)*p[1]]}
const n=4096,gs=[0],gc=[0];
for(let i=0;i<n;i++){const x=U*(i+.5)/n,b=kin(x)[1];gs.push(gs[i]+U/n*S(b));gc.push(gc[i]+U/n*C(b))}
const A=gs[n]+gc[n]/Math.tan(U),Bhigh=gc[n]/S(U);
function base(u){let j=Math.floor((u+U)/P),local=u-j*P,sign=local>=0?1:-1,v=Math.abs(local),h=Math.min(n-1,Math.floor(v/U*n)),t=v/U*n-h,dx=gs[h]+(gs[h+1]-gs[h])*t,dy=gc[h]+(gc[h+1]-gc[h])*t,[k,b]=kin(v),be=j*P+sign*b;return {p:rotate([A-dx,sign*dy],j*P),N:[C(be),S(be)],T:[-S(be),C(be)],k,be}}

function ring(q,n=512){const qint=(fun,u)=>{let k=Math.floor(u/U*n),v=u/U*n-k;let a=fun[Math.min(n,k)],b=fun[Math.min(n,k+1)];return a*(1-v)+b*v};let ix=[0],iy=[0],dx=[0],dy=[0],d2x=[0],d2y=[0];
 for(let j=0;j<n;j++){const u=(j+.5)*U/n,delta=kin(u)[1]-u,th=u+q*delta,sn=S(th),cs=C(th),h=U/n;
   ix.push(ix[j]+h*sn);iy.push(iy[j]+h*cs);
   dx.push(dx[j]+h*cs*delta);dy.push(dy[j]-h*sn*delta);
   d2x.push(d2x[j]-h*sn*delta**2);d2y.push(d2y[j]-h*cs*delta**2)}
 const A=ix[n]+iy[n]/Math.tan(U),Aq=dx[n]+dy[n]/Math.tan(U),Aqq=d2x[n]+d2y[n]/Math.tan(U);
 return function(u){let h=Math.floor((u+U)/P),z=u-h*P,sg=z<0?-1:1,t=Math.abs(z),[k,b]=kin(t),delta=sg*(b-t),theta=u+q*delta,N=[C(theta),S(theta)],T=[-S(theta),C(theta)];
 return {p:rotate([A-qint(ix,t),sg*qint(iy,t)],h*P),pq:rotate([Aq-qint(dx,t),sg*qint(dy,t)],h*P),pqq:rotate([Aqq-qint(d2x,t),sg*qint(d2y,t)],h*P),k:1+q*(k-1),delta,N,T}}
}

const Lc=.68,Rc=.97;
function radial(t,n){const x=2*t-1,b=64*t**3*(1-t)**3,bp=192*t*t*(1-t)*(1-t)*(1-2*t),p=[1],d=[0];if(n>1){p.push(x);d.push(2)}for(let j=2;j<n;j++){p[j]=((2*j-1)*x*p[j-1]-(j-1)*p[j-2])/j;d[j]=((2*j-1)*(2*p[j-1]+x*d[j-1])-(j-1)*d[j-2])/j}return [p.map(y=>y*b),p.map((y,i)=>(d[i]*b+y*bp)/Lc)]}
function modes(u,n){let v=[1],d=[0];for(let i=1;i<=n;i++){let j=3*i;v.push(C(j*u),S(j*u));d.push(-j*S(j*u),j*C(j*u))}return [v,d]}
function shell(v,nu){let t=v,q=1-t**3*(10-15*t+6*t*t),qd=-30*t*t*(1-t)**2/Lc,f=Rc+(1-Rc)*q,df=(1-Rc)*qd,rs=ring(q,nu);return (u,p)=>{let {p:x,pq,T}=rs(u-p),V=rotate(x.map((v,i)=>df*v+f*qd*pq[i]),p-u),W=rotate(T.map(y=>y*f),p-u);return [V[0],V[1],1,W[0],W[1],0]}}
function sample(phase,nr,na,ns,nt,shift,reference=etaMax){const cells=[],nang=na*2+1,nvar=nr*nang*3;for(let j=0;j<ns;j++){const t=(j+shift)/ns, m=radial(t,nr), f=shell(t,1024);
 for(let i=0;i<nt;i++){const u=(i+shift)*P/nt, n=modes(u,na),S0=f(u,reference),S1=f(u,phase),E=1+S0[0]**2+S0[1]**2,F=S0[0]*S0[3]+S0[1]*S0[4],G=S0[3]**2+S0[4]**2;
 let A=1/Math.sqrt(E),B=1/Math.sqrt(G-F**2/E),Ccoef=F/E,vs=new Float64Array(nr*nang),us=new Float64Array(nr*nang),uval=new Float64Array(nr*nang);
 for(let v=0;v<nr;v++)for(let h=0;h<nang;h++){let z=v*nang+h,w=m[0][v]*n[0][h];vs[z]=m[1][v]*n[0][h];us[z]=m[0][v]*n[1][h];uval[z]=w}
 cells.push({S1,A,B,Ccoef,vs,us,uval})}}
 return {cells,nvar,nr,na,ns,nt}}
function evalState(grid,x,useJ=false){let no=grid.nvar,nx=no/3,nrow=3*grid.cells.length,J=useJ?new Float64Array(nrow*no):null,r=new Float64Array(nrow),mx=0,obj=0,ds=new Float64Array(no);
 for(let k=0;k<grid.cells.length;k++){let {S1,A,B,Ccoef:C0,vs,us,uval}=grid.cells[k];let [vx,vy,vz,wx,wy,wz]=S1;
 for(let i=0;i<nx;i++){let sx=vs[i],ux=us[i],h=uval[i],cx=x[3*i],cy=x[3*i+1],cz=x[3*i+2];
 vx+=sx*cx;vy+=sx*cy;vz+=sx*cz;wx+=ux*cx-h*cy;wy+=ux*cy+h*cx;wz+=ux*cz}
 wx=B*(wx-C0*vx);wy=B*(wy-C0*vy);wz=B*(wz-C0*vz);vx*=A;vy*=A;vz*=A;
 let e=vx*vx+vy*vy+vz*vz-1,b=vx*wx+vy*wy+vz*wz,g=wx*wx+wy*wy+wz*wz-1;
 r[3*k]=e;r[3*k+1]=Math.SQRT2*b;r[3*k+2]=g;obj+=e*e+2*b*b+g*g;mx=Math.max(mx,Math.abs((e+g)/2)+H((e-g)/2,b));
 if(!useJ)continue;
 let v=[vx,vy,vz],w=[wx,wy,wz],tv=[vy,-vx,0],tw=[wy,-wx,0];for(let i=0;i<nx;i++){let v1=A*vs[i],u1=B*(us[i]-C0*vs[i]),d=B*uval[i];for(let j=0;j<3;j++){let id=3*i+j,je=2*v[j]*v1,jf=Math.SQRT2*(v1*w[j]+v[j]*u1+d*tv[j]),jg=2*(w[j]*u1+d*tw[j]);J[(3*k)*no+id]=je;J[(3*k+1)*no+id]=jf;J[(3*k+2)*no+id]=jg;ds[id]+=je*je+jf*jf+jg*jg}}}
 return {obj:obj/grid.cells.length,mx,J,r,ds}}
function direction(y,n,damp,cgit){const {J,r,ds}=y,m=r.length,diag=Float64Array.from(ds,v=>1/Math.sqrt(v+.01));let b=new Float64Array(n);
 for(let i=0;i<m;i++){let k=i*n,t=-r[i];for(let j=0;j<n;j++){J[k+j]*=diag[j];b[j]+=J[k+j]*t}}
 const dot=(a,b)=>{let v=0;for(let i=0;i<a.length;i++)v+=a[i]*b[i];return v};let d=b.slice(),h=b.slice(),x=new Float64Array(n),v=dot(h,h),tmp=new Float64Array(m),o=new Float64Array(n);for(let it=0;it<cgit;it++){
 o.fill(0);for(let i=0;i<m;i++){let s=0,k=i*n;for(let j=0;j<n;j++)s+=J[k+j]*d[j];tmp[i]=s;for(let j=0;j<n;j++)o[j]+=J[k+j]*s}for(let j=0;j<n;j++)o[j]+=damp*d[j];const denom=dot(d,o);if(denom<=0)break;const a=v/denom;for(let j=0;j<n;j++){x[j]+=a*d[j];h[j]-=a*o[j]}const vv=dot(h,h);if(vv<=1e-18)break;for(let j=0;j<n;j++)d[j]=h[j]+vv/v*d[j];v=vv}return Float64Array.from(x,(v,i)=>v*diag[i])}
function optimize(phase,nr,na,ns,nt,start,its=5,cgit=34){const g=sample(phase,nr,na,ns,nt,.5),o=sample(phase,nr,na,ns+7,nt+13,.271);
 let x=Float64Array.from(start||new Array(g.nvar).fill(0)),history=[],damp=.006;
 for(let i=0;i<its;i++){const y=evalState(g,x,true),h=direction(y,g.nvar,damp,cgit);let accept=false;for(let l of [1,.5,.25,.125,.0625]){let xc=Float64Array.from(x,(v,i)=>v+l*h[i]),e=evalState(g,xc);if(e.obj<y.obj){const obs=evalState(o,xc);history.push([i+1,l,y.obj,e.obj,y.mx,e.mx,obs.mx]);x=xc;damp=Math.max(.0002,damp*.45);accept=true;break}}if(!accept){damp*=5;history.push([i+1,0,y.obj,y.obj,y.mx])}}
 return {phase,nr,na,ns,nt,history,x:Array.from(x)}}

function secondBases(t,n,u,nmode){let x=2*t-1,p=[1,x],d=[0,2],e=[0,0];
 for(let i=2;i<n;i++){p[i]=((2*i-1)*x*p[i-1]-(i-1)*p[i-2])/i;d[i]=((2*i-1)*(2*p[i-1]+x*d[i-1])-(i-1)*d[i-2])/i;e[i]=((2*i-1)*(4*d[i-1]+x*e[i-1])-(i-1)*e[i-2])/i}
 let z=64*t**3*(1-t)**3,z1=192*t*t*(1-t)**2*(1-2*t),z2=384*t*(1-t)*((1-2*t)**2-t*(1-t)),v=[],b=[],a=[];for(let i=0;i<n;i++){v.push(z*p[i]);b.push((z1*p[i]+z*d[i])/Lc);a.push((z2*p[i]+2*z1*d[i]+z*e[i])/Lc**2)}
 let [m,m1]=modes(u,nmode),m2=m.map((y,i)=>-((3*Math.ceil(i/2))**2)*y);return [v,b,a,m,m1,m2]}
function curvatureActual(phase,xx,nr,na,ns,nt){let peak=0,min=1e3,disp=0;
 for(let j=0;j<ns;j++){let t=(j+.371)/ns,q=1-t**3*(10-15*t+6*t*t),qd=-30*t*t*(1-t)**2/Lc,ddq=-60*t*(1-t)*(1-2*t)/Lc**2,f=Rc+(1-Rc)*q,df=(1-Rc)*qd,ddf=(1-Rc)*ddq,rs=ring(q,1024);
 for(let i=0;i<nt;i++){let u=(i+.271)*P/nt,{p,pq,pqq,k,delta,N,T}=rs(u-phase),dir=phase-u;
 const turn=z=>[...rotate(z,dir),0];
 let v=turn(p.map((x,k)=>df*x+f*qd*pq[k])),w=turn(T.map(x=>f*x)),vv=turn(p.map((x,k)=>ddf*x+(2*df*qd+f*ddq)*pq[k]+f*qd**2*pqq[k])),vw=turn(T.map((x,k)=>df*x-f*qd*delta*N[k])),ww=turn(N.map(x=>-f*k*x)),dpos=[0,0,0];v[2]=1;
 let [a,b,c,h,g,hh]=secondBases(t,nr,u,na);
 for(let l=0;l<nr;l++)for(let m=0;m<h.length;m++){let id=3*(l*h.length+m),X=[xx[id],xx[id+1],xx[id+2]],rot=[-X[1],X[0],0],rr=[-X[0],-X[1],0];
 for(let h0=0;h0<3;h0++){const z=X[h0],rz=rot[h0],r2z=rr[h0],ang=g[m]*z+h[m]*rz;dpos[h0]+=a[l]*h[m]*z;v[h0]+=b[l]*h[m]*z;w[h0]+=a[l]*ang;vv[h0]+=c[l]*h[m]*z;vw[h0]+=b[l]*ang;ww[h0]+=a[l]*(hh[m]*z+2*g[m]*rz+h[m]*r2z)}}
 const dot=(a,b)=>a.reduce((z,x,k)=>z+x*b[k],0),n=[v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0]],area=H(...n);min=Math.min(min,area);const E=dot(v,v),F=dot(v,w),G=dot(w,w),l=dot(n,vv)/area,m=dot(n,vw)/area,k0=dot(n,ww)/area,half=(G*l-2*F*m+E*k0)/(2*area**2),kg=(l*k0-m*m)/area**2;peak=Math.max(peak,Math.abs(half)+Math.sqrt(Math.max(0,half**2-kg)));disp=Math.max(disp,H(...dpos))
 }}return {peak,min,disp}}

function quadSmooth(fn,top,n=80) {
  let v=0;
  for(let j=0;j<n;j++){
    let t=Math.PI*(j+.5)/(2*n),u=top*Math.sin(t)**2;
    v+=fn(u)*top*Math.PI*Math.sin(t)*Math.cos(t)/n;
  }
  return v;
}
const rootR=.115,plate=.233,flat=.234,delta=.004,tube=plate-rootR*(1+delta*Math.PI/2);
const tipJ=quadSmooth(t=>Math.sqrt(Math.sin(t)),Math.PI/2,320),tipG=(tube-rootR)/tipJ;
const specs=[[1.37,.24,.90,'short'],[-1.33,.24,.28,'s5']];
function turnAngle(t,w,law) {
  if(law==='s5')return w*t**3*(10+t*(-15+6*t));
  const e=.05;
  if(t<e){let v=t/e;return w*e*v**3*(1-v/2)/(1-e)}
  if(t>1-e){let v=(1-t)/e;return w*(1-e-e*v**3*(1-v/2))/(1-e)}
  return w*(t-e/2)/(1-e);
}
function actualRings(spec,n=44) {
  const [omega,first,last,law]=spec,bend=law==='short'?.43:.78,rows=[];
  for(let j=0;j<=n;j++){
    const t=Math.PI*j/(2*n),extra0=j===n?Math.PI/2:quadSmooth(x=>Math.cos(x)/Math.sqrt(Math.sin(2*x)),t),
      extra1=j===n?Math.PI/2:quadSmooth(x=>Math.sin(x)/Math.sqrt(Math.sin(2*x)),t);
    rows.push(j===0?[0,0,plate,0]:[rootR*(1-C(t)+delta*extra1),0,plate-rootR*(S(t)+delta*extra0),0]);
  }
  const y0=rootR*(1+delta*Math.PI/2);
  for(let j=1;j<=n;j++)rows.push([y0+first*j/n,0,tube,0]);
  let y=y0+first,z=0;
  for(let j=0;j<n;j++){
    for(let k=0;k<16;k++){let u=(j+(k+.5)/16)/n,b=turnAngle(u,omega,law);y+=bend*C(b)/(16*n);z+=bend*S(b)/(16*n)}
    rows.push([y,z,tube,turnAngle((j+1)/n,omega,law)]);
  }
  for(let j=1;j<=n;j++)rows.push([y+last*j/n*C(omega),z+last*j/n*S(omega),tube,omega]);
  y+=last*C(omega);z+=last*S(omega);
  for(let j=1;j<=n;j++){
    const t=Math.PI*j/(2*n),d=rootR*S(t)+2*tipG*Math.sqrt(S(t));
    const rr=j===n?0:tube-rootR*(1-C(t))-tipG*quadSmooth(x=>Math.sqrt(S(x)),t,200);
    rows.push([y+d*C(omega),z+d*S(omega),rr,omega]);
  }
  return rows;
}
function bevel(i,x) {
  const k=i?kh:kl,w=i?.31:.249,dx=w-flat,e=dx/20,c=k*(w/dx-.025)/.95;
  const old=u=>-k*u*u/(1+Math.sqrt(1-(k*u)**2));
  if(Math.abs(x)>=w)return old(Math.abs(x));
  const a=Math.max(flat,Math.abs(x)),limits=[a,...[flat+e,w-e].filter(y=>y>a),w];
  let s=old(w);
  for(let j=1;j<limits.length;j++){
    const h=(limits[j]-limits[j-1])/32;
    for(let t=0;t<32;t++){
      const u=limits[j-1]+(t+.5)*h;let y;
      if(u<flat+e){let v=(u-flat)/e;y=c*e*v**3*(1-v/2)}
      else if(u<w-e)y=c*(u-flat-e/2);
      else{let v=(u-w+e)/e;y=c*(dx-1.5*e)+e*(c*v+(k-c)*v**3*(1-v/2))}
      s+=h*y/Math.sqrt(1-y*y);
    }
  }
  return s;
}
const flatH=[bevel(0,0),bevel(1,0)];
function frame(i,p) {
  let k=i?kh:kl,angle=i*Math.PI,ray=i?Bhigh:A,be=angle+k*(etaMax/2-p)+p;
  const n=[C(be),S(be)],t=[-S(be),C(be)],o=rotate([(ray-1/k)*C(angle),(ray-1/k)*S(angle)],p);
  return {n,t,o:[o[0]+n[0]/k,o[1]+n[1]/k]};
}
function holding(x,phase){
  const a=frame(1,phase),dx=x[0]-a.o[0],dy=x[1]-a.o[1];
  return [dx*a.n[0]+dy*a.n[1],dx*a.t[0]+dy*a.t[1],x[2]];
}
function physicalCloud(phase,coeff,ns=54,nu=192) {
  const points=[],arms=[],ports=[frame(0,phase),frame(1,phase)];
  for(let j=0;j<nu;j++){
    const u=2*Math.PI*j/nu,p0=rotate(base(u-phase).p,phase);
    const entries=ports.map((_,i)=>{
      let off=u-etaMax/2-i*Math.PI;
      off-=2*Math.PI*Math.round(off/(2*Math.PI));
      const k=i?kh:kl,w=i?.31:.249,x=S(k*off)/k;
      if(Math.abs(off)>Math.asin(k*w)/k)return null;
      return {x,H:bevel(i,x),h:-k*x*x/(1+Math.sqrt(1-(k*x)**2))};
    });
    for(let s=0;s<=ns;s++){
      const z=.78*(2*s/ns-1);let p=[...p0,z],include=true;
      for(let i=0;i<2;i++){let a=entries[i];if(!a)continue;
        if(a.x*a.x+z*z<plate*plate)include=false;
        const f=ports[i],v=Math.max(0,Math.min(1,(.77-Math.abs(z))/.30)),w=v**3*(10+v*(-15+6*v)),h=a.h+w*(a.H-a.h);
        p=[f.o[0]+a.x*f.t[0]+h*f.n[0],f.o[1]+a.x*f.t[1]+h*f.n[1],z];
      }
      if(include)points.push(p);
    }
  }
  for(let j=0;j<=ns;j++){
    const t=j/ns,q=1-t**3*(10-15*t+6*t*t),f=Rc+(1-Rc)*q,rs=ring(q,1024);
    const radialValues=radial(t,5)[0];
    for(let i=0;i<nu;i++){
      const u=2*Math.PI*i/nu,p=rotate(rs(u-phase).p,phase),h=modes(u,4)[0],d=[0,0,0];
      for(let a=0;a<5;a++)for(let b=0;b<h.length;b++)for(let c=0;c<3;c++)d[c]+=radialValues[a]*h[b]*coeff[3*(a*h.length+b)+c];
      const xy=rotate(d,u),x=f*p[0]+xy[0],y=f*p[1]+xy[1],z=.78+Lc*t+d[2];
      points.push([x,y,z],[x,y,-z]);
      const r=Rc*Math.sqrt(1-t**4),zc=.78+Lc+.32*t;points.push([r*C(u),r*S(u),zc],[r*C(u),r*S(u),-zc]);
    }
  }
  for(let i=0;i<2;i++){
    const f=ports[i],xs=[],rows=actualRings(specs[i],48);
    for(const [d,t,r,a] of rows)for(let j=0;j<48;j++){
      const chi=2*Math.PI*j/48,v=d+flatH[i]-r*C(chi)*S(a),w=t+r*C(chi)*C(a);
      xs.push([f.o[0]+v*f.n[0]+w*f.t[0],f.o[1]+v*f.n[1]+w*f.t[1],r*S(chi)]);
    }
    arms.push(xs);points.push(...xs);
  }
  return {points,arms};
}
function dot3(a,b){return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]}
function dist2(a,b){return (a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2}
function farSet(points){let id=0,best=0,pair=[];for(let i=0;i<56;i++){
 if(i%4===0)id=Math.min(points.length-1,Math.floor(i/56*points.length));let big=-1,jj=id,a=points[id];
 for(let j=0;j<points.length;j++){let d=dist2(a,points[j]);if(d>big){big=d;jj=j}}
 if(big>best){best=big;pair=[a,points[jj]]}id=jj;
 }return {distance:Math.sqrt(best),pair}}
function fullObserve(anchor,last){
  const cs=[physicalCloud(etaMax,anchor),physicalCloud(0,last)];
  const ds=cs.map(c=>farSet(c.points));let support=0,dir=0;
  const hh=cs.map((c,i)=>c.points.map(x=>holding(x,i===0?etaMax:0)));
  for(let k=0;k<240;k++){let theta=2*Math.PI*k/240,d=[C(theta),S(theta),0],m=hh.map(v=>{let max=-Infinity;for(const x of v)max=Math.max(max,dot3(x,d));return max});
    if(Math.abs(m[0]-m[1])>support){support=Math.abs(m[0]-m[1]);dir=theta}}
  return {pointCounts:cs.map(c=>c.points.length),diameters:ds,heldDirectional:support,heldDirection:dir,
    finiteHeldRatio:support/ds[0].distance,finiteDiameterQuotientRatio:(ds[1].distance/ds[0].distance-1)/2};
}
function main() {
  const fs=require('node:fs'), crypto=require('node:crypto');
  const args=process.argv.slice(2), idx=args.indexOf('--out');
  if(idx<0) throw Error('use --out fresh.json');
  const states=[];
  for(const phase of [.3075,.205,.1025,0]){
    const last=states.length?states[states.length-1].x:null;
    const start=last?last.map(v=>v*(states.length+1)/states.length):null;
    states.push(optimize(phase,5,4,22,32,start,9,50));
  }
  const fixed=states[0].x.map(x=>0);
  const anchors=[...states,{phase:etaMax,x:fixed}].sort((a,b)=>a.phase-b.phase);
  const rows=[];
  for(let i=0;i<=16;i++){
    const phase=etaMax*i/16, a=Math.min(3,Math.floor(i/4));
    const tau=(phase-anchors[a].phase)/(anchors[a+1].phase-anchors[a].phase);
    const x=anchors[a].x.map((v,j)=>v+tau*(anchors[a+1].x[j]-v));
    const grid=sample(phase,5,4,37,57,.371);
    const initial=evalState(grid,fixed),final=evalState(grid,x);
    rows.push({phase,initialPeak:initial.mx,finalPeak:final.mx,
      closureCurvature:curvatureActual(phase,x,5,4,36,58)});
  }
  const output={schema:'threefold-two-rigid-ports-exact-angular-speed-closure-and-four-actual-xyz-phases-v1',
    sourceSHA256:crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),
    parameters:{period:P,kl,kh,lowLength:loLen,highLength:hiLen,transition:tau,
      materialPhase:[0,etaMax],fixedMetricPhase:etaMax,length:Lc,capRadius:Rc,capHeight:.32,
      halfCentral:.78,radialBasis:5,angularOrderThreeMultiples:4,
      lowArm:[1.37,.24,.90,'short'],highArm:[-1.33,.24,.28,'s5'],
      armWidths:[.249,.31],centerArclengths:[etaMax/2,Math.PI+etaMax/2]},
    centralExtremeRadii:[A,Bhigh],rampRule:'No intermediate old R299 or R262 ramp. Closed unit-speed threefold rings are integrated from their tangent. The common target is frozen from the unmodified compact phase.',
    wholeCycleInterpolation:'piecewise linear in actual spatial coefficients, continuous in the spatial C2 topology',
    method:'sampled Levenberg update with dense analytic J and diagonally scaled Krylov solve; independent shifted grids',
    continuousMetricCertified:false,completeReachCertified:false,
    actualClosedEndpoints:fullObserve(fixed,states[states.length-1].x),rows,states};
  fs.writeFileSync(args[idx+1],JSON.stringify(output,null,2)+'\n',{flag:'wx'});
}
if(typeof require==='function' && require.main===module)main();
