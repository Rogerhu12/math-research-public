#!/usr/bin/env python3
"""Construct the true final CM Miller frame function, without assigning an uncomputed norm."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()

def actual_transport(Kold,Aold,Knew,Anew,M,rng,r):
    import numpy as np
    Sold,Snew=r.mm(M['V2'],Kold),r.mm(M['V2'],Knew)
    for attempt in range(100):
        ss,sc=r.rational_trace(Aold,rng);s=r.mm(Sold,sc)
        if not np.all(r.units(s)):continue
        gs,gc=r.rational_trace(Aold,rng);g=r.mm(Sold,gc)
        scaled=r.mul(r.mul(g,r.inverse_values(s)),Snew)
        residual=r.sub(scaled,r.mm(M['V2'],r.rows(scaled,M['P2'])))
        rows,cols=r.rank_pivots(residual)
        if len(rows)!=72:continue
        c,free,block=r.kernel_from_rows(r.rows(residual,rows),rows,cols)
        assert len(free)==1 and r.iszero(r.mm(residual,c))
        transformed=r.mm(Anew,r.conjugate(c));lam=r.rows(transformed,free)
        descend_seed,small=r.rational_trace(lam,rng);c=r.mm(c,small)
        if not np.any(r.units(c)):continue
        assert r.equal(r.mm(Anew,r.conjugate(c)),c)
        t=r.mm(Snew,c);allproducts=r.mul(r.mul(t,r.inverse_values(s)),Sold)
        prows,pcols=r.rank_pivots(Snew);assert len(prows)==73
        change=r.mm(r.inverse_matrix(r.rows(Snew,prows)),r.rows(allproducts,prows))
        assert r.equal(allproducts,r.mm(Snew,change))
        inverse=r.inverse_matrix(change)
        assert r.equal(r.mm(change,inverse),r.eye(73))
        return r.mm(Knew,c),r.mm(Kold,sc),{
            'attempt':attempt+1,'old_section_seed':r.to_json(ss),'auxiliary_seed':r.to_json(gs),
            'line_descent_seed':r.to_json(descend_seed),'full_ideal_isomorphism_determinant_unit':True,
            'one_dimensional_transport_kernel_rank':72,
            'isomorphism_matrix_sha256':hashlib.sha256(json.dumps(r.to_json(change),separators=(',',':')).encode()).hexdigest()}
    raise RuntimeError('No actual full-ideal CM endpoint isomorphism')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--discriminant',type=int,choices=[7,12],required=True)
    p.add_argument('--miller',type=Path)
    p.add_argument('--endpoints',type=Path,default=Path('/tmp/p41_cm_formal_endpoints47_checkpoint.json.gz'))
    p.add_argument('--bases',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    p.add_argument('--output',type=Path);args=p.parse_args()
    folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_formal47_multiply import write_checkpoint,point_hash
    sources,hashes=load_sources(folder/'data');M0=make_model(sources)
    cp=args.miller or Path('/tmp/p41_cm'+str(args.discriminant)+'_slp47_rolling.json.gz')
    slp,ssha=read(cp);ep,esha=read(args.endpoints);base,bsha=read(args.bases)
    assert slp['source_sha256']==ep['source_sha256']==base['source_sha256']==hashes
    assert slp['bits_done']==304 and slp['sign']==1 and slp['magnitude']==slp['target_multiplier']==ep['target_multiplier']
    assert len(slp['steps'])==454
    label='x'+str(args.discriminant);target=ep['targets'][label]['targets']['m']['exponentials'][0]
    Kold,Aold=r.from_json(slp['point_coordinates']),r.from_json(slp['point_frobenius'])
    Knew,Anew=r.from_json(target['point_coordinates']),r.from_json(target['point_frobenius'])
    assert point_hash(Kold,Aold)==slp['point_sha256'] and point_hash(Knew,Anew)==target['point_sha256']
    M=M0;C2=r.eye(199)
    if 'working_chart' in slp:
        omitted={i-1 for i in slp['working_chart']['omitted_evaluation_rows_1based']};keep=[i for i in range(820) if i not in omitted]
        assert all(M0['tau'][i] in omitted for i in omitted) and len(keep)>504
        M=dict(M0);M['W']=r.rows(M0['W'],keep)
        V2,P2,cols,C2=r.normalize(r.rows(M0['V2'],keep),199);assert cols==list(range(199))
        M['V2'],M['P2']=V2,P2;C2i=r.inverse_matrix(C2)
        M['A2']=r.mm(r.mm(C2i,M0['A2']),r.conjugate(C2))
        enc=hashlib.sha256(json.dumps(r.to_json(C2),separators=(',',':')).encode()).hexdigest()
        assert enc==slp['working_chart']['V2_change_sha256']
        Kold,Knew=r.mm(C2i,Kold),r.mm(C2i,Knew)
    ts,ss,record=actual_transport(Kold,Aold,Knew,Anew,M,random.Random(4104717100+args.discriminant),r)
    ts,ss=r.mm(C2,ts),r.mm(C2,ss)
    for c in [ts,ss]:assert r.equal(r.mm(M0['A2'],r.conjugate(c)),c)
    record.update({'new_section_coefficients':r.to_json(ts),'old_section_coefficients':r.to_json(ss),
                   'v1_coefficients':base['families'][0]['v_coefficients']})
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'discriminant':-args.discriminant,
            'input_sha256':{'miller':ssha,'formal_endpoints':esha,'bases':bsha},
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'old_final_point_sha256':slp['point_sha256'],'new_formal_point_sha256':target['point_sha256'],
            'transport':record,
            'transport_function':'g=(new/f0^2)/(old/f0^2)/(v1/f0), div(g)=A_formal-A_old',
            'global_based_function':'f_C=F_chain/(g*h^m), h=f_b/f0; div(f_C)=m(P-b)-A_formal',
            'uncomputed_inputs':'No norm or height is assigned to these actual functions; evaluation, collision units and local heights are subsequent computations',
            'status':'complete actual304-bit CM point equals the independently constructed formal endpoint; true principal frame function retained'}
    output=args.output or Path('/tmp/p41_cm'+str(args.discriminant)+'_endpoint47_certificate.json.gz')
    sha,size=write_checkpoint(output,result);print('ACTUAL CM ENDPOINT TRANSPORT PASS',args.discriminant,size,sha,flush=True)

if __name__=='__main__':main()

