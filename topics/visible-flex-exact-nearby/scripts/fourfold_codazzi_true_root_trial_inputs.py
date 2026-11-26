"""TC complete original-input admission and exact carrier materialization.

No IO or numerical work at import.  This module validates entire old result
objects and 40 complete native parts.  AST extraction admits only named
pure arithmetic/readers; no old producer or numerical target is callable.
"""
from fractions import Fraction
from bisect import bisect_right
from pathlib import Path
import ast, gzip, hashlib, io, json, math

TOPIC = "topics/visible-flex-exact-nearby/"
CENTRE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
ALPHA = Fraction(6890507429876859,9007199254740992)
DELTA = Fraction(9368259853002,100000000000000000000000)
ROOT = (Fraction(1191984371497,5000000000000),
        Fraction(2383968743003,10000000000000))
POSITIVE_CUT = Fraction(1192029371497,5000000000000)
NEGATIVE_CUT = ROOT[1]-Fraction(1,200)
OUTER = Fraction(25,8)
CONTROL = (Fraction(1,20),Fraction(9,50))
PRIOR_SHA = {
    "RW_manifest":"be8da3e31973d9c3725a4dcb4834287a1add06121e3853ea4308b08b656fac05",
    "RW_actual":"b0faf218c059b6f7ee113a5f127a7518e78d2c87dc70b4dcf650ce97594c7fa4",
    "RW_execution":"3cfc1cbc9f8b1c5fe450c779146042c6b7f4bd4f42ca48606c4c9309e94a0b00",
    "NW_manifest":"b697e8665801a6e4d5120ca312d72a339cc28a2516d6dabd255f56ee79690f2d",
    "old_body_manifest":"c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784",
    "old_centre_repair":"6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc",
    "old_direction_repair":"87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88",
    "base_index":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
    "direction_index":"ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6",
}
ROW_PAYLOAD = "06fdb69708f63d27587fb91bb0760b50e23fa8d1719ed8b8903d8be6e922abe6"
ROW_SOURCE = "1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07"


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
            ensure_ascii=False,allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def pure_definitions(raw,names,namespace,label):
    """Exact AST definitions only; all import/top-level execution is excluded."""
    tree = ast.parse(raw.decode("utf-8"),filename=label)
    nodes = [node for node in tree.body
             if isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.name in names]
    require(len(nodes) == len(names) and {node.name for node in nodes} == set(names),
            "every unique declared pure definition exists: "+label)
    module = ast.Module(body=nodes,type_ignores=[])
    exec(compile(ast.fix_missing_locations(module),label,"exec"),namespace)
    return {"source_sha256":sha(raw),"names":list(names),
            "complete_AST_subset_sha256":sha(ast.dump(module,include_attributes=False).encode())}


def directed_backend(np,flint,box_source,fft_source):
    namespace = {"np":np,"arb":flint.arb,"acb":flint.acb,"ctx":flint.ctx,
                 "up":lambda x:np.nextafter(x,np.inf),
                 "down":lambda x:np.nextafter(x,-np.inf)}
    receipts = [
        pure_definitions(box_source,("Box","stack"),namespace,"old_complete_Box"),
        pure_definitions(fft_source,
            ("arb_box","scalar_arb","reduce_box","square_box","CBox",
             "zeros","cstack","DirectedFFT"),namespace,"old_complete_directed_FFT")]
    return namespace,receipts


def candidate_reader(np,source):
    def forbidden(*args,**kwargs):
        raise ValueError("only the complete original sharded JSON indices are admitted")
    namespace = {"np":np,"gzip":gzip,"io":io,"json":json,"Path":Path,
                 "sha256":hashlib.sha256,"load_single":forbidden}
    receipt = pure_definitions(source,("digest","load_candidate"),namespace,"old_candidate_reader")
    return namespace["load_candidate"],receipt


def repair_iterator(source):
    namespace = {"Fraction":Fraction}
    receipt = pure_definitions(source,("fraction","iter_repair"),namespace,"old_exact_repair_iterator")
    return namespace["iter_repair"],receipt


