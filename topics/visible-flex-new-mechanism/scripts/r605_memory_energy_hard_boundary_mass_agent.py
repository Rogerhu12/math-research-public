#!/usr/bin/env python3
"""R605: whole-path memory/energy input and exact-boundary original mass BVP.

The R598 mother, R590 full positive square, both complete histories, fixed
gauge and original physical residuals are unchanged. Only public Actions
executes science. No paid identity, derivative or old guide fit is replayed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import time

import numpy as np
from scipy.integrate import cumulative_simpson, simpson
from scipy.optimize import least_squares
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import lsmr

import r598_wide_mother_prepared_mass_bvp_agent as base
import r603_vtwo_center_mass_continuation_agent as interface

previous, paid = base.previous, base.paid
LD, ODD, JPAR, emit = base.LD, base.ODD, base.JPAR, base.emit
THETA_CAP = .6


class MemoryGuide:
    """Eleven real coefficients, with one common integral I on the whole path.

    The analytical I is integral(theta_x/R**2,0,x). Its fixed positive Gauss
    evaluation depends on the requested x, not the other evaluation nodes.
    No independent eta values or per-point gauge controls are introduced.
    """
    def __init__(self, memory_order):
        gx, gw = np.polynomial.legendre.leggauss(memory_order)
        self.memory_x, self.memory_w = (gx+1)/2, gw/2
        self.geometry_calls = self.shape_points = self.memory_integrand_points = 0
        self.root_solves = self.root_integrand_calls = 0

    def shape(self, parameters, x):
        x = np.asarray(x, dtype=float).reshape(-1)
        self.shape_points += len(x)
        height, aa, bb, length = parameters[0], parameters[1:5], parameters[5:10], parameters[10]
        orders = np.arange(4)
        phase = np.pi*orders[:, None]*x[None, :]
        ev = np.sum(aa[:, None]*np.cos(phase), axis=0)
        ex = np.sum(-np.pi*orders[:, None]*aa[:, None]*np.sin(phase), axis=0)
        exx = np.sum(-(np.pi*orders[:, None])**2*aa[:, None]*np.cos(phase), axis=0)
        angle = np.pi*x/2
        sa, ca, frequency = np.sin(angle), np.cos(angle), np.pi/2
        exponential = np.exp(ev)
        q = exponential*sa
        qx = exponential*(frequency*ca+sa*ex)
        qxx = exponential*(-frequency**2*sa+2*frequency*ca*ex+sa*(exx+ex*ex))
        # A=0 and both velocity endpoints force B_plus=B_minus=0 there.
        # One positive leading lambda therefore requires m(1)=0 as well.
        # This radius leaves H to fourth order and returns to H to second
        # order; it is strictly above H only in the open interval.
        fourth, fourth_x = q**4, 4*q**3*qx
        fourth_xx = 12*q*q*qx*qx+4*q**3*qxx
        endpoint_factor = ca*ca
        endpoint_x = -2*frequency*sa*ca
        endpoint_xx = 2*frequency**2*(sa*sa-ca*ca)
        power = fourth*endpoint_factor
        power_x = fourth_x*endpoint_factor+fourth*endpoint_x
        power_xx = (fourth_xx*endpoint_factor+2*fourth_x*endpoint_x
                    +fourth*endpoint_xx)
        radius = height*(1+power/(1+power))
        rx = height*power_x/(1+power)**2
        rxx = height*(power_xx/(1+power)**2-2*power_x**2/(1+power)**3)
        modes = np.arange(3,12,2)
        c1 = -2*length/(np.pi*THETA_CAP)-np.dot(modes, bb)
        coeff = np.r_[c1,bb]
        full_modes = np.r_[1,modes]
        angles = np.pi/2*full_modes[:, None]*x[None, :]
        inner = np.sum(coeff[:, None]*np.sin(angles), axis=0)
        ix = np.sum(np.pi/2*full_modes[:, None]*coeff[:, None]*np.cos(angles), axis=0)
        ixx = np.sum(-(np.pi/2*full_modes[:, None])**2*coeff[:, None]*np.sin(angles), axis=0)
        tangent = np.tanh(inner)
        theta = THETA_CAP*tangent
        tx = THETA_CAP*(1-tangent*tangent)*ix
        txx = THETA_CAP*(1-tangent*tangent)*(ixx-2*tangent*ix*ix)
        return radius,rx,rxx,theta,tx,txx

    def components(self, parameters, x):
        x = np.asarray(x, dtype=float).reshape(-1)
        radius,rx,rxx,theta,tx,txx = self.shape(parameters,x)
        integration_nodes = self.memory_x[:, None]*x[None, :]
        qr,_,_,_,qt,_ = self.shape(parameters,integration_nodes.ravel())
        self.memory_integrand_points += integration_nodes.size
        integrand = (qt/qr**2).reshape(integration_nodes.shape)
        memory = x*np.sum(self.memory_w[:, None]*integrand,axis=0)
        length = parameters[-1]
        d = np.tan(theta)
        qg = 1+d*d
        h = radius/np.cos(theta)
        ar,omega = rx/(length*radius),tx/length
        gamma = h*(ar+d*omega)
        eta = -h*memory
        k = -d-h*h*memory
        upsilon = -2*qg*omega-2*h*gamma*memory
        acc = h*(rxx/(length*length*radius)+2*ar*d*omega
                 +(1+2*d*d)*omega*omega+d*txx/length**2)
        bcc = (-4*d*qg*omega*omega-2*qg*txx/length**2
               -2*(gamma*gamma+h*acc)*memory-2*h*gamma*omega/radius**2)
        return np.array([h,k,eta,gamma,upsilon]),acc,bcc,radius,theta,memory

    def geometry(self, parameters, x, c=None):
        self.geometry_calls += 1
        geometry,acc,bcc,*_ = self.components(parameters,x)
        return geometry,acc,bcc,0.

    def fields(self, parameters, x, c=None):
        geometry,acc,bcc,*_ = self.components(parameters,x)
        h,k,_,gamma,upsilon = geometry
        length = parameters[-1]
        return h,k,length*gamma,length*upsilon,length**2*acc,length**2*bcc,length

    prepared = staticmethod(base.PreparedGuide.prepared)


def leading_energy(geometry,history,centers,weights):
    """R605 B+ and B-; c_* is absorbed into one global positive lambda."""
    h,k,eta,gamma,upsilon = geometry
    d = h*eta-k
    ds = gamma*eta-upsilon/2
    p0,p1,p2,t1,r1,s1,s0,r0 = history
    results = []
    for sign in (1.,-1.):
        y = sign*centers[:,None]
        q = 1+(h[None,:]*y+d[None,:])**2
        ca = (r0[None,:]+(r1+s0)[None,:]*y+1.5*s1[None,:]*y*y
              +(t1-p1/4)[None,:]*y**3-p2[None,:]*y**4/4)
        v2 = -2*ca-q*(gamma[None,:]*y+ds[None,:])/(4*h[None,:]**3)
        results.append(np.sum(weights[:,None]*q*v2*v2,axis=0))
    return np.asarray(results)


def compactness_proxy(geometry,length,x):
    """Only the two reflected strip enclosure and collar focal budget."""
    h,k,eta,gamma,upsilon = geometry
    if np.max(np.abs(eta)) >= 3.5:
        return 1.e3,None
    curvatures,umax = [],0.
    for y in (4.,6.):
        for sign in (1.,-1.):
            u = h/(y+sign*eta)
            aa = h*h-sign*k*u
            den = np.sqrt(aa*aa+u*u)
            s11 = u*(2*h*sign*gamma-upsilon*u)/den**3
            s12 = -h*h/den**2
            curvatures.append((np.abs(s11)+np.sqrt(s11*s11+4*s12*s12))/2)
            umax = max(umax,float(np.max(np.abs(u))))
    curvature = float(np.max(curvatures))
    enclosure = float(2*length*simpson(h*h,x=x)+2*umax)
    product = curvature*enclosure
    return max(0.,product/30.-1.),{
        "sampled_collar_curvature":curvature,"two_strip_path_enclosure":enclosure,
        "curvature_times_enclosure":product,
        "only_new_guide_objective_proxy_not_closed_surface_reach":True}


def fit_memory_guide(args,model):
    started = time.time()
    # Explicit two-dimensional memory loop input, not a mapped old fit.
    initial = np.r_[args.initial_height,.4,0.,0.,0.,
                    -args.initial_length/(np.pi*THETA_CAP),0.,0.,0.,0.,
                    args.initial_length]
    lower = np.r_[.9,-1.,np.full(3,-1.5),np.full(5,-3.),2.1]
    upper = np.r_[1.2,1.,np.full(3,1.5),np.full(5,3.),5.8]
    if not np.all((initial>lower)&(initial<upper)):
        raise ValueError("explicit memory input is outside this finite guide scope")
    x = np.linspace(0.,1.,args.guide_nodes)
    energy_indices = np.arange(0,len(x),args.energy_stride)
    if energy_indices[-1] != len(x)-1:
        energy_indices = np.r_[energy_indices,len(x)-1]
    centers,weights,_ = base.wide_graph()
    centers,weights = centers[1],weights[1]
    matrix_units = np.array([2.,1.,2.,8.,8.,4.,4.,8.])
    best = {"parameters":initial.copy(),"score":float("inf")}
    feasible = {"parameters":None,"score":float("inf")}
    calls = 0
    energy_unit = None

    def read(parameters):
        geometry,a,b,radius,theta,memory = model.components(parameters,x)
        model.geometry_calls += 1
        ac = model.prepared(geometry)
        history = ac[:,None]+parameters[-1]*cumulative_simpson(
            previous.matrix_rates(geometry),x=x,axis=1,initial=0.)
        energy = leading_energy(geometry,history,centers,weights)
        d = geometry[0]*geometry[2]-geometry[1]
        m = (1+d*d)*(radius-parameters[0])*(radius+parameters[0])
        denominator = 2*np.dot(m,m)
        if denominator <= 1.e-24:
            raise FloatingPointError("declared_memory_guide_m_too_small")
        lam = np.dot(m,energy[0]+energy[1])/denominator
        mismatch = energy-lam*m[None,:]
        overflow = np.array([np.max(np.abs(geometry[1]))-1.94,
                             np.max(np.abs(geometry[2]))-.94,
                             np.max(np.abs(geometry[3]))-5.7,
                             np.max(np.abs(geometry[4]))-5.7])
        compact,compact_record = compactness_proxy(geometry,parameters[-1],x)
        return {"geometry":geometry,"acc":a,"bcc":b,"radius":radius,"theta":theta,
                "memory":memory,"history":history,"B":energy,"m":m,"lambda":lam,
                "mismatch":mismatch,"overflow":overflow,"compact":compact,
                "compact_record":compact_record}

    first_data = read(initial)
    energy_unit = max(1.,float(np.max(first_data["B"])))

    def residual(parameters):
        nonlocal calls
        calls += 1
        data = read(parameters)
        moment = matrix_units*data["history"][:,-1]/parameters[-1]
        energy = (args.leading_energy_weight/np.sqrt(len(energy_indices))
                  *data["mismatch"][:,energy_indices].ravel()/energy_unit)
        violation = 25*np.maximum(data["overflow"],0.)
        value = np.r_[moment,energy,violation,args.compactness_weight*data["compact"]]
        score = float(np.linalg.norm(value))
        if score < best["score"]:
            best.update(parameters=parameters.copy(),score=score)
        if np.all(data["overflow"]<0) and score < feasible["score"]:
            feasible.update(parameters=parameters.copy(),score=score)
        return value

    first = residual(initial)
    emit("R605_MEMORY_GUIDE_INPUT",{
        "initial_eleven_parameters":initial.tolist(),"fixed_energy_unit":energy_unit,
        "initial_eight_true_moments":first_data["history"][:,-1].tolist(),
        "initial_global_lambda":float(first_data["lambda"]),
        "initial_B_max":float(np.max(first_data["B"])),
        "initial_leading_mismatch_max":float(np.max(np.abs(first_data["mismatch"]))),
        "first_weighted_residual":first.tolist(),
        "old_fit_or_old_derivative_gate_replayed":False,
        "m_positive_inside_and_zero_at_both_analytical_endpoints":True,
        "eight_moments_paid_in_objective":True,"fixed_gauge_not_replaced_by_local_lambda":True})
    result = least_squares(residual,initial,bounds=(lower,upper),method="trf",
                           jac="3-point",x_scale="jac",max_nfev=args.guide_max_nfev,
                           ftol=1.e-12,xtol=1.e-12,gtol=1.e-12)
    chosen = feasible["parameters"] if feasible["parameters"] is not None else best["parameters"]
    final = residual(chosen)
    data = read(chosen)
    nonzero = data["m"]>1.e-20
    ratio = data["B"][:,nonzero]/data["m"][None,nonzero]
    record = {
        "new_eleven_parameters":chosen.tolist(),"nfev":int(result.nfev),
        "actual_residual_calls":calls,"elapsed_seconds":time.time()-started,
        "status":int(result.status),"message":str(result.message),"optimizer_success":bool(result.success),
        "sampled_legal_guide_found":feasible["parameters"] is not None,
        "eight_true_endpoint_moments":data["history"][:,-1].tolist(),
        "one_global_leading_lambda":float(data["lambda"]),
        "B_plus_minus_max":[float(np.max(v)) for v in data["B"]],
        "leading_equation_original_max":float(np.max(np.abs(data["mismatch"]))),
        "B_over_m_ranges":[[float(v.min()),float(v.max())] for v in ratio],
        "m_positive_sample_min_interior":float(data["m"][1:-1].min()),
        "m_endpoints":data["m"][[0,-1]].tolist(),
        "fixed_leading_objective_unit":energy_unit,"final_weighted_residual":final.tolist(),
        "geometry_ranges":{name:[float(row.min()),float(row.max())] for name,row in zip(
            ("h","k","eta","gamma","upsilon"),data["geometry"])},
        "radius_range":[float(data["radius"].min()),float(data["radius"].max())],
        "theta_range":[float(data["theta"].min()),float(data["theta"].max())],
        "true_memory_endpoint_quadrature":float(data["memory"][-1]),
        "numerical_center_jet":{"h0":float(data["geometry"][0,0]),
                               "h_ss0":float(data["acc"][0]),
                               "k_s0":float(data["geometry"][4,0]),
                               "k_ss0":float(data["bcc"][0])},
        "end_velocity":[float(v) for v in data["geometry"][3:5,-1]],
        "compactness_proxy":data["compact_record"],
        "memory_quadrature_order":args.memory_order,
        "memory_integrand_points":model.memory_integrand_points,
        "no_continuous_box_or_leading_energy_root_certificate":True,
        "leading_fit_not_original_finite_width_ruling_solution":True}
    emit("R605_MEMORY_GUIDE_FINAL",record)
    return chosen,record


class HardBoundaryMass(base.MassCollocation):
    """Exact coordinate embedding of all original 29 boundary conditions.

    There remain 19*(N-1)+2*N equations and 21*N+10-29 unknowns.
    The true derivative of the prepared-plus-free center is included.
    """
    def __init__(self,rhs,x,ruling_unit):
        super().__init__(rhs,x,ruling_unit)
        self.full_size = self.size
        stages = 21*len(self.x)
        eliminated = np.r_[np.arange(19),
                           21*(len(self.x)-1)+np.r_[3,4,np.arange(5,13)]]
        self.free_stage_indices = np.setdiff1d(np.arange(stages),eliminated)
        self.size = len(self.free_stage_indices)+10

    def unpack(self,z):
        count = len(self.free_stage_indices)
        p = z[count:]
        if len(p) != 10:
            raise ValueError("hard boundary coordinates require the original ten parameters")
        flat = np.zeros(21*len(self.x))
        flat[self.free_stage_indices] = z[:count]
        y = flat.reshape((21,len(self.x)),order="F")
        _,ac,_,_ = self.rhs.coordinates.center([paid.constant(v,0) for v in p])
        y[0,0],y[4,0] = p[0],p[1]
        y[5:13,0] = np.array([v.value for v in ac],dtype=float)
        return y,p

    def pack(self,y,p):
        return np.r_[np.asarray(y).ravel(order="F")[self.free_stage_indices],p]

    def embedding_jacobian(self,p):
        count = len(self.free_stage_indices)
        rows = self.free_stage_indices.tolist()+list(range(self.full_size-10,self.full_size))
        cols = list(range(count))+list(range(count,count+10))
        values = [1.]*(count+10)
        rows.extend([0,4]); cols.extend([count,count+1]); values.extend([1.,1.])
        eye = np.eye(10,dtype=LD)
        _,ac,_,_ = self.rhs.coordinates.center([paid.Jet(v,eye[i]) for i,v in enumerate(p)])
        for j,value in enumerate(ac):
            for k,derivative in enumerate(value.derivative):
                if derivative != 0:
                    rows.append(5+j); cols.append(count+k); values.append(float(derivative))
        return coo_matrix((values,(rows,cols)),shape=(self.full_size,self.size)).tocsc()

    def evaluate(self,z):
        y,p = self.unpack(z)
        # The base evaluator calls self.unpack; pass its reduced coordinates,
        # then retain only the equations whose BC rows are identically paid.
        current = super().evaluate(z)
        current["residual"] = current["residual"][:-29]
        current["weights"] = current["weights"][:-29]
        current["weighted"] = current["weights"]*current["residual"]
        return current

    def jacobian(self,current):
        # The inherited assembly uses self.size for its square shape only.
        # Restore full dimensions during assembly, then apply the exact map.
        reduced_size = self.size
        self.size = self.full_size
        try:
            complete = super().jacobian(current)
        finally:
            self.size = reduced_size
        return complete[:-29,:]@self.embedding_jacobian(current["p"])


def hard_boundary_seed(system,y,p):
    """Smooth endpoint projection is an initial guess, not true M integration."""
    original = y.copy()
    x = system.x
    blend = x**3*(10-15*x+6*x*x)
    y = y.copy()
    y[5:13] -= original[5:13,-1,None]*blend[None,:]
    z = system.pack(y,p)
    projected,parameters = system.unpack(z)
    emit("R605_HARD_BOUNDARY_INITIAL_PROJECTION",{
        "true_integrated_guide_eight_endpoint":original[5:13,-1].tolist(),
        "smooth_A_correction_max":float(np.max(np.abs(projected[5:13]-original[5:13]))),
        "projected_original_bc":system.rhs.boundary(projected[:,0],projected[:,-1],parameters).tolist(),
        "rho_seed_from_unprojected_true_guide_retained":True,
        "matrix_and_rho_differential_defects_not_declared_zero":True,
        "BC_coordinate_projection_not_an_actual_history_payment":True,
        "reduced_unknowns":system.size,"original_unknowns_before_BC_elimination":system.full_size})
    return z


def solve_hard_boundary_mass(rhs,x,y,p,unit,args,level=0,project_initial=True):
    started = time.time()
    system = HardBoundaryMass(rhs,x,unit)
    z = hard_boundary_seed(system,y,p) if project_initial else system.pack(y,p)
    current = system.evaluate(z)
    trust,damping = args.trust_radius,args.damping
    report = base.mass_checkpoint(rhs,system,current,0,level,trust,damping,
                                  "new_whole_memory_guide_exact_boundary_coordinates")
    accepted = rejected = linear_iterations = 0
    status = "iteration_limit_with_finite_state"

    def converged(state):
        return (np.max(np.abs(state["differential"]))<=args.flow_tol
                and np.max(np.abs(state["algebraic"]))<=args.ruling_tol
                and np.max(np.abs(state["bc"]))<=args.bc_tol)

    for iteration in range(1,args.newton_iterations+1):
        if converged(current):
            status = "actual_discrete_mass_equations_converged"
            break
        try:
            jacobian = system.jacobian(current)
        except (FloatingPointError,ValueError,OverflowError) as exc:
            status = "finite_state_after_Jacobian_failure"
            emit("R605_HARD_MASS_FAILURE",{"stage":"Jacobian","type":type(exc).__name__,"message":str(exc)})
            break
        weighted = diags(current["weights"])@jacobian
        maximum = np.maximum(1.,np.asarray(abs(weighted).max(axis=0).toarray()).ravel())
        normalized = weighted@diags(1/maximum)
        norms = np.sqrt(np.asarray(normalized.power(2).sum(axis=0)).ravel())
        columns = (1/maximum)/np.maximum(1.,norms)
        matrix = weighted@diags(columns)
        residual = current["weighted"]
        merit = .5*residual@residual
        accepted_here = False
        for trial in range(args.trial_limit):
            try:
                linear = lsmr(matrix,-residual,damp=np.sqrt(damping),
                              atol=1.e-11,btol=1.e-11,maxiter=args.linear_iterations)
            except (FloatingPointError,ValueError,OverflowError,RuntimeError) as exc:
                emit("R605_HARD_MASS_FAILURE",{"stage":"linear","type":type(exc).__name__,
                                             "message":str(exc),"finite_state_retained":True})
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
                    raise FloatingPointError("nonfinite_hard_boundary_mass_merit")
                actual = merit-next_merit
                ratio = actual/predicted if predicted>0 else -np.inf
            except (FloatingPointError,ValueError,OverflowError) as exc:
                candidate = None
                error = {"type":type(exc).__name__,"message":str(exc)}
            ok = (candidate is not None and predicted>0 and actual>0
                  and np.isfinite(ratio) and ratio>=args.acceptance_ratio)
            finite = lambda v: None if v is None or not np.isfinite(v) else float(v)
            emit("R605_HARD_MASS_TRIAL",{
                "level":level,"iteration":iteration,"trial":trial,"accepted":bool(ok),
                "current_merit":float(merit),"trial_merit":finite(next_merit),
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
                report = base.mass_checkpoint(rhs,system,current,iteration,level,trust,damping,
                                               "accepted_full_equations_with_exact_boundary_map")
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
    summary = {
        "level":level,"status":status,"elapsed_seconds":time.time()-started,
        "reduced_unknowns":system.size,"original_unknowns":system.full_size,
        "boundary_conditions_eliminated_by_exact_coordinate_map":29,
        "stage_nodes":len(x),"accepted_steps":accepted,"rejected_trials":rejected,
        "LSMR_total_iterations":linear_iterations,
        "actual_differential_max":float(np.max(np.abs(current["differential"]))),
        "actual_ruling_max":float(np.max(np.abs(current["algebraic"]))),
        "actual_boundary_max":float(np.max(np.abs(current["bc"]))),
        "weighted_merit":float(.5*current["weighted"]@current["weighted"]),
        "continuous_root_or_geometry_claim":False}
    emit("R605_HARD_MASS_LEVEL_FINAL",summary)
    return system,current,summary,report


def main():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("Science only in the declared public Actions repository")
    parser = argparse.ArgumentParser()
    parser.add_argument("--initial-height",type=float,default=1.1)
    parser.add_argument("--initial-length",type=float,default=4.)
    parser.add_argument("--memory-order",type=int,default=64)
    parser.add_argument("--guide-nodes",type=int,default=257)
    parser.add_argument("--energy-stride",type=int,default=4)
    parser.add_argument("--leading-energy-weight",type=float,default=2.)
    parser.add_argument("--compactness-weight",type=float,default=1.)
    parser.add_argument("--guide-max-nfev",type=int,default=300)
    parser.add_argument("--history-nodes",type=int,default=513)
    parser.add_argument("--order",type=int,default=192)
    parser.add_argument("--gap-order",type=int,default=8)
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
    coefficients = model = rhs = None
    status = "not_initialized"
    try:
        labels,rows = previous.rebuild_known_rows()
        grid = base.WideReferenceGrid(args.order,args.gap_order,5.)
        coefficients = base.CountedCoefficients(labels,rows,grid)
        potential = previous.FactoredPotential(grid)
        emit("R605_SAME_WIDE_MOTHER_NEW_INPUT",{
            "graph":grid.graph_info,"coefficients":coefficients.stats,"positive_Gram":potential.stats,
            "necessary_table_recreation_counted":True,"old_numerical_data_not_stored_or_replayed":True,
            "old_identity_derivative_or_quadrature_gate_repeated":False,
            "whole_positive_square_coefficient":1,"same_R598_mother":True})
        model = MemoryGuide(args.memory_order)
        guide,guide_record = fit_memory_guide(args,model)
        emit("R605_NEW_GUIDE_GEOMETRY_BUDGET",base.guide_geometry_budget(model,guide,0.,grid))
        rhs = interface.ColumnMassRHS(coefficients,potential,args.coordinate_guard)
        x,y,p,unit,seed = base.make_seed(rhs,model,guide,0.,args)
        interface.retain_complete_mass_input(rhs,x,y,p,unit,seed)
        system,current,summary,report = solve_hard_boundary_mass(rhs,x,y,p,unit,args)
        if summary["status"]=="actual_discrete_mass_equations_converged":
            refined = np.linspace(0.,1.,4*args.intervals+1)
            physical = system.physical_spline(current)(refined)
            acceleration = np.vstack([np.interp(refined,system.x,row) for row in current["y"][19:]])
            system,current,summary,report = solve_hard_boundary_mass(
                rhs,refined,np.vstack([physical,acceleration]),current["p"],unit,args,1,False)
        status = summary["status"]
        try:
            budget = interface.final_mass_geometry_budget(rhs,system,current)
            json.dumps(budget,allow_nan=False)
            emit("R605_FINAL_ACTUAL_MASS_GEOMETRY_BUDGET",budget)
        except (FloatingPointError,ValueError,OverflowError,RuntimeError) as exc:
            emit("R605_FINAL_GEOMETRY_FAILURE",{
                "type":type(exc).__name__,"message":str(exc),"last_finite_mass_state_retained":True})
    except (FloatingPointError,ValueError,OverflowError,RuntimeError) as exc:
        status = "new_memory_guide_or_hard_mass_attempt_failed"
        emit("R605_NEW_SCOPE_FAILURE",{
            "type":type(exc).__name__,"message":str(exc),"original_equations_not_replaced":True,
            "finite_width_nonexistence_or_completion_claim":False})
    emit("R605_DONE",{
        "elapsed_seconds":time.time()-started,"last_status":status,
        "coefficient_value_evaluations_all_scopes":None if coefficients is None else coefficients.value_calls,
        "coefficient_jet_evaluations_all_scopes":None if coefficients is None else coefficients.jet_calls,
        "guide_geometry_calls":None if model is None else model.geometry_calls,
        "guide_shape_points":None if model is None else model.shape_points,
        "guide_memory_integrand_points":None if model is None else model.memory_integrand_points,
        "mass_RHS_calls":None if rhs is None else rhs.calls,
        "mass_RHS_points":None if rhs is None else rhs.points,
        "mass_Jacobian_calls":None if rhs is None else rhs.jacobian_calls,
        "mass_direct_state_evaluations":None if rhs is None else rhs.direct_state_evaluations,
        "mass_derivative_state_evaluations":None if rhs is None else rhs.derivative_state_evaluations,
        "README_completion_claim":False,"full_period_or_reach_claim":False})


if __name__=="__main__":
    main()

