#!/usr/bin/env python3
"""Exact dyadic J923 -> J1845 layout for a fixed M160/N2048 SO3 target.

The fixed reference remains the original J923 object. Current node meanings
are exact affine pairs. Old node WORDS are copied to even positions; new
midpoint carriers and all actual coefficient restrictions are distinct
working data with their declared unpaid rounding responsibility.

No old R/T/Z column ordering is used. The SO3 x/y/z 161/161/160 channels
are preserved, and each old radial value/first/second derivative is copied.
Numerical carrier construction and coefficient injection require Actions.
"""
from __future__ import annotations

from fractions import Fraction
import copy
import hashlib
import json
import math
import os
from pathlib import Path

SCHEMA = "complete-fixed-reference-SO3-J923-to-J1845-dyadic-layout-v1"
REFERENCE_SOURCE_SHA256 = "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"
REFERENCE_SCHEMA = "R690-independent-axisymmetric-SO3-reference-input-v1"
REFERENCE_J = 923
CURRENT_J = 1845
M = 160
K = 3
FULL_N = 2048


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Radial carrier construction and full coefficient injection require public Actions")


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda: stream.read(1 << 20), b""):
            value.update(part)
    return value.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def digest(value, name):
    if (not isinstance(value,str) or len(value)!=64
            or any(c not in "0123456789abcdef" for c in value)):
        raise ValueError("Keep the full actual digest: "+name)
    return value


def rational(value):
    if isinstance(value,bool):
        raise TypeError("An affine coefficient is not a boolean")
    if isinstance(value,Fraction):
        return value
    if isinstance(value,int):
        return Fraction(value)
    if not isinstance(value,str):
        raise TypeError("Use explicit exact rational node coefficients")
    answer=Fraction(value)
    if str(answer)!=value:
        raise ValueError("Use canonical Fraction strings")
    return answer


def pair(value):
    if not isinstance(value,(tuple,list)) or len(value)!=2:
        raise ValueError("Keep both exact affine node coefficients")
    return tuple(rational(v) for v in value)


def words(value):
    return [[str(v) for v in pair(point)] for point in value]


def bisect_nodes(original):
    nodes=tuple(pair(v) for v in original)
    if (len(nodes)!=REFERENCE_J or nodes[0]!=(0,0) or nodes[-1]!=(1,0)):
        raise ValueError("Retain the complete original J923 affine nodes from 0 to S")
    result=[]
    for left,right in zip(nodes,nodes[1:]):
        if left==right:
            raise ValueError("Original symbolic nodes must be distinct")
        result.extend((left,tuple((a+b)/2 for a,b in zip(left,right))))
    result.append(nodes[-1])
    if len(result)!=CURRENT_J or tuple(result[::2])!=nodes:
        raise ArithmeticError("The exact complete dyadic node inclusion changed")
    return tuple(result)


def free_radial_slots(J):
    if J not in (REFERENCE_J,CURRENT_J):
        raise ValueError("Use one of the two explicitly declared radial layouts")
    return tuple(i for i in range(3*J) if i not in (0,3*(J-1),3*(J-1)+1))


def definition(reference_model, original_nodes, *, current_mesh_sha256):
    if (not isinstance(reference_model,dict)
            or reference_model.get("schema")!=REFERENCE_SCHEMA
            or reference_model.get("source_sha256")!=REFERENCE_SOURCE_SHA256
            or reference_model.get("M")!=M or reference_model.get("J")!=REFERENCE_J):
        raise ValueError("Bind the complete unchanged actual M160/J923 reference model")
    digest(reference_model.get("mesh_sha256"),"reference mesh")
    digest(reference_model.get("symbolic_node_report_sha256"),"whole original node report")
    digest(current_mesh_sha256,"current mesh")
    original=tuple(pair(v) for v in original_nodes)
    current=bisect_nodes(original)
    old_free,new_free=free_radial_slots(REFERENCE_J),free_radial_slots(CURRENT_J)
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        complete_original_reference_model=copy.deepcopy(reference_model),
        original_reference_model_identity_sha256=canonical(reference_model),
        original_symbolic_node_report_sha256=reference_model["symbolic_node_report_sha256"],
        reference_J=REFERENCE_J,current_J=CURRENT_J,M=M,K=K,full_N=FULL_N,
        rotation_channels=3*M+2,
        original_free_radial_slots=list(old_free),current_free_radial_slots=list(new_free),
        original_free_size=M-K+len(old_free)*(3*M+2)+1,
        current_free_size=M-K+len(new_free)*(3*M+2)+1,
        reference_mesh_sha256=reference_model["mesh_sha256"],
        current_mesh_sha256=current_mesh_sha256,
        complete_original_node_definitions=words(original),
        complete_current_node_definitions=words(current),
        original_node_definition_identity_sha256=canonical(words(original)),
        current_node_definition_identity_sha256=canonical(words(current)),
        dyadic_factor=2,old_node_index_to_current="i -> 2*i",
        current_cell_to_reference="(2*i+j,u) -> (i,(j+Fraction(binary64_u))/2), j in {0,1}",
        current_query_definition="exact affine combination of complete current symbolic endpoints",
        reference_local_coordinate_rounding_permitted=False,
        midpoint_carrier_is_not_assumed_to_equal_binary_average=True,
        original_mesh_words_copied_to_current_even_nodes=True,
        original_core_height_and_three_SO3_channels_retained=True,
        new_radial_shared_quintic_jets_are_free=True,
        mathematical_restriction="unique degree<=5 Hermite restriction at each accurate symbolic midpoint",
        working_midpoint_coefficients_equal_accurate_restriction_claimed=False,
        full_working_field_or_root_bitwise_equality_claimed=False,
        exact_selected_field_inclusion_requires_compatible_implicit_branch=True,
        old_norm_rows_physical_values_or_certificates_inherited=False)


