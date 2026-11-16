"""Typed readonly WPTV admission; no flint, numpy, or original producer import."""
from __future__ import annotations
import ast, gzip, hashlib, io, json, os, re, struct, zipfile
from bisect import bisect_right
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby/"
REPOSITORY="Rogerhu12/math-research-public"
MANIFEST_KIND="complete_frozen_cross_block_remaining_body_current_inputs_v1"
PROBLEM_ID="WPTV_remaining_body_after_43854566735_v1"
PARAMETERS={"bits":320,"parent_band_subcells":8,"maximum_doubling_bands":20,
 "maximum_parent_cells":161,"uniform_refinements":[1,2],"maximum_refined_cells":322,
 "reference_q_floor":"1/8","reference_q_binary_places":20,
 "head_dimension":193,"first_high_index":97,"physical_high_minimum":388,
 "reference_centre_degree":32,"actual_delta_degree":96,
 "new_array_artifacts":False,"old_targets_recomputed":0}
INVENTORY_SHA="f7dd2ed019b30c076aa70ad1536601813095ef59bb504049d976eb0cd93b1547"
PROOF_SHA="dda500b8f5e2d02a39fbef4efcc5c2ad10dac93eef194f6e8d5b9b5a816cd0e9"
REFINEMENT_SHA="62adc53eedc1ea339e02f6e2a8fa654e38c92fe04784343557e23c84ddd696c2"
CHECKS=[
 "all_current_UTF8_files_and_three_fixed_contracts_verified",
 "two_new_and_seven_original_sources_AST_only_verified",
 "all_nineteen_historical_receipts_and_original_native_bytes_verified",
 "complete_original_summary_and_native_projection_identical",
 "both_complete_4650_row_covers_and_3594_interfaces_verified",
 "same_real_family_and_all_original_successes_verified",
 "all_nine_original_literals_and_completed_WHVA_retained",
 "all_five_original_cubic_parts_and_full_shape_verified",
 "original_repair_whole_document_and_all_65_suprema_verified",
 "actual_raw_identity_transmissions_and_full_affine_ports_retained"]

SPEC_KEYS={"role","path","bytes","sha256","git_blob_sha"}
ROW_BOUNDS=("p_row_lower","g_row_lower","W_lower","K_over_W_upper","E",
 "base_M32_E","delta_drift_E","delta_local_E","delta_primitive_E",
 "delta_primitive_Gamma","gap","frame","reconstruction",
 "low_to_high_source","high_to_low_raw","head_generator")
ROW_KERNELS=("complete_forward_kernel","complete_backward_kernel",
 "complete_forward_ordinary_source_square","complete_backward_ordinary_source_square")

INTRINSIC_KEYS=("a","beta","Ebar","R","K","gamma","Cref")
COMPLETE_COEFFICIENT_KEYS=(
 "mean_v","radial_speed","U_A0","V_A0","U_phi_A0","V_phi_A0",
 "V_nonmean_A0","drift_A0","drift_phi_A0","full_S_mean",
 "local_a_A0","local_e_A0","local_b_A0","local_a_sup","local_e_sup",
 "local_b_sup","primitive_raw_L2","mean_rank_raw_L2","mean_own_rate",
 "mean_nonmean_feedback_L2","real_physical_inverse_gap")
DELTA_FEE_KEYS=("delta_u_squared","delta_v_squared","delta_uv","delta_S",
 "local_a","local_e","local_b","drift","drift_phi","mean_own_rate")
INFLATED_GROUP_KEYS={
 "original_intrinsic_enclosure":INTRINSIC_KEYS,
 "original_complete_repaired_bounds":COMPLETE_COEFFICIENT_KEYS,
 "complete_delta_bounds":COMPLETE_COEFFICIENT_KEYS,
 "complete_delta_fees":DELTA_FEE_KEYS}

