#!/usr/bin/env python3
"""Request180: change only the accurate R323 coast's three coefficients.

Rebuild the original accurate model from the actual165 original recipe, complete
cut enclosures and historical accepted core. Certify the other418 exact pieces
once. Try a finite explicit descending dyadic coast homotopy, including zero.
This is a new parameter selection in the SAME accurate nine-control family,
not an accepted field, a numerical-reference certificate or a new BVP gate.
All interval/polynomial/scalar arithmetic is public Actions only.
"""
from __future__ import annotations
import argparse, copy, gzip, hashlib, importlib.util, json, math, os, signal, struct, sys, time, traceback
from fractions import Fraction as Q
from pathlib import Path

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="request180-accurate-R323-coast-three-coefficient-repair-v1"
FACTORY="geometry_20261115_continuous_nine_scalar_factory_v3.py"
FACTORY_SHA="0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e"
CORE="geometry_20261114_full_prefix_operator.py"
CORE_SHA="a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703"
PARAMETERS=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3"]
COAST=[2,5,8]
ORIGINAL_RUN="43736208020"
ORIGINAL_COMMIT="1f2ec637430e5c6b27b1a93720e106539281a156"
MEMBERS={
 "input":("original-input-binding.json",62398,"996593f3a615c3694596463c949990a4967cc5c5a1bf48b100fbc4e149e73e48"),
 "target":("original-target-result.json",105512,"e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619"),
 "construction":("original-construction-summary.json",27207,"6ff7fb33455be8dbc4eef1eb819a8f7b90329c8575c442dc810c83db13117fb8")
}
POLICY=dict(sqrt_bits=256,maximum_seconds=900,unchanged_piece_seconds=300,
 unchanged_piece_max_nodes=65536,coast_per_candidate_max_nodes=8192,
 maximum_depth=28,largest_halving_exponent=16,include_explicit_zero_candidate=True,
 summary_enclosure_grid_bits=128,
 choose_first_whole_accurate_domain_proved_candidate=True,
 whole_original_parameter_radius_and_native_thresholds_not_changed=True)

def require(ok,message):
 if not ok:raise ValueError(message)

def canonical(value):
 return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode("utf-8")

def sha(raw):return hashlib.sha256(raw).hexdigest()

def receipt(path):
 raw=Path(path).read_bytes();return dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))

def checked(path,size,digest):
 raw=Path(path).read_bytes();require(len(raw)==size and sha(raw)==digest,"Bound original member: "+str(path))
 return json.loads(raw),dict(file=Path(path).name,bytes=size,sha256=digest)

def write(path,value):
 raw=canonical(value);Path(path).write_bytes(raw)
 return dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))

def same(a,b,label):
 require(canonical(a)==canonical(b),"Unchanged actual identity: "+label)

def load_module(directory,name,digest,label):
 path=directory/name;require(sha(path.read_bytes())==digest,"Bound source "+name)
 spec=importlib.util.spec_from_file_location(label,path);module=importlib.util.module_from_spec(spec)
 sys.modules[label]=module;spec.loader.exec_module(module);return module

class ResourceStop(RuntimeError):pass

class Clock:
 def __init__(self,seconds):
  self.start=time.monotonic();self.deadline=self.start+seconds
 def check(self):
  if time.monotonic()>=self.deadline:raise ResourceStop("whole-science-wall-budget")

