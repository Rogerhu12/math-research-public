// Compare momentum-zero-padding with geometric Q/L embedding at a saved point.
// No shooting solve and no candidate output is produced.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
const srcRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
const src=name=>pathToFileURL(path.join(srcRoot,'topics/large-amplitude-twist-flex/scripts',name));
const {createFastSplitFluxMomentumTailEngine}=await import(src('f6tail_fast_split_flux_engine.mjs'));
const {createMomentumPhysicalJetEvaluator}=await import(src('f6tail_momentum_physical_jets.mjs'));
const {actualMetricFromDarbouxJets}=await import(src('f6tail_actual_metric.mjs'));
const {withCuspAwareRK}=await import(src('f6tail_cusp_grid.mjs'));
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.packet||!opt.out||fs.existsSync(opt.out))throw Error('input and fresh output required');
const started=Date.now(),pb=fs.readFileSync(opt.packet),packet=JSON.parse(zlib.gunzipSync(pb)),cfg=packet.config,cp=packet.response.checkpoint,oldM=cfg.modes,oldN=cfg.quadrature;
const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),stage=Number(opt.stage??34),x=Number(opt.x??.125),c=stages.cells[stage],p=c.profiles[0];
const steps=cfg.steps,count=x*steps;if(!Number.isInteger(count)||count<0||count>steps)throw Error('point must be on original integration grid');
function engine(M,N){let e=createFastSplitFluxMomentumTailEngine({modes:M,spacing:cfg.spacing,quadrature:N,mu:c.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05});return cfg.cuspAwareFlow?withCuspAwareRK(e):e;}
const old=engine(oldM,oldN);let state=new Float64Array(2*oldM+2);state.set(cp.states[stage+1]);for(let k=0;k<count;k++)state=old.rk4(state,p,k/steps,1/steps);
const root=old.root(state,p,x),raw=old.toRaw(state,p,x,root),baseJets=createMomentumPhysicalJetEvaluator(old,{spacing:cfg.spacing})(state,p,x),baseMetric=actualMetricFromDarbouxJets(root.g,baseJets.perAngle);
function metrics(e,s){const j=createMomentumPhysicalJetEvaluator(e,{spacing:cfg.spacing})(s,p,x),g=e.geometry(p,x),m=actualMetricFromDarbouxJets(g,j.perAngle);let urGap=0,utGap=0,urrGap=0,urtGap=0,heightGap=0;const ratio=e.N/oldN;if(!Number.isInteger(ratio))throw Error('nested N required');for(let k=0;k<oldN;k++){const a=j.perAngle[k*ratio],b=baseJets.perAngle[k];urGap=Math.max(urGap,Math.abs(a.ur-b.ur));utGap=Math.max(utGap,Math.abs(a.ut-b.ut));urrGap=Math.max(urrGap,Math.abs(a.urr-b.urr));urtGap=Math.max(urtGap,Math.abs(a.urt-b.urt));heightGap=Math.max(heightGap,Math.abs(a.height-b.height));}let omegaWeightedMeanSquare=0;for(const v of j.perAngle){const S=g.r*g.r-v.ut*v.ut,D=g.E*S-g.r*g.r*v.ur*v.ur,om=v.darboux*g.E*g.E*g.r**4/(D*Math.sqrt(D)),A=1+(v.ur/g.w-1)+(g.E*v.utt/(g.r*g.w)),weight=g.w*A/(D/g.r**2)**1.5;omegaWeightedMeanSquare+=om*om/weight/e.N;}
 return {metric:m.actualMetricRelativeOperatorError,rr:m.actualMetricRelativeRR,rt:m.actualMetricRelativeRT,tt:m.actualMetricRelativeTT,fullD:j.maxDarboux,minLeading:j.minA,minD:j.minD,rootResidual:j.rootRelativeResidual,urGap,utGap,urrGap,urtGap,heightGap,omegaWeightedMeanSquare};}
const rows=[],modes=String(opt.modes??'18,22,26,32,40').split(',').map(Number),quadratures=String(opt.quadratures??String(oldN)).split(',').map(Number);
for(const N of quadratures)for(const M of modes){if(M<oldM)throw Error('only prolongation');const e=engine(M,N),zero=new Float64Array(2*M+2);for(let j=0;j<oldM;j++){zero[j]=state[j];zero[M+j]=state[oldM+j];}zero[2*M]=state[2*oldM];zero[2*M+1]=state[2*oldM+1];const zr=metrics(e,zero);
 const extendedRaw=new Float64Array(2*M);for(let j=0;j<oldM;j++){extendedRaw[j]=raw.raw[j];extendedRaw[M+j]=raw.raw[oldM+j];}const init=e.initializeFromRaw(extendedRaw,p,x),s=init.state;s[2*M]=state[2*oldM];s[2*M+1]=state[2*oldM+1];let lowPiChange=0,highPi=0,piScale=0;for(let j=0;j<oldM;j++){lowPiChange=Math.max(lowPiChange,Math.abs(s[M+j]-state[oldM+j]));piScale=Math.max(piScale,Math.abs(state[oldM+j]));}for(let j=oldM;j<M;j++)highPi=Math.max(highPi,Math.abs(s[M+j]));const gr=metrics(e,s);rows.push({modes:M,quadrature:N,momentumZeroPadding:zr,geometricEmbedding:gr,relativeLowPiChange:lowPiChange/Math.max(piScale,1e-300),relativeNewHighPi:highPi/Math.max(piScale,1e-300),meanRootResidual:init.normalizedMeanResidual});console.log(JSON.stringify({modes:M,quadrature:N,zero:zr.metric,geometric:gr.metric,urGap:gr.urGap,elapsedSeconds:(Date.now()-started)/1000}));}
const report={scope:'Local higher-M initial-jet comparison only. Same-N Q/L embedding preserves the exact discrete root in exact arithmetic; different N may alter the mean root. No high-M trajectory or coupled solution is claimed.',packet:{path:path.resolve(opt.packet),bytes:pb.length,sha256:crypto.createHash('sha256').update(pb).digest('hex')},program:{path:path.resolve(process.argv[1]),sha256:crypto.createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex')},originalModes:oldM,originalQuadrature:oldN,stage,rawCell:c.rawCell,rawSegment:c.rawSegment,part:c.part,x,r:root.g.r,mu:c.mu,orientation:cfg.orientation,baseMetric:baseMetric.actualMetricRelativeOperatorError,base:metrics(old,state),rows,elapsedSeconds:(Date.now()-started)/1000};fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,elapsedSeconds:report.elapsedSeconds}));