CONTINUATION_CONTRACT={"kind":"complete_WPTV_preserved_collar_remaining_body_contract_v1","prior_files":[{"role":"prior_science","path":"topics/visible-flex-exact-nearby/notes/frozen_cross_block_value_tail_ci/run-43854566735-1/actual-scientific-conclusion.json","git_blob_sha":"e5721a0ecea7c3131401a8caa94839ad10e2e315","bytes":15309,"sha256":"b8812b6b940b17532c7643555d3393da71c2190606082862ccf651fbff762274"},{"role":"prior_execution","path":"topics/visible-flex-exact-nearby/notes/frozen_cross_block_value_tail_ci/run-43854566735-1/execution.json","git_blob_sha":"fe4c3e274701d9237736809e7dd12b801ce8c79c","bytes":31256,"sha256":"e7246476bc02fe196ec10186783bcda8892621ec1c105d4b99dc612647cd3eca"},{"role":"prior_manifest","git_blob_sha":"c1228b9d5984a0a2d11de37b6dcd6e6eebbb5801","bytes":45380,"sha256":"9b52fa3ceafb51d65d946bcdfbd58ce323f1fc9aa8b72432452b3729c975c3b4","path":"topics/visible-flex-exact-nearby/notes/2026-11-16-R133-frozen-cross-block-current-inputs.json"}],"prior_problem_id":"WPTV_frozen_cross_block_value_tail_v1","prior_run_id":"43854566735","prior_run_attempt":"1","first_unfinished_parent":1,"completed_parent_prefix":1,"total_parent_cells":153,"remaining_body_parents":152,"prior_reference_chain":{"count":1,"sha256":"947c13032e6e6dc6496e42d2a78b0178b41dbc4372069a321f3f501a07547df7"},"no_completed_collar_or_old_target_may_be_recomputed":True,"original_failure_and_complete_file_bindings_preserved":True,"raw_three_or_five_field_records_use_original_lower_upper_hull":True,"single_ball_new_records_read_unchanged":True,"finite_display_parser":"ASCII decimal/scientific; bare, [exact], [mid +/- radius], [+/- radius]; no condensed or nonfinite forms","reference_sign_fallback":"ball centre; then endpoint display midpoint/lower/upper; then K=1/64, gamma=1, Cref=-1; all are reference choices only","future_scientific_restart_requires_another_explicit_remaining_contract":True}
PRIOR_FIELD_SHA256={"actual_checkout_commit":"fdc15495ffe3a6360d65ccdb763ce230bce61d77b68b3491bca3963427b6a52d","actual_progress":"5f3a4ab60fbbab8092c6421d4801158d062c65cddb9d2e519b64ce9ef9086dbd","complete":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0","complete_coefficient_maxima":"45cf27f9814727904fd612b9e1aef313312ec58fa151db5939ecb24757ab3e41","completed_targets":"37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570","conditional_inverse":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed","copied_complete_candidate_metadata":"aa864b2f189497b01dff719f3c16634620fc2f75d22236f81c42236f12abb356","copied_complete_repair_definition":"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47","copied_original_records":"02a86f96d35494fdc13f56bc47cc48415214620c0b28cdccb90a96c170f8fefe","copied_original_scope":"0ecf9b7ebedbd61e1d0309af891d0308ba4615210ae5799a8f225a2284221bab","current_parent":"b3e03ed2d9fb09686e35a6530a75744ef941305f99921ba990ef17dc5ae36cc9","current_target":"386dc13da35428d40b384c448c7f1e0383db637792dce68156f9c491f4fa4878","failure":"b18ba44ff286cd01c4b4a59275f272792197e471ca8610fb634a4da6644c4235","gates":"67deab527dafde52afb72513d259a1d4ac4d2ae7b484dcfe160b386dc59c38ec","inventory_sha256":"81c5386e0443b68673fc69629ee2bf70bab8ed03f9ffd59e02066dedd3f1a712","kind":"473073c84220a9569476d773d3697480d526f70bad88aad29f53601c47d51ee1","last_completed_parent":"caa3bc544996365707a839516f0b9ced54f9536e39134a0ea1c93e77ab612502","manifest_sha256":"1538ce775da1b41097d5a6d81f1b50511d50e2ba79fb6c828d1667a51086145c","mathematical_contract_sha256":"3ec6876153a1b82335aee6ead929ebed298121f83794112d8aab655f5c2e2e49","mesh_summary":"a9ef25981dc073a987c57ac481159526f1c9b72a5806b4a32d2f109281fcd151","original_admission":"f86cc18bcd8253d036eac1fe0d32fe335d71d43894ac6f13866e0553637ff171","original_input_sha256":"00919519f014f74e5e20c4fd2bce48f728aadd69f9acb6a8963f089901780e4e","parameters":"e4981a971565d1e966911ccf39517016c02b1f58024d0e5672d7968c3e092f76","problem_id":"a35ddfd0763fc5f6c950743b37896f7ce1d0d39550f8d186adf4ca1893a0ced6","reference_chain":"8ccf775bfc5d65b7126fefce0d169d3fda31194f41f195bc5610f6357431f8f0","refinement_contract_sha256":"38a7732363163936341cc668136b1bf54c54357e014b41708e91cc3604fd525c","retained_scope":"691e6c77226f980254b31fb5a9a665c8b73df17a52096260551f15a467aa040e","runtime":"01b71a1aeec3c2dacf477658455943bda38d6732a4e920db9ef397aad94e90a4","scientific_modules":"0d499644f80b8db1a127ddadf895bf160268dc3c418550160f2e2d908ace5d7f","selected_mesh":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed","stage":"5246726b2af7bd324c1cc845d12c06cc5b3d778a2ce2d85323b65a29a45bd2b0","whole_candidates":"ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356"}

def require(ok,message):
 if not ok: raise ValueError(message)

def digest(raw):
 return hashlib.sha256(raw).hexdigest()

def canonical(value):
 def encode(v):
  if isinstance(v,Decimal):
   require(v.is_finite(),"finite original JSON number")
   return str(v)
  if isinstance(v,dict):
   return "{"+",".join(json.dumps(k,ensure_ascii=False)+":"+encode(v[k])
                      for k in sorted(v))+"}"
  if isinstance(v,(list,tuple)): return "["+",".join(encode(x) for x in v)+"]"
  return json.dumps(v,ensure_ascii=False,allow_nan=False,separators=(",",":"))
 return (encode(value)+"\n").encode("utf-8")

def data(raw):
 return json.loads(raw,parse_float=Decimal,
                   parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))

