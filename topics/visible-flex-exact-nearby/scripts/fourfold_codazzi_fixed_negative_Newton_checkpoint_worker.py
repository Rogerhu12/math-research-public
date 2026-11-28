"""Distinct first ASQ27R reservation conditional on the immutable failed zero-cell parent."""
import argparse
import ast
import json
import os
from pathlib import Path
import sys
from urllib.request import HTTPRedirectHandler, Request, build_opener

import fourfold_codazzi_fixed_negative_Newton_checkpoint as fixed

SOURCE = fixed.WORKER


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def terminal():
    """Use only the official API for the exact run attempt and job, without redirects."""
    base="https://api.github.com/repos/Rogerhu12/math-research-public/actions/"
    root=build_opener(NoRedirect())
    headers={"Accept":"application/vnd.github+json","User-Agent":"ASQ27R-terminal",
             "X-GitHub-Api-Version":"2022-11-28"}
    if os.getenv("GITHUB_TOKEN"):
        headers["Authorization"]="Bearer "+os.environ["GITHUB_TOKEN"]
    def get(path):
        with root.open(Request(base+path,headers=headers),timeout=30) as response:
            return json.load(response)
    run=get("runs/"+fixed.PARENT_RUN+"/attempts/1")
    job=get("jobs/"+str(fixed.PARENT_JOB))
    fixed.require(str(run["id"])==str(job["run_id"])==fixed.PARENT_RUN and job["id"]==fixed.PARENT_JOB
            and run["run_attempt"]==job["run_attempt"]==1 and job["name"]=="fixed-trajectory"
            and run["repository"]["full_name"]=="Rogerhu12/math-research-public"
            and all(row["status"]=="completed" and row["conclusion"]=="failure" and row["head_sha"]==fixed.EVENT
                    for row in (run,job)) and job["completed_at"]=="2026-11-28T13:30:23Z",
            "original terminal failed attempt and its unique actual failed scientific job")
    return {k:{a:r[a] for a in ("id","head_sha","status","conclusion","run_attempt")}
            for k,r in (("run",run),("job",job))}


def adapter(repo):
    fixed.pinned(repo,"ASQ27_worker")
    from fourfold_codazzi_fixed_negative_Newton_public_worker import adapter as original_adapter
    from fourfold_codazzi_fixed_negative_Newton_public_worker import OLD, stage_affine
    raw=(repo/OLD).read_bytes()
    tree=original_adapter(raw)
    main,=tree.body
    rename={
        "R149_fixed_affine_base_Newton_trajectory_inputs_v1":fixed.MANIFEST_KIND,
        "R149_fixed_affine_base_Newton_trajectory_execution_v1":"R149_fixed_negative_Newton_atomic_checkpoint_execution_v1",
        "consumed_fixed_affine_base_Newton_trajectory_v1":"consumed_fixed_negative_Newton_atomic_checkpoint_v1",
        "RECOVERABLE WHOLE ASQ27 FIXED NEGATIVE NEWTON BEFORE GIT ":"RECOVERABLE WHOLE ASQ27R CANONICAL CHECKPOINT BEFORE GIT ",
        "visible-exact: reserve fixed affine negative Newton trajectory":"visible-exact: reserve negative Newton after true zero-cell failure",
        "visible-exact: preserve complete fixed affine Newton suffix":"visible-exact: preserve whole atomic negative Newton suffix",
        "visible-exact: preserve fixed affine negative Newton trajectory":"visible-exact: preserve actual atomic negative Newton trajectory"}
    hits=dict.fromkeys(rename,0)
    for n in ast.walk(main):
        if isinstance(n,ast.Constant) and isinstance(n.value,str) and n.value in rename:
            hits[n.value]+=1
            n.value=rename[n.value]
    fixed.require(all(n==1 for n in hits.values()),"unique original first reservation and execution labels")
    current,=[f for f in main.body if isinstance(f,ast.FunctionDef) and f.name=="current"]
    current.body.extend(ast.parse('fixed.parent(inputs)\nstate.setdefault("terminal_parent_checks",[]).append(terminal())').body)
    last,=[stmt for stmt in main.body if isinstance(stmt,ast.Try) and stmt.finalbody and
           any(isinstance(n,ast.Assign) and ast.unparse(n.targets[0])=='state[\'finished_utc\']' for n in stmt.finalbody)]
    checkpoint,=[i for i,n in enumerate(last.finalbody) if isinstance(n,ast.Assign) and
                 isinstance(n.targets[0],ast.Name) and n.targets[0].id=="complete_small"]
    last.finalbody[checkpoint:checkpoint]=ast.parse('''try:
    current(shared["pull"]())
    state["terminal_parent_after"]=terminal()
except Exception as terminal_error:
    state["complete"]=False
    state["terminal_parent_error"]={"type":type(terminal_error).__name__,"message":str(terminal_error)}
    if state["failure"] is None:
        state["failure"]=dict(state["terminal_parent_error"],traceback=traceback.format_exc())''').body
    return ast.fix_missing_locations(tree),OLD,stage_affine


def main():
    arg=argparse.ArgumentParser(add_help=False)
    arg.add_argument("--repo",type=Path,required=True)
    args,_=arg.parse_known_args()
    root=args.repo.resolve()
    # Check the whole wrapper and reader before either is imported by the transport adapter.
    fixed.pinned(root,"ASQ27_worker")
    tree,old_path,stage_affine=adapter(root)
    from fourfold_codazzi_whole_selected_signed_source_public_worker import load
    old=load(root/old_path,"_ASQ27R_original_WSS_worker")
    scope=dict(vars(old),__file__=__file__,SOURCE=SOURCE,stage_affine=stage_affine,terminal=terminal,fixed=fixed)
    exec(compile(tree,str(old_path)+"#whole-zero-cell-terminal","exec"),scope)
    scope["main"]()


if __name__=="__main__":
    sys.dont_write_bytecode=True
    main()
