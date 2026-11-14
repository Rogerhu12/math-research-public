#!/usr/bin/env python3
"""Assemble the first three actual global heights from complete pinned inputs."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

Q = 47**4
M = 21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--topic-dir', type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument('--recovery-dir', type=Path)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    data = args.topic_dir/'scripts'/'data'
    inputs = {}

    def read(name, recovery=False):
        p = (args.recovery_dir/name if recovery and args.recovery_dir else data/name)
        if name.startswith('notes/'):
            p = args.topic_dir/name
        raw = p.read_bytes()
        inputs[name] = hashlib.sha256(raw).hexdigest()
        return json.loads(gzip.decompress(raw) if name.endswith('.gz') else raw)

    eta = read('p41_eta_calibration47_complete.json.gz', True)
    tiny = read('p41_eta_hecke_tiny47_complete.json.gz', True)
    assert tiny['eta_certificate_sha256'] == inputs['p41_eta_calibration47_complete.json.gz']
    assert eta['equations_checked'] == 154 and eta['final_calibration_rank'] == 93
    assert eta['numerator_sha256'] == 'f1be6a6ae4e9cee06e0439d49c02234926099ba7825ee0cbacabe93d072a3e87'
    cm4 = read('p41_cm4_miller_norm47_complete.json.gz')
    cm16 = read('p41_cm16_miller_norm47_complete.json.gz', True)
    cm36 = read('p41_cm36_miller_norm47_complete.json.gz', True)
    cusp = read('p41_cusp_miller_norm47_complete.json.gz')
    non47 = read('notes/r195_non47_local_heights_certificate.json')
    chain = '2e24db934bf136b7280385c20dd8d1c4bfd97f850cad4b32b4705ba05b8546ed'
    for d in (cm4, cm16, cm36, cusp):
        assert d['complete_full_chain'] and d['bits'] == 304 and d['steps'] == 454
        assert int(d.get('multiplier', d.get('exponent'))) == M
        assert d['input_sha256']['p41_poincare_miller_jets47_saved.json.gz'] == chain
    assert cm16['number_of_points'] == 20 and cm36['number_of_points'] == 40
    assert cusp['tangent'] == 'q41'
    assert cusp['final_f_B_cusp_norm']['phi20_fixed']
    assert int(cusp['final_f_B_cusp_norm']['cusp_order']) == -M
    for d in (cm4, cm16, cm36):
        assert d['Frobenius'] and d['all_actual_ideal_columns_checked'] == 73
    L4 = cm4['final_f_B_CM4_norm']['log_norm_unit_j_minus1728']
    L16 = cm16['final_f_B_CM_norm']['log_norm']
    L36 = cm36['final_f_B_CM_norm']['log_norm']
    assert L4[1] == L16[1] == L36[1] == 0
    L4, L16, L36 = L4[0], L16[0], L36[0]
    LD = cusp['final_f_B_cusp_norm']['log_norm20']
    assert [L4,L16,L36,LD] == [2452507,1668829,5546,571990]
    ints = tiny['families'][0]['tiny_integrals_mod47_fourth']
    assert ints == {'1':890368,'2':463561,'3':924161}
    assert tiny['families'][1]['tiny_integrals_mod47_fourth'] == {'1':1730352}
    for n in (2,3):
        assert tiny['traces'][str(n)]['all_good_rows_checked'] and tiny['traces'][str(n)]['Frobenius']
    norm_logs = {1:(L4-LD)%Q, 2:(L4+2*L16-3*LD)%Q, 3:(2*L36-4*LD)%Q}
    inv = pow(M,-1,Q)
    assert inv == 4074216 and M % 47 == 9
    rows=[]
    for n in (1,2,3):
        matches = [row for row in non47['rows'] if row['correspondence']['kind']=='Hecke' and row['correspondence']['index']==n]
        assert len(matches)==1
        correction = matches[0]['non47_correction_mod47four']
        numerator=(ints[str(n)]+norm_logs[n])%Q
        local=numerator*inv%Q
        height=(local-correction)%Q
        rows.append({'n':n,'actual_CM_cycle':{1:{'Z4':1},2:{'Z4':1,'Z16':2},3:{'Z36':2}}[n],
                     'cusp_multiplicity':{1:1,2:3,3:4}[n],
                     'tiny_integral':ints[str(n)],'log_fB_on_TnA':norm_logs[n],
                     'm_times_47_local_height':numerator,'47_local_height':local,
                     'non47_correction':correction,'global_height':height,
                     'non47_coefficients':matches[0]['non47_coefficients']})
    assert [r['47_local_height'] for r in rows]==[2970212,4304166,3451351]
    assert [r['global_height'] for r in rows]==[3623418,2463646,4692386]
    out={'status':'complete actual T1,T2,T3 global heights in the R140/R145 Hecke-compatible splitting',
         'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'multiplier':str(M),
         'multiplier_mod47four':M%Q,'multiplier_inverse_mod47four':inv,
         'CM_and_cusp_logs':{'Z4_j_minus1728':L4,'Z16':L16,'Z36':L36,'D_q41':LD},
         'rows':rows,'input_sha256':inputs,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'formula':'h(A,TnA)=(tiny(Tn eta_A,mA)+log f_B[TnA])/m - sum_{ell !=47} I_ell(A,TnA) log_47(ell)',
         'scope':'three of the 54 actual Hecke-basis heights; no unit-root identification or all-layer conclusion'}
    raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode()
    args.output.write_bytes(gzip.compress(raw,mtime=0) if args.output.name.endswith('.gz') else raw)
    print(json.dumps({'global_heights':[row['global_height'] for row in rows],
                      'output_sha256':hashlib.sha256(args.output.read_bytes()).hexdigest()},sort_keys=True))


if __name__=='__main__':
    main()
