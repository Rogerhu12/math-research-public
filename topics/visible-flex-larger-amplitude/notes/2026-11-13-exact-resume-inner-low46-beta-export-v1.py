#!/usr/bin/env python3
"""Lossless R123-compatible export of actual same-domain complete low46 beta.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No arithmetic or change of field units is performed.
"""
import argparse,gzip,hashlib,json
from pathlib import Path


def read(path):
    with (gzip.open(path,'rt') if path.suffix=='.gz' else path.open()) as stream:
        return json.load(stream)


def pin(path):
    return dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('primary','resource','audit','audit-resource','out'):
        parser.add_argument('--'+key,type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError('Preserve previous actual beta export')
    x=read(args.primary);r=read(args.resource);audit=read(args.audit);ar=read(args.audit_resource)
    assert x['all_gates'] and all(x['gates'].values()) and audit['all_gates']
    assert r['exitcode']==ar['exitcode']==0 and r['termination_signal'] is ar['termination_signal'] is None
    assert audit['primary']['sha256']==pin(args.primary)['sha256']
    assert audit['resource']['sha256']==pin(args.resource)['sha256']
    assert x['domain']==dict(S_product_radius=['1',0],T_l1_radius=['1',-5])
    rows=[]
    for row in x['mode_rows']:
        rows.append(dict(mode=row['mode'],group=row['group'],
          complete_true_beta_cosine_K_coefficient=row['Kbar']['chosen_complete'],
          complete_true_beta_Wsigma1=row['Wsigma1']['chosen_complete'],
          complete_true_beta_Wtau_b1=row['Whead1']['chosen_complete'],
          original_cut_weighted_beta_bound=row['original_cut_weighted_beta_bound']))
    assert [row['mode'] for row in rows]==list(range(2,93,2))
    common=x['common_bounds']
    out=dict(schema='same-R100-complete-low46-actual-source-beta-R123-export-v1',
      author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,
      domain=x['domain'],radius_T=x['domain']['T_l1_radius'],sigma=x['sigma'],head_strip=x['head_strip'],
      all46_mode_rows=rows,
      whole46_true_beta_Kbar=common['Kbar']['chosen_complete'],
      whole46_true_beta_Wsigma1=common['Wsigma1']['chosen_complete'],
      whole46_true_beta_Wtau_b1=common['Whead1']['chosen_complete'],
      T_head_complete_in_original_cut_norm=common['T_cut']['chosen_complete'],
      whole46_complete_beta_to_original_field_norm=common['field']['chosen_complete'],
      T_head_complete_in_original_cut_norm_is_shared=True,
      true_far_added_once=x['complete_true_far_common_at_reference_width2'],
      primary=pin(args.primary),resource=pin(args.resource),independent_exact_audit=pin(args.audit),audit_resource=pin(args.audit_resource),
      source_sha256=pin(Path(__file__))['sha256'],
      primary_paths=dict(mode_rows='mode_rows[i].Kbar/Wsigma1/Whead1.chosen_complete',
        T_shared='common_bounds.T_cut.chosen_complete',true_far='complete_true_far_common_at_reference_width2'),
      original_R123_beta=x['input_identities']['old_beta'],original_R100_cut_weights=x['input_identities']['cut_weights'],
      complete_mean_inverse_far=True,same_original_Sunit_T1over32_domain=True,
      units='complete_true_beta_cosine_K_coefficient equals raw relative physical kappa_perp/w cosine coefficient or full signed Fourier pair mass; no factor2, 1+m, S or w conversion. Use original inner_K_trace_to_canonical_cut_absolute/chosen_axis unchanged.',
      scope='Same original complete inner field beta only. The Lambda linear DN cancels at equal heights; Lambda remains in the nonlinear source and complete true far. No new parameter cut fixed point is asserted.')
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(path=str(args.out),sha256=pin(args.out)['sha256'],bytes=args.out.stat().st_size)))


if __name__=='__main__':main()
