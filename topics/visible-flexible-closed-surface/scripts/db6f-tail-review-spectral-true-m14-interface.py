#!/usr/bin/env python3
"""Static AST/metadata review only; never import a candidate or solver module."""
import argparse
import ast
import gzip
import hashlib
import json
import math
from pathlib import Path

T = Path(__file__).resolve().parent.parent
N = T / "notes"
S = T / "scripts"
P = "2026-11-09-db6f-"


def read(p):
    p = Path(p)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == ".gz" else raw)


def identity(p):
    p = Path(p).resolve()
    raw = p.read_bytes()
    return {"path":str(p),"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--out", type=Path, required=True)
    args = a.parse_args()
    out = args.out.resolve()
    assert T in out.parents and not out.exists()
    method = N / (P + "prefix-spectral-true-m14-interface.md")
    ledger = N / (P + "prefix-spectral-true-m14-interface-sources.json")
    publication = N / (P + "prefix-spectral-true-m14-interface-publication.json")
    assert identity(method)["sha256"] == "39516e14f7185ecd4ff14c3a4df7c8501794a90bc34be0bb2622371f0b6c3f6d"
    assert identity(ledger)["sha256"] == "150a196fc14b79ec21f0cae635d32f8635617ee79b14edd646b5449e50c50800"
    data, pub = read(ledger), read(publication)
    source = {}
    def check(row):
        actual = identity(row["path"])
        assert actual["sha256"] == row["sha256"] and actual["bytes"] == row["bytes"]
        source[actual["path"]] = actual
    for row in pub["files"]:
        check(row)
    assert len(data["source_bindings"]) == 39
    for row in data["source_bindings"]:
        check(row)
    launch_path = N / (P + "prefix-spectral-affine-m14q512-01-launch.json")
    launch = read(launch_path)
    assert len(launch["bindings"]) == 97
    for row in launch["bindings"]:
        check(row)

    tree = ast.parse((S / "db6f-prefix-coupled.py").read_text())
    fn = next(x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == "solve_with_actual_tail")
    bvp_calls = [x for x in ast.walk(fn) if isinstance(x, ast.Call) and isinstance(x.func, ast.Name) and x.func.id == "solve_bvp"]
    assert len(bvp_calls) == 2
    assert not any(isinstance(x, ast.Name) and isinstance(x.ctx, ast.Store) and x.id == "solve_bvp" for x in ast.walk(fn))
    assert not any(arg.arg == "solve_bvp" for arg in fn.args.args)
    restore = [x for x in ast.walk(fn) if isinstance(x, ast.Try) and x.finalbody]
    assert len(restore) == 1
    restored = restore[0].finalbody
    assert len(restored) == 1 and ast.unparse(restored[0]) == "o.tail = tail"
    loop = next(x for x in fn.body if isinstance(x, ast.For))
    assert ast.unparse(loop.iter) == "range(8)"
    assert "actual = tail.solve(candidate, jacobian=True, audit=False)" in ast.unparse(fn)
    assert "if defect <= a.bc_tol:" in ast.unparse(fn)

    M = 14
    block = [1 << (9*j*j).bit_length() for j in range(1,M+1)]
    weights = [1] + block * 3
    assert weights == launch["weights"] and len(weights) == 43 and max(weights) == 2048
    assert all(1+9*j*j <= w < 2*(1+9*j*j) for j,w in enumerate(block,1))
    expected = dict(M=14,prefix_state_components=43,parameters=14,central_correction_scales=13,
                    tail_height_jacobian_entries=(3*M+2)*M,tail_state_rows=865,tail_state_columns=28,
                    raw_state_rows=13,raw_state_columns=28,jet_scalar_fields=14,jet_vector_fields=3,
                    jet_vector_length=14,audit_fields=8,seam_angular_samples=max(512,64*M),
                    export_degree192_coefficient_count=143,export_degree192_stride=575,
                    export_1000_rows_uncompressed_bytes=4600000)
    planar = [m for m in range(-192,193) if (m-1)%3 == 0]
    assert len(planar) == 128 and len(planar)+M+1 == 143
    assert (3+4*143)*1000*8 == 4600000
    assert data["static_dimensions"] == expected

    stem = P + "prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14"
    cp_path = N / (stem + ".json.gz")
    cp = read(cp_path)
    assert cp["solver_success"] is True and cp["config"]["actual_nonlinear_tail"] is True
    assert cp["config"]["modes"] == M
    assert len(cp["parameters"]) == M and len(cp["central_correction_scales"]) == M-1
    assert cp["tail_seam"]["angular_samples"] == 896
    assert cp["tail_seam"]["tail_record"] == stem + "_tail_0002.json.gz"
    previous = 0
    for chunk in cp["pp_coefficient_chunks"]:
        path = N / chunk["file"]
        actual = identity(path)
        assert actual["bytes"] == chunk["bytes"] and actual["sha256"] == chunk["sha256"]
        assert chunk["state_first"] == previous
        previous = chunk["state_last_exclusive"]
        source[actual["path"]] = actual
    assert previous == 43
    tail = read(N / cp["tail_seam"]["tail_record"])
    r = tail["response"]
    assert tail["request"]["jacobian"] is True and tail["request"]["audit"] is True
    assert r["converged"] is True and 0 <= r["residual"] < 2e-9
    assert len(r["heightJetJacobian"]) == 616 and all(math.isfinite(x) and not isinstance(x,bool) for x in r["heightJetJacobian"])
    assert len(r["jets"]) == 17 and len(r["audit"]) == 8
    assert all(len(r["jets"][k]) == 14 for k in ("height","slope","second"))
    assert len(r["checkpoint"]["states"]) == 865 and all(len(x)==28 for x in r["checkpoint"]["states"])
    assert len(r["checkpoint"]["rawStates"]) == 13 and all(len(x)==28 for x in r["checkpoint"]["rawStates"])
    assert len(tail["source_sha256"]) == 8
    for name,h in tail["source_sha256"].items():
        actual=identity(S/name);assert actual["sha256"]==h;source[actual["path"]]=actual
    cfg=read(N/(stem+'-tail-config.json'))
    assert (cfg['modes'],cfg['spacing'],cfg['depth'],cfg['shootingParts'],cfg['steps'],cfg['quadrature'],cfg['maxIterations'],cfg['solveTolerance']) == (14,3,12,8,32,512,36,2e-9)
    assert 'trialDiagnosticFile' not in cfg and 'trialStatePrefix' not in cfg
    assert 'correctInitialBoundary' not in cfg and 'projectionFloor' not in cfg
    for row in source.values():
        assert identity(row['path'])==row
    report={
        'status':'PASS_STATIC_TRUE_M14_SPECTRAL_INTERFACE_SOURCE_AND_METADATA_CHECK',
        'reviewer':'/root/tail_theory','script':identity(__file__),
        'method':identity(method),'source_ledger':identity(ledger),'publication':identity(publication),
        'source_entries_checked':39,'old_affine_launch_entries_checked':97,
        'unique_files_rehashed':len(source),'source_files':sorted(source.values(),key=lambda x:x['path']),
        'two_unshadowed_module_global_solve_bvp_calls':True,
        'lagged_original_eight_outer_loops_and_finally_restore_preserved':True,
        'true_candidate_DN_and_original_BC_remain_separate_from_inner_affine_physical_BC':True,
        'integer_weight_and_schema_checks':expected,
        'old_successful_M14_own_final_tail_schema_checked':True,
        'future_runtime_newton_identity_observed':False,
        'future_selector_implemented_or_reviewed_by_this_check':False,
        'candidate_class_imports_or_initializations':0,'new_solver_root_flow_DN_BVP_calls':0,
        'old_source_or_candidate_modified':False,
        'scope':'Static feasibility and exact dimension/identity checks only; no numerical improvement or new true coupled solution.',
    }
    with out.open('x') as f:json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({'status':report['status'],'report':identity(out),'source_entries':39,
                      'old_launch_entries':97,'unique_files':len(source),'new_solver_calls':0}))


if __name__=='__main__':main()
