#!/usr/bin/env python3
"""Assemble all54 actual global heights and the exact R186 trace coefficients.

The norm input already includes physical D0 coordinate units, fixed j-1728
horizontal tangents, and the selected near-CM4 logarithms.  The assembly adds
R221's merged endpoint remainder, subtracts the full cusp norm, divides by m
once, and subtracts the complete R195 non47 correction.
"""
import argparse
import gzip
import hashlib
import json
from math import gcd,isqrt
from pathlib import Path

Q=47**4
M=21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def scalar(x):
    if isinstance(x,(list,tuple)):
        assert len(x)==2 and x[1]%Q==0
        return int(x[0])%Q
    return int(x)%Q


def mm(A,B):return [[sum(x*y for x,y in zip(row,col))%Q for col in zip(*B)] for row in A]
def mv(A,v):return [sum(x*y for x,y in zip(row,v))%Q for row in A]


def rho(n):
    b=isqrt(n)
    c=sum(a*a+d*d==n and gcd(a,d)==1 for a in range(-b,b+1) for d in range(-b,b+1))
    assert c%4==0
    return c//4


def psi(n):
    v=n;p=2;m=n
    while p*p<=m:
        if m%p==0:
            v=v//p*(p+1)
            while m%p==0:m//=p
        p+=1
    if m>1:v=v//m*(m+1)
    return v


