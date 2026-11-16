#!/usr/bin/env python3
"""R882: original exact 2058-by17 system at the common auxiliary place."""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import time
import traceback
import flint
from flint import nmod_mat

REPOSITORY="Rogerhu12/math-research-public"
RESULT="R882-original-cyclic-seven-common-place-coefficients"
FINAL="p41-original-cyclic-seven-common-place-coefficients-certificate.json"
PREFIX="R882-common-place-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
ROWS,DIM,TARGETS=2200,2058,17
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
STRATEGY={
    "scope": "common-place-seventeen-coefficients-only",
    "original_curve": "original genus127 Y at p41; original minus3 descent and level82 phase",
    "auxiliary_prime": 1000000753,
    "original_zeta_root": 549966761,
    "original_s_root": 99932770,
    "old_auxiliary_prime": 739,
    "integer_scale": "82^16",
    "matrix_shape": [
        2200,
        2058
    ],
    "right_hand_side_shape": [
        2200,
        17
    ],
    "column_order": "2050 original R799 V8 columns with only q109 from R801; eight completed R873 complements",
    "complement_V2_indices": [
        0,
        1,
        2,
        3,
        73,
        74,
        75,
        76
    ],
    "selected_rows": "exactly the completed R873 2058 selected coordinate rows",
    "matrix_column_block_size": 64,
    "verification_row_block_size": 64,
    "unit_minor_policy": "fixed original rows; stop honestly if singular at1000000753",
    "inverse_verification": "both complete2058 square products",
    "coordinate_verification": "all2200 rows for all17 targets",
    "target_column_order": "P coefficients0..8 then K coefficients0..7",
    "characteristic_zero_coordinates": "same exact R873 integer-minor unit-solve expression; not expanded",
    "old_739_coordinates_or_inverse_reused_as753": False,
    "new_Eisenstein_tail_or_exact_norm_recomputed": False,
    "target_normal_basis_computed": False,
    "nine_reference_norms_computed": False,
    "original_Picard_support_computed": False,
    "height_or_nonp_calibration_computed": False,
    "budget_and_transport_excluded_from_identity": True
}

class BudgetStop(RuntimeError):
    pass

