#!/usr/bin/env python3
"""Small independent exact-tail check of actual curvature and one rigid cut fit.

This is a constructed R128 tail fixture, not a BVP field or a surface certificate.
It checks the new postprocessor's geometry formulas, including an actual nonzero
tilt and horizontal translation which must be retained by the registration.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_raw_native_field import pack_body_state
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily
from fd2d_flat_developable_tail import FlatDevelopableTail

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('actual_raw_body_screen',HERE/'fd2d-metric-raw-body-screen.py')
body=importlib.util.module_from_spec(spec);spec.loader.exec_module(body)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out-prefix',type=Path,required=True)
    args=p.parse_args()
    report_path=Path(str(args.out_prefix)+'-report.json')
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'*')):
        raise FileExistsError('Use a new output stem')
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    a=.8;u=2*np.pi*(np.arange(64)+.137)/64
    tail=PositiveFlatDevelopableFamily(np.full(8,.9))
    g=tail.cut_port(u)
    independent=FlatDevelopableTail(amplitude=.9).cut_port(u)
    c,s=np.cos,.sin
    ax,ay,az=-.17,.37,.23
    Qx=np.array([[1.,0,0],[0,c(ax),-s(ax)],[0,s(ax),c(ax)]])
    Qy=np.array([[c(ay),0,s(ay)],[0,1.,0],[-s(ay),0,c(ay)]])
    Qz=np.array([[c(az),-s(az),0],[s(az),c(az),0],[0,0,1.]])
    Q=Qz@Qy@Qx;t=np.array([.13,-.2,.7])
    F=np.stack((g['e1'],g['e2'],g['N']),axis=-1)
    r=np.column_stack((a*g['n'],-a*g['m'],-np.ones(len(u))))
    b=np.zeros_like(r);b[:,1]=a
    v=np.column_stack((a*g['n_u'],-a*g['m_u'],np.zeros(len(u))))
    state=pack_body_state(g['X']@Q.T+t,Q@F,r,b,v,np.zeros_like(r))
    physical=dict(a=np.full(len(u),a),J=np.ones(len(u)),s=np.zeros(len(u)),
        n=g['n'],m=g['m'],l=g['l'],angle_inverse_error=np.zeros(len(u)))
    reader=SimpleNamespace(physical=lambda x,angles,**kwargs:physical,tail=tail,
        nodes=np.array([0.,1.]),values=np.zeros((2,1)))
    actual=body.field_summary(reader,0.,u,state)
    cut=body.cut_comparison(reader,actual,u,args.out_prefix)
    expected_curvature=np.column_stack((np.zeros(len(u)),g['kappa']))
    errors=dict(metric=float(np.max(actual['metric_relative_error'])),
        actual_curvature=float(np.max(np.abs(actual['principal_curvatures']-expected_curvature))),
        rotation=float(np.max(np.abs(np.asarray(cut['registration']['Q'])-Q))),
        translation=float(np.max(np.abs(np.asarray(cut['registration']['translation'])-t))),
        rigid_twojets=max(q['absolute_vector_max'] for q in cut['jets'].values()),
        rigid_normal=cut['inward_normal_vector_error_max'],
        independent_R128_twojets=max(float(np.max(np.abs(g[k]-independent[k]))) for k in body.JET_KEYS))
    checks=dict(actual_curvature=errors['actual_curvature']<2e-12,metric=errors['metric']<2e-13,
        proper_rigid_fit=errors['rotation']<2e-12 and errors['translation']<2e-12,
        all_cartesian_jets=errors['rigid_twojets']<2e-11,
        oriented_normal=errors['rigid_normal']<2e-12,
        independent_R128=errors['independent_R128_twojets']<2e-11,
        nonzero_tilt_retained=cut['registration']['unoriented_vertical_axis_tilt_radians']>.1,
        nonzero_horizontal_translation_retained=cut['registration']['horizontal_translation_norm']>.1)
    report=dict(schema='fd2d-raw-body-exact-tail-geometry-check-v1',scope=__doc__,
        sources=[identity(__file__),identity(HERE/'fd2d-metric-raw-body-screen.py'),
            identity(HERE/'fd2d_gc_raw_native_field.py'),
            identity(HERE/'fd2d_positive_flat_developable_family.py'),
            identity(HERE/'fd2d_flat_developable_tail.py')],
        fixture=dict(tail_kind='positive_bernstein',controls=[.9]*8,cut_radius=a,
            angles=64,angle_formula='2*pi*(j+.137)/64',proper_rotation=Q.tolist(),
            translation=t.tolist(),body_state='Exact tail frame and angle variations, then one declared rigid motion'),
        errors=errors,checks=checks,implementation_checks_passed=all(checks.values()),cut=cut,
        no_BVP_or_continuous_surface_claim=True)
    body.atomic_json(report_path,report)
    print(json.dumps(dict(report=str(report_path),errors=errors,checks=checks)),flush=True)
    return 0 if all(checks.values()) else 1


if __name__=='__main__':raise SystemExit(main())

