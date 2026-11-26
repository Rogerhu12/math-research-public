"use strict";
/* Sample the complete actual R219 position field after an explicit A/Z change.
 * This is source data for a NEW C2 transplant, not a same-metric solve.
 * Binary arrays and execution reports belong in scratch, never in git.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const JETS=["X","Xs","Xss","Xu","Xsu","Xuu"];
function createSource(candidate,input,options={}) {
  const q=require("./6a65-geometry-gap-length-value.cjs").createGapLengthState(candidate,input);
  const A=options.amplitude??.8746432018013935,Z=options.Z??.51;
  const amplitudeIndex=q.position.definition.amplitudeIndex,cutHeightIndex=q.cutHeightIndex;
  const oldA=q.z[amplitudeIndex],oldZ=q.base.height+q.z[cutHeightIndex];
  q.z[amplitudeIndex]=A;q.z[cutHeightIndex]=Z-q.base.height;
  return {...q,sourceChange:{oldA,oldZ,A,Z,amplitudeIndex,cutHeightIndex,
    completeBoundaryLiftingReevaluated:true,sameSolvedField:false}};
}
function mesh(cuts,lo,hi,maxStep) {
  const xs=[lo,...cuts.filter(x=>x>lo&&x<hi),hi].sort((a,b)=>a-b),out=[lo];
  for(let j=1;j<xs.length;j++) {
    const n=Math.ceil((xs[j]-xs[j-1])/maxStep);
    for(let k=1;k<=n;k++)out.push(xs[j-1]+(xs[j]-xs[j-1])*k/n);
  }
  return out;
}
module.exports={createSource,JETS,mesh};
if(require.main===module) {
  const [candidateFile,inputFile,prefix,mode="probe",angleText="256"]=process.argv.slice(2);
  if(!prefix||!["probe","archive"].includes(mode))throw Error("candidate input fresh-prefix [probe|archive] [angles] required");
  const count=Number(angleText);if(!Number.isInteger(count)||count<64)throw Error("angles >=64 required");
  const reportFile=prefix+"-report.json",dataFile=prefix+"-data.f64";
  if(fs.existsSync(reportFile)||fs.existsSync(dataFile))throw Error("Fresh output required");
  fs.mkdirSync(path.dirname(prefix),{recursive:true});
  const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
  const q=createSource(JSON.parse(fs.readFileSync(candidateFile)),JSON.parse(fs.readFileSync(inputFile)));
  const start=Date.now(),support=q.metric.definition.centralA;
  const nodes=mode==="probe"?[.18,.22,.25,.28,.30,.32,.34,.37,.4,q.base.end]:mesh(q.position.radialCuts,.18,q.base.end,.01);
  const rows=[],fd=fs.openSync(dataFile,"wx");
  const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),norm=x=>Math.hypot(...x);
  let written=0;
  try {
    for(let i=0;i<nodes.length;i++) {
      const s=nodes[i],sl=q.position.slice(s,q.z,false),data=new Float64Array(count*18),mean=[0,0,0];
      let maxMetric=0,maxCurvature=0,minArea=Infinity,minHeld=Infinity,maxRadius=0,maxY=0,maxZ=-Infinity,a;
      for(let j=0;j<count;j++) {
        // Exact native nodes avoid the inherited floating modulo boundary bug.
        // The second half is the provider's declared proper half-turn symmetry.
        const jj=j<count/2?j:j-count/2,ratio=jj*q.position.definition.fullEquivalentAngles/count;
        const packet=Math.abs(ratio-Math.round(ratio))<1e-12?sl.node(Math.round(ratio)):sl.point(2*Math.PI*jj/count);
        const p=j<count/2?packet.jets:Object.fromEntries(JETS.map(k=>[k,packet.jets[k].map((x,l)=>l<2?-x:x)]));a=packet.a;
        for(let k=0;k<JETS.length;k++)data.set(p[JETS[k]],j*18+k*3);
        for(let k=0;k<3;k++)mean[k]+=p.X[k]/count;
        const E=dot(p.Xs,p.Xs),F=dot(p.Xs,p.Xu),G=dot(p.Xu,p.Xu);
        minArea=Math.min(minArea,Math.sqrt(Math.max(0,E*G-F*F))/a);
        maxMetric=Math.max(maxMetric,packet.relativeMetric);maxCurvature=Math.max(maxCurvature,packet.curvature);
        minHeld=Math.min(minHeld,norm([p.X[0],p.X[1]-support,p.X[2]]),norm([p.X[0],p.X[1]+support,p.X[2]]));
        maxRadius=Math.max(maxRadius,norm(p.X));maxY=Math.max(maxY,Math.abs(p.X[1]));maxZ=Math.max(maxZ,p.X[2]);
      }
      fs.writeSync(fd,Buffer.from(data.buffer));written+=data.length;
      rows.push({s,a,mean,maxMetric,maxCurvature,minArea,minHeld,maxRadius,maxY,maxZ});
      q.position.clearSliceReuse?.();if(typeof global.gc==="function"&&i%16===0)global.gc();
      if(i%20===0||i===nodes.length-1)console.log(JSON.stringify({row:i,total:nodes.length,...rows.at(-1)}));
    }
  } finally {fs.closeSync(fd);}
  const report={schema:"6a65-actual-retargeted-R219-transplant-source-v1",mode,count,nodes,rows,
    dtype:"little-endian Float64",shape:[nodes.length,count,JETS.length,3],jetOrder:JETS,writtenScalars:written,
    sourceChange:q.sourceChange,actualCentralSupport:support,baseEnd:q.base.end,baseHeight:q.base.height,
    completeParameterDimension:q.z.length,sourceStateSHA256:hash(inputFile),candidateSHA256:hash(candidateFile),
    entrySHA256:hash(__filename),dataSHA256:hash(dataFile),dataFile,
    observedSourceMetricMaximum:Math.max(...rows.map(x=>x.maxMetric)),observedSourceCurvatureMaximum:Math.max(...rows.map(x=>x.maxCurvature)),
    observedSourceMinimumArea:Math.min(...rows.map(x=>x.minArea)),
    actualNewValueGeometry:true,oldStateUnmodified:true,continuousCertificate:false,seconds:(Date.now()-start)/1000};
  fs.writeFileSync(reportFile,JSON.stringify(report,null,2)+"\n");
  console.log(JSON.stringify({rows:nodes.length,angles:count,seconds:report.seconds,dataSHA256:report.dataSHA256,
    maximumMetric:report.observedSourceMetricMaximum,maximumCurvature:report.observedSourceCurvatureMaximum,minimumArea:report.observedSourceMinimumArea}));
}
