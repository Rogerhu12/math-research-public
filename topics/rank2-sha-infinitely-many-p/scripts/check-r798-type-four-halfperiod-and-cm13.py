#!/usr/bin/env python3
"""R798: full S34/type4 CM13 and canonical halfperiod B projector.

Reuses the actual R732 division/trace algorithm, not saved output tables.
The halfperiod matrix is derived from x(z+t) at all three actual E[2] roots.
Its only sign is calibrated by the paid whole H_Y(S)=omega^2 S identity.
Also reads type5 H_Y on the same complete fibers, without assigning a
Schwartz identity or any negative-moment nonvanishing to the type4 space.
Public: python3 scripts/check-r798-type-four-halfperiod-and-cm13.py --workers=4
Dependencies: python-flint==0.9.0. No output files.
"""
from __future__ import annotations
import concurrent.futures, hashlib, importlib.util, json, pathlib, sys, time
START=time.time()
path=pathlib.Path(__file__).with_name("check-r732-original-type-five-cm13.py")
spec=importlib.util.spec_from_file_location("r798_core",path)
core=importlib.util.module_from_spec(spec);sys.modules[spec.name]=core
spec.loader.exec_module(core)
for name in ("Q","Z","O","W","K","add","neg","sub","mul","scale","inv","div","conj",
             "power","sumk","enc","trim","pa","pn","ps","pm","pd","pq","rem","pi",
             "ppow","peval","ratio_derivative","rref","mm","ma","ms","eye","mpow","null"):
    globals()[name]=getattr(core,name)
DEL=K(1,2);OM2=mul(W,W)
def ordinary_power(P,n):
    r=[O]
    while n:
        if n&1:r=pm(r,P)
        P=pm(P,P);n//=2
    return r
def monomial(n,a=O):return [Z]*n+[a]
def full_half_sum(P,odd_y=False):
    """U: i*T_nonzero summed, up to one common canonical sign."""
    out=[]
    for e in (neg(O),neg(W),neg(OM2)):
        assert power(e,3)==neg(O)
        invphase=inv(power(mul(DEL,e),17))
        for n,c in enumerate(P):
            if c==Z:continue
            if odd_y:
                assert n<=15
                scalar=mul(c,mul(invphase,mul(K(-3),power(e,n+2))))
                term=pm(ordinary_power([scale(e,2),O],n),
                        ordinary_power([neg(e),O],15-n))
            else:
                assert n<=17
                scalar=mul(c,mul(invphase,power(e,n)))
                term=pm(ordinary_power([scale(e,2),O],n),
                        ordinary_power([neg(e),O],17-n))
            out=pa(out,ps(term,scalar))
    return out
SP=[K(-128,0,7),K(-80,0,7),K(-12,0,7),K(-53,0,7),O]
S=[]
for j,c in enumerate(SP):S=pa(S,monomial(2+3*j,c))
US=full_half_sum(S)
SIGNS=[s for s in (1,-1) if ps(US,K(s))==ps(S,DEL)]
assert len(SIGNS)==1,"canonical phase is uniquely fixed by original S"
EPS=SIGNS[0]
def h_action(P,odd_y=False):
    return ps(pa(P,ps(full_half_sum(P,odd_y),K(EPS))),K(-1,0,2))
assert h_action(S)==ps(S,OM2)
def h_matrix(exponents,odd_y):
    H=[]
    cols=[]
    for n in exponents:
        P=h_action(monomial(n),odd_y)
        assert all(c==Z or j in exponents for j,c in enumerate(P))
        cols.append([P[j] if j<len(P) else Z for j in exponents])
    H=[list(row) for row in zip(*cols)]
    I=eye(len(exponents))
    assert ma(ma(mm(H,H),H),I)==ms(I,Z)
    return H
H4=h_matrix([3*j for j in range(6)],False)
H5=h_matrix([1+3*j for j in range(5)],True)
PB4=ms(ma(eye(6),ms(H4,neg(W))),inv(sub(O,OM2)))
PB5=ms(ma(eye(5),ms(H5,neg(W))),inv(sub(O,OM2)))
assert mm(PB4,PB4)==PB4 and mm(PB5,PB5)==PB5
def fiber(a):
    F=pa(core.N,ps(core.D,K(-a)));F=ps(F,inv(F[-1]))
    assert len(F)==14
    pi(pd(F),F)
    ratio=rem(pm(core.qb,pi(core.q,F)),F)
    xb=rem(pm(core.NB,pi(core.DB,F)),F)
    yr=ps(rem(pm(ratio_derivative(core.NB,core.DB,F),
             pi(ratio_derivative(core.N,core.D,F),F)),F),div(core.G,core.GB))
    r34=ppow(ratio,34,F);fp=pd(F);step=ppow(xb,3,F)
    def rows(value,n):
        out=[]
        for j in range(n):
            r=rem(pm(value,fp),F);out.append(r[12] if len(r)>12 else Z)
            value=rem(pm(value,step),F)
        return out
    row4=rows(r34,6)
    row5=rows(rem(pm(pm(r34,yr),xb),F),5)
    sv=[]
    for j,c in enumerate(SP):sv=pa(sv,ps(ppow(xb,2+3*j,F),c))
    rt=rem(pm(rem(pm(r34,sv),F),fp),F)
    sa=mul(power(K(a),2),peval(SP,power(K(a),3)))
    assert (rt[12] if len(rt)>12 else Z)==neg(mul(core.G,sa))
    print("R798 complete CM13 fiber",a,"elapsed",round(time.time()-START,3),
          file=sys.stderr,flush=True)
    return a,{"type4":row4,"type5":row5}
