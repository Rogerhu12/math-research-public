// Explicit in-memory capacity extension of three pinned tail constructors.
// Numerical equations, quadrature guards, positive branch, Newton policy,
// complete DN Jacobian and full finite audit are unchanged.  No source file
// is modified.  Use as Node 24 --import before tail_frozen_worker.mjs.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {registerHooks} from 'node:module';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('Tail execution belongs to this public repository GitHub Actions');
const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
const requestedCapacity=Number(process.env.VISIBLE_FLEX_TAIL_MODE_CAPACITY);
const capacity=Math.max(64,requestedCapacity);
const recordPath=process.env.VISIBLE_FLEX_TAIL_CAPACITY_RECORD;
if(!topic||!Number.isSafeInteger(requestedCapacity)||requestedCapacity<1||!recordPath)
  throw Error('Explicit source topic, integer mode capacity and manifest path required');
const sha=raw=>crypto.createHash('sha256').update(raw).digest('hex');
const specifications=[
  {relative:'scripts/78718-tail-fourier-root-momentum.mjs',
   sha256:'cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88',
   changes:[['M>=1&&M<=64&&Number.isInteger(M)',`M>=1&&M<=${capacity}&&Number.isInteger(M)`]]},
  {relative:'repro/source-root/topics/large-amplitude-twist-flex/scripts/general_root_tail_momentum.mjs',
   sha256:'182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c',
   changes:[['M>=1&&M<=64&&Number.isInteger(M)',`M>=1&&M<=${capacity}&&Number.isInteger(M)`]]},
  {relative:'repro/source-root/topics/large-amplitude-twist-flex/scripts/general_exact_tail_cauchy.mjs',
   sha256:'f33343a8f9e7e3180513e7bf20fa620c5bf5329ef3d0949d8cbac0e2994b70b4',
   changes:[['M<1||M>64||!Number.isInteger(spacing)',`M<1||M>${capacity}||!Number.isInteger(spacing)`],
            ['Require 1<=modes<=64, integer spacing, quadrature>4*modes*spacing.',
             `Require 1<=modes<=${capacity}, integer spacing, quadrature>4*modes*spacing.`]]}
];
const prepared=new Map();
for(const item of specifications){
  const file=path.resolve(topic,item.relative),raw=fs.readFileSync(file);
  if(sha(raw)!==item.sha256)throw Error('Pinned capacity source changed: '+item.relative);
  let transformed=raw.toString('utf8');
  for(const [before,after] of item.changes){
    if(transformed.split(before).length!==2)throw Error('Capacity source anchor is not unique: '+item.relative);
    transformed=transformed.replace(before,after);
  }
  prepared.set(file,{...item,original:raw.toString('utf8'),transformed,
    transformedSHA256:sha(transformed),loaded:false});
}
const manifest={
  name:'pinned-tail-constructor-mode-capacity-v1',capacity,requestedCapacity,
  nodeVersion:process.version,adapterSHA256:sha(fs.readFileSync(new URL(import.meta.url))),
  originalConstructorCapacity:64,originalFilesModified:false,
  numericalChange:'Only the three constructor mode ceilings and the corresponding error-message ceiling.',
  retained:['M integer and M>=1','quadrature>4*M*spacing','all physical parameters and frozen metric',
    'D/S/A projectionFloor','root tolerance 8e-14 and existing 5e-12 roundoff fallback',
    'original Newton and line search','complete actual variational shooting',
    'original endpoint jets and source second differences','requested full finite audit'],
  scope:'A finite mode capacity adapter. High-mode conditioning, actual solves and mode/radial/angle/depth convergence remain to be measured.',
  files:[]
};
function save(){
  manifest.files=[...prepared.values()].map(({relative,sha256,changes,transformedSHA256,loaded})=>
    ({relative,originalSHA256:sha256,changes,transformedSHA256,loaded}));
  fs.writeFileSync(recordPath,JSON.stringify(manifest,null,2)+'\n');
}
fs.writeFileSync(recordPath,'',{flag:'wx'});
save();
registerHooks({
  load(url,context,nextLoad){
    const loaded=nextLoad(url,context);
    if(!url.startsWith('file:'))return loaded;
    const entry=prepared.get(path.resolve(fileURLToPath(url)));
    if(!entry)return loaded;
    const actual=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
    if(sha(actual)!==entry.sha256)throw Error('Actual loaded capacity source changed: '+entry.relative);
    entry.loaded=true;save();
    return {...loaded,source:entry.transformed};
  }
});
