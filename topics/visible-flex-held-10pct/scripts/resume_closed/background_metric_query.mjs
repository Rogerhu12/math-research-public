// Numerical w(r) of the same fixed rotational background, evaluated at the
// finite map's actual radius. This is not an interval quadrature certificate.
import fs from 'node:fs';import path from 'node:path';import readline from 'node:readline';
import {pathToFileURL}from'node:url';import{gunzipSync}from'node:zlib';
const [sourceArg,checkpointArg]=process.argv.slice(2),source=path.resolve(sourceArg),buf=fs.readFileSync(checkpointArg);
const rec=JSON.parse(buf[0]===31?gunzipSync(buf):buf),cp=rec.response?.checkpoint??rec.checkpoint??rec;
process.env.CLOSING_TAIL_CACHE=path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const{createRecalibrationFactory}=await import(pathToFileURL(path.join(source,'scripts/closing_weighted_tail.mjs')));
const factory=createRecalibrationFactory(rec.config??cp.parameters),physical=factory.assemble(),p=physical.parameters,alpha=physical.stats.alpha;
if(p.orientation!==1||p.protectCell!==160)throw Error('Expected the fixed positive 160-cell background');
function accumulator(){let s=0,c=0;return{add(v){const y=v-c,t=s+y;c=t-s-y;s=t;},value(){return s;}};}
const acc=accumulator(),pieces=[];
for(let n=0;n<160;n++){
 const es=factory.getEntries(n,p.valleyControls[n]??0).entries;
 for(let j=es.length-1;j>=0;j--){const e=es[j],width=e.total[0]+alpha*e.total[1],outer=p.rCut-acc.value();acc.add(width);const inner=p.rCut-acc.value();if(outer>inner)pieces.push({n,j,e,outer,inner,width});}
}
let maxResidual=0,maxIterations=0;
function query(R){
 if(!(R>=p.rCuff&&R<=p.rCut))throw Error('Radius outside retained tail');
 if(R===p.rCut)return{w:p.wCut,wr:-7*p.wCut/p.rCut,residual:0,iterations:0};
 if(R===p.rCuff)return{w:0,wr:0,residual:0,iterations:0};
 let lo=0,hi=pieces.length;
 while(lo<hi){const mid=(lo+hi)>>1;if(pieces[mid].inner>R)lo=mid+1;else hi=mid;}
 const q=pieces[lo];if(!q||R<q.inner||R>q.outer)throw Error('Unresolved physical radius '+R);
 const target=q.width-(q.outer-R),S=p.warpSteps;
 const value=k=>q.e.cumA[k]+alpha*q.e.cumB[k];
 let l=0,h=S;while(l+1<h){const mid=(l+h)>>1;if(value(mid)<=target)l=mid;else h=mid;}
 let a=l/S,b=h/S,x=a+(b-a)*Math.max(0,Math.min(1,(target-value(l))/(value(h)-value(l))));
 let point,delta=0,it=0;
 for(;it<24;it++){
  point=q.e.point(x);delta=point.A+alpha*point.B-target;
  if(Math.abs(delta)<=3e-17)break;
  if(delta<0)a=x;else b=x;
  const nx=x-delta/(point.dA+alpha*point.dB);x=nx>a&&nx<b?nx:(a+b)/2;
 }
 point=q.e.point(x);delta=point.A+alpha*point.B-target;const w=Math.exp(point.g.logw),wr=w*point.g.dlogwdx/(point.dA+alpha*point.dB);
 maxResidual=Math.max(maxResidual,Math.abs(delta));maxIterations=Math.max(maxIterations,it);
 return{w,wr,residual:Math.abs(delta),iterations:it,cell:q.n,segment:q.j,x};
}
console.log(JSON.stringify({ready:true,alphaApprox:alpha,scope:'Numerical inverse at actual finite-map radius; true background definition and continuous bounds are separate.'}));
for await(const line of readline.createInterface({input:process.stdin,crlfDelay:Infinity})){
 if(!line.trim())continue;try{const req=JSON.parse(line);console.log(JSON.stringify({rows:req.radii.map(query),maxInverseRadiusResidual:maxResidual,maxIterations}));}catch(e){console.log(JSON.stringify({error:String(e.message??e)}));}
}
