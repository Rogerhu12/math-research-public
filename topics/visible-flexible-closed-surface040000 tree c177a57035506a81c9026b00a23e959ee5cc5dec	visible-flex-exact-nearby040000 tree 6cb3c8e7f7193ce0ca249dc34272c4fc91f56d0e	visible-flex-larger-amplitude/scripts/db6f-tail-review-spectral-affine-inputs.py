#!/usr/bin/env python3
"""Read-only independent AST/hash/closed-metadata audit; never imports runner.

No NumPy/SciPy, prefix object, source initializer, flow, tail client or solver.
Only this independent checker and its new JSON output are executed.
"""
import argparse
import ast
import gzip
from hashlib import sha256
import json
import math
from pathlib import Path

T = Path(__file__).resolve().parents[1]
P = "2026-11-09-db6f-"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def identity(path):
    p = Path(path).resolve()
    h = sha256()
    with p.open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return {"path": str(p), "bytes": p.stat().st_size, "sha256": h.hexdigest()}


def read(path):
    p = Path(path)
    if p.suffix == ".gz":
        with gzip.open(p, "rt") as stream:
            return json.load(stream)
    return json.loads(p.read_text())


def source_definitions(path):
    text = Path(path).read_text()
    lines = text.splitlines()
    result = {}
    def walk(body, prefix):
        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                name = prefix + node.name
                result[name] = node
                if isinstance(node, ast.ClassDef):
                    inside = name + "."
                else:
                    inside = name + ".<locals>."
                walk(node.body, inside)
    walk(ast.parse(text).body, "")
    return lines, result


def finite(v):
    return type(v) in (int, float) and math.isfinite(v)


