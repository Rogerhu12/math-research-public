#!/usr/bin/env python3
"""Isolated original support/frame input for the short Cartier consumer.

No Sage import is permitted in this process.  Existing actual markings,
short full heat flows and the original two-phase Reynolds source are consumed
from the pinned Miller support, with NEW field-valued residue jets.
"""
import argparse
import hashlib
import importlib.util
from importlib.metadata import version
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
REPO="Rogerhu12/math-research-public"
BASE=PRE+"scripts/full_p47_Miller_support.py"
TANGENTS=PRE+"scripts/full_p47_eight_CM_tangents.py"
TRANSFER=PRE+"scripts/original_p47_ell4513_cuspidal_transfer.py"
TR_REQUEST=PRE+"notes/original-p47-ell4513-cuspidal-transfer-request.json"
CM_REQUEST=PRE+"notes/full-p47-CM-height-move-request.json"
P,Q=47,4513
IDS=[0,76,77,100,108,141,196,220]
START=time.monotonic()
DEADLINE=None

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()

def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def emit(kind,**data):
    print(json.dumps(dict(kind=kind,field_seconds=time.monotonic()-START,**data),
                     sort_keys=True),flush=True)

def check():
    if DEADLINE is not None and time.monotonic()>=DEADLINE:
        raise TimeoutError("The declared original Cartier support budget was reached.")

def stop(signum,frame):
    raise TimeoutError("The declared original Cartier support budget was reached.")

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def field_jet(base,rows,jseries,e):
    """Ratios and the actual differential frame; keep the complete field."""
    if e not in (1,2,3) or len(rows)!=95 or any(len(r)!=2*e for r in rows):
        raise ArithmeticError("The new support jet has the wrong exact order.")
    if e==1:
        te=rows[0][0]-rows[0][0]+1
        parameter="heat_u"
    else:
        if len(jseries)<e+1 or any(not v.is_zero() for v in jseries[1:e]):
            raise ArithmeticError("A stable elliptic point has a forbidden j term.")
        te=jseries[e]
        parameter="j-j_support"
    if te.is_zero():
        raise ArithmeticError("The actual local parameter has zero leading term.")
    pivot=next((i for i,r in enumerate(rows) if not r[e-1].is_zero()),None)
    if pivot is None:
        raise ArithmeticError("The original degree167 frame has a basepoint.")
    if any(any(not x.is_zero() for x in r[:e-1]) for r in rows):
        raise ArithmeticError("A coarse support character did not descend.")
    zero=te-te
    inv=base.inverse_series(list(rows[pivot][e-1:2*e]),e,te/te,zero)
    values=[]
    derivatives=[]
    for row in rows:
        rr=base.series_product(list(row[e-1:2*e]),inv,e,zero)
        if any(not v.is_zero() for v in rr[1:e]):
            raise ArithmeticError("A ratio has a forbidden lower coarse coefficient.")
        values.append(rr[0])
        derivatives.append(rr[e]/te)
    if values[pivot]!=1 or not derivatives[pivot].is_zero():
        raise ArithmeticError("The projective support pivot did not normalize.")
    frame=rows[pivot][e-1]/(e*te)
    if frame.is_zero():
        raise ArithmeticError("The actual differential frame is not a unit.")
    return values,derivatives,frame,pivot,parameter