def validate_definition(value):
    if not isinstance(value,dict):
        raise ValueError("Keep the complete exact radial layout definition")
    expected=definition(value.get("complete_original_reference_model"),
        value.get("complete_original_node_definitions"),
        current_mesh_sha256=value.get("current_mesh_sha256"))
    if value!=expected:
        raise ValueError("A current/reference node, free slot or complete radial policy changed")
    return canonical(expected)


def local_fraction(value):
    if isinstance(value,bool):
        raise TypeError("A local coordinate is not a boolean")
    if isinstance(value,float):
        if not math.isfinite(value):
            raise ValueError("A local coordinate must be finite")
        answer=Fraction.from_float(value)
    else:
        answer=rational(value)
    if not 0<=answer<=1:
        raise ValueError("Use the complete closed local interval")
    return answer


def affine_point(nodes, cell, local):
    if type(cell) is not int or not 0<=cell<len(nodes)-1:
        raise ValueError("Use an actual integer current/reference cell")
    u=local_fraction(local)
    a,b=pair(nodes[cell]),pair(nodes[cell+1])
    return tuple((1-u)*x+u*y for x,y in zip(a,b))


def original_location_to_current(cell, local, original_nodes):
    """Exact old address transfer with a proved representable new binary local."""
    if type(cell) is not int or not 0<=cell<REFERENCE_J-1:
        raise ValueError("Use an original J923 integer cell")
    u=local_fraction(local)
    child=0 if u<=Fraction(1,2) else 1
    current_cell=2*cell+child
    exact_local=2*u-child
    literal=float(exact_local)
    if not math.isfinite(literal) or Fraction.from_float(literal)!=exact_local:
        raise ValueError("The exact transferred local coordinate has no identical binary64 word")
    current_nodes=bisect_nodes(original_nodes)
    old_point=affine_point(original_nodes,cell,u)
    new_point=affine_point(current_nodes,current_cell,exact_local)
    if old_point!=new_point:
        raise ArithmeticError("The complete accurate original material location changed")
    return dict(cell=current_cell,local_hex=literal.hex(),
        original_cell=cell,original_local_exact=str(u),
        exact_current_local=str(exact_local),exact_affine_point=[str(v) for v in old_point],
        exact_address_identity_verified=True,approximate_local_conversion_used=False)


def current_location_to_original_exact(cell, local, original_nodes):
    """The returned original local is a Fraction, never a rounded double."""
    if type(cell) is not int or not 0<=cell<CURRENT_J-1:
        raise ValueError("Use an actual current J1845 cell")
    u=local_fraction(local)
    original_cell,child=divmod(cell,2)
    original_local=(child+u)/2
    current_nodes=bisect_nodes(original_nodes)
    point=affine_point(current_nodes,cell,u)
    if point!=affine_point(original_nodes,original_cell,original_local):
        raise ArithmeticError("The whole current-to-original affine identity changed")
    return original_cell,original_local,point


def upper_float(value):
    value=Fraction(value)
    answer=float(value)
    if not math.isfinite(answer):
        raise ArithmeticError("An exact error has no finite binary64 upper carrier")
    if Fraction.from_float(answer)<value:
        answer=math.nextafter(answer,math.inf)
    if Fraction.from_float(answer)<value:
        raise ArithmeticError("The claimed scalar carrier does not enclose its exact error")
    return answer


def array_sha(value):
    import numpy as np
    value=np.ascontiguousarray(value)
    result=hashlib.sha256(str(value.dtype).encode())
    result.update(json.dumps(list(value.shape)).encode())
    result.update(value.tobytes())
    return result.hexdigest()


