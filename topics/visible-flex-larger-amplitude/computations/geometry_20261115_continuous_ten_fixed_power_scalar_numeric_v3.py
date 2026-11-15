#!/usr/bin/env python3
"""Independent v3-cut numerical profile for the accurate fixed-power ten-scalar family.

The accurate target remains the bound expression tree with semantic C-target
cut leaves.  This module openly compiles one finite binary64 approximation;
it does not replace those real leaves by midpoints in the target definition.
Public material coordinate u=s_numeric/L_numeric is retained in every export.
No old scalar_spec/450 identity, true-DN assertion, or acceptance is created.
"""
from __future__ import annotations
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
import struct

REPOSITORY="Rogerhu12/math-research-public"
HERE=Path(__file__).resolve().parent
FACTORY_NAME="geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
FACTORY_SHA="72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682"
MODEL_SCHEMA="R300-new-continuous-ten-fixed-support1-power4-target-family-v3-cut-v1"
R300_PROOF_SHA="5df99d5de2296fe830b8a51e76f27ea41cce217dd343a9803f7f1a830fec3147"
SCHEMA="R300-numerical-ten-fixed-support1-power4-v3-cut-accurate-public-u-target-v1"
SOURCE_TEXT_BASELINE="geometry_20261115_continuous_nine_scalar_numeric_v3.py"
SOURCE_TEXT_BASELINE_SHA="7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60"
PARAMETERS=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3","xi"]
CONTROL_TERMS=json.loads(r'''[{"parameter_index":0,"support_index":0,"power":0},{"parameter_index":1,"support_index":1,"power":0},{"parameter_index":2,"support_index":2,"power":0},{"parameter_index":3,"support_index":0,"power":1},{"parameter_index":4,"support_index":1,"power":1},{"parameter_index":5,"support_index":2,"power":1},{"parameter_index":6,"support_index":0,"power":2},{"parameter_index":7,"support_index":1,"power":2},{"parameter_index":8,"support_index":2,"power":2},{"parameter_index":9,"support_index":1,"power":4}]''')
ADDITION_ORDER=(0,1,2,4,3,5,6,7,8,9)
np=None


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Numerical search profiles run only in this public repository's Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode()


def words(values):
    return [struct.pack("<d",float(x)).hex() for x in values]


def real_vector(values,length,label):
    value=np.asarray(values)
    if (value.shape!=(length,) or not np.isrealobj(value)
            or not np.all(np.isfinite(value))):
        raise ValueError(label)
    return np.array(value,dtype=float,copy=True)


def public_u_jet(profile,u,parameters):
    u=float(u)
    if not math.isfinite(u) or not 0<=u<=1:
        raise ValueError("Use the complete fixed public material interval [0,1]")
    a,as_,ass=profile.profile(u*profile.end,parameters)
    return a,profile.end*as_,profile.end*profile.end*ass


def poly(coefficients,x):
    value=0.
    for coefficient in reversed(coefficients):
        value=value*x+coefficient
    return value


def derivative(coefficients):
    return [j*coefficients[j] for j in range(1,len(coefficients))] or [0.]


def multiplied(a,b):
    result=[0.]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            result[i+j]+=x*y
    return result


def bump_coefficients(order):
    result=[0.,0.,0.,64.,-192.,192.,-64.]
    for _ in range(order):
        result=multiplied(result,[-1.,2.])
    return result


