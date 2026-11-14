#!/usr/bin/env python3
"""Actual effective representatives in precisely the new canonical-Hessian frame."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--hessian',type=Path,default=Path('/tmp/p41_hecke3_hessian47_checkpoint.json.gz'))
    parser.add_argument('--jets',type=Path,default=Path('/tmp/p41_source_cubic47_checkpoint.json.gz'))
    parser.add_argument('--bases',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_hecke3_exponential_checkpoint.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,flip
    from p41_formal47_exponential import build_base,construct_point
    from p41_formal47_multiply import write_checkpoint
    from p41_poincare_norms47 import quotient,determinant
    from p41_cm4_divisor47 import kernel
    from p41_formal47_chart import make_chart,evaluate_chart
    from verify_p41_formal47_exponential import move_away
    sources,hashes=load_sources(folder/'data');M=make_model(sources);M['_divs']=sources[1]
    hr=args.hessian.read_bytes();hessian=json.loads(gzip.decompress(hr));jr=args.jets.read_bytes();jets=json.loads(gzip.decompress(jr))
    derivative=r.from_json(jets['evaluation_coefficients'][1]);families=[[i-1 for i in f['points_1based']] for f in hessian['families']]
    rng=random.Random(4104714201)
    if args.bases.exists():
        base=json.loads(gzip.decompress(args.bases.read_bytes()));assert base['source_sha256']==hashes and base['hessian_sha256']==hashlib.sha256(hr).hexdigest()
    else:
        records=[];vs=[]
        for j,points in enumerate(families):
            for attempt in range(100):
                aux,v,rec=build_base(points,M,derivative,r,rng)
                if j:
                    K2=r.rows(r.mul(vs[0],M['W']),M['P2']);K3=r.rows(r.mul(vs[0],M['V2']),M['P3'])
                    Q2,r2=quotient(K2);Q3,r3=quotient(K3)
                    c=r.rows(r.mul(v,M['V2']),M['P3']);mu=r.cols(r.mm(Q3,c),[i-1 for i in r2['free_rows_1based']]);det=determinant(mu)
                    if det is None:continue
                    rec['disjointness_determinant']=det
                records.append(rec);vs.append(v);break
            else:raise RuntimeError('Could not choose disjoint bases in new fixed frame')
            print('New canonical-Hessian frame',j+1,'actual disjoint effective base PASS.',flush=True)
        base={'source_sha256':hashes,'hessian_sha256':hashlib.sha256(hr).hexdigest(),'jets_sha256':hashlib.sha256(jr).hexdigest(),
              'families':records,'status':'effective representatives of precisely the new Hessian frame; residual72-points cancel from its degree-zero divisors'}
        write_checkpoint(args.bases,base)
    lograw=(folder/'data/p41_formal47_log_compact.json.gz').read_bytes();log=json.loads(gzip.decompress(lograw));target=r.from_json(log['log_of_signed_multiple'])
    old=json.loads(gzip.decompress((folder/'data/p41_formal47_multiplication_saved.json.gz').read_bytes()))
    chart=make_chart(M,sources[0]);known,wit=evaluate_chart(r.from_json(old['point_coordinates']),r.from_json(old['point_frobenius']),M,chart,rng)
    results=[]
    for j,record in enumerate(base['families']):
        point,A,witness=construct_point(target,record,jets,sources[1],M,r,kernel)
        moved,Am,first=move_away(point,A,families[j],M,derivative,r,rng)
        back,Ab,second=flip(r.mm(M['V2'],moved),Am,M,rng,'New-frame representative move')
        actual,check=evaluate_chart(back,Ab,M,chart,rng);assert r.equal(actual,known)
        witness['full_PicChart_comparison']=True;results.append(witness)
        print('New Hessian frame',j+1,'all820x73 PicChart entries agree with published Y PASS.',flush=True)
    out={'source_sha256':hashes,'hessian_sha256':hashlib.sha256(hr).hexdigest(),'bases_sha256':hashlib.sha256(args.bases.read_bytes()).hexdigest(),
         'jets_sha256':hashlib.sha256(jr).hexdigest(),'log_sha256':hashlib.sha256(lograw).hexdigest(),'exponentials':results,
         'status':'same canonical-Hessian frame, both actual formal exponentials fully compared with published Y'}
    digest,size=write_checkpoint(args.output,out);print('New frame actual exponents',size,digest,flush=True)

if __name__=='__main__':main()
