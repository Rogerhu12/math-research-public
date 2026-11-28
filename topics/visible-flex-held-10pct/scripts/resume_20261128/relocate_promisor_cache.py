#!/usr/bin/env python3
"""Relocate verified remote promisor pack caches to a second scratch filesystem.

Keeps refs, index, loose objects (including unpublished objects), and worktree
files in place. Uses Git's standard objects/info/alternates mechanism. No
history, source, mathematical input, or remote ref is modified.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import time

def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda:f.read(4*1024*1024),b""):h.update(b)
    return h.hexdigest()

def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_suffix(p.suffix+".tmp")
    with tmp.open("w") as f:
        json.dump(d,f,ensure_ascii=False,indent=2);f.write("\n");f.flush();os.fsync(f.fileno())
    os.replace(tmp,p)

def git(repo,*a):
    return subprocess.check_output(["git","-C",str(repo),*a],text=True).strip()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--cache",type=Path,required=True)
    ap.add_argument("--manifest",type=Path,required=True)
    a=ap.parse_args();repo=a.repo.resolve();dest=a.cache.resolve()
    assert not dest.exists(),"Choose a new empty cache directory"
    assert git(repo,"rev-list","--count","origin/main..HEAD")=="0","Publish owned commits first"
    assert git(repo,"config","--get","remote.origin.promisor")=="true"
    common=Path(git(repo,"rev-parse","--git-common-dir"))
    if not common.is_absolute():common=repo/common
    objects=common.resolve()/"objects";pack=objects/"pack"
    assert not (pack/"multi-pack-index").exists(),"Handle an existing MIDX explicitly first"
    sources=[]
    for mark in sorted(pack.glob("pack-*.promisor")):
        stem=mark.name[:-len(".promisor")]
        for suffix in [".pack",".idx",".promisor",".rev",".bitmap",".keep"]:
            p=pack/(stem+suffix)
            if suffix in (".pack",".idx",".promisor"):assert p.is_file(),str(p)
            if p.exists():
                assert p.is_file() and not p.is_symlink(),str(p)
                sources.append(p)
    assert sources
    needed=sum(p.stat().st_size for p in sources)
    assert shutil.disk_usage(dest.parent).free>needed+64*1024**2
    available=int(next(x.split()[1] for x in Path("/proc/meminfo").read_text().splitlines() if x.startswith("MemAvailable:")))*1024
    assert available>needed+3*1024**3,"Preserve actual memory headroom for the active numerical jobs"
    head=git(repo,"rev-parse","HEAD")
    free_before=shutil.disk_usage(repo).free
    dest.mkdir(parents=True);(dest/"pack").mkdir()
    report={"status":"copying_verified_remote_promisor_cache","head":head,
        "repository":str(repo),"original_objects":str(objects),"alternate_cache":str(dest),
        "source_bytes":needed,"worktree_and_refs_and_index_unchanged":True,
        "loose_objects_not_relocated":True,"sources":[],"started_unix":time.time()}
    save(a.manifest,report)
    for p in sources:
        q=dest/"pack"/p.name
        shutil.copy2(p,q)
        before=sha(p);after=sha(q)
        assert before==after and p.stat().st_size==q.stat().st_size,str(p)
        report["sources"].append({"original":str(p),"alternate":str(q),"bytes":p.stat().st_size,"sha256":before})
    report["status"]="all_copies_byte_verified_before_alternate_install";save(a.manifest,report)
    assert git(repo,"rev-parse","HEAD")==head
    alt=objects/"info"/"alternates";alt.parent.mkdir(exist_ok=True)
    previous=alt.read_text() if alt.exists() else ""
    lines=[x for x in previous.splitlines() if x]
    assert str(dest) not in lines
    temp=alt.with_name("alternates.held10-tmp")
    with temp.open("w") as f:
        f.write("\n".join(lines+[str(dest)])+"\n");f.flush();os.fsync(f.fileno())
    os.replace(temp,alt)
    report["previous_alternates"]=lines
    report["status"]="alternate_installed_all_copies_verified";save(a.manifest,report)
    released=0
    for row in report["sources"]:
        p=Path(row["original"])
        assert sha(p)==row["sha256"]
        released+=p.stat().st_blocks*512
        p.unlink()
    assert git(repo,"rev-parse","HEAD")==head
    subprocess.run(["git","-C",str(repo),"cat-file","-e",head+"^{commit}"],check=True)
    subprocess.run(["git","-C",str(repo),"diff","--quiet"],check=True)
    report.update(status="complete_verified_remote_cache_relocated",released_allocated_bytes=released,
        free_before=free_before,free_after=shutil.disk_usage(repo).free,finished_unix=time.time(),
        recovery_if_alternate_scratch_is_lost="All relocated packs are remote promisor caches; preserve worktree/refs/loose objects, remove only the missing alternate line, then refetch the recorded HEAD and origin/main with blob:none and fetch.negotiationAlgorithm=noop. Never reset or discard source files.")
    save(a.manifest,report)
    print(json.dumps({k:report[k] for k in ["status","head","source_bytes","released_allocated_bytes","free_before","free_after","alternate_cache"]},ensure_ascii=False),flush=True)
if __name__=="__main__":main()
