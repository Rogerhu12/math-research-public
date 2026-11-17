// Actual full Cartesian node two-jets for an explicit shared-jet C2 map.
// This postprocessor uses the original positive Gram root at each stable node.
// It is not a mixed-DAE continuation through a singular Gram matrix.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const [topicArg,inputArg,checkpointArg,outArg,fdArg='0.0001',subsamplesArg='4']=process.argv.slice(2);
const topic=path.resolve(topicArg),input=path.resolve(inputArg),checkpoint=path.resolve(checkpointArg),out=path.resolve(outArg);
const radialDifferenceStep=Number(fdArg),subsamples=Number(subsamplesArg);
if(!(radialDifferenceStep>0&&Number.isInteger(subsamples)&&subsamples>0))throw Error('Invalid audit resolution');
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const original=process.env.CLOSING_TAIL_CACHE;
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-subdivision.mjs')));
const {createMomentumTailEngine}=await import(pathToFileURL(path.join(original,'general_root_tail_momentum.mjs')));
const {createRelativeSpatialJetEvaluator}=await import(pathToFileURL(path.join(original,'f6tail_relative_spatial_jets.mjs')));
const digest=file=>createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const packed=JSON.parse(gunzipSync(fs.readFileSync(input))),rec=JSON.parse(gunzipSync(fs.readFileSync(checkpoint)));
if(digest(checkpoint)!==packed.checkpoint_sha256)throw Error('Checkpoint hash differs');
const cp=rec.response?.checkpoint??rec.checkpoint??rec,cfg=rec.config??cp.parameters;
if(cp.parameters.constructor!=='closing_weighted_tail_v1')throw Error('Wrong physical constructor');
const M=cp.parameters.modes,N=cp.parameters.quadrature,spacing=cp.parameters.spacing;
if(M!==packed.parameters.M||N!==packed.parameters.N)throw Error('Angular dimensions differ');
const physical=createRecalibrationFactory(cfg).assemble();
const stages=subdividePhysical(physical,cp.parameters.physicalDepth??cfg.depth,cfg.shootingParts??1);
if(JSON.stringify(stages.rawNode)!==JSON.stringify(cp.rawNode))throw Error('Stage map differs');
const rawCell=packed.parameters.rawCell,cell=physical.cells[rawCell];
const engine=createMomentumTailEngine({modes:M,quadrature:N,spacing,mu:cell.mu,orientation:1,projectionFloor:cp.parameters.projectionFloor});
const evaluator=createRelativeSpatialJetEvaluator(engine,{spacing,radialDifferenceStep});
const rOuter=packed.nodes[0].r;
const maxDiff=(a,b)=>Math.max(...a.flat(2).map((v,j)=>Math.abs(v-b.flat(2)[j])));

function evaluate(node,stageNumber,t){
  const p=stages.cells[stageNumber].profiles[0],g=p(t),r=g.r,w=Math.exp(g.logw);
  const state=new Float64Array(2*M+2);
  // Preserve physical h=rwv and p=w^2 t across tiny endpoint roundoff.
  for(let j=0;j<M;j++){
    const h=node.r*node.w*node.Y[j],momentum=node.w*node.w*node.Y[M+j];
    state[j]=Math.SQRT2*h/r**4;
    state[M+j]=Math.SQRT2*r**4*momentum/(Math.sqrt(12)*cell.mu);
  }
  const q=evaluator.evaluate(state,p,t),wr=w*g.dlogwdx/g.drdx;
  const jets=q.perAngle.map((v,j)=>{
    const u=2*Math.PI*j/N,c=Math.cos(u),s=Math.sin(u);
    return [[r*c+v.V[0],r*s+v.V[1],v.V[2]],
            [c+v.Vr[0],s+v.Vr[1],w+v.Vr[2]],
            [v.Vrr[0],v.Vrr[1],wr+v.Vrr[2]],
            [-r*s+v.Vt[0],r*c+v.Vt[1],v.Vt[2]],
            [-s+v.Vrt[0],c+v.Vrt[1],v.Vrt[2]],
            [-r*c+v.Vtt[0],-r*s+v.Vtt[1],v.Vtt[2]]];
  });
  return {r,w,wr,jets,relative_jets:q.perAngle.map(v=>[v.V,v.Vr,v.Vrr]),rootL:q.root.L,
    audit:{root_relative:q.heightJets.rootRelativeResidual,minA:q.heightJets.minA,minD:q.heightJets.minD,
      minS:q.root.e.minS,holonomy:q.heightJets.physicalHolonomyResidual,
      L_change_from_mixed:Math.max(...q.root.L.map((v,j)=>Math.abs(v-node.Y[2*M+j])))}};
}

