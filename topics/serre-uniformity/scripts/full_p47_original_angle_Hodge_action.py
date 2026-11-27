#!/usr/bin/env python3
"""Actual full-47 angle operators from one cyclic original CM evaluation.

Public Actions only.  Sage Hodge algebra and wheel-FLINT geometric arithmetic
run in separate exec processes.  All 1081 targets use one original torsion
grid, and the complete 23 angle sums are read before any prime-field descent.
"""
import hashlib
import importlib.util
from importlib.metadata import version
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
REPO="Rogerhu12/math-research-public"
THIS=PRE+"scripts/full_p47_original_angle_Hodge_action.py"
REQUEST=ROOT/(PRE+"notes/full-p47-original-angle-Hodge-request.json")
HODGE=PRE+"scripts/full_p47_weight_one_Hodge_certificate.py"
TANGENT=PRE+"scripts/full_p47_eight_CM_tangents.py"
CM_REQUEST=PRE+"notes/full-p47-CM-height-move-request.json"
TRANSFER_REQUEST=PRE+"notes/original-p47-ell4513-cuspidal-transfer-request.json"
TRANSFER=PRE+"scripts/original_p47_ell4513_cuspidal_transfer.py"
P,Q=47,4513
ANGLES=[0]+list(range(2,24))
START=time.monotonic()
DEADLINE=None
SOURCE=None
REQUEST_HASH=None
STAGE="preflight"
COMPLETED={}

def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":")).encode()

def digest(x):
    return hashlib.sha256(canonical(x)).hexdigest()

def emit(kind,**data):
    if "elapsed_seconds" in data:
        raise RuntimeError("Reserved parent timing field.")
    print(json.dumps(dict(kind=kind,elapsed_seconds=time.monotonic()-START,
                          **data),sort_keys=True),flush=True)

def check():
    if DEADLINE is not None and time.monotonic()>=DEADLINE:
        raise TimeoutError("The declared angle arithmetic reserve was reached.")

def stop(signum,frame):
    raise TimeoutError("The declared public angle budget was reached.")

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    result=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

def read_request():
    global REQUEST_HASH
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Only the specified public Actions may execute mathematics.")
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("New angle request pin mismatch.")
    req=json.loads(raw)
    if (req["execution_id"]!="full-p47-original-angle-Hodge-v1" or
        req["prime"]!=P or req["coefficient_prime"]!=Q or
        req["base_CM_candidate_id"]!=76 or req["total_seconds"]!=1200 or
        req["reserve_seconds"]!=30 or req["sage_version"]!="10.6" or
        req["python_flint_version"]!="0.9.0"):
        raise RuntimeError("Unexpected finite original-angle request.")
    for path,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Source hash mismatch: "+path)
    return req

def can_angle(c):
    c%=P
    return min(c,(-c)%P)

def field_targets():
    """Actual trace-zero I'^2=-1 matrices modulo sign, with determinant-one frames."""
    points=set()
    for a in range(P):
        for b in range(1,P):
            c=(-1-a*a)*pow(b,-1,P)%P
            m=(a,b,c)
            points.add(min(m,tuple((-x)%P for x in m)))
    if len(points)!=1081:
        raise ArithmeticError("The actual complete necklace fiber is not 1081.")
    groups={c:[] for c in [1]+ANGLES}
    inv2=pow(2,-1,P)
    for a,b,c in sorted(points):
        # The source matrix is I=(0,-1;1,0), so angle=-tr(I I')/2.
        angle=can_angle((c-b)*inv2)
        chosen=None
        for u in range(P):
            for v in range(P):
                if (c*u*u-2*a*u*v-b*v*v)%P==1:
                    chosen=(u,(a*u+b*v)%P,v,(c*u-a*v)%P)
                    break
            if chosen is not None:
                break
        if chosen is None:
            raise ArithmeticError("The actual anisotropic norm did not represent 1.")
        g00,g01,g10,g11=chosen
        if (g00*g11-g01*g10)%P!=1:
            raise ArithmeticError("A target frame changed the original Weil root.")
        # Check I'g=gI, including its second column.
        if ((a*g00+b*g10)%P,(a*g01+b*g11)%P,
            (c*g00-a*g10)%P,(c*g01-a*g11)%P)!=(
                g01,(-g00)%P,g11,(-g10)%P):
            raise ArithmeticError("The determinant-one frame has the wrong Cartan.")
        groups[angle].append(((a,b,c),chosen))
    if {c:len(v) for c,v in groups.items()}!={1:1,0:24,**{c:48 for c in ANGLES if c}}:
        raise ArithmeticError("An actual angle fiber lost multiplicity.")
    return groups

