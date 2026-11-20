#!/usr/bin/env python3
"""Combine executed M24 bridge component bounds without rerunning integrals.

The explicit new bridge has shared-Hermite Y/e, an analytically extended phase,
a true radius primitive, and the original fixed 1168-node mean primitive.
The metric transfer concerns the source's mathematical hand-jet oracle; it
does NOT concern actual derivatives of its terminal clipped radius function.
"""
import argparse,bisect,hashlib,importlib.util,json,math,sys
from fractions import Fraction as Q
from pathlib import Path

HERE=Path(__file__).resolve().parent
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod)
    return mod
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))
def pack(x):return {"exact":str(x),"display":float(x)}
def usqrt(x):
    scale=10**18;t=math.isqrt(x.numerator*scale*scale//x.denominator)
    if t*t*x.denominator<x.numerator*scale*scale:t+=1
    return Q(t,scale)
def norm(*xs):return usqrt(sum(x*x for x in xs))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("source-run","physical","shared","nonmean","mean","background","out"):
        p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--support-dir",type=Path,default=HERE)
    a=p.parse_args()
    shared,nonmean,mean,bg=[json.loads(x.read_text()) for x in
                            (a.shared,a.nonmean,a.mean,a.background)]
    rsha,psha=sha(a.source_run),sha(a.physical)
    for obj in (shared,nonmean,mean):
        assert obj.get("run_sha256",obj.get("input_run_sha256"))==rsha
        assert obj["physical_sha256"]==psha
    assert bg["run_sha256"]==rsha
    for obj,name in [(shared,"certify_r59_shared_jet_transfer.py"),
                     (nonmean,"certify_r59_c2_nonmean_ranges.py"),
                     (mean,"certify_r59_shared_fixed_mean_ranges.py")]:
        assert obj["source_sha256"]==sha(HERE/name)
    assert mean["complete"] and mean["explicit_shared_C2_interval_family"]
    assert mean["mean_nodes"]==1168
    assert nonmean["explicit_new_shared_C2_object"]
    assert shared["new_C2_interpretation_explicit"]
    assert bg["status"]=="exact_moment_and_true_parameter_bounds_passed"
    assert bg["normalized_analytic_domain_upper_exact"]=="1000000000001/1000000000000"
    nm=lambda k:Q(nonmean["maxima"][k]["exact"])
    se=lambda k:Q(shared["all_angle_computational_field_error"][k]["exact"])
    be=lambda k:Q(bg[k]["upper_exact"])
    ce=max(abs(Q(bg["endpoint_pullback_scale_minus_one"][k]))
           for k in ("lower_exact","upper_exact"))
    assert ce<Q(1,10**12)
    # True source primitive -> exact endpoint-pulled R59 reference. Each
    # triangle includes the source GL->true difference; no identification is made.
    br=[]
    for j in range(3):
        x=Q(bg["endpoint_pulled_primitive_vs_R59_piecewise_jet_bounds"]["sin"][j]["upper_exact"])
        y=Q(bg["same_literal_parameters_primitive_physical_jet_bounds"]["sin"][j]["upper_exact"])
        br.append(x+(1+ce)**j*y)
    assert max(br)<Q(1,10**8)
    aerr=Q(1,10**8);amin=Q(299,1000)
    m0=fq(mean["mean_difference_upper"]);m1=fq(mean["mean_derivative_difference_upper"])
    phase,phase1=be("phase_gap"),be("phase_derivative_gap")
    assert m0<Q(1,100) and m1<Q(284,1000)
    hp_raw=(1+ce)*m0+ce+phase
    hpp_raw=(1+ce)**2*m1+(1+ce)*phase1+4*(ce+(1+ce)*phase)
    hp,hpp=Q(101,10000),Q(285,1000)
    assert hp_raw<hp and hpp_raw<hpp
    h=Q(932,1000)*hp
    assert nm("G0")<Q(25,1000) and nm("G1")<Q(168,1000) and nm("G2")<Q(1351,1000)
    V0=nm("G0")+norm(aerr,h)
    V1=nm("G1")+norm(aerr,hp,aerr/amin)
    V2=nm("G2")+norm(aerr,hpp,
        usqrt(Q(2))*(aerr+aerr/amin)/amin,
        aerr/amin**2+aerr/amin,hp/amin)
    v0,v1,v2=Q(35,1000),Q(179,1000),Q(1639,1000)
    assert V0<v0 and V1<v1 and V2<v2
    radius=Q(121,100)+v0
    support=Q(74,100)-Q(121,100)*Q(99,70)*v1-v0
    curvature=(Q(4001,1000)+v2)/(1-v1)**2
    assert radius==Q(249,200) and support>Q(398,1000) and curvature<Q(837,100)

    # Recompute only the small angular-spline polynomial bound, not any
    # background integral or continuous mean/nonmean grid.
    sh=module("_r59_combiner_shared",HERE/"certify_r59_shared_jet_transfer.py")
    ad=module("_r59_combiner_model",a.support_dir/"actual_m3_metric_model.py")
    ld=module("_r59_combiner_field",a.support_dir/"audit_full_relative_metric.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=ld.load_physical(a.physical)
    o.initial(z.p);f=o.flow(z.p[0]);end,entry=fq(f.end),fq(f.prefix_end)
    knots=[fq(x)*end for x in f.spline.x];cut=Q(3,4)*end
    grid=sorted(set([entry,end]+[x for x in knots if entry<x<end]+
                    ([cut] if entry<cut<end else [])))
    epmax=Q(0)
    for left,right in zip(grid[:-1],grid[1:]):
        mid=(left+right)/2;i=min(len(knots)-2,bisect.bisect_right(knots,mid)-1)
        pp=[fq(f.spline.c[3-j,i])/end**j for j in range(4)]
        hh=knots[i+1]-knots[i]
        if i+1<len(knots)-1:
            target=[fq(f.spline.c[3,i+1]),fq(f.spline.c[2,i+1])/end,
                    2*fq(f.spline.c[1,i+1])/end**2]
        else:target=[sh.value(sh.derivative(pp,j),hh) for j in range(3)]
        corr,_=sh.right_correction(pp,hh,target)
        pol=[(pp[j] if j<len(pp) else Q(0))+corr[j] for j in range(6)]
        if mid>cut:
            u=[(knots[i]-cut)/(end/4),4/end];chi=[Q(1)]+[Q(0)]*5
            for factor,degree in [(-10,3),(15,4),(-6,5)]:
                for j,x in enumerate(sh.power(u,degree)):chi[j]+=factor*x
            pol=sh.mul(pol,chi)
        pol=[fq(f.warp_e)*x for x in pol]
        epmax=max(epmax,sh.abrange(sh.derivative(pol),knots[i],left,right))
    assert epmax<Q(3)

    # All these are budgets between the mathematical hand-jet oracle and
    # the explicitly defined new C2 bridge, at the same computational psi.
    ea,eap=Q(1,10**12),Q(1,10**12)
    egp,egpp,ee,eep=Q(1,10**17),Q(1,10**17),Q(1,10**17),Q(1,10**15)
    assert be("clipped_source_radius_vs_true_primitive_gap")<ea
    assert Q(bg["clipped_source_hand_geo_jet_vs_analytic_phase_gaps"][0]["upper_exact"])<eap
    assert se("G_psi")<egp and se("G_psipsi")<egpp and se("G_s_comp")<Q(1,10**16)
    assert Q(shared["angular_chart_e_error"][0]["exact"])<ee
    assert Q(shared["angular_chart_e_error"][1]["exact"])<eep
    u,v=Q(11,100),Q(54,100);arho,rho=Q(298,1000),Q(85,100)
    # A first-exit bootstrap below verifies the all-angle U/V bounds on the
    # whole interpolation, starting from the certified canonical field.
    assert Q(nonmean["chart_rho_lower"]["exact"])-ee>rho
    assert 3*(1-Q(nonmean["chart_rho_lower"]["exact"])+ee)<Q(1,2)
    assert Q(bg["true_primitive_radius_lower"]["lower_exact"])-ea>arho
    assert fq(mean["frenet_root_lower"])>Q(39,1000)**2
    assert epmax+eep<3
    assert Q(1001,1000)*Q(115,100)*u<Q(13,100)
    assert nm("G_s")+Q(1,10**12)<Q(132,1000)
    assert max(map(abs,map(fq,mean["mean_value_range"])))<Q(101,100)
    beta=Q(39,1000);apbound=Q(101,100)
    c0=1-u-v-u*v;kmin=c0/(1+u)**3;nmin=c0/(1+u)
    assert c0>0 and u*Q(1,2)/rho**2<v
    du=egp/(arho*rho)+u*(ea/arho+ee/rho+ee/3)
    dv=egpp/(arho*rho**2)+egp*Q(1,2)/(arho*rho**3)+v*(ea/arho+3*ee/rho+ee/3)+3*u*ee/rho**2
    assert nm("U_error")/(1-aerr/amin)+du<u
    assert nm("V_error")/(1-aerr/amin)+dv<v
    dt=du/(1-u)
    dn=(dv+2*(1+v)*dt)/nmin
    dk=((1+v)*du+(1+u)*dv)/(1-u)**3+3*(1+u)*(1+v)*du/(1-u)**4
    dalpha=eap/kmin+apbound*dk/kmin**2
    vchart=Q(3)/(3*rho)
    dvchart=eep/(3*rho)+Q(3)*ee/(3*rho**2)
    conv=dvchart*Q(13,100)+vchart*egp
    assert conv<Q(1,10**12)
    dm=(1+1/beta)*dalpha+2*dn+dt+conv
    assert dm<Q(5,10**9)
    dgs=Q(1,10**16)+conv+Q(132,1000)*ee/3
    dfs=eap+apbound*ee/3+dgs+dm
    # U was compared in the rotating theta frame; add the full frame rotation
    # if comparing actual Cartesian vectors at the same computational psi.
    dfth=du+(1+u)*ee/3
    assert dfs<Q(6,10**9) and dfth<Q(1,10**12)
    frame_diff=norm(dfs,dfth)
    assert frame_diff<Q(7,10**9)
    # A Frobenius upper bound also bounds the source frame operator norm.
    frame_bound=norm(Q(101,100)*Q(99,70)+Q(132,1000),1+u)
    assert frame_bound<2
    gram=2*frame_bound*frame_diff+frame_diff**2
    assert gram<Q(3,10**8)
    result={
        "status":"exact_component_combination_passed",
        "new_C2_bridge_explicit":True,"original_physical_modified":False,
        "run_sha256":rsha,"physical_sha256":psha,"source_sha256":sha(__file__),
        "input_certificate_sha256":{k:sha(getattr(a,k)) for k in ("shared","nonmean","mean","background")},
        "mean_nodes":1168,"original_GL6_height_rule_replaced_by_true_mean_primitive":True,
        "background_reference_jet_triangle":[pack(x) for x in br],
        "mean_reference_first_second":[pack(hp_raw),pack(hpp_raw)],
        "conditional_R59_bounds":{"V0":pack(V0),"V1":pack(V1),"V2":pack(V2),
            "radius":pack(radius),"support_lower":pack(support),"curvature_upper":pack(curvature),
            "condition":"Absolute new bridge entry height z0 in [7/20,51/100]"},
        "chart_e_prime_upper":pack(epmax),
        "source_math_oracle_to_new_C2_transfer":{
            "U":pack(du),"V":pack(dv),"T":pack(dt),"N":pack(dn),
            "kappa_times_a":pack(dk),"alpha":pack(dalpha),"mean_speed":pack(dm),
            "first_column":pack(dfs),"second_column":pack(dfth),
            "relative_frame_difference":pack(frame_diff),"source_frame_bound":pack(frame_bound),
            "relative_Gram_difference":pack(gram),"advertised_Gram_allowance":pack(Q(3,10**8)),
            "radius_only_target_g_transfer":pack(be("radius_only_relative_metric_transfer_bound"))},
        "not_certified":["Derivatives of the original literal upper-clipped radius function",
            "Continuous original or new bridge metric error from finite sampled values",
            "Original GL6 height quadrature versus the new true mean primitive",
            "Absolute bridge-entry height, prefix/tail C2 seam, or the complete closed surface",
            "An unchanged frozen metric or blanket machine/libm evaluation roundoff"]}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":result["status"],"conditional_geometry":
        {k:float(x) for k,x in (("V0",V0),("V1",V1),("V2",V2),("radius",radius),("support",support),("curvature",curvature))},
        "mean_transfer":float(dm),"relative_Gram_transfer":float(gram),"chart_e_prime":float(epmax)}))
if __name__=="__main__":main()
