#!/usr/bin/env node
"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {createR187}=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs");
const {createR187Provider}=require("./fd2d-direct-position-metric-provider-R187.cjs");
const {createR190Provider}=require("./fd2d-direct-position-designed-metric-provider-R190.cjs");
const {createR187Geometry}=require("./fd2d-direct-position-two-jet-geometry-R187.cjs");
const {createR190GeometryView}=require("./fd2d-direct-position-two-jet-geometry-R190.cjs");
const {diagnostic}=require("./fd2d-diagnose-direct-position-state-R187.cjs");
const identity=file=>{const b=fs.readFileSync(file);return {path:file,bytes:b.length,sha256:crypto.createHash("sha256").update(b).digest("hex")};};
const [stateFile,outputFile]=process.argv.slice(2);
if(!stateFile||!outputFile)throw Error("Usage: node this.cjs actual-193-state.json new-report.json");
if(fs.existsSync(outputFile))throw Error("Output already exists");
const topic=path.resolve(__dirname,".."),candidate=path.join(topic,"notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json");
const input=JSON.parse(fs.readFileSync(stateFile,"utf8")),bundle=JSON.parse(fs.readFileSync(candidate,"utf8"));
const ep=path.join(__dirname,"fd2d-direct-position-tangent-lift-baseline-R187.cjs"),pp=path.join(__dirname,"fd2d-direct-position-designed-metric-provider-R190.cjs");
if(input.identity.engine!==identity(ep).sha256||input.identity.provider!==identity(pp).sha256||input.identity.bundle!==identity(candidate).sha256)
  throw Error("Exact saved R190 source identity differs");
const engine=createR187(),old=createR187Provider(engine,bundle,input.options),designed=createR190Provider(engine,bundle,input.options);
const view=createR190GeometryView(engine,old,designed,input.z,createR187Geometry);
const start=process.hrtime.bigint(),summary=diagnostic(engine,view.providerView,view.geometry,view.oldParameters);
const previous=input.history.at(-1).evaluation.worst;
const at=view.geometry.point(previous.s,previous.u,view.oldParameters).geometry;
const report={schema:"fd2d-R190-immutable-actual-state-two-jet-finite-geometry-v1",input:identity(stateFile),stateIteration:input.iteration,
  source:identity(__filename),engine:identity(ep),provider:identity(pp),candidate:identity(candidate),
  geometrySource:identity(path.join(__dirname,"fd2d-direct-position-two-jet-geometry-R187.cjs")),
  adapterSource:identity(path.join(__dirname,"fd2d-direct-position-two-jet-geometry-R190.cjs")),
  definition:view.definition,seconds:Number(process.hrtime.bigint()-start)/1e9,summary,
  overlap_at_saved_actual_worst:{saved:previous,actual_rE:at.rE,actual_rF:at.rF,maximum_difference:Math.max(Math.abs(at.rE-previous.rE),Math.abs(at.rF-previous.rF))},
  no_BVP_Jacobian_or_normal_computed:true,continuousCertificate:false,strongTargetComplete:false};
fs.mkdirSync(path.dirname(outputFile),{recursive:true});fs.writeFileSync(outputFile+".tmp",JSON.stringify(report,null,2)+"\n");fs.renameSync(outputFile+".tmp",outputFile);
console.log(JSON.stringify({outputFile,seconds:report.seconds,iteration:input.iteration,maxRelativeMetric:summary.maxRelativeMetric,minImmersion:summary.minImmersion,
  maxCurvature:summary.maxCurvature,maxSquaredRadius:summary.maxSquaredRadius,minZ:summary.minHeight,maxZ:summary.maxHeight,cutZ:summary.cut.true_state_center_height,
  overlap:report.overlap_at_saved_actual_worst,worstCurvature:summary.worstCurvature}));
