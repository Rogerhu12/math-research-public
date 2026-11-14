#!/usr/bin/env python3
"""Close a completed actual step; publish last state, not repeated normal tiles.

This is storage/reporting only. It never evaluates the field, residual,
Jacobian, or a direction, and does not remove any original artifact.
"""
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path


def identity(path):
    path=Path(path)
    return dict(path=str(path),bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def write_new(path,value):
    if path.exists():raise FileExistsError(path)
    path.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    return path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request',type=Path,required=True)
    parser.add_argument('--direction-id',required=True)
    parser.add_argument('--extra',type=Path,action='append',default=[])
    args=parser.parse_args()
    request=json.loads(args.request.read_text())
    prefix=Path(request['run_prefix']);root=Path(request['cache_dir'])
    stem=prefix.name;notes=prefix.parent
    target=prefix.with_name(stem+'-closed-manifest.json')
    if target.exists():raise FileExistsError(target)
    accepted=json.loads((root/'accepted-result.json').read_text())
    if not accepted.get('accepted') or not accepted.get('actual_full_residual_evaluated'):
        raise ValueError('Only a saved actual full-F accepted step may use this closer')
    field=Path(accepted['accepted_state']['path'])
    if identity(field)['sha256']!=accepted['accepted_state']['sha256']:
        raise ValueError('Accepted field changed')
    direction_path=root/'directions'/args.direction_id/'summary.json'
    direction=json.loads(direction_path.read_text())
    if direction['direction_id']!=accepted['direction_id']:
        raise ValueError('Close only the actual accepted direction; other diagnostics stay separate')
    trials=[]
    for path in sorted((root/'trials'/args.direction_id).glob('back-*.json')):
        row=json.loads(path.read_text());alpha=float(row['alpha'])
        baseline_squared=2*float(row['baseline_cost'])
        slope=float(row['merit_directional_derivative'])
        full=float(direction['information']['linear_residual_squared_unclamped'])
        Jd_squared=full-baseline_squared-2*slope
        predicted=.5*(baseline_squared+2*alpha*slope+alpha*alpha*Jd_squared)
        decrease=float(row['baseline_cost'])-predicted
        trials.append(dict(result=identity(path),alpha=alpha,accepted=row['accepted'],
            actual_full_residual_evaluated=row['actual_full_residual_evaluated'],
            actual_norm=row.get('objective_norm'),actual_cost=row.get('actual_cost'),
            rejection=row.get('rejection'),normal_model_cost=predicted,
            actual_to_model_decrease_ratio=((row['baseline_cost']-row['actual_cost'])/decrease
                if row.get('actual_full_residual_evaluated') and decrease>0 else None)))
    receipts=[]
    for path in sorted(notes.glob(stem+'*-process-receipt.json')):
        row=json.loads(path.read_text())
        receipts.append(dict(identity(path),actual_child_returncode=row.get('actual_child_returncode'),
            seconds=row.get('seconds'),peak_rss_kib=row.get('kernel_child_maximum_resident_KiB')))
    tiles=[]
    for path in sorted((root/'normal-tiles').glob('*/manifest.json')):
        row=json.loads(path.read_text())
        tiles.append(dict(id=path.parent.name,manifest=identity(path),schema=row['schema'],
            logical_manifest=row.get('logical_manifest'),
            logical_numerical_bytes=row.get('logical_numerical_bytes'),
            compressed_numerical_bytes=row.get('compressed_numerical_bytes')))
    normal_path=root/'normal-partitioned/manifest.json'
    normal=json.loads(normal_path.read_text())
    summary=write_new(prefix.with_name(stem+'-closed-summary.json'),dict(
        schema='fd2d-staged-actual-accepted-step-summary-v1',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        request=identity(args.request),input=identity(request['settings']['warm_start']),
        accepted=accepted['accepted_state'],actual_norm=accepted['objective_norm'],
        diagnostics=accepted['diagnostics'],locations=accepted['locations'],trials=trials,
        complete_normal=identity(normal_path),actual_process_receipts=receipts,
        numerical_calculations_in_closure=0,strong_target_complete=False,
        continuous_geometry_certificate=False,source=identity(__file__)))
    inventory=write_new(prefix.with_name(stem+'-reproducible-cache-inventory.json'),dict(
        schema='fd2d-regenerable-normal-cache-inventory-v2',complete_normal_manifest=identity(normal_path),
        normal_pieces=normal['pieces'],tiles=tiles,
        matrix_pieces_in_publication=False,original_files_unchanged=True,
        note='Request, frozen sources, plan, true baseline and deterministic row order reproduce these intermediate matrices.'))
    files={summary,inventory,args.request,field,root/'accepted-result.json',direction_path,
           Path(direction['direction']['path']),normal_path,
           root/'normal-reference.json',root/'normal-partition-plan.json',
           root/'normal-partitioned-summary.json',root/'baseline-summary.json',Path(__file__)}
    for stage in ('baseline-adoption','plan-a01','compressed-controller-a01','compressed-merge-a01',
                  'schur-a01','qp-a01','trial-back00-a01','trial-back01-a01','trial-back02-a01'):
        for suffix in ('-report.json','-progress.jsonl','-process-receipt.json'):
            path=prefix.with_name(stem+'-'+stage+suffix)
            if path.is_file():files.add(path)
    for path in (root/'trials'/args.direction_id).glob('back-*.json'):files.add(path)
    for path in (root/'accepted-values').rglob('*'):
        if path.is_file():files.add(path)
    for path in notes.glob(stem+'-trial-*-physical-metric.json'):files.add(path)
    factor=direction['saved_Schur_summary']
    files.add(Path(factor['path']))
    files.update(args.extra)
    compression=[]
    for path in sorted(files.copy()):
        if path.stat().st_size>=1_000_000:
            raw=path.read_bytes();compressed=path.with_name(path.name+'.gz')
            if compressed.exists():
                if gzip.decompress(compressed.read_bytes())!=raw:raise ValueError('Existing gzip differs')
            else:compressed.write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
            if gzip.decompress(compressed.read_bytes())!=raw:raise ValueError('Gzip roundtrip differs')
            compression.append(dict(original=identity(path),gzip=identity(compressed),restore_original_path_before_original_loader=True))
            files.remove(path);files.add(compressed)
    pack=write_new(prefix.with_name(stem+'-publication-compression.json'),dict(
        schema='fd2d-lossless-publication-compression-v1',entries=compression,originals_retained_locally=True))
    files.add(pack)
    rows=[identity(path) for path in sorted(files)]
    if max(row['bytes'] for row in rows)>=5_000_000:raise ValueError('An artifact exceeds the publication limit')
    write_new(target,dict(schema='fd2d-closed-research-artifact-manifest-v1',closed=True,
        scope='Frozen input, completed original actual step, necessary accepted value packet, compact execution and regenerable matrix inventory; excludes other direction diagnostics and later active runs',
        accepted_state_sha256=accepted['accepted_state']['sha256'],
        actual_final_objective_norm=accepted['objective_norm'],strong_target_complete=False,files=rows))
    print(json.dumps(dict(manifest=identity(target),files=len(rows),bytes=sum(r['bytes'] for r in rows),
                         maximum=max(r['bytes'] for r in rows))))


if __name__=='__main__':main()
