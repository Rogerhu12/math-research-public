#!/usr/bin/env node
/** Reproduce complete text inputs from pinned whole Git files. No numerical work. */
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {readFileSync, mkdirSync, writeFileSync} from 'node:fs';
import {resolve, dirname, sep} from 'node:path';

function identity(path, body) {
  const bytes=Buffer.byteLength(body,'utf8');
  const hash=(algorithm,value)=>createHash(algorithm).update(value,'utf8').digest('hex');
  return {path,bytes,sha256:hash('sha256',body),git_blob_sha:hash('sha1','blob '+bytes+'\0'+body)};
}
function equal(record,body) {
  const value=identity(record.path,body);
  return ['bytes','sha256','git_blob_sha'].every(key=>value[key]===record[key]);
}
function readWhole(root,record) {
  let body;
  try { body=readFileSync(resolve(root,record.path),'utf8'); } catch {}
  if(typeof body!=='string'||!equal(record,body))
    body=execFileSync('git',['-C',root,'cat-file','blob',record.git_blob_sha],{encoding:'utf8',maxBuffer:256000});
  if(!equal(record,body)) throw Error('Whole source identity differs: '+record.path);
  return body;
}

const records={
  "request": {
    "role": "request",
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-33.json",
    "bytes": 41482,
    "sha256": "5037da8272a0490f554fd4ca7fad288e95f514e598f248d1d0033be686e0636e",
    "git_blob_sha": "4d3d8753a571febbe98f7d95f3717406a1febf27"
  },
  "queue": {
    "role": "queue",
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-33.json",
    "bytes": 80264,
    "sha256": "230b6ab4a1c2dbf43edc522d466f4fa30d9571d880a38a3f9287204c5043f480",
    "git_blob_sha": "55458eecbdd30c6ad4bfc3ae3f2b425ae5b3154f"
  },
  "science": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-bhalf-science-complete-ready.json",
    "bytes": 80928,
    "sha256": "d35579f13e07cf004a333905af411c0a47f2147f42c574b9b0c65af7b02b1798",
    "git_blob_sha": "8631722f6367d98f4515adce383f49226f69c3cd"
  },
  "pure": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-bhalf-pure-complete-ready.json",
    "bytes": 70074,
    "sha256": "19e226f138e2076dc2834f7b3a2449eef633961c4a80159e5933c7f0fa0e290a",
    "git_blob_sha": "86116e5b0605b3fc5d24cf8b998695bf65939401"
  }
};
const settings={
  "when": "2026-11-28 10:02:21 UTC",
  "requestID": "visible-larger-resume-20261128-33-retry-section16",
  "publication": "3ff5795e46cc5a2b50f0ba27d6c747a00bc54d03",
  "rulesReadCommit": "60e476a228cda7c9d485fd220d0507e58a4b2e2a",
  "ruleRecords": [
    {
      "path": "README.md",
      "bytes": 10649,
      "sha256": "539f1ea02feb8a63c5aa734ed560ab6ecbf3ff7f570212e46788413bb072f444",
      "git_blob_sha": "99c5ad8d06e939e6cfbbab1afdeffa5463f15f18",
      "fixed_commit": "60e476a228cda7c9d485fd220d0507e58a4b2e2a"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/README.md",
      "bytes": 2664,
      "sha256": "3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d",
      "git_blob_sha": "bff8aea253a9e6a7a4fac28d810ac454c5499fec",
      "fixed_commit": "60e476a228cda7c9d485fd220d0507e58a4b2e2a"
    }
  ],
  "failure": {
    "official_run_id": "46130690181",
    "official_attempt": 1,
    "official_job_id": "140934949073",
    "official_job_conclusion": "failure",
    "official_step_five_conclusion": "failure",
    "research_step_ended_utc": "2026-11-28T09:38:54Z",
    "official_job_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46130690181/job/140934949073",
    "original_job_log": {
      "bytes": 64705,
      "sha256": "ad490cac7f23076de59607b79514f6a2df58009836c9bc73cc3b55c02b6c06ac",
      "evidence": "Complete original job log read by the research coordinator. Only compact execution metadata enters this package."
    },
    "original_index_and_first_input_volume": [
      {
        "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46130690181-1-part-001.md",
        "bytes": 5756,
        "sha256": "466eff9ea7e6262c86fb827fcfd09c21dcefca91c1e3887470e570eafdbefe18",
        "git_blob_sha": "a9c146a0cbef11f78d0c839e7f93786c84ea2ddc",
        "fixed_commit": "56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb"
      },
      {
        "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46130690181-1.md",
        "bytes": 49260,
        "sha256": "9b71dd2ce4e34a11d037fb2d30be45815602169f76c9475881d138e88bfedc01",
        "git_blob_sha": "002947e90bbcec8332dd5db5e20238abcefd799a",
        "fixed_commit": "56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb"
      }
    ],
    "two_original_inputs_returned_zero": true,
    "published_original_index_records_one_input": true,
    "original_second_input": {
      "state": "completed",
      "returncode": 0,
      "event_utc": "2026-11-28T09:38:53.3589567Z",
      "seconds": 499.935978069,
      "source_commit": "77b0048525a4ae51aad18ab36dc64f5ec849b44a",
      "pid": 2969,
      "source_sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      "report": {
        "bytes": 84971,
        "sha256": "c2ac7be69f718960b53a3f8c887ab54d619d517cb1dfb66cfdd58451dab0b423"
      },
      "evidence": "The full original job log recorded followup_returned before its finish_record publication was interrupted."
    },
    "stopped_at": "Publisher.sync after an ordinary pull during publication of the second input finish_record",
    "cause": "The root README gained section 16. The original controller raised its existing exception on the current diff.",
    "exact_original_error": "README changed: the research agent must read this exact diff before further computation/publication",
    "new_rule_acknowledgment_commit": "f57995b11d7b9e390d61a6f363cdf50bf5febc43",
    "old_science_started": false,
    "old_scientific_report_or_final": null,
    "second_input_report_used_as_current_input": false
  }
};
const expected={
  "request": {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-33.json",
    "bytes": 45113,
    "sha256": "3cf46b086e19b5a711ebec118b037a08b8a065db4750700e574f2066bb25a51b",
    "git_blob_sha": "01a54493aa65c133fadffc98090eb3a1832b8727"
  },
  "queue": {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-33.json",
    "bytes": 80280,
    "sha256": "7a385ee75986b6693fdf354a6288000eb583a63d95eaaefd654ddd65365b61f0",
    "git_blob_sha": "de659fd7787046fea517e0579da6db86fcec9aeb"
  }
};