def operator(rows,key,exponents,fit,extra):
    V=[[K(a**n) for n in exponents] for a in fit]
    M=[[Z]*len(exponents) for _ in exponents]
    for j in range(len(exponents)):
        _,piv,col=rref(V,[rows[a][key][j] for a in fit])
        assert len(piv)==len(exponents)
        for i,v in enumerate(col):M[i][j]=v
    for a in extra:
        assert mm([[K(a**n) for n in exponents]],M)[0]==rows[a][key]
    return ms(M,inv(core.G))
def characteristic(A):
    I=eye(len(A));B=I;ch=[O]
    for k in range(1,len(A)+1):
        B=mm(A,B)
        c=scale(sumk(B[i][i] for i in range(len(A))),Q(-1,k))
        ch.append(c);B=ma(B,ms(I,c))
    assert all(x==Z for r in B for x in r)
    return ch
def restriction(A,P):
    _,piv,_=rref(P)
    B=[[r[j] for j in piv] for r in P]
    d=len(piv);AB=mm(A,B);R=[[Z]*d for _ in range(d)]
    for j in range(d):
        _,rp,col=rref(B,[r[j] for r in AB])
        assert len(rp)==d
        for i,x in enumerate(col):R[i][j]=x
    assert mm(B,R)==AB
    return B,R,piv
def eigens(A):
    out=[]
    for ev in (O,neg(O),W,neg(W),OM2,neg(OM2)):
        for v in null(ma(A,ms(eye(len(A)),neg(ev)))):
            lead=max(j for j,x in enumerate(v) if x!=Z)
            v=[div(x,v[lead]) for x in v]
            out.append({"eigenvalue":enc(ev),"vector_ascending":[enc(x) for x in v]})
    return out
def encode_matrix(A):return [[enc(x) for x in r] for r in A]
def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=core.ARGS.workers) as ex:
        rows=dict(ex.map(fiber,range(2,10)))
    A4=operator(rows,"type4",[3*j for j in range(6)],range(2,8),(8,9))
    A5=operator(rows,"type5",[1+3*j for j in range(5)],range(2,7),(7,8,9))
    assert mm(A4,H4)==mm(H4,A4),"same full CM torus commutes with H4"
    assert mm(A5,H5)==mm(H5,A5),"same full CM torus commutes with H5"
    B4,R4,piv4=restriction(A4,PB4)
    B5,R5,piv5=restriction(A5,PB5)
    type5lines=[]
    for l in eigens(A5):
        vv=[(Q(x[0]),Q(x[1])) for x in l["vector_ascending"]]
        hv=mm(H5,[[x] for x in vv])
        ev=next((s for s in (W,OM2) if hv==[[mul(s,x)] for x in vv]),None)
        assert ev is not None
        l["whole_H_eigenvalue"]=enc(ev);type5lines.append(l)
    # True covariant derivative from -sigma^34*x^(1+3j)*y.
    C=[[Z]*5 for _ in range(6)]
    for j in range(5):
        a=1+3*j;C[j][j]=K(-2*a);C[j+1][j]=K(-2*a-3)
    ans={
      "format":"R798 exact canonical halfperiod and full S34 type4 CM13",
      "status":"PASS","field":"Q(omega), omega^2+omega+1=0",
      "input_producer_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
      "halfperiod_formula":"H=-1/2(I+epsilon sum_e(delta e)^-17 (x-e)^17 pull_x(e(x+2e)/(x-e)))",
      "halfperiod_common_sign":EPS,
      "absolute_halfperiod_anchor":"H(S)=omega^2 S as whole original source",
      "type4_basis":"sigma^34*x^(3j), j=0,...,5; b=1",
      "type4_fitting_fibers":list(range(2,8)),"additional_fibers":[8,9],
      "type4_CM13":encode_matrix(A4),"type4_H":encode_matrix(H4),
      "type4_B_projector":encode_matrix(PB4),
      "type4_characteristic_descending":[enc(x) for x in characteristic(A4)],
      "type4_mu6_lines":eigens(A4),
      "type4_B_rank":len(piv4),"type4_B_pivot_columns":piv4,
      "type4_B_basis":encode_matrix(B4),"type4_B_CM13":encode_matrix(R4),
      "type4_B_characteristic_descending":[enc(x) for x in characteristic(R4)],
      "type5_H":encode_matrix(H5),"type5_B_projector":encode_matrix(PB5),
      "type5_B_rank":len(piv5),"type5_B_basis":encode_matrix(B5),
      "type5_B_CM13":encode_matrix(R5),
      "type5_B_characteristic_descending":[enc(x) for x in characteristic(R5)],
      "type5_complete_mu6_lines":type5lines,
      "covariant_derivative_type5_to_type4":encode_matrix(C),
      "type4_eighteenth_power_identity":mpow(A4,18)==eye(6),
      "type5_eighteenth_power_identity":mpow(A5,18)==eye(5),
      "elapsed_seconds":time.time()-START,
      "scope":"Exact full operators. Does not identify an elliptic Schwartz vector from an eigenvalue or assert a negative-two unit moment nonzero. Actual qstar second source still uses the paid complete cd generator.",
      "outputs_persisted":False}
    print(json.dumps(ans,separators=(",",":")))
if __name__=="__main__":main()