def admit_prior_bundles(raw_by_path,role_specs,rw_owner,nw_owner):
    """All historical numerical statements remain original whole objects."""
    for role,want in PRIOR_SHA.items():
        spec = role_specs[role]
        require(sha(raw_by_path[spec["path"]]) == want == spec["sha256"],
                "entire immutable original input: "+role)
    def subset(label,owner):
        manifest = parse(raw_by_path[role_specs[label+"_manifest"]["path"]])
        specs = {item["role"]:item for item in
                 manifest["files"]+manifest.get("historical_inputs",[])}
        require(len(specs) == len(manifest["files"])+len(manifest.get("historical_inputs",[])),
                "no duplicate inherited original roles")
        contents = {role:raw_by_path[item["path"]] for role,item in specs.items()}
        prior = owner.admit_complete_inputs(contents,specs)
        return manifest,specs,contents,prior
    rwm,rws,rwc,rw = subset("RW",rw_owner)
    nwm,nws,nwc,nw = subset("NW",nw_owner)
    actual = parse(raw_by_path[role_specs["RW_actual"]["path"]])
    execution = parse(raw_by_path[role_specs["RW_execution"]["path"]])
    targets = ["row_%03d"%j for j in range(1,97)]
    require(actual["identity"]["kind"] == "R149_complete_reflected_finite_waist_rows_v1"
            and actual["complete"] is actual["proved"] is True
            and actual["actual_returncode"] == 0 and actual["failure"] is None
            and actual["completed_targets"] == targets
            and actual["saved_record_count"] == actual["private_complete_row_count"] == 96
            and actual["parameters"] == rwm["parameters"]
            and actual["identity"]["manifest_sha256"] == PRIOR_SHA["RW_manifest"]
            and actual["identity"]["source_sha256"] == rws["science"]["sha256"]
            and actual["identity"]["row_math_sha256"] == rws["row_math"]["sha256"],
            "entire successful original RW96 result and same exact definitions")
    require(execution["complete"] is True and execution["actual_child_returncode"] == 0
            and execution["original_scientific_complete"] is True
            and execution["original_scientific_failure"] is None
            and execution["run_id"] == "45787309600" and execution["run_attempt"] == "1"
            and execution["manifest_sha256"] == PRIOR_SHA["RW_manifest"]
            and execution["scientific_files"] == [{
                "path":role_specs["RW_actual"]["path"],
                "bytes":role_specs["RW_actual"]["bytes"],"sha256":PRIOR_SHA["RW_actual"]}]
            and execution["old_completed_targets_recomputed"] == 0,
            "whole actual RW execution binds the exact complete scientific bytes")
    require(actual["reference_identity"] == rw["family"] == nw["family"]
            and rw["family"]["continuous_centre_definition_sha256"] == CENTRE
            and rw["family"]["continuous_response_definition_sha256"] == DIRECTION
            and Fraction(rw["family"]["exact_alpha"]) == ALPHA
            and Fraction(nwm["parameters"]["selected_parameter_absolute_upper"]) == DELTA
            and list(map(Fraction,nwm["parameters"]["exact_root_interval"])) == list(ROOT)
            and Fraction(nwm["parameters"]["exact_strict_interval"][1]) == NEGATIVE_CUT
            and nwm["parameters"]["fixed_intrinsic_parameter"] == "eta_0",
            "one same selected member, true root and complete physical means")
    require(nw["difference"]["original_rows_canonical_payload_sha256"] == ROW_PAYLOAD
            and nw["difference"]["complete_original_rows_verified"] == 7721,
            "the already completed exact original whole-row payload")
    for name in targets:
        record = actual["new_records"][name]
        require(record["mode"] == int(name[-3:])
                and record["carrier"]["complete_real_count"] == 1025
                and set(record) == {"mode","carrier","mean","trial_l2",
                                    "compound_error","incoming_error","physical_error"},
                "each of all96 whole old row records")
    repair = parse(raw_by_path[role_specs["old_centre_repair"]["path"]])
    direction = parse(raw_by_path[role_specs["old_direction_repair"]["path"]])
    require(repair["complete"] is True
            and repair["derived_definition_sha256"] == CENTRE
            and repair["candidate_sha256"] == PRIOR_SHA["base_index"]
            and repair["exact_interface_count"] == 6143
            and all(g["passed"] is True for g in repair["gates"])
            and direction["complete"] is True
            and direction["derived_direction_definition_sha256"] == DIRECTION
            and direction["background_definition_sha256"] == CENTRE
            and direction["original_trial_sha256"] == PRIOR_SHA["direction_index"]
            and direction["exact_interface_count"] == 6143
            and direction["exact_component_interface_count"] == 6143*193
            and all(g["passed"] is True for g in direction["gates"]),
            "whole original exact repair results, both means and complete interfaces")
    return {"RW":rw,"NW":nw,"RW_actual":actual,"RW_manifest":rwm,
            "RW_specs":rws,"RW_contents":rwc,"NW_manifest":nwm,"NW_specs":nws,
            "centre_repair":repair,"direction_repair":direction,
            "old_body_manifest":parse(raw_by_path[role_specs["old_body_manifest"]["path"]])}


