const fs=require("node:fs"),path=require("node:path");
const source=fs.readFileSync(path.join(__dirname,"2026-11-13-universal-birth-one-first-edge-support-certificates-1cf.mjs"),"utf8");
const verify=new Function(source+"\nreturn verifyUniversalBirthOneFirstEdge;")();
verify({onProgress:async p=>{process.stdout.write(JSON.stringify(p)+"\n");await new Promise(resolve=>setImmediate(resolve));}})
.then(result=>{process.stdout.write(JSON.stringify(result,null,2)+"\n");if(!result.all_pass)process.exitCode=1;})
.catch(error=>{process.stderr.write(String(error.stack||error)+"\n");process.exitCode=1;});
