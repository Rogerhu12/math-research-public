#!/usr/bin/env python3
"""Actual first-variable Miller transport in P_(B_minus4,Y), Y=m B_minus4.

The second variable uses exactly the new R141/R145 Abel frame.  Every AddFlip
has div(f/f0^3)=A_P+A_Q+A_R, so its torus coordinate is (uP*uQ*Norm(f/f0^3))^-1.
The arithmetic path and RNG are identical to the published R121 multiplication;
every resulting point hash is compared with its published step.
"""
import argparse,gzip,hashlib,json,random,sys,time
from pathlib import Path

def log_pair(u,r):
    assert u[1]==0 and u[0]%47==1
    w=(u[0]-1)%r.Q
    return (w-w*w*pow(2,-1,r.Q)+w*w*w*pow(3,-1,r.Q))%r.Q

def prepare_evaluation(M,sources,base,exp,jets,r):
    """The real54 moving points of A2(Y), with all section degrees calibrated."""
    import numpy as np
    from p41_cm4_divisor47 import kernel
    from p41_poincare_norms47 import pair_mul,pair_inverse
    from verify_p41_hecke3_hessian47 import cubic_basis
    points=[i-1 for i in base['families'][1]['points_1based']]
    tr=r.from_json(exp['exponentials'][1]['parameters']);t=tr[0].T,tr[1].T
    assert t[0].shape==(54,1) and all(np.all(a%47==0) for a in t)
    Ws=[r.rows(r.from_json(A),points) for A in jets['evaluation_coefficients']]
    W=r.zeros(54,73)
    for A in reversed(Ws):W=r.add(r.mul(W,t),A)
    sourceW=r.rows(M['W'],points)
    sq=sources[1]['square_basis_monomials_1based'];C2=r.from_json(sources[1]['square_basis_inverse'])
    V2=r.mm(r.mul(r.cols(W,[a-1 for a,b in sq]),r.cols(W,[b-1 for a,b in sq])),C2)
    _,_,C3=cubic_basis(M['W'],r.zeros(820,73),sources,M,None,r)
    V3,_,_=cubic_basis(W,r.zeros(54,73),sources,M,C3,r)
    K=r.from_json(kernel(73,sources[1]['cusp_rank_columns_1based'],sources[1]['cusp_free_columns_1based'],sources[1]['canonical_kernel_block']))
    fc=r.mm(K,r.column(sources[1]['canonical_coefficients']))
    f0=r.mm(sourceW,fc);ft=r.mm(W,fc)
    def product(A):
        result=[1,0]
        assert A[0].shape==(54,1)
        for i in range(54):result=pair_mul(result,[int(A[0][i,0]),int(A[1][i,0])])
        return result
    def raw_norm(a,b):
        assert np.all(r.units(a)) and np.all(r.units(b))
        result=pair_mul(product(a),pair_inverse(product(b)))
        assert result[1]==0 and result[0]%47==1
        return result
    fn=raw_norm(ft,f0)
    shifted={1:W,2:V2,3:V3};original={1:sourceW,2:r.rows(M['V2'],points),3:r.rows(M['V3'],points)}
    def section_norm(coeff,degree):
        norm=raw_norm(r.mm(shifted[degree],coeff),r.mm(original[degree],coeff))
        factor=[1,0]
        for _ in range(degree):factor=pair_mul(factor,fn)
        return pair_mul(norm,pair_inverse(factor))
    print('Actual54 moving-point norm evaluator uses the exact new second Abel frame.',flush=True)
    return section_norm,raw_norm,shifted,original,fc

