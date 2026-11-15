#!/usr/bin/env python3
"""R816: actual S66 complete CM7/CM13 mass kernel and E[-11] rank witness.

Public execution only: --workers=4, python-flint==0.9.0.
No generated inputs and no output files.  Reuses the original full-fiber
producers, with their complete sigma carrier and absolute normalization.
This does not identify a Hecke character by a handful of Frobenius values.
"""
from __future__ import annotations
import concurrent.futures, hashlib, importlib.util, json, pathlib, sys, time
from flint import fmpq as Q
START=time.time()
HERE=pathlib.Path(__file__).resolve().parent
def module(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m)
    return m
C=module("r816_cm13",HERE/"check-r732-original-type-five-cm13.py")
D7=module("r816_cm7",HERE/"check-r464-degree102-cm7-exact.py")
Z,O,W=C.Z,C.O,C.W
K,add,neg,sub,mul,div,inv,scale,power,enc=C.K,C.add,C.neg,C.sub,C.mul,C.div,C.inv,C.scale,C.power,C.enc
mm,ma,ms,eye,mpow,null,rref=C.mm,C.ma,C.ms,C.eye,C.mpow,C.null,C.rref
pa,ps,pm,pd,pi,ppow,rem,peval=C.pa,C.ps,C.pm,C.pd,C.pi,C.ppow,C.rem,C.peval
NTH=66;DIM=12

def fiber13(a):
    F=pa(C.N,ps(C.D,K(-a)));F=ps(F,inv(F[-1]))
    assert len(F)==14
    pi(pd(F),F)
    ratio=rem(pm(C.qb,pi(C.q,F)),F)
    xb=rem(pm(C.NB,pi(C.DB,F)),F)
    value=ppow(ratio,NTH,F)
    step=ppow(xb,3,F);fp=pd(F);row=[]
    for j in range(DIM):
        r=rem(pm(value,fp),F)
        row.append(div(r[12] if len(r)>12 else Z,C.G))
        value=rem(pm(value,step),F)
    # Full original S34 anchor; the same canonical trace, not a reset phase.
    r34=ppow(ratio,34,F)
    sp=[K(-128,0,7),K(-80,0,7),K(-12,0,7),K(-53,0,7),O]
    sv=[]
    for j,c in enumerate(sp):sv=pa(sv,ps(ppow(xb,2+3*j,F),c))
    rt=rem(pm(rem(pm(r34,sv),F),fp),F)
    sa=mul(power(K(a),2),peval(sp,power(K(a),3)))
    assert (rt[12] if len(rt)>12 else Z)==neg(mul(C.G,sa))
    print("R816 complete norm13 fiber",a,"elapsed",round(time.time()-START,3),
          file=sys.stderr,flush=True)
    return a,row

def fiber7(a):
    _,r=D7.exact_fiber_row((NTH,0,a))
    # Producer uses delta; this script uses omega with delta=1+2omega.
    row=[K(Q(x[0])+Q(x[1]),2*Q(x[1])) for x in r]
    print("R816 complete norm7 fiber",a,"elapsed",round(time.time()-START,3),
          file=sys.stderr,flush=True)
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
        for i,v in enumerate(col):M[i][j]=v
    for a in ats[DIM:]:
        assert mm([[K(a**(3*j)) for j in range(DIM)]],M)[0]==rows[a]
    return M

def characteristic(A):
    I=eye(DIM);B=I;ch=[O]
    for k in range(1,DIM+1):
        B=mm(A,B)
        c=scale(C.sumk(B[i][i] for i in range(DIM)),Q(-1,k))
        ch.append(c);B=ma(B,ms(I,c))
    assert all(x==Z for row in B for x in row)
    return ch

def mass_observability(A):
    row=[Z]*(DIM-1)+[O];out=[]
    for _ in range(DIM):
        out.append(row);row=mm([row],A)[0]
    return out

def scalar_on_vector(A,v):
    av=mm(A,[[x] for x in v])
    j=next(i for i,x in enumerate(v) if x!=Z)
    ev=div(av[j][0],v[j])
    return ev if all(av[i][0]==mul(ev,v[i]) for i in range(DIM)) else None

