#!/usr/bin/env python3
"""Shared original168 scalar/position/selected-body/full-suffix value and J chain.

Import-only; no ordinary field.geometry, original actual, CLI or test is called.
Saved source arrays stay read-only. Every missing preparation and every real
new/repeated geometry or derivative operation belongs to the external clock.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import time
import numpy as np

from frame_collar_bvp import periodic_operator
from frame_complete_body_extension168 import (
    LEFT_EXACT,RIGHT_EXACT,LENGTH_EXACT,array_binding)
from frame_complete_body_extension168_joint_selected import _validate_first_jets
from frame_complete_body_extension168_selected_cache import bind_selected_current168_geometry
from frame_complete_body_extension168_curvature_prediction import _validate_metric
from frame_selected_row_radial_jacobian import angular_kernels,virtual_selected_jets,expand_radial_rows
from frame_metric_spectral_recovery import spectral_proposal_rows,spectral_parameter_rows
from frame_curvature_mixed_grid_steps import selected_physical_derivatives
from frame_curvature_psd import curvature_values,independent_principal_curvatures
from frame_metric_current168_fixed_ring_prefix102 import _slice_radial
from frame_metric_current168_joint168_body_suffix import (
    POLICY,LABELS,POSITION_KEYS,ALL_POSITION_KEYS,SCALAR_KEYS,ROW_NAMES,SUFFIX_LEFT_EXACT,
    _require,_error,_wall,_finite,_same,_vector,_paid_array,_Trace,
    _curvature_differentials,_curvature_rows_from_differentials,digest)

OWNED_WIDTH=4
HEIGHT_COLUMNS=(154,155,156,157,158,167)

def _new_last3(field,radial):
    from scipy.interpolate import BSpline
    old=field.original_field._direct_single
    basis=old.source.field_basis;full=basis.full
    _require(basis.count==9 and not basis.endpoint_weight and full.k==5,
        "literal original retained nine quintics")
    _require(float(full.t[9])>=old.entry.left+old.entry.length,
        "last3 original support lies beyond both entry weights")
    last=BSpline(full.t,full.c[:,9:12],full.k,extrapolate=False,axis=full.axis)
    inside=(radial>basis.left)&(radial<basis.right)
    out=[]
    for order in range(3):
        a=np.zeros((len(radial),3));a[inside]=last(radial[inside],nu=order)
        out.append(_finite(a,(len(radial),3),"missing original last3 radial jet"))
    return tuple(out),{"degree":5,"full_spline_indices":[9,10,11],
        "knots_binary64":_vector(np.asarray(full.t)),
        "first6_original_weighted_arrays_restored_not_recomputed":True,
        "last3_entry_weights_equal_one_where_nonzero":True}

def _new_body_height(field,radial):
    left,right,ell=(float(Q(v)) for v in (LEFT_EXACT,RIGHT_EXACT,LENGTH_EXACT))
    active=(radial>left)&(radial<right)
    xi=(radial[active]-left)/ell
    take=(xi>0)&(xi<1);ids=np.flatnonzero(active)[take];xi=xi[take]
    body={};local={}
    for name,power in (("u",5),("v",8)):
        out=[np.zeros_like(radial) for _ in range(3)]
        d=1-xi;exp=np.exp(-xi/d);q=d**-2;r3=d**-3;base=xi**power
        parts=(base,power*xi**(power-1)-q*base,
            power*(power-1)*xi**(power-2)-2*power*q*xi**(power-1)+(q*q-2*r3)*base)
        for j,p in enumerate(parts):
            out[j][ids]=exp*p
            _require(np.all(np.isfinite(out[j])),"finite original body radial derivatives")
        local[name]=out;body[name]=tuple(out[j][:,None]/ell**j for j in range(3))
    null=field.original_field.null_basis
    hh={"center":_finite(null.values(radial,integral=True),(len(radial),5),"exact-null primitive"),
        "b":_finite(null.values(radial),(len(radial),5),"exact-null b"),
        "b_s":_finite(null.values(radial,1),(len(radial),5),"exact-null b_s")}
    additions={"center":ell*local["v"][0],"b":local["v"][1],"b_s":local["v"][2]/ell}
    height={key:np.column_stack((value,additions[key])) for key,value in hh.items()}
    return body,height,{"body_definition":{"left_exact":LEFT_EXACT,"right_exact":RIGHT_EXACT,
        "length_exact":LENGTH_EXACT,"powers":[5,8],"orders":[0,1,2]},
        "height_columns":list(HEIGHT_COLUMNS),"null_basis_sha256":null.identity_sha256,
        "complete_exact_null_primitive_is_required_for_body_X":True,
        "body_height_center_is_length_times_P8":True,
        "body_height_b_is_P8_xi_prime":True,
        "body_height_b_s_is_P8_xi_second_over_length":True}

def _new_Q_angles(field,theta):
    value,first,error=field.original_field._direct_single.Q.evaluate(theta)
    return _finite(value,(len(theta),),"original Q angular")[:,None],\
        _finite(first,(len(theta),),"original Q angular first")[:,None],float(error)

def _row_tolerances(cfg):
    out=np.asarray([cfg["metric_row_tolerance"]]*2+[cfg["signed_height_tolerance"]]
        +[cfg["shape_constraint_tolerance"]]*3+[cfg["mirror_polynomial_tolerance"]]
        +[cfg["curvature_row_tolerance"]]*4,dtype=float)
    _require(out.shape==(11,) and np.all(np.isfinite(out)) and np.all(out>=0),"original11 tolerances")
    return out

def prepare_geometry(model,prepared,completed,first_jet_bounds,metric_bound,trace):
    r=_finite(prepared["radial"],(len(prepared["radial"]),),"original full radial")
    model.radial=r;nr=len(r)
    model.thetas={"coarse":_finite(prepared["theta"],(384,),"original coarse theta"),
                  "fine":_finite(prepared["fine_theta"],(768,),"original fine theta")}
    model.metric=_validate_metric(model.field,r,metric_bound)
    model.base_first={};model.selected_bounds={};model.layouts={};model.pools={}
    model.pool_versions={};model.seed_fields={};model.families={}
    model.body_row_tolerances=_row_tolerances(model.cfg)
    original=completed["paid_prefix_model"];source=original["new_paid_input"]
    _require(_same(_paid_array(source["radial"],(nr,),"prefix full radial"),r),"source radial identity")
    model.seed_height={name:_paid_array(source["fixed_height_derivatives"][name],(nr,),"paid q_R "+name)
        for name in ("b","b_s")}
    model.suffix_ids=np.asarray([j for j,s in enumerate(r) if Q.from_float(float(s))>=Q(SUFFIX_LEFT_EXACT)],dtype=np.int64)
    _require(len(model.suffix_ids)==21 and 141 in model.suffix_ids,"all original21 suffix rows")
    model.last3_radial,radial_receipt=trace.run("new_last3_complete_radial_input",
        lambda:_new_last3(model.field,r),lambda x:model.build_sink.__setitem__("_new_last3_radial",x[0]))
    model.body_radial,model.height_basis,height_receipt=trace.run("new_complete_body_and_height_input",
        lambda:_new_body_height(model.field,r),
        lambda x:model.build_sink.__setitem__("_new_body_height_arrays",{"body":x[0],"height":x[1]}))
    cache=completed["accepted_cache"];cp=prepared["replay"]["source_checkpoint"]
    bindings={};angle_receipts={}
    for label in LABELS:
        th=model.thetas[label];nt=len(th)
        _require(_same(_paid_array(source["theta"][label],(nt,),"paid prefix "+label+" angles"),th),
            "literal original prefix angle identity")
        _,_,_,data=_validate_first_jets(model.field,model.accepted_state168,r,th,first_jet_bounds[label])
        model.base_first[label]=data
        for key in ("a","a_s"):
            _require(_same(data["metric"][key],model.metric[key]),"same restored fixed metric in first jets")
        ids=np.asarray(prepared[label+"_pool"],dtype=np.int64)
        _require(ids.ndim==1 and len(ids)==(4454 if label=="coarse" else 4549)
            and len(np.unique(ids))==len(ids) and np.all((0<=ids)&(ids<11*nr*nt))
            and ids.tolist()==cp[label+"_pool"],"literal accepted58 complete pool/order")
        version=int(cp[label+"_pool_version"])
        _require(version==(15 if label=="coarse" else 14),"original pool version")
        model.pools[label]=ids;model.pool_versions[label]=version
        saved=cache["selected_current168_geometry"][label]
        owner=cache["binding"]["selected_current168_geometry"][label]
        bound=bind_selected_current168_geometry(model.field,model.accepted_state168,r,th,ids,saved,model.cfg,
            grid_label=label,side=model.side,pool_version=version,
            expected_binding_sha256=owner["binding_sha256"],wall=lambda:_wall(model.wall,POLICY+".paid-selected-bind"))
        model.selected_bounds[label]=bound;paid=bound["arrays"]
        body_points=paid["point_ids"];suf_points=(model.suffix_ids[:,None]*nt+np.arange(nt)[None,:]).ravel()
        union=np.unique(np.r_[body_points,suf_points]).astype(np.int64)
        slots=np.searchsorted(union,body_points)
        model.layouts[label]={"pool_ids":ids,"groups":ids//(nr*nt),"pool_points":ids%(nr*nt),
            "body_points":body_points,"body_ri":body_points//nt,"body_ti":body_points%nt,
            "pool_body_slots":np.searchsorted(body_points,ids%(nr*nt)),
            "union_points":union,"union_ri":union//nt,"union_ti":union%nt,
            "body_union_slots":slots,"pool_union_slots":np.searchsorted(union,ids%(nr*nt)),
            "suffix_points":suf_points,"suffix_union_slots":np.searchsorted(union,suf_points),
            "suffix_ri":suf_points//nt,"suffix_ti":suf_points%nt}
        model.seed_fields[label]={name:{key:_paid_array(source["source_scalar_fields"][label][name][key],
            (nr,nt),"paid q_R/"+label+"/"+name+"/"+key) for key in SCALAR_KEYS} for name in ("u","v")}
        uv={}
        for name,modes in (("u",9),("v",8)):
            f=source["original_families"][label][name]
            angle=_paid_array(f["angular"],(nt,modes),"paid "+label+"/"+name+"/angle")
            first=_paid_array(f["angular_first"],(nt,modes),"paid "+label+"/"+name+"/first")
            first6=tuple(_paid_array(f["radial"][j],(nr,6),"paid first6 radial") for j in range(3))
            radial=tuple(np.concatenate((first6[j],model.last3_radial[j]),axis=1) for j in range(3))
            uv[name]={"name":name,"angular":angle,"angular_first":first,"radial":radial,
                "body":model.body_radial[name],"modes":modes,
                "old_columns":list(range(0,81)) if name=="u" else list(range(81,153)),
                "body_columns":list(range(159,163)) if name=="u" else list(range(163,167))}
        qa,qap,qerr=trace.run("new_missing_original_Q_angular_input",
            lambda th=th:_new_Q_angles(model.field,th),
            lambda v,label=label:model.build_sink.setdefault("_new_Q_arrays",{}).__setitem__(label,v[:2]),
            grid=label,original_radial_Q_reused_from_paid_v_first_column=True)
        qfam={"name":"v","angular":qa,"angular_first":qap,
            "radial":tuple(uv["v"]["radial"][j][:,:1] for j in range(3)),
            "body":None,"modes":1,"old_columns":[153],"body_columns":[],"family_name":"Q"}
        model.families[label]=(uv["u"],uv["v"],qfam)
        angle_receipts[label]={"original_Q_inverse_error":qerr,
            "Q_angular_binding":array_binding(qa),"Q_angular_first_binding":array_binding(qap)}
        bindings[label]={"first_jets":first_jet_bounds[label]["binding_sha256"],
            "selected_geometry":bound["binding_sha256"],"pool":array_binding(ids),"pool_version":version,
            "union_points":array_binding(union),"literal_selected_points":array_binding(body_points),
            "suffix_points":array_binding(suf_points),
            "saved_selected_X_and_all_two_jets_are_not_fullgrid_surrogates":True}
    model.input_receipt={"schema":POLICY+"-shared-input-binding",
        "fixed_metric":metric_bound["binding_sha256"],
        "prefix_source_binding":original["binding_sha256"],"grids":bindings,
        "new_last3_radial":radial_receipt,"new_body_height":height_receipt,"new_Q_angles":angle_receipts,
        "body_radial_bindings":{name:[array_binding(a) for a in rows] for name,rows in model.body_radial.items()},
        "height_basis_bindings":{name:array_binding(a) for name,a in model.height_basis.items()},
        "old_Q_radial_is_literal_paid_W5_B3_column":True,
        "all_original_pool_groups_retained":True,
        "both_domains_share_new_actualq_geometry":True,
        "new_model_queries_have_no_original_full_ordinary_call":True,
        "no_closed_full62_scientific_arrays_recovered_from_bindings":True}

def _fields(model,q,label):
    nr,nt=len(model.radial),len(model.thetas[label])
    out={"_theta":model.thetas[label][None,:]}
    delta=np.asarray([float(Q.from_float(float(a))-Q.from_float(float(b)))
        for a,b in zip(q,model.ring_candidate168)])
    for fam in model.families[label][:2]:
        name=fam["name"];coeff=delta[fam["old_columns"]].reshape(9,fam["modes"])
        out[name]={}
        for j,key in enumerate(("value","s","ss")):
            out[name][key]=model.seed_fields[label][name][key]+np.einsum(
                "ri,im,tm->rt",fam["radial"][j],coeff,fam["angular"])
        out[name]["theta"]=model.seed_fields[label][name]["theta"]+np.einsum(
            "ri,im,tm->rt",fam["radial"][0],coeff,fam["angular_first"])
        dc=delta[fam["body_columns"]]
        if np.any(dc!=0.):
            aa=fam["angular"][:,:4]@dc;ap=fam["angular_first"][:,:4]@dc
            for j,key in enumerate(("value","s","ss")):
                out[name][key]+=fam["body"][j]*aa[None,:]
            out[name]["theta"]+=fam["body"][0]*ap[None,:]
    if delta[153]!=0.:
        fam=model.families[label][2]
        for j,key in enumerate(("value","s","ss")):
            out["v"][key]+=delta[153]*fam["radial"][j]*fam["angular"].T
        out["v"]["theta"]+=delta[153]*fam["radial"][0]*fam["angular_first"].T
    _require(all(np.all(np.isfinite(out[name][key])) for name in ("u","v") for key in SCALAR_KEYS),
        "finite shared complete original scalar fields")
    return out

def _frame(fields,paid_T=None):
    u,v=fields["u"]["value"],fields["v"]["value"]
    psi=fields["_theta"]+u;zero=np.zeros_like(u)
    N=np.stack((np.cos(psi),np.sin(psi),zero),axis=-1)
    H=np.stack((-np.sin(psi),np.cos(psi),zero),axis=-1)
    ez=np.stack((zero,zero,np.ones_like(u)),axis=-1);c=1/np.sqrt(1+v*v)
    Tu,Tv=-c[...,None]*N,(c**3)[...,None]*(ez-v[...,None]*H)
    Tuu,Tuv=-c[...,None]*H,(v*c**3)[...,None]*N
    Tvv=((2*v*v-1)*c**5)[...,None]*H-(3*v*c**5)[...,None]*ez
    us,vs=fields["u"]["s"],fields["v"]["s"]
    return {"T":paid_T if paid_T is not None else c[...,None]*H+(v*c)[...,None]*ez,
        "Ts":us[...,None]*Tu+vs[...,None]*Tv,
        "Tss":(us*us)[...,None]*Tuu+(2*us*vs)[...,None]*Tuv+(vs*vs)[...,None]*Tvv
            +fields["u"]["ss"][...,None]*Tu+fields["v"]["ss"][...,None]*Tv,
        "Ttheta":(1+fields["u"]["theta"])[...,None]*Tu+fields["v"]["theta"][...,None]*Tv,
        "Tpart":{"u":Tu,"v":Tv},
        "Ts_value_part":{"u":us[...,None]*Tuu+vs[...,None]*Tuv,
                         "v":us[...,None]*Tuv+vs[...,None]*Tvv}}

def _height(model,q):
    delta=np.asarray([float(Q.from_float(float(q[i]))-Q.from_float(float(model.ring_candidate168[i])))
        for i in HEIGHT_COLUMNS])
    return {key:model.seed_height[key]+model.height_basis[key]@delta for key in ("b","b_s")}

def _baseline(model,sink):
    if model.baseline_cache is not None:
        _require(model.baseline_cache.get("status")=="complete","a failed baseline preparation is not silently retried")
        return model.baseline_cache
    trace=_Trace(model.wall,sink)
    base={"status":"entered","grids":{}}
    model.baseline_cache=base;sink["_shared_baseline_partial"]=base
    try:
        base["height"]=_height(model,model.accepted_state168)
        for label in LABELS:
            work={};base["grids"][label]=work
            fields=trace.run("new_baseline_derivative_scalar_input",
                lambda label=label:_fields(model,model.accepted_state168,label),
                lambda v:work.__setitem__("fields",v),grid=label)
            frame=trace.run("new_baseline_derivative_frame_input_without_T_replay",
                lambda label=label:_frame(fields,model.base_first[label]["T"]),
                lambda v:work.__setitem__("frame",v),grid=label)
            model.shared_counts["baseline_frame_preparations"]+=1
            pi={}
            work["primitives"]=pi
            for key in ("T","Ts"):
                trace.run("new_missing_baseline_angular_primitive",
                    lambda key=key:periodic_operator(frame[key],-1),
                    lambda v,key=key:pi.__setitem__(key,v),grid=label,source_array=key)
                model.shared_counts["baseline_primitive_calls"]+=1
        base["status"]="complete"
        return base
    except Exception as error:
        base.update(status="raised",error=_error(error));raise

def _take(data,indices,count):
    return {key:(value[indices] if isinstance(value,np.ndarray) and value.ndim and value.shape[0]==count else value)
        for key,value in data.items()}

def _curvature_at_K(model,c,K):
    if K==model.cap:
        factor=K/model.curvature_scale
        return c,c["rows"]*np.asarray((factor,factor*factor,factor,factor*factor))
    q=c["q"];tau=1/K
    h11=np.stack((q*c["E"]+tau*c["e"],q*c["E"]-tau*c["e"]),axis=-1)
    h12=np.stack((q*c["F"]+tau*c["f"],q*c["F"]-tau*c["f"]),axis=-1)
    h22=np.stack((q*c["G"]+tau*c["k"],q*c["G"]-tau*c["k"]),axis=-1)
    tr=h11+h22;det=h11*h22-h12*h12
    rows=np.stack((tr[:,0],det[:,0],tr[:,1],det[:,1]),axis=-1)
    answer=dict(c);answer.update(h11=h11,h12=h12,h22=h22,rows=rows,tau=tau)
    factor=K/model.curvature_scale
    return answer,rows*np.asarray((factor,factor*factor,factor,factor*factor))

def _body_rows(model,label,X,U,T,metric_rows,curvature,scaled):
    W=np.cross(U,T);area2=np.sum(W*W,axis=-1);z=X[:,2]
    ball=float(Q(model.cfg["hard_ball_radius_exact"]))
    strip=float(Q(model.cfg["hard_strip_half_width_exact"]))
    tau=float(Q(model.cfg["mirror_target_exact"]))
    rows=np.empty((11,len(X)),dtype=float)
    rows[:2]=metric_rows
    rows[2]=model.side*z-float(Q(model.cfg["minimum_signed_height_exact"]))
    rows[3]=1-np.sum(X*X,axis=-1)/ball**2
    rows[4]=1-X[:,1]/strip;rows[5]=1+X[:,1]/strip
    rows[6]=z*z*area2-tau*tau*W[:,2]**2
    rows[7:]=scaled.T
    layout=model.layouts[label]
    values=rows[layout["groups"],layout["pool_body_slots"]]
    return _finite(values,(len(model.pools[label]),),"complete original selected11 values")


def _union_jets(model,label,frame,primitives,height,U,is_initial,trace,work):
    layout=model.layouts[label];ri,ti=layout["union_ri"],layout["union_ti"]
    n=len(ri);saved=model.selected_bounds[label]["arrays"]
    missing=np.ones(n,dtype=bool)
    if is_initial:
        missing[layout["body_union_slots"]]=False
    actual=np.flatnonzero(missing);ari,ati=ri[actual],ti[actual]
    need_radial=np.unique(ari)
    piss=trace.run("new_position_second_primitive_on_required_radials",
        lambda:periodic_operator(frame["Tss"][need_radial],-1),
        lambda v:work.__setitem__("second_primitive",{"radial_ids":need_radial,"values":v}),
        grid=label,actual_radial_count=len(need_radial),
        paid_initial_selected_two_jets_not_replayed=bool(is_initial))
    jri=np.searchsorted(need_radial,ari)
    def assemble():
        jets={key:np.empty((n,3),dtype=float) for key in POSITION_KEYS+("T",)}
        if is_initial:
            bs=layout["body_union_slots"]
            for key in jets:
                jets[key][bs]=saved["position_"+key]
        a,ap,app=(model.metric[key][ari,None] for key in ("a","a_s","a_ss"))
        T=frame["T"][ari,ati];Ts=frame["Ts"][ari,ati]
        jets["Xs"][actual]=U[ari,ati];jets["T"][actual]=T
        jets["Xt"][actual]=a*T
        jets["Xst"][actual]=ap*T+a*Ts
        jets["Xtt"][actual]=a*frame["Ttheta"][ari,ati]
        second=app*primitives["T"][ari,ati]+2*ap*primitives["Ts"][ari,ati]+a*piss[jri,ati]
        second[:,2]+=height["b_s"][ari]
        jets["Xss"][actual]=second
        _require(all(np.all(np.isfinite(a)) for a in jets.values()),"all actual shared union position jets finite")
        return jets
    jets=trace.run("new_shared_union_position_two_jets",assemble,
        lambda v:work.__setitem__("union_position_two_jets",v),grid=label,
        literal_paid_selected_points=0 if not is_initial else len(layout["body_points"]),
        new_point_count=len(actual))
    if not is_initial:
        model.shared_counts["selected_two_jet_queries"]+=1
    model.shared_counts["suffix_two_jet_queries"]+=1
    return jets

def evaluate_geometry(model,q,sink):
    key=q.tobytes()
    if key==model.loaded_geometry_key:
        model.full_point_counts["cache_hits"]+=1
        sink["_last_complete_geometry"]=model.loaded_geometry
        return model.loaded_geometry
    model.temporary.evict("geometry",int(model.loaded_geometry is not None))
    model.temporary.evict("physical_derivative_blocks",len(model.derivative_input_cache))
    model.temporary.evict("final_J",int(model.loaded_J is not None))
    model.loaded_geometry=None;model.loaded_geometry_key=None
    model.derivative_input_cache.clear();model.loaded_J=None;model.loaded_J_key=None
    model.full_point_counts["started"]+=1
    if key in model.seen_geometry_keys:
        model.full_point_counts["recomputed_after_eviction"]+=1
    else:
        model.seen_geometry_keys.add(key);model.full_point_counts["distinct_new_physical_points"]+=1
    ordinal=model.full_point_counts["started"];is_initial=_same(q,model.accepted_state168)
    partial={"schema":POLICY+"-geometry-partial","status":"entered","state168":q,
        "new_joint_geometry_ordinal":ordinal,"actual58_literal_input_reuse":bool(is_initial),
        "completed_grids":{},"working_grid":None}
    sink["_last_geometry_partial"]=partial
    trace=_Trace(model.wall,sink);tick=time.monotonic()
    try:
        base=_baseline(model,sink)
        height=trace.run("new_actual_height_from_complete_null_inputs",
            lambda:_height(model,q),lambda v:partial.__setitem__("height",v))
        center_delta=np.asarray([float(Q.from_float(float(q[i]))-Q.from_float(float(model.accepted_state168[i])))
            for i in HEIGHT_COLUMNS])
        delta_center=model.height_basis["center"]@center_delta
        partial["height_primitive_increment"]=delta_center
        grids={}
        if is_initial:
            model.full_point_counts["paid58_firstjet_and_selected_identity_hits"]+=1
        for label in LABELS:
            layout=model.layouts[label];nt=len(model.thetas[label]);nr=len(model.radial)
            work={"grid":label,"status":"entered"};partial["working_grid"]=work
            source=model.base_first[label]
            if is_initial:
                fields=base["grids"][label]["fields"];frame=base["grids"][label]["frame"]
                primitives=base["grids"][label]["primitives"]
                U,T,e,f=source["U"],source["T"],source["e"],source["f"]
                work["paid_full58_U_T_e_f_read_without_query"]=True
            else:
                fields=trace.run("new_wholebody_scalar_increment_fields",
                    lambda label=label:_fields(model,q,label),
                    lambda v:work.__setitem__("scalar_fields",v),grid=label,geometry_ordinal=ordinal)
                frame=trace.run("new_wholebody_tangent_and_derivative_frame",
                    lambda:_frame(fields),lambda v:work.__setitem__("frame",v),
                    grid=label,geometry_ordinal=ordinal)
                model.shared_counts["wholebody_scalar_frame_queries"]+=1
                primitives={};work["primitive_arrays"]=primitives
                for name in ("T","Ts"):
                    trace.run("new_wholebody_complete_angle_primitive",
                        lambda name=name:periodic_operator(frame[name],-1),
                        lambda v,name=name:primitives.__setitem__(name,v),
                        grid=label,source_array=name,geometry_ordinal=ordinal)
                def first_jets():
                    basepi=base["grids"][label]["primitives"]
                    U=source["U"]+model.metric["a_s"][:,None,None]*(primitives["T"]-basepi["T"])
                    U+=model.metric["a"][:,None,None]*(primitives["Ts"]-basepi["Ts"])
                    U[...,2]+=height["b"][:,None]-base["height"]["b"][:,None]
                    T=frame["T"];e=np.sum(U*U,axis=-1)-1.;f=np.sum(U*T,axis=-1)
                    return {"U":U,"T":T,"e":e,"f":f}
                current=trace.run("new_complete_body_first_jets_and_metric",first_jets,
                    lambda v:work.__setitem__("global_first_jets",v),grid=label,geometry_ordinal=ordinal)
                U,T,e,f=(current[name] for name in ("U","T","e","f"))
                model.shared_counts["wholebody_firstjet_queries"]+=1
            eta=trace.run("new_full_body_unsmoothed_metric_values",
                lambda:(abs(e)+np.hypot(e,2*f))/2,lambda v:work.__setitem__("global_eta",v),
                grid=label,geometry_ordinal=ordinal)
            metric_rows=trace.run("new_internal_metric_proposal_values",
                lambda:spectral_proposal_rows(e,f,model.internal_metric_budget,model.epsilon),
                lambda v:work.__setitem__("global_internal_metric_rows",v),
                grid=label,geometry_ordinal=ordinal)
            jets=_union_jets(model,label,frame,primitives,height,U,is_initial,trace,work)
            curv=trace.run("new_union_original_unsquared_curvature_values",
                lambda:curvature_values(jets,model.metric["a"][layout["union_ri"]],1/model.cap,area_floor=model.area_floor),
                lambda v:work.__setitem__("union_curvature_inputs",v),
                grid=label,geometry_ordinal=ordinal,unique_point_count=len(layout["union_points"]))
            principal=trace.run("new_union_direct_principal_curvatures",
                lambda:independent_principal_curvatures(curv),
                lambda v:work.__setitem__("union_principal_curvatures",v),
                grid=label,geometry_ordinal=ordinal)
            model.shared_counts["union_curvature_queries"]+=1
            bri,bti=layout["body_ri"],layout["body_ti"]
            saved=model.selected_bounds[label]["arrays"]
            if is_initial:
                X=saved["position_X"]
            else:
                X=saved["position_X"]+model.metric["a"][bri,None]*(
                    primitives["T"][bri,bti]-base["grids"][label]["primitives"]["T"][bri,bti])
                X[:,2]+=delta_center[bri]
            bs=layout["body_union_slots"];cbody=_take(curv,bs,len(layout["union_points"]))
            _,scaled=_curvature_at_K(model,cbody,model.cap)
            bodyvalues=trace.run("new_all_original_selected11_values",
                lambda:_body_rows(model,label,X,U[bri,bti],T[bri,bti],metric_rows[:,bri,bti],cbody,scaled),
                lambda v:work.__setitem__("literal_body_pool_values",v),grid=label,geometry_ordinal=ordinal,
                pool_rows=len(model.pools[label]))
            _require(all(np.all(np.isfinite(a)) for a in (U,T,e,f,eta,metric_rows,principal,X)),
                "finite shared geometry")
            grid={"fields":fields,"frame":frame,"primitives":primitives,"height":height,
                "U":U,"T":T,"e":e,"f":f,"eta":eta,"metric_rows":metric_rows,
                "union_jets":jets,"union_curvature":curv,"union_principal":principal,
                "body_X":X,"body_values":bodyvalues,
                "actual58_selected_jets_restored":bool(is_initial)}
            grids[label]=grid;partial["completed_grids"][label]=grid
            work["status"]="complete";partial["working_grid"]=None
        answer={"state168":q,"grids":grids,"new_joint_geometry_ordinal":ordinal,
            "height":height,"actual58_literal_input_reuse":bool(is_initial)}
        partial.update(status="complete",geometry=answer)
        model.loaded_geometry_key,model.loaded_geometry=key,answer
        sink["_last_complete_geometry"]=answer
        model.full_point_counts["completed"]+=1
        return answer
    except Exception as error:
        partial["error"]=_error(error)
        if partial.get("status")!="complete":
            partial["status"]="raised";model.full_point_counts["failed"]+=1
        else:
            partial["completed_arrays_retained_before_post_call_failure"]=True
        raise
    finally:
        partial["seconds"]=time.monotonic()-tick
        sink["new_geometry_counts"]=copy.deepcopy(model.full_point_counts)
        sink["shared_component_scientific_counts"]=copy.deepcopy(model.shared_counts)

def _grid_summary(model,label,grid,K,suffix_scaled):
    layout=model.layouts[label];eta=grid["eta"];nt=len(model.thetas[label])
    at=np.unravel_index(int(np.argmax(eta)),eta.shape)
    maximum=float(eta[at]);sids=layout["suffix_union_slots"];bids=layout["body_union_slots"]
    s_eta=eta[model.suffix_ids];s_at=np.unravel_index(int(np.argmax(s_eta)),s_eta.shape)
    sc=grid["union_principal"][sids];bc=grid["union_principal"][bids]
    sq=grid["union_curvature"]["q"][sids];bq=grid["union_curvature"]["q"][bids]
    bodyvalues=grid["body_values"];groups=layout["groups"];hard=groups>=2
    tol=model.body_row_tolerances[groups[hard]]
    _,body_psd=_curvature_at_K(model,_take(grid["union_curvature"],bids,len(layout["union_points"])),model.cap)
    body_gates={"all_selected_original_hard_rows":bool(np.all(bodyvalues[hard]>=-tol)),
        "selected_points_original_unsquared_PSD":bool(np.min(body_psd)>=-model.curvature_row_tolerance),
        "selected_points_direct_hard58":bool(np.max(abs(bc))<=model.cap+model.direct_curvature_tolerance),
        "selected_points_original_normal_area":bool(np.min(bq)>model.area_floor)}
    suffix_gates={"original_unsmoothed_metric_budget":bool(np.max(s_eta)<=model.metric_budget),
        "original_unsquared_PSD_at_returned_K":bool(np.min(suffix_scaled)>=-model.curvature_row_tolerance),
        "direct_curvature_at_returned_K":bool(np.max(abs(sc))<=K+model.direct_curvature_tolerance),
        "original_hard58_curvature":bool(np.max(abs(sc))<=model.cap+model.direct_curvature_tolerance),
        "original_normal_area":bool(np.min(sq)>model.area_floor)}
    global_gate=maximum<=model.metric_budget
    return {"grid":label,"actual_shared_state_domain":"same complete168 field, regrouped finite arithmetic",
        "global_metric":{"maximum_eta":maximum,"original_metric_budget":model.metric_budget,
            "internal_solver_budget":model.internal_metric_budget,
            "original_budget_minus_eta":model.metric_budget-maximum,
            "internal_budget_minus_eta":model.internal_metric_budget-maximum,
            "original_budget_pass":bool(global_gate),
            "attainer":{"radial_index":int(at[0]),"theta_index":int(at[1]),
                "s":float(model.radial[at[0]]),"theta":float(model.thetas[label][at[1]])}},
        "body_selected":{"pool_rows":len(bodyvalues),"pool_version":model.pool_versions[label],
            "hard_minimum":float(np.min(bodyvalues[hard])),
            "minimum_normal_area":float(np.min(bq)),
            "maximum_absolute_principal_curvature":float(np.max(abs(bc))),
            "gates":body_gates,"all_gates_pass":bool(all(body_gates.values()))},
        "suffix":{"radial_count":21,"theta_count":nt,"maximum_eta":float(np.max(s_eta)),
            "maximum_absolute_principal_curvature":float(np.max(abs(sc))),
            "minimum_normal_area":float(np.min(sq)),"K":K,
            "scaled_PSD_minima":dict(zip(ROW_NAMES[2:],map(float,np.min(suffix_scaled,axis=0)))),
            "eta_attainer":{"radial_index":int(model.suffix_ids[s_at[0]]),"theta_index":int(s_at[1]),
                "s":float(model.radial[model.suffix_ids[s_at[0]]]),"theta":float(model.thetas[label][s_at[1]])},
            "gates":suffix_gates,"all_gates_pass":bool(all(suffix_gates.values()))},
        "all_joint_original_necessary_gates_pass":bool(global_gate and all(body_gates.values()) and all(suffix_gates.values())),
        "canonical_fullbody_prediction_and_original_actual14_still_required":True}

def evaluate_value(model,backend,sink,*,state168=None):
    x=_finite(backend,(170,),"new joint backend170")
    _require(x[168]>0,"positive suffix K")
    q=model.point_from_backend(x) if state168 is None else state168
    geometry=model._geometry(q,sink);trace=_Trace(model.wall,sink)
    rows=[];summaries={}
    for label in LABELS:
        grid=geometry["grids"][label];layout=model.layouts[label]
        c=_take(grid["union_curvature"],layout["suffix_union_slots"],len(layout["union_points"]))
        _,scaled=trace.run("current_K_suffix_PSD_value_assembly",
            lambda c=c:_curvature_at_K(model,c,float(x[168])),grid=label,K=float(x[168]))
        groups=layout["groups"]
        # These are precisely the original selected hard tolerances; the
        # metric rows alone use the stricter internal budget without a shift.
        hard_shift=np.where(groups>=2,model.body_row_tolerances[groups],0.)
        rows.append(grid["body_values"]+hard_shift)
        sm=np.moveaxis(grid["metric_rows"][:,model.suffix_ids],0,-1).reshape(-1,2)
        rows.append(np.concatenate((sm,scaled),axis=1).ravel())
        summaries[label]=_grid_summary(model,label,grid,float(x[168]),scaled)
    rows.append(model.linear_b-model.linear_A@x)
    values=_finite(np.concatenate(rows),(model.constraint_count,),"complete joint residual")
    return {"backend":x,"state168":q,"values":values,"summaries":summaries,
        "joint_pass":bool(all(v["all_joint_original_necessary_gates_pass"] for v in summaries.values())),
        "geometry_key":q.tobytes(),"jacobian_key":q.tobytes()+np.asarray(x[168],dtype=np.float64).tobytes()}


def _family_columns(family):
    if family.get("family_name")=="height":
        return list(HEIGHT_COLUMNS),((154,159),(167,168))
    old=list(family["old_columns"]);body=list(family["body_columns"])
    ranges=[(old[0],old[-1]+1)]
    if body:
        ranges.append((body[0],body[-1]+1))
    return old+body,tuple(ranges)

def _expand_family(local,family,global_ri):
    if family.get("family_name")=="height":
        return local
    value=np.asarray(local,dtype=float);modes=family["modes"]
    old=expand_radial_rows(value,family["radial"],global_ri)/4
    if family["body"] is None:
        return old
    first4=value.reshape(len(global_ri),3,modes)[:,:,:4].reshape(len(global_ri),12)
    body=expand_radial_rows(first4,family["body"],global_ri)/4
    return np.concatenate((old,body),axis=1)

def _filled_rows(partial,rows,ranges,*,grid,family,domain):
    # Row order in the permanent pool is arbitrary.  Only these literal
    # completed indices, not their enclosing interval, may be hashed on failure.
    ids=np.asarray(rows,dtype=np.int64)
    if not len(ids):
        return
    for first,stop in ranges:
        partial["completed_column_blocks"].append({"grid":grid,"family":family,"domain":domain,
            "row_indices":ids,"column_start":int(first),"column_stop":int(stop)})

def assemble_jacobian(model,entry,sink):
    key=entry["jacobian_key"]
    if key==model.loaded_J_key:
        model.jacobian_counts["cache_hits"]+=1
        return model.loaded_J
    model.assert_context();model.jacobian_counts["started"]+=1
    if key in model.seen_J_keys:
        model.jacobian_counts["reassembled_after_eviction"]+=1
    else:
        model.seen_J_keys.add(key);model.jacobian_counts["distinct_q_K_keys"]+=1
    ordinal=model.jacobian_counts["started"];K=float(entry["backend"][168])
    geometry=model._geometry(entry["state168"],sink)
    J=np.empty((model.constraint_count,170),dtype=np.float64)
    partial={"status":"entered","ordinal":ordinal,"backend170":entry["backend"],
        "matrix":J,"completed_column_blocks":[],"working_kernel_arrays":None}
    sink["_last_jacobian_partial"]=partial;trace=_Trace(model.wall,sink);tick=time.monotonic()
    try:
        offset=0
        for label in LABELS:
            grid=geometry["grids"][label];layout=model.layouts[label]
            nr,nt=len(model.radial),len(model.thetas[label])
            union=layout["union_points"];nunion=len(union);ns=len(layout["suffix_points"])
            body_offset=offset;suffix_offset=offset+len(model.pools[label])
            end_offset=suffix_offset+6*ns
            c58=grid["union_curvature"]
            cs=_take(c58,layout["suffix_union_slots"],nunion)
            cK,_=trace.run("current_K_suffix_PSD_for_requested_J",
                lambda:_curvature_at_K(model,cs,K),grid=label,K=K)
            factor=K/model.curvature_scale
            E,F,G,q=(cK[name] for name in ("E","F","G","q"))
            h11,h12,h22=(cK[name]*factor for name in ("h11","h12","h22"))
            dtrace=q*(E+G)/model.curvature_scale
            ddet=(q/model.curvature_scale)[:,None]*(E[:,None]*h22+G[:,None]*h11-2*F[:,None]*h12)
            dk=np.stack((np.zeros_like(q),np.zeros_like(q),dtrace,ddet[:,0],dtrace,ddet[:,1]),axis=1)
            J[body_offset:suffix_offset,168:170]=0.
            J[suffix_offset:end_offset,168]=dk.ravel();J[suffix_offset:end_offset,169]=0.
            partial["completed_column_blocks"].append({"grid":label,"family":"K_h",
                "row_start":body_offset,"row_stop":end_offset,"column_start":168,"column_stop":170})
            radial_ids=np.unique(layout["union_ri"])
            families=list(model.families[label])+[{"family_name":"height","name":"height"}]
            for begin in range(0,len(radial_ids),OWNED_WIDTH):
                _wall(model.wall,POLICY+".shared-J.block")
                owned=radial_ids[begin:begin+OWNED_WIDTH]
                point_slots=np.flatnonzero(np.isin(layout["union_ri"],owned))
                global_ri=layout["union_ri"][point_slots];ti=layout["union_ti"][point_slots]
                ri=np.searchsorted(owned,global_ri);count=len(point_slots)
                small={name:grid["union_jets"][name][point_slots] for name in POSITION_KEYS+("T",)}
                cv=_take(c58,point_slots,nunion)
                e,f=grid["e"][global_ri,ti],grid["f"][global_ri,ti]
                body_rows=np.flatnonzero(np.isin(layout["pool_points"]//nt,owned))
                body_at=np.searchsorted(point_slots,layout["pool_union_slots"][body_rows])
                body_groups=layout["groups"][body_rows]
                physical_mask=(body_groups>=2)&(body_groups<7)
                physical_positions=np.flatnonzero(physical_mask)
                physical_at=body_at[physical_mask]
                suffix_positions=np.flatnonzero(np.isin(layout["suffix_ri"],owned))
                suffix_at=np.searchsorted(point_slots,layout["suffix_union_slots"][suffix_positions])
                body_output_rows=body_offset+body_rows
                suffix_output_rows=(suffix_offset+6*suffix_positions[:,None]+np.arange(6)[None,:]).ravel()
                fields=None;frame=None
                metric={name:values[owned] for name,values in model.metric.items()}
                for family in families:
                    name=family.get("family_name",family["name"])
                    columns,ranges=_family_columns(family)
                    derivative_key=(entry["geometry_key"],label,tuple(int(v) for v in owned),name)
                    if derivative_key in model.derivative_input_cache:
                        model.derivative_input_counts["cache_hits"]+=1
                        bundle=model.derivative_input_cache[derivative_key]
                    else:
                        model.derivative_input_counts["started"]+=1
                        if derivative_key in model.seen_derivative_keys:
                            model.derivative_input_counts["recomputed_after_eviction"]+=1
                        else:
                            model.seen_derivative_keys.add(derivative_key)
                            model.derivative_input_counts["distinct_input_keys"]+=1
                        try:
                            if name=="height":
                                kernels=None
                                def height_virtual():
                                    values={jet:np.zeros((count,3,len(HEIGHT_COLUMNS)),dtype=float)
                                        for jet in ALL_POSITION_KEYS}
                                    for jet,basis in (("X","center"),("Xs","b"),("Xss","b_s")):
                                        values[jet][:,2,:]=model.height_basis[basis][global_ri]/4
                                    return values
                                virtual=trace.run("new_shared_exact_height_J_inputs",height_virtual,
                                    lambda v:partial.__setitem__("working_virtual_position_J",v),
                                    grid=label,original_radial_ids=owned.tolist(),
                                    independent_height_columns=list(HEIGHT_COLUMNS))
                            else:
                                if fields is None:
                                    fields=_slice_radial(grid["fields"],owned,nr)
                                    frame=_slice_radial(grid["frame"],owned,nr)
                                kernels=trace.run("new_shared_full_angle_J_kernels",
                                    lambda family=family:angular_kernels(fields,frame,family["name"],
                                        family["angular"],family["angular_first"],second=True),
                                    lambda v:partial.__setitem__("working_kernel_arrays",v),
                                    grid=label,family=name,original_radial_ids=owned.tolist(),
                                    selected_body_and_suffix_use_one_kernel=True)
                                virtual=trace.run("new_shared_virtual_position_J_inputs",
                                    lambda:virtual_selected_jets(kernels,ri,ti,metric,second=True),
                                    lambda v:partial.__setitem__("working_virtual_position_J",v),
                                    grid=label,family=name)
                            data=dict(small);data.update({"jac_"+jet:value for jet,value in virtual.items()})
                            U,T=small["Xs"],small["T"]
                            de=2*np.einsum("ic,icn->in",U,virtual["Xs"])
                            df=np.einsum("ic,icn->in",T,virtual["Xs"])+np.einsum("ic,icn->in",U,virtual["T"])
                            raw=_curvature_differentials(data,model.metric["a"][global_ri],cv)
                            raw["metric0"]=spectral_parameter_rows(e,f,de,df,np.zeros(count,dtype=int),model.epsilon)
                            raw["metric1"]=spectral_parameter_rows(e,f,de,df,np.ones(count,dtype=int),model.epsilon)
                            physical={}
                            if len(physical_positions):
                                original_body_slots=layout["pool_body_slots"][body_rows[physical_mask]]
                                physical={"X":grid["body_X"][original_body_slots],
                                    "Xs":small["Xs"][physical_at],"T":small["T"][physical_at]}
                                physical.update({"jac_"+jet:virtual[jet][physical_at] for jet in ("X","Xs","T")})
                                other=trace.run("new_original_selected_shape_mirror_J_contractions",
                                    lambda:selected_physical_derivatives(physical,body_groups[physical_mask],model.side,model.cfg),
                                    lambda v:partial.__setitem__("working_body_physical_J",v),
                                    grid=label,family=name,row_count=len(physical_positions))
                                other=_expand_family(other,family,global_ri[physical_at])
                            else:
                                other=np.zeros((0,len(columns)),dtype=float)
                            differentials={quantity:_expand_family(value,family,global_ri)
                                for quantity,value in raw.items()}
                            _require(all(value.shape==(count,len(columns)) and np.all(np.isfinite(value))
                                for value in differentials.values()),"complete finite shared physical curvature/metric differential block")
                            _require(other.shape==(len(physical_positions),len(columns))
                                and np.all(np.isfinite(other)),"complete original selected shape/mirror differential block")
                            bundle={"differentials":differentials,"body_physical_values":other}
                            partial["working_contracted_physical_differentials"]=bundle
                            model.derivative_input_cache[derivative_key]=bundle
                            model.derivative_input_counts["completed"]+=1
                            partial["working_kernel_arrays"]=None
                            partial.pop("working_virtual_position_J",None);partial.pop("working_body_physical_J",None)
                            del kernels,virtual,data,de,df,raw,physical,other
                        except Exception:
                            model.derivative_input_counts["failed"]+=1;raise
                    d=bundle["differentials"]
                    body_block=np.empty((len(body_rows),len(columns)),dtype=float)
                    for group in (0,1):
                        mask=body_groups==group
                        body_block[mask]=d["metric"+str(group)][body_at[mask]]
                    body_block[physical_mask]=bundle["body_physical_values"]
                    curvature_mask=body_groups>=7
                    if np.any(curvature_mask):
                        hard=trace.run("new_original_hard58_selected_PSD_J_assembly",
                            lambda:_curvature_rows_from_differentials(cv,d,model.cap,model.curvature_scale),
                            lambda v:partial.__setitem__("working_hard58_PSD_J",v),
                            grid=label,family=name,K=model.cap)
                        body_block[curvature_mask]=hard[body_at[curvature_mask],body_groups[curvature_mask]-7]
                    _require(np.all(np.isfinite(body_block)),"all original body pool J entries filled and finite")
                    J[np.ix_(body_output_rows,np.asarray(columns,dtype=int))]=body_block
                    _filled_rows(partial,body_output_rows,ranges,grid=label,family=name,domain="original_body_pool")
                    if len(suffix_positions):
                        current=_take(cK,suffix_positions,ns)
                        ds={quantity:value[suffix_at] for quantity,value in d.items()}
                        cj=trace.run("new_current_K_suffix_PSD_J_assembly",
                            lambda:_curvature_rows_from_differentials(current,ds,K,model.curvature_scale),
                            lambda v:partial.__setitem__("working_K_dependent_PSD_J",v),
                            grid=label,family=name,K=K)
                        six=np.concatenate((ds["metric0"][:,None,:],ds["metric1"][:,None,:],cj),axis=1)
                        suffix_block=six.reshape(len(suffix_output_rows),len(columns))
                        _require(np.all(np.isfinite(suffix_block)),"all original suffix J entries filled and finite")
                        J[np.ix_(suffix_output_rows,np.asarray(columns,dtype=int))]=suffix_block
                        _filled_rows(partial,suffix_output_rows,ranges,grid=label,family=name,domain="complete_suffix")
                        del current,ds,cj,six,suffix_block
                    partial["working_kernel_arrays"]=None
                    for field in ("working_contracted_physical_differentials","working_hard58_PSD_J",
                                  "working_K_dependent_PSD_J"):
                        partial.pop(field,None)
                    del bundle,d,body_block
            offset=end_offset
        J[offset:]=-model.linear_A
        partial["completed_column_blocks"].append({"family":"original_linear_rows",
            "row_start":offset,"row_stop":model.constraint_count,"column_start":0,"column_stop":170})
        _require(offset==model.nonlinear_constraint_count and np.all(np.isfinite(J)),
            "complete finite154847 by170 shared analytic Jacobian required")
        J.setflags(write=False);partial.update(status="complete",matrix_binding=array_binding(J))
        model.jacobian_counts["completed"]+=1
        model.temporary.evict("final_J",int(model.loaded_J is not None))
        model.loaded_J_key,model.loaded_J=key,J
        return J
    except Exception as error:
        partial["error"]=_error(error)
        if partial.get("status")!="complete":
            partial["status"]="raised";model.jacobian_counts["failed"]+=1
        else:
            partial["completed_J_retained_before_cache_or_clock_failure"]=True
        raise
    finally:
        partial["seconds"]=time.monotonic()-tick
        sink["new_J_counts"]=copy.deepcopy(model.jacobian_counts)
        sink["K_independent_derivative_input_counts"]=copy.deepcopy(model.derivative_input_counts)
        sink["shared_component_scientific_counts"]=copy.deepcopy(model.shared_counts)
