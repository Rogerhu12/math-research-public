"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {buildRankOneCenteredIntegerSystem}=require("./2026-11-14-rank-one-centered-integer-system-generator.js");
const {translateRankOneCenteredSystem}=require("./2026-11-14-rank-one-centered-translation.js");
const {rankOneNormalLinearProjection,checkRankOneProjectionKernel}=require("./2026-11-14-rank-one-exceptional-mean-normal-projection.js");
const {rankOneMacaulayF11}=require("./2026-11-14-rank-one-exceptional-mean-macaulay-f11.js");
const files={"2":"2026-11-14-rank-one-physical-mean-two-rank-certificate-receipt.json","-6":"2026-11-14-rank-one-physical-mean-minus-six-rank-certificate-receipt.json"};
const hash=x=>crypto.createHash("sha256").update(JSON.stringify(x)).digest("hex");
async function verifyRankOneFixedContactMean(s=2,report){
 if(!files[String(s)])throw new Error("No completed fixed-mean certificate registered for "+s);
 const receipt=JSON.parse(fs.readFileSync(path.join(__dirname,files[String(s)]),"utf8"));
 const data=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json"),"utf8"));
 const mean=Array.from({length:6},(_,i)=>String(BigInt(s)**BigInt(i)));
 const z=translateRankOneCenteredSystem(buildRankOneCenteredIntegerSystem(data,mean),s);
 if(hash(z)!==receipt.coordinateSystemSHA256)throw new Error("Original transformed equations checksum mismatch");
 for(const e of z.equations){if(e.linear.slice(0,2).some(x=>BigInt(x)))throw new Error("Pure tangent linear term");z.quadraticMonomials.forEach(([i,j],k)=>{if(i<2&&j<2&&BigInt(e.quadratic[k]))throw new Error("Pure tangent quadratic term");});}
 const P=rankOneNormalLinearProjection(z,[0,1]),cert=receipt.projectionKernel;
 if(hash(cert)!==receipt.kernelSHA256)throw new Error("Stored exact kernel checksum mismatch");
 const upper=checkRankOneProjectionKernel(P,cert);
 if(upper.independentRationalKernelVectors!==2||upper.projectionRankUpperBound!==133)throw new Error("Wrong characteristic-zero upper bound");
 const lower=await rankOneMacaulayF11(z,5,report);
 if(lower.rows!==6188||lower.columns!==4367||lower.rank!==4345)throw new Error("Macaulay lower bound mismatch");
 if(4212+upper.projectionRankUpperBound!==lower.rank)throw new Error("Rank bounds do not meet");
 return {s,characteristicZeroRank:4345,projection:upper,kernelSHA256:receipt.kernelSHA256,finiteFieldLowerBound:lower,conclusion:"All nine normal-coordinate squares belong to the degree-five span of the original seventeen equations; every complex critical point lies in the physical tangent plane and has T3=0."};
}
module.exports={verifyRankOneFixedContactMean};
if(require.main===module)verifyRankOneFixedContactMean(Number(process.argv[2]||2),x=>process.stderr.write(JSON.stringify(x)+"\n")).then(x=>process.stdout.write(JSON.stringify(x,null,2)+"\n")).catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
