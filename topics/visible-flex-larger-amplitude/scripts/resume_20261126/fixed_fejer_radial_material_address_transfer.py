#!/usr/bin/env python3
"""Complete exact material-address bridge for fixed-target J923 -> J1845.

All old tagged stage indices are resolved with their own original J923
carrier before dyadic address mapping. New current rows are read from their
whole actual runner carrier and checked against the exact union algorithm.
This is a standard-library consumer. It neither evaluates a field nor
reconstructs any numerical root, Jacobian, scalar integral or geometry value.
"""
from __future__ import annotations

import ast
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
import zipfile

SCHEMA="complete-exact-radial-material-address-transfer-v1"
LAYOUT_SOURCE_SHA256="a31d80a953722cc3644f793e4a28a372d980f6d0af7c8d98402f5f4739e3b5cf"
OBSERVATION_SOURCE_SHA256="a89cb4f660f56ccc49e6f59191730aacc414cb36714ec64c2061784d3215f07d"
HISTORY_SOURCE_SHA256="4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60"
REFERENCE_SOURCE_SHA256="e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
CURRENT_REFERENCE_MODEL_SHA256="ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac"
ROLES=("curvature_points","radius_points","protected_curvature_points")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("Actual array/history reads require public Actions")


def sha(path):
    value=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda:stream.read(1<<20),b""):
            value.update(part)
    return value.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def file_record(path):
    path=Path(path).resolve(strict=True)
    if not path.is_file():
        raise ValueError("The complete immutable input file is absent")
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def bound_json(record):
    if not isinstance(record,dict) or file_record(record.get("path"))!=record:
        raise ValueError("The complete input JSON file record changed")
    raw=Path(record["path"]).read_bytes()
    if len(raw)!=record["bytes"] or hashlib.sha256(raw).hexdigest()!=record["sha256"]:
        raise ValueError("The complete JSON input changed during reading")
    value=json.loads(raw)
    if file_record(record["path"])!=record:
        raise ValueError("The complete JSON input changed after reading")
    return value


def _module(name,expected):
    path=Path(__file__).resolve().with_name(name)
    if sha(path)!=expected:
        raise ValueError("The full radial address source changed: "+name)
    key="_radial_material_address_"+expected
    module=sys.modules.get(key)
    if module is None:
        spec=importlib.util.spec_from_file_location(key,path)
        module=importlib.util.module_from_spec(spec);sys.modules[key]=module
        spec.loader.exec_module(module)
    if sha(module.__file__)!=expected:
        raise ValueError("The actual loaded radial address source differs")
    return module


def npy_member(archive, name):
    raw = archive.read(name+'.npy')
    if raw[:6] != b'\x93NUMPY' or len(raw) < 10:
        raise ValueError('Not a complete literal NPY member: '+name)
    version = tuple(raw[6:8])
    if version == (1, 0):
        length, start = struct.unpack('<H', raw[8:10])[0], 10
    elif version in ((2, 0), (3, 0)):
        if len(raw) < 12:
            raise ValueError('Truncated NPY header')
        length, start = struct.unpack('<I', raw[8:12])[0], 12
    else:
        raise ValueError('Unsupported NPY version')
    end = start+length
    if end > len(raw):
        raise ValueError('Truncated NPY header payload')
    header = ast.literal_eval(raw[start:end].decode('utf-8' if version == (3, 0) else 'latin1'))
    if (not isinstance(header, dict) or set(header) != {'descr', 'fortran_order', 'shape'}
            or header['fortran_order'] is not False or not isinstance(header['shape'], tuple)
            or any(isinstance(v, bool) or not isinstance(v, int) or v < 0 for v in header['shape'])):
        raise ValueError('Require the complete C-order literal array')
    descriptor, shape, data = header['descr'], header['shape'], raw[end:]
    if descriptor in ('<f8', '<i8'):
        width = 8
    elif isinstance(descriptor, str) and descriptor.startswith('<U') and descriptor[2:].isdigit():
        width = 4*int(descriptor[2:])
    else:
        raise ValueError('No object arrays or changed binary64 dtype')
    if len(data) != width*math.prod(shape):
        raise ValueError('Complete NPY shape and payload differ')
    return descriptor, shape, data

def _array_sha(dtype, shape, data):
    h = hashlib.sha256(dtype.encode())
    h.update(json.dumps(list(shape)).encode())
    h.update(data)
    return h.hexdigest()

