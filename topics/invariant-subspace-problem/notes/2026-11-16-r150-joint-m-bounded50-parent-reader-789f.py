#!/usr/bin/env python3
"""Read and verify the independently rebuilt true16 parent; never mutate it.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
This bridge does not identify high-p coordinates merely from their mod31 matrix.
All target controls and new targets must use this same fresh parent binding.
"""
from __future__ import annotations
import hashlib,json,struct,importlib.util
from pathlib import Path
REBUILD_NAME="2026-11-16-r150-joint-m-true16-source-rebuild-p9-bounded50-789f.py"
REBUILD_SHA="07cd9a2c6d09c9efc11be8aba50cbdd5bceba6f058f1fab986f6a1017a150d87"
REBUILD_BYTES=38621
FORMAT="r150-joint-m-selected-true16-parent-p9-precision50-v1"
OLD_BINDING="712f9b426017d3f63c05e755a314e14d79ac03d22bce6a4b3f943efcd80d7093"
U16_SHA="679132fd4727fd305b77c82beb5d3f2e002df1860045200c3392158ab8eb48b9"
J16_SHA="59d09cbeec71ebf7cda6f12ddd21c1b7ffe1c83a3f9de81b776df0a97df687d8"
INDICES={"L3":list(range(8)),"L4":list(range(6,13)),"L5":[10,11,12],"L6":[12]}
SHAPES={"L3":(8,50,45,3,[0]),"L4":(7,45,40,4,[0,1,2,3]),"L5":(3,40,35,5,[0,1]),"L6":(1,35,30,6,[0])}
CLASS_NAMES={"L3":"L3-selected8-paid-class-check","L4":"L4-selected7-paid-class-check",
 "L5":"L5-selected3-paid-class-check","L6":"L6-selected1-complete-class"}
GV={"G":(26397022,"ef9976aca179c382c4bf265b362e56280ea725aea16e164e8d29d5759bd92202",24),
 "V":(55688902,"ed02ca487853bff3a9f117b2e3c749c0cf5c9897bb4bb9d4dd53184ee0597d5a",28)}
def check(ok,message):
 if not ok:raise ValueError(message)
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)+"\n").encode("ascii")
def sha(data):return hashlib.sha256(data).hexdigest()
def identity(path):
 h=hashlib.sha256()
 with path.open("rb") as f:
  for block in iter(lambda:f.read(1048576),b""):h.update(block)
 return {"bytes":path.stat().st_size,"sha256":h.hexdigest()}
def local(root,name):
 p=Path(name);check(not p.is_absolute() and ".." not in p.parts,"parent paths must stay inside its output directory")
 path=root/p;check(path.resolve().is_relative_to(root.resolve()),"resolved parent path escapes its directory")
 return path
def require_record(path,record,label):
 got=identity(path);check(got=={k:record[k] for k in ("bytes","sha256")},"actual fresh parent file identity "+label);return got
