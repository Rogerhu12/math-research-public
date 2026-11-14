#!/usr/bin/env python3
"""Archive immutable completed prefix calls without duplicating live partials.

Default selection keeps complete fun_jac calls (both J and PJ) and whole-field
RHS calls. Small finite-difference RHS entries are redundant for restoring a
completed Jacobian call and are left local. Every selected gzip is byte-exact,
all embedded inputs and outputs are hashed again, and each archive is under
5 MB. This tool neither computes derivatives nor accepts a solution.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import struct
import tarfile

MAGIC=b'STRONG-PREFIX-CACHE-1\n'
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def sha(data):return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()


def verify_entry(data,identity,key):
    with gzip.GzipFile(fileobj=io.BytesIO(data),mode='rb') as stream:
        if stream.read(len(MAGIC))!=MAGIC:raise ValueError('Prefix cache magic differs')
        size=struct.unpack('<Q',stream.read(8))[0]
        if size>2_000_000:raise ValueError('Implausible prefix cache header size')
        record=json.loads(stream.read(size))
        if record['key']!=key or sha(canonical(record['request']))!=key:
            raise ValueError('The complete input key cannot be reconstructed')
        if record['request']['identity_sha256']!=identity:
            raise ValueError('The cache item belongs to another source/runtime identity')
        for collection in ('inputs','outputs'):
            for item in record[collection]:
                meta=item['array'];left=meta['bytes'];digest=hashlib.sha256()
                while left:
                    block=stream.read(min(left,65536))
                    if not block:raise ValueError('Truncated cached array')
                    digest.update(block);left-=len(block)
                if digest.hexdigest()!=meta['C_bytes_sha256']:
                    raise ValueError('An original input/output byte digest differs')
                if collection=='inputs' and record['request']['inputs'][item['name']]!=meta:
                    raise ValueError('Recorded complete input metadata differs')
        if stream.read(1):raise ValueError('Trailing cache bytes')
    operation=record['request']['operation']
    if operation=='fun_jac' and (not record['tuple_output'] or len(record['outputs'])!=2):
        raise ValueError('The complete state and parameter Jacobians are required')
    return dict(key=key,operation=operation,points=record['request']['inputs']['t']['shape'][0],
        bytes=len(data),sha256=sha(data),input_array_hashes={v['name']:v['array']['C_bytes_sha256'] for v in record['inputs']},
        output_array_hashes=[v['array']['C_bytes_sha256'] for v in record['outputs']],
        physical_chart_identity_sha256=sha(canonical(record['request']['object'])))


def immutable(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        if path.read_bytes()!=data:raise ValueError('Immutable restored file differs: '+str(path))
        return
    tmp=path.with_name(path.name+'.tmp-'+str(os.getpid()))
    try:
        with tmp.open('xb') as stream:
            stream.write(data);stream.flush();os.fsync(stream.fileno())
        try:os.link(tmp,path)
        except FileExistsError:
            if path.read_bytes()!=data:raise ValueError('Concurrent immutable cache data differs')
    finally:tmp.unlink(missing_ok=True)


def check_archive(path,expected,destination=None):
    if sha(path.read_bytes())!=expected['sha256']:raise ValueError('Archive bytes differ')
    wanted={v['member']:v for v in expected['members']};seen=set()
    with tarfile.open(path,'r:gz') as archive:
        for member in archive:
            if not member.isfile() or member.name not in wanted or member.name in seen:
                raise ValueError('Unexpected or duplicated cache archive member')
            rel=Path(member.name)
            if rel.is_absolute() or '..' in rel.parts or len(rel.parts)!=2:
                raise ValueError('Unsafe cache archive member name')
            data=archive.extractfile(member).read()
            item=wanted[member.name]
            if len(data)!=item['bytes'] or sha(data)!=item['sha256']:
                raise ValueError('Archived original item is not byte-identical')
            if rel.name=='identity.json':
                if sha(canonical(json.loads(data)))!=rel.parts[0]:
                    raise ValueError('The complete source/runtime identity digest differs')
            else:
                actual=verify_entry(data,rel.parts[0],rel.name[:-7])
                if any(actual[k]!=item[k] for k in actual):
                    raise ValueError('Archived full-input call fails its metadata')
            if destination is not None:immutable(destination/rel,data)
            seen.add(member.name)
    if seen!=set(wanted):raise ValueError('An archived cache member is missing')
    return len(seen)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--identity-directory',type=Path)
    parser.add_argument('--out-prefix',type=Path)
    parser.add_argument('--include-all-calls',action='store_true')
    parser.add_argument('--prior-manifest',type=Path,action='append',default=[])
    parser.add_argument('--restore-manifest',type=Path)
    parser.add_argument('--restore-directory',type=Path)
    args=parser.parse_args()
    if args.restore_manifest:
        if args.restore_directory is None:raise ValueError('Restore directory is required')
        record=json.loads(args.restore_manifest.read_text());total=0
        for item in record['archives']:
            total+=check_archive(Path(item['path']),item,args.restore_directory)
        print(json.dumps(dict(event='prefix_cache_archive_restored',complete_items=total,
            derivative_evaluations=0,Node_processes=0)),flush=True)
        return
    if args.identity_directory is None or args.out_prefix is None:
        raise ValueError('Identity directory and fresh output prefix are required')
    directory=args.identity_directory.resolve();identity=directory.name
    identity_path=directory/'identity.json';identity_data=identity_path.read_bytes()
    if sha(canonical(json.loads(identity_data)))!=identity:raise ValueError('Identity digest mismatch')
    prior=set();prior_records=[]
    for path in args.prior_manifest:
        value=json.loads(path.read_text())
        if value['identity_sha256']!=identity:raise ValueError('Prior archive is from another identity')
        for archive in value['archives']:
            for member in archive['members']:prior.add(member['member'])
        prior_records.append(dict(path=str(path),sha256=sha(path.read_bytes())))
    items=[];omitted_small=0
    # Snapshot completed immutable filenames once. Atomic writers never expose
    # their .tmp files through this glob; later complete entries are next-batch.
    for path in sorted(directory.glob('*.bin.gz')):
        member=identity+'/'+path.name
        if member in prior:continue
        data=path.read_bytes();item=verify_entry(data,identity,path.name[:-7])
        if not args.include_all_calls and item['operation']=='fun' and item['points']<100:
            omitted_small+=1;continue
        items.append(dict(item,member=member,local_path=str(path)))
    id_member=identity+'/identity.json'
    if id_member not in prior:
        items.insert(0,dict(member=id_member,bytes=len(identity_data),sha256=sha(identity_data),local_path=str(identity_path)))
    groups=[];group=[];size=0
    for item in items:
        charge=item['bytes']+2048
        if charge>4_600_000:raise ValueError('One cache item exceeds the archive single-item limit')
        if group and size+charge>4_600_000:
            groups.append(group);group=[];size=0
        group.append(item);size+=charge
    if group:groups.append(group)
    archives=[]
    for number,group in enumerate(groups):
        path=args.out_prefix.with_name(args.out_prefix.name+'-part%03d.tar.gz'%number)
        if path.exists():raise FileExistsError('Use fresh archive prefix: '+str(path))
        temp=path.with_name(path.name+'.tmp-'+str(os.getpid()))
        try:
            with temp.open('xb') as raw:
                with gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0,compresslevel=1) as zipped:
                    with tarfile.open(fileobj=zipped,mode='w|',format=tarfile.USTAR_FORMAT) as archive:
                        for item in group:
                            data=Path(item['local_path']).read_bytes()
                            if sha(data)!=item['sha256']:raise ValueError('Immutable cache item changed during archive')
                            info=tarfile.TarInfo(item['member']);info.size=len(data);info.mtime=0;info.mode=0o600
                            archive.addfile(info,io.BytesIO(data))
                raw.flush();os.fsync(raw.fileno())
            if temp.stat().st_size>=5_000_000:raise ValueError('Archive exceeds 5 MB')
            os.link(temp,path)
        finally:temp.unlink(missing_ok=True)
        record=dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path.read_bytes()),
            members=[{k:v for k,v in item.items() if k!='local_path'} for item in group])
        check_archive(path,record)
        archives.append(record)
        print(json.dumps(dict(event='prefix_cache_archive_part_verified',path=str(path),
            items=len(group),bytes=record['bytes'],sha256=record['sha256'])),flush=True)
    result=dict(scope=__doc__,identity_sha256=identity,source_sha256=SELF_SHA,
        prior_archives=prior_records,archives=archives,selected_items=len(items),
        omitted_redundant_small_RHS_calls=omitted_small,all_selected_items_roundtrip_verified=True,
        complete_J_and_PJ_preserved=True,new_solution=False,derivative_evaluations=0,Node_processes=0)
    path=args.out_prefix.with_name(args.out_prefix.name+'-archive.json')
    immutable(path,json.dumps(result,indent=2,allow_nan=False).encode()+b'\n')
    print(json.dumps(dict(event='prefix_cache_archive_complete',path=str(path),
        sha256=sha(path.read_bytes()),selected_items=len(items),parts=len(archives))),flush=True)


if __name__=='__main__':main()
