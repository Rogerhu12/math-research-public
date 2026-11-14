// Reuse the source's finite physical gate optimizer for mode two.
// Every trial changes the metric; no trial is a nonlinear tail or refinement proof.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
const [sourceTopic,portFile,outFile,steps='96',count='7']=process.argv.slice(2);
const sourceRoot=path.join(sourceTopic,'repro/source-root');process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const rawConfig=JSON.parse(fs.readFileSync(portFile,'utf8')),config=rawConfig.parameters??rawConfig,configFile=outFile.replace(/\.json$/,'-input.json');fs.writeFileSync(configFile,JSON.stringify(config,null,2)+'\n');
const script=path.join(sourceTopic,'scripts/closing_weighted_hard_gate_opt.mjs');let code=fs.readFileSync(script,'utf8');
const changes=[["'./closing_weighted_tail.mjs'",JSON.stringify(pathToFileURL(path.join(sourceTopic,'scripts/closing_weighted_tail.mjs')).href)],["[2,1,.5,.25,.125,.0625,.03125,.015625]","[2,1,.5,.25,.125,.0625]"],["pass<5","pass<3"]];
for(const [from,to] of changes){if(!code.includes(from))throw Error('Missing explicit optimizer replacement '+from);code=code.replace(from,to);}
const sourceHashes=Object.fromEntries([script,portFile,...['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs'].map(x=>path.join(sourceTopic,'scripts',x))].map(file=>[file,crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex')]));
fs.writeFileSync(outFile.replace(/\.json$/,'-manifest.json'),JSON.stringify({scope:'Finite linear design optimization only, with independently documented source adaptation.',source_revision:fs.existsSync(path.join(sourceTopic,'source-origin.json'))?JSON.parse(fs.readFileSync(path.join(sourceTopic,'source-origin.json'),'utf8')).source_revision:null,sourceHashes,changes,sourceTopic,portFile,steps:Number(steps),mode:2,far:32,controls:Number(count)},null,2)+'\n');
process.argv=[process.argv[0],script,configFile,outFile,'2',steps,'32',count];await import('data:text/javascript;base64,'+Buffer.from(code).toString('base64'));
