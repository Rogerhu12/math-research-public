#!/usr/bin/env python3
"""R863 appendix: the actual H22 companion in the complete S22/type4 space.

Public execution only: --workers=4, python-flint==0.9.0.
Reuses the original full CM7/CM13 fiber algorithms, with all sigma ratios
and the original S34 absolute CM13 anchor. No generated inputs and no
output files. This does not identify any Hecke character or prove a
divided-row nonvanishing.
"""
from __future__ import annotations
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Mathematical execution is restricted to the public repository Actions.")
import concurrent.futures, hashlib, importlib.util, json, pathlib, sys, time
from flint import fmpq as Q
START=time.time()
HERE=pathlib.Path(__file__).resolve().parent

def module(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp)
    sys.modules[name]=m
    sp.loader.exec_module(m)
    return m

C=module("r863_h22_cm13",HERE/"check-r732-original-type-five-cm13.py")
D7=module("r863_h22_cm7",HERE/"check-r464-degree102-cm7-exact.py")
Z,O,W=C.Z,C.O,C.W
K,add,neg,sub,mul,div,inv,scale,power,enc=C.K,C.add,C.neg,C.sub,C.mul,C.div,C.inv,C.scale,C.power,C.enc
mm,ma,ms,eye,mpow,null,rref=C.mm,C.ma,C.ms,C.eye,C.mpow,C.null,C.rref
pa,ps,pm,pd,pi,ppow,rem,peval=C.pa,C.ps,C.pm,C.pd,C.pi,C.ppow,C.rem,C.peval
NTH=22
DIM=4
HV=[Z,K(464),K(-380),K(65)]

def fiber13(a):
    F=pa(C.N,ps(C.D,K(-a)))
    F=ps(F,inv(F[-1]))
    assert len(F)==14
    pi(pd(F),F)
    ratio=rem(pm(C.qb,pi(C.q,F)),F)
    xb=rem(pm(C.NB,pi(C.DB,F)),F)
    value=ppow(ratio,NTH,F)
    step=ppow(xb,3,F)
    fp=pd(F)
    row=[]
    for j in range(DIM):
        rr=rem(pm(value,fp),F)
        row.append(div(rr[12] if len(rr)>12 else Z,C.G))
        value=rem(pm(value,step),F)

    # The same complete S34 source fixes the absolute trace phase.
    r34=ppow(ratio,34,F)
    sp=[K(-128,0,7),K(-80,0,7),K(-12,0,7),K(-53,0,7),O]
    sv=[]
    for j,c in enumerate(sp):
        sv=pa(sv,ps(ppow(xb,2+3*j,F),c))
    rr=rem(pm(rem(pm(r34,sv),F),fp),F)
    sa=mul(power(K(a),2),peval(sp,power(K(a),3)))
    assert (rr[12] if len(rr)>12 else Z)==neg(mul(C.G,sa))
    print("R863 H22 complete norm13 fiber",a,
          "elapsed",round(time.time()-START,3),file=sys.stderr,flush=True)
    return a,row

def fiber7(a):
    _,r=D7.exact_fiber_row((NTH,0,a))
    row=[K(Q(x[0])+Q(x[1]),2*Q(x[1])) for x in r]
    assert len(row)==DIM
    print("R863 H22 complete norm7 fiber",a,
          "elapsed",round(time.time()-START,3),file=sys.stderr,flush=True)
    return a,row

def matrix(f):
    ats=list(range(1,DIM+3))
    with concurrent.futures.ProcessPoolExecutor(max_workers=C.ARGS.workers) as ex:
        rows=dict(ex.map(f,ats))
    V=[[K(a**(3*j)) for j in range(DIM)] for a in ats[:DIM]]
    M=[[Z]*DIM for _ in range(DIM)]
    for j in range(DIM):
        _,piv,col=rref(V,[rows[a][j] for a in ats[:DIM]])
        assert len(piv)==DIM
        for i,v in enumerate(col):
            M[i][j]=v
    for a in ats[DIM:]:
        assert mm([[K(a**(3*j)) for j in range(DIM)]],M)[0]==rows[a]
    return M

def characteristic(A):
    I=eye(DIM)
    B=I
    ch=[O]
    for k in range(1,DIM+1):
        B=mm(A,B)
        c=scale(C.sumk(B[i][i] for i in range(DIM)),Q(-1,k))
        ch.append(c)
        B=ma(B,ms(I,c))
    assert all(x==Z for row in B for x in row)
    return ch

def action(A,v):
    return [r[0] for r in mm(A,[[x] for x in v])]

def scalar(A,v):
    av=action(A,v)
    j=next(i for i,x in enumerate(v) if x!=Z)
    ev=div(av[j],v[j])
    return ev if all(av[i]==mul(ev,v[i]) for i in range(DIM)) else None