def rebuild(args,request,clock):
 clock.check()
 recovery=json.loads((args.restored_directory/"recovery-result.json").read_bytes())
 require(recovery.get("complete") is True and recovery.get("error") is None,"Complete original log recovery, not substitute data")
 data={};original={}
 for role,(name,size,digest) in MEMBERS.items():
  data[role],original[role]=checked(args.restored_directory/name,size,digest)
 binding,construction,target=data["input"],data["construction"],data["target"]
 for name,value in data.items():
  require(str(value.get("run_id"))==ORIGINAL_RUN and value.get("source_commit")==ORIGINAL_COMMIT,"Actual165 producer run/source: "+name)
 require(binding["actual_request"]["sha256"]==request["original165_request"]["sha256"],"Actual165 request binding")
 require(target.get("source",{}).get("sha256")=="61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205","Original target producer")
 require(target["input_binding"]["sha256"]==original["input"]["sha256"],"Original target consumes complete original input")
 require(construction["source"]["sha256"]=="738dd352cf62fbd47eb80e867ac441b7d0c179074cbee93fb8dd6528ba0d4cb0","Original construction producer")
 factory=load_module(args.code_directory,FACTORY,FACTORY_SHA,"_r180_frozen_factory")
 kernel,core_source=factory.load_core_kernel(args.code_directory)
 core_item=request["inputs"]["accepted_core"];core_raw=args.accepted_core.read_bytes()
 require(len(core_raw)==core_item["bytes"] and sha(core_raw)==core_item["sha256"],"Whole original accepted M96 core")
 accepted=json.loads(gzip.decompress(core_raw) if core_raw.startswith(b"\x1f\x8b") else core_raw)
 require(accepted.get("success") is True and accepted.get("M")==96,"Original accepted core")
 geometry=factory.pointer(accepted,"/fixed_scalar_profile/geometry")
 require(factory.sha(factory.canonical(geometry))==binding["actual_core_input"]["selected_geometry_canonical_sha256"],"Full selected original geometry identity")
 require(binding["actual_core_input"]["sha256"]==core_item["sha256"],"Original geometry consumes same core bytes")
 same(core_source,binding["actual_core_input"]["original_exact_shared_jet_source"],"Exact shared core constructor")
 config_item=request["inputs"]["config"];config_raw=args.config.read_bytes()
 require(len(config_raw)==config_item["bytes"] and sha(config_raw)==config_item["sha256"],"Complete original T112 config")
 config=json.loads(config_raw);require(config["modes"]==112 and config["quadrature"]==2048,"Original full112 target configuration")
 same({k:binding["actual_config"][k] for k in ("bytes","sha256")},
      {k:config_item[k] for k in ("bytes","sha256")},"Actual original config")
 recipe=copy.deepcopy(construction["actual_recipe"]);recipe_raw=factory.canonical(recipe)
 require(len(recipe_raw)==binding["actual_recipe"]["bytes"] and sha(recipe_raw)==binding["actual_recipe"]["sha256"],"Whole original R323 recipe")
 require(sha(recipe_raw)==construction["actual_recipe_file"]["sha256"],"Constructor's actual recipe identity")
 require(recipe["parameter_order"]==PARAMETERS and len(recipe["nine_parameters"])==9,"All actual nine parameters")
 same(recipe["nine_parameters"],request["initial_nine_parameters"],"Same actual146 numerical input words as165, not actual157")
 params=[factory.rational(x) for x in recipe["nine_parameters"]]
 same([str(x) for x in params],binding["complete_nine_parameters_as_exact_dyadics"],"Exact lift of all original nine words")
 same([struct.pack("<d",float(x)).hex() for x in recipe["nine_parameters"]],
      binding["complete_nine_parameter_words"],"Original parameter binary64 words")
 cut=factory.rational(recipe["cut_radius"])
 require(cut==Q.from_float(float(config["rCut"])),"Original cut not renormalized")
 require(factory.rational(recipe["core_end"])==Q.from_float(float(accepted["mesh"][-1])),"Original accepted core endpoint")
 tail=binding["original_tail_binding"]
 require(tail["source_sha256"]=="f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
  and tail["preserved_unit_panel_source_sha256"]=="004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea"
  and tail["preserved_original_source_sha256"]=="9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed","Same continuous-C producer family")
 require(tail["original_producer_encloses_every_admissible_root_sequence"] is True
  and tail["coefficient_midpoints_substituted"] is False
  and tail["original_error"] is None,"Complete semantic root-family cut input")
 require(tail["actual_input_binding"]["convention"]["deep_definition"]=="original-exact-root-family","Actual accurate C definition")
 require(factory.rational(tail["original_binary_cut"]["exact_rational"])==cut,"Same complete binary cut")
 leaves={key:factory.ball_record(tail["actual_cut_twojet_enclosures"][old])
  for key,old in (("E0","E"),("E1","E_r"),("E2","E_rr"))}
 model=factory.build_expression(kernel,geometry,recipe,leaves,cut)
 values=model["tree"].evaluate(leaves,POLICY["sqrt_bits"])
 conditions=factory.construction_conditions(model,values)
 original_factory=construction["original_factory_result"]
 same(conditions,original_factory["construction_conditions"],"All original exact construction conditions")
 require(conditions["all_strict_conditions_proved"],"Original structural construction premises")
 rebuilt=factory.definition(model,tail,binding["actual_core_input"],binding["actual_recipe"])
 rebuilt.update(construction_conditions=conditions,
  published_structural_and_effective_scope_proof=original_factory["published_R300_proof"],
  given_finite_enclosure_is_not_an_effective_real_name=True,automatic_width_search_performed=False,
  actual_enclosure_leaves={k:v.record() for k,v in leaves.items()},
  base_complete_domain=original_factory["base_domain"])
 field_rows=binding["all_definition_fields_rebuilt_and_exactly_compared"]
 require(len({r["field"] for r in field_rows})==len(field_rows) and set(rebuilt)=={r["field"] for r in field_rows},"Every original definition field is reconstructed")
 comparisons=[]
 for row in field_rows:
  digest=sha(factory.canonical(rebuilt[row["field"]]))
  require(row["exactly_equal"] is True and digest==row["canonical_sha256"],"Original definition field "+row["field"])
  comparisons.append(dict(field=row["field"],sha256=digest,exactly_same=True))
 full=factory.canonical(rebuilt)
 require(len(full)==binding["actual_definition"]["bytes"] and sha(full)==binding["actual_definition"]["sha256"],"Whole original accurate definition exactly rebuilt, not fabricated from its SHA")
 require(len(model["pieces"])==419 and [p["name"] for p in model["pieces"][-4:]]==[
  "first-velocity-transition","negative-speed-coast","last-velocity-transition","canonical-cubic-cut-collar"],"Original complete419 accurate piece order")
 source_rows=[]
 for item in binding["complete_scientific_sources"]:
  name=item["file"];require(Path(name).name==name,"Original source basename")
  raw=(args.code_directory/name).read_bytes()
  require(len(raw)==item["bytes"] and sha(raw)==item["sha256"]==request["original_source_sha256"][name],"Original scientific source closure: "+name)
  source_rows.append(dict(file=name,bytes=len(raw),sha256=sha(raw),executed_here=name in (FACTORY,CORE)))
 require(len(source_rows)==len(request["original_source_sha256"])==21,"Complete original source identity set")
 return factory,model,values,rebuilt,dict(original_members=original,
  official_log_recovery=receipt(args.restored_directory/"recovery-result.json"),
  original_complete_log=recovery["original_stream"],original_definition=binding["actual_definition"],
  all_rebuilt_definition_fields=comparisons,original_sources=source_rows,
  actual_original_core=dict(bytes=len(core_raw),sha256=sha(core_raw)),
  actual_original_config=dict(bytes=len(config_raw),sha256=sha(config_raw)),
  complete_original_cut_enclosures=tail["actual_cut_twojet_enclosures"],
  original_semantic_C=dict(source_sha256=tail["source_sha256"],
   model_schema=tail["actual_input_binding"]["convention"]["schema"],
   deep_definition=tail["actual_input_binding"]["convention"]["deep_definition"],
   all_admissible_original_root_sequences_retained=True),
  reconstruction_reuses_original_enclosure_evidence_not_a_new_C_solve=True)

