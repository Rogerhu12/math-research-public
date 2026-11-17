// Approximate point queries of the unchanged rotational background.
// Exact geometry is defined by the source's real integrals, with the separate
// interval proof. This binary64 evaluator does not certify its quadrature.
import fs from 'node:fs';
import path from 'node:path';
import readline from 'node:readline';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
const [sourceArg,checkpointArg]=process.argv.slice(2);
if(!sourceArg||!checkpointArg)throw Error('SOURCE_TOPIC TAIL_CHECKPOINT required');
const source=path.resolve(sourceArg),raw=fs.readFileSync(checkpointArg);
const record=JSON.parse((raw[0]===31?gunzipSync(raw):raw).toString());
const cp=record.response?.checkpoint??record.checkpoint??record;
process.env.CLOSING_TAIL_CACHE=path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(source,'scripts/closing_weighted_tail.mjs')));
const factory=createRecalibrationFactory(record.config??cp.parameters),physical=factory.assemble(),p=physical.parameters;
if(p.orientation!==1||p.protectCell!==160)throw Error('This evaluator is frozen to the positive 160-cell background');
const alpha=physical.stats.alpha,pieces=[];
function accumulator(){let sum=0,c=0;return {add(v){const y=v-c,t=sum+y;c=(t-sum)-y;sum=t;},value(){return sum;}};}
const dr=accumulator(),dz=accumulator();
for(let n=0;n<160;n++){
 const entries=factory.getEntries(n,p.valleyControls[n]??0).entries;
 for(let j=entries.length-1;j>=0;j--){
  const e=entries[j],width=e.total[0]+alpha*e.total[1],height=e.total[4]+alpha*e.total[5];
  const outer=p.rCut-dr.value(),z=dz.value();dr.add(width);dz.add(height);
  pieces.push({n,j,e,outer,inner:p.rCut-dr.value(),z});
 }
}
const heightTotal=dz.value();
function integral(piece,x){const v=piece.e.integrate(x,1);return [v[0]+alpha*v[1],v[4]+alpha*v[5]];}
function query(R){
 if(!(Number.isFinite(R)&&R>=0&&R<=p.rCut))throw Error('Radius outside closed cap');
 if(R<=p.rCuff)return {R,heightFromRToCut:heightTotal,w:0,wr:0,where:'flat-disk',deepHeightOmissionUpper:256*2**-280*p.rCuff*Math.expm1((6*p.delta0*2**-160+6*p.delta0*p.etaRatioAtN0*2**-240/(1-2**-1.5))/Math.sqrt(12))};
 if(R===p.rCut)return {R,heightFromRToCut:0,w:p.wCut,wr:-7*p.wCut/p.rCut,where:'literal-cut'};
 const piece=pieces.find(z=>z.outer>z.inner&&R>=z.inner&&R<=z.outer);
 if(!piece)throw Error('Binary64 background inverse does not resolve this radius; use the exact integral definition or higher precision');
 let lo=0,hi=1;const target=piece.outer-R;
 for(let k=0;k<44;k++){const mid=(lo+hi)/2;if(integral(piece,mid)[0]>target)lo=mid;else hi=mid;}
 const x=(lo+hi)/2,iv=integral(piece,x),g=piece.e.profileSource(x),v=piece.e.integrand(x),w=Math.exp(g.logw);
 return {R,heightFromRToCut:piece.z+iv[1],w,wr:w*g.dlogwdx/(v[0]+alpha*v[1]),
  where:'finite-source-profile',cell:piece.n,piece:piece.j,sourceX:x,inverseRadiusResidual:iv[0]-target};
}
console.log(JSON.stringify({ready:true,alphaApprox:alpha,heightToCutApprox:heightTotal,scope:'Numerical evaluator only; exact background and geometric bounds are separately defined/proved.'}));
for await(const line of readline.createInterface({input:process.stdin,crlfDelay:Infinity})){
 if(!line.trim())continue;
 try{const req=JSON.parse(line);console.log(JSON.stringify({rows:req.radii.map(query)}));}
 catch(e){console.log(JSON.stringify({error:String(e.message??e)}));}
}
