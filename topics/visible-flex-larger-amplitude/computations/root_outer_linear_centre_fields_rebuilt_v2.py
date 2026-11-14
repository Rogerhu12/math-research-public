#!/usr/bin/env python3
"""Rebuild the actual two-mode linear centre and its complete nonlinear source.

New recovery version; this is not claimed byte-identical to the unexecuted
local entry lost on 2026-11-12.  C* is reconstructed from its actual positive
moments. Only its m=2,4 functions are replaced by the genuine phi*Qout/S0.
Every mean/inverse term is kept. This stage does not solve the outer PDE.
"""
from __future__ import annotations
import argparse, gzip, json, resource, time
from fractions import Fraction as F
from itertools import zip_longest
from pathlib import Path
from flint import arb, acb, ctx
from closure_split_joint_io_v2 import read, read_field, iter_array, digest
from closure_real_head_source_enclosure import exact_q
from closure_shared_slope_cut_interface import ball, record
from closure_outer_two_cell_adjoint import compact_ball
from closure_outer_whole_field_green_budget import pair
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_candidate_domain import endpoint_candidate, nonnegative_integral
from tail_outer_weighted_compatible import MOMENT_KEYS, make_weighted_candidate
from tail_outer_centered_quartic_fields_v2 import weighted_panel_fields, finite, intersection
from closure_outer_refined_moment_source import EXPECTED, partial_box

MODES = list(range(2,41,2))
SELECTED = (2,4)

def from_pair(x):
    lo,hi = pair(x)
    return exact_q(lo).union(exact_q(hi))

def save(p,data):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(data,ensure_ascii=False,separators=(",",":"))+"\n").encode()
    if len(raw)>1000000:
        raise ValueError("put large primary rows in gzip groups")
    tmp=Path(str(p)+".partial"); tmp.write_bytes(raw); tmp.replace(p)

def positive_upper(x):
    y=finite(x).upper()
    if not y>=0:
        raise ArithmeticError("nonnegative majorant required")
    return y

def cap_original(x,V,weight_lower):
    cap=(V/weight_lower).upper()
    return intersection(finite(x),(-cap).union(cap))

def physical_source(Ps,Ks,r,rx,w,ell,tau):
    """Exact finite quadratic centre and rigorous full analytic remainder."""
    E=1+w*w; z=w*w; ss=rx/r
    weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in MODES}
    lower_weights={m:((1+m)*(exact_q(tau)*m).exp()).lower() for m in MODES}
    Ts={m:m*Ps[m] for m in MODES}
    Us={m:-m*Ks[m]-Ps[m] for m in MODES}
    norms={name:arb(0) for name in ("P","K","T","U","L")}
    for m in MODES:
        for name,value in (("P",Ps[m]),("K",Ks[m]),("T",Ts[m]),
                           ("U",Us[m]),("L",Ks[m]+E*Ts[m])):
            norms[name]+=weights[m]*abs(value).upper()
    norms={k:positive_upper(v) for k,v in norms.items()}
    R=positive_upper(norms["P"]+norms["K"])
    if not R<arb(1)/64:
        raise ArithmeticError("new centre is outside the full R33 mean work domain")
    c=positive_upper(4*R*R)
    lead=positive_upper(c+norms["L"])
    if not lead<1:
        raise ArithmeticError("complete analytic leading inverse not positive")
    Dchange=positive_upper(z.upper()*(2*(norms["K"]+c)+
                 (norms["K"]+c)**2+E.upper()*norms["P"]**2))
    if not Dchange<1:
        raise ArithmeticError("complete metric square-root domain not paid")
    Qnorm=positive_upper(E.upper()*ss.upper()*norms["U"]**2+
        abs(ell).upper()*((norms["K"]+norms["T"])**2+
        z.upper()*(2*norms["K"]*norms["T"]+norms["T"]**2+norms["P"]**2)))
    mean=positive_upper(abs(ell).upper()*(2*c*(norms["K"]+norms["T"])+
                      c*c+2*z.upper()*c*norms["T"]))
    remainder=positive_upper((mean+lead*Qnorm)/(1-lead))
    full=positive_upper((Qnorm+mean)/(1-lead))
    P={}; K={}; T={}; U={}; C={}
    for m in MODES:
        P[m]=acb(0,-Ps[m]/2); K[m]=acb(Ks[m]/2)
        T[m]=acb(Ts[m]/2); U[m]=acb(0,-Us[m]/2)
        C[m]=K[m]+T[m]
        for table in (P,K,T,U,C):
            table[-m]=table[m].conjugate()
    keys=sorted(P)
    def conv(a,b,m):
        return sum((a[j]*b[m-j] for j in keys if m-j in b),acb(0))
    selected=[]
    for m in SELECTED:
        q=E*ss*conv(U,U,m)+ell*(conv(C,C,m)+z*(
            2*conv(K,T,m)+conv(T,T,m)-conv(P,P,m)))
        if not q.imag.contains(0):
            raise ArithmeticError("real-even quadratic source symmetry lost")
        quad=finite(2*q.real)
        error=positive_upper(remainder/lower_weights[m])
        total_cap=positive_upper(full/lower_weights[m])
        enclosed=intersection(quad+(-error).union(error),
                              (-total_cap).union(total_cap))
        selected.append({"mode":m,"quadratic_cosine":compact_ball(quad),
            "complete_source_cosine":compact_ball(enclosed),
            "complete_remainder_coefficient_upper":record(error)})
    return {"selected_cosine_sources":selected,
        "complete_nonlinear_source_W1":record(full),
        "complete_source_minus_quadratic_W1_upper":record(remainder),
        "complete_mean_abs":record(c),"complete_leading_norm":record(lead),
        "complete_D_perturbation_upper":record(Dchange),
        "strong_norms":{k:record(v) for k,v in norms.items()},
        "strong_R":record(R)}

