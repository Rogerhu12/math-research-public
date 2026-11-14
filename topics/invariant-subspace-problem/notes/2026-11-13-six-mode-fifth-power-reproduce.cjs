/* Reproduce the six-mode N=5 rational-recovery attempt from repository inputs.
 * Usage: node this-file.cjs [maximum-lifting-rounds] [optional-output-certificate.json]
 * Exit 0 means the independent exact 9009-coefficient verifier passed.
 * Exit 2 means only the requested finite lifting budget completed; no Q-membership claim.
 * The solver and verifier use no network, credentials, LU cache, or prior lift cache.
 */
"use strict";
const fs=require("fs"),path=require("path");
const read=name=>fs.readFileSync(path.join(__dirname,name),"utf8");
const maximum=Number(process.argv[2]||4096);
if(!Number.isSafeInteger(maximum)||maximum<1)throw Error("maximum lifting rounds must be a positive safe integer");
const memory=new Map();
const store=(key,value)=>{memory.set(key,value);};
const load=key=>memory.get(key);
const notify=value=>process.stdout.write(JSON.stringify(value)+"\n");
const yield_control=()=>new Promise(resolve=>setImmediate(resolve));
const source=[
 "2026-11-13-six-mode-fifth-power-dixon-lu.js",
 "2026-11-13-six-mode-fifth-power-dixon-rhs.js",
 "2026-11-13-six-mode-fifth-power-dixon-driver-v3.js",
 "2026-11-13-six-mode-fifth-power-independent-rational-verifier.js"
].map(read).join("\n");
const api=Function("store","load","notify","yield_control",source+
 "\nreturn {prepareDixonLU,buildDixonIntegerProblem,runDixonBatch,verifyN5RationalCertificate};"
)(store,load,notify,yield_control);
const data=JSON.parse(read("2026-11-13-six-mode-fifth-power-dixon-integer-generators.json"));
const seed=JSON.parse(read("2026-11-13-six-mode-fifth-power-mod103-certificate.json"));
async function main(){
 store("replay_integer_input",data);
 const problem=api.buildDixonIntegerProblem(data);
 store("replay_integer_problem",problem);
 notify({stage:"integer target",rows:problem.rows,content:problem.rhsContent,maxDigits:problem.maxDigitsAfterContent});
 notify(await api.prepareDixonLU(data,seed,"replay_lu"));
 let step=0;
 while(step<maximum){
  const result=await api.runDixonBatch({
   prefix:"replay_lift",luPrefix:"replay_lu",
   integerDataKey:"replay_integer_input",problemKey:"replay_integer_problem",
   steps:Math.min(128,maximum-step),checkpointEvery:32,reconstructEvery:8
  });
  if(!Number.isSafeInteger(result.step)||result.step<=step)throw Error("lifting did not advance");
  step=result.step;
  if(result.success){
   const certificate=load(result.certificateKey);
   if(!certificate)throw Error("successful reconstruction omitted its certificate");
   const verified=api.verifyN5RationalCertificate(data,certificate);
   if(!verified.all_pass||verified.exactCoefficientIdentities!==9009)throw Error("independent exact verification failed: "+JSON.stringify(verified));
   if(process.argv[3])fs.writeFileSync(process.argv[3],JSON.stringify(certificate)+"\n");
   notify({status:"PASS",step,verified,identity:certificate.identity,
    scope:"Characteristic-zero algebraic identity for the supplied integer generators; application still uses the separate actual Bell inverse theorem."});
   return;
  }
 }
 notify({status:"LIFTING_CHECKPOINT_ONLY",step,scope:"No rational membership certificate has passed; increase the finite budget to continue the reproducible attempt."});
 process.exitCode=2;
}
main().catch(error=>{process.stderr.write(String(error.stack||error)+"\n");process.exitCode=1;});
