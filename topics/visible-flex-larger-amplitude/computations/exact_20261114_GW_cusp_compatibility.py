#!/usr/bin/env python3
"""Replay one saved GW cusp window and separate the position compatibility term.

The packet contains original point bytes, not precomputed GW second jets.
The hash-locked original TargetMetricTail reconstructs those jets in Actions.
No ODE, shooting solve, default-rr rule, or global replacement field is used.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(65536), b''):
            h.update(block)
    return h.hexdigest()


def write_json(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def read_verified(packet, name, record):
    path = (packet / name).resolve()
    if not path.is_relative_to(packet) or sha(path) != record['sha256']:
        raise ValueError('Changed or escaped packet input: ' + name)
    if path.stat().st_size != record['bytes']:
        raise ValueError('Changed packet size: ' + name)
    return path


def rational_worst_rr(layer, radius):
    """Exact arithmetic on the binary64 GW Fourier nodal coefficients at theta=0.

    This removes polynomial/FFT evaluation rounding from this shadow only.
    It cannot remove errors already present in the original point data or in
    the original GW nodal reconstruction / binary64 Fourier transform.
    """
    def node(c):
        out = []
        for coordinate in range(3):
            values = c[:, coordinate].real
            if any(type(value)(float(value)) != value for value in values):
                raise ValueError('Expected original binary64 Fourier coefficients')
            out.append(sum((Fraction.from_float(float(v)) for v in values), Fraction(0)))
        return out

    d0, v0, a0 = (node(c) for c in layer['nodes'][0])
    d1, v1, a1 = (node(c) for c in layer['nodes'][1])
    r0, r1 = (Fraction.from_float(float(r)) for r in layer['r'])
    h = r1 - r0
    u = (Fraction.from_float(float(radius)) - r0) / h
    answer = {'P_rr': [], 'Q_cusp_rr': [], 'compatibility_rr': [],
              'E_theta_zero': [], 'all_polynomial_identity_coefficients_zero': True}
    for j in range(3):
        aa, bb = h*h*a0[j], h*h*a1[j]
        dy, dv = d1[j]-d0[j]-h*v0[j], h*(v1[j]-v0[j])
        p = [d0[j], h*v0[j], aa/2,
             10*dy-4*dv-3*aa/2+bb/2,
             -15*dy+7*dv+3*aa/2-bb,
             6*dy-3*dv-aa/2+bb/2]
        e = d1[j]-d0[j]-h*(v0[j]+v1[j])/2-h*h*(a0[j]-a1[j])/12
        q = [d0[j]+e, h*v0[j], aa/2,
             h*(v1[j]-v0[j])-h*h*(2*a0[j]+a1[j])/3,
             h*(v0[j]-v1[j])/2+h*h*(a0[j]+a1[j])/4, Fraction(0)]
        correction = [-e, Fraction(0), Fraction(0), 10*e, -15*e, 6*e]
        if any(p[k]-q[k]-correction[k] for k in range(6)):
            raise ArithmeticError('Exact Hermite compatibility identity failed')
        for key, polynomial in [('P_rr', p), ('Q_cusp_rr', q),
                                ('compatibility_rr', correction)]:
            value = sum((k*(k-1)*polynomial[k]*u**(k-2)/h**2
                         for k in range(2, 6)), Fraction(0))
            answer[key].append(float(value))
        answer['E_theta_zero'].append(float(e))
    answer['physical_u'] = float(u)
    answer['scope'] = ('Exact rational operations on the existing binary64 GW Fourier '
                       'nodal data at theta=0; not a higher-precision ODE/GW reconstruction.')
    return answer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True, help='New output directory')
    parser.add_argument('--angles', type=int, default=1024)
    args = parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise RuntimeError('Numerical consumption is restricted to this public repository Actions')
    if args.angles < 1024 or args.angles % 2:
        raise ValueError('Use an even grid with at least the original 1024 angles')
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[key] = '1'
    start = time.monotonic()
    packet, out = args.packet.resolve(), args.out.resolve()
    manifest_path = packet / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    if manifest.get('schema') != 'original-GW-cusp-input-byte-extraction-v1':
        raise ValueError('Unexpected packet schema')
    if manifest['saved_GW_Cartesian_second_jet_arrays_exist'] or not manifest['GW_node_jets_must_be_reconstructed_in_Actions']:
        raise ValueError('Packet must accurately identify its original point-data scope')
    hashes = {str(Path(__file__).resolve()): sha(__file__), str(manifest_path): sha(manifest_path)}
    for name, digest in manifest['consumed_source_sha256'].items():
        path = HERE / name
        if sha(path) != digest:
            raise ValueError('Original GW numerical source changed: ' + name)
        hashes[str(path)] = digest
    for table in ('row_files', 'node_files'):
        for name, record in manifest[table].items():
            path = read_verified(packet, name, record)
            hashes[str(path)] = record['sha256']
    original_report = manifest['original_report_file']
    reference_path = read_verified(packet, original_report['path'], original_report)
    reference = json.loads(reference_path.read_text())
    hashes[str(reference_path)] = original_report['sha256']
    out.mkdir(parents=True, exist_ok=False)
    write_json(out / 'intent.json', dict(argv=sys.argv, source_and_input_sha256=hashes,
        original_common_stage=450, no_ODE_or_shooting_solve=True, default_rr_used=False,
        reconstructed_GW_node_jets=True, global_field_adopted=False, task_completed=False))

    import numpy as np
    import exact_20261114_common_grid_refinement as core
    from exact_20261114_refined_tail_adapter import hermite
    from exact_20261114_source_knot_rr_probe import TargetMetricTail

    background = json.loads((packet / manifest['background_row_file']).read_text())
    if background['stage'] != 450 or background['originalStage'] != 28:
        raise ValueError('This packet must contain the retained source-stage-28 cusp window')
    points = background['points']
    r = np.asarray([p['r'] for p in points], np.longdouble)
    if len(points) != 17 or any(float(x) >= .29 for x in r):
        raise ValueError('Expected original 17-point window outside the fixed outer cut patch')
    theta = 2*np.pi*np.arange(args.angles)/args.angles
    layers, archived_arrays = {}, {}

    def jets(c, radial, r0, h):
        u = (radial-r0)/h
        if u.min() < -1e-12 or u.max() > 1+1e-12:
            raise ValueError('Local window leaves the packaged physical interval')
        u = np.clip(u, 0, 1)
        angular = core.angle_coefficients(c, args.angles)
        return {name: core.evaluate(angular[t], u, h, d)
                for name, (d, t) in core.JET_RULES.items()}

    def maximum(values):
        at = np.unravel_index(np.argmax(values), values.shape)
        return dict(value=float(values[at]), source_subinterval_x=points[at[0]]['x'],
                    r=points[at[0]]['r'], theta=float(theta[at[1]]))

    def jet_sizes(values):
        return {key: maximum(np.linalg.norm(value, axis=-1)) for key, value in values.items()}

    def differences(left, right):
        return {key: right[key]-left[key] for key in core.JET_RULES}

    with tempfile.TemporaryDirectory(prefix='GW-cusp-', dir=out) as temporary:
        for label in ('coarse', 'fine'):
            spec = manifest['layers'][label]
            rows = []
            for item in spec['rows']:
                row = json.loads((packet/item['row_file']).read_text())
                if row['node'] != item['original_rows_index']:
                    raise ValueError('Original node index changed')
                row['file'] = str(packet/item['node_file'])
                rows.append(row)
            mini = Path(temporary)/(label+'.json')
            write_json(mini, dict(finished=True, angular=spec['angular'], rows=rows,
                schema='explicit-two-node-input-view-not-a-complete-tail',
                original_complete_sha256=spec['original_complete_sha256']))
            tail = TargetMetricTail(mini)
            nodes = [tail.node_coefficients(i) for i in range(2)]
            d0, v0, a0 = nodes[0]
            d1, v1, a1 = nodes[1]
            h = tail.r[1]-tail.r[0]
            e = d1-d0-h*(v0+v1)/2-h*h*(a0-a1)/12
            p = hermite(d0, d1, v0, v1, a0, a1, h)
            q = np.zeros_like(p)
            # Integral of the shared cubic velocity, anchored at the common cusp.
            q[0], q[1], q[2] = d0+e, h*v0, h*h*a0/2
            q[3] = h*(v1-v0)-h*h*(2*a0+a1)/3
            q[4] = h*(v0-v1)/2+h*h*(a0+a1)/4
            correction = np.zeros_like(p)
            correction[0], correction[3], correction[4], correction[5] = -e, 10*e, -15*e, 6*e
            value = {name: jets(poly, r, tail.r[0], h)
                     for name, poly in [('P', p), ('Q_cusp', q), ('compatibility', correction)]}
            for name in ('P', 'Q_cusp'):
                value[name]['position'][:, :, 2] -= np.longdouble(spec['small_mean_at_cut'])
            geom = {name: core.measured_geometry(value[name], r, points, theta)
                    for name in ('P', 'Q_cusp')}
            closure = {key: value['P'][key]-value['Q_cusp'][key]-value['compatibility'][key]
                       for key in core.JET_RULES}
            e_polynomial = np.zeros_like(p); e_polynomial[0] = e
            e_angles = core.angle_coefficients(e_polynomial, args.angles)[0][0]
            ee = float(np.max(np.linalg.norm(e_angles, axis=-1)))
            layers[label] = dict(r=tail.r.copy(), nodes=nodes, value=value, geometry=geom,
                report=dict(original_label=spec['original_label'], r_interval=[float(x) for x in tail.r],
                    h=float(h), original_node_rows=spec['rows'], GW_node_diagnostics=tail.diag,
                    E_max_at_sampled_angles=ee,
                    E_over_h_squared_max_at_sampled_angles=float(ee/h**2),
                    compatibility_rr_sup_over_physical_u_at_sampled_angles=float(10*ee/(np.sqrt(3)*h**2)),
                    cusp_anchor='Q(r_cusp,theta)=the original common cusp position; P-Q=E*(S-1).',
                    coefficient_identity_residual=float(np.max(abs(p-q-correction))),
                    evaluated_identity_residual=jet_sizes(closure),
                    finite_window_jet_norms={name:jet_sizes(data) for name,data in value.items()},
                    finite_window_geometry={name:{key:maximum(z) for key,z in data.items()} for name,data in geom.items()},
                    metric_scalar_change_P_to_Q=maximum(abs(geom['Q_cusp']['metric']-geom['P']['metric'])),
                    kappa_scalar_change_P_to_Q=maximum(abs(geom['Q_cusp']['kappa']-geom['P']['kappa']))))
            for endpoint, data in enumerate(nodes):
                for name, c in zip(('position', 'radial_first', 'radial_second'), data):
                    archived_arrays[label+'_node'+str(endpoint)+'_'+name+'_coefficients'] = np.asarray(c, np.complex128)
            for name, c in [('P',p), ('Q_cusp',q), ('compatibility',correction), ('E',e)]:
                archived_arrays[label+'_'+name+'_coefficients'] = c
            archived_arrays[label+'_r'] = tail.r.copy()

    comparison = {}
    for name in ('P', 'Q_cusp', 'compatibility'):
        comparison[name] = jet_sizes(differences(layers['coarse']['value'][name], layers['fine']['value'][name]))
    for name in ('P','Q_cusp'):
        comparison[name]['metric_scalar_difference'] = maximum(abs(
            layers['fine']['geometry'][name]['metric']-layers['coarse']['geometry'][name]['metric']))
        comparison[name]['kappa_scalar_difference'] = maximum(abs(
            layers['fine']['geometry'][name]['kappa']-layers['coarse']['geometry'][name]['kappa']))
    witness = reference['adjacent_comparisons'][0]['witnesses']['radial_second']
    point_index = next(i for i,p in enumerate(points) if p['r']==witness['r'] and p['x']==witness['x'])
    if witness['theta'] != 0 or witness['common_stage'] != 450:
        raise ValueError('Expected the original theta-zero rr witness')
    witness_data = dict(original_witness=witness,
        original_saved_global_rr_difference=reference['adjacent_comparisons'][0]['maxima']['radial_second'],
        layers={})
    for label in ('coarse','fine'):
        layer = layers[label]
        record = {name:[float(x) for x in data['radial_second'][point_index,0]]
                  for name,data in layer['value'].items()}
        shadow = rational_worst_rr(layer, witness['r'])
        record['exact_rational_finite_data_shadow'] = shadow
        record['P_rr_evaluation_minus_shadow'] = [float(a-b) for a,b in zip(record['P'],shadow['P_rr'])]
        witness_data['layers'][label] = record
    for name in ('P','Q_cusp','compatibility'):
        vector = np.asarray(witness_data['layers']['fine'][name],np.longdouble)-np.asarray(witness_data['layers']['coarse'][name],np.longdouble)
        witness_data[name+'_fine_minus_coarse'] = dict(vector=[float(x) for x in vector],norm=float(np.linalg.norm(vector)))
    shadow_vector = np.asarray(witness_data['layers']['fine']['exact_rational_finite_data_shadow']['P_rr'])-np.asarray(witness_data['layers']['coarse']['exact_rational_finite_data_shadow']['P_rr'])
    witness_data['finite_data_rational_shadow_rr_difference_norm'] = float(np.linalg.norm(shadow_vector))
    coefficient_path = out/'GW-node-and-polynomial-coefficients.npz'
    np.savez_compressed(coefficient_path, **archived_arrays)
    report = dict(schema='GW-cusp-compatibility-diagnostic-v1',finished=True,
        source_and_input_sha256=hashes,profile_fingerprint=manifest['original_profile_fingerprint'],
        runtime=dict(python=platform.python_version(),numpy=np.__version__,
                     longdouble_mantissa_bits=int(np.finfo(np.longdouble).nmant)),
        reconstructed_GW_node_jets=True,saved_GW_Cartesian_second_jet_arrays_exist=False,
        no_ODE_or_shooting_solve=True,default_rr_used=False,global_field_adopted=False,
        original_stage=28,common_stage=450,radial_points=len(points),angles=args.angles,
        local_domain='Original retained common-stage-450 background samples; no continuous angular or radial metric bound.',
        decomposition='P=Q_cusp+E*(10u^3-15u^4+6u^5-1), so P_rr=Q_cusp_rr+E*S_second(u)/h^2.',
        coefficient_archive=dict(path=coefficient_path.name,sha256=sha(coefficient_path),bytes=coefficient_path.stat().st_size),
        layers={label:layer['report'] for label,layer in layers.items()},
        fine_minus_coarse=comparison,original_worst_rr_point=witness_data,
        seconds=time.monotonic()-start,task_completed=False,
        limitations=['Local finite diagnostics; the sampled angle bound for E does not cover unsampled angles.',
            'E contains genuine interpolation truncation, point reconstruction and endpoint errors as well as possible rounding; it is not named roundoff.',
            'The rational shadow freezes the already reconstructed binary64 Fourier nodal coefficients; it is not a higher-precision ODE or GW-node computation.',
            'Cusp-anchored integrated velocity is a local comparison field only; global cumulative position, seam, collar and closed geometry are not adopted or certified.',
            'The full-domain position/angular maxima at common stage 451 are outside this three-node packet.',
            'Original point data came from the historical completed local GW consumer inputs; this job supplies a new public Actions consumption identity.'])
    write_json(out/'report.json', report)
    print(json.dumps(dict(event='GW_cusp_compatibility_complete',out=str(out),
        original_rr_difference=witness_data['original_saved_global_rr_difference'],
        actual_local_rr_difference=comparison['P']['radial_second']['value'],
        Q_cusp_rr_difference=comparison['Q_cusp']['radial_second']['value'],
        compatibility_rr_difference=comparison['compatibility']['radial_second']['value'],
        seconds=report['seconds'],task_completed=False)),flush=True)


if __name__ == '__main__':
    main()
