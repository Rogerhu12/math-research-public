#!/usr/bin/env python3
"""Retire only root-authorized reproducible old q122-derived geometry chunks.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All original manifests, screens, recipes, source hashes, owned outcomes and
accepted/raw/response inputs are retained. The current q126 nineteen fields
and current release warm are outside this script's allowlisted directory.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import time

PREFIXES=(
 'q126-tail2-size102-r1','q130-tail4-size1035-r1',
 'q130-eight-tail4-size1035-exactchart-r1',
 'q130-eight-sync-tail4-size102-r1',
 'q130-eight-sync-tail4-size1035-exactchart-r1',
)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
def read(p):return json.loads(Path(p).read_text())
def durable(p,data):
    with p.open('x') as f:
        json.dump(data,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inventory',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.inventory.exists() or a.out.exists():raise FileExistsError('Fresh retirement records required')
    root=Path.cwd().resolve();base=root/'m32-q122-r1'
    if root.name!='geometry-work' or base.is_symlink():raise ValueError('Unexpected private geometry workspace')
    groups=[];files=[];metadata=[]
    for prefix in PREFIXES:
        rp=base/(prefix+'-geometry-resource.json')
        if not rp.exists():rp=base/(prefix+'-resource.json')
        owned=read(rp);cmd=owned['command']
        assert owned['exitcode']==0 and owned['wait4_observed'] and owned['termination_signal'] is None
        screenpath=root/cmd[cmd.index('--inspect-warm-output')+1]
        screen=read(screenpath)
        assert screen['finished'] and screen['geometry_fields']['shape']==[3764,768,3]
        names=[base/(prefix+'-field.json')]
        if '--point-cloud-array' in cmd:names.append(root/cmd[cmd.index('--point-cloud-array')+1])
        current_inputs={}
        for arg in cmd:
            p=Path(arg)
            if not p.is_absolute():p=root/p
            if p.is_file() and not p.name.endswith('.npy.gz'):current_inputs[str(p)]=sha(p)
        group=dict(prefix=prefix,owned_resource=str(rp),owned_resource_sha256=sha(rp),
            formal_exitcode=0,original_command=cmd,original_source_sha256=screen.get('source_sha256'),
            retained_current_recipe_inputs=current_inputs,screen=str(screenpath),screen_sha256=sha(screenpath),
            manifests=[])
        metadata.extend([dict(path=str(rp),sha256=sha(rp)),dict(path=str(screenpath),sha256=sha(screenpath))])
        for mp in names:
            m=read(mp);assert m['complete'] and m['shape']==[3764,768,3] and len(m['chunks'])==18
            previous=0
            for row in m['chunks']:
                p=mp.parent/row['file']
                assert p.parent.resolve()==base and not p.is_symlink() and p.name.endswith('.npy.gz')
                assert row['start']==previous and row['end']>row['start'];previous=row['end']
                st=p.stat();assert st.st_size==row['bytes'] and sha(p)==row['sha256']
                files.append(dict(path=str(p),sha256=row['sha256'],bytes=st.st_size,
                    allocated_bytes=st.st_blocks*512,links=st.st_nlink,manifest=str(mp),
                    start=row['start'],end=row['end']))
            assert previous==3764
            group['manifests'].append(dict(path=str(mp),sha256=sha(mp),full_manifest=m))
            metadata.append(dict(path=str(mp),sha256=sha(mp)))
        groups.append(group)
    assert len(files)==126 and len({f['path'] for f in files})==126
    inventory=dict(schema='authorized-old-m32-q122-derived-chunk-retirement-inventory-v1',
        source_sha256=sha(__file__),authorization='Parent root explicitly authorized retirement of unused reproducible m32-q122-r1 derived geometry/point chunks; preserve current-A19/current-release, all metadata and true solver inputs.',
        files=files,groups=groups,retained_metadata=metadata,
        file_count=len(files),bytes=sum(r['bytes'] for r in files),
        allocated_bytes=sum(r['allocated_bytes'] for r in files),
        original_owned_outcomes_and_all_chunk_SHA_verified=True,
        reproduction='Run each retained original command with the retained exact inputs and source hashes; manifests store every original compressed chunk SHA and coverage. Renamed output paths can change metadata text, not numerical array content.',
        protected_directories=['m32-q126-r1','notes'],created_epoch=time.time())
    durable(a.inventory,inventory)
    freed_before=shutil.disk_usage(root).free
    removed=[]
    for row in files:
        p=Path(row['path']);assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
        p.unlink();removed.append(row['path'])
    assert all(not Path(p).exists() for p in removed)
    assert all(sha(r['path'])==r['sha256'] for r in metadata)
    result=dict(schema='authorized-old-m32-q122-derived-chunk-retirement-result-v1',
        source_sha256=sha(__file__),inventory=str(a.inventory),inventory_sha256=sha(a.inventory),
        removed_count=len(removed),removed_logical_bytes=inventory['bytes'],removed_allocated_bytes=inventory['allocated_bytes'],
        all_allowlisted_chunks_removed=True,all_recorded_metadata_unchanged=True,
        current_A19_and_current_release_untouched=True,accepted_raw_response_inputs_untouched=True,
        free_bytes_before=freed_before,free_bytes_after=shutil.disk_usage(root).free,
        elapsed_seconds=time.monotonic()-start)
    durable(a.out,result)
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
