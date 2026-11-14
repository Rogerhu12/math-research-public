#!/usr/bin/env python3
"""Replay a completed CM SLP against the true formal Y, keeping all54 local connection jets."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def read(path):
    b=path.read_bytes();return json.loads(gzip.decompress(b)),hashlib.sha256(b).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--discriminant',type=int,choices=[7,12],required=True)
    p.add_argument('--miller',type=Path);p.add_argument('--endpoint',type=Path)
    p.add_argument('--bases',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    p.add_argument('--jets',type=Path,default=Path('/tmp/p41_source_cubic47_checkpoint.json.gz'))
    p.add_argument('--B-endpoints',type=Path,default=Path('/tmp/p41_hecke3_exponential_checkpoint.json.gz'))
    p.add_argument('--cm-endpoints',type=Path,default=Path('/tmp/p41_cm_formal_endpoints47_checkpoint.json.gz'))
    p.add_argument('--mixed-height',type=Path,default=Path('/tmp/p41_cm_mixed_formal_height47_checkpoint.json.gz'))
    p.add_argument('--hessian',type=Path,default=Path('/tmp/p41_hecke3_hessian47_compact.json.gz'))
    p.add_argument('--output',type=Path);args=p.parse_args()
    folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_poincare_miller47 import prepare_evaluation,log_pair
    from p41_poincare_miller_jets47 import jet_evaluator,evaluate_jet
    from p41_poincare_norms47 import pair_mul,pair_inverse
    from p41_formal47_multiply import write_checkpoint
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    cp=args.miller or Path('/tmp/p41_cm'+str(args.discriminant)+'_slp47_rolling.json.gz')
    ep=args.endpoint or Path('/tmp/p41_cm'+str(args.discriminant)+'_endpoint47_certificate.json.gz')
    paths=[cp,ep,args.bases,args.jets,args.B_endpoints,args.cm_endpoints,args.mixed_height,args.hessian]
    pairs=[read(p) for p in paths]
    slp,endpoint,base,jets,Bexp,CMexp,mixed,hessian=[d for d,h in pairs]
    ih={p.name:h for p,(d,h) in zip(paths,pairs)}
    for d in [slp,endpoint,base,Bexp,CMexp,mixed,hessian]:assert d['source_sha256']==hashes
    assert slp['bits_done']==304 and slp['sign']==1 and len(slp['steps'])==454
    assert endpoint['input_sha256']['miller']==ih[cp.name]
    assert endpoint['input_sha256']['formal_endpoints']==ih[args.cm_endpoints.name]
    assert mixed['input_sha256'][args.cm_endpoints.name]==ih[args.cm_endpoints.name]
    assert mixed['input_sha256'][args.B_endpoints.name]==ih[args.B_endpoints.name]
    local=next(a for a in mixed['records'] if a['discriminant']==-args.discriminant)
    target=CMexp['targets']['x'+str(args.discriminant)]['targets']['m']['exponentials'][0]
    assert local['positive_formal_point_sha256']==target['point_sha256']==endpoint['new_formal_point_sha256']
    norm,*_=prepare_evaluation(M,sources,base,Bexp,jets,r);normjet,Omega=jet_evaluator(M,sources,base,jets,r)
    del jets,pairs
    parameters=Bexp['exponentials'][1]['parameters']
    negcf=r.from_json(slp['negative_quadratic_coefficients'])
    uminus=pair_inverse(norm(negcf,2));jminus=r.neg(normjet(negcf,2))
    assert evaluate_jet(jminus,parameters,r)==log_pair(uminus,r)
    u=[1,0];J=r.zeros(54,3);sign=1;records=[]
    for k,step in enumerate(slp['steps']):
        cf=step['principal_section_coefficients']
        assert hashlib.sha256(json.dumps(cf,separators=(',',':')).encode()).hexdigest()==step['principal_coefficient_sha256']
        c=r.from_json(cf);nf,nj=norm(c,3),normjet(c,3)
        if step['operation']=='double':
            u=pair_inverse(pair_mul(pair_mul(u,u),nf));J=r.neg(r.add(tuple(2*x%r.Q for x in J),nj))
        else:
            assert step['operation']=='add'
            uq,jq=([1,0],r.zeros(54,3)) if sign==1 else (uminus,jminus)
            u=pair_inverse(pair_mul(pair_mul(u,uq),nf));J=r.neg(r.add(r.add(J,jq),nj))
        sign=-sign;assert sign==step['sign']
        assert evaluate_jet(nj,parameters,r)==log_pair(nf,r)
        assert evaluate_jet(J,parameters,r)==log_pair(u,r)
        records.append({'step_index_1based':k+1,'principal_coefficient_sha256':step['principal_coefficient_sha256'],
                        'principal_norm':nf,'coordinate':u,'norm_jet_sha256':hashlib.sha256(json.dumps(r.to_json(nj),separators=(',',':')).encode()).hexdigest()})
    assert sign==1;m=slp['target_multiplier'];tr=endpoint['transport']
    v1=r.from_json(tr['v1_coefficients'])
    trnorm=pair_mul(norm(r.from_json(tr['new_section_coefficients']),2),
                    pair_inverse(pair_mul(norm(r.from_json(tr['old_section_coefficients']),2),norm(v1,1))))
    trjet=r.sub(r.sub(normjet(r.from_json(tr['new_section_coefficients']),2),normjet(r.from_json(tr['old_section_coefficients']),2)),normjet(v1,1))
    assert evaluate_jet(trjet,parameters,r)==log_pair(trnorm,r)
    hc=r.from_json(slp['initial_principal_transport_coefficients']);hn=norm(hc,1);hj=normjet(hc,1)
    assert evaluate_jet(hj,parameters,r)==log_pair(hn,r)
    def power(a,n):
        out=[1,0]
        while n:
            if n&1:out=pair_mul(out,a)
            a=pair_mul(a,a);n//=2
        return out
    finalnorm=pair_mul(u,pair_inverse(pair_mul(trnorm,power(hn,m))))
    finaljet=r.sub(r.sub(J,trjet),tuple(x*(m%r.Q)%r.Q for x in hj))
    lf=log_pair(finalnorm,r);assert evaluate_jet(finaljet,parameters,r)==lf
    height=(local['actual_hecke_local_log']+lf)*pow(m,-1,r.Q)%r.Q
    ac=r.from_json(local['actual_first_inverse_function']['numerator_coefficients'])
    phijet=r.sub(normjet(ac,2),tuple(2*x%r.Q for x in normjet(v1,1)))
    assert evaluate_jet(phijet,parameters,r)==log_pair(local['first_inverse_degree_zero_norm'],r)
    B=r.from_json(hessian['hecke_correction_matrix']);z=r.from_json(target['target_logarithm'])
    correction=r.mm(r.mm(Omega,(B[0].T,B[1].T)),(z[0].T,z[1].T))
    paramgrad=r.add(r.add(r.cols(finaljet,[0]),tuple(x*pow(2,-1,r.Q)%r.Q for x in r.cols(phijet,[0]))),correction)
    liegrad=r.mm(r.inverse_matrix(Omega),paramgrad)
    liegrad=tuple(x*pow(m,-1,r.Q)%r.Q%47**3 for x in liegrad)
    AK=tuple(x%47**3 for x in r.from_json(sources[1]['canonical_frobenius_matrix']))
    assert r.equal(r.mm(AK,r.conjugate(liegrad,47**3),47**3),liegrad)
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'input_sha256':ih,
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'discriminant':-args.discriminant,
            'bits':304,'steps':records,'negative_norm_coordinate':uminus,'negative_norm_jets':r.to_json(jminus),
            'initial_h_norm':hn,'initial_h_log_norm':log_pair(hn,r),'endpoint_transition_norm':trnorm,
            'true_based_Miller_norm':finalnorm,'true_based_Miller_log_norm':lf,'true_based_Miller_jets':r.to_json(finaljet),
            'formal_fibre_local_log':local['actual_hecke_local_log'],'actual_nonformal_first_variable_local_log':height,
            'actual_local_Lie_gradient_mod47_cubed':r.to_json(liegrad),
            'fibre':'P_(P-b,Y), rational1 in the actual degree-zero divisor pair P-b and R141 second Abel frame A2(Y)',
            'status':'complete actual CM first-variable transport and all54 local connection coefficients; initial h and endpoint retained; not a global height or QC section value'}
    output=args.output or Path('/tmp/p41_cm'+str(args.discriminant)+'_local_connection47_checkpoint.json.gz')
    sha,size=write_checkpoint(output,result);print('ACTUAL CM LOCAL CONNECTION COMPLETE',args.discriminant,'value',height,'norm',finalnorm,size,sha,flush=True)

if __name__=='__main__':main()

