"""TCX adapter: one exact trial restoration, at most3 disjoint cell children.

The complete original TC owner and the published continuation adapter are
byte-pinned. Every original numerical cell formula is copied unchanged;
only scheduling, checkpoint regrouping and exact metadata transition change.
"""
from pathlib import Path
import hashlib
import importlib.util

BASE_NAME = "fourfold_codazzi_true_root_trial_owner.py"
BASE_BYTES = 63363
BASE_SHA256 = "193a317166204eef3870f12e5aee08be5a3de46e18b65de4b471b2a478f253dc"
BASE_PATH = "topics/visible-flex-exact-nearby/scripts/"+BASE_NAME
CONT_NAME = "fourfold_codazzi_true_root_trial_continuation_owner.py"
CONT_BYTES = 9136
CONT_SHA256 = "51107472dcac412fc0772be5a55182c93acc707c841ad750a9672779b34d1862"
CONT_PATH = "topics/visible-flex-exact-nearby/scripts/"+CONT_NAME
ADAPTER_PATH = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_parallel_trial_owner.py"
PARALLEL_NAME = "fourfold_codazzi_true_root_parallel_cell_slices.py"
PARALLEL_PATH = "topics/visible-flex-exact-nearby/scripts/"+PARALLEL_NAME
PARALLEL_KEY = "complete_parallel_cell_slices"
TCX_CONTRACT = {"kind": "TCX_same_trial_disjoint_complete_cell_continuation_v1",
    "maximum_arithmetic_children": 3, "complete_original_trial_arrays_restored_once": 4,
    "same_complete_exact_cell_evaluator": True, "same96_columns_and_all5_sources": True,
    "whole_immutable_seed_and_fixed_partition_retained": True,
    "old_accepted_cell_integrals_repeated": False, "artificial_slice_boundary_conditions": False,
    "requires_actual_ended_predecessor": True}

OWNER_TRANSITION = '''def _same_complete_owner_manifest(previous_manifest,roles):
    current,original,continuation = (roles[name] for name in
        ("owner","original_TC_owner","original_TC_continuation_owner"))
    here = Path(__file__).read_bytes()
    require(current["path"] == ADAPTER_PATH and current["sha256"] == digest(here)
            and current["bytes"] == len(here)
            and original["path"] == BASE_PATH and original["bytes"] == BASE_BYTES
            and original["sha256"] == BASE_SHA256
            and continuation["path"] == CONT_PATH and continuation["bytes"] == CONT_BYTES
            and continuation["sha256"] == CONT_SHA256,
            "three explicit whole original/continuation/parallel owner identities")
    old_path = previous_manifest["roles"]["owner"]
    choices = {BASE_PATH:original,CONT_PATH:continuation,ADAPTER_PATH:current}
    require(old_path in choices,"the predecessor is one of the explicitly pinned TC owners")
    matches = [spec for spec in previous_manifest["files"] if spec["path"] == old_path]
    require(len(matches) == 1,"one whole exact original predecessor owner")
    expected = choices[old_path]
    return all(matches[0][key] == expected[key] for key in ("path","bytes","sha256","git_blob_sha"))

'''

