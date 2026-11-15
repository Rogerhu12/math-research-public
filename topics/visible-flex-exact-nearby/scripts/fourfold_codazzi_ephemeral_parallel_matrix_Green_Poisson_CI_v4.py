#!/usr/bin/env python3
"""One ephemeral public run: exact old inputs, three streams, complete contraction.

Only script/parameter/run/output-hash receipts and true small conclusions
are committed. No new numerical array, native output, stdout archive or
Actions artifact is uploaded. Missing immutable old pins are restored
from one explicitly fixed pre-deletion public commit into scratch only.
"""
from __future__ import annotations
import argparse,hashlib,importlib.metadata,json,os,re,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request
from pathlib import Path
import fourfold_codazzi_complete_directional_matrix_Green_CI as original
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO,save,now

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_ephemeral_parallel_matrix_Green_Poisson_v4.py'
FOLDER='notes/ephemeral_parallel_matrix_Green_Poisson_v4_ci'
KIND='actual_ephemeral_parallel_finite193_Green_true97_Poisson_same97_cap_v4'
WORKER_KIND='actual_public_ephemeral_parallel_matrix_Green_Poisson_process_v4'
MANIFEST_KIND='ephemeral_parallel_matrix_Green_Poisson_public_inputs_v4'
OLD_MANIFEST=REL+'notes/2026-11-15-R133-complete-same97-cap-posterior-Poisson-CI-inputs.json'
OLD_MANIFEST_SHA='7473f7866cc7676124f0f95ce047b6316ec5a4156bed8452f3cbd1bfb257ae95'
PREDELETE='7c130fb94528de8f003a43e7049fb42768a64eec'
RULES=('README.md',REL+'README.md')
RULES_SHA='65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1'
LIVE_RULES=REL+'notes/2026-11-15-R133-live-reviewed-public-CI-rules-index.json'
V3_RECEIPT=REL+'notes/ephemeral_matrix_Green_stopped_log_diagnostic_ci/run-43709951426-1/execution.json'
V3_RECEIPT_SHA='f526d0b17bc9ac74e167ba612d4911a7bcc526cfe2d7fa7b784eb893ddf8000a'
V3_SOURCE='1d8383a8531b9120b25f0ce132e33fc858afdaa53be26bf0bfade385e6a70784'
REPOSITORY='Rogerhu12/math-research-public'
BACK_RUN='43672023585'
BACK_NAME='visible-exact-directional-matrix-Green-backward-43672023585-1'
BACK_ID=14146873569
BACK_ZIP='de4e8dbdde0e34f6cfbd00b643ed70544ddc55d5852e1654a400ec8d3eaf3773'
CAP_RUN='43671537267'
CAP_NAME='visible-exact-same97-cap-posterior-cap-43671537267-1'
CAP_ID=14144516627
CAP_ZIP='b8809594d2efeba92b510c1c78ba4b8155b62514f60475c806e2bf10ceae7957'
CAP_NATIVE='56efa27c6410caed656eb7e691de49283dfbd34d60e5b2c23c516b932c72dd99'
CAP_ARRAY='c500a1a96ae6eca76de7447effe225e0a11621b06090e2fbf2dce7ef325c3ec0'
LABEL='actual_ephemeral_missing_future_past_true97_Poisson_and_same97_contraction'
SOURCE_KEYS=('matrix-data','matrix-process','profile','profile-process','green','green-process',
    'kernel','kernel-process','impulse','impulse-process','reviewed-impulse-process',
    'boundary','nominal-cut')
WINDOWS=('whole_inner_body','fixed_complete_negative_phase_window','true_cut_trace')
PRIOR_DIR=REL+'notes/ephemeral_parallel_matrix_Green_Poisson_v2_ci/run-43681612825-1-ephemeral-parallel-matrix-Green-Poisson-v2/'
PRIOR_PROCESS=PRIOR_DIR+'process.json'
PRIOR_SUMMARY=PRIOR_DIR+'actual-conclusion-summary.json'
PRIOR_PROCESS_SHA='0b2e08152feee47b47666e2bc03a1b3e535e2389891e26a0674014d3a2fef4ba'
PRIOR_SUMMARY_SHA='770a61fa89902954178cf1a2bb9a347312232545e434685f9e332a2ce149b8db'
PRIOR_SOURCE='f33345d1ab2500fd3811692311ce931606e389cf3c8ef508925d225748565190'
PRIOR_COUNTS=dict(future=4226,past=1800,product=4331,ports=5970,groups=0)



