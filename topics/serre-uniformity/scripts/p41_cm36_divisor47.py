#!/usr/bin/env python3
"""Actual T3 B_minus4 with both CM(-36) branches and its two-function transport."""
import argparse
import gc
import gzip
import hashlib
import json
from pathlib import Path
import random
import resource
import sys
import time


def digest(data):return hashlib.sha256(json.dumps(data,separators=(',',':')).encode()).hexdigest()


def prepare_chart(M0,omitted,r):
    assert all(M0['tau'][j] in omitted for j in omitted)
    keep=[j for j in range(820) if j not in omitted];assert len(keep)>630
    label={j:i for i,j in enumerate(keep)}
    M={k:v for k,v in M0.items() if k not in ['B','WB','AB']}
    M['W']=r.rows(M0['W'],keep);M['tau']=[label[M0['tau'][j]] for j in keep]
    M['V2'],M['P2'],cc2,C2=r.normalize(r.rows(M0['V2'],keep),199)
    M['V3'],M['P3'],cc3,C3=r.normalize(r.rows(M0['V3'],keep),325)
    assert cc2==list(range(199)) and cc3==list(range(325))
    C2i=r.inverse_matrix(C2);C3i=r.inverse_matrix(C3)
    M['A2']=r.mm(r.mm(C2i,M0['A2']),r.conjugate(C2))
    M['A3']=r.mm(r.mm(C3i,M0['A3']),r.conjugate(C3))
    for V,A in [(M['W'],M['A1']),(M['V2'],M['A2']),(M['V3'],M['A3'])]:
        assert r.equal(r.mm(V,A),r.conjugate(r.rows(V,M['tau'])))
    metadata={'omitted_evaluation_rows_1based':[j+1 for j in sorted(omitted)],
      'retained_evaluation_count':len(keep),'V2_change_sha256':digest(r.to_json(C2)),
      'V3_change_sha256':digest(r.to_json(C3)),
      'faithfulness':'retained count>5*degL=630; all cleared multiplication identities are global'}
    return M,C2,C2i,C3,metadata


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--cm36',type=Path,default=Path('/tmp/p41_cm36_hecke47_raw.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_cm36_divisor47_checkpoint.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_cm4_divisor47 import kernel
    from p41_hecke3_hessian47 import section_jets,projective_rows
    from p41_poincare_miller47 import addflip_with_section
    from p41_formal47_multiply import write_checkpoint,point_hash
    started=time.monotonic();raw=args.cm36.read_bytes();cm=json.loads(gzip.decompress(raw))
    assert cm['status'].startswith('all4 actual cyclic3-isogenies')
    sources,hashes=load_sources(folder/'data')
    assert cm['source_sha256']['p41_makdisi47_certificate.json.gz']==hashes['p41_makdisi47_certificate.json.gz']
    assert cm['source_sha256']['p41_cm4_divisor47_certificate.json']==hashes['p41_cm4_divisor47_certificate.json']
    M0=make_model(sources);divs=sources[1]
    K1=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    fc=r.mm(K1,r.column(divs['canonical_coefficients']))
    KI=r.from_json(kernel(199,divs['K_rank_columns_1based'],divs['K_free_columns_1based'],divs['K_kernel_block']))
    original_keys=projective_rows(M0['W'],r);index={key:j for j,key in enumerate(original_keys)}
    assert len(index)==820
    all_target_keys=set();omitted=set();branch_points=[];records=[]
    for record in cm['records']:
        W=r.from_json(record['weight2_values']);keys=projective_rows(W,r)
        assert None not in keys and len(set(keys))==20 and not set(keys)&all_target_keys
        all_target_keys.update(keys)
        intersection=[index[k] for k in keys if k in index];omitted.update(intersection)
        fz=r.mm(W,fc);assert np.all(r.units(fz)), 'Actual K_f meets this CM36 branch; retain multiplicities explicitly'
        V2,V3=section_jets([W],sources,M0,r);V2=V2[0]
        restriction=r.mm(V2,KI);rr,cc=r.rank_pivots(restriction);assert len(rr)==20
        ker,free,block=r.kernel_from_rows(r.rows(restriction,rr),rr,cc)
        assert r.iszero(r.mm(restriction,ker))
        K=r.mm(KI,ker);K,piv,cols,change=r.normalize(K,73);assert cols==list(range(73))
        A=r.rows(r.mm(M0['A2'],r.conjugate(K)),piv)
        assert r.equal(r.mm(K,A),r.mm(M0['A2'],r.conjugate(K)))
        assert r.equal(r.mm(A,r.conjugate(A)),r.eye(73)) and r.iszero(r.mm(V2,K))
        tau=[i-1 for i in record['target_frobenius_permutation_1based']]
        assert r.equal(r.mm(V2,M0['A2']),r.conjugate(r.rows(V2,tau)))
        branch_points.append((K,A))
        records.append({'branch':record['branch'],'j_invariant':record['j_invariant'],
          'actual_degree':20,'canonical_values':r.to_json(fz),
          'restriction_rank':20,'restriction_rank_columns_1based':[j+1 for j in cc],
          'restriction_kernel_block_sha256':digest(r.to_json(block)),
          'point_coordinates':r.to_json(K),'point_frobenius':r.to_json(A),'point_sha256':point_hash(K,A),
          'actual_class':'Z_branch-D; effective representative is Z_branch+K_f',
          'residual_intersection_rows_1based':[j+1 for j in intersection]})
        print('ACTUAL CM36 BRANCH IDEAL PASS',record['branch'],'residual_E0_intersections',len(intersection),flush=True)
    assert len(all_target_keys)==40 and len(omitted)==20
    M,C2,C2i,C3,chart=prepare_chart(M0,omitted,r)
    original_A2,original_A3=M0['A2'],M0['A3']
    P0,A0=branch_points[0];P1,A1=branch_points[1]
    P0,P1=r.mm(C2i,P0),r.mm(C2i,P1)
    rng=random.Random(4104719003)
    N,AN,s1,rec1=addflip_with_section(P0,A0,P1,A1,M,rng,'CM36 negative total',r)
    T,AT,s2,rec2=addflip_with_section(N,AN,N,AN,M,rng,'Actual T3 B4',r,same=True)
    Norig,Torig=r.mm(C2,N),r.mm(C2,T);s1,s2=r.mm(C3,s1),r.mm(C3,s2)
    for point,action in [(Norig,AN),(Torig,AT)]:
        assert r.equal(r.mm(original_A2,r.conjugate(point)),r.mm(point,action))
    for section in [s1,s2]:assert r.equal(r.mm(original_A3,r.conjugate(section)),section)
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
      'CM36_source_sha256':hashlib.sha256(raw).hexdigest(),
      'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'branches':records,'working_chart':chart,'actual_divisor_identity':'T3 Z_minus4=2*(Z_branch0+Z_branch1); T3D=4D',
      'operation_plan':['N=-(B_branch0+B_branch1)','T3B=-2N'],
      'negative_total_point_coordinates':r.to_json(Norig),'negative_total_point_frobenius':r.to_json(AN),
      'negative_total_point_sha256':point_hash(Norig,AN),'add_record':rec1,'double_record':rec2,
      'T3B_point_coordinates':r.to_json(Torig),'T3B_point_frobenius':r.to_json(AT),
      'T3B_point_sha256':point_hash(Torig,AT),
      'principal_transport':{'first_cubic_coefficients':r.to_json(s1),'second_cubic_coefficients':r.to_json(s2),
        'base_linear_coefficients':r.to_json(fc),'actual_function':'h_T3=(s2/f0^3)/(s1/f0^3)^2=s2*f0^3/s1^2',
        'actual_divisor':'A_T3B - T3(A_B4) = A_T3B - 2*(Z_branch0+Z_branch1-2D)'},
      'int64_accumulation_bound':2*820*(r.Q-1)**2,
      'status':'actual40 CM36 points, full ideals, exact T3B and complete principal transport; no local or global height claimed'}
    sha,size=write_checkpoint(args.output,result)
    print('ACTUAL CM36 DIVISOR AND T3B PASS',point_hash(Torig,AT),'bytes',size,'sha',sha,
       'seconds',round(time.monotonic()-started,2),'peak_MiB',round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,2),flush=True)


if __name__=='__main__':main()
