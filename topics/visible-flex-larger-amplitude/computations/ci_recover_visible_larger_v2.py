#!/usr/bin/env python3
"""Isolated CI recovery v2: optional legacy HANDOFF marker, frozen mathematics."""
from __future__ import annotations
import argparse, base64, datetime, difflib, fnmatch, gzip, hashlib, json, os
from pathlib import Path
import re, shutil, subprocess, sys, time
TOPIC = "topics/visible-flex-larger-amplitude"
RULES = ["README.md", TOPIC + "/README.md"]
RULE_BLOBS = ["f787a306d90892d8dec765dc59747d60ba39f055",
              "696eb3ba7d3a90636e51e8fbdd573b2f37cae707"]
def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(p):
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda: f.read(1048576), b""):
            h.update(b)
    return h.hexdigest()
def save(p, x):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + "\n")
def call(argv, cwd, env=None, check=True):
    p = subprocess.run(argv, cwd=cwd, env=env, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if check and p.returncode:
        raise RuntimeError(json.dumps(argv) + "\n" + p.stdout[-16000:])
    return p
class Publisher:
    def __init__(self, repo, work, out, request):
        self.repo, self.path, self.out, self.request = repo, work / "publisher", out, request
        self.history, self.last, self.last_clock = [], None, 0.
        self.env = os.environ.copy()
        for k in list(self.env):
            if k.startswith("GIT_TRACE") or k == "GIT_CURL_VERBOSE":
                self.env.pop(k)
        token = self.env.pop("GH_TOKEN", "")
        if not token:
            raise RuntimeError("ephemeral runner token missing")
        auth = base64.b64encode(("x-access-token:" + token).encode()).decode()
        self.env.update({"GIT_TERMINAL_PROMPT":"0","GIT_CONFIG_COUNT":"5",
            "GIT_CONFIG_KEY_0":"credential.helper","GIT_CONFIG_VALUE_0":"",
            "GIT_CONFIG_KEY_1":"http.https://github.com/.extraheader",
            "GIT_CONFIG_VALUE_1":"AUTHORIZATION: basic " + auth,
            "GIT_CONFIG_KEY_2":"pack.threads","GIT_CONFIG_VALUE_2":"1",
            "GIT_CONFIG_KEY_3":"pack.window","GIT_CONFIG_VALUE_3":"0",
            "GIT_CONFIG_KEY_4":"pack.windowMemory","GIT_CONFIG_VALUE_4":"4m"})
        work.mkdir(parents=True, exist_ok=True)
        url = "https://github.com/" + os.environ["GITHUB_REPOSITORY"] + ".git"
        call(["git","clone","--filter=blob:none","--sparse","--no-checkout",
              "--depth","1","--branch","main",url,str(self.path)],repo,self.env)
        self.git(["sparse-checkout","set","--no-cone","/README.md",
                  "/" + TOPIC + "/README.md", "/" + TOPIC + "/HANDOFF.md",
                  "/" + TOPIC + "/open.md", "/" + TOPIC + "/log.md"])
        self.git(["checkout","-B","visible-larger-recovery","origin/main"])
        self.git(["config","user.name","github-actions[bot]"])
        self.git(["config","user.email","41898282+github-actions[bot]@users.noreply.github.com"])
        self.pull()
    def git(self, args, check=True):
        return call(["git"] + args,self.path,self.env,check)
    def pull(self):
        started = utc()
        p = self.git(["pull","--rebase","origin","main"],False)
        while p.returncode:
            conflicts = self.git(["diff","--name-only","--diff-filter=U"],False).stdout.splitlines()
            hp = TOPIC + "/HANDOFF.md"
            if conflicts != [hp]:
                raise RuntimeError("actual pull/rebase needs review: " + p.stdout[-16000:])
            versions = [self.git(["show",":" + str(i) + ":" + hp]).stdout for i in (1,2,3)]
            def body(text):
                text = re.sub(r"两README最近确认提交\x60[0-9a-f]{40}\x60",
                              "两README最近确认提交\x60READ_SHA\x60",text)
                return text.split("\n<!-- visible-larger-ci-actual-pull -->\n",1)[0].rstrip()
            b,x,y = map(body,versions)
            if y == b or x == y:
                selected = versions[1]
            elif x == b:
                selected = versions[2]
            else:
                raise RuntimeError("HANDOFF body changed on both sides; preserve for review")
            (self.path / hp).write_text(selected)
            self.git(["add","--sparse","--",hp])
            p = self.git(["-c","core.editor=true","rebase","--continue"],False)
        head = self.git(["rev-parse","origin/main"]).stdout.strip()
        changes = []
        for path, expected in zip(RULES,RULE_BLOBS):
            actual = self.git(["rev-parse","origin/main:" + path]).stdout.strip()
            if actual != expected:
                old = (self.repo / path).read_text()
                new = self.git(["show","origin/main:" + path]).stdout
                d = "".join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),
                    fromfile="recorded/" + path,tofile=head + "/" + path))
                changes.append({"path":path,"old_blob":expected,"new_blob":actual,"diff":d})
        self.history.append({"utc":utc(),"started":started,"main":head,
            "actual_pull":True,"readme_changes":changes,"git_output":p.stdout})
        save(self.out / "actual-pulls.json",self.history)
        self.last, self.last_clock = head,time.monotonic()
        print(json.dumps({"actual_pull":head,"readmes_unchanged":not changes,"utc":utc()}),flush=True)
        if changes:
            for x in changes:
                print(x["diff"],flush=True)
            raise RuntimeError("README changed; read and adapt before more work")
    def marker(self):
        p = self.path / TOPIC / "HANDOFF.md"
        s,_ = re.subn(r"两README最近确认提交\x60[0-9a-f]{40}\x60",
            "两README最近确认提交\x60" + self.last + "\x60",p.read_text(),count=1)
        # New HANDOFF prose may omit the legacy inline marker. The dedicated
        # footer below always records the actual pull without rewriting its body.
        tag = "\n<!-- visible-larger-ci-actual-pull -->\n"
        if tag in s:
            s = s.split(tag,1)[0].rstrip() + "\n"
        s += tag + "运行器实际pull/两README无差异：" + utc() + "，\x60" + self.last + "\x60。数学checkout保持触发提交。\n"
        if len(s.encode()) >= 10000:
            raise RuntimeError("HANDOFF exceeds 10000 bytes")
        p.write_text(s)
    def commit(self, paths, message):
        if not paths:
            return
        self.git(["add","--sparse","--"] + sorted(set(paths)))
        p = self.git(["diff","--cached","--quiet"],False)
        if p.returncode == 0:
            return
        if p.returncode != 1:
            raise RuntimeError("cannot inspect index")
        self.git(["diff","--cached","--check"])
        self.git(["commit","-m",message])
    def push(self):
        while True:
            self.pull()
            self.marker()
            self.commit([TOPIC + "/HANDOFF.md"],"visible-flex: record actual recovery README pull")
            p = self.git(["push","origin","HEAD:main"],False)
            if p.returncode == 0:
                self.pull()
                return
            if ("non-fast-forward" in p.stdout or "fetch first" in p.stdout
                    or "[rejected]" in p.stdout
                    or ("cannot lock ref" in p.stdout and "refs/heads/main" in p.stdout
                        and "but expected" in p.stdout)):
                print("ordinary main push raced; immediately git pull --rebase",flush=True)
                continue
            raise RuntimeError("git push failed: " + p.stdout[-16000:])
    def sources(self):
        paths = []
        for item in self.request.get("publish_sources",[]):
            rel = item["path"]
            if not (rel.startswith(TOPIC + "/") or
                    rel == ".github/workflows/visible-larger-runtime-recovery.yml"):
                raise RuntimeError("undeclared source scope")
            data = (self.repo / rel).read_bytes()
            old = self.git(["rev-parse","HEAD:" + rel],False)
            oldsha = old.stdout.strip() if old.returncode == 0 else None
            if oldsha:
                prior = self.git(["show","HEAD:" + rel]).stdout.encode()
                if prior == data:
                    continue
            if oldsha != item.get("expected_old_blob"):
                raise RuntimeError("source changed concurrently: " + rel)
            dst = self.path / rel; dst.parent.mkdir(parents=True,exist_ok=True)
            dst.write_bytes(data); paths.append(rel)
        for item in self.request.get("handoff_replacements",[]):
            hp = self.path / TOPIC / "HANDOFF.md"
            text = hp.read_text()
            if item["old"] in text:
                hp.write_text(text.replace(item["old"],item["new"],1))
                paths.append(TOPIC + "/HANDOFF.md")
            elif item["new"] not in text:
                raise RuntimeError("requested HANDOFF context changed; preserve for review")
        entry = self.request.get("log_append")
        if entry:
            lp = self.path / TOPIC / "log.md"
            text = lp.read_text()
            if entry not in text:
                lp.write_text(text.rstrip() + "\n\n" + entry.rstrip() + "\n")
                paths.append(TOPIC + "/log.md")
        if paths:
            self.marker(); paths.append(TOPIC + "/HANDOFF.md")
            self.commit(paths,"visible-flex: preserve recovery and isolated CI sources")
            self.push()
    def import_inputs(self, lane, values):
        """Import only declared immutable notes through terminal git at this actual pull."""
        specs = self.request.get("main_input_globs",{}).get(lane,[])
        if not specs:
            return
        head = self.last
        listing = self.git(["ls-tree","--full-tree","-r","-z",head,"--",TOPIC+"/notes"]).stdout
        entries = {}
        for entry in listing.split("\0"):
            if not entry:
                continue
            meta,rel = entry.split("\t",1)
            mode,kind,sha = meta.split()
            if kind == "blob":
                entries[rel] = (mode,sha)
        chosen,matched = {},[]
        for raw in specs:
            spec = {"glob":raw} if isinstance(raw,str) else raw
            pattern = spec["glob"].format_map(values)
            if not pattern.startswith(TOPIC+"/notes/") or ".." in Path(pattern).parts:
                raise RuntimeError("main import must be explicitly scoped to topic notes")
            found = sorted(p for p in entries if fnmatch.fnmatchcase(p,pattern))
            if not found and spec.get("required",True):
                raise FileNotFoundError("required main input missing: "+pattern)
            for rel in found:
                mode,sha = entries[rel]
                if mode != "100644":
                    raise RuntimeError("main input must be a regular file: "+rel)
                chosen[rel] = sha
            matched.append({"glob":pattern,"files":found})
        rows = []
        for rel,sha in sorted(chosen.items()):
            dst = self.repo / rel
            dst.parent.mkdir(parents=True,exist_ok=True)
            tmp = dst.with_name(dst.name+".ci-import-partial")
            if tmp.exists():
                raise FileExistsError("main import temporary path exists")
            with tmp.open("xb") as out:
                proc = subprocess.run(["git","cat-file","blob",sha],cwd=self.path,
                    env=self.env,stdout=out,stderr=subprocess.PIPE)
            if proc.returncode:
                tmp.unlink()
                raise RuntimeError("git binary input read failed: "+proc.stderr.decode(errors="replace")[-4000:])
            h = hashlib.sha1()
            h.update(("blob "+str(tmp.stat().st_size)+"\0").encode())
            with tmp.open("rb") as stream:
                for chunk in iter(lambda:stream.read(1048576),b""):
                    h.update(chunk)
            if h.hexdigest() != sha:
                tmp.unlink()
                raise RuntimeError("main import Git blob hash mismatch: "+rel)
            before = dst.exists()
            sh256 = digest(tmp)
            if before:
                if not dst.is_file() or dst.is_symlink() or digest(dst) != sh256:
                    tmp.unlink()
                    raise RuntimeError("main import would change a frozen existing input: "+rel)
                tmp.unlink()
            else:
                tmp.replace(dst)
            rows.append({"path":rel,"git_blob":sha,"sha256":sh256,
                         "bytes":dst.stat().st_size,"already_identical":before})
        save(self.out/"main-imports.json",{"schema":"visible-larger-main-input-import-v1",
            "utc":utc(),"actual_pulled_main":head,"trigger_commit":os.environ["GITHUB_SHA"],
            "patterns":matched,"files":rows,"code_checkout_changed":False})
        diagnostic = []
        for rel in self.request.get("main_text_diagnostics",{}).get(lane,[]):
            rel = rel.format_map(values)
            if rel not in chosen or not rel.endswith(".log.gz"):
                raise RuntimeError("diagnostic must be an explicitly imported gzip log")
            with gzip.open(self.repo/rel,"rb") as stream:
                data = stream.read(64001)
            if len(data)>64000:
                raise RuntimeError("requested text diagnostic exceeds64000bytes")
            diagnostic.append({"path":rel,"compressed_sha256":digest(self.repo/rel),
                "raw_sha256":hashlib.sha256(data).hexdigest(),"raw_bytes":len(data),
                "text":data.decode("utf-8")})
        if diagnostic:
            save(self.out/"imported-text-diagnostics.json",diagnostic)
        print(json.dumps({"main_inputs":len(rows),"exact_main":head,"utc":utc()}),flush=True)
    def outputs(self, patterns):
        candidates = set(self.out.rglob("*"))
        for pattern in patterns:
            candidates.update(self.repo.glob(pattern))
        paths, rows = [], []
        for src in sorted(candidates):
            if not src.is_file():
                continue
            rel = src.relative_to(self.repo).as_posix()
            if not rel.startswith(TOPIC + "/notes/"):
                raise RuntimeError("output outside topic notes")
            size = src.stat().st_size
            if src.suffix == ".md" and size >= 100000:
                raise RuntimeError("oversized Markdown")
            dstrel = rel + ".gz" if (size > 1000000 or src.suffix in (".log",".jsonl")) and src.suffix != ".gz" else rel
            dst = self.path / dstrel; dst.parent.mkdir(parents=True,exist_ok=True)
            if dstrel != rel:
                with src.open("rb") as fi, dst.open("wb") as raw:
                    with gzip.GzipFile(filename="",mode="wb",fileobj=raw,mtime=0,compresslevel=6) as fo:
                        shutil.copyfileobj(fi,fo)
            else:
                shutil.copyfile(src,dst)
            row = {"source_path":rel,"source_bytes":size,"source_sha256":digest(src),
                   "publication_path":dstrel,"publication_bytes":dst.stat().st_size,
                   "publication_sha256":digest(dst)}
            if dst.stat().st_size >= 5000000:
                dst.unlink(); row.update(published=False,reason=">=5MB; retained as workflow artifact/recipe/hash")
            else:
                row["published"] = True; paths.append(dstrel)
            rows.append(row)
        rel = self.out.relative_to(self.repo).as_posix() + "/publication-manifest.json"
        save(self.path / rel,{"schema":"visible-larger-ci-publication-v1","utc":utc(),
            "run_id":os.environ["GITHUB_RUN_ID"],"trigger_commit":os.environ["GITHUB_SHA"],
            "request":self.request,"files":rows,"task_complete":False})
        paths.append(rel); self.marker(); paths.append(TOPIC + "/HANDOFF.md")
        self.commit(paths,"visible-flex: preserve actual CI recovery outcome")
        self.push()
