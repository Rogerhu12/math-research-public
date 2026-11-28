"""Signed physical first transport from the genuine cut all the way to the waist.

One deterministic private data stream retains the complete signed first
amplitudes and invariant-label derivatives on every original or refined radial
piece and every closed angular bin. The genuine GCS and GPR inputs each have
independent whole-file identities, and no old target is counted a second time.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isfinite,nextafter,inf
import argparse,gzip,hashlib,json,os,struct,sys,time
from flint import arb,ctx
from fourfold_codazzi_true_characteristic_seed_admission import ROOT
from fourfold_codazzi_true_phase_global_validation import canonical,upper64
from fourfold_codazzi_true_phase_original_inputs import MANIFEST,CUT,admit,check
from fourfold_codazzi_true_phase_signed_speed import Inputs,scalar_model
from fourfold_codazzi_signed_density_transport_arithmetic import exact,hull
from fourfold_codazzi_true_ratio_live_rules import gate
from fourfold_codazzi_true_ratio_prefix import Prefix,record_failure,replace
from fourfold_codazzi_true_ratio_first_raw import make_direction
from fourfold_codazzi_true_ratio_label_mesh import (
    M,CELLS,angular_compose,label_jet,project_to_labels,project_to_physical,series)
from fourfold_codazzi_true_ratio_physical_packets import prepare,positive_power,values
from fourfold_codazzi_true_ratio_cut_and_reference import (
    cut_ratio,Phase,subcells,file_sha,GCS_RUN,GCS_SHA,GCS_BYTES,GCS_RECEIPT_SHA)

BOX=struct.Struct("<dd");L=struct.Struct("<I")
KEYS=("U_label","U_inward_source_label","R_plus_physical","imag_a1_positive","real_b1")


def boxes(jets):
    raw=bytearray()
    for v in jets:
        a,b=nextafter(float(v.lower()),-inf),nextafter(float(v.upper()),inf)
        check(isfinite(a) and isfinite(b) and a<=b,"complete signed finite first-ratio box")
        raw.extend(BOX.pack(a,b))
    return raw


def selected_model_inputs(root):
    import subprocess
    def read(c,p):return subprocess.check_output(["git","show",c+":"+p],cwd=root)
    args=admit((root/MANIFEST).read_bytes(),read)
    inp=Inputs(*args[:-1]);direction=make_direction(args[3])
    kmodels=[scalar_model(row["models"]["K"]) for _,_,row in args[4]]
    return inp,direction,kmodels,args[-1]


def physical_output(labels,images,p,corr,fields,meta,E):
    pulled=project_to_physical(images,labels);rplus=[]
    for i,u in enumerate(pulled):
        pjet=[arb(0)]+[p[i][j-1]/j for j in range(1,M+1)]
        v=angular_compose(u,pjet);rplus.append([a+b for a,b in zip(v,corr[i])])
    aw=[];bw=[]
    for i,r in enumerate(rplus):
        refl=(-i)%CELLS
        rminus=series([(-1)**(j+1)*v for j,v in enumerate(rplus[refl])])
        pminus=series([(-1)**j*v for j,v in enumerate(p[refl])])
        sp=series(p[i]);rp=series(r)
        A=series(fields[i][3])
        s=positive_power(series(fields[i][4])*exact(Q(3,2)),Q(1,3))
        G=E*positive_power(A,Q(1,6))/(meta["k"].sqrt().sqrt())
        plus=sp*sp*rp;minus=pminus*pminus*rminus
        aw.append(values(G*(plus+minus)/2))
        bw.append(values(G*(plus-minus)/(2*s)))
    return rplus,aw,bw


def summary(rows):
    return [max(abs(v[j]).upper() for v in rows) for j in range(M+1)]


def run(a):
    import platform
    from importlib.metadata import version
    check(os.environ["GITHUB_ACTIONS"]=="true" and os.environ["GITHUB_REPOSITORY"]=="Rogerhu12/math-research-public"
          and os.environ["GITHUB_RUN_ATTEMPT"]=="1","public first-run signed ratio owner")
    check(platform.python_version()=="3.12.14" and version("numpy")=="2.3.5" and version("python-flint")=="0.9.0",
          "same directed native runtime")
    ctx.prec=320;ctx.cap=16
    wgs=a.repo/"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json"
    wb=wgs.read_bytes();check(len(wb)==72251 and hashlib.sha256(wb).hexdigest()==
        "8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e","original complete WGS")
    wd=json.loads(wb)
    check(wd["complete"] and wd["proved"] and wd["failure"] is None and
          arb(wd["complete_higher_flow_and_cut_conclusion"]["strict_phase_lower"]["ball"]).lower()>arb(1)/27,
          "reuse the same certified positive lower for both true ray slopes")
    sb=a.seed_receipt.read_bytes()
    check(len(sb)==19866 and hashlib.sha256(sb).hexdigest()==GCS_RECEIPT_SHA,
          "entire original first successful GCS receipt")
    gs=json.loads(sb)
    check(gs["run"]==GCS_RUN and gs["attempt"]=="1" and gs["complete"] is gs["proved"] is True
          and gs["cut"]==str(CUT) and gs["private_bytes"]==GCS_BYTES and gs["private_whole_sha256"]==GCS_SHA,
          "same successful seed and private whole identity")
    pp=a.phase_receipt.read_bytes()
    check(0<len(pp)<100000 and hashlib.sha256(pp).hexdigest()==a.phase_receipt_sha,
          "complete original public GPR result")
    gpr=json.loads(pp)
    gates=("both_full_spacetime_H1_below_one_over_64","both_full_angle_H1_below_one_over_64",
           "both_strict_label_H1_below_one_over_64","strict_gap_H1_below_one_over_64")
    check(gpr["kind"]=="true_global_phase_and_common_gap_v1" and gpr["complete"] is gpr["proved"] is True
          and gpr["run"]==a.phase_run and gpr["attempt"]==1 and gpr["event_commit"]==a.phase_event
          and gpr["quantitative_gates"]==dict.fromkeys(gates,True) and gpr["physical_angle"]=="phi"
          and gpr["seed_sha256"]==GCS_SHA and gpr["seed_bytes"]==GCS_BYTES
          and gpr["original_successful_GCS_run"]==GCS_RUN+"/1",
          "only the successful complete GPR reference may enter")
    inp,z,km,receipts=selected_model_inputs(a.repo)
    plan_rows=[[str(l),str(r),k,i] for l,r,k,i in inp.plan]
    check(gpr["original_count"]==len(receipts)==176 and gpr["original_bytes"]==sum(x["bytes"] for x in receipts)
          and gpr["original_receipts_sha256"]==hashlib.sha256(canonical(receipts)).hexdigest()
          and gpr["radial_cells"]==gpr["completed_cells"]==len(plan_rows)
          and gpr["inward_plan_sha256"]==hashlib.sha256(canonical(plan_rows)).hexdigest(),
          "same whole original natural inputs and all closed ordered cells")
    rcut,pref=cut_ratio(a.seed)
    phase=Phase(a.phase,gpr["private_carrier"],inp.plan)
    rl,rh=map(Q,ROOT)
    plan=[(i,l,r) for i,(lo,hi,_,_) in enumerate(inp.plan) for l,r in subcells(lo,hi,rl)]
    check(len(plan)<=4500,"complete qualified route and memory budget")
    identity={"schema":"GRQ-1","run":os.environ["GITHUB_RUN_ID"],"attempt":1,"cut":str(inp.plan[0][1]),
              "physical_cells":CELLS,"fixed_label_cells":CELLS,"angular_order":M,
              "fields":list(KEYS),"root":list(ROOT),"source_phase_run":gpr["run"],
              "source_phase_receipt":a.phase_receipt_sha,"source_cut_run":GCS_RUN,
              "signed_continuation":"at epsilon=+, R_sigma=i*sigma*rplus(sigma*phi); a1 is i times the stored real jet",
              "storage":"per inward piece then named field then centered bin then normalized jet: little-endian real f64 lo,hi",
              "subpieces":[[i,str(l),str(r)] for i,l,r in plan]}
    root=a.private;root.mkdir(parents=True,exist_ok=True)
    path=root/"true-complete-first-ratio.bin.gz"
    maxima={k:[arb(0)]*(M+1) for k in KEYS}
    state=None;U=None;E=None;idx=-1;beg=time.monotonic();written=0;max_overlap=0
    first_source=None
    header=canonical(identity)
    base={"kind":"actual_signed_first_ray_ratio_on_complete_strict_physical_domain_v1",
          "run":os.environ["GITHUB_RUN_ID"],"attempt":1,"event_commit":os.environ["GITHUB_SHA"],
          "source_phase_run":gpr["run"],"source_phase_receipt_sha256":a.phase_receipt_sha,
          "phase_whole":gpr["private_carrier"],"seed_sha256":GCS_SHA,"seed_receipt_sha256":GCS_RECEIPT_SHA,
          "original_count":gpr["original_count"],"original_bytes":gpr["original_bytes"],
          "original_receipts_sha256":gpr["original_receipts_sha256"],"original_plan_sha256":gpr["inward_plan_sha256"],
          "plan_sha256":hashlib.sha256(canonical(identity["subpieces"])).hexdigest(),
          "header_sha256":hashlib.sha256(header).hexdigest(),"physical_subpieces":len(plan),
          "native_original_cells":len(inp.plan),"whole_old_scientific_targets_recomputed":0}
    private=Prefix(path,a.receipt,header,base)
    try:
        for count,(i,l,r) in enumerate(plan,1):
            readhead=gate()
            cell=inp.plan[i];lo,hi=cell[:2]
            if i!=idx:q,errors=phase.row();idx=i
            rho0=hull(rl-r,rh-r);rr=hull(rl-r,rh-l)
            if state is None:
                im,ps,co,_,_,state,m=prepare(inp,z,km,cell,r,r,(rho0,rho0),q,errors,arb(0),None)
                U=project_to_labels(im,[label_jet([v-u for v,u in zip(x,y)],p)
                                   for x,y,p in zip(rcut,co,ps)])
                E=pref*(-m["K"]).sqrt().sqrt()
                check(E.lower()>0,"actual positive E scalar at cut")
            tau=hull((hi-r)/(hi-lo),(hi-l)/(hi-lo))
            images,p,corr,src,fields,state,m=prepare(inp,z,km,cell,l,r,(rho0,rr),q,errors,tau,state)
            max_overlap=max(max_overlap,max(map(len,images)))
            src=project_to_labels(images,src)
            h=exact(r-l)
            right=[[v+h*w for v,w in zip(x,y)] for x,y in zip(U,src)]
            whole=[[v.union(w) for v,w in zip(x,y)] for x,y in zip(U,right)]
            Enext=E*(2*h*m["beta_mean_S"]).exp()
            Ew=E.union(Enext)
            rplus,wa,wb=physical_output(whole,images,p,corr,fields,m,Ew)
            allvals=(whole,src,rplus,wa,wb)
            row=bytearray()
            for key,vals in zip(KEYS,allvals):
                maximum=summary(vals)
                maxima[key]=[max(x,y).upper() for x,y in zip(maxima[key],maximum)]
                row.extend(b"".join(boxes(v) for v in vals))
            if count==1:first_source=[upper64(v) for v in maxima["U_inward_source_label"]]
            U,E=right,Enext
            checkpoint=dict(kind="signed_first_ratio_continuation_v1",completed=count,source_cell=i,
                            outward_left=str(l),outward_right=str(r),plan_sha256=base["plan_sha256"],
                            box_fields=["label_U[128,7]","radial_E","radial_k1","omega_lower","A1_upper[7]"],
                            format="little-endian binary64 outward real lower,upper pairs",
                            next_origin="left endpoint of just-completed physical subpiece",
                            radial_upper_fields=["A1_upper"],radial_lower_fields=["omega_lower"])
            cb=canonical(checkpoint)
            frontier=(L.pack(len(cb))+cb+b"".join(boxes(z) for z in U)+boxes([E,state["k1"],state["omega_lower"]])
                      +boxes(state["A1"]))
            aggregate={k:[upper64(v) for v in z] for k,z in maxima.items()}
            update=dict(base,completed_subpieces=count,prefix_proved=True,original_cell_index=i,
                        complete_physical_subpiece=[str(l),str(r)],current_readhead=readhead,
                        maximum_label_bin_overlap=max_overlap,all_whole_global_derivative_upper=aggregate,
                        first_source=first_source,final_label_U_upper=[upper64(v) for v in summary(U)])
            # If the rules changed during this physical cell, retain the
            # preceding fully observed prefix and let the guard report it.
            gate()
            private.append(row);private.commit(update,frontier)
            if count%32==0:
                print("GRQ_WHOLE_PREFIX",count,len(plan),round(time.monotonic()-beg,2),private.raw.hexdigest(),
                      "R0",upper64(maxima["R_plus_physical"][0]),flush=True)
                print("GRQ_COMPLETE_PREFIX_RECEIPT",a.receipt.read_text().strip(),flush=True)
    except Exception as exc:
        raise RuntimeError("subpiece "+str(count)+" of "+str(len(plan))+
                           " original cell "+str(i)+" ["+str(l)+","+str(r)+"]: "+str(exc)) from exc
    finally:
        private.close()
    written=private.usize;hh=private.raw
    phase.close()
    # Scan EVERY normalized real interval a second time, to physical EOF.
    check(written<=365_000_000 and path.stat().st_size<=365_000_000,"bounded whole private first-ratio storage")
    hr=hashlib.sha256()
    with gzip.open(path,"rb") as f:
        n=f.read(4);size,=L.unpack(n);head=f.read(size)
        check(head==header,"GRQ signed schema complete")
        hr.update(n+head)
        nrow=len(KEYS)*CELLS*(M+1)*BOX.size
        for _ in plan:
            row=f.read(nrow);check(len(row)==nrow,"whole signed ratio physical row")
            for low,high in BOX.iter_unpack(row):
                check(isfinite(low) and isfinite(high) and low<=high,"complete signed ratio readback")
            hr.update(row)
        check(not f.read(1) and hr.hexdigest()==hh.hexdigest(),"complete first-ratio private EOF and SHA")
    receipt={"kind":"actual_signed_first_ray_ratio_on_complete_strict_physical_domain_v1",
             "run":os.environ["GITHUB_RUN_ID"],"attempt":1,"event_commit":os.environ["GITHUB_SHA"],
             "complete":True,"proved":True,"input_phase_receipt":a.phase_receipt_sha,
             "phase_run":gpr["run"],"original_cut_run":GCS_RUN,"original_cut_sha":GCS_SHA,
             "physical_subpieces":len(plan),"native_original_cells":len(inp.plan),
             "physical_bins":CELLS,"fixed_label_bins":CELLS,"all_four_real_branches":True,
             "maximum_label_bin_overlap":max_overlap,"first_source":first_source,
             "all_whole_global_derivative_upper":{k:[upper64(v) for v in z] for k,z in maxima.items()},
             "final_label_U_upper":[upper64(v) for v in summary(U)],
             "private_bytes":path.stat().st_size,"private_sha256":file_sha(path),
             "private_uncompressed_bytes":written,"private_uncompressed_sha256":hh.hexdigest(),
             "old_scientific_targets_recomputed":0,"complete_genuine_B_high_response_proved":False,
             "seconds":time.monotonic()-beg}
    receipt.update(plan_sha256=base["plan_sha256"],private_continuation_available=True,
                   last_rules_read_head=gate(),completed_subpieces=len(plan))
    prior=json.loads(a.receipt.read_bytes())
    check(receipt["private_sha256"]==prior["private_prefix_sha256"] and
          receipt["private_bytes"]==prior["private_prefix_bytes"],"last whole compressed prefix identity")
    receipt.update({k:v for k,v in prior.items() if k.startswith("continuation_")})
    replace(a.receipt,canonical(receipt))
    print("GRQ_WHOLE_SMALL_RECEIPT",canonical(receipt).decode().strip(),flush=True)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for x in ("repo","private","receipt","seed","seed-receipt","phase","phase-receipt"):
        p.add_argument("--"+x,required=True,type=Path)
    for x in ("phase-receipt-sha","phase-run","phase-event"):
        p.add_argument("--"+x,required=True)
    args=p.parse_args()
    try:run(args)
    except Exception as exc:
        record_failure(args.receipt,exc)
        raise