def addflip_with_section(KP,AP,KQ,AQ,M,rng,label,r,same=False):
    """Identical choices to R121; retain the actual cubic principal numerator."""
    from p41_group_operations47 import flip
    from p41_formal47_multiply import point_hash
    WP,WQ=r.mm(M['V2'],KP),r.mm(M['V2'],KQ)
    P,prows,pcols,pinv=r.normalize(WP,73);assert pcols==list(range(73))
    if same:Q=P
    else:
        square=r.rows(WQ,prows);qr,qc=r.rank_pivots(square)
        if len(qr)==73:Q=r.mm(WQ,r.inverse_matrix(square))
        else:
            Q,_,qcols,_=r.normalize(WQ,73);assert qcols==list(range(73))
    pairs=[[k,k] for k in range(73)]+[[k,(k+1)%73] for k in range(73)]
    while True:
        pairs += [[rng.randrange(73),rng.randrange(73)] for _ in range(100)]
        products=r.mul(r.cols(P,[a for a,b in pairs]),r.cols(Q,[b for a,b in pairs]))
        rr,cc=r.rank_pivots(products)
        if len(rr)==199:break
        assert len(rr)<199 and len(pairs)<746
    U,Urows,_,_=r.normalize(products,199)
    for attempt in range(1,31):
        seed,coeff=r.rational_trace(M['A1'],rng);v=r.mm(M['W'],coeff)
        residual=r.mul(v,M['V3']);residual=r.sub(residual,r.mm(U,r.rows(residual,Urows)))
        rr,cc=r.rank_pivots(residual)
        if len(rr)!=252:continue
        K,free,_=r.kernel_from_rows(r.rows(residual,rr),rr,cc);assert r.iszero(r.mm(residual,K))
        transformed=r.mm(M['A3'],r.conjugate(K));A=r.rows(transformed,free)
        assert r.equal(r.mm(K,A),transformed) and r.equal(r.mm(A,r.conjugate(A)),r.eye(73))
        break
    else:raise RuntimeError('No complete colon in R121 arithmetic replay')
    result,Aresult,fliprec=flip(r.mm(M['V3'],K),A,M,rng,label)
    principal=r.mm(K,r.column(fliprec['f_coefficients']))
    assert r.equal(r.mm(M['A3'],r.conjugate(principal)),principal)
    return result,Aresult,principal,{'product_rank':199,'colon_rank':252,'flip_rank':126,
                                  'colon_attempts':attempt,'point_sha256':point_hash(result,Aresult)}

