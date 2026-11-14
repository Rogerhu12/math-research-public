#!/usr/bin/env python3
"""Numerical global polynomials for the 53 actual QC directions.

The coefficients are in the eight published H=T2+2T3 power bases.  No local
height function or Abel logarithm on a new residue disk is inferred here.
Both absolute U=20P-D and based C=P-P_minus3 conventions are supplied, and
the two independent R184 actual F2 local heights must agree exactly.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

P=47
Q=P**4


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def mv(A,v):return [sum(a*b for a,b in zip(row,v))%Q for row in A]


def power_traces(f,N):
    d=len(f)-1;out=[d]
    for k in range(1,N+1):
        total=sum(f[j]*out[k-j] for j in range(1,min(k-1,d)+1))
        if k<=d:total+=k*f[k]
        out.append(-total%Q)
    return out


class Field:
    def __init__(self,descending):
        self.f=descending[::-1];self.d=len(self.f)-1
        assert self.f[-1]==1
        self.traces=power_traces(descending,3*self.d-3)

    def val(self,pair):
        den,coeffs=pair
        assert den%P
        return self.pad([a*pow(den,-1,Q)%Q for a in coeffs[::-1]])

    def pad(self,a):
        assert len(a)<=self.d
        return a+[0]*(self.d-len(a))

    def add(self,a,b):return [(x+y)%Q for x,y in zip(self.pad(a),self.pad(b))]
    def scale(self,a,c):return [x*c%Q for x in a]

    def mul(self,a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%Q
        while len(out)>self.d:
            x=out.pop();k=len(out)-self.d
            for j in range(self.d):out[k+j]=(out[k+j]-x*self.f[j])%Q
        return self.pad(out)

    def weighted_moments(self,a,N):
        return [sum(x*self.traces[j+k] for j,x in enumerate(a))%Q for k in range(N+1)]

    def trace(self,a):return sum(x*t for x,t in zip(a,self.traces))%Q


def eval_blocks(record,x,convention):
    blocks=record[convention]['quadratic_blocks_mod47four']
    linear=record[convention]['linear_vector_mod47four']
    v=record[convention]['constant_mod47four'];offset=0
    for block in blocks:
        d=len(block);xx=x[offset:offset+d]
        v+=sum(xx[i]*block[i][j]*xx[j] for i in range(d) for j in range(d))
        offset+=d
    assert offset==len(x)==54
    return (v+sum(a*b for a,b in zip(linear,x)))%Q


def logarithm_unit(a):
    assert a%P
    z=(pow(a,P-1,Q)-1)%Q
    return (z-z*z*pow(2,-1,Q)+z*z*z*pow(3,-1,Q))*pow(P-1,-1,Q)%Q


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--heights',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();data=args.script_dir/'data';inputs={}
    def get(name,path=None):
        path=path or data/name;inputs[name]=sha(path);return read(path)
    complete=get('p41_all_global_heights_and_coefficients47.json.gz',args.heights)
    full=get('p41_full_chow_heegner_certificate.json.gz')
    jacobi=get('p41_jacobi_cm_certificate.json')
    absolute=get('p41_cm_height_calibration47_certificate.json.gz')
    relative=get('p41_cm_relative_calibration47_certificate.json.gz')
    bad=get('p41_all_bad_heights_certificate.json')
    cm12=get('p41_cm12_f2_complete_height47_certificate.json.gz')
    cm7=get('p41_cm7_f2_complete_height47_certificate.json.gz')
    assert complete['complete_coefficients'] and complete['all54_height_equations_verified']
    assert full['jacobi_reference_sha256']==inputs['p41_jacobi_cm_certificate.json']
    assert complete['input_sha256']['p41_full_chow_heegner_certificate.json.gz']==inputs['p41_full_chow_heegner_certificate.json.gz']
    s=complete['s_coordinates_mod47four'];assert len(s)==54
    indices=full['indices'][1:];meta=full['row_metadata']
    assert indices==[m['n'] for m in meta]==[r['n'] for r in bad['directions']]
    assert len(indices)==53 and bad['component_labels']==[0,3,28,32]
    rows=[]
    for k,n in enumerate(indices):
        rows.append({'direction_1based':k+1,'n':n,
                     'F_Tn_coefficient':meta[k]['F_Tn_coefficient'],
                     'F_identity_coefficient':meta[k]['F_identity_coefficient'],
                     'absolute_U':{'quadratic_blocks_mod47four':[], 'linear_vector_mod47four':[], 'constant_mod47four':0},
                     'based_C':{'quadratic_blocks_mod47four':[], 'linear_vector_mod47four':[], 'constant_mod47four':0},
                     'F_field_coefficients_ascending_mod47four':[],
                     'xi_G_field_coefficients_ascending_mod47four':[]})
    offset=0;fields=[];r3all=[];r7all=[];r12all=[]
    for number,(ff,jf) in enumerate(zip(full['fields'],jacobi['fields']),1):
        assert ff['factor_descending']==jf['factor_descending']
        field=Field(ff['factor_descending']);d=field.d;ss=s[offset:offset+d]
        r3=field.val([jf['r3_denominator'],jf['r3_numerator_descending']])
        r7=field.val([jf['r7_denominator'],jf['r7_numerator_descending']])
        r12=field.scale(field.mul(field.val(ff['directions'][0][0]),r3),pow(3,-1,Q))
        assert r12==relative['r_minus12_field_coefficients_ascending'][number-1]
        r3all+=r3;r7all+=r7;r12all+=r12
        fields.append({'field_1based':number,'factor_descending':ff['factor_descending'],
                       'coordinate_positions_1based':list(range(offset+1,offset+d+1)),
                       'r_minus3':r3,'r_minus7':r7,'r_minus12':r12})
        for k,(dd,mt,row) in enumerate(zip(ff['directions'],meta,rows)):
            assert mt['G_multiplier']==2
            T=field.val(dd[0]);xi=field.val(dd[2])
            F=field.add(field.scale(T,mt['F_Tn_coefficient']),[mt['F_identity_coefficient']])
            sf=field.mul(ss,F)
            aqmom=field.weighted_moments(field.scale(sf,2),2*d-2)
            aq=[[aqmom[i+j] for j in range(d)] for i in range(d)]
            al=field.weighted_moments(field.scale(field.mul(ss,xi),-1),d-1)
            basedlinear=field.add(field.scale(field.mul(F,r3),80),field.scale(xi,-20))
            bl=field.weighted_moments(field.mul(ss,basedlinear),d-1)
            row['absolute_U']['quadratic_blocks_mod47four'].append(aq)
            row['absolute_U']['linear_vector_mod47four']+=al
            row['based_C']['quadratic_blocks_mod47four'].append([[400*a%Q for a in rr] for rr in aq])
            row['based_C']['linear_vector_mod47four']+=bl
            row['F_field_coefficients_ascending_mod47four'].append(F)
            row['xi_G_field_coefficients_ascending_mod47four'].append(xi)
        offset+=d
    assert offset==54
    predicted_abs=mv(absolute['height_coefficient_matrix'],s)
    predicted_rel=mv(relative['height_coefficient_matrix'],s)
    based12=[(a-b)*pow(20,-1,Q)%Q for a,b in zip(r12all,r3all)]
    based7=[(a-b)*pow(20,-1,Q)%Q for a,b in zip(r7all,r3all)]
    for k,row in enumerate(rows):
        anchor=eval_blocks(row,r3all,'absolute_U')
        assert anchor==predicted_abs[k]
        cm12abs=eval_blocks(row,r12all,'absolute_U')
        cm12diff=eval_blocks(row,based12,'based_C')
        assert cm12diff==(cm12abs-anchor)%Q==predicted_rel[k]
        row['absolute_anchor_value_mod47four']=anchor
        row['predicted_CM12_height_difference_mod47four']=cm12diff
    cm7abs=eval_blocks(rows[0],r7all,'absolute_U')
    cm7diff=eval_blocks(rows[0],based7,'based_C')
    assert cm7abs==predicted_abs[-1]
    assert cm7diff==(cm7abs-predicted_abs[0])%Q==predicted_rel[-1]
    comparisons=[]
    for discriminant,cert,prediction in [(12,cm12,predicted_rel[0]),(7,cm7,predicted_rel[-1])]:
        assert cert['QC_tensor_power']==800 and cert['bad_height_for_F2']==0
        observed=cert['actual_QC_section_height_difference_from_b']
        assert prediction==observed
        comparisons.append({'discriminant':-discriminant,'n':2,'global_height_difference_mod47four':prediction,
                            'independently_computed_R184_section_height_difference_mod47four':observed,
                            'bad_component':3 if discriminant==12 else 28,'bad_height':0,
                            'same_actual_normalization':True,'exact_match_mod47four':True})
    log41=logarithm_unit(41);assert log41==1315812
    components=[]
    for j,label in enumerate(bad['component_labels']):
        values=[dr['bad_values'][j] for dr in bad['directions']]
        components.append({'component_label_at41':label,'bad_values_integer':values,
                           'QC_defect_target_mod47four':[(-log41*v)%Q for v in values]})
    for k,row in enumerate(rows):
        row['bad_values_by_component_order']=bad['directions'][k]['bad_values']
        row['QC_defect_targets_by_component_order']=[cc['QC_defect_target_mod47four'][k] for cc in components]
    expected_disks=48-full['hecke_traces'][full['indices'].index(47)]
    assert expected_disks==129
    output={'scope':'Numerical global quadratic/linear polynomials for all53 actual QC directions; local functions not asserted',
            'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
            'complete_global_polynomials':True,'complete_local_functions':False,'complete_common_roots':False,
            'coordinate_basis':'eight R89 fields in order, ascending powers of H=T2+2T3; coefficients of C=aB_minus4 or U=rB_minus4',
            'polynomial_convention':'x^T A x+L*x+constant; quadratic matrices are not Hessians and have no additional 1/2',
            'absolute_formula':'Tr(s*(2*F_n*r^2-xi_(2F_n)*r)), U=20P-D=rB_minus4',
            'based_formula':'Tr(s*(800*F_n*a^2+(80*F_n*r_minus3-20*xi_(2F_n))*a)), C=P-P_minus3=aB_minus4',
            'based_zero_constant':True,'d':20,'G_multiplier':2,'based_quadratic_multiplier':800,
            'actual_local_section_requirement':'Use lambda47(t_n(P))-lambda47(t_n(P_minus3)) for the fixed global algebraic section; disk frames alone do not set its integration constants',
            'QC_defect_formula':'based_global_polynomial(C(P))-actual_based_local_section_height(P)',
            'component_requirement':'One component_label_at41 must hold simultaneously for all53 directions at a candidate point',
            'direction_indices':indices,'fields':fields,'directions':rows,
            'component_order':bad['component_labels'],'component_vectors':components,'log47_41_mod47four':log41,
            'CM_comparison':comparisons,
            'all54_R133_absolute_calibration_values_mod47four':predicted_abs,
            'all54_R144_relative_calibration_values_mod47four':predicted_rel,
            'all54_absolute_and_relative_matrix_matches':True,
            'expected_F47_rational_residue_disks':expected_disks,
            'disk_count_formula':'#X(F47)=47+1-Tr(T47|H0(Omega)); actual trace=-81',
            's_input_sha256':inputs['p41_all_global_heights_and_coefficients47.json.gz'],
            'input_sha256':inputs,'source_sha256':sha(__file__)}
    args.output.write_bytes(gzip.compress((json.dumps(output,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
    print('PASS all53 global quadratic/linear polynomials; all54 R133 and R144 equations; both actual R184 CM heights',flush=True)
    print('R184 comparisons',comparisons,flush=True)
    print('Expected F47 disks',expected_disks,'SHA',sha(args.output),flush=True)


if __name__=='__main__':main()