class OriginalReynoldsValues:
    """The original two-phase source, with extension values retained until trace."""

    def __init__(self,field,descriptors,grid):
        self.field=field
        self.descriptors=descriptors
        self.old={label:row[0] for label,row in grid.items()}
        self.labels=sorted(self.old)
        self.halves={h:[] for h in range(1,P)}
        for a,b in self.labels:
            if (a,b)<((-a)%P,(-b)%P):
                self.halves[(a*a+b*b)%P].append((a,b))
        if any(len(rows)!=24 for rows in self.halves.values()):
            raise ArithmeticError("The original norm half-fibers changed.")
        self.descriptor_groups={}
        for i,(phase,c,d) in enumerate(descriptors):
            self.descriptor_groups.setdefault((c,d),[]).append((i,phase))
        self.pairs={}
        for c,d in self.descriptor_groups:
            self.pairs[c,d]={h:[
                ((a,b),((d*a-c*b)%P,(c*a+d*b)%P),
                       ((d*a+c*b)%P,(-c*a+d*b)%P))
                for a,b in labels] for h,labels in self.halves.items()}
        self.zeta=[field(pow(2,h,Q)) for h in range(P)]

    def values(self,g):
        check()
        a,b,c,d=g
        transformed={label:self.old[((a*label[0]+b*label[1])%P,
                                     (c*label[0]+d*label[1])%P)]
                     for label in self.labels}
        result=[self.field.zero() for _ in self.descriptors]
        for rho,descs in self.descriptor_groups.items():
            first,second={},{}
            for h,pairs in self.pairs[rho].items():
                f=self.field.zero()
                s=self.field.zero()
                for left,right,conjugate in pairs:
                    e=transformed[left]
                    f+=2*e*transformed[right]
                    s+=2*e*transformed[conjugate]
                first[h],second[h]=f,s
            for i,phase in descs:
                result[i]=sum((self.zeta[phase*h%P]*first[h]+
                               self.zeta[-phase*h%P]*second[h]
                               for h in range(1,P)),self.field.zero())
        return result

