#!/usr/bin/env python3
"""Strict readable constants from the actual complete ac1 scalar Green run."""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx
from fourfold_codazzi_curvature_angle_energy_prefix import read
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

SOURCE='6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
BODY={
 'raw_outer_mean_z':'0.288584',
 'outer_physical_Cmean':'9.707939',
 'true_cap_DZ_mean':'0.000007157487',
 'independent_fB_dotH2_mean':'0.0000007952763',
 'ordinary_mean_source_L2_r':'0.538112',
 'nonmean_L2_rphi_feedback':'0.103384',
 'independent_response_mean_jumps_l1':'0.698331',
 'reduced_nu_body_and_interface':'0.001498957'}
WAIST={
 'outer_mean_z':'0.0000000000002729204',
 'outer_physical_Cmean':'0.000000000009181042',
 'true_cap_DZ_mean':'0.000000000000000006769015',
 'independent_fB_dotH2_mean':'0.0000000000000000007521128',
 'nonmean_Linfty_r_L2_feedback':'0.085776712',
 'ordinary_mean_source_Linfty_r':'0.597291063',
 'nonmean_L2_rphi_feedback':'0.112001425',
 'ordinary_mean_source_L2_r':'0.732535123',
 'independent_response_mean_jumps_l1':'1.017011959',
 'reference_subtracted_nu_body_and_interface':'0.004626403'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--native',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=320
    if a.out.exists():raise FileExistsError('preserve prior actual results')
    d=read(a.native)
    if (not d['complete'] or d['failure'] is not None or d['source_sha256']!=SOURCE
            or d['candidate_sha256']!=CANDIDATE or d['exact_interval']!=['0','25/8']
            or not d['whole_original_affine_parameter_interval']
            or not d['complete_original_primitive_tail_reused']):
        raise ValueError('actual full candidate/target/certificate identity required')
    if len(d['rows'])!=d['total_closed_cells'] or len(d['rows'])!=7721:
        raise ValueError('the full common radial cover is required')
    right=Fraction(0)
    for i,row in enumerate(d['rows']):
        l,r=map(Fraction,row['interval'])
        if i!=row['common_row'] or l!=right or not l<r:
            raise ValueError('the full exact closed cover lost adjacency')
        right=r
    if right!=Fraction(25,8) or len(d['interfaces'])!=6143:
        raise ValueError('complete endpoint or candidate joins are missing')
    gates=[]
    def bound(name,value,limit):
        q=Fraction(limit);b=exact_arb(q)
        if not value<b:raise ValueError('strict directed gate failed: '+name)
        gates.append(dict(name=name,value=record(value),strict_rational_upper=str(q),passed=True))
    b=d['bounds'];get=lambda k:box_from_record(b[k])
    bound('complete_log_Gamma',get('complete_log_Gamma_upper'),'0.013149548')
    bound('complete_Gamma',get('complete_log_Gamma_upper').exp(),'1.013237')
    bound('candidate_interface_log',get('full_interface_log_upper'),'0.000000000000000001169345')
    bound('signed_diagonal_integral',get('signed_residual_sensitive_diagonal_integral'),'-0.00046415')
    for key,limits in (
        ('complete_full_body_mean_gain_if_log_Gamma_below_100',BODY),
        ('complete_waist_mean_gain_if_log_Gamma_below_100',WAIST)):
        for name,limit in limits.items():bound(key+'/'+name,box_from_record(b[key][name]),limit)
    direct=get('full_body_direct_nu_contact_L2')
    bound('direct_parameter_contact_L2',direct,'0.001436627')
    bound('complete_parameter_column_L2',direct+box_from_record(
        b['complete_full_body_mean_gain_if_log_Gamma_below_100']['reduced_nu_body_and_interface']),
        '0.002935584')
    doc=dict(kind='actual_final_full_mean_Green_strict_readable_constants',complete=True,
        source_sha256=sha(__file__),native_path=str(a.native),native_sha256=sha(a.native),
        original_native_source_sha256=SOURCE,candidate_sha256=CANDIDATE,
        actual_closed_cells=7721,actual_candidate_mean_interfaces=6143,
        exact_interval=['0','25/8'],whole_original_eta=True,all_primitive_tails=True,
        original_complete_mean_given_nonmean_scope=True,
        full_body_inverse_proved=False,nu_scalar_nonzero_proved=False,
        full_body_bounds=BODY,waist_bounds=WAIST,gates=gates)
    save(a.out,doc)
    print(dict(complete=True,strict_gates=len(gates),out=str(a.out)),flush=True)


if __name__=='__main__':main()