def at(value,path):
 for key in path: value=value[key]
 return value

DECIMAL_TOKEN=r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"

def finite_display_tokens(text,context):
 require(isinstance(text,str) and text.isascii() and 0<len(text)<=128,
         context+": bounded ASCII original ball text")
 value=text.strip();bracketed=value.startswith("[")
 if bracketed:
  require(value.endswith("]"),context+": complete outer ball brackets")
  value=value[1:-1].strip()
 else:
  require("[" not in value and "]" not in value,
          context+": no partial ball brackets")
 if "+/-" in value:
  require(bracketed and value.count("+/-")==1,context+": one bracketed radius")
  left,radius=value.split("+/-")
  centre=left.strip() or "0";radius=radius.strip()
  require(re.fullmatch(DECIMAL_TOKEN,radius) is not None,
          context+": finite decimal radius token")
  require(Decimal(radius).is_finite() and Decimal(radius)>=0,
          context+": finite nonnegative printed radius")
  form="mid_radius" if left.strip() else "zero_centred_radius"
 else:
  centre=value;radius=None;form="bracket_exact" if bracketed else "bare_exact"
 require(re.fullmatch(DECIMAL_TOKEN,centre) is not None,
         context+": finite decimal centre token in "+repr(text))
 return centre,radius,form

def signed_display_centre(value,context="original finite reference display"):
 text=value["ball"] if isinstance(value,dict) else value
 return Fraction(finite_display_tokens(text,context)[0])

def record(value,context="original record"):
 require(isinstance(value,dict) and set(value)=={"ball","lower","upper"},
         context+": exact three-field record required")
 require(all(isinstance(x,str) and x.isascii() and 0<len(x)<=128 and not re.search(r"nan|inf",x,re.I)
             and all(len(e)<=6 for e in re.findall(r"[eE][+-]?(\d+)",x))
             for x in value.values()),context+": finite original record text")
 return value

def intrinsic_record(value,context):
 # Original metric_defect.record calls beta_interval.ball_record (five fields).
 # The two JSON numbers are display metadata; no mathematical bound uses them.
 require(isinstance(value,dict) and set(value)==
         {"ball","lower","upper","mid_float","radius_upper_float"},
         context+": exact five-field intrinsic record required")
 record({key:value[key] for key in ("ball","lower","upper")},context)
 for key in ("ball","lower","upper"):
  finite_display_tokens(value[key],context+"/"+key)
 for key in ("mid_float","radius_upper_float"):
  number=value[key]
  require(type(number) is int or
          (isinstance(number,Decimal) and number.is_finite()),
          context+"/"+key+": finite JSON numeric display metadata required")
 require(value["radius_upper_float"]>=0,
         context+"/radius_upper_float: nonnegative display radius required")
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


def npy_bytes(raw,shape):
 require(raw.startswith(b"\x93NUMPY"),"original NPY magic")
 version=tuple(raw[6:8])
 require(version in ((1,0),(2,0),(3,0)),"original NPY version")
 width=2 if version==(1,0) else 4
 size=int.from_bytes(raw[8:8+width],"little")
 require(0<size<=4096,"original NPY header size")
 start=8+width
 header=ast.literal_eval(raw[start:start+size].decode("utf-8" if version==(3,0) else "latin1"))
 require(set(header)=={"descr","fortran_order","shape"}
         and header["descr"]=="<f8" and header["fortran_order"] is False
         and header["shape"]==tuple(shape),"complete original float64 shape")
 payload=raw[start+size:]
 count=1
 for n in shape: count*=n
 require(len(payload)==8*count,"complete original NPY bytes")
 for (bits,) in struct.iter_unpack("<Q",payload):
  require(((bits>>52)&2047)!=2047,"finite original binary64 datum")
 return payload