def run_stage(stage,repo,out,publisher,values):
    argv = [x.format_map(values) for x in stage["argv"]]
    cwd, log = repo / stage.get("cwd",""), out / (stage["name"] + ".log")
    env = os.environ.copy(); env.pop("GH_TOKEN",None)
    if stage.get("needs_github_artifact",False):
        env["GH_TOKEN"] = os.environ["GH_TOKEN"]
    if stage.get("needs_git_source_recovery",False):
        for k,v in publisher.env.items():
            if k.startswith("GIT_CONFIG_") or k == "GIT_TERMINAL_PROMPT":
                env[k] = v
    start, wall = utc(),time.monotonic()
    pid = os.fork()
    if pid == 0:
        try:
            os.chdir(cwd)
            fd = os.open(log,os.O_WRONLY | os.O_CREAT | os.O_EXCL,0o600)
            os.dup2(fd,1); os.dup2(fd,2); os.close(fd)
            os.execvpe(argv[0],argv,env)
        except BaseException:
            import traceback
            traceback.print_exc(); os._exit(126)
    while True:
        got,status,usage = os.wait4(pid,os.WNOHANG)
        if got:
            break
        if time.monotonic() - publisher.last_clock > 45 * 60:
            publisher.pull(); publisher.marker()
            publisher.commit([TOPIC + "/HANDOFF.md"],"visible-flex: hourly actual README check")
            publisher.push()
        time.sleep(1)
    row = {"name":stage["name"],"argv":argv,"cwd":str(cwd),"started_utc":start,
           "ended_utc":utc(),"wall_seconds":time.monotonic()-wall,"wait4_status":status,
           "exit_code":os.WEXITSTATUS(status) if os.WIFEXITED(status) else None,
           "signal":os.WTERMSIG(status) if os.WIFSIGNALED(status) else None,
           "maxrss_kib":usage.ru_maxrss,"utime":usage.ru_utime,"stime":usage.ru_stime,
           "log":str(log.relative_to(repo)),"log_sha256":digest(log)}
    if row["exit_code"] != 0 or row["signal"] is not None:
        with log.open("rb") as stream:
            stream.seek(max(0,log.stat().st_size-16000))
            row["failure_log_tail"] = stream.read().decode("utf-8",errors="replace")
    save(out / (stage["name"] + "-terminal.json"),row)
    print(json.dumps(row),flush=True)
    return row
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo",required=True); ap.add_argument("--request",required=True)
    ap.add_argument("--lane",choices=["sync","strong","interval"],required=True)
    a = ap.parse_args(); repo = Path(a.repo).resolve()
    request = json.loads((repo / a.request).read_text())
    ident = os.environ["GITHUB_RUN_ID"] + "-" + os.environ["GITHUB_RUN_ATTEMPT"] + "-" + a.lane
    work = Path(os.environ["RUNNER_TEMP"]) / ("visible-larger-recovery-" + ident)
    out = repo / TOPIC / "notes" / ("ci-recovery-" + ident)
    out.mkdir(parents=True,exist_ok=False)
    save(out / "request.json",request)
    save(out / "runtime.json",{"utc":utc(),"python":sys.version,
        "node":call(["node","--version"],repo).stdout.strip(),"platform":sys.platform,
        "trigger_commit":os.environ["GITHUB_SHA"],"old_local_r7_terminal":"unknown"})
    publisher,results,failure = None,[],None
    values = {"python":sys.executable,"repo":str(repo),
        "runner_temp":os.environ["RUNNER_TEMP"],"run_id":"actions-"+ident,"id":ident}
    patterns = [x.format_map(values) for x in request.get("publish_output_globs",{}).get(a.lane,[])]
    try:
        publisher = Publisher(repo,work,out,request)
        if a.lane == "sync":
            publisher.sources()
        publisher.import_inputs(a.lane,values)
        for stage in request.get("stages",[]):
            if stage.get("lane") != a.lane:
                continue
            prior = {r["name"]:r for r in results}
            missing = [dep for dep in stage.get("depends_on",[])
                       if dep not in prior or prior[dep]["exit_code"] != 0
                       or prior[dep]["signal"] is not None]
            if missing:
                save(out / (stage["name"]+"-skipped.json"),
                     {"name":stage["name"],"status":"not-started","dependencies":missing})
                continue
            row = run_stage(stage,repo,out,publisher,values); results.append(row)
            publisher.outputs(patterns)
            if row["exit_code"] != 0 or row["signal"] is not None:
                failure = "stage nonzero: " + stage["name"]
                if not request.get("continue_independent",False):
                    break
    except BaseException as e:
        failure = type(e).__name__ + ": " + str(e)
        import traceback
        traceback.print_exc()
    finally:
        save(out / "recovery-status.json",{"utc":utc(),"actual_results":results,
             "failure":failure,"task_complete":False,"old_local_r7_terminal":"unknown"})
        if publisher is not None:
            try:
                publisher.outputs(patterns)
            except BaseException as e:
                save(out / "publication-failure.json",{"utc":utc(),"error":str(e)})
                raise
    return 1 if failure else 0
if __name__ == "__main__":
    raise SystemExit(main())
