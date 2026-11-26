#!/usr/bin/env python3
"""Held10 same-runner command worker; publishes compact diagnostics, never arrays.
It does not certify a surface or change any numerical acceptance gate.
Run from a main checkout with persist-credentials:false and contents:write.
Only GITHUB_TOKEN in this process is used for the one result Contents API write.
"""
import argparse, base64, hashlib, json, os, re, signal, subprocess, sys, time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-held-10pct"
COMMAND = TOPIC + "/ci/live-material-command.json"
RESULT = TOPIC + "/ci/live-material-result.json"
RULES = ["README.md", TOPIC + "/README.md"]
LIMIT = 64 * 1024
ALLOWED = set("""status scope error exception returncode solver_success solver_status
solver_message metric metric_max audit c2_audit rms nodes iterations accepted_raw
accepted_directory stages progress summary result results physical_bc_max
actual_bc_max tail_seam_converged tail_residual actual_tail_requested
complete_surface fixed_metric_refinement phase tau target tau_reached
parameter_scales core_settings gauge_q modes angular probe_passed
domain_rejections merit_rejections accepted_steps total_steps reason
original_linear_DN_physical_residual residual initial_metrics final_metrics
inlet terminal minimum_margin maximum_metric current_stage next_stage
metric_gate_passed true_tail_gate_passed finite_only raw_sha256 physical_sha256
physical_controls actual_core_corrections candidate_H controls diagnostics
source_hashes accepted error_kind metric_maxima Darboux prefix_audit raw_return
actual_outer_checks tail_seam domain_newton_stats domain_error_counts
boundary_kind original_nonlinear_DN_accepted
""".split())
FORBIDDEN = set("x y c matrix matrices jacobian jacobians mesh pp_coefficients cubic_c cubic_x coefficients field fields raw_array arrays data".split())
VOLATILE = set("timestamp updated_at utc elapsed elapsed_seconds wall_seconds wall_time_seconds runtime_seconds".split())

def compact(value, depth=0):
    if depth > 8:
        return "[omitted: nesting]"
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        return value[:2048]
    if isinstance(value, dict):
        return {str(k): compact(v, depth+1) for k,v in list(value.items())[:64]
                if k not in FORBIDDEN and k not in VOLATILE}
    if isinstance(value, list):
        if len(value) > 64 or any(isinstance(v, list) for v in value):
            return "[omitted: array]"
        return [compact(v, depth+1) for v in value]
    return "[omitted: type]"

def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      allow_nan=False, separators=(",", ":")).encode()

