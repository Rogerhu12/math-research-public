// Analytic finite-tail cut slope derivative on the actual shooting graph.
// This module does not change the tail equations, metric, state, or branch.
// It consumes the source DN object's actual variational shooting graph.
// All numerical matrices are row-major, with physical height columns.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

export function actualSlopeJacobian(dn, solution) {
  const tail=dn.tail, M=tail.parameters.modes, K=2*M;
  const node=solution.states?.[0];
  if(!node || node.length!==K)throw Error('Complete actual cut shooting state required');
  const cell=tail.cells[0], engine=cell.engine, profile=cell.profiles.at(-1);
  const rho=2**tail.parameters.a, y=new Float64Array(K+2);
  y.set(node);
  for(let j=0;j<M;j++)y[M+j]*=rho;
  const field=engine.rhsWithJacobian(y,profile,1), g=field.root.g;
  const graph=dn.tangentGraphAtCut(solution);
  if(graph.length!==M*M || field.jacobian.length!==(K+2)*K)
    throw Error('Actual variational graph dimensions disagree');
  if(!(g.r>0 && Number.isFinite(g.drdx) && g.drdx!==0))
    throw Error('Regular physical cut radial chart required');
  const slope=new Float64Array(M), slopeJacobian=new Float64Array(M*M);
  const meanSlopeJacobian=new Float64Array(M), J=field.jacobian;
  // Q=H/r^4.  The DN node momentum is rescaled by rho at the cut.
  // From Q_x=(r_x/r)[(m^2-4)Q+sqrt(2)w L/r^3],
  // Z_r[m]=r^4 Q_x/r_x+4r^3Q.
  // Therefore d Z_r/d H=(F_Q+rho F_pi G)/r_x+(4/r)I.
  for(let i=0;i<M;i++) {
    slope[i]=g.r**4*field.derivative[i]/g.drdx+4*g.r**3*y[i];
    for(let k=0;k<M;k++) {
      let v=J[i*K+k];
      for(let j=0;j<M;j++)v+=rho*J[i*K+M+j]*graph[j*M+k];
      slopeJacobian[i*M+k]=v/g.drdx+(i===k?4/g.r:0);
    }
  }
  // The mean state derivative is r_x w L_0, so its cut slope
  // derivative has an additional r^(-4) conversion from Q to H.
  for(let k=0;k<M;k++) {
    let v=J[K*K+k];
    for(let j=0;j<M;j++)v+=rho*J[K*K+M+j]*graph[j*M+k];
    meanSlopeJacobian[k]=v/(g.drdx*g.r**4);
  }
  return {
    slope, slopeJacobian, meanSlopeCorrection:field.derivative[K]/g.drdx,
    meanSlopeJacobian, graph,
    scope:'Analytic derivative of the finite nonlinear shooting DN first slope and mean slope on its retained positive branch. Finite Fourier/radial/depth convergence remains separate.',
    dimensions:{modes:M,columns:'physical cut height H_j',layout:'row-major'},
    cut:{radius:g.r,radialChartDerivative:g.drdx,momentumRescale:rho},
    root:{minA:field.root.e.minA,minD:field.root.e.minD,minS:field.root.e.minS,relativeResidual:field.root.err/field.root.scale}
  };
}

export function replaceFirstSlopeRows(heightJetJacobian, actual) {
  // Preserve source second-jet rows, which still use a symmetric difference.
  const M=actual.dimensions.modes, out=Float64Array.from(heightJetJacobian);
  if(out.length!==(3*M+2)*M)throw Error('Source height-jet matrix dimensions disagree');
  out.set(actual.slopeJacobian,0);
  out.set(actual.meanSlopeJacobian,2*M*M);
  return out;
}

function readRecord(file) {
  const bytes=fs.readFileSync(file);
  return JSON.parse((file.endsWith('.gz')?zlib.gunzipSync(bytes):bytes).toString());
}
const sha256=file=>crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const maximum=v=>Math.max(0,...Array.from(v,Math.abs));