EXTRA_METADATA = '''
def _TCX_parallel_module(expected_sha=None):
    path = Path(__file__).with_name(PARALLEL_NAME)
    raw = path.read_bytes()
    require(expected_sha is None or digest(raw) == expected_sha,"the whole pinned cell-slice module")
    return import_source(path,"_TCX_complete_cell_slice_metadata")


def admit_prior_metadata(manifest,roles,raws,current_identity):
    result = _TCX_original_prior_metadata(manifest,roles,raws,current_identity)
    require("prior_matrix" in roles and "prior_prefix" in roles,
            "parallel continuation inherits the entire matrix and an actual whole-cell prefix")
    require(roles["parallel_math"]["path"] == PARALLEL_PATH,
            "one declared complete same-trial scheduling implementation")
    parallel = _TCX_parallel_module(roles["parallel_math"]["sha256"])
    previous = json.loads(raws[roles["prior_state"]["path"]])
    prefix_raw = raws[roles["prior_prefix"]["path"]]
    record = previous["preparation"].get(PARALLEL_KEY)
    if record is not None:
        _,total,contiguous,accepted = parallel.validate_parallel_metadata(record,previous["proposal"],
            previous["input_identity"]["scientific_sources"],roles["parallel_math"]["sha256"],require_prefix=True)
        require(parallel.stable_prefix_matches(record,prefix_raw),
                "the previous whole disjoint ledger and contiguous prefix are the same stable checkpoint")
        result["complete_disjoint_cell_admission"] = {"same_fixed_partition":True,
            "complete_union_cells":accepted,"contiguous_complete_cells":contiguous,"total_cells":total,
            "all_accepted_slices_reused_without_reintegration":True}
    else:
        prefix = json.loads(prefix_raw)
        result["complete_disjoint_cell_admission"] = {"same_fixed_partition":False,
            "complete_union_cells":prefix["next_cell"],"contiguous_complete_cells":prefix["next_cell"],
            "total_cells":prefix["total_cells"],"all_accepted_slices_reused_without_reintegration":True}
    return result


def preflight(args):
    value = _TCX_original_preflight(args)
    manifest,roles,raws,helper,prior,rows,identity = value
    require(manifest.get("parallel_continuation") == TCX_CONTRACT
            and manifest["continuation"] is not None
            and roles["parallel_math"]["path"] == PARALLEL_PATH,
            "complete explicit disjoint continuation contract after a real ended predecessor")
    _TCX_parallel_module(roles["parallel_math"]["sha256"])
    return value


def validate_parallel_checkpoint(document,prefix_raw):
    record = document["preparation"].get(PARALLEL_KEY)
    if record is None:
        return True
    parallel = _TCX_parallel_module()
    parallel.validate_parallel_metadata(record,document["proposal"],
        document["input_identity"]["scientific_sources"],
        digest(Path(__file__).with_name(PARALLEL_NAME).read_bytes()),require_prefix=True)
    if prefix_raw is None:
        return False
    return parallel.stable_prefix_matches(record,prefix_raw)

'''


