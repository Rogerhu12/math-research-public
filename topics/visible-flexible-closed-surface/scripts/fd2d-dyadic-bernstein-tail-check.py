#!/usr/bin/env python3
"""One bounded R170 algebra/domain/jet/native-dispatch check; no BVP or body."""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path
import time
import numpy as np
from fd2d_gc_raw_native_field import identity
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily
from fd2d_dyadic_bernstein_tail import (
    DyadicBernsteinControlBox, DyadicBernsteinFlatDevelopableFamily,
    strict_witness_controls, DENOMINATOR)
from fd2d_gc_independent_tail_native_field import IndependentTailPositiveTraceNativeField
from fd2d_gc_dyadic_tail_native import (
    DyadicBernsteinTailNativeField, load_dyadic_tail_body_reader)


def write(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError('Use a new check prefix: '+str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def bernstein_exact(controls, t):
    n = len(controls)-1
    return sum(b*comb(n, i)*t**i*(1-t)**(n-i) for i,b in enumerate(controls))


def max_difference(left, right, prefix=''):
    result = {}
    if isinstance(left, dict):
        if set(left) != set(right):
            raise AssertionError('Different numerical packets: '+prefix)
        for key in left:
            result.update(max_difference(left[key], right[key], prefix+key+'.'))
    elif isinstance(left, np.ndarray) or isinstance(left, (float, int, np.floating)):
        a, b = np.asarray(left), np.asarray(right)
        if a.shape != b.shape:
            raise AssertionError('Different shape: '+prefix)
        result[prefix.rstrip('.')] = float(np.max(np.abs(a-b))) if a.size else 0.
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-definition', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args()
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'*')):
        raise FileExistsError('Use a fresh output prefix')
    started = time.monotonic()
    box = DyadicBernsteinControlBox()
    if not np.array_equal(np.ldexp(box.matrix, 45).astype(np.int64), box.numerators):
        raise AssertionError('Matrix entries are not exact binary64 dyadics')
    if not np.all(np.sum(box.numerators, axis=1) == DENOMINATOR):
        raise AssertionError('Exact rows do not sum to one')
    probe = tuple(Fraction((-1)**i*(i+1), 100+i) for i in range(16))
    restricted = box.coefficients_exact(probe)
    polynomial_checks = []
    for j in range(8):
        for t in (Fraction(0), Fraction(1, 3), Fraction(1)):
            a = bernstein_exact(probe, (j+t)/8)
            b = bernstein_exact(restricted[j*16:(j+1)*16], t)
            if a != b:
                raise AssertionError('Restriction identity failed')
            polynomial_checks.append(dict(interval=j, local_parameter=str(t), exact_equal=True))
    witness_exact = strict_witness_controls()
    certificate_exact = box.certificate(witness_exact, include_local_coefficients=True)
    if not certificate_exact['passed'] or certificate_exact['global_control_box_passed']:
        raise AssertionError('Strict exact witness was lost')
    controls = np.asarray([float(v) for v in witness_exact])
    new_tail = DyadicBernsteinFlatDevelopableFamily(controls)
    tail_definition_path = str(args.out_prefix)+'-tail-definition.json'
    write(tail_definition_path, new_tail.definition())
    tail_reloaded = DyadicBernsteinFlatDevelopableFamily.from_definition(tail_definition_path)
    if not np.array_equal(new_tail.coefficients, tail_reloaded.coefficients):
        raise AssertionError('Tail definition changed controls')

    # Compare exactly the same legal old-box controls through the two real
    # classes, including all returned position/two-jet parameter arrays.
    positive = np.linspace(.2, 1., 16)
    old = PositiveFlatDevelopableFamily(positive)
    same = DyadicBernsteinFlatDevelopableFamily(positive)
    rr = np.array([.32, .53, .8])[:,None]
    uu = np.array([0., .3, .7, 1.1, np.pi/2, 2.2, 4.3])[None,:]
    jets = max_difference(old.evaluate(rr, uu, phase=.13), same.evaluate(rr, uu, phase=.13))
    direction = np.array([(-1.)**i*(i+1)/16 for i in range(16)])
    jvp = max_difference(old.jvp(rr, uu, direction, phase=.13),
                         same.jvp(rr, uu, direction, phase=.13))
    if max(jets.values()) != 0. or max(jvp.values()) != 0.:
        raise AssertionError('The inherited same-polynomial jet calculation changed')
    repair = box.repair_toward_constant(np.full(16, np.nextafter(1.2, np.inf)))
    if repair['info']['input_certificate']['passed'] or not repair['info']['exact_recheck_passed']:
        raise AssertionError('The explicit near-boundary repair was not exercised')
    unchanged = box.repair_toward_constant(controls)
    if not np.array_equal(unchanged['controls'], controls) or unchanged['info']['field_changed']:
        raise AssertionError('A valid witness was needlessly changed')

    # Only two radial labels and two angles: no full native/body recheck.
    parent = IndependentTailPositiveTraceNativeField.from_definition(args.parent_definition)
    same_native = DyadicBernsteinTailNativeField(args.parent_definition, parent.tail.coefficients)
    xx = np.array([parent.trace_start+.004, parent.trace_cut])[:,None]
    xi = np.array([.7, 1.1])[None,:]
    same_native_differences = max_difference(parent.evaluate_angular_native(xx, xi),
                                            same_native.evaluate_angular_native(xx, xi))
    if max(same_native_differences.values()) != 0.:
        raise AssertionError('Same controls changed the complete native field')
    override = DyadicBernsteinTailNativeField(args.parent_definition, controls)
    native_path = str(args.out_prefix)+'-native-definition.json'
    write(native_path, override.definition())
    body = load_dyadic_tail_body_reader(native_path)
    reload_difference = max_difference(override.evaluate_angular_native(xx, xi),
                                      body.native.evaluate_angular_native(xx, xi))
    if max(reload_difference.values()) != 0.:
        raise AssertionError('Complete new schema did not reconstruct the same field')
    cut = body.physical(parent.trace_cut, xi.ravel())
    cut_tail = override.tail.cut_port(xi.ravel(), position_jets=False)
    cut_differences = {key:float(np.max(abs(cut[key]-cut_tail[key])))
                       for key in ('n','m','l','n_u','m_u','l_u')}
    if max(cut_differences.values()) > 2e-14:
        raise AssertionError('The true new cut trace does not match its tail')
    radial_cut_refused = False
    try:
        body.native.evaluate_native(parent.trace_cut, .7)
    except ValueError as error:
        radial_cut_refused = 'radial' in str(error).lower()
    if not radial_cut_refused:
        raise AssertionError('Exact-cut radial scope was silently extended')
    outside = np.ones(parent.parameter_count, bool)
    outside[parent.tail_parameter_slice] = False
    if (not np.array_equal(override.parameters[outside], parent.parameters[outside]) or
            not np.array_equal(override.values, parent.values) or
            not np.array_equal(override.nodes, parent.nodes)):
        raise AssertionError('The explicit override changed a non-tail defining value')
    report = dict(schema='fd2d-R170-bounded-algebra-tail-native-check-v1',
        input_parent_definition=identity(args.parent_definition),
        input_parent_field=identity(parent.arrays_path),
        source=identity(__file__), source_domain=identity(Path(__file__).with_name('fd2d_dyadic_bernstein_tail.py')),
        source_native=identity(Path(__file__).with_name('fd2d_gc_dyadic_tail_native.py')),
        exact_restriction_matrix=box.definition(),
        matrix_exact_dyadic_roundtrip=True, integer_row_sums_exact=True,
        exact_polynomial_restriction_checks=polynomial_checks,
        exact_witness_controls=[str(v) for v in witness_exact],
        exact_witness_certificate=certificate_exact,
        actual_rounded_witness_certificate=new_tail.control_certificate,
        inherited_tail_value_and_jet_comparison=jets,
        nonzero_direction=direction.tolist(), inherited_tail_JVP_comparison=jvp,
        tail_methods_reused_verbatim={name:getattr(DyadicBernsteinFlatDevelopableFamily,name)
            is getattr(PositiveFlatDevelopableFamily,name) for name in
            ('angle_basis','angle_jets','curve','evaluate','cut_port','jvp')},
        near_boundary_contraction=repair['info'], valid_witness_repair_is_identity=True,
        actual_native_labels=dict(s=xx.ravel().tolist(), xi=xi.ravel().tolist()),
        same_controls_complete_native_comparison=same_native_differences,
        explicit_override_reload_comparison=reload_difference,
        true_cut_tail_comparison=cut_differences,
        exact_cut_radial_scope_refused=radial_cut_refused,
        new_tail_class=type(override.tail).__module__+'.'+type(override.tail).__name__,
        new_native_class=type(override).__module__+'.'+type(override).__name__,
        negative_global_controls=override.tail.control_certificate['global_negative_indices'],
        old_parent_archive_or_sources_modified=False,
        override_preserves_all_non_tail_defining_bytes=True,
        generated_tail_definition=identity(tail_definition_path),
        generated_native_definition=identity(native_path),
        body_adapter=body.body_adapter_definition(),
        body_or_BVP_or_whole_FJ_run=False,
        continuous_prefix_or_closed_surface_geometry_certified=False,
        elapsed_seconds=time.monotonic()-started,
        internal_check_passed=True,
        process_exit_is_recorded_separately=True)
    report_path = str(args.out_prefix)+'-report.json'
    write(report_path, report)
    print(json.dumps(dict(report=report_path, check_passed=True,
        exact_witness_global_middle=str(witness_exact[7]),
        exact_witness_local_lower=certificate_exact['local_lower_exact'],
        same_jet_max=max(jets.values()), same_native_max=max(same_native_differences.values()),
        cut_max=max(cut_differences.values()), elapsed_seconds=report['elapsed_seconds']),
        allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