def construct_current_carriers(context):
    """Use original even words and genuine exact-affine midpoint enclosures."""
    require_actions()
    import inspect
    import numpy as np
    if (sha(inspect.getfile(type(context)))!=REFERENCE_SOURCE_SHA256
            or context.model.get("schema")!=REFERENCE_SCHEMA
            or context.model.get("source_sha256")!=REFERENCE_SOURCE_SHA256
            or canonical(context.model)!=context.identity
            or context.J!=REFERENCE_J or context.M!=M):
        raise ValueError("Use the complete actually bound original reference context")
    original_nodes=tuple(pair(v) for v in context.nodes)
    current_nodes=bisect_nodes(original_nodes)
    old=np.asarray(context.mesh)
    if (str(old.dtype)!="float64" or not old.dtype.isnative or old.shape!=(REFERENCE_J,)
            or not np.isfinite(old).all() or np.any(np.diff(old)<=0)
            or array_sha(old)!=context.model["mesh_sha256"]):
        raise ValueError("Keep every original finite increasing mesh word")
    scale=int(context.full.h.S)
    if scale<=0:
        raise ValueError("The actual complete interval arithmetic scale must be positive")
    current=np.empty(CURRENT_J,dtype=np.float64)
    current[::2]=old
    node_error=np.empty(CURRENT_J,dtype=np.float64)
    exact_boxes=[]
    for i,point in enumerate(current_nodes):
        box=context.full.affine_time(*point)
        lo,hi=Fraction(int(box[0]),scale),Fraction(int(box[1]),scale)
        if lo>hi:
            raise ArithmeticError("A whole accurate node box is reversed")
        if i%2:
            value=float(context.full.carrier(box))
            if not math.isfinite(value):
                raise ArithmeticError("An accurate midpoint has a nonfinite working carrier")
            current[i]=value
        word=Fraction.from_float(float(current[i]))
        node_error[i]=upper_float(max(abs(word-lo),abs(word-hi)))
        exact_boxes.append([str(lo),str(hi)])
    if current[::2].tobytes()!=old.tobytes():
        raise ArithmeticError("An original complete mesh word changed")
    widths=np.diff(current)
    if not np.isfinite(widths).all() or np.any(widths<=0):
        bad=np.flatnonzero((~np.isfinite(widths))|(widths<=0))
        raise ArithmeticError("This literal binary64 mesh cannot represent all accurate half-cells; "
            "no node was merged or jittered: "+repr([int(v) for v in bad]))
    true_current_width_boxes=[]
    current_width_error=np.empty(CURRENT_J-1,dtype=np.float64)
    original_width_carriers=np.empty(REFERENCE_J-1,dtype=np.float64)
    for i,(left,right) in enumerate(zip(current_nodes,current_nodes[1:])):
        delta=tuple(b-a for a,b in zip(left,right))
        box=context.full.affine_time(*delta)
        lo,hi=Fraction(int(box[0]),scale),Fraction(int(box[1]),scale)
        if lo<=0 or lo>hi:
            raise ArithmeticError("Every accurate current half-cell must have a strictly positive enclosure")
        word=Fraction.from_float(float(widths[i]))
        current_width_error[i]=upper_float(max(abs(word-lo),abs(word-hi)))
        true_current_width_boxes.append([str(lo),str(hi)])
        if i%2==0:
            old_delta=tuple(b-a for a,b in zip(original_nodes[i//2],original_nodes[i//2+1]))
            old_box=context.full.affine_time(*old_delta)
            if old_box[0]<=0:
                raise ArithmeticError("The accurate original whole cell must remain positive")
            original_width_carriers[i//2]=float(context.full.carrier(old_box))
    if not np.isfinite(original_width_carriers).all() or np.any(original_width_carriers<=0):
        raise ArithmeticError("Original true-width midpoint carriers must be positive and finite")
    model=definition(context.model,original_nodes,current_mesh_sha256=array_sha(current))
    record=dict(schema=SCHEMA,source_sha256=sha(__file__),
        definition=model,definition_identity_sha256=canonical(model),
        original_mesh_sha256=array_sha(old),current_mesh_sha256=array_sha(current),
        all_original_node_words_copied_to_even=True,
        accurate_node_boxes=exact_boxes,
        accurate_current_width_boxes=true_current_width_boxes,
        actual_node_carrier_error_array_sha256=array_sha(node_error),
        actual_width_carrier_error_array_sha256=array_sha(current_width_error),
        midpoint_coefficients_not_constructed_here=True,
        scalar_metric_or_normal_root_or_field_evaluated=False,
        ordinary_field_quadrature_and_root_errors_enclosed=False)
    for value in (current,widths,node_error,current_width_error,original_width_carriers):
        value.setflags(write=False)
    return dict(mesh=current,widths=widths,node_error=node_error,
        width_error=current_width_error,original_width_carriers=original_width_carriers,
        exact_nodes=current_nodes,definition=model,record=record)


def embed_outer_shared_quintic_words(value,layout,original_width_carriers):
    """Complete ordinary working restriction; exact coefficient error remains explicit."""
    require_actions()
    import numpy as np
    identity=validate_definition(layout)
    x=np.asarray(value)
    old_free=np.asarray(layout["original_free_radial_slots"],dtype=np.int64)
    new_free=np.asarray(layout["current_free_radial_slots"],dtype=np.int64)
    if (str(x.dtype)!="float64" or not x.dtype.isnative
            or x.shape!=(layout["original_free_size"],) or not np.isfinite(x).all()):
        raise ValueError("Use every finite actual original M160/J923 free word")
    widths=np.asarray(original_width_carriers)
    if (str(widths.dtype)!="float64" or widths.shape!=(REFERENCE_J-1,)
            or not np.isfinite(widths).all() or np.any(widths<=0)):
        raise ValueError("Use all actual positive carriers of the true original widths")
    channels=3*M+2
    old=np.zeros((3*REFERENCE_J,channels),dtype=np.float64)
    old[old_free]=x[M-K:-1].reshape(len(old_free),channels)
    old=old.reshape(REFERENCE_J,3,channels)
    current=np.zeros((CURRENT_J,3,channels),dtype=np.float64)
    current[::2]=old
    h=widths[:,None]
    Y0,U0,A0=old[:-1,0],old[:-1,1],old[:-1,2]
    Y1,U1,A1=old[1:,0],old[1:,1],old[1:,2]
    current[1::2,0]=(Y0+Y1)/2.+(5.*h/32.)*(U0-U1)+(h*h/64.)*(A0+A1)
    current[1::2,1]=(15./(8.*h))*(Y1-Y0)-(7./16.)*(U0+U1)+(h/32.)*(A1-A0)
    current[1::2,2]=(3./(2.*h))*(U1-U0)-(A0+A1)/4.
    zero=np.all(old[:-1]==0,axis=1)&np.all(old[1:]==0,axis=1)
    for order in range(3):
        current[1::2,order][zero]=0.
    if (not np.isfinite(current).all()
            or current[::2].tobytes()!=old.tobytes()
            or np.any(current[0,0]!=0) or np.any(current[-1,:2]!=0)):
        raise ArithmeticError("All original radial words, structural zeros and complete midpoint jets must remain usable")
    y=np.r_[x[:M-K],current.reshape(3*CURRENT_J,channels)[new_free].ravel(),x[-1]]
    if y.shape!=(layout["current_free_size"],) or not np.isfinite(y).all():
        raise ArithmeticError("The complete new free vector changed shape or finiteness")
    if y[:M-K].tobytes()!=x[:M-K].tobytes() or y[-1:].tobytes()!=x[-1:].tobytes():
        raise ArithmeticError("Keep every free core word and the actual height")
    rotation_blocks=[]
    for component,a,b in (("x",0,M+1),("y",M+1,2*(M+1)),("z",2*(M+1),3*M+2)):
        rotation_blocks.append(dict(component=component,channel_start=a,channel_stop=b,
            original_all_three_jet_words_sha256=array_sha(old[:,:,a:b]),
            current_even_all_three_jet_words_sha256=array_sha(current[::2,:,a:b]),
            every_original_node_word_identical=True))
    record=dict(schema="actual-complete-SO3-shared-quintic-dyadic-word-injection-v1",
        source_sha256=sha(__file__),layout_identity_sha256=identity,
        original_full_point_sha256=array_sha(x),current_full_point_sha256=array_sha(y),
        original_free_size=int(x.size),current_free_size=int(y.size),
        complete_original_jets_sha256=array_sha(old),complete_current_jets_sha256=array_sha(current),
        original_width_carriers_sha256=array_sha(widths),
        original_height_hex=float(x[-1]).hex(),current_height_hex=float(y[-1]).hex(),
        all_original_core_height_and_even_node_words_copied=True,
        rotation_blocks=rotation_blocks,
        all_new_shared_radial_jet_slots_remain_free=True,
        complete_midpoint_formula="R676.7 on each whole original cell, independently in all SO3 channels",
        exactly_zero_old_polynomial_channels_kept_zero=True,
        actual_zero_polynomial_channel_count=int(np.count_nonzero(zero)),
        coefficient_true_width_and_rounding_error_enclosed=False,
        accurate_midpoint_coefficients_equal_saved_binary64_claimed=False,
        current_normal_roots_field_or_Phi_evaluated=False,
        old_physical_values_norm_or_certificates_inherited=False)
    return y,record
