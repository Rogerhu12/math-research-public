#!/usr/bin/env python3
"""Losslessly retire only completed own normal tiles after their complete merge.

Every old byte remains in a verified gzip capsule. No mathematical object is
changed, and the complete merged normal is read-only. The old tile directory
can be restored with fd2d_gc_normal_capsule.restore_normal_capsule.
"""
import argparse,datetime,json,shutil
from pathlib import Path
from fd2d_gc_normal_capsule import create_normal_capsule,stream_identity,stream_inflate
from fd2d_gc_stage_io import atomic_json


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('plan','tile-root','archive-root','complete-normal-manifest','report'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--retire-uncompressed',action='store_true')
    args=ap.parse_args()
    if args.report.exists():raise FileExistsError('Use a separate report for an actual recovery attempt')
    plan=json.loads(args.plan.read_text());complete=json.loads(args.complete_normal_manifest.read_text())
    if not complete['complete'] or complete['binding']['plan_sha256']!=plan['plan_sha256']:
        raise ValueError('Only tiles of the supplied complete merged normal may be retired')
    if complete['binding']['ordered_tile_ids']!=[d['id'] for d in plan['tiles']]:
        raise ValueError('The merged normal does not bind the complete tile ledger')
    report=dict(schema='fd2d-lossless-own-closed-tile-retirement-v1',complete=False,
        source=stream_identity(__file__),plan=stream_identity(args.plan),
        complete_merged_normal=stream_identity(args.complete_normal_manifest),
        merged_normal_modified=False,retire_uncompressed=args.retire_uncompressed,
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),tiles=[])
    atomic_json(args.report,report)
    for descriptor in plan['tiles']:
        name=descriptor['id'];old=args.tile_root/name;archive=args.archive_root/name
        index=archive/'index.json'
        if not index.exists():
            raw_manifest=old/'manifest.json';raw=json.loads(raw_manifest.read_text())
            if raw['binding']['common']!=complete['binding']['common'] or raw['binding']['descriptor']!=descriptor:
                raise ValueError('Old tile mathematical identity differs: '+name)
            index=create_normal_capsule(raw_manifest,archive,
                expected_manifest_sha256=stream_identity(raw_manifest)['sha256'])
        packed=json.loads(index.read_text())
        original=archive/packed['original_manifest']['file'];raw=json.loads(original.read_text())
        if not packed['complete'] or stream_identity(original)!=dict(bytes=packed['original_manifest']['bytes'],sha256=packed['original_manifest']['sha256']):
            raise ValueError('Incomplete archived tile: '+name)
        if raw['binding']['common']!=complete['binding']['common'] or raw['binding']['descriptor']!=descriptor:
            raise ValueError('Archived tile mathematical identity differs: '+name)
        for row in packed['pieces']:
            piece=archive/row['compressed_file']
            if stream_identity(piece)!=row['compressed']:raise ValueError('Archived compressed bytes differ')
            stream_inflate(piece,row['original'])
        before=0
        if old.exists():
            allowed={'manifest.json'}|{r['file'] for r in raw['pieces']}
            if {q.name for q in old.iterdir()}!=allowed:raise ValueError('Unexpected file in the own closed tile directory')
            if stream_identity(old/'manifest.json')!=stream_identity(original):raise ValueError('Old manifest changed')
            before=sum(q.stat().st_size for q in old.iterdir())
            if args.retire_uncompressed:shutil.rmtree(old)
        row=dict(id=name,index=str(index),index_identity=stream_identity(index),
            old_bytes=before,compressed_bytes=sum(q.stat().st_size for q in archive.iterdir()),
            every_decompressed_byte_SHA_checked=True,uncompressed_directory_retired=not old.exists())
        report['tiles'].append(row);atomic_json(args.report,report)
        print(json.dumps(dict(event='closed_tile_losslessly_archived',**row)),flush=True)
    report.update(complete=True,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        original_bytes=sum(x['old_bytes'] for x in report['tiles']),
        archive_bytes=sum(x['compressed_bytes'] for x in report['tiles']),
        numerical_operations_performed=False)
    atomic_json(args.report,report)
    return 0

if __name__=='__main__':raise SystemExit(main())
