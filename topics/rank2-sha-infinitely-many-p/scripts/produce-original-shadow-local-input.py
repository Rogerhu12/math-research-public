#!/usr/bin/env sage-python
"""Actual original r-adic input for the R881/R882 shadow consumer.

All exact coefficients come from the same fixed CM producer used in the
characteristic-zero P certificate and from E17.anlist for the original F.
This script certifies only formal input and precision.  Interpretation as
actual reduced modular maps still requires BOTH original char-zero PASS
receipts.  No coefficient output data file is written.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import argparse
import hashlib
import importlib.util
import json
import time
from pathlib import Path
from sage.all import (QQ, ZZ, GF, NumberField, Qq, PolynomialRing,
                      PowerSeriesRing, EllipticCurve, matrix, vector,
                      identity_matrix)
from sage.env import SAGE_VERSION
from original_good_prime_germ_tools import (
    original_P_good_prime_germ, original_F_good_prime_germ)

STARTED = time.monotonic()

def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=True)

def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()

def progress(stage,**kw):
    print("RANK2_SHADOW_LOCAL_STAGE "+canonical(dict(
        stage=stage,elapsed_seconds=time.monotonic()-STARTED,**kw)),flush=True)

def exact_original_P_input(maximum):
    dep = Path(__file__).with_name("check-r873-original-cm-petersson-degree.py")
    spec = importlib.util.spec_from_file_location("original_shadow_r873",str(dep))
    r873 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r873)
    K9,eigen,_,ideal_count,input_hash = r873.exact_coefficients(3*maximum+1)
    z9 = K9.gen()
    theta = z9**2+z9**(-2)
    ebase = [K9.one(),theta,theta**2-2]
    def coords9(z):
        co = K9(z).list()
        return vector(QQ,[co[i] if i<len(co) else 0 for i in range(6)])
    B9 = matrix(QQ,[coords9(z) for z in ebase]).transpose()
    chosen = tuple(B9.transpose().pivots())
    assert len(chosen)==3
    inverse = matrix(QQ,[[B9[i,j] for j in range(3)] for i in chosen]).inverse()
    Pa = PolynomialRing(QQ,"aa")
    F = NumberField(Pa.gen()**3-17,"a17")
    a = F.gen()
    lam = (68+7*a-13*a*a)/3
    vnew = (-34-17*a+11*a*a)/3
    v = -122465-47628*a-QQ(314892)/17*a*a
    assert lam.norm()==34 and lam**3*v==vnew
    lam_basis = [F.one(),-497+237*a-17*a*a,609-44*a-75*a*a]
    M1 = matrix(QQ,[[0,2,-1],[1,0,1],[0,1,0]])
    M2 = matrix(QQ,[[0,-1,2],[0,1,-1],[1,0,-1]])
    uc = vector(QQ,[QQ(915)/55569,QQ(1097)/55569,QQ(2962)/55569])
    Mu = uc[0]*identity_matrix(QQ,3)+uc[1]*M1+uc[2]*M2
    assert Mu*(106*identity_matrix(QQ,3)+59*M1+185*M2)==17*identity_matrix(QQ,3)
    ff = []
    for n in range(maximum+1):
        ev = coords9(eigen[3*n+1])
        ac = inverse*vector(QQ,[ev[i] for i in chosen])
        assert B9*ac==ev and all(x.denominator()==1 for x in ac)
        out = Mu*ac
        ff.append(sum((lam_basis[i]*out[i] for i in range(3)),F.zero())/lam)
    assert ff[0]==1 and ff[1]==-2
    # The proof of this support is part of the original source; keep it as a
    # direct exact check in the consumer input as well.
    assert all(eigen[n]==0 for n in range(1,len(eigen)) if n%3!=1)
    serial = []
    for z in ff:
        co=F(z).list()
        serial.append([str(QQ(co[i])) if i<len(co) else "0" for i in range(3)])
    return F,ff,lam,v,vnew,dict(
        exact_CM_input_sha256=input_hash,normalized_fP_sha256=digest(serial),
        ideal_count=ideal_count,maximum=maximum)

def evaluate_number_field(z,field,root):
    result = field.zero()
    for c in reversed(z.list()):
        result = result*root+field(QQ(c))
    return result

def finite_coordinates(z):
    co=z.polynomial().list()
    return [int(co[i]) if i<len(co) else 0 for i in range(2)]

def residue_hash(row):
    return digest([finite_coordinates(z) for z in row])

def euler_series(R,N,dilation=1):
    q=R.gen()
    out=R.one()
    j=1
    while dilation*j*(3*j-1)//2<N:
        a=dilation*j*(3*j-1)//2
        b=dilation*j*(3*j+1)//2
        sign=-1 if j%2 else 1
        out+=sign*q**a
        if b<N:
            out+=sign*q**b
        j+=1
    return out.add_bigoh(N)

def build_local_input(prime=29,p_maximum=1226,f_maximum=1428,
                      precision=64,packet_embeddings=(0,1,2)):
    prime,p_maximum,f_maximum,precision=map(int,
        (prime,p_maximum,f_maximum,precision))
    embeddings=tuple(int(i) for i in packet_embeddings)
    assert prime in (29,41) and precision==64
    assert 1<=p_maximum<=1226 and 1<=f_maximum<=1428
    assert embeddings and len(set(embeddings))==len(embeddings)
    assert all(i in (0,1,2) for i in embeddings)
    progress("exact original packet coefficients",maximum=p_maximum)
    F,ff,lam,v,vnew,cm_meta=exact_original_P_input(p_maximum)
    progress("exact original first factor coefficients",maximum=f_maximum)
    E17=EllipticCurve(QQ,[0,0,0,0,17])
    aa=E17.anlist(6*f_maximum+1)
    assert aa[1]==1 and aa[2]==aa[3]==aa[17]==0
    assert aa[7]==-5
    assert all(aa[n]==0 for n in range(1,len(aa)) if n%6!=1)
    fF=[ZZ(aa[6*n+1]) for n in range(f_maximum+1)]

    # Use an exact integral defining polynomial, never a polynomial known only
    # modulo r.  Eighty working digits leave the required 64 absolute digits
    # even for the established ell(v) expression at r=41.
    Pz=PolynomialRing(ZZ,"z")
    local=Qq(ZZ(prime)**2,prec=80,names="omega_local",
             modulus=Pz.gen()**2+Pz.gen()+1,type="capped-rel")
    om=local.gen()
    k=local.residue_field()
    ombar=om.residue()
    assert om**2+om+1==0 and ombar**2+ombar+1==0
    ar=pow(17,int(ZZ(3).inverse_mod(prime-1)),prime)
    a0=local(ar)
    for _ in range(8):
        a0=(2*a0+17/(a0*a0))/3
    assert (a0**3-17).valuation()>=80
    roots=tuple(a0*om**i for i in range(3))
    alpha=-1+2*om
    def ell_at(vv):
        return ((21905009-23122022*om)
           +(112353990182+54575060764*om)*vv
           +(305813+148546*om)*vv*vv)/25505280
    vs=tuple(evaluate_number_field(v,local,r) for r in roots)
    sigma_indices=[]
    for i,vv in enumerate(vs):
        target=alpha**3*vv/ell_at(vv)**3
        matches=[j for j,vj in enumerate(vs) if (target-vj).valuation()>=precision]
        assert len(matches)==1
        sigma_indices.append(matches[0])
    assert sorted(sigma_indices)==[0,1,2]
    assert all(sigma_indices[i]!=i and
               sigma_indices[sigma_indices[sigma_indices[i]]]==i for i in range(3))
    progress("fixed unramified embeddings",
             a_residue=[finite_coordinates(r.residue()) for r in roots],
             sigma_a_index=sigma_indices)

    packet={}
    packet_summaries=[]
    for i in embeddings:
        fp=[evaluate_number_field(z,local,roots[i]) for z in ff]
        vi=evaluate_number_field(vnew,local,roots[i])
        assert all(z.precision_absolute()>=precision and z.valuation()>=0 for z in fp)
        progress("R881 actual packet germ",embedding=i,maximum=p_maximum)
        qy,meta=original_P_good_prime_germ(
            local,prime,vi,fp,p_maximum,precision)
        residues=[z.residue() for z in qy]
        packet[i]={"QY":residues,"vnew":vi.residue(),
                   "a17":roots[i].residue(),
                   "lambda":evaluate_number_field(lam,local,roots[i]).residue(),
                   "v":vs[i].residue(),"metadata":meta}
        packet_summaries.append(dict(
            embedding=i,QY_sha256=residue_hash(residues),
            vnew=finite_coordinates(vi.residue()),
            original_a17=finite_coordinates(roots[i].residue()),
            **meta))
    if 0 in packet:
        assert all(z**prime==z for z in packet[0]["QY"])
    if 1 in packet and 2 in packet:
        assert [z**prime for z in packet[1]["QY"]]==packet[2]["QY"]

    progress("R881 actual first-factor germ",maximum=f_maximum)
    uu,first_meta=original_F_good_prime_germ(
        local,prime,[local(z) for z in fF],f_maximum,precision)
    ubar=[z.residue() for z in uu]
    assert all(z**prime==z for z in ubar)
    N=f_maximum+1
    PS=PowerSeriesRing(k,"Q",default_prec=N)
    eu=euler_series(PS,N)
    sig=[ZZ(0)]*N
    for d in range(1,N):
        for n in range(d,N,d):
            sig[n]+=d
    ss=[k.one()]+[k(12*sig[n]-(36*sig[n//3] if n%3==0 else 0))
                     for n in range(1,N)]
    S=PS(ss).add_bigoh(N)
    vform=(PS(ubar).add_bigoh(N)*eu**12/S**3).add_bigoh(N)
    vform_row=[vform[n] for n in range(N)]
    assert vform_row[0]==-1
    first_meta=dict(first_meta,U_sha256=residue_hash(ubar),
                    vF_sha256=residue_hash(vform_row))
    context={"prime":prime,"local_field":local,"constants":k,"omega":ombar,
             "a_roots":tuple(r.residue() for r in roots),
             "sigma_a_index":tuple(sigma_indices),
             "packet":packet,"first":{"U":ubar,"vF":vform_row,"metadata":first_meta},
             "cm_exact_field":F,"cm_exact_input":ff}
    result={
        "kind":"rank2_original_shadow_local_input",
        "status":"formal_input_and_precision_certified",
        "prime":prime,"packet_maximum":p_maximum,"first_maximum":f_maximum,
        "packet_embeddings":list(embeddings),"input_absolute_precision":precision,
        "working_relative_precision":80,"CM_input":cm_meta,
        "packet":packet_summaries,"first":first_meta,
        "fixed_residue_modulus":"omega^2+omega+1",
        "sigma_a_index":sigma_indices,
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID",os.environ.get("GITHUB_RUN_ID")),
        "sage_version":SAGE_VERSION,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds":time.monotonic()-STARTED,
        "scope":"Only the exact original coefficients and the R881 formal germs are certified. No original modular map or nonzero shadow is inferred without both original characteristic-zero PASS receipts."
    }
    return context,result

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument("--prime",type=int,choices=(29,41),default=29)
    pa.add_argument("--packet-maximum",type=int,default=1226)
    pa.add_argument("--first-maximum",type=int,default=1428)
    pa.add_argument("--packet-embeddings",default="0,1,2")
    ar=pa.parse_args()
    context,result=build_local_input(
        ar.prime,ar.packet_maximum,ar.first_maximum,64,
        tuple(int(i) for i in ar.packet_embeddings.split(",")))
    globals()["ORIGINAL_SHADOW_LOCAL_CONTEXT"]=context
    payload=canonical(result)
    print("RANK2_SHADOW_LOCAL_RESULT "+payload,flush=True)
    print("RANK2_SHADOW_LOCAL_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)

if __name__=="__main__":
    main()
