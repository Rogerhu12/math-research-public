#!/usr/bin/env python3
"""Select a genuine full-field continuation guess on a compact geometry grid.

This design screen retains every raw state and core mode, the original
material chart, the production angular means of height derivatives, and
the exact original inlet correction. It intentionally integrates height
on the compact positive Gauss-6 partition instead of all raw cells. Thus
size and the LP objective are approximate design proxies. A selected guess
still needs the original full warm residual/geometry check and a new actual
nonlinear full-H BVP with every original final audit.
"""
from __future__ import annotations

import argparse
import copy
import gzip
import hashlib
import io
import json
import math
import os
from pathlib import Path
import sys
import time
from types import SimpleNamespace

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import linprog
from strong_20261114_loop_bridge import rebuild

PRIMARY = ('delta', 'boost_length', 'boost_speed')
# Finite-difference width and the largest first trial increment. The LP
# uses normalized variables, then the actual continuation uses these units.
CONTROL = {
    'actual_q1': (.0005, .032),
    'actual_q4': (2e-5, .001),
    'actual_c6': (1e-6, .00015),
    'loop_curvature': (.003, 1.),
    'loop_radius': (1e-4, .04),
    'loop_speed': (1e-5, .003),
    'terminal_peak_fraction': (2e-4, .04),
    'vu': (.0002, .04),
    'descending_turn_curvature': (.0025, 1.),
    'start_acceleration': (.002, .15),
    'initial_speed_frontload': (.005, .2),
    'vd': (.00005, .004),
    'descending_sync_curvature': (.003, .5),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path); data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def response_directions(response, names):
    result = {}
    rows = {row['direction']: row for row in response['prescribed_low_core_responses']}
    rows.update({row['external_field']: row for row in response['additional_core_held_directions']})
    for name in names:
        suffix = ('-prescribed-' if name.startswith('actual_') else '-core-held-')+name+'.npy.gz'
        matches = [item for item in response['tangent_arrays'] if item['file'].endswith(suffix)]
        if len(matches) != 1 or sha(matches[0]['file']) != matches[0]['sha256']:
            raise ValueError('A complete same-state direction is missing or changed: '+name)
        with gzip.open(matches[0]['file'], 'rb') as stream:
            vector = np.load(stream, allow_pickle=False)
        result[name] = dict(row=rows[name], vector=vector, source=matches[0])
    return result