class NumericContinuousTenProfile:
    """Same basic base_jet/control_jets/profile surface as the old model.

    M is field dimension metadata.  This profile has no fabricated tail port;
    any actual full-DN/physical boundary must be supplied by a separately
    honest new binding.  The original CircleReference accepts this numerical
    profile mathematically, but its passed J keeps its actual old/new scope.
    """
    def __init__(self,definition_file,definition_sha256,*,modes,code_directory=HERE):
        require_actions()
        global np
        if np is None:
            import numpy as numpy
            np=numpy
        factory_path=Path(code_directory)/FACTORY_NAME
        if sha(factory_path.read_bytes())!=FACTORY_SHA:
            raise ValueError("The R300 accurate expression factory source differs")
        path=Path(definition_file)
        raw=path.read_bytes()
        if sha(raw)!=definition_sha256:
            raise ValueError("The actual complete accurate model definition differs")
        definition=json.loads(raw)
        if (definition.get("schema")!=MODEL_SCHEMA
                or definition.get("source_sha256")!=FACTORY_SHA
                or definition.get("parameter_order")!=PARAMETERS
                or definition.get("control_terms")!=CONTROL_TERMS
                or definition.get("polynomial_coefficients_are_expressions_not_cut_interval_midpoints") is not True
                or definition.get("no_early_segment_mask_or_primal_clip") is not True
                or definition.get("construction_conditions",{}).get("all_strict_conditions_proved") is not True
                or definition.get("published_structural_and_effective_scope_proof",{}).get("sha256")!=R300_PROOF_SHA):
            raise ValueError("A complete independent R300 exact-expression definition is required")
        self.definition=definition
        self.definition_receipt=dict(file=path.name,bytes=len(raw),sha256=sha(raw))
        if not isinstance(modes,int) or isinstance(modes,bool) or modes<=0:
            raise ValueError("Declare the actual field mode count")
        self.M=self.tail_modes=modes
        self.parameter_count=10
        self.initial_exact_parameters=[Q(x) for x in definition["ten_parameters"]]
        self.initial_parameters=np.asarray([float(x) for x in self.initial_exact_parameters])
        if self.initial_parameters.shape!=(10,) or not np.all(np.isfinite(self.initial_parameters)):
            raise ValueError("Retain all finite actual initial ten coefficients")
        self.initial_projection_differences=[Q.from_float(float(word))-exact
            for word,exact in zip(self.initial_parameters,self.initial_exact_parameters)]
        self.leaf_values={}
        for name,box in definition["actual_enclosure_leaves"].items():
            lo,hi=Q(box["lower"]),Q(box["upper"])
            if lo>hi:
                raise ValueError("A semantic leaf enclosure is reversed")
            self.leaf_values[name]=float((lo+hi)/2)
        if set(self.leaf_values)!={"E0","E1","E2"} or not self.leaf_values["E0"]>1:
            raise ArithmeticError("The finite cut approximation cannot represent the strict original scalar domain")
        values=[]
        for node in definition["expression_nodes"]:
            kind=node["op"]
            if kind=="rational": value=float(Q(node["value"]))
            elif kind=="semantic-cut-leaf": value=self.leaf_values[node["name"]]
            else:
                args=[values[i] for i in node["args"]]
                if kind=="add": value=args[0]+args[1]
                elif kind=="neg": value=-args[0]
                elif kind=="mul": value=args[0]*args[1]
                elif kind=="div": value=args[0]/args[1]
                elif kind=="sqrt": value=math.sqrt(args[0])
                else: raise ValueError("Unknown original expression operation")
            if not math.isfinite(value):
                raise ArithmeticError("Nonfinite numerical compilation of the accurate expression")
            values.append(value)
        self.values=values
        self.end=values[definition["derived_expression_roots"]["total_length"]]
        self.prefix_end=float(Q(definition["core_end"]))
        self.cut_radius=float(Q(definition["cut_radius"]))
        self.pieces=[]
        for piece in definition["pieces"]:
            anchor,width=values[piece["anchor"]],values[piece["width"]]
            if width<=0:
                raise ArithmeticError("A finite numerical piece width is not positive")
            coefficients=[values[index] for index in piece["coefficients"]]
            tlo,thi=map(lambda x:float(Q(x)),piece["local_interval"])
            self.pieces.append(dict(name=piece["name"],anchor=anchor,width=width,
                coefficients=coefficients,first=derivative(coefficients),
                second=derivative(derivative(coefficients)),tlo=tlo,thi=thi))
        if not self.pieces or not math.isfinite(self.end) or self.end<=0:
            raise ValueError("The numerical prefix does not have a complete finite domain")
        # One common finite partition for lookup.  This does not assert that
        # independently rounded polynomial traces are exactly C2.
        self.partition=[p["anchor"]+p["width"]*p["tlo"] for p in self.pieces]+[self.end]
        if (self.partition[0]!=0. or any(b<=a for a,b in zip(self.partition[:-1],self.partition[1:]))):
            raise ArithmeticError("The accurate piece order cannot be represented by this finite partition")
        self.supports=[]
        if len(definition["three_true_supports"])!=3:
            raise ValueError("Retain exactly the three complete new-family supports")
        for item in definition["three_true_supports"]:
            left,width=values[item["left"]],values[item["width"]]
            if not math.isfinite(left) or width<=0:
                raise ArithmeticError("An original new-family support is not representable")
            self.supports.append(dict(left=left,width=width,right=left+width))
        self.control_coefficients={k:bump_coefficients(k) for k in (0,1,2,4)}
        self.control_first={k:derivative(v) for k,v in self.control_coefficients.items()}
        self.control_second={k:derivative(v) for k,v in self.control_first.items()}
        self.knots=sorted(set(self.partition+
            [s for item in self.supports for s in (item["left"],item["right"]) if 0<=s<=self.end]))
        join_traces=[]
        for index,boundary in enumerate(self.partition[1:-1]):
            pair=[]
            for p in (self.pieces[index],self.pieces[index+1]):
                t=(boundary-p["anchor"])/p["width"]
                pair.append([poly(p["coefficients"],t),
                    poly(p["first"],t)/p["width"],
                    poly(p["second"],t)/(p["width"]*p["width"])])
            join_traces.append(dict(left_piece=index,right_piece=index+1,
                common_station_float64le=struct.pack("<d",boundary).hex(),
                left_numerical_jet_float64le=words(pair[0]),
                right_numerical_jet_float64le=words(pair[1]),
                numerical_jet_words_identical=words(pair[0])==words(pair[1]),
                no_exact_real_C2_conclusion_from_this_finite_comparison=True))
        self.compilation=dict(
            schema=SCHEMA+"-finite-compilation",source_sha256=sha(Path(__file__).read_bytes()),
            factory_sha256=FACTORY_SHA,accurate_definition=self.definition_receipt,
            numerical_leaf_midpoints={key:dict(value=value,float64le=struct.pack("<d",value).hex())
                                      for key,value in self.leaf_values.items()},
            expression_values_float64le=words(values),
            common_lookup_partition_float64le=words(self.partition),
            supports_float64le=[words((x["left"],x["width"],x["right"])) for x in self.supports],
            piece_coefficient_float64le=[words(p["coefficients"]) for p in self.pieces],
            complete_numerical_piece_join_traces=join_traces,
            original_semantic_leaves_redefined=False,
            numerical_cut_leaf_midpoints_jointly_realised_by_one_tail_root_not_proved=True,
            selected_tail_root_rule=self.definition["chosen_root_scope"],
            given_finite_enclosures_are_not_arbitrarily_refinable_real_names=True,
            numerical_shadow_metric_identified_with_accurate_target=False,
            finite_polynomial_endpoint_identity_or_C2_proved=False,
            true_evaluator_error_bound_supplied=False,
            base_jet_and_control_jets_use_same_polynomial_derivatives=True,
            batch_profile_uses_same_scalar_evaluation_order=True,
            public_material_coordinate="u=s_numeric/L_numeric; exact target uses s_true=L_true*u",
            numerical_length_float64le=struct.pack("<d",self.end).hex(),
            true_length_expression_root=definition["derived_expression_roots"]["total_length"],
            ten_addition_order=list(ADDITION_ORDER),complete_control_terms=[dict(term) for term in CONTROL_TERMS],
            source_text_baseline=dict(file=SOURCE_TEXT_BASELINE,sha256=SOURCE_TEXT_BASELINE_SHA,
                old_nine_numeric_producer_not_executed_or_relabelled=True),
            definition_initial_accurate_parameters=[str(x) for x in self.initial_exact_parameters],
            initial_numeric_parameter_float64le=words(self.initial_parameters),
            exact_projection_difference_binary64_minus_accurate=[str(x) for x in self.initial_projection_differences],
            all_initial_coefficients_exactly_represented_by_numeric_words=all(x==0 for x in self.initial_projection_differences),
            coefficient_projection_is_distinct_from_cut_leaf_midpoint_error=True,
            old_Gauss_mask_primal_branch_not_reused=True)
        self.compilation_sha256=sha(canonical(self.compilation))

    def _point(self,s):
        s=float(s)
        if not math.isfinite(s) or not 0<=s<=self.end:
            raise ValueError("Numerical scalar point is outside its complete current domain")
        # This branch lookup has no early mask and no clipping of local t.
        import bisect
        index=min(len(self.pieces)-1,bisect.bisect_right(self.partition,s)-1)
        p=self.pieces[index];t=(s-p["anchor"])/p["width"]
        return s,p,t

    def base_jet(self,s):
        _,p,t=self._point(s);w=p["width"]
        return np.asarray([poly(p["coefficients"],t),poly(p["first"],t)/w,
            poly(p["second"],t)/(w*w)],float)

    def control_jets(self,s):
        s,_,_=self._point(s)
        answer=np.zeros((3,10))
        for term in CONTROL_TERMS:
            support=self.supports[term["support_index"]]
            w=support["width"];x=(s-support["left"])/w
            if x<=0 or x>=1:
                continue
            order=term["power"];column=term["parameter_index"]
            answer[:,column]=[w*w*poly(self.control_coefficients[order],x),
                w*poly(self.control_first[order],x),poly(self.control_second[order],x)]
        return answer

    def raw_jet(self,s,parameters=None):
        p=self.initial_parameters if parameters is None else np.asarray(parameters)
        if p.shape!=(10,) or not np.all(np.isfinite(p)):
            raise ValueError("Retain all actual ten coefficients for this profile call")
        jet=self.base_jet(s).astype(np.result_type(p,float),copy=True)
        controls=self.control_jets(s)
        for index in ADDITION_ORDER:
            if p[index]!=0:
                jet=jet+p[index]*controls[:,index]
        return jet

    def profile(self,s,parameters=None):
        jet=self.raw_jet(s,parameters)
        if not np.all(np.isfinite(jet)):
            raise FloatingPointError("The actual complete numerical scalar jet is nonfinite")
        if np.isrealobj(jet) and (jet[0]<=0 or abs(jet[1])>=1):
            raise FloatingPointError("The actual new scalar left original a>0, |a'|<1; no interval claim")
        return tuple(jet)

    def scalar_jets(self,points,parameters=None):
        # Point and batch evaluations share exactly the same profile body.
        x=np.asarray(points,float)
        rows=[self.profile(s,parameters) for s in x.ravel()]
        return np.asarray(rows).reshape(x.shape+(3,))

    def jets_u(self,u,parameters=None):
        return public_u_jet(self,u,parameters)

    def mesh_from_public_u(self,u):
        u=np.asarray(u,float)
        if (u.ndim!=1 or len(u)<2 or u[0]!=0 or u[-1]!=1
                or np.any(~np.isfinite(u)) or np.any(np.diff(u)<=0)):
            raise ValueError("Supply an explicit full strictly ordered public-u mesh")
        x=u*self.end
        x[0],x[-1]=0.,self.end
        if np.any(np.diff(x)<=0):
            raise ArithmeticError("The chosen public mesh loses a finite distinct node")
        return x

    def export_specification(self,parameters):
        p=real_vector(parameters,10,"Export the complete current real ten parameters")
        base_keys=("expression_nodes","pieces","three_true_supports","derived_expression_roots",
                   "continuous_tail","core_input","core_end","cut_radius","chosen_root_scope",
                   "control_terms","added_term","parameter_order")
        base_identity={key:self.definition[key] for key in base_keys}
        return dict(schema=SCHEMA,source_sha256=sha(Path(__file__).read_bytes()),
            accurate_definition=self.definition_receipt,
            published_R300_proof_sha256=R300_PROOF_SHA,
            accurate_family_base_identity_sha256=sha(canonical(base_identity)),
            complete_numeric_compilation=self.compilation,
            numeric_compilation_sha256=self.compilation_sha256,
            parameter_order=PARAMETERS,ten_parameters=p.tolist(),
            ten_parameter_float64le=words(p),
            ten_parameters_as_exact_dyadics=[str(Q.from_float(float(x))) for x in p],
            definition_initial_accurate_ten_parameters=[str(x) for x in self.initial_exact_parameters],
            current_numeric_words_exactly_equal_definition_initial=all(
                Q.from_float(float(x))==q for x,q in zip(p,self.initial_exact_parameters)),
            current_ten_dyadics_define_the_current_accurate_family_point=True,
            coefficient_projection_must_not_silently_relabel_exact_input=True,
            complete_control_terms=[dict(term) for term in CONTROL_TERMS],
            field_modes=self.M,tail_modes=self.tail_modes,
            numeric_physical_length=self.end,accurate_length_expression_root=base_identity["derived_expression_roots"]["total_length"],
            public_material_interval=["0","1"],
            numerical_metric_radial_in_u="L_numeric^2",
            accurate_target_metric_radial_in_u="L_true^2, with the original semantic cut leaves",
            actual_point_batch_equality_observed=False,
            old_finite_scalar_schema_or_existing450_relabelled=False,
            full_DN_or_exact_tail_port_supplied=False,
            original_zero_tail_J_relabelled_as_current_C_target_J=False,
            current_g_numerically_solved=False,
            accepted_field_created=False,
            accurate_target_geometry_or_metric_certificate_paid=False)

    def description(self):
        return dict(schema=SCHEMA,source_sha256=sha(Path(__file__).read_bytes()),
            accurate_definition=self.definition_receipt,
            numeric_compilation_sha256=self.compilation_sha256,
            field_modes=self.M,tail_modes=self.tail_modes,scalar_parameters=10,
            parameter_order=PARAMETERS,public_material_interval=["0","1"],
            numerical_length=self.end,original_cut_radius=self.cut_radius,
            actual_original_controlled_core_identity_verified=False,
            scalar_continuity_error_or_continuous_target_metric_certified=False,
            original_tail_port_or_current_C_response_supplied=False,
            mathematical_new_target_defined_by_original_expression_tree=True)

    def frozen_seven_shapes(self,shape_coefficients):
        return FrozenSevenShapes(self,shape_coefficients)

    def frozen_ten(self,parameters):
        return FrozenTen(self,parameters)


