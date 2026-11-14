#!/usr/bin/env python3
"""Actual R153 exit-rim cell with the R152 affine-only quadrature change.

This targeted check keeps the full actual nonlinear field fixed, shows the
changed finite Codazzi averages, and checks a nonzero shared-parameter
Jacobian. It does not solve a BVP or replace nonlinear correction Gauss2
with an unreported fine rule.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import argparse,copy,datetime,json,resource,time,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_raw_bump_positive_gauss import PositiveGaussRawBumpDAE
from fd2d_gc_gauss_cell_positive_gauss import gauss_cell_positive_gauss
from fd2d_gc_positive_gauss_hybrid import gauss_cell_positive_gauss_hybrid


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','field','radius-packet','reference-inlet','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path);ap.add_argument('--cell',type=int,default=71)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh local report stem')
    start=time.monotonic();report=dict(schema='fd2d-actual-R153-R152-explicit-composition-local-check-v1',
        source=identity(__file__),consumer=identity(Path(__file__).with_name('fd2d_gc_positive_gauss_hybrid.py')),
        field=identity(args.field),candidate=identity(args.candidate),started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        completed=False,exception=None,nonlinear_BVP_performed=False,continuous_certificate=False)
    def save():
        report.update(seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        a=load_npz(args.field);proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:raise ValueError('Wrong radius packet')
        p=PositiveGaussRawBumpDAE(args.candidate,modes=int(a['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            base_lower_bound='4/5',base_lower_provenance=dict(**identity(args.radius_packet),candidate_sha256=proof['candidate_sha256']),radius_floor=.1)
        if not np.array_equal(a['mesh'],p.x) or json.loads(str(a['gauss_l_definition']))!=p.gauss_l_definition:
            raise ValueError('The saved actual nonlinear field differs')
        j=args.cell;view=copy.copy(p);view.x=p.x[j:j+2].copy();view.N=2;view.h=np.diff(view.x)
        view.size=2*p.q+p.parameter_count;view.residual_size=2*p.q+2*p.K+2
        view.coords={k:np.asarray(v,float) for k,v in view.chart.coordinates(view.x).items()}
        view._operator_cache={};view._cell_gauss_view_cache=None;view._hybrid_known_lifting_cache=None
        z=np.r_[a['corrections'][j:j+2].ravel(),a['parameters']];offset=2*p.q
        coarse=gauss_cell_positive_gauss(view,z,jacobian=True)
        fine=gauss_cell_positive_gauss_hybrid(view,z,jacobian=True,known_order=8)
        tighter=gauss_cell_positive_gauss_hybrid(view,z,jacobian=False,known_order=12)
        def maxima(row):
            return dict(full_by_component=np.max(abs(row['full_codazzi_cells']),axis=(0,1)).tolist(),
                high_by_component=np.max(abs(row['omitted_codazzi_cells']),axis=(0,1)).tolist(),
                low=float(np.max(abs(row['retained_residual']))),info=row['info'])
        report.update(cell=j,endpoints=view.x.tolist(),original_R153_G2=maxima(coarse),
            affine_only_G8=maxima(fine),affine_only_G12=maxima(tighter),
            G8_to_G12_full_difference=float(np.max(abs(fine['full_codazzi_cells']-tighter['full_codazzi_cells']))),
            G2_to_hybrid_full_change=float(np.max(abs(fine['full_codazzi_cells']-coarse['full_codazzi_cells']))),
            actual_point_Gauss_unchanged=bool(np.array_equal(fine['point_gauss'],coarse['point_gauss'])),
            field_changed=False,physical_g_changed=False,nonlinear_Delta_quadrature_still_G2=True)
        state_differences={}
        for key in ('retained_jacobian','high_jacobian'):
            delta=fine[key][:,:offset]-coarse[key][:,:offset]
            state_differences[key]=float(np.max(abs(delta.data),initial=0.))
        report['complete_nonlinear_state_jacobian_changes']=state_differences
        direction=np.zeros(view.size)
        direction[offset+view.tail_parameter_slice.start:offset+view.tail_parameter_slice.stop]=.03*np.cos(.4+np.arange(view.K+1)*.43)
        direction[offset+view.profile_parameter_slice.start:offset+view.profile_parameter_slice.stop]=.0003*np.sin(.6+np.arange(len(view.profile.supports))*.71)
        report['parameter_checks']=[]
        for step in (2e-5,1e-5):
            plus=gauss_cell_positive_gauss_hybrid(view,z+step*direction,jacobian=False,known_order=8)
            minus=gauss_cell_positive_gauss_hybrid(view,z-step*direction,jacobian=False,known_order=8)
            for res,jac in (('retained_residual','retained_jacobian'),('high_residual','high_jacobian')):
                exact=fine[jac]@direction;fd=(plus[res]-minus[res])/(2*step);error=fd-exact
                report['parameter_checks'].append(dict(step=step,block=res,analytic_norm=float(np.linalg.norm(exact)),
                    absolute_maximum=float(np.max(abs(error),initial=0.)),relative_L2=float(np.linalg.norm(error)/max(np.linalg.norm(exact),1e-12))))
        report['completed']=True;save()
        print(json.dumps({k:report[k] for k in ('completed','seconds','peak_rss_kib','G8_to_G12_full_difference','G2_to_hybrid_full_change','complete_nonlinear_state_jacobian_changes','parameter_checks')}),flush=True)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise

if __name__=='__main__':main()