function buildRetry(input,records,settings,identity) {
  const wire=x=>JSON.stringify(x)+'\n';
  const whole=(complete_file,json_pointer='')=>({complete_file,json_pointer,whole_file_required:true});
  const q={...input.queue,parent_request_id:settings.requestID};
  const original=input.request;
  const r={...original};
  r.request_id=settings.requestID;r.created_utc=settings.when;r.rules_read_commit=settings.rulesReadCommit;
  r.rules_sha256=Object.fromEntries(settings.ruleRecords.map(x=>[x.path,x.sha256]));
  r.rules_read_method='The complete current README blobs were read and their identities compared to the two files at the named commit, including root rule 16. The complete original controller still performs its ordinary pull, diff and rule checks before publication and on its full original schedule.';
  r.complete_launch_rules_records=settings.ruleRecords;
  r.source_and_parameter_scope=original.source_and_parameter_scope.replace('New33 source/parameter publication is unknown at preparation, and all required new files must be published with or before this request.','The whole original publication is '+settings.publication+'. Its complete current science, pure and all pinned source and parameter references are retained in the source and parameter deliveries.');
  const fresh=identity(records.queue.path,wire(q));
  const pureQueue=steps=>wire({parent_request_id:settings.requestID,finish_when_done:false,steps});
  const deferred=identity(records.queue.path,pureQueue(input.pure.steps));
  r.queue_capacity_policy={...original.queue_capacity_policy,initial_queue:fresh,initial_queue_bytes:fresh.bytes,
    science_plus_pure_two_step_queue_bytes:identity(records.queue.path,pureQueue([...input.science.steps,...input.pure.steps])).bytes,
    all_four_step_queue_bytes:identity(records.queue.path,pureQueue([...q.steps,...input.pure.steps])).bytes,
    pure_only_queue_bytes:deferred.bytes,pure_only_queue:deferred};
  r.original_complete_launch_request=whole(records.request);
  r.all_original_launch_request_metadata_preserved_in_full={...whole(records.request),all_original_keys_and_values_preserved:true};
  r.current_scientific_source_and_parameter_publications={...original.current_scientific_source_and_parameter_publications,
    source:settings.publication,parameters:settings.publication,scope:'This ordinary commit contains the complete original run33 source, parameters and launch packages. The new official retry run and its execution source checkout are unknown until actual execution.'};
  r.complete_current_launch_source_and_inputs={...original.complete_current_launch_source_and_inputs,published_scientific_source_commit:settings.publication};
  r.original_request_key_count=Object.keys(original).length;
  r.retry_scope={original33_request:whole(records.request),original33_queue:whole(records.queue),complete_original_retry_history:whole(records.request,'/retry_scope'),
    earlier_real_run:settings.failure,current_request:settings.requestID,ordinary_retry_with_fresh_GitHub_run_and_runner:true,
    complete_original_input_steps_and_science_step_copied_literally:true,source_parameters_and_physical_family_unchanged:true,
    original_GitHub_run_or_job_rerun_in_place:false,previous_runner_files_or_final_used:false,both_input_steps_repeat_on_fresh_runner:true,
    new_run_id:null,new_attempt:null,new_actual_child_source_commit:null,new_input_hashes:null,new_actual_model:null,new_actual_point:null,new_actual_report:null,new_typed_history:null,new_final_bundle:null,new_geometry_certificate:null};
  r.complete_original_terminal_and_failure_histories={...original.complete_original_terminal_and_failure_histories,original33_failure_record_in_this_request:'/retry_scope/earlier_real_run',whole_original33_request:whole(records.request)};
  r.current_complete_request_key_count=Object.keys(r).length;
  return {queue:wire(q),request:wire(r)};
}

const argv=process.argv.slice(2);
if(argv.length!==4||argv[0]!=='--source-repository'||argv[2]!=='--output-repository')
  throw Error('Use --source-repository ROOT --output-repository OUTPUT');
const root=resolve(argv[1]), output=resolve(argv[3]), input={};
for(const [key,record] of Object.entries(records)){
  const source=readWhole(root,record);
  input[key]=record.path.endsWith('.json')?JSON.parse(source):source;
}
const files=buildRetry(input,records,settings,identity);
for(const [key,body] of Object.entries(files)){
  if(!expected[key]||!equal(expected[key],body)) throw Error('Regenerated complete text differs: '+key);
  const path=resolve(output,expected[key].path);
  if(!path.startsWith(output+sep)) throw Error('Expected an output inside the indicated repository');
  mkdirSync(dirname(path),{recursive:true});
  writeFileSync(path,body,{encoding:'utf8'});
}
console.log(JSON.stringify(expected,null,2));
