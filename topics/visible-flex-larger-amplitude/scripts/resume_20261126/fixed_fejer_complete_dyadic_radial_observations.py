#!/usr/bin/env python3
"""Complete fixed-target J923 -> J1845 radial observations and old-row inclusion.

The current grid contains its entire native node/midpoint/six-Gauss plan
and every original observation. Coordinates are exact affine Fraction pairs;
old cells/local words are decoded under J923 before exact dyadic transfer.
The original fixed scalar is queried from its actual complete preparation.
No scalar values are interpolated, no rows are dropped, and no old field
or geometry values are inherited.

Scientific reconstruction, quadrature carriers and scalar queries run only
in the public Actions repository. Importing this source does no science.
"""
from __future__ import annotations

from fractions import Fraction as F
import copy
import hashlib
import heapq
import inspect
import json
import math
import os
from pathlib import Path
import time

SCHEMA = "complete-fixed-fejer-target-dyadic-radial-observation-union-v1"
REFERENCE_SHA = "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
DEEP_SHA = "e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"
OBSERVED_SHA = "26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d"
LAYOUT_SHA = "a31d80a953722cc3644f793e4a28a372d980f6d0af7c8d98402f5f4739e3b5cf"
CURRENT_J = 1845
REFERENCE_J = 923


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Full dyadic observations and exact scalar queries require public Actions")


def sha(path):
    result=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda:stream.read(1<<20),b""):
            result.update(chunk)
    return result.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    import numpy as np
    value=np.ascontiguousarray(value)
    result=hashlib.sha256(str(value.dtype).encode())
    result.update(json.dumps(list(value.shape)).encode())
    result.update(value.tobytes())
    return result.hexdigest()


def actual_file(record):
    if (not isinstance(record,dict) or not isinstance(record.get("path"),str)
            or not isinstance(record.get("sha256"),str)
            or type(record.get("bytes")) is not int or record["bytes"]<0):
        raise ValueError("Keep the complete actual immutable reference input record")
    path=Path(record["path"]).resolve(strict=True)
    if not path.is_file() or path.stat().st_size!=record["bytes"] or sha(path)!=record["sha256"]:
        raise ValueError("An actual fixed-reference input file changed: "+str(path))
    return dict(path=str(path),sha256=record["sha256"],bytes=record["bytes"])


def definition(reference_model,radial_layout,*,observation_arrays):
    if (not isinstance(reference_model,dict)
            or reference_model.get("source_sha256")!=REFERENCE_SHA
            or reference_model.get("J")!=REFERENCE_J or reference_model.get("M")!=160
            or not isinstance(radial_layout,dict)
            or radial_layout.get("reference_J")!=REFERENCE_J
            or radial_layout.get("current_J")!=CURRENT_J
            or radial_layout.get("complete_original_reference_model")!=reference_model
            or radial_layout.get("source_sha256")!=LAYOUT_SHA):
        raise ValueError("Bind the same complete fixed reference and the full dyadic node definition")
    required=("cells","local_u","times","a","a_error","time_error","legacy_simpson",
        "current_gauss","retained_parent_quadrature","mixed_quadrature",
        "parent_stage_map","parent_a","parent_simpson","parent_quadrature")
    if (not isinstance(observation_arrays,dict) or set(observation_arrays)!=set(required)
            or any(not isinstance(observation_arrays[k],dict)
                or set(observation_arrays[k])!={"sha256","shape","dtype"}
                for k in required)):
        raise ValueError("Keep every complete observation, weight and original-row array identity")
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        complete_original_reference_model=copy.deepcopy(reference_model),
        original_reference_model_identity_sha256=canonical(reference_model),
        fixed_scalar_metric_identity_sha256=reference_model["fixed_scalar_metric_identity_sha256"],
        complete_radial_layout_definition=copy.deepcopy(radial_layout),
        radial_layout_identity_sha256=canonical(radial_layout),
        reference_source_sha256=REFERENCE_SHA,deep_scalar_source_sha256=DEEP_SHA,
        original_observation_source_sha256=OBSERVED_SHA,radial_layout_source_sha256=LAYOUT_SHA,
        reference_J=REFERENCE_J,current_J=CURRENT_J,full_N=2048,
        native_observation_order=6,
        native_legacy_prefix_count=2*CURRENT_J-1,
        original_observation_count=7377,original_legacy_prefix_count=1845,
        complete_observation_arrays=copy.deepcopy(observation_arrays),
        new_quadrature="Q_current = (G_native_current + Q_parent_transferred)/2",
        complete_row_weight="W(f) = f*S_native_current + (1-f)*Q_current, 0<f<1",
        complete_common_parent_rule="W_parent(f) = f*S_parent + (1-f)*Q_parent on all 7377 literal parent rows",
        exact_old_address_transfer="(i,u) -> (2*i,2*u) if u<=1/2, else (2*i+1,2*u-1)",
        original_local_words_interpreted_under_original_J=True,
        complete_old_rows_retained=True,complete_new_rows_retained=True,
        old_common_a_words_checked_and_retained=True,
        all_new_a_from_same_exact_original_scalar_oracle=True,
        scalar_interpolation_used=False,mathematical_metric_redefined=False,
        old_finite_objective_inherited_as_new_grid_objective=False,
        ordinary_weight_and_field_quadrature_errors_enclosed=False,
        original_geometry_values_or_certificates_inherited=False)


