#!/usr/bin/env python3
"""New integral CM height moving operators, consuming the original Hodge hashes."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[3]
PRE = "topics/serre-uniformity/"
REQUEST = ROOT/(PRE+"notes/full-p47-CM-height-move-request.json")
START = time.monotonic()
SOURCE = None
REQUEST_HASH = None
STAGE = "preflight"
COMPLETED = {}

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,elapsed_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)

def stop(signum,frame):
    raise TimeoutError("The declared mathematical reserve has been reached.")

def main():
    global SOURCE, REQUEST_HASH, STAGE
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get(
            "GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Only this public repository's Actions may execute mathematics.")
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req=json.loads(raw)
    if (req["execution_id"] != "full-p47-CM-height-move-v1" or
        req["prime"] != 47 or req["coefficient_prime"] != 4513 or
        req["total_seconds"] != 120 or req["reserve_seconds"] != 10 or
        req["odd_primitive_t_values"] != list(range(64)) or
        req["sage_version"] != "10.6"):
        raise RuntimeError("Unexpected finite request.")
    for name,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != wanted:
            raise RuntimeError("Source pin mismatch: "+name)
    spec=importlib.util.spec_from_file_location("original_hodge",
        ROOT/(PRE+"scripts/full_p47_weight_one_Hodge_certificate.py"))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    SOURCE=module.source_head()
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,110-(time.monotonic()-START)))
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,source_sha256=req["source_sha256"],
         consumed_Hodge_run=req["Hodge_source_run"],consumed_CM_run=req["CM_source_run"])
    from sage.all import identity_matrix
    STAGE="consume_original_Hodge_inputs"
    source=module.build_source(descriptors=req["Hodge_descriptors"],
        expected_certificate=req["Hodge_certificate"])
    bridge=module.hecke_bridge(source)
    for n in (2,3,5):
        actual=digest(module.integral_rows(bridge["operators"][n]))
        if actual != req["original_Hecke_hashes"][str(n)]:
            raise ArithmeticError("Original Hecke matrix hash mismatch.")
    if bridge["H2_sha256"] != req["original_Hecke_hashes"]["H2"]:
        raise ArithmeticError("Original H2 matrix hash mismatch.")
    emit("original_inputs_consumed",original_Hecke_hashes=req["original_Hecke_hashes"])
    K=source["K"]
    M2,M3,M5=[bridge["operators"][n] for n in (2,3,5)]
    H2=bridge["H2"]
    I=identity_matrix(K,73)
    STAGE="new_CM_moving_units"
    A=M2-I
    detA,det3=A.det(),M3.det()
    move={"T2_minus_one_determinant":int(detA),"T2_minus_one_is_unit":bool(detA),
          "T3_determinant":int(det3),"T3_is_unit":bool(det3)}
    if detA:
        inv=A.inverse()
        if A*inv != I or inv*A != I:
            raise ArithmeticError("Integral moving inverse failed.")
        move["T2_minus_one_inverse_sha256"]=digest(module.integral_rows(inv))
    if det3:
        inv=M3.inverse()
        if M3*inv != I:
            raise ArithmeticError("T3 moving inverse failed.")
        move["T3_inverse_sha256"]=digest(module.integral_rows(inv))
    COMPLETED["moving_operators"]=move
    emit("new_moving_operator_certificate",**move)
    STAGE="new_CM16_linear_values"
    rows=[]
    for old in req["original_CM_linear_rows"]:
        root=K(old["H2_eigenvalue"])
        kernel=(H2.transpose()-root*I).right_kernel()
        if kernel.dimension() != 1:
            raise ArithmeticError("Original simple linear block lost dimension.")
        v=kernel.basis()[0]
        leading=next(c for c in v if c)
        v=v/leading
        if digest([int(c) for c in v]) != old["eigenform_coordinates_sha256"]:
            raise ArithmeticError("Original normalized eigenform hash mismatch.")
        pivot=next(j for j,c in enumerate(v) if c)
        a2=(v*M2)[pivot]
        a3=(v*M3)[pivot]
        if v*M2 != a2*v or v*M3 != a3*v:
            raise ArithmeticError("Original Hecke scalar coordinate failed.")
        cm16=(a2-1)*K(old["q_inverse_log_Bq_u1728"])/2
        rows.append({"H2_eigenvalue":int(root),"T2_eigenvalue":int(a2),
                     "T3_eigenvalue":int(a3),"q_inverse_log_Bq_u16":int(cm16)})
    COMPLETED["CM16_linear_values"]=rows
    emit("new_CM16_linear_values",rows=rows,rows_sha256=digest(rows))
    STAGE="new_odd_Hecke_primitive"
    odd=None
    for t in req["odd_primitive_t_values"]:
        H=M3+t*M5
        chi=H.charpoly("X")
        gcd_degree=int(chi.gcd(chi.derivative()).degree())
        emit("odd_primitive_progress",t=t,characteristic_degree=int(chi.degree()),
             repeated_factor_degree=gcd_degree)
        if gcd_degree == 0:
            degrees=sorted(int(f.degree()) for f,e in chi.factor())
            odd={"t":t,"definition":"T3+t*T5","dimension":73,
                 "characteristic_polynomial_sha256":digest([int(c) for c in chi.list()]),
                 "matrix_sha256":digest(module.integral_rows(H)),
                 "discriminant_mod4513":int(chi.discriminant()),
                 "factor_degrees":degrees,"squarefree":True}
            break
    COMPLETED["odd_primitive"]=odd
    if odd is not None:
        emit("new_odd_Hecke_primitive_certificate",**odd)
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="completed"
    emit("receipt",status="complete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=COMPLETED,result_sha256=digest(COMPLETED),
         scope="New CM moving-operator units, derived actual CM16 log values and a finite odd-Hecke primitive search. No new CM series, height value or rational-point exclusion.")

if __name__ == "__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
             request_sha256=REQUEST_HASH,stage=STAGE,completed=COMPLETED,
             exception_type=type(exc).__name__,message=str(exc))
        traceback.print_exc()
        sys.exit(1)
