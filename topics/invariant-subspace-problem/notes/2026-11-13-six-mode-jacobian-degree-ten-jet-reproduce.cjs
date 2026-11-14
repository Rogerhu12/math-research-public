// Reproduce the complete certificate from the three saved JSON inputs.
const fs=require("node:fs"),path=require("node:path");
const read=name=>JSON.parse(fs.readFileSync(path.join(__dirname,name),"utf8"));
const source=fs.readFileSync(path.join(__dirname,"2026-11-13-six-mode-jacobian-degree-ten-jet-verify.js"),"utf8");
const verify=new Function(source+"\nreturn verifySixModeJacobianJetCertificate;")();
(async()=>{
 const result=await verify(
  read("2026-11-13-six-mode-fifth-power-dixon-integer-generators.json"),
  read("2026-11-13-six-mode-jacobian-degree-ten-jet-certificate.json"),
  read("2026-11-13-six-mode-fifth-power-mod103-certificate.json"),
  {onProgress:async p=>{process.stdout.write(JSON.stringify(p)+"\n");await new Promise(resolve=>setImmediate(resolve));}}
 );
 process.stdout.write(JSON.stringify(result,null,2)+"\n");
 if(!result.all_pass)process.exitCode=1;
})().catch(error=>{process.stderr.write(String(error.stack||error)+"\n");process.exitCode=1;});