def geometry(obj, x, y, p, grid, angular):
    """Original Cartesian cubic jets; only the height partition is coarsened."""
    obj.select(p); flow = obj.flow()
    s_nodes, _ = obj.chart(x, 0.)
    s, _ = obj.chart(grid, 0.)
    if not np.all(np.diff(s_nodes) > 0) or not np.all(np.diff(s) > 0):
        raise ValueError('A physical chart lost strict orientation')
    cubic = CubicSpline(s_nodes, y, axis=1)
    mean_angular = max(512, 16*(3*flow.M+1))
    _, mean_B1, mean_B2 = flow.basis(mean_angular)
    gauss, weights = np.polynomial.legendre.leggauss(6)
    lengths = np.diff(s)
    q = ((s[:-1]+s[1:])[:, None]+lengths[:, None]*gauss)/2
    flat = q.ravel(); means = np.empty_like(flat)
    for first in range(0, len(flat), 8):
        points = flat[first:first+8]
        frame = flow.frame(points, flow.base(points)+obj.q*cubic(points), mean_B1, mean_B2)
        means[first:first+8] = np.mean(frame['V'][:, :, 2], axis=1)
    height = np.r_[0., np.cumsum(lengths/2*(means.reshape(q.shape)@weights))]
    B, B1, B2 = flow.basis(angular)
    values = np.empty((len(grid), angular, 3))
    margin, area_min, metric_max, zmax = np.inf, np.inf, 0., 0.
    for first in range(0, len(s), 8):
        sl = slice(first, first+8); ss = s[sl]
        Y, Ys, Yss = cubic(ss), cubic(ss, 1), cubic(ss, 2)
        frame, mixed, _ = flow.velocity_s(ss, Y, Ys, B1, B2)
        mean_frame, _, mean_dW = flow.velocity_s(ss, Y, Ys, mean_B1, mean_B2)
        geo = frame['geo']
        Fs = geo['s1']+obj.q*flow.values(Ys, B)
        Fs[:, :, 2] += np.mean(mean_frame['V'][:, :, 2], axis=1)[:, None]
        Fss = geo['s2']+obj.q*flow.values(Yss, B)
        Fss[:, :, 2] += np.mean(mean_dW[:, :, 2], axis=1)[:, None]
        Ft, Ftt = frame['d'], frame['dd']
        cross = np.cross(Fs, Ft); area = np.linalg.norm(cross, axis=2)
        if not np.isfinite(area).all() or np.min(area) <= 0:
            raise FloatingPointError('Degenerate cubic tangent plane')
        normal = cross/area[:, :, None]
        E, F, G = np.sum(Fs*Fs, axis=2), np.sum(Fs*Ft, axis=2), np.sum(Ft*Ft, axis=2)
        determinant = E*G-F*F
        if np.min(determinant) <= 0:
            raise FloatingPointError('Nonpositive cubic first fundamental form')
        e, f, g = np.sum(normal*Fss, axis=2), np.sum(normal*mixed, axis=2), np.sum(normal*Ftt, axis=2)
        trace = (e*G-2*f*F+g*E)/determinant
        product = (e*g-f*f)/determinant
        discriminant = trace*trace-4*product
        tolerance = 128*np.finfo(float).eps*(1+trace*trace+4*abs(product))
        if np.any(discriminant < -tolerance):
            raise FloatingPointError('Principal-curvature discriminant is negative')
        root = np.sqrt(np.maximum(discriminant, 0.))
        values[sl, :, 0], values[sl, :, 1] = (trace-root)/2, (trace+root)/2
        position = geo['pos']+obj.q*flow.values(Y, B)
        position[:, :, 2] += height[sl, None]
        values[sl, :, 2] = 2*np.linalg.norm(position, axis=2)
        physical_s = Fs-geo['v'][:, :, None]*Ft
        physical_theta = Ft/geo['rho'][:, :, None]
        a = flow.profile(ss)[0][:, None]
        defects = [np.sum(physical_s**2, axis=2)-1,
            np.sum(physical_s*physical_theta, axis=2)/a,
            np.sum(physical_theta**2, axis=2)/a**2-1]
        metric_max = max(metric_max, *[float(np.sum(abs(np.fft.fft(v, axis=1)/angular), axis=1).max()) for v in defects])
        margin = min(margin, float(frame['margin'].min()), float(mean_frame['margin'].min()))
        area_min = min(area_min, float(area.min()))
        zmax = max(zmax, float(abs(position[:, :, 2]).max()))
    if not np.isfinite(values).all() or margin <= 0:
        raise FloatingPointError('Finite geometry or Frenet domain failed')
    core = obj.actual_coefficients(p)
    kap = float(abs(values[:, :, :2]).max()); size = float(values[:, :, 2].max())
    gap = 2*float(core[::2].sum())
    return values, dict(kappa_sample=kap, twice_norm_coarse_height_sample=size,
        kappa_times_size_proxy=kap*size, complete_core_axis_gap=gap,
        gap_over_size_proxy=gap/size, metric_l1_sample=metric_max,
        frenet_margin_sample=margin, tangent_area_min_sample=area_min,
        height_max_coarse_sample=zmax, physical_profile=dict(flow.cfg),
        actual_core=core.tolist(), angular=angular, mean_angular=mean_angular,
        radial_samples=len(s), mean_height_partition='compact material grid; positive Gauss6',
        local_height_derivative_angular_rule='unchanged production max(512,16*(3M+1))',
        nonlinear_solution=False)


