"""Request205 actual202 accurate-ten solve, closed geometry and explicit ownership."""
import hashlib
import json
import os
from pathlib import Path
import runpy
import sys
import time

ROLES={"selection":"rule-sync-selection","C":"rule-sync","construction":"construction-rule-sync","far":"rule-sync-far","sampling":"rule-sync-sampling","binding":"candidate-bind-rule-sync","bvp":"rule-sync-BVP","postsolve":"postsolve-rule-sync"}
def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
def root():
    base=Path(os.environ["VISIBLE_BASE"]).resolve()
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve()
    if base.name!="visible-current-C-actual202-ten450-closed-geometry205" or base.parent!=temporary:
        raise ValueError("Use this job's exclusive request205 namespace")
    return base
def identity(pid):
    try:
        text=(Path("/proc")/str(pid)/"stat").read_text()
    except (FileNotFoundError,ProcessLookupError):
        return None
    fields=text.rsplit(")",1)[1].split()
    return dict(pid=pid,state=fields[0],ppid=int(fields[1]),pgid=int(fields[2]),
        start_ticks=int(fields[19]))
def record(role,kind,phase,**details):
    if role not in ROLES or kind not in ("parent","science"):
        raise ValueError("Unknown original stage owner")
    directory=root()/"owned-rule-sync-processes"
    directory.mkdir(exist_ok=True)
    value=dict(schema="request205-owned-process-receipt-v1",
        repository=os.environ["GITHUB_REPOSITORY"],run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],role=role,kind=kind,phase=phase,
        own_process=identity(os.getpid()),unix_seconds=time.time(),**details)
    path=directory/(role+"-"+kind+"-"+phase+".json")
    raw=canonical(value)
    with path.open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    print(json.dumps(dict(event="request205-owned-process-receipt",
        relative_file=str(path.relative_to(root())),bytes=len(raw),
        sha256=hashlib.sha256(raw).hexdigest(),role=role,kind=kind,phase=phase)),flush=True)
    return value
def invoke_parent(role,callback):
    record(role,"parent","launch",exclusive_process_group=False,
        parent_may_inherit_a_shared_job_process_group=True)
    try:
        code=callback()
    except BaseException as error:
        record(role,"parent","return",actual_exception_type=type(error).__name__,
            actual_exception=str(error),normal_return=False)
        raise
    record(role,"parent","return",actual_returncode=code,normal_return=True)
    return code
