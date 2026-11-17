// Recover centered actual Cartesian cut jets from the finite momentum root.
// Generated angular arrays stay in scratch. They are not a closure certificate.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,factoryFile,input,out,angularArg='512',stepArg='0.0001']=process.argv.slice(2);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const hash=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const record=JSON.parse(gunzipSync(fs.readFileSync(input))),cp=record.response.checkpoint;
const cfg={...record.config,quadrature:Number(angularArg)};
const {createRecalibrationFactory}=await import(pathToFileURL(factoryFile));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/78718-tail-tangent-split.mjs')));
const {createRelativeSpatialJetEvaluator}=await import(pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,'f6tail_relative_spatial_jets.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const c=dn.tail.cells[0],profile=c.profiles[0],state=new Float64Array(2*cfg.modes+2);
state.set(cp.states[0]);
// Stored cut momentum is normalized after the outer shooting port. This is
// precisely the inverse normalization in the immutable DN.cutJets method.
const rho=2**dn.tail.parameters.a;
for(let j=0;j<cfg.modes;j++)state[cfg.modes+j]*=rho;
const ev=createRelativeSpatialJetEvaluator(c.engine,{spacing:cfg.spacing,radialDifferenceStep:Number(stepArg)});
const a=ev.evaluate(state,profile,1),g=a.g,wr=g.w*g.dlogwdx/g.drdx;
const reflect=v=>[v[0],v[1],-v[2]],rs=-1/Math.sqrt(g.E),rss=-g.w*wr/(g.E*g.E);
const rows=a.perAngle.map(v=>{
 const t=v.theta,C=Math.cos(t),S=Math.sin(t);
 const X=reflect([g.r*C+v.V[0],g.r*S+v.V[1],v.V[2]]);
 const Xr=reflect([C+v.Vr[0],S+v.Vr[1],g.w+v.Vr[2]]);
 const Xrr=reflect([v.Vrr[0],v.Vrr[1],wr+v.Vrr[2]]);
 const Xtheta=reflect([-g.r*S+v.Vt[0],g.r*C+v.Vt[1],v.Vt[2]]);
 const Xrtheta=reflect([-S+v.Vrt[0],C+v.Vrt[1],v.Vrt[2]]);
 const Xthetatheta=reflect([-g.r*C+v.Vtt[0],-g.r*S+v.Vtt[1],v.Vtt[2]]);
 return {theta:t,X,Xs:Xr.map(x=>rs*x),Xss:Xrr.map((x,j)=>rs*rs*x+rss*Xr[j]),Xtheta,Xstheta:Xrtheta.map(x=>rs*x),Xthetatheta};
});
fs.writeFileSync(out,JSON.stringify({scope:'Actual centered finite Cartesian tail cut. Entire worker z is reflected; s uses dr/ds=-1/sqrt(E). A constant translation and SO(2) gauge remain for alignment. No infinite closure claim.',input,input_sha256:hash(input),factory:factoryFile,factory_sha256:hash(factoryFile),angular:cfg.quadrature,radialDifferenceStep:Number(stepArg),cut:{r:g.r,w:g.w,wr,E:g.E,rs,rss},actualMetric:a.development.actualMetricRelativeOperatorError,rootResidual:a.heightJets.rootRelativeResidual,rows})+'\n');
console.log(JSON.stringify({out,angular:cfg.quadrature,actualMetric:a.development.actualMetricRelativeOperatorError,rootResidual:a.heightJets.rootRelativeResidual,sha256:hash(out)}));
