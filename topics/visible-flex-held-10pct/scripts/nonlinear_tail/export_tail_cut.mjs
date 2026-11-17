// Actual R16-developed Cartesian cut two-jets from a finite nonlinear tail.
// The planar rr jet uses the published fourth-order difference evaluator.
import fs from 'node:fs';import path from 'node:path';import{pathToFileURL}from'node:url';import{gunzipSync,gzipSync}from'node:zlib';import{createHash}from'node:crypto';
const[topic,input,out,nArg='512',hArg='.0001']=process.argv.slice(2);const N=Number(nArg),dh=Number(hArg);if(!out)throw Error('topic response.gz out.gz [N=512] [profile_difference_step=.0001]');
const root=path.join(topic,'repro/source-root');process.env.VISIBLE_FLEX_SOURCE_ROOT=root;process.env.CLOSING_TAIL_CACHE=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const source=n=>pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,n));
const{createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const{createFastSplitFluxMomentumTailEngine}=await import(source('f6tail_fast_split_flux_engine.mjs'));
const{withCuspAwareRK}=await import(source('f6tail_cusp_grid.mjs'));
const{createRelativeSpatialJetEvaluator}=await import(source('f6tail_relative_spatial_jets.mjs'));
const bytes=fs.readFileSync(input),record=JSON.parse((input.endsWith('.gz')?gunzipSync(bytes):bytes).toString()),cp=record.response?.checkpoint??record.checkpoint??record,p=cp.parameters,M=p.modes;
const physical=createRecalibrationFactory(record.config??p).assemble(),cell=physical.cells[0],profile=cell.profiles.at(-1);let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});engine=withCuspAwareRK(engine);
const y=new Float64Array(2*M+2);y.set(cp.states[0]);for(let j=0;j<M;j++)y[M+j]*=2**p.a;
const ev=createRelativeSpatialJetEvaluator(engine,{spacing:p.spacing,radialDifferenceStep:dh}),z=ev.evaluate(y,profile,1),g=z.g,wr=g.w*g.dlogwdx/g.drdx;
const jets=z.perAngle.map(v=>{const c=Math.cos(v.theta),s=Math.sin(v.theta);return{u:v.theta,X:[g.r*c+v.V[0],g.r*s+v.V[1],v.V[2]],Xr:[c+v.Vr[0],s+v.Vr[1],g.w+v.Vr[2]],Xu:[-g.r*s+v.Vt[0],g.r*c+v.Vt[1],v.Vt[2]],Xrr:[v.Vrr[0],v.Vrr[1],wr+v.Vrr[2]],Xru:[-s+v.Vrt[0],c+v.Vrt[1],v.Vrt[2]],Xuu:[-g.r*c+v.Vtt[0],-g.r*s+v.Vtt[1],v.Vtt[2]]};});
const result={scope:'Finite nonlinear R16 Cartesian two-jets; mean z at cut is zero. Upper-surface use reflects the entire z coordinate then translates. A complete seam is a separate test. Planar rr is finite difference, not exact.',input,inputSHA256:createHash('sha256').update(bytes).digest('hex'),parameters:p,angular:N,profileDifferenceStep:dh,cut:{r:g.r,w:g.w,wr,drdx:g.drdx},diagnostics:{minA:z.heightJets.minA,minD:z.heightJets.minD,fullD:z.heightJets.maxDarboux,formalK:z.heightJets.formalHeightCurvature,metric:z.development.actualMetricRelativeOperatorError,rootRelative:z.heightJets.rootRelativeResidual},jets};fs.writeFileSync(out,gzipSync(JSON.stringify(result)+'\n'));console.log(JSON.stringify({out,cut:result.cut,diagnostics:result.diagnostics}));
