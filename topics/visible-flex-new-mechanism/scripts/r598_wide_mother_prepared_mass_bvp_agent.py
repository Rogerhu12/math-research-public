#!/usr/bin/env python3
"""R598: a new wide 18-block mother, prepared true moments, original mass BVP.

Only the named public Actions runner may execute science. Old R578 numerical
states/tables are never inputs. Reuse of proved formulas is not an identity
rerun. Both actual ruling equations and the full positive square are retained.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
import os
import time

import mpmath as mp
import numpy as np
from scipy.integrate import cumulative_simpson, simpson, solve_ivp
from scipy.optimize import brentq, least_squares
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import lsmr
from scipy.spatial.distance import pdist

import r590_c2_staged_trust_collocation_agent as previous

paid = previous.paid
LD, ODD, EVEN, JPAR = paid.LD, paid.ODD, paid.EVEN, paid.JPAR
Jet, constant, emit = paid.Jet, paid.constant, paid.emit
WIDTH = 1/12000
POSITION_SCALE = .99
ACCELERATION_UNIT = 8.


@lru_cache(maxsize=1)
def wide_graph():
    """Generate the exact R598 algebraic definitions at 80 decimal digits."""
    start = time.time()
    with mp.workdps(80):
        fifth, _ = mp.gauss_quadrature(5, "legendre")
        cuts = [mp.mpf(-1)]+list(fifth)+[mp.mpf(1)]
        groups, weights = [], []
        for tau in (-1, 0, 1):
            roots = []
            def polynomial(x):
                return mp.legendre(6, x)+tau*mp.legendre(5, x)
            for left, right in zip(cuts[:-1], cuts[1:]):
                if tau == 1 and left == -1:
                    roots.append(left)
                    continue
                if tau == -1 and right == 1:
                    roots.append(right)
                    continue
                lo, hi = left, right
                flo = polynomial(lo)
                for _ in range(280):
                    mid = (lo+hi)/2
                    fm = polynomial(mid)
                    if fm == 0:
                        lo = hi = mid
                        break
                    if flo*fm > 0:
                        lo, flo = mid, fm
                    else:
                        hi = mid
                roots.append((lo+hi)/2)
            row = []
            for i, root in enumerate(roots):
                coeff = [mp.mpf(1)]
                denom = mp.mpf(1)
                for j, other in enumerate(roots):
                    if i == j:
                        continue
                    new = [mp.mpf(0)]*(len(coeff)+1)
                    for degree, value in enumerate(coeff):
                        new[degree] -= other*value
                        new[degree+1] += value
                    coeff = new
                    denom *= root-other
                row.append(sum(value/(degree+1) for degree, value in enumerate(coeff)
                               if degree % 2 == 0)/denom)
            groups.append([5+mp.mpf(99)/100*x for x in roots])
            weights.append(row)
        moment_error = max(
            abs(sum(weights[j][i]*((groups[j][i]-5)/(mp.mpf(99)/100))**degree
                    for i in range(6))-(mp.mpf(0) if degree % 2 else mp.mpf(1)/(degree+1)))
            for j in range(3) for degree in range(11))
        ordered = sorted(x for row in groups for x in row)
        spacing = min(b-a for a, b in zip(ordered[:-1], ordered[1:]))
        metadata = {
            "actual_blocks":18, "micro_packets":576, "rotations":3,
            "tau":[-1,0,1], "micro_half_width":WIDTH,
            "position_scale":POSITION_SCALE, "common_window":[4,6],
            "actual_copy_amplitude":"(2*w)^(1/4) times epsilon^(7/4)/256",
            "whole_envelope_half_width":31/6000,
            "each_open_collar":1/3000,
            "proved_spacing_lower_bound":"319/30000",
            "evaluated_minimum_spacing":mp.nstr(spacing,50),
            "evaluated_degree_ten_moment_error":mp.nstr(moment_error,12),
            "actual_centers":[[float(x) for x in row] for row in groups],
            "actual_positive_weights":[[float(w) for w in row] for row in weights],
            "elapsed_seconds":time.time()-start,
            "paper_spacing_proof":"R598; numerical values are not the proof"}
        if min(w for row in weights for w in row) <= 0:
            raise FloatingPointError("new_actual_positive_weight_failed")
        return (np.array([[float(x) for x in row] for row in groups]),
                np.array([[float(w) for w in row] for row in weights]),metadata)


class WideReferenceGrid(paid.old.ReferenceGrid):
    """Six unrotated reference blocks represent the 18 actual blocks via R598.

    The reference raw amplitude omits (2*w)^(1/4). Inherited reference_integral
    and PositivePotentialGram use total factor 6 = 3*2, with weight w once.
    Only the proved quartic readouts use this convention.
    """
    def __post_init__(self):
        core = paid.old.c2.core
        positions, weights, self.graph_info = wide_graph()
        self.actual_blocks, self.blocks = 18, 6
        self.width = WIDTH
        self.copy_positions, self.copy_weights = positions, weights
        self.block_weights = weights[1].copy()  # tau=0 common moment rule
        centers = np.array([15*j+3*m-57 for j in range(8) for m in range(4)])*WIDTH
        self.segments = []
        nodes, quadrature, active, local_x, fcoef, gcoef = [], [], [], [], [], []
        cursor = 0
        for packet, center in enumerate(centers):
            if packet:
                left, right = centers[packet-1]+WIDTH, center-WIDTH
                xn, wn, integration = core.gauss_right_matrix(self.gap_order)
                count, scale = len(xn), (right-left)/2
                self.segments.append((slice(cursor,cursor+count),scale,integration))
                nodes.extend((left+right)/2+scale*xn)
                quadrature.extend(scale*wn)
                active.extend([False]*count)
                local_x.extend([0.]*count)
                fcoef.extend([0.]*count)
                gcoef.extend([0.]*count)
                cursor += count
            xn, wn, integration = core.gauss_right_matrix(self.order)
            self.segments.append((slice(cursor,cursor+self.order),WIDTH,integration))
            nodes.extend(center+WIDTH*xn)
            quadrature.extend(WIDTH*wn)
            active.extend([True]*self.order)
            local_x.extend(xn)
            macro, micro = divmod(packet,4)
            amp = (-1)**macro*core.comb(7,macro)**(1/3)
            af = amp*(1 if micro==0 else np.sqrt(3) if micro==2 else 0)
            ag = amp*(np.sqrt(3) if micro==1 else 1 if micro==3 else 0)
            fcoef.extend([af]*self.order)
            gcoef.extend([ag]*self.order)
            cursor += self.order
        self.local_nodes = np.asarray(nodes)
        self.y = positions[1,:,None]+self.local_nodes[None,:]
        self.quad = np.asarray(quadrature)
        self.amplitude = WIDTH**1.75/256
        mask, xx = np.asarray(active,dtype=bool), np.asarray(local_x)
        raw = np.zeros((5,cursor))
        with np.errstate(over="ignore",under="ignore",invalid="raise"):
            for degree, fun in enumerate(core.bump_derivative_functions()):
                raw[degree,mask] = self.amplitude*fun(xx[mask])/WIDTH**degree
        self.raw = np.broadcast_to(raw[:,None,:],(5,6,cursor)).copy()
        self.fcoef = np.broadcast_to(np.asarray(fcoef)[None,:],self.y.shape).copy()
        self.gcoef = np.broadcast_to(np.asarray(gcoef)[None,:],self.y.shape).copy()
        self.y_limits = (4.,6.)


class CountedCoefficients(paid.DifferentiableCoefficients):
    def __init__(self,*args):
        super().__init__(*args)
        self.stats["actual_blocks"] = 18
        self.stats["mother"] = "R598-fixed-epsilon-1-over-12000"
        self.value_calls = self.jet_calls = 0

    def evaluate(self,*args):
        self.value_calls += 1
        return super().evaluate(*args)

    def evaluate_jets(self,*args):
        self.jet_calls += 1
        return super().evaluate_jets(*args)


class PreparedGuide:
    """A finite bounded analytic geometry with one true monotone moment choice.

    The continuous definition uniquely sets c by integral h*k=0. Here that
    scalar integral is approximated with a fixed positive Gauss rule; all
    eight final actual moment defects are still reported, including p2.
    """
    def __init__(self,root_order):
        qx, qw = np.polynomial.legendre.leggauss(root_order)
        self.root_x, self.root_w = (qx+1)/2, qw/2
        self.geometry_calls = self.root_solves = self.root_integrand_calls = 0

    @staticmethod
    def fields(parameters,x,c):
        x = np.asarray(x)
        aa, bb = parameters[:5], parameters[5:10]
        length = parameters[10]
        orders = np.arange(5)
        angles = np.pi*orders[:,None]*x[None,:]
        hv = np.sum(aa[:,None]*np.cos(angles),axis=0)
        hxv = np.sum(-np.pi*orders[:,None]*aa[:,None]*np.sin(angles),axis=0)
        hxxv = np.sum(-(np.pi*orders[:,None])**2*aa[:,None]*np.cos(angles),axis=0)
        ht = np.tanh(hv)
        h = 1.9+ht
        hx = (1-ht*ht)*hxv
        hxx = (1-ht*ht)*(hxxv-2*ht*hxv*hxv)
        modes = np.r_[1,3,5,7,9,11]
        coeff = np.r_[c,bb]
        phase = np.pi/2*modes[:,None]*x[None,:]
        kv = np.sum(coeff[:,None]*np.sin(phase),axis=0)
        kxv = np.sum(np.pi/2*modes[:,None]*coeff[:,None]*np.cos(phase),axis=0)
        kxxv = np.sum(-(np.pi/2*modes[:,None])**2*coeff[:,None]*np.sin(phase),axis=0)
        kt = np.tanh(kv)
        k = 1.95*kt
        kx = 1.95*(1-kt*kt)*kxv
        kxx = 1.95*(1-kt*kt)*(kxxv-2*kt*kxv*kxv)
        return h,k,hx,kx,hxx,kxx,length

    def center_coefficient(self,parameters):
        self.root_solves += 1
        def residual(c):
            self.root_integrand_calls += 1
            h,k,*_ = self.fields(parameters,self.root_x,c)
            return np.dot(self.root_w,h*k)
        radius = 2+2*np.sum(np.abs(parameters[5:10]))
        while residual(-radius)*residual(radius)>0:
            radius *= 2
            if radius>1024:
                raise FloatingPointError("monotone_guide_bracket_unresolved")
        return brentq(residual,-radius,radius,xtol=2.e-13,rtol=8.e-15,maxiter=100)

    def geometry(self,parameters,x,c=None):
        self.geometry_calls += 1
        if c is None:
            c = self.center_coefficient(parameters)
        h,k,hx,kx,hxx,kxx,length = self.fields(parameters,x,c)
        eta = cumulative_simpson(kx/(2*h),x=x,initial=0.)
        return np.array([h,k,eta,hx/length,kx/length]),hxx/length**2,kxx/length**2,c

    @staticmethod
    def prepared(geometry):
        h,v = geometry[0,0],geometry[4,0]
        ac = np.zeros(8)
        ac[ODD] = [v/(12*h),0.,v/(16*h**3),v/(24*h)]
        return ac


def fit_prepared_guide(args):
    start = time.time()
    model = PreparedGuide(args.guide_root_order)
    x = np.linspace(0.,1.,args.guide_nodes)
    initial = np.array([.2,-.4,1.4,0.,0.,1.2,0.,0.,0.,0.,5.])
    lower, upper = np.r_[np.full(10,-2.5),2.05],np.r_[np.full(10,2.5),7.5]
    kept = np.array([0,1,3,4,5,6,7])
    scale = np.array([2.,1.,8.,8.,4.,4.,8.])
    best = {"parameters":initial.copy(),"score":float("inf")}
    best_feasible = {"parameters":None,"score":float("inf")}
    calls = 0
    def residual(parameters):
        nonlocal calls
        calls += 1
        geo,_,_,_ = model.geometry(parameters,x)
        ac = model.prepared(geo)
        endpoint = ac+parameters[-1]*simpson(previous.matrix_rates(geo),x=x,axis=1)
        core = endpoint[kept]/parameters[-1]*scale
        overflow = np.array([np.max(np.abs(geo[2]))-.94,
                             np.max(np.abs(geo[3]))-5.7,
                             np.max(np.abs(geo[4]))-5.7])
        value = np.r_[core,25*np.maximum(overflow,0.)]
        score = np.linalg.norm(value)
        if score<best["score"]:
            best.update(parameters=parameters.copy(),score=float(score))
        if np.all(overflow<0) and np.linalg.norm(core)<best_feasible["score"]:
            best_feasible.update(parameters=parameters.copy(),score=float(np.linalg.norm(core)))
        return value
    first = residual(initial)
    result = least_squares(residual,initial,bounds=(lower,upper),method="trf",
                           jac="3-point",x_scale="jac",max_nfev=args.guide_max_nfev,
                           ftol=1.e-12,xtol=1.e-12,gtol=1.e-12)
    chosen = best_feasible["parameters"] if best_feasible["parameters"] is not None else best["parameters"]
    last = residual(chosen)
    fine_x = np.linspace(0.,1.,args.history_nodes)
    geo,a,b,c = model.geometry(chosen,fine_x)
    ac = model.prepared(geo)
    endpoint = ac+chosen[-1]*simpson(previous.matrix_rates(geo),x=fine_x,axis=1)
    record = {"parameters":chosen.tolist(),"dependent_c":float(c),
              "prepared_center_Aodd":ac[ODD].tolist(),
              "eight_true_numerical_endpoint_moments":endpoint.tolist(),
              "initial_residual":first.tolist(),"chosen_residual":last.tolist(),
              "actual_residual_calls":calls,"nfev":int(result.nfev),
              "status":int(result.status),"message":str(result.message),
              "feasible_sampled_guide_found":best_feasible["parameters"] is not None,
              "success":bool(result.success),"elapsed_seconds":time.time()-start,
              "geometry_ranges":{name:[float(v.min()),float(v.max())] for name,v in
                  zip(("h","k","eta","gamma","upsilon"),geo)},
              "monotone_root_quadrature_order":args.guide_root_order,
              "monotone_root_solves":model.root_solves,
              "monotone_root_integrand_calls":model.root_integrand_calls,
              "exact_moment_or_ruling_root_claim":False,
              "sampled_eta_is_not_a_continuous_box_certificate":True}
    emit("R598_PREPARED_GUIDE",record)
    return model,chosen,c,record


class MassRHS(previous.CenteredRHS):
    """21 stage coordinates, of which the last two are algebraic accelerations."""
    def __init__(self,coefficients,potential,coordinate_guard):
        super().__init__(coefficients,potential,coordinate_guard)
        # These fixed units define only the finite search guard. They do not
        # transform a state, parameter, equation, residual, or AD column.
        self.state_guard_units = np.ones(21)
        self.parameter_guard_units = np.ones(10)

    def set_gauge_unit(self,unit):
        self.nuhat_scale = LD(unit)
        self.coordinates = previous.CenterCoordinates(self.nuhat_scale)

    def one(self,state,parameters,derivatives=False):
        self.direct_state_evaluations += 1
        self.derivative_state_evaluations += int(derivatives)
        if not np.all(np.isfinite(state)) or not np.all(np.isfinite(parameters)):
            raise FloatingPointError("nonfinite_mass_coordinate")
        if max(np.max(np.abs(state)/self.state_guard_units),
               np.max(np.abs(parameters)/self.parameter_guard_units))>self.coordinate_guard:
            raise FloatingPointError("declared_mass_coordinate_guard")
        js = self.jets(state,parameters,31 if derivatives else 0)
        ys,ps = js[:21],js[21:]
        geo,chart = self.coordinates.physical(ys[:19])
        center,ca,zeta,length = self.coordinates.center(ps)
        h,k,eta,gamma,upsilon = geo
        ah = ys[5:13]
        neg,aneg = [h,-k,-eta,-gamma,upsilon],[q*v for q,v in zip(JPAR,ah)]
        op,om = self.coefficients.evaluate_jets(geo,ah),self.coefficients.evaluate_jets(neg,aneg)
        hp,kp,hm,km = op[1],op[2],om[1],om[2]
        if not (hp.value<0 and hm.value<0 and kp.value>0 and km.value>0):
            raise FloatingPointError("actual_mass_Ch_Ck_sign_domain")
        acc,bcc = ACCELERATION_UNIT*ys[19],ACCELERATION_UNIT*ys[20]
        dep = self.potential.center_difference(geo,ah,center,ca)
        dem = self.potential.center_difference(neg,aneg,center,ca)
        wp,wm = paid.weights(geo),paid.weights(neg)
        fp = (op[0]-4*paid.dot(wp,ys[13:16])-4*dep
              -2*previous.center_pairing(geo,center,zeta))
        fm = (om[0]-4*paid.dot(wm,ys[16:19])-4*dem
              -2*previous.center_pairing(neg,center,zeta))
        qg = 1+(h*eta-k)**2
        flow = [gamma/chart[0],upsilon/chart[1],upsilon/(2*h*chart[2]),
                acc/chart[3],bcc/chart[4]]
        flow.extend(paid.density(geo))
        flow.extend((op[3+3*j]+acc*op[4+3*j]+bcc*op[5+3*j])/qg**2 for j in range(3))
        flow.extend(-(om[3+3*j]+acc*om[4+3*j]-bcc*om[5+3*j])/qg**2 for j in range(3))
        # Algebraic equations are the original two ruling residuals, not a
        # guessed slow manifold. Eliminating a,b recovers the paid Cramer RHS.
        outputs = [length*v for v in flow]+[fp+hp*acc+kp*bcc,fm+hm*acc-km*bcc]
        value,jac = paid.values_and_jacobian(outputs)
        if not np.all(np.isfinite(value)) or not np.all(np.isfinite(jac)):
            raise FloatingPointError("nonfinite_original_mass_equations")
        return np.asarray(value,dtype=float),np.asarray(jac,dtype=float)

    def jacobian(self,x,states,parameters):
        self.jacobian_calls += 1
        out = np.stack([self.one(states[:,i],parameters,True)[1]
                        for i in range(states.shape[1])],axis=2)
        return out[:,:21],out[:,21:]

    def boundary(self,left,right,parameters):
        return super().boundary(left[:19],right[:19],parameters)

    def boundary_jacobian(self,left,right,parameters):
        bl,br,bp = super().boundary_jacobian(left[:19],right[:19],parameters)
        return np.pad(bl,((0,0),(0,2))),np.pad(br,((0,0),(0,2))),bp


def make_seed(rhs,model,guide,c,args):
    start = time.time()
    count = args.history_nodes
    if (count-1)%(2*args.intervals):
        raise ValueError("history nodes must contain every initial stage")
    x = np.linspace(0.,1.,count)
    geometry,a,b,_ = model.geometry(guide,x,c)
    ac = model.prepared(geometry)
    length = guide[-1]
    history = ac[:,None]+length*cumulative_simpson(
        previous.matrix_rates(geometry),x=x,axis=1,initial=0.)
    h0,v0 = geometry[0,0],geometry[4,0]
    parameters = np.zeros(10)
    parameters[0] = float(np.tan(paid.PI/2*(h0-1.9)/1.1))
    parameters[1] = float(np.tan(paid.PI/2*v0/6))
    parameters[9] = float(np.tan(paid.PI/2*(length-5)/3))
    outputs_plus,outputs_minus,energies = [],[],[]
    for i in range(count):
        gg = tuple(geometry[:,i])
        gm = (gg[0],-gg[1],-gg[2],-gg[3],gg[4])
        ap,am = history[:,i],JPAR*history[:,i]
        op = rhs.coefficients.evaluate(gg,ap)
        om = rhs.coefficients.evaluate(gm,am)
        outputs_plus.append(op); outputs_minus.append(om)
        for gv,av in ((gg,ap),(gm,am)):
            energies.append(rhs.potential.energy([constant(v,0) for v in gv],
                            [constant(v,0) for v in av]).value)
    # This fixed reversible parameter unit is chosen from this new true guide,
    # not the old r0=1 reference. It never changes during the subsequent solve.
    unit = max(LD(1),max(abs(v) for v in energies))
    rhs.set_gauge_unit(unit)
    center,ca,zeta,_ = rhs.coordinates.center([constant(v,0) for v in parameters])
    center_outputs = rhs.coefficients.evaluate(tuple(v.value for v in center),ac)
    parameters[6] = float((center_outputs[0]+center_outputs[1]*a[0]
                          +center_outputs[2]*b[0])/(2*paid.old.weights(h0,0.,0.)[0]))
    state = np.zeros((21,count))
    state[:5] = rhs.coordinates.encode(geometry)
    state[5:13] = history
    rp,rm = [],[]
    for i in range(count):
        gg = tuple(geometry[:,i]); gm = (gg[0],-gg[1],-gg[2],-gg[3],gg[4])
        rp.append(rhs.coefficients.history_rhs(outputs_plus[i],gg,a[i],b[i]))
        rm.append(-rhs.coefficients.history_rhs(outputs_minus[i],gm,a[i],-b[i]))
    state[13:16] = length*cumulative_simpson(np.asarray(rp).T,x=x,axis=1,initial=0.)
    state[16:19] = length*cumulative_simpson(np.asarray(rm).T,x=x,axis=1,initial=0.)
    state[19],state[20] = a/ACCELERATION_UNIT,b/ACCELERATION_UNIT
    rows,targets = [],[]
    for i in range(count):
        h,k,eta,gamma,upsilon = geometry[:,i]
        for sign,op,rho in ((1,outputs_plus[i],state[13:16,i]),
                             (-1,outputs_minus[i],state[16:19,i])):
            gg = [constant(v,0) for v in (h,sign*k,sign*eta,sign*gamma,upsilon)]
            av = history[:,i] if sign==1 else JPAR*history[:,i]
            aj = [constant(v,0) for v in av]
            dep = rhs.potential.center_difference(gg,aj,center,ca).value
            dg = sign*(h*eta-k)
            w = paid.old.weights(h,sign*k,sign*eta)
            q2 = ((h-h0)*(h+h0)-h0*h0*dg*dg)/(4*h)
            rows.append([dg,2*q2])
            targets.append(op[0]+op[1]*a[i]+sign*op[2]*b[i]
                           -4*w@rho-4*dep-2*w[0]*parameters[6])
    matrix = np.asarray(rows,dtype=float)*float(unit)
    target = np.asarray(targets,dtype=float)
    fitted,_,rank,singular = np.linalg.lstsq(matrix,target,rcond=None)
    used = bool(np.all(np.isfinite(fitted)) and np.max(np.abs(fitted))<rhs.coordinate_guard)
    if used:
        parameters[7:9] = fitted
    after = target-matrix@parameters[7:9]
    center_energy = rhs.potential.energy(center,ca).value
    rhs.state_guard_units[13:19] = np.maximum(1.,np.max(np.abs(state[13:19]),axis=1))
    rhs.parameter_guard_units[6] = max(1.,abs(parameters[6]))
    indices = np.linspace(0,count-1,2*args.intervals+1,dtype=int)
    record = {
        "elapsed_seconds":time.time()-start,"history_nodes":count,
        "dependent_c_frozen":float(c),"odd_center":ac[ODD].tolist(),
        "center_positive_energy":float(center_energy),
        "center_E":np.asarray(center_outputs[16:19],dtype=float).tolist(),
        "fixed_center_null_parameter_unit":float(unit),
        "fixed_state_guard_units":rhs.state_guard_units.tolist(),
        "fixed_parameter_guard_units":rhs.parameter_guard_units.tolist(),
        "guard_units_only_define_finite_search_scope":True,
        "gauge_LS_rank":int(rank),"gauge_LS_singular_values":singular.tolist(),
        "gauge_LS_fitted_coordinates":[float(v) if np.isfinite(v) else None for v in fitted],
        "gauge_LS_used":used,"gauge_LS_guard":rhs.coordinate_guard,
        "true_guide_ruling_peak_before":float(np.max(np.abs(target))),
        "true_guide_ruling_peak_after":float(np.max(np.abs(after))),
        "actual_eight_endpoint":history[:,-1].tolist(),
        "actual_bc_max":float(np.max(np.abs(rhs.boundary(state[:,0],state[:,-1],parameters)))),
        "actual_acceleration_ranges":[[float(v.min()),float(v.max())] for v in (a,b)],
        "true_current_positive_energy_max":float(max(energies)),
        "exact_root_claim":False}
    emit("R598_TRUE_PREPARED_SEED",record)
    return x[indices],state[:,indices],parameters,float(unit),record


class StableHermite:
    """Evaluate the cubic in Hermite basis and copy exact endpoint data."""
    def __init__(self,x,y,f):
        self.x,self.y,self.f = np.asarray(x),np.asarray(y),np.asarray(f)

    def __call__(self,t,nu=0):
        vals = np.atleast_1d(np.asarray(t,dtype=float))
        index = np.clip(np.searchsorted(self.x,vals,side="right")-1,0,len(self.x)-2)
        h = self.x[index+1]-self.x[index]
        q = (vals-self.x[index])/h
        yl,yr = self.y[:,index],self.y[:,index+1]
        fl,fr = self.f[:,index],self.f[:,index+1]
        if nu==0:
            out = ((2*q**3-3*q*q+1)*yl+(q**3-2*q*q+q)*h*fl
                   +(-2*q**3+3*q*q)*yr+(q**3-q*q)*h*fr)
            for j,v in enumerate(vals):
                exact = np.flatnonzero(self.x==v)
                if exact.size:
                    out[:,j] = self.y[:,exact[0]]
        elif nu==1:
            out = ((6*q*q-6*q)*yl/h+(3*q*q-4*q+1)*fl
                   +(-6*q*q+6*q)*yr/h+(3*q*q-2*q)*fr)
        else:
            raise ValueError("Only value and first derivative are used")
        return out[:,0] if np.ndim(t)==0 else out


class MassCollocation:
    def __init__(self,rhs,x,ruling_unit):
        self.rhs,self.x,self.ruling_unit = rhs,np.asarray(x),float(ruling_unit)
        self.h = self.x[2::2]-self.x[:-2:2]
        self.intervals = len(self.h)
        self.size = 21*len(self.x)+10

    def pack(self,y,p):
        return np.r_[y.ravel(order="F"),p]

    def unpack(self,z):
        return z[:-10].reshape((21,len(self.x)),order="F"),z[-10:]

    def evaluate(self,z):
        y,p = self.unpack(z)
        out = self.rhs(self.x,y,p)
        f,algebraic = out[:19],out[19:]
        mid = y[:19,1::2]-(y[:19,:-2:2]+y[:19,2::2])/2+self.h*(f[:,2::2]-f[:,:-2:2])/8
        total = y[:19,2::2]-y[:19,:-2:2]-self.h*(f[:,:-2:2]+4*f[:,1::2]+f[:,2::2])/6
        differential = np.column_stack([np.r_[mid[:,i]/self.h[i],total[:,i]/self.h[i]]
                                       for i in range(self.intervals)]).ravel(order="F")
        bc = self.rhs.boundary(y[:,0],y[:,-1],p)
        residual = np.r_[differential,algebraic.ravel(order="F"),bc]
        weights = np.r_[np.ones(len(differential)),
                        np.full(algebraic.size,1/self.ruling_unit),np.ones(29)]
        if not np.all(np.isfinite(residual)):
            raise FloatingPointError("nonfinite_original_mass_collocation")
        return {"z":z,"y":y,"p":p,"f":f,"algebraic":algebraic,
                "differential":differential,"bc":bc,"residual":residual,
                "weights":weights,"weighted":weights*residual}

    def jacobian(self,current):
        y,p = current["y"],current["p"]
        jy,jp = self.rhs.jacobian(self.x,y,p)
        fy,fp = jy[:19],jp[:19]
        bl,br,bp = self.rhs.boundary_jacobian(y[:,0],y[:,-1],p)
        rows,cols,values = [],[],[]
        def block(row,col,mat):
            rr,cc = np.indices(mat.shape)
            rows.extend((row+rr.ravel()).tolist())
            cols.extend((col+cc.ravel()).tolist())
            values.extend(mat.ravel().tolist())
        eye = np.pad(np.eye(19),((0,0),(0,2)))
        par = 21*len(self.x)
        for i,h in enumerate(self.h):
            l,m,r = 2*i,2*i+1,2*i+2
            row = 38*i
            block(row,21*l,-eye/(2*h)-fy[:,:,l]/8)
            block(row,21*m,eye/h)
            block(row,21*r,-eye/(2*h)+fy[:,:,r]/8)
            block(row,par,(fp[:,:,r]-fp[:,:,l])/8)
            block(row+19,21*l,-eye/h-fy[:,:,l]/6)
            block(row+19,21*m,-2*fy[:,:,m]/3)
            block(row+19,21*r,eye/h-fy[:,:,r]/6)
            block(row+19,par,-(fp[:,:,l]+4*fp[:,:,m]+fp[:,:,r])/6)
        row = 38*self.intervals
        for i in range(len(self.x)):
            block(row+2*i,21*i,jy[19:,:,i])
            block(row+2*i,par,jp[19:,:,i])
        row += 2*len(self.x)
        block(row,0,bl); block(row,21*(len(self.x)-1),br); block(row,par,bp)
        matrix = coo_matrix((values,(rows,cols)),shape=(self.size,self.size)).tocsc()
        matrix.eliminate_zeros()
        if not np.all(np.isfinite(matrix.data)):
            raise FloatingPointError("nonfinite_original_mass_Jacobian")
        return matrix

    def physical_spline(self,current):
        return StableHermite(self.x[::2],current["y"][:19,::2],current["f"][:,::2])


def mass_checkpoint(rhs,system,current,iteration,level,trust,damping,reason):
    data = {"schema":"r598-full-mass-accepted-state-v1","level":level,"iteration":iteration,
            "reason":reason,"clock_nodes":system.x.tolist(),
            "state_rows":current["y"].tolist(),"parameters":current["p"].tolist(),
            "acceleration_unit":ACCELERATION_UNIT,
            "fixed_differential_row_units":[1.]*19,
            "fixed_ruling_unit":system.ruling_unit,
            "fixed_center_null_parameter_unit":float(rhs.nuhat_scale),
            "fixed_state_guard_units":rhs.state_guard_units.tolist(),
            "fixed_parameter_guard_units":rhs.parameter_guard_units.tolist(),
            "guard_units_only_define_finite_search_scope":True,
            "trust_radius":trust,"damping":damping,
            "weighted_merit":float(.5*current["weighted"]@current["weighted"]),
            "actual_differential_max":float(np.max(np.abs(current["differential"]))),
            "actual_ruling_max":float(np.max(np.abs(current["algebraic"]))),
            "actual_boundary_residual":current["bc"].tolist(),
            "actual_boundary_max":float(np.max(np.abs(current["bc"])))}
    canonical = json.dumps(data,sort_keys=True,separators=(",",":"),allow_nan=False)
    digest = hashlib.sha256(canonical.encode()).hexdigest()
    emit("R598_MASS_ACCEPTED_STATE",{"state_sha256":digest,"complete_state":data})
    try:
        report = previous.physical_report(rhs,system,current)
        report["stored_stage_velocity_boundary"] = current["bc"][-2:].tolist()
        report["Hermite_to_stored_endpoint_max"] = float(np.max(np.abs(
            system.physical_spline(current)(np.array([0.,1.]))-current["y"][:19,[0,-1]])))
        report["original_mass_stage_acceleration_ranges"] = [
            [float(v.min()*ACCELERATION_UNIT),float(v.max()*ACCELERATION_UNIT)]
            for v in current["y"][19:]]
        json.dumps(report,allow_nan=False)
    except (FloatingPointError,ValueError,OverflowError) as exc:
        report = {"inspection_failure":{"type":type(exc).__name__,"message":str(exc)},
                  "complete_finite_state_retained":True}
    emit("R598_MASS_PHYSICAL",{"level":level,"iteration":iteration,
                             "state_sha256":digest,"readout":report})
    return report


def solve_mass(rhs,x,y,p,ruling_unit,args,level=0):
    started = time.time()
    system = MassCollocation(rhs,x,ruling_unit)
    current = system.evaluate(system.pack(y,p))
    trust,damping = args.trust_radius,args.damping
    report = mass_checkpoint(rhs,system,current,0,level,trust,damping,"new_prepared_wide_mother")
    accepted = rejected = linear_iterations = 0
    status = "iteration_limit_with_finite_state"
    def converged(evaluation):
        return (np.max(np.abs(evaluation["differential"]))<=args.flow_tol
                and np.max(np.abs(evaluation["algebraic"]))<=args.ruling_tol
                and np.max(np.abs(evaluation["bc"]))<=args.bc_tol)
    for iteration in range(1,args.newton_iterations+1):
        if converged(current):
            status = "actual_discrete_mass_equations_converged"
            break
        try:
            jac = system.jacobian(current)
        except (FloatingPointError,ValueError,OverflowError) as exc:
            status = "finite_state_after_Jacobian_failure"
            emit("R598_MASS_LINEAR_FAILURE",{"type":type(exc).__name__,"message":str(exc)})
            break
        weighted_jac = diags(current["weights"])@jac
        colmax = np.maximum(1.,np.asarray(abs(weighted_jac).max(axis=0).toarray()).ravel())
        normalized = weighted_jac@diags(1/colmax)
        norms = np.sqrt(np.asarray(normalized.power(2).sum(axis=0)).ravel())
        columns = (1/colmax)/np.maximum(1.,norms)
        matrix = weighted_jac@diags(columns)
        residual = current["weighted"]
        merit = .5*residual@residual
        accepted_here = False
        for trial in range(args.trial_limit):
            try:
                linear = lsmr(matrix,-residual,damp=np.sqrt(damping),
                              atol=1.e-11,btol=1.e-11,maxiter=args.linear_iterations)
            except (FloatingPointError,ValueError,OverflowError,RuntimeError) as exc:
                emit("R598_MASS_LINEAR_FAILURE",{
                    "level":level,"iteration":iteration,"trial":trial,
                    "type":type(exc).__name__,"message":str(exc),
                    "last_complete_finite_state_retained":True})
                break
            linear_iterations += int(linear[2])
            step = linear[0]
            rms = np.linalg.norm(step)/np.sqrt(len(step))
            if rms>trust:
                step *= trust/rms
            predicted = merit-.5*np.linalg.norm(residual+matrix@step)**2
            candidate,error = None,None
            actual,ratio,next_merit = None,None,None
            try:
                candidate = system.evaluate(current["z"]+columns*step)
                next_merit = .5*candidate["weighted"]@candidate["weighted"]
                if not np.isfinite(next_merit):
                    raise FloatingPointError("nonfinite_weighted_mass_merit")
                actual = merit-next_merit
                ratio = actual/predicted if predicted>0 else -np.inf
            except (FloatingPointError,ValueError,OverflowError) as exc:
                candidate = None
                error = {"type":type(exc).__name__,"message":str(exc)}
            ok = (candidate is not None and predicted>0 and actual>0
                  and np.isfinite(ratio) and ratio>=args.acceptance_ratio)
            finite = lambda value: None if value is None or not np.isfinite(value) else float(value)
            emit("R598_MASS_TRIAL",{"level":level,"iteration":iteration,"trial":trial,
                 "accepted":bool(ok),"current_merit":float(merit),"trial_merit":finite(next_merit),
                 "predicted_decrease":finite(predicted),"actual_decrease":finite(actual),
                 "actual_predicted_ratio":finite(ratio),"step_rms":finite(rms),
                 "lsmr_stop":int(linear[1]),"lsmr_iterations":int(linear[2]),
                 "trust_radius":trust,"damping":damping,"error":error})
            if ok:
                current = candidate
                accepted += 1
                if ratio>.75:
                    trust = min(args.maximum_trust,2*trust)
                    damping = max(1.e-14,damping/2)
                elif ratio<.25:
                    trust *= .75
                    damping *= 2
                report = mass_checkpoint(rhs,system,current,iteration,level,trust,damping,
                                         "accepted_actual_mass_merit_decrease")
                accepted_here = True
                break
            rejected += 1
            trust *= .5
            damping = min(1.e14,4*damping)
        if not accepted_here:
            status = "no_acceptable_step_finite_state_retained"
            break
    if converged(current):
        status = "actual_discrete_mass_equations_converged"
    summary = {"level":level,"status":status,"elapsed_seconds":time.time()-started,
               "unknowns":system.size,"stage_nodes":len(x),"accepted_steps":accepted,
               "rejected_trials":rejected,"LSMR_total_iterations":linear_iterations,
               "actual_differential_max":float(np.max(np.abs(current["differential"]))),
               "actual_ruling_max":float(np.max(np.abs(current["algebraic"]))),
               "actual_boundary_max":float(np.max(np.abs(current["bc"]))),
               "weighted_merit":float(.5*current["weighted"]@current["weighted"]),
               "full_RHS_calls":rhs.calls,"full_RHS_points":rhs.points,
               "full_Jacobian_calls":rhs.jacobian_calls,
               "full_direct_state_evaluations":rhs.direct_state_evaluations,
               "full_derivative_state_evaluations":rhs.derivative_state_evaluations,
               "continuous_root_claim":False}
    emit("R598_MASS_LEVEL_FINAL",summary)
    return system,current,summary,report


def guide_geometry_budget(model,guide,c,grid):
    """Original base-space and first-variation readouts, never a finite flex."""
    started = time.time()
    length = guide[-1]
    def ode(x,state):
        h,k,*_ = model.fields(guide,np.array([x]),c)
        frame = state[:9].reshape(3,3)
        omega = np.array([[0.,-k[0],0.],[k[0],0.,1.],[0.,-1.,0.]])
        return length*np.r_[(frame@omega).ravel(),h[0]**2*frame[:,0]]
    initial = np.r_[np.eye(3).ravel(),np.zeros(3)]
    result = solve_ivp(ode,(0.,1.),initial,method="DOP853",rtol=2.e-10,atol=2.e-12,dense_output=True)
    if not result.success:
        return {"frame_success":False,"message":str(result.message),
                "elapsed_seconds":time.time()-started}
    x = np.linspace(0.,1.,513)
    geo,*_ = model.geometry(guide,x,c)
    if (np.max(np.abs(geo[2]))>=1 or np.max(np.abs(geo[3:5]))>=6):
        return {"frame_success":True,"frame_nfev":int(result.nfev),
                "physical_guide_box_failed":True,
                "geometry_ranges":[[float(v.min()),float(v.max())] for v in geo],
                "elapsed_seconds":time.time()-started,
                "continuous_reach_embedding_or_finite_flex_claim":False}
    posed = result.sol(x)
    frames,alpha = posed[:9].T.reshape(-1,3,3),posed[9:].T
    h,k,eta,gamma,upsilon = geo
    normal = frames[:,:,1]
    edges,curvatures = [],[]
    for yy in (4.,6.):
        for sign in (1,-1):
            u = h/(yy+sign*eta)
            if sign==1:
                edges.append(alpha+u[:,None]*normal)
            else:
                edges.append(np.array([-1.,-1.,1.])*(alpha-u[:,None]*normal))
            kk,gg,vv = sign*k,sign*gamma,upsilon
            aa = h*h-kk*u
            den = np.sqrt(aa*aa+u*u)
            s11 = u*(2*h*gg-vv*u)/den**3
            s12 = -h*h/den**2
            curvatures.append((np.abs(s11)+np.sqrt(s11*s11+4*s12*s12))/2)
    points = np.concatenate(edges)
    sampled_diameter = float(np.max(pdist(points)))
    curvature = float(np.max(curvatures))
    positions,weights,_ = wide_graph()
    raw,fc,gc = grid.raw[:,0],grid.fcoef[0],grid.gcoef[0]
    H = h[0]
    first = []
    for which in ("f","g"):
        displacements,variations = [],[]
        for j,(cc,ss) in enumerate(((1.,0.),(-.5,np.sqrt(3)/2),(-.5,-np.sqrt(3)/2))):
            coeff = cc*fc-ss*gc if which=="f" else ss*fc+cc*gc
            for i in range(6):
                yy = positions[j,i]+grid.local_nodes
                actual = raw*coeff*(2*weights[j,i])**.25
                ff,pp,_,tt = actual[:4]
                e = H*yy
                displacement = np.hypot(-pp/(2*yy),H*ff/yy-e*pp/(2*yy))
                variation = yy**3*np.sqrt(1+e*e)*np.abs(tt)/(2*H*H)
                displacements.append(np.max(displacement))
                variations.append(np.max(variation))
        first.append({"profile":which,"sampled_first_field_norm":float(max(displacements)),
                      "sampled_exact_normal_curvature_variation":float(max(variations))})
    return {"frame_success":True,"frame_nfev":int(result.nfev),
            "elapsed_seconds":time.time()-started,
            "sampled_base_edges_diameter_lower":sampled_diameter,
            "sampled_base_collar_principal_curvature_max":curvature,
            "sampled_collar_focal_cap":1/curvature,
            "sampled_focal_cap_over_edge_diameter":1/(curvature*sampled_diameter),
            "center_first_variations":first,
            "base_pose_readouts":[float(normal[-1,2]**2-.5),
                float(alpha[-1,0]*normal[-1,1]-alpha[-1,1]*normal[-1,0])],
            "continuous_reach_embedding_or_finite_flex_claim":False,
            "scope":"actual new guide base and exact first-variation formula only"}


def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("Science only in the declared public Actions repository")
    parser = argparse.ArgumentParser()
    parser.add_argument("--order",type=int,default=192)
    parser.add_argument("--gap-order",type=int,default=8)
    parser.add_argument("--guide-root-order",type=int,default=96)
    parser.add_argument("--guide-nodes",type=int,default=257)
    parser.add_argument("--guide-max-nfev",type=int,default=400)
    parser.add_argument("--history-nodes",type=int,default=513)
    parser.add_argument("--intervals",type=int,default=32)
    parser.add_argument("--newton-iterations",type=int,default=50)
    parser.add_argument("--trial-limit",type=int,default=12)
    parser.add_argument("--linear-iterations",type=int,default=1600)
    parser.add_argument("--trust-radius",type=float,default=.25)
    parser.add_argument("--maximum-trust",type=float,default=4.)
    parser.add_argument("--damping",type=float,default=1.e-4)
    parser.add_argument("--acceptance-ratio",type=float,default=1.e-4)
    parser.add_argument("--coordinate-guard",type=float,default=1.e6)
    parser.add_argument("--flow-tol",type=float,default=1.e-7)
    parser.add_argument("--ruling-tol",type=float,default=1.e-7)
    parser.add_argument("--bc-tol",type=float,default=1.e-10)
    args = parser.parse_args()
    started = time.time()
    labels,rows = previous.rebuild_known_rows()
    grid = WideReferenceGrid(args.order,args.gap_order,5.)
    coefficients = CountedCoefficients(labels,rows,grid)
    potential = previous.FactoredPotential(grid)
    emit("R598_NEW_FIXED_MOTHER",{"graph":grid.graph_info,
         "coefficients":coefficients.stats,"positive_Gram":potential.stats,
         "formal_definition_rebuild_paid_as_new_cost":True,
         "old_identity_or_derivative_gates_repeated":False,
         "old_numeric_state_or_table_reused":False,"full_square_coefficient":1,
         "same_mother_claim_as_R578":False})
    model,guide,c,guide_record = fit_prepared_guide(args)
    emit("R598_NEW_GEOMETRY_BUDGET",guide_geometry_budget(model,guide,c,grid))
    rhs = MassRHS(coefficients,potential,args.coordinate_guard)
    try:
        x,y,p,unit,seed = make_seed(rhs,model,guide,c,args)
        system,current,summary,report = solve_mass(rhs,x,y,p,unit,args)
        if summary["status"]=="actual_discrete_mass_equations_converged":
            refined = np.linspace(0.,1.,4*args.intervals+1)
            physical = system.physical_spline(current)(refined)
            # Algebraic stage unknowns are only interpolated initial guesses.
            acc = np.vstack([np.interp(refined,system.x,row) for row in current["y"][19:]])
            system,current,summary,report = solve_mass(
                rhs,refined,np.vstack([physical,acc]),current["p"],unit,args,1)
        status = summary["status"]
    except (FloatingPointError,ValueError,OverflowError) as exc:
        status = "new_guide_or_mass_initialization_failed"
        emit("R598_NEW_INPUT_FAILURE",{"type":type(exc).__name__,"message":str(exc),
             "old_input_not_replayed":True,"exact_root_claim":False})
    emit("R598_DONE",{"elapsed_seconds":time.time()-started,"last_status":status,
         "coefficient_value_evaluations_all_scopes":coefficients.value_calls,
         "coefficient_jet_evaluations_all_scopes":coefficients.jet_calls,
         "guide_geometry_calls":model.geometry_calls,"guide_scalar_root_solves":model.root_solves,
         "guide_scalar_integrand_calls":model.root_integrand_calls,
         "README_completion_claim":False,"full_period_or_reach_claim":False})


if __name__=="__main__":
    main()

