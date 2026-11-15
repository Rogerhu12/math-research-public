#!/usr/bin/env python3
"""New genuine positive Ai cutoff and complete strong correction scalar budget.

Only the new PC positive functional, positive row products/integrals,
full-frequency cutoff/head sums and correction composition are evaluated.
Every old target, intrinsic/fold/transport/Taylor/profile/matrix/integral is
read from immutable successful output. No old scientific module is imported.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_genuine_positive_Ai_cutoff_and_strong_correction_v1"
CONTRACT="5368abae4c66f73800c16d5f2b906ddaa0f1d62d07e9bd9a3ca539061bdf5d68"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
H=Q(893368603925465506687,21990232555520000000000000)
RG=Q(3,8000);SG=Q(3,128);SB=Q(1,64);RS=Q(1,8000);SS=Q(3,512)
SIGMA=Q(1,512);SP=Q(1,256);L=Q(1,2000);N=388;J0=97
S0=Q(2,10**6);S1=Q(3,10**6);DERIVATIVE_CUTOFF=Q(15*10**6,8)
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
OLD_NATIVE="7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c"
OLD_SOURCE="56b68983f36bb3d88e1427081ba9e60a8f6cf43dcd9578a0d925e1834292555d"
OLD_MANIFEST="7290cbb07293c15a239ffafb0e342e6c1b7ea812106f569e88bbe4d2502180df"
DIRECT_NATIVE="3c8c4f3c93108de5a1c17149518f3aa16500a7f8ad58343f7a8dac325cc48d4b"
DIRECT_SOURCE="f3a5d7b0caad97d65464e6b79e0884e3a50085cbc6b2d9bab35e9ab1e8a66b0d"
DIRECT_MANIFEST="29465d2a93165f40f42b2ea73c772374a882475fd59f44fdbce20b37ff4d402f"
BRANCHES=("central","positive_characteristic","negative_characteristic")
EXPECTED={
    "columns_execution": [
        "43688459733",
        "9596ebee08e95939cf1b8a9d46a9f32053bd4706cc77e2263a80d09ede99294c",
        "1869212f28702ae915787a6b5189406b13e6824b93e436a8650fa83e86b11f99",
        "fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57",
        16
    ],
    "potential_execution": [
        "43685624307",
        "042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7",
        "44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437",
        "d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9",
        16
    ],
    "accepted_ER_execution": [
        "43724065270",
        "5e1e33549c1495f5d65a68ce3755367eb4ddbd232ffd0b5e5b6923514980b652",
        "6b47f4a62c9d2cdcb6ed7b539c89816d142bc998c140e40002c205fe24cc0df6",
        "dedbfcad60efd024fddab17ca948ab5720c24e34a48dcde7e25af7a0aea641fc",
        20
    ],
    "accepted_RV_execution": [
        "43719681982",
        "d59893af66b8829d924d75686fb0ecd6e6d25f9b72b70a0fac6564c4e96fdf60",
        "4718b4b818ec5d72537aa3a93e5825747a586ece87a086c7578ec6ec4c3b9ded",
        "0781239c0753785d2b196b77cc90c0eb343d52cc73226d84d7f8f6bb23136473",
        27
    ],
    "accepted_M_execution": [
        "43721735003",
        "b4bc768e149f01591102a9bcc8c16b166bd8ba97fd0c0c245ba3073ba3382496",
        "1055c8231c7646acb5b37e7c876a62321436192927ba9616ad7a1d08a24cb1e2",
        "b858853023fd93bfefbac5f8e18471c93c88d90c051999bcf35dd9bc0df8aa4e",
        23
    ],
    "accepted_SV_execution": [
        "43722805762",
        "44021afbf608638e7e08f584a5574acdc76738c5985d72ca0f2b036c8f7d2dc0",
        "5306e66c5102e358caba5946b3c651dda11fb98a18848f8fe27f779f775d73cf",
        "ba96a4832017144ea3ccd59902e8bcb8f1b0acd1c722edadc44b763dfac6c0d0",
        23
    ],
    "accepted_HP_execution": [
        "43726426053",
        "bacbc58b43d7b5463996377802ff700a6ff1abf9dc23dce835541ef934f6a6e6",
        "12f93b005f06a5df4342e25cf814b8eed39571e36594401d3194a6a08a37e5cd",
        "01d9990041478c1a81a6413909d388038af43395578054fd71be2e83a4f8b036",
        25
    ],
    "accepted_BG_execution": [
        "43726985545",
        "f3f3737931bfa528f57a8f23c0c00043c6027b7ec0d2157ec2a05fb2985d27e4",
        "77fd42dd62ba5007cca008e8c868f61d7ed317176f0290818aae091f4e1c62b1",
        "7736f33c74ccfc84cd8d00108f8035d6cc5d3f16cd9878f885a17481b8d17927",
        24
    ],
    "refined_first_local_execution": [
        "43711480764",
        "e0541949f521e0852bb4a8b204b51281f7d83e0ed2a7a1afbb259ca73362e92a",
        "5e2618c446288cd8d84fcbf4bb7955f56f7a1041f823e05213d043d20b5aeaaf",
        "20422f41645c2a4544bb8a0d79eddf771b45ff0386cc81b3ee97a32849586ef2",
        19
    ],
    "accepted_DG_execution": [
        "43720766795",
        "7d28ab5f16bfec72faf898118781a5df0af9bc610e80d11bc9d67b8e0527e594",
        "cbb0f2acedd715220fc90b43bacd3dd571092b7dacd2da0cc4c554160fffe833",
        "48ca7d65c1abd9575c7be6e4e8ae4594cb6f4e1cf3d415cf119e2f2de3ebe425",
        27
    ],
    "complete_genuine_execution": [
        "43702688640",
        "b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0",
        "8465759dfe9101bb7e20275cec1a5b98e23efb4dbe643e492fb8189250b005b9",
        "bca0f97d7c610f8f2572e61d1e1442a8b9c256a4c5429253682b6d803e3a21c3",
        17
    ],
    "accepted_RJ_execution": [
        "43728317408",
        "c1ed2857915498a4f301f3ad3bd6caaeea99232b97e0b1e7f87d08e89beb23a8",
        "e0a36c82ed4f2a7aa0ea9bbbcccee8ab3aee06ccbc78ed113a08e9f353eb93d8",
        "042031e1e0baaa53ef062d87918c7ede09eb1f6b4c12bc1d4e4a2ee19ad6a084",
        27
    ],
    "accepted_PW_execution": [
        "43734233535",
        "268e033e3973ba60eb01b6b45842221f5d480cbe584de541731a4e34e5632e3c",
        "8c3d9c450f571541295754b21667f02b964c26b3ceca918765b3d77b9ec07133",
        "f17516d3083cd2782866c2163635a3a89efe9479ced8f57eefb2bf63e3f92e90",
        21
    ]
}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def payload_sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def save(p,x,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    b=gzip.compress(raw,mtime=0) if compressed else raw
    t=p.with_name(p.name+".tmp");t.write_bytes(b);t.replace(p)
def ex(x):
    x=Q(x);return arb(x.numerator)/arb(x.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    return arb(v["ball"])
def upper(v,label="positive budget"):
    a=rb(v)
    if not a.is_finite() or a.lower()<0:raise ValueError("invalid nonnegative "+label)
    return a.upper()
def up(v):return upper(v)
def gap(v,label):
    a=rb(v).lower()
    if not a.is_finite() or not a>0:raise ValueError("unproved strict positive gap: "+label)
    return a
def pw(x,p):return (rb(x).log()*ex(p)).exp()
def rec(x):return dict(ball=rb(x).str(52))
def encode(x):
    if isinstance(x,arb):return rec(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def unpack(x):
    if isinstance(x,dict):
        if set(x)=={"ball"}:return rb(x)
        return {k:unpack(v) for k,v in x.items()}
    if isinstance(x,list):return [unpack(v) for v in x]
    return x
def add(*vs,k):
    if min(map(len,vs))<=k:raise ValueError("missing full angular derivative in sum")
    return [up(sum((v[i] for v in vs),arb(0))) for i in range(k+1)]
def mul(a,b,k):
    if min(len(a),len(b))<=k:raise ValueError("missing full angular derivative in product")
    return [up(sum((math.comb(j,l)*a[l]*b[j-l] for l in range(j+1)),arb(0))) for j in range(k+1)]
def scale(a,b):return [up(v*rb(b)) for v in a]
def vmul(a,v,k):return [mul(a,v[i],k) for i in range(2)]
def vscale(v,b):return [scale(a,b) for a in v]
def vadd(*vs,k):return [add(*(v[i] for v in vs),k=k) for i in range(2)]
def vder(v):return [a[1:] for a in v]
def vector(x,k):
    if len(x)!=2 or any(len(a)!=k+1 for a in x):raise ValueError("saved vector orders changed")
    return [[upper(v) for v in a] for a in x]
def accepted(path,identity,gate):
    run,source,manifest,digest,ngates=identity
    e=read(path);r=e.get("actual_scientific_receipt",{})
    # PW used only Python/flint; bind that exact recorded runtime to its exact successful source.
    recorded_runtime=({"python":"3.12.14","python_flint":"0.9.0"}
        if (run,source)==("43734233535","268e033e3973ba60eb01b6b45842221f5d480cbe584de541731a4e34e5632e3c")
        else RUNTIME)
    gate("accepted complete run "+run+"/1 retains its full immutable success",
        sha(path)==digest and str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("source_sha256")==source and r.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("runtime")==recorded_runtime
        and len(r.get("gates",[]))==ngates and all(g.get("passed") is True for g in r["gates"]))
    return r

def params():
    return dict(cutoff_abs_j=J0,physical_frequency="n=4|j|",physical_root_piece=2549,
        exact_root_interval=list(map(str,ROOTS)),exact_physical_piece_interval=list(map(str,PIECE)),
        exact_real_delta_radius="1/100000000",fixed_intrinsic_parameter="eta_0",
        exact_transition_s_interval=[str(S0),str(S1)],exact_cutoff_derivative_upper=str(DERIVATIVE_CUTOFF),
        exact_original_fold_radius=str(RG),exact_original_fold_strip=str(SG),
        exact_original_inverse_strip=str(SB),exact_new_p_strip=str(SP),exact_new_shift=str(SIGMA),
        exact_original_genuine_amplitude_radius=str(RS),exact_original_genuine_amplitude_strip=str(SS),
        common_potential_radius_case="1/6000",exact_reference_terminal_T=str(L),
        both_carrier_signs=True,real_parameter_values_before_contour=True,
        input_window="H^(-4/3), physical |j|>=97",
        positive_source_window="ordinary L2_dr H^(-2/3) plus independent constant row",
        correction_output_window="old-circle primitive density L2 pair plus both full means",
        old_directed_run="43632464994/1",old_directed_artifact_id=14128707026,
        arithmetic_bits=320)

def read_original_fold(paths,gate):
    ms=read(paths["old_fold_majorants_stage"]);p=read(paths["adjacent_process"]);u=read(paths["adjacent_publication"])
    entries=[e for e in u["files"] if e["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
    gate("the original complete fold coefficient and leading product are restored exactly without producer calls",
        sha(paths["old_fold_majorants_stage"])==MAJORANTS and sha(paths["adjacent_process"])==APROC
        and sha(paths["adjacent_publication"])==APUB and len(entries)==1
        and entries[0]["bytes"]==4501 and entries[0]["sha256"]==MAJORANTS
        and ms["complete"] and ms["stage"]==ms["name"]=="complete-original-reference-holomorphic-majorants"
        and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
        and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==RUNTIME
        and p["actual_returncode"]==0 and p["mathematical_complete"] and p["mathematical_proved"]
        and p["mathematical_failure"] is None and u["complete"]
        and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi","a0","b0")))
    return unpack(ms["payload"])

def read_original_rows(paths,gate):
    old=read(paths["original_norm_native"]);op=read(paths["original_norm_process"])
    directed=read(paths["directed_native"]);dp=read(paths["directed_process"])
    gate("all1328 old norm rows retain their complete zero-return provenance and full real delta cover",
        sha(paths["original_norm_native"])==OLD_NATIVE
        and old["complete"] and old["proved"] and old["failure"] is None
        and old["source_sha256"]==OLD_SOURCE and old["input_manifest_sha256"]==OLD_MANIFEST
        and all(g["passed"] for g in old["gates"])
        and op["complete"] and op["actual_returncode"]==0 and op["failure"] is None
        and op["mathematical_complete"] and op["mathematical_failure"] is None
        and op["native_sha256"]==OLD_NATIVE and op["native_bytes"]==4837715
        and op["mathematical_source_sha256"]==OLD_SOURCE and op["manifest_sha256"]==OLD_MANIFEST
        and str(op["run_id"])=="43629465215" and str(op["run_attempt"])=="1"
        and all(g["passed"] for g in op["mathematical_gates"])
        and op["exact_root_interval"]==list(map(str,ROOTS))
        and old["exact_real_delta_radius"]==op["exact_real_delta_radius"]=="1/100000000"
        and old["old_mean_and_all_Fourier_outputs_retained"] is True)
    gate("the original directed native and its temporary archive member have immutable full-matrix success",
        sha(paths["directed_native"])==DIRECT_NATIVE
        and directed["complete"] and directed["proved"] and directed["failure"] is None
        and directed["source_sha256"]==DIRECT_SOURCE and directed["input_manifest_sha256"]==DIRECT_MANIFEST
        and all(g["passed"] for g in directed["gates"])
        and dp["complete"] and dp["actual_returncode"]==0 and dp["failure"] is None
        and dp["mathematical_complete"] and dp["mathematical_failure"] is None
        and dp["native_sha256"]==DIRECT_NATIVE and dp["native_bytes"]==7873296
        and dp["mathematical_source_sha256"]==DIRECT_SOURCE and dp["manifest_sha256"]==DIRECT_MANIFEST
        and str(dp["run_id"])=="43632464994" and str(dp["run_attempt"])=="1"
        and len(dp["mathematical_gates"])==8 and all(g["passed"] for g in dp["mathematical_gates"])
        and dp["exact_root_interval"]==list(map(str,ROOTS))
        and dp["exact_real_delta_radius"]=="1/100000000"
        and dp["old_mean_and_all_Fourier_outputs_retained"] is True
        and dp["original_completed_norm_native_sha256"]==OLD_NATIVE)
    rows=old["coefficient_rows"];dr=directed["coefficient_rows"]
    gate("old ordinary and directed1328 rows share the same complete common intervals and both-sided root piece",
        len(rows)==len(dr)==1328
        and [r["common_row"] for r in rows]==[r["common_row"] for r in dr]==list(range(1328))
        and all(x["interval"][1]==y["interval"][0] for x,y in zip(rows,rows[1:]))
        and all((x["common_row"],x["interval"],x["original_root_row"])==
                (y["common_row"],y["interval"],y["original_root_row"]) for x,y in zip(rows,dr))
        and [rows[0]["interval"][0],rows[-1]["interval"][1]]==op["exact_cover"]==dp["exact_cover"])
    selected=[];cursor=ROOTS[0];right=ROOTS[1]+S1
    for row,drow in zip(rows,dr):
        lo,hi=map(Q,row["interval"]);a=max(lo,ROOTS[0]);b=min(hi,right)
        if not a<b:continue
        if a!=cursor:raise ValueError("the new positive union has a gap")
        cuts=sorted(set([a,b]+[r for r in ROOTS if a<r<b]))
        selected.extend((row,drow,l,r) for l,r in zip(cuts,cuts[1:]))
        cursor=b
    gate("the complete new positive union including uncertain-root band is covered inside the same physical piece",
        bool(selected) and selected[0][2]==ROOTS[0] and cursor==right
        and PIECE[0]<ROOTS[0]<ROOTS[1]<right<PIECE[1]
        and all(x[3]==y[2] for x,y in zip(selected,selected[1:])))
    return selected,op,dp

def common_domain(original,R,gate):
    f=original["fold"];c=original["coefficients"];maj=original["majorants"]
    rv=R["accepted_RV_execution"]["complete_domain_conclusion"]
    sv=R["accepted_SV_execution"]["complete_exact_inverse_column_conclusion"]
    hp=R["accepted_HP_execution"]["complete_normalized_p_zero_conclusion"]
    dg=R["accepted_DG_execution"]["complete_genuine_derivative_conclusion"]
    gd=R["accepted_DG_execution"]["complete_direct_physical_transport_conclusion"]
    ref=R["refined_first_local_execution"]["complete_domain_conclusion"]
    hi=R["columns_execution"]["old_circle_inverse"]
    cases=[x for x in R["potential_execution"]["cases"] if x["exact_complex_radial_radius"]=="1/6000"]
    if len(cases)!=1:raise ValueError("the same common potential case is not unique")
    pc=cases[0];h=Q(rv["exact_negative_rho_cover"])
    gate("all reused amplitudes and inverse columns have the same two-sided signed disk and full mean qualification",
        S1+ROOTS[1]-ROOTS[0]<h<H<RS<RG
        and Q(sv["exact_negative_rho_cover"])==Q(hp["exact_negative_rho_cover"])==Q(dg["exact_negative_rho_cover"])==h
        and Q(gd["exact_negative_rho_cover"])==h
        and Q(hi["exact_full_physical_root_cover"])==H
        and Q(hi["exact_old_rho_radius"])>h and Q(hi["exact_inverse_phi_strip"])==SB
        and hi["full_mean_output_retained"] and sv["same_full_complex_delta_and_old_angle_domains_retained"]
        and hp["same_full_SG_zero_order_moduli_and_SB_inverse_used"]
        and gd["full_amplitude_means_and_signed_carriers_retained"]
        and dg["full_zero_mode_and_both_carriers_retained"]
        and Q(ref["exact_new_old_rho_radius"])==RS and Q(ref["exact_new_old_phi_strip"])==SS
        and ref["all_sT_paths_in_same_paid_domain"] and ref["root_normalization_and_all_means_unchanged"]
        and len(c["D"])>=3 and all(maj[k][1:]==[str(RG),str(SG)] for k in ("a0","b0")))
    Am=gap(f["Am"],"same full fold real A");Ap=up(f["Ap"])
    Th=up(rv["new_complete_negative_T_image_upper"])
    image=gap(pc["reference_image"]["complete_image_disk_radius_lower"],"same common V image")
    Tmin=ex(S0)*pw(Am,Q(2,3));Tmax=up(ex(S1)*pw(Ap,Q(2,3)))
    Y0=up(sv["complete_Y_angular_derivative_upper"][0]);j=up(sv["complete_x_minus_one_upper"])
    M0=up(pc["complete_modulus_upper"]["V"]);M1=up(pc["complete_modulus_upper"]["V_T"])
    ca=up(R["columns_execution"]["reference_columns"]["complete_positive_Ai_weighted_height_and_derivative_factor"])
    inv=up(hi["complete_inverse_HV_angular_derivative_bounds"][0])
    gate("the actual positive transition and every shifted T-image stay in the original terminal and potential products",
        pc["complete"] and pc["proved"] and pc["failure"] is None
        and pc["exact_complex_delta_square_halfwidth"]=="1/100000000"
        and pc["exact_complex_z_square_halfwidth"]=="1/9409" and pc["both_carrier_signs_retained"]
        and pc["whole_complex_bilinear_family"] and pc["fixed_intrinsic_parameter"]=="eta_0"
        and Tmin>0 and Tmin<Tmax and Tmax<ex(L) and Th<image and Th<ex(L)
        and Q(pc["reference_image"]["old_fold_original_radius"])==RG
        and Q(pc["reference_image"]["old_fold_phi_width"])==SG
        and 0<SIGMA<SP<min(SB,SS,SG)
        and Q(hi["exact_old_rho_radius"])>h
        and gap(hi["complete_deformed_determinant_modulus_lower"],"complete genuine inverse")>0)
    m=gap(1-j,"true real Xphi minimum")
    X=list(map(up,sv["complete_X_angular_derivative_upper"]))
    Z=list(map(up,sv["complete_zeta_angular_derivative_upper"]))
    Y=list(map(up,sv["complete_Y_angular_derivative_upper"]))
    if not (len(X)==len(Y)==4 and len(Z)==3):raise ValueError("saved full profile jets changed order")
    f2=X[1];f3=X[2];mup=X[0]
    p2=f2/m**3;p3=f3/m**4+3*f2*f2/m**5
    c0=1/m.sqrt()
    c2=(mup*(m**-2+2*p2*p2+m**-4+p3*p3+ex(Q(9,2))*p2*p2/m**2+m**-6)).sqrt()
    CX=up(pw(c0,Q(1,6))*pw(c2,Q(5,6)))
    Ast=up(max(arb(1),Th+M0/(N*N)))
    ch=gap(ex(SIGMA)*(1-j-Ast*Y0),"actual contour exponent")
    out=dict(h=h,Am=Am,Ap=Ap,Th=Th,Tmin=gap(Tmin,"strict positive transition T"),Tmax=Tmax,
        potential_image=image,V=M0,VT=M1,CA=ca,m=m,M=mup,F2=f2,F3=f3,CX=CX,
        Z0=Z[0],Z1=up(Z[1]+Z[0]*Z[0]),Y0=Y[0],Y1=Y[1],
        j=j,contour_A=Ast,contour_c=ch,inverse_HV=inv,
        whole_Q=up(f["Q"]),whole_D=up(c["D"][0]),whole_leading_modulus=up(maj["a0"][0])+up(maj["b0"][0]),
        whole_genuine_modulus=up(ref["complete_new_amplitude_modulus"]["a1"])+up(ref["complete_new_amplitude_modulus"]["b1"]))
    summary=encode({k:v for k,v in out.items() if k not in ("whole_leading_modulus","whole_genuine_modulus")})
    summary.update(exact_reused_signed_radius=str(h),exact_new_positive_union=[str(ROOTS[0]),str(ROOTS[1]+S1)],
        exact_new_shift=str(SIGMA),exact_p_strip=str(SP),exact_transition=[str(S0),str(S1)],
        same_complete_terminal_solution_and_root_shear=True,
        complex_delta_not_promoted_to_real_phase=True,all_six_required_holomorphic_domains_checked=True,
        DG_full_disk_g_used_not_RJ_negative_six_row_max=True)
    return out,summary

def positive_functional(domain,C,ER,RV,gate):
    """PC10--19: one new positive profile; no old profile evaluation."""
    d=domain;M=d["V"];MT=d["VT"];z=d["Z0"];zz=d["Z1"];y=d["Y0"];yy=d["Y1"]
    def S(p):
        p=Q(p)
        return arb(1) if p==0 else up(pw(ex(p)/arb(1).exp(),2*p/3))
    a=[S(Q(1,4)),up(z*(S(Q(5,4))+S(Q(7,4)))),
       up(z*z*S(Q(13,4))+M*y*y*S(Q(1,4))+zz*(S(Q(5,4))+S(Q(7,4))))]
    ninv=pw(ex(N),Q(-1,3))
    b2_scaled=up(z*z*(S(Q(9,4))+S(Q(13,4))+S(Q(15,4)))+
        zz*S(Q(9,4))+M*y*y*(S(Q(1,4))+S(Q(3,4))))
    b=[up(ninv*(S(Q(1,4))+S(Q(3,4)))),
       up(ninv*z*S(Q(9,4))+M*y*S(Q(1,4))/N),
       up(ninv*b2_scaled+(MT*y*y+M*yy)*S(Q(1,4))/N)]
    radial=up(d["CA"]*pw(d["Am"],Q(-1,6)))
    n1=up(pw(arb(2),Q(5,3))*pw(ex(1+N*N),Q(-1,6)))
    n2=up(8*(pw(ex(J0),Q(-4,3))+3*pw(ex(J0),Q(-1,3))).sqrt())
    def functional(v):
        if len(v)!=2 or any(len(x)<3 for x in v):raise ValueError("positive column requires complete six jets")
        ds=[up(radial*sum((math.comb(k,l)*(a[l]*v[0][k-l]+b[l]*v[1][k-l])
                           for l in range(k+1)),arb(0))) for k in range(3)]
        transformed=up(ds[2]/d["m"]**2+ds[1]*d["F2"]/d["m"]**3)
        return up(d["CX"]*(n1*(ds[0]+arb.pi()**2*transformed/48)+n2*transformed))
    kapp=[]
    for i in range(6):
        basis=[[arb(0) for _ in range(3)] for _ in range(2)];basis[i//3][i%3]=arb(1)
        kapp.append(functional(basis))
    old=C["complete_positive_linear_operator_conclusion"]
    gate("the old eighteen positive coefficient parameters retain their full three-branch budget identity",
        len(old)==3 and tuple(x["branch"] for x in old)==BRANCHES
        and all(x["exact_input_component_order"]==["a","a_phi","a_phiphi","b","b_phi","b_phiphi"]
                and len(x["complete_positive_linear_coefficients"])==6 for x in old))
    lowers=[gap(sum((rb(x["complete_positive_linear_coefficients"][i]).lower() for x in old),arb(0)),
                "same old algorithm coefficient "+str(i)) for i in range(6)]
    ratios=[up(a/b) for a,b in zip(kapp,lowers)];qplus=max(ratios).upper()
    lc=C["complete_local_vector_conclusion"]
    oldlocals=[ER["complete_local_operator_conclusion"]["complete_first_local_raw_operator_upper"],
        RV["complete_local_operator_conclusion"]["new_complete_raw_local_operator_upper"][1],
        lc["raw_complete_operator_coefficients"][2]]
    local=[up(qplus*up(v)) for v in oldlocals]
    L2=vector(RV["complete_local_operator_conclusion"]["complete_new_raw_local_angular_derivative_upper"]["L2"],2)
    direct2=functional(L2);local[1]=min(local[1],direct2).upper()
    gate("all new positive profiles coefficients and complete local conversions are finite without clipping or upper subtraction",
        all(x.is_finite() and x.lower()>=0 for x in a+b+kapp+ratios+local)
        and qplus>0 and len(ER["complete_local_operator_conclusion"]["accepted_seven_complete_M_non_E_summands"])==7
        and lc["exact_input_weights"]==["1","1/388","1/150544"]
        and RV["complete_local_operator_conclusion"]["second_vector_only_b1_r_b1_phi_and_full_rank"]
        and RV["complete_local_operator_conclusion"]["exact_input_weights"]==["1","1/388"])
    conclusion=dict(profile_a=encode(a),profile_b=encode(b),complete_positive_coefficients=encode(kapp),
        old_algorithm_parameter_lower=encode(lowers),conversion_ratios=encode(ratios),
        maximum_complete_conversion_ratio=rec(qplus),conversion_not_clipped_to_one=True,
        direct_read_RV_second_vector_candidate=rec(direct2),
        complete_positive_local_raw_upper=encode(local),exact_input_weights=["1","1/388","1/150544"],
        old_profiles_or_positive_coefficients_recomputed=False,old_operator_upper_subtracted=False)
    return functional,local,conclusion

def saved_columns(R,gate):
    """Only exact successful whole-disk outputs; no old derivative or tail calls."""
    sv=R["accepted_SV_execution"]["complete_exact_inverse_column_conclusion"]
    hp=R["accepted_HP_execution"]["complete_normalized_p_zero_conclusion"]
    bg=R["accepted_BG_execution"]["complete_normalized_g_zero_conclusion"]
    dg=R["accepted_DG_execution"]["complete_genuine_derivative_conclusion"]
    dt=R["accepted_DG_execution"]["complete_direct_physical_transport_conclusion"]
    rv=R["accepted_RV_execution"]["complete_negative_Taylor_conclusion"]
    rj=R["accepted_RJ_execution"]["complete_new_density_one_column_conclusion"]
    raw=dict(w0=[sv["complete_inverse_column_first_angular_upper"],sv["complete_inverse_column_second_angular_upper"]],
        p0=hp["complete_normalized_p_zero_angular_derivative_upper"],
        g0=bg["complete_normalized_g_zero_angular_derivative_upper"],
        w1=[dg["complete_a1_value_derivative_upper"],dg["accepted_b1_value_derivative_upper"]],
        p1=rj["complete_physical_p_angular_derivative_upper"],
        g1=dt["complete_g_angular_derivative_upper"])
    gate("every saved column keeps its exact full-disk producer and order without a missing p third derivative",
        len(raw["w0"])==len(raw["p0"])==len(raw["g0"])==len(raw["w1"])==2
        and all(len(v)==4 for k in ("w0","p0","g0","w1") for v in raw[k])
        and all(len(v)==3 for k in ("p1","g1") for v in raw[k])
        and dg["accepted_b1_value_derivative_upper"]==rv["retained_complete_b1_value_derivative_upper"]
        and dg["accepted_b1_radial_derivative_upper"]==rv["retained_complete_b1_radial_derivative_upper"]
        and bg["accepted_complete_normalized_p_zero_angular_derivative_upper"]==raw["p0"]
        and dt["full_amplitude_means_and_signed_carriers_retained"]
        and sv["full_radial_G_and_all_output_means_retained"]
        and hp["full_radial_W_and_all_output_means_retained"]
        and bg["full_radial_principal_and_all_means_retained"])
    cols={k:vector(v,3 if k in ("w0","p0","g0","w1") else 2) for k,v in raw.items()}
    summary=dict(saved_payload_sha256=payload_sha(raw),saved_column_derivative_counts={k:[len(v) for v in x] for k,x in raw.items()},
        density_zero_columns_already_include_ordered_inverse=True,
        density_one_g_producer="DG complete_direct_physical_transport_conclusion.complete_g_angular_derivative_upper",
        density_one_g_same_full_fold_D_disk=True,RJ_negative_rowwise_g_maximum_used=False,
        RJ_missing_p_third_derivative_invented=False,all_complete_means_and_both_signs_retained=True)
    return cols,summary

def positive_nonlocal(c,d,cols,A,density):
    """PC20--23, all nine words and all five independent physical mean terms."""
    k=3 if density==0 else 2
    U=c["U"];V=c["V"]
    if min(len(U),len(V))<k+2:raise ValueError("an old positive coefficient row lost an angular jet")
    eta=gap(c["eta_lower"],"same positive row eta")
    w=cols["w"+str(density)];p=cols["p"+str(density)];g=cols["g"+str(density)]
    h=vscale(p,1/eta);y=vmul(V,p,k)
    q=vadd(vmul(V,g,k),vmul(V[1:],p,k),k=k)
    def GM(v):
        value=A(v)
        if density==1:return value,value
        mean=A(vder(v));return up(value+mean),mean
    Gw,Mw=GM(w);Gh,Mh=GM(h);Gg,Mg=GM(g);Gq,Mq=GM(q);_,My=GM(y)
    CJ=up(c["C_J_new"] if density==0 else c["C_J_scalar"])
    CV=up(c["C_V"]+(c["C_R"]*CJ*c["C_B"] if density else 0))
    # Each minimum compares two COMPLETE bounds for the SAME ordered operator.
    def whole(name,fallback):return min(up(d[name]),up(fallback)).upper()
    WV=whole("C_SV_directed",CV);WQ=whole("C_SQ_directed",c["C_Q"])
    WR=whole("C_RQJ_directed",c["C_R"]*CJ)
    WRL=whole("C_RQJL_directed",c["C_R"]*CJ*c["C_L"])
    WP=whole("C_primitive_directed",c["cB"]*c["m3_vphi"]*c["C_I"])
    WU=whole("C_uJ_directed",c["m3_u"]*CJ)
    WUL=whole("C_uJL_directed",c["m3_u"]*CJ*c["C_L"])
    WUB=whole("C_uJB_directed",c["m3_u"]*CJ*c["C_B"])
    mean_primitive=up(c["cB"]*V[1]*V[0]*Mg/4)
    mean_T0=up(c["m0_T0"]*Mg)
    terms=dict(complete_SV=up(WV*Gw),complete_SQ=up(WQ*Gh),
        complete_RQ_J_g=up(WR*Gg),complete_RQ_JL_h=up(WRL*Gh),
        complete_primitive=up(WP*Gq),old_mean_rQ=up(c["m0_rQ"]*Mh),
        old_mean_vphi=up(c["cB"]*V[1]*My),
        old_mean_transported=up(mean_primitive+mean_T0),old_mean_V0=up(c["m0_V0"]*Mw))
    uh=vmul(U,h,k);vn=list(V);vn[0]=min(up(V[0]),up(V[1]/4)).upper()
    _,Muh=GM(uh);_,Mvm=GM(vmul(vn,w,k))
    fac=up(c["exact_nonlocal_even_mean_row_factor"])
    means=dict(complete_u_h=up(fac*Muh),complete_uJ_g=up(fac*WU*Gg),
        complete_uJL_h=up(fac*WUL*Gh),complete_uJB_w=up(fac*WUB*Gw),
        complete_K_vminus_w=up(fac*c["K"]*Mvm))
    return dict(nine_complete_words=terms,five_independent_physical_mean_terms=means,
        five_old_mean_summands=dict(rQ=terms["old_mean_rQ"],vphi=terms["old_mean_vphi"],
            primitive_of_v=mean_primitive,T0=mean_T0,V0=terms["old_mean_V0"]),
        total=up(sum(terms.values(),arb(0))),physical_mean=up(sum(means.values(),arb(0))),
        actual_J_factor=CJ,complete_SV_window_factor=CV,
        complete_amplitude_operator_bounds=dict(Gamma_w=Gw,Gamma_h=Gh,Gamma_g=Gg,Gamma_q=Gq,
            M_w=Mw,M_h=Mh,M_g=Mg,M_y=My,M_uh=Muh,M_vminus_w=Mvm))

def positive_weight(left,right):
    """Full real family, physical dr, retaining the entire uncertain-root band."""
    if not ROOTS[0]<=left<right<=ROOTS[1]+S1:raise ValueError("wrong new positive radial interval")
    if right<=ROOTS[1]:return up(2*ex(right-left).sqrt())
    if left<ROOTS[1]:raise ValueError("the uncertain-root band was not split")
    return up(2*(ex(right-ROOTS[1]).sqrt()-ex(left-ROOTS[1]).sqrt()))

def same_shift_words(drow):
    """M1 exponential matrix norm, BEFORE the old Sobolev conversion."""
    found=[x for x in drow["complete_width_evidence"] if x["width"]==str(SB)]
    if len(found)!=1:raise ValueError("same paid matrix width is not unique")
    e=found[0]
    if not (e["usable"] and up(e["actual_original_contraction"])<1
            and e["all_old_mean_ranks_and_radial_terms_retained"]
            and e["parity_reflection_inserted_in_exponential_algebra"] is False):
        raise ValueError("the same-shift full matrix domain is not certified")
    return {k:up(e["operator_words"][k]["z"]) for k in ("J","B","L")}

def finite_head_coefficient(c):
    """Full low-to-high moving linearization, including primitive and low mean input."""
    U,V,D=c["U"],c["V"],c["D"];b=c["beta"];K=c["K"]
    local=b*(2+4*U[0]**2+4*K*V[0]**2+2*(1+K)*U[0]*V[0])
    primitive=b*(U[1]+V[1])*(U[0]+K*V[0])/2
    return up(384*D[0]+local+primitive)

def integrate_positive(selected,cols,A,local,gate):
    """Only NEW positive source products and NEW physical integrals."""
    sq1=arb(0);sqm=arb(0);termsq={};meansq={};kfh2=arb(0);audit=[]
    zmax={k:arb(0) for k in ("J","B","L")};eta_min=None;rawlength=Q(0)
    distinct=set();root_band_count=0;functional_calls=0
    for row,drow,left,right in selected:
        c=unpack(row["bounds"]);d=unpack(drow["bounds"])
        for value in c.values():
            for z in value if isinstance(value,list) else [value]:up(z)
        for value in d.values():up(value)
        norms=same_shift_words(drow)
        for k,v in norms.items():zmax[k]=max(zmax[k],v).upper()
        em=gap(c["eta_lower"],"positive same-family eta")
        eta_min=em if eta_min is None else min(eta_min,em).lower()
        n0=positive_nonlocal(c,d,cols,A,0);n1=positive_nonlocal(c,d,cols,A,1)
        # Each density uses seven GM calls; density zero uses two A per call.
        functional_calls+=21
        J=up(c["C_J_scalar"])
        weighted=[local[0],up(local[1]/N),up(local[2]/(N*N))]
        ts={"local_raw_"+str(i+1):up(J*v) for i,v in enumerate(weighted)}
        ms={}
        for i,rr in enumerate((n0,n1)):
            ts.update({"density"+str(i)+"_"+k:up(J*v) for k,v in rr["nine_complete_words"].items()})
            ms.update({"density"+str(i)+"_"+k:v for k,v in rr["five_independent_physical_mean_terms"].items()})
        first=up(sum(ts.values(),arb(0)));mean=up(sum(ms.values(),arb(0)))
        weight=positive_weight(left,right)
        sq1+=weight*first*first;sqm+=weight*mean*mean
        for k,v in ts.items():termsq[k]=termsq.get(k,arb(0))+weight*v*v
        for k,v in ms.items():meansq[k]=meansq.get(k,arb(0))+weight*v*v
        K=finite_head_coefficient(c);length=right-left;kfh2+=ex(length)*K*K;rawlength+=length
        distinct.add(row["common_row"]);root_band_count+=int(right<=ROOTS[1])
        audit.append(dict(common_row=row["common_row"],original_interval=row["interval"],
            exact_positive_intersection=[str(left),str(right)],exact_physical_length=str(length),
            original_complete_row_sha256=payload_sha(row),original_directed_row_sha256=payload_sha(drow),
            radial_weight_upper=rec(weight),first=rec(first),mean=rec(mean),density0=encode(n0),density1=encode(n1),
            complete_first_row_terms=encode(ts),complete_independent_mean_terms=encode(ms),
            complete_low_to_high_coefficient=rec(K),same_shift_L2_words=encode(norms)))
    gate("the positive products retain21 complete first-row and10 independent mean terms on every true intersection",
        len(termsq)==21 and len(meansq)==10 and len(audit)==len(selected)
        and all(len(x["complete_first_row_terms"])==21 and len(x["complete_independent_mean_terms"])==10 for x in audit)
        and root_band_count>0 and rawlength==ROOTS[1]+S1-ROOTS[0]
        and eta_min is not None and eta_min>0)
    first=up(sq1.sqrt());mean=up(sqm.sqrt());pair=up((sq1+sqm).sqrt());KFH=up(kfh2.sqrt())
    gate("the new positive ordinary source and complete finite-head coefficient integrals are finite with actual dr",
        all(x.is_finite() and x.lower()>=0 for x in (first,mean,pair,KFH,*zmax.values()))
        and all(x["exact_positive_intersection"][0]!=x["exact_positive_intersection"][1] for x in audit))
    summary=dict(exact_positive_union=[str(ROOTS[0]),str(ROOTS[1]+S1)],exact_union_length=str(rawlength),
        restored_complete_original_rows=1328,distinct_original_positive_rows=len(distinct),
        complete_positive_intersections=len(audit),uncertain_root_band_intersections=root_band_count,
        complete_first_row_L2_upper=rec(first),complete_independent_mean_L2_upper=rec(mean),
        complete_pair_L2_upper=rec(pair),
        separate_complete_first_row_term_L2_upper={k:rec(up(v.sqrt())) for k,v in termsq.items()},
        separate_complete_independent_mean_term_L2_upper={k:rec(up(v.sqrt())) for k,v in meansq.items()},
        complete_low_to_high_coefficient_L2_upper=rec(KFH),same_shift_L2_word_maxima=encode(zmax),
        exact_same_shift_paid_matrix_width=str(SB),eta_lower=rec(eta_min),
        complete_positive_row_payload_sha256=payload_sha(audit),new_positive_functional_evaluations=functional_calls,
        complete_physical_dr_used=True,negative_integrals_or_negative_row_maxima_reused=False,
        no_pointwise_actual_root_from_interval_midpoint=True,finite_low_mean_input_retained=True,
        full_row_arrays_temporary_only=True)
    return dict(pair=pair,KFH=KFH,z=zmax,eta=eta_min),summary,audit

def exponential_sum(power,c):
    """Exact positive Eulerian form of sum_{j>=97}(4j)^power exp(-8cj)."""
    if power not in (5,7):raise ValueError("wrong full-frequency polynomial")
    c=gap(c,"full-frequency positive exponent");x=(-8*c).exp().upper()
    den=gap(1-x,"full infinite exponential denominator")
    moments=[1/den];euler=[1]
    for k in range(1,power+1):
        if k>1:
            previous=euler
            euler=[(m+1)*(previous[m] if m<len(previous) else 0)
                +(k-m)*(previous[m-1] if m>0 else 0) for m in range(k)]
        if sum(euler)!=math.factorial(k) or min(euler)<0:
            raise ValueError("the exact positive Eulerian polynomial is incomplete")
        poly=sum((ex(v)*x**i for i,v in enumerate(euler)),arb(0))
        moments.append(x*poly/den**(k+1))
    total=4**power*x**J0*sum((ex(math.comb(power,k)*J0**(power-k))*moments[k]
                             for k in range(power+1)),arb(0))
    return up(total),dict(power=power,physical_frequency_multiplier=4,first_abs_j=J0,
        exponent_lower=rec(c),geometric_ratio_upper=rec(x),strict_one_minus_ratio_lower=rec(den),
        complete_infinite_sum_upper=rec(up(total)),no_finite_frequency_truncation=True)

def cutoff_and_head(domain,integ,gate):
    """PC25--33, complete two-row exact reconstruction and finite-head leakage."""
    d=domain;z=integ["z"];h=d["h"]
    WL=d["whole_leading_modulus"];WV=d["whole_genuine_modulus"]
    W0=up(WL+WV/N)
    WD=up(WL*(1/ex(RG-h)+d["whole_D"]/ex(SG-SP))
        +(WV/N)*(1/ex(RS-h)+d["whole_D"]/ex(SS-SP)))
    KA=up(d["CA"]*(1+pw(ex(N),Q(-1,3))+d["Tmax"].sqrt()))
    kN=up(pw(1+ex(Q(1,N*N)),Q(2,3)))
    dx=up(d["whole_Q"]*d["Th"]*d["Y0"]);dt=up(d["whole_Q"]*d["M"])
    KD=up(dx+dt*max(arb(1),d["Tmax"]+d["V"]/(N*N)))
    KDh=up(dx+dt*d["contour_A"])
    Bmat=up(2*d["inverse_HV"])
    eta=integ["eta"]
    def pair(K,strip_margin):
        Ac=up(KA*z["J"]*K*W0)
        Bc=up(KA*(W0+z["J"]*(WD+z["B"]*W0)))
        P0=up(Bmat*K*W0)
        Pphi=up(P0/ex(strip_margin));H0=up(P0/eta);G0=up(WD+Pphi)
        sharp=up(KA*(W0+H0+z["J"]*(G0+z["L"]*H0+z["B"]*W0)))
        return dict(A=Ac,B=Bc,sharp=sharp,P=P0,P_phi=Pphi,H=H0,G=G0)
    real=pair(KD,SP);shift=pair(KDh,SP-SIGMA)
    cp=gap(ex(Q(2,3))*pw(d["Tmin"],Q(3,2)),"actual positive Airy decay")
    ch=d["contour_c"]
    Z5,z5=exponential_sum(5,cp);Z7,z7=exponential_sum(7,cp)
    H5,h5=exponential_sum(5,ch);H7,h7=exponential_sum(7,ch)
    sqrt2=arb(2).sqrt()
    cutoff_factor=up(ex(DERIVATIVE_CUTOFF)*ex(S1-S0).sqrt()*kN*sqrt2)
    cutoff_crude=up(cutoff_factor*(real["A"]*Z7.sqrt()+real["B"]*Z5.sqrt()))
    cutoff_sharp=up(cutoff_factor*real["sharp"]*Z5.sqrt())
    cutoff=min(cutoff_crude,cutoff_sharp).upper()
    head_factor=up((384*ex(SIGMA)).exp()*kN*sqrt2)
    head_crude=up(head_factor*(shift["A"]*H7.sqrt()+shift["B"]*H5.sqrt()))
    head_sharp=up(head_factor*shift["sharp"]*H5.sqrt())
    head=min(head_crude,head_sharp).upper()
    leakage=up(integ["KFH"]*head)
    gate("the complete cutoff and finite-head sums use true T-curve length full same-shift matrices and both rows",
        cp>0 and ch>0 and h<RS and SIGMA<SP<min(SB,SS,SG)
        and all(x.is_finite() and x.lower()>=0 for x in
                (W0,WD,KD,KDh,KA,Bmat,Z5,Z7,H5,H7,cutoff,head,leakage))
        and S1-S0==Q(1,10**6))
    summary=dict(complete_pair_amplitude_holomorphic_upper=rec(W0),
        complete_D_amplitude_holomorphic_upper=rec(WD),
        genuine_n_minus_one_included=True,exact_holomorphic_p_strip=str(SP),
        exact_contour_shift=str(SIGMA),complete_KD_real_upper=rec(KD),complete_KD_shift_upper=rec(KDh),
        complete_terminal_KA_upper=rec(KA),complete_matrix_entry_sum_upper=rec(Bmat),
        complete_real_reconstruction_coefficients=encode(real),complete_shift_reconstruction_coefficients=encode(shift),
        complete_positive_decay_exponent_lower=rec(cp),complete_contour_decay_exponent_lower=rec(ch),
        infinite_sums=dict(cutoff_Z5=z5,cutoff_Z7=z7,finite_head_Z5=h5,finite_head_Z7=h7),
        complete_cutoff_two_row_crude_upper=rec(cutoff_crude),
        complete_cutoff_two_row_reconstructed_upper=rec(cutoff_sharp),
        complete_cutoff_two_row_source_upper=rec(cutoff),
        complete_finite_head_crude_upper=rec(head_crude),
        complete_finite_head_reconstructed_upper=rec(head_sharp),
        complete_finite_head_at_root_and_body_upper=rec(head),
        complete_finite_head_to_high_source_upper=rec(leakage),
        exact_transition_length=str(S1-S0),exact_transition_derivative_upper=str(DERIVATIVE_CUTOFF),
        physical_mean_and_full_head_retained=True,finite_head_derivative_not_discarded=True,
        radial_derivative_commutes_with_finite_projection=True,
        actual_high_projection_of_finite_mean_rank_zero_by_degree96=True,
        negative_Sobolev_operator_norm_not_used_as_same_shift_L2=True,
        full_true_T_contour_length_not_endpoint_distance=True,
        independent_complex_delta_phase_claimed=False)
    return dict(cutoff=cutoff,head=head,leakage=leakage),summary

def complete_correction(integ,cut,PW,RJ,gate):
    """Only the same positive zero-stable-port correction; trial normalization stays open."""
    ports=PW["complete_seven_port_waist_conclusion"]
    negative=PW["complete_negative_inputs_conclusion"]
    copied=PW["current_genuine_source_contribution_read_verbatim"]
    incoming=ports["complete_positive_seven_port_to_waist_coefficients_upper"]
    nd=negative["complete_to_waist_coefficients_read_verbatim"]
    current=RJ["complete_source_conclusion"]
    if len(incoming)!=7 or len(nd)!=5:raise ValueError("complete port shape changed")
    Cplus=up(integ["pair"]+cut["cutoff"]+cut["leakage"])
    positive=up(up(incoming[1])*Cplus)
    head=up(up(nd[0])*cut["head"])
    # Preserve the successful PW multiplication literally; never recompute it.
    old_product=copied["current_genuine_strong_source_to_waist_contribution_upper"]
    value=up(positive+head+up(old_product))
    gate("the complete positive correction keeps zero correction stable port independent trial root mean and old negative product",
        ports["input_order"][1]=="collar_ordinary_Hminus2over3_source"
        and ports["root_stable_input_retained"] and ports["finite_root_head_and_two_mean_inputs_retained"]
        and negative["independent_two_root_mean_coordinates"]==2
        and copied["current_genuine_source_pair_L2_upper"]==current["combined_L2_upper"]
        and len(current["complete_first_source_term_L2_upper"])==21 and len(current["complete_independent_mean_term_L2_upper"])==10
        and all(v.is_finite() and v.lower()>=0 for v in (Cplus,positive,head,value)))
    return dict(input="H^(-4/3), both physical carrier signs and all |j|>=97",
        output="same waist old-circle primitive density L2 pair plus both full mean coordinates",
        exact_complete_positive_source_window="ordinary L2_dr H^(-2/3) first row plus independent constant row",
        complete_positive_ordinary_volume_upper=rec(integ["pair"]),
        complete_positive_cutoff_source_upper=rec(cut["cutoff"]),
        complete_finite_head_commutator_source_upper=rec(cut["leakage"]),
        complete_positive_high_residual_upper=rec(Cplus),
        accepted_positive_collar_to_waist_gain_read_verbatim=incoming[1],
        accepted_root_head_to_waist_gain_read_verbatim=nd[0],
        new_positive_correction_to_waist_upper=rec(positive),
        new_root_finite_head_to_waist_upper=rec(head),
        accepted_negative_whole_source_read_verbatim=copied["current_genuine_source_pair_L2_upper"],
        accepted_negative_source_to_waist_product_read_verbatim=old_product,
        complete_strong_correction_to_waist_upper=rec(value),
        positive_correction_root_stable_boundary_condition="zero",
        trial_root_stable_trace_retained_and_not_inverted=True,
        outgoing_unstable_root_trace_paid_by_complete_seven_port_graph=True,
        full_root_finite_head_and_two_mean_inputs_retained=True,
        negative_root_raw_Hminus1_not_promoted_to_raw_L2=True,
        genuine_root_beta_shear_not_discarded=True,
        all_old_completed_multiplications_preserved=True,
        full_true_incoming_inverse_proved=False,
        full_trial_minus_exponential_or_linear_return_reference_bound=False,
        full_strong_return_R0_or_cutoff97_inverse_claimed=False)

def render_conclusion(doc):
    out={k:doc[k] for k in ("kind","complete","proved","actual_returncode","failure","source_sha256",
        "input_manifest_sha256","runtime","arithmetic_bits","run_id","run_attempt","actual_mathematical_wall_seconds") if k in doc}
    out["passed_gates"]=sum(g["passed"] for g in doc["gates"]);out["total_gates"]=len(doc["gates"])
    out["mathematical_parameters"]=doc["mathematical_parameters"]
    for k in ("complete_strong_correction_conclusion","scope"):
        if k in doc:out[k]=doc[k]
    if "complete_positive_volume_conclusion" in doc:
        v=doc["complete_positive_volume_conclusion"]
        out["complete_positive_volume"]={k:v[k] for k in ("exact_positive_union","exact_union_length",
            "restored_complete_original_rows","distinct_original_positive_rows","complete_positive_intersections",
            "uncertain_root_band_intersections","complete_first_row_L2_upper","complete_independent_mean_L2_upper",
            "complete_pair_L2_upper","complete_low_to_high_coefficient_L2_upper","same_shift_L2_word_maxima",
            "complete_positive_row_payload_sha256")}
    if "complete_cutoff_and_head_conclusion" in doc:
        v=doc["complete_cutoff_and_head_conclusion"]
        out["complete_cutoff_and_head"]={k:v[k] for k in (
            "complete_positive_decay_exponent_lower","complete_contour_decay_exponent_lower",
            "complete_cutoff_two_row_source_upper","complete_finite_head_at_root_and_body_upper",
            "complete_finite_head_to_high_source_upper")}
    lines=["# Genuine positive Ai cutoff and complete strong correction","",
        "The full small scientific receipt also retains the complete21 first-row and10 independent mean conclusions.",
        "Complete intermediate positive-row tables exist only in the temporary native.","",
        chr(96)*3+"json",json.dumps(out,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False),chr(96)*3,""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","workdir","process","conclusion","out"):
        p.add_argument("--"+name,type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new scientific arithmetic is permitted only on the public repository Actions runner")
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the frozen public scientific runtime changed")
    ctx.prec=320;a.workdir.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,arithmetic_bits=320,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        mathematical_parameters=params(),original_successful_small_receipts_read=0,
        original_complete_fold_stages_read=0,original_complete_coefficient_rows_read=0,
        original_complete_directed_matrix_rows_read=0,original_positive_linear_coefficients_read=0,
        saved_complete_column_derivative_bounds_read=0,new_positive_profile_functionals=0,
        new_positive_intersections=0,new_positive_source_products=0,new_positive_radial_integrals=0,
        new_complete_exponential_sums=0,new_cutoff_and_finite_head_bounds=0,new_strong_correction_compositions=0,
        old_numerical_enclosures_recomputed=0,old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed=0,
        old_amplitude_derivatives_profiles_or_calibrations_recomputed=0,
        old_matrix_words_or_rows_recomputed=0,old_negative_source_or_integrals_recomputed=0,
        old_positive_graph_negative_Cauchy_SP_or_PW_products_recomputed=0,
        original_natural_stage_bytes_modified=False,full_high_inverse_claimed=False,
        full_strong_return_R0_evaluated=False,temporary_native_is_not_published=True,
        reproducible_outputs_published_to_repository=False,reproducible_outputs_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False)
    def gate(name,truth):
        passed=bool(truth);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("actual PC gate failed: "+name)
    try:
        manifest=read(a.manifest)
        gate("the new immutable manifest and complete input closure agree with the frozen source and contract",
            manifest["source_sha256"]==sha(__file__) and manifest["contract_sha256"]==CONTRACT
            and manifest["runtime"]==RUNTIME and manifest["mathematical_parameters"]==params()
            and manifest["historical_input_commit"]=="a3d84d905ce72e3a854874bbe98d119623f3f8de"
            and len({e["path"] for e in manifest["files"]})==len(manifest["files"]))
        for e in manifest["files"]:
            q=a.repo_root/e["path"]
            if not q.is_file() or q.stat().st_size!=e["bytes"] or sha(q)!=e["sha256"]:
                raise ValueError("immutable input changed: "+e["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        for k in EXPECTED:
            if k not in paths:raise ValueError("missing successful scalar receipt: "+k)
        gate("the new source contains no old scientific import and pins every completed producer identity",
            all(e["path"] in {v for v in manifest["input_paths"].values()} or e.get("role")=="primary_source_or_proof"
                for e in manifest["files"])
            and set(EXPECTED)<=set(paths)
            and sha(paths["contract"])==CONTRACT)
        R={k:accepted(paths[k],identity,gate) for k,identity in EXPECTED.items()}
        doc["original_successful_small_receipts_read"]=len(R)
        original=read_original_fold(paths,gate);doc["original_complete_fold_stages_read"]=1
        rows,old_process,direct_process=read_original_rows(paths,gate)
        doc["original_complete_coefficient_rows_read"]=1328;doc["original_complete_directed_matrix_rows_read"]=1328
        d,con=common_domain(original,R,gate);doc["complete_positive_domain_conclusion"]=con
        A,local,con=positive_functional(d,R["complete_genuine_execution"],R["accepted_ER_execution"],R["accepted_RV_execution"],gate)
        doc["complete_positive_profile_and_local_conclusion"]=con
        doc["original_positive_linear_coefficients_read"]=18;doc["new_positive_profile_functionals"]=1
        cols,con=saved_columns(R,gate);doc["complete_saved_columns_conclusion"]=con
        doc["saved_complete_column_derivative_bounds_read"]=44
        integ,con,audit=integrate_positive(rows,cols,A,local,gate)
        doc["complete_positive_volume_conclusion"]=con
        doc["new_positive_intersections"]=len(rows);doc["new_positive_source_products"]=con["new_positive_functional_evaluations"]
        doc["new_positive_radial_integrals"]=len(rows)
        cut,con=cutoff_and_head(d,integ,gate);doc["complete_cutoff_and_head_conclusion"]=con
        doc["new_complete_exponential_sums"]=4;doc["new_cutoff_and_finite_head_bounds"]=2
        doc["complete_strong_correction_conclusion"]=complete_correction(integ,cut,R["accepted_PW_execution"],R["accepted_RJ_execution"],gate)
        doc["new_strong_correction_compositions"]=1
        doc["scope"]=dict(
            full_real_delta_family=True,physical_input_n_equals_4_abs_j=True,both_carriers_and_all_output_means=True,
            new_same_full_disk_positive_Airy_functional=True,all_three_raw_local_vectors=True,
            two_J_density_windows_and_full_nine_words=True,all_five_old_and_independent_physical_means=True,
            new_positive_intersections_only=True,actual_dr_and_uncertain_root_band=True,
            ordinary_source_is_not_return_inverse=True,nonzero_root_beta_n_retained=True,
            terminal_Ai_solution_not_replaced_by_root_Ai=True,full_J_L_B_same_shift_exponential_matrix_domain=True,
            new_finite_head_low_to_high_operator_complete=True,
            correction_stable_port_zero_does_not_set_trial_stable_port_zero=True,
            full_positive_correction_seven_port_graph_consumed=True,
            physical_mixed_root_output9_and_independent_finite_head_retained=True,
            same_negative_Cauchy_and_SP_waist_readout_consumed=True,
            old_negative_product_read_verbatim=True,
            full_trial_remainder_true_incoming_inverse_and_complete_strong_R0_not_claimed=True)
        gate("all old successful mathematics is read only and all new scalar outputs retain their exact limited scope",
            doc["original_successful_small_receipts_read"]==13
            and doc["original_complete_coefficient_rows_read"]==doc["original_complete_directed_matrix_rows_read"]==1328
            and doc["original_positive_linear_coefficients_read"]==18
            and doc["saved_complete_column_derivative_bounds_read"]==44
            and doc["new_complete_exponential_sums"]==4
            and doc["new_strong_correction_compositions"]==1
            and all(doc[k]==0 for k in (
                "old_numerical_enclosures_recomputed","old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed",
                "old_amplitude_derivatives_profiles_or_calibrations_recomputed","old_matrix_words_or_rows_recomputed",
                "old_negative_source_or_integrals_recomputed","old_positive_graph_negative_Cauchy_SP_or_PW_products_recomputed")))
        native=dict(kind=KIND,source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),
            mathematical_parameters=params(),complete_positive_rows=audit,complete_positive_domain=encode(d),
            complete_saved_columns=encode(cols),complete_positive_profile_and_local_conclusion=doc["complete_positive_profile_and_local_conclusion"],
            complete_cutoff_and_head_conclusion=doc["complete_cutoff_and_head_conclusion"],
            complete_strong_correction_conclusion=doc["complete_strong_correction_conclusion"],
            complete=True,proved=True,actual_returncode=0,failure=None)
        save(a.out,native,compressed=True)
        doc["temporary_complete_source_row_count"]=len(audit)
        doc["temporary_complete_source_row_payload_sha256"]=payload_sha(audit)
        doc["temporary_native_sha256"]=sha(a.out);doc["temporary_native_bytes"]=a.out.stat().st_size
        doc.update(complete=True,proved=True,actual_returncode=0)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
        raise
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        # No temporary rows, arrays or rerunnable middle products enter either small public output.
        save(a.process,doc);a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        a.conclusion.write_text(render_conclusion(doc),encoding="utf-8")
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            actual_returncode=doc["actual_returncode"],gates=len(doc["gates"]),
            positive_intersections=doc["new_positive_intersections"],
            seconds=doc["actual_mathematical_wall_seconds"])),flush=True)
if __name__=="__main__":main()
