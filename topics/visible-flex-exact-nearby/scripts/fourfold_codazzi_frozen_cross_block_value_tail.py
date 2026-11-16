# WPTV/VR new finite cross-block bounds only; never imports an old producer.
from fractions import Fraction
from bisect import bisect_right
from math import isqrt
import hashlib, json, re

def exact(q):
    q=Fraction(q)
    return arb(q.numerator)/arb(q.denominator)

def upper(x):
    require(x.is_finite() and x.lower()>=0,"nonnegative finite bound")
    return x.upper()

def mag(x):
    require(x.is_finite(),"finite signed coefficient")
    return abs(x).upper()

def saved(record):
    if isinstance(record,dict): record=record["ball"]
    return upper(arb(record))

def whole(record):
    return arb(record["ball"] if isinstance(record,dict) else record)

def interval(lo,hi):
    require(lo<=hi,"ordered exact interval")
    return exact((lo+hi)/2)+exact((hi-lo)/2)*arb(0,1)

def signed_display_centre(record):
    # A reference only. Never claims this centre is the metric's value at r.
    text=record["ball"] if isinstance(record,dict) else record
    if text.startswith("["):
        text=text[1:].split(" +/- ",1)[0]
    require(re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?",text)
            is not None,"original finite display centre")
    return Fraction(text)

def poly_zero(m):
    return {j:arb(0) for j in range(-m,m+1)}

def poly_add(a,b):
    keys=set(a)|set(b)
    return {j:a.get(j,arb(0))+b.get(j,arb(0)) for j in keys}

def poly_scale(a,c):
    return {j:c*v for j,v in a.items()}

def poly_difference(a,b):
    return {j:a.get(j,arb(0))-b.get(j,arb(0)) for j in set(a)|set(b)}

def convolution(a,b):
    out=poly_zero(max(map(abs,a))+max(map(abs,b)))
    for j,av in a.items():
        for k,bv in b.items():
            out[j+k]+=av*bv
    return out

def polynomial_A0(a):
    # Only a new reference or an actual signed difference uses this function.
    return upper(sum((mag(x) for x in a.values()),arb(0)))

def fields(cubic,repair,piece,left,right,intrinsic,reference=False):
    values=cubic.polynomial_values(piece,left,right,exact,interval)
    alpha=Fraction("6890507429876859/9007199254740992")
    physical=[exact(alpha)*v for v in values]
    if not reference:
        for j in range(65):
            physical[j]+=interval(-repair[j],repair[j])
    cr=whole(intrinsic["Cref"])
    require(cr.upper()<0,"same signed intrinsic Cref")
    physical[32]+=1/cr
    ui=poly_zero(32); vr=poly_zero(32)
    vr[0]=physical[32]
    for j in range(1,33):
        ui[j]=-physical[j-1]/2; ui[-j]=physical[j-1]/2
        vr[j]=vr[-j]=physical[32+j]/2
    return ui,vr

def coefficients(ui,vr,beta,K):
    # ui is the real coefficient of i in the Laurent series of real odd u.
    u2=poly_scale(convolution(ui,ui),-1)
    v2=convolution(vr,vr)
    uv=convolution(ui,vr)
    S=poly_add(u2,poly_scale(v2,K))
    la=poly_scale(poly_add(poly_scale(u2,3),poly_scale(v2,K)),-beta)
    le=poly_scale(poly_add(u2,poly_scale(v2,3*K)),-beta)
    la[0]-=beta; le[0]+=beta
    ell=poly_scale(uv,-2*beta)
    drift={j:(beta*S[j]/(4*j) if j else arb(0)) for j in S}
    ap=[{j:beta*(-4*j)*ui[j] for j in ui},
        {j:beta*(4*j)*vr[j] for j in vr}]
    bp=[ui,poly_scale(vr,K)]
    # ap[0] real even; ap[1] imaginary odd; bp[0] imaginary odd, bp[1] real even.
    return {"d":drift,"la":la,"le":le,"ell":ell,"Kell":poly_scale(ell,K),
            "a":ap,"b":bp}

