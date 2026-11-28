"""Pay the full G.6 rank-one G.9 summand in its original negative window."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from importlib.metadata import version
from math import nextafter,inf,isfinite
import argparse,gzip,json,os,struct,subprocess,sys
from flint import arb,ctx
from fourfold_codazzi_signed_density_transport_arithmetic import exact,ball
from fourfold_codazzi_true_phase_original_inputs import (
    CUT,MANIFEST,CENTRE,DIRECTION,DELTA,admit,check)
from fourfold_codazzi_true_characteristic_seed_admission import ROOT
from fourfold_codazzi_true_phase_signed_speed import Inputs
from fourfold_codazzi_true_ratio_first_raw import first_raw,make_direction
from fourfold_codazzi_true_ratio_live_rules import canonical,gate
from fourfold_codazzi_true_ratio_prefix import Prefix,replace

TOPIC="topics/visible-flex-exact-nearby/"
OLD="notes/complex_inner_root_first_Airy_forcing_ci/run-43638232415-1/consumers/process.json"
RADIUS="notes/piecewise_real_root_fold_resume_v2_ci/run-43616813816-1/consumers/process.json"
BINS=(388,4*(2**20+1))
L=struct.Struct("<I");BOX=struct.Struct("<dddd")


def old_receipt(repo,path,n,digest):
    b=(repo/(TOPIC+path)).read_bytes()
    check(len(b)==n and sha256(b).hexdigest()==digest,"complete saved natural input "+path)
    return json.loads(b)


def up64(x):
    z=nextafter(float(x.upper()),inf)
    check(isfinite(z) and z>=0,"finite directed real upper")
    return z


def add(total,mass,a,b):
    coeff=(1400000*a+40000*b)*exact(Q(35,2))
    return (total+exact(mass)*coeff*coeff).upper()


def result(total):
    base=total.sqrt().upper();out={}
    for n in BINS:
        # (1+n^-2)^(2/3) <= 1+n^-2, a rational upper with the original units.
        val=base*(1+exact(Q(1,n*n)))/arb(n).sqrt()
        out[str(n)]={"scalar_Hminus5over3_ordinary_dr_L2_upper":up64(val),
                     "first_row_after_original_J_Hminus2over3_ordinary_dr_L2_upper":up64(2*val),
                     "full_original_reflected_input_Hminus4over3":True}
    return out


def verify_prefix(path,receipt,frontier):
    csize=receipt["private_prefix_bytes"]
    with path.open("rb") as f:b=f.read(csize)
    check(len(b)==csize and sha256(b).hexdigest()==receipt["private_prefix_sha256"],"entire committed GSF prefix")
    u=gzip.decompress(b)
    check(len(u)==receipt["private_prefix_uncompressed_bytes"] and
          sha256(u).hexdigest()==receipt["private_prefix_uncompressed_sha256"],"entire uncompressed GSF prefix")
    if not receipt["completed_subpieces"]:return u,None
    c=frontier.read_bytes();d=gzip.decompress(c)
    check((len(c),sha256(c).hexdigest(),len(d),sha256(d).hexdigest())==
          tuple(receipt[k] for k in ("continuation_bytes","continuation_sha256","continuation_uncompressed_bytes",
                                     "continuation_uncompressed_sha256")),"entire GSF continuation")
    return u,json.loads(d)


def receive_prefix(a,base,head,private):
    import io
    if not a.resume_receipt:return None
    saved=a.resume_receipt.read_bytes()
    check(sha256(saved).hexdigest()==a.resume_receipt_sha,"original complete failed or stopped prefix receipt")
    prior=json.loads(saved);n=prior["completed_subpieces"]
    for key in ("original_receipts_sha256","charged_subcells_sha256","negative_root_interval","absolute_delta_upper"):
        check(prior[key]==base[key],"same complete GSF input and plan: "+key)
    check(prior["complete"] is False and 0<n<base["charged_strict_subcells"],"strictly incomplete prior prefix")
    root=a.resume_private
    u,frontier=verify_prefix(root/"genuine-rank-one-original-theta-rows.gz",prior,root/prior["continuation_file"])
    f=io.BytesIO(u);nh,=L.unpack(f.read(4))
    check(f.read(nh)==head and frontier["completed"]==n and frontier["plan"]==base["charged_subcells_sha256"],
          "same entire natural prefix and frontier")
    for i in range(n):
        header=f.read(8);lo,count=struct.unpack("<ii",header);data=f.read(BOX.size*count)
        check(0<count<=4096 and len(data)==BOX.size*count,"complete uniquely counted prior signed row")
        private.append(header+data)
    check(not f.read(1) and private.raw.hexdigest()==prior["private_prefix_uncompressed_sha256"] and
          private.gz.hexdigest()==prior["private_prefix_sha256"],"prior rows copied exactly without evaluating them")
    man,exp=frontier["sum_upper_exact_dyadic"];total=exact(Q(int(man))*Q(2)**int(exp))
    check(total.is_exact() and total>=0,"exact directed positive accumulated moment at continuation")
    private.commit(dict(base,completed_subpieces=n,completed_strict_subcells=n,prefix_proved=True,
                   resumed_whole_prefix_receipt_sha256=a.resume_receipt_sha,actual_weighted_prefix=result(total)),
                   canonical(frontier))
    return total,n


def run(a):
    check(os.environ["GITHUB_REPOSITORY"]=="Rogerhu12/math-research-public" and os.environ["GITHUB_ACTIONS"]=="true"
          and os.environ["GITHUB_RUN_ATTEMPT"]=="1" and sys.version_info[:3]==(3,12,14)
          and version("python-flint")=="0.9.0" and version("numpy")=="2.3.5","declared public scientific owner")
    ctx.prec=320;gate()
    d=old_receipt(a.repo,OLD,43790,"f8ab9fbf35c39df97f7318e3b71d1c1f08dba6a62290a8ab3144fe7f7446a274")
    m=old_receipt(a.repo,RADIUS,32670,"c30eb4c5e1efebd3663528418389ececf1ba8f4450f8e667496026915e2dfb64")
    rl,rh=map(Q,ROOT)
    lo,hi=map(Q,d["exact_original_complex_radial_rectangle"]["real_interval"])
    tensor=d["complete_coefficient_budget_numeric"];bud=m["selected"]["bounds"]
    check(d["complete"] and d["mathematical_complete"] and d["actual_returncode"]==0 and d["failure"] is None
          and d["mathematical_failure"] is None and d["background_definition_sha256"]==CENTRE
          and d["explicit_direction_definition_sha256"]==DIRECTION and d["actual_intrinsic_parameter"]=="eta_0"
          and Q(d["exact_complex_parameter_radius"])>=DELTA and list(map(Q,d["exact_root_interval"]))==[rl,rh]
          and lo<=CUT<rl<=rh<=hi and rh-CUT<Q(1,100000) and
          ball(tensor["vartheta"]).upper()<23 and ball(tensor["sigma"]).lower()>exact(Q(1,128)),
          "full old root theta and angle loss apply from the genuine cut to the true root")
    check(m["selected"]["exact_radius"]=="1/50" and m["selected"]["passed"]
          and ball(bud["a_upper"]).upper()<23 and ball(bud["A_lower"]).lower()>4
          and ball(bud["leading_G"]).upper()<exact(Q(23,10)),
          "same complete piecewise positive leading bounds")
    def read(c,p):return subprocess.check_output(["git","show",c+":"+p],cwd=a.repo)
    old=admit((a.repo/MANIFEST).read_bytes(),read)
    inp=Inputs(*old[:-1]);direction=make_direction(old[3]);oldreceipts=old[-1]
    stop=rl-Q(1,5000)
    plan=[(i,max(l,stop),r,k,j) for i,(l,r,k,j) in enumerate(inp.plan) if r>stop]
    check(plan and plan[0][2]==CUT and plan[-1][1]==stop and
          all(x[1]==y[2] for x,y in zip(plan,plan[1:])),"entire possible physical potential support")
    ids=[[i,str(l),str(r),k,j] for i,l,r,k,j in plan]
    base={"kind":"actual_genuine_G6_rank_one_w0_in_original_G9_strong_source_window",
          "run":os.environ["GITHUB_RUN_ID"],"attempt":1,"event_commit":os.environ["GITHUB_SHA"],
          "fixed_parameter":"eta_0","absolute_delta_upper":str(DELTA),"negative_root_interval":list(ROOT),
          "potential_support_inward_distance_upper":"1/5000","root_to_cut_comparison":str(CUT),
          "charged_strict_left":str(stop),"whole_original_physical_plan_cells":len(inp.plan),
          "charged_strict_subcells":len(plan),"charged_subcells_sha256":sha256(canonical(ids)).hexdigest(),
          "original_count":len(oldreceipts),"original_bytes":sum(v["bytes"] for v in oldreceipts),
          "original_receipts_sha256":sha256(canonical(oldreceipts)).hexdigest(),
          "old_scientific_targets_recomputed":0,"old_private_phase_carriers_restored":0,
          "complete_high_waist_response_proved":False,"independent_positive_correction_included":False}
    a.private.mkdir(parents=True,exist_ok=True)
    path=a.private/"genuine-rank-one-original-theta-rows.gz"
    mass=(rh-CUT)**5/5
    total=add(arb(0),mass,arb(23),arb(128*23));passed=0
    head=canonical({"plan":ids,"schema":"GSF1","column":"all original signed Laurent coefficients of theta",
                    "payload":"four outward binary64 endpoints per complex coefficient"})
    private=Prefix(path,a.receipt,head,dict(base,completed_strict_subcells=0,actual_weighted_prefix=result(total)))
    try:
        prior=receive_prefix(a,base,head,private)
        if prior is not None:total,passed=prior
        for i,l,r,k,j in plan[passed:]:
            gate()
            original=inp.plan[i]
            th=first_raw(inp,direction,original,l,r)["theta"]
            check(th.finite(),"every actual angular coefficient without a frequency cutoff")
            ta,tb=th.a(0),th.a(1)
            mass=((rh-l)**5-(rh-r)**5)/5
            check(mass>0,"real positive fourth radial moment")
            local=add(total,mass,ta,tb)
            row=bytearray()
            for z in th.p:
                box=(nextafter(float(z.real.lower()),-inf),nextafter(float(z.real.upper()),inf),
                     nextafter(float(z.imag.lower()),-inf),nextafter(float(z.imag.upper()),inf))
                check(all(map(isfinite,box)) and box[0]<=box[1] and box[2]<=box[3],"signed directed private row")
                row.extend(BOX.pack(*box))
            payload=struct.pack("<ii",th.lo,len(th.p))+row
            total=local;passed+=1
            man,exp=total.man_exp()
            frontier=canonical({"kind":"GSF_positive_moment_continuation","completed":passed,
                               "sum_upper_exact_dyadic":[str(man),int(exp)],"outward_left":str(l),
                               "next_original_cell":None if passed==len(plan) else plan[passed][0],
                               "plan":base["charged_subcells_sha256"]})
            current=dict(base,completed_subpieces=passed,completed_strict_subcells=passed,prefix_proved=True,
                         last_original_cell=i,closed_strict_subpiece=[str(l),str(r)],current_read_head=gate(),
                         actual_weighted_prefix=result(total))
            private.append(payload);private.commit(current,frontier)
            if passed%16==0:print("GSF_CONFIRMED_PREFIX",a.receipt.read_text().strip(),flush=True)
    finally:
        private.close()
    saved=json.loads(a.receipt.read_bytes())
    full,frontier=verify_prefix(path,saved,a.private/saved["continuation_file"])
    check(frontier["completed"]==passed==len(plan) and len(full)==private.usize and
          sha256(full).hexdigest()==private.raw.hexdigest() and path.stat().st_size<10_000_000,
          "entire signed private GSF stream and every accepted natural row")
    nraw=private.usize
    last=result(total);p=path.read_bytes()
    gates={"whole97_first_row_below_one_over_8":last[str(BINS[0])]["first_row_after_original_J_Hminus2over3_ordinary_dr_L2_upper"]<1/8,
           "whole_late_first_row_below_one_over_256":last[str(BINS[1])]["first_row_after_original_J_Hminus2over3_ordinary_dr_L2_upper"]<1/256}
    published=dict(base,completed_strict_subcells=passed,complete=True,proved=True,
                   full_sources=last,quantitative_tests=gates,
                   private_bytes=len(p),private_sha256=sha256(p).hexdigest(),private_uncompressed_bytes=nraw,
                   private_uncompressed_sha256=private.raw.hexdigest(),last_rules_read_head=gate(),
                   completed_subpieces=passed,resumed_complete_prefix=bool(a.resume_receipt))
    published.update({k:v for k,v in saved.items() if k.startswith("continuation_")})
    replace(a.receipt,canonical(published))
    print("GSF_WHOLE_SMALL_RECEIPT",canonical(published).decode().strip(),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","private","receipt"):ap.add_argument("--"+k,required=True,type=Path)
    ap.add_argument("--resume-receipt",type=Path);ap.add_argument("--resume-receipt-sha")
    ap.add_argument("--resume-private",type=Path)
    a=ap.parse_args()
    try:
        check(bool(a.resume_receipt)==bool(a.resume_receipt_sha)==bool(a.resume_private),"whole prior prefix identity tuple")
        run(a)
    except Exception as exc:
        prior=json.loads(a.receipt.read_bytes()) if a.receipt.exists() else {"completed_subpieces":0}
        if prior.get("completed_subpieces",0) and "private_prefix_bytes" in prior:
            verify_prefix(a.private/"genuine-rank-one-original-theta-rows.gz",prior,a.private/prior["continuation_file"])
        prior.update(complete=False,proved=False,failure=str(exc),run=os.environ["GITHUB_RUN_ID"],attempt=1,
                     event_commit=os.environ["GITHUB_SHA"])
        replace(a.receipt,canonical(prior));print("GSF_FAILED_AT_COMPLETE_PREFIX",canonical(prior).decode().strip(),flush=True)
        raise
