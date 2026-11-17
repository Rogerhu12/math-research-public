// Locate failures of the original finite-tail initial guess without altering equations or guards.
import fs from 'node:fs';import path from 'node:path';import{pathToFileURL}from'node:url';
const [topic,config,hfile,lambdastr,out]=process.argv.slice(2),lam=Number(lambdastr);process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const{createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const{createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/78718-tail-tangent-split.mjs')));
const{createFourierProductVariationalEngine}=await import(pathToFileURL(path.join(topic,'scripts/78718-tail-fourier-product-flow.mjs')));
const cfg=JSON.parse(fs.readFileSync(config)),H=JSON.parse(fs.readFileSync(hfile)).H,physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical}),M=cfg.modes,rcut=dn.cutJets(new Float64Array(2*M)).radius,target=Float64Array.from({length:M},(_,j)=>lam*(H[j]??0)/rcut**4),states=dn.tail.initial(target);
const replaced=new Set();for(const c of dn.tail.cells){if(replaced.has(c.engine))continue;replaced.add(c.engine);const original={...c.engine};Object.assign(c.engine,createFourierProductVariationalEngine({modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,mu:c.mu,orientation:1,projectionFloor:cfg.projectionFloor,cuspAwareFlow:cfg.cuspAwareFlow},original));}
let perMode=Array(M).fill(null).map(()=>({maxP:0,maxTarget:0})),nodeFailures=[],minA=1,minD=1;const sq12=Math.sqrt(12),sq2=Math.sqrt(2);
for(let n=0;n<dn.tail.cells.length;n++){const c=dn.tail.cells[n],p=c.profiles[0],g=c.engine.geometry(p,0),s=new Float64Array(2*M+2);s.set(states[n+1]);
 for(let j=0;j<M;j++){const P=Math.abs((j+1)*cfg.spacing*g.r**3*s[j]/g.w),L=Math.abs(sq12*c.mu*s[M+j]/(g.r**4*g.w2));if(P>perMode[j].maxP)Object.assign(perMode[j],{maxP:P,Pstage:n,Pr:g.r});if(L>perMode[j].maxTarget)Object.assign(perMode[j],{maxTarget:L,Lstage:n,Lr:g.r});}
 try{const r=c.engine.root(s,p,0);minA=Math.min(minA,r.e.minA);minD=Math.min(minD,r.e.minD);}catch(e){nodeFailures.push({stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,r:g.r,w:g.w,error:String(e)});}
}
const scales=new Float64Array(states.length);scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));for(let n=0;n<states.length-1;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);let evaluation;
try{const e=dn.tail.evaluate(states,target,true,scales);evaluation={norm:e.norm,minA:e.minA,minD:e.minD};}catch(e){evaluation={error:String(e),stage:e.tailStage,rawCell:e.tailRawCell,rawSegment:e.tailRawSegment};}
const result={scope:'Initial-guess diagnostic only, not nonlinear nonexistence or tail capacity.',config,lam,M,perMode,nodeFailures,minA,minD,evaluation};fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
