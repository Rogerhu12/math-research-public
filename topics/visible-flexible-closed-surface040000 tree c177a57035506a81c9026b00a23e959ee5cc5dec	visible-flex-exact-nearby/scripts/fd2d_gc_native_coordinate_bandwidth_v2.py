#!/usr/bin/env python3
"""Compare one actual field in its original xi chart and fixed material u.

The same saved shared-C1 field is evaluated. No BVP, ODE, coordinate refit,
or physical-metric design is performed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,sys,json,time
from pathlib import Path
import numpy as np


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field',type=Path,required=True)
    parser.add_argument('--source-dir',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--points',type=int,default=2048)
    parser.add_argument('--locations',type=float,nargs='+',default=[.78,.84,.92])
    args=parser.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError(args.out)
    sys.path.insert(0,str(args.source_dir.resolve()))
    import fd2d_gc_native_log_field as native
    from fd2d_gc_native_log_physical import PhysicalNativeLogField
    from fd2d_gc_native_spectral_residual_screen import Reader
    native.np=Reader();model=PhysicalNativeLogField(args.field)
    angle=2*np.pi*np.arange(args.points)/args.points
    retained=[16,32,64,94,190]

    def spectrum(values):
        values=np.asarray(values,dtype=float).reshape(-1)
        coefficients=np.fft.rfft(values)/args.points
        weights=np.full(len(coefficients),2.);weights[0]=weights[-1]=1.
        bands=[]
        for limit in retained:
            low=coefficients.copy();low[limit+1:]=0
            represented=np.fft.irfft(low,n=args.points)*args.points
            tail=coefficients[limit+1:]
            bands.append(dict(retained_maximum_frequency=limit,
                sampled_reconstruction_maximum=float(abs(values-represented).max()),
                sampled_coefficient_tail_l1=float(np.sum(weights[limit+1:]*abs(tail))),
                sampled_tail_coefficient_maximum=float(abs(tail).max(initial=0))))
        return dict(maximum=float(abs(values).max()),
            weighted_coefficient_l1=float(np.sum(weights*abs(coefficients))),
            odd_coefficient_l1=float(np.sum(weights[1::2]*abs(coefficients[1::2]))),bands=bands)

    rows=[]
    for x in args.locations:
        row=dict(x=x,nearest_native_node=int(np.argmin(abs(model.native.nodes-x))),charts={})
        for kind in ['original_xi','material_u','seed_phi']:
            if kind=='original_xi':f=model.evaluate(x,angle)
            elif kind=='material_u':f=model.evaluate_material(x,angle)
            else:f=model.evaluate_material(x,model.geometry.material_coordinate(angle)['u'])
            v=lambda name:np.asarray(f[name]).reshape(-1)
            eta,zeta,eta_xi,zeta_xi=(v(k) for k in ('eta','zeta','eta_xi','zeta_xi'))
            a,ap,app,J=(v(k)[0] for k in ('a','ap','app','J'))
            q,Ux=v('q'),v('Ux');c=ap/a;chi=-a*app/(1-ap*ap);inverse=np.exp(-eta)
            eta_s=inverse*zeta_xi/(a*q)+c*(zeta*zeta*inverse*inverse+chi*np.expm1(-2*eta))
            zeta_s=inverse*(2*zeta*zeta_xi-(zeta*zeta+chi)*eta_xi)/(a*q)-c*(1+chi)*zeta
            drift=Ux/q
            rhs_eta=J*eta_s;rhs_zeta=J*zeta_s
            actual_eta_x=v('eta_x');actual_zeta_x=v('zeta_x')
            if kind=='original_xi':
                rhs_eta=rhs_eta+drift*eta_xi;rhs_zeta=rhs_zeta+drift*zeta_xi
            else:
                actual_eta_x=actual_eta_x-drift*eta_xi;actual_zeta_x=actual_zeta_x-drift*zeta_xi
            fields=dict(eta=eta,zeta=zeta,eta_rhs_at_fixed_coordinate=rhs_eta,zeta_rhs_at_fixed_coordinate=rhs_zeta,
                eta_velocity_residual=actual_eta_x-rhs_eta,zeta_velocity_residual=actual_zeta_x-rhs_zeta)
            row['charts'][kind]=dict(beta=float(model.blend(x)[0][0]),
                material_inverse_maximum=float(abs(f['material_angle_residual']).max()) if kind!='original_xi' else None,
                evaluation_chart_beta=0. if kind=='seed_phi' else (1. if kind=='material_u' else float(model.blend(x)[0][0])),
                evaluation_chart_beta_x=0. if kind!='original_xi' else float(model.blend(x)[1][0]),
                q_minimum=float(q.min()),q_maximum=float(q.max()),
                fields={name:spectrum(value) for name,value in fields.items()})
        rows.append(row)
    report=dict(schema='fd2d-actual-native-three-coordinate-bandwidth-v2',source=native.identity(__file__),
        actual_field=native.identity(args.field),defining_arrays=model.meta['actual_arrays'],
        physical_evaluator=native.identity(Path(sys.modules['fd2d_gc_native_log_physical'].__file__)),
        native_evaluator=native.identity(Path(native.__file__)),
        gzip_reader=native.identity(Path(sys.modules['fd2d_gc_native_spectral_residual_screen'].__file__)),
        angular_points=args.points,maximum_native_frequency=2*model.native.K,retained_frequencies=retained,
        same_actual_field=True,new_solve=False,physical_metric_changed=False,continuous_certificate=False,
        coordinate_rhs_note='Original mixed xi RHS includes its U_x/U_xi transport. Material u and pure fixed seed phi both have beta_x=0, so RHS is J times the physical fixed-u shape RHS, sampled respectively at u or U_seed(phi). Their actual x derivative is transported from the same original mixed field by the matching chain rule.',
        interpretation_note='Native eta,zeta are finite degree94 in xi by definition, so xi tails above94 are rounding. Material tails measure re-expression of that same field. RHS and residual spectra are also reported to distinguish this representation fact from genuine resolved-velocity content.',
        rows=rows,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    small=[]
    for row in rows:
        entry=dict(x=row['x'],charts={})
        for chart,data in row['charts'].items():
            entry['charts'][chart]={name:{'max':field['maximum'],'tails':{str(b['retained_maximum_frequency']):b['sampled_coefficient_tail_l1'] for b in field['bands'] if b['retained_maximum_frequency'] in [94,190]}} for name,field in data['fields'].items()}
        small.append(entry)
    print(json.dumps(dict(out=str(args.out),seconds=report['seconds'],rows=small)))


if __name__=='__main__':main()
