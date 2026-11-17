#!/usr/bin/env python3
"""Read-only binding of an actual raw-core state to its declared true atlas.

No width, lambda, amplitude, control, profile or material length is overridden.
The CLI inspects metadata only.  The callable load_actual_integral function
additionally connects the original accepted-state reader to the general
true-integral oracle; it is intended for the next actual accepted candidate.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np

from generic_raw_core_intervals import (
    GeneralExactRawM3Core, fixed_atlas_identity, literal_structure, RAW_KIND, RAW_PATH,
)
from integral_core_intervals import pi_interval
from m3_integral_prefix import RAW_ROUND, _same_recorded_sources, sha


SETTINGS = {'halfwidth', 'transition', 'control_transition', 'homotopy', 'center',
            'bimodal_eta', 'lock_fundamental', 'coefficient_precision', 'positivity_grid_max'}
PHYSICAL_CORE_SETTINGS = ('halfwidth', 'transition', 'control_transition', 'homotopy',
                          'center', 'bimodal_eta', 'lock_fundamental')
RAW_SOURCE_NAMES = {'plateau_core.py', 'large_radius_local_core.py', 'fixed_large_radius_core.py',
                    'complementary_moment_basis.py', 'moment_interval_bounds.py',
                    'tight_moment_interval_bounds.py', 'exact_core_lift.py',
                    'exact_lift_parameter_jac.py', 'analytic_adaptive_core_jac.py'}


def encoded_hash(value):
    encoded = json.dumps(literal_structure(value), sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(encoded).hexdigest()


def inspect_actual_checkpoint(path, library=RAW_ROUND):
    """Complete original acceptance plus actual source/parameter conventions."""
    path, library = Path(path).resolve(), Path(library).resolve()
    record = json.load(gzip.open(path, 'rt'))
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'resume_m3'))
    from couple_m3_smallcut_secant import accepted_anchor
    accepted_anchor(record, path)
    config = record['config']
    if (config['base_mode'] != 3 or config.get('core_kind') != RAW_KIND
            or record.get('core_control_path') != RAW_PATH or not config.get('exact_core_lift')):
        raise ValueError('Expected a complete accepted raw m3 integral-core checkpoint')
    settings = record['core_round_settings']
    if set(settings) != SETTINGS:
        raise ValueError('Unreviewed physical/core numerical setting convention')
    if (settings['center'] != math.pi/3 or settings['bimodal_eta'] != 0.
            or settings['lock_fundamental'] is not True):
        raise ValueError('Expected the even eta=0, pi/3-centered, locked-primary core')
    a, bp, bc = (F(str(settings[k])) for k in ('halfwidth', 'transition', 'control_transition'))
    if not (0 < a < a+bp < pi_interval()[0]/3 and a < a+bc < pi_interval()[0]/3):
        raise ValueError('The actual declared widths do not fit their reflection half-sector')
    if not 0 <= settings['homotopy'] <= 1:
        raise ValueError('Invalid recorded lambda')
    if bool(config.get('exact_circle_core')) != (settings['homotopy'] == 1):
        raise ValueError('The circle flag and actual lambda disagree')
    M = config['modes']
    parameters = np.asarray(record['parameters'], dtype=np.float64)
    scales = np.asarray(record['central_correction_scales'], dtype=np.float64)
    if parameters.shape != (M,) or scales.shape != (M-1,):
        raise ValueError('The complete physical control vector is missing')
    controls = parameters[1:]*scales
    if not np.all(np.isfinite(controls)) or not np.all(np.isfinite(parameters)):
        raise ValueError('Nonfinite recorded physical state')
    qa, qg = record['actual_primary_amplitude'], record['gauge_amplitude']
    if not (math.isfinite(qa) and qa > 0 and math.isfinite(qg) and qg > 0):
        raise ValueError('Invalid actual/gauge amplitudes')
    if not config['fixed_metric'] and qa != qg:
        raise ValueError('The design amplitude convention changed')
    sources = sorted(library.glob('*.py'))
    if {p.name for p in sources} != RAW_SOURCE_NAMES:
        raise ValueError('The reviewed raw-core source inventory changed')
    _same_recorded_sources(record, sources)
    core_definition = dict(base_mode=3, core_kind=RAW_KIND, core_control_path=RAW_PATH,
                           settings={k: settings[k] for k in PHYSICAL_CORE_SETTINGS})
    return record, controls, core_definition, {str(p): sha(p) for p in sources}


def bind_actual_integral(checkpoint, *, mode, atlas_anchor=None,
                         require_lambda_one=False, library=RAW_ROUND):
    """Choose a new physical anchor explicitly or retain the earlier anchor.

    New-design mode uses the candidate itself.  Refinement mode requires
    the original accepted anchor and enforces both the intrinsic metric
    identity and the physical raw-core family.  Unknown q/c values may
    change under a fixed-metric solve; their complete actual values are
    retained separately and never borrowed from a previous certificate.
    """
    checkpoint = Path(checkpoint).resolve()
    record, controls, family, sources = inspect_actual_checkpoint(checkpoint, library)
    if require_lambda_one and record['core_round_settings']['homotopy'] != 1:
        raise ValueError('The caller requires an actual lambda-one terminal state')
    if mode == 'new-design':
        if atlas_anchor is not None:
            raise ValueError('New-design mode anchors to this terminal state, not an earlier design')
        anchor, anchor_path = record, checkpoint
        common_family = None
    elif mode == 'fixed-metric-refinement':
        if atlas_anchor is None:
            raise ValueError('Fixed-metric refinement requires its original accepted atlas anchor')
        if record['config']['fixed_metric'] is not True:
            raise ValueError('The candidate was not solved with its physical metric frozen')
        anchor_path = Path(atlas_anchor).resolve()
        anchor, _, anchor_family, anchor_sources = inspect_actual_checkpoint(anchor_path, library)
        if literal_structure(family) != literal_structure(anchor_family):
            raise ValueError('A core family parameter changed; declare a new design explicitly')
        if record['config']['modes'] < anchor['config']['modes']:
            raise ValueError('This refinement binding does not call a lower mode count an enrichment')
        if sources != anchor_sources:
            raise ValueError('The core source implementation changed and needs a new interface review')
        common_family = True
    else:
        raise ValueError('Declare new-design or fixed-metric-refinement explicitly')
    identity = fixed_atlas_identity(record, anchor_record=anchor)
    nominal_cut = dict(radius=anchor['physical_tail_parameters']['rCut'],
                       backgroundSlope=anchor['physical_tail_parameters']['wCut'])
    binding = dict(mode=mode, checkpoint_sha256=sha(checkpoint),
        atlas_anchor_sha256=sha(anchor_path), atlas_anchor_path=str(anchor_path),
        intrinsic_metric_identity_sha256=identity['identity_sha256'],
        fixed_core_family_identity_sha256=encoded_hash(family),
        actual_core_settings=dict(record['core_round_settings']),
        actual_q_exact=str(F.from_float(float(record['actual_primary_amplitude']))),
        gauge_q_exact=str(F.from_float(float(record['gauge_amplitude']))),
        full_physical_controls_exact=[str(F.from_float(float(v))) for v in controls],
        original_solver_actual_tail_acceptance_checked=True,
        complete_metric_gate_inferred_from_acceptance=False,
        exact_circle=record['core_round_settings']['homotopy'] == 1,
        fixed_core_family_checked=common_family,
        core_projection_order_J=record['config']['modes'],
        previous_q_or_controls_reused=False, physical_settings_overridden=False,
        actual_frozen_profile=record['frozen_profile'],
        material_length=anchor['meridian_length'], nominal_physical_cut=nominal_cut,
        derived_source_cut_is_not_an_independent_physical_input=True,
        round_sources_sha256=sources,
        raw_library_manifest_sha256=sha(Path(library)/'manifest.json'),
        unresolved=['No actual field is decoded by this metadata binding.',
                    'The callable loader must still verify the source topic/short bridge/port and chunked field.',
                    'All q/c-dependent continuous core and map bounds need this terminal state as input.',
                    'A matching metric/core family does not establish convergence, phase-range identity, closure or reach.'])
    return record, anchor, binding


def load_actual_integral(source_topic, short_bridge, checkpoint, port_path, *, mode,
                         atlas_anchor=None, require_lambda_one=False, angular=512):
    """Use the complete actual checkpoint as recorded, without design overrides."""
    record, anchor, binding = bind_actual_integral(checkpoint, mode=mode,
        atlas_anchor=atlas_anchor, require_lambda_one=require_lambda_one)
    from m3_integral_prefix import load_integral_prefix
    from prefix_true_profile import TruePrefix
    loaded, obj, flow, sol, raw = load_integral_prefix(source_topic, short_bridge,
                                                     checkpoint, port_path, angular)
    if literal_structure(loaded['core_round_settings']) != literal_structure(record['core_round_settings']):
        raise ValueError('The actual-state reader changed the declared core')
    expected_controls = [float(F(v)) for v in binding['full_physical_controls_exact']]
    if list(obj._core.corrections) != expected_controls:
        raise ValueError('The actual-state reader changed a physical control')
    if obj._core.support_amplitude != record['actual_primary_amplitude']:
        raise ValueError('The actual-state reader changed q')
    oracle = GeneralExactRawM3Core(obj._core, obj.integral_reader_provenance)
    cut = binding['nominal_physical_cut']
    atlas = TruePrefix(anchor['frozen_profile'], cut, anchor['meridian_length'])
    binding['actual_field_and_general_oracle_loaded'] = True
    return loaded, obj, flow, sol, raw, oracle, atlas, binding


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--mode', choices=('new-design', 'fixed-metric-refinement'), required=True)
    p.add_argument('--atlas-anchor', type=Path)
    p.add_argument('--require-lambda-one', action='store_true')
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    _, _, binding = bind_actual_integral(args.checkpoint, mode=args.mode,
        atlas_anchor=args.atlas_anchor, require_lambda_one=args.require_lambda_one)
    here = Path(__file__).resolve().parent
    paths = [Path(__file__), here/'generic_raw_core_intervals.py', here/'m3_integral_prefix.py',
             here/'integral_core_intervals.py', here/'prefix_true_profile.py',
             here.parent/'resume_m3/couple_m3_smallcut_secant.py']
    result = dict(scope=__doc__, command=sys.argv, binding=binding,
        source_sha256={str(p.resolve()): sha(p) for p in paths}, metadata_only=True,
        source_field_decodes=0, true_core_integral_evaluations=0, bvp_solves=0,
        metric_audits_or_boxes=0, actual_lambda_one_end_to_end_validation=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k: binding[k] for k in ('mode', 'intrinsic_metric_identity_sha256',
        'fixed_core_family_identity_sha256', 'actual_q_exact', 'gauge_q_exact',
        'core_projection_order_J', 'material_length', 'exact_circle')}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
