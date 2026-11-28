#!/usr/bin/env python3
"""Recover the literal terminals of fixed, naturally completed public jobs."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import subprocess
import tempfile
import time
from collections import Counter

REPO = 'Rogerhu12/math-research-public'
ROOT = 'https://api.github.com/repos/'+REPO
OUT = Path('completed-receipts')
TARGETS = (
    ('R695',46148919282,140990956410,'9d2e6c88623a42b351b65e9bf5eb502631839253','R695_ACTUAL204_EARLY_HEIGHT_FULL_BVP_FINAL'),
    ('R711',46152161518,141000942072,'9e577e4e27e0b4b9d7a8ce29542d05147c23c54f',None),
    ('R643',46134171516,140945669998,'bc7799966d423e6ee7bb43f19c7a5549c8eb3dbd','R643_COUPLED_FINAL'),
    ('R631',46133637169,140944040121,'df0c989652a0f243a1bae3cb37e116932455cc99','R631_DESIGN_FINAL'),
    ('R702',46150227928,140995038056,'89f416b3c39057ef22441e194f343a24553ebe27','R702_ALIGNED44_ORIGINAL_FULL_RULING_FINAL'),
    ('R707',46153308216,141004422866,'427914e2e6ff476e78d0a73e4e66b4771ed6c396','FINITE_LOCAL_TAIL_FINAL'),
    ('R705',46153586472,141005268888,'0fafb2760fe60ae072f1754dd1daa7983c42b5a3','R705_FINAL'),
    ('R703',46151140087,140997832329,'1b2ba533d51b4f4b416d30dcee1aaa516b2c64be',None),
)
SOURCE = 'INVERSE_ACTIONS_SOURCE'
STAMP = re.compile(rb'^(?:\xef\xbb\xbf)?\d{4}-\d\d-\d\dT[0-9:.]+Z ')
KINDS = re.compile(rb'"kind"\s*:\s*"(terminal|transport|transported_actual_source)"')
SIDE = {'R695':('FRONTIER_ACTUAL_',), 'R702':('R674_ALIGNED_ACTUAL_STATE','R674_ACTUAL_TRIAL','R702_'),
        'R705':('R705_PAID_OBJECT','R705_R709_CONTINUOUS_PHYSICAL_STRIP','R705_TRANSPORT','R705_NEW_ATLAS'),
        'R707':('FINITE_LOCAL_TAIL_DEFINITION',), 'R631':('R631_DESIGN_RESTORED',), 'R643':('R643_COUPLED_RESTORED',)}
STATE = {'R695':'actual_last_complete_true_state.shape_parameters','R702':'actual_last_complete_true_state.shape_parameters',
         'R643':'actual_response','R631':'actual_current_checkpoint.actual_complete_q',
         'R711':'actual_parameters','R703':'all_parameters','R705':'parameters','R707':'actual_retained_state.q'}
PICK = {'R695':'actual_last_complete_true_state_identity actual_last_complete_true_observation fixed_actual_curve_refinement inflight_trial latest_polynomial_qualification',
        'R702':'actual_last_complete_true_state_identity actual_last_complete_true_observation fixed_actual_curve_refinement inflight_trial latest_genuine_unclosed_trial physical_material_tree_cost',
        'R643':'actual_current_checkpoint actual_response_identity pending_trial_not_accepted complete_final_readout partial_readout',
        'R631':'actual_current_checkpoint pending_actual_trial_not_accepted complete_or_partial_final_readout',
        'R707':'termination actual_retained_state paid_fine_prefix_artifact original_ada2_pending_identity pending_radial_nodes',
        'R705':'coarse independent damping_and_line_search', 'R711':'independent_crossed stages previous_secant_parameters',
        'R703':'independent_crossed stages actual_space frozen'}
PRIOR = re.compile(r'prior|older|inherited|brought_forward|not_counted_as_new|old_cost|preceding_centered|source_receipt|paid_R674')
COST = re.compile(r'cost|count|fees|seconds|clock|calls|factor_receipts|work$|rejections|attempts|receipts')
SCI = re.compile(r'ratio|diameter|normal_chord|attaining_pair|physical_points|max_abs_principal|max_relative_gram|actual_sigma|curl|fixed_g_eta|metric_L2|sampled_whole|metric_attainer|residual|ruling|endpoint|phi|merit|status|identity|accepted|complete|trust|damping|grid')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def enc(v):
    return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()


def get(path, output=None):
    # curl strips the authorization header on a cross-host archive/log redirect.
    cmd=['curl','--fail','--silent','--show-error','--location','--proto','=https','--proto-redir','=https',
         '--header','Authorization: Bearer '+os.environ['GH_TOKEN'],'--header','Accept: application/vnd.github+json',
         '--header','X-GitHub-Api-Version: 2022-11-28']
    if output is not None:
        cmd+=['--output',str(output)]
    p=subprocess.run(cmd+[ROOT+path],stdout=subprocess.PIPE,check=False)
    if p.returncode:
        raise RuntimeError('GitHub GET failed at '+path+' with curl status '+str(p.returncode))
    if output is None:
        return json.loads(p.stdout)


def file_sha(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f,'sha256').hexdigest()


def short(v):
    b=enc(v)
    return {'canonical_json_bytes':len(b),'canonical_json_sha256':sha(b),
            'entries':len(v) if isinstance(v,(list,dict)) else None}


def nums(v):
    if isinstance(v,list):
        if not v:
            return [0],[]
        d,arr=nums(v[0])
        flat=list(arr)
        for w in v[1:]:
            shape,row=nums(w)
            if shape!=d:
                raise ValueError('Ragged numeric field')
            flat.extend(row)
        return [len(v),*d],flat
    if type(v) not in (int,float):
        raise ValueError('Field contains non-binary64 source coordinates')
    return [],[v]


def vector(v):
    ans=short(v)
    try:
        dims,x=nums(v)
    except ValueError:
        return ans
    ans.update(shape=dims,packed_le_float64_sha256=sha(b''.join(struct.pack('<d',p) for p in x)))
    return ans


def view(v, depth=2):
    if isinstance(v,dict):
        if depth<=0:
            return short(v)
        ans={}
        for k,w in v.items():
            if isinstance(w,(dict,list)):
                if (SCI.search(k) or COST.search(k)) and depth>1:
                    ans[k]=view(w,depth-1)
            elif not isinstance(w,str) or len(w)<180:
                ans[k]=w
        return ans
    if isinstance(v,list):
        if len(v)<=12 and all(isinstance(x,(int,float,str,bool)) and len(str(x))<100 for x in v):
            return v
        if v and isinstance(v[-1],dict) and depth>0:
            return {'entries':len(v),'last_record':view(v[-1],depth-1)}
        return short(v)
    return v if not isinstance(v,str) or len(v)<300 else short(v)


def at(v,path):
    for k in path.split('.'):
        if not isinstance(v,dict) or k not in v:
            return None
        v=v[k]
    return v


def bounded(rows,limit):
    out={}
    omitted=[]
    for k,v in rows.items():
        if len(enc({**out,k:v}))<=limit:
            out[k]=v
        else:
            omitted.append(k)
    if omitted:
        out['_additional_fields_in_artifact']=len(omitted)
    return out


def summary(label,f,transports,folder):
    path=STATE[label]
    v=at(f,path)
    if v is None and label=='R643':
        path='actual_current_checkpoint.actual_response'
        v=at(f,path)
    state={'path':path,'recorded':v is not None,'value':vector(v) if v is not None else None}
    if label in ('R695','R702') and isinstance(f.get('actual_last_complete_true_state'),dict):
        state['complete_state_canonical_json']=short(f['actual_last_complete_true_state'])
        state['producer_complete_state_identity']=f.get('actual_last_complete_true_state_identity')
    if label=='R705' and v is not None:
        if state['value'].get('packed_le_float64_sha256')!=f['packed_le_float64_sha256'] or state['value']['shape']!=f['parameter_shape']:
            raise ValueError('R705 packed q or shape differs from producer')
    diag={k:view(f[k],3) for k in PICK[label].split() if k in f}
    if label=='R705':
        for key in ('coarse','independent'):
            section=f[key]
            diag[key]={k:w for k,w in section.items() if not isinstance(w,(dict,list))}
            diag[key]['per_phase']=[{k:w for k,w in p.items() if k=='phase' or SCI.search(k) and (not isinstance(w,(dict,list)) or isinstance(w,list) and len(w)<=3)} for p in section['phases']]
    if label in ('R711','R703'):
        diag['independent_crossed']={k:view(w,2) for k,w in f.get('independent_crossed',{}).items()}
    current={}
    inherited={}
    for k,w in f.items():
        if PRIOR.search(k):
            inherited[k]={'locator':k,**short(w),'readout':view(w)}
        elif COST.search(k):
            current[k]={'locator':k,**short(w),'readout':view(w)}
    for k,w in transports.items():
        inherited['event/'+k]={'locator':'paid-events.jsonl.gz/'+k,**short(w),'readout':view(w,3)}
    scalars={k:v for k,v in f.items() if not isinstance(v,(dict,list)) and (not isinstance(v,str) or len(v)<260)}
    primary={}
    if label=='R705':
        for grid in ('coarse','independent'):
            rows=f[grid]['phases']
            primary[grid]={'diameter':f[grid]['all_phase_union_sample_diameter'],
                           'support_ratio':f[grid]['support_difference_over_diameter'],
                           'phase_sigma_and_original_worst_chord':[
                               [row['phase'],row['actual_sigma'],row.get('max_two_sided_normal_chord_ratio'),row.get('attaining_pair')]
                               for row in rows]}
    elif label in ('R711','R703'):
        last=f.get('independent_crossed',{}).get('both',{})
        primary['crossed_both']={k:v for k,v in last.items() if not isinstance(v,(list,dict)) and
                                 (SCI.search(k) or 'eta' in k or 'reach' in k or 'angle' in k or 'mass' in k)}
        primary['crossed_both']=bounded(primary['crossed_both'],900)
    elif label in ('R695','R702'):
        obs=f.get('actual_last_complete_true_observation') or {}
        primary['actual_observation']=bounded(view(obs,2),800)
        primary['fine_state']=at(f,'fixed_actual_curve_refinement.state')
    elif label in ('R631','R643'):
        cp=f.get('actual_current_checkpoint') or {}
        primary['actual_checkpoint']=bounded({k:w for k,w in cp.items() if not isinstance(w,(dict,list)) and
                                              (not isinstance(w,str) or len(w)<130)},900)
    elif label=='R707':
        primary['retained_scan']=bounded(view(at(f,'actual_retained_state.scan') or {},2),900)
    full=dict(accepted_parameter=state,terminal_scalars=scalars,diagnostics=diag,original_cost_fields=inherited,current_cost_fields=current,
              cost_fields_can_overlap=True,scientific_qualification='Only original fields in the literal terminal')
    (folder/'fields.json').write_bytes(enc(full))

    def cost_compact(rows):
        return {k:w['readout'] if len(enc(w['readout']))<350 else {'entries':w['entries'],'sha256':w['canonical_json_sha256']} for k,w in rows.items()}

    return dict(accepted_parameter=state,selected_physical_readout=primary,terminal_scalars=bounded(scalars,1050),diagnostics=bounded(diag,3600),
                inherited_cost_fields=bounded(cost_compact(inherited),1400),current_cost_fields=bounded(cost_compact(current),1500),
                full_field_index_sha256=file_sha(folder/'fields.json'))


def verify(label,rid,jid,head):
    run=get(f'/actions/runs/{rid}')
    job=get(f'/actions/jobs/{jid}')
    for x in (run,job):
        if x['status']!='completed' or x['conclusion']!='success' or x['head_sha']!=head or x['run_attempt']!=1:
            raise ValueError(label+' not the fixed successful attempt')
    if (run['id']!=rid or run['repository']['full_name'].lower()!=REPO.lower() or job['id']!=jid or job['run_id']!=rid
            or not run['path'].startswith('.github/workflows/visible-'+label.lower()+'-') or not job['completed_at']):
        raise ValueError(label+' job or workflow identity mismatch')
    return job,run


def recover(target,tmpdir):
    label,rid,jid,head,marker=target
    job,run=verify(label,rid,jid,head)
    folder=OUT/label
    folder.mkdir()
    raw=Path(tmpdir)/(label+'.log')
    get(f'/actions/jobs/{jid}/logs',raw)
    raw_info={'raw_log_bytes':raw.stat().st_size,'raw_log_sha256':file_sha(raw),'job':jid,'run':rid,'head':head,
              'job_completed_at':job['completed_at'],'workflow_path':run['path']}
    (folder/'log-identity.json').write_bytes(enc(raw_info))
    final=None
    source=None
    identity=None
    events=Counter()
    transports={}
    with raw.open('rb') as lines,gzip.open(folder/'paid-events.jsonl.gz','wb',compresslevel=3) as side:
        for line in lines:
            body=STAMP.sub(b'',line.rstrip(b'\r\n'),count=1)
            tag,_,literal=body.partition(b' ')
            if marker is None and body.startswith(b'{'):
                match=KINDS.search(body)
                if not match:
                    continue
                obj=json.loads(body)
                kind=obj.get('kind')
                if kind=='terminal':
                    tag=b'JSON/terminal'
                    literal=body
                elif kind in ('transport','transported_actual_source'):
                    transports[kind]=obj
                    events[kind]+=1
                    side.write(body+b'\n')
                    continue
                else:
                    continue
            if tag==SOURCE.encode():
                if source is not None:
                    raise ValueError('Duplicate source receipt')
                (folder/'source.json').write_bytes(literal)
                source=json.loads(literal)
            elif tag==(marker or 'JSON/terminal').encode():
                if final is not None:
                    raise ValueError('Duplicate scientific terminal')
                (folder/'final.json').write_bytes(literal)
                final=json.loads(literal)
            elif tag in (b'R631_DESIGN_FINAL_IDENTITY',b'R643_COUPLED_FINAL_IDENTITY'):
                if identity is not None:
                    raise ValueError('Duplicate producer size/hash receipt')
                identity=json.loads(literal)
            elif any(tag.startswith(p.encode()) for p in SIDE.get(label,())):
                obj=json.loads(literal)
                name=tag.decode('ascii')
                events[name]+=1
                side.write(body+b'\n')
                if name in ('R705_TRANSPORT','R631_DESIGN_RESTORED','R643_COUPLED_RESTORED'):
                    transports[name]=obj
    raw.unlink()
    if not isinstance(final,dict) or not isinstance(source,dict):
        raise ValueError(label+' missing literal FINAL or producer source')
    if source['source_commit']!=head or str(source['run_id'])!=str(rid) or str(source['run_attempt'])!='1':
        raise ValueError(label+' log run/source differs from API')
    path=folder/'final.json'
    size=path.stat().st_size
    h=file_sha(path)
    if label in ('R631','R643') and (not identity or (identity['JSON_bytes'],identity['sha256'])!=(size,h)):
        raise ValueError(label+' literal FINAL differs from producer identity')
    if label=='R703' and (size,h)!=(39163,'bd5a52dcc40e31e898d3e02b99e4e5c0d449bfd697ac95faa8a168082c6012b2'):
        raise ValueError('R703 original terminal differs from previously consumed seed')
    art=get(f'/actions/runs/{rid}/artifacts?per_page=100')
    if art['total_count']!=len(art['artifacts']):
        raise ValueError('Artifact pagination exceeds this fixed batch')
    objs=[{k:a.get(k) for k in ('id','name','size_in_bytes','digest','expired','expires_at')} for a in art['artifacts']]
    if label=='R705':
        aid=15267952844
        az=folder/'original-paid-state.zip'
        wanted='d621875382f6a4fa6aff05b478f41644b4f846fdd19d8c03466da43216c1de90'
        original=next(a for a in art['artifacts'] if a['id']==aid)
        if (original['name']!='visible-r705-paid-state-46153586472-1' or original['expired']
                or original['workflow_run']['id']!=rid or original['workflow_run']['head_sha']!=head
                or original['size_in_bytes']!=494659 or original['digest']!='sha256:'+wanted):
            raise ValueError('R705 paid ZIP metadata differs')
        get(f'/actions/artifacts/{aid}/zip',az)
        if az.stat().st_size!=494659 or file_sha(az)!=wanted:
            raise ValueError('R705 paid ZIP literal differs')
    return dict(label=label,job_name=job['name'],attempt=1,marker=marker or 'JSON.kind=terminal',
                **raw_info,literal_FINAL_bytes=size,literal_FINAL_sha256=h,request_path=source['request_path'],
                request_bytes=source['request_bytes'],request_sha256=source['request_sha256'],paid_events=dict(events),
                original_artifacts=objs,**summary(label,final,transports,folder))


def main():
    start=time.monotonic()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!=REPO.lower():
        raise RuntimeError('Public recovery workflow only')
    OUT.mkdir(exist_ok=False)
    result=[]
    failures=[]
    with tempfile.TemporaryDirectory() as tmp:
        for t in TARGETS:
            then=time.monotonic()
            try:
                row=recover(t,tmp)
                result.append(row)
            except Exception as exc:
                row={'label':t[0],'type':type(exc).__name__,'message':str(exc)[:360]}
                folder=OUT/t[0]
                row['available_file_bytes']={p.name:p.stat().st_size for p in folder.glob('*') if p.is_file()}
                failures.append(row)
            row['recovery_elapsed_seconds']=time.monotonic()-then
    data={'schema':'fixed-completed-public-receipts-20261128-v1','records':result,'failures':failures,
          'new_scientific_evaluations':0,'recovery_elapsed_seconds':time.monotonic()-start}
    report=enc(data)
    if len(report)>79500:
        for row in result:
            row['diagnostics']=bounded(row['diagnostics'],1900)
        report=enc(data)
    if len(report)>79500:
        raise ValueError('Recovery readout unexpectedly exceeds 79,500 bytes')
    (OUT/'summary.json').write_bytes(report)
    print('COMPLETED_RECEIPT_SUMMARY '+report.decode(),flush=True)
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
