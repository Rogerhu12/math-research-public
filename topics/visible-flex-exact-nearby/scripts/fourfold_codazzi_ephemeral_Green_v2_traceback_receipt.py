#!/usr/bin/env python3
"""Read one failed public job; emit only its provenance and short traceback."""
from __future__ import annotations
import base64,datetime,hashlib,json,os,subprocess,urllib.error,urllib.parse,urllib.request
from pathlib import Path

REPOSITORY='Rogerhu12/math-research-public'
RUN,ATTEMPT,JOB=43681612825,1,132713247491
SOURCE='f33345d1ab2500fd3811692311ce931606e389cf3c8ef508925d225748565190'
PROCESS_PATH=('topics/visible-flex-exact-nearby/notes/ephemeral_parallel_matrix_Green_Poisson_v2_ci/'
    'run-43681612825-1-ephemeral-parallel-matrix-Green-Poisson-v2/process.json')
PROCESS_REF='6c76caf431fb841f653dd1f01a792fc3555f1c2f'
PROCESS_SHA='0b2e08152feee47b47666e2bc03a1b3e535e2389891e26a0674014d3a2fef4ba'
RULES={
    'README.md':'c6db597c32b022d46d861463e32ad7160545e088610916339bd47e1acae74970',
    'topics/visible-flex-exact-nearby/README.md':'81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220',
}
API='https://api.github.com/repos/'+REPOSITORY
TOKEN=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
if not TOKEN:raise RuntimeError('the public Actions read token is absent')

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):return None

def api(path):
    request=urllib.request.Request(API+path,headers={
        'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json',
        'X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.build_opener(NoRedirect()).open(request,timeout=120) as response:
        return response.read()

def git(*args):
    return subprocess.check_output(['git',*args],stderr=subprocess.STDOUT,text=True,timeout=180)

def review():
    before=git('rev-parse','HEAD').strip()
    prior={p:Path(p).read_bytes() for p in RULES}
    pull=git('pull','--ff-only','origin','main')
    after=git('rev-parse','HEAD').strip()
    checks=[]
    for path,expected in RULES.items():
        raw=Path(path).read_bytes()
        difference=git('diff',before,after,'--',path)
        checks.append(dict(path=path,before_sha256=digest(prior[path]),
            after_sha256=digest(raw),actual_diff=difference,
            actual_diff_sha256=digest(difference.encode()),reviewed_expected_sha256=expected))
        if digest(raw)!=expected:raise ValueError('a README changed beyond the explicitly reviewed rules: '+path)
    return dict(utc=now(),before_commit=before,after_commit=after,actual_pull_output=pull,checks=checks)

def original_log():
    request=urllib.request.Request(API+'/actions/jobs/'+str(JOB)+'/logs',headers={
        'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json'})
    try:
        with urllib.request.build_opener(NoRedirect()).open(request,timeout=120) as response:
            return response.read()
    except urllib.error.HTTPError as error:
        if error.code not in (301,302,303,307,308):raise
        location=error.headers.get('Location','')
        parsed=urllib.parse.urlsplit(location)
        if parsed.scheme!='https' or not parsed.hostname:
            raise ValueError('the original public job log redirect is not HTTPS')
        # Never forward GitHub credentials to the log-storage host.
        with urllib.request.urlopen(urllib.request.Request(location),timeout=120) as response:
            return response.read()

def traceback_evidence(text):
    lines=text.splitlines()
    anchors=[i for i,line in enumerate(lines)
        if ('nonfinite exact dyadic slack' in line or
            'Traceback (most recent call last)' in line or
            'actual temporary consumer-0 child failed' in line)]
    windows=[]
    for i in anchors:
        left=max(0,i-25);right=min(len(lines),i+12)
        if windows and left<=windows[-1][1]:
            windows[-1]=(windows[-1][0],max(windows[-1][1],right))
        else:windows.append((left,right))
    evidence=[dict(first_original_line=l+1,last_original_line=r,
        excerpt='\n'.join(lines[l:r])) for l,r in windows]
    if len(json.dumps(evidence,ensure_ascii=False).encode())>20000:
        # Selected traceback evidence, not chunks for reconstructing a log.
        evidence=[]
        for i,line in enumerate(lines):
            if any(word in line for word in ('Traceback (most recent call last)',
                'File "','ArithmeticError:','RuntimeError:','exact_upper_float',
                'weighted_add(','covariance_bound(','put_cov(','sandwich(')):
                evidence.append(dict(original_line=i+1,text=line))
        if len(json.dumps(evidence,ensure_ascii=False).encode())>20000:
            raise ValueError('necessary traceback evidence exceeds20000bytes; do not split')
    return evidence

def main():
    started=now();first=review()
    run=json.loads(api('/actions/runs/'+str(RUN)))
    job=json.loads(api('/actions/jobs/'+str(JOB)))
    if (run['id']!=RUN or run['run_attempt']!=ATTEMPT or run['conclusion']!='failure'
        or job['id']!=JOB or job['run_id']!=RUN or job['conclusion']!='failure'):
        raise ValueError('the original failed run/job identity changed')
    original=json.loads(api('/contents/'+urllib.parse.quote(PROCESS_PATH,safe='/')+'?ref='+PROCESS_REF))
    rawprocess=base64.b64decode(original['content'])
    if digest(rawprocess)!=PROCESS_SHA:raise ValueError('original failed process SHA mismatch')
    process=json.loads(rawprocess)
    if process.get('actual_source_sha256')!=SOURCE:
        raise ValueError('the original scientific source differs')
    children=process.get('children',[])
    if not any(c.get('actual_returncode')==1 for c in children):
        raise ValueError('the original actual mathematical child1 is absent')
    raw=original_log();text=raw.decode('utf-8')
    if 'nonfinite exact dyadic slack' not in text:
        raise ValueError('the observed actual failure is absent from the original job log')
    result=dict(kind='actual_failed_Green_v2_traceback_receipt_only',
        repository=REPOSITORY,original_run_id=RUN,original_run_attempt=ATTEMPT,original_job_id=JOB,
        started_utc=started,finished_utc=now(),new_mathematical_calls=0,
        new_native_data=False,new_Actions_artifacts=False,new_Release_uploads=False,
        original_source_sha256=SOURCE,original_process_path=PROCESS_PATH,
        original_process_ref=PROCESS_REF,original_process_bytes=len(rawprocess),
        original_process_sha256=PROCESS_SHA,original_log_bytes=len(raw),
        original_log_sha256=digest(raw),original_actual_children=children,
        original_failure=process.get('actual_scientific_failure'),
        original_progress=process.get('actual_temporary_progress'),
        selected_traceback_evidence=traceback_evidence(text),actual_readme_reviews=[first,review()])
    encoded=(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()
    if len(encoded)>60000:raise ValueError('the genuine whole receipt exceeds60000bytes')
    print(encoded.decode(),flush=True)
    fence=chr(96)*3
    Path(os.environ['GITHUB_STEP_SUMMARY']).write_text(
        '## Actual failed Green v2 traceback receipt\n\n'+fence+'json\n'+encoded.decode()+fence+'\n',
        encoding='utf-8')

if __name__=='__main__':main()
