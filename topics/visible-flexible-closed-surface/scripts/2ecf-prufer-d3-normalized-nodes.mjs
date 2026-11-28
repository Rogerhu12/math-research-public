#!/usr/bin/env node
/** Threefold nonanalytic tail, generated on an outer-anchored material clock. */
import {writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {pruferPackets} from './2ecf-slow-prufer-packet-tail.mjs';
const m=3, k=m*Math.sqrt(m*m-1), A=m*m, B=2*A-1, h=m/Math.sqrt(A-1);
const input={fundamental:m,slope:.000055,epsilon:8e-11,delta:.018,shrink:1.5};
function physicalRow(n,part,phase,R,w,wr,Q,pPi,muPi,d,qout,rout,o=input){
 const e=o.epsilon,F=e*R**A*Q,T=e*R**(A-1)*(A*Q-k*pPi),TT=-(wr/w)*(T-A*F/R);
 const U=-e*h*muPi/R**(A-1),V=-w*T,VV=-A*wr*F/R;
 const gU=(m-1/m)**2/2,gF=A/2,eU=(1+1/A)/2;
 const g=gU*U*U+gF*F*F,gp=2*(gU*U*V+gF*F*T),gpp=2*(gU*(V*V+U*VV)+gF*(T*T+F*TT));
 const ee=eU*V*V+T*T/2,x=g/R**2,y=gp/(2*R),rad=w*w-ee+(2*y-y*y-x)/(1-x);
 if(!(rad>0))throw Error('D3 mean radicand');
 const W=Math.sqrt(rad),sa=Math.sqrt(1-x),da=-g/(R*(1+sa)),hp=(1-y)/sa;
 const ap=((x-2*y+y*y)/(1-x))/(hp+1),hpp=(-2*ap-ap*ap-gpp/2)/(R+da);
 const dc=(-ee+(2*y-y*y-x)/(1-x))/(W+w),cp=-wr*dc/W-(eU*V*VV+T*TT/2+hp*hpp)/W;
 return [n,part,phase,R,w,wr,F,T,TT,U,V,VV,da,ap,hpp,dc,cp,d,qout,rout];
}
function macroRow(R,o=input){
 const phase=k*Math.log(R),P=Math.sin(phase),w=o.slope/R**B;
 return physicalRow(0,5,phase,R,w,-B*w/R,Math.cos(phase),P,o.slope*P,o.delta,1,1,o);
}
function d3Samples(levels=20,density=3,shift=0,panels=100,Rend=1.35,o=input){
 const p0=pruferPackets({cuff:1,Z:0,shrink:o.shrink,prefix:0,delta:o.delta,slope:o.slope,levels});
 let distance=0;for(const c of p0.cells){c.rout=Math.exp(-distance/k);distance+=c.xlen;c.rin=Math.exp(-distance/k);c.mu=o.slope*c.scale*c.delta;}
 const rows=[];
 for(let n=levels-1;n>=0;n--){const c=p0.cells[n];for(let j=0;j<c.parts.length;j++){
  const part=c.parts[j];for(const g of part.table){const count=density*(part.table.length===1?20:1);
   for(let i=0;i<=count;i++){if(shift?(i===count):(i===0&&rows.length))continue;
    const phi=i===count?g.v:g.u+(g.v-g.u)*(i+shift)/count,[dx,da]=part.int(g.u,phi),[p,lp,xp]=part.val(phi);
    const R=c.rin*Math.exp((g.x+dx)/k),amp=c.qin*Math.exp(g.a+da),Q=amp*Math.cos(phi),P=amp*Math.sin(phi);
    const w=c.mu/(R**B*p),wr=(-B-k*lp/xp)*w/R;
    rows.push(physicalRow(n,j,phi,R,w,wr,Q,p*P,c.mu*P,c.delta,c.qout,c.rout,o));
   }
  }
 }}
 if(!shift)rows[rows.length-1]=macroRow(1,o);
 for(let j=0;j<panels;j++)rows.push(macroRow(1+(Rend-1)*(j+(shift||1))/panels,o));
 return {levels,density,normalizedEpsilon:o.epsilon,outerAnchor:1,fundamental:m,slope:o.slope,macro:{Rend,panels},rows};
}
export {d3Samples,physicalRow,macroRow,input};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){const [out,n,d,s,p,R]=process.argv.slice(2);writeFileSync(out,JSON.stringify(d3Samples(Number(n??20),Number(d??3),Number(s??0),Number(p??100),Number(R??1.35)))+'\n');}
