#!/usr/bin/env python3
"""Evaluate the actual Miller SLP on CM discs by exact Weierstrass cancellation."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--jets',type=Path,default=Path('/tmp/p41_cm_quadratic_jets47_raw.json.gz'))
    p.add_argument('--miller',type=Path,default=Path('/tmp/p41_poincare_miller_jets47_rolling.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_miller_cm_prepared47_checkpoint.json.gz'))
    args=p.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_hecke3_hessian47 import section_jets
    from p41_weierstrass_unit47 import prepare_unit
    from p41_formal47_multiply import write_checkpoint
    from p41_poincare_norms47 import pair_mul,pair_inverse
    sources,hashes=load_sources(args.script_dir/'data');M=make_model(sources)
    data,jsha=read(args.jets);slp,ssha=read(args.miller)
    assert data['source_sha256']==slp['source_sha256']==hashes
    labels=[a['label'] for a in data['records']];n=len(labels);order=data['order']
    W=[r.from_json([rec['normalized_weight2_coefficients'][k] for rec in data['records']]) for k in range(order+1)]
    V2,V3=section_jets(W,sources,M,r)
    fp=[]
    for j in range(n):
        x=r.rows(W[0],[j]);fp.append(r.equal(r.mm(x,M['A1']),r.conjugate(x)))
    def prepared(values,point,column=0):
        coefficients=[[int(v[0][point,column]),int(v[1][point,column])] for v in values]
        if fp[point]:assert all(b==0 for a,b in coefficients),'rational germ failed Frobenius descent'
        return prepare_unit(coefficients,precision=4)
    def add(a,b):return [(a[0]+b[0])%r.Q,(a[1]+b[1])%r.Q]
    def neg(a):return [(-a[0])%r.Q,(-a[1])%r.Q]
    def product(a,b):
        out=[[0,0] for _ in range(len(a)+len(b)-1)]
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]=add(out[i+j],pair_mul(x,y))
        return out
    def divide(a,b):
        assert a[-1]==b[-1]==[1,0] and len(a)>=len(b)
        rem=[x[:] for x in a];quo=[[0,0] for _ in range(len(a)-len(b)+1)]
        for k in range(len(quo)-1,-1,-1):
            c=rem[k+len(b)-1];quo[k]=c[:]
            for j,x in enumerate(b):rem[k+j]=add(rem[k+j],neg(pair_mul(c,x)))
        assert all(x==[0,0] for x in rem),'Shared actual divisor factors failed exact cancellation'
        assert quo[-1]==[1,0] and all(a%47==b%47==0 for a,b in quo[:-1])
        return quo
    cf=r.mm(M['B'],r.column(sources[3]['negative_flip_section_seeds_and_coefficients'][0][1]))
    nv=[r.mm(v,cf) for v in V2];negative=[prepared(nv,j) for j in range(n)]
    assert all(a['degree']==0 for a in negative)
    minusU=[pair_inverse(a['unit_constant']) for a in negative]
    coefficients=[]
    for step in slp['steps']:
        cf=step['principal_section_coefficients']
        assert hashlib.sha256(json.dumps(cf,separators=(',',':')).encode()).hexdigest()==step['principal_coefficient_sha256']
        coefficients.append(r.from_json(cf))
    allcf=r.hcat(*coefficients);values=[r.mm(v,allcf) for v in V3]
    currentW=[[[1,0]] for _ in range(n)];currentU=[[1,0] for _ in range(n)];sign=1;records=[];maxdegree=0
    for k,step in enumerate(slp['steps']):
        allprepared=[prepared(values,j,k) for j in range(n)]
        for j,a in enumerate(allprepared):
            maxdegree=max(maxdegree,a['degree']);wp=currentW[j]
            if step['operation']=='double':
                denominator=product(wp,wp);u=pair_mul(currentU[j],currentU[j])
            else:
                assert step['operation']=='add';denominator=wp;u=pair_mul(currentU[j],[1,0] if sign==1 else minusU[j])
            currentW[j]=divide(a['weierstrass_coefficients'],denominator)
            currentU[j]=pair_inverse(pair_mul(u,a['unit_constant']))
        sign=-sign;assert sign==step['sign']
        records.append({'step_index_1based':k+1,'principal_coefficient_sha256':step['principal_coefficient_sha256'],
                        'unit_constants':[a['unit_constant'] for a in allprepared],
                        'nonunit_points':[{'point_index_1based':j+1,'degree':a['degree'],
                                           'weierstrass_coefficients':a['weierstrass_coefficients'],
                                           'required_last_jet':a['required_last_jet']}
                                          for j,a in enumerate(allprepared) if a['degree']]})
    # Identify the complete current effective divisor directly from its actual ideal.
    point=r.from_json(slp['point_coordinates']);vv=[r.mm(v,point) for v in V2];witnesses=[]
    for j in range(n):
        choices=[]
        for c in range(point[0].shape[1]):
            e=next((k for k,v in enumerate(vv) if r.units(r.rows(r.cols(v,[c]),[j]))[0,0]),None)
            if e is not None:choices.append((e,c))
        assert choices;e,c=min(choices)
        # The ideal generators need not themselves be rational; prepare directly.
        co=[[int(v[0][j,c]),int(v[1][j,c])] for v in vv]
        a=prepare_unit(co,precision=4,degree=e)
        assert a['weierstrass_coefficients']==currentW[j]
        witnesses.append({'column_1based':c+1,'degree':e,'weierstrass_coefficients':currentW[j]})
    base,bsha=read(Path('/tmp/p41_hecke3_abel_bases_checkpoint.json.gz'))
    endpoint,esha=read(Path('/tmp/p41_miller_endpoint47_certificate.json'))
    epdiv,dsha=read(Path('/tmp/p41_cm_endpoint_divisors47_certificate.json.gz'))
    assert base['source_sha256']==endpoint['source_sha256']==epdiv['source_sha256']==hashes
    assert epdiv['jet_source_sha256']==jsha
    assert endpoint['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz']==bsha
    trans=endpoint['transport_function'];v1=r.from_json(base['families'][0]['v_coefficients'])
    components={'new': [r.mm(v,r.from_json(trans['new_section_coefficients'])) for v in V2],
                'old': [r.mm(v,r.from_json(trans['old_section_coefficients'])) for v in V2],
                'v1': [r.mm(v,v1) for v in W]}
    oldE=epdiv['records'][2]['points'];newE=epdiv['records'][3]['points'];transition=[]
    for j in range(n):
        a={k:prepared(values,j) for k,values in components.items()}
        numerator=product(a['new']['weierstrass_coefficients'],oldE[j]['weierstrass_coefficients'])
        denominator=product(product(a['old']['weierstrass_coefficients'],a['v1']['weierstrass_coefficients']),newE[j]['weierstrass_coefficients'])
        assert numerator==denominator,'Endpoint shared-divisor cancellation failed'
        unit=pair_mul(a['new']['unit_constant'],pair_inverse(pair_mul(a['old']['unit_constant'],a['v1']['unit_constant'])))
        transition.append({'point_label':labels[j],'components':a,'unit_constant':unit})
    complete=slp['bits_done']==304
    finalvalues=None;actualnorms=None
    if complete:
        assert sign==1 and all(a['local_effective_degree']==0 for a in newE)
        assert all(currentW[j]==oldE[j]['weierstrass_coefficients'] for j in range(n))
        finalvalues=[pair_mul(currentU[j],pair_inverse(transition[j]['unit_constant'])) for j in range(n)]
        def norm(indices):
            z=[1,0]
            for j in indices:z=pair_mul(z,finalvalues[j])
            assert z[1]==0
            return z[0]
        actualnorms={'at_Pminus3':finalvalues[0],'at_Pminus12':finalvalues[1],'at_Pminus7':finalvalues[2],
                     'on_Q2':norm([2,2]+list(range(3,23))),
                     'T2_at_Pminus12':norm([0,23,24]),'T2_at_Pminus7':norm([2,2,25])}
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
            'input_sha256':{'jets':jsha,'miller':ssha,'endpoint':esha,'endpoint_divisors':dsha,'base':bsha},
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'weierstrass_source_sha256':hashlib.sha256((args.script_dir/'p41_weierstrass_unit47.py').read_bytes()).hexdigest(),
            'labels':labels,'F47_rational_labels':[labels[j] for j in range(n) if fp[j]],
            'bits_done':slp['bits_done'],'steps_done':len(records),'maximum_residual_degree':maxdegree,
            'negative_B':negative,'steps':records,'current_effective_divisor_witnesses':witnesses,
            'current_unit_constants':currentU,'endpoint_transition':transition,
            'complete_new_frame_values':finalvalues,'complete_actual_norms':actualnorms,
            'nonunit_divisions':0,
            'status':('complete actual SLP values and CM norms after exact whole-disc cancellation' if complete else
                      'partial actual SLP unit transport; every shared factor cancels and the current ideal matches; full CM values await the304-bit chain')}
    sha,size=write_checkpoint(args.output,result)
    print('ACTUAL CM WEIERSTRASS SLP PASS',slp['bits_done'],'bits',len(records),'steps maxe',maxdegree,
          'complete',complete,'bytes',size,'sha',sha,flush=True)
    if complete:print(actualnorms,flush=True)

if __name__=='__main__':main()
