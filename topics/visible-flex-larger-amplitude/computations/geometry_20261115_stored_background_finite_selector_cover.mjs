#!/usr/bin/env node
// Exact coverage of the ORIGINAL FINITE background selector, not continuous g.
// Source-only component: actual scalar evaluations run only in public Actions.
// No nonlinear solver, new target metric, true inverse or monotonicity is assumed.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {gunzipSync} from 'node:zlib';
import {fileURLToPath,pathToFileURL} from 'node:url';

const REPOSITORY='Rogerhu12/math-research-public';
const SCHEMA='original-stored-background-finite-selector-closed-cover-v1';
const QUERY_SCHEMA='original-stored-background-finite-selector-closed-queries-v1';
const PINS={
 'tail_frozen_geometry.mjs':'db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3',
 'strong_frozen_calibration_factory.mjs':'77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247',
 'closure_bounded_point_cache.mjs':'35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043',
 'exact_20261114_closed_background.mjs':'be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b'
};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const canonical=o=>Buffer.from(JSON.stringify(o)+'\n');
const ownFile=fileURLToPath(import.meta.url);
const ownSHA=sha(fs.readFileSync(ownFile));
function requireActions(){
 if(process.env.GITHUB_ACTIONS!=='true'||process.env.GITHUB_REPOSITORY!==REPOSITORY)
  throw Error('Original scalar geometry arithmetic runs only in the named public Actions repository');
}
function insist(ok,message){if(!ok)throw Error(message);}
function finite(x,label){insist(typeof x==='number'&&Number.isFinite(x),'Nonfinite original '+label);return x;}
function word(x){
 const b=Buffer.alloc(8);b.writeDoubleLE(x);
 return {value:Number.isFinite(x)?x:null,float64le_hex:b.toString('hex'),
  classification:Number.isNaN(x)?'NaN':x===Infinity?'positive-infinity':x===-Infinity?'negative-infinity':Object.is(x,-0)?'negative-zero':'finite'};
}
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;}
function rational(a,b=1n){
 insist(b!==0n,'Zero rational denominator');if(b<0n){a=-a;b=-b;}
 const d=gcd(a,b);return {n:a/d,d:b/d};
}
function fromNumber(x){
 finite(x,'rational endpoint');
 const b=Buffer.alloc(8);b.writeDoubleLE(x);
 const bits=b.readBigUInt64LE(),negative=(bits>>63n)!==0n;
 const e=Number((bits>>52n)&2047n),fraction=bits&((1n<<52n)-1n);
 let m=e===0?fraction:fraction+(1n<<52n),p=e===0?-1074:e-1075;
 if(negative)m=-m;
 return p>=0?rational(m<<BigInt(p)):rational(m,1n<<BigInt(-p));
}
function parseRational(value){
 if(typeof value==='number')return fromNumber(value);
 insist(typeof value==='string'&&/^-?[0-9]+(?:\/[1-9][0-9]*)?$/.test(value),
  'Query endpoint must be a finite JSON binary64 number or an exact integer/fraction string');
 const [a,b='1']=value.split('/');return rational(BigInt(a),BigInt(b));
}
const cmp=(a,b)=>{const x=a.n*b.d-b.n*a.d;return x<0n?-1:x>0n?1:0;};
const rtext=a=>a.d===1n?String(a.n):String(a.n)+'/'+String(a.d);
function interval(a,b,lc=true,rc=true){return {a,b,lc,rc};}
function nonempty(x){const c=cmp(x.a,x.b);return c<0||(c===0&&x.lc&&x.rc);}
function intersection(x,y){
 const l=cmp(x.a,y.a),r=cmp(x.b,y.b);
 const z=interval(l>=0?x.a:y.a,r<=0?x.b:y.b,
  l===0?x.lc&&y.lc:l>0?x.lc:y.lc,
  r===0?x.rc&&y.rc:r<0?x.rc:y.rc);
 return nonempty(z)?z:null;
}
function subtract(x,y){
 const z=intersection(x,y);if(!z)return [x];
 return [interval(x.a,z.a,x.lc,!z.lc),interval(z.b,x.b,!z.rc,x.rc)].filter(nonempty);
}
function showInterval(x){return {left:rtext(x.a),right:rtext(x.b),left_closed:x.lc,right_closed:x.rc};}
function readBound(file,want,label){
 const resolved=path.resolve(file),raw=fs.readFileSync(resolved);
 insist(/^[0-9a-f]{64}$/.test(want)&&sha(raw)===want,label+' exact bytes differ');
 const decoded=raw[0]===31&&raw[1]===139?gunzipSync(raw):raw;
 return {value:JSON.parse(decoded.toString('utf8')),raw,receipt:{file:resolved,bytes:raw.length,sha256:want,
  encoding:decoded===raw?'plain-json':'gzip-json',decoded_bytes:decoded.length,decoded_sha256:sha(decoded)}};
}
function receipt(file,root){
 const raw=fs.readFileSync(file);
 return {file:path.relative(root,file),bytes:raw.length,sha256:sha(raw)};
}
function argumentMap(argv){
 const out={};
 for(let i=0;i<argv.length;i+=2){
  insist(argv[i]?.startsWith('--')&&i+1<argv.length&&!(argv[i] in out),'Distinct explicit value arguments required');
  out[argv[i]]=argv[i+1];
 }
 const required=['--runtime-computations','--source-topic','--config','--config-sha256',
  '--ledger-ready','--ledger-ready-sha256','--stored-ready','--stored-ready-sha256','--out'];
 for(const k of required)insist(out[k], 'Missing '+k);
 const allowed=new Set([...required,'--plan','--plan-sha256','--queries','--queries-sha256',
  '--budget-seconds','--max-selector-nodes']);
 for(const k of Object.keys(out))insist(allowed.has(k),'Unknown argument '+k);
 for(const k of ['--plan','--queries'])insist(Boolean(out[k])===Boolean(out[k+'-sha256']),'Pair '+k+' with its SHA');
 return out;
}
function logWriter(file){
 const fd=fs.openSync(file,'wx'),hash=crypto.createHash('sha256');
 let lines=0,bytes=0,closed=false;
 return {
  add(o){insist(!closed,'Closed ledger');const raw=canonical(o);let offset=0;
   while(offset<raw.length){const written=fs.writeSync(fd,raw,offset,raw.length-offset);
    insist(written>0,'Zero-byte ledger write');offset+=written;}
   hash.update(raw);bytes+=raw.length;lines++;},
  finish(){if(!closed){fs.fsyncSync(fd);fs.closeSync(fd);closed=true;}
   return {file:path.basename(file),bytes,lines,sha256:hash.digest('hex')};}
 };
}
function originalE(g){
 const w=Math.exp(g.logw);
 const E=1+w*w;
 return {w:word(w),E:word(E),logw:word(g.logw)};
}
function explicitFlatOverride(piece,p){
 // This is the precise source-level assignment in closing_recalibrated_tail.
 // The later cut-preserving overrides are excluded even if an endpoint agrees.
 const last=p.flatOuterThroughCell,start=p.flatOuterStartSegment??2;
 if(!(Number.isInteger(last)&&last>=0&&p.flatSlope>0))return null;
 if(!(piece.n<last||(piece.n===last&&piece.j>start)))return null;
 const final=piece.profileCount-1;
 if(p.capMode==='cut-preserving'&&piece.n===0&&(piece.j===final||piece.j===final-1))return null;
 return {rule:'original explicit flatOuter logw assignment, after cap and before only chi/j0 changes',
  flatOuterThroughCell:last,flatOuterStartSegment:start,flatSlope:word(p.flatSlope),
  cell:piece.n,segment:piece.j,excluded_later_cut_preserving_overrides:true,
  original_logw_is_the_same_number_for_every_x_in_closed_0_1:true};
}
function selectedParts(query,pieces,cut,cuff){
 let left=[query];const selected=[];
 function take(owner,domain){
  const rest=[];
  for(const piece of left){
   const yes=intersection(piece,domain);if(yes)selected.push({...owner,domain:yes});
   rest.push(...subtract(piece,domain));
  }
  left=rest;
 }
 // Exact original priority: cut, cuff, then .find in original list order.
 take({kind:'cut'},interval(cut,cut));
 take({kind:'cuff'},interval(cuff,cuff));
 for(const piece of pieces)take({kind:'piece',piece},interval(piece.innerQ,piece.outerQ));
 return {selected,uncovered:left};
}

