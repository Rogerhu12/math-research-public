#!/usr/bin/env python3
"""R590: real moment guide and explicit-stage, safeguarded collocation.

Science runs only in the public Actions job. No old identity, directional
derivative gate, old four guesses, or 96/192 diagnostic is replayed.
All 19 physical equations, all 29 boundary conditions, and the square remain.
Every accepted complete finite state is printed before another trial is made.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import time

import numpy as np
from scipy.integrate import cumulative_simpson, simpson
from scipy.interpolate import CubicHermiteSpline
from scipy.optimize import least_squares
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import lsmr

import r590_c2_history_positive_square_free_germs_agent as paid

LD, ODD, EVEN, JPAR = paid.LD, paid.ODD, paid.EVEN, paid.JPAR
Jet, constant = paid.Jet, paid.constant
emit = paid.emit


def rebuild_known_rows():
    """Necessary definition rebuild, not a repeat of the paid identity gate."""
    started = time.time()
    old = paid.old
    labels, original, stats = old.compile_bundle()
    x,u,p,r,t,d = old.X,old.U,old.P,old.R,old.T,old.D
    h,k,eta,gamma,upsilon = old.H,old.K,old.E,old.G,old.V
    e = h*(x+eta)-k
    q,qg = 1+e**2,1+(h*eta-k)**2
    fzero = q*(gamma*p-(gamma*(x+eta)-upsilon/2)*r)/(8*h**3)
    _,a1,a2,b0,b1,b2 = old.e8_coefficients(old.AVAR)
    ha = a1*u+2*a2*p-2*(b0+x*b1+x*x*b2)*r
    rows,names = list(original[:3]),list(labels[:3])
    for j in range(3):
        for suffix,poly in zip(("0","a","b"),original[3+3*j:6+3*j]):
            rows.append(poly.coefficient(old.IT,0)
                        -old.d0(poly.coefficient(old.IT,1).primitive(old.IR)))
            names.append(f"C2N{j}_{suffix}")
    rows.extend(original[12:16])
    names.extend(labels[12:16])
    for j in range(3):
        rows.append(d**2*(qg*x**j*(fzero**2/4+ha**2/16)
                          +(q*fzero*ha/4 if j==0 else 0))*t**2)
        names.append(f"E{j}_numerator")
    emit("R590_TRUST_REBUILD",{
        "elapsed_seconds":time.time()-started,
        "definition_rows":len(rows),
        "old_formal_definition_seconds":stats["elapsed_seconds"],
        "paid_highest_identity_retested":False,
        "reason":"The prior stdout contains hashes but no reusable coefficient table."})
    return names,rows


class FactoredPotential(paid.PositivePotentialGram):
    def center_difference(self,geometry,history,center_geometry,center_history):
        h,k,eta,_,_ = geometry
        hc = center_geometry[0]
        dg = h*eta-k
        current,_,_ = paid.profile_vectors(geometry,history)
        centered,fc,hac = paid.profile_vectors(center_geometry,center_history)
        first = self.weighted_pair(paid.vector_add(current,centered,-1),
                                   paid.vector_add(current,centered),h,dg)
        deltaq = [h*0,-2*h*dg,hc*hc*dg*dg+(hc-h)*(hc+h)]
        return (first-4*self.pair(paid.multiply_position(fc,deltaq),hac))/(64*h)


class CenterCoordinates(paid.FiniteCoordinates):
    def center(self,parameters):
        geometry,history,_,length = super().center(parameters)
        zeta = [parameters[6],self.nuhat_scale*parameters[7],
                self.nuhat_scale*parameters[8]]
        return geometry,history,zeta,length


def center_pairing(geometry,center_geometry,zeta):
    h,k,eta,_,_ = geometry
    hc = center_geometry[0]
    dg = h*eta-k
    return ((1+dg*dg)*zeta[0]/(4*h)+dg*zeta[1]/2
            +((h-hc)*(h+hc)-hc*hc*dg*dg)*zeta[2]/(4*h))


def actual_nubar(center_geometry,zeta):
    h = center_geometry[0]
    return [zeta[0]-h*h*zeta[2],zeta[1],zeta[2]]


class CenteredRHS(paid.FullC2RHS):
    def __init__(self,coefficients,potential,coordinate_guard):
        super().__init__(coefficients,potential)
        self.coordinates = CenterCoordinates(self.nuhat_scale)
        self.coordinate_guard = coordinate_guard

    def one(self,state,parameters,derivatives=False):
        self.direct_state_evaluations += 1
        self.derivative_state_evaluations += int(derivatives)
        if not np.all(np.isfinite(state)) or not np.all(np.isfinite(parameters)):
            raise FloatingPointError("nonfinite_coordinate")
        if max(np.max(np.abs(state)),np.max(np.abs(parameters)))>self.coordinate_guard:
            raise FloatingPointError("declared_finite_coordinate_search_guard")
        jets = self.jets(state,parameters,29 if derivatives else 0)
        ys,ps = jets[:19],jets[19:]
        geo,chart = self.coordinates.physical(ys)
        center_geo,center_a,zeta,length = self.coordinates.center(ps)
        h,k,eta,gamma,upsilon = geo
        aa = ys[5:13]
        neg = [h,-k,-eta,-gamma,upsilon]
        aneg = [sign*value for sign,value in zip(JPAR,aa)]
        op = self.coefficients.evaluate_jets(geo,aa)
        om = self.coefficients.evaluate_jets(neg,aneg)
        wp,wm = paid.weights(geo),paid.weights(neg)
        dep = self.potential.center_difference(geo,aa,center_geo,center_a)
        dem = self.potential.center_difference(neg,aneg,center_geo,center_a)
        hp,kp,hm,km = op[1],op[2],om[1],om[2]
        determinant = -hp*km-hm*kp
        if not (hp.value<0 and hm.value<0 and kp.value>0 and km.value>0
                and determinant.value>0):
            raise FloatingPointError("original_Ch_Ck_domain")
        fp = op[0]-4*paid.dot(wp,ys[13:16])-4*dep-2*center_pairing(geo,center_geo,zeta)
        fm = om[0]-4*paid.dot(wm,ys[16:19])-4*dem-2*center_pairing(neg,center_geo,zeta)
        acc = (km*fp+kp*fm)/determinant
        bcc = (hm*fp-hp*fm)/determinant
        qg = 1+(h*eta-k)**2
        out = [gamma/chart[0],upsilon/chart[1],upsilon/(2*h*chart[2]),
               acc/chart[3],bcc/chart[4]]
        out.extend(paid.density(geo))
        out.extend((op[3+3*j]+acc*op[4+3*j]+bcc*op[5+3*j])/qg**2 for j in range(3))
        out.extend(-(om[3+3*j]+acc*om[4+3*j]-bcc*om[5+3*j])/qg**2 for j in range(3))
        value,jac = paid.values_and_jacobian([length*v for v in out])
        if not np.all(np.isfinite(value)) or not np.all(np.isfinite(jac)):
            raise FloatingPointError("nonfinite_complete_original_equation")
        return np.asarray(value,dtype=float),np.asarray(jac,dtype=float)


def geometric_guide(parameters,x):
    """One genuine bounded geometry family; it is not a ruling solution."""
    h0,peak,blend,b3,b5,cap,length = parameters
    theta = np.pi*x/2
    w = np.pi/2
    ss,cc = np.sin(theta),np.cos(theta)
    shape = blend*ss**2+(1-blend)*ss**4
    sx = w*(2*blend*ss*cc+4*(1-blend)*ss**3*cc)
    sxx = w*w*(2*blend*(cc*cc-ss*ss)
                    +4*(1-blend)*(3*ss*ss*cc*cc-ss**4))
    norm = 1+np.sqrt(b3*b3+1.e-8)+np.sqrt(b5*b5+1.e-8)
    q = (ss+b3*np.sin(3*theta)+b5*np.sin(5*theta))/norm
    qx = w*(cc+3*b3*np.cos(3*theta)+5*b5*np.cos(5*theta))/norm
    qxx = -w*w*(ss+9*b3*np.sin(3*theta)+25*b5*np.sin(5*theta))/norm
    h = h0+(peak-h0)*shape
    k = cap*q
    hx,hxx = (peak-h0)*sx,(peak-h0)*sxx
    kx,kxx = cap*qx,cap*qxx
    eta = cumulative_simpson(kx/(2*h),x=x,initial=0.)
    geometry = np.array([h,k,eta,hx/length,kx/length])
    return geometry,hxx/length**2,kxx/length**2


def matrix_rates(geometry):
    h,k,eta,gamma,upsilon = geometry
    dg,ds = h*eta-k,gamma*eta-upsilon/2
    qg = 1+dg*dg
    a1 = 2*k*eta-(k*k+1)/h
    a0 = k*eta*eta-(k*k+1)*eta/h
    common = gamma*qg/h-2*dg*ds
    return np.array([
        -k*qg/(2*h),-k*dg,-k*h/2,
        (h*a1-gamma*gamma/h**2)/8,
        (a1*qg+gamma*common/h**2)/(8*h),
        (a1*dg-gamma*ds/h**2)/4,
        (a0*dg-ds*ds/h**2)/4,
        (a0*qg+ds*common/h**2)/(8*h)])


def fit_real_even_guide(args):
    x = np.linspace(0.,1.,args.guide_nodes)
    initial = np.array([1.05,2.8,.35,0.,0.,1.8,4.])
    lower = [.85,2.4,.02,-.75,-.4,.8,3.]
    upper = [1.2,2.95,.98,.75,.4,1.98,7.5]
    best = {"parameters":initial.copy(),"score":float("inf")}
    calls = 0
    def residual(parameters):
        nonlocal calls
        calls += 1
        geo,_,_ = geometric_guide(parameters,x)
        rates = matrix_rates(geo)
        means = simpson(rates,x=x,axis=1)
        core = means[EVEN]*np.array([1.,8.,8*1.05**2,4*1.05**2])
        bounds = np.array([np.max(np.abs(geo[2]))-.95,
                           np.max(np.abs(geo[3]))-5.8,
                           np.max(np.abs(geo[4]))-5.8])
        value = np.r_[core,20*np.maximum(0.,bounds)]
        if np.all(bounds<0) and np.linalg.norm(core)<best["score"]:
            best.update(parameters=parameters.copy(),score=float(np.linalg.norm(core)))
        return value
    started = time.time()
    first = residual(initial)
    result = least_squares(residual,initial,bounds=(lower,upper),method="trf",
                           jac="3-point",x_scale="jac",tr_solver="lsmr",
                           max_nfev=args.guide_max_nfev,
                           ftol=1.e-10,xtol=1.e-10,gtol=1.e-10)
    chosen = best["parameters"]
    coarse = residual(chosen)
    fine_x = np.linspace(0.,1.,2*(args.guide_nodes-1)+1)
    fine_geo,_,_ = geometric_guide(chosen,fine_x)
    fine_even = simpson(matrix_rates(fine_geo),x=fine_x,axis=1)[EVEN]
    record = {"elapsed_seconds":time.time()-started,
              "status":int(result.status),"success":bool(result.success),
              "message":str(result.message),"nfev":int(result.nfev),
              "actual_residual_calls":calls,"parameters":chosen.tolist(),
              "initial_weighted_even_and_box":first.tolist(),
              "chosen_weighted_even_and_box":coarse.tolist(),
              "fine_actual_even_integrals":(chosen[-1]*fine_even).tolist(),
              "best_feasible_guide_norm":best["score"],
              "ruling_solution_claim":False,"exact_moment_root_claim":False}
    emit("R590_TRUST_REAL_GUIDE",record)
    return chosen,record


def build_real_seed(rhs,guide,args):
    count = max(args.history_nodes,4*args.intervals+1)
    if (count-1)%(2*args.intervals):
        count = (int(np.ceil((count-1)/(2*args.intervals)))*(2*args.intervals)+1)
    x = np.linspace(0.,1.,count)
    geometry,acc,bcc = geometric_guide(guide,x)
    length = guide[-1]
    rates = matrix_rates(geometry)
    total = length*simpson(rates,x=x,axis=1)
    ac = np.zeros(8)
    ac[ODD] = -total[ODD]
    history = ac[:,None]+length*cumulative_simpson(rates,x=x,axis=1,initial=0.)
    h0,v0 = geometry[0,0],geometry[4,0]
    prepared = np.array([v0/(12*h0),0.,v0/(16*h0**3),v0/(24*h0)])
    correction = ac[ODD]-prepared
    if np.max(np.abs(correction))>=float(rhs.coordinates.acap):
        raise FloatingPointError("The actual integrated odd center exceeds the declared open parameter box")
    par = np.zeros(10)
    par[0] = np.tan(np.pi*(h0-float(rhs.coordinates.hmid))/(2*float(rhs.coordinates.hcap)))
    par[1] = np.tan(np.pi*v0/(2*float(rhs.coordinates.vcap)))
    par[2:6] = np.tan(np.pi*correction/(2*float(rhs.coordinates.acap)))
    par[9] = np.tan(np.pi*(length-float(rhs.coordinates.lmid))/(2*float(rhs.coordinates.lcap)))
    center,center_a,zeta,ll = rhs.coordinates.center([constant(v,0) for v in par])
    center_values = np.asarray([v.value for v in center_a],dtype=LD)
    opcenter = rhs.coefficients.evaluate(tuple(v.value for v in center),center_values)
    par[6] = float((opcenter[0]+opcenter[1]*acc[0])/(2*paid.old.weights(h0,0.,0.)[0]))
    rho_plus,rho_minus,outputs_plus,outputs_minus = [],[],[],[]
    for i in range(count):
        geo = tuple(geometry[:,i])
        neg = (geo[0],-geo[1],-geo[2],-geo[3],geo[4])
        op = rhs.coefficients.evaluate(geo,history[:,i])
        om = rhs.coefficients.evaluate(neg,JPAR*history[:,i])
        outputs_plus.append(op)
        outputs_minus.append(om)
        rho_plus.append(rhs.coefficients.history_rhs(op,geo,acc[i],bcc[i]))
        rho_minus.append(-rhs.coefficients.history_rhs(om,neg,acc[i],-bcc[i]))
    state = np.zeros((19,count))
    for i in range(count):
        state[:5,i] = rhs.coordinates.encode(geometry[:,i])
    state[5:13] = history
    state[13:16] = length*cumulative_simpson(np.asarray(rho_plus).T,x=x,axis=1,initial=0.)
    state[16:19] = length*cumulative_simpson(np.asarray(rho_minus).T,x=x,axis=1,initial=0.)
    # One pair of constant global gauge coordinates, not a per-node control.
    # Their center pairing vanishes, so this retains the paid center ruling.
    gauge_rows,gauge_targets = [],[]
    hc = center[0].value
    for i in range(count):
        h,k,eta,gamma,upsilon = geometry[:,i]
        for sign,outputs,rho in ((1,outputs_plus[i],state[13:16,i]),
                                  (-1,outputs_minus[i],state[16:19,i])):
            gg = [constant(v,0) for v in (h,sign*k,sign*eta,sign*gamma,upsilon)]
            ah = history[:,i] if sign==1 else JPAR*history[:,i]
            aj = [constant(v,0) for v in ah]
            dep = rhs.potential.center_difference(gg,aj,center,center_a).value
            dg = h*(sign*eta)-sign*k
            weights = paid.old.weights(h,sign*k,sign*eta)
            b2 = ((h-hc)*(h+hc)-hc*hc*dg*dg)/(4*h)
            target = (outputs[0]+outputs[1]*acc[i]+sign*outputs[2]*bcc[i]
                      -4*weights@rho-4*dep-2*weights[0]*par[6])
            gauge_rows.append([dg,2*b2])
            gauge_targets.append(target)
    gauge_matrix = np.asarray(gauge_rows,dtype=float)*float(rhs.nuhat_scale)
    gauge_vector = np.asarray(gauge_targets,dtype=float)
    fitted,_,rank,singular_values = np.linalg.lstsq(gauge_matrix,gauge_vector,rcond=None)
    gauge_fit_used = bool(np.all(np.isfinite(fitted))
                          and np.max(np.abs(fitted))<rhs.coordinate_guard)
    if gauge_fit_used:
        par[7:9] = fitted
    else:
        fitted = np.zeros(2)
    gauge_after = gauge_vector-gauge_matrix@par[7:9]
    indices = np.linspace(0,count-1,2*args.intervals+1,dtype=int)
    cp = rhs.potential.energy(center,center_a).value
    eo = rhs.coefficients.evaluate(tuple(v.value for v in center),center_values)[16:19]
    nubar = np.array([par[6]-hc*hc*rhs.nuhat_scale*par[8],
                     rhs.nuhat_scale*par[7],rhs.nuhat_scale*par[8]],dtype=LD)
    emit("R590_TRUST_REAL_SEED",{
        "guide_parameters":guide.tolist(),"history_nodes":count,
        "odd_center_from_actual_M_integral":ac[ODD].tolist(),
        "center_v0":float(v0),"prepared_center_correction":correction.tolist(),
        "center_E":np.asarray(eo,dtype=float).tolist(),
        "center_positive_energy":float(cp),"nubar":np.asarray(nubar,dtype=float).tolist(),
        "nuhat":np.asarray(nubar-2*eo,dtype=float).tolist(),
        "center_null_parameter_unit":float(rhs.nuhat_scale),
        "global_two_column_gauge_seed_rank":int(rank),
        "global_two_column_gauge_seed_used":gauge_fit_used,
        "global_two_column_gauge_seed_singular_values":singular_values.tolist(),
        "true_guide_ruling_peak_before_two_constant_controls":float(np.max(np.abs(gauge_vector))),
        "true_guide_ruling_peak_after_two_constant_controls":float(np.max(np.abs(gauge_after))),
        "true_guide_ruling_l2_before_two_constant_controls":float(np.linalg.norm(gauge_vector)),
        "true_guide_ruling_l2_after_two_constant_controls":float(np.linalg.norm(gauge_after)),
        "fine_eight_endpoint":history[:,-1].tolist(),
        "boundary_max_abs":float(np.max(np.abs(rhs.boundary(state[:,0],state[:,-1],par)))),
        "center_kinematic_ruling_target_accelerations":[float(acc[0]),float(bcc[0])],
        "whole_guide_ruling_solution_claim":False})
    return x[indices],state[:,indices],par


class StagedCollocation:
    """The same cubic Lobatto equations, without eliminating midpoint states."""
    def __init__(self,rhs,x,flow_units=None):
        self.rhs,self.x = rhs,np.asarray(x,dtype=float)
        if len(x)%2!=1 or len(x)<3:
            raise ValueError("An explicit-stage mesh has 2m+1 ordered points")
        self.h = self.x[2::2]-self.x[:-2:2]
        self.intervals = len(self.h)
        self.size = 19*len(x)+10
        self.flow_units = None if flow_units is None else np.asarray(flow_units,dtype=float)

    def pack(self,y,p):
        return np.r_[y.ravel(order="F"),p]

    def unpack(self,z):
        return z[:-10].reshape((19,len(self.x)),order="F"),z[-10:]

    def evaluate(self,z):
        y,p = self.unpack(z)
        f = self.rhs(self.x,y,p)
        mid = y[:,1::2]-(y[:,:-2:2]+y[:,2::2])/2+self.h*(f[:,2::2]-f[:,:-2:2])/8
        total = y[:,2::2]-y[:,:-2:2]-self.h*(f[:,:-2:2]+4*f[:,1::2]+f[:,2::2])/6
        bc = self.rhs.boundary(y[:,0],y[:,-1],p)
        residual = np.r_[np.column_stack([
            np.r_[mid[:,i]/self.h[i],total[:,i]/self.h[i]]
            for i in range(self.intervals)]).ravel(order="F"),bc]
        if not np.all(np.isfinite(residual)):
            raise FloatingPointError("nonfinite_complete_collocation_residual")
        if self.flow_units is None:
            self.flow_units = np.maximum(1.,np.max(np.abs(f),axis=1))
        weights = np.r_[np.tile(np.r_[1/self.flow_units,1/self.flow_units],
                                 self.intervals),np.ones(29)]
        return {"z":z,"y":y,"p":p,"f":f,"residual":residual,"weights":weights,
                "weighted":weights*residual,"bc":bc}

    def jacobian(self,evaluation):
        y,p = evaluation["y"],evaluation["p"]
        fy,fp = self.rhs.jacobian(self.x,y,p)
        bl,br,bp = self.rhs.boundary_jacobian(y[:,0],y[:,-1],p)
        rows,cols,values = [],[],[]
        def block(row,column,matrix):
            rr,cc = np.indices(matrix.shape)
            rows.extend((row+rr.ravel()).tolist())
            cols.extend((column+cc.ravel()).tolist())
            values.extend(matrix.ravel().tolist())
        eye = np.eye(19)
        for i,h in enumerate(self.h):
            l,m,r = 2*i,2*i+1,2*i+2
            row = 38*i
            block(row,19*l,-eye/(2*h)-fy[:,:,l]/8)
            block(row,19*m,eye/h)
            block(row,19*r,-eye/(2*h)+fy[:,:,r]/8)
            block(row,self.size-10,(fp[:,:,r]-fp[:,:,l])/8)
            block(row+19,19*l,-eye/h-fy[:,:,l]/6)
            block(row+19,19*m,-2*fy[:,:,m]/3)
            block(row+19,19*r,eye/h-fy[:,:,r]/6)
            block(row+19,self.size-10,-(fp[:,:,l]+4*fp[:,:,m]+fp[:,:,r])/6)
        row = 38*self.intervals
        block(row,0,bl)
        block(row,19*(len(self.x)-1),br)
        block(row,self.size-10,bp)
        matrix = coo_matrix((values,(rows,cols)),shape=(self.size,self.size)).tocsc()
        matrix.eliminate_zeros()
        if not np.all(np.isfinite(matrix.data)):
            raise FloatingPointError("nonfinite_actual_sparse_Jacobian")
        return matrix

    def physical_spline(self,evaluation):
        return CubicHermiteSpline(self.x[::2],evaluation["y"][:,::2],
                                 evaluation["f"][:,::2],axis=1)


def original_shift(coefficients,geometry,history):
    outputs = coefficients.evaluate(geometry,history)
    h,k,eta,_,_ = geometry
    w0 = (1+(h*eta-k)**2)/(4*h)
    result = np.asarray(outputs[12:15]/4,dtype=LD)
    result[0] -= outputs[15]/(4*w0)
    return result


def physical_report(rhs,system,evaluation):
    """Original physical equations on the actual C1 interpolant, no defect scaling."""
    sol = system.physical_spline(evaluation)
    x = system.x
    state = sol(x)
    center,ca,zeta,ll = rhs.coordinates.center([constant(v,0) for v in evaluation["p"]])
    length = float(ll.value)
    cg = tuple(v.value for v in center)
    av = np.asarray([v.value for v in ca],dtype=LD)
    nb = np.asarray([v.value for v in actual_nubar(center,zeta)],dtype=LD)
    ec = rhs.coefficients.evaluate(cg,av)[16:19]
    rc = original_shift(rhs.coefficients,cg,av)
    nhat = nb-2*ec
    deriv = sol(x,1)/length
    kin,mat,regular,original,ruling,direct = [],[],[],[],[],[]
    energies,geometries = [],[]
    for i in range(len(x)):
        geo,chart = rhs.coordinates.physical([constant(v,0) for v in state[:,i]])
        gp = tuple(v.value for v in geo)
        h,k,eta,gamma,upsilon = gp
        gd = np.asarray([v.value for v in chart],dtype=LD)*deriv[:5,i]
        aa,bb = gd[3:5]
        ah = np.asarray(state[5:13,i],dtype=LD)
        gm = (h,-k,-eta,-gamma,upsilon)
        neg = [constant(v,0) for v in gm]
        aj,anj = [constant(v,0) for v in ah],[constant(v,0) for v in JPAR*ah]
        op,om = rhs.coefficients.evaluate(gp,ah),rhs.coefficients.evaluate(gm,JPAR*ah)
        wp,wm = paid.old.weights(h,k,eta),paid.old.weights(h,-k,-eta)
        ep,em = rhs.potential.energy(geo,aj),rhs.potential.energy(neg,anj)
        dep = rhs.potential.center_difference(geo,aj,center,ca).value
        dem = rhs.potential.center_difference(neg,anj,center,ca).value
        zp,zm = center_pairing(geo,center,zeta).value,center_pairing(neg,center,zeta).value
        ruling.append([op[0]+op[1]*aa+op[2]*bb-4*wp@state[13:16,i]-4*dep-2*zp,
                       om[0]+om[1]*aa-om[2]*bb-4*wm@state[16:19,i]-4*dem-2*zm])
        direct.append([op[0]+op[1]*aa+op[2]*bb-4*wp@state[13:16,i]-4*ep.value-2*wp@nhat,
                       om[0]+om[1]*aa-om[2]*bb-4*wm@state[16:19,i]-4*em.value-2*wm@nhat])
        kin.append(gd[:3]-np.array([gamma,upsilon,upsilon/(2*h)]))
        md = paid.old.core.matrix_density(*gp)
        mat.append(deriv[5:13,i]-md)
        rd = np.r_[deriv[13:16,i]-rhs.coefficients.history_rhs(op,gp,aa,bb),
                   deriv[16:19,i]+rhs.coefficients.history_rhs(om,gm,aa,-bb)]
        regular.append(rd)
        model_geo = np.array([gamma,upsilon,upsilon/(2*h),aa,bb])
        correction = []
        for sg,sa in ((np.ones(5),np.ones(8)),(np.array([1.,-1.,-1.,-1.,1.]),JPAR)):
            gj = [Jet(v*s,[dc*s,dm*s]) for v,dc,dm,s in zip(gp,gd,model_geo,sg)]
            ajs = [Jet(v*s,[dc*s,dm*s]) for v,dc,dm,s in zip(ah,deriv[5:13,i],md,sa)]
            ej = rhs.coefficients.evaluate_jets(gj,ajs)
            qgj = 1+(gj[0]*gj[2]-gj[1])**2
            correction.extend((ej[16+j]/qgj).derivative[0]-(ej[16+j]/qgj).derivative[1]
                              for j in range(3))
        original.append(rd+np.asarray(correction,dtype=LD))
        energies.append([ep.value,em.value])
        geometries.append(gp)
    end = state[:,-1]
    last_geo,_ = rhs.coordinates.physical([constant(v,0) for v in end])
    gv = tuple(v.value for v in last_geo)
    negv = (gv[0],-gv[1],-gv[2],-gv[3],gv[4])
    end_a = np.asarray(end[5:13],dtype=LD)
    qge = 1+(gv[0]*gv[2]-gv[1])**2
    eplus = rhs.coefficients.evaluate(gv,end_a)[16:19]/qge
    eminus = rhs.coefficients.evaluate(negv,JPAR*end_a)[16:19]/qge
    rp = original_shift(rhs.coefficients,gv,end_a)
    rm = original_shift(rhs.coefficients,negv,JPAR*end_a)
    sp,sm = end[13:16]+eplus-ec,end[16:19]+eminus-ec
    initial = state[:,0]
    first_geo,_ = rhs.coordinates.physical([constant(v,0) for v in initial])
    first = tuple(v.value for v in first_geo)
    first_minus = (first[0],-first[1],-first[2],-first[3],first[4])
    initial_t = []
    for gg,ah,rho in ((first,initial[5:13],initial[13:16]),
                       (first_minus,JPAR*initial[5:13],initial[16:19])):
        qgi = 1+(gg[0]*gg[2]-gg[1])**2
        ei = rhs.coefficients.evaluate(gg,ah)[16:19]/qgi
        ri = original_shift(rhs.coefficients,gg,ah)
        initial_t.append(np.asarray(rho+ei-ec-ri+rc,dtype=float).tolist())
    def maximum(values):
        return float(np.max(np.abs(np.asarray(values,dtype=LD))))
    ranges = np.asarray(geometries,dtype=LD).T
    return {"physical_samples":len(x),"actual_center_height":float(cg[0]),
            "actual_length":length,"actual_center_v0":float(cg[4]),
            "actual_center_Aodd":np.asarray(av[ODD],dtype=float).tolist(),
            "sampled_geometry_ranges":{name:[float(row.min()),float(row.max())]
               for name,row in zip(("h","k","eta","gamma","upsilon"),ranges)},
            "sampled_kinematic_defect":maximum(kin),
            "sampled_matrix_defect":maximum(mat),"sampled_C2_history_defect":maximum(regular),
            "sampled_original_sigma_history_defect":maximum(original),
            "sampled_original_factored_ruling_defect":maximum(ruling),
            "sampled_original_direct_square_ruling_defect":maximum(direct),
            "factored_vs_direct_original_ruling_discrepancy":maximum(np.asarray(ruling)-np.asarray(direct)),
            "sampled_current_positive_energy_max":maximum(energies),
            "center_E":np.asarray(ec,dtype=float).tolist(),"center_r":np.asarray(rc,dtype=float).tolist(),
            "nubar":np.asarray(nb,dtype=float).tolist(),"nuhat":np.asarray(nhat,dtype=float).tolist(),
            "actual_fixed_nu":np.asarray(nb-2*rc,dtype=float).tolist(),
            "eight_endpoint":np.asarray(end_a,dtype=float).tolist(),
            "two_velocity_endpoint":[float(v) for v in gv[3:]],
            "endpoint_E_plus":np.asarray(eplus,dtype=float).tolist(),
            "endpoint_E_minus":np.asarray(eminus,dtype=float).tolist(),
            "recovered_center_t_plus_minus":initial_t,
            "three_T_projection_difference":np.asarray(sp-sm-rp+rm,dtype=float).tolist(),
            "actual_reanchored_chi_Gram":np.asarray(nb+2*sm-2*rm,dtype=float).tolist(),
            "full_reanchored_T_period_not_evaluated":True,
            "continuous_root_or_geometry_certificate":False}


def checkpoint(rhs,system,evaluation,iteration,level,trust,damping,reason):
    raw = evaluation["residual"]
    block = raw[:-29].reshape((system.intervals,2,19))
    data = {"schema":"r590-staged-trust-complete-state-v1","level":level,
            "iteration":iteration,"reason":reason,"clock_nodes":system.x.tolist(),
            "state_rows":evaluation["y"].tolist(),"parameters":evaluation["p"].tolist(),
            "fixed_flow_row_units":system.flow_units.tolist(),
            "fixed_center_null_parameter_unit":float(rhs.nuhat_scale),
            "trust_radius":trust,"damping":damping,
            "weighted_merit":float(.5*np.dot(evaluation["weighted"],evaluation["weighted"])),
            "actual_collocation_component_max":np.max(np.abs(block),axis=(0,1)).tolist(),
            "actual_boundary_residual":evaluation["bc"].tolist(),
            "actual_collocation_max":float(np.max(np.abs(raw[:-29]))),
            "actual_boundary_max":float(np.max(np.abs(evaluation["bc"])))}
    canonical = json.dumps(data,sort_keys=True,separators=(",",":"),allow_nan=False)
    digest = hashlib.sha256(canonical.encode()).hexdigest()
    emit("R590_TRUST_ACCEPTED_STATE",{"state_sha256":digest,"complete_state":data})
    try:
        with np.errstate(over="raise",divide="raise",invalid="raise"):
            report = physical_report(rhs,system,evaluation)
        json.dumps(report,allow_nan=False)
    except (FloatingPointError,ValueError,OverflowError) as exc:
        report = {"inspection_failure":{"type":type(exc).__name__,"message":str(exc)},
                  "complete_finite_node_state_retained":True,
                  "physical_defect_not_available":True}
    emit("R590_TRUST_PHYSICAL",{"level":level,"iteration":iteration,
                               "state_sha256":digest,"readout":report})
    return report


def solve_staged(rhs,x,y,p,args,level=0,flow_units=None):
    system = StagedCollocation(rhs,x,flow_units)
    current = system.evaluate(system.pack(y,p))
    trust,damping = args.trust_radius,args.damping
    report = checkpoint(rhs,system,current,0,level,trust,damping,"initial_true_history_seed")
    accepted = rejected = 0
    status = "iteration_limit_with_finite_state"
    started = time.time()
    for iteration in range(1,args.newton_iterations+1):
        raw = current["residual"]
        if np.max(np.abs(raw[:-29]))<=args.collocation_tol and np.max(np.abs(raw[-29:]))<=args.bc_tol:
            status = "actual_discrete_equations_converged"
            break
        try:
            jac = system.jacobian(current)
        except (FloatingPointError,ValueError,OverflowError) as exc:
            status = "finite_state_retained_after_Jacobian_failure"
            emit("R590_TRUST_LINEAR_FAILURE",{"type":type(exc).__name__,"message":str(exc)})
            break
        weighted_jac = diags(current["weights"])@jac
        column_max = np.maximum(1.,np.asarray(abs(weighted_jac).max(axis=0).toarray()).ravel())
        normalized = weighted_jac@diags(1/column_max)
        norms = np.sqrt(np.asarray(normalized.power(2).sum(axis=0)).ravel())
        columns = (1/column_max)/np.maximum(1.,norms)
        matrix = weighted_jac@diags(columns)
        residual = current["weighted"]
        merit = .5*np.dot(residual,residual)
        took_step = False
        for trial in range(args.trial_limit):
            try:
                linear = lsmr(matrix,-residual,damp=np.sqrt(damping),
                              atol=1.e-11,btol=1.e-11,maxiter=args.linear_iterations)
            except (FloatingPointError,ValueError,OverflowError,RuntimeError) as exc:
                emit("R590_TRUST_LINEAR_FAILURE",{
                    "level":level,"iteration":iteration,"trial":trial,
                    "type":type(exc).__name__,"message":str(exc),
                    "complete_finite_state_retained":True})
                break
            step = linear[0]
            rms_step = np.linalg.norm(step)/np.sqrt(len(step))
            if rms_step>trust:
                step *= trust/rms_step
            predicted = merit-.5*np.linalg.norm(residual+matrix@step)**2
            candidate_z = current["z"]+columns*step
            error = None
            candidate = None
            try:
                candidate = system.evaluate(candidate_z)
                candidate_merit = .5*np.dot(candidate["weighted"],candidate["weighted"])
                if not np.isfinite(candidate_merit):
                    raise FloatingPointError("nonfinite_weighted_merit")
                actual = merit-candidate_merit
                ratio = actual/predicted if predicted>0 else -np.inf
            except (FloatingPointError,ValueError,OverflowError) as exc:
                candidate = None
                candidate_merit,actual,ratio = None,None,None
                error = {"type":type(exc).__name__,"message":str(exc)}
            acceptable = (candidate is not None and predicted>0 and actual>0
                          and np.isfinite(ratio) and ratio>=args.acceptance_ratio)
            emit("R590_TRUST_TRIAL",{
                "level":level,"iteration":iteration,"trial":trial,
                "accepted":bool(acceptable),"current_merit":float(merit),
                "trial_merit":None if candidate_merit is None else float(candidate_merit),
                "predicted_decrease":float(predicted) if np.isfinite(predicted) else None,
                "actual_decrease":None if actual is None else float(actual),
                "actual_predicted_ratio":None if ratio is None or not np.isfinite(ratio) else float(ratio),
                "step_rms_before_trust_limit":float(rms_step) if np.isfinite(rms_step) else None,
                "trust_radius":trust,"damping":damping,
                "lsmr_stop":int(linear[1]),"lsmr_iterations":int(linear[2]),
                "error":error})
            if acceptable:
                current = candidate
                accepted += 1
                if ratio>.75:
                    trust = min(args.maximum_trust,2*trust)
                    damping = max(1.e-14,damping/2)
                elif ratio<.25:
                    trust *= .75
                    damping *= 2
                report = checkpoint(rhs,system,current,iteration,level,trust,damping,"accepted_actual_merit_decrease")
                took_step = True
                break
            rejected += 1
            trust *= .5
            damping = min(1.e14,4*damping)
        if not took_step:
            status = "no_acceptable_step_complete_finite_state_retained"
            break
    if (np.max(np.abs(current["residual"][:-29]))<=args.collocation_tol
            and np.max(np.abs(current["bc"]))<=args.bc_tol):
        status = "actual_discrete_equations_converged"
    summary = {"level":level,"status":status,"accepted_steps":accepted,"rejected_trials":rejected,
               "elapsed_seconds":time.time()-started,"explicit_stage_nodes":len(system.x),
               "unknowns":system.size,"actual_collocation_max":float(np.max(np.abs(current["residual"][:-29]))),
               "actual_boundary_max":float(np.max(np.abs(current["bc"]))),
               "weighted_merit":float(.5*np.dot(current["weighted"],current["weighted"])),
               "rhs_calls":rhs.calls,"rhs_points":rhs.points,"jacobian_calls":rhs.jacobian_calls,
               "all_direct_state_evaluations":rhs.direct_state_evaluations,
               "all_derivative_state_evaluations":rhs.derivative_state_evaluations,
               "continuous_root_claim":False}
    emit("R590_TRUST_LEVEL_FINAL",summary)
    return system,current,summary,report


def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("New science is restricted to the declared public Actions repository")
    parser = argparse.ArgumentParser()
    parser.add_argument("--order",type=int,default=192)
    parser.add_argument("--gap-order",type=int,default=8)
    parser.add_argument("--guide-nodes",type=int,default=257)
    parser.add_argument("--guide-max-nfev",type=int,default=80)
    parser.add_argument("--history-nodes",type=int,default=513)
    parser.add_argument("--intervals",type=int,default=32)
    parser.add_argument("--newton-iterations",type=int,default=30)
    parser.add_argument("--trial-limit",type=int,default=12)
    parser.add_argument("--linear-iterations",type=int,default=1200)
    parser.add_argument("--trust-radius",type=float,default=.5)
    parser.add_argument("--maximum-trust",type=float,default=4.)
    parser.add_argument("--damping",type=float,default=1.e-4)
    parser.add_argument("--acceptance-ratio",type=float,default=1.e-4)
    parser.add_argument("--coordinate-guard",type=float,default=1.e6)
    parser.add_argument("--collocation-tol",type=float,default=1.e-7)
    parser.add_argument("--bc-tol",type=float,default=1.e-10)
    args = parser.parse_args()
    started = time.time()
    labels,rows = rebuild_known_rows()
    grid = paid.old.ReferenceGrid(args.order,args.gap_order,5.)
    coefficients = paid.DifferentiableCoefficients(labels,rows,grid)
    expected = "602b47988d4ef51e472001532e633efe24bc6bec88c62c0d1876c02271064286"
    if args.order==192 and coefficients.stats["coefficient_float64_sha256"]!=expected:
        raise RuntimeError("Necessary rebuilt coefficient table differs from the already paid exact source")
    potential = FactoredPotential(grid)
    rhs = CenteredRHS(coefficients,potential,args.coordinate_guard)
    emit("R590_TRUST_FIXED_INPUT",{
        "coefficients":coefficients.stats,"positive_Gram":potential.stats,
        "paid_identity_gate_repeated":False,"paid_RHS_direction_gate_repeated":False,
        "paid_quadrature_comparison_repeated":False,
        "same_physical_R578_input":True,"full_potential_coefficient":1,
        "fixed_center_null_parameter_unit":float(rhs.nuhat_scale),
        "explicit_midpoint_states":True,
        "all_29_original_boundary_conditions_retained":True})
    guide,guide_record = fit_real_even_guide(args)
    x,y,p = build_real_seed(rhs,guide,args)
    system,current,summary,report = solve_staged(rhs,x,y,p,args)
    if summary["status"]=="actual_discrete_equations_converged":
        newx = np.linspace(0.,1.,4*args.intervals+1)
        newy = system.physical_spline(current)(newx)
        system,current,summary,report = solve_staged(rhs,newx,newy,current["p"],args,1,system.flow_units)
    emit("R590_TRUST_DONE",{
        "elapsed_seconds":time.time()-started,"last_status":summary["status"],
        "finite_state_preserved":True,"exact_root_rank_pose_period_claim":False,
        "README_completion_claim":False})


if __name__=="__main__":
    main()