class CubicData:
 def __init__(self,index,path):
  self.parts=[];self.nodes=[];edge_bits=None;next_piece=0
  for spec in index["parts"]:
   part=Path(path).parent/spec["file"]
   raw=part.read_bytes()
   require(len(raw)==spec["bytes"] and digest(raw)==spec["sha256"],"complete candidate part bytes")
   start=spec["first_interval"];end=spec["last_interval_exclusive"]
   require(type(start) is int and type(end) is int and start==next_piece and start<end,
           "original part order")
   count=end-start
   with zipfile.ZipFile(io.BytesIO(gzip.decompress(raw))) as z:
    require(len(z.infolist())==2 and set(z.namelist())==
            {"radial_nodes.npy","piece_coefficients.npy"},"complete original NPZ fields")
    for info in z.infolist():
     require(info.file_size<=4*count*65*8+8192,"original NPZ finite resource bound")
    rn=npy_bytes(z.read("radial_nodes.npy"),(count+1,))
    cn=npy_bytes(z.read("piece_coefficients.npy"),(4,count,65))
   require(edge_bits is None or rn[:8]==edge_bits,"bitwise original shard interface")
   vals=[Fraction.from_float(x[0]) for x in struct.iter_unpack("<d",rn)]
   require(all(vals[k]<vals[k+1] for k in range(count)),"original node strict order")
   require(float(vals[0])==float(spec["radial_left"])
           and float(vals[-1])==float(spec["radial_right"]),"original displayed shard endpoints")
   self.nodes.extend(vals if edge_bits is None else vals[1:])
   self.parts.append((start,end,cn))
   edge_bits=rn[-8:];next_piece=end
  require(next_piece==6144 and len(self.nodes)==6145 and self.nodes[0]==0
          and self.nodes[-1]==Fraction(25,8),"complete original candidate coverage")
 def value(self,degree,piece,component):
  for first,last,payload in self.parts:
   if first<=piece<last:
    offset=((degree*(last-first)+(piece-first))*65+component)*8
    return Fraction.from_float(struct.unpack_from("<d",payload,offset)[0])
  raise ValueError("original cubic index absent")
 def exact_values(self,piece,point):
  require(self.nodes[piece]<=point<=self.nodes[piece+1],"reference in one original piece")
  x=point-self.nodes[piece]
  result=[]
  for component in range(65):
   value=Fraction(0)
   for degree in range(4): value=value*x+self.value(degree,piece,component)
   result.append(value)
  return result
 def polynomial_values(self,piece,left,right,exact,interval):
  require(self.nodes[piece]<=left<=right<=self.nodes[piece+1],
          "new signed enclosure stays in original cubic piece")
  x=interval(left-self.nodes[piece],right-self.nodes[piece])
  result=[]
  for component in range(65):
   value=exact(0)
   for degree in range(4): value=value*x+exact(self.value(degree,piece,component))
   result.append(value)
  return result


