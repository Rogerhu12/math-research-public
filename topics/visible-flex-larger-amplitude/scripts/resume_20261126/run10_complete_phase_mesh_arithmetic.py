#!/usr/bin/env python3
"""Complete material-chart phase meshes of one fixed run10 six-jet field.

All original radial cells and a full 2*pi angular circle are evaluated. Mesh
levels and physical-time levels change discretization only. They never change
the current free point, the frozen scalar, numerical root policy, or q.N/M/J.
Caps are fixed Cartesian R661 p4 graphs; shared seam vertices use their exact
source boundary formula and report every working-word projection discrepancy.
Finite readouts here are not continuous error, reach or embedding certificates.
"""
from __future__ import annotations
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import time

SCHEMA = "same-field-complete-material-phase-mesh-arithmetic-v1"
JET_KEYS = ("F","Fs","Ftheta","Fss","Fstheta","Fthetatheta")
RAW_KEYS = ("F","Fs","Fphi","Fss","Fsphi","Fphiphi")
MARKERS = ((F(3,20),F(0),F(1,25),1),
    (F(0),F(3,20),F(9,200),1),
    (F(-3,20),F(0),F(1,20),1),
    (F(0),F(0),F(11,200),-1))
MARKER_HEIGHT = F(1,1000)


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    import numpy as np
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def finite_array(value, shape=None):
    import numpy as np
    value = np.asarray(value,dtype=np.float64)
    if (shape is not None and value.shape != tuple(shape)) or not np.isfinite(value).all():
        raise ValueError("A complete requested field array is unavailable or nonfinite")
    return value


def positive_integer(value):
    if type(value) is not int or value < 1:
        raise ValueError("Use explicit positive integer full mesh/time subdivisions")
    return value


def parse_levels(text):
    values = []
    for item in text.split(","):
        parts = item.split(":")
        if len(parts) != 3:
            raise ValueError("Each whole mesh level is radial-subdivisions:full-angles:cap-rings")
        r,n,c = (positive_integer(int(v)) for v in parts)
        if n % 4 or any(v & (v-1) for v in (r,n,c)):
            raise ValueError("Use explicit dyadic nested radial/angular/cap grids, including all cardinal rays")
        values.append(dict(radial=r,angles=n,cap_rings=c))
    if not values:
        raise ValueError("At least one complete mesh level is required")
    for old,new in zip(values,values[1:]):
        if (new["radial"] % old["radial"] or new["angles"] % old["angles"]
                or new["cap_rings"] % old["cap_rings"]
                or new["radial"] <= old["radial"] or new["angles"] <= old["angles"]):
            raise ValueError("Use genuine nested spatial levels with both radial and angular refinement")
    return values


def rational_times(text):
    values = [F(v) for v in text.split(",")]
    if not values or len(set(values)) != len(values) or any(v<0 or v>1 for v in values):
        raise ValueError("Keep distinct explicit physical times in [0,1]")
    return values