def final_frame_transfer(Kold,Aold,Knew,Anew,base,M,rng,r,norm):
    """Actual g with div(g)=A1(Y)-A_old, including the change of base divisor."""
    import numpy as np
    Sold,Snew=r.mm(M['V2'],Kold),r.mm(M['V2'],Knew)
    for attempt in range(100):
        ss,sc=r.rational_trace(Aold,rng);s=r.mm(Sold,sc)
        if not np.all(r.units(s)):continue
        gs,gc=r.rational_trace(Aold,rng);g=r.mm(Sold,gc)
        ratio=r.mul(g,r.inverse_values(s));scaled=r.mul(ratio,Snew)
        residual=r.sub(scaled,r.mm(M['V2'],r.rows(scaled,M['P2'])))
        rows,cols=r.rank_pivots(residual)
        if len(rows)!=72:continue
        c,free,block=r.kernel_from_rows(r.rows(residual,rows),rows,cols)
        assert len(free)==1 and r.iszero(r.mm(residual,c))
        transformed=r.mm(Anew,r.conjugate(c));lam=r.rows(transformed,free)
        # Descend the one-dimensional line before choosing its vector.
        seed,small=r.rational_trace(lam,rng);c=r.mm(c,small)
        assert not r.iszero(c) and r.equal(r.mm(Anew,r.conjugate(c)),c)
        t=r.mm(Snew,c);quot=r.mul(t,r.inverse_values(s));allproducts=r.mul(quot,Sold)
        prows,pcols=r.rank_pivots(Snew);assert len(prows)==73
        inv=r.inverse_matrix(r.rows(Snew,prows));change=r.mm(inv,r.rows(allproducts,prows))
        assert r.equal(allproducts,r.mm(Snew,change))
        r.inverse_matrix(change)
        ts=r.mm(Knew,c);ss2=r.mm(Kold,sc)
        # (t/s)*(f0/v1); all section_norms already divide by the proper f0 power.
        from p41_poincare_norms47 import pair_mul,pair_inverse
        first=pair_mul(norm(ts,2),pair_inverse(norm(ss2,2)))
        v1=r.from_json(base['families'][0]['v_coefficients'])
        value=pair_mul(first,pair_inverse(norm(v1,1)))
        return value,{'attempt':attempt+1,'old_section_coefficients':r.to_json(ss2),'new_section_coefficients':r.to_json(ts),
                      'full_ideal_isomorphism_determinant_checked':True,'transition_norm':value}
    raise RuntimeError('No actual endpoint frame isomorphism')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--bases',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    parser.add_argument('--exponential',type=Path,default=Path('/tmp/p41_hecke3_exponential_checkpoint.json.gz'))
    parser.add_argument('--jets',type=Path,default=Path('/tmp/p41_source_cubic47_checkpoint.json.gz'))
    parser.add_argument('--local-height',type=Path,default=Path('/tmp/p41_hecke3_formal_height47_compact.json.gz'))
    parser.add_argument('--checkpoint',type=Path,default=Path('/tmp/p41_poincare_miller47_rolling.json.gz'))
    parser.add_argument('--max-bits',type=int,default=304)
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,replay_negative
    from p41_formal47_multiply import write_checkpoint,restore_tuple,point_hash
    from p41_poincare_norms47 import pair_mul,pair_inverse
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    paths=[args.bases,args.exponential,args.jets,args.local_height,folder/'data/p41_formal47_multiplication_saved.json.gz']
    raws=[p.read_bytes() for p in paths];base,exp,jets,local,published=[json.loads(gzip.decompress(raw)) for raw in raws]
    input_hashes={p.name:hashlib.sha256(b).hexdigest() for p,b in zip(paths,raws)}
    assert base['source_sha256']==exp['source_sha256']==local['source_sha256']==published['source_sha256']==hashes
    assert exp['bases_sha256']==input_hashes[args.bases.name] and exp['jets_sha256']==input_hashes[args.jets.name]
    norm,_,_,_,_=prepare_evaluation(M,sources,base,exp,jets,r)
    # Independent geometric calibration against R145's full126-degree algebras:
    # the fixed72 residual points cancel, leaving the54 direct moving points.
    numerator=r.from_json(local['principal_numerators'][0]);v1=r.from_json(base['families'][0]['v_coefficients'])
    nv=norm(v1,1);direct=pair_mul(norm(numerator,2),pair_inverse(pair_mul(nv,nv)))
    assert direct==local['first_inverse_degree_zero_norm']
    print('Direct54-point norm agrees with the independent126-degree restriction-algebra norm.',flush=True)
    minusB,AminusB=replay_negative(M,sources[3]);seed,cf=sources[3]['negative_flip_section_seeds_and_coefficients'][0]
    negative_numerator=r.mm(M['B'],r.column(cf));negative_norm=norm(negative_numerator,2);uminus=pair_inverse(negative_norm)
    rng=random.Random(4104711704);m=published['target_multiplier'];bits=bin(m)[2:]
    assert len(bits)==304 and published['bits_done']==304 and published['sign']==1
    data={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'input_sha256':input_hashes,
          'target_multiplier':m,'bits_done':1,'magnitude':1,'sign':1,'steps':[],'torus_coordinate':[1,0],
          'negative_B_coordinate':uminus,'negative_B_norm':negative_norm,
          'status':'actual first-variable Miller transport in progress; no nonformal height output yet'}
    K,A=M['B'],M['AB']
    if args.checkpoint.exists():
        data=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
        assert data['source_sha256']==hashes and data['input_sha256']==input_hashes
        K,A=r.from_json(data['point_coordinates']),r.from_json(data['point_frobenius'])
        assert point_hash(K,A)==data['point_sha256'];rng.setstate(restore_tuple(data['random_state']))
        print('Miller resume',data['bits_done'],'bits,',len(data['steps']),'steps.',flush=True)
    start=time.monotonic()
    for n in range(data['bits_done'],min(len(bits),args.max_bits)):
        u=data['torus_coordinate']
        K,A,f,rec=addflip_with_section(K,A,K,A,M,rng,'Miller double bit'+str(n+1),r,same=True)
        nf=norm(f,3);u=pair_inverse(pair_mul(pair_mul(u,u),nf));data['sign']*=-1;data['magnitude']*=2
        rec.update({'operation':'double','bit':n+1,'sign':data['sign']})
        assert all(rec[k]==v for k,v in published['steps'][len(data['steps'])].items())
        rec.update({'principal_norm':nf,'torus_coordinate':u,'principal_coefficient_sha256':hashlib.sha256(json.dumps(r.to_json(f),separators=(',',':')).encode()).hexdigest()})
        data['steps'].append(rec)
        if bits[n]=='1':
            B0,AB0,u0=(M['B'],M['AB'],[1,0]) if data['sign']==1 else (minusB,AminusB,uminus)
            K,A,f,rec=addflip_with_section(K,A,B0,AB0,M,rng,'Miller add bit'+str(n+1),r)
            nf=norm(f,3);u=pair_inverse(pair_mul(pair_mul(u,u0),nf));data['sign']*=-1;data['magnitude']+=1
            rec.update({'operation':'add','bit':n+1,'sign':data['sign']})
            assert all(rec[k]==v for k,v in published['steps'][len(data['steps'])].items())
            rec.update({'principal_norm':nf,'torus_coordinate':u,'principal_coefficient_sha256':hashlib.sha256(json.dumps(r.to_json(f),separators=(',',':')).encode()).hexdigest()})
            data['steps'].append(rec)
        data['bits_done']=n+1;data['torus_coordinate']=u
        assert data['magnitude']==int(bits[:n+1],2) and u[1]==0 and u[0]%47==1
        data['point_coordinates'],data['point_frobenius']=r.to_json(K),r.to_json(A)
        data['point_sha256']=point_hash(K,A);data['random_state']=rng.getstate()
        if (n+1)%5==0 or n+1==min(len(bits),args.max_bits):
            digest,size=write_checkpoint(args.checkpoint,data)
            print('MILLER CHECKPOINT',n+1,'bits',len(data['steps']),'steps; torus',u,'seconds',round(time.monotonic()-start,1),'sha',digest,flush=True)
    if data['bits_done']==304:
        assert data['point_sha256']==published['point_sha256'] and data['sign']==1
        newK=r.from_json(exp['exponentials'][0]['point_coordinates']);newA=r.from_json(exp['exponentials'][0]['point_frobenius'])
        transfer,record=final_frame_transfer(K,A,newK,newA,base,M,random.Random(4104714601),r,norm)
        unew=pair_mul(data['torus_coordinate'],pair_inverse(transfer));lu=log_pair(unew,r)
        h=(local['actual_hecke_local_log_of_same_frame']+lu)*pow(m,-1,r.Q)%r.Q
        data.update({'endpoint_transfer':record,'endpoint_new_frame_coordinate':unew,'endpoint_log_coordinate':lu,
                     'actual_hecke_local_log_initial_fibre':h,
                     'status':'actual Miller transport into the same formal frame complete; initial fibre P_(B_minus4,Y), rational1 in (E_B-D0,A2(Y)); independent norm verification pending'})
        digest,size=write_checkpoint(args.checkpoint,data)
        print('ACTUAL NONFORMAL FIRST-VARIABLE LOCAL LOG',h,'endpoint scalar',unew,'sha',digest,flush=True)

if __name__=='__main__':main()
