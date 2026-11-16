"""WCTR full readonly admission; WVC56 and WPS60 frozen; no numeric imports."""
from __future__ import annotations
import ast, gzip, hashlib, io, json, os, re, struct, zipfile
from bisect import bisect_right
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby/"
REPOSITORY="Rogerhu12/math-research-public"
MANIFEST_KIND="complete_clipped_scalar_trace_current_inputs_v1"
PROBLEM_ID="WCTR_complete_clipped_scalar_trace_candidate_v1"
PARAMETERS=json.loads(r'''{"actual_delta_degree":96,"actual_tail_inverse_bound":3,"analytic_new_head_lift_upper":"5/4","bits":320,"complete_family_residual_last_index":352,"cutoff_width":"1/16","decimal_record_digits":75,"first_high_index":97,"head_dimension":193,"high_trial_last_index":160,"maximum_comparison_cells":155,"maximum_doubling_bands":20,"new_array_artifacts":false,"old_targets_recomputed":0,"parent_band_subcells":8,"parent_cells":153,"physical_high_minimum":388,"prior_complete_paired_records":60,"prior_complete_tracefree_records":56,"prior_completed_mode_prefix_records":6,"prior_completed_tracefree_modal_prefix_records":5,"reference_centre_degree":32,"reference_diagonal_lower_clip":"-c/32","reference_diagonal_upper_clip":"c/16","reference_impedance_lower_barrier":"1/16","reference_matrix_normalizer":"I+h^2*D^2/12","reference_outer_impedance":"13/80","reference_q_binary_places":20,"reference_q_floor":"1/8","reference_scalar_trace_lower_clip":"-c/64","reference_scalar_trace_upper_clip":"c/64","refined_cells":24480,"repaired_centre_residual_last_index":224,"same_actual_spaces_and_projections":true,"unchanged_reference_modes_are_read_only":true,"uniform_refinement":160,"whole_zero_trace_candidate_is_read_only":true}''')
INVENTORY_SHA="f7dd2ed019b30c076aa70ad1536601813095ef59bb504049d976eb0cd93b1547"
PROOF_SHA="dda500b8f5e2d02a39fbef4efcc5c2ad10dac93eef194f6e8d5b9b5a816cd0e9"
REFINEMENT_SHA="62adc53eedc1ea339e02f6e2a8fa654e38c92fe04784343557e23c84ddd696c2"
CHECKS=[
 "all_current_UTF8_files_and_three_fixed_contracts_verified",
 "five_new_and_ten_original_definition_sources_AST_only_verified",
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
 require(len(specs)==manifest["expected_current_input_count"]==45
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
 require([s["role"] for s in modules]==["science","readonly_admission","kernel_math","assembly_math","reference_math"]
         and all(by_role[s["role"]]==s for s in modules),"five new modules")
 originals=("negative_one_source","collar_source","body_source",
  "complete_coefficient_definition","continuous_repair_definition",
  "repaired_value_inflation_definition","lossless_shard_format",
  "completed_reference_definition","WIC_module","WQS_module")
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
  "old_gate_counts":[19,11,18,14,6],"new_source_AST_count":5,"old_source_AST_count":10,
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
 admitted["paired_inputs"]=admit_paired_inputs(admitted,texts,by_role)
 admitted["completed_paired_inputs"]=admit_completed_paired_inputs(admitted,texts,by_role)
 admitted["admission"]["checks"].append({
  "name":"all_sixty_old_WPS_records_full_false_scope_and_six_prefix_records_verified",
  "passed":True})
 admitted["admission"]["prior_completed_candidate_records"]=60
 admitted["admission"]["prior_completed_modal_prefix_records"]=6
 admitted["completed_tracefree_inputs"]=admit_completed_tracefree_inputs(admitted,texts,by_role)
 admitted["admission"]["checks"].append({
  "name":"all_fifty_six_old_WVC_records_full_false_scope_and_five_prefix_records_verified",
  "passed":True})
 admitted["admission"]["prior_completed_tracefree_candidate_records"]=56
 admitted["admission"]["prior_completed_tracefree_modal_prefix_records"]=5
 return admitted

PAIRED_INPUT_PINS=json.loads(r'''{"WPTVS_actual":{"git_blob_sha":"c79f9de99b0f6e398c97f840e82a7e653b5e6626","bytes":24767,"sha256":"bdd8857cf98d3497600b349b05fc81b8aab7441cd7020b6a5f337b6067f774ef"},"WOBSA_actual":{"git_blob_sha":"b21c6d0717bccd6827eff4792bb12b8b1cd40d05","bytes":60416,"sha256":"ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79"},"proof_WIC":{"git_blob_sha":"019b1136ebe81e44e98399dff5fb895aafb4362e","bytes":29026,"sha256":"527fc35e48f8bb8807e2dc7e7a4b8726e381d35183f31bf8977b252dbb66e59f"},"proof_WPS":{"git_blob_sha":"e830f7df4643fe77b941478dbde06ebf9378ebef","bytes":43851,"sha256":"ffd000ff15f705ffaaf3c33dddcd0c09c997c0c92d5110bab5be5ea9c114fa72"},"proof_WQS":{"git_blob_sha":"ff2d61db92e89cc9397c6131675bbcd6294a025c","bytes":25336,"sha256":"bea9137248b445405c7ae483fdc56c4875cc515820632b1d34fdee8b6bfc6fee"},"proof_WOB":{"git_blob_sha":"8a55c94d8decc25f33876665119b327eb1d1fd29","bytes":41683,"sha256":"f13024a72e09d9b388fc51eac39d675b656d4d75ee72cdafe449a1c325e92979"},"WIC_module":{"git_blob_sha":"b181bb80373c870769e2c35b28e764ab7be76e44","bytes":11013,"sha256":"c5de896f603424c0fed3892287031d38d775843e55580f52f4759fe1daba4de3"},"WQS_module":{"git_blob_sha":"d39ae08753f04a5b59c90231d605f8443b8cb9eb","bytes":10070,"sha256":"878c4aec5ed14f4d5e5f3d24ecd23476373a5e26c7b1dd4119b2198e9b73bb02"},"completed_reference_definition":{"git_blob_sha":"ff79fe62e6a948b2536d2594e995047eb65fd820","bytes":31266,"sha256":"159d8fdc153cadf844e1d28f2e0271ae12e55c38d560d7330ee28f164bf21d3c"}}''')
PAIRED_RECORD_PATHS=json.loads(r'''{"C_c":["WOBSA_actual",["copied_original_scalar_records","C_c"]],"C_b":["WOBSA_actual",["copied_original_scalar_records","C_b"]],"Y_c":["WOBSA_actual",["copied_original_scalar_records","Y_c"]],"Y_b":["WOBSA_actual",["copied_original_scalar_records","Y_b"]],"E_minus":["WOBSA_actual",["copied_original_scalar_records","E_minus"]],"mu_minus":["WOBSA_actual",["copied_original_scalar_records","mu_minus"]],"P_b_raw":["WOBSA_actual",["complete_new_graphs","complete_positive_head_and_outer_columns","complete_new_records","complete_outer_b_raw_state_upper"]],"Y_b_outer":["WOBSA_actual",["complete_new_graphs","complete_positive_head_and_outer_columns","complete_new_records","complete_outer_b_outer_trace_upper"]],"reciprocal_sqrt_two":["WOBSA_actual",["complete_new_graphs","complete_zero_stable_root_receiver_rows","complete_new_records","complete_reciprocal_sqrt_two_upper"]],"A_c":["WHV_actual",["new_records","A_c"]],"lambda_388_minus_two_thirds":["WHV_actual",["new_records","A_c_weight"]],"pi":["WHV_actual",["new_records","pi"]],"shell_1153":["WHV_actual",["copied_original_records","shell_1153"]],"G_c":["WHV_actual",["copied_original_records","G_c"]],"L_c_raw":["WHV_actual",["copied_original_records","L_c_raw"]]}''')

def admit_paired_inputs(admitted,texts,by_role):
 for role,expected in PAIRED_INPUT_PINS.items():
  require(role in by_role and all(by_role[role][key]==value for key,value in expected.items()),
          "fixed complete paired input: "+role)
 prior=data(texts["WPTVS_actual"]);wob=data(texts["WOBSA_actual"])
 require(prior["kind"]=="complete_frozen_cross_block_remaining_body_tail_v1"
         and prior["problem_id"]=="WPTV_remaining_body_after_43854566735_v1"
         and prior["complete"] is True and prior["stage"]=="complete"
         and prior["failure"] is None,"complete original WPTVS")
 gates(prior,"gates",18)
 require(prior["reference_chain"]=={"count":153,"sha256":
  "6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac"}
  and prior["actual_progress"]["completed_body_intersections"]==4801
  and prior["actual_progress"]["completed_parent_cells"]==153
  and prior["actual_progress"]["old_targets_recomputed"]==0
  and prior["selected_mesh"] is None and prior["conditional_inverse"] is None,
  "complete old identity and two failed sufficient comparisons")
 require(set(prior["whole_candidates"])=={"1","2"}
         and all(v["complete"] is True and v["strict_tail_gate"] is False
                 for v in prior["whole_candidates"].values()),"both old false gates retained")
 require(prior["original_input_sha256"]==
         {spec["role"]:spec["sha256"] for spec in admitted["manifest"]["core_current_files"]},
         "same full original body/collar/candidate/repair inputs")
 archive=prior["copied_original_records"];whv=admitted["WHV"]
 require(isinstance(archive,dict) and set(archive)=={
  "original_nine","WHV_readonly_records","WHV_previous_strict_mesh_gate",
  "WHV_previous_required_N_diagnostic","WHV_previous_actual_progress"},
  "complete original WPTVS five-part scalar archive")
 require(archive["original_nine"]==admitted["literals"]==whv["copied_original_records"]
         and archive["WHV_readonly_records"]==
             {key:whv["new_records"][key] for key in ("A_c","A_c_weight","pi")}
         and archive["WHV_previous_strict_mesh_gate"]==whv["strict_mesh_gate"]
         and archive["WHV_previous_required_N_diagnostic"]==whv["required_N_diagnostic"]
         and archive["WHV_previous_actual_progress"]==whv["actual_progress"],
         "all original scalar, failed-gate, required-N and progress objects identical")
 require(prior["copied_complete_candidate_metadata"]==admitted["candidate_metadata"]
         and prior["copied_complete_repair_definition"]==admitted["repair_definition"]
         and prior["copied_original_scope"]==admitted["old_scope"],
         "same original coefficients and positive ordinary-dr realization")
 require(prior["mesh_summary"]["parent_cells"]==153
         and prior["mesh_summary"]["all_full_delta_mean_and_low_columns_retained"] is True
         and prior["mesh_summary"]["homogeneous_raw_transmission_is_identity"] is True
         and prior["mesh_summary"]["reference_q_floor"]=="1/8"
         and prior["mesh_summary"]["reference_q_binary_places"]==20,
         "same exact inherited S/D/B0 identity, not old norm reevaluation")
 require(wob["kind"]=="complete_outer_rows_and_rough_positive_observation_bounds_v1"
         and wob["problem_id"]=="selected_WOB_complete_outer_source_and_root_rows_v1"
         and wob["complete"] is True and wob["proved"] is True
         and wob["failure"] is None and wob["actual_returncode"]==0,"complete WOBSA receiver")
 gates(wob,"gates",18)
 require(wob["actual_progress"]["new_records_saved"]==37
         and wob["actual_progress"]["new_graphs_completed"]==6
         and wob["actual_progress"]["old_scientific_calls"]==0
         and wob["input_sha256"]["WHVA"]==by_role["WHV_actual"]["sha256"]
         and wob["input_sha256"]["negative"]==by_role["negative_one_summary"]["sha256"]
         and wob["input_sha256"]["proof_WOB"]==by_role["proof_WOB"]["sha256"],
         "same complete raw seven-port source and actual outer units")
 require(wob["parameters"]["original_raw_state_window"]=="ordinary L2_dr H^-1"
         and wob["parameters"]["original_outer_high_and_low_window"]=="H^-5/6"
         and wob["parameters"]["same_selected_member_only"] is True
         and wob["retained_scope"]["full_low193_rows_and_independent_even_mean_retained"] is True
         and wob["retained_scope"]["full_source_jump_root_mean_and_cokernel_rows_retained"] is True,
         "complete unchanged physical/source/endpoint domains")
 docs={"WPTVS_actual":prior,"WOBSA_actual":wob,"WHV_actual":admitted["WHV"]}
 records={}
 for name,(role,path) in PAIRED_RECORD_PATHS.items():
  value=at(docs[role],path)
  if name in ("G_c","L_c_raw"):
   require(isinstance(value,str) and Fraction(value)>0,"exact old collar literal "+name)
  elif set(value)=={"ball"}:
   require(isinstance(value["ball"],str) and value["ball"].isascii()
           and len(value["ball"])<512,"whole new-style saved old ball "+name)
   finite_display_tokens(value["ball"],"copied/"+name)
  else:
   record(value,"copied/"+name)
  records[name]=value
 require(len(records)==15,"all fifteen complete typed old records")
 scope={"WPTVS_parameters":prior["parameters"],"WPTVS_retained_scope":prior["retained_scope"],
  "WPTVS_mesh_summary":prior["mesh_summary"],"WPTVS_original_scope":prior["copied_original_scope"],
  "WPTVS_complete_original_scalar_archive":archive,
  "WOBSA_parameters":wob["parameters"],"WOBSA_retained_scope":wob["retained_scope"],
  "WOBSA_complete_positive_columns":wob["complete_new_graphs"]["complete_positive_head_and_outer_columns"],
  "full_degree32_repaired_centre_and_degree96_error_distinction":True,
  "repaired_centre_source_output_last_j":224,"complete_actual_source_output_last_j":352,
  "opaque_family_error_leg_is_a_full_output_norm_not_a_128_coordinate_projection":True,
  "all_seven_primal_dual_ports_and_true_mean_rows_retained":True}
 return {"records":records,"scope":scope,"reference_chain":prior["reference_chain"],
  "completed_five_maxima":prior["complete_coefficient_maxima"],
  "old_false_candidates":prior["whole_candidates"],
  "reference_definition_pin":by_role["completed_reference_definition"],
  "old_native_restoration_receipt":admitted["admission"]["restoration_receipts_sha256"],
  "all_completed_targets_read_only":True}


COMPLETED_PAIRED_PINS=json.loads(r'''{"WPS_actual":{"bytes":65347,"git_blob_sha":"17a70a8a6304f387d271378f31964e075ddb9594","path":"topics/visible-flex-exact-nearby/notes/complete_paired_finite_residual_ci/run-43878765372-1/actual-scientific-conclusion.json","role":"WPS_actual","sha256":"0c2467867a6eade717a1df17936729f5e6978ee49fc2cf611e183424a51e2123"},"WPS_execution":{"bytes":35857,"git_blob_sha":"21bf7ec0d72950132e3b0c09f940069588640302","path":"topics/visible-flex-exact-nearby/notes/complete_paired_finite_residual_ci/run-43878765372-1/execution.json","role":"WPS_execution","sha256":"01d18a4461d4aef6bff42484f195a95a5889a9e4d9ebbe2da4428a5898255c71"},"WPS_manifest":{"bytes":48445,"git_blob_sha":"ed9aede898fcb79523a188ecee54a00763593019","path":"topics/visible-flex-exact-nearby/notes/2026-11-16-R133-complete-paired-finite-residual-current-inputs.json","role":"WPS_manifest","sha256":"aabc28e194b27377d26f24ec7fff03708c0ff903841881233429ab0e36b76981"},"proof_WPSA":{"bytes":50464,"git_blob_sha":"6bcd4484f596e39f94cb6adc870dec3b937ad984","path":"topics/visible-flex-exact-nearby/results/R133-supplement-actual-complete-paired-finite-residual-and-false-gate.md","role":"proof_WPSA","sha256":"470d2547de70dea45468103bc3518e6ed5bcc757c348543896df4edda65a2f92"},"proof_WVC":{"bytes":29128,"git_blob_sha":"e377cb2e0578fc66ba8a7bc32e339fadcb0a242c","path":"topics/visible-flex-exact-nearby/results/R133-supplement-continuous-repaired-centre-trials-and-clipped-tracefree-reference.md","role":"proof_WVC","sha256":"fade78e696506af0ef2c1e304e824ff7415c63df53b31f0ed299d8ff548845a8"}}''')
COMPLETED_PAIRED_FIELD_IDENTITIES=json.loads(r'''{"actual_checkout_commit":{"bytes":43,"sha256":"736387b83de4a0b0cc5b9dab4d3445693154c661be1e8c4c4362f36876e45a0d"},"actual_mathematical_wall_seconds":{"bytes":14,"sha256":"39ad6c1bbdea0f306348094ed9fb3a132eb99de45d78ac39e08c031a7f8f1cc8"},"actual_progress":{"bytes":647,"sha256":"50de2f1bb7d051abdaed7207122b34220456f12707f65defc92d42b2a5f3395c"},"actual_returncode":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"automatic_retry_authorized":{"bytes":6,"sha256":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0"},"complete":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"complete_current_file_receipts":{"bytes":10697,"sha256":"d20216c0ca94e0b1dc45c1a379b28c2f5ae742229e4f03b4d92b39dc8cf32908"},"complete_new_graphs":{"bytes":9081,"sha256":"55297e96bebd664ef1c37787d208a3b3c5497b4ffed97731170b5a233215760a"},"complete_restoration_receipts":{"bytes":13771,"sha256":"4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac"},"complete_support_contract":{"bytes":231,"sha256":"eb6ade8a2e2561fa863370055c2a8012ccb578a161277bdde77b85d4249a3c33"},"completed_targets":{"bytes":186,"sha256":"709c5e57181e94d5048670fcfbb1536f661ca7d0bef058e8ccbc1951751e8a7b"},"conditional_finite_inverse":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"copied_complete_candidate_metadata":{"bytes":2581,"sha256":"aa864b2f189497b01dff719f3c16634620fc2f75d22236f81c42236f12abb356"},"copied_complete_repair_definition":{"bytes":792,"sha256":"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"},"copied_original_records":{"bytes":2627,"sha256":"b313df918a9ec86507695b49ba8eb5c5a75afbe268faeffdb14ece854f1f2e71"},"copied_original_scope":{"bytes":8502,"sha256":"94c595173f4591660211251da7f67ea47e15fd52749167379f5ff4c50909736b"},"current_target":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"failure":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"finite_gate":{"bytes":341,"sha256":"c6c4883d48526c61556d6741ad9a49d72aa47323769f8c9a3bd54e27eca61689"},"gates":{"bytes":1705,"sha256":"01ee6e3a7581450f8101695e4d784894723bbf94651d7981ba2a6749d3bf3828"},"input_sha256":{"bytes":3050,"sha256":"4e7d8b1472ebedb34d9015fc85553fce9fa0dd73ee1bc6942a8a636e51d23245"},"kind":{"bytes":47,"sha256":"ca7d187dd18be9551a7a8f5d6a6f2d9c25b4548bdc9c2cfe64a1fe4a6df45ab6"},"manifest_sha256":{"bytes":67,"sha256":"9f3b7dad11178fd3f3aabad39c82ecbaaee2ee7728d7f9e5ef1f2f5e3e385ee5"},"original_admission":{"bytes":1539,"sha256":"dda0de3bd7936363cd32d33baf4d8d05d3fa853b6186da2c43e7f57a6712cff4"},"parameters":{"bytes":627,"sha256":"8e416ccdca32608a50d3a97435ca6abf40fe0cf959d47e49da089a2734c0d5e9"},"preparation_prefix":{"bytes":323,"sha256":"ae009c73b02625046b47309b2e7e39487f2169ab062b72ca302052713d21028e"},"problem_id":{"bytes":41,"sha256":"cbe10b13b3f2ab8a0bcadd082042a2a54941f9b293b557d90b06ccc050db3b31"},"proved":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"reference_chain":{"bytes":90,"sha256":"17a03aa6671788c510cb926fe507c7686bd0e7610c49dd1e1cf5fd2cb8b684ca"},"reference_mode_prefix":{"bytes":827,"sha256":"f2f9c5ef4499ef9775ee08375817546c74670587ce7ed9021bf056e7da0d7a38"},"retained_completed_five_maxima":{"bytes":2350,"sha256":"407ca196cf8f60ac7c037cd2c2056673e139ecd4c1ecc4343d78a5cbf99a6f74"},"retained_original_false_candidates":{"bytes":1082,"sha256":"af586adb9e63165b204717ac8ace80c2d05285940573a1f7bdc39599b89ae187"},"retained_scope":{"bytes":1486,"sha256":"50eefdca8e6d7359e8e3e5fd9b11ef73d71c096c8e3eb791c6dc1844dcc322e4"},"run_attempt":{"bytes":4,"sha256":"ee0ce7db9ce2f1d4d2e01f0e96d73fa2399a99d825d8a9898947539a8d8e1742"},"run_id":{"bytes":14,"sha256":"6baf361fa913930ab07cc627e880ff3c99e66fc3077e36faf1cc9c7782ade53a"},"runtime":{"bytes":101,"sha256":"55c8f0053c75775912f034ed7a12221ac01f5f5439a1e0dc2ad5f6d2aa1e5734"},"saved_record_counts":{"bytes":201,"sha256":"6edcca8b4e6e061d68e78a81afc257d6b657937ac7b0699bd906adbb553c563e"},"scientific_modules":{"bytes":1363,"sha256":"d9eb55e0e36e0fa001b95509ae6dd835f1672d7be2b3644d72bde20c401705c2"},"stage":{"bytes":11,"sha256":"b4a80c61a1f8c6101403f9f26edc545babd033d6ea52f4cc918a4d8a75d394a4"},"workflow_event_commit":{"bytes":43,"sha256":"3a7b3cdae56ad21506d7ddc029b82d23cffddf5a0f7c636e57196f02303b588c"}}''')
COMPLETED_PAIRED_EXECUTION_FIELD_IDENTITIES=json.loads(r'''{"AST_receipts":{"bytes":3304,"sha256":"ffbe8ce05c72ade5cb8ca0bbdd2ba968a26e4858d76ec13b9c8682d3855f75be"},"actual_child_returncode":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"actual_scientific_checkout":{"bytes":43,"sha256":"736387b83de4a0b0cc5b9dab4d3445693154c661be1e8c4c4362f36876e45a0d"},"all_pulls_match_review":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"child_timeout":{"bytes":6,"sha256":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0"},"child_wall_seconds":{"bytes":14,"sha256":"fa773de6efebc9549c4dc94d007c693eca4393665bf1c7cd2e76b56daa8512ec"},"complete_child_stdout":{"bytes":130,"sha256":"2e13703372d94336333990b6c1b6e8dd3727475f479582366709dc674704a9f6"},"completed_old_targets_recomputed":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"completed_target_names":{"bytes":186,"sha256":"709c5e57181e94d5048670fcfbb1536f661ca7d0bef058e8ccbc1951751e8a7b"},"consumed_marker_publication":{"bytes":389,"sha256":"415071af7f082a3629e4229cb0cdf20e1f434041e65dce28df69e45e2492eb53"},"current_input_receipts":{"bytes":10697,"sha256":"d20216c0ca94e0b1dc45c1a379b28c2f5ae742229e4f03b4d92b39dc8cf32908"},"entry_checkout":{"bytes":43,"sha256":"3a7b3cdae56ad21506d7ddc029b82d23cffddf5a0f7c636e57196f02303b588c"},"failure":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"final_capacity_metadata":{"bytes":266,"sha256":"c7d0d4da1a284f661d5e35cc95fe276e48303d22181348845cc8be7ab7110407"},"finished_utc":{"bytes":35,"sha256":"278d3f810f2669be5e114322061bf6c7b3daf3739d6c92fee5d7e515d66cdba6"},"historical_restoration":{"bytes":13771,"sha256":"4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac"},"immediate_pre_science_capacity":{"bytes":266,"sha256":"3e91d2b7e746df7c260324369622af0e970e306ee8b819cdcb915bc01d529943"},"interrupted_target":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"kind":{"bytes":46,"sha256":"b6d2d89953b4df3f0d089085fa8c5596cafd388f5737725a7c9cd1e10e847ac9"},"manifest_sha256":{"bytes":67,"sha256":"9f3b7dad11178fd3f3aabad39c82ecbaaee2ee7728d7f9e5ef1f2f5e3e385ee5"},"new_Releases":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"new_arrays_published":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"new_artifacts":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"original_scientific_complete_flag":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"original_scientific_failure":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"pre_execution_capacity":{"bytes":266,"sha256":"866a3a02c4133b8f7284de025114531f0fdeb5463fcd439fcf86073d5a98767d"},"problem_id":{"bytes":41,"sha256":"cbe10b13b3f2ab8a0bcadd082042a2a54941f9b293b557d90b06ccc050db3b31"},"publication_attempts":{"bytes":2,"sha256":"53c234e5e8472b6ac51c1ae1cab3fe06fad053beb8ebfd8977b010655bfdd3c3"},"readme_check_count":{"bytes":2,"sha256":"06e9d52c1720fca412803e3b07c4b228ff113e303f4c7ab94665319d832bbfb7"},"readme_checks":{"bytes":2374,"sha256":"d55faa1fc846eae9c15de25f5c74aed3542b167ae2c6b1957fe4b923d3c5e6b5"},"readme_receipt_chain_sha256":{"bytes":67,"sha256":"54a896832e30373bd70d8e1b2c43d78c1d416b97a127b827be5fec5d499693b3"},"readme_retention":{"bytes":90,"sha256":"ae12f795b99ea7f0ba2d8fe98df8007f59f51fb2bddc8bc66ce69fa054393e41"},"readonly_diagnostic_only":{"bytes":6,"sha256":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0"},"readonly_preflight":{"bytes":2302,"sha256":"b1c7f33dd545729746a662c1eb457ab9645ae2d6bed4b4b8b32680b64b411f9c"},"repository":{"bytes":33,"sha256":"ea69415f4036ec17f5e16041068cd74ddb1cc3e19aa80963210e2a69ac8da719"},"run_attempt":{"bytes":4,"sha256":"ee0ce7db9ce2f1d4d2e01f0e96d73fa2399a99d825d8a9898947539a8d8e1742"},"run_id":{"bytes":14,"sha256":"6baf361fa913930ab07cc627e880ff3c99e66fc3077e36faf1cc9c7782ade53a"},"scientific_children":{"bytes":2,"sha256":"4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"},"scientific_complete":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"scientific_files":{"bytes":229,"sha256":"d2a95398931aa68c79c82ca6e3da3a487a66c05cc6c39a7adef3020a0a764d73"},"scientific_finished_utc":{"bytes":35,"sha256":"f9cda7ead6d9a4e0597ff3dda5fbbd0a0ef5863dda65cd11c9c9614f6c388a8a"},"scientific_started":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"scientific_started_utc":{"bytes":35,"sha256":"4fe271c42bea436b48331eee1269cd67ed6522b456ae68de4e3fb6076b89af66"},"started_utc":{"bytes":35,"sha256":"e6c89fd25acd5c7d43bc1842cba73cc0769a19e7c1f5ee0b7d0c24285087c580"},"workflow_event_commit":{"bytes":43,"sha256":"3a7b3cdae56ad21506d7ddc029b82d23cffddf5a0f7c636e57196f02303b588c"}}''')
COMPLETED_PAIRED_GRAPH_KEYS=json.loads(r'''{"complete_actual_E_D_T":["complete_actual_D_upper","complete_actual_E0_upper","complete_actual_T_upper","complete_actual_finite_defect_upper"],"complete_actual_paired_receivers":["complete_actual_paired_LH_upper","complete_actual_tail_LH_upper","complete_centre_paired_LH_column_upper","complete_centre_paired_LH_norm_upper","complete_centre_paired_LH_row_upper","complete_centre_tail_LH_column_upper","complete_centre_tail_LH_norm_upper","complete_centre_tail_LH_row_upper","complete_difference_paired_LH_column_upper","complete_difference_paired_LH_norm_upper","complete_difference_paired_LH_row_upper","complete_difference_tail_LH_upper","complete_head_paired_error_upper","complete_low_generator_difference_column_upper","complete_low_generator_difference_norm_upper","complete_low_generator_difference_row_upper","complete_low_generator_tail_error_upper","complete_outer_paired_error_upper","complete_raw_difference_LH_receiver_column_upper","complete_raw_difference_LH_receiver_norm_upper","complete_raw_difference_LH_receiver_row_upper","complete_raw_difference_tail_LH_upper"],"complete_endpoint_correction":["complete_head_endpoint_correction_upper","complete_high_trace_endpoint_receiver_upper","complete_outer_endpoint_correction_upper"],"complete_high_trial_source":["complete_body_ordinary_source_upper","complete_family_HL_body_residual_upper","complete_family_high_kernel_column_upper","complete_family_high_kernel_norm_upper","complete_family_high_kernel_row_upper","complete_high_outer_trace_error_upper","complete_high_state_error_upper","complete_repaired_centre_body_residual_column_upper","complete_repaired_centre_body_residual_norm_upper","complete_repaired_centre_body_residual_row_upper","complete_trial_raw_column_upper","complete_trial_raw_norm_upper","complete_trial_raw_row_upper"],"complete_local_signed_remainder":["complete_actual_head_tail_source_upper","complete_actual_outer_tail_source_upper","complete_signed_centre_paired_source_column_upper","complete_signed_centre_paired_source_norm_upper","complete_signed_centre_paired_source_row_upper","complete_signed_centre_tail_source_column_upper","complete_signed_centre_tail_source_norm_upper","complete_signed_centre_tail_source_row_upper"],"complete_reference_receivers":["complete_reference_Z_squared_upper","complete_reference_column_ratio_upper","complete_reference_head_lift_upper","complete_reference_inverse_norm_upper","complete_reference_mean_endpoint_receiver_upper","complete_reference_odd_endpoint_receiver_upper","complete_reference_rho_column_ratio_upper","complete_reference_rho_defect_upper","complete_reference_rho_row_ratio_upper","complete_reference_row_ratio_upper"]}''')
COMPLETED_PAIRED_GATES=json.loads(r'''["all_current_UTF8_files_and_three_fixed_contracts_verified","five_new_and_ten_original_definition_sources_AST_only_verified","all_nineteen_historical_receipts_and_original_native_bytes_verified","complete_original_summary_and_native_projection_identical","both_complete_4650_row_covers_and_3594_interfaces_verified","same_real_family_and_all_original_successes_verified","all_nine_original_literals_and_completed_WHVA_retained","all_five_original_cubic_parts_and_full_shape_verified","original_repair_whole_document_and_all_65_suprema_verified","actual_raw_identity_transmissions_and_full_affine_ports_retained","fixed_directed_runtime_and_one_new_entry","all_fifteen_old_records_typed_and_published_tail_bound_retained","entire_frozen_reference_definition_chain_materialized_without_old_bounds","complete_continuous_parent_and_comparison_domains_admitted","complete_reference_receivers_saved","complete_high_trial_source_saved","complete_actual_paired_receivers_saved","complete_local_signed_remainder_saved","complete_endpoint_correction_saved","complete_actual_E_D_T_saved","all_current_inputs_and_manifest_reverified_after_new_work","complete_whole_candidate_shape_and_old_zero_recomputation"]''')

def admit_completed_paired_inputs(admitted,texts,by_role):
 """Every old WPS field and record is read, never numerically reevaluated."""
 for role,spec in COMPLETED_PAIRED_PINS.items():
  require(by_role.get(role)==spec,"fixed complete previous WPS/proof object "+role)
 prior=data(texts["WPS_actual"]);execution=data(texts["WPS_execution"])
 previous_manifest=data(texts["WPS_manifest"])
 for value,identities,label in (
    (prior,COMPLETED_PAIRED_FIELD_IDENTITIES,"complete prior scientific"),
    (execution,COMPLETED_PAIRED_EXECUTION_FIELD_IDENTITIES,"complete prior execution")):
  require(set(value)==set(identities),label+" complete field set")
  for key,expected in identities.items():
   raw=canonical(value[key])
   require(len(raw)==expected["bytes"] and digest(raw)==expected["sha256"],
           label+" original whole field "+key)
 require(prior["kind"]=="complete_paired_finite_residual_candidate_v1"
         and prior["problem_id"]=="WPS_complete_paired_finite_residual_v1"
         and prior["complete"] is True and prior["proved"] is True
         and prior["stage"]=="complete" and prior["failure"] is None
         and prior["actual_returncode"]==0 and prior["current_target"] is None
         and prior["automatic_retry_authorized"] is False,"old completed false candidate")
 require(prior["gates"]==[{"name":name,"passed":True} for name in COMPLETED_PAIRED_GATES],
         "all twenty-two original complete structural gates")
 require(set(prior["complete_new_graphs"])==set(COMPLETED_PAIRED_GRAPH_KEYS)
         and len(prior["completed_targets"])==6
         and set(prior["completed_targets"])==set(COMPLETED_PAIRED_GRAPH_KEYS),
         "all six original graphs")
 count=0
 for name,keys in COMPLETED_PAIRED_GRAPH_KEYS.items():
  graph=prior["complete_new_graphs"][name]
  require(set(graph)=={"complete","new_records"} and graph["complete"] is True
          and set(graph["new_records"])==set(keys)
          and prior["saved_record_counts"][name]==len(keys),
          "every original complete graph shape "+name)
  for key in keys:
   value=graph["new_records"][key]
   require(isinstance(value,dict) and set(value)=={"ball"},
           "original complete new-record type "+name+"/"+key)
   finite_display_tokens(value["ball"],"original WPS/"+name+"/"+key)
   count+=1
 require(count==prior["actual_progress"]["new_scalar_records_saved"]==60,
         "all sixty original completed records")
 require(prior["reference_mode_prefix"]["completed_modes"]==96
         and len(prior["reference_mode_prefix"]["running"])==6
         and set(prior["reference_mode_prefix"]["running"])==
             set(prior["reference_mode_prefix"]["witnesses"])
         and all(type(j) is int and 1<=j<=96
                 for j in prior["reference_mode_prefix"]["witnesses"].values()),
         "all six saved original modal prefixes and witnesses")
 for name,value in prior["reference_mode_prefix"]["running"].items():
  require(set(value)=={"ball"},"complete saved old modal-prefix record")
  finite_display_tokens(value["ball"],"old mode prefix/"+name)
 require(prior["finite_gate"]["passed"] is False
         and prior["finite_gate"]["actual_tail_inverse_upper"]==3
         and prior["finite_gate"]["actual_tail_gate_is_published_analytic_m160"] is True
         and prior["finite_gate"]["complete_defect_record"]==
           prior["complete_new_graphs"]["complete_actual_E_D_T"]["new_records"]
                ["complete_actual_finite_defect_upper"]
         and prior["conditional_finite_inverse"] is None,
         "old complete finite sufficient gate is false and remains false")
 require(prior["actual_progress"]["original_body_intersections"]==4801
         and prior["actual_progress"]["original_closed_rows_covered"]==4650
         and prior["actual_progress"]["completed_new_body_parent_packets"]==152
         and prior["actual_progress"]["comparison_cells"]==155
         and prior["actual_progress"]["reference_modes_completed"]==96
         and prior["actual_progress"]["refined_cells"]==24480
         and all(prior["actual_progress"][key]==0 for key in (
           "old_targets_recomputed","old_producer_imports_or_calls",
           "old_reference_bounds_reevaluated","dense_finite_matrices_allocated",
           "new_array_artifacts_published","physical_state_columns_computed")),
         "complete old domains, completed prefix and zero old science")
 require(previous_manifest["kind"]=="complete_paired_finite_residual_current_inputs_v1"
         and previous_manifest["problem_id"]==prior["problem_id"]
         and previous_manifest["expected_current_input_count"]==36
         and len(previous_manifest["files"])==36
         and previous_manifest["parameters"]==prior["parameters"]
         and previous_manifest["retained_scope"]==prior["retained_scope"]
         and previous_manifest["scientific_modules"]==prior["scientific_modules"]
         and digest(texts["WPS_manifest"].encode())==prior["manifest_sha256"]
            ==execution["manifest_sha256"],"full original source/manifest binding")
 old_by_role={s["role"]:s for s in previous_manifest["files"]}
 require(len(old_by_role)==36
         and prior["complete_current_file_receipts"]==previous_manifest["files"]
         and execution["current_input_receipts"]==previous_manifest["files"]
         and prior["input_sha256"]=={k:s["sha256"] for k,s in old_by_role.items()},
         "all thirty-six complete previous file receipts")
 new_source_roles={"science","readonly_admission","kernel_math","assembly_math","reference_math"}
 for role,spec in old_by_role.items():
  if role not in new_source_roles|{"worker","rules"}:
   require(by_role[role]==spec,"unchanged original input receipt "+role)
 require(previous_manifest["core_current_files"]==admitted["manifest"]["core_current_files"]
         and previous_manifest["historical_inputs"]==admitted["manifest"]["historical_inputs"]
         and len(execution["AST_receipts"])==16,"same entire original coefficient closure")
 for item in execution["AST_receipts"]:
  require(set(item)=={"path","role","sha256"}
          and item["role"] in old_by_role
          and item["path"]==old_by_role[item["role"]]["path"]
          and item["sha256"]==old_by_role[item["role"]]["sha256"],
          "full original AST source identity")
 require(execution["scientific_children"]==1 and execution["scientific_started"] is True
         and execution["scientific_complete"] is True
         and execution["actual_child_returncode"]==0
         and execution["failure"] is None and execution["interrupted_target"] is None
         and execution["original_scientific_failure"] is None
         and execution["original_scientific_complete_flag"] is True
         and execution["completed_old_targets_recomputed"]==0
         and execution["new_artifacts"]==execution["new_arrays_published"]
             ==execution["new_Releases"]==0,"old complete execution and no lost target")
 for key in ("run_id","run_attempt","workflow_event_commit"):
  require(execution[key]==prior[key],"old original execution/science "+key)
 require(execution["actual_scientific_checkout"]==prior["actual_checkout_commit"]
         and execution["scientific_files"]==[{
           k:by_role["WPS_actual"][k] for k in ("path","bytes","sha256")}],
         "actual original full scientific file")
 preflight=execution["readonly_preflight"]
 require(preflight["returncode"]==0 and preflight["stderr_bytes"]==0
         and preflight["complete_output"]["complete"] is True
         and preflight["complete_output"]["flint_imported"] is False
         and preflight["complete_output"]["admission"]==prior["original_admission"],
         "full original readonly successful boundary")
 raw=canonical(preflight["complete_output"])
 require(len(raw)==preflight["stdout_bytes"]
         and digest(raw)==preflight["stdout_sha256"],"complete original preflight bytes")
 paired=admitted["paired_inputs"]
 for oldkey,current in (
    ("copied_original_records",paired["records"]),
    ("copied_original_scope",paired["scope"]),
    ("copied_complete_candidate_metadata",admitted["candidate_metadata"]),
    ("copied_complete_repair_definition",admitted["repair_definition"]),
    ("retained_completed_five_maxima",paired["completed_five_maxima"]),
    ("retained_original_false_candidates",paired["old_false_candidates"]),
    ("reference_chain",paired["reference_chain"])):
  require(prior[oldkey]==current,"whole unchanged original object "+oldkey)
 require(prior["complete_restoration_receipts"]==execution["historical_restoration"]
         and digest(canonical(prior["complete_restoration_receipts"]))==
                 admitted["admission"]["restoration_receipts_sha256"],
         "same complete nineteen-object readonly restoration")
 comparable=dict(admitted["admission"]);comparable["current_file_count"]=36
 require(comparable==prior["original_admission"],"same complete old admission except current count")
 reference=prior["complete_new_graphs"]["complete_reference_receivers"]["new_records"]
 family=prior["complete_new_graphs"]["complete_high_trial_source"]["new_records"][
           "complete_family_HL_body_residual_upper"]
 # This is a rational comparison of the saved display enclosure, not a new
 # Arb evaluation or an original target recomputation.
 midpoint,radius,form=finite_display_tokens(reference["complete_reference_Z_squared_upper"]["ball"],
                                       "original complete reference Z record")
 require(Fraction(midpoint)+Fraction(radius or "0")<Fraction(33,100),
         "published old complete Z implies the new analytic lift bound")
 archive={
  "complete_original_scientific_file":by_role["WPS_actual"],
  "complete_original_execution_file":by_role["WPS_execution"],
  "complete_original_manifest_file":by_role["WPS_manifest"],
  "complete_original_field_verification":{
   "scientific_field_count":40,"execution_field_count":45,
   "scientific_identity_table_sha256":digest(canonical(COMPLETED_PAIRED_FIELD_IDENTITIES)),
   "execution_identity_table_sha256":digest(canonical(COMPLETED_PAIRED_EXECUTION_FIELD_IDENTITIES)),
   "full_tables_are_in_the_current_pinned_readonly_module":True,
   "all_original_fields_verified_before_science":True},
  "complete_original_parameters":prior["parameters"],
  "complete_original_retained_scope":prior["retained_scope"],
  "complete_original_actual_progress":prior["actual_progress"],
  "complete_original_finite_gate":prior["finite_gate"],
  "complete_original_reference_mode_prefix":prior["reference_mode_prefix"],
  "complete_original_reference_graph":prior["complete_new_graphs"]["complete_reference_receivers"],
  "complete_original_family_HL_record":family,
  "complete_original_scientific_modules":prior["scientific_modules"],
  "complete_original_completion":{k:prior[k] for k in (
      "complete","proved","stage","failure","actual_returncode","automatic_retry_authorized")},
  "all_sixty_completed_records_read_without_reevaluation":True,
  "all_six_original_modal_prefix_records_and_witnesses_retained":True,
  "all_original_complete_objects_bound_by_full_file_and_field_identity":True,
  "no_original_success_or_false_sufficient_gate_reclassified":True}
 return {"archive":archive,"reference_records":reference,"family_HL_record":family,
         "old_completed_record_count":60,"old_prefix_record_count":6}


COMPLETED_TRACE_PINS=json.loads(r'''{"WVC_actual":{"bytes":78627,"git_blob_sha":"746ec1e16befe8914c64521ad087c1f1dd23ab73","path":"topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json","role":"WVC_actual","sha256":"85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88"},"WVC_execution":{"bytes":37911,"git_blob_sha":"c8cd8e8bb863c500a1e26c009e0af76cd7cb8941","path":"topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/execution.json","role":"WVC_execution","sha256":"5e560887d2deee497cb9da5b7549af1070db36cf69a7b11077ef4a0bb4f0feb5"},"WVC_manifest":{"bytes":60844,"git_blob_sha":"1ea008a1df3116aedd66be67b11b1d8ec62af2d5","path":"topics/visible-flex-exact-nearby/notes/2026-11-16-R133-continuous-centre-tracefree-current-inputs.json","role":"WVC_manifest","sha256":"229198f56efdf10ea8de6fef50804aa3832ca5ff2127101685c8d7117c9afbfb"},"proof_WCTR":{"bytes":26966,"git_blob_sha":"21491641c33a4261d6364c2107d80882d11d0e49","path":"topics/visible-flex-exact-nearby/results/R133-supplement-clipped-scalar-trace-matrix-normalizers-and-paired-circuits.md","role":"proof_WCTR","sha256":"efe08e59290ffb483dc97f59443eb4a7100390e7d655a846b954e409d5084295"}}''')
COMPLETED_TRACE_FIELD_IDENTITIES=json.loads(r'''{"actual_checkout_commit":{"bytes":43,"sha256":"b10480100811bf79025806b82ec7c30723383103e65351c958ab461d02cff1d2"},"actual_mathematical_wall_seconds":{"bytes":14,"sha256":"f1152bf01b295572174295506e483164ad638f6cf496de5f4b8984dd9b8c9ba6"},"actual_progress":{"bytes":819,"sha256":"025ee97a08c80ef85d07d2aac09394f19a7696f0a0f4ed8203b1e0cf6cefb275"},"actual_returncode":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"automatic_retry_authorized":{"bytes":6,"sha256":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0"},"complete":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"complete_current_file_receipts":{"bytes":12199,"sha256":"45e8cd94d6b806042732fc206994e293309cb6a007651bbf408e742802b21629"},"complete_new_graphs":{"bytes":8637,"sha256":"0882b563cdd2e425d5d1e383bd158ce5bce7fb1604903df2bb1a0756b5f4ea42"},"complete_restoration_receipts":{"bytes":13771,"sha256":"4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac"},"complete_support_contract":{"bytes":520,"sha256":"622693074042afeceb02fb81efb373aeb8d33c01003332ba16d5b0f6eb349067"},"completed_targets":{"bytes":186,"sha256":"709c5e57181e94d5048670fcfbb1536f661ca7d0bef058e8ccbc1951751e8a7b"},"conditional_finite_inverse":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"copied_complete_candidate_metadata":{"bytes":2581,"sha256":"aa864b2f189497b01dff719f3c16634620fc2f75d22236f81c42236f12abb356"},"copied_complete_repair_definition":{"bytes":792,"sha256":"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"},"copied_original_records":{"bytes":2627,"sha256":"b313df918a9ec86507695b49ba8eb5c5a75afbe268faeffdb14ece854f1f2e71"},"copied_original_scope":{"bytes":8502,"sha256":"94c595173f4591660211251da7f67ea47e15fd52749167379f5ff4c50909736b"},"current_target":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"failure":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"finite_gate":{"bytes":341,"sha256":"3eb7880c2ebf4f282f5101c1246b51bca718bca0bcffa2ba5198364bd4ace819"},"gates":{"bytes":1808,"sha256":"e475a0f9db43ad510a8b72672576747bcefc432ea7e259e02fbb69254e648f69"},"input_sha256":{"bytes":3454,"sha256":"b49b74104fea8c7bcc5de012882a7be2b8bad72859e8bbdb77ed71df7a9ced7d"},"kind":{"bytes":52,"sha256":"f31b30439d2aa9a11b6625590546ad4538dfd23b0c130620580e6d4e34e2c6ad"},"manifest_sha256":{"bytes":67,"sha256":"c51318a1afe26802f6771f4ddca7b08672f777b929a10de307e796bfebd3a55f"},"original_admission":{"bytes":1719,"sha256":"b8156edca3e6674cb50762b23a13c0333850c29cf6e35b236563850777c7fe6b"},"parameters":{"bytes":950,"sha256":"a500b703beee4032f6f6d6f47988f39146b691d2d34848f166443f38a60f9526"},"preparation_prefix":{"bytes":323,"sha256":"ae009c73b02625046b47309b2e7e39487f2169ab062b72ca302052713d21028e"},"prior_completed_candidate":{"bytes":8977,"sha256":"2e70e03efe8d2275f5365fff52b5a964c912594edd6a156145affafe7146799e"},"problem_id":{"bytes":56,"sha256":"f213b05cb84dcf89ea55e8ccb1e7520713271bac5fae059a6682e1538b1c5c42"},"proved":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"reference_chain":{"bytes":90,"sha256":"17a03aa6671788c510cb926fe507c7686bd0e7610c49dd1e1cf5fd2cb8b684ca"},"reference_mode_prefix":{"bytes":988,"sha256":"842157bf20b74c7df36a3f4c96ca9491e371c12fd2f72d9c4daa3fa6cf597d7b"},"reference_selection":{"bytes":507,"sha256":"6dab06a990a60129c0ebf5a442f935851050dedb6ce7b6655076be29bd9cd7d9"},"retained_completed_five_maxima":{"bytes":2350,"sha256":"407ca196cf8f60ac7c037cd2c2056673e139ecd4c1ecc4343d78a5cbf99a6f74"},"retained_original_false_candidates":{"bytes":1082,"sha256":"af586adb9e63165b204717ac8ace80c2d05285940573a1f7bdc39599b89ae187"},"retained_scope":{"bytes":2282,"sha256":"fcefcfc2e136079f5098c3f324230b5e4ab058798e950c2c6a91a878046d7267"},"run_attempt":{"bytes":4,"sha256":"ee0ce7db9ce2f1d4d2e01f0e96d73fa2399a99d825d8a9898947539a8d8e1742"},"run_id":{"bytes":14,"sha256":"3cc684ee3338fc5f912febed8d3bf18660de96381167897a067c218cf88448ea"},"runtime":{"bytes":101,"sha256":"55c8f0053c75775912f034ed7a12221ac01f5f5439a1e0dc2ad5f6d2aa1e5734"},"saved_copy_counts":{"bytes":198,"sha256":"9e3ccb782b4021c94e0980c37b6255241c4f37dbc89969bf3156f50390e12285"},"saved_record_counts":{"bytes":200,"sha256":"c506a78e9ca9d4a5a32b4ce75adca8332ff1fb533a43d216aaec267bcd5cecd3"},"scientific_modules":{"bytes":1386,"sha256":"c010c61e6964a0803301f9b593a59dfebb50e3c62cc6e871f3e4e5b2acc20e3f"},"stage":{"bytes":11,"sha256":"b4a80c61a1f8c6101403f9f26edc545babd033d6ea52f4cc918a4d8a75d394a4"},"workflow_event_commit":{"bytes":43,"sha256":"68c4ea36f7468efadb57332e1e3b8859a138662f5356d96c05871482dafc81da"}}''')
COMPLETED_TRACE_EXECUTION_FIELD_IDENTITIES=json.loads(r'''{"AST_receipts":{"bytes":3327,"sha256":"8f63179ac52dd50ae5139e4119f62c355cf9c88733f9957408687b7d9d1cbaf6"},"actual_child_returncode":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"actual_scientific_checkout":{"bytes":43,"sha256":"b10480100811bf79025806b82ec7c30723383103e65351c958ab461d02cff1d2"},"all_pulls_match_review":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"child_timeout":{"bytes":6,"sha256":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0"},"child_wall_seconds":{"bytes":14,"sha256":"fc0ca09e688812a34087416225daea2098cdf785ff3336e5cf835c2517164963"},"complete_child_stdout":{"bytes":130,"sha256":"7d00951973682a240b57b0e00c1f0413b3ef856a509bf43223f19e5be2468620"},"completed_old_targets_recomputed":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"completed_target_names":{"bytes":186,"sha256":"709c5e57181e94d5048670fcfbb1536f661ca7d0bef058e8ccbc1951751e8a7b"},"consumed_marker_publication":{"bytes":389,"sha256":"bbb233e08179ef7e8754162555ccb63840d9009cf71d20e25bd357777cf70b4f"},"current_input_receipts":{"bytes":12199,"sha256":"45e8cd94d6b806042732fc206994e293309cb6a007651bbf408e742802b21629"},"entry_checkout":{"bytes":43,"sha256":"68c4ea36f7468efadb57332e1e3b8859a138662f5356d96c05871482dafc81da"},"failure":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"final_capacity_metadata":{"bytes":266,"sha256":"562eeeb9f17b29882cc06c6448938691eafce34dd1032e7c093d7f0291aef640"},"finished_utc":{"bytes":35,"sha256":"fd33869e4d27dcaba3f5081671f15f6bb222e072e1a3e13632ef87ae6871b03a"},"historical_restoration":{"bytes":13771,"sha256":"4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac"},"immediate_pre_science_capacity":{"bytes":266,"sha256":"eaea25065b1bffa998ca77c57cf8e429d083d520d6f5f2aabdadd96df6060c11"},"interrupted_target":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"kind":{"bytes":46,"sha256":"b6d2d89953b4df3f0d089085fa8c5596cafd388f5737725a7c9cd1e10e847ac9"},"manifest_sha256":{"bytes":67,"sha256":"c51318a1afe26802f6771f4ddca7b08672f777b929a10de307e796bfebd3a55f"},"new_Releases":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"new_arrays_published":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"new_artifacts":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"original_scientific_complete_flag":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"original_scientific_failure":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"pre_execution_capacity":{"bytes":266,"sha256":"ea2e87e8bc362b1e275b22af68d828c6f0a510dfbffea824ac74da891da9e026"},"problem_id":{"bytes":56,"sha256":"f213b05cb84dcf89ea55e8ccb1e7520713271bac5fae059a6682e1538b1c5c42"},"publication_attempts":{"bytes":2,"sha256":"4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"},"readme_check_count":{"bytes":2,"sha256":"7de1555df0c2700329e815b93b32c571c3ea54dc967b89e81ab73b9972b72d1d"},"readme_checks":{"bytes":2374,"sha256":"bd358f2413f99f482ce446ab238e1fcfcf2d48049019dca42f35c21e244caef4"},"readme_receipt_chain_sha256":{"bytes":67,"sha256":"4b7b71cf276d9959c65ead53e005b42e06277e3d9879cf55c2787b26d357d356"},"readonly_diagnostic_only":{"bytes":6,"sha256":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0"},"readonly_preflight":{"bytes":2920,"sha256":"c4c510b60c387cba344434bbc36e4a6fd445387e5c347cd945d0c60825611e01"},"repository":{"bytes":33,"sha256":"ea69415f4036ec17f5e16041068cd74ddb1cc3e19aa80963210e2a69ac8da719"},"run_attempt":{"bytes":4,"sha256":"ee0ce7db9ce2f1d4d2e01f0e96d73fa2399a99d825d8a9898947539a8d8e1742"},"run_id":{"bytes":14,"sha256":"3cc684ee3338fc5f912febed8d3bf18660de96381167897a067c218cf88448ea"},"scientific_children":{"bytes":2,"sha256":"4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"},"scientific_complete":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"scientific_files":{"bytes":234,"sha256":"46592265f48c1e55dbe26d04ceaf91979875661a4977d171b0b8592ef2c5d5f7"},"scientific_finished_utc":{"bytes":35,"sha256":"9c87f758cf64191fc7628b57f5612e6aab9b5cc72e4979501b66ff86dcebdc17"},"scientific_started":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"scientific_started_utc":{"bytes":35,"sha256":"721737d4ae0efb00455daa9724db2b313f3013c475024cdf514ff619248d1d1a"},"started_utc":{"bytes":35,"sha256":"da9dec5df6a9a9f84c518ed91ad7f339d3f0d365b30a0ce1bdf3c342ca22b2c5"},"workflow_event_commit":{"bytes":43,"sha256":"68c4ea36f7468efadb57332e1e3b8859a138662f5356d96c05871482dafc81da"}}''')
COMPLETED_TRACE_GATES=json.loads(r'''["all_current_UTF8_files_and_three_fixed_contracts_verified","five_new_and_ten_original_definition_sources_AST_only_verified","all_nineteen_historical_receipts_and_original_native_bytes_verified","complete_original_summary_and_native_projection_identical","both_complete_4650_row_covers_and_3594_interfaces_verified","same_real_family_and_all_original_successes_verified","all_nine_original_literals_and_completed_WHVA_retained","all_five_original_cubic_parts_and_full_shape_verified","original_repair_whole_document_and_all_65_suprema_verified","actual_raw_identity_transmissions_and_full_affine_ports_retained","all_sixty_old_WPS_records_full_false_scope_and_six_prefix_records_verified","fixed_directed_runtime_and_one_new_entry","all_twenty_six_old_records_typed_and_published_tail_bound_retained","entire_frozen_reference_definition_chain_materialized_without_old_bounds","complete_continuous_parent_and_comparison_domains_admitted","complete_reference_receivers_saved","complete_high_trial_source_saved","complete_actual_paired_receivers_saved","complete_local_signed_remainder_saved","complete_endpoint_correction_saved","complete_actual_E_D_T_saved","all_current_inputs_and_manifest_reverified_after_new_work","complete_whole_candidate_shape_and_old_zero_recomputation"]''')
COMPLETED_TRACE_GRAPH_KEYS=json.loads(r'''{"complete_actual_E_D_T":["complete_actual_D_upper","complete_actual_E0_upper","complete_actual_T_upper","complete_actual_finite_defect_upper"],"complete_actual_paired_receivers":["complete_actual_paired_LH_upper","complete_actual_tail_LH_upper","complete_centre_paired_LH_column_upper","complete_centre_paired_LH_norm_upper","complete_centre_paired_LH_row_upper","complete_centre_tail_LH_column_upper","complete_centre_tail_LH_norm_upper","complete_centre_tail_LH_row_upper","complete_difference_paired_LH_column_upper","complete_difference_paired_LH_norm_upper","complete_difference_paired_LH_row_upper","complete_difference_tail_LH_upper","complete_head_paired_error_upper","complete_low_generator_difference_column_upper","complete_low_generator_difference_norm_upper","complete_low_generator_difference_row_upper","complete_low_generator_tail_error_upper","complete_outer_paired_error_upper","complete_raw_difference_LH_receiver_column_upper","complete_raw_difference_LH_receiver_norm_upper","complete_raw_difference_LH_receiver_row_upper","complete_raw_difference_tail_LH_upper"],"complete_endpoint_correction":["complete_head_endpoint_correction_upper","complete_high_trace_endpoint_receiver_upper","complete_outer_endpoint_correction_upper"],"complete_high_trial_source":["complete_body_ordinary_source_upper","complete_family_high_kernel_column_upper","complete_family_high_kernel_norm_upper","complete_family_high_kernel_row_upper","complete_high_outer_trace_error_upper","complete_high_state_error_upper","complete_repaired_centre_body_residual_column_upper","complete_repaired_centre_body_residual_norm_upper","complete_repaired_centre_body_residual_row_upper","complete_trial_raw_column_upper","complete_trial_raw_norm_upper","complete_trial_raw_row_upper"],"complete_local_signed_remainder":["complete_actual_head_tail_source_upper","complete_actual_outer_tail_source_upper","complete_signed_centre_paired_source_column_upper","complete_signed_centre_paired_source_norm_upper","complete_signed_centre_paired_source_row_upper","complete_signed_centre_tail_source_column_upper","complete_signed_centre_tail_source_norm_upper","complete_signed_centre_tail_source_row_upper"],"complete_reference_receivers":["complete_reference_column_ratio_upper","complete_reference_inverse_norm_upper","complete_reference_odd_endpoint_receiver_upper","complete_reference_rho_column_ratio_upper","complete_reference_rho_defect_upper","complete_reference_rho_row_ratio_upper","complete_reference_row_ratio_upper"]}''')
COMPLETED_TRACE_COPY_PATHS=json.loads(r'''{"complete_actual_outer_tail_source_upper":["complete_new_graphs","complete_local_signed_remainder","new_records","complete_actual_outer_tail_source_upper"],"complete_actual_tail_LH_upper":["complete_new_graphs","complete_actual_paired_receivers","new_records","complete_actual_tail_LH_upper"],"complete_body_ordinary_source_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_body_ordinary_source_upper"],"complete_centre_tail_LH_column_upper":["complete_new_graphs","complete_actual_paired_receivers","new_records","complete_centre_tail_LH_column_upper"],"complete_centre_tail_LH_norm_upper":["complete_new_graphs","complete_actual_paired_receivers","new_records","complete_centre_tail_LH_norm_upper"],"complete_centre_tail_LH_row_upper":["complete_new_graphs","complete_actual_paired_receivers","new_records","complete_centre_tail_LH_row_upper"],"complete_difference_tail_LH_upper":["complete_new_graphs","complete_actual_paired_receivers","new_records","complete_difference_tail_LH_upper"],"complete_family_high_kernel_column_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_family_high_kernel_column_upper"],"complete_family_high_kernel_norm_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_family_high_kernel_norm_upper"],"complete_family_high_kernel_row_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_family_high_kernel_row_upper"],"complete_high_outer_trace_error_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_high_outer_trace_error_upper"],"complete_high_state_error_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_high_state_error_upper"],"complete_low_generator_tail_error_upper":["complete_new_graphs","complete_actual_paired_receivers","new_records","complete_low_generator_tail_error_upper"],"complete_raw_difference_tail_LH_upper":["complete_new_graphs","complete_actual_paired_receivers","new_records","complete_raw_difference_tail_LH_upper"],"complete_repaired_centre_body_residual_column_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_repaired_centre_body_residual_column_upper"],"complete_repaired_centre_body_residual_norm_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_repaired_centre_body_residual_norm_upper"],"complete_repaired_centre_body_residual_row_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_repaired_centre_body_residual_row_upper"],"complete_trial_raw_column_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_trial_raw_column_upper"],"complete_trial_raw_norm_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_trial_raw_norm_upper"],"complete_trial_raw_row_upper":["complete_new_graphs","complete_high_trial_source","new_records","complete_trial_raw_row_upper"]}''')

def admit_completed_tracefree_inputs(admitted,texts,by_role):
 """All 56 completed WVC records and every original field remain read-only.

 The full current actual/manifest/execution bytes are verified independently.
 Whole-file bindings preserve every prior qualification; the projections below
 contain exactly the literal records needed by the new complete candidate.
 No original numeric producer is imported or called.
 """
 for role,spec in COMPLETED_TRACE_PINS.items():
  require(by_role.get(role)==spec,"fixed complete previous WVC/proof object "+role)
 prior=data(texts["WVC_actual"]);execution=data(texts["WVC_execution"])
 old_manifest=data(texts["WVC_manifest"])
 for value,identities,label in (
    (prior,COMPLETED_TRACE_FIELD_IDENTITIES,"complete previous WVC science"),
    (execution,COMPLETED_TRACE_EXECUTION_FIELD_IDENTITIES,"complete previous WVC execution")):
  require(set(value)==set(identities),label+" field set")
  for key,expected in identities.items():
   raw=canonical(value[key])
   require(len(raw)==expected["bytes"] and digest(raw)==expected["sha256"],
           label+" entire original field "+key)
 require(prior["kind"]=="complete_continuous_centre_tracefree_candidate_v1"
         and prior["problem_id"]=="WVC_complete_continuous_centre_tracefree_candidate_v1"
         and prior["complete"] is True and prior["proved"] is True
         and prior["stage"]=="complete" and prior["failure"] is None
         and prior["actual_returncode"]==0 and prior["current_target"] is None
         and prior["automatic_retry_authorized"] is False,
         "original completed WVC candidate, no altered failure classification")
 require(prior["gates"]==[{"name":name,"passed":True} for name in COMPLETED_TRACE_GATES]
         and len(prior["gates"])==23,"all original WVC structural gates")
 require(set(prior["complete_new_graphs"])==set(COMPLETED_TRACE_GRAPH_KEYS)
         and len(prior["completed_targets"])==6
         and set(prior["completed_targets"])==set(COMPLETED_TRACE_GRAPH_KEYS),
         "all six complete WVC graphs in original order")
 count=0
 for name,keys in COMPLETED_TRACE_GRAPH_KEYS.items():
  graph=prior["complete_new_graphs"][name]
  require(set(graph)=={"complete","new_records","copied_records"}
          and graph["complete"] is True and graph["copied_records"]=={}
          and set(graph["new_records"])==set(keys)
          and prior["saved_record_counts"][name]==len(keys)
          and prior["saved_copy_counts"][name]==0,
          "complete original WVC graph shape "+name)
  for key in keys:
   record_value=graph["new_records"][key]
   require(isinstance(record_value,dict) and set(record_value)=={"ball"},
           "exact original WVC scalar object "+name+"/"+key)
   finite_display_tokens(record_value["ball"],"original WVC/"+name+"/"+key)
   count+=1
 require(count==prior["actual_progress"]["new_scalar_records_saved"]==56,
         "all fifty-six completed original WVC bounds")
 prefix=prior["reference_mode_prefix"]
 require(set(prefix)=={"completed_modes","running","witnesses","status"}
         and prefix["completed_modes"]==96 and len(prefix["running"])==5
         and set(prefix["running"])==set(prefix["witnesses"])
         and prefix["status"]=={"changed_modes_completed":96,"unchanged_modes_qualified":0,
                               "all_reference_targets_copied":False},
         "original five complete modal maxima and full changed-mode qualification")
 for key,value in prefix["running"].items():
  require(set(value)=={"ball"},"original complete WVC modal record")
  finite_display_tokens(value["ball"],"original WVC modal prefix/"+key)
  witness=prefix["witnesses"][key]
  require(set(witness)=={"origin","mode"} and witness["origin"]=="new_changed_mode"
          and type(witness["mode"]) is int and 1<=witness["mode"]<=96,
          "full original WVC witness")
 require(prior["reference_selection"]["complete"] is True
         and prior["reference_selection"]["changed_mode_indices"]==list(range(1,97))
         and prior["reference_selection"]["unchanged_mode_indices"]==[]
         and prior["reference_selection"]["same_actual_spaces_and_projection"] is True,
         "actual completed WVC selected reference identity")
 require(prior["finite_gate"]["passed"] is False
         and prior["finite_gate"]["actual_tail_inverse_upper"]==3
         and prior["finite_gate"]["actual_tail_gate_is_published_analytic_m160"] is True
         and prior["finite_gate"]["complete_defect_record"]==
           prior["complete_new_graphs"]["complete_actual_E_D_T"]["new_records"][
              "complete_actual_finite_defect_upper"]
         and prior["conditional_finite_inverse"] is None,
         "original complete finite sufficient gate remains false")
 progress=prior["actual_progress"]
 require(progress["original_body_intersections"]==4801
         and progress["original_closed_rows_covered"]==4650
         and progress["completed_new_body_parent_packets"]==152
         and progress["comparison_cells"]==155 and progress["refined_cells"]==24480
         and progress["new_reference_modes_computed"]==progress["reference_modes_completed"]==96
         and progress["unchanged_reference_modes_read"]==0
         and all(progress[key]==0 for key in (
           "old_targets_recomputed","old_producer_imports_or_calls",
           "old_reference_bounds_reevaluated","dense_finite_matrices_allocated",
           "new_array_artifacts_published","physical_state_columns_computed",
           "conditional_finite_inverses","graph_old_records_copied")),
         "complete old WVC domain and zero recomputation/lost boundary")
 require(old_manifest["kind"]=="complete_continuous_centre_tracefree_current_inputs_v1"
         and old_manifest["problem_id"]==prior["problem_id"]
         and old_manifest["expected_current_input_count"]==41
         and len(old_manifest["files"])==41
         and old_manifest["parameters"]==prior["parameters"]
         and old_manifest["retained_scope"]==prior["retained_scope"]
         and old_manifest["scientific_modules"]==prior["scientific_modules"]
         and digest(texts["WVC_manifest"].encode())==prior["manifest_sha256"]
             ==execution["manifest_sha256"],
         "complete original WVC source/manifest identity")
 old_by_role={s["role"]:s for s in old_manifest["files"]}
 require(len(old_by_role)==41 and prior["complete_current_file_receipts"]==old_manifest["files"]
         and execution["current_input_receipts"]==old_manifest["files"]
         and prior["input_sha256"]=={k:s["sha256"] for k,s in old_by_role.items()},
         "all forty-one original whole-file receipts")
 replaced={"science","readonly_admission","kernel_math","assembly_math","reference_math","worker","rules"}
 for role,spec in old_by_role.items():
  if role not in replaced:
   require(by_role[role]==spec,"same complete WVC coefficient/proof input "+role)
 require(old_manifest["core_current_files"]==admitted["manifest"]["core_current_files"]
         and old_manifest["historical_inputs"]==admitted["manifest"]["historical_inputs"]
         and len(execution["AST_receipts"])==16,
         "unchanged full core and nineteen historical objects")
 for item in execution["AST_receipts"]:
  require(set(item)=={"path","role","sha256"} and item["role"] in old_by_role
          and item["path"]==old_by_role[item["role"]]["path"]
          and item["sha256"]==old_by_role[item["role"]]["sha256"],
          "original WVC full AST identity")
 require(execution["scientific_children"]==1 and execution["scientific_started"] is True
         and execution["scientific_complete"] is True and execution["actual_child_returncode"]==0
         and execution["failure"] is None and execution["interrupted_target"] is None
         and execution["original_scientific_failure"] is None
         and execution["original_scientific_complete_flag"] is True
         and execution["completed_old_targets_recomputed"]==0
         and execution["new_artifacts"]==execution["new_arrays_published"]==execution["new_Releases"]==0,
         "complete original WVC scientific execution")
 for key in ("run_id","run_attempt","workflow_event_commit"):
  require(execution[key]==prior[key],"original WVC execution/science "+key)
 require(execution["actual_scientific_checkout"]==prior["actual_checkout_commit"]
         and execution["scientific_files"]==[{
             k:by_role["WVC_actual"][k] for k in ("path","bytes","sha256")}],
         "complete actual WVC scientific file")
 preflight=execution["readonly_preflight"]
 require(preflight["returncode"]==0 and preflight["stderr_bytes"]==0
         and preflight["complete_output"]["complete"] is True
         and preflight["complete_output"]["flint_imported"] is False
         and preflight["complete_output"]["admission"]==prior["original_admission"],
         "entire original WVC successful readonly boundary")
 raw=canonical(preflight["complete_output"])
 require(len(raw)==preflight["stdout_bytes"] and digest(raw)==preflight["stdout_sha256"],
         "whole original WVC preflight bytes")
 paired=admitted["paired_inputs"]
 for key,current in (
    ("copied_original_records",paired["records"]),
    ("copied_original_scope",paired["scope"]),
    ("copied_complete_candidate_metadata",admitted["candidate_metadata"]),
    ("copied_complete_repair_definition",admitted["repair_definition"]),
    ("retained_completed_five_maxima",paired["completed_five_maxima"]),
    ("retained_original_false_candidates",paired["old_false_candidates"]),
    ("reference_chain",paired["reference_chain"]),
    ("prior_completed_candidate",admitted["completed_paired_inputs"]["archive"])):
  require(prior[key]==current,"full original WVC qualification "+key)
 require(prior["complete_restoration_receipts"]==execution["historical_restoration"]
         and digest(canonical(prior["complete_restoration_receipts"]))==
             admitted["admission"]["restoration_receipts_sha256"],
         "entire unchanged original restoration")
 comparable=dict(admitted["admission"]);comparable["current_file_count"]=41
 require(comparable==prior["original_admission"],
         "same full WVC admission before the additional completed-WVC check")
 copied={key:at(prior,path) for key,path in COMPLETED_TRACE_COPY_PATHS.items()}
 require(len(copied)==20 and len(canonical(copied))==2875
         and digest(canonical(copied))==
             "4a32dc9dcb5b3e6abf72eaf66cc74baa30bfa8bf309dfe2ac97d9ee3086995b6",
         "all twelve high, seven unchanged-tail and one outer-tail literal records")
 reference=prior["complete_new_graphs"]["complete_reference_receivers"]["new_records"]
 old_paired=admitted["completed_paired_inputs"]
 mean_record=old_paired["reference_records"]["complete_reference_mean_endpoint_receiver_upper"]
 family_record=old_paired["family_HL_record"]
 archive={
  "complete_original_scientific_file":by_role["WVC_actual"],
  "complete_original_execution_file":by_role["WVC_execution"],
  "complete_original_manifest_file":by_role["WVC_manifest"],
  "complete_original_field_verification":{
   "scientific_field_count":43,"execution_field_count":44,
   "scientific_identity_table_sha256":digest(canonical(COMPLETED_TRACE_FIELD_IDENTITIES)),
   "execution_identity_table_sha256":digest(canonical(COMPLETED_TRACE_EXECUTION_FIELD_IDENTITIES)),
   "full_tables_are_in_the_current_pinned_readonly_module":True,
   "all_original_fields_verified_before_science":True},
  "complete_original_parameters":prior["parameters"],
  "complete_original_retained_scope":prior["retained_scope"],
  "complete_original_actual_progress":prior["actual_progress"],
  "complete_original_finite_gate":prior["finite_gate"],
  "complete_original_reference_mode_prefix":prefix,
  "complete_original_reference_selection":prior["reference_selection"],
  "complete_original_reference_graph":prior["complete_new_graphs"]["complete_reference_receivers"],
  "complete_twenty_copied_record_objects":copied,
  "complete_original_mean_reference_record":mean_record,
  "complete_original_family_HL_record":family_record,
  "complete_original_scientific_modules":prior["scientific_modules"],
  "complete_original_completion":{k:prior[k] for k in (
      "complete","proved","stage","failure","actual_returncode","automatic_retry_authorized")},
  "complete_original_graphs_identity":{
   "bytes":len(canonical(prior["complete_new_graphs"])),
   "sha256":digest(canonical(prior["complete_new_graphs"]))},
  "complete_prior_WPS_archive_identity":{
   "bytes":len(canonical(prior["prior_completed_candidate"])),
   "sha256":digest(canonical(prior["prior_completed_candidate"])),
   "whole_archive_is_in_the_original_WVC_file_and_was_independently_reconstructed":True},
  "all_fifty_six_records_and_five_modal_prefixes_read_without_reevaluation":True,
  "full_previous_WPS_and_WPTVS_scopes_remain_in_the_complete_original_files":True,
  "all_original_complete_objects_bound_by_full_file_and_field_identity":True,
  "no_original_success_or_false_sufficient_gate_reclassified":True}
 return {"archive":archive,"reference_records":reference,"mean_reference_record":mean_record,
         "family_HL_record":family_record,"copied_records":copied,
         "selected_diagonal_chain":prior["reference_selection"]["selected_diagonal_chain"],
         "complete_original_candidate":prior,
         "old_completed_record_count":56,"old_prefix_record_count":5}
