"""Read-only WHV admission. No flint and no original producer import."""
from __future__ import annotations
import ast, gzip, hashlib, json, os, re
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby/"
REPOSITORY="Rogerhu12/math-research-public"
MANIFEST_KIND="complete_zero_volterra_positive_head_mesh_current_inputs_v1"
PROBLEM_ID="WHV_zero_volterra_positive_head_mesh_v1"
PARAMETERS={"bits":320,"radial_mesh_N":4096,"resource_cap_N":4096,
 "head_dimension":193,"first_high_index":97,"physical_high_minimum":388,
 "required_N_diagnostic":True}
INVENTORY_SHA="80f9f606f14f8cea41f3a4f18a5d6b9c7d59274ea8016199b1cc086cf58b59ce"
PROOF_SHA="e993f0685dad2bd61740cf1fc02ff20d8cd5c02f43970d2eee05fdba885d5dd2"
SPEC_KEYS={"role","path","bytes","sha256","git_blob_sha"}
CHECKS=[
 "all_current_UTF8_files_and_the_fixed_contracts_verified",
 "two_new_and_three_original_sources_AST_only_verified",
 "all_thirteen_historical_receipts_and_original_native_bytes_verified",
 "complete_original_summary_and_native_projection_identical",
 "both_complete_4650_row_covers_and_3594_interfaces_verified",
 "same_real_family_and_all_three_original_successes_verified",
 "all_nine_original_literals_preserved_verbatim"]
ROW_BOUNDS=("p_row_lower","g_row_lower","W_lower","K_over_W_upper","E",
 "base_M32_E","delta_drift_E","delta_local_E","delta_primitive_E",
 "delta_primitive_Gamma","gap","frame","reconstruction",
 "low_to_high_source","high_to_low_raw","head_generator")
ROW_KERNELS=("complete_forward_kernel","complete_backward_kernel",
 "complete_forward_ordinary_source_square","complete_backward_ordinary_source_square")

def require(ok,message):
 if not ok: raise ValueError(message)

def digest(raw):
 return hashlib.sha256(raw).hexdigest()

def canonical(value):
 return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                    allow_nan=False)+"\n").encode("utf-8")

def data(raw):
 return json.loads(raw,parse_float=Decimal,
                   parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))

def at(value,path):
 for key in path: value=value[key]
 return value

def record(value):
 require(isinstance(value,dict) and set(value)=={"ball","lower","upper"},
         "original complete record shape")
 require(all(isinstance(x,str) and x.isascii() and 0<len(x)<=128 and not re.search(r"nan|inf",x,re.I)
             and all(len(e)<=6 for e in re.findall(r"[eE][+-]?(\d+)",x))
             for x in value.values()),"original finite record text")
 return value

def read_spec(repo,spec):
 require(isinstance(spec,dict) and set(spec)==SPEC_KEYS,"complete current spec")
 require(isinstance(spec["role"],str) and spec["role"],"current role")
 require(isinstance(spec["path"],str) and spec["path"].startswith(TOPIC),
         "current path scope")
 path=(repo/spec["path"]).resolve()
 require(path.is_relative_to(repo) and path.is_file(),"current file containment")
 raw=path.read_bytes()
 require(type(spec["bytes"]) is int and 0<len(raw)<100000
         and len(raw)==spec["bytes"],"current byte count")
 require(digest(raw)==spec["sha256"],"current SHA256")
 blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
 require(blob==spec["git_blob_sha"],"current Git blob")
 return raw.decode("utf-8")

def gates(doc,key,count):
 value=doc[key]
 require(isinstance(value,list) and len(value)==count
         and all(set(x)=={"name","passed"} and isinstance(x["name"],str)
                 and x["passed"] is True for x in value),"original complete gates")

def children(doc,count):
 require(doc["complete"] is True and len(doc["children"])==count
         and all(type(x["actual_returncode"]) is int and x["actual_returncode"]==0
                 for x in doc["children"]),"original child success")