def admit(repo,manifest_path,manifest_sha,native_path,receipts_path,candidate_path,repair_path):
 require(os.environ.get("GITHUB_ACTIONS")=="true"
         and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,"public Actions only")
 repo=Path(repo).resolve()
 raw=Path(manifest_path).read_bytes()
 require(digest(raw)==manifest_sha,"manifest SHA256")
 manifest=data(raw)
 require(manifest["kind"]==MANIFEST_KIND and manifest["problem_id"]==PROBLEM_ID
         and manifest["repository"]==REPOSITORY and manifest["parameters"]==PARAMETERS,
         "fixed whole-target manifest")
 specs=manifest["files"]
 require(len(specs)==manifest["expected_current_input_count"]
         and len({x["role"] for x in specs})==len(specs)
         and len({x["path"] for x in specs})==len(specs),"unique complete current files")
 by_role={x["role"]:x for x in specs}
 texts={s["role"]:read_spec(repo,s) for s in specs}
 for key,expected in (("inventory",INVENTORY_SHA),("mathematical_contract",PROOF_SHA),
                      ("refinement_contract",REFINEMENT_SHA)):
  s=manifest[key]
  require(by_role[s["role"]]==s and s["sha256"]==expected,"fixed complete mathematical contract")
 inventory=data(texts[manifest["inventory"]["role"]])
 old_inventory=data(texts["WHV_readonly_inventory"])
 require(manifest["core_current_files"]==inventory["existing_small_text_inputs"]
         and len(manifest["core_current_files"])==17
         and manifest["historical_inputs"]==inventory["historical_inputs"]
         and len(manifest["historical_inputs"])==19,"entire closed input inventory")
 for s in manifest["core_current_files"]:
  require(by_role[s["role"]]==s,"original current identity")
 require([{k:v for k,v in s.items() if k!="role"} for s in manifest["historical_inputs"][:13]]
         ==old_inventory["historical_parts"],"same original thirteen body parts")
 modules=manifest["scientific_modules"]
 require([s["role"] for s in modules]==["science","readonly_admission"]
         and all(by_role[s["role"]]==s for s in modules),"two new modules")
 originals=("negative_one_source","collar_source","body_source",
  "complete_coefficient_definition","continuous_repair_definition",
  "repaired_value_inflation_definition","lossless_shard_format")
 for role in originals+tuple(s["role"] for s in modules):
  ast.parse(texts[role])
 docs={role:data(texts[role]) for role in
       ("negative_one_summary","negative_one_process","collar_process","body_process",
        "body_summary","body_parts_manifest","WHV_actual","candidate_index")}
 receipt_raw=Path(receipts_path).read_bytes();receipts=data(receipt_raw)
 require(set(receipts)=={"kind","historical_inputs","native","candidate_index",
         "candidate_part_roles","centre_repair_role","old_producers_executed",
         "original_repairs_regenerated","new_artifacts","new_arrays_published","scope"}
         and receipts["kind"]=="complete_readonly_native_cubic_repair_restoration_v1",
         "complete typed readonly restoration")
 for key in ("old_producers_executed","original_repairs_regenerated","new_artifacts","new_arrays_published"):
  require(type(receipts[key]) is int and receipts[key]==0,"no old science or new arrays")
 require(len(receipts["historical_inputs"])==19,"all nineteen restored objects")
 for number,(s,r) in enumerate(zip(inventory["historical_inputs"],receipts["historical_inputs"])):
  extra={"git_tree_blob_and_size_verified","compressed_sha256_verified",
         "chunk_sha256_verified" if number<13 else "identical_original_bytes_materialized"}
  require(set(r)==set(s)|extra and {k:r[k] for k in s}==s
          and all(r[k] is True for k in extra),"complete original restoration tuple")
 require(receipts["candidate_index"]==by_role["candidate_index"]
         and receipts["candidate_part_roles"]==[s["role"] for s in inventory["historical_inputs"][13:18]]
         and receipts["centre_repair_role"]==inventory["historical_inputs"][18]["role"],
         "candidate and repair restoration identities")
 restoration=old_inventory["native_restoration"]
 expected_native={"bytes":restoration["complete_container_bytes"],
  "sha256":restoration["complete_container_sha256"],"complete_concatenation_verified":True}
 require(receipts["native"]==expected_native,"complete concatenation receipt")
 compressed=Path(native_path).read_bytes()
 require(len(compressed)==expected_native["bytes"] and digest(compressed)==expected_native["sha256"],
         "original native container")
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
 left=Fraction(old_inventory["scope"]["body_cut"]); right=Fraction(25,8)
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
 for item in old_inventory["readonly_literal_inputs"]:
  value=roots if item["name"]=="rstar_interval" else at(docs[item["role"]],item["path"])
  expected=item.get("original_record",item.get("original_value"))
  require(value==expected,"original literal "+item["name"])
  literals[item["name"]]=value
 require(len(literals)==9,"nine complete old literals")

 require(native["actual_family_value_and_all_angular_derivative_jumps_zero"] is True,
         "complete actual family value continuity")
 for row_index,row in enumerate(inflated):
  row_context="inflated_rows["+str(row_index)+"]"
  require(type(row["original_candidate_piece"]) is int
          and 0<=row["original_candidate_piece"]<6144,
          row_context+": original cubic piece identity")
  for group,keys in INFLATED_GROUP_KEYS.items():
   context=row_context+"/"+group
   require(group in row and isinstance(row[group],dict)
           and set(row[group])==set(keys),context+": exact original coefficient keys")
   check=intrinsic_record if group=="original_intrinsic_enclosure" else record
   for key in keys: check(row[group][key],context+"/"+key)
  for key in ("full_delta_A0","full_delta_angular_A0","independent_mean_variation_bound"):
   record(row[key],row_context+"/"+key)
  if row["original_right_interface"] is not None:
   interface=row["original_right_interface"]
   require(interface["homogeneous_linear_interface"]=="identity in the same moving unknown"
           and interface["independent_affine_interface_source_retained"] is True,
           "actual raw identity transmission and separate affine jump")
 whv=docs["WHV_actual"]
 require(whv["kind"]=="complete_zero_volterra_positive_head_mesh_v1"
         and whv["problem_id"]=="WHV_zero_volterra_positive_head_mesh_v1"
         and whv["complete"] is True and whv["failure"] is None
         and isinstance(whv["strict_mesh_gate"],dict)
         and set(whv["strict_mesh_gate"])=={"comparison","epsilon_record","passed"}
         and whv["strict_mesh_gate"]["comparison"]=="saved epsilon upper < 1"
         and whv["strict_mesh_gate"]["epsilon_record"]==whv["new_records"]["epsilon"]
         and whv["strict_mesh_gate"]["passed"] is False
         and whv["resolvent_admitted"] is False,
         "complete previous WHV result including failed sufficient comparison")
 gates(whv,"gates",14)
 require(whv["original_input_sha256"]==
         {s["role"]:s["sha256"] for s in old_inventory["complete_existing_text_inputs"]}
         and whv["inventory_sha256"]==by_role["WHV_readonly_inventory"]["sha256"]
         and whv["mathematical_contract_sha256"]==
             "e993f0685dad2bd61740cf1fc02ff20d8cd5c02f43970d2eee05fdba885d5dd2",
         "completed WHV is bound to these exact original inputs")
 require(whv["copied_original_records"]==literals and whv["actual_progress"]==
         {"matrix_allocations":0,"new_maxima_completed":3,"new_required_N_diagnostics_completed":1,
          "new_scalar_records_completed":18,"new_strict_comparisons_completed":1,"old_targets_recomputed":0},
         "all completed WHV records and zero matrix result retained")
 require(set(whv["maxima"])=={"G_b","H_b","L_b"} and len(whv["new_records"])==18,
         "all previous whole maxima and scalar targets")
 cpath=Path(candidate_path)
 require(cpath.read_bytes()==texts["candidate_index"].encode("utf-8"),"whole original candidate index")
 index=docs["candidate_index"];candidate=inventory["readonly_restoration"]["candidate"]
 require(index["kind"]==candidate["kind"] and index["polynomial_order"]==candidate["polynomial_order"]
         and index["coefficient_shape"]==[4,6144,65] and index["radial_nodes_count"]==6145
         and len(index["parts"])==5 and len(index["initial_state"])==65,
         "complete original cubic index shape")
 meta=index["metadata"]
 require(meta["modes"]==32 and meta["physical_frequency_factor"]==4
         and meta["exact_float_amplitude"]==candidate["exact_alpha"]
         and meta["exact_float_nu"]==candidate["exact_nu"]
         and meta["object_sha256"]==candidate["object_sha256"]
         and meta["finite_BVP_success"] is True and meta["mathematical_certificate"] is False,
         "original candidate definition and finite success/noncertificate distinction")
 for s,p in zip(inventory["historical_inputs"][13:18],index["parts"]):
  require(Path(s["path"]).name==p["file"] and Path(p["file"]).name==p["file"]
          and all(s[k]==p[k] for k in ("bytes","sha256","first_interval","last_interval_exclusive")),
          "complete five original cubic part identities")
 cubic=CubicData(index,cpath)
 for row in inflated:
  lo,hi=map(Fraction,row["interval"]);piece=row["original_candidate_piece"]
  require(cubic.nodes[piece]<=lo<hi<=cubic.nodes[piece+1],"whole original row and cubic piece")
 s=inventory["historical_inputs"][18];repair_bytes=Path(repair_path).read_bytes()
 require(len(repair_bytes)==s["bytes"] and digest(repair_bytes)==s["sha256"]
         and hashlib.sha1(b"blob "+str(len(repair_bytes)).encode()+b"\0"+repair_bytes).hexdigest()
         ==s["git_blob_sha"],"entire original repair bytes")
 repair=data(gzip.decompress(repair_bytes))
 gates(repair,"gates",6)
 require(repair["kind"]=="actual_final_exact_continuous_value_repair_v1"
         and repair["complete"] is True and repair["source_sha256"]==by_role["continuous_repair_definition"]["sha256"]
         and repair["candidate_sha256"]==by_role["candidate_index"]["sha256"]
         and repair["derived_definition_sha256"]==
             inventory["readonly_restoration"]["repaired_centre"]["required_definition_sha256"]
         and digest(canonical(repair["definition"]))==repair["derived_definition_sha256"],
         "complete original physical repair definition")
 definition=repair["definition"]
 require(definition["exact_alpha"]==candidate["exact_alpha"]
         and definition["object_sha256"]==candidate["object_sha256"]
         and definition["physical_frequency_factor"]==4 and definition["modes"]==32
         and definition["exact_radial_interval"]==["0","25/8"]
         and definition["offsets_independent_of_eta_and_nu"] is True
         and repair["corrected_value_and_all_angular_derivatives_continuous"] is True
         and repair["corrected_radial_derivative_continuity_claimed"] is False,
         "actual physical repair scaling and value-only continuity")
 suprema=repair["exact_cumulative_coefficient_suprema"]
 require(len(suprema)==65 and all(isinstance(v,str) and v.isascii() and len(v)<=4096 and Fraction(v)>=0 for v in suprema),
         "all sixty-five original exact offset suprema")
 old_scope={key:neg[key] for key in ("physical_parameter","nu_family",
  "entire_positive_interval","fixed_body_cut","ordinary_source_contract","raw_state_contract",
  "same_genuine_forward_and_backward_Riccati_reference",
  "independent_even_mean_and_all_head_and_affine_source_ports_retained",
  "given_complete_head_positive_high_inverse_and_root_graph_proved",
  "full_low_high_Schur_inverse_proved","complete_infinite_BVP_inverse_proved")}
 summary={"checks":[{"name":name,"passed":True} for name in CHECKS],
  "old_gate_counts":[19,11,18,14,6],"new_source_AST_count":2,"old_source_AST_count":7,
  "old_source_import_count":0,"old_targets_recomputed":0,"repairs_regenerated":0,
  "native_bytes":expected_native["bytes"],"native_sha256":expected_native["sha256"],
  "per_order_complete_rows":[4650,4650],"inflated_rows":4650,"interfaces":3594,
  "original_progress_counter":4608,"original_parts_manifest_row_counter":0,
  "candidate_shape":[4,6144,65],"candidate_nodes":6145,"repair_suprema_count":65,
  "current_file_count":len(specs),"historical_input_count":19,
  "restoration_receipts_bytes":len(receipt_raw),"restoration_receipts_sha256":digest(receipt_raw)}
 admitted={"manifest":manifest,"inventory":inventory,"native":native,"rows":inflated,
  "kernels":orders[0]["complete_rows"],"cubic":cubic,"repair_suprema":list(map(Fraction,suprema)),
  "literals":literals,"WHV":whv,"old_scope":old_scope,"candidate_metadata":meta,
  "repair_definition":definition,"admission":summary,"current_receipts":specs,
  "scientific_modules":modules}
 admitted["continuation_admission"]=admit_preserved_prefix(admitted,texts,by_role,receipts)
 admitted["prior_failed_science"]=data(texts["prior_science"])
 return admitted

