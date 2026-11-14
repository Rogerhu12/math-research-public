#!/usr/bin/env python3
"""Compute disjoint actual forward leaves from the unchanged exact cache.

Every g0 leaf and expanded parameter proof has a separate process lifetime.
This orchestration never declares a block to be the complete 550-segment
return. It invokes the existing complete arithmetic kernels, preserves every
failed attempt, and writes a portable manifest of completed same-object leaves.
The final chronological merge must retain all cross-block Fourier terms.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gc
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import traceback

BASE=Path('data/phase_ring_continuation')
DESCRIPTOR=BASE/'step5_retargeted_reference/descriptor.json'
COVER=BASE/'type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_forward.json.gz'
G0=Path('scripts/fourfold_forward_density_pipeline_composition_v9.py')
PRECOMPUTE=Path('scripts/fourfold_parameter_precompute_expanded_domain.py')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path,value):
    path=Path(path);temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value,indent=2)+'\n');temporary.replace(path)


def run_child(command,log):
    print('RUN',command,flush=True)
    with Path(log).open('w') as stream:
        result=subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'))
    if result.returncode:
        print(Path(log).read_text()[-6000:],flush=True)
        raise RuntimeError('actual arithmetic child failed; its report and log are retained: '+str(log))


def inventory(directory):
    rows=[]
    for path in sorted(Path(directory).rglob('*')):
        if path.is_file() and path.name not in ('block-manifest.json','files.json'):
            rows.append(dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path)))
    return rows


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--start',type=int,required=True);p.add_argument('--stop',type=int,required=True)
    p.add_argument('--run-tag',default='local')
    p.add_argument('--parameter-pipeline',type=Path,
        default=Path('scripts/fourfold_parameter_density_pipeline_efficient_v5.py'))
    p.add_argument('--only-g0',action='store_true')
    p.add_argument('--plan-only',action='store_true')
    a=p.parse_args()
    if not 0<=a.start<a.stop<=550 or not re.fullmatch(r'[A-Za-z0-9_.-]+',a.run_tag):
        raise ValueError('invalid actual block interval or output tag')
    directory=BASE/'step5_ci_forward_blocks'/a.run_tag/('block_%04d_%04d'%(a.start,a.stop))
    directory.mkdir(parents=True,exist_ok=True)
    logs=directory/'logs';logs.mkdir(exist_ok=True)
    report_path=directory/'block-manifest.json'
    started=time.monotonic()
    report=dict(kind='actual_independent_forward_density_block',complete=False,
        source_sha256=sha(__file__),source_commit=os.environ.get('GITHUB_SHA'),
        requested_segment_interval=[a.start,a.stop],run_tag=a.run_tag,
        descriptor_sha256=sha(DESCRIPTOR),field_cover_sha256=sha(COVER),
        g0_pipeline_path=str(G0),g0_pipeline_sha256=sha(G0),
        parameter_pipeline_path=str(a.parameter_pipeline),
        parameter_pipeline_sha256=sha(a.parameter_pipeline),
        parameter_precompute_source_sha256=sha(PRECOMPUTE),
        full_forward_leg_claimed=False,actual_R31_accepted=False,
        final_global_cross_block_terms_still_required=True,leaves=[])
    save(report_path,report)
    try:
        from flint import ctx
        from fourfold_saved_circle_field_multidomain_budget import read
        from fourfold_phase_domain_cover_verify import Closure
        from fourfold_retarget_reference_jets import RetargetReference
        from fourfold_forward_density_cover_v6 import load_cover,exact_case_leaves,check_reference_seams
        from fourfold_phase_unified_scalar_time_circle import exact_time
        ctx.prec=320;ctx.cap=24
        reference=RetargetReference(DESCRIPTOR)
        closure=Closure(Path.cwd(),reference.doc['target_object']['sha256'],reference.doc['target_root']['sha256'])
        grid=read(reference.doc['old_forward_reference']['path'])
        check_reference_seams(Path('notes/2026-11-12-step5-forward-reference-derivative-complete-summary.json'),
                              DESCRIPTOR,reference)
        cover,cases=load_cover(COVER,DESCRIPTOR,reference,closure)
        if len(cases)!=550 or any(('forward',segment) not in cases for segment in range(550)):
            raise ValueError('the full original field-domain partition is absent')
        leaves=[]
        for segment in range(a.start,a.stop):
            leaves.extend(exact_case_leaves(cases[('forward',segment)],cover,grid,closure))
        report['requested_exact_domain_leaves']=[dict(path=str(row[2]),sha256=row[3]) for row in leaves]
        save(report_path,report)
        if a.plan_only:
            report.update(plan_only=True,requested_domain_partition_proved=True,
                          wall_seconds=time.monotonic()-started)
            save(report_path,report)
            print(dict(plan_only=True,requested_segments=[a.start,a.stop],
                       proved_domain_leaves=len(leaves),actual_flow_completion=False),flush=True)
            return 0
        g0_directory=directory/'g0'
        # Each true leaf owns a fresh native process. The original v9 index
        # and ordered accumulator remain single-leaf objects, not a fabricated
        # block chronological sum. The independent block index lists all leaves.
        g0_index=dict(kind='actual_independent_block_zero_order_leaf_inventory',
            source_sha256=sha(__file__),complete=False,leaves=[],
            cross_leaf_ordered_integrals_not_computed_here=True)
        g0_block_index=directory/'g0-block-leaf-index.json'
        for number,domain in enumerate(leaves):
            tag='%04d_%04d'%(read(domain[2])['segment'],number)
            run_child([sys.executable,'-u',str(G0),'--domains',str(domain[2]),
                '--out-directory',str(g0_directory),'--primitive-nodes','640','--root-nodes','1024',
                '--expanded-domain-directory',str(directory/'expanded-field'),
                '--target','1e-20','--bits','320','--resume'],logs/('g0_'+tag+'.log'))
            one=read(g0_directory/'index.json')
            if not one.get('complete') or len(one['leaves'])!=1:
                raise ValueError('requested actual single zero-order leaf did not complete')
            if number==0:g0_index['exact_initial_time']=one['exact_initial_time']
            elif exact_time(g0_index['exact_final_time'])!=exact_time(one['exact_initial_time']):
                raise ValueError('isolated actual zero-order leaves have a chronological gap')
            g0_index['exact_final_time']=one['exact_final_time']
            g0_index['leaves'].append(one['leaves'][0])
            save(g0_block_index,g0_index)
        g0_index['complete']=len(g0_index['leaves'])==len(leaves)
        save(g0_block_index,g0_index)
        report['g0_leaf_inventory_path']=str(g0_block_index)
        report['g0_leaf_inventory_sha256']=sha(g0_block_index)
        if not g0_index['complete']:
            raise ValueError('not all requested actual zero-order leaves completed')
        report['complete_requested_g0_block']=True
        report['exact_begin']=g0_index['exact_initial_time'];report['exact_end']=g0_index['exact_final_time']
        if (exact_time(report['exact_begin'])!=exact_time(grid['exact_time_endpoints'][a.start])
            or exact_time(report['exact_end'])!=exact_time(grid['exact_time_endpoints'][a.stop])):
            raise ValueError('the actual block does not have its declared exact endpoints')
        save(report_path,report)
        for row,domain in zip(g0_index['leaves'],leaves):
            path=Path(row['path']);g0=read(path)
            if (sha(path)!=row['sha256'] or g0['domain_sha256']!=domain[3]
                or not g0.get('complete_continuous_true_density_proved')):
                raise ValueError('completed actual g0 identity changed')
            item=dict(segment=row['segment'],normalized_subspan=row['normalized_subspan'],
                domain_path=str(domain[2]),domain_sha256=domain[3],
                g0_report_path=str(path),g0_report_sha256=sha(path))
            for scope in ([] if a.only_g0 else ['center','uniform']):
                target='1e-9' if scope=='center' else '1e-7'
                half_width='0' if scope=='center' else '1/1000000000'
                stem=path.name.removesuffix('.json.gz')+'_'+scope
                out=directory/(stem+'.json.gz')
                command=[sys.executable,'-u',str(a.parameter_pipeline),'--descriptor',str(DESCRIPTOR),
                    '--domain',str(domain[2]),'--reference-certificate',str(path),
                    '--reference-source',str(G0),'--uniform-half-width',half_width,
                    '--target',target,'--primitive-nodes','384','--root-nodes','1024',
                    '--bits','256','--coefficient-bits','160','--directory',str(directory/stem),
                    '--expanded-domain-directory',str(directory/'expanded-field'),
                    '--parameter-proof-directory',str(directory/'expanded-parameter'),
                    '--parameter-proof-lock-directory',str(directory/'locks'),
                    '--out',str(out)]
                if scope=='uniform':command.append('--second-only')
                if not (out.exists() and read(out).get('complete')):
                    precompute=directory/(stem+'_precompute.json')
                    run_child([sys.executable,'-u',str(PRECOMPUTE),
                        '--domain',str(domain[2]),'--descriptor',str(DESCRIPTOR),
                        '--uniform-half-width',half_width,
                        '--expanded-domain-directory',str(directory/'expanded-field'),
                        '--parameter-proof-directory',str(directory/'expanded-parameter'),
                        '--parameter-proof-lock-directory',str(directory/'locks'),
                        '--expanded-proof-nodes','512','--root-nodes','1024',
                        '--log-directory',str(logs/'parameter-proof'),
                        '--out',str(precompute)],logs/(stem+'_precompute.log'))
                    item[scope+'_precompute_report_path']=str(precompute)
                    item[scope+'_precompute_report_sha256']=sha(precompute)
                    run_child(command,logs/(stem+'.log'))
                param=read(out)
                if (not param.get('complete_continuous_parameter_densities_proved')
                    or param['source_sha256']!=sha(a.parameter_pipeline)
                    or param['reference_certificate_sha256']!=sha(path)
                    or param['identity']['reference']!=g0['identity']['reference']
                    or param['identity']['whole_real_parameter_tube']!=(scope=='uniform')):
                    raise ValueError('completed actual parameter identity differs')
                for name,digest in param['dependency_sha256'].items():
                    if sha(Path('scripts')/name)!=digest:
                        raise ValueError('actual parameter dependency changed: '+name)
                item[scope+'_report_path']=str(out);item[scope+'_report_sha256']=sha(out)
            report['leaves'].append(item);save(report_path,report)
            print('COMPLETED_ACTUAL_LEAF',row['segment'],row['normalized_subspan'],flush=True)
            gc.collect()
        report['complete']=True
        report['only_zero_order_requested']=a.only_g0
        report['complete_center_and_uniform_g2_block']=not a.only_g0
    except Exception as exc:
        report.update(failure=type(exc).__name__+': '+str(exc),traceback=traceback.format_exc())
    report['wall_seconds']=time.monotonic()-started
    save(report_path,report)
    save(directory/'files.json',dict(kind='completed_or_failed_actual_block_file_inventory',
         block_manifest_sha256=sha(report_path),files=inventory(directory)))
    print({k:report.get(k) for k in ('complete','complete_requested_g0_block','failure','wall_seconds')},flush=True)
    return 0 if report['complete'] else 2


if __name__=='__main__':raise SystemExit(main())