def field_worker():
    global DEADLINE,SOURCE,STAGE
    req=read_request()
    packet=json.loads(sys.stdin.readline())
    if (packet["protocol"]!="original_angle_fields_v1" or
        packet["request_sha256"]!=REQUEST_HASH or
        packet["parent_pid"]!=os.getppid()):
        raise RuntimeError("The geometric worker has no pinned parent.")
    DEADLINE=packet["deadline"]
    started=packet["parent_started"]
    if abs(DEADLINE-started-1170)>0.000001 or not started<=time.monotonic()<DEADLINE:
        raise RuntimeError("The worker cannot obtain a separate budget.")
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    tangent=module("angle_original_tangent_source",TANGENT)
    SOURCE=tangent.checkout_source_head()
    if SOURCE!=packet["source"]:
        raise RuntimeError("Geometric source commit differs from parent.")
    tangent.DEADLINE=DEADLINE
    if tangent.field_runtime_libraries() or any(
            n=="sage" or n.startswith("sage.") for n in sys.modules):
        raise RuntimeError("A native mathematical runtime preceded the isolated field import.")
    from flint import fq_default_ctx,nmod_poly
    if version("python-flint")!="0.9.0":
        raise RuntimeError("Wrong field runtime version.")
    libraries=tangent.field_runtime_libraries()
    if len(libraries)!=1 or any("/sage/local/lib/libflint" in n for n in libraries):
        raise RuntimeError("The wheel FLINT was not isolated.")
    emit("field_ready",source=SOURCE,request_sha256=REQUEST_HASH,
         flint_libraries=libraries,imports_sage=False)
    cmreq=json.loads((ROOT/CM_REQUEST).read_text())
    trreq=json.loads((ROOT/TRANSFER_REQUEST).read_text())
    descriptors=packet["descriptors"]
    if descriptors!=cmreq["Hodge_descriptors"] or digest(descriptors)!=packet["descriptors_sha256"]:
        raise RuntimeError("The original95 descriptor packet changed.")
    transfer=module("angle_original_transfer",TRANSFER)
    transfer.STARTED,transfer.DEADLINE=started,DEADLINE
    old,roles,characters,models,candidates=transfer.candidate_input(ROOT,trreq,nmod_poly)
    cms=transfer.consume_known_cm(candidates,trreq["certified_cm_rows"])
    cm=next(r for r in cms if r["candidate_id"]==76)
    zeta0=next(z for z in range(2,Q) if pow(z,P,Q)==1)
    log0={pow(zeta0,i,Q):i for i in range(P)}
    beta=transfer.circle_values(zeta0,list(range(2,P-2,2)),log0)
    target=[c*beta[r]%P for c,r in zip(candidates[76]["vector"],roles)]
    curve,pp,qq,marking=tangent.select_actual_model(
        transfer,fq_default_ctx,cm,target,roles,zeta0,beta)
    model=marking["model"]
    if model!={"j":1138,"A":786,"B":524,"trace":0} or marking["field_degree"]!=4:
        raise ArithmeticError("The certified original CM76 input changed.")
    grid,grid_certificate=tangent.torsion_grid(curve,pp,qq,0,model["j"])
    evals=OriginalReynoldsValues(curve.field,descriptors,grid)
    identity=evals.values((1,0,0,1))
    initial95=[tangent.base_integer(x) for x in identity]
    initial_coarse,formula=tangent.coarse_tangent_vector(
        [[x] for x in initial95],model["A"],model["B"],model["j"])
    if digest(initial_coarse)!=req["consumed_CM76_coarse_tangent95_sha256"]:
        raise ArithmeticError("The already certified CM76 differential input changed.")
    D=(4*model["A"]**3+27*model["B"]**2)%Q
    scale=D*pow(124416*model["A"]**2*model["B"]%Q,-1,Q)%Q
    probe={"candidate_id":76,"marking":marking,"G1_grid":grid_certificate,
           "coarse_parameter":"j-j_CM","coarse_tangent95":initial_coarse,
           "coarse_tangent95_sha256":digest(initial_coarse),"coarse_KS_formula":formula}
    emit("cyclic_probe",record=probe)
    answer=json.loads(sys.stdin.readline())
    if answer!={"proceed":True,"coarse_tangent95_sha256":digest(initial_coarse)}:
        raise RuntimeError("The parent did not certify a cyclic actual evaluation.")
    groups=field_targets()
    all_rows=[]
    for angle in [1]+ANGLES:
        STAGE="actual_angle_%d"%angle
        total=[curve.field.zero() for _ in descriptors]
        targets_hash=hashlib.sha256()
        for necklace,g in groups[angle]:
            values=evals.values(g)
            for i,x in enumerate(values):
                total[i]+=x
            targets_hash.update(canonical([list(necklace),list(g)])+b"\n")
        # A complete rational correspondence fixes F_q; individual targets need not.
        coarse=[scale*tangent.base_integer(x)%Q for x in total]
        if angle==1 and coarse!=initial_coarse:
            raise ArithmeticError("Normalizer orientation changed the original source.")
        record={"angle":angle,"degree":len(groups[angle]),
                "actual_targets_sha256":targets_hash.hexdigest(),
                "coarse_sum95":coarse,"coarse_sum95_sha256":digest(coarse)}
        all_rows.append(record)
        emit("field_angle",record=record)
    signal.setitimer(signal.ITIMER_REAL,0)
    emit("field_receipt",status="complete",source=SOURCE,request_sha256=REQUEST_HASH,
         angle_count=23,necklace_count=1081,field_rows_sha256=digest(all_rows))