def execute(argv):
    if len(argv)<2 or argv[0] not in ROLES:
        raise ValueError("Use exec ROLE original-script original-arguments")
    role=argv[0]
    # Only the source/parameter restoration wrapper needs the official API
    # token. It passes it solely to original630c transport and removes all
    # token variables before the original595/ba8 numerical reconstruction.
    if role!="selection":
        for key in ("GH_TOKEN","GITHUB_TOKEN","MR_TOKEN"):os.environ.pop(key,None)
    own=identity(os.getpid())
    if own is None or own["pgid"]!=own["pid"]:
        raise ValueError("The original rule runner must own an exclusive science session")
    record(role,"science","launch",exclusive_process_group=True,
        exclusive_group_created_by_original_rules_runner_start_new_session=True)
    actual=list(argv[1:])
    declared_argv_sha256=hashlib.sha256(canonical(actual)).hexdigest()
    base=root()
    request_raw=(base/"dispatch-request.json").read_bytes()
    request=json.loads(request_raw)
    deadline=json.loads((base/"job-science-deadline.json").read_bytes())
    if (deadline["schema"]!="request205-owned-job-science-deadline-v1"
            or deadline["repository"]!=os.environ["GITHUB_REPOSITORY"]
            or deadline["run_id"]!=os.environ["GITHUB_RUN_ID"]
            or deadline["source_commit"]!=os.environ["GITHUB_SHA"]
            or deadline["request_sha256"]!=hashlib.sha256(request_raw).hexdigest()
            or deadline["template_recipe_sha256"]!=request["current_BVP_recipe"]["sha256"]
            or deadline["science_seconds_from_namespace"]!=18900
            or deadline["readback_reserve_seconds"]!=2700):
        raise ValueError("Bind the actual same-job namespace resource plan")
    remaining=deadline["namespace_created_unix_seconds"]+18900-time.time()
    policy=dict(schema="request205-actual-stage-resource-clip-v1",
        role=role,actual_remaining_namespace_seconds=remaining,
        original_argv=actual[:],original_argv_sha256=declared_argv_sha256,
        clipping_happens_after_original_rules_startup_sync=True,
        phase_clocks_still_exclude_source_binding_and_runtime_setup=True,
        namespace_is_a_startup_plan_outside_the_original_BVP_launcher=True,
        original_BVP_launcher_enforces_its_actual_namespace_deadline=True,
        resource_scope_not_a_mathematical_or_denominator_gate=True)
    def stop(reason):
        record(role,"science","resource-stop",scientific_script_started=False,
            reason=reason,resource_policy=policy)
        record(role,"science","return",actual_returncode=124,normal_return=True,
            original_scientific_scope_unpaid=True)
        return None
    def position(flag):
        if actual.count(flag)!=1:
            raise ValueError("One original resource argument required: "+flag)
        return actual.index(flag)+1
    if remaining<=0 and role not in ("bvp","postsolve"):
        stop("namespace-resource-plan-exhausted-before-this-scientific-entry")
        return 124
    if role=="sampling":
        declared=request["native_sampling"]["parameters"]
        linear=float(declared["linear_budget_seconds"])
        sampling=float(declared["sampling_budget_seconds"])
        reserve=float(request["execution"]["sampling_future_BVP_reserve_seconds"])
        allowance=max(0.0,remaining-reserve)
        scale=min(1.0,allowance/(linear+sampling))
        policy.update(original_linear_seconds=linear,original_sampling_seconds=sampling,
            planned_later_BVP_reserve_seconds=reserve,
            original193_later_BVP_reserve_seconds=7200,
            full_BVP_process_upper_bound_seconds=float(request["execution"]["full_BVP_process_budget_seconds"]),
            reserve_change_does_not_change_BVP_mathematics_or_maximum_budget=True,
            actual_stage_allowance_seconds=allowance,
            actual_linear_seconds=linear*scale,actual_sampling_seconds=sampling*scale,
            sampling_phase_excludes_pruefer_propagation_elapsed=True)
        if scale<=0:
            stop("no-sampling-allowance-after-explicit-BVP-resource-reserve")
            return 124
        for flag,original,effective in (
                ("--linear-budget-seconds",linear,linear*scale),
                ("--sampling-budget-seconds",sampling,sampling*scale)):
            i=position(flag)
            if float(actual[i])!=original:raise ValueError("Declared phase argument differs")
            actual[i]=repr(effective)
    elif role=="bvp":
        pi=position("--recipe");hi=position("--recipe-sha256")
        raw=Path(actual[pi]).read_bytes();original=hashlib.sha256(raw).hexdigest()
        binding_raw=(base/"actual202-ten-BVP-input"/"result.json").read_bytes()
        binding=json.loads(binding_raw)
        generated=binding.get("generated_BVP_recipe",{})
        if (binding.get("schema")!="request205-actual202-accurate-ten-construction-v1-actual-BVP-input"
                or binding.get("source_sha256")!=request["pipeline"]["sha256"]
                or binding.get("run_id")!=os.environ["GITHUB_RUN_ID"]
                or binding.get("source_commit")!=os.environ["GITHUB_SHA"]
                or binding.get("direct_BVP_input_created") is not True
                or generated.get("sha256")!=original or generated.get("bytes")!=len(raw)
                or original!=actual[hi]
                or Path(actual[pi]).resolve()!=(base/"actual202-ten-BVP-input"/generated["file"]).resolve()):
            raise ValueError("Use the actual202 accurate-ten construction and two-problem recipe")
        recipe=json.loads(raw)
        if (recipe.get("request_number")!=205
                or recipe.get("schema")!=request["pruefer_provider"]["recipe_schema"]):
            raise ValueError("The generated BVP input must identify this independent experiment")
        policy["actual_selected_input_binding"]=dict(bytes=len(binding_raw),
            sha256=hashlib.sha256(binding_raw).hexdigest())
        policy["original179_template_recipe"]=request["current_BVP_recipe"]
        if (recipe["execution"]["pruefer_sampling_startup_reserves_original_BVP_seconds"]
                !=request["execution"]["sampling_future_BVP_reserve_seconds"]
                or recipe["explicit_resource_binding"]["actual_sampling_startup_reserve_seconds"]
                !=request["execution"]["sampling_future_BVP_reserve_seconds"]):
            raise ValueError("Sampling and generated recipe must bind one actual explicit reserve")
        declared=float(recipe["execution"]["complete_BVP_process_budget_seconds"])
        policy.update(original_BVP_seconds=declared,
            positive_remaining_plan_seconds=max(0.0,remaining),
            actual_BVP_clipping_and_stop_use_unchanged_algorithm_in_new_identity_launcher=True,
            original_recipe=dict(file=actual[pi],bytes=len(raw),sha256=original),
            original_scientific_controls_unchanged_selected_initial_parameters_explicit=True,
            expired_deadline_still_enters_original_launcher_to_record_unstarted_scope=True)
    else:
        policy["original_parameter_or_scientific_arguments_unchanged"]=True
    policy["actual_argv"]=actual[:]
    policy["actual_argv_sha256"]=hashlib.sha256(canonical(actual)).hexdigest()
    record(role,"science","resource-policy",resource_policy=policy)
    sys.argv=actual
    try:
        runpy.run_path(actual[0],run_name="__main__")
    except SystemExit as result:
        code=0 if result.code is None else (result.code if type(result.code) is int else 1)
        record(role,"science","return",actual_returncode=code,normal_return=True,
            original_system_exit_value=result.code if result.code is None or type(result.code) in (int,str) else repr(result.code))
        raise
    except BaseException as error:
        record(role,"science","return",actual_exception_type=type(error).__name__,
            actual_exception=str(error),normal_return=False)
        raise
    record(role,"science","return",actual_returncode=0,normal_return=True)
    return 0