def main():
    global COMMAND, RESULT
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--workdir", type=Path, required=True)
    ap.add_argument("--channel", choices=("material", "lowq", "warm", "design"), default="material",
                    help="Separate reviewed command/result streams on distinct runners")
    a = ap.parse_args()
    if a.channel != "material":
        COMMAND = TOPIC + "/ci/live-" + a.channel + "-command.json"
        RESULT = TOPIC + "/ci/live-" + a.channel + "-result.json"
    repo, work = a.repo.resolve(), a.workdir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    if work == repo or repo in work.parents:
        raise ValueError("Work directory must be outside the repository")
    token = os.environ["GITHUB_TOKEN"]
    env = {k:v for k,v in os.environ.items()
           if not any(w in k.upper() for w in ("TOKEN", "SECRET", "PASSWORD"))}
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
        env[key] = "1"
    state_path = work / ("live-" + a.channel + "-worker-state.json")
    state = json.loads(state_path.read_text()) if state_path.exists() else {"seen": {}}
    state.setdefault("seen", {})
    def save():
        tmp = state_path.with_suffix(".tmp")
        tmp.write_bytes(encoded(state))
        tmp.replace(state_path)
    def api(method, path, body=None):
        data = None if body is None else encoded(body)
        req = Request("https://api.github.com/repos/"+REPOSITORY+"/"+path,
                      data=data, method=method, headers={
                          "Authorization":"Bearer "+token,
                          "Accept":"application/vnd.github+json",
                          "X-GitHub-Api-Version":"2022-11-28",
                          "Cache-Control":"no-cache",
                          "User-Agent":"held10-live-material-worker"})
        for attempt in range(4):
            try:
                with urlopen(req, timeout=25) as r:
                    return json.load(r)
            except HTTPError as e:
                if e.code == 404 and method == "GET":
                    return None
                if attempt == 3 or (e.code != 429 and e.code < 500):
                    raise
            except URLError:
                if attempt == 3:
                    raise
            time.sleep((2,5,12)[attempt])
    def get_content(path):
        obj = api("GET", "contents/"+path+"?ref=main")
        if obj is None:
            return None, None
        return json.loads(base64.b64decode(obj["content"])), obj["sha"]
    def publish(payload):
        payload = dict(payload, schema="held10-live-material-v1",
                       complete_surface=False)
        data = encoded(payload)
        if len(data) > LIMIT:
            # Preserve current states when verbose histories exceed the same
            # original 64 KiB bound. Complete source/run files remain local.
            diagnostics_original = payload.get("diagnostics", {})
            reduced = {}
            for path, row in diagnostics_original.items():
                if not isinstance(row, dict):
                    continue
                value = {k:v for k,v in row.items()
                         if k not in ("stages", "source_hashes", "scope", "exception")}
                if isinstance(value.get("results"), list):
                    value["results"] = value["results"][-3:]
                reduced[path] = value
            payload["diagnostics"] = reduced
            payload["diagnostic_projection_reduced"] = True
            data = encoded(payload)
            if len(data) > LIMIT:
                payload["diagnostics"] = {
                    path:{key:value for key,value in row.items()
                          if key in ("status", "error", "returncode", "solver_success")}
                    for path,row in reduced.items()}
                payload["diagnostic_detail_scope"] = "Only current states fit; request a narrower active projection."
                data = encoded(payload)
        if len(data) > LIMIT:
            payload = {"schema":"held10-live-material-v1","status":"result_too_large",
                       "id":payload.get("id"),"complete_surface":False}
            data = encoded(payload)
        digest = hashlib.sha256(data).hexdigest()
        if state.get("published_digest") == digest:
            return
        while True:
            old, sha = get_content(RESULT)
            if old is not None and encoded(old) == data:
                break
            body = {"message":"held10: live material "+str(payload.get("status","result")),
                    "content":base64.b64encode(data+b"\n").decode(), "branch":"main"}
            if sha:
                body["sha"] = sha
            try:
                api("PUT", "contents/"+RESULT, body)
                break
            except HTTPError as e:
                if e.code == 409:
                    continue
                if e.code == 422:
                    detail = e.read().decode("utf-8", "replace").lower()
                    if any(term in detail for term in
                           ("sha does not match", "sha wasn't supplied", "not a fast forward",
                            "is at", "but expected", "reference update failed")):
                        continue
                raise
        state["published_digest"] = digest
        save()
    def git(*args):
        r = subprocess.run(["git","-C",str(repo),*args], env=env, text=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if r.returncode:
            raise RuntimeError("git "+args[0]+" failed: "+r.stderr[-2000:])
        return r.stdout.strip()
    last_pull = -1e30
    def pull():
        nonlocal last_pull
        before = git("rev-parse", "HEAD")
        git("pull", "--rebase", "origin", "main")
        head = git("rev-parse", "HEAD")
        diff = git("diff", before, head, "--", *RULES)
        last_pull = time.monotonic()
        state["last_pull_commit"] = head
        save()
        return head, diff
    def rules_diff(request):
        ref = request.get("read_rules_commit", "")
        if not re.fullmatch(r"[0-9a-f]{40}", ref):
            raise ValueError("read_rules_commit must be the reviewed full commit")
        try:
            git("cat-file", "-e", ref+"^{commit}")
        except RuntimeError:
            git("fetch", "--no-tags", "--depth=1", "origin", ref)
        return git("diff", ref, "HEAD", "--", *RULES)
    def substitute(value):
        if not isinstance(value, str) or "\0" in value or "\n" in value:
            raise ValueError("Arguments must be single-line strings")
        value = value.replace("@REPO@", str(repo)).replace("@WORK@", str(work))
        candidate = value.split("=",1)[-1] if value.startswith("--") else value
        if candidate.startswith("/"):
            p = Path(candidate).resolve()
            topic = (repo/TOPIC).resolve()
            if not (p == repo or p == work or work in p.parents
                    or p == topic or topic in p.parents):
                raise ValueError("Argument path leaves task directories")
        if ".." in Path(candidate).parts:
            raise ValueError("Parent path components are not accepted")
        return value
    def diagnostics(request):
        out = {}
        for item in request.get("diagnostics", [])[:12]:
            p = Path(substitute(item["path"])).resolve()
            if work not in p.parents or p.suffix != ".json":
                raise ValueError("Diagnostic must be a JSON file under workdir")
            keys = item["keys"]
            if not isinstance(keys, list) or not set(keys) <= ALLOWED:
                raise ValueError("Diagnostic top key is not whitelisted")
            if not p.exists():
                continue
            if p.stat().st_size > 1024*1024:
                out[str(p.relative_to(work))] = {"omitted":"Input JSON exceeds 1 MiB"}
                continue
            try:
                raw = json.loads(p.read_text())
                if not isinstance(raw, dict):
                    raise ValueError("Diagnostic root is not an object")
                out[str(p.relative_to(work))] = {k:compact(raw[k]) for k in keys if k in raw}
            except (OSError, ValueError):
                continue
        return out
    def stop(proc):
        if proc is None or proc.poll() is not None:
            return
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            proc.wait(timeout=25)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.wait()
    started = idle_since = time.monotonic()
    proc = request = output = None
    payload = {"status":"worker_ready","workdir":str(work)}
    try:
        pull()
        publish(payload)
        while True:
            now = time.monotonic()
            if now-started >= 5.5*3600 or (proc is None and now-idle_since >= 1800):
                stop(proc)
                publish(dict(payload, status="worker_deadline" if proc else "worker_idle_limit",
                             diagnostics=diagnostics(request) if request else {}))
                return
            if now-last_pull >= 3500:
                head, changed = pull()
                if request and rules_diff(request):
                    stop(proc)
                    proc = None
                    if output is not None and not output.closed:
                        output.close()
                    payload = {"status":"rules_changed","id":request["id"],
                               "head":head,"rules_diff":rules_diff(request)[:16000]}
                    publish(payload)
                    idle_since = time.monotonic()
            if proc is not None:
                ended = proc.poll()
                if ended is not None:
                    output.close()
                    state["seen"][request["id"]] = {"status":"finished","returncode":ended}
                    save()
                    payload = dict(payload, status="finished",returncode=ended,
                                   diagnostics=diagnostics(request))
                    publish(payload)
                    proc = None
                    idle_since = time.monotonic()
                elif now-state.get("last_diagnostic_poll",0) >= 60:
                    # An unchanged active command may narrow or extend only
                    # its validated diagnostic projection, without restart.
                    try:
                        candidate, _ = get_content(COMMAND)
                        if (candidate and candidate.get("id") == request["id"]
                                and candidate.get("script") == request.get("script")
                                and candidate.get("args", []) == request.get("args", [])):
                            diagnostics(candidate)
                            request = dict(request, diagnostics=candidate.get("diagnostics", []))
                    except (HTTPError, URLError):
                        pass
                    publish(dict(payload,diagnostics=diagnostics(request)))
                    state["last_diagnostic_poll"] = now
            if proc is None:
                incoming, _ = get_content(COMMAND)
                if (incoming and incoming.get("id") not in state["seen"]
                        and hashlib.sha256(encoded(incoming)).hexdigest() != state.get("blocked_request_digest")):
                    ident = incoming.get("id","")
                    if not re.fullmatch(r"[A-Za-z0-9_.-]{1,96}", ident):
                        raise ValueError("Invalid command id")
                    head, changed = pull()
                    # Re-read the actual checked-out request after the true pull.
                    incoming = json.loads((repo/COMMAND).read_text())
                    if incoming.get("id") != ident:
                        continue
                    diff = rules_diff(incoming)
                    if diff:
                        state["blocked_request_digest"] = hashlib.sha256(encoded(incoming)).hexdigest()
                        save()
                        publish({"status":"rules_changed","id":ident,"head":head,
                                 "rules_diff":diff[:16000]})
                    else:
                        script = (repo/incoming["script"]).resolve()
                        allowed = (repo/TOPIC/"scripts").resolve()
                        if allowed not in script.parents or script.suffix != ".py" or not script.is_file():
                            raise ValueError("Only an existing held10 Python script is accepted")
                        args = [substitute(v) for v in incoming.get("args",[])]
                        diagnostics(incoming)  # Validate projection before any execution.
                        command = [sys.executable,"-u",str(script),*args]
                        state["seen"][ident] = {"status":"started","commit":head}
                        save()  # A restarted worker never repeats a launched id.
                        request = incoming
                        payload = {"status":"running","id":ident,"commit":head,
                                   "script":incoming["script"],
                                   "script_sha256":hashlib.sha256(script.read_bytes()).hexdigest()}
                        publish(payload)
                        output = (work/("live-"+ident+".log")).open("wb")
                        proc = subprocess.Popen(command,cwd=repo,env=env,stdout=output,
                                                stderr=subprocess.STDOUT,start_new_session=True)
                        state["last_diagnostic_poll"] = 0
            time.sleep(30)
    except Exception as exc:
        stop(proc)
        try:
            publish(dict(payload, status="worker_error",
                         error=type(exc).__name__+": "+str(exc)[:2000]))
        except Exception:
            pass
        raise
    finally:
        if proc is not None and proc.poll() is None:
            stop(proc)
        if output is not None and not output.closed:
            output.close()

if __name__ == "__main__":
    main()