def add(a,b,Box):
 n=max(len(a),len(b));return [(a[i] if i<len(a) else Box(0))+(b[i] if i<len(b) else Box(0)) for i in range(n)]

def affine(coefficients,offset,scale,Box):
 out=[Box(0) for _ in coefficients]
 for k,c in enumerate(coefficients):
  for j in range(k+1):out[j]=out[j]+c*math.comb(k,j)*(offset**(k-j))*(scale**j)
 return out

def derivative(c):
 return [j*c[j] for j in range(1,len(c))] if len(c)>1 else [c[0]*0]

def jets(c,width):
 first=derivative(c);second=derivative(first)
 return [c,[x/width for x in first],[x/(width*width) for x in second]]

def bernstein(c,lo,hi,Box):
 restricted=affine(c,Q(lo),Q(hi)-Q(lo),Box);n=len(restricted)-1
 b=[]
 for j in range(n+1):
  value=Box(0)
  for k in range(j+1):value=value+restricted[k]*Q(math.comb(j,k),math.comb(n,k))
  b.append(value)
 return Box(min(x.lo for x in b),max(x.hi for x in b))

def poly(c,t,Box):
 value=Box(0)
 for x in reversed(c):value=value*t+x
 return value

def exact(box,label):
 require(box.lo==box.hi,"Literal rational coefficient expected: "+label);return box.lo

def group(model,factory,support,beta=Q(1)):
 result=[Q(0)]*9
 for order in range(3):
  p=model["parameters"][3*order+support]*(beta if support==2 else 1)
  for j,c in enumerate(factory.bump_polynomial(order)):result[j]+=p*c
 return result

