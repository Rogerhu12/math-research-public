#!/usr/bin/env python3
"""Read accepted complete conclusions and bound factored g/y/q sources.

Only new scalar factor products, the regular quotient, the identified inverse
remainder branch, and ten complete source comparisons are evaluated. All old
targets, forcing, amplitudes, inverse/profile/word bounds, coefficient rows and
radial weights are restored without reevaluation. Reproducible output is
temporary to the public Actions runner.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_factored_transport_and_companion_complete_sources_v1"
CONTRACT="64e9ae0f3b9a3f62a2aa5d84c0b820c0d3af9100ba8c2a77cf587695af72d8d4"
FACTOR_CONTRACT="0b4099e02bca3c81e046b5102760c0c994da114c201ccf2200cd4f1fcf5f4ff8"
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
S_EXEC="3896925b758840c4bbf2ce910141ca8a93d725d56bf22b5002e9c0b2486004af"
S_SOURCE="564759dceb4b38dd37fdd275d0fa3e22cdf2efa271cd9ef1049c6cfa4ff121f6"
S_MANIFEST="a6fbb28de8a85bd6f71054df0056a869285f131cc4c4702c66e5434deb7061cf"
C_EXEC="bca0f97d7c610f8f2572e61d1e1442a8b9c256a4c5429253682b6d803e3a21c3"
C_SOURCE="b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0"
C_MANIFEST="8465759dfe9101bb7e20275cec1a5b98e23efb4dbe643e492fb8189250b005b9"
D_EXEC="2c5cba2e7351267e090d0ca6c06cfecbb21309c039a7844937ee64026254f1d0"
D_SOURCE="1aa46093bba5150d636cc7c6ef4f5b080447fc2c75d7438b2e52ae5fa6b5d0af"
D_MANIFEST="5ce9aceb3be46e795696c09028f39091fdc9a4f969dba0e0b317408974083e9b"
G_EXEC="1fe8a528ec5e22dedc0803a129591de2fd3f25d148c5e57cb1c619cc06463bc1"
G_SOURCE="617bf821e9cff5847b4257e448fe8556eda63acf5c018105a2dff32ac452cf8a"
G_MANIFEST="aadf3e2bcf02d818e12c8950b4b4eb523345a4a63777a16d39720f98040a5e3f"
P_EXEC="8cc43eb17f28b6b3fd82b9a220e8db86c7eb53fa7c491d0de7f8feda70bfc926"
P_SOURCE="c479aaec9438a80340e425223b2eac0ed9b5707583c6a8125553e59ccd189048"
P_MANIFEST="8113b0d7e73c220a766947c198c09b6e66bd3a83210539fed6b4d6d5285e8e3f"
B_EXEC="20422f41645c2a4544bb8a0d79eddf771b45ff0386cc81b3ee97a32849586ef2"
B_SOURCE="e0541949f521e0852bb4a8b204b51281f7d83e0ed2a7a1afbb259ca73362e92a"
B_MANIFEST="5e2618c446288cd8d84fcbf4bb7955f56f7a1041f823e05213d043d20b5aeaaf"
H_EXEC="fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57"
H_SOURCE="9596ebee08e95939cf1b8a9d46a9f32053bd4706cc77e2263a80d09ede99294c"
H_MANIFEST="1869212f28702ae915787a6b5189406b13e6824b93e436a8650fa83e86b11f99"
OLD_NATIVE="7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c"
OLD_PROCESS="f888e47e69f41b4b5c73656ac9afd321289a806ce948816d9612111a045d99e4"
OLD_SOURCE="56b68983f36bb3d88e1427081ba9e60a8f6cf43dcd9578a0d925e1834292555d"
OLD_MANIFEST="7290cbb07293c15a239ffafb0e342e6c1b7ea812106f569e88bbe4d2502180df"
ROOT_SHA="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
FORCE_SHA="54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47"
H=Q(893368603925465506687,21990232555520000000000000)
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
RG=Q(3,8000);SG=Q(3,128);CW=Q(1,32);SP=Q(1,256)
SB=Q(1,64);SW=Q(1,128);RT=Q(3,5000);SA=Q(13,2048)
RF=Q(3,20000);N=388
BRANCHES=("central","positive_characteristic","negative_characteristic")
FIRST=("complete_RQ_J_g","complete_primitive","old_mean_transported","old_mean_vphi")
MEAN=("complete_uJ_g",)
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(x):
    v=Q(x);return arb(v.numerator)/arb(v.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    return arb(v["ball"])
def up(v):return abs(rb(v)).upper()
def gap(v,label):
    v=rb(v).lower()
    if not v.is_finite() or not v>0:raise ValueError("missing complete positive gap: "+label)
    return v
def bound(v,label):
    v=rb(v)
    if not v.is_finite() or v.lower()<0:raise ValueError("invalid complete upper bound: "+label)
    return v.upper()
def powr(v,p):return (rb(v).log()*ex(p)).exp()
def rec(v):return dict(ball=rb(v).str(64))
def unpack(v):
    if isinstance(v,dict):
        if set(v)=={"ball"}:return arb(v["ball"])
        return {k:unpack(x) for k,x in v.items()}
    if isinstance(v,list):return [unpack(x) for x in v]
    return v
def encode(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return v
def read(p):
    p=Path(p);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
def payload_sha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(p,v,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    b=(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    t=p.with_name(p.name+".partial");t.write_bytes(gzip.compress(b,mtime=0) if compressed else b);t.replace(p)
def receipt(path,run,source,manifest,gate):
    e=read(path);r=e.get("actual_scientific_receipt",{})
    gate("accepted complete run "+run+"/1 is restored with its exact scientific identity",
        str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("source_sha256")==source
        and r.get("input_manifest_sha256")==manifest and r.get("runtime")==RUNTIME
        and r.get("gates") and all(g.get("passed") is True for g in r["gates"]))
    return r



def read_positive_coefficients(C,gate):
    rows=C["complete_positive_linear_operator_conclusion"]
    gate("the eighteen accepted positive coefficients retain the identical complete profile branches and input ordering",
        len(rows)==3 and [r["branch"] for r in rows]==list(BRANCHES)
        and all(r["exact_input_component_order"]==["a","a_phi","a_phiphi","b","b_phi","b_phiphi"]
            and len(r["complete_positive_linear_coefficients"])==6
            and len(r["selected_inputs"])==6
            and all(v["denominator_is_lower_for_bound_number_only"] for v in r["selected_inputs"]) for r in rows)
        and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
        and C["scope"]["all_input_abs_j_at_least97"]
        and C["scope"]["budget_parameter_lower_is_not_true_amplitude_lower"])
    return [[rb(v) for v in r["complete_positive_linear_coefficients"]] for r in rows]


def selected_rows(rows):
    left,right=PIECE[0],ROOTS[1];out=[];cursor=left;parts=0
    for row in rows:
        lo,hi=map(Q,row["interval"]);a=max(lo,left);b=min(hi,right)
        if not a<b:continue
        if a!=cursor:raise ValueError("the original rows no longer cover the actual physical interval")
        cuts=sorted(set([a,b]+[t for t in ROOTS if a<t<b]))
        parts+=len(cuts)-1;out.append(row);cursor=b
    if cursor!=right or not out:raise ValueError("incomplete actual negative cover")
    return out,parts



def add(*values,k):
    if any(len(v)<=k for v in values):raise ValueError("an angular sum omitted a derivative")
    return [up(sum((v[q] for v in values),arb(0))) for q in range(k+1)]

def scale(v,a,k):
    if len(v)<=k:raise ValueError("an angular scalar product omitted a derivative")
    return [up(rb(a)*v[q]) for q in range(k+1)]

def mul(a,b,k):
    if min(len(a),len(b))<=k:raise ValueError("an angular product omitted a derivative")
    return [up(sum((math.comb(q,j)*a[j]*b[q-j] for j in range(q+1)),arb(0)))
        for q in range(k+1)]

def product(*values,k):
    if not values:raise ValueError("empty ordered scalar product")
    result=list(values[0][:k+1])
    for value in values[1:]:result=mul(result,value,k)
    return result

def cauchy(value,width,k):
    if not Q(width)>0:raise ValueError("nonpositive Cauchy width")
    return [up(math.factorial(q)*rb(value)/ex(Q(width)**q)) for q in range(k+1)]

def pair_add(a,b,k):
    return [add(a[i],b[i],k=k) for i in range(2)]

def pair_mul(v,w,k):
    return [mul(v,w[i],k) for i in range(2)]

def pair_scale(w,value,k):
    return [scale(w[i],value,k) for i in range(2)]

def pair_diff(w):
    return [list(w[i][1:]) for i in range(2)]

def read_real_jets(S,G,gate):
    cases=[v for v in S["cases"] if Q(v["exact_output_old_phi_width"])==0]
    if len(cases)!=1:raise ValueError("the accepted real angular table is not unique")
    case=cases[0];out={}
    if Q(case["exact_whole_physical_cover_radius"])!=H:raise ValueError("the accepted whole root cover changed")
    for name in ("fa","a1","b1"):
        fields=[v for v in case["fields"] if v["field"]==name]
        if len(fields)!=1:raise ValueError("the original complete amplitude field changed")
        field=fields[0]
        if not (Q(field["exact_output_old_phi_width"])==0
            and field["original_complete_bound_only_read"]
            and field["full_radial_and_Fourier_tails_retained"]
            and field["joint_sum_of_radial_coefficient_suprema"]
            and field["amplitude_mean_is_not_independent_physical_even_mean"]):
            raise ValueError("the accepted angular norm or complete mean convention changed")
        rows=[v for v in field["complete_mixed_derivative_rows"] if v["radial_derivative_order"]==0]
        if len(rows)!=1 or rows[0]["angular_derivative_orders"]!=[0,1,2,3]:
            raise ValueError("the accepted complete zero-radial-order row changed")
        out[name]=[bound(v,name+" real angular jet") for v in rows[0]["complete_joint_Wiener_upper"]]
        if len(out[name])!=4:raise ValueError("a saved real derivative row is incomplete")
    extra=G["missing_derivative_conclusions"]
    for name in ("a1","b1"):
        out[name].append(bound(extra["complete_real_fourth_angle_first_correction_upper"][name],name+" fourth derivative"))
    gate("all real forcing and correction jets and the two fourth derivatives are restored with complete tails and means",
        all(len(out[n])==(4 if n=="fa" else 5) for n in out)
        and extra["all_original_order_two_inverse_values_only_read"]
        and G["original_target_FFT_intrinsic_fold_transport_or_Taylor_recomputed"]==0
        and S["original_signed_Taylor_coefficients_recomputed"]==0)
    return out

def supporting_coefficients(f,c,P,B,S,gate):
    """G9--17: new factor budgets on H; every old fold/product number is read."""
    pd=P["complete_domain_conclusion"];bd=B["complete_domain_conclusion"]
    TH=bound(pd["physical_T_image_upper"],"accepted complete physical T image")
    XH=bound(pd["physical_X_image_upper"],"accepted complete physical X image")
    # The frozen P producer defines TH as H*Ap^(2/3). The same full SG fold
    # modulus therefore bounds T on SG; no old image power is recomputed.
    gate("the accepted physical image is the identical full-fold expression and the larger regular product remains exact",
        Q(pd["exact_actual_old_phi_strip"])==SP
        and Q(pd["exact_full_physical_cover"])==H
        and pd["actual_sT_segments_remain_in_original_product"]
        and pd["original_leading_and_reference_gauges_unchanged"]
        and Q(bd["exact_new_canonical_radius"])==RT
        and Q(bd["exact_new_canonical_strip"])==SA
        and Q(bd["exact_full_physical_cover"])==H
        and Q(bd["exact_new_old_rho_radius"])==Q(1,8000)
        and Q(bd["exact_new_old_phi_strip"])==Q(3,512)
        and bd["all_sT_paths_in_same_paid_domain"]
        and bd["root_normalization_and_all_means_unchanged"]
        and B["old_forcing_fold_transport_RF_or_profile_recomputed"]==0)
    Am=gap(f["Am"],"complete A modulus lower")
    mu=gap(f["mu"],"complete principal mu modulus lower")
    t=ex(H/RG)
    smallx=up(t*bound(f["j"],"complete x-1 root budget"))
    y0=up(t*t*bound(f["BT"],"complete T_phi root budget"))
    z0=up(ex(Q(2,3))*t*bound(f["BA"],"complete A_phi root budget")/Am)
    x=cauchy(smallx,SG,4);x[0]=up(1+smallx)
    y=cauchy(y0,SG,4);zeta=cauchy(z0,SG,4)
    T=[TH]+y[:4]
    q=[bound(f["Q"],"complete Q")];g=[bound(f["G"],"complete G with radial mean")]
    for n in range(4):
        q.append(up(sum((math.comb(n,j)*q[j]*zeta[n-j] for j in range(n+1)),arb(0))/2))
        g.append(up(sum((math.comb(n,j)*g[j]*zeta[n-j] for j in range(n+1)),arb(0))/4))
    bplus=add(mul(x,x,4),product(T,y,y,k=4),k=4)
    factor=scale(product(q,g,bplus,k=4),ex(Q(1,2)),4)
    D0=bound(c["D"][0],"complete physical drift")
    D1=bound(c["D"][1],"complete physical drift derivative")
    T0=bound(c["T0"],"complete T0")
    qr_gap=gap(ex(RG-H),"complete Q radial derivative margin")
    HQ=up(q[0]/qr_gap+D0*q[0]*z0/2+q[0]*D1+T0*q[0])
    c0=up((HQ*x[0]+q[0]*q[0]*y0*y0/2)/mu)
    xi0=up((HQ*y0+q[0]*q[0]*x[0]*z0/2)/mu)
    ct=cauchy(c0,SG,3);xi=cauchy(xi0,SG,3)
    M=bound(f["M"],"complete leading a0")
    B2=bound(f["B2"],"complete b0/T squared")
    Bi=bound(f["Bi"],"complete inverse leading branch")
    ma=bound(bd["complete_new_amplitude_modulus"]["a1"],"accepted canonical a1")
    mb=bound(bd["complete_new_amplitude_modulus"]["b1"],"accepted canonical b1")
    Acan=up(Bi*Bi*(M*ma+B2*ex(RT**3)*mb))
    dT=gap(ex(RT)-TH,"regular quotient T margin")
    dX=gap(ex(SA)-XH,"regular quotient X margin")
    Fb=bound(S["complete_forcing_conclusion"]["fb"],"accepted normalized fb")
    L0=up(ex(Q(2,3))*(Fb/dT+Acan/dX))
    L=cauchy(L0,SP,3)
    inverse0=[[up(Bi*Bi*M),up(Bi*Bi*B2*TH**3)],
              [up(Bi*Bi*B2*TH**2),up(Bi*Bi*M)]]
    inverse=[[cauchy(inverse0[i][j],SG,3) for j in range(2)] for i in range(2)]
    gate("every new complete regular-quotient margin and original nonzero gap is positive on the same physical strip",
        H<RG and H<Q(1,8000) and 0<SP<SB<SG<CW
        and all(v.is_finite() and v>0 for v in (Am,mu,qr_gap,dT,dX))
        and Q(S["complete_forcing_conclusion"]["exact_new_old_rho_radius"])==RF
        and Q(S["complete_forcing_conclusion"]["exact_new_old_angle_strip"])==SB
        and all(v.is_finite() and v.lower()>=0 for v in (HQ,c0,xi0,Acan,L0)))
    conclusion=dict(exact_full_physical_cover=str(H),exact_physical_phi_strip=str(SP),
        exact_original_fold_radius=str(RG),exact_original_fold_strip=str(SG),
        exact_accepted_canonical_radius=str(RT),exact_accepted_canonical_strip=str(SA),
        accepted_complete_physical_T_image=pd["physical_T_image_upper"],
        accepted_complete_physical_X_image=pd["physical_X_image_upper"],
        complete_positive_gaps=encode(dict(A=Am,mu=mu,Q_radial=qr_gap,T_margin=dT,X_margin=dX)),
        complete_canonical_A_modulus=rec(Acan),complete_regular_breg_modulus=rec(L0),
        complete_cT_holomorphic_upper=rec(c0),complete_Xi_holomorphic_upper=rec(xi0),
        exact_regular_root_condition="B(0,X)=fb(0,X)",
        all_sT_segments_in_accepted_product=True,
        full_mean_and_radial_G_scalar_retained=True,
        physical_T_image_definition_read_from_frozen_producer=True,
        old_image_fold_forcing_and_amplitude_enclosures_recomputed=False)
    return dict(x=x,y=y,zeta=zeta,T=T,Q=q,G=g,Bplus=bplus,factor=factor,
        cT=ct,Xi=xi,breg=L,M_inverse=inverse,complete_T_modulus=TH),conclusion

def complete_factored_sources(C,jets,Hr,gate):
    """G3--7 component order is preserved before positive scalar products."""
    x,y,zeta,T,q,g=C["x"],C["y"],C["zeta"],C["T"],C["Q"],C["G"]
    ct,xi,L=C["cT"],C["Xi"],C["breg"]
    w0=[mul(g,add(mul(x,x,4),product(T,y,y,k=4),k=4),4),
        scale(product(g,x,y,k=4),2,4)]
    w1=[jets["a1"],jets["b1"]];fa=jets["fa"]
    inverse=C["M_inverse"]
    Z=[add(mul(inverse[i][0],w1[0],3),mul(inverse[i][1],w1[1],3),k=3) for i in range(2)]
    A,B=Z
    diagonal=add(mul(ct,x,3),product(T,y,xi,k=3),k=3)
    lower=add(mul(x,xi,3),mul(ct,y,3),zeta,k=3)
    upper=add(product(T,x,xi,k=3),product(T,ct,y,k=3),y,k=3)
    g0=pair_mul(C["factor"],[diagonal,lower],3)
    g1=pair_mul(C["factor"],[
        add(mul(x,fa,3),product(T,y,L,k=3),mul(diagonal,A,3),mul(upper,B,3),k=3),
        add(mul(y,fa,3),mul(x,L,3),mul(diagonal,B,3),mul(lower,A,3),k=3)],3)
    hi=Hr["old_circle_inverse"]
    det=gap(hi["complete_deformed_determinant_modulus_lower"],"accepted complete genuine determinant")
    V=bound(hi["complete_composed_V_angular_derivative_bounds"][0],"accepted full composed V")
    pref=cauchy(up(q[0]*V/det),SB,4)
    pref0=cauchy(up(q[0]*V*g[0]*C["Bplus"][0]/det),SB,4)
    rank0=pair_mul(pref0,[mul(x,y,4),mul(y,y,4)],4)
    inner=add(mul(y,w1[0],4),mul(x,w1[1],4),k=4)
    rank1=pair_mul(pref,[mul(x,inner,4),mul(y,inner,4)],4)
    full=[];temp=[]
    for density,(w,gbase,rank) in enumerate(((w0,g0,rank0),(w1,g1,rank1))):
        # p=(-sQK-n^-2 QV)w and g=G0w+n^-2 d_phi(QVw).
        principal=[product(q,T,w[1],k=3),mul(q,w[0],3)]
        p=pair_add(principal,pair_scale(rank,ex(Q(1,N*N)),3),3)
        gg=pair_add(gbase,pair_scale(pair_diff(rank),ex(Q(1,N*N)),3),3)
        full.append(dict(density=density,g=gg,p=p))
        temp.append(dict(density=density,leading_or_correction_amplitude=encode(w),
            factored_transport=encode(gbase),genuine_rank_through_four=encode(rank),
            complete_p=encode(p),complete_g=encode(gg)))
    gate("both complete density sources preserve the ordered genuine rank and their exact physical input weights",
        Q(hi["exact_old_rho_radius"])>=H and Q(hi["exact_inverse_phi_strip"])==SB
        and Q(hi["exact_full_physical_root_cover"])==H
        and hi["full_mean_output_retained"] and hi["actual_reference_seam_jumps_retained"]
        and all(v.is_finite() and v.lower()>=0 for f in full for k in ("g","p") for a in f[k] for v in a)
        and len(full)==2 and N==4*97)
    return full,dict(new_supporting_coefficients=encode(C),new_Z_jets=encode(Z),
        ordered_factor_and_rank_products=temp)

def inverse_remainder(Hr,G,gate):
    hi=Hr["old_circle_inverse"]
    w0=bound(hi["complete_inverse_Wiener_angular_derivative_bounds"][0],"accepted inverse Wiener minimum")
    cf=rb(hi["complete_two_signed_Fourier_conversion_factor"])
    b0=rb(hi["complete_inverse_HV_angular_derivative_bounds"][0])
    first_lower=(gap(cf,"accepted Fourier conversion number")*gap(b0,"accepted inverse number")).lower()
    delta=(w0-1).upper()
    gate("the frozen inverse minimum selected its constant-plus-remainder branch with a nonnegative recoverable remainder",
        w0<first_lower and delta.is_finite() and delta.lower()>=0
        and Q(hi["exact_Wiener_phi_strip"])==SW
        and hi["inverse_constant_subtraction"]=="-i epsilon times identity, retained exactly"
        and hi["same_strip_sup_called_Wiener"] is False and hi["full_mean_output_retained"])
    missing=[r for r in G["missing_derivative_conclusions"]["genuine_inverse_missing_angular_orders"]
        if Q(r["exact_output_phi_strip"])==0]
    if len(missing)!=1 or Q(missing[0]["exact_margin"])!=SB:
        raise ValueError("the accepted real third inverse derivative product changed")
    accepted=[bound(v,"accepted inverse derivative") for v in hi["complete_inverse_HV_angular_derivative_bounds"][1:]]
    accepted.append(bound(missing[0]["B_phi3_upper"],"accepted inverse third derivative"))
    if len(accepted)!=3:raise ValueError("the complete inverse derivatives are truncated")
    dj=[delta]+[min(up(math.factorial(q)*delta/ex(SW**q)),accepted[q-1]).upper() for q in (1,2,3)]
    return dj,dict(accepted_Wiener_minimum=hi["complete_inverse_Wiener_angular_derivative_bounds"][0],
        excluded_first_branch_strict_lower=rec(first_lower),
        complete_inverse_remainder_Wiener_upper=rec(delta),
        exact_Wiener_phi_strip=str(SW),complete_real_remainder_derivative_upper=encode(dj),
        exact_constant_minus_i_epsilon_identity_retained=True,
        branch_lower_is_algorithm_number_not_function_lower=True,
        original_inverse_or_Fourier_conversion_recomputed=False)

class PositiveOperator:
    """The accepted full three-profile functional, without recalibration."""
    def __init__(self,coeff):
        self.coeff=[[bound(v,"accepted positive coefficient") for v in row] for row in coeff]
    def __call__(self,v):
        if len(v)!=2 or any(len(a)<3 for a in v):raise ValueError("a complete row symbol omitted an angular derivative")
        ordered=[v[0][0],v[0][1],v[0][2],v[1][0],v[1][1],v[1][2]]
        return up(sum((self.coeff[b][i]*ordered[i] for b in range(3) for i in range(6)),arb(0)))

def complete_window(v,density,A,delta):
    if density==1:
        value=A(v);return value,value
    if density!=0 or any(len(a)<4 for a in v):raise ValueError("the first complete density window needs four real jets")
    # Each matrix entry is bounded by the full saved matrix norm. All four
    # ordered products, including both input means, are included.
    row=mul(delta,add(v[0],v[1],k=3),3)
    Ev=[list(row),list(row)]
    principal=A(v);remainder=A(Ev)
    mean=up(A(pair_diff(v))+A(pair_diff(Ev)))
    return up(principal+remainder+mean),mean

def complete_companion_comparisons(rows,sources,A,delta,words,W2,baseline,gate):
    """New whole row inequalities; the accepted radial integral is only read."""
    if len(rows)!=6:raise ValueError("the complete companion source requires the identical six rows")
    weight=bound(W2,"accepted full squared-envelope radial weight").sqrt()
    weight=weight.upper()
    maxima={};allrows=[];operator_conclusions=[]
    gg=[]
    for source in sources:
        gamma,mean=complete_window(source["g"],source["density"],A,delta)
        gg.append((gamma,mean))
        operator_conclusions.append(dict(density=source["density"],
            amplitude_identity="w0" if source["density"]==0 else "w1=MZ",
            Gamma_g=rec(gamma),M_g=rec(mean),
            same_complete_column_envelope="abs(rho)^(-1/4)",
            complete_zero_mode_and_both_signed_carriers=True))
    KR=bound(words["C_RQJ_directed"],"accepted complete RQJ word")
    KP=bound(words["C_primitive_directed"],"accepted complete primitive word")
    KU=bound(words["C_uJ_directed"],"accepted complete independent-mean uJ word")
    for row in rows:
        c=unpack(row["bounds"]);V=c["V"]
        if len(V)<5:raise ValueError("the complete physical background lacks its fourth derivative")
        V=[bound(v,"original complete physical V jet") for v in V]
        J=bound(c["C_J_scalar"],"original outer scalar J")
        cb=bound(c["cB"],"original complete mean prefactor")
        mt=bound(c["m0_T0"],"original complete transported mean")
        ef=bound(c["exact_nonlocal_even_mean_row_factor"],"original independent physical mean factor")
        first={};physical={};operators=[];companions=[]
        for i,source in enumerate(sources):
            g,p=source["g"],source["p"]
            y=pair_mul(V,p,3)
            q=pair_add(pair_mul(V,g,3),pair_mul(V[1:],p,3),3)
            Gg,Mg=gg[i];Gq,Mq=complete_window(q,i,A,delta);Gy,My=complete_window(y,i,A,delta)
            primitive_mean=up(cb*V[1]*V[0]*Mg/4)
            T0_mean=up(mt*Mg)
            vals=dict(complete_RQ_J_g=up(J*KR*Gg),
                complete_primitive=up(J*KP*Gq),
                old_mean_transported=up(J*(primitive_mean+T0_mean)),
                old_mean_vphi=up(J*cb*V[1]*My))
            for name,value in vals.items():first["density"+str(i)+"_"+name]=value
            physical["density"+str(i)+"_complete_uJ_g"]=up(ef*KU*Gg)
            operators.append(dict(density=i,Gamma_g=Gg,M_g=Mg,Gamma_q=Gq,M_q=Mq,Gamma_y=Gy,M_y=My,
                mean_primitive_before_outer_J=primitive_mean,mean_T0_before_outer_J=T0_mean))
            companions.append(dict(density=i,complete_q=encode(q),complete_y=encode(y)))
        if any(not v.is_finite() or v.lower()<0 for v in list(first.values())+list(physical.values())):
            raise ValueError("a complete factored row bound is invalid")
        for name,value in {**first,**physical}.items():
            maxima[name]=value if name not in maxima else max(maxima[name],value).upper()
        allrows.append(dict(common_row=row["common_row"],exact_original_interval=row["interval"],
            exact_original_complete_row_payload_sha256=payload_sha(row),
            complete_first_row_coefficients=encode(first),complete_physical_mean_coefficients=encode(physical),
            complete_window_operators=encode(operators),new_companion_derivatives=companions))
    terms=dict(baseline["complete_first_source_term_L2_upper"])
    means=dict(baseline["complete_independent_mean_term_L2_upper"])
    evidence=[]
    for i in (0,1):
        for name in FIRST+MEAN:
            key="density"+str(i)+"_"+name;target=terms if name in FIRST else means
            candidate=up(weight*maxima[key]);old=target[key]
            selected,improved=selected_total(old,candidate);target[key]=selected
            evidence.append(dict(source_term=key,output="first" if name in FIRST else "independent_physical_mean",
                same_original_row_count=6,complete_uniform_row_coefficient=rec(maxima[key]),
                accepted_complete_L2_upper=old,new_complete_L2_upper=rec(candidate),
                selected_complete_L2_upper=selected,strictly_smaller_complete_term=improved,
                original_radial_integral_recomputed=False,
                wholeword_contains_original_inner_factors=True))
    gate("ten complete source comparisons preserve every actual row, independent mean factor and unchanged local term",
        len(evidence)==10 and len(maxima)==10 and len(terms)==21 and len(means)==10
        and all(v==terms[k] for k,v in baseline["complete_first_source_term_L2_upper"].items()
            if not any(k=="density"+str(i)+"_"+n for i in (0,1) for n in FIRST))
        and all(v==means[k] for k,v in baseline["complete_independent_mean_term_L2_upper"].items()
            if not k.endswith("_complete_uJ_g")))
    return terms,means,evidence,operator_conclusions,allrows

def selected_total(old,candidate):
    candidate=up(candidate)
    if not candidate.is_finite():raise ValueError("nonfinite complete scalar combination")
    if candidate<rb(old).lower():return rec(candidate),True
    return old,False

def combine(original,terms,means):
    local=original["local_L2_upper"]
    nl_sum=sum((up(v) for k,v in terms.items() if not k.startswith("local_raw_")),arb(0))
    nl,nlnew=selected_total(original["nonlocal_total_L2_upper"],nl_sum)
    first,fnew=selected_total(original["first_L2_upper"],up(local)+up(nl))
    mean,mnew=selected_total(original["mean_L2_upper"],sum((up(v) for v in means.values()),arb(0)))
    pair,pnew=selected_total(original["combined_L2_upper"],(up(first)**2+up(mean)**2).sqrt())
    return dict(local_L2_upper=local,nonlocal_total_L2_upper=nl,first_L2_upper=first,
        mean_L2_upper=mean,combined_L2_upper=pair,
        complete_first_source_term_L2_upper=terms,complete_independent_mean_term_L2_upper=means,
        strictly_smaller_complete_aggregates=dict(nonlocal_total=nlnew,first=fnew,mean=mnew,combined=pnew),
        exact_negative_physical_cover=original["exact_negative_physical_cover"],
        actual_dr_measure=original["actual_dr_measure"],
        one_sided_uncertain_root_band_retained=original["one_sided_uncertain_root_band_retained"],
        both_density_windows_retained=True,
        total_squared_envelope_radial_weight_upper=original["total_squared_envelope_radial_weight_upper"],
        old_nine_word_and_five_physical_mean_counts=original["old_nine_word_and_five_physical_mean_counts"],
        first_output_window=original["first_output_window"],
        independent_even_mean_window=original["independent_even_mean_window"],
        input_window=original["input_window"],outer_J_window=original["outer_J_window"],
        complete_local_budget_read_unchanged=True,
        original_temporary_row_payload_sha256=original["original_temporary_row_payload_sha256"],
        old_source_row_or_radial_integral_recomputed=False)


def params():
    return dict(cutoff_abs_j=97,physical_frequency="4j",physical_root_piece=2549,
        exact_full_physical_cover=str(H),exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],
        exact_root_interval=list(map(str,ROOTS)),original_fold_radius=str(RG),original_fold_phi_strip=str(SG),
        actual_old_phi_strip=str(SP),genuine_inverse_phi_strip=str(SB),inverse_Wiener_phi_strip=str(SW),
        accepted_regular_canonical_radius=str(RT),accepted_regular_canonical_strip=str(SA),
        complete_complex_delta_square_halfwidth="1/100000000",
        complete_complex_z_square_halfwidth="1/9409",fixed_intrinsic_parameter="eta_0",
        input_window="H^(-4/3) both genuine columns and both signs",
        first_source_window="ordinary L2_r H^(-2/3)",independent_mean_window="ordinary L2_r constants",
        density_zero_amplitude="w0",density_one_amplitude="w1=MZ",
        density_zero_word_window="H^(-8/3) -> H^(-5/3)",
        density_one_word_window="H^(-5/3) -> H^(-2/3)",
        actual_directed_matrix_right_gain_provenance=True,original_matrix_radius="1/1000",
        baseline_complete_source_run="43711480764/1",
        original_directed_source_run="43703879926/1",
        original_positive_calibration_run="43702688640/1",
        original_inverse_run="43688459733/1",
        new_factored_transport_angular_orders=[0,1,2,3],
        new_genuine_rank_angular_orders=[0,1,2,3,4],
        output_old_phi_strip="0",common_column_envelope="abs(rho)^(-1/4)",
        old_radial_integrations_recomputed=0,new_radial_integrations_computed=0,
        real_parameter_values_for_final_operator_only=True,arithmetic_bits=320)

def checked_accepted_rows(paths,C,D,B,gate):
    old=read(paths["original_norm_native"]);op=read(paths["original_norm_process"])
    gate("the original 1328 complete coefficient rows retain their successful native and process identities",
        old["complete"] and old["proved"] and old["failure"] is None
        and old["source_sha256"]==OLD_SOURCE and old["input_manifest_sha256"]==OLD_MANIFEST
        and all(v["passed"] for v in old["gates"])
        and op["complete"] and op["actual_returncode"]==0 and op["failure"] is None
        and op["mathematical_complete"] and op["mathematical_failure"] is None
        and op["native_sha256"]==OLD_NATIVE and op["native_bytes"]==4837715
        and op["mathematical_source_sha256"]==OLD_SOURCE and op["manifest_sha256"]==OLD_MANIFEST
        and str(op["run_id"])=="43629465215" and str(op["run_attempt"])=="1"
        and old["root_native_sha256"]==ROOT_SHA and old["first_forcing_native_sha256"]==FORCE_SHA
        and all(v["passed"] for v in op["mathematical_gates"]))
    rows=old["coefficient_rows"]
    if not (len(rows)==1328 and [x["common_row"] for x in rows]==list(range(1328))
        and all(x["interval"][1]==y["interval"][0] for x,y in zip(rows,rows[1:]))
        and [rows[0]["interval"][0],rows[-1]["interval"][1]]==op["exact_cover"]
        and op["exact_root_interval"]==list(map(str,ROOTS))
        and old["exact_real_delta_radius"]==str(Q(1,100000000))
        and old["old_mean_and_all_Fourier_outputs_retained"]):
        raise ValueError("the complete original row cover or real family changed")
    selected,parts=selected_rows(rows)
    original=C["complete_source_conclusion"];current=B["complete_source_conclusion"]
    gate("the identical six physical intersections and saved squared-envelope measure are restored without radial integration",
        len(selected)==C["original_selected_coefficient_rows_read"]==D["original_selected_coefficient_rows_read"]==6
        and parts==C["new_genuine_source_radial_integrals"]==original["temporary_complete_source_row_count"]==6
        and original["total_squared_envelope_radial_weight_upper"]
            ==current["total_squared_envelope_radial_weight_upper"]
            ==D["complete_source_conclusion"]["total_squared_envelope_radial_weight_upper"]
        and original["temporary_complete_source_row_payload_sha256"]==current["original_temporary_row_payload_sha256"]
        and current["actual_dr_measure"] and current["one_sided_uncertain_root_band_retained"])
    # Read the original successful small process, not the 7.8 MB directed native.
    dp=read(paths["directed_process"])
    cases=[v for v in dp["cases"] if Q(v["exact_radius"])==Q(1,1000)]
    if len(cases)!=1:raise ValueError("the complete word case changed")
    case=cases[0];ml,mr=map(Q,case["exact_cover"])
    words=D["actual_original_directed_word_maxima"]
    gate("the three complete words retain both full matrix windows and their entire original radius case",
        dp["complete"] and dp["actual_returncode"]==0 and dp["failure"] is None
        and dp["mathematical_complete"] and dp["mathematical_failure"] is None
        and str(dp["run_id"])=="43632464994" and str(dp["run_attempt"])=="1"
        and dp["mathematical_source_sha256"]=="f3a5d7b0caad97d65464e6b79e0884e3a50085cbc6b2d9bab35e9ab1e8a66b0d"
        and dp["manifest_sha256"]=="29465d2a93165f40f42b2ea73c772374a882475fd59f44fdbce20b37ff4d402f"
        and len(dp["mathematical_gates"])==8 and all(v["passed"] for v in dp["mathematical_gates"])
        and dp["original_completed_norm_native_sha256"]==OLD_NATIVE
        and dp["root_native_sha256"]==ROOT_SHA and dp["first_forcing_native_sha256"]==FORCE_SHA
        and dp["exact_root_interval"]==list(map(str,ROOTS))
        and dp["old_mean_and_all_Fourier_outputs_retained"]
        and case["complete"] and case["complete_original_rows"]==144
        and case["complete_original_matrix_widths"]==["1/16","1/32","1/64"]
        and words==case["complete_case_operator_cost_maxima"]
        and all(ml<=Q(row["interval"][0])<Q(row["interval"][1])<=mr for row in selected)
        and D["mathematical_parameters"]["density_zero_word_window"]=="H^(-8/3) -> H^(-5/3)"
        and D["mathematical_parameters"]["density_one_word_window"]=="H^(-5/3) -> H^(-2/3)"
        and D["scope"]["complete_directed_word_right_gain_reused"]
        and D["scope"]["density_one_conversion_from_complete_matrix_not_isolated_Sobolev"])
    return selected,words

def render(doc):
    lines=["# Actual factored transport and companion complete-source comparison","",
        "Public Actions run "+str(doc.get("run_id"))+"/"+str(doc.get("run_attempt"))+".",
        "Complete: "+str(doc.get("complete"))+"; proved: "+str(doc.get("proved"))+".",
        "Scientific source SHA256: "+doc["source_sha256"]+".",
        "Input manifest SHA256: "+doc["input_manifest_sha256"]+".","",
        "The new calculation bounds the exact factored transport, its genuine rank correction,",
        "the full y/q companions and ten complete source terms. Every original numerical enclosure",
        "and the six-row integrated radial weight are restored. Density 0 uses w0; density 1 uses w1.",
        "All three local terms, the latest complete local aggregate and the other mean terms remain unchanged."]
    for title,key in (("Complete product and regular quotient","complete_domain_conclusion"),
        ("Identified complete inverse remainder","complete_inverse_remainder_conclusion"),
        ("Complete g operators in the two source windows","complete_transport_operator_conclusions")):
        if key in doc:lines+=["","## "+title,"",json.dumps(doc[key],sort_keys=True)]
    if "complete_comparison_conclusions" in doc:
        lines+=["","## Ten whole-term comparisons","",
            "| Term | New complete ordinary L2 bound | Selected complete bound | Strictly smaller |",
            "|---|---|---|---|"]
        for r in doc["complete_comparison_conclusions"]:
            lines.append("| "+r["source_term"]+" | "+r["new_complete_L2_upper"]["ball"]+" | "+
                r["selected_complete_L2_upper"]["ball"]+" | "+str(r["strictly_smaller_complete_term"])+" |")
    if "complete_source_conclusion" in doc:
        con=doc["complete_source_conclusion"]
        lines+=["","## Complete physical source ledger","","| Channel | Ordinary radial L2 upper ball |","|---|---|"]
        for k in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+k+" | "+con[k]["ball"]+" |")
        for title,key in (("All 21 first-output terms","complete_first_source_term_L2_upper"),
            ("All 10 independent physical-mean terms","complete_independent_mean_term_L2_upper")):
            lines+=["","## "+title,"","| Term | Complete ordinary L2 upper ball |","|---|---|"]
            lines+=["| "+k+" | "+v["ball"]+" |" for k,v in con[key].items()]
    lines+=["","## Actual identity and mathematical gates",""]
    lines+=["- "+v["name"]+": "+str(v["passed"])+"." for v in doc["gates"]]
    lines+=["","## Counts and scope","",json.dumps(doc.get("scope",{}),sort_keys=True),
        "","Actual new scalar seconds: "+repr(doc.get("actual_mathematical_wall_seconds"))+".",
        "Failure: "+str(doc.get("failure"))+".",
        "Temporary native SHA256: "+str(doc.get("temporary_native_sha256"))+".",
        "Full derivative and six-row coefficient tables remain temporary.",
        "These volume-source bounds do not prove a physical-to-wave trace, positive graph, full high inverse or strong return.",""]
    return "\n".join(lines)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new mathematical arithmetic requires this public Actions repository")
    ctx.prec=320;ctx.cap=8
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise ValueError("the accepted scientific runtime changed")
    a.out_dir.mkdir(parents=True,exist_ok=True);source=sha(__file__);started=time.monotonic()
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        original_complete_fold_stages_read=0,original_successful_small_receipts_read=0,
        original_complete_coefficient_rows_read=0,original_selected_coefficient_rows_read=0,
        original_positive_linear_coefficients_read=0,original_complete_source_terms_read=0,
        original_complete_word_maxima_read=0,original_complete_word_maxima_consumed=0,
        new_supporting_factor_jet_closures=0,new_complete_regular_quotient_budgets=0,
        new_complete_factored_density_source_budgets=0,new_identified_inverse_remainder_recoveries=0,
        new_complete_companion_row_budgets=0,new_complete_window_evaluations=0,
        new_complete_uniform_comparisons=0,new_complete_scalar_recombinations=0,
        old_numerical_enclosures_recomputed=0,old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed=0,
        old_RF_forcing_amplitude_or_profile_enclosures_recomputed=0,
        old_inverse_word_or_positive_calibration_recomputed=0,old_source_row_or_radial_integral_recomputed=0,
        new_radial_integrals_computed=0,original_natural_stage_bytes_modified=0,
        full_physical_negative_volume_source_paid=False,full_high_inverse_claimed=False,
        reproducible_outputs_published_to_repository=False,reproducible_outputs_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False)
    temporary={}
    def gate(name,condition):
        doc["gates"].append(dict(name=name,passed=bool(condition)))
        if not condition:raise ValueError(name)
    try:
        manifest=read(a.manifest);parameters=params();doc["mathematical_parameters"]=parameters
        gate("the source manifest exact products and new-only scalar scope have their reviewed identities",
            sha(a.manifest)==a.manifest_sha and manifest["public_repository"]==PUBLIC
            and manifest["scientific_source_sha256"]==source and manifest["mathematical_parameters"]==parameters)
        pins={e["path"]:e for e in manifest["files"]}
        if len(pins)!=len(manifest["files"]):raise ValueError("duplicate immutable input")
        for e in manifest["files"]:
            rel=Path(e["path"]);f=a.repo/rel
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):
                raise ValueError("an immutable input left the topic")
            if not f.is_file() or f.stat().st_size!=e["bytes"] or sha(f)!=e["sha256"]:
                raise ValueError("changed exact input "+str(rel))
        if any(v not in pins for v in manifest["input_paths"].values()):raise ValueError("an input role is not pinned")
        paths={k:a.repo/v for k,v in manifest["input_paths"].items()}
        expected=dict(contract=CONTRACT,factor_contract=FACTOR_CONTRACT,
            old_fold_majorants_stage=MAJORANTS,adjacent_process=APROC,adjacent_publication=APUB,
            amplitude_execution=S_EXEC,operator_execution=G_EXEC,complete_genuine_execution=C_EXEC,
            directed_source_execution=D_EXEC,first_local_execution=P_EXEC,
            refined_first_local_execution=B_EXEC,columns_execution=H_EXEC,
            original_norm_native=OLD_NATIVE,original_norm_process=OLD_PROCESS,
            original_scalar_algorithm=S_SOURCE,original_operator_algorithm=G_SOURCE,
            complete_genuine_source=C_SOURCE,directed_source_algorithm=D_SOURCE,
            original_first_local_algorithm=P_SOURCE,refined_first_local_algorithm=B_SOURCE,
            original_inverse_algorithm=H_SOURCE,
            directed_process="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8",
            original_fold_algorithm="410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783")
        gate("all seven accepted scientific receipts and every frozen source and legacy byte identity are exact",
            all(sha(paths[k])==v for k,v in expected.items()))
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        publication=[v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
        if len(publication)!=1:raise ValueError("the original natural fold receipt is not unique")
        mr=publication[0]
        gate("the complete fold and physical background retain their exact legacy payload and successful publication",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
            and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==runtime
            and mr["bytes"]==4501 and mr["sha256"]==MAJORANTS
            and ap["actual_returncode"]==0 and ap["mathematical_complete"] and ap["mathematical_proved"]
            and ap["mathematical_failure"] is None and au["complete"]
            and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi")))
        old=unpack(ms["payload"]);fold=old["fold"];coefficient=old["coefficients"]
        doc["original_complete_fold_stages_read"]=1
        S=receipt(paths["amplitude_execution"],"43698106023",S_SOURCE,S_MANIFEST,gate)
        G=receipt(paths["operator_execution"],"43700281022",G_SOURCE,G_MANIFEST,gate)
        C=receipt(paths["complete_genuine_execution"],"43702688640",C_SOURCE,C_MANIFEST,gate)
        D=receipt(paths["directed_source_execution"],"43703879926",D_SOURCE,D_MANIFEST,gate)
        P=receipt(paths["first_local_execution"],"43709396175",P_SOURCE,P_MANIFEST,gate)
        B=receipt(paths["refined_first_local_execution"],"43711480764",B_SOURCE,B_MANIFEST,gate)
        Hr=receipt(paths["columns_execution"],"43688459733",H_SOURCE,H_MANIFEST,gate)
        doc["original_successful_small_receipts_read"]=7
        sd=S["complete_domain_conclusion"];family=C["scope"];base=B["complete_source_conclusion"]
        gate("the full original complex squares fixed intrinsic root genuine signs and physical mean are unchanged",
            sd["exact_original_physical_piece_interval"]==list(map(str,PIECE))
            and sd["exact_original_true_root_interval"]==list(map(str,ROOTS))
            and Q(sd["true_physical_root_piece_radius"])==H
            and sd["same_potential_T_segment_proved"] and sd["actual_inverseimage_and_both_regular_paths_proved"]
            and S["scope"]["original_root_piece_2549_only"] and S["scope"]["full_complex_delta_square"]
            and S["scope"]["full_z_square_all_abs_j_ge97"] and S["scope"]["both_carrier_signs"]
            and family["original_fixed_intrinsic_parameter"]=="eta_0"
            and family["same_original_real_explicit_family"]
            and family["both_genuine_columns_and_both_carrier_signs"] and family["all_input_abs_j_at_least97"]
            and family["output_mean_and_complete_original_primitive_retained"]
            and family["physical_J_only_on_its_proved_reflected_parity_domain"]
            and [len(r["gates"]) for r in (S,G,C,D,P,B,Hr)]==[26,16,17,12,13,19,16]
            and C["full_physical_negative_volume_source_paid"] and not C["full_high_inverse_claimed"])
        stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
            "both_density_windows_retained","outer_J_window","input_window","first_output_window",
            "independent_even_mean_window","total_squared_envelope_radial_weight_upper",
            "nonlocal_total_L2_upper","mean_L2_upper","complete_independent_mean_term_L2_upper")
        ledgers=[r["complete_source_conclusion"] for r in (D,P,B)]
        gate("the latest refined local ledger is retained with all original nonlocal terms and source windows",
            len(base["complete_first_source_term_L2_upper"])==21
            and len(base["complete_independent_mean_term_L2_upper"])==10
            and all(ledgers[0][k]==ledgers[1][k]==ledgers[2][k] for k in stable)
            and all(v==base["complete_first_source_term_L2_upper"][k]
                ==ledgers[1]["complete_first_source_term_L2_upper"][k]
                for k,v in ledgers[0]["complete_first_source_term_L2_upper"].items() if k!="local_raw_1")
            and base["old_nine_word_and_five_physical_mean_counts"]==[9,5]
            and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and base["only_complete_first_local_vector_replaced"]
            and B["new_complete_wrr_derivative_bounds"]==6
            and B["old_numerical_enclosures_recomputed"]==0)
        # Bind the claimed domain to the exact frozen producer statements. This
        # is textual provenance checking, not reevaluation of their arithmetic.
        ps=paths["original_first_local_algorithm"].read_text()
        fs=paths["original_fold_algorithm"].read_text()
        bs=paths["refined_first_local_algorithm"].read_text()
        gate("the saved T image uses the whole SG fold modulus and M Bi B2 share the accepted canonical inverse product",
            'imageT=up(ex(H)*powr(Ap,Q(2,3)))' in ps
            and 'Ap=bound(f["Ap"],"old A modulus")' in ps
            and 'exact_canonical_radius=str(LAM*R/2),exact_canonical_width=str(SF)' in fs
            and 'SG=Q(3,128);SF=Q(1,64)' in fs and 'LAM=Q(9,2)' in fs
            and 'M=bound(f["M"],"complete canonical leading coefficient")' in bs
            and 'Bi=bound(f["Bi"],"complete inverse leading branch")' in bs
            and RT<Q(9,4)*RG and SA<SB
            and rb(B["complete_domain_conclusion"]["complete_domain_gaps"]["original_inverse_radius"]).lower()>0
            and old["majorants"]["A"][1:]==[str(RG),str(SG)])
        rows,words=checked_accepted_rows(paths,C,D,B,gate)
        doc.update(original_complete_coefficient_rows_read=1328,original_selected_coefficient_rows_read=6,
            original_complete_word_maxima_read=8,original_complete_word_maxima_consumed=3,
            original_complete_source_terms_read=31)
        positive=read_positive_coefficients(C,gate);A=PositiveOperator(positive)
        doc["original_positive_linear_coefficients_read"]=18
        jets=read_real_jets(S,G,gate)
        factors,domain=supporting_coefficients(fold,coefficient,P,B,S,gate)
        doc.update(new_supporting_factor_jet_closures=1,new_complete_regular_quotient_budgets=1,
            complete_domain_conclusion=domain)
        sources,factor_temp=complete_factored_sources(factors,jets,Hr,gate)
        doc["new_complete_factored_density_source_budgets"]=2
        delta,remainder=inverse_remainder(Hr,G,gate)
        doc.update(new_identified_inverse_remainder_recoveries=1,complete_inverse_remainder_conclusion=remainder)
        terms,means,comparisons,operators,row_temp=complete_companion_comparisons(
            rows,sources,A,delta,words,base["total_squared_envelope_radial_weight_upper"],base,gate)
        doc.update(new_complete_companion_row_budgets=12,new_complete_window_evaluations=26,
            new_complete_uniform_comparisons=10,complete_comparison_conclusions=comparisons,
            complete_transport_operator_conclusions=operators)
        result=combine(base,terms,means)
        doc.update(new_complete_scalar_recombinations=4,complete_source_conclusion=result,
            strictly_smaller_complete_term_bounds=sum(int(v["strictly_smaller_complete_term"]) for v in comparisons))
        gate("only the ten declared whole terms may change and the thirteen other first terms eight other means and full local aggregate remain verbatim",
            result["local_L2_upper"]==base["local_L2_upper"]
            and all(result["complete_first_source_term_L2_upper"]["local_raw_"+str(i)]
                ==base["complete_first_source_term_L2_upper"]["local_raw_"+str(i)] for i in (1,2,3))
            and sum(k not in {v["source_term"] for v in comparisons} for k in terms)==13
            and sum(k not in {v["source_term"] for v in comparisons} for k in means)==8
            and len(row_temp)==6 and len(comparisons)==10
            and result["total_squared_envelope_radial_weight_upper"]==base["total_squared_envelope_radial_weight_upper"]
            and result["original_temporary_row_payload_sha256"]==base["original_temporary_row_payload_sha256"])
        gate("the complete new negative volume source is finite with both density windows true dr and independent physical mean",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["both_density_windows_retained"] and result["outer_J_window"]==base["outer_J_window"])
        doc["scope"]=dict(original_physical_root_piece_2549_only=True,original_fixed_intrinsic_parameter="eta_0",
            same_original_real_explicit_family=True,full_complex_delta_and_z_squares_in_supporting_bounds=True,
            final_operators_restrict_to_original_real_parameters=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            negative_side_only=True,density_zero_amplitude="w0",density_one_amplitude="w1=MZ",
            exact_signed_factorization_before_absolute_bounds=True,
            exact_regular_B_root_condition_and_all_sT_paths_retained=True,
            complete_genuine_rank_and_exact_input_n_minus_two_retained=True,
            q_is_v_Dw_minus_angle_derivative_of_vp_not_D_of_vw=True,
            all_old_h_amplitude_source_terms_retained_verbatim=True,
            full_G_radial_scalar_and_all_amplitude_means_retained=True,
            output_mean_and_complete_original_primitive_retained=True,
            both_complete_directed_word_windows_retained=True,
            no_duplicate_inner_word_or_physical_mean_factors=True,
            physical_J_only_on_its_proved_reflected_parity_domain=True,
            latest_refined_first_local_result_and_all_local_terms_retained=True,
            inverse_remainder_read_from_identified_frozen_minimum_branch=True,
            new_supporting_factor_jets_distinct_from_original_ordered_closure=True,
            all_actual_physical_seams_and_reference_matching_sources_retained=True,
            original_positive_graph_and_outer_source_ports_retained=True,
            original_eighteen_positive_coefficients_only_read=True,
            original_source_rows_and_all_radial_integrals_only_read=True,
            complete_row_and_derivative_arrays_published=False,
            physical_to_wave_readout_paid=False,full_negative_BVP_inverse_paid=False,
            positive_growing_column_operator_paid=False,cutoff97_strong_return_contraction_paid=False)
        temporary.update(factored_supporting_data=factor_temp,complete_companion_rows=row_temp,
            accepted_positive_coefficients_payload_sha256=payload_sha(C["complete_positive_linear_operator_conclusion"]))
        doc["temporary_complete_companion_row_payload_sha256"]=payload_sha(row_temp)
        doc["temporary_complete_companion_row_count"]=len(row_temp)
        doc["full_physical_negative_volume_source_paid"]=True
        doc.update(complete=True,proved=True,actual_returncode=0)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,complete_conclusions=doc)
        native=a.out_dir/"temporary-factored-transport-companion-sources.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            text=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(text.encode())>60000:raise ValueError("small conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(text)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in ("complete_domain_conclusion",
                "complete_inverse_remainder_conclusion","complete_transport_operator_conclusions",
                "complete_comparison_conclusions","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual factored-source formatting failure\n\n"
                "The original scientific child code was "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_comparisons=doc["new_complete_uniform_comparisons"],
            old_numerical_enclosures_recomputed=0,new_radial_integrals_computed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
