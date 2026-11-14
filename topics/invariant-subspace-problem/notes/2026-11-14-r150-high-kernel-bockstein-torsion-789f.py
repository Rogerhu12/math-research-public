#!/usr/bin/env python3
"""All200 original Bocksteins and1152 allowed shifts in the infinite quotient.

This is only a necessary test for the true finite B85 cokernel. Every output
explicitly keeps finite_budget_verified=False, even when the image test passes.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,struct,time
from pathlib import Path
import flint
from flint import nmod_mat

STATE_SHA="06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
RHO_SHA="f3efdaf748571cd830decf3e67b87d9821f1508cc794a6eecd93b5a6a1260e45"

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        while b:=f.read(1048576):h.update(b)
    return h.hexdigest()

def parse_nf(data, expected, index):
    if data[:8]!=b"R150NF31" or struct.unpack_from("<3I",data,8)!=(0,len(expected),1034):
        raise ValueError("complete normal-form header")
    offset=20
    rows=[[0]*len(expected) for _ in range(820)]
    for j,label in enumerate(expected):
        raw,number,count=struct.unpack_from("<IHI",data,offset);offset+=10
        if raw or number!=label:raise ValueError("actual normal-form column label")
        previous=0
        for _ in range(count):
            c,length=struct.unpack_from("<HB",data,offset);offset+=3
            if c<=previous or c>1034 or not 1<=length<=8:raise ValueError("class outside the certified finite normal-form state")
            previous=c
            for d in range(length):
                a=data[offset];offset+=1
                if a>30 or (a and (c,d) not in index):raise ValueError("nonstandard actual image coefficient")
                if a:rows[index[c,d]][j]=a
    if offset!=len(data):raise ValueError("trailing actual normal forms")
    return rows

def main():
    p=argparse.ArgumentParser()
    for name in ("state","state-receipt","original-metadata","image-metadata","image-quotients","image-remainders","first-remainders","out"):
        p.add_argument("--"+name,type=Path,required=True)
    a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
    root=Path(__file__).resolve().parent
    hp=root/"2026-11-14-r150-torsion-characteristic-789f.py"
    spec=importlib.util.spec_from_file_location("r150_frozen_torsion_state",hp);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    receipt=json.loads(a.state_receipt.read_text());original=json.loads(a.original_metadata.read_text());imeta=json.loads(a.image_metadata.read_text())
    if receipt.get("status")!="completed" or receipt["outputs"]["state.bin"]["sha256"]!=STATE_SHA or not receipt["nativeStatistics"].get("allTargetsInTorsion"):raise ValueError("complete original whole-state receipt required")
    if original.get("status")!="completed" or original.get("highKernelColumns")!=200 or not original.get("fullOriginalBocksteinDivisionIdentity") or not original.get("allIndividualWeightedBoundsVerified"):raise ValueError("complete original200 Bockstein source identities required")
    if imeta.get("status")!="completed" or not imeta.get("fullImageQuotientIdentity") or not imeta.get("everyRemainderIsIrreducible") or imeta.get("finite_budget_verified") is not False:raise ValueError("complete infinite-quotient image identities required")
    labels=original["labels"]
    if len(labels)!=200 or {cost:sum(L[2]==cost for L in labels) for cost in (80,81,85)}!={80:160,81:38,85:2}:raise ValueError("actual200 kernel costs")
    data=a.state.read_bytes()
    if a.state.suffix==".gz":data=gzip.decompress(data)
    if hashlib.sha256(data).hexdigest()!=STATE_SHA:raise ValueError("original state checksum")
    state_path=a.out/"state-input.bin";state_path.write_bytes(data);state=helper.load_state(state_path)
    qdata=a.image_quotients.read_bytes()
    if qdata[:8]!=b"R150IQ31" or struct.unpack_from("<4I",qdata,8)!=(1034,1021,200,85):raise ValueError("all200 quotient dictionary")
    offset=24;heads={}
    for _ in range(1021):
        c,d,lc=struct.unpack_from("<HBB",qdata,offset);offset+=4
        if c in heads or not 1<=c<=1034 or d>8 or not 1<=lc<=30:raise ValueError("actual image head dictionary")
        heads[c]=d
        for _ in range(200):
            length=struct.unpack_from("<H",qdata,offset)[0];offset+=2+length
    if offset!=len(qdata) or sum(heads.values())!=716:raise ValueError("complete original image dictionary")
    coordinates=[[c,d] for d in range(8) for c in range(1,1035) if c not in heads or d<heads[c]]
    if coordinates!=state["coordinates"] or [c for c in range(1,1035) if c not in heads]!=state["freeComponents"]:raise ValueError("complete module standard coordinates changed")
    index={tuple(cd):i for i,cd in enumerate(coordinates)}
    beta_rows=parse_nf(a.image_remainders.read_bytes(),[L[1] for L in labels],index)
    first=a.first_remainders.read_bytes()
    if a.first_remainders.suffix==".gz":first=gzip.decompress(first)
    if hashlib.sha256(first).hexdigest()!=RHO_SHA:raise ValueError("original first residual remainder checksum")
    rho_rows=parse_nf(first,list(range(2,11)),index)
    pivots=set(state["pivotStateCoordinates"]);free=[i for i in range(820) if i+1 not in pivots]
    K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose();J=nmod_mat(state["matrices"]["action"],31)
    observation=nmod_mat(state["observabilityEchelon"],31)
    BR=nmod_mat(beta_rows,31);RR=nmod_mat(rho_rows,31)
    B=nmod_mat([[beta_rows[i][j] for j in range(200)] for i in free],31)
    R=nmod_mat([[rho_rows[i][j] for j in range(9)] for i in free],31)
    observed=observation*BR
    if any(int(observed[i,j]) for i in range(505) for j in range(200)):raise ValueError("original Bockstein has a nonzero infinite free part; no torsion projection may be substituted")
    bk=K*B;rk=K*R
    if any(int(bk[i,j])!=beta_rows[i][j] for i in range(820) for j in range(200)) or any(int(rk[i,j])!=rho_rows[i][j] for i in range(820) for j in range(9)):raise ValueError("full original state reconstruction failed")
    print(json.dumps({"phase":"all200-infinite-quotient-torsion","columns":200,"full505ObservationsZero":True,"full820CoordinatesVerified":True,"finite_budget_verified":False,"elapsedSeconds":time.monotonic()-start}),flush=True)
    powers=[B]
    for k in range(5):powers.append(J*powers[-1])
    descriptors=[];columns=[]
    for j,L in enumerate(labels):
        for shift in range(86-L[2]):
            descriptors.append([j+1,L[1],shift,L[2]+shift])
            columns.append([int(powers[shift][r,j]) for r in range(315)])
    if len(columns)!=1152:raise ValueError("exact finite-budget kernel shift count")
    rows=[[columns[c][r] for c in range(1152)] for r in range(315)]
    X=nmod_mat(rows,31);right=[[int(R[r,j]) for j in range(9)] for r in range(315)]
    augmented=nmod_mat([rows[r]+right[r] for r in range(315)],31)
    rank=X.rank();red,augmented_rank=augmented.rref()
    pivot_columns=[next(c for c in range(1161) if int(red[r,c])) for r in range(augmented_rank)]
    if sum(c<1152 for c in pivot_columns)!=rank or any(c>=1152 for c in pivot_columns[:rank]):raise ValueError("actual augmented coefficient pivots")
    compatible=[all(int(red[r,1152+j])==0 for r in range(rank,augmented_rank)) for j in range(9)]
    solutions=[[0]*9 for _ in range(1152)]
    for j in range(9):
        if compatible[j]:
            for r in range(rank):solutions[pivot_columns[r]][j]=int(red[r,1152+j])
    product=X*nmod_mat(solutions,31)
    if any(int(product[r,j])!=right[r][j] for j in range(9) if compatible[j] for r in range(315)):raise ValueError("complete315-dimensional necessary source-combination identity")
    dual=None
    if not all(compatible):
        j=next(j for j in range(9) if not compatible[j]);single=next((r for r,row in enumerate(rows) if not any(row) and right[r][j]),None)
        if single is not None:selected=[single];weights=[pow(right[single][j],-1,31)]
        else:
            one=nmod_mat([rows[r]+[right[r][j]] for r in range(315)],31);tr,rr=one.transpose().rref()
            if rr!=rank+1:raise ValueError("failed RHS augmented rank")
            selected=[next(c for c in range(315) if int(tr[i,c])) for i in range(rr)]
            sub=nmod_mat([rows[r] for r in selected],31).transpose();sred,srank=sub.rref()
            if srank!=rank:raise ValueError("dual selected coefficient rank")
            ps=[next(c for c in range(rank+1) if int(sred[i,c])) for i in range(rank)]
            f=next(c for c in range(rank+1) if c not in ps);weights=[0]*(rank+1);weights[f]=1
            for i,c in enumerate(ps):weights[c]=(-int(sred[i,f]))%31
            anchor=sum(weights[k]*right[r][j] for k,r in enumerate(selected))%31
            if not anchor:raise ValueError("dual necessary-test anchor")
            weights=[v*pow(anchor,-1,31)%31 for v in weights]
        if any(sum(weights[k]*rows[r][c] for k,r in enumerate(selected))%31 for c in range(1152)) or sum(weights[k]*right[r][j] for k,r in enumerate(selected))%31!=1:raise ValueError("full1152-column dual necessary certificate")
        dual={"target":j+2,"coordinates":[{"torsionCoordinate":r+1,"stateCoordinate":free[r]+1,"normalFormComponent":coordinates[free[r]][0],"parameterExponent":coordinates[free[r]][1],"weight":w} for r,w in zip(selected,weights) if w],"all1152CoefficientProductsZero":True,"rightHandSide":1}
    # The whole finite family of allowed shifts is saved. It is being projected
    # into the infinite quotient; its1152 original source labels remain intact.
    system=bytearray(b"R150BI31")+struct.pack("<7I",31,315,200,1152,9,rank,augmented_rank)
    for L in labels:system.extend(struct.pack("<IHHII",*L))
    for d in descriptors:system.extend(struct.pack("<4H",*d))
    system.extend(bytes(v for row in rows for v in row));system.extend(bytes(v for row in right for v in row));system.extend(bytes(v for row in solutions for v in row))
    system.extend(struct.pack(f"<{rank}H",*pivot_columns[:rank]));system.extend(bytes(int(red[r,c]) for r in range(rank) for c in range(1152)));system.extend(bytes(compatible))
    sp=a.out/"complete-infinite-quotient-system.bin.gz";sp.write_bytes(gzip.compress(bytes(system),mtime=0))
    base=bytearray(b"R150BV31")+struct.pack("<3I",31,315,200)
    for L in labels:base.extend(struct.pack("<IHHII",*L))
    base.extend(bytes(int(B[r,c]) for r in range(315) for c in range(200)))
    bp=a.out/"all200-torsion-columns.bin.gz";bp.write_bytes(gzip.compress(bytes(base),mtime=0))
    result={"format":"r150-all200-original-bockstein-infinite-quotient-test-v1","status":"completed","field":31,
      "finite_budget_verified":False,"infiniteQuotientNecessaryTestOnly":True,"stateSHA256":STATE_SHA,"sourceSHA256":sha(__file__),"stateReaderSHA256":sha(hp),
      "originalMetadataSHA256":sha(a.original_metadata),"imageMetadataSHA256":sha(a.image_metadata),"imageRemaindersSHA256":sha(a.image_remainders),"firstRemaindersSHA256":RHO_SHA,
      "pythonFlintVersion":flint.__version__,"flintVersion":flint.__FLINT_VERSION__,"all200BocksteinsInTorsion":True,"full505ObservationsZero":True,"full820CoordinatesVerified":True,
      "actualHighKernelColumns":200,"allowedB85ShiftColumns":1152,"infiniteImageRank":rank,"augmentedRank":augmented_rank,"targetCompatibility":compatible,"allNineTargetsPassInfiniteNecessaryTest":all(compatible),
      "full315CoordinateSolutionChecks":True,"dualCertificate":dual,"coefficientPivotColumnsOneBased":[c+1 for c in pivot_columns[:rank]],"shiftDescriptors":descriptors,
      "outputs":{"system":{"file":str(sp),"gzipBytes":sp.stat().st_size,"gzipSHA256":sha(sp),"bytes":len(system),"sha256":hashlib.sha256(system).hexdigest()},"baseColumns":{"file":str(bp),"gzipBytes":bp.stat().st_size,"gzipSHA256":sha(bp),"bytes":len(base),"sha256":hashlib.sha256(base).hexdigest()}},
      "elapsedSeconds":time.monotonic()-start,
      "sourceIdentity":"Every one of the200 original high kernels has its original6188-row integer mod961 Bockstein identity. Only its infinite polynomial quotient class is used in this necessary test. All1152 shifts satisfy the individual source cost85 bound, all9 original first residuals are retained, and all315 torsion coordinates are checked. A positive result is not the true1658-dimensional finite-cokernel test: the remaining canonical-source coefficients of cost>85 must still be paid. No characteristic-zero conclusion is asserted."}
    (a.out/"high-kernel-infinite-quotient-result.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"all200-original-bockstein-infinite-test-complete","all200BocksteinsInTorsion":True,"allowedB85ShiftColumns":1152,"infiniteImageRank":rank,"augmentedRank":augmented_rank,"targetCompatibility":compatible,"allNineTargetsPassInfiniteNecessaryTest":all(compatible),"finite_budget_verified":False,"elapsedSeconds":result["elapsedSeconds"]}),flush=True)

if __name__=="__main__":main()
