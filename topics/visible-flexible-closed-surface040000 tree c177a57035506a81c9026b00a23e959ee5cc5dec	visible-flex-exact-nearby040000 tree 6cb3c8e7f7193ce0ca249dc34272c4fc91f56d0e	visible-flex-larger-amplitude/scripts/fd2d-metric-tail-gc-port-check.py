#!/usr/bin/env python3
"""Finite checks of R117's actual height-to-GC port and algebraic JVP.

An existing solved OLD-metric nonlinear tail packet checks the real Fourier
and full-mean conventions. It is not a new strong-target solve. An artificial
packed jet Jacobian checks row layout only, not the old DN derivative.
"""
from __future__ import annotations
import argparse
import copy
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from fd2d_metric_tail_gc_port import TailGCJetPort, height_to_gc, height_to_gc_jvp, LD

HERE = Path(__file__).resolve().parent


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def maxabs(x):
    return float(np.max(abs(np.asarray(x)), initial=LD(0)))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--old-tail', type=Path, default=HERE.parent/'notes'/'2026-11-10-78718-numerical-m15-w22-fast-07_tail_0009.json.gz')
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a new port-check report')
    pi = np.arccos(LD(-1))
    u = np.arange(513, dtype=LD)*2*pi/513
    co, si = np.cos(u), np.sin(u)
    # A genuinely nonzero-m exact local isometric immersion: the associate
    # family of the catenoid and helicoid, with r^2=s^2+c^2 and s<0.
    r, c, alpha = LD('.8'), LD('.3'), LD('.37')
    s = -np.sqrt(r*r-c*c)
    v, app = s/r, c*c/r**3
    ca, sa = np.cos(alpha), np.sin(alpha)
    z0 = ca*c*np.arcsinh(s/c)+sa*c*u
    height = dict(z=z0, zr=np.full_like(u, ca*c/s), zu=np.full_like(u, sa*c),
                  zrr=np.full_like(u, -ca*c*r/s**3), zru=np.zeros_like(u), zuu=np.zeros_like(u))
    values = height_to_gc(height, radius=r, radial_speed=v, radial_acceleration=app)
    expected = dict(l=-c*ca/r**2, m=-c*sa/r**2, n=c*ca/r**2, N_z=v)
    associate = {key+'_error':maxabs(values[key]-expected[key]) for key in expected}
    associate['gauss_defect'] = maxabs(values['gauss_defect'])
    reflected = height_to_gc({key:-value for key,value in height.items()},
                            radius=r, radial_speed=v, radial_acceleration=app)
    associate['unsigned_half_reflection_II_sign_error'] = max(maxabs(reflected[k]+values[k]) for k in ('l','m','n'))
    associate['unsigned_half_reflection_Nz_error'] = maxabs(reflected['N_z']-values['N_z'])
    lower_global = dict(l=-reflected['l'], m=reflected['m'], n=-reflected['n'])
    associate['signed_global_mirror_parity_error'] = max(maxabs(lower_global[k]-(values[k] if k!='m' else -values[k])) for k in lower_global)
    # An ambiently tilted sphere independently checks the angle derivatives
    # and the invariance under a proper rotation in the vertical graph chart.
    radius, sphere_radius, beta = LD('.7'), LD(2), LD('.31')
    z = np.sqrt(sphere_radius**2-radius**2)
    speed, acceleration = -z/sphere_radius, -radius/sphere_radius**2
    cb, sb = np.cos(beta), np.sin(beta)
    tilted = dict(z=-sb*radius*co+cb*z, zr=-sb*co-cb*radius/z,
                  zu=sb*radius*si, zrr=np.full_like(u,-cb*sphere_radius**2/z**3),
                  zru=sb*si, zuu=sb*radius*co)
    sphere = height_to_gc(tilted, radius=radius, radial_speed=speed, radial_acceleration=acceleration)
    translated_height = dict(tilted); translated_height['z'] = tilted['z']+LD(17)
    translated = height_to_gc(translated_height, radius=radius, radial_speed=speed, radial_acceleration=acceleration)
    sphere_check = dict(l_error=maxabs(sphere['l']-1/sphere_radius), n_error=maxabs(sphere['n']-1/sphere_radius),
        m_error=maxabs(sphere['m']), gauss_defect=maxabs(sphere['gauss_defect']),
        translation_invariance_error=max(maxabs(translated[k]-sphere[k]) for k in ('l','m','n')))
    with gzip.open(args.old_tail, 'rt') as stream:
        record = json.load(stream)
    port = TailGCJetPort.from_worker_record(record)
    actual = port.evaluate(u)
    old_check = dict(source=identity(args.old_tail), converged=record['response'].get('converged'),
        worker_residual=record['response'].get('residual'), modes=port.M, spacing=port.spacing,
        target_jet=[float(x) for x in port.target_jet], background_jet_difference=[float(x) for x in port.background_jet_difference],
        minimum_normal_projection_squared=float(np.min(actual['normal_projection_squared'])),
        maximum_gauss_defect=maxabs(actual['gauss_defect']),
        l_range=[float(np.min(actual['l'])),float(np.max(actual['l']))],
        m_range=[float(np.min(actual['m'])),float(np.max(actual['m']))],
        n_range=[float(np.min(actual['n'])),float(np.max(actual['n']))],
        old_metric_packet_only=True, strong_target_tail_solved_here=False,
        complete_means_used=True, extra_sqrt2_applied=False)
    # This explicit artificial tangent exercises all (3M+2) row blocks.
    # It deliberately does not assert that the old packet had a DN Jacobian.
    M, k = port.M, port.frequencies
    J = np.zeros((3*M+2,M), dtype=LD)
    J[:M] = np.diag(2+k)
    J[M:2*M] = np.diag(3+k*k)
    J[2*M] = LD('.001')/(1+k)
    J[2*M+1] = LD('.002')/(1+k)
    J[2*M+2:] = np.eye(M)
    direction = LD('.0003')*(-1)**np.arange(M)/(1+k)
    layout = TailGCJetPort(port.jets, spacing=port.spacing, height_jacobian=J)
    delta = layout.unpack_height_jvp(direction)
    tangent = layout.jvp(u,direction)
    difference_rows = []
    for step in (LD('.001'),LD('.0003')):
        moved = []
        for sign in (-1,1):
            jets = copy.deepcopy(port.jets)
            for key in ('height','slope','second'):
                jets[key] = np.asarray(jets[key],dtype=LD)+sign*step*delta[key]
            jets['meanSlope'] = LD(jets['meanSlope'])+sign*step*delta['meanSlopeCorrection']
            jets['meanSecond'] = LD(jets['meanSecond'])+sign*step*delta['meanSecondCorrection']
            moved.append(TailGCJetPort(jets,spacing=port.spacing).evaluate(u))
        difference_rows.append(dict(step=float(step), **{key+'_jvp_difference':maxabs((moved[1][key]-moved[0][key])/(2*step)-tangent[key])
                                                         for key in ('l','m','n','N_z')}))
    report = dict(schema='fd2d-tail-height-gc-port-check-v1', scope=__doc__,
        script=identity(__file__), provider=identity(HERE/'fd2d_metric_tail_gc_port.py'),
        worker_jet_source=identity(HERE/'fd2d-bounded-tail-stage-core.mjs'),
        worker_height_fourier_source=identity(HERE.parent/'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_relative_spatial_jets.mjs'),
        angle_count=len(u), exact_nonzero_m_associate_patch_check=associate,
        tilted_sphere_check=sphere_check, actual_old_tail_check=old_check,
        packed_layout_check=dict(matrix_kind='explicit artificial test tangent, NOT a DN solve',
             shape=list(J.shape), rows=['slope[M]','second[M]','meanSlopeCorrection','meanSecondCorrection','height[M]'],
             height_identity_block_error=maxabs(delta['height']-direction), finite_difference_checks=difference_rows),
        new_nonlinear_tail_computed=False, continuous_certificate=False, closed_surface=False)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out), associate=associate, sphere=sphere_check, old_tail=old_check,
                         parameter_checks=difference_rows)),flush=True)


if __name__=='__main__':
    main()
