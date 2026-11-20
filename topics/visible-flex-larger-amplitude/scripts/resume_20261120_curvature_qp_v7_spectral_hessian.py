#!/usr/bin/env python3
"""Same-metric weighted Gram QP with arbitrary physical geometry witnesses.

The original Gauss/legacy metric rows are unchanged. Extra points are
geometry-only evaluations of the actual quintic field and analytic lift.
They are necessary screens, never a continuous reach certificate.
The general halfspace repair below also handles negative linear bounds.
Known curvature basins are permanent priority seeds. Every direction keeps
all its actual arbitrary constraint points throughout its entire line search.
This version uses the published positive physical-height integrated step norm
and immutable geometry-witness manifests. This new version changes the
objective to a fixed-epsilon positive spectral Lp, while retaining every
original Gram row, the fixed metric and all geometric screens.
This version uses the exact positive Hessian with respect to the matrix
residual in its normal model. The true gradient is unchanged; the nonlinear
field Hessian is not claimed to be exact, and actual Phi still decides.
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
from scipy.linalg import cho_factor, cho_solve, solve_triangular
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



def physical_norm(operator, basis, args):
    norm_module=load(args.norm_source)
    coordinate_module=load(args.coordinate_source)
    scale_module=load(args.scale_source)
    height_module=load(args.height_source)
    scale=scale_module.make_scale(operator)
    nc0=operator.M-operator.K;na0=2*operator.M+1
    nai=(operator.J-2)*operator.n;ne=(operator.J-1)*operator.n
    at=nc0+na0+nai+ne
    scale[at:at+ne].reshape(operator.J-1,operator.n)[:]*=np.diff(operator.mesh)[:,None]
    scale[-1]=height_module.height_scale(operator.S)
    coordinates=coordinate_module.DoubleIntegrated(operator,scale=scale)
    height_map=height_module.PhysicalHeight(coordinates,basis)
    d,L,metadata=norm_module.coarse_norm(basis,coordinates,height_map)
    R=solve_triangular(L.T,np.eye(basis.dimension),lower=False,check_finite=False)/d[:,None]
    metadata.update(coordinate_map=height_map.metadata(),
        coefficient_space_whitener='p=R z; R^T G R=I',
        penalty_convention='mean-data normal plus mu^2 I in whitened coordinates',
        exact_bending_energy_claimed=False)
    return R,metadata



def spectral_evaluate(self, base_first, rho, coefficients, *, linearize=False):
    """All original rows; exact positive residual Hessian, true Phi readout.

    The returned normal and half-gradient are both multiplied by k/scale^2.
    Divide both by C0 before adding the physical-H2 step penalty.
    """
    o, spectral, parameters = self.o, self.spectral_module, self.spectral_parameters
    hessian = self.spectral_hessian_module
    c = self.coefficient_matrix(coefficients)
    yu, yy = self.stage_u@c, self.stage_y@c
    normal = np.zeros((self.dimension,self.dimension)) if linearize else None
    gradient = np.zeros(self.dimension) if linearize else None
    cost, raw_cost, loss, maximum, determinant = 0.,0.,0.,0.,float('inf')
    minimum_weight, maximum_weight = float('inf'),0.
    ri,cj = self.pairs.T
    mw = self.multiplicity
    factor = parameters.k/(parameters.scale*parameters.scale)
    for stage,a in enumerate(o.a):
        weight = self.radial_weights[stage]
        V = base_first[0,stage]+np.einsum('c,nck->nk',yu[stage],self.h)
        d = base_first[1,stage]+np.einsum('c,nck->nk',yy[stage],self.dh)
        ar = a*rho
        r0 = np.sum(V*V,axis=1)-1.
        r1 = np.sum(V*d,axis=1)/ar
        r2 = np.sum(d*d,axis=1)/(ar*ar)-1.
        residual = np.stack((r0,r1,r2),axis=-1)
        local = float(mw@(r0*r0+2*r1*r1+r2*r2))
        cost += weight*local
        raw_cost += local
        loss += weight*float(mw@spectral.point_loss(residual,parameters))
        metric_norm = (np.abs(r0+r2)+np.sqrt((r0-r2)**2+4*r1*r1))/2
        maximum = max(maximum,float(np.max(metric_norm)))
        determinant = min(determinant,float(np.min((1+r0)*(1+r2)-r1*r1)))
        if not linearize:
            continue
        blocks = hessian.HessianBlocks(residual,parameters)
        minimum_weight = min(minimum_weight,blocks.minimum_eigenweight)
        maximum_weight = max(maximum_weight,blocks.maximum_eigenweight)
        by,bu = self.stage_y[stage,ri],self.stage_u[stage,ri]
        active = np.flatnonzero((by != 0)|(bu != 0))
        if not active.size:
            continue
        vh = np.einsum('nk,nck->nc',V,self.h)
        dh = np.einsum('nk,nck->nc',d,self.h)
        vdh = np.einsum('nk,nck->nc',V,self.dh)
        ddh = np.einsum('nk,nck->nc',d,self.dh)
        # A: derivative with respect to radial velocity coefficients.
        # B: derivative with respect to radial position coefficients.
        J = np.zeros((o.N,3,2*self.nc))
        J[:,0,:self.nc] = 2*vh
        J[:,1,:self.nc] = dh/ar[:,None]
        J[:,1,self.nc:] = vdh/ar[:,None]
        J[:,2,self.nc:] = 2*ddh/(ar*ar)[:,None]
        moments,first = blocks.normal_and_gradient(J,residual,mw)
        kuu = moments[:self.nc,:self.nc]
        kuy = moments[:self.nc,self.nc:]
        kyy = moments[self.nc:,self.nc:]
        gu,gy = first[:self.nc],first[self.nc:]
        ci = cj[active]; ix = np.ix_(ci,ci)
        u,y = bu[active],by[active]
        block = (np.outer(u,u)*kuu[ix]+np.outer(u,y)*kuy[ix]
                 +np.outer(y,u)*kuy.T[ix]+np.outer(y,y)*kyy[ix])
        normal[np.ix_(active,active)] += weight*block
        gradient[active] += weight*(u*gu[ci]+y*gy[ci])
    C0 = float(np.sum(self.radial_weights))*o.full_N
    if linearize:
        normal *= factor
        gradient *= factor
    return dict(weighted_sse=cost,all_raw_sse=raw_cost,max_gram=maximum,
        min_determinant=determinant,phi_normalized=loss/C0,
        normal_matrix=normal,gradient=gradient,
        spectral_half_gradient_factor=factor,
        spectral_minimum_eigenweight=minimum_weight,
        spectral_maximum_eigenweight=maximum_weight)


def spectral_stats(o,x,stage_weights,spectral,parameters):
    raw = o.raw_residual(x)
    value = spectral.statistics(raw,stage_weights,o.multiplicity,parameters)
    e,f,g = raw[...,0],raw[...,1],raw[...,2]
    costs = (e*e+2*f*f+g*g)@o.multiplicity
    norm = (np.abs(e+g)+np.sqrt((e-g)**2+4*f*f))/2
    value.update(weighted_sse=value['original_weighted_sse'],
        weighted_mean_sse=value['original_weighted_mean_sse'],
        all_raw_sse=float(np.sum(costs)),
        legacy_raw_sse=float(np.sum(costs[:o.legacy_P])),
        legacy_max_gram=float(np.max(norm[:o.legacy_P])),
        added_max_gram=float(np.max(norm[o.legacy_P:])),
        min_determinant=float(np.min((1+e)*(1+g)-f*f)))
    return value


def spectral_coarse_probe(o,x,basis,R,linear,normalization):
    """One new exact-space probe for the new spectral assembly and units."""
    spectral,parameters = basis.spectral_module,basis.spectral_parameters
    rng = np.random.default_rng(202611201)
    coefficients = R@rng.normal(size=basis.dimension)/np.sqrt(basis.dimension)
    free = basis.free_direction(coefficients)
    # This is the original complete derivative, not the coarse stage formula.
    jraw = o.unweight(o.jvp(x,free)).reshape(o.P,o.N,3)
    raw = o.raw_residual(x)
    exact_quadratic,cs_gradient = 0.,0.
    h = 1.e-25
    factor = parameters.k/parameters.scale**2
    for start in range(0,o.P,o.stage_block):
        stop=min(start+o.stage_block,o.P)
        blocks=basis.spectral_hessian_module.HessianBlocks(raw[start:stop],parameters)
        weights=basis.radial_weights[start:stop,None]*o.multiplicity[None]
        exact_quadratic += float(np.sum(weights*np.sum(
            jraw[start:stop]*blocks.apply(jraw[start:stop]),axis=-1)))
        losses=spectral.point_loss(raw[start:stop]+1j*h*jraw[start:stop],parameters)
        cs_gradient += float(np.sum(weights*losses.imag)/h)
    expected_quadratic=float(coefficients@linear['normal_matrix']@coefficients)/normalization
    exact_quadratic *= factor/normalization
    predicted_gradient=2*float(coefficients@linear['gradient'])/normalization
    cs_gradient /= normalization
    qerr=abs(expected_quadratic-exact_quadratic)/max(1.e-30,abs(expected_quadratic),abs(exact_quadratic))
    gerr=abs(predicted_gradient-cs_gradient)/max(1.e-30,abs(predicted_gradient),abs(cs_gradient))
    value=dict(normal_direction_relative_error=qerr,true_phi_gradient_relative_error=gerr,
        predicted_phi_gradient=predicted_gradient,complex_step_phi_gradient=cs_gradient,
        expected_mean_quadratic=expected_quadratic,original_Jv_mean_quadratic=exact_quadratic,
        half_gradient_factor=factor,normalization=normalization,
        probe='One whitened random physical direction against original complete Jv and complex polynomial Phi')
    if max(qerr,gerr)>2.e-8:
        raise ValueError('New positive spectral coarse mapping/units mismatch: '+repr(value))
    return value


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
        self.fixed_curvature, self.fixed_radius = OrderedDict(), OrderedDict()

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
            self.fixed_curvature[point_key(item['point'])] = None
            self.put('curvature', item['point'])
        for item in reversed(report.get('radius_witnesses', [])):
            self.fixed_radius[point_key(item['point'])] = None
            self.put('radius', item['point'])

    def restore(self, path):
        value = json.loads(Path(path).read_text())
        for key in ('curvature','radius'):
            for point in value.get('fixed_'+key+'_points', []):
                getattr(self,'fixed_'+key)[point_key(point)]=None
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
            fixed_curvature_points=list(self.fixed_curvature),fixed_radius_points=list(self.fixed_radius),
            scope='Geometry-only locations; both current principal branches are always reread')


def scan_local(field, o, x, grid, curvatures, radii, memory, *, refine=4, reach_ratio=.03,
               pinned_curvature=(), pinned_radius=()):
    field.set_state(x)
    cpoints = list(memory.fixed_curvature)+list(memory.protected)+list(memory.curvature)+list(pinned_curvature)+[stage_point(o,*v[:2]) for v in curvatures[:12]]
    rpoints = list(memory.fixed_radius)+list(memory.radius)+list(pinned_radius)+[stage_point(o,*v) for v in radii[:2]]
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


def general_direction(normal, gradient, Q, bounds, damping, *, norm_right, normalization,
                      repair_iterations=40000, relative_damping=1.e-3):
    """Approximate convex QP then general A-orthogonal halfspace repair.

    Unlike contraction to zero, this repair never assumes b >= 0.
    Every repair projection is z <- z - A^-1 r_i * violation/(r_i A^-1 r_i).
    A successful numerical repair is checked in the original unscaled rows.
    The nonlinear acceptance is independent and stricter.
    """
    R=norm_right
    data_normal=(R.T@normal@R)/normalization
    mean_eigenvalue=float(np.trace(data_normal))/len(gradient)
    if damping is None:
        if not np.isfinite(mean_eigenvalue) or mean_eigenvalue<=0 or relative_damping<=0:
            raise ValueError('Need positive finite data trace and relative damping')
        damping=float(np.sqrt(relative_damping*mean_eigenvalue))
    C=data_normal+damping*damping*np.eye(len(gradient))
    C=(C+C.T)/2
    factor=cho_factor(C,lower=True,check_finite=False)
    z0=cho_solve(factor,-(R.T@gradient)/normalization,check_finite=False)
    rawrows=Q@R
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
    direction=R@z
    true_violation=float(np.max(Q@direction-bounds))
    feasible=bool(np.isfinite(direction).all() and true_violation <= 2.e-8)
    return direction,dict(feasible=feasible,dual_success=bool(result.success),
        dual_message=str(result.message),dual_iterations=int(result.nit),
        constraints=len(bounds),negative_bounds=int(np.sum(bounds<0)),
        nonzero_dual=int(np.sum(lam>1.e-9)),
        scaled_max_violation_before_repair=before,projection_repairs=repairs,
        maximum_primal_violation=true_violation,
        original_gradient_dot_direction=float(gradient@direction),
        step_norm=float(np.linalg.norm(direction)),physical_coordinate_norm=float(np.linalg.norm(z)),
        damping=damping,mean_normalization=normalization,
        data_mean_eigenvalue=mean_eigenvalue,
        damping_squared_over_data_mean_eigenvalue=damping*damping/mean_eigenvalue,
        unnormalized_step_penalty_coefficient=normalization*damping*damping,
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
    spectral=load(args.spectral_source)
    spectral_hessian=load(args.hessian_source)
    parameters=spectral.Parameters(p=args.spectral_p,epsilon=args.spectral_epsilon,scale=args.spectral_scale)
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
    basis.spectral_module=spectral
    basis.spectral_hessian_module=spectral_hessian
    basis.spectral_parameters=parameters
    basis.evaluate=MethodType(spectral_evaluate,basis)
    base.fields_block=gauss.fields_block_observed
    norm_right,norm_metadata=physical_norm(o,basis,args)
    normalization=float(np.sum(radial_weights))*o.full_N
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
    fixed_sources=[]
    for path in args.fixed_point_input:
        value=json.loads(path.read_text())
        if value.get('carrier_sha256',sha(args.carrier))!=sha(args.carrier):
            raise ValueError('Fixed witness carrier mismatch')
        for point in value.get('protected_curvature_points',[]):
            local.protect(point)
        for point in value.get('curvature_points',[]):
            local.fixed_curvature[point_key(point)]=None
        for point in value.get('radius_points',[]):
            local.fixed_radius[point_key(point)]=None
        for stage,angle in value.get('grid_curvature_locations',[]):
            local.fixed_curvature[point_key(stage_point(o,stage,angle))]=None
        for stage,angle in value.get('grid_radius_locations',[]):
            local.fixed_radius[point_key(stage_point(o,stage,angle))]=None
        fixed_sources.append(dict(path=str(path),sha256=sha(path),source_bundle_sha256=value.get('bundle_sha256')))
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
    initial=state=spectral_stats(o,x,radial_weights,spectral,parameters)
    initial_grid,initial_local=grid,current_local
    initial_restoration=current_local['necessary_reach_product']>args.safety
    args.out.with_suffix('.initial.json').write_text(json.dumps(dict(
        source_sha256=sha(__file__),input_sha256=sha(args.bundle),initial=initial,
        gauss_geometry=initial_grid,arbitrary_geometry=initial_local,
        arbitrary_derivative_probe=probe,witness_reference_checks=witness_checks,
        physical_norm=norm_metadata,fixed_witness_sources=fixed_sources),indent=2)+'\n')
    records=[]; damping=args.damping; status='iteration_budget'; restoration_failures=0
    initial_mapping_check=None; initial_spectral_mapping_check=None
    initial_damping_used=None; spectral_probe=None
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
        phi_difference=abs(linear['phi_normalized']-state['phi_normalized'])/max(1.e-300,abs(state['phi_normalized']))
        if phi_difference>2.e-10:
            raise ValueError('Actual positive spectral objective disagrees with coarse evaluation')
        if initial_mapping_check is None:
            initial_mapping_check=difference
            initial_spectral_mapping_check=phi_difference
            if not args.skip_spectral_probe:
                spectral_probe=spectral_coarse_probe(o,x,basis,norm_right,linear,normalization)
        cpoints,rpoints=memory.combine(curvatures,radii,o)
        Q,bounds,active=all_constraints(base,geometry,local_geometry,o,x,cpoints,rpoints,
            local,args.reach_ratio,args.safety-args.linear_margin)
        pinned_curvature=tuple(dict.fromkeys(list(local.protected)+list(local.curvature)))
        pinned_radius=tuple(local.radius)
        direction,qp=general_direction(linear['normal_matrix'],linear['gradient'],Q,bounds,damping,
            norm_right=norm_right,normalization=normalization,repair_iterations=args.repair_iterations,
            relative_damping=args.relative_damping)
        damping=qp['damping']
        if initial_damping_used is None:
            initial_damping_used=damping
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
                definition='predicted true-Phi model decrease = (-2 alpha g.p - alpha^2 p.N.p)/C0; g and N both contain k/scale^2; LM penalty excluded',
                spectral_weights=dict(minimum=linear['spectral_minimum_eigenweight'],maximum=linear['spectral_maximum_eigenweight']))
            for backtrack in range(args.backtracks):
                alpha=2.**(-backtrack)
                predicted=(-2*alpha*gp-alpha*alpha*pp)/normalization
                candidate=x+alpha*free
                trial=spectral_stats(o,candidate,radial_weights,spectral,parameters)
                actual=state['phi_normalized']-trial['phi_normalized']
                ratio=actual/predicted if predicted>0 else None
                item=dict(alpha=alpha,statistics=trial,predicted_decrease=predicted,
                          actual_decrease=actual,model_ratio=ratio,accepted=False)
                if np.isfinite(trial['phi_normalized']) and actual>0 and trial['min_determinant']>0:
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
                    item['rejection']='no_true_Phi_descent_or_nonpositive_metric'
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
    report=dict(schema='fullclosed-coarse-exact-spectral-residual-Hessian-physical-H2-curvature-QP-v7',status=status,
        source_sha256=sha(__file__),input_sha256=sha(args.bundle),output_bundle_sha256=sha(output),
        dependency_sha256={key:sha(getattr(args,key)) for key in
            ('gauss_source','qp_source','memory_source','operator','batch_source','observed_source',
             'carrier','base_source','coarse_source','norm_source','coordinate_source','scale_source','height_source','spectral_source','hessian_source')},
        initial=initial,final=state,initial_gauss_geometry=initial_grid,final_gauss_geometry=grid,
        initial_arbitrary_geometry=initial_local,final_arbitrary_geometry=current_local,
        initial_restore_required=initial_restoration,
        final_known_point_safety_pass=bool(current_local['complete'] and current_local['necessary_reach_product']<=args.safety),
        initial_height=float(data['Hcap']),final_height=float(height),
        initial_affine=affine,final_affine=final_affine,initial_memory=initial_memory,
        final_memory=dict(grid=grid_memory_state(),arbitrary=local_memory_state()),
        witness_reference_checks=witness_checks,arbitrary_derivative_probe=probe,
        physical_norm=norm_metadata,fixed_witness_sources=fixed_sources,
        mean_normalization=normalization,
        initial_unnormalized_step_penalty=None if initial_damping_used is None else normalization*initial_damping_used*initial_damping_used,
        spectral_parameters=parameters.as_dict(),spectral_half_gradient_factor=parameters.k/parameters.scale**2,
        initial_spectral_basis_operator_relative_difference=initial_spectral_mapping_check,
        spectral_coarse_probe=spectral_probe,
        initial_damping_policy='fixed explicit mu' if args.damping is not None else 'mu^2 = relative_damping * trace(whitened mean spectral normal)/dimension, evaluated at the initial parent only',
        initial_relative_damping=None if args.damping is not None else args.relative_damping,
        initial_weighted_basis_operator_difference=initial_mapping_check,
        subspace_dimension=basis.dimension,low_modes=args.low_modes,
        centers=[float(o.mesh[i]) for i in basis.center_nodes],full_variables=o.free_size,
        observation_metadata=o.observation_metadata(),all_original_gram_rows_retained=True,
        objective='True normalized fixed-epsilon spectral Phi on every original positive Simpson/Gauss/orbit row; Jw and maxGram remain diagnostics. Frozen blocks are not an MM majorant for p>2',
        all_new_arbitrary_witness_locations_retained=True,
        data_normal='(k/scale^2) J^T weights [T^* Dh(E) T] J; exact positive residual Hessian',
        data_gradient='(k/scale^2) J^T weights K(E)r; unchanged true half-gradient, not L(E)r',
        full_nonlinear_field_Hessian_exact=False,
        spectral_eigenweight_metadata='Dh(E) in orthonormal Frobenius coordinates',
        radial_weight_sum=float(np.sum(radial_weights)),legacy_fraction=args.legacy_fraction,
        numerical_safety=args.safety,linear_margin=args.linear_margin,reach_ratio=args.reach_ratio,
        local_refine=args.local_refine,initial_damping=initial_damping_used,final_damping=damping,
        iterations=records,elapsed_seconds=time.monotonic()-started,
        fixed_scalar_mesh_and_core_unchanged=True,continuous_metric_certified=False,
        reach_certified=False,held_amplitude_certified=False,exact_solution_claimed=False)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='iterations'}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('bundle','operator','batch-source','base-source','coarse-source','out',
                'gauss-source','qp-source','memory-source','observed-source','carrier',
                'norm-source','coordinate-source','scale-source','height-source','spectral-source','hessian-source'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--memory-input',type=Path)
    p.add_argument('--local-memory-input',type=Path)
    p.add_argument('--witness-input',type=Path,action='append',default=[])
    p.add_argument('--protected-point',action='append',default=[])
    p.add_argument('--fixed-point-input',type=Path,action='append',default=[])
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
    damping_group=p.add_mutually_exclusive_group()
    damping_group.add_argument('--damping',type=float,default=None)
    damping_group.add_argument('--relative-damping',type=float,default=1.e-3)
    p.add_argument('--spectral-p',type=int,default=8)
    p.add_argument('--spectral-epsilon',type=float,default=.001)
    p.add_argument('--spectral-scale',type=float,default=.05)
    p.add_argument('--skip-spectral-probe',action='store_true')
    p.add_argument('--steps',type=int,default=12)
    p.add_argument('--backtracks',type=int,default=12)
    p.add_argument('--repair-iterations',type=int,default=40000)
    p.add_argument('--restoration-attempts',type=int,default=3)
    p.add_argument('--seconds',type=float,default=1800.)
    main(p.parse_args())






