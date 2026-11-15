"""The one byte-preserving migration of run43675967042's28 successful stages.

Pure standard-library provenance only. No numerical stage is evaluated here.
Every original header remains original. This is not a general cross-source resume.
"""
from __future__ import annotations
import ast
import copy
import gzip
import hashlib
import json
from pathlib import Path

PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
SCI=TOPIC/"scripts/fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources.py"
ALG=TOPIC/"scripts/fourfold_codazzi_adjacent_piece_correlated_Airy_algebra.py"
CI=TOPIC/"scripts/fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources_CI.py"
BASE=TOPIC/"notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43675967042-1"
ARCHIVE=TOPIC/"notes/adjacent_piece_scalar_coercion_inputs"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
OLD_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
OLD_ALGEBRA="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
OLD_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
OLD_NATIVE="b46953d23b021359d1f98a55e820a28d2cfbce5fe2f7b93e3841d47fe0fe6d35"
OLD_PROCESS="da9445d1a11f4d956a949b36fbfb45a7a417f0465c66208a09e141170b79e573"
OLD_PUBLICATION="e1944e1f94564ba0aa4c2fb3ad5bdaab5506f9c6c8484c97e31732eee3c24017"
FAILURE=dict(type="AttributeError",message="'int' object has no attribute 'upper'")
ORIGINAL_INPUTS={
 "scalar_coercion_previous_native":(BASE/"consumers/correlated-adjacent-piece-first-Airy-sources.json.gz",24929,OLD_NATIVE),
 "scalar_coercion_previous_process":(BASE/"consumers/process.json",5410,OLD_PROCESS),
 "scalar_coercion_previous_publication":(BASE/"publication.json",10445,OLD_PUBLICATION),
 "scalar_coercion_previous_source":(ARCHIVE/"original-scientific-source.py",51519,OLD_SOURCE),
 "scalar_coercion_previous_algebra":(ARCHIVE/"original-algebra.py",24469,OLD_ALGEBRA),
 "scalar_coercion_previous_manifest":(ARCHIVE/"original-input-manifest.json",83150,OLD_MANIFEST),
}
EXPECTED_NAMES={
 "complete-original-reference-holomorphic-majorants",
 "complete-root-bstar-polynomial-norms-at-one-thirtytwo",
 "exact-signed-cubic-difference-2548",
 "same-intrinsic-root15-and-third-tail-2548",
}
for _key in ("A","G","Q","T","Xp","a0","b0","chi"):
    for _width in ("3-512","5-256"):
        EXPECTED_NAMES.add("reference-Fourier-norms-"+_key+"-"+_width)
for _key in ("F0","F1","f0","f1","Z0","Z1","w1a","w1b"):
    EXPECTED_NAMES.add("reference-Fourier-norms-"+_key+"-3-512")
assert len(EXPECTED_NAMES)==28

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def _kind(name):
    if name=="complete-original-reference-holomorphic-majorants":return "new_piece_comparison_stages"
    if name=="exact-signed-cubic-difference-2548":return "new_exact_cubic_difference_stages"
    if name=="same-intrinsic-root15-and-third-tail-2548":return "new_intrinsic_consumption_stages"
    return "new_reference_coefficient_norm_stages"
def _functions(text):
    tree=ast.parse(text)
    return {node.name:ast.dump(node,include_attributes=False) for node in ast.walk(tree)
            if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef))}