def load_parent(root,notes_root,expected_inputs,helper_records):
 root=Path(root)
 source=Path(notes_root)/REBUILD_NAME
 check(identity(source)=={"bytes":REBUILD_BYTES,"sha256":REBUILD_SHA},"frozen minimal true16 rebuilding source")
 rp=root/"selected-true16-source-rebuild-receipt.json";pp=root/"selected-true16-parent.json"
 receipt=json.loads(rp.read_bytes());pack=json.loads(pp.read_bytes())
 check(receipt["format"]=="r150-joint-m-true16-selected-source-rebuild-p9-bounded50-v1" and receipt["status"]=="completed","actually completed selected-column rebuilding")
 check(pack["format"]==FORMAT and pack["status"]=="completed","actually completed selected-column parent pack")
 sem=receipt["parameters"]["inputIdentity"];binding=sha(canonical(sem))
 check(receipt["binding"]==pack["binding"]==binding and sem["driver"]==identity(source),"fresh parent mathematical binding")
 check(sem["format"]==receipt["format"] and sem["paidFull210Binding"]==OLD_BINDING
       and sem["originalSelectedIndices"]==INDICES and sem["precisionChain"]==[50,45,40,35,30],"exact selected dependency closure")
 require_record(pp,receipt["parameters"]["parentPack"],"parent pack")
 check(pack["sourceSHA256"]==REBUILD_SHA and pack["full210OriginalTheoremBinding"]==OLD_BINDING
       and pack["complete210Recomputed"] is False and pack["originalSelectedIndices"]==INDICES
       and pack["precisionChain"]==[50,45,40,35,30],"no false full210 rerun or ancestor identity")
 check(pack["sources"]==sem["sources"] and pack["inputs"]==sem["inputs"],"pack and completed receipt use the same sources and inputs")
 for key,value in pack["sources"].items():
  check(helper_records.get(key)==value,"same frozen original mathematical helper "+key)
 for key,value in pack["inputs"].items():
  check(expected_inputs.get(key)==value,"same exact original input "+key)
 stages=receipt["parameters"]["stages"]
 check(len(stages)==30 and all(d["status"]=="completed" and d.get("exitCode")==0 for d in stages.values()),"all30 original rebuilding stages actually completed with actual exit zero")
 for flag in ("allOriginalIntegerCarriesVerified","allLowerPaid315ClassesMatched","all104LocalFreeChecks",
              "all505GlobalFreeChecks","samePaid25PrefixAndComplete50OriginalGAndV","canonicalOriginalColumnRecipesPreserved"):
  check(pack.get(flag) is True,"completed parent gate "+flag)
 check(pack["trueBasisIdentities"]==receipt["parameters"]["trueBasisIdentities"]
       and pack["trueBasisIdentities"]["true16"]=={"rows":315,"columns":16,"sha256":U16_SHA}
       and pack["trueBasisIdentities"]["parameterAction16"]=={"rows":16,"columns":16,"sha256":J16_SHA},
       "same complete residue basis and original parameter action")
 contract={"binding":binding};classes={};input_pins={"selected-parent-receipt":identity(rp),"selected-parent-pack":identity(pp)}
 spec=importlib.util.spec_from_file_location("r150_joint_b_parent_source",source);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
 for key,(size,oldsha,offset) in GV.items():
  d=pack["constantCaches"][key];path=local(root,d["path"]);got=require_record(path,d,key)
  prefix=base.paid_gv_prefix(path,key,binding)
  check(all(d.get(k)==v for k,v in prefix.items()),"same complete50 cache and paid25 mathematical prefix "+key)
  contract[key]=d;input_pins["parent-"+key]=got
 for key,(n,L,valid,e,indices) in SHAPES.items():
  d=pack["sourceFamilies"][key];path=local(root,d["path"]);got=require_record(path,d,key)
  check((d["labels"],d["L"],d["valid"],d["e"],d["indices"])==(n,L,valid,e,indices)
        and d["originalIndices"]==INDICES[key],"exact selected original source positions "+key)
  with path.open("rb") as f:
   fixed=f.read(100);labs=list(struct.unpack("<%dH"%n,f.read(2*n)));exps=list(f.read(n))
  check(fixed[:8]==b"R150SJ91" and struct.unpack_from("<IQ4I",fixed,8)==(31,26439622160671,6188,n,L,2)
        and fixed[36:100]==binding.encode("ascii") and labs==d["sourceLabels"] and exps==[e]*n,
        "fresh original source header, labels and exact divisor orders "+key)
  check(got["bytes"]==100+3*n+6188*(15+8*L*n),"complete original source length "+key)
  contract[key]=d;input_pins["parent-"+key]=got
  cd=pack["classes"][key];cp=local(root,cd["path"]);require_record(cp,cd,key+" class")
  c=json.loads(cp.read_bytes());rows=c["matrixRows"]
  check(c["binding"]==binding and len(rows)==315 and all(len(row)==n for row in rows)
        and all(type(x) is int and 0<=x<31 for row in rows for x in row),"whole315 class dimensions and coefficients "+key)
  matrix={"rows":315,"columns":n,"sha256":sha(bytes(x for row in rows for x in row))}
  check(matrix==cd["matrix"]==c["matrix"]==receipt["parameters"]["comparisons"][CLASS_NAMES[key]]["matrix"],
        "complete original class identity "+key)
  check(c["sourceLabels"]==labs and all(c.get(flag) is True for flag in
        ("all104LocalFreeChecks","all315OriginalCoordinateReconstruction","all505GlobalFreeChecks","sameOriginalSAction")),
        "complete original free and parameter-action gates "+key)
  if key!="L6":check(c.get("matchesPaidClass") is True,"actual comparison to paid lower original class "+key)
  classes[key]=c;input_pins["parent-"+key+"-class"]=identity(cp)
 return contract,pack,classes,input_pins