def rank(rows):
    return len(rref(rows)[1])

def transpose(A):
    return [list(x) for x in zip(*A)]

def source_cyclic(A7,A13):
    rows=[HV]
    ranks=[1]
    while True:
        extra=rows+mm(rows,transpose(A7))+mm(rows,transpose(A13))
        R,piv,_=rref(extra)
        new=[r[:DIM] for r in R[:len(piv)]]
        ranks.append(len(new))
        if len(new)==len(rows):
            return ranks,new
        rows=new

def krylov(A):
    rows=[]
    v=HV
    for _ in range(DIM):
        rows.append(v)
        v=action(A,v)
    return {"rank":rank(rows),
            "vectors_H_NH_N2H_N3H":[[enc(x) for x in r] for r in rows]}

def common_mu6_lines(A7,A13):
    roots=[O,neg(O),W,neg(W),mul(W,W),neg(mul(W,W))]
    I=eye(DIM)
    out=[]
    for ev7 in roots:
        for ev13 in roots:
            ker=null(ma(A7,ms(I,neg(ev7)))+ma(A13,ms(I,neg(ev13))))
            for v in ker:
                lead=max(j for j,x in enumerate(v) if x!=Z)
                v=[div(x,v[lead]) for x in v]
                assert action(A7,v)==[mul(ev7,x) for x in v]
                assert action(A13,v)==[mul(ev13,x) for x in v]
                out.append({"N7":enc(ev7),"N13":enc(ev13),
                            "polynomial_X_ascending":[enc(x) for x in v],
                            "first_order":NTH-6*lead})
    return out

def main():
    A13=matrix(fiber13)
    A7=matrix(fiber7)
    assert mm(A13,A7)==mm(A7,A13)
    ranks,space=source_cyclic(A7,A13)
    mats={"N7":[[enc(x) for x in r] for r in A7],
          "N13":[[enc(x) for x in r] for r in A13]}
    ch7=characteristic(A7)
    ch13=characteristic(A13)
    ev7=scalar(A7,HV)
    ev13=scalar(A13,HV)
    ans={
      "status":"PASS",
      "field":"Q(omega), omega^2+omega+1=0",
      "degree":NTH,
      "basis":"sigma^22 X^j, j=0,...,3; X=x^3; b=1",
      "source_H22":"sigma^22 X (65X^2-380X+464)",
      "source_polynomial_X_ascending":[enc(x) for x in HV],
      "source_first_order":4,
      "source_first_coefficient":65,
      "normalization":"N_gamma=[gamma]_*[bar_gamma]^*/gamma",
      "fitting_complete_fibers":[1,2,3,4],
      "additional_complete_fibers":[5,6],
      "S34_absolute_CM13_anchor_preserved":True,
      "complete_matrices":mats,
      "N7_char_descending":[enc(x) for x in ch7],
      "N13_char_descending":[enc(x) for x in ch13],
      "N7_H22":[enc(x) for x in action(A7,HV)],
      "N13_H22":[enc(x) for x in action(A13,HV)],
      "H22_N7_eigenvalue":None if ev7 is None else enc(ev7),
      "H22_N13_eigenvalue":None if ev13 is None else enc(ev13),
      "H22_joint_cyclic_ranks":ranks,
      "H22_joint_cyclic_rref":[[enc(x) for x in r] for r in space],
      "H22_N7_krylov":krylov(A7),
      "H22_N13_krylov":krylov(A13),
      "common_mu6_eigenlines":common_mu6_lines(A7,A13),
      "canonical_matrix_sha256":hashlib.sha256(
          json.dumps(mats,separators=(",",":")).encode()).hexdigest(),
      "dependency_sha256":{p:hashlib.sha256((HERE/p).read_bytes()).hexdigest()
          for p in ["check-r732-original-type-five-cm13.py",
                    "check-r464-degree102-cm7-exact.py"]},
      "elapsed_seconds":time.time()-START,
      "scope":"Only the actual complete finite CM operators and the specified H22 source. No identification of all 2/3/11 Schwartz labels, no central zero, and no target-prime or divided-row nonvanishing.",
      "output_files":False}
    ans["run"]={
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID"),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "script_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "readme_blobs":{"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
          "topics/rank2-sha-infinitely-many-p/README.md":os.environ.get("RANK2_TOPIC_README_SHA")},
        "parameters":{"workers":C.ARGS.workers,"python_flint":"0.9.0"}
    }
    payload=json.dumps(ans,sort_keys=True,separators=(",",":"))
    print("RANK2_H22_CM_RESULT "+payload,flush=True)
    print("RANK2_H22_CM_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)

if __name__=="__main__":
    main()