def root_literal(text):
 tree=ast.parse(text)
 functions=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=="main"]
 require(len(functions)==1,"original main AST")
 assignments=[n for n in ast.walk(functions[0]) if isinstance(n,ast.Assign)
              and any(isinstance(t,ast.Name) and t.id=="expected" for t in n.targets)]
 require(len(assignments)==1 and isinstance(assignments[0].value,ast.List),
         "original root literal AST")
 values=[]
 for node in assignments[0].value.elts:
  require(isinstance(node,ast.Call) and isinstance(node.func,ast.Name)
          and node.func.id=="q" and len(node.args)==2 and not node.keywords
          and all(isinstance(x,ast.Constant) and type(x.value) is int
                  for x in node.args),"original rational call")
  values.append(str(Fraction(node.args[0].value,node.args[1].value)))
 return values

def admit(repo,manifest_path,manifest_sha,native_path,receipts_path):
 require(os.environ.get("GITHUB_ACTIONS")=="true"
         and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,"public Actions only")
 repo=Path(repo).resolve()
 raw=Path(manifest_path).read_bytes()
 require(digest(raw)==manifest_sha,"manifest SHA256")
 manifest=data(raw)
 require(manifest["kind"]==MANIFEST_KIND and manifest["problem_id"]==PROBLEM_ID
         and manifest["repository"]==REPOSITORY
         and manifest["parameters"]==PARAMETERS,"fixed WHV manifest")
 specs=manifest["files"]
 require(isinstance(specs,list) and len(specs)==manifest["expected_current_input_count"]
         and len({x["role"] for x in specs})==len(specs)
         and len({x["path"] for x in specs})==len(specs),"unique complete files")
 by_role={x["role"]:x for x in specs}
 texts={spec["role"]:read_spec(repo,spec) for spec in specs}
 for key,sha in (("inventory",INVENTORY_SHA),("mathematical_contract",PROOF_SHA)):
  spec=manifest[key]
  require(by_role[spec["role"]]==spec and spec["sha256"]==sha,"fixed proof/inventory")
 inventory=data(texts[manifest["inventory"]["role"]])
 require(manifest["core_current_files"]==inventory["complete_existing_text_inputs"]
         and len(manifest["core_current_files"])==9
         and manifest["historical_inputs"]==inventory["historical_parts"]
         and len(manifest["historical_inputs"])==13,"original closed input inventory")
 for spec in manifest["core_current_files"]:
  require(by_role[spec["role"]]==spec,"original current identity")
 modules=manifest["scientific_modules"]
 require([x["role"] for x in modules]==["science","readonly_admission"]
         and all(by_role[x["role"]]==x for x in modules),"two new modules")
 original_sources=("negative_one_source","collar_source","body_source")
 for role in original_sources+tuple(x["role"] for x in modules):
  ast.parse(texts[role])
 docs={role:data(texts[role]) for role in
       ("negative_one_summary","negative_one_process","collar_process",
        "body_process","body_summary","body_parts_manifest")}
 receipts_raw=Path(receipts_path).read_bytes()
 receipts=data(receipts_raw)
 require(set(receipts)=={"kind","historical_inputs","native","old_producers_executed"}
         and receipts["kind"]=="complete_readonly_restored_positive_body_native_v1"
         and type(receipts["old_producers_executed"]) is int
         and receipts["old_producers_executed"]==0,"read-only restoration receipt")
 extra={"git_tree_blob_and_size_verified","compressed_sha256_verified",
        "chunk_sha256_verified"}
 require(len(receipts["historical_inputs"])==13,"thirteen restored inputs")
 for expected,actual in zip(inventory["historical_parts"],receipts["historical_inputs"]):
  require(set(actual)==set(expected)|extra
          and {k:actual[k] for k in expected}==expected
          and all(actual[k] is True for k in extra),"complete historical tuple")
 restoration=inventory["native_restoration"]
 expected_native={"bytes":restoration["complete_container_bytes"],
  "sha256":restoration["complete_container_sha256"],
  "complete_concatenation_verified":True}
 require(receipts["native"]==expected_native,"complete concatenation receipt")
 compressed=Path(native_path).read_bytes()
 require(len(compressed)==expected_native["bytes"]
         and digest(compressed)==expected_native["sha256"],"original native container")
 native=data(gzip.decompress(compressed))
 body=docs["body_summary"]; bp=docs["body_process"]
 neg=docs["negative_one_summary"]; np=docs["negative_one_process"]
 collar=docs["collar_process"]
 require(native["kind"]==restoration["native_kind"] and native["complete"] is True
         and native["failure"] is None,"original native success")
 gates(native,"gates",11)
 require(native["gates"]==restoration["complete_original_gates"],"all eleven old gates")
 require(native["source_sha256"]==by_role["body_source"]["sha256"],"body source pin")
 projection={k:v for k,v in native.items() if k not in ("inflated_rows","orders")}
 projection["orders"]=[{k:v for k,v in order.items() if k!="complete_rows"}
                       for order in native["orders"]]
 require(projection=={k:v for k,v in body.items() if k!="native_sha256"},
         "entire original summary projection")
 require(body["native_sha256"]==expected_native["sha256"]
         and native["actual_new_scalar_rows"]==4608
         and native["complete_original_rows"]==4650
         and native["complete_original_raw_response_envelope_rows"]==7721
         and native["original_right_interfaces_preserved"]==3594,"complete old counts")
 left=Fraction(inventory["scope"]["body_cut"]); right=Fraction(25,8)
 inflated=native["inflated_rows"]; orders=native["orders"]
 require(len(inflated)==4650 and len(orders)==2,"full native arrays")
 edge=left; interfaces=0
 for index,row in enumerate(inflated):
  require(len(row["interval"])==2 and all(isinstance(x,str) and x.isascii() and len(x)<=128
          for x in row["interval"]),"original interval text width")
  lo,hi=map(Fraction,row["interval"])
  require(type(row["index"]) is int and row["index"]==index and lo==edge and lo<hi,
          "original inflated row cover")
  edge=hi
  interfaces+=row["original_right_interface"] is not None
 require(edge==right and interfaces==3594,"full inflated interval and interfaces")
 for order_index,order in enumerate(orders):
  require(order["homogeneous_angular_order"]==order_index and order["complete"] is True
          and order["failure"] is None and order["actual_scalar_comparison_rows"]==4650
          and len(order["complete_rows"])==4650,"both original complete orders")
  require(order["canonical_exterior_feedback_closed"] is (order_index==0)
          and order["independent_right_high_port"] is (order_index==1),
          "original independent second-order port")
  for index,row in enumerate(order["complete_rows"]):
   require(set(row)=={"original_row","interval","bounds",*ROW_KERNELS}
           and type(row["original_row"]) is int and row["original_row"]==index
           and row["interval"]==inflated[index]["interval"]
           and set(row["bounds"])==set(ROW_BOUNDS),"original complete kernel row")
   for value in row["bounds"].values(): record(value)
   for key in ROW_KERNELS: record(row[key])
 children(bp,2); children(np,1)
 require(collar["complete"] is True and collar["mathematical_complete"] is True
         and type(collar["actual_returncode"]) is int and collar["actual_returncode"]==0,
         "collar original success")
 gates(collar,"mathematical_gates",19); gates(neg,"gates",18)
 require(neg["complete"] is True and neg["failure"] is None
         and neg["source_sha256"]==by_role["negative_one_source"]["sha256"]
         and collar["mathematical_source_sha256"]==by_role["collar_source"]["sha256"],
         "original scientific sources")
 require(bp["run_id"]=="43615531666" and np["run_id"]=="43627228225"
         and collar["run_id"]=="43606747196","three actual runs")
 require(bp["complete_native_sha256"]==expected_native["sha256"]
         and neg["original_complete_body_native_sha256"]==expected_native["sha256"]
         and neg["original_collar_native_sha256"]==collar["native_sha256"]
         and np["complete_native_sha256"]==neg["native_sha256"]
         and np["actual_scientific_gates"]==18
         and np["actual_complete_source_columns"]==7
         and np["actual_complete_output_rows"]==8,"old receipt/native chain")
 for key in ("original_candidate_sha256","derived_definition_sha256",
             "explicit_direction_definition_sha256","exact_real_delta_radius"):
  require(neg[key]==native[key],"same real family")
 require(neg["exact_real_delta_radius"]=="1/100000000"
         and neg["fixed_body_cut"]==str(left)
         and neg["entire_positive_interval"][1]=="25/8"
         and native["exact_radial_interval"]==[str(left),"25/8"],"same positive interval")
 require(neg["original_complete_outer_native_sha256"]==
         native["actual_new_complete_outer_native_sha256"]==
         bp["actual_full_delta_outer_native_sha256"],"same actual outer reference")
 for role,key in (("collar_process","collar-process"),("body_process","body-process"),
                  ("body_summary","body-summary")):
  require(neg["input_sha256"][key]==by_role[role]["sha256"],"old admitted input bytes")
 require(np["actual_original_small_input_sha256"]==neg["input_sha256"],
         "complete original small-input identity")
 require(len(neg["input_order"])==7 and len(neg["response_rows"])==8
         and all(len(row)==7 for row in neg["response_rows"].values()),
         "complete seven by eight graph")
 for row in neg["response_rows"].values():
  for value in row: record(value)
 require(neg["independent_even_mean_and_all_head_and_affine_source_ports_retained"] is True
         and neg["high_to_head_uses_complete_original97_to288_shell_and1153_factor"] is True
         and neg["given_complete_head_positive_high_inverse_and_root_graph_proved"] is True
         and neg["full_low_high_Schur_inverse_proved"] is False
         and neg["complete_infinite_BVP_inverse_proved"] is False
         and native["complete_positive_finite_head_inverse_proved"] is False,
         "retained original scope")
 roots=root_literal(texts["collar_source"]); literals={}
 for item in inventory["readonly_literal_inputs"]:
  value=roots if item["name"]=="rstar_interval" else at(docs[item["role"]],item["path"])
  expected=item.get("original_record",item.get("original_value"))
  require(value==expected,"original literal "+item["name"])
  literals[item["name"]]=value
 require(len(literals)==9,"nine complete old literals")
 old_scope={key:neg[key] for key in ("physical_parameter","nu_family",
  "entire_positive_interval","fixed_body_cut","ordinary_source_contract",
  "raw_state_contract","same_genuine_forward_and_backward_Riccati_reference",
  "independent_even_mean_and_all_head_and_affine_source_ports_retained",
  "given_complete_head_positive_high_inverse_and_root_graph_proved",
  "full_low_high_Schur_inverse_proved","complete_infinite_BVP_inverse_proved")}
 summary={"checks":[{"name":name,"passed":True} for name in CHECKS],
  "old_runs":["43606747196/1","43615531666/1","43627228225/1"],
  "old_gate_counts":[19,11,18],"new_source_AST_count":2,"old_source_AST_count":3,
  "old_source_import_count":0,"old_targets_recomputed":0,
  "native_bytes":expected_native["bytes"],"native_sha256":expected_native["sha256"],
  "per_order_complete_rows":[4650,4650],"inflated_rows":4650,"interfaces":3594,
  "original_progress_counter":4608,"original_parts_manifest_row_counter":0,
  "current_file_count":len(specs),"historical_input_count":13,
  "old_numeric_text_width_cap":128,"old_exponent_digit_cap":6,
  "restoration_receipts_bytes":len(receipts_raw),
  "restoration_receipts_sha256":digest(receipts_raw)}
 return {"manifest":manifest,"inventory":inventory,"rows":orders[0]["complete_rows"],
  "literals":literals,"old_scope":old_scope,"admission":summary,
  "current_receipts":specs,"scientific_modules":modules}
