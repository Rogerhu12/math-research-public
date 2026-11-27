#!/usr/bin/env python3
"""Complete fixed Fejer whole-leaf Gram, curvature and support enclosure producer.

Every output uses the complete source-bound accurate physical sixjets and the
same target a_deep/rho0 boxes. No finite-node field, J, root or quadrature is
replayed. The output is for the entire upper meridian on a verified full
circle. Closed lower/cap assembly, outward orientation, physical phases and
R650's global hypotheses are separate responsibilities.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
import uuid

SCHEMA="actual-fixed-fejer-meridian-batched-complete-continuous-gram-curvature-support-v1"
BINDING_SCHEMA=SCHEMA+"-binding"
BLOCK_SCHEMA=SCHEMA+"-complete-angle-block"
STREAM_SCHEMA=SCHEMA+"-whole-leaf-stream"
JOURNAL_SCHEMA=SCHEMA+"-block-journal"
TOPIC="topics/visible-flex-larger-amplitude"
LEAF_READER=("fixed_fejer_meridian_batched_complete_physical_leaf_binding.py","897fceaa340fd042db03b3ea0f9b72b3e2c1a5c235d7104ead2c4b0104c07fc6")
BETA_SOURCE=("same_field_positive_support_parameter.py",
    "e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991")
NORMAL_CONVENTION="candidate Fphi cross Fs on the entire upper meridian"
PATCH="upper-original-activity-and-complete-tail"


def load_reader(repo):
    path=Path(repo).resolve()/TOPIC/"scripts/resume_20261126"/LEAF_READER[0]
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=LEAF_READER[1]:
        raise ValueError("The entire exact physical-leaf reader changed")
    spec=importlib.util.spec_from_file_location("_fixed_fejer_complete_geometry_leaf_reader",path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    if (Path(module.__file__).resolve()!=path or module.sha(path)!=LEAF_READER[1]
            or module.sha(module.physical_cells.__code__.co_filename)!=LEAF_READER[1]):
        raise ValueError("Use the complete source-pinned leaf reader, not an injected callback")
    return module,path


def encoded(value):
    if isinstance(value,F):
        return str(value)
    if hasattr(value,"json") and callable(value.json):
        return value.json()
    if isinstance(value,dict):
        return {str(k):encoded(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [encoded(v) for v in value]
    if value is None or type(value) in (bool,int,str):
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise TypeError("Keep complete accurate values rational and actual metadata finite")


def immutable_json(path,value,r):
    raw=(json.dumps(encoded(value),sort_keys=True,separators=(",",":"),
        allow_nan=False)+"\n").encode()
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        if path.read_bytes()!=raw:
            raise ValueError("An immutable same-field geometry object changed")
        return r.file_record(path)
    tmp=path.with_name(path.name+".partial-"+uuid.uuid4().hex)
    with tmp.open("xb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp,path)
    return r.file_record(path)


def write_report(path,value,r):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(encoded(value),sort_keys=True,indent=2,allow_nan=False)+"\n").encode()
    tmp=path.with_name(path.name+".partial-"+uuid.uuid4().hex)
    with tmp.open("xb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp,path)
    return r.file_record(path)


def square_norm(v,k):
    return k.isum((x**2 for x in v),v[0].bits)


def symmetric_operator_upper(a,b,c,k):
    """Uniform spectral norm of a real symmetric 2x2 interval matrix."""
    trace=a+c
    gap=a-c
    radius=k.sqrt_bounds(gap.abs_upper()**2+4*b.abs_upper()**2,a.bits)[1]
    return k.up((trace.abs_upper()+radius)/2,a.bits)


def physical_leaf_geometry(value,context,k):
    """Exact whole-cell implications; no working matrix or eigenvalue is used."""
    bits=context["bits"]
    fields=value["physical_sixjets"]
    v={name:[k.box(x,bits) for x in fields[name]]
       for name in ("F","Fs","Fphi","Fss","Fsphi","Fphiphi")}
    scalar=value["accurate_fixed_scalar"]
    a=k.box(scalar["a_deep"],bits)
    rho=k.box(fields["rho0"],bits)
    t=a*rho
    E=square_norm(v["Fs"],k)
    mixed=k.dot(v["Fs"],v["Fphi"])
    G=square_norm(v["Fphi"],k)
    normal=k.cross(v["Fphi"],v["Fs"])
    n2=square_norm(normal,k)
    # The Lagrange identity is exact for this same complete pair of vectors.
    # Intersect independent outward enclosures; never clamp an inconsistent box.
    determinant=E*G-mixed**2
    n2=n2.intersect(determinant).intersect(k.Interval(0,n2.hi,bits))
    area=n2.sqrt()
    area_low=area.lo
    area_high=area.hi
    metric_available=(a.lo>0 and rho.lo>0 and t.lo>0)
    relative=None
    gram_error=None
    gram_lower=None
    gram_reason=None
    if metric_available:
        rel11,rel12,rel22=E,mixed/t,G/(t**2)
        h11,h12,h22=rel11-1,rel12,rel22-1
        gram_error=symmetric_operator_upper(h11,h12,h22,k)
        relative=dict(value=[[rel11,rel12],[rel12,rel22]],
            error=[[h11,h12],[h12,h22]],operator_norm_upper=gram_error)
        if gram_error<1:
            # det(relative Gram) >= (1-error)^2 and |N|=t*sqrt(det).
            proved=k.down(t.lo*(1-gram_error),bits)
            area_low=max(area_low,proved)
        if area_low>area_high:
            raise ArithmeticError("Independent exact immersion bounds are inconsistent")
        trace_upper=rel11.hi+rel22.hi
        gram_lower=max(F(0),1-gram_error)
        if area_low>0:
            if trace_upper<=0:
                raise ArithmeticError("A positive normal cannot have nonpositive Gram trace")
            det_relative_lower=area_low**2/(t.hi**2)
            gram_lower=max(gram_lower,det_relative_lower/trace_upper)
        gram_lower=k.down(gram_lower,bits)
    else:
        gram_reason="The full same-target a_deep/rho0 box has not proved strict positivity"
    if area_low<0 or area_high<area_low:
        raise ArithmeticError("The exact normal norm enclosure is inconsistent")
    area=k.Interval(area_low,area_high,bits)
    horizontal=v["F"][0]*normal[0]+v["F"][1]*normal[1]
    vertical=v["F"][2]*normal[2]
    normal_unit=None
    second=None
    normalized_second=None
    curvature=None
    curvature_methods={}
    curvature_reason=None
    if area_low>0:
        normal_unit=[(x/area).intersect(k.Interval(-1,1,bits)) for x in normal]
        l=k.dot(normal_unit,v["Fss"])
        m=k.dot(normal_unit,v["Fsphi"])
        n=k.dot(normal_unit,v["Fphiphi"])
        second=[[l,m],[m,n]]
        raw_trace=E.hi+G.hi
        if raw_trace<=0:
            raise ArithmeticError("The complete immersed first form has nonpositive trace")
        raw_lambda=area_low**2/raw_trace
        raw_bound=k.up(symmetric_operator_upper(l,m,n,k)/raw_lambda,bits)
        curvature_methods["physical_parameter_Gram_det_over_trace"]=raw_bound
        if metric_available and gram_lower>0:
            bl,bm,bn=l,m/t,n/(t**2)
            normalized_second=[[bl,bm],[bm,bn]]
            relative_bound=k.up(symmetric_operator_upper(bl,bm,bn,k)/gram_lower,bits)
            curvature_methods["same_target_normalized_Gram"]=relative_bound
        curvature=min(curvature_methods.values())
    else:
        curvature_reason="These complete boxes do not yet prove a strictly positive normal norm"
    raw_defects=[[k.box(x,bits) for x in row]
        for row in fields["all_three_raw_accurate_closure_defects"]]
    radial_xy=square_norm(v["F"][:2],k).sqrt().hi
    full_position_norm=square_norm(v["F"],k).sqrt().hi
    return dict(
        target_metric=dict(formula="diag(1,(a_deep*rho0)^2)",
            a_deep=a,rho0=rho,angular_scale=t,
            fixed_scalar_metric_identity_sha256=scalar["fixed_scalar_metric_identity_sha256"],
            accurate_fixed_target_identity_sha256=context["actual"]["exact_fixed_target_identity_sha256"],
            full_same_scalar_infinite_tail_included=True),
        raw_first_form=[[E,mixed],[mixed,G]],
        same_field_normal=normal,normal_norm=area,
        squared_normal_lagrange_intersection=n2,
        relative_Gram=relative,relative_Gram_operator_norm_available=metric_available,
        relative_Gram_error_operator_norm_upper=gram_error,
        relative_Gram_smallest_eigenvalue_lower=gram_lower,
        relative_Gram_unavailable_reason=gram_reason,
        immersion_positive_from_this_entire_closed_cell=area_low>0,
        oriented_unit_normal=normal_unit,
        second_fundamental_form=second,
        same_target_normalized_second_fundamental_form=normalized_second,
        principal_curvature_absolute_upper=curvature,
        principal_curvature_bound_methods=curvature_methods,
        principal_curvature_unavailable_reason=curvature_reason,
        support=dict(horizontal_numerator=horizontal,vertical_numerator=vertical,
            a_lower=horizontal.lo,b_lower=vertical.lo,
            normal_norm_lower=area_low,normal_norm_upper=area_high,
            candidate_normal_convention=NORMAL_CONVENTION,
            closed_surface_outward_orientation_certified=False),
        position_hull=v["F"],horizontal_position_norm_upper=radial_xy,
        full_position_norm_upper=full_position_norm,
        full_position_norm_uses_this_same_complete_leaf=True,
        complete_raw_accurate_closure_defect_absolute_component_uppers=
            [[x.abs_upper() for x in row] for row in raw_defects],
        all_six_physical_jet_vectors_used=True,
        all_original_raw_lift_terms_retained=True,
        finite_node_or_entry_max_used_as_operator_norm=False,
        accurate_field_enclosure_replaced_by_working_words=False)


class Statistics:
    def __init__(self):
        self.count=0
        self.gram_missing=0
        self.curvature_missing=0
        self.normal_unproved=0
        self.maxima={}
        self.minima={}
        self.position=None
        self.first_unavailable=[]

    def _maximum(self,key,value,witness):
        if value is None:
            return
        value=F(value)
        if key not in self.maxima or value>self.maxima[key]["value"]:
            self.maxima[key]=dict(value=value,witness=witness)

    def _minimum(self,key,value,witness):
        if value is None:
            return
        value=F(value)
        if key not in self.minima or value<self.minima[key]["value"]:
            self.minima[key]=dict(value=value,witness=witness)

    def add(self,body,witness):
        self.count+=1
        if not body["relative_Gram_operator_norm_available"]:
            self.gram_missing+=1
        if body["principal_curvature_absolute_upper"] is None:
            self.curvature_missing+=1
        if not body["immersion_positive_from_this_entire_closed_cell"]:
            self.normal_unproved+=1
        if ((body["relative_Gram_unavailable_reason"] or body["principal_curvature_unavailable_reason"])
                and len(self.first_unavailable)<16):
            self.first_unavailable.append(dict(id=witness,
                relative_Gram=body["relative_Gram_unavailable_reason"],
                curvature=body["principal_curvature_unavailable_reason"]))
        self._maximum("relative_Gram_error_operator_norm_upper",
            body["relative_Gram_error_operator_norm_upper"],witness)
        self._maximum("principal_curvature_absolute_upper",
            body["principal_curvature_absolute_upper"],witness)
        self._maximum("normal_norm_upper",body["support"]["normal_norm_upper"],witness)
        self._maximum("horizontal_position_norm_upper",body["horizontal_position_norm_upper"],witness)
        self._maximum("full_position_norm_upper",body["full_position_norm_upper"],witness)
        self._minimum("normal_norm_lower",body["support"]["normal_norm_lower"],witness)
        self._minimum("horizontal_support_numerator_lower",body["support"]["a_lower"],witness)
        self._minimum("vertical_support_numerator_lower",body["support"]["b_lower"],witness)
        self._minimum("relative_Gram_eigenvalue_lower",
            body["relative_Gram_smallest_eigenvalue_lower"],witness)
        self._minimum("accurate_target_a_lower",body["target_metric"]["a_deep"].lo,witness)
        self._minimum("accurate_fixed_rho0_lower",body["target_metric"]["rho0"].lo,witness)
        position=body["position_hull"]
        if self.position is None:
            self.position=[[v.lo,v.hi] for v in position]
        else:
            self.position=[[min(a[0],b.lo),max(a[1],b.hi)]
                for a,b in zip(self.position,position)]

    def absorb(self,value):
        required={"complete_leaf_count","relative_Gram_unavailable_leaf_count",
            "curvature_unavailable_leaf_count","normal_positive_unproved_leaf_count",
            "maxima_over_processed_leaves","minima_over_processed_leaves",
            "processed_position_hull","first_unavailable_leaves"}
        if not isinstance(value,dict) or set(value)!=required:
            raise ValueError("The complete block statistics schema changed")
        for name in ("complete_leaf_count","relative_Gram_unavailable_leaf_count",
                "curvature_unavailable_leaf_count","normal_positive_unproved_leaf_count"):
            if type(value[name]) is not int or value[name]<0:
                raise ValueError("Keep exact nonnegative block counts")
        total=value["complete_leaf_count"]
        if any(value[key]>total for key in
                ("relative_Gram_unavailable_leaf_count","curvature_unavailable_leaf_count",
                 "normal_positive_unproved_leaf_count")):
            raise ValueError("Unavailable block counts exceed the complete block")
        self.count+=total
        self.gram_missing+=value["relative_Gram_unavailable_leaf_count"]
        self.curvature_missing+=value["curvature_unavailable_leaf_count"]
        self.normal_unproved+=value["normal_positive_unproved_leaf_count"]
        for key,item in value["maxima_over_processed_leaves"].items():
            self._maximum(key,F(item["value"]),item["witness"])
        for key,item in value["minima_over_processed_leaves"].items():
            self._minimum(key,F(item["value"]),item["witness"])
        position=value["processed_position_hull"]
        if position is not None:
            if len(position)!=3 or any(len(v)!=2 or F(v[0])>F(v[1]) for v in position):
                raise ValueError("The complete block position hull changed")
            position=[[F(v) for v in row] for row in position]
            if self.position is None:
                self.position=position
            else:
                self.position=[[min(a[0],b[0]),max(a[1],b[1])]
                    for a,b in zip(self.position,position)]
        if not isinstance(value["first_unavailable_leaves"],list):
            raise ValueError("Unavailable-leaf provenance must remain explicit")
        self.first_unavailable.extend(value["first_unavailable_leaves"][:max(0,16-len(self.first_unavailable))])

    def metadata(self):
        return encoded(dict(complete_leaf_count=self.count,
            relative_Gram_unavailable_leaf_count=self.gram_missing,
            curvature_unavailable_leaf_count=self.curvature_missing,
            normal_positive_unproved_leaf_count=self.normal_unproved,
            maxima_over_processed_leaves=self.maxima,minima_over_processed_leaves=self.minima,
            processed_position_hull=self.position,first_unavailable_leaves=self.first_unavailable))


def complete_support_cell(leaf_record,body,job,ordinal):
    return dict(id=job["request"]["id"]+"/"+leaf_record["exact_radial_leaf"]["id"],
        patch=PATCH,cell=ordinal-1,u_interval=["0","1"],
        phi_over_pi_interval=job["request"]["exact_phi_over_pi_interval"],
        exact_radial_leaf=leaf_record["exact_radial_leaf"],
        a_lower=str(body["support"]["a_lower"]),b_lower=str(body["support"]["b_lower"]),
        normal_norm_lower=str(body["support"]["normal_norm_lower"]),
        normal_norm_upper=str(body["support"]["normal_norm_upper"]),
        candidate_normal_convention=NORMAL_CONVENTION,
        outward_orientation_or_full_closed_activity_claimed=False)


def produce_angle_block(job,context,r,k,binding_identity,outdir,inputs,outputs):
    request=job["request"]
    directory=outdir/"angles"/request["id"]
    directory.mkdir(parents=True,exist_ok=True)
    stream_path=directory/"whole-leaf-geometry.jsonl.gz"
    temp=directory/("whole-leaf-geometry.partial-"+uuid.uuid4().hex+".jsonl.gz")
    stats=Statistics()
    header=dict(schema=STREAM_SCHEMA,producer_source_sha256=r.sha(__file__),
        geometry_binding_identity_sha256=binding_identity,
        complete_normal_execution_binding_identity_sha256=context["binding_identity"],
        current_full_point_sha256=context["actual"]["current_full_point_sha256"],
        model_identity_sha256=context["actual"]["model_identity_sha256"],
        accurate_request=request,normal_journal_binding_identity_sha256=job["identity"],
        original_stage_count=32,original_sixjet_stream=job["physical"]["file"],
        candidate_normal_convention=NORMAL_CONVENTION,
        original_working_F_J_or_root_replayed=False)
    with temp.open("xb") as raw:
        with gzip.GzipFile(filename="",mode="wb",fileobj=raw,mtime=0) as stream:
            def emit(value):
                stream.write((json.dumps(encoded(value),sort_keys=True,
                    separators=(",",":"),allow_nan=False)+"\n").encode())
            emit(header)
            for ordinal,value in enumerate(r.physical_cells(job,context,inputs,k),1):
                body=physical_leaf_geometry(value,context,k)
                support=complete_support_cell(value,body,job,ordinal)
                stats.add(body,support["id"])
                emit(dict(kind="complete_continuous_geometry_leaf",ordinal=ordinal,
                    source_physical_stream_ordinal=ordinal,
                    exact_radial_leaf=value["exact_radial_leaf"],
                    accurate_phi_interval=value["accurate_phi_interval"],
                    support_cell=support,whole_cell_geometry=body))
            footer=dict(kind="complete_continuous_geometry_footer",complete_leaf_count=stats.count,
                all_original_radial_leaves_processed=True,
                complete_statistics=stats.metadata(),
                closed_surface_outward_orientation_or_reach_certified=False)
            emit(footer)
    if stats.count!=job["physical"]["complete_radial_leaf_count"]:
        raise ValueError("A whole original radial leaf was lost during geometry production")
    if stream_path.exists():
        if r.file_record(stream_path)["sha256"]!=r.file_record(temp)["sha256"]:
            raise ValueError("An immutable whole-leaf geometry stream already has different bytes")
        temp.unlink()
    else:
        os.replace(temp,stream_path)
    stream_record=r.file_record(stream_path)
    outputs.verify(stream_record)
    definition=encoded(dict(schema=BLOCK_SCHEMA,source_sha256=r.sha(__file__),
        geometry_binding_identity_sha256=binding_identity,
        current_full_point_sha256=context["actual"]["current_full_point_sha256"],
        complete_model_identity_sha256=context["actual"]["model_identity_sha256"],
        exact_fixed_target_identity_sha256=context["actual"]["exact_fixed_target_identity_sha256"],
        accurate_request=request,normal_journal_binding_identity_sha256=job["identity"],
        complete_original_stage_count=32,original_physical_stream=job["physical"]["file"],
        original_journal=job["summary"]["journal"],
        original_journal_header=job["summary"]["journal_header"],
        whole_leaf_geometry_stream=stream_record,complete_statistics=stats.metadata(),
        complete=True,full_original_radial_domain_and_tail=True,
        normal_convention=NORMAL_CONVENTION,
        original_working_word_errors_not_claimed=True,
        external_parameter_J_and_transpose_error_not_claimed=True,
        complete_closed_geometry_or_all_phases_certified=False))
    block=dict(schema=BLOCK_SCHEMA,definition=definition,identity_sha256=r.canonical(definition))
    record=immutable_json(directory/"complete-block.json",block,r)
    outputs.verify(record)
    return record,block


def read_block(record,job,context,r,k,binding_identity,outputs):
    block,_=outputs.read_json(record)
    body=block.get("definition")
    if (block.get("schema")!=BLOCK_SCHEMA or not isinstance(body,dict)
            or block.get("identity_sha256")!=r.canonical(body)
            or body.get("schema")!=BLOCK_SCHEMA or body.get("source_sha256")!=r.sha(__file__)
            or body.get("geometry_binding_identity_sha256")!=binding_identity
            or body.get("current_full_point_sha256")!=context["actual"]["current_full_point_sha256"]
            or body.get("complete_model_identity_sha256")!=context["actual"]["model_identity_sha256"]
            or body.get("exact_fixed_target_identity_sha256")!=context["actual"]["exact_fixed_target_identity_sha256"]
            or body.get("accurate_request")!=job["request"]
            or body.get("normal_journal_binding_identity_sha256")!=job["identity"]
            or body.get("complete_original_stage_count")!=32
            or body.get("original_physical_stream")!=job["physical"]["file"]
            or body.get("original_journal")!=job["summary"]["journal"]
            or body.get("original_journal_header")!=job["summary"]["journal_header"]
            or body.get("complete") is not True
            or body.get("full_original_radial_domain_and_tail") is not True
            or body.get("normal_convention")!=NORMAL_CONVENTION
            or body.get("complete_closed_geometry_or_all_phases_certified") is not False):
        raise ValueError("A saved complete geometry block changed source, point, cover or scope")
    expected_path=(Path(record["path"]).resolve().parent/"whole-leaf-geometry.jsonl.gz").resolve()
    stream_record=body["whole_leaf_geometry_stream"]
    if Path(stream_record["path"]).resolve()!=expected_path:
        raise ValueError("The saved geometry block points to another stream namespace")
    path=outputs.verify(stream_record)
    expected=iter(r.refined_leaves(context,k))
    count=0
    footer=None
    with gzip.open(path,"rb") as handle:
        line=handle.readline()
        if not line.endswith(b"\n"):
            raise ValueError("A saved geometry stream has no complete header")
        header=r.strict_json(line)
        if (header.get("schema")!=STREAM_SCHEMA
                or header.get("producer_source_sha256")!=r.sha(__file__)
                or header.get("geometry_binding_identity_sha256")!=binding_identity
                or header.get("complete_normal_execution_binding_identity_sha256")!=context["binding_identity"]
                or header.get("current_full_point_sha256")!=context["actual"]["current_full_point_sha256"]
                or header.get("model_identity_sha256")!=context["actual"]["model_identity_sha256"]
                or header.get("normal_journal_binding_identity_sha256")!=job["identity"]
                or header.get("accurate_request")!=job["request"]
                or header.get("original_sixjet_stream")!=job["physical"]["file"]
                or header.get("original_stage_count")!=32
                or header.get("candidate_normal_convention")!=NORMAL_CONVENTION
                or header.get("original_working_F_J_or_root_replayed") is not False):
            raise ValueError("A saved geometry stream header changed")
        for raw in handle:
            if not raw.endswith(b"\n"):
                raise ValueError("A partial saved geometry leaf cannot be reused")
            item=r.strict_json(raw)
            if item.get("kind")=="complete_continuous_geometry_footer":
                footer=item
                break
            leaf=next(expected,None)
            count+=1
            support=item.get("support_cell",{})
            if (item.get("kind")!="complete_continuous_geometry_leaf"
                    or item.get("ordinal")!=count or item.get("source_physical_stream_ordinal")!=count
                    or leaf is None or item.get("exact_radial_leaf")!=leaf
                    or item.get("accurate_phi_interval")!=job["request"]["accurate_phi_interval"]
                    or support.get("id")!=job["request"]["id"]+"/"+leaf["id"]
                    or support.get("patch")!=PATCH or support.get("cell")!=count-1
                    or support.get("u_interval")!=["0","1"]
                    or support.get("phi_over_pi_interval")!=job["request"]["exact_phi_over_pi_interval"]
                    or support.get("exact_radial_leaf")!=leaf
                    or support.get("candidate_normal_convention")!=NORMAL_CONVENTION
                    or support.get("outward_orientation_or_full_closed_activity_claimed") is not False):
                raise ValueError("A saved support/geometry leaf changed its complete domain")
            for name in ("a_lower","b_lower","normal_norm_lower","normal_norm_upper"):
                k.rational(support[name])
            if k.rational(support["normal_norm_lower"])>k.rational(support["normal_norm_upper"]):
                raise ValueError("Saved normal-norm bounds are reversed")
        if handle.read(1):
            raise ValueError("A saved complete geometry stream has trailing records")
    outputs.verify(stream_record,force=True)
    if (footer is None or footer.get("all_original_radial_leaves_processed") is not True
            or footer.get("closed_surface_outward_orientation_or_reach_certified") is not False
            or footer.get("complete_leaf_count")!=count
            or count!=job["physical"]["complete_radial_leaf_count"]
            or footer.get("complete_statistics")!=body["complete_statistics"]
            or next(expected,None) is not None):
        raise ValueError("A saved geometry block does not contain the entire exact radial cover")
    statistics=Statistics()
    statistics.absorb(body["complete_statistics"])
    if statistics.count!=count:
        raise ValueError("Saved complete leaf statistics differ from the actual full stream")
    return block


class BlockJournal:
    def __init__(self,outdir,binding_identity,r):
        self.r=r
        self.header=dict(schema=JOURNAL_SCHEMA,geometry_binding_identity_sha256=binding_identity,
            complete_angle_blocks_are_atomic=True,missing_blocks_are_not_zero=True)
        self.header_record=immutable_json(outdir/"block-journal-binding.json",self.header,r)
        self.identity=r.canonical(self.header)
        self.path=outdir/"complete-block-journal.jsonl"
        self.events=[]
        self.blocks={}
        self.last=self.identity
        if self.path.exists():
            with self.path.open("rb") as handle:
                for raw in handle:
                    if not raw.endswith(b"\n"):
                        raise ValueError("A partial geometry journal line cannot be a complete block")
                    self._accept(r.strict_json(raw))

    def _accept(self,item):
        d=item.get("definition")
        if (not isinstance(d,dict) or item.get("sequence")!=len(self.events)+1
                or item.get("previous_identity_sha256")!=self.last
                or item.get("event_identity_sha256")!=self.r.canonical(d)
                or d.get("journal_binding_identity_sha256")!=self.identity
                or d.get("kind")!="complete_geometry_angle_block"):
            raise ValueError("The complete geometry block journal changed")
        name=d["job_id"]
        if not isinstance(name,str) or name in self.blocks:
            raise ValueError("A complete angular block was repeated")
        self.blocks[name]=d
        self.events.append(item)
        self.last=item["event_identity_sha256"]

    def append(self,job,record,block):
        d=dict(kind="complete_geometry_angle_block",journal_binding_identity_sha256=self.identity,
            job_id=job["request"]["id"],accurate_request=job["request"],
            complete_block_file=record,complete_block_identity_sha256=block["identity_sha256"],
            original_physical_stream=job["physical"]["file"])
        item=dict(sequence=len(self.events)+1,previous_identity_sha256=self.last,
            definition=d,event_identity_sha256=self.r.canonical(d))
        with self.path.open("ab") as handle:
            handle.write((json.dumps(item,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode())
            handle.flush()
            os.fsync(handle.fileno())
        self._accept(item)

    def recheck(self):
        expected=hashlib.sha256()
        for event in self.events:
            expected.update((json.dumps(event,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode())
        if self.path.exists() and self.r.sha(self.path)!=expected.hexdigest():
            raise ValueError("The complete saved journal changed after consumption")
        if self.events and not self.path.exists():
            raise ValueError("A complete saved geometry journal is missing")
        if self.r.file_record(self.header_record["path"])!=self.header_record:
            raise ValueError("The immutable geometry journal binding changed")

    def metadata(self):
        return dict(binding=self.header_record,binding_identity_sha256=self.identity,
            journal=(self.r.file_record(self.path) if self.path.exists() else None),
            complete_event_count=len(self.events),last_event_identity_sha256=self.last)


def derived_global_bounds(stats,context,k,complete):
    """Complete-cover bounds, including R717's same-leaf three-dimensional norm."""
    def maxval(key):
        item=stats.maxima.get(key)
        return None if item is None else item["value"]
    result=dict(full_upper_cover_bound_scope=complete,
        relative_Gram_error_operator_norm_upper=None,
        principal_curvature_absolute_upper=None,
        normal_norm_lower=None,upper_base_phase_diameter_upper=None,
        upper_base_phase_position_hull=None,
        full_upper_normal_positive_from_boxes=False,
        full_marked_surface_diameter_upper=None,
        complete_closed_surface_reach_lower=None,
        formal_reflection_fixed_caps_all_rotation_set_diameter_upper=None,
        formal_diameter_is_actual_phase_family_certificate=False)
    if not complete or stats.count==0:
        return result
    if stats.gram_missing==0:
        result["relative_Gram_error_operator_norm_upper"]=maxval("relative_Gram_error_operator_norm_upper")
    if stats.curvature_missing==0:
        result["principal_curvature_absolute_upper"]=maxval("principal_curvature_absolute_upper")
    result["normal_norm_lower"]=stats.minima["normal_norm_lower"]["value"]
    result["full_upper_normal_positive_from_boxes"]=stats.normal_unproved==0
    result["upper_base_phase_position_hull"]=stats.position
    d2=sum(((hi-lo)**2 for lo,hi in stats.position),F(0))
    result["upper_base_phase_diameter_upper"]=k.sqrt_bounds(d2,context["bits"])[1]
    rho=max(maxval("horizontal_position_norm_upper"),context["R"].hi,F(1,5))
    z=max(abs(stats.position[2][0]),abs(stats.position[2][1]),
        abs(k.rational(context["geometry"]["current_H"]))+F(1,1000))
    cylinder_diameter=2*k.sqrt_bounds(rho*rho+z*z,context["bits"])[1]
    # One leaf's x,y,z boxes bound one physical point simultaneously.
    # Rotations about the fixed origin and the lower reflection preserve |F|.
    upper_norm=maxval("full_position_norm_upper")
    if upper_norm is None or upper_norm<0:
        raise ValueError("The entire cover must retain every same-leaf position norm")
    cap_rho=max(context["R"].hi,F(1,5))
    cap_z=abs(k.rational(context["geometry"]["current_H"]))+F(1,1000)
    cap_norm=k.sqrt_bounds(cap_rho*cap_rho+cap_z*cap_z,context["bits"])[1]
    complete_set_norm=max(upper_norm,cap_norm)
    norm_diameter=2*complete_set_norm
    result["formal_reflection_fixed_caps_all_rotation_set_diameter_upper"]=min(
        cylinder_diameter,norm_diameter)
    result["formal_diameter_definition"]=dict(
        upper_set="the complete same-point upper-meridian image",
        lower_set="formal reflection (x,y,z)->(x,y,-z)",
        activity_motion="formal rotations about the fixed origin z axis",
        cap_set="formal disks of the current accurate R at +/-H with the fixed p4 recipe",
        cap_mark_height="1/1000",cap_mark_support_radius="1/5",
        horizontal_radius_upper=str(rho),absolute_z_upper=str(z),
        radius_support_disks_fit_from_current_R_lower=context["R"].lo>=F(1,5),
        diameter_method="minimum of the complete same-leaf three-dimensional norm bound and the complete coordinate-cylinder bound",
        same_leaf_position_norm_upper=str(upper_norm),
        cap_position_norm_upper=str(cap_norm),
        complete_rotation_reflection_and_cap_position_norm_upper=str(complete_set_norm),
        same_leaf_norm_diameter_upper=str(norm_diameter),
        separate_coordinate_cylinder_diameter_upper=str(cylinder_diameter),
        all_upper_lower_activity_phase_and_fixed_cap_pairs_in_formal_union=True,
        same_leaf_position_norms_come_from_all_complete_physical_sixjet_leaves=True,
        distinct_leaf_coordinate_extrema_not_combined_in_norm_bound=True,
        proof_reference="R717 section 9",
        additional_field_root_or_angle_evaluations=0,
        source_link_to_an_actual_closed_physical_family_proved=False)
    return result