def compose_coeff(A,B,D):
    def chi(x):
        x%=P
        if not x:
            return 0
        return 1 if pow(x,23,P)==1 else -1
    if A and B:
        return 2+chi(1+2*A*B*D-A*A-B*B-D*D)+chi(
            1-2*A*B*D-A*A-B*B-D*D)
    if A or B:
        return 1+chi(1-A*A-B*B-D*D)
    return (1+chi(1-D*D))//2

def expected_trace(C):
    def chi(x):
        x%=P
        if not x:
            return 0
        return 1 if pow(x,23,P)==1 else -1
    if C==0:
        return -4
    inv2,inv3=pow(2,-1,P),pow(3,-1,P)
    e4=24*(2+chi((1+C)*inv2)+chi((1-C)*inv2))
    e3=24*(2+chi((1+2*C)*inv3)+chi((1-2*C)*inv3))
    n=2+chi(2*(C-1))+chi(-2*(C+1))
    numerator=12*48-3*e4-4*e3-138*n
    result,remainder=divmod(numerator,12)
    if remainder:
        raise ArithmeticError("Nonintegral original fixed-cycle trace.")
    return result

def recover_angles(source,H,probe,field_rows,req):
    """Importable deterministic consumer; caller supplies certified original inputs."""
    from sage.all import matrix,vector,PolynomialRing,identity_matrix
    k=source["K"]
    PR=PolynomialRing(k,"X")
    poly=PR(H.charpoly("X"))
    if digest([int(c) for c in poly.list()])!=req["Hodd_characteristic_polynomial_sha256"]:
        raise ArithmeticError("The original Hodd polynomial changed.")
    e=source["kernel"]*vector(k,probe["coarse_tangent95"])
    columns=[]
    v=e
    for _ in range(73):
        columns.append(v)
        v=H*v
    Cyclic=matrix(k,columns).transpose()
    if not Cyclic.det():
        raise ArithmeticError("The specified actual CM76 evaluation is not cyclic.")
    inverse=Cyclic.inverse()
    if Cyclic*inverse!=identity_matrix(k,73):
        raise ArithmeticError("Cyclic evaluation inverse failed.")
    if [r["angle"] for r in field_rows]!=[1]+ANGLES:
        raise ArithmeticError("The complete actual angle list is missing.")
    operators={}
    certificate_rows=[]
    for row in field_rows:
        u=source["kernel"]*vector(k,row["coarse_sum95"])
        coeff=inverse*u
        if Cyclic*coeff!=u:
            raise ArithmeticError("Actual angle evaluation interpolation failed.")
        operators[row["angle"]]=PR(list(coeff))
        certificate_rows.append({
            "angle":row["angle"],"degree":row["degree"],
            "actual_targets_sha256":row["actual_targets_sha256"],
            "coarse_sum95_sha256":row["coarse_sum95_sha256"],
            "polynomial_sha256":digest([int(x) for x in coeff])})
    if operators[1]!=PR.one() or sum((operators[c] for c in [1]+ANGLES),PR.zero())%poly:
        raise ArithmeticError("The full original j-pull-push identity failed.")
    rows=[[operators[c][j] for j in range(73)] for c in ANGLES]
    if matrix(k,rows).rank()!=23:
        raise ArithmeticError("The actual angle image lost its certified full dimension.")
    # Read all traces by the same actual Hodge matrix powers.
    traces=[]
    power=identity_matrix(k,73)
    for _ in range(73):
        traces.append(power.trace())
        power=power*H
    def trace(f):
        f%=poly
        return sum((f[j]*traces[j] for j in range(73)),k.zero())
    for C in ANGLES:
        if trace(operators[C])!=k(expected_trace(C)):
            raise ArithmeticError("Actual geometric angle/fixed-cycle trace mismatch.")
    for A in ANGLES:
        check()
        for B in ANGLES:
            rhs=PR(24 if A==B==0 else (48 if A==B else 0))
            rhs+=sum((compose_coeff(A,B,D)*operators[D] for D in ANGLES),PR.zero())
            if (operators[A]*operators[B]-rhs)%poly:
                raise ArithmeticError("The complete original orbital composition failed.")
    ZA=(13*operators[0]+4*operators[2])%poly
    ZB=(2*operators[4]-7*operators[0])%poly
    if trace(ZA) or trace(ZB) or trace(ZA*ZA)!=k(336288):
        raise ArithmeticError("The original sparse trace-zero correspondences changed.")
    common=poly.gcd(ZA).gcd(ZB)
    cert={
        "dimension":73,"angle_algebra_dimension":23,"base_CM_candidate_id":76,
        "complete_necklace_count":1081,"Cyclic_determinant_mod4513":int(Cyclic.det()),
        "Cyclic_matrix_sha256":digest([[int(x) for x in row] for row in Cyclic.rows()]),
        "Hodge_evaluation_sha256":digest([int(x) for x in e]),
        "angle_coefficients_sha256":digest([[int(x) for x in row] for row in rows]),
        "all_original_compositions_verified":True,
        "all_original_fixed_cycle_traces_verified":True,
        "complete_j_pull_push_zero":True,"rows":certificate_rows,
        "ZA_polynomial_sha256":digest([int(x) for x in ZA.list()]),
        "ZB_polynomial_sha256":digest([int(x) for x in ZB.list()]),
        "ZA_ZB_common_zero_degree":int(common.degree()),
        "scope":"Actual all-73 Hecke-coordinate angle action only; no QC root exclusion."}
    return {"operators":operators,"polynomial":poly,"certificate":cert,
            "Cyclic":Cyclic,"base_evaluation":e}

