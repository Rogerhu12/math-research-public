#!/usr/bin/env python3
"""Actual endpoint divisor change for the ongoing first-variable Miller transport."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_miller_endpoint47_certificate.json'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_poincare_miller47 import prepare_evaluation,final_frame_transfer
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    paths=[Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'),Path('/tmp/p41_hecke3_exponential_checkpoint.json.gz'),
           Path('/tmp/p41_source_cubic47_checkpoint.json.gz'),folder/'data/p41_formal47_multiplication_saved.json.gz']
    raws=[p.read_bytes() for p in paths];base,exp,jets,published=[json.loads(gzip.decompress(b)) for b in raws]
    norm,*_=prepare_evaluation(M,sources,base,exp,jets,r)
    K,A=r.from_json(published['point_coordinates']),r.from_json(published['point_frobenius'])
    newK,newA=r.from_json(exp['exponentials'][0]['point_coordinates']),r.from_json(exp['exponentials'][0]['point_frobenius'])
    value,record=final_frame_transfer(K,A,newK,newA,base,M,random.Random(4104714601),r,norm)
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
            'input_sha256':{p.name:hashlib.sha256(b).hexdigest() for p,b in zip(paths,raws)},
            'transport_function':record,'actual_transition_norm':value,
            'status':'actual endpoint divisor isomorphism A_new=A_old+div(g) and degree-zero norm g(A2(Y)); no completed Miller scalar claimed'}
    raw=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode();args.output.write_bytes(raw)
    print('ACTUAL ENDPOINT TRANSITION',value,'bytes',len(raw),'sha',hashlib.sha256(raw).hexdigest(),flush=True)

if __name__=='__main__':main()
