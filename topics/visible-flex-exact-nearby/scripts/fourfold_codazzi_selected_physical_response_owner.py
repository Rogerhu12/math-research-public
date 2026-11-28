"""First joint use of the complete GG graph and WSS forcing for actual physical observations."""
import argparse
from fractions import Fraction
import gc
from hashlib import sha1,sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys
import time
import traceback

REPO="Rogerhu12/math-research-public"
KIND="R149_actual_selected_physical_response_v1"
TARGETS=["all_193_signed_boundary_columns","both_whole_signed_affine_columns",
         "both_known_high_and_physical_returns","full_true_neighbourhood_physical_gate",
         "selected_height_and_actual_affine_responses"]
PARAMETERS=dict(original_low_dimension=193,whole_physical_source_rows=577,original_physical_source_columns=2,
    original_GG_cells=1424,original_WSS_pieces=7728,physical_cut="9/10",positive_domain=["true_root","25/8"],
    low_shell=["17/20","19/20"],negative_ordinary_window=["0","r_plus"],negative_threshold="1/200",
    full_state_radius="1e-7",outer_state_radius="9e-10",maximum_actual_bytes=95000,
    maximum_private_bytes=8589934592,maximum_aggregate_rss=15032385536,maximum_scientific_seconds=19500,
    workers=4,original_WSS_bits=320,original_GG_bits=384,old_completed_targets_recomputed=0)
RUNTIME={"python":"3.12.14","packages":{"python-flint":"0.9.0","numpy":"2.3.5"}}
BOUND=("true_low193_grassmann_owner","grassmann_validator","grassmann_math","grassmann_runner","grassmann_carriers",
       "original81_restore","grassmann_proof","true_low193_whole_child_coefficients","true_low193_direct_flow_math")
PORTS=("root_left96","root_stable","collar_Hthird","body_Hthird","body_frame_jumps","collar_frame_jumps",
       "cut_stable_jump","cut_unstable_jump","positive_low_raw_jump_sum","low_ordinary_extra",
       "extra_charted_right97","height_second_Hsixth","Robin_extra_Hsixth","mean_extra",
       "negative_root_jump_sum","negative_strict_raw_jump_sum","positive_sliver_low_jump_sum",
       "extra_negative_root_Hthird","extra_negative_strict_L2")


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def canonical(v):
    return (json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(",",":"),allow_nan=False)+"\n").encode()


def sha(raw):
    return sha256(raw).hexdigest()


def whole(root,s):
    p=(root/s["path"]).resolve()
    require(p.is_relative_to(root),"one safe immutable topic path")
    raw=p.read_bytes()
    require(len(raw)==s["bytes"] and sha(raw)==s["sha256"] and
            sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==s["git_blob_sha"],"whole "+s["path"])
    return raw


def load(root,s):
    whole(root,s)
    key="_R149_receiver_"+s["sha256"][:22]
    if key not in sys.modules:
        spec=importlib.util.spec_from_file_location(key,root/s["path"])
        module=importlib.util.module_from_spec(spec)
        sys.modules[key]=module
        spec.loader.exec_module(module)
    return sys.modules[key]