def circle_vectors(n):
    import numpy as np
    n = positive_integer(n)
    theta = 2*math.pi*np.arange(n,dtype=np.float64)/n
    values = np.column_stack((np.cos(theta),np.sin(theta)))
    if n%4 == 0:
        values[[0,n//4,n//2,3*n//4]] = ((1.,0.),(0.,1.),(-1.,0.),(0.,-1.))
    return theta,values


def rotation(time_value):
    import numpy as np
    t = F(time_value)
    alpha = math.pi*float(t)/2
    c,s = math.cos(alpha),math.sin(alpha)
    if t == 0:
        c,s = 1.,0.
    elif t == 1:
        c,s = 0.,1.
    return np.array(((c,-s,0.),(s,c,0.),(0.,0.,1.)),dtype=np.float64)


def phase_shift(n, time_value):
    shift = F(n)*F(time_value)/4
    if shift.denominator != 1:
        raise ValueError("The declared exact physical time must map this complete theta grid by an integer shift")
    return int(shift) % n


def fixed_chart_inverse(field, n, *, iterations, tolerance):
    """Original q._chart arithmetic; fixed theta targets, not shifted phi."""
    np = field.np
    torch = field.bound.meridian.torch
    q = field.q
    n = positive_integer(n)
    theta,xy = circle_vectors(n)
    lo = np.zeros(n,dtype=np.float64)
    hi = np.full(n,2*math.pi,dtype=np.float64)
    phi = theta.copy()
    minimum_rho = float("inf")
    actual_iterations = 0
    with torch.no_grad():
        for k in range(positive_integer(iterations)):
            actual_theta,rho,_,_,_ = q._chart(phi)
            actual_theta = actual_theta.cpu().numpy()
            rho = rho.cpu().numpy()
            finite_array(actual_theta,(n,));finite_array(rho,(n,))
            if np.any(rho <= 0):
                raise ValueError("The fixed material chart is nonpositive at an actually queried inverse iterate")
            minimum_rho = min(minimum_rho,float(rho.min()))
            residual = actual_theta-theta
            actual_iterations = k+1
            if float(np.max(np.abs(residual))) <= tolerance:
                break
            lo = np.where(residual<0,phi,lo)
            hi = np.where(residual>0,phi,hi)
            trial = phi-residual/rho
            valid = (trial>lo)&(trial<hi)&np.isfinite(trial)
            proposed = np.where(valid,trial,(lo+hi)/2)
            # Exactly satisfied coordinates stay at their actual selected word.
            phi = np.where(residual==0,phi,proposed)
        chart = q._chart(phi)
        actual_theta,rho,rhop = [v.cpu().numpy() for v in chart[:3]]
    residual = actual_theta-theta
    if (not np.isfinite(residual).all() or np.any(rho<=0)
            or float(np.max(np.abs(residual))) > tolerance):
        raise ValueError("The complete fixed-chart inverse did not meet its explicit working tolerance")
    # Every nested coarse angle is selected from these actual finest words.
    return dict(phi=phi,theta=theta,xy=xy,rho=rho,rhop=rhop,
        definition=dict(full_angles=n,theta_over_pi=[str(F(2*k,n)) for k in range(n)],
            actual_phi_hex=[float(v).hex() for v in phi],
            original_fixed_chart_core_sha256=array_sha(q.parent_core),
            chart_method_source_sha256=field.pins["endpoint"][1],
            maximum_working_inverse_residual=float(np.max(np.abs(residual))),
            minimum_actually_read_chart_rho=minimum_rho,
            maximum_iterations=iterations,actual_iterations=actual_iterations,
            working_tolerance=tolerance,continuous_inverse_error_enclosed=False,
            all_coarse_angle_words_taken_from_same_finest_table=True))


def radial_grid(field, subdivisions):
    np = field.np
    q = field.q
    d = positive_integer(subdivisions)
    cells = np.r_[np.repeat(np.arange(q.J-1,dtype=np.int64),d),q.J-2]
    local = np.r_[np.tile(np.arange(d,dtype=np.float64)/d,q.J-1),1.]
    widths = np.diff(q.mesh)
    s = q.mesh[cells]+widths[cells]*local
    intervals = np.repeat(widths/d,d)
    if np.any(intervals<=0) or not np.isfinite(intervals).all():
        raise ValueError("Retain every positive original radial interval and each explicit subinterval")
    exact = []
    for cell,u in zip(cells,local):
        v = F(float(u))
        exact.append([str((1-v)*a+v*b)
            for a,b in zip(field.context.nodes[int(cell)],field.context.nodes[int(cell)+1])])
    target = np.array([field.target_radius(int(c),float(u)) for c,u in zip(cells,local)])
    return dict(cells=cells,local=local,s=s,intervals=intervals,original_cell_widths=widths,
        a=target[:,0],a_error=target[:,1],
        definition=dict(original_cell_count=q.J-1,subdivisions_per_original_cell=d,
            exact_affine_points=exact,affine_pair_order="s = first*S + second",
            current_complete_scalar_reconstruction=field.scalar_reconstruction,
            every_original_cell_retained=True,original_tail_not_omitted=True,
            actual_working_s_coalesced_intervals=int(np.count_nonzero(np.diff(s)<=0)),
            interval_widths_taken_from_original_positive_cell_width_divided_by_integer=True,
            working_widths_are_not_exact_interval_bounds=True))


def spectral_error(Fs,Ftheta,a):
    import numpy as np
    V = finite_array(Fs)
    W = finite_array(Ftheta)/np.asarray(a,dtype=float)[...,None]
    e = np.sum(V*V,axis=-1)-1
    f = np.sum(V*W,axis=-1)
    d = np.sum(W*W,axis=-1)-1
    value = (np.abs(e+d)+np.hypot(e-d,2*f))/2
    return finite_array(value)


def evaluate_finest(field, radial, chart, directory, *, angle_block, callback=None):
    """One complete full-circle original field read, without a changed q policy."""
    np = field.np
    q = field.q
    torch = field.bound.meridian.torch
    directory = Path(directory)
    directory.mkdir(parents=True,exist_ok=False)
    R,A = len(radial["cells"]),len(chart["phi"])
    paths = {k:directory/(k+".npy") for k in JET_KEYS}
    values = {k:np.lib.format.open_memmap(path,mode="w+",dtype=np.float64,shape=(R,A,3))
              for k,path in paths.items()}
    query = q.base.make_query(radial["cells"],radial["local"])
    max_metric = 0.
    max_raw_defect = 0.
    max_centered = 0.
    max_core_z = 0.
    max_cap_position = 0.
    port_errors = dict(core_Fz=0.,core_Fs_xy=0.,core_Fss_z=0.,
        core_Ftheta_z=0.,core_Fthetatheta_z=0.,core_Fstheta_xy=0.,
        cap_F=0.,cap_Fs=0.,cap_Fss=0.,cap_Ftheta=0.,cap_Fstheta=0.,cap_Fthetatheta=0.)
    periodic_errors = None
    start = time.monotonic()
    original_counts = dict(q.counts)
    try:
        with torch.no_grad():
            xt = field.bound.meridian.tensor(field.x)
            for begin in range(0,A,angle_block):
                end = min(A,begin+angle_block)
                phi = chart["phi"][begin:end]
                result = q.fields_torch(xt,query,phi,curvature=True,query_label="same-field-full-mesh")
                expected_keys = set(RAW_KEYS)|{"rho0","closure_delta","centered_closure_residual"}
                if set(result) != expected_keys:
                    raise ValueError("Keep every original physical six-jet and explicit diagnostic")
                raw = {k:finite_array(result[k].detach().cpu().numpy(),(R,end-begin,3)) for k in RAW_KEYS}
                rho = finite_array(result["rho0"].detach().cpu().numpy(),(end-begin,))
                actual_chart = q._chart(phi)
                check_rho = actual_chart[1].cpu().numpy()
                rp = actual_chart[2].cpu().numpy()
                if check_rho.tobytes() != rho.tobytes() or np.any(rho <= 0):
                    raise ValueError("The complete physical field and its same-block chart disagree")
                chart["rho"][begin:end] = rho
                chart["rhop"][begin:end] = rp
                actual_inverse_error = np.max(np.abs(
                    actual_chart[0].cpu().numpy()-chart["theta"][begin:end]))
                chart["definition"]["maximum_working_inverse_residual"] = max(
                    chart["definition"]["maximum_working_inverse_residual"],float(actual_inverse_error))
                if (not math.isfinite(float(actual_inverse_error)) or
                        float(actual_inverse_error)>chart["definition"]["working_tolerance"]):
                    raise ValueError("The original same-block chart inverse exceeds its declared working tolerance")
                derived = dict(F=raw["F"],Fs=raw["Fs"],Fss=raw["Fss"],
                    Ftheta=raw["Fphi"]/rho[None,:,None],
                    Fstheta=raw["Fsphi"]/rho[None,:,None],
                    Fthetatheta=raw["Fphiphi"]/rho[None,:,None]**2
                        -raw["Fphi"]*rp[None,:,None]/rho[None,:,None]**3)
                for key,value in derived.items():
                    values[key][:,begin:end] = finite_array(value,(R,end-begin,3))
                max_metric = max(max_metric,float(spectral_error(
                    derived["Fs"],derived["Ftheta"],radial["a"][:,None]).max()))
                defect = finite_array(result["closure_delta"].detach().cpu().numpy(),(end-begin,3))
                centered = finite_array(result["centered_closure_residual"].detach().cpu().numpy(),(end-begin,3))
                max_raw_defect = max(max_raw_defect,float(np.linalg.norm(defect,axis=-1).max()))
                max_centered = max(max_centered,float(np.linalg.norm(centered,axis=-1).max()))
                max_core_z = max(max_core_z,float(np.max(np.abs(raw["F"][0,:,2]))))
                cap = np.column_stack((q.R*chart["xy"][begin:end],
                    np.full(end-begin,field.height,dtype=float)))
                max_cap_position = max(max_cap_position,float(np.linalg.norm(raw["F"][-1]-cap,axis=-1).max()))
                core = {k:v[0] for k,v in derived.items()}
                for key,value in dict(core_Fz=np.abs(core["F"][:,2]),
                        core_Fs_xy=np.linalg.norm(core["Fs"][:,:2],axis=-1),
                        core_Fss_z=np.abs(core["Fss"][:,2]),
                        core_Ftheta_z=np.abs(core["Ftheta"][:,2]),
                        core_Fthetatheta_z=np.abs(core["Fthetatheta"][:,2]),
                        core_Fstheta_xy=np.linalg.norm(core["Fstheta"][:,:2],axis=-1)).items():
                    port_errors[key] = max(port_errors[key],float(value.max()))
                er = np.column_stack((chart["xy"][begin:end],np.zeros(end-begin)))
                et = np.column_stack((-chart["xy"][begin:end,1],
                    chart["xy"][begin:end,0],np.zeros(end-begin)))
                targets = dict(F=cap,Fs=-er,Fss=np.zeros_like(er),
                    Ftheta=q.R*et,Fstheta=-et,Fthetatheta=-q.R*er)
                for key,target in targets.items():
                    port_errors["cap_"+key] = max(port_errors["cap_"+key],
                        float(np.linalg.norm(derived[key][-1]-target,axis=-1).max()))
                for value in values.values():
                    value.flush()
                if callback is not None:
                    callback(dict(phase="full-field-angular-block-returned",completed_angles=end,
                        total_angles=A,radial_nodes=R,maximum_sampled_metric_operator_error=max_metric,
                        seconds=time.monotonic()-start))
        with torch.no_grad():
            boundary = q.fields_torch(xt,query,np.array([2*math.pi]),curvature=True,
                query_label="same-field-full-periodic-boundary")
            ch = q._chart(np.array([2*math.pi]))
            rr,rp = float(ch[1][0]),float(ch[2][0])
            if not math.isfinite(rr) or rr<=0:
                raise ValueError("The actual full-circle endpoint chart is not positive")
            raw_end = {k:finite_array(boundary[k].detach().cpu().numpy(),(R,1,3))[:,0]
                       for k in RAW_KEYS}
            end_jets = dict(F=raw_end["F"],Fs=raw_end["Fs"],Fss=raw_end["Fss"],
                Ftheta=raw_end["Fphi"]/rr,Fstheta=raw_end["Fsphi"]/rr,
                Fthetatheta=raw_end["Fphiphi"]/rr**2-raw_end["Fphi"]*rp/rr**3)
            periodic_errors = {key:float(np.linalg.norm(value-np.asarray(values[key][:,0]),axis=-1).max())
                               for key,value in end_jets.items()}
            periodic_errors["endpoint_actual_material_phi_hex"] = float(2*math.pi).hex()
            periodic_errors["endpoint_working_theta_error"] = abs(float(ch[0][0])-2*math.pi)
            periodic_errors["full_original_radial_nodes_reread"] = R
            periodic_errors["continuous_branch_glue_certified"] = False
        if array_sha(field.x) != field.point_sha or q._current_point_sha256 != field.point_sha:
            raise ValueError("The complete field read changed the actual selected outer point")
    finally:
        for value in values.values():
            value.flush()
        del values
    return dict(paths={k:str(v.resolve()) for k,v in paths.items()},shape=[R,A,3],
        coordinate_jets=list(JET_KEYS),coordinates="s and physical material theta0",
        original_phi_sixjets_preserved_by_explicit_chain_rule=True,
        maximum_sampled_metric_operator_error=max_metric,
        maximum_original_working_raw_closure_defect=max_raw_defect,
        maximum_original_working_centered_closure_residual=max_centered,
        maximum_raw_core_vertical_port_discrepancy=max_core_z,
        maximum_raw_cap_cartesian_port_discrepancy=max_cap_position,
        all_sampled_sixjet_port_discrepancies=port_errors,
        actual_full_radial_periodic_seam_read=periodic_errors,
        additional_periodic_endpoint_points=R,
        literal_C2_ports_or_continuous_branch_glue_not_inferred=True,
        complete_full_circle=True,all_original_cells=True,
        evaluated_field_points=R*A,actual_seconds=time.monotonic()-start,
        operator_counts_before=original_counts,operator_counts_after=dict(q.counts),
        no_q_norm_or_root_budget_or_frequency_change=True,
        positive_a_carrier_errors_not_included_in_numerical_Gram_norm=True,
        continuous_error_certified=False)


def open_jets(result):
    import numpy as np
    return {key:np.load(path,mmap_mode="r",allow_pickle=False) for key,path in result["paths"].items()}


def cap_radii(radius, count):
    import numpy as np
    if not math.isfinite(radius) or radius <= float(F(1,5)):
        raise ValueError("The complete actual cap must contain all fixed R661 supports")
    values = list(np.linspace(0.,radius,positive_integer(count)+1))
    values += [float(F(3,20)),float(F(9,20))]
    values += [float(F(3,20)-v) for v in (F(1,25),F(9,200),F(1,20))]
    values += [float(F(3,20)+v) for v in (F(1,25),F(9,200),F(1,20))]
    values += [float(F(11,200))]
    return np.array(sorted(set(v for v in values if 0<=v<=radius)),dtype=np.float64)


def cap_graph(xy, height, sign):
    """Fixed Cartesian graph and its first/two derivatives; no phase rotation."""
    import numpy as np
    xy = finite_array(xy)
    if xy.shape[-1] != 2 or sign not in (-1,1):
        raise ValueError("Use either complete Cartesian cap")
    z = np.full(xy.shape[:-1],sign*height,dtype=np.float64)
    gradient = np.zeros_like(xy)
    Hessian = np.zeros(xy.shape[:-1]+(2,2),dtype=np.float64)
    for cx,cy,r,sigma in MARKERS:
        if sigma != sign:
            continue
        delta = xy-np.array((float(cx),float(cy)),dtype=float)
        b2 = float(r*r)
        w = np.maximum(0.,1-np.sum(delta*delta,axis=-1)/b2)
        h = sign*float(MARKER_HEIGHT)
        z += h*w**4
        gradient += (-8*h/b2*w**3)[...,None]*delta
        Hessian += (48*h/b2**2*w**2)[...,None,None]*delta[...,None]*delta[...,None,:]
        Hessian -= (8*h/b2*w**3)[...,None,None]*np.eye(2)
    return np.concatenate((xy,z[...,None]),axis=-1),gradient,Hessian


def level_indices(finest,level,radial_count):
    import numpy as np
    rs,ns = finest["radial"]//level["radial"],finest["angles"]//level["angles"]
    if finest["radial"]%level["radial"] or finest["angles"]%level["angles"]:
        raise ValueError("A coarse level must be a literal subset of the finest material grid")
    radial = np.arange(0,radial_count,rs,dtype=np.int64)
    angles = np.arange(0,finest["angles"],ns,dtype=np.int64)
    if radial[-1] != radial_count-1:
        raise ValueError("Both complete radial boundary circles must remain")
    return radial,angles


def coarse_interpolation_comparison(jets,radial,finest,coarse,fine,*,radius,height,block=32):
    """Actual finer samples against both triangles of the complete coarser mesh."""
    import numpy as np
    cr,ca = level_indices(finest,coarse,len(radial["cells"]))
    fr,fa = level_indices(finest,fine,len(radial["cells"]))
    R,A = len(fr),len(fa)
    rf = fine["radial"]//coarse["radial"]
    af = fine["angles"]//coarse["angles"]
    angular_coarse = np.arange(A)//af
    v = (np.arange(A)%af)/af
    next_angular = (angular_coarse+1)%len(ca)
    delta_theta = 2*math.pi/coarse["angles"]
    _, coarse_xy = circle_vectors(coarse["angles"])
    _, fine_xy = circle_vectors(fine["angles"])
    maximum = dict(position=0.,raw_working_position=0.,
                   actual_port_projection=0.,radial_derivative=0.,angular_derivative=0.,
                   coarse_PL_metric_operator_error=0.,actual_fine_metric_operator_error=0.)
    tested = 0
    for begin in range(0,R,block):
        stop = min(R,begin+block)
        for ii in range(begin,stop):
            ci = min(ii//rf,len(cr)-2)
            u = (ii-ci*rf)/rf
            coarse_first = _port_values(jets,int(cr[ci]),ca,coarse_xy,radius,height)
            coarse_next = _port_values(jets,int(cr[ci+1]),ca,coarse_xy,radius,height)
            f00,f01 = coarse_first[angular_coarse],coarse_first[next_angular]
            f10,f11 = coarse_next[angular_coarse],coarse_next[next_angular]
            lower = u <= v
            interp1 = (1-v)[:,None]*f00+(v-u)[:,None]*f01+u*f11
            interp2 = (1-u)*f00+(u-v)[:,None]*f10+v[:,None]*f11
            interp = np.where(lower[:,None],interp1,interp2)
            # Width remains the complete original cell width divided by the
            # declared integer, even if two rounded global s words coalesce.
            original_cell = ci//coarse["radial"]
            width = radial["original_cell_widths"][original_cell]/coarse["radial"]
            ds = np.where(lower[:,None],f11-f01,f10-f00)/width
            dt = np.where(lower[:,None],f01-f00,f11-f10)/delta_theta
            true = {key:np.asarray(jets[key][fr[ii],fa]) for key in ("F","Fs","Ftheta")}
            raw_first = np.asarray(jets["F"][cr[ci],ca])
            raw_next = np.asarray(jets["F"][cr[ci+1],ca])
            r00,r01 = raw_first[angular_coarse],raw_first[next_angular]
            r10,r11 = raw_next[angular_coarse],raw_next[next_angular]
            raw_interp = np.where(lower[:,None],
                (1-v)[:,None]*r00+(v-u)[:,None]*r01+u*r11,
                (1-u)*r00+(u-v)[:,None]*r10+v[:,None]*r11)
            maximum["raw_working_position"] = max(maximum["raw_working_position"],
                float(np.linalg.norm(true["F"]-raw_interp,axis=-1).max()))
            projected = _port_values(jets,int(fr[ii]),fa,fine_xy,radius,height)
            maximum["actual_port_projection"] = max(maximum["actual_port_projection"],
                float(np.linalg.norm(projected-true["F"],axis=-1).max()),
                float(np.linalg.norm(raw_first-coarse_first,axis=-1).max()),
                float(np.linalg.norm(raw_next-coarse_next,axis=-1).max()))
            true["F"] = projected
            maximum["position"] = max(maximum["position"],float(np.linalg.norm(true["F"]-interp,axis=-1).max()))
            maximum["radial_derivative"] = max(maximum["radial_derivative"],float(np.linalg.norm(true["Fs"]-ds,axis=-1).max()))
            maximum["angular_derivative"] = max(maximum["angular_derivative"],float(np.linalg.norm(true["Ftheta"]-dt,axis=-1).max()))
            a = np.full(A,radial["a"][fr[ii]])
            maximum["coarse_PL_metric_operator_error"] = max(maximum["coarse_PL_metric_operator_error"],
                float(spectral_error(ds,dt,a).max()))
            maximum["actual_fine_metric_operator_error"] = max(maximum["actual_fine_metric_operator_error"],
                float(spectral_error(true["Fs"],true["Ftheta"],a).max()))
            tested += A
    return dict(coarse=coarse,fine=fine,actual_full_finer_nodes_tested=tested,
        differences=maximum,source_point_shared_byte_for_byte=True,
        interpolation_in_physical_s_theta_coordinates=True,
        position_uses_the_same_explicit_port_rounding_as_exported_closed_meshes=True,
        full_upper_grid_tested_lower_reflection_preserves_these_norms=True,
        original_nonlinear_field_not_reoptimized=True,
        same_exact_target_not_interpolated_from_old_values=True,
        derivatives_are_finite_readouts_not_supremum_certificates=True,
        target_a_outward_uncertainty_not_added_to_this_working_norm=True,
        same_g_solver_refinement_convergence_claimed=False)


def time_interpolation_comparison(jets,radial,finest,coarse_steps,fine_steps,*,radius,height,block=24):
    import numpy as np
    coarse_steps,fine_steps = positive_integer(coarse_steps),positive_integer(fine_steps)
    if fine_steps <= coarse_steps or fine_steps%coarse_steps:
        raise ValueError("Use a genuine nested complete physical time refinement")
    A,R = finest["angles"],len(radial["cells"])
    full_indices = np.arange(A)
    _, xy = circle_vectors(A)
    cap = np.column_stack((radius*xy,np.full(A,height)))
    maximum = dict(position=0.,raw_working_position=0.,radial_derivative=0.,physical_angular_derivative=0.)
    max_port_projection = 0.
    times = []
    count = 0
    for index in range(fine_steps+1):
        t = F(index,fine_steps)
        left_index = min((index*coarse_steps)//fine_steps,coarse_steps-1)
        left,right = F(left_index,coarse_steps),F(left_index+1,coarse_steps)
        weight = float((t-left)/(right-left))
        shifts = [phase_shift(A,v) for v in (t,left,right)]
        rotations = [rotation(v) for v in (t,left,right)]
        local = {key:0. for key in maximum}
        for start in range(0,R,block):
            stop = min(R,start+block)
            for key,label in (("F","position"),("Fs","radial_derivative"),
                              ("Ftheta","physical_angular_derivative")):
                base = np.asarray(jets[key][start:stop])
                actual = base[:,(full_indices-shifts[0])%A]@rotations[0].T
                first = base[:,(full_indices-shifts[1])%A]@rotations[1].T
                second = base[:,(full_indices-shifts[2])%A]@rotations[2].T
                if key == "F":
                    raw_error = float(np.linalg.norm(actual-((1-weight)*first+weight*second),axis=-1).max())
                    local["raw_working_position"] = max(local["raw_working_position"],raw_error)
                    maximum["raw_working_position"] = max(maximum["raw_working_position"],raw_error)
                    for value in (actual,first,second):
                        if start == 0:
                            max_port_projection = max(max_port_projection,float(np.max(np.abs(value[0,:,2]))))
                            value[0,:,2] = 0.
                        if stop == R:
                            max_port_projection = max(max_port_projection,float(np.linalg.norm(value[-1]-cap,axis=-1).max()))
                            value[-1] = cap
                error = float(np.linalg.norm(actual-((1-weight)*first+weight*second),axis=-1).max())
                local[label] = max(local[label],error)
                maximum[label] = max(maximum[label],error)
        count += R*A
        times.append(dict(t_exact=str(t),coarse_left_exact=str(left),
            coarse_right_exact=str(right),differences=local))
    return dict(coarse_steps=coarse_steps,fine_steps=fine_steps,
        complete_time_interval=[0,1],all_fine_times=times,
        all_upper_material_nodes_at_each_time=True,
        lower_reflection_has_the_same_norms=True,fixed_cartesian_caps_interpolation_error=0.,
        actual_node_time_pairs=count,maximum_differences=maximum,
        maximum_port_projection_over_all_actually_tested_times=max_port_projection,
        raw_working_position_and_exported_port_projection_kept_separate=True,
        exact_R248_phase_formula_used_at_actual_times=True,
        linear_time_interpolant_is_a_different_map=True,
        interpolated_family_not_claimed_isometric=True,
        continuous_in_t_error_not_certified=True)


def _vertex_chunks(jets,radial_indices,angle_indices,radii,radius,height,time_value,*,block=32):
    import numpy as np
    R,N = len(radial_indices),len(angle_indices)
    shift = phase_shift(N,time_value)
    chosen = angle_indices[(np.arange(N)-shift)%N]
    rot = rotation(time_value)
    _,xy = circle_vectors(N)
    # Belt vertices go from lower cuff to core to upper cuff, in signed u.
    rows = [(int(radial_indices[i]),-1) for i in range(R-1,0,-1)]
    rows += [(int(radial_indices[i]),1) for i in range(R)]
    max_projection = 0.
    for start in range(0,len(rows),block):
        use = rows[start:start+block]
        values = np.stack([np.asarray(jets["F"][r,chosen])@rot.T for r,_ in use])
        for i,(r,side) in enumerate(use):
            if side < 0:
                values[i,:,2] *= -1
            expected = None
            if r == int(radial_indices[-1]):
                expected = np.column_stack((radius*xy,np.full(N,side*height)))
            elif r == int(radial_indices[0]):
                expected = values[i].copy()
                expected[:,2] = 0.
            if expected is not None:
                max_projection = max(max_projection,float(np.linalg.norm(values[i]-expected,axis=-1).max()))
                values[i] = expected
        yield values.reshape(-1,3),max_projection
    for side in (1,-1):
        center = cap_graph(np.zeros((1,2)),height,side)[0]
        yield center,max_projection
        for r in radii[1:-1]:
            yield cap_graph(r*xy,height,side)[0],max_projection


def _face_chunks(radial_count,angles,radii):
    import numpy as np
    R,N = radial_count,angles
    belt_rows = 2*R-1
    j = np.arange(N,dtype=np.int64)
    nxt = (j+1)%N
    for row in range(belt_rows-1):
        a,b = row*N+j,row*N+nxt
        c,d = (row+1)*N+j,(row+1)*N+nxt
        yield np.stack((a,b,d),axis=-1)
        yield np.stack((a,d,c),axis=-1)
    cap_size = 1+(len(radii)-2)*N
    for side in (1,-1):
        base = belt_rows*N+(0 if side==1 else cap_size)
        outer = (belt_rows-1)*N if side==1 else 0
        def ring(k):
            return outer+j if k==len(radii)-1 else base+1+(k-1)*N+j
        first = ring(1)
        faces = np.stack((np.full(N,base),first,np.roll(first,-1)),axis=-1)
        yield faces if side==1 else faces[:,[0,2,1]]
        for k in range(1,len(radii)-1):
            inside,outside = ring(k),ring(k+1)
            a = np.stack((inside,outside,np.roll(outside,-1)),axis=-1)
            b = np.stack((inside,np.roll(outside,-1),np.roll(inside,-1)),axis=-1)
            yield a if side==1 else a[:,[0,2,1]]
            yield b if side==1 else b[:,[0,2,1]]


def write_mesh(path,jets,radial_indices,angle_indices,radii,radius,height,time_value,*,
               float_bits=64,max_bytes=None):
    import numpy as np
    path = Path(path)
    if path.exists() or float_bits not in (32,64):
        raise ValueError("Write a fresh explicit complete mesh at a declared floating format")
    R,N = len(radial_indices),len(angle_indices)
    V = (2*R-1)*N+2*(1+(len(radii)-2)*N)
    triangles = 2*((2*R-2)*N)+2*N+4*(len(radii)-2)*N
    if V > np.iinfo(np.int32).max:
        raise ValueError("The explicit PLY index width cannot represent the complete requested mesh")
    kind = "double" if float_bits==64 else "float"
    header = ("ply\nformat binary_little_endian 1.0\n"
        "comment same actual run10 full point; fixed material chart phase; fixed p4 caps\n"
        +"element vertex "+str(V)+"\n"
        +"property "+kind+" x\nproperty "+kind+" y\nproperty "+kind+" z\n"
        +"element face "+str(triangles)+"\nproperty list uchar int vertex_indices\nend_header\n").encode()
    bytes_expected = len(header)+V*3*(float_bits//8)+triangles*13
    if max_bytes is not None and bytes_expected >= max_bytes:
        raise ValueError("The declared standalone preview mesh is not below its explicit byte limit")
    temporary = path.with_name(path.name+".partial")
    max_projection,max_quantization = 0.,0.
    vertex_count,face_count = 0,0
    low,high = np.full(3,np.inf),np.full(3,-np.inf)
    with temporary.open("xb") as stream:
        stream.write(header)
        for chunk,projection in _vertex_chunks(jets,radial_indices,angle_indices,
                radii,radius,height,time_value):
            finite_array(chunk)
            encoded = np.asarray(chunk,dtype="<f8" if float_bits==64 else "<f4")
            if not np.isfinite(encoded).all():
                raise ValueError("The selected mesh representation overflowed")
            max_quantization = max(max_quantization,float(np.linalg.norm(
                chunk-encoded.astype(np.float64),axis=-1).max()))
            max_projection = max(max_projection,projection)
            low,high = np.minimum(low,chunk.min(0)),np.maximum(high,chunk.max(0))
            stream.write(encoded.tobytes(order="C"))
            vertex_count += len(chunk)
        dtype = np.dtype([("count","u1"),("indices","<i4",(3,))])
        for faces in _face_chunks(R,N,radii):
            if np.any(faces<0) or np.any(faces>=V):
                raise AssertionError("A complete topology index lies outside the actual vertex set")
            data = np.empty(len(faces),dtype=dtype)
            data["count"] = 3
            data["indices"] = faces
            stream.write(data.tobytes())
            face_count += len(faces)
    if vertex_count != V or face_count != triangles or temporary.stat().st_size != bytes_expected:
        raise AssertionError("The complete mesh writer omitted declared vertices or faces")
    temporary.replace(path)
    return dict(path=str(path.resolve()),bytes=path.stat().st_size,
        vertex_count=V,triangle_count=triangles,coordinate_bits=float_bits,
        physical_t_exact=str(F(time_value)),alpha_over_pi_exact=str(F(time_value)/2),
        full_belt_and_both_cartesian_marked_caps=True,
        cuff_indices_shared_with_caps=True,central_reflection_indices_shared=True,
        material_grid_phase_shift_exact_integer=phase_shift(N,time_value),
        complete_known_topology_euler_characteristic=2,
        triangle_order="signed belt Ftheta cross Fu; Cartesian upper +z, lower -z",
        port_rounding_projection_maximum=max_projection,
        coordinate_serialization_error_maximum=max_quantization,
        mesh_coordinate_bbox=[low.tolist(),high.tolist()],
        exact_port_formula_used_for_mesh_boundary_vertices=True,
        working_field_values_not_silently_relabelled_as_exact_ports=True,
        polygonal_mesh_not_a_C2_surface_certificate=True,
        geometric_self_intersection_or_reach_certified=False)


def _port_values(jets, radial_index, angle_indices, xy, radius, height):
    import numpy as np
    result = np.array(jets["F"][radial_index,angle_indices],copy=True)
    if radial_index == 0:
        result[:,2] = 0.
    elif radial_index == jets["F"].shape[0]-1:
        result = np.column_stack((radius*xy,np.full(len(xy),height)))
    return result


def cap_mesh_nodes(radii, angles, height, sign):
    import numpy as np
    _,xy = circle_vectors(angles)
    return np.vstack([cap_graph(np.zeros((1,2)),height,sign)[0]]+
        [cap_graph(r*xy,height,sign)[0] for r in radii[1:]])


def cap_faces(radii,angles,sign):
    import numpy as np
    j = np.arange(angles,dtype=np.int64)
    first = 1+j
    f = np.stack((np.zeros(angles,dtype=np.int64),first,1+(j+1)%angles),axis=-1)
    yield f if sign==1 else f[:,[0,2,1]]
    for k in range(1,len(radii)-1):
        inside = 1+(k-1)*angles+j
        outside = 1+k*angles+j
        a = np.stack((inside,outside,1+k*angles+(j+1)%angles),axis=-1)
        b = np.stack((inside,1+k*angles+(j+1)%angles,1+(k-1)*angles+(j+1)%angles),axis=-1)
        yield a if sign==1 else a[:,[0,2,1]]
        yield b if sign==1 else b[:,[0,2,1]]


def cap_metric_readout(radius,height,level):
    """Every actual cap triangle, sampled at its actual Cartesian centroid."""
    import numpy as np
    radii = cap_radii(radius,level["cap_rings"])
    n = level["angles"]
    tested,degenerate = 0,0
    maximum = 0.
    for sign in (1,-1):
        vertices = cap_mesh_nodes(radii,n,height,sign)
        for faces in cap_faces(radii,n,sign):
            v = vertices[faces]
            edges = v[:,1:]-v[:,:1]
            matrix = edges[:,:,:2]
            det = matrix[:,0,0]*matrix[:,1,1]-matrix[:,0,1]*matrix[:,1,0]
            good = np.isfinite(det)&(det != 0)
            degenerate += int(np.count_nonzero(~good))
            tested += len(faces)
            if not np.any(good):
                continue
            e = edges[good]
            gradient = np.linalg.solve(matrix[good],e[:,:,2,None])[...,0]
            centroid = v[good,:,:2].mean(1)
            _,true_gradient,_ = cap_graph(centroid,height,sign)
            reference = np.eye(2)+true_gradient[:,:,None]*true_gradient[:,None,:]
            actual = np.eye(2)+gradient[:,:,None]*gradient[:,None,:]
            eigenvectors_values,eigenvectors = np.linalg.eigh(reference)
            if np.any(eigenvectors_values <= 0):
                raise ValueError("The complete fixed Cartesian cap target lost positive definiteness")
            inverse = (eigenvectors*(1/np.sqrt(eigenvectors_values))[:,None,:])@np.swapaxes(eigenvectors,-1,-2)
            error = inverse@(actual-reference)@inverse
            norm = finite_array(np.max(np.abs(np.linalg.eigvalsh(error)),axis=-1))
            maximum = max(maximum,float(norm.max()))
    return dict(level=level,complete_both_cap_triangles_tested=tested,
        degenerate_actual_triangles=degenerate,
        maximum_sampled_relative_cap_metric_error=None if degenerate else maximum,
        maximum_over_non_degenerate_triangles=maximum,
        sample="every actual Cartesian triangle centroid",
        fixed_metric_is_the_complete_marked_cap_graph_metric=True,
        unmarked_flat_metric_not_substituted=True,continuous_cap_error_certified=False)


def cap_position_refinement(radius,height,coarse,fine):
    import numpy as np
    cr = cap_radii(radius,coarse["cap_rings"])
    fr = cap_radii(radius,fine["cap_rings"])
    if not set(float(v).hex() for v in cr) <= set(float(v).hex() for v in fr):
        raise ValueError("Every coarse actual cap ring word must be present on the fine cap")
    cn,fn = coarse["angles"],fine["angles"]
    ratio = fn//cn
    if fn%cn:
        raise ValueError("The entire fine cap circle must refine the old circle")
    _,cxy = circle_vectors(cn)
    _,fxy = circle_vectors(fn)
    oldangle = np.arange(fn)//ratio
    v = (np.arange(fn)%ratio)/ratio
    nxt = (oldangle+1)%cn
    maximum,tested = 0.,0
    for sign in (1,-1):
        center = cap_graph(np.zeros((1,2)),height,sign)[0][0]
        for r in fr:
            actual = cap_graph(r*fxy,height,sign)[0]
            if r == 0:
                predicted = np.broadcast_to(center,(fn,3))
            else:
                k = min(max(int(np.searchsorted(cr,r,side="right"))-1,0),len(cr)-2)
                u = (r-cr[k])/(cr[k+1]-cr[k])
                outside = cap_graph(cr[k+1]*cxy,height,sign)[0]
                if k == 0:
                    predicted = (1-u)*center+u*((1-v)[:,None]*outside[oldangle]+v[:,None]*outside[nxt])
                else:
                    inside = cap_graph(cr[k]*cxy,height,sign)[0]
                    f00,f01 = inside[oldangle],inside[nxt]
                    f10,f11 = outside[oldangle],outside[nxt]
                    first = (1-v)[:,None]*f00+(v-u)[:,None]*f01+u*f11
                    second = (1-u)*f00+(u-v)[:,None]*f10+v[:,None]*f11
                    predicted = np.where((u<=v)[:,None],first,second)
            maximum = max(maximum,float(np.linalg.norm(actual-predicted,axis=-1).max()))
            tested += fn
    return dict(coarse=coarse,fine=fine,complete_cap_node_pairs=tested,
        maximum_actual_position_difference=maximum,
        both_fixed_marked_caps_retained=True,
        center_fan_uses_its_full_polar_barycentric_material_map=True,
        bound_between_tested_points_certified=False)
