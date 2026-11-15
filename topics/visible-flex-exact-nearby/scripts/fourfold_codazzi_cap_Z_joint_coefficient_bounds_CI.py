#!/usr/bin/env python3
"""Public original-byte restoration and reviewed publication for cap Z norms."""
from __future__ import annotations
import argparse,hashlib,json,os,shutil,signal,subprocess,sys,time,urllib.error,urllib.request,zipfile
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC,REPO,save,now
from fourfold_native_lossless_parts import restore

PUBLIC='Rogerhu12/math-research-public'
REL=Path('topics/visible-flex-exact-nearby')
PRODUCER=REL/'scripts/fourfold_codazzi_cap_Z_joint_coefficient_bounds.py'
FOLDER='cap_Z_joint_coefficient_ci'
KIND='actual_complete_cap_full193_Z_joint_coefficient_suprema_v1'
NATIVE='complete-cap-Z-joint-coefficients.json.gz'
INDEX=REL/'data/current_root_phase_response_20261114/response-full.json'
DIRECTION=REL/'notes/2026-11-14-R133-explicit-continuous-response-direction-native.json.gz'
PREPARED=REL/'notes/correlated_body_ci/run-43583838026-1-prepare/prepared-manifest.json'
PREPARED_PROCESS=REL/'notes/correlated_body_ci/run-43583838026-1-prepare/process.json'
SOURCE_SHA='d909f2fc5eff54e42c3dcfe9355016f42c08cef1a6b04298cc62022fe6bf7d1e'
ZDEF='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'
PARTS={
 'response-full-part012.npz.gz':('777337c853329f26719b148e34db079c5ca0ed34991aa40220f25624e4af0b3c',2698989),
 'response-full-part013.npz.gz':('4a863085ec89c7d7104b4fdf566f9ae380d22eb7b4e4f8b2146cd190c3b4b037',1517845)}
ARCHIVE=dict(id=14109363064,run_id=43583838026,attempt=1,
 name='visible-exact-body-prepared-43583838026-1',size_in_bytes=166702374,
 sha256='34d95f5d263b210134da3ae5bb243df4369cd83fbdd196c068c9727b194cd710')

def small(path,value):
    raw=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if len(raw)>60000:raise ValueError('a genuine cap-joint summary exceeds60000 UTF8 bytes')
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_bytes(raw)

def identity():
    return dict(index='ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6',
        direction='87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88',
        selected_original_shards={k:v[0] for k,v in PARTS.items()},
        exact_domain=['9/10','25/8'],complete_direction_definition=ZDEF)

def hydrate(a):
    if digest(a.manifest)!=a.manifest_sha or digest(a.rules)!=a.rules_sha:
        raise ValueError('the exact new manifest or separately reviewed rules changed')
    m=read(a.manifest)
    paths=set(m['files'])|set(m['readme_sha256'])|{
        str(a.manifest.relative_to(REPO)),str(a.rules.relative_to(REPO)),
        str(REL/'scripts/'),str(REL/'notes'/FOLDER)}
    subprocess.run(['git','-c','safe.directory='+str(REPO),'sparse-checkout','set','--no-cone','--stdin'],
        cwd=REPO,input='\n'.join('/'+p for p in sorted(paths))+'\n',text=True,check=True)
    print(json.dumps(dict(complete_pinned_paths=len(paths),old_cap_shards_not_reconstructed=True)),flush=True)

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):return None

