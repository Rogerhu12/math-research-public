#!/usr/bin/env python3
"""Recover the missing initial cubic-section SLP against the saved exact Miller hashes."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--reference',type=Path,default=Path('/tmp/p41_poincare_miller_jets47_before_slp_45bits.json.gz'))
    parser.add_argument('--checkpoint',type=Path,default=Path('/tmp/p41_poincare_miller_slp_prefix47_rolling.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,replay_negative
    from p41_formal47_multiply import write_checkpoint,restore_tuple,point_hash
    from p41_poincare_miller47 import addflip_with_section
    sources,hashes=load_sources(folder/'data');M=make_model(sources);minusB,AminusB=replay_negative(M,sources[3])
    raw=args.reference.read_bytes();reference=json.loads(gzip.decompress(raw))
    assert reference['source_sha256']==hashes
    rng=random.Random(4104711704);bits=bin(reference['target_multiplier'])[2:];limit=reference['bits_done']
    data={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
          'reference_sha256':hashlib.sha256(raw).hexdigest(),'target_bits':limit,'bits_done':1,'sign':1,
          'steps':[],'status':'missing initial actual cubic-section SLP being recovered against existing point and coefficient hashes'}
    K,A=M['B'],M['AB']
    if args.checkpoint.exists():
        data=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
        assert data['source_sha256']==hashes and data['reference_sha256']==hashlib.sha256(raw).hexdigest()
        K,A=r.from_json(data['point_coordinates']),r.from_json(data['point_frobenius'])
        assert point_hash(K,A)==data['point_sha256'];rng.setstate(restore_tuple(data['random_state']))
    def record(rec,f):
        old=reference['steps'][len(data['steps'])]
        assert all(rec[k]==old[k] for k in rec)
        coeff=r.to_json(f);digest=hashlib.sha256(json.dumps(coeff,separators=(',',':')).encode()).hexdigest()
        assert digest==old['principal_coefficient_sha256']
        rec.update({'principal_section_coefficients':coeff,'principal_coefficient_sha256':digest})
        data['steps'].append(rec)
    for n in range(data['bits_done'],limit):
        K,A,f,rec=addflip_with_section(K,A,K,A,M,rng,'SLP prefix double bit'+str(n+1),r,same=True)
        data['sign']*=-1;rec.update({'operation':'double','bit':n+1,'sign':data['sign']});record(rec,f)
        if bits[n]=='1':
            B0,AB0=(M['B'],M['AB']) if data['sign']==1 else (minusB,AminusB)
            K,A,f,rec=addflip_with_section(K,A,B0,AB0,M,rng,'SLP prefix add bit'+str(n+1),r)
            data['sign']*=-1;rec.update({'operation':'add','bit':n+1,'sign':data['sign']});record(rec,f)
        data['bits_done']=n+1;data['point_coordinates'],data['point_frobenius']=r.to_json(K),r.to_json(A)
        data['point_sha256']=point_hash(K,A);data['random_state']=rng.getstate()
        if (n+1)%5==0 or n+1==limit:
            if n+1==limit:
                assert data['point_sha256']==reference['point_sha256'] and len(data['steps'])==len(reference['steps'])
                data['status']='complete actual initial SLP recovered; every cubic coefficient hash and every true Jacobian point hash matches the saved Miller computation'
            digest,size=write_checkpoint(args.checkpoint,data)
            print('SLP PREFIX SAVED',n+1,'bits',len(data['steps']),'sections',size,digest,flush=True)
if __name__=='__main__':main()