def _TCX_continuation_source():
    path = Path(__file__).with_name(CONT_NAME)
    raw = path.read_bytes()
    if len(raw) != CONT_BYTES or hashlib.sha256(raw).hexdigest() != CONT_SHA256:
        raise ValueError("the complete original continuation metadata adapter changed")
    spec = importlib.util.spec_from_file_location("_TCX_pinned_serial_adapter", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.patched_source()


def patched_source():
    source = _TCX_continuation_source()
    replacements = [
        ('SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_true_root_trial_continuation_owner.py"',
         'SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_true_root_parallel_trial_owner.py"',1),
        ('previous["owner"] in (BASE_SHA256,here)',
         'previous["owner"] in (BASE_SHA256,CONT_SHA256,here)',1),
        ('def admit_prior_metadata(manifest,roles,raws,current_identity):',
         'def _TCX_original_prior_metadata(manifest,roles,raws,current_identity):',1),
        ('def preflight(args):','def _TCX_original_preflight(args):',1),
        ('        def save_prefix(index):','        def save_prefix(index,parallel_record=None):',1),
        ('            atomic(output/FILES["prefix"],raw)\n',
         '''            if parallel_record is None:
                parallel_record = state["preparation"].get(PARALLEL_KEY)
            if parallel_record is not None:
                require(parallel_record["contiguous_next_cell"] == index,
                        "the disjoint ledger and continuous prefix describe the same complete checkpoint")
                parallel_record["contiguous_prefix_receipt"] = {"bytes":len(raw),"sha256":digest(raw)}
                state["preparation"][PARALLEL_KEY] = copy.deepcopy(parallel_record)
            atomic(output/FILES["prefix"],raw)
''',1),
        ('                "prior_whole_manifest_sha256":old_manifest_sha}\n            save_state()\n',
         '''                "prior_whole_manifest_sha256":old_manifest_sha}
            if PARALLEL_KEY in previous["preparation"]:
                state["preparation"][PARALLEL_KEY] = copy.deepcopy(previous["preparation"][PARALLEL_KEY])
            save_state()
''',1),
    ]
    for old,new,count in replacements:
        if source.count(old) != count:
            raise ValueError("the exact TCX source adaptation did not match: "+old)
        source = source.replace(old,new)
    start = source.index("def _same_complete_owner_manifest(")
    end = source.index("def _qualified_original_input_reconstruction(",start)
    source = source[:start]+OWNER_TRANSITION+source[end:]
    location = source.index("def main():\n")
    source = source[:location]+EXTRA_METADATA+source[location:]
    start = source.index("        last_trial = None\n")
    loop = source.index("        for index in range(next_cell,len(plan)):\n",start)
    body_start = source.index("            budget()\n",loop)
    body_end = source.index("            # All source components for this cell are formed BEFORE any\n",body_start)
    body = source[body_start:body_end]
    end = source.index('        if "positive" not in copied:\n',body_end)
    # This exact original text retains full Hermite restriction, true h,
    # cutoff, selected scalar/background and all declared paired norms.
    body_sha = hashlib.sha256(body.encode()).hexdigest()
    replacement = '''        last_trial = None
        trial_coefficients = None
        true_left = true_right = true_length = None
        def evaluate_complete_original_cell(index):
            nonlocal last_trial,trial_coefficients,true_left,true_right,true_length
'''+body+'''            return contributions

        parallel = _TCX_parallel_module(roles["parallel_math"]["sha256"])
        old_parallel = state["preparation"].get(PARALLEL_KEY)
        seed = json.loads(raws[roles["prior_prefix"]["path"]])
        if old_parallel is not None:
            seed = old_parallel["seed_prefix"]
        require(seed["last_complete_cell"] == (None if seed["next_cell"] == 0 else plan[seed["next_cell"]-1]),
                "the whole original exact-plan seed is restored before any fork")
        for info in arrays.values():
            info["array"].flags.writeable = False
        state["preparation"]["parallel_cell_evaluator"] = {
            "unchanged_original_evaluator_text_sha256":"'''+body_sha+'''",
            "all_four_trial_arrays_verified_before_fork":True,
            "whole_trial_materializations_in_this_parent":1,
            "maximum_arithmetic_children":3,
            "original96_columns_and_all_source_components":True}
        def publish_disjoint_record(record,index,prefix_sums,union_sums):
            nonlocal accumulators
            accumulators = prefix_sums
            save_prefix(index,record)
            formal = json.loads((output/FILES["state"]).read_bytes())["preparation"][PARALLEL_KEY]
            require(formal == record,"the entire disjoint ledger is formal before any dependent conclusion")
            parallel.validate_parallel_metadata(formal,proposal_identity,input_identity["scientific_sources"],
                roles["parallel_math"]["sha256"],require_prefix=True)
            require(parallel.stable_prefix_matches(formal,(output/FILES["prefix"]).read_bytes()),
                    "the whole saved ledger and continuous prefix have one stable identity")
            accumulators = union_sums
            if index > last_negative and "negative" not in copied:
                finish_sources("negative")
            print(canonical({"complete_disjoint_union_cells":record["accepted_union_complete_cells"],
                "contiguous_complete_cells":index,"total":len(plan),
                "complete_columns_per_cell":96,"all_source_windows":5}).decode(),end="",flush=True)
        remaining = PARAMETERS["maximum_scientific_seconds"]-(time.perf_counter()-started)-60
        require(remaining > 0,"whole trial and prior prefixes saved before the parallel arithmetic allowance")
        parallel_record = parallel.fork_remaining_cells(c,seed,old_parallel,proposal_identity,
            input_identity["scientific_sources"],roles["parallel_math"]["sha256"],
            evaluate_complete_original_cell,lambda index:plan[index]["norms"],publish_disjoint_record,
            private_directory=private/"private-disjoint-cell-states",seconds_remaining=remaining,
            checkpoint_stride=PARAMETERS["complete_cell_checkpoint_stride"])
        require(parallel_record["complete"] is True,
                "parallel TC batch incomplete; every whole accepted disjoint cell slice is retained")
        if "negative" not in copied:
            finish_sources("negative")
'''
    source = source[:start]+replacement+source[end:]
    return source


exec(compile(patched_source(), __file__, "exec"), globals())
