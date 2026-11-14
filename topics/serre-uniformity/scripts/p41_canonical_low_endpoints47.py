#!/usr/bin/env python3
"""Actual whole-residue-disc endpoint divisors and Weierstrass factors at the actual canonical degree-one points."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--jets',type=Path,default=Path('/tmp/p41_canonical_low_jets47_raw.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_canonical_low_endpoints47_certificate.json.gz'))
    args=parser.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,replay_negative
    from p41_hecke3_hessian47 import section_jets
    from p41_weierstrass_unit47 import prepare_unit
    from p41_formal47_multiply import write_checkpoint
    sources,hashes=load_sources(args.script_dir/'data');M=make_model(sources)
    j,jsha=read(args.jets);assert j['source_sha256']==hashes
    W=[r.from_json([rec['normalized_weight2_coefficients'][k] for rec in j['records']]) for k in range(j['order']+1)]
    V2,V3=section_jets(W,sources,M,r)
    published,psha=read(args.script_dir/'data/p41_formal47_multiplication_saved.json.gz')
    exp,esha=read(Path('/tmp/p41_hecke3_exponential_checkpoint.json.gz'))
    transport,tsha=read(Path('/tmp/p41_miller_endpoint47_certificate.json'))
    assert published['source_sha256']==exp['source_sha256']==transport['source_sha256']==hashes
    neg,Aneg=replay_negative(M,sources[3])
    divisors={'initial_B_effective_divisor':M['B'],'negative_B_effective_divisor':neg,
              'old_final_Y_effective_divisor':r.from_json(published['point_coordinates']),
              'new_final_Y_effective_divisor':r.from_json(exp['exponentials'][0]['point_coordinates'])}
    records=[]
    for label,B in divisors.items():
        vals=[r.mm(v,B) for v in V2];rr=[]
        for n,point in enumerate(j['records']):
            degrees=[]
            for c in range(B[0].shape[1]):
                degrees.append(next((k for k,v in enumerate(vals) if r.units(r.rows(r.cols(v,[c]),[n]))[0,0]),None))
            candidates=[(e,c) for c,e in enumerate(degrees) if e is not None]
            assert candidates,'No effective divisor generator found to order16'
            e,c=min(candidates);coefficients=[[int(v[0][n,c]),int(v[1][n,c])] for v in vals]
            prepared=prepare_unit(coefficients,precision=4,degree=e)
            rr.append({'point_label':point['label'],'local_effective_degree':e,
                       'witness_section_column_1based':c+1,'weierstrass_coefficients':prepared['weierstrass_coefficients'],
                       'unit_constant_of_witness':prepared['unit_constant'],'required_last_jet':prepared['required_last_jet']})
        records.append({'divisor_label':label,'points':rr})
        print(label,'nonempty residue discs',[(a['point_label'],a['local_effective_degree']) for a in rr if a['local_effective_degree']],flush=True)
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
            'jet_source_sha256':jsha,'endpoint_sources_sha256':{'R121':psha,'R136':esha,'transition':tsha},
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'weierstrass_source_sha256':hashlib.sha256((args.script_dir/'p41_weierstrass_unit47.py').read_bytes()).hexdigest(),
            'records':records,'status':'actual effective-divisor ideals on complete closed residue discs; all nonempty endpoint factors retained; no support inferred merely from f0 being a unit'}
    sha,size=write_checkpoint(args.output,result);print('ACTUAL ENDPOINT DISC DIVISORS PASS',size,sha,flush=True)

if __name__=='__main__':main()
