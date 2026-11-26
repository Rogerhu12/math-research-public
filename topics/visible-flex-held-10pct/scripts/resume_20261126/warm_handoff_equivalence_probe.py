#!/usr/bin/env python3
"""Read-only raw-grid checks at the actual R53 -> zero-phase handoff.

No solve_bvp, finite acceptance, or continuation is performed. The source
must be a real accepted original run and --warm-run an actual prepared
same-lambda, same-M attempt. Two radial coordinate choices are compared:
the deployed fixed constructor and the literal original radial chart.
The latter only changes the numerical coordinate, not the physical metric.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback
import numpy as np
import scipy
import scipy.integrate._bvp as bvp


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def finite_max(value):
    result=float(np.max(np.abs(value)))
    if not math.isfinite(result):
        raise FloatingPointError('Nonfinite comparison')
    return result


def gap(a,b):
    a,b=np.asarray(a),np.asarray(b)
    return dict(max_abs=finite_max(a-b),max_reference=finite_max(a),
                bitwise_equal=bool(np.array_equal(a,b)))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--source-run',type=Path,required=True)
    p.add_argument('--warm-run',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--skip-jacobian-probe',action='store_true')
    a=p.parse_args()
    a.outdir.mkdir(parents=True,exist_ok=False)
    start=time.monotonic()
    output=dict(status='preparing',result={},error=None,
        scope=__doc__,BVP_invoked=False,accepted_warm_candidate=False,
        complete_surface=False,source_run=str(a.source_run.resolve()),
        source_run_sha256=sha(a.source_run),warm_run=str(a.warm_run.resolve()),
        warm_run_sha256=sha(a.warm_run),source_sha256=sha(__file__),
        scipy_version=scipy.__version__,scipy_bvp_sha256=sha(bvp.__file__))
    def save():
        output['elapsed']=time.monotonic()-start
        path=a.outdir/'summary.json'
        tmp=path.with_suffix('.tmp')
        tmp.write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
        tmp.replace(path)
    def event(name,**values):
        output['progress']=dict(event=name,**values)
        save()
        print(json.dumps(dict(event=name,elapsed=time.monotonic()-start,**values)),flush=True)
    def measure(obj,x,y,par):
        h=np.diff(x)
        cr,ym,f,fm=bvp.collocation_fun(obj.fun,y,par,x,h)
        spline=bvp.create_spline(y,f,x,h)
        rms=bvp.estimate_rms_residuals(obj.fun,spline,x,h,par,1.5*cr/h,fm)
        bc=obj.bc(y[:,0],y[:,-1],par)
        physical_bc=obj.terminal(y[:,-1],par)*obj.bcweights
        return dict(rms=rms,bc=bc,physical_bc=physical_bc,f=f,fm=fm,cr=cr,
                    summary=dict(nodes=len(x),rms_max=finite_max(rms),
                    scaled_bc_max=finite_max(bc),physical_bc_max=finite_max(physical_bc),
                    collocation_residual_max=finite_max(cr),rhs_max=finite_max(f)))
    try:
        scripts=a.repo/'topics/visible-flex-held-10pct/scripts'
        current=scripts/'resume_20261126'
        sys.path.insert(0,str(current))
        model=module('_probe_warm_model',current/'warm_fixed_m3_model.py')
        record=json.loads(a.warm_run.read_text())
        original=json.loads(a.source_run.read_text())
        output['result']['actual_warm_attempt_error']=record.get('error')
        output['result']['actual_warm_attempt_traceback']=record.get('traceback','')[-6000:]
        if (not original.get('solver_success') or
                not original.get('raw_return',{}).get('success') or original.get('error')):
            raise ValueError('Require the actual successful original raw return')
        if original.get('prefix_audit',{}).get('metric_l1',math.inf)>1e-6:
            raise ValueError('Original finite metric gate did not pass')
        if (record['model_kind']!=model.KIND or
                Path(record['origin_design_run']).resolve()!=a.source_run.resolve() or
                record['origin_design_sha256']!=sha(a.source_run) or
                record['modes']!=original['modes'] or
                record['homotopy']!=original['core_settings']['homotopy']):
            raise ValueError('Probe is only for the literal same-M, same-lambda anchor')
        old,source,signature,oldp=model.bootstrap(a.source_run)
        if signature!=record['frozen_source_signature']:
            raise ValueError('Numerical source binding differs')
        raw_path=a.source_run.parent/source['raw_return']['file']
        if sha(raw_path)!=source['raw_return']['sha256']:
            raise ValueError('Original raw return changed')
        with np.load(raw_path,allow_pickle=False) as raw:
            x,y,oldp,scales=(raw[k].copy() for k in ('x','y','p','pscale'))
            saved_rms=raw['rms'].copy()
        if not np.array_equal(scales,old.pscale):
            raise ValueError('Original auxiliary scales changed')
        old_initial=old.initial(oldp).copy()
        oldcore=old._core
        oldflow=old.flow(oldp[0])
        old_s,old_ds=old.chart(x,oldp[0])
        original_measure=measure(old,x,y,oldp)
        output['result']['original']=original_measure['summary']
        output['result']['original_recomputed_vs_saved_rms']=gap(saved_rms,original_measure['rms'])
        obj=model.build_model(old,source,record,anchor_baseline=oldcore)
        newp=np.zeros(obj.M)
        initial=obj.initial(newp).copy()
        flow=obj.flow(0.)
        theta=2*np.pi*np.arange(max(1168,32*obj.M))/max(1168,32*obj.M)
        before,after=oldcore.evaluate(theta),obj._core.evaluate(theta)
        output['result']['complete_core_zero_control_jets']={
            key:gap(before[key],after[key]) for key in ('F','Ft','Ftt')}
        output['result']['initial_projection']=gap(old_initial,initial)
        output['result']['angular_nodes']=dict(original=old.nt,warm=obj.nt,
            mean_source=source.get('prefix_audit',{}).get('samples_psi'),mean_warm=record['mean_nodes'])
        output['result']['radial_chart']=dict(original_join=old.chart_join,
            warm_join=obj.chart_join,original_reference_prefix=old.chart_reference_prefix,
            warm_reference_prefix=obj.chart_reference_prefix,
            physical_end_gap=abs(float(oldflow.end-flow.end)))
        legacy=np.maximum(obj.q**np.arange(2,obj.M+1),1e-10)
        output['result']['actual_phase_parameter_scale_factors']=np.r_[1.,obj.pscale/legacy].tolist()
        output['result']['auxiliary_coordinate_domain']=dict(
            p0_lower=math.log(1e-7/obj.seed_support_amplitude),
            p0_upper=math.log(.124/obj.seed_support_amplitude),
            coordinate_only=True,changes_metric=False)
        probe=newp.copy();probe[0]=1000.
        try:
            obj.initial(probe)
            overflow='Unexpectedly accepted p0=1000'
        except Exception as error:
            overflow=type(error).__name__+': '+str(error)
        obj.initial(newp)
        output['result']['out_of_domain_p0_exception']=overflow
        event('source_and_core_checked')

        # Node values are identical here; no interpolation, lift correction,
        # or new chart break is inserted into either comparison.
        x_default=obj.inverse_chart(old_s,0.)
        default=measure(obj,x_default,y,newp)
        output['result']['deployed_fixed_radial_chart']=default['summary']
        output['result']['deployed_same_physical_node_rhs']=gap(
            original_measure['f']/old_ds[None,:],
            default['f']/obj.chart(x_default,0.)[1][None,:])
        output['result']['deployed_boundary_gap']=gap(original_measure['bc'],default['bc'])
        event('deployed_radial_chart_checked',rms=default['summary']['rms_max'])

        obj.chart_join=old.chart_join
        obj.chart_reference_prefix=old.chart_reference_prefix
        obj.chart_breaks=old.chart_breaks.copy()
        fixed=measure(obj,x,y,newp)
        output['result']['frozen_original_radial_chart']=fixed['summary']
        output['result']['frozen_chart_gap']={
            's':gap(old_s,obj.chart(x,0.)[0]),'ds':gap(old_ds,obj.chart(x,0.)[1])}
        output['result']['raw_equation_gaps']={key:gap(original_measure[key],fixed[key])
            for key in ('f','fm','cr','bc','physical_bc','rms')}
        event('original_raw_chart_checked',rms=fixed['summary']['rms_max'])

        audit=module('_probe_physical_loader',scripts/'resume_m3/audit_full_relative_metric.py')
        compare=module('_probe_complete_jets',current/'warm_fixed_m3_compare_c2.py')
        physical=audit.load_physical(a.source_run.parent/'physical.npz')
        if physical.source_sha256!=source['physical_sha256'] or not np.array_equal(physical.p,oldp):
            raise ValueError('Actual physical interpolant or parameter vector changed')
        sp=np.unique(np.r_[0.,.25*flow.prefix_end,.5*flow.prefix_end,
                            .7*flow.prefix_end,.9*flow.prefix_end,flow.prefix_end,flow.end])
        jets=[compare.complete_jets(o,f,physical,sp,1168,1168,np.zeros(len(sp)))
              for o,f in ((old,oldflow),(obj,flow))]
        output['result']['same_physical_interpolant_jet_gaps']={
            name:gap(jets[0][name],jets[1][name]) for name in jets[0]}
        output['result']['same_physical_interpolant_jet_scope']=(
            'Seven physical radii, mean1168. F is compared before adding the '
            'common vertical primitive; its difference is unchanged by the '
            'same literal primitive. Fs and Fss include independently '
            'evaluated mean derivatives. No height primitive is recomputed '
            'or silently used as a new acceptance certificate.')
        event('same_physical_interpolant_jets_checked')

        if not a.skip_jacobian_probe:
            # A small actual Jacobian/FD probe; no collocation matrix or LU.
            indices=np.unique(np.clip(np.r_[0,len(x)//4,len(x)//2,3*len(x)//4,len(x)-1],0,len(x)-1))
            xt,yt=x[indices],y[:,indices]
            _,analytic=obj.fun_jac(xt,yt,newp)
            _,_,bcj=obj.bc_jac(y[:,0],y[:,-1],newp)
            columns=sorted(set(j for j in (0,1,6,7,8,obj.M-1) if j<obj.M))
            comparisons=[]
            for j in columns:
                rows=[]
                for step in (1e-5,2e-6):
                    plus,minus=newp.copy(),newp.copy()
                    plus[j]+=step;minus[j]-=step
                    fd=(obj.fun(xt,yt,plus)-obj.fun(xt,yt,minus))/(2*step)
                    bfd=(obj.bc(y[:,0],y[:,-1],plus)-obj.bc(y[:,0],y[:,-1],minus))/(2*step)
                    rows.append(dict(step=step,rhs=gap(analytic[:,j,:],fd),bc=gap(bcj[:,j],bfd)))
                comparisons.append(dict(column=j,comparisons=rows))
                event('actual_parameter_column_checked',column=j)
            obj.initial(newp)
            output['result']['analytic_parameter_columns']=comparisons
        output['status']='read_only_probe_complete'
        output['result']['scope_limit']='Finite actual raw-grid/column checks only. No new BVP return, acceptance, lambda progress, continuous certificate, or completion.'
        save()
        return 0
    except Exception as error:
        output.update(status='error',error=repr(error),traceback=traceback.format_exc())
        save()
        print(json.dumps(dict(event='error',error=repr(error))),flush=True)
        return 1


if __name__=='__main__':
    sys.exit(main())