def admit_all_rows(part_paths,prior):
    old = prior["old_body_manifest"]
    response = prior["NW"]["difference"]
    expected = {tuple(item["indices"]):item["sha256"]
                for item in response["original_part_receipts"]}
    # Some old D receipts include a natural path; only the original interval
    # and complete compressed bytes identify the immutable scientific input.
    require(len(expected) == 40,"all40 completed original natural parts")
    paths = {}
    for path in part_paths:
        raw = Path(path).read_bytes()
        matches = [key for key,want in expected.items() if sha(raw) == want]
        require(len(matches) == 1 and matches[0] not in paths,
                "complete unique original natural-part bytes")
        paths[matches[0]] = raw
    require(set(paths) == set(expected),"no original natural part omitted")
    rows,receipts = [],[]
    cursor,radial = 0,Fraction(0)
    payload = hashlib.sha256()
    required = ["a"]+[name+(str(k) if k else "") for name in ("beta","K","gamma","s")
                      for k in range(4)]
    for key,raw in sorted(paths.items()):
        part = parse(raw)
        require(part["kind"] == old["residual_kind"]
                and part["identity"] == old["row_identity"]
                and part["source_sha256"] == ROW_SOURCE
                and part["selected_cells_complete"] is True
                and part["failure"] is None
                and tuple(part["selected_indices"]) == key and key[0] == cursor
                and len(part["rows"]) == key[1]-key[0],
                "complete original local part identity and exact index cover")
        for row in part["rows"]:
            left,right = map(Fraction,row["interval"])
            germ = row["actual_scalar_germ"]
            require(row["common_row"] == cursor and left == radial and left < right
                    and Fraction(germ[0]) <= left < right <= Fraction(germ[1])
                    and all(name in row[group] for group in
                        ("intrinsic_midpoint_jets","intrinsic_whole_third_jets")
                        for name in required),
                    "complete old midpoint/whole-third schema and real exact radial cover")
            payload.update(canonical(row))
            rows.append({name:row[name] for name in (
                "common_row","interval","pieces","actual_scalar_germ",
                "intrinsic_midpoint_jets","intrinsic_whole_third_jets")})
            cursor,radial = cursor+1,right
        receipts.append({"indices":list(key),"bytes":len(raw),"sha256":sha(raw)})
    require(cursor == 7721 and radial == OUTER and payload.hexdigest() == ROW_PAYLOAD,
            "exact all7721 original full-row payload; no old enclosure narrowed")
    return rows,receipts


def materialize_repairs(context,base,direction,iterator,prior,allocate,progress=None):
    """Only necessary same-definition signed offsets; no old norm target."""
    c = context
    require(base["piece_coefficients"].shape == (4,6144,65)
            and direction["piece_coefficients"].shape == (4,6144,193)
            and c.np.array_equal(base["radial_nodes"],direction["radial_nodes"]),
            "both complete original cubic arrays and every same exact endpoint")
    out,receipts = {},{}
    for name,saved,alpha,expected in (
        ("base",base,ALPHA,prior["centre_repair"]["definition"]["offset_sequence_sha256"]),
        ("direction",direction,Fraction(1),
         prior["direction_repair"]["derived_direction_definition"]["complete_offset_sequence_sha256"])):
        dimension = saved["piece_coefficients"].shape[2]
        lower = allocate(name+"_offset_lower",(6144,dimension))
        upper = allocate(name+"_offset_upper",(6144,dimension))
        midpoint = allocate(name+"_offset_midpoint",(6144,dimension))
        digest = hashlib.sha256()
        count = 0
        for piece,offset,jump in iterator(saved,alpha):
            digest.update(canonical({"piece":piece,"physical_offset":list(map(str,offset))}))
            for k,value in enumerate(offset):
                box = c.arb_box(c.exact(value))
                lower[piece,k],upper[piece,k] = float(box.lo),float(box.hi)
                midpoint[piece,k] = float(value)
            count += 1
            if progress is not None and (piece % 256 == 0 or piece == 6143):
                progress("same_exact_signed_"+name+"_offsets",{"pieces":piece+1,"total":6144})
        require(count == 6144 and digest.hexdigest() == expected,
                "same full original signed repair chain, never a coefficient sup")
        out[name] = {"lower":lower,"upper":upper,"midpoint":midpoint}
        receipts[name] = {"complete_pieces":count,"coordinates":dimension,
                         "complete_offset_sequence_sha256":digest.hexdigest(),
                         "old_repair_norm_targets_recomputed":0}
    return out,receipts