function invertRadius(p,r){
  if(r<=p(0).r)return 0;if(r>=p(1).r)return 1;
  let lo=0,hi=1;
  for(let k=0;k<54;k++){const m=(lo+hi)/2;if(p(m).r<r)lo=m;else hi=m;}
  return (lo+hi)/2;
}

const nodes=[],joins=[];
for(let i=0;i<packed.nodes.length;i++){
  const n=packed.nodes[i],v=evaluate(n,n.stage,n.local_parameter);
  nodes.push({x:n.x,stage:n.stage,raw_segment:n.raw_segment,local_parameter:n.local_parameter,...v});
  if(n.local_parameter===0&&n.stage+1<packed.parameters.lastStageExclusive){
    const alt=evaluate(n,n.stage+1,1);
    joins.push({node:i,left_stage:n.stage,right_stage:n.stage+1,
      background_difference:[Math.abs(v.r-alt.r),Math.abs(v.w-alt.w),Math.abs(v.wr-alt.wr)],
      cartesian_jet_difference:Array.from({length:6},(_,k)=>maxDiff(v.jets.map(a=>a[k]),alt.jets.map(a=>a[k]))),
      shared_choice:'outer-stage inner endpoint; both adjacent quintics use these same literal data'});
  }
  if(i%64===0)console.log(JSON.stringify({event:'node',i,nodes:packed.nodes.length,minA:v.audit.minA}));
}
const samples=[];
for(let i=0;i<nodes.length-1;i++){
  const stage=packed.nodes[i+1].stage,p=stages.cells[stage].profiles[0];
  for(let j=0;j<=subsamples;j++){
    const fraction=j/subsamples,x=nodes[i].x+(nodes[i+1].x-nodes[i].x)*fraction,r=rOuter-x,t=invertRadius(p,r),g=p(t),w=Math.exp(g.logw);
    samples.push({interval:i,fraction,x,r,w,wr:w*g.dlogwdx/g.drdx,stage,local_parameter:t,radius_inverse_error:Math.abs(g.r-r)});
  }
}
const sourceFiles=['scripts/closing_weighted_tail.mjs','scripts/950f-tail-subdivision.mjs',
  ...['general_root_tail_momentum.mjs','general_root_smooth_tail_cells.cjs','f6tail_momentum_physical_jets.mjs',
      'f6tail_relative_spatial_jets.mjs','f6tail_relative_development.mjs'].map(s=>'repro/source-root/topics/large-amplitude-twist-flex/scripts/'+s)];
const doc={scope:'Full Cartesian two-jets at fixed physical mixed-solution nodes, before explicit global mean integration and shared-jet interpolation. Radial second jets use a recorded finite difference.',
 inputs:{packed:{path:input,sha256:digest(input)},checkpoint:{path:checkpoint,sha256:digest(checkpoint)},...packed.inputs},
 source_sha256:Object.fromEntries(sourceFiles.map(s=>[s,digest(path.join(topic,s))])),exporter_sha256:digest(process.argv[1]),
 parameters:{...packed.parameters,radialDifferenceStep,subsamples,coordinate:'x=rOuter-r; stored derivatives use r',
 angular_frame:'same centered periodic development with zero mean angle primitive at every node',
 mean_position:'zero here; global compatible mean position is assigned by the C2 builder',
 jet_order:['X','Xr','Xrr','Xu','Xru','Xuu']},nodes,joins,samples};
fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,gzipSync(JSON.stringify(doc)));
console.log(JSON.stringify({event:'completed',out,sha256:digest(out),nodes:nodes.length,samples:samples.length,joins:joins.length}));
