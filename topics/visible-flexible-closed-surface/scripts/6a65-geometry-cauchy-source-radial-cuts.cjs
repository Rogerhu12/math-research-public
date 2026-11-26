"use strict";
/* Metadata-only adapter: the frozen original source and its q.z are unchanged.
 * No value, derivative, radial metric, or background field is replaced. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const sourceFile=path.join(__dirname,"6a65-geometry-cauchy-tail-source.cjs");
const original=require(sourceFile);
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
function createCauchySource(candidate,input,options={}) {
  const source=original.createCauchySource(candidate,input,options);
  const cuts=Array.from(source.q.position.radialCuts);
  if(!cuts.every(Number.isFinite)||cuts.some((v,i)=>i&&v<=cuts[i-1]))
    throw Error("Original source radial cuts must be finite and strictly ordered");
  source.metadata={...source.metadata,radialCuts:cuts,
    sourceMetadataAdapterSHA256:hash(__filename),
    radialCutsAreOriginalPositionProviderCuts:true,
    completeIntegrationCuts:Array.from(new Set([0,...cuts,source.metadata.S,
      source.metadata.S+(.8-.34),source.metadata.cuff])).sort((a,b)=>a-b),
    trueTailInnerTransition:source.metadata.S+(.8-.34),
    adapterChangesOnlyMetadata:true};
  source.assertUnchanged();
  return source;
}
module.exports={...original,createCauchySource};
if(require.main===module){
  const [mode,scriptsDirectory,candidateFile,inputFile]=process.argv.slice(2);
  if(mode!=="serve"||!inputFile)throw Error("serve scripts-dir candidate actual-checkpoint required");
  const source=createCauchySource(JSON.parse(fs.readFileSync(candidateFile)),JSON.parse(fs.readFileSync(inputFile)),
    {scriptsDirectory,identities:{candidateSHA256:hash(candidateFile),sourceStateSHA256:hash(inputFile)}});
  const lines=require("node:readline").createInterface({input:process.stdin,crlfDelay:Infinity});
  lines.on("line",line=>{
    let request;
    try{
      request=JSON.parse(line);let answer;
      if(request.method==="metadata")answer={metadata:source.metadata};
      else if(request.method==="sample"||request.method===undefined)answer=source.sample(request.s,request.u,!!request.deep);
      else if(request.method==="clear"){source.clear();if(global.gc)global.gc();answer={cleared:true};}
      else throw Error("Unknown source request method");
      process.stdout.write(JSON.stringify({id:request.id??null,ok:true,...answer})+"\n");
    }catch(error){
      process.stdout.write(JSON.stringify({id:request?.id??null,ok:false,error:String(error.stack||error)})+"\n");
    }
  });
}