def rank_witness():
    # A 2-descent homomorphism on the good finite reduction with rational
    # 2-torsion (r,0) is x-r modulo squares.  Its kernel contains 2E.
    P=(3,4);Qp=(15,58)
    assert P[1]**2==P[0]**3-11 and Qp[1]**2==Qp[0]**3-11
    report=[]
    for ell,r in ((5,1),(17,12)):
        assert (r**3-11)%ell==0
        vals=[]
        for x,y in (P,Qp):
            assert (y*y-x*x*x+11)%ell==0 and (x-r)%ell
            vals.append(pow((x-r)%ell,(ell-1)//2,ell))
        report.append({"prime":ell,"two_torsion_x":r,"Legendre_P_Q":vals})
    assert report[0]["Legendre_P_Q"]==[4,1]
    assert report[1]["Legendre_P_Q"]==[1,16]
    # E(Q)[2]=0 because 11 is not a rational cube.
    return report

def main():
    witness=rank_witness()
    A13=matrix(fiber13)
    A7=matrix(fiber7)
    assert mm(A13,A7)==mm(A7,A13)
    Obs13=mass_observability(A13)
    Obs7=mass_observability(A7)
    # Actual mass row closure under both original operators.
    R,piv,_=rref(Obs13+Obs7)
    rows=[r[:DIM] for r in R[:len(piv)]]
    ranks=[len(rows)]
    while True:
        extra=rows+mm(rows,A13)+mm(rows,A7)
        R,piv,_=rref(extra)
        newrows=[r[:DIM] for r in R[:len(piv)]]
        ranks.append(len(newrows))
        if len(newrows)==len(rows):break
        rows=newrows
    ker=null(rows)
    normalized=[]
    for v in ker:
        lead=max(j for j,x in enumerate(v) if x!=Z)
        v=[div(x,v[lead]) for x in v]
        normalized.append({
          "polynomial_X_ascending":[enc(x) for x in v],
          "origin_order":NTH-6*lead,
          "norm7_eigenvalue":None if scalar_on_vector(A7,v) is None else enc(scalar_on_vector(A7,v)),
          "norm13_eigenvalue":None if scalar_on_vector(A13,v) is None else enc(scalar_on_vector(A13,v))})
    mats=json.dumps({"N7":[[enc(x) for x in row] for row in A7],
                     "N13":[[enc(x) for x in row] for row in A13]},separators=(",",":"))
    ans={
      "status":"PASS","field":"Q(omega), omega^2+omega+1=0",
      "degree":NTH,"basis":"sigma^66 X^j (j=0,...,11), X=x^3, b=1",
      "normalization":"N_gamma=[gamma]_*[bar_gamma]^*/gamma",
      "full_fibers_per_operator":list(range(1,DIM+3)),
      "rank_witness_for_y2_x3_minus11":witness,
      "N13_char_descending":[enc(x) for x in characteristic(A13)],
      "N7_char_descending":[enc(x) for x in characteristic(A7)],
      "N13_mass_kernel_dimension":len(null(Obs13)),
      "N7_mass_kernel_dimension":len(null(Obs7)),
      "joint_observability_ranks":ranks,
      "joint_mass_kernel_dimension":len(ker),
      "joint_mass_kernel":normalized,
      "canonical_matrix_sha256":hashlib.sha256(mats.encode()).hexdigest(),
      "dependency_sha256":{p:hashlib.sha256((HERE/p).read_bytes()).hexdigest()
          for p in ["check-r732-original-type-five-cm13.py",
                    "check-r464-degree102-cm7-exact.py"]},
      "elapsed_seconds":time.time()-START,
      "scope":"Exact whole S66 type0 operators and actual common mass kernel. The new E[-11] local Schwartz and conductor must be proved separately; no finite-prime rank guesses.",
      "output_files":False}
    print(json.dumps(ans,separators=(",",":")))
if __name__=="__main__":main()
