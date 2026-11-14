#!/usr/bin/env python3
"""Exact CM(-27) SS point and all53 reciprocal height anchors from T3(b)=b+3v."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

Q=47**4;Q3=47**3


def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%Q,(x[0]*y[1]+x[1]*y[0])%Q)


def dot(x,y):
    values=[mul(a,b) for a,b in zip(x,y)]
    return (sum(x[0] for x in values)%Q,sum(x[1] for x in values)%Q)


def inv(x):
    h=pow((x[0]*x[0]+x[1]*x[1])%Q,-1,Q)
    return (x[0]*h%Q,-x[1]*h%Q)


def fieldmul(a,b,descending):
    d=len(descending)-1;f=list(reversed(descending));assert f[-1]==1
    out=[0]*(2*d-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%Q
    for k in range(2*d-2,d-1,-1):
        for j in range(d):out[k-d+j]=(out[k-d+j]-out[k]*f[j])%Q
    return out[:d]


def globalvalue(direction,aa):
    b=direction['based_C'];out=b['constant_mod47four']+sum(x*y for x,y in zip(b['linear_vector_mod47four'],aa))
    offset=0
    for block in b['quadratic_blocks_mod47four']:
        d=len(block)
        out+=sum(aa[offset+i]*block[i][j]*aa[offset+j] for i in range(d) for j in range(d))
        offset+=d
    assert offset==54
    return out%Q


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir','fixed-support','output']:ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();data=args.script_dir.resolve()/'data';inputs={}
    def load(p):inputs[str(p)]=sha(p);return read(p)
    fixed=load(args.fixed_support)
    globals=load(data/'p41_global_qc_polynomials47_complete.json.gz')
    known=load(data/'p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz')
    atlas=load(data/'p41_rational_SS_residue_atlas47_complete.json.gz')
    tiny=load(data/'p41_all129_tiny_Abel47_complete.json.gz')
    group=fixed['groups']['v'];assert len(group['points'])==1
    point=group['points'][0];W=point['W_mod47four']
    j=-12288000;component=j%41;assert component==28
    disk='SS_j9_11'
    F3=next(f for f in globals['directions'] if f['n']==3)
    assert F3['F_Tn_coefficient']==9 and F3['F_identity_coefficient']==2
    rv=[];r3=[];field_records=[]
    for k,(field,F) in enumerate(zip(globals['fields'],F3['F_field_coefficients_ascending_mod47four'])):
        dim=len(field['factor_descending'])-1
        assert len(F)==dim
        T=[x*pow(9,-1,Q)%Q for x in F];T[0]=(T[0]-2*pow(9,-1,Q))%Q
        Tminus1=list(T);Tminus1[0]=(Tminus1[0]-1)%Q
        rminus3=field['r_minus3'];v=[x*pow(3,-1,Q)%Q for x in fieldmul(Tminus1,rminus3,field['factor_descending'])]
        left=fieldmul(T,rminus3,field['factor_descending'])
        assert left==[(x+3*y)%Q for x,y in zip(rminus3,v)]
        r3+=rminus3;rv+=v
        field_records.append({'factor_descending':field['factor_descending'],'T3_ascending_mod47four':T,'r_v_ascending_mod47four':v,'T3_r_minus3_equals_r_minus3_plus3r_v':True})
    av=[(x-y)*pow(20,-1,Q3)%Q3 for x,y in zip(rv,r3)];assert len(av)==54
    chart=next(c for c in atlas['charts'] if disk in c['disk_ids']);row=chart['disk_ids'].index(disk)
    frame=[x[0] for x in chart['frame']];coordinate=[x[0] for x in chart['coordinate']]
    scale=inv(dot(W,frame));Wp=[list(mul(x,scale)) for x in W]
    base=chart['rational_coordinate_at_center_mod47four'][row]
    assert isinstance(base,int)
    zz=dot(Wp,coordinate);assert zz[1]==0
    z=(zz[0]-base)%Q;assert z%47==0;y=z//47
    recovered=[[sum(chart['W_coefficients_0to3'][k][row][j][part]*pow(z,k,Q) for k in range(4))%Q for part in range(2)] for j in range(73)]
    assert recovered==Wp
    tc=next(c for c in tiny['charts'] if disk in c['disk_ids']);ti=tc['disk_ids'].index(disk)
    assert tc['origin_chart_0based']==chart['chart_0based']
    center=next(r for r in known['actual_113_rational_disk_global_polynomials'] if r['disk_id']==disk)
    delta=[sum(tc['cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed'][k-1][ti][c]*pow(y,k,Q3) for k in range(1,4))%Q3 for c in range(54)]
    actual=[(x+d)%Q3 for x,d in zip(center['actual_center_C_cyclic_coordinates_mod47cubed'],delta)]
    assert actual==av
    labels=globals['component_order'];assert labels==[0,3,28,32];ci=labels.index(component)
    heights=[]
    for direction in globals['directions']:
        value=globalvalue(direction,av)
        polynomial=next(p for p in center['global_polynomials'] if p['n']==direction['n'])['coefficients_0to4_in_y_mod47four']
        assert value==sum(c*pow(y,k,Q) for k,c in enumerate(polynomial))%Q
        target=direction['QC_defect_targets_by_component_order'][ci]
        scaled=(value-target)%Q;h=scaled*pow(800,-1,Q)%Q
        heights.append({'n':direction['n'],'global_value_mod47four':value,'same_component_QC_target_mod47four':target,'scaled_by800_local_height_mod47four':scaled,'canonical_local_sigma_height_mod47four':h})
    out={'result':'R314','discriminant':-27,'j_integer':j,'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
        'disk_id':disk,'bad_component_at41':component,'complete_actual_CM_point_and_all53_height_anchors':True,
        'point_source':'R292 actual T3(b)=b+3v, with all73 exact target coincidence already verified',
        'exact_Jacobian_class_formula':'U_v=(T3-1)U_minus3/3; C_v=(U_v-U_minus3)/20',
        'fields':field_records,'actual_U_v_cyclic_coordinates_mod47four':rv,'actual_C_v_cyclic_coordinates_mod47cubed':av,
        'actual_fc_normalized_W_mod47four':W,'actual_W_in_original_SS_atlas_frame_mod47four':Wp,
        'atlas_chart_0based':chart['chart_0based'],'atlas_row_0based':row,'frame':chart['frame'],'coordinate':chart['coordinate'],
        'actual_original_chart_z_mod47four':z,'actual_original_y_mod47cubed':y,
        'all73_actual_point_coordinates_recovered_from_original_chart':True,
        'all54_exact_Hecke_class_coordinates_equal_actual_SS_constant_plus_tiny':True,
        'all53_global_values_match_actual_disk_polynomial_evaluation':True,
        'known_CM_anchors_in_same_SS_disk':[],
        'all53_local_height_anchors_by_global_reciprocity':heights,
        'anchor_method':'Exact rational CM point plus proven global heights and its fixed bad label; no claim of independent local Norm evaluation',
        'complete_local_disk_QC_heights':False,'complete_common_roots':False,
        'input_sha256':inputs,'source_sha256':sha(__file__)}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode();args.output.write_bytes(gzip.compress(raw,mtime=0))
    print('PASS true CM27 SS anchor',disk,'z',z,'y',y,'bad label',component,'F2 height',heights[0]['canonical_local_sigma_height_mod47four'],'SHA',sha(args.output))


if __name__=='__main__':main()
