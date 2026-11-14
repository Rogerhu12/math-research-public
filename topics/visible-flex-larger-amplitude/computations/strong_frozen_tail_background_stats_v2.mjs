// v2: preflight the real primary.summary.height_max; preserve factory stats before endpoint diagnostics.
// AI-assisted finite background diagnostic, strong_recovery, 2026-11-13.
// This entry is deliberately outside the frozen production MJS directory.
// It reads the original factory's existing background height integrals. It
// does not construct a nonlinear D-N solver, integrate shooting states, or
// replace the actual nonlinear mean by the background in any acceptance gate.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {gunzipSync, gzipSync} from 'node:zlib';
import {pathToFileURL, fileURLToPath} from 'node:url';

const argv=process.argv.slice(2), options={};
for(let j=0;j<argv.length;j+=2){
  if(!argv[j].startsWith('--')||j+1>=argv.length||options[argv[j]])throw Error('Distinct explicit path arguments required');
  options[argv[j]]=path.resolve(argv[j+1]);
}
const required=['runtime-computations','source-topic','config','actual-primary','actual-owned',
  'actual-ready','stored-reference-ready','ledger-ready','out'];
for(const name of required)if(!options['--'+name])throw Error('Missing --'+name);
if(Object.keys(options).length!==required.length)throw Error('Undeclared diagnostic argument');
const sha=data=>crypto.createHash('sha256').update(data).digest('hex');
const hashes={},checks={};
function read(file){const b=fs.readFileSync(file);hashes[file]=sha(b);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());}
function check(name,value){if(!value)throw Error('Frozen background check failed: '+name);checks[name]=true;}
function equal(a,b){
  if(typeof a==='number'||typeof b==='number')return Object.is(a,b);
  if(a===b)return true;
  if(!a||!b||typeof a!=='object'||typeof b!=='object'||Array.isArray(a)!==Array.isArray(b))return false;
  const ak=Object.keys(a).sort(),bk=Object.keys(b).sort();
  return ak.length===bk.length&&ak.every((k,j)=>k===bk[j]&&equal(a[k],b[k]));
}
const config=read(options['--config']),primary=read(options['--actual-primary']);
const owned=read(options['--actual-owned']),actualReady=read(options['--actual-ready']);
read(options['--stored-reference-ready']);read(options['--ledger-ready']);
check('actual_original_owned_exit_zero',owned.exitcode===0&&owned.wait4_observed===true);
check('genuine_finite_actual_primary',primary.solver_success===true&&primary.audit_pending===false
  &&primary.config.actual_nonlinear_tail===true&&primary.modes===32);
check('exact_original_ready_object',equal(actualReady,primary.actual_tail.ready));
const height0=primary.summary.height_max;
check('finite_prefix_height_sample',Number.isFinite(height0)&&height0>0);
const ioKeys=new Set(['traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint']);
for(const key of new Set([...Object.keys(config),...Object.keys(primary.actual_tail.config)]))
  if(!ioKeys.has(key))check('same_nonIO_tail_'+key,equal(config[key],primary.actual_tail.config[key]));
const sourceDir=options['--runtime-computations'];
const pins={
  'tail_frozen_geometry.mjs':'db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3',
  'strong_frozen_calibration_factory.mjs':'77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247',
  'closure_bounded_point_cache.mjs':'35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043'
};
for(const [name,want] of Object.entries(pins)){
  const file=path.join(sourceDir,name),got=sha(fs.readFileSync(file));hashes[file]=got;
  check('unchanged_original_'+name,got===want);
}
process.env.VISIBLE_FLEX_SOURCE_TOPIC=options['--source-topic'];
process.env.VISIBLE_FLEX_FROZEN_LEDGER_READY=options['--ledger-ready'];
process.env.VISIBLE_FLEX_FROZEN_STORED_READY=options['--stored-reference-ready'];
process.env.VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT='8';
const start=process.hrtime.bigint();
const module=await import(pathToFileURL(path.join(sourceDir,'tail_frozen_geometry.mjs')).href);
const {physical,factory,manifest}=await module.createStoredPhysical(config);
const old=actualReady.storedMetricAdapter;
check('same_complete_160_cell_geometry',physical.cells.length===160&&manifest.cellCount===160
  &&manifest.profileFingerprintBefore===old.profileFingerprintBefore
  &&manifest.profileFingerprintAfter===old.profileFingerprintAfter
  &&manifest.profileFingerprintBefore===manifest.profileFingerprintAfter);
check('same_saved_global_warp_alpha',Object.is(physical.stats.alpha,old.frozenWarpAlpha));
for(const key of new Set([...Object.keys(manifest.physicalParameters),...Object.keys(old.physicalParameters)]))
  if(!ioKeys.has(key))check('same_stored_physical_parameter_'+key,
    equal(manifest.physicalParameters[key],old.physicalParameters[key]));
const checkpointPath=options['--out'].replace(/\.json\.gz$/, '')+'-factory-checkpoint.json.gz';
const factoryCheckpoint={schema:'same-frozen-tail-original-background-factory-checkpoint-v1',
  scope:'Original background factory identity and stats only; no nonlinear tail mean or closed geometry claimed.',
  created_utc:new Date().toISOString(),input_sha256:hashes,checks:{...checks},
  source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
  original_geometry_manifest:manifest,original_background_stats:physical.stats,
  original_physical_parameters:physical.parameters,saved_prefix_height_max:height0,
  cells:physical.cells.map((cell,n)=>({cell:n,rStart:cell.rStart,rEnd:cell.rEnd,
    localWidth:cell.localWidth,meridianLength:cell.meridianLength,heightSpan:cell.heightSpan})),
  no_nonlinear_tail_or_variational_solve_called:true,complete_endpoint_report_pending:true};