def admit_preserved_prefix(admitted,texts,by_role,receipt):
 manifest=admitted["manifest"]
 require(manifest.get("continuation_contract")==CONTINUATION_CONTRACT
         and manifest["expected_current_input_count"]==27,
         "exact declared remaining-body input contract")
 for spec in CONTINUATION_CONTRACT["prior_files"]:
  require(by_role.get(spec["role"])==spec,"entire original failed-file identity")
 prior=data(texts["prior_science"]);execution=data(texts["prior_execution"])
 old_manifest=data(texts["prior_manifest"])
 require(set(prior)==set(PRIOR_FIELD_SHA256)
         and digest(canonical(prior))==by_role["prior_science"]["sha256"]
         and {key:digest(canonical(value)) for key,value in prior.items()}==PRIOR_FIELD_SHA256,
         "all32 original scientific fields retained verbatim")
 require(old_manifest["kind"]=="complete_frozen_cross_block_positive_head_current_inputs_v1"
         and old_manifest["problem_id"]==CONTINUATION_CONTRACT["prior_problem_id"]
         and old_manifest["parameters"]==PARAMETERS
         and old_manifest["core_current_files"]==manifest["core_current_files"]
         and old_manifest["historical_inputs"]==manifest["historical_inputs"]
         and len(old_manifest["files"])==24,
         "original complete manifest and same full scientific inputs")
 for key in ("inventory","mathematical_contract","refinement_contract"):
  require(old_manifest[key]==manifest[key],"unchanged complete primary "+key)
 require(prior["kind"]=="complete_frozen_cross_block_value_tail_v1"
         and prior["problem_id"]==old_manifest["problem_id"]
         and prior["parameters"]==PARAMETERS
         and prior["manifest_sha256"]==by_role["prior_manifest"]["sha256"]
         and prior["scientific_modules"]==old_manifest["scientific_modules"]
         and prior["retained_scope"]==manifest["retained_scope"]
         and prior["original_input_sha256"]==
            {s["role"]:s["sha256"] for s in manifest["core_current_files"]},
         "all original parameter/source/scope/binding qualifications")
 require(prior["complete"] is False and prior["stage"]=="failed_saved_complete_prefix"
         and prior["completed_targets"]==[]
         and prior["current_target"]=="complete_frozen_cell_coefficient_maxima"
         and prior["whole_candidates"]=={} and prior["selected_mesh"] is None
         and prior["conditional_inverse"] is None,
         "only the original incomplete whole-maxima target may continue")
 require(execution["kind"]=="small_frozen_public_scientific_execution_v1"
         and execution["repository"]==REPOSITORY
         and execution["run_id"]==CONTINUATION_CONTRACT["prior_run_id"]
         and execution["run_attempt"]==CONTINUATION_CONTRACT["prior_run_attempt"]
         and execution["manifest_sha256"]==prior["manifest_sha256"]
         and execution["problem_id"]==prior["problem_id"]
         and execution["scientific_started"] is True
         and execution["scientific_children"]==1
         and execution["actual_child_returncode"]==1
         and execution["readonly_diagnostic_only"] is False
         and execution["scientific_complete"] is False
         and execution["original_scientific_complete_flag"] is False
         and execution["completed_old_targets_recomputed"]==0,
         "complete original failed execution and unique scientific boundary")
 require(execution["current_input_receipts"]==old_manifest["files"]
         and execution["actual_scientific_checkout"]==prior["actual_checkout_commit"]
         and execution["original_scientific_failure"]==prior["failure"]
         and execution["historical_restoration"]==receipt
         and execution["scientific_files"]==[
          {key:by_role["prior_science"][key] for key in ("path","bytes","sha256")}],
         "original current/native/scientific receipts all match")
 expected_ast=[{key:s[key] for key in ("role","path","sha256")}
               for s in old_manifest["files"] if s["path"].endswith(".py")]
 require(execution["AST_receipts"]==expected_ast and len(expected_ast)==10,
         "all original10 AST receipts, not an old import")
 preflight=execution["readonly_preflight"]
 require(preflight["returncode"]==0 and preflight["stderr_bytes"]==0
         and preflight["complete_output"]==
          {"complete":True,"preflight_only":True,"admission":prior["original_admission"]}
         and preflight["stdout_bytes"]==len(canonical(preflight["complete_output"]))
         and preflight["stdout_sha256"]==digest(canonical(preflight["complete_output"])),
         "entire old successful readonly preflight")
 check_old=dict(prior["original_admission"]);check_new=dict(admitted["admission"])
 require(check_old.pop("current_file_count")==24 and check_new.pop("current_file_count")==27
         and check_old==check_new,"same complete native and candidate qualifications")
 require(prior["gates"]==[{"name":name,"passed":True} for name in CHECKS]+
         [{"name":"predeclared_small_mesh_and_all_original_domains_admitted","passed":True}],
         "all eleven original completed gates")
 progress=prior["actual_progress"]
 require(progress["completed_parent_cells"]==1 and progress["completed_body_intersections"]==0
         and progress["scientific_targets_started"]==1 and progress["scientific_targets_completed"]==0
         and all(progress[key]==0 for key in (
          "new_whole_maxima_completed","new_scalar_records_completed",
          "new_strict_comparisons_completed","conditional_resolvents_completed",
          "old_targets_recomputed","original_repairs_regenerated",
          "finite_matrix_allocations","new_array_artifacts")),
         "exact original completed collar and no completed body/scalar target")
 require(prior["reference_chain"]==CONTINUATION_CONTRACT["prior_reference_chain"]
         and prior["last_completed_parent"]["parent_index"]==0
         and prior["last_completed_parent"]["kind"]=="collar"
         and prior["last_completed_parent"]["body_intersections"]==0
         and prior["current_parent"]["parent_index"]==1
         and prior["current_parent"]["kind"]=="body"
         and prior["current_parent"]["state"]=="started"
         and set(prior["current_parent"])==
          {"kind","left","length_upper","parent_index","right","state"},
         "no saved body reference may be discarded or repeated")
 require(prior["mesh_summary"]["parent_cells"]==153
         and prior["mesh_summary"]["refined_counts"]==[153,306]
         and set(prior["complete_coefficient_maxima"])=={"A","E_b","U_b","L","B"},
         "same mesh and five complete original running maxima")
 root_reference=digest(b"root:S=Id,D=0,B0=0")
 require(prior["last_completed_parent"]["reference_sha256"]==root_reference
         and prior["reference_chain"]["sha256"]==
          digest(bytes.fromhex(digest(b""))+bytes.fromhex(root_reference)),
         "complete original collar reference chain without recomputing its bounds")
 for name,value in prior["complete_coefficient_maxima"].items():
  require(set(value)=={"ball","witness"} and isinstance(value["ball"],str),
          "entire original maximum record "+name)
  finite_display_tokens(value["ball"],"preserved maximum/"+name)
  require((value["witness"] is None and name in ("E_b","U_b","B") and value["ball"]=="0")
          or (name in ("A","L") and value["witness"]["parent_index"]==0
              and value["witness"]["reference_sha256"]==root_reference),
          "unaltered original witness "+name)
 old=prior["copied_original_records"];whv=admitted["WHV"]
 require(old["original_nine"]==admitted["literals"]
         and old["WHV_readonly_records"]==
          {key:whv["new_records"][key] for key in ("A_c","A_c_weight","pi")}
         and old["WHV_previous_strict_mesh_gate"]==whv["strict_mesh_gate"]
         and old["WHV_previous_required_N_diagnostic"]==whv["required_N_diagnostic"]
         and old["WHV_previous_actual_progress"]==whv["actual_progress"]
         and prior["copied_original_scope"]==admitted["old_scope"]
         and prior["copied_complete_candidate_metadata"]==admitted["candidate_metadata"]
         and prior["copied_complete_repair_definition"]==admitted["repair_definition"],
         "all copied original metadata/records exactly inherited")
 return {"kind":"complete_WPTV_preserved_collar_admission_v1",
   "prior_files":CONTINUATION_CONTRACT["prior_files"],
   "prior_full_json_sha256":by_role["prior_science"]["sha256"],
   "all_original_field_sha256":PRIOR_FIELD_SHA256,
   "prior_failure":prior["failure"],"prior_runtime":prior["runtime"],
   "preserved_reference_chain":prior["reference_chain"],
   "preserved_maxima":prior["complete_coefficient_maxima"],
   "preserved_actual_progress":prior["actual_progress"],
   "preserved_last_completed_parent":prior["last_completed_parent"],
   "preserved_interrupted_parent":prior["current_parent"],
   "first_unfinished_parent":1,"remaining_body_parents":152,
   "all32_original_fields_and_complete_execution_read":True,
   "all_old_sources_and_scopes_kept_at_original_file_identities":True,
   "completed_collar_recomputation_forbidden":True,
   "single_ball_new_records_are_read_verbatim":True}
