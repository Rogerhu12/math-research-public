"""TCF: terminal-admitted, disjoint missing cells of the original TC trial.

Metadata routines use only the standard library. Numerical work is confined
to the same original whole96 cell evaluator on a declared missing interval.
The optional Legendre memo has one-cell lifetime and returns the first
unchanged full Box for the identical immutable input object.
"""
from __future__ import annotations
import ast, hashlib, importlib.util, json, math
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PARENT_MANIFEST = TOPIC+"/notes/2026-11-28-true-root-trial-complete2677-inputs.json"
PARENT_MANIFEST_SHA = "6b82d09170ed4ec780eccd0910cb69df98615390ef2f73237ed324d1e3f2c692"
PARENT_RUN = "46117170011"
PARENT_OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_trial_owner.py"
PARENT_OWNER_SHA = "2408b84e7aa820ec6942dcd6255b77583cd776072c09fb6f521866930fcb7200"
BASE_OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_owner.py"
BASE_OWNER_SHA = "193a317166204eef3870f12e5aee08be5a3de46e18b65de4b471b2a478f253dc"
KIND = "R149_original_TC_terminal_missing_cell_fleet_v1"
SLICE_KIND = "R149_original_TC_whole96_missing_cell_assignment_v1"
UNION_KIND = "R149_original_TC_terminal_complete_accepted_union_v1"
NORMS = ("positive_low", "positive_high_collar", "positive_high_body",
         "negative_root", "negative_strict")
TOTAL, COLUMNS = 7724, 96


