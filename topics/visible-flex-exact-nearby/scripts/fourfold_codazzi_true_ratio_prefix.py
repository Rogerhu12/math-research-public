"""Crash-consistent private GRQ stream, continuation state and small receipt."""
from hashlib import sha256
import gzip,json,os,struct
from fourfold_codazzi_true_ratio_live_rules import canonical

L=struct.Struct("<I")


def replace(path,body):
    tmp=path.with_suffix(".partial")
    with tmp.open("wb") as f:
        f.write(body);f.flush();os.fsync(f.fileno())
    tmp.replace(path)


def digest(data):
    return sha256(data).hexdigest()


class Prefix:
    def __init__(self,path,receipt,header,summary):
        self.path=path;self.receipt=receipt
        self.raw=sha256();self.gz=sha256();self.usize=0;self.csize=0
        self.file=path.open("xb");self.count=0;self.committed=0
        self.append(L.pack(len(header))+header)
        self.commit(dict(summary,completed_subpieces=0,prefix_proved=False),None)

    def append(self,row):
        # Each natural row is a complete gzip member. The full file reads as
        # one gzip stream and can be truncated at any confirmed prefix.
        member=gzip.compress(row,compresslevel=1,mtime=0)
        self.file.write(member);self.file.flush();os.fsync(self.file.fileno())
        self.raw.update(row);self.gz.update(member)
        self.usize+=len(row);self.csize+=len(member)

    def commit(self,summary,frontier):
        ready=dict(summary,complete=False,proved=False,private_prefix_bytes=self.csize,
                   private_prefix_sha256=self.gz.hexdigest(),private_prefix_uncompressed_bytes=self.usize,
                   private_prefix_uncompressed_sha256=self.raw.hexdigest())
        if frontier is not None:
            name="grq-frontier-"+str(summary["completed_subpieces"]%2)+".bin.gz"
            b=gzip.compress(frontier,compresslevel=1,mtime=0);p=self.path.parent/name
            replace(p,b)
            if p.read_bytes()!=b:raise ValueError("whole private continuation readback")
            ready.update(continuation_file=name,continuation_bytes=len(b),continuation_sha256=digest(b),
                         continuation_uncompressed_bytes=len(frontier),continuation_uncompressed_sha256=digest(frontier))
        body=canonical(ready)
        if len(body)>=100000:raise ValueError("entire small scientific prefix")
        replace(self.receipt,body)
        self.committed=self.csize;self.count=ready["completed_subpieces"]

    def close(self):
        self.file.truncate(self.committed);self.file.flush();self.file.close()


def record_failure(path,exc):
    prior=json.loads(path.read_bytes()) if path.exists() else {"complete":False,"proved":False,
            "completed_subpieces":0,"prefix_proved":False}
    prior.update(complete=False,proved=False,failure=str(exc),event_commit=os.environ["GITHUB_SHA"],
                 run=os.environ["GITHUB_RUN_ID"],attempt=1)
    b=canonical(prior);replace(path,b)
    print("GRQ_FAILED_AT_COMPLETE_PREFIX",b.decode().strip(),flush=True)


def verify_last(private,receipt):
    from pathlib import Path
    prior=json.loads(Path(receipt).read_bytes())
    if prior.get("complete") or "private_prefix_bytes" not in prior:return prior
    root=Path(private);p=root/"true-complete-first-ratio.bin.gz"
    size=prior["private_prefix_bytes"]
    h=sha256()
    if p.stat().st_size<size:raise ValueError("an entire confirmed private prefix is missing")
    with p.open("rb") as f:
        remaining=size
        while remaining:
            b=f.read(min(1<<20,remaining))
            if not b:raise ValueError("partial compressed natural row")
            h.update(b);remaining-=len(b)
    if h.hexdigest()!=prior["private_prefix_sha256"]:raise ValueError("whole compressed prefix differs")
    # Remove only an uncommitted partial write from this private output.
    if p.stat().st_size>size:
        with p.open("r+b") as f:f.truncate(size)
    h=sha256();length=0
    with gzip.open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):h.update(b);length+=len(b)
    if (length,h.hexdigest())!=(prior["private_prefix_uncompressed_bytes"],prior["private_prefix_uncompressed_sha256"]):
        raise ValueError("entire original confirmed uncompressed prefix")
    if prior["completed_subpieces"]:
        b=(root/prior["continuation_file"]).read_bytes();u=gzip.decompress(b)
        if (len(b),digest(b),len(u),digest(u))!=(prior["continuation_bytes"],prior["continuation_sha256"],
                 prior["continuation_uncompressed_bytes"],prior["continuation_uncompressed_sha256"]):
            raise ValueError("whole private physical continuation state")
    return prior


if __name__=="__main__":
    import sys
    from pathlib import Path
    result=verify_last(sys.argv[1],sys.argv[2]);b=Path(sys.argv[2]).read_bytes()
    print("GRQ_FINAL_SMALL_OR_PREFIX",len(b),digest(b),b.decode().strip(),flush=True)
