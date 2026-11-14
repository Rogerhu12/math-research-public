import fs from 'node:fs';
import zlib from 'node:zlib';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {subdividePhysical} from './fd2d-gc-tail-stage-graphs.mjs';
import {createDeepSplitMomentumEngine} from './fd2d-gc-tail-deep-engine.mjs';
import {prepareGeometricNodeRetraction as oldRetraction} from './fd2d-gc-tail-deep-retraction-centered.mjs';
import {prepareGeometricNodeRetraction as normalizedRetraction} from './fd2d-gc-tail-normalized-retraction.mjs';
const [configFile,checkpointFile,outFile]=process.argv.slice(2),cfg=JSON.parse(fs.readFileSync(configFile)),
 record=JSON.parse(zlib.gunzipSync(fs.readFileSync(checkpointFile))),factory=createRecalibrationFactory(cfg);
boundTailPointCaches(factory,cfg,{pointsPerEntry:8});
const physical=factory.assemble(),stages=subdividePhysical(physical,160,cfg.shootingParts),
 cell=stages.cells[2640],M=cfg.modes,K=2*M,
 engine=createDeepSplitMomentumEngine({modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,mu:cell.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor}),
 state=Float64Array.from(record.checkpoint.states[2640]),delta=new Float64Array(K);
delta[M]=1e-278;
const opts={engine,profile:cell.profiles.at(-1),x:1,state,delta,spacing:cfg.spacing,portRatio:1},
 old=oldRetraction(opts),fresh=normalizedRetraction(opts),a=old.step(1,{detail:true}),b=fresh.step(1,{detail:true}),
 deep={stage:2640,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
  inputPi:state[M],requestedCanonicalDirection:delta[M],
  oldPhysicalRawDirection:old.rawDirection[M],
  oldActualCanonicalIncrement:a.state[M]-state[M],
  normalizedActualCanonicalIncrement:b.state[M]-state[M],
  normalizedDirectionError:(b.state[M]-state[M]-delta[M])/delta[M],
  normalizedLDirection:fresh.normalizedDirection[1],
  old:a.diagnostics,normalized:b.diagnostics};
deep.oldCanonicalRelativeDirectionError=(deep.oldActualCanonicalIncrement-delta[M])/delta[M];
if(Math.abs(deep.normalizedDirectionError)>1e-10)throw Error('Normalized retraction lost the actual tiny canonical direction');
const profile=x=>({r:.47+.004*x,drdx:.004,logw:Math.log(.018)+.08*x,dlogwdx:.08}),
 e=createDeepSplitMomentumEngine({modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,mu:.00013,orientation:1,projectionFloor:.05}),
 raw=Float64Array.from([1e-6,-2e-8,3e-10,-4e-12,4e-7,-5e-9,6e-11,-7e-13]),
 initial=e.initializeFromRaw(raw,profile,.37).state.slice(0,K),direction=Float64Array.from(initial,(v,j)=>v*(j%2?.03:-.02)),
 normalOpts={engine:e,profile,x:.37,state:initial,delta:direction,spacing:cfg.spacing},
 oldNormal=oldRetraction(normalOpts).step(.5,{detail:true}),newNormal=normalizedRetraction(normalOpts).step(.5,{detail:true}),
 normalDifference=Math.max(...oldNormal.state.map((v,j)=>Math.abs(v-newNormal.state[j])));
const report={status:'actual local retraction check completed',checkpointFile,deep,
 normal:{maximum_state_difference:normalDifference,old:oldNormal.diagnostics,normalized:newNormal.diagnostics},
 scope:'Same exact Q/L retraction, local floating arithmetic check only. No complete DN or newly accepted state.'};
fs.writeFileSync(outFile,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({outFile,deep:{...deep,old:undefined,normalized:undefined},normalDifference}));
