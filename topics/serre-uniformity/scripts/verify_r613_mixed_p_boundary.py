#!/usr/bin/env python3
"""Check R613's small exact boundary algebra from the two actual inputs.

This reuses the published R198 44-row certificate and the newly executed
R561 scalar certificate.  It does not repeat their Robert evaluations.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def read(path):
    data=path.read_bytes()
    if path.suffix=='.gz': data=gzip.decompress(data)
    return json.loads(data),hashlib.sha256(data).hexdigest()


def add(a,b):
    return [(a[0]+b[0])%43,(a[1]+b[1])%43]


def mul(a,b):
    return [(a[0]*b[0]-a[1]*b[1])%43,(a[0]*b[1]+a[1]*b[0])%43]


def sm(a,c):
    return [a[0]*c%43,a[1]*c%43]


def main():
    p=argparse.ArgumentParser()
    p.add_argument('r198_certificate',type=Path)
    p.add_argument('r561_scalar_certificate',type=Path)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--check',type=Path)
    a=p.parse_args()
    anti,ash=read(a.r198_certificate)
    scalar,ssh=read(a.r561_scalar_certificate)
    assert anti['expected']['status']=='PASS' and scalar['status']=='PASS'
    assert int(anti['q'])==int(scalar['q'])
    assert scalar['input_sha256']==ash
    assert anti['anti_p_step']==21 and anti['tame_correction']==11
    assert scalar['CM_tame_correction_scalar']==22
    assert scalar['high_projection_logs']==[9,0]
    assert scalar['Kq_Frobenius_S_exponent']==32 and scalar['s_on_mu_p2']==87
    w=[1,0]; base=[0,0]; deriv=[0,0]
    rows=anti['expected']['rows']; assert len(rows)==44
    for j,row in enumerate(rows):
        assert row['index']==j and row['norm_ratio']=='1'
        base=add(base,sm(w,row['base_unit_log']))
        deriv=add(deriv,sm(w,row['derivative_log']))
        w=mul(w,[8,25])
    assert w==[1,0] and base==[0,0] and deriv==[0,13]
    q=int(anti['q'])
    assert ((q*q-1)//43)%43==21
    assert ((q**86-1)//1849)%43==21
    conversion=pow(21,-1,43); assert conversion==41
    scalar_direct=9*conversion%43; assert scalar_direct==25
    anti_direct_D=sm(deriv,conversion); assert anti_direct_D==[0,17]
    phase_coefficient=sm(anti_direct_D,2); assert phase_coefficient==[0,34]
    class_coefficient=mul([0,-1],phase_coefficient); assert class_coefficient==[34,0]
    assert sum(pow(87,j,1849) for j in range(43))%1849==43
    assert all(pow(87,r*j,1849)==(1+86*r*j)%1849 for r in range(43) for j in range(43))
    family=[]; nonzero_count=0
    for r in range(43):
        phase=add([25,0],sm(phase_coefficient,r))
        assert phase==[25,34*r%43]
        actual_possible=[]
        for nu in range(43):
            # C=i*nu is deliberately a symbolic possible original value.
            r_y=(25+nu)%43
            phase_difference=add(phase,[-r_y,0])
            h_direct=sm(phase_difference,pow(2,-1,43))
            h_log=sm(h_direct,21)
            C_r=mul([0,-pow(32,-1,43)],h_log)
            assert C_r==[34*r%43,nu]
            if r:
                assert C_r!=[0,0]
                assert (C_r[0]*C_r[0]+C_r[1]*C_r[1])%43!=0
                nonzero_count+=1
            actual_possible.append(C_r)
        family.append({'r':r,'H_r_vector_in_S_T':[r,1],
          'direct_mu_p_phase_u_r':phase,'C_r_minus_C':[34*r%43,0],
          'real_part_for_every_possible_C':34*r%43,
          'all_43_possible_C_values_nonzero':bool(r)})
    assert nonzero_count==42*43
    assert pow(42,21,43)==42
    out={'status':'PASS','p':43,'coefficient_field':'F_43[i], i^2=-1, i not in F_43',
      'r198_uncompressed_sha256':ash,'r561_scalar_uncompressed_sha256':ssh,
      'recomputed_44_row_raw_base':base,'recomputed_44_row_D_T_power_log':deriv,
      'mu_index_from_power_log_factor':conversion,'scalar_mu_index':scalar_direct,
      'D_T_u_t_direct_mu_index':anti_direct_D,'u_r_phase_coefficient':phase_coefficient,
      'C_r_minus_C_coefficient':class_coefficient,'family':family,
      'nonzero_classes_checked_for_every_symbolic_C':nonzero_count,
      'ordinary_capitulation_extensions_proved':42,
      'large_Robert_evaluations_repeated':False,'C_is_symbolic_in_iFp':True,
      'original_scalar_C_computed':False,'original_b_lambda_n_computed':False,
      'original_L_computed':False,'old_34_bridge_to_b_restored':False}
    if a.check:
        expected,_=read(a.check)
        assert out==expected
    a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','recomputed_44_row_D_T_power_log','scalar_mu_index','u_r_phase_coefficient','C_r_minus_C_coefficient','ordinary_capitulation_extensions_proved','original_scalar_C_computed','original_L_computed']}))


if __name__=='__main__':
    main()
