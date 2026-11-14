#!/usr/bin/env python3
"""One actual Miller chain with all54 independent formal-variable cubic norm jets.

The old scalar run is retained as a prefix check.  No second multiplication is
needed to retain the full162 first/second/third local norm coefficients.
"""
import argparse,gzip,hashlib,json,random,sys,time
from pathlib import Path

def jet_evaluator(M,sources,base,jets,r):
    from p41_cm4_divisor47 import kernel
    from p41_hecke3_hessian47 import section_jets
    points=[i-1 for i in base['families'][1]['points_1based']]
    W=[r.rows(r.from_json(A),points) for A in jets['evaluation_coefficients']]
    V2,V3=section_jets(W,sources,M,r)
    assert r.equal(V2[0],r.rows(M['V2'],points)) and r.equal(V3[0],r.rows(M['V3'],points))
    spaces={1:W,2:V2,3:V3}
    K=r.from_json(kernel(73,sources[1]['cusp_rank_columns_1based'],sources[1]['cusp_free_columns_1based'],sources[1]['canonical_kernel_block']))
    fc=r.mm(K,r.column(sources[1]['canonical_coefficients']))
    def raw(coeff,degree):
        values=[r.mm(V,coeff) for V in spaces[degree]];iv=r.inverse_values(values[0])
        a,b,c=[r.mul(v,iv) for v in values[1:]]
        a2=r.mul(a,a);a3=r.mul(a2,a)
        second=r.sub(b,tuple(x*pow(2,-1,r.Q)%r.Q for x in a2))
        third=r.add(r.sub(c,r.mul(a,b)),tuple(x*pow(3,-1,r.Q)%r.Q for x in a3))
        return r.hcat(a,second,third)
    fjet=raw(fc,1)
    def normjet(coeff,degree):return r.sub(raw(coeff,degree),tuple(x*degree%r.Q for x in fjet))
    Omega=tuple(x*(-3*pow(27652,-1,r.Q)%r.Q)%r.Q for x in r.mm(W[0],K))
    return normjet,Omega