def counted_tail_class(deep_module):
    """A declared fixed-work table; exact scalar kernels and integer tie order stay original."""
    class ReconstructedTail(deep_module.DeepValleyTail):
        def __init__(self, full, *, original_input_identity, target_leaves,
                     epsilon, integral_tolerance, historical_clock_seconds):
            self.reconstruction_leaf_target = int(target_leaves)
            if self.reconstruction_leaf_target < 1:
                raise ValueError('A positive predeclared deterministic live-leaf count is required')
            super().__init__(full, input_identity=original_input_identity,
                epsilon=epsilon, integral_tolerance=integral_tolerance,
                admission_seconds=historical_clock_seconds)

        def _build_integral_table(self):
            # The original e091 table body is preserved below except that its
            # wall-clock admission comparison is replaced by the predeclared
            # live-leaf count.  All per-leaf operations and tie order are exact.
            tail = self._tail_integrals(self.epsilon)
            points = sorted(set((self.epsilon,F(1,8),F(1,4))))
            live,heap,sequence = {},[],0
            total = list(tail)
            def admit(leaf):
                nonlocal sequence
                sequence += 1
                live[sequence] = leaf
                width = sum(value[1]-value[0] for value in leaf['values'])
                heapq.heappush(heap,(-width,sequence))
                for j in range(2):
                    total[j] = deep_module.add(total[j],leaf['values'][j])
            for low,high in zip(points,points[1:]):
                admit(self._leaf(low,high))
            count = len(live)
            while heap:
                uncertainty = max(F(value[1]-value[0],deep_module.SCALE)*self.width
                                  for value in total)
                if uncertainty <= self.integration_tolerance:
                    break
                if len(live) >= self.reconstruction_leaf_target:
                    break
                _,key = heapq.heappop(heap)
                leaf = live.pop(key)
                for j in range(2):
                    total[j] = (total[j][0]-leaf['values'][j][0],
                                total[j][1]-leaf['values'][j][1])
                middle = (leaf['low']+leaf['high'])/2
                admit(self._leaf(leaf['low'],middle))
                admit(self._leaf(middle,leaf['high']))
                count += 2
            self.leaves = sorted(live.values(),key=lambda leaf:leaf['low'])
            self.total_integrals_dimensionless = tuple(total)
            self.leaves_evaluated = count
            self.integral_uncertainty = max(F(value[1]-value[0],deep_module.SCALE)*self.width
                                            for value in total)
            self.requested_integral_accuracy_reached = (
                self.integral_uncertainty <= self.integration_tolerance)
            if len(self.leaves) != self.reconstruction_leaf_target:
                raise ArithmeticError('The exact accuracy stop preceded the declared fixed-work leaf count')
    return ReconstructedTail



