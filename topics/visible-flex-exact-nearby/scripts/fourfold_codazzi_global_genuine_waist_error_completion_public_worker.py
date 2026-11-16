#!/usr/bin/env python3
"""Supervise only the 30 uncomputed WEJ records; preserve every completed prior record."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata,re
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def save(p,v):
  p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
  t=p.with_name(p.name+".partial")
  t.write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+"\n");t.replace(p)
def checked(p,size,digest):
  p=Path(p)
  if not p.is_file() or p.stat().st_size!=size or sha(p)!=digest:
    raise ValueError("one complete pinned input differs: "+str(p))
def read(p):return json.loads(Path(p).read_text())
def relpath(p):
  p=Path(p)
  if p.is_absolute() or ".." in p.parts or not str(p).startswith(str(TOPIC)+"/"):
    raise ValueError("one input left the authorized topic")
  return p
def safe_name(value):
  p=Path(value)
  if p.is_absolute() or not value or ".." in p.parts:
    raise ValueError("one scientific conclusion has an unsafe relative path")
  return p
def rec(p,base):
  p=Path(p);return dict(file=str(p.relative_to(base)),bytes=p.stat().st_size,sha256=sha(p))
def ball(v):
  if isinstance(v,dict):
    if isinstance(v.get("ball"),str):return v["ball"]
    if "upper" in v:return str(v["upper"])
    return json.dumps(v,ensure_ascii=False,separators=(",",":"))
  return str(v)
def cell(v):return str(v).replace("|","\\|").replace("\n"," ")

class TransientMetadataError(RuntimeError):
  """Retryable read-only metadata failure; no failed identity or policy gate is suppressed."""
  pass

def topic_tree_metadata(git,topic,repository):
  """Read the exact published origin/main tree; never request an unpublished local HEAD or a blob body."""
  head=git("rev-parse","origin/main").stdout.strip()
  def oid(value):
    return isinstance(value,str) and len(value)==40 and all(c in "0123456789abcdef" for c in value)
  if not oid(head):raise ValueError("the capacity audit requires an exact Git commit")
  root_tree=git("rev-parse",head+"^{tree}").stdout.strip()
  local_topic_tree=git("rev-parse",head+":"+str(topic)).stdout.strip()
  if not oid(root_tree) or not oid(local_topic_tree):
    raise ValueError("the capacity audit requires complete local commit and tree identities")
  token=os.environ.get("GITHUB_TOKEN")
  if not token:raise RuntimeError("the public metadata request requires its Actions token")
  responses=[]
  class NoMetadataRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,request,fp,code,message,headers,newurl):
      raise RuntimeError("the capacity metadata endpoint attempted a redirect")
  opener=urllib.request.build_opener(NoMetadataRedirect())
  def request_tree(tree,recursive=False):
    url="https://api.github.com/repos/"+repository+"/git/trees/"+tree
    if recursive:url+="?recursive=1"
    request=urllib.request.Request(url,headers={
      "Accept":"application/vnd.github+json",
      "X-GitHub-Api-Version":"2022-11-28",
      "Authorization":"Bearer "+token})
    # A transient read-only service failure is not a scientific or policy gate.
    # Retry the same frozen tree identity; never substitute stale capacity.
    for attempt in range(4):
      try:
        with opener.open(request,timeout=45) as response:
          if response.geturl()!=url:
            raise RuntimeError("the capacity metadata request was redirected")
          data=response.read(16000001)
        break
      except urllib.error.HTTPError as error:
        if error.code not in (408,425,429,500,502,503,504):
          raise RuntimeError("the Git tree metadata request returned HTTP "+str(error.code)) from None
        if attempt==3:
          raise TransientMetadataError("read-only Git tree metadata returned HTTP "+str(error.code)) from None
      except (urllib.error.URLError,TimeoutError) as error:
        if attempt==3:
          raise TransientMetadataError("read-only Git tree metadata transport failed") from None
      time.sleep(2**attempt)
    if len(data)>16000000:raise ValueError("the Git tree metadata response exceeded its bounded size")
    doc=json.loads(data)
    if doc.get("sha")!=tree or doc.get("truncated") is not False or not isinstance(doc.get("tree"),list):
      raise ValueError("a Git tree metadata identity or complete-response gate failed")
    responses.append(dict(tree=tree,recursive=recursive,bytes=len(data),
      sha256=hashlib.sha256(data).hexdigest(),truncated=False))
    return doc["tree"]
  # Freeze the public origin/main commit before resolving its topic components.
  # Compare with Git's independent commit:topic identity; API URLs contain only exact object IDs.
  tree=root_tree
  for component in topic.parts:
    entries=request_tree(tree)
    matches=[entry for entry in entries if entry.get("path")==component]
    if len(matches)!=1 or matches[0].get("type")!="tree" or matches[0].get("mode")!="040000":
      raise ValueError("the authorized topic is not an exact tree at this commit")
    tree=matches[0].get("sha")
    if not oid(tree):raise ValueError("the topic path contains an invalid Git tree identity")
  if tree!=local_topic_tree:
    raise ValueError("the API and local published-commit topic tree identities differ")
  entries=request_tree(tree,recursive=True)
  seen=set();blobs={};inventory=[];trees=0;gitlinks=0
  for entry in entries:
    path=entry.get("path")
    if (not isinstance(path,str) or not path or path.startswith("/")
      or any(part in ("",".","..") for part in path.split("/")) or path in seen):
      raise ValueError("the complete topic tree contains an invalid or duplicate path")
    seen.add(path)
    kind=entry.get("type");mode=entry.get("mode");digest=entry.get("sha")
    if not oid(digest):raise ValueError("a topic object has an invalid Git identity")
    if kind=="blob":
      size=entry.get("size")
      if type(size) is not int or size<0 or mode not in ("100644","100755","120000"):
        raise ValueError("a topic blob has no exact nonnegative metadata size or valid mode")
      full=str(topic)+"/"+path
      blobs[full]=dict(bytes=size,git_blob=digest,mode=mode)
      inventory.append(dict(path=full,bytes=size,git_blob=digest,mode=mode))
    elif kind=="tree":
      if mode!="040000":raise ValueError("a nested topic tree has the wrong mode")
      trees+=1
    elif kind=="commit":
      if mode!="160000":raise ValueError("a topic Git link has the wrong mode")
      gitlinks+=1
    else:raise ValueError("the complete topic tree has an unsupported entry type")
  inventory.sort(key=lambda entry:entry["path"])
  receipt=dict(method="published_origin_main_Git_Trees_API_metadata_only",commit=head,
    root_tree=root_tree,topic=str(topic),topic_tree=tree,
    truncated=False,all_blob_sizes_checked=True,blob_count=len(blobs),
    blob_bytes=sum(entry["bytes"] for entry in blobs.values()),
    nested_tree_count=trees,gitlink_count=gitlinks,
    complete_blob_metadata_inventory_sha256=hashlib.sha256(
      json.dumps(inventory,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest(),
    metadata_responses=responses,blob_bodies_requested=False)
  return receipt,blobs

def owned_head_delta(git,root,capacity,blob_map,allowed_paths):
  """Audit local unpushed report blobs without querying their unpublished Git tree through the API."""
  base=capacity["commit"];head=git("rev-parse","HEAD").stdout.strip()
  raw=git("diff","--name-status","--no-renames","-z",base,head,"--",str(TOPIC)).stdout
  fields=raw.split("\0")
  if fields[-1:]!=[""]:raise ValueError("the complete local topic delta lacks its terminator")
  fields=fields[:-1]
  if len(fields)%2:raise ValueError("the local topic delta is not an exact name-status list")
  total=capacity["blob_bytes"];count=capacity["blob_count"];changes=[]
  for status,name in zip(fields[0::2],fields[1::2]):
    if name not in allowed_paths or status not in ("A","M","D"):
      raise ValueError("an unpublished local topic change is outside the declared owned small conclusions")
    before=blob_map.get(name)
    if status=="A" and before is not None:raise ValueError("an added owned path already exists in the published base")
    if status in ("M","D") and before is None:raise ValueError("a changed owned path is absent from the published base")
    oldbytes=0 if before is None else before["bytes"]
    total-=oldbytes;count-=int(before is not None)
    change=dict(path=name,status=status,published_bytes=oldbytes,
      published_git_blob=None if before is None else before["git_blob"])
    if status!="D":
      line=git("ls-tree","-z",head,"--",name).stdout
      if not line.endswith("\0") or line.count("\0")!=1:
        raise ValueError("the owned HEAD path is not one exact Git entry")
      header,path=line[:-1].split("\t",1);mode,kind,digest=header.split()
      if path!=name or mode!="100644" or kind!="blob" or len(digest)!=40:
        raise ValueError("the owned HEAD conclusion is not a regular text blob")
      body=git("show",head+":"+name).stdout.encode()
      limit=allowed_paths[name]
      if len(body)>limit:raise ValueError("an owned HEAD conclusion exceeds its exact small-text limit")
      calculated=hashlib.sha1(b"blob "+str(len(body)).encode()+b"\0"+body).hexdigest()
      if calculated!=digest:raise ValueError("the exact owned HEAD bytes do not match their Git blob")
      total+=len(body);count+=1
      change.update(head_bytes=len(body),head_git_blob=digest,head_sha256=hashlib.sha256(body).hexdigest())
    changes.append(change)
  return dict(method="published_origin_main_API_plus_exact_owned_HEAD_delta",commit=head,
    published_base_commit=base,published_base_topic_tree=capacity["topic_tree"],
    head_topic_tree=git("rev-parse",head+":"+str(TOPIC)).stdout.strip(),
    blob_bytes=total,blob_count=count,owned_local_delta=changes,
    original_complete_base_metadata_inventory_sha256=capacity["complete_blob_metadata_inventory_sha256"],
    exact_owned_paths_only=True,unpublished_tree_requested_from_API=False)


def compact(value):
  return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
           allow_nan=False)+"\n").encode()


MANIFEST_KIND="complete_WEJ_remaining_current_input_manifest_v1"
INDEX_KIND="complete_remaining_WEJ_posterior_v1"
ENVELOPE_KIND="WEJ_complete_atomic_node_v1"
SCIENTIFIC_ROLES=("remaining_pipeline","remaining_math")
INDEX_FIELDS=(
"kind","complete","proved","actual_returncode","failure","public_repository",
"run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit",
"source_sha256","scientific_module_sha256","input_manifest_sha256",
"parameters","parameters_sha256","mathematical_input_sha256","runtime",
"arithmetic_bits","gates","node_receipts","original_input_files",
"locked_attempted_nodes","active_node","stage","actual_progress",
"actual_mathematical_wall_seconds","old_scientific_calls","old_binary_parts_restored",
"new_reproducible_arrays_persisted","new_artifacts","new_Releases","retained_scope")
BINDING_FIELDS={"problem_id","parameters_sha256","mathematical_input_sha256",
        "scientific_module_sha256","direct_dependency_receipts"}
COMPLETE_NODE_FIELDS={"kind","node_name","binding","complete",
  "printed_record_event_count","all_printed_records_in_complete_conclusion",
  "conclusion","failure","automatic_retry_authorized"}
PARTIAL_NODE_FIELDS={"kind","node_name","binding","complete","printed_record_events",
  "conclusion","explicit_math_prefix","failure","automatic_retry_authorized"}
PARTIAL_DESCRIPTOR_KIND="WEJ_lossless_split_partial_envelope_v1"
PARTIAL_FIELD_KIND="WEJ_complete_partial_field_v1"
PARTIAL_FIELD_FILES={
"conclusion":"partial-node-conclusion.json",
"printed_record_events":"partial-node-record-events.json",
"explicit_math_prefix":"partial-node-explicit-prefix.json"}
ORIGINAL_FILENAMES=("retained-prefix-admission.json",)
REMAINING_NODE_NAMES=(
"complete_free_waist_Airy_and_Schur_map",
"complete_four_waist_endpoint_contributions",
"complete_same_physical_whole_and_reduced_error")
REMAINING_COMPLETE_RECORD_COUNTS=(52,8,15)
REMAINING_NEW_RECORD_COUNTS=(13,8,9)
RETAINED_RECORD_COUNTS={
"complete_nodes":23,"complete_saved_slots":1609,"complete_new_records":1600,
"complete_original_copy_slots":9,"partial_new_records":39,
"allowed_remaining_new_records":30}

def require(test,message):
  if not test:raise ValueError(message)

def reject_constant(value):
  raise ValueError("nonfinite JSON token is not a complete saved scientific record: "+value)

def exact_json(raw):
  return json.loads(raw.decode("utf-8"),parse_constant=reject_constant)

def hex_string(value,size):
  return (isinstance(value,str) and len(value)==size
    and all(c in "0123456789abcdef" for c in value))

def finite_record(value):
  return (isinstance(value,dict) and set(value)=={"ball"}
    and isinstance(value["ball"],str) and 0<len(value["ball"])<=1024
    and any(c.isdigit() for c in value["ball"])
    and not any(x in value["ball"].lower() for x in ("nan","inf"))
    and re.fullmatch(r"[\[\]0-9eE+\-./ \t]+",value["ball"]) is not None)

def finite_number(value):
  return type(value) in (int,float) and value==value and abs(value)<float("inf")

def full_shape(value,expected):
  # This is a pure JSON check. No ball or old scientific producer is evaluated.
  if isinstance(expected,dict) and set(expected)=={"ball"}:
    token=expected["ball"]
    if isinstance(token,str) and token.startswith("__NEW_"):
      return finite_record(value)
  if isinstance(expected,str):
    if expected in ("#U","#L","__NEW_FINITE_NONNEGATIVE_RECORD__"):
      return finite_record(value)
    if expected.startswith("__TYPE_") and expected.endswith("__"):
      kind=expected[7:-2]
      if kind.startswith("OPTIONAL_"):
        if value is None:return True
        kind=kind[9:]
      kinds={"STRING":isinstance(value,str),"INTEGER":type(value) is int,
         "NUMBER":finite_number(value),"BOOLEAN":type(value) is bool,
         "OBJECT":isinstance(value,dict),"LIST":isinstance(value,list)}
      return kinds.get(kind,False)
  if isinstance(expected,dict):
    return (isinstance(value,dict) and set(value)==set(expected)
      and all(full_shape(value[k],v) for k,v in expected.items()))
  if isinstance(expected,list):
    return (isinstance(value,list) and len(value)==len(expected)
      and all(full_shape(x,y) for x,y in zip(value,expected)))
  if type(expected) in (int,float):
    return type(value) in (int,float) and value==expected
  return type(value) is type(expected) and value==expected

def json_equal(value,expected):
  if isinstance(expected,dict):
    return (isinstance(value,dict) and set(value)==set(expected)
        and all(json_equal(value[k],v) for k,v in expected.items()))
  if isinstance(expected,list):
    return (isinstance(value,list) and len(value)==len(expected)
        and all(json_equal(a,b) for a,b in zip(value,expected)))
  if type(expected) in (int,float):
    return type(value) in (int,float) and value==expected
  return type(value) is type(expected) and value==expected

def ball_count(value):
  if isinstance(value,dict):
    if set(value)=={"ball"} and isinstance(value["ball"],str):return 1
    return sum(ball_count(v) for v in value.values())
  if isinstance(value,list):return sum(ball_count(v) for v in value)
  return 0

def at(value,path):
  for key in path:value=value[key]
  return value

def expected_pins(manifest):
  files={p["role"]:p for p in manifest["files"]}
  originals={r:files[r]["sha256"] for r in manifest["mathematical_input_roles"]}
  modules={r:files[r]["sha256"] for r in SCIENTIFIC_ROLES}
  return originals,modules

def declared_caps(manifest):
  limits=manifest["publication_limits"]
  caps={"index.json":limits["complete_index_max_bytes"],
     "report.md":limits["complete_report_max_bytes"],
     "execution.json":limits["complete_execution_max_bytes"]}
  for spec in manifest["original_input_specs"]:
    require(spec["relative_path"] not in caps,"duplicate complete original-input filename")
    caps[spec["relative_path"]]=spec["publication_max_bytes"]
  for spec in manifest["ordered_node_specs"]:
    require(spec["relative_path"] not in caps,"duplicate owned scientific filename")
    caps[spec["relative_path"]]=spec["publication_max_bytes"]
  for spec in manifest["complete_publication_static_budget"]["partial_files"]:
    require(spec["file"] not in caps,"duplicate complete partial-field filename")
    caps[spec["file"]]=spec["max_bytes"]
  return caps

def validate_contract(root,manifest,pipeline_sha,worker_path,worker_sha,rules_path,rules_sha,resolve_shapes=True):
  m=manifest;files=m.get("files",[]);roles=[x.get("role") for x in files]
  paths=[x.get("path") for x in files]
  require(m.get("kind")==MANIFEST_KIND and m.get("public_repository")==PUBLIC,
      "different remaining-only manifest")
  require(m.get("historical_inputs")==[] and m.get("legacy_artifact_inputs",[])==[],
      "current text inputs only")
  require(len(roles)==len(set(roles)) and len(paths)==len(set(paths)),
      "duplicate immutable current input")
  require(m.get("expected_input_count")==len(files),"incomplete current file count")
  require(m.get("expected_current_input_count",len(files))==len(files),
      "different current file count")
  byrole={x["role"]:x for x in files}
  if resolve_shapes:
    role=m["output_contract_role"]
    require(role in byrole and byrole[role]["read_as_json"] is True,
        "missing remaining output contract")
    spec=byrole[role];path=root/relpath(spec["path"])
    checked(path,spec["bytes"],spec["sha256"])
    output_contract=exact_json(path.read_bytes())
    require(output_contract.get("kind")=="complete_WEJ_remaining_output_contract_v1",
        "wrong remaining output contract")
    require(set(output_contract["binding_fields"])==BINDING_FIELDS
        and set(output_contract["complete_node_envelope_fields"])==COMPLETE_NODE_FIELDS
        and set(output_contract["partial_node_envelope_fields"])==PARTIAL_NODE_FIELDS,
        "envelope schema changed")
    for key in ("complete_index_shape","partial_index_shape"):
      require(set(output_contract[key])==set(INDEX_FIELDS),"index shape field closure differs")
    m["_resolved_output_contract"]=output_contract
    for key in ("publication_limits","complete_publication_static_budget",
          "ordered_node_specs","original_input_specs"):
      if key in output_contract:
        if key in m:
          require(json_equal(m[key],output_contract[key]),
              "manifest and output contract disagree: "+key)
        else:m[key]=output_contract[key]
  for spec in files:
    name=relpath(spec["path"])
    require(name.suffix in (".py",".json",".md") and type(spec["bytes"]) is int
        and 0<spec["bytes"]<100000,"all current files must be complete small text")
    require(hex_string(spec["sha256"],64) and hex_string(spec["git_blob_sha"],40),
        "incomplete original byte or Git identity")
    require(isinstance(spec.get("read_as_json"),bool),"explicit current JSON/text admission required")
  require(set(SCIENTIFIC_ROLES)<=set(roles),"incomplete two-module remaining-only scientific closure")
  require(all(byrole[r]["path"].endswith(".py") for r in SCIENTIFIC_ROLES),
      "a scientific module is not the declared Python text")
  pipeline=relpath(m["source_path"]);reports=relpath(m["reports_path"])
  require(str(pipeline).startswith(str(TOPIC)+"/scripts/") and pipeline.suffix==".py",
      "driver outside topic scripts")
  require(str(reports).startswith(str(TOPIC)+"/notes/") and "." not in reports.name,
      "report path outside topic notes")
  require(byrole["remaining_pipeline"]["path"]==str(pipeline)
      and byrole["remaining_pipeline"]["sha256"]==pipeline_sha
      and m.get("source_sha256")==pipeline_sha,"scientific source pin mismatch")
  workers=[x for x in files if x["path"]==str(worker_path)]
  rule_entries=[x for x in files if x["path"]==str(rules_path)]
  require(len(workers)==1 and workers[0]["sha256"]==worker_sha
      and len(rule_entries)==1 and rule_entries[0]["sha256"]==rules_sha,
      "worker/rules pins differ")
  mathroles=m.get("mathematical_input_roles")
  require(isinstance(mathroles,list) and bool(mathroles)
      and len(set(mathroles))==len(mathroles) and set(mathroles)<=set(roles),
      "retained input map missing")
  require(not (set(mathroles)&set(SCIENTIFIC_ROLES)),
      "old/new role overlap")
  require(m.get("original_input_filenames")==list(ORIGINAL_FILENAMES),
      "different complete original-admission filenames")
  require(m.get("parameters",{}).get("arithmetic_bits")==320,
      "different directed precision")
  require(m.get("problem_id")=="WEJ_remaining_after_43827705714_v1",
      "different exact-prefix continuation target")
  require(m.get("expected_final_gate_count")==9,"different complete 9-gate contract")
  ast_roles=[v["role"] for v in files if v["path"].endswith(".py")]
  require(m.get("expected_immutable_AST_files")==len(ast_roles),
      "incomplete immutable AST count")
  if "immutable_AST_roles" in m:
    require(m["immutable_AST_roles"]==ast_roles,"different immutable AST order")
  specs=m.get("ordered_node_specs",[])
  require([v["node_name"] for v in specs]==list(REMAINING_NODE_NAMES),
      "wrong remaining node inventory")
  seen=set()
  for node_index,spec in enumerate(specs):
    name=spec["node_name"]
    require(isinstance(name,str) and re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*",name)
        and name not in seen,"invalid or duplicate scientific node")
    require(spec["relative_path"]=="graphs/"+name+".json","noncanonical scientific path")
    require(isinstance(spec["dependency_names"],list)
        and len(set(spec["dependency_names"]))==len(spec["dependency_names"])
        and set(spec["dependency_names"])<=seen,"dependencies must be complete earlier nodes")
    require(spec["module_role"]=="remaining_math","only the new remaining mathematics may produce a node")
    for key in ("producer_name","decoder_name"):
      require(isinstance(spec[key],str) and
        re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*",spec[key]),"unsafe declared callable")
    require(type(spec["record_count"]) is int
        and spec["record_count"]==REMAINING_COMPLETE_RECORD_COUNTS[node_index]
        and type(spec.get("printed_record_event_count")) is int
        and spec["printed_record_event_count"]==REMAINING_NEW_RECORD_COUNTS[node_index],
        "complete/new record counts differ")
    require(spec["dependency_names"]==([] if node_index==0 else
          [REMAINING_NODE_NAMES[node_index-1]]),
        "new dependency order differs")
    require(type(spec["publication_max_bytes"]) is int
        and 0<spec["publication_max_bytes"]<100000,"node publication cap must be below100KB")
    if "conclusion_shape" not in spec:
      role=spec["schema_role"];key=spec["conclusion_shape_key"]
      require(role in byrole and byrole[role]["read_as_json"] is True,
          "missing current pinned full shape source")
      if resolve_shapes:
        path=root/relpath(byrole[role]["path"])
        checked(path,byrole[role]["bytes"],byrole[role]["sha256"])
        models=exact_json(path.read_bytes())
        spec["conclusion_shape"]=models["complete_conclusion_shapes"][key]
    if "conclusion_shape" in spec:
      require(ball_count_shape(spec["conclusion_shape"])==spec["record_count"],
          "declared complete shape record count differs")
    seen.add(name)
  if not resolve_shapes:return pipeline,reports,{}
  limits=m.get("publication_limits",{})
  require(limits.get("reserved_publication_bytes")==120000,"different reviewed publication reserve")
  for key in ("complete_index_max_bytes","complete_original_inputs_max_bytes",
        "complete_report_max_bytes","complete_execution_max_bytes"):
    require(type(limits.get(key)) is int and 0<limits[key]<100000,
        "publication cap must be below100KB")
  require(limits["complete_report_max_bytes"]<=8000
      and limits["complete_execution_max_bytes"]<=59000,
      "report/execution cap too large")
  budget=m["complete_publication_static_budget"]
  require(isinstance(budget,dict) and set(budget)=={
    "base_files","complete_nodes","partial_files","partial_scenarios",
    "complete_total_max_bytes","maximum_total_bytes"},
    "incomplete conditional static publication budget")
  require([v["file"] for v in budget["partial_files"]]==list(PARTIAL_FIELD_FILES.values()),
      "the complete partial-field inventory differs")
  for spec in budget["partial_files"]:
    require(type(spec["max_bytes"]) is int and 0<spec["max_bytes"]<100000,
        "a complete partial-field file reaches100KB")
  require([v["relative_path"] for v in m["original_input_specs"]]==list(ORIGINAL_FILENAMES),
      "the complete original-input publication order differs")
  for spec in m["original_input_specs"]:
    require(spec["validation"]=="exact_independent_retained_prefix_input_document_reconstruction"
        and type(spec["publication_max_bytes"]) is int
        and 0<spec["publication_max_bytes"]<=limits["complete_original_inputs_max_bytes"],
        "the complete original-input publication contract differs")
  caps=declared_caps(m)
  require({v["file"] for v in budget["base_files"]}==
      {"index.json","report.md","execution.json",*ORIGINAL_FILENAMES}
      and len(budget["base_files"])==4,
      "the complete static base-file budget differs")
  require(len(budget["complete_nodes"])==len(specs),
      "the complete static node-file budget differs")
  for v,spec in zip(budget["complete_nodes"],specs):
    require(v["node_name"]==spec["node_name"] and v["file"]==spec["relative_path"],
        "static node budget order differs")
  all_files=budget["base_files"]+budget["complete_nodes"]+budget["partial_files"]
  require(len({v["file"] for v in all_files})==len(all_files)
      and {v["file"] for v in all_files}==set(caps),
      "publication budget inventory differs")
  for v in all_files:
    require(type(v["max_bytes"]) is int and 0<v["max_bytes"]<=caps[v["file"]],
        "per-file budget exceeds cap")
  base_total=sum(v["max_bytes"] for v in budget["base_files"])
  complete_total=base_total+sum(v["max_bytes"] for v in budget["complete_nodes"])
  require(type(budget["complete_total_max_bytes"]) is int
      and budget["complete_total_max_bytes"]==complete_total,
      "complete static success total differs")
  scenarios=budget["partial_scenarios"]
  require(len(scenarios)==len(specs),"every failed-node prefix must have its complete static budget")
  totals=[complete_total];prefix=0
  names=[s["node_name"] for s in specs]
  partial_caps={v["file"]:v["max_bytes"] for v in budget["partial_files"]}
  for i,(scenario,spec) in enumerate(zip(scenarios,specs)):
    count=scenario["completed_prefix_nodes"]
    require((type(count) is int and count==i) or
        (isinstance(count,list) and count==names[:i]),
        "failed-node budget has a different completed prefix")
    require(scenario["node_name"]==spec["node_name"],"failed-node budget order differs")
    amounts=[scenario[k] for k in ("descriptor_max_bytes","conclusion_max_bytes",
         "record_events_max_bytes","explicit_prefix_max_bytes")]
    require(all(type(n) is int and n>=0 for n in amounts)
        and amounts[0]>0 and amounts[0]<=spec["publication_max_bytes"],
        "descriptor budget exceeds cap")
    for amount,filename in zip(amounts[1:],PARTIAL_FIELD_FILES.values()):
      require(amount<=partial_caps[filename],
          "partial field exceeds cap")
    total=base_total+prefix+sum(amounts)
    require(type(scenario["total_max_bytes"]) is int and scenario["total_max_bytes"]==total,
        "conditional prefix publication total differs")
    totals.append(total);prefix+=budget["complete_nodes"][i]["max_bytes"]
  require(type(budget["maximum_total_bytes"]) is int
      and budget["maximum_total_bytes"]==max(totals),
      "success/partial maximum differs")
  if "complete_input_bytes" in m:
    require(m["complete_input_bytes"]==sum(v["bytes"] for v in files),
        "complete current input byte total differs")
  require(m.get("old_successful_scientific_calls_allowed") is False
      and m.get("new_native_arrays_or_artifact_persistence_allowed") is False,
      "old math/artifacts prohibited")
  return pipeline,reports,caps

def ball_count_shape(value):
  if isinstance(value,dict):
    if set(value)=={"ball"} and isinstance(value["ball"],str):return 1
    return sum(ball_count_shape(v) for v in value.values())
  if isinstance(value,list):return sum(ball_count_shape(v) for v in value)
  if isinstance(value,str) and value in ("#U","#L","__NEW_FINITE_NONNEGATIVE_RECORD__"):
    return 1
  return 0


def split_partial_envelope(filename,raw,payload):
  """Lossless JSON projection only; no record, number or scientific target is evaluated."""
  require(payload.get("kind")==ENVELOPE_KIND and payload.get("complete") is False
      and set(payload)==PARTIAL_NODE_FIELDS,
      "only a complete saved partial envelope may be split")
  node=payload["node_name"]
  require(filename=="graphs/"+node+".json","different partial node filename")
  require(raw==compact(payload),"the original partial bytes must be canonical before projection")
  remaining={k:v for k,v in payload.items() if k not in PARTIAL_FIELD_FILES}
  refs={};parts={}
  for field,path in PARTIAL_FIELD_FILES.items():
    value=payload[field]
    document={"kind":PARTIAL_FIELD_KIND,"node_name":node,
         "field":field,"complete_field_value":value}
    data=compact(document);parts[path]=data
    refs[field]={"file":path,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
  descriptor={
   "kind":PARTIAL_DESCRIPTOR_KIND,"node_name":node,"complete":False,
   "original_envelope_fields":remaining,
   "original_envelope_identity":{"file":filename,"bytes":len(raw),
                  "sha256":hashlib.sha256(raw).hexdigest()},
   "complete_field_files":refs,
   "reconstruction":"restore all three original fields, then sorted compact UTF8 JSON plus LF",
   "all_original_fields_and_record_order_retained":True,
   "automatic_retry_authorized":False}
  physical={filename:compact(descriptor),**parts}
  # Verify the codec immediately by full original byte identity, not an upper bound.
  restored=reconstruct_partial_envelope(filename,descriptor,physical)
  require(restored==raw,"lossless partial projection changed original scientific bytes")
  return physical,descriptor

def reconstruct_partial_envelope(filename,descriptor,physical_files):
  require(isinstance(descriptor,dict) and set(descriptor)=={
    "kind","node_name","complete","original_envelope_fields",
    "original_envelope_identity","complete_field_files","reconstruction",
    "all_original_fields_and_record_order_retained","automatic_retry_authorized"},
    "partial descriptor schema differs")
  require(descriptor["kind"]==PARTIAL_DESCRIPTOR_KIND and descriptor["complete"] is False
      and descriptor["all_original_fields_and_record_order_retained"] is True
      and descriptor["automatic_retry_authorized"] is False
      and descriptor["reconstruction"]==
       "restore all three original fields, then sorted compact UTF8 JSON plus LF",
      "partial descriptor changed its preservation contract")
  node=descriptor["node_name"]
  require(filename=="graphs/"+node+".json","partial descriptor changed its scientific node")
  identity=descriptor["original_envelope_identity"]
  require(isinstance(identity,dict) and set(identity)=={"file","bytes","sha256"}
      and identity["file"]==filename and type(identity["bytes"]) is int
      and identity["bytes"]>0 and hex_string(identity["sha256"],64),
      "complete original partial identity missing")
  rest=descriptor["original_envelope_fields"]
  require(isinstance(rest,dict) and set(rest)==PARTIAL_NODE_FIELDS-set(PARTIAL_FIELD_FILES),
      "partial descriptor dropped an original envelope field")
  refs=descriptor["complete_field_files"]
  require(isinstance(refs,dict) and set(refs)==set(PARTIAL_FIELD_FILES),
      "partial field inventory is incomplete")
  envelope=dict(rest)
  for field,path in PARTIAL_FIELD_FILES.items():
    ref=refs[field]
    require(isinstance(ref,dict) and set(ref)=={"file","bytes","sha256"}
        and ref["file"]==path and type(ref["bytes"]) is int and ref["bytes"]>0
        and hex_string(ref["sha256"],64),"partial field reference differs")
    require(path in physical_files,"complete partial projection file missing")
    raw=physical_files[path]
    require(len(raw)==ref["bytes"] and hashlib.sha256(raw).hexdigest()==ref["sha256"],
        "complete partial projection byte identity differs")
    part=exact_json(raw)
    require(raw==compact(part) and isinstance(part,dict) and set(part)=={
      "kind","node_name","field","complete_field_value"}
      and part["kind"]==PARTIAL_FIELD_KIND and part["node_name"]==node
      and part["field"]==field,"complete partial projection schema differs")
    envelope[field]=part["complete_field_value"]
  require(envelope.get("kind")==ENVELOPE_KIND and envelope.get("node_name")==node
      and envelope.get("complete") is False and envelope.get("automatic_retry_authorized") is False,
      "reconstructed partial is a different scientific target")
  original=compact(envelope)
  require(len(original)==identity["bytes"]
      and hashlib.sha256(original).hexdigest()==identity["sha256"],
      "lossless partial reconstruction does not match its complete original SHA")
  return original

def prepare_publication_files(bundle,manifest):
  """Project every stopped partial into the same three complete natural JSON fields."""
  caps=declared_caps(manifest)
  physical=dict(bundle.get("physical_raw",bundle["raw"]))
  split=[]
  for spec in manifest["ordered_node_specs"]:
    filename=spec["relative_path"];raw=bundle["raw"].get(filename)
    doc=bundle["documents"].get(filename)
    if raw is None or not isinstance(doc,dict) or doc.get("complete") is not False:
      continue
    require(not split,"only one stopped partial node may be projected in this run")
    projected,descriptor=split_partial_envelope(filename,raw,doc)
    physical.update(projected);split.append(descriptor)
  bundle["publication_raw"]=physical
  bundle["split_partial_descriptors"]=split
  return physical


def complete_expected_original_documents(root,manifest,input_receipts):
  """Reconstruct retained JSON only; no original producer or ball is evaluated."""
  files={p["role"]:p for p in manifest["files"]};docs={};raws={};by_path={}
  keys=("role","path","bytes","sha256","git_blob_sha")
  receipts=[{k:r[k] for k in keys} for r in input_receipts]
  require([r["role"] for r in receipts]==[r["role"] for r in manifest["files"]],
      "complete current-input receipt order differs")
  byrole={r["role"]:r for r in receipts}
  for role in set(manifest["mathematical_input_roles"])|set(SCIENTIFIC_ROLES):
    require(byrole.get(role)=={k:files[role][k] for k in keys},
        "retained or remaining scientific input identity differs: "+role)
  for r in receipts:
    require(set(r)==set(keys) and isinstance(r["role"],str)
        and type(r["bytes"]) is int and 0<r["bytes"]<100000
        and hex_string(r["sha256"],64) and hex_string(r["git_blob_sha"],40),
        "invalid complete retained current receipt")
    relpath(r["path"])
  for role,spec in files.items():
    if not spec["read_as_json"]:continue
    path=root/relpath(spec["path"]);checked(path,spec["bytes"],spec["sha256"])
    raws[role]=path.read_bytes();docs[role]=exact_json(raws[role])
    by_path[spec["path"]]=role
  role=manifest["_resolved_output_contract"]["retained_prefix_contract_role"]
  require(role=="recovery_contract" and role in manifest["mathematical_input_roles"]
      and docs[role].get("kind")=="exact_preserved_WEJ_prefix_continuation_contract_v1",
      "one complete frozen continuation contract required")
  contract=docs[role];old=docs["prior_manifest"]
  index=docs["prior_index"];execution=docs["prior_execution"]
  for role,key in (("prior_index","original_index"),("prior_execution","original_execution"),
          ("prior_manifest","original_manifest")):
    require({k:files[role][k] for k in keys[1:]}==contract[key],
        "the original failed execution identity differs")
  require(set(index)==set(INDEX_FIELDS)
      and index["kind"]=="complete_global_genuine_waist_error_posterior_v1"
      and index["complete"] is False and index["proved"] is False
      and type(index["actual_returncode"]) is int and index["actual_returncode"]==1
      and index["stage"]=="preserved_failure"
      and index["active_node"]==REMAINING_NODE_NAMES[0],
      "the complete original index lost its exact partial status")
  pairs=(("run_id","original_run_id"),("run_attempt","original_run_attempt"),
   ("workflow_event_commit","original_workflow_event_commit"),
   ("actual_scientific_checkout_commit","actual_scientific_checkout_commit"),
   ("failure","original_failure"),("gates","complete_original_gate_array"),
   ("locked_attempted_nodes","complete_original_attempted_node_locks"),
   ("node_receipts","complete_original_node_receipts"),
   ("parameters","complete_original_parameters"),
   ("mathematical_input_sha256","complete_original_mathematical_input_sha256"),
   ("scientific_module_sha256","complete_original_scientific_module_sha256"),
   ("retained_scope","scope"))
  require(all(json_equal(index[k],contract[v]) for k,v in pairs),
      "an original complete status, gate, binding, parameter or scope changed")
  require(len(index["gates"])==27 and all(g["passed"] is True for g in index["gates"])
      and len(index["node_receipts"])==23 and len(index["locked_attempted_nodes"])==24
      and index["parameters_sha256"]==hashlib.sha256(compact(index["parameters"])).hexdigest()
      and json_equal(index["parameters"],old["parameters"])
      and index["input_manifest_sha256"]==files["prior_manifest"]["sha256"]
      and index["source_sha256"]==old["source_sha256"]
      and index["runtime"]==manifest["scientific_runtime"] and index["arithmetic_bits"]==320,
      "incomplete original identity and parameter chain")
  oldreceipts=[{**{k:s[k] for k in keys},"origin":"exact_current_small_text"} for s in old["files"]]
  require(execution["actual_original_Git_input_receipts"]==oldreceipts
      and execution["actual_verified_Git_input_count"]==len(oldreceipts)
      and execution["actual_verified_Git_input_receipts_sha256"]==
        hashlib.sha256(compact(oldreceipts)).hexdigest(),
      "the full original Git-input receipt chain differs")
  require(execution["complete"] is False and execution["actual_returncode"]==1
      and type(execution["actual_returncode"]) is int
      and execution["actual_new_scientific_processes"]==1
      and execution["scientific_child_launch_attempted"] is True
      and execution["complete_original_input_receipt_available"] is True
      and execution["complete_mathematical_receipt_available"] is False
      and execution["automatic_scientific_retry_authorized"] is False,
      "original failure qualifications were changed")
  for a,b in (("run_id","run_id"),("run_attempt","run_attempt"),
    ("workflow_commit","workflow_event_commit"),
    ("actual_scientific_checkout_commit","actual_scientific_checkout_commit"),
    ("source_sha256","source_sha256"),("input_manifest_sha256","input_manifest_sha256"),
    ("actual_scientific_runtime","runtime"),("parameters","parameters"),
    ("mathematical_input_sha256","mathematical_input_sha256"),
    ("scientific_module_sha256","scientific_module_sha256"),("actual_failure","failure"),
    ("locked_attempted_nodes_read_verbatim","locked_attempted_nodes")):
    require(json_equal(execution[a],index[b]),"original execution/index mismatch: "+a)
  oldraw={}
  for ref in contract["all_original_published_scientific_file_receipts"]:
    role=by_path[ref["path"]];raw=raws[role]
    require(len(raw)==ref["bytes"] and hashlib.sha256(raw).hexdigest()==ref["sha256"],
        "one whole original scientific file differs")
    oldraw[ref["file"]]=raw
  refs=[{"file":n,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()} for n,raw in oldraw.items()]
  require(execution["scientific_files"]==refs
      and execution["scientific_index"]==refs[0]
      and execution["complete_original_input_files"]==index["original_input_files"],
      "the original execution does not bind every published file")
  old_byrole={r["role"]:{k:r[k] for k in keys} for r in oldreceipts}
  core=docs[by_path[next(s["path"] for s in old["files"]
            if s["role"]=="posterior_admission_contract")]]
  require(core["kind"]=="complete_WEJ_original_actual_admission_contract_v1"
      and [s["role"] for s in core["original_actual_inputs"]]==old["old_actual_input_roles"]
      and len(core["original_actual_inputs"])==12
      and sum(s["gate_count"] for s in core["original_actual_inputs"])==212
      and sum(len(s["exact_checks"]) for s in core["original_actual_inputs"])==280
      and len(core["consumed_original_records"])==19
      and len(core["complete_old_conclusions"])==15,"prior admission counts differ")
  bindings={}
  for spec in core["original_actual_inputs"]:
    role=spec["role"];outer=docs[role];science=at(outer,spec["scientific_root"])
    require(byrole[role]==old_byrole[role],"original full-file receipt differs")
    require(isinstance(outer,dict) and sorted(outer)==spec["outer_keys"]
        and isinstance(science,dict) and sorted(science)==spec["scientific_keys"],
        "prior full schema mismatch: "+role)
    fields=[]
    for check in spec["exact_checks"]:
      value=at(outer,check["path"])
      require(json_equal(value,check["value"]),"prior identity or domain mismatch: "+role)
      fields.append({"path":check["path"],"value":value})
    gates=at(outer,spec["gates_path"]) if spec["gates_path"] is not None else []
    require(len(gates)==spec["gate_count"]
        and (spec["gates_path"] is None or
          (json_equal(gates,spec["complete_original_gates"])
           and all(g.get("passed") is True for g in gates))),
        "prior gate mismatch: "+role)
    bindings[role]={"original_file":old_byrole[role],"scientific_root":spec["scientific_root"],
     "complete_original_gates":gates,"complete_exact_identity_and_domain_fields":fields,
     "outer_schema_retained":True,"scientific_schema_retained":True,
     "original_complete_file_remains_at_immutable_public_identity":True}
  originals={}
  for spec in core["consumed_original_records"]:
    value=at(docs[spec["role"]],spec["path"])
    require(json_equal(value,spec["original_value"])
        and (value if isinstance(value,str) else value["ball"])==spec["ball_string"],
        "prior complete record changed")
    originals[spec["name"]]=value
  conclusions={spec["name"]:{"role":spec["role"],"path":spec["path"],
    "complete_value":at(docs[spec["role"]],spec["path"])}
    for spec in core["complete_old_conclusions"]}
  expected_admission={
   "kind":"complete_WEJ_original_actual_input_admission_v1","complete":True,
   "original_file_count":12,"complete_original_actual_bindings":bindings,
   "complete_current_file_receipts":[old_byrole[r["role"]] for r in oldreceipts],
   "complete_scientific_parameter_contract":old["parameters"],
   "read_only_scope":"complete immutable current files; zero historical restoration and zero old producer calls",
   "same_selected_real_member_only":True,"WGS_geometry_and_amplitudes_are_sup_not_A0":True,
   "strict_d_A0_has_its_independent_original_Banach_product_and_primitive_proof":True,
   "all_old_successes_and_original_failure_qualifications_retained":True}
  expected_consumed={
   "kind":"complete_WEJ_consumed_original_conclusions_v1","complete":True,
   "complete_original_consumed_record_objects":originals,"complete_old_conclusions":conclusions,
   "complete_WGS_original_files":{r:old_byrole[r] for r in ("WGS_main","WGS_original_inputs")},
   "WGS_full_graphs_read_from_their_complete_immutable_original_files":True,
   "WGS_437_slots_and_all_66_plus_40_original_records_not_recomputed":True,
   "no_partial_or_truncated_source_conclusion_substituted":True,
   "all_false_scope_flags_in_selected_complete_conclusions_retained":True}
  require(json_equal(exact_json(oldraw["original-inputs-admission.json"]),expected_admission)
      and json_equal(exact_json(oldraw["original-inputs-consumed-conclusions.json"]),
             expected_consumed),"full original admission or consumed document differs")
  node_refs={};slots=0;events=0
  for spec,ref in zip(old["ordered_node_specs"][:23],index["node_receipts"]):
    name=spec["node_name"];filename=spec["relative_path"];payload=exact_json(oldraw[filename])
    receipt={"file":filename,"bytes":len(oldraw[filename]),
        "sha256":hashlib.sha256(oldraw[filename]).hexdigest()}
    binding={"problem_id":old["problem_id"]+"/"+name,
      "parameters_sha256":index["parameters_sha256"],
      "mathematical_input_sha256":index["mathematical_input_sha256"],
      "scientific_module_sha256":index["scientific_module_sha256"],
      "direct_dependency_receipts":{n:node_refs[n] for n in spec["dependency_names"]}}
    require(ref=={"node_name":name,**receipt} and set(payload)==COMPLETE_NODE_FIELDS
        and payload["kind"]==ENVELOPE_KIND and payload["node_name"]==name
        and payload["binding"]==binding and payload["complete"] is True
        and payload["failure"] is None and payload["automatic_retry_authorized"] is False
        and payload["all_printed_records_in_complete_conclusion"] is True
        and type(payload["printed_record_event_count"]) is int
        and payload["printed_record_event_count"]==
          {"mean_gamma_bridge":8,"same_angular_J_local":19,"negative_reception":32}.get(
            name,spec["record_count"]),
        "a completed original node or original dependency binding changed")
    schema=docs[by_path[next(s["path"] for s in old["files"] if s["role"]==spec["schema_role"])]]
    shape=schema["complete_conclusion_shapes"][spec["conclusion_shape_key"]]
    require(full_shape(payload["conclusion"],shape)
        and ball_count(payload["conclusion"])==spec["record_count"],
        "one complete original scientific graph lost a field or record")
    node_refs[name]=receipt;slots+=spec["record_count"];events+=payload["printed_record_event_count"]
  require(slots==1609 and events==1600
      and index["actual_progress"]==[{"node_name":r["node_name"],"complete_file_saved":True}
                     for r in index["node_receipts"]],
      "original complete node or event count differs")
  sv=execution["scientific_validation"]
  require(sv=={"complete":False,"original_inputs_valid":True,"index_valid":True,
      "complete_node_receipts":node_refs,"partial_nodes":[REMAINING_NODE_NAMES[0]],"errors":[]},
      "the complete original validation outcome changed")
  descriptor=docs["prior_partial_descriptor"]
  partial_raw=reconstruct_partial_envelope("graphs/"+REMAINING_NODE_NAMES[0]+".json",
                       descriptor,oldraw)
  partial=exact_json(partial_raw)
  require(len(partial_raw)==13563 and hashlib.sha256(partial_raw).hexdigest()==
        contract["exact_preserved_prefix"]["original_partial_sha256"],
      "the exact failed prefix was not losslessly reconstructed")
  spec=old["ordered_node_specs"][23]
  require(partial["binding"]=={"problem_id":old["problem_id"]+"/"+spec["node_name"],
    "parameters_sha256":index["parameters_sha256"],
    "mathematical_input_sha256":index["mathematical_input_sha256"],
    "scientific_module_sha256":index["scientific_module_sha256"],
    "direct_dependency_receipts":{n:node_refs[n] for n in spec["dependency_names"]}},
    "the original partial dependency binding changed")
  prefix=partial["explicit_math_prefix"]["complete_scientific_document_prefix"]
  saved_events=partial["printed_record_events"]
  require(ball_count(prefix)==39 and len(saved_events)==39 and prefix["complete"] is False
      and partial["conclusion"] is None,
      "the whole 39-record prefix qualification differs")
  strings=[]
  def collect(value):
    if finite_record(value):strings.append(value["ball"])
    elif isinstance(value,dict):
      for item in value.values():collect(item)
    elif isinstance(value,list):
      for item in value:collect(item)
  collect(prefix)
  require(all(set(e)=={"direction","record"} and e["direction"] in ("upper","lower")
        and finite_record(e["record"]) for e in saved_events)
      and sorted(strings)==sorted(e["record"]["ball"] for e in saved_events),
      "one complete saved partial record or direction was lost")
  for path in contract["all_39_preserved_record_paths"]:
    value=prefix
    for key in path:
      if isinstance(value,list):
        require(isinstance(key,str) and key.isdigit() and int(key)<len(value),
            "invalid retained array record index")
        key=int(key)
      value=value[key]
    require(finite_record(value),"one original saved record path disappeared")
  phase=docs["WGS_main"]["complete_strict_geometry_conclusion"]["complete_jets"]["phase_derivatives"]
  cert=docs["WGS_main"]["complete_derivative_request_certificate"]
  require(phase["shape"]==[15,3] and phase["value_omitted_for_lift"] is True
      and phase["group_upper"][0] is None and cert["fixed_degree_groups"][2]==[2,2],
      "the paid phase derivative qualification changed")
  phase_records={"phase_second_normalized_upper":phase["group_upper"][2],
    "phase_first_lower":docs["WGS_main"]["complete_higher_flow_and_cut_conclusion"]["strict_phase_lower"],
    "derivative_multi_index":[0,2],"ordinary_derivative_factorial":2,"lift_value_omitted":True}
  require(finite_record(phase_records["phase_second_normalized_upper"])
      and finite_record(phase_records["phase_first_lower"]),"missing complete paid derivative records")
  return ({"kind":"complete_WEJ_retained_prefix_input_admission_v1","complete":True,
    "complete_current_file_receipts":receipts,"complete_original_failed_index":index,
    "complete_original_failed_execution_file":byrole["prior_execution"],
    "complete_original_partial_envelope":partial,
    "complete_phase_derivative_record_qualification":phase_records,
    "preserved_record_counts":RETAINED_RECORD_COUNTS,
    "complete_scientific_parameter_contract":manifest["parameters"],
    "retained_scope":manifest["retained_scope"],
    "all_completed_records_are_read_verbatim":True,
    "all_old_successes_and_failed_prefix_qualifications_retained":True,
    "no_completed_target_reevaluated":True},)

def read_scientific_files(directory,manifest):
  """Read every available declared file; defer all format failures until preservation."""
  directory=Path(directory);raws={};documents={};errors=[];extra={}
  names=[name for name in declared_caps(manifest) if name not in ("report.md","execution.json")]
  for name in names:
    path=directory/safe_name(name)
    if not path.exists():continue
    if path.is_symlink() or not path.is_file():
      errors.append({"file":name,"type":"NonregularScientificFile",
             "message":"declared scientific path is not a regular file"})
      continue
    raw=path.read_bytes();raws[name]=raw
    try:
      doc=exact_json(raw)
      require(isinstance(doc,dict),"scientific top-level JSON must be an object")
      require(raw==compact(doc),"complete scientific bytes are not canonical JSON plus LF")
      documents[name]=doc
    except (ValueError,TypeError,UnicodeError) as error:
      errors.append({"file":name,"type":type(error).__name__,"message":str(error)})
  # An interrupted atomic replacement is additional preserved stdout evidence.
  # It never replaces the last complete/partial node and is never auto-executed.
  for name in names:
    path=directory/(name+".partial")
    if path.is_file() and not path.is_symlink():
      extra[name+".partial"]=path.read_bytes()
  if (directory/"graphs").is_dir():
    allowed={str(Path(n).name) for n in names if n.startswith("graphs/")}
    for path in sorted((directory/"graphs").iterdir()):
      if path.name not in allowed and path.name not in {v+".partial" for v in allowed}:
        errors.append({"file":"graphs/"+path.name,"type":"UndeclaredScientificFile",
               "message":"graph filename is not in the frozen complete list"})
        if path.is_file() and not path.is_symlink():
          extra["graphs/"+path.name]=path.read_bytes()
  physical=dict(raws);descriptors=[];used_parts=set()
  for spec in manifest["ordered_node_specs"]:
    name=spec["relative_path"];doc=documents.get(name)
    if isinstance(doc,dict) and doc.get("kind")==PARTIAL_DESCRIPTOR_KIND:
      try:
        restored=reconstruct_partial_envelope(name,doc,physical)
        raws[name]=restored;documents[name]=exact_json(restored)
        descriptors.append(doc)
        for ref in doc["complete_field_files"].values():
          if ref is not None:used_parts.add(ref["file"])
      except (KeyError,TypeError,ValueError,IndexError,UnicodeError) as error:
        errors.append({"file":name,"type":type(error).__name__,"message":str(error)})
  for name in PARTIAL_FIELD_FILES.values():
    if name in physical and name not in used_parts:
      errors.append({"file":name,"type":"UnboundPartialField",
             "message":"partial projection is not bound by its exact descriptor"})
    raws.pop(name,None);documents.pop(name,None)
  if len(descriptors)>1:
    errors.append({"file":"partial-node-*","type":"MultiplePartialNodes",
           "message":"one stopped scientific attempt may have only one split partial"})
  return {"raw":raws,"physical_raw":physical,"documents":documents,
      "parse_errors":errors,"extra_raw":extra,"source_partial_descriptors":descriptors}

def file_reference(bundle,name):
  raw=bundle["raw"][name]
  return {"file":name,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}

def node_valid(payload,spec,manifest,dependency_receipts):
  originals,modules=expected_pins(manifest)
  expected_binding={
   "problem_id":manifest["problem_id"]+"/"+spec["node_name"],
   "parameters_sha256":hashlib.sha256(compact(manifest["parameters"])).hexdigest(),
   "mathematical_input_sha256":originals,"scientific_module_sha256":modules,
   "direct_dependency_receipts":dependency_receipts}
  require(isinstance(payload,dict) and payload.get("kind")==ENVELOPE_KIND
      and payload.get("node_name")==spec["node_name"]
      and payload.get("binding")==expected_binding,
      "complete scientific node binding differs")
  require(set(payload["binding"])==BINDING_FIELDS
      and payload.get("automatic_retry_authorized") is False,
      "node binding or no-repeat contract changed")
  if payload.get("complete") is True:
    require(set(payload)==COMPLETE_NODE_FIELDS and payload["failure"] is None
        and payload["all_printed_records_in_complete_conclusion"] is True
        and type(payload["printed_record_event_count"]) is int
        and payload["printed_record_event_count"]==spec["printed_record_event_count"],
        "complete atomic-node envelope differs")
    require(full_shape(payload["conclusion"],spec["conclusion_shape"]),
        "complete scientific conclusion shape or fixed literal differs")
    require(ball_count(payload["conclusion"])==spec["record_count"],
        "complete scientific record count differs")
    return True
  require(payload.get("complete") is False and set(payload)==PARTIAL_NODE_FIELDS,
      "partial atomic-node envelope differs")
  events=payload["printed_record_events"]
  require(isinstance(events,list),"partial record journal missing")
  for event in events:
    require(isinstance(event,dict) and set(event)=={"direction","record"}
        and event["direction"] in ("upper","lower") and finite_record(event["record"]),
        "partial record journal lost a complete typed record")
  require(payload["conclusion"] is None or isinstance(payload["conclusion"],dict),
      "returned partial scientific document must be retained in full")
  require(payload["explicit_math_prefix"] is None
      or isinstance(payload["explicit_math_prefix"],dict),
      "explicit mathematical prefix must be a complete JSON object")
  failure=payload["failure"]
  require(failure is None or (isinstance(failure,dict)
      and isinstance(failure.get("type"),str)
      and isinstance(failure.get("message"),str)),
      "partial scientific diagnostic differs")
  return False

def validate_scientific_bundle(bundle,manifest,root,execution):
  """Independent JSON/binding checks only; no imports of scientific modules."""
  docs=bundle["documents"];specs=manifest["ordered_node_specs"]
  names=[s["node_name"] for s in specs]
  originals,modules=expected_pins(manifest)
  valid_nodes={};partial_nodes=[];errors=list(bundle["parse_errors"])
  for spec in specs:
    name=spec["node_name"];filename=spec["relative_path"]
    if filename not in docs:continue
    try:
      deps={}
      for dep in spec["dependency_names"]:
        require(dep in valid_nodes,"a saved graph depends on an unvalidated predecessor")
        deps[dep]=valid_nodes[dep]
      if node_valid(docs[filename],spec,manifest,deps):
        valid_nodes[name]=file_reference(bundle,filename)
      else:partial_nodes.append(name)
    except (KeyError,TypeError,ValueError,IndexError) as error:
      errors.append({"file":filename,"type":type(error).__name__,"message":str(error)})
  originals_valid=False
  try:
    expected=complete_expected_original_documents(root,manifest,
          execution.get("actual_original_Git_input_receipts",[]))
    require(all(json_equal(docs.get(name),value) for name,value in zip(ORIGINAL_FILENAMES,expected)),
        "complete original-admission documents differ from the actual inputs")
    originals_valid=True
  except (KeyError,TypeError,ValueError,IndexError) as error:
    errors.append({"file":"retained-prefix-admission.json","type":type(error).__name__,"message":str(error)})
  index=docs.get("index.json");index_valid=False;complete=False
  try:
    require(isinstance(index,dict) and set(index)==set(INDEX_FIELDS),
        "complete posterior index schema differs")
    require(index["kind"]==INDEX_KIND and index["public_repository"]==PUBLIC,
        "different complete posterior kind or repository")
    shape=manifest["_resolved_output_contract"][
      "complete_index_shape" if index.get("complete") is True else "partial_index_shape"]
    require(full_shape(index,shape),"complete frozen index template differs")
    require(index["source_sha256"]==modules["remaining_pipeline"]
        and index["scientific_module_sha256"]==modules
        and index["mathematical_input_sha256"]==originals
        and json_equal(index["parameters"],manifest["parameters"])
        and index["parameters_sha256"]==hashlib.sha256(compact(manifest["parameters"])).hexdigest()
        and index["runtime"]==manifest["scientific_runtime"]
        and index["arithmetic_bits"]==320
        and json_equal(index["retained_scope"],manifest["retained_scope"]),
        "posterior identity, runtime, parameter or retained scope differs")
    require(index["run_id"]==execution.get("run_id")
        and index["run_attempt"]==execution.get("run_attempt")
        and index["source_sha256"]==execution.get("source_sha256")
        and index["input_manifest_sha256"]==execution.get("input_manifest_sha256")
        and index["workflow_event_commit"]==execution.get("workflow_commit")
        and index["actual_scientific_checkout_commit"]==
          execution.get("actual_scientific_checkout_commit"),
        "index is not bound to this exact scientific execution")
    if "scientific_files" in execution:
      actual_refs=[{"file":name,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}
        for name,raw in bundle.get("physical_raw",bundle["raw"]).items()]
      require(execution["scientific_files"]==actual_refs
          and execution.get("scientific_index")==file_reference(bundle,"index.json"),
          "prior execution does not bind all actual published scientific file bytes")
    require(hex_string(index["input_manifest_sha256"],64)
        and hex_string(index["workflow_event_commit"],40)
        and hex_string(index["actual_scientific_checkout_commit"],40),
        "incomplete manifest or checkout identity")
    require(index["old_scientific_calls"]==0 and type(index["old_scientific_calls"]) is int
        and index["old_binary_parts_restored"]==0
        and index["new_reproducible_arrays_persisted"] is False
        and index["new_artifacts"]==0 and index["new_Releases"]==0,
        "old calculations, binary restoration or artifact persistence occurred")
    expected_gates=manifest["_resolved_output_contract"]["complete_index_shape"]["gates"]
    require(isinstance(expected_gates,list) and len(expected_gates)==9
        and all(isinstance(g,dict) and set(g)=={"name","passed"}
            and isinstance(g["name"],str) and g["passed"] is True
            for g in expected_gates)
        and expected_gates[4:7]==[{"name":"complete natural scientific node "+n,
                    "passed":True} for n in names],
        "the four admission, three new-node and two final gates differ")
    gates=index["gates"]
    require(isinstance(gates,list) and gates==expected_gates[:len(gates)],
        "saved structural gates are not the complete ordered prefix")
    locked=index["locked_attempted_nodes"]
    require(isinstance(locked,list) and locked==names[:len(locked)],
        "attempted-node lock is not the original unique order")
    require(index["active_node"] is None or
        (bool(locked) and index["active_node"]==locked[-1]),
        "active scientific node differs from the last locked attempt")
    require((set(valid_nodes)|set(partial_nodes))<=set(locked),
        "saved scientific node was not locked before evaluation")
    require(len(partial_nodes)<=1
        and (not partial_nodes or partial_nodes[0]==locked[-1]),
        "multiple or reordered partial scientific targets")
    refs=index["node_receipts"]
    require(isinstance(refs,list) and len(refs)<=len(names),
        "saved node reference list is missing")
    expected_refs=[{"node_name":n,**valid_nodes[n]} for n in names if n in valid_nodes]
    require(refs==expected_refs[:len(refs)],"node receipts do not bind complete actual bytes")
    expected_progress=[{"node_name":r["node_name"],"complete_file_saved":True} for r in refs]
    require(index["actual_progress"]==expected_progress,
        "actual scientific progress differs from saved complete receipts")
    origrefs=index["original_input_files"]
    available_orig=[file_reference(bundle,n) for n in ORIGINAL_FILENAMES if n in bundle["raw"]]
    require(isinstance(origrefs,list) and origrefs==available_orig[:len(origrefs)],
        "original-input references do not bind complete actual bytes")
    elapsed=index["actual_mathematical_wall_seconds"]
    require(elapsed is None or (finite_number(elapsed) and elapsed>=0),
        "invalid actual mathematical wall time")
    require(type(index["complete"]) is bool and type(index["proved"]) is bool,
        "missing true completion state")
    if index["complete"] is True:
      require(index["proved"] is True and type(index["actual_returncode"]) is int
          and index["actual_returncode"]==0 and index["failure"] is None
          and index["stage"]=="complete" and index["active_node"] is None
          and locked==names and refs==expected_refs and len(refs)==len(specs)
          and len(valid_nodes)==len(specs) and not partial_nodes
          and origrefs==available_orig and len(origrefs)==1
          and gates==expected_gates and len(gates)==9
          and elapsed is not None and originals_valid and not errors,
          "the whole posterior lacks its complete successful scientific evidence")
      complete=True
    else:
      require(index["proved"] is False and index["actual_returncode"] in (None,1)
          and (index["failure"] is None or isinstance(index["failure"],dict)),
          "incomplete posterior was promoted to a proof")
    index_valid=True
  except (KeyError,TypeError,ValueError,IndexError) as error:
    errors.append({"file":"index.json","type":type(error).__name__,"message":str(error)})
  return {"complete":complete,"original_inputs_valid":originals_valid,
      "index_valid":index_valid,"complete_node_receipts":valid_nodes,
      "partial_nodes":partial_nodes,"errors":errors}

def same_mathematical_target(index_or_execution,manifest):
  originals,modules=expected_pins(manifest)
  value=index_or_execution or {}
  return (value.get("mathematical_input_sha256")==originals
      and value.get("parameters")==manifest["parameters"]
      and (value.get("kind")==INDEX_KIND or
        value.get("scientific_problem_id")==manifest["problem_id"]))


def render(state,bundle,validation,manifest):
  complete=validation.get("complete") is True
  admitted=validation.get("original_inputs_valid") is True
  index=bundle["documents"].get("index.json",{})
  nodes=validation.get("complete_node_receipts",{})
  partial=set(validation.get("partial_nodes",[]))
  lines=["# Actual remaining-only genuine waist-error completion","",
    ("All 30 new records and three complete conclusions are admitted." if complete else
    "Preserved execution; the remaining-only conclusion is not admitted."),
    "The original 23 nodes and 39-record prefix remain unchanged.","",
    "## Execution","","| Item | Recorded value |","|---|---|"]
  for key,value in (
   ("Run / attempt",str(state["run_id"])+"/"+str(state["run_attempt"])),
   ("Workflow event",state["workflow_commit"]),
   ("Scientific checkout",state.get("actual_scientific_checkout_commit","not launched")),
   ("Source SHA256",state["source_sha256"]),("Manifest SHA256",state["input_manifest_sha256"]),
   ("Complete mathematics",complete),("Retained input admission",admitted),
   ("Child return code",state.get("actual_returncode")),
   ("New scientific children",state["actual_new_scientific_processes"]),
   ("Complete nodes",str(len(nodes))+"/3"),("Old restores / scientific calls","0 / 0")):
    lines.append("| "+cell(key)+" | "+cell(value)+" |")
  if complete:
    whole=bundle["documents"]["graphs/complete_same_physical_whole_and_reduced_error.json"]["conclusion"]
    lines+=["","## Complete new bounds","","| Retained record | Outward value |","|---|---|"]
    for key,value in whole["complete_new_records"].items():
      lines.append("| "+cell(key)+" | "+cell(ball(value))+" |")
  lines+=["","## Node inventory","","| Node | Saved state | Complete / new records |","|---|---|---|"]
  for spec in manifest["ordered_node_specs"]:
    name=spec["node_name"]
    status=("complete and validated" if name in nodes else "partial; locked" if name in partial
        else "retained; validation incomplete" if spec["relative_path"] in bundle["raw"]
        else "not produced")
    count=(str(spec["record_count"])+"/"+str(spec["printed_record_event_count"])
       if name in nodes else "—")
    lines.append("| "+cell(name)+" | "+status+" | "+count+" |")
  lines+=["","## Scope and evidence","",
    "The selected member, cutoff 97, both signs, all 3070 interfaces and full physical mean feedback retain their original scope. Whole and reduced errors remain distinct. Finite columns, parameter rows, two mean coordinates and the infinite radial head remain unpaid.",
    "No passing high cutoff, finite Schur inverse, full incoming inverse, nonlinear background or final surface is certified.",
    "All gates, progress and hashes: [index.json](index.json). Complete failed index, reconstructed prefix, original records and current receipts: [retained-prefix-admission.json](retained-prefix-admission.json).",
    "Every available file is printed and hashed before format gates. Full operational and README history: [execution.json](execution.json)."]
  checks=state.get("readme_checks",[])
  lines+=["","Latest actual pulls ("+str(len(checks))+" total):"]
  for check in checks[-2:]:lines.append("- "+cell(check["time"])+" -> "+cell(check["after"]))
  failure=state.get("actual_failure") or index.get("failure")
  if failure is not None or validation.get("errors"):
    text=json.dumps(failure or validation["errors"][0],sort_keys=True,ensure_ascii=False)
    lines+=["","## Preserved diagnostic","",cell(text[:256])+
        (" [excerpt; full diagnostic remains saved]" if len(text)>256 else ""),
        "Saved complete or partial mathematics never authorizes an automatic retry."]
  return "\n".join(lines)+"\n"

def emit_prepublication(state,bundle,validation,manifest):
  """Print every complete available payload before any size or publication gate."""
  caps=declared_caps(manifest)
  raws=dict(bundle.get("publication_raw",bundle.get("physical_raw",bundle["raw"])))
  raws["report.md"]=render(state,bundle,validation,manifest).encode("utf-8")
  raws["execution.json"]=compact(state)
  receipts={};oversized=[]
  for filename,limit in caps.items():
    raw=raws.get(filename);available=raw is not None
    receipt={"available":available,"bytes":None if raw is None else len(raw),
        "sha256":None if raw is None else hashlib.sha256(raw).hexdigest(),
        "limit_bytes":limit}
    receipts[filename]=receipt
    print(json.dumps({"marker":"WEJ_COMPLETE_PREPUBLICATION_FILE_V1",
       "filename":filename,"run_id":state["run_id"],"run_attempt":state["run_attempt"],
       **receipt},sort_keys=True,separators=(",",":")),flush=True)
    if available:
      print("BEGIN_COMPLETE_WEJ_PREPUBLICATION_FILE "+filename,flush=True)
      sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
      if not raw.endswith(b"\n"):print("",flush=True)
      print("END_COMPLETE_WEJ_PREPUBLICATION_FILE "+filename,flush=True)
      if len(raw)>limit or len(raw)>=100000:oversized.append(filename)
  for filename,raw in bundle["extra_raw"].items():
    print(json.dumps({"marker":"WEJ_ADDITIONAL_INTERRUPTED_FILE_V1","filename":filename,
       "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),
       "published":False},sort_keys=True,separators=(",",":")),flush=True)
    print("BEGIN_COMPLETE_WEJ_INTERRUPTED_FILE "+filename,flush=True)
    sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
    if not raw.endswith(b"\n"):print("",flush=True)
    print("END_COMPLETE_WEJ_INTERRUPTED_FILE "+filename,flush=True)
  print(json.dumps({"marker":"WEJ_COMPLETE_PREPUBLICATION_STATUS_V1",
    "complete_mathematics":validation.get("complete") is True,
    "complete_original_inputs":validation.get("original_inputs_valid") is True,
    "declared_file_count":len(caps),"all_available_files_separately_printed":True,
    "oversized_files":oversized},sort_keys=True,separators=(",",":")),flush=True)
  require(not oversized,
      "all complete payloads were printed; per-file publication limit failed: "+",".join(oversized))
  return {"files":receipts,"every_available_payload_preserved_in_full":True,
    "all_payloads_are_separate_files":True,"before_any_git_publication":True,
    "execution_payload_precedes_this_recoverable_metadata_field":True,
    "additional_interrupted_files_printed":len(bundle["extra_raw"])}


def accept_live_rules(root,git,initial,manifest,state):
  relative=relpath(manifest["operational_live_review_index"])
  index_path=root/relative
  if not index_path.is_file() or index_path.stat().st_size>60000:
    raise ValueError("the explicit operational live review index is absent or too large")
  index=read(index_path);policy=initial["large_data_policy"]
  if (index.get("kind")!="explicit_live_review_index_for_unchanged_public_execution_rules"
    or index.get("repository")!=PUBLIC or index.get("execution_policy")!=policy
    or index.get("new_or_changed_operational_rules_require_new_worker_review") is not True
    or index.get("unread_README_revisions_are_not_accepted") is not True):
    raise ValueError("the live index attempted to change an execution policy")
  current={name:sha(root/name) for name in initial["readme_sha256"]}
  matching=[v for v in index.get("accepted_reviews",[]) if v.get("readme_sha256")==current]
  if not matching:
    raise RuntimeError("new unread README revision requires its actual diff and a root review")
  for record in matching:
    name=relpath(record["path"]);path=root/name
    checked(path,record["bytes"],record["sha256"])
    review=read(path);commit=record.get("read_commit")
    if (not isinstance(commit,str) or len(commit)!=40
      or any(c not in "0123456789abcdef" for c in commit)
      or record.get("all_operational_rules_unchanged") is not True
      or record.get("scientific_input_manifests_and_sources_not_changed") is not True
      or review.get("repository")!=PUBLIC or review.get("read_commit")!=commit
      or review.get("readme_sha256")!=current
      or review.get("large_data_policy")!=policy
      or review.get("scientific_input_manifests_and_sources_not_changed") is not True
      or review.get("new_unread_rules_must_still_be_reported_and_applied") is not True):
      raise ValueError("a live review did not retain the exact unchanged execution policy")
    if git("cat-file","-e",commit+"^{commit}",check=False).returncode:
      git("fetch","--filter=blob:none","--no-tags","origin",commit)
    for readme,digest in current.items():
      text=git("show",commit+":"+readme).stdout
      if hashlib.sha256(text.encode("utf-8")).hexdigest()!=digest:
        raise ValueError("the separately read commit does not contain the exact current README")
    receipt=dict(path=str(name),bytes=record["bytes"],sha256=record["sha256"],
      read_commit=commit,readme_sha256=current,actual_review_commit_README_bytes_verified=True,
      all_operational_rules_unchanged=True)
    state.setdefault("accepted_live_rule_versions",[])
    if receipt not in state["accepted_live_rule_versions"]:
      state["accepted_live_rule_versions"].append(receipt)
    state["actual_reviewed_readme_sha256"]=current
    state["live_review_index"]=dict(path=str(relative),bytes=index_path.stat().st_size,
      sha256=sha(index_path),observed_at_commit=git("rev-parse","HEAD").stdout.strip())
    return receipt
  raise RuntimeError("no valid explicitly reviewed current README exists")




def main():
  parser=argparse.ArgumentParser(description=__doc__)
  parser.add_argument("--mode",choices=("hydrate","run"),required=True)
  parser.add_argument("--manifest",type=Path,required=True)
  parser.add_argument("--manifest-sha",required=True)
  parser.add_argument("--pipeline-sha",required=True)
  parser.add_argument("--rules",type=Path,required=True)
  parser.add_argument("--rules-sha",required=True)
  parser.add_argument("--work",type=Path)
  parser.add_argument("--out-dir",type=Path)
  a=parser.parse_args()
  if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
    raise RuntimeError("only this public Actions repository may run remaining mathematics")
  root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
  a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
  require(sha(a.manifest)==a.manifest_sha and sha(a.rules)==a.rules_sha,
      "manifest/rules pin changed")
  m=exact_json(a.manifest.read_bytes());rules=exact_json(a.rules.read_bytes())
  rm=a.manifest.relative_to(root);rr=a.rules.relative_to(root)
  rw=Path(__file__).resolve().relative_to(root);ws=sha(__file__)
  pipeline,reports,caps=validate_contract(root,m,a.pipeline_sha,rw,ws,rr,a.rules_sha,
                     resolve_shapes=a.mode=="run")
  require(rules.get("repository")==PUBLIC,"different reviewed public repository")
  for key in ("reproducible_data_persisted_in_repository","reproducible_data_persisted_in_Releases",
        "new_reproducible_Actions_output_uploads"):
    require(rules["large_data_policy"].get(key) is False,
        "the current complete rule15 policy is required")
  gb=["git","-c","safe.directory="+str(root)]
  if a.mode=="hydrate":
    paths={str(pipeline),str(rw),str(rm),str(rr),str(reports)+"/"}|set(rules["readme_sha256"])
    paths.update(entry["path"] for entry in m["files"])
    paths.add(m["operational_live_review_index"])
    paths.add(str(TOPIC/"notes")+"/*reviewed-public-CI-rules*.json")
    subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
      input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
    print("Hydrated the full frozen current-only closure and live rule reviews. No mathematical target was called.",flush=True)
    return
  require(a.work is not None and a.out_dir is not None,
      "temporary work/output paths required")
  work=a.work.resolve();out=a.out_dir.resolve()
  if work.exists() or out.exists():
    raise FileExistsError("preserve any complete or partial attempt")
  require(not any(v.is_relative_to(root) for v in (work,out))
      and work!=out and not work.is_relative_to(out) and not out.is_relative_to(work),
      "work/output must be disjoint and outside Git")
  work.mkdir(parents=True);out.mkdir(parents=True)
  original_pins,module_pins=expected_pins(m)
  state=dict(kind="actual_public_global_genuine_waist_error_completion_execution_v1",
    repository=PUBLIC,run_id=os.environ["GITHUB_RUN_ID"],
    run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
    workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
    source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
    scientific_problem_id=m["problem_id"],parameters=m["parameters"],
    mathematical_input_sha256=original_pins,scientific_module_sha256=module_pins,
    reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
    started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
    actual_new_scientific_processes=0,old_successful_scientific_targets_recomputed=0,
    old_completed_scalar_products_recomputed=0,old_producers_or_integrals_reexecuted=0,
    old_binary_parts_restored=0,old_artifacts_downloaded=0,
    old_scientific_calls=0,new_artifact_count=0,new_Release_count=0,
    reproducible_data_published_to_repository=False,
    new_per_row_arrays_retained_after_job=False,final_topic_complete=False,
    automatic_scientific_retry_authorized=False)
  report=root/reports/("run-"+state["run_id"]+"-"+state["run_attempt"])
  owned_caps={str((report/name).relative_to(root)):limit for name,limit in caps.items()}
  env=os.environ.copy();token=env.pop("GITHUB_TOKEN")
  env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="1",
    GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
    GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+token).encode()).decode())
  def git(*args,check=True,stdout=None):
    result=subprocess.run(gb+list(args),cwd=root,env=env,text=stdout is None,
      stdout=subprocess.PIPE if stdout is None else stdout,stderr=subprocess.PIPE,timeout=900)
    if check and result.returncode:
      err=result.stderr if isinstance(result.stderr,str) else result.stderr.decode("utf-8","replace")
      raise RuntimeError("public Git "+str(args[0])+" failed: "+err[:1200])
    return result
  latest_blobs={}
  def sync():
    nonlocal latest_blobs
    before=git("rev-parse","HEAD").stdout.strip()
    git("pull","--rebase","origin","main")
    after=git("rev-parse","origin/main").stdout.strip()
    diff=git("diff",before,after,"--",*rules["readme_sha256"]).stdout
    state["readme_checks"].append(dict(time=utc(),before=before,after=after,actual_diff=diff,
      explicitly_reviewed_commit=rules["read_commit"]))
    save(out/"worker-process.json",state)
    try:
      review=accept_live_rules(root,git,rules,m,state)
    except Exception:
      print(diff,flush=True);raise
    state["readme_checks"][-1].update(accepted_review_sha256=review["sha256"],
      separately_read_rules_commit=review["read_commit"])
    if sha(a.rules)!=a.rules_sha or sha(a.manifest)!=a.manifest_sha or sha(root/pipeline)!=a.pipeline_sha:
      raise ValueError("source/manifest/rules changed during pull")
    if sha(root/rw)!=ws:
      raise ValueError("running worker pin changed")
    for spec in m["files"]:
      if sha(root/relpath(spec["path"]))!=spec["sha256"]:
        raise ValueError("current input pin changed")
    published,blobs=topic_tree_metadata(git,TOPIC,PUBLIC)
    latest_blobs=blobs
    capacity=owned_head_delta(git,root,published,blobs,owned_caps)
    state.update(current_published_topic_capacity_metadata=published,
      current_topic_capacity_metadata=capacity,current_topic_blob_bytes=capacity["blob_bytes"],
      current_topic_blob_count=capacity["blob_count"],current_topic_metadata_commit=capacity["commit"],
      current_topic_below_200000000_bytes=capacity["blob_bytes"]<200000000)
    save(out/"worker-process.json",state)
    if ("finished_mathematical_stage_utc" not in state
        and capacity["blob_bytes"]+m["publication_limits"]["reserved_publication_bytes"]>=200000000):
      raise ValueError("missing 120000-byte reserve before mathematics finishes")
  last_checkpoint=time.monotonic()
  child=None
  def metadata_event(error,healthy):
    event=dict(time=utc(),type=type(error).__name__,message=str(error),
      healthy_child_preserved=healthy,completed_child_not_repeated=not healthy,
      publication_deferred_without_stale_capacity=True)
    previous=state.get("metadata_retry_event_chain_sha256","0"*64)
    state["metadata_retry_event_chain_sha256"]=hashlib.sha256(
      bytes.fromhex(previous)+compact(event)).hexdigest()
    state["metadata_retry_event_count"]=state.get("metadata_retry_event_count",0)+1
    state.setdefault("last_read_only_metadata_retry_events",[]).append(event)
    state["last_read_only_metadata_retry_events"]=state["last_read_only_metadata_retry_events"][-12:]
    state["metadata_publication_retry_pending"]=True
    save(out/"worker-process.json",state)
    print(json.dumps(dict(kind="WEJ_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
      full_event_count=state["metadata_retry_event_count"],
      full_event_chain_sha256=state["metadata_retry_event_chain_sha256"])),flush=True)
  def checkpoint(force=False):
    nonlocal last_checkpoint
    interval=60 if state.get("metadata_publication_retry_pending") else 600
    if force or time.monotonic()-last_checkpoint>=interval:
      try:
        # True pull, live README review and every frozen pin precede
        # the only retryable operation: a read-only metadata request.
        sync()
        state["metadata_publication_retry_pending"]=False
      except TransientMetadataError as error:
        if child is None or child.poll() is not None:raise
        metadata_event(error,True)
      last_checkpoint=time.monotonic()
  def copy_current(entry):
    name=relpath(entry["path"]);src=root/name;dst=work/name
    if name.suffix not in (".py",".md",".json") or not 0<entry["bytes"]<100000:
      raise ValueError("input must be complete current text")
    checked(src,entry["bytes"],entry["sha256"])
    raw=src.read_bytes();raw.decode("utf-8")
    if hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()!=entry["git_blob_sha"]:
      raise ValueError("input Git blob mismatch")
    dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
    checked(dst,entry["bytes"],entry["sha256"])
    return dst,dict(role=entry["role"],path=str(name),bytes=entry["bytes"],
      sha256=entry["sha256"],git_blob_sha=entry["git_blob_sha"],
      origin="exact_current_small_text")
  bundle=read_scientific_files(out,m)
  validation={"complete":False,"original_inputs_valid":False,"index_valid":False,
        "complete_node_receipts":{},"partial_nodes":[],"errors":[]}
  runtime=None
  try:
    git("config","user.name","github-actions[bot]")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    sync();last_checkpoint=time.monotonic()
    runtime={"Python":sys.version.split()[0],
        "python_flint":importlib.metadata.version("python-flint")}
    state["actual_scientific_runtime"]=runtime
    require(runtime==m["scientific_runtime"],"exact Python and directed runtime differ before reuse")
    # Inspect complete and partial files before hydrating temporary scientific
    # work or launching a child. A changed wrapper cannot repeat old mathematics.
    parent=root/reports
    if parent.is_dir():
      for previous_dir in sorted(path for path in parent.iterdir() if path.is_dir()):
        prior_exec_path=previous_dir/"execution.json"
        previous=None
        if prior_exec_path.is_file():
          require(prior_exec_path.stat().st_size<100000,
              "prior execution exceeds small-text limit")
          previous=exact_json(prior_exec_path.read_bytes())
        prior=read_scientific_files(previous_dir,m)
        prior_index=prior["documents"].get("index.json")
        matching=(same_mathematical_target(previous,m)
             or same_mathematical_target(prior_index,m))
        if matching:
          if previous is not None:
            old_validation=validate_scientific_bundle(prior,m,root,previous)
            if old_validation["complete"] is True:
              print(json.dumps({
                "reused_complete_same_scientific_index":str((previous_dir/"index.json").relative_to(root)),
                "original_run_id":previous["run_id"],
                "original_run_attempt":previous["run_attempt"],
                "complete_scientific_files":[file_reference(prior,name) for name in prior["raw"]],
                "original_execution_sha256":sha(prior_exec_path),
                "new_scientific_processes":0,"old_successful_mathematics_recomputed":0,
                "all_complete_node_bindings_and_original_documents_validated":True},
                sort_keys=True,separators=(",",":")),flush=True)
              return
          if (prior["raw"] or previous is None
            or previous.get("scientific_child_launch_attempted") is True
            or previous.get("actual_new_scientific_processes",0)>0):
            raise RuntimeError("same target has scientific evidence; preserve it; explicit recovery required")
        # A node or atomic index can outlive an interrupted wrapper. Its
        # mathematical binding independently locks that target as well.
        for spec in m["ordered_node_specs"]:
          payload=prior["documents"].get(spec["relative_path"])
          binding=(payload.get("binding") or
              payload.get("original_envelope_fields",{}).get("binding",{})) if isinstance(payload,dict) else {}
          if (binding.get("problem_id")==m["problem_id"]+"/"+spec["node_name"]
            and binding.get("mathematical_input_sha256")==original_pins
            and binding.get("parameters_sha256")==
              hashlib.sha256(compact(m["parameters"])).hexdigest()):
            raise RuntimeError("complete/partial node already exists; no automatic repetition")
    require(state["run_attempt"]=="1",
        "Actions rerun cannot start mathematics")
    planned=m["complete_publication_static_budget"]["maximum_total_bytes"]
    capacity=state["current_topic_capacity_metadata"]
    current_owned={name:latest_blobs[name]["bytes"] for name in owned_caps if name in latest_blobs}
    for change in capacity["owned_local_delta"]:
      if change["status"]=="D":current_owned.pop(change["path"],None)
      else:current_owned[change["path"]]=change["head_bytes"]
    planned_total=capacity["blob_bytes"]-sum(current_owned.values())+planned
    state["complete_static_publication_budget_check"]={
      "file_count":len(caps),"planned_complete_file_bytes":planned,
      "exact_existing_owned_bytes_replaced":sum(current_owned.values()),
      "base_topic_blob_bytes":capacity["blob_bytes"],
      "projected_topic_blob_bytes":planned_total,
      "all_declared_complete_files_counted":True,
      "static_budget_sha256":hashlib.sha256(compact(m["complete_publication_static_budget"])).hexdigest()}
    save(out/"worker-process.json",state)
    require(planned_total<200000000,"the complete static publication budget does not fit the actual topic")
    inputs=[];index_files={}
    for entry in m["files"]:
      dst,receipt=copy_current(entry);inputs.append(receipt)
      index_files[entry["role"]]=dict(path=str(dst),bytes=dst.stat().st_size,sha256=entry["sha256"])
      checkpoint()
    state["actual_original_Git_input_receipts"]=inputs
    state["actual_verified_Git_input_count"]=len(inputs)
    state["actual_verified_Git_input_receipts_sha256"]=hashlib.sha256(compact(inputs)).hexdigest()
    tm=work/rm;tm.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.manifest,tm)
    checked(tm,a.manifest.stat().st_size,a.manifest_sha)
    tr=work/rr;tr.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.rules,tr)
    checked(tr,a.rules.stat().st_size,a.rules_sha)
    parsed=[]
    for entry in m["files"]:
      if entry["path"].endswith(".py"):
        source=work/relpath(entry["path"]);ast.parse(source.read_text(),filename=str(source))
        parsed.append(dict(path=entry["path"],sha256=entry["sha256"]))
    state.update(complete_immutable_Python_AST_closure_passed=True,
      complete_immutable_Python_AST_file_count=len(parsed),
      complete_immutable_Python_AST_inventory_sha256=hashlib.sha256(compact(parsed)).hexdigest())
    require(len(inputs)==m["expected_input_count"]
        and len(parsed)==m["expected_immutable_AST_files"],
        "current input/AST closure differs")
    require(m["historical_inputs"]==[] and state["old_binary_parts_restored"]==0,
        "no old binary restoration is authorized")
    cmd=[sys.executable,"-u",str(work/pipeline),"--repo",str(work),
      "--manifest",str(tm),"--manifest-sha",a.manifest_sha,"--bits","320",
      "--out-dir",str(out)]
    for role,digest in {**original_pins,**module_pins}.items():
      require(index_files[role]["sha256"]==digest,"one complete scientific input identity changed")
    state["command_sha256"]=hashlib.sha256(compact(cmd)).hexdigest()
    state["actual_scientific_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
    state["scientific_child_launch_attempted"]=True
    save(out/"worker-process.json",state)
    ce=os.environ.copy();ce["ACTUAL_CHECKOUT_COMMIT"]=state["actual_scientific_checkout_commit"]
    for key in ("GITHUB_TOKEN","GH_TOKEN"):ce.pop(key,None)
    started=time.monotonic();timeout=m["new_scientific_timeout_seconds"]
    require(type(timeout) is int and timeout==18000,"different reviewed scientific timeout")
    logpath=out/"new-scientific-child.stdout.log"
    with logpath.open("wb") as log:
      child=subprocess.Popen(cmd,cwd=work,env=ce,stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,start_new_session=True,bufsize=0)
      state["actual_new_scientific_processes"]=1
      save(out/"worker-process.json",state)
      fd=child.stdout.fileno();os.set_blocking(fd,False)
      eof=False
      while not eof:
        ready,_,_=select.select([fd],[],[],1)
        if ready:
          raw=os.read(fd,1<<16)
          if raw:
            log.write(raw);log.flush()
            sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
          else:eof=True
        if child.poll() is None and time.monotonic()-started>timeout:
          state["timeout_seconds"]=timeout
          os.killpg(child.pid,signal.SIGTERM)
          try:child.wait(timeout=15)
          except subprocess.TimeoutExpired:
            os.killpg(child.pid,signal.SIGKILL);child.wait()
        checkpoint()
        if child.poll() is not None and not ready:
          raw=os.read(fd,1<<16)
          if raw:
            log.write(raw);log.flush()
            sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
          else:eof=True
      child.wait();state["actual_returncode"]=child.returncode
      state["complete_child_stdout_tee"]=True
    state["new_scientific_child_wall_seconds"]=time.monotonic()-started
    bundle=read_scientific_files(out,m)
    validation=validate_scientific_bundle(bundle,m,root,state)
    state["complete_original_input_receipt_available"]=validation["original_inputs_valid"]
    state["complete_mathematical_receipt_available"]=validation["complete"]
    state["complete"]=bool(child.returncode==0 and validation["complete"])
    index=bundle["documents"].get("index.json",{})
    state["actual_failure"]=None if state["complete"] else (
      index.get("failure") or {"type":"IncompleteScientificReceipt",
        "message":"complete remaining files/inputs/index did not validate"})
  except BaseException as error:
    if child is not None and child.poll() is None:
      os.killpg(child.pid,signal.SIGTERM)
      try:child.wait(timeout=15)
      except subprocess.TimeoutExpired:
        os.killpg(child.pid,signal.SIGKILL);child.wait()
    if child is not None:state["actual_returncode"]=child.poll()
    state["actual_failure"]={"type":type(error).__name__,"message":str(error)}
    bundle=read_scientific_files(out,m)
    validation=validate_scientific_bundle(bundle,m,root,state)
    state["complete_original_input_receipt_available"]=validation["original_inputs_valid"]
    state["complete_mathematical_receipt_available"]=validation["complete"]
    state["complete"]=False
  state["finished_mathematical_stage_utc"]=utc()
  if child is not None and not state.get("complete_child_stdout_tee"):
    with (out/"new-scientific-child.stdout.log").open("ab") as log:
      stop=time.monotonic()+10
      while time.monotonic()<stop:
        ready,_,_=select.select([child.stdout.fileno()],[],[],1)
        if not ready:continue
        raw=os.read(child.stdout.fileno(),1<<16)
        if not raw:
          state["complete_child_stdout_tee"]=True;break
        log.write(raw);log.flush();sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
  # Reprint the complete final state of every declared file independently of
  # whether a later schema, size, capacity or Git publication gate succeeds.
  for filename,raw in bundle["raw"].items():
    print(json.dumps({"kind":"WEJ_ATOMIC_SCIENTIFIC_FILE_REPRINT",**file_reference(bundle,filename)},
            sort_keys=True,separators=(",",":")),flush=True)
    print("BEGIN_COMPLETE_WEJ_ATOMIC_FILE "+filename,flush=True)
    sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
    if not raw.endswith(b"\n"):print("",flush=True)
    print("END_COMPLETE_WEJ_ATOMIC_FILE "+filename,flush=True)
  state["complete_atomic_scientific_files_reprinted"]=True
  state["scientific_validation"]=validation
  publication_raw=prepare_publication_files(bundle,m)
  state["scientific_files"]=[{"file":name,"bytes":len(raw),
    "sha256":hashlib.sha256(raw).hexdigest()} for name,raw in publication_raw.items()]
  state["lossless_partial_envelope_projections"]=bundle["split_partial_descriptors"]
  state["original_partial_envelopes_printed_before_projection"]=True
  logpath=out/"new-scientific-child.stdout.log"
  if logpath.is_file():state["complete_child_stdout_receipt"]=rec(logpath,out)
  state["scientific_index"]=(
    file_reference(bundle,"index.json") if "index.json" in bundle["raw"] else None)
  state["complete_original_input_files"]=[
    file_reference(bundle,n) for n in ORIGINAL_FILENAMES if n in bundle["raw"]]
  state["declared_publication_file_count"]=len(caps)
  state["locked_attempted_nodes_read_verbatim"]=(
    bundle["documents"].get("index.json",{}).get("locked_attempted_nodes",[]))
  save(out/"worker-process.json",state)
  state["recoverable_prepublication_stdout"]=emit_prepublication(state,bundle,validation,m)
  save(out/"worker-process.json",state)
  report.mkdir(parents=True,exist_ok=True)
  def snapshot():
    text=render(state,bundle,validation,m)
    names=sorted(owned_caps)
    capacity,blobs=topic_tree_metadata(git,TOPIC,PUBLIC)
    state["publication_owned_HEAD_delta"]=owned_head_delta(
      git,root,capacity,blobs,owned_caps)
    total=capacity["blob_bytes"]
    oldbytes=sum(blobs[name]["bytes"] for name in names if name in blobs)
    state.update(publication_capacity_metadata=capacity,
      publication_base_topic_blob_bytes=total,
      publication_capacity_metadata_commit=capacity["commit"],
      projected_topic_blob_bytes=0)
    science_bytes=sum(len(raw) for raw in publication_raw.values())
    while True:
      raw_state=compact(state)
      projected=total-oldbytes+science_bytes+len(text.encode("utf-8"))+len(raw_state)
      if projected==state["projected_topic_blob_bytes"]:break
      state["projected_topic_blob_bytes"]=projected
    require(projected<200000000,
        "actual publication exceeds topic capacity")
    require(len(raw_state)<=caps["execution.json"] and
        len(text.encode("utf-8"))<=caps["report.md"],
        "complete payloads are in stdout; report/execution cap failed")
    for filename,raw in publication_raw.items():
      raw.decode("utf-8")
      require(filename in caps and len(raw)<=caps[filename] and len(raw)<100000,
          "scientific file exceeds publication cap")
    # Only the declared files may enter this run's directory.
    for path in report.rglob("*"):
      if path.is_file():
        require(str(path.relative_to(root)) in owned_caps,
            "report path outside frozen list")
    for filename,raw in publication_raw.items():
      target=report/safe_name(filename)
      target.parent.mkdir(parents=True,exist_ok=True)
      target.write_bytes(raw)
    (report/"report.md").write_text(text,encoding="utf-8")
    (report/"execution.json").write_bytes(raw_state)
  def publish():
    snapshot();owned=str(report.relative_to(root))
    git("add","--sparse","--",owned)
    staged=git("diff","--cached","--name-only","-z").stdout
    require(all(name in owned_caps for name in staged.split("\0") if name),
        "only declared run files may be committed")
    if git("diff","--cached","--quiet","--",owned,check=False).returncode!=0:
      git("commit","-m","visible-exact: retain exact-prefix remaining waist conclusions")
    while True:
      result=git("push","origin","HEAD:refs/heads/main",check=False)
      if result.returncode==0:return owned
      if not any(v in result.stderr for v in
           ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
        raise RuntimeError("publication failed outside concurrent rebase")
      sync();snapshot();git("add","--sparse","--",owned)
      git("commit","--amend","--no-edit")
  publication_retry_start=time.monotonic()
  while True:
    try:
      sync();state["metadata_publication_retry_pending"]=False
      owned=publish()
      break
    except TransientMetadataError as error:
      metadata_event(error,False)
      if time.monotonic()-publication_retry_start>600:raise
      time.sleep(10)
  print(json.dumps({"complete":state["complete"],"actual_returncode":state["actual_returncode"],
    "report":owned,"actual_new_scientific_processes":state["actual_new_scientific_processes"],
    "old_successful_mathematics_recomputed":0,"old_binary_parts_restored":0,
    "new_artifacts":0,"new_Releases":0,"new_numerical_arrays_retained":False,
    "all_available_declared_scientific_files_published_in_full":True},
    sort_keys=True,separators=(",",":")),flush=True)
  if not state["complete"]:raise SystemExit(1)


if __name__=="__main__":
  main()
