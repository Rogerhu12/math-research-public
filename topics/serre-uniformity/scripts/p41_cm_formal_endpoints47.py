#!/usr/bin/env python3
"""Actual CM logarithms and formal endpoint representatives in the fixed R141 frame.

The m-endpoints use R121's actual finite-field annihilator. H47=48-T47
endpoints are also saved; their class identification uses the good-reduction
Eichler-Shimura relation, not a numerical comparison with a new Miller chain.
No principal transport function or final local height is claimed here.
"""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--bases',type=Path,default=Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    ap.add_argument('--jets',type=Path,default=Path('/tmp/p41_source_cubic47_checkpoint.json.gz'))
    ap.add_argument('--output',type=Path,default=Path('/tmp/p41_cm_formal_endpoints47_checkpoint.json.gz'))
    args=ap.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_cm_height_calibration47 import invert,matmul
    from p41_group_operations47 import load_sources,make_model
    from p41_formal47_exponential import construct_point
    from p41_formal47_multiply import write_checkpoint,point_hash
    from p41_cm4_divisor47 import kernel
    from p41_poincare_norms47 import determinant
    def read(path):
        raw=path.read_bytes();return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()
    names=['p41_full_chow_heegner_certificate.json.gz','p41_jacobi_cm_certificate.json','p41_small_hecke_cm_transport47_certificate.json.gz','p41_hecke47_compact.json.gz','p41_formal47_log_compact.json.gz','p41_cm_based_points47_checkpoint.json.gz']
    values=[read(folder/'data'/name) for name in names];full,jac,small,hecke,log,based=[v[0] for v in values]
    input_hashes={name:v[1] for name,v in zip(names,values)}
    for name in names[:2]:assert small['source_sha256'][name]==input_hashes[name]
    base,bh=read(args.bases);jets,jh=read(args.jets)
    input_hashes[args.bases.name]=bh;input_hashes[args.jets.name]=jh
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    assert base['source_sha256']==hashes==log['source_sha256']
    assert base['jets_sha256']==jh
    Q=r.Q;P=47;basis=[[] for _ in range(54)];targets={'r3':[],'r7':[],'T2':[],'T47':[]}
    for field,jf in zip(full['fields'],jac['fields']):
        assert field['factor_descending']==jf['factor_descending']
        f=[v%Q for v in field['factor_descending'][::-1]];d=len(f)-1
        def val(pair):
            co=[int(v)*pow(int(pair[0]),-1,Q)%Q for v in pair[1][::-1]]
            return co+[0]*(d-len(co))
        def mul(a,b):
            c=[0]*(2*d-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%Q
            for k in range(len(c)-1,d-1,-1):
                lead=c[k]
                for i in range(d):c[k-d+i]=(c[k-d+i]-lead*f[i])%Q
            return c[:d]
        t3=val(field['directions'][full['indices'].index(3)-1][0]);power=[1]+[0]*(d-1)
        for k in range(54):basis[k]+=power;power=mul(power,t3)
        targets['r3']+=val([jf['r3_denominator'],jf['r3_numerator_descending']])
        targets['r7']+=val([jf['r7_denominator'],jf['r7_numerator_descending']])
        for ell in (2,47):targets['T'+str(ell)]+=val(field['directions'][full['indices'].index(ell)-1][0])
    inverse,det=invert(basis,Q)
    for name in ('x12','x7'):
        co=small['coordinates'][name]
        row=[v*pow(co['denominator'],-1,Q)%Q for v in co['numerators']]
        targets[name]=matmul([row],small['basis_matrix_mod47_4'],Q)[0]
    polys={key:matmul([value],inverse,Q)[0] for key,value in targets.items()}
    for key in targets:assert matmul([polys[key]],basis,Q)[0]==targets[key]
    T2=r.from_json(hecke['operators']['2']['canonical_operator']);T3=r.from_json(hecke['operators']['3']['canonical_operator'])
    I=r.eye(54)
    def scale(a,c):return tuple(x*(int(c)%Q)%Q for x in a)
    def eval_matrix(poly):
        ans=r.zeros(54,54)
        for c in poly[::-1]:ans=r.add(r.mm(ans,T3),scale(I,c))
        return ans
    assert r.equal(eval_matrix(polys['T2']),T2)
    T47=eval_matrix(polys['T47']);N=r.sub(scale(I,48),T47);Ninv=r.inverse_matrix(N)
    assert r.equal(r.mm(N,Ninv),I) and r.equal(r.mm(Ninv,N),I)
    m=int(log['formal_input_multiplier']);assert log['formal_input_sign']==1
    assert determinant(N)==[m%Q,0]
    lb=r.from_json(log['log_of_B_minus4']);assert r.equal(scale(lb,m),r.from_json(log['log_of_signed_multiple']))
    def eval_log(poly):
        out=r.zeros(1,54)
        for c in poly[::-1]:out=r.add(r.mm(out,T3),scale(lb,c))
        return out
    logs={key:eval_log(polys[key]) for key in ('r3','r7','x12','x7')}
    assert r.equal(scale(logs['x12'],20),r.sub(scale(r.mm(logs['r3'],T2),pow(3,-1,Q)),logs['r3']))
    assert r.equal(scale(logs['x7'],20),r.sub(logs['r7'],logs['r3']))
    AK=r.from_json(sources[1]['canonical_frobenius_matrix'])
    results={}
    for name in ('x12','x7'):
        lc=logs[name];assert r.equal(r.mm(lc,AK),r.conjugate(lc))
        assert all(np.all(a%P==0) for a in lc)
        entry={'log_of_class':r.to_json(lc),'T3_polynomial_ascending':polys[name],'targets':{}}
        for label,target in [('m',scale(lc,m)),('H47',r.mm(lc,N))]:
            witnesses=[]
            for k,rec in enumerate(base['families']):
                point,A,w=construct_point(target,rec,jets,sources[1],M,r,kernel)
                assert r.equal(r.mm(point,A),r.mm(M['A2'],r.conjugate(point)))
                w['point_sha256']=point_hash(point,A);w['family_index']=k
                witnesses.append(w)
                print('CM actual formal endpoint',name,label,'family',k,'PASS',w['point_sha256'],flush=True)
            entry['targets'][label]={'logarithm':r.to_json(target),'exponentials':witnesses}
        results[name]=entry
    out={'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'source_sha256':hashes,
         'input_sha256':input_hashes,'target_multiplier':m,'T3_power_basis_determinant_mod47':det%P,
         'T3_power_basis_matrix':basis,'inverse_T3_power_basis_matrix':inverse,
         'T2_polynomial_ascending':polys['T2'],'T47_polynomial_ascending':polys['T47'],
         'H47_differential_matrix':r.to_json(N),'H47_inverse_differential_matrix':r.to_json(Ninv),
         'H47_determinant_mod47_power':[m%Q,0],'targets':results,
         'H47_formality_reason':'good47 Eichler-Shimura: T47=Frob47+Ver47 on special fibre; on F47-rational points both give 1 and47, so48-T47 kills reduction',
         'status':'exact CM Lie coordinates and both fixed Abel families for m and H47; actual principal transport functions and complete new Miller-chain comparisons still pending',
         'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    digest,size=write_checkpoint(args.output,out)
    print('CM FORMAL ENDPOINTS SAVED',size,digest,flush=True)

if __name__=='__main__':main()
