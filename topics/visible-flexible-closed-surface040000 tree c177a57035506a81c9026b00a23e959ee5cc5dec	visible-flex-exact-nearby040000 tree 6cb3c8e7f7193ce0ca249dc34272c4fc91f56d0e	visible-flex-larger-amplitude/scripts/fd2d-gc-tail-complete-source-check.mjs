// Small explicit equality fixture for stage traversal and unchanged-source extension.
// It is not a nonlinear solve or a certificate for the input physical candidate.
import fs from 'node:fs';
import crypto from 'node:crypto';
import v8 from 'node:v8';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {appendUnchangedDeepSource} from './fd2d-gc-tail-deep-extension.mjs';
import {buildStableStageGraphs as original,subdividePhysical} from './950f-tail-subdivision.mjs';
import {buildStableStageGraphs as bounded,stageGraphStatistics} from './fd2d-gc-tail-stage-graphs.mjs';
const input=process.argv[2],output=process.argv[3];
if(!input||!output)throw Error('Usage: node check.mjs INPUT_CONFIG OUTPUT_JSON');
const identity=file=>({path:file,sha256:crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex')});
const start=Date.now(),originalInput=JSON.parse(fs.readFileSync(input,'utf8'));
const cfg={...originalInput,protectCell:20,
  valleyControls:originalInput.valleyControls.slice(0,20),
  pulseCaps:originalInput.pulseCaps?.slice(0,20),
  valleyCaps:originalInput.valleyCaps?.slice(0,20),
  warpWeightLevels:originalInput.warpWeightLevels?.slice(0,20)};
const factory=createRecalibrationFactory(cfg),cache=boundTailPointCaches(factory,cfg,{pointsPerEntry:64}),
  physical=factory.assemble(),extended=appendUnchangedDeepSource(physical,24),
  stages=subdividePhysical(physical,2,2),options={modes:4,spacing:2,linearFar:8,linearSteps:16};
const a=original(physical,stages,options),b=bounded(physical,stages,options);
const differences={},counts={};
for(const key of ['graphs','gains']){
  let max=0,count=0,identical=0;
  for(let i=0;i<a[key].length;i++)for(let j=0;j<a[key][i].length;j++){
    const x=a[key][i][j],y=b[key][i][j];
    if(!Number.isFinite(x)||!Number.isFinite(y))throw Error('Nonfinite comparison');
    max=Math.max(max,Math.abs(x-y));count++;if(Object.is(x,y))identical++;
  }
  differences[key]=max;counts[key]={entries:count,bitwise_identical:identical};
}
const firstModifiedCellsRetained=physical.cells.every((c,i)=>extended.cells[i]===c);
if(!firstModifiedCellsRetained||Object.values(differences).some(v=>v!==0))throw Error('Storage-only equality check failed');
const sources=['fd2d-gc-tail-complete-source-check.mjs','fd2d-gc-tail-deep-extension.mjs',
  'fd2d-gc-tail-stage-graphs.mjs','950f-tail-subdivision.mjs','closing_weighted_tail.mjs',
  'closing_recalibrated_tail.mjs','fd2d-bounded-tail-point-cache.mjs'];
const result={schema:'fd2d-complete-tail-source-equality-fixture-v1',input:identity(input),
  source: sources.map(name=>identity(new URL(name,import.meta.url))),
  fixture_overrides:{protectCell:20,extensionEnd:24,rawDepth:2,parts:2,...options},
  scope:'Explicit small derived fixture only. It changes protectCell for this implementation equality check; it is not the original input candidate or a nonlinear DN solve. The actual full-tail entry keeps protectCell160.',
  differences,counts,first_modified_cells_retained_by_identity:firstModifiedCellsRetained,
  extension:extended.deepExtension,point_cache:cache,graph_cache:stageGraphStatistics(),
  runtime:{seconds:(Date.now()-start)/1000,heap_size_limit:v8.getHeapStatistics().heap_size_limit,
    memory:process.memoryUsage(),resources:process.resourceUsage()},completed:true};
fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({output,differences,counts,extension:extended.deepExtension.difference,
  seconds:result.runtime.seconds,peak_rss_kb:result.runtime.resources.maxRSS}));
