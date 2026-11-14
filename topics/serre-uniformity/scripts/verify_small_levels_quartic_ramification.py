#!/usr/bin/env python3
"""R98: complete Thue certificate when no new order-four inertia occurs.

Every normal invocation reruns every irreducible Thue equation with
PARI thueinit(P,1).  Python arithmetic uses only the standard library.
No bounded search is used to assert completeness of the integer solutions.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from math import isqrt
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE=Path(__file__).resolve().parent
LEVELS=(47,59,83)
SPLIT_GENERATORS={59:(3,5),83:(9,1)}

def qmul(a,b,m):
    return (a[0]*b[0]+m*a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def qpow(a,n,m):
    out=(1,0)
    for _ in range(n): out=qmul(out,a,m)
    return out

def cube_root(n):
    sign=-1 if n<0 else 1
    n=abs(n); low,high=0,1
    while high**3<n: high*=2
    while low<high:
        mid=(low+high)//2
        if mid**3<n: low=mid+1
        else: high=mid
    assert low**3==n
    return sign*low

def prime(q):
    return q>=2 and all(q%d for d in range(2,isqrt(q)+1))

def actual_trace(j,q):
    assert prime(q) and q>3 and j*(j-1728)%q!=0
    inverse=pow((j-1728)%q,-1,q)
    a4,a6=-36*inverse%q,-inverse%q
    characters=[]
    for x in range(q):
        discriminant=(x*x+4*(x**3+a4*x+a6))%q
        characters.append(0 if discriminant==0 else
                          (1 if pow(discriminant,(q-1)//2,q)==1 else -1))
    trace=-sum(characters)
    assert trace*trace<=4*q
    return {"q":q,"j_mod_q":j%q,"a4":a4,"a6":a6,
            "quadratic_characters":characters,"trace":trace}

def thue_cases():
    cases=[]; omitted=[]
    params=[(6,a,b,r) for a in (1,2) for b in (0,1) for r in (1,2)]
    params += [(9,0,b,r) for b in (1,2) for r in (1,2)]
    for p in LEVELS:
        for c,a,b,r in params:
            d,bp=2**a*3**b*p**r,(b-1)%3
            D0=2**a*3**bp*p**r
            common={"p":p,"c":c,"a":a,"b":b,"r":r,"d":d,"D0":D0}
            if pow(-2%p,(p-1)//2,p)==p-1:
                assert p==47 and 24%p
                omitted.append({**common,"m":-2,
                    "reason":"p inert in Q(sqrt(-2)); p|Norm(gamma) forces p|24"})
            else:
                assert p in SPLIT_GENERATORS
                pp=SPLIT_GENERATORS[p]
                assert pp[0]**2+2*pp[1]**2==p
                for k1,k2 in itertools.product(range(3),repeat=2):
                    if (k1+k2-bp)%3: continue
                    delta=qmul(qpow((0,1),a,-2),qpow(pp,r,-2),-2)
                    delta=qmul(delta,qpow((1,1),k1,-2),-2)
                    delta=qmul(delta,qpow((1,-1),k2,-2),-2)
                    n=delta[0]**2+2*delta[1]**2
                    assert n%D0==0
                    w=cube_root(n//D0)
                    s,t=delta
                    coefficients=[s,-6*t,-6*s,4*t]
                    assert s
                    cases.append({**common,"id":len(cases)+1,"m":-2,
                        "delta":list(delta),"three_exponents":[k1,k2],
                        "norm_multiplier":w,"polynomial_desc":coefficients,"rhs":24})
            for i1,i2 in itertools.product(range(3),repeat=2):
                if (i1+i2-a)%3: continue
                for k1,k2 in itertools.product(range(3),repeat=2):
                    if (k1+k2-bp)%3: continue
                    d1,d2=2**i1*3**k1*p**r,2**i2*3**k2
                    assert d1*d2%D0==0
                    w=cube_root(d1*d2//D0)
                    cases.append({**common,"id":len(cases)+1,"m":1,
                        "delta":[d1,d2],"two_exponents":[i1,i2],
                        "three_exponents":[k1,k2],"norm_multiplier":w,
                        "polynomial_desc":[d1,0,0,d2],"rhs":48})
    assert len(cases)==396 and len(omitted)==12
    assert {p:sum(row["p"]==p for row in cases) for p in LEVELS}=={47:108,59:144,83:144}
    return cases,omitted

def solve(gp,cases):
    with tempfile.TemporaryDirectory(prefix="serre-r98-thue-") as directory:
        folder=Path(directory)
        inputs,outputs=folder/"input.gp",folder/"output.jsonl"
        inputs.write_text(json.dumps([[row["polynomial_desc"],row["rhs"]]
                                     for row in cases])+"\n")
        source=HERE/"small_levels_quartic_ramification_thue.gp"
        command=(f"read({json.dumps(str(source))});\n"
                 f"small_levels_quartic_ramification_thue({json.dumps(str(inputs))},"
                 f"{json.dumps(str(outputs))});\nquit;\n")
        proc=subprocess.run([gp,"-q","-f","-s","268435456"],input=command,
                            text=True,capture_output=True,timeout=240,check=True)
        if "***" in proc.stderr or "all 396 Thue equations" not in proc.stdout:
            raise RuntimeError(proc.stderr+"\n"+proc.stdout)
        print(proc.stdout.strip(),flush=True)
        answers=[json.loads(line) for line in outputs.read_text().splitlines()]
    assert len(answers)==len(cases)
    for row,(identifier,solutions) in zip(cases,answers):
        assert row["id"]==identifier
        assert len({tuple(s) for s in solutions})==len(solutions)
        row["solutions"]=sorted(solutions)
    return cases

def recover(cases):
    recovered=[]; levels=[]
    for p in LEVELS:
        by_j={0:[]}
        for case in cases:
            if case["p"]!=p: continue
            co=case["polynomial_desc"]
            for u,v in case["solutions"]:
                assert co[0]*u**3+co[1]*u*u*v+co[2]*u*v*v+co[3]*v**3==case["rhs"]
                m=case["m"]; s,t=case["delta"]; w=case["norm_multiplier"]
                if m==1:
                    z=w*u*v
                    assert (s*u**3-t*v**3)%2==0
                    y=(s*u**3-t*v**3)//2
                else:
                    real,imag=u**3+3*m*u*v*v,3*u*u*v+m*v**3
                    assert s*real+m*t*imag==24
                    y,z=s*imag+t*real,w*(u*u-m*v*v)
                x=3*z if case["b"]==0 else z
                j=case["d"]*x**3
                assert j-1728==-3*m*y*y and j%p==0
                recovered.append({"case_id":case["id"],"p":p,"solution":[u,v],
                                  "x":x,"y":y,"j":j})
                by_j.setdefault(j,[]).append(case["id"])
        excluded=[]; left=[]
        for j,ids in sorted(by_j.items()):
            if j in (0,1728):
                left.append(j); continue
            witness=None
            for q in range(5,1000):
                if not prime(q) or q==p or q%3!=2 or j*(j-1728)%q==0: continue
                trace=actual_trace(j,q)
                if trace["trace"]%p:
                    witness={"j":j,"case_ids":ids,**trace}; break
            if witness is None: left.append(j)
            else: excluded.append(witness)
        levels.append({"p":p,"distinct_j":sorted(by_j),
                       "inert_frobenius_exclusions":excluded,"unexcluded_j":left})
    return recovered,levels

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    parser.add_argument("--gp",default=shutil.which("gp") or "/tmp/pari-2.19.0/gp")
    args=parser.parse_args()
    cases,omitted=thue_cases()
    cases=solve(args.gp,cases)
    recovered,levels=recover(cases)
    result={"result":"R98","levels":list(LEVELS),"unconditional_thueinit_flag":1,
            "reference_pari_version":"2.19.0","omitted_inert_parameter_branches":omitted,
            "thue_cases":cases,"recovered_solutions":recovered,"level_results":levels,
            "zero_j_is_explicitly_retained":True}
    payload=(json.dumps(result,indent=2)+"\n").encode()
    output=HERE/"data"/"small_levels_quartic_ramification.json"
    if args.write: output.write_bytes(payload)
    else: assert output.read_bytes()==payload
    print("Recovered integer solutions:",len(recovered))
    for row in levels:
        print("p",row["p"],"j count",len(row["distinct_j"]),"unexcluded",row["unexcluded_j"])
    print("SHA256",hashlib.sha256(payload).hexdigest())

if __name__=="__main__":
    main()
