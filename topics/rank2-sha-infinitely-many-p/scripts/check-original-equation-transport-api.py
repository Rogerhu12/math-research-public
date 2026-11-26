#!/usr/bin/env sage-python
"""Public exact identities and source-preservation gate for seven-map transport."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import ast
import hashlib
import json
import time
from collections import Counter
from pathlib import Path
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical, digest
import original_ys_fraction_bridge as original_bridge
import original_ys_equation_transport as transport

HERE = Path(__file__).resolve().parent
ROOT, TOPIC = HERE.parents[2], HERE.parent
REQUEST = TOPIC/"ci/original-equation-transport-api-request.json"
WORKFLOW = ROOT/".github/workflows/rank2-sha-equation-transport-api.yml"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
SOURCE_FILES = tuple(dict.fromkeys((
    "check-original-equation-transport-api.py",
    "section_quotient_algebra.py",
)+transport.SOURCE_DEPENDENCIES))
STARTED = time.monotonic()


def source_preservation_gate():
    base_source = Path(original_bridge.__file__).read_text(encoding="utf-8")
    new_source = Path(transport.__file__).read_text(encoding="utf-8")
    assert hashlib.sha256(base_source.encode()).hexdigest() == transport.BASE_BRIDGE_SHA256
    old = next(n for n in ast.parse(base_source).body if isinstance(n, ast.FunctionDef)
               and n.name == "build_original_ys_fraction_maps")
    new = next(n for n in ast.parse(new_source).body if isinstance(n, ast.FunctionDef)
               and n.name == "build_original_ys_fraction_maps_with_equation_transport")
    dump = lambda x: ast.dump(x, include_attributes=False)
    assert dump(old.args) == dump(new.args)
    def actual_position(body):
        return next(i for i, stmt in enumerate(body)
                    if isinstance(stmt, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == "actual"
                            for t in stmt.targets))
    old_end, new_end = actual_position(old.body), actual_position(new.body)
    # Only a changed docstring and two new provenance/formal-identity lines
    # precede the identical complete original source and root construction.
    assert [dump(n) for n in old.body[1:old_end]] == [
        dump(n) for n in new.body[3:new_end]]
    old_formulas = next(n for n in old.body if isinstance(n, ast.FunctionDef)
                        and n.name == "formulas")
    new_formulas = next(n for n in new.body if isinstance(n, ast.FunctionDef)
                        and n.name == "formulas")
    assert dump(old_formulas) == dump(new_formulas)
    old_assertions = Counter(dump(n) for n in ast.walk(old) if isinstance(n, ast.Assert))
    new_assertions = Counter(dump(n) for n in ast.walk(new) if isinstance(n, ast.Assert))
    missing = old_assertions-new_assertions
    expected_missing = ast.parse('assert row["y2"]**2 == v*row["x2"]**3+1').body[0]
    assert missing == Counter({dump(expected_missing):1})
    def whole_W_loop(function):
        return next(n for n in function.body if isinstance(n, ast.For)
                    and isinstance(n.target, ast.Tuple)
                    and [x.id for x in n.target.elts] == ["original_row", "Wrow"])
    assert dump(whole_W_loop(old)) == dump(whole_W_loop(new))
    def reflection_loop(function):
        return next(n for n in function.body if isinstance(n, ast.For)
                    and any(isinstance(q, ast.Assign) and
                            any(isinstance(t, ast.Tuple) and
                                [x.id for x in t.elts] == ["star", "phase"]
                                for t in q.targets)
                            for q in n.body))
    assert dump(reflection_loop(old)) == dump(reflection_loop(new))
    # The entire returned source context is unchanged, not only its dimension.
    old_update = next(n for n in old.body if isinstance(n, ast.Expr)
                      and isinstance(n.value, ast.Call)
                      and isinstance(n.value.func, ast.Attribute)
                      and isinstance(n.value.func.value, ast.Name)
                      and n.value.func.value.id == "actual" and n.value.func.attr == "update")
    new_update = next(n for n in new.body if isinstance(n, ast.Expr)
                      and isinstance(n.value, ast.Call)
                      and isinstance(n.value.func, ast.Attribute)
                      and isinstance(n.value.func.value, ast.Name)
                      and n.value.func.value.id == "actual" and n.value.func.attr == "update")
    assert dump(old_update) == dump(new_update)
    return dict(
        complete_original_root_source_prefix_identical=True,
        all_original_fraction_formulas_identical=True,
        complete_forward_reverse_W_loop_identical=True,
        complete_all_indices_and_endpoints_reflection_loop_identical=True,
        all_original_assertion_syntax_except_y2_direct_statement_retained=True,
        complete_returned_original_context_identical=True,
        original_bridge_sha256=transport.BASE_BRIDGE_SHA256,
        static_source_gate_only=True)


def main():
    raw = REQUEST.read_bytes()
    request = json.loads(raw)
    assert request == {
        "schema":"rank2-original-equation-transport-api/v1",
        "checks":["universal-ZZ-identities", "W-rational-scalar-identities",
                  "complete-original-source-preservation"],
        "original_geometry":False,
    }
    assert len(raw) <= 4096 and SAGE_VERSION == "10.6"
    assert os.environ["RANK2_IMAGE"] == IMAGE
    source = os.environ["RANK2_SOURCE_SHA"]
    assert len(source) == 40 and all(c in "0123456789abcdef" for c in source)
    assert os.environ["RANK2_RUN_ID"].isdecimal()
    assert os.environ["RANK2_RUN_ATTEMPT"].isdecimal()
    for name in SOURCE_FILES:
        ast.parse((HERE/name).read_text(encoding="utf-8"), filename=name)
    files = [HERE/name for name in SOURCE_FILES]+[
        REQUEST, WORKFLOW, ROOT/"README.md", TOPIC/"README.md"]
    manifest = dict(
        source=source, run_id=os.environ["RANK2_RUN_ID"],
        run_attempt=os.environ["RANK2_RUN_ATTEMPT"], image=IMAGE,
        sage_version=SAGE_VERSION, request=request,
        request_sha256=hashlib.sha256(raw).hexdigest(),
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in files},
        readme_blobs={"root":os.environ["RANK2_ROOT_README_SHA"],
                      "topic":os.environ["RANK2_TOPIC_README_SHA"]},
        source_mount_read_only=True, Sage_network_mode="none",
        original_geometric_input_generated=False)
    print("RANK2_EQUATION_TRANSPORT_API_MANIFEST "+canonical(manifest), flush=True)
    source_gate = source_preservation_gate()
    formal = transport.equation_transport_formal_preflight()
    result = dict(
        kind="rank2_original_seven_map_equation_transport_API",
        status="exact_universal_identities_and_complete_source_preservation_passed",
        source=source, run_id=os.environ["RANK2_RUN_ID"],
        run_attempt=os.environ["RANK2_RUN_ATTEMPT"], image=IMAGE,
        sage_version=SAGE_VERSION, manifest_sha256=digest(manifest),
        complete_source_gate=source_gate, universal_identities=formal,
        all_source_ASTs_checked=True, source_file_count=len(SOURCE_FILES),
        original_maps_normalization_divisors_or_shadow_computed=False,
        coefficient_or_data_file_written=False,
        elapsed_seconds=time.monotonic()-STARTED)
    payload = canonical(result)
    print("RANK2_EQUATION_TRANSPORT_API_RESULT "+payload, flush=True)
    print("RANK2_EQUATION_TRANSPORT_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),
          flush=True)


if __name__ == "__main__":
    main()