def _restore_actual_scalar(context):
    """Reconstruct the actual CURRENT table, not the historical 2397-leaf input."""
    require_actions()
    d=context.modules["deep_scalar"]
    if sha(d.__file__)!=DEEP_SHA or sha(d.DeepValleyTail.metadata.__code__.co_filename)!=DEEP_SHA:
        raise ValueError("Use the whole original exact scalar and all its integral methods")
    report=context.preparation
    actual=report.get("true_scalar")
    if (not isinstance(actual,dict) or actual.get("definition")!=context.scalar_definition
            or actual.get("model_identity_sha256")!=context.scalar_identity
            or canonical(actual["definition"])!=context.scalar_identity
            or actual.get("all_tail_domain_included") is not True
            or actual.get("unresolved_oscillations_dropped") is not False
            or type(actual.get("requested_integral_accuracy_reached")) is not bool
            or type(actual.get("integral_leaves")) is not int or actual["integral_leaves"]<1
            or type(actual.get("integral_leaves_evaluated")) is not int):
        raise ValueError("Read the complete actual current preparation scalar definition and result")
    scalar_class=counted_tail_class(d)
    started=time.monotonic()
    deep=scalar_class(context.full,
        original_input_identity=copy.deepcopy(context.scalar_definition["original_input"]),
        target_leaves=actual["integral_leaves"],
        epsilon=F(actual["infinite_tail_cutoff_exact"]),
        integral_tolerance=F(actual["requested_integral_width_exact"]),
        historical_clock_seconds=actual["admission_seconds"])
    observed=deep.metadata()
    left={k:v for k,v in observed.items() if k!="elapsed_seconds"}
    right={k:v for k,v in actual.items() if k!="elapsed_seconds"}
    if left!=right:
        differing=sorted(k for k in set(left)|set(right) if left.get(k)!=right.get(k))
        raise ValueError("The reconstructed CURRENT complete scalar table differs from actual preparation: "+repr(differing))
    if (deep.definition!=context.scalar_definition
            or deep.model_identity_sha256!=context.scalar_identity
            or observed["integral_leaves"]!=actual["integral_leaves"]
            or observed["requested_integral_accuracy_reached"]!=actual["requested_integral_accuracy_reached"]):
        raise ValueError("A table carrier cannot redefine the fixed scalar target or its actual accuracy status")
    return deep,dict(schema="actual-current-preparation-scalar-table-reconstruction-v1",
        source_sha256=sha(__file__),original_scalar_source_sha256=DEEP_SHA,
        complete_actual_preparation_scalar=copy.deepcopy(actual),
        actual_current_leaf_count=actual["integral_leaves"],
        actual_current_leaf_evaluation_count=actual["integral_leaves_evaluated"],
        current_table_metadata_equal_except_elapsed=True,
        original_accuracy_status_preserved=actual["requested_integral_accuracy_reached"],
        actual_reconstruction_seconds=time.monotonic()-started,
        historical_2397_table_used_as_current=False,
        exact_fixed_scalar_definition_unchanged=True,
        achieved_accuracy_threshold_not_inferred_from_leaf_count=True)


