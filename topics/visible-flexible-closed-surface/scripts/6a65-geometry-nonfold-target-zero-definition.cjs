"use strict";
/* Reconstruct only the declared zero-parameter target metric definition.
 * No old baseline, raw cache, CI checkpoint or optimization is reconstructed. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const [scriptsDirectory,candidateFile,recipeFile,outputFile]=process.argv.slice(2);
if(!outputFile||fs.existsSync(outputFile))throw Error("scripts candidate recipe fresh-output required");
const sha=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const scripts=path.resolve(scriptsDirectory),branch=require(path.join(scripts,"6a65-cauchy-global-position.cjs"));
const candidate=JSON.parse(fs.readFileSync(candidateFile)),recipe=JSON.parse(fs.readFileSync(recipeFile));
const input=JSON.parse(JSON.stringify(recipe.config)),q=branch.build(candidate,input);
if(!q.z.every((x,j)=>j===q.amplitudeIndex||j===q.cutHeightIndex||x===0))
  throw Error("The target definition requires zero theta/phi/height/rho coefficients");
const output={...input,schema:branch.INITIAL,z:Array.from(q.z),cauchyAcceptedSteps:0,
  accepted:false,interfaceProbeOnly:true,actualValueBaseline:false,actualAcceptedSteps:0,
  targetMetricDefinitionOnly:true,notCICheckpoint:true,noCIValueOrCurvatureInherited:true,
  purpose:"Independent frozen target g definition for a NEW polar position field; old field value/cache not recomputed.",
  source:{candidateSHA256:sha(candidateFile),recipeSHA256:sha(recipeFile),entrySHA256:sha(__filename),
    factorySHA256:sha(path.join(scripts,"6a65-cauchy-global-position.cjs"))}};
fs.mkdirSync(path.dirname(outputFile),{recursive:true});fs.writeFileSync(outputFile,JSON.stringify(output)+"\n");
process.stdout.write(JSON.stringify({outputFile,outputSHA256:sha(outputFile),
  parameterVectorSHA256:crypto.createHash("sha256").update(JSON.stringify(q.z)).digest("hex"),
  dimension:q.z.length,actualOldValueBaselinesComputed:0,actualAcceptedSteps:0})+"\n");
