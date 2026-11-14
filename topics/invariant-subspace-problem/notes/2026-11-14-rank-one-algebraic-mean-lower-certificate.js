"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {buildRankOneCenteredIntegerSystem}=require("./2026-11-14-rank-one-centered-integer-system-generator.js");
const {translateRankOneCenteredSystem}=require("./2026-11-14-rank-one-centered-translation.js");
const {rankOneMacaulayF17F19}=require("./2026-11-14-rank-one-macaulay-f17-f19.js");
const {verifyE8Irreducibility}=require("./2026-11-14-rank-one-E8-irreducibility-verify.js");
const files={Pplus:"2026-11-14-rank-one-Pplus-algebraic-lower-bound-receipt.json",Pminus:"2026-11-14-rank-one-Pminus-algebraic-lower-bound-receipt.json",E8:"2026-11-14-rank-one-E8-algebraic-lower-bound-receipt.json"};
const md=(x,p)=>((x%p)+p)%p,peval=(a,x,p)=>a.reduceRight((v,c)=>md(v*x+c,p),0);
async function verifyRankOneAlgebraicMeanLowerBound(family="Pplus",report){
 if(!files[family])throw new Error("No completed algebraic-mean lower certificate registered for "+family);
 const receipt=JSON.parse(fs.readFileSync(path.join(__dirname,files[family]),"utf8")),F=receipt.minimalPolynomialThetaAscending,ell=receipt.irreducibilityPrime;
 if(F.length===4){if(F[3]!==1||Array.from({length:ell},(_,x)=>peval(F,x,ell)).some(x=>x===0))throw new Error("Monic cubic irreducibility certificate failed");}
 else if(family==="E8"&&F.length===9){const e=verifyE8Irreducibility();if(JSON.stringify(e.thetaPolynomial)!==JSON.stringify(F)||e.irreducibilityPrime!==ell)throw new Error("Degree-eight irreducibility certificate mismatch");}
 else throw new Error("Unsupported irreducibility certificate");
 const p=receipt.reductionPrime,s=receipt.sourceResidue,theta=receipt.thetaResidue;
 if(md(5*s,p)!==theta||peval(F,theta,p)!==0)throw new Error("Bad algebraic residue");
 const derivative=F.slice(1).map((a,i)=>(i+1)*a);if(!peval(derivative,theta,p))throw new Error("Residue is not simple");
 const data=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json"),"utf8"));
 const mean=Array.from({length:6},(_,i)=>String(BigInt(s)**BigInt(i)));
 let z=translateRankOneCenteredSystem(buildRankOneCenteredIntegerSystem(data,mean),s);
 z={...z,equations:z.equations.map(e=>({...e,linear:e.linear.map(x=>String(BigInt(x)*BigInt(e.scale))),quadratic:e.quadratic.map(x=>String(BigInt(x)*BigInt(e.scale))),scale:"1"}))};
 if(BigInt(z.denominator)%BigInt(p)===0n)throw new Error("Bad common denominator prime");
 const h=crypto.createHash("sha256").update(JSON.stringify(z)).digest("hex");if(h!==receipt.integerSystemSHA256)throw new Error("Fixed-D original system checksum mismatch");
 const lower=await rankOneMacaulayF17F19(z,5,p,report,4352);
 if(lower.columns!==4367||lower.totalRows!==6188||lower.rankLowerBound!==4352)throw new Error("Insufficient modular rank lower bound");
 return {family,...(F.length===4?{irreducibleCubic:F}:{irreduciblePolynomialTheta:F}),prime:p,sourceResidue:s,thetaResidue:theta,integerSystemSHA256:h,lower,characteristicZeroMacaulayRankLowerBound:4352,interpretation:"A nonzero modular minor cannot vanish in the irreducible number field. Together with the published pointwise projection rank bound 140, all nine normal squares belong to the original degree-five ideal span."};
}
module.exports={verifyRankOneAlgebraicMeanLowerBound};
if(require.main===module)verifyRankOneAlgebraicMeanLowerBound(process.argv[2]||"Pplus",x=>process.stderr.write(JSON.stringify(x)+"\n")).then(x=>process.stdout.write(JSON.stringify(x,null,2)+"\n")).catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
