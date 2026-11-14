#!/usr/bin/env python3
"""Pay the complete cap error into the actual moving cut, mean and high rows.

The full physical cap and trial-Hessian certificates are unchanged inputs.
Every full saved 193-by-96 frame entry is used in the directed Gram and
boundary computation. This proves the stated finite low-cut boundary
facts and retains the entire moving high output; it does not certify a
continuous body inverse or solve its infinite-frequency feedback.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,arb_mat,ctx

EXPECTED={
 'cap':'69f55939742b26988690e54b7f5636eb591a351063b93187feeb38c1f6611ebe',
 'hessian':'cf055cac05569701ebcb0df95fb064c94cec8c18bb28121292a3836b3862be26',
 'cut':'528e2f47d4572d7b90878abc542c3389d76d5fb326d7ef7c3390ef086d6266ba'}
CENTRE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
CAP_SOURCE='953227cd8871a71ee0c5b9e7ed8a53c3099b1890eadfde3936d9de06067e455a'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
def box(value):return arb(value['lower']).lower().union(arb(value['upper']).upper())
def exact(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator
def hexadecimal(value):return exact(Fraction.from_float(float.fromhex(value)))
def rec(value):
    value=arb(value)
    if not value.is_finite():raise ValueError('a true complete cut bound became nonfinite')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))
def frobenius(matrix):
    total=arb(0)
    for i in range(matrix.nrows()):
        for j in range(matrix.ncols()):total+=abs(matrix[i,j]).upper()**2
    return total.upper().sqrt().upper()
def save(path,document):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(document,indent=2,allow_nan=False)+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.tmp');temporary.write_bytes(raw);temporary.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('cap','hessian','cut','actual-process','out'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual complete cut outcome')
    for name,expected in EXPECTED.items():
        if sha(getattr(a,name))!=expected:raise ValueError('an unchanged complete original cap input differs: '+name)
    cap,hessian,cut=read(a.cap),read(a.hessian),read(a.cut);process=read(a.actual_process)
    if (not process.get('complete') or not process.get('whole_original_cap_complete')
        or process.get('failure') or process.get('repository')!='Rogerhu12/math-research-public'
        or str(process.get('run_id'))!='43583838015'
        or process.get('complete_native_sha256')!=EXPECTED['cap']
        or len(process.get('children',[]))!=2
        or any(x.get('actual_returncode')!=0 for x in process['children'])):
        raise ValueError('the original real public complete-cap outcome must be retained')
    ident=cap['identity']
    if (not cap.get('complete') or cap.get('failure') or cap.get('first')!=0 or cap.get('end')!=1977
        or ident.get('source_sha256')!=CAP_SOURCE
        or ident.get('base_candidate_sha256')!=CENTRE or ident.get('derived_definition_sha256')!=REPAIR
        or ident.get('moving_even_input_columns')!=97 or ident.get('physical_modes')!=128
        or ident.get('parameter_half_width')!='1/1000000000'
        or not cap.get('all_ordinary_divergence_mean_true_Robin_and_endpoint_terms_consumed')
        or not cap.get('all_unretained_output_modes_included')):
        raise ValueError('the entire original physical cap certificate is required')
    radius=Fraction(9,10)
    for index,row in enumerate(cap['rows']):
        left,right=map(Fraction,row['interval'])
        if row['index']!=index or left!=radius or not left<right:
            raise ValueError('the actual complete original cap row cover has a gap or duplicate')
        radius=right
    if len(cap['rows'])!=1977 or radius!=Fraction(25,8):raise ValueError('the true full cap domain is required')
    for doc in (hessian,cut):
        if (not doc.get('complete') or doc.get('failure') or doc.get('candidate_sha256')!=CENTRE
            or doc.get('derived_definition_sha256')!=REPAIR):
            raise ValueError('the same complete repaired background is required in every input')
    if (hessian['proposal_input_sha256']!=ident['proposal_sha256']
        or any(ident['full_matrix_inputs'].get(k)!=v for k,v in hessian['complete_input_arrays'].items())
        or hessian.get('exact_affine_offset')!='0' or hessian.get('whole_original_eta') is not False
        or hessian.get('complete_actual_trial_subcells')!=1977
        or not hessian.get('all_input_mean_and_all_outer_rows_retained')
        or cut.get('exact_cut')!='9/10' or cut.get('exact_odd_block')!='I_96'
        or not cut.get('no_head_or_high_boundary_row_deleted')):
        raise ValueError('the complete same-trial Hessian or actual mean/cut contract changed')
    eps=box(cap['complete_actual_cap_graph_error']).upper()
    multiplier=box(hessian['multiplier_of_complete_physical_cap_matrix_error']).upper()
    additive=box(hessian['additive_actual_moving_cap_matrix_error']).upper()
    moving=(multiplier*eps+additive).upper()
    S=box(cut['complete_physical_cap_to_moving_row_gain']).upper()
    low=(box(cut['complete_low_row_error_before_unknown_cap_error'])+S*moving).upper()
    mean=(box(cut['complete_mean_midpoint_error_before_unknown_cap_error'])+moving).upper()
    high=(box(cut['complete_moving_high_before_unknown_cap_error'])+S*moving).upper()
    total=(low*low+mean*mean).sqrt().upper()
    denominator=int(cut['exact_interval_denominator'])
    lo,hi=map(int,cut['independent_mean_row']['exact_interval_numerators'][0])
    m0=exact(Fraction(lo,denominator)).union(exact(Fraction(hi,denominator)))
    mean_margin=(abs(m0).lower()-moving).lower()
    if not mean_margin>0:raise ValueError('the true independent mean coefficient has no paid positive margin')
    J=arb_mat([[hexadecimal(v) for v in row['complete_even_binary64_proposal_hex']] for row in cut['rows']])
    M=[hexadecimal(v) for v in cut['independent_mean_row']['binary64_proposal_hex']]
    B=arb_mat([[arb(int(i==j)) for j in range(96)]+[J[i,j] for j in range(97)] for i in range(96)]
        +[[arb(0) for _ in range(96)]+M])
    Q=arb_mat([[hexadecimal(v) for v in row] for row in cut['kernel_proposal']['complete_basis_binary64_hex']])
    if Q.nrows()!=193 or Q.ncols()!=96:raise ValueError('the entire original proposed frame is required')
    gram=Q.transpose()*Q
    for j in range(96):gram[j,j]-=1
    gram_fee=frobenius(gram);g=(1-gram_fee).lower();qnorm=(1+gram_fee).sqrt().upper()
    if not g>0:raise ValueError('the full exact frame Gram rank gate failed')
    finite_kernel=frobenius(B*Q)
    actual_kernel=((finite_kernel+total*qnorm)/g.sqrt()).upper()
    # A true right inverse chooses only the independent even mean to
    # solve the scalar row; the complete odd identity solves all 96
    # remaining rows. This does not delete the other 96 even columns.
    J0=arb_mat([[J[i,0]] for i in range(96)])
    actual_J0=(frobenius(J0)+low).upper()
    aa=(actual_J0/mean_margin).upper();bb=(1/mean_margin).upper()
    trace=(1+aa*aa+bb*bb).upper()
    discriminant=trace*trace-4*bb*bb
    right_inverse=((trace+discriminant.sqrt())/2).sqrt().upper()
    row_singular=(1/right_inverse).lower()
    complement_square=(row_singular*row_singular-actual_kernel*actual_kernel).lower()
    if not complement_square>0:raise ValueError('the actual full 97-row complement rank gate failed')
    complement_singular=complement_square.sqrt().lower()
    LR=(1/complement_singular).upper();DL=(LR*actual_kernel).upper()
    gap=(right_inverse*actual_kernel).upper()
    bounds=dict(complete_physical_cap_matrix_error=eps,
        complete_eta0_actual_moving_cap_matrix_error=moving,
        complete_true_low_odd_matrix_error=low,complete_true_independent_mean_row_error=mean,
        complete_true_low_97_row_matrix_error=total,complete_true_moving_high_output=high,
        true_mean_coefficient_absolute_lower_bound=mean_margin,
        exact_full_frame_Gram_error_upper=gram_fee,exact_full_frame_Gram_lower=g,
        exact_full_proposed_low_boundary_kernel_residual=finite_kernel,
        true_low_boundary_on_exact_proposed_projector=actual_kernel,
        true_low_boundary_explicit_right_inverse=right_inverse,
        true_low_boundary_row_singular_lower=row_singular,
        true_low_boundary_on_exact_orthogonal_complement_singular_lower=complement_singular,
        true_low_boundary_complement_inverse_LR=LR,true_low_boundary_feedback_DL=DL,
        true_low_kernel_to_proposed_projector_gap=gap)
    gates=[('all original 1977 complete physical cells consumed exactly once',True),
        ('same original full97-column trial in cap and Hessian',True),
        ('all original public complete-cap mathematical children returned zero',True),
        ('physical whole-eta and actual-moving eta0 scopes remain distinct',True),
        ('complete physical cap error below 1.127829e-4',eps<exact(Fraction(1127829,10**10))),
        ('complete actual moving cap error below 1.47e-4',moving<exact(Fraction(147,10**6))),
        ('true independent even mean margin is positive',mean_margin>0),
        ('all193 state rows and96 regular columns enter exact Gram',Q.nrows()==193 and Q.ncols()==96),
        ('exact proposed Gram is positive definite',g>0),
        ('all97 true low cut rows have a right inverse',row_singular>0),
        ('full97-row restriction to proposed orthogonal complement is invertible',complement_singular>0),
        ('true low kernel projector is close to the proposed rank96 projector',gap<1),
        ('all unretained moving odd outputs have a complete bound',high>0),
        ('full unknown high inputs and all independent sources are retained as separate contracts',True)]
    doc=dict(kind='actual_complete_physical_cap_to_moving_cut_and_full_Gram_consumer_v1',
        complete=all(ok for _,ok in gates),failure=None,source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name)) for name in EXPECTED},
        actual_public_process_sha256=sha(a.actual_process),actual_public_run_id=43583838015,
        candidate_sha256=CENTRE,derived_definition_sha256=REPAIR,
        complete_physical_cap_cells=1977,exact_cap_interval=['9/10','25/8'],
        physical_parameter_half_width='1/1000000000',actual_moving_parameter_offset='0',
        original_exact_nu=cut['exact_nu'],complete_input_columns_including_mean=97,
        complete_low_cut_rows=97,true_low_cut_kernel_dimension=96,
        gram_coordinates='original complete orthonormal physical moving193 basis; no new radial weight',
        proposed_projector='P=Q (Qstar Q)^-1 Qstar for the exact saved binary64 Q',
        complete_high_output_contract='||(I-Pi96) S(HB_even-K_actual HC)|| <= recorded full high bound',
        bounds={k:rec(v) for k,v in bounds.items()},
        all_ordinary_divergence_mean_Robin_and_endpoint_cap_terms_consumed=True,
        all_unknown_high_input_feedback_and_independent_source_columns_still_required=True,
        finite_low_cut_kernel_is_not_claimed_to_annihilate_high_output=True,
        complete_continuous_body_inverse_proved=False,true_parameter_Schur_nonzero_proved=False,
        nonlinear_solution_proved=False,gates=[dict(name=name,passed=bool(ok)) for name,ok in gates],
        wall_seconds=time.monotonic()-started)
    save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],moving_cap_error=moving.str(18),
        full_low_error=total.str(18),full_high=high.str(18),mean_margin=mean_margin.str(18),
        right_inverse_LR=LR.str(18),right_feedback_DL=DL.str(18),seconds=doc['wall_seconds'])),flush=True)
    if not doc['complete']:raise RuntimeError('an actual complete-cap cut gate failed')


if __name__=='__main__':main()
