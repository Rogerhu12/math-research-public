#!/usr/bin/env python3
"""Independent reconstruction of the complete frozen nine-control scalar.

This is a new same-metric identity, never a v3/v4 relabel.  The nested v3
specification remains the actual original three-control base definition.
All nine final coefficients, supports, stored widths, and both finite
assembly paths of the published nine-control full112 adapter are retained.
There are zero active controls and zero fixed core targets.  No future
accepted field, parameter vector, lambda, native response or run is supplied.
Version2 additionally binds the genuine nine-control H(s) producer as itself;
its original endpoint receipt is provenance, not a new450 acceptance/cache.
The published v1 sources and both finite scalar evaluator paths are unchanged.
Scientific reconstruction is public repository Actions only.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
import os
from pathlib import Path
import struct

HERE = Path(__file__).resolve().parent
SCHEMA = 'frozen-nine-control-complete-same-metric-scalar-v2'
FIELD_SCHEMA = 'nine-control-all-frozen-same-metric450-complete-physical-DN-v2'
DESIGN_SCHEMA = 'nine-control-three-active-nonzero112-complete-physical-DN-v1'
HEIGHT_DESIGN_SCHEMA = 'nine-control-height-path-three-active-nonzero112-complete-physical-DN-v1'
ENTRY_NAME = 'geometry_20261115_nine_control_same_metric_full112_v2.py'
DESIGN_NAMES = {
    DESIGN_SCHEMA: 'geometry_20261115_nine_control_full112.py',
    HEIGHT_DESIGN_SCHEMA: 'geometry_20261115_nine_control_height_continuation_full112.py',
}
PARAMETER_ORDER = ['p1', 'p2', 'p3', 'theta1', 'theta2', 'theta3', 'eta1', 'eta2', 'eta3']
SOURCE_PINS = {
    'geometry_20261115_nine_control_height_continuation_full112.py': '0433e1014a4d55ca52554ec5b17e9afa1d01a3b8e376d2afda890b26c35aa924',
    'geometry_20261115_original_tail_height_path.py': 'e830a1679908cdc0cdd8c1ecd5663bbf6b82b24a3d52e44cf678aedc227eee48',
    'geometry_20261115_nine_control_full112.py': '00e4d2c3413cfa6c1df915b9d85050bf375ab88c04e8756149d4ea0533ef3bd8',
    'geometry_20261115_small_core_nine_control_family.py': '086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629',
    'geometry_20261114_lifted_modes_profile.py': '13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5',
    'geometry_20261114_prefix_controls_profile.py': 'f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24',
    'geometry_20261114_full_scalar_profile.py': '8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b',
    'geometry_20261114_full_dn_augmented.py': 'f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e',
}


def actions_only():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Reconstruct and evaluate the frozen scalar only in public repository Actions')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def digest_valid(value):
    return (isinstance(value, str) and len(value) == 64
            and all(c in '0123456789abcdef' for c in value))


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, allow_nan=False).encode('utf-8')


def canonical_sha(value):
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def words(values):
    result = []
    for value in values:
        if type(value) not in (int, float) or not math.isfinite(value):
            raise ValueError('Use actual finite real binary64 scalar coefficients')
        result.append(struct.pack('<d', float(value)).hex())
    return result


def checked_sources():
    actions_only()
    result = {name: sha(HERE/name) for name in SOURCE_PINS}
    if result != SOURCE_PINS:
        raise ValueError('The original nine-family, full112 or literal scalar construction differs')
    result[Path(__file__).name] = sha(__file__)
    return result


def finite_assembly_contract():
    return dict(
        schema='published-nine-full112-two-finite-scalar-paths-v1',
        full112_source_sha256=SOURCE_PINS['geometry_20261115_nine_control_full112.py'],
        family_source_sha256=SOURCE_PINS['geometry_20261115_small_core_nine_control_family.py'],
        augmented_flow_source_sha256=SOURCE_PINS['geometry_20261114_full_dn_augmented.py'],
        point_path='00e4 active_profile.ThreeActiveView.profile(s, fixed_p1_p2_p3)',
        batch_path='original AugmentedFlow.scalar_jets(x, repeat(fixed_p1_p2_p3[:,None], len(x), axis=1))',
        frozen_base_path='original base_jet then theta2,theta1,theta3 then eta1,eta2,eta3; original zero-skips retained',
        even_control_path='point uses original control_jets @ p; batch uses original einsum(mjk,km->mj)',
        original_search_even_first_path_substituted=False,
        no_new_zero_control_einsum_or_zero_addition=True,
        every_literal_original_support_and_width_retained=True,
        bitwise_equality_across_runtimes_or_different_batch_layouts_claimed=False)


def reconstruct_nine_design(d, specification, accepted=None):
    """Rebuild the real nested definition, then verify its complete nine identity."""
    actions_only()
    checked_sources()
    family = d.family
    if (specification.get('schema') != family.SCALAR_SCHEMA
            or specification.get('parameter_order') != PARAMETER_ORDER
            or specification.get('profile_source_sha256') != SOURCE_PINS[Path(family.__file__).name]
            or specification.get('field_modes') != 112 or specification.get('tail_modes') != 112):
        raise ValueError('Consume the complete original nine scalar, not an older re-labelled schema')
    parameters = specification.get('frozen_design_parameters')
    if not isinstance(parameters, list) or len(parameters) != 9:
        raise ValueError('Retain all nine actual final scalar coefficients')
    parameter_words = words(parameters)
    nested = specification['original_three_parameter_specification']
    if (nested.get('field_modes') != 112 or nested.get('tail_modes') != 112
            or nested.get('base_prefix_M') != 96
            or words(nested.get('frozen_design_parameters', [])) != parameter_words[:3]
            or nested.get('accepted_prefix_sha256') != family.EXPECTED['accepted']):
        raise ValueError('The nested original three-control geometry or source identity differs')
    if accepted is not None:
        if (accepted.get('M') != 96 or accepted.get('N') != 1024
                or canonical_bytes(nested['base_prefix_geometry']) !=
                   canonical_bytes(accepted['fixed_scalar_profile']['geometry'])
                or words([nested['base_prefix_end']]) != words([accepted['mesh'][-1]])):
            raise ValueError('The original accepted96 scalar construction facts differ')
    from geometry_20261114_lifted_modes_profile import reconstruct_profile as original_reconstruct
    # The nested v3 is genuinely the old base definition; it is not the new
    # nine-control metric, a fabricated accepted field, or a native cache.
    original_frozen = original_reconstruct(nested)
    designed = family.NineControlProfile(original_frozen.designed)
    rebuilt = family.scalar_spec(designed, nested['complete_original_port'],
                                 parameters, nested['accepted_prefix_sha256'])
    if canonical_bytes(rebuilt) != canonical_bytes(specification):
        raise ValueError('The complete nine coefficients, definitions, support widths or sources differ')
    support_words = [
        dict(index=i, parameter=PARAMETER_ORDER[i],
             left_float64le=words([b.left])[0], right_float64le=words([b.right])[0],
             stored_width_float64le=words([b.width])[0])
        for i, b in enumerate(designed.bumps)]
    return designed, d.np.asarray(parameters, float), support_words


def scalar_identity_payload(specification, support_words):
    return dict(
        schema='complete-frozen-nine-scalar-and-finite-evaluator-identity-v1',
        original_nine_scalar_specification=copy.deepcopy(specification),
        frozen_nine_float64le=words(specification['frozen_design_parameters']),
        scalar_support_float64le=copy.deepcopy(support_words),
        finite_assembly=finite_assembly_contract())



def checked_height_provenance(d, record):
    """Validate saved identity only; do not read/replay its ephemeral path payload."""
    if (not isinstance(record, dict)
            or record.get('original_00e4_adapter_baseline_sha256') !=
               SOURCE_PINS['geometry_20261115_nine_control_full112.py']
            or record.get('height_path_helper_sha256') !=
               SOURCE_PINS['geometry_20261115_original_tail_height_path.py']
            or record.get('height_path_policy') != d.original_height_path.POLICY
            or record.get('same_original_tail_worker_for_height_path_FD_fullDN_and_final_audit') is not True
            or record.get('intermediate_height_convergence_not_full_DN_acceptance') is not True):
        raise ValueError('The actual height-path producer/helper/policy identity differs')
    receipt = record.get('completed_height_path_status')
    if (not isinstance(receipt, dict)
            or receipt.get('file') != 'height-path/height-path-status.json'
            or type(receipt.get('bytes')) is not int or receipt['bytes'] <= 0
            or not digest_valid(receipt.get('sha256'))):
        raise ValueError('The bound accepted height-path producer must retain its actual endpoint receipt')
    return copy.deepcopy(record)


def height_provenance(d, binding):
    names = ('original_00e4_adapter_baseline_sha256', 'height_path_helper_sha256',
             'height_path_policy',
             'same_original_tail_worker_for_height_path_FD_fullDN_and_final_audit',
             'intermediate_height_convergence_not_full_DN_acceptance',
             'completed_height_path_status')
    return checked_height_provenance(d, {name: binding.get(name) for name in names})


def make_frozen_spec(d, specification, origin):
    designed, parameters, support_words = reconstruct_nine_design(d, specification)
    if not isinstance(origin, dict) or origin.get('schema') not in DESIGN_NAMES:
        raise ValueError('Name the actual original or height-path nine-design producer explicitly')
    producer_name = DESIGN_NAMES[origin['schema']]
    if (origin.get('source_sha256') != SOURCE_PINS[producer_name]
            or not digest_valid(origin.get('file_sha256'))
            or type(origin.get('file_bytes')) is not int or origin['file_bytes'] <= 0):
        raise ValueError('Bind the real originating nine-control complete-field bytes')
    source_binding = origin.get('producer_source_binding')
    expected_inputs = {key: d.family.EXPECTED[key]
                       for key in ('accepted', 'prepared', 'tail_anchor', 'tail_config')}
    if (not isinstance(source_binding, dict)
            or source_binding.get('consumed_source_sha256') !=
               d.parent_design_source_closures[origin['schema']]
            or source_binding.get('input_sha256') != expected_inputs):
        raise ValueError('The complete originating producer/source/input identity differs')
    if origin['schema'] == HEIGHT_DESIGN_SCHEMA:
        checked_height_provenance(d, origin.get('height_path_provenance'))
    elif 'height_path_provenance' in origin:
        raise ValueError('Do not attach a height-path identity to the original00e4 producer')
    identity = scalar_identity_payload(specification, support_words)
    return dict(
        schema=SCHEMA, frozen_design_scalar_profile=copy.deepcopy(specification),
        frozen_design_parameters=parameters.tolist(), parameter_order=PARAMETER_ORDER,
        frozen_parameter_indices=list(range(9)), active_parameter_indices=[],
        active_scalar_parameters=0, fixed_core_modes=0,
        field_modes=112, tail_modes=112, field_angular_quadrature=2048,
        base_prefix_M=96, design_field_modes=112,
        complete_original_port=copy.deepcopy(specification['original_three_parameter_specification']['complete_original_port']),
        origin_design_field=copy.deepcopy(origin),
        accepted_source_prefix_sha256=specification['original_three_parameter_specification']['accepted_prefix_sha256'],
        canonical_scalar_identity_sha256=canonical_sha(identity),
        canonical_json='UTF-8 json.dumps(sort_keys=True,separators=(comma,colon),ensure_ascii=False,allow_nan=False)',
        frozen_nine_float64le=identity['frozen_nine_float64le'],
        scalar_support_float64le=support_words,
        finite_assembly=identity['finite_assembly'],
        profile_source_sha256=sha(__file__), reconstruction_source_sha256=checked_sources(),
        canonical_material_metric='The unchanged ds^2+a(s;all nine final coefficients)^2*dtheta_material^2',
        scalar_coefficients_are_not_refrozen_from_empty_active_vector=True,
        new_field_acceptance_created=False,
        continuous_scalar_domain_or_C2_certificate_created=False)


class FrozenNineProfile:
    """No active controls; point and batch evaluator responsibilities stay distinct."""
    parameter_count = 0
    M = 112
    tail_modes = 112

    def __init__(self, d, designed, parameters, specification):
        self.d = d
        self.designed_nine = designed
        self.frozen_parameters = d.np.array(parameters, dtype=float, copy=True)
        self.frozen_parameters.setflags(write=False)
        self.three_active = d.full112.active_profile(d, designed, self.frozen_parameters[3:])
        self.specification = copy.deepcopy(specification)
        self.canonical_scalar_identity_sha256 = specification['canonical_scalar_identity_sha256']
        self.bumps = []
        self.end, self.knots = self.three_active.end, list(self.three_active.knots)
        self.cut, self.tail_parameters = self.three_active.cut, self.three_active.tail_parameters

    def __getattr__(self, name):
        return getattr(self.three_active, name)

    def base_jet(self, s):
        return self.d.np.asarray(self.three_active.profile(s, self.frozen_parameters[:3]))

    def control_jets(self, s):
        return self.d.np.zeros((3, 0))

    def profile(self, s, parameters=None):
        if parameters is not None and self.d.np.asarray(parameters).shape != (0,):
            raise ValueError('The complete nine scalar is already frozen; active parameters must be empty')
        return self.three_active.profile(s, self.frozen_parameters[:3])

    def description(self):
        result = dict(self.three_active.description())
        result.pop('three_active_design_search_is_not_same_g_refinement', None)
        result.update(scope=__doc__, scalar_schema=SCHEMA, adapter_schema=FIELD_SCHEMA,
            profile_source_sha256=sha(__file__), field_modes=112, tail_modes=112,
            scalar_parameters=0, active_parameter_count=0, complete_scalar_coefficient_count=9,
            fixed_core_modes=0, state_dimension=338, augmented_state_dimension=450,
            left_boundary_rows=226, separated_left_rows=338, right_boundary_rows=112,
            active_parameter_indices=[], frozen_parameter_indices=list(range(9)),
            frozen_design_parameters=self.frozen_parameters.tolist(),
            canonical_scalar_identity_sha256=self.canonical_scalar_identity_sha256,
            finite_scalar_assembly=finite_assembly_contract(),
            same_material_metric_refinement_interface=True,
            same_g_refers_to_origin_nine_design_not_accepted96=True)
        return result


def reconstruct_profile(d, specification, accepted=None):
    if specification.get('schema') != SCHEMA:
        raise ValueError('Use this explicit frozen-nine identity; no older schema fallback')
    design_spec = specification['frozen_design_scalar_profile']
    expected = make_frozen_spec(d, design_spec, specification['origin_design_field'])
    if canonical_bytes(expected) != canonical_bytes(specification):
        raise ValueError('The complete already-frozen nine scalar identity changed')
    designed, parameters, unused = reconstruct_nine_design(d, design_spec, accepted)
    return FrozenNineProfile(d, designed, parameters, specification)


def frozen_flow_class(d):
    """Retain every original field/J expression and the original batch scalar path."""
    original_class = d.AugmentedFlow
    np = d.np

    class FrozenNineFlow(original_class):
        def __init__(self, probe, profile, workers=1):
            if not isinstance(profile, FrozenNineProfile):
                raise TypeError('The 450-state flow requires the genuine frozen-nine profile')
            super().__init__(probe, profile, workers)
            self._original_three_scalar_flow = original_class(probe, profile.three_active, workers)
            if (self.n, self.M, self.k, self.dimension) != (338, 112, 0, 450):
                raise ValueError('Keep all physical338/core112 and no scalar-control rows')

        def scalar_jets(self, x, parameters):
            x, parameters = np.asarray(x, dtype=float), np.asarray(parameters)
            if parameters.shape != (0, len(x)):
                raise ValueError('Supply the true empty active-control matrix at every current node')
            fixed = np.repeat(self.profile.frozen_parameters[:3, None], len(x), axis=1)
            # No reassociation, search-family substitution or extra k=0 sum.
            return self._original_three_scalar_flow.scalar_jets(x, fixed)

    return FrozenNineFlow


def serialize(profile, port, parameters, accepted_sha256):
    if not isinstance(profile, FrozenNineProfile):
        raise TypeError('Write the genuine complete frozen-nine scalar owner')
    if (profile.d.np.asarray(parameters).shape != (0,)
            or accepted_sha256 != profile.specification['accepted_source_prefix_sha256']
            or canonical_bytes(port) != canonical_bytes(profile.specification['complete_original_port'])):
        raise ValueError('The source, port or empty active vector changed; never refreeze empty coefficients')
    return copy.deepcopy(profile.specification)


def original_acceptance_receipt(parent):
    if (parent.get('success') is not True or parent.get('status') != 0
            or not isinstance(parent.get('actual_tail'), dict)
            or not digest_valid(parent['actual_tail'].get('final_response_sha256'))):
        raise ValueError('Consume a genuine accepted complete full-DN field, not a candidate or failed native record')
    report = {}
    for key, bound in (('collocation_rms_max', 1e-6),
                       ('boundary_residual_max', 1e-11),
                       ('physical_frozen_control_RMS_max', 1e-6)):
        value = parent.get(key)
        if type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= bound:
            raise ValueError('The saved field does not report its original complete acceptance: '+key)
        report[key] = value
    report.update(actual_tail=copy.deepcopy(parent['actual_tail']),
        parent_tail_payload_reexecuted_or_used_as_new_native_cache=False,
        parent_original_final_acceptance_read_from_bound_actual_file=True,
        new_native_J_FD_full_DN_and_final_audit_still_required=True)
    return report


def freeze_parent(d, parent, parent_receipt, accepted):
    np = d.np
    if (not digest_valid(parent_receipt.get('sha256'))
            or type(parent_receipt.get('bytes')) is not int or parent_receipt['bytes'] <= 0):
        raise ValueError('Bind the whole actual complete parent file')
    acceptance = original_acceptance_receipt(parent)
    if (parent.get('M'), parent.get('N')) != (112, 2048):
        raise ValueError('This independent entry retains exactly M=T112/N2048')
    if parent.get('field_representation') != d.field_spec(112, 2048):
        raise ValueError('The complete physical/full-mean state representation differs')
    source_spec = parent['complete_scalar_profile']
    if canonical_bytes(parent['fixed_scalar_profile']['geometry']) != canonical_bytes(source_spec):
        raise ValueError('The two saved scalar identities do not agree')
    schema = parent.get('schema')
    if schema in DESIGN_NAMES:
        expected_producer = SOURCE_PINS[DESIGN_NAMES[schema]]
        binding = parent['nine_control_full112_implementation']
        expected_inputs = {key: d.family.EXPECTED[key] for key in ('accepted','prepared','tail_anchor','tail_config')}
        if (parent.get('source_sha256') != expected_producer
                or binding.get('source_sha256') != expected_producer
                or binding.get('schema') != schema
                or binding.get('input_sha256') != expected_inputs
                or parent.get('active_parameter_indices') != [0,1,2]
                or parent.get('frozen_parameter_indices') != [3,4,5,6,7,8]
                or parent.get('fixed_modes') != 3):
            raise ValueError('The actual original nine-design producer or all source identities differ')
        if binding.get('consumed_source_sha256') != d.parent_design_source_closures[schema]:
            raise ValueError('The complete actual nine-design producer source closure differs')
        designed, parameters, unused = reconstruct_nine_design(d, source_spec, accepted)
        if (words(parent.get('scalar_parameters', [])) != words(parameters[:3].tolist())
                or words(binding.get('actual_frozen_shape_coefficients', [])) != words(parameters[3:].tolist())):
            raise ValueError('Freeze all actual final p and all six unchanged shape coefficients')
        origin = dict(schema=schema, source_sha256=expected_producer,
            file_sha256=parent_receipt['sha256'], file_bytes=parent_receipt['bytes'],
            producer_source_binding=dict(
                consumed_source_sha256=copy.deepcopy(binding['consumed_source_sha256']),
                input_sha256=copy.deepcopy(binding['input_sha256'])))
        if schema == HEIGHT_DESIGN_SCHEMA:
            origin['height_path_provenance'] = height_provenance(d, binding)
        specification = make_frozen_spec(d, source_spec, origin)
        expected_dimension = 453
    elif schema == FIELD_SCHEMA:
        binding = parent['nine_control_same_metric450_implementation']
        if (parent.get('source_sha256') != sha(HERE/ENTRY_NAME)
                or binding.get('source_sha256') != sha(HERE/ENTRY_NAME)
                or parent.get('fixed_modes') != 0 or parent.get('active_scalar_parameters') != 0
                or parent.get('active_parameter_indices') != []
                or parent.get('frozen_parameter_indices') != list(range(9))
                or parent.get('scalar_parameters') != []
                or binding.get('consumed_source_sha256') != d.closure):
            raise ValueError('Continue only this explicitly accepted frozen-nine 450 implementation')
        specification = copy.deepcopy(source_spec)
        expected_dimension = 450
    else:
        raise ValueError('A different design, raw scalar recipe, or old v3/v4 field cannot be relabelled')
    profile = reconstruct_profile(d, specification, accepted)
    x = np.asarray(parent['mesh'], float)
    physical = np.asarray(parent['states'], float)
    physical_rhs = np.asarray(parent['rhs'], float)
    augmented = np.asarray(parent['augmented_states'], float)
    augmented_rhs = np.asarray(parent['augmented_rhs'], float)
    core = np.asarray(parent['core']['coefficients'], float)
    if (x.ndim != 1 or len(x) < 2 or x[0] != 0 or np.any(np.diff(x) <= 0)
            or abs(x[-1]-profile.end) > 1e-12
            or physical.shape != (len(x), 338) or physical_rhs.shape != physical.shape
            or augmented.shape != (len(x), expected_dimension)
            or augmented_rhs.shape != augmented.shape or core.shape != (112,)
            or not all(np.all(np.isfinite(v)) for v in
                       (x, physical, physical_rhs, augmented, augmented_rhs, core))):
        raise ValueError('Every parent node, full physical/core row and saved RHS is required')
    def raw(value):
        return np.asarray(value, dtype='<f8', order='C').tobytes()
    if raw(augmented[:, :338]) != raw(physical):
        raise ValueError('The saved physical rows are not the same complete parent state words')
    if expected_dimension == 453:
        if words(augmented[-1, 450:].tolist()) != words(profile.frozen_parameters[:3].tolist()):
            raise ValueError('The scalar specification is not the actual terminal active p')
    elif binding.get('canonical_scalar_identity_sha256') != profile.canonical_scalar_identity_sha256:
        raise ValueError('The own-schema frozen metric binding differs')
    initial = np.array(augmented[:, :450], copy=True)
    receipt = dict(parent_file=copy.deepcopy(parent_receipt),
        parent_schema=schema, parent_reported_original_acceptance=acceptance,
        original_design_origin=copy.deepcopy(profile.specification['origin_design_field']),
        source_path_receipt_is_bound_provenance_not_replayed_or_promoted_to_new_acceptance=True,
        parent_augmented_dimension=expected_dimension, new_augmented_dimension=450,
        all_parent_physical338_and_core112_words_preserved=True,
        parent_mesh_float64le_sha256=hashlib.sha256(raw(x)).hexdigest(),
        parent_physical_float64le_sha256=hashlib.sha256(raw(physical)).hexdigest(),
        retained_initial450_float64le_sha256=hashlib.sha256(raw(initial)).hexdigest(),
        dropped_active_control_rows=3 if expected_dimension == 453 else 0,
        all_nine_final_coefficients_frozen=True,
        parent_RHS_not_relabelled_as_fresh_fixed_metric_RHS=True,
        nodal_active_parameter_drift_not_inherited_as_varying_metric=True,
        all_112_core_rows_preserved_without_projection=True,
        same_metric_means_the_declared_final_nine_scalar_not_any_old_v3_v4=True)
    return profile, x, initial, receipt
