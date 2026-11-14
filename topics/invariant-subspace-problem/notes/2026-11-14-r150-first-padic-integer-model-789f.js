#!/usr/bin/env node
// Exact original integer 17-equation model, reduced mod 31^2 for one lift digit.
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {parameterSystem}=require("./2026-11-14-rank-one-parameter-ideal-runner-789f.js");
const hash=x=>crypto.createHash("sha256").update(x).digest("hex");
const mul=(a,b)=>{const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c;};
const norm=x=>Number((x%961n+961n)%961n);
function main(){
 const args=process.argv.slice(2);if(args.length!==2)throw Error("usage: GENERATOR ORIGINAL_NF_INPUT OUTPUT_DIRECTORY");
 const [inputFile,out]=args;fs.mkdirSync(out,{recursive:true});
 const z=parameterSystem("original",event=>process.stdout.write(JSON.stringify(event)+"\n"));
 const input=fs.readFileSync(inputFile),tokens=input.toString().trim().split(/\s+/);let pos=0;
 if(hash(input)!=="291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"||tokens[pos++]!=="R150_NATIVE_NF_V1")throw Error("original model hash");
 const lines=["R150_ORIGINAL_MOD961_V1",[norm(BigInt(z.denominator)),...z.contents.map(norm)].join(" ")];
 let checks=0;
 function get(row,term,d){return row[term][d]||0n;}
 for(let e=0;e<11;e++){
  const row=z.equations[e],co=[];
  for(let k=0;k<66;k++){
   if(row[k+11].slice(1).some(x=>x!==0n))throw Error("N quadratic acquired parameter dependence");
   const a=norm(get(row,k+11,0));if(a%31!==Number(tokens[pos++]))throw Error("N quadratic mod31 mismatch");co.push(a);checks++;
  }
  for(let v=0;v<11;v++)for(let d=0;d<=10;d++){const a=norm(get(row,v,d));if(a%31!==Number(tokens[pos++]))throw Error("N linear mod31 mismatch");co.push(a);checks++;}
  lines.push(co.join(" "));
 }
 const pre=Number(tokens[pos++]);if(pre!==3333)throw Error("prebasis count");pos+=4*pre;
 for(let e=11;e<17;e++){
  const row=z.equations[e];if(row.slice(0,11).some(p=>p.some(x=>x!==0n)))throw Error("Gamma is not quadratic");
  const co=[];for(let k=0;k<66;k++)for(let d=0;d<=5;d++){const a=norm(get(row,k+11,d));if(a%31!==Number(tokens[pos++]))throw Error("Gamma mod31 mismatch");co.push(a);checks++;}lines.push(co.join(" "));
 }
 const fp=[-8n,32n,-25n,5n],fm=[864n,864n,135n,5n],e8=[9600n,-25472n,-3392n,15936n,-2888n,-936n,153n,50n,5n];
 const h0=mul(mul(mul(mul([0n,0n,0n,1n],[-2n,1n]),mul(fp,fp)),mul(fm,fm)),e8);
 if(h0.length!==25||h0[24]!==3125n)throw Error("original integer h0");
 const ann=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-14-r150-target-minimum-annihilators-receipt-789f.json"),"utf8"));
 if(h0.some((c,i)=>Number((c%31n+31n)%31n)!==25*ann.commonMinimum.coefficientsAscending[i]%31))throw Error("h0 is not 25*h31 mod31");
 lines.push(h0.map(norm).join(" "));
 const payload=lines.join("\n")+"\n",modelFile=path.join(out,"original-integer-mod961.txt");fs.writeFileSync(modelFile,payload);
 const exact=JSON.stringify({format:"r150-original-primitive-integer-equations-v1",denominator:z.denominator,contents:z.contents.map(String),equations:z.equations.map(row=>row.map(p=>p.map(String))),h0:h0.map(String)})+"\n";
 const exactFile=path.join(out,"original-primitive-integer-equations.json");fs.writeFileSync(exactFile,exact);
 const receipt={format:"r150-first-lift-integer-model-v1",status:"exact-integer-model-generated",modulus:961,field:31,originalInputSHA256:hash(input),sourceDataSHA256:z.sourceDataSHA256,originalFixedDChecks:z.checks,coefficientResidueChecks:checks,originalCommonDenominator:z.denominator,constantRowContents:z.contents.map(String),h0CoefficientsAscending:h0.map(String),h0Mod31Scale:25,model:{file:modelFile,bytes:Buffer.byteLength(payload),sha256:hash(payload)},exactIntegerEquations:{file:exactFile,bytes:Buffer.byteLength(exact),sha256:hash(exact)},generatorSHA256:hash(fs.readFileSync(__filename))};
 fs.writeFileSync(path.join(out,"integer-model-receipt.json"),JSON.stringify(receipt,null,2)+"\n");process.stdout.write(JSON.stringify(receipt)+"\n");
}
main();
