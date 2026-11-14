#!/usr/bin/env python3
"""Preserve every immutable old M28 cache byte in RAM and its original path.
Author: strong_recovery (GPT-6 Astra Pro, AI assisted), 2026-11-13.
Parent explicitly authorized at 20:36Z. Current M32 identity and live J are excluded.
"""
from pathlib import Path
import hashlib,json,os,stat,time
BASE=Path('/workspace/scratch/d1aa462cfc02/strong-work/full-tangent-stage-cache')
OLD=BASE/'a14c9bbf51316f35811e1d73ce0f41431e292a47a419a503a9bb5409c83e7766'
RAM=Path(__file__).resolve().parent
DEST=RAM/'preserved-cache-r3'
def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):h.update(chunk)
    return h.hexdigest()
def free(path):
    s=os.statvfs(path);return s.f_bavail*s.f_frsize
def main():
    assert OLD.is_dir() and not OLD.is_symlink()
    DEST.mkdir(exist_ok=False)
    files=sorted(p for p in OLD.rglob('*') if p.is_file())
    total=sum(p.stat().st_size for p in files)
    assert free(RAM)>total+(256<<20)
    first=dict(scope=__doc__,source=str(OLD),destination=str(DEST),
        file_count=len(files),bytes=total,workspace_free_before=free(OLD),
        current_M32_identity_excluded='cfbd416badbaa450fbbc02f979ec50408ed4449862ebafa91e4aae76f2a8567b',
        scientific_bytes_deleted=False)
    (RAM/'intent-r3.json').write_text(json.dumps(first,indent=2)+'\n')
    moved=0;allocated=0;start=time.monotonic()
    with (RAM/'inventory-r3.jsonl').open('x') as log:
        for p in files:
            if p.is_symlink():
                destination=p.resolve();assert str(destination).startswith('/dev/shm/vfxm28/')
                source_sha=digest(p);assert digest(destination)==source_sha
                log.write(json.dumps(dict(original=str(p),preserved=str(destination),bytes=p.stat().st_size,sha256=source_sha,previously_restored_RAM_copy=True,original_path_reads_same_bytes=True))+'\n')
                moved+=1
                continue
            info=p.lstat();assert stat.S_ISREG(info.st_mode)
            rel=p.relative_to(OLD);out=DEST/rel;out.parent.mkdir(parents=True,exist_ok=True)
            source_sha=digest(p)
            with p.open('rb') as inp,out.open('xb') as dst:
                for chunk in iter(lambda:inp.read(1<<20),b''):dst.write(chunk)
                dst.flush();os.fsync(dst.fileno())
            assert out.stat().st_size==info.st_size and digest(out)==source_sha
            os.chmod(out,stat.S_IMODE(info.st_mode))
            short=Path('/dev/shm/vfxm28')/('%06d'%moved)
            os.link(out,short)
            temporary=p.with_name(p.name+'.ramlink-2036')
            assert p.stat().st_size==info.st_size and digest(p)==source_sha
            try:
                temporary.symlink_to(short)
                os.replace(temporary,p)
            except OSError as error:
                if error.errno!=28:raise
                # The complete old inactive byte stream is already double-SHA
                # verified in RAM. Only ENOSPC prevents a new link inode.
                log.write(json.dumps(dict(event='verified_RAM_before_ENOSPC_relink',original=str(p),preserved=str(out),sha256=source_sha,bytes=info.st_size))+'\n')
                log.flush();os.fsync(log.fileno())
                p.unlink()
                p.symlink_to(short)
            assert p.is_symlink() and digest(p)==source_sha
            row=dict(original=str(p),preserved=str(out),bytes=info.st_size,
                old_allocated_bytes=info.st_blocks*512,sha256=source_sha,
                original_path_reads_same_bytes=True)
            log.write(json.dumps(row)+'\n');moved+=1;allocated+=info.st_blocks*512
            if moved%128==0:log.flush()
    summary={**first,'finished':True,'moved_files':moved,'released_old_allocated_bytes':allocated,
        'all_original_paths_preserved':True,'all_original_and_RAM_SHA256_verified':True,
        'workspace_free_after':free(OLD),'RAM_free_after':free(RAM),
        'inventory_sha256':digest(RAM/'inventory-r3.jsonl'),'wall_seconds':time.monotonic()-start}
    (RAM/'receipt-r3.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary),flush=True)
if __name__=='__main__':main()
