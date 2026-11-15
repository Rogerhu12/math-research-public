#!/usr/bin/env python3
"""Complete R163 weight -2 normal generators and their translation denominator.

Read published static L0, unreduced N0/N2 and v2/v4, five normal A/H families,
the proved R_-2 basis, and two completed axis contractions.  Construct only
missing weight-filtered contractions.  No forcing/W/old response compiler,
profile evaluation, normal-form rank, or positivity solver is invoked.
Actual research is restricted to this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import json
import os
from pathlib import Path
import resource
import tempfile
import time

import literature_acceleration_layer_mixed as layer
import literature_constrained_static_fourth as constrained

old, static = layer.old, layer.static
colored, exact, formal, blocks = layer.colored, layer.exact, layer.formal, layer.blocks
canonical, sha = layer.canonical, layer.sha
Field = layer.StateField
SCHEMA = "visible-flex-complete-character-head-minus2-v1"
REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = Path(layer.__file__).resolve().parents[1]
MODES = (-4, -2)
WEIGHT = -2
STATE_ZERO = (0, 0, 0, 0)
FAMILIES = ("F0", "Q2_0", "Q2_1", "Q2_2",
            "A_hh", "A_hk", "A_kk", "H1", "H2",
            "Q4_0", "Q4_1", "Q4_2", "Q4_3", "Q4_4")
R_RETAINED = list(range(24))+[25,27,28,29,31,32,33,35,36,39,40,41,46,47,48,49]
SOURCE_SHA = {
    "literature_local_fourth_quotient.py": "9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0",
    "literature_local_fourth_derivative_factors.py": "02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf",
    "literature_acceleration_layer_mixed.py": "271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c",
    "literature_G_translation_successor.py": "a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406",
    "literature_h_axis_sharp_coefficient.py": "7f4ee057a16a620e089102ea9c84fccafd922306e8febf8b73391b478e4a4a0b",
    "literature_constrained_static_fourth.py": "814e1338679914b32542f8b360978281002ee02a2c4e8c03912aa40c876786f4",
    "literature_total_P1_scaling_blocks.py": "40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa",
}


def info_export(filename, stored_bytes, stored_sha, raw_bytes, raw_sha):
    return {"filename": filename, "stored_bytes": stored_bytes, "stored_sha256": stored_sha,
            "raw_bytes": raw_bytes, "raw_sha256": raw_sha}


INPUTS = {
    "static": {
        "directory": "actions-43645177423-1-local_fourth_quotient",
        "run": "43645177423", "commit": "2f1b809c0b0abb7a26303d36940edc203815f872",
        "lane": "local_fourth_quotient", "driver": "literature_local_fourth_quotient.py",
        "main": "local-fourth-quotient.json", "main_bytes": 3982,
        "main_sha": "19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a",
        "receipt_sha": "c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba",
        "metadata": "portable_original_expression_export",
        "schema": "visible-flex-R109-local-fourth-quotient-static-v1",
        "scope": "W-and-local-static-density",
        "export": info_export("local-fourth-quotient-original-expressions.json.gz", 657195,
            "ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace", 3518194,
            "d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1"),
    },
    "factors": {
        "directory": "actions-43651096112-1-local_fourth_derivative_factors",
        "run": layer.FACTORS_RUN, "commit": layer.FACTORS_COMMIT,
        "lane": "local_fourth_derivative_factors", "driver": layer.FACTORS_DRIVER["filename"],
        "main": "local-fourth-derivative-factors.json", "main_bytes": layer.FACTORS_MAIN["bytes"],
        "main_sha": layer.FACTORS_MAIN["sha256"], "receipt_sha": layer.FACTORS_RECEIPT["sha256"],
        "metadata": "portable_complete_factor_export",
        "schema": layer.factors.SCHEMA, "scope": "unreduced-N0-N2-and-complete-two-mode-v2-v4",
        "export": layer.FACTORS_EXPORT,
    },
    "acceleration": {
        "directory": "actions-43654534244-1-acceleration_layer_mixed",
        "run": "43654534244", "commit": "1177f251dc3d9455adf88b585e4c0e4bd6f7e69b",
        "lane": "acceleration_layer_mixed", "driver": "literature_acceleration_layer_mixed.py",
        "main": "acceleration-layer-mixed.json", "main_bytes": 57753,
        "main_sha": "baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745",
        "receipt_sha": "3c147ca2edaa03d4c27fa0694adca26764c0f98c8fde363387359d8fddccc494",
        "metadata": "portable_acceleration_expression_export", "schema": layer.SCHEMA,
        "scope": "five-complete-two-mode-normal-acceleration-families",
        "export": info_export("acceleration-layer-mixed-original-expressions.json.gz", 318634,
            "b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e", 1909429,
            "7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38"),
    },
    "response": {
        "directory": "actions-43653293263-1-g_translation_successor",
        "run": "43653293263", "commit": "2f0add61f44365d713abf836beaa8b0be2806a3d",
        "lane": "g_translation_successor", "driver": "literature_G_translation_successor.py",
        "main": "G-third-translation.json", "main_bytes": 25014,
        "main_sha": "b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3",
        "receipt_sha": "a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523",
        "metadata": "portable_new_block_expression_export", "schema": layer.BLOCK_SCHEMA,
        "scope": "one-translation-target-and-complete-new-response-block",
        "export": info_export("G-third-translation-original-expressions.json.gz", 157782,
            "226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e", 889438,
            "eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7"),
    },
    "axis": {
        "directory": "actions-43657526246-1-h_axis_sharp",
        "run": "43657526246", "commit": "0d5df1843fd829e7c09b17afdead930ec4395f34",
        "lane": "h_axis_sharp", "driver": "literature_h_axis_sharp_coefficient.py",
        "main": "h-axis-sharp.json", "main_bytes": 17542,
        "main_sha": "e0007757b7d113a34b5c2ec594a607d380855f5652042f67fe3f32c1c81397f0",
        "receipt_sha": "1d635cdbe80251339d1157cee579c6838cad8975310a80959ef92b171f2458ea",
        "metadata": "portable_axis_expression_export", "schema": "visible-flex-h-axis-sharp-coefficient-v1",
        "scope": "one-complete-h-axis-D0-K0-and-two-unreduced-N2-contractions",
        "export": info_export("h-axis-sharp-original-expressions.json.gz", 14497,
            "ecd9edf2d461f6d4f6b9355e17e210ad435b20c53bc16baeda412258b8b3fabd", 80444,
            "2d0433a628b22f223a0f8700cebad02e70305699ff39a65e075de81dad5ceed0"),
    },
}


def source_identity():
    root = Path(layer.__file__).resolve().parent
    found = {name: static.identity(root/name) for name in SOURCE_SHA}
    for name, wanted in SOURCE_SHA.items():
        if found[name]["sha256"] != wanted:
            raise ValueError("frozen semantic source changed: "+name)
    return {"driver": static.identity(__file__), "frozen_inputs_and_helpers": found,
            "complete_original_semantic_dependencies": layer.source_identity()}


def subset_decode(ring, data, names):
    names = set(names)
    if not names.issubset(data["roots"]) or not names.issubset(data["original_root_sha256"]):
        raise ValueError("missing bound original root")
    return old.decode_expressions(ring, {**data,
        "roots": {k: data["roots"][k] for k in names},
        "original_root_sha256": {k: data["original_root_sha256"][k] for k in names}})


def bind_input(which, directory, report):
    spec = INPUTS[which]
    main_path, receipt_path = directory/spec["main"], directory/"receipt.json"
    main = layer.read_bound_json(main_path, {"bytes": spec["main_bytes"], "sha256": spec["main_sha"]})
    raw_receipt = static.checked_bytes(receipt_path, 100000)
    if sha(raw_receipt) != spec["receipt_sha"]:
        raise ValueError("bound publication receipt changed: "+which)
    receipt = json.loads(raw_receipt)
    metadata = main.get(spec["metadata"]) or (main.get("checkpoint") or {}).get(spec["metadata"]) or {}
    if (main.get("schema") != spec["schema"]
        or any(metadata.get(k) != v for k,v in spec["export"].items())
        or (which != "static" and main.get("completion") != "complete")):
        raise ValueError("completed original input identity/scope: "+which)
    driver = report["source_hashes"]["frozen_inputs_and_helpers"][spec["driver"]]
    if main.get("source_hashes", {}).get("driver") != driver:
        raise ValueError("original producer identity changed: "+which)
    binding = layer.check_publication(receipt, run=spec["run"], commit=spec["commit"],
        lane=spec["lane"], driver=driver, main_name=spec["main"],
        main_info={"bytes": spec["main_bytes"], "sha256": spec["main_sha"]}, export_info=metadata)
    # The old static small fallback lacks run/source fields; its receipt supplies them.
    for obj in (main,):
        if obj.get("github_run_id") is not None and str(obj["github_run_id"]) != spec["run"]:
            raise ValueError("input run changed")
        if obj.get("github_sha") is not None and obj["github_sha"] != spec["commit"]:
            raise ValueError("input source commit changed")
    data = layer.read_bound_export(directory/metadata["filename"], metadata)
    if (data.get("schema") != spec["schema"]+"-original-expressions"
        or data.get("content_scope") != spec["scope"]
        or data.get("source_hashes") != main["source_hashes"]):
        raise ValueError("complete original export scope/source: "+which)
    if which != "static" and (str(data.get("github_run_id")) != spec["run"]
                              or data.get("github_sha") != spec["commit"]):
        raise ValueError("complete original export run/source")
    report.setdefault("inputs", {})[which] = {
        "publication": binding, "main": {"filename": spec["main"], "bytes": spec["main_bytes"],
        "sha256": spec["main_sha"]}, "receipt_sha256": spec["receipt_sha"],
        "original_export": metadata, "producer_completion": main.get("completion")}
    return main, data


def split_key(key):
    key = tuple(key)
    if len(key) == 8:
        key += (0,0)
    if (len(key) != 10 or any(not isinstance(v,int) for v in key)
        or any(key[i] < 0 for i in range(1,10))):
        raise ValueError("complete Laurent/log ten-coordinate key required")
    return tuple(key[i] for i in (0,1,2,7)), tuple(key[i] for i in (3,4,5,6,8,9))


def add_term(terms, key, value):
    terms[key] = terms.get(key, value.ring.number(0)) + value
    if not terms[key].terms:
        del terms[key]


def scalar_add(terms, key, value):
    terms[key] = terms.get(key, F(0)) + value
    if not terms[key]:
        del terms[key]


def state_value(key, state):
    h,k,omega = state
    if h != 1:
        raise ValueError("the fixed reference evaluations use h=1 exactly")
    return F(0) if key[3] else k**key[1]*omega**key[2]


def evaluate_field(field, state):
    return sum((state_value(key,state)*value for key,value in field.terms.items()),
               field.ring.number(0))


def scalar_times(field_scalar, value):
    return Field(value.ring, {key: coefficient*value for key,coefficient in field_scalar.items()})


def horizontal(poly, degree):
    ring = next(iter(poly.values())).ring
    out = {i: Field(ring) for i in range(degree+2)}
    for i,field in poly.items():
        out[i+1] = out[i+1].add(field.X())
        out[i] = out[i].add(field.Y())
    return out


def normalize_v2(groups, ring):
    get = lambda name: Field(ring, groups.get(name, {}))
    p,q = get("p"),get("q")
    return {2:get("q20").add(p.X(),-1),
            1:get("q11").add(p.Y(),-1).add(q.X(),-1),
            0:get("q02").add(q.Y(),-1)}


def normalize_v4_quartic(groups, ring):
    get = lambda name: Field(ring, groups.get(name, {}))
    b = {2:get("beta_hh"),1:get("beta_hk").add(get("beta_kh")),0:get("beta_kk")}
    c = {3:get("C_h_20"),2:get("C_h_11").add(get("C_k_20")),
         1:get("C_h_02").add(get("C_k_11")),0:get("C_k_02")}
    dc = horizontal(c,3)
    ddb = horizontal(horizontal(b,2),3)
    return {i:get("q4_"+str(i)).add(dc[i],F(-1,3)).add(ddb[i],F(1,3)) for i in range(5)}


def read_matrix(data):
    if data.get("pointwise_matrix_coordinate_order") != list(exact.PARAMETERS):
        raise ValueError("eight matrix coordinate order changed")
    matrix = {0:[{} for _ in range(8)],2:[{} for _ in range(8)]}
    rows = data.get("pointwise_matrix_original_coefficients") or []
    if len(rows) != 8:
        raise ValueError("all eight original matrix coordinates required")
    for a,entries in enumerate(rows):
        for row in entries:
            state,jets = split_key(row["geometry_key"])
            degree = row["geometry_derivative_weight"]
            if degree not in matrix or any(jets[2:]) or sum(jets[:2]) != degree:
                raise ValueError("m0/m2 contain an unsupported jet")
            token = (state,jets[:2])
            if token in matrix[degree][a]:
                raise ValueError("duplicate original matrix coefficient")
            matrix[degree][a][token] = F(row["coefficient"])
    if any(matrix[2][a] for a in range(3)):
        raise ValueError("m2 has unexpected p0/p1/p2 coordinates")
    return matrix


def restore_static(ring, grade, data):
    if (data.get("geometry_names") != list(old.local.NAMES)
        or data.get("projection") != "derivative weight zero"
        or Counter(str(r["mode"]) for r in data["local_roots"]) != Counter({"-4":197,"-2":197})):
        raise ValueError("complete old static density coverage changed")
    records = data["local_roots"]
    roots = subset_decode(ring,data,[row["root"] for row in records])
    terms = {mode:{} for mode in MODES}
    for row in records:
        state,jets = split_key(row["geometry_key"])
        if any(jets) or state in terms[row["mode"]]:
            raise ValueError("duplicate/nonstatic original L0 key")
        terms[row["mode"]][state] = grade.project(roots[row["root"]],WEIGHT)
    return {mode:Field(ring,items) for mode,items in terms.items()}


def restore_factors(ring, grade, data):
    if (data.get("geometry_names") != list(layer.factors.GEOMETRY_NAMES)
        or data.get("real_s_derivatives_before_history_zero") is not True
        or data.get("potential_two_assumed_in_W") is not False):
        raise ValueError("complete real-derivative factor semantics changed")
    matrix = read_matrix(data)
    potential = data["potential_records"]
    if Counter(row["geometry_derivative_weight"] for row in potential) != Counter({0:79,2:93}):
        raise ValueError("all 79 N0 and 93 unreduced N2 records required")
    names = {row["root"] for row in potential}
    selected = []
    counts = Counter()
    patterns2 = {(0,0,1,0,0,0):"p",(0,0,0,1,0,0):"q",
                 (2,0,0,0,0,0):"q20",(1,1,0,0,0,0):"q11",(0,2,0,0,0,0):"q02"}
    seen = set()
    for row in data["local_generator_records"]:
        mode,dw,key = row["mode"],row["geometry_derivative_weight"],tuple(row["geometry_key"])
        if mode not in MODES or dw not in (2,4) or (mode,key) in seen:
            raise ValueError("complete v2/v4 mode/key coverage")
        seen.add((mode,key));counts[(mode,dw)]+=1
        state,jets = split_key(key)
        if dw == 2:
            if jets not in patterns2:
                raise ValueError("undeclared complete v2 jet")
            tag = patterns2[jets]
        else:
            tag,state2 = layer.shape(key)
            if state != state2:
                raise ValueError("horizontal state coordinates changed")
            if tag in ("A_hh","A_hk","A_kk"):
                continue
            if tag == "velocity_quartic_not_consumed":
                tag = "q4_"+str(jets[0])
        names.add(row["root"])
        selected.append((mode,dw,tag,state,row["root"]))
    if counts != Counter({(-4,2):665,(-2,2):665,(-4,4):1236,(-2,4):1236}):
        raise ValueError("3974-factor generator coverage changed")
    if Counter((m,w) for m,w,_,_,_ in selected) != Counter({(-4,2):665,(-2,2):665,(-4,4):1038,(-2,4):1038}):
        raise ValueError("only raw B/C/Q v4 blocks should be newly consumed")
    roots = subset_decode(ring,data,names)
    nrows = []
    nseen = set()
    for row in potential:
        state,jets = split_key(row["geometry_key"])
        dw = row["geometry_derivative_weight"]
        if any(jets[2:]) or sum(jets[:2]) != dw or (dw,tuple(row["geometry_key"])) in nseen:
            raise ValueError("unreduced N factors must be static or velocity quadratic")
        nseen.add((dw,tuple(row["geometry_key"])))
        value = roots[row["root"]]
        if (any(ring.p.weight(m)!=3 for m in value.terms)
            or any(d != (("a",1),("b",1),("c",1)) for d in ring.color_degrees(value))):
            raise ValueError("original N lost exterior/inner slots")
        nrows.append({**row,"state":state,"velocity":jets[:2],
                      "original_sha256":data["original_root_sha256"][row["root"]],
                      "value":value})
    groups = {mode:{2:{},4:{}} for mode in MODES}
    for mode,dw,tag,state,name in selected:
        items = groups[mode][dw].setdefault(tag,{})
        if state in items:
            raise ValueError("duplicate selected original v coefficient")
        items[state] = grade.project(roots[name],WEIGHT)
    return nrows,groups,matrix


def restore_acceleration(ring, data):
    rows = data.get("selected_weight_records") or []
    if data.get("selected_weight") != WEIGHT or [row["id"] for row in rows] != list(range(10)):
        raise ValueError("the completed ten weight -2 acceleration records are required")
    names = [name for row in rows for name in row["roots"].values()]
    roots = subset_decode(ring,data,names)
    out = {mode:{family:{} for family in layer.FAMILIES} for mode in MODES}
    for row in rows:
        for mode in MODES:
            value = roots[row["roots"][str(mode)]]
            if ring.digest(value) != row["original_mode_sha256"][str(mode)]:
                raise ValueError("published acceleration original hash changed")
            for alias in row["aliases"]:
                family,key = alias["family"],tuple(alias["state_key"])
                if family not in out[mode] or key in out[mode][family]:
                    raise ValueError("acceleration aliases overlap or change family")
                out[mode][family][key] = value
    return {mode:{family:Field(ring,terms) for family,terms in families.items()}
            for mode,families in out.items()}


def restore_responses(ring, main, data):
    checkpoint = main.get("checkpoint") or {}
    upper = checkpoint.get("response_upper_bound") or {}
    witness = checkpoint.get("dual_certificate") or {}
    if (checkpoint.get("requested_weight")!=WEIGHT or checkpoint.get("requested_order")!=3
        or upper.get("retained_original_columns")!=R_RETAINED
        or upper.get("original_columns")!=50 or upper.get("proved_true_response_dimension_upper_bound")!=40
        or upper.get("verified_original_dependency_count")!=10
        or not witness.get("rational_nonmembership_certified")
        or witness.get("modular_control_rank")!=40 or not witness.get("modular_pivot_determinant")):
        raise ValueError("the already proved complete forty-dimensional R_-2 basis is required")
    records = data.get("column_records") or []
    if len(records)!=50 or not data.get("all_compiled_original_columns_included"):
        raise ValueError("published full response block coverage changed")
    selected = [records[i] for i in R_RETAINED]
    roots = subset_decode(ring,data,[name for row in selected for name in row["roots"].values()])
    result = []
    for index,row in zip(R_RETAINED,selected):
        if row["index"]!=index:
            raise ValueError("old response column order changed")
        modes = {mode:roots[row["roots"][str(mode)]] for mode in MODES}
        if any(ring.digest(modes[mode])!=row["original_mode_sha256"][str(mode)] for mode in MODES):
            raise ValueError("old retained response original hash changed")
        result.append({"original_column":index,"label":row["label"],"modes":modes})
    return result


def build_plan(ring, grade, nrows):
    entries, requests, projected = {}, {}, {}
    for row in nrows:
        indices = range(8) if row["geometry_derivative_weight"]==2 else range(3,8)
        for a in indices:
            wanted = WEIGHT-blocks.PARAMETER_WEIGHTS[a]
            key = (row["root"],wanted)
            if key not in projected:
                projected[key] = grade.project(row["value"],wanted)
            value = projected[key]
            request = (row["root"],a)
            if not value.terms:
                requests[request] = None
                continue
            digest = ring.digest(value)
            token = str(a)+":"+digest
            entry = entries.setdefault(token,{
                "token":token,"parameter_index":a,"parameter_name":exact.PARAMETERS[a],
                "parameter_weight":blocks.PARAMETER_WEIGHTS[a],
                "third_weight":wanted,"result_weight":WEIGHT,
                "projected_third_sha256":digest,"uses":[],"template":value})
            entry["uses"].append({"potential_derivative_weight":row["geometry_derivative_weight"],
                "root":row["root"],"geometry_key":row["geometry_key"],
                "original_sha256":row["original_sha256"]})
            requests[request] = token
    ordered = sorted(entries.values(),key=lambda x:(x["parameter_index"],x["projected_third_sha256"]))
    for index,entry in enumerate(ordered):
        entry["plan_index"] = index
        entry["uses"].sort(key=lambda x:(x["potential_derivative_weight"],x["root"]))
    public = [{k:v for k,v in entry.items() if k!="template"} for entry in ordered]
    return ordered,requests,public,sha(canonical(public))


def seed_axis_cache(ring, grade, data, nrows, requests):
    names = ["N2_axis_hm2","N2_axis_hm4"]+[
        "new_response_"+name+"_"+str(mode) for name in ("r1","t1") for mode in MODES]
    roots = subset_decode(ring,data,names)
    by_key = {tuple(row["geometry_key"]):row for row in nrows}
    cache = {}
    for hpower,parameter,suffix in ((-2,"r1","hm2"),(-4,"t1","hm4")):
        key = (hpower,0,0,2,0,0,0,0,0,0)
        row = by_key.get(key)
        if not row or ring.digest(roots["N2_axis_"+suffix])!=row["original_sha256"]:
            raise ValueError("old axis contraction input must equal the exact stored unreduced N2 root")
        a = exact.PARAMETERS.index(parameter)
        token = requests[(row["root"],a)]
        modes = {mode:grade.project(roots["new_response_"+parameter+"_"+str(mode)],WEIGHT) for mode in MODES}
        if token is None:
            if any(value.terms for value in modes.values()):
                raise ValueError("zero projected input has a nonzero archived projected contraction")
            continue
        cache[token] = {"modes":modes,"origin":"published-axis-cache"}
    return cache


def coordinate_polynomials(matrix, inverse):
    result = {dw:[{} for _ in range(8)] for dw in (0,2)}
    for dw in (0,2):
        for i in range(8):
            for a in range(8):
                if not inverse[i][a]:
                    continue
                for key,value in matrix[dw][a].items():
                    scalar_add(result[dw][i],key,inverse[i][a]*value)
    return result


def coefficient_scalar(coordinates, i, velocity):
    return {state:value for (state,jets),value in coordinates[i].items() if jets==velocity}


def subtract_matrix_responses(fields, degree, nrows, nweight, matrix, mweight, requests, cache):
    """Only geometry multiplication; the same stored response feeds L2 and L4."""
    for row in nrows:
        if row["geometry_derivative_weight"] != nweight:
            continue
        for a,scalar_terms in enumerate(matrix[mweight]):
            if not scalar_terms:
                continue
            request = (row["root"],a)
            if request not in requests:
                raise ValueError("matrix contraction has no declared input/weight request")
            token = requests[request]
            if token is None:
                continue  # Its declared true-weight input was exactly the empty original expression.
            if token not in cache:
                raise ValueError("uncompleted contraction must never be interpreted as zero")
            for (mstate,mvelocity),amount in scalar_terms.items():
                velocity = tuple(x+y for x,y in zip(row["velocity"],mvelocity))
                if sum(velocity) != degree:
                    raise ValueError("complete matrix contraction changed derivative degree")
                state = tuple(x+y for x,y in zip(row["state"],mstate))
                for mode in MODES:
                    add_term(fields[mode][velocity[0]],state,-amount*cache[token]["modes"][mode])


def assemble_families(ring, vgroups, nrows, matrix, coordinates, requests, cache, static_fields, acceleration):
    refs = {mode:[evaluate_field(static_fields[mode],state) for state in constrained.BASIS_STATES]
            for mode in MODES}
    out = {mode:{} for mode in MODES}
    q2 = {mode:{i:dict(field.terms) for i,field in normalize_v2(vgroups[mode][2],ring).items()}
          for mode in MODES}
    q4 = {mode:{i:dict(field.terms) for i,field in normalize_v4_quartic(vgroups[mode][4],ring).items()}
          for mode in MODES}
    subtract_matrix_responses(q2,2,nrows,2,matrix,0,requests,cache)
    subtract_matrix_responses(q2,2,nrows,0,matrix,2,requests,cache)
    subtract_matrix_responses(q4,4,nrows,2,matrix,2,requests,cache)
    for mode in MODES:
        f0 = static_fields[mode]
        for i,value in enumerate(refs[mode]):
            f0 = f0.add(scalar_times(coefficient_scalar(coordinates[0],i,(0,0)),value),-1)
            for j in range(3):
                field = scalar_times(coefficient_scalar(coordinates[2],i,(j,2-j)),value)
                for key,term in field.terms.items():
                    add_term(q2[mode][j],key,-term)
        if any(evaluate_field(f0,state).terms for state in constrained.BASIS_STATES):
            raise ValueError("new original static normalization did not vanish at its eight fixed references")
        out[mode]["F0"] = f0
        out[mode].update({"Q2_"+str(i):Field(ring,q2[mode][i]) for i in range(3)})
        out[mode].update(acceleration[mode])
        out[mode].update({"Q4_"+str(i):Field(ring,q4[mode][i]) for i in range(5)})
        if set(out[mode]) != set(FAMILIES):
            raise ValueError("all fourteen normal families are required")
    return out,refs


class LinearVector:
    """Exact coordinates in the newly exported original coefficient list."""
    def __init__(self, ring, terms=None):
        self.ring = ring
        self.terms = {int(i):F(c) for i,c in (terms or {}).items() if c}
    def __add__(self, other):
        if other == 0:
            return self
        if not isinstance(other,LinearVector) or other.ring is not self.ring:
            raise ValueError("same formal coefficient list required")
        terms = dict(self.terms)
        for i,c in other.terms.items():
            scalar_add(terms,i,c)
        return LinearVector(self.ring,terms)
    __radd__ = __add__
    def __neg__(self):
        return LinearVector(self.ring,{i:-c for i,c in self.terms.items()})
    def __sub__(self,other):
        return self+(-other)
    def __mul__(self,amount):
        amount = F(amount)
        return LinearVector(self.ring,{i:amount*c for i,c in self.terms.items()})
    __rmul__ = __mul__
    def __truediv__(self,amount):
        return self*(1/F(amount))


class LinearRing:
    def number(self, value):
        if value:
            raise ValueError("no free constant in a list of profile vectors")
        return LinearVector(self)
    def unit(self, index):
        return LinearVector(self,{index:F(1)})
    def digest(self, value):
        return sha(canonical([[i,str(c)] for i,c in sorted(value.terms.items())]))


def original_coefficient_list(ring, families):
    records,values,linear_fields = [],[],{}
    lin = LinearRing()
    for family in FAMILIES:
        keys = sorted(set(families[-4][family].terms)|set(families[-2][family].terms))
        terms = {}
        for key in keys:
            modes = {mode:families[mode][family].terms.get(key,ring.number(0)) for mode in MODES}
            if not any(value.terms for value in modes.values()):
                continue
            index = len(records)
            records.append({"index":index,"family":family,"state_key":list(key),
                "weight":WEIGHT,"original_mode_sha256":{str(m):ring.digest(v) for m,v in modes.items()}})
            values.append(modes);terms[key]=lin.unit(index)
        linear_fields[family] = Field(lin,terms)
    return records,values,linear_fields


def translation_presentation(linear_fields, coordinates, states):
    lin = linear_fields["F0"].ring
    cref = [evaluate_field(linear_fields["F0"].partial(2),state) for state in states]
    den = {}
    for family in FAMILIES:
        field = linear_fields[family].partial(2)
        if family=="F0" or family.startswith("Q2_"):
            dw,velocity = (0,(0,0)) if family=="F0" else (2,(int(family[-1]),2-int(family[-1])))
            for i,value in enumerate(cref):
                field = field.add(scalar_times(coefficient_scalar(coordinates[dw],i,velocity),value),-1)
        den[family] = field
    rows = []
    for family in FAMILIES:
        for key,value in sorted(den[family].terms.items()):
            rows.append({"family":family,"state_key":list(key),
                "coefficients":[[i,str(c)] for i,c in sorted(value.terms.items())]})
    correction = [{"reference_index":i,"coefficients":[[j,str(c)] for j,c in sorted(value.terms.items())]}
                  for i,value in enumerate(cref)]
    sref = [evaluate_field(linear_fields["F0"].X(),state)-state[2]*cref[i]
            for i,state in enumerate(states)]
    scaling = [{"reference_index":i,"coefficients":[[j,str(c)] for j,c in sorted(value.terms.items())]}
               for i,value in enumerate(sref)]
    return rows,correction,scaling


def serialize_coordinates(coordinates):
    return {str(dw):[[{"state_key":list(state),"velocity":list(velocity),"coefficient":str(value)}
             for (state,velocity),value in sorted(terms.items())] for terms in values]
            for dw,values in coordinates.items()}


def write_originals(args, report, ctx):
    if "plan" not in ctx:
        return
    ring,cache = ctx["ring"],ctx["cache"]
    stamp = (tuple(sorted(cache)),bool(ctx.get("normal_records") is not None))
    if ctx.get("saved_stamp")==stamp:
        return
    named,cache_rows = {},[]
    for entry in ctx["plan"]:
        token = entry["token"]
        if token not in cache:
            continue
        index = entry["plan_index"]
        tname = "cache_%04d_input"%index
        named[tname] = entry["template"]
        names = {str(mode):"cache_%04d_mode_%d"%(index,mode) for mode in MODES}
        for mode in MODES:
            named[names[str(mode)]] = cache[token]["modes"][mode]
        cache_rows.append({"plan_index":index,"token":token,"projected_input_root":tname,
            "projected_third_sha256":entry["projected_third_sha256"],
            "roots":names,"origin":cache[token]["origin"],
            "original_mode_sha256":{str(m):ring.digest(v) for m,v in cache[token]["modes"].items()}})
    normal = []
    for record,modes in zip(ctx.get("normal_records") or [],ctx.get("normal_values") or []):
        names = {str(mode):"normal_%05d_mode_%d"%(record["index"],mode) for mode in MODES}
        for mode in MODES:
            named[names[str(mode)]] = modes[mode]
        normal.append({**record,"roots":names})
    response = []
    if ctx.get("normal_records") is not None:
        for row in ctx["responses"]:
            names = {str(mode):"archived_R_%02d_mode_%d"%(row["original_column"],mode) for mode in MODES}
            for mode in MODES:
                named[names[str(mode)]] = row["modes"][mode]
            response.append({"original_column":row["original_column"],"label":row["label"],"roots":names})
        for mode in MODES:
            for i,value in enumerate(ctx["references"][mode]):
                named["static_reference_%d_mode_%d"%(i,mode)] = value
    complete = ctx.get("normal_records") is not None
    scope = "complete-fourteen-weight-minus2-families-and-translation-presentation" if complete else "partial-weight-minus2-contraction-cache"
    data = {"schema":SCHEMA+"-original-expressions","content_scope":scope,
        "github_repository":REPOSITORY,"github_run_id":report["github_run_id"],"github_sha":report["github_sha"],
        "source_hashes":report["source_hashes"],"input_identity_sha256":ctx["input_identity"],
        "input_bindings":report["inputs"],"target_weight":WEIGHT,
        "contraction_plan":ctx["public_plan"],"contraction_plan_sha256":ctx["plan_sha"],
        "planned_contractions":len(ctx["plan"]),"completed_contractions":len(cache),
        "all_planned_contractions_present":len(cache)==len(ctx["plan"]),
        "cache_records":cache_rows,"normal_family_records":normal,
        "archived_R_basis_records":response,"all_fourteen_families_complete":complete,
        "head_translation_presentation":ctx.get("translation_rows") or [],
        "static_translation_reference_coefficients":ctx.get("translation_reference") or [],
        "static_scaling_reference_coefficients":ctx.get("scaling_reference") or [],
        "reference_matrix":ctx.get("reference_matrix"),
        "eight_reference_coordinate_polynomials":ctx.get("serialized_coordinates"),
        "pure_and_balanced_both_required_for_later_identities":True,
        "function_space_rank_computed":False,"positive_character_decided":False,
        **old.serialize_expressions(ring,named)}
    raw = canonical(data)
    if len(raw)>40000000:
        raise formal.CompilationBudgetExceeded("portable original presentation raw byte ceiling")
    packed = gzip.compress(raw,mtime=0)
    if len(packed)>args.max_export_bytes:
        raise formal.CompilationBudgetExceeded("portable original presentation gzip byte ceiling")
    path = args.output.with_name(args.output.stem+"-original-expressions.json.gz")
    path.parent.mkdir(parents=True,exist_ok=True)
    temp = path.with_name(path.name+".tmp")
    temp.write_bytes(packed);temp.replace(path)
    report["portable_head_export"] = {
        "filename":path.name,"stored_bytes":len(packed),"stored_sha256":sha(packed),
        "raw_bytes":len(raw),"raw_sha256":sha(raw),"root_count":len(named),
        "profile_atom_count":len(data["profile_atoms"]),"content_scope":scope,"persisted":True,
        "completed_contractions":len(cache),"planned_contractions":len(ctx["plan"]),
        "all_fourteen_families_complete":complete,"normal_records":len(normal),
        "translation_relation_records":len(data["head_translation_presentation"])}
    ctx["saved_stamp"] = stamp


def merge_bound_cache(ring, data, plan, public_plan, input_identity, cache):
    if (data.get("schema")!=SCHEMA+"-original-expressions"
        or data.get("input_identity_sha256")!=input_identity
        or data.get("target_weight")!=WEIGHT
        or data.get("contraction_plan")!=public_plan
        or data.get("contraction_plan_sha256")!=sha(canonical(public_plan))
        or data.get("planned_contractions")!=len(plan)):
        raise ValueError("resume cache must bind the exact inputs and true-weight plan")
    if data.get("all_fourteen_families_complete"):
        raise ValueError("a completed head presentation must be consumed directly, not regenerated")
    records = data.get("cache_records") or []
    if len(records)!=data.get("completed_contractions"):
        raise ValueError("partial cache count changed")
    by_token = {entry["token"]:entry for entry in plan}
    seen = set()
    for row in records:
        token = row["token"]
        if token not in by_token or token in seen:
            raise ValueError("duplicate or undeclared cached contraction")
        seen.add(token)
        entry = by_token[token]
        if row["plan_index"]!=entry["plan_index"] or row["projected_third_sha256"]!=entry["projected_third_sha256"]:
            raise ValueError("cached contraction type/input mismatch")
    names = [name for row in records for name in [row["projected_input_root"],*row["roots"].values()]]
    roots = subset_decode(ring,data,names)
    for row in records:
        token = row["token"]
        if ring.digest(roots[row["projected_input_root"]])!=by_token[token]["projected_third_sha256"]:
            raise ValueError("cached projected input original hash changed")
        modes = {mode:roots[row["roots"][str(mode)]] for mode in MODES}
        if any(ring.digest(v)!=row["original_mode_sha256"][str(m)] for m,v in modes.items()):
            raise ValueError("cached response original hash changed")
        if token in cache and any(ring.digest(cache[token]["modes"][m])!=ring.digest(v) for m,v in modes.items()):
            raise ValueError("two published caches disagree on the same original contraction")
        cache[token] = {"modes":modes,"origin":"published-resume-cache"}
    return len(records)


def restore_resume(args, report, ctx):
    if args.resume_report is None:
        return
    raw = static.checked_bytes(args.resume_report,100000)
    pubraw = static.checked_bytes(args.resume_publication,100000)
    if sha(raw)!=args.resume_report_sha256 or sha(pubraw)!=args.resume_publication_sha256:
        raise ValueError("resume main/receipt explicit identity changed")
    main,publication = json.loads(raw),json.loads(pubraw)
    metadata = main.get("portable_head_export") or {}
    if (main.get("schema")!=SCHEMA or main.get("source_hashes")!=report["source_hashes"]
        or str(main.get("github_run_id"))!=args.resume_run or main.get("github_sha")!=args.resume_commit
        or not metadata.get("persisted")):
        raise ValueError("resume must be a published artifact of this exact frozen consumer")
    binding = layer.check_publication(publication,run=args.resume_run,commit=args.resume_commit,
        lane="character_head_minus2",driver=report["source_hashes"]["driver"],
        main_name=args.resume_report.name,main_info={"bytes":len(raw),"sha256":sha(raw)},export_info=metadata)
    data = layer.read_bound_export(args.resume_export,metadata)
    if (data.get("source_hashes")!=report["source_hashes"]
        or str(data.get("github_run_id"))!=args.resume_run or data.get("github_sha")!=args.resume_commit):
        raise ValueError("resume original export source/run changed")
    count = merge_bound_cache(ctx["ring"],data,ctx["plan"],ctx["public_plan"],
                             ctx["input_identity"],ctx["cache"])
    report["resume"] = {"publication":binding,"complete_export":metadata,
                        "completed_contractions_restored_without_recalculation":count}


def study(args, report, ctx):
    limits = exact.Limits(seconds=args.max_seconds,nodes=500000,atoms=120000,
                          terms=150000,rewrites=1000000,memory_mib=args.memory_mib,rational_bits=8192)
    ring = colored.ColoredRing(limits);grade = blocks.ScalingGrading(ring)
    ctx["ring"] = ring
    report["phase"] = "read_published_static_originals"
    _,data = bind_input("static",args.static_directory,report)
    static_fields = restore_static(ring,grade,data);del data
    report["phase"] = "read_published_complete_N0_N2_and_selected_v2_v4_originals"
    _,data = bind_input("factors",args.factors_directory,report)
    nrows,groups,matrix = restore_factors(ring,grade,data);del data
    report["phase"] = "read_published_ten_weight_minus2_acceleration_coefficients"
    _,data = bind_input("acceleration",args.acceleration_directory,report)
    acceleration = restore_acceleration(ring,data);del data
    report["phase"] = "read_published_forty_original_response_columns_without_rebuilding"
    rmain,data = bind_input("response",args.response_directory,report)
    ctx["responses"] = restore_responses(ring,rmain,data);del data,rmain
    report["phase"] = "plan_only_required_true_weight_contractions"
    plan,requests,public_plan,plan_sha = build_plan(ring,grade,nrows)
    _,axisdata = bind_input("axis",args.axis_directory,report)
    cache = seed_axis_cache(ring,grade,axisdata,nrows,requests);del axisdata
    ctx.update(plan=plan,requests=requests,public_plan=public_plan,plan_sha=plan_sha,cache=cache,
               input_identity=sha(canonical(report["inputs"])))
    report["input_identity_sha256"] = ctx["input_identity"]
    report["contraction_plan"] = {"sha256":plan_sha,"distinct_nonzero_projected_inputs":len(plan),
        "declared_requests_before_filtering":len(requests),
        "exact_zero_projected_requests":sum(value is None for value in requests.values()),
        "archived_axis_cache_entries":len(cache),"true_result_weight":WEIGHT,
        "required_third_weight_by_quadratic":{
            name:WEIGHT-blocks.PARAMETER_WEIGHTS[i] for i,name in enumerate(exact.PARAMETERS)},
        "N2_pool_shared_by_L2_and_L4":True,"N0_directions":list(exact.PARAMETERS[3:]),
        "complete_plan_saved_in_original_export":True}
    restore_resume(args,report,ctx)
    write_originals(args,report,ctx)
    report["phase"] = "only_missing_true_weight_N_contractions"
    quadratics = exact.operator_basis(ring)
    new_count = 0
    for entry in plan:
        token = entry["token"]
        if token in cache:
            continue
        limits.formal.time_check()
        value = blocks.full_response(ring,colored.ThirdOperator(ring,entry["template"]),
                                     quadratics[entry["parameter_index"]])
        if any(set(grade.split(expr))-{WEIGHT} for expr in value.values()):
            raise ValueError("new contraction violated its declared true output weight")
        if any(any(ring.p.weight(m)!=4 for m in expr.terms) for expr in value.values()):
            raise ValueError("new contraction lost complete fourth profile degree")
        cache[token] = {"modes":value,"origin":"new-required-contraction"}
        new_count += 1
        report["new_contractions_completed"] = new_count
        if new_count % args.checkpoint_every == 0:
            write_originals(args,report,ctx)
    write_originals(args,report,ctx)
    if len(cache)!=len(plan):
        raise ValueError("all declared required contractions must exist before family assembly")
    report["phase"] = "assemble_nine_missing_families_and_reuse_five_archived_families"
    _,reference_info = constrained.reference_coordinates()
    inverse = [[F(v) for v in row] for row in reference_info["inverse"]]
    coordinates = coordinate_polynomials(matrix,inverse)
    families,refs = assemble_families(ring,groups,nrows,matrix,coordinates,requests,cache,
                                    static_fields,acceleration)
    records,values,linear = original_coefficient_list(ring,families)
    translation,cref,sref = translation_presentation(linear,coordinates,constrained.BASIS_STATES)
    ctx.update(normal_records=records,normal_values=values,references=refs,
        translation_rows=translation,translation_reference=cref,scaling_reference=sref,
        reference_matrix=reference_info,serialized_coordinates=serialize_coordinates(coordinates))
    report["assembly_complete_before_storage"] = True
    write_originals(args,report,ctx)
    report["normal_presentation"] = {
        "families":list(FAMILIES),"normal_records":len(records),
        "records_by_family":dict(Counter(row["family"] for row in records)),
        "translation_relation_records":len(translation),
        "translation_relations_by_family":dict(Counter(row["family"] for row in translation)),
        "all_fourteen_families_complete":True,
        "eight_reference_static_values_originally_zero":True,
        "same_matrix_normalization_used_in_L0_and_L2":True,
        "low_translation_is_domega_minus_same_cocycle":True,
        "static_translation_reference_derivatives":8,"static_scaling_reference_derivatives":8,
        "adjacent_weight_minus1_targets_constructed":False,
        "new_profile_translation_compositions":False,
        "original_full_modes_saved":[-4,-2],
        "R_minus2_existing_true_dimension":40,
        "normal_state_records_are_not_claimed_independent":True,
        "head_dimension_or_positive_character_not_yet_decided":True}
    report["checkpoint"] = {
        "outcome":"complete_original_weight_minus2_head_generating_presentation",
        "theorem":"R163 U_sigma=R_sigma+T_sigma and R_sigma+N U_(sigma+1)=R_sigma+D_sigma",
        "target_weight":WEIGHT,"complete_original_generation":True,
        "function_space_rank_computed":False,"positive_character_excluded":False,
        "J6_head_class_decided":False,"next_problem":"sound new relations and full-character necessary positivity"}
    report.update(completion="complete",phase="complete_original_generating_presentation",
        new_contractions_completed=new_count,new_response_cache_entries=len(cache),
        head_generation_complete=True,task_complete=False)


def toy_only():
    limits = exact.Limits(seconds=40,nodes=25000,atoms=15000,terms=15000,rewrites=10000,memory_mib=384)
    ring = colored.ColoredRing(limits);grade=blocks.ScalingGrading(ring)
    q = ring.color("q");phi=q*q*q*q
    checks = {}
    def eqfield(a,b,label):
        if a.add(b,-1).terms:
            raise AssertionError(label)
        checks[label]=True
    def zero_poly(poly,label):
        if any(field.terms for field in poly.values()):
            raise AssertionError(label)
        checks[label]=True
    f = Field(ring,{(-2,0,1,1):phi})
    eqfield(f.Y().X().add(f.X().Y(),-1),f.partial(2).shift_h(-2).scale(F(-1,2)),
            "real_horizontal_XY_commutator_and_log_chain")
    g = Field(ring,{(-1,1,2,0):phi})
    v2={"p":f.terms,"q":g.terms,"q20":f.X().terms,
        "q11":f.Y().add(g.X()).terms,"q02":g.Y().terms}
    zero_poly(normalize_v2(v2,ring),"complete_artificial_linear_acceleration_boundary_removed")
    v4={"beta_hh":f.terms,"C_h_20":f.X().terms,"C_h_11":f.Y().terms}
    zero_poly(normalize_v4_quartic(v4,ring),"complete_artificial_third_jet_potential_removed_from_Q4")
    v4={"C_h_11":g.scale(2).terms,"C_k_20":g.terms,"q4_3":g.X().terms,"q4_2":g.Y().terms}
    zero_poly(normalize_v4_quartic(v4,ring),"complete_artificial_velocity_cubic_boundary_removed")
    a,b,c=(ring.color(name) for name in ("a","b","c"))
    third=a*b*c+a.D()*b*c
    nrows=[]
    for dw,name,vel,key in ((0,"artN0",(0,0),(0,)*10),
                            (2,"artN2",(2,0),(0,0,0,2,0,0,0,0,0,0))):
        nrows.append({"geometry_derivative_weight":dw,"root":name,"geometry_key":list(key),
            "state":STATE_ZERO,"velocity":vel,"original_sha256":ring.digest(third),"value":third})
    plan,requests,public_plan,plan_sha=build_plan(ring,grade,nrows)
    if len(plan)!=4 or {row["parameter_index"] for row in plan}!={0,4,5,6}:
        raise AssertionError("single-weight plan should exclude all undeclared third weights")
    if requests[("artN0",4)]!=requests[("artN2",4)]:
        raise AssertionError("identical actual projected input should share one N0/N2 cache")
    checks["single_true_weight_filter_and_cross_factor_cache_dedup"]=True
    entry=next(row for row in plan if row["parameter_index"]==4)
    response=blocks.full_response(ring,colored.ThirdOperator(ring,entry["template"]),exact.operator_basis(ring)[4])
    if any(set(grade.split(value))-{WEIGHT} for value in response.values()):
        raise AssertionError("artificial true-weight response covariance")
    checks["artificial_exterior_inner_response_preserves_output_weight"]=True
    named={"input":entry["template"],**{str(mode):response[mode] for mode in MODES}}
    data={"schema":SCHEMA+"-original-expressions","input_identity_sha256":"a"*64,
        "target_weight":WEIGHT,"contraction_plan":public_plan,"contraction_plan_sha256":plan_sha,
        "planned_contractions":len(plan),"completed_contractions":1,"all_fourteen_families_complete":False,
        "cache_records":[{"token":entry["token"],"plan_index":entry["plan_index"],
            "projected_third_sha256":entry["projected_third_sha256"],"projected_input_root":"input",
            "roots":{str(mode):str(mode) for mode in MODES},
            "original_mode_sha256":{str(mode):ring.digest(value) for mode,value in response.items()}}],
        **old.serialize_expressions(ring,named)}
    cache={}
    merge_bound_cache(ring,data,plan,public_plan,"a"*64,cache)
    if set(cache)!={entry["token"]}:
        raise AssertionError("partial archive must not mark uncompleted calls zero")
    checks["partial_original_cache_roundtrip_preserves_pending_calls"]=True
    with tempfile.TemporaryDirectory() as directory:
        artificial_args=argparse.Namespace(output=Path(directory)/"artificial.json",max_export_bytes=100000)
        artificial_report={"github_run_id":None,"github_sha":None,"source_hashes":{"artificial":True},
                           "inputs":{"artificial":True}}
        artificial_ctx={"ring":ring,"cache":cache,"plan":plan,"public_plan":public_plan,
            "plan_sha":plan_sha,"input_identity":"a"*64}
        write_originals(artificial_args,artificial_report,artificial_ctx)
        metadata=artificial_report["portable_head_export"]
        packed=(Path(directory)/metadata["filename"]).read_bytes()
        archived=json.loads(gzip.decompress(packed))
        if (metadata["stored_sha256"]!=sha(packed) or archived["all_fourteen_families_complete"]
            or archived["completed_contractions"]!=1 or archived["planned_contractions"]!=4):
            raise AssertionError("atomic partial original artifact changed completion semantics")
        restored={}
        merge_bound_cache(ring,archived,plan,public_plan,"a"*64,restored)
        if set(restored)!=set(cache):
            raise AssertionError("saved partial artifact cannot restore its exact completed input")
    checks["actual_cache_writer_roundtrip_keeps_partial_scope"]=True
    changed={**data,"contraction_plan_sha256":"b"*64}
    try:
        merge_bound_cache(ring,changed,plan,public_plan,"a"*64,{})
    except ValueError:
        checks["changed_weight_plan_rejected"]=True
    else:
        raise AssertionError("changed plan accepted")
    fake_matrix={0:[{} for _ in range(8)],2:[{} for _ in range(8)]}
    fake_matrix[0][4][(STATE_ZERO,(0,0))]=F(3)
    fake_matrix[2][4][(STATE_ZERO,(2,0))]=F(5)
    terms={mode:{0:{},1:{},2:{STATE_ZERO:20*phi}} for mode in MODES}
    fake_cache={"n0":{"modes":{mode:2*phi for mode in MODES}},
                "n2":{"modes":{mode:phi for mode in MODES}}}
    fake_req={("artN0",4):"n0",("artN2",4):"n2"}
    subtract_matrix_responses(terms,2,nrows,2,fake_matrix,0,fake_req,fake_cache)
    subtract_matrix_responses(terms,2,nrows,0,fake_matrix,2,fake_req,fake_cache)
    for mode in MODES:
        add_term(terms[mode][2],STATE_ZERO,-7*phi)
    if any(terms[mode][2] for mode in MODES):
        raise AssertionError("both N factors and the same Gamma(m2) must survive")
    checks["complete_L2_two_N_factors_and_Gamma_m2_signs"]=True
    try:
        subtract_matrix_responses({m:{0:{},1:{},2:{}} for m in MODES},2,
            nrows,2,fake_matrix,0,fake_req,{})
    except ValueError:
        checks["uncompleted_contraction_is_not_zero"]=True
    else:
        raise AssertionError("missing contraction silently dropped")
    lin=LinearRing()
    omega=Field(lin,{(0,0,1,0):lin.unit(0)})
    fields={name:Field(lin) for name in FAMILIES}
    fields["F0"]=omega;fields["Q2_2"]=omega
    coordinates={0:[{(STATE_ZERO,(0,0)):F(1)}],
                 2:[{(STATE_ZERO,(2,0)):F(1)}]}
    den,cref,sref=translation_presentation(fields,coordinates,[(F(1),F(0),F(0))])
    if den or cref!=[{"reference_index":0,"coefficients":[[0,"1"]]}]:
        raise AssertionError("the shared low-layer cocycle must subtract the reference derivative")
    checks["low_translation_negative_cocycle_in_both_layers"]=True
    logfield=Field(lin,{(0,0,0,1):lin.unit(1)})
    fields["F0"]=logfield
    _,_,sref=translation_presentation(fields,coordinates,[(F(1),F(0),F(0))])
    if sref!=[{"reference_index":0,"coefficients":[[1,"1"]]}]:
        raise AssertionError("log derivative must be taken before h=1 reference evaluation")
    checks["scaling_reference_derivative_keeps_logh_at_h_one"]=True
    return {"all_passed":all(checks.values()),"checks":checks,
            "published_research_inputs_read":False,"real_research_targets_composed":False,
            "only_one_artificial_response_composed":True,"old_basis_or_profile_evaluation_repeated":False}


def write_reports(args, report):
    args.output.parent.mkdir(parents=True,exist_ok=True)
    raw=canonical(report);packed=gzip.compress(raw,mtime=0)
    full=args.output.with_name(args.output.stem+"-complete-report.json.gz")
    used=(report.get("portable_head_export") or {}).get("stored_bytes",0)
    if len(packed)>args.max_full_report_bytes or used+len(packed)+args.max_main_bytes>4800000:
        raise ValueError("bounded complete report cannot be published with its original artifact")
    full.write_bytes(packed)
    info={"filename":full.name,"stored_bytes":len(packed),"stored_sha256":sha(packed),
          "raw_bytes":len(raw),"raw_sha256":sha(raw)}
    compact=dict(report)
    compact["complete_report_file"]=info
    data=canonical(compact)+b"\n"
    if len(data)>args.max_main_bytes:
        for key in ("inputs",):
            value=compact.pop(key,None)
            if value is not None:
                compact[key+"_in_complete_report"]={"sha256":sha(canonical(value))}
        data=canonical(compact)+b"\n"
    if len(data)>=100000 or len(data)>args.max_main_bytes:
        raise ValueError("compact main exceeded its small-text limit")
    args.output.write_bytes(data)
    return {"output":str(args.output),"completion":report["completion"],"bytes":len(data),
            "sha256":sha(data),"complete_report":info}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--output",type=Path,required=True)
    for name,spec in INPUTS.items():
        parser.add_argument("--"+name+"-directory",type=Path,default=TOPIC/"notes"/spec["directory"])
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--checkpoint-every",type=int,default=8)
    parser.add_argument("--max-main-bytes",type=int,default=95000)
    parser.add_argument("--max-full-report-bytes",type=int,default=250000)
    parser.add_argument("--max-export-bytes",type=int,default=4400000)
    parser.add_argument("--resume-report",type=Path)
    parser.add_argument("--resume-publication",type=Path)
    parser.add_argument("--resume-export",type=Path)
    parser.add_argument("--resume-report-sha256")
    parser.add_argument("--resume-publication-sha256")
    parser.add_argument("--resume-run")
    parser.add_argument("--resume-commit")
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.checkpoint_every,args.max_main_bytes,
           args.max_full_report_bytes,args.max_export_bytes)<=0:
        parser.error("positive explicit budgets required")
    if args.max_main_bytes>=100000 or args.max_main_bytes+args.max_full_report_bytes+args.max_export_bytes>4800000:
        parser.error("main <100KB and total published output <=4.8MB required")
    resume=[args.resume_report,args.resume_publication,args.resume_export,args.resume_report_sha256,
            args.resume_publication_sha256,args.resume_run,args.resume_commit]
    if any(value is not None for value in resume) and not all(value is not None for value in resume):
        parser.error("resume requires the complete published run/source/main/receipt/export binding")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true"
                                 and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY):
        parser.error("actual complete head research only in this public repository GitHub Actions")
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),"github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "github_sha":os.environ.get("GITHUB_SHA"),"source_hashes":{},
        "scope":"one true weight: nine missing normal families, five archived families, complete R163 translation presentation",
        "limits":{"seconds":args.max_seconds,"memory_polling_mib":args.memory_mib,
            "max_main_bytes":args.max_main_bytes,"max_full_report_bytes":args.max_full_report_bytes,
            "max_original_export_bytes":args.max_export_bytes,"checkpoint_every_new_contractions":args.checkpoint_every},
        "head_generation_complete":False,"old_forcing_or_W_compiled":False,
        "old_response_basis_rebuilt_or_reevaluated":False,"profile_values_or_geometry_evaluated":False,
        "function_space_rank_computed":False,"positive_character_decided":False,
        "all_even_weights_computed":False,"period_or_ruling_paid":False,"task_complete":False}
    ctx={};code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["phase"]="small_artificial_new_head_interfaces"
            report["toy"]=toy_only();report["completion"]="toy_passed"
        else:
            study(args,report,ctx)
    except formal.CompilationBudgetExceeded as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
    finally:
        if not args.toy_only:
            try:
                write_originals(args,report,ctx)
            except Exception as error:
                report["checkpoint_storage_error"]={"type":type(error).__name__,"message":str(error)}
                if code==0:
                    report["completion"]="resource_limit";report["head_generation_complete"]=False;code=2
        report["elapsed_seconds"]=time.monotonic()-started
        report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    written=write_reports(args,report)
    print(json.dumps(written),flush=True)
    return code


if __name__=="__main__":
    raise SystemExit(main())
