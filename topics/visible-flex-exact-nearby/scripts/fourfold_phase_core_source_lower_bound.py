#!/usr/bin/env python3
"""A true lower bound for the chosen R107 weak-load representation on one leaf.

The finite Gram and its complete true-function difference come from the
executed exact-time source producer. This is not a lower bound for the
intrinsic PDE inverse or for all possible equivalent flux representations.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from flint import arb, ctx


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def exact_float(x):
    n, d = float(x).as_integer_ratio()
    return arb(n)/d


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-report', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise ValueError('Use a fresh output path')
    ctx.prec = 256
    j = json.loads(args.source_report.read_text())
    scripts = Path(__file__).parent
    if not j.get('complete') or j['source_sha256'] != sha(scripts/'fourfold_phase_core_even_weak_residual_exact.py'):
        raise ValueError('Need the completed unchanged actual source certificate')
    if sha(j['arrays']['path']) != j['arrays']['sha256']:
        raise ValueError('Changed source Gram arrays')
    for name, value in j['dependency_sha256'].items():
        if sha(scripts/name) != value:
            raise ValueError('Changed actual source dependency: '+name)
    if not (j['physical_modes']==4 and j['physical_input_columns']==5 and
            j['finite_time_integration_exact'] and j['angular_mean_retained']):
        raise ValueError('Unexpected physical normalization or omitted mean')
    record = j['records']['Hthreehalf']['components']['radial_all']
    with np.load(j['arrays']['path'], allow_pickle=False) as a:
        G = a['finite_PSD_Gram_majorant_centers'][
            j['component_order'].index('radial_all'),
            j['space_order'].index('Hthreehalf')]
    diagonal = G[4,4]
    if diagonal.imag != 0:
        raise ValueError('A Hermitian Gram diagonal must be real')
    selection = arb(record['finite_PSD_Gram_selection_error']['ball']).upper()
    difference = arb(record['complete_actual_residual_L2r_Hs_difference']['ball']).upper()
    rayleigh = (exact_float(diagonal.real)-selection).lower()
    if not rayleigh > 0:
        raise ValueError('The chosen exact coordinate gives no positive finite norm')
    finite_lower = rayleigh.sqrt().lower()
    lower = (finite_lower-difference).lower()
    if not lower > arb(31):
        raise ValueError('The stated actual chosen-source lower gate failed')
    from fourfold_phase_beta_interval import ball_record
    result = dict(
        kind='actual_one_leaf_chosen_weak_source_lower_bound', complete=True,
        source_sha256=sha(__file__),
        input_report=dict(path=str(args.source_report),sha256=sha(args.source_report)),
        input_array=j['arrays'], exact_physical_interval=j['exact_physical_interval'],
        exact_parameter_interval=j['identity'].get('exact_parameter_interval'),
        identity=j['identity'],
        exact_unit_input=[0,0,0,0,1],
        normalization='The same five normalized paired cosine height inputs as the completed source producer; positive radial leaf only.',
        component='Rr in L2(dr; H^(3/2)(physical 4Z))',
        finite_Gram_Rayleigh_lower=ball_record(rayleigh),
        finite_source_norm_lower=ball_record(finite_lower),
        complete_true_minus_finite_operator_upper=ball_record(difference),
        actual_source_norm_lower=ball_record(lower),
        complete_three_source_operator_lower=ball_record(lower),
        exact_upper_report_preserved=True,
        intrinsic_PDE_residual_lower_bound=False,
        no_global_inverse_obstruction_claimed=True,
        scope='This proves the saved weak flux representation of the existing finite-core reference is not small in the R107/R110 strong source norm. Equivalent solenoidal gauges, a better reference, or an actual full solver can change this quantity. No failure of the geometric construction or the true PDE inverse follows.',
    )
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(complete=True,finite_source_norm_lower=ball_record(finite_lower),
                         actual_source_norm_lower=ball_record(lower)),indent=2))


if __name__=='__main__':
    main()
