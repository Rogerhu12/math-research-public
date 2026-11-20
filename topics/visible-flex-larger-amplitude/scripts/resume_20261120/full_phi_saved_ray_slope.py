#!/usr/bin/env python3
"""Read one true Phi derivative along an already paid complete-field direction.

Consumes an actual completed, accepted, single-direction report and its saved
arrays in the same public Actions workspace.  It evaluates the actual accepted
field once and pays one directional JVP.  No new QP, fixture, geometry screen,
or trial acceptance is performed.  All source/data hashes are actual inputs.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            value.update(block)
    return value.hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise SystemExit('The actual derivative is evaluated only in public GitHub Actions.')
    if args.out.exists():
        raise FileExistsError(args.out)
    started = time.monotonic()
    report_path = args.report.resolve()
    report = json.loads(report_path.read_text())
    result = dict(schema='accepted-complete-Phi-saved-ray-true-slope-v1',
        source_sha256=sha(__file__), input_report=str(report_path), input_report_sha256=sha(report_path),
        github_run_id=os.environ.get('GITHUB_RUN_ID'), new_QP_directions=0, new_fixtures=0,
        actual_field_residual_evaluations=0, actual_JVP_calls=0, actual_VJP_calls=0,
        new_nonlinear_acceptance=False, continuous_geometry_claimed=False)
    directions = report.get('directions', [])
    if (not report.get('complete') or len(directions) != 1
            or not directions[0].get('accepted') or report.get('objective') != 'spectral'):
        result.update(status='no_accepted_single_spectral_direction_to_read',
            actual_direction_count=len(directions), scope='No scientific field call was made.')
        write(args.out, result)
        print(json.dumps(result), flush=True)
        return
    direction = directions[0]
    paths = {key: Path(value) for key,value in report['source_paths'].items()}
    required_roles = ('operator','implementation','base_batch','spectral','spectral_hessian')
    for role in required_roles:
        if sha(paths[role]) != report['source_sha256_by_role'][role]:
            raise ValueError('The used scientific source changed: ' + role)
    bundle = Path(report['final_bundle'])
    carrier_path = Path(report['observation_carrier'])
    direction_path = report_path.parent / ('direction-%03d.npz' % direction['index'])
    for path, expected in ((bundle,report['final_bundle_sha256']),
                           (carrier_path,report['observation_carrier_sha256']),
                           (direction_path,direction['direction_sha256'])):
        if sha(path) != expected:
            raise ValueError('An actual saved input changed: ' + str(path))
    import numpy as np
    observed = module('saved_ray_observed_gram', paths['implementation'])
    batch = module('saved_ray_batch_gram', paths['base_batch'])
    spectral = module('saved_ray_spectral_target', paths['spectral'])
    hessian = module('saved_ray_spectral_hessian', paths['spectral_hessian'])
    data = np.load(bundle, allow_pickle=False)
    carrier = np.load(carrier_path, allow_pickle=False)
    saved = np.load(direction_path, allow_pickle=False)
    plan = observed.ObservationPlan.from_arrays(carrier)
    op = observed.create(paths['operator'],data['mesh'],data['a_stages'],
        float(data['radius']),data['fixed_core_first3'],
        M=(data['qjets'].shape[-1]-2)//3,N=report['N'],width=float(data['width']),
        stage_block=64,quarter=True,batch_source=batch,observation_plan=plan,
        a_observations=carrier['a_observations'])
    x, affine = op.pack(data['qjets'],float(data['Hcap']),require_affine=True)
    step = saved['step']
    if step.shape != x.shape:
        raise ValueError('The saved full-free direction uses another space')
    parameters_record = direction['quadratic_model']['bridge']['blocks']
    parameters = spectral.Parameters(p=parameters_record['p'],
        epsilon=parameters_record['epsilon'],scale=parameters_record['scale'])
    radial = op.mixed_stage_weights(report['radial_weights']['legacy_fraction'])
    mass = float(radial.sum()*op.full_N)
    op.set_base(x)
    raw = op.unweight(op.residual(x)).reshape(op.P,op.N,3)
    result['actual_field_residual_evaluations'] = 1
    delta = op.unweight(op.jvp(x,step)).reshape(op.P,op.N,3)
    result['actual_JVP_calls'] = 1
    weights = radial[:,None]*op.multiplicity[None,:]
    primitive = hessian.primitive_gradient(raw,parameters)
    half_factor = parameters.k/(parameters.scale**2*mass)
    true_slope = float(2*half_factor*np.einsum('ij,ijk,ijk->',weights,primitive,delta))
    blocks = hessian.HessianBlocks(raw,parameters)
    whitened = blocks.whiten(delta)
    half_curvature = float(half_factor*np.einsum('ij,ijk,ijk->',weights,whitened,whitened))
    current_stats = spectral.statistics(raw,radial,op.multiplicity,parameters)
    if not np.isfinite(true_slope) or not np.isfinite(half_curvature):
        raise ArithmeticError('The actual scalar derivative is not finite')
    old_mu = float(direction['damping'])
    old_norm2 = float(direction['coordinate_norm'])**2
    ray_damping = old_mu**2*old_norm2
    old_filter = report.get('final_curvature_filter') or {}
    numerical_product = old_filter.get('necessary_reach_product')
    numerical_safety = report['numerical_reach_safety_factor']
    prior_phi = report.get('current',report['initial'])['spectral']['phi_normalized']
    result.update(status='actual_accepted_field_derivative_returned',
        accepted_bundle=str(bundle),accepted_bundle_sha256=sha(bundle),
        direction_path=str(direction_path),direction_sha256=sha(direction_path),
        observation_carrier_sha256=sha(carrier_path),affine=affine,
        used_source_sha256_by_role={role:sha(paths[role]) for role in required_roles},
        actual_accepted_old_alpha=direction['accepted_alpha'],
        fresh_current_statistics=current_stats,
        previous_report_current_Phi=prior_phi,
        fresh_Phi_minus_report=current_stats['phi_normalized']-prior_phi,
        true_current_Phi_directional_derivative=true_slope,
        true_slope_negative=bool(true_slope < 0),
        residual_Hessian_half_ray_curvature=half_curvature,
        previous_coordinate_ray_regularization_energy=ray_damping,
        residual_Hessian_model_increment=(-true_slope/(2*half_curvature)
            if true_slope < 0 and half_curvature > 0 else None),
        previous_mu_model_increment=(-true_slope/(2*(half_curvature+ray_damping))
            if true_slope < 0 and half_curvature+ray_damping > 0 else None),
        known_point_product_from_same_hashed_accepted_report=numerical_product,
        previous_known_point_margin=(numerical_safety-numerical_product
            if isinstance(numerical_product,(float,int)) else None),
        current_geometry_reread=False,
        derivative_formula='2*k/(scale^2*C0) sum radial*orbit <Traw* h(E), J_raw d>; no extra cross factor',
        second_derivative_scope='Positive exact residual-Hessian pullback only; not the complete x-Hessian.',
        conditional_descent_statement=('For the exact finite model, a negative true derivative and strictly positive margins '
            'at every retained geometric/domain point imply some positive sufficiently small actual Armijo step. '
            'The derivative here is evaluated in floating point; all candidate Phi and permanent geometry still require actual rereads.'),
        next_trial_parameterization='x_accepted + eta * original_saved_full_free_step; eta is an increment, not a replacement for the old accepted alpha.',
        seconds=time.monotonic()-started)
    op.clear_base()
    write(args.out,result)
    print(json.dumps(result),flush=True)


if __name__ == '__main__':
    main()
