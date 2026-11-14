#!/usr/bin/env python3
"""Independent exact CM-anchor, etale separation and same-component F3 audit."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

P,Q=47,47**4


def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mul(a,b,m):return ((a[0]*b[0]-a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)


def add(a,b,m):return ((a[0]+b[0])%m,(a[1]+b[1])%m)


def inv(a,m):
    u=pow((a[0]*a[0]+a[1]*a[1])%m,-1,m)
    return (a[0]*u%m,-a[1]*u%m)


def dot(a,b,m):
    out=(0,0)
    for x,y in zip(a,b):out=add(out,mul(x,y,m),m)
    return out


def rank(rows):
    a=[[tuple(t%P for t in x) for x in row] for row in rows]
    i=0;pivots=[]
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]!=(0,0)),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i];u=inv(a[i][j],P)
        a[i]=[mul(x,u,P) for x in a[i]]
        for k in range(i+1,len(a)):
            factor=a[k][j]
            a[k]=[add(x,tuple(-t%P for t in mul(factor,y,P)),P) for x,y in zip(a[k],a[i])]
        pivots.append(j);i+=1
        if i==len(a):break
    return i,pivots


def trim(a):
    a=[x%P for x in a]
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def rem(a,b):
    a=trim(a);b=trim(b)
    while len(a)>=len(b) and a!=[0]:
        c=a[-1]*pow(b[-1],-1,P)%P;d=len(a)-len(b)
        for i,x in enumerate(b):a[d+i]=(a[d+i]-c*x)%P
        a=trim(a)
    return a


def pmul(a,b,f):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%P
    return rem(out,f)


def ppow(a,n,f):
    out=[1]
    while n:
        if n&1:out=pmul(out,a,f)
        a=pmul(a,a,f);n//=2
    return out


def pgcd(a,b):
    while trim(b)!=[0]:a,b=b,rem(a,b)
    u=pow(a[-1],-1,P)
    return trim([u*x for x in a])


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ['script-dir','connection','polynomial','support','f2-polynomial','f2-audit','cm-anchors','fixed-support','output']:
        ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();scripts=args.script_dir.resolve();folder=Path(__file__).resolve().parent
    paths={k:getattr(args,k.replace('-','_')) for k in ['connection','polynomial','support','f2-polynomial','f2-audit','cm-anchors','fixed-support']}
    connection,poly,support,f2,f2audit,anchors,fixed=[read(paths[k]) for k in paths]
    disk=poly['disk_id'];assert disk in ['ORD_j39','ORD_j40']
    assert connection['disk_id']==support['source_disk_id']==f2['disk_id']==f2audit['disk_id']==disk
    for name,data in [('p41_CM_ordinary_F3_anchored_connection47.py',connection),('p41_CM_ordinary_F3_anchored_polynomial47.py',poly)]:
        source=folder/name;assert data['source_sha256']==sha(source);paths[name]=source
    def edge(data,path):
        got=[v for k,v in data['input_sha256'].items() if Path(k).name==Path(path).name]
        assert got and set(got)=={sha(path)},path
    edge(poly,args.connection);edge(poly,args.f2_polynomial);edge(poly,args.f2_audit)
    edge(connection,args.support);edge(connection,args.fixed_support);edge(connection,args.cm_anchors)
    edge(f2audit,args.f2_polynomial)
    atlas_path=scripts/'data/p41_ordinary_rational_atlas47.json.gz'
    globals_path=scripts/'data/p41_global_qc_polynomials47_complete.json.gz'
    atlas,globals=read(atlas_path),read(globals_path);paths.update(atlas=atlas_path,global_forms=globals_path)
    chart=next(c for c in atlas['charts'] if disk in c['disk_ids']);row=chart['disk_ids'].index(disk)
    point=chart['W_coefficients_0to3'][0][row]
    WT=support['W_coefficients_ascending_in_kernel_root'];assert len(WT)==4
    b=next(p['W_mod47four'] for p in fixed['groups']['Z0fix']['points'] if p['is_basepoint_b'])
    v=fixed['groups']['v']['points'][0]['W_mod47four']
    separation={}
    for name,x in [('P',point),('b',b)]:
        rr,cc=rank(WT+[x]);assert rr==5;separation[name]={'rank':rr,'pivot_columns_0based':cc}
    qT=[x[0] for x in connection['actual_connections']['T3C']['denominator_linear_coefficients_mod47four']]
    assert all(dot(x,qT,Q)==(0,0) for x in WT+[b,v])
    qP=dot(point,qT,Q);assert (qP[0]*qP[0]+qP[1]*qP[1])%P
    AA,BB=support['source_curve'];f=support['kernel_polynomial_ascending']
    assert f==[-AA*AA*pow(3,-1,Q)%Q,4*BB%Q,2*AA%Q,0,1]
    f=trim(f);xx=[0,1]
    assert ppow(xx,P**4,f)==xx
    xx2=ppow(xx,P**2,f);xx2 += [0]*(2-len(xx2));xx2[1]=(xx2[1]-1)%P
    assert pgcd(f,trim(xx2))==[1]
    assert support['raw_level_determinant_mod41']==support['raw_target_pairing_exponent']==3
    assert support['complete_actual_T3_support'] and support['kernel_factor_degrees_mod47']==[[4,1]]
    anchor=next(a for a in anchors['three_ordinary_CM_anchors'] if a['disk_id']==disk)
    idx=globals['direction_indices'].index(3);direction=globals['directions'][idx]
    assert direction['F_Tn_coefficient']==9 and direction['F_identity_coefficient']==2
    based=direction['based_C'];aCM=anchor['actual_CM_C_cyclic_coordinates_mod47cubed']
    value=based['constant_mod47four']+sum(x*y for x,y in zip(based['linear_vector_mod47four'],aCM))
    offset=0
    for block in based['quadratic_blocks_mod47four']:
        d=len(block)
        value+=sum(aCM[offset+i]*block[i][j]*aCM[offset+j] for i in range(d) for j in range(d))
        offset+=d
    assert offset==54;value%=Q
    labels=globals['component_order'];assert labels==[0,3,28,32]
    targets=[x['QC_defect_target_mod47four'][idx] for x in globals['component_vectors']]
    ycm=anchor['rescaled_parameter_y_of_CM_point_mod47cubed'];label=anchor['bad_component_at41']
    scaled=(value-targets[labels.index(label)])%Q
    assert scaled==anchor['local_global_section_heights_at_CM_point_by_global_reciprocity'][idx]
    local_cm=scaled*pow(800,-1,Q)%Q
    recorded=poly['known_CM_anchor'];assert recorded==connection['known_CM_anchor']
    assert recorded['canonical_sigma_F3_local_height_mod47four']==local_cm
    cmW=[];zcm=47*ycm
    for j in range(73):
        cmW.append([sum(chart['W_coefficients_0to3'][k][row][j][part]*pow(zcm,k,Q) for k in range(4))%Q for part in range(2)])
    assert [cmW]==anchor['physical_CM_W_in_chart_frame_mod47four']
    height=poly['canonical_local_sigma_F3_height_coefficients_0to3_in_y_mod47four']
    differential=[]
    for k in range(3):
        c=[sum(v[k][0][0][part] for v in poly['differential_pieces_coefficients_mod47cubed'].values())%(47**3) for part in range(2)]
        assert c[1]==0 and [[c]]==poly['local_differential_coefficients_0to2_in_z_mod47cubed'][k]
        differential.append(c[0])
    assert height[1:]==[c*47**(k+1)*pow(k+1,-1,Q)%Q for k,c in enumerate(differential)]
    assert sum(c*pow(ycm,k,Q) for k,c in enumerate(height))%Q==local_cm
    globalpoly=next(x for x in anchor['global_polynomials_at_rational_center'] if x['n']==3)['coefficients_0to4_in_y_mod47four']
    assert globalpoly==poly['global_F3_coefficients_0to4_in_y_mod47four']
    qc=[(globalpoly[k]-800*(height[k] if k<4 else 0))%Q for k in range(5)]
    assert qc==poly['actual_QC_F3_coefficients_0to4_in_y_mod47four']
    assert all(x%P==0 for x in qc) and targets==poly['F3_bad_targets_in_same_component_order']
    f2co=f2['actual_QC_F2_coefficients_0to4_in_y_mod47four'];survivors=[];checks=[]
    candidates=f2audit['simple_single_F2_root_candidates_to_available_precision']
    assert len(candidates)==2 and ycm in [c['y_mod47cubed'] for c in candidates]
    for candidate in candidates:
        y=candidate['y_mod47cubed'];assert sum(c*pow(y,k,Q) for k,c in enumerate(f2co))%Q==0
        assert candidate['derivative_mod47']%P
        f3value=sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q
        rowchecks=[]
        for label,target in zip(labels,targets):
            diff=(f3value-target)%Q;rowchecks.append({'label':label,'difference_mod47four':diff})
            if diff==0:survivors.append({'y_mod47cubed':y,'bad_component_label':label})
        checks.append({'y_mod47cubed':y,'QC_F3_value_mod47four':f3value,'component_tests':rowchecks})
    assert survivors==poly['remaining_F2_F3_candidate_and_component_pairs']
    assert all(s['y_mod47cubed']==ycm for s in survivors)
    assert {'y_mod47cubed':ycm,'bad_component_label':anchor['bad_component_at41']} in survivors
    out={'disk_id':disk,'input_sha256':{str(p):sha(p) for p in paths.values()},
         'irreducible_quartic_kernel_verified_by_Frobenius_and_gcd':True,
         'actual_four_target_span_separation_independently_reduced_mod47':separation,
         'new_T3_denominator_all_pole_constraints_and_center_unit_verified':True,
         'all73_true_CM_coordinate_transport_independently_verified':True,
         'CM_global_pairing_recomputed_from_actual54_coordinates':value,
         'CM_scaled_height':scaled,'CM_height_after_exact_division_by800':local_cm,
         'local_height_polynomial':height,'local_derivative':differential,
         'global_polynomial':globalpoly,'QC_polynomial':qc,
         'F2_candidate_checks':checks,'remaining_same_component_pairs':survivors,
         'extra_F2_root_excluded_in_all_four_components':True,
         'known_CM_height_is_an_input_not_an_independent_local_Norm_check':True,
         'source_sha256':sha(__file__)}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('PASS independent CM anchored F3',disk,'extra F2 root excluded;remaining',survivors,'SHA',sha(args.output))


if __name__=='__main__':main()
