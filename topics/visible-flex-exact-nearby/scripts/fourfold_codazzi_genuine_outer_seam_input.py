"""Recover the single necessary whole one-sided 193-direction cubic, under its original native SHA."""
from argparse import ArgumentParser
from hashlib import sha256
from pathlib import Path
import ast
import importlib.util
import json
import os
import subprocess
import sys

TOPIC='topics/visible-flex-exact-nearby'
TC=TOPIC+'/notes/2026-11-28-true-root-trial-complete2677-inputs.json'
TC_SHA='6b82d09170ed4ec780eccd0910cb69df98615390ef2f73237ed324d1e3f2c692'
CURRENT='fa24312d2388f164c2e9cb5dd4014d2a83d09ce5'
NATIVE='3484712c492440e15bfd15607b5e66aa317288bd0271710cca7cc5ec82ce9402'


def require(ok,msg):
    if not ok:raise ValueError(msg)


def inputs(repo,target):
    require(os.environ['GITHUB_ACTIONS']=='true' and os.environ['GITHUB_REPOSITORY']=='Rogerhu12/math-research-public'
            and os.environ['GITHUB_RUN_ATTEMPT']=='1','sole authorized original carrier restoration')
    def fetch(rev,path):return subprocess.check_output(['git','show',rev+':'+path],cwd=repo)
    raw=fetch(CURRENT,TC)
    require(sha256(raw).hexdigest()==TC_SHA,'whole original 184+32 scientific descriptor')
    tc=json.loads(raw);roles=tc['roles'];plan=tc['input_restoration']
    allspec={x['path']:x for x in tc['files']+tc['historical_inputs']}
    require(len(tc['files'])==184 and len(tc['historical_inputs'])==32 and
            plan['verified_runtime']['CORETYPE']=='SkylakeX' and plan['original_cubic_sha256']==NATIVE
            and plan['original_nodal_answer_sha256']=='5d69eabc45757f91a4739c58114310c5534ac1a84e01e54233188dfffa567b1c',
            'exact previously qualified whole nodal and cubic identity')
    table={k:allspec[p] for k,p in roles.items()}
    paths={plan[k] for k in ('object','q_vector','waist_row','nodal_manifest','reconstructor')}
    directory=Path(plan['nodal_manifest']).parent
    paths.update(str(directory/k) for k in ('response-finite-native.json','response-nonmean.json'))
    required=['base_index','direction_index','restoration_helper','original_TCX_restoration_helper',
              'verified_runtime_actual','verified_runtime_execution','verified_runtime_manifest']
    required.extend('base_part%03d'%k for k in range(5))
    required.extend('nodal_response_%d'%k for k in range(3))
    required.extend(('original_geometry_direction','original_geometry_origin_inputs'))
    paths.update(roles[k] for k in required)
    scripts={Path(s).stem:s for s in allspec if s.startswith(TOPIC+'/scripts/') and s.endswith('.py')}
    seen=set();root=target/'source';receipts=[]
    while paths:
        p=paths.pop()
        if p in seen:continue
        seen.add(p);spec=allspec[p];rev=spec.get('commit',CURRENT)
        b=fetch(rev,p)
        require((len(b),sha256(b).hexdigest())==(spec['bytes'],spec['sha256']), 'whole exact original '+p)
        if 'git_blob_sha' in spec:
            import hashlib
            require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==spec['git_blob_sha'],
                    'same original git object')
        dst=root/p;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(b)
        receipts.append([rev,p,len(b),spec['sha256']])
        if p.endswith('.py'):
            for n in ast.walk(ast.parse(b,filename=p)):
                names=[n.module] if isinstance(n,ast.ImportFrom) else [a.name for a in n.names] if isinstance(n,ast.Import) else []
                paths.update(scripts[k.split('.')[0]] for k in names if k and k.split('.')[0] in scripts)
    path=root/roles['restoration_helper']
    cfg=importlib.util.spec_from_file_location('_GJO_exact_old_nodal_direction',path)
    helper=importlib.util.module_from_spec(cfg);cfg.loader.exec_module(helper)
    st={};tmp=target/'private';tmp.mkdir(parents=True,exist_ok=True)
    report=helper.reconstruct_direction(plan,root,tmp,table,st)
    cubic=tmp/'reconstruct-work'/'trial-cubic.npy'
    digest=sha256(cubic.read_bytes()).hexdigest()
    require(report['complete'] and report['whole_original_cubic_SHA_verified'] and
            report['old_QR_solve_called'] is False and report['old_residual_or_norm_targets_called']==0
            and len(report['complete_direction_input_receipts'])==14 and digest==NATIVE,'whole qualified cubic and all 14 shards')
    info=dict(cubic=str(cubic.resolve()),bytes=cubic.stat().st_size,sha256=digest,
              original_nodal_sha256=plan['original_nodal_answer_sha256'],
              receipt_count=len(receipts),original_inputs_sha256=sha256(json.dumps(sorted(receipts),separators=(',',':')).encode()).hexdigest(),
              all14=report['complete_direction_input_receipts'],no_old_science=True)
    (target/'original-direction.json').write_text(json.dumps(info,sort_keys=True,separators=(',',':'))+'\n')
    print('GJO_ORIGINAL_RAW_CUBIC',info['bytes'],digest,'original_files',len(receipts),'restore_only',flush=True)


if __name__=='__main__':
    ap=ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--target',type=Path,required=True)
    a=ap.parse_args();inputs(a.repo,a.target)
