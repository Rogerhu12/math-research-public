"""ASQ11 successor after the terminal zero-target gate-list type failure."""
import argparse
import ast
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request
from zipfile import ZipFile

TOPIC="topics/visible-flex-exact-nearby"
SOURCE=TOPIC+"/scripts/fourfold_codazzi_actual_positive_i_after_gate_list.py"
OLD=TOPIC+"/scripts/fourfold_codazzi_actual_positive_i_model_fees.py"
OLD_SHA="80f4f6705af547ac068e9fe6d86fd3db293fd29f19c52879a8df5342bf48874f"
WF=".github/workflows/visible-exact-original-positive-i-after-gate-list.yml"
PARENT="46136643646"
JOB=140953320244
EVENT="dfb9991cce548ba258ab0f658180628cc14cb9e2"
LOG="0_consume-saved-original-1502-candidates.txt"
LOG_SHA="32cf100144139eef96080b96ced9c5ba819cc88595ddd2f3cf16277223ba74b4"


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def gate_list(gates):
    return (isinstance(gates,list) and len(gates)==11 and
            all(set(g)=={"name","passed"} and isinstance(g["name"],str) and g["passed"] is True for g in gates))


def build(raw):
    require(sha(raw)==OLD_SHA,"whole previous scientific source")
    tree=ast.parse(raw)
    target=ast.dump(ast.parse('p["mathematical_gates"] == 11',mode="eval").body)
    count=0
    class Repair(ast.NodeTransformer):
        def visit_Compare(self,node):
            nonlocal count
            if ast.dump(node)==target:
                count+=1
                fixed=ast.parse('gate_list(p["mathematical_gates"])',mode="eval").body
                return ast.copy_location(fixed,node)
            return self.generic_visit(node)
    tree=Repair().visit(tree)
    require(count==1,"only the unique original wrong scalar-versus-list comparison changes")
    return ast.fix_missing_locations(tree)


def terminal():
    base="https://api.github.com/repos/Rogerhu12/math-research-public/actions/"
    headers={"Authorization":"Bearer "+os.environ["GITHUB_TOKEN"],"Accept":"application/vnd.github+json"}
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,*args,**kwargs):
            return None
    api=urllib.request.build_opener(NoRedirect)
    def get(path,allow_signed_download=False):
        req=urllib.request.Request(base+path,headers=headers)
        try:
            with api.open(req,timeout=60) as res:
                return res.read()
        except urllib.error.HTTPError as error:
            if not allow_signed_download or error.code!=302:
                raise
            location=error.headers["Location"]
            require(urllib.parse.urlsplit(location).scheme=="https","the signed log location uses HTTPS")
        with urllib.request.urlopen(location,timeout=60) as res:
            return res.read()
    run_raw=get("runs/"+PARENT+"/attempts/1")
    job_raw=get("jobs/"+str(JOB))
    run,job=map(json.loads,(run_raw,job_raw))
    require(str(run["id"])==str(job["run_id"])==PARENT and run["run_attempt"]==job["run_attempt"]==1
            and job["id"]==JOB and run["status"]==job["status"]=="completed"
            and run["conclusion"]==job["conclusion"]=="failure" and run["head_sha"]==job["head_sha"]==EVENT,
            "one real terminal original public failure before any new combination")
    archive=get("runs/"+PARENT+"/logs",allow_signed_download=True)
    with ZipFile(io.BytesIO(archive)) as package:
        raw=package.read(LOG)
    require(len(raw)==198234 and sha(raw)==LOG_SHA and
            raw.count(b"ValueError: original actual all-integer norm and actual finite Cayley conclusions")==1 and
            b"ASQ11 COMPLETE SMALL CONCLUSION bytes=" not in raw,
            "whole original job log proves failure at its first metadata check and zero new targets")
    return {"parent_run":PARENT,"parent_attempt":"1","parent_job":JOB,"parent_event":EVENT,
            "whole_parent_run_API_sha256":sha(run_raw),"whole_parent_job_API_sha256":sha(job_raw),
            "whole_parent_job_log_bytes":len(raw),"whole_parent_job_log_sha256":sha(raw),"completed_new_parent_targets":0}


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--source-sha",required=True)
    args,_=parser.parse_known_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ["GITHUB_RUN_ATTEMPT"]=="1"
            and os.environ["GITHUB_REPOSITORY"]=="Rogerhu12/math-research-public" and
            os.environ["GITHUB_RUN_ID"]!=PARENT and sha(Path(__file__).read_bytes())==args.source_sha,
            "new exact first run identity and whole current owner")
    parent=terminal()
    root=args.repo.resolve()
    env={"__name__":"_ASQ11_original_with_whole_gate_list","__file__":__file__,"gate_list":gate_list}
    exec(compile(build((root/OLD).read_bytes()),"<complete ASQ11 corrected gate-list reader>","exec"),env)
    science=env["arithmetic"]
    def carried(inputs,native):
        return {**science(inputs,native),"terminal_zero_target_parent":parent,"old_scientific_source_sha256":OLD_SHA}
    env.update(SOURCE=SOURCE,WF=WF,arithmetic=carried)
    return env["main"]()


if __name__=="__main__":
    main()