def vector(v, n):
    return isinstance(v, list) and len(v) == n and all(finite(x) for x in v)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    output = Path(args.out).resolve()
    assert not output.exists()
    runner = T / "scripts/db6f-prefix-spectral-affine-replay.py"
    preparer = T / "scripts/db6f-prefix-prepare-spectral-affine-m14.py"
    launch_path = T / "notes" / (P + "prefix-spectral-affine-m14q512-01-launch.json")
    expected = [(runner,"ad219dbab80278670665ac3cb5401cb55daf33834cea8495dd16bf1c1396e4bd"),
                (preparer,"915c3701e8b2de3857e10e7462e09630a5d5f4f955fc77882723788f1344fc99"),
                (launch_path,"e45c553ea6832525c6a2719a197dbcc49a7ee5dd77badfb4b363e19a4b974a83")]
    for path,wanted in expected:
        assert identity(path)["sha256"] == wanted
    launch = read(launch_path)
    assert launch["schema"] == "db6f-spectral-affine-m14q512-v1"
    settings = {"modes":14,"angular":512,"tol":2e-9,"bc_tol":1e-8,
                "physical_bc_tol":2e-11,"max_nodes":6500}
    flags = {"actual_nonlinear_tail":False,"frozen_affine_dn":True}
    assert canonical(launch["settings"]) == canonical(settings)
    assert canonical(launch["scope_flags"]) == canonical(flags)
    assert all(launch[k] is v for k,v in flags.items())
    bindings = launch["bindings"]
    assert len(bindings) == 97
    for row in bindings:
        assert identity(row["path"]) == row
    bypath = {row["path"]:row for row in bindings}
    assert len(bypath) == len(bindings)
    callbacks=[]
    for label, row in launch["callbacks"].items():
        assert bypath[row["file"]["path"]] == row["file"]
        lines, definitions=source_definitions(row["file"]["path"])
        node=definitions[row["qualname"]]
        assert isinstance(node, ast.FunctionDef) and not node.decorator_list
        assert node.lineno == row["first_line"]
        source="\n".join(lines[node.lineno-1:node.end_lineno]).rstrip()
        assert sha256(source.encode()).hexdigest() == row["source_sha256_rstrip"]
        callbacks.append(label)
    assert len(callbacks) == 15
    for name in ("checkpoint","frozen_tail","linear_port","profile","chart","tail_config"):
        assert identity(launch[name]["path"]) == launch[name]
        assert bypath[launch[name]["path"]] == launch[name]
    rec,tail,port=[read(launch[k]["path"]) for k in ("checkpoint","frozen_tail","linear_port")]
    cfg=rec["config"]
    assert rec["solver_success"] is True and cfg["actual_nonlinear_tail"] is True and cfg["fixed_metric"] is True
    for key in ("modes","angular","tol","bc_tol","physical_bc_tol"):
        assert canonical(cfg[key]) == canonical(settings[key])
    physical=("angular_chart","chart","frozen_profile","physical_tail_parameters","physical_tail_cut","warp_reference_q")
    assert canonical({k:rec[k] for k in physical}) == canonical(launch["frozen_physical_fields"])
    assert canonical(rec["gauge_amplitude"]) == canonical(launch["gauge_amplitude"])
    assert rec["physical_port_sha256"] == launch["linear_port"]["sha256"]
    assert canonical(rec["physical_tail_parameters"]) == canonical(port["parameters"])
    assert canonical(rec["physical_tail_cut"]) == canonical(port["cut"])
    for key in ("chart","frozen_profile","tail_config"):
        pathkey="profile" if key=="frozen_profile" else key
        assert canonical(rec[key]) == canonical(read(launch[pathkey]["path"]))
    assert canonical(rec["tail_config"]) == canonical(tail["config"])
    assert (Path(launch["checkpoint"]["path"]).parent/rec["tail_seam"]["tail_record"]).resolve() == Path(launch["frozen_tail"]["path"])
    response=tail["response"];request=tail["request"]
    assert response["converged"] is True and finite(response["residual"]) and 0 <= response["residual"] < 2e-9
    assert request["jacobian"] is True and request["audit"] is True
    assert vector(request["height"],14) and vector(response["heightJetJacobian"],616)
    jets=response["jets"]
    scalar_keys={"radius","backgroundSlope","backgroundSecond","E","Ep","meanSlope","meanSecond",
                 "meanSlopeCorrection","meanSecondCorrection","minLeading","minD","endpointFullD","endpointPhi","formalCurvature"}
    assert set(jets) == scalar_keys|{"height","slope","second"}
    assert all(finite(jets[k]) for k in scalar_keys)
    assert all(vector(jets[k],14) for k in ("height","slope","second"))
    audit_keys={"fullD","normalizedFullDefect","minLeading","minD","formalCurvature","maxPhysicalPV","actualMetric","holonomy"}
    assert set(response["audit"]) == audit_keys and all(finite(v) for v in response["audit"].values())
    assert canonical(tail["source_sha256"]) == canonical(launch["frozen_tail_sources"])
    assert len(tail["source_sha256"]) == 8
    for name,expected_sha in tail["source_sha256"].items():
        assert identity(T/"scripts"/name)["sha256"] == expected_sha
    assert canonical(response["checkpoint"]["cutHeight"]) == canonical(request["height"])
    assert rec["tail_seam"]["tail_converged"] is True
    assert canonical(rec["tail_seam"]["tail_shooting_residual"]) == canonical(response["residual"])
    coeff=[]
    for row in rec["pp_coefficient_chunks"]:
        p=Path(launch["checkpoint"]["path"]).parent/row["file"]
        actual=identity(p)
        assert actual["sha256"] == row["sha256"] and actual["bytes"] == row["bytes"]
        assert bypath[str(p.resolve())] == actual
        coeff.append(actual)
    block=[float(2**(9*j*j).bit_length()) for j in range(1,15)]
    weights=[1.]+block*3
    assert canonical(weights) == canonical(launch["weights"]) and len(weights)==43
    assert all(1+9*j*j <= block[j-1] < 2*(1+9*j*j) for j in range(1,15))
    root=Path(launch["source_root"]).resolve()
    assert root == T/"repro/source-root"
    newton=root/"topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py"
    assert launch["callbacks"]["domain_solve_newton"]["file"]["path"] == str(newton)
    _,defs=source_definitions(newton)
    assert [a.arg for a in defs["solve_newton"].args.args] == ["n","m","h","col_fun","bc","jac","y","p","B","bvp_tol","bc_tol"]
    # Pure static guard: this entry calls only the reviewed affine replacement,
    # never the original outer actual-DN routine or a tail-port constructor.
    tree=ast.parse(runner.read_text())
    called=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Call):
            fn=node.func
            if isinstance(fn,ast.Name):called.append(fn.id)
            elif isinstance(fn,ast.Attribute):called.append(fn.attr)
    assert "WeightedTailPort" not in called and "solve_with_actual_tail" not in called and "seam_audit" not in called
    assert called.count("solve_bvp") == 1 and called.count("AffineTailForInnerBVP") == 1
    prefix=Path(launch["out_prefix"])
    assert prefix.parent == T/"notes"
    for key in ("stdout_log","reproduction_file","summary_file","checkpoint_output","coefficient_output_pattern"):
        p=Path(launch[key]);assert p.parent == prefix.parent and p.name.startswith(prefix.name)
        assert str(p) not in bypath
    assert launch["command"][1:] == [str(runner),"--launch",str(launch_path)]
    assert launch["cwd"] == str(T.parents[1])
    prep=read(T/"notes"/(P+"prefix-spectral-affine-m14q512-01-preparation.json"))
    assert prep["launch"] == identity(launch_path)
    for k in ("actual_new_DN_calls","actual_BVP_calls","actual_flow_or_bridge_initializations", "actual_newton_install_calls","actual_weighted_solver_factory_calls"):
        assert type(prep[k]) is int and prep[k] == 0
    report={"status":"PASS_METADATA_AND_AST_FOR_FROZEN_AFFINE_SPECTRAL_RUNNER",
            "script":identity(Path(__file__)),"runner":identity(runner),"preparer":identity(preparer),"launch":identity(launch_path),
            "binding_count":len(bindings),"callback_AST_identities":callbacks,
            "physical_state_components":43,"unchanged_parameter_components":14,"physical_restart_fields":list(physical),
            "original_true_DN_J_length":616,"original_true_jets_scalar_count":14,"original_true_jets_vector_count":3,
            "original_true_audit_keys":sorted(audit_keys),"frozen_tail_source_count":8,"original_coefficient_chunks":coeff,
            "scope_flags":flags,"settings":settings,"weight_definition":"mean=1; each of R/T/Z mode j uses 2**bit_length(9*j*j)",
            "runtime_newton_identity_and_signature_are_future_runtime_gates":True,
            "only_metadata_and_AST_executed":True,"prefix_objects":0,"flow_initializations":0,
            "newton_install_calls":0,"solver_factory_calls":0,"actual_BVP_or_DN_calls":0}
    with output.open("x") as f:
        json.dump(report,f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({"status":report["status"],"bindings":len(bindings),"callbacks":len(callbacks),
                      "bytes":output.stat().st_size,"sha256":sha256(output.read_bytes()).hexdigest()}))


if __name__=="__main__":
    main()