def missing_geometric_responsibilities():
    return dict(
        eight_original_beta_evidence_roles=[
            "current_field_binding","physical_six_jets",
            "complete_activity_domain_and_seams","closed_sphere_immersion",
            "all_physical_phases","diameter_bound","activity_curvature_bound",
            "fixed_cap_parameters"],
        lower_reflection_and_full_activity_extension_if_using_only_upper_patch=
            "same_field_lower_reflection_and_all_activity_seams",
        original_beta_source_sha256=BETA_SOURCE[1],
        every_role_needs_complete_same_field_source_and_proof_bytes=True,
        roles_fabricated_from_upper_complete_flags=False,
        outward_unit_normal_identification_paid=False,
        complete_closed_C2_sphere_assembly_paid=False,
        all_physical_phases_paid=False,
        half_turn_branch_covariance_paid=False,
        upper_K_or_upper_D_relabelled_as_full_closed_bounds=False,
        complete_original_working_field_word_error_paid=False,
        original_external_parameter_J_and_transpose_error_paid=False,
        historical_unknown_peer_roles_removed=False)


def parse_args():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--normal-report",type=Path,required=True)
    parser.add_argument("--expected-normal-report-sha256")
    parser.add_argument("--outdir",type=Path,required=True)
    parser.add_argument("--seconds",type=float,default=900.0)
    args=parser.parse_args()
    if not math.isfinite(args.seconds) or args.seconds<=0:
        parser.error("Use a finite positive execution time budget; no bound is accepted by this budget")
    return args