def require(ok, message):
    if not ok:
        raise ValueError(message)


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(path, label):
    raw=Path(path).read_bytes();ast.parse(raw)
    spec=importlib.util.spec_from_file_location(label,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def descriptor(root, path):
    require(path.startswith(TOPIC+"/") and all(x not in ("", ".", "..") for x in path.split("/")),
            "one entire safe original topic object")
    raw=(Path(root)/path).read_bytes()
    require(0<len(raw)<100000,"one entire small metadata object")
    raw.decode()
    return {"path":path,"bytes":len(raw),"sha256":sha(raw),
        "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def require_whole(root, spec):
    observed=descriptor(root,spec["path"])
    require(all(observed[key]==spec[key] for key in observed),"the whole original object: "+spec["path"])
    return (Path(root)/spec["path"]).read_bytes()


def inspect_parent(root, directory):
    """Readiness may inspect an active run; admission cannot accept it."""
    root=Path(root)
    paths={"manifest":PARENT_MANIFEST,
        "state":directory+"/actual-trial-state.json",
        "prefix":directory+"/complete-radial-integration-prefix.json",
        "matrix":directory+"/complete-signed-trial-matrices.json",
        "execution":directory+"/execution.json"}
    for key,name in (("negative","complete-negative-trial-sources.json"),
                     ("positive","complete-positive-trial-sources.json")):
        if (root/(directory+"/"+name)).is_file():paths[key]=directory+"/"+name
    missing=[path for path in paths.values() if not (root/path).is_file()]
    if missing:
        return {"ready":False,"reason":"whole_parent_files_missing","missing":missing},None
    specs={key:descriptor(root,path) for key,path in paths.items()}
    raw={key:(root/spec["path"]).read_bytes() for key,spec in specs.items()}
    docs={key:json.loads(value) for key,value in raw.items()}
    state,execution=docs["state"],docs["execution"]
    require(specs["manifest"]["sha256"]==PARENT_MANIFEST_SHA
        and state["run_id"]==execution["run_id"]==PARENT_RUN
        and state["run_attempt"]==execution["run_attempt"]=="1"
        and execution["manifest_sha256"]==state["input_identity"]["manifest_sha256"]==PARENT_MANIFEST_SHA,
        "the exact current TC continuation, never a different trial or run")
    if not (execution.get("scientific_finished_utc") and execution.get("finished_utc")
            and type(execution.get("actual_child_returncode")) is int):
        return {"ready":False,"reason":"parent_science_or_public_job_not_ended",
            "parent_run":PARENT_RUN+"/1","accepted_complete_cells":execution.get("parallel_accepted_complete_cells"),
            "no_new_assignment_issued":True},None
    owner_raw=(root/PARENT_OWNER).read_bytes()
    require(sha(owner_raw)==PARENT_OWNER_SHA,"the whole actually executing predecessor owner")
    owner=load(root/PARENT_OWNER,"_TCF_unchanged_terminal_parent")
    require(sorted(state)==sorted(owner.STATE_FIELDS)
        and execution["repository"]=="Rogerhu12/math-research-public"
        and execution["scientific_children"]==1
        and execution["old_completed_targets_recomputed"]==0
        and execution["new_arrays_published"]==execution["new_artifacts"]==execution["new_Releases"]==0,
        "the complete actual terminal TC scientific/execution contract")
    for key in ("state","prefix","matrix","negative","positive"):
        if key not in specs:continue
        spec=specs[key]
        require([entry for entry in execution["scientific_files"] if entry["path"]==spec["path"]]==[
            {name:spec[name] for name in ("path","bytes","sha256")}],
            "the terminal public execution binds each whole scientific object")
    parent=docs["manifest"]
    by_path={item["path"]:item for item in parent["files"]+parent["historical_inputs"]}
    roles={key:by_path[path] for key,path in parent["roles"].items()}
    sources=state["input_identity"]["scientific_sources"]
    require(all(roles[key]["sha256"]==value for key,value in sources.items()),
        "all original eight mathematical sources and the real parent owner are retained")
    record=state["preparation"][owner.PARALLEL_KEY]
    parallel=owner._TCX_parallel_module(roles["parallel_math"]["sha256"])
    first,total,contiguous,accepted=parallel.validate_parallel_metadata(
        record,state["proposal"],sources,roles["parallel_math"]["sha256"],require_prefix=True)
    require(total==TOTAL and parallel.stable_prefix_matches(record,raw["prefix"])
        and execution["parallel_accepted_complete_cells"]==accepted
        and execution["qualified_complete_cells"]==contiguous,
        "the whole terminal accepted union and contiguous prefix agree")

    evidence_path=Path(root)/TOPIC/'scripts/fourfold_codazzi_tcf_whole_terminal_rule16.py'
    require(sha(evidence_path.read_bytes())=='f9d35b5558427d75ea18ac1585489971cfced93ca134311b563f637a9cbc0522','entire actual TC terminal policy and job attestation')
    evidence=load(evidence_path,'_TCF_exact_hard_stop_and_rule_16')
    if not record["child_outcomes"]:
        evidence.hard_stopped(root,record,raw)
    else:
        require(len(record["child_outcomes"])==len(record["slices"])
            and {item["ordinal"] for item in record["child_outcomes"]}==set(range(len(record["slices"])))
            and all(type(item["actual_exitcode"]) is int for item in record["child_outcomes"]),
            "every predecessor arithmetic process has a real terminal outcome")
    matrix=docs["matrix"]
    owner.validate_complete_result(matrix,"matrix",state["proposal"],matrix["input_manifest_sha256"],
                                    state["input_identity"]["same_selected_family"])
    old_matrix=roles["prior_matrix"]
    require(specs["matrix"]["sha256"]==old_matrix["sha256"]
        and specs["matrix"]["bytes"]==old_matrix["bytes"],
        "the already completed full signed matrix is copied verbatim")
    if accepted==TOTAL:
        return {"ready":False,"reason":"all_original_cells_already_complete","no_new_assignment_issued":True},None
    complete_keys=[key for key in ("matrix","negative","positive") if key in docs]
    require(complete_keys==["matrix"] or complete_keys==["matrix","negative"],
        "every already completed original norm is retained and never recomputed")
    for key in complete_keys[1:]:
        value=docs[key]
        owner.validate_complete_result(value,key,state["proposal"],value["input_manifest_sha256"],
                                        state["input_identity"]["same_selected_family"])
    require(state["complete"] is execution["complete"] is False and state["proved"] is False
        and state["completed_targets"]==execution["completed_natural_targets"]==owner.TARGETS[:len(complete_keys)],
        "the exact complete old natural-target prefix remains authoritative")
    missing_ranges=[[item["next_cell"],item["stop_cell"]] for item in record["slices"]
                    if item["next_cell"]<item["stop_cell"]]
    require(sum(b-a for a,b in missing_ranges)==TOTAL-accepted,"every and only unaccepted original cell")
    bundle={"specs":specs,"documents":docs,"record":record,"owner":owner,
        "missing_ranges":missing_ranges,"accepted_cells":accepted,"parent_identity":sha(encode(specs)),
        "completed_natural_keys":complete_keys}
    bundle["original_parent_identity"]=bundle["parent_identity"]
    bundle["accepted_intervals"]=merge_intervals([[0,record["seed_prefix"]["next_cell"]]]+
        [[item["first_cell"],item["next_cell"]] for item in record["slices"] if item["first_cell"]<item["next_cell"]])
    bundle["base_sums"]=([record["seed_prefix"]["squared_norm_upper_exact_binary64"]]+
        [item["squared_norm_upper_exact_binary64"] for item in record["slices"]])
    return {"ready":True,"parent_run":PARENT_RUN+"/1","accepted_complete_cells":accepted,
        "remaining_cells":TOTAL-accepted,"missing_ranges":missing_ranges,
        "parent_identity_sha256":bundle["parent_identity"]},bundle


def merge_intervals(intervals):
    out=[]
    for first,stop in sorted(intervals):
        require(type(first) is type(stop) is int and 0<=first<stop<=TOTAL,"a complete accepted natural-cell interval")
        if out:
            require(first>=out[-1][1],"no accepted cell is counted twice")
            if first==out[-1][1]:out[-1][1]=stop;continue
        out.append([first,stop])
    return out


def missing_intervals(accepted):
    accepted=merge_intervals(accepted);out=[];cursor=0
    for first,stop in accepted:
        if cursor<first:out.append([cursor,first])
        cursor=stop
    if cursor<TOTAL:out.append([cursor,TOTAL])
    return out


def read_job_records(root, definition, records, run):
    """Complete published prefixes, after all corresponding public jobs ended."""
    require(len(records)==len(definition["assignments"]),"every fixed assignment has a terminal public-job entry")
    documents=[]
    for ordinal,entry in enumerate(records):
        require(entry["ordinal"]==ordinal and entry["job"]["name"]=="TCF original cells %d"%ordinal
            and entry["job"]["status"]=="completed" and entry["job"]["conclusion"] is not None,
            "the actual whole public job, including a failed or unstarted arithmetic child, has ended")
        actual,execution=entry.get("actual"),entry.get("execution")
        if actual is None:
            if execution is not None:json.loads(require_whole(root,execution))
            documents.append(None);continue
        require(execution is not None,"every accepted cell is bound by its entire public execution")
        doc=json.loads(require_whole(root,actual));public=json.loads(require_whole(root,execution))
        validate_slice(doc,definition,ordinal)
        require(doc["run_id"]==public["run_id"]==run and doc["run_attempt"]==public["run_attempt"]=="1"
            and doc["manifest_sha256"]==public["manifest_sha256"]==definition["_whole_manifest_sha256"]
            and public["fleet_identity_sha256"]==definition["fleet_identity_sha256"]
            and public["assignment"]==definition["assignments"][ordinal]
            and doc["parameters"]==definition["parameters"]
            and public["old_completed_targets_recomputed"]==public["new_arrays_published"]==0
            and doc["old_completed_matrix_or_norm_targets_called"]==doc["new_arrays_published"]==0,
            "same entire executed assignment, source parameters and no old numerical targets")
        require([spec for spec in public["scientific_files"] if spec["path"]==actual["path"]]==[
            {key:actual[key] for key in ("path","bytes","sha256")}],"the entire actual prefix has its public whole-file binding")
        if doc["accepted_complete_cells"]:
            require(public["scientific_children"]==1 and doc["carrier_restoration"] is not None,
                "accepted cells follow complete original array and input restoration")
        documents.append(doc)
    return documents


def apply_carry(root, original, carry):
    """Metadata admission of a previous *terminal* fleet's complete union.

    The previous scalar sums are copied, never numerically added a second
    time here. Its complete public sources and integer coverage are checked.
    A later public worker separately verifies that its whole Actions run is
    completed before reserving any new tail.
    """
    if carry is None:return original
    require(set(carry)=={"manifest","union","execution"},"one whole previous fleet union and execution")
    raw={key:require_whole(root,spec) for key,spec in carry.items()}
    definition=json.loads(raw["manifest"]);union=json.loads(raw["union"]);public=json.loads(raw["execution"])
    require(definition["kind"]=="R149_original_TC_terminal_missing_cell_fleet_inputs_v1"
        and definition["terminal_parent_objects"]==original["specs"],"the identical original terminal TC parent")
    for spec in definition["files"]:require_whole(root,spec)
    previous=apply_carry(root,original,definition["carry_union"])
    require(previous["parent_identity"]==definition["parent_identity_sha256"],"the whole prior accepted-union lineage")
    validate_assignments(previous["missing_ranges"],definition["assignments"])
    require(union["kind"]==UNION_KIND and union["aggregation_complete"] is True
        and union["actual_returncode"]==public["actual_child_returncode"]==0
        and union["failure"] is public["failure"] is None and public["complete"] is True
        and union["manifest_sha256"]==public["manifest_sha256"]==sha(raw["manifest"])
        and union["fleet_identity_sha256"]==definition["fleet_identity_sha256"]
        and union["original_parent_identity_sha256"]==original["original_parent_identity"]
        and union["parent_identity_sha256"]==previous["parent_identity"]
        and union["run_id"]==public["run_id"] and union["run_attempt"]==public["run_attempt"]=="1"
        and public["finished_utc"] and public["scientific_finished_utc"]
        and public["old_completed_targets_recomputed"]==public["new_arrays_published"]==0,
        "one successfully preserved full accepted union, not a claimed full source result")
    require([spec for spec in public["scientific_files"] if spec["path"]==carry["union"]["path"]]==[
        {key:carry["union"][key] for key in ("path","bytes","sha256")}],"whole actual union public binding")
    definition["_whole_manifest_sha256"]=sha(raw["manifest"])
    documents=read_job_records(root,definition,union["source_records"],union["run_id"])
    intervals=accepted_with_documents(previous,definition,documents)
    count=sum(stop-first for first,stop in intervals)
    require(union["accepted_intervals"]==intervals and union["accepted_complete_cells"]==count
        and union["missing_intervals"]==missing_intervals(intervals)
        and union["complete_original_domain"] is (count==TOTAL)
        and union["complete_columns"]==COLUMNS and union["all_original_source_windows"]==list(NORMS),
        "the entire preserved union has the exact complete integer domain")
    validate_sums(union["squared_norm_upper_exact_binary64"])
    require(count<TOTAL,"the original source domain is already complete; no new cell may be assigned")
    out=dict(original)
    out.update(parent_identity=sha(encode({"original":original["specs"],"carry":carry})),
        accepted_cells=count,accepted_intervals=intervals,missing_ranges=missing_intervals(intervals),
        base_sums=[union["squared_norm_upper_exact_binary64"]],carry_union=carry)
    return out


def resolve_parent(root, definition):
    readiness,original=inspect_parent(root,definition["terminal_parent_directory"])
    require(readiness["ready"] is True and original["specs"]==definition["terminal_parent_objects"],
        "the same real terminal original parent")
    parent=apply_carry(root,original,definition["carry_union"])
    require(parent["parent_identity"]==definition["parent_identity_sha256"],"the entire actual accepted-union baseline")
    validate_assignments(parent["missing_ranges"],definition["assignments"])
    return parent


def accepted_with_documents(parent, definition, documents):
    require(len(documents)==len(definition["assignments"]),"every fixed assignment has one whole terminal slot")
    validate_assignments(parent["missing_ranges"],definition["assignments"])
    intervals=list(parent["accepted_intervals"])
    for ordinal,doc in enumerate(documents):
        if doc is None:continue
        cursor=validate_slice(doc,definition,ordinal)
        first=definition["assignments"][ordinal]["first_cell"]
        if first<cursor:intervals.append([first,cursor])
    return merge_intervals(intervals)


def materialize_carry(carry, read):
    """Walk whole small metadata edges; no numerical input is reconstructed."""
    if carry is None:return
    objects={key:json.loads(read(spec)) for key,spec in carry.items()}
    for spec in objects["manifest"]["files"]:read(spec)
    materialize_carry(objects["manifest"]["carry_union"],read)
    for record in objects["union"]["source_records"]:
        for key in ("actual","execution"):
            if record.get(key) is not None:read(record[key])


def partition_missing(parent, maximum_cells=256):
    require(type(maximum_cells) is int and 1<=maximum_cells<=512,
            "bounded integer scheduling only; no numerical estimate chooses a cell")
    assignments=[]
    for left,right in parent["missing_ranges"]:
        for first in range(left,right,maximum_cells):
            stop=min(first+maximum_cells,right)
            assignments.append({"ordinal":len(assignments),"first_cell":first,"stop_cell":stop,
                "complete_cells":stop-first,"complete_columns":COLUMNS,"all_original_source_windows":list(NORMS)})
    validate_assignments(parent["missing_ranges"],assignments)
    return assignments


def validate_assignments(missing_ranges, assignments):
    wanted=[i for a,b in missing_ranges for i in range(a,b)]
    actual=[]
    for ordinal,item in enumerate(assignments):
        first,stop=item["first_cell"],item["stop_cell"]
        require(item=={"ordinal":ordinal,"first_cell":first,"stop_cell":stop,
            "complete_cells":stop-first,"complete_columns":COLUMNS,"all_original_source_windows":list(NORMS)}
            and type(first) is type(stop) is int and 0<=first<stop<=TOTAL,
            "one full natural-cell assignment with every original96 column/window")
        actual.extend(range(first,stop))
    require(actual==wanted and len(set(actual))==len(actual),
            "the assignments form exactly the disjoint complement of the terminal accepted union")


def original_cell_factory(root):
    """Compile the exact original cell body; no coefficient or norm changes."""
    raw=(Path(root)/BASE_OWNER).read_bytes()
    require(sha(raw)==BASE_OWNER_SHA,"the complete original TC scientific owner")
    source=raw.decode()
    anchor=source.index("        last_trial = None\n")
    loop=source.index("        for index in range(next_cell,len(plan)):\n",anchor)
    start=source.index("            budget()\n",loop)
    stop=source.index("            # All source components for this cell are formed BEFORE any\n",start)
    body=source[start:stop]
    text="def make_original_cell():\n    last_trial = None\n    trial_coefficients = None\n    true_left = true_right = true_length = None\n    def evaluate(index):\n        nonlocal last_trial, trial_coefficients, true_left, true_right, true_length\n"
    text+="\n".join(line[4:] for line in body.rstrip().splitlines())+"\n        return contributions\n    return evaluate\n"
    code=compile(ast.parse(text),"<TCF exact unchanged original whole96 cell>","exec")
    return code,{"whole_original_owner_sha256":BASE_OWNER_SHA,"exact_original_cell_text_sha256":sha(body.encode()),
        "original_cell_formulas_or_operation_order_changed":False,"complete_columns":COLUMNS}


class OneCellLegendreMemo:
    """Identical object, immutable Box, one call lifetime; no norm memo."""
    def __init__(self, context):
        self.context=context
        self.original=context.legendre_coefficients
        self.cache={}
        self.calls=self.hits=0

    @staticmethod
    def freeze(value):
        for component in (value.real,value.imag):
            component.lo.flags.writeable=False
            component.hi.flags.writeable=False

    def __enter__(self):
        def cached(value):
            self.calls+=1
            identity=id(value)
            if identity in self.cache:
                previous,result=self.cache[identity]
                require(previous is value,"strong reference prevents a recycled input identity")
                self.hits+=1
                return result
            self.freeze(value)
            result=self.original(value)
            self.freeze(result)
            self.cache[identity]=(value,result)
            return result
        self.context.legendre_coefficients=cached
        return self

    def __exit__(self, *unused):
        self.context.legendre_coefficients=self.original
        self.cache.clear()


def validate_sums(values):
    require(set(values)==set(NORMS),"all five original source windows")
    for row in values.values():
        require(type(row) is list and len(row)==COLUMNS,"every original96 scalar upper")
        for text in row:
            value=float.fromhex(text)
            require(type(text) is str and value.hex()==text and math.isfinite(value) and value>=0,
                    "one exact nonnegative binary64 upper")


def validate_slice(document, definition, ordinal):
    item=definition["assignments"][ordinal]
    require(document["kind"]==SLICE_KIND and document["fleet_identity_sha256"]==definition["fleet_identity_sha256"]
        and document["assignment"]==item and document["parent_identity_sha256"]==definition["parent_identity_sha256"]
        and document["old_accepted_cells_evaluated"]==0
        and document["complete_columns"]==COLUMNS
        and document["all_original_source_windows"]==list(NORMS),"the same whole96 original missing-only target")
    first,stop,next_cell=item["first_cell"],item["stop_cell"],document["next_cell"]
    require(type(next_cell) is int and first<=next_cell<=stop
        and document["accepted_complete_cells"]==next_cell-first
        and document["complete_assignment"] is (next_cell==stop),"all and only complete cells advance the cursor")
    validate_sums(document["squared_norm_upper_exact_binary64"])
    if next_cell==first:
        require(all(value==float(0).hex() for row in document["squared_norm_upper_exact_binary64"].values() for value in row),
                "the empty new assignment contributes exact zero")
    return next_cell


def exact_saved_upper_sum(records):
    """New aggregation only, never a cell or old norm; call in public CI."""
    require(records,"nonempty original scalar-upper ledger")
    for record in records:validate_sums(record)
    result={}
    for name in NORMS:
        row=[]
        for j in range(COLUMNS):
            value=sum((Fraction.from_float(float.fromhex(record[name][j])) for record in records),Fraction(0))
            point=float(value)
            if Fraction.from_float(point)<value:point=math.nextafter(point,math.inf)
            require(math.isfinite(point) and Fraction.from_float(point)>=value,"a complete exact sum rounded upward once")
            row.append(point.hex())
        result[name]=row
    validate_sums(result)
    return result


def aggregate_accepted(parent, definition, documents):
    """Public arithmetic for the entire terminal accepted union, even partial."""
    intervals=accepted_with_documents(parent,definition,documents)
    values=list(parent["base_sums"])
    values.extend(item["squared_norm_upper_exact_binary64"] for item in documents if item is not None)
    return intervals,exact_saved_upper_sum(values)
