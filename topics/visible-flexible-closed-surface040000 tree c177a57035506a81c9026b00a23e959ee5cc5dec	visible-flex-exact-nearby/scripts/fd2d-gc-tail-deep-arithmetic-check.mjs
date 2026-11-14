// Targeted checks for the actual full160 w^2 underflow and normal-range identity.
import fs from 'node:fs';
import crypto from 'node:crypto';
import {loadClosingTailSource} from './closing_tail_sources.mjs';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {createDeepSplitMomentumEngine} from './fd2d-gc-tail-deep-engine.mjs';
import {createFourierProductVariationalEngine} from './78718-tail-fourier-product-flow.mjs';
import {createMomentumPhysicalJetEvaluator} from './fd2d-metric-deep-momentum-physical-jets.mjs';
const {createFastSplitFluxMomentumTailEngine}=await loadClosingTailSource('f6tail_fast_split_flux_engine.mjs');
const {createMomentumPhysicalJetEvaluator:createOldJets}=await loadClosingTailSource('f6tail_momentum_physical_jets.mjs');
const [configFile,outFile]=process.argv.slice(2),started=Date.now(),
 configBytes=fs.readFileSync(configFile),cfg=JSON.parse(configBytes),
 common={modes:4,spacing:2,quadrature:64,orientation:1,projectionFloor:.05};
function oldEngine(options){return createFourierProductVariationalEngine(options,createFastSplitFluxMomentumTailEngine(options));}
function diff(a,b){let absolute=0,relative=0,nonidentical=0;for(let j=0;j<a.length;j++){
 if(!Number.isFinite(a[j])||!Number.isFinite(b[j]))throw Error('Nonfinite numerical check at '+j);
 absolute=Math.max(absolute,Math.abs(a[j]-b[j]));relative=Math.max(relative,Math.abs(a[j]-b[j])/Math.max(1e-300,Math.abs(a[j]),Math.abs(b[j])));
 if(!Object.is(a[j],b[j]))nonidentical++;
}return {count:a.length,nonidentical,maximum_absolute:absolute,maximum_relative:relative};}
const normalOptions={...common,mu:.00013},normalProfile=x=>({r:.47+.004*x,drdx:.004,logw:Math.log(.018)+.08*x,dlogwdx:.08}),
 old=oldEngine(normalOptions),fresh=createDeepSplitMomentumEngine(normalOptions),
 raw=Float64Array.from([1e-6,-2e-8,3e-10,-4e-12,4e-7,-5e-9,6e-11,-7e-13]),
 oldInitial=old.initializeFromRaw(raw,normalProfile,.37),newInitial=fresh.initializeFromRaw(raw,normalProfile,.37),
 of=old.rhsWithJacobian(oldInitial.state,normalProfile,.37),nf=fresh.rhsWithJacobian(newInitial.state,normalProfile,.37),
 oj=createOldJets(old,{spacing:2})(oldInitial.state,normalProfile,.37),
 nj=createMomentumPhysicalJetEvaluator(fresh,{spacing:2})(newInitial.state,normalProfile,.37),
 normal={state:diff(oldInitial.state,newInitial.state),root:diff(of.root.L,nf.root.L),rhs:diff(of.derivative,nf.derivative),jacobian:diff(of.jacobian,nf.jacobian),Ldot:diff(oj.Ldot,nj.Ldot)};
for(const row of Object.values(normal))if(row.nonidentical)throw Error('Normal arithmetic differs: '+JSON.stringify(normal));
const factory=createRecalibrationFactory(cfg),cache=boundTailPointCaches(factory,cfg,{pointsPerEntry:8}),physical=factory.assemble();
let minimum=null;
for(let n=0;n<physical.cells.length;n++)for(let k=0;k<physical.cells[n].profiles.length;k++){
 const profile=physical.cells[n].profiles[k],points=[0,.25,.5,.75,1,...(profile.integrationBreakpoints??[])];
 for(const x of points){const g=profile(x);if(!minimum||g.logw<minimum.g.logw)minimum={rawCell:n,rawSegment:k,x,g,profile,mu:physical.cells[n].mu};}
}
const options={...common,mu:minimum.mu},deep=createDeepSplitMomentumEngine(options),g=deep.geometry(minimum.profile,minimum.x);
if(!(g.deepScaled&&g.w2===0))throw Error('The actual deepest source did not exercise w^2 underflow');
const actualRaw=new Float64Array(8);actualRaw[0]=1e-3*g.w/g.r**3;actualRaw[4]=2e-3*g.w/(Math.sqrt(6)*g.r**3);
const initial=deep.initializeFromRaw(actualRaw,minimum.profile,minimum.x),f=deep.rhsWithJacobian(initial.state,minimum.profile,minimum.x),
 jets=createMomentumPhysicalJetEvaluator(deep,{spacing:2})(initial.state,minimum.profile,minimum.x);
if(![...initial.state,...f.derivative,...f.jacobian,...jets.Ldot,...jets.perAngle.flatMap(v=>Object.values(v))].every(Number.isFinite))throw Error('Nonfinite actual deep value');
// A lifted copy in the normal range gives the same normalized root and flow
// up to terms <1e-180; Q/raw height scale by s, pi and normalized L do not.
const shift=-200-g.logw,scale=Math.exp(shift),liftedOptions={...common,mu:minimum.mu*Math.exp(2*shift)},
 lifted=oldEngine(liftedOptions),lp=x=>{const q=minimum.profile(x);return {...q,logw:q.logw+shift};},
 ly=Float64Array.from(initial.state,(v,j)=>j<4||j>=8?v*scale:v),lf=lifted.rhsWithJacobian(ly,lp,minimum.x),
 lj=createOldJets(lifted,{spacing:2})(ly,lp,minimum.x),
 convertedField=Float64Array.from(lf.derivative,(v,j)=>j<4||j>=8?v/scale:v),
 convertedJac=Float64Array.from(lf.jacobian,(v,j)=>{const row=Math.floor(j/8),col=j%8;return v*(col<4?scale:1)/(row<4||row>=8?scale:1);}),
 liftedComparison={root:diff(f.root.L,lf.root.L),rhs:diff(f.derivative,convertedField),jacobian:diff(f.jacobian,convertedJac),Ldot:diff(jets.Ldot,lj.Ldot)};
const report={status:'actual arithmetic checks completed',started_ms:started,elapsed_seconds:(Date.now()-started)/1000,
 config:{path:configFile,sha256:crypto.createHash('sha256').update(configBytes).digest('hex')},normal,
 actualDeep:{rawCell:minimum.rawCell,rawSegment:minimum.rawSegment,x:minimum.x,geometry:minimum.g,mu:minimum.mu,w:g.w,w2:g.w2,
   rootResidual:f.root.err,rootRelativeResidual:f.root.err/f.root.scale,minA:f.root.e.minA,minD:f.root.e.minD,
   normalizedDarboux:jets.maxNormalizedDarboux,physicalDarbouxUnderflowCount:jets.physicalDarbouxUnderflowCount,
   allRootRhsJacobianAndPhysicalJetsFinite:true},lifted:{shift,scale,mu:liftedOptions.mu,...liftedComparison},cache,
 scope:'Actual local arithmetic only. No complete nonlinear DN response, radial convergence, or infinite-tail assertion.'};
fs.writeFileSync(outFile,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({outFile,normal,actualDeep:report.actualDeep,lifted:liftedComparison,elapsed_seconds:report.elapsed_seconds}));
