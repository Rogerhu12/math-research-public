#!/usr/bin/env python3
"""Actual first QC rows on the eight original full-level47 CM disks.

New scope is the full trace pairing and each explicitly requested (A,B)
matrix, using already certified heights, CM first logs and third-kind values.
Every old source regenerated here is a hash-pinned input, not a new scan.
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
REQUEST=ROOT/(PRE+"notes/full-p47-QC-first-rows-request.json")
THIS=PRE+"scripts/full_p47_QC_first_rows.py"
Q,P=4513,47
IDS=[0,76,77,100,108,141,196,220]
BASIC=[0,141,76,108]
START=time.monotonic()
DEADLINE=None
SOURCE=None
REQUEST_HASH=None
STAGE="preflight"
COMPLETED={}


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def matrix_rows(M):
    return [[int(a) for a in row] for row in M.rows()]


def emit(kind,**data):
    print(json.dumps(dict(kind=kind,elapsed_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)


def check():
    if DEADLINE is not None and time.monotonic()>=DEADLINE:
        raise TimeoutError("The declared original QC arithmetic reserve was reached.")


def stop(signum,frame):
    raise TimeoutError("The declared original QC arithmetic reserve was reached.")


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


def read_request():
    global REQUEST_HASH
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("Mathematics is restricted to this public repository's Actions.")
    raw=REQUEST.read_bytes()
    REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("The original QC request hash changed.")
    req=json.loads(raw)
    if (req["execution_id"]!="full-p47-QC-first-rows-v2" or req["prime"]!=P or
            req["coefficient_prime"]!=Q or req["sage_version"]!="10.6" or
            req["python_flint_version"]!="0.9.0" or req["total_seconds"]!=2400 or
            req["reserve_seconds"]!=60 or req["correspondences"]!=["ZA","ZB"]):
        raise RuntimeError("Unexpected original full-trace QC request.")
    centers=list(map(int,req["CM_candidate_ids"]))
    if not centers or centers!=sorted(set(centers)) or any(i not in IDS for i in centers):
        raise RuntimeError("Only the named original CM disks may be read.")
    for path,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("An original QC source pin changed: "+path)
    return req


def field_worker():
    """Only reconstruct consumed CM tangents/angles, with their old full hashes."""
    global DEADLINE,SOURCE,STAGE
    req=read_request()
    packet=json.loads(sys.stdin.read())
    if (packet["protocol"]!="original_QC_field_inputs_v1" or
            packet["request_sha256"]!=REQUEST_HASH or packet["parent_pid"]!=os.getppid()):
        raise RuntimeError("The original field consumer has no pinned parent.")
    DEADLINE=float(packet["deadline"])
    if not time.monotonic()<DEADLINE:
        raise TimeoutError("The old field inputs have no remaining shared time.")
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,DEADLINE-time.monotonic())
    tangent=module("QC_old_tangents",PRE+"scripts/full_p47_eight_CM_tangents.py")
    SOURCE=tangent.checkout_source_head()
    if SOURCE!=packet["source"]:
        raise RuntimeError("The original field inputs have the wrong source checkout.")
    if tangent.field_runtime_libraries() or any(
            n=="sage" or n.startswith("sage.") for n in sys.modules):
        raise RuntimeError("A native mathematical runtime preceded the pure field worker.")
    from flint import fq_default_ctx,nmod_poly
    libraries=tangent.field_runtime_libraries()
    if version("python-flint")!="0.9.0" or len(libraries)!=1 or (
            "python_flint.libs" not in Path(libraries[0]).parts):
        raise RuntimeError("The original field worker did not isolate wheel FLINT.")
    tangent.DEADLINE=DEADLINE
    transfer=module("QC_old_transfer",PRE+"scripts/original_p47_ell4513_cuspidal_transfer.py")
    transfer.DEADLINE=DEADLINE
    angle=module("QC_old_angles",PRE+"scripts/full_p47_original_angle_Hodge_action.py")
    angle.DEADLINE=DEADLINE
    cmreq=json.loads((ROOT/(PRE+"notes/full-p47-CM-height-move-request.json")).read_text())
    trreq=json.loads((ROOT/(PRE+"notes/original-p47-ell4513-cuspidal-transfer-request.json")).read_text())
    descriptors=packet["descriptors"]
    if descriptors!=cmreq["Hodge_descriptors"] or digest(descriptors)!=packet["descriptors_sha256"]:
        raise ArithmeticError("The field packet changed the original95 descriptors.")
    old,roles,characters,models,candidates=transfer.candidate_input(ROOT,trreq,nmod_poly)
    cms=transfer.consume_known_cm(candidates,trreq["certified_cm_rows"])
    by_id={int(cm["candidate_id"]):cm for cm in cms}
    zeta0=next(z for z in range(2,Q) if pow(z,P,Q)==1)
    log0={pow(zeta0,j,Q):j for j in range(P)}
    beta=transfer.circle_values(zeta0,list(range(2,P-2,2)),log0)
    tangents={}
    field_rows=None
    probe=None
    original_angles={int(row["angle"]):row for row in req["consumed_angle_certificate"]["rows"]}
    for identifier in IDS:
        check()
        STAGE="consume_CM_%d"%identifier
        target=[c*beta[r]%P for c,r in zip(candidates[identifier]["vector"],roles)]
        curve,pp,qq,marking=tangent.select_actual_model(
            transfer,fq_default_ctx,by_id[identifier],target,roles,zeta0,beta)
        model=marking["model"]
        order=1 if model["j"]==1728%Q else (2 if model["j"]==0 else 0)
        grid,gcert=tangent.torsion_grid(curve,pp,qq,order,model["j"])
        jets=tangent.original_reynolds_jets(curve,grid,descriptors,order)
        coarse,formula=tangent.coarse_tangent_vector(jets,model["A"],model["B"],model["j"])
        actual={"G1_grid_sha256":gcert["grid_sha256"],"heat_jets95_sha256":digest(jets),
                "coarse_tangent95_sha256":digest(coarse)}
        if actual!=req["consumed_CM_low_jet_hashes"][str(identifier)]:
            raise ArithmeticError("An actual original CM input changed its certified three hashes.")
        tangents[str(identifier)]=coarse
        emit("consumed_CM_input",candidate_id=identifier,coarse_tangent95_sha256=digest(coarse))
        if identifier==76:
            evals=angle.OriginalReynoldsValues(curve.field,descriptors,grid)
            groups=angle.field_targets()
            scale=(4*model["A"]**3+27*model["B"]**2)*pow(
                124416*model["A"]**2*model["B"]%Q,-1,Q)%Q
            field_rows=[]
            for c in [1]+angle.ANGLES:
                check()
                total=[curve.field.zero() for _ in descriptors]
                thash=hashlib.sha256()
                for necklace,frame in groups[c]:
                    vv=evals.values(frame)
                    for k,x in enumerate(vv):
                        total[k]+=x
                    thash.update(canonical([list(necklace),list(frame)])+b"\n")
                values=[scale*tangent.base_integer(x)%Q for x in total]
                row={"angle":c,"degree":len(groups[c]),
                     "actual_targets_sha256":thash.hexdigest(),
                     "coarse_sum95":values,"coarse_sum95_sha256":digest(values)}
                prior=original_angles[c]
                if any(row[k]!=prior[k] for k in (
                        "angle","degree","actual_targets_sha256","coarse_sum95_sha256")):
                    raise ArithmeticError("A consumed original angle input changed its exact receipt.")
                field_rows.append(row)
            if field_rows[0]["coarse_sum95"]!=coarse:
                raise ArithmeticError("The complete identity angle is not the same original CM76 point.")
            probe={"candidate_id":76,"coarse_tangent95":coarse}
    if field_rows is None or probe is None or sorted(map(int,tangents))!=IDS:
        raise ArithmeticError("The complete requested old geometric inputs are missing.")
    answer={"protocol":"original_QC_field_inputs_v1","source":SOURCE,
            "request_sha256":REQUEST_HASH,"tangents95":tangents,
            "probe":probe,"angle_rows":field_rows,"wheel_flint_libraries":libraries}
    signal.setitimer(signal.ITIMER_REAL,0)
    print(json.dumps(dict(kind="field_input_packet",packet=answer,
                         packet_sha256=digest(answer)),sort_keys=True),flush=True)


def consume_field_inputs(req,source):
    packet={"protocol":"original_QC_field_inputs_v1","source":SOURCE,
            "request_sha256":REQUEST_HASH,"parent_pid":os.getpid(),
            "deadline":DEADLINE,"descriptors":source["descriptors"],
            "descriptors_sha256":digest(source["descriptors"])}
    proc=subprocess.Popen([sys.executable,"-u",str(ROOT/THIS),"--field-worker"],
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
        text=True,env=dict(os.environ))
    try:
        stdout,stderr=proc.communicate(canonical(packet).decode(),
                                     timeout=max(0.1,DEADLINE-time.monotonic()))
    except BaseException:
        proc.kill()
        proc.communicate()
        raise
    finally:
        if proc.poll() is None:
            proc.kill()
            proc.communicate()
    answer=None
    for line in stdout.splitlines():
        item=json.loads(line)
        if item.get("kind")=="field_input_packet":
            if answer is not None or digest(item["packet"])!=item["packet_sha256"]:
                raise ArithmeticError("The consumed geometric packet did not round-trip.")
            answer=item["packet"]
        else:
            emit("old_field_input_progress",record=item)
    if proc.returncode or answer is None:
        if stderr:
            print(stderr[-12000:],file=sys.stderr,flush=True)
        raise RuntimeError("An old field input could not be reconstructed; no new QC row.")
    if answer["source"]!=SOURCE or answer["request_sha256"]!=REQUEST_HASH:
        raise ArithmeticError("An old field input belongs to a different actual source.")
    return answer


def height_multiplier(basis,req):
    """Recover the already certified K=kappa/a from its 73 saved small values."""
    from sage.all import matrix,vector
    P=basis["polynomial"]
    K=P.base_ring()
    PR=P.parent()
    indices=basis["indices"]
    pairs=req["consumed_height_values"]
    if [int(row[0]) for row in pairs]!=indices or digest(pairs)!=req[
            "consumed_height_certificate"]["height_values_sha256"]:
        raise ArithmeticError("The complete original 73 height-value inputs changed.")
    g=vector(K,[int(row[1]) for row in pairs])
    moments=basis["coordinate_matrix"].solve_right(g)
    traces=[K(73)]
    for k in range(1,145):
        if k<=73:
            traces.append(-K(k)*P[73-k]-sum(
                (P[73-j]*traces[k-j] for j in range(1,k)),K.zero()))
        else:
            traces.append(-sum((P[73-j]*traces[k-j] for j in range(1,74)),K.zero()))
    gram=matrix(K,[[traces[i+j] for j in range(73)] for i in range(73)])
    coeff=gram.solve_right(moments)
    kappa=PR(list(coeff))
    resolvent=PR([sum((moments[j]*P[i+j+1] for j in range(73-i)),K.zero())
                  for i in range(73)])
    if (resolvent*P.derivative().inverse_mod(P))%P!=kappa:
        raise ArithmeticError("The consumed original height trace/resolvent normalization changed.")
    a=((basis["hecke_polynomials"][2]-1)/K(2))%P
    w=(kappa*a.inverse_mod(P))%P
    cert=req["consumed_height_certificate"]
    actual={"Hodd_height_moments_sha256":digest(list(map(int,moments))),
            "trace_Gram_sha256":digest(matrix_rows(gram)),
            "kappa_coefficients_sha256":digest(list(map(int,coeff))),
            "resolvent_numerator_sha256":digest([int(c) for c in resolvent.list()]),
            "full_height_multiplier_norm":int(P.resultant(w)),
            "normalized_full_height_determinant_mod4513":int(gram.det()*P.resultant(w))}
    if any(actual[k]!=cert[k] for k in actual):
        raise ArithmeticError("A full original height coefficient changed its prior certificate.")
    return w,traces[:73],actual


def consume_gaussian_generator(source,req):
    """R1093's full vector was not stored; regenerate it as a pinned input."""
    from sage.all import PolynomialRing,vector
    gaussian=module("QC_original_Gaussian_source",PRE+"scripts/full_p47_Gaussian_CM_log.py")
    gaussian.DEADLINE=DEADLINE
    gaussian.emit=lambda kind,**data:emit("consumed_Gaussian_source_progress",
                                        source_kind=kind,record=data)
    ring=PolynomialRing(source["K"],"z")
    S,grid=gaussian.torsion_eisenstein_grid(ring,(653,525),(3860,232),95)
    W=gaussian.coefficient_weight(S)
    moments=gaussian.original_forms_moments(S,grid,source["descriptors"],W)
    lam=source["kernel"]*vector(source["K"],moments)
    if digest(list(map(int,lam)))!=req["consumed_Gaussian_log"]["lambda73_sha256"]:
        raise ArithmeticError("The actual original Bq*u4 first-log input changed.")
    emit("original_MW_generator_consumed",
         source_run=req["consumed_Gaussian_log"]["run"],
         lambda73_sha256=req["consumed_Gaussian_log"]["lambda73_sha256"],
         original_divisor="Bq*(23*y1728-C_infinity)",new_log_conclusion=False)
    return lam


