#!/usr/bin/env python3
"""R363 requestless locator for actual R351 weights and local C2 shapes.

No scientific operation is run on import. All constructors, exact shape
sampling and finite-arithmetic contractions are public-Actions only.
This source does not choose a historical parent, create a new nonlinear
family, run a trial, prove rank, or adopt any accepted field.

A repeated physical position is a single function jet, but need not be one
shared q variable. Preserve every logical node/mid q occurrence. Node
weights already include their left/right-cell and terminal responsibilities.
"""
from __future__ import annotations
from decimal import Decimal
from fractions import Fraction
import hashlib
import inspect
import json
import math
import os
from pathlib import Path
import time
import traceback

HERE=Path(__file__).resolve().parent
ENTRY='geometry_20261115_literal_local_zerojet_station_catalogue.py'
SCHEMA='R363-actual-literal-local-zerojet-station-catalogue-v1'
SHAPE_SCHEMA='R363-frozen-local-odd-septic-C2-zerojet-shape-v1'
ADJOINT_NAME='geometry_20261115_literal_seven_state_adjoint.py'
ADJOINT_BYTES=35419
ADJOINT_SHA='12a95d40929cc7799761e56c33eadc9e5fbe16fa3eacf0d0be94c56ea3452b0f'
FAMILY_NAME='geometry_20261115_small_core_nine_control_family.py'
FAMILY_SHA='086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629'
PRIMAL_NAME='geometry_20261115_nine_control_decimal_literal_model.py'
PRIMAL_SHA='2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75'
NODE_COUNT,CELL_COUNT=699,698
FORMULA='epsilon^2*t*(1-t^2)^3, t=(s-center)/epsilon, abs(t)<1; zero elsewhere'
SCOPE='This odd shape has h(center)=0. Repeated nonshared (a,b) retain every w/a term; no claim about the independent nonzero-value jet direction.'


class CatalogueInputError(ValueError):
    pass


class CatalogueResourceStop(RuntimeError):
    pass


class ShapeRepresentationError(ValueError):
    pass


def require_actions():
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise RuntimeError('All shape arithmetic and response work is restricted to the public repository Actions')