def coast_jets(factory,model,values,beta):
 B=factory.Box;r=model["roots"];k=model["explicit_lengths"][0]
 RA=values[r["RA"]];IA=values[r["IA"]];w=values[r["coast_length"]]
 require(w.lo>0,"Accurate coast width remains positive")
 g=group(model,factory,2,beta);dg=derivative(g);ddg=derivative(dg)
 # Accurate calibration is used only for the accurate target, not numeric words.
 radius=add([RA+IA,-k*w],[w*w*c for c in g],B)
 speed=add([B(-k)],[w*c for c in dg],B)
 acceleration=[B(c) for c in ddg]
 return [radius,speed,acceleration]

def fixed_segments(factory,model,values):
 B=factory.Box;segments=[]
 for index,piece in enumerate(model["pieces"]):
  if index==416:continue
  c=[values[i] for i in piece["coefficients"]]
  a=values[piece["anchor"]];w=values[piece["width"]]
  require(w.lo>0,"Every accurate piece has positive width")
  lo,hi=map(Q,piece["local_interval"])
  cuts=[lo,hi]
  if piece["name"].startswith("core-"):
   aq=exact(a,"core anchor");wq=exact(w,"core width")
   support=model["supports"][0]
   left=exact(values[support["left"]],"core support left")
   width=exact(values[support["width"]],"core support width")
   for boundary in (left,left+width):
    t=(boundary-aq)/wq
    if lo<t<hi:cuts.append(t)
   cuts=sorted(set(cuts));g=group(model,factory,0)
   for first,last in zip(cuts[:-1],cuts[1:]):
    physical=aq+wq*(first+last)/2
    radius=list(c)
    inside=left<physical<left+width
    if inside:
     controls=affine([B(x*width*width) for x in g],(aq-left)/width,wq/width,B)
     radius=add(radius,controls,B)
    segments.append(dict(piece=index,name=piece["name"],lo=first,hi=last,jets=jets(radius,wq),
     control_support=0 if inside else None))
  elif piece["name"]=="first-velocity-transition":
   require(index==415,"Actual first transition index")
   width=exact(w,"fixed first transition width")
   support=model["supports"][1]
   require(a.lo==a.hi==values[support["left"]].lo==values[support["left"]].hi
    and width==values[support["width"]].lo==values[support["width"]].hi,"Same true support1 and transition")
   radius=add(c,[B(x*width*width) for x in group(model,factory,1)],B)
   segments.append(dict(piece=index,name=piece["name"],lo=lo,hi=hi,jets=jets(radius,width),control_support=1))
  else:
   require(index in (417,418) and piece["name"] in ("last-velocity-transition","canonical-cubic-cut-collar"),"All accurate fixed pieces accounted")
   # Supports0/1/2 are disjoint except zero-two-jet endpoints. No control is
   # silently evaluated on a different coordinate or carried into this piece.
   width=exact(w,"fixed last/collar width")
   segments.append(dict(piece=index,name=piece["name"],lo=lo,hi=hi,jets=jets(c,width),control_support=None))
 require({x["piece"] for x in segments}==set(range(419))-{416},"All418 fixed accurate pieces")
 return segments