fs.writeFileSync(checkpointPath,gzipSync(Buffer.from(JSON.stringify(factoryCheckpoint,null,2)+'\n'),{level:9}),{flag:'wx'});
console.log(JSON.stringify({event:'original_background_factory_checkpoint',file:checkpointPath,
  sha256:sha(fs.readFileSync(checkpointPath)),heightSpan:physical.stats.heightSpan}));
const rows=[],endpoints=[];let h=0,maxEndpoint=0,maxRectangle=0;
function addEndpoint(cell,segment,end,r){
  const z=height0+h,norm=Math.hypot(r,z);maxEndpoint=Math.max(maxEndpoint,norm);
  endpoints.push({cell,segment,end,radius:r,background_height_from_cut:h,
    conditional_z_from_saved_prefix_height_sample:z,conditional_norm:norm});
}
addEndpoint(0,physical.cells[0].profiles.length-1,1,physical.cells[0].profiles.at(-1)(1).r);
for(let n=0;n<physical.cells.length;n++){
  const cell=physical.cells[n],entries=factory.getEntries(n,config.valleyControls?.[n]??0);
  check('original_cell_height_'+n,Object.is(cell.heightSpan,entries.total[4]+physical.stats.alpha*entries.total[5]));
  let cellHeight=0;
  for(let j=cell.profiles.length-1;j>=0;j--){
    const profile=cell.profiles[j],entry=entries.entries[j];
    const outer=profile(1),inner=profile(0);
    const delta=entry.total[4]+physical.stats.alpha*entry.total[5];
    check('finite_nonnegative_background_height_'+n+'_'+j,
      Number.isFinite(delta)&&delta>=0&&Number.isFinite(outer.r)&&Number.isFinite(inner.r)&&outer.r>=inner.r);
    const begin=h;h+=delta;cellHeight+=delta;
    const rectangle=Math.hypot(outer.r,height0+h);maxRectangle=Math.max(maxRectangle,rectangle);
    rows.push({cell:n,segment:j,outer_radius:outer.r,inner_radius:inner.r,
      original_entry_total_height_A:entry.total[4],original_entry_total_height_B:entry.total[5],
      background_height_increment:delta,cumulative_height_before:begin,cumulative_height_after:h,
      floating_monotone_background_rectangle_norm:rectangle});
    addEndpoint(n,j,0,inner.r);
  }
  rows.at(-1).original_cell_heightSpan=cell.heightSpan;
  rows.at(-1).reverse_segment_sum_minus_original_cell_height=cellHeight-cell.heightSpan;
}
check('all_original_head_segments_retained',rows.length===physical.cells.reduce((s,c)=>s+c.profiles.length,0));
check('finite_reported_height_span',Number.isFinite(physical.stats.heightSpan)&&physical.stats.heightSpan>=0);
const result={schema:'same-frozen-tail-background-height-diagnostic-v1',
  scope:'Original 160-cell frozen rotational background geometry only. Its existing scalar height integrals and all profile endpoints are reused. No nonlinear tail mean, complete closed-surface diameter, reach, or Hausdorff amplitude is certified.',
  created_utc:new Date().toISOString(),source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
  input_sha256:hashes,checks,all_checks:true,original_geometry_manifest:manifest,
  original_background_stats:physical.stats,original_physical_parameters:physical.parameters,
  original_factory_checkpoint:{file:checkpointPath,sha256:sha(fs.readFileSync(checkpointPath))},
  original_same_metric_cut:primary.physical_tail_cut,
  saved_actual_prefix_height_max_sample:height0,
  all_160_cells_background_height_sum:h,
  reverse_profile_sum_minus_original_stats_height:h-physical.stats.heightSpan,
  complete_head_profile_count:rows.length,rows,endpoints,
  background_finite_endpoint_diameter_diagnostic:2*maxEndpoint,
  background_floating_monotone_rectangle_diameter_diagnostic:2*maxRectangle,
  diameter_diagnostic_assumptions:['Start z at the saved finite prefix height maximum, not a verified cut mean.',
    'Use the rotational background height increments, not the current nonlinear full-mean increments.',
    'Finite original quadrature is not interval bounded here; deep cells beyond the 160-cell head and the flat closure are not certified.'],
  no_new_nonlinear_tail_or_variational_solve_called:true,no_actual_acceptance_gate_changed:true,
  production_MJS_files_unchanged:true,original_factory_scalar_quadratures_only:true,
  seconds:Number(process.hrtime.bigint()-start)/1e9};
const outputText=JSON.stringify(result,null,2)+'\n';
fs.writeFileSync(options['--out'],options['--out'].endsWith('.gz')
  ?gzipSync(Buffer.from(outputText),{level:9}):outputText,{flag:'wx'});
console.log(JSON.stringify({out:options['--out'],sha256:sha(fs.readFileSync(options['--out'])),
  checks:Object.keys(checks).length,backgroundHeightSpan:physical.stats.heightSpan,
  cumulativeHeight:h,endpointDiameter:2*maxEndpoint,rectangleDiameter:2*maxRectangle,
  seconds:result.seconds,noNonlinearTailSolve:true}));