def scales(q,direction):
    return ([arb(1),arb(1)],[arb(1),1/q]) if direction=="HL" else (
           [arb(1),q],[arb(1),arb(1)])

def cross_pairs(degree,direction):
    # Normalized real basis: sqrt(2) sin(4j phi), sqrt(2) cos(4j phi), and mean 1.
    # Both nonmean sqrt(2) factors cancel; the unit phases are diag(-i,1).
    # Centre/reference have degree <=64, so j+k>degree kills the opposite sign.
    # Their complete mean input and modes 1..32 have no output >=97.
    # The full degree96 delta part is never restricted by this centre identity.
    for shift in range(1,degree+1):
        for low in range(97-shift,97):
            high=low+shift
            yield (high,low,shift) if direction=="HL" else (low,high,-shift)

def cross_local_norm(c,q,direction,output_derivative=False,input_H1=False):
    out_scale,in_scale=scales(q,direction)
    rows={}; cols={}
    for j,k,p in cross_pairs(64,direction):
        values=((c["la"][p]-4*k*c["d"][p],-c["Kell"][p]),
                (c["ell"][p],c["le"][p]-4*k*c["d"][p]))
        w=(4*j if output_derivative else 1)*(4*k+1 if input_H1 else 1)
        for a in range(2):
            for b in range(2):
                value=mag(values[a][b])*out_scale[a]*in_scale[b]*w
                rows[(a,j)]=rows.get((a,j),arb(0))+value
                cols[(b,k)]=cols.get((b,k),arb(0))+value
    rr=max((upper(v) for v in rows.values()),default=arb(0))
    cc=max((upper(v) for v in cols.values()),default=arb(0))
    return upper((rr*cc).sqrt())

def cross_multiplier(a,direction,input_primitive=False,output_primitive=False,
                     output_derivative=False,input_H1=False):
    rows={};cols={}
    for j,k,p in cross_pairs(32,direction):
        value=mag(a[p])
        if input_primitive: value/=4*k
        if output_primitive: value/=4*j
        if output_derivative: value*=4*j
        if input_H1: value*=4*k+1
        rows[j]=rows.get(j,arb(0))+value
        cols[k]=cols.get(k,arb(0))+value
    return upper((max((upper(v) for v in rows.values()),default=arb(0))*
                  max((upper(v) for v in cols.values()),default=arb(0))).sqrt())

def primitive_cross(a,b,A,B,q,direction,output_derivative=False,input_H1=False):
    # Exact split of the intermediate Q97 + P97. Every original mean is retained.
    # This helper is only for two degree32 factors, not an arbitrary high input.
    # First right-limit the WHOLE LH product to modes 97..160 by its band64.
    # Its first term reads <=128. Only after that identity may 4j+1<=641 be used.
    # Output S and input S^-1 are included componentwise by scales().
    out_scale,in_scale=scales(q,direction)
    if direction=="HL":
        require(not input_H1,"unrequested HL input weight")
        ca=[cross_multiplier(v,"HL",input_primitive=True,
                            output_derivative=output_derivative) for v in a]
        cb=[cross_multiplier(v,"HL") for v in b]
        factor=arb(640 if output_derivative else 1)/388
        fees=[[ca[i]*B[j]+factor*A[i]*cb[j] for j in range(2)] for i in range(2)]
    else:
        require(not output_derivative,"unrequested LH output weight")
        cb=[cross_multiplier(v,"LH",output_primitive=True,input_H1=input_H1) for v in b]
        ca=[cross_multiplier(v,"LH",input_primitive=True) for v in a]
        factor=arb(641 if input_H1 else 1)
        fees=[[A[i]*cb[j]+factor*ca[i]*B[j] for j in range(2)] for i in range(2)]
    square=arb(0)
    for i in range(2):
        for j in range(2):
            term=2*out_scale[i]*in_scale[j]*fees[i][j]
            square+=term*term
    return upper(square.sqrt())

