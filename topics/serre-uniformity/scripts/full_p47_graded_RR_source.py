#!/usr/bin/env python3
"""Original level-47 graded RR source from the certified logarithmic frame.

New scope: canonical product bases of L^2,...,L^5 at one actual cusp.
No new point sieve, CM logarithm or height is computed. Raw matrices remain
in this public Actions process; later consumers rebuild and check hashes.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
REQUEST=ROOT/(PRE+"notes/full-p47-graded-RR-source-request.json")
START=time.monotonic()
STAGE="preflight"
SOURCE=None
REQUEST_HASH=None
COMPLETED={}
DEADLINE=None
PRECISION=836
TARGETS={1:95,2:262,3:429,4:596,5:763}

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,elapsed_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)

def check_budget():
    if DEADLINE is not None and time.monotonic()>=DEADLINE:
        raise TimeoutError("Declared mathematical reserve reached.")

def stop(signum,frame):
    raise TimeoutError("Declared mathematical reserve reached.")

def ci_only():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("Only this public repository's Actions may execute mathematics.")

def import_source(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def row_hash(M):
    return digest([[int(a) for a in row] for row in M.rows()])

def build_graded_source(req,expected_certificate=None):
    """Return original product bases and recursive pairs, in runner memory.

    A consumer may regenerate these deterministic bounded input bases, compare
    the complete prior certificate, and perform a NEW RR operation. It must not
    present this input regeneration as a second independent certification.
    """
    ci_only()
    from sage.all import matrix,PolynomialRing
    original_path=req["original_Hodge_request_path"]
    original=json.loads((ROOT/original_path).read_text())
    module=import_source("original_hodge_for_RR",PRE+"scripts/full_p47_weight_one_Hodge_certificate.py")
    source=module.build_source(descriptors=original["Hodge_descriptors"],
        expected_certificate=original["Hodge_certificate"])
    K=source["K"]
    ring=PolynomialRing(K,"t")
    full=source["engine"].jets(source["descriptors"],length=PRECISION)
    if full.matrix_from_columns(range(168))!=source["logarithmic_jets"]:
        raise ArithmeticError("The longer original cusp source changed its certified prefix.")
    polynomials={1:[ring(list(row)) for row in full.rows()]}
    pairs={}
    all_cusp_values={1:source["residues"]/K(47)}
    cusp_kernels={1:source["kernel"]}
    matrices={1:full}
    certificate={"prime":47,"coefficient_prime":4513,"genus":73,
        "line_bundle":"Omega(C_infinity)","line_bundle_degree":167,
        "jet_length":PRECISION,"primitive_root":2,
        "original_Hodge_certificate_sha256":digest(source["certificate"]),
        "L1_long_jet_matrix_sha256":row_hash(full),
        "degrees":[]}
    for degree in range(2,6):
        check_budget()
        target=TARGETS[degree]
        previous=polynomials[degree-1]
        selected=[]
        selected_pairs=[]
        batch=[]
        batch_pairs=[]
        considered=0
        batches=0
        last_source=None

        def flush():
            nonlocal selected,selected_pairs,batch,batch_pairs,batches
            if not batch:
                return
            check_budget()
            candidates=selected+batch
            labels=selected_pairs+batch_pairs
            rows=[[int(f[k]) for k in range(PRECISION)] for f in candidates]
            M=matrix(K,rows)
            pivots=list(M.transpose().pivots())
            if len(pivots)>target:
                raise ArithmeticError("Products exceed the original RR dimension.")
            if list(pivots[:len(selected)])!=list(range(len(selected))):
                raise ArithmeticError("A previously independent prefix was lost.")
            selected=[candidates[i] for i in pivots]
            selected_pairs=[labels[i] for i in pivots]
            batch=[]
            batch_pairs=[]
            batches+=1
            emit("RR_rank_progress",degree=degree,rank=len(selected),
                 target=target,products_considered=considered,batches=batches)

        for j,right in enumerate(polynomials[1]):
            if len(selected)==target:
                break
            for i,left in enumerate(previous):
                if degree==2 and i<j:
                    continue
                batch.append(left._mul_trunc_(right,PRECISION))
                batch_pairs.append([i,j])
                considered+=1
                if len(batch)==95:
                    flush()
                    if len(selected)==target:
                        break
            flush()
            last_source=j
        if len(selected)!=target:
            raise ArithmeticError("The finite complete product family did not fill L^%d."%degree)
        M=matrix(K,[[int(f[k]) for k in range(PRECISION)] for f in selected])
        polynomials[degree]=selected
        pairs[degree]=selected_pairs
        matrices[degree]=M
        # Only the original 23 cusps are read; no new point enumeration.
        old_cusp_values=source["residues"]/K(47)
        if degree==2:
            previous_cusps=old_cusp_values
        else:
            previous_cusps=cusp_values
        cusp_values=matrix(K,23,target,
            lambda b,r:previous_cusps[b,selected_pairs[r][0]]*
                       old_cusp_values[b,selected_pairs[r][1]])
        expected_omega_dimension=target-23
        kernel=cusp_values.right_kernel().basis_matrix()
        if kernel.nrows()!=expected_omega_dimension or not (
                cusp_values*kernel.transpose()).is_zero():
            raise ArithmeticError("Full cusp vanishing did not give Omega*L^(n-1).")
        all_cusp_values[degree]=cusp_values
        cusp_kernels[degree]=kernel
        # All degrees here have deg(L^n(-C))>2g-2, so all23 conditions are independent.
        entry={"degree":degree,"dimension":target,
               "products_considered":considered,"last_source_index":last_source,
               "product_pairs_sha256":digest(selected_pairs),
               "basis_jets_sha256":row_hash(M),
               "all_23_cusp_values_sha256":row_hash(cusp_values),
               "cusp_vanishing_dimension":int(kernel.nrows()),
               "cusp_vanishing_kernel_sha256":row_hash(kernel)}
        certificate["degrees"].append(entry)
        COMPLETED["last_complete_degree"]=degree
        COMPLETED["graded_certificate"]=certificate
        emit("new_graded_degree",**entry)
    if expected_certificate is not None and certificate!=expected_certificate:
        raise ArithmeticError("Regenerated original graded-source certificate changed.")
    return {"source":source,"ring":ring,"matrices":matrices,
            "polynomials":polynomials,"product_pairs":pairs,
            "cusp_values":all_cusp_values,"cusp_vanishing_kernels":cusp_kernels,
            "certificate":certificate}

def main():
    global SOURCE,REQUEST_HASH,DEADLINE,STAGE
    ci_only()
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req=json.loads(raw)
    if (req["execution_id"]!="full-p47-graded-RR-source-v1" or
        req["prime"]!=47 or req["coefficient_prime"]!=4513 or
        req["sage_version"]!="10.6" or req["jet_length"]!=836 or
        req["degrees"]!=[1,2,3,4,5] or req["total_seconds"]!=900 or
        req["reserve_seconds"]!=30):
        raise RuntimeError("Unexpected finite graded-source request.")
    for path,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Source pin mismatch: "+path)
    module=import_source("original_head",PRE+"scripts/full_p47_weight_one_Hodge_certificate.py")
    SOURCE=module.source_head()
    DEADLINE=START+870
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    from sage.env import SAGE_VERSION
    from sage.all import proof
    if SAGE_VERSION!="10.6":
        raise RuntimeError("Wrong pinned Sage version.")
    proof.all(True)
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,consumed_Hodge_run=45946046378,
         jet_length=836,scope=req["scope"])
    STAGE="new_original_graded_RR_source"
    result=build_graded_source(req)
    certificate=result["certificate"]
    COMPLETED["graded_certificate"]=certificate
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="completed"
    emit("receipt",status="complete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=COMPLETED,
         result_sha256=digest(COMPLETED),
         scope="Original finite graded RR source only; no meromorphic Cartier or QC rank claimed.")

if __name__=="__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
             request_sha256=REQUEST_HASH,stage=STAGE,completed=COMPLETED,
             exception_type=type(exc).__name__,message=str(exc))
        traceback.print_exc()
        sys.exit(1)
