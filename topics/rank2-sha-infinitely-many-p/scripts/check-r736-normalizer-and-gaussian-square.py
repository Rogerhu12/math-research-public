#!/usr/bin/env python3
"""Fixed original normalizer and Gaussian-square tests; no varying-p scan."""
import hashlib, importlib.util, json, math, pathlib
path=pathlib.Path(__file__).with_name("check-r736-original-brandt-vector-and-full-first-wild.py")
spec=importlib.util.spec_from_file_location("r736_fixed",path)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
X,ix,f,reps,ranks,base=m.fixed_vector()

def right_j(x):
    # Right j normalizes each original local order.
    return m.canon(m.conj((x[0],x[1]),2)
                   +m.conj((x[2],x[3]),17)
                   +m.k3mul((x[4],x[5]),(0,1)))
jval=[f[ix[right_j(x)]] for x in X]
signs=[e for e in (1,-1) if all(jval[i]==e*f[i] for i in range(len(X)))]
assert len(signs)==1
M=102
dist={}
witness=[]
records=[]
for a in range(M):
    for b in range(M):
        n=a*a+b*b
        if math.gcd(n,102)!=1 or n%3!=2 or (a+b)%2!=1:
            continue
        q=(a,0,b,0)
        beta=m.qmul(q,q)
        value=f[ix[m.canon(m.act(m.qconj(beta),base))]]
        dist[str(value)]=dist.get(str(value),0)+1
        rec=[a,b,n%102,value,list(m.canon(m.act(m.qconj(beta),base)))]
        records.append(rec)
        if value%2 and len(witness)<12: witness.append(rec)
table=json.dumps(records,separators=(",",":")).encode()
print(json.dumps({"model_script_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                  "whole_right_j_eigenvalue":signs[0],
                  "Gaussian_modulus":M,
                  "Gaussian_square_value_distribution":dist,
                  "Gaussian_odd_witnesses":witness,
                  "Gaussian_records_sha256":hashlib.sha256(table).hexdigest(),
                  "Gaussian_record_count":len(records),
                  "fixed_Hecke_dimensions":ranks,
                  "prime_samples":0},sort_keys=True,separators=(",",":")))
