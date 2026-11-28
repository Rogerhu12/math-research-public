#!/usr/bin/env sage-python
"""One public exact check of the full quadratic polynomial representation.

This is a software correctness/performance input, not an original-geometry
PASS.  It includes non-prime coefficients, nonreduced thick quotients,
arbitrary source rows, and exact return coordinates against the untouched
pinned implementation.
"""
import os
if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
    raise SystemExit("Run only in public research Actions.")

def _dispatch_fixed_request():
    """Choose one reviewed software check; never accept an arbitrary path."""
    import ast
    import hashlib
    import json
    import runpy
    from pathlib import Path
    here = Path(__file__).resolve().parent
    request_path = here.parent/"ci"/"original-complete-quadratic-api-request.json"
    request_bytes = request_path.read_bytes()
    request = json.loads(request_bytes.decode("utf-8"))
    default_kind = "complete-original-quadratic-polynomial-api-check"
    kind = request.get("kind", default_kind)
    if kind == default_kind:
        return  # Keep the complete original API check below unchanged.
    if kind == "original-native-captured-complete-return-software-check":
        check_name = "check-original-native-return-binding.py"
        binding_name = "original_native_complete_return_binding.py"
        check_sha = "e706e6ff3ee7033907c3f2a817592fc0ccbac35f3f8037b14a528890a0d5a146"
        binding_sha = "23f862035b668478bfafebdf95cf4d7f600d251243c3e47791fd4fec47c2c5bd"
    elif kind == "original-current-idempotent-square-software-check":
        check_name = "check-original-current-idempotent-square.py"
        binding_name = "original_current_idempotent_square.py"
        check_sha = "1ebafdeb5221cddd0d001e86b79874b0eb650d20b2c4881dcc87afffb6dd0e0e"
        binding_sha = "4c01f72b41e503be862045c7b9e1b63b3a457c7c63282ee3bf5df9d0d7d2a410"
    elif kind == "original-scalar-base-support-software-check":
        check_name = "check-original-scalar-base-divisor-support.py"
        binding_name = "original_scalar_base_divisor_support.py"
        check_sha = "3dd124a953a0a5dc160dd35a3a6ef6a04af11cf0231a947b32053cec40af297c"
        binding_sha = "c84656c73bb062958c233de20fbed4fb889779985d154058548305e02d73e39a"
    elif kind == "original-scalar-primary-return-software-check":
        check_name = "check-original-scalar-primary-return.py"
        binding_name = "original_scalar_primary_return.py"
        check_sha = "30cb33209c8d9e11838aaba41255081f3901dd51f95b12b012c2114e1001a591"
        binding_sha = "d8d4f90b667d2d66346636e69d764207c84de1ebb5d82c4cfa55d4ca7a87c7d3"
    elif kind == "original-function-field-denominator-return-software-check":
        check_name = "check-original-function-field-denominator-return.py"
        binding_name = "original_function_field_denominator_return.py"
        check_sha = "07b8e39757e998a91b64c2114253ec6072ebdb19ab53aeed58b3dea625c090eb"
        binding_sha = "0a1b6232348067cf9deb49498d97f9d32a0213dc3ef12d882d83ae35f00df5c4"
    elif kind == "original-row-operation-right-return-software-check":
        check_name = "check-original-row-operation-right-return.py"
        binding_name = "original_row_operation_right_return.py"
        check_sha = "aab13e7e58d1700157456e39ae616bd1405237ad45f6e592383f18dacf6e8d4e"
        binding_sha = "ce7675e8b57fee62a2b5c7907a5cd5887759e4d72bc1e4117f04c4032e4dc225"
    elif kind == "original-complete-cyclic-denominator-return-software-check":
        check_name = "check-original-cyclic-denominator-return.py"
        binding_name = "original_cyclic_denominator_return.py"
        check_sha = "6113c7b4eb46c00b40cad02028a8e97705e219cbef8175ac5d4e6ed1ef35f396"
        binding_sha = "4ebbe8018347d9bf6269d6e0d83960224bb399fa5ae1998b7d91e3c1ba96fbf1"
    elif kind == "original-streamed-same-denominator-return-software-check":
        check_name = "check-original-streamed-denominator-return.py"
        binding_name = "original_streamed_denominator_return.py"
        check_sha = "ef03e1cddcfb760d1e0175b9f38e481515b729d0119ba3a464c8b18ad995f927"
        binding_sha = "e315b6a330df38d370657d1db68a4b3a6ebe161509d92d9b239e6da8c89b542f"
    elif kind == "original-adaptive-scalar-graph-software-check":
        check_name = "check-original-adaptive-scalar-graph.py"
        binding_name = "original_adaptive_scalar_graph.py"
        check_sha = "61b44d0b58e15db3c2e692b43ce5cd5a32efea54b651e1a2035d3ec88a6b6b92"
        binding_sha = "b6e5c9a2ad61a9314bac08b0ce221f15076feabd70a7d5b51c86688519df7ede"
    else:
        raise RuntimeError("Unknown fixed complete-quadratic API request kind.")
    if (request.get("check_script") != "scripts/"+check_name or
            request.get("check_sha256") != check_sha or
            request.get("binding_script") != "scripts/"+binding_name or
            request.get("binding_sha256") != binding_sha):
        raise RuntimeError("The fixed software-check request or pins changed.")
    verified = {}
    for name, expected in ((check_name, check_sha), (binding_name, binding_sha)):
        source = (here/name).read_bytes()
        actual = hashlib.sha256(source).hexdigest()
        if actual != expected:
            raise RuntimeError("Fixed selected software source changed: "+name)
        ast.parse(source.decode("utf-8"), filename=str(here/name))
        verified[name] = actual
    if kind == "original-adaptive-scalar-graph-software-check":
        pins = request["source_sha256"]
        manifest = hashlib.sha256(json.dumps(
            pins, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        if (manifest != "8457723b6818e2329ad7912cefdc2604292cd605ca106f0c6f6d69faef6638d6" or request["source_manifest_sha256"] != manifest or
                request["source_files"] != sorted(pins)):
            raise RuntimeError("The fixed adaptive software source manifest changed.")
        for name, expected in pins.items():
            if Path(name).name != name:
                raise RuntimeError("Invalid adaptive software source basename.")
            source = (here/name).read_bytes()
            actual = hashlib.sha256(source).hexdigest()
            if actual != expected:
                raise RuntimeError("Adaptive software source changed: "+name)
            if name.endswith(".py"):
                ast.parse(source, filename=str(here/name))
            verified[name] = actual
        if any(verified[name] != sha for name, sha in
               ((check_name, check_sha), (binding_name, binding_sha))):
            raise RuntimeError("Adaptive selector and complete source manifest disagree.")
    print("RANK2_COMPLETE_QUADRATIC_API_SELECTOR "+json.dumps({
        "kind": kind,
        "request_id": request["request_id"],
        "request_sha256": hashlib.sha256(request_bytes).hexdigest(),
        "fixed_check_script": "scripts/"+check_name,
        "verified_source_sha256": verified,
        "selected_sources_syntax_parsed": True,
        "original_default_check_retained": True,
        "no_production_request_or_mathematical_input_changed": True,
    }, sort_keys=True, separators=(",", ":")), flush=True)
    if kind == "original-adaptive-scalar-graph-software-check":
        from contextlib import redirect_stdout
        from io import StringIO
        import time
        started = time.monotonic()
        output = StringIO()
        try:
            with redirect_stdout(output):
                runpy.run_path(str(here/check_name), run_name="__main__")
        finally:
            print(output.getvalue(), end="", flush=True)
        lines = output.getvalue().splitlines()
        def one_record(tag):
            matches = [line[len(tag)+1:] for line in lines if line.startswith(tag+" ")]
            if len(matches) != 1:
                raise RuntimeError("Expected exactly one original software record: "+tag)
            return matches[0]
        raw = one_record("RANK2_ADAPTIVE_SCALAR_GRAPH_SOFTWARE_RESULT")
        actual_hash = hashlib.sha256(raw.encode()).hexdigest()
        if one_record("RANK2_ADAPTIVE_SCALAR_GRAPH_SOFTWARE_SHA256") != actual_hash:
            raise RuntimeError("The complete original fixture payload hash changed.")
        result = json.loads(raw)
        if (result["kind"] != "small_adaptive_graph_software_only" or
                result["comparisons"] != 8 or len(result["refinements_by_case"]) != 8 or
                result["actual_post_ideal_polynomial_part_tamper_rejections"] != 2 or
                result["actual_final_X_budget_rejections_before_any_new_audit"] != 2 or
                result["nonlinear_good_place_and_true_transpose"] is not True or
                result["original_geometry_claimed"] is not False):
            raise RuntimeError("The complete adaptive software fixtures did not return.")
        envelope = dict(kind=kind, status="PASS", source=os.environ["RANK2_SOURCE_SHA"],
            run_id=os.environ["RANK2_RUN_ID"], run_attempt=os.environ["RANK2_RUN_ATTEMPT"],
            root_readme_blob=os.environ["RANK2_ROOT_README_SHA"],
            topic_readme_blob=os.environ["RANK2_TOPIC_README_SHA"],
            image=os.environ["RANK2_IMAGE"], request_sha256=hashlib.sha256(request_bytes).hexdigest(),
            selector_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            source_file_sha256=verified, source_manifest_sha256=manifest,
            fixture_result=result, fixture_result_sha256=actual_hash,
            elapsed_seconds=time.monotonic()-started, software_budget_seconds=420,
            original_geometry_executed=False, heavy_producer_executed=False)
        payload = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
        print("RANK2_ADAPTIVE_SCALAR_GRAPH_PUBLIC_RESULT "+payload, flush=True)
        print("RANK2_ADAPTIVE_SCALAR_GRAPH_PUBLIC_SHA256 "+
              hashlib.sha256(payload.encode()).hexdigest(), flush=True)
        raise SystemExit(0)
    runpy.run_path(str(here/check_name), run_name="__main__")
    raise SystemExit(0)


_dispatch_fixed_request()

import hashlib,json,time
from pathlib import Path
from copy import copy
from sage.all import GF,PolynomialRing,matrix,vector
import original_complete_quadratic_returns as fast
from original_ys_divisor_ideal_tools import polynomial_matrix_digest

def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"))
started=time.monotonic()
preparation=fast.prepare_backend()
checks=[]
for prime,n in ((29,12),(41,9)):
    k=GF(prime**2,"original_z")
    z=k.gen()
    R=PolynomialRing(k,"original_t")
    t=R.gen()
    # Non-prime diagonal coefficients force the full conjugate/norm division.
    H=matrix(R,n,n)
    for i in range(n):
        H[i,i]=(t-z-(i%3))**(2+i%3)
        for j in range(i+1,n):
            H[i,j]=R([(z+i+j+1)*(e+1) for e in range(2+j%3)])
    assert H.is_hermite()
    C=matrix(R,n+3,n,lambda i,j:
             (z+i+1)*t**((i+2*j)%4)+(z*j+i+2))
    rows=C*H
    before=time.monotonic()
    product=fast.complete_product(C,H)
    assert product==rows
    coordinates=fast.complete_hermite_coordinates(H,rows)
    assert coordinates==C
    returned=fast.complete_remainder_rows(rows,H)
    assert returned.is_zero()
    perturbed=matrix(R,n+3,n,lambda i,j:
        rows[i,j]+(z+i+j+1)*t**((i+j)%3))
    assert fast.complete_remainder_rows(perturbed,H)==fast.ORIGINAL_REMAINDER(perturbed,H)
    assert fast.complete_hermite_coordinates(H,rows)==fast.ORIGINAL_COORDINATES(H,rows)
    # A mutable caller basis must invalidate its complete representation.
    changed=copy(H)
    assert fast.complete_remainder_rows(perturbed,changed)==fast.ORIGINAL_REMAINDER(perturbed,changed)
    changed[0,1]+=z+1
    assert changed.is_hermite()
    assert fast.complete_remainder_rows(perturbed,changed)==fast.ORIGINAL_REMAINDER(perturbed,changed)
    # Reject an actual full-module non-inclusion, never clear denominators.
    bad=matrix(rows)
    bad[0,0]+=1
    rejected=False
    try:
        fast.complete_hermite_coordinates(H,bad)
    except ArithmeticError:
        rejected=True
    assert rejected
    empty=matrix(R,0,n)
    assert fast.complete_remainder_rows(empty,H)==empty
    assert fast.complete_hermite_coordinates(H,empty)==empty
    assert fast.complete_product(matrix(R,0,n),H)==empty
    checks.append({
        "prime":prime,"constant_degree":2,"rank":n,
        "full_thick_length":sum(int(H[i,i].degree()) for i in range(n)),
        "actual_nonprime_diagonal_used":any(c not in k.prime_subfield()
            for i in range(n) for c in H[i,i].list()),
        "full_product_sha256":polynomial_matrix_digest(product),
        "full_coordinates_sha256":polynomial_matrix_digest(coordinates),
        "same_complete_reference_remainder_and_coordinates":True,
        "actual_noninclusion_rejected":rejected,
        "empty_full_matrix_shapes_retained":True,
        "caller_basis_mutation_invalidates_complete_representation":True,
        "elapsed_seconds":time.monotonic()-before,
    })
# Rank 306 is the actual original module width.  Use an explicitly specified
# complete upper Hermite module with quadratic coefficients and nilpotents;
# do not call it an original geometric primary block.
k=GF(29**2,"original_z")
z=k.gen()
R=PolynomialRing(k,"original_t")
t=R.gen()
n=306
H=matrix(R,n,n)
for i in range(n):
    H[i,i]=(t-z)**2
    for j in range(i+1,min(n,i+8)):
        H[i,j]=(z+i+j)*t+(z*i+j+1)
C=matrix(R,2,n,lambda i,j:(z+i+j)*t**(j%3)+(j+1))
rows=C*H
before=time.monotonic()
assert fast.complete_product(C,H)==rows
assert fast.complete_hermite_coordinates(H,rows)==C
assert fast.complete_remainder_rows(rows,H).is_zero()
checks.append({"prime":29,"constant_degree":2,"rank":n,
    "full_thick_length":612,"source_rows":2,
    "same_full_product_and_original_return":True,
    "elapsed_seconds":time.monotonic()-before,
    "not_a_claim_about_original_geometric_primary_blocks":True})
# Repeated scalar-row reductions are the real idempotent-lift use case.
before=time.monotonic()
for repeat in range(8):
    assert fast.complete_remainder_rows(matrix(R,[rows.row(0)]),H).is_zero()
repeat_seconds=time.monotonic()-before
binding=fast.bind_original_returns()
assert binding["full_reverse_identity_H_equals_CI_plus_H_one_minus_e_retained"]
files=("original_complete_quadratic_polynomials.pyx",
       "original_complete_quadratic_returns.py",Path(__file__).name)
result={"kind":"complete-original-quadratic-polynomial-api-check",
    "status":"PASS","source":os.environ["RANK2_SOURCE_SHA"],
    "run_id":os.environ["RANK2_RUN_ID"],
    "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
    "root_readme_blob":os.environ["RANK2_ROOT_README_SHA"],
    "topic_readme_blob":os.environ["RANK2_TOPIC_README_SHA"],
    "source_file_sha256":{p:hashlib.sha256((Path(__file__).parent/p).read_bytes()).hexdigest() for p in files},
    "preparation":preparation,"checks":checks,"binding":binding,
    "same_complete_basis_repeat_count":8,"same_complete_basis_repeat_seconds":repeat_seconds,
    "transient_complete_representation_hits":fast.CACHE_HITS,
    "transient_complete_representation_refreshes":fast.CACHE_REFRESHES,
    "all_original_geometric_gates_still_required":True,
    "data_artifact_written":False,"elapsed_seconds":time.monotonic()-started}
payload=canonical(result)
print("RANK2_COMPLETE_QUADRATIC_API_RESULT "+payload,flush=True)
print("RANK2_COMPLETE_QUADRATIC_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)