def small(path,document):
    raw=(json.dumps(document,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode()
    if len(raw)>60000:raise ValueError('a genuine small conclusion exceeds60000 bytes; do not split its full data')
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.tmp');temporary.write_bytes(raw);os.replace(temporary,path)


def safe_relative(name):
    p=Path(name)
    if p.is_absolute() or '..' in p.parts or not name.startswith(REL):
        raise ValueError('only an exact topic-relative immutable input is authorized')
    return p



def readme_receipt(check):
    # The complete original process is an immutable input, not republished
    # data. Preserve the exact difference identity and its actual timing.
    result={k:v for k,v in check.items() if k!='actual_diff'}
    raw=check.get('actual_diff','').encode()
    result['actual_diff_bytes']=len(raw)
    result['actual_diff_sha256']=hashlib.sha256(raw).hexdigest()
    return result


def archive_receipt(receipt):
    # This is a genuine provenance summary, not an encoded/split archive.
    return dict(run_id=receipt['run_id'],run_attempt=receipt['run_attempt'],
        artifact_name=receipt['artifact_name'],artifact_id=receipt['artifact_id'],
        original_zip_bytes=receipt['exact_downloaded_archive']['bytes'],
        original_zip_sha256=receipt['exact_downloaded_archive']['sha256'],
        actual_process_sha256=receipt.get('actual_process_sha256'))


def topic_tree_metadata(git,topic,repository):
    """Read the exact published origin/main tree; never request an unpublished local HEAD or a blob body."""
    head=git("rev-parse","origin/main").stdout.strip()
    def oid(value):
        return isinstance(value,str) and len(value)==40 and all(c in "0123456789abcdef" for c in value)
    if not oid(head):raise ValueError("the capacity audit requires an exact Git commit")
    root_tree=git("rev-parse",head+"^{tree}").stdout.strip()
    local_topic_tree=git("rev-parse",head+":"+str(topic)).stdout.strip()
    if not oid(root_tree) or not oid(local_topic_tree):
        raise ValueError("the capacity audit requires complete local commit and tree identities")
    token=os.environ.get("GITHUB_TOKEN")
    if not token:raise RuntimeError("the public metadata request requires its Actions token")
    responses=[]
    class NoMetadataRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,request,fp,code,message,headers,newurl):
            raise RuntimeError("the capacity metadata endpoint attempted a redirect")
    opener=urllib.request.build_opener(NoMetadataRedirect())
    def request_tree(tree,recursive=False):
        url="https://api.github.com/repos/"+repository+"/git/trees/"+tree
        if recursive:url+="?recursive=1"
        request=urllib.request.Request(url,headers={
            "Accept":"application/vnd.github+json",
            "X-GitHub-Api-Version":"2022-11-28",
            "Authorization":"Bearer "+token})
        try:
            with opener.open(request,timeout=45) as response:
                if response.geturl()!=url:
                    raise RuntimeError("the capacity metadata request was redirected")
                data=response.read(16000001)
        except urllib.error.HTTPError as error:
            raise RuntimeError("the Git tree metadata request returned HTTP "+str(error.code)) from None
        except urllib.error.URLError:
            raise RuntimeError("the Git tree metadata request failed at transport") from None
        if len(data)>16000000:raise ValueError("the Git tree metadata response exceeded its bounded size")
        doc=json.loads(data)
        if doc.get("sha")!=tree or doc.get("truncated") is not False or not isinstance(doc.get("tree"),list):
            raise ValueError("a Git tree metadata identity or complete-response gate failed")
        responses.append(dict(tree=tree,recursive=recursive,bytes=len(data),
            sha256=hashlib.sha256(data).hexdigest(),truncated=False))
        return doc["tree"]
    # Freeze the public origin/main commit before resolving its topic components.
    # Compare with Git's independent commit:topic identity; API URLs contain only exact object IDs.
    tree=root_tree
    for component in topic.parts:
        entries=request_tree(tree)
        matches=[entry for entry in entries if entry.get("path")==component]
        if len(matches)!=1 or matches[0].get("type")!="tree" or matches[0].get("mode")!="040000":
            raise ValueError("the authorized topic is not an exact tree at this commit")
        tree=matches[0].get("sha")
        if not oid(tree):raise ValueError("the topic path contains an invalid Git tree identity")
    if tree!=local_topic_tree:
        raise ValueError("the API and local published-commit topic tree identities differ")
    entries=request_tree(tree,recursive=True)
    seen=set();blobs={};inventory=[];trees=0;gitlinks=0
    for entry in entries:
        path=entry.get("path")
        if (not isinstance(path,str) or not path or path.startswith("/")
            or any(part in ("",".","..") for part in path.split("/")) or path in seen):
            raise ValueError("the complete topic tree contains an invalid or duplicate path")
        seen.add(path)
        kind=entry.get("type");mode=entry.get("mode");digest=entry.get("sha")
        if not oid(digest):raise ValueError("a topic object has an invalid Git identity")
        if kind=="blob":
            size=entry.get("size")
            if type(size) is not int or size<0 or mode not in ("100644","100755","120000"):
                raise ValueError("a topic blob has no exact nonnegative metadata size or valid mode")
            full=str(topic)+"/"+path
            blobs[full]=dict(bytes=size,git_blob=digest,mode=mode)
            inventory.append(dict(path=full,bytes=size,git_blob=digest,mode=mode))
        elif kind=="tree":
            if mode!="040000":raise ValueError("a nested topic tree has the wrong mode")
            trees+=1
        elif kind=="commit":
            if mode!="160000":raise ValueError("a topic Git link has the wrong mode")
            gitlinks+=1
        else:raise ValueError("the complete topic tree has an unsupported entry type")
    inventory.sort(key=lambda entry:entry["path"])
    receipt=dict(method="published_origin_main_Git_Trees_API_metadata_only",commit=head,
        root_tree=root_tree,topic=str(topic),topic_tree=tree,
        truncated=False,all_blob_sizes_checked=True,blob_count=len(blobs),
        blob_bytes=sum(entry["bytes"] for entry in blobs.values()),
        nested_tree_count=trees,gitlink_count=gitlinks,
        complete_blob_metadata_inventory_sha256=hashlib.sha256(
            json.dumps(inventory,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest(),
        metadata_responses=responses,blob_bodies_requested=False)
    return receipt,blobs

def owned_head_delta(git,root,capacity,blob_map,allowed_paths,topic):
    """Audit local unpushed report blobs without querying their unpublished Git tree through the API."""
    base=capacity["commit"];head=git("rev-parse","HEAD").stdout.strip()
    raw=git("diff","--name-status","--no-renames","-z",base,head,"--",str(topic)).stdout
    fields=raw.split("\0")
    if fields[-1:]!=[""]:raise ValueError("the complete local topic delta lacks its terminator")
    fields=fields[:-1]
    if len(fields)%2:raise ValueError("the local topic delta is not an exact name-status list")
    total=capacity["blob_bytes"];count=capacity["blob_count"];changes=[]
    for status,name in zip(fields[0::2],fields[1::2]):
        if name not in allowed_paths or status not in ("A","M","D"):
            raise ValueError("an unpublished local topic change is outside the two owned small conclusions")
        before=blob_map.get(name)
        if status=="A" and before is not None:raise ValueError("an added owned path already exists in the published base")
        if status in ("M","D") and before is None:raise ValueError("a changed owned path is absent from the published base")
        oldbytes=0 if before is None else before["bytes"]
        total-=oldbytes;count-=int(before is not None)
        change=dict(path=name,status=status,published_bytes=oldbytes,
            published_git_blob=None if before is None else before["git_blob"])
        if status!="D":
            line=git("ls-tree","-z",head,"--",name).stdout
            if not line.endswith("\0") or line.count("\0")!=1:
                raise ValueError("the owned HEAD path is not one exact Git entry")
            header,path=line[:-1].split("\t",1);mode,kind,digest=header.split()
            if path!=name or mode!="100644" or kind!="blob" or len(digest)!=40:
                raise ValueError("the owned HEAD conclusion is not a regular text blob")
            body=git("show",head+":"+name).stdout.encode()
            if len(body)>60000:raise ValueError("an owned HEAD conclusion exceeds the small-text limit")
            calculated=hashlib.sha1(b"blob "+str(len(body)).encode()+b"\0"+body).hexdigest()
            if calculated!=digest:raise ValueError("the exact owned HEAD bytes do not match their Git blob")
            total+=len(body);count+=1
            change.update(head_bytes=len(body),head_git_blob=digest,head_sha256=hashlib.sha256(body).hexdigest())
        changes.append(change)
    return dict(method="published_origin_main_API_plus_exact_owned_HEAD_delta",commit=head,
        published_base_commit=base,published_base_topic_tree=capacity["topic_tree"],
        head_topic_tree=git("rev-parse",head+":"+str(topic)).stdout.strip(),
        blob_bytes=total,blob_count=count,owned_local_delta=changes,
        original_complete_base_metadata_inventory_sha256=capacity["complete_blob_metadata_inventory_sha256"],
        exact_owned_paths_only=True,unpublished_tree_requested_from_API=False)


class EphemeralWorker(original.MatrixGreenWorker):
    def __init__(self,a):
        super().__init__(a)
        self.name=f'run-{self.run_label}-ephemeral-parallel-matrix-Green-Poisson-v4'
        self.dest=TOPIC/FOLDER/self.name
        self.temp=self.work/'ephemeral-mathematics'
        self.final_native=self.work/'ephemeral-complete-Green-Poisson-cap.json.gz'
        self.hydrated=False;self.history_ready=False;self.summary=None
        self.source_receipts=[]
        self.initial_review=read(a.rules)
        self.accepted_rule_cache={}
        self.final_receipts_captured=False
        self.last_stdout_receipt=None
        self.state.update(kind=WORKER_KIND,worker_source_sha256=digest(__file__),
            phase='one_ephemeral_complete_consumer',
            historical_restore_commit=PREDELETE,
            new_recomputable_repository_data=False,new_Release_uploads=False,new_Actions_artifacts=False,
            actual_original_backwards_run=BACK_RUN,actual_original_cap_run=CAP_RUN,
            original_complete_scientific_rows_recomputed=0,new_arithmetic_bits=a.bits,
            maximum_compute_processes=4,actual_available_cpu_count=os.cpu_count(),conclusion_scope='finite193 and true97 Poisson; full high inverse remains separate')
        self.state.pop('new_array_storage',None)
        self.state['new_product_error_method']='full signed output-side Gram; all positive weights and Gram scales are exact arbitrary-exponent dyadics'

    def git_text(self,*args):
        return self.git(list(args)).stdout

    def accept_live_review(self):
        """Operational review can advance; the immutable mathematical closure cannot."""
        raw=self.git_text('show','HEAD:'+LIVE_RULES)
        if len(raw.encode())>60000:raise ValueError('the independent live review index is not small text')
        index=json.loads(raw);policy=self.initial_review.get('large_data_policy')
        if (index.get('kind')!='explicit_live_review_index_for_unchanged_public_execution_rules'
            or index.get('repository')!=REPOSITORY
            or index.get('execution_policy')!=policy
            or index.get('new_or_changed_operational_rules_require_new_worker_review') is not True
            or index.get('unread_README_revisions_are_not_accepted') is not True):
            raise ValueError('the independent live review index changes the original execution policy')
        entries=index.get('accepted_reviews')
        if not isinstance(entries,list) or not entries or len(entries)>128:
            raise ValueError('a finite explicit list of separately read rule versions is required')
        actual={p:digest(REPO/p) for p in RULES}
        matches=[e for e in entries if e.get('readme_sha256')==actual]
        if len(matches)!=1:
            raise RuntimeError('current README bytes have no unique explicit unchanged-operational-rules review')
        entry=matches[0];name=str(safe_relative(entry.get('path','')))
        expected=entry.get('sha256');commit=entry.get('read_commit')
        if (not re.fullmatch('[0-9a-f]{64}',str(expected))
            or not re.fullmatch('[0-9a-f]{40}',str(commit))
            or type(entry.get('bytes')) is not int or not 0<entry['bytes']<=60000
            or entry.get('all_operational_rules_unchanged') is not True
            or entry.get('scientific_input_manifests_and_sources_not_changed') is not True):
            raise ValueError('a new rule review must expressly preserve all operational instructions and science')
        body=self.git_text('show','HEAD:'+name).encode()
        if len(body)!=entry['bytes'] or hashlib.sha256(body).hexdigest()!=expected:
            raise ValueError('the exact separately read live rules record changed')
        review=json.loads(body)
        if (review.get('kind')!='explicitly_read_public_repository_rules_for_existing_CI'
            or review.get('repository')!=REPOSITORY or review.get('read_commit')!=commit
            or review.get('readme_sha256')!=actual or review.get('large_data_policy')!=policy
            or review.get('scientific_input_manifests_and_sources_not_changed') is not True
            or review.get('new_unread_rules_must_still_be_reported_and_applied') is not True):
            raise ValueError('the live rules receipt does not preserve the exact reviewed execution policy')
        # A statement alone is insufficient: independently read the two historical
        # README objects at the stated immutable review commit and verify their bytes.
        if expected not in self.accepted_rule_cache:
            if self.git(['cat-file','-e',commit+'^{commit}'],check=False).returncode:
                self.git(['fetch','--filter=blob:none','--no-tags','--depth=1','origin',commit])
            checked={p:hashlib.sha256(self.git_text('show',commit+':'+p).encode()).hexdigest()
                for p in RULES}
            if checked!=actual:raise ValueError('the claimed review commit contains different README bytes')
            self.accepted_rule_cache[expected]=dict(path=name,bytes=len(body),sha256=expected,
                read_commit=commit,readme_sha256=actual,
                actual_review_commit_README_bytes_verified=True,
                all_operational_rules_unchanged=True)
        self.reviewed=review
        self.state.update(reviewed_rules_sha256=expected,explicit_readme_review_commit=commit,
            actual_reviewed_readme_sha256=actual,
            live_review_index=dict(path=LIVE_RULES,bytes=len(raw.encode()),
                sha256=hashlib.sha256(raw.encode()).hexdigest(),
                observed_at_commit=self.git_text('rev-parse','HEAD').strip()),
            accepted_live_rule_versions=list(self.accepted_rule_cache.values()),
            original_initial_rules_sha256=self.args.rules_sha)
        return actual

    def capacity_gate(self):
        # Exact metadata only. Use published origin/main, never an unpublished
        # local tree API URL and never ls-tree -l on a partial clone.
        git=lambda *args,**kw:self.git(list(args),**kw)
        topic=Path(REL.rstrip('/'))
        public,blobs=topic_tree_metadata(git,topic,REPOSITORY)
        owned={str((self.dest/name).relative_to(REPO))
            for name in ('process.json','actual-conclusion-summary.json')}
        current=owned_head_delta(git,REPO,public,blobs,owned,topic)
        reserve=120000
        self.state.update(actual_published_topic_capacity=public,
            actual_local_topic_capacity=current,
            required_small_conclusion_reserve_bytes=reserve)
        if current['blob_bytes']+reserve>200000000:
            raise RuntimeError('actual topic capacity lacks the120000-byte reserve for two small conclusions')
        return current

    def sync(self):
        owned=str(self.dest.relative_to(REPO))
        changed=set(self.git(['diff','--name-only']).stdout.splitlines())
        changed.update(self.git(['diff','--cached','--name-only']).stdout.splitlines())
        if any(p!=owned and not p.startswith(owned+'/') for p in changed):
            raise RuntimeError('unexpected changes outside this job report; preserve them')
        if changed:
            self.git(['add','--sparse','--',owned])
            if self.git(['diff','--cached','--quiet'],check=False).returncode:
                self.git(['commit','-m','visible-exact: preserve actual ephemeral evidence before rebase'])
        before=self.read_commit or self.git_text('rev-parse','HEAD').strip()
        self.git(['pull','--rebase','origin','main'])
        after=self.git_text('rev-parse','HEAD').strip()
        difference=self.git_text('diff',before,after,'--',*RULES)
        check=dict(time=now(),before=before,after=after,changed=bool(difference),
            actual_diff=difference,separately_read_rules_commit=self.reviewed['read_commit'])
        self.state['readme_checks'].append(check)
        if difference:print('ACTUAL_README_DIFF_CHECKED_AGAINST_LIVE_EXPLICIT_REVIEW\n'+difference,flush=True)
        self.check_inputs()
        check.update(separately_read_rules_commit=self.reviewed['read_commit'],
            accepted_review_sha256=self.state['reviewed_rules_sha256'],
            live_review_index_sha256=self.state['live_review_index']['sha256'])
        self.capacity_gate()
        self.read_commit=after;self.state['last_read_commit']=after

    def publish(self,final=False):
        self.emit_small_stdout('before_final_publication' if final else 'before_checkpoint_publication')
        self.sync();self.snapshot();owned=str(self.dest.relative_to(REPO))
        self.git(['add','--sparse','--',owned])
        if self.git(['diff','--cached','--quiet'],check=False).returncode==0:return
        self.git(['commit','-m',f'visible-exact: {"finish" if final else "checkpoint"} actual ephemeral Green v4'])
        while True:
            result=self.git(['push','--no-thin','origin','HEAD:refs/heads/main'],check=False)
            print(result.stdout,flush=True)
            if result.returncode==0:
                self.state['published_checkpoints'].append(dict(time=now(),final=final,
                    commit=self.git_text('rev-parse','HEAD').strip()))
                save(self.statusfile,self.state);return
            if not any(s in result.stdout for s in
                ('fetch first','non-fast-forward','failed to update ref','remote rejected','rejected')):
                raise RuntimeError('actual push failed for another reason')
            self.sync();self.snapshot()
            self.git(['add','--sparse','--',owned])
            self.git(['commit','--amend','--no-edit'])

    def v3_stopped_identity(self):
        path=self.science/V3_RECEIPT
        if digest(path)!=V3_RECEIPT_SHA:raise ValueError('the actual stopped-v3 diagnostic receipt changed')
        report=read(path)
        if (str(report.get('run_id'))!='43709951426' or not report.get('complete')
            or report.get('new_scientific_subprocesses')!=0 or len(report.get('jobs',[]))!=1):
            raise ValueError('the unique actual zero-math stopped-v3 receipt is required')
        job=report['jobs'][0];old=job.get('original_complete_small_process_stdout',{})
        meta=job.get('actual_job',{})
        if (job.get('run_id')!=43690634784 or job.get('job_id')!=132740339581
            or meta.get('conclusion')!='failure' or meta.get('status')!='completed'
            or meta.get('head_sha')!='8e962541b9bb6f5fb44f3aa2e8a8975045ac7c3e'
            or old.get('complete') is not False
            or old.get('failure')!=dict(type='RuntimeError',
                message='new unread repository rules require their actual diff to be read and applied')
            or job.get('recoverable_scientific_arrays_or_native_outputs') is not False
            or old.get('exact_old_future_prefix',{}).get('actual_complete_rows')!=1886):
            raise ValueError('the stopped-v3 failure, noncompletion or original1886 identity changed')
        p=old.get('actual_temporary_progress',{})
        if (p.get('future',{}).get('completed_rows')!=5970
            or p.get('future',{}).get('reused_rows')!=1886
            or p.get('future',{}).get('new_rows')!=4084 or p.get('future',{}).get('done') is not True
            or p.get('product',{}).get('completed_rows')!=5970 or p.get('product',{}).get('done') is not True
            or p.get('past',{}).get('completed_rows')!=4032
            or p.get('combined',{}).get('complete_groups')!=103):
            raise ValueError('the actual last-reported v3 stream progress changed')
        self.state['actual_stopped_v3_temporary_arithmetic_to_replay']=dict(
            original_run_id='43690634784',original_run_attempt='1',
            actual_job_id=132740339581,original_source_sha256=V3_SOURCE,
            zero_math_log_reader_run='43709951426',actual_receipt_sha256=V3_RECEIPT_SHA,
            original_complete_log_identity=job['complete_log_identity'],
            original_step8_selected_process_identity=job['original_complete_small_process_stdout_identity'],
            actual_original_failure=old['failure'],
            actual_child_returns=old.get('actual_child_returns'),
            exact_completed_future_rows=5970,accepted_original_future_rows_reused=1886,
            exact_lost_new_future_rows=4084,exact_completed_lost_product_rows=5970,
            last_reported_lost_past_rows=4032,last_reported_lost_complete_groups=103,
            past_and_group_counts_are_not_exact_terminal_native_counts=True,
            additional_unreported_temporary_arithmetic_may_have_completed=True,
            original_last_reported_progress_utc={k:v.get('actual_utc') for k,v in p.items()},
            original1886_rows_recomputed=0,old5970_same_F_Grams_recomputed=0,
            original_same97_cap_rows_recomputed=0,temporary_native_or_arrays_recoverable=False,
            this_is_not_zero_repeated_temporary_arithmetic=True,
            original_math_child_returncode_unknown=True,
            README_guard_failure_is_not_a_new_mathematical_failure=True)

    def stopped_file_receipts(self):
        """Count actual atomic metadata only after all children have stopped."""
        result={}
        source=self.manifest['files'][PRODUCER];stage_identity=None
        for stage in ('future','past','product','ports','groups'):
            directory=self.temp/stage;aggregate=hashlib.sha256();count=0
            for path in sorted(directory.glob('*.json')) if directory.exists() else ():
                raw=path.read_bytes();d=json.loads(raw)
                if (d.get('kind')!=KIND or d.get('source_sha256')!=source
                    or d.get('complete') is not True or not re.fullmatch('[0-9]{5}\\.json',path.name)
                    or not isinstance(d.get('stage_identity'),str)):
                    raise ValueError('an actual stopped-state receipt changed the complete scientific identity')
                if stage_identity is None:stage_identity=d['stage_identity']
                if stage_identity!=d['stage_identity']:raise ValueError('stopped state receipts use different stages')
                aggregate.update(path.name.encode()+b'\0'+hashlib.sha256(raw).digest());count+=1
            result[stage]=dict(complete_state_files=count,
                ordered_exact_state_receipts_sha256=aggregate.hexdigest(),
                count_scope='complete atomic state receipt files actually present after child termination',
                array_bytes_not_reverified_by_this_metadata_only_count=True,
                persisted_recomputable_output=False)
        return result

    def emit_small_stdout(self,label):
        out=dict(kind='recoverable_ephemeral_Green_v4_small_execution_receipt',label=label,
            run_id=self.state.get('run_id'),run_attempt=self.state.get('run_attempt'),utc=now(),
            source_sha256=getattr(self,'manifest',{}).get('files',{}).get(PRODUCER),
            reused_existing_complete_conclusion=self.state.get('reused_existing_complete_conclusion'),
            worker_sha256=digest(__file__),input_manifest_sha256=self.args.manifest_sha,
            original1886_successful_rows_recomputed=0,
            actual_temporary_progress=self.small_progress(),
            actual_terminal_state_metadata=self.state.get('actual_terminal_state_metadata'),
            actual_child_returns=[dict(label=c['label'],actual_returncode=c.get('actual_returncode'))
                for c in self.state.get('children',[])],
            failure=self.state.get('failure'),publication_failure=self.state.get('publication_failure'),
            last_read_commit=self.state.get('last_read_commit'),
            actual_last_readme_check=self.state.get('readme_checks',[])[-1:],
            accepted_rules_sha256=self.state.get('reviewed_rules_sha256'),
            actual_topic_capacity=self.state.get('actual_local_topic_capacity'),
            new_recomputable_data_persisted=False)
        if self.final_native.exists():
            out['complete_scientific_small_conclusion']=self.summarize(read(self.final_native))
        raw=(json.dumps(out,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode()
        if len(raw)>59000:raise ValueError('the actual stdout conclusion exceeds59000 bytes; no artificial splitting')
        receipt=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
        print('BEGIN_GREEN_V4_SMALL_EXECUTION_RECEIPT '+json.dumps(receipt,separators=(',',':')),flush=True)
        print(raw.decode(),end='',flush=True)
        print('END_GREEN_V4_SMALL_EXECUTION_RECEIPT',flush=True)
        self.last_stdout_receipt=receipt
        self.state['latest_recoverable_stdout_conclusion']=receipt

    def reuse_complete_conclusion(self):
        """Reuse an already published success of this exact source and manifest."""
        prefix=str((TOPIC/FOLDER).relative_to(REPO))
        names=self.git_text('ls-tree','-r','--name-only','HEAD','--',prefix).splitlines()
        candidates=sorted(p for p in names if p.startswith(prefix+'/run-') and p.endswith('/process.json'))
        for name in candidates:
            body=self.git_text('show','HEAD:'+name).encode()
            if len(body)>60000:raise ValueError('an existing v4 process is not a genuine small receipt')
            old=json.loads(body)
            if (old.get('input_manifest_sha256')!=self.args.manifest_sha
                or old.get('actual_source_sha256')!=self.manifest['files'][PRODUCER]
                or old.get('worker_source_sha256')!=self.args.worker_sha
                or old.get('complete') is not True):
                continue
            companion=name[:-len('process.json')]+'actual-conclusion-summary.json'
            if companion not in names:
                raise ValueError('a claimed existing complete v4 run lacks its full small conclusion')
            raw=self.git_text('show','HEAD:'+companion).encode()
            if len(raw)>60000:raise ValueError('the existing complete conclusion is not small text')
            d=json.loads(raw);phases=d.get('actual_phase_output_hashes',{})
            if (old.get('actual_scientific_complete') is not True or old.get('failure')
                or old.get('actual_complete5970') is not True
                or old.get('actual_output_sha256')!=d.get('output_sha256')
                or not any(c.get('label')==LABEL and c.get('actual_returncode')==0
                    for c in old.get('children',[]))
                or d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or d.get('complete') is not True or d.get('failure')
                or not d.get('gates') or not all(g.get('passed') is True for g in d['gates'])
                or not all(d.get(k) is True for k in (
                    'complete_finite193_directional_two_boundary_bound_proved',
                    'complete97_input_Poisson_Gram_bound_proved',
                    'complete_true_right_Poisson_contraction_proved'))
                or d.get('complete_infinite_BVP_inverse_proved') is not False
                or d.get('true_parameter_Schur_proved') is not False
                or d.get('old_future_rows_recomputed')!=0
                or d.get('old_target_F_C_Gram_or_validator_calls')!=0
                or {k:v.get('complete_state_files') for k,v in phases.items()}!=
                    dict(future=5970,past=5970,product=5970,ports=5970,groups=187)
                or set(d.get('complete_same_input_directional_contractions',{}))!=set(WINDOWS)):
                raise ValueError('an existing claimed complete v4 conclusion failed exact identity or scope')
            self.state.update(complete=True,reused_existing_complete_conclusion=dict(
                original_run_id=old.get('run_id'),original_run_attempt=old.get('run_attempt'),
                process=dict(path=name,bytes=len(body),sha256=hashlib.sha256(body).hexdigest()),
                summary=dict(path=companion,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()),
                original_output_sha256=d['output_sha256'],same_exact_source_and_manifest=True,
                new_mathematical_subprocesses=0,completed_mathematics_recomputed=0),
                finished_utc=now())
            self.emit_small_stdout('reuse_existing_exact_complete_conclusion')
            self.publish(final=True)
            return True
        return False

    def run_cap(self):
        try:
            self.check_inputs()
            if not os.environ.get('GITHUB_TOKEN'):raise RuntimeError('terminal publication credential unavailable')
            self.git(['config','user.name','github-actions[bot]'])
            self.git(['config','user.email','41898282+github-actions[bot]@users.noreply.github.com'])
            self.sync();self.science_copy()
            if self.reuse_complete_conclusion():return
            self.prepare()
        except BaseException as error:
            self.terminate_child('actual v4 wrapper failure; preserve and count every existing temporary state')
            self.state.update(failure=dict(type=type(error).__name__,message=str(error)),finished_utc=now())
            try:self.state['actual_terminal_state_metadata']=self.stopped_file_receipts()
            except Exception as count_error:
                self.state['actual_terminal_state_metadata_failure']=dict(
                    type=type(count_error).__name__,message=str(count_error))
            self.emit_small_stdout('actual_failure_before_any_publication');self.snapshot()
            try:self.publish(final=True)
            except Exception as publication_error:
                self.state['publication_failure']=str(publication_error)
                save(self.statusfile,self.state);self.emit_small_stdout('actual_final_publication_failure')
            raise
        self.state['finished_utc']=now()
        self.state['actual_terminal_state_metadata']=self.stopped_file_receipts()
        self.emit_small_stdout('actual_complete_science_before_any_final_publication')
        self.publish(final=True)

    def ensure_history(self):
        if self.history_ready:return
        check=self.git(['cat-file','-e',PREDELETE+'^{commit}'],check=False)
        if check.returncode:self.git(['fetch','--filter=blob:none','--no-tags','--depth=1','origin',PREDELETE])
        if self.git(['cat-file','-e',PREDELETE+'^{commit}'],check=False).returncode:
            raise ValueError('the fixed public pre-deletion commit is unavailable')
        self.history_ready=True

    def restore_pins(self):
        self.science.mkdir(parents=True,exist_ok=True)
        receipts=[]
        for name,expected in sorted(self.manifest['files'].items()):
            relative=safe_relative(name);target=self.science/relative;current=REPO/relative
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():
                if digest(target)!=expected:raise ValueError('an immutable temporary pin changed: '+name)
                source='existing_exact_temporary'
            elif current.is_file() and digest(current)==expected:
                shutil.copyfile(current,target);source='exact_current_public_checkout'
            else:
                # New scripts and current rule receipts cannot be substituted
                # by history. Only the exact original closure is eligible.
                if name in self.manifest['new_nonhistorical_files']:
                    raise ValueError('a new exact source or rule receipt is absent or changed: '+name)
                self.ensure_history()
                temporary=target.with_suffix(target.suffix+'.historical-tmp')
                with temporary.open('wb') as output:
                    result=subprocess.run(self.gitbase+['show',PREDELETE+':'+name],
                        cwd=REPO,env=self.env,stdout=output,stderr=subprocess.PIPE,timeout=180)
                if result.returncode:
                    temporary.unlink(missing_ok=True)
                    raise ValueError('one fixed historical public input is absent: '+name)
                if digest(temporary)!=expected:
                    temporary.unlink(missing_ok=True)
                    raise ValueError('one fixed historical public input has another SHA: '+name)
                os.replace(temporary,target);source='fixed_public_history'
            if digest(target)!=expected:raise ValueError('one temporary restored scientific pin changed')
            receipts.append(dict(path=name,sha256=expected,bytes=target.stat().st_size,source=source))
        self.source_receipts=receipts
        save(self.work/'exact-historical-hydration.json',dict(
            commit=PREDELETE,entries=receipts,restored_into_checkout=False,old_mathematics_executed=False))
        self.state['historical_hydration']=dict(
            fixed_public_commit=PREDELETE,exact_files=len(receipts),
            historical_files=sum(r['source']=='fixed_public_history' for r in receipts),
            full_temporary_receipt_sha256=digest(self.work/'exact-historical-hydration.json'),
            restored_into_checkout=False,old_mathematics_executed=False)
        self.hydrated=True

    def check_inputs(self):
        if digest(__file__)!=self.args.worker_sha:raise ValueError('the exact new worker changed')
        if digest(self.args.manifest)!=self.args.manifest_sha:raise ValueError('the new input manifest changed')
        if digest(self.args.rules)!=RULES_SHA or self.args.rules_sha!=RULES_SHA:
            raise ValueError('the currently read no-persistence rules receipt changed')
        self.manifest=read(self.args.manifest)
        if (self.manifest.get('kind')!=MANIFEST_KIND
            or self.manifest.get('repository')!=REPOSITORY
            or os.environ.get('GITHUB_REPOSITORY')!=REPOSITORY
            or self.manifest.get('historical_restore_commit')!=PREDELETE
            or self.manifest.get('new_recomputable_outputs_persisted') is not False):
            raise ValueError('the exact current public one-run policy is required')
        if digest(Path(original.__file__))!=self.manifest['files'][REL+'scripts/'+Path(original.__file__).name]:
            raise ValueError('the actually imported original CI worker changed')
        if self.args.driver_sha!=self.manifest['files'][REL+'scripts/fourfold_codazzi_reviewed_CI_resume.py']:
            raise ValueError('the original reviewed driver identity changed')
        for module in list(sys.modules.values()):
            filename=getattr(module,'__file__',None)
            if not filename:continue
            path=Path(filename).resolve()
            try:relative=str(path.relative_to(REPO))
            except ValueError:continue
            if relative in self.manifest['files'] and digest(path)!=self.manifest['files'][relative]:
                raise ValueError('one actually imported frozen infrastructure source changed: '+relative)
        actual_rules=self.accept_live_review()
        versions={name:importlib.metadata.version(name) for name in self.manifest['packages']}
        if (versions!=self.manifest['packages']
            or '.'.join(map(str,sys.version_info[:3]))!=self.manifest['python_version']):
            raise ValueError('the pinned arithmetic runtime changed')
        if not self.hydrated:self.restore_pins()
        for name,expected in self.manifest['files'].items():
            if digest(self.science/safe_relative(name))!=expected:
                raise ValueError('the immutable scientific copy changed: '+name)
        old=read(self.science/OLD_MANIFEST)
        if (digest(self.science/OLD_MANIFEST)!=OLD_MANIFEST_SHA
            or len(old['files'])!=353
            or any(self.manifest['files'].get(k)!=v for k,v in old['files'].items())
            or set(self.manifest['files'])!=(set(old['files'])|{OLD_MANIFEST}|set(self.manifest['new_nonhistorical_files']))):
            raise ValueError('one original same97/Poisson/5970 closure pin changed')
        self.prior_failure_identity()
        self.v3_stopped_identity()
        self.state.update(input_manifest_sha256=self.args.manifest_sha,
            package_versions=versions,python_version=sys.version,all_pinned_inputs_verified=True,
            immutable_scientific_copy=str(self.science),
            actual_reviewed_readme_sha256=actual_rules,
            explicit_readme_review_commit=self.reviewed['read_commit'])


    def prior_failure_identity(self):
        pp,sp=self.science/PRIOR_PROCESS,self.science/PRIOR_SUMMARY
        if digest(pp)!=PRIOR_PROCESS_SHA or digest(sp)!=PRIOR_SUMMARY_SHA:
            raise ValueError('the exact failed v2 process or actual final-file count receipt changed')
        prior,summary=read(pp),read(sp)
        if (str(prior.get('run_id'))!='43681612825' or str(prior.get('run_attempt'))!='1'
            or prior.get('actual_source_sha256')!=PRIOR_SOURCE
            or summary.get('source_sha256')!=PRIOR_SOURCE
            or summary.get('complete') or summary.get('failure',{}).get('type')!='RuntimeError'
            or not any(c.get('actual_returncode')==1 for c in prior.get('children',[]))
            or summary.get('output_sha256')!='c5c15d6ce18c8831cd820f6d9cfc699502475f544c9a52ae94f75e70da43b960'
            or {k:v['complete_state_files'] for k,v in summary['actual_phase_output_hashes'].items()}!=PRIOR_COUNTS
            or prior['actual_temporary_progress']['consumer-0']['failure']!=
                dict(message='nonfinite exact dyadic slack',type='ArithmeticError')):
            raise ValueError('the original genuine mathematical failure and lost temporary prefix are required')
        self.state['actual_previous_unpersisted_arithmetic_to_redo']=dict(
            original_run_id='43681612825',actual_returncode=1,
            original_source_sha256=PRIOR_SOURCE,
            actual_process_sha256=PRIOR_PROCESS_SHA,actual_summary_sha256=PRIOR_SUMMARY_SHA,
            exact_final_complete_files=PRIOR_COUNTS,
            lost_new_future_rows=2340,lost_new_past_rows=1800,
            lost_new_product_rows=4331,lost_new_canonical_ports=5970,
            lost_complete_local_groups=0,old1886_recomputed=0,
            old_final_phase_receipt_hashes=summary['actual_phase_output_hashes'],
            temporary_data_not_available_after_original_job=True,
            this_is_not_zero_repeated_temporary_arithmetic=True)

    def runtime_resources(self,label):
        disk=shutil.disk_usage(self.work)
        memory={}
        for line in Path('/proc/meminfo').read_text().splitlines():
            name,rest=line.split(':',1)
            if name in ('MemTotal','MemAvailable'):
                memory[name]=int(rest.split()[0])*1024
        # All exact original arrays are already restored. This reserve
        # covers the complete new future/past/product/port/group arrays,
        # including the additional97-by97 error Gram, without deleting
        # a mathematical channel. The remaining4GiB is working margin.
        required_new_output_bytes=10*1024**3
        required_margin_bytes=4*1024**3
        item=dict(label=label,utc=now(),disk_free_bytes=disk.free,
            disk_total_bytes=disk.total,memory_bytes=memory,available_cpu_count=os.cpu_count(),
            required_new_output_bytes=required_new_output_bytes,
            required_working_margin_bytes=required_margin_bytes,
            required_available_memory_bytes=4*1024**3,required_compute_cpus=4)
        self.state['actual_runtime_resource_check']=item
        if (disk.free<required_new_output_bytes+required_margin_bytes
            or memory.get('MemAvailable',0)<4*1024**3 or (os.cpu_count() or 0)<4):
            self.snapshot()
            raise RuntimeError('insufficient measured temporary resources for the complete declared computation')
        return item

    def science_copy(self):
        if not self.hydrated:raise ValueError('exact historical hydrate must precede science execution')
        self.check_inputs()

    def zip_download(self,metadata,path):
        actual=super().zip_download(metadata,path)
        expected=metadata.get('digest','')
        if (metadata.get('size_in_bytes')!=actual['bytes']
            or not expected.startswith('sha256:') or expected[7:]!=actual['sha256']):
            raise ValueError('an actual original artifact ZIP differs from GitHub metadata')
        fixed={BACK_ID:(286134725,BACK_ZIP),CAP_ID:(759122,CAP_ZIP)}
        if metadata['id'] in fixed and (actual['bytes'],actual['sha256'])!=fixed[metadata['id']]:
            raise ValueError('one explicitly fixed original complete ZIP changed')
        return actual

    def download(self,run,name,arrays_only=False):
        # Full extraction can also supply the original matrices. Reuse the
        # one actual ZIP instead of downloading the old failure a second time.
        if arrays_only:
            full=self.input_root/name
            marker=full/'actual-original-artifact-download.json'
            if marker.exists() and (full/'matrices').is_dir():
                recorded=read(marker);metadata=self.artifact_metadata(run,name)
                if (recorded.get('artifact_id')!=metadata['id'] or
                    str(recorded.get('run_id'))!=str(run) or recorded.get('arrays_only')):
                    raise ValueError('a complete original artifact alias changed identity')
                alias=self.array_root/name
                if alias.is_symlink():
                    if alias.resolve()!=full.resolve():raise ValueError('an existing exact array alias changed')
                elif alias.exists():raise ValueError('refuse to replace any original array directory')
                else:alias.symlink_to(full,target_is_directory=True)
                return alias
        return super().download(run,name,arrays_only=arrays_only)

    def original_prefix(self):
        root=self.download(BACK_RUN,BACK_NAME);meta=self.artifact_metadata(BACK_RUN,BACK_NAME)
        if meta['id']!=BACK_ID:raise ValueError('the unique actual rule-failure artifact changed')
        pp=root/'process.json';actual=read(pp)
        if (str(actual.get('run_id'))!=BACK_RUN or str(actual.get('run_attempt'))!='1'
            or actual.get('worker_source_sha256')!='3709858655e70ebe7bd334b4c1b0c070cdb8855ad31878a240229c4768b3e096'
            or actual.get('input_manifest_sha256')!='3350a96fbea47ee33bb09cb6602cb1e978e8ba00a034c7f735dfb60bade99910'
            or actual.get('failure',{}).get('type')!='RuntimeError'
            or actual.get('failure',{}).get('message')!='new unread repository rules need their actual diff read: README.md'):
            raise ValueError('the actual original stopping reason or scientific worker identity differs')
        logical='native/complete-directional-matrix-Green-backward.json.gz'
        matches=[x for x in actual.get('native_files',[]) if x.get('logical_file')==logical]
        if len(matches)!=1:raise ValueError('one exact native receipt of the stopped original sweep is required')
        header=self.exact_native(root,logical,actual,matches[0]['sha256'])
        staged=self.staged_sweep(root,actual,header,self.work/'exact-old-future-prefix')
        doc,rows=self.all_sweep_rows(staged)
        if (doc.get('complete') or doc.get('failure') or not 1658<=len(rows)<5970
            or not doc.get('gates') or not all(g['passed'] for g in doc['gates'])):
            raise ValueError('the old successful future prefix has another complete scope')
        self.state['exact_old_future_prefix']=dict(
            run_id=BACK_RUN,run_attempt='1',artifact_id=BACK_ID,original_zip_sha256=BACK_ZIP,
            native_sha256=digest(staged),process_sha256=digest(pp),
            actual_complete_rows=len(rows),old_successful_rows_recomputed=0,
            actual_original_failure=actual['failure'],actual_original_gates=doc['gates'],
            latest_original_readme_check=[readme_receipt(c) for c in actual.get('readme_checks',[])[-1:]] or None)
        self.record_process(pp,'original-rule-failure-process.json')
        self.publish()
        return staged,pp

    def original_cap(self):
        root=self.download(CAP_RUN,CAP_NAME);meta=self.artifact_metadata(CAP_RUN,CAP_NAME)
        if meta['id']!=CAP_ID:raise ValueError('the exact completed same97 cap artifact changed')
        pp=root/'process.json';actual=read(pp)
        native=self.exact_native(root,'native/complete-same97-cap-posterior.json.gz',actual,CAP_NATIVE)
        arrays=root/'matrices'/'complete-same97-full-cap-posterior-Grams.npz'
        if not arrays.is_file() or arrays.stat().st_size!=723262 or digest(arrays)!=CAP_ARRAY:
            raise ValueError('the original complete signed97 cap matrices changed')
        self.record_process(pp,'original-complete-same97-cap-process.json')
        self.state['exact_original_cap']=dict(run_id=CAP_RUN,artifact_id=CAP_ID,
            native_sha256=CAP_NATIVE,original_array_sha256=CAP_ARRAY,
            actual_process_sha256=digest(pp),original_rows_recomputed=0)
        return native,pp,root/'matrices'

    def small_progress(self):
        progress={}
        directory=self.temp/'progress'
        if directory.exists():
            for path in sorted(directory.glob('*.json')):
                d=read(path)
                progress[path.stem]={k:d.get(k) for k in
                    ('stage','actual_utc','completed_rows','reused_rows','new_rows','completed_groups',
                     'last_group','streams','complete_groups','queued_groups','consumer_processes',
                     'done','seconds','failure','diagnostic_exponents','reused_same_run_preflight_rows',
                     'extreme_positive_weight_tests') if k in d}
                progress[path.stem]['original_temporary_receipt_sha256']=digest(path)
        return progress

    def summarize(self,d):
        result={k:d.get(k) for k in (
            'kind','source_sha256','complete','failure','gates','seconds','arithmetic_bits',
            'input_sha256','original_formula_sources','exact_original_future_prefix','actual_phase_output_hashes',
            'complete_true_finite193_body_high_to_low_bounds','complete_directional_posterior_components',
            'posterior_complete_true_Green_constants',
            'complete_true_right_Poisson_operator_upper','actual_true97_normalization',
            'exact_inner_interval','exact_negative_output_interval','exact_boundary_input_units',
            'old_future_rows_recomputed','old_target_F_C_Gram_or_validator_calls',
            'complete_finite193_directional_two_boundary_bound_proved',
            'complete97_input_Poisson_Gram_bound_proved',
            'complete_true_right_Poisson_contraction_proved',
            'independent_full_high_body_and_high_cut_inputs_retained',
            'complete_infinite_BVP_inverse_proved','true_parameter_Schur_proved',
            'new_recomputable_arrays_persisted','actual_early_preflight','actual_v2_unpersisted_arithmetic_redone')}
        result['actual_stopped_v3_temporary_arithmetic_replayed']=self.state.get('actual_stopped_v3_temporary_arithmetic_to_replay')
        result['output_sha256']=digest(self.final_native)
        result['output_bytes']=self.final_native.stat().st_size
        result['complete_same_input_directional_contractions']={
            w:dict(complete_operator_upper=r['complete_operator_upper'],
                selected_complete_contraction=r['selected_complete_contraction'],
                all_complete_contraction_choices={k:dict(operator_upper=v['operator_upper'],origin=v['origin'])
                    for k,v in r['all_complete_contraction_choices'].items()},
                signed_trace_before_final_upper=r['signed_trace_before_final_upper'])
            for w,r in d.get('complete_same_input_directional_contractions',{}).items()}
        result['actual_parallel_completion']={k:v for k,v in d.get('actual_parallel_completion',{}).items()
            if k!='streams'}
        result['actual_final_stream_counts']=self.small_progress()
        result['temporary_final_output_receipts']=[]
        for name in ('complete-true97-Poisson.json','complete-same97-contraction.json'):
            path=self.temp/name
            if path.exists():
                meta=read(path)
                result['temporary_final_output_receipts'].append(dict(
                    logical_file=name,sha256=digest(path),bytes=path.stat().st_size,
                    array_receipt=meta.get('arrays'),retained_after_job=False))
        return result

    def snapshot(self):
        self.dest.mkdir(parents=True,exist_ok=True)
        self.state.update(snapshot_utc=now(),wall_seconds=time.monotonic()-self.started,
            actual_temporary_progress=self.small_progress(),
            new_recomputable_repository_data=False,new_Release_uploads=False,new_Actions_artifacts=False)
        if self.final_native.exists():
            d=read(self.final_native);self.summary=self.summarize(d)
            self.state['actual_output_sha256']=digest(self.final_native)
            self.state['actual_scientific_complete']=bool(d.get('complete'))
            self.state['actual_scientific_failure']=d.get('failure')
            small(self.dest/'actual-conclusion-summary.json',self.summary)
        actual=dict(self.state)
        # Full original inputs/processes and temporary native outputs are
        # only in scratch. The concise publication contains no such bytes.
        actual['original_process_receipts']=[dict(file=p.name,bytes=p.stat().st_size,sha256=digest(p))
            for p in sorted(self.evidence.glob('*process.json')) if p.is_file()]
        actual['actual_original_artifact_archives']=[archive_receipt(read(p))
            for p in sorted((self.evidence/'original-artifact-downloads').glob('*.json'))]
        actual['new_output_policy']='only scripts, parameters, run IDs, output SHA and true small conclusions; no new data artifact'
        small(self.dest/'process.json',actual)
        save(self.statusfile,self.state)

    def execute(self,label,command):
        item=dict(label=label,command=command,started_utc=now(),actual_returncode=None)
        self.state['children'].append(item);save(self.statusfile,self.state)
        began=time.monotonic()
        with self.log.open('ab') as stream:
            self.child=subprocess.Popen(command,cwd=self.science_topic,env=self.env,
                stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
            previous=time.monotonic()
            while self.child.poll() is None:
                if self.interrupted:
                    self.terminate_child('actual runner signal; new temporary outputs are not persisted');break
                if time.monotonic()-self.started>self.args.compute_minutes*60:
                    self.terminate_child('actual single public slot reached its limit; no false completion');break
                if time.monotonic()-previous>self.args.checkpoint_minutes*60:
                    self.publish();previous=time.monotonic()
                time.sleep(5)
        item.update(actual_returncode=self.child.returncode,wall_seconds=time.monotonic()-began,finished_utc=now())
        save(self.statusfile,self.state)
        if self.child.returncode:
            if self.log.exists():print(self.log.read_text(errors='replace')[-20000:],flush=True)
            raise RuntimeError(label+' actually returned '+str(self.child.returncode))
        self.publish()

    def prepare(self):
        inputs,data=self.inputs()
        backward,process=self.original_prefix()
        if read(process).get('actual_input_sha256')!={k:digest(inputs[k]) for k in SOURCE_KEYS}:
            raise ValueError('the old successful future prefix uses another exact input process snapshot')
        self.matrix_arrays(data,backward,None,False)
        native,cap_process,cap_arrays=self.original_cap()
        self.state['actual_input_sha256']={k:digest(v) for k,v in inputs.items()}
        self.state['actual_source_sha256']=self.manifest['files'][PRODUCER]
        self.runtime_resources('after_all_exact_original_inputs_before_new_arithmetic')
        self.publish()
        command=[sys.executable,'-u',str(self.science/PRODUCER),
            '--matrix-run',self.args.matrix_run,'--array-root',str(self.array_root),
            '--old-backward',str(backward),'--old-backward-process',str(process),
            '--cap',str(native),'--cap-process',str(cap_process),'--cap-arrays',str(cap_arrays),
            '--temp',str(self.temp),'--out',str(self.final_native),'--bits',str(self.args.bits)]
        for key in SOURCE_KEYS:command+=['--'+key,str(inputs[key])]
        self.execute(LABEL,command)
        d=read(self.final_native)
        if (d.get('kind')!=KIND or d.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or not d.get('complete') or d.get('failure')
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or not d.get('complete_finite193_directional_two_boundary_bound_proved')
            or not d.get('complete97_input_Poisson_Gram_bound_proved')
            or not d.get('complete_true_right_Poisson_contraction_proved')
            or d.get('complete_infinite_BVP_inverse_proved') or d.get('true_parameter_Schur_proved')
            or d.get('old_future_rows_recomputed')!=0
            or d.get('old_target_F_C_Gram_or_validator_calls')!=0):
            raise ValueError('the new full temporary calculation did not pass its declared exact scope')
        self.state.update(complete=True,actual_output_sha256=digest(self.final_native),
            actual_scientific_gates=len(d['gates']),actual_complete5970=True,
            actual_full_source_Poisson_and_cap_contraction=True,
            old_future_rows_recomputed=0,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
        self.snapshot()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir'):
        parser.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha','worker-sha'):
        parser.add_argument('--'+name,required=True)
    parser.add_argument('--matrix-run',default='43654510038')
    parser.add_argument('--matrix-attempt',default='1')
    parser.add_argument('--bits',type=int,default=192)
    parser.add_argument('--compute-minutes',type=int,default=340)
    parser.add_argument('--checkpoint-minutes',type=int,default=10)
    a=parser.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if a.matrix_run!='43654510038' or a.matrix_attempt!='1' or a.bits<192:
        raise ValueError('the exact old whole5970 matrix identity and directed precision floor are fixed')
    if not 1<=a.checkpoint_minutes<=10 or not 1<=a.compute_minutes<=345:
        raise ValueError('real pull checkpoints and one bounded public runner are required')
    a.phase='ephemeral';a.kind='ephemeral-parallel-matrix-Green-Poisson-v4'
    a.mode='prepare';a.first=0;a.end=5970;a.recovery_manifest=None;a.recovery_sha=None
    worker=EphemeralWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