class DomainWork:
 def __init__(self,factory,clock,deadline,max_nodes,depth,ledger):
  self.factory=factory;self.clock=clock;self.deadline=deadline
  self.max_nodes=max_nodes;self.depth=depth;self.ledger=ledger
  self.count=0;self.h=hashlib.sha256();self.bytes=0;self.leaves=0
 def check(self):
  self.clock.check()
  if time.monotonic()>=self.deadline:raise ResourceStop("local-domain-wall-budget")
  if self.count>=self.max_nodes:raise ResourceStop("local-domain-node-budget")
 def append(self,value):
  raw=canonical(value);self.ledger.write(raw);self.h.update(raw);self.bytes+=len(raw);self.leaves+=1
 def prove(self,segments,stop_on_strict_refutation=False):
  stack=[(seg,seg["lo"],seg["hi"],0) for seg in reversed(segments)]
  paid=0;unresolved=[];refuted=[];minimum=None;speed_lo=None;speed_hi=None
  by_piece={x["piece"]:dict(piece=x["piece"],name=x["name"],proved_leaves=0,unresolved_leaves=0,
             refuted_leaves=0,unvisited_intervals=0,visited_nodes=0) for x in segments}
  reason=None;unvisited=[];active=None;error=None
  try:
   while stack:
    self.check();seg,lo,hi,depth=stack.pop();active=(seg,lo,hi,depth);self.count+=1
    row=by_piece[seg["piece"]];row["visited_nodes"]+=1
    enclosed=[bernstein(c,lo,hi,self.factory.Box) for c in seg["jets"]]
    a,v,aa=enclosed
    ok=a.lo>0 and -1<v.lo and v.hi<1
    invalid=a.hi<=0 or v.lo>=1 or v.hi<=-1
    if not ok and not invalid and depth<self.depth:
     mid=(lo+hi)/2
     stack.append((seg,mid,hi,depth+1));stack.append((seg,lo,mid,depth+1));active=None;continue
    record=dict(piece=seg["piece"],name=seg["name"],closed_piece_coordinate=[str(lo),str(hi)],
     depth=depth,a_ap_app=[x.record() for x in enclosed],proved=ok,
     rigorous_radius_refutation=a.hi<=0,rigorous_speed_refutation=v.lo>=1 or v.hi<=-1,
     all_coefficient_Bernstein=True)
    self.append(record);active=None
    minimum=a.lo if minimum is None else min(minimum,a.lo)
    speed_lo=v.lo if speed_lo is None else min(speed_lo,v.lo)
    speed_hi=v.hi if speed_hi is None else max(speed_hi,v.hi)
    if ok:paid+=1;row["proved_leaves"]+=1
    elif invalid:
     refuted.append(small_leaf(record));row["refuted_leaves"]+=1
     if stop_on_strict_refutation:reason="stopped-after-one-sufficient-rigorous-coast-refutation";break
    else:unresolved.append(small_leaf(record));row["unresolved_leaves"]+=1
  except ResourceStop as exc:
   reason=str(exc)
   if active is not None:stack.append(active)
  except BaseException as exc:
   reason="original-domain-arithmetic-or-program-exception"
   error=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
   if active is not None:stack.append(active)
  for seg,lo,hi,depth in reversed(stack):
   by_piece[seg["piece"]]["unvisited_intervals"]+=1
   unvisited.append(dict(piece=seg["piece"],closed_piece_coordinate=[str(lo),str(hi)],depth=depth))
  complete=not stack and not unresolved and not refuted and error is None
  return dict(complete=complete,error=error,all_closed_segments_visited=not stack,proved_leaves=paid,
   processed_nodes=self.count,unresolved_leaves=unresolved,rigorously_refuted_leaves=refuted,
   complete_unvisited_suffix=unvisited,stop_reason=reason or "all-planned-closed-pieces-visited",
   minimum_enclosed_radius_lower=None if minimum is None else compact_box(self.factory.Box(minimum)),
   enclosed_speed_hull=None if speed_lo is None else compact_box(self.factory.Box(speed_lo,speed_hi)),
   piece_table_columns=["piece","name","visited_nodes","proved_leaves","unresolved_leaves","refuted_leaves","unvisited_intervals"],
   piece_table=[[r[k] for k in ("piece","name","visited_nodes","proved_leaves","unresolved_leaves","refuted_leaves","unvisited_intervals")]
      for _,r in sorted(by_piece.items())],
   complete_terminal_leaf_ledger=dict(bytes=self.bytes,sha256=self.h.hexdigest(),rows=self.leaves),
   large_passed_leaf_table_is_only_identity_in_small_summary=True)

def bounds_record(factory,model,values,beta):
 j=coast_jets(factory,model,values,beta);B=factory.Box
 return dict(beta_exact=str(beta),changed_parameter_indices=COAST,
  coast_parameter_exact=[str(model["parameters"][i]*beta) for i in COAST],
  exact_center_coordinate="1/2",
  center_as=compact_box(poly(j[1],Q(1,2),B)),
  whole_coast_single_Bernstein_a_as=[compact_box(bernstein(c,Q(0),Q(1),B)) for c in j[:2]],
  center_speed_formula="-kappa+2*coast_length*beta*theta3",
  centered_constraint_is_necessary_not_complete_domain_sufficient=True)