def metadata(root,manifest):
    root=Path(root).resolve()
    specs={s["role"]:s for s in manifest["files"]}
    require(len(specs)==len(manifest["files"]) and manifest["kind"]=="R149_actual_selected_physical_response_inputs_v1"
            and manifest["target_order"]==TARGETS and manifest["parameters"]==PARAMETERS
            and manifest["runtime"]==RUNTIME and manifest["repository"]==REPO,"the complete new joint scientific scope")
    content={k:whole(root,s) for k,s in specs.items()}
    d={k:json.loads(raw) for k,raw in content.items() if specs[k]["path"].endswith(".json")}
    gg,wm=d["gg_manifest"],d["wss_manifest"]
    gr,wr=({s["role"]:s for s in m["files"]} for m in (gg,wm))
    paths=set()
    for s in list(specs.values())+list(gr.values())+list(wr.values()):
        whole(root,s)
        paths.add(s["path"])
    require(len(paths)==manifest["whole_distinct_current_files"] and len(gr)==gg["expected_current_input_count"]
            and len(gg["historical_inputs"])==21 and len(wr)==19,"entire nested original closures")
    qual=load(root,gr["grassmann_validator"])
    ggargs=(content["gg_actual"],content["gg_execution"],content["gg_manifest"],dict(
        actual_spec=specs["gg_actual"],execution_spec=specs["gg_execution"],manifest_spec=specs["gg_manifest"],
        expected_reference=d["gh5_actual"]["reference_identity"],bound_definitions={k:gr[k] for k in BOUND}))
    qual.admit_success(*ggargs[:3],**ggargs[3])
    wargs=dict(owner=load(root,wr["science"]),inputs={k:content["wss_"+k] for k in ("actual","execution","manifest")},
               specs={k:specs["wss_"+k] for k in ("actual","execution","manifest")})
    load(root,specs["srr"]).admit(**wargs)
    require(specs["wss_actual"]["sha256"]=="d3135d3cf9855b2312a922c9bfd9162da3debd844855eea22668ba0d8318b16e"
            and specs["wss_execution"]["sha256"]=="fb1e7e7a828cc8a8086ecd9eb50d96bc895b194a58017271aad210cf986a563a"
            and specs["FHC"]["sha256"]=="6534bd6fb43c492db16fe563f9c1c219b30b913f58d6a3c15ee011754f3e372a"
            and specs["NPG_fees"]["sha256"]=="53f584018bb507c5dd5c34a92c5db7a58c46ff14d4b10d82aa353732261493ee"
            and d["NPG_fees"]["proved"] and d["NPG_fees"]["whole_source_sha256"]==specs["npg"]["sha256"]
            and d["NPG_fees"]["whole_proof_sha256"]==specs["NPG_proof"]["sha256"]
            and d["FHC"]["proved"] and len(d["FHC"]["checks"])==25 and all(d["FHC"]["checks"].values())
            and d["FHC"]["whole_inputs"]["NPG"]==specs["NPG_proof"]["sha256"]
            and d["FHC"]["whole_inputs"]["WHN_actual"]==specs["WHN"]["sha256"]
            and d["FHC"]["whole_inputs"]["OHR"]==specs["OHR"]["sha256"]
            and d["FHC"]["whole_inputs"]["SPN"]==specs["SPN"]["sha256"],"same selected signed source and exact downstream proof")
    for k,run in (("gh5","44736533396"),("gh4","44740105701"),("D","44745017016"),
                  ("L","44724797559"),("weighted","44746534556")):
        a,e,s=d[k+"_actual"],d[k+"_execution"],specs[k+"_actual"]
        identity=a.get("identity",a)
        require(a["complete"] and a.get("failure") is None and identity["run_id"]==e["run_id"]==run
                and identity["run_attempt"]==e["run_attempt"]=="1" and e["actual_child_returncode"]==0
                and e.get("scientific_complete",e.get("complete")) is True and e["failure"] is None
                and e["scientific_files"]==[{n:s[n] for n in ("path","bytes","sha256")}],"complete original "+k)
        if k in ("D","weighted"):
            base=d[k+"_manifest"]
            require(identity["manifest_sha256"]==e["manifest_sha256"]==specs[k+"_manifest"]["sha256"]
                and a["scientific_modules"]==base["operation"]["scientific_module_binding"]
                and a["complete_current_file_receipts"]==e["current_input_receipts"]==base["files"]
                and sorted(a)==base["operation"]["scientific_field_names"]
                and [v["name"] for v in a["gates"]]==base["operation"]["complete_gate_names"]
                and all(v["passed"] is True for v in a["gates"]),"source and native scope of complete "+k)
    load(root,specs["high_admit"]).admit_original_high_reports(d["base0"],d["base0_process"],d["negative"],
        d["negative_process"],specs["base0"],specs["negative"])
    require(not any(k in sys.modules for k in ("numpy","flint","scipy")),"all whole qualifications before numerical import")
    return specs,content,d,gr,wr,ggargs,wargs


