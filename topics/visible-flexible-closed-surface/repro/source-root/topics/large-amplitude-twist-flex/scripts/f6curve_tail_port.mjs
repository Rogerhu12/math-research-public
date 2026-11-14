// Nonlinear finite-depth tail port server for coupling to a geometric curve BVP.
// GPT-6 Astra Pro / curve_transition, AI-assisted, 2026-11-08.
// It preserves the actual nonlinear DN; finite-depth results are not an R20 certificate.
import {makeDN} from './tailnext_dn_response.mjs';
import fs from 'node:fs';
import readline from 'node:readline';
const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const dn=makeDN(cfg),M=cfg.modes;
const zero=dn.cutJets(new Float64Array(2*M));
const D=[];
for(let j=0;j<M;j++){
 const node=new Float64Array(2*M);const amp=1e-20;
 node[j]=amp;node[M+j]=amp*dn.tail.graphs[0][j];
 const z=dn.cutJets(node);D.push(z.slope[j]/z.height[j]);
}
console.log(JSON.stringify({event:'ready',parameters:dn.tail.parameters,linearSlope:D,cut:zero}));
let last=null;
for await(const line of readline.createInterface({input:process.stdin,terminal:false})){
 try{
  const req=JSON.parse(line);if(req.stop)break;
  const target=req.height.map(v=>v/zero.radius**4);
  const sol=dn.solve(target,{maxIterations:16,tolerance:2e-10,jacobian:!!req.jacobian,audit:!!req.audit});
  if(sol.converged)last=sol;
  console.log(JSON.stringify({converged:sol.converged,residual:sol.normalizedResidual,jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,history:sol.history,audit:sol.audit??null}));
 }catch(e){console.log(JSON.stringify({failed:String(e)}));}
}

process.stdin.destroy();
