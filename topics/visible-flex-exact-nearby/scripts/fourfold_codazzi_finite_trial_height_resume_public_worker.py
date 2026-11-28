"""Public H96 suffix transport with terminal parent validation and an exclusive new consumed marker."""
import argparse
import ast
import hashlib
import importlib.util
import json
import os
import sys
import urllib.request
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
ORIGINAL = TOPIC+"/scripts/fourfold_codazzi_finite_trial_height_public_worker.py"
ORIGINAL_SHA = "1f98010b06299e843bea939f4a14974aec50b0e0db970edae5b6b836a8e1e8fd"
OWNER = TOPIC+"/scripts/fourfold_codazzi_finite_trial_height_resume_owner.py"
OWNER_SHA = "538e9198a2b04fcb75389aefe95422ab6df909be3efbfe4a412f54aeab288981"
REPO = "Rogerhu12/math-research-public"
PARENT = "46123190757"
JOB = 140911924186
EVENT = "0ed00cf191cf6ce8366db09769f6ad377ab66257"
OLD_STAGE = "complete_original_finite_trial_height_rows"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(root, path, digest, name):
    require(sha((root/path).read_bytes()) == digest, "complete immutable adapter source: "+path)
    spec = importlib.util.spec_from_file_location(name, root/path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def terminal():
    headers = {"Accept":"application/vnd.github+json","Authorization":"Bearer "+os.environ["GITHUB_TOKEN"]}
    def get(path):
        req = urllib.request.Request("https://api.github.com/repos/"+REPO+"/actions/"+path, headers=headers)
        with urllib.request.urlopen(req,timeout=60) as result:
            raw = result.read()
        obj = json.loads(raw)
        require(obj["status"] == "completed" and obj["conclusion"] == "failure"
                and obj["head_sha"] == EVENT, "public original H96 run and job actually ended on the fixed failure")
        receipt = {key:obj[key] for key in ("id","head_sha","status","conclusion","html_url")}
        return obj, {**receipt,"whole_API_bytes":len(raw),"whole_API_sha256":sha(raw)}
    run,r = get("runs/"+PARENT+"/attempts/1")
    job,j = get("jobs/"+str(JOB))
    require(str(run["id"]) == str(job["run_id"]) == PARENT and job["id"] == JOB
            and run["run_attempt"] == job["run_attempt"] == 1 and run["repository"]["full_name"] == REPO
            and job["completed_at"] and job["name"] == "first-complete-original96-height-rows",
            "terminal run and job identify this unique original H96 input")
    return {"run":r,"job":{**j,"completed_at":job["completed_at"]}}


def build_adapter(root):
    old = load(root,ORIGINAL,ORIGINAL_SHA,"_H96_original_worker")
    definitions = load(root,OWNER,OWNER_SHA,"_H96_resume_contract")
    tree = old.build_adapter(root)
    replace = {OLD_STAGE:definitions.STAGE, "R149_"+OLD_STAGE+"_inputs_v1":definitions.MANIFEST_KIND,
               "R149_"+OLD_STAGE+"_execution_v1":definitions.EXECUTION_KIND,
               "consumed_R149_"+OLD_STAGE+"_v1":"consumed_R149_"+definitions.STAGE+"_v1"}
    counts = dict.fromkeys(replace,0)
    hooks = dict.fromkeys(("materialize","final_files","validate_output"),0)
    class Bind(ast.NodeTransformer):
        def visit_Constant(self,node):
            if isinstance(node.value,str) and node.value in replace:
                counts[node.value] += 1
                return ast.copy_location(ast.Constant(replace[node.value]),node)
            return node
        def visit_FunctionDef(self,node):
            node = self.generic_visit(node)
            if node.name not in hooks:
                return node
            hooks[node.name] += 1
            if node.name == "materialize":
                node.body += ast.parse("""
receipts = state.setdefault("terminal_original_parent_checks", [])
require(attempt == "1" and run != PARENT and manifest["resume"] == definitions.RECEIPT
        and marker_path == definitions.NOTES+"finite_trial_height_after_728_ci/consumed-target.json",
        "unique successor reservation and exact prescribed original suffix")
receipts.append(terminal())
originals = {path: snapshots[role].read_bytes() for role,(path,_) in definitions.PARENT_FILES.items()}
originals[definitions.REVIEW[0]] = snapshots["reviewed_rules"].read_bytes()
old = parse(originals[definitions.ORIGINAL_MANIFEST])
originals[old["roles"]["reviewed_rules"]] = snapshots["H96_original_reviewed_rules"].read_bytes()
definitions.check_parent(originals)
""").body
            if node.name == "validate_output":
                require(isinstance(node.body[-1],ast.Return) and ast.unparse(node.body[-1].value) == "doc",
                        "original validator returns the entire actual object after every success check")
                node.body[-1:-1] = ast.parse("""
parent = parse(snapshots["H96_parent_actual"].read_bytes())
require(doc["resume"] == definitions.RECEIPT and doc["identity"]["run_id"] != PARENT
        and prefix is not None and 728 <= prefix["complete_relative_cells"] <= 2847
        and (prefix["complete_relative_cells"] != 728 or prefix == parent["height_integral_prefix"])
        and all(doc[key] is None or doc[key] == parent[key] for key in definitions.CARRIERS),
        "retained whole parent, identical full carriers, and one cumulative all96 covered prefix")
""").body
            if node.name == "final_files":
                node.body[:0] = ast.parse("""
if "terminal_original_parent_after" not in state:
    state["terminal_original_parent_after"] = terminal()
""").body
                # Name the new identity in the native report; the numerical specification is unchanged.
                for stmt in node.body:
                    if isinstance(stmt,ast.Assign) and ast.unparse(stmt.targets[0]) == "report":
                        node.body.insert(node.body.index(stmt)+1,ast.parse(
                            'report += b"Original run 46123190757/1 paid cells [0,728). This distinct run carries all 96 signed balls and the whole adjoint fee and evaluates only [728,2847).\\n"').body[0])
                        break
            return node
    tree = Bind().visit(tree)
    require(all(value == 1 for value in [*counts.values(), *hooks.values()]),
            "exact four successor identities and three whole public AST insertion sites")
    return ast.fix_missing_locations(tree)


def main():
    sys.dont_write_bytecode = True
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo",type=Path,required=True)
    args,_=parser.parse_known_args()
    root=args.repo.resolve()
    definitions=load(root,OWNER,OWNER_SHA,"_H96_current_contract")
    env={"__file__":__file__,"__name__":"_H96_after_728_public","terminal":terminal,
         "definitions":definitions,"PARENT":PARENT}
    exec(compile(build_adapter(root),"<H96 public continuation after paid 728>", "exec"),env)
    return env["main"]()


if __name__ == "__main__":
    raise SystemExit(main())
