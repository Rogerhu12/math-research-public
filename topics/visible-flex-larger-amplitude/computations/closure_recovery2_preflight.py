#!/usr/bin/env python3
"""Read-only dependency and fresh-command preparation after executor loss.

This script never starts a numerical job.  It hashes present inputs,
reports missing material cells and prepares all three resource-wrapped
commands.  A successful process exit is not a mathematical certificate.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shlex
import sys


PREFIX='notes/2026-11-12-'
BASE={
    'columns':PREFIX+'closure-real-linear-q003-low46-recovered.json.gz',
    'ordered':PREFIX+'closure-ordered-green-low46-v2.json.gz',
    'density':PREFIX+'tail-r33-plateau2-density-window.json.gz',
    'reference':PREFIX+'closure-plateau2-reference.json',
    'box':PREFIX+'closure-plateau2-box.json',
    'ready':PREFIX+'closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json',
}


def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()


def read(path):
    b=path.read_bytes()
    return json.loads(gzip.decompress(b) if path.suffix=='.gz' else b)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--material-summary',type=Path,default=Path(PREFIX+'tail-r33-plateau2-continuous-strip-panels-summary.json'))
    p.add_argument('--high',type=Path,default=Path(PREFIX+'tail-r33-plateau2-quadratic-high-recovered-r1.json'))
    p.add_argument('--python',default='/workspace/scratch/c0de65fac774/research-venv/bin/python')
    p.add_argument('--prefix',default=PREFIX+'closure-recovery2')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError('Use a fresh preflight report path')
    records={};docs={}
    def add(path,role,expected=None):
        path=Path(path);key=str(path)
        if key not in records:
            exists=path.is_file()
            records[key]=dict(path=key,role=role,exists=exists,
                bytes=path.stat().st_size if exists else None,
                sha256=digest(path) if exists else None)
        row=records[key]
        if expected is not None:
            if row.get('expected_sha256') not in (None,expected):
                raise ValueError('Conflicting expected hashes: '+key)
            row['expected_sha256']=expected
            row['matches_expected']=row['sha256']==expected
        return row
    for role,path in BASE.items():
        if add(path,role)['exists']:docs[role]=read(Path(path))
    lift=PREFIX+'closure-plateau2-nonlinear-low-far-lift.json'
    add(lift,'exact auxiliary nonlinear low far lift')
    summary_rec=add(args.material_summary,'original or freshly recomputed complete material summary')
    material_cells=[]
    if summary_rec['exists']:
        summary=read(args.material_summary)
        for row in summary['cells']:
            rec=add(row['file'],'complete real source/strip material cell',row['sha256'])
            material_cells.append(dict(cell=row['cell'],path=row['file'],available=bool(rec['exists'] and rec['matches_expected'])))
        for path,h in summary.get('input_hashes',{}).items():add(path,'material-summary input',h)
        for name,h in summary.get('source_hashes',{}).items():add(Path('computations')/name,'material generator dependency',h)
    if 'columns' in docs:
        for row in docs['columns']['column_groups']:add(row['path'],'true signed column group',row['sha256'])
    for role in ('columns','ordered','reference','box'):
        for path,h in docs.get(role,{}).get('input_hashes',{}).items():
            # Only declared runtime files are checked, never inferred or fetched.
            add(path,role+' provenance input',h)
    sources=[
        'closure_weighted_panel_flow_v4.py','closure_panel_centred_low_green_v2.py',
        'closure_assemble_centred_green.py','closure_joint_head_box_reduced.py',
        'closure_weighted_panel_low_green_v3.py','closure_real_head_source_enclosure.py',
        'closure_real_linear_head_enclosure.py','closure_real_head_green_enclosure.py',
        'closure_projective_interval_column.py','strong_resource_run.py']
    for name in sources:add(Path('computations')/name,'frozen runtime source')
    high_rec=add(args.high,'fresh complete quadratic high response required by the joint check')
    if high_rec['exists']:
        high=read(args.high)
        if high.get('gamma_source'):
            path=high['gamma_source']
            add(path,'complete middle causal kernel',high.get('input_hashes',{}).get(path))
    panel_prefix=args.prefix+'-centred-panels-low46-r1'
    green_prefix=args.prefix+'-centred-four-green-r1'
    joint_prefix=args.prefix+'-full-frequency-joint-r1'
    common=[]
    for key,value in BASE.items():common+=['--'+key,value]
    panel=[args.python,'computations/closure_panel_centred_low_green_v2.py',*common,
        '--panels-summary',str(args.material_summary),'--out-prefix',panel_prefix]
    assembly=[args.python,'computations/closure_assemble_centred_green.py',*common,
        '--panel-summary',panel_prefix+'-summary.json','--low-far-lift',lift,
        '--out-prefix',green_prefix]
    joint=[args.python,'computations/closure_joint_head_box_reduced.py',
        '--low',green_prefix+'.json.gz','--high',str(args.high),
        '--density',BASE['density'],'--out',joint_prefix+'.json.gz']
    def wrapped(command,prefix):
        return [args.python,'computations/strong_resource_run.py','--out',prefix+'-resource.json','--',*command]
    steps=[]
    for number,name,command,prefix in (
        (1,'all12 real46 panel cells',panel,panel_prefix),
        (2,'all213 four-family directed matrices',assembly,green_prefix),
        (3,'214 proposal solves and original428 direct gates',joint,joint_prefix)):
        matches=sorted(str(x) for x in Path(prefix).parent.glob(Path(prefix).name+'*'))
        argv=wrapped(command,prefix)
        steps.append(dict(step=number,name=name,argv=argv,shell_command=shlex.join(argv),
            output_prefix=prefix,prefix_is_fresh=not matches,existing_outputs=matches,
            started=False,resource_authorization='Wait for the parent-exclusive numerical window; this report does not launch a process.'))
    unavailable=[r for r in records.values() if not r['exists'] or r.get('matches_expected') is False]
    result=dict(status='Static dependency report and exact fresh command preparation; no numerical execution',
        author='exact_closure (GPT-6 Astra Pro, AI-assisted)',material_cells=material_cells,
        all12_material_cells_present_and_hashed=len(material_cells)==12 and all(r['available'] for r in material_cells),
        material_cell_coverage=[r['cell'] for r in material_cells],
        inputs=list(records.values()),unavailable_or_changed=unavailable,steps=steps,
        python_path=args.python,python_exists=Path(args.python).is_file(),
        joint_high_path=str(args.high),fresh_high_available=high_rec['exists'],
        source_sha256=digest(Path(__file__)),preflight_python=sys.executable,
        mathematical_gates_evaluated=False,old_joint90734_final_state='Unknown; only matrix assembly was observed before executor replacement.',
        recompute_policy='All unpushed numerical outputs must be produced afresh, including the complete panel chain and high response.')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),records=len(records),
        missing_or_changed=len(unavailable),material_cells_available=sum(r['available'] for r in material_cells),
        all_output_prefixes_fresh=all(s['prefix_is_fresh'] for s in steps)),indent=2))


if __name__=='__main__':main()
