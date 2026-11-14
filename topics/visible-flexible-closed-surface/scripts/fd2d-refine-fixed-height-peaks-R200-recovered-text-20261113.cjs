"use strict";
/* Thin R200 constraint rebinding after the unchanged R196 frozen-peak refiner.
 * It never changes the copied cut coefficient and performs no new solve.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto"),cp=require("node:child_process");
const sha=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
function bits(x){const b=Buffer.alloc(8);b.writeDoubleBE(x);return b.toString("hex");}
function need(c,m){if(!c)throw Error(m);}
const [shared,input,rawOutput,output,countText="2"]=process.argv.slice(2),count=Number(countText);
need(shared&&input&&rawOutput&&output&&Number.isInteger(count)&&count>0,"shared-scripts parent raw-injection-output fixed-output count");
need(!fs.existsSync(rawOutput)&&!fs.existsSync(output),"Fresh raw and fixed output files required");
const parent=JSON.parse(fs.readFileSync(input,"utf8")),c=parent.fixedHeightConstraint;
need(c&&c.schema==="R200-fixed-finite-cut-height-coordinate-v1","Explicit R200 parent required");
need(bits(parent.z[c.index])===c.coefficientBinary64,"Parent fixed coordinate does not match saved bits");
const refiner=path.join(path.resolve(shared),"fd2d-refine-frozen-metric-peaks-R196.cjs"),t=process.hrtime.bigint();
const child=cp.spawnSync(process.execPath,[refiner,path.resolve(input),path.resolve(rawOutput),String(count)],{stdio:"inherit"});
if(child.error)throw child.error;
need(child.status===0&&child.signal===null,"Frozen R196 refiner did not naturally exit zero");
const refined=JSON.parse(fs.readFileSync(rawOutput,"utf8")),J=refined.options.radialBasisCount,K=refined.options.modes,newIndex=2*J*K+J;
need(refined.z.length===2*J*K+2*J+1,"Refined full layout mismatch");
need(K===parent.options.modes&&refined.options.angles===parent.options.angles,"This wrapper only rebinds radial refinement");
need(bits(refined.z[newIndex])===c.coefficientBinary64,"Boehm injection did not preserve the fixed cut coefficient");
need(refined.guide===undefined||JSON.stringify(refined.guide)===JSON.stringify(parent.guide||parent.curvatureOptions),"Changed objective guide");
refined.schema="R200-fixed-height-after-R196-radial-injection-v1";
refined.fixedHeightConstraint={...c,index:newIndex};
refined.iteration=parent.iteration;
refined.guide=parent.guide||parent.curvatureOptions;
refined.parentInitialIteration=parent.iteration;
refined.constraintRebinding={parentIndex:c.index,newIndex,coefficientBinary64:c.coefficientBinary64,coefficientWasCopiedWithoutArithmetic:true,finiteHeightUnchanged:c.targetFiniteHeight,acceptedStep:false,rawInjectionSHA256:sha(rawOutput),parentSHA256:sha(input),rootRefinerSHA256:sha(refiner),adapterSHA256:sha(__filename),rawRefinerChildExitCode:child.status,elapsedSeconds:Number(process.hrtime.bigint()-t)/1e9};
refined.actualFiniteCutHeight=c.targetFiniteHeight;
refined.continuousCertificate=false;refined.strongTargetComplete=false;
const temp=output+".tmp";fs.writeFileSync(temp,JSON.stringify(refined,null,2)+"\n");fs.renameSync(temp,output);
console.log(JSON.stringify({output,dimension:refined.z.length,J,K,iteration:refined.iteration,newKnots:refined.selection.insertedKnots,oldIndex:c.index,newIndex,fixedBits:c.coefficientBinary64,cut:c.targetFiniteHeight,newQuadratureBaseline:refined.newQuadratureBaseline,rawRefinerExit:child.status}));
