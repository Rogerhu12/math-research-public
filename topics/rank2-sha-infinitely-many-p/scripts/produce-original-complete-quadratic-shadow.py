#!/usr/bin/env sage-python
"""Same complete original v11 pipeline with faithful quadratic polynomial returns."""
import os
if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
    raise SystemExit("Run only in public research Actions.")
import hashlib,importlib.util,sys,time
from pathlib import Path
import original_complete_quadratic_returns as quadratic
from section_quotient_algebra import canonical,digest

HERE=Path(__file__).resolve().parent
IMPLEMENTATION="complete-quadratic-returns-native-rows-original-linear-fibers-v12"
PINNED_NATIVE_SOURCE_SHA256="63ff0e1dbec3797b1276e7892e2177aac3c0bdd674ba5f5415d434fb0f5590d8"
PINNED_QUADRATIC={
    "original_complete_quadratic_polynomials.pyx":"7742254770d03bbdab649902e4a9faf92dc7e82c0fb360d279b496b7eb7ed917",
    "original_complete_quadratic_returns.py":"7da06cd12f35f7f2b98bf0c2c247c2732c838924c5497d3b8755b34932ce6d09",
}
STARTED=time.monotonic()

def emit(tag,value):
    payload=canonical(value)
    print(tag+"_RESULT "+payload,flush=True)
    print(tag+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)

def main():
    assert os.environ["RANK2_LINEAR_ALGEBRA"]==IMPLEMENTATION
    for name,expected in PINNED_QUADRATIC.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected
    preparation=quadratic.prepare_backend()
    path=HERE/"produce-original-native-row-artinian-shadow.py"
    assert hashlib.sha256(path.read_bytes()).hexdigest()==PINNED_NATIVE_SOURCE_SHA256
    spec=importlib.util.spec_from_file_location("original_quadratic_v12_pinned_native_producer",str(path))
    entry=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=entry
    spec.loader.exec_module(entry)
    assert entry.IMPLEMENTATION=="r1035-complete-native-rows-projector-original-linear-fibers"
    entry.IMPLEMENTATION=IMPLEMENTATION
    inner,state,native_preparation=entry.prepare_source_bindings()
    # The unchanged projector dependency hook adds every one of these to
    # the SAME original geometric source manifest before any acceptance work.
    dependencies=tuple(dict.fromkeys((Path(__file__).name,)+quadratic.SOURCE_DEPENDENCIES))
    inner.PROJECTOR_DEPENDENCIES=tuple(dict.fromkeys(inner.PROJECTOR_DEPENDENCIES+dependencies))
    binding=quadratic.bind_original_returns()
    emit("RANK2_COMPLETE_QUADRATIC_BINDINGS",{
        "source":os.environ["RANK2_SOURCE_SHA"],"run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "linear_algebra":IMPLEMENTATION,
        "pinned_native_producer_sha256":PINNED_NATIVE_SOURCE_SHA256,
        "pinned_complete_quadratic_source_sha256":PINNED_QUADRATIC,
        "preparation":preparation,"binding":binding,
        "all_original_geometric_acceptance_gates_retained":True,
        "no_original_matrix_or_coefficient_cache_loaded":True,
        "mathematical_acceptance_claimed":False})
    entry.main()
    linear=state["linear_entry"]
    assert linear is not None
    original=linear.ENTRY
    assert all(name in original.SOURCE_DEPENDENCIES for name in dependencies)
    context=linear.ORIGINAL_LINEAR_FIBER_COMPLETE_CONTEXT
    assert context["certificate"]["status"]=="all_requested_original_acceptance_gates_completed"
    emit("RANK2_COMPLETE_QUADRATIC_COMPLETE",{
        "status":"all_original_gates_completed_with_complete_quadratic_returns",
        "source":os.environ["RANK2_SOURCE_SHA"],"run_id":os.environ["RANK2_RUN_ID"],
        "linear_algebra":IMPLEMENTATION,
        "complete_original_pipeline_receipt_sha256":digest(context["certificate"]),
        "all_original_geometric_acceptance_gates_retained":True,
        "same_original_constants_basis_and_every_nilpotent_retained":True,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
        "recomputable_data_file_written":False,
        "elapsed_seconds":time.monotonic()-STARTED})

if __name__=="__main__":
    try:
        main()
    except Exception as exc:
        print("RANK2_COMPLETE_QUADRATIC_FAILED "+canonical({
            "exception_type":type(exc).__name__,"message":str(exc),
            "elapsed_seconds":time.monotonic()-STARTED}),flush=True)
        raise
