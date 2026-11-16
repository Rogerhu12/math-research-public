#!/usr/bin/env python3
"""R451 accurate-ten target and complete finite-M prefix relative metric.

This independently named consumer requires the actual R442 frozen-M
checkpoint.  The field is the exact rational nodal Hermite interpretation,
not the rounded PhysicalQuintic evaluator.  The target is the complete
published continuous-ten DAG at the actual frozen ten dyadic words, with
the original common model-C cut enclosures.  It is not the finite-Gauss
family and not the numerical compiler's midpoint metric.

Every accurate piece possibly meeting a closed public-u interval is
included, as are all ten control terms and their actual support boundaries.
The unchanged R251 four strict Loewner tests are applied to all 3M+2
physical rows and the complete M-mode material pullback.  This source covers the
two prefix sheets only; it neither invents current-C native radial data
nor invokes an old finite-tail/shared-B loader.  Full closed seams, both
native tails/collars/caps, held/reach and the complete task remain unpaid.

Scientific arithmetic is allowed only in the named public Actions.
"""
from __future__ import annotations
import argparse
from collections import OrderedDict
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import struct
import time
from types import SimpleNamespace

REPOSITORY="Rogerhu12/math-research-public"
HERE=Path(__file__).resolve().parent
SCHEMA="R451-current-C-complete-M-frozen-prefix-relative-metric-v1"
SAVED_NAME="geometry_20261116_continuous_ten_frozen_M_saved_prefix.py"
FACTORY_NAME="geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
ACTIVE_NAME="geometry_20261115_shared_active_interval_balls.py"
METRIC_NAME="geometry_20261115_shared_field_relative_metric.py"
SOURCE_PINS={
    "geometry_20261116_continuous_ten_frozen_M_saved_prefix.py": "86a88a66a57c05b64c21efa650374746ad42be272f0d741188ff81bdf4fed2f6",
    "geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py": "72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682",
    "geometry_20261115_shared_active_interval_balls.py": "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b",
    "geometry_20261115_shared_field_relative_metric.py": "a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17"
}
SUMMARY_LIMIT=90000


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Run exact/interval field arithmetic only in the named public Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode()


def receipt(path,root=None):
    path=Path(path);h=hashlib.sha256();size=0
    with path.open("rb") as stream:
        for raw in iter(lambda:stream.read(1048576),b""):
            h.update(raw);size+=len(raw)
    return dict(file=str(path.relative_to(root)) if root else path.name,
        bytes=size,sha256=h.hexdigest())


def load(directory,name):
    path=Path(directory)/name
    if receipt(path)["sha256"]!=SOURCE_PINS[name]:
        raise ValueError("An actual complete source differs: "+name)
    # An isolated module instance prevents an existing legacy loader's
    # runtime globals from being mutated.  No original module/file is edited.
    module_name="_r400_prefix_metric_"+name[:-3]
    spec=importlib.util.spec_from_file_location(module_name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[module_name]=module
    try:spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name,None);raise
    return module


def runtime(directory):
    require_actions()
    source_closure={name:receipt(Path(directory)/name) for name in SOURCE_PINS}
    Saved=load(directory,SAVED_NAME)
    Factory=load(directory,FACTORY_NAME)
    M=load(directory,ACTIVE_NAME)
    Kernel=load(directory,METRIC_NAME)
    # Only the original pure six-jet/Fourier arithmetic is used.  Calling
    # old initialise_runtime/load_shared_bundle would import a legacy
    # finite-tail route that is not a current-C producer.
    import numpy as np
    from flint import arb,ctx,fmpq
    M.np,M.arb,M.ctx,M.fmpq=np,arb,ctx,fmpq
    source_closure[Path(__file__).name]=receipt(__file__)
    return Saved,Factory,M,Kernel,source_closure