def main():
    args=parse_args()
    r,reader_path=load_reader(args.repo)
    r.require_actions()
    started=time.monotonic()
    inputs=r.Files()
    outputs=r.Files()
    inputs.add(__file__)
    inputs.add(reader_path)
    k,kernel_record=r.load_arithmetic(args.repo,inputs)
    context=r.bind_input(args.normal_report,args.expected_normal_report_sha256,args.repo,inputs,k)
    jobs,branch=r.read_all_jobs(context,inputs,k)
    outdir=inputs.protect_output(args.outdir)
    outdir.mkdir(parents=True,exist_ok=True)
    source_records=dict(geometry_producer=r.file_record(__file__),
        complete_leaf_reader=r.file_record(reader_path),outward_arithmetic=kernel_record)
    if not context["available"]:
        inputs.recheck()
        result=dict(schema=SCHEMA,source_sha256=r.sha(__file__),
            source_commit=os.environ.get("GITHUB_SHA"),github_run_id=os.environ.get("GITHUB_RUN_ID"),
            github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
            complete=False,normal_report=context["record"],actual_source_files=source_records,
            reason=context["reason"],geometry_setup_available=False,
            all_input_bytes_rechecked=True,full_upper_cover_processed=False,
            continuous_Gram_bound_complete=False,continuous_curvature_bound_complete=False,
            continuous_support_numerator_bounds_complete=False,
            accurate_global_bounds=None,partial_processed_statistics=None,
            complete_closed_geometry_certified=False,remaining=missing_geometric_responsibilities(),
            new_working_field_J_or_root_calls=0,new_accurate_root_or_integrand_calls=0,
            original_solver_admission_gate=False,
            elapsed_seconds_binary64_hex=float(time.monotonic()-started).hex())
        record=write_report(outdir/"report.json",result,r)
        print(json.dumps(dict(schema=SCHEMA,report=record,complete=False,
            status="upstream-complete-binding-unavailable"),sort_keys=True))
        return 0
    whole_requests=[q for q in context["binding"]["complete_angle_requests"]
        if q["kind"]=="full_angle_cell"]
    leaves=list(r.refined_leaves(context,k))
    exact_mesh=[leaves[0]["left"]]+[q["right"] for q in leaves]
    binding=encoded(dict(schema=BINDING_SCHEMA,source_sha256=r.sha(__file__),
        actual_source_files=source_records,normal_fee_report=context["record"],
        complete_normal_execution_binding_identity_sha256=context["binding_identity"],
        complete_original_actual_input_identity_sha256=context["actual_identity"],
        complete_original_model=context["actual"]["complete_model"],
        complete_original_model_identity_sha256=context["actual"]["model_identity_sha256"],
        actual_current_full_point_sha256=context["actual"]["current_full_point_sha256"],
        actual_current_point_checkpoint=context["actual"]["current_point_arrays_file"],
        actual_snapshot_identity_sha256=context["actual"]["actual_snapshot_identity_sha256"],
        exact_fixed_target_identity_sha256=context["actual"]["exact_fixed_target_identity_sha256"],
        fixed_scalar_metric_identity_sha256=context["actual"]["fixed_scalar_metric_identity_sha256"],
        fixed_material_chart_identity_sha256=context["actual"]["fixed_chart_core_sha256"],
        complete_exact_radial_mesh_affine=exact_mesh,
        complete_exact_radial_leaves=leaves,
        original_exact_normal_partition=[str(v) for v in context["partition"]],
        original_stage_count=32,complete_whole_angle_requests=whole_requests,
        accurate_S=context["geometry"]["accurate_S"],accurate_R=context["geometry"]["accurate_R"],
        current_H=context["geometry"]["current_H"],precision_bits=context["bits"],
        target_metric="diag(1,(a_deep(s)*rho0(phi))^2)",
        normal_convention=NORMAL_CONVENTION,all_original_physical_lift_terms_retained=True,
        full_circle_without_symmetry_reduction=True,
        output_support_patch=PATCH,output_support_cell_mesh_is_full_exact_common_refinement=True,
        closed_outward_surface_or_physical_phase_assumed=False))
    identity=r.canonical(binding)
    binding_record=immutable_json(outdir/"complete-binding.json",binding,r)
    outputs.verify(binding_record)
    journal=BlockJournal(outdir,identity,r)
    blocks={}
    stats=Statistics()
    latest_unavailable=None
    final_recheck=False
    whole_ids={q["id"] for q in whole_requests}
    if not set(journal.blocks).issubset(whole_ids):
        raise ValueError("A saved geometry journal contains an unrequested angular job")
    for name,event in journal.blocks.items():
        job=jobs[name]
        if (job["complete"] is None or event.get("accurate_request")!=job["request"]
                or event.get("original_physical_stream")!=job["physical"]["file"]):
            raise ValueError("A saved complete block no longer has its original complete physical input")
        block=read_block(event["complete_block_file"],job,context,r,k,identity,outputs)
        if event["complete_block_identity_sha256"]!=block["identity_sha256"]:
            raise ValueError("The whole saved block differs from its journal")
        blocks[name]=dict(record=event["complete_block_file"],body=block)
        stats.absorb(block["definition"]["complete_statistics"])

    def report():
        all_processed=bool(whole_requests) and len(blocks)==len(whole_requests)
        upper_complete=(all_processed and branch.get("complete") is True
            and context["upstream_final_bytes_rechecked"] and context["report"].get("complete") is True
            and context["report"].get("all_planned_original_stages_and_sixjet_streams_complete") is True
            and final_recheck)
        global_bounds=derived_global_bounds(stats,context,k,upper_complete)
        return encoded(dict(schema=SCHEMA,source_sha256=r.sha(__file__),
            source_commit=os.environ.get("GITHUB_SHA"),github_run_id=os.environ.get("GITHUB_RUN_ID"),
            github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
            complete=upper_complete,complete_binding=binding_record,
            complete_binding_identity_sha256=identity,normal_report=context["record"],
            actual_source_files=source_records,
            actual_current_full_point_sha256=context["actual"]["current_full_point_sha256"],
            complete_original_model_identity_sha256=context["actual"]["model_identity_sha256"],
            actual_snapshot_identity_sha256=context["actual"]["actual_snapshot_identity_sha256"],
            exact_fixed_target_identity_sha256=context["actual"]["exact_fixed_target_identity_sha256"],
            fixed_scalar_metric_identity_sha256=context["actual"]["fixed_scalar_metric_identity_sha256"],
            full_exact_phi_over_pi_domain=["0","2"],full_exact_radial_domain_affine=[["0","0"],["1","0"]],
            original_stage_count=32,geometry_setup_available=True,
            expected_whole_angle_jobs=len(whole_requests),
            upstream_complete_whole_angle_jobs=sum(jobs[q["id"]]["complete"] is not None for q in whole_requests),
            processed_complete_whole_angle_jobs=len(blocks),
            expected_radial_leaves_per_angle=len(leaves),
            expected_complete_geometry_leaves=len(whole_requests)*len(leaves),
            processed_geometry_leaves=stats.count,
            full_upper_cover_processed=all_processed,
            continuous_Gram_bound_complete=upper_complete and stats.gram_missing==0,
            continuous_curvature_bound_complete=upper_complete and stats.curvature_missing==0,
            continuous_support_numerator_bounds_complete=upper_complete,
            complete_upper_immersion_lower_from_boxes=upper_complete and stats.normal_unproved==0,
            original_complete_angle_branch=branch,
            upstream_final_bound_bytes_rechecked=context["upstream_final_bytes_rechecked"],
            all_input_and_output_bytes_rechecked=final_recheck,
            accurate_global_bounds=global_bounds,
            partial_processed_statistics=stats.metadata(),
            completed_blocks=[dict(job_id=q["id"],complete_block=blocks[q["id"]]["record"],
                identity_sha256=blocks[q["id"]]["body"]["identity_sha256"])
                for q in whole_requests if q["id"] in blocks],
            unfinished_whole_angle_job_ids=[q["id"] for q in whole_requests if q["id"] not in blocks],
            complete_block_journal=journal.metadata(),
            latest_unavailable=latest_unavailable,
            complete_closed_geometry_certified=False,
            complete_upper_and_closed_C2_assembly_independently_proved=False,
            conditional_formal_reflection_diameter_not_relabelled=True,
            remaining=missing_geometric_responsibilities(),
            new_working_field_J_or_root_calls=0,new_accurate_root_or_integrand_calls=0,
            all_entire_physical_sixjet_input_errors_retained=True,
            original_solver_admission_gate=False,
            actual_budget_seconds_binary64_hex=float(args.seconds).hex(),
            elapsed_seconds_binary64_hex=float(time.monotonic()-started).hex()))

    write_report(outdir/"report.json",report(),r)
    try:
        for request in whole_requests:
            name=request["id"]
            if name in blocks:
                continue
            if time.monotonic()-started>=args.seconds:
                latest_unavailable=dict(reason="Execution budget reached before another complete angular block",
                    next_job_id=name,partial_is_not_geometric_impossibility=True)
                break
            job=jobs[name]
            if job["complete"] is None:
                latest_unavailable=dict(reason="The original accurate normal chain or physical stream is incomplete",
                    job_id=name,completed_original_stages=len(job["stages"]),
                    partial_is_not_geometric_impossibility=True)
                continue
            record,block=produce_angle_block(job,context,r,k,identity,outdir,inputs,outputs)
            journal.append(job,record,block)
            blocks[name]=dict(record=record,body=block)
            stats.absorb(block["definition"]["complete_statistics"])
            write_report(outdir/"report.json",report(),r)
        inputs.recheck()
        outputs.recheck()
        journal.recheck()
        final_recheck=True
    except Exception as error:
        latest_unavailable=dict(reason=str(error),exception_type=type(error).__name__,
            source_or_arithmetic_error_is_not_geometric_impossibility=True)
        write_report(outdir/"report.json",report(),r)
        raise
    result=report()
    record=write_report(outdir/"report.json",result,r)
    print(json.dumps(dict(schema=SCHEMA,report=record,complete=result["complete"],
        processed_complete_whole_angle_jobs=len(blocks),expected_whole_angle_jobs=len(whole_requests),
        continuous_Gram_bound_complete=result["continuous_Gram_bound_complete"],
        continuous_curvature_bound_complete=result["continuous_curvature_bound_complete"],
        continuous_support_numerator_bounds_complete=result["continuous_support_numerator_bounds_complete"],
        complete_closed_geometry_certified=False,new_working_F_J_root_calls=0),sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