def complete_plan(rows,base_nodes):
    """Exactly reconstructible trial grid and conservative true-root cover."""
    cuts = {Fraction(x) for row in rows for x in row["interval"]}
    cuts.update(Fraction.from_float(float(x)) for x in base_nodes)
    cuts.update((Fraction(0),OUTER,Fraction(3),*CONTROL,POSITIVE_CUT,NEGATIVE_CUT))
    fixed = sorted(x for x in cuts if x < ROOT[0] or x > ROOT[1])
    require(fixed[0] == 0 and fixed[-1] == OUTER,"complete fixed mesh endpoints")
    root_index = sum(x < ROOT[0] for x in fixed)
    labels = [str(x) for x in fixed[:root_index]]+["true_root"]+[str(x) for x in fixed[root_index:]]
    proposal_root = Fraction.from_float(float((ROOT[0]+ROOT[1])/2))
    require(ROOT[0] <= proposal_root <= ROOT[1],"one explicit dyadic proposal root")
    proposal_nodes = [float(proposal_root if x == "true_root" else Fraction(x)) for x in labels]
    certificate = []
    row_intervals = [tuple(map(Fraction,row["interval"])) for row in rows]
    row_rights = [value[1] for value in row_intervals]
    for i,(left,right) in enumerate(zip(labels,labels[1:])):
        a = ROOT[0] if left == "true_root" else Fraction(left)
        b = ROOT[1] if right == "true_root" else Fraction(right)
        side = "negative" if i < root_index else "positive"
        first_row = bisect_right(row_rights,a)
        for j in range(first_row,len(rows)):
            l,r = row_intervals[j]
            if l >= b:
                break
            l,r = max(l,a),min(r,b)
            if l >= r:
                continue
            internal = sorted({l,r,*[x for x in (Fraction(3),*CONTROL,POSITIVE_CUT,NEGATIVE_CUT)
                                     if l < x < r]})
            for x,y in zip(internal,internal[1:]):
                names = (["negative_strict"] if y <= NEGATIVE_CUT else ["negative_root"]) if side == "negative" else (
                         ["positive_low","positive_high_collar"] if y <= POSITIVE_CUT else
                         ["positive_low","positive_high_body"])
                require((side != "negative" or x >= NEGATIVE_CUT or y <= NEGATIVE_CUT)
                        and (side != "positive" or x >= POSITIVE_CUT or y <= POSITIVE_CUT),
                        "complete original source windows are explicitly split")
                certificate.append({"trial_piece":i,"original_row":j,
                    "interval":[str(x),str(y)],"side":side,"norms":names})
    definition = {"kind":"TC_true_root_septic_dyadic_endpoint_definition_v1",
        "node_labels":labels,"proposal_root_dyadic":str(proposal_root),
        "proposal_root_hex":float(proposal_root).hex(),
        "root_index":root_index,"cutoff":"TC.10 exact L0(8(r-3)) after r=3",
        "root_even96_exact":"identity","same_entire_root_value_on_both_sides":True,
        "physical_frequency_factor":4,"real_normalization":"sqrt(2) sin/cos; mean one"}
    return definition,proposal_nodes,certificate


def true_interval(context,definition,index):
    labels = definition["node_labels"]
    c = context
    def endpoint(label):
        return (c.exact(ROOT[0]).union(c.exact(ROOT[1])) if label == "true_root"
                else c.exact(Fraction(label)))
    left,right = endpoint(labels[index]),endpoint(labels[index+1])
    require((right-left).lower() > 0,"entire true trial interval has positive length")
    return left,right,right-left


def selected_background(context,base,direction,offsets,piece,left,right,mean_scalar,math_module):
    c = context
    left,right = Fraction(left),Fraction(right)
    knot = Fraction.from_float(float(base["radial_nodes"][piece]))
    next_knot = Fraction.from_float(float(base["radial_nodes"][piece+1]))
    require(knot <= left < right <= next_knot,"one original complete cubic restriction")
    centre,half = (left+right)/2,(right-left)/2
    terms = {}
    for name,saved,alpha in (("base",base,ALPHA),("direction",direction,Fraction(1))):
        raw = saved["piece_coefficients"][:,piece,:][::-1]
        cs = [c.Box(row.reshape(-1,1))*c.box(alpha) for row in raw]
        offset = offsets[name]
        cs[0] = cs[0]+c.Box(offset["lower"][piece,:,None],offset["upper"][piece,:,None])
        cs = c.affine_polynomial(cs,centre-knot,half)
        if name == "base":
            expanded = []
            for value in cs:
                lo,hi = c.np.zeros((193,1)),c.np.zeros((193,1))
                for start,stop,source in ((0,32,slice(0,32)),(96,97,slice(32,33)),
                                          (97,129,slice(33,65))):
                    lo[start:stop],hi[start:stop] = value.lo[source],value.hi[source]
                expanded.append(c.Box(lo,hi))
            cs = expanded
        terms[name] = cs
    d = c.box(c.exact(-DELTA).union(c.exact(DELTA)))
    coefficients = [a+b*d for a,b in zip(terms["base"],terms["direction"])]
    return math_module.unnormalized_background(c,coefficients,mean_scalar)
