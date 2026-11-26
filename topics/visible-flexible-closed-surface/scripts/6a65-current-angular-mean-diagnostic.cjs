"use strict";
/* Consume the existing R207 decomposition on a newly accepted full field.
 * This evaluates a possible new target without changing any state coefficient.
 * It is not a solver, an accepted step, or fixed-g refinement. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const [candidateFile,inputFile,outputFile]=process.argv.slice(2);
if(!candidateFile||!inputFile||!outputFile||fs.existsSync(outputFile))throw Error("candidate input fresh-output required");
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile));
let q;
if(input.gapLengthDesign)q=require("./6a65-geometry-gap-length-value.cjs").createGapLengthState(candidate,input);
else if(input.outerLengthDesign)throw Error("Standalone outer-length states need their explicit physical factory");
else q=require("./6a65-low-memory-r211-provider-recovered-20261126.cjs").createMemoryBoundR211RunProvider(candidate,input);
const started=Date.now();
const report=require("./fd2d-angular-mean-metric-decomposition-R207.cjs")
  .decomposeR207AngularMeans(q.position,q.engine,q.z??input.z);
report.execution={startedUTC:new Date(started).toISOString(),seconds:(Date.now()-started)/1000,node:process.version};
report.source={inputSHA256:hash(inputFile),candidateSHA256:hash(candidateFile),entrySHA256:hash(__filename),
  decompositionSHA256:hash(path.join(__dirname,"fd2d-angular-mean-metric-decomposition-R207.cjs"))};
fs.mkdirSync(path.dirname(outputFile),{recursive:true});fs.writeFileSync(outputFile,JSON.stringify(report,null,2)+"\n");
const summary={...report};delete summary.rows;
summary.outputSHA256=hash(outputFile);process.stdout.write(JSON.stringify(summary)+"\n");
