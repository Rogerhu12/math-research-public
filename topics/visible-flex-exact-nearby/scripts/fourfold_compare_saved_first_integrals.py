#!/usr/bin/env python3
"""Cross-check complete finite first integrals from two true-density proofs."""
from pathlib import Path
from fractions import Fraction
import argparse
import gzip
import json
from flint import arb,acb,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_actual_field_fourier_package import decode_complex,read_dyadic


def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)


def upper(row):return arb(row['upper']).upper()


def decode_enclosure(row):
    return acb(*[arb(read_dyadic(mid),read_dyadic(radius)) for mid,radius in row])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--old-density',type=Path,default=Path('notes/2026-11-12-actual-forward419-complete-reference-density.json'))
    p.add_argument('--old-integrals',type=Path,default=Path('data/phase_ring_continuation/step5_forward419_two_chronological_integrals.json.gz'))
    p.add_argument('--new-density',type=Path,default=Path('data/phase_ring_continuation/step5_forward_density_pipeline_pilot419_Q1024/forward_0419_ef134f2a18.json.gz'))
    p.add_argument('--inner-strip',default='1/512');p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx.prec=args.bits
    old=read(args.old_density);old_int=read(args.old_integrals);new=read(args.new_density)
    if (not old.get('complete_continuous_true_density_proved_on_this_segment')
        or not new.get('complete_continuous_true_density_proved')
        or old_int['density_manifest_sha256']!=old['density_polynomial_manifest_sha256']):
        raise ValueError('completed actual density and matched old integrals required')
    a,b=old['identity']['reference'],new['identity']['reference']
    for key in ('retarget_descriptor_sha256','leg','segment','normalized_subspan',
                'exact_segment_time_rows','branch_sign','target_exact_delta_fraction',
                'target_object_sha256','target_root_sha256'):
        if a[key]!=b[key]:raise ValueError('the two exact reference identities differ: '+key)
    if old_int['identity']!=old['identity']:raise ValueError('old integral identity differs')
    record=new['first_integral_file']
    if sha(record['path'])!=record['sha256']:raise ValueError('new integral bytes changed')
    new_int=read(record['path'])
    if (new_int['identity']!=new['identity']
        or new_int['density_coefficient_sha256']!=new['density_coefficient_sha256']):
        raise ValueError('new exact integral belongs to another chosen polynomial')
    first=[decode_complex(z) for z in old_int['first']]
    second=[decode_enclosure(z) for z in new_int['coefficients']]
    S=min(Fraction(old['initial_label_strip']),Fraction(new['label_strip']))
    s=Fraction(args.inner_strip)
    if not 0<=s<S:raise ValueError('a genuine inner label strip is required')
    difference=arb(0)
    for k in range(max(len(first),len(second))):
        v=(first[k] if k<len(first) else acb(0))-(second[k] if k<len(second) else acb(0))
        difference+=abs(v)*(1 if k==0 else 2*(k*exact_arb(s)).exp())
    difference=difference.upper()
    Eold=upper(old['R72_inputs_on_this_whole_segment']['integrated_approximation_error_E'])
    Enew=upper(new['R72_inputs']['integrated_approximation_error_E'])
    old_choice=upper(old_int['complete_choice_error_on_outer_strip']['first'])
    gap=exact_arb(S-s);factor=(2*gap.coth()-1).sqrt().upper()
    allowance=((Eold+Enew)*factor+old_choice).upper()
    if not difference<allowance:raise ValueError('independent exact finite first integrals violate their true error budgets')
    result=dict(kind='independent_complete_saved_first_integral_comparison',complete=True,
        source_sha256=sha(__file__),bits=args.bits,old_density_sha256=sha(args.old_density),
        old_integrals_sha256=sha(args.old_integrals),new_density_sha256=sha(args.new_density),
        new_integrals_sha256=record['sha256'],same_actual_reference_identity_fields_checked=True,
        comparison_strip=str(s),common_true_error_strip=str(S),
        all_modes_retained=True,complete_finite_difference_A_norm=ball_record(difference),
        Hardy_factor=ball_record(factor),sum_of_true_error_budget_allowance=ball_record(allowance),
        comparison_passed=True,
        scope='Independent complete finite first-integral consistency check, not an additional full-flow or KAM assertion.')
    args.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)


if __name__=='__main__':main()