def _member(archive, name, dtype, shape):
    d, s, b = npy_member(archive, name)
    if d != dtype or s != tuple(shape):
        raise ValueError('Changed complete carrier member: '+name)
    code = '<d' if dtype == '<f8' else '<q'
    values = tuple(v for (v,) in struct.iter_unpack(code, b))
    if dtype == '<f8' and not all(math.isfinite(v) for v in values):
        raise ValueError('Nonfinite actual carrier word')
    return values, b


def validate_layout(value):
    module=_module("fixed_fejer_radial_bisection_layout.py",LAYOUT_SOURCE_SHA256)
    if (sha(module.validate_definition.__code__.co_filename)!=LAYOUT_SOURCE_SHA256
            or module.validate_definition(value)!=canonical(value)
            or value.get("original_reference_model_identity_sha256")!=CURRENT_REFERENCE_MODEL_SHA256
            or value.get("complete_original_reference_model",{}).get("source_sha256")!=REFERENCE_SOURCE_SHA256):
        raise ValueError("The entire accurate node layout must bind the real fixed Fejer target")
    return module


def _transfer(cell,u,nodes):
    """Exact old address to a representable new address, without recomputing all nodes."""
    if isinstance(cell,bool) or int(cell)!=cell or not 0<=int(cell)<922:
        raise ValueError("Use an actual original J923 cell")
    u=float(u)
    if not math.isfinite(u) or not 0<=u<=1:
        raise ValueError("Use an actual finite original local word")
    cell=int(cell);q=F.from_float(u)
    child=0 if q<=F(1,2) else 1
    fine_u=2*q-child
    word=float(fine_u)
    if F.from_float(word)!=fine_u:
        raise ValueError("The exact old local address is not identically representable on the fine cell")
    left,right=nodes[cell],nodes[cell+1]
    midpoint=tuple((a+b)/2 for a,b in zip(left,right))
    a,b=(left,midpoint) if child==0 else (midpoint,right)
    old_point=tuple((1-q)*x+q*y for x,y in zip(left,right))
    new_point=tuple((1-fine_u)*x+fine_u*y for x,y in zip(a,b))
    if old_point!=new_point:
        raise ArithmeticError("The exact complete old material point changed")
    return 2*cell+child,word,old_point


def mapped_radial_words(original,layout):
    validate_layout(layout)
    nodes=tuple(tuple(F(v) for v in p) for p in layout["complete_original_node_definitions"])
    result=[]
    for cell,word in original:
        if not isinstance(word,str) or float.fromhex(word).hex()!=word:
            raise ValueError("Keep every original literal local coordinate")
        c,u,_=_transfer(cell,float.fromhex(word),nodes)
        result.append((c,u.hex()))
    return result


def map_point(value,layout,*,source_J):
    if not isinstance(value,dict):
        raise ValueError("Keep a complete actual material point dictionary")
    c,u,p=value.get("cell"),value.get("u"),value.get("phi")
    if isinstance(c,bool) or int(c)!=c or not math.isfinite(float(p)):
        raise ValueError("The full cell and angle word must be finite and literal")
    c,u,p=int(c),float(u),float(p)
    if not math.isfinite(u) or not 0<=u<=1:
        raise ValueError("Use an actual complete local word")
    if source_J==923:
        nodes=tuple(tuple(F(v) for v in r) for r in layout["complete_original_node_definitions"])
        c,u,_=_transfer(c,u,nodes)
    elif source_J==1845:
        if not 0<=c<1844:
            raise ValueError("Use the actual current J1845 cell")
    else:
        raise ValueError("This bridge must not reinterpret another radial layout")
    result=copy.deepcopy(value)
    result.update(cell=c,u=u,phi=p)
    return result


