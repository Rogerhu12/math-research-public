// Original accepted-A fixed metric at interior points of its 576 saved stages.
// This evaluates only frozen background profiles, with no point-root or ODE.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
const args=process.argv.slice(2),opt={};
for(let i=0;i<args.length;i+=2)opt[args[i]]=args[i+1];
for(const k of ['--repo-root','--source-topic','--out'])if(!opt[k])throw Error('Missing '+k);
const repo=path.resolve(opt['--repo-root']),sourceTopic=path.resolve(opt['--source-topic']);
const topic=path.join(repo,'topics/visible-flex-larger-amplitude'),comp=path.join(topic,'computations'),notes=path.join(topic,'notes');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const configPath=path.join(notes,'2026-11-13-strong-q126-m32-tail2-actual-r1-config.json');
const configBytes=fs.readFileSync(configPath);
if(sha(configBytes)!=='3b0deaaf0cdc65a34a8e4652e0a04d96a840db354ccada71d9cba5e4cd228e23')throw Error('Wrong original A config');
const config=JSON.parse(configBytes);
const ledger=path.join(notes,'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json');
const stored=path.join(notes,'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json');
process.env.VISIBLE_FLEX_SOURCE_TOPIC=sourceTopic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_FROZEN_LEDGER_READY=ledger;
process.env.VISIBLE_FLEX_FROZEN_STORED_READY=stored;
process.env.VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT='8';
process.env.CLOSING_TAIL_CACHE=path.join(sourceTopic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const {createStoredPhysical}=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')).href);
const {subdividePhysical}=await import(pathToFileURL(path.join(sourceTopic,'scripts/950f-tail-subdivision.mjs')).href);
const {physical,manifest}=await createStoredPhysical(config);
const stages=subdividePhysical(physical,config.depth,config.shootingParts);
if(stages.cells.length!==576)throw Error('Wrong original subdivision');
const xs=[0,.0625,.125,.25,.375,.5,.625,.75,.875,.9375,1];
const rows=stages.cells.map((cell,stage)=>{
  if(cell.profiles.length!==1)throw Error('Expected one original subprofile');
  return {stage,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
    points:xs.map(x=>{
      const raw=cell.profiles[0](x),w=Math.exp(raw.logw),w2=Math.exp(2*raw.logw);
      const g={...raw,w,w2,E:1+w2};
      if(!(g.r>0&&g.drdx>0&&Number.isFinite(g.w)))throw Error('Invalid background point');
      return {x,r:g.r,w:g.w,E:g.E,drdx:g.drdx,dlogwdx:g.dlogwdx};
    })};
});
const result={schema:'actual-A-original-metric-interior-samples-v1',
  source_sha256:sha(fs.readFileSync(new URL(import.meta.url))),
  original_config_sha256:sha(configBytes),ledger_sha256:sha(fs.readFileSync(ledger)),
  stored_reference_sha256:sha(fs.readFileSync(stored)),
  source_manifest_sha256:sha(fs.readFileSync(path.join(comp,'source-dependencies.json'))),
  original_profile_fingerprint:manifest.profileFingerprintAfter,
  stages:576,samples_per_stage:xs.length,rows,
  scope:'Finite background-profile samples in exactly the original frozen A metric. No new point roots or ODE. Not interval bounds.'};
fs.writeFileSync(opt['--out'],JSON.stringify(result)+'\n',{flag:'wx'});
console.log(JSON.stringify({file:opt['--out'],stages:576,samples:rows.length*xs.length}));