export async function runOriginalFiniteSelectorCover(options){
 requireActions();
 const args=options;
 const budgetSeconds=Number(args['--budget-seconds']??600);
 const maxNodes=Number(args['--max-selector-nodes']??100000);
 insist(Number.isFinite(budgetSeconds)&&budgetSeconds>0&&Number.isSafeInteger(maxNodes)&&maxNodes>0,
  'Explicit positive computation resources required');
 const start=performance.now(),out=path.resolve(args['--out']);
 insist(!fs.existsSync(out),'Use a new producer-owned output directory');
 fs.mkdirSync(out,{recursive:true});fs.mkdirSync(path.join(out,'large-arrays'));
 const comp=path.resolve(args['--runtime-computations']),sourceTopic=path.resolve(args['--source-topic']);
 const config=readBound(args['--config'],args['--config-sha256'],'Original config');
 const ledger=readBound(args['--ledger-ready'],args['--ledger-ready-sha256'],'Original calibration ledger');
 const stored=readBound(args['--stored-ready'],args['--stored-ready-sha256'],'Original stored reference');
 const plan=args['--plan']?readBound(args['--plan'],args['--plan-sha256'],'Optional original closed plan'):null;
 const request=args['--queries']?readBound(args['--queries'],args['--queries-sha256'],'Exact closed queries'):null;
 const sources={};
 for(const [name,want] of Object.entries(PINS)){
  const raw=fs.readFileSync(path.join(comp,name));insist(sha(raw)===want,'Original source differs: '+name);
  sources[name]={bytes:raw.length,sha256:want};
 }
 if(plan)insist(plan.value.inputs.config.sha256===config.receipt.sha256,'Plan and original config differ');
 Object.assign(process.env,{
  VISIBLE_FLEX_SOURCE_TOPIC:sourceTopic,
  VISIBLE_FLEX_SOURCE_ROOT:path.join(sourceTopic,'repro/source-root'),
  VISIBLE_FLEX_FROZEN_LEDGER_READY:path.resolve(args['--ledger-ready']),
  VISIBLE_FLEX_FROZEN_STORED_READY:path.resolve(args['--stored-ready']),
  VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT:'8',
  CLOSING_TAIL_CACHE:path.join(sourceTopic,'repro/source-root/topics/large-amplitude-twist-flex/scripts')
 });
 // This is the unmodified original factory, including its existing scalar
 // quadratures and any original auxiliary linear calibration/transfers.
 const original=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')).href);
 const {physical,factory,manifest}=await original.createStoredPhysical(config.value);
 const cutProfile=physical.cells[0].profiles.at(-1),cutG=cutProfile(1);
 const cut=finite(cutG.r,'cut radius'),cuff=finite(physical.parameters.rCuff,'cuff radius');
 insist(cuff>0&&cuff<cut,'Original finite selector needs its original positive ordered cuff/cut');
 if(plan){
  insist(manifest.profileFingerprintAfter===plan.value.profile_fingerprint,'Plan source fingerprint differs');
  insist(cut===plan.value.cut&&cuff===plan.value.cuff,'Plan closing anchors differ');
 }
 const pieces=[],pieceRows=[];
 for(let n=0;n<physical.cells.length;n++){
  const entries=factory.getEntries(n,config.value.valleyControls?.[n]??0).entries;
  for(let j=entries.length-1;j>=0;j--){
   const profile=physical.cells[n].profiles[j],outerG=profile(1),innerG=profile(0);
   const outer=outerG.r,inner=innerG.r,positive=outer>inner;
   const row={cell:n,segment:j,outer:word(outer),inner:word(inner),retained_by_original_outer_greater_inner:positive};
   if(positive){
    finite(outer,'piece outer radius');finite(inner,'piece inner radius');
    const piece={index:pieces.length,n,j,profile,profileCount:entries.length,outer,inner,
     outerQ:fromNumber(outer),innerQ:fromNumber(inner),outerG,innerG};
    piece.flat=explicitFlatOverride(piece,physical.parameters);
    pieces.push(piece);row.retained_index=piece.index;row.source_constant_rule=piece.flat;
   }
   pieceRows.push(row);
  }
 }
 const cuffQ=fromNumber(cuff),cutQ=fromNumber(cut);
 let queryRows;
 if(request){
  const q=request.value;
  insist(q.schema===QUERY_SCHEMA&&Array.isArray(q.queries)&&q.queries.length,'Exact closed query schema required');
  if(q.config_sha256!==undefined)insist(q.config_sha256===config.receipt.sha256,'Queries name another config');
  if(q.original_profile_fingerprint!==undefined)
   insist(q.original_profile_fingerprint===manifest.profileFingerprintAfter,'Queries name another source');
  queryRows=q.queries.map((q,i)=>({index:i,id:q.id??String(i),
   domain:interval(parseRational(q.left),parseRational(q.right))}));
 }else queryRows=[{index:0,id:'whole-original-cuff-to-cut',domain:interval(cuffQ,cutQ)}];
 for(const q of queryRows)insist(nonempty(q.domain)&&cmp(q.domain.a,cuffQ)>=0&&cmp(q.domain.b,cutQ)<=0,
  'A query is outside the original closed cuff/cut or has reversed endpoints');
 const queryPlan={schema:QUERY_SCHEMA,queries:queryRows.map(q=>({index:q.index,id:q.id,...showInterval(q.domain)}))};
 fs.writeFileSync(path.join(out,'query-plan.json'),canonical(queryPlan),{flag:'wx'});
 fs.writeFileSync(path.join(out,'source-piece-index.json'),canonical({rows:pieceRows,original_order:'n ascending, j descending; positive width only'}),{flag:'wx'});
 fs.writeFileSync(path.join(out,'original-geometry-manifest.json'),canonical(manifest),{flag:'wx'});
 const binding={schema:'original-stored-finite-background-selector-input-binding-v1',
  source_sha256:ownSHA,selector_source:sources['exact_20261114_closed_background.mjs'],sources,
  config:config.receipt,calibration_ledger:ledger.receipt,stored_reference:stored.receipt,
  optional_closed_plan:plan?.receipt??null,query_request:request?.receipt??null,
  original_profile_fingerprint:manifest.profileFingerprintAfter,
  source_revision:manifest.sourceRevision,cut:word(cut),cuff:word(cuff),
  original_geometry_manifest:receipt(path.join(out,'original-geometry-manifest.json'),out),
  original_selector_iterations:48,
  comparison_extension:'Real query radii compared to exact values of original binary64 thresholds; no continuous target identification',
  source_arithmetic_or_integrator_modified:false,
  global_continuous_g_identification_paid:false};
 fs.writeFileSync(path.join(out,'input-binding.json'),canonical(binding),{flag:'wx'});
 const leaves=logWriter(path.join(out,'large-arrays','selector-leaves.jsonl'));
 const unpaid=logWriter(path.join(out,'large-arrays','selector-unresolved.jsonl'));
 const decisions=logWriter(path.join(out,'large-arrays','selector-decisions.jsonl'));
 const results=[];
 const counters={selector_nodes:0,profile_threshold_calls:0,leaf_profile_calls:0,
  complete_leaf_regions:0,constant_source_regions:0,unresolved_regions:0,source_failures:0};
 let resourceStopped=false,firstUnvisitedQuery=null,allQueriesComplete=true;
 const exceeded=()=>counters.selector_nodes>=maxNodes||(performance.now()-start)/1000>=budgetSeconds;
 const statusTask=t=>({query_index:t.query.index,query_id:t.query.id,kind:t.kind,
  piece:t.piece?{index:t.piece.index,cell:t.piece.n,segment:t.piece.j}:null,
  domain:showInterval(t.domain),
  original_selector_state:t.kind==='tree'?{lo:word(t.lo),hi:word(t.hi),completed_steps:t.depth}:null});
 function unresolved(t,reason,extra={}){
  counters.unresolved_regions++;unpaid.add({...statusTask(t),reason,...extra});
 }
 function pay(t,g,kind,record={}){
  let v;
  if(kind==='explicit-cuff')v={w:word(0),E:word(1),logw:null};
  else v=originalE(g);
  const E=v.E.value;
  if(!(typeof E==='number'&&Number.isFinite(E)&&E>0))
   throw Error('Original selector returned a nonfinite or nonpositive E');
  const q=t.query;
  q.lower=q.lower===null?E:Math.min(q.lower,E);
  q.upper=q.upper===null?E:Math.max(q.upper,E);
  q.paid++;counters.complete_leaf_regions++;
  leaves.add({...statusTask(t),kind,original_point:g?{
   r:word(g.r),drdx:word(g.drdx),logw:word(g.logw),dlogwdx:word(g.dlogwdx)}:null,
   original_scalar_return:v,...record});
 }
 try{
  for(let qi=0;qi<queryRows.length;qi++){
   if(exceeded()){resourceStopped=true;firstUnvisitedQuery=qi;allQueriesComplete=false;break;}
   const row=queryRows[qi],query={...row,lower:null,upper:null,paid:0,unpaid:0};
   const owned=selectedParts(row.domain,pieces,cutQ,cuffQ);
   const tasks=owned.selected.map(t=>({...t,query})).reverse();
   for(const domain of owned.uncovered){
    const task={kind:'no-original-piece',query,domain};
    unresolved(task,'Original first-match selector has no positive-width source piece on this subdomain');
    query.unpaid++;
   }
   while(tasks.length){
    if(exceeded()){
     resourceStopped=true;allQueriesComplete=false;
     for(const t of tasks){unresolved(t,'Resource limit; original selector depth and arithmetic unchanged');query.unpaid++;}
     tasks.length=0;break;
    }
    const t=tasks.pop();
    try{
     if(t.kind==='cut'){pay(t,cutG,'explicit-cut');continue;}
     if(t.kind==='cuff'){pay(t,null,'explicit-cuff');continue;}
     const piece=t.piece;
     if(t.kind==='piece'){
      if(piece.flat){
       counters.constant_source_regions++;
       pay(t,piece.innerG,'proved-original-flat-assignment',{source_rule:piece.flat});continue;
      }
      let remaining=[t.domain];
      for(const [x,endpoint,g] of [[1,piece.outerQ,piece.outerG],[0,piece.innerQ,piece.innerG]]){
       const singleton=interval(endpoint,endpoint),next=[];
       for(const domain of remaining){
        const hit=intersection(domain,singleton);
        if(hit)pay({...t,domain:hit},g,'original-piece-exact-endpoint',{sourceX:word(x)});
        next.push(...subtract(domain,singleton));
       }
       remaining=next;
      }
      for(const domain of remaining.reverse())tasks.push({...t,kind:'tree',domain,lo:0,hi:1,depth:0});
      continue;
     }
     insist(t.kind==='tree','Unknown finite selector task');
     if(t.depth===48){
      const x=(t.lo+t.hi)/2;
      counters.leaf_profile_calls++;
      const g=piece.profile(x);
      pay(t,g,'original48-step-leaf',{sourceX:word(x),original_48_iterations_completed:true});
      continue;
     }
     counters.selector_nodes++;counters.profile_threshold_calls++;
     const mid=(t.lo+t.hi)/2,g=piece.profile(mid),value=g.r;
     decisions.add({...statusTask(t),sourceX:word(mid),original_radius_threshold:word(value),
      predicate:'original_radius_threshold < real query radius',
      true_branch_updates:'lo=mid',false_branch_updates:'hi=mid',
      strict_comparison_endpoint_belongs_to_false_branch:true});
     // NaN comparison is always false in the original source. No idealized
     // finite substitute or synthetic monotone bracket is introduced.
     if(Number.isNaN(value)||value===Infinity){
      tasks.push({...t,hi:mid,depth:t.depth+1});
     }else if(value===-Infinity){
      tasks.push({...t,lo:mid,depth:t.depth+1});
     }else{
      const threshold=fromNumber(value);
      const left=intersection(t.domain,interval(t.domain.a,threshold,t.domain.lc,true));
      const right=intersection(t.domain,interval(threshold,t.domain.b,false,t.domain.rc));
      // Push right then left solely for deterministic DFS order.
      if(right)tasks.push({...t,domain:right,lo:mid,depth:t.depth+1});
      if(left)tasks.push({...t,domain:left,hi:mid,depth:t.depth+1});
     }
    }catch(error){
     query.unpaid++;counters.source_failures++;
     unresolved(t,'Original point call or literal E readback failed',{error:String(error)});
    }
   }
   const complete=query.unpaid===0;
   allQueriesComplete&&=complete;
   results.push({query_index:qi,query_id:row.id,domain:showInterval(row.domain),complete,
    paid_regions:query.paid,unresolved_regions:query.unpaid,
    certified_finite_selector_E:complete&&query.lower!==null?{lower:word(query.lower),upper:word(query.upper)}:null,
    partial_visited_E_range:query.lower===null?null:{lower:word(query.lower),upper:word(query.upper)},
    continuous_original_g_bound_claimed:false});
   console.log(JSON.stringify({event:'original-finite-selector-query-readback',query_index:qi,
    complete,paid_regions:query.paid,unresolved_regions:query.unpaid,selector_nodes:counters.selector_nodes}));
   if(resourceStopped){firstUnvisitedQuery=qi+1<queryRows.length?qi+1:null;break;}
  }
 }finally{
  const leafLedger=leaves.finish(),unpaidLedger=unpaid.finish(),decisionLedger=decisions.finish();
  fs.writeFileSync(path.join(out,'query-results.json'),canonical({results}),{flag:'wx'});
  const report={schema:SCHEMA,source_sha256:ownSHA,run_id:process.env.GITHUB_RUN_ID??null,
   source_commit:process.env.GITHUB_SHA??null,
   runtime:{node:process.version,v8:process.versions.v8,platform:process.platform,arch:process.arch},
   input_binding:receipt(path.join(out,'input-binding.json'),out),
   query_plan:receipt(path.join(out,'query-plan.json'),out),
   source_piece_index:receipt(path.join(out,'source-piece-index.json'),out),
   query_results:receipt(path.join(out,'query-results.json'),out),
   leaf_ledger:{...leafLedger,file:'large-arrays/'+leafLedger.file},
   unresolved_ledger:{...unpaidLedger,file:'large-arrays/'+unpaidLedger.file},
   decision_ledger:{...decisionLedger,file:'large-arrays/'+decisionLedger.file},
   requested_queries:queryRows.length,returned_query_reports:results.length,
   first_unvisited_query:firstUnvisitedQuery,
   unvisited_query_suffix:firstUnvisitedQuery===null?null:{
    first:firstUnvisitedQuery,stop:queryRows.length,original_query_plan_preserved:true},
   counters,resource_stopped:resourceStopped,
   all_requested_closed_queries_completely_covered:allQueriesComplete&&results.length===queryRows.length,
   original_selector_depth:48,original_depth_or_scientific_gate_modified:false,
   budget:{seconds:budgetSeconds,max_selector_nodes:maxNodes},
   original_factory_reconstructed:true,
   original_factory_auxiliary_linear_calibrations_and_transfers_not_removed:true,
   nonlinear_tail_solve_called:false,new_shooting_state_or_224_column_J_called:false,
   original_factory_auxiliary_linear_and_calibration_variations_not_counted_as_zero:true,
   no_R26_real_integral_or_Bprime_substitution:true,
   only_original_numeric_selector_real_comparison_extension_certified:true,
   original_continuous_target_g_identification_or_enclosure_proved:false,
   C2_continuity_or_exact_inverse_or_monotonicity_proved:false,
   a601_missing_original_continuous_g_producer_discharged:false,
   actual_accepted_field_created:false,raw_outputs_temporary_and_recomputable:true,
   seconds:(performance.now()-start)/1000};
  fs.writeFileSync(path.join(out,'result.json'),canonical(report),{flag:'wx'});
  const raw=fs.readFileSync(path.join(out,'result.json'));
  console.log('BEGIN_ORIGINAL_STORED_FINITE_SELECTOR_SUMMARY');
  console.log(JSON.stringify(report));
  console.log('END_ORIGINAL_STORED_FINITE_SELECTOR_SUMMARY');
  console.log(JSON.stringify({event:'original-stored-finite-selector-result-sha256',
   bytes:raw.length,sha256:sha(raw),scope:'Actual result.json bytes, including final LF'}));
 }
 return {out,report:JSON.parse(fs.readFileSync(path.join(out,'result.json'),'utf8'))};
}

if(process.argv[1]&&path.resolve(process.argv[1])===ownFile){
 try{await runOriginalFiniteSelectorCover(argumentMap(process.argv.slice(2)));}
 catch(error){
  console.error(JSON.stringify({event:'original-stored-finite-selector-failure',error:String(error),
   original_native_science_not_modified:true,complete_cover_not_claimed:true}));
  process.exitCode=1;
 }
}