def profile_table(group):
    """Take a proven hull; R84 compact [lower,upper] records use pair()."""
    if digest(group["path"])!=group["sha256"]:
        raise ValueError("R84 whole-field group changed")
    tab={}; count=0
    for row in iter_array(group["path"],"panels"):
        i=row["panel"]; vlo,vhi=pair(row["source_envelope"])
        if vlo!=vhi or vlo<=0:
            raise ValueError("retain the exact original upward dyadic V")
        fields={r["mode"]:[from_pair(x) for x in r["phi_physical_PK"]] for r in row["modes"]}
        if sorted(fields)!=list(SELECTED):
            raise ValueError("both actual homogeneous columns required")
        if i not in tab:
            tab[i]={"V":vlo,"pieces":[],"phi":fields}
        else:
            if tab[i]["V"]!=vlo:
                raise ValueError("V changed inside an original source leaf")
            for m in SELECTED:
                tab[i]["phi"][m]=[x.union(y) for x,y in zip(tab[i]["phi"][m],fields[m])]
        lo,hi=F(row["x_left"]),F(row["x_right"])
        if not lo<hi:
            raise ValueError("profile subpanel must have positive true x width")
        tab[i]["pieces"].append((lo,hi))
        count+=1
    if count!=group["subpanels"] or len(tab)!=group["original_panels"]:
        raise ValueError("incomplete original position/true subpanel coverage")
    for info in tab.values():
        pieces=sorted(info["pieces"])
        if any(pieces[k][1]!=pieces[k+1][0] for k in range(len(pieces)-1)):
            raise ValueError("true profile subpanel cover has a gap or overlap")
        info["left"],info["right"]=pieces[0][0],pieces[-1][1]
        info.pop("pieces")
    return tab,count

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ("profiles","green","linear","material11","material10","source11",
                "source10","moments10","ports","response","ready","out-prefix"):
        ap.add_argument("--"+key,required=True,type=Path)
    ap.add_argument("--rss-kib",type=int,default=98304)
    ap.add_argument("--prepare-only",action="store_true")
    a=ap.parse_args(); ctx.prec,ctx.threads=192,1; start=time.monotonic()
    output=Path(str(a.out_prefix)+"-summary.json")
    if output.exists() or Path(str(a.out_prefix)+"-cell11-segment0-part0.json.gz").exists():
        raise FileExistsError("use a new complete linear-centre run prefix")
    for name,expected in EXPECTED.items():
        if digest(Path(__file__).with_name(name))!=expected:
            raise ValueError("frozen mathematical helper changed: "+name)
    keys=("profiles","green","linear","material11","material10","source11",
          "source10","moments10","ports","response","ready")
    hashes={str(getattr(a,k)):digest(getattr(a,k)) for k in keys}
    profiles,green,linear=[read(getattr(a,k)) for k in ("profiles","green","linear")]
    if not all(x["all_gates"] for x in (profiles,green,linear)):
        raise ValueError("complete original geometry/ordered kernels/linear data required")
    if (profiles["config"]["modes"]!=[2,4] or
        profiles["counts"]["original_material"]!=10793 or
        green["input_hashes"].get(str(a.profiles))!=hashes[str(a.profiles)] or
        green["input_hashes"].get(str(a.linear))!=hashes[str(a.linear)]):
        raise ValueError("the exact R84/R86 two-output outer problem must be retained")
    byprofile={(g["cell"],g["segment"]):g for g in profiles["profile_groups"]}
    if sorted(byprofile)!=[(n,j) for n in (10,11) for j in range(9)]:
        raise ValueError("all18 true profile groups required")
    lrows={r["mode"]:r for r in linear["rows"] if r["endpoint_physical_node"]==10}
    if sorted(lrows)!=list(SELECTED):
        raise ValueError("actual outer endpoint must be physical node10")
    ratios={m:from_pair(lrows[m]["exact_saved_outer_candidate_Q"])/
                 from_pair(lrows[m]["same_true_S0_Q"]) for m in SELECTED}
    ports,ready=read(a.ports),read(a.ready)
    cp=read_field(a.response,"response")["checkpoint"]
    if cp["parameters"]["modes"]!=20 or cp["parameters"]["physicalDepth"]!=12:
        raise ValueError("retain all20 original actual saved modes and depth12")
    head=SourceValues(ready); head.params=ready["rationalDeepModel"]["physicalParameters"]
    prows={r["physical_node"]:r for r in ports["rows"]}
    mats={11:read(a.material11),10:read(a.material10)}
    sources={11:read(a.source11),10:read(a.source10)}
    moments=read(a.moments10)
    if not moments["all_gates"] or moments["entrypoint_sha256"]!=EXPECTED["closure_outer_true_moment_taylor.py"]:
        raise ValueError("cell10 true refined moments required")
    for n in (11,10):
        mat,src=mats[n],sources[n]
        if (mat["cell"]!=n or src["cell"]!=n or not all(mat["checks"].values())
                or not src["all_gates"] or mat["panels"]!=src["panels"]):
            raise ValueError("same complete candidate/material cover required")
        for p in (getattr(a,"material"+str(n)),a.ports,a.response,a.ready):
            if src["input_hashes"].get(str(p))!=hashes[str(p)]:
                raise ValueError("candidate/source identity changed: "+str(p))
        sp=getattr(a,"source"+str(n))
        if profiles["input_hashes"].get(str(sp))!=hashes[str(sp)]:
            raise ValueError("original V envelopes must match this same candidate source")
    if (moments["original_material_manifest"]!=str(a.material10) or
        moments["panels"]!=mats[10]["panels"]):
        raise ValueError("cell10 refined moment identity differs")
    for p in (a.material10,a.ready):
        if moments["input_hashes"].get(str(p))!=hashes[str(p)]:
            raise ValueError("cell10 moments use another actual background")
    plan={"status":"Prepared fresh actual linear-centre source; not yet executed",
          "entrypoint_sha256":digest(__file__),"input_hashes":hashes,
          "source_hashes":EXPECTED,"precision":192,"modes":MODES,
          "selected_outputs":list(SELECTED),"rss_kib":a.rss_kib,
          "old_lost_entry_byte_identity_claimed":False,
          "no_new_ODE_or_source_integral":True}
    save(str(a.out_prefix)+"-plan.json",plan)
    if a.prepare_only:
        print(json.dumps({"prepared":True,"out_prefix":str(a.out_prefix)}),flush=True)
        return
    owned=[]; original_count=0; subcount=0; active=None
    original_mass={m:{"P":arb(0),"K":arb(0)} for m in MODES}
    original_raw_mass={m:{"P":arb(0),"K":arb(0)} for m in MODES}
    mixed_mass={m:{"P":arb(0),"K":arb(0)} for m in SELECTED}
    maxnorm={k:arb(0) for k in ("R","L","mean","full_source","remainder")}
    def guard():
        rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss>a.rss_kib:
            raise MemoryError("observed linear-centre RSS exceeded declared threshold: "+str(rss))
    def recover(error=None):
        save(str(a.out_prefix)+"-recovery.json",{
            "status":"Completed source groups; no unfinished-group or PDE claim",
            "error":error,"completed_groups":owned,"original_panels":original_count,
            "true_subpanels":subcount,"input_hashes":hashes,"source_sha256":digest(__file__),
            "elapsed_seconds":time.monotonic()-start})
    try:
        for n in (11,10):
            mat,src=mats[n],sources[n]; meta=mat["original_metadata"]
            tau=F(src["tau"])
            if tau!=F(1,64):
                raise ValueError("the original R84 analytic strip is fixed")
            cell=OuterCell(head,n)
            left,lr=endpoint_candidate(cell,"inner",n+1,cp["rawStates"][n+1],
                prows[n+1],ball(meta["inner_radius"]),tau,8)
            right,rr=endpoint_candidate(cell,"outer",n,cp["rawStates"][n],
                prows[n],ball(meta["outer_radius"]),tau,8)
            oldtotal={k:nonnegative_integral(v,strict=True)
                      for k,v in meta["total_positive_moments"].items()}
            totals=oldtotal if n==11 else {
                k:nonnegative_integral(v,strict=True)
                for k,v in moments["total_positive_moments"].items()}
            candidate=make_weighted_candidate(left,right,totals)
            oldcandidate=make_weighted_candidate(left,right,oldtotal)
            if sorted(left["H"])!=MODES:
                raise ValueError("all20 original endpoint modes are required")
            for m in MODES:
                candidate["bubble_coefficient"][m]=intersection(
                    candidate["bubble_coefficient"][m],oldcandidate["bubble_coefficient"][m])
            weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in MODES}
            wlower={m:((1+m)*(exact_q(tau)*m).exp()).lower() for m in MODES}
            material_groups={g["source_segment"]:g for g in mat["groups"]}
            source_groups={g["segment"]:g for g in src["groups"]}
            if any(sorted(x)!=list(range(9)) for x in (material_groups,source_groups)):
                raise ValueError("all nine original segments are required")
            if n==10:
                moment_groups={g["source_segment"]:g for g in moments["groups"]}
                if sorted(moment_groups)!=list(range(9)):
                    raise ValueError("all refined positive-moment groups required")
                gs=[tuple(ball(moment_groups[j]["summed_moments"][k])
                          for k in MOMENT_KEYS) for j in range(9)]
                for z,k in enumerate(MOMENT_KEYS):
                    intersection(sum((v[z] for v in gs),arb(0)),totals[k])
            for j in range(9):
                og,sg,pg=material_groups[j],source_groups[j],byprofile[n,j]
                for group in (og,sg,pg):
                    if digest(group["path"])!=group["sha256"]:
                        raise ValueError("frozen source/material/profile group changed")
                    hashes[group["path"]]=group["sha256"]
                if og["panels"]!=sg["panels"] or og["panels"]!=pg["original_panels"]:
                    raise ValueError("material and source covers disagree")
                tab,ng=profile_table(pg)
                if n==10:
                    mg=moment_groups[j]
                    if (digest(mg["path"])!=mg["sha256"] or
                        mg["original_group_sha256"]!=og["sha256"] or
                        mg["panels"]!=og["panels"]):
                        raise ValueError("refined moment group is another candidate partition")
                    hashes[mg["path"]]=mg["sha256"]
                    imrows=[]
                    for im in iter_array(mg["path"],"panels"):
                        imrows.append((im["panel"],im["x_left"],im["x_right"],
                            im["original_parent"],tuple(ball(im["moments"][k]) for k in MOMENT_KEYS)))
                    if len(imrows)!=og["panels"]:
                        raise ValueError("incomplete refined positive moments")
                    integrals=[r[4] for r in imrows]
                    suffix=[None]*(len(integrals)+1)
                    suffix[-1]=tuple(arb(0) for k in MOMENT_KEYS)
                    for i in range(len(integrals)-1,-1,-1):
                        suffix[i]=tuple(integrals[i][z]+suffix[i+1][z] for z in range(5))
                    for z in range(5):
                        intersection(suffix[0][z],gs[j][z])
                    earlier=tuple(sum((gs[k][z] for k in range(j)),arb(0)) for z in range(5))
                    later=tuple(sum((gs[k][z] for k in range(j+1,9)),arb(0)) for z in range(5))
                    running=tuple(arb(0) for k in MOMENT_KEYS)
                chunks=[]; chunk_rows=0; chunk_number=0; seen=0; target=None
                def finish_chunk():
                    nonlocal active,chunk_rows,target
                    if active is None:
                        return
                    active.write("\n]}\n"); active.close(); active=None
                    if target.stat().st_size>=5000000:
                        raise ValueError("a primary source chunk exceeds5MB")
                    chunks.append({"path":str(target),"sha256":digest(target),
                                   "bytes":target.stat().st_size,"panels":chunk_rows})
                    chunk_rows=0
                for i,pack in enumerate(zip_longest(iter_array(og["path"],"panels"),
                                                   iter_array(sg["path"],"panels"))):
                    if any(x is None for x in pack):
                        raise ValueError("source/material stream ended early")
                    g,old=pack; info=tab[i]
                    if (old["panel"]!=i or g["segment"]!=j or
                        (g["x_left"],g["x_right"])!=(old["x_left"],old["x_right"]) or
                        (F(g["x_left"]),F(g["x_right"]))!=(info["left"],info["right"])):
                        raise ValueError("retain every exact original source position")
                    Vq=info["V"]; V=exact_q(Vq)
                    if Vq*Vq<pair(old["complete_mean_abs"])[1]/4:
                        raise ArithmeticError("saved dyadic V does not cover its own original mean certificate")
                    if n==11:
                        prefix={k:nonnegative_integral(v) for k,v in g["prefix_moments"].items()}
                        after={k:nonnegative_integral(v) for k,v in g["suffix_moments"].items()}
                    else:
                        im=imrows[i]
                        if im[:4]!=(i,g["x_left"],g["x_right"],g["original_parent"]):
                            raise ValueError("refined moment position changed")
                        prefix={}; after={}
                        for z,k in enumerate(MOMENT_KEYS):
                            prefix[k]=partial_box(earlier[z]+running[z],integrals[i][z],g["prefix_moments"][k])
                            after[k]=partial_box(later[z]+suffix[i+1][z],integrals[i][z],g["suffix_moments"][k])
                            prefix[k]=nonnegative_integral(record(intersection(prefix[k],totals[k]-after[k])))
                            after[k]=nonnegative_integral(record(intersection(after[k],totals[k]-prefix[k])))
                    H,K,Kx=weighted_panel_fields(candidate,u=ball(g["u"]),u_x=ball(g["u_x"]),
                                                prefix_moments=prefix,suffix_moments=after)
                    r,w,rx,ell=[ball(g[k]) for k in ("radius","w","radius_x","log_w_x")]
                    if not r>0 or not w>0 or not rx>0 or not w<=arb(1)/2:
                        raise ArithmeticError("actual background positivity lost")
                    origP={}; origK={}
                    for m in MODES:
                        if not H[m].imag.contains(0) or not K[m].imag.contains(0):
                            raise ArithmeticError("original real-even centre symmetry lost")
                        origP[m]=cap_original(-2*m*H[m].real/(r*w),V,wlower[m])
                        origK[m]=cap_original(2*K[m].real,V,wlower[m])
                        for name,v in (("P",origP[m]),("K",origK[m])):
                            raw=positive_upper(abs(v).upper()/V)
                            original_raw_mass[m][name]=max(original_raw_mass[m][name],raw)
                            # Original certified pointwise total norm <= V.
                            strong=min(arb(1),positive_upper(weights[m]*raw))
                            original_mass[m][name]=max(original_mass[m][name],strong)
                    mixedP=dict(origP); mixedK=dict(origK)
                    for m in SELECTED:
                        mixedP[m]=finite(info["phi"][m][0]*ratios[m])
                        mixedK[m]=finite(info["phi"][m][1]*ratios[m])
                        for name,v in (("P",mixedP[m]),("K",mixedK[m])):
                            mass=positive_upper(weights[m]*abs(v).upper()/V)
                            mixed_mass[m][name]=max(mixed_mass[m][name],mass)
                    nonlinear=physical_source(mixedP,mixedK,r,rx,w,ell,tau)
                    for name,key in (("R","strong_R"),("L","complete_leading_norm"),
                            ("mean","complete_mean_abs"),("full_source","complete_nonlinear_source_W1"),
                            ("remainder","complete_source_minus_quadratic_W1_upper")):
                        maxnorm[name]=max(maxnorm[name],ball(nonlinear[key]).upper())
                    row={"cell":n,"segment":j,"panel":i,"x_left":g["x_left"],
                         "x_right":g["x_right"],"source_envelope":record(V),
                         "radius":g["radius"],"radius_x":g["radius_x"],"w":g["w"],
                         "log_w_x":g["log_w_x"],
                         "original_candidate_PK":[{"mode":m,"P":compact_ball(origP[m]),
                             "K":compact_ball(origK[m])} for m in MODES],
                         "true_linear_selected_PK":[{"mode":m,"P":compact_ball(mixedP[m]),
                             "K":compact_ball(mixedK[m])} for m in SELECTED],
                         **nonlinear}
                    if active is None:
                        target=Path(str(a.out_prefix)+f"-cell{n}-segment{j}-part{chunk_number}.json.gz")
                        if target.exists():
                            raise FileExistsError("fresh source chunk would overwrite existing data")
                        active=gzip.open(target,"wt",compresslevel=6)
                        active.write('{"cell":'+str(n)+',"segment":'+str(j)+',"panels":[\n')
                        chunk_number+=1
                    if chunk_rows:
                        active.write(",\n")
                    active.write(json.dumps(row,separators=(",",":")))
                    chunk_rows+=1; seen+=1; original_count+=1
                    if n==10:
                        running=tuple(running[z]+integrals[i][z] for z in range(5))
                    if chunk_rows==128:
                        finish_chunk(); guard()
                finish_chunk()
                if seen!=og["panels"]:
                    raise ValueError("incomplete original source group")
                subcount+=ng
                owned.append({"cell":n,"segment":j,"panels":seen,"subpanels":ng,
                    "chunks":chunks,"original_material_sha256":og["sha256"],
                    "original_source_sha256":sg["sha256"],"profile_sha256":pg["sha256"]})
                recover(); guard()
                print(json.dumps({"event":"complete_linear_centre_source_group","cell":n,
                    "segment":j,"panels":seen,"subpanels":ng,
                    "seconds":time.monotonic()-start,
                    "maxrss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
                del tab
        if original_count!=10793 or subcount!=profiles["counts"]["taylor"]+profiles["counts"]["root_brackets"]:
            raise ValueError("full two-cell source/profile coverage missing")
        allmass=sum((v for row in original_mass.values() for v in row.values()),arb(0)).upper()
        restmass=sum((v for m,row in original_mass.items() if m not in SELECTED
                      for v in row.values()),arb(0)).upper()
        result={"status":"Actual complete source at true linear selected centre and original remaining modes",
            "all_gates":True,"gates":{
                "all10793_original_leaves_and10933_actual_profile_subpanels":True,
                "same_g_mu_cut_and_true_outer_boundary":True,
                "all20_original_candidate_modes_reconstructed":True,
                "only_selected2and4_replaced_by_actual_homogeneous_phi":True,
                "cell10_refined_true_moments_keep_exact_candidate":True,
                "complete_mean_root_and_all_inverse_generated_modes_retained":True,
                "signed_real_quadratic_and_complete_remainder":True,
                "not_intersected_with_R79_different_centre_source":True},
            "tau":"1/64","groups":owned,"original_panels":original_count,
            "actual_subpanels":subcount,"original_mode_component_mass":{
                str(m):{c:record(v) for c,v in row.items()} for m,row in original_mass.items()},
            "original_unweighted_component_mass":{
                str(m):{c:record(v) for c,v in row.items()} for m,row in original_raw_mass.items()},
            "original_all_mode_strong_mass_upper":record(allmass),
            "original_rest_excluding2and4_strong_mass_upper":record(restmass),
            "true_linear_selected_component_mass":{
                str(m):{c:record(v) for c,v in row.items()} for m,row in mixed_mass.items()},
            "maximum_complete_source_domain":{k:record(v) for k,v in maxnorm.items()},
            "linear_factors_Qout_over_S0":{str(m):record(v) for m,v in ratios.items()},
            "input_hashes":hashes,"source_hashes":EXPECTED,"source_sha256":digest(__file__),
            "no_new_ODE_or_source_integral":True,
            "ordered_source_integral_or_cut_selfmap_paid":False,
            "full_outer_or_closed_surface_claimed":False,
            "elapsed_seconds":time.monotonic()-start,
            "peak_RSS_KiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
        save(output,result)
        print(json.dumps({"summary":str(output),"all_gates":True,"panels":original_count,
            "rest_strong_mass":str(restmass),"seconds":time.monotonic()-start}),flush=True)
    except BaseException as e:
        if active is not None:
            active.close()
        recover(type(e).__name__+": "+str(e))
        raise
if __name__=="__main__":
    main()
