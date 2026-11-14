// Inspect the actual complete finite linear initializer in the nonlinear
// momentum variables. No nonlinear root or DN result is inferred here.
import fs from 'node:fs';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {createSplitFluxCompactTailDN} from './78718-tail-geometric-trial-split.mjs';
const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const request=JSON.parse(fs.readFileSync(process.argv[3],'utf8'));
const start=Date.now(),physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical}),M=cfg.modes;
const cut=dn.cutJets(new Float64Array(2*M)),target=Float64Array.from(request.height,h=>h/cut.radius**4);
const states=dn.tail.initial(target),rows=[];
for(let stage=0;stage<dn.tail.cells.length;stage++){
 const cell=dn.tail.cells[stage],g=cell.engine.geometry(cell.profiles[0],0),y=states[stage+1];
 const p=[],L=[];
 for(let j=0;j<M;j++){
  p.push(-cfg.spacing*(j+1)*g.r**3*y[j]/(Math.sqrt(2)*g.w));
  L.push(dn.tail.parameters.orientation*Math.sqrt(6)*cell.mu*y[M+j]/(g.r**4*g.w2));
 }
 const P=Math.sqrt(2)*p.reduce((s,v)=>s+Math.abs(v),0),
   Pt=Math.sqrt(2)*p.reduce((s,v,j)=>s+Math.abs(cfg.spacing*(j+1)*v),0),
   LL=Math.sqrt(2)*L.reduce((s,v)=>s+Math.abs(v),0);
 rows.push({stage,rawCell:cell.rawCell,rawSegment:cell.rawSegment,r:g.r,w:g.w,
  P_upper:P,Pt_upper:Pt,L_upper:LL,A_perturbation_upper:LL+g.w2*Pt,
  physical_gradient_wP_upper:g.w*P,
  momentum_root_target:Array.from(L),Q:Array.from(y.slice(0,M))});
}
function worst(key){return rows.reduce((a,b)=>a[key]>b[key]?a:b);}
const bound=Math.max(...rows.map(r=>Math.max(r.P_upper,r.Pt_upper,r.L_upper)));
const result={scope:'Full finite linear initializer NODE bounds only, not a nonlinear solution or a between-node certificate.',
 height:request.height,stages:rows.length,maximumP:worst('P_upper'),maximumPt:worst('Pt_upper'),maximumL:worst('L_upper'),
 maximumAPerturbation:worst('A_perturbation_upper'),
 suggested_initial_ray_scale:Math.min(1,.002/bound),rows,seconds:(Date.now()-start)/1000};
fs.writeFileSync(process.argv[4],JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({stages:result.stages,maxP:result.maximumP.P_upper,maxPt:result.maximumPt.Pt_upper,
 maxL:result.maximumL.L_upper,maxAperturbation:result.maximumAPerturbation.A_perturbation_upper,
 suggested_initial_ray_scale:result.suggested_initial_ray_scale,seconds:result.seconds}));
