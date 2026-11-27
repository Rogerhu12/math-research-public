#!/usr/bin/env node
/** Complete scalar-only observer integration from whole immutable sources.
 * The authored observer is a pinned complete stdlib-only input.
 * No Python, numerical calculation, fixture or scientific gate.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const INPUTS={
  "parents": {
    "driver": {
      "name": "fullclosed_fixed_fejer_stage_point_so3_qp.py",
      "bytes": 93158,
      "sha256": "050a6067fbb2fb4d054a97bf73899cfe5d4629197e42c39f00846a1f6a63b268",
      "git_blob_sha": "b0374f2db88ca38a936c7eadfc97f5377922c146"
    },
    "launcher": {
      "name": "launch_fixed_fejer_stage_point_actions.py",
      "bytes": 21785,
      "sha256": "8fed7b6a7ff6c988ee2240a4193f9440fd91ef158e5ac47d6248868d4e19214c",
      "git_blob_sha": "fed243876328a2933fcfb10288f6f42edda16211"
    },
    "reader": {
      "name": "read_fixed_fejer_stage_point_so3_report.py",
      "bytes": 97975,
      "sha256": "42e198f8d886641048059c3cdd8110b8bc3d000cdf350da1de54ac4bb83014a0",
      "git_blob_sha": "4304a1fdbe907bdb9c6708d7a89f5a18733ce15b"
    }
  },
  "helper": {
    "name": "fixed_fejer_actual_mathematical_progress.py",
    "bytes": 26595,
    "sha256": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
    "git_blob_sha": "509d502e13511c3746ba4647a6be32fce165bb61"
  }
};
const EXPECTED={
  "scalar_progress": {
    "name": "fixed_fejer_actual_mathematical_progress.py",
    "bytes": 26595,
    "sha256": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
    "git_blob_sha": "509d502e13511c3746ba4647a6be32fce165bb61"
  },
  "driver": {
    "name": "fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
    "bytes": 95632,
    "sha256": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
    "git_blob_sha": "3a537a58e82f152c78d0408c8b2c5f4403af1106"
  },
  "launcher": {
    "name": "launch_fixed_fejer_stage_point_observed_actions.py",
    "bytes": 21794,
    "sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
    "git_blob_sha": "1848230bd8a4f2dbbb4e4281e84d20d3d33ac531"
  },
  "reader": {
    "name": "read_fixed_fejer_stage_point_observed_so3_report.py",
    "bytes": 98763,
    "sha256": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
    "git_blob_sha": "f37f64e9da226b40cc836c1b5f139eec342db764"
  }
};
const hash=s=>({sha256:crypto.createHash('sha256').update(s,'utf8').digest('hex'),bytes:Buffer.byteLength(s,'utf8')});
function buildObservedEntry(parent,helper,hash){
 const all={},patches={};
 function rewrite(role,name,changes){
  let source=parent[role].text;const list=[];
  for(const[before,after,count=1]of changes){
   const n=source.split(before).length-1;if(n!==count)throw Error(role+' source occurrence '+n+' != '+count);
   source=source.split(before).join(after);list.push({before,after,count});
  }
  const value={role,name,text:source,...hash(source),parent:{name:parent[role].name,bytes:parent[role].bytes,
   sha256:parent[role].sha256,git_blob_sha:parent[role].git_blob_sha}};
  all[role]=value;patches[role]=list;return value;
 }
 const oldLine=parent.driver.text.match(/^SOURCE_PINS = .+$/m)[0];
 const pins=JSON.parse(oldLine.slice('SOURCE_PINS = '.length).replaceAll('(','[').replaceAll(')',']'));
 pins.scalar_progress=['scripts/resume_20261126/'+helper.name,helper.sha256];
 const newLine='SOURCE_PINS = {'+Object.entries(pins).map(([k,v])=>JSON.stringify(k)+':('+JSON.stringify(v[0])+','+JSON.stringify(v[1])+')').join(',')+'}';
 const setup=`    scalar_progress_module=load('_actual_fixed_fejer_mathematical_progress',paths['scalar_progress'])
    mathematical_progress=scalar_progress_module.Recorder(args.outdir/'actual-mathematical-progress.json',report)
    report.update(mathematical_progress_source=file_record(paths['scalar_progress']),
        mathematical_progress_definition=scalar_progress_module.definition(),
        actual_mathematical_observation=None)

    def observe_mathematical(event_name,value,point,*,phase=None,serial=None):
        try:
            digest_started=time.monotonic()
            actual_point_sha256=meridian.array_sha(point)
            digest_seconds=time.monotonic()-digest_started
            mathematical_progress.observe(event_name,value,point_sha256=actual_point_sha256,
                phase=phase,serial=serial,point_digest_seconds=digest_seconds)
        except Exception as error:
            mathematical_progress.failure(event_name,error)

`;
 const save=`        try:
            report['actual_mathematical_observation']=mathematical_progress.report_snapshot(report)
        except Exception as error:
            report['actual_mathematical_observation']=None
            mathematical_progress.failure('report-snapshot',error)
        write_json(output, report)
        try:
            mathematical_progress.report_saved(report)
        except Exception as error:
            mathematical_progress.failure('report-saved',error)
`;
 const oldSchema='complete-fixed-fejer-stage-point-material-envelope-SO3-QP-v1';
 const newSchema='complete-fixed-fejer-stage-point-observed-material-envelope-SO3-QP-v1';
 const driver=rewrite('driver','fullclosed_fixed_fejer_stage_point_observed_so3_qp.py',[
  [oldLine,newLine],[oldSchema,newSchema],
  ['    def save_report():',setup+'    def save_report():'],
  ['        write_json(output, report)\n',save],
  ['        current = statistics(x, native)\n',"        current = statistics(x, native)\n        observe_mathematical('initial-statistics-returned',current,x)\n"],
  ["        geometry = scan(x)\n        q.detached_closure_values.progress('initial-complete-geometry-returned',force=True)",
   "        geometry = scan(x)\n        observe_mathematical('initial-geometry-returned',geometry,x)\n        q.detached_closure_values.progress('initial-complete-geometry-returned',force=True)"],
  ['        geometry = scan(x)\n        feasible = geometric_feasible(geometry)',
   "        geometry = scan(x)\n        observe_mathematical('current-geometry-returned',geometry,x)\n        feasible = geometric_feasible(geometry)"],
  ['            trial_native, trial_statistics, trial_geometry = None, None, None',
   "            observe_mathematical('trial-start',trial,candidate,phase=phase,serial=record['serial'])\n            trial_native, trial_statistics, trial_geometry = None, None, None"],
  ['                trial_statistics = statistics(candidate, trial_native)',
   "                trial_statistics = statistics(candidate, trial_native)\n                observe_mathematical('trial-statistics-returned',trial_statistics,candidate,phase=phase,serial=record['serial'])"],
  ['                    trial_geometry = scan(candidate)',
   "                    trial_geometry = scan(candidate)\n                    observe_mathematical('trial-geometry-returned',trial_geometry,candidate,phase=phase,serial=record['serial'])"],
  ["            record['trials'].append(trial)",
   "            record['trials'].append(trial)\n            observe_mathematical('trial-decision-returned',trial,candidate,phase=phase,serial=record['serial'])"],
  ["                record['accepted_bundle'] = file_record(accepted_path)",
   "                record['accepted_bundle'] = file_record(accepted_path)\n                observe_mathematical('accepted-checkpoint-returned',record,x,phase=phase,serial=record['serial'])"],
  ['    geometry = scan(x)\n    current = statistics(x, q.residual(x))',
   "    geometry = scan(x)\n    observe_mathematical('final-geometry-returned',geometry,x)\n    current = statistics(x, q.residual(x))\n    observe_mathematical('final-statistics-returned',current,x)"]
 ]);
 rewrite('launcher','launch_fixed_fejer_stage_point_observed_actions.py',[
  [parent.driver.name,driver.name],[parent.driver.sha256,driver.sha256]]);
 const pure=`def mathematical_progress_binding(report,topic,driver):
    relative,expected=load_pins(driver)['scalar_progress']
    path=topic/relative
    if sha(path)!=expected or report.get('mathematical_progress_source',{}).get('sha256')!=expected:
        raise ValueError('Keep the whole explicitly declared standard-library scalar observer')
    name='_pure_fixed_fejer_mathematical_progress_'+expected[:16]
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module.validate_report_progress(report,source_sha256=expected,driver_sha256=DRIVER_SHA)


`;
 rewrite('reader','read_fixed_fejer_stage_point_observed_so3_report.py',[
  [parent.driver.name,driver.name],[parent.driver.sha256,driver.sha256],[oldSchema,newSchema],
  ['actual-fixed-fejer-stage-point-envelope-SO3-readout-v1','actual-fixed-fejer-stage-point-observed-envelope-SO3-readout-v1'],
  ['def read_report(repo, report_path, *, verify_final_bundle=False):',pure+'def read_report(repo, report_path, *, verify_final_bundle=False):'],
  ["        reader_sha256=sha(__file__), report_path=str(Path(report_path).resolve()),",
   "        mathematical_observation=mathematical_progress_binding(report,topic,driver),\n        reader_sha256=sha(__file__), report_path=str(Path(report_path).resolve()),"]
 ]);
 return {outputs:{scalar_progress:helper,...all},patches,pins,report_schema:newSchema};
}
function forwardAndInverse(parent,patches,expected){
 let text=parent;const trace=[];
 for(const p of patches){
  if(p.append!==undefined){trace.push({append:p.append,start:text.length});text+=p.append;continue;}
  if(!p.before)throw Error('A complete exact old source fragment is required');
  const positions=[];let cursor=0,at;while((at=text.indexOf(p.before,cursor))>=0){positions.push(at);cursor=at+p.before.length;}
  if(positions.length!==p.count)throw Error('Whole original patch multiplicity differs');
  const finalPositions=positions.map((x,j)=>x+j*(p.after.length-p.before.length));
  text=text.split(p.before).join(p.after);trace.push({before:p.before,after:p.after,positions:finalPositions});
 }
 if(text!==expected)throw Error('Whole forward source text differs');
 for(const p of trace.reverse()){
  if(p.append!==undefined){if(text.slice(p.start)!==p.append)throw Error('Appended complete source changed');text=text.slice(0,p.start);continue;}
  for(const at of p.positions.slice().reverse()){
   if(text.slice(at,at+p.after.length)!==p.after)throw Error('Exact inverse source fragment changed');
   text=text.slice(0,at)+p.before+text.slice(at+p.after.length);
  }
 }
 if(text!==parent)throw Error('Whole inverse original source differs');
 return true;
}
function readFull(directory,record){
 const raw=fs.readFileSync(path.join(directory,record.name)),text=raw.toString('utf8');
 if(!Buffer.from(text,'utf8').equals(raw)||raw.length!==record.bytes||hash(text).sha256!==record.sha256)
  throw Error('Keep the whole original source '+record.name);
 return {...record,text};
}
function main(argv){
 const options={};
 for(let i=0;i<argv.length;i+=2){
  if(!['--source-directory','--generated-directory'].includes(argv[i])||argv[i+1]===undefined||options[argv[i]])
   throw Error('Supply both whole directory options once');
  options[argv[i]]=path.resolve(argv[i+1]);
 }
 const directory=options['--source-directory'],out=options['--generated-directory'];
 if(!directory||!out||directory===out||out.startsWith(directory+path.sep)||fs.existsSync(out))
  throw Error('Keep the parent sources and choose a separate fresh output directory');
 const parents=Object.fromEntries(Object.entries(INPUTS.parents).map(([role,r])=>[role,readFull(directory,r)]));
 const helper=readFull(directory,INPUTS.helper),result=buildObservedEntry(parents,helper,hash);
 if(Object.keys(result.pins).length!==120)throw Error('Keep the complete original 119 roles and explicit scalar observer');
 for(const[role,item]of Object.entries(result.outputs)){
  const wanted=EXPECTED[role];
  if(item.name!==wanted.name||item.bytes!==wanted.bytes||item.sha256!==wanted.sha256||item.bytes>=100000)
   throw Error('Whole observed source changed: '+role);
  if(role!=='scalar_progress')forwardAndInverse(parents[role].text,result.patches[role],item.text);
 }
 for(const r of Object.values(INPUTS.parents))readFull(directory,r);readFull(directory,INPUTS.helper);
 fs.mkdirSync(out,{recursive:true});
 for(const item of Object.values(result.outputs))fs.writeFileSync(path.join(out,item.name),item.text,{encoding:'utf8',flag:'wx'});
 console.log(JSON.stringify({complete:true,whole_runtime_sources:4,whole_source_roles:120,
  original_arithmetic_and_scientific_call_order_retained:true,
  new_field_J_or_root_calls:0,all_three_forward_and_inverse_source_texts_match:true,
  local_Python_AST_or_compile:false,scientific_execution:false,source_reproduction_is_not_an_admission_gate:true}));
}
if(path.resolve(process.argv[1]||'')===fileURLToPath(import.meta.url))main(process.argv.slice(2));
