#!/usr/bin/env node
/** Finite old-input observations for the analytic R323 infinite obstruction. */
import {pruferPackets} from './2ecf-compact-prufer-packet-tail.mjs';
const p=pruferPackets({cuff:.371,Z:.5724,delta:.011,prefix:2,slope:8e-6,switch:1,levels:37}),eps=4e-6;
const rows=p.cells.map(c=>{const part=c.parts[2],g=p.layerPoint(c,part,part.table[0],Math.PI/2),fp=eps*g.fr,ratio=Math.abs(fp/g.w);return {n:c.n,r:g.r,w:g.w,actualFp:fp,ratio,necessaryRadicandUpper:g.w**2-fp**2/2};});
if(rows.some(x=>!(x.ratio>Math.SQRT2)))throw Error('Finite packet witness failed');
console.log(JSON.stringify({oldCuff:p.cuff,generatedOuterRadius:p.rout,rows},null,2));