class UnitFailure(RuntimeError):
    pass

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for part in iter(lambda:f.read(4*1024*1024),b""):
            h.update(part)
    return h.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as f:
        return json.load(f)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if path.suffix==".gz":
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0) as g:
                g.write(raw)
    else:
        tmp.write_bytes(raw)
    tmp.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def plain(row):
    ans={k:row[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(ans["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in ans["file"]
    assert isinstance(ans["bytes"],int) and ans["bytes"]>=0
    assert re.fullmatch("[0-9a-f]{64}",ans["sha256"])
    return ans

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def identity(source):
    return {**{k:source[k] for k in BASE},
            "configuration_sha256":source["configuration_sha256"],
            "certificate":plain(source["certificate"]),
            "selected_files_sha256":fingerprint(source["files"])}

def ref(group,row):
    return dict(plain(row),source_group=group)

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"p":41,
            "python_flint":"0.9.0","proofs":item["proofs"],
            "method_sha256":item["method_sha256"],
            "sources":{g:identity(item["retained_sources"][g]) for g in ("R873","R799","R801")},
            "inputs":item["inputs"],"original_carrier":item["original_carrier"],
            "strategy":STRATEGY}

def matrix_rows(a):
    return [[int(a[i,j]) for j in range(a.ncols())] for i in range(a.nrows())]

def matrix(data):
    return nmod_mat(data,P)

def eye(n):
    return matrix([[int(i==j) for j in range(n)] for i in range(n)])

def shape(a,m,n):
    assert len(a)==m and all(len(row)==n for row in a)

class Source:
    def __init__(self,root,label,source):
        self.label=label;self.source=source
        self.directory=Path(root)/label
        self.files={name:plain(row) for name,row in source["files"].items()}
        assert all(name==row["file"] for name,row in self.files.items())
        mpath=self.directory/MANIFEST
        assert sha(mpath)==source["manifest_sha256"]
        manifest=read(mpath)
        assert manifest["result"]==source["result"]
        entries={row["file"]:plain(row) for row in manifest["files"]}
        assert len(entries)==len(manifest["files"])
        entries[MANIFEST]=spec(mpath)
        assert all(entries[name]==row for name,row in self.files.items())
        self.checked=set()
        self.certificate=self.get(source["certificate"]["file"])
        assert self.certificate["result"]==source["result"] and self.certificate["complete"] is True
        self.tag=self.certificate["configuration"]
        assert fingerprint(self.tag)==source["configuration_sha256"]
        assert self.tag.get("source_sha256",self.tag.get("core_sha256"))==source["core_sha256"]

    def get(self,name):
        row=self.files[name];path=self.directory/name
        if name not in self.checked:
            assert spec(path)==row,(self.label,name,"source SHA")
            self.checked.add(name)
        return read(path)

    def stage(self,row):
        row=plain(row);assert self.files[row["file"]]==row
        value=self.get(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        return value

class Job:
    def __init__(self,args):
        self.args=args;self.started=time.monotonic()
        self.out=Path(args.output);self.out.mkdir(parents=True,exist_ok=True)
        self.item=read(args.config)
        assert self.item["result"]==RESULT and self.item["p"]==41
        assert self.item["producer_inputs_pending"] is False
        assert sha(__file__)==self.item["core_sha256"]
        assert flint.__version__=="0.9.0"
        topic=Path(__file__).resolve().parent.parent
        for value in self.item["proofs"].values():
            assert sha(topic/value["path"])==value["sha256"]
        assert sha(topic/self.item["method"])==self.item["method_sha256"]
        assert set(self.item["retained_sources"])=={"R873","R799","R801"}
        self.sources={g:Source(args.retained,g,self.item["retained_sources"][g])
                      for g in ("R873","R799","R801")}
        self.tag=expected_tag(self.item)
        self.inputs=self.item["inputs"];self.refs={};self.block_refs=[];self.verify_refs=[]
        self.current=None;self.A=None;self.Y=None;self.U=None;self.C=None
        self.c873=self.sources["R873"].certificate
        assert self.c873["actual_auxiliary_prime"]==739
        assert self.c873["all17_exact_characteristic_zero_unit_solve_expressions_certified"] is True
        assert self.c873["all2200_original_modular_coordinate_relations_verified"] is True
        assert self.c873["actual_original_cyclic7_correspondence_source_target_expression_certified"] is True
        assert self.c873["actual_new_complement_V2_indices"]==STRATEGY["complement_V2_indices"]
        for key,right in (("section_basis","section_basis"),("target_index","norm_target_index"),
                          ("exact_expression","exact_coordinate_expression"),("correspondence_DAG","correspondence_DAG")):
            assert plain(self.inputs[key])==plain(self.c873[right])
            assert self.inputs[key]["source_group"]=="R873"
        self.basis=self.input("section_basis")
        self.target_index=self.input("target_index")
        self.original_expression=self.input("exact_expression")
        self.program=self.input("correspondence_DAG")
        self.index=self.input("V8_index")
        self.frontier=self.input("V8_frontier")
        self.plan=self.input("recipe_plan")
        self.selected=list(self.basis["selected_coordinate_rows"])
        assert len(self.selected)==DIM and len(set(self.selected))==DIM
        assert all(isinstance(i,int) and 0<=i<ROWS for i in self.selected)
        assert self.basis["prime"]==739 and self.basis["actual_2058_minor_determinant"]==510
        assert self.basis["independent_columns"]==self.basis["actual_nonzero_minor_rank"]==DIM
        self.complements=self.basis["selected_complement"]
        assert [v["original_V2_index"] for v in self.complements]==STRATEGY["complement_V2_indices"]
        assert self.original_expression["basis_minor"]==plain(self.inputs["section_basis"])
        assert self.original_expression["target_index"]==plain(self.inputs["target_index"])
        assert self.original_expression["selected_coordinate_rows"]==self.selected
        assert self.original_expression["all2200_coordinates_for_all17_targets_verified_mod_prime"] is True
        assert self.original_expression["prime"]==739
        assert self.program["coefficient_unit_solve"]==plain(self.inputs["exact_expression"])
        assert self.program["exact_original_correspondence_expression_certified"] is True
        assert self.index["dimension"]==2050 and self.index["ordinary_power"]==8
        assert self.index["bound_qY"]==108 and self.index["integer_scale"]==str(82**16)
        assert self.index["characteristic_zero_basis_certified"] is True
        assert len(self.index["basis_rows"])==len(self.frontier["basis_rows"])==2050
        assert self.frontier["new_first_exponent"]==109
        self.nodes={v["node_key"]:v for v in self.plan["nodes"]}
        assert len(self.nodes)==len(self.plan["nodes"])
        assert self.plan["primary_targets"]["8"]==[v["node_key"] for v in self.frontier["basis_rows"]]
        assert self.target_index["actual_target_count"]==TARGETS
        assert len(self.target_index["targets"])==TARGETS
        assert len(self.target_index["P_coefficients"])==9 and len(self.target_index["K_coefficients"])==8
        self.source_audit()

    def input(self,key):
        row=self.inputs[key];return self.sources[row["source_group"]].stage(row)

    def budget(self):
        if time.monotonic()-self.started>self.args.budget_minutes*60:
            raise BudgetStop("R882 budget reached; complete new-place stages are reusable.")

    def path(self,name):
        return self.out/(PREFIX+name+".json.gz")

    def old(self,name):
        path=self.path(name)
        if not path.exists():
            return None
        value=read(path)
        assert value["result"]==RESULT and value["configuration"]==self.tag
        assert value["complete"] is True
        self.refs[name]=spec(path)
        return value

    def put(self,name,value):
        full={"result":RESULT,"complete":True,"configuration":self.tag,**value}
        path=self.path(name)
        if path.exists():
            assert read(path)==full
        else:
            save(path,full)
        self.refs[name]=spec(path)
        return full

    def checkpoint(self,phase):
        value={"result":RESULT,"complete":False,"configuration":self.tag,
               "phase":phase,"completed_stage_specs":dict(self.refs),
               "new_auxiliary_prime":P,"old_auxiliary_prime":739,
               "old_arithmetic_recomputed":False}
        save(self.path("current"),value);self.current=spec(self.path("current"))

    def source_audit(self):
        if self.old("source-audit") is None:
            self.put("source-audit",{
                "sources":{g:identity(self.item["retained_sources"][g]) for g in self.sources},
                "inputs":self.inputs,"original_carrier":self.item["original_carrier"],
                "old_auxiliary_prime":739,"new_auxiliary_prime":P,
                "original_zeta_root":549966761,"original_s_root":99932770,
                "source_integer_matrix_shape":[ROWS,DIM],"source_integer_rhs_shape":[ROWS,TARGETS],
                "original_selected_coordinate_rows":self.selected,
                "actual_completed_original_eight_complement_indices":STRATEGY["complement_V2_indices"],
                "old_characteristic_zero_unit_solve_expression":self.inputs["exact_expression"],
                "source_global_injectivity_20_times110_gt2184":True,
                "same_exact_original_matrix_and_target_columns":True,
                "old_source_tags_and_bytes_preserved":True,
                "old_mod739_coordinates_not_used_as_mod1000000753":True,
                "new_exact_series_norm_or_Berkowitz_computed":False})
        self.checkpoint("sources_bound")

    def original_column(self,index):
        if index<2050:
            entry=self.index["basis_rows"][index];frontier=self.frontier["basis_rows"][index]
            assert entry["index"]==frontier["index"]==index
            old=self.sources["R799"].stage(entry)
            assert old["integer_scale"]==str(82**16) and old["bound_qY"]==108
            assert old["recipe"]==frontier["original_recipe"]
            node=self.nodes[frontier["node_key"]]
            assert node["node_fingerprint"]==frontier["node_fingerprint"]
            assert node["ordinary_power"]==8 and node["original_recipe"]==old["recipe"]
            prefixes=[v for v in frontier["original_prefix_segments"]
                      if v["producer"]=="R799" and v["first"]==0 and v["stop"]==109]
            assert len(prefixes)==1 and plain(prefixes[0])==plain(entry)
            tails=[v for v in frontier["new_tail_segments"] if v["first"]<=109<v["stop"]]
            assert len(tails)==1 and tails[0]["producer"]=="R801"
            tail=self.sources["R801"].stage(tails[0])
            assert tail["node_key"]==frontier["node_key"]
            assert tail["node_fingerprint"]==frontier["node_fingerprint"]
            assert tail["first_exponent"]==tails[0]["first"]
            assert tail["last_exponent_exclusive"]==tails[0]["stop"]
            assert tail["old_coefficients_recomputed"] is False
            rows=old["integer_v_t_coefficients"]
            shape(rows,109,20)
            last=tail["integer_v_t_coefficients"][109-tails[0]["first"]]
            assert len(last)==20
            values=[int(v)%P for row in rows for v in row]+[int(v)%P for v in last]
            sources={"old_prefix":ref("R799",entry),"only_q109_tail":ref("R801",tails[0]),
                     "original_node_key":frontier["node_key"],"ordinary_power":8}
        else:
            entry=self.complements[index-2050]
            value=self.sources["R873"].stage(entry["candidate"])
            assert value["original_V2_index"]==entry["original_V2_index"]
            assert value["integer_scale"]==str(82**16)
            shape(value["integer_v_t_coefficients"],110,20)
            values=[int(v)%P for row in value["integer_v_t_coefficients"] for v in row]
            sources={"completed_original_complement":ref("R873",entry["candidate"]),
                     "original_V2_index":entry["original_V2_index"]}
        assert len(values)==ROWS
        return values,sources

    def reductions(self):
        self.block_refs=[]
        for first in range(0,DIM,64):
            stop=min(DIM,first+64);name=f"matrix-columns-{first:04d}-{stop:04d}"
            value=self.old(name)
            if value is None:
                columns=[];sources=[]
                for index in range(first,stop):
                    self.budget()
                    col,source=self.original_column(index)
                    columns.append(col);sources.append(dict(source,original_basis_index=index))
                value=self.put(name,{
                    "prime":P,"column_interval":[first,stop],"matrix_shape":[ROWS,stop-first],
                    "coordinate_order":"qY exponent first0..109; original real coordinate0..19",
                    "original_integer_scale":str(82**16),
                    "original_column_sources":sources,
                    "matrix_mod_prime":[[columns[j][i] for j in range(stop-first)] for i in range(ROWS)],
                    "only_new_modular_reduction":True,"old_q_coefficients_recomputed":False})
            assert value["prime"]==P and value["column_interval"]==[first,stop]
            shape(value["matrix_mod_prime"],ROWS,stop-first)
            self.block_refs.append(self.refs[name])
            self.checkpoint("matrix_reductions")
        target=self.old("seventeen-target-reductions")
        if target is None:
            self.budget();columns=[]
            for entry in self.target_index["targets"]:
                value=self.sources["R873"].stage(entry)
                assert value["integer_scale"]==str(82**16) and value["qY_count"]==110
                shape(value["integer_v_t_coefficients"],110,20)
                columns.append([int(v)%P for row in value["integer_v_t_coefficients"] for v in row])
            target=self.put("seventeen-target-reductions",{
                "prime":P,"source_target_index":self.inputs["target_index"],
                "original_target_specs":[ref("R873",r) for r in self.target_index["targets"]],
                "matrix_shape":[ROWS,TARGETS],
                "matrix_mod_prime":[[columns[j][i] for j in range(TARGETS)] for i in range(ROWS)],
                "column_order":"P0..P8,K0..K7",
                "original_integer_scale":str(82**16),"exact_norm_or_series_recomputed":False})
        shape(target["matrix_mod_prime"],ROWS,TARGETS)
        self.Y=target["matrix_mod_prime"]
        if self.old("original-matrix-index") is None:
            self.put("original-matrix-index",{
                "prime":P,"matrix_shape":[ROWS,DIM],"selected_coordinate_rows":self.selected,
                "matrix_column_blocks":self.block_refs,
                "right_hand_side":self.refs["seventeen-target-reductions"],
                "source_exact_expression":self.inputs["exact_expression"],
                "all_original_columns_present_once_in_original_order":True})
        self.checkpoint("complete_modular_matrix")

    def assemble_rows(self,indices):
        out=[[] for _ in indices]
        for row in self.block_refs:
            self.budget()
            value=read(self.out/row["file"])
            assert spec(self.out/row["file"])==plain(row)
            assert value["configuration"]==self.tag and value["complete"] is True
            data=value["matrix_mod_prime"]
            for local,index in enumerate(indices):
                out[local].extend(data[index])
        shape(out,len(indices),DIM)
        return out

    def inverse(self):
        value=self.old("selected-unit-inverse")
        if value is None:
            self.budget();A=matrix(self.assemble_rows(self.selected))
            determinant_stage=self.old("selected-minor-determinant")
            det=int(A.det()) if determinant_stage is None else determinant_stage["actual_determinant_mod_prime"]
            if determinant_stage is None:
                self.put("selected-minor-determinant",{
                    "prime":P,"source_matrix_index":self.refs["original-matrix-index"],
                    "selected_coordinate_rows":self.selected,"matrix_shape":[DIM,DIM],
                    "actual_determinant_mod_prime":det,"actual_unit_minor":bool(det)})
            else:
                assert determinant_stage["prime"]==P
                assert determinant_stage["selected_coordinate_rows"]==self.selected
                assert determinant_stage["source_matrix_index"]==self.refs["original-matrix-index"]
            if det==0:
                raise UnitFailure("The fixed original2058 rows are singular at1000000753; no same-place coefficients accepted.")
            self.budget();U=A.inv()
            I=eye(DIM)
            assert A*U==I and U*A==I
            self.put("selected-unit-inverse",{
                "prime":P,"source_matrix_index":self.refs["original-matrix-index"],
                "source_determinant":self.refs["selected-minor-determinant"],
                "selected_coordinate_rows":self.selected,"matrix_shape":[DIM,DIM],
                "actual_determinant_mod_prime":det,"inverse_matrix_mod_prime":matrix_rows(U),
                "both_complete_inverse_products_verified":True,
                "exact_original_minor_is_unit_at_new_place":True,
                "old_mod739_inverse_reused":False,
                "new_complete_mod1000000753_inverse_computed":True})
            self.U=U
        else:
            assert value["prime"]==P and value["selected_coordinate_rows"]==self.selected
            assert value["both_complete_inverse_products_verified"] is True
            assert 0<value["actual_determinant_mod_prime"]<P
            shape(value["inverse_matrix_mod_prime"],DIM,DIM)
            self.U=matrix(value["inverse_matrix_mod_prime"])
        self.checkpoint("complete_new_unit_inverse")

    def solve(self):
        value=self.old("seventeen-coordinates")
        if value is None:
            self.budget();YJ=matrix([self.Y[i] for i in self.selected])
            C=self.U*YJ
            self.put("seventeen-coordinates",{
                "prime":P,"basis_dimension":DIM,"target_count":TARGETS,
                "source_inverse":self.refs["selected-unit-inverse"],
                "source_rhs":self.refs["seventeen-target-reductions"],
                "source_exact_R873_unit_solve":self.inputs["exact_expression"],
                "coordinate_matrix_mod_prime":matrix_rows(C),
                "column_order":"P0..P8,K0..K7",
                "same_characteristic_zero_coefficients_integral_at_new_place":True,
                "characteristic_zero_coordinates_expanded":False,
                "old_mod739_coordinates_relabelled":False})
            self.C=C
        else:
            assert value["prime"]==P and value["source_inverse"]==self.refs["selected-unit-inverse"]
            shape(value["coordinate_matrix_mod_prime"],DIM,TARGETS)
            self.C=matrix(value["coordinate_matrix_mod_prime"])
        self.checkpoint("seventeen_new_place_coordinates")

    def verify_all(self):
        self.verify_refs=[]
        # Read each saved reduced matrix block once; original exact q rows are not recomputed.
        if self.A is None:
            self.A=self.assemble_rows(list(range(ROWS)))
        for first in range(0,ROWS,64):
            stop=min(ROWS,first+64);name=f"full-relations-{first:04d}-{stop:04d}"
            value=self.old(name)
            if value is None:
                self.budget()
                actual=matrix(self.A[first:stop])*self.C
                target=matrix(self.Y[first:stop])
                assert actual==target,("full_original_coordinate_relation",first,stop)
                self.put(name,{
                    "prime":P,"coordinate_row_interval":[first,stop],
                    "target_columns":list(range(TARGETS)),
                    "source_matrix_index":self.refs["original-matrix-index"],
                    "source_coordinates":self.refs["seventeen-coordinates"],
                    "source_target_reductions":self.refs["seventeen-target-reductions"],
                    "actual_product_rows_sha256":fingerprint(matrix_rows(actual)),
                    "all_original_rows_and_all17_targets_verified":True,
                    "verification_is_full_original_basis_not_only_selected_minor":True})
            else:
                assert value["coordinate_row_interval"]==[first,stop]
                assert value["all_original_rows_and_all17_targets_verified"] is True
                assert value["source_coordinates"]==self.refs["seventeen-coordinates"]
            self.verify_refs.append(self.refs[name])
            self.checkpoint("full_original_relations")
        if self.old("same-place-correspondence-coefficients") is None:
            inverse=read(self.out/self.refs["selected-unit-inverse"]["file"])
            self.put("same-place-correspondence-coefficients",{
                "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
                "source_R873_correspondence_DAG":self.inputs["correspondence_DAG"],
                "source_R873_exact_unit_solve":self.inputs["exact_expression"],
                "original_basis_index":self.inputs["V8_index"],
                "original_frontier":self.inputs["V8_frontier"],
                "old_original_basis_minor":self.inputs["section_basis"],
                "new_complete_inverse":self.refs["selected-unit-inverse"],
                "new_modular_coordinates":self.refs["seventeen-coordinates"],
                "full_verification_stages":self.verify_refs,
                "actual_new_minor_determinant":inverse["actual_determinant_mod_prime"],
                "all2200_by17_original_equations_verified":True,
                "all17_same_exact_coefficient_expressions_reduced_at_common_place":True,
                "normalizations_and_original_source_target_descent_unchanged":True,
                "P_columns":list(range(9)),"K_columns":list(range(9,17)),
                "all2058_original_basis_columns_preserved":True,
                "new_exact_norm_or_series_computed":False,
                "characteristic_zero_coefficients_expanded":False,
                "target_normal_basis_computed":False,"nine_reference_norms_computed":False,
                "original_Picard_support_computed":False,"height_or_nonp_calibration_computed":False})
        self.checkpoint("common_place_complete")

    def manifest(self):
        entries=[]
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name==self.path("current").name or path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value=read(path)
            assert value["result"]==RESULT and value["configuration"]==self.tag
            assert value["complete"] is True
            entries.append(spec(path))
        current=spec(self.path("current")) if self.path("current").exists() else None
        value={"result":RESULT,"complete":True,"configuration":self.tag,
               "files":entries,"current_checkpoints":[] if current is None else [current],
               "all_listed_mathematical_stages_complete":True}
        name="stage-manifest-"+fingerprint(value)
        path=self.path(name)
        if path.exists():
            assert read(path)==value
        else:
            save(path,value)
        return spec(path)

    def finish(self,complete,error):
        done="same-place-correspondence-coefficients" in self.refs
        inverse=self.old("selected-unit-inverse")
        value={"result":RESULT,"configuration":self.tag,"complete":bool(complete),"p":41,
               "old_auxiliary_prime":739,"actual_auxiliary_prime":P,
               "original_zeta_root":549966761,"original_s_root":99932770,
               "source_audit":self.refs.get("source-audit"),
               "original_matrix_index":self.refs.get("original-matrix-index"),
               "new_complete_unit_inverse":self.refs.get("selected-unit-inverse"),
               "seventeen_coordinates":self.refs.get("seventeen-coordinates"),
               "same_place_correspondence_coefficients":self.refs.get("same-place-correspondence-coefficients"),
               "actual_new_minor_determinant":None if inverse is None else inverse["actual_determinant_mod_prime"],
               "actual_matrix_shape":[ROWS,DIM],"actual_target_shape":[ROWS,TARGETS],
               "all17_same_exact_coefficient_expressions_reduced_at_common_place":done,
               "all2200_by17_original_equations_verified":done,
               "both_complete_inverse_products_verified":inverse is not None,
               "old739_coordinates_or_inverse_relabelled":False,
               "old_exact_norm_Berkowitz_or_q_tail_recomputed":False,
               "R879_reference_system_recomputed":False,"old_Krylov_inverses_recomputed":False,
               "characteristic_zero_coefficients_expanded":False,
               "target_normal_basis_computed":False,"nine_reference_norms_computed":False,
               "original_Picard_support_computed":False,"height_or_nonp_calibration_computed":False,
               "stage_manifest":self.manifest(),"resume_state":self.current,
               "failure_or_stop_reason":error,"seconds":time.monotonic()-self.started}
        if complete:
            assert done and inverse is not None
        save(self.out/FINAL,value)
        return value

    def run(self):
        self.reductions();self.inverse();self.solve();self.verify_all()
        return self.finish(True,None)

def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise SystemExit("R882 new arithmetic runs only in the authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    parser.add_argument("--retained",required=True)
    parser.add_argument("--output",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args=parser.parse_args();assert 0<args.budget_minutes<=300
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    job=None;final=None;code=1;error=None;started=time.monotonic()
    try:
        job=Job(args);final=job.run();code=0
    except BudgetStop as exc:
        code=124;error=str(exc)
    except UnitFailure as exc:
        code=2;error=str(exc)
    except Exception as exc:
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    if code and job is not None:
        final=job.finish(False,error)
    receipt={"result":RESULT,"source_sha256":sha(__file__),"complete":code==0,
             "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
             "configuration":None if job is None else job.tag,
             "certificate_sha256":sha(out/FINAL) if (out/FINAL).exists() else None,
             "all_new_mathematics_only_in_public_Actions":True}
    save(out/"core-receipt.json",receipt)
    print("R882_CORE_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()
