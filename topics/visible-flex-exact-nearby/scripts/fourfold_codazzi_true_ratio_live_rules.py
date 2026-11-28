"""Observe both public rules in an independent sparse checkout during GRQ."""
from pathlib import Path
from hashlib import sha256
import json,os,subprocess,sys,time

PATHS=("README.md","topics/visible-flex-exact-nearby/README.md")
PERIOD=900
SOFT_LIMIT=19_200


def canonical(d):
    return (json.dumps(d,sort_keys=True,separators=(",",":"))+"\n").encode()


def atomic(path,data):
    q=path.with_suffix(".partial");q.write_bytes(data);q.replace(path)


def directory():
    return Path(os.environ["RUNNER_TEMP"])/"grq-live-rules"


def git(directory,*args):
    return subprocess.check_output(["git","-C",str(directory),*args],timeout=120)


def initialize(home):
    repo=Path(os.environ["GITHUB_WORKSPACE"]);event=os.environ["GITHUB_SHA"]
    work=home/"read-only-checkout"
    if not work.exists():
        subprocess.run(["git","clone","--shared","--no-checkout",str(repo),str(work)],check=True,timeout=120)
        url=git(repo,"remote","get-url","origin").decode().strip()
        git(work,"remote","set-url","origin",url)
        git(work,"config","remote.origin.promisor","true")
        git(work,"config","remote.origin.partialclonefilter","blob:none")
        git(work,"sparse-checkout","set","--no-cone",*["/"+p for p in PATHS])
        git(work,"switch","--detach",event)
    return repo,work,event


def update(home,record):
    record=dict(record,checking=True,checked_at=time.time())
    atomic(home/"status.json",canonical(record))
    try:
        if record["checked_at"]-record["started"]>=SOFT_LIMIT:
            raise RuntimeError("GRQ soft wall budget reached at a complete prefix")
        repo,work,event=initialize(home)
        git(work,"fetch","--filter=blob:none","origin","+refs/heads/main:refs/remotes/origin/main")
        git(work,"pull","--ff-only","origin","main")
        head=git(work,"rev-parse","HEAD").decode().strip()
        observations=[];changed=[]
        for name in PATHS:
            initial=git(repo,"show",event+":"+name);current=(work/name).read_bytes()
            matches=initial==current
            observations.append({"path":name,"bytes":len(current),"sha256":sha256(current).hexdigest(),
                                 "reviewed_bytes":len(initial),"reviewed_sha256":sha256(initial).hexdigest(),
                                 "matches_event_rules":matches})
            if not matches:changed.append(name)
        record.update(read_head=head,rules=observations)
        if changed:
            raise RuntimeError("changed public rules require review: "+", ".join(changed))
        record.update(ok=True,checking=False)
    except Exception as exc:
        record.update(ok=False,checking=False,error=str(exc))
    record["finished_at"]=time.time()
    b=canonical(record);atomic(home/"status.json",b)
    with (home/"observations.jsonl").open("ab") as f:f.write(b)
    print("GRQ_README_OBSERVATION",b.decode().strip(),flush=True)
    return record


def gate():
    p=directory()/"status.json"
    while True:
        d=json.loads(p.read_bytes())
        if not d.get("ok") and not d.get("checking"):
            raise RuntimeError(d.get("error","GRQ public rule observation stopped"))
        if not d["checking"]:break
        time.sleep(2)
    if time.time()-d["checked_at"]>=1800 or time.time()-d["started"]>=SOFT_LIMIT:
        raise RuntimeError("GRQ observed-rule freshness or soft wall budget expired")
    return d["read_head"]


def supervise(command):
    home=directory();home.mkdir(parents=True,exist_ok=True)
    path=home/"status.json"
    record=json.loads(path.read_bytes()) if path.exists() else {"started":time.time()}
    if record.get("ok") is False:raise RuntimeError(record["error"])
    record=update(home,record)
    if not record["ok"]:return 1
    child=subprocess.Popen(command)
    while child.poll() is None:
        now=time.time()
        if now-record["checked_at"]>=PERIOD or now-record["started"]>=SOFT_LIMIT:
            record=update(home,record)
            if not record["ok"]:
                # The next row boundary stops the scientific child. Its
                # last fully committed private row and receipt already exist.
                try:child.wait(timeout=120)
                except subprocess.TimeoutExpired:child.terminate();child.wait(timeout=30)
                return 1
        time.sleep(2)
    return child.returncode


if __name__=="__main__":
    if os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public" or not sys.argv[1:]:
        raise RuntimeError("public checked scientific command")
    sys.exit(supervise(sys.argv[1:]))
