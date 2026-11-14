#!/usr/bin/env python3
"""Resolve wave-number, fixed-angle, and parity questions for R139 tables."""
from pathlib import Path
import argparse,hashlib,json,time
import numpy as np


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser();root=Path(__file__).resolve().parent.parent
    ap.add_argument('--field',type=Path,default=root/'notes/2026-12-12-placeholder.npz')
    ap.add_argument('--native-report',type=Path,default=root/'notes/2026-11-12-fd2d-k0-native-gc-01-report.json')
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.field.name=='2026-12-12-placeholder.npz':args.field=root/'notes/2026-11-12-fd2d-k0-native-gc-01-field.npz'
    if args.out.exists():raise FileExistsError(args.out)
    start=time.monotonic();p=np.load(args.field,allow_pickle=False);native=json.loads(args.native_report.read_text())
    if digest(args.field)!=native['arrays_sha256']:raise ValueError('Native table identity mismatch')
    y=p['lmn'];N=y.shape[1];j=np.arange(N);phi=p['phi'];u=p['material_u']
    parity=[]
    for label,indices,sign in (('pi periodic',(j+N//2)%N,[1,1,1]),
        ('minus phi',(-j)%N,[1,-1,1]),('pi minus phi',(N//2-j)%N,[1,-1,1])):
        error=abs(y-y[:,indices]*np.asarray(sign))
        parity.append(dict(operation=label,component_maxima=np.max(error,axis=(0,1)).tolist(),
            endpoint_component_maxima=np.max(error[-1],axis=0).tolist()))
    raw=np.fft.rfft(y,axis=1,norm='forward');table=[]
    for wave in (15,31,63,95,191):
        z=raw.copy();z[:,wave+1:]=0;restored=np.fft.irfft(z,n=N,axis=1,norm='forward')
        errors=np.max(abs(y-restored),axis=(0,1))
        table.append(dict(maximum_integer_Fourier_wave_in_phi=wave,
            largest_retained_even_wave=2*(wave//2),maximum_k_in_cos_2k_phi=wave//2,
            l_n_keep_mean=True,m_has_no_mean=True,component_value_errors=errors.tolist(),maximum_value_error=float(errors.max())))
    report=dict(schema='fd2d-R139-fixed-angle-wave-convention-audit-v1',actual_execution=True,
        source_sha256=digest(__file__),field_sha256=digest(args.field),native_report_sha256=digest(args.native_report),
        angular_coordinate='Uniform fixed exact balanced-seed normal phi. Material u=U_seed(phi) is common but nonuniform on this grid.',
        phi_uniform_grid_max_error=float(np.max(abs(phi-2*np.pi*np.arange(N)/N))),
        material_u_step_range=[float(np.diff(u).min()),float(np.diff(u).max())],
        actual_longdouble_mantissa_bits=int(np.finfo(np.longdouble).nmant),stored_table_dtype=str(y.dtype),
        parity=parity,projection_table=table,
        original_evaluation_max_material_inverse_residual=max(r['material_inverse_residual'] for r in native['rows']),
        original_evaluation_material_provider_inverse_error=native['material_provider_input_inverse_error'],
        field_periodic_parity_consistent=max(max(r['component_maxima']) for r in parity)<1e-12,
        no_branch_or_period_error_inferred_from_these_checks=True,
        scope='Finite representation audit. Unique exact inverse additionally follows from the separately certified D>0; no finite Fourier BVP success is asserted.',
        seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out),sha256=digest(args.out),parity_max=max(max(r['component_maxima']) for r in parity),seconds=report['seconds'])))


if __name__=='__main__':main()
