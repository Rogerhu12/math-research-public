#!/usr/bin/env python3
"""Actual source-bound growing model -> complete true cap-to-mouth anchor.

The input identity is captured BEFORE forming any bound. Every original
homogeneous, pre-tanh, envelope, local-extra and forced coefficient is read
from that actual model/literal source. Every new analytic tail column and
requested parameter direction is included. No caller supplies a preassembled
response budget that can be re-labelled as another Gaussian policy.

This is pure source for a future public scope, with no invented actual q or
normalization certificate. A complete explicit source-error contract is
mandatory. Unpaid finite-M/Cauchy/ODE/normalization/roundoff errors remain
unresolved; a strict consumer rejects them. Conditional numeric consumption
never becomes a complete geometry certificate.
"""
from collections import defaultdict
from decimal import Decimal
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

HEIGHT_SHA = '87fdb14d80d12836c6328d3adf83abfc020300e468da43b3ebfffe4bdc6409e2'
BOUNDS_SHA = '83ecdfaa26a8cd4dc399ef0ffaf714263696b8309b2cda6a74e5d5fc764c0e53'
HERE = Path(__file__).resolve().parent
COUNTS = defaultdict(int)
ERROR_CATEGORIES = ('finite_M_to_true_infinite_germs','paid_finite_Cauchy_roundoff',
    'dense_ODE_and_connector_core_normalizations','original_envelope_normalizations',
    'original_forced_tail_multiplier_and_scale','literal_coefficient_realization',
    'same_reference_E_and_mean_branch_numerical_evaluation')


def bound_import():
    path = HERE/'r618_analytic_tail_anchor_bound_20261127.py'
    if hashlib.sha256(path.read_bytes()).hexdigest() != BOUNDS_SHA:
        raise RuntimeError('whole-tail bound source changed')
    spec = importlib.util.spec_from_file_location('r618_actual_tail_anchor_bounds',path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


bounds = bound_import()
I = bounds.I


def json_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
                                     allow_nan=False).encode()).hexdigest()


def literal_interval(value):
    """Enclose a JSON decimal exactly, with no rounded product before I."""
    decimal = value if isinstance(value,Decimal) else Decimal(str(value))
    if not decimal.is_finite():
        raise ValueError('finite literal decimal required')
    center = float(decimal)
    if not math.isfinite(center):
        raise ArithmeticError('literal source parameter overflows interval arithmetic')
    represented = Decimal.from_float(center)
    lo = math.nextafter(center,-math.inf) if represented > decimal else center
    hi = math.nextafter(center,math.inf) if represented < decimal else center
    return I(lo,hi)


def supplied_interval(value):
    if not isinstance(value,dict) or set(value) != {'lo','hi'}:
        raise ValueError('each supplied source interval requires explicit lo and hi')
    low,high = literal_interval(value['lo']),literal_interval(value['hi'])
    return I(low.lo,high.hi)


def absolute(value):
    bounds.intervals(value)
    return I(0,max(abs(value.lo),abs(value.hi)))


def include_observation(value,observed,label):
    if not value.lo <= float(observed) <= value.hi:
        raise ValueError('the bound source interval does not contain the actual reconstructed '+label)
    return value


def tree_intervals(value):
    if isinstance(value,I):
        return {'lo':value.lo,'hi':value.hi}
    if isinstance(value,dict):
        return {str(key):tree_intervals(item) for key,item in value.items()}
    if isinstance(value,(tuple,list)):
        return [tree_intervals(item) for item in value]
    return value