def validate(doc,manifest):
    n=len(doc["completed_targets"])
    require(doc["kind"]==KIND and doc["parameters"]==PARAMETERS and doc["completed_targets"]==TARGETS[:n]
            and list(sorted(doc["conclusions"]))==sorted(TARGETS[:n]) and n<=len(TARGETS)
            and doc["old_completed_targets_recomputed"]==0 and doc["new_arrays_published"]==0
            and not doc["actual_global_port_matching_verified"] and not doc["final_nonlinear_family_proved"]
            and doc["whole_input_list_sha256"]==sha(canonical(manifest["files"])),"actual full signed response prefix")
    if doc["complete"]:
        require(doc["failure"] is None and doc["actual_returncode"]==0 and
             (n==5 or n==4 and not doc["conclusions"][TARGETS[3]]["physical_gate_passed"]),
             "complete new observed mathematical branch")
    return doc


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","manifest","out","private","rows-index","native","native-receipts","candidate-index",
              "centre-repair","root-germ","root-budget"):
        parser.add_argument("--"+k,type=Path,required=True)
    for k in ("manifest-sha","checkout"):
        parser.add_argument("--"+k,required=True)
    parser.add_argument("--preflight-only",action="store_true")
    parser.add_argument("--source-only",action="store_true")
    a=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","the one original first public entry")
    root=a.repo.resolve()
    raw=a.manifest.read_bytes()
    require(sha(raw)==a.manifest_sha,"entire frozen joint manifest")
    manifest=json.loads(raw)
    specs,contents,d,gr,wr,ggargs,wargs=metadata(root,manifest)
    require(sha(Path(__file__).read_bytes())==specs["science"]["sha256"],"actual scientific owner")
    ggload=lambda k:load(root,gr[k])
    new=lambda k:load(root,specs[k])
    owner=ggload("true_low193_grassmann_owner")
    core,readonly=ggload("readonly_core"),ggload("readonly_admission")
    native=readonly.admit(root,root/specs["gg_manifest"]["path"],specs["gg_manifest"]["sha256"],
        a.native,a.native_receipts,a.candidate_index,a.centre_repair,a.root_germ,a.root_budget,core)
    sr=new("srr")
    original=sr.preflight(**wargs,root=root,old_rows_index=a.rows_index)
    require(len(native["admission"]["checks"])==18 and all(g["passed"] for g in native["admission"]["checks"]),
            "all original 18 native/repair/operator qualifications")
    old_data=lambda k:json.loads(whole(root,gr[k]))
    signed=old_data(owner.SL_ACTUAL_ROLE)
    plan,counts=owner.read_prior_plan(old_data(owner.PRIOR_ACTUAL_ROLE),old_data(owner.PRIOR_EXECUTION_ROLE),
                                      signed,old_data(owner.SL_EXECUTION_ROLE))
    restore=ggload("original81_restore")
    tf=restore.admit_complete_original(*(whole(root,gr[k]) for k in
        ("original_TF_failure_actual","original_TF_failure_execution","original_TF_manifest")))
    if a.preflight_only:
        print(json.dumps(dict(ready=True,native_checks=18,gg_inputs=len(gr),gg_history=21,wss_inputs=len(wr),
            original_source_identity=original[-1],complete_original_cells=sum(counts),old_and_new_science_calls=0)))
        return 0
    field=load(root,wr["carrier"])
    carriers=ggload("grassmann_carriers")
    runner=ggload("grassmann_runner")
    deadline=float(os.environ["GSA_JOB_MONOTONIC_START"])+PARAMETERS["maximum_scientific_seconds"]
    index_file=a.private/"source-index.json"
    if a.source_only:
        require(not a.private.exists() and not index_file.exists(),"fresh original-only recovery in WSS runtime")
        a.private.mkdir(parents=True)
        import numpy as np
        import flint
        require(os.environ.get("OPENBLAS_CORETYPE")=="Haswell" and len(os.sched_getaffinity(0))>=4,
                "actual original WSS process and four-worker support")
        flint.ctx.prec=320
        sampled=[0.,0,0]
        def check(workers):
            now=time.monotonic()
            sampled[1]=max(sampled[1],carriers.aggregate_rss_bytes(workers))
            if now-sampled[0]>=5:
                sampled[2]=max(sampled[2],runner.private_bytes((a.private.parent,root.parent,a.native.parent)))
                sampled[0]=now
            require(now<deadline and sampled[1]<=PARAMETERS["maximum_aggregate_rss"] and
                    sampled[2]<=PARAMETERS["maximum_private_bytes"],"original full recovery within the joint budget")
        storage,rows,receipt=sr.restore(**wargs,root=root,old_rows_index=a.rows_index,directory=a.private/"sources",
            np=np,flint=flint,admitted=original,budget=check,progress=lambda k,v:print(k,flush=True),wall_deadline=deadline)
        source_plan=[[j,k,str(l),str(r)] for j,k,l,r in storage.plan]
        value=dict(plan=source_plan,records=[storage.records[i] for i in range(len(source_plan))],receipt=receipt,
            whole_WSS_plan_sha256=sha(canonical(source_plan)),resource_peaks={"rss":sampled[1],"disk":sampled[2]})
        b=canonical(value)
        index_file.write_bytes(b)
        require(index_file.read_bytes()==b,"whole original carrier index on same job private disk")
        return 0
    require(not a.out.exists() and index_file.is_file(),"unique new positive scientific result after same-job WSS")
    idx=json.loads(index_file.read_bytes())
    expected=d["wss_actual"]["new_records"][wargs["owner"].TARGETS[0]]
    require(sha(canonical(idx["plan"]))==idx["whole_WSS_plan_sha256"]==d["wss_actual"]["plan"]["canonical_sha256"]
            and len(idx["records"])==len(idx["plan"])==PARAMETERS["original_WSS_pieces"]
            and idx["receipt"]["original_whole_packet"]==expected
            and idx["receipt"]["actual"]==specs["wss_actual"]["sha256"]
            and idx["receipt"]["execution"]==specs["wss_execution"]["sha256"],"whole WSS plus its physical partition")
    storage=object.__new__(field.SignedSourceStore)
    storage.directory=a.private/"sources"/"signed"
    storage.plan=[(j,k,Fraction(l),Fraction(r)) for j,k,l,r in idx["plan"]]
    storage.ends=[r for _,_,_,r in storage.plan]
    storage.records=dict(enumerate(idx["records"]))
    require(storage.receipt()==expected,"whole original private index and all actual signed source bytes across runtimes")
    receipt,previous_peaks=idx["receipt"],idx["resource_peaks"]
    rows=original[-2]
    del original,idx
    doc=dict(kind=KIND,identity=dict(run_id=os.environ["GITHUB_RUN_ID"],run_attempt="1",
        event_commit=os.environ["GITHUB_SHA"],actual_checkout=a.checkout,manifest_sha256=a.manifest_sha,
        source_sha256=specs["science"]["sha256"]),parameters=PARAMETERS,whole_input_list_sha256=sha(canonical(manifest["files"])),
        complete=False,actual_returncode=None,failure=None,stage="all_whole_actuals_preflighted",completed_targets=[],
        conclusions={},record_bounds={},carrier_recovery={},actual_resource_peaks=previous_peaks,
        geometric_and_global_remaining_ports=list(PORTS)+["selected_cut_explicit_L2","external_added_far_height",
            "whole_waist_holonomy","two_period_rows","actual_absolute_placement","same_world_height_span"],
        actual_global_port_matching_verified=False,final_nonlinear_family_proved=False,
        new_arrays_published=0,old_completed_targets_recomputed=0,progress=None)
    start=time.monotonic()
    last=[0.,0.]
    def save():
        doc["seconds"]=time.monotonic()-start
        validate(doc,manifest)
        body=canonical(doc)
        require(len(body)<=PARAMETERS["maximum_actual_bytes"],"bounded complete small scientific outcome")
        tmp=a.out.with_suffix(".tmp")
        tmp.write_bytes(body)
        require(tmp.read_bytes()==body,"whole scientific outcome/prefix readback")
        tmp.replace(a.out)
        last[0]=time.monotonic()
    def budget(processes=()):
        now=time.monotonic()
        import multiprocessing
        active={p.pid:p for p in list(multiprocessing.active_children())+list(processes)}
        peaks=doc["actual_resource_peaks"]
        peaks["rss"]=max(peaks["rss"],carriers.aggregate_rss_bytes(active.values()))
        if now-last[1]>5:
            peaks["disk"]=max(peaks["disk"],runner.private_bytes((a.private.parent,a.native.parent,a.rows_index.parent,root)))
            last[1]=now
        require(peaks["disk"]<=PARAMETERS["maximum_private_bytes"] and peaks["rss"]<=PARAMETERS["maximum_aggregate_rss"]
                and now<deadline,"one full private/native and process-fleet budget")
    def progress(stage,detail):
        budget()
        if time.monotonic()-last[0]>=30:
            info={k:v for k,v in detail.items() if v is None or type(v) in (bool,int,str)}
            doc["progress"]={"stage":stage,"detail":info}
            save()
            print(json.dumps(doc["progress"]),flush=True)
    def finish(name,record):
        require(name==TARGETS[len(doc["completed_targets"])],"one natural irreversible target in original order")
        doc["conclusions"][name]=record
        doc["completed_targets"].append(name)
        doc["stage"]=name
        save()
    save()
    try:
        import flint
        import numpy as np
        require(platform.python_version()==RUNTIME["python"] and flint.__version__=="0.9.0" and np.__version__=="2.3.5"
                and len(os.sched_getaffinity(0))>=4 and all(os.environ.get(k)=="1" for k in
                   ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")),"original arithmetic, four CPU and one thread")
        flint.ctx.prec=320
        doc["carrier_recovery"]["WSS"]=receipt
        gc.collect()
        save()
        api=ggload("science").NumericalAPI(flint)
        km,assembly,reference,collar,green,refined,child,flow,mathmod=(ggload(k) for k in ("kernel_math",
            "assembly_math","reference_math","collar_math",owner.GREEN_ROLE,owner.REFINED_ROLE,owner.CHILD_ROLE,
            owner.FLOW_ROLE,"grassmann_math"))
        old={}
        for k,v in native["same_operator_records"].items():
            if k in ("G_c","L_c_raw"):
                f=Fraction(v)
                ball=api.rational(f.numerator,f.denominator)
            else:
                ball=api.old_interval(v)
            old[k]=api.upper(ball)
        require(len(old)==29,"all original same29 records")
        context=assembly.prepare_complete_kernel_context(api,km,reference,collar,native,
            native["completed_tracefree_inputs"]["complete_original_candidate"],old,core.signed_display_centre,progress)
        require(context.reference_identity==signed["reference_identity"]==d["gg_actual"]["reference_identity"]
                and len(context.domain.cells)==155 and context.parent_definition_count==153
                and context.original_body_row_count==4650 and context.original_intersection_count==4801,
                "whole actual same-operator input")
        flint.ctx.prec=384
        rc=refined.RefinedContext(context,counts)
        balances=[refined.exact_float(api,r[3]) for r in plan]
        charts=refined.prepare_chart_specs(api,context,rc,progress)
        provider=child.WholeChildSignedCoefficientProvider(api,km,green,assembly,collar,native,context,rc,rc.domain.to_parent_box)
        e=mathmod.Engine(api,km,green,flow)
        model,graph_receipt=new("grr").restore_graph(np=np,flint=flint,engine=e,math_module=mathmod,carriers=carriers,
            runner=runner,restore=restore,green=green,refined=refined,flow=flow,context=rc,provider=provider,
            charts=charts,balances=balances,tf_admission=tf,gg_validator=ggload("grassmann_validator"),gg_inputs=ggargs,
            private_directory=a.private/"graphs",native_directory=a.native.parent,progress=progress,wall_deadline=deadline)
        doc["carrier_recovery"]["GG"]=graph_receipt
        save()
        def pub(x):
            if hasattr(x,"mid_rad_10exp"):
                return x.str(48)
            if isinstance(x,dict):
                return {k:pub(v) for k,v in x.items() if k!="private_model_token"}
            if isinstance(x,(list,tuple)):
                return [pub(v) for v in x]
            require(x is None or type(x) in (int,str,float,bool),"public small scalar or receipt")
            return x
        def emit(name,point,sense):
            require(sense in ("upper","lower") and name not in doc["record_bounds"],"unique complete scientific scalar")
            record={"bound":sense,"ball":point.str(48)}
            v=api.arb(record["ball"])
            require(v.contains(point),"outward scalar representation includes its actual endpoint")
            doc["record_bounds"][name]=record
            return v.upper() if sense=="upper" else v.lower()
        bs=carriers.DiskJointStore(e,mathmod,a.private/"boundary")
        ps=carriers.DiskJointStore(e,mathmod,a.private/"particular")
        boundary=new("gbc").solve(engine=e,model=model,provider=provider,balances=balances,
            graph_math=mathmod,output_store=bs,budget=budget,progress=progress)
        finish(TARGETS[0],pub(boundary))
        field=load(root,wr["carrier"])
        sar=new("sar")
        part=sar.source_columns(engine=e,model=model,provider=provider,balances=balances,graph_math=mathmod,
            carriers=carriers,gsr=new("gsr"),field=field,source_store=storage,source_expected=receipt["original_whole_packet"],
            rows=rows,read_ball=lambda r:field.historical_ball(flint,r),work_store=ps,budget=budget,progress=progress,deadline=deadline)
        finish(TARGETS[1],pub(part))
        gtp=new("gtp")
        admitted=gtp.admit_complete_inputs(api,d["gg_actual"],d["gg_execution"],d["gh5_actual"],d["gh5_execution"],
            d["gh4_actual"],d["gh4_execution"],d["D_actual"],d["D_execution"],d["L_actual"],d["L_execution"],
            d["negative"],weighted=d["weighted_actual"],weighted_execution=d["weighted_execution"])
        ret=sar.actual_known_high_returns(engine=e,model=model,provider=provider,particular=part,part_store=ps,
            boundary=boundary,boundary_store=bs,gtp=gtp,admitted=admitted,ohr_raw=contents["OHR"],wob_raw=contents["WOB"],
            emit=emit,budget=budget)
        finish(TARGETS[2],pub({k:ret[k] for k in ("kind","source_index","actual_affine_independent_observations",
            "complete_cut_trace_arc_gains","authentic_fourth_and_raw_GG_maps_retained","independent_mean_retained")}))
        npg=new("npg")
        # These exact rational combinations were already completed on the pinned source.
        # Its sole fees() dependency now reads that original successful whole instead.
        npg.fees=lambda:dict(d["NPG_fees"]["complete_raw_and_distributional_fees"])
        gate=npg.numerical_gate(engine=e,model=model,admitted=admitted,boundary=boundary,boundary_store=bs,gtp=gtp,
            outer_raw=contents["outer"],SPN_raw=contents["SPN"],WHN_raw=contents["WHN"],whn_spec=specs["WHN"],
            radius=PARAMETERS["full_state_radius"],emit=emit)
        finish(TARGETS[3],pub(gate))
        if gate["physical_gate_passed"]:
            # Both independent signed affine constants, all other inputs supplied by the global matching layer.
            # Zero here is the origin of that linear input space. It is not evidence for a zero actual port.
            results={}
            for column in ("Newton","nu"):
                result=new("fhc").close(engine=e,model=model,admitted=admitted,gate=gate,boundary=boundary,particular=part,
                    npg=npg,fhc_raw=contents["FHC"],fhc_spec=specs["FHC"],oa_raw=contents["OA"],ohr_raw=contents["OHR"],
                    state_radius="0",inputs={k:api.zero for k in PORTS},column=column,explicit_cut_L2=api.zero,
                    external_height=api.zero,cut_entry=None,emit=emit)
                results[column]=pub(result)
            independent=None
            if result["complete_selected_height_loop_passed"]:
                def endpoint(port,item,value):
                    signed=value.upper()
                    ball=api.arb(signed.str(40))
                    require(ball.contains(signed),"whole directed independent output "+port+" "+item)
                    return signed.str(40)
                independent=new("independent").complete(engine=e,model=model,admitted=admitted,gate=gate,
                    boundary=boundary,fields=PORTS,selected=result,emit=endpoint)
            finish(TARGETS[4],dict(selected_affine_constants=results,whole_independent_response=independent,
                other_inputs_are_independent_coordinates=True,actual_global_values_substituted=False))
        doc.update(complete=True,actual_returncode=0,stage="whole_observed_physical_branch")
        save()
        return 0
    except BaseException as exc:
        doc.update(complete=False,actual_returncode=1,stage="terminal_actual_failure_with_whole_natural_prefix",
            failure=dict(type=type(exc).__name__,message=str(exc)[:1600],traceback=traceback.format_exc()[-5500:]))
        save()
        print(traceback.format_exc(),flush=True)
        return 1


if __name__=="__main__":
    sys.exit(main())
