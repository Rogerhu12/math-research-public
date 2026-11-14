#!/usr/bin/env python3
"""Independent integer resultant checks on actual restriction-algebra records.

The finite-field matrix construction checks actual section identities using the
published bounded exact backend.  Norms use only Python integers below, with a
unit-pivot determinant fallback when the Euclidean resultant has nonunit leads.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

MOD=47**4


def add(a,b):return ((a[0]+b[0])%MOD,(a[1]+b[1])%MOD)
def neg(a):return (-a[0]%MOD,-a[1]%MOD)
def sub(a,b):return add(a,neg(b))
def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%MOD,(a[0]*b[1]+a[1]*b[0])%MOD)
def inv(a):
    c=pow((a[0]*a[0]+a[1]*a[1])%MOD,-1,MOD)
    return a[0]*c%MOD,-a[1]*c%MOD
def power(a,n):
    x=(1,0)
    while n:
        if n&1:x=mul(x,a)
        a=mul(a,a);n//=2
    return x
def trim(a):
    while a and a[-1]==(0,0):a.pop()
    return a


def integer_determinant(rows):
    a=[[tuple(map(int,x)) for x in row] for row in rows]
    n=len(a);value=(1,0)
    assert all(len(row)==n for row in a)
    for k in range(n):
        pivot=next((i for i in range(k,n) if (a[i][k][0]**2+a[i][k][1]**2)%47),None)
        assert pivot is not None,('nonunit determinant',k)
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];value=neg(value)
        value=mul(value,a[k][k]);iv=inv(a[k][k])
        normalized=[mul(x,iv) for x in a[k][k+1:]]
        for i in range(k+1,n):
            c=a[i][k]
            a[i][k+1:]=[sub(x,mul(c,y)) for x,y in zip(a[i][k+1:],normalized)]
    return value


def polynomial_norm(m,a):
    relation=[tuple(map(int,x)) for x in m]
    original=[tuple(map(int,x)) for x in a]
    A=trim(relation.copy());B=trim(original.copy());value=(1,0)
    try:
        while B:
            n=len(B)-1;mdeg=len(A)-1
            if n==0:return mul(value,power(B[0],mdeg))
            ib=inv(B[-1]);R=A.copy()
            while len(R)>=len(B):
                c=mul(R[-1],ib);offset=len(R)-len(B)
                for j in range(len(B)):R[offset+j]=sub(R[offset+j],mul(c,B[j]))
                trim(R)
            if not R:return (0,0)
            k=len(R)-1
            if mdeg*n%2:value=neg(value)
            value=mul(value,power(B[-1],mdeg-k))
            A,B=B,R
        return (0,0)
    except ValueError:
        print('Independent integer unit-matrix fallback for nonunit Euclidean lead.',flush=True)
        d=len(relation)-1
        col=original+[(0,0)]*(d-len(original));columns=[]
        for j in range(d):
            columns.append(col)
            top=col[-1];shifted=[(0,0)]+col[:-1]
            col=[sub(x,mul(top,y)) for x,y in zip(shifted,relation[:-1])]
        return integer_determinant([[columns[j][i] for j in range(d)] for i in range(d)])


def verify_one(label,K,rec,alg,M,sources,r):
    from p41_poincare_norms47 import quotient_from_record
    Q2=quotient_from_record(rec['quotient2']);Q3=quotient_from_record(rec['quotient3'])
    pairs=rec['product_pairs_1based']
    S=r.mm(M['V2'],K)
    products=r.mul(r.cols(M['W'],[a-1 for a,b in pairs]),r.cols(S,[b-1 for a,b in pairs]))
    U=r.from_json(rec['product_coordinate_matrix'])
    assert r.equal(r.mm(M['V3'],U),products)
    for basis,Q,record in [(K,Q2,rec['quotient2']),(U,Q3,rec['quotient3'])]:
        pp=[i-1 for i in record['pivot_rows_1based']]
        invmatrix=r.from_json(record['kernel_basis_inverse'])
        assert r.equal(r.mm(r.rows(basis,pp),invmatrix),r.eye(len(pp)))
        assert r.iszero(r.mm(Q,basis))
    free2=[i-1 for i in rec['quotient2']['free_rows_1based']]
    def action(coeff):
        section=r.mm(M['W'],r.column(coeff));values=r.mul(section,M['V2'])
        coordinates=r.rows(values,M['P3'])
        assert r.equal(r.mm(M['V3'],coordinates),values)
        return r.cols(r.mm(Q3,coordinates),free2)
    Fc=action(alg['comparison_numerator_coefficients']);Fv=action(alg['denominator_coefficients'])
    nc=integer_determinant(r.to_json(Fc));nv=integer_determinant(r.to_json(Fv))
    assert list(nc)==rec['numerator_determinant'] and list(nv)==rec['denominator_determinant']
    assert list(mul(nc,inv(nv)))==rec['norm']
    Fvi=r.inverse_matrix(Fv);Mg=r.mm(Fvi,action(alg['generator_coefficients']))
    v=r.mm(M['W'],r.column(alg['denominator_coefficients']))
    current=r.mm(Q2,r.rows(r.mul(v,v),M['P2']))
    krylov=r.zeros(126,126)
    for j in range(126):
        krylov[0][:,j],krylov[1][:,j]=current[0][:,0],current[1][:,0]
        current=r.mm(Mg,current)
    Ki=r.from_json(alg['krylov_inverse'])
    assert r.equal(r.mm(Ki,krylov),r.eye(126))
    last=r.mm(Ki,current)
    relation=alg['minimal_polynomial_ascending']
    assert relation[-1]==[1,0]
    assert relation[:-1]==[[int(-last[0][i,0])%MOD,int(-last[1][i,0])%MOD] for i in range(126)]
    Phi2=r.mm(Ki,Q2);Phi3=r.mm(r.mm(Ki,Fvi),Q3)
    Phi1=r.mm(Phi2,r.rows(r.mul(v,M['W']),M['P2']))
    def norm(Phi,coeff):
        values=r.mm(Phi,r.column(coeff))
        pairs=[[int(values[0][i,0]),int(values[1][i,0])] for i in range(126)]
        return polynomial_norm(relation,pairs)
    assert list(norm(Phi1,alg['comparison_numerator_coefficients']))==rec['norm']
    print(label,'actual quotient, monogenic algebra, and independent norm PASS.',flush=True)
    return Phi1,Phi2,Phi3,norm


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--inverse',action='store_true')
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,replay_negative
    from p41_cm4_divisor47 import kernel
    sources,hashes=load_sources(folder/'data');M=make_model(sources);minus,_=replay_negative(M,sources[3])
    raw=(folder/'data'/'p41_poincare_norms47_checkpoint.json.gz').read_bytes();norms=json.loads(gzip.decompress(raw))
    araw=(folder/'data'/'p41_poincare_algebras47_checkpoint.json.gz').read_bytes();algs=json.loads(gzip.decompress(araw))
    assert norms['source_sha256']==algs['source_sha256']==hashes
    assert algs['norm_source_sha256']==hashlib.sha256(raw).hexdigest()
    divs=sources[1];K1=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    fc=r.mm(K1,r.column(divs['canonical_coefficients']));f=r.mm(M['W'],fc)
    D0=r.rows(r.mul(f,M['W']),M['P2'])
    verified={}
    for label,K in [('D0',D0),('E_B',M['B']),('E_minusB',minus)]:
        A=verify_one(label,K,norms['divisors'][label],algs['divisors'][label],M,sources,r);verified[label]=A
        assert list(A[3](A[2],algs['cubic_section_coefficients']))==algs['cubic_norms'][label]
    A=verified['E_minusB']
    assert list(A[3](A[1],algs['quadratic_section_coefficients']))==[1412636,0]
    print('All independent restriction algebras and actual quadratic/cubic norms PASS.',flush=True)
    print('SHA256',hashlib.sha256(araw).hexdigest(),flush=True)
    if args.inverse:
        iraw=(folder/'data'/'p41_poincare_inverse47_checkpoint.json.gz').read_bytes()
        inverse=json.loads(gzip.decompress(iraw))
        assert inverse['source_sha256']==hashes
        assert inverse['norm_source_sha256']==hashlib.sha256(raw).hexdigest()
        vc=r.column(sources[3]['norm_section_seeds_and_coefficients'][1][1])
        v=r.mm(M['W'],vc);Dv=r.rows(r.mul(v,M['W']),M['P2'])
        AM=verify_one('E_minus inverse',minus,norms['divisors']['E_minusB'],inverse['E_minusB_algebra'],M,sources,r)
        AV=verify_one('D_v inverse',Dv,inverse['D_v_norm_data'],inverse['D_v_algebra'],M,sources,r)
        sc,tc=[r.mm(M['B'],r.column(c)) for seed,c in sources[3]['negative_flip_section_seeds_and_coefficients']]
        k=inverse['pencil_coefficient']
        ac=r.add(tc,tuple(k*x%MOD for x in sc))
        nf=AM[3](AM[0],[[int(fc[0][j,0]),int(fc[1][j,0])] for j in range(73)])
        av=[[int(ac[0][j,0]),int(ac[1][j,0])] for j in range(199)]
        nm=AM[3](AM[1],av);nv=AV[3](AV[1],av)
        assert list(nf)==inverse['norm_f_over_v_on_E_minusB']==[2436042,0]
        assert list(nm)==inverse['norm_a_over_v_squared_on_E_minusB']==[1412636,0]
        assert list(nv)==inverse['norm_a_over_f_squared_on_D_v']==[1311028,0]
        inverse_scalar=mul(mul(nv,mul(nf,nf)),inv(nm))
        assert inverse_scalar==(inverse['left_inverse_torus_scalar'],0)==(149764,0)
        assert inverse_scalar[0]*inverse['psi_on_second_divisor']%MOD==1
        s=r.mm(M['V2'],sc);a=r.mm(M['V2'],ac)
        scaled=r.mul(r.mul(s,r.inverse_values(a)),M['V2'])
        R=r.sub(scaled,r.mm(M['V2'],r.rows(scaled,M['P2'])))
        rr=[i-1 for i in inverse['inverse_effective_divisor_rank_rows_1based']]
        cc=[i-1 for i in inverse['inverse_effective_divisor_rank_columns_1based']]
        Ka=r.from_json(kernel(199,inverse['inverse_effective_divisor_rank_columns_1based'],
              inverse['inverse_effective_divisor_free_columns_1based'],inverse['inverse_effective_divisor_kernel_block']))
        assert len(rr)==len(cc)==126
        r.inverse_matrix(r.cols(r.rows(R,rr),cc))
        assert r.iszero(r.mm(R,Ka))
        Aa=r.from_json(inverse['inverse_effective_divisor_frobenius'])
        assert r.equal(r.mm(Ka,Aa),r.mm(M['A2'],r.conjugate(Ka)))
        assert r.equal(r.mm(Aa,r.conjugate(Aa)),r.eye(73))
        w=(pow(inverse_scalar[0],46,MOD)-1)%MOD
        logarithm=(w-w*w*pow(2,-1,MOD)+w**3*pow(3,-1,MOD))*pow(46,-1,MOD)%MOD
        assert logarithm==inverse['log_of_inverse_torus_scalar']==4140042
        print('Actual nonzero Poincare left inverse: independent norms, full ideal and descent PASS.',flush=True)
        print('Inverse SHA256',hashlib.sha256(iraw).hexdigest(),flush=True)


if __name__=='__main__':main()
