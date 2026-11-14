#!/usr/bin/env python3
"""Exact torsion membership and common 24-coefficient h correction.

Reuses the fully certified original 820-dimensional normal-form state, checks
its standard-coordinate dictionary against the actual T96 image certificate,
and retains full-vector identities. Run under a 60s/512MiB external cap.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import time

import flint
from flint import nmod_mat, nmod_poly

STATE_SHA = "06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load_record(path, record):
    data = Path(path).read_bytes()
    if Path(path).suffix == ".gz":
        if hashlib.sha256(data).hexdigest() != record["gzipSHA256"]:
            raise ValueError("compressed actual certificate checksum")
        data = gzip.decompress(data)
    if hashlib.sha256(data).hexdigest() != record["sha256"]:
        raise ValueError("complete actual certificate checksum")
    return data

def main():
    parser = argparse.ArgumentParser()
    for name in ("state", "state-receipt", "image-quotients", "image-remainders", "image-receipt", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    args.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    hp = root / "2026-11-14-r150-torsion-characteristic-789f.py"
    spec = importlib.util.spec_from_file_location("r150_frozen_state", hp)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    sr = json.loads(args.state_receipt.read_text())
    ir = json.loads(args.image_receipt.read_text())
    if sr.get("status") != "completed" or sr["outputs"]["state.bin"]["sha256"] != STATE_SHA or not sr["nativeStatistics"]["allTargetsInTorsion"]:
        raise ValueError("complete original state receipt required")
    if ir.get("status") != "completed" or not ir["nativeStatistics"].get("fullImageQuotientIdentity") or not ir["nativeStatistics"].get("everyRemainderIsIrreducible"):
        raise ValueError("actual complete first-residual image certificate required")
    payload = args.state.read_bytes()
    if args.state.suffix == ".gz":
        payload = gzip.decompress(payload)
    if hashlib.sha256(payload).hexdigest() != STATE_SHA:
        raise ValueError("original exact finite state checksum")
    state_path = args.out / "state-input.bin"
    state_path.write_bytes(payload)
    state = helper.load_state(state_path)
    if (state["stateDimension"], state["torsionDimension"], state["observabilityRank"]) != (820,315,505):
        raise ValueError("whole original state dimensions")
    qdata = load_record(args.image_quotients, ir["outputs"]["image-quotients.bin"])
    if qdata[:8] != b"R150IQ31" or struct.unpack_from("<4I",qdata,8) != (1034,1021,9,85):
        raise ValueError("actual complete image quotient dictionary")
    offset = 24
    heads = {}
    for _ in range(1021):
        c,d,lc = struct.unpack_from("<HBB",qdata,offset)
        offset += 4
        if c in heads or c<1 or c>1034 or d>8 or not 1<=lc<=30:
            raise ValueError("actual image head dictionary")
        heads[c]=d
        for _ in range(9):
            count = struct.unpack_from("<H",qdata,offset)[0]
            offset += 2+count
    if offset != len(qdata) or sum(heads.values()) != 716:
        raise ValueError("complete image dictionary mismatch")
    coordinates = [[c,d] for d in range(8) for c in range(1,1035) if c not in heads or d<heads[c]]
    free_components = [c for c in range(1,1035) if c not in heads]
    if coordinates != state["coordinates"] or free_components != state["freeComponents"]:
        raise ValueError("old and actual complete GB standard coordinate dictionaries differ")
    index = {tuple(cd):i for i,cd in enumerate(coordinates)}
    rdata = load_record(args.image_remainders, ir["outputs"]["image-remainders.bin"])
    if rdata[:8] != b"R150NF31" or struct.unpack_from("<3I",rdata,8) != (0,9,1034):
        raise ValueError("actual first residual remainder format")
    offset = 20
    rho = [[0]*9 for _ in range(820)]
    for j in range(9):
        raw,target,count=struct.unpack_from("<IHI",rdata,offset)
        offset+=10
        if raw or target!=j+2:
            raise ValueError("actual remainder target mapping")
        previous=0
        for _ in range(count):
            c,length=struct.unpack_from("<HB",rdata,offset)
            offset+=3
            if c<=previous or not 1<=length<=8:
                raise ValueError("actual remainder not in finite standard state")
            previous=c
            for d in range(length):
                a=rdata[offset]
                offset+=1
                if a>30 or (a and (c,d) not in index):
                    raise ValueError("nonstandard remainder entry")
                if a:
                    rho[index[c,d]][j]=a
    if offset!=len(rdata):
        raise ValueError("trailing actual remainders")
    R=nmod_mat(rho,31)
    observation=nmod_mat(state["observabilityEchelon"],31)
    observed=observation*R
    torsion=[all(int(observed[i,j])==0 for i in range(505)) for j in range(9)]
    first_observation=[]
    for j in range(9):
        first_observation.append(next(([i+1,int(observed[i,j])] for i in range(505) if int(observed[i,j])),None))
    pivots=set(state["pivotStateCoordinates"])
    free_state=[i for i in range(820) if i+1 not in pivots]
    K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose()
    J=nmod_mat(state["matrices"]["action"],31)
    residual_coordinates=nmod_mat([[rho[i][j] for j in range(9)] for i in free_state],31)
    reconstructed=K*residual_coordinates
    for j in range(9):
        valid=all(int(reconstructed[i,j])==rho[i][j] for i in range(820))
        if valid!=torsion[j]:
            raise ValueError("observability and full torsion reconstruction disagree")
    print(json.dumps({"phase":"whole-quotient-torsion-membership","allResidualsInTorsion":all(torsion),"residualsInTorsion":torsion,"firstNonzeroObservations":first_observation,"elapsedSeconds":time.monotonic()-start}),flush=True)
    ann=[]
    common=nmod_poly([1],31)
    for j in range(9):
        if not torsion[j]:
            ann.append({"target":j+2,"inTorsion":False,"firstNonzeroObservation":first_observation[j]})
            continue
        vector=nmod_mat([[int(residual_coordinates[i,j])] for i in range(315)],31)
        columns=[]
        for k in range(316):
            columns.append([int(vector[i,0]) for i in range(315)])
            if k<315:
                vector=J*vector
        krylov=nmod_mat([[columns[k][i] for k in range(316)] for i in range(315)],31)
        reduced,rank=krylov.rref()
        actual_pivots=[next(k for k in range(316) if int(reduced[i,k])) for i in range(rank)]
        if actual_pivots!=list(range(rank)):
            raise ValueError("residual Krylov initial independence")
        co=[(-int(reduced[i,rank]))%31 for i in range(rank)]+[1]
        polynomial=nmod_poly(co,31)
        check=krylov*nmod_mat([[a] for a in co+[0]*(316-len(co))],31)
        if any(int(check[i,0]) for i in range(315)):
            raise ValueError("full actual residual annihilator identity")
        common=(common//common.gcd(polynomial))*polynomial
        ann.append({"target":j+2,"inTorsion":True,"minimumDegree":rank,"coefficientsAscending":co,**helper.factored(polynomial),"initialKrylovColumnsIndependent":True,"fullVectorRelationZero":True,"krylovColumnMajorSHA256":hashlib.sha256(bytes(a for c in columns for a in c)).hexdigest()})
        print(json.dumps({"phase":"actual-residual-minimum","target":j+2,"degree":rank,"factors":ann[-1]["factors"],"elapsedSeconds":time.monotonic()-start}),flush=True)
    # All equations are retained. If any rho is outside torsion, use all820
    # state coordinates; otherwise the exact K embedding allows315 per target.
    use_torsion=all(torsion)
    d=315 if use_torsion else 820
    action=J if use_torsion else nmod_mat(state["matrices"]["A"],31)
    target=nmod_mat(state["matrices"]["targetCoordinates" if use_torsion else "targets"],31).transpose()
    rhs=residual_coordinates if use_torsion else R
    powers=[]
    for k in range(24):
        powers.append([int(target[i,j]) for j in range(9) for i in range(d)])
        if k<23:
            target=action*target
    b=[(-int(rhs[i,j]))%31 for j in range(9) for i in range(d)]
    rows=[[powers[k][r] for k in range(24)] for r in range(9*d)]
    M=nmod_mat(rows,31)
    augmented=nmod_mat([row+[b[r]] for r,row in enumerate(rows)],31)
    rank=M.rank()
    augmented_rank=augmented.rank()
    if rank!=24:
        raise ValueError("known exact common degree24 annihilator independence changed")
    correction={"unknowns":24,"equations":9*d,"coefficientRank":rank,"augmentedRank":augmented_rank,"compatible":augmented_rank==rank,"equationSpace":"exact torsion coordinates" if use_torsion else "full finite standard coordinates"}
    if augmented_rank==rank:
        reduced,rr=augmented.rref()
        if rr!=24:
            raise ValueError("correction rank")
        g=[int(reduced[k,24]) for k in range(24)]
        product=M*nmod_mat([[a] for a in g],31)
        if any(int(product[r,0])!=b[r] for r in range(9*d)):
            raise ValueError("complete nine-target h correction identity")
        correction.update(coefficientsAscending=g,fullNineTargetIdentity=True)
    else:
        # Produce an explicit small dual certificate, never just a rank label.
        single=next((r for r,row in enumerate(rows) if not any(row) and b[r]),None)
        if single is not None:
            selected=[single]
            weights=[pow(b[single],-1,31)]
        else:
            transposed,rr=augmented.transpose().rref()
            if rr!=25:
                raise ValueError("one-column augmented rank")
            selected=[next(c for c in range(9*d) if int(transposed[i,c])) for i in range(25)]
            small=nmod_mat([rows[r] for r in selected],31).transpose()
            red,rr=small.rref()
            ps=[next(c for c in range(25) if int(red[i,c])) for i in range(rr)]
            if rr!=24:
                raise ValueError("selected true coefficient rank")
            f=next(c for c in range(25) if c not in ps)
            weights=[0]*25
            weights[f]=1
            for i,p in enumerate(ps):
                weights[p]=(-int(red[i,f]))%31
            anchor=sum(weights[k]*b[r] for k,r in enumerate(selected))%31
            if not anchor:
                raise ValueError("dual correction anchor vanished")
            weights=[a*pow(anchor,-1,31)%31 for a in weights]
        if any(sum(weights[k]*rows[r][j] for k,r in enumerate(selected))%31 for j in range(24)) or sum(weights[k]*b[r] for k,r in enumerate(selected))%31!=1:
            raise ValueError("full small dual correction certificate failed")
        witness=[]
        for r,a in zip(selected,weights):
            if not a:
                continue
            target_number=2+r//d
            local=r%d
            original_coordinate=free_state[local] if use_torsion else local
            witness.append({"equationIndex":r+1,"target":target_number,"stateCoordinate":original_coordinate+1,"normalFormComponent":coordinates[original_coordinate][0],"parameterExponent":coordinates[original_coordinate][1],"weight":a,"coefficientRow":rows[r],"rightHandSide":b[r]})
        correction.update(dualCertificate=witness,dualCoefficientProductZero=True,dualRightHandSide=1)
    # Save the whole small linear system, including every original target.
    system=bytearray(b"R150HC31")+struct.pack("<4I",31,9,d,24)
    for row,value in zip(rows,b):
        system.extend(bytes(row+[value]))
    system_path=args.out/"complete-h-correction-system.bin.gz"
    system_path.write_bytes(gzip.compress(bytes(system),mtime=0))
    result={"format":"r150-first-residual-torsion-and-common-h-correction-v1","status":"completed","field":31,
      "stateSHA256":STATE_SHA,"stateReceiptSHA256":digest(args.state_receipt),"imageReceiptSHA256":digest(args.image_receipt),
      "sourceSHA256":digest(__file__),"stateReaderSHA256":digest(hp),"pythonFlintVersion":flint.__version__,"flintVersion":flint.__FLINT_VERSION__,
      "sameCompleteModuleStandardCoordinates":True,"residualsInTorsion":torsion,"fullTorsionReconstructionVerified":True,
      "firstNonzeroObservations":first_observation,"residualMinimumPolynomials":ann,
      "commonResidualMinimum":({"degree":common.degree(),"coefficientsAscending":helper.coefficients(common),**helper.factored(common)} if all(torsion) else None),
      "hCorrection":correction,"system":{"file":str(system_path),"compressedBytes":system_path.stat().st_size,"gzipSHA256":digest(system_path),"uncompressedBytes":len(system),"sha256":hashlib.sha256(system).hexdigest()},
      "elapsedSeconds":time.monotonic()-start,
      "sourceIdentity":"The original certified whole-state and the actual T96 image have exactly the same standard coordinates and represent the same complete original R module, hence their irreducible normal forms coincide. Membership uses the full505 observation rows and full820-coordinate K reconstruction. Minimal polynomials use full315-dimensional vectors. The common h correction retains all9 original targets and all24 coefficients; inconsistency has an explicit exact dual certificate. This does not decide a change of initial mod31 source by an original kernel element."}
    (args.out/"first-residual-torsion-and-h-correction.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"first-residual-torsion-and-h-correction-complete","residualsInTorsion":torsion,"commonResidualMinimum":result["commonResidualMinimum"],"coefficientRank":rank,"augmentedRank":augmented_rank,"hCorrectionCompatible":correction["compatible"],"elapsedSeconds":result["elapsedSeconds"]}),flush=True)

if __name__=="__main__":
    main()
