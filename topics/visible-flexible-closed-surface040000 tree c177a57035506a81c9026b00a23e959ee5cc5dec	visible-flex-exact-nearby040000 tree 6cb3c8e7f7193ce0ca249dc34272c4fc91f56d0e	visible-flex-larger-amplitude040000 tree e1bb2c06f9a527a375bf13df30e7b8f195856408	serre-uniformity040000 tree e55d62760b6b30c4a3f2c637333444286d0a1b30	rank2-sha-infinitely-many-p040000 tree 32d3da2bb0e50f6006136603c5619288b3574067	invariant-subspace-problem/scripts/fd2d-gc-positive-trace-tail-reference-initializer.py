#!/usr/bin/env python3
"""Explicit R157 late initializer on the frozen R153/R155 actual field.

A fixed wide radial window blends the old complete affine/R153 field to
cut-material-kappa plus b I. K_ref=max(K,0) is used only in this initializer
if needed; every actual equation uses the untouched physical K. This is a
new projected initial field, not an exact representation or a GC solution.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,datetime,json,resource,time,traceback,gc
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE,checkpoint_arrays,terminal_window
from fd2d_gc_gauss_cell_positive_trace import gauss_cell_positive_trace
from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi
from fd2d_gc_terminal_rank_one_reference import terminal_rank_one_reference
from fd2d_gc_bump_residual_locations import residual_locations


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('candidate','warm-start','radius-packet','reference-inlet','out-prefix'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path);ap.add_argument('--blend-start',type=float,default=1.3)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh explicit initializer name')
    started=time.monotonic();report=dict(schema='fd2d-explicit-R157-wide-blend-positive-trace-initializer-v1',source=identity(__file__),
        input=identity(args.warm_start),candidate=identity(args.candidate),reference_source=identity(Path(__file__).with_name('fd2d_gc_terminal_rank_one_reference.py')),
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),completed=False,exception=None,nonlinear_BVP_performed=False,continuous_certificate=False)
    def save():
        report.update(seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        a=load_npz(args.warm_start);proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:raise ValueError('Wrong radius packet')
        p=PositiveTraceRawBumpDAE(args.candidate,modes=int(a['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            base_lower_bound='4/5',base_lower_provenance=dict(**identity(args.radius_packet),candidate_sha256=proof['candidate_sha256']),radius_floor=.1)
        if str(a['candidate_sha256'])!=report['candidate']['sha256'] or not np.array_equal(a['mesh'],p.x):raise ValueError('Wrong source mesh or metric')
        if not p.gauss_l_definition['support'][1]<args.blend_start<p.trace_ramp_stop:raise ValueError('Blend must be disjoint from the coast and precede terminal plateau')
        old=np.r_[a['corrections'].ravel(),a['parameters']];y,parameters=p.unpack(old)
        _,olddata=p.coast_background_view().evaluate(old)
        fields=olddata['fields'];lift=olddata['lift']['values'];K=olddata['profile_jet']['K']
        chi=terminal_window(p.x,args.blend_start,p.trace_ramp_stop)
        active=chi>0;u=p.coords['u'][:,active]
        cut_kappa=p.tail(parameters[p.tail_parameter_slice]).curve(.8*np.sin(u),integrate=False)['kappa']
        reference=terminal_rank_one_reference(np.maximum(K[active],0)[None,:],cut_kappa,u)['values']
        desired=(1-chi[active])[None,:,None]*fields[:,active]+chi[active][None,:,None]*reference
        new=y.copy();difference=desired-lift[:,active]
        new[active,:p.e]=(p.PE@difference[:,:,0]).T
        new[active,p.e:p.d]=(p.PO@difference[:,:,1]).T
        new[active,p.d:]=(p.PE@difference[:,:,2]).T
        vector=p.impose_linear_boundary_values(np.r_[new.ravel(),parameters.copy()])
        definition=dict(kind='new_R157_cut_material_tail_plus_isotropic_reference_with_wide_quintic_blend',
            blend_start=args.blend_start,blend_stop=p.trace_ramp_stop,step=5,
            kappa='Exact cut kappa_T(u), evaluated at .8*sin(material u), frozen along radial reference',
            reference_K='max(actual K,0), initializer only; actual target K and all equations unchanged',
            negative_K_reference_node_count=int(np.count_nonzero(K[active]<0)),negative_reference_K_minimum=float(np.min(K[active])),
            actual_g_changed=False,actual_parameters_unchanged=bool(np.array_equal(vector[-p.parameter_count:],parameters)),
            old_actual_field_preserved=False,finite_projection_changed=True,cut_and_central_boundary_exact=True,
            earlier_zero_window_coefficients_unchanged=bool(np.array_equal(p.unpack(vector)[0][chi==0],y[chi==0])),
            exact_trace_gauge_applied=True,R157_GC_solution_claimed=False)
        report['initializer_definition']=definition
        report['warm']=save_npz(stem.with_name(stem.name+'-warm.npz'),**checkpoint_arrays(p,vector,report['candidate']['sha256']),
            initializer_definition=np.array(json.dumps(definition,sort_keys=True)),initializer_input_sha256=np.array(report['input']['sha256']))
        del olddata,fields,lift,new,difference,reference;gc.collect()
        raw,data=p.evaluate(vector);del data['lift'],data['fields_parameters']
        quadrature=gauss_cell_codazzi(p,vector,jacobian=False,order=2,block_cells=8,consumer=gauss_cell_positive_trace)
        actual_raw=np.r_[quadrature['retained_residual'],raw[(p.N-1)*p.d:]]
        n,m,l=(data['fields'][:,:,j] for j in range(3));disc=np.hypot(n-l,2*m)
        data['codazzi_cells']=quadrature['retained_cells']
        report['actual_initial']=dict(raw_maximum=float(np.max(abs(actual_raw))),full_G_node_maximum=float(np.max(abs(data['full_gauss']))),
            formal_curvature_node_maximum=float(np.max(np.maximum(abs(n+l+disc),abs(n+l-disc)))/2),
            full_average_C_maximum=quadrature['info']['sampled_full_average_codazzi_maximum'],
            high_average_C_maximum=quadrature['info']['sampled_omitted_average_codazzi_maximum'],
            gap=float(data['axes']['gap']),coast_minimum_n=data['gauss_l_delta']['sampled_minimum_active_n'],
            actual_node_reference_projection_difference=float(np.max(abs(data['fields'][:,active]-desired))),
            no_solve_or_strong_target_claim=True)
        report['locations']=residual_locations(p,vector,data,{'omitted_codazzi_cells':quadrature['omitted_codazzi_cells']},7.2)
        report['completed']=True;save();print(json.dumps(dict(completed=True,warm=report['warm'],initial=report['actual_initial']),allow_nan=False),flush=True)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise

if __name__=='__main__':main()