def map_arrays(arrays,layout,*,source_J):
    validate_layout(layout)
    if not isinstance(arrays,dict) or not set(ROLES).issubset(arrays):
        raise ValueError("Retain all three explicit historical role sets")
    result={}
    for role in ROLES:
        values=arrays[role]
        if not isinstance(values,(list,tuple)):
            raise ValueError("Keep every complete literal location array")
        output=[];seen=set()
        for row in values:
            if not isinstance(row,(list,tuple)) or len(row)!=3:
                raise ValueError("Keep each complete cell/local/angle location")
            point=map_point(dict(cell=row[0],u=row[1],phi=row[2]),layout,source_J=source_J)
            key=(point["cell"],point["u"].hex(),point["phi"].hex())
            if key not in seen:
                seen.add(key);output.append([point["cell"],point["u"],point["phi"]])
        result[role]=output
    protected={(int(c),float(u).hex(),float(p).hex()) for c,u,p in result["protected_curvature_points"]}
    curvature={(int(c),float(u).hex(),float(p).hex()) for c,u,p in result["curvature_points"]}
    if not protected.issubset(curvature):
        raise ValueError("Protected original points cannot disappear from the complete curvature set")
    return result


def transfer_typed_row(row,layout,*,source_J):
    if not isinstance(row,dict):
        raise ValueError("Keep a complete typed separation record")
    result=copy.deepcopy(row)
    if result.get("location") is not None:
        result["location"]=map_point(result["location"],layout,source_J=source_J)
    partner=result.get("partner")
    if partner is not None and partner.get("location") is not None:
        partner["location"]=map_point(partner["location"],layout,source_J=source_J)
    return result


