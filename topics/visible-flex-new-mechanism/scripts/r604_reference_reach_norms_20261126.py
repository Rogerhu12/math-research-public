#!/usr/bin/env python3
"""R604 finite observations of a declared circular reference and actual geometry.

This module never certifies continuous norms. It consumes an already completed
geometry evaluation, with all original FFT/material/roundoff qualifications.
It does not import or rerun a seed, core shooting, or geometry solver.
"""
from collections import defaultdict
import math
import time

import numpy as np

SCHEMA = "r604-same-paid-reference-and-reused-parametric-geometry-norms-v1"
COUNTS = defaultdict(int)


def values(a):
    return np.asarray(a.v if hasattr(a, "v") else a, dtype=float)


def circular_reference_profile(model, reference_q):
    """The original R582 circle's mean formula on the existing radial block.

    The 81 reference coordinates and controls are supplied by the identified
    prior input. The finite nonround model's current core a0 is not substituted.
    This defines a candidate reference; it does not certify closed geometry.
    """
    q = np.asarray(reference_q, dtype=float)
    if (q.shape != (81,) or not np.all(np.isfinite(q))
            or np.any(q[:64] != 0) or model.par.radial_count != 8
            or model.par.core_half_width != .02 or model.par.length != .9
            or model.par.cap_disk_radius != .22):
        raise ValueError("R604 observer requires its identified R582 circle coordinates")
    s = np.asarray(model.s, dtype=float)
    B, B1, B2 = [np.asarray(x, dtype=float) for x in model.bases]
    ac = q[64:72]
    zc = q[72:80]
    alpha = B@ac + np.asarray(model.mean_control_alpha[0])[:,0]
    alpha1 = B1@ac + np.asarray(model.mean_control_alpha[1])[:,0]
    alpha2 = B2@ac + np.asarray(model.mean_control_alpha[2])[:,0]
    chi, comp, dchi, ddchi = [np.asarray(x,dtype=float)[:,0] for x in
        (model.bg_w,model.bg_wm,model.bg_wd,model.bg_wdd)]
    tail = .22+.9-s
    abase = comp*.38+chi*tail
    abase1 = dchi*(tail-.38)-chi
    abase2 = ddchi*(tail-.38)-2*dchi
    ea = np.exp(alpha)
    a = ea*abase
    a1 = ea*(abase1+abase*alpha1)
    a2 = ea*(abase2+2*abase1*alpha1+abase*(alpha2+alpha1*alpha1))
    zh, zh1, zh2 = [np.asarray(x,dtype=float)[:,0] for x in
        (model.tail_height,model.tail_height1,model.tail_height2)]
    dz, dz1, dz2 = [np.asarray(x,dtype=float)[:,0] for x in model.mean_control_z]
    central, end = .02+s, q[80]+zh
    z = comp*central+chi*end+B@zc+dz
    z1 = comp+dchi*(end-central)+chi*zh1+B1@zc+dz1
    z2 = -2*dchi+ddchi*(end-central)+2*dchi*zh1+chi*zh2+B2@zc+dz2
    b = np.hypot(a1,z1)
    if not np.all(np.isfinite(np.r_[a,a1,a2,z,z1,z2,b])) or np.min(a)<=0 or np.min(b)<=0:
        raise ArithmeticError("sampled reference is outside its positive radial immersion chart")
    COUNTS["reference_radial_nodes_evaluated"] += len(s)
    return {"a":a,"a1":a1,"a2":a2,"z":z,"z1":z1,"z2":z2,"speed":b}


def matrix_norm_two_columns(c1,c2):
    aa = np.sum(c1*c1,axis=-1)
    cc = np.sum(c2*c2,axis=-1)
    ab = np.sum(c1*c2,axis=-1)
    top = .5*(aa+cc+np.hypot(aa-cc,2*ab))
    return np.sqrt(np.maximum(top,0.))