def worker(req,output,seconds):
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Only the pinned public repository's Actions may evaluate points.")
    if any(n=="sage" or n.startswith("sage.") for n in sys.modules):
        raise RuntimeError("The wheel FLINT worker must not import Sage.")
    global DEADLINE
    DEADLINE=START+seconds
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,DEADLINE-time.monotonic()))
    base=load("original_Miller_input_for_Cartier",BASE)
    old=load("original_tangent_input_for_Cartier",TANGENTS)
    base.DEADLINE=DEADLINE
    old.DEADLINE=DEADLINE
    if old.field_runtime_libraries():
        raise RuntimeError("A native FLINT runtime preceded the isolated wheel import.")
    if version("python-flint")!="0.9.0":
        raise RuntimeError("Wrong pinned wheel version.")
    from flint import fq_default_ctx,nmod_poly
    libraries=old.field_runtime_libraries()
    if len(libraries)!=1 or any("python_flint.libs" not in Path(p).parts for p in libraries):
        raise RuntimeError("The wheel FLINT library was not isolated.")
    transfer=load("original_transfer_input_for_Cartier",TRANSFER)
    transfer.STARTED,transfer.DEADLINE=START,DEADLINE
    cmreq=json.loads((ROOT/CM_REQUEST).read_text())
    trreq=json.loads((ROOT/TR_REQUEST).read_text())
    descriptors=cmreq["Hodge_descriptors"]
    if len(descriptors)!=95:
        raise RuntimeError("The complete original95 source changed.")
    _,roles,character_rows,p_models,candidates=transfer.candidate_input(ROOT,trreq,nmod_poly)
    cm_rows=transfer.consume_known_cm(candidates,trreq["certified_cm_rows"])
    byid={int(r["candidate_id"]):r for r in cm_rows}
    if sorted(byid)!=IDS:
        raise ArithmeticError("The eight original centers changed.")
    zeta0=next(z for z in range(2,Q) if pow(z,P,Q)==1)
    if zeta0!=2:
        raise ArithmeticError("The physical Weil root changed.")
    log0={pow(zeta0,i,Q):i for i in range(P)}
    beta=transfer.circle_values(zeta0,list(range(2,P-2,2)),log0)
    allI=base.all_cartans()
    result={"protocol":"full-p47-short-Cartier-support-v1","prime":P,
        "coefficient_prime":Q,"descriptor_sha256":digest(descriptors),
        "fields":[],"points":[],"centers":[],"angle_images":{},
        "family_receipts":[],"target_jet_receipt":[],"gaussian_free":[]}
    gaussian_model=None
    for identifier in IDS:
        check()
        cm=byid[identifier]
        target=[c*beta[r]%P for c,r in zip(candidates[identifier]["vector"],roles)]
        curve,pp,qq,marking=old.select_actual_model(
            transfer,fq_default_ctx,cm,target,roles,zeta0,beta)
        j=int(cm["j_rational"])%Q
        if (identifier==141)!=(j==1728%Q):
            raise ArithmeticError("Another original center entered the Gaussian support fibre.")
        e_center=2 if j==1728%Q else (3 if j==0 else 1)
        order=2*e_center-1
        jets,jseries,fm,autos,grid_receipt=base.original_native_grid(
            old,curve,pp,qq,order,j)
        evaluator=base.Evaluation(curve,jets,descriptors)
        central=evaluator.evaluate(base.I_STD,order)
        coarse,values,derivatives,pivot=base.coarse_jet(old,central,jseries,e_center)
        factorials=(1,1,2)
        old_derivatives=[[old.base_integer(row[k]*factorials[k])
                          for k in range(e_center)] for row in central]
        old_coarse,formula=old.coarse_tangent_vector(
            old_derivatives,old.base_integer(curve.a),old.base_integer(curve.b),j)
        low={"coarse_tangent95_sha256":digest(coarse),
             "heat_jets95_sha256":digest(old_derivatives),
             "G1_grid_sha256":grid_receipt["original_low_G1_grid_sha256"]}
        if (low!=base.CERTIFIED_LOW_JET_HASHES[str(identifier)] or old_coarse!=coarse or
            digest(coarse)!=req["certified_CM_tangent95_sha256"][str(identifier)]):
            raise ArithmeticError("The new short input changed R1105.")
        result["centers"].append({"candidate_id":identifier,
            "j_rational":cm["j_rational"],"coarse_parameter":"j-j_CM",
            "denominator_index":pivot,"ratio_values":values,"ratio_dz":derivatives,
            "differential_frame":coarse[pivot],"coarse_values95":coarse,
            "coarse_tangent95_sha256":digest(coarse)})
        result["target_jet_receipt"].append({"candidate_id":identifier,
            "ratio_values_sha256":digest(values),"ratio_dz_sha256":digest(derivatives),
            "differential_frame":coarse[pivot],"R1105_low_receipt":low,
            "power_series_order":order,"j_series_order":e_center})
        emit("actual_Cartier_target_frame",**result["target_jet_receipt"][-1])

        def coarse_key(I):
            return min(base.sign_class(base.conjugate(g,I)) for g in autos)

        center_key=coarse_key(base.I_STD)
        angles={0,2,4}
        if identifier==141:
            angles.update((5,20))
        if identifier==0:
            angles.add(12)
        image_counts={c:{} for c in angles}
        all_coarse=set()
        for I in allI:
            prod=base.mm(base.I_STD,I)
            c=(-(prod[0]+prod[3])*pow(2,-1,P))%P
            c=min(c,P-c)
            if c in angles:
                key=coarse_key(I)
                if key==center_key:
                    raise ArithmeticError("A nonidentity raw angle met a canonical target.")
                image_counts[c][key]=image_counts[c].get(key,0)+1
                all_coarse.add(key)
        for c,counts in image_counts.items():
            if sum(counts.values())!=(24 if c==0 else 48):
                raise ArithmeticError("An original raw angle degree was lost.")
        unseen=set(all_coarse)
        point_id={}
        closed=[]
        while unseen:
            first=min(unseen)
            orbit=[]
            current=first
            while current not in orbit:
                if current not in all_coarse:
                    raise ArithmeticError("The actual support is not Frobenius-stable.")
                orbit.append(current)
                current=coarse_key(base.conjugate(fm,current))
            if current!=first:
                raise ArithmeticError("An actual Frobenius orbit did not close.")
            representative=min(orbit)
            cut=orbit.index(representative)
            orbit=orbit[cut:]+orbit[:cut]
            f=len(orbit)
            if marking["field_degree"]%f:
                raise ArithmeticError("The actual closed degree does not divide its field.")
            e=sum(1 for g in autos if base.sign_class(
                base.conjugate(g,representative))==base.sign_class(representative))
            rows=evaluator.evaluate(representative,2*e-1)
            vv,dd,frame,piv,param=field_jet(base,rows,jseries,e)
            if any(base.frob(a,f)!=a for a in vv):
                raise ArithmeticError("Projective support values failed closed-point descent.")
            for d in range(1,f):
                if f%d==0 and all(base.frob(a,d)==a for a in vv):
                    raise ArithmeticError("The embedded support has smaller closed degree.")
            pid="%d:%s"%(identifier,",".join(map(str,representative)))
            for point in orbit:
                if point in point_id:
                    raise ArithmeticError("Closed support orbits overlap.")
                point_id[point]=pid
                unseen.discard(point)
            record={"id":pid,"field_id":str(identifier),"degree":f,
                "values95":[base.encode(a) for a in vv],
                "derivatives95":[base.encode(a) for a in dd],
                "differential_frame":base.encode(frame),"uniformizer":param,
                "native_Cartan":list(representative),"effective_stabilizer":e,
                "projective_pivot":piv,"geometric_orbit":[list(a) for a in orbit],
                "power_series_order":2*e-1}
            # A fine parameter may descend with an automorphism.  Do NOT require
            # its derivative or frame separately to be in k(P); the residue
            # formed by their ratio is checked over k(P) in the Sage parent.
            closed.append(record)
            result["points"].append(record)
        for c,counts in image_counts.items():
            grouped={}
            for key,mult in counts.items():
                pid=point_id[key]
                if pid in grouped and grouped[pid]!=mult:
                    raise ArithmeticError("A raw coarse multiplicity changed under Frobenius.")
                grouped[pid]=mult
            degree=sum(grouped[row["id"]]*row["degree"]
                       for row in closed if row["id"] in grouped)
            if degree!=(24 if c==0 else 48):
                raise ArithmeticError("Closed grouping changed an original angle cycle.")
            result["angle_images"]["%d:%d"%(identifier,c)]=[
                [pid,grouped[pid]] for pid in sorted(grouped)]
        result["fields"].append({"id":str(identifier),"degree":marking["field_degree"],
            "modulus":[int(c) for c in curve.field.modulus()]})
        receipt={"candidate_id":identifier,"actual_marking":marking,
            "new_short_grid":grid_receipt,"selected_angles":sorted(angles),
            "geometric_support_count":len(all_coarse),"closed_support_count":len(closed),
            "closed_support_jet_sha256":digest(closed),
            "angle_images_sha256":digest({str(c):result["angle_images"][
                "%d:%d"%(identifier,c)] for c in sorted(angles)}),
            "target_frame_sha256":digest(result["centers"][-1])}
        result["family_receipts"].append(receipt)
        emit("actual_Cartier_support_family",**receipt)
        if identifier==141:
            if (marking["field_degree"]!=1 or fm!=base.ONE or
                old.base_integer(curve.a)!=343 or not curve.b.is_zero() or
                tuple(old.base_integer(a) for a in pp)!=(653,525) or
                tuple(old.base_integer(a) for a in qq)!=(3860,232)):
                raise ArithmeticError("The shared Gaussian physical source changed.")
            all_keys={coarse_key(I) for I in allI}
            free_keys=[I for I in sorted(all_keys) if sum(
                base.sign_class(base.conjugate(g,I))==base.sign_class(I)
                for g in autos)==1]
            if len(free_keys)!=528:
                raise ArithmeticError("The original Gaussian free coarse fibre is not 528.")
            for I in free_keys:
                if I in all_coarse:
                    continue
                rows=evaluator.evaluate(I,0)
                vals=[old.base_integer(row[0]) for row in rows]
                if not any(vals):
                    raise ArithmeticError("A free Gaussian point is a logarithmic basepoint.")
                if base.conjugate(fm,I)!=I:
                    raise ArithmeticError("A selected Gaussian frame is not rational.")
                result["gaussian_free"].append({"Cartan":list(I),
                    "frame":list(base.cartan_frame(I)),"values95":vals})
            if len(result["gaussian_free"])<312:
                raise ArithmeticError("The proven common Gaussian evaluation supply was lost.")
            gaussian_model={"A":343,"B":0,"P":[653,525],"Q":[3860,232],
                "i":95,"weil_root":2,"free_coarse_count":528,
                "retained_common_count":len(result["gaussian_free"]),
                "retained_common_sha256":digest(result["gaussian_free"])}
            emit("actual_Cartier_Gaussian_candidates",**gaussian_model)
    if [row["candidate_id"] for row in result["centers"]]!=IDS or gaussian_model is None:
        raise ArithmeticError("The original fixed source packet is incomplete.")
    result["gaussian_model"]=gaussian_model
    tmp=Path(str(output)+".tmp")
    tmp.write_text(json.dumps(result,sort_keys=True,separators=(",",":")))
    tmp.replace(output)
    signal.setitimer(signal.ITIMER_REAL,0)
    emit("actual_Cartier_support_receipt",status="complete",
         result_sha256=digest(result),closed_point_count=len(result["points"]),
         Gaussian_candidate_count=len(result["gaussian_free"]),
         scope="New finite residue jets and shared Gaussian constants only; no alpha computed.")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--request",required=True)
    parser.add_argument("--output",required=True)
    parser.add_argument("--seconds",required=True,type=int)
    args=parser.parse_args()
    raw=Path(args.request).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("The isolated support request pin changed.")
    req=json.loads(raw)
    if req["execution_id"]!="full-p47-short-Cartier-third-kind-v1":
        raise RuntimeError("Wrong isolated Cartier support request.")
    for path,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("Pinned support source changed: "+path)
    if not 1<=args.seconds<=int(req["field_worker_seconds"]):
        raise RuntimeError("The isolated budget exceeds the declared input stage.")
    worker(req,Path(args.output),args.seconds)

if __name__=="__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("actual_Cartier_support_receipt",status="incomplete",
             exception_type=type(exc).__name__,message=str(exc))
        traceback.print_exc()
        sys.exit(1)