def exact_reference(cubic,rows,midpoint):
    row_index=next(i for i,row in enumerate(rows)
                   if Fraction(row["interval"][0])<=midpoint<Fraction(row["interval"][1]))
    intrinsic=rows[row_index]["original_intrinsic_enclosure"]
    ref={name:signed_display_centre(intrinsic[name]) for name in ("beta","K","gamma","Cref")}
    require(ref["K"]>0 and ref["Cref"]<0 and ref["gamma"]>0,"positive reference selection")
    scale=1<<20
    q=Fraction(max(scale//8,isqrt((ref["K"].numerator*scale*scale)//ref["K"].denominator)),scale)
    piece=bisect_right(cubic.nodes,midpoint)-1
    require(0<=piece<6144,"reference belongs to original cubic")
    raw=cubic.exact_values(piece,midpoint)
    alpha=Fraction("6890507429876859/9007199254740992")
    physical=[alpha*x for x in raw]
    physical[32]+=1/ref["Cref"]
    eta=-ref["gamma"]*physical[32]
    ui={j:Fraction(0) for j in range(-32,33)}
    vr=dict(ui);vr[0]=physical[32]
    for j in range(1,33):
        ui[j]=-physical[j-1]/2;ui[-j]=physical[j-1]/2
        vr[j]=vr[-j]=physical[32+j]/2
    definition={"midpoint":str(midpoint),"original_row":row_index,"original_piece":piece,
                "intrinsic_centres":{k:str(v) for k,v in ref.items()},"q":str(q),"eta":str(eta),
                "u_imag_laurent":[str(ui[j]) for j in range(-32,33)],
                "v_real_laurent":[str(vr[j]) for j in range(-32,33)],
                "repair_reference_is_zero":True,"actual_repair_enclosure_retained":True}
    rawdef=json.dumps(definition,sort_keys=True,separators=(",",":")).encode()
    reference_identity={k:v for k,v in definition.items()
        if k not in ("u_imag_laurent","v_real_laurent")}
    require(len(json.dumps(reference_identity,sort_keys=True,separators=(",",":")).encode())<=8192,
            "bounded exact reference identity metadata before new Arb reference bounds")
    c=coefficients({j:exact(v) for j,v in ui.items()},
                   {j:exact(v) for j,v in vr.items()},exact(ref["beta"]),exact(ref["K"]))
    A=[polynomial_A0(v) for v in c["a"]];B=[polynomial_A0(v) for v in c["b"]]
    aq=exact(q)
    R0=upper(cross_local_norm(c,aq,"HL")+primitive_cross(c["a"],c["b"],A,B,aq,"HL"))
    R1=upper(cross_local_norm(c,aq,"HL",output_derivative=True)
             +primitive_cross(c["a"],c["b"],A,B,aq,"HL",output_derivative=True))
    return {"q":aq,"eta":exact(eta),"coefficients":c,"A":A,"B":B,"R0":R0,"R1":R1,
            "reference_hash":hashlib.sha256(rawdef).hexdigest(),
            "reference_identity":reference_identity}

def original_delta_difference(row):
    base=row["original_complete_repaired_bounds"]
    fee=row["complete_delta_fees"]
    U,V,U1,V1=(saved(base[k]) for k in ("U_A0","V_A0","U_phi_A0","V_phi_A0"))
    e0=saved(row["full_delta_A0"]);e1=saved(row["full_delta_angular_A0"])
    beta=mag(whole(row["original_intrinsic_enclosure"]["beta"]))
    K=mag(whole(row["original_intrinsic_enclosure"]["K"]))
    local=saved(fee["local_a"])+saved(fee["local_e"])+(1+K)*saved(fee["local_b"])
    primitive=beta/2*(e1*(U+e0+K*(V+e0))+(U1+V1)*(1+K)*e0)
    hl=upper(384*saved(fee["drift"])+local+primitive)
    lh=upper(hl+saved(fee["drift_phi"]))
    return hl,lh

def complete_row_bounds(cubic,repair,row,kernel,left,right,reference,lambda_inverse):
    intrinsic=row["original_intrinsic_enclosure"]
    old=row["complete_delta_bounds"];base=row["original_complete_repaired_bounds"]
    q=reference["q"]; invq=1/q
    snorm=max(arb(1),upper(q)); sinv=max(arb(1),upper(invq))
    condition=upper(snorm*sinv)
    beta=whole(intrinsic["beta"]);K=whole(intrinsic["K"])
    require(K.lower()>0,"original positive body curvature")
    Kplus=upper(K); betaplus=mag(beta)
    speed=whole(old["radial_speed"])
    require(speed.lower()>0,"original positive actual speed")
    local=saved(old["local_a_A0"])+saved(old["local_e_A0"])
    ell=saved(old["local_b_A0"]);drift=saved(old["drift_A0"])
    primitive=saved(old["primitive_raw_L2"]);meanrank=saved(old["mean_rank_raw_L2"])
    eta=reference["eta"]
    principal=384*max(upper(mag(speed*K-eta*q*q)/q),upper(q*mag(speed-eta)))
    e=upper(384*drift+principal+local+(Kplus/q+q)*ell+condition*(primitive+meanrank))
    ui,vr=fields(cubic,repair,row["original_candidate_piece"],left,right,intrinsic)
    c=coefficients(ui,vr,beta,K); r=reference["coefficients"]
    difference={key:poly_difference(c[key],r[key]) for key in ("d","la","le","ell","Kell")}
    da=[poly_difference(c["a"][i],r["a"][i]) for i in range(2)]
    db=[poly_difference(c["b"][i],r["b"][i]) for i in range(2)]
    DA=[polynomial_A0(v) for v in da]; DB=[polynomial_A0(v) for v in db]
    A=[betaplus*saved(base["U_phi_A0"]),betaplus*saved(base["V_phi_A0"])]
    B=[saved(base["U_A0"]),Kplus*saved(base["V_A0"])]
    deltaHL,deltaLH=original_delta_difference(row)
    centre_difference=(
        cross_local_norm(difference,q,"HL")
        +primitive_cross(da,c["b"],DA,B,q,"HL")
        +primitive_cross(r["a"],db,reference["A"],DB,q,"HL"))
    EB=upper(lambda_inverse*(centre_difference+sinv*deltaHL))
    LH=upper(cross_local_norm(c,q,"LH",input_H1=True)
         +primitive_cross(c["a"],c["b"],A,B,q,"LH",input_H1=True)
         +1153*snorm*deltaLH)
    R0=reference["R0"];R1=reference["R1"]
    CA=upper(lambda_inverse*((upper(speed)*max(arb(1),Kplus)+drift)*R1
              +(local+(1+Kplus)*ell+primitive)*R0))
    CB=upper(snorm*saved(kernel["bounds"]["high_to_low_raw"])*R0)
    return {"e":e,"EB":EB,"CA":CA,"CB":CB,"LH":LH}

def parent_mesh(literals):
    root_lower=Fraction(literals["rstar_interval"][0])
    cut=Fraction(literals["c_body"]);right=Fraction(literals["R"])
    rho=cut-root_lower
    require(rho>0,"same root/collar ordering")
    result=[{"kind":"collar","left":"actual_rstar","right":cut,"length_upper":rho}]
    left=cut
    for band in range(20):
        if left==right: break
        end=min(right,root_lower+2*rho)
        require(left<end,"positive body mesh band")
        for sub in range(8):
            lo=left+(end-left)*sub/8;hi=left+(end-left)*(sub+1)/8
            result.append({"kind":"body","left":lo,"right":hi,"length_upper":hi-lo,
                           "band":band,"subcell":sub})
        left=end;rho*=2
    require(left==right and len(result)<=161,"predeclared mesh resource cap")
    return result


KIND="complete_frozen_cross_block_value_tail_v1"
ORDERED_TARGETS=["complete_frozen_cell_coefficient_maxima",
 "complete_uniform_refinement_one","complete_uniform_refinement_two",
 "complete_predeclared_mesh_selection","conditional_same_tail_resolvent"]
SCOPE={"same_positive_given_head_realization":True,"selected_member_scope_retained":True,
 "ordinary_dr_and_normalized_real_reflection":True,"complete_193_head_components":True,
 "full_mean_and_affine_jump_ports_retained":True,"true_outer_chart_and_all_cross_terms_retained":True,
 "old_negative_head_and_metric_obligations_retained":True,"physical_96_signed_inverse_proved":False,
 "complete_coupled_head_inverse_proved":False,"finite_matrix_inverse_proved":False,
 "reference_is_not_a_certified_actual_point_value":True,
 "only_centre_reference_mean_column_has_exact_zero_high_image":True,
 "new_array_artifacts":False,"old_targets_recomputed":0}
MAX_SCIENTIFIC_BYTES=40000

def main():
    global arb, require
    import argparse, copy, importlib.metadata, os, platform, sys, time
    from pathlib import Path
    from fourfold_codazzi_frozen_cross_block_readonly import (
        admit,canonical,data,digest,require,PARAMETERS,PROBLEM_ID,CHECKS)
    parser=argparse.ArgumentParser(description="Only new whole WPTV/VR targets.")
    for option in ("repo","manifest","manifest-sha","out","native","native-receipts",
                   "candidate-index","centre-repair"):
        parser.add_argument("--"+option,required=True)
    parser.add_argument("--bits",type=int,required=True)
    parser.add_argument("--preflight-only",action="store_true")
    args=parser.parse_args()
    require(args.bits==320,"predeclared precision")
    admitted=admit(args.repo,args.manifest,args.manifest_sha,args.native,
                   args.native_receipts,args.candidate_index,args.centre_repair)
    if args.preflight_only:
        print(canonical({"complete":True,"preflight_only":True,
              "admission":admitted["admission"]}).decode("utf-8"),end="",flush=True)
        return
    output=Path(args.out)
    require(not output.exists(),"already saved scientific conclusion is immutable")
    output.parent.mkdir(parents=True,exist_ok=True)
    manifest=admitted["manifest"]
    require(manifest["retained_scope"]==SCOPE,"fixed retained physical scope")
    started=time.monotonic()
    whv=admitted["WHV"]
    document={"kind":KIND,"problem_id":PROBLEM_ID,"complete":False,"stage":"admitted",
     "failure":None,"current_target":None,"completed_targets":[],
     "parameters":PARAMETERS,"manifest_sha256":args.manifest_sha,
     "actual_checkout_commit":os.environ["ACTUAL_CHECKOUT_COMMIT"],
     "scientific_modules":admitted["scientific_modules"],
     "inventory_sha256":manifest["inventory"]["sha256"],
     "mathematical_contract_sha256":manifest["mathematical_contract"]["sha256"],
     "refinement_contract_sha256":manifest["refinement_contract"]["sha256"],
     "original_input_sha256":{s["role"]:s["sha256"] for s in manifest["core_current_files"]},
     "copied_original_records":{"original_nine":copy.deepcopy(admitted["literals"]),
        "WHV_readonly_records":{key:copy.deepcopy(whv["new_records"][key])
                               for key in ("A_c","A_c_weight","pi")},
        "WHV_previous_strict_mesh_gate":whv["strict_mesh_gate"],
        "WHV_previous_required_N_diagnostic":copy.deepcopy(whv["required_N_diagnostic"]),
        "WHV_previous_actual_progress":copy.deepcopy(whv["actual_progress"])},
     "copied_original_scope":copy.deepcopy(admitted["old_scope"]),
     "copied_complete_candidate_metadata":copy.deepcopy(admitted["candidate_metadata"]),
     "copied_complete_repair_definition":copy.deepcopy(admitted["repair_definition"]),
     "original_admission":admitted["admission"],"retained_scope":SCOPE,"runtime":{},
     "gates":copy.deepcopy(admitted["admission"]["checks"]),
     "actual_progress":{"scientific_targets_started":0,"scientific_targets_completed":0,
        "completed_parent_cells":0,"completed_body_intersections":0,
        "new_whole_maxima_completed":0,"new_scalar_records_completed":0,
        "new_strict_comparisons_completed":0,"conditional_resolvents_completed":0,
        "old_targets_recomputed":0,"original_repairs_regenerated":0,
        "finite_matrix_allocations":0,"new_array_artifacts":0},
     "mesh_summary":None,"current_parent":None,"last_completed_parent":None,
     "reference_chain":{"count":0,"sha256":hashlib.sha256(b"").hexdigest()},
     "complete_coefficient_maxima":{},
     "whole_candidates":{},"selected_mesh":None,"conditional_inverse":None}
    def publish():
        raw=canonical(document)
        tmp=output.with_name(output.name+".tmp")
        with tmp.open("wb") as stream:
            stream.write(raw);stream.flush();os.fsync(stream.fileno())
        os.replace(tmp,output)
        require(output.read_bytes()==raw,"complete scientific file readback")
        print(raw.decode("utf-8"),end="",flush=True)
        require(len(raw)<=MAX_SCIENTIFIC_BYTES,"complete scientific output byte limit")
        return data(raw)
    def start_target(name):
        require(document["current_target"] is None
                and name==ORDERED_TARGETS[len(document["completed_targets"])],
                "ordered new target and no repetition")
        document["current_target"]=name;document["stage"]=name
        document["actual_progress"]["scientific_targets_started"]+=1
        publish()
    def finish_target(name):
        require(document["current_target"]==name,"whole target complete")
        document["completed_targets"].append(name);document["current_target"]=None
        document["actual_progress"]["scientific_targets_completed"]+=1
        return publish()
    def gate(name,ok):
        document["gates"].append({"name":name,"passed":bool(ok)})
        publish()
        require(ok,name)
    def ball_record(value):
        value=upper(value)
        text=value.str(75)
        require(text.isascii() and 0<len(text)<=256 and not re.search(r"nan|inf",text,re.I),
                "complete finite scientific record")
        return {"ball":text}
    def emit(group,key,value):
        require(key not in group,"new scalar target already saved")
        group[key]=ball_record(value)
        document["actual_progress"]["new_scalar_records_completed"]+=1
        publish()
        return saved(data(output.read_bytes())["whole_candidates"][str(group["refinement"])][key])
    publish()
    try:
        from flint import arb,ctx
        require(platform.python_version()=="3.12.14"
                and importlib.metadata.version("python-flint")=="0.9.0","fixed runtime")
        ctx.prec=320
        document["runtime"]={"python":platform.python_version(),"python_flint":"0.9.0",
                             "bits":320,"old_producer_imports":0,"numpy_imported":False}
        mesh=parent_mesh(admitted["literals"])
        pi_record=copy.deepcopy(whv["new_records"]["pi"])
        pi_lower=whole(pi_record).lower()
        require(pi_lower>0,"original positive pi lower")
        lambda_inverse=saved(whv["new_records"]["A_c_weight"])
        document["mesh_summary"]={"rule":"root collar plus eight subcells of each original-rminus doubling band",
            "parent_cells":len(mesh),"parent_cap":161,
            "declared_refinements":[1,2],"refined_counts":[len(mesh),2*len(mesh)],
            "refined_cap":322,"root":admitted["literals"]["rstar_interval"],
            "body_cut":admitted["literals"]["c_body"],"right":admitted["literals"]["R"],
            "reference_q_floor":"1/8","reference_q_binary_places":20,
            "reference_mean_and_low_1_to_32_zero_only_in_centre":True,
            "all_full_delta_mean_and_low_columns_retained":True,
            "original_closed_rows":4650,"original_interfaces":3594,
            "homogeneous_raw_transmission_is_identity":True}
        gate("predeclared_small_mesh_and_all_original_domains_admitted",
             len(mesh)<=161 and 2*len(mesh)<=322)
        start_target(ORDERED_TARGETS[0])
        names=("A","E_b","U_b","L","B")
        running={name:arb(0) for name in names}
        witnesses={name:None for name in names}
        roots=admitted["literals"];rows=admitted["rows"];kernels=admitted["kernels"]
        cursor=0;covered_rows=set()
        for parent_index,cell in enumerate(mesh):
            left=cell["left"];right=cell["right"]
            descriptor={"parent_index":parent_index,"kind":cell["kind"],
                        "left":str(left),"right":str(right),
                        "length_upper":str(cell["length_upper"])}
            document["current_parent"]={**descriptor,"state":"started"}
            publish()
            # All cell candidates are internal to one declared whole-maxima target.
            # Only a fully processed parent is committed to its persistent prefix.
            candidate=dict(running);candidate_witness=copy.deepcopy(witnesses)
            tau=upper(exact(cell["length_upper"])/pi_lower)
            intersections=0
            if cell["kind"]=="collar":
                values={"A":upper(tau*exact(roots["G_c"])),
                        "L":upper(tau*1153*exact(roots["L_c_raw"]))}
                reference_hash=hashlib.sha256(b"root:S=Id,D=0,B0=0").hexdigest()
                for name,value in values.items():
                    if value>candidate[name]:
                        candidate[name]=value
                        candidate_witness[name]={**descriptor,"original_row":None,
                                                "reference_sha256":reference_hash}
            else:
                reference=exact_reference(admitted["cubic"],rows,(left+right)/2)
                reference_hash=reference["reference_hash"]
                document["current_parent"].update({"reference_sha256":reference_hash,
                    "reference_identity":reference["reference_identity"],"state":"reference_complete"})
                publish()
                covered=left
                while cursor<len(rows) and Fraction(rows[cursor]["interval"][1])<=left:
                    cursor+=1
                row_index=cursor
                while row_index<len(rows) and Fraction(rows[row_index]["interval"][0])<right:
                    row=rows[row_index]
                    lo=max(left,Fraction(row["interval"][0]))
                    hi=min(right,Fraction(row["interval"][1]))
                    require(lo==covered and lo<hi,"all original closed row intersections")
                    bounds=complete_row_bounds(admitted["cubic"],admitted["repair_suprema"],
                        row,kernels[row_index],lo,hi,reference,lambda_inverse)
                    values={"A":upper(tau*bounds["e"]),"E_b":bounds["EB"],
                            "U_b":upper(tau*bounds["CA"]),"L":upper(tau*bounds["LH"]),
                            "B":upper(tau*tau*bounds["CB"])}
                    for name,value in values.items():
                        value=upper(value)
                        if value>candidate[name]:
                            candidate[name]=value
                            candidate_witness[name]={**descriptor,"original_row":row_index,
                             "original_piece":row["original_candidate_piece"],
                             "intersection":[str(lo),str(hi)],"reference_sha256":reference_hash}
                    covered=hi;intersections+=1;covered_rows.add(row_index)
                    if covered==right:break
                    row_index+=1
                require(covered==right and intersections>0,"whole parent cell covered")
                cursor=row_index
            for name in names:
                document["complete_coefficient_maxima"][name]={
                    **ball_record(candidate[name]),"witness":candidate_witness[name]}
            chain=bytes.fromhex(document["reference_chain"]["sha256"])+bytes.fromhex(reference_hash)
            document["reference_chain"]={"count":parent_index+1,"sha256":hashlib.sha256(chain).hexdigest()}
            document["actual_progress"]["completed_parent_cells"]=parent_index+1
            document["actual_progress"]["completed_body_intersections"]+=intersections
            document["last_completed_parent"]={**descriptor,"reference_sha256":reference_hash,
                                             "body_intersections":intersections}
            document["current_parent"]=None
            returned=publish()
            running={name:saved(returned["complete_coefficient_maxima"][name]) for name in names}
            witnesses={name:copy.deepcopy(returned["complete_coefficient_maxima"][name]["witness"])
                       for name in names}
        require(document["actual_progress"]["completed_parent_cells"]==len(mesh)
                and Fraction(rows[-1]["interval"][1])==Fraction(25,8)
                and document["actual_progress"]["completed_body_intersections"]>=4650
                and len(covered_rows)==4650,
                "complete original body represented in finished parent prefix")
        document["actual_progress"]["new_whole_maxima_completed"]=5
        document["actual_progress"]["new_scalar_records_completed"]=5
        saved_document=finish_target(ORDERED_TARGETS[0])
        gate("complete_five_whole_maxima_and_all_original_closed_rows_saved",True)
        maxs={name:saved(saved_document["complete_coefficient_maxima"][name]) for name in names}
        Cc=saved(roots["C_c"]);Cb=saved(roots["C_b"]);Ec=saved(whv["new_records"]["A_c"])
        for refinement,target in ((1,ORDERED_TARGETS[1]),(2,ORDERED_TARGETS[2])):
            start_target(target)
            group={"refinement":refinement,"parent_cells":len(mesh),
                   "refined_cells":refinement*len(mesh),"complete":False,
                   "all_parent_S_D_B0_enclosures_inherited":True}
            document["whole_candidates"][str(refinement)]=group
            a=Cc*Ec;b=Cb*(maxs["E_b"]+maxs["U_b"]/refinement)
            source=emit(group,"complete_source_quadrature_upper",upper((a*a+b*b).sqrt()))
            feedback=emit(group,"complete_feedback_upper",
                          upper(maxs["L"]*source/refinement+maxs["B"]/(refinement*refinement)))
            delta=emit(group,"complete_delta_upper",upper(maxs["A"]/refinement+feedback))
            group["strict_tail_gate"]=bool(delta<1);group["complete"]=True
            document["actual_progress"]["new_strict_comparisons_completed"]+=1
            finish_target(target)
            gate("complete_uniform_refinement_"+str(refinement)+"_saved_including_its_true_comparison",True)
        start_target(ORDERED_TARGETS[3])
        for refinement in (1,2):
            group=document["whole_candidates"][str(refinement)]
            if group["strict_tail_gate"]:
                document["selected_mesh"]={"refinement":refinement,
                    "refined_cells":refinement*len(mesh),
                    "complete_delta_upper":copy.deepcopy(group["complete_delta_upper"]),
                    "selection_rule":"first admitted predeclared mesh, coarse first",
                    "all_four_finite_Schur_blocks_and_both_rhs_still_required":True}
                break
        finish_target(ORDERED_TARGETS[3])
        gate("only_complete_predeclared_candidates_selected_and_no_adaptive_refinement",True)
        if document["selected_mesh"] is not None:
            start_target(ORDERED_TARGETS[4])
            delta=saved(document["selected_mesh"]["complete_delta_upper"])
            require(delta<1,"saved strict gate before a resolvent")
            gap=(arb(1)-delta).lower()
            require(gap>0,"positive saved resolvent denominator")
            document["conditional_inverse"]={"refinement":document["selected_mesh"]["refinement"],
                "complete_same_tail_inverse_upper":ball_record(1/gap),
                "finite_signed_inverse_proved":False}
            document["actual_progress"]["new_scalar_records_completed"]+=1
            document["actual_progress"]["conditional_resolvents_completed"]=1
            publish()
            finish_target(ORDERED_TARGETS[4])
        gate("conditional_tail_inverse_only_after_true_gate_and_zero_finite_allocations",
             (document["conditional_inverse"] is not None)==(document["selected_mesh"] is not None))
        gate("complete_scientific_target_shape_and_old_zero_recomputation",
             len(document["completed_targets"]) in (4,5)
             and document["actual_progress"]["new_scalar_records_completed"] in (11,12)
             and document["actual_progress"]["new_strict_comparisons_completed"]==2
             and document["actual_progress"]["new_whole_maxima_completed"]==5
             and document["actual_progress"]["finite_matrix_allocations"]==0
             and document["actual_progress"]["old_targets_recomputed"]==0)
        document["complete"]=True;document["stage"]="complete"
        document["runtime"]["wall_seconds"]=time.monotonic()-started
        publish()
    except Exception as error:
        document["complete"]=False;document["stage"]="failed_saved_complete_prefix"
        message=str(error)
        encoded=message.encode("utf-8")
        if len(encoded)>1000:message=encoded[:1000].decode("utf-8","ignore")
        document["failure"]={"type":type(error).__name__,"message":message,
            "completed_targets_retained":True,"completed_parent_prefix_retained":True,
            "no_automatic_scientific_restart":True}
        document["runtime"]["wall_seconds"]=time.monotonic()-started
        publish()
        raise

if __name__=="__main__":
    main()