def read_refined_plan(files,definition,*,original_current):
    """Read the complete actual saved fine plan and prove its full row inclusion."""
    require_actions()
    if (not isinstance(files,dict)
            or files.get("schema")!="complete-same-target-dyadic-observation-files-v1"
            or files.get("definition_identity_sha256")!=canonical(definition)
            or files.get("raw_stays_on_runner") is not True
            or not isinstance(files.get("files"),dict)):
        raise ValueError("Keep the complete actual current radial input file set")
    layout=definition.get("complete_radial_layout_definition")
    layout_module=validate_layout(layout)
    observer=_module("fixed_fejer_complete_dyadic_radial_observations.py",OBSERVATION_SOURCE_SHA256)
    if (sha(observer.definition.__code__.co_filename)!=OBSERVATION_SOURCE_SHA256
            or definition!=observer.definition(layout["complete_original_reference_model"],layout,
                observation_arrays=definition.get("complete_observation_arrays"))):
        raise ValueError("The complete saved same-target observation rule changed")
    records=files["files"]
    required={"complete-dyadic-observations.npz","current-symbolic-nodes.json",
        "complete-a-boxes.json","complete-parent-address-transfer.json","observation-definition.json"}
    if set(records)!=required:
        raise ValueError("Keep every actual current carrier, exact node/anchor and complete transfer file")
    for record in records.values():
        if not isinstance(record,dict) or file_record(record.get("path"))!=record:
            raise ValueError("A complete current radial output file changed")
    if bound_json(records["observation-definition.json"])!=definition:
        raise ValueError("The complete saved observation definition differs")
    node_record=bound_json(records["current-symbolic-nodes.json"])
    if (node_record.get("source_sha256")!=OBSERVATION_SOURCE_SHA256
            or node_record.get("reference_model_identity_sha256")!=CURRENT_REFERENCE_MODEL_SHA256
            or node_record.get("radial_layout_identity_sha256")!=canonical(layout)
            or node_record.get("exact_current_nodes")!=layout["complete_current_node_definitions"]
            or node_record.get("current_legacy_count")!=3689
            or node_record.get("original_reference_context_not_replaced") is not True):
        raise ValueError("Every exact current node and original reference identity is required")
    array_records=definition["complete_observation_arrays"]
    P=array_records["cells"]["shape"][0]
    if type(P) is not int or not 14753<=P<=22130:
        raise ValueError("Keep every native and retained original observation")
    decoded={};raw_bytes={}
    raw_record=records["complete-dyadic-observations.npz"]
    with zipfile.ZipFile(raw_record["path"]) as archive:
        for name,record in array_records.items():
            dtype="<i8" if record["dtype"]=="int64" else "<f8"
            values,data=_member(archive,name,dtype,record["shape"])
            if _array_sha(record["dtype"],record["shape"],data)!=record["sha256"]:
                raise ValueError("The full actual radial array changed: "+name)
            decoded[name]=values;raw_bytes[name]=data
        mesh,mesh_bytes=_member(archive,"mesh","<f8",(1845,))
        oldmesh,oldmesh_bytes=_member(archive,"original_mesh","<f8",(923,))
        gc,gb=_member(archive,"observation_gauss_unit_nodes","<f8",(6,))
        gw,gwb=_member(archive,"observation_gauss_unit_weights","<f8",(6,))
        oc,ocb=_member(archive,"observation_cells","<i8",(P,))
        ou,oub=_member(archive,"observation_u","<f8",(P,))
        legacy,_=_member(archive,"observation_legacy_count","<i8",())
        order,_=_member(archive,"observation_order","<i8",())
        pc,pcb=_member(archive,"parent_cells","<i8",(7377,))
        pu,pub=_member(archive,"parent_local_u","<f8",(7377,))
    if (ocb!=raw_bytes["cells"] or oub!=raw_bytes["local_u"]
            or legacy!=(3689,) or order!=(6,)
            or pc!=tuple(original_current["cells"]) or pu!=tuple(original_current["local"])
            or pcb!=original_current["cell_bytes"] or pub!=original_current["local_bytes"]
            or _array_sha("float64",(1845,),mesh_bytes)!=layout["current_mesh_sha256"]
            or _array_sha("float64",(923,),oldmesh_bytes)!=layout["reference_mesh_sha256"]
            or b"".join(struct.pack("<d",v) for v in mesh[::2])!=oldmesh_bytes
            or any(a>=b for a,b in zip(mesh,mesh[1:]))
            or any(not 0<v<1 for v in gc) or any(v<=0 for v in gw)):
        raise ValueError("The entire old/new carrier words, node inclusion or native Gauss rule changed")
    nodes=tuple(tuple(F(v) for v in pair) for pair in layout["complete_current_node_definitions"])
    original_nodes=tuple(tuple(F(v) for v in pair) for pair in layout["complete_original_node_definitions"])
    expected=[]
    for j in range(1845):
        expected.append((min(j,1843),1. if j==1844 else 0.))
        if j<1844:
            expected.append((j,.5))
    expected.extend((j,u) for j in range(1844) for u in gc)
    def point(cell,u):
        a,b=nodes[cell],nodes[cell+1];v=F.from_float(float(u))
        return tuple((1-v)*x+v*y for x,y in zip(a,b))
    lookup={}
    for i,(c,u) in enumerate(expected):
        p=point(c,u)
        if p in lookup:raise ValueError("The whole native refined plan has duplicate exact points")
        lookup[p]=i
    mapped=[]
    for c,u in zip(pc,pu):
        cc,uu,p=_transfer(c,u,original_nodes)
        row=lookup.get(p)
        if row is None:
            row=len(expected);lookup[p]=row;expected.append((cc,uu))
        mapped.append(row)
    actual=[(c,u.hex()) for c,u in zip(oc,ou)]
    expected_words=[(c,u.hex()) for c,u in expected]
    if (actual!=expected_words or tuple(mapped)!=decoded["parent_stage_map"]
            or len(expected)!=P or len(set(mapped))!=7377):
        raise ValueError("The entire actual refined union or one original row is missing")
    if any(decoded["a"][mapped[i]]!=decoded["parent_a"][i] for i in range(7377)):
        raise ValueError("Every actual parent target scalar word must remain in the new union")
    if any(a<=0 for a in decoded["a"]) or any(e<0 for e in decoded["a_error"]+decoded["time_error"]):
        raise ValueError("Keep all finite positive same-target a words and nonnegative actual errors")
    if any(s<0 or g<0 or p<0 or q<0 or q!=(g+p)/2.
            or .5*s+.5*q<=0
            for s,g,p,q in zip(decoded["legacy_simpson"],decoded["current_gauss"],
                decoded["retained_parent_quadrature"],decoded["mixed_quadrature"])):
        raise ValueError("Every current and old row must retain its complete positive declared weight")
    if _array_sha("float64",(7377,),raw_bytes["parent_a"])!=layout["complete_original_reference_model"]["a_observations_sha256"]:
        raise ValueError("The complete original common-functional target array changed")
    transfers=bound_json(records["complete-parent-address-transfer.json"])
    if len(transfers)!=7377:
        raise ValueError("Keep all exact original-row transfer records")
    for i,(c,u) in enumerate(zip(pc,pu)):
        item=transfers[i];cc,uu,p=_transfer(c,u,original_nodes)
        if (item.get("cell")!=cc or item.get("local_hex")!=uu.hex()
                or item.get("original_cell")!=c
                or item.get("original_local_exact")!=str(F.from_float(u))
                or item.get("exact_current_local")!=str(F.from_float(uu))
                or item.get("exact_affine_point")!=[str(v) for v in p]
                or item.get("exact_address_identity_verified") is not True
                or item.get("approximate_local_conversion_used") is not False):
            raise ValueError("An actual original material address was rounded or relabelled")
    boxes=bound_json(records["complete-a-boxes.json"])
    if (len(boxes)!=P
            or node_record.get("complete_current_node_midpoint_a_boxes")!=boxes[:3689]):
        raise ValueError("Keep every complete scalar enclosure and all fine-node anchors")
    for i,(pair,a,error) in enumerate(zip(boxes,decoded["a"],decoded["a_error"])):
        if not isinstance(pair,list) or len(pair)!=2:
            raise ValueError("Every actual scalar enclosure needs both exact endpoints")
        lo,hi=F(pair[0]),F(pair[1])
        if (str(lo)!=pair[0] or str(hi)!=pair[1] or lo>hi
                or max(abs(F.from_float(a)-lo),abs(F.from_float(a)-hi))>F.from_float(error)):
            raise ValueError("The claimed exact scalar/carrier error does not contain its complete interval at row "+str(i))
    for record in records.values():
        if file_record(record["path"])!=record:
            raise ValueError("A complete radial input changed during the full read")
    return dict(record=copy.deepcopy(raw_record),cells=oc,local=ou,cell_bytes=ocb,local_bytes=oub,
        radial_words=actual,mesh_sha256=layout["current_mesh_sha256"],
        metadata=dict(record=copy.deepcopy(raw_record),complete_radial_entry_count=P,
            complete_unique_radial_entry_count=len(set(actual)),legacy_count=3689,
            cells_sha256=_array_sha("int64",(P,),ocb),
            local_u_sha256=_array_sha("float64",(P,),oub),
            radial_words_sha256=canonical(actual),
            gauss_unit_nodes_binary64_hex=[v.hex() for v in gc],
            gauss_unit_nodes_sha256=_array_sha("float64",(6,),gb),
            original_complete_parent_stage_map_sha256=_array_sha("int64",(7377,),raw_bytes["parent_stage_map"]),
            all_original_7377_rows_preserved=True,
            complete_native_grid_and_literal_old_union_checked=True,
            full_plan_closed_form_checked=True),
        complete_files=copy.deepcopy(files),definition=copy.deepcopy(definition),
        layout_definition=copy.deepcopy(layout),
        exact_parent_transfer_identity_sha256=canonical(transfers),
        actual_complete_a_boxes_identity_sha256=canonical(boxes))


