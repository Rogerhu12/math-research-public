// Coupled seven-valley finite linear design search; not nonlinear validation.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
const [sourceTopic,portFile,outFile,steps='64',count='7',iterations='180']=process.argv.slice(2);
const sourceRoot=path.join(sourceTopic,'repro/source-root');process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const rawConfig=JSON.parse(fs.readFileSync(portFile,'utf8')),config=rawConfig.parameters??rawConfig,configFile=outFile.replace(/\.json$/,'-input.json');fs.writeFileSync(configFile,JSON.stringify(config,null,2)+'\n');
const script=path.join(sourceTopic,'scripts/closing_weighted_hard_gate_opt.mjs');let code=fs.readFileSync(script,'utf8');
const replacements=[["'./closing_weighted_tail.mjs'",JSON.stringify(pathToFileURL(path.join(sourceTopic,'scripts/closing_weighted_tail.mjs')).href)],["p=32","p=8"],["objectivePower:32","objectivePower:8"]];
for(const [from,to] of replacements){if(!code.includes(from))throw Error('Missing replacement '+from);code=code.replace(from,to);}
const marker="await evaluate(base.slice(0,number),'input');";if(!code.includes(marker))throw Error('Missing optimizer body marker');code=code.slice(0,code.indexOf(marker));
const body=String.raw`
const bound=x=>x.map(v=>Math.max(-10,Math.min(16,v)));
let simplex=[await evaluate(base.slice(0,number),'simplex input')];
for(let j=0;j<number;j++){const x=base.slice(0,number);x[j]+=.25;simplex.push(await evaluate(x,'simplex seed '+j));}
for(let iter=0;iter<MAX_ITER;iter++){
 simplex.sort((a,b)=>b.score-a.score);
 const top=simplex[0],worst=simplex[number],second=simplex[number-1],center=Array(number).fill(0);
 for(let j=0;j<number;j++)for(let k=0;k<number;k++)center[k]+=simplex[j].x[k]/number;
 const far=Math.max(...simplex.map(r=>Math.hypot(...r.x.map((v,j)=>v-top.x[j]))));
 if(far<.003)break;
 const reflection=await evaluate(bound(center.map((v,j)=>2*v-worst.x[j])),'simplex reflect '+iter);
 if(reflection.score>top.score){
  const expansion=await evaluate(bound(center.map((v,j)=>3*v-2*worst.x[j])),'simplex expand '+iter);
  simplex[number]=expansion.score>reflection.score?expansion:reflection;
 }else if(reflection.score>second.score){simplex[number]=reflection;}
 else{
  const outside=reflection.score>worst.score,ref=outside?reflection:worst;
  const contraction=await evaluate(bound(center.map((v,j)=>.5*(v+ref.x[j]))),'simplex contract '+iter);
  if(contraction.score>(outside?reflection.score:worst.score)){simplex[number]=contraction;}
  else for(let j=1;j<=number;j++)simplex[j]=await evaluate(bound(simplex[j].x.map((v,k)=>.5*(v+top.x[k]))),'simplex shrink '+iter);
 }
}
console.log(JSON.stringify({finished:true,evaluations:history.length,best}));
`;
code+=body.replace('MAX_ITER',String(Number(iterations)));
fs.writeFileSync(outFile.replace(/\.json$/,'-manifest.json'),JSON.stringify({scope:'Finite linear design, maximizing soft minimum of physical mode-two positive-branch gates. Each evaluation changes the metric.',source_sha256:Object.fromEntries([script,portFile].map(file=>[file,crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex')])),replacements,driver_sha256:crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex'),steps:Number(steps),mode:2,far:32,controls:Number(count),maxIterations:Number(iterations)},null,2)+'\n');
process.argv=[process.argv[0],script,configFile,outFile,'2',steps,'32',count];await import('data:text/javascript;base64,'+Buffer.from(code).toString('base64'));
