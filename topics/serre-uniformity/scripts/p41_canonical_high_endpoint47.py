#!/usr/bin/env python3
"""Actual canonical high-factor endpoint transport for the B Miller SLP."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def read(path):
    b=path.read_bytes()
    return json.loads(gzip.decompress(b) if path.suffix=='.gz' else b),hashlib.sha256(b).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--algebra',type=Path,default=Path('/tmp/p41_canonical_restriction47_candidate1_raw.json.gz'))
    p.add_argument('--low-points',type=Path,default=Path('/tmp/p41_canonical_low_points47_certificate.json.gz'))
    p.add_argument('--base',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    p.add_argument('--exponential',type=Path,default=Path('/tmp/p41_hecke3_exponential_checkpoint.json.gz'))
    p.add_argument('--endpoint',type=Path,default=Path('/tmp/p41_miller_endpoint47_certificate.json'))
    p.add_argument('--high-norms',type=Path)
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_canonical_high_endpoint47_certificate.json.gz'))
    args=p.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources
    from p41_formal47_multiply import write_checkpoint,point_hash
    from flint import fmpz_poly,nmod_poly
    sources,hashes=load_sources(args.script_dir/'data')
    data,asha=read(args.algebra);low,lsha=read(args.low_points)
    base,bsha=read(args.base);exp,xsha=read(args.exponential);endpoint,esha=read(args.endpoint)
    for o in [data,base,exp,endpoint]:assert o['source_sha256']==hashes
    assert low['canonical_algebra_sha256']==asha
    assert endpoint['input_sha256'][args.base.name]==bsha and endpoint['input_sha256'][args.exponential.name]==xsha
    old,oldsha=read(args.script_dir/'data/p41_formal47_multiplication_saved.json.gz')
    assert endpoint['input_sha256']['p41_formal47_multiplication_saved.json.gz']==oldsha
    Phi={j:r.from_json(data['Phi'+str(j)]) for j in [1,2]}
    H=low['high_factor_ascending'];HZ=fmpz_poly(H);Hp=nmod_poly([a%47 for a in H],47)
    assert Hp.degree()==102 and Hp.gcd(Hp.derivative()).degree()==0
    # Rational sections are actual functions s/f0^degree in this fixed algebra.
    def evaluate(label,cf,degree):
        pol=r.mm(Phi[degree],cf);assert not np.any(pol[1])
        aa=[int(x) for x in pol[0][:,0]]
        ap=nmod_poly([a%47 for a in aa],47)
        gcd=Hp.gcd(ap);value=int(HZ.resultant(fmpz_poly(aa)))%r.Q
        assert gcd.degree()==0 and value%47!=0
        return {'label':label,'polynomial_ascending_mod47four':aa,
                'actual_norm_mod47four':value,'common_factor_degree_mod47':0}
    trans=endpoint['transport_function']
    values={}
    for label,cf,d in [('new',trans['new_section_coefficients'],2),('old',trans['old_section_coefficients'],2),
                       ('v1',base['families'][0]['v_coefficients'],1)]:
        values[label]=evaluate(label,r.from_json(cf),d)
    gt=values['new']['actual_norm_mod47four']*pow(values['old']['actual_norm_mod47four']*values['v1']['actual_norm_mod47four']%r.Q,-1,r.Q)%r.Q
    # Prove the complete old/new effective ideals miss the high closed support,
    # rather than infer it merely from a divisor-class equality.
    def ideal_witness(label,K,A):
        rng=random.Random(4104716800+(0 if label=='old' else 1))
        running=Hp;used=[]
        for k in range(20):
            seed,c=r.rational_trace(A,rng);cf=r.mm(K,c)
            assert r.equal(r.mm(A,r.conjugate(c)),c)
            pol=r.mm(Phi[2],cf);assert not np.any(pol[1])
            aa=[int(x)%47 for x in pol[0][:,0]];running=running.gcd(nmod_poly(aa,47))
            used.append({'seed':r.to_json(seed),'section_polynomial_ascending_mod47':aa,'cumulative_gcd_degree':running.degree()})
            if running.degree()==0:break
        assert running.degree()==0
        return {'point_sha256':point_hash(K,A),'rational_ideal_sections':used,'complete_effective_support_disjoint':True}
    ideals={
        'old':ideal_witness('old',r.from_json(old['point_coordinates']),r.from_json(old['point_frobenius'])),
        'new':ideal_witness('new',r.from_json(exp['exponentials'][0]['point_coordinates']),r.from_json(exp['exponentials'][0]['point_frobenius']))
    }
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
            'input_sha256':{'algebra':asha,'low_points':lsha,'base':bsha,'exponential':xsha,'endpoint':esha,'old_final_point':oldsha},
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'degree':102,'high_polynomial_ascending':H,'transition_components':values,
            'actual_transition_norm_mod47four':gt,'actual_effective_ideal_witnesses':ideals,
            'transition_function':'g=(new/f0^2)/(old/f0^2)/(v1/f0), div(g)=A_new-A_old; F_new=F_old/g',
            'status':'actual canonical high-factor endpoint norm and complete ideal support checks PASS'}
    if args.high_norms:
        hi,hsha=read(args.high_norms)
        assert hi['source_sha256']==hashes and hi['canonical_algebra_sha256']==asha
        assert hi['bits_done']==304 and hi['all_actual_step_norms_units'] and not hi['missing_steps_1based']
        assert hi['available_steps']==454
        result['input_sha256']['complete_high_norms']=hsha
        result['complete_new_frame_norm_mod47four']=hi['cumulative_actual_norm_of_F_signed_n']*pow(gt,-1,r.Q)%r.Q
        result['status']='complete actual B Miller norm on canonical high102 factor, including exact formal endpoint transport'
    sha,size=write_checkpoint(args.output,result)
    print('ACTUAL HIGH CANONICAL ENDPOINT PASS',gt,'bytes',size,'sha',sha,flush=True)
    if 'complete_new_frame_norm_mod47four' in result:print('FINAL NORM',result['complete_new_frame_norm_mod47four'],flush=True)

if __name__=='__main__':main()