class FrozenSevenShapes:
    """The same new family with seven true shape coefficients fixed, three active."""
    def __init__(self,designed,shape_coefficients):
        self.designed=designed
        self.fixed=real_vector(shape_coefficients,7,
            "Fix theta1..3, eta1..3 and xi, keeping all seven current real words")
        self.initial_parameters=designed.initial_parameters[:3].copy()
        self.parameter_count=3

    def __getattr__(self,name):
        return getattr(self.designed,name)

    def base_jet(self,s):
        p=np.r_[np.zeros(3),self.fixed]
        # This raw base value is not independently subjected to the full
        # parameter guard before the three active coefficients are added.
        jet=self.designed.base_jet(s).copy();controls=self.designed.control_jets(s)
        for index in ADDITION_ORDER:
            if p[index]!=0:
                jet=jet+p[index]*controls[:,index]
        return jet

    def control_jets(self,s):
        return self.designed.control_jets(s)[:,:3]

    def profile(self,s,parameters=None):
        if parameters is None:
            parameters=self.initial_parameters
        p=np.asarray(parameters)
        if p.shape!=(3,):
            raise ValueError("The square check has exactly the declared three active parameters")
        return self.designed.profile(s,np.r_[p,self.fixed])

    def raw_jet(self,s,parameters=None):
        p=self.initial_parameters if parameters is None else np.asarray(parameters)
        if p.shape!=(3,):
            raise ValueError("The raw square view retains all three active parameters")
        return self.designed.raw_jet(s,np.r_[p,self.fixed])

    def scalar_jets(self,points,parameters=None):
        x=np.asarray(points,float)
        return np.asarray([self.profile(s,parameters) for s in x.ravel()]).reshape(x.shape+(3,))

    def jets_u(self,u,parameters=None):
        return public_u_jet(self,u,parameters)

    def export_specification(self,parameters=None):
        p=self.initial_parameters if parameters is None else real_vector(
            parameters,3,"Export exactly the three active current p coefficients")
        record=self.designed.export_specification(np.r_[p,self.fixed])
        record.update(view="seven-shapes-fixed-three-active",active_scalar_parameters=3,
            active_parameter_indices=[0,1,2],fixed_parameter_indices=list(range(3,10)),
            actual_fixed_parameter_float64le=words(self.fixed))
        return record

    def description(self):
        record=self.designed.description()
        record.update(view="seven-shapes-fixed-three-active",scalar_parameters=3,
            active_parameter_indices=[0,1,2],fixed_parameter_indices=list(range(3,10)),
            actual_fixed_parameter_float64le=words(self.fixed),
            point_and_batched_AugmentedFlow_paths_are_not_claimed_bit_identical=True)
        return record