async function main() {
  const [sourceTopic, responseFile, outputFile]=process.argv.slice(2);
  if(!sourceTopic || !responseFile || !outputFile)
    throw Error('Usage: node numerical-tail-slope-jacobian.mjs SOURCE_TOPIC RESPONSE.json.gz OUTPUT.json');
  const started=Date.now(), sourceRoot=path.join(sourceTopic,'repro/source-root');
  process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
  process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
  const moduleURL=name=>pathToFileURL(path.join(sourceTopic,'scripts',name));
  const {createRecalibrationFactory}=await import(moduleURL('closing_weighted_tail.mjs'));
  const {createSplitFluxCompactTailDN}=await import(moduleURL('78718-tail-tangent-split.mjs'));
  const {createFourierRootSplitFluxEngine}=await import(moduleURL('78718-tail-fourier-root-split-engine.mjs'));
  const record=readRecord(responseFile), response=record.response;
  if(!response?.converged || response.failed)throw Error('A successful actual nonlinear tail response is required');
  const config=record.config, M=config.modes, physical=createRecalibrationFactory(config).assemble();
  const dn=createSplitFluxCompactTailDN({...config,tail:physical,retainTangentPredictor:true});
  const transformed=new Set();
  for(const cell of dn.tail.cells) {
    if(transformed.has(cell.engine))continue;
    transformed.add(cell.engine);
    Object.assign(cell.engine,createFourierRootSplitFluxEngine({
      modes:M,spacing:config.spacing,quadrature:config.quadrature,mu:cell.mu,
      orientation:dn.tail.parameters.orientation,projectionFloor:dn.tail.parameters.projectionFloor,
      cuspAwareFlow:config.cuspAwareFlow===true
    }));
  }
  const sol={states:response.checkpoint.states};
  const actual=actualSlopeJacobian(dn,sol), jets=dn.cutJets(sol.states[0]);
  const sourceJ=dn.heightJetJacobian(sol), sourceMatrix=sourceJ.matrix;
  const difference=Array.from(actual.slopeJacobian,(v,k)=>v-sourceMatrix[k]);
  const meanDifference=Array.from(actual.meanSlopeJacobian,(v,k)=>v-sourceMatrix[2*M*M+k]);
  const slopeIdentity=Array.from(actual.slope,(v,k)=>v-jets.slope[k]);
  // A second independent scale on the same tangent graph checks the expected
  // truncation/roundoff behavior of the source symmetric difference.
  const finer=dn.heightJetJacobian(sol,{differenceStep:2e-5});
  const fineDifference=Array.from(actual.slopeJacobian,(v,k)=>v-finer.matrix[k]);
  const fineMeanDifference=Array.from(actual.meanSlopeJacobian,(v,k)=>v-finer.matrix[2*M*M+k]);
  const result={
    scope:actual.scope,
    source_revision:readRecord(path.join(sourceTopic,'source-origin.json')).source_revision,
    response_file:responseFile,response_sha256:sha256(responseFile),
    input_scope:'Same successful actual mixed-mode response; no amplitude, metric, depth, modes, or discretization changed.',
    source_response_residual:response.residual,source_response_audit:response.audit??null,
    physical_height:record.request.height,jets,
    ...actual,
    slope:Array.from(actual.slope),slopeJacobian:Array.from(actual.slopeJacobian),
    meanSlopeJacobian:Array.from(actual.meanSlopeJacobian),graph:Array.from(actual.graph),
    comparison:{
      source_endpoint_method:'symmetric difference along the actual variational graph',
      source_difference_step:sourceJ.differenceStep,finer_difference_step:finer.differenceStep,
      slope_identity_max:maximum(slopeIdentity),
      mean_identity_error:actual.meanSlopeCorrection-jets.meanSlopeCorrection,
      source_slope_jacobian_max:maximum(sourceMatrix.slice(0,M*M)),
      analytic_minus_source_max:maximum(difference),
      analytic_minus_source_relative:maximum(difference)/Math.max(1,maximum(actual.slopeJacobian)),
      analytic_minus_finer_max:maximum(fineDifference),
      mean_analytic_minus_source_max:maximum(meanDifference),
      mean_analytic_minus_finer_max:maximum(fineMeanDifference)
    },
    source_sha256:{...record.source_sha256,
      'numerical-tail-slope-jacobian.mjs':sha256(new URL(import.meta.url)),
      '78718-tail-tangent-core.mjs':sha256(path.join(sourceTopic,'scripts/78718-tail-tangent-core.mjs')),
      '78718-tail-fourier-product-jacobian.mjs':sha256(path.join(sourceTopic,'scripts/78718-tail-fourier-product-jacobian.mjs'))
    },seconds:(Date.now()-started)/1000
  };
  const output=JSON.stringify(result,null,2)+'\n';
  if(Buffer.byteLength(output)>=1_000_000)throw Error('Unexpectedly large derivative report');
  fs.writeFileSync(outputFile,output,{flag:'wx'});
  console.log(JSON.stringify({output:outputFile,comparison:result.comparison,seconds:result.seconds}));
}
if(process.argv[1] && import.meta.url===pathToFileURL(path.resolve(process.argv[1])).href)
  await main();