def evaluate_jet(J,parameters,r):
    tr=r.from_json(parameters);t=tr[0].T,tr[1].T;current=t;out=r.zeros(54,1)
    for k in range(3):out=r.add(out,r.mul(r.cols(J,[k]),current));current=r.mul(current,t)
    result=[int(out[0].sum()%r.Q),int(out[1].sum()%r.Q)]
    assert result[1]==0
    return result[0]

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--bases',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    parser.add_argument('--exponential',type=Path,default=Path('/tmp/p41_hecke3_exponential_checkpoint.json.gz'))
    parser.add_argument('--jets',type=Path,default=Path('/tmp/p41_source_cubic47_checkpoint.json.gz'))
    parser.add_argument('--local-height',type=Path,default=Path('/tmp/p41_hecke3_formal_height47_compact.json.gz'))
    parser.add_argument('--hessian',type=Path,default=Path('/tmp/p41_hecke3_hessian47_compact.json.gz'))
    parser.add_argument('--scalar-prefix',type=Path,default=Path('/tmp/p41_poincare_miller47_rolling.json.gz'))
    parser.add_argument('--checkpoint',type=Path,default=Path('/tmp/p41_poincare_miller_jets47_rolling.json.gz'))
    parser.add_argument('--max-bits',type=int,default=304)
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,replay_negative
    from p41_formal47_multiply import write_checkpoint,restore_tuple,point_hash
    from p41_poincare_norms47 import pair_mul,pair_inverse
    from p41_poincare_miller47 import prepare_evaluation,addflip_with_section,final_frame_transfer,log_pair
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    paths=[args.bases,args.exponential,args.jets,args.local_height,args.hessian,folder/'data/p41_formal47_multiplication_saved.json.gz']
    raws=[p.read_bytes() for p in paths];base,exp,jets,local,hessian,published=[json.loads(gzip.decompress(raw)) for raw in raws]
    input_hashes={p.name:hashlib.sha256(b).hexdigest() for p,b in zip(paths,raws)}
    assert base['source_sha256']==exp['source_sha256']==local['source_sha256']==hessian['source_sha256']==published['source_sha256']==hashes
    assert exp['bases_sha256']==input_hashes[args.bases.name] and exp['jets_sha256']==input_hashes[args.jets.name]
    norm,*_=prepare_evaluation(M,sources,base,exp,jets,r);normjet,Omega=jet_evaluator(M,sources,base,jets,r)
    parameters=exp['exponentials'][1]['parameters']
    prefix=json.loads(gzip.decompress(args.scalar_prefix.read_bytes())) if args.scalar_prefix.exists() else None
    numerator=r.from_json(local['principal_numerators'][0]);v1=r.from_json(base['families'][0]['v_coefficients'])
    nv=norm(v1,1);direct=pair_mul(norm(numerator,2),pair_inverse(pair_mul(nv,nv)))
    assert direct==local['first_inverse_degree_zero_norm']
    phijet=r.sub(normjet(numerator,2),tuple(2*x%r.Q for x in normjet(v1,1)))
    assert evaluate_jet(phijet,parameters,r)==log_pair(direct,r)
    minusB,AminusB=replay_negative(M,sources[3]);seed,cf=sources[3]['negative_flip_section_seeds_and_coefficients'][0]
    negative=r.mm(M['B'],r.column(cf));negative_norm=norm(negative,2);uminus=pair_inverse(negative_norm);Jminus=r.neg(normjet(negative,2))
    assert evaluate_jet(Jminus,parameters,r)==log_pair(uminus,r)
    rng=random.Random(4104711704);m=published['target_multiplier'];bits=bin(m)[2:]
    data={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'input_sha256':input_hashes,
          'target_multiplier':m,'bits_done':1,'magnitude':1,'sign':1,'steps':[],'torus_coordinate':[1,0],
          'negative_B_coordinate':uminus,'negative_B_norm':negative_norm,'negative_B_log_norm_jets':r.to_json(Jminus),
          'status':'actual Miller transport retaining all54 cubic norm jets in progress; no completed nonformal height yet'}
    K,A=M['B'],M['AB'];J=r.zeros(54,3)
    if args.checkpoint.exists():
        data=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
        assert data['source_sha256']==hashes and data['input_sha256']==input_hashes
        K,A=r.from_json(data['point_coordinates']),r.from_json(data['point_frobenius']);J=r.from_json(data['cumulative_log_norm_jets'])
        assert point_hash(K,A)==data['point_sha256'];rng.setstate(restore_tuple(data['random_state']))
        assert evaluate_jet(J,parameters,r)==log_pair(data['torus_coordinate'],r)
        print('Miller full-jets resume',data['bits_done'],'bits;',len(data['steps']),'steps.',flush=True)
    start=time.monotonic()
    def record_step(rec,f,nf,nj,u,J):
        original=published['steps'][len(data['steps'])]
        assert all(rec[k]==v for k,v in original.items())
        assert evaluate_jet(nj,parameters,r)==log_pair(nf,r)
        assert evaluate_jet(J,parameters,r)==log_pair(u,r)
        if prefix and len(data['steps'])<len(prefix['steps']):
            old=prefix['steps'][len(data['steps'])];assert old['principal_norm']==nf and old['torus_coordinate']==u
        rec.update({'principal_norm':nf,'torus_coordinate':u,
                    'principal_section_coefficients':r.to_json(f),
                    'principal_coefficient_sha256':hashlib.sha256(json.dumps(r.to_json(f),separators=(',',':')).encode()).hexdigest(),
                    'principal_log_norm_jet_sha256':hashlib.sha256(json.dumps(r.to_json(nj),separators=(',',':')).encode()).hexdigest()})
        data['steps'].append(rec)
    for n in range(data['bits_done'],min(len(bits),args.max_bits)):
        u=data['torus_coordinate']
        K,A,f,rec=addflip_with_section(K,A,K,A,M,rng,'Miller jets double bit'+str(n+1),r,same=True)
        nf,nj=norm(f,3),normjet(f,3);u=pair_inverse(pair_mul(pair_mul(u,u),nf));J=r.neg(r.add(tuple(2*x%r.Q for x in J),nj))
        data['sign']*=-1;data['magnitude']*=2;rec.update({'operation':'double','bit':n+1,'sign':data['sign']})
        record_step(rec,f,nf,nj,u,J)
        if bits[n]=='1':
            B0,AB0,u0,J0=(M['B'],M['AB'],[1,0],r.zeros(54,3)) if data['sign']==1 else (minusB,AminusB,uminus,Jminus)
            K,A,f,rec=addflip_with_section(K,A,B0,AB0,M,rng,'Miller jets add bit'+str(n+1),r)
            nf,nj=norm(f,3),normjet(f,3);u=pair_inverse(pair_mul(pair_mul(u,u0),nf));J=r.neg(r.add(r.add(J,J0),nj))
            data['sign']*=-1;data['magnitude']+=1;rec.update({'operation':'add','bit':n+1,'sign':data['sign']})
            record_step(rec,f,nf,nj,u,J)
        data['bits_done']=n+1;data['torus_coordinate']=u;data['cumulative_log_norm_jets']=r.to_json(J)
        assert data['magnitude']==int(bits[:n+1],2)
        data['point_coordinates'],data['point_frobenius']=r.to_json(K),r.to_json(A)
        data['point_sha256']=point_hash(K,A);data['random_state']=rng.getstate()
        if (n+1)%5==0 or n+1==min(len(bits),args.max_bits):
            digest,size=write_checkpoint(args.checkpoint,data)
            print('MILLER ALL54 JETS CHECKPOINT',n+1,'bits',len(data['steps']),'steps; torus',u,'seconds',round(time.monotonic()-start,1),'sha',digest,flush=True)
    if data['bits_done']==304:
        assert data['point_sha256']==published['point_sha256'] and data['sign']==1
        newK,newA=r.from_json(exp['exponentials'][0]['point_coordinates']),r.from_json(exp['exponentials'][0]['point_frobenius'])
        transfer,record=final_frame_transfer(K,A,newK,newA,base,M,random.Random(4104714601),r,norm)
        transjet=r.sub(r.sub(normjet(r.from_json(record['new_section_coefficients']),2),normjet(r.from_json(record['old_section_coefficients']),2)),normjet(v1,1))
        assert evaluate_jet(transjet,parameters,r)==log_pair(transfer,r)
        newjet=r.sub(J,transjet);unew=pair_mul(data['torus_coordinate'],pair_inverse(transfer));lu=log_pair(unew,r)
        assert evaluate_jet(newjet,parameters,r)==lu
        height=(local['actual_hecke_local_log_of_same_frame']+lu)*pow(m,-1,r.Q)%r.Q
        z=r.from_json(exp['exponentials'][0]['target_logarithm']);B=r.from_json(hessian['hecke_correction_matrix'])
        correction=r.mm(r.mm(Omega,(B[0].T,B[1].T)),(z[0].T,z[1].T))
        paramgrad=r.add(r.add(r.cols(newjet,[0]),tuple(x*pow(2,-1,r.Q)%r.Q for x in r.cols(phijet,[0]))),correction)
        liegrad=r.mm(r.inverse_matrix(Omega),paramgrad);liegrad=tuple(x*pow(m,-1,r.Q)%r.Q for x in liegrad)
        liegrad3=tuple(x%47**3 for x in liegrad);AK=tuple(x%47**3 for x in r.from_json(sources[1]['canonical_frobenius_matrix']))
        assert r.equal(r.mm(AK,r.conjugate(liegrad3,47**3),47**3),liegrad3)
        data.update({'endpoint_transfer':record,'endpoint_new_frame_coordinate':unew,'endpoint_log_coordinate':lu,
                     'endpoint_new_frame_log_norm_jets':r.to_json(newjet),
                     'actual_hecke_local_log_initial_fibre':height,
                     'actual_initial_fibre_Lie_gradient_mod47_cubed':r.to_json(liegrad3),
                     'gradient_precision_reason':'total-degree>=4 terms at fixed Y in47J contribute at least47^3 to the derivative at Q=0; actual gradient is certified modulo47^3',
                     'status':'actual full Miller transport and all54 formal norm jets complete; scalar nonformal-first-variable local value and all54 local connection coefficients; not global height coefficients'})
        digest,size=write_checkpoint(args.checkpoint,data)
        print('ACTUAL MILLER ALL54 LOCAL CONNECTION COMPLETE',height,'endpoint',unew,'sha',digest,flush=True)

if __name__=='__main__':main()