def read_actual_QC_rows(source,basis,w,traces,lambda0,angles,geometric,req):
    """The full 73-dimensional trace, with every original scale retained."""
    from sage.all import matrix,vector,PolynomialRing,identity_matrix
    K=source["K"]
    PR=basis["polynomial"].parent()
    P=basis["polynomial"]
    H=basis["Hodd"]
    columns=[]
    v=lambda0
    for _ in range(73):
        columns.append(v)
        v=H*v
    L=matrix(K,columns).transpose()
    if not L.det():
        raise ArithmeticError("The paid original MW log lattice is not integral.")
    inverse=L.inverse()
    ops=angles["operators"]
    ZA=(13*ops[0]+4*ops[2])%P
    ZB=(2*ops[4]-7*ops[0])%P
    fixed={
        "ZA":((13*ops[20]+4*ops[5])%P,(13*ops[4])%P,ZA),
        "ZB":((-7*ops[20])%P,(2*ops[12]-7*ops[4])%P,ZB),
    }
    logs={}
    coordinate_method=req["CM_coordinate_method"]
    if coordinate_method=="q2-residue-trace-R1108":
        certificates=req["consumed_CM_logs"]
        if digest(certificates)!=req["consumed_CM_logs_sha256"]:
            raise ArithmeticError("The completed original CM log records changed their pinned hash.")
        if {int(r["candidate_id"]) for r in certificates}!=set(BASIC) or len(certificates)!=4:
            raise ArithmeticError("All four actual original basic CM log columns are required.")
        for row in certificates:
            identifier=int(row["candidate_id"])
            values=row["lambda73"]
            if (row["exact_divisor"]!="23*y-C_infty" or row["coefficient_prime"]!=Q or
                    row["modulus"]!=Q*Q or row["N_mod_q"]!=551 or
                    row["N_sha256"]!=req["consumed_group_order_json_sha256"] or
                    row["terminal"]["terminal_reduction_is_actual_D0"] is not True or
                    len(values)!=73 or any(type(x) is not int or not 0<=x<Q for x in values)
                    or digest(values)!=row["lambda73_sha256"]):
                raise ArithmeticError("A consumed original CM first-log column is invalid.")
            logs[identifier]=PR(list(inverse*vector(K,values)))
    elif coordinate_method=="signed-Jacobi-R1119":
        records=req["consumed_CM_Hecke_coordinates"]
        cert=req["consumed_CM_Hecke_certificate"]
        if (digest(records)!=req["consumed_CM_Hecke_coordinates_sha256"] or
                digest(cert)!=req["consumed_CM_Hecke_certificate_sha256"] or
                len(records)!=4 or {int(r["candidate_id"]) for r in records}!=set(BASIC)):
            raise ArithmeticError("The four complete signed Jacobi coordinate inputs changed.")
        bcert=basis["certificate"]
        if (cert["prime"]!=47 or cert["coefficient_prime"]!=Q or cert["dimension"]!=73 or
                cert["common_reference_rank"]!=73 or cert["reference_discriminant"]!=-4 or
                cert["reference_pair"]!=[-8836,0] or cert["actual_Hodge_row_checks"]!=[2,3,5] or
                cert["Hodd_characteristic_polynomial_sha256"]!=bcert[
                    "Hodd_characteristic_polynomial_sha256"] or
                cert["Hodd_matrix_sha256"]!=bcert["Hodd_matrix_sha256"] or
                cert["exact_rational_path_relations"] is not True or
                cert["all_needed_denominators_q_units"] is not True or
                cert["consumed_Tq_integer_charpoly_sha256"]!=
                    "ca554eaecfa7f5ac349fdf9db69f32e584eb45c0787714e97e6ef3c44e1cba62" or
                cert["Bq_determinant_mod_q"]!=551):
            raise ArithmeticError("The actual full73 Jacobi projection or Bq source is incomplete.")
        def original_coefficients(values,wanted):
            if (len(values)!=73 or any(type(x) is not int or not 0<=x<Q for x in values)
                    or digest(values)!=wanted):
                raise ArithmeticError("An actual original Hecke coordinate vector is malformed.")
            return PR(values)
        bp=original_coefficients(cert["Bq_coefficients"],cert["Bq_coefficients_sha256"])
        if bp.gcd(P)!=PR.one() or int(P.resultant(bp))!=551:
            raise ArithmeticError("The signed coordinate input lost the original Bq unit.")
        discs={141:(-4,2),0:(-3,3),76:(-7,1),108:(-8,1)}
        for row in records:
            identifier=int(row["candidate_id"])
            D,units=discs[identifier]
            if (row["method"]!="R1119" or row["coefficient_prime"]!=Q or row["dimension"]!=73 or
                    row["fundamental_discriminant"]!=D or
                    row["exact_divisor"]!="23*y_%d-C_infty"%identifier or
                    row["weighted_Jacobi_pair"]!=[2209*D,0 if D%2==0 else 2209] or
                    row["source_coarse_weight"]!=1 or row["reverse_incidence_multiplicity"]!=units or
                    row["Hodd_characteristic_polynomial_sha256"]!=cert[
                        "Hodd_characteristic_polynomial_sha256"] or
                    row["Bq_coefficients_sha256"]!=cert["Bq_coefficients_sha256"]):
                raise ArithmeticError("An actual CM point, signed pair or coarse weight changed.")
            ratio=original_coefficients(row["ratio_to_u4_coefficients"],row["ratio_to_u4_sha256"])
            coordinate=original_coefficients(row["coordinate_relative_Bq_u4_coefficients"],
                                            row["coordinate_relative_Bq_u4_sha256"])
            if (coordinate*bp-ratio)%P or (identifier==141 and ratio!=PR.one()):
                raise ArithmeticError("An actual CM class has the wrong Bq normalization.")
            logs[identifier]=coordinate
        COMPLETED["CM_coordinate_input"]={"method":coordinate_method,
            "certificate_sha256":req["consumed_CM_Hecke_certificate_sha256"],
            "records_sha256":req["consumed_CM_Hecke_coordinates_sha256"]}
    else:
        raise RuntimeError("No recognized complete original CM coordinate source.")
    p2=basis["hecke_polynomials"][2]
    p3=basis["hecke_polynomials"][3]
    logs[196]=((p2-1)*logs[141]/K(2))%P
    logs[220]=(p2*logs[0]/K(3))%P
    logs[77]=((p3-1)*logs[0]/K(3))%P
    logs[100]=((p2-2)*logs[76])%P
    if set(logs)!=set(IDS) or logs[141].gcd(P).degree()!=0:
        raise ArithmeticError("The actual eight CM log classes or paid u4 unit are missing.")
    tangents={}
    for identifier in IDS:
        values=geometric["tangents95"][str(identifier)]
        if digest(values)!=req["consumed_CM_low_jet_hashes"][str(identifier)][
                "coarse_tangent95_sha256"]:
            raise ArithmeticError("An original CM tangent changed its certified scale.")
        e=source["kernel"]*vector(K,values)
        tangents[identifier]=PR(list(inverse*e))
    third={}
    if digest(req["consumed_third_kind_values"])!=req["consumed_third_kind_values_sha256"]:
        raise ArithmeticError("The completed original third-kind records changed their pinned hash.")
    for row in req["consumed_third_kind_values"]:
        key=(int(row["candidate_id"]),str(row["angle"]))
        if (key in third or row["id"]!="%d-%s"%key or row["coarse_parameter"]!="j-j_CM" or
                row["clearing_denominator"]!=6 or row["order_mod_q"]!=551 or
                type(row["alpha"]) is not int or not 0<=row["alpha"]<Q):
            raise ArithmeticError("A consumed original third-kind value has wrong normalization.")
        method=row.get("method","R1107-finite-Miller")
        if method=="R1118-short-Cartier":
            cc=req["consumed_Cartier_matrix_certificate"]
            if (digest(cc)!=req["consumed_Cartier_matrix_certificate_sha256"] or
                    row["Cartier_matrix_certificate_sha256"]!=digest(cc) or
                    cc["dimension"]!=73 or cc["one_minus_C_determinant"]!=551 or
                    cc["convention"]!="columns; original Hecke row is transpose"):
                raise ArithmeticError("A complete original Cartier source is missing.")
            rr=row["meromorphic_RR_certificate"]
            degree=int(rr["reduced_support_degree"])
            if (rr["id"]!=row["id"] or rr["all_original_cusps_included"] is not True or
                    rr["support_ideal_dimension"]!=262-degree or
                    rr["numerator_dimension"]!=72+degree or rr["residue_rank"]!=degree-1 or
                    rr["original_cleared_divisor_sha256"]!=row["exact_initial_divisor_sha256"] or
                    not 0<degree<=(159 if key[1]=="ZA" else 151) or
                    len(row["all_eight_log_derivatives"])!=8 or
                    any(type(x) is not int or not 0<=x<Q for x in row["all_eight_log_derivatives"]) or
                    row["all_eight_log_derivatives"][IDS.index(key[0])]!=row["alpha"]):
                raise ArithmeticError("A normalized Cartier value lost its full original residue source.")
        elif method!="R1107-finite-Miller":
            raise ArithmeticError("An unrecognized third-kind source was supplied.")
        third[key]=K(row["alpha"])
    if any(r.get("method")=="R1118-short-Cartier" for r in req["consumed_third_kind_values"]):
        cc=req["consumed_Cartier_matrix_certificate"]
        if coordinate_method=="signed-Jacobi-R1119":
            one=identity_matrix(K,73)
            Bmatrix=0*one
            for a in reversed(bp.list()):
                Bmatrix=Bmatrix*H+a*one
            # Same original Hodge frame, not merely matching spectra or det(1-C).
            if digest(matrix_rows(one-Bmatrix))!=cc["Cartier_row_matrix_sha256"]:
                raise ArithmeticError("The actual Cartier matrix differs from the signed Jacobi Tq coordinate.")
        COMPLETED["Cartier_input_certificate_sha256"]=digest(cc)
    wanted={(int(i),z) for i in req["CM_candidate_ids"] for z in ("ZA","ZB")}
    if set(third)!=wanted:
        raise ArithmeticError("The new QC request must supply exactly its completed local values.")
    def tr(f):
        f%=P
        return sum((f[j]*traces[j] for j in range(73)),K.zero())
    TP=PolynomialRing(K,"t")
    t=TP.gen()
    answer=[]
    for identifier in req["CM_candidate_ids"]:
        check()
        identifier=int(identifier)
        b=tangents[identifier]
        cy=logs[identifier]
        coeffrows=[]
        equations=[]
        for name in ("ZA","ZB"):
            f4,f3,z=fixed[name]
            d=(f4*logs[141]/K(2)+K(2)*f3*logs[0]/K(3)-2*z*cy)/K(23)
            d%=P
            A=-tr(w*z*b*b)
            global_B=tr(w*b*d)
            alpha=third[identifier,name]
            B=global_B-alpha
            coeffrows.append({"angle":name,"A":int(A),"B":int(B),
                "global_linear_part":int(global_B),"actual_local_alpha":int(alpha),
                "tangent_coordinates_sha256":digest([int(b[j]) for j in range(73)]),
                "Chow_Heegner_coordinates_sha256":digest([int(d[j]) for j in range(73)]),
                "trace_uses_all_73_directions":True})
            equations.append(t*(B+A*t))
        M=matrix(K,[[r["A"],r["B"]] for r in coeffrows])
        gcd=TP.zero()
        for f in equations:
            gcd=gcd.gcd(f)
        if gcd:
            gcd=gcd.monic()
        rank=int(M.rank())
        simple=any(r["B"] for r in coeffrows)
        unique=bool(simple and gcd==t)
        if unique!=(simple and (rank==2 or all(r["A"]==0 for r in coeffrows))):
            raise ArithmeticError("The exact reduced common-root and full-rank tests disagree.")
        row={"candidate_id":identifier,"coarse_parameter":"j-j_CM","z_equals":"4513*t",
             "actual_equations":"t*(B+A*t)","rows":coeffrows,
             "matrix_rank":rank,"matrix_determinant":int(M.det()),
             "common_reduction_polynomial":None if not gcd else [int(x) for x in gcd.list()],
             "common_reduction_is_identically_zero":not bool(gcd),
             "common_roots":None if not gcd else [
                 [int(r),int(m)] for r,m in gcd.roots()],
             "some_linear_coefficient_is_a_unit":simple,
             "whole_original_4513_disk_unique":unique,
             "integral_tail_and_nonq_terms_source":"R1103 including section6.1 and R1074 bad47"}
        answer.append(row)
        emit("actual_QC_first_rows",**row)
    return {"coefficient_prime":Q,"dimension":73,
            "original_MW_log_matrix_sha256":digest(matrix_rows(L)),
            "original_MW_log_matrix_determinant":int(L.det()),
            "height_multiplier_sha256":digest([int(w[j]) for j in range(73)]),
            "all_eight_CM_coordinate_sha256":digest([
                [i,[int(logs[i][j]) for j in range(73)]] for i in IDS]),
            "requested_CM_disks":list(map(int,req["CM_candidate_ids"])),
            "disks":answer,"all_requested_disks_unique":all(
                r["whole_original_4513_disk_unique"] for r in answer),
            "scope":"Exactly the requested original4513 disks; fixed level47 only, Serre uniformity remains open."}


