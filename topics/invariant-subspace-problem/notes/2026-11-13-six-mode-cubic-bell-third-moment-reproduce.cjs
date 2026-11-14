#!/usr/bin/env node
'use strict';
const fs=require('fs'),path=require('path'),vm=require('vm');
const dir=__dirname,ctx={};
vm.runInNewContext(fs.readFileSync(path.join(dir,'2026-11-13-six-mode-cubic-bell-third-moment-verify.js'),'utf8'),ctx);
const result=ctx.verifySixModeCubicBellStructure();
const saved=JSON.parse(fs.readFileSync(path.join(dir,'2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json'),'utf8'));
for(const k of ['K','J3','adjugateJ3','detJ3'])
 if(JSON.stringify(result.data[k])!==JSON.stringify(saved[k]))throw Error('stored exact data differs: '+k);
delete result.data;result.storedDataMatches=true;
process.stdout.write(JSON.stringify(result,null,2)+'\n');

