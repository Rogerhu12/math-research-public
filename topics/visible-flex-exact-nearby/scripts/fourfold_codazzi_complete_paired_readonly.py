"""WPS full typed readonly admission; no flint, numpy, or producer execution."""
from __future__ import annotations
import ast, gzip, hashlib, io, json, os, re, struct, zipfile
from bisect import bisect_right
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby/"
REPOSITORY="Rogerhu12/math-research-public"
MANIFEST_KIND="complete_paired_finite_residual_current_inputs_v1"
PROBLEM_ID="WPS_complete_paired_finite_residual_v1"
PARAMETERS=json.loads(r'''{"bits":320,"decimal_record_digits":75,"parent_band_subcells":8,"maximum_doubling_bands":20,"parent_cells":153,"uniform_refinement":160,"refined_cells":24480,"maximum_comparison_cells":155,"reference_q_floor":"1/8","reference_q_binary_places":20,"head_dimension":193,"first_high_index":97,"physical_high_minimum":388,"reference_centre_degree":32,"actual_delta_degree":96,"high_trial_last_index":160,"repaired_centre_residual_last_index":224,"complete_family_residual_last_index":352,"cutoff_width":"1/16","reference_outer_impedance":"13/80","actual_tail_inverse_bound":3,"new_array_artifacts":false,"old_targets_recomputed":0}''')
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
 require(len(specs)==manifest["expected_current_input_count"]==36
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
