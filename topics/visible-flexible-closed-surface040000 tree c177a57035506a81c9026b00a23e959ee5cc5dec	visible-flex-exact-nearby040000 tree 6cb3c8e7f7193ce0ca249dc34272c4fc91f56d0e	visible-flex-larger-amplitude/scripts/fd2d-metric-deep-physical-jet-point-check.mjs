// Reproduce the ordinary/deep-algebra overlap check of the same point root.
// No DN, radial ODE, or synthetic complete tail is constructed here.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createMomentumPhysicalJetEvaluator} from './fd2d-metric-deep-momentum-physical-jets.mjs';

const [verifiedDirectory,output]=process.argv.slice(2);
if(!verifiedDirectory||!output)throw Error('Usage: node POINT_CHECK.mjs VERIFIED_SOURCE_DIRECTORY NEW_REPORT.json');
if(fs.existsSync(output))throw Error('Keep actual point checks immutable');
function identity(file){const bytes=fs.readFileSync(file);return {file:path.resolve(file),bytes:bytes.length,sha256:crypto.createHash('sha256').update(bytes).digest('hex')};}
const expected={
 'general_root_tail_momentum.mjs':'182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c',
 'general_exact_tail_cauchy_raw.mjs':'0c8139fd146a52188a6eedfe898003f8417d745c2fcde6f2a9eb5479aa7855df',
 'f6tail_momentum_physical_jets.mjs':'2b96df25211c5d6ebfc7faf689ea7035704bf0bf7c1ea3aa50b1c137fbe39ea8'};
const verified={};
for(const [name,sha] of Object.entries(expected)){
 verified[name]=identity(path.join(verifiedDirectory,name));
 if(verified[name].sha256!==sha)throw Error('Changed frozen source: '+name);
}
const {createMomentumTailEngine}=await import(pathToFileURL(path.join(verifiedDirectory,'general_root_tail_momentum.mjs')));
const {createMomentumPhysicalJetEvaluator:createOldJets}=await import(pathToFileURL(path.join(verifiedDirectory,'f6tail_momentum_physical_jets.mjs')));
const options={modes:4,quadrature:64,spacing:2,mu:.003,orientation:1},x=.37,
 profile=t=>({r:.4+.003*t,drdx:.003,logw:Math.log(.1)-.05*t,dlogwdx:-.05}),
 state=Float64Array.from([1e-3,-2e-4,7e-5,-1e-5,3e-6,-4e-7,2e-7,-3e-8,.02,.03]),
 engine=createMomentumTailEngine(options),old=createOldJets(engine,{spacing:2})(state,profile,x),
 ordinary=createMomentumPhysicalJetEvaluator(engine,{spacing:2})(state,profile,x);
const forced={...engine,
 root(y,p,t){
  const rt=engine.root(y,p,t),g=rt.g;
  g.deepScaled=true;
  g.momentumTargetFactor=options.orientation*Math.sqrt(6)*options.mu/(g.r**4*g.w2);
  g.momentumPFactor=g.r**3/(Math.sqrt(2)*g.w);
  return rt;
 },
 rhsWithComponents(y,p,t,knownRoot){
  const rt=knownRoot??this.root(y,p,t),flux=new Float64Array(options.modes);
  for(let n=0;n<options.quadrature;n++){
   const v=rt.e.rows[n],f=(1+v.K)*v.U/(v.S*v.sd),theta=2*Math.PI*n/options.quadrature;
   for(let j=0;j<options.modes;j++)flux[j]+=f*Math.sqrt(2)*Math.sin(options.spacing*(j+1)*theta)/options.quadrature;
  }
  return {derivative:engine.rhs(y,p,t,false,rt),momentumFlux:flux,root:rt};
 }
};
const regrouped=createMomentumPhysicalJetEvaluator(forced,{spacing:2})(state,profile,x),keys=['ur','ut','urr','urt','utt','darboux','height'];
function differences(a,b){
 const answer={};
 for(const key of keys)answer[key]=Math.max(...a.perAngle.map((v,j)=>Math.abs(v[key]-b.perAngle[j][key])));
 answer.Ldot=Math.max(...a.Ldot.map((v,j)=>Math.abs(v-b.Ldot[j])));
 if(!Object.values(answer).every(Number.isFinite))throw Error('Nonfinite overlap comparison');
 return answer;
}
const normalDiff=differences(old,ordinary),deepDiff=differences(old,regrouped);
if(Object.values(normalDiff).some(v=>v!==0))throw Error('Ordinary arithmetic changed');
if(Object.values(deepDiff).some(v=>v>1e-12))throw Error('Point regrouping discrepancy exceeds overlap diagnostic scale');
const report={schema:'fd2d-deep-physical-jet-point-algebra-check-v2',
 checker:identity(fileURLToPath(import.meta.url)),
 source:identity(fileURLToPath(new URL('./fd2d-metric-deep-momentum-physical-jets.mjs',import.meta.url))),
 verified_sources:verified,point:{...options,x,profile:profile(x),state:Array.from(state)},
 ordinary_arithmetic_max_difference:normalDiff,forced_regrouped_arithmetic_max_difference:deepDiff,
 finite_point_root_only:true,DN_solved:false,radial_ODE_integrated:false,deep_actual_profile_solved:false,
 scope:'A reproducible overlap identity check. The forced branch has ordinary positive w^2; actual w^2-underflow is covered separately by numerical deep-arithmetic-check-02.'};
fs.writeFileSync(output,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({report:identity(output),ordinary:normalDiff,forced:deepDiff}));
