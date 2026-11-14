#!/usr/bin/env python3
"""Standard-library check of actual Hecke class logs, coarse jets and regulator."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--certificate',type=Path)
    parser.add_argument('--hecke',type=Path)
    parser.add_argument('--log',type=Path)
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    from verify_p41_makdisi47 import qmatmul,qdet
    from verify_p41_cusp_divisors47 import kernel,conjugate
    q=47**4
    def read(path):
        b=path.read_bytes();return b,json.loads(gzip.decompress(b) if path.name.endswith('.gz') else b)
    raw,data=read(args.certificate or folder/'data/p41_cm3_logjets47_checkpoint.json.gz')
    hr,hecke=read(args.hecke or folder/'data/p41_hecke47_compact.json.gz')
    lr,log=read(args.log or folder/'data/p41_formal47_log_compact.json.gz')
    assert hashlib.sha256(hr).hexdigest()==data['hecke_sha256']
    assert hashlib.sha256(lr).hexdigest()==data['log_sha256']
    sources={}
    for name,digest in data['source_sha256'].items():
        b,x=read(folder/'data'/name);assert hashlib.sha256(b).hexdigest()==digest;sources[name]=x
    divs=sources['p41_cusp_divisors47_certificate.json.gz'];cm=sources['p41_cm3_makdisi47_certificate.json'];jacobi=sources['p41_jacobi_cm_certificate.json']
    T2,T3=[hecke['operators'][str(ell)]['canonical_operator'] for ell in (2,3)]
    H=[[[ (x+2*y)%q for x,y in zip(a,b)] for a,b in zip(row,other)] for row,other in zip(T2,T3)]
    z=log['log_of_B_minus4']
    def scale(A,n,mod=q):return [[[(n*a)%mod,(n*b)%mod] for a,b in row] for row in A]
    def add(A,B):return [[[(a+c)%q,(b+d)%q] for (a,b),(c,d) in zip(row,other)] for row,other in zip(A,B)]
    def reduce(poly,f):
        a=[x%q for x in poly];f=[x%q for x in f];n=len(f)-1
        while len(a)>n:
            c=a[-1];k=len(a)-len(f)
            for i,x in enumerate(f):a[k+i]=(a[k+i]-c*x)%q
            a.pop()
        return a+[0]*(n-len(a))
    for key,poly in data['crt_polynomials_ascending_mod_q'].items():
        for field in jacobi['fields']:
            target=[x*pow(field[key+'_denominator'],-1,q)%q for x in field[key+'_numerator_descending'][::-1]]
            assert reduce(poly,field['factor_descending'][::-1])==reduce(target,field['factor_descending'][::-1])
        value=[[[0,0] for _ in range(54)]]
        for c in reversed(poly):value=add(qmatmul(value,H,q),scale(z,c))
        assert value==data['class_logarithms'][key]
        assert qmatmul(value,divs['canonical_frobenius_matrix'],q)==conjugate(value,q)
    K=kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block'])
    F=qmatmul(cm['coarse_evaluation_coefficients'],K,q)
    # Coefficient comparison in (2*(4t+27))*beta(t)=3.
    beta=data['KS_coefficients'];assert 54*beta[0]%q==3
    assert all((54*beta[n]+8*beta[n-1])%q==0 for n in (1,2))
    omega=[]
    for n in range(3):
        v=[[[0,0] for _ in range(54)]]
        for j in range(n+1):v=add(v,scale([F[n-j]],beta[j]))
        assert v==data['canonical_differential_coefficients'][n]
        assert qmatmul(v,divs['canonical_frobenius_matrix'],q)==conjugate(v,q)
        omega.append(v)
    expected=[data['class_logarithms']['r3']]+[scale(v,20*pow(i+1,-1,q)) for i,v in enumerate(omega)]
    assert expected==data['log_of_20z_minus_D_coefficients']
    assert all(a%47==b%47==0 for a,b in z[0]);v=[[[a//47%47,b//47%47] for a,b in z[0]]]
    hp=scale(H,1,47);orbit=[]
    for _ in range(54):orbit.append(v[0]);v=qmatmul(v,hp,47)
    assert orbit==data['orbit_of_logB_divided47_mod47']
    det=qdet(orbit,47);assert list(det)==data['orbit_determinant_mod47']==[10,18]
    assert det!=(0,0) and data['orbit_rank_mod47']==54
    print('Independent exact CRT,class logs,all CM coefficients,KS factor,Frobenius and54x54 orbit PASS.',flush=True)
    print('Regulator determinant mod47 =',det,'; norm',(det[0]**2+det[1]**2)%47,flush=True)
    print('SHA256',hashlib.sha256(raw).hexdigest(),flush=True)


if __name__=='__main__':main()
