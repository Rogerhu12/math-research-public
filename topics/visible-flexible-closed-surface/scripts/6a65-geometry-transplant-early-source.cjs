"use strict";
/* Extend the actual archived R219 field to an explicitly earlier physical
 * inlet. Existing complete source arrays are preserved after SHA verification.
 * Only the newly required prefix slices are recomputed. Scratch outputs only. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {createSource,JETS,mesh}=require("./6a65-geometry-strong-transplant-source.cjs");
const [candidateFile,inputFile,oldReportFile,prefix,loText=".14"]=process.argv.slice(2),lo=Number(loText);
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
if(!prefix)throw Error("candidate input old-report fresh-prefix [new lower s] required");
const old=JSON.parse(fs.readFileSync(oldReportFile)),count=old.count;
if(hash(old.dataFile)!==old.dataSHA256||hash(inputFile)!==old.sourceStateSHA256)throw Error("Original source identity mismatch");
if(!(lo>=13/128&&lo<old.nodes[0]))throw Error("Strict earlier physical inlet required");
const q=createSource(JSON.parse(fs.readFileSync(candidateFile)),JSON.parse(fs.readFileSync(inputFile)),
  {amplitude:old.sourceChange.A,Z:old.sourceChange.Z});
const nodes=mesh(q.position.radialCuts,lo,old.nodes[0],.005).slice(0,-1),rows=[],dataFile=prefix+"-data.f64",reportFile=prefix+"-report.json";
if(fs.existsSync(dataFile)||fs.existsSync(reportFile))throw Error("Fresh outputs required");
fs.mkdirSync(path.dirname(prefix),{recursive:true});const fd=fs.openSync(dataFile,"wx"),start=Date.now();
try {
  for(const s of nodes){
    const sl=q.position.slice(s,q.z,false),data=new Float64Array(count*18),mean=[0,0,0];
    let a,maxMetric=0,maxCurvature=0,minArea=Infinity;
    for(let j=0;j<count;j++) {
      const jj=j<count/2?j:j-count/2,r=jj*q.position.definition.fullEquivalentAngles/count;
      const packet=Math.abs(r-Math.round(r))<1e-12?sl.node(Math.round(r)):sl.point(2*Math.PI*jj/count);
      const p=j<count/2?packet.jets:Object.fromEntries(JETS.map(k=>[k,packet.jets[k].map((x,l)=>l<2?-x:x)]));a=packet.a;
      for(let k=0;k<JETS.length;k++)data.set(p[JETS[k]],j*18+k*3);
      for(let k=0;k<3;k++)mean[k]+=p.X[k]/count;
      maxMetric=Math.max(maxMetric,packet.relativeMetric);maxCurvature=Math.max(maxCurvature,packet.curvature);minArea=Math.min(minArea,Math.sqrt(packet.immersion));
    }
    fs.writeSync(fd,Buffer.from(data.buffer));rows.push({s,a,mean,maxMetric,maxCurvature,minArea});q.position.clearSliceReuse?.();
  }
  fs.writeSync(fd,fs.readFileSync(old.dataFile));
} finally {fs.closeSync(fd);}
const report={...old,nodes:[...nodes,...old.nodes],rows:[...rows,...old.rows],shape:[nodes.length+old.nodes.length,count,6,3],
  writtenScalars:(nodes.length+old.nodes.length)*count*18,dataFile,dataSHA256:hash(dataFile),entrySHA256:hash(__filename),
  extension:{newLower:lo,oldLower:old.nodes[0],newSlices:nodes.length,oldReportSHA256:hash(oldReportFile),oldDataSHA256:old.dataSHA256},
  observedSourceMetricMaximum:Math.max(old.observedSourceMetricMaximum,...rows.map(x=>x.maxMetric)),
  observedSourceCurvatureMaximum:Math.max(old.observedSourceCurvatureMaximum,...rows.map(x=>x.maxCurvature)),
  observedSourceMinimumArea:Math.min(old.observedSourceMinimumArea,...rows.map(x=>x.minArea)),seconds:(Date.now()-start)/1000};
fs.writeFileSync(reportFile,JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify({newSlices:nodes.length,allSlices:report.nodes.length,seconds:report.seconds,dataSHA256:report.dataSHA256,
  metric:report.observedSourceMetricMaximum,curvature:report.observedSourceCurvatureMaximum,minRelativeArea:report.observedSourceMinimumArea}));
