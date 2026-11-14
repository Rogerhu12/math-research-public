#!/usr/bin/env python3
"""Actual P1 source-only DQ windows in the uniformly translated inner strip.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The existing exact DQ formula, even-frequency membership partition and low
singleton formula are replayed on the actual P1 modal centre. The difference
weights are recomputed at tau_original+2/5, not copied from the old width.
Vprime=(257/256)Vs, the original B floor and all physical source units remain
unchanged. Outputs include 213 x 2 x 13 x 15 shared-window coefficients and
213 x 2 x 13 x 46 separate low-input coefficients. This constructs no ODE,
Green kernel, full nonlinear ball, solution identification or cut theorem.
"""
from fractions import Fraction as Q
import argparse
import ast
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import types

BASE_SHA = 'ecd091b4400b21d66dcc78b0933fe09689ae65473d287f0b119f8782a5e1b673'
LOW_SHA = '58083926d2cbfcc2800f4b694eb59f5aad20cd68fbfc3115dadab15b51aedd22'
INPUT_SHA = 'c23f7f76037247d877a62833f00eb9a96798d4720b8188c5243bc8f128a3c773'
RESOURCE_SHA = '0b042b5eabf6a78702b07dc33e03608110d2033ba469698bb99f40c03e4dc426'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def rational(value):
    return Q(int(value['numerator']), int(value['denominator']))


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--input-resource', type=Path, required=True)
    args, unused = parser.parse_known_args()
    if sha(args.input) != INPUT_SHA or sha(args.input_resource) != RESOURCE_SHA:
        raise ValueError('Use the actual completed P1 +2/5 modal input and its original resource')
    modal, resource = read(args.input), read(args.input_resource)
    domain = modal['domain']
    axes = list(map(rational, domain['T_coordinate_caps_by_mode']))
    if (modal['schema'] != 'inner-R100-uniformly-shifted-Cs-Lambda-modal-v1' or
            not modal['all_gates'] or not all(modal['gates'].values()) or
            resource['exitcode'] != 0 or resource['termination_signal'] is not None or
            resource.get('resource_wrapper_sha256') != 'bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59' or
            domain['name'] != 'R156_actual_full_cut_posterior' or
            rational(domain['S_product_radius']) != Q(3,8) or
            rational(domain['T_l1_radius']) != Q(1,64) or
            len(axes) != 46 or any(axes[:6]) or not all(x > 0 for x in axes[6:]) or
            rational(modal['angular_weight_translation']) != Q(2,5) or
            not modal['original_common_kernel_strip_difference_identity'] or
            not modal['original_high_frame_strip_derivative_unchanged'] or
            modal['full_error_or_infinite_tail_reweighted']):
        raise ValueError('The full actual P1 domain or translated strip identity differs')
    domain_identity = dict(input_schema=modal['schema'], domain=domain,
        parent_full_domain=modal['parent_full_domain'],
        angular_weight_translation=modal['angular_weight_translation'],
        original_weight_definition=modal['old_and_new_weight_definitions'],
        input_sha256=INPUT_SHA, input_resource_sha256=RESOURCE_SHA,
        reference_pair_caps_used_as_saved=True, no_full_error_or_infinite_tail_reweighting=True,
        new_fixedpoint_or_same_solution_identification_claimed=False)
    origin = dict(density_identity=modal['input_identities']['density'],
        old_and_new_weight_definitions=modal['old_and_new_weight_definitions'],
        angular_weight_translation=modal['angular_weight_translation'],
        original_common_kernel_strip_difference_identity=True,
        original_high_frame_strip_derivative_unchanged=True,
        no_density_or_Vprime_renormalization=True)
    del modal, resource
    base_path = Path(__file__).with_name('inner_CsLambda_DQ_window_kernels.py')
    low_path = Path(__file__).with_name('inner_restricted_DQ_windows_and_low_modes_v2.py')
    if sha(base_path) != BASE_SHA or sha(low_path) != LOW_SHA:
        raise ValueError('The frozen DQ formulas or low singleton helper changed')
    spec = importlib.util.spec_from_file_location('frozen_low_singleton_DQ_helper', low_path)
    low = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(low)
    original = base_path.read_text()
    doc = ast.parse(original).body[0]
    old_doc = ''.join(original.splitlines(keepends=True)[doc.lineno-1:doc.end_lineno])
    changes = [
        (old_doc, repr(__doc__)+'\n'),
        ("INPUT_SHA='0816e8e7d62bb5df1df58848dfe8ab1c9a3699210f5df9b9da7e5e31e6a18d93'", "INPUT_SHA='"+INPUT_SHA+"'"),
        ("source['canonical_bootstrap_applied'] and source['schema']=='inner-r100-Cs-Lambda-modal-input-v1'", "source['schema']=='inner-R100-uniformly-shifted-Cs-Lambda-modal-v1'"),
        ("fraction(source['R100_envelope_scale'])==Q(257,256) and fraction(source['transverse_radius'])==Q(1,32)", "fraction(source['R100_envelope_scale'])==Q(257,256) and fraction(source['domain']['T_l1_radius'])==Q(1,64)"),
        ("source['exact_original_continuous_strip_origin']['do_not_renormalize_using_new_strong_density']", "source['original_common_kernel_strip_difference_identity'] and source['original_high_frame_strip_derivative_unchanged']"),
        ("B0=B.numerator//B.denominator;tau=fraction(r['tau_outer_lower'])", "B0=B.numerator//B.denominator;tau=fraction(r['translated_tau_outer_lower'])"),
        ("tau==fraction(d['tau_outer']) and tau>0 and len(r['Cs_plus_Lambda_pair_caps'])==46", "fraction(r['original_tau_outer_lower'])==fraction(d['tau_outer']) and tau==fraction(d['tau_outer'])+Q(2,5) and tau>0 and len(r['Cs_plus_Lambda_pair_caps'])==46"),
        ("normalization=source['normalization'];domain=source['parameter_domain'];origin=source['exact_original_continuous_strip_origin']", "normalization=source['normalization'];domain=source['domain'];origin=_translated_origin"),
        ("                rs.append(pack(bests));re.append(pack(beste));rns.append(at_s);rne.append(at_e)",
         "                check('positive_material_domination_'+str(cell)+'_'+str(wi)+'_'+str(ji),bests>=beste)\n                rs.append(pack(bests));re.append(pack(beste));rns.append(at_s);rne.append(at_e)"),
        ("        rows.append(dict(cell=cell,B_floor=B0,tau_outer_lower=",
         "        low_s,low_e=_low_singletons(OUTPUT_WINDOWS,sums,B0,check,cell,ranges,pack,arb)\n        rows.append(dict(low_singleton_kernels_s_upper=low_s,low_singleton_kernels_ell_upper=low_e,cell=cell,B_floor=B0,tau_outer_lower="),
        ("        parameter_domain=domain,normalization=normalization,original_continuous_strip_origin=origin,",
         "        parameter_domain=domain,normalization=normalization,original_continuous_strip_origin=origin,\n        shifted_P1_input_domain=_domain_identity,original_DQ_source_sha256=_base_sha,\n        low_singleton_helper_sha256=_low_sha,low_singleton_input_modes=MODES,low_singleton_matrix_shape=[213,2,13,46],\n        low_singleton_contract='Each low mode n has its own signed-pair strong Fourier mass; sum separate positive columns against these distinct caps without repeating the common low mass.',\n        actual_difference_weights_recomputed_at_translated_tau=True,\n        material_units_clarification='Relative N uses s*(Vprime/w)^2 and abs(ell)*(Vprime/w)^2. Physical kappa source w*N uses d1=Vprime^2/(r*w) and d_lambda=abs(w_r/w)*Vprime^2/w. No output 1+m is included in these weak-source coefficients.',"),
    ]
    source = original
    for before, after in changes:
        if source.count(before) != 1:
            raise ValueError('The frozen source adapter site is not unique: '+before[:100])
        source = source.replace(before, after, 1)
    reverse = source
    for before, after in reversed(changes):
        if reverse.count(after) != 1:
            raise ValueError('The explicit source adapter cannot be reversed')
        reverse = reverse.replace(after, before, 1)
    if reverse != original:
        raise ValueError('An undeclared original DQ arithmetic site changed')
    ast.parse(source)
    module = types.ModuleType('translated_P1_DQ_original_formula_replay')
    module.__file__ = str(Path(__file__).resolve())
    module.__dict__.update(_low_singletons=low.low_singletons,
        _domain_identity=domain_identity, _translated_origin=origin,
        _base_sha=BASE_SHA, _low_sha=LOW_SHA)
    exec(compile(source, '<actual-P1-shift040-DQ-windows>', 'exec'), module.__dict__)
    module.main()


if __name__ == '__main__':
    main()