def optimize(base, slopes, rows, names, core, profile, sampled_directions, size_factors, trust):
    count = len(names); frequencies = 2*np.arange(1, len(core)+1)
    scales = np.array([CONTROL[name][1] for name in names])
    core_slopes = np.column_stack([rows[name]['row']['core_derivative'] for name in names])*scales
    gap_slopes = 2*core_slopes[::2].sum(axis=0)
    tail_indices = np.flatnonzero(frequencies >= 16)
    weights = frequencies**2-1
    variables = count+len(tail_indices)
    tail_scale = max(float(np.sum(weights[tail_indices]*abs(core[tail_indices]))), 1e-6)
    b0 = base.reshape(-1, 3); ss = slopes.reshape(-1, 3, count)
    # Row generation retains the full compact sample set while avoiding
    # huge dense inequalities in the LP solver.
    extrema = []
    groups = [(0,-1),(0,1),(1,-1),(1,1),(2,1)]
    for component, sign in groups:
        extrema.append(set(np.argsort(sign*b0[:, component])[-64:].tolist()))
    bounds = []
    for name in names:
        if name in ('actual_q1','initial_speed_frontload'):bounds.append((0.,trust))
        elif name == 'start_acceleration':bounds.append((-trust,0.))
        else:bounds.append((-trust,trust))
    bounds += [(0.,None)]*len(tail_indices)
    common_A, common_b = [], []
    for local, index in enumerate(tail_indices):
        for sign in (-1,1):
            row = np.zeros(variables)
            row[:count] = sign*weights[index]*core_slopes[index]/tail_scale
            row[count+local] = -1.
            common_A.append(row);common_b.append(-sign*weights[index]*core[index]/tail_scale)
    for frequency in (16,24,32,40,48):
        mask = frequencies[tail_indices] >= frequency
        budget = float(np.sum(weights[frequencies>=frequency]*abs(core[frequencies>=frequency])))
        row = np.zeros(variables);row[count:][mask] = 1.
        common_A.append(row);common_b.append(max(1.5*budget, .02*tail_scale)/tail_scale)
    # Keep the complete-field first-order guess in a finite neighborhood.
    # These rows use every state component at the selected raw mesh sites.
    for sign in (-1,1):
        raw_rows = np.zeros((len(sampled_directions),variables))
        raw_rows[:,:count] = sign*sampled_directions
        common_A.extend(raw_rows);common_b.extend(np.full(len(raw_rows),.08))
    for field, radius in (('delta',.05),('boost_length',.06),('boost_speed',.10)):
        derivative=np.array([rows[name]['row']['physical_profile_derivative'].get(field,0.) for name in names])*scales
        for sign in (-1,1):
            row=np.zeros(variables);row[:count]=sign*derivative
            common_A.append(row);common_b.append(radius)
    common_A=np.asarray(common_A);common_b=np.asarray(common_b)
    objective=np.r_[-gap_slopes/tail_scale,np.zeros(len(tail_indices))]
    result=[]; size0=float(base[:,:,2].max())
    for factor in size_factors:
        cap=size0*factor; kcap=33.0/cap
        active=[set(v) for v in extrema]
        fitted=None;worst=np.inf
        for iteration in range(25):
            A=[common_A];b=[common_b]
            for (component,sign),chosen in zip(groups,active):
                idx=np.asarray(sorted(chosen),dtype=int)
                matrix=np.zeros((len(idx),variables));matrix[:,:count]=sign*ss[idx,component]
                limit=cap if component==2 else kcap
                A.append(matrix);b.append(limit-sign*b0[idx,component])
            fitted=linprog(objective,A_ub=np.vstack(A),b_ub=np.hstack(b),bounds=bounds,method='highs')
            if not fitted.success:break
            predicted=b0+np.einsum('ijk,k->ij',ss,fitted.x[:count])
            worst=-np.inf;added=0
            for j,(component,sign) in enumerate(groups):
                limit=cap if component==2 else kcap
                violation=sign*predicted[:,component]-limit
                worst=max(worst,float(violation.max()))
                indices=np.flatnonzero(violation>1e-8)
                if len(indices):
                    indices=indices[np.argsort(violation[indices])[-64:]]
                    previous=len(active[j]);active[j].update(indices.tolist());added+=len(active[j])-previous
            if worst <= 1e-8 or not added:break
        item=dict(size_factor=factor,size_cap=cap,kappa_cap=kcap,success=bool(fitted.success and worst<=1e-8),
            solver_message=fitted.message,compact_rows=5*len(b0),iterations=iteration+1)
        if item['success']:
            physical=dict(zip(names,(fitted.x[:count]*scales).tolist()))
            predicted_core=core+core_slopes@fitted.x[:count]
            increment={}
            for name,value in physical.items():
                for field,derivative in rows[name]['row']['physical_profile_derivative'].items():
                    increment[field]=increment.get(field,0.)+value*derivative
            item.update(physical_steps=physical,target_core=predicted_core[:3].tolist(),
                complete_predicted_core=predicted_core.tolist(),physical_profile_increment=increment,
                predicted_gap=2*float(predicted_core[::2].sum()),
                predicted_kappa=float(abs(predicted[:,:2]).max()),predicted_size=float(predicted[:,2].max()),
                maximum_compact_row_violation=worst)
        result.append(item)
    return result


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--compact-response',type=Path,required=True)
    parser.add_argument('--compact-out',type=Path,required=True)
    parser.add_argument('--compact-controls',default=','.join(CONTROL))
    parser.add_argument('--compact-angular',type=int,default=256)
    parser.add_argument('--compact-trust',type=float,default=1.)
    parser.add_argument('--compact-size-factors',type=float,nargs='+',default=[.98,1.,1.02])
    parser.add_argument('--compact-baseline-only',action='store_true')
    parser.add_argument('--compact-cache-only',action='store_true')
    parser.add_argument('--compact-geometry-cache',type=Path)
    options,remaining=parser.parse_known_args()
    response=read(options.compact_response)
    if not response.get('finished') or response.get('new_solution'):
        raise ValueError('Complete actual same-state responses are required')
    names=options.compact_controls.split(',')
    if len(set(names))!=len(names) or any(name not in CONTROL for name in names):
        raise ValueError('Distinct declared controls are required')
    rows=response_directions(response,names)
    import strong_actual_warm_screen as warm
    import strong_20261114_loop_actual_bvp as entry
    original,old_argv=warm.inspect_warm,sys.argv
    completed=False

    def screen(obj,x,y,p,baseline_H,**unused):
        nonlocal completed
        begin=time.monotonic();baseline_cfg=dict(obj.cfg)
        baseline_port,baseline_bridge=obj.port,obj.bridge
        baseline_core=obj.actual_coefficients(p)
        if (baseline_core.tolist()!=response['baseline']['core'] or baseline_cfg!=response['baseline']['profile']
                or obj.q!=response['baseline']['gauge'] or len(x)!=response['nodes']):
            raise ValueError('The compact screen is not at the exact response baseline')
        knots=np.asarray(obj._neck_knots)
        # Include the actually measured A loop-turn curvature witness.
        # Its physical s is converted using this unchanged baseline chart.
        critical_s=np.asarray([2.6336433085309867])
        critical_t=obj.inverse_chart(critical_s,0.)
        grid=np.unique(np.r_[np.linspace(0,1,121),critical_t,
            *[np.linspace(a,b,7) for a,b in zip(knots[:-1],knots[1:])]])
        # These are newly chosen design samples, not stored raw knots.
        grid=grid[np.r_[True,np.diff(grid)>1e-12]];grid[-1]=1.
        record=dict(scope=__doc__,finished=False,new_solution=False,response=str(options.compact_response),
            response_sha256=sha(options.compact_response),source_sha256=sha(__file__),
            controls=names,control_units=CONTROL,grid=grid.tolist(),angular=options.compact_angular,
            complete_raw_nodes=len(x),all_modes=obj.M,production_mean_height_derivatives=True,
            baseline_critical_physical_s=critical_s.tolist(),
            full_raw_cell_height_quadrature=False,continuous_geometry_certificate=False)
        options.compact_out.parent.mkdir(parents=True,exist_ok=True)
        def save():options.compact_out.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
        def state(steps):
            cfg=dict(baseline_cfg);yy=y.copy();pp=p.copy();core=baseline_core.copy()
            for name,weight in steps.items():
                direction=rows[name]['vector'];row=rows[name]['row']
                yy+=weight*direction[:y.size].reshape(y.shape,order='F')
                pp[:obj.M]+=weight*direction[y.size:]
                core+=weight*np.asarray(row['core_derivative'])
                for field,value in row['physical_profile_derivative'].items():
                    if field in PRIMARY:pp[obj.M+PRIMARY.index(field)]+=weight*value
                    else:cfg[field]=cfg.get(field,0.)+weight*value
            obj.cfg=cfg;obj.port,obj.bridge=rebuild(cfg,baseline_port,baseline_bridge)
            obj._flow=obj._flow_key=obj._core_key=obj._initial=None
            obj._augmented_initial_geometry_key=None
            pp[0]=math.log(core[0]/obj.q)
            pp[1]=(core[1]-obj.ref_coeff[1])/obj.pscale[0]
            pp[2]=core[2]/obj.pscale[1]
            obj.select(pp);flow=obj.flow();s,_=obj.chart(x,0.)
            correction=obj.initial(pp)-yy[:,0]
            yy+=correction[:,None]*np.maximum(0.,1-s/(flow.Tu/2))[None,:]**3
            return yy,pp
        base,summary=geometry(obj,x,y,p,grid,options.compact_angular)
        record['baseline']=summary;record['directional_checks']=[];save()
        print(json.dumps(dict(event='compact_geometry_baseline',**summary)),flush=True)
        if options.compact_baseline_only:
            record.update(finished=True,seconds=time.monotonic()-begin);save();completed=True
            return dict(finite_domain_passed=True,compact_screen=str(options.compact_out),nonlinear_solution=False)
        slopes=np.empty((*base.shape,len(names)))
        for column,name in enumerate(names):
            width,scale=CONTROL[name]
            identity=dict(source_sha256=sha(__file__),grid=grid.tolist(),angular=options.compact_angular,
                baseline_profile=baseline_cfg,baseline_core=baseline_core.tolist(),gauge=obj.q,
                direction_array_sha256=rows[name]['source']['sha256'],
                direction_row=rows[name]['row'],width=width,scale=scale)
            cache_key=hashlib.sha256(json.dumps(identity,sort_keys=True,separators=(',',':')).encode()).hexdigest()
            cached=None
            if options.compact_geometry_cache:
                options.compact_geometry_cache.mkdir(parents=True,exist_ok=True)
                cache_path=options.compact_geometry_cache/(name+'-'+cache_key+'.json')
                array_path=cache_path.with_suffix('.npy.gz')
                if cache_path.exists():
                    cached=read(cache_path)
                    if cached['identity']!=identity or sha(array_path)!=cached['array_sha256']:
                        raise ValueError('A compact directional cache changed')
                    with gzip.open(array_path,'rb') as stream:slopes[:,:,:,column]=np.load(stream,allow_pickle=False)
                    record['directional_checks'].append(cached['summary'])
                    save();print(json.dumps(dict(event='compact_geometry_direction_reused',name=name)),flush=True)
                    continue
            yy,pp=state({name:width});plus,ps=geometry(obj,x,yy,pp,grid,options.compact_angular)
            yy,pp=state({name:-width});minus,ms=geometry(obj,x,yy,pp,grid,options.compact_angular)
            slopes[:,:,:,column]=(plus-minus)*scale/(2*width)
            summary=dict(name=name,width=width,scale=scale,plus=ps,minus=ms,
                observed_second_difference=np.max(abs(plus+minus-2*base),axis=(0,1)).tolist())
            record['directional_checks'].append(summary)
            if options.compact_geometry_cache:
                stream=io.BytesIO();np.save(stream,slopes[:,:,:,column],allow_pickle=False)
                array_path.write_bytes(gzip.compress(stream.getvalue(),mtime=0))
                cache_path.write_text(json.dumps(dict(identity=identity,summary=summary,
                    array_sha256=sha(array_path)),indent=2)+'\n')
            save();print(json.dumps(dict(event='compact_geometry_direction',name=name,seconds=time.monotonic()-begin)),flush=True)
        if options.compact_cache_only:
            state({})
            record.update(finished=True,seconds=time.monotonic()-begin,design_cache_only=True);save();completed=True
            return dict(finite_domain_passed=True,compact_screen=str(options.compact_out),nonlinear_solution=False)
        selected=np.unique(np.r_[np.arange(0,len(x),max(1,len(x)//80)),len(x)-1]).astype(int)
        sampled=np.column_stack([obj.q*rows[name]['vector'][:y.size].reshape(y.shape,order='F')[:,selected].ravel()*CONTROL[name][1] for name in names])
        record['predictions']=optimize(base,slopes,rows,names,baseline_core,baseline_cfg,sampled,options.compact_size_factors,options.compact_trust)
        record['combined_warm_geometry']=[];save()
        viable=[row for row in record['predictions'] if row['success']]
        for candidate in sorted(viable,key=lambda row:row['predicted_gap']/row['predicted_size'],reverse=True)[:2]:
            for factor in (1.,.5):
                steps={name:factor*value for name,value in candidate['physical_steps'].items()}
                try:
                    yy,pp=state(steps);_,summary=geometry(obj,x,yy,pp,grid,options.compact_angular)
                    item=dict(factor=factor,steps=steps,summary=summary,finite_domain_passed=True)
                except (ValueError,FloatingPointError) as error:
                    item=dict(factor=factor,steps=steps,finite_domain_passed=False,error=repr(error))
                record['combined_warm_geometry'].append(item);save()
        state({})
        record.update(finished=True,seconds=time.monotonic()-begin);save();completed=True
        return dict(finite_domain_passed=True,compact_screen=str(options.compact_out),nonlinear_solution=False)
    warm.inspect_warm=screen;sys.argv=[old_argv[0],*remaining]
    try:entry.main()
    finally:warm.inspect_warm,sys.argv=original,old_argv
    if not completed:raise RuntimeError('The compact geometry screen did not finish')


if __name__=='__main__':main()
