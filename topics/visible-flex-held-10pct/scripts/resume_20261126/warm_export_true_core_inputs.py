#!/usr/bin/env python3
"""Export newly computed strict core intervals for an actual warm field.

The mean file retains exactly the original 1168 literal binary64 angle
nodes. True period, support inverse, beta, position integral and phase
controls are enclosed independently. Optional external point/closed-box
arrays cover the whole angle circle. These are core inputs only, not a new
prefix metric, tail, reach, convergence, or closed-surface certificate.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import bisect
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import traceback
from fractions import Fraction as Q
import numpy as np
import mpmath as mp

HERE=Path(__file__).resolve().parent
MEAN_SHA='f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


def canonical_sha(value):
    text=json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)
    return hashlib.sha256(text.encode()).hexdigest()


def write(path,value):
    tmp=path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    tmp.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--source-run',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--external-nodes',type=int,default=0)
    p.add_argument('--allow-intermediate-lambda',action='store_true')
    a=p.parse_args()
    repo=a.repo.resolve();out=a.outdir.resolve();run=a.source_run.resolve()
    if out==repo or repo in out.parents:
        raise ValueError('Generated core arrays must remain outside the repository')
    if a.external_nodes and a.external_nodes<16:
        raise ValueError('A complete external angle grid needs at least 16 cells')
    out.mkdir(parents=True,exist_ok=False)
    start=time.monotonic()
    state=dict(status='loading_actual_source',complete=False,stages=[],result={},error=None,
        scope=__doc__,BVP_invoked=False,DN_invoked=False,complete_surface=False)
    def event(name,**values):
        state['progress']=dict(event=name,**values)
        state['seconds']=time.monotonic()-start
        write(out/'summary.json',state)
        print(json.dumps(dict(stage=name,seconds=time.monotonic()-start,**values),allow_nan=False),flush=True)
    try:
        scripts=repo/'topics/visible-flex-held-10pct/scripts'
        current=scripts/'resume_20261126';support=scripts/'resume_m3'
        mean_kernel=support/'certify_r59_fixed_mean_ranges.py'
        interval_kernel=scripts/'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py'
        record=json.loads(run.read_text())
        paths=[Path(__file__),HERE/'warm_phase_validated_core.py',
               support/'r53_validated_material_core.py',mean_kernel,interval_kernel]
        warm_models={'warm-supported-material-phase-fixed-metric-v2':'warm_fixed_m3_model_v2.py',
                     'warm-supported-material-phase-fixed-metric-v3':'warm_fixed_m3_model_v3.py'}
        kind=record.get('model_kind')
        if kind in warm_models:
            model_file=current/warm_models[kind]
            sys.path.insert(0,str(current))
            model=module('_true_warm_export_model',model_file)
            record=model.accepted_input(run,require_lambda_one=not a.allow_intermediate_lambda)
        elif record.get('model_kind')=='warm-supported-material-phase-fixed-metric-actual-dn':
            acceptance_file=current/'warm_actual_dn_acceptance.py'
            accepted=module('_true_warm_actual_acceptance',acceptance_file)
            record=accepted.accepted_actual_input(run,repo=repo)
            model_file=current/'warm_true_dn_solve.py'
            model=module('_true_warm_export_actual_model',model_file)
            paths.append(acceptance_file)
        else:
            raise ValueError('Require the explicit accepted v2/v3 warm or actual warm-DN model')
        paths.append(model_file)
        obj=model.load_model(dict(source_run=str(run),repo=str(repo)))
        physical_file=run.parent/'physical.npz'
        loader=module('_true_warm_export_physical',support/'audit_full_relative_metric.py')
        physical=loader.load_physical(physical_file)
        if physical.source_sha256!=record['physical_sha256']:
            raise ValueError('The accepted physical field changed')
        obj.initial(physical.p)
        flow=obj.flow(physical.p[0]);core=flow.exact_lift_core
        if not np.isfinite(flow.warp_e) or abs(float(flow.warp_e))>=1:
            raise ValueError('True material-angle interval boxes require finite abs(warp_e)<1')
        if record['mean_nodes']!=1168 or not hasattr(core,'baseline') or not hasattr(core,'controls'):
            raise ValueError('This source does not have the declared mean1168 supported-phase core')
        definition=record['warm_definition']
        source_kind=record.get('linear_source_model_kind',record['model_kind'])
        family=getattr(core,'phase_basis_kind','full_period_sine_v1')
        if source_kind=='warm-supported-material-phase-fixed-metric-v3':
            if (family!='complementary_arc_sine_v1' or
                    definition.get('phase_basis',{}).get('family')!=family):
                raise ValueError('The actual v3 core and full declared complementary family differ')
            for key in ('basis_anchor_v2_run','basis_anchor_v2_sha256'):
                if record.get(key)!=definition.get(key):
                    raise ValueError('The complete zero-control anchor binding differs: '+key)
        elif family!='full_period_sine_v1':
            raise ValueError('A complementary family requires its explicit accepted v3 source kind')
        oracle=module('_true_warm_export_oracle',HERE/'warm_phase_validated_core.py')
        v=oracle.build_oracle(core,support,mean_kernel,interval_kernel,
            progress=lambda value:event(value['stage'],**{k:x for k,x in value.items() if k not in ('stage','seconds')}))
        I,K=v.I,v.K
        bounds=v.all_angle_curvature_bounds()
        if not bounds['positive_curvature_certified']:
            state['result']['continuous_core_bounds']=bounds
            raise ArithmeticError('Positive curvature of the actual full warm core was not resolved')
        cache_tools=module('_true_warm_cache_distance',support/'certify_r53_core_lift_cache.py')
        paths.extend([support/'certify_r53_core_lift_cache.py',support/'audit_full_relative_metric.py'])
        paths.extend(Path(path) for path in record.get('source_hashes',{}))
        paths.extend([current/name for name in ('warm_supported_core_factory.py',
            'warm_fixed_m3_model.py','warm_auxiliary_domain_guard.py')])
        if source_kind in warm_models:
            paths.extend([current/'warm_supported_core_factory_v2.py',current/'warm_fixed_m3_model_v2.py'])
        if source_kind=='warm-supported-material-phase-fixed-metric-v3':
            paths.extend([current/'warm_complement_core_factory_v3.py',current/'warm_fixed_m3_model_v3.py'])
        source_hashes={str(path.resolve()):sha(path) for path in sorted(set(paths))}
        raw_file=run.parent/record['raw_return']['file']
        if sha(raw_file)!=record['raw_return']['sha256']:
            raise ValueError('The accepted raw return changed during core reconstruction')
        common=dict(source_run=str(run),source_run_sha256=sha(run),physical_sha256=sha(physical_file),
            raw_return_sha256=sha(raw_file),raw_return_file=str(raw_file),
            model_kind=record['model_kind'],modes=obj.M,homotopy=float(core.homotopy),
            linear_source_model_kind=source_kind,warm_definition=definition,
            warm_definition_sha256=canonical_sha(definition),phase_basis_family=family,
            phase_basis=definition.get('phase_basis',dict(family='full_period_sine_v1',frequency='3*j')),
            source_hashes=source_hashes,mean_nodes=1168,mean_rule_changed=False,
            complete_surface=False,fixed_metric_C2_convergence_paid=False,
            oracle=v.metadata(),continuous_all_angle_bounds=bounds,
            exact_core_regular_order_at_least=5,
            source_cache_is_not_treated_as_exact=True)
        for key in ('basis_anchor_v2_run','basis_anchor_v2_sha256','frozen_radial_chart'):
            if key in record:
                common[key]=record[key]
        N=1168
        ang=flow.angular(N);psi=np.asarray(ang[0],dtype=np.float64)
        psi_sha=hashlib.sha256(psi.tobytes()).hexdigest()
        literal=2*np.pi*np.arange(N)/N
        if not np.array_equal(psi,literal) or psi_sha!=MEAN_SHA:
            raise ValueError('The actual literal mean1168 node bytes changed')
        flow.geo(np.array([0.]),N)
        cache=flow.exact_lift_cache[N]
        initial=np.asarray(flow.exact_lift_initial,float)
        q=I(obj.q);warp=I(flow.warp_e);freq=I(np.asarray(flow.even,int))
        M=obj.M
        R0=q*I(initial[0]);R=q*I(initial[1:M+1])
        T=q*I(initial[M+1:2*M+1]);Z=q*I(initial[2*M+1:])
        fields=('F','Ft','Ftt','Fttt','Ftttt','H','H1','H2')
        arrays={name:np.empty((2,N,3)) for name in fields}
        material=np.empty((2,N))
        gaps={name:0. for name in ('H','H1','H2')}
        for j,pj in enumerate(psi):
            pp=I(float(pj));s3,c3=v.sincos(3*pp);sp,cp=v.sincos(pp)
            if pj==0:
                s3,sp,c3,cp=I(0),I(0),I(1),I(1)
            theta=pp-warp*s3/3;rho=1-warp*c3;rp=3*warp*s3
            g=v.point(theta)
            material[:,j]=[float(theta.x[0]),float(theta.x[1])]
            sn,cs=v.sincos(freq*pp)
            Rv=R0+(R*cs).sum();Tv=(T*sn).sum();Zv=(Z*cs).sum()
            R1=-(freq*R*sn).sum();T1=(freq*T*cs).sum();Z1=-(freq*Z*sn).sum()
            R2=-(freq.sq()*R*cs).sum();T2=-(freq.sq()*T*sn).sum();Z2=-(freq.sq()*Z*cs).sum()
            def cart(r,t,z):
                return [r*cp-t*sp,r*sp+t*cp,z]
            ini=cart(Rv,Tv,Zv);ini1=cart(R1-Tv,T1+Rv,Z1)
            ini2=cart(R2-2*T1-Rv,T2+2*R1-Tv,Z2)
            st,ct=v.sincos(theta)
            circle=[ct,st,I(0)];circle1=[-rho*st,rho*ct,I(0)]
            circle2=[-rho.sq()*ct-rp*st,-rho.sq()*st+rp*ct,I(0)]
            g['H']=[g['F'][k]-circle[k]-ini[k] for k in range(3)]
            g['H1']=[g['Ft'][k]*rho-circle1[k]-ini1[k] for k in range(3)]
            g['H2']=[g['Ftt'][k]*rho.sq()+g['Ft'][k]*rp-circle2[k]-ini2[k] for k in range(3)]
            for name in fields:
                for k,box in enumerate(g[name]):
                    if not box.finite():
                        raise ArithmeticError('A true mean-node core interval is nonfinite')
                    arrays[name][:,j,k]=[float(box.x[0]),float(box.x[1])]
            for name,cached in zip(('H','H1','H2'),cache):
                gaps[name]=max(gaps[name],cache_tools.gap_norm(g[name],cached[j],K))
            if (j+1)%128==0:
                event('literal_mean_core_nodes',completed=j+1,nodes=N)
        mean_file=out/'mean1168-core-intervals.npz'
        np.savez(mean_file,psi=psi,psi_lo=psi,psi_hi=psi,theta_point=material,
                 exact_lift_initial=initial,**arrays)
        mean=dict(common,status='strict_literal_mean_core_inputs_completed',complete=True,
            kind='warm_true_core_literal_mean_intervals',format_version=1,
            arrays=dict(path=str(mean_file),sha256=sha(mean_file)),literal_psi_sha256=psi_sha,
            exact_lift_initial_sha256=hashlib.sha256(initial.tobytes()).hexdigest(),
            source_cache_distance_upper=gaps,array_axes='(lower_or_upper, literal_node, Cartesian_component)',
            input_angles='Exact literal binary64 NumPy mean nodes; mathematical true sin/cos at those nodes',
            original_mean_primitive_resampled=False,
            scope='Strict fresh core/lift inputs on the unchanged finite mean rule; no radial mean integral or full prefix certificate')
        write(out/'mean1168-core.json',mean)
        state['result']['mean_core_certificate']=dict(path=str(out/'mean1168-core.json'),
            sha256=sha(out/'mean1168-core.json'),arrays_sha256=sha(mean_file))
        event('literal_mean_core_inputs_completed',source_cache_distance_upper=gaps)
        if a.external_nodes:
            external_count=a.external_nodes
            points=2*np.pi*np.arange(external_count)/external_count
            upper_period=float(v.from_mp(2*mp.iv.pi).x[1])
            lows=points.copy();highs=np.r_[points[1:],upper_period]
            cuts=[]
            for sector in range(-1,5):
                for boundary in v.pg:
                    value=boundary+sector*v.T
                    cuts.extend([float(value.x[0]),float(value.x[1])])
            cuts=sorted(set(cuts))
            jet_names=('F','Ft','Ftt','Fttt','Ftttt')
            point={key:np.empty((2,external_count,3)) for key in jet_names}
            boxes={key:np.empty((2,external_count,3)) for key in jet_names}
            theta_points=np.empty((2,external_count));theta_boxes=np.empty((2,external_count))
            total_parts=0;maximum_parts=0
            def theta_at(value):
                if value==0:
                    return I(0)
                value=I(float(value));sn,_=v.sincos(3*value)
                return value-warp*sn/3
            def hull_jets(theta):
                nonlocal total_parts,maximum_parts
                lo,hi=map(float,theta.x)
                middle=cuts[bisect.bisect_right(cuts,lo):bisect.bisect_left(cuts,hi)]
                partition=[lo,*middle,hi]
                result=None;parts=0
                for left,right in zip(partition[:-1],partition[1:]):
                    values=v.point(I(left,right));parts+=1
                    if result is None:
                        result={key:list(values[key]) for key in jet_names}
                    else:
                        result={key:[v.hull(old,new) for old,new in zip(result[key],values[key])]
                                for key in jet_names}
                total_parts+=parts;maximum_parts=max(maximum_parts,parts)
                return result
            for j,(lo,hi) in enumerate(zip(lows,highs)):
                tl,tr=theta_at(lo),theta_at(hi)
                box=I(float(tl.x[0]),float(tr.x[1]))
                theta_points[:,j]=[float(tl.x[0]),float(tl.x[1])]
                theta_boxes[:,j]=[float(box.x[0]),float(box.x[1])]
                gp,gb=hull_jets(tl),hull_jets(box)
                for key in jet_names:
                    for k in range(3):
                        point[key][:,j,k]=[float(gp[key][k].x[0]),float(gp[key][k].x[1])]
                        boxes[key][:,j,k]=[float(gb[key][k].x[0]),float(gb[key][k].x[1])]
                if (j+1)%128==0:
                    event('external_core_nodes_and_boxes',completed=j+1,nodes=external_count)
            external_file=out/'external-core-intervals.npz'
            np.savez(external_file,psi=points,psi_lo=lows,psi_hi=highs,
                theta_point=theta_points,theta_box=theta_boxes,
                **{'point_'+key:value for key,value in point.items()},
                **{'box_'+key:value for key,value in boxes.items()})
            external=dict(common,status='strict_external_core_inputs_completed',complete=True,
                kind='warm_true_core_external_intervals',format_version=1,nodes=external_count,
                arrays=dict(path=str(external_file),sha256=sha(external_file)),
                interval_output_sha256=sha(external_file),
                material_parts=total_parts,maximum_parts_per_query=maximum_parts,
                exact_final_endpoint='The last binary upper endpoint encloses mathematical 2pi',
                splitting='Both dyadic ends of each rigorous sector/window/Taylor partition boundary are included',
                scope='True core Gamma through fourth material derivative on nodes and full closed angle boxes only')
            write(out/'external-core.json',external)
            state['result']['external_core_certificate']=dict(path=str(out/'external-core.json'),
                sha256=sha(out/'external-core.json'),arrays_sha256=sha(external_file))
        state.update(status='requested_true_core_inputs_completed',complete=True)
        event('requested_true_core_inputs_completed')
        return 0
    except Exception as error:
        state.update(status='error',error=repr(error),traceback=traceback.format_exc())
        event('error',error=repr(error))
        return 1


if __name__=='__main__':
    sys.exit(main())
