#!/usr/bin/env python3
"""Locate actual interior Gauss defect of an immutable R153/R155 P1 field.

No Jacobian, optimizer, new field, or geometric certificate. Evaluate the
two existing quadrature points and apply the two disjoint exact algebraic
field transforms, independently of the cell-report diagnostic reduction.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,datetime,json,resource,time,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE
from fd2d_gc_gauss_cell_codazzi import _view
from fd2d_gc_positive_gauss_l import positive_gauss_l_delta
from fd2d_gc_positive_trace_branch import positive_trace_delta


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('field','candidate','radius-packet','reference-inlet','out-prefix'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh output prefix')
    start=time.monotonic();here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-actual-positive-trace-interior-Gauss-location-v1',source=identity(__file__),
        provider=identity(here/'fd2d_gc_raw_bump_positive_trace.py'),input=identity(args.field),
        candidate=identity(args.candidate),started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        completed=False,no_BVP=True,no_Jacobian=True,no_new_field=True,continuous_certificate=False)
    def save():
        report.update(seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        arr=load_npz(args.field);packet=json.loads(args.radius_packet.read_text())
        if not packet['passed'] or packet['candidate_sha256']!=report['candidate']['sha256']:raise ValueError('Wrong certified radius input')
        problem=PositiveTraceRawBumpDAE(args.candidate,modes=int(arr['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            base_lower_bound='4/5',base_lower_provenance={**identity(args.radius_packet),'candidate_sha256':packet['candidate_sha256']},
            radius_floor=.1,minimum_active_n=.05)
        if not np.array_equal(problem.x,arr['mesh']):raise ValueError('Saved mesh differs')
        for key in ('angular_atlas_definition','coast_reference_definition','gauss_l_definition','positive_trace_definition'):
            if json.loads(str(arr[key]))!=getattr(problem,key):raise ValueError('Different field definition: '+key)
        y=arr['corrections'];p=arr['parameters'];rule=_view(problem,2);view=rule['view'];tau=rule['tau']
        yq=((1-tau)[None,:,None]*y[:-1,None,:]+tau[None,:,None]*y[1:,None,:]).reshape(view.N,view.q)
        ops=view.operators(p[view.profile_parameter_slice]);jet=ops['jet']
        lift=view.lifting(p[view.profile_parameter_slice],p[view.tail_parameter_slice])
        affine=np.stack((view.E@yq[:,:view.e].T,view.O@yq[:,view.e:view.d].T,view.E@yq[:,view.d:].T),axis=-1)+lift['values']
        angular=np.stack((view.Ex@yq[:,:view.e].T,view.Ox@yq[:,view.e:view.d].T,view.Ex@yq[:,view.d:].T),axis=-1)+lift['xi']
        d=positive_gauss_l_delta(affine,angular,jet['K'][None,:],view.window()[None,:],minimum_active_n=problem.minimum_active_n)
        background=affine.copy();background[:,:,2]=d['actual_l']
        bangular=angular.copy();bangular[:,:,2]+=d['delta_xi']
        trace=positive_trace_delta(background,bangular,jet['K'][None,:],view.trace_window()[None,:],exact_tail_mask=view.trace_mask()[None,:])
        actual=trace['actual'];G=actual[:,:,0]*actual[:,:,2]-actual[:,:,1]**2-jet['K'][None,:]
        perq=np.max(abs(G),axis=0);top=np.argsort(perq)[-12:][::-1]
        rows=[]
        for j in top:
            i=int(np.argmax(abs(G[:,j])));cell=int(j//2);q=int(j%2)
            rows.append(dict(cell=cell,quadrature_index=q,s=float(view.x[j]),xi=float(view.chart.theta[i]),material_u=float(view.coords['u'][i,j]),
                cell_endpoints=problem.x[cell:cell+2].tolist(),G=float(G[i,j]),n_m_l=actual[i,j].tolist(),
                affine_n_m_l=affine[i,j].tolist(),K=float(jet['K'][j]),coast_weight=float(view.window()[j]),trace_weight=float(view.trace_window()[j])))
        report.update(completed=True,maximum=float(np.max(abs(G))),locations=rows,
            quadrature_point_count=view.N,angular_point_count=view.work,formula='Exact saved affine P1+lifting, then R153, then R155; no projection or new interpolation')
        save();print(json.dumps({'completed':True,'maximum':report['maximum'],'locations':rows[:3]}),flush=True)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise


if __name__=='__main__':main()
