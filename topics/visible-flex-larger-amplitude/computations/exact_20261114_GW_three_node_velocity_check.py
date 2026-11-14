#!/usr/bin/env python3
"""Use the completed GW coefficient archive to test its retained middle node.

All numerical work is restricted to this public repository's Actions.  The
three actual point velocities and the three reconstructed GW accelerations
remain distinct data.  A polynomial velocity derivative is never identified
with the true derivative of the original continuous point-development map.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time

EXPECTED_REPORT = 'd993156b4c876ecb18287464e9f465e78d7e4e65a23f0daae6bdaf8a11b00cab'
EXPECTED_COEFFICIENTS = '9f7cbb35544521ab352f4ce06cd03966a96c41f4bc63a42bffee42c16ea98cf0'
EXPECTED_PACKET = 'ef3bd5d5fb05143c109de8875c21424068db5814d9158187950b2f5d132ea75e'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(65536), b''):
            h.update(block)
    return h.hexdigest()


def write(path, data):
    with Path(path).open('x') as stream:
        json.dump(data, stream, indent=2, allow_nan=False)
        stream.write('\n')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-directory', type=Path, required=True)
    p.add_argument('--packet', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True, help='New output directory')
    p.add_argument('--angles', type=int, default=1024)
    args = p.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public'):
        raise RuntimeError('Numerical work belongs to this public repository Actions')
    if args.angles < 1024 or args.angles % 2:
        raise ValueError('Resolve the complete original cardinal Fourier field')
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[key] = '1'
    import numpy as np

    start = time.monotonic()
    source, packet, out = args.input_directory.resolve(), args.packet.resolve(), args.out.resolve()
    report_path = source/'report.json'
    coefficients_path = source/'GW-node-and-polynomial-coefficients.npz'
    manifest_path = packet/'manifest.json'
    required = {report_path:EXPECTED_REPORT, coefficients_path:EXPECTED_COEFFICIENTS,
                manifest_path:EXPECTED_PACKET}
    for path, expected in required.items():
        if sha(path) != expected:
            raise ValueError('The completed actual input differs: '+str(path))
    original = json.loads(report_path.read_text())
    manifest = json.loads(manifest_path.read_text())
    if (original.get('finished') is not True or not original.get('reconstructed_GW_node_jets') or
            original.get('default_rr_used') is not False):
        raise ValueError('Expected the actual completed GW local reconstruction')
    if original['coefficient_archive']['sha256'] != EXPECTED_COEFFICIENTS:
        raise ValueError('The original report does not bind this coefficient archive')
    hashes = {str(path):value for path,value in required.items()}
    hashes[str(Path(__file__).resolve())] = sha(__file__)
    metadata = {}
    for label in ('coarse','fine'):
        descriptors = []
        for record in manifest['layers'][label]['rows']:
            path = packet/record['row_file']
            expected = manifest['row_files'][record['row_file']]['sha256']
            if sha(path) != expected:
                raise ValueError('Original node metadata changed')
            row = json.loads(path.read_text())
            hashes[str(path)] = expected
            descriptors.append(dict(r=row['geometry']['r'], original_layer=label,
                original_rows_index=record['original_rows_index'],
                original_source_parameter=row['x'], original_file=row['file'],
                packet_file=record['node_file'], original_file_sha256=row['sha256'],
                original_row_sha256=expected))
        metadata[label] = sorted(descriptors, key=lambda row:row['r'])
    background_path = packet/manifest['background_row_file']
    if sha(background_path) != manifest['row_files'][manifest['background_row_file']]['sha256']:
        raise ValueError('The saved background row changed')
    hashes[str(background_path)] = sha(background_path)
    background = json.loads(background_path.read_text())

    def node(archive, label, endpoint):
        values = []
        for name in ('position','radial_first','radial_second'):
            key = label+'_node'+str(endpoint)+'_'+name+'_coefficients'
            value = archive[key]
            if value.shape != (257,3) or not np.all(np.isfinite(value)):
                raise ValueError('Incomplete original 512-angle coefficient data')
            values.append(value.astype(np.clongdouble))
        return values

    with np.load(coefficients_path, allow_pickle=False) as archive:
        radii = {label:archive[label+'_r'].copy() for label in ('coarse','fine')}
        for label in radii:
            if radii[label].shape != (2,) or not np.array_equal(
                    radii[label],np.asarray([q['r'] for q in metadata[label]],np.longdouble)):
                raise ValueError('Ascending numerical radii disagree with their original row metadata')
        A, B = node(archive,'coarse',0), node(archive,'fine',0)
        C, C_other = node(archive,'coarse',1), node(archive,'fine',1)
        if any(not np.array_equal(a,b) for a,b in zip(C,C_other)):
            raise ValueError('The claimed shared cusp does not have identical actual coefficients')
    ra, rb, rc = radii['coarse'][0], radii['fine'][0], radii['coarse'][1]
    if not ra < rb < rc or radii['fine'][1] != rc:
        raise ValueError('The actual three-node nesting differs')
    if metadata['coarse'][1]['original_file_sha256'] != metadata['fine'][1]['original_file_sha256']:
        raise ValueError('The shared right cusp must have the same original point bytes')
    target = next((row for row in background['points'] if row['r']==float(rb)),None)
    if target is None:
        raise ValueError('No actual saved background at the retained middle node')
    theta = 2*np.pi*np.arange(args.angles)/args.angles
    k = np.arange(args.angles//2+1)[:,None]

    def angular(c, order=0):
        spectrum = np.zeros((args.angles//2+1,3),complex)
        spectrum[:len(c)] = np.asarray(c,complex)
        spectrum[1:len(c)] /= 2
        return np.asarray(np.fft.irfft(spectrum*(1j*k)**order,n=args.angles,axis=0)*args.angles,np.longdouble)

    def describe(c):
        result = dict(coefficient_max_abs=float(np.max(abs(c))),angular={})
        for order in (0,1,2):
            values = angular(c,order)
            norms = np.linalg.norm(values,axis=1)
            at = int(np.argmax(norms))
            result['angular'][str(order)] = dict(maximum=float(norms[at]),theta=float(theta[at]),
                vector=[float(v) for v in values[at]],
                xy_norm_max=float(np.max(np.linalg.norm(values[:,:2],axis=1))),
                z_abs_max=float(np.max(abs(values[:,2]))))
        result['theta_zero'] = [float(v) for v in angular(c)[0]]
        return result

    def velocity(left,right,h):
        vl,al,vr,ar = left[1],left[2],right[1],right[2]
        return np.stack([vl,h*al,3*(vr-vl)-h*(2*al+ar),2*(vl-vr)+h*(al+ar)])

    def evaluate(c,u,h,derivative=0):
        result = np.zeros_like(c[0])
        for i in range(derivative,len(c)):
            factor = 1
            for j in range(derivative):factor *= i-j
            result += factor*c[i]*u**(i-derivative)/h**derivative
        return result

    def integral(left,right,h):
        return h*(left[1]+right[1])/2+h*h*(left[2]-right[2])/12

    hab,hbc,hac = rb-ra,rc-rb,rc-ra
    ub = hab/hac
    coarse = velocity(A,C,hac)
    predicted_vb = evaluate(coarse,ub,hac)
    predicted_ab = evaluate(coarse,ub,hac,1)
    # Independent of all GW acceleration inputs; still only a finite polynomial
    # derivative estimate from three actual velocities, not a true derivative.
    secant_ab = (B[1]-A[1])/hab
    secant_bc = (C[1]-B[1])/hbc
    divided_second = (secant_bc-secant_ab)/hac
    velocity_only_ab = secant_ab+hab*divided_second
    Iac,Iab,Ibc = integral(A,C,hac),integral(A,B,hab),integral(B,C,hbc)
    Eac,Eab,Ebc = C[0]-A[0]-Iac,B[0]-A[0]-Iab,C[0]-B[0]-Ibc
    nested_change = Iab+Ibc-Iac
    identity = nested_change-(Eac-Eab-Ebc)

    er = np.c_[np.cos(theta),np.sin(theta),np.zeros(args.angles)]
    et = np.c_[-np.sin(theta),np.cos(theta),np.zeros(args.angles)]
    ft = angular(B[0],1)+rb*et
    actual_fr = angular(B[1])+er
    actual_fr[:,2] += target['w']
    actual_ar = angular(B[2]);actual_ar[:,2] += target['wr']
    predicted_fr = angular(predicted_vb)+er;predicted_fr[:,2] += target['w']
    predicted_ar = angular(predicted_ab);predicted_ar[:,2] += target['wr']
    velocity_only_ar = angular(velocity_only_ab);velocity_only_ar[:,2] += target['wr']

    def metric(fr):
        aa = np.sum(fr*fr,axis=1)/np.longdouble(target['E'])-1
        bb = np.sum(fr*ft,axis=1)/(np.sqrt(np.longdouble(target['E']))*rb)
        dd = np.sum(ft*ft,axis=1)/rb**2-1
        operator = (abs(aa+dd)+np.sqrt((aa-dd)**2+4*bb*bb))/2
        at = int(np.argmax(operator))
        return dict(maximum=float(operator[at]),theta=float(theta[at]),
                    definition='Same actual middle-node F_theta; only the proposed F_r changes at this point. This is not a new global field.')

    def acceleration_constraints(ar):
        gamma = np.longdouble(target['w'])*np.longdouble(target['wr'])/np.longdouble(target['E'])
        radial = 2*np.sum(actual_fr*ar,axis=1)-2*np.longdouble(target['w'])*np.longdouble(target['wr'])
        transverse = np.sum((ar-gamma*actual_fr)*ft,axis=1)
        return dict(radial_metric_derivative_max_abs=float(np.max(abs(radial))),
                    Gamma_removed_Ftheta_component_max_abs=float(np.max(abs(transverse))),
                    definition='Algebraic target-metric conditions tested against the actual middle-node F_r and F_theta; not a measured continuous derivative.')

    residuals = dict(
        coarse_velocity_at_B_minus_actual_saved_velocity=predicted_vb-B[1],
        coarse_velocity_derivative_at_B_minus_GW_acceleration=predicted_ab-B[2],
        velocity_only_quadratic_derivative_at_B_minus_GW_acceleration=velocity_only_ab-B[2],
        secant_AB_minus_GW_acceleration_at_B=secant_ab-B[2],
        secant_BC_minus_GW_acceleration_at_B=secant_bc-B[2],
        E_AC=Eac,E_AB=Eab,E_BC=Ebc,
        nested_velocity_integral_minus_coarse_velocity_integral=nested_change,
        nested_integral_E_identity_residual=identity)
    out.mkdir(parents=True,exist_ok=False)
    coefficient_output = out/'three-node-residual-coefficients.npz'
    np.savez_compressed(coefficient_output,**residuals,
        coarse_velocity_coefficients=coarse,
        actual_middle_velocity=B[1],actual_middle_GW_acceleration=B[2],
        coarse_predicted_middle_velocity=predicted_vb,
        coarse_predicted_middle_acceleration=predicted_ab,
        velocity_only_quadratic_middle_acceleration=velocity_only_ab)
    result = dict(schema='actual-GW-three-node-velocity-consistency-v1',finished=True,
        sources_and_inputs_sha256=hashes,
        original_actions=dict(run=43586618658,job=132422438078,artifact=14110608098),
        profile_fingerprint=original['profile_fingerprint'],angles=args.angles,
        runtime=dict(python=platform.python_version(),numpy=np.__version__,
                     longdouble_mantissa_bits=int(np.finfo(np.longdouble).nmant)),
        numerical_endpoint_mapping=dict(A=metadata['coarse'][0],B=metadata['fine'][0],
            C=dict(r=float(rc),coarse_origin=metadata['coarse'][1],fine_origin=metadata['fine'][1],
                   all_stored_d_v_a_coefficients_identical=True)),
        radii=[float(ra),float(rb),float(rc)],
        widths=dict(AB=float(hab),BC=float(hbc),AC=float(hac)),
        middle_node_normalized_coordinate_in_AC=float(ub),
        actual_middle_background=target,
        residuals={name:describe(value) for name,value in residuals.items()},
        actual_middle_fields=dict(saved_velocity=describe(B[1]),GW_acceleration=describe(B[2]),
            coarse_velocity_derivative=describe(predicted_ab),
            velocity_only_quadratic_derivative=describe(velocity_only_ab)),
        middle_metric=dict(actual_saved_velocity=metric(actual_fr),coarse_velocity_prediction=metric(predicted_fr)),
        middle_acceleration_metric_conditions=dict(GW_closure=acceleration_constraints(actual_ar),
            coarse_velocity_derivative=acceleration_constraints(predicted_ar),
            velocity_only_quadratic_derivative=acceleration_constraints(velocity_only_ar)),
        coefficient_archive=dict(path=coefficient_output.name,bytes=coefficient_output.stat().st_size,
                                 sha256=sha(coefficient_output)),
        integral_identity='I_AB+I_BC-I_AC = E_AC-E_AB-E_BC; the middle position d_B cancels exactly.',
        source_velocity_continuous_radial_derivative_computed=False,
        no_new_ODE_or_shooting=True,new_field_adopted=False,target_metric_changed=False,
        seconds=time.monotonic()-start,task_completed=False,
        limitations=['Finite full-cardinal-field angle samples, not continuous angular bounds.',
            'Actual saved point velocity, algebraic GW acceleration, and derivatives of comparison polynomials are distinct quantities.',
            'A discrepancy at B detects underresolution or data inconsistency but alone does not prove the GW acceleration differs from the true continuous source velocity derivative.',
            'No higher-precision original node reconstruction or new radial source solve was performed.',
            'The integral identity separates a velocity quadrature change from the middle position datum; it does not classify every upstream error.',
            'No metric, seam, collar, reach or amplitude conclusion is inherited by a replacement field.'])
    write(out/'report.json',result)
    print(json.dumps(dict(event='GW_three_node_velocity_check_complete',out=str(out),
        velocity_error=result['residuals']['coarse_velocity_at_B_minus_actual_saved_velocity']['angular']['0']['maximum'],
        acceleration_error=result['residuals']['coarse_velocity_derivative_at_B_minus_GW_acceleration']['angular']['0']['maximum'],
        seconds=result['seconds'],task_completed=False)),flush=True)


if __name__ == '__main__':
    main()
