#!/usr/bin/env python3
"""Actual R643 true cap-to-mouth fields, without an implicit-trial-mean gate.

Reuse source-bound infinite-germ and Gaussian inequalities, including every
old normalization/error. The paid accepted seed mean bound is consumed as
such. The94 free mean columns contribute their actual four Gaussian tails;
all other mean columns vanish here by their genuine support. No c0/lambda
box is imposed on the new trial mean. This does not close the continuous
new connection/position error in the unseen tail.
"""
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
PRODUCER_SHA = '0fcbc3608dc7bb8c05285f1fea11e2416303867f9c961e3b712170d830942c0e'
SEED_FINAL_SHA = '1fb5abfdf70e6c8154938b07ec5bd3353b68735c0dd5fd49f704204e65bd024e'
SEED_RESPONSE_SHA = '19519575f7b4a8100cf9813851c258188ad4a0063edad05eb1b5b332b83f2cc7'
COUNTS = defaultdict(int)


def _load():
    path = HERE/'r618_current_model_tail_anchor_20261127.py'
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PRODUCER_SHA:
        raise RuntimeError('unchanged exact-source tail formulas changed')
    spec = importlib.util.spec_from_file_location('r643_paid_tail_source_formulas',path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


paid = _load()
bounds,I = paid.bounds,paid.I


def _seed_anchor(model,natural_terminal,data):
    literal = natural_terminal['literal_FINAL_JSON']
    if hashlib.sha256(literal.encode()).hexdigest()!=SEED_FINAL_SHA:
        raise ValueError('same natural completed seed FINAL required')
    final = json.loads(literal)
    anchor = final['summary']['last_report']['true_tail_anchor']
    expected = dict(target_sha256=model.identity.target_sha256,
                    response_model_sha256=model.owned.response_model_sha256,
                    response_sha256=SEED_RESPONSE_SHA,cap_radius=model.base.RC,
                    mouth_radius=float(data['r'][0]))
    if (any(anchor.get(key)!=value for key,value in expected.items())
            or anchor['parameter_indices']!=[]
            or len(anchor['integral_and_directions'])!=1
            or len(anchor['absolute_error_bounds_or_unresolved_radii'])!=1
            or not anchor['conditional_whole_tail_mean_branch']
                ['all_radial_points_below_the_original_mouth_and_all_angles_covered']):
        raise ValueError('paid true seed anchor and actual original mouth differ')
    result = json.loads(json.dumps(anchor))
    result['true_tail_evidence'] = {
        'consumed_original_natural_FINAL_sha256':SEED_FINAL_SHA,
        'consumed_run_id':46117718197,'consumed_job_id':140895158286,
        'same_actual_seed_response_sha256':SEED_RESPONSE_SHA,
        'paid_conditional_whole_tail_mean_branch':result['conditional_whole_tail_mean_branch'],
        'original_unresolved_source_errors_retained':result['unresolved_errors'],
        'paid_seed_bound_consumed_without_replaying_its_gate':True}
    return result


class CompleteMeanTail:
    # These source-bound algebraic functions operate on the real old model
    # and its original literal data. No old object/class/global is patched.
    _old_germs = paid.CurrentModelTailAnchor._old_germs
    _old_budget = paid.CurrentModelTailAnchor._old_budget
    _reference_scaled = paid.CurrentModelTailAnchor._reference_scaled
    _gaussian = paid.CurrentModelTailAnchor._gaussian

    def __init__(self,joint,data,natural_terminal,source_contract_json,source_contract_sha256):
        bounds.public_only()
        joint.guard()
        self.joint,self.model,self.data = joint,joint.owned.original,data
        self.response = joint.seed_response.copy()
        self.indices = []
        self.contract_sha = source_contract_sha256
        if hashlib.sha256(source_contract_json.encode()).hexdigest()!=source_contract_sha256:
            raise ValueError('complete actual source contract bytes differ')
        self.contract = json.loads(source_contract_json)
        definition = json.loads(joint.identity.mathematical_field_json)
        expected = {
            'target_sha256':joint.identity.target_sha256,
            'response_model_sha256':joint.owned.response_model_sha256,
            'reconstruction_source_sha256':self.model.original_reconstruction_receipt['reconstruction_source_sha256'],
            'true_inner_definition_sha256':paid.json_sha(definition['accurate_inner_tail_definition']),
            'true_germ_choice':'same_R600_accurate_infinite_germs_with_all_source_errors_accounted',
            'original_inner_phase':0}
        if any(self.contract.get(key)!=value for key,value in expected.items()):
            raise ValueError('same whole original tail/reference identity required')
        rows = self.contract.get('source_error_accounting')
        if not isinstance(rows,dict) or set(rows)!=set(paid.ERROR_CATEGORIES):
            raise ValueError('all original source-error categories must remain explicit')
        self.unresolved = []
        for key,row in rows.items():
            if (not isinstance(row,dict) or not row.get('evidence')
                    or row.get('status') not in ('unresolved','covered_by_supplied_exact_source_enclosures')):
                raise ValueError('each original source error requires its actual status')
            if row['status']=='unresolved':
                self.unresolved.append({'category':key,'evidence':row['evidence']})
        if ([int(mode.mode) for mode in self.model.old.modes]!=list(range(2,23,2))
                or list(map(int,self.model.old.column_modes[:10]))!=list(range(4,23,2))
                or self.model.amplitude!=1e-5 or self.model.old.args.height_saturation!=.15):
            raise ValueError('all old true germs and the same fixed amplitude/canonical field required')
        self.seed_anchor = _seed_anchor(joint,natural_terminal,data)
        self.identity = {
            'target_sha256':joint.identity.target_sha256,
            'response_model_sha256':joint.owned.response_model_sha256,
            'response_sha256':SEED_RESPONSE_SHA,'cap_radius':float(joint.base.RC),
            'mouth_radius':float(data['r'][0]),'parameter_indices':[]}
        self.rc,self.ell,self.A = I(11)/50,I(1)/5,I(4)/5
        self.mouth = I(float(data['r'][0]))
        uu = self.ell/(self.mouth-self.rc)
        if uu.lo < 108:
            raise ArithmeticError('same complete true cap-to-mouth window is required')
        self.U = I(uu.lo)
        self.W_upper = bounds.upper(self.A*bounds.exp_i(-self.U))
        support_left = min(float(joint.driver.weak.BULK_LEFT),
            float(joint.compact.PATCH_KNOTS[0][0]),float(joint.driver.complete.CORE_LEFT),
            float(joint.core_lift_left),float(joint.policy['mean_plateau_left']),.53)
        if self.mouth.hi >= support_left or self.mouth.hi > joint.tail_left:
            raise ArithmeticError('some retained non-tail support now meets the true tail')
        self.seed_ratio,self.raw_ratio,self.germ_receipts = self._old_germs()
        self.gaussian_columns = {}
        self.amplitude = I(1)/100000
        self.reference_scaled = self._reference_scaled()
        self.seed_angular_budget = self._budget(self.response)
        self.mean_gaussian = {
            k:bounds.gaussian_column_bounds(
                rc=self.rc,ell=self.ell,A=self.A,mouth=self.mouth,
                denominator=paid.literal_interval(joint.owned.policy['tail_gaussian_denominator']),
                cutoff_left=paid.literal_interval(joint.tail_left),
                cutoff_right=paid.literal_interval(joint.tail_right),degree=k,mode=1)
            for k in range(4)}
        # Only the radial threejet inequalities above are used. Their
        # formulas are independent of this helper's positive mode argument;
        # no angular j=1 function is added to the actual mean.
        self.provenance = joint.guard()
        self.source_snapshot = paid.CurrentModelTailAnchor._snapshot(self)
        self.seed_integral_bound = paid.literal_interval(
            self.seed_anchor['absolute_error_bounds_or_unresolved_radii'][0])
        self.seed_lambda_bound = paid.supplied_interval(
            self.seed_anchor['conditional_whole_tail_mean_branch']['lambda_radius_upper'])
        self.Elo = paid.supplied_interval(self.contract['whole_reference_E_lower_bound'])
        self.Ehi = paid.supplied_interval(self.contract['whole_reference_E_upper_bound'])
        COUNTS['complete_source_bound_new_mean_tail_models'] += 1

    def _budget(self,response):
        budgets = [self._old_budget(j,paid.absolute(self.amplitude*paid.literal_interval(float(response[i]))))
                   for i,j in enumerate(range(4,23,2))]
        m = self.model
        for mode_index,j in enumerate(m.modes):
            for basis_index,k in enumerate(m.tail_degrees):
                index = m.tail_start+mode_index*len(m.tail_degrees)+basis_index
                coefficient = paid.absolute(self.amplitude*paid.literal_interval(float(response[index])))
                budgets.append(bounds.gaussian_response_budget(self._gaussian(int(j),int(k)),coefficient))
        COUNTS['all_actual_angular_tail_coefficients_in_new_bounds'] += 106
        return bounds.add_budgets(budgets)

    def evaluate(self,response):
        bounds.public_only()
        self.joint._check(response)
        if (self.joint.guard()!=self.provenance
                or paid.CurrentModelTailAnchor._snapshot(self)!=self.source_snapshot):
            raise ValueError('true mean-tail source changed after binding')
        z = self.joint.angular_response(response)
        actual = self._budget(z)
        difference = self._budget(z-self.joint.seed_response)
        coeff = np.asarray(response)[self.joint.mean_start:]
        mean_three = [I(0),I(0),I(0)]
        mean_scaled = [I(0),I(0),I(0)]
        first = 61+28
        for k in range(4):
            coefficient = paid.absolute(self.amplitude*paid.literal_interval(float(coeff[first+k])))
            column = self.mean_gaussian[k]
            for d in range(3):
                mean_three[d] += coefficient*column['absolute_threejet_upper'][d]
                mean_scaled[d] += coefficient*column['over_W_threejet_upper'][d]
        mean_three = list(map(bounds.upper,mean_three))
        mean_scaled = list(map(bounds.upper,mean_scaled))
        Ar,Aq,At = [bounds.upper(self.reference_scaled[key]+actual['scaled'][key]
                                   +self.seed_angular_budget['scaled'][key])
                    for key in ('r','q','t')]
        P = bounds.upper(1+self.seed_lambda_bound+mean_scaled[1]+Ar)
        beta2 = 1-(self.W_upper*Aq/self.rc)**2
        bounds.positive(beta2)
        beta = bounds.sqrt_i(beta2)
        u2 = self.Elo-self.W_upper**2*P**2/beta2
        Nlo = 1-self.W_upper**2*P*At/(self.rc*beta**3)
        Nhi = 1/beta+self.W_upper**2*P*At/(self.rc*beta**3)
        bounds.positive(u2,Nlo)
        u = bounds.sqrt_i(u2)
        # A Lipschitz change from the fixed seed uses the whole same-E
        # energy component. It never solves a trial root or divides by c0.
        ep = (self.Ehi*At+self.mouth*P)/(u**3*self.rc*beta**3)
        et = P/(u*self.rc*beta**3)
        eq = (Aq/(u*self.rc**2*beta**3)
              +3*self.W_upper**2*P*At*Aq/(u*self.rc**3*beta**5)
              +Nhi*self.W_upper**2*P**2*Aq/(u**3*self.rc**2*beta**4))
        Fbound = bounds.upper(self.W_upper**2*(
            ep*(mean_scaled[1]+difference['scaled']['r'])
            +eq*difference['scaled']['q']+et*difference['scaled']['t']))
        COUNTS['actual_unsolved_mean_tail_evaluations'] += 1
        COUNTS['actual_new_mean_Gaussian_coefficients_included'] += 4
        result = {
            'joint_model_sha256':self.joint.model_sha256,
            'same_target_sha256':self.joint.identity.target_sha256,
            'actual_response_sha256':paid.json_sha(np.asarray(response).tolist()),
            'fixed_seed_response_sha256':SEED_RESPONSE_SHA,
            'fixed_seed_paid_FINAL_sha256':SEED_FINAL_SHA,
            'true_cap_radius':self.rc,'true_numerical_mouth':self.mouth,
            'complete_angular_response_budget':actual,
            'complete_angular_difference_from_fixed_seed_budget':difference,
            'actual_new_mean_absolute_threejet_upper':mean_three,
            'actual_new_mean_over_W_threejet_upper':mean_scaled,
            'actual_mean_height_cap_to_mouth_absolute_bound':bounds.upper(self.seed_integral_bound+mean_three[0]),
            'whole_tail_b_over_r_squared_lower':beta2,
            'whole_tail_u_squared_lower':u2,'whole_tail_N_lower':Nlo,
            'whole_tail_actual_turning_F_absolute_bound':Fbound,
            'all94_mean_columns_accounted':True,
            'mean_columns_zero_here_by_true_support':90,
            'mean_Gaussian_degree_list':[0,1,2,3],
            'scalar_helper_mode1_not_added_to_actual_angular_field':True,
            'new_trial_mean_root_or_lambda_box_consumed':False,
            'old_source_error_accounting':self.contract['source_error_accounting'],
            'unresolved_original_source_errors':self.unresolved,
            'new_continuous_G_and_full_S_tail_errors_enclosed':False,
            'new_continuous_G_and_full_S_tail_errors_status':
                'unresolved; no zero assigned and no complete metric certificate claimed',
            'conditional_on_all_original_declared_source_enclosures':bool(self.unresolved),
            'complete_new_tail_consumer_counts':dict(COUNTS),
            'underlying_old_source_bound_arithmetic_counts':dict(paid.COUNTS),
            'underlying_true_Gaussian_and_infinite_germ_counts':dict(bounds.COUNTS),
            'overlapping_counts_not_disjoint_costs':True,
            'whole_surface_metric_or_README_certified':False}
        return paid.tree_intervals(result)