def observe():
    base=root();directory=base/"owned-rule-sync-processes"
    active=[];unknown=[];identities=[];launches={}
    for path in (sorted(directory.glob("*-launch.json")) if directory.is_dir() else []):
        try:
            raw=path.read_bytes();value=json.loads(raw)
            if (value["schema"]!="request205-owned-process-receipt-v1"
                    or value["repository"]!=os.environ["GITHUB_REPOSITORY"]
                    or value["run_id"]!=os.environ["GITHUB_RUN_ID"]
                    or value["source_commit"]!=os.environ["GITHUB_SHA"]):
                raise ValueError("An original owner receipt has a different source or run")
            role,kind=value["role"],value["kind"];saved=value["own_process"]
            if role not in ROLES or kind not in ("parent","science") or saved is None:
                raise ValueError("Original owner identity is incomplete")
            launches[(role,kind)]=value
            current=identity(saved["pid"])
            same=(current is not None and current["start_ticks"]==saved["start_ticks"])
            one=dict(relative_file=str(path.relative_to(base)),bytes=len(raw),
                sha256=hashlib.sha256(raw).hexdigest(),role=role,kind=kind,
                original_pid=saved["pid"],original_start_ticks=saved["start_ticks"],
                original_pgid=saved["pgid"],same_original_process_currently_present=same,
                current_state=current["state"] if same else None)
            if same and current["state"]!="Z":
                active.append(dict(role=role,kind=kind,**current))
            if kind=="science":
                if value.get("exclusive_process_group") is not True or saved["pgid"]!=saved["pid"]:
                    raise ValueError("A science group was not proved exclusive at launch")
                members=[]
                for child in Path("/proc").iterdir():
                    if not child.name.isdigit():continue
                    current_member=identity(int(child.name))
                    if (current_member is not None and current_member["pgid"]==saved["pgid"]
                            and current_member["state"]!="Z"):
                        members.append(current_member)
                one["live_members_of_original_exclusive_science_group"]=members
                for member in members:
                    if not any(x["pid"]==member["pid"] for x in active):
                        active.append(dict(role=role,kind="science-group-member",**member))
            else:
                one["shared_parent_process_group_not_required_to_be_empty"]=True
            identities.append(one)
        except Exception as error:
            unknown.append(dict(relative_file=str(path.relative_to(base)),
                type=type(error).__name__,message=str(error)))
    for role,name in ROLES.items():
        out=base/name
        if (out/"science-launch.json").is_file() and (role,"science") not in launches:
            if not (out/"runner-result.json").is_file() and not (out/"science-launch-failed.json").is_file():
                unknown.append(dict(role=role,
                    reason="Original launch intent exists but no actual child identity or joined return was recorded"))
        if out.is_dir() and (role,"parent") not in launches:
            unknown.append(dict(role=role,
                reason="An original rules directory exists without its wrapper owner launch identity"))
    return dict(schema="request205-original-owner-quiescence-observation-v1",
        repository=os.environ["GITHUB_REPOSITORY"],run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],unix_seconds=time.time(),
        original_process_receipts=identities,live_original_owned_processes=active,
        unknown_owner_scopes=unknown,quiescent=not active and not unknown,
        parent_shared_job_group_not_treated_as_science=True,
        no_signal_or_process_mutation_performed=True,
        this_metadata_condition_is_not_a_mathematical_acceptance_gate=True)
if __name__=="__main__":
    if sys.argv[1:2]!=["exec"]:raise SystemExit("Use exec ROLE original scientific argv")
    raise SystemExit(execute(sys.argv[2:]))