class PrefixExactField:
    """All 3M+2 exact Hermite rows with the complete actual M-mode Phi.

    A constant identity SE2 gauge is chosen for this prefix-only Gram
    comparison.  Any actual single rigid registration would give the same
    Gram matrix.  No prefix-to-tail matching is thereby asserted.
    """
    def __init__(self,saved,M):
        self.saved,self.kernel=saved,M
        self.M=int(saved.M)
        self.x=tuple(Q.from_float(float(v)) for v in saved.quintic.x)
        self.nodal=tuple(saved.quintic.nodal)
        if (len(self.x)<2 or self.x[0]!=0
                or any(a>=b for a,b in zip(self.x,self.x[1:]))
                or any(v.shape!=(len(self.x),3*self.M+2) or v.dtype.kind!="f"
                    or v.dtype.itemsize!=8 for v in self.nodal)):
            raise ValueError("Retain every actual physical node and all three complete 3M+2-row nodal jets")
        self.core=tuple(Q.from_float(float(x)) for x in saved.core)
        self.density=tuple((1-4*m*m)*x for m,x in enumerate(self.core,1))
        self.rho_lower=saved.rho_lower_exact
        if len(self.core)!=self.M or self.rho_lower<=0:
            raise ValueError("The original full-core material inverse responsibility is unpaid")
        self.beta=Q(0);self.translation=(Q(0),Q(0))
        self.prefix_cache=OrderedDict()
        self.pieces=[dict(kind="prefix",index=i,left=a,right=b,prefix_span=i)
            for i,(a,b) in enumerate(zip(self.x,self.x[1:]))]
        self.target_identity=copy.deepcopy(saved.checkpoint.target_identity)

    def prefix_coefficients(self,index):
        if index in self.prefix_cache:
            self.prefix_cache.move_to_end(index)
            return self.prefix_cache[index]
        values=self.saved.exact_prefix_coefficients(index)
        if len(values)!=3*self.M+2 or any(len(v)!=6 for v in values):
            raise ValueError("The exact Hermite field lost a complete physical coefficient")
        self.prefix_cache[index]=values
        while len(self.prefix_cache)>2:self.prefix_cache.popitem(last=False)
        return values

    def registered_world(self,*args,**kwargs):
        return self.kernel.ExactFiniteField.registered_world(self,*args,**kwargs)

    def prefix(self,*args,**kwargs):
        return self.kernel.ExactFiniteField.prefix(self,*args,**kwargs)

    def material_angle(self,*args,**kwargs):
        return self.kernel.ExactFiniteField.material_angle(self,*args,**kwargs)

    def evaluate(self,piece,radial,angular,lower):
        if piece.get("kind")!="prefix":
            raise ValueError("This typed component owns prefix cells only")
        return self.kernel.ExactFiniteField.evaluate(self,piece,radial,angular,lower)

    def identity(self):
        M=self.kernel
        return dict(schema=SCHEMA+"-exact-prefix-expression",
            actual_saved_prefix=self.saved.definition,
            field_modes=self.M,full_core_modes=self.M,physical_rows=3*self.M+2,
            exact_mesh=[str(x) for x in self.x],
            complete_nodal_identities=[M.array_identity(v,"<f8") for v in self.nodal],
            all_physical_nodal_values_first_second_retained=True,
            zero_mode_means_retained=True,
            exact_rational_Hermite_two_jet_sharing=True,
            chosen_prefix_only_rigid_gauge=dict(rotation="0",translation=["0","0"]),
            Gram_invariant_under_any_one_constant_actual_SE2=True,
            actual_shared_tail_registration_produced=False,
            whole_lower_sheet_reflection_used_for_Gram_only=True,
            reflection_seam_C2_proved_here=False,
            rounded_PhysicalQuintic_is_not_the_certified_expression=True,
            rounded_evaluator_to_this_exact_field_error_certified=False,
            physical_phi_coordinate="phi=2*pi*q",
            material_angle="Phi(phi)=phi+sum((1-4*m*m)*c_m*sin(2*m*phi)/(2*m)),m=1..M",
            finite_theta_bandwidth_inferred=False,
            complete_target_identity=self.target_identity)


