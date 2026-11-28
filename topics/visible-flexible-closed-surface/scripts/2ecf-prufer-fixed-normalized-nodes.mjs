#!/usr/bin/env node
/** Same infinite rotation background in units of its exact outer packet radius. */
import {writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {pruferPackets} from './2ecf-slow-prufer-packet-tail.mjs';
import {exactMeanState} from './2ecf-slow-prufer-exact-mean.mjs';

function anchoredSamples(levels=20, density=3, shift=0) {
 const opts={cuff:.371,Z:0,shrink:1.5,prefix:0,delta:.018,slope:.00014,levels},packet=pruferPackets(opts),eps=3.5e-10,rt=Math.sqrt(12),rows=[];
 let distance=0;for(const c of packet.cells){c.rout=Math.exp(-distance/rt);distance+=c.xlen;c.rin=Math.exp(-distance/rt);c.mu=opts.slope*c.scale*c.delta;}
 for(let n=levels-1;n>=0;n--){const c=packet.cells[n];for(let k=0;k<c.parts.length;k++){let part=c.parts[k];for(let j=0;j<part.table.length;j++){let g=part.table[j],nj=density*(part.table.length===1?20:1);for(let it=0;it<=nj;it++){if(shift?(it===nj):(it===0&&rows.length))continue;let ph=it===nj?g.v:g.u+(g.v-g.u)*(it+shift)/nj,q=packet.layerPoint(c,part,g,ph),m=exactMeanState(q,eps),F=eps*q.f,T=eps*q.fr,TT=eps*q.frr,U=eps*q.U,V=eps*q.Ur,VV=eps*q.Urr,W=Math.sqrt(m.rad),hp=1+m.Ap,h=q.r+m.A,gpp=9*(V*V+U*VV)/4+4*(T*T+F*TT),hpp=(-2*m.Ap-m.Ap*m.Ap-gpp/2)/h,cp=-q.wr*m.dc/W-(5*V*VV/8+T*TT/2+hp*hpp)/W;
 rows.push([n,k,ph,q.r,q.w,q.wr,F,T,TT,U,V,VV,m.A,m.Ap,hpp,m.dc,cp,c.delta,c.qout,c.rout]);}}}}
 return {levels,density,normalizedEpsilon:eps,outerAnchor:1,options:opts,rows};
}
export {anchoredSamples};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){const [out,levels,density,shift]=process.argv.slice(2);writeFileSync(out,JSON.stringify(anchoredSamples(Number(levels??20),Number(density??3),Number(shift??0)))+'\n');}