class CurrentModelTailAnchor:
    """One actual response/model/source producer, no post-hoc identity input.

    source_contract_json is a literal reviewed contract for THIS frozen
    target/model. It contains all normalization intervals and an explicit
    evidence/status row for every ERROR_CATEGORIES entry. A status can be
    'unresolved' or 'covered_by_supplied_exact_source_enclosures'; neither
    absence nor a missing field means zero error. In strict mode all rows
    must have the latter status. Conditional mode reports all unresolved rows.
    """
    def __init__(self,model,response,data,parameter_indices,*,
                 source_contract_json,source_contract_sha256,
                 require_source_errors_enclosed):
        bounds.public_only()
        module = sys.modules.get(type(model).__module__)
        if (module is None or Path(module.__file__).resolve() !=
                (HERE/'r618_growing_post_fixed_metric_height_20261127.py').resolve()
                or hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest() != HEIGHT_SHA):
            raise ValueError('the exact source-bound complete growing model is required')
        self.model,self.data = model,data
        self.response = model._check_response(response).copy()
        state_identity = model._field_identity(self.response,data,include_angles=False)
        indices = list(parameter_indices)
        if (any(type(index) is not int or not 0 <= index < model.nq for index in indices)
                or len(set(indices)) != len(indices)):
            raise ValueError('all requested parameter indices must be distinct actual columns')
        self.identity = {'target_sha256':model.identity.target_sha256,
            'response_model_sha256':state_identity['response_model_sha256'],
            'response_sha256':state_identity['response_sha256'],
            'cap_radius':float(model.base.RC),'mouth_radius':float(data['r'][0]),
            'parameter_indices':indices}
        self.radial_grid_sha256 = state_identity['radial_grid_sha256']
        self.indices = indices
        if hashlib.sha256(source_contract_json.encode()).hexdigest() != source_contract_sha256:
            raise ValueError('literal reviewed tail source contract changed')
        contract = json.loads(source_contract_json)
        self.contract,self.contract_sha = contract,source_contract_sha256
        definition = json.loads(model.identity.mathematical_field_json)
        expected = {'target_sha256':self.identity['target_sha256'],
            'response_model_sha256':self.identity['response_model_sha256'],
            'reconstruction_source_sha256':model.original_reconstruction_receipt['reconstruction_source_sha256'],
            'true_inner_definition_sha256':json_sha(definition['accurate_inner_tail_definition']),
            'true_germ_choice':'same_R600_accurate_infinite_germs_with_all_source_errors_accounted',
            'original_inner_phase':0}
        for key,value in expected.items():
            if contract.get(key) != value:
                raise ValueError('actual tail producer source identity differs: '+key)
        rows = contract.get('source_error_accounting')
        if not isinstance(rows,dict) or set(rows) != set(ERROR_CATEGORIES):
            raise ValueError('every old finite-M/Cauchy/ODE/normalization/source error requires an explicit row')
        self.unresolved = []
        for key,row in rows.items():
            if (not isinstance(row,dict) or not row.get('evidence')
                    or row.get('status') not in ('unresolved','covered_by_supplied_exact_source_enclosures')):
                raise ValueError('explicit original error status and evidence required: '+key)
            if row['status'] == 'unresolved':
                self.unresolved.append({'category':key,'evidence':row['evidence']})
        if type(require_source_errors_enclosed) is not bool:
            raise TypeError('strict versus conditional consumption must be explicitly selected')
        self.strict = require_source_errors_enclosed
        if self.strict and self.unresolved:
            raise ArithmeticError('strict cap anchor blocked by explicit unresolved original source errors')
        if not (float(model.base.RC) == .22 and float(model.base.ELL) == .2
                and float(model.amplitude) == 1e-5 and float(model.old.args.height_saturation) == .15):
            raise ValueError('same original physical tail/amplitude/canonical saturation required')
        if [int(mode.mode) for mode in model.old.modes] != list(range(2,23,2)):
            raise ValueError('all original modes2..22 must be present')
        if list(map(int,model.old.column_modes[:10])) != list(range(4,23,2)):
            raise ValueError('original true-germ coefficient order changed')
        self.rc,self.ell,self.A = I(11)/50,I(1)/5,I(4)/5
        self.mouth = I(self.identity['mouth_radius'])
        u = self.ell/(self.mouth-self.rc)
        if u.lo < 108:
            raise ArithmeticError('the entire actual cap-to-mouth interval is outside the proved common window')
        self.U = I(u.lo)
        self.W_upper = bounds.upper(self.A*bounds.exp_i(-self.U))
        # This actual mouth lies below every old body/compact/core cutoff.
        # All omitted-from-tail columns are zero by their retained support,
        # and are still explicitly counted as parameter directions below.
        support_left = min(float(model.driver.weak.BULK_LEFT),
            float(model.compact.PATCH_KNOTS[0][0]),float(model.driver.complete.CORE_LEFT),
            float(model.core_lift_left),.53)
        if self.mouth.hi >= support_left or self.mouth.hi > model.tail_left:
            raise ArithmeticError('original support-based zero tail columns no longer apply at this actual mouth')
        self.source_snapshot_sha256 = self._snapshot()
        self.seed_ratio,self.raw_ratio,self.germ_receipts = self._old_germs()
        self.gaussian_columns = {}
        self.amplitude = I(1)/100000
        self.reference_scaled = self._reference_scaled()
        self.response_budget = self._response_budget()
        self.direction_budgets = [self._direction_budget(index) for index in self.indices]
        L = literal_interval(model.policy['mean_bracket_radius']['lambda'])
        E_lower = supplied_interval(contract['whole_reference_E_lower_bound'])
        E_upper = supplied_interval(contract['whole_reference_E_upper_bound'])
        self.branch = bounds.uniform_mean_branch(rc=self.rc,mouth=self.mouth,
            W_upper=self.W_upper,E_lower=E_lower,E_upper=E_upper,L=L,
            reference_scaled=self.reference_scaled,response_budget=self.response_budget)
        if self._snapshot() != self.source_snapshot_sha256:
            raise ValueError('the actual original/new source changed during cap-anchor production')
        COUNTS['actual_response_complete_anchor_producers'] += 1

    def _snapshot(self):
        m = self.model;old = m.old;paid = old.old
        return json_sha({'target_sha256':m.identity.target_sha256,'policy':m.policy,
            'q_reference':m.q_reference.tolist(),'paidq':old.paidq.tolist(),
            'mode_inputs':[[int(mode.mode),float(mode.flat.display_log),float(mode.Acore)] for mode in old.modes],
            'old_height_scales':paid.mode_height_scales.tolist(),
            'old_envelope_scale':float(paid.envelope_scale),'old_knots':paid.bs.t.tolist(),
            'old_degree':int(paid.bs.k),'old_basis_count':int(paid.nb),
            'force_tail_multiplier':float(paid.forced.tail_multiplier),'force_scale':float(paid.forced.scale),
            'R':float(m.par.R),'alpha':float(m.par.alpha),
            'tail_shape':[m.tail_left,m.tail_right,m.tail_denominator],
            'tail_degrees':m.tail_degrees.tolist(),'all_independent_modes':m.modes.tolist(),
            'response':self.response.tolist(),'original_reconstruction':m.original_reconstruction_receipt,
            'radial_identity':m._field_identity(self.response,self.data,include_angles=False)})

    def _old_germs(self):
        rows = self.contract['old_germ_normalizations']
        if set(rows) != {str(j) for j in range(2,23,2)}:
            raise ValueError('every original true germ2..22 needs its own complete normalization interval')
        normalized,raw,receipts = {},{},{}
        for mode in self.model.old.modes:
            j = int(mode.mode);row = rows[str(j)]
            D = include_observation(supplied_interval(row['display_log']),mode.flat.display_log,'display log')
            c = include_observation(supplied_interval(row['core_A_abs']),abs(mode.Acore),'core normalization')
            bounds.positive(c)
            normalized[j] = bounds.normalized_old_mode_ratio(mode=j,display_log=D,normalization_abs=c)
            raw[j] = bounds.normalized_old_mode_ratio(mode=j,display_log=D,normalization_abs=I(1))
            receipts[str(j)] = {'display_log':D,'core_A_abs':c,'normalized_ratio_bound':normalized[j],
                'raw_ratio_bound':raw[j],'accurate_infinite_germ_not_a_finite_M_error_certificate':True}
        return normalized,raw,receipts

    def _old_budget(self,j,coefficient_abs,*,raw=False):
        return bounds.old_mode_response_budget(mode=j,coefficient_abs=coefficient_abs,
            ratio_bound=(self.raw_ratio if raw else self.seed_ratio)[j],
            rc=self.rc,mouth=self.mouth,W_upper=self.W_upper)

    def _reference_scaled(self):
        m = self.model;old = m.old;paid = old.old
        # Literal original q/knots are read from the same bound original
        # module, then checked against the actual object's complete arrays.
        raw_q,raw_knots = m.driver.weak.RAW_Q_JSON,m.driver.weak.RAW_KNOT_JSON
        if (hashlib.sha256(raw_q.encode()).hexdigest() != m.driver.weak.SOURCE_Q_SHA
                or hashlib.sha256(raw_knots.encode()).hexdigest() != m.driver.weak.SOURCE_KNOT_SHA):
            raise ValueError('original paid q or complete knot literal identity changed')
        paid_q = json.loads(raw_q,parse_float=Decimal)
        knots = json.loads(raw_knots,parse_float=Decimal)
        reference = json.loads(m.original_q_json,parse_float=Decimal)
        if ([float(x) for x in paid_q] != old.paidq.tolist()
                or [float(x) for x in knots] != paid.bs.t.tolist()
                or [float(x) for x in reference] != m.q_reference.tolist()):
            raise ValueError('literal coefficients/knots and actual original model disagree')
        degree = int(paid.bs.k);base_count = len(knots)-degree-1
        if (degree != 5 or paid.nb != base_count+4
                or paid.original_nq != 4+4*paid.nb or len(paid_q) != paid.original_nq+1):
            raise ValueError('complete old spline plus four exact local-extra columns required')
        if any(a > b for a,b in zip(knots[:-1],knots[1:])):
            raise ValueError('original knot order changed')
        P,Q = [],[]
        for index in range(base_count):
            slope = I(0)
            for left,right in ((index,index+degree),(index+1,index+degree+1)):
                if knots[left] == knots[right]:
                    continue
                width = literal_interval(knots[right])-literal_interval(knots[left])
                bounds.positive(width)
                slope += degree/width
            P.append(I(1));Q.append(bounds.upper(slope))
        # All four old local-enrichment columns start at.53. Their original
        # coefficients remain in the complete array; P=Q=0 is their exact
        # restriction to this true tail, not a numerical underflow shortcut.
        P.extend([I(0)]*4);Q.extend([I(0)]*4)
        self.original_basis_receipt = {'full_knot_sha256':m.driver.weak.SOURCE_KNOT_SHA,
            'base_B_spline_count':base_count,'old_local_extra_columns':4,
            'all_old_pre_tanh_coefficients_included':4*paid.nb,
            'whole_tail_basis_value_bounds':P,'whole_tail_basis_derivative_bounds':Q}
        normal = self.contract['old_envelope_and_force_normalizations']
        if len(normal['mode_height_scales']) != 4:
            raise ValueError('all four original mode height normalizations required')
        scales = [include_observation(supplied_interval(row),value,'mode height normalization')
                  for row,value in zip(normal['mode_height_scales'],paid.mode_height_scales)]
        C = include_observation(supplied_interval(normal['envelope_scale']),paid.envelope_scale,'envelope normalization')
        force_multiplier = include_observation(supplied_interval(normal['force_tail_multiplier']),
                                               paid.forced.tail_multiplier,'forced tail multiplier')
        force_scale = include_observation(supplied_interval(normal['force_scale']),paid.forced.scale,'forced scale')
        bounds.positive(C,force_scale,*scales)
        R = include_observation(supplied_interval(self.contract['physical_R']),m.par.R,'physical R')
        alpha = include_observation(supplied_interval(self.contract['physical_alpha']),m.par.alpha,'physical alpha')
        envelope = bounds.original_envelope_bounds(seed_ratio_bounds=[self.seed_ratio[j] for j in (2,4,6,8)],
            height_scales=scales,envelope_scale=C,rc=self.rc,ell=self.ell,A=self.A,
            mouth=self.mouth,R=R,p=2+2*alpha,gamma=I(1)/10000,W_upper=self.W_upper)
        seed_coefficients = [self.amplitude]+[absolute(self.amplitude*literal_interval(x)) for x in paid_q[1:4]]
        bulk = [[absolute(self.amplitude*literal_interval(paid_q[4+j*paid.nb+i]))
                 for i in range(paid.nb)] for j in range(4)]
        post = [self._old_budget(j,absolute(self.amplitude*literal_interval(reference[index+1])))
                for index,j in enumerate(range(4,23,2))]
        force_coefficient = absolute(self.amplitude**2*literal_interval(paid_q[paid.original_nq])
                                     *force_multiplier/force_scale)
        post.append(self._old_budget(4,force_coefficient,raw=True))
        post_budget = bounds.add_budgets(post)
        self.reference_construction_receipt = {'canonical_mean_points':512,
            'actual_original_paid_q_sha256':m.driver.weak.SOURCE_Q_SHA,
            'actual_original_reference_q_sha256':hashlib.sha256(m.original_q_json.encode()).hexdigest(),
            'old_envelope_bound':envelope,'fixed_forced_tail_coefficient_abs':force_coefficient,
            'old_post_homogeneous_modes':list(range(4,23,2)),
            'fixed_force_mode':4,'canonical_mean_not_replaced_by_output_grid_mean':True}
        return bounds.original_reference_scaled_jets(seed_ratio_bounds=[self.seed_ratio[j] for j in (2,4,6,8)],
            seed_coefficient_abs=seed_coefficients,bulk_coefficient_abs=bulk,
            basis_value_bounds=P,basis_derivative_bounds=Q,envelope=envelope,
            post_scaled_budget=post_budget['scaled'],W_upper=self.W_upper,saturation=I(3)/20)

    def _gaussian(self,j,k):
        key = (j,k)
        if key not in self.gaussian_columns:
            m = self.model
            self.gaussian_columns[key] = bounds.gaussian_column_bounds(rc=self.rc,ell=self.ell,A=self.A,
                mouth=self.mouth,denominator=literal_interval(m.policy['tail_gaussian_denominator']),
                cutoff_left=literal_interval(m.policy['tail_cutoff_left']),
                cutoff_right=literal_interval(m.policy['tail_cutoff_right']),degree=k,mode=j)
        return self.gaussian_columns[key]

    def _response_budget(self):
        m = self.model
        budgets = [self._old_budget(j,absolute(self.amplitude*literal_interval(float(self.response[index]))))
                   for index,j in enumerate(range(4,23,2))]
        for mode_index,j in enumerate(m.modes):
            for basis_index,k in enumerate(m.tail_degrees):
                index = m.tail_start+mode_index*len(m.tail_degrees)+basis_index
                coefficient = absolute(self.amplitude*literal_interval(float(self.response[index])))
                budgets.append(bounds.gaussian_response_budget(self._gaussian(int(j),int(k)),coefficient))
                COUNTS['actual_new_tail_coefficients_included'] += 1
        COUNTS['actual_original_true_germ_response_coefficients_included'] += 10
        return bounds.add_budgets(budgets)

    def _direction_budget(self,index):
        m = self.model
        COUNTS['actual_parameter_direction_tail_budgets'] += 1
        if index < 10:
            return self._old_budget(4+2*index,self.amplitude)
        if m.tail_start <= index < m.core_start:
            mode,basis = divmod(index-m.tail_start,len(m.tail_degrees))
            return bounds.gaussian_response_budget(self._gaussian(int(m.modes[mode]),int(m.tail_degrees[basis])),
                                                   self.amplitude)
        COUNTS['actual_parameter_directions_zero_by_original_support'] += 1
        return bounds.empty_budget()

    def result(self):
        bounds.public_only()
        if self._snapshot() != self.source_snapshot_sha256:
            raise ValueError('actual source/response/grid changed before consuming its cap anchor')
        radii = [bounds.mean_integral_radius(self.branch,self.response_budget)]
        radii.extend(bounds.mean_integral_radius(self.branch,budget) for budget in self.direction_budgets)
        evidence = {'producer_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'whole_tail_bounds_source_sha256':BOUNDS_SHA,'height_model_source_sha256':HEIGHT_SHA,
            'input_identity_captured_before_arithmetic':dict(self.identity),
            'actual_model_source_snapshot_sha256':self.source_snapshot_sha256,
            'literal_source_contract_sha256':self.contract_sha,
            'radial_grid_sha256':self.radial_grid_sha256,
            'complete_old_germ_normalizations':tree_intervals(self.germ_receipts),
            'complete_original_basis':tree_intervals(self.original_basis_receipt),
            'complete_original_reference':tree_intervals(self.reference_construction_receipt),
            'reference_scaled_jets':tree_intervals(self.reference_scaled),
            'complete_response_budget':tree_intervals(self.response_budget),
            'all_requested_direction_budgets':tree_intervals(self.direction_budgets),
            'whole_continuous_mean_branch':tree_intervals(self.branch),
            'old_source_error_accounting':self.contract['source_error_accounting'],
            'all_new_tail_modes_and_degrees':[[int(j),int(k)] for j in self.model.modes for k in self.model.tail_degrees],
            'unknown_old_M_or_ODE_errors_assigned_zero':False}
        return {**self.identity,'integral_and_directions':[0.]*len(radii),
            'absolute_error_bounds_or_unresolved_radii':[radius.hi for radius in radii],
            'true_tail_evidence':evidence,'unresolved_errors':list(self.unresolved),
            'all_tail_input_errors_enclosed':not self.unresolved,
            'strict_source_consumer_requested':self.strict,
            'conditional_exact_source_interval_consequence':bool(self.unresolved),
            'zero_centers_are_proved_or_conditional_integral_enclosures_not_zero_tail_continuation':True,
            'entire_body_metric_reach_or_README_certified':False,
            'producer_cumulative_counts':dict(COUNTS),'bound_helper_cumulative_counts':dict(bounds.COUNTS)}
