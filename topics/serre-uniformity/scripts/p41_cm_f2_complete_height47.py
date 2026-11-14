#!/usr/bin/env python3
"""Assemble actual F2 global-section local heights after both Miller transports.

All function inputs must be complete and bound to the same actual Abel
points.  The normalized QC-section value is800 times the L_b value.
"""
import argparse,gzip,hashlib,json
from pathlib import Path

Q=47**4


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()


def logarithm(a):
    assert a%47
    z=(pow(a,46,Q)-1)%Q
    return (z-z*z*pow(2,-1,Q)+z*z*z*pow(3,-1,Q))*pow(46,-1,Q)%Q


def save(path,payload):
    raw=gzip.compress((json.dumps(payload,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0)
    temporary=path.with_suffix(path.suffix+'.new');temporary.write_bytes(raw);temporary.replace(path)
    return len(raw),hashlib.sha256(raw).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--discriminant',type=int,choices=[12,7],required=True)
    parser.add_argument('--common-norms',type=Path,default=Path('/tmp/p41_translation_window_norms47_complete.json.gz'))
    parser.add_argument('--common-endpoint',type=Path,default=Path('/tmp/p41_common_original_endpoint47_certificate.json.gz'))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();prefix='/tmp/p41_cm'+str(args.discriminant)
    paths={
      'collision_norm':Path(prefix+'_f2_leading_norm47_certificate.json.gz'),
      'direct_fCS_norm':Path(prefix+'_newS_norm_first47_certificate.json.gz'),
      'Hecke_fCS_norm':Path(prefix+'_t2_miller_norm47_complete.json.gz'),
      'rhoT_norms':Path('/tmp/p41_t2_transport_norms47_checkpoint.json.gz'),
      'short_sum_norm':Path(prefix+'_formal_combination47_checkpoint.json.gz'),
      'formal_height':Path(prefix+'_translation_formal_height47_certificate.json.gz'),
      'common_norms':args.common_norms,'common_endpoint':args.common_endpoint,
      'canonical_section_coordinates':args.script_dir/'data/p41_miller_completion47_compact.json.gz'}
    loaded={key:read(path) for key,path in paths.items()}
    inputs={key:pair[1] for key,pair in loaded.items()}
    objects={key:pair[0] for key,pair in loaded.items()}
    C,N,T,R,S,H,D,E,G=[objects[key] for key in ['collision_norm','direct_fCS_norm','Hecke_fCS_norm','rhoT_norms','short_sum_norm','formal_height','common_norms','common_endpoint','canonical_section_coordinates']]
    hashes=C['source_sha256']
    for data in objects.values():assert data['source_sha256']==hashes and data['precision']==4
    m=C['target_multiplier'];assert m%47==9
    for data in [N,T,H,D,E,G]:assert data['target_multiplier']==m
    assert C['discriminant']==N['discriminant']==-args.discriminant
    assert T['class_name']=='cm'+str(args.discriminant)
    assert S['class_name']=='x'+str(args.discriminant)
    assert C['input_sha256']['complete_Miller']==N['input_sha256']['complete_Miller']==T['input_sha256']['miller']
    assert N['input_sha256']['actual_gS']==T['input_sha256']['endpoint']
    assert T['new_S_formal_point_sha256']==N['newS_formal_point_sha256']==S['basis_point_sha256']['Y']
    assert H['target_name']=='three_m_D'+str(args.discriminant)
    assert H['positive_second_formal_point_sha256']==S['basis_point_sha256']['target']
    assert E['class_name']=='common' and E['frame']=='original'
    assert E['new_formal_point_sha256']==S['basis_point_sha256']['Db']
    assert D['current_node']==369 and D['current_exponent']==m
    assert D['status'].startswith('complete actual f_D=')
    assert D['input_sha256']['endpoint']==inputs['common_endpoint']
    assert H['input_sha256']['actual_second_endpoints']==S['input_sha256']['common_formal_endpoints']==E['input_sha256']['formal_endpoints']
    hrec=next(rec for rec in H['records'] if rec['discriminant']==-args.discriminant)
    drec=next(rec for rec in D['records'] if rec['discriminant']==-args.discriminant)
    rrec=next(rec for rec in R['records'] if rec['discriminant']==-args.discriminant)
    psha=N['first_formal_point_sha256']
    assert hrec['first_formal_point_sha256']==drec['actual_formal_point_sha256']==rrec['first_formal_point_sha256']==T['first_formal_point_sha256']==S['first_formal_point_sha256']==psha
    assert C['nonunit_divisions']==N['nonunit_divisions']==T['nonunit_divisions']==0
    assert N['all_actual_principal_values_units'] and drec['all_actual_principal_values_units']
    coords=G['actual_global_F2_section_coordinates_for_K_g1']['u' if args.discriminant==12 else 'c7']
    scalar=coords['actual_g1_coordinate'];ls=logarithm(scalar)
    assert ls==coords['log_of_coordinate_only']
    factors={
      'collision':(C['generalized_f_C_D_P_j_norm'],C['log_generalized_f_C_D_P_j_norm']),
      'Hecke':(T['actual_Hecke_norm'],T['log_actual_Hecke_norm']),
      'rhoT':(rrec['actual_rho_T_norm'],rrec['log_actual_rho_T_norm']),
      'direct':(N['actual_f_CS_norm_on_first_family'],N['log_actual_f_CS_norm_on_first_family']),
      'common':(drec['true_f_D_norm'],drec['log_true_f_D_norm']),
      'sum':(S['actual_Fsigma_norm'],S['log_actual_Fsigma_norm'])}
    for unit,lv in factors.values():assert logarithm(unit)==lv
    lf=factors['collision'][1]
    gnorm=pow(factors['Hecke'][0]*factors['rhoT'][0]%Q,81,Q)*pow(factors['direct'][0],12,Q)%Q
    gnorm=gnorm*factors['common'][0]%Q*factors['sum'][0]%Q
    lg=(81*(factors['Hecke'][1]+factors['rhoT'][1])+12*factors['direct'][1]+factors['common'][1]+factors['sum'][1])%Q
    assert logarithm(gnorm)==lg
    formal=hrec['actual_Hecke_local_log']
    assert formal==(hrec['half_log_double_inverse']+hrec['actual_Hecke_bilinear_correction'])%Q
    denominator=3*m*m%Q;assert denominator%47
    transported=(formal+3*m*lf+lg)%Q
    fibre=transported*pow(denominator,-1,Q)%Q
    section=(ls+fibre)%Q
    qc=800*section%Q
    assert denominator*section%Q==(denominator*ls+formal+3*m*lf+lg)%Q
    payload={'level':41,'auxiliary_prime':47,'precision':4,'discriminant':-args.discriminant,
      'source_sha256':hashes,'input_sha256':inputs,
      'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'target_multiplier':m,'first_formal_point_sha256':psha,
      'second_formal_point_sha256':H['positive_second_formal_point_sha256'],
      'actual_Kg1_section_coordinate':scalar,'log_actual_section_coordinate':ls,
      'actual_function_norms':{key:{'norm':a,'log':b} for key,(a,b) in factors.items()},
      'actual_second_transport_norm':gnorm,'log_actual_second_transport_norm':lg,
      'actual_formal_fibre_height':formal,'three_m_squared_mod47four':denominator,
      'actual_nonformal_eN_height':fibre,'actual_Lb_rigidified_section_height':section,
      'actual_QC_section_height_difference_from_b':qc,'QC_tensor_power':800,
      'bad_height_for_F2':0,'bad_height_source':'R134: all4 actual bad targets vanish for27T2+4',
      'formula':'3m^2*lambda(sigma_P)=3m^2*log(s_P)+lambda(A0(mC),A1(3mD_P))+3m*log f_C0[D_P]_j+log g_P(A0)',
      'second_transport':'g_P=(Norm_T2(f_CS)*rho_T)^81*f_CS^12*f_D*F_Sigma',
      'status':'complete actual F2 normalized QC-section local height difference at this CM point; only the specified direction, not the full54-equation calibration or rational-point classification'}
    output=args.output or Path(prefix+'_f2_complete_height47_certificate.json.gz')
    size,sha=save(output,payload)
    print('ACTUAL COMPLETE F2 HEIGHT PASS',args.discriminant,'nonformal',fibre,'Lb_section',section,'QC_difference',qc,'bytes',size,'sha',sha,flush=True)


if __name__=='__main__':main()
