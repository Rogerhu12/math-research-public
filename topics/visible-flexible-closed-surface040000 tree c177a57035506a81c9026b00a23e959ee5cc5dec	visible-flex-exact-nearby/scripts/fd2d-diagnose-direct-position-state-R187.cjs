#!/usr/bin/env node
/* Stream finite real-position geometry for an immutable R187 state.
 * No BVP, no Jacobian, no DFT, no continuous certificate.
 */
"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {createR187}=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs");
const {createR187Provider}=require("./fd2d-direct-position-metric-provider-R187.cjs");
const {createR187Geometry}=require("./fd2d-direct-position-two-jet-geometry-R187.cjs");
const identity=file=>{const b=fs.readFileSync(file);return {path:file,bytes:b.length,sha256:crypto.createHash("sha256").update(b).digest("hex")};};
function insertTop(array,row,key,limit=6){
  array.push(row);array.sort((a,b)=>b[key]-a[key]);if(array.length>limit)array.pop();
}
function selectedNodes(engine,provider){
  const b=provider.base,J=provider.definition.radialBasisCount,c=b.centralLength,S=b.end,step=(S-c)/(J+3),g=engine.gauss(2);
  let cuts=[0,S,...b.segments.map(p=>p.s0),...b.segments.map(p=>p.s1)];
  for(let j=0;j<=J+3;j++)cuts.push(c+j*step);
  cuts.sort((a,b)=>a-b);cuts=cuts.filter((x,i)=>i===0||x-cuts[i-1]>2e-14);cuts[0]=0;cuts[cuts.length-1]=S;
  const all=[...cuts];
  for(let i=1;i<cuts.length;i++){
    const l=cuts[i-1],h=cuts[i]-l;all.push(l+h/2);
    for(const x of g.x)all.push(l+h*x);
  }
  all.sort((a,b)=>a-b);return all.filter((x,i)=>i===0||x-all[i-1]>2e-14);
}
function diagnostic(engine,provider,geometry,z,angularCount=128){
  const nodes=selectedNodes(engine,provider),b=provider.base;
  const out={count:0,radialCount:nodes.length,angularCount,maxRelativeMetric:0,minImmersion:Infinity,maxCurvature:0,
    minHeight:Infinity,maxHeight:-Infinity,maxSquaredRadius:0,minInwardSupport:Infinity,maxAbsCoordinate:[0,0,0],
    topMetric:[],topCurvature:[],radialSummary:[],nonimmersedSamples:0};
  for(const s of nodes){
    const sl=geometry.slice(s,z),p=b.at(s);
    const piece=b.segments.find(q=>s<=q.s1)||b.segments.at(-1);
    const row={s,piece:piece.label||piece.kind,maxMetric:0,maxCurvature:0,minImmersion:Infinity,maxSquaredRadius:0,minZ:Infinity,maxZ:-Infinity};
    for(let j=0;j<angularCount;j++){
      const u=2*Math.PI*j/angularCount,v=sl.point(u),g=v.geometry;out.count++;
      const short={s,u,piece:row.piece,relativeMetric:g.relativeMetric,curvature:g.curvature,immersion:g.immersion,
        X:v.X,rE:g.rE,rF:g.rF,rG:g.rG,inwardSupport:g.inwardSupport,principalCurvatures:g.principalCurvatures};
      if(g.relativeMetric>out.maxRelativeMetric){out.maxRelativeMetric=g.relativeMetric;out.worstMetric=short;}
      if(g.curvature!==null&&g.curvature>out.maxCurvature){out.maxCurvature=g.curvature;out.worstCurvature=short;}
      if(g.curvature===null)out.nonimmersedSamples++;
      // Quarter representatives suffice for an informative top list; the
      // complete full-circle sample still enters all summary maxima.
      if(j<=angularCount/4){insertTop(out.topMetric,short,"relativeMetric");if(g.curvature!==null)insertTop(out.topCurvature,short,"curvature");}
      out.minImmersion=Math.min(out.minImmersion,g.immersion);
      out.minHeight=Math.min(out.minHeight,g.height);out.maxHeight=Math.max(out.maxHeight,g.height);
      out.maxSquaredRadius=Math.max(out.maxSquaredRadius,g.squaredRadius);
      if(g.inwardSupport!==undefined)out.minInwardSupport=Math.min(out.minInwardSupport,g.inwardSupport);
      for(let k=0;k<3;k++)out.maxAbsCoordinate[k]=Math.max(out.maxAbsCoordinate[k],Math.abs(v.X[k]));
      row.maxMetric=Math.max(row.maxMetric,g.relativeMetric);
      row.maxCurvature=Math.max(row.maxCurvature,g.curvature||0);
      row.minImmersion=Math.min(row.minImmersion,g.immersion);row.maxSquaredRadius=Math.max(row.maxSquaredRadius,g.squaredRadius);
      row.minZ=Math.min(row.minZ,g.height);row.maxZ=Math.max(row.maxZ,g.height);
    }
    out.radialSummary.push(row);
  }
  const cut=geometry.slice(b.end,z).point(0);
  out.cut={s:b.end,true_state_center_height:cut.Z,X:cut.X,Xs:cut.Xs,Xss:cut.Xss,metric:cut.geometry.relativeMetric,curvature:cut.geometry.curvature};
  out.central={A:provider.definition.centralA,B:provider.definition.centralB,gap:provider.definition.centralGap};
  return out;
}
if(require.main===module){
  const [stateFile,outputFile]=process.argv.slice(2);
  if(!stateFile||!outputFile)throw Error("Usage: node this.cjs actual-state.json new-report.json");
  if(fs.existsSync(outputFile))throw Error("Output already exists");
  const topic=path.resolve(__dirname,".."),candidateFile=path.join(topic,"notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json");
  const input=JSON.parse(fs.readFileSync(stateFile,"utf8")),bundle=JSON.parse(fs.readFileSync(candidateFile,"utf8"));
  const providerPath=path.join(__dirname,"fd2d-direct-position-metric-provider-R187.cjs"),enginePath=path.join(__dirname,"fd2d-direct-position-tangent-lift-baseline-R187.cjs");
  const expectedProvider=input.providerSHA256||input.identity?.provider;
  const expectedEngine=input.engineSHA256||input.identity?.engine;
  const expectedCandidate=input.physicalCandidateSHA256||input.identity?.bundle;
  if(expectedProvider!==identity(providerPath).sha256||expectedEngine!==identity(enginePath).sha256||expectedCandidate!==identity(candidateFile).sha256)
    throw Error("Immutable state mathematical source binding differs");
  const engine=createR187(),provider=createR187Provider(engine,bundle,input.options),geometry=createR187Geometry(engine,provider);
  if(input.z.length!==provider.dimension)throw Error("This entry consumes the exact 181-layout state");
  const started=process.hrtime.bigint(),summary=diagnostic(engine,provider,geometry,Float64Array.from(input.z));
  const report={schema:"fd2d-R187-immutable-actual-state-two-jet-finite-geometry-v1",input:identity(stateFile),stateIteration:input.iteration,options:input.options,
    source:identity(__filename),engine:identity(enginePath),provider:identity(providerPath),
    geometry:identity(path.join(__dirname,"fd2d-direct-position-two-jet-geometry-R187.cjs")),candidate:identity(candidateFile),
    provider_definition:provider.definition,geometry_definition:geometry.definition(),
    seconds:Number(process.hrtime.bigint()-started)/1e9,summary,
    sampling:"All original profile and B3 knots, each interval midpoint and G2 nodes; 128 complete angular points, full primitive, no DFT",
    no_BVP_Jacobian_or_normal_computed:true,continuousCertificate:false,strongTargetComplete:false};
  fs.mkdirSync(path.dirname(outputFile),{recursive:true});
  const tmp=outputFile+".tmp";fs.writeFileSync(tmp,JSON.stringify(report,null,2)+"\n");fs.renameSync(tmp,outputFile);
  console.log(JSON.stringify({outputFile,seconds:report.seconds,iteration:input.iteration,maxRelativeMetric:summary.maxRelativeMetric,
    minImmersion:summary.minImmersion,maxCurvature:summary.maxCurvature,maxSquaredRadius:summary.maxSquaredRadius,
    minZ:summary.minHeight,maxZ:summary.maxHeight,cutZ:summary.cut.true_state_center_height,
    worstMetric:summary.worstMetric,worstCurvature:summary.worstCurvature}));
}
module.exports={diagnostic,selectedNodes};