def valid_index(value,size):
    return type(value) is int and 0<=value<size


class AccurateTenTarget:
    """An executable enclosure of the actual ten DAG, with common C leaves."""
    def __init__(self,saved,Factory,sqrt_bits):
        self.Factory=Factory
        owner=saved.checkpoint.owner
        data=owner.data
        definition=data["definition"]
        identity=saved.checkpoint.target_identity
        if (definition.get("schema")!=Factory.MODEL_SCHEMA
                or definition.get("source_sha256")!=SOURCE_PINS[FACTORY_NAME]
                or definition.get("parameter_order")!=Factory.PARAMETERS
                or definition.get("control_terms")!=Factory.CONTROL_TERMS
                or identity.get("parameter_order")!=Factory.PARAMETERS
                or identity.get("control_terms")!=Factory.CONTROL_TERMS):
            raise ValueError("Use the actual complete continuous-ten family and all ten controls")
        self.definition=definition
        self.parameters=[Q(x) for x in identity["complete_ten_exact_dyadics"]]
        if len(self.parameters)!=10:
            raise ValueError("Retain every actually frozen dyadic coefficient")
        nodes=copy.deepcopy(definition["expression_nodes"])
        leaves_seen=[]
        for i,node in enumerate(nodes):
            op=node.get("op")
            if op=="rational":
                Q(node["value"])
            elif op=="semantic-cut-leaf":
                if node.get("name") not in ("E0","E1","E2"):
                    raise ValueError("Do not add or replace semantic target leaves")
                leaves_seen.append(node["name"])
            else:
                arity={"add":2,"mul":2,"div":2,"neg":1,"sqrt":1}.get(op)
                if (arity is None or len(node.get("args",[]))!=arity
                        or any(not valid_index(j,i) for j in node["args"])):
                    raise ValueError("The complete exact expression DAG is not ordered")
        if sorted(leaves_seen)!=["E0","E1","E2"]:
            raise ValueError("The same complete three semantic cut leaves are required")
        self.tree=Factory.Tree();self.tree.nodes=nodes
        self.leaves={key:Factory.Box(Q(row["lower"]),Q(row["upper"]))
            for key,row in definition["actual_enclosure_leaves"].items()}
        if set(self.leaves)!={"E0","E1","E2"}:
            raise ValueError("Only the actual common model-C cut enclosures are allowed")
        self.values=self.tree.evaluate(self.leaves,sqrt_bits)
        self.pieces=copy.deepcopy(definition["pieces"])
        self.supports=copy.deepcopy(definition["three_true_supports"])
        self.roots=copy.deepcopy(definition["derived_expression_roots"])
        last_names=["first-velocity-transition","negative-speed-coast",
            "last-velocity-transition","canonical-cubic-cut-collar"]
        if (len(self.pieces)<5 or [x["name"] for x in self.pieces[-4:]]!=last_names
                or [x["name"] for x in self.pieces[:-4]]!=
                    ["core-"+str(i) for i in range(len(self.pieces)-4)]
                or len(self.supports)!=3):
            raise ValueError("Retain the complete original core and all four accurate joining pieces")
        size=len(nodes)
        for piece in self.pieces:
            indices=[piece["anchor"],piece["width"]]+piece["coefficients"]
            if any(not valid_index(i,size) for i in indices):
                raise ValueError("A complete accurate piece lost an expression index")
            lo,hi=map(Q,piece["local_interval"])
            if lo>hi or self.values[piece["width"]].lo<=0:
                raise ArithmeticError("An actual accurate piece width/domain is unresolved")
        for support in self.supports:
            if (not valid_index(support["left"],size)
                    or not valid_index(support["width"],size)
                    or self.values[support["width"]].lo<=0):
                raise ArithmeticError("A complete actual control support is unresolved")
        root=self.roots["total_length"]
        if not valid_index(root,size):
            raise ValueError("The natural scalar length expression was changed")
        self.length=self.values[root]
        self.numeric_length=Q.from_float(float(saved.checkpoint.profile.end))
        if self.length.lo<=0 or self.numeric_length<=0:
            raise ArithmeticError("The shared public-u pullback lacks a positive length enclosure")
        if (identity["accurate_length_expression_root"]!=root
                or identity["numerical_length_float64le"]!=
                    struct.pack("<d",float(saved.checkpoint.profile.end)).hex()):
            raise ValueError("The actual field's numerical/accurate length identity differs")
        # CurrentTenProfile already binds the exact binary length word.  Do
        # not infer equality of L_numeric and the semantic interval L_true.
        self.model=dict(tree=self.tree,pieces=self.pieces,supports=self.supports,
            roots=self.roots,parameters=self.parameters,
            control_terms=copy.deepcopy(Factory.CONTROL_TERMS))
        self.breakpoints=()
        self.cache=OrderedDict()
        self.binding=dict(schema=SCHEMA+"-accurate-target",
            complete_target_identity=copy.deepcopy(identity),
            actual_factory_result=copy.deepcopy(data["result_receipt"]),
            complete_accurate_definition=copy.deepcopy(data["definition_receipt"]),
            complete_original_C_input_binding=copy.deepcopy(data["complete_C_binding"]),
            actual_common_cut_enclosures=copy.deepcopy(data["semantic_cut_hulls"]),
            actual_C_cut_to_natural_Rout_responsibility=copy.deepcopy(
                definition["continuous_tail"]),
            all_root_family_retained=True,
            all10_frozen_exact_dyadics=[str(x) for x in self.parameters],
            full_control_terms=copy.deepcopy(Factory.CONTROL_TERMS),
            complete_accurate_piece_count=len(self.pieces),
            complete_expression_node_count=len(nodes),
            full_expression_nodes_sha256=sha(canonical(nodes)),
            complete_piece_definitions_sha256=sha(canonical(self.pieces)),
            complete_support_definitions_sha256=sha(canonical(self.supports)),
            actual_semantic_leaves={key:value.record() for key,value in self.leaves.items()},
            true_length_enclosure=self.length.record(),
            numeric_length_exact=str(self.numeric_length),
            public_u="s_numeric/L_numeric=s_true/L_true",
            radial_target_in_numeric_coordinate="(L_true/L_numeric)^2",
            angular_target_in_physical_q="a_true(L_true*s_numeric/L_numeric;p10)^2*(dPhi/dq)^2",
            actual_frozen_point_need_not_equal_factory_starting_point=True,
            no_cut_box_midpoint_inserted_into_accurate_target=True,
            no_finite_Gauss_or_old_nine_target_relabelled=True,
            constant_cut_enclosures_are_not_arbitrarily_refinable_real_names=True,
            output_prefix_metric_does_not_certify_all_scalar_speed_or_seam_conditions=True,
            true_tail_radii_outside_original_C_domain_are_not_extended=True)

    def closed_range(self,left,right):
        key=(left,right)
        if key in self.cache:
            self.cache.move_to_end(key);return self.cache[key]
        if not 0<=left<=right<=self.numeric_length:
            raise ValueError("Use an actual complete prefix subinterval")
        F=self.Factory;Box=F.Box
        public=Box(left/self.numeric_length,right/self.numeric_length)
        radial=self.length*public
        jets=None;candidates=[]
        # Enumerate all original pieces.  A nominal midpoint piece lookup
        # cannot cover uncertain exact boundaries or closed shared endpoints.
        for index,piece in enumerate(self.pieces):
            anchor,width=self.values[piece["anchor"]],self.values[piece["width"]]
            t=(radial-anchor)/width
            own_left,own_right=map(Q,piece["local_interval"])
            lo,hi=max(t.lo,own_left),min(t.hi,own_right)
            if lo>hi:continue
            local=Box(lo,hi)
            row=F.piece_range(self.model,self.values,piece,local,include_controls=True)
            jets=list(row) if jets is None else [a.hull(b) for a,b in zip(jets,row)]
            candidates.append(dict(index=index,name=piece["name"],
                complete_closed_local_interval=local.record(),
                accurate_radius_first_second=[x.record() for x in row]))
        if jets is None:
            raise ArithmeticError("No complete accurate piece enclosure covers this public-u box")
        scale=self.length/Box(self.numeric_length)
        report=dict(schema=SCHEMA+"-closed-target-cell",
            numerical_coordinate=[str(left),str(right)],public_u=public.record(),
            same_true_radial_coordinate=radial.record(),
            all_possible_accurate_pieces=candidates,
            every_original_accurate_piece_examined=len(self.pieces),
            selected_candidate_count=len(candidates),
            accurate_radius_first_second=[x.record() for x in jets],
            radial_metric=(scale*scale).record(),
            closed_endpoints_and_all_support_cases_included=True,
            no_finite_angle_bandwidth_or_sample_selection=True,
            parameter_count=10,all_control_terms_retained=True,
            piece_union_is_conservative_not_a_common_midpoint_choice=True)
        result=(jets,scale*scale,report)
        self.cache[key]=result
        while len(self.cache)>64:self.cache.popitem(last=False)
        return result