def load_policy(repo,manifest):
    """Verify the six exact records,28 original byte receipts and unchanged builders."""
    repo=Path(repo)
    pins={v["path"]:v for v in manifest["files"]}
    if len(pins)!=len(manifest["files"]):
        raise ValueError("the immutable scientific manifest contains duplicate paths")
    docs={};locations={}
    for key,(relative,size,expected) in ORIGINAL_INPUTS.items():
        if manifest["input_paths"].get(key)!=str(relative):
            raise ValueError("the unique scalar-coercion predecessor path changed: "+key)
        pin=dict(path=str(relative),bytes=size,sha256=expected)
        if pins.get(str(relative))!=pin:
            raise ValueError("the unique scalar-coercion predecessor pin changed: "+key)
        path=repo/relative
        if not path.is_file() or path.stat().st_size!=size or sha(path)!=expected:
            raise ValueError("the unique original scalar-coercion record changed: "+key)
        locations[key]=path
        if key.endswith(("_native","_process","_publication","_manifest")):docs[key]=read(path)
    native=docs["scalar_coercion_previous_native"];process=docs["scalar_coercion_previous_process"]
    publication=docs["scalar_coercion_previous_publication"];old_manifest=docs["scalar_coercion_previous_manifest"]
    expected=dict(source_sha256=OLD_SOURCE,input_manifest_sha256=OLD_MANIFEST,
                  algebra_sha256=OLD_ALGEBRA,runtime=RUNTIME)
    if (any(native.get(k)!=v for k,v in expected.items())
        or native.get("run_id")!="43675967042" or native.get("run_attempt")!="1"
        or native.get("public_repository")!=PUBLIC
        or native.get("complete") is not False or native.get("proved") is not False
        or native.get("failure")!=FAILURE or native.get("cases") or native.get("case_stages")
        or native.get("pieces") or len(native.get("gates",[]))!=10
        or not all(v.get("passed") is True for v in native["gates"])):
        raise ValueError("the original28-stage failure boundary changed")
    if (process.get("run_id")!="43675967042" or process.get("run_attempt")!="1"
        or process.get("actual_returncode")!=1 or process.get("native_sha256")!=OLD_NATIVE
        or process.get("native_bytes")!=24929 or process.get("mathematical_source_sha256")!=OLD_SOURCE
        or process.get("manifest_sha256")!=OLD_MANIFEST or process.get("algebra_sha256")!=OLD_ALGEBRA
        or process.get("mathematical_failure")!=FAILURE
        or process.get("mathematical_gates")!=native["gates"]
        or process.get("complete_natural_stage_inventory",{}).get("complete_scalar_stage_count")!=28
        or process.get("complete_natural_stage_inventory",{}).get("complete_case_count")!=0):
        raise ValueError("the original successful prefix lacks its exact actual failed-child receipt")
    if (publication.get("repository")!=PUBLIC or publication.get("run_id")!="43675967042"
        or publication.get("actual_returncode")!=1 or publication.get("complete") is not False):
        raise ValueError("the original mathematical failure publication changed")
    original_files={v["file"]:v for v in publication["files"]}
    for key in ("scalar_coercion_previous_native","scalar_coercion_previous_process"):
        rel=str(locations[key].relative_to(repo/BASE));entry=original_files.get(rel,{})
        if entry.get("sha256")!=sha(locations[key]) or entry.get("bytes")!=locations[key].stat().st_size:
            raise ValueError("the original published native or process lost its exact byte receipt")
    live={str(SCI),str(ALG),str(CI)}
    for pin in old_manifest["files"]:
        if pin["path"] not in live and pins.get(pin["path"])!=pin:
            raise ValueError("an unchanged original mathematical input moved during the scalar coercion repair")
    if (manifest.get("external_completed_natives")!=old_manifest.get("external_completed_natives")
        or any(manifest["input_paths"].get(k)!=v for k,v in old_manifest["input_paths"].items())):
        raise ValueError("an original complete case or input role changed during prefix migration")
    old_helper=locations["scalar_coercion_previous_algebra"].read_text()
    new_helper=(repo/ALG).read_text()
    old_line="def up(v):return abs(v).upper()"
    new_line="def up(v):\n    if isinstance(v,(int,Q)):v=ex(v)\n    return abs(v).upper()"
    if old_helper.count(old_line)!=1 or new_helper!=old_helper.replace(old_line,new_line):
        raise ValueError("the helper change exceeds exact int/Fraction coercion")
    old_source=locations["scalar_coercion_previous_source"].read_text();new_source=(repo/SCI).read_text()
    assignments=lambda text:[ast.dump(node,include_attributes=False) for node in ast.parse(text).body
        if isinstance(node,(ast.Assign,ast.AnnAssign))]
    if assignments(old_source)!=assignments(new_source):
        raise ValueError("an accepted original parameter or source constant changed")
    before=_functions(old_source);after=_functions(new_source)
    unchanged=("pack","unpack","dyadic","exact_cubic_at","exact_cubic_difference",
        "cubic_difference_jets","reference_majorants","joint_coefficient_norms",
        "complete_reference","complete_radius_augmented","source_row")
    if any(name not in before or name not in after or before[name]!=after[name] for name in unchanged):
        raise ValueError("an accepted mathematical builder changed during the exact scalar repair")
    if set(native.get("stages",{}))!=EXPECTED_NAMES:
        raise ValueError("the predecessor is not precisely the28 accepted original stages")
    entries={};paths={};kinds={}
    for name,entry in native["stages"].items():
        relative=Path("stages")/(name+".json.gz")
        if entry.get("file")!=str(relative) or entry.get("stage_kind")!=_kind(name):
            raise ValueError("a whitelisted original stage changed its name or scientific role")
        path=locations["scalar_coercion_previous_native"].parent/relative
        pin=dict(path=str(path.relative_to(repo)),bytes=entry["bytes"],sha256=entry["sha256"])
        original=original_files.get("consumers/"+str(relative),{})
        if (pins.get(pin["path"])!=pin or original.get("sha256")!=entry["sha256"]
            or original.get("bytes")!=entry["bytes"] or not path.is_file()
            or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]):
            raise ValueError("a whitelisted old stage lacks identical manifest, publication and actual bytes")
        value=read(path)
        if (any(value.get(k)!=v for k,v in expected.items())
            or value.get("name")!=name or value.get("stage")!=name or value.get("complete") is not True
            or value.get("stage_kind")!=_kind(name)
            or value.get("payload_sha256")!=digest(value.get("payload"))):
            raise ValueError("an original successful scalar stage changed its header or payload")
        entries[name]=copy.deepcopy(entry);paths[name]=str(path)
        kinds[_kind(name)]=kinds.get(_kind(name),0)+1
    if kinds!={"new_piece_comparison_stages":1,"new_reference_coefficient_norm_stages":25,
               "new_exact_cubic_difference_stages":1,"new_intrinsic_consumption_stages":1}:
        raise ValueError("the exact original successful mathematical scope changed")
    receipt=dict(run_id="43675967042",run_attempt="1",native_sha256=OLD_NATIVE,process_sha256=OLD_PROCESS,
        publication_sha256=OLD_PUBLICATION,source_sha256=OLD_SOURCE,algebra_sha256=OLD_ALGEBRA,
        input_manifest_sha256=OLD_MANIFEST,runtime=copy.deepcopy(RUNTIME),
        complete_original_stage_count=28,original_stage_headers_and_payloads_unchanged=True,
        old_scalar_failure_preserved=copy.deepcopy(FAILURE),original_mathematical_stages_recomputed=0)
    return dict(identity=expected,stages=entries,paths=paths,receipt=receipt)

def identity_for_stage(name,entry,policy,current):
    """Only an exact whitelisted name AND original receipt receives the old identity."""
    if name not in policy["stages"]:return current
    original=policy["stages"][name]
    if any(entry.get(k)!=original.get(k) for k in ("file","bytes","sha256","stage_kind")):
        raise ValueError("a whitelisted name no longer has its one exact original byte receipt")
    return policy["identity"]