def runtime_plan(q,*,original_current):
    base=q.base
    if (base.J!=1845 or base.reference_J!=923 or q.J!=1845 or q.N!=513 or q.full_N!=2048
            or base.model.get("radial_layout_identity_sha256")!=canonical(base.radial_layout_definition)
            or base.model.get("radial_observation_identity_sha256")!=canonical(base.radial_observations.definition)):
        raise ValueError("Keep the complete actual fine operator and fixed original reference layout")
    value=read_refined_plan(base.radial_observation_files,base.radial_observations.definition,
        original_current=original_current)
    if (q.observation_cells.tobytes()!=value["cell_bytes"]
            or q.observation_u.tobytes()!=value["local_bytes"]
            or q.P!=len(value["cells"])):
        raise ValueError("The current physical operator is not using the full actually read fine observation union")
    return value


def history_arrays(history,payload,*,source_J,reference_carrier,current_carrier,current_P):
    require_actions()
    if sha(history.Locations.walk.__code__.co_filename)!=HISTORY_SOURCE_SHA256:
        raise ValueError("Retain the complete original location walker")
    if source_J not in (923,1845):
        raise ValueError("Resolve tagged positions on their explicitly declared original/current layout")
    J,P,path=(923,7377,reference_carrier) if source_J==923 else (1845,current_P,current_carrier)
    collector=history.Locations(J,P,2048)
    collector.walk(payload,path=("full_declared_radial_history",str(J)))
    resolved=collector.resolve_grid(path)
    return collector.arrays(),dict(source_J=J,source_P=P,full_N=2048,
        resolved_grid_positions=resolved,actual_summary=collector.summary(),
        carrier=file_record(path),no_tagged_index_reinterpretation=True)
