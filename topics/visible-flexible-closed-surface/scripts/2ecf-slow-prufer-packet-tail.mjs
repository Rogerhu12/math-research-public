#!/usr/bin/env node
/** Purpose-built second-mode tail. A full real Prüfer half-turn is the independent variable of each packet. */
import {pathToFileURL} from 'node:url';
import {gauss01} from './2ecf-compact-p32-normal-meridian-design.mjs';
function pruferPackets(opts={}){
 const shrink=opts.shrink??2,pi=Math.PI,rt=Math.sqrt(12),a=Math.sqrt(3)/2,cuff=opts.cuff??.371,baseZ=opts.Z??.5724,delta0=opts.delta??.011,pre=opts.prefix??2,beta=3,cutSlope=opts.slope??8e-6,sw=opts.switch??1,levels=opts.levels??37,theta=Math.atan(4),gamma=Math.atan(.25),G8=[[.0198550717512319,.0506142681451881],[.101666761293187,.111190517226687],[.237233795041836,.156853322938944],[.408282678752175,.181341891689181],[.591717321247825,.181341891689181],[.762766204958164,.156853322938944],[.898333238706813,.111190517226687],[.980144928248768,.0506142681451881]],cells=[];
 const smooth=x=>x**3*(10+x*(-15+6*x)),smoothD=x=>30*(x*(1-x))**2;
 function make(n){const deep=Math.max(0,n-pre),delta=delta0*shrink**(-deep),scale=shrink**(-beta*deep),p0=n<pre?delta:shrink**beta*delta,p1=1/delta,p2=delta,om=sw*delta,parts=[],bounds=[0,theta-om,theta+om,pi-gamma-om,pi-gamma+om,pi],v=[p0,p1,p2];let X=0,A=0;
  function pack(lo,hi,l,r,ramp){const logl=Math.log(l),logr=Math.log(r);function val(ph){const y=(ph-lo)/(hi-lo),lp=ramp?logl+(logr-logl)*smooth(y):logl,p=ramp?Math.exp(lp):l,c=Math.cos(ph),s=Math.sin(ph),den=p*s*s+c*c/p;return [p,ramp?(logr-logl)*smoothD(y)/(hi-lo):0,1/den,(1/p-p)*s*c/den];}
   function int(a,b){if(a===b)return [0,0];if(!ramp){const f=t=>Math.atan2(l*Math.sin(t),Math.cos(t)),q=t=>Math.hypot(Math.cos(t),l*Math.sin(t));return [f(b)-f(a),Math.log(q(a)/q(b))];}let x=0,h=0;for(let [u,w] of G8){const y=val(a+(b-a)*u);x+=w*y[2];h+=w*y[3];}return [(b-a)*x,(b-a)*h];}
   let J=ramp?24:1,table=[];for(let j=0;j<J;j++){const u=lo+(hi-lo)*j/J,v=lo+(hi-lo)*(j+1)/J,[dx,da]=int(u,v);table.push({u,v,x:X,a:A,dx,da});X+=dx;A+=da;}
   parts.push({lo,hi,val,int,table});}
  pack(bounds[0],bounds[1],p0,p0,false);pack(bounds[1],bounds[2],p0,p1,true);pack(bounds[2],bounds[3],p1,p1,false);pack(bounds[3],bounds[4],p1,p2,true);pack(bounds[4],bounds[5],p2,p2,false);
  return {n,delta,scale,parts,xlen:X,gain:Math.exp(A)};
 }
 for(let n=0;n<levels;n++)cells.push(make(n));
 let inside=0;for(let j=levels-1;j>=0;j--){let c=cells[j];c.innerX=inside;inside+=c.xlen;c.outerX=inside;c.rin=cuff*Math.exp(c.innerX/rt);c.rout=cuff*Math.exp(c.outerX/rt);}
 const rout=cells[0].rout,k0=cutSlope*rout**7;let Qout=1;
 for(let c of cells){c.qout=Qout;c.qin=-Qout/c.gain;Qout=c.qin;c.mu=k0*c.scale*c.delta;}
 let totalZ=0;for(let n=levels-1;n>=0;n--){let c=cells[n];c.zin=totalZ;for(let part of c.parts)for(let row of part.table){row.z=totalZ;
   function dz(ph){const [dx]=part.int(row.u,ph),x=row.x+dx,r=c.rin*Math.exp(x/rt),[p,lp,xp]=part.val(ph);return c.mu*xp/(rt*p*r**6);}
   let inc=0;if(part.table.length===1){let p=part.val((row.u+row.v)/2)[0],ra=c.rin*Math.exp(row.x/rt),rb=c.rin*Math.exp((row.x+row.dx)/rt);inc=c.mu/p*(ra**(-6)-rb**(-6))/6;}
   else{for(let [q,w] of G8)inc+=w*dz(row.u+(row.v-row.u)*q);inc*=row.v-row.u;}totalZ+=inc;
  }c.zout=totalZ;}
 function layerPoint(c,part,row,ph,exactX=null){let [dx,da]=part.int(row.u,ph),xx=exactX??(row.x+dx),r=c.rin*Math.exp(xx/rt),[p,lp,xp]=part.val(ph),amp=c.qin*Math.exp(row.a+da),Q=amp*Math.cos(ph),ff=r**4*Q,pp=amp*Math.sin(ph),ww=c.mu/(r**7*p),wr=ww*(-7-rt*lp/xp)/r,fr=r**3*(4*Q-rt*p*pp),frr=-(wr/ww)*(fr-4*ff/r),U=-c.mu*pp/(a*r**3),Ur=-ww*fr,Urr=-4*wr*ff/r;let dz=0;
  if(part.table.length===1){const ra=c.rin*Math.exp(row.x/rt);dz=c.mu/p*(ra**(-6)-r**(-6))/6;}else{for(let [q,w] of G8){let ang=row.u+(ph-row.u)*q,[dx]=part.int(row.u,ang),rr=c.rin*Math.exp((row.x+dx)/rt),v=part.val(ang);dz+=w*c.mu*v[2]/(rt*v[0]*rr**6);}dz*=ph-row.u;}
  return {r,z:baseZ+row.z+dz,w:ww,wr,f:ff,fr,frr,U,Ur,Urr,n:c.n,phi:ph};
 }
 function physical(r){if(r<=cuff)return {r,z:baseZ,w:0,wr:0,f:0,fr:0,frr:0,U:0,Ur:0,Urr:0,n:Infinity};
  if(r>rout*(1+1e-13))throw Error('Outside the packet input');let c=cells.find(c=>r>=c.rin)||cells.at(-1),s=rt*Math.log(r/c.rin),part=c.parts.find(p=>s<=p.table.at(-1).x+p.table.at(-1).dx)||c.parts.at(-1),row=part.table.find(a=>s<=a.x+a.dx)||part.table.at(-1);
  let low=row.u,high=row.v,x=low+(high-low)*Math.max(0,Math.min(1,(s-row.x)/row.dx));for(let i=0;i<24;i++){let y=row.x+part.int(row.u,x)[0]-s;if(Math.abs(y)<2e-15)break;if(y>0)high=x;else low=x;const q=x-y/part.val(x)[2];x=q>low&&q<high?q:(low+high)/2;}
  return layerPoint(c,part,row,x,s);
 }
 function stats(){let worst=[0,0,0,0,0],at=[];for(let c of cells.slice(0,14))for(let part of c.parts)for(let row of part.table)for(let q of [0,.2,.5,.8,1]){let z=layerPoint(c,part,row,row.u+(row.v-row.u)*q),v=[Math.abs(z.wr),Math.abs(z.frr),Math.abs(z.fr),Math.abs(z.Urr),Math.abs(z.Ur)];for(let j=0;j<v.length;j++)if(v[j]>worst[j]){worst[j]=v[j];at[j]=[c.n,z.r];}}
  return {rout,height:totalZ,first:cells.slice(0,8).map(c=>[c.n,c.xlen,c.gain,c.qout]),minGain:Math.min(...cells.map(c=>c.gain)),sampledDerivativeMax:worst,at,cut:physical(rout)};}
 return {cells,cuff,rout,physical,stats,layerPoint};
}
function pruferExtension(packet,initial,targetR,targetMode,sign=1){
 const q=packet.physical(packet.rout),r0=packet.rout,w0=q.w,f0=initial*r0**4,Z0=q.z,c3=14*f0/r0**3,dR=targetR-r0,c4=(f0*(1+4*dR/r0)-c3*dR**3-targetMode)/dR**4;
 if(!(c4>0&&dR<3*r0))throw Error('Need a decreasing mode cap beyond the true incoming trace');
 const A=12*f0/r0,B=3*r0*c3,C=4*c4*r0-c3,n0=-6*c3*r0,n1=-6*c3-12*c4*r0,n2=-12*c4,k0=n2/C,k1=(n1-k0*B)/(2*C),k2=n0-k0*A-k1*B,disc=Math.sqrt(4*A*C-B*B);
 if(!(disc>0))throw Error('Buffer quadratic');
 function data(d){let den=A+B*d+C*d*d,J=2*Math.atan2(2*C*d*disc,disc*disc+B*(2*C*d+B))/disc,
  w=w0*Math.exp(k0*d+k1*Math.log(den/A)+k2*J),wr=w*(n0+n1*d+n2*d*d)/den,
   r=r0+d,f=f0*(1+4*d/r0)-c3*d**3-c4*d**4,fr=4*f0/r0-3*c3*d*d-4*c4*d**3,frr=-6*c3*d-12*c4*d*d;
  return {w,wr,r,f,fr,frr,U:w*(r*fr-4*f)/3,Ur:-w*fr,Urr:-4*wr*f/r};}
 const [x,w]=gauss01(8),depths=[0];let s=Math.sqrt(A/C)/8;while(s<dR){depths.push(s);s*=1.35;}depths.push(dR);let zz=[0];
 function integral(l,r){let sum=0;for(let k=0;k<x.length;k++)sum+=w[k]*data(l+(r-l)*x[k]).w;return (r-l)*sum;}
 for(let j=0;j+1<depths.length;j++)zz.push(zz[j]+integral(depths[j],depths[j+1]));
 function value(r){if(r<=r0){let v=packet.physical(r);return {...v,z:packet.physical(packet.cuff).z+sign*(v.z-packet.physical(packet.cuff).z),w:sign*v.w,wr:sign*v.wr,f:initial*v.f,fr:initial*v.fr,frr:initial*v.frr,U:sign*initial*v.U,Ur:sign*initial*v.Ur,Urr:sign*initial*v.Urr};}
  let d=r-r0,o=data(d),j=depths.findIndex(h=>h>=d);j=j<0?depths.length-2:Math.max(0,j-1);let v=zz[j]+integral(depths[j],d);
  return {...o,z:packet.physical(packet.cuff).z+sign*(Z0-packet.physical(packet.cuff).z+v),w:sign*o.w,wr:sign*o.wr,U:sign*o.U,Ur:sign*o.Ur,Urr:sign*o.Urr};}
 return {value,r0,targetR,targetMode,f0,c3,c4,outer:value(targetR),bufferHeight:zz.at(-1)};
}

export {pruferPackets,pruferExtension};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const packet=pruferPackets(),buffer=pruferExtension(packet,4e-6,packet.rout+.16,-.015);
 const {height,rout,minGain,first,sampledDerivativeMax}=packet.stats();
 console.log(JSON.stringify({numericalLevels:37,omittedLogCoordinateUpper:48*.022/2**35,rout,height,minGain,first,sampledDerivativeMax,buffer:{target:buffer.targetR,endpoint:buffer.outer,c3:buffer.c3,c4:buffer.c4}},null,2));
}
