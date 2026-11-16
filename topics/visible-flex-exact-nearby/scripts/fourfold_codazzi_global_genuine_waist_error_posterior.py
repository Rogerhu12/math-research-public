"""One new public calculation: complete global genuine waist-error posterior.
Every completed natural graph is saved independently before its successors.
No old producer, ODE, profile or successful scientific target is executed.
"""
from __future__ import annotations
import argparse, ast, copy, hashlib, importlib.metadata, importlib.util
import json, os, sys, time, traceback
from pathlib import Path
from flint import ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby"
KIND="complete_global_genuine_waist_error_posterior_v1"
ENVELOPE_KIND="WEJ_complete_atomic_node_v1"
WHOLE_NODE="complete_same_physical_whole_and_reduced_error"
SCIENTIFIC_ROLES=("posterior_support","posterior_residual","posterior_endpoint",
                  "posterior_pipeline","posterior_admission")

def compact(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def require(condition,message):
    if not condition:
        raise ValueError(message)

def write_atomic(path,document):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=compact(document);tmp=path.with_name(path.name+".partial")
    tmp.write_bytes(raw);tmp.replace(path)
    return raw

def emit_file(relative,raw):
    print("BEGIN_COMPLETE_WEJ_FILE "+relative,flush=True)
    sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
    if not raw.endswith(b"\n"):print("",flush=True)
    print("END_COMPLETE_WEJ_FILE "+relative,flush=True)

def load_new_module(path,name,expected):
    raw=Path(path).read_bytes()
    require(sha(raw)==expected,"new module byte identity changed: "+name)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def complete_whole_error(api,original,negative,endpoints,publish_graph):
    rows={}
    def put(name,value):
        rows[name]=api.record(value)
        return api.read_up(rows[name])
    old=copy.deepcopy({k:original[k] for k in
        ("Calg","Rplus","RF","KHinv_L2","Ni_Hminus4_3","D_infinity")})
    alg,rp,rf,kh,ni,di=(api.read_up(old[k]) for k in
        ("Calg","Rplus","RF","KHinv_L2","Ni_Hminus4_3","D_infinity"))
    cn=negative["C_negative"];ce=endpoints["Cend"]
    invsqrt2=put("complete_inverse_sqrt_two_upper",api.ex(1)/api.ex(2).sqrt())
    left=put("complete_final_left_readout_upper",kh*invsqrt2)
    ordered=put("complete_left_readout_times_right_input_upper",left*ni)
    nonroot=put("complete_positive_negative_endpoint_sum_upper",rp+cn+ce)
    allsource=put("complete_positive_root_negative_endpoint_sum_upper",nonroot+rf)
    received=put("complete_received_whole_trial_error_upper",ordered*allsource)
    whole=put("complete_same_physical_whole_error_upper",alg+received)
    reduced_received=put("complete_received_error_after_exact_root_factor_upper",
                         ordered*nonroot)
    reduced=put("complete_infinite_error_after_exact_finite_factors_upper",
                di+reduced_received)
    doc={
      "kind":WHOLE_NODE,"complete":True,
      "complete_original_records":old,
      "complete_new_records":rows,
      "complete_received_negative_predecessor":"negative_reception",
      "complete_endpoint_predecessor":"complete_four_waist_endpoint_contributions",
      "whole_identity":"Calg+(KHinv_L2/sqrt(2))*Ni_Hminus4_3*(Rplus+RF+Cnegative+Cend)",
      "reduced_identity":"D_infinity+(KHinv_L2/sqrt(2))*Ni_Hminus4_3*(Rplus+Cnegative+Cend)",
      "same_operator_domain":"Xfr -> P Fix(R_a), input H^(-4/3), output normalized physical L2 waist row",
      "exact_finite_parts_retained_in_auxiliary_border":[
          "WFR complete root trace factor with its full input/output columns",
          "WCF complete FJ term and both primitive ranks",
          "WCF -(h-1)*rho_i and +(h-1)*ell2"],
      "true_physical_96_columns_and_all_Theta_cross_blocks_retained":True,
      "physical_two_means_nu_and_infinite_radial_head_retained":True,
      "root_factor_auxiliary_dimension_is_not_physical_dimension":True,
      "whole_Calg_not_replaced_by_D_infinity":True,
      "the_reduced_bound_keeps_every_exact_finite_factor":True,
      "original_CG_ST4_and_coordinate_factors_not_multiplied_twice":True,
      "new_whole_and_reduced_norms_only":True,
      "passing_high_cutoff_proved":False,
      "finite_Schur_inverse_proved":False,
      "full_incoming_inverse_proved":False,
      "full_nonlinear_background_proved":False,
      "final_surface_proved":False,
      "old_scientific_calls":0}
    saved=publish_graph(WHOLE_NODE,doc)
    require(saved==doc,"whole graph publication changed its exact JSON")
    return decode_whole_error_node(saved,api),saved

def decode_whole_error_node(saved,api):
    """Pure saved-record reader; never evaluates the complete error target."""
    require(saved.get("kind")==WHOLE_NODE and saved.get("complete") is True,
            "not the complete same-physical whole and reduced error node")
    require(saved["whole_Calg_not_replaced_by_D_infinity"] is True and
            saved["the_reduced_bound_keeps_every_exact_finite_factor"] is True,
            "an exact finite obligation was omitted")
    return {k:api.read_up(v) for k,v in saved["complete_new_records"].items()}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--manifest-sha",required=True)
    ap.add_argument("--bits",type=int,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    raw=args.manifest.read_bytes()
    require(sha(raw)==args.manifest_sha,"immutable posterior manifest changed")
    m=json.loads(raw)
    require(m["kind"]=="complete_WEJ_posterior_current_input_manifest_v1",
            "wrong complete posterior manifest")
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
            os.environ.get("GITHUB_REPOSITORY")==PUBLIC,"public own Actions only")
    require(args.bits==320 and m["parameters"]["arithmetic_bits"]==320,
            "different directed precision")
    runtime={"Python":sys.version.split()[0],
             "python_flint":importlib.metadata.version("python-flint")}
    require(runtime==m["scientific_runtime"],"different scientific runtime")
    require(m["historical_inputs"]==[],"posterior cannot restore old binaries")
    files={p["role"]:p for p in m["files"]}
    require(len(files)==len(m["files"]),"duplicate complete input roles")
    root=args.repo.resolve();out=args.out_dir.resolve()
    out.mkdir(parents=True,exist_ok=True)
    require(not (out/"index.json").exists(),"fresh output path required; never overwrite a prior attempt")
    code={}
    for role,spec in files.items():
        path=Path(spec["path"])
        require(not path.is_absolute() and ".." not in path.parts and
                str(path).startswith(TOPIC+"/"),"one input escaped the topic")
        rr=(root/path).read_bytes()
        require(len(rr)==spec["bytes"] and sha(rr)==spec["sha256"],
                "one immutable input differs before imports: "+role)
        if str(path).endswith(".py"):
            ast.parse(rr.decode("utf-8"),filename=str(path))
        code[role]=root/path
    require(sha(Path(__file__).read_bytes())==files["posterior_pipeline"]["sha256"],
            "actual scientific source differs")
    admission=load_new_module(code["posterior_admission"],"new_WEJ_admission",
                              files["posterior_admission"]["sha256"])
    ctx.prec=320
    api=load_new_module(code["posterior_support"],"new_WEJ_support",
                       files["posterior_support"]["sha256"])
    residual=load_new_module(code["posterior_residual"],"new_WEJ_residual",
                            files["posterior_residual"]["sha256"])
    endpoint=load_new_module(code["posterior_endpoint"],"new_WEJ_endpoint",
                            files["posterior_endpoint"]["sha256"])
    contract=json.loads(code["posterior_admission_contract"].read_bytes())
    require(contract["kind"]=="complete_WEJ_original_actual_admission_contract_v1",
            "different full original admission contract")
    for key in ("original_actual_inputs","consumed_original_records","complete_old_conclusions"):
        require(key not in m,"duplicate original admission contract field")
        m[key]=contract[key]
    params=m["parameters"];specs=[]
    for spec in m["ordered_node_specs"]:
        model=json.loads(code[spec["schema_role"]].read_bytes())
        full=dict(spec)
        full["conclusion_shape"]=model["complete_conclusion_shapes"][spec["conclusion_shape_key"]]
        specs.append(full)
    require(len({s["node_name"] for s in specs})==len(specs),"duplicate scientific node")
    byname={s["node_name"]:s for s in specs}
    input_sha={role:files[role]["sha256"] for role in m["old_actual_input_roles"]}
    module_sha={role:files[role]["sha256"] for role in SCIENTIFIC_ROLES}
    state={
      "kind":KIND,"complete":False,"proved":False,"actual_returncode":None,"failure":None,
      "public_repository":PUBLIC,"run_id":os.environ["GITHUB_RUN_ID"],
      "run_attempt":os.environ["GITHUB_RUN_ATTEMPT"],
      "workflow_event_commit":os.environ["GITHUB_SHA"],
      "actual_scientific_checkout_commit":os.environ["ACTUAL_CHECKOUT_COMMIT"],
      "source_sha256":files["posterior_pipeline"]["sha256"],
      "scientific_module_sha256":module_sha,
      "input_manifest_sha256":args.manifest_sha,
      "parameters":copy.deepcopy(params),"parameters_sha256":sha(compact(params)),
      "mathematical_input_sha256":input_sha,"runtime":runtime,"arithmetic_bits":320,
      "gates":[],"node_receipts":[],"original_input_files":[],
      "locked_attempted_nodes":[],"active_node":None,"stage":"admission",
      "actual_progress":[],"actual_mathematical_wall_seconds":None,
      "old_scientific_calls":0,"old_binary_parts_restored":0,
      "new_reproducible_arrays_persisted":False,"new_artifacts":0,"new_Releases":0,
      "retained_scope":copy.deepcopy(m["retained_scope"])}
    require(len(state["actual_scientific_checkout_commit"])==40 and
            all(c in "0123456789abcdef" for c in state["actual_scientific_checkout_commit"]),
            "actual scientific checkout is not an exact Git commit")
    completed={};saved_documents={};bindings={};progress={}
    def checkpoint(stage=None,emit=False):
        if stage is not None:state["stage"]=stage
        payload=write_atomic(out/"index.json",state)
        if emit:emit_file("index.json",payload)
    def gate(name,passed=True):
        require(passed,name)
        state["gates"].append({"name":name,"passed":True})
        checkpoint()
    def binding_for(name):
        spec=byname[name]
        dependencies={}
        for dep in spec["dependency_names"]:
            require(dep in completed,"unpaid complete predecessor: "+dep)
            dependencies[dep]=copy.deepcopy(completed[dep])
        return {
          "problem_id":m["problem_id"]+"/"+name,
          "parameters_sha256":state["parameters_sha256"],
          "mathematical_input_sha256":copy.deepcopy(input_sha),
          "scientific_module_sha256":copy.deepcopy(module_sha),
          "direct_dependency_receipts":dependencies}
    def publish_envelope(name,payload):
        require(name==state["active_node"] and name in byname,"different active scientific node")
        require(name not in completed,"a completed scientific node cannot be overwritten")
        require(payload.get("kind")==ENVELOPE_KIND and payload.get("node_name")==name and
                payload.get("binding")==bindings[name],"scientific node binding differs")
        spec=byname[name];relative=spec["relative_path"]
        require(relative=="graphs/"+name+".json","different fixed scientific path")
        data=write_atomic(out/relative,payload)
        emit_file(relative,data)
        # Science is durable and fully printed before any output-format gate.
        if payload["complete"] is True:
            completed[name]={"file":relative,"bytes":len(data),"sha256":sha(data)}
            saved_documents[name]=copy.deepcopy(payload["conclusion"])
            state["node_receipts"].append({"node_name":name,**completed[name]})
            state["actual_progress"].append({"node_name":name,"complete_file_saved":True})
            checkpoint()
            require(admission.finite_shape(payload["conclusion"],spec["conclusion_shape"]),
                    "full scientific graph differs from frozen complete shape: "+name)
            require(admission.ball_count(payload["conclusion"])==spec["record_count"],
                    "full scientific graph record count differs: "+name)
            require(len(data)<=spec["publication_max_bytes"] and len(data)<100000,
                    "full node preserved before its publication size gate: "+name)
            gate("complete natural scientific node "+name)
        else:
            checkpoint()
        readback=json.loads((out/relative).read_bytes())
        require(readback==payload,"atomic complete JSON readback differs")
        return readback
    def begin_node(name):
        require(name not in state["locked_attempted_nodes"],"an attempted node cannot be repeated")
        index=len(state["locked_attempted_nodes"])
        require(index<len(specs) and specs[index]["node_name"]==name,
                "scientific node order differs from the complete frozen DAG")
        bindings[name]=binding_for(name)
        state["active_node"]=name;state["locked_attempted_nodes"].append(name)
        checkpoint("evaluating "+name)
        publish_envelope(name,{"kind":ENVELOPE_KIND,"node_name":name,
            "binding":copy.deepcopy(bindings[name]),"complete":False,
            "printed_record_events":[],"conclusion":None,"explicit_math_prefix":None,
            "failure":None,"automatic_retry_authorized":False})
    def tail_node(name,producer,decoder):
        begin_node(name)
        result=api.evaluate_declared_node(name,bindings[name],producer,decoder,publish_envelope)
        require(name in completed,"whole natural graph not saved")
        state["active_node"]=None;checkpoint()
        return result
    def publishing_node(name,producer):
        begin_node(name)
        require(api._ACTIVE_RECORD_CAPTURE is None,"nested scientific record capture")
        capture={"records":[]};math_published=False
        def prefix(event=None,failure=None,returned=None,explicit=None):
            if name in completed:return
            publish_envelope(name,{"kind":ENVELOPE_KIND,"node_name":name,
                "binding":copy.deepcopy(bindings[name]),"complete":False,
                "printed_record_events":copy.deepcopy(capture["records"]),
                "conclusion":copy.deepcopy(returned),
                "explicit_math_prefix":copy.deepcopy(explicit),
                "failure":failure,"automatic_retry_authorized":False})
        capture["on_record"]=prefix;api._ACTIVE_RECORD_CAPTURE=capture
        def bare_callback(callback_name,doc):
            nonlocal math_published
            require(callback_name==name,"bare producer changed its scientific node")
            issued={e["record"]["ball"] for e in capture["records"]}
            require(issued.issubset(api.all_saved_ball_strings(doc)),
                    "one computed scientific record missing from complete graph")
            payload={"kind":ENVELOPE_KIND,"node_name":name,
              "binding":copy.deepcopy(bindings[name]),"complete":True,
              "printed_record_event_count":len(capture["records"]),
              "all_printed_records_in_complete_conclusion":True,
              "conclusion":copy.deepcopy(doc),"failure":None,
              "automatic_retry_authorized":False}
            saved=publish_envelope(name,payload);math_published=True
            return copy.deepcopy(saved["conclusion"])
        try:
            work,doc=producer(bare_callback)
            require(math_published and saved_documents[name]==doc,
                    "bare producer did not preserve its whole graph")
        except BaseException as error:
            if name not in completed:
                prefix(failure={"type":type(error).__name__,"message":str(error)},
                       returned=locals().get("doc"),
                       explicit=progress.get(name,getattr(error,"complete_new_prefix",None)))
            raise
        finally:
            api._ACTIVE_RECORD_CAPTURE=None
        state["active_node"]=None;checkpoint()
        return work
    try:
        checkpoint(emit=True)
        gate("actual public directed runtime and immutable new AST closure")
        docs,receipts,oldbindings=admission.read_current_inputs(root,m)
        require(len(oldbindings)==12,"twelve complete old actual input files are required")
        records,originals,oldconclusions=admission.original_records_and_conclusions(docs,m)
        gate("all twelve original actual files retain complete identities schemas gates and scopes")
        admission.verify_WGS_pair(docs)
        q=admission.verify_analytic_admission(docs,records,api)
        q["waist"]["complete_WGS_pair_admitted"]=True
        handoff=api.readonly_WGS_handoff(docs["WGS_main"],docs["WGS_original_inputs"],True)
        input_documents=admission.complete_input_documents(
            docs,receipts,oldbindings,originals,oldconclusions,m)
        for filename,document in zip(m["original_input_filenames"],input_documents):
            payload=write_atomic(out/filename,document);emit_file(filename,payload)
            state["original_input_files"].append({
                "file":filename,"bytes":len(payload),"sha256":sha(payload)})
            checkpoint()
            require(len(payload)<100000,"complete original admission file reaches100KB")
        gate("complete immutable WGS pair and original same-domain qualification admitted")
        gate("both complete original-admission documents saved before new mathematics")
        bridge=tail_node("mean_gamma_bridge",
          lambda:api.full_input_mean_gamma_bridge(records["FA2_cut_mean"],
                    handoff["local_c"],q["mean_bridge"]),api.decode_bridge_conclusion)
        extension=tail_node("extension_scalars",
          lambda:api.complete_extension_scalars(True),api.decode_extension_conclusion)
        extended={}
        for patch in ("strict","local"):
            extended[patch]=tail_node("extended_amplitude_"+patch,
              lambda patch=patch:api.complete_extended_amplitude_patch(
                  handoff["patches"][patch],extension),api.decode_extended_patch_conclusion)
        physical={}
        def physical_producer(patch):
            if patch=="strict":
                p,d,eta=api.strict_physical_primitives(handoff["old"],
                                                       handoff["strict_saved_coefficients"])
            else:
                p,d,eta=api.local_physical_primitives(handoff["local_c"],bridge)
            return api.complete_physical_patch(p,d,eta)
        for patch in ("strict","local"):
            physical[patch]=tail_node("physical_coefficients_"+patch,
              lambda patch=patch:physical_producer(patch),api.decode_physical_patch_conclusion)
        same_J={}
        local_old={"same_full_germ_even0_to_odd":True,
                   "J0":records["local_J0"],"L0":records["local_L0"]}
        for patch in ("strict","local"):
            same_J[patch]=tail_node("same_angular_J_"+patch,
              lambda patch=patch:api.complete_same_J_patch(physical[patch],
                handoff["old"][patch+"_eta_lower"],None if patch=="strict" else local_old),
              api.decode_same_J_conclusion)
        jost=tail_node("Jost_scalars",
          lambda:api.complete_Jost_scalars(extension),api.decode_Jost_conclusion)
        geometry={}
        for patch in ("strict","local"):
            geometry[patch]=tail_node("profile_geometry_"+patch,
              lambda patch=patch:api.complete_profile_geometry(
                handoff["patches"][patch],patch,handoff["old"]["whole_t_over_rho_lower"],
                handoff["old"]["strict_phase_lower"],handoff["old_fold"]),
              lambda doc,patch=patch:api.decode_profile_geometry_conclusion(
                doc,handoff["old"]["whole_t_over_rho_record"],
                api.ordinary(handoff["patches"][patch]["T"])))
        profiles={}
        for patch in ("strict","local"):
            profiles[patch]=tail_node("profile_block_"+patch,
              lambda patch=patch:api.complete_profile_patch(
                handoff["patches"][patch],geometry[patch],extension,jost),
              api.decode_profile_conclusion)
        kernels={}
        for patch in ("strict","local"):
            kernels[patch]=tail_node("mean_kernel_"+patch,
              lambda patch=patch:api.complete_mean_kernel_patch(physical[patch],same_J[patch]),
              api.decode_mean_kernel_conclusion)
        means={}
        for patch in ("strict","local"):
            means[patch]=tail_node("mean_N6_"+patch,
              lambda patch=patch:api.complete_mean_N6_patch(
                handoff["patches"][patch],extended[patch],kernels[patch],profiles[patch]["Pstar"]),
              api.decode_mean_N6_conclusion)
        mean_union=tail_node("mean_union",
          lambda:api.complete_mean_union(kernels,means),api.decode_mean_union_conclusion)
        bundle=api.posterior_bundle_for_residual(
            handoff,extended,physical,same_J,kernels,profiles,mean_union)
        residual_work={}
        for patch in ("strict","local"):
            residual_work[patch]=publishing_node("N6_"+patch,
              lambda pub,patch=patch:residual.complete_ordered_residual_patch(
                  bundle,patch,api,pub,progress))
        jumps=publishing_node("true_jumps",
          lambda pub:residual.complete_true_jump_graph(bundle,api,pub,progress))
        receiver_old={key:records[key] for key in ("C_O","C_R","C_1")}
        negative=publishing_node("negative_reception",
          lambda pub:residual.complete_negative_reception_graph(
            bundle,residual_work,jumps,receiver_old,api,pub,progress))
        require("extended_amplitude_strict" in completed and
                saved_documents["extended_amplitude_strict"]["shape"]==[12,2],
                "complete extended strict first amplitude must already be published")
        q["waist"]["complete_extended_first_amplitude_admitted"]=True
        waist_records={key:records[key] for key in endpoint.ORIGINAL_RECORD_PATHS}
        waist=endpoint.prepare_waist_input(handoff,extended["strict"],waist_records,q["waist"])
        reconstruction=publishing_node(endpoint.NODE_NAMES[0],
          lambda pub:endpoint.complete_waist_reconstruction(api,waist,pub,progress))
        extension_doc=saved_documents["extension_scalars"]
        free_map=publishing_node(endpoint.NODE_NAMES[1],
          lambda pub:endpoint.complete_free_waist_map(
            api,waist,reconstruction,extension_doc,pub,progress))
        endpoints=publishing_node(endpoint.NODE_NAMES[2],
          lambda pub:endpoint.complete_four_waist_endpoints(
            api,waist,free_map,extension_doc,saved_documents["mean_union"],pub,progress))
        publishing_node(WHOLE_NODE,
          lambda pub:complete_whole_error(api,records,negative,endpoints,pub))
        require(len(completed)==len(specs) and
                state["locked_attempted_nodes"]==[s["node_name"] for s in specs],
                "the complete declared scientific DAG was not evaluated")
        for role,spec in files.items():
            require(sha((root/spec["path"]).read_bytes())==spec["sha256"],
                    "one immutable input changed during new mathematics")
        gate("all original inputs remain unchanged and every declared graph is retained")
        require(all(state["retained_scope"][k] is False for k in
             ("passing_high_cutoff_proved","finite_Schur_inverse_proved",
              "full_incoming_inverse_proved","full_nonlinear_background_proved",
              "final_surface_proved")),"an unpaid scope was promoted")
        gate("complete whole error preserves every unpaid physical finite parameter and background obligation")
        require(len(state["gates"])==m["expected_final_gate_count"],"complete structural gate count")
        state.update(complete=True,proved=True,actual_returncode=0,failure=None,stage="complete")
    except BaseException as error:
        state.update(complete=False,proved=False,actual_returncode=1,
           failure={"type":type(error).__name__,"message":str(error),
                    "active_node":state.get("active_node")},stage="preserved_failure")
        print("WEJ_PRESERVED_FAILURE "+json.dumps(state["failure"],ensure_ascii=False),flush=True)
    finally:
        state["actual_mathematical_wall_seconds"]=time.monotonic()-started
        checkpoint(emit=True)
    if not state["complete"]:
        raise SystemExit(1)

if __name__=="__main__":
    main()
