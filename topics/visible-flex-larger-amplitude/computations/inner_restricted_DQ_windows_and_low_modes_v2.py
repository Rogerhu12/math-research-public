#!/usr/bin/env python3
"""Original DQ arithmetic on one strictly pinned restricted R100 modal input.

Preserves the original 213 x 13 x 15 two-material kernel and additionally
retains all 46 low input modes separately.  No source or Green integration.
The restricted S/T domain is read exactly; Cs is NOT scaled by 3/4.
Author: geometry_audit (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
from fractions import Fraction
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import types

BASE_SHA = 'ecd091b4400b21d66dcc78b0933fe09689ae65473d287f0b119f8782a5e1b673'
INPUT_SHA = 'd74b5972d555086b0e5dc9b7b63f6b7ee0a6399838f077da538bd79cfd497968'
INPUT_RESOURCE_SHA = '64f0621c647f379dc11a332cc7579a8149a4f2f479d6c32d932695d1e4d1222f'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p = Path(path)
    with gzip.open(p,'rt') if p.suffix == '.gz' else p.open() as f:
        return json.load(f)


def rational(x):
    return Fraction(int(x['numerator']),int(x['denominator']))


def main():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--input-resource',type=Path,required=True)
    args, unused = p.parse_known_args()
    if digest(args.input) != INPUT_SHA or digest(args.input_resource) != INPUT_RESOURCE_SHA:
        raise ValueError('Use this completed restricted input and its own exact resource record')
    d, resource = read(args.input), read(args.input_resource)
    if (d['schema'] != 'inner-R100-Cs-Lambda-restricted-profile-modal-input-v1'
            or not d['all_gates'] or not all(d['gates'].values())
            or resource['exitcode'] != 0 or resource['termination_signal'] is not None
            or resource.get('resource_wrapper_sha256') != 'bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59'):
        raise ValueError('Restricted producer has not formally completed all original gates')
    domain = d['domain']
    caps = list(map(rational,domain['T_coordinate_caps_by_mode']))
    if (domain['name'] != 'expanded_profile'
            or rational(domain['S_product_radius']) != Fraction(3,4)
            or rational(domain['T_l1_radius']) != Fraction(1,32)
            or len(caps) != 46 or any(caps[:6]) or not all(v>0 for v in caps[6:])
            or not d['gates']['domain_inside_original_R100']
            or not d['gates']['Cs_full_unit_envelope_valid_on_subset']):
        raise ValueError('Wrong simultaneous S/T subset or incomplete transverse axes')
    restricted = dict(input_schema=d['schema'],domain=domain,
                      parent_full_domain=d['parent_full_domain'],
                      restriction_provenance=d['restriction_provenance'],
                      reference_Cs_remains_full_unit_envelope=True,
                      input_resource_sha256=INPUT_RESOURCE_SHA)
    del d, resource
    base_path = Path(__file__).with_name('inner_CsLambda_DQ_window_kernels.py')
    if digest(base_path) != BASE_SHA:
        raise ValueError('Original DQ formula source changed')
    original = base_path.read_text()
    changes = [
      ("INPUT_SHA='0816e8e7d62bb5df1df58848dfe8ab1c9a3699210f5df9b9da7e5e31e6a18d93'",
       "INPUT_SHA='"+INPUT_SHA+"'"),
      ("source['schema']=='inner-r100-Cs-Lambda-modal-input-v1'",
       "source['schema']=='inner-R100-Cs-Lambda-restricted-profile-modal-input-v1'"),
      ("normalization=source['normalization'];domain=source['parameter_domain'];origin=source['exact_original_continuous_strip_origin']",
       "normalization=source['normalization'];domain=source['domain'];origin=source['exact_original_continuous_strip_origin']"),
      ("        rows.append(dict(cell=cell,B_floor=B0,tau_outer_lower=",
       "        low_s,low_e=_low_singletons(OUTPUT_WINDOWS,sums,B0,check,cell,ranges,pack,arb)\n"
       "        rows.append(dict(low_singleton_kernels_s_upper=low_s,low_singleton_kernels_ell_upper=low_e,cell=cell,B_floor=B0,tau_outer_lower="),
      ("        parameter_domain=domain,normalization=normalization,original_continuous_strip_origin=origin,",
       "        parameter_domain=domain,normalization=normalization,original_continuous_strip_origin=origin,\n"
       "        restricted_input_domain=_restricted,original_DQ_source_sha256=_base_sha,\n"
       "        low_singleton_input_modes=MODES,low_singleton_matrix_shape=[213,2,13,46],\n"
       "        low_singleton_contract='Each low mode n has its own signed-pair strong Fourier mass; sum the 46 positive columns against those distinct caps. No low common mass is repeated 46 times.',\n"
       "        material_units_clarification='In relative N the materials are s*(Vprime/w)^2 and abs(ell)*(Vprime/w)^2. For physical kappa source w*N, the radial materials are d1=Vprime^2/(r*w) and d_lambda=abs(w_r/w)*Vprime^2/w.',"),
    ]
    source = original
    for before,after in changes:
        if source.count(before) != 1:
            raise ValueError('Original source anchor is not unique')
        source = source.replace(before,after)
    module = types.ModuleType('restricted_DQ_original_formula_replay')
    module.__file__ = str(Path(__file__).resolve())
    module.__dict__.update(_low_singletons=low_singletons,_restricted=restricted,_base_sha=BASE_SHA)
    exec(compile(source,str(base_path),'exec'),module.__dict__)
    module.main()


def low_singletons(windows,sums,B0,check,cell,ranges,pack,arb):
    ss, ee = [], []
    zero = ['0',0]
    for wi,window in enumerate(windows):
        rs, re = [], []
        for n in range(2,93,2):
            plus,minus = ranges(window,n)
            # Both centre and input are <=92.  Their difference is <=90,
            # so only the unchanged k+n support can enter any output>=94.
            if minus is not None:
                raise ArithmeticError('A low-input difference entered an output >=94')
            s0,s1 = (sums[plus][0],sums[plus][1]) if plus else (arb(0),arb(0))
            gs = (arb(5*n)*s1/(4*(1+n))).upper()
            # k,n<=92 and B0>=120 give the exact old ell reduction=1.
            ge = (s0/(1+n)).upper()
            if not (5*n<=4*B0 and ((gs==0 and ge==0)==(plus is None))):
                raise ArithmeticError('A singleton low support or exact ell reduction failed')
            # Positive coefficientwise common-material domination is kept.
            if not gs>=ge:
                raise ArithmeticError('Common material coefficient domination failed')
            rs.append(pack(gs) if gs else zero);re.append(pack(ge) if ge else zero)
        check(f'low_singleton_all46_support_and_coefficient_gates_{cell}_{wi}',len(rs)==len(re)==46)
        ss.append(rs);ee.append(re)
    return ss,ee


if __name__ == '__main__':
    main()
