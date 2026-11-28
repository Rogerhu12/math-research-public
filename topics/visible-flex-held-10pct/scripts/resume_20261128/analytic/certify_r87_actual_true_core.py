#!/usr/bin/env python3
"""Run the existing true-integral core oracle on one actual R87 design.

This consumes the complete accepted source and its literal finite support
coefficients.  The zero-phase specialization is the original R53 true core;
the source is not re-labelled as a warm/phase field.  No prefix field, mean,
large Jacobian, BVP, or native tail is built.  This is a core certificate, not
a continuous metric certificate or a completed surface.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def save(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    with temporary.open('w') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def interval(value):
    """Preserve every outward binary endpoint, without decimal rounding."""
    x = np.asarray(value.x)
    if x.shape != (2,) or not np.all(np.isfinite(x)) or x[0] > x[1]:
        raise ArithmeticError('Expected one finite ordered rigorous interval')
    return dict(exact=[str(Q.from_float(float(z))) for z in x],
                display=list(map(float, x)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run', type=Path, required=True)
    parser.add_argument('--original-core-source', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError('Generated oracle evidence stays outside the source repository')
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    beta_path = HERE/'certify_r87_core_beta_from_actual_coefficients.py'
    oracle_path = SCRIPTS/'resume_20261126/warm_phase_validated_core.py'
    support = SCRIPTS/'resume_m3'
    mean = support/'certify_r59_fixed_mean_ranges.py'
    kernel = SCRIPTS/'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py'
    sources = [Path(__file__).resolve(), beta_path, oracle_path,
               support/'r53_validated_material_core.py', mean, kernel,
               SCRIPTS/'resume_transfer/material_flattened_support_core.py',
               args.original_core_source.resolve(),
               SCRIPTS/'resume_20261126/material_design_secant_predictor.py']
    report = dict(schema='actual-R87-complete-true-core-oracle-v1',
        status='validating_actual_complete_source', source_run=ref(args.source_run),
        source_hashes=[ref(path) for path in sources],
        true_core_kind='R53-material-support-true-phase-position-integral',
        zero_phase_specialization=True, source_field_relabelled=False,
        phase_controls_added_to_source=False, prefix_or_mean_built=False,
        large_matrix_or_BVP_or_native_called=False,
        old_core_or_prefix_certificate_reused=False,
        continuous_prefix_metric_certified=False, tail_certified=False,
        whole_surface_geometry_certified=False, readme_completion_claimed=False)

    def progress(value):
        report['progress'] = value
        report['seconds'] = time.monotonic()-started
        report['maximum_rss_KiB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        save(out/'summary.json', report)
        print(json.dumps(dict(value, seconds=report['seconds'])), flush=True)

    progress(dict(stage='actual_original_gate'))
    beta_module = module('_r87_actual_true_core_beta', beta_path)
    scalar = beta_module.certificate(SimpleNamespace(
        historical_note=None, actual_run=args.source_run,
        original_core_source=args.original_core_source, panels=64))
    save(out/'scalar-normalization.json', scalar)
    report['scalar_normalization'] = ref(out/'scalar-normalization.json')
    report['original_BVP_acceptance_revalidated'] = scalar['original_BVP_acceptance_revalidated']
    report['complete_support_coefficients_exact'] = scalar['actual_support_coefficients_exact']
    report['source_settings'] = scalar['source_settings']
    report['source_homotopy_exact'] = scalar['source_homotopy_exact']
    report['actual_lambda_one_core'] = Q(scalar['source_homotopy_exact']) == 1
    record = json.loads(args.source_run.read_text())
    report['raw_return'] = ref(args.source_run.parent/record['raw_return']['file'])
    report['physical'] = ref(args.source_run.parent/'physical.npz')
    if (report['raw_return']['sha256'] != record['raw_return']['sha256']
            or report['physical']['sha256'] != record['physical_sha256']):
        raise ValueError('The accepted source array identity changed after its original gate')
    coefficients = [float(Q(z)) for z in scalar['actual_support_coefficients_exact']]
    original = module('_r87_actual_true_core_original', args.original_core_source)
    material = module('_r87_actual_true_core_material',
                      SCRIPTS/'resume_transfer/material_flattened_support_core.py')
    base = original.PlanarSupportCore(coefficients[0], coefficients[1:], base_mode=3)
    finite = material.MaterialFlattenedSupportCore(base, **scalar['source_settings'])
    if Q.from_float(float(finite.beta)) != Q(scalar['recorded_finite_Gauss_beta_exact']):
        raise ValueError('The actual small source core does not reproduce its recorded finite normalization')
    factory = module('_r87_actual_true_integral_factory', oracle_path)
    v = factory.build_oracle(SimpleNamespace(base_mode=3, baseline=finite,
                                            controls=np.zeros(1)),
                             support, mean, kernel, progress=progress)
    report['true_oracle_metadata'] = v.metadata()
    report['true_beta'] = interval(v.beta)
    report['true_normalized_origin_real'] = interval(v.origin)
    report['origin_imaginary_consistency_interval'] = interval(v.origin_imag_check)
    report['true_sector_turn'] = interval(v.T)
    report['position_partition_cells'] = len(v.pg)-1
    report['normalization_definition'] = (
        'Gamma(0)=integral_0^T i exp(i phi(u)) du / (exp(i T)-1); '
        'reflection proves the imaginary part zero; interval containment is checked, '
        'rather than discarding a sampled imaginary coordinate.')
    blo, bhi = map(Q, scalar['exact_scalar_bounds']['beta'])
    vlo, vhi = map(Q, report['true_beta']['exact'])
    if max(blo, vlo) > min(bhi, vhi):
        raise ArithmeticError('Independent true beta enclosures are disjoint')
    report['independent_true_beta_intervals_overlap'] = True
    fbeta = Q(scalar['recorded_finite_Gauss_beta_exact'])
    report['finite_beta_true_error_upper_exact'] = str(max(abs(fbeta-vlo), abs(fbeta-vhi)))
    report['position_GL_rule'] = dict(
        order=12, analytic_remainder_constant_exact=str(v.gauss_C),
        true_rule_node_max_error_exact=str(v.gauss_node_gap),
        true_rule_weight_l1_error_exact=str(v.gauss_weight_l1),
        source_GL64_position_error_not_substituted=True,
        all_inverse_and_integration_bounds_recomputed=True)
    progress(dict(stage='all_angle_true_curvature'))
    report['complete_true_sector_curvature'] = v.all_angle_curvature_bounds()
    if not report['complete_true_sector_curvature']['positive_curvature_certified']:
        raise ArithmeticError('This actual core has unresolved positive-curvature boxes')
    report['complete_true_core_curvature_certified'] = True
    report['finite_source_phase_derivative_or_position_error_paid'] = False
    report['source_float_core_values_used_as_exact_curve'] = False
    report['status'] = 'actual_complete_true_core_and_normalization_returned'
    report['seconds'] = time.monotonic()-started
    report['maximum_rss_KiB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report['versions'] = dict(python=sys.version, numpy=np.__version__, mpmath=mp.__version__)
    for item in report['source_hashes']:
        if sha(item['path']) != item['sha256']:
            raise ValueError('A source changed during the oracle calculation')
    save(out/'summary.json', report)
    print(json.dumps(dict(status=report['status'], summary=str(out/'summary.json'),
        sha256=sha(out/'summary.json'), seconds=report['seconds'],
        maximum_rss_KiB=report['maximum_rss_KiB'],
        beta=report['true_beta']['display'],
        curvature=report['complete_true_sector_curvature'])), flush=True)


if __name__ == '__main__':
    main()