def main():
    global SOURCE,STAGE,DEADLINE
    req=read_request()
    hodge=module("angle_original_Hodge",HODGE)
    SOURCE=hodge.source_head()
    DEADLINE=START+1170
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,source_sha256=req["source_sha256"],
         arithmetic_seconds=1200,reserve_seconds=30)
    from sage.all import matrix,vector
    from sage.env import SAGE_VERSION
    if SAGE_VERSION!="10.6":
        raise RuntimeError("Wrong Sage runtime.")
    old=json.loads((ROOT/CM_REQUEST).read_text())
    source=hodge.build_source(descriptors=old["Hodge_descriptors"],
                              expected_certificate=old["Hodge_certificate"])
    bridge=hodge.hecke_bridge(source)
    for n in (2,3,5):
        if digest(hodge.integral_rows(bridge["operators"][n]))!=old["original_Hecke_hashes"][str(n)]:
            raise ArithmeticError("Original Hodge Hecke matrix hash mismatch.")
    H=bridge["operators"][3]+bridge["operators"][5]
    if digest(hodge.integral_rows(H))!=req["Hodd_matrix_sha256"]:
        raise ArithmeticError("The original Hodd matrix changed.")
    emit("original_Hodge_inputs_consumed",Hodge_certificate=source["certificate"],
         Hodd_matrix_sha256=req["Hodd_matrix_sha256"],
         consumed_CM_tangent_run=req["consumed_CM_tangent_run"])
    packet={"protocol":"original_angle_fields_v1","source":SOURCE,
            "request_sha256":REQUEST_HASH,"parent_pid":os.getpid(),
            "parent_started":START,"deadline":DEADLINE,
            "descriptors":[list(map(int,row)) for row in source["descriptors"]]}
    packet["descriptors_sha256"]=digest(packet["descriptors"])
    worker=None
    probe=None
    field_rows=[]
    field_receipt=None
    ready=False
    try:
        worker=subprocess.Popen([sys.executable,"-u",str(ROOT/THIS),"--field-worker"],
            cwd=ROOT,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None,
            text=True,encoding="utf-8",bufsize=1)
        worker.stdin.write(json.dumps(packet)+"\n")
        worker.stdin.flush()
        for line in worker.stdout:
            check()
            if not line.strip():
                continue
            item=json.loads(line)
            kind=item.pop("kind")
            child_seconds=item.pop("elapsed_seconds")
            if field_receipt is not None:
                raise RuntimeError("A field item followed its final receipt.")
            if kind=="field_ready":
                if ready or item["source"]!=SOURCE or item["imports_sage"] is not False:
                    raise RuntimeError("Wrong field isolation acknowledgement.")
                ready=True
                emit(kind,field_seconds=child_seconds,**item)
                continue
            if kind=="field_receipt" and item.get("status")!="complete":
                emit(kind,field_seconds=child_seconds,**item)
                raise RuntimeError("The isolated geometry failed: "+item.get("message","incomplete"))
            if not ready:
                raise RuntimeError("Field data arrived before isolation.")
            if kind=="cyclic_probe":
                if probe is not None:
                    raise RuntimeError("Duplicate geometric base point.")
                probe=item["record"]
                values=probe["coarse_tangent95"]
                if (len(values)!=95 or any(type(x) is not int or not 0<=x<Q for x in values) or
                    digest(values)!=req["consumed_CM76_coarse_tangent95_sha256"]):
                    raise ArithmeticError("Invalid certified original CM76 input bridge.")
                e=source["kernel"]*vector(source["K"],values)
                powers=[]
                v=e
                for _ in range(73):
                    powers.append(v)
                    v=H*v
                Cyclic=matrix(source["K"],powers).transpose()
                det=Cyclic.det()
                COMPLETED["cyclic_probe"]={"determinant_mod4513":int(det),
                    "coarse_tangent95_sha256":digest(values)}
                emit("new_cyclic_evaluation",**COMPLETED["cyclic_probe"])
                if not det:
                    raise ArithmeticError("The actual specified base point is not cyclic.")
                worker.stdin.write(json.dumps(
                    {"proceed":True,"coarse_tangent95_sha256":digest(values)})+"\n")
                worker.stdin.flush()
                worker.stdin.close()
            elif kind=="field_angle":
                if probe is None:
                    raise RuntimeError("An angle preceded the actual cyclic source.")
                row=item["record"]
                if row["angle"]!=([1]+ANGLES)[len(field_rows)]:
                    raise ArithmeticError("The geometric target order changed.")
                values=row["coarse_sum95"]
                if (len(values)!=95 or any(type(x) is not int or not 0<=x<Q for x in values) or
                    digest(values)!=row["coarse_sum95_sha256"]):
                    raise ArithmeticError("The exact angle-sum bridge failed.")
                field_rows.append(row)
                emit("actual_angle_sum_completed",angle=row["angle"],degree=row["degree"],
                     coarse_sum95_sha256=row["coarse_sum95_sha256"],
                     actual_targets_sha256=row["actual_targets_sha256"],
                     field_seconds=child_seconds)
            elif kind=="field_receipt":
                field_receipt=item
                if (item["status"]!="complete" or item["source"]!=SOURCE or
                    item["request_sha256"]!=REQUEST_HASH or item["necklace_count"]!=1081 or
                    item["field_rows_sha256"]!=digest(field_rows)):
                    raise RuntimeError("The complete geometric field receipt failed.")
                emit(kind,field_seconds=child_seconds,**item)
            else:
                raise RuntimeError("Unexpected geometric worker message: "+str(kind))
        code=worker.wait(timeout=max(0.1,DEADLINE-time.monotonic()))
        if code or field_receipt is None or len(field_rows)!=24:
            raise RuntimeError("The actual complete angle worker failed: "+str(code))
    finally:
        if worker is not None:
            if worker.poll() is None:
                worker.kill()
                worker.wait(timeout=5)
            if worker.stdout is not None:
                worker.stdout.close()
    STAGE="actual_all73_angle_interpolation"
    data=recover_angles(source,H,probe,field_rows,req)
    COMPLETED["angle_action"]=data["certificate"]
    emit("new_original_angle_certificate",**data["certificate"])
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="completed"
    emit("receipt",status="complete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=COMPLETED,result_sha256=digest(COMPLETED),
         scope="All original 23 angle actions in the actual73 Hecke coordinates; no disk uniqueness.")

if __name__=="__main__":
    try:
        if sys.argv[1:]==["--field-worker"]:
            field_worker()
        elif not sys.argv[1:]:
            main()
        else:
            raise RuntimeError("Unexpected command-line arguments.")
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("field_receipt" if sys.argv[1:]==["--field-worker"] else "receipt",
             status="incomplete",source=SOURCE,stage=STAGE,request_sha256=REQUEST_HASH,
             completed=COMPLETED,exception_type=type(exc).__name__,message=str(exc))
        traceback.print_exc()
        sys.exit(1)
