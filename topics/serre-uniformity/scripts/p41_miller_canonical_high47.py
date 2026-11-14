#!/usr/bin/env python3
"""Actual SLP norms on the high-degree etale factor of a canonical restriction algebra; no division by47."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw)),hashlib.sha256(raw).hexdigest()

def valuation(value,cap=4):
    if not value:return cap
    answer=0
    while answer<cap and value%47==0:
        answer+=1;value//=47
    return answer

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--algebra',type=Path,default=Path('/tmp/p41_canonical_restriction47_candidate1_raw.json.gz'))
    parser.add_argument('--low-points',type=Path,default=Path('/tmp/p41_canonical_low_points47_certificate.json.gz'))
    parser.add_argument('--miller',type=Path,default=Path('/tmp/p41_poincare_miller_jets47_rolling.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_miller_canonical_high47_checkpoint.json.gz'))
    args=parser.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_formal47_multiply import write_checkpoint
    from flint import fmpz_poly,nmod_poly
    data,algebra_sha=read(args.algebra);slp,slp_sha=read(args.miller)
    sources,source_hashes=load_sources(args.script_dir/'data');M=make_model(sources)
    assert data['source_sha256']==slp['source_sha256']==source_hashes
    Phi2=r.from_json(data['Phi2']);Phi3=r.from_json(data['Phi3'])
    low,low_sha=read(args.low_points);assert low['canonical_algebra_sha256']==algebra_sha
    H=low['high_factor_ascending'];HZ=fmpz_poly(H);Hp=nmod_poly([a%47 for a in H],47)
    factors=[f for f,e in Hp.factor()[1]]
    assert data['etale_mod47'] and Hp.gcd(Hp.derivative()).degree()==0
    def evaluate(label,coefficients,degree):
        pol=r.mm(Phi3 if degree==3 else Phi2,coefficients)
        assert not np.any(pol[1]),'A rational section has nonrational coordinates'
        aa=[int(x) for x in pol[0][:,0]];ap=nmod_poly([a%47 for a in aa],47)
        gcd=Hp.gcd(ap)
        value=int(HZ.resultant(fmpz_poly(aa)))%r.Q
        common=[j+1 for j,f in enumerate(factors) if ap%f==0]
        assert sum(factors[j-1].degree() for j in common)==gcd.degree()
        assert (value%47!=0)==(gcd.degree()==0)
        return {'label':label,'polynomial_sha256':hashlib.sha256(json.dumps(aa,separators=(',',':')).encode()).hexdigest(),
                'actual_norm_mod47four':value,'norm_valuation_capped_at4':valuation(value),
                'common_factor_indices_1based':common,'common_factor_degree':gcd.degree()}
    cf=r.mm(M['B'],r.column(sources[3]['negative_flip_section_seeds_and_coefficients'][0][1]))
    negative=evaluate('negative_B_quadratic',cf,2)
    records=[];norm=1;sign=1;valid=negative['actual_norm_mod47four']%47!=0
    inverse_negative=pow(negative['actual_norm_mod47four'],-1,r.Q) if valid else None
    missing=[]
    for k,step in enumerate(slp['steps']):
        if 'principal_section_coefficients' not in step:
            missing.append(k+1);valid=False;continue
        coefficients=step['principal_section_coefficients']
        assert hashlib.sha256(json.dumps(coefficients,separators=(',',':')).encode()).hexdigest()==step['principal_coefficient_sha256']
        rec=evaluate('AddFlip_'+str(k+1),r.from_json(coefficients),3)
        rec.update({'step_index_1based':k+1,'principal_coefficient_sha256':step['principal_coefficient_sha256'],
                    'operation':step['operation'],'bit':step['bit'],'sign':step['sign']})
        n=rec['actual_norm_mod47four'];valid=valid and n%47!=0
        if valid:
            if step['operation']=='double':norm=pow(norm*norm%r.Q*n%r.Q,-1,r.Q)
            elif step['operation']=='add':norm=pow(norm*(1 if sign==1 else inverse_negative)%r.Q*n%r.Q,-1,r.Q)
            else:raise AssertionError('unknown actual SLP operation')
            rec['cumulative_actual_norm_of_F_signed_n']=norm
        sign=-sign;assert sign==step['sign']
        records.append(rec)
    bad=[rec['step_index_1based'] for rec in records if rec['common_factor_indices_1based']]
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':source_hashes,
            'canonical_algebra_sha256':algebra_sha,'miller_snapshot_sha256':slp_sha,
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'canonical_candidate':data['canonical_candidate'],'degree':len(H)-1,'low_point_certificate_sha256':low_sha,
            'factor_polynomials_ascending_mod47':[[int(a) for a in f.coeffs()] for f in factors],
            'factor_degrees_mod47':[f.degree() for f in factors],
            'bits_done':slp['bits_done'],'available_steps':len(records),'missing_steps_1based':missing,
            'negative_B':negative,'steps':records,'nonunit_steps_1based':bad,
            'all_actual_step_norms_units':valid,'cumulative_actual_norm_of_F_signed_n':norm if valid else None,
            'status':'actual finite-algebra resultant norms and exact mod47 collision factors; no division by47; nonunit chains are not claimed evaluated'}
    sha,size=write_checkpoint(args.output,result)
    print('ACTUAL HIGH CANONICAL SLP NORMS',len(records),'steps; factors',result['factor_degrees_mod47'],
          'nonunit steps',bad,'all units',valid,'bytes',size,'sha',sha,flush=True)

if __name__=='__main__':main()
