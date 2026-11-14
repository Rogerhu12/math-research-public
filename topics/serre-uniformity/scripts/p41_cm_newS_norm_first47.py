#!/usr/bin/env python3
"""Actual f_CS on the first Abel family, including all54 cubic jets.

The complete CM SLP and gS are evaluated only at verified units in the
original evaluation pool.  No replacement by a class relation is used.
"""
import argparse,gc,gzip,hashlib,json,resource,sys,time
from pathlib import Path


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--discriminant',type=int,choices=[12,7],required=True)
    parser.add_argument('--miller',type=Path)
    parser.add_argument('--endpoint',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_hecke3_hessian47 import section_jets
    from p41_poincare_miller_jets47 import evaluate_jet
    from p41_poincare_norms47 import pair_mul,pair_inverse
    from p41_formal47_multiply import write_checkpoint
    from p41_cm4_divisor47 import kernel
    started=time.monotonic();prefix='/tmp/p41_cm'+str(args.discriminant)
    slp,ssha=read(args.miller or Path(prefix+'_slp47_complete.json.gz'))
    endpoint,esha=read(args.endpoint or Path(prefix+'_newS_endpoint47_certificate.json.gz'))
    assert slp['bits_done']==304 and slp['sign']==1 and len(slp['steps'])==454
    assert slp['magnitude']==slp['target_multiplier']
    assert endpoint['input_sha256']['miller']==ssha and endpoint['frame']=='newS'
    assert endpoint['old_final_point_sha256']==slp['point_sha256']
    slp={key:slp[key] for key in ['source_sha256','initial_source_sha256','point_label','target_multiplier',
                                   'initial_principal_transport_coefficients','negative_quadratic_coefficients','steps']}
    bases,bsha=read(folder/'data/p41_hecke3_abel_bases_checkpoint.json.gz')
    rows=[j-1 for j in bases['families'][0]['points_1based']]
    assert 253 not in rows
    jets,jsha=read(folder/'data/p41_source_cubic47_full_saved.json.gz')
    W=[r.from_json([matrix[j] for j in rows]) for matrix in jets['evaluation_coefficients']]
    del jets,bases
    cm,csha=read(folder/'data/p41_cm_formal_endpoints47_checkpoint.json.gz')
    assert cm['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz']==bsha
    assert cm['input_sha256']['p41_source_cubic47_checkpoint.json.gz']==jsha
    target=cm['targets']['x'+str(args.discriminant)]['targets']['m']['exponentials'][0]
    target={key:target[key] for key in ['parameters','point_sha256']}
    assert cm['source_sha256']==slp['source_sha256']==endpoint['source_sha256']
    del cm
    gc.collect()
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    assert hashes==slp['source_sha256']
    V2,V3=section_jets(W,sources,M,r);spaces={1:W,2:V2,3:V3}
    div=sources[1]
    K=r.from_json(kernel(73,div['cusp_rank_columns_1based'],div['cusp_free_columns_1based'],div['canonical_kernel_block']))
    f0=r.mm(K,r.column(div['canonical_coefficients']))
    Omega=tuple(a*(-3*pow(27652,-1,r.Q)%r.Q)%r.Q for a in r.mm(W[0],K))
    AK=r.from_json(div['canonical_frobenius_matrix'])
    permutation=[rows.index(M['tau'][j]) for j in rows]
    del sources,M,div
    gc.collect()
    par=r.from_json(target['parameters']);t=par[0].T,par[1].T
    assert all(np.all(a%47==0) for a in t)
    def scale(A,k):return tuple(a*(k%r.Q)%r.Q for a in A)
    def product(A):
        assert np.all(r.units(A));out=[1,0]
        for i in range(54):out=pair_mul(out,[int(A[0][i,0]),int(A[1][i,0])])
        return out
    def raw(coefficient,degree):
        values=[r.mm(v,coefficient) for v in spaces[degree]]
        assert np.all(r.units(values[0]))
        shifted=r.zeros(54,1)
        for value in reversed(values):shifted=r.add(r.mul(shifted,t),value)
        norm=pair_mul(product(shifted),pair_inverse(product(values[0])))
        assert norm[1]==0 and norm[0]%47==1
        inv=r.inverse_values(values[0]);a,b,c=[r.mul(values[k],inv) for k in [1,2,3]]
        jet=r.hcat(a,r.sub(b,scale(r.mul(a,a),pow(2,-1,r.Q))),
                    r.add(r.sub(c,r.mul(a,b)),scale(r.mul(r.mul(a,a),a),pow(3,-1,r.Q))))
        assert r.equal(r.rows(jet,permutation),r.conjugate(jet))
        return norm[0],jet
    def logarithm(a):
        assert a%47==1;z=(a-1)%r.Q
        return (z-z*z*pow(2,-1,r.Q)+z*z*z*pow(3,-1,r.Q))%r.Q
    f0norm,f0jet=raw(f0,1)
    def section(coefficient,degree):
        norm,jet=raw(coefficient,degree)
        norm=norm*pow(f0norm,-degree,r.Q)%r.Q;jet=r.sub(jet,scale(f0jet,degree))
        assert evaluate_jet(jet,target['parameters'],r)==logarithm(norm)
        return norm,jet
    negative,nj=section(r.from_json(slp['negative_quadratic_coefficients']),2)
    minus,minusj=pow(negative,-1,r.Q),r.neg(nj)
    u=1;J=r.zeros(54,3);sign=1;magnitude=1;records=[]
    for k,step in enumerate(slp['steps'],1):
        encoded=step['principal_section_coefficients']
        assert hashlib.sha256(json.dumps(encoded,separators=(',',':')).encode()).hexdigest()==step['principal_coefficient_sha256']
        norm,jet=section(r.from_json(encoded),3)
        if step['operation']=='double':
            u=pow(u*u%r.Q*norm%r.Q,-1,r.Q);J=r.neg(r.add(scale(J,2),jet));magnitude*=2
        else:
            assert step['operation']=='add'
            un,jn=(1,r.zeros(54,3)) if sign==1 else (minus,minusj)
            u=pow(u*un%r.Q*norm%r.Q,-1,r.Q);J=r.neg(r.add(r.add(J,jn),jet));magnitude+=1
        sign=-sign;assert sign==step['sign']
        assert evaluate_jet(J,target['parameters'],r)==logarithm(u)
        records.append({'step_index_1based':k,'principal_coefficient_sha256':step['principal_coefficient_sha256'],
                        'actual_principal_norm':norm,'actual_cumulative_F_norm':u})
    m=slp['target_multiplier'];assert sign==1 and magnitude==m
    tr=endpoint['transport'];gn,gj=section(r.from_json(tr['new_section_coefficients']),2)
    for key,degree in [('old_section_coefficients',2),('v1_coefficients',1)]:
        n,j=section(r.from_json(tr[key]),degree);gn=gn*pow(n,-1,r.Q)%r.Q;gj=r.sub(gj,j)
    hn,hj=section(r.from_json(slp['initial_principal_transport_coefficients']),1)
    actual=u*pow(gn*pow(hn,m,r.Q)%r.Q,-1,r.Q)%r.Q
    actualjet=r.sub(r.sub(J,gj),scale(hj,m));actualgrad=r.mm(r.inverse_matrix(Omega),r.cols(actualjet,[0]))
    assert evaluate_jet(actualjet,target['parameters'],r)==logarithm(actual)
    assert r.equal(r.mm(AK,r.conjugate(actualgrad)),actualgrad)
    payload={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
             'input_sha256':{'complete_Miller':ssha,'actual_gS':esha,'original_Abel_bases':bsha,
                              'actual_source_cubic':jsha,'CM_formal_endpoints':csha},
             'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'discriminant':-args.discriminant,'target_multiplier':m,
             'first_formal_point_sha256':target['point_sha256'],'newS_formal_point_sha256':endpoint['new_formal_point_sha256'],
             'records':records,'actual_negative_quadratic_norm':negative,
             'actual_F_chain_norm':u,'actual_gS_norm':gn,'actual_initial_h_norm':hn,
             'actual_f_CS_norm_on_first_family':actual,'log_actual_f_CS_norm_on_first_family':logarithm(actual),
             'actual_f_CS_log_jets':r.to_json(actualjet),'actual_f_CS_Lie_log_gradient_mod47four':r.to_json(actualgrad),
             'all_actual_principal_values_units':True,'nonunit_divisions':0,
             'formula':'f_CS=F_chain/(gS*h^m); div(f_CS)=m(P-b)-A_S(m(P-b))',
             'status':'complete actual f_CS norm on A_family0(mC), with all54 cubic jets and actual gS; this is a function input, not a height'}
    output=args.output or Path(prefix+'_newS_norm_first47_certificate.json.gz')
    sha,size=write_checkpoint(output,payload)
    print('ACTUAL f_CS FIRST FAMILY NORM PASS',args.discriminant,'norm',actual,'log',logarithm(actual),
          size,sha,'seconds',round(time.monotonic()-started,2),'peak_MiB',round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,2),flush=True)


if __name__=='__main__':main()
