"use strict";
// This script reconstructs the complete finite rank certificate from the original
// integer equations. It uses no symbolic algebra package and no floating point
// tolerance. The large rational null vectors are generated, not split for upload.
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {rankOneMacaulayF7}=require("./2026-11-14-rank-one-exceptional-mean-macaulay-f7.js");
const {integerRightKernel}=require("./2026-11-14-rank-one-exceptional-mean-integer-kernel.js");
const {rankOneNormalLinearProjection,checkRankOneProjectionKernel}=require("./2026-11-14-rank-one-exceptional-mean-normal-projection.js");
const expected={"zero":{"branch":"zero","degree":5,"projectionRows":170,"projectionColumns":135,"independentIntegerKernelVectors":7,"identityCount":1190,"projectionRankUpperBound":128,"free":[8,26,130,131,132,133,134],"kernelSHA256":"039af344dfc85b2d77ad597cdf0cdfdac4f387875b7250ce363466f8a1adf5a5","kernelJSONBytes":179138},"infinity":{"branch":"infinity","degree":5,"projectionRows":170,"projectionColumns":135,"independentIntegerKernelVectors":7,"identityCount":1190,"projectionRankUpperBound":128,"free":[8,26,98,125,132,133,134],"kernelSHA256":"a7eacfb2929c88d7b160d71ccf52d6c8a958be6c0a1a0312a82b7f09e8f8334d","kernelJSONBytes":84154}};
async function verifyRankOneExceptionalMean(branch="zero",report){
 if(!expected[branch])throw new Error("No completed certificate registered for "+branch);
 const original=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-14-rank-one-zero-infinity-centered-systems.json"),"utf8"))[branch];
 const tangent=branch==="zero"?[0,1]:[9,10],projection=rankOneNormalLinearProjection(original,tangent);
 // Each original polynomial vanishes on the complete tangent plane.
 for(const e of original.equations){
  for(const i of tangent)if(BigInt(e.linear[i]))throw new Error("Pure tangent linear term");
  original.quadraticMonomials.forEach(([i,j],k)=>{if(tangent.includes(i)&&tangent.includes(j)&&BigInt(e.quadratic[k]))throw new Error("Pure tangent quadratic term");});
 }
 const exact=await integerRightKernel(projection.rows,report);
 const cert={format:"rank-one-exceptional-mean-projection-kernel-v1",branch,degree:5,free:exact.free,kernels:exact.kernels};
 const hash=crypto.createHash("sha256").update(JSON.stringify(cert)).digest("hex");
 const upper=checkRankOneProjectionKernel(projection,cert);
 if(hash!==expected[branch].kernelSHA256)throw new Error("Exact kernel checksum mismatch");
 const lower=await rankOneMacaulayF7(original,5,report);
 if(lower.rows!==6188||lower.columns!==4367||lower.rank!==4340)throw new Error("Macaulay lower-bound certificate mismatch");
 if(4212+upper.projectionRankUpperBound!==lower.rank)throw new Error("Rank bounds do not meet");
 return {branch,originalEquations:17,maxMultiplierDegree:3,maxPolynomialDegree:5,characteristicZeroRank:4340,projection:upper,kernelSHA256:hash,finiteFieldLowerBound:lower,conclusion:"Every polynomial of degree at most 5 containing at least two normal factors lies in the degree-5 span of the original 17 equations. All nine normal squares vanish at every complex solution."};
}
module.exports={verifyRankOneExceptionalMean};
if(require.main===module)verifyRankOneExceptionalMean(process.argv[2]||"zero",x=>{process.stderr.write(JSON.stringify(x)+"\n");}).then(x=>process.stdout.write(JSON.stringify(x,null,2)+"\n")).catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