class CapJointWorker(ReviewedBodyWorker):
    def __init__(self,args):
        super().__init__(args)
        self.name=f'run-{self.run_label}-complete-cap-Z-joint-coefficients'
        self.dest=TOPIC/'notes'/FOLDER/self.name
        self.download_pull=time.monotonic()
        self.state.update(kind='actual_public_complete_cap_Z_joint_coefficient_process',
            worker_source_sha256=digest(__file__),exact_Z_definition_sha256=ZDEF,
            original_trial_repairs_targets_FFTs_and_residuals_recomputed=0,
            intrinsic_beta_gamma_K_bounds_consumed=False,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
        self.state.pop('whole_original_parameter_half_width',None)
        self.state.pop('original_ac1_operator_not_relabelled_as_repaired',None)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest['files'][str(PRODUCER)]!=SOURCE_SHA:
            raise ValueError('the complete cap-joint mathematical source changed')
        if self.manifest['original_prepared_artifact']!=ARCHIVE:
            raise ValueError('the original successful prepared archive changed')

    def api(self,suffix):
        req=urllib.request.Request('https://api.github.com/repos/'+PUBLIC+suffix,
            headers={'Authorization':'Bearer '+os.environ['GITHUB_TOKEN'],
                'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
        with urllib.request.urlopen(req,timeout=90) as response:return json.load(response)

    def download_original(self):
        info=self.api('/actions/artifacts/'+str(ARCHIVE['id']))
        if (info['id']!=ARCHIVE['id'] or info['name']!=ARCHIVE['name']
            or info['size_in_bytes']!=ARCHIVE['size_in_bytes'] or info['expired']
            or info['workflow_run']['id']!=ARCHIVE['run_id']
            or info.get('digest')!='sha256:'+ARCHIVE['sha256']):
            raise ValueError('the original exact public body archive metadata changed')
        destination=self.work/'original-body-prepared.zip'
        if not destination.exists():
            req=urllib.request.Request('https://api.github.com/repos/'+PUBLIC+
                '/actions/artifacts/'+str(ARCHIVE['id'])+'/zip',
                headers={'Authorization':'Bearer '+os.environ['GITHUB_TOKEN'],
                    'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
            opener=urllib.request.build_opener(NoRedirect)
            try:response=opener.open(req,timeout=90)
            except urllib.error.HTTPError as error:
                if error.code not in (301,302,303,307,308):raise
                url=error.headers.get('Location','')
                if not url.startswith('https://'):raise ValueError('the original artifact redirect is not HTTPS')
                # Repository credentials are never forwarded to the signed object URL.
                response=urllib.request.urlopen(url,timeout=90)
            tmp=destination.with_suffix('.part')
            with response,tmp.open('wb') as output:
                while True:
                    chunk=response.read(8*1024*1024)
                    if not chunk:break
                    output.write(chunk)
                    if time.monotonic()-self.download_pull>self.args.checkpoint_minutes*60:
                        self.publish();self.download_pull=time.monotonic()
            os.replace(tmp,destination)
        if destination.stat().st_size!=ARCHIVE['size_in_bytes'] or digest(destination)!=ARCHIVE['sha256']:
            raise ValueError('the original prepared archive bytes differ from their exact recorded identity')
        small(self.evidence/'original-prepared-artifact-receipt.json',
            dict(original=ARCHIVE,actual_archive_sha256=digest(destination),
                actual_archive_bytes=destination.stat().st_size,
                all_original_bytes_verified=True,old_reconstruction_executed=False))
        return destination

    def original_inputs(self):
        prepared,process=read(self.science/PREPARED),read(self.science/PREPARED_PROCESS)
        if (not prepared['complete'] or prepared['kind']!='exact_same_all_regular_body_CI_bundle_v1'
            or not prepared['all_original_cubic_and_trial_shard_SHA256_verified']
            or process['run_id']!='43583838026' or process['run_attempt']!='1'
            or not process['complete'] or not process['all_original_scientific_bytes_reconstructed']
            or process['prepared_bundle_sha256']!=digest(self.science/PREPARED)
            or len(process['children'])!=2
            or not all(c.get('actual_returncode')==0 for c in process['children'])):
            raise ValueError('the original already successful preparation receipt changed')
        archive=self.download_original();destination=self.artifact/'original-data';destination.mkdir(exist_ok=True)
        receipts=[]
        with zipfile.ZipFile(archive) as z:
            def exact_member(name):
                found=[n for n in z.namelist() if n==name or n.endswith('/'+name)]
                if len(found)!=1:raise ValueError('the original archive member is absent or ambiguous: '+name)
                return z.read(found[0])
            raw=exact_member('prepared-manifest.json')
            if hashlib.sha256(raw).hexdigest()!=digest(self.science/PREPARED):
                raise ValueError('the archived complete preparation manifest differs from its pinned original bytes')
            requested={'response-full.json':(identity()['index'],11295),**PARTS}
            for name,(h,size) in requested.items():
                member='trials/response/'+name
                if prepared['files'][member]!={'sha256':h,'bytes':size}:
                    raise ValueError('one selected whole original shard differs from the prepared manifest')
                raw=exact_member(member)
                if len(raw)!=size or hashlib.sha256(raw).hexdigest()!=h:
                    raise ValueError('one selected whole original cap shard changed')
                path=destination/name
                if path.exists() and path.read_bytes()!=raw:raise ValueError('preserve the original selected input')
                path.write_bytes(raw);receipts.append(dict(original_member=member,bytes=size,sha256=h))
        if digest(destination/'response-full.json')!=digest(self.science/INDEX):
            raise ValueError('the already published root index differs from the complete original physical index')
        shutil.copyfile(self.science/DIRECTION,destination/DIRECTION.name)
        small(self.evidence/'original-two-cap-shard-selection.json',
            dict(original_archive=ARCHIVE,original_prepared_manifest_sha256=digest(self.science/PREPARED),
                original_success_process_sha256=digest(self.science/PREPARED_PROCESS),
                complete_cap_inputs=receipts,original_complete_direction_certificate=digest(self.science/DIRECTION),
                exact_cap_domain=['9/10','25/8'],old_repairs_and_targets_recomputed=0))
        archive.unlink()
        return destination

    def previous(self):
        candidates=[]
        for pp in sorted((TOPIC/'notes'/FOLDER).glob('*/process.json')):
            if pp==self.dest/'process.json':continue
            p=read(pp)
            if (p.get('kind')!=self.state['kind'] or p.get('repository')!=PUBLIC
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha):continue
            entries=[r for r in p.get('native_files',[])
                if r.get('logical_file')=='native/'+NATIVE]
            if not entries:continue
            if len(entries)!=1:raise ValueError('one original cap-joint native receipt is ambiguous')
            receipt=entries[0]
            if receipt.get('file'):native=pp.parent/receipt['file']
            else:
                manifest=pp.parent/receipt['lossless_manifest']
                native=self.work/('restored-'+receipt['sha256']+'.json.gz')
                restore(manifest,native)
            if not native.exists() or digest(native)!=receipt['sha256'] or native.stat().st_size!=receipt['bytes']:
                raise ValueError('a matching original cap-joint prefix is missing; restore it without recomputing')
            d=read(native)
            if (d.get('kind')!=KIND or d.get('source_sha256')!=SOURCE_SHA
                or d.get('input_sha256')!=identity()):continue
            if d.get('failure'):
                raise ValueError('preserve an actual mathematical failure; do not repeat it without a correction')
            rows=d.get('completed_cap_piece_count',-1)
            if rows<0 or rows!=len(d.get('rows',[])):
                raise ValueError('an original completed cap prefix has inconsistent row counts')
            child0=any(c.get('label')=='complete_cap193_coefficientwise_Bernstein_and_joint_norms'
                and c.get('actual_returncode')==0 for c in p.get('children',[]))
            reused=p.get('original_complete_success_reused_without_child') and p.get('original_success_process_sha256')
            complete=bool(d.get('complete') and d.get('gates') and all(g['passed'] for g in d['gates'])
                and (child0 or reused))
            candidates.append(((int(complete),rows),pp,native,complete))
        return max(candidates,key=lambda item:item[0]) if candidates else None

    def summary(self,d):
        return {k:d.get(k) for k in (
            'kind','source_sha256','complete','failure','seconds','gates','input_sha256',
            'exact_interval','requested_cap_piece_count','completed_cap_piece_count',
            'actual_first_piece','actual_last_piece','reused_complete_cap_pieces','new_complete_cap_pieces',
            'complete_Z_joint_homogeneous_angular_derivative_norms','exact_complete_Z_mean_absolute_upper',
            'exact_complete_Z_pair_A0_upper','joint_norm_order',
            'all_original_repair_target_FFT_ODE_and_cap_residual_recomputations',
            'intrinsic_beta_gamma_K_bounds_consumed','nonlinear_solution_or_full_infinite_inverse_claimed')}

    def snapshot(self):
        path=self.cache/NATIVE
        if path.exists():
            d=read(path);s=self.summary(d)
            s['native_sha256']=digest(path)
            small(self.evidence/'actual-latest-cap-Z-joint-summary.json',s)
            self.state['actual_completed_cap_pieces']=d.get('completed_cap_piece_count')
            self.state['latest_scientific_native_sha256']=digest(path)
        super().snapshot()

    def prepare(self):
        old=self.previous();native=self.cache/NATIVE;resume=None;complete=False
        if old:
            _,pp,path,complete=old
            prior=self.artifact/'original-processes';prior.mkdir(exist_ok=True)
            shutil.copyfile(pp,prior/'process.json')
            small(self.evidence/'original-cap-joint-prefix-reuse.json',
                dict(original_process_sha256=digest(pp),original_native_sha256=digest(path),
                    original_process_complete=read(pp).get('complete'),original_math_complete=complete,
                    original_actual_completed_cap_pieces=read(path)['completed_cap_piece_count'],
                    successful_mathematics_reused_after_publication_failure=True))
            if complete:
                shutil.copyfile(path,native)
                self.state.update(original_complete_success_reused_without_child=True,
                    original_success_process_sha256=digest(pp))
            else:
                resume=self.work/'accepted-original-prefix.json.gz';shutil.copyfile(path,resume)
        if not complete:
            original=self.original_inputs()
            self.publish()
            command=[sys.executable,'-u',str(self.science/PRODUCER),
                '--index',str(self.science/INDEX),'--parts-dir',str(original),
                '--direction-native',str(self.science/DIRECTION),'--out',str(native)]
            if resume:command+=['--resume',str(resume)]
            self.execute('complete_cap193_coefficientwise_Bernstein_and_joint_norms',command)
        d=read(native)
        if (d.get('kind')!=KIND or d.get('source_sha256')!=SOURCE_SHA
            or d.get('input_sha256')!=identity() or not d.get('complete') or d.get('failure')
            or not d.get('gates') or not all(g['passed'] for g in d['gates'])
            or d['completed_cap_piece_count']!=d['requested_cap_piece_count']
            or d['all_original_repair_target_FFT_ODE_and_cap_residual_recomputations']!=0
            or d['nonlinear_solution_or_full_infinite_inverse_claimed']):
            raise ValueError('the actual complete cap coefficientwise joint bounds did not pass their exact scope')
        summary=self.summary(d);summary.update(native_sha256=digest(native),
            original_complete_success_reused_without_child=complete)
        small(self.evidence/'complete-cap-Z-joint-summary.json',summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_completed_cap_pieces=d['completed_cap_piece_count'],actual_scientific_gates=len(d['gates']),
            actual_new_cap_pieces_this_child=0 if complete else d['new_complete_cap_pieces'],
            original_complete_success_reused_without_child=complete,
            complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode',choices=('hydrate','prepare'),required=True)
    for name in ('manifest','rules'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--work',type=Path);p.add_argument('--artifact-dir',type=Path)
    p.add_argument('--compute-minutes',type=int,default=45)
    p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='cap-Z-joint';a.first=0;a.end=6144;a.recovery_manifest=None;a.recovery_sha=None
    if a.mode=='hydrate':hydrate(a);return
    if a.work is None or a.artifact_dir is None:p.error('actual work and artifact directories are required')
    worker=CapJointWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()

if __name__=='__main__':main()