class CompleteDyadicObservationPlan:
    def __init__(self,context,carriers,layout_module):
        require_actions()
        import numpy as np
        if (sha(inspect.getfile(type(context)))!=REFERENCE_SHA
                or sha(context.observed.__file__)!=OBSERVED_SHA
                or sha(layout_module.__file__)!=LAYOUT_SHA
                or sha(layout_module.affine_point.__code__.co_filename)!=LAYOUT_SHA
                or sha(layout_module.original_location_to_current.__code__.co_filename)!=LAYOUT_SHA
                or canonical(context.model)!=context.identity):
            raise ValueError("Bind all complete original/reference/layout sources")
        self.context=context
        self.input_records={k:actual_file(v) for k,v in context.input_records.items()}
        if set(self.input_records)!={"reference_bundle","carrier","node_report","scalar_input","preparation_report"}:
            raise ValueError("Keep all five actual fixed-reference inputs")
        saved=json.loads(Path(self.input_records["preparation_report"]["path"]).read_bytes())
        if saved!=context.preparation:
            raise ValueError("The live reference and exact captured preparation differ")
        layout=carriers["definition"]
        if (layout_module.validate_definition(layout)!=canonical(layout)
                or layout["complete_original_reference_model"]!=context.model):
            raise ValueError("The complete exact dyadic layout belongs to this fixed target")
        self.layout=copy.deepcopy(layout)
        self.layout_identity=canonical(layout)
        self.nodes=tuple(tuple(F(v) for v in p) for p in layout["complete_current_node_definitions"])
        original_nodes=tuple(tuple(F(v) for v in p) for p in layout["complete_original_node_definitions"])
        mesh=np.asarray(carriers["mesh"])
        if (mesh.shape!=(CURRENT_J,) or str(mesh.dtype)!="float64"
                or array_sha(mesh)!=layout["current_mesh_sha256"]
                or mesh[::2].tobytes()!=np.asarray(context.mesh).tobytes()):
            raise ValueError("Keep all actual old and current node carriers")
        old=context.plan
        if (len(old.cells)!=7377 or old.legacy_count!=1845 or old.order!=6
                or type(old.lift_break_node) is not int
                or not 0<old.lift_break_node<REFERENCE_J-1):
            raise ValueError("Keep every original observed row and its exact symbolic lift breakpoint")
        native=context.observed.make_plan(mesh,context.width,order=old.order,
            lift_break_node=2*old.lift_break_node)
        if (native.legacy_count!=2*CURRENT_J-1
                or len(native.cells)!=2*CURRENT_J-1+6*(CURRENT_J-1)):
            raise ValueError("The whole native refined node/midpoint/six-Gauss plan changed")
        self.mesh=np.array(mesh,dtype=np.float64,copy=True)
        self.original_mesh=np.array(context.mesh,dtype=np.float64,copy=True)
        self.mesh.setflags(write=False);self.original_mesh.setflags(write=False)
        self.native_P=len(native.cells)
        cells=[int(v) for v in native.cells]
        local=[float(v) for v in native.local_u]
        times=[float(v) for v in native.times]
        weights=[np.array(v,copy=True) for v in native.weights]
        points=[layout_module.affine_point(self.nodes,c,u) for c,u in zip(cells,local)]
        lookup={}
        for i,p in enumerate(points):
            if p in lookup:
                raise ValueError("Native refined observations must have distinct accurate affine addresses")
            lookup[p]=i
        mapping=[]
        exact_transfer_records=[]
        for i,(cell,u) in enumerate(zip(old.cells,old.local_u)):
            moved=layout_module.original_location_to_current(int(cell),float(u),original_nodes)
            current_cell=int(moved["cell"])
            current_u=float.fromhex(moved["local_hex"])
            p=tuple(F(v) for v in moved["exact_affine_point"])
            if p!=layout_module.affine_point(self.nodes,current_cell,current_u):
                raise ArithmeticError("An old physical observation was reinterpreted on the new grid")
            row=lookup.get(p)
            if row is None:
                row=len(cells)
                lookup[p]=row
                cells.append(current_cell);local.append(current_u);points.append(p)
                width=float(mesh[current_cell+1]-mesh[current_cell])
                times.append(float(mesh[current_cell]+width*current_u))
                weights.append(context.observed.hermite_weights(width,current_u))
            mapping.append(row)
            exact_transfer_records.append(moved)
        mapping=np.asarray(mapping,dtype=np.int64)
        if mapping.shape!=(7377,) or len(set(int(v) for v in mapping))!=7377:
            raise ValueError("Every distinct original observation requires its complete physical image")
        P=len(cells)
        fine_simpson=np.zeros(P,dtype=np.float64)
        fine_gauss=np.zeros(P,dtype=np.float64)
        old_quad=np.zeros(P,dtype=np.float64)
        fine_simpson[:self.native_P]=native.legacy_simpson_weights
        fine_gauss[:self.native_P]=native.quadrature_weights
        np.add.at(old_quad,mapping,np.asarray(old.quadrature_weights,dtype=np.float64))
        mixed_quad=(fine_gauss+old_quad)/2.
        test_weights=(fine_simpson+mixed_quad)/2.
        if (not np.isfinite(test_weights).all() or np.any(test_weights<=0)
                or np.any(fine_simpson<0) or np.any(fine_gauss<0) or np.any(old_quad<0)):
            raise ArithmeticError("Every retained and new row needs an actual finite positive combined weight")
        self.deep,self.scalar_reconstruction=_restore_actual_scalar(context)
        reference_module=inspect.getmodule(type(context))
        if reference_module is None or sha(reference_module.__file__)!=REFERENCE_SHA:
            raise ValueError("Use the actual complete reference target-a oracle")
        a=[];ae=[];te=[];aboxes=[]
        scalar_started=time.monotonic()
        for row,(point,tc) in enumerate(zip(points,times)):
            box=reference_module.target_a_box(context.full,self.deep,
                context.modules["deep_scalar"],point)
            value,error=reference_module.midpoint_and_error(box,
                context.modules["deep_scalar"].SCALE)
            if not math.isfinite(value) or value<=0 or not math.isfinite(error) or error<0:
                raise ArithmeticError("A same-target observation has no usable positive scalar carrier at row "+str(row))
            a.append(value);ae.append(error)
            scale=context.modules["deep_scalar"].SCALE
            aboxes.append([str(F(int(box[0]),scale)),str(F(int(box[1]),scale))])
            time_box=context.full.affine_time(*point)
            exact_word=F(float(tc))
            time_error=max(abs(exact_word-F(int(time_box[0]),context.full.h.S)),
                abs(exact_word-F(int(time_box[1]),context.full.h.S)))
            te.append(layout_module.upper_float(time_error))
            if (row+1)%1024==0 or row+1==P:
                print(json.dumps(dict(event='same_target_complete_dyadic_a_queries',
                    completed=row+1,total=P,current_scalar_leaf_count=self.scalar_reconstruction['actual_current_leaf_count']),
                    sort_keys=True),flush=True)
        a,ae,te=np.asarray(a),np.asarray(ae),np.asarray(te)
        parent_a=np.asarray(context.a_observations,dtype=np.float64).copy()
        if (a[mapping].tobytes()!=parent_a.tobytes()
                or array_sha(parent_a)!=context.model["a_observations_sha256"]):
            raise ArithmeticError("Reconstructed current scalar queries failed to reproduce all original 7377 target words")
        self.cells=np.asarray(cells,dtype=np.int64)
        self.local_u=np.asarray(local,dtype=np.float64)
        self.times=np.asarray(times,dtype=np.float64)
        self.weights=np.asarray(weights,dtype=np.float64)
        self.a,self.a_error,self.time_error=a,ae,te
        self.legacy_simpson_weights=fine_simpson
        self.native_gauss_weights=fine_gauss
        self.retained_parent_quadrature_weights=old_quad
        self.quadrature_weights=mixed_quad
        self.parent_stage_map=mapping
        self.parent_a=parent_a
        self.parent_simpson=np.asarray(old.legacy_simpson_weights,dtype=np.float64).copy()
        self.parent_quadrature=np.asarray(old.quadrature_weights,dtype=np.float64).copy()
        self.parent_cells=np.asarray(old.cells,dtype=np.int64).copy()
        self.parent_local_u=np.asarray(old.local_u,dtype=np.float64).copy()
        self.legacy_count=native.legacy_count
        self.order=native.order
        self.lift_break_node=native.lift_break_node
        self.piece_cells=np.array(native.piece_cells,copy=True)
        self.piece_u=np.array(native.piece_u,copy=True)
        self.gauss_indices=np.array(native.gauss_indices,copy=True)
        self.gauss_unit_nodes=np.array(native.gauss_unit_nodes,copy=True)
        self.gauss_unit_weights=np.array(native.gauss_unit_weights,copy=True)
        self.exact_points=tuple(points)
        self.accurate_a_boxes=aboxes
        self.exact_parent_transfer=exact_transfer_records
        self.current_symbolic_node_report=dict(
            schema="same-fixed-target-current-J1845-symbolic-nodes-and-a-anchors-v1",
            source_sha256=sha(__file__),
            reference_model_identity_sha256=context.identity,
            radial_layout_identity_sha256=self.layout_identity,
            original_symbolic_node_report_sha256=context.model["symbolic_node_report_sha256"],
            exact_current_nodes=[[str(v) for v in p] for p in self.nodes],
            current_legacy_count=self.legacy_count,
            complete_current_node_midpoint_a_boxes=copy.deepcopy(aboxes[:self.legacy_count]),
            all_legacy_anchor_boxes_from_actual_same_scalar_queries=True,
            original_reference_context_not_replaced=True)
        named=self._named_arrays()
        records={name:dict(sha256=array_sha(value),shape=list(value.shape),dtype=str(value.dtype))
            for name,value in named.items()}
        self.definition=definition(context.model,layout,observation_arrays=records)
        self.identity=canonical(self.definition)
        self.record=dict(schema=SCHEMA,source_sha256=sha(__file__),
            definition=self.definition,definition_identity_sha256=self.identity,
            input_records=copy.deepcopy(self.input_records),
            original_observation_count=7377,native_observation_count=self.native_P,
            current_complete_observation_count=P,
            additional_retained_parent_rows=P-self.native_P,
            current_legacy_count=self.legacy_count,
            exact_parent_stage_transfer_identity_sha256=canonical(exact_transfer_records),
            all_parent_target_words_reproduced=True,
            parent_scalar_words_sha256=array_sha(parent_a),
            actual_scalar_reconstruction=copy.deepcopy(self.scalar_reconstruction),
            actual_a_query_seconds=time.monotonic()-scalar_started,
            maximum_actual_a_carrier_error=float(ae.max()),
            maximum_actual_time_carrier_error=float(te.max()),
            accurate_a_boxes_identity_sha256=canonical(aboxes),
            same_exact_fixed_scalar_definition=True,
            requested_scalar_accuracy_reached=self.scalar_reconstruction["original_accuracy_status_preserved"],
            complete_scalar_remainder_and_carrier_error_bounds_recorded=True,
            field_rotation_root_normalization_quadrature_errors_enclosed=False,
            continuous_metric_or_geometry_certified=False)
        for value in list(named.values())+[self.weights,self.parent_cells,self.parent_local_u,
                self.piece_cells,self.piece_u,self.gauss_indices,self.gauss_unit_nodes,self.gauss_unit_weights]:
            value.setflags(write=False)
        self.recheck_inputs()

    def _named_arrays(self):
        return dict(cells=self.cells,local_u=self.local_u,times=self.times,
            a=self.a,a_error=self.a_error,time_error=self.time_error,
            legacy_simpson=self.legacy_simpson_weights,current_gauss=self.native_gauss_weights,
            retained_parent_quadrature=self.retained_parent_quadrature_weights,
            mixed_quadrature=self.quadrature_weights,parent_stage_map=self.parent_stage_map,
            parent_a=self.parent_a,parent_simpson=self.parent_simpson,
            parent_quadrature=self.parent_quadrature)

    def mixed_stage_weights(self,fraction):
        require_actions()
        import numpy as np
        t=float(fraction)
        if not math.isfinite(t) or not 0<t<1:
            raise ValueError("All native and retained row families need positive mixture weight")
        value=t*self.legacy_simpson_weights+(1-t)*self.quadrature_weights
        if value.shape!=self.a.shape or not np.isfinite(value).all() or np.any(value<=0):
            raise ArithmeticError("Every complete current residual row needs a positive actual weight")
        return value

    def common_parent_weights(self,fraction):
        require_actions()
        import numpy as np
        t=float(fraction)
        if not math.isfinite(t) or not 0<t<1:
            raise ValueError("Use the same explicit parent mixture fraction")
        result=t*self.parent_simpson+(1-t)*self.parent_quadrature
        if result.shape!=(7377,) or not np.isfinite(result).all() or np.any(result<=0):
            raise ArithmeticError("Keep all complete positive parent finite-functional weights")
        return result

    def recheck_inputs(self):
        for role,record in self.input_records.items():
            if actual_file(record)!=record:
                raise ValueError("A captured actual same-target input changed: "+role)
        if canonical(self.context.model)!=self.context.identity:
            raise ValueError("The fixed reference model changed during complete refinement")

    def metadata(self):
        self.recheck_inputs()
        return copy.deepcopy(self.record)

    def save(self,directory):
        require_actions()
        import numpy as np
        directory=Path(directory).resolve()
        directory.mkdir(parents=True,exist_ok=False)
        arrays=dict(self._named_arrays())
        arrays.update(mesh=self.mesh,original_mesh=self.original_mesh,
            observation_cells=self.cells,observation_u=self.local_u,observation_times=self.times,
            observation_legacy_count=np.array(self.legacy_count,dtype=np.int64),
            observation_order=np.array(self.order,dtype=np.int64),
            weights=self.weights,parent_cells=self.parent_cells,parent_local_u=self.parent_local_u,
            observation_piece_cells=self.piece_cells,observation_piece_u=self.piece_u,
            observation_gauss_indices=self.gauss_indices,
            observation_gauss_unit_nodes=self.gauss_unit_nodes,
            observation_gauss_unit_weights=self.gauss_unit_weights)
        raw=directory/"complete-dyadic-observations.npz"
        np.savez(raw,**arrays)
        records={}
        objects={"current-symbolic-nodes.json":self.current_symbolic_node_report,
            "complete-a-boxes.json":self.accurate_a_boxes,
            "complete-parent-address-transfer.json":self.exact_parent_transfer,
            "observation-definition.json":self.definition}
        for name,value in objects.items():
            path=directory/name
            path.write_text(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")
            records[name]=dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path))
        records[raw.name]=dict(path=str(raw),bytes=raw.stat().st_size,sha256=sha(raw))
        self.recheck_inputs()
        return dict(schema="complete-same-target-dyadic-observation-files-v1",
            definition_identity_sha256=self.identity,files=records,
            raw_stays_on_runner=True,scientific_input_precision_status_not_upgraded=True)
