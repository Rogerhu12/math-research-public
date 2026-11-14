#!/usr/bin/env python3
"""Extract actual integral degree-one points from the canonical restriction algebra."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--algebra',type=Path,default=Path('/tmp/p41_canonical_restriction47_candidate1_raw.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_canonical_low_points47_certificate.json.gz'))
    args=p.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from p41_formal47_multiply import write_checkpoint
    raw=args.algebra.read_bytes();d=json.loads(gzip.decompress(raw))
    sources,hashes=load_sources(args.script_dir/'data');M=make_model(sources);assert d['source_sha256']==hashes
    H=d['minimal_polynomial_ascending'];Phi1=r.from_json(d['Phi1']);fc=r.from_json(d['denominator_coefficients'])
    divs=sources[1]
    K=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    gc=r.mm(K,r.from_json(d['canonical_coefficients']));uc=r.from_json(d['primitive_generator_coefficients'])
    def evaluate(poly,x,modulus):
        value=0
        for a in reversed(poly):value=(value*x+a)%modulus
        return value
    derivative=[(i+1)*H[i+1] for i in range(len(H)-1)]
    roots=[x for x in range(47) if evaluate(H,x,47)==0];records=[]
    for a in roots:
        root=a
        for _ in range(3):root=(root-evaluate(H,root,r.Q)*pow(evaluate(derivative,root,r.Q),-1,r.Q))%r.Q
        assert evaluate(H,root,r.Q)==0 and root%47==a
        W=r.zeros(1,73)
        for k in range(105,-1,-1):W=r.add(tuple(x*root%r.Q for x in W),r.rows(Phi1,[k]))
        assert r.equal(r.mm(W,fc),r.eye(1)) and r.iszero(r.mm(W,gc))
        target=r.zeros(1,1);target[0][0,0]=root;assert r.equal(r.mm(W,uc),target)
        assert r.equal(r.mm(W,M['A1']),r.conjugate(W))
        records.append({'label':'canonical1_root_'+str(a),'primitive_root_mod47':a,
                        'primitive_root_mod47four':root,'normalized_weight2_values':r.to_json(W)[0]})
    high=H[:];low=[1]
    for rec in records:
        root=rec['primitive_root_mod47four'];q=[0]*(len(high)-1)
        for i in range(len(q)-1,-1,-1):
            q[i]=high[i+1];high[i]=(high[i]+root*q[i])%r.Q
        assert high[0]==0;high=q
        new=[0]*(len(low)+1)
        for i,c in enumerate(low):new[i]=(new[i]-root*c)%r.Q;new[i+1]=(new[i+1]+c)%r.Q
        low=new
    product=[0]*(len(low)+len(high)-1)
    for i,a in enumerate(low):
        for k,b in enumerate(high):product[i+k]=(product[i+k]+a*b)%r.Q
    assert product==H
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
            'canonical_algebra_sha256':hashlib.sha256(raw).hexdigest(),
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'records':records,'low_factor_ascending':low,'high_factor_ascending':high,
            'high_degree':len(high)-1,'status':'actual degree-one integral canonical points by simple-root Hensel lifting; exact monic factorization and full Frobenius descent PASS'}
    sha,size=write_checkpoint(args.output,result)
    print('ACTUAL CANONICAL LOW POINTS',len(records),'roots',roots,'high degree',len(high)-1,'bytes',size,'sha',sha,flush=True)

if __name__=='__main__':main()