def file_identity(path):
    path=Path(path);raw=path.read_bytes()
    return dict(name=path.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def own_identity():
    return file_identity(__file__)


def json_bytes(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=True,allow_nan=False,
                      separators=(',',':')).encode('ascii')


def metadata_copy(value):
    return json.loads(json_bytes(value))


def rational(value):
    """An existing exact word becomes a rational, not a numerical estimate."""
    if isinstance(value,Fraction):
        return value
    if isinstance(value,Decimal):
        if not value.is_finite():
            raise CatalogueInputError('A recorded Decimal station is nonfinite')
        return Fraction(value)
    if isinstance(value,float):
        if not math.isfinite(value):
            raise CatalogueInputError('A recorded binary64 value is nonfinite')
        return Fraction.from_float(value)
    if isinstance(value,int) and not isinstance(value,bool):
        return Fraction(value)
    raise CatalogueInputError('Require an existing finite numeric word or exact rational')


def rational_record(value):
    value=rational(value)
    return dict(numerator=str(value.numerator),denominator=str(value.denominator))


def rational_from_record(value):
    if not isinstance(value,dict) or set(value)!={'numerator','denominator'}:
        raise CatalogueInputError('An exact rational record requires numerator and denominator')
    return Fraction(int(value['numerator']),int(value['denominator']))


def exact_dyadic_decimal(value):
    """Construct the exact finite Decimal, bypassing context rounding."""
    require_actions()
    value=rational(value);den=value.denominator
    if den<=0 or den&(den-1):
        raise CatalogueInputError('The center/width must have a dyadic exact representation')
    exponent=den.bit_length()-1
    coefficient=value.numerator*(5**exponent)
    sign=int(coefficient<0);digits=tuple(int(x) for x in str(abs(coefficient)))
    return Decimal((sign,digits,-exponent))


def float_record(value):
    value=float(value)
    return dict(word=value.hex(),finite=math.isfinite(value),
        negative_zero=bool(value==0.0 and math.copysign(1.0,value)<0),
        exact=rational_record(value) if math.isfinite(value) else None)


def decimal_matrix(value,rows,columns,label):
    if not isinstance(value,(list,tuple)) or len(value)!=rows:
        raise CatalogueInputError(label+' row count differs')
    result=[]
    for row in value:
        if not isinstance(row,(list,tuple)) or len(row)!=columns:
            raise CatalogueInputError(label+' column count differs')
        if any(not isinstance(x,Decimal) or not x.is_finite() for x in row):
            raise CatalogueInputError(label+' must retain finite actual Decimal words')
        result.append(list(row))
    return result


class FrozenLocalShape:
    """One immutable physical function, reusable on later meshes.

    No grid-dependent re-isolation happens in any sampling method. Original
    selection-grid receipts remain provenance; new samples get new identities.
    """
    def __init__(self,center,epsilon,selection):
        require_actions()
        self.center=rational(center);self.epsilon=rational(epsilon)
        if self.epsilon<=0 or self.epsilon.denominator&(self.epsilon.denominator-1):
            raise CatalogueInputError('Use a positive dyadic epsilon')
        if self.epsilon.numerator!=1:
            raise CatalogueInputError('This explicit locator uses epsilon=2^(-k), k>=0')
        self.left=self.center-self.epsilon;self.right=self.center+self.epsilon
        self.selection=metadata_copy(selection)
        mathematical=dict(schema=SHAPE_SCHEMA,formula=FORMULA,
            center=rational_record(self.center),epsilon=rational_record(self.epsilon),
            support_left=rational_record(self.left),support_right=rational_record(self.right),
            zero_extension=True,zero_012_jets_at_support_endpoints=True,
            center_value=0,center_derivative=rational_record(self.epsilon),center_second_derivative=0,
            original_scalar_two_columns_a_and_b_not_assumed_derivative_compatible=True)
        self.mathematical=mathematical
        self.mathematical_sha256=hashlib.sha256(json_bytes(mathematical)).hexdigest()

    @classmethod
    def from_definition(cls,definition):
        require_actions()
        if definition.get('schema')!=SHAPE_SCHEMA or definition.get('source')!=own_identity():
            raise CatalogueInputError('Bind the frozen function source, not a relabelled new grid')
        shape=cls(rational_from_record(definition['mathematical']['center']),
            rational_from_record(definition['mathematical']['epsilon']),
            definition['selection'])
        if shape.mathematical!=definition['mathematical'] or shape.mathematical_sha256!=definition.get('mathematical_sha256'):
            raise CatalogueInputError('Frozen center/width/formula identity differs')
        return shape

    def definition(self):
        return dict(schema=SHAPE_SCHEMA,source=own_identity(),
            mathematical=self.mathematical,mathematical_sha256=self.mathematical_sha256,
            selection=self.selection,parameter_is_not_an_old_nine_coordinate=True,
            coefficient_not_selected_or_adopted_by_this_helper=True,
            required_continuous_domain_breakpoints=[rational_record(self.left),rational_record(self.right)],
            same_g_refinement_requires_frozen_center_width_and_coefficients=True,
            regeneration_of_Kronecker_table_on_new_grid_is_not_same_g=True,
            global_original_base_C2_or_ap_compatibility_not_repaired=True,
            no_native_or_nonlinear_full_field_claim=True)

    def jet_exact(self,s):
        require_actions()
        s=rational(s)
        if s<=self.left or s>=self.right:
            return (Fraction(0),Fraction(0),Fraction(0))
        t=(s-self.center)/self.epsilon
        H=t*(1-t*t)**3
        Hp=1-9*t*t+15*t**4-7*t**6
        Hpp=-18*t+60*t**3-42*t**5
        return (self.epsilon*self.epsilon*H,self.epsilon*Hp,Hpp)

    def binary64_definition(self):
        require_actions()
        center=float(self.center);epsilon=float(self.epsilon)
        center_finite=math.isfinite(center)
        width_valid=math.isfinite(epsilon) and epsilon>0
        return dict(center=float_record(center),epsilon=float_record(epsilon),
            center_exactly_represented=center_finite and Fraction.from_float(center)==self.center,
            epsilon_exactly_represented=width_valid and Fraction.from_float(epsilon)==self.epsilon,
            usable_positive_finite_binary64_width=center_finite and width_valid,
            support_endpoints_remain_exact_rationals=True,
            rounded_display_endpoints_not_used_to_define_mathematical_support=True)

    def jet_binary64(self,s):
        require_actions()
        record=self.binary64_definition()
        if not record['usable_positive_finite_binary64_width']:
            raise ShapeRepresentationError('Exact local width has no positive finite binary64 representation')
        center=float(self.center);epsilon=float(self.epsilon);s=float(s)
        if not math.isfinite(s):
            raise ShapeRepresentationError('Actual binary64 sample coordinate is nonfinite')
        t=(s-center)/epsilon
        if not math.isfinite(t) or abs(t)>=1.0:
            return (0.0,0.0,0.0)
        # This precise finite expression is separately identified. Exact-real
        # Kronecker sampling is not used to overwrite its original words.
        H=t*(1.0-t*t)**3
        Hp=1.0-9.0*t*t+15.0*t**4-7.0*t**6
        Hpp=-18.0*t+60.0*t**3-42.0*t**5
        return (epsilon*epsilon*H,epsilon*Hp,Hpp)

    def interval_jet(self,lift,s,branch_midpoint):
        """Exact declared formula for a caller that splits at both endpoints.

        lift is the caller's exact rational-to-ball constructor. The caller
        owns the interval engine, complete base expression and all final gates.
        """
        require_actions()
        middle=rational(branch_midpoint)
        if not self.left<middle<self.right:
            zero=lift(Fraction(0));return zero,zero,zero
        epsilon=lift(self.epsilon);t=(s-lift(self.center))/epsilon
        H=t*(1-t*t)**3
        Hp=1-9*t*t+15*t**4-7*t**6
        Hpp=-18*t+60*t**3-42*t**5
        return epsilon*epsilon*H,epsilon*Hp,Hpp


class LocalZeroJetCatalogue:
    """Consume a completed, explicitly bound frozen R351 original-nine object.

    This version deliberately does not accept a ten-coordinate state by
    pretending it is an old nine-state. An extended local-trace producer
    requires its own future explicit source/schema contract.
    """
    def __init__(self,completed_adjoint,original_nine_profile,binding,*,event_sink=None,deadline=None):
        require_actions()
        self.started=time.monotonic();self.deadline=deadline
        self.event_sink=event_sink or (lambda event:None)
        self.adjoint=adj=completed_adjoint;self.b=b=adj.b
        self.complete=False;self.stage='bind actual R351 weights and original supports'
        self.failure=None;self.groups=[];self.candidates=[];self.skipped=[]
        self.materializations=[];self.processed_groups=0
        self.visited_occurrences=dict(node=0,midpoint=0);self.grouping_complete=False
        if Path(inspect.getfile(type(adj))).resolve()!=HERE/ADJOINT_NAME:
            raise CatalogueInputError('Consume the actual R351 class, not a look-alike object')
        actual_adjoint_source=file_identity(HERE/ADJOINT_NAME)
        if actual_adjoint_source['bytes']!=ADJOINT_BYTES or actual_adjoint_source['sha256']!=ADJOINT_SHA:
            raise CatalogueInputError('The complete frozen R351 source changed')
        if file_identity(HERE/PRIMAL_NAME)['sha256']!=PRIMAL_SHA:
            raise CatalogueInputError('The frozen literal primal differs')
        if (not adj.complete or adj.failure is not None
                or adj.reverse_rows_completed!=CELL_COUNT
                or adj.binding.get('original_nine_family_source_sha256')!=FAMILY_SHA):
            raise CatalogueInputError('The original local/terminal/reverse trace must actually be complete')
        if (Path(inspect.getfile(type(original_nine_profile))).resolve()!=HERE/FAMILY_NAME
                or file_identity(HERE/FAMILY_NAME)['sha256']!=FAMILY_SHA
                or original_nine_profile.parameter_count!=9):
            raise CatalogueInputError('This version binds the true frozen original nine profile')
        if not isinstance(binding,dict):
            raise CatalogueInputError('Explicit caller and actual-point binding is required')
        caller=binding.get('producer_source')
        if (not isinstance(caller,dict) or not isinstance(caller.get('name'),str)
                or Path(caller['name']).name!=caller['name']):
            raise CatalogueInputError('Caller source must be a computation basename')
        if file_identity(HERE/caller['name'])!=caller:
            raise CatalogueInputError('Actual independent caller source bytes differ')
        trace_binding=dict(adj.binding);trace_hash=trace_binding.pop('canonical_sha256',None)
        if trace_hash!=b.digest(trace_binding):
            raise CatalogueInputError('Original R351 binding canonical bytes differ')
        profile_description=original_nine_profile.description()
        expected=dict(expected_adjoint_binding_sha256=trace_hash,
            expected_literal_model_binding_sha256=adj.binding['literal_model_binding_sha256'],
            actual_parameter_words=list(adj.binding['actual_parameter_words']),
            expected_original_profile_description_sha256=b.digest(profile_description))
        for name,value in expected.items():
            if binding.get(name)!=value:
                raise CatalogueInputError('Explicit actual point/profile identity differs: '+name)
        if len(expected['actual_parameter_words'])!=9:
            raise CatalogueInputError('Do not relabel a future extended owner as an original nine point')
        arrays=adj.formed_arrays()
        self.nodes=list(adj.x);self.mids=list(adj.mid)
        if len(self.nodes)!=NODE_COUNT or len(self.mids)!=CELL_COUNT:
            raise CatalogueInputError('Keep all699 nodes and698 midpoint occurrences')
        self.node_weights=decimal_matrix(arrays['node_weights'],NODE_COUNT,3,'complete node weights')
        self.mid_weights=decimal_matrix(arrays['midpoint_weights'],CELL_COUNT,3,'complete midpoint weights')
        self.node_scalar=decimal_matrix(adj.scalar_nodes,NODE_COUNT,2,'actual node a/b')
        self.mid_scalar=decimal_matrix(adj.scalar_middle,CELL_COUNT,2,'actual midpoint a/b')
        self.node_q=list(adj.q);self.mid_q=list(adj.qm)
        self.F=list(adj.original_equation)
        self.start=rational(self.nodes[0]);self.end=rational(self.nodes[-1])
        if not self.start<self.end:
            raise CatalogueInputError('The fixed initial and terminal coordinates are ordered')
        for name,array in (('node',self.node_scalar),('midpoint',self.mid_scalar)):
            if any(row[0]<=0 for row in array):
                raise CatalogueInputError('The actual bound primal must have positive scalar a: '+name)
        bumps=original_nine_profile.original_three.bumps
        if len(bumps)!=3:
            raise CatalogueInputError('Use the actual three original supports')
        self.supports=[]
        for i,bump in enumerate(bumps):
            left=float(bump.left);width=float(bump.width);display=float(bump.right)
            if not all(math.isfinite(x) for x in (left,width,display)) or width<=0:
                raise CatalogueInputError('An actual original support is invalid')
            L=rational(left);W=rational(width);R=L+W
            self.supports.append(dict(index=i,left=L,width=W,right=R,
                open_left=max(L,self.start),open_right=min(R,self.end),
                left_word=float_record(left),stored_width_word=float_record(width),
                right_metadata_word=float_record(display),
                nominal_right_is_not_used_in_place_of_left_plus_width=True))
        self.binding=dict(schema=SCHEMA,source=own_identity(),
            actual_R351_source=actual_adjoint_source,actual_caller=metadata_copy(caller),
            current_run_id=os.environ.get('GITHUB_RUN_ID'),current_source_commit=os.environ.get('GITHUB_SHA'),
            explicit_caller_binding=metadata_copy(binding),actual_R351_binding=adj.binding,
            original_profile_source=file_identity(HERE/FAMILY_NAME),
            original_profile_description_sha256=b.digest(profile_description),
            original_node_mid_decimal_coordinate_sha256=b.digest(dict(nodes=self.nodes,middle=self.mids)),
            complete_formed_node_weight_sha256=b.digest(self.node_weights),
            complete_formed_midpoint_weight_sha256=b.digest(self.mid_weights),
            complete_actual_a_b_q_sha256=b.digest(dict(node=self.node_scalar,middle=self.mid_scalar,
                node_q=self.node_q,midpoint_q=self.mid_q)),
            original_three_equations=self.F,original_full112_right_identity=b.digest(adj.original_full_right),
            input_parameter_dimension=9,current_ten_or_other_extended_state_supported=False,
            local_trace_and_all112_terminal_already_formed=True,
            new_RHS_J_native_or_trial_computed_by_locator=False,
            actual_formed_weights_not_certified_exact_derivatives=True)
        self.binding['canonical_sha256']=b.digest(self.binding)

    def _check(self):
        require_actions()
        if self.deadline is not None and time.monotonic()>=self.deadline:
            raise CatalogueResourceStop('Explicit caller resource deadline reached in station catalogue')

    def _emit(self,event,**fields):
        self.event_sink(dict(event=event,schema=SCHEMA,stage=self.stage,**fields))

    def _support_record(self,row):
        return dict(index=row['index'],left=rational_record(row['left']),
            stored_width=rational_record(row['width']),mathematical_right=rational_record(row['right']),
            allowed_open_left=rational_record(row['open_left']),
            allowed_open_right=rational_record(row['open_right']),
            left_word=row['left_word'],stored_width_word=row['stored_width_word'],
            right_metadata_word=row['right_metadata_word'],
            clipping_to_fixed_initial_terminal_open_interval_is_explicit=True)

    def _occurrence(self,kind,index,station,scalar,q,weight):
        if not isinstance(q,Decimal) or not q.is_finite():
            raise CatalogueInputError('Retain the actual finite ratio word')
        position=rational(station)
        if kind=='node':
            roles=[]
            if index>0:roles.append(dict(cell=index-1,role='right-node'))
            if index<CELL_COUNT:roles.append(dict(cell=index,role='left-node'))
            if index==NODE_COUNT-1:roles.append(dict(role='direct-complete112-terminal'))
        else:
            roles=[dict(cell=index,role='cell-midpoint')]
        return dict(kind=kind,index=index,variable_id=kind+':'+str(index),position=position,
            original_coordinate_word=str(station),scalar_a=scalar[0],returned_b=scalar[1],
            actual_q=q,complete_three_weight=list(weight),already_scattered_roles=roles,
            original_shared_node_roles_already_summed_not_to_be_multiplied_again=True)

    def _formed_response(self,occurrences,epsilon):
        b=self.b;eps=exact_dyadic_decimal(epsilon)
        with b.precision_context():
            node_terms=[[],[],[]];mid_terms=[[],[],[]]
            quotients=[];word_differences=[]
            formula_sum=[b.ZERO,b.ZERO,b.ZERO]
            for row in occurrences:
                a,c=row['scalar_a'],row['returned_b']
                current=b.Jet(c,[eps])/b.Jet(a,[b.ZERO])
                dq=current.d[0]
                quotients.append(dict(variable_id=row['variable_id'],
                    current_q_from_same_ratio_rule=current.v,
                    original_q=row['actual_q'],formed_directional_q=dq,
                    direct_epsilon_over_a=eps/a))
                if str(current.v)!=str(row['actual_q']):
                    word_differences.append(row['variable_id'])
                target=node_terms if row['kind']=='node' else mid_terms
                for k,weight in enumerate(row['complete_three_weight']):
                    target[k].append(weight*dq)
                    formula_sum[k]=formula_sum[k]+weight/a
            formed=[sum(node_terms[k],b.ZERO)+sum(mid_terms[k],b.ZERO) for k in range(3)]
            quotient_formula=[eps*x for x in formula_sum]
            finite=all(x.is_finite() for x in formed+quotient_formula)
            gradient=b.dot(self.F,formed)
            all_common_scalar_words=len({(str(x['scalar_a']),str(x['returned_b']),str(x['actual_q'])) for x in occurrences})==1
            return dict(exact_epsilon=rational_record(epsilon),exact_epsilon_Decimal_word=str(eps),
                complete_three_formed_response=formed,
                complete_three_rounded_epsilon_sum_weight_over_a=quotient_formula,
                actual_ratio_rule_minus_rounded_formula=[a-c for a,c in zip(formed,quotient_formula)],
                original_quotient_rule_per_logical_occurrence=quotients,
                ratio_reformation_word_mismatch_variable_ids=word_differences,
                complete_three_response_finite=finite,
                formed_original_full3_merit_action=gradient,
                absolute_formed_original_merit_action=abs(gradient),
                formed_slope_finite=gradient.is_finite(),
                formed_slope_nonzero=gradient!=0,
                actual_original_three_equations=self.F,
                all_occurrence_scalar_a_b_q_words_equal=all_common_scalar_words,
                equality_of_values_is_not_a_source_shared_variable_proof=True,
                logical_occurrence_weights_never_discarded=True,
                all_same_position_occurrences_receive_the_same_shape_jet=True,
                formula_scope=SCOPE,
                sum_common_weight_over_one_denominator_not_used_as_a_shortcut=True,
                node_then_mid_contraction_retained_but_omitted_zero_terms_not_claimed_word_identical=True,
                formed_action_is_a_proposal_not_a_rank_accuracy_or_acceptance_certificate=True)

    def build(self):
        require_actions()
        if self.groups or self.complete or self.failure is not None:
            raise CatalogueInputError('Build once; partial catalogues are not silently resumed')
        grouped={}
        try:
            self.stage='all1397 actual node/mid occurrences and exact repeated positions'
            for kind,stations,scalars,ratios,weights in (
                    ('node',self.nodes,self.node_scalar,self.node_q,self.node_weights),
                    ('midpoint',self.mids,self.mid_scalar,self.mid_q,self.mid_weights)):
                for i,(s,scalar,q,weight) in enumerate(zip(stations,scalars,ratios,weights)):
                    self._check()
                    row=self._occurrence(kind,i,s,scalar,q,weight)
                    grouped.setdefault(row['position'],[]).append(row)
                    self.visited_occurrences[kind]=i+1
            positions=sorted(grouped)
            for i,position in enumerate(positions):
                self.groups.append(dict(group_id=i,position=position,
                    occurrences=grouped[position],candidate=None))
            self.grouping_complete=True
            self.stage='strict dyadic isolation and complete formed three-response'
            for group in self.groups:
                self._check()
                i=group['group_id'];position=group['position']
                support_choices=[]
                for support in self.supports:
                    if support['open_left']<position<support['open_right']:
                        distances=[position-support['open_left'],support['open_right']-position]
                        if i>0:distances.append(position-positions[i-1])
                        if i+1<len(positions):distances.append(positions[i+1]-position)
                        support_choices.append((min(distances),support['index'],support))
                if not support_choices:
                    self.skipped.append(dict(group_id=i,position=rational_record(position),
                        reason='No declared original-support interior also strictly between fixed start and terminal'))
                    self.processed_groups+=1
                    continue
                # One physical shape per unique station. If original supports
                # overlap, the widest permitted exact gap wins; index breaks ties.
                support_choices.sort(key=lambda row:(-row[0],row[1]))
                gap,support_index,support=support_choices[0]
                if gap<=0:
                    raise CatalogueInputError('A distinct internal station requires a positive exact isolation gap')
                epsilon=Fraction(1);halvings=0
                while epsilon>=gap/4:
                    self._check();epsilon/=2;halvings+=1
                proof=dict(group_id=i,actual_position=rational_record(position),
                    selected_original_support=self._support_record(support),
                    all_containing_original_support_indices=[x[1] for x in support_choices],
                    exact_minimum_other_station_or_allowed_boundary_gap=rational_record(gap),
                    exact_epsilon_strictly_less_than_gap_over_four=epsilon<gap/4,
                    epsilon_halvings_from_one=halvings,
                    previous_distinct_station=None if i==0 else rational_record(positions[i-1]),
                    next_distinct_station=None if i+1==len(positions) else rational_record(positions[i+1]),
                    fixed_start_coordinate=rational_record(self.start),
                    fixed_terminal_coordinate=rational_record(self.end),
                    selection_grid_identity=self.binding['original_node_mid_decimal_coordinate_sha256'],
                    fixed_start_and_direct_terminal_shape_jets_zero_by_strict_isolation=True)
                shape=FrozenLocalShape(position,epsilon,proof)
                record=dict(group_id=i,shape_definition=shape.definition(),
                    logical_occurrence_count=len(group['occurrences']),
                    occurrences=[{k:v for k,v in row.items() if k!='position'} for row in group['occurrences']],
                    source_shared_q_policy='Each node:index or midpoint:index is one actual R351 variable. Cell-role sharing is already scattered; equal coordinates across distinct IDs are not asserted aliases.',
                    duplicated_physical_position=len(group['occurrences'])>1,
                    source_identified_single_q_variable=len(group['occurrences'])==1,
                    binary64_definition=shape.binary64_definition(),
                    response=None,response_error=None)
                try:
                    record['response']=self._formed_response(group['occurrences'],epsilon)
                except Exception as error:
                    record['response_error']=dict(exception=repr(error),traceback=traceback.format_exc(),
                        no_stationarity_or_infeasibility_inference=True)
                self.candidates.append(record);group['candidate']=len(self.candidates)-1
                self.processed_groups+=1
                if self.processed_groups%64==0 or self.processed_groups==len(self.groups):
                    self._emit('R363-station-catalogue-progress',processed_groups=self.processed_groups,
                        total_unique_positions=len(self.groups),candidate_shapes=len(self.candidates))
            self.complete=True;self.stage='complete actual-position catalogue; no nonlinear proposal accepted'
        except Exception as error:
            self.failure=dict(stage=self.stage,exception=repr(error),traceback=traceback.format_exc(),
                resource_partial=isinstance(error,CatalogueResourceStop),
                mathematical_nonexistence_not_inferred=True)
            raise
        finally:
            self._emit('R363-station-catalogue-return',report=self.report())
        return self

    def _candidate(self,group_id):
        require_actions()
        if not isinstance(group_id,int) or isinstance(group_id,bool) or not 0<=group_id<len(self.groups):
            raise CatalogueInputError('Use an actual formed group ID')
        index=self.groups[group_id]['candidate']
        if index is None:
            raise CatalogueInputError('This position has no declared support-isolated candidate')
        return self.candidates[index]

    def shape_definition(self,group_id):
        return metadata_copy(self._candidate(group_id)['shape_definition'])

    def materialize_current_grid(self,group_id,*,run_existing_sampled_response=False):
        """Exact current-grid jets and separately formed original binary64 words.

        Optional R351 contraction is a diagnostic on this same old-nine point.
        It is neither a new nonlinear family nor a trial/acceptance gate.
        """
        require_actions();self._check()
        candidate=self._candidate(group_id)
        shape=FrozenLocalShape.from_definition(candidate['shape_definition'])
        b=self.b;exact_nodes=[];exact_mids=[];actual_nodes=[];actual_mids=[]
        value_mismatches=[];negative_zero_words=[];station_projection_differences=[]
        group_position=self.groups[group_id]['position']
        for kind,positions,exact_out,actual_out in (
                ('node',self.nodes,exact_nodes,actual_nodes),
                ('midpoint',self.mids,exact_mids,actual_mids)):
            for i,s in enumerate(positions):
                self._check()
                exact=shape.jet_exact(s)
                expected=(Fraction(0),shape.epsilon,Fraction(0)) if rational(s)==group_position else (Fraction(0),Fraction(0),Fraction(0))
                if exact!=expected:
                    raise CatalogueInputError('Exact current-grid isolation or zero-jet formula identity failed')
                sf=float(s)
                if Fraction.from_float(sf)!=rational(s):
                    station_projection_differences.append(dict(kind=kind,index=i,
                        original=str(s),binary64=float_record(sf)))
                actual=shape.jet_binary64(sf)
                if not all(math.isfinite(x) for x in actual):
                    raise ShapeRepresentationError('An actual binary64 local-shape jet is nonfinite')
                exact_out.append([rational_record(x) for x in exact])
                actual_out.append([b.dec(actual[0]),b.dec(actual[1])])
                for component,(q,v) in enumerate(zip(exact,actual)):
                    if Fraction.from_float(v)!=q:
                        value_mismatches.append(dict(kind=kind,index=i,component=component,
                            exact=rational_record(q),actual=float_record(v)))
                    if v==0.0 and math.copysign(1.0,v)<0:
                        negative_zero_words.append(dict(kind=kind,index=i,component=component,word=v.hex()))
        binding=dict(kind='independent-sampled-scalar-shape',coefficient_is_an_original_nine_parameter=False,
            source=own_identity(),definition=dict(family_schema=SHAPE_SCHEMA,formula=FORMULA,
                support=dict(left=rational_record(shape.left),right=rational_record(shape.right)),
                center=rational_record(shape.center),epsilon=rational_record(shape.epsilon),
                mathematical_identity_sha256=shape.mathematical_sha256,
                zero_jet_proof_reference='R363-local-C2-shapes-and-complete-finite-sample-response-rank',
                frozen_center_width_must_be_preserved_for_same_g_refinement=True),
            coordinate_contract=dict(derivative_column='derivative with respect to original scalar-table coordinate',
                literal_mesh_canonical_sha256=b.digest(dict(nodes=self.nodes,middle=self.mids))))
        record=dict(schema=SCHEMA,group_id=group_id,shape_definition=shape.definition(),
            exact_current_grid_formula_identity=b.digest(dict(nodes=exact_nodes,middle=exact_mids)),
            actual_binary64_value_and_returned_derivative_lift_identity=b.digest(dict(nodes=actual_nodes,middle=actual_mids)),
            node_count=NODE_COUNT,midpoint_count=CELL_COUNT,
            exact_real_Kronecker_sampling_verified_from_rational_formula=True,
            actual_binary64_values_equal_exact_rational_jet_values=not value_mismatches,
            actual_binary64_value_mismatches=value_mismatches,
            negative_zero_original_words=negative_zero_words,
            coordinate_binary64_projection_differences=station_projection_differences,
            source_bound_shape_binding=binding,
            fixed_start_and_terminal_shape_012_jets_exactly_zero=True,
            binary64_checks_are_diagnostics_not_new_accuracy_or_acceptance_gates=True,
            original_R351_complete112_sampled_response=None,
            new_nonlinear_model_or_trial_or_accepted_field_created=False,
            new_family_and_continuous_domain_breakpoint_registration_still_required=True,
            independent_extended_owner_and_fresh_current_forward_still_required=True)
        if run_existing_sampled_response:
            record['original_R351_complete112_sampled_response']=self.adjoint.sampled_shape_response(
                actual_nodes,actual_mids,binding)
        self.materializations.append(dict(group_id=group_id,record_canonical_sha256=b.digest(record),
            optional_original_R351_complete112_response_executed=bool(run_existing_sampled_response)))
        self._emit('R363-current-grid-shape-materialized',
            group_id=group_id,record_canonical_sha256=b.digest(record),
            no_original_nonlinear_trial=True)
        return dict(record=record,exact_node_jets=exact_nodes,exact_midpoint_jets=exact_mids,
            actual_binary64_node_pairs=actual_nodes,actual_binary64_midpoint_pairs=actual_mids,
            frozen_shape=shape)

    def report(self,maximum_candidate_records=8):
        require_actions()
        if not isinstance(maximum_candidate_records,int) or not 0<=maximum_candidate_records<=16:
            raise CatalogueInputError('Use an explicitly small report; the full catalogue remains temporary')
        b=self.b
        usable=[row for row in self.candidates if row['response'] is not None
            and row['response']['formed_slope_finite'] and row['response']['complete_three_response_finite']]
        ordered=sorted(usable,key=lambda row:(-row['response']['absolute_formed_original_merit_action'],row['group_id']))
        top=[]
        for row in ordered[:maximum_candidate_records]:
            response=row['response'];definition=row['shape_definition']
            top.append(dict(group_id=row['group_id'],
                original_support_index=definition['selection']['selected_original_support']['index'],
                exact_center=definition['mathematical']['center'],exact_epsilon=definition['mathematical']['epsilon'],
                mathematical_shape_sha256=definition['mathematical_sha256'],
                logical_occurrence_count=row['logical_occurrence_count'],
                source_identified_single_q_variable=row['source_identified_single_q_variable'],
                actual_formed_response=response['complete_three_formed_response'],
                actual_rounded_quotient_formula_response=response['complete_three_rounded_epsilon_sum_weight_over_a'],
                actual_formed_merit_action=response['formed_original_full3_merit_action'],
                actual_formed_action_absolute_value=response['absolute_formed_original_merit_action'],
                all_occurrence_scalar_a_b_q_words_equal=response['all_occurrence_scalar_a_b_q_words_equal'],
                binary64_definition=row['binary64_definition'],
                whole_original_candidate_canonical_sha256=b.digest(row),
                finite_score_is_only_a_proposal=True))
        occurrence_count=sum(len(row['occurrences']) for row in self.groups)
        processed_ids=sorted({row['group_id'] for row in self.candidates+self.skipped})
        unvisited_ids=[row['group_id'] for row in self.groups if row['group_id'] not in processed_ids]
        return dict(schema=SCHEMA,source=own_identity(),complete=self.complete,stage=self.stage,
            binding=self.binding,failure=self.failure,
            original_node_count=NODE_COUNT,original_midpoint_count=CELL_COUNT,
            actual_occurrence_grouping_complete=self.grouping_complete,
            visited_logical_occurrences=dict(self.visited_occurrences),
            unvisited_node_indices=list(range(self.visited_occurrences['node'],NODE_COUNT)),
            unvisited_midpoint_indices=list(range(self.visited_occurrences['midpoint'],CELL_COUNT)),
            grouped_logical_occurrence_count=occurrence_count,
            unique_physical_positions=(len(self.groups) if self.grouping_complete else None),
            grouped_position_records_so_far=len(self.groups),
            repeated_position_groups=(sum(len(row['occurrences'])>1 for row in self.groups)
                if self.grouping_complete else None),
            processed_unique_position_groups=len(processed_ids),
            processed_unique_group_ids=processed_ids,
            unvisited_unique_group_ids=(unvisited_ids if self.grouping_complete else None),
            allowed_candidate_count=len(self.candidates),skipped_group_count=len(self.skipped),
            response_error_count=sum(row['response_error'] is not None for row in self.candidates),
            formed_finite_response_count=len(usable),
            formed_nonzero_merit_action_count=sum(row['response']['formed_slope_nonzero'] for row in usable),
            all_finite_formed_actions_zero=(all(not row['response']['formed_slope_nonzero'] for row in usable) if usable else None),
            original_supports=[self._support_record(row) for row in self.supports],
            exact_position_and_occurrence_layout_sha256=b.digest([
                dict(group_id=row['group_id'],position=rational_record(row['position']),
                    occurrences=[{k:v for k,v in item.items() if k!='position'} for item in row['occurrences']])
                for row in self.groups]),
            complete_candidate_catalogue_sha256=b.digest(self.candidates),
            complete_skipped_groups_sha256=b.digest(self.skipped),
            small_actual_candidate_records=top,large_catalogue_or_weight_matrix_transported=False,
            materialization_receipts=list(self.materializations),
            no_explicit_candidate_parent_or_shape_selected_by_requestless_source=True,
            no_new_RHS_J_nonlinear_primal_or_trial_executed_here=True,
            optional_existing_formed_R351_sampled_response_is_separately_recorded=True,
            formed_weights_and_scores_not_exact_derivative_sign_or_rank_certificates=True,
            same_position_general_value_jet_span_not_claimed=True,
            duplicate_occurrence_scope=SCOPE,
            old_nine_point_only_this_version=True,
            future_actual_ten_point_requires_explicit_new_local_trace_source=True,
            all_original_new_family_domain_FD_circle_native_final_obligations_retained=True,
            no_new_numeric_rank_or_comparison_gate=True,
            elapsed_wall_seconds=format(time.monotonic()-self.started,'.9f'))