def inspect(M,Kernel,field,target,spec,eta):
    piece=field.pieces[spec["piece_index"]]
    radial=tuple(map(Q,spec["radial"]))
    angular=tuple(map(Q,spec["angular"]))
    values=field.evaluate(piece,radial,angular,spec["lower"])
    X,Y=tuple(v.d[1] for v in values),tuple(v.d[2] for v in values)
    E,B,C=M.dot(X,X),M.dot(X,Y),M.dot(Y,Y)
    theta,angular_record=Kernel.angle_density(field,M,angular)
    jets,radial_metric,target_record=target.closed_range(*radial)
    if jets[0].lo<=0:
        return dict(certified=False,reason="accurate_ten_positive_radius_lower_unresolved",
            target=target_record,angular=angular_record,
            scalar_speed_domain_or_metric_counterexample_inferred=False)
    a=M.interval(jets[0].lo,jets[0].hi)
    g11=M.interval(radial_metric.lo,radial_metric.hi)
    g22=a*a*theta*theta
    result=Kernel.loewner_certificate(M,E,B,C,g11,g22,eta)
    result.update(target=target_record,angular=angular_record,
        complete_position_and_six_jets={name:[M.encode_interval(v.d[j]) for v in values]
            for j,name in enumerate(M.JET_NAMES)},
        original_four_Loewner_inequalities_unchanged=True,
        exact_Hermite_derivatives_not_rounded_renderer_jets=True,
        all_physical_and_material_modes_and_zero_means_retained=True,
        old_finite_Gauss_scalar_or_Bprime_not_substituted=True)
    return result