def observe_completed_geometry(model,geometry,reference_q):
    """Observe formulas R604(22)(23) without any geometry/AD recomputation."""
    started=time.monotonic()
    ref=circular_reference_profile(model,reference_q)
    theta=np.asarray(model.theta,dtype=float)
    co,si=np.cos(theta),np.sin(theta)
    er=np.stack((co,si,np.zeros_like(co)),axis=-1)
    et=np.stack((-si,co,np.zeros_like(co)),axis=-1)
    ez=np.array([0.,0.,1.])
    a,a1,z,z1,b=[ref[k][:,None,None] for k in ("a","a1","z","z1","speed")]
    X=np.stack([values(x) for x in geometry["position"]],axis=-1)
    Xs=np.stack([values(x) for x in geometry["Xs"]],axis=-1)
    T=np.stack([values(x) for x in geometry["T"]],axis=-1)
    current_a=values(geometry["radius"])[...,None]
    Xt=current_a*T
    X0=a*er[None,:,:]+z*ez
    X0s=a1*er[None,:,:]+z1*ez
    X0t=a*et[None,:,:]
    first,second=Xs/b,Xt/a
    dfirst,dsecond=(Xs-X0s)/b,(Xt-X0t)/a
    cross=np.cross(Xs,T)
    cross_length=np.linalg.norm(cross,axis=-1)
    if np.min(cross_length)<=0 or not np.all(np.isfinite(cross_length)):
        raise ArithmeticError("sampled finite immersion failed before R604 observation")
    normal=cross/cross_length[...,None]
    normal0=(-z1*er[None,:,:]+a1*ez)/b
    k=np.maximum(abs(values(geometry["curvature"][0])),
                 abs(values(geometry["curvature"][1])))
    fields={
        "C0_displacement":np.linalg.norm(X-X0,axis=-1),
        "C1_difference_operator_norm":matrix_norm_two_columns(dfirst,dsecond),
        "first_derivative_operator_norm":matrix_norm_two_columns(first,second),
        "normal_projection_difference":np.linalg.norm(np.cross(normal,normal0),axis=-1),
        "original_operator_curvature_max":k}
    maxima={}
    for name,field in fields.items():
        if not np.all(np.isfinite(field)):
            raise ArithmeticError("nonfinite R604 finite observation")
        i,j=np.unravel_index(int(np.argmax(field)),field.shape)
        maxima[name]={"value":float(field[i,j]),"s":float(model.s[i]),
            "theta":float(theta[j]),"radial_index":int(i),"angular_index":int(j)}
    ref_km=np.abs(ref["a1"]*ref["z2"]-ref["z1"]*ref["a2"])/ref["speed"]**3
    ref_kc=np.abs(ref["z1"])/(ref["a"]*ref["speed"])
    result={"maxima":maxima,"reference_radius_min":float(np.min(ref["a"])),
        "reference_speed_min":float(np.min(ref["speed"])),
        "reference_z_s_min":float(np.min(ref["z1"])),
        "reference_curvature_max":float(max(np.max(ref_km),np.max(ref_kc))),
        "radial_nodes":len(model.s),"angular_nodes":len(theta),
        "new_geometry_or_AD_calls":0,"new_seed_or_shooting_calls":0,
        "seconds":time.monotonic()-started}
    COUNTS["reused_geometry_blocks"]+=1
    COUNTS["observed_radial_angular_points"]+=len(model.s)*len(theta)
    return result


