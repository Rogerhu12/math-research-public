#!/usr/bin/env node
"use strict";
/*
R791: read the actual J-only first-return type-five spectrum.
This compatibility wrapper reuses the unchanged R773 producer and all original
R594/R702/R715/R734 source constraints. It adds only the already available
oddSource(raw0) and oddSource(raw1) outputs. No new adaptation or data input.
All numerical execution is on public GitHub Actions.
*/
const fs=require("fs"),path=require("path"),Module=require("module"),crypto=require("crypto");
const original=path.join(__dirname,"check-r773-native-conditional-five-moments.js");
let code=fs.readFileSync(original,"utf8");
const originalSHA=crypto.createHash("sha256").update(code).digest("hex");
const mark="conditional_theta_descending:theta.solution,complete_spectrum:spectrum,";
if(code.split(mark).length!==2)throw Error("R773 existing spectrum output entry changed");
code=code.replace(mark,()=>mark+
 "first_return_spectrum:oddSource(raw0),second_return_spectrum:oddSource(raw1),"+
 "J_only_prefactor:"+JSON.stringify("lambda^N*beta^N").replace(/"/g,'\\"')+","+
 "J_only_scope:"+JSON.stringify("Exact auxiliary boundary of R786(21)-(22); full E inverse and M-unit term retained, no U subtraction.").replace(/"/g,'\\"')+",");
const finalMark="const derived=path.join(__dirname,";
if(code.split(finalMark).length!==2)throw Error("R773 module boundary changed");
code=code.replace(finalMark,()=>
 "process.stderr.write("+JSON.stringify("R791 R773 producer SHA256 "+originalSHA+"\n")+");\n"+finalMark);
const derived=path.join(__dirname,"check-r791-j-only-arithmetic-amplitudes.compiled.js");
const mod=new Module(derived,module);
mod.filename=derived;mod.paths=module.paths;mod._compile(code,derived);
