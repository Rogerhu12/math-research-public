#!/usr/bin/env python3
"""Actual CM constants, canonical coarse jets and Chow--Heegner translation.

Requires the completed actual B_minus4 logarithm and actual T2/T3 matrices.
This is first-order abelian integration data, not a local-height function.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

Q=47**4


def trim(a):
    while a and a[-1]==0:a.pop()
    return a


def add(a,b,q):return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%q for i in range(max(len(a),len(b)))])
def neg(a,q):return trim([-x%q for x in a])
def mul(a,b,q):
    c=[0]*max(0,len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%q
    return trim(c)


def division(a,b,q):
    a=trim([x%q for x in a]);b=trim([x%q for x in b]);assert b
    quot=[0]*max(0,len(a)-len(b)+1);iv=pow(b[-1],-1,q)
    while a and len(a)>=len(b):
        k=len(a)-len(b);c=a[-1]*iv%q;quot[k]=c
        for j,x in enumerate(b):a[k+j]=(a[k+j]-c*x)%q
        trim(a)
    return trim(quot),a


def residue(a,f,q):return division(a,f,q)[1]


def inverse(a,f):
    r0,r1=([x%47 for x in f],residue(a,f,47));s0,s1=[],[1]
    while r1:
        d,remainder=division(r0,r1,47);r0,r1=r1,remainder
        s0,s1=s1,add(s0,neg(mul(d,s1,47),47),47)
    assert len(r0)==1
    g=residue([x*pow(r0[0],-1,47)%47 for x in s0],f,47)
    for _ in range(2):g=residue(mul(g,add([2],neg(residue(mul(a,g,Q),f,Q),Q),Q),Q),f,Q)
    assert residue(mul(a,g,Q),f,Q)==[1]
    return g


def chinese(fields,key):
    fs=[[x%Q for x in f['factor_descending'][::-1]] for f in fields];F=[1]
    for f in fs:F=mul(F,f,Q)
    out=[]
    for i,f in enumerate(fs):
        m=[1]
        for j,g in enumerate(fs):
            if j!=i:m=mul(m,g,Q)
        entry=fields[i];c=[x*pow(entry[key+'_denominator'],-1,Q)%Q for x in entry[key+'_numerator_descending'][::-1]]
        e=residue(mul(m,inverse(residue(m,f,Q),f),Q),F,Q)
        out=residue(add(out,mul(e,c,Q),Q),F,Q)
    for f,entry in zip(fs,fields):
        c=[x*pow(entry[key+'_denominator'],-1,Q)%Q for x in entry[key+'_numerator_descending'][::-1]]
        assert residue(out,f,Q)==residue(c,f,Q)
    return out


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--hecke',type=Path)
    parser.add_argument('--log',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    from p41_formal47_multiply import write_checkpoint
    names=['p41_cusp_divisors47_certificate.json.gz','p41_cm3_makdisi47_certificate.json','p41_jacobi_cm_certificate.json']
    raws=[(folder/'data'/n).read_bytes() for n in names]
    divs,cm,jacobi=[json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n,b in zip(names,raws)]
    hp=args.hecke or folder/'data'/'p41_hecke47_compact.json.gz';lp=args.log or folder/'data'/'p41_formal47_log_compact.json.gz'
    hr,lr=hp.read_bytes(),lp.read_bytes();hecke,log=json.loads(gzip.decompress(hr)),json.loads(gzip.decompress(lr))
    assert hecke['source_sha256']['p41_cusp_divisors47_certificate.json.gz']==hashlib.sha256(raws[0]).hexdigest()
    assert log['source_sha256']['p41_cusp_divisors47_certificate.json.gz']==hashlib.sha256(raws[0]).hexdigest()
    assert hecke['source_sha256']['p41_jacobi_cm_certificate.json']==hashlib.sha256(raws[2]).hexdigest()
    T2,T3=[r.from_json(hecke['operators'][str(ell)]['canonical_operator']) for ell in (2,3)]
    H=r.add(T2,tuple(2*x%Q for x in T3));z=r.from_json(log['log_of_B_minus4'])
    def scale(A,n):return tuple(x*(n%Q)%Q for x in A)
    def act(poly):
        out=r.zeros(1,54)
        for c in reversed(poly):out=r.add(r.mm(out,H),scale(z,c))
        return out
    polynomials={key:chinese(jacobi['fields'],key) for key in ('s8','r3','r7','xiG')}
    classes={key:act(poly) for key,poly in polynomials.items()}
    AK=r.from_json(divs['canonical_frobenius_matrix'])
    for value in classes.values():assert r.equal(r.mm(value,AK),r.conjugate(value))
    K1=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    # Coarse t=A^3, raw weight-two value=A^2 F(t).
    F=r.mm(r.from_json(cm['coarse_evaluation_coefficients']),K1)
    assert F[0].shape==(3,54)
    beta=[pow(18,-1,Q),-2*pow(243,-1,Q)%Q,8*pow(6561,-1,Q)%Q]
    omega=[]
    for n in range(3):
        value=r.zeros(1,54)
        for k in range(n+1):value=r.add(value,scale(r.rows(F,[n-k]),beta[k]))
        assert r.equal(r.mm(value,AK),r.conjugate(value))
        omega.append(value)
    ujet=[classes['r3']]+[scale(omega[n],20*pow(n+1,-1,Q)) for n in range(3)]
    # The Hecke orbit consists of actual rational points.  The test below is a
    # sufficient integral saturation certificate only when its rank is54.
    assert all(int(x)%47==0 for A in z for x in A.flat)
    orbit=r.zeros(54,54);v=tuple((x//47)%47 for x in z);H47=tuple(x%47 for x in H)
    for j in range(54):orbit[0][j],orbit[1][j]=v[0][0],v[1][0];v=r.mm(v,H47,47)
    rr,cc=r.rank_pivots(orbit)
    from verify_p41_makdisi47 import qdet
    orbit_determinant=qdet(r.to_json(orbit),47)
    assert (orbit_determinant!=(0,0))==(len(rr)==54)
    result={'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
            'source_sha256':{n:hashlib.sha256(b).hexdigest() for n,b in zip(names,raws)},
            'hecke_sha256':hashlib.sha256(hr).hexdigest(),'log_sha256':hashlib.sha256(lr).hexdigest(),
            'hecke_primitive':'T2+2T3','crt_polynomials_ascending_mod_q':polynomials,
            'class_logarithms':{k:r.to_json(v) for k,v in classes.items()},
            'class_meanings':{'s8':'B_minus8','r3':'20*P_minus3-D','r7':'20*P_minus7-D','xiG':'R89 actual translation for G=54*T2+8'},
            'coarse_parameter':'t=A^3 on y^2=x^3+A*x+1',
            'KS_factor':'3/(2*(4*t+27))','KS_coefficients':beta,
            'canonical_differential_coefficients':[r.to_json(v) for v in omega],
            'log_of_20z_minus_D_coefficients':[r.to_json(v) for v in ujet],
            'orbit_of_logB_divided47_mod47':r.to_json(orbit),
            'orbit_determinant_mod47':list(orbit_determinant),
            'orbit_rank_mod47':len(rr),'orbit_rank_rows_1based':[i+1 for i in rr],
            'orbit_rank_columns_1based':[i+1 for i in cc],
            'status':'actual abelian log constants,coarse CM jets and Chow--Heegner translation; no local height or QC root claim'}
    out=args.output or folder/'data'/'p41_cm3_logjets47_checkpoint.json.gz'
    digest,size=write_checkpoint(out,result)
    print('Actual CM3 differential jets and Hecke class logs PASS; orbit rank mod47',len(rr),flush=True)
    print('Saved',size,'bytes; SHA256',digest,flush=True)


if __name__=='__main__':main()
