#!/usr/bin/env python3
"""Independent scalar, actual-point, second-kind and Hensel audit of R318."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

Q=47**4
q=47**3


def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mul(x,y,m=Q):
    return [(x[0]*y[0]-x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0])%m]


def dot(x,y,m=Q):
    a=[mul(u,v,m) for u,v in zip(x,y)]
    return [sum(z[0] for z in a)%m,sum(z[1] for z in a)%m]


def inv(x):
    a=pow((x[0]*x[0]+x[1]*x[1])%Q,-1,Q)
    return [x[0]*a%Q,-x[1]*a%Q]


def scalar(x):
    assert len(x)==len(x[0])==1 and x[0][0][1]==0
    return x[0][0][0]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ['script-dir','center','polynomial','anchor','connection-source','polynomial-source','support','output']:
        ap.add_argument('--'+n,type=Path,required=True)
    args=ap.parse_args()
    data=args.script_dir.resolve()/'data'
    paths={k:getattr(args,k) for k in ['center','polynomial','anchor','connection_source','polynomial_source','support']}
    C,P,A=map(read,[args.center,args.polynomial,args.anchor])
    assert C['source_sha256']==sha(args.connection_source)
    assert P['source_sha256']==sha(args.polynomial_source)
    assert C['disk_id']==P['disk_id']==A['disk_id']=='SS_j10_05'
    for target in [args.center,args.anchor]:
        matches=[v for k,v in P['input_sha256'].items() if Path(k).name==target.name]
        assert matches and set(matches)=={sha(target)}
    atlas=read(data/'p41_rational_SS_residue_atlas47_complete.json.gz')
    ch=next(c for c in atlas['charts'] if P['disk_id'] in c['disk_ids'])
    row=ch['disk_ids'].index(P['disk_id'])
    frame=[v[0] for v in ch['frame']]
    W0=ch['W_coefficients_0to3'][0][row]
    assert C['actual_connections']['C']['finite_pole_coordinates_fc_normalized'][0]==W0
    assert dot(W0,frame)==[1,0]
    z=A['actual_original_chart_z_mod47four'];y=A['actual_original_y_mod47cubed']
    assert z==47*y==4043034
    Wcm=[[sum(ch['W_coefficients_0to3'][k][row][i][part]*pow(z,k,Q) for k in range(4))%Q
          for part in range(2)] for i in range(73)]
    assert Wcm==A['actual_W_in_original_SS_atlas_frame_mod47four']
    assert Wcm==A['actual_fc_normalized_W_mod47four']
    second=read(data/'p41_rational_SS_second_kind_integrals47_complete.json.gz')
    s=next(v for v in second['rational_SS_center_integrals'] if v['disk_id']==P['disk_id'])
    support=read(args.support)
    assert s['vertex_0based']==support['source_vertex_0based']
    assert C['actual_gradients_original_nu_mod47cubed']['C']==[s['C_original_nu_coordinates_mod47cubed']]
    assert support['source_disk_id']==P['disk_id']
    assert support['actual_source_W_fc_normalized']==W0
    matches=[v for k,v in C['input_sha256'].items() if Path(k).name==args.support.name]
    assert matches and set(matches)=={sha(args.support)}
    targets=support['actual_T2_targets_fc_normalized']
    assert targets==C['actual_T2_target_coordinates_fc_normalized']
    graph=read(data/'p41_SS_Hecke_graph47.json.gz')
    assert graph['adjacency']['2'][support['source_vertex_0based']]==support['actual_target_vertices_0based']
    qt=[v[0] for v in C['actual_connections']['T2C']['denominator_linear_coefficients_mod47four']]
    assert all(dot(W,qt)==[0,0] for W in targets)
    qp=dot(W0,qt)
    assert (qp[0]**2+qp[1]**2)%47
    pieces=P['differential_pieces_coefficients_mod47cubed']
    differential=[scalar(x) for x in P['local_differential_coefficients_0to2_in_z_mod47cubed']]
    for k,d in enumerate(differential):
        assert sum(scalar(v[k]) for v in pieces.values())%q==d
    lam=P['canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four']
    assert lam[1:]==[d*47**(k+1)*pow(k+1,-1,Q)%Q for k,d in enumerate(differential)]
    a2=next(v for v in A['all53_local_height_anchors_by_global_reciprocity'] if v['n']==2)
    assert a2['same_component_QC_target_mod47four']==0
    assert sum(c*pow(y,k,Q) for k,c in enumerate(lam))%Q==a2['canonical_local_sigma_height_mod47four']==85446
    assert 800*a2['canonical_local_sigma_height_mod47four']%Q==a2['global_value_mod47four']
    aa=P['actual_cyclic_C_coefficients_0to3_in_y_mod47cubed']
    assert [sum(aa[k][i]*pow(y,k,q) for k in range(4))%q for i in range(54)]==A['actual_C_w_cyclic_coordinates_mod47cubed']
    known=read(data/'p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz')
    rec=next(x for x in known['actual_113_rational_disk_global_polynomials'] if x['disk_id']==P['disk_id'])
    G=next(f for f in rec['global_polynomials'] if f['n']==2)['coefficients_0to4_in_y_mod47four']
    assert G==P['global_F2_coefficients_0to4_in_y_mod47four']
    qc=[(g-800*(lam[k] if k<4 else 0))%Q for k,g in enumerate(G)]
    assert qc==P['actual_QC_F2_coefficients_0to4_in_y_mod47four']
    assert all(v%47==0 for v in qc)
    divided=[v//47 for v in qc]
    reduction=[v%47 for v in divided]
    roots=[t for t in range(47) if sum(v*pow(t,k,47) for k,v in enumerate(reduction))%47==0]
    assert roots==P['residual_QC_roots']==[2,12]
    lifts=[]
    for t in roots:
        derivative=sum(k*v*pow(t,k-1,47) for k,v in enumerate(divided) if k)%47
        assert derivative
        value=t;mod=47;digits=[t]
        for _ in range(2):
            newmod=47*mod
            f=sum(v*pow(value,k,newmod) for k,v in enumerate(divided))%newmod
            assert f%mod==0
            digit=-(f//mod)*pow(derivative,-1,47)%47
            value+=mod*digit;mod=newmod;digits.append(digit)
        assert sum(v*pow(value,k,q) for k,v in enumerate(divided))%q==0
        lifts.append({'y_mod47cubed':value,'z_mod47four':47*value,'y_base47_digits':digits,'derivative_mod47':derivative})
    assert y in [v['y_mod47cubed'] for v in lifts]
    assert sum(v*pow(y,k,Q) for k,v in enumerate(qc))%Q==0
    for name in ['p41_rational_SS_residue_atlas47_complete.json.gz','p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_Hecke_graph47.json.gz','p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz']:
        paths[name]=data/name
    out={'result':'R318','disk_id':P['disk_id'],'all73_actual_CM_coordinates':True,
         'actual54_center_nu_equal_R247':True,'all_three_actual_T2_targets_and_pole_constraints':True,
         'all54_actual_CM_Abel_coordinates':True,'same_global_polynomial_as_R237':True,
         'exact_CM_reciprocity_height_and_800_scale':True,'CM_y_mod47cubed':y,
         'local_polynomial':lam,'global_polynomial':G,'QC_polynomial':qc,
         'QC_div47_reduction':reduction,'residual_roots':roots,
         'simple_single_F2_root_candidates_to_available_precision':lifts,
         'scope':'Independent exact arithmetic and actual saved point checks; no duplicated moving RR rank or Hecke interpolation computation.',
         'input_sha256':{str(p):sha(p) for p in paths.values()},'source_sha256':sha(__file__)}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('PASS R318 actual SS anchor/nu/T2/54Abel/scalar audit',lifts,'SHA',sha(args.output))


if __name__=='__main__':
    main()