def run(args):
    require_actions()
    if args.out.exists():
        raise FileExistsError("Use a fresh owned temporary output")
    if args.directory.resolve().is_relative_to(args.out.resolve()):
        raise ValueError("The new output must not own the actual parent input")
    eta=Q(args.eta)
    if (not 0<eta<1 or not 64<=args.precision_bits<=8192
            or not 64<=args.sqrt_bits<=8192
            or not 0<=args.initial_angular_depth<=20
            or not 0<=args.max_depth<=30 or args.max_visited_cells<=0
            or not math.isfinite(args.budget_seconds) or args.budget_seconds<=0):
        raise ValueError("Use explicit finite work limits and an explicit relative-metric eta")
    args.out.mkdir(parents=True)
    large=args.out/"large-arrays";large.mkdir()
    started=time.monotonic()
    old_precision=None;M=None;journal=None
    binding=None;plan=None;pending_receipt=None
    expression_receipt=None;target_receipt=None;ledger_receipt=None
    complete=False;prefix_ok=False;root_results=[]
    visited=terminal=passed=0;resource_stop=None;execution_error=None
    input_phase="binding_and_full_nodal_interpretation"
    try:
        Saved,Factory,M,Kernel,closure=runtime(args.code_directory)
        old_precision=M.ctx.prec
        M.ctx.prec=args.precision_bits+args.max_depth
        saved=Saved.ContinuousTenSavedPrefix(args.directory,args.checkpoint_sha256,
            args.code_directory)
        field=PrefixExactField(saved,M)
        target=AccurateTenTarget(saved,Factory,args.sqrt_bits)
        if field.x[-1]!=target.numeric_length:
            raise ValueError("The actual complete field and numeric scalar domains differ")
        (large/"same-exact-prefix-expression.json").write_bytes(canonical(field.identity()))
        expression_receipt=receipt(large/"same-exact-prefix-expression.json",args.out)
        (large/"same-accurate-ten-target.json").write_bytes(canonical(target.binding))
        target_receipt=receipt(large/"same-accurate-ten-target.json",args.out)
        binding=dict(schema=SCHEMA+"-input-binding",source_sha256=sha(Path(__file__).read_bytes()),
            source_closure=closure,
            saved_full_source_closure=saved.source_sha256,
            actual_accepted_frozen_M_checkpoint=saved.checkpoint.receipt,
            current_target_identity=saved.checkpoint.target_identity,
            exact_prefix_expression=expression_receipt,
            accurate_target=target_receipt,
            original675_pure_jet_formulas_used=True,
            original_a601_four_Loewner_and_closed_DFS_formulas_used=True,
            old675_initialise_runtime_or_legacy_shared_loaders_called=False,
            old_finite_tail_or_Bprime_substitution=False,
            original_BVP_acceptance_not_changed=True)
        (large/"input-binding.json").write_bytes(canonical(binding))
        binding=receipt(large/"input-binding.json",args.out)
        plan=Kernel.root_plan(field,target,SimpleNamespace(cuts=()),args.initial_angular_depth)
        plan["original_plan_algorithm_schema"]=plan["schema"]
        plan["schema"]=SCHEMA+"-complete-prefix-root-plan"
        plan["scope"]="all exact prefix spans, both reflected copies, all closed physical-q endpoints"
        if plan["planned_roots"]<=0:
            raise ValueError("The actual full prefix contains no cells")
        (large/"planned-closed-roots.json").write_bytes(canonical(plan))
        journal=Kernel.Journal(large/"relative-metric-cells.jsonl.gz")
        journal.append(dict(type="identity",input_binding=binding,
            plan=receipt(large/"planned-closed-roots.json",args.out),
            eta_exact=str(eta)))
        input_phase="complete_prefix_closed_cover"
        next_rank=0;pending=[]
        for root in Kernel.roots(plan):
            next_rank=root["rank"]
            stack=[root];root_ok=True
            while stack:
                if (visited>=args.max_visited_cells
                        or time.monotonic()-started>=args.budget_seconds):
                    resource_stop="explicit_cell_or_wall_budget_before_next_complete_cell"
                    pending=list(reversed(stack));break
                spec=stack.pop();visited+=1
                try:
                    report=inspect(M,Kernel,field,target,spec,eta)
                except (ArithmeticError,ValueError) as exc:
                    report=dict(certified=False,reason="interval_or_declared_expression_unresolved",
                        exception=dict(type=type(exc).__name__,message=str(exc)))
                except Exception as exc:
                    execution_error=dict(type=type(exc).__name__,message=str(exc),cell=spec)
                    pending=[spec]+list(reversed(stack));break
                if not report["certified"] and spec["depth"]<args.max_depth:
                    journal.append(dict(type="subdivided",cell=spec,diagnostic=report))
                    stack.extend(reversed(Kernel.split_cell(spec)));continue
                journal.append(dict(type="terminal_closed_cell",cell=spec,operator=report))
                terminal+=1;passed+=int(report["certified"])
                root_ok=root_ok and report["certified"]
            if resource_stop is not None or execution_error is not None:break
            root_results.append(dict(rank=root["rank"],complete_closed_subdivision=True,
                certified=root_ok))
            next_rank=root["rank"]+1
            if len(root_results)%20==0:
                print(json.dumps(dict(event="R451_complete_M_prefix_metric_progress",
                    completed_roots=len(root_results),planned_roots=plan["planned_roots"],
                    visited_cells=visited,certified_cells=passed,
                    elapsed_seconds=time.monotonic()-started),separators=(",",":")),flush=True)
        complete=len(root_results)==plan["planned_roots"]
        prefix_ok=complete and all(x["certified"] for x in root_results)
        coverage=dict(schema=SCHEMA+"-coverage-and-pending",
            complete_prefix_partition=complete,
            current_root_rank=None if complete else next_rank,
            remaining_closed_DFS_cells=pending,
            untouched_root_rank_suffix=[plan["planned_roots"] if complete else next_rank+1,
                plan["planned_roots"]],
            immutable_root_plan=receipt(large/"planned-closed-roots.json",args.out),
            completed_root_results=root_results,
            all_unresolved_terminal_cells_retained_in_ledger=True,
            full_other_closed_pieces_unpaid=["both-native-tails","both-collars","both-fixed-caps",
                "prefix-tail-shared-seams","reflection-seam","target-atlas"])
        (large/"coverage-and-pending.json").write_bytes(canonical(coverage))
        pending_receipt=receipt(large/"coverage-and-pending.json",args.out)
        journal.append(dict(type="coverage_end",coverage=pending_receipt,
            resource_stop=resource_stop,execution_error=execution_error))
        journal.close();journal=None
        ledger_receipt=receipt(large/"relative-metric-cells.jsonl.gz",args.out)
    except Exception as exc:
        execution_error=dict(type=type(exc).__name__,message=str(exc),phase=input_phase)
    finally:
        if journal is not None:
            journal.close()
            ledger_receipt=receipt(large/"relative-metric-cells.jsonl.gz",args.out)
        if M is not None and old_precision is not None:M.ctx.prec=old_precision
    if pending_receipt is None:
        # Setup/output errors do not discharge a guessed prefix or erase the
        # whole responsibility.  Any completed ledger remains separately
        # identified; this source makes no success claim from that ledger.
        whole_unpaid=dict(schema=SCHEMA+"-setup-or-output-unpaid",
            entire_prefix_and_all_other_closed_pieces_unpaid=True,
            original_checkpoint=dict(directory=str(args.directory),
                manifest_sha256=args.checkpoint_sha256),
            phase=input_phase,execution_error=execution_error,
            actual_root_plan=(receipt(large/"planned-closed-roots.json",args.out)
                if (large/"planned-closed-roots.json").is_file() else None),
            complete_existing_cell_ledger=ledger_receipt)
        (large/"whole-unpaid-scope.json").write_bytes(canonical(whole_unpaid))
        pending_receipt=receipt(large/"whole-unpaid-scope.json",args.out)
        complete=False;prefix_ok=False
    result=dict(schema=SCHEMA,repository=REPOSITORY,run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),source_sha256=sha(Path(__file__).read_bytes()),
        completed=complete,complete_accurate_ten_prefix_relative_operator_bound=prefix_ok,
        requested_eta_exact=str(eta),
        parameters=dict(precision_bits=args.precision_bits,
            effective_precision_bits=args.precision_bits+args.max_depth,
            sqrt_bits=args.sqrt_bits,initial_angular_depth=args.initial_angular_depth,
            max_depth=args.max_depth,max_visited_cells=args.max_visited_cells,
            budget_seconds=args.budget_seconds),
        input_binding=binding,exact_prefix_expression=expression_receipt,
        accurate_ten_target=target_receipt,complete_cell_ledger=ledger_receipt,
        complete_coverage_and_unpaid=pending_receipt,
        counts=dict(planned_roots=None if plan is None else plan["planned_roots"],
            completed_roots=len(root_results),visited_cells=visited,
            terminal_cells=terminal,certified_cells=passed,
            unresolved_terminal_cells=terminal-passed),
        scope=dict(field="exact rational Hermite interpretation of all actual 3M+2 nodal rows",
            target="same full continuous-ten DAG at the actual frozen10 dyadic point and complete C leaf family",
            chart="s_numeric,q; target g11=(L_true/L_numeric)^2,g22=a_true(L_true*s_numeric/L_numeric)^2*Phi_q^2",
            all_ten_controls_and_closed_piece_candidates_retained=True,
            two_prefix_sheets_and_full_closed_angle_covered=complete,
            all_six_field_jets_and_both_means_retained=True,
            exact_field_equals_rounded_renderer_not_claimed=True,
            accurate_scalar_global_speed_domain_proved_by_this_consumer=False,
            all_four_original_Loewner_tests_preserved=True,
            old_finite_Gauss_or_nine_target_relabelled=False,
            new_current_C_native_radial_field_supplied=False,
            shared_B_and_full_closed_tail_collar_cap_comparison_performed=False,
            caps_target_is_induced_cap_metric_not_zero_tensor=True,
            prefix_tail_and_cuff_C2_seams_proved=False,
            original_target_atlas_compatibility_proved=False,
            complete_closed_relative_metric_standard4=False,
            all_phase_reach_held_embedding_or_task_completed=False,
            original_native_RMS_BC_FD_or_fresh_audit_acceptance_changed=False,
            missing_interval_margin_is_not_a_pointwise_counterexample=True,
            arbitrary_refinement_of_fixed_C_cut_boxes_promised=False),
        resource_stop=resource_stop,execution_error=execution_error,
        elapsed_seconds=time.monotonic()-started,
        timer_scope="includes source/runtime/input interpretation; checked before each complete cell, not an asynchronous whole-process kill",
        raw_outputs_temporary_recomputable=True)
    raw=canonical(result);(args.out/"result.json").write_bytes(raw)
    summary=dict(schema=SCHEMA+"-necessary-summary",
        result=receipt(args.out/"result.json",args.out),
        **{k:result[k] for k in ("repository","run_id","source_commit","source_sha256",
            "completed","complete_accurate_ten_prefix_relative_operator_bound","requested_eta_exact",
            "parameters","input_binding","exact_prefix_expression","accurate_ten_target",
            "complete_cell_ledger","complete_coverage_and_unpaid","counts","scope",
            "resource_stop","execution_error","elapsed_seconds","timer_scope")})
    output=canonical(summary);(args.out/"summary.json").write_bytes(output)
    if len(output)>SUMMARY_LIMIT:
        print(json.dumps(dict(schema=SCHEMA+"-necessary-summary-over-budget",
            bytes=len(output),sha256=sha(output),limit=SUMMARY_LIMIT,
            full_summary_not_emitted=True),separators=(",",":")),flush=True)
        return 70
    print("BEGIN_R451_COMPLETE_M_PREFIX_METRIC_SUMMARY",flush=True)
    print(output.decode(),end="",flush=True)
    print("END_R451_COMPLETE_M_PREFIX_METRIC_SUMMARY",flush=True)
    return 1 if execution_error is not None else 0


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory",type=Path,required=True)
    parser.add_argument("--checkpoint-sha256",required=True)
    parser.add_argument("--code-directory",type=Path,default=HERE)
    parser.add_argument("--eta",required=True)
    parser.add_argument("--precision-bits",type=int,required=True)
    parser.add_argument("--sqrt-bits",type=int,required=True)
    parser.add_argument("--initial-angular-depth",type=int,required=True)
    parser.add_argument("--max-depth",type=int,required=True)
    parser.add_argument("--max-visited-cells",type=int,required=True)
    parser.add_argument("--budget-seconds",type=float,required=True)
    parser.add_argument("--out",type=Path,required=True)
    return run(parser.parse_args(argv))


if __name__=="__main__":
    raise SystemExit(main())
