"use strict";
/* Extract one actual current Cartesian cross-section and its two-jets.
 * The later Fourier curve/arc normalization is an explicit new inlet.
 * This sampler does not claim the old approximate surface is an exact port. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const [candidateFile,inputFile,outputFile,oldEntryText=".3735625",countText="512"]=process.argv.slice(2);
if(!candidateFile||!inputFile||!outputFile||fs.existsSync(outputFile))throw Error("candidate input fresh-output [old-coordinate entry] [count] required");
const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile));
const q=require("./6a65-geometry-gap-length-value.cjs").createGapLengthState(candidate,input);
const oldEntry=Number(oldEntryText),count=Number(countText);
if(!Number.isFinite(oldEntry)||oldEntry<=q.oldBase.centralLength||oldEntry>=q.oldBase.end||!Number.isInteger(count)||count<64)
  throw Error("Interior old-coordinate entry and count>=64 required");
const s=q.base.oldToNew(oldEntry),sl=q.position.slice(s,q.z,false),points=[];
const norm=x=>Math.hypot(...x),dot=(a,b)=>a.reduce((v,x,i)=>v+x*b[i],0);
let minSpeed=Infinity,maxSpeed=0,minTu=Infinity,maxTu=0,maxMetric=0,maxCurvature=0,maxRadius=0,minHeld=Infinity;
const support=q.metric.definition.centralA;
for(let j=0;j<count;j++){
  const u=2*Math.PI*j/count,p=sl.point(u),jets=p.jets,T=jets.Xu.map(v=>v/p.a),Tu=jets.Xuu.map(v=>v/p.a);
  const speed=norm(jets.Xu),tu=norm(Tu);
  minSpeed=Math.min(minSpeed,speed);maxSpeed=Math.max(maxSpeed,speed);minTu=Math.min(minTu,tu);maxTu=Math.max(maxTu,tu);
  maxMetric=Math.max(maxMetric,p.relativeMetric);maxCurvature=Math.max(maxCurvature,p.curvature);maxRadius=Math.max(maxRadius,norm(jets.X));
  minHeld=Math.min(minHeld,norm([jets.X[0],jets.X[1]-support,jets.X[2]]),norm([jets.X[0],jets.X[1]+support,jets.X[2]]));
  points.push({u,a:p.a,...jets,metric:p.relativeMetric,curvature:p.curvature,TdotTu:dot(T,Tu)});
}
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const report={schema:"6a65-current-strong-field-inlet-cartesian-samples-v1",
  source:{candidateFile,candidateSHA256:hash(candidateFile),inputFile,inputSHA256:hash(inputFile),entrySHA256:hash(__filename)},
  oldEntry,s,count,oldBaseJet:q.oldBase.at(oldEntry),actualCentralSupport:support,
  actualCuffHeight:q.design.trueCuffHeight,tailAmplitude:q.design.amplitude,
  inheritedGapLengthDesign:q.design,summary:{minSpeed,maxSpeed,minTu,maxTu,maxMetric,maxCurvature,maxRadius,minHeld},
  points,oldApproximateInletNotDeclaredExact:true,continuousCertificate:false};
fs.mkdirSync(path.dirname(outputFile),{recursive:true});fs.writeFileSync(outputFile,JSON.stringify(report)+"\n");
process.stdout.write(JSON.stringify({oldEntry,s,count,summary:report.summary,outputSHA256:hash(outputFile)})+"\n");