def compact_box(box):
 """Outward summary enclosure only; original exact-Q values remain in temporary ledgers."""
 bits=POLICY["summary_enclosure_grid_bits"];scale=1<<bits
 lo=box.lo.numerator*scale//box.lo.denominator
 hi=-((-box.hi.numerator*scale)//box.hi.denominator)
 original=canonical(box.record())
 return dict(lower_integer=str(lo),upper_integer=str(hi),binary_exponent=-bits,
  original_exact_Q_interval_sha256=sha(original),original_exact_Q_interval_bytes=len(original))

def small_leaf(record):
 result=dict(record)
 result["a_ap_app"]=[compact_box_from_record(x) for x in record["a_ap_app"]]
 return result

def compact_box_from_record(record):
 lo,hi=Q(record["lower"]),Q(record["upper"])
 class Endpoints:
  def __init__(self):self.lo=lo;self.hi=hi
  def record(self):return dict(lower=str(lo),upper=str(hi))
 return compact_box(Endpoints())


def candidate_plan():
 return [Q(1,1<<j) for j in range(POLICY["largest_halving_exponent"]+1)]+[Q(0)]

def projection(parameters):
 rows=[]
 for i,value in enumerate(parameters):
  try:
   x=float(value);finite=math.isfinite(x)
   exact_value=Q.from_float(x) if finite else None
   rows.append(dict(parameter=PARAMETERS[i],accurate_rational=str(value),
    binary64_value=x if finite else None,binary64_word=struct.pack("<d",x).hex() if finite else None,
    represented_exactly=finite and exact_value==value,
    exact_projection_difference=None if exact_value is None else str(exact_value-value)))
  except (ValueError,OverflowError) as error:
   rows.append(dict(parameter=PARAMETERS[i],accurate_rational=str(value),represented_exactly=False,
    projection_error=dict(type=type(error).__name__,message=str(error))))
 return dict(all_nine_exactly_representable=all(x["represented_exactly"] for x in rows),parameters=rows,
  accurate_parameter_strings_not_silently_replaced_by_projection=True,
  numeric_C_midpoint_profile_or_numeric_full_domain_not_computed=True)

def new_profile(factory,model,values,old_definition,beta,args,request,binding):
 parameters=list(model["parameters"])
 for i in COAST:parameters[i]*=beta
 recipe=copy.deepcopy(model["recipe"])
 recipe["nine_parameters"]=[str(x) for x in parameters]
 recipe["parameter_origin"]=dict(kind="actual165-accurate-coast-only-finite-dyadic-repair",
  producer_source_sha256=sha(Path(__file__).read_bytes()),run_id=os.environ["GITHUB_RUN_ID"],
  source_commit=os.environ["GITHUB_SHA"],original_run_id=ORIGINAL_RUN,original_source_commit=ORIGINAL_COMMIT,
  original_input=binding["original_members"]["input"],original_definition=binding["original_definition"],
  beta_exact=str(beta),changed_indices=COAST,other_six_and_semantic_C_and_R323_lengths_unchanged=True)
 recipe_receipt=write(args.out/"selected-accurate-nine-recipe.json",recipe)
 candidate=dict(model,parameters=parameters,recipe=recipe)
 data=factory.definition(candidate,old_definition["continuous_tail"],old_definition["core_input"],recipe_receipt)
 for key in ("construction_conditions","published_structural_and_effective_scope_proof",
             "given_finite_enclosure_is_not_an_effective_real_name","automatic_width_search_performed",
             "actual_enclosure_leaves","base_complete_domain"):
  data[key]=copy.deepcopy(old_definition[key])
 desc=write(args.out/"selected-accurate-nine-definition.json",data)
 parameters_binding=dict(parameter_order=PARAMETERS,nine_parameters_exact=[str(x) for x in parameters],
  coefficient_change_rule="indices2,5,8 multiplied by the explicit common exact dyadic beta; all other six unchanged",
  beta_exact=str(beta),recipe=recipe_receipt,accurate_definition=desc,
  factory_source_sha256=FACTORY_SHA,new_selection_source_sha256=sha(Path(__file__).read_bytes()),
  continuous_model_schema=factory.MODEL_SCHEMA,
  semantic_C_remains_original_all_root_family=True,full_length_expression_unchanged=True,
  source_identity_not_an_accepted_BVP_or_field=True,binary64_projection=projection(parameters))
 return parameters_binding

def finish(args,result,exit_code):
 result["process_exit_code"]=exit_code
 full=write(args.out/"result.json",result)
 summary=dict(result,actual_complete_result=full,summary_complete=True)
 raw=canonical(summary)
 if len(raw)>90000:
  summary={k:result.get(k) for k in ("schema","request_number","run_id","source_commit","source",
   "phase","error","resource_partial","selected_beta_exact","full_accurate_nine_domain_proved",
   "actual_field_created","native_success","fullDN_success","process_exit_code")}
  summary.update(summary_complete=False,transport_error="necessary-summary-exceeds90000",
   complete_temporary_result=full,necessary_summary_bytes=len(raw),necessary_summary_sha256=sha(raw),
   original_result_or_error_not_discarded=True,no_data_split_or_encoding_fallback=True)
  raw=canonical(summary);exit_code=70
 require(len(raw)<=90000,"One honest compact summary")
 args.out.joinpath("summary.json").write_bytes(raw)
 print("BEGIN_REQUEST180_ACCURATE_COAST_REPAIR_SUMMARY",flush=True)
 print(raw.decode("utf-8"),end="",flush=True)
 print("END_REQUEST180_ACCURATE_COAST_REPAIR_SUMMARY",flush=True)
 print(json.dumps(dict(event="request180_summary_identity",bytes=len(raw),sha256=sha(raw),
  includes_final_LF=True,process_exit_code=exit_code)),flush=True)
 if os.environ.get("GITHUB_OUTPUT"):
  with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
   stream.write("coast_summary="+raw.decode("utf-8").rstrip("\n")+"\n")
   stream.write("coast_summary_bytes="+str(len(raw))+"\n")
   stream.write("coast_summary_sha256="+sha(raw)+"\n")
 return exit_code

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for key in ("request","restored-directory","accepted-core","config","code-directory","out"):
  ap.add_argument("--"+key,type=Path,required=True)
 args=ap.parse_args()
 require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,"Public repository Actions scientific execution only")
 require(not any(os.environ.get(k) for k in ("GH_TOKEN","GITHUB_TOKEN","GH_AUTH_TOKEN","GITHUB_AUTH_TOKEN")),"Scientific process receives no GitHub credentials")
 request=json.loads(args.request.read_bytes())
 require(request["schema"]==SCHEMA and request["request_number"]==180 and request["scientific_policy"]==POLICY,"Explicit independent coast-repair contract")
 require(request["source_sha256"][Path(__file__).name]==sha(Path(__file__).read_bytes()),"Actual scientific source pin")
 runner=Path(os.environ["RUNNER_TEMP"]).resolve()
 require(not args.out.exists() and not args.out.is_symlink() and args.out.resolve()!=runner and args.out.resolve().is_relative_to(runner),"Fresh owned temporary scientific output")
 args.out.mkdir(parents=True)
 clock=Clock(POLICY["maximum_seconds"])
 result=dict(schema=SCHEMA,request_number=180,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
  source=receipt(__file__),phase="restore-and-rebuild-same-accurate-definition",
  scientific_policy=POLICY,selected_beta_exact=None,selected_profile=None,
  full_accurate_nine_domain_proved=False,resource_partial=False,error=None,
  all_actual_failed_unresolved_unvisited_candidates_preserved=True,
  summary_enclosures_are_outward_128bit_grid_not_original_exact_Q_endpoints=True,
  original_exact_Q_leaf_ledger_hashes_kept_and_not_recomputed_by_report=True,
  same_C_not_recomputed=True,old_numeric_reference_not_mislabeled_new_profile=True,
  actual_field_created=False,native_success=False,fullDN_success=False,
  new_BVP_acceptance_gate=False,relative_metric_transfer_to_old_field_not_supplied=True,
  continuous_tail_or_caps_closed_geometry_strong_C2_reach_held_not_paid=True,
  raw_outputs_temporary_only=True)
 plan=candidate_plan();result["candidate_plan"]=[dict(index=i,beta_exact=str(b),status="not-started") for i,b in enumerate(plan)]
 code=2
 def interrupted(signum,frame):raise ResourceStop("external-signal-"+str(signum))
 signal.signal(signal.SIGTERM,interrupted);signal.signal(signal.SIGINT,interrupted)
 try:
  factory,model,values,old_definition,binding=rebuild(args,request,clock);result["binding"]=binding
  result["original_coast"]=bounds_record(factory,model,values,Q(1))
  result["unchanged_target_geometry"]=dict(parameter_order=PARAMETERS,
   original_nine_parameters_exact=[str(x) for x in model["parameters"]],
   changed_indices=COAST,unchanged_indices=[i for i in range(9) if i not in COAST],
   complete_accurate_piece_count=419,coast_piece=416,unchanged_piece_count=418,
   core_end=str(model["core_end"]),kappa_exact=str(model["explicit_lengths"][0]),
   d_da_db=[str(x) for x in model["explicit_lengths"][1:]],
   coast_length=compact_box(values[model["roots"]["coast_length"]]),
   total_length=compact_box(values[model["roots"]["total_length"]]),
   support1_xi_not_introduced_and_cannot_change_coast=True,
   center_speed_is_not_used_as_full_domain_certificate=True)
  result["phase"]="prove-all418-unchanged-accurate-pieces-once"
  write(args.out/"progress.json",result)
  segments=fixed_segments(factory,model,values)
  with (args.out/"unchanged418-domain-ledger.jsonl").open("wb") as ledger:
   work=DomainWork(factory,clock,min(clock.deadline,time.monotonic()+POLICY["unchanged_piece_seconds"]),
       POLICY["unchanged_piece_max_nodes"],POLICY["maximum_depth"],ledger)
   outside=work.prove(segments)
  result["all418_unchanged_piece_domain"]=outside
  write(args.out/"progress.json",result)
  print(json.dumps(dict(event="request180-fixed418-complete-or-partial",
   complete=outside["complete"],processed_nodes=outside["processed_nodes"],
   proved_leaves=outside["proved_leaves"],unresolved_leaves=len(outside["unresolved_leaves"]),
   refuted_leaves=len(outside["rigorously_refuted_leaves"]),
   unvisited_intervals=len(outside["complete_unvisited_suffix"]),
   mathematical_success_not_inferred_from_process_progress=True)),flush=True)
  if outside["error"] is not None:raise ArithmeticError("Fixed-piece arithmetic failure retained in complete domain record")
  if outside["complete_unvisited_suffix"]:result["resource_partial"]=True
  result["phase"]="bounded-descending-dyadic-coast-repair"
  for i,beta in enumerate(plan):
   clock.check();record=result["candidate_plan"][i];record.update(bounds_record(factory,model,values,beta))
   record["status"]="running"
   segment=dict(piece=416,name="negative-speed-coast",lo=Q(0),hi=Q(1),
                jets=coast_jets(factory,model,values,beta),control_support=2)
   with (args.out/("coast-candidate-"+str(i).zfill(3)+".jsonl")).open("wb") as ledger:
    work=DomainWork(factory,clock,clock.deadline,POLICY["coast_per_candidate_max_nodes"],
         POLICY["maximum_depth"],ledger)
    domain=work.prove([segment],stop_on_strict_refutation=True)
   record["complete_coast_domain"]=domain
   if domain["error"] is not None:raise ArithmeticError("Coast arithmetic failure retained in actual candidate record")
   if domain["stop_reason"] in ("whole-science-wall-budget","local-domain-wall-budget","local-domain-node-budget"):
    result["resource_partial"]=True
   record["whole_accurate_nine_domain_proved"]=bool(outside["complete"] and domain["complete"])
   record["status"]=("whole-domain-proved" if record["whole_accurate_nine_domain_proved"]
       else "coast-proved-fixed-part-unpaid" if domain["complete"]
       else "rigorously-refuted" if domain["rigorously_refuted_leaves"]
       else "unresolved-or-resource-partial")
   write(args.out/"progress.json",result)
   print(json.dumps(dict(event="request180-actual-coast-candidate",index=i,beta_exact=str(beta),
    status=record["status"],complete_coast_domain=domain["complete"],
    whole_accurate_nine_domain_proved=record["whole_accurate_nine_domain_proved"],
    actual_domain_error=domain["error"],processed_nodes=domain["processed_nodes"])),flush=True)
   if record["whole_accurate_nine_domain_proved"]:
    result["selected_beta_exact"]=str(beta);result["selected_profile"]=new_profile(
       factory,model,values,old_definition,beta,args,request,binding)
    result["full_accurate_nine_domain_proved"]=True
    for remaining in result["candidate_plan"][i+1:]:
     remaining["status"]="not-visited-after-first-proved-full-domain-candidate"
    break
  result["phase"]="bounded-repair-finished"
  result["first_proved_in_declared_order_not_global_or_continuous_maximum"]=True
  result["all_declarations_are_uniform_over_inherited_semantic_cut_boxes"]=True
  result["actual_BVP_parameter_restart_available"]=result["full_accurate_nine_domain_proved"]
  code=0 if result["full_accurate_nine_domain_proved"] else 3
 except ResourceStop as exc:
  result["resource_partial"]=True;result["error"]=dict(type=type(exc).__name__,message=str(exc));code=3
 except BaseException as exc:
  result["error"]=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());code=2
 finally:
  signal.signal(signal.SIGTERM,signal.SIG_IGN);signal.signal(signal.SIGINT,signal.SIG_IGN)
  for row in result["candidate_plan"]:
   if row["status"]=="not-started":
    row["status"]="unvisited-after-"+result["phase"]
   elif row["status"]=="running":
    row["status"]="attempted-but-interrupted-or-error-after-"+result["phase"]
  result["elapsed_seconds"]=time.monotonic()-clock.start
  code=finish(args,result,code)
 return code

if __name__=="__main__":raise SystemExit(main())
