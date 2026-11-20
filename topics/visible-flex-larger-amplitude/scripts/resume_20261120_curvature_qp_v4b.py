#!/usr/bin/env python3
"""Same-metric weighted Gram QP with arbitrary physical geometry witnesses.

The original Gauss/legacy metric rows are unchanged. Extra points are
geometry-only evaluations of the actual quintic field and analytic lift.
They are necessary screens, never a continuous reach certificate.
The general halfspace repair below also handles negative linear bounds.
Known curvature basins are permanent priority seeds. Every direction keeps
all its actual arbitrary constraint points throughout its entire line search.
"""
import argparse
from collections import OrderedDict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import MethodType

import numpy as np
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import minimize


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    name = 'arbitrary_curvature_dependency_' + sha(path)[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def point_key(point):
    return (int(point[0]), min(1.,max(0.,round(float(point[1]),12))),
            min(float(np.pi/2),max(0.,round(float(point[2]),12))))


class ArbitraryField:
    """Original dense synthesis at one freely chosen (cell,u,phi)."""

    def __init__(self, dense_source, observed, data):
        dense = load(dense_source)
        self.weights = observed.hermite_weights
        self.o = dense.ClosedGram(data['mesh'], data['a_stages'],
            float(data['radius']), data['fixed_core_first3'],
            M=(data['qjets'].shape[-1]-2)//3, N=2, width=float(data['width']))
        self.o.N = 1

    def set_state(self, x):
        self.jets, self.height, self.core = self.o.unpack(x)

    def fields(self, point):
        cell, u, phi = int(point[0]), float(point[1]), float(point[2])
        o = self.o
        if not (0 <= cell < o.J-1 and 0 <= u <= 1 and 0 <= phi <= np.pi/2):
            raise ValueError('Arbitrary witness outside the actual cell/quarter domain')
        h = o.mesh[cell+1]-o.mesh[cell]
        s = o.mesh[cell]+h*u
        y, v, acc = self.weights(h, u)@self.jets[cell:cell+2].reshape(6, o.n)
        o.cos = np.r_[1., np.cos(phi*o.freq)][None]
        o.sin = np.sin(phi*o.freq)[None]
        rho = 1.+o.cos[:, 1:]@(o.qfreq*self.core)
        rho_phi = -o.sin@(o.freq*o.qfreq*self.core)
        delta = o.sin@((o.qfreq/o.freq)*self.core)
        er = np.array([[np.cos(delta[0]), np.sin(delta[0]), 0.]])
        et = np.array([[-np.sin(delta[0]), np.cos(delta[0]), 0.]])
        chi, cp, cpp, f, fp, fpp = o._lift_scalar(float(s))
        F = o.synth(y)+f*er
        Fs = o.synth(v)+fp*er
        Fss = o.synth(acc)+fpp*er
        F[:, 2] += chi*self.height
        Fs[:, 2] += cp*self.height
        Fss[:, 2] += cpp*self.height
        Fphi = o.angular(y)+f*rho[:, None]*et
        Fsphi = o.angular(v)+fp*rho[:, None]*et
        Fphiphi = o.angular(y, order=2)+f*(rho_phi[:, None]*et-rho[:, None]**2*er)
        return {name:value[0] for name,value in dict(F=F, Fs=Fs,
            Fphi=Fphi, Fss=Fss, Fsphi=Fsphi, Fphiphi=Fphiphi).items()}

    def read(self, point):
        z = self.fields(point)
        V, d = z['Fs'], z['Fphi']
        cross = np.cross(V, d)
        area = float(np.linalg.norm(cross))
        if not np.isfinite(area) or area <= 0:
            return dict(point=list(point), complete=False, area=area,
                        maximum_absolute_principal_curvature=float('inf'),
                        diameter_point_lower=float('inf'))
        n = cross/area
        E, F, G = V@V, V@d, d@d
        e, f, g = n@z['Fss'], n@z['Fsphi'], n@z['Fphiphi']
        trace = (e*G+g*E-2*f*F)/(area*area)
        gauss = (e*g-f*f)/(area*area)
        gap = np.sqrt(max(0., trace*trace-4*gauss))
        kappas = np.array([(trace-gap)/2, (trace+gap)/2])
        cell, u, phi = int(point[0]), float(point[1]), float(point[2])
        return dict(point=[cell,u,phi], complete=bool(np.isfinite(kappas).all()),
            s=float(self.o.mesh[cell]+np.diff(self.o.mesh)[cell]*u),
            principal_curvatures=kappas.tolist(),
            maximum_absolute_principal_curvature=float(np.max(np.abs(kappas))),
            diameter_point_lower=float(2*np.linalg.norm(z['F'])), area=area)


def stage_point(o, stage, angle):
    return (int(o.observation_cells[stage]), float(o.observation_u[stage]), float(o.phi[angle]))


class ArbitraryCoarseGeometry:
    """Exact restriction of all current coarse columns to an arbitrary point."""

    def __init__(self, field, basis):
        self.field, self.b = field, basis

    def row(self, point, cotangent):
        b, field = self.b, self.field
        cell, u, phi = int(point[0]), float(point[1]), float(point[2])
        o = field.o
        hcell = o.mesh[cell+1]-o.mesh[cell]
        radial = field.weights(hcell, u)@b.node_jets[:, cell:cell+2, :].reshape(b.nb,6).T
        radial[:, b.height_radial] += np.asarray(
            o._lift_scalar(float(o.mesh[cell]+hcell*u))[:3])
        h, dh, d2h = (np.zeros((b.nc,3)) for _ in range(3))
        for j, (kind, m, _) in enumerate(b.channels):
            nu = 2*m
            co, si = np.cos(nu*phi), np.sin(nu*phi)
            if kind == 'R':
                h[j] = (co, 0, 0)
                dh[j] = (-nu*si, co, 0)
                d2h[j] = (-(nu*nu+1)*co, -2*nu*si, 0)
            elif kind == 'T':
                h[j] = (0, si, 0)
                dh[j] = (-si, nu*co, 0)
                d2h[j] = (-2*nu*co, -(nu*nu+1)*si, 0)
            else:
                h[j] = (0, 0, co)
                dh[j] = (0, 0, -nu*si)
                d2h[j] = (0, 0, -nu*nu*co)
        ri, cj = b.pairs.T
        aa = h@cotangent['Fss']
        uu = h@cotangent['Fs']+dh@cotangent['Fsphi']
        yy = h@cotangent['F']+dh@cotangent['Fphi']+d2h@cotangent['Fphiphi']
        return radial[2,ri]*aa[cj]+radial[1,ri]*uu[cj]+radial[0,ri]*yy[cj]


class LocalMemory:
    def __init__(self, curvature_capacity=12, radius_capacity=2):
        self.curvature_capacity, self.radius_capacity = curvature_capacity, radius_capacity
        self.curvature, self.radius = OrderedDict(), OrderedDict()
        self.protected = OrderedDict()

    def protect(self, point):
        self.protected[point_key(point)] = None

    def put(self, which, point):
        target = getattr(self, which)
        capacity = getattr(self, which+'_capacity')
        key = point_key(point)
        # Replace only a very nearby witness of the same basin. Both branches
        # are still evaluated afresh; no curvature values are remembered.
        for old in list(target):
            if old[0] == key[0] and abs(old[1]-key[1]) < .002 and abs(old[2]-key[2]) < .002:
                del target[old]
        target[key] = None
        while len(target) > capacity:
            target.popitem(last=False)

    def observe(self, report):
        for item in reversed(report.get('curvature_witnesses', [])):
            self.put('curvature', item['point'])
        for item in reversed(report.get('radius_witnesses', [])):
            self.put('radius', item['point'])

    def restore(self, path):
        value = json.loads(Path(path).read_text())
        for point in value.get('protected_curvature_points', []):
            self.protect(point)
        for key in ('curvature','radius'):
            for point in value.get(key+'_points', []):
                self.put(key, point)

    def state(self):
        return dict(schema='arbitrary-physical-witness-memory-v1',
            curvature_capacity=self.curvature_capacity, radius_capacity=self.radius_capacity,
            curvature_points=list(self.curvature), radius_points=list(self.radius),
            protected_curvature_points=list(self.protected),
            scope='Geometry-only locations; both current principal branches are always reread')


def scan_local(field, o, x, grid, curvatures, radii, memory, *, refine=4, reach_ratio=.03,
               pinned_curvature=(), pinned_radius=()):
    field.set_state(x)
    cpoints = list(memory.protected)+list(memory.curvature)+list(pinned_curvature)+[stage_point(o,*v[:2]) for v in curvatures[:12]]
    rpoints = list(memory.radius)+list(pinned_radius)+[stage_point(o,*v) for v in radii[:2]]
    cpoints = list(dict.fromkeys(point_key(v) for v in cpoints))
    rpoints = list(dict.fromkeys(point_key(v) for v in rpoints))
    creads = [field.read(point) for point in cpoints]
    rreads = [field.read(point) for point in rpoints]
    evaluations = []
    if not all(v['complete'] for v in creads+rreads):
        return dict(complete=False, necessary_reach_product=float('inf'),
                    curvature_witnesses=creads, radius_witnesses=rreads)
    starts = sorted(creads, key=lambda v:v['maximum_absolute_principal_curvature'], reverse=True)
    selected = [list(p) for p in memory.protected] if refine > 0 else []
    if refine > 0 and len(selected) > refine:
        raise ValueError('local-refine must include every protected basin')
    for item in starts:
        if len(selected) >= refine:
            break
        p = item['point']
        if any(p[0] == q[0] and abs(p[1]-q[1]) < .10 and abs(p[2]-q[2]) < .10 for q in selected):
            continue
        selected.append(p)
        if len(selected) >= refine:
            break
    if refine <= 0:
        selected = []
    for point in selected:
        cell = point[0]
        objective = lambda uv: -field.read((cell,uv[0],uv[1]))['maximum_absolute_principal_curvature']
        result = minimize(objective, point[1:], method='Nelder-Mead',
            bounds=((0.,1.),(0.,np.pi/2)),
            options=dict(xatol=2.e-9, fatol=2.e-9, maxiter=180))
        final = field.read((cell,*result.x))
        creads.append(final)
        evaluations.append(dict(kind='curvature', start=point, final=final,
            success=bool(result.success), iterations=int(result.nit), evaluations=int(result.nfev)))
    if refine > 0 and rreads:
        seed = max(rreads, key=lambda v:v['diameter_point_lower'])['point']
        cell = seed[0]
        result = minimize(lambda uv:-field.read((cell,uv[0],uv[1]))['diameter_point_lower'],
            seed[1:], method='Nelder-Mead', bounds=((0.,1.),(0.,np.pi/2)),
            options=dict(xatol=2.e-9, fatol=2.e-9, maxiter=180))
        final = field.read((cell,*result.x))
        rreads.append(final)
        evaluations.append(dict(kind='diameter', start=seed, final=final,
            success=bool(result.success), iterations=int(result.nit), evaluations=int(result.nfev)))
    def selected_witnesses(reads, key, limit):
        selected = []
        for item in sorted(reads,key=lambda v:v[key],reverse=True):
            p = item['point']
            if any(p[0] == old['point'][0] and abs(p[1]-old['point'][1]) < .002
                   and abs(p[2]-old['point'][2]) < .002 for old in selected):
                continue
            selected.append(item)
            if len(selected) == limit:
                break
        return selected
    best_c = max(creads,key=lambda v:v['maximum_absolute_principal_curvature'])
    best_r = max(creads+rreads,key=lambda v:v['diameter_point_lower'])
    K = max(grid['maximum_absolute_principal_curvature'], best_c['maximum_absolute_principal_curvature'])
    D = max(grid['diameter_point_lower'], best_r['diameter_point_lower'])
    return dict(complete=all(v['complete'] for v in creads+rreads),
        maximum_absolute_principal_curvature=K, diameter_point_lower=D,
        necessary_reach_product=reach_ratio*K*D,
        best_arbitrary_curvature=best_c, best_arbitrary_diameter=best_r,
        curvature_witnesses=selected_witnesses(creads,'maximum_absolute_principal_curvature',min(6,memory.curvature_capacity)),
        radius_witnesses=selected_witnesses(creads+rreads,'diameter_point_lower',memory.radius_capacity),
        local_searches=evaluations, tested_fixed_points=len(cpoints)+len(rpoints),
        continuous_geometry_certified=False, local_optimizer_is_global_bound=False)


def all_constraints(base, grid_geometry, local_geometry, o, x, cpoints, rpoints,
                    local_memory, reach_ratio, linear_safety):
    b, field = local_geometry.b, local_geometry.field
    p = o.prepare(x)
    field.set_state(x)
    curves, diameters = [], []
    grid_c = set()
    for stage, angle, branch in cpoints:
        z = base.single_fields(o,p,stage,angle)
        k, cot, meta = base.curvature_cotangent(z,branch)
        curves.append((k,grid_geometry.row(stage,angle,cot),dict(kind='grid',stage=stage,angle=angle,branch=branch),meta))
        grid_c.add((point_key(stage_point(o,stage,angle)),branch))
    for point in dict.fromkeys(list(local_memory.protected)+list(local_memory.curvature)):
        z = field.fields(point)
        for branch in (0,1):
            if (point_key(point),branch) in grid_c:
                continue
            k,cot,meta = base.curvature_cotangent(z,branch)
            curves.append((k,local_geometry.row(point,cot),dict(kind='arbitrary',point=point,branch=branch),meta))
    grid_r = set()
    for stage,angle in rpoints:
        z = base.single_fields(o,p,stage,angle)
        radius = float(np.linalg.norm(z['F']))
        cot = {name:np.zeros(3) for name in z}
        cot['F'] = 2*z['F']/radius
        diameters.append((2*radius,grid_geometry.row(stage,angle,cot),dict(kind='grid',stage=stage,angle=angle)))
        grid_r.add(point_key(stage_point(o,stage,angle)))
    for point in local_memory.radius:
        if point_key(point) in grid_r:
            continue
        z = field.fields(point)
        radius = float(np.linalg.norm(z['F']))
        cot = {name:np.zeros(3) for name in z}
        cot['F'] = 2*z['F']/radius
        diameters.append((2*radius,local_geometry.row(point,cot),dict(kind='arbitrary',point=point)))
    diameters.append((2.,np.zeros(b.dimension),dict(kind='fixed_core')))
    height_row = np.zeros(b.dimension); height_row[-1]=2*np.sign(float(p.height))
    diameters.append((2*abs(float(p.height)),height_row,dict(kind='cap_height')))
    rows, bounds, metadata = [], [], []
    for k,dk,loc,meta in curves:
        for D,dD,dloc in diameters:
            rows.append(reach_ratio*(D*np.sign(k)*dk+abs(k)*dD))
            bounds.append(linear_safety-reach_ratio*D*abs(k))
            metadata.append(dict(curvature_point=loc,diameter_point=dloc,curvature=k,diameter_lower=D,**meta))
    return np.asarray(rows), np.asarray(bounds), metadata


def general_direction(normal, gradient, Q, bounds, damping, *, repair_iterations=40000):
    """Approximate convex QP then general A-orthogonal halfspace repair.

    Unlike contraction to zero, this repair never assumes b >= 0.
    Every repair projection is z <- z - A^-1 r_i * violation/(r_i A^-1 r_i).
    A successful numerical repair is checked in the original unscaled rows.
    The nonlinear acceptance is independent and stricter.
    """
    scale = np.sqrt(np.maximum(np.diag(normal),np.max(np.diag(normal))*1.e-28))
    C = normal/scale[:,None]/scale[None,:]+damping*np.eye(len(scale))
    factor = cho_factor(C,lower=True,check_finite=False)
    z0 = cho_solve(factor,-gradient/scale,check_finite=False)
    rawrows = Q/scale[None,:]
    rownorm = np.linalg.norm(rawrows,axis=1)
    if np.any((rownorm <= 1.e-30)&(bounds < -1.e-12)):
        return None,dict(feasible=False,reason='infeasible_constant_row',damping=damping)
    keep = rownorm > 1.e-30
    rows, rhs = rawrows[keep]/rownorm[keep,None], bounds[keep]/rownorm[keep]
    inverse_rows = cho_solve(factor,rows.T,check_finite=False)
    G = rows@inverse_rows
    G = (G+G.T)/2
    d = rhs-rows@z0
    def objective(lam):
        v=G@lam
        return float(.5*lam@v+d@lam),v+d
    result=minimize(objective,np.zeros(len(rhs)),jac=True,method='L-BFGS-B',
        bounds=[(0.,None)]*len(rhs),
        options=dict(maxiter=1800,ftol=1.e-14,gtol=1.e-10,maxls=50))
    lam=result.x.copy()
    z=z0-inverse_rows@lam
    violation=rows@z-rhs
    before=float(np.max(violation)) if len(rhs) else 0.
    # An explicit tiny inward margin allows a final unscaled check.
    margin=2.e-10
    repairs=0
    for repairs in range(repair_iterations):
        i=int(np.argmax(violation))
        if violation[i] <= -margin:
            break
        if not np.isfinite(G[i,i]) or G[i,i] <= 0:
            break
        delta=(violation[i]+2*margin)/G[i,i]
        lam[i]+=delta
        violation-=delta*G[:,i]
    z=z0-inverse_rows@lam
    direction=z/scale
    true_violation=float(np.max(Q@direction-bounds))
    feasible=bool(np.isfinite(direction).all() and true_violation <= 2.e-8)
    return direction,dict(feasible=feasible,dual_success=bool(result.success),
        dual_message=str(result.message),dual_iterations=int(result.nit),
        constraints=len(bounds),negative_bounds=int(np.sum(bounds<0)),
        nonzero_dual=int(np.sum(lam>1.e-9)),
        scaled_max_violation_before_repair=before,projection_repairs=repairs,
        maximum_primal_violation=true_violation,
        original_gradient_dot_direction=float(gradient@direction),
        step_norm=float(np.linalg.norm(direction)),damping=damping,
        repair='A-orthogonal halfspace projections; no feasible-zero assumption')


def arbitrary_probe(base, field, geometry, basis, x, point):
    field.set_state(x)
    z=field.fields(point)
    branch=int(np.argmax(np.abs([base.analytic_kappa(z,k) for k in (0,1)])))
    k,cot,meta=base.curvature_cotangent(z,branch)
    if meta['principal_gap'] <= 1.e-8:
        raise ValueError('Arbitrary-point probe needs a simple branch')
    rng=np.random.default_rng(20261120)
    coefficients=rng.normal(size=basis.dimension)
    free=basis.free_direction(coefficients)
    predicted=geometry.row(point,cot)@coefficients
    step=1.e-25
    field.set_state(x.astype(complex)+1j*step*free)
    zc=field.fields(point)
    cs=base.analytic_kappa(zc,branch).imag/step
    kerr=abs(cs-predicted)/max(1.,abs(cs),abs(predicted))
    cotD={name:np.zeros(3) for name in z}
    cotD['F']=2*z['F']/np.linalg.norm(z['F'])
    predD=geometry.row(point,cotD)@coefficients
    csD=(2*np.sqrt(zc['F']@zc['F'])).imag/step
    derr=abs(csD-predD)/max(1.,abs(csD),abs(predD))
    field.set_state(x)
    value=dict(point=list(point),branch=branch,kappa=float(k),
        complex_step=step,coarse_kappa_relative_error=float(kerr),
        coarse_diameter_relative_error=float(derr),**meta)
    if max(kerr,derr)>2.e-9:
        raise ValueError('Arbitrary geometry derivative mismatch: '+repr(value))
    return value


def update_damping(damping, accepted, alpha, ratio):
    if not accepted:
        return damping*10,'rejected_x10'
    if alpha < .25:
        return damping*4,'small_accepted_step_x4'
    if ratio is None or ratio < .25:
        return damping*4,'poor_model_ratio_x4'
    if alpha == 1. and ratio > .75:
        return max(damping/2,1.e-8),'good_full_step_half'
    return damping,'intermediate_step_hold'


def main(args):
    started=time.monotonic()
    if args.out.exists() or args.out.with_suffix('.npz').exists():
        raise FileExistsError('Use a fresh output')
    gauss,base,memory_module=load(args.gauss_source),load(args.qp_source),load(args.memory_source)
    batch,observed,coarse=load(args.batch_source),load(args.observed_source),load(args.coarse_source)
    data=np.load(args.bundle,allow_pickle=False)
    carrier=np.load(args.carrier,allow_pickle=False)
    plan=observed.ObservationPlan.from_arrays(carrier)
    common=dict(M=(data['qjets'].shape[-1]-2)//3,N=args.angles,width=float(data['width']),
                quarter=True,stage_block=args.stage_block)
    inputs=(data['mesh'],data['a_stages'],float(data['radius']),data['fixed_core_first3'])
    native=batch.create(args.operator,*inputs,**common)
    o=observed.create(args.operator,*inputs,batch_source=batch,observation_plan=plan,
        a_observations=carrier['a_observations'],**common)
    x,affine=o.pack(data['qjets'],float(data['Hcap']),require_affine=True)
    original_core=x[:o.M-o.K].copy()
    basis=coarse.make_space(args.base_source,native,low_modes=args.low_modes,
        desired_centers=[float(v) for v in args.centers.split(',')])
    basis,geometry=gauss.retarget_basis(o,basis,base.CoarseGeometry(native,basis))
    radial_weights=o.mixed_stage_weights(args.legacy_fraction)
    if not np.all(radial_weights>0):
        raise ValueError('Every metric row must keep a positive radial weight')
    basis.radial_weights=radial_weights
    basis.evaluate=MethodType(gauss.weighted_evaluate,basis)
    base.fields_block=gauss.fields_block_observed
    memory=memory_module.ActiveMemory(args.memory_curvature,args.memory_radius)
    if args.memory_input is not None:
        payload=json.loads(args.memory_input.read_text())
        if payload.get('observation_carrier_sha256') != sha(args.carrier):
            raise ValueError('Grid memory must be bound to this exact observation carrier')
        memory.restore(args.memory_input)
    local=LocalMemory(args.local_curvature,args.local_radius)
    if args.local_memory_input is not None:
        payload=json.loads(args.local_memory_input.read_text())
        if payload.get('observation_carrier_sha256') != sha(args.carrier):
            raise ValueError('Arbitrary memory must be bound to this same mesh/carrier')
        local.restore(args.local_memory_input)
    field=ArbitraryField(args.operator,observed,data)
    field.set_state(x)
    local_geometry=ArbitraryCoarseGeometry(field,basis)
    witness_checks=[]
    for value in args.protected_point:
        pieces=value.split(',')
        if len(pieces)!=3:
            raise ValueError('protected-point requires cell,u,phi')
        local.protect((int(pieces[0]),float(pieces[1]),float(pieces[2])))
    for path in args.witness_input:
        witness=json.loads(path.read_text())
        point=witness['final']
        loc=(point['cell'],point['u'],point['phi'])
        local.put('curvature',loc)
        local.protect(loc)
        if witness['bundle_sha256']==sha(args.bundle):
            read=field.read(loc)
            err=abs(read['maximum_absolute_principal_curvature']-point['maximum_absolute_principal_curvature'])
            if err>2.e-9:
                raise ValueError('Actual arbitrary witness disagrees with reference')
            witness_checks.append(dict(path=str(path),sha256=sha(path),absolute_kappa_difference=err))
    def grid_memory_state():
        value=memory.state()
        value.update(observation_carrier_sha256=sha(args.carrier),full_angles=o.full_N,
                     legacy_stages=o.legacy_P,total_stages=o.P)
        return value
    def local_memory_state():
        value=local.state()
        value.update(observation_carrier_sha256=sha(args.carrier))
        return value
    initial_memory=dict(grid=grid_memory_state(),arbitrary=local_memory_state())
    o.set_base(x)
    grid,curvatures,radii=base.scan_geometry(o,x,top_curvature=args.top_curvature,top_radius=args.top_radius)
    if not grid['complete']:
        raise ValueError('Input geometry invalid')
    current_local=scan_local(field,o,x,grid,curvatures,radii,local,refine=args.local_refine,reach_ratio=args.reach_ratio)
    local.observe(current_local)
    probe=arbitrary_probe(base,field,local_geometry,basis,x,current_local['best_arbitrary_curvature']['point'])
    initial=state=gauss.observed_stats(o,x,radial_weights)
    initial_grid,initial_local=grid,current_local
    initial_restoration=current_local['necessary_reach_product']>args.safety
    args.out.with_suffix('.initial.json').write_text(json.dumps(dict(
        source_sha256=sha(__file__),input_sha256=sha(args.bundle),initial=initial,
        gauss_geometry=initial_grid,arbitrary_geometry=initial_local,
        arbitrary_derivative_probe=probe,witness_reference_checks=witness_checks),indent=2)+'\n')
    records=[]; damping=args.damping; status='iteration_budget'; restoration_failures=0
    initial_mapping_check=None
    for iteration in range(args.steps):
        if time.monotonic()-started>args.seconds:
            status='time_budget'; break
        # Rejected trials may teach locations that expose a new witness in
        # the unchanged parent as well. Reread those current values now.
        current_local=scan_local(field,o,x,grid,curvatures,radii,local,
            refine=args.local_refine,reach_ratio=args.reach_ratio)
        local.observe(current_local)
        o.set_base(x)
        linear=basis.evaluate(o._base_first,o._base_p.rho,np.zeros(basis.dimension),linearize=True)
        difference=abs(linear['weighted_sse']-state['weighted_sse'])/max(1.,state['weighted_sse'])
        if difference>2.e-10:
            raise ValueError('Weighted metric basis mapping mismatch')
        if initial_mapping_check is None:
            initial_mapping_check=difference
        cpoints,rpoints=memory.combine(curvatures,radii,o)
        Q,bounds,active=all_constraints(base,geometry,local_geometry,o,x,cpoints,rpoints,
            local,args.reach_ratio,args.safety-args.linear_margin)
        pinned_curvature=tuple(dict.fromkeys(list(local.protected)+list(local.curvature)))
        pinned_radius=tuple(local.radius)
        direction,qp=general_direction(linear['normal_matrix'],linear['gradient'],Q,bounds,damping,
            repair_iterations=args.repair_iterations)
        record=dict(iteration=iteration,before=state,gauss_geometry_before=grid,
            arbitrary_geometry_before=current_local,qp=qp,active_constraints=active,
            pinned_curvature_points=pinned_curvature,pinned_radius_points=pinned_radius,
            memory_before=dict(grid=grid_memory_state(),arbitrary=local_memory_state()),trials=[])
        accepted=False; accepted_alpha=None; accepted_ratio=None
        if direction is not None and qp['feasible']:
            free=basis.free_direction(direction)
            gp=float(linear['gradient']@direction)
            pp=float(direction@(linear['normal_matrix']@direction))
            record['model']=dict(gradient_dot_direction=gp,GN_quadratic=pp,
                definition='predicted data-SSE decrease = -2 alpha g.p - alpha^2 p.GN.p; LM penalty excluded')
            for backtrack in range(args.backtracks):
                alpha=2.**(-backtrack)
                predicted=-2*alpha*gp-alpha*alpha*pp
                candidate=x+alpha*free
                trial=gauss.observed_stats(o,candidate,radial_weights)
                actual=state['weighted_sse']-trial['weighted_sse']
                ratio=actual/predicted if predicted>0 else None
                item=dict(alpha=alpha,statistics=trial,predicted_decrease=predicted,
                          actual_decrease=actual,model_ratio=ratio,accepted=False)
                if np.isfinite(trial['weighted_sse']) and actual>0 and trial['min_determinant']>0:
                    checked,cnext,rnext=base.scan_geometry(o,candidate,
                        top_curvature=args.top_curvature,top_radius=args.top_radius)
                    item['gauss_geometry']=checked
                    grid_pass=checked['complete'] and args.reach_ratio*checked['diameter_point_lower']*checked['maximum_absolute_principal_curvature']<=args.safety
                    if checked['complete']:
                        checked_local=scan_local(field,o,candidate,checked,cnext,rnext,local,
                            refine=args.local_refine if grid_pass else 0,reach_ratio=args.reach_ratio,
                            pinned_curvature=pinned_curvature,pinned_radius=pinned_radius)
                        item['arbitrary_geometry']=checked_local
                        if grid_pass and checked_local['complete'] and checked_local['necessary_reach_product']<=args.safety:
                            x,state,grid,current_local=candidate,trial,checked,checked_local
                            curvatures,radii=cnext,rnext
                            local.observe(checked_local)
                            item['accepted']=True
                            accepted=True; accepted_alpha=alpha; accepted_ratio=ratio
                            # Keep each actual accepted field reviewable. Rejected
                            # trial memory cannot erase or mutate this checkpoint.
                            cj,ch,_=o.unpack(x)
                            ck=('mesh','a_stages','radius','width','fixed_core_first3',
                                'a_stage_absolute_error','stage_time_absolute_error')
                            ca={key:np.array(data[key],copy=True) for key in ck if key in data.files}
                            ca.update(qjets=cj,Hcap=np.asarray(ch))
                            cp=args.out.with_name(args.out.stem+f'.accepted-{iteration+1}.npz')
                            np.savez_compressed(cp,**ca)
                            item['accepted_bundle_path']=str(cp)
                            item['accepted_bundle_sha256']=sha(cp)
                        else:
                            memory.observe(checked)
                            local.observe(checked_local)
                    else:
                        item['rejection']='invalid_gauss_geometry'
                else:
                    item['rejection']='no_true_SSE_descent_or_nonpositive_metric'
                record['trials'].append(item)
                if accepted:
                    break
        else:
            record['direction_rejected']='linear_halfspace_repair_not_feasible'
        damping,reason=update_damping(damping,accepted,accepted_alpha,accepted_ratio)
        record.update(accepted=accepted,damping_after=damping,damping_reason=reason,
            memory_after=dict(grid=grid_memory_state(),arbitrary=local_memory_state()),
            elapsed_seconds=time.monotonic()-started)
        records.append(record)
        print(json.dumps({k:v for k,v in record.items() if k!='active_constraints'}),flush=True)
        args.out.with_suffix('.memory.json').write_text(json.dumps(grid_memory_state(),indent=2)+'\n')
        args.out.with_suffix('.local-memory.json').write_text(json.dumps(local_memory_state(),indent=2)+'\n')
        args.out.with_suffix('.progress.json').write_text(json.dumps(dict(
            source_sha256=sha(__file__),input_sha256=sha(args.bundle),initial=initial,
            current=state,gauss_geometry=grid,arbitrary_geometry=current_local,records=records),indent=2)+'\n')
        if not accepted and current_local['necessary_reach_product']>args.safety:
            restoration_failures+=1
            if restoration_failures>=args.restoration_attempts:
                status='restoration_failed'; break
    current_local=scan_local(field,o,x,grid,curvatures,radii,local,
        refine=args.local_refine,reach_ratio=args.reach_ratio)
    local.observe(current_local)
    jets,height,_=o.unpack(x)
    _,final_affine=o.pack(jets,height,require_affine=True)
    if not np.array_equal(x[:o.M-o.K],original_core):
        raise ValueError('Core shape changed')
    keys=('mesh','a_stages','radius','width','fixed_core_first3','a_stage_absolute_error','stage_time_absolute_error')
    arrays={k:np.array(data[k],copy=True) for k in keys if k in data.files}
    arrays.update(qjets=jets,Hcap=np.asarray(height))
    output=args.out.with_suffix('.npz')
    np.savez_compressed(output,**arrays)
    report=dict(schema='fullclosed-coarse-arbitrary-curvature-QP-v4b',status=status,
        source_sha256=sha(__file__),input_sha256=sha(args.bundle),output_bundle_sha256=sha(output),
        dependency_sha256={key:sha(getattr(args,key)) for key in
            ('gauss_source','qp_source','memory_source','operator','batch_source','observed_source',
             'carrier','base_source','coarse_source')},
        initial=initial,final=state,initial_gauss_geometry=initial_grid,final_gauss_geometry=grid,
        initial_arbitrary_geometry=initial_local,final_arbitrary_geometry=current_local,
        initial_restore_required=initial_restoration,
        final_known_point_safety_pass=bool(current_local['complete'] and current_local['necessary_reach_product']<=args.safety),
        initial_height=float(data['Hcap']),final_height=float(height),
        initial_affine=affine,final_affine=final_affine,initial_memory=initial_memory,
        final_memory=dict(grid=grid_memory_state(),arbitrary=local_memory_state()),
        witness_reference_checks=witness_checks,arbitrary_derivative_probe=probe,
        initial_weighted_basis_operator_difference=initial_mapping_check,
        subspace_dimension=basis.dimension,low_modes=args.low_modes,
        centers=[float(o.mesh[i]) for i in basis.center_nodes],full_variables=o.free_size,
        observation_metadata=o.observation_metadata(),all_original_gram_rows_retained=True,
        objective='Same positive radial Simpson/Gauss weighted Gram SSE as v3; arbitrary geometry adds no metric rows',
        radial_weight_sum=float(np.sum(radial_weights)),legacy_fraction=args.legacy_fraction,
        numerical_safety=args.safety,linear_margin=args.linear_margin,reach_ratio=args.reach_ratio,
        local_refine=args.local_refine,initial_damping=args.damping,final_damping=damping,
        iterations=records,elapsed_seconds=time.monotonic()-started,
        fixed_scalar_mesh_and_core_unchanged=True,continuous_metric_certified=False,
        reach_certified=False,held_amplitude_certified=False,exact_solution_claimed=False)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='iterations'}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('bundle','operator','batch-source','base-source','coarse-source','out',
                'gauss-source','qp-source','memory-source','observed-source','carrier'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--memory-input',type=Path)
    p.add_argument('--local-memory-input',type=Path)
    p.add_argument('--witness-input',type=Path,action='append',default=[])
    p.add_argument('--protected-point',action='append',default=[])
    p.add_argument('--legacy-fraction',type=float,default=.5)
    p.add_argument('--memory-curvature',type=int,default=32)
    p.add_argument('--memory-radius',type=int,default=4)
    p.add_argument('--local-curvature',type=int,default=12)
    p.add_argument('--local-radius',type=int,default=2)
    p.add_argument('--local-refine',type=int,default=4)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--stage-block',type=int,default=64)
    p.add_argument('--low-modes',type=int,default=12)
    p.add_argument('--centers',default='.30,.60,.83,1.05,1.20,1.35,1.55,1.75,1.95,2.15,2.26')
    p.add_argument('--top-curvature',type=int,default=32)
    p.add_argument('--top-radius',type=int,default=4)
    p.add_argument('--reach-ratio',type=float,default=.03)
    p.add_argument('--safety',type=float,default=.98)
    p.add_argument('--linear-margin',type=float,default=.0002)
    p.add_argument('--damping',type=float,default=.001)
    p.add_argument('--steps',type=int,default=12)
    p.add_argument('--backtracks',type=int,default=12)
    p.add_argument('--repair-iterations',type=int,default=40000)
    p.add_argument('--restoration-attempts',type=int,default=3)
    p.add_argument('--seconds',type=float,default=1800.)
    main(p.parse_args())