class FrozenTen:
    """Identical selected new target parameters, zero active scalar controls."""
    def __init__(self,designed,parameters):
        self.designed=designed
        self.fixed=real_vector(parameters,10,"Freeze every one of the actual ten coefficients")
        self.initial_parameters=np.empty(0)
        self.parameter_count=0

    def __getattr__(self,name):
        return getattr(self.designed,name)

    def base_jet(self,s):
        return np.asarray(self.designed.raw_jet(s,self.fixed))

    def control_jets(self,s):
        return np.zeros((3,0))

    def profile(self,s,parameters=None):
        if parameters is not None and np.asarray(parameters).shape!=(0,):
            raise ValueError("This new scalar is frozen; do not reset its actual ten coefficients")
        return self.designed.profile(s,self.fixed)

    def raw_jet(self,s,parameters=None):
        if parameters is not None and np.asarray(parameters).shape!=(0,):
            raise ValueError("The raw frozen view has no active scalar parameters")
        return self.designed.raw_jet(s,self.fixed)

    def scalar_jets(self,points,parameters=None):
        if parameters is not None and np.asarray(parameters).shape!=(0,):
            raise ValueError("The full same-target call has no active scalar control")
        return self.designed.scalar_jets(points,self.fixed)

    def jets_u(self,u,parameters=None):
        return public_u_jet(self,u,parameters)

    def export_specification(self,parameters=None):
        if parameters is not None and np.asarray(parameters).shape!=(0,):
            raise ValueError("Export no active scalar parameters for the fully frozen target")
        record=self.designed.export_specification(self.fixed)
        record.update(view="all-ten-fixed-zero-active",active_scalar_parameters=0,
            active_parameter_indices=[],fixed_parameter_indices=list(range(10)),
            actual_fixed_parameter_float64le=words(self.fixed))
        return record

    def description(self):
        record=self.designed.description()
        record.update(view="all-ten-fixed-zero-active",scalar_parameters=0,
            active_parameter_indices=[],fixed_parameter_indices=list(range(10)),
            actual_fixed_parameter_float64le=words(self.fixed))
        return record
