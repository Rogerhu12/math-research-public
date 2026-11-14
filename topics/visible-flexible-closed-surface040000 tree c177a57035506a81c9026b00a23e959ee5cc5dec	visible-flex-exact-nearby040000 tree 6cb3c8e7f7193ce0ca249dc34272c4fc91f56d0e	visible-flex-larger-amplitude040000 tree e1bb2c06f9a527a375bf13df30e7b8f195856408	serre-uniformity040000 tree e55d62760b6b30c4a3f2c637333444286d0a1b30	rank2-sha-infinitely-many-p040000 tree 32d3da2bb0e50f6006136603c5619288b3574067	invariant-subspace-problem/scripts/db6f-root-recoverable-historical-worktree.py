#!/usr/bin/env python3
"""Evict/restore only 42 frozen, locally recoverable historical data copies.

Payloads remain in published local Git objects. No network, object deletion,
repacking or ref changes. Skip-worktree flags prevent staging deletions.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

MANIFEST_SHA = 'cfc440e00797e6c68bbb3cb78077757f20d8bfa1f0f7902f594581f1b40c45c7'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('operation', choices=['evict','restore'])
    ap.add_argument('--manifest', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    repo = Path(__file__).resolve().parents[3]
    assert sha(args.manifest) == MANIFEST_SHA and not args.out.exists()
    data = json.loads(args.manifest.read_text())
    assert Path(data['repository']) == repo and data['file_count'] == 42
    assert 'GIT_INDEX_FILE' not in os.environ
    env = dict(os.environ, GIT_NO_LAZY_FETCH='1', GIT_OPTIONAL_LOCKS='0')
    git = ['/usr/bin/git','-c','protocol.allow=never','-c','remote.origin.promisor=false',
           '-c','core.fsmonitor=false','-c','gc.auto=0','-C',str(repo)]

    def run(*argv, input=None):
        result = subprocess.run(git+list(argv), input=input, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, env=env)
        if result.returncode:
            raise RuntimeError('Local Git operation failed: '+argv[0]+'; exit '+str(result.returncode))
        return result.stdout

    rows = data['files']
    paths = [v['path'] for v in rows]
    assert len(set(paths)) == 42
    for name in paths:
        assert name.startswith('topics/visible-flexible-closed-surface/notes/') and name.endswith('.f64.gz')
    paths_input = b''.join(p.encode()+b'\0' for p in paths)
    head = run('rev-parse','HEAD').decode().strip()
    if args.operation == 'evict':
        assert head == data['published_head'] == run('rev-parse','origin/main').decode().strip()
        assert not run('status','--porcelain=v1','-z','--',*paths)
    protected = set()
    for row in data['source_bindings']:
        p = Path(row['path'])
        assert p.stat().st_size == row['bytes'] and sha(p) == row['sha256']
        obj = json.loads(p.read_text())
        for value in obj.get('bound_files',obj.get('bindings',[])):
            protected.add(str(Path(value['path']).resolve()))
    tree = {}
    for item in run('ls-tree','-rz','--full-tree',head,'--',*paths).split(b'\0'):
        if item:
            metadata,name = item.split(b'\t',1)
            mode,kind,oid = metadata.decode().split()
            assert kind == 'blob'
            tree[name.decode()] = (mode,oid)
    index = {}
    for item in run('ls-files','--stage','-z','--',*paths).split(b'\0'):
        if item:
            metadata,name = item.split(b'\t',1)
            mode,oid,stage = metadata.decode().split()
            assert stage == '0'
            index[name.decode()] = (mode,oid)
    before = shutil.disk_usage(repo).free
    snapshots = {}
    # Validate every object and every working copy before a first mutation.
    for row in rows:
        p = repo/row['path']
        assert tree[row['path']] == index[row['path']] == (row['mode'],row['git_blob_sha1'])
        assert str(p) not in protected
        assert not any(str(p).startswith(v) for v in data['protected_full_output_prefixes'])
        local = row['local_object']
        assert local['kind'] == 'pack-index-v2'
        idx = Path(local['index']).read_bytes()
        assert hashlib.sha1(idx[:-20]).hexdigest() == local['index_checksum_hex']
        assert idx[-40:-20].hex() == local['pack_checksum_hex']
        offset = 8+1024+20*local['index_position']
        assert idx[offset:offset+20].hex() == row['git_blob_sha1'] and Path(local['pack']).is_file()
        payload = run('cat-file','blob',row['git_blob_sha1'])
        assert len(payload) == row['bytes'] and hashlib.sha256(payload).hexdigest() == row['sha256']
        assert hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload).hexdigest() == row['git_blob_sha1']
        if args.operation == 'evict' or p.exists():
            assert p.is_file() and not p.is_symlink() and p.stat().st_nlink == 1
            assert p.stat().st_size == row['bytes'] and sha(p) == row['sha256']
            snapshots[row['path']] = (p.stat().st_ino,p.stat().st_mtime_ns,p.stat().st_size)
    assert run('rev-parse','HEAD').decode().strip() == head
    report = {'status':'VALIDATED_BEFORE_WORKTREE_OPERATION','operation':args.operation,
              'manifest_sha256':MANIFEST_SHA,'head':head,'network_operations':0,
              'git_objects_or_refs_removed_or_rewritten':False,
              'file_count':42,'source_root_bindings_rechecked':len(data['source_bindings']),
              'all_local_decoded_payloads_verified':True,'files_completed':[],
              'available_bytes_before':before}

    def save():
        temporary = args.out.with_name(args.out.name+'.tmp')
        temporary.write_text(json.dumps(report,indent=2)+'\n')
        os.replace(temporary,args.out)

    save()
    try:
        if args.operation == 'evict':
            run('update-index','--skip-worktree','-z','--stdin',input=paths_input)
            for row in rows:
                p = repo/row['path'];st=p.stat()
                assert (st.st_ino,st.st_mtime_ns,st.st_size) == snapshots[row['path']]
                assert sha(p) == row['sha256']
                p.unlink()
                report['files_completed'].append(row['path']);save()
        else:
            for row in rows:
                p = repo/row['path']
                if not p.exists():
                    payload = run('cat-file','blob',row['git_blob_sha1'])
                    assert len(payload)==row['bytes'] and hashlib.sha256(payload).hexdigest()==row['sha256']
                    with p.open('xb') as stream:
                        stream.write(payload);stream.flush();os.fsync(stream.fileno())
                    p.chmod(0o644)
                assert sha(p)==row['sha256']
                report['files_completed'].append(row['path']);save()
            run('update-index','--no-skip-worktree','-z','--stdin',input=paths_input)
        assert not run('status','--porcelain=v1','-z','--',*paths)
        assert run('rev-parse','HEAD').decode().strip() == head
        report['status'] = 'RECOVERABLE_WORKTREE_EVICTION_COMPLETE' if args.operation=='evict' else 'LOCAL_WORKTREE_RESTORATION_COMPLETE'
        report['selected_paths_git_status_clean'] = True
    except Exception as error:
        report.update(status='PARTIAL_WORKTREE_OPERATION_REQUIRES_REVIEW',error_type=type(error).__name__)
        save()
        raise
    report['available_bytes_after'] = shutil.disk_usage(repo).free
    report['observed_free_bytes_change'] = report['available_bytes_after']-before
    report['recovery'] = 'Invoke this exact script with restore and the same manifest, choosing a new observation path; source blobs are local and network is disabled.'
    save()
    print(json.dumps({key:report[key] for key in ['status','file_count','available_bytes_before','available_bytes_after','observed_free_bytes_change','selected_paths_git_status_clean']}))


if __name__ == '__main__':
    main()
