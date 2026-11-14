// Full XYZ endpoint packets for the fixed-metric R6 collar construction.
// Coefficients define finite angular polynomials exactly as binary reals.
// Their relation to the continuous shooting solution is numerical, not certified.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';

const {values,positionals}=parseArgs({allowPositionals:true,options:{
  'source-root':{type:'string'}, 'nodes':{type:'string',default:'4,6,8,10,12'},
  'angular-nodes':{type:'string',default:'256'},
  'difference-step':{type:'string',default:'0.00005'},
  'symmetry':{type:'string',default:'c3'},
  'background-curvature':{type:'string',default:'6.001'}}});
if(positionals.length!==2||!values['source-root'])throw Error('checkpoint output --source-root ROOT required');
const [input,out]=positionals;
if(fs.existsSync(out))throw Error('Refusing to overwrite earlier packet');
const sourceRoot=path.resolve(values['source-root']),here=path.dirname(fileURLToPath(import.meta.url));
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const source=name=>pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,name));
const readJson=f=>JSON.parse((f.endsWith('.gz')?gunzipSync(fs.readFileSync(f)):fs.readFileSync(f)).toString());
const sha=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const record=readJson(input),response=record.response??record;
const cp=response.checkpoint??response.tail_checkpoint??response.seam?.tail_checkpoint??response;
if(!cp.parameters||!cp.states)throw Error('No tail checkpoint');
const p=cp.parameters,M=p.modes,K=2*M,rawStates=cp.rawStates??cp.states;
const nodes=values.nodes.split(',').map(Number),N=Number(values['angular-nodes']),h=Number(values['difference-step']),B=Number(values['background-curvature']);
if(!(Number.isInteger(N)&&N>=32&&(N&(N-1))===0))throw Error('power of 2 angular nodes required');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(source('f6tail_fast_split_flux_engine.mjs'));
const {withCuspAwareRK}=await import(source('f6tail_cusp_grid.mjs'));
const {createRelativeSpatialJetEvaluator}=await import(source('f6tail_relative_spatial_jets.mjs'));
const factory=createRecalibrationFactory(record.config??p),physical=factory.assemble(),a=physical.parameters.rCuff;
const keys=['rCut','wCut','width','curvatureBound','delta0','R','a','etaPower','etaRatioAtN0','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','calibrationSteps','warpSteps','quadratureTolerance','slopeCap','capTransition','capMode','cuspAwareQuadrature','valleyControls','pulseCaps','valleyCaps','warpWeightLevels','rCuff','epsilonScale'];
for(const key of keys)if(JSON.stringify(p[key]??null)!==JSON.stringify(physical.parameters[key]??null))throw Error('physical parameter mismatch '+key);

function coefficients(samples){
  // a0+sum_{k=1}^{N/2}(ak cos k theta+bk sin k theta), b_N/2=0.
  const ans=[];
  for(let k=0;k<=N/2;k++){
    const c=[0,0,0],s=[0,0,0],f=(k===0||k===N/2)?1/N:2/N;
    for(let j=0;j<N;j++){
      const z=2*Math.PI*j*k/N,co=Math.cos(z),si=Math.sin(z);
      for(let q=0;q<3;q++){c[q]+=samples[j][q]*co*f;if(k&&k<N/2)s[q]+=samples[j][q]*si*f;}
    }
    ans.push({frequency:k,cos:c,sin:s});
  }
  return ans;
}
function norm(rows){return rows.reduce((s,v)=>s+(1+v.frequency)**2*(v.cos.reduce((a,b)=>a+Math.abs(b),0)+v.sin.reduce((a,b)=>a+Math.abs(b),0)),0);}
function project(rows){
  if(values.symmetry==='none')return rows;
  if(values.symmetry!=='c3')throw Error('symmetry must be c3 or none');
  return rows.map(v=>{
    const m=v.frequency,co=[0,0,m%3===0?v.cos[2]:0],si=[0,0,0];
    if(m%3){const sign=m%3===1?1:-1,xy=(v.cos[0]+sign*v.sin[1])/2;co[0]=xy;si[1]=sign*xy;}
    return {frequency:m,cos:co,sin:si};
  });
}
const result={status:'numerical-source-packet',scope:'Finite Fourier endpoint polynomials for exact Hermite assembly over one fixed infinite metric. R6 bounds on these polynomials are checked separately using exact arithmetic. These packets do not certify continuous-flow endpoint errors, infinite nonlinear continuation, or common-exterior C2 Cauchy convergence.',input:path.resolve(input),inputSHA256:sha(input),sourceSHA256:Object.fromEntries([fileURLToPath(import.meta.url),...['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs','closing_tail_sources.mjs'].map(f=>path.join(here,f)),...['f6tail_relative_spatial_jets.mjs','f6tail_relative_development.mjs','f6tail_fast_split_flux_engine.mjs','f6tail_momentum_physical_jets.mjs'].map(f=>path.join(process.env.CLOSING_TAIL_CACHE,f))].map(f=>[f,sha(f)])),parameters:{...p},settings:{angularNodes:N,radialDifferenceStep:h,assumedBackgroundCurvature:B,symmetry:values.symmetry},gauge:'Centered planar primitive; at each selected port the nonradial mean height is chosen zero. Exterior height must be shifted to this port gauge before assembly, and inter-depth gauge differences must be controlled.',rows:[]};
for(const n of nodes){
  if(!(Number.isInteger(n)&&n>0&&n<rawStates.length))continue;
  const cell=physical.cells[n-1],profile=cell.profiles[0];
  let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});
  engine=withCuspAwareRK(engine);
  const y=new Float64Array(K+2);y.set(rawStates[n]);
  const ev=createRelativeSpatialJetEvaluator(engine,{spacing:p.spacing,radialDifferenceStep:h}),z=ev.evaluate(y,profile,0);
  const original=[coefficients(z.perAngle.map(v=>v.V)),coefficients(z.perAngle.map(v=>v.Vr)),coefficients(z.perAngle.map(v=>v.Vrr))],coeff=original.map(project);
  const projectionChangeNorm=original.map((rows,j)=>norm(rows.map((v,k)=>({frequency:v.frequency,cos:v.cos.map((x,l)=>x-coeff[j][k].cos[l]),sin:v.sin.map((x,l)=>x-coeff[j][k].sin[l])}))));
  const norms=coeff.map(norm),L=z.g.r-a,kn=norms[0]/L**2+norms[1]/L+norms[2],ell=L/a,eta1=Math.sqrt(5)*L*kn,eta2=kn*Math.sqrt((12+2*L*B)**2+3*(2*ell+ell**2)**2);
  const row={rawNode:n,r:z.g.r,cuff:a,L,sourceSlopes:{w:z.g.w,wr:z.g.w*z.g.dlogwdx/z.g.drdx},norms,K:kn,eta1,eta2,metricUpper:2*eta1+eta1**2,fullTensorUpper:Math.sqrt(2)*B*eta2+.5*eta2**2+B**2*(2*eta1+eta1**2),curvatureUpper:(B+eta2)/(1-eta1)**2,projectionChangeNorm,endpointDiagnostics:{metric:z.development.actualMetricRelativeOperatorError,leading:z.heightJets.minA,projection:z.heightJets.minD,fullD:z.heightJets.maxDarboux,meanSlopeCorrection:z.g.w*z.root.L[0]},coefficients:coeff};
  result.rows.push(row);console.log(JSON.stringify({node:n,L,K:kn,metricUpper:row.metricUpper,fullTensorUpper:row.fullTensorUpper,curvatureUpper:row.curvatureUpper}));
}
fs.writeFileSync(out,JSON.stringify(result)+'\n');
