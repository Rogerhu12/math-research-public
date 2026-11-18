#!/usr/bin/env python3
"""Bind the completed q060 trace initializer to the R40 radius-monotonic corollary.

Only exact arithmetic on saved parameters and source hashes is performed.
No old integral, core, inverse, collocation, Jacobian or BVP is evaluated.
The R40 lower sum is a cited proved input, not recomputed by this script.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import struct
import sys


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent.parent
INPUT = HERE.parent/'resume_m3/q060_circle_trace_initializer_terminal.json'
INPUT_SHA = '8c478f12c2472a3df75017613e606adf801282a7d5f413aec48e14705bc5aa75'
R40_RECORD = HERE.parent/'resume_m3/smallq_ramp_window_execution.json'
R40_RECORD_SHA = '330829a9b6ca456b4d4ead8b041af197a011fbe023b8568f7c5cadbbb9d51c82'
R40_PROOF = TOPIC/'results/R40-small-q-actual-flat-ramp-characteristic-window.md'
R40_PROOF_SHA = '9b6c4c434a2994a2f4a6e68e591d6de4232a5e85876b74523c9a71aff79547ac'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def packed(values):
    return struct.pack('<'+'d'*len(values), *values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Preserve the existing parameter-binding record')
    for path, expected in ((INPUT, INPUT_SHA), (R40_RECORD, R40_RECORD_SHA),
                           (R40_PROOF, R40_PROOF_SHA)):
        assert sha(path) == expected, str(path)
    state = json.loads(INPUT.read_text())
    old = json.loads(R40_RECORD.read_text())
    old_literal = old['certificate_summary']['checkpoint_binary_parameters']
    published = F('0.2108827779904414')
    assert old['result'] == 'R40' and old['exit_code'] == 0
    assert old_literal['gates']['lower_above_published']
    assert F(old_literal['lower_decimal_rounded_down']) > published
    for path, digest in state['source_sha256'].items():
        assert sha(path) == digest, path
    for name in ('probe', 'resource'):
        item = state[name]
        assert sha(item['path']) == item['sha256'], name
    settings = state['new_core_settings']
    assert settings['halfwidth'] == .21 and settings['homotopy'] == 1.
    assert settings['bimodal_eta'] == 0. and settings['lock_fundamental'] is True
    actual = state['actual_core']
    assert actual['summary']['core_kind'] == 'exact_m3_circle_trace_replacement_integral'
    assert actual['summary']['control_path'] == 'circle-trace-replace-last-two-v1'
    controls, parameters, scales = (actual[key] for key in
                                   ('physical_controls', 'parameters', 'parameter_scales'))
    assert len(controls) == len(scales) == 7 and len(parameters) == 8
    assert packed([p*s for p, s in zip(parameters[1:], scales)]) == packed(controls)
    assert parameters[0] == 0. and state['finite_initializer']['original_initial_domain_passed']
    q = F.from_float(state['new_primary_q']['binary64'])
    t = F.from_float(controls[-2])
    radius = 1+8*q+t
    profile = state['physical_profile']
    assert profile['direction'] == 'outward' and profile['ramp_law'] == 'flat'
    v, eps, eta, delta = (F.from_float(profile[key]) for key in ('vu', 'ramp', 'ramp_eta', 'delta'))
    assert (v, eps, eta) == tuple(F(old_literal[key]) for key in ('vu', 'eps', 'eta'))
    radius_min, delta_min = F(164, 125), F(3, 50)
    B, Bmin = delta*eps/(1-eps), delta_min*eps/(1-eps)
    y, ymin = radius*v, radius_min*v
    gates = dict(radius_above_reference=radius >= radius_min,
                 delta_above_reference=delta >= delta_min,
                 B_above_reference=B >= Bmin,
                 y_above_reference=y >= ymin,
                 y_below_one=y < 1,
                 inherited_lower_above_halfwidth=published > F(21, 100))
    assert all(gates.values())
    record = dict(
        scope=__doc__, source=ref(__file__), command=[sys.executable, *sys.argv],
        completed_initializer=ref(INPUT), R40_proof=ref(R40_PROOF), R40_execution=ref(R40_RECORD),
        original_source_hashes_verified=len(state['source_sha256']),
        full_seven_control_chain_binary64_verified=True,
        complete_physical_control_binary64_sha256=hashlib.sha256(packed(controls)).hexdigest(),
        radius_definition='R=1+8*q+t; actual physical trace coefficient t=parameters[-2]*scales[-2]',
        exact_parameters={name: str(value) for name, value in
                          (('q', q), ('t', t), ('R', radius), ('vu', v), ('ramp', eps),
                           ('ramp_eta', eta), ('delta', delta), ('B', B), ('y', y))},
        reference_parameters={name: str(value) for name, value in
                              (('R_min', radius_min), ('delta_min', delta_min), ('B_min', Bmin), ('y_min', ymin))},
        cited_strict_lower=str(published), angular_halfwidth='21/100', gates=gates,
        physical_inference='R40 J(B,y) increases in both B and y on 0<=y<1. The same binary64-literal ramp therefore has chi(L)/R > 0.2108827779904414 > .21 for this saved initializer.',
        integrals_recomputed=False, core_constructed=False, inverse_evaluated=False,
        collocation_or_Jacobian_evaluated=False, BVP_solver_invoked=False,
        limits='This binds a local circular-data cone budget to the saved initializer. It is not BVP existence, disappearance of the circular patch outside the cone, full metric, holding/reach or a terminal-state claim. A later delta or t must satisfy the same stated inequalities anew.')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x') as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(output=str(args.out.resolve()), sha256=sha(args.out),
                          R_fraction=str(radius), Rv_float_for_display=float(y), all_gates=True)))


if __name__ == '__main__':
    main()
