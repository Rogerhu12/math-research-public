#!/usr/bin/env python3
"""R761: exact projections of the original D_S, using the original R732 producer.
Run in public Actions. Recomputes full CM13 fibers; consumes no saved output.
Only a compact summary is printed; no generated files are written.
"""
from fractions import Fraction as Q
import hashlib, json, pathlib, subprocess, sys

def K(a=0,b=0): return (Q(a),Q(b))
ZERO=K(); ONE=K(1); W=K(0,1)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c=a[1]*b[1]
    return (a[0]*b[0]-c,a[0]*b[1]+a[1]*b[0]-c)
def inv(a):
    d=a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
    assert d
    return ((a[0]-a[1])/d,-a[1]/d)
def div(a,b):return mul(a,inv(b))
def total(v):
    a=ZERO
    for b in v:a=add(a,b)
    return a
def mv(A,v):return [total(mul(a,b) for a,b in zip(row,v)) for row in A]
def va(v,w):return [add(a,b) for a,b in zip(v,w)]
def vs(v,c):return [mul(a,c) for a in v]
def enc(v):return [[str(a),str(b)] for a,b in v]

base=pathlib.Path(__file__).with_name("check-r732-original-type-five-cm13.py")
out=subprocess.run([sys.executable,str(base),"--workers=4"],
                   stdout=subprocess.PIPE,check=True)
data=json.loads(out.stdout)
assert data["status"]=="PASS" and data["normalized_eighteenth_power_identity"]
A=[[K(*v) for v in row] for row in data["normalized_CM13_matrix"]]
ds=[K(Q(a,119)) for a in (-256,-400,-96,-583,98)]
a3=ds
for _ in range(3):a3=mv(A,a3)
p6=vs(va(a3,vs(ds,W)),inv(sub(W,ONE)))
w2=mul(W,W)
pminus=vs(va(mv(A,p6),vs(p6,w2)),inv(sub(w2,ONE)))
pomega=vs(va(mv(A,p6),p6),inv(sub(ONE,w2)))
pprim=va(ds,vs(p6,K(-1)))
vminus=[K(a) for a in (64,-104,-156,13,1)]
vomega=[K(Q(a,11)) for a in (128,368,120,-109,11)]
assert pminus==vs(vminus,pminus[-1])
assert pomega==vs(vomega,pomega[-1])
assert va(va(pminus,pomega),pprim)==ds
r3=pprim
for _ in range(3):r3=mv(A,r3)
assert va(r3,vs(pprim,W))==[ZERO]*5
assert any(a!=ZERO for a in pprim)
linear=total(mul(K(a),ds[j]) for a,j in ((429,4),(51,3),(7,2)))
assert linear==K(Q(11637,119))
print(json.dumps({
 "status":"PASS",
 "input":"D_S=zeta*S-S_prime/34, original b=1",
 "basis":"-sigma^34*x*y*X^j, j=0,...,4; b transport is R732",
 "R732_producer_sha256":hashlib.sha256(base.read_bytes()).hexdigest(),
 "D_S_ascending":enc(ds),
 "coefficient_D_minus":enc([pminus[-1]])[0],
 "coefficient_D_omega":enc([pomega[-1]])[0],
 "primitive_polynomial_ascending":enc(pprim),
 "primitive_z5_coefficient_nonzero":pprim[-1]!=ZERO,
 "both_original_rank_one_coefficients_nonzero":pminus[-1]!=ZERO and pomega[-1]!=ZERO,
 "first_three_annihilator_value":enc([linear])[0],
 "scope":"Full exact source projections only. No negative Mellin value is computed.",
 "outputs_persisted":False
},separators=(",",":")))