class NormAccumulator:
    def __init__(self,reference_q):
        self.reference_q=np.asarray(reference_q,dtype=float).copy()
        self.maxima={}
        self.blocks=0
        self.points=0
        self.seconds=0.
        self.reference_radius_min=math.inf
        self.reference_speed_min=math.inf
        self.reference_z_s_min=math.inf
        self.reference_curvature_max=0.
        self.unavailable_blocks=[]

    def add(self,model,geometry,radial_offset):
        started=time.monotonic()
        try:
            part=observe_completed_geometry(model,geometry,self.reference_q)
        except (ArithmeticError,ValueError) as error:
            self.seconds+=time.monotonic()-started
            self.unavailable_blocks.append({"radial_offset":int(radial_offset),
                "radial_nodes":len(model.s),"first_s":float(model.s[0]),
                "last_s":float(model.s[-1]),"reason":str(error)})
            COUNTS["unavailable_reference_norm_blocks"]+=1
            return
        for name,item in part["maxima"].items():
            candidate=dict(item)
            candidate["radial_index"]+=int(radial_offset)
            if name not in self.maxima or candidate["value"]>self.maxima[name]["value"]:
                self.maxima[name]=candidate
        for name in ("reference_radius_min","reference_speed_min","reference_z_s_min"):
            setattr(self,name,min(getattr(self,name),part[name]))
        self.reference_curvature_max=max(self.reference_curvature_max,part["reference_curvature_max"])
        self.blocks+=1
        self.points+=part["radial_nodes"]*part["angular_nodes"]
        self.seconds+=part["seconds"]

    def report(self,current_height):
        cap_delta=abs(float(current_height)-float(self.reference_q[-1]))
        maxima={k:dict(v) for k,v in self.maxima.items()}
        if not maxima:
            return {"schema":SCHEMA,"complete_sampled_scan_accumulated":False,
                "unavailable_blocks":self.unavailable_blocks,"seconds":self.seconds,
                "continuous_norms_certified":False,"R604_reach_conclusion_claimed":False,
                "observation_unavailability_does_not_change_original_acceptance":True}
        if cap_delta>maxima["C0_displacement"]["value"]:
            maxima["C0_displacement"]={"value":cap_delta,"piece":"two full flat cap disks",
                "s":None,"theta":None,"radial_index":None,"angular_index":None}
        if maxima["first_derivative_operator_norm"]["value"]<1.:
            maxima["first_derivative_operator_norm"]={"value":1.,"piece":"two full flat cap disks",
                "s":None,"theta":None,"radial_index":None,"angular_index":None}
        return {"schema":SCHEMA,"complete_sampled_scan_accumulated":not self.unavailable_blocks,
            "maxima":maxima,"blocks":self.blocks,"radial_angular_points":self.points,
            "unavailable_blocks":self.unavailable_blocks,
            "observed_maxima_do_not_bound_unavailable_blocks":bool(self.unavailable_blocks),
            "observation_unavailability_does_not_change_original_acceptance":True,
            "seconds":self.seconds,"cap_disk_translation_difference":cap_delta,
            "reference_radius_min":self.reference_radius_min,
            "reference_speed_min":self.reference_speed_min,
            "reference_z_s_min":self.reference_z_s_min,
            "reference_curvature_max":self.reference_curvature_max,
            "reference_identity":"original circular 81q mean entries64:81, core radius .38, same mu/nu",
            "reference_is_a_candidate_not_an_already_certified_closed_reach_model":True,
            "central_cylinder_uses_the_s_zero_curve_when_exact_open_core_definition_holds":True,
            "lower_half_norms_agree_under_the_exact_mirror_isometry":True,
            "flat_cap_bounds_use_the_same_radius_and_complete_disk_definition":True,
            "operator_space_jets_retain_original_FFT_and_material_error_qualifications":True,
            "original_operator_curvature_smoothing_is_not_removed":True,
            "continuous_norms_certified":False,"reference_normal_chord_rho_certified":False,
            "R604_reach_conclusion_claimed":False,"new_geometry_or_AD_calls":0}


def conditional_reach_budget(rho,delta,nu,lam,curvature):
    """Only algebra on supplied bounds; no validation of their hypotheses."""
    if not (rho>0 and delta>=0 and 0<=nu<=1 and lam>0 and curvature>0):
        raise ValueError("invalid R604 conditional constants")
    distance=2*rho*math.tanh(math.pi/(4*lam*curvature*rho))
    if distance<=2*delta:
        return {"applicable_if_bounds_certified":False,
            "reason":"C0 displacement consumes the available near-chord threshold",
            "near_chord_threshold":distance,"hypotheses_certified_by_this_function":False}
    far=(distance-2*delta)**2/(distance*distance/rho+2*nu*distance+4*delta)
    return {"applicable_if_bounds_certified":True,"near_chord_threshold":distance,
        "conditional_reach_lower_bound":min(1/curvature,far),
        "hypotheses_certified_by_this_function":False,
        "floating_formula_evaluation_is_not_an_outward_rounded_bound":True}