def main():
    global SOURCE,STAGE,DEADLINE
    req=read_request()
    DEADLINE=START+2340
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    hodge=module("QC_original_Hodge",PRE+"scripts/full_p47_weight_one_Hodge_certificate.py")
    SOURCE=hodge.source_head()
    from sage.env import SAGE_VERSION
    from sage.all import proof
    if SAGE_VERSION!="10.6":
        raise RuntimeError("Wrong pinned Sage release.")
    proof.all(True)
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,requested_CM_disks=req["CM_candidate_ids"])
    STAGE="consume_original_fixed_odd_basis"
    basis_module=module("QC_original_odd_basis",PRE+"scripts/full_p47_small_odd_Hecke_basis.py")
    basisreq=json.loads((ROOT/req["consumed_basis_request_path"]).read_text())
    basis=basis_module.build_basis(basisreq,indices=req["consumed_basis_certificate"]["indices"],
                                  expected_certificate=req["consumed_basis_certificate"])
    COMPLETED["basis_certificate_sha256"]=digest(basis["certificate"])
    old=json.loads((ROOT/(PRE+"notes/full-p47-CM-height-move-request.json")).read_text())
    source=hodge.build_source(descriptors=old["Hodge_descriptors"],
                              expected_certificate=old["Hodge_certificate"])
    STAGE="consume_complete_height_pairing"
    w,traces,hcert=height_multiplier(basis,req)
    COMPLETED["height_input"]=hcert
    STAGE="consume_actual_geometric_inputs"
    geometric=consume_field_inputs(req,source)
    angle=module("QC_original_angles",PRE+"scripts/full_p47_original_angle_Hodge_action.py")
    angle.DEADLINE=DEADLINE
    areq=json.loads((ROOT/(PRE+"notes/full-p47-original-angle-Hodge-request.json")).read_text())
    angles=angle.recover_angles(source,basis["Hodd"],geometric["probe"],
                               geometric["angle_rows"],areq)
    if angles["certificate"]!=req["consumed_angle_certificate"]:
        raise ArithmeticError("The complete original angle-action certificate changed.")
    COMPLETED["angle_input_sha256"]=digest(angles["certificate"])
    STAGE="consume_original_MW_generator_log"
    lambda0=consume_gaussian_generator(source,req)
    STAGE="new_actual_full_trace_QC_rows"
    result=read_actual_QC_rows(source,basis,w,traces,lambda0,angles,geometric,req)
    COMPLETED["QC_first_rows"]=result
    signal.setitimer(signal.ITIMER_REAL,0)
    STAGE="complete"
    emit("receipt",status="complete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         request_sha256=REQUEST_HASH,completed=COMPLETED,result_sha256=digest(COMPLETED),
         scope=result["scope"])


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
        emit("receipt",status="incomplete",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
             request_sha256=REQUEST_HASH,stage=STAGE,completed=COMPLETED,
             exception_type=type(exc).__name__,message=str(exc),
             scope="Only explicitly complete requested QC rows survive; no uncomputed exclusion.")
        traceback.print_exc()
        sys.exit(1)