def traces(f,N):
    d=len(f)-1;assert f[0]==1
    out=[d]
    for k in range(1,N+1):
        total=0
        for j in range(1,min(k,d)+1):
            total+=k*f[j] if j==k else f[j]*out[k-j]
        out.append(-total%Q)
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--topic-dir',type=Path,required=True)
    ap.add_argument('--norms',type=Path)
    ap.add_argument('--endpoints',type=Path)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();folder=args.topic_dir.resolve();data=folder/'scripts/data';inputs={}
    def get(name,path=None):
        path=path or (folder/name if name.startswith('notes/') else data/name)
        inputs[name]=sha(path)
        return read(path)
    basis=get('p41_hecke_height_basis47_certificate.json.gz')
    source=get('p41_source_j9_descending_kernel_dag47.json.gz')
    cm=get('p41_CM4_descending_kernel_dag47.json.gz')
    endpoints=get('p41_source_j9_all_endpoint_integrals47.json.gz',args.endpoints)
    cancellation=get('p41_all_D0_cancellation_and_CM4_poles47.json.gz')
    precision=get('p41_selected_CM4_precision6_audit.json.gz')
    non47=get('notes/r195_non47_local_heights_certificate.json')
    z4=get('p41_cm4_miller_norm47_complete.json.gz')
    z16=get('p41_cm16_miller_norm47_complete.json.gz')
    z36=get('p41_cm36_miller_norm47_complete.json.gz')
    cusp=get('p41_cusp_miller_norm47_complete.json.gz')
    first=get('p41_first_three_heights47_complete.json.gz')
    full=get('p41_full_chow_heegner_certificate.json.gz')
    calibration=get('p41_cm_height_calibration47_certificate.json.gz')
    assert endpoints['complete_regular_parts'] and endpoints['complete_level_input']
    assert cancellation['all_54_D0_counters_match'] and precision['all_54_Frobenius_checks']
    assert endpoints['constant_dag_sha256']==inputs['p41_source_j9_descending_kernel_dag47.json.gz']
    assert cancellation['input_sha256']['p41_source_j9_all_endpoint_integrals47.json.gz']==inputs['p41_source_j9_all_endpoint_integrals47.json.gz']
    assert calibration['coordinate_basis']=='eight R89 fields in order, ascending powers of H=T2+2T3'
    labels=basis['new_correspondence_labels'];indices=[r['index'] for r in labels]
    assert len(indices)==len(set(indices))==54 and indices==source['indices']==cm['indices']
    assert len(non47['rows'])==54
    corrections={r['correspondence']['index']:r for r in non47['rows']}
    assert set(corrections)==set(indices)=={int(k) for k in endpoints['aggregates']}
    chain='2e24db934bf136b7280385c20dd8d1c4bfd97f850cad4b32b4705ba05b8546ed'
    for cert in [z4,z16,z36,cusp]:
        assert cert['complete_full_chain'] and cert['bits']==304 and cert['steps']==454
        assert int(cert.get('multiplier',cert.get('exponent')))==M
        assert cert['input_sha256']['p41_poincare_miller_jets47_saved.json.gz']==chain
    L4=scalar(z4['final_f_B_CM4_norm']['log_norm_unit_j_minus1728'])
    L16=scalar(z16['final_f_B_CM_norm']['log_norm'])
    L36=scalar(z36['final_f_B_CM_norm']['log_norm'])
    LD=scalar(cusp['final_f_B_cusp_norm']['log_norm20'])
    assert cusp['tangent']=='q41' and [L4,L16,L36,LD]==[2452507,1668829,5546,571990]
    inv=pow(M,-1,Q);assert inv==4074216
    rows=[]
    for position,label in enumerate(labels):
        n=label['index'];correction=corrections[n];ep=endpoints['aggregates'][str(n)]
        assert all(correction['correspondence'][k]==label[k] for k in ['kind','index','effective_degree'])
        degree=psi(n);return_count=rho(n)
        assert degree==label['effective_degree']==len(source['targets'][str(n)])==len(cm['targets'][str(n)])==ep['target_count']
        assert return_count==correction['CM_return_multiplicity']==cancellation['per_index'][str(n)]['rho_cyclic']
        assert correction['I41']==-40*return_count
        merged=scalar(ep['combined_remainder_after_global_factor_cancellation'])
        K=correction['non47_correction_mod47four']
        rows.append({'basis_row_1based':position+1,'correspondence':label,'index':n,
                     'psi_cyclic':degree,'rho_cyclic':return_count,
                     'CM_target_rows':20*degree,'endpoint_merged_remainder':merged,
                     'CM4_endpoint_poles':ep['CM4_logarithmic_rows'],
                     'D0_norm_collision_rows':cancellation['per_index'][str(n)]['D0_collision_norm_rows'],
                     'cusp_log_norm':LD,'cusp_log_subtraction':degree*LD%Q,
                     'horizontal_CM4_norm_already_in_norm':return_count*L4%Q,
                     'near_CM4_rows':precision['aggregates'][str(n)]['near_CM4_rows'],
                     'near_CM4_m_log_j_already_in_norm':M*scalar(precision['aggregates'][str(n)]['log_j_minus1728_sum_mod47_fourth'])%Q,
                     'non47_correction':K,'non47_coefficients':correction['non47_coefficients'],
                     'known_numerator_offset':(merged-degree*LD)%Q})
    old_by_n={r['n']:r for r in first['rows']}
    known_norms={1:L4,2:(L4+2*L16)%Q,3:2*L36%Q}
    regressions=[]
    for n in [1,2,3]:
        row=next(r for r in rows if r['index']==n)
        local=(row['known_numerator_offset']+known_norms[n])*inv%Q
        height=(local-row['non47_correction'])%Q
        assert local==old_by_n[n]['47_local_height'] and height==old_by_n[n]['global_height']
        regressions.append({'n':n,'CM_norm':known_norms[n],'47_local_height':local,
                            'global_height':height,'R197_exact_match':True})
    output={'scope':'All54 actual Hecke global-height inputs and, when norms supplied, global trace coefficients',
            'complete_heights':False,'complete_coefficients':False,'modulus':Q,'level':41,'auxiliary_prime':47,
            'multiplier':str(M),'multiplier_inverse_mod47four':inv,
            'basis_labels':labels,'rows':rows,'R197_regression':regressions,
            'norm_contract':'CM_norm_after_D0_factor_removal already includes the D0 chart-to-physical units, all fixed j-1728 horizontal norms, and the m*log(j-1728) near-CM4 terms',
            'assembly_formula':'global_height=m_inverse*(CM_norm_after_D0_factor_removal+endpoint_merged_remainder-psi_cyclic*cusp_log_norm)-non47_correction',
            'canonical_tangents':{'CM4':'j-1728','cusp':'q41','horizontal_Hecke_derivative_extra_term':0},
            'input_sha256':inputs,'source_sha256':sha(__file__)}
    if args.norms:
        norms=get('p41_all_CM_Miller_norms47.json.gz',args.norms)
        assert norms['complete'] and norms['all_54_aggregate_imaginary_parts_zero']
        assert norms['D0_physical_parameter_correction_retained']
        assert norms['all_200_static_CM4_logarithms_used_once_per_target']
        assert norms['modulus']==Q and int(norms['multiplier'])==M
        assert set(norms['aggregates'])=={str(n) for n in indices}
        heights=[]
        for row in rows:
            n=row['index'];nr=norms['aggregates'][str(n)]
            assert nr['effective_degree']==row['psi_cyclic'] and nr['index']==n
            norm=scalar(nr['CM_norm_after_D0_factor_removal'])
            if n in known_norms:assert norm==known_norms[n]
            numerator=(norm+row['known_numerator_offset'])%Q
            local=numerator*inv%Q;height=(local-row['non47_correction'])%Q
            row.update({'CM_norm_after_D0_factor_removal':norm,'m_times_47_local_height':numerator,
                        '47_local_height':local,'global_height':height})
            heights.append(height)
            if n in old_by_n:assert height==old_by_n[n]['global_height']
        C=basis['new_basis_matrix_mod47four'];G=basis['trace_gram_mod47four']
        H=basis['height_matrix_mod47four'];Hi=basis['inverse_height_matrix_mod47four']
        identity=[[int(i==j) for j in range(54)] for i in range(54)]
        assert mm(C,G)==H and mm(H,Hi)==mm(Hi,H)==identity
        s=mv(Hi,heights);assert mv(H,s)==heights
        expectedG=[[0]*54 for _ in range(54)];heightGram=[[0]*54 for _ in range(54)]
        fields=[];offset=0
        assert len(full['fields'])==8
        for number,field in enumerate(full['fields'],1):
            f=field['factor_descending'];d=len(f)-1;T=traces(f,3*d-3)
            coeff=s[offset:offset+d]
            moments=[sum(coeff[j]*T[j+k] for j in range(d))%Q for k in range(2*d-1)]
            for i in range(d):
                for j in range(d):
                    expectedG[offset+i][offset+j]=T[i+j]
                    heightGram[offset+i][offset+j]=moments[i+j]
            fields.append({'field_1based':number,'factor_descending':f,
                           'coordinate_positions_1based':list(range(offset+1,offset+d+1)),
                           's_coefficients_ascending_mod47four':coeff,
                           'trace_s_times_H_powers_0to2dminus2':moments})
            offset+=d
        assert offset==54 and expectedG==G
        one=[0]*54
        for field in fields:one[field['coordinate_positions_1based'][0]-1]=1
        assert mv(C,mv(heightGram,one))==heights
        assert sum(field['trace_s_times_H_powers_0to2dminus2'][0] for field in fields)%Q==heights[0]
        output.update({'complete_heights':True,'complete_coefficients':True,
                       'height_vector_basis_order_mod47four':heights,
                       's_coordinates_mod47four':s,'s_field_decomposition':fields,
                       'coordinate_basis':calibration['coordinate_basis'],
                       'height_bilinear_Gram_in_B_cyclic_coordinates_mod47four':heightGram,
                       'actual_equation':'h(a*B,b*B)=Trace_E/Q47(s*a*b)',
                       'all54_height_equations_verified':True,'trace_Gram_rebuilt_from_all8_field_polynomials':True,
                       'height_matrix_determinant_mod47':basis['determinants_mod47']['height'],
                       'precision_loss_in_solve':0,
                       'remaining':'Complete QC functions on all residue disks, their common roots, and the main uniformity objective are not asserted by this assembly'})
    args.output.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(output,sort_keys=True,separators=(',',':'))+'\n').encode()
    args.output.write_bytes(gzip.compress(raw,mtime=0))
    print('all54 inputs; heights',output['complete_heights'],'coefficients',output['complete_coefficients'],
          'SHA',sha(args.output),flush=True)
    if output['complete_heights']:print('height vector',output['height_vector_basis_order_mod47four'],flush=True)


if __name__=='__main__':main()
