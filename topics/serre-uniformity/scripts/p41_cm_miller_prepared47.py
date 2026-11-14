#!/usr/bin/env python3
"""Integral local-factor evaluation of an actual based-CM Miller SLP."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def read(path):
    b=path.read_bytes()
    return json.loads(gzip.decompress(b) if path.suffix=='.gz' else b),hashlib.sha256(b).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--script-dir',type=Path,required=True);p.add_argument('--discriminant',type=int,choices=[7,12],required=True)
    p.add_argument('--jets',type=Path,default=Path('/tmp/p41_cm_quadratic_jets47_raw.json.gz'))
    p.add_argument('--miller',type=Path);p.add_argument('--endpoint',type=Path)
    p.add_argument('--formal-endpoints',type=Path,default=Path('/tmp/p41_cm_formal_endpoints47_checkpoint.json.gz'))
    p.add_argument('--output',type=Path);args=p.parse_args()
    folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_hecke3_hessian47 import section_jets
    from p41_weierstrass_unit47 import prepare_unit
    from p41_formal47_multiply import write_checkpoint,point_hash
    from p41_poincare_norms47 import pair_mul,pair_inverse
    sources,hashes=load_sources(folder/'data');M=make_model(sources)
    jets,jsha=read(args.jets);cp=args.miller or Path('/tmp/p41_cm'+str(args.discriminant)+'_slp47_rolling.json.gz')
    slp,ssha=read(cp)
    initial,isha=read(folder/'data/p41_cm_based_points47_checkpoint.json.gz')
    assert slp['source_sha256']==jets['source_sha256']==initial['source_sha256']==hashes
    assert slp['initial_source_sha256']==isha
    point=next(a for a in initial['records'] if a['point_label']==slp['point_label'])
    labels=[a['label'] for a in jets['records']];n=len(labels);order=jets['order']
    W=[r.from_json([rec['normalized_weight2_coefficients'][k] for rec in jets['records']]) for k in range(order+1)]
    V2,V3=section_jets(W,sources,M,r)
    one=[[1,0]];t=[[0,0],[1,0]]
    def add(a,b):return [(a[0]+b[0])%r.Q,(a[1]+b[1])%r.Q]
    def neg(a):return [(-a[0])%r.Q,(-a[1])%r.Q]
    def product(a,b):
        ans=[[0,0] for _ in range(len(a)+len(b)-1)]
        for i,x in enumerate(a):
            for j,y in enumerate(b):ans[i+j]=add(ans[i+j],pair_mul(x,y))
        return ans
    def divide(a,b):
        assert a[-1]==b[-1]==[1,0] and len(a)>=len(b)
        rem=[x[:] for x in a];quo=[[0,0] for _ in range(len(a)-len(b)+1)]
        for k in range(len(quo)-1,-1,-1):
            c=rem[k+len(b)-1];quo[k]=c[:]
            for j,x in enumerate(b):rem[k+j]=add(rem[k+j],neg(pair_mul(c,x)))
        assert all(x==[0,0] for x in rem),'Actual shared local factors failed monic exact division'
        assert quo[-1]==[1,0] and all(a%47==b%47==0 for a,b in quo[:-1])
        return quo
    def power(a,k):
        assert k>=0;v=[1,0]
        while k:
            if k&1:v=pair_mul(v,a)
            a=pair_mul(a,a);k//=2
        return v
    def prepared(values,j,c=0,degree=None):
        return prepare_unit([[int(v[0][j,c]),int(v[1][j,c])] for v in values],precision=4,degree=degree)
    def ideal_factors(coeff):
        vv=[r.mm(v,coeff) for v in V2];out=[]
        for j in range(n):
            choices=[]
            for c in range(coeff[0].shape[1]):
                e=next((k for k,v in enumerate(vv) if r.units(r.rows(r.cols(v,[c]),[j]))[0,0]),None)
                if e is not None:choices.append((e,c))
            assert choices;e,c=min(choices);a=prepared(vv,j,c,e)
            out.append({'column_1based':c+1,'degree':e,'weierstrass_coefficients':a['weierstrass_coefficients']})
        return out
    ip=r.from_json(point['point_coordinates'])
    assert point_hash(ip,r.from_json(point['point_frobenius']))==slp['initial_point_sha256']
    initial_ideals=ideal_factors(ip);iw=[a['weierstrass_coefficients'] for a in initial_ideals]
    hh=[r.mm(v,r.from_json(initial['f_b_coefficients'])) for v in W]
    hs=[prepared(hh,j) for j in range(n)]
    for j,label in enumerate(labels):
        wh=hs[j]['weierstrass_coefficients']
        expected=product(wh,t) if label==slp['point_label'] else divide(wh,t) if label=='P_minus3' else wh
        assert iw[j]==expected,'The actual initial ideal does not match P-b+div(f_b/f0) on the whole disc'
    nv=[r.mm(v,r.from_json(slp['negative_quadratic_coefficients'])) for v in V2]
    negative=[prepared(nv,j) for j in range(n)]
    nw=[divide(negative[j]['weierstrass_coefficients'],iw[j]) for j in range(n)]
    negative_ideals=ideal_factors(r.from_json(slp['negative_point_coordinates']))
    assert [a['weierstrass_coefficients'] for a in negative_ideals]==nw
    minusU=[pair_inverse(a['unit_constant']) for a in negative]
    coeffs=[]
    for a in slp['steps']:
        c=a['principal_section_coefficients']
        assert hashlib.sha256(json.dumps(c,separators=(',',':')).encode()).hexdigest()==a['principal_coefficient_sha256']
        coeffs.append(r.from_json(c))
    allcf=r.hcat(*coeffs);values=[r.mm(v,allcf) for v in V3]
    cw=[[x[:] for x in a] for a in iw];cu=[[1,0] for _ in range(n)];sign=1;records=[];maxe=0
    for k,step in enumerate(slp['steps']):
        pp=[prepared(values,j,k) for j in range(n)]
        for j,a in enumerate(pp):
            maxe=max(maxe,a['degree'])
            if step['operation']=='double':
                denominator=product(cw[j],cw[j]);u=pair_mul(cu[j],cu[j])
            else:
                assert step['operation']=='add'
                denominator=product(cw[j],iw[j] if sign==1 else nw[j])
                u=pair_mul(cu[j],[1,0] if sign==1 else minusU[j])
            cw[j]=divide(a['weierstrass_coefficients'],denominator)
            cu[j]=pair_inverse(pair_mul(u,a['unit_constant']))
        sign=-sign;assert sign==step['sign']
        records.append({'step_index_1based':k+1,'principal_coefficient_sha256':step['principal_coefficient_sha256'],
                        'unit_constants':[a['unit_constant'] for a in pp],
                        'nonunit_points':[{'point_index_1based':j+1,'degree':a['degree'],'weierstrass_coefficients':a['weierstrass_coefficients'],
                                           'required_last_jet':a['required_last_jet']} for j,a in enumerate(pp) if a['degree']]})
    current_ideals=ideal_factors(r.from_json(slp['point_coordinates']))
    assert [a['weierstrass_coefficients'] for a in current_ideals]==cw
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,'discriminant':-args.discriminant,
            'input_sha256':{'jets':jsha,'miller':ssha,'initial':isha},
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'labels':labels,'bits_done':slp['bits_done'],'steps_done':len(records),'maximum_residual_degree':maxe,
            'initial_effective_divisor':initial_ideals,'initial_h_preparation':hs,
            'negative_effective_divisor':negative_ideals,'negative_section_preparation':negative,
            'steps':records,'current_effective_divisor':current_ideals,'current_unit_constants':cu,
            'local_function_convention':'F_n=V_n*W_initial^n/W_current; true f_C after final transport is F_n/(g*h^m)',
            'nonunit_divisions':0,'status':'actual based-CM SLP local unit transport through the saved prefix; no height claimed'}
    if args.endpoint:
        assert slp['bits_done']==304 and sign==1
        endpoint,esha=read(args.endpoint);exps,xsha=read(args.formal_endpoints)
        assert endpoint['input_sha256']['miller']==ssha and endpoint['input_sha256']['formal_endpoints']==xsha
        assert endpoint['source_sha256']==exps['source_sha256']==hashes
        target=exps['targets']['x'+str(args.discriminant)]['targets']['m']['exponentials'][0]
        new_ideals=ideal_factors(r.from_json(target['point_coordinates']))
        assert all(a['degree']==0 for a in new_ideals),'New formal representative meets one of the required closed discs'
        tr=endpoint['transport'];components={
            'new':[r.mm(v,r.from_json(tr['new_section_coefficients'])) for v in V2],
            'old':[r.mm(v,r.from_json(tr['old_section_coefficients'])) for v in V2],
            'v1':[r.mm(v,r.from_json(tr['v1_coefficients'])) for v in W]}
        transition=[];global_values=[];m=slp['target_multiplier']
        for j,label in enumerate(labels):
            a={k:prepared(v,j) for k,v in components.items()}
            assert product(a['new']['weierstrass_coefficients'],cw[j])==product(a['old']['weierstrass_coefficients'],a['v1']['weierstrass_coefficients'])
            ug=pair_mul(a['new']['unit_constant'],pair_inverse(pair_mul(a['old']['unit_constant'],a['v1']['unit_constant'])))
            unit=pair_mul(cu[j],pair_inverse(pair_mul(ug,power(hs[j]['unit_constant'],m))))
            ordx=1 if label==slp['point_label'] else -1 if label=='P_minus3' else 0
            global_values.append({'label':label,'order_in_fixed_local_parameter':m*ordx,'leading_unit_mod47four':unit,
                                  'ordinary_finite_value':unit if ordx==0 else None})
            transition.append({'label':label,'components':a,'unit_constant':ug})
        result['input_sha256'].update({'endpoint':esha,'formal_endpoints':xsha})
        result.update({'new_formal_effective_divisor':new_ideals,'endpoint_transition':transition,'global_based_function_local_values':global_values,
                       'status':'complete actual based-CM Miller function on all fixed discs; exact global P-b divisor, endpoint and initial h retained; local leading coefficients are not yet a height'})
    out=args.output or Path('/tmp/p41_cm'+str(args.discriminant)+'_miller_prepared47_checkpoint.json.gz')
    sha,size=write_checkpoint(out,result)
    print('ACTUAL BASED CM LOCAL SLP PASS',args.discriminant,slp['bits_done'],'bits',len(records),'steps','maxe',maxe,size,sha,flush=True)

if __name__=='__main__':main()

