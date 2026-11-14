#!/usr/bin/env python3
"""Actual endpoint scalar primitives for a saved isogeny DAG.

This consumes the independent constant kernels, Gauss--Manin target jets,
actual raw level transport, and scalar primitive atlas.  True CM4 logarithms
are returned as explicit factors for the global height cancellation; they
are never evaluated by inverting a positive-valuation input at precision47^4.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time

P=47
MOD=P**4
ZERO=(0,0)
ONE=(1,0)


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def add(x,y,q=MOD):return ((x[0]+y[0])%q,(x[1]+y[1])%q)
def sub(x,y,q=MOD):return ((x[0]-y[0])%q,(x[1]-y[1])%q)
def scale(x,n,q=MOD):return (x[0]*n%q,x[1]*n%q)
def mul(x,y,q=MOD):return ((x[0]*y[0]-x[1]*y[1])%q,(x[0]*y[1]+x[1]*y[0])%q)
def inv(x,q=MOD):
    t=pow((x[0]*x[0]+x[1]*x[1])%q,-1,q)
    return (x[0]*t%q,-x[1]*t%q)
def power(x,n,q=MOD):
    if n<0:return power(inv(x,q),-n,q)
    y=ONE
    while n:
        if n&1:y=mul(y,x,q)
        x=mul(x,x,q);n//=2
    return y


def evaluate(coeff,t):
    v=ZERO
    for c in reversed(coeff):v=add(mul(v,t),tuple(c))
    return v


def one_plus_rational_power(z,n,d):
    assert all(v%P==0 for v in z)
    v=ONE;c=1;zk=ONE;a=n*pow(d,-1,MOD)%MOD
    for k in range(1,4):
        c=c*(a-k+1)*pow(k,-1,MOD)%MOD
        zk=mul(zk,z);v=add(v,scale(zk,c))
    return v


def truncated_valuation(x):
    v=0
    while v<4 and all(c%P**(v+1)==0 for c in x):v+=1
    return v


def principal_unit_log(x):
    z=sub(x,ONE)
    assert all(c%P==0 for c in z)
    z2=mul(z,z);z3=mul(z2,z)
    return add(sub(z,scale(z2,pow(2,-1,MOD))),scale(z3,pow(3,-1,MOD)))


def integral_linear_factor(B):
    """Weierstrass factor B(t)=(t-alpha)v(t), with only unit inverses."""
    B=[tuple(c) for c in B]
    assert len(B)==5 and truncated_valuation(B[0])>=1 and truncated_valuation(B[1])==0
    derivative=[scale(B[k],k) for k in range(1,5)]
    alpha=ZERO
    for _ in range(2):alpha=sub(alpha,mul(evaluate(B,alpha),inv(evaluate(derivative,alpha))))
    assert evaluate(B,alpha)==ZERO
    v=[ZERO]*4
    v[3]=B[4]
    for k in range(2,-1,-1):v[k]=add(B[k+1],mul(alpha,v[k+1]))
    assert sub(B[0],scale(mul(alpha,v[0]),-1))==ZERO
    assert truncated_valuation(v[0])==0
    return alpha,v


class SavedPrimitives:
    def __init__(self,obj):
        self.ordinary={};self.elliptic={}
        for rec in obj['ordinary_charts']:
            pos={label:k for k,label in enumerate(rec['ordinary_necklace_indices_1based'])}
            self.ordinary[str(rec['reference_j'])]=(rec,pos)
        for rec in obj['elliptic_charts']:
            pos={label:k for k,label in enumerate(rec['indices_1based'])}
            self.elliptic[rec['kind']]=(rec,pos)

    def ordinary_difference(self,key,label,t0,t1):
        rec,pos=self.ordinary[key]
        assert all(v%P==0 for v in t0+t1)
        row=pos[label];s0=s1=ONE;out=ZERO
        for cc in rec['primitive_coefficients_degrees1_to3_mod47_cubed']:
            s0=mul(s0,t0);s1=mul(s1,t1)
            out=add(out,mul(tuple(cc[row][0]),sub(s1,s0)))
        return out

    def elliptic_regular_difference(self,key,label,u0,u1):
        rec,pos=self.elliptic[key];row=pos[label]
        pole=rec['true_logarithmic_pole']
        assert all(v%(P**(2 if pole else 3))==0 for v in u0+u1)
        c=tuple(rec['integrand_coefficients_mod47_cubed'][1 if pole else 0][row][0])
        return mul(c,sub(u1,u0))


def target_parameter(jet,record,t):
    A0,B0=tuple(jet['A'][0]),tuple(jet['B'][0])
    A1,B1=evaluate(jet['A'],t),evaluate(jet['B'],t)
    key=record['reference_key'];c=tuple(record['homothety']);t0=tuple(record['reference_parameter'])
    if key=='0':
        ratio=sub(mul(B1,inv(B0)),ONE)
        Aref=mul(A0,power(c,-4))
        An=mul(mul(A1,power(c,-4)),one_plus_rational_power(ratio,-2,3))
        t1=add(t0,sub(An,Aref))
    else:
        ratio=sub(mul(A1,inv(A0)),ONE)
        Bref=mul(B0,power(c,-6))
        Bn=mul(mul(B1,power(c,-6)),one_plus_rational_power(ratio,-3,2))
        t1=add(t0,sub(Bn,Bref))
    assert all(v%P==0 for v in t1)
    return A1,B1,t1


def integrate_node(key,jet,record,physical_parameters,primitives):
    A0,B0=tuple(jet['A'][0]),tuple(jet['B'][0])
    ref=record['reference_key'];t0=tuple(record['reference_parameter'])
    labels=record['image_indices_1based'];ordinary=primitives.ordinary[ref][1]
    assert len(labels)==len(physical_parameters)
    ordinary_sum=ZERO;elliptic_regular_sum=ZERO;cancelled_log_remainder=ZERO
    poles=[];ordinary_count=cm3_count=0;linear_factor=None
    for row,(t,label) in enumerate(zip(physical_parameters,labels)):
        A1,B1,t1=target_parameter(jet,record,t)
        if label in ordinary:
            ordinary_sum=add(ordinary_sum,primitives.ordinary_difference(ref,label,t0,t1))
            ordinary_count+=1
            continue
        coarse=record['coarse'];ckey=coarse['reference_key'];clabel=coarse['image_indices_1based'][row]
        assert clabel in primitives.elliptic[ckey][1]
        if ckey=='CM3':
            u0=mul(power(A0,3),power(B0,-2));u1=mul(power(A1,3),power(B1,-2))
            cm3_count+=1
        else:
            u0=mul(power(B0,2),power(A0,-3));u1=mul(power(B1,2),power(A1,-3))
            if linear_factor is None:linear_factor=integral_linear_factor(jet['B'])
            alpha,v=linear_factor;vY=evaluate(v,t)
            assert mul(sub(t,alpha),vY)==B1
            remainder=sub(scale(principal_unit_log(mul(vY,inv(v[0]))),2),
                          scale(principal_unit_log(mul(A1,inv(A0))),3))
            cancelled_log_remainder=add(cancelled_log_remainder,remainder)
            poles.append({'source_row_0based':row,'coarse_necklace_index_1based':clabel,
                          'A0':A0,'A1':A1,'B0':B0,'B1':B1,
                          'B0_valuation_at_most4':truncated_valuation(B0),
                          'B1_valuation_at_most4':truncated_valuation(B1),
                          'logarithm':'2*log(B1/B0)-3*log(A1/A0)',
                          'weierstrass_root_alpha':alpha,
                          'unit_v_coefficients_degrees0_to3':v,
                          'source_tY':t,
                          'cancelled_logarithm':'2*log((tY-alpha)/(-alpha))',
                          'logarithmic_remainder_after_global_factor_cancellation':remainder,
                          'unit_factorization_verified':True})
        assert u0==tuple(coarse['invariant_parameter'])
        elliptic_regular_sum=add(elliptic_regular_sum,
                                primitives.elliptic_regular_difference(ckey,clabel,u0,u1))
    total=add(ordinary_sum,elliptic_regular_sum)
    return {'degree':record['degree'],'ordinary_rows':ordinary_count,'CM3_regular_rows':cm3_count,
            'CM4_logarithmic_rows':len(poles),'ordinary_sum':ordinary_sum,
            'elliptic_regular_sum':elliptic_regular_sum,'regular_sum':total,
            'cancelled_log_remainder':cancelled_log_remainder,
            'combined_remainder_after_global_factor_cancellation':add(total,cancelled_log_remainder),
            'complete_tiny_value':total if not poles else None,'CM4_log_factors':poles}


def run(dag_path,jet_path,level_path,primitive_path,source_frame_path,outpath,allow_partial=False,equivalence=None):
    dag,jets,levels,primitive,frame=map(read,[dag_path,jet_path,level_path,primitive_path,source_frame_path])
    assert dag['curve']==jets['curve']==levels['curve']=='source_j9'
    assert jets['constant_dag_sha256']==sha(dag_path)
    if levels['constant_dag_sha256']!=sha(dag_path):
        from p41_dag_equivalence47 import semantic_digest
        proof=read(equivalence)
        assert proof['all_kernel_coefficients_models_line_ids_parent_paths_targets_equal']
        assert levels['constant_dag_sha256']==proof['left_dag_sha256']
        assert sha(dag_path)==proof['right_dag_sha256']
        assert sha(level_path)==proof['level_certificate_sha256']
        assert semantic_digest(dag)==proof['semantic_dag_sha256']
    assert jets['complete']
    assert levels['complete'] or allow_partial
    fam=frame['families'][0]
    assert fam['points_1based']==levels['source_necklace_indices_1based']
    parameters=[tuple(v) for v in fam['actual_parameters'][0]]
    assert all(all(c%P==0 for c in t) for t in parameters)
    atlas=SavedPrimitives(primitive);records={};aggregates={}
    for key,record in levels['nodes'].items():
        records[key]=integrate_node(key,jets['jets'][key],record,parameters,atlas)
    for n,targets in dag['targets'].items():
        keys=[t['node'] for t in targets]
        if any(k not in records for k in keys):continue
        total=ZERO;combined=ZERO;poles=0;ordinary=cm3=0
        for key in keys:
            r=records[key];total=add(total,r['regular_sum'])
            combined=add(combined,r['combined_remainder_after_global_factor_cancellation'])
            poles+=r['CM4_logarithmic_rows'];ordinary+=r['ordinary_rows'];cm3+=r['CM3_regular_rows']
        assert total[1]==0 and combined[1]==0,(n,total,combined)
        aggregates[n]={'target_count':len(keys),'ordinary_rows':ordinary,'CM3_regular_rows':cm3,
                       'CM4_logarithmic_rows':poles,'regular_sum':total,
                       'combined_remainder_after_global_factor_cancellation':combined,
                       'complete_tiny_value':total if not poles else None}
    checks={}
    for n,value in [(1,(890368,0)),(2,(463561,0)),(3,(924161,0))]:
        if str(n) in aggregates:
            actual=aggregates[str(n)]['complete_tiny_value']
            assert actual==value,(n,actual,value)
            checks[str(n)]={'value':actual,'independent_R216_matches':True}
    result={'scope':'Actual source54 endpoint integrals; true CM4 logs explicitly retained',
            'modulus':MOD,'curve':'source_j9','complete_level_input':levels['complete'],
            'complete_regular_parts':levels['complete'],'complete_tiny_indices':
                [int(n) for n,a in aggregates.items() if not a['CM4_logarithmic_rows']],
            'source_sha256':sha(__file__),'constant_dag_sha256':sha(dag_path),
            'quartic_sha256':sha(jet_path),'level_sha256':sha(level_path),
            'equivalence_sha256':sha(equivalence) if equivalence else None,
            'primitive_atlas_sha256':sha(primitive_path),'source_frame_sha256':sha(source_frame_path),
            'source_necklace_indices_1based':fam['points_1based'],
            'nodes':records,'aggregates':aggregates,'independent_checks':checks,
            'boundary':'CM4 integral linear factors must be matched to the R197 global norm factors; only the resulting unit remainder is evaluated; no complete global height asserted'}
    raw=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    Path(outpath).parent.mkdir(parents=True,exist_ok=True)
    Path(outpath).write_bytes(gzip.compress(raw,mtime=0))
    print('endpoint saved',len(records),'nodes',len(aggregates),'indices',
          'pole rows',sum(a['CM4_logarithmic_rows'] for a in aggregates.values()),
          'sha256',sha(outpath),flush=True)
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dag',type=Path,required=True)
    ap.add_argument('--quartic',type=Path,required=True)
    ap.add_argument('--level',type=Path,required=True)
    ap.add_argument('--primitives',type=Path,required=True)
    ap.add_argument('--source-frame',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--allow-partial',action='store_true')
    ap.add_argument('--equivalence',type=Path)
    args=ap.parse_args();start=time.monotonic()
    run(args.dag,args.quartic,args.level,args.primitives,args.source_frame,args.output,args.allow_partial,args.equivalence)
    print('elapsed',round(time.monotonic()-start,3),flush=True)


if __name__=='__main__':main()
